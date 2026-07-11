# AmiC2 (alr0093) — Nostoc/Anabaena sp. PCC 7120 — Gene Review Notes

UniProt: A0ACD7S2F2 (unreviewed, TrEMBL), 627 aa. Ordered locus **alr0093**. Taxon
NCBITaxon:103690 (Nostoc/Anabaena sp. PCC 7120). Encoded immediately downstream of its
paralog **amiC1 (alr0092)**.

## Summary

AmiC2 is a secreted **cell-wall N-acetylmuramoyl-L-alanine amidase** (EC 3.5.1.28) that
hydrolyses the bond between N-acetylmuramoyl residues and L-alanine in peptidoglycan (PG).
Unlike the housekeeping AmiC amidases of unicellular bacteria (which split the septum for
daughter-cell separation), the cyanobacterial AmiC2 **drills a regular array of nanopores
into the septal cross-wall (murein)**. These nanopores form the framework through which
**septal junctions (SJs)** thread to directly connect the cytoplasms of adjacent cells in
the filament, enabling intercellular exchange of metabolites and signalling molecules. This
communication is a prerequisite for multicellular behaviour, filament integrity and
heterocyst (N2-fixation cell) differentiation.

The definitive biochemical, structural and cell-biological characterisation of AmiC2 was
performed on the **Nostoc punctiforme ortholog (Npun_F1846)**; the **Anabaena PCC 7120
gene alr0093 (AmiC2)** studied here was characterised genetically (mutant phenotypes,
nanopore counts, FRAP cell–cell communication) by Bornikoel et al. 2017 alongside its
paralog AmiC1 (alr0092).

## Protein family / domain architecture

- **AMIN domain** (InterPro IPR021731, Pfam PF11741) in the N-terminal region — a
  septal/PG-targeting module that directs the enzyme to the division septum.
- **N-acetylmuramoyl-L-alanine amidase catalytic domain, Amidase_3 / MurNAc-LAA**
  (InterPro IPR002508, Pfam PF01520, CDD cd02696) in the C-terminal region — a
  **Zn-dependent amidase** (SCOP/SSF53187, Zn-dependent exopeptidases). PANTHER family
  **PTHR30404 "N-acetylmuramoyl-L-alanine amidase 3"**.
- The 627-aa preprotein begins with a signal-peptide-like hydrophobic N-terminus
  (`MKLHWLLSGTVGTIFLLSSPALAA…`), consistent with export across the cytoplasmic membrane to
  the periplasmic/cell-wall compartment where the septal PG resides.
