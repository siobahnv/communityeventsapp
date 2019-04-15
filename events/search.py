# from elasticsearchapp.search import *
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Integer, Keyword, Search, Document
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch

from . import models
from .models import *

# Create a connection to Elasticsearch
# connections.create_connection()
connections.create_connection(hosts=['localhost'])

# Elasticsearch "model" mapping out what fields to index
# class EventIndex(DocType):
class EventIndex(Document):
    event_name = Text()
    nominator = Text()
    event_url = Text()
    address = Text()
    city = Text()
    state_province = Text()
    country = Text()
    start_date = Date()
    end_date = Date()
    cfp_url = Text()
    conference_contact = Text()
    votes = Integer()
    tags = Keyword(multi=True)

    class Index:
        name = 'event-index'

    # class Meta:
    #     index = 'event-index'

def gendata():
    events = Events.objects.all()
    for event in events:
        yield {
            # "_index": "events",
            # "_type": "document",
            "_type": "_doc",
            # "_id": event.id,
            "doc": {"event": event},
        }

# Bulk indexing function, run in shell
def bulk_indexing():
    EventIndex.init()
    es = Elasticsearch()
    # bulk(client=es, actions=(b.indexing() for b in models.Event.objects.all().iterator()))
    bulk(es, gendata())

# Simple search function
def search(event_name):
    s = Search().filter('term', event_name=event_name)
    response = s.execute()
    return response