from lib.file import read_file_chunks, compare_hashes, compare_chunk_hashes


FILENAME = 'data/sample_file.txt'
FILENAME_CHANGED = 'data/sample_file_changed.txt'


def main():
    print('Hello, World!')

    h1, h1_chunks = read_file_chunks(FILENAME)
    h2, h2_chunks = read_file_chunks(FILENAME_CHANGED)

    print(f'h1: {h1}')
    print(f'h2: {h2}')
    print(f'compare_hashes: {compare_hashes(h1=h1, h2=h2)}')

    print(f'h1_chunks:\n{h1_chunks}')
    print(f'h2_chunks:\n{h2_chunks}')
    print(f'compare_chunk_hashes: {compare_chunk_hashes(h1_chunks=h1_chunks, h2_chunks=h2_chunks)}')


if __name__ == '__main__':
    main()
