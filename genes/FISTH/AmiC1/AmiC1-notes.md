# AmiC1 (FJSC11DRAFT_3094 / G6FW03) — Fischerella thermalis JSC-11 — Gene review notes

UniProt: G6FW03 (G6FW03_9CYAN, unreviewed, TrEMBL), 629 aa.
Locus: FJSC11DRAFT_3094 (ORF name; EMBL EHC11642.1; RefSeq WP_009458035.1).
Taxon: NCBITaxon:741277 (Fischerella thermalis JSC-11); Nostocales, Hapalosiphonaceae,
Stigonematales (true-branching cyanobacteria).
Function line (UniProt): "N-acetylmuramoyl-L-alanine amidase", EC 3.5.1.28.
Adjacent tandem paralog: AmiC2 = FJSC11DRAFT_3096 (UniProt G6FW05).

## Summary (orthology-based)
G6FW03 (FJSC11DRAFT_3094) is the AmiC1 ortholog of Fischerella thermalis. By protein family it
is a secreted cell-wall N-acetylmuramoyl-L-alanine amidase (murein hydrolase / autolysin, EC
3.5.1.28) that cleaves the amide bond joining the stem peptide (N-terminal L-Ala) to the
N-acetylmuramic acid (MurNAc) of peptidoglycan. In the filamentous, heterocyst-forming
cyanobacteria the AmiC amidases remodel/perforate the septal peptidoglycan to generate the
array of nanopores through which septal junctions connect the cytoplasms of adjacent cells,
supporting intercellular communication, heterocyst differentiation, and diazotrophic growth.
This gene itself (G6FW03) has not been directly assayed; its functional attributes are
transferred by orthology (ISS) from the characterized Anabaena (Nostoc sp. PCC 7120) AmiC1.

## Domain architecture (from UniProt G6FW03)
- Signal peptide (SignalP, residues 1..24) — secreted / periplasmic.
- AMIN domain (IPR021731 / Pfam PF11741; two copies per UniProt): septal / PG-targeting module.
- N-acetylmuramoyl-L-alanine amidase "Amidase_3" catalytic domain (IPR002508 MurNAc-LAA_cat /
  Pfam PF01520; CDD cd02696 MurNAc-LAA; SMART SM00646 Ami_3), a Zn-dependent amidase fold
  (SUPFAM SSF53187 Zn-dependent exopeptidases; Gene3D 3.40.630.40).
- InterPro family IPR050695 (N-acetylmuramoyl_amidase_3); PANTHER PTHR30404 subfamily SF0
  "N-ACETYLMURAMOYL-L-ALANINE AMIDASE AMIC".
- The conserved catalytic motif ...IDPGHGG... is present (sequence ...GKVVVLIDPGHGGRDSGAVG...),
  the signature of this amidase family.
- The GOA molecular-function IEA (GO:0008745) derives from InterPro IPR002508 / EC 3.5.1.28 /
  PANTHER, consistent with this architecture.

## Orthology evidence (reciprocal best hit)
- Reciprocal-best-hit (RBH) analysis against the Anabaena / Nostoc sp. PCC 7120 genome (taxon
  103690) resolves the tandem amidase paralogs: G6FW03 (FJSC11DRAFT_3094) is the reciprocal
  best hit of 7120 AmiC1 (A0ACD7S1M0, alr0092) [forward E = 5.1e-241, reciprocal], and G6FW05
  (FJSC11DRAFT_3096) is the AmiC2 ortholog. G6FW03 is therefore the AmiC1 ortholog and G6FW05
  the AmiC2 ortholog, a tandem pair mirroring the 7120 alr0092/alr0093 arrangement.
  [file:modules/septal_junction/RESULTS.md]
- Because paralog assignment for these broadly-conserved amidase domains cannot be made from a
  single forward best hit alone, RBH was used specifically to disambiguate AmiC1 from AmiC2;
  the assignment is reciprocal in both directions.

## Stigonematales retains the tandem AmiC1/AmiC2 pair (ancestral duplication)
- The AmiC1/AmiC2 duplication is NOT Nostoc/Anabaena-specific. Fischerella thermalis, a
  deep-branching Stigonematales (true-branching) cyanobacterium, retains BOTH an AmiC2 ortholog
  (G6FW05 / FJSC11DRAFT_3096) and this AmiC1 ortholog (G6FW03 / FJSC11DRAFT_3094).
- Presence of the tandem pair in both Nostoc/Anabaena and the deep-branching Fischerella makes
  an ancestral duplication (with lineage-specific AmiC1 loss in, e.g., Cylindrospermum stagnale
  and Chlorogloeopsis fritschii, which retain only the single AmiC2 ortholog) the more
  parsimonious reading than independent duplications. [file:modules/septal_junction/RESULTS.md]

