from libraries.neo4j_query import Neo4jQuery

from libraries.get_query_params import get_person_name, get_datetime_range, get_cell_number, get_datetime, \
    get_coordinates, get_max_distance

from libraries.print_results import print_date_name, print_date_tower
from libraries.display_menu import display_menu


def main():
    neo4j_connection = Neo4jQuery('neo4j+s://eb6f0bed.databases.neo4j.io', 'neo4j',
                                  'ljHcaoYZSuSfYMj5v4sekaR70iqQivr26RVZuOOgjlk')

    while True:
        print("\n=== Police Tracker 👮‍♂️🚓 ===")
        display_menu()
        choice = input('Enter your action (1-3): ').lower().strip()

        match choice:
            case '1':  # Search by date range and name
                person_name = get_person_name()
                start_datetime, end_datetime = get_datetime_range()

                result = neo4j_connection.search_by_date_person(person_name, start_datetime, end_datetime)

                print_date_name(result)

            case '2':  # Search by date and cell tower number
                cell_number = get_cell_number()
                search_date = get_datetime()

                result = neo4j_connection.search_by_date_tower(cell_number, search_date)

                print_date_tower(result)

            case '3':  # Search by date and location coordinates
                coordinates = get_coordinates()
                max_distance = get_max_distance()
                search_date = get_datetime()

                result = neo4j_connection.search_by_date_location(search_date, max_distance, coordinates)

                print_date_tower(result)

            case 'q':  # Exit the program
                print("Exiting the program...")
                neo4j_connection.close_connection()
                break

            case _:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
