from langchain_google_vertexai import VertexAIEmbeddings
import os

# Set the path to your service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\egeha\\project\\.venv\\gemini_project\\gemini-quizzify-1-1e1d78dac83f.json"

"""
    Task: Initialize the EmbeddingClient class to connect to Google Cloud's VertexAI for text embeddings.
    
    The EmbeddingClient class should be capable of initializing an embedding client with specific configurations
    for model name, project, and location. Your task is to implement the __init__ method based on the provided
    parameters. This setup will allow the class to utilize Google Cloud's VertexAIEmbeddings for processing text queries.
    
    Steps:
    1. Implement the __init__ method to accept 'model_name', 'project', and 'location' parameters.
        These parameters are crucial for setting up the connection to the VertexAIEmbeddings service.
    
    2. Within the __init__ method, initialize the 'self.client' attribute as an instance of VertexAIEmbeddings
        using the provided parameters. This attribute will be used to embed queries.
    
    Parameters:
    - model_name: A string representing the name of the model to use for embeddings.
    - project: The Google Cloud project ID where the embedding model is hosted.
    - location: The location of the Google Cloud project, such as 'us-central1'.

    Note: The 'embed_query' method has been provided for you. Focus on correctly initializing the class.
"""

class EmbeddingClient:
    def __init__(self, model_name, project, location):
        """
        Initialize the VertexAIEmbeddings client with the given parameters.

        :param model_name: Name of the model to use for embeddings.
        :param project: Google Cloud project ID where the embedding model is hosted.
        :param location: Location of the Google Cloud project.
        """
        self.client = VertexAIEmbeddings(
            model=model_name,
            project=project,
            location=location
        )
    
    def embed_query(self, query):
        """
        Retrieve embedding for a single query.
        
        :param query: A text query to embed.
        :return: The embedding for the given query.
        """
        try:
            return self.client.embed_query(query)
        except AttributeError:
            print("Method embed_query not defined for the client.")
            return None
    
    def embed_documents(self, documents):
        """
        Retrieve embeddings for multiple documents.
        
        :param documents: A list of text documents to embed.
        :return: A list of embeddings for the given documents.
        """
        try:
            # Check if embed_documents method exists, else fallback to embed_query in a loop
            if hasattr(self.client, 'embed_documents'):
                return self.client.embed_documents([doc.page_content for doc in documents])
            else:
                return [self.client.embed_query(doc.page_content) for doc in documents]
        except AttributeError:
            print("Method embed_documents not defined for the client.")
            return None

if __name__ == '__main__':
    model_name = 'textembedding-gecko@003'
    project = 'gemini-quizzify-1'
    location = 'europe-west2'
    
    # Initialize the embedding client
    embedding_client = EmbeddingClient(model_name, project, location)
    
    # Test the embed_query method with a sample query
    vectors = embedding_client.embed_query("hello world!")
    if vectors:
        print(vectors)
        print('Successfully used the embedding client!')
