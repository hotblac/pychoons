import eyed3
import os

ROOT_DIR = '/media/music'
MEDIA_EXTENSIONS = ['.mp3']


def load_meta(path):
    """
    Load metadata for given media file
    """
    media_file = eyed3.load(path)
    if media_file is None:
        print(f'WARN: unrecognised file: {path}')
        return None
    return media_file.tag


def read_all(root):
    """
    Read metadata for all files under root path
    """
    for path, dirs, files in os.walk(root):
        for file in files:
            if os.path.splitext(file)[1] in MEDIA_EXTENSIONS:
                full_path = os.path.join(path, file)
                tag = load_meta(full_path)
                print_tag(tag)


def print_tag(tag):
    if tag is not None:
        print(f'Artist:     {tag.artist}\n'
              f'Album:      {tag.album}\n'
              f'Title       {tag.title}\n'
              f'Genre:      {tag.genre}\n'
              f'Released:   {tag.getBestDate()}')


if __name__ == '__main__':
    read_all(ROOT_DIR)



