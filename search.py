import json
from turtle import title
from whoosh.index import create_in, exists_in, open_dir
from whoosh.filedb.filestore import FileStorage
from whoosh.fields import *
import os
from whoosh.analysis import *
from whoosh.qparser import QueryParser


storage = FileStorage("indexdir")

analyzer = StemmingAnalyzer()
schema = Schema(content=TEXT(analyzer=StemmingAnalyzer()),
                title=TEXT(stored=True))

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")


if exists_in("indexdir"):
    ix = open_dir("indexdir")
else:
    ix = create_in("indexdir", schema)

writer = ix.writer()


def document_index(document):
    for item in document:
        writer.add_document(content=item['overview'], title=item['title'])

    writer.commit()


# f = open('movies.json')
# json_data = json.load(f)
# document_index(json_data)
search_res = []


def search(q):
    parser = QueryParser("content", ix.schema)
    myquery = parser.parse(q)
    with ix.searcher() as searcher:
        results = searcher.search(myquery)
        for result in results:
            search_res.append({'title': result['title']})
    return search_res
