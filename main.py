from pathlib import Path
import audio_extracter # Milestone 1
import transcript_chunker # Milestone 2
import chroma_storage # Milestone 3
import llm_response # Milestone 6

# If the video transcript already exists, then we return the contents of the transcript
# If the video transcript does not exist and the video file exists, then we extract the audio from the video, convert it into a transcript, and return the contents
# If neither the video transcript nor video do not exist, then we raise an error!
def load_or_create_transcript(video_path: str, transcript_path: str) -> str:
    transcript_file = Path(transcript_path)
    video_file = Path(video_path)

    if transcript_file.exists():
        with transcript_file.open("r", encoding="utf-8") as f:
            return f.read()

    if not video_file.exists():
        raise FileNotFoundError(f"Neither transcript nor video exists: {transcript_path}, {video_path}")

    # MILESTONE 1 - extracting the audio based on the file name from user input and creating a .txt file containing the transcript
    audio_path = audio_extracter.extract_audio(video_path)
    full_transcript = audio_extracter.transcribe_audio(audio_path)
    audio_extracter.save_transcript(full_transcript, transcript_path)
    return full_transcript


# "Ingest" handles loading the transcript, chunking it, and adding it to the Chroma collection
def ingest_transcript(transcript_path: str):
    full_transcript = Path(transcript_path).read_text(encoding="utf-8")
    
    # MILESTONE 2 - Create a list and chunking the transcript into sentences
    transcript_chunks = transcript_chunker.chunk_by_sentences(full_transcript)

    # MILESTONE 3 - Storing the transcript chunks into a Chroma database and printing out its count
    chroma_client = chroma_storage.get_chroma_client()
    collection = chroma_storage.get_or_create_transcript_collection(chroma_client)

    video_name = Path(transcript_path).stem
    ids = chroma_storage.create_chunk_ids(video_name, transcript_chunks)
    metadatas = chroma_storage.create_chunk_metadata(video_name, transcript_chunks)
    chroma_storage.store_chunks(collection, ids, transcript_chunks, metadatas)
    

# "Query" handles using the user question to retrieve the most relevant information in the persistent Chroma collection
def query_transcript(question: str, n_results: int = 3):
    question = question.strip()

    if not question:
        raise ValueError("Question cannot be empty.")

    # MILESTONE 4 - SEMANTIC SEARCH    
    chroma_client = chroma_storage.get_chroma_client()
    collection = chroma_storage.get_or_create_transcript_collection(chroma_client)
    relevant_info = chroma_storage.semantic_search(collection, question)
           
    return relevant_info


# Handles the OpenAI request inside "llm_response.py"
def answer_question(question):
    relevant_info = query_transcript(question)
    
    retrieved_docs = relevant_info["documents"][0]
    retrieved_metadata = relevant_info["metadatas"][0]

    answer = llm_response.generate_answer(
        question=question,
        retrieved_docs=retrieved_docs,
        retrieved_metadata=retrieved_metadata
    )

    return answer


# Display retrieval results for debugging and evaluation
def display_retrieved_results(relevant_info):
    # MILESTONE 5 - GENERATE RELEVANT TRANSCRIPT CHUNKS
    ids = relevant_info["ids"][0]
    documents = relevant_info["documents"][0]
    metadatas = relevant_info["metadatas"][0]
    distances = relevant_info["distances"][0]
    
    for rank, (chunk_id, document, metadata, distance) in enumerate(
        zip(ids, documents, metadatas, distances),
        start=1
    ):
        print("\n" + "=" * 70)
        print(f"Rank: {rank}")
        print(f"Chunk ID: {chunk_id}")
        print(f"Distance: {distance:.4f}")
        print("\nTranscript Chunk:")
        print(document)
        print("\nMetadata:")
        for key, value in metadata.items():
            print(f"  {key}: {value}")
            

def main():
    mode = input(
        "Type 'ingest' to create/update a transcript, "
        "or 'answer' to generate an answer: "
    ).strip().lower()

    if mode == "ingest":
        video_path = input("Enter the video path (.mp4): ")
        transcript_path = input("Enter the transcript path (.txt): ")
        
        load_or_create_transcript(video_path, transcript_path)
        ingest_transcript(transcript_path)

    elif mode == "answer":
        question = input("What do you want to ask about the video? ")
        answer = answer_question(question)
        
        print("\n" + "=" * 70)
        print("Generated Answer")
        print("=" * 70)
        print(answer)

    else:
        print("Invalid mode. Use 'ingest' or 'answer'.")
        
        
if __name__ == '__main__':
    main()