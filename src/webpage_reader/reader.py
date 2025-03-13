from langchain_community.document_loaders import WebBaseLoader

class WebPageReader:
    def __init__(self, url):
        self.url = url
        self.loader = WebBaseLoader(url)

    def get_url(self):
        return self.url

    def get_loader(self):
        return self.loader

    def read(self):
        return self.loader.load()