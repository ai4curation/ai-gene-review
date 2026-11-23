---
title: "eggNOG-mapper Failure Modes by Ontology"
autolink_gene_symbols: false
---

# eggNOG-mapper failure modes by ontology

[Back to the eggNOG-mapper evaluation](../EGGNOG_MAPPER_EVALUATION.md)

This page collects every adjudicated eggNOG-mapper GO term that was judged
wrong, organised by GO aspect and error type. The full catalog, with each
reviewer's rationale, is
[`adjudication/failure_modes.yaml`](adjudication/failure_modes.yaml). Tallies
are in [`adjudication/summary.yaml`](adjudication/summary.yaml).

## Samples

All claims come from the run that hid the query's own species. Two samples
were drawn:

- **Round 1:** 80 leaves (40 UNRELATED, 20 REJECTED, 20 NARROWER), at most
  one per protein per stratum.
- **Round 2:** 72 leaves stratified by aspect. For each of MF, BP and CC it
  took 12 UNRELATED, 6 REJECTED and 6 NARROWER leaves, from proteins not used
  in round 1.

The two rounds give 152 claims. AI reviewers judged each against the gene's
review, UniProt record and notes, using the COR/LSP/UNC/PLI/NPI/REP scheme of
PMID:40703034.

Round 2 gives the like-for-like comparison across ontologies, since each
aspect had the same 24-claim design:

| Aspect | Correct (COR) | True but vague (LSP) | Undecided (UNC) | Wrong (NPI/PLI/REP) |
|---|---|---|---|---|
| MF | 4 | 3 | 1 | **16** |
| BP | 5 | 2 | 5 | **12** |
| CC | 3 | 2 | 9 | **10** |

Pooling both rounds (MF 41, BP 66, CC 45 claims), 61% of MF, 45% of BP and
42% of CC claims were wrong.

This reverses the automatic picture on the main page, where MF has the
highest exact-match rate. Molecular-function transfers are usually either
already in GOA or wrong: when emapper proposes an MF term that the review
does not have, it is wrong most of the time. Cellular-component claims are
the hardest to settle (9 of 24 undecided), because a location is rarely
refuted outright.

## Molecular function

25 wrong calls. MF errors are about **what the protein is**: the transferred
activity belongs to a different molecule in the same family, complex or
pathway.

