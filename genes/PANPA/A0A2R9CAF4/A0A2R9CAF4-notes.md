# A0A2R9CAF4 (bonobo SLC26A11) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 prediction files were not opened or used.

### Identity
- A0A2R9CAF4 (TrEMBL, PE 3) is 606 aa, the same length as human SLC26A11 Q86WA9 (606 aa).
  Global alignment: 601/606 identical, no gaps (99.2%); vs mouse Q80ZD3 (593 aa) 82.5%
  [file:PANPA/A0A2R9CAF4/A0A2R9CAF4-bioinformatics/RESULTS-rereview.md].
- Not a fragment, isoform or alternative gene model. UniProt CTD xref 284129 = human SLC26A11 gene.
- Human Glu-320 (pH-sensing residue, PMID:42509233) conserved as E320.
- PANTHER: UniProt gives family PTHR11814 only. The PANTHER API places human SLC26A11 and mouse
  Slc26a11 in PTHR11814:SF55 (SODIUM-INDEPENDENT SULFATE ANION TRANSPORTER). Bonobo is not a PANTHER
  genome, so the subfamily is inferred from one-to-one orthology. The PAINT IBD for GO:1902358
  sulfate transmembrane transport is at PTN000212046, with Q86WA9 among its seeds.

### Literature (cached)
- PMID:42509233 (Kuhn et al. 2026, full text): purified human SLC26A11 performs proton:sulfate symport
  coupled to chloride antiport and also has an uncoupled chloride conductance. It is a homodimer and
  is lysosomal in mammalian cell lines. Bicarbonate and phosphate had no effect on transport.
- PMID:21716257 (Xu 2011, mouse kidney): apical (A-IC) and basolateral (B-IC) plasma membrane with
  V-ATPase. Cl-/HCO3- exchange was inferred from pHi assays in COS7 cells.
- PMID:23733100 (Rahmati 2013): mouse Slc26a11 is a chloride channel in HEK293 and is on the Purkinje cell plasma membrane.
- PMID:12626430 (Vincourt 2003): human SLC26A11 reaches the cell membrane and transports sulfate independently of Na+.
- PMID:37380823 (Wei 2023): chloride entry and swelling in hypoxic neurons. This is pathological context and
  is not annotated as a process.
- A DOI in the falcon report (10.3390/ijms25084190 = PMID:38673775) is an SLC26A4 review, not an
  SLC26A11 localization paper. The Manders coefficients and the "50-fold" affinity figure in the report
  were not verified and were dropped from the description.

### Decisions changed from the previous draft
- GO:0008271 changed to MODIFY → GO:0008512 sulfate:proton symporter activity (is_a GO:0008271).
- General terms (membrane, inorganic anion transport, transmembrane transport, monoatomic anion
  transport and transporter activity) changed from KEEP_AS_NON_CORE/over-annotated to MODIFY, with
  specific replacements already on the gene.
- Apical and basolateral plasma membrane changed from MARK_AS_OVER_ANNOTATED to KEEP_AS_NON_CORE,
  because in vivo mouse kidney immunostaining supports them.
- GO:0140900 chloride:bicarbonate antiporter changed from MODIFY (a lateral replacement) to
  MARK_AS_OVER_ANNOTATED: the claim is disputed and only indirect cellular evidence supports it.
- Chloride transmembrane transport changed to ACCEPT.

### Relative to review next
- Human SLC26A11 (Q86WA9) is the one-to-one ortholog in the same PANTHER subfamily SF55 and is the
  subject of the definitive biochemistry. It has no review in the repo.
