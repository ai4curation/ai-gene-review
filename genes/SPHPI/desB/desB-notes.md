# desB (Q5NTE5, Sphingomonas paucimobilis SYK-6 = Sphingobium sp. SYK-6) - curator notes

Deep research could not be run for this session; these notes were written by hand from the
cached publications and the UniProt record. No `-deep-research-*.md` file exists.

## Identity
- DesB, 418 aa, gallate dioxygenase. Unreviewed TrEMBL entry (PE 4), but the protein was purified
  and characterized in PMID:16030198 (abstract-only in cache).
- Two-domain fusion of the LigB-type (class III extradiol dioxygenase, Pfam PF02900) catalytic domain
  and a LigA-like domain (Pfam PF07746); CDD cd07950 Gallate_Doxase_N / cd07923 Gallate_dioxygenase_C.
  [PMID:16030198 "The amino acid sequences of the N-terminal region (residues 1 to 285) and the C-terminal region (residues 286 to 418) of DesB exhibited ca. 40% and 27% identity with the sequences of the PCA 4,5-dioxygenase beta and alpha subunits, respectively."]
  Same architecture as P. putida GalA (genes/PSEPK/galA).
- Homodimer: [PMID:16030198 "DesB produced in Escherichia coli was purified and was estimated to be a homodimer (86 kDa)."]

## Function
- [PMID:16030198 "DesB specifically attacked gallate to generate 4-oxalomesaconate as the reaction product."]
  Km gallate 66.9 uM, Vmax 42.7 U/mg. This is exactly GO:0036238 gallate dioxygenase activity
  (gallate + O2 = (1E)-4-oxobut-1-ene-1,2,4-tricarboxylate).
- Fe(II): not stated in the DesB abstract. Inferred from family: the LigB active-site Fe
  [PMID:15262932 "The crystallographic study revealed that the active site of LigB contains the Fe ion coordinated by His12, His61, and Glu242, and His195 is thought to act as the catalytic base ( 37 )."]
  and the related SYK-6 type II extradiol dioxygenase DesZ requires Fe2+
  [PMID:15262932 "These results suggested that DesZ requires Fe 2+ for its activity."]
  P. putida GalA experimentally uses Fe2+.

## Pathway / in vivo
- Syringate -> 3-O-methylgallate (DesA) -> gallate (LigM) -> OMA (DesB) -> LigU/LigJ/LigK lower pathway.
  [PMID:16030198 "In the 3MGA O-demethylation pathway, LigM converts 3MGA to gallate, and the resulting gallate appears to be degraded by a dioxygenase other than LigAB or DesZ."]
- [PMID:16030198 "(ii) the pathway involving LigM and DesB plays an especially important role in the growth of SYK-6 on syringate, and (iii) DesB and LigAB are involved in gallate degradation."]
- Earlier evidence of a gallate dioxygenase in SYK-6 extracts: [PMID:15262932 "Similarly, SYK-6 seemed to contain gallate dioxygenase."]

## Curation decisions
- GO:0016491 oxidoreductase activity (InterPro2GO): MODIFY -> GO:0036238 gallate dioxygenase activity.
- GO:0016702 dioxygenase (two O atoms) (ARBA): MODIFY -> GO:0036238 (is_a descendant).
- GO:0008198 ferrous iron binding (InterPro2GO, LigB domain): KEEP_AS_NON_CORE (family-level inference,
  cofactor not the core function).
- NEW GO:0036238 (IDA, PMID:16030198) and NEW GO:0019396 gallate catabolic process (IMP/IDA, PMID:16030198).
- No GO term for syringate catabolism exists (GO:1901065 syringal lignin catabolic process is for the polymer);
  not proposed.
