# Comparing mutational effects in two homologs of HIV Env
This repository contains the code used to compare the mutational effects in the BG505 and BF520 homologs of HIV Env.

## Authors
Hugh Haddox and Adam Dingens performed the experiments.
Sarah Hilton and Jesse Bloom developed the capabilities to use gamma-distributed models in [phydms](http://jbloomlab.github.io/phydms/).
Hugh led the analysis, with some help from Jesse and Adam.

## Analysis
The actual analysis is performed by the Jupyter notebook [analysis_notebook.ipynb](analysis_notebook.ipynb).
The analysis primarily uses [dms_tools2](https://jbloomlab.github.io/dms_tools2/), and also makes some use of [phydms](http://jbloomlab.github.io/phydms/).

## Input data
All input data required by [analysis_notebook.ipynb](analysis_notebook.ipynb) is in the [./data/](./data/) subdirectory. 
Specifically, this subdirectory includes the following files:

    * The wildtype *env* coding sequences for the BG505 and BF520 strains used in the experiments are in [./data/BG505_env.fasta](./data/BG505_env.fasta) and [./data/BF520_env.fasta](./data/BF520_env.fasta).

    * A protein alignment of the Env homologs used in this study plus HXB2 is in [./data/Env_protalignment_manualtweaks.fasta](./data/Env_protalignment_manualtweaks.fasta). This is a manually tweaked version of an alignment created by [mafft](https://mafft.cbrc.jp/alignment/software/). The alignment is used to get the other homologs into the HXB2 numbering scheme. The manual tweaking was done by Hugh Haddox in regions of the variable loops, which are hard to align due to low identity and many indels. Specifically,. Hugh notes that he:
        - re-aligned BF520 in the regions between 184-191 (noninclusive bounds in variable loop 1; HXB2 numbering) and 395-412 (noninclusive bounds in variable loop 4; HXB2 numbering). 
        - re-aligned LAI in the region between 137-144 (noninclusive bounds in variable loop 1; HXB2 numbering). 

    * An alignment of HIV Env coding sequences is in [./data/HIV1_FLT_2016_env_DNA.fasta](./data/HIV1_FLT_2016_env_DNA.fasta). This alignment is used for the phylogenetic analyses. This alignment was downloaded from the [Los Alamos (LANL) HIV sequence database](http://www.hiv.lanl.gov/). Specifically, it was downloaded using the following settings:
        - Alignment type: Filtered web
        - Organism: HIV-1/SIVcpz
        - Region: Env
        - Subtype: M group without recombinants (A-K)
        - DNA/Protein: DNA 
        - Year: 2016
        - Format: FASTA

    * A breakdown of Env into regions (*gp41*, *gp120 variable loops*, *gp120 other regions*) in HXB2 nubmering is in [./data/Env_regions.csv](./data/Env_regions.csv). The variable loop definitions are the [ones provided by the Los Alamos database](https://www.hiv.lanl.gov/content/sequence/VAR_REG_CHAR/variable_region_characterization_explanation.html). The gp41 definition is also the one provided at that site.

