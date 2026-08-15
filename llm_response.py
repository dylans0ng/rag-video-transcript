import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import List, Dict, Any


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file.")

openai = OpenAI(api_key=api_key)

def generate_answer(question: str, retrieved_docs: List[str], 
                    retrieved_metadata: List[Dict[str, Any]],
                    model: str = 'gpt-4.1-mini'):
    """
    Returns a string.
    """
    
    # Clean and validate the user's question
    question = question.strip()

    if not question:
        raise ValueError("The question cannot be empty.")

    # Retrieval may return no documents
    if not retrieved_docs:
        return (
            "I could not find enough relevant information in the video "
            "transcript to answer that question."
        )

    # Each document should have a corresponding metadata dictionary
    if len(retrieved_docs) != len(retrieved_metadata):
        raise ValueError(
            "The number of retrieved documents must match the number "
            "of metadata records."
        )
        
    # Format each retrieved chunk into a readable context section
    context_parts = []

    for rank, (document, metadata) in enumerate(
        zip(retrieved_docs, retrieved_metadata),
        start=1
    ):
        # Skip empty transcript chunks
        if not document or not document.strip():
            continue

        chunk_number = metadata.get("chunk_number", "Unknown")
        video_name = metadata.get("video_name", "Unknown")
        source_file = metadata.get("source_file", "Unknown")

        formatted_chunk = f"""
            [Retrieved Chunk {rank}]
            Video: {video_name}
            Chunk Number: {chunk_number}
            Source File: {source_file}

            Transcript:
            {document.strip()}
            """.strip()

        context_parts.append(formatted_chunk)
        
    # All retrieved documents may have been empty
    if not context_parts:
        return (
            "I could not find enough relevant information in the video "
            "transcript to answer that question."
        )

    context = "\n\n---\n\n".join(context_parts)

    # SYSTEM PROMPT
    instructions = """
        You answer questions about a video using retrieved excerpts from its transcript.

        Follow these rules:
        1. Use only the information provided in the retrieved transcript context.
        2. Do not add facts based on outside knowledge.
        3. Cite supporting transcript excerpts using their source IDs, such as [S1].
        4. Cite only source IDs that appear in the retrieved context.
        5. Never invent or reuse a source ID from the example.
        6. End the response with a Sources section containing only the sources
   actually used.
        7. If the context does not contain enough information to answer the question,
        clearly say that the video does not provide enough information.
        8. Give a clear, direct, and concise answer.
        9. Do not claim that the video said something unless it is supported by the
        provided transcript context.
        
        # Example
        Question:
        How do I load a CSV file?

        Retrieved context:
        [Source S1]
        Video: Pandas Tutorial
        Source File: pandas_tutorial.mp4

        Transcript:
        You can load a CSV file into a DataFrame by using the pd.read_csv()
        function and passing the file path as an argument.

        Expected response:
        Use `pd.read_csv()` and pass the CSV file path into the function to load
        the data into a Pandas DataFrame.
        
        Sources:
        - S1: Pandas Tutorial (pandas_tutorial.mp4)
        
        # Important

        The example demonstrates formatting only. For the real response, use only
        the source IDs and information provided in the current retrieved context.
        """.strip()

    # USER PROMPT
    user_input = f"""
        Question:
        {question}

        Retrieved Transcript Context:
        {context}

        Answer the question using only the retrieved transcript context.
        """.strip()
        
    # Makes the API call using our system prompt and user prompt
    try:
        response = openai.responses.create(
            model=model,
            instructions=instructions,
            input=user_input
        )
    except Exception as error:
        raise RuntimeError(
            f"Failed to generate an answer with the OpenAI API: {error}"
        ) from error
        
    answer = response.output_text.strip()
    
    if not answer:
        raise RuntimeError("The OpenAI API returned an empty answer.")

    return answer   