import chromadb
from transcript_chunker import split_into_sentences, chunk_by_sentences

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name='transcript_chunks')

transcript = None

with open('transcript.txt', "r", encoding="utf-8") as f:
    transcript = f.read()

transcript_chunks = chunk_by_sentences(transcript) # Formatted as a list!
ids = [f'id{id}' for id in range(1, len(transcript_chunks)+1)] 

metadatas = []
for i, chunk in enumerate(transcript_chunks):
    metadatas.append({
        'chunk_number': i+1,
        'source_type': 'video_transcript',
        'source_file': 'transcript.txt',
        'chunking_strategy': 'sentence_based',
        'max_chars': 800
    })


# Adding the chunks to the Chroma collection, along with the IDs
collection.add(ids=ids, 
               documents=transcript_chunks,
               metadatas=metadatas)

print(collection.count())