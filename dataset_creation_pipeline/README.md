## Folder - `dataset_creation_pipeline`

This folder includes script and notebooks for generating, processing, and uploading the Electrical Engineering NER dataset.

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
python dataset_creation_pipeline/01_dataset_creation.py
```

- Configure the total samples, batch size, and parallel API calls as needed.
- The script outputs CSV files with annotated NER data in a specified output directory.

### **Step 2: Convert CSVs to Hugging Face Dataset**

Open the Jupyter notebook - `02_csvs_to_hf_dataset.ipynb` in VS Code and follow the instructions to process the CSV files.

- Specify the input directory for the CSV files.
- Process the data and save it in the Hugging Face format.

### **Step 3: Upload to Hugging Face Hub**

Use the final notebook - `03_upload_to_hf_hub.ipynb` to upload the dataset.

- Ensure your Hugging Face credentials are configured.
- Customize the dataset card with metadata like description, tags, and citation.

