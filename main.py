import os

def main(path):
    files = os.listdir(path)
    for index, file in enumerate(files):
        names = os.path.join(path, file), os.path.join(path, ''.join([str(index + 1), '.', file.split('.')[-1]]))
        os.rename(*names)


if __name__ == "__main__":
    main("/Applications/MAMP/htdocs/Image")

