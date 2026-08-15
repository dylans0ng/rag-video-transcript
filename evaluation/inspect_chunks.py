from typing import Any, Dict
import chroma_storage
from .evaluation_config import EVALUATION_CONFIG


def get_chunk_number(metadata: Dict[str, Any]) -> int:
    """
    Return a sortable chunk number.

    Records without a valid chunk number are placed at the end.
    """
    chunk_number = metadata.get("chunk_number")

    try:
        return int(chunk_number)
    except (TypeError, ValueError):
        return 999999


# Prints all the chunks based on the video of EVALUATION_CONFIG['video_name']
def inspect_chunks() -> None:
    """
    Print all transcript chunks stored for the configured video.
    """
    chroma_client = chroma_storage.get_chroma_client()
    collection_name = EVALUATION_CONFIG["collection_name"]
    collection = chroma_client.get_or_create_collection(name=collection_name)

    video_name = EVALUATION_CONFIG["video_name"]

    # Only retrieve chunks belonging to the video being evaluated.
    results = collection.get(
        where={"video_name": video_name},
        include=["documents", "metadatas"]
    )

    ids = results.get("ids", [])
    documents = results.get("documents") or []
    metadatas = results.get("metadatas") or []

    if not ids:
        print(
            f"No chunks were found for video_name='{video_name}' "
            f"in collection '{collection_name}'.\n"
            "Check that evaluation_config.py matches your stored metadata "
            "and collection name."
        )
        return

    records = []

    for index, chunk_id in enumerate(ids):
        document = documents[index] if index < len(documents) else ""
        metadata = metadatas[index] if index < len(metadatas) else {}

        records.append(
            {
                "id": chunk_id,
                "document": document,
                "metadata": metadata or {}
            }
        )

    # Display chunks in transcript order instead of database return order.
    records.sort(
        key=lambda record: get_chunk_number(record["metadata"])
    )

    print(f"\nCollection: {collection_name}")
    print(f"Video: {video_name}")
    print(f"Total chunks: {len(records)}")

    # Looping through the list of dictionaries, where each dictionaries containing info on each chunk
    for record in records:
        print("\n" + "=" * 80)
        print(f"Chunk ID: {record['id']}")
        print(
            f"Chunk Number: "
            f"{record['metadata'].get('chunk_number', 'Unknown')}"
        )

        print("\nMetadata:")
        for key, value in record["metadata"].items():
            print(f"  {key}: {value}")

        print("\nTranscript:")
        print(record["document"])

    print("\n" + "=" * 80)
    print("Finished displaying chunks.")


if __name__ == "__main__":
    inspect_chunks()