| Error type | n | What goes wrong | Examples |
|---|---|---|---|
| Source annotation wrong | 8 | A mistaken row on one ortholog is copied to the whole group | KRAS given guanyl-nucleotide exchange factor activity (it is the GEF's substrate); thioredoxin given thioredoxin reductase activity; the TRAIL ligand given "TRAIL binding", a receptor term; fly Idh given (R)-2-hydroxyglutarate dehydrogenase, a cancer-mutant neomorphic activity |
| Domain the protein lacks | 6 | The activity needs a domain or motif this protein does not have | SecA given ABC-type transporter activity; TOMM70, a TPR receptor, given protein-transporting ATPase activity; fission yeast cab4 given dephospho-CoA kinase, a domain only its bifunctional orthologs carry; UBL-5 given protein tag activity although it lacks the C-terminal di-glycine |
| Paralog or subfamily | 4 | Function of a sister subfamily | *P. putida* AcnD-type 2-methylcitrate dehydratase given aconitate hydratase; *S. aureus* FosB given glutathione transferase (FosA's activity; staphylococci have no glutathione); CcmG given protein disulfide isomerase; CRTISO, an isomerase, given oxidoreductase activity |
| Complex activity on a non-catalytic subunit | 3 | Activity of the holoenzyme assigned to a regulatory or scaffold subunit | calcineurin B (Ppp3r1) given phosphoprotein phosphatase activity; worm DDB-1 given damaged DNA binding (DDB2's role); dynein-2 heavy chain given dynein light chain binding |
| Pseudoenzyme | 1 | Ancestral activity on a member that lost it | HSP47 (Serpinh1) given serine-type endopeptidase inhibitor activity |
| Others | 3 | Wrong context, in vitro only, generic | worm MUT-7 given the fly-specific miRNA 3'-end trimming term; yeast Cdc14 given tyrosine phosphatase activity; monomeric rat RNase 1 given identical protein binding |

## Biological process

30 wrong calls. BP errors are about **where the knowledge came from**. Process
terms are usually inferred from a mutant phenotype in one model organism.
Copying them carries over that organism's anatomy and that phenotype's
indirect causes.

| Error type | n | What goes wrong | Examples |
|---|---|---|---|
| Process that cannot exist in this lineage | 9 | The term names anatomy, cell types or mechanisms the target organism lacks | worm ced-6 given mushroom body development (insects); worm dyf-6 given retina development in camera-type eye; fly elg1 given positive regulation of B cell proliferation; fly alc given nail development; fly mre11 given telomere maintenance via telomerase (flies have none); yeast HST2 given Candida phenotypic switching |
| Phenotype read as process | 9 | A downstream consequence of losing the gene becomes a process it performs | UCK2 given feeding behavior; fly Pde4/dunce given negative regulation of locomotion; zebrafish tbx5b given pericardium development from cardiac edema; yeast HSC82 given filamentous growth; *P. putida* ssuD given response to heat |
| Source annotation wrong | 8 | Mis-scoped or mis-read source rows | mouse App given protein phosphorylation (the paper shows dephosphorylation); Arabidopsis D14, the strigolactone receptor, given strigolactone biosynthesis; Dnajb11, a target gene of the UPR, given IRE1-mediated UPR; Rbpj given DNA recombination, a relic of its original name; SPCS3 given protein targeting to ER |
| Generic or out-of-context | 4 | High-frequency or host-pathogen terms | ALDH4A1 given signal transduction; worm cebp-2 given mRNA metabolic process; worm DDB-1 given interaction with symbiont (from viral hijacking of human DDB1); Hspa8 given autophosphorylation |

## Cellular component

19 wrong calls, and the most undecided calls. CC errors are about **the
target's own sorting signals and anatomy**. A location inherited from an
ortholog ignores whether this protein has the targeting sequence, membrane
anchor or organelle that location requires.

| Error type | n | What goes wrong | Examples |
|---|---|---|---|
| Source annotation wrong | 7 | High-throughput or co-purification locations carried across | fission yeast Rad21 given mitochondrion; rat Amacr and fly Gcat, both matrix enzymes, given plasma membrane; fly Acadvl given mitochondrial nucleoid (co-purification); fly and *Aspergillus* NudE given kinesin complex; EGF given signaling receptor complex |
| Structure absent in this lineage | 4 | The compartment does not exist in the target | mouse Ccnt1 given polytene chromosome puff; worm unc-47 given cone cell pedicle; yeast Hrt1 given Cul7-RING complex; worm che-11 given centrosome (its ciliated neurons are post-mitotic) |
| Default compartment | 4 | Generic cytoplasm, cytosol or nucleus overriding a specific location | rat Sstr5, a plasma-membrane GPCR, given cytoplasm; horse DARS2, a mitochondrial tRNA synthetase, given nucleus; lipid-anchored worm PEF-1 given nucleus; fly Myd88 given cytosol although it is held at the membrane |
| Paralog | 2 | Location of a sister protein | yeast Swi3 given RSC-type complex (yeast RSC uses Rsc8); mouse Ang2 given neuronal cell body (from angiogenin) |
| Missing targeting signal | 1 | The donor's location depends on a motif the target lacks | fly Idh given peroxisomal matrix; fly isoforms lack the PTS1 that sends human IDH1 there |
| Other | 1 | Wrong organelle family-wide | the *Starmerella* sophorolipid exporter Mdr given fungal-type vacuole |

## What goes right

31 of the 152 claims were correct additions. Most were specific and
mechanistic, and many filled gaps in GOA:
- macroautophagy for the fly VMP1 ortholog Tango5;
- site of double-strand break for rat Tp53;
- peptidyl-prolyl isomerization for SurA;
- allantoin biosynthesis for zebrafish uox;
- mitochondrial inner–outer membrane contact site for Ckmt2;
- mRNA splicing via spliceosome for CBP80.

Correct NARROWER claims typically refine a curated parent, for example
nucleoplasm under nucleus and E-box binding under DNA binding.

## Reading the pattern

eggNOG-mapper copies the union of every ortholog's terms, with no support
threshold. Each error type above is a different way that one ortholog's
annotation fails to describe another protein:

- **MF:** the molecule differs (domain, subunit, subfamily).
- **BP:** the context differs (lineage, phenotype).
- **CC:** the protein's own sorting differs.

A single wrong source row, of which there were 23, is amplified rather than
outvoted.
