from nose.tools import *
from collections import namedtuple

Cell = namedtuple('Cell', ('x', 'y'))

def is_neighbor(cell1, cell2):
	return (cell1 in get_neighbors(cell2))

def get_neighbors(cell):
	return {Cell(x,y) for x in xrange(cell.x-1,cell.x+2) 
	                  for y in xrange(cell.y-1,cell.y+2)
	                  }.difference(set([cell]))

def play(world):
	survivors = {cell for cell in world if cell_should_live(cell, world)}
	neighbors = reduce(set.union, [get_neighbors(cell) for cell in world])
	babies = {cell for cell in neighbors if cell_should_birth(cell, world)}
	return survivors.union(babies)

def cell_should_live(targetcell, world):
	return 2 <= alive_neighbors(targetcell, world) <= 3

def cell_should_birth(targetcell, world):
	return alive_neighbors(targetcell, world) == 3 and targetcell not in world

def alive_neighbors(targetcell, world):
	return len([cell for cell in world if is_neighbor(targetcell, cell)])

def world_generator(world):
	while len(world) != 0:
		world = play(world)
		yield world