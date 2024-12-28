import pandas as pd
import json
from tqdm import tqdm
import os
from datetime import datetime
import asyncio

from openai import AsyncOpenAI
from dotenv import load_dotenv

from prompt.prompt import SYSTEM_PROMPT, USER_PROMPT

_ = load_dotenv()


async def get_single_response(client: AsyncOpenAI, model: str):
    """
    Get a single response from a LLM model.

    Args:
        client (AsyncOpenAI): The async client to use for the API call.
        model (str): The model to use for the API call.

    Returns:
        str: The response message from the model.
    """
    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT},
            ],
            response_format={"type": "json_object"},
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in API call: {e}")
        return None


async def get_batch_responses(
    batch_size: int, model: str, base_url: str = None, api_key: str = None
):
    """Get multiple responses in parallel"""
    client = AsyncOpenAI(base_url=base_url, api_key=api_key)
    tasks = [get_single_response(client, model) for _ in range(batch_size)]
    responses = await asyncio.gather(*tasks)
    return [r for r in responses if r is not None]  # Filter out failed responses


def parse_ner_json(json_string):
    """
    Parse the JSON output from a NER model into a dictionary of:
    - text: the original sentence
    - tokens: a list of tokens in the sentence
    - ner_tags: a list of NER tags corresponding to the tokens
    """
    data = json.loads(json_string)
    tokens = [ann["token"] for ann in data["annotations"]]
    tags = [ann["tag"] for ann in data["annotations"]]

    return {"text": data["sentence"], "tokens": tokens, "ner_tags": tags}


def save_batch(df_rows, batch_num, output_dir="ner_datasets"):
    """
    Saves a batch of NER data to CSV files in the specified output directory.

    Args:
        df_rows (list): A list of dictionaries, each containing 'text',
                        'tokens', and 'ner_tags' for NER data.
        batch_num (int): The batch number to include in the filenames.
        output_dir (str, optional): The directory to save the files. Defaults to 'ner_datasets'.

    Returns:
        tuple: A tuple containing:
            - df (DataFrame): A DataFrame of the raw NER data.
            - df_exploded (DataFrame): A DataFrame with one token per row.
    """

    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    df = pd.DataFrame(df_rows)

    raw_filename = f"{output_dir}/ner_dataset_raw_batch_{batch_num}_{timestamp}.csv"
    df.to_csv(raw_filename, index=False)

    df_exploded = pd.DataFrame(
        [
            {"sentence_id": idx, "text": row["text"], "token": token, "ner_tag": tag}
            for idx, row in df.iterrows()
            for token, tag in zip(row["tokens"], row["ner_tags"])
        ]
    )

    tokens_filename = (
        f"{output_dir}/ner_dataset_tokens_batch_{batch_num}_{timestamp}.csv"
    )
    df_exploded.to_csv(tokens_filename, index=False)

    print(f"Saved batch {batch_num} to:\n- {raw_filename}\n- {tokens_filename}")

    return df, df_exploded


async def collect_llm_responses(
    total_samples: int,
    model: str = "qwq:latest",
    base_url: str = None,
    api_key: str = None,
    batch_size: int = 25,
    parallel_calls: int = 10,
):
    """
    Collect a specified number of samples from a language model (LLM) in parallel.

    Args:
        total_samples (int): The total number of samples to collect.
        model (str, optional): The model to use for the API call. Defaults to "qwq:latest".
        base_url (str, optional): The base URL to use for the API call. Defaults to None.
        api_key (str, optional): The API key to use for the API call. Defaults to None.
        batch_size (int, optional): The number of samples to collect in each batch. Defaults to 25.
        parallel_calls (int, optional): The number of parallel batches to use. Defaults to 10.

    Returns:
        int: The total number of samples collected.
    """
    df_rows = []
    batch_num = 1

    # Calculate number of iterations needed
    num_iterations = (total_samples + batch_size - 1) // batch_size

    try:
        with tqdm(total=total_samples, desc="Collecting samples") as pbar:
            for _ in range(num_iterations):
                # Calculate how many samples we still need
                samples_needed = min(batch_size, total_samples - len(df_rows))

                # Split into parallel batches
                parallel_batches = (
                    samples_needed + parallel_calls - 1
                ) // parallel_calls

                for _ in range(parallel_batches):
                    current_batch_size = min(parallel_calls, samples_needed)
                    responses = await get_batch_responses(
                        current_batch_size,
                        model=model,
                        base_url=base_url,
                        api_key=api_key,
                    )

                    # Process successful responses
                    for response in responses:
                        if response:
                            try:
                                parsed = parse_ner_json(response)
                                df_rows.append(parsed)
                                pbar.update(1)
                            except Exception as e:
                                print(f"\nError parsing response: {e}")

                    samples_needed -= len(responses)

                # Save completed batch
                if len(df_rows) >= batch_size:
                    print(
                        f"\nReached {len(df_rows)} of {total_samples} samples. Saving batch {batch_num}..."
                    )
                    save_batch(df_rows[-batch_size:], batch_num)
                    batch_num += 1

    except KeyboardInterrupt:
        print("\nCollection interrupted by user")

    finally:
        # Save any remaining samples
        remaining = len(df_rows) % batch_size
        if remaining > 0:
            print(f"Saving remaining {remaining} samples...")
            save_batch(df_rows[-remaining:], batch_num)

        print(f"\nCollection completed. Total samples collected: {len(df_rows)}")
        return len(df_rows)


# Usage
if __name__ == "__main__":
    try:
        total_collected = asyncio.run(
            collect_llm_responses(
                total_samples=15000,  # Total samples to collect
                model="gpt-4o-mini",
                # base_url="http://localhost:11434/v1",
                # api_key="ollama",
                batch_size=100,  # Save every 100 samples
                parallel_calls=50,  # Make 50 API calls in parallel
            )
        )
        print(f"Successfully collected {total_collected} samples")
    except Exception as e:
        print(f"Collection stopped due to error: {e}")
