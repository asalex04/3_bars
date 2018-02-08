import json
import os
from sys import argv


def load_data(filepath):
    with open(filepath) as json_file:
        bars = json.load(json_file)
    return bars


def get_biggest_bar(size):
    max_bar = max(bars, key=lambda x: x['Cells']['SeatsCount'])
    return max_bar['Number']-1


def get_smallest_bar(size):
    min_bar = min(bars, key=lambda x: x['Cells']['SeatsCount'])
    return min_bar['Number']-1


def get_closest_bar(distance):
    min_dist = 99999
    index = 0
    for ind in range(len(bars)):
        dist = ((bars[ind]['Cells']['geoData']['coordinates'][0] -
                 my_longitude) ** 2 +
                (bars[ind]['Cells']['geoData']['coordinates'][1] -
                 my_latitude) ** 2) ** 0.5
        if dist < min_dist:
            min_dist = dist
            index = ind
        return index


if __name__ == '__main__':

    try:
        filepath = argv[1]
        bars = load_data(filepath)
        my_longitude = float(input('введите значение долготы:'))
        my_latitude = float(input('введите значение широты:'))
    except FileNotFoundError:
        exit('File not found')
    except IndexError:
        print('Index is out of range')
    except ValueError:
        print('Invalid argument value')
    print(
        'Самый большой бар: {} имеет {} мест\n'
        'Самый маленький бар: {} имеет {} мест\n'
        'Самый близкий к Вам: {} имеет {} мест\n'
        'Находится по адресу: {}'.format(
            bars[get_biggest_bar(bars)]['Cells']['Name'],
            bars[get_biggest_bar(bars)]['Cells']['SeatsCount'],
            bars[get_smallest_bar(bars)]['Cells']['Name'],
            bars[get_smallest_bar(bars)]['Cells']['SeatsCount'],
            bars[get_closest_bar(bars)]['Cells']["Name"],
            bars[get_closest_bar(bars)]['Cells']["SeatsCount"],
            bars[get_closest_bar(bars)]['Cells']['Address']
        )
    )



