def read_file_chunks(filename: str, chunk_size: int = 1024):
    '''
    A function to lazy load a file with a specified chunk size.
    '''
    with open(filename) as file:
        while chunk := file.read(chunk_size):
            print(chunk)
