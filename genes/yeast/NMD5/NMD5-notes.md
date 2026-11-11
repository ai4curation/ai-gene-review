# NMD5 (YJR132W, Kap119p) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

### Provenance / process
- `just fetch-gene yeast NMD5` created the UniProt, GOA (16 rows) and stub files.
- `just deep-research-falcon yeast NMD5 --fallback perplexity-lite` FAILED: Edison API
  returned "Failed to authenticate" (403), and the perplexity-lite fallback also failed.
  No deep-research file exists; the review is built from the literature read directly
  (PubMed search for Nmd5/Kap119 returned 14 records; the yeast-relevant ones were cached).
- ProtNLM2 output was not opened or used.

### Identity and family placement
- 1048 aa importin-beta-family karyopherin; Importin N-terminal (IBN_N, Ran-binding) domain
  at 24-104 (PROSITE PRU00115). Name "NMD5" is historical (He & Jacobson GenBank
  submission); there is no published evidence that Nmd5 acts in nonsense-mediated decay.
- PANTHER PTHR10997:SF18 (D-IMPORTIN 7_RANBP7), shared with Drosophila Msk/DIM-7,
  Arabidopsis SAD2, S. pombe SPCC550.11, Dictyostelium DDB_G0269860
  [file:interpro/panther/PTHR10997/PTHR10997-entries.csv]. Human IPO7 is in SF27 and IPO8
  in SF26 (same file), so vertebrate importin-7/8 are family-level, not subfamily-level,
  relatives. Other yeast PTHR10997 members: CSE1 (SF8, exportin-2), KAP114 (SF9),
  KAP120 (SF7), SXM1 (SF28).
- PAINT: all IBA terms come from PTN000108134 (family root, includes the exportin-2 clade).
  The import-receptor MF and import BP were explicitly negated (IRD) at PTN000108304
  (exportin branch). Nmd5 (SGD:S000003893) is itself a donor for GO:0061608 and GO:0006606
  at PTN000108134 [file:interpro/panther/PTHR10997/PTHR10997-paint.tsv]. The nuclear
  envelope IBD was seeded only by SGD:S000003207 and Q587E0, not by Nmd5.

### Experimental findings in S. cerevisiae (all establish import-receptor function)
- TFIIS (Dst1): Nmd5/Kap119p forms a ~stoichiometric cytoplasmic complex with TFIIS;
  RanGTP (not RanGDP) dissociates it and binds Kap119p; Kap119p binds FG nucleoporins
  (Nup1, Nup2, Nup159) in overlays; TFIIS is mislocalized to cytoplasm in kap119Δ; other
  Kap cargoes unaffected; Kap119p in nucleus and cytoplasm; kap119Δ viable with slightly
  longer doubling time [PMID:9852143].
- Hog1 MAPK: osmotic-stress nuclear import of phosphorylated Hog1 requires NMD5 and Ran,
  but not Kap60/Kap95 [PMID:9755161, abstract only].
- Crz1: NLS#1 (residues 394-422) recognised by Nmd5; direct binding of recombinant
  proteins; binding requires calcineurin dephosphorylation and is disrupted by
  Gsp1-GTP(Q71L); nmd5Δ blocks Crz1 import and CDRE-lacZ activity [PMID:11535618].
  Light-induced Crz1 nuclear localisation also Nmd5-dependent [PMID:23335962].
- Hsp70 Ssa4: Nmd5 required for starvation- and ethanol-induced nuclear accumulation of
  Ssa4 N-terminal domain; ethanol increases Nmd5-Ssa4 import complexes and Nmd5 docking
  at the NPC [PMID:11279056, PMID:15001563, abstracts only].
- Heterologous: Aspergillus AlcR is imported in yeast via Kap104, Sxm1 and Nmd5 (Nmd5 not
  shown to bind directly) [PMID:12684370, abstract only].

### What is established vs inferred (for transfer to Msk and other SF18 members)
- Experimentally established in yeast: nuclear import signal receptor activity
  (direct cargo binding + RanGTP-dissociation + in vivo requirement), RanGTP binding,
  FG-nucleoporin binding, protein import into nucleus, nucleus + cytoplasm location.
- Cargo identities (TFIIS, Hog1, Crz1, Ssa4) are yeast-specific facts and should not be
  transferred as such; the Hog1-MAPK import parallels Msk/DIM-7-mediated D-ERK import but
  that parallel is a hypothesis, not an inference licensed by PAINT.
- Not established: any role in NMD; nuclear export; nuclear-envelope residence beyond
  transient NPC docking.