- The Zn²⁺ ion in the active site is essential for catalysis; a point mutation of a
  conserved glutamate near the zinc abolishes activity [PMID:26833702 "A single point
  mutation of a conserved glutamate near the zinc ion results in total loss of activity,
  whereas zinc removal leads to instability of AmiC2-cat"].

The high-resolution (1.12 Å) crystal structure of the AmiC2 catalytic domain (AmiC2-cat)
from N. punctiforme (PDB 5EMI) differs markedly from the daughter-cell-separation and
PG-recycling amidases: it has a wide, shallow substrate-binding cavity and **lacks the
autoinhibitory α-helix** seen in E. coli AmiC [PMID:26833702 "A wide and shallow binding
cavity allows easy access of the substrate to the active site, which harbors an essential
zinc ion" ; "An inhibitory α-helix, as found in the Escherichia coli AmiC(E. coli)
structure, is absent"].

## Molecular function — amidase activity

AmiC2 is a bona fide N-acetylmuramoyl-L-alanine amidase. The N. punctiforme ortholog shows
amidase activity **in vivo and in vitro** [PMID:23444428 "The AmiC2 protein localizes to
the young septum between cells and shows bona fide amidase activity in vivo and in vitro"],
and the isolated catalytic domain "exhibits strong hydrolytic activity in vitro"
[PMID:26833702 "AmiC2-cat exhibits strong hydrolytic activity in vitro"]. It is assigned
EC 3.5.1.28 [PMID:26833702 "The N-acetylmuramoyl-l-alanine amidase AmiC2 (Npun_F1846; EC
3.5.1.28) in N. punctiforme generates arrays of such nanopores in the septal PGN"].
UniProt names alr0093 as "N-acetylmuramoyl-L-alanine amidase" [file:NOSS1/AmiC2/AmiC2-uniprot.txt
"SubName: Full=N-acetylmuramoyl-L-alanine amidase"].

## Biological process — septal PG remodelling / nanopore array / cell–cell communication

The enzyme perforates the septal peptidoglycan, creating the nanopore array
[PMID:28929086 "This enzyme perforates the septal peptidoglycan creating an array of
nanopores, which may be the framework for septal junction complexes"]. Ultrastructural
work on N. punctiforme showed AmiC2 "drills holes into the cross-walls, forming an array of
~155 nanopores with a diameter of ~20 nm each" [PMID:23444428], and this represents a
**novel function for a cell-wall amidase** distinct from the daughter-cell-separation role
of homologous amidases in unicellular bacteria [PMID:26833702 "in contrast to homologous
amidases that mediate daughter cell separation after cell division in unicellular
bacteria. Nanopore formation is therefore a novel property of AmiC homologs"].

In Anabaena PCC 7120, inactivation of amiC2 (alr0093) reduces the septal nanopore array and
impairs intercellular communication: "in the amiC2 mutant DR1992, the quantity of nanopores
was 31% of the wild type" [PMID:28929086], and in single amidase mutants "a decreased rate
of exchange of both calcein and 5-CF was observed, with rate constants about 60 and 30% of
the wild-type activity, respectively" (FRAP) [PMID:28929086]. The two amidases are partly
redundant; in the double mutant "filament morphology was affected and heterocyst
differentiation was abolished" [PMID:28929086]. Overall, "Inactivation of either amidase
resulted in significant reduction in nanopore count and in the rate of fluorescent tracer
exchange between neighboring cells measured by FRAP analysis" [PMID:28929086].

In N. punctiforme, where amiC1 could not be inactivated, AmiC2 alone is essential: mutation
of the single gene "completely changes the morphology and abrogates cell differentiation
and intercellular communication" [PMID:21244533], establishing AmiC2 as "a novel morphogene
required for cell-cell communication, cellular development and multicellularity"
[PMID:21244533].

## Cellular localisation

AmiC2 is exported and localises to the division septum / cross-wall (i.e. the
periplasmic cell-wall compartment where septal PG lies). In Anabaena "both amidases, AmiC1
and AmiC2, localized to the septa of young vegetative cells and to the septal and polar
neck areas connecting heterocysts with vegetative cells" [PMID:28929086]. AmiC2-GFP
"localizes in the cell wall with a focus in the cross walls of dividing cells"
[PMID:21244533]; native AmiC2 "localizes to the maturing septum" by immunofluorescence
[PMID:26833702]. AmiC2 covers the septal plane during invagination and is no longer
detectable in older septa [PMID:28929086 "AmiC2 localizes to the newly formed septum and
migrates during septal invagination to cover the entire septal plane. In older septa,
however, the protein can no longer be detected"].

The GOA CC annotation (GO:0030288 outer membrane-bounded periplasmic space) is a
defensible compartment call for a secreted amidase of a diderm (outer-membrane-bearing)
cyanobacterium acting on periplasmic septal PG; however the experimentally supported and
more informative location is the **cell septum (GO:0030428)**.

## Relationship to AmiC1 (alr0092)

AmiC1 (alr0092) is an adjacent, very similar paralog. In Anabaena the two are partly
functionally redundant for nanopore formation and cell–cell communication, but they are not
equivalent: amiC1 mutants are Fox− (cannot fix N2 aerobically) and delayed in heterocyst
differentiation, and AmiC1 (not AmiC2) is required for proper focal SepJ localisation and
influences the sepJ/fraCD filament-fragmentation phenotype [PMID:28929086 "these results
indicate that AmiC1 but not AmiC2 appears to be needed for proper subcellular localization
of SepJ" — paraphrase; verbatim: "deletion of amiC2 had no impact on the localization of
SepJ-GFP"]. AmiC1 was independently characterised in Berendt et al. 2012 [PMID:22821973
"Cell wall amidase AmiC1 is required for cellular communication and heterocyst development
in the cyanobacterium Anabaena PCC 7120 but not for filament integrity"] — that paper is
about the paralog, not alr0093. Care was taken to attribute each result to the amidase
actually assayed.

## Nanopore-array mechanism (context)

The septal cross-wall of heterocyst-forming cyanobacteria carries a semi-regular array of
~100–150 nanopores. These are the sites where septal junctions (built from SepN/FraD, with
SepJ/FraCD as associated septal proteins) traverse the septal PG to connect neighbouring
cytoplasms. The amidases AmiC1/AmiC2 act **upstream** to drill and pattern this nanopore
array (an assembly prerequisite for SJs); see `modules/septal_junction.yaml`, which grounds
AmiC2 (alr0093) as the primary nanopore driller.

## Cited references (verified via NCBI eutils / cached in publications/)

- PMID:28929086 — Bornikoel et al. 2017, Front Cell Infect Microbiol — PRIMARY (Anabaena
  amiC1/amiC2 mutants, nanopores, FRAP, heterocysts). Full text cached.
- PMID:21244533 — Lehner et al. 2011, Mol Microbiol — "The morphogene AmiC2 is pivotal for
  multicellular development in Nostoc punctiforme." Abstract cached.
- PMID:23444428 — Lehner et al. 2013, FASEB J — "Prokaryotic multicellularity: a nanopore
  array for bacterial cell communication." Abstract cached.
- PMID:26833702 — Büttner et al. 2016, FEBS J — "…structure, function and localization of
  the unique cell wall amidase AmiC2 of Nostoc punctiforme." (crystal structure, PDB 5EMI).
  Abstract cached.
- PMID:22821973 — Berendt et al. 2012, J Bacteriol — AmiC1 (alr0092) paralog (context only).
</content>
