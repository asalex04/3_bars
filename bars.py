import json
import os
from sys import argv


def load_data(filepath):
    with open(filepath) as json_file:
        bars = json.load(json_file)
    return bars


def print_inf(bars, index):
    print('Название: ', bars[index]['Cells']['Name'],
          '\nКолличество мест: ', bars[index]['Cells']['SeatsCount'],
          '\nАдрес: ', bars[index]['Cells']['Address'])


def get_biggest_bar(size):
    index_max_bar = max(bars, key=lambda x: x['Cells']['SeatsCount'])
    return index_max_bar['Number']-1


def get_smallest_bar(size):
    index_min_bar = min(bars, key=lambda x: x['Cells']['SeatsCount'])
    return index_min_bar['Number']-1


def calc_distance(x, y, x1, y1):
    dist_count = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
    return dist_count


def get_closest_bar(bars, longitude, latitude):
    min_dist = min(bars, key=lambda x: calc_distance(longitude,
                                                     latitude,
                   x['Cells']['geoData']['coordinates'][0],
                   x['Cells']['geoData']['coordinates'][1]))
    return min_dist['Number']-1


if __name__ == '__main__':

    try:
        filepath = argv[1]
        bars = load_data(filepath)
    except FileNotFoundError:
        exit('Файл не найден')
    try:
        my_long = float(input('введите значение долготы: '))
        my_lat = float(input('введите значение широты: '))
    except ValueError:
        exit('Вы указали неверные координаты')
    print('\nСамый большой бар:')
    print_inf(bars, get_biggest_bar(bars))
    print('\nСамый маленький бар:')
    print_inf(bars, get_smallest_bar(bars))
    print('\nСамый близкий к Вам:')
    print_inf(bars, get_closest_bar(bars, my_long, my_lat))




