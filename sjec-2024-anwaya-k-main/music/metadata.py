import tinytag

def show_metadata(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.mp3', '.wav', '.ogg')):
                file_path = os.path.join(root, file)
                tag = tinytag.TinyTag.get(file_path)
                print(f"File: {file_path}")
                print(f"Song: {tag.title}")
                print(f"Artist: {tag.artist}")
                print(f"Album: {tag.album}")
                print("--------------------")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--show-metadata', action='store_true')
    args = parser.parse_args()
    
    if args.show_metadata:
        show_metadata(args.input)

