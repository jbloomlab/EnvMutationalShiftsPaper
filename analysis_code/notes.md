# Notes on converting Hugh's code to this analysis

* Hugh's code built an alignment with `mafft`. But as far as I can tell, that alignment was never actually used for anything, since the manual alignment was used instead. So I have just gotten rid of the `mafft` alignment.
