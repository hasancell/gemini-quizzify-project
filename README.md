# Gemini Quizzify Project

This project presents the Gemini Quizzify application, a tool designed to generate quizzes from documents and topics you provide. It incorporates various technologies, including Google Gemini, Vertex AI API, text embeddings, Google Service Account, Langchain, PDF loader, and Streamlit. This project is part of the challenges provided by Radical AI, and several contributions have been made to implement its various features.

## Overview

Gemini Quizzify aims to create engaging and informative quizzes based on user-provided documents and topics. The application uses advanced machine learning models for generating text embeddings and leverages Google's Gemini and Vertex AI APIs for document processing and quiz generation. The interface is built with Streamlit, making it interactive and user-friendly.

## Features

By running the provided script files, you can achieve the following functionalities:

1. **Document Processing with Google Gemini**: Efficiently process and extract relevant information from various documents using Google Gemini's robust capabilities.

2. **Text Embeddings with Langchain**: Generate high-quality text embeddings that capture the semantic meaning of the text, facilitating accurate quiz generation.

3. **Google Service Account Integration**: Securely authenticate and access Google's APIs using a Google Service Account, ensuring seamless integration and operation.

4. **PDF Loader for Document Ingestion**: Easily load and ingest documents in PDF format, preparing them for processing and quiz generation.

5. **Interactive User Interface with Streamlit**: Build a visually appealing and interactive user interface with Streamlit, enabling users to interact with the application effortlessly.

6. **Quiz Generation Based on User Input Topics**: Create customized quizzes tailored to the topics specified by the user, enhancing the relevance and engagement of the quizzes.

7. **Providing Detailed Explanations for Quiz Answers**: Offer comprehensive explanations for each quiz answer, helping users understand the reasoning behind the correct responses.

8. **Navigation Controls for the Quiz Interface**: Incorporate intuitive navigation controls within the quiz interface, allowing users to move through questions and review answers easily.

9. **Error Handling and Validation Mechanisms**: Implement robust error handling and validation mechanisms to ensure the smooth functioning of the application and provide meaningful feedback to users.

10. **Packaging and Deployment Considerations**: Consider various packaging and deployment options to facilitate easy distribution and deployment of the application in different environments.

## Getting Started

To run Gemini Quizzify, follow these steps:

1. **Install Dependencies**:
   - Ensure you have all the necessary dependencies installed by following the instructions in the `requirements.txt` file. Use the command `pip install -r requirements.txt` to install them.
   
2. **Launch the Application**:
   - Start the Streamlit application by running `streamlit run xxx.py` in your terminal, replacing `xxx` with the name of the script you want to execute.
   
3. **Interact with the Application**:
   - Follow the on-screen instructions to upload documents, specify topics, and generate quizzes. The user interface will guide you through each step of the process.

## License

This project is licensed under the MIT License. For more details, refer to the LICENSE file.

## Acknowledgments

This project builds upon the work done in [mission-quizify](https://github.com/radicalxdev/mission-quizify) by [radicalxdev]. We are grateful for their foundational contributions, which have been instrumental in the development of Gemini Quizzify.

- **[Radical AI](https://www.radicalai.org/)**: For providing the challenges and inspiration that led to the creation of this project.
- **[Streamlit](https://streamlit.io/)**: For developing a platform that enables the creation of user-friendly interfaces.
- **[Google Cloud Platform](https://cloud.google.com/)**: For offering APIs and services that are integral to the functioning of this project.
- **[Langchain](https://langchain.com/)**: For providing the technology needed to generate high-quality text embeddings.
