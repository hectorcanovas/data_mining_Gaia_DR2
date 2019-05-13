Data:
This directory contains the analysis of the member candidates identified by DBSCAN, OPTICS, and HDBSCAN. In addition,
it contains extra tables downloaded from the SIMBAD service and complementary data. 


Software:
* 01_compare_outputs.ipynb       >>  Compare DBSCAN, OPTICS, and HDBSCAN outputs. Output: Fig. 6 of the article.

* 02_make_common.ipynb           >>  Creates Combined sample. It allows to choose among 3 combinations: (min/max/average). For the
                                     article we choose the minimum combination. Outputs:
                                     * Table 3 of the paper (in .vot/.tex/.dat) >> Input for CDS/VizieR.
                                     * "common_sample_case_0_vizier.txt" (VizieR input target list)
                                     * "common_sample_case_0_no_control_simbad.txt" (SIMBAD input target list, used to search for "new" targets).  

	** At this stage: upload "common_sample_case_0_no_control_simbad.txt" to SIMBAD using the "Identifier Query" mode with ""Query a list of
	identifiers option. The output (as May 10, 2019) contains SIMBAD records for 77 targets out 243 (391 of the common sample - 148 control
	elements), saved here as "simbad.xml"

* 03_compare_to_simbad.ipynb     >>  It reads the SIMBAD output ("simbad.xml") and it creates input file dor SIMBAD script to examine the literature
                                     citations to the objects in the common sample. Outputs:
                                     * "common_sample_case_0_no_control_simbad_out.txt": Input file for (http://simbad.u-strasbg.fr/simbad/sim-fscript)
                                     * "simbad_bibcodes.txt":                            Output of http://simbad.u-strasbg.fr/simbad/sim-fscript.


* 04_astrometry_ext.ipynb        >>  It creates Fig. 6 of the article, and a zoomed-in versino of it for further inspection.

* 05_astrometry_analysis.ipynb   >>  It creates Figs. 8, 9, and Tables 4,5 of the article. It reads Table 1 from Galli et al. 2018 (UpperSco Gaia DR1 sample)

* 06_estimate_Av.ipynb           >>  It computes the average optical extinction for a subsample of sources form the commo sample, using published values.
                                    Outputs: '06_estimate_Av.tex': published (Av) and Gaia Ag values for a subset of common sample sources,

* 07_create_CMD.ipynb            >>  It creates Fig. 7 of the article. It reads BT-Settl and PARSEC evolutionary tracks from my local library, and
                                     it creates the extinction vector using the average Ag derived by 06_estimate_Av.ipynb. 

* 08_IR_crossmatch.ipynb         >>  It crossmatches the common sample against 2MASS & WISE catalogues. It creates the input file to obtain the WISE
                                     1,2,3,4 maps from the IPAC webpage.

* 08_IR_crossmatch.ipynb         >>  It crossmatches the common sample against 2MASS & WISE catalogues and creates a table with good IR photometry
                                     containing 48 sources. It creates the input file to obtain the WISE 1,2,3,4 maps from the IPAC webpage
                                     ("08_IR_crossmatch_WISE_check.txt").

** At this stage: upload "08_IR_crossmatch_WISE_check.txt" to IPAC and download all WISE mapds for the IR-sample (48 elements).

* 09_make_WISE_maps.ipynb.ipynb  >>  It creates WISE 4 images for the 48 sources with good IR photometry. It then applies aperture photometry
                                     to estimate the SN at WISE 4 band and stores that info in "09_make_WISE_maps_0_w4_SN.vot"

* 10_make_photometry.ipynb       >> It creates the photometry table after removing the sources with SN < 4 at WISE 4, resulting in 48 sources.
                                    The code then creates a color-color plot and classifies the objects based on their IR-SED slope. This way
                                    we find 12 new discs. Outputs: Figs. 11, 12, and Ap.5 of the paper. Table Ap.4.

Data:

* simbad.xml                       >>  Output of uploading "common_sample_case_0_no_control_simbad.txt" to SIMBAD. Contains SIMBAD info for
                                       sources with SIMBAD record.
* simbad_bibcodes.txt              >>  Output of uploading "simbad.xml" to the SIMBAD scripting service, following the query described in Notebook 
                                       "03_compare_to_simbad.ipynb". It contains bibcodes for papers including common_sample sources.
* galli_2018.txt                   >>  Vizier Table from Galli 2018 et. al (UpperSco sample).
* 2015_dunham_OPH_YSO.vot          >>  Vizier Table from Dunham et al. 2015 (c2d/Oph sample)
* 2015_Rizutto.vot                 >>  Vizier Table from Rizutto et al. 2015 (UpperSco sample)
* 08_IR_crossmatch_WISE_check.txt  >>  Input file for IPAC/WISE.