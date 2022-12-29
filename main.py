import eyed3
import os
from elasticsearch_client import ElasticsearchClient
from tqdm import tqdm

ROOT_DIR = '/media/music'
MEDIA_EXTENSIONS = ['.mp3']
DEBUG_INFO = False


def load_meta(path):
    """
    Load metadata for given media file
    :return eyed3 tag
    """
    media_file = eyed3.load(path)
    if media_file is None:
        print(f'WARN: unrecognised file: {path}')
        return None
    return media_file.tag


def index_all(root, index):
    """
    Read metadata for all files under root path
    """
    for path, dirs, files in tqdm(os.walk(root), unit='albums'):
        for file in files:
            if os.path.splitext(file)[1] in MEDIA_EXTENSIONS:
                full_path = os.path.join(path, file)
                tag = load_meta(full_path)
                if DEBUG_INFO:
                    print_tag(tag)
                index.index(tag.artist, tag.album, tag.title, tag.genre.name, tag.getBestDate(), full_path)


def print_tag(tag):
    if tag is not None:
        print(f'Artist:     {tag.artist}\n'
              f'Album:      {tag.album}\n'
              f'Title       {tag.title}\n'
              f'Genre:      {tag.genre.name}\n'
              f'Released:   {tag.getBestDate()}')


if __name__ == '__main__':
    index = ElasticsearchClient('http://localhost:9200', 'id3')
    index_all(ROOT_DIR, index)



