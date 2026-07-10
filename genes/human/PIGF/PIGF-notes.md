# PIGF (Q07326) review notes

Deep research: falcon was OUT OF CREDITS (HTTP 402); no `-deep-research-falcon.md` generated.
Review grounded in `PIGF-uniprot.txt`, the seeded `PIGF-goa.tsv`, and cached `publications/PMID_*.md`.

## Core biology (verified)
- PIGF is a **non-catalytic accessory (stabilizing) subunit** of the GPI ethanolamine-phosphate
  transferases PIGO and PIGG. It is NOT an independent enzyme.
  - [PMID:15632136 "hGPI7 was associated with and stabilized by PIG-F, which is known to bind to and stabilize PIG-O, a protein homologous to hGPI7"]
  - [PMID:32156170 "Both PIGO and PIGG are stabilized by association with PIGF"]
  - [PMID:32156170 "Two EtNPs are sequentially transferred to the 6-positions of Man3 and then Man2 by PIGO"] (PIGO adds EtNP to Man3, PIGG to Man2; PIGF is the shared stabilizer)
  - UniProt: "Stabilizing subunit of the ethanolamine phosphate transferase 3 and ethanolamine phosphate transferase 2 complexes"; "PIGF is required to stabilize PIGG and PIGO".
- Core BP: **GPI anchor biosynthetic process (GO:0006506)**.
- Location: **ER membrane (GO:0005789)**; multi-pass membrane protein (6 TM helices in UniProt features).
- Disease: homozygous p.Pro172Arg causes an inherited GPI-deficiency disorder (OORS / DOORS-overlap).
  - [PMID:33386993 "We demonstrate impaired glycosylphosphatidylinositol (GPI) biosynthesis through flow cytometry analysis"]

## GOA molecular function
- The seeded GOA TSV carries **NO catalytic MF term** for PIGF. The only MF line is
  `GO:0005515 protein binding` (IPI, PMID:32296183 HuRI Y2H). Per instructions I did NOT invent a
  catalytic activity. NOTE: the UniProt DR block lists `GO:0051377 mannose-ethanolamine
  phosphotransferase activity; IBA:GO_Central`, but that term is NOT in the GOA TSV, so it was
  intentionally not added as a core_function `function`.
- core_functions therefore omits `function` and records BP under `directly_involved_in`
  (GO:0006506) + location (GO:0005789).

## protein binding IPI (PMID:32296183)
- 8 IPI lines to AQP6, GPR152, LYVE1, MANBAL, TIMMDC1, TMEM130, TMEM14B, TMEM86B — all HuRI
  high-throughput Y2H hits to unrelated membrane proteins, none of them PIGO/PIGG.
- Action: MARK_AS_OVER_ANNOTATED (bare uninformative `protein binding`; not REMOVE per policy).

## PANTHER family id
- **No PTHR##### family id** is present in the UniProt cross-references. The GOA WITH/FROM only
  shows a PANTHER *node* id `PANTHER:PTN009167560` (from the IBA), and UniProt has a `PAN-GO` line
  but no `PANTHER; PTHR#####` DR line.

## Other identifiers
- InterPro IPR009580 (GPI_biosynthesis_protein_Pig-F); Pfam PF06699 (PIG-F). eggNOG KOG3144.
- Isoforms: Q07326-1 (canonical), Q07326-2 (VSP_004361).
