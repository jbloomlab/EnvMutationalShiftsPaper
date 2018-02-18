"""
This script is for coloring Env's structure by RSA

It is intended to be run in the PyMOL terminal as:
    run color_Env_entropy.py

Hugh Haddox, January-28-2016
"""

import pymol
from pymol import cmd

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
cmd.set_name(structure, '5VN3_trimer')
cmd.select('gp160', 'c;A,G')
cmd.create(structure, 'gp160')

# Read in RSA values from file
d = {}
with open ('5VN3_RSA_and_SS.txt') as f:
    for (i, line) in enumerate(f):
        line = line.strip().split(',')
        site = line[0]
        RSA = line[3]
        if i == 0:
            assert site == 'site'
            assert RSA == 'RSA'
        else:
            site = int(site)
            d[site] = float(RSA)

# Read in entropies from a file of amino-acid preferences (HXB2 numbering)
minRSA = min(d.values())
maxRSA = max(d.values())

print "The minimum and maximum RSA values are:"
print "min: %s"%minRSA
print "max: %s"%maxRSA

# Replace residue b-factors with RSA values
for site in d:
    cmd.alter("resi %d" % site, "b = %g" % d[site])

# cmd.hide('everything')
# cmd.bg_color('white')
cmd.show('surface', '5VN3')
cmd.select(None)
cmd.spectrum('b', 'blue_red', '5VN3', minimum=minRSA, maximum=maxRSA)

# Make sure all sites in the structure have an RSA value. Not all sites in the
# structure have RSA values, but it looks like the sites lacking them are all
# unresolved, but are still incorporated in the PDB file somehow, and so counted
# in the list of total sites.
sites_in_structure = []
cmd.iterate("(name ca)","sites_in_structure.append(resi)")
unique_sites_in_structure = []
for site in sites_in_structure:
	if site not in unique_sites_in_structure:
		unique_sites_in_structure.append(site)
sites_without_RSA_values = [
    site for site in unique_sites_in_structure
    if int(site) not in d.keys()
]

print("There are {0} sites in the structure".format(len(unique_sites_in_structure)))
print("We computed RSA values for {0} sites".format(len(d.keys())))
print("Here are a list of sites lacking RSA values:")
print(sites_without_RSA_values)
