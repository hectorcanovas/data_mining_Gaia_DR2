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
ReadMe.txt      80          .    This file
table_3.dat     93        532    Entire sample.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: table_3.dat
--------------------------------------------------------------------------------
   Bytes Format  Units   Label    Explanations
--------------------------------------------------------------------------------
   2- 13  F12.8  deg     RAdeg      Right ascension (J2015.5)
  15- 26  F12.8  deg     DEdeg      Declination     (J2015.5)
  29- 38  F10.8  mas     plx        Parallax
  40- 51  F12.8  mas/yr  pmRA       Proper motion in Right Ascension
  53- 64  F12.8  mas/yr  pmDE       Proper motion in Declination
  66- 84  I19    ---     source_ID  Gaia DR2 Source ID
  87- 88  A2     ---     Control    Control sample membership (Y/N)
  90- 93  A4     ---     DOH        Candidate member by Dbscan/Optics/Hdbscan 
--------------------------------------------------------------------------------

Note: The astrometry is given in the Gaia DR2 catalogue epoch, J2015.5

Author's address:
    Hector Canovas Cabrera    <hcanovas@sciops.esa.in>

================================================================================
(End)            Hector Canovas Cabrera [ESA/ESAC]                  03-May-2019

