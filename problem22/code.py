f = open('input.txt', 'r')
grid = set()

def numofpoints(grid):
	numpoints=0
	for val in grid:
		valmin, valmax = val
		numpoints += (1+valmax[0]-valmin[0])*(1+valmax[1]-valmin[1])*(1+valmax[2]-valmin[2])
	return numpoints

for x in f:
	x = x.rstrip()
	direction = x.split(' ')[0]
	xmin, xmax = tuple(map(int, x.split(' ')[1].split(',')[0].split('=')[1].split('..')))
	ymin, ymax = tuple(map(int, x.split(' ')[1].split(',')[1].split('=')[1].split('..')))
	zmin, zmax = tuple(map(int, x.split(' ')[1].split(',')[2].split('=')[1].split('..')))
	if xmin <-50 or xmax>50 or ymin<-50 or ymax > 50 or zmin< -50 or zmax >50:
		pass
	if len(list(filter(lambda cube:not ((xmin > cube[1][0] or xmax < cube[0][0]) or (ymin>cube[1][1] or ymax < cube[0][1]) or (zmin>cube[1][2] or zmax < cube[0][2])), grid))) !=0:
		#split affected blocks into subcuboids
		# print("found overlap")
		for cube in grid.copy():
			if ((xmin > cube[1][0] or xmax < cube[0][0]) or (ymin>cube[1][1] or ymax < cube[0][1]) or (zmin>cube[1][2] or zmax < cube[0][2])) :
				continue
			else:
				grid.remove(cube)
				if cube[0][0] <xmin:
					grid.add(((cube[0][0], cube[0][1], cube[0][2]), (xmin-1,cube[1][1],cube[1][2])))
				if cube[1][0]> xmax:
					grid.add(((xmax+1, cube[0][1], cube[0][2]), (cube[1][0], cube[1][1], cube[1][2])))
				if cube[0][1] < ymin:
					grid.add(((max(xmin, cube[0][0]), cube[0][1], cube[0][2]), (min(xmax, cube[1][0]), ymin -1, cube[1][2])))
				if cube[1][1] > ymax:
					grid.add(((max(xmin, cube[0][0]), ymax+1, cube[0][2]), (min(xmax, cube[1][0]), cube[1][1], cube[1][2])))
				if cube[0][2] < zmin:
					grid.add(((max(xmin, cube[0][0]), max(ymin, cube[0][1]), cube[0][2]), (min(xmax, cube[1][0]), min(ymax, cube[1][1]), zmin-1)))
				if cube[1][2] > zmax:
					grid.add(((max(xmin, cube[0][0]), max(ymin, cube[0][1]), zmax+1), (min(xmax, cube[1][0]), min(ymax, cube[1][1]), cube[1][2])))
				if direction == 'on':
					grid.add(((xmin, ymin, zmin), (xmax, ymax, zmax)))
	elif direction == 'on':
		grid.add(((xmin,ymin,zmin),(xmax,ymax,zmax)))
	print(numofpoints(grid))
