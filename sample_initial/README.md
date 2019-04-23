Data:
This directory contains 3 different target lists from reference works on the Ophiuchus Region. Thos are:
* Wilking 2008: http://simbad.u-strasbg.fr/simbad/sim-ref?querymethod=bib&simbo=on&submit=submit+bibcode&bibcode=2008yCat.2289....0W
* Erickson et al. 2011: http://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/AJ/142/140
* Dunham et al. 2015: http://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/ApJS/220/11

Additionally, data from two generic articles describing ALL SFRs in the Galaxy are also included:
* Ribas et al. 2015: http://adsabs.harvard.edu/abs/2015A%26A...576A..52R
* Porras et al. 2003: http://vizier.cfa.harvard.edu/viz-bin/VizieR?-source=J/AJ/126/1916

* sample_initial_oph_x_gaia-result.vot >> Output of running the "gaia_query.sql" in this directory
in the Gaia DR2 archive.


Software:
* 00_read_generic_cats.ipynb  >>  First look to different SFR in the Galaxy
* 01_read_oph_cats.ipynb      >>  Obtain 2MASS IDs for the 3 Oph generic catalogues
* 02_create_Sample_Ini.ipynb  >>  Combine the previous result into 1 single file (after remocing duplicate targets). Prepare .vot file for Gaia query.
* 03_add_labels.ipynb         >>  Creates Initial Sample in article-loike format. Includes reference and Control (Y/N) informative labels.

* gaia_query.sql  >> ADQL query to crossmatch the initial sample against the the Gaia DR2 using the individual 2MASS IDs of the targets. The output is analysed in the "sample_control/" subdirectory.
