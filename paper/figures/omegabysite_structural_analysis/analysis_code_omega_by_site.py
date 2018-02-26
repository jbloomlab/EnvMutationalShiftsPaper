"""
This script is for analyzing omega-by-site values in PyMOL

It is intended to be run in the PyMOL terminal as:
	run analysis_code_omega_by_site.py

Hugh Haddox, November-2-2017
"""

# Imports
import pymol
from pymol import cmd
import math

homologs = ['BG505', 'BF520']
for h in homologs:

	# Fetch structure
	structure = '5fyl'
	cmd.reinitialize()
	cmd.delete('all')
	cmd.fetch(structure) #, type='pdb1')

	# Remove non-Env chains
	# gp41 = chain B
	# gp120 = chain G
	# 35O22 = chains D and E
	# PGT122 = chains H and L
	cmd.remove ('c;D,E,H,L,U,V')
	cmd.symexp(structure, structure, structure, 3) # generate symmetry partners based on crystal structure

	# Tweak initial display and color of Env monomers
	cmd.hide('everything')
	cmd.bg_color('white')
	cmd.show('cartoon')
	cmd.color('grey40')
	#cmd.color('grey20', structure)
	cmd.set('cartoon_transparency', '0.5')
	cmd.set('cartoon_transparency', '0', structure)
	#cmd.hide('hetatm')

	# Identify unique sites in structure
	sites_in_structure = []
	cmd.iterate("(name ca)","sites_in_structure.append(resi)")
	unique_sites_in_structure = []
	for site in sites_in_structure:
		if site not in unique_sites_in_structure:
			unique_sites_in_structure.append(site)

	# Get omega-by-site values and determine which sites evolve significantly
	# faster or slower than expected
	omega_d = {'BG505':{}, 'BF520':{}}
	sites_sig_fast = {'BG505':[], 'BF520':[]}
	sites_sig_slow = {'BG505':[], 'BF520':[]}
	Q_cutoff = 0.05
	with open('../merged_omegabysite.csv') as f:
		lines = f.readlines()[1:]
		for line in lines:
			(site, omega, P, dLnL, Q, Env, log10Q, log10Qdir, N_glycans) = line.strip().split(',')
			omega_d[Env][site] = float(log10Qdir)
			if float(Q) < Q_cutoff and float(omega) < 1.0:
				sites_sig_slow[Env].append(site)
			if float(Q) < Q_cutoff and float(omega) > 1.0:
				sites_sig_fast[Env].append(site)
	min_omega = min(omega_d['BG505'].values() + omega_d['BF520'].values())
	max_omega = max(omega_d['BG505'].values() + omega_d['BF520'].values())
	print "\nThe minimum and maximum omega-by-site values are:"
	print "min: {0}".format(min_omega)
	print "max: {0}".format(max_omega)

	# Color residues by omega-by-site log10Q values

	BG505_sites = sorted(omega_d['BG505'].keys())
	BF520_sites = sorted(omega_d['BF520'].keys())
	assert BG505_sites == BF520_sites
	sites_with_data = BG505_sites
	sites_not_in_structure = []
	for site in sites_with_data:
		cmd.alter("{0} and resi {1}".format(structure, site), "b = {0}".format(omega_d[h][site]))
		if site not in unique_sites_in_structure:
			sites_not_in_structure.append(site)
	cutoff_min_omega = -6
	cutoff_max_omega = 6
	if cutoff_min_omega:
		print("Using manually specified min and max omega values of {0} and {1}".format(
			cutoff_min_omega, cutoff_max_omega
		))
	cmd.spectrum('b', 'blue_white_red', structure,
					minimum = cutoff_min_omega, maximum = cutoff_max_omega)
	print ("\nSites with data not in structure: {0}".format(', '.join(sites_not_in_structure)))

	# Color residues lacking data black
	sites_lacking_data = [site for site in unique_sites_in_structure if site not in sites_with_data]
	print ("\nThe following sites in the structure, but lacking data will be colored white: {0}".format(', '.join(sites_lacking_data)))
	cmd.color('black', '{0} and resi {1}'.format(structure, '+'.join(sites_lacking_data)))

	# Show significant sites as spheres
	print ("\nUsing a Q-value cutoff of {0}".format(Q_cutoff))
	print ("\n{0} sites that evolve slower than expected with significant Q values: {1}".format(len(sites_sig_slow[h]), ', '.join(sites_sig_slow[h])))
	print ("\n{0} sites that evolve faster than expected with significant Q values: {1}".format(len(sites_sig_fast[h]), ', '.join(sites_sig_fast[h])))
	cmd.select('sites_sig_slow', '{0} and resi {1}'.format(structure, '+'.join(sites_sig_slow[h])))
	cmd.select('sites_sig_fast', '{0} and resi {1}'.format(structure, '+'.join(sites_sig_fast[h])))
	cmd.show('spheres', 'sites_sig_fast')
	cmd.show('spheres', 'sites_sig_slow')

	# Take a pictures of Env rotated 120 degrees relative to one another
	cmd.set_view ("""\
		 0.413237274,    0.018612767,   -0.910427451,\
		 0.910516560,    0.006436472,    0.413409144,\
		 0.013554142,   -0.999800861,   -0.014289021,\
		-0.000450239,   -0.000266090, -364.028167725,\
		64.596366882,   39.767127991,   -5.709826946,\
	   224.197448730,  503.894958496,  -20.000000000""")
	take_pictures = True
	if take_pictures:
		cmd.bg_color('white')
		cmd.png('{0}_face1.png'.format(h), width=1000, dpi=1000, ray=1)
		cmd.rotate('y', '120')
		cmd.png('{0}_face2.png'.format(h), width=1000, dpi=1000, ray=1)

