
def print_date_name(result: list):
    if not result:
        print("No results found!")
        return

    for index, single_result in enumerate(result, start=1):
        print(f'\n- Cell Tower Connection {index} -')
        print(f"Sim Card Details: ICCID {single_result['sim']['ICCID']} - {single_result['sim']['provider']}")
        print(f"Cell Tower Number: {single_result['tower']['cellNumber']}")
        print(f"Connection Date: {single_result['data_in']}")
        print(f"Disconnection Date: {single_result['data_out']}")


def print_date_tower(result: list):
    if not result:
        print("No results found!")
        return

    for index, single_result in enumerate(result, start=1):
        print(f'\n- Cell Tower Connection {index} -')
        print(f"Sim Card Details: ICCID {single_result['sim']['ICCID']} - {single_result['sim']['provider']}")
        print(f"Person Details: {single_result['person']['name']}")


