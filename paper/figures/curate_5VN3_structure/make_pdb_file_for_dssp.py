"""
This script is for loading 5VN3 and removing non-Env chains

It is intended to be run in the PyMOL terminal as:
    run make_pdb_file_for_dssp.py

Hugh Haddox, February-17-2018
"""
import pymol
from pymol import cmd, stored

# Input variables
structure = '5VN3'

# Clear pymol, get structure, and remove non-Env chains
# gp41 = chain A, B, D
# gp120 = chain G, I, J
# CD4 = chains C, E, F
# 17b = chains H, K, M and L, N, O
cmd.delete('all')
cmd.fetch(structure) #, type='pdb1')
cmd.remove ('c;C,E,F,H,K,M,L,N,O')

cmd.save('5VN3_Env_trimer.pdb')
