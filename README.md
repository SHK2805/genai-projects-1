# GenAI Projects

### Setup
* Run the `main.py` file to start the program
* Set the environment variables from the `.env` file at the start of the program
  * This contains the `API_KEY` for the OPENAI platform, ollama, huggingface. 
* Add the below at the beginning of the file you are running the program from
```python
from src.config.set_config import Config

config = Config()
if config.set():
    print("Environment variables set")
else:
    print("Environment variables NOT set")
```

### Projects List
#### 1. Webpage Reader
* The `Webpage Reader` project reads the text from a webpage, stores it in a vectordb
* Users can query the vectordb
* The code is written in `src/webpage_reader`

#### 2. Readers
* At the moment the `Readers` project reads the text from a file txt or PDF, stores it in a vectordb
* This can be extended to reading from other sources like webpage, images, audio, video, etc.
* Refer to the `Webpage Reader` section for more details
* The `Readers` project reads the text from a file txt or PDF, stores it in a vectordb
* Users can query the vectordb
* The code is written in `src/readers`
* The data for this is stored in the `data` folder
* The database files are stored in the `database` folder
* The structure of the code is split
```plaintext
root/
├── data/
│   ├── file.txt
│   └── file.pdf
├── database/
│   ├── txt_vector_store/
│   └── pdf_vector_store/
├── src/
│   ├── config/
│   ├── constants/
│   ├── readers/
│   │   ├── manager/
│   │   ├── platforms/
│   │   ├── services/
│   │   └── main_reader.py
│   └── utils/
├── main.py
└── README.md
```
* The `platforms` folder contains code to manage various platforms like OPENAI, HuggingFace, Ollama
* The application takes the file name and the platform name as input in `main_reader.py` 
* Below is the sample code
```python
file_path = "../../data/pyramids.txt"  # Update to the desired file
db_base_path = "../../database/"

# Initialize QAManager for file processing and retriever creation
vectorstore_manager = VectorStoreManager(file_path, db_base_path)

# Ollama
# Initialize PlatformManager for Ollama
platform_manager = PlatformManager(PlatformTypes.OPENAI)
llm = platform_manager.get_llm(openai_llm_model_name)
embedding = platform_manager.get_embedding(openai_embeddings_model_name)
```
* The data is then embedded and stored under the folder `database` using which the user can query the data


### Ollama
#### Installation
* Install the `Ollama` package using the below code in the commandline 
* To install Ollama on Windows, download the **OllamaSetup.exe** installer from the official website [Ollama](https://ollama.com/)
* Run it as administrator and follow the on-screen instructions. 
* Here's a more detailed breakdown:
  * Download the Installer: Go to the Ollama website and download the OllamaSetup.exe file. 
  * Run as Administrator: Right-click on the downloaded file and select "Run as administrator."
  * Follow the Installation Steps: The installer will guide you through the installation process. Click "Install" when prompted. 
  * Check for the Ollama Icon: Once the installation is complete, you'll find an Ollama icon in the system tray (bottom right of the desktop). 
  * Verify Installation: Open a terminal or command prompt and type `ollama` to confirm Ollama is installed and running correctly.
* To install Ollama in a specific folder on Windows, run the below code in the commandline
* Open Windows PowerShell as administrator
```commandline
<path to ollamaexe>\OllamaSetup.exe /DIR=<new ollama path>
.\OllamaSetup.exe /DIR=D:\ANYDIRECTORY
```
* To test if `Ollama` is installed correctly, run the below code in the commandline
```commandline
ollama --version
```
* Open the webpage [Ollama](http://localhost:11434/) to check if the installation is successful
* See the list of models available in the `Ollama` website from the [Ollama Models](https://github.com/ollama/ollama?tab=readme-ov-file#model-library) page
* Run the ollama model using the below code in the commandline
```commandline
ollama run llama3.2
```
#### Uninstallation
* To uninstall the `Ollama` package, run the below code in the commandline
* Open Windows PowerShell as administrator
```commandline
winget list
```
* Look for the process name of the `Ollama` package and run the below command
```commandline
winget uninstall Ollama.Ollama
```
* Delete the folder `C:\Users\<username>\.ollama`

#### Models
* By default, the models are stored in the below paths 
  * macOS: ~/.ollama/models 
  * Linux: /usr/share/ollama/.ollama/models 
  * Windows: C:\Users\%username%\.ollama\models
* We can change the path of the models by setting the environment variables `OLLAMA_MODELS_PATH` and `OLLAMA_MODELS` to the desired path
* To set the environment variables, follow the below steps 
  * Open Windows Settings. 
  * Go to System. 
  * Select About 
  * Select Advanced System Settings. 
  * Go to the Advanced tab. 
  * Select Environment Variables.... 
  * Click on New... 
  * And create a variables pointing to where you want to store the models (set a path for store models)
* Restart the computer to apply the changes