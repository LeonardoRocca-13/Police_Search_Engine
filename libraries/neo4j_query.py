from neo4j import GraphDatabase
import neo4j.exceptions


class Neo4jQuery:
    def __init__(self, uri, user, password):
        print('Connecting to Neo4j...')

        try:
            self._driver = GraphDatabase.driver(uri, auth=(user, password))
            print('Connected established!')

        except neo4j.exceptions.AuthError:
            print('Authentication failed!')
            exit(-1)

        except neo4j.exceptions.ServiceUnavailable:
            print('Connection failed!')
            exit(-1)

    def close_connection(self):
        try:
            self._driver.close()
            print('Connection closed!')

        except neo4j.exceptions.DriverError:
            print('Connection already closed!')

    def clear_database(self):
        with self._driver.session() as session:
            return session.run('MATCH (n) DETACH DELETE n')

    def search_by_date_person(self):
        ...

    def search_by_date_tower(self):
        ...

    def search_by_date_location(self):
        ...
