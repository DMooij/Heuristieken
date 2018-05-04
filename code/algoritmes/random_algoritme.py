# from overlap_check import *
from houses import *
from grid import *

import random as random

# Random coordinate generation after grid boundaries are given
def Randomizer(amount):
	# max and min value of the coordinates are grid outliers
	maxX = 320
	maxY = 360
	minX = 0
	minY = 0

	# generate random x and y for left up corner
	random_x = random.randint(minX, maxX)
	random_y = random.randint(minY, maxY)
	return [random_x, random_y]

def SetHouseInList(build, cord, coordinate_list, cordinatelist):

	# if thing == "house":
	housecords = build(cord).coordinates_house()
	if housecords != None:
		if len(coordinate_list) == 0:
			coordinate_list.append(housecords)
			# cordinatelist = grid().updatecordinatelist(cordinatelist, housecords, "houses")
			return True
		elif grid().overlapping(cordinatelist, housecords) == True:
			coordinate_list.append(housecords)
			cordinatelist = grid().updatecordinatelist(cordinatelist, housecords, "house")
			return True
		elif grid().overlapping(cordinatelist, housecords) != True:
			return False

		# elif Overlap(housecords, coordinate_list) == True:
		# 	coordinate_list.append(housecords)
		# 	cordinatelist = grid().updatecordinatelist(cordinatelist, housecords, "houses")
		# 	return True
		# elif Overlap(housecords, coordinate_list) != True:
		# 	return False

# def Watercreator():
	
# 	water_bodies = [1, 2, 3, 4]
# 	amount_water = random.choice(water_bodies)
# 	print(amount_water)
		
# 	total_water = MakeWater(amount_water)
# 	for water in total_water:
# 		if grid().overlapping(cordinatelist, water) == True:
# 			if grid().updatecordinatelist(cordinatelist, water, "water") != True:
# 				print("gaat mis")
# 			return True
# 		elif grid().overlapping(cordinatelist, water) != True:
# 				return False	

# 	return total_water


def BuildRandomAmstelhaege(amount, cordinatelist):
	build_single = int(amount*0.6)
	build_bungalow = int(amount*0.25)
	build_maison = int(amount*0.15)

	# cordinatelist = grid().makecordinatelist()

	coordinate_list = []
	housecount = 0
	total_value = 0

	while housecount < build_single:
		cord = Randomizer(1)
		build = single
		if SetHouseInList(build, cord, coordinate_list, cordinatelist) == True:
			housecount += 1
			total_value += single(cord).giveworth()

	while housecount < (build_single + build_bungalow):
		cord = Randomizer(1)
		build = bungalow
		if SetHouseInList(build, cord, coordinate_list, cordinatelist) == True:
			housecount += 1
			total_value += bungalow(cord).giveworth()

	while housecount < amount:
		cord = Randomizer(1)
		build = maison
		if SetHouseInList(build, cord, coordinate_list, cordinatelist) == True:
			housecount += 1
			total_value += maison(cord).giveworth()

	print(cordinatelist)
	print("hoi")
	grid().makegrid(coordinate_list, total_value) 


def Random(nr_of_houses):
	# make empty coordinate list

	cordinatelist = grid().makecordinatelist()
	# make water
	# water = Watercreator()

	BuildRandomAmstelhaege(nr_of_houses, cordinatelist)
