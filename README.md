# Electrical Engineering Named Entity Recognition (NER) Dataset Creation Pipeline

This repository contains scripts and notebooks for creating, processing, and uploading the **ElectricalNER** dataset, a NER dataset tailored for the electrical engineering domain. The pipeline is divided into three stages, each handled by a specific script or notebook.

---

## **Pipeline Overview**

### **1. Dataset Creation (`01_dataset_creation.py`)**

- **Purpose**: Generate annotated NER data by using a large language model (LLM).
- **Functionality**:
  - Sends structured prompts to an LLM to generate sentences and their corresponding NER annotations.
  - Saves the generated data in batches to CSV files.
- **Key Features**:
  - Asynchronous API calls for efficient batch processing.
  - Handles large-scale dataset generation with options for saving intermediate results.
- **Output**:
  - Raw CSV files containing sentence-level and token-level NER annotations.

### **2. Convert CSVs to Hugging Face Dataset (`02_csvs_to_hf_dataset.ipynb`)**

- **Purpose**: Process the CSV files into a Hugging Face-compatible dataset.
- **Functionality**:
  - Reads the raw CSV files generated in the previous step.
  - Structures the data into `DatasetDict` format with splits for training, validation, and testing.
  - Saves the dataset in Hugging Face's binary format for efficient loading.
- **Output**:
  - A Hugging Face Dataset (`.arrow`) ready for use with Hugging Face models and libraries.

### **3. Upload to Hugging Face Hub (`03_upload_to_hf_hub.ipynb`)**

- **Purpose**: Upload the processed dataset to the Hugging Face Hub for public sharing.
- **Functionality**:
  - Configures the Hugging Face `datasets` library.
  - Uses the Hugging Face API to create a dataset repository and upload the dataset files.
  - Includes metadata such as dataset card and license.
- **Output**:
  - The ElectricalNER dataset hosted on the Hugging Face Hub.

---

## **Environment Setup**

### **1. Clone the Repository**

```bash
git clone ner-electrical-engineering
cd ner-electrical-engineering
```

### **2. Create and Activate a Virtual Environment**

```bash
conda create -n ner_ee python=3.12
conda activate ner_ee
```

### **3. Install Dependencies**

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### **4. Configure API Keys**

Set up environment variables for OpenAI API Key and HuggingFace Access Token. Create a `.env` file in the root directory:

```
HF_TOKEN=<huggingface_access_token>
OPENAI_API_KEY=<your_openai_api_key>
```

---

## **File Details**

1. **`01_dataset_creation.py`**:

   - Script for generating NER dataset batches using an LLM.
   - Includes parsing and saving functionality.

2. **`02_csvs_to_hf_dataset.ipynb`**:

   - Notebook for converting raw CSVs into a structured Hugging Face dataset.

3. **`03_upload_to_hf_hub.ipynb`**:
   - Notebook for uploading the processed dataset to the Hugging Face Hub.

---  

## **Usage Instructions**

### **Step 1: Dataset Creation**

Run the Python script to generate the NER dataset.

```bash
python 01_dataset_creation.py
```

- Configure the total samples, batch size, and parallel API calls as needed.
- The script outputs CSV files with annotated NER data in a specified output directory.

### **Step 2: Convert CSVs to Hugging Face Dataset**

Open the Jupyter notebook and follow the instructions to process the CSV files:

```bash
jupyter notebook 02_csvs_to_hf_dataset.ipynb
```

- Specify the input directory for the CSV files.
- Process the data and save it in the Hugging Face format.

### **Step 3: Upload to Hugging Face Hub**

Use the final notebook to upload the dataset:

```bash
jupyter notebook 03_upload_to_hf_hub.ipynb
```

- Ensure your Hugging Face credentials are configured.
- Customize the dataset card with metadata like description, tags, and citation.

---

## **Limitations**

- The dataset is generated using GPT-4o-mini and may contain inaccuracies.
- Intended for research and educational purposes; not recommended for critical applications without validation.
- Contributions for refinement and expansion are welcome.

---

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

---

## **Contributing**

- Report issues or suggest improvements via GitHub.
- Contributions to expand or refine the dataset are highly encouraged.

---

## **Acknowledgments**

This project utilizes GPT-4o-mini for dataset generation and Hugging Face libraries for dataset processing and hosting.
