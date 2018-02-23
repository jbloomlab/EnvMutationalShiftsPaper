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

# Get site-specific RMSDcorrected values and whether the shift at a site is
# significant
RMSD_dict = {}
sig_dict = {}
with open('../BG505_to_BF520_prefs_dist.csv') as f:
	lines = f.readlines()[1:]
	for line in lines:
		elements = line.split(',')
		site = elements[0]
		# The numbering for this structure follows HXB2 numbering, but is
		# indexed at 1 where HBX2 is indexed at 512. Also, the first 29 resiudes
		# are not derived from Env, so those should be skipped
		try:
			site = int(site)
			if site >= 512 + 29:
				site = str(site-511)
			else:
				continue
		except ValueError:
			continue
		RMSDcorrected = elements[1]
		significant_shift = elements[6]
		RMSD_dict[site] = float(RMSDcorrected)
		sig_dict[site] = significant_shift
sig_sites = [site for site in sig_dict if sig_dict[site]=='True']
min_RMSD = min(RMSD_dict.values())
max_RMSD = max(RMSD_dict.values())
print "\nThe minimum and maximum RMSDcorrected values are:"
print "min: {0}".format(min_RMSD)
print "max: {0}".format(max_RMSD)

# Color residues by omega-by-site log10P values
sites_with_data = RMSD_dict.keys()
sites_not_in_structure = []
for site in sites_with_data:
	#print(site, RMSD_dict[site])
	cmd.alter("{0} and resi {1}".format(structure, site),
				"b = {0}".format(RMSD_dict[site]))
	if site not in unique_sites_in_structure:
		sites_not_in_structure.append(site)
color_scheme = 'white_red'
cmd.spectrum('b', color_scheme, structure, minimum=min_RMSD, maximum=max_RMSD)
print ("\nSites with data not in structure: {0}".format(
								', '.join(sites_not_in_structure)))
print ("Sites with significant shifts not in structure: {0}".format(
								', '.join(s for s in sig_sites
											if s in sites_not_in_structure)))

# Color residues lacking data black
#sites_lacking_data = [site for site in unique_sites_in_structure if site not in sites_with_data]
#if len(sites_lacking_data) > 0:
#	print ("\nThe following sites in the structure, but lacking data will be colored black: {0}".format(', '.join(sites_lacking_data)))
#	cmd.color('black', '{0} and resi {1}'.format(structure, '+'.join(sites_lacking_data)))

# Show significant sites as spheres
print ("\nThere are {0} sites with significant RMSD corrected values".format(len(sig_sites)))
print (', '.join(sig_sites))
cmd.select('sig_RMSDcorrected', '{0} and resi {1}'.format(structure, '+'.join(sig_sites)))
cmd.show('spheres', 'sig_RMSDcorrected')

# Report how many significant sites are in the structure
sig_site_in_structure = [site for site in sig_sites if site in unique_sites_in_structure]
print ("\nOf the significant sites, {0} of them are in the structure".format(len(sig_site_in_structure)))

# Identify sites that have substituted
substituted_sites = []
with open('../BG505_to_BF520_prefs_dist.csv') as f:
	lines = f.readlines()[1:]
	for line in lines:
		(site, RMSDcorrected, RMSDbetween,RMSDwithin, BG505, BF520, significant_shift, substituted) = line.split(',')[:8]
		# The numbering for this structure follows HXB2 numbering, but is
		# indexed at 1 where HBX2 is indexed at 512. Also, the first 29 resiudes
		# are not derived from Env, so those should be skipped
		try:
			site = int(site)
			if site >= 512 + 29:
				site = str(site-511)
			else:
				continue
		except ValueError:
			continue
		if substituted == 'True':
			substituted_sites.append(site)
substituted_sites = list(set(substituted_sites)) # for some reason, this is needed to handle duplicates
cmd.select('subs', structure + ' and resi ' + '+'.join(substituted_sites))
print("\nThere are {0} substituted sites:".format(len(substituted_sites)))
print(', '.join(substituted_sites))
