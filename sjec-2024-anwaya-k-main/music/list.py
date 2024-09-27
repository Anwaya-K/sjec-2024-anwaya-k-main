import argparse
import os

def list_music_files(directory):
    supported_formats = ['.mp3', '.wav', '.ogg', '.flac']
    music_files = [file for file in os.listdir(directory) if file.endswith(tuple(supported_formats))]
    return music_files

def main():
    parser = argparse.ArgumentParser(description='List music files in a directory')
    parser.add_argument('--input', required=True, help='C:\Users\hp\Downloads\sjec-2024-anwaya-k-main\sjec-2024-anwaya-k-main\music\Music')
    parser.add_argument('--list-files', action='store_true', help='List music files')
    args = parser.parse_args()

    if args.list_files:
        directory = args.input
        if not os.path.isdir(directory):
            print(f"Error: {directory} is not a valid directory")
            return

        music_files = list_music_files(directory)
        for file in music_files:
            print(file)

if __name__ == "__main__":
    main()