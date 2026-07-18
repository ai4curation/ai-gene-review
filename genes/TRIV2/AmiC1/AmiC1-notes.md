# AmiC1 (Ava_1465 / Q3MD48) — Anabaena variabilis ATCC 29413 (Trichormus variabilis, TRIV2) — Gene review notes

UniProt: Q3MD48 (Q3MD48_TRIV2, unreviewed, TrEMBL), 627 aa.
Locus: Ava_1465 (ordered locus name; EMBL ABA21088.1; RefSeq WP_011318288.1).
Taxon: NCBITaxon:240292 (Trichormus variabilis / Anabaena variabilis strain ATCC 29413 / PCC 7937).
Function line (UniProt): "Cell wall hydrolase/autolysin", EC 3.5.1.28.
Adjacent tandem paralog: AmiC2 = Q3MD47 (Ava_1464), the immediately adjacent gene in the tandem amidase pair.

## Summary (orthology-based)
Q3MD48 (Ava_1465) is the AmiC1 ortholog of Anabaena variabilis ATCC 29413. By protein family it
is a secreted cell-wall N-acetylmuramoyl-L-alanine amidase (murein hydrolase / autolysin, EC
3.5.1.28) that cleaves the amide bond joining the stem peptide (N-terminal L-Ala) to the
N-acetylmuramic acid (MurNAc) of peptidoglycan. In the filamentous, heterocyst-forming
cyanobacteria the AmiC amidases remodel/perforate the septal peptidoglycan to generate the array
of nanopores through which septal junctions connect the cytoplasms of adjacent cells, supporting
intercellular communication, heterocyst differentiation, and diazotrophic growth. This gene
itself (Q3MD48) has not been directly assayed; its functional attributes are transferred by
orthology (ISS) from the characterized Anabaena (Nostoc sp. PCC 7120) AmiC1 (alr0092).

## Domain architecture (from UniProt Q3MD48)
- N-terminal signal peptide (SignalP, residues 1–23) → secreted / periplasmic cell-wall protein.
- AMIN domain (IPR021731 / Pfam PF11741; two copies per UniProt): septal/PG-targeting module.
- N-acetylmuramoyl-L-alanine amidase "Amidase_3" catalytic domain (IPR002508 MurNAc-LAA_cat /
  Pfam PF01520; CDD cd02696 MurNAc-LAA; SMART SM00646 Ami_3; UniProt DOMAIN 513–622), a
  Zn-dependent amidase fold (SUPFAM SSF53187 Zn-dependent exopeptidases; Gene3D 3.40.630.40).
- InterPro family IPR050695 (N-acetylmuramoyl_amidase_3); PANTHER PTHR30404 subfamily SF0
  "N-ACETYLMURAMOYL-L-ALANINE AMIDASE AMIC".
- The conserved catalytic motif ...IDPGHGG... is present (sequence ...RLVVLIDPGHGGKDPG...
  around residue 470), the signature of this Zn-dependent amidase family.
- The GOA molecular-function IEA (GO:0008745) derives from InterPro IPR002508 / EC 3.5.1.28 /
  PANTHER, consistent with this architecture.

## Orthology evidence (reciprocal best hit)
- Reciprocal-best-hit (RBH) analysis against the Anabaena/Nostoc sp. PCC 7120 genome (taxon
  103690) assigns the tandem amidase paralogs cleanly for Anabaena variabilis (TRIV2, taxon
  240292): AmiC1 = Q3MD48 and AmiC2 = Q3MD47, mirroring the 7120 alr0092/alr0093 arrangement.
  The AmiC1 forward hit to 7120 AmiC1 (A0ACD7S1M0, alr0092) is reciprocal (forward E = 0).
  [file:modules/septal_junction/RESULTS.md: "the tandem amidases AmiC2 Q3MD47 / AmiC1 Q3MD48"]
- Because paralog assignment for these broadly-conserved amidase domains cannot be made from a
  single forward best hit alone, RBH was used specifically to disambiguate AmiC1 from AmiC2;
  the assignment is reciprocal in both directions.

