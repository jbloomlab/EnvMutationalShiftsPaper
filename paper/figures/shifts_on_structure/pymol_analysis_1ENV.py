"""
This is a PyMOL script for analyzing shifts in preferences on the structure 1ENV

This script is similar to `pymol_analysis_5FYL.py`, but performs the analysis on
the structure 1ENV instead of 5FYL.

This script intended to be run in the PyMOL terminal as:
    run pymol_analysis_1ENV.py

Hugh Haddox, February-18-2018
"""

# Imports
import pymol
from pymol import cmd

# Fetch structure
structure = '1ENV'
cmd.reinitialize()
cmd.delete('all')
cmd.fetch(structure) #, type='pdb1')

# Generate symmetry partners based on crystal structure, using a distance of
# 1.9 since this reproduces the timer without segments from any other adjacent
# monomers in the crystal structure
cmd.symexp(structure, structure, structure, 2.5)

# Tweak initial display and color of Env monomers
cmd.hide('everything')
cmd.bg_color('white')
cmd.show('cartoon')
cmd.color('grey40')
#cmd.set('cartoon_transparency', '0.5')
#cmd.set('cartoon_transparency', '0', structure)
