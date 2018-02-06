import json
import os
from sys import argv


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_file:
        bars = json.load(json_file)
    return bars


def get_biggest_bar(data):
    max_bar = max(bars,key=lambda x: x['Cells']['SeatsCount'])
    ind_max = max_bar['Number']
    return ind_max


def get_smallest_bar(data):
    min_bar = min(bars,key=lambda x: x['Cells']['SeatsCount'])
    ind_min = min_bar['Number']
    return ind_min


def get_closest_bar(data):
    my_longitude = float(input('введите значение долготы:'))
    my_latitude = float(input('введите значение широты:'))
    min_dist = 99999
    index = 0
    for ind in range(len(bars)):
        dist = ((bars[ind]['Cells']['geoData']['coordinates'][0] - my_longitude)**2 +
                (bars[ind]['Cells']['geoData']['coordinates'][1] - my_latitude)**2)**0.5
        if dist < min_dist:
            min_dist = dist
            index = ind
    return index


if __name__ == '__main__':
    filepath = argv[1]
    if os.path.isfile(filepath):
        bars = load_data(filepath)
        big_bar = get_biggest_bar(bars) - 1
        small_bar = get_smallest_bar(bars) - 1
        closest_bar = get_closest_bar(bars)
        print('Самый большой бар: ', bars[big_bar]['Cells']['Name']
              + ' имеет ' + str(bars[big_bar]['Cells']['SeatsCount'])+ ' мест')
        print('Самый маленький бар: ', bars[small_bar]['Cells']['Name']
              + ' имеет ' + str(bars[small_bar]['Cells']['SeatsCount'])+ ' мест')
        print("Самый близкий к вам: " + bars[closest_bar]['Cells']["Name"] + " имеет "
              + str(bars[closest_bar]['Cells']["SeatsCount"]) + " мест\n"
              'Находится по адресу: ', bars[closest_bar]['Cells']['Address'])







