from elasticsearch import Elasticsearch


class ElasticsearchClient:
    def __init__(self, url):
        self.es = Elasticsearch(url)

    def connect_test(self):
        print(self.es.info())


if __name__ == '__main__':
    es = ElasticsearchClient('http://localhost:9200')
    es.connect_test()
