# SEC11 notes

## Literature summary

No `SEC11-deep-research-*.md` file was present in this sparse worktree, so this
review was completed from the seeded GOA rows, the cached UniProt and PANTHER
files, seeded publications, and manual literature checks for newer yeast
SEC11/Sec11 signal peptidase papers.

The core SEC11 story is compact and well supported. Bohni, Deshaies, and
Schekman cloned the authentic yeast SEC11 locus and showed that temperature
sensitive `sec11` cells accumulate core-glycosylated invertase and acid
phosphatase precursors that still carry signal peptides, separating Sec11 from
upstream ER entry and pointing specifically to signal peptide removal
[PMID:3283143, "At 37 degrees C, the restrictive growth temperature, sec11 cells
accumulate core-glycosylated forms of invertase and acid phosphatase, each
retaining an intact signal peptide."]. YaDeau and Blobel solubilized yeast
signal peptidase as an integral membrane enzyme and showed in vitro that it
removes the prepro-alpha-factor signal peptide [PMID:2644273,
"Radiosequencing of the cleaved substrate revealed that the enzyme removed the
signal peptide."; "The membrane association of yeast signal peptidase is
resistant to carbonate extraction, indicating that it is an integral membrane
protein."].

The SPC component assignments also fit cleanly. YaDeau, Klein, and Blobel
purified yeast microsomal signal peptidase as a four-polypeptide complex and
identified its 18 kDa chain as the SEC11 product [PMID:1846444, "Partially
purified yeast microsomal signal peptidase appears to be a complex of four
polypeptides of 13, 18, 20, and 25 kDa. The 18-kDa chain is the product of the
Sec11 gene, which is necessary for signal peptidase activity."]. Spc3 was later
purified as the fourth subunit and shown to be essential for in-vivo precursor
processing and in-vitro signal peptidase activity [PMID:9148931, "Depletion of
SPC3 leads to accumulation of precursors of secretory proteins in vivo and to
the loss of the signal peptidase activity in vitro."]. Spc1 and Spc2 are
noncatalytic and nonessential under standard conditions, but they are
functionally distinct accessory subunits [PMID:8910564, "These results indicate
that although both Spc1p and Spc2p are noncatalytic, they are functionally
distinct."].

VanValkenburgh and colleagues established that Sec11 carries the catalytic
chemistry of ER SPC: a serine, a histidine, and two aspartates are important for
yeast Sec11 signal peptidase activity [PMID:10206957, "Instead, a serine,
histidine, and two aspartic acids are important for signal peptidase activity
by the Sec11p subunit of the yeast signal peptidase complex."]. The follow-up
OST/SPC paper used signal-peptide cleavage of prepro-alpha-factor and
preinvertase to show that signal peptide removal must precede efficient
glycosylation at nearby Asn-X-Ser/Thr sites in the ER [PMID:11058593, "We
demonstrate that the signal peptides of prepro-alpha-factor and preinvertase
must be cleaved before Asn-X-Ser/Thr acceptor tripeptides located near the
signal peptides of these precursors can be efficiently glycosylated within the
endoplasmic reticulum of the yeast Saccharomyces cerevisiae."].

Two newer full-text studies refine substrate selection without changing the core
GO picture. The 2024 Spc2 study shows that removing or mutating Spc2 changes
substrate discrimination and cleavage-site choice by yeast SPC
[PMID:39565596, "Our data show that discrimination between substrates and
identification of the cleavage site by SPC is compromised when Spc2 is absent
or mutated."]. The 2026 Sec11 C-terminal-short-helix paper shows that the Sec11
CTS spans the ER membrane and selectively helps process internal signal
sequences while preserving core Sec11-Spc3 assembly and standard N-terminal
signal-sequence cleavage [PMID:42586426, "While N-terminal signal sequences of
varying hydrophobicity were efficiently cleaved, internal signal sequences with
extended N-terminal region were selectively defective in cleavage in the absence
of the Sec11 CTS."].

## PAINT and annotation decisions

PTHR10806 is the signal peptidase complex catalytic subunit family for SEC11.
The PAINT slice contains three node assertions:

- `PTN000086749`: `GO:0008233 peptidase activity` at the family root, seeded by
  S. cerevisiae SEC11 plus metazoan, Plasmodium, and other SEC11A/SEC11C
  signal-peptidase descendants.
- `PTN000086750`: `GO:0005787 signal peptidase complex` at Eukaryota.
- `PTN000086750`: `GO:0051604 protein maturation` at Eukaryota.

The PTN000086750 rows are well scoped for SEC11: the Eukaryota node matches the
ER heterotetrameric SPC, and the yeast gene itself is a descendant with direct
experimental evidence, so the self-appearance in the IBA `WITH/FROM` list is
not circular. The PTN000086749 row is not biologically wrong, but at the gene
level it is less informative than `GO:0009003 signal peptidase activity`, so the
GO:0008233 rows were modified to that specific term.

All `GO:0005515 protein binding` rows were removed because they assert only
generic interactions with Spc1 or Spc3. The useful biological statement is that
Sec11 is part of the ER signal peptidase complex, which is already captured by
the accepted `GO:0005787` rows.

The broad CC rows were refined rather than dropped: `GO:0005783 endoplasmic
reticulum` and `GO:0016020 membrane` were modified to `GO:0005789 endoplasmic
reticulum membrane`. The `GO:0045047 protein targeting to ER` and
`GO:0051604 protein maturation` rows were modified to `GO:0016485 protein
processing` because the original sec11 phenotype shows that the assayed
precursors entered the ER and became core-glycosylated; the defect was
proteolytic signal-peptide cleavage after entry, not the upstream targeting
reaction.
