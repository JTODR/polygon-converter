'''
Script that converts an EPSG:900913 polygon to an EPSG:4326 polygon

EXAMPLE:
 INPUT: POLYGON((-437396.91611144005_6962698.374744099,-437396.91611144005_6965220.7966772,-433555.95544064_6965220.7966772,-433555.95544064_6962698.3747441005,-437396.91611144005_6962698.374744099))
 OUPUT: POLYGON((-3.929203350243457 52.89011715234372,-3.929203350243457 52.903786385493476,-3.894699413475837 52.903786385493476,-3.894699413475837 52.89011715234372,-3.929203350243457 52.8901171523437))

'''

import math

def point_epsg900913_to_epsg4326(xy_coord):
	x = float(xy_coord.split('_')[0])
	y = float(xy_coord.split('_')[1])

	lon = x *  180 / 20037508.34
	lat = math.atan(math.exp(y * math.pi / 20037508.34)) * 360 / math.pi - 90

	return str(lon) + ' ' + str(lat)	
	
def get_epsg4326_polygon_points(polygon_900913):
	lat_long_coords = []

	xy_points = (((polygon_900913.split('((')[1]).split('))')[0]).split(','))	# remove prefix 'POLYGON((' and suffix '))' and extract points

	for xy_coord in xy_points:
		if '_' not in xy_coord:
			print('\nInvalid point in polygon: ' + xy_coord)
			print('Points in polygon should be of the form: x_y')
			return '-1'
		lat_long_coords.append(point_epsg900913_to_epsg4326(xy_coord))
	return lat_long_coords

def get_epsg4326_polygon_string(epsg4326_points):
	epsg4326_polygon = 'POLYGON(('

	for point in epsg4326_points:

		epsg4326_polygon = epsg4326_polygon + point + ','

	return (epsg4326_polygon[:-2] + '))')		# [:-2] removes the last ', ' from the string

def main():
	while True:
		epsg900913_polygon = input('\nEnter EPSG:900913 polygon:\n')
		if 'POLYGON((' not in epsg900913_polygon or '))' not in epsg900913_polygon:
			print('Enter a valid EPSG:900913 polygon in the form: POLYGON((x_y, x_y, ...))')
		else:
			epsg4326_points = get_epsg4326_polygon_points(epsg900913_polygon)

			if '-1' != epsg4326_points:
				epsg4326_polygon = get_epsg4326_polygon_string(epsg4326_points)
				print('\nEPSG:4326 polygon: \n' + epsg4326_polygon)

			print('\n---------------------------------------------------------')

if __name__ == '__main__':
	main()