# Annotations of structural features
# gp120 and gp41
cmd.select('gp120', structure + ' and resi 31-511')
cmd.select('gp41', structure +' and resi 512-664')

# Variable loops
cmd.select('c1', structure +' and resi 31-131')
cmd.select('v1', structure +' and resi 132-156')
cmd.select('v2', structure +' and resi 158-195')
cmd.select('c2', structure +' and resi 196-295')
cmd.select('v3', structure +' and resi 296-330')
cmd.select('c3', structure +' and resi 331-385')
cmd.select('v4', structure +' and resi 386-417')
cmd.select('c4', structure +' and resi 418-459')
cmd.select('v5', structure +' and resi 460-470')
cmd.select('c5', structure +' and resi 471-511')
cmd.select('vloops', 'v1 v2 v3 v4 v5')

# Disulfides
cmd.select('disulfides', structure +' and resi 54+74+119+126+131+157+196+205+218+228+239+247+296+331+378+385+418+445')

# CD4 binding site
cmd.select('cd4bs', structure +' and resi 124-127+196+198+279-283+365-370+374+425-432+455-461+469+471-477') # Zhou et al. 2010 PMID 20616231; Supplemental Fig. S1

# co-receptor binding site
cmd.select('cxcr4_bs_mutagenesis', structure +' and resi 298+308+315+317+421+422') # Basmaciogullari et al., 2002
cmd.select('ccr5_bs_mutagenesis', structure +' and resi 121+123+207+381+420+421+422+438+440+441') # Rizzuto et al., 1998
cmd.select('coreceptor_bs_GPGR', structure +' and resi 312-315')

# Antibody epitopes determined in previous computational analyses
cmd.select('CD4bs_epitope', structure + ' and resi 96+97+98+102+122+124+198+275+276+278+279+280+281+282+283+354+357+365+366+367+368+370+371+425+426+427+428+429+430+431+432+455+456+457+458+459+460+461+462+463+465+466+467+469+472+473+474+476+480')
cmd.select('V3_epitope', structure + ' and resi 135+136+137+156+301+322+323+324+325+326+327+328+330+332+373+384+386+389+392+409+415+417+418+419+442+444')
cmd.select('V1_V2_epitope', structure + ' and resi 156+158+160+162+163+164+165+166+167+168+169+170+171+172+173')
cmd.select('gp120_gp41_epitope', structure + ' and resi 44+45+46+58+80+82+83+84+85+87+88+90+91+92+93+94+229+230+231+232+234+237+238+240+241+245+246+262+276+277+278+352+448+462+512+513+514+515+516+517+518+519+520+521+522+527+529+542+543+549+550+554+592+611+613+615+616+617+618+620+621+624+625+627+629+630+632+633+634+636+637+638+640+641+643+644+647')
cmd.select('fusion_peptide', structure + ' and resi 512-527')
cmd.select(None)
