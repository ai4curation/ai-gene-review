# CDD1 (Q06549, YLR245C) notes

Module: `pyrimidine_salvage`, role = cytidine deaminase (EC 3.5.4.5). YeastCyc: CYTIDEAM2-RXN (YEAST-RNT-SALV), CYTIDEAM-RXN (dC, YEAST-SALV-PYRMID-DNTP).

## Evidence journal
- Activity [PMID:10501935 "Disruption of a unique ORF (Genbank accession No. U 20865) bearing homology with eucaryotic or bacterial cytidine deaminases abolished cytidine deaminase activity and resulted in 5-fluorocytidine resistance"]
- Not limiting [PMID:10501935 "a block in cytosine deaminase (Fcy1p), but not in cytidine deaminase (Cdd1p), constitutes a limiting step in cytidine utilisation as a UMP precursor"]
- Orphan editase [PMID:11292850 "only CDD1, a cytidine deaminase, is shown to have the capacity to carry out C-->U editing on a reporter mRNA"]; [PMID:11292850 "Naturally occurring yeast mRNAs edited to a significant extent by CDD1 were, however, not detected"]
- dC deamination (in vitro), homodimer, Zn [UniProt:Q06549]. YeastCyc's own pathway comment says Cdd1's role in deoxy salvage is doubtful.
- IntAct self-interaction from PMID:23267104 is from a S. pneumoniae interactome paper; attribution unverified.

## Decisions
- MF and cytidine rows ACCEPT; deoxycytidine catabolism non-core; deoxyribonucleoside salvage RCA MARK_AS_OVER_ANNOTATED; generic ARBA BPs MODIFY.
