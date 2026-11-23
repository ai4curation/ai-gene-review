# ilv5 (SPBC56F2.12, UniProt P78827) notes

- Ketol-acid reductoisomerase (EC 1.1.1.86), ortholog of S. cerevisiae ILV5. [PMID:35325114 "by acetohydroxyacid reductoisomerase, which is predicted to be encoded by ilv5+"]; Mg2+ requirement shown for S. pombe crude enzyme [PMID:35325114 "it has been confirmed that at least the reaction using (S)-2-aceto-2-hydroxybutanoate as a substrate requires Mg2+ in S. pombe"].
- Mitochondrial: [PMID:35325114 "Like ALS, the protein encoded by ilv5+ is localized in the mitochondria (Matsuyama et al. 2006)."]; UniProt has a transit peptide of undetermined length.
- UniProt catalytic activities cover both acetolactate (Rhea:22068) and acetohydroxybutanoate (Rhea:13493) [UniProt:P78827].
- GOA lacks an isoleucine BP although UniProt pathway lists step 2/4 of isoleucine synthesis and the PomBase GO-CAM places ilv5 part_of GO:1901705 -> proposed NEW GO:1901705 (ilv5 itself catalyses the step).
- GOA ISS "L-leucine metabolic process" (GO:0006551, from S. cerevisiae ILV5) -> MODIFY to GO:0009098. The PomBase GO-CAM leucine-branch ilv5 activity also uses GO:0006551 (module notes flag this).
- generic oxidoreductase activity -> MODIFY to GO:0004455 (as in S. cerevisiae ILV5 review).
- S. cerevisiae Ilv5 moonlights in mtDNA nucleoid stability; no S. pombe data and no such annotation in GOA for ilv5. Not a core function here (differs from the S. cerevisiae review, which has a second core function for dsDNA binding).
