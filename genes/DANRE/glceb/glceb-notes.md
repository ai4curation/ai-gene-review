# Notes for DANRE glceb

## 2026-05-09 review notes

- Core function is Golgi membrane D-glucuronyl C5 epimerase activity in heparan sulfate biosynthesis [file:DANRE/glceb/glceb-uniprot.txt "Converts D-glucuronic acid residues adjacent to N-sulfate"].
- Heparin biosynthesis is kept as non-core because UniProt lists it as a pathway, but the central review emphasis is heparan sulfate chain epimerization [file:DANRE/glceb/glceb-uniprot.txt "PATHWAY: Glycan metabolism; heparin biosynthesis."].
- Identical protein binding reflects homodimerization, not the core catalytic function [PMID:25568314 "zebrafish Glce has a dimeric structure"].

## Re-review 2026-09-29

Starting state: valid with no warnings, but every review block was templated (one-line reasons
repeated verbatim across rows, the UniProt FUNCTION line pasted under localization terms).

- Cached the zebrafish developmental paper that UniProt cites as ECO:0000269 but that was
  absent from the review: Ghiselli & Farber 2005 [PMID:16156897 "Overexpression of glce-B
  produced an identical spectrum of phenotypes as the overexpression of glce-A."; "glce-A,
  glce-B and ext2-A transcripts were present in fertilized embryos at developmental stages
  prior to the onset of zygotic transcription, indicating that these messages are maternally
  derived."]. It confirms that glce-B is the gene reviewed here and supplies the BMP/DV
  context for the description. No NEW annotation was proposed from it: ventralization on
  overexpression is a signalling consequence of altered HS fine structure, not work the
  epimerase performs in axis formation.
- Rebuilt the catalytic rows on the structure paper rather than on UniProt paraphrase
  [PMID:25568314 "Based on the structural and mutagenesis studies, three tyrosine residues,
  Tyr 468 , Tyr 528 , and Tyr 546 , in the active site were found to be crucial for the
  enzymatic activity."; "A heparan sulfate chain is synthesized in vivo by several steps:
  tetrasaccharide linkage formation, chain elongation, N -deacetylation/ N -sulfation,
  epimerization, and O -sulfation"]. The pathway-step quote is now what supports the two
  GO:0015012 rows, replacing the FUNCTION line.
- GO:0005794 Golgi apparatus (IBA): ACCEPT -> KEEP_AS_NON_CORE. It is the parent of the
  GO:0000139 Golgi membrane rows already annotated from UniProt, and glceb is a single-pass
  type II membrane protein, so the child is the informative statement.
- GO:0042802 identical protein binding (IPI): kept KEEP_AS_NON_CORE, now argued from the
  structure rather than asserted [PMID:25568314 "A Glce dimer contains two catalytic sites,
  each at a positively charged cleft in C-terminal α-helical domains binding one negatively
  charged hexasaccharide."]. The dimer is the functional unit, but the activity is already
  recorded as GO:0047464.
- GO:0030210 heparin proteoglycan biosynthetic process kept non-core with a real argument
  (same chemistry, but a mast-cell-restricted output with no zebrafish evidence).
- GO:0047464 IBA: the zebrafish gene appearing in its own WITH/FROM is noted as the expected
  marker of experimental grounding on the target, not circularity.
- Added reference_review to both PMIDs, rewrote the description (now mechanism- and
  structure-first, with the paralog and maternal-transcript facts), rewrote the core function
  description, and added a question about glceb/glcea division of labour plus a localization
  experiment (the Golgi assignment is ISS from rat, never imaged in zebrafish).

Validation after edits: zero errors, zero warnings.
