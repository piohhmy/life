import itertools
from life import *

def test_cell_is_neighbor():
	cell1 = Cell(0,0)
	cell2 = Cell(0,1)

	assert_true(is_neighbor(cell1, cell2))

def test_cell_is_not_neighbor():
	cell1 = Cell(0,0)
	cell2 = Cell(0,5)

	assert_false(is_neighbor(cell1, cell2))

def test_equal_cells_are_not_neighbors():
	cell1 = Cell(0,0)
	cell2 = Cell(0,0)

	assert_false(is_neighbor(cell1, cell2))

def test_cell_should_live_with_two_neighbors_in_world():
	targetcell = Cell(0,0)
	world = set([targetcell, Cell(0,1), Cell(1,0)])

	assert_true(cell_should_live(targetcell, world))

def test_cell_should_die_with_one_neighbor_in_world():
	targetcell = Cell(0,0)
	world = set([targetcell, Cell(0,1)])

	assert_false(cell_should_live(targetcell, world))

def test_cell_should_die_with_4_neighbors_in_world():
	targetcell = Cell(0,0)
	world = set([targetcell, Cell(0,1), Cell(0,-1),Cell(1,0),Cell(-1,0)])

	assert_false(cell_should_live(targetcell, world))

def test_cell_should_birth_with_3_neighbors_in_world():
	targetcell = Cell(0,0)
	world = set([Cell(0,1), Cell(0,-1), Cell(1,0)])

	assert_true(cell_should_birth(targetcell, world))

def test_cell_should_not_birth_with_2_neighbors_in_world():
	targetcell = Cell(0,0)
	world = set([targetcell, Cell(0,1), Cell(0,-1)])

	assert_false(cell_should_birth(targetcell, world))

def test_world_with_single_cell_dies():
	world = set([Cell(0,0)])

	new_world = play(world)

	assert_equal(set(), new_world)

def test_world_play_follows_rules_for_life_and_death():
	world = set([Cell(0,0), Cell(-1,-1), Cell(1,1)])

	new_world = play(world)

	assert_equal(set([Cell(0,0)]), new_world)

def test_world_play_follows_rules_for_birth():
	world = set([Cell(0,0), Cell(1,1), Cell(2,-1)])

	new_world = play(world)

	assert_equal(set([Cell(1,0)]), new_world)


def test_diehard():
	start_world = set([Cell(0,0), Cell(1,0), Cell(1,-1), Cell(5,-1), Cell(6,-1), Cell(7,-1), Cell(6,1)])

	diehard_lifecycle = [world for world in world_generator(start_world)]
	assert_equal(len(diehard_lifecycle), 130)
