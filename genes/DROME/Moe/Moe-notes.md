# Moe review notes

## Session 1 (create review)

- Fetched with `just fetch-gene DROME Moe`; UniProt P46150 confirmed; 110 GOA rows.
- No deep-research provider available; literature synthesis in `Moe-deep-research-manual.md`.
- Full text read: PMID:18283112 (Carreno 2008, mitotic cortex/Slik), PMID:23857773
  (microtubule binding), PMID:16216927 (TRP/TRPL), PMID:16887114 (DRok), PMID:23468526
  (Conu), PMID:23544124 (Wengen), PMID:24413568 (Btsz), PMID:25061859 (Slik/Btl),
  PMID:25065756 (Syx7/endocytosis), PMID:20237161 (spermatid ring canals). PMID:8666669 full
  text read via PMC2120840 (PubMed MCP) but the cached copy is abstract-only, so quotes come
  from the abstract.
- Abstract-only: 28554770, 12360288, 12511959, 14724125, 18207738, 19592131, 20519583,
  22133918, 31364377, 31371377, 34107250, 18836316 and the reviews.

### Key judgments

- Core: membrane-actin linker (actin binding + PI(4,5)P2 binding) at the apical/cortical
  plasma membrane; FERM-mediated microtubule binding/anchoring at the cortex; adaptor
  recruiting Conu (RhoGAP) to cortex to restrain Rho1.
- `GO:0045807 positive regulation of endocytosis` (IMP, PMID:25065756): REMOVE; the paper's
  own data place endocytosis upstream of p-Moe [PMID:25065756 "Taken together, these data
  suggest that p-Moe is critically regulated by endocytosis"].
- `GO:0016057 regulation of membrane potential in photoreceptor cell` (IDA, PMID:16216927):
  over-annotation; no membrane-potential measurement in the paper.
- `GO:1990023 mitotic spindle midzone` (IDA, PMID:18283112): visible text describes
  cortical/equatorial p-moesin, not spindle midzone; UNDECIDED (figure detail truncated).
- `GO:0031514 motile cilium` (IEA from UniProt SubCell "flagellum"): source paper
  PMID:20237161 places P-moesin at ring canals at the growing end of flagellar axonemes, not
  in the cilium.
- `GO:0007368 determination of left/right symmetry` (IMP, PMID:18836316): abstract about
  Myo31DF/Myo61F only; full text unavailable -> UNDECIDED.
- Endosome-related IBAs (GO:1902966, GO:2000643) reflect mammalian ERM data; no fly evidence.
- Protein binding IPI rows: Conu rows MODIFY to protein-membrane adaptor activity (paper shows
  recruitment to cortex); PCID2, Mer, Arm rows REMOVE (uninformative; Mer/Arm are
  colocalization only in 8666669).
- No NEW process terms proposed (strict NEW bar).
