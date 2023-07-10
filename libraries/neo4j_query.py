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

    def search_by_date_person(self, person_name: str, start_date: str, end_date: str) -> list:
        results = []
        with self._driver.session() as session:
            records = session.run(
                'MATCH (person:Person {name: $personName})<-[:OWNED_BY]-(sim:Sim)-[connection:CONNECTION]->(tower:CellTower) \
                WHERE datetime($startDate) <= connection.dataIn <= datetime($endDate) \
                RETURN sim, tower, connection.dataIn, connection.dataOut',
                personName=person_name, startDate=start_date, endDate=end_date
            )

            for record in records:
                sim_node = record['sim']
                tower_node = record['tower']
                data_in_date = record['connection.dataIn'].strftime('%Y/%m/%d %H:%M:%S')
                data_out_date = record['connection.dataOut'].strftime('%Y/%m/%d %H:%M:%S')

                sim_details = dict(sim_node.items())
                tower_details = dict(tower_node.items())

                single_result = {
                    'sim': sim_details,
                    'tower': tower_details,
                    'data_in': data_in_date,
                    'data_out': data_out_date,
                }

                results.append(single_result)

            return results

    def search_by_date_tower(self, cell_number: int, search_date: str) -> list:
        results = []
        with self._driver.session() as session:
            records = session.run(
                'MATCH (person:Person)<-[:OWNED_BY]-(sim:Sim)-[connection:CONNECTION]->(tower:CellTower {cellNumber: $cellNumber}) \
                WHERE datetime($searchDate) <= connection.dataIn <= datetime($searchDate) + duration({minutes: 10}) \
                RETURN sim, person',
                cellNumber=cell_number, searchDate=search_date
            )

            for record in records:
                sim_node = record['sim']
                person_node = record['person']

                sim_details = dict(sim_node.items())
                person_details = dict(person_node.items())

                single_result = {
                    'sim': sim_details,
                    'person': person_details,
                }

                results.append(single_result)

            return results

    def search_by_date_location(self):
        ...
