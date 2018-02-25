# Using `PyMOL` to map shifts in amino-acid preferences on the structure of Env

The goal of this directory is to visualize site-specific shifts in amino acid preferences on the structure of Env.

## We examine the shifts in context of multiple conformations of Env

We will examine these shifts in context of multiple different Env conformations, including the "closed" receptor-unbound pre-fusion state, an intermediate receptor-bound state, and the post-fusion six-helix bundle. Specifically, we will examine the following experimentally determined structures, each of which are in or approximate one of these conformations:

* `5FYL`: Crystalized by [(Stewart-Jones et al, 2016, Cell)](https://doi.org/10.1016/j.cell.2016.04.010), this structure shows the BG505 Env in the "closed" receptor-unbound pre-fusion state. It is bound by the antibodies 35O22 and PGT122. We will remove these antibodies when we visualize the shifts on Env's structure.

* `5VN3`: Obtained via cryo-electron microscopy by [(Ozorowski et al, 2017, Nature)](https://doi.org/10.1038/nature23010), this structure shows the B41 Env in complex with CD4 and 17b, stabilized in a receptor-bound state. As above, we will remove both CD4 and 17b in our analysis so as to better visualize the shifts on this structure.

* `1AIK`: Crystalized by [(Chan et al, 1997, Cell)](https://www.sciencedirect.com/science/article/pii/S0092867400802056), this structure shows the post-fusion six-helix bundle. Only the gp41 helices that take part in this bundle were resolved (546-581 and 628-661). The rest of Env is not included. It turns out that none of the sites that we identify to have significant shifts in amino-acid preference are located within the six-helix bundle resolved in this structure. Note: there is also a more recent structure by [(Buzon et al, 2010, PLoS Pathogens)](https://doi.org/10.1371/journal.ppat.1000880) (`2X7R`) that includes additional adjacent residues (531-581 and 629-681). But even then, this structure only contains a single significantly shifted site (542).

* `1ENV`: This structure also shows the post-fusion six-helix bundle resolved between residues 541-588 and 628-665.

## Mapping shifts onto these structures using `PyMOL`

This directory has multiple `PyMOL` scripts for visualizing shifts in amino-acid preferences in context of these structures. There is one script for each structure, called `pymol_analysis_*.py`, where the `*` is the PDB code of the structure in question. To execute these scripts, simply open `PyMOL`, change to this directory in the `PyMOL` terminal, and enter the command:

    run {script_name}

## Results

### Clustering of sites in the six-helix bundle
There are multiple crystal structures of the six-helix bundle, each obtained by crystalizing fragments of gp41 that sum to about 80 residues in length. Of the four structures we examined (PDB codes: `1AIK`, `1ENV`, `1SZT` and `2X7R`), each of which resolve slightly different sets of sites, the one that resolved the most significantly shifted sites in our analysis was `1ENV`. Specifically, there are four shifted sites in this structure. Of relevance to the reviewer comment, this structure also has five substituted sites (i.e., sites that differ in wildtype amino-acid sequence between BG505 and BF520) (HXB2 numbering, `1ENV` numbering):

    * (542, 31), (582, 71), (583, 72), (587, 76)

In analyzing the structural proximity of the shifted and substituted sites, we found two clusters: one with four sites (three shifted sites and one substituted site) and another with two sites (one shifted site and one substituted site). A motivation of investigating the six-helix bundle was to look for clusters that were unique to this conformation. As it turns out, the observed clusters are also present in the pre-fusion conformation we initially analyzed. This is largely because each of these clusters is made up of sites that are all very close to one another in primary sequence. For this reason, and because only a small fraction of shifted sites are structurally resolved in the six-helix bundle, we decided not to statistically analyze this structure in the same way as we did the pre-fusion structure in Figure 7B-D.

However, as the observed clustering is still of interest, we added a new supplemental figure that highlights the larger of the two clusters (cite figure). Interestingly, all three of the shifted sites in this cluster are more mutationally tolerant in the BG505 structure, indicating that they are more structurally and functionally critical in BF520. For the two shifted sites that point into the core of the six helix bundle, this may have to do with the role of these residues in packing. However, since the BF520 structure has not been determined, it is difficult to test this hypothesis.

### Clustering of sites near the hydrophobic network of the CD4-bound structure

This figure shows a region of Env in the open CD4-bound state that is involved in mediating the large conformational changes that occur upon CD4 binding. Nearly one third of the significantly shifted sites (9/30) cluster within this region near a network of hydrophobic residues that help mediate this change. Side chains of sites that are shifted, sites in the hydrophobic network, and sites that have substituted are all shown as sticks and are colored according to the key. Most shifted sites do not directly contact network residues. But, their presence in this dynamic region makes it possible that they also influence Env's dynamics and that this accounts for their shifts in preference. One possibility is that these shifts are caused by substitutions at shifted sites or direct contacts between shifted and substituted sites. However, a visual inspection of this region shows that only a few of the shifted sites have substituted or are immediately adjacent to substituted sites, suggesting that shifts at these sites may be mediated by long-range epistatic interactions with distant substitutions. It is possible that these interactions are mediated through a larger network of residues that modulate Env's dynamics. Though this hypothesis is difficult to test.

### Trimer apex

308 (sub) - R in BG505, H in BF520
164 (shfted, contacts 308) - bulky hydrophobics in BG505, less bulky hydrophobics in BF520

### Scratch


The $\sim$80 residues per monomer that are resolved in this structure include four significantly shifted sites and five substituted sites.
Of these, three of the shifted sites (582, 583, and 587) and one substituted site (588) form a cluster at one end of the bundle, where we highlight the side chain of each site in a different color.
As shown in \FIG{prefsdist}D, each of the shifted sites are more tolerant of mutations in BG505 than in BF520, indicating they are of greater structural and functional importance in BF520.
For the two shifted sites that point inward towards the bundles core (583 and 587), this importance may involve in packing.
Based on this structure, it is difficult to discern if or how the substituted site may impact the preferences at the shifted sites nearby, in part since the arginine side chain is not fully resolved.

### Reviewer response

We added an entire supplemental figure on:
"Clusters of shifted and substituted sites in context of different conformations of Env"

512, 516, 520 (all in the fusion peptide?)


## To do

* Look at co-receptor binding site
