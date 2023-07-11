from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import prompt
import datetime


def get_person_name() -> str:
    while True:
        try:
            names = ['John Smith', 'Emma Johnson', 'Michael Brown', 'Sophia Davis', 'Daniel Miller', 'Olivia Taylor', 'Matthew Anderson', 'Ava Thomas', 'David Martinez', 'Isabella Wilson']
            name = prompt('\nEnter person name: ', completer=WordCompleter(names))
            return name

        except ValueError:
            print('Invalid name format! Try again.')


def get_cell_number() -> int:
    while True:
        try:
            cell_numbers = [str(i) for i in range(1, 11)]
            cell_number = int(prompt('\nEnter cell tower number: ', completer=WordCompleter(cell_numbers)))
            return cell_number

        except ValueError:
            print('Invalid cell tower number! Try again.')


def get_max_distance() -> int:
    while True:
        try:
            max_distance = int(input('\nEnter max distance (Km): ')) * 1000
            return max_distance

        except ValueError:
            print('Invalid cell tower number! Try again.')


def get_coordinates():
    while True:
        try:
            long_num = [str(i) for i in range(44, 48)]
            long = float(prompt('\nEnter longitude (Decimal Degrees): ', completer=WordCompleter(long_num)))
            if not -180 <= long <= 180:
                raise ValueError

            lat_num = [str(i) for i in range(8, 11)]
            lat = float(prompt('Enter latitude (Decimal Degrees): ', completer=WordCompleter(lat_num)))
            if not -90 <= lat <= 90:
                raise ValueError

            return round(long, 4), round(lat, 4)

        except ValueError:
            print('Error: range out of bounds!')


def get_datetime() -> datetime.datetime:
    while True:
        try:
            dates = ['2023/07/06', '2023/07/07']
            times = ['08:35', '10:18', '11:42', '13:05', '14:21', '15:03', '16:27', '17:45',
                     '19:08', '20:14', '21:32', '22:57', '00:25', '01:50', '03:30', '04:42',
                     '06:07', '07:47', '08:53', '10:16']

            date = prompt('Enter date in format (YYYY/MM/DD): ', completer=WordCompleter(dates))
            time = prompt('Enter time in format (HH:MM): ', completer=WordCompleter(times))

            return datetime.datetime.strptime(f'{date} {time}', '%Y/%m/%d %H:%M')

        except ValueError:
            print('Invalid date format! Try again.')


def get_datetime_range() -> tuple:
    while True:
        try:
            print('\nEnter start date and time: ')
            start_date = get_datetime()

            print('\nEnter end date and time: ')
            end_date = get_datetime()

            if start_date > end_date:
                raise ValueError

            return start_date, end_date

        except ValueError:
            print('Invalid date range! Try again.')
