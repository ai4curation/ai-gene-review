# Manual deep-research synthesis for human RPL36A

Date: 2026-07-18

## Scope and retrieval

This synthesis covers human RPL36A (UniProtKB P83881) using the reviewed UniProt
record, all 58 fetched GOA groups, eleven cached GOA-cited publications, human
ribosome structures, and the complete ComplexPortal-linked muscle papers. The
Falcon research request failed with HTTP 402 and the Perplexity-lite fallback
failed with HTTP 401 because quota was unavailable. No provider-labelled report
was retained.

## Molecular identity and core function

RPL36A encodes the 106-residue large ribosomal subunit protein eL42, historically
called 60S ribosomal protein L36a or L44. The reviewed UniProt record assigns it
to the eukaryotic eL42 family and states that it is a component of the large
ribosomal subunit [file:human/RPL36A/RPL36A-uniprot.txt, "Component of the large
ribosomal subunit."]. Human 80S and pre-60S cryo-EM studies place the complete
protein in the cytosolic large ribosomal subunit [PMID:23636399,
"Structures of the human and Drosophila 80S ribosome."]; [PMID:25957688,
"Structural snapshots of actively translating human ribosomes."];
[PMID:32669547, "Structural snapshots of human pre-60S ribosomal particles
before and after nuclear export."].

Evidence conclusion: RPL36A/eL42 is a structural component of the cytosolic 60S
ribosomal subunit that supports cytoplasmic translation.

The cytoplasm, cytosol, ribosome, cytosolic-ribosome, large-subunit, structural-
constituent, and cytoplasmic-translation annotations all describe this same
well-supported molecular core. Broad `ribosome` and `translation` terms are
better represented by the existing more-specific cytosolic large-subunit and
cytoplasmic-translation terms.

## Interaction and RNA-capture annotations

Two generic protein-binding records do not define independent functions.
PMID:32296183 is a proteome-scale binary-interaction map. PMID:24965446 recovered
RPL36A among many ribosomal proteins in a GST-Npro pulldown and explicitly notes
that indirect co-purification is possible [PMID:24965446, "It may be that Npro
interacts with one or two of these RNA binding proteins, and the other proteins
are pulled down in the same complex."]. These records are retained as underlying
interaction observations but GO:0005515 is marked over-annotated.

The mRNA-bound-proteome study detects proteins associated with polyadenylated
RNA in living cells, but for a constitutive ribosomal protein this does not
separate direct mRNA contact from capture of an assembled translating ribosome
[PMID:22681889, "The mRNA-bound proteome and its global occupancy profile on
protein-coding transcripts."]. Generic RNA binding is therefore not promoted to
a second core molecular function.

## Muscle-process citation problem

The two ComplexPortal-derived process annotations cite studies of RPL3L, a
muscle-specific paralog of RPL3, not RPL36A. The full text of PMID:26684695 tests
inducible RPL3L in C2C12 cells and attributes reduced myoblast fusion to RPL3L
[PMID:26684695, "RPL3L expression significantly impaired myotube growth"]. The
abstract of PMID:34081545 likewise tests Rpl3l knockdown in mouse muscle. Neither
study perturbs, measures, or distinguishes RPL36A/eL42. Propagating negative
regulation of myoblast fusion or striated muscle contraction to every
constituent of a muscle ribosome is an over-annotation, so both NAS records are
marked MARK_AS_OVER_ANNOTATED rather than accepted as RPL36A-specific biology.

## Localization boundary

RPL36A is cytoplasmic and cytosolic as part of cytosolic ribosomes. An HPA-derived
endoplasmic-reticulum localization can reflect ribosomes engaged on the rough ER;
it is retained as non-core rather than interpreted as ER residency of a distinct
RPL36A pool. Reactome cytosol records are accepted consistently.

