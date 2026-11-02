# CYS3 (YAL012W, P31373) notes

Evidence journal for the review (no paid deep research run; built from UniProt and cached publications).

## Identity and activity
- Cystathionine gamma-lyase, EC 4.4.1.1; PLP enzyme, homotetramer [UniProt:P31373].
- CYS3 is the structural gene: purified gamma-CTLase N-terminus matched CYS3 [PMID:8511969 "leading to the conclusion that CYS3 is the structural gene for gamma-CTLase"]; cloning [PMID:1577698 "CYS3 (CYI1) was concluded to be the structural gene for this enzyme"].
- Recombinant enzyme has several cystathionine-related activities [PMID:8335636 "The protein showed a number of cystathionine-related activities, i.e., cystathionine beta-lyase (EC 4.4.1.8), cystathionine gamma-lyase, and cystathionine gamma-synthase (EC 4.2.99.9) with L-homoserine as substrate."]; the gamma-synthase activity is non-physiological because O-succinylhomoserine is absent in yeast [PMID:1577698 "propose that their different in vivo functions are due to the unavailability of O-succinylhomoserine in S. cerevisiae"].
- C-S lyase on a cysteine-furfural conjugate, giving 2-furfurylthiol [PMID:29436228 "Str3p and Cys3p were able to cleave the cysteine-furfural conjugate to release 2-furfurylthiol."].

## Pathway role
- Yeast makes cysteine only from homocysteine via CBS (Cys4) and CGL (Cys3) [PMID:10509018 "cysteine is synthesized exclusively through the pathway constituted with beta-CTSase and gamma-CTLase"]; [PMID:8366024 "The only phenotypic consequence of the inactivation of STR1 or STR4 is cysteine auxotrophy."].
- H2S: CYS3 overexpression raises H2S; TORC1-Sch9 controls CYS3/CYS4 mRNA [PMID:31582588 "Overexpressing CYS3 significantly increased H2S production by WT cell."]. The regulator is Sch9, not Cys3, so the regulation term was changed (MODIFY) to H2S biosynthetic process.

## Curation decisions
- Obsolete GO:0019346 transsulfuration (3 rows): MODIFY to GO:0019344 L-cysteine biosynthetic process (QuickGO lists GO:0019344 and GO:0071269 as consider-replacements).
- GO:0006567 L-threonine catabolic process (RCA, THREOCAT2-PWY): REMOVE. Pathway artefact, probably from the shared product 2-oxobutanoate.
- Nucleus HDA: non-core.
