# AmiC1 (alr0092) — Nostoc/Anabaena sp. PCC 7120 — Gene review notes

UniProt: A0ACD7S1M0 (unreviewed, TrEMBL), 627 aa. Locus: alr0092 (ordered locus name).
Taxon: NCBITaxon:103690 (Nostoc sp. strain PCC 7120 / SAG 25.82 / UTEX 2576, "Anabaena").
Adjacent paralog: AmiC2 (alr0093, UniProt A0ACD7S2F2), the immediate downstream gene.

## Summary
AmiC1 is a secreted cell-wall N-acetylmuramoyl-L-alanine amidase (murein hydrolase) of the
filamentous, heterocyst-forming cyanobacterium Anabaena sp. PCC 7120. It cleaves the amide
bond joining the stem peptide (N-terminal L-Ala) to the N-acetylmuramic acid (MurNAc) of the
peptidoglycan glycan backbone. Rather than acting simply in daughter-cell separation as in
unicellular bacteria, AmiC1 (with its paralog AmiC2) remodels/perforates the septal
peptidoglycan to generate the array of nanopores through which septal junctions connect the
cytoplasms of adjacent cells in the filament. This intercellular conduit is required for
cell-cell communication (metabolite/signal exchange), for heterocyst development, and for
diazotrophic (N2-fixing) growth.

## Protein family / domain architecture
- N-terminal signal/export sequence (the mature protein acts in the periplasm/cell-wall
  compartment; the sequence begins MKLHWLLSGTVGTVLLLSSPALA..., a signal-anchor-like stretch).
- AMIN domain (IPR021731 / Pfam PF11741): septal/PG-targeting module that directs the enzyme
  to the division septum.
- N-acetylmuramoyl-L-alanine amidase catalytic domain, "Amidase_3" (IPR002508 / Pfam PF01520;
  cd02696 MurNAc-LAA). Zn-dependent amidase fold (Zn-dependent exopeptidase-like,
  SSF53187). The conserved catalytic motif ...FIDPGHGG... (near residue 430 of AmiC1) is the
  signature of this amidase family.
- PANTHER family PTHR30404 "N-acetylmuramoyl-L-alanine amidase 3".
- The GOA molecular-function IEA (GO:0008745) derives from InterPro IPR002508 and PANTHER,
  consistent with this architecture.

