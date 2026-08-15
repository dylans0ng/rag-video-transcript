import chromadb

def get_chroma_client():
    chroma_client = chromadb.PersistentClient(path='chroma_db')
    return chroma_client


def get_or_create_transcript_collection(client):
    collection = client.get_or_create_collection(name='transcript_chunks')
    return collection


def create_chunk_ids(video_name, chunks):
    # Chunks is formatted as a list!
    # video_name will be dependent!
    ids = [f'{video_name}_chunk_{id}' for id in range(1, len(chunks)+1)] 
    return ids


def create_chunk_metadata(video_name, chunks):
    metadatas = []
    for i, _ in enumerate(chunks):
        metadatas.append({
            'chunk_number': i+1,
            'video_name': video_name,
            'source_type': 'video_transcript',
            'source_file': 'transcript.txt',
            'chunking_strategy': 'sentence_based',
            'max_chars': 800
        })
        
    return metadatas


def store_chunks(collection, ids, chunks, metadatas):
    # Adding the chunks to the Chroma collection, along with the IDs
    collection.upsert(
        ids=ids, 
        documents=chunks,
        metadatas=metadatas
    )


def get_chunk_by_id(collection, chunk_id):
    result = collection.get(
        ids=[chunk_id],
        include=['documents', 'metadatas']
    )
    
    return result


def semantic_search(collection, question, n_results=3):
    results = collection.query(
        query_texts=[question],
        n_results=n_results,
        include=['documents', 'metadatas', 'distances']
    )
    
    return results


def get_collection_count(collection):
    return collection.count()

# transcript = None

# with open('transcript.txt', "r", encoding="utf-8") as f:
#     transcript = f.read()
