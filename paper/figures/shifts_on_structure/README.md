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

There are multiple crystal structures of the six-helix bundle, each obtained by crystalizing fragments of gp41 that sum to about 80 residues in length. Of the structures we examined (`1AIK`, `1ENV`, `1SZT` and `2X7R`), each of which resolve slightly different sets of sites, the structure that resolved the most sites that were significantly shifted in our analysis was `1ENV`. Specifically, this structure has four shifted sites. Of relevance to the reviewer comment, it also had five substituted sites (i.e., sites that differ in wildtype amino-acid sequence between BG505 and BF520) (HXB2 numbering, `1ENV` numbering):

    * (542, 31), (582, 71), (583, 72), (587, 76)

In analyzing the structural proximity of shifted and substituted sites, we found two clusters: one with four sites (three shifted sites and one substituted site) and another with two sites (one shifted site and one substituted site). A motivation of investigating the six-helix bundle was to look for clusters that were unique to this conformation. As it turns out, the observed clusters are also present in the pre-fusion conformation we initially analyzed. This is largely because each of these clusters is made up of sites that are all very close to one another in primary sequence. For this reason, and because only a small fraction of shifted sites are structurally resolved in the six-helix bundle, we decided not to statistically analyze this structure in the same way as we did for the pre-fusion structure in Figure 7B-D.

However, we did add a new supplemental figure to highlight the larger of the two clusters described above (cite figure). Interestingly, all three of the shifted sites in this cluster are more mutationally tolerant in the BG505 structure, indicating they are more critical for the structural and functional integrity of BF520. For the two shifted sites that point into the core of the six helix bundle, this may have to do with the role of these residues in packing. However, since the BF520 structure has not been determined, it is difficult to test this hypothesis.

## To do

* Analyze clusters. Is there any structural significance? E.g., what about the cluster of residues at the trimer apex of `5VN3`? Could sites be involved in co-receptor interface, or the conformational change induced by receptor binding?
