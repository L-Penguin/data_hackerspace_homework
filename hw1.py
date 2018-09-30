#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    crashes_each_hour = [0 for i in range(24)]
    with open(filename) as f:
        csv_reader = csv.reader(f)
        airplane_data = list(csv_reader)
    for incident in airplane_data[1:]:
        if incident[1]:
            hour = int(incident[1].split(':')[0])
            crashes_each_hour[hour] += 1
    return crashes_each_hour

def weigh_pokemons(filename, weight):
    namelist = []
    with open(filename) as f:
        data = json.load(f)
    for i in range(len(data["pokemon"])):
        if float(data["pokemon"][i]["weight"].split(' ')[0]) == weight:
            namelist.append(data["pokemon"][i]["name"])
    return namelist

def single_type_candy_count(filename):
    count = 0
    with open(filename) as f:
        data = json.load(f)
    for i in range(len(data["pokemon"])):
        if "candy_count" in data["pokemon"][i]:
            if len(data["pokemon"][i]["type"]) == 1:
                count += int(data["pokemon"][i]["candy_count"])
    return count
    

def reflections_and_projections(points):
    toTransform = points
    for y in range(len(toTransform[1])):
        toTransform[1][y] = 1 - (toTransform[1][y] - 1)
    R = np.array([[np.cos(np.pi/2), -np.sin(np.pi/2)],[np.sin(np.pi/2), np.cos(np.pi/2)]])
    for x, y in range(len(toTransform[0])), range(len(toTransform[0])):
        toTransform[0][x], toTransform[1][y] = R @ np.array([toTransform[0][x], toTransform[1][y]])
    for x, y in range(len(toTransform[0])), range(len(toTransform[0])):
        toTransform[0][x], toTransform[1][y] = (1/(10))*(np.array([[1, 3],[3, 9]]) @ np.array([toTransform[0][x], toTransform[1][y]]))
    return toTransform

def normalize(image):
    max = image.max()
    min = image.min()
    for x, y in range(len(image)), range(len(image[0])):
        image[x][y] = (image[x][y] - min) * (255/(max-min))
    return image

def sigmoid_normalize(image, a):
    for x, y in range(len(image)), range(len(image[0])):
        image[x][y] = 255*(1+(np.e**(-(image[x][y]**-1)*(a - 128)))**-1)
    return image