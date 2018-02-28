# Name: Fire
# Dimensions: 2

# --- Set up executable path, do not edit ---
import sys
import inspect
this_file_loc = (inspect.stack()[0][1])
main_dir_loc = this_file_loc[:this_file_loc.index('ca_descriptions')]
sys.path.append(main_dir_loc)
sys.path.append(main_dir_loc + 'capyle')
sys.path.append(main_dir_loc + 'capyle/ca')
sys.path.append(main_dir_loc + 'capyle/guicomponents')
# ---

from capyle.ca import Grid2D, Neighbourhood, CAConfig, randomise2d
import capyle.utils as utils
import numpy as np

def initGrid_func(grid):
    grid[:,:] = 0
    for i in range(10,14)
        for j in range(5,14)
            grid[i,j] = 1
    for i in range(5,34)
        for j in range(32,34)
            grid[i,j] = 2
    for i in range(30,39)
        for j in range(15,24)
            grid[i,j] = 3
            
    return grid

def transition_func(grid, neighbourstates, neighbourcounts):
    # dead = state == 0, live = state == 1
    # unpack state counts for state 0 and state 1
    dead_neighbours, live_neighbours = neighbourcounts
    # create boolean arrays for the birth & survival rules
    # if 3 live neighbours and is dead -> cell born    
    birth = (live_neighbours == 3) & (grid == 0)
    # if 2 or 3 live neighbours and is alive -> survives
    survive = ((live_neighbours == 2) | (live_neighbours == 3)) & (grid == 1)
    if grid[11,6] != 1
        grid = initGrid_func(grid)
    #Else will be who survives.
    # Set cells to 1 where either cell is born or survives
    grid[birth | survive] = 1
    return grid
 
 
def setup(args):
    config_path = args[0]
    config = utils.load(config_path)
    # ---THE CA MUST BE RELOADED IN THE GUI IF ANY OF THE BELOW ARE CHANGED---
    config.title = "Fire"
    config.dimensions = 2
    config.states = (0,1,2,3,4,5)
    # ------------------------------------------------------------------------
    
    # ---- Override the defaults below (these may be changed at anytime) ----
    
    config.state_colors = [(0.74,0.725,0.125),(0.19,0.355,0.645),(0.375,0.375,0.375),(0.14,0.355,0.17),(1,0,0),(0,0,0)]
    config.num_generations = 150
    config.grid_dims = (50,50)
    
    # ----------------------------------------------------------------------
    
    if len(args) == 2:
        config.save()
        sys.exit()
        
    return config
    
def main():
    # Open the config object
    config = setup(sys.argv[1:])
 
    # Create grid object
    grid = Grid2D(config, transition_func)
    
    # Run the CA, save grid state every generation to timeline
    timeline = grid.run()
 
    # save updated config to file
    config.save()
    # save timeline to file
    utils.save(timeline, config.timeline_path)
    
if __name__ == "__main__":    
    main()
 
 
    
