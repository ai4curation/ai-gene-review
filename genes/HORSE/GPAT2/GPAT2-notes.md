# GPAT2 (horse, A0A3Q2HKJ8) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was opened or used. This folder was created for this review
(`just fetch-gene HORSE A0A3Q2HKJ8 --alias GPAT2`); the stub id is A0A3Q2HKJ8.

### Deep research

`just deep-research-falcon HORSE GPAT2 --fallback perplexity-lite` failed: falcon
returned "Edison API request failed: Failed to authenticate" (403) and the
perplexity-lite fallback also failed. No deep-research file exists; the review
uses the cached primary literature on mouse Gpat2 and UniProt records.

### Identity of the benchmark accession

- A0A3Q2HKJ8 is an unreviewed TrEMBL entry (PE 3), 800 aa, Ensembl
  ENSECAP00000034437.2, VGNC:18473 GPAT2, horse chromosome 15.
- It aligns over the full length of human GPAT2 Q6NUI2 (795 aa; 88.2% identity)
  and mouse Gpat2 Q14DK4 (801 aa; 83.9%), keeps the HXXXXD motif at 205-210
  (HKSLLD) and both predicted transmembrane segments
  [file:HORSE/GPAT2/GPAT2-bioinformatics/RESULTS.md]. It is the canonical
  full-length product, not a fragment or isoform. Identity to GPAM is 36.5%.
- UniProt places it in PANTHER PTHR12563:SF15 (GPAT2, mitochondrial), the same
  subfamily as human Q6NUI2, mouse Q14DK4 and rat D3ZI76
  (interpro/panther/PTHR12563/PTHR12563-entries.csv).

### Evolutionary grounding

- The IBA rows come from PAINT node PTN000970957 (taxon 6072, Eumetazoa), which
  contains both GPAT1 (GPAM) and GPAT2. Curators placed GO:0004366, GO:0005739,
  GO:0006650 and GO:0019432 there. They did NOT place piRNA processing or
  1-acylglycerol-3-phosphate O-acyltransferase activity at that node, although
  mouse Gpat2 carries both experimentally; I read that as a deliberate decision
  that these are not ancestral to the GPAT1/GPAT2 clade.
- The GO_REF:0000107 IEA rows are Ensembl Compara ortholog transfers from mouse
  Gpat2 (Q14DK4), which is in the same SF15 subfamily as the horse protein, so
  the transfers stay within the GPAT2 ortholog group.

### Literature (mouse Gpat2; human GPAT2 has only ISS annotation in UniProt)

- Cloning from mouse testis; NEM-sensitive GPAT activity rises 30% on
  overexpression; mitochondrial by confocal microscopy; oleate into TAG up 84%
  [PMID:17689486 "When Cos-7 cells were transiently transfected with GPAT2,
  NEM-sensitive GPAT activity increased 30%. Confocal microscopy confirmed a
  mitochondrial location."].
- Independent cloning (as xGPAT1): membrane fraction, GPAT activity in CHO-K1
  [PMID:17013544 "xGPAT1 was distributed in the membrane fraction and showed GPAT
  activity when epitope-tagged xGPAT1 was expressed in Chinese hamster ovary
  (CHO)-K1 cells."].
- Topology: two TM segments, N and C termini cytosolic [PMID:22285183].
- Arachidonoyl-CoA preference; GPAT and AGPAT activity rise 2-fold; authors say
  the AGPAT rise may be secondary and cannot exclude dual activity
  [PMID:22905194 "These findings suggest that the increase in PA may be due to an
  AGPAT activity for this heterologously-expressed protein, but we cannot exclude
  the possibility that the protein has dual enzymatic activities."].
- piRNA: Gpat2 binds MILI/PIWIL2 in germline stem cells; knockdown impairs
  primary piRNA production; catalytic HXXXXD mutants rescue, so the role does not
  need acyltransferase activity; authors propose a scaffold on the outer
  mitochondrial membrane [PMID:23611983].
- Testis-restricted, promoter-methylation-regulated expression [PMID:26268560].

### Decisions

- GO:0004366 GPAT activity: ACCEPT (IBA + IEA), core.
- GO:0003841 AGPAT activity (IEA): KEEP_AS_NON_CORE. Membrane-overexpression
  evidence only, the authors are equivocal, and PAINT did not propagate it.
- GO:0005739 mitochondrion (IBA, IEA) and GO:0016020 membrane: MODIFY to
  GO:0005741 mitochondrial outer membrane.
- GO:0006654 phosphatidic acid biosynthetic process (IEA): ACCEPT; GO:0019432
  triglyceride biosynthetic process (IBA): ACCEPT (the first acylation in the
  glycerol-3-phosphate route).
- GO:0006650, GO:0006629, GO:0016746, GO:0016747: TOO_GENERAL (entailed by
  GO:0006654 / GO:0004366).
- GO:0034587 piRNA processing (IEA): KEEP_AS_NON_CORE. A single knockdown study in
  cultured mouse germline stem cells with MILI binding and catalytic-dead rescue;
  this is a role within the pathway (a proposed scaffold), not just a downstream
  phenotype, but the mechanism is unknown and PAINT did not propagate it.

### Relative

Closest experimentally characterised relative is the mouse ortholog Gpat2
(Q14DK4, same PANTHER subfamily SF15). Human GPAT2 (Q6NUI2) has no experimental
data of its own (UniProt annotations are ECO:0000250 from Q14DK4). No mouse or
human GPAT2 review exists in the repo; the donkey GPAT2 (genes/EQUAS/GPAT2) is the
paired campaign target, reviewed separately.

### PANTHER family review

interpro/panther/PTHR12563/PTHR12563-review.yaml lists only SF16 (GPAM) as a
subfamily and keeps GO:0004366 UNRESOLVED for family scope, noting that GPAT2 is
also in the family. No disagreement with the SF15 placement of horse GPAT2; the
family review simply does not describe SF15.

### Modules

modules/triacylglycerol_biosynthesis.yaml covers the glycerol-3-phosphate
acylation step with GPAM (PTHR12563) as the animal exemplar; GPAT2 is a
testis-restricted member of the same family and is not a part of that module.
