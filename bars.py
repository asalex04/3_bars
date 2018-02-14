import json
import sys


def load_data(filepath):
    with open(filepath, encoding='windows-1251') as json_file:
        bars = json.load(json_file)
    return bars


def print_func(bar):
    print('Название: ', bar['Name'],
          '\nКолличество мест: ', bar['SeatsCount'],
          '\nАдрес: ', bar['Address'])


def get_biggest_bar(bar_name):
    max_bar = max(bar_name, key=lambda x: x['SeatsCount'])
    return max_bar


def get_smallest_bar(bar_name):
    min_bar = min(bar_name, key=lambda x: x['SeatsCount'])
    return min_bar


def calc_distance(x, y, x1, y1):
    dist_count = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
    return dist_count


def get_closest_bar(bar_name, longitude, latitude):
    min_dist = min(bar_name, key=lambda x: calc_distance(
        longitude,
        latitude,
        x['geoData']['coordinates'][0],
        x['geoData']['coordinates'][1]))
    return min_dist


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        bars = load_data(filepath)
    except (ValueError, IndexError, FileNotFoundError):
        exit('Не найден корректный json файл')
    try:
        user_long = float(input('введите значение долготы: '))
        user_lat = float(input('введите значение широты: '))
    except ValueError:
        exit('Вы указали неверные координаты')
    print('\nСамый большой бар:')
    print_func(get_biggest_bar(bars))
    print('\nСамый маленький бар:')
    print_func(get_smallest_bar(bars))
    print('\nСамый близкий к Вам:')
    print_func(get_closest_bar(bars, user_long, user_lat))