## Functional evidence (experimental)
- AmiC1 is a cell-wall-lytic amidase / autolysin: overexpression of amiC1 from a copper-
  inducible promoter caused cell lysis. [PMID:22821973 "cell lysis could be observed as a
  result of the autolysin activity of AmiC1"]
- Amidase biochemistry (family context): [PMID:22821973 "Murein hydrolases degrade
  specifically the bacterial murein sacculus by cleaving defined bonds in the peptidoglycan."]
- Loss-of-function phenotype: an amiC1 (alr0092) mutant fails to make heterocysts and cannot
  grow diazotrophically, and loses intercellular communication. [PMID:22821973 "The amiC1
  (alr0092) mutant was not able to differentiate heterocysts or to grow diazotrophically"];
  FRAP: [PMID:22821973 "fluorescence recovery after photobleaching (FRAP) studies showed a
  lack of cell-cell communication only in the AmiC1 mutant."]; and reiterated in
  [PMID:28929086 "A mutant of amiC1 (alr0092) was unable to form heterocysts and lost
  intercellular communication"].
- Complementation: [PMID:22821973 "Green fluorescent protein (GFP)-tagged AmiC1 was able to
  complement the mutant phenotype to wild-type properties."]
- Subcellular localization (GFP fusions): AmiC1 concentrates at the division septum of newly
  dividing cells and at the polar neck of differentiating heterocysts. [PMID:22821973 "The
  protein localized in the septal regions of newly dividing cells and at the neck region of
  differentiating heterocysts."]; [PMID:22821973 "the amidase AmiC1 is present mainly in the
  septum of freshly dividing cells"]; [PMID:28929086 "both amidases, AmiC1 and AmiC2,
  localized to the septa of young vegetative cells and to the septal and polar neck areas
  connecting heterocysts with vegetative cells"].
- Septal nanopore array: inactivation of amiC1 reduces the septal PG nanopore count.
  [PMID:28929086 "the amiC1 mutants SR477 and FQ1633 showed 47 and 52% of the count of
  nanopores, respectively"] (i.e. roughly half of wild-type), accompanied by reduced
  intercellular tracer (calcein / 5-CF) exchange by FRAP.
- Interpretive model: [PMID:22821973 "We suggest that AmiC1 processes the newly synthesized
  septum to allow the formation of structures for cell-cell communication."]

## Relationship to AmiC2 (do not conflate)
- amiC1 and amiC2 are adjacent paralogs; both encode septum-localized AmiC-type amidases and
  are partially redundant, as one of the two is required for normal growth/cell division
  (double knockouts could not be fully segregated). [PMID:28929086]
- AmiC1 is the dominant/more-important amidase in Anabaena: amiC1 inactivation gives the
  stronger phenotype (Fox-, Het-, loss of communication), whereas an amiC2 single mutant is
  phenotypically near-normal under standard conditions; amiC1 can compensate loss of amiC2 but
  not vice versa. [PMID:22821973; PMID:28929086 "Nonetheless, AmiC1 seems to be the more
  important amidase..."]
- AmiC1-specific (not shared with AmiC2): only amiC1 inactivation delocalizes SepJ-GFP and
  suppresses the fragmentation phenotype of sepJ / fraC fraD mutants. [PMID:28929086 "These
  results indicate that AmiC1 but not AmiC2 appears to be needed for proper subcellular
  localization of SepJ at the center of intercellular septa."]
- In the more-characterized N. punctiforme system, AmiC2 (Npun_F1846) is the nanopore driller
  whose amiC1 ortholog could not be inactivated; in Anabaena both paralogs were inactivated,
  and AmiC1 turns out to carry the dominant role. Care: many mechanistic "nanopore driller"
  statements in the literature are grounded on AmiC2 (N. punctiforme); the AmiC1-specific
  Anabaena data are in Berendt 2012 (PMID:22821973) and Bornikoel 2017 (PMID:28929086).

## Annotation decisions (GOA review)
1. GO:0008745 N-acetylmuramoyl-L-alanine amidase activity (IEA, enables) — ACCEPT (core MF).
   Supported by domain architecture (IPR002508/PF01520) and direct autolysin evidence.
2. GO:0009253 peptidoglycan catabolic process (IEA, involved_in) — ACCEPT (core BP). The
   enzyme cleaves/degrades peptidoglycan.
3. GO:0030288 outer membrane-bounded periplasmic space (IEA, located_in) — MODIFY to
   GO:0030428 cell septum. Anabaena is Gram-negative and the mature amidase acts in the
   periplasmic/cell-wall compartment (so the periplasm call is not wrong), but the
   experimentally documented, functionally relevant location is the division septum / polar
   neck; cell septum is the more informative CC. Periplasmic space (GO:0042597) retained as a
   core-function location alongside cell septum.

New (not in GOA) functions supported by experiment and added as NEW existing_annotations /
core_functions:
- GO:0071555 cell wall organization (septal PG remodeling / nanopore array formation).
- GO:0007267 cell-cell signaling (drilling the septal nanopores that carry septal junctions
  mediating intercellular communication; amiC1 mutant loses FRAP tracer exchange).
- GO:0030428 cell septum (septal localization).

## References
- PMID:22821973 — Berendt et al. 2012, J Bacteriol. "Cell wall amidase AmiC1 is required for
  cellular communication and heterocyst development in the cyanobacterium Anabaena PCC 7120
  but not for filament integrity." PRIMARY, AmiC1-specific.
- PMID:28929086 — Bornikoel et al. 2017, Front Cell Infect Microbiol. "Role of Two Cell Wall
  Amidases in Septal Junction and Nanopore Formation in the Multicellular Cyanobacterium
  Anabaena sp. PCC 7120." PRIMARY; compares AmiC1 and AmiC2 in Anabaena.
- Module grounding: modules/septal_junction.yaml (AmiC1 = amiC1_annoton; septal PG nanopore
  formation prerequisite for septal junctions).
