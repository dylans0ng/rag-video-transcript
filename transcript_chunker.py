import re


def split_into_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s for s in sentences if s]


def chunk_by_sentences(text, max_chars=800):
    sentences = split_into_sentences(text)
    chunks = []
    current_chunk = ''
    
    for sentence in sentences:
        if len(sentence) + len(current_chunk) + 1 <= max_chars: # We do +1 because a new sentence typically begins with a space
            if current_chunk: # If the current_chunk has text, then we want to add a space and then the sentence
                current_chunk += ' ' + sentence
            else: # If the current_chunk is empty, then we want to set it equal to the sentence
                current_chunk = sentence
            
        else: # If the length of the sentence + the current chunk + 1 is greater than max_chars...
            chunks.append(current_chunk) # Add the finished chunk to "chunks"
            current_chunk = sentence # Set the current_chunk equal to the current sentence so that it can be dealt with in the next iteration
    
    if current_chunk:
        chunks.append(current_chunk) # Add the leftover chunk if there is a chunk still remaining
        
    return chunks
        

def main():
    with open('transcript.txt', "r", encoding="utf-8") as f:
        transcript = f.read()
        
    chunks = chunk_by_sentences(transcript)
    with open('transcript_chunking_test.txt', "w", encoding="utf-8") as f:
        for i, chunk in enumerate(chunks, start=1):
            f.write(f"--- Chunk {i} ---\n")
            f.write(chunk)
            f.write("\n\n")
    
    print(len(chunk_by_sentences(transcript)))
    print(len(chunk_by_sentences(transcript)))
    # print(chunk_by_sentences(transcript)[]])
    print(len(chunk_by_sentences(transcript)[0]))
        
        
if __name__ == '__main__':
    main()