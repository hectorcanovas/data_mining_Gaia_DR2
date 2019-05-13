X/YYY      Census of Rho Oph candidate members from Gaia DR2 (Canovas +2019)
================================================================================
Census of Rho Oph candidate members from Gaia Data Release 2
     Canovas H., Cantero C., Cieza L., Bombrun A., Lammers U., Merin B.,
     Mora A., Ribas A., Ruiz-Rodriguez D.
    <Astron. Astrophys., XXX, YY-ZZ (2019)>
    =2019A&AS..XXX...YYZ 
================================================================================
Keywords: astrometry - data analysis - pre-main sequence  - circumstellar matter
ADC_Keywords: Cross identifications ; Astrometric data
Mission_Name: Gaia

Abstract:
    The Ophiuchus cloud complex is one of the best laboratories to study the
    earlier stages of the stellar and protoplanetary disc evolution. We
    constructed a control sample composed of 188 bona fide Ophiuchus members.
    Using this sample as a reference we applied three different density-based
    machine learning clustering algorithms (DBSCAN, OPTICS, and HDBSCAN) to a
    sample drawn from the Gaia DR2 catalogue centred on the Ophiuchus cloud
    that contains 2300 sources covering a sky area of 38deg^2. The
    clustering analysis was applied in the five astrometric dimensions defined
    by the three-dimensional Cartesian space and the proper motions in right
    ascension and declination. The three clustering algorithms systematically
    identify a similar set of candidate members in a main cluster with
    astrometric properties consistent with those of the control sample. We
    constructed a common sample containing 391 member candidates including 166
    new objects, which have not yet been discussed in the literature. We built
    the SEDs for a subset of 48 objects and found a total of 41 discs.

Description:
    This table contains the initial sample described in Sect. 2.1 of the
    article. 


File Summary:
--------------------------------------------------------------------------------
 FileName    Lrecl    Records    Explanations
--------------------------------------------------------------------------------
readme.txt      80          .    This file
tab_3.dat       93        532    Entire sample of candidate members.
tab_ap_1.dat    51        470    Initial sample.
tab_ap_4.dat    242        48    Photometry for subset of 48 candidate members.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: tab_3.dat
--------------------------------------------------------------------------------
   Bytes Format  Units   Label    Explanations
--------------------------------------------------------------------------------
   2- 13  F12.8  deg     RAdeg      Right ascension (J2015.5)
  15- 26  F12.8  deg     DEdeg      Declination     (J2015.5)
  29- 38  F10.8  mas     plx        Parallax (J2015.5)
  40- 51  F12.8  mas/yr  pmRA       Proper motion in Right Ascension (J2015.5)
  53- 64  F12.8  mas/yr  pmDE       Proper motion in Declination (J2015.5)
  66- 84  I19    ---     source_ID  Gaia DR2 Source ID
  87- 88  A2     ---     Control    Control sample membership (Y/N)
  90- 93  A4     ---     DOH        Candidate member by Dbscan/Optics/Hdbscan 
--------------------------------------------------------------------------------

Byte-by-byte Description of file: tab_ap_1.dat
--------------------------------------------------------------------------------
   Bytes Format  Units   Label    Explanations
--------------------------------------------------------------------------------
   2- 18  A17    ---     2MASS    2MASS Source ID
  20- 27  A8     ---     Ref      References (1)
  29- 30  A2     ---     Control  Control Sample Membership 
  32- 51  I20    ---     DR2      Gaia DR 2 Source ID
--------------------------------------------------------------------------------

Notes (1): References are: (1) = Wilking  2008 (2008hsf2.book..351W), 
	(2) = Erickson et al. 2011 (2011AJ....142..140E),	(3) = Dunham et al. 2015
  (2015ApJS..220...11D)
--------------------------------------------------------------------------------

Byte-by-byte Description of file: tab_ap_4.dat
--------------------------------------------------------------------------------
   Bytes Format  Units   Label    Explanations
--------------------------------------------------------------------------------
   2-20   I19    ---   source_ID  Gaia DR2 Source ID
  23-30   E8.2  W/m2   GFlux      Observed Flux at Gaia G passband
  33-40   E8.2  W/m2   e_GFlux    1 sigma error on GFlux  
  43-50   E8.2  W/m2   BPFlux     Observed Flux at Gaia G_BP passband
  53-60   E8.2  W/m2   e_BPFlux   1 sigma error on BPFlux
  63-70   E8.2  W/m2   RPFlux     Observed Flux at Gaia G_RP passband
  73-80   E8.2  W/m2   e_RPFlux   1 sigma error on RPFlux
  83-90   E8.2  W/m2   JFlux      Observed Flux at 2MASS J passband
  93-100  E8.2  W/m2   e_JFlux    1 sigma error on JFlux  
  103-110 E8.2  W/m2   HFlux      Observed Flux at 2MASS H passband
  113-120 E8.2  W/m2   e_HFlux    1 sigma error on HFlux
  123-130 E8.2  W/m2   KsFlux     Observed Flux at 2MASS Ks passband
  133-140 E8.2  W/m2   e_KsFlux   1 sigma error on KsFlux
  143-150 E8.2  W/m2   W1Flux     Observed Flux at WISE W1 passband
  153-160 E8.2  W/m2   e_W1Flux   1 sigma error on W1Flux
  163-170 E8.2  W/m2   W2Flux     Observed Flux at WISE W2 passband
  173-180 E8.2  W/m2   e_W2Flux   1 sigma error on W2Flux
  183-190 E8.2  W/m2   W3Flux     Observed Flux at WISE W3 passband
  193-200 E8.2  W/m2   e_W3Flux   1 sigma error on W3Flux
  203-210 E8.2  W/m2   W4Flux     Observed Flux at WISE W4 passband
  213-220 E8.2  W/m2   e_W4Flux   1 sigma error on W4Flux
  223-233 A11   ---    SED        SED class (as detailed in Sect. 4.2)
  236-242 A7    ---    status     Indicates previous observations (if any) (1)
 -------------------------------------------------------------------------------
  Notes: (1) Possible values are "control": the source belongs to the control
             sample; "new": there is no literature record of this source in
             SIMBAD; "other": there is at least 1 literature record of the
             source in SIMBAD.

Author's address:
    Hector Canovas Cabrera    <hcanovas@sciops.esa.in>

================================================================================
(End)            Hector Canovas Cabrera [ESA/ESAC]                  09-May-2019

