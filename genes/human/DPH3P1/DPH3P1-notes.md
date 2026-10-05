# DPH3P1 notes (Q9H4G8, "Putative DPH3 homolog B")

## 2026-10-04: Tier 3 audit (MICROPROTEINS project, pseudogene / uncertain products)

### Does the product exist?
- UniProt Q9H4G8 is PE 5 (Uncertain), with "CAUTION: Could be the product of a pseudogene". The sequence
  comes only from genomic DNA (AL035669, NOT_ANNOTATED_CDS), from the chromosome 20 genome sequencing
  project (UniProt RN [1]). There is no cDNA, CCDS, RefSeq protein or Ensembl translation.
- HGNC:16136 (REST, 2026-10-04): locus_type **pseudogene**, "diphthamide biosynthesis 3
  pseudogene 1". Previous symbols C20orf143, ZCSL1, DPH3B. No MANE transcript.
- Ensembl ENSG00000233838: biotype processed_pseudogene, 20q13.33, a single 249-nt exon. The
  transcript ENST00000486648 has no translation.
- GTEx v8 returns no expression rows for the gene, while parent DPH3 is expressed in all 54
  tissues ([file:human/DPH3P1/DPH3P1-bioinformatics/RESULTS.md]).
- PubMed: 0 hits for DPH3P1, DPH3B or ZCSL1 (esearch, 2026-10-04). No literature exists on the locus.
- Proteomics: UniProt lists a PeptideAtlas cross-reference, but my automated query to check
  for DPH3P1-unique peptides failed. Not established either way.

### Is the annotation inherited correctly?
- The parent is DPH3 (Q96FX2; yeast KTI11/Dph3). DPH3 is a CSL-type zinc finger protein that
  binds iron and acts as the electron donor that reduces the Dph1-Dph2 Fe-S cluster in the first
  step of diphthamide biosynthesis: "yeast Dph3 (also known as KTI11), a CSL-type zinc finger
  protein, can bind iron and in the reduced state can serve as an electron donor to reduce the
  Fe-S cluster in Dph1-Dph2" [PMID:24422557]. The metal ligands are four cysteines: "the
  Cys25, Cys27, Cys47, and Cys50 are responsible for metal coordination" [PMID:24422557].
  Dph3 can also donate an iron atom to convert the [3Fe-4S] cluster to [4Fe-4S] [PMID:34154323].
- Alignment (bioinformatics folder): 70/82 identical, with the frame intact on the genome
  (78 aa, matching UniProt). All four DPH3 metal-ligand cysteines (C26, C28, C48, C51) are
  retained, and the C-terminal LVKC is missing. The sequence therefore shows **no residue-level
  loss**. It sits inside the DPH3 clade and would probably bind metal if it were made.
- PANTHER: the entry is assigned to its own subfamily PTHR21454:SF23 "DPH3 HOMOLOG B-RELATED",
  while human DPH3 is in SF31. The IBA rows come from PTN000485452, the DPH3 ortholog node
  (with/from includes yeast S000007587 Kti11 and mouse MGI:1922658 Dph3). The node placement is
  sound for real DPH3 orthologs. DPH3P1 inherits from it only because a recent processed
  retrocopy of DPH3 sits in the tree as a leaf.

### Action logic
- The problem is not phylogenetic placement or residue loss. The problem is that the leaf is a
  pseudogene with no evidence of transcription into mRNA or of translation. Following the Tier 3
  rule ("REMOVE where the product is unlikely to exist"), all five rows (3 IBA, 2 IEA
  InterPro) are REMOVE.
- Propagation routes: PAINT IBA from PTN000485452 (iron ion binding, cytosol, diphthamide
  modification), and InterPro2GO from IPR044248 (DPH3/4-like; diphthamide BP and metal ion
  binding).
- Upstream fix: exclude PE5 or pseudogene-flagged leaves from IBA propagation, or have PANTHER
  mark SF23 as a pseudogene leaf. The same applies to the InterPro2GO pipeline for PE5 entries
  carrying a "product of a pseudogene" caution.

### Note
- GOA has no tRNA wobble uridine modification row for DPH3P1. Yeast Dph3/Kti11 does work in
  Elongator-dependent wobble uridine modification [PMID:27694803], but GOA only gives DPH3P1
  the diphthamide term, so there was nothing to review for that process.
