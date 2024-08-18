# Gemini Quizzify Project

Gemini Quizzify is a robust project designed to generate quizzes from documents and subjects you provide. It incorporates technologies including Google Gemini, Vertex AI API, text embeddings, Google Cloud Platform (GCP), Langchain, PDF loader, and Streamlit. This project is provided by Radical AI, and several contributions have been made to implement its various features.

## Key features of the Project

By running the provided script files, you can achieve the following functionalities:

1. Load multiple PDF files simultaneously for batch processing.
2. Extract key information from PDFs and generate text embeddings with Langchain.
3. Implement a vector database with Chroma DB to efficiently access and organize embeddings.
4. Set up a chain implementation with setup_and_retrieval, prompt, and self.llm to optimize processing.
5. Integrate a web user interface to display the generated questions in an intuitive, interactive format, powered by Streamlit and GCP's Vertex AI LLM.
7. Generate multiple-choice questions through prompt design, tailored to the processed content and the desired subject.
8. Implement navigation controls in the quiz interface along with detailed explanations for each answer.

## Requirements

In order to run Gemini Quizzify, ensure that you have the following:

* **Python 3.10 or higher**
* **Access to a Google Cloud Platform Acccount**
* **Vertex AI API**
* **LangChain**
* **Streamlit**
* **Chroma DB**
*  **PyPDF**

## Getting Started

To run Gemini Quizzify, follow these steps:

1. **Clone the Repository**:
   - You can clone this repository using the following command: `git clone https://github.com/hasancell/gemini-quizzify-project.git`

2. **Create your Virtual Environment**:
   - Create a virtual environment. Use the command: `virtualenv venv` `source venv/bin/activate`

3. **Google Cloud Authentication with Vertex AI API**:
   - Ensure that you have Google Cloud account and authenticate your SDK with IAM User. You must create IAM user with necessary permissions to enable Vertex AI API. This is possible by downloading the credential JSON key file from GCP and setting it equal to an environment variable in your script. `GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-file.json"`

4. **Install Dependencies**:
   - You must have all the necessary dependencies installed by following the instructions in the `requirements.txt` file. Use the command `pip install -r requirements.txt` to install them.

5. **Launch the Application**:
   - Start the Streamlit application by running `streamlit run xxx.py` in your terminal, replacing `xxx` with the name of the script you want to execute. In this case, you should run the last task which is `streamlit run main.py`. This will open a new window on your default browser and navigate you to http://localhost:8501/ in order to access Streamlit Web UI.

6. **Interact with the Gemini Quizzify**:
   - Follow the on-screen instructions to upload documents, specify the subject, and generate a quiz. The user interface will guide you through each step of the process.

## License

This project is licensed under the MIT License. For more details, refer to the LICENSE file.

## Acknowledgments

This project builds upon the work done in [mission-quizify](https://github.com/radicalxdev/mission-quizify) by [radicalxdev]. I am grateful for their foundational contributions, which have been instrumental in the development of Gemini Quizzify.

- **[Radical AI](https://www.radicalai.org/)**: For providing the challenges and inspiration that led to the creation of this project.
- **[Streamlit](https://streamlit.io/)**: For developing a platform that enables the creation of user-friendly interfaces.
- **[Google Cloud Platform](https://cloud.google.com/)**: For offering APIs and services that are integral to the functioning of this project.
- **[Langchain](https://langchain.com/)**: For providing the technology needed to generate high-quality text embeddings.
