# README

## **Folder - `prompt`**

The `prompt` folder contains the file `prompt.py`, which defines the system and user prompts used for generating the NER dataset. These prompts are designed to elicit unique and diverse sentences that cover various aspects of electrical engineering, such as:

- Circuit design
- Testing and maintenance
- Installation and troubleshooting
- Research and development

### **Purpose**

While it's impossible to cover all potential sentence variations in the domain, the prompts are carefully crafted to ensure a wide range of contexts are included, making the dataset as representative as possible.

### **Usage**

- The `prompt.py` file is loaded by the dataset creation script (`01_dataset_creation.py`) to guide the LLM in generating annotated sentences.
- You can modify the prompts to extend or refine the dataset to better suit specific requirements.

