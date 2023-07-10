from libraries.display_menu import display_menu


def main():
    while True:
        print("\n=== Police Tracker 👮‍♂️🚓 ===")
        display_menu()
        choice = input('Enter your action (1-3): ').lower().strip()

        match choice:
            case '1':  # Search by date range and name
                ...
            case '2':  # Search by date and cell tower number
                ...
            case '3':  # Search by date and location coordinates
                ...
            case 'q':  # Exit the program
                print("Exiting the program...")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
