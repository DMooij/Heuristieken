# import os, sys
# directory = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(os.path.join(directory, "code"))
# sys.path.append(os.path.join(directory, "code", "classes"))
# sys.path.append(os.path.join(directory, "code", "algoritmes"))
# sys.path.append(os.path.join(directory, "code", "grid"))

from overlap_check import *
from houses import *
from grid import *

import random as random

# Random coordinate generation after grid boundaries are given
def Randomizer(grid):

	# max and min value of the coordinates are grid outliers
	maxX = grid.width
	maxY = grid.height
	minX = 0
	minY = 0
	
	# generate random x and y for left up corner
	random_x = random.randint(minX, maxX)
	random_y = random.randint(minY, maxY)
	return [random_x, random_y]

def BuildRandomHouses(amount, coordinate_list):
	for houses in range(amount):
		cord = Randomizer(grid(180, 160))
		
		# build_single = amount*0.6
		# build_bungalow = amount*0.25
		# build_maison = amount*0.15

		# for building in range(build_single)
		# 	build = single

		# create either single, bungalow or maison
		housenr = random.randint(1, 3)
		if housenr == 1:
			build = single
		elif housenr == 2:
			build = bungalow
		elif housenr == 3:
			build = maison
		
		housecords = build(cord).coordinates_house()
		if housecords != None:
			if len(coordinate_list) == 0:
					coordinate_list.append(housecords)
			
			elif Overlap(housecords, coordinate_list) == True:
				coordinate_list.append(housecords)
	
	grid(180, 160).makegrid(coordinate_list) 
