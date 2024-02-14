import os


class DocumentDownload:

    def __init__(self, document_path):
        self.document_path = document_path
        self.document_download = self.document()

    def document(self):
        document_download = os.path.abspath(self.document_path)
        return document_download
