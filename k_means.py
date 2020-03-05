from image_utils import *
import math as m

def k_means(image, k):
	"""incorporates all of the following functions to perform the k means
	clustering algorithm on an image"""
	prevAssignments = 0
	means = initialGuess(k)
	width, height = get_width_height(image)
	assignments = [ [] for i in range(width) ] 
	for row in range(height):
		for col in range(width):
			colorFromImage = image[col][row]
			assignments[col].append(getAssignment(colorFromImage, means))

	while assignments != prevAssignments:
		# update the means list
		means = updateMeans(image, assignments, k, width, height)

		# save assignments as prevAssignments and update assignments
		prevAssignments = assignments
		assignments = updateAssignments(image, means, k, width, height)

	newImage = replaceColors(assignments, means, width, height)
	return newImage



def replaceColors(assignments, means, width, height):
	"""writes out the values of the means list to each pixel assigned 
	to a particular cluster. This builds a new image"""
	modifiedImage = [ [] for i in range(width) ]
	for row in range(height):
		for col in range(width):
			colorCluster = assignments[col][row]
			modifiedImage[col].append(means[colorCluster])
	return modifiedImage

def initialGuess(k):
	"""used to populate the k_means list with k random colors"""
	means = []
	for color in range(k):
		means.append(random_color())
	return means

def getAssignment(colorFromImage, means):
	"""checks a pixel color against all the colors in the means list to
	find out which means color is most similar. returns the index of 
	the closest mean"""
	shortest = 6080    # country mile
	nearestMean = 0
	for meanColor in means:
		if distance(colorFromImage, meanColor) < shortest:
			shortest = distance(colorFromImage, meanColor)
			nearestMean = means.index(meanColor) 
	return nearestMean   # returns the index of the nearest mean

def updateMeans(image, assignments, k, width, height):
	"""creates a new means list by grouping all of the pixels assigned to
	an old mean color in a list and averaging them to find the color that 
	best represents the 'middle' of the cluster"""
	updatedMeans = []
	clusterData = [ [] for i in range(k) ]
	for row in range(height):
		for col in range(width):
			meanIndex = assignments[col][row]
			clusterData[meanIndex].append(image[col][row])
	for j in range(k):
		updatedMeans.append(avgColor(clusterData[j]))
	return updatedMeans

def updateAssignments(image, means, k, width, height):
	"""creates new assignments list by looping through image and checking pixels
	against the mean colors list to see which is the best fit"""
	newAssignments = [ [] for i in range(width) ]
	for row in range(height):
		for col in range(width):
			colorFromImage = image[col][row]
			newAssignments[col].append(getAssignment(colorFromImage, means))
	return newAssignments

def distance(color1, color2):
	"""just like in geometry how you can calculate the distance between two distinct
	points in three dimensions, the 'distance' in between two colors is computed and returned"""
	distance = 0
	distance = m.sqrt(m.pow((color1[0] - color2[0]), 2) + m.pow((color1[1] - color2[1]), 2) + m.pow((color1[2] - color2[2]), 2))
	return distance

def avgColor(lst):
	"""given a list of colors, computes the average of the R, G, and B components
	and then repackages up the averages into one color, keeping the int type for all components"""
	red = 0
	green = 0
	blue = 0
	numColors = len(lst)
	for color in lst:
		red += color[0]
		green += color[1]
		blue += color[2]
	return (int(red / numColors), int(green / numColors), int(blue / numColors))