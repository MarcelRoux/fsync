from lib.file import read_file_chunks


FILENAME = 'data/sample_file.txt'


def main():
    print('Hello, World!')

    read_file_chunks(FILENAME)


if __name__ == '__main__':
    main()
