from hashlib import sha256
import sys


def read_file_chunks(filename: str, chunk_size: int = 1024):
    '''
    A function to lazy load a file with a specified chunk size.
    '''
    # Whole file's hash.
    h = sha256()

    # Individual chunk hashes.
    h_chunks = []
    with open(filename, 'rb') as file:
        while chunk := file.read(chunk_size):
            # print(chunk)
            h.update(chunk)

            h_chunk = sha256()
            h_chunk.update(chunk)
            h_chunks.append(h_chunk.hexdigest())

            # print(f'chunk size: {sys.getsizeof(chunk)}')
            # print(f'chunk_hash size: {sys.getsizeof(h_chunk)}')

    return h.hexdigest(), h_chunks

