# sptl-1 review notes

## 2026-10-28 initial review
- Fetched P91079 (SPTC1_CAEEL); 8 GOA rows. Cached PMID:21926990, 15340492, 23705068, 38704027, 31138658, 41191545.
- No deep-research provider available; manual research in sptl-1-deep-research-manual.md.
- Bioinformatics (sptl-1-bioinformatics/): SPTL-1 aligns best with SPTLC1 and carries Asn297 at the SPTLC2
  PLP-lysine position -> PLP binding IEA marked over-annotated (as for human SPTLC1).
- SPT activity IBA/IEA accepted (subunit of heterodimer; GO convention for LCB1 subunits).
- ER IBA accepted after checking PAINT seeds (human, mouse, yeast, Arabidopsis, trypanosomatid LCB1 with
  experimental ER data). Did NOT add ER membrane NEW: only homology supports it; UniProt has no TM feature,
  though residues ~8-25 (WHFYIETLLVALLAYVVM) are hydrophobic by inspection.
- sphingolipid metabolic process IEA -> MODIFY to GO:0030148 sphingolipid biosynthetic process.
- Polarity IMP (PMID:21926990, full text read) -> KEEP_AS_NON_CORE: real requirement, but it is the glycosphingolipid
  products that act; the enzyme is upstream.
- No NEW process terms proposed (strict bar: mutant phenotypes such as larval development, lysosome integrity,
  neuronal polarity are downstream consequences of lipid loss).
- Curation gap: no complex (GO:0017059) annotation for the worm; raised as a suggested question only.
