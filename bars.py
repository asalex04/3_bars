import json
import os
import sys


def load_data(filepath):
    with open(filepath, encoding="windows-1251") as json_file:
        bars = json.load(json_file)
    return bars


def get_biggest_bar(bar):
    max_bar = max(bar, key=lambda x: x['SeatsCount'])
    return max_bar['Name']


def get_smallest_bar(bar):
    min_bar = min(bar, key=lambda x: x['SeatsCount'])
    return min_bar['Name']


def calc_distance(x, y, x1, y1):
    dist_count = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
    return dist_count


def get_closest_bar(bar, longitude, latitude):
    min_dist = min(bar, key=lambda x: calc_distance(longitude,
                                                    latitude,
                   x['geoData']['coordinates'][0],
                   x['geoData']['coordinates'][1]))
    return min_dist['Name']


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
    print('\nСамый большой бар:', get_biggest_bar(bars))
    print('\nСамый маленький бар:', get_smallest_bar(bars))
    print('\nСамый близкий к Вам:', get_closest_bar(bars, user_long, user_lat))




