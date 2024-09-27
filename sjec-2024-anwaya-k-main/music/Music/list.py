import os
import argparse

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.mp3', '.wav', '.ogg')):
                print(os.path.join(root, file))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--list-files', action='store_true')
    args = parser.parse_args()
    
    if args.list_files:
        list_files(args.input)
