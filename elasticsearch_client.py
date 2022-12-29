from elasticsearch import Elasticsearch


class ElasticsearchClient:
    def __init__(self, url, index_name):
        self.es = Elasticsearch(url)
        self.index_name = index_name

    def connect_test(self):
        print(self.es.info())

    def index(self, artist, album, title, genre, date, path):
        doc = {
            'artist': artist,
            'album': album,
            'title': title,
            'genre': genre,
            'date': date,
            'path': path
        }
        self.es.index(index=self.index_name, document=doc)


if __name__ == '__main__':
    es = ElasticsearchClient('http://localhost:9200')
    es.connect_test()
