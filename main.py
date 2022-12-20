import eyed3


def load_meta(path):
    """
    Load metadata for given media file
    """
    media_file = eyed3.load(path)
    return media_file.tag


if __name__ == '__main__':
    tag = load_meta('/home/stevie/Music/01 I Caputure Castles.mp3')
    print(f'Artist:     {tag.artist}\n'
          f'Album:      {tag.album}\n'
          f'Genre:      {tag.genre}\n'
          f'Released:   {tag.getBestDate()}')


