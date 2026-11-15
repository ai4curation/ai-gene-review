# ddlA (Escherichia coli K-12, P0A6J8) notes

## Provenance

- Provider deep research (`just deep-research`) was **not** run for this gene; no
  `ddlA-deep-research-*.md` file exists. These notes summarise manual reading of
  the cached publications and the UniProt record. All cited papers are
  abstract-only in the cache except PMID:18304323 (full text).
- `just paint-losses ECOLI ddlA`: no IRD or IKR loss on the lineage.

## Literature summary

- E. coli has two D-Ala-D-Ala ligases, both cloned by complementing the
  ligase-deficient strain ST640
  [PMID:1993184 "Two distinct genes encoding D-alanine:D-alanine (D-Ala-D-Ala) ligase (ADP forming) activity in Escherichia coli have been cloned by complementation of E. coli strain ST640(lambda 112) deficient in D-Ala-D-Ala ligase activity"].
  ddlA was named by similarity to Salmonella ddlA, and both enzymes were purified
  and characterised kinetically
  [PMID:1993184 "Both DdlA and DdlB enzymes were purified to greater than 90% homogeneity and characterized kinetically."].
- UniProt reaction (from PMID:1993184): ATP-dependent ligation of two D-alanine
  [file:ECOLI/ddlA/ddlA-uniprot.txt "2 D-alanine + ATP = D-alanyl-D-alanine + ADP + phosphate +"].
  Cofactor (by similarity): [file:ECOLI/ddlA/ddlA-uniprot.txt "Binds 2 magnesium or manganese ions per subunit."]
- Localisation: detected in cytosolic fractions in two proteome studies
  (PMID:15911532 fractionation + 2-DE/MS; PMID:18304323 cytosol LC-MS/MS
  [PMID:18304323 "We performed approximately 200 individual LC-MS/MS runs of the E. coli MC4100 cytosol"]).
  The gene-level hit lists are in supplements not in the cache.
- Radiation screen (PMID:27718375): ddlA listed among 33 "uncommon" Keio hits
  with increased radiation sensitivity
  [PMID:27718375 "Our 76 genes includes 43 common genes and 33 uncommon (potentially novel) genes"];
  no mechanism. Treated as an indirect phenotype (MARK_AS_OVER_ANNOTATED),
  matching cysE and betB rows from the same screen.

## Curation decisions

- Core: D-alanine-D-alanine ligase activity; peptidoglycan biosynthetic process
  (performs the D-Ala-D-Ala step); cytosol.
- cytoplasm IEA: MODIFY to cytosol (gene already carries cytosol IDA/IBA).
- metal ion binding IEA: MODIFY to magnesium ion binding.
- ATP binding IEA: KEEP_AS_NON_CORE (substrate binding of the ATP-grasp ligase).
- response to X-ray IMP: MARK_AS_OVER_ANNOTATED.
- Open question: the relative physiological contribution of DdlA versus DdlB
  (the original ddl mutant ST640 maps to ddlB) is not resolved by the cached
  abstracts.
