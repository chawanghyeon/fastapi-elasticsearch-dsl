from dependency_injector import containers, providers
from .database import Database
from .elastic import ElasticSearchClient

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    db = providers.Singleton(Database, db_url=config.SQLALCHEMY_DATABASE_URI)
    es_client = providers.Singleton(ElasticSearchClient, es_url=config.ELASTICSEARCH_URL)