## Basis for ISS transfer from Anabaena (Nostoc sp. PCC 7120) AmiC1
The characterized reference protein is Anabaena AmiC1 (alr0092, A0ACD7S1M0). Its documented
functions are transferred to this A. variabilis ortholog with ISS evidence:
- Autolysin / amidase activity: [PMID:22821973 "cell lysis could be observed as a result of the
  autolysin activity of AmiC1"]; family biochemistry [PMID:22821973 "Murein hydrolases degrade
  specifically the bacterial murein sacculus by cleaving defined bonds in the peptidoglycan."].
- Septal localization: [PMID:22821973 "the amidase AmiC1 is present mainly in the septum of
  freshly dividing cells"]; [PMID:28929086 "both amidases, AmiC1 and AmiC2, localized to the
  septa of young vegetative cells and to the septal and polar neck areas connecting heterocysts
  with vegetative cells"].
- Septal PG remodeling / nanopore array: [PMID:28929086 "the amiC1 mutants SR477 and FQ1633
  showed 47 and 52% of the count of nanopores, respectively"].
- Cell-cell communication / heterocyst development: [PMID:22821973 "The amiC1 (alr0092) mutant
  was not able to differentiate heterocysts or to grow diazotrophically"]; [PMID:22821973 "We
  suggest that AmiC1 processes the newly synthesized septum to allow the formation of structures
  for cell-cell communication."]; [PMID:28929086 "A mutant of amiC1 (alr0092) was unable to form
  heterocysts and lost intercellular communication"].

## IMPORTANT: distinguish this gene (AmiC1 / Q3MD48) from AmiC2 (Q3MD47)
- The direct experimental characterization of an AmiC amidase in Nostoc punctiforme is of AmiC2
  (Npun_F1846), NOT of an AmiC1. Do NOT attribute the N. punctiforme AmiC2 structural / nanopore
  / morphogenesis assays to this AmiC1 gene.
- The AmiC1-specific functional data used here come from Anabaena (Nostoc sp. PCC 7120) AmiC1
  (Berendt 2012 PMID:22821973; Bornikoel 2017 PMID:28929086), transferred to this A. variabilis
  ortholog by orthology (ISS). No direct assay on Q3MD48 is claimed.
- Q3MD48 (AmiC1) must be kept distinct from its adjacent tandem paralog Q3MD47 (AmiC2).

## Annotation decisions (GOA review)
GOA seeds three IEA annotations for Q3MD48:
1. GO:0008745 N-acetylmuramoyl-L-alanine amidase activity (IEA, enables; GO_REF:0000120) —
   ACCEPT (core MF). Grounded on EC 3.5.1.28 + Amidase_3 catalytic domain (IPR002508/PF01520).
2. GO:0009253 peptidoglycan catabolic process (IEA, involved_in; GO_REF:0000002) — ACCEPT (core
   BP). The amidase cleaves/degrades peptidoglycan.
3. GO:0030288 outer membrane-bounded periplasmic space (IEA, located_in; GO_REF:0000118) —
   ACCEPT. A. variabilis is a Gram-negative cyanobacterium with an outer membrane; the mature,
   signal-peptide-cleaved cell-wall amidase acts in the periplasmic / cell-wall compartment.
   Retained as a core-function location, with the more informative septal sublocation (cell
   septum) added by orthology.

NEW annotations transferred by orthology (ISS) from 7120 AmiC1:
- GO:0030428 cell septum (septal localization of the AmiC1 ortholog).
- GO:0071555 cell wall organization (septal PG remodeling / nanopore array formation).
- GO:0007267 cell-cell signaling (gated intercellular communication via septal nanopores /
  septal junctions).

## References
- PMID:22821973 — Berendt et al. 2012, J Bacteriol. "Cell wall amidase AmiC1 is required for
  cellular communication and heterocyst development in the cyanobacterium Anabaena PCC 7120 but
  not for filament integrity." PRIMARY, AmiC1-specific (in Anabaena PCC 7120); ISS source.
- PMID:28929086 — Bornikoel et al. 2017, Front Cell Infect Microbiol. "Role of Two Cell Wall
  Amidases in Septal Junction and Nanopore Formation in the Multicellular Cyanobacterium
  Anabaena sp. PCC 7120." PRIMARY; compares AmiC1 and AmiC2 in Anabaena; ISS source.
- file:modules/septal_junction/RESULTS.md — RBH orthology assignment (Q3MD48 = AmiC1 ortholog,
  Q3MD47 = AmiC2 ortholog for TRIV2).
