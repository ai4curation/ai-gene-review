# mcrA (MJ0846, Q58256) - Methanocaldococcus jannaschii DSM 2661

Notes for the ARCHAEA project review (round 5). Automated deep-research providers
were unavailable (API key failures), so no `-deep-research-*.md` file exists.
Literature was found with WebSearch and NCBI/PMC id conversion; every PMID below
was cached with `just fetch-pmid` and read. Ortholog reviews used for consistency:
`genes/METTH/mcrA/` (O27232) and `genes/METAC/mcrA/` (Q8THH1).

## Identity and genomic context

- UniProt Q58256 (MCRA_METJA), 553 aa, locus MJ0846, EC 2.8.4.1 (by similarity to
  P11558, M. marburgensis MCR I alpha). Sequence from the genome project
  [PMID:8688087 "Complete genome sequence of the methanogenic archaeon, Methanococcus jannaschii."].
- PE 1 only because of PDB 6PEU, a YcaO (MJ1094) co-crystal with McrA peptide 442-453;
  no structure of the M. jannaschii holoenzyme exists.
- M. jannaschii has **two** MCR operons (UniProt REST query, organism 243232):
  mcr (MJ0842 mcrB, MJ0843 mcrD, MJ0844 mcrC, MJ0845 mcrG, MJ0846 mcrA) and
  mrt (MJ0081 mrtB, MJ0082 mrtG, MJ0083 mrtA; mrtD MJ0118). MJ0841, next to the mcr
  operon, is the [MCR]-arginine C5-methyltransferase (Mmp10 family).
- Many Methanococcales carry two isoenzymes
  [PMID:30951290 "many members of the Methanococcales, and a few members of the Methanomicrobiales contain two MCR isoenzymes"].
- Naming caveat: "MCR I" is a name transferred from M. marburgensis. Phylogenetically,
  Methanococcales MCRs fall into type II or the Methanococcales-only type III
  [PMID:28559298 "(ii) MCRs from Methanobacteriales and Methanococcales, and (iii) MCRs from Methanococcales"].
  The PMC full text of PMID:28559298 (read via WebFetch, not in the cache, which is
  abstract-only) places M. jannaschii MCR in type III. So "isoenzyme I" in this entry
  does not mean orthology to M. marburgensis MCR I specifically; the active sites of all
  types are nonetheless conserved
  [PMID:28559298 "virtually identical active site architectures reflecting the chemically challenging mechanism of methane formation"].

## Organism physiology

- Obligate hydrogenotroph
  [PMID:24505058 "a deeply rooted hyperthermophilic methanogen growing only on H 2 plus CO 2"].
  So the route MCR serves is CO2 reduction (GO:0019386), as for M. thermautotrophicus.
- Unlike Methanothermobacter (where mcr vs mrt switch with H2 supply, METTH notes),
  M. jannaschii chemostat cultures showed no change in either mcrA with H2 supply
  [PMID:30824444 "for any of the methyl-coenzyme M (CoM) reductase A I or II genes (mcrA, MJ_RS00415 and MJ_RS04540)"].
  The physiological division of labour between the two isoenzymes in this organism is unknown.
- Sulfite (from O2-sulfide chemistry at vents) inhibits MCR
  [PMID:24505058 "Sulfite inhibits methyl-coenzyme M reductase and, thereby, impedes methanogenesis"].
- Shotgun proteomics of M. jannaschii (PMID:15253435) is abstract-only in the cache and
  the abstract does not name MCR; not used as support.

## Protein-level evidence in M. jannaschii

- MCR I has been isolated from M. jannaschii and analysed by MS for active-site PTMs;
  all MCRs contain the thioxo peptide bond (thioglycine), methylations differ
  [PMID:17725644 "MCR I from Methanocaldococcus jannaschii and Methanoculleus thermophilus"],
  [PMID:17725644 "MCRs from all methanogens investigated contain the thioxo peptide bond"].
  Abstract only; the specific methylation pattern of the M. jannaschii enzyme is not
  visible in the cache.
- Thioglycine installation: M. jannaschii has no tfuA, and MjYcaO alone thioamidates a
  McrA peptide at Gly448 (numbering matches Q58256 v2: H441-S-R443-L-G445-F-Y-G448)
  [PMID:31139720 "a similar peptide derived from MjMcrA with the natural site of modification at Gly448"],
  [PMID:31139720 "these two hyperthermophiles can catalyze thioamidation on the cognate McrA peptide in a TfuA-independent fashion."].
  The Q58256 entry has no thioglycine MOD_RES at Gly448 (only 5-methylarginine 274 by
  similarity to Q8THH1). Recorded as a MISSING_STATEMENT source defect for UniProt.
- 5-methylarginine (Arg274) by MJ0841: UniProt PTM by similarity to Q8THH1 (M. acetivorans
  MA4551 work, PMID:29743535, see METAC review). No M. jannaschii-specific data found.

## Structure / mechanism (orthologous enzyme)

- Hexamer alpha2beta2gamma2 with two identical F430 active sites
  [PMID:9367957 "two molecules of the nickel porphinoid coenzyme F430 are embedded between the subunits alpha, alpha', beta, and gamma and alpha', alpha, beta', and gamma', forming two identical active sites."].
- UniProt (by similarity to P11558): axial F430 Ni ligand at residue 150 (Gln150 here,
  equivalent to Gln147 in M. marburgensis and Gln161 in M. acetivorans); CoB and CoM
  binding residues; cytoplasm.

## Annotation decisions (summary)

- cytoplasm IEA + ISS: ACCEPT (soluble enzyme; same as METTH/METAC).
- methanogenesis IEA (InterPro2GO): MODIFY to GO:0019386 methanogenesis, from carbon
  dioxide (obligate hydrogenotroph; same reasoning as METTH).
- coenzyme-B sulfoethylthiotransferase activity IEA + ISS: ACCEPT.
- NEW: GO:0044674 methyl coenzyme M reductase complex (ISS from the orthologous
  structure, plus isolation of MCR I from M. jannaschii, PMID:17725644).
- F430: no direct evidence in this organism, so no NEW tetrapyrrole-binding row (METAC
  added one by IDA from its own cryo-EM structure; METTH added none). The coenzyme F430
  binding term proposal is carried over from METAC for consistency.

## Consistency observations across the three mcrA reviews

- METAC carries a NEW GO:0046906 tetrapyrrole binding row and a proposed "coenzyme F430
  binding" term; METTH only asks the F430 question. Not strictly inconsistent (evidence
  differs), but METTH could adopt the proposed term.
- METTH and METAC complex NEW rows use IDA; here ISS, because no M. jannaschii subunit
  composition data are visible.
