---
title: "Transposon-derived proteins and the host annotations they inherit"
maturity: SCOPING
tags: [EVALUATION]
collections: [HOMOLOGY_PROPAGATION]
index_group: CROSS_CUTTING
description: Where IBA and other propagation give transposable-element ORFs the biology of host genes, and where a transposon-domain protein is a genuine domesticated gene
species: [human, mouse, CHICK, DROME, ARATH, SCHPO]
genes: [TERT, ARC, PEG10]
---

# Transposon-derived proteins and the host annotations they inherit

Genomes are full of open reading frames from transposable elements (TEs): retrotransposon
Gag-Pol ORFs, endogenous retroviruses, DNA-transposon transposases. Most are selfish sequence
with no host function. A few have been domesticated into host genes with real, conserved roles.
UniProt states such an origin for SETMAR (a methylase fused to a mariner transposase), syncytin-1
(ERVW-1, a retroviral envelope that fuses trophoblast), ARC and PEG10 (Ty3/gypsy Gag-derived
capsid proteins) and PGBD5 (a transposase domesticated about 500 million years ago).

This project asks how often annotation pipelines confuse the two kinds of protein:
- a TE ORF that inherits a host gene's biology because a family or PAINT node groups them;
- a domesticated gene whose own function is lost or mislabelled as "transposon".

It belongs with the [IBA review](IBA_REVIEW.md), where the relevant failure is
[issue 12, mis-grouping revealed by the WITH/FROM column](IBA_REVIEW.md#12-mis-grouping-revealed-by-the-withfrom-column).

## How it started: Pericardin and a chicken reverse transcriptase

The RAR triage of vertebrate-flagged terms
([rar_rerun_triage_fungus_vertebrate.yaml](RAR_MISANNOTATION/data/rar_rerun_triage_fungus_vertebrate.yaml))
found GO:0007508 larval heart development on chicken A0A8V0ZN40. That protein is a reverse
transcriptase ORF (Pfam PF00078 and PF14529, no other domains). The annotation is an IBA from
PAINT node PTN008655974, whose only experimental donor is fly Pericardin, a basement-membrane
collagen of the heart.

The cause is the PANTHER family. PTHR33395 is named "TRANSCRIPTASE, PUTATIVE-RELATED-RELATED".
It holds Pericardin as subfamily SF21 ("PERICARDIN") beside SF22 ("REVERSE TRANSCRIPTASE
DOMAIN-CONTAINING PROTEIN"), so a node placed above both carries Pericardin's terms to the
transposon ORFs.

The node propagates three terms and 2,072 IBA rows in all (QuickGO, 2026-11-23):

| Term | Rows |
|---|---|
| GO:0031012 extracellular matrix | 730 |
| GO:0007508 larval heart development | 671 |
| GO:0061343 cell adhesion involved in heart morphogenesis | 671 |

By lineage that is 510 vertebrate, 201 mollusc, 114 nematode and 642 arthropod rows, of which
only 21 are in Diptera, the order that has Pericardin. Only three of the 2,072 rows, all on the
one chicken protein, fall in the model-organism proteomes scanned below. The RAR screen found it only because the screen looks
at those proteomes.

## First scan: model-organism proteomes

[scripts/scan_te_iba.py](TRANSPOSON_DERIVED_ANNOTATIONS/scripts/scan_te_iba.py) collects every
protein with a TE Pfam domain in 12 proteomes and lists the IBA rows on them by PAINT node. The
proteomes are human, mouse, rat, chicken, zebrafish, fly, worm, Arabidopsis, the two yeasts,
*Candida* and *Dictyostelium*. The domains are reverse transcriptase, integrase, Pao RNase H,
two DDE endonuclease families and IS4 transposase. The output is
[data/te_iba_scan.yaml](TRANSPOSON_DERIVED_ANNOTATIONS/data/te_iba_scan.yaml).

The scan found 1,152 TE-domain proteins. Only 100 of them carry an IBA (191 rows), from 13 nodes,
so in curated proteomes PAINT mostly leaves TE ORFs alone. A first reading of the nodes:

| Node | TE-domain proteins | Terms | First reading |
|---|---|---|---|
| PTN002712198 | 38 | DNA binding, nucleus | Domesticated pogo transposases (CENPB, JRK, TIGD, fission-yeast cbh1/cbh2, PDC2); fits |
| PTN002222925 | 38 | RNA stem-loop binding | HERV-K Gag-Pro-Pol ORFs in human, and chicken Gag-Pro-Pol ORFs; a TE-to-TE transfer, to check |
| PTN002005226 | 5 | transposase activity, DNA transposition | PGBD5 orthologs, a domesticated active transposase; fits |
| PTN000249074 | 5 | telomerase activity and complex | TERT; a host enzyme with a reverse transcriptase domain, not a TE |
| PTN002931680 | 4 | sequence-specific DNA binding | PGBD1-3; plausible for domesticated piggyBac genes |
| PTN008617116, PTN002810938, PTN001227002 | 3, 2, 2 | transcription factor terms | POGZ and fish/chicken orthologs; fits |
| PTN001458056 | 2 | RNA-directed DNA polymerase, intron homing | Yeast mitochondrial group II intron proteins; fits |
| PTN000360827, PTN001018444 | 1 | transcription factor terms; PcG complex | A zebrafish zinc finger-THAP-transposase fusion; the PcG term is unclear |
| PTN002505681 | 1 | chromatin binding, ESC/E(Z) and PRC1 complexes | Arabidopsis ALP1, a transposase-derived antagonist of Polycomb silencing; the complex terms need checking |
| PTN008655974 | 1 | larval heart development, ECM, heart cell adhesion | Chicken RT ORF inheriting fly Pericardin; wrong |

Most of these are domesticated genes doing what the terms say. The clear error is the
Pericardin node, and it is the kind of error a model-proteome scan barely sees.

## Scope and caveats

- **A TE domain is not proof of a TE.** TERT has a reverse transcriptase domain, and domesticated
  genes keep their transposase or Gag domains. Each node has to be read against the proteins it
  reaches.
- **The domain list is a choice.** Gag, envelope and other transposase families are not in the
  first scan. The script's lists are easy to extend.
- **IBA is only one route.** InterPro2GO, ARBA and ortholog projection can carry host terms to TE
  ORFs too. The first scan covers IBA only.

## Next steps

- [ ] Review PTHR33395: confirm that SF22 members are TE ORFs and ask PAINT to move the
  Pericardin IBD from PTN008655974 down to the Pericardin subfamily, as a family review under
  `interpro/panther/`.
- [ ] Scan beyond model proteomes: list the PAINT nodes whose IBA rows land on TE-domain proteins
  across UniProt, since that is where the Pericardin node does nearly all its damage.
- [ ] Check the two unclear nodes: the HERV-K "RNA stem-loop binding" transfer to chicken
  Gag-Pro-Pol ORFs, and the Polycomb complex terms on ALP1 and the zebrafish fusion protein.
- [ ] Extend the scan to Gag, envelope and further transposase domains, and to InterPro2GO and
  ARBA rows.
- [ ] Use the domesticated genes reviewed here (ARC, PEG10, TERT) as controls: their terms
  should survive any filter the project proposes.
