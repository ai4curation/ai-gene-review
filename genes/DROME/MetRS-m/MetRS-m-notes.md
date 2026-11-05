# MetRS-m review notes

- 2026-10-28: fetched Q9VFL5 (Swiss-Prot SYMM_DROME, GeneID 41733, FlyBase FBgn0027083). 17 GOA rows.
- Literature: PMID:22448145 (full text) is the key fly paper; no direct biochemistry, but genetic
  rescue by human MARS2 [PMID:22448145 "The fly and human cDNAs rescued the lethality associated with
  FB/Df and HV/Df, the strongest allelic combinations."]. PMID:26761199 catalogue review (TAS rows).
  PMID:25594180 (glial lipid droplets) phenotypic only - not used for new process terms.
- GO:0006431 methionyl-tRNA aminoacylation is shown as obsolete in GOA (OLS not yet updated); following
  the DARS2/TyrRS precedent the rows are MODIFIED to GO:0070127 tRNA aminoacylation for mitochondrial
  protein translation (methionine specificity carried by GO:0004825).
- GO:0006418 IEA -> MODIFY to GO:0070127 (descendant); GO:0004812 -> MODIFY to GO:0004825;
  GO:0000166 -> MODIFY to GO:0005524.
- Matrix location: predicted transit peptide + function (mt translation is intramatrix) + by-similarity
  to MARS2; matrix rows accepted.
- No NEW terms proposed: mutant phenotypes (ROS, lipid droplets, neurodegeneration, UPRmt) are
  indirect consequences of loss of mitochondrial translation.
