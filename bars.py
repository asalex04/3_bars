import json
import os
import sys


def load_data(filepath):
    with open(filepath) as json_file:
        bars = json.load(json_file)
    return bars


def print_inf(bar, index):
    print('Название: ', bar[index]['Cells']['Name'],
          '\nКолличество мест: ', bar[index]['Cells']['SeatsCount'],
          '\nАдрес: ', bar[index]['Cells']['Address'])


def get_biggest_bar(bar):
    index_max_bar = max(bar, key=lambda x: x['Cells']['SeatsCount'])
    return index_max_bar['Number']-1


def get_smallest_bar(bar):
    index_min_bar = min(bar, key=lambda x: x['Cells']['SeatsCount'])
    return index_min_bar['Number']-1


def calc_distance(x, y, x1, y1):
    dist_count = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
    return dist_count


def get_closest_bar(bar, longitude, latitude):
    min_dist = min(bar, key=lambda x: calc_distance(longitude,
                                                     latitude,
                   x['Cells']['geoData']['coordinates'][0],
                   x['Cells']['geoData']['coordinates'][1]))
    return min_dist['Number']-1


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        bars = load_data(filepath)
    except (ValueError, FileNotFoundError):
        exit('Не найден корректный json файл')
    try:
        user_long = float(input('введите значение долготы: '))
        user_lat = float(input('введите значение широты: '))
    except ValueError:
        exit('Вы указали неверные координаты')
    print('\nСамый большой бар:')
    print_inf(bars, get_biggest_bar(bars))
    print('\nСамый маленький бар:')
    print_inf(bars, get_smallest_bar(bars))
    print('\nСамый близкий к Вам:')
    print_inf(bars, get_closest_bar(bars, user_long, user_lat))