## Basis for ISS transfer from Anabaena (Nostoc sp. PCC 7120) AmiC1
The characterized reference protein is Anabaena AmiC1 (alr0092, A0ACD7S1M0). Its documented
functions are transferred to this F. thermalis ortholog with ISS evidence:
- Autolysin / amidase activity: [PMID:22821973 "cell lysis could be observed as a result of
  the autolysin activity of AmiC1"]; family biochemistry [PMID:22821973 "Murein hydrolases
  degrade specifically the bacterial murein sacculus by cleaving defined bonds in the
  peptidoglycan."].
- Septal localization: [PMID:22821973 "The protein localized in the septal regions of newly
  dividing cells and at the neck region of differentiating heterocysts."]; [PMID:22821973 "the
  amidase AmiC1 is present mainly in the septum of freshly dividing cells"]; [PMID:28929086
  "both amidases, AmiC1 and AmiC2, localized to the septa of young vegetative cells and to the
  septal and polar neck areas connecting heterocysts with vegetative cells"].
- Septal PG remodeling / nanopore array: [PMID:28929086 "the amiC1 mutants SR477 and FQ1633
  showed 47 and 52% of the count of nanopores, respectively"].
- Cell-cell communication / heterocyst development: [PMID:22821973 "The amiC1 (alr0092) mutant
  was not able to differentiate heterocysts or to grow diazotrophically"]; [PMID:22821973 "We
  suggest that AmiC1 processes the newly synthesized septum to allow the formation of
  structures for cell-cell communication."]; [PMID:28929086 "A mutant of amiC1 (alr0092) was
  unable to form heterocysts and lost intercellular communication"].

## IMPORTANT: distinguish this gene (AmiC1/FJSC11DRAFT_3094) from AmiC2/FJSC11DRAFT_3096
- The direct experimental characterization of the AmiC amidases is in Anabaena (Nostoc sp. PCC
  7120); in the wider Nostoc punctiforme literature the direct amidase work is on AmiC2, not on
  AmiC1. Do NOT attribute AmiC2-specific structural / nanopore / morphogenesis assays to this
  AmiC1 gene, and do NOT confuse FJSC11DRAFT_3094 (AmiC1, this gene) with FJSC11DRAFT_3096
  (AmiC2, the tandem paralog).
- The AmiC1-specific functional data used here come from Anabaena (Nostoc sp. PCC 7120) AmiC1
  (Berendt 2012 PMID:22821973; Bornikoel 2017 PMID:28929086), transferred to this F. thermalis
  ortholog by orthology (ISS). No direct assay on G6FW03 is claimed.

## Annotation decisions (GOA review)
GOA seeds three IEA annotations for G6FW03:
1. GO:0008745 N-acetylmuramoyl-L-alanine amidase activity (IEA, enables) — ACCEPT (core MF).
   Grounded on EC 3.5.1.28 + Amidase_3 catalytic domain (IPR002508/PF01520).
2. GO:0009253 peptidoglycan catabolic process (IEA, involved_in) — ACCEPT (core BP). The
   amidase cleaves/degrades peptidoglycan.
3. GO:0030288 outer membrane-bounded periplasmic space (IEA, located_in) — ACCEPT. F. thermalis
   is a Gram-negative cyanobacterium with an outer membrane; the mature cell-wall amidase (with
   a SignalP signal peptide) acts in the periplasmic / cell-wall compartment. Retained as a
   core-function location, with the more informative septal sublocation (cell septum) added by
   orthology.

NEW annotations transferred by orthology (ISS) from 7120 AmiC1:
- GO:0030428 cell septum (septal localization of the AmiC1 ortholog).
- GO:0071555 cell wall organization (septal PG remodeling / nanopore array formation).
- GO:0007267 cell-cell signaling (gated intercellular communication via septal nanopores /
  septal junctions).

## References
- PMID:22821973 — Berendt et al. 2012, J Bacteriol. "Cell wall amidase AmiC1 is required for
  cellular communication and heterocyst development in the cyanobacterium Anabaena PCC 7120
  but not for filament integrity." PRIMARY, AmiC1-specific (in Anabaena PCC 7120).
- PMID:28929086 — Bornikoel et al. 2017, Front Cell Infect Microbiol. "Role of Two Cell Wall
  Amidases in Septal Junction and Nanopore Formation in the Multicellular Cyanobacterium
  Anabaena sp. PCC 7120." PRIMARY; compares AmiC1 and AmiC2 in Anabaena.
- file:modules/septal_junction/RESULTS.md — RBH orthology assignment (G6FW03 = AmiC1 ortholog;
  Stigonematales retains the tandem AmiC1/AmiC2 pair).
