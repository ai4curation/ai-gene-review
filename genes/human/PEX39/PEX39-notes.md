# PEX39 (Q5I0X4, HGNC:34431; formerly C6orf226) review notes

## Why this gene was selected

PEX39 is a "curation gap" case rather than a contested one: a 101-residue C-orf that was
deorphanized in 2025 and renamed by HGNC to PEX39 (Peroxisomal biogenesis factor 39), with
HGNC citing PMID:40739340 and placing the gene in the Peroxins group. GOA has partly caught
up (one IDA MF, one IMP BP from that paper) but the bulk of the record is still bare
`protein binding` from binary-interactome screens.

## Reference verification

PMID:40739340 verified against PubMed: Chen WW, Rodrigues TA, Wendscheck D, et al.
"PEX39 facilitates the peroxisomal import of PTS2-containing proteins." Nat Cell Biol
2025 Aug;27(8):1256-1271. doi:10.1038/s41556-025-01711-z. PMC12339391. Full text cached.

UniProt's FUNCTION block for Q5I0X4 additionally cites PMID:37160800, which PubMed resolves
to Pedrosa AG et al., "Peroxisomes: novel findings and future directions", Histochem Cell
Biol 2023;159(5):379-387 — a meeting/review article, not primary evidence for PEX39. It is
not used here as support for any annotation.

## What the 2025 paper establishes

Headline claim:
[PMID:40739340 "we show that PEX39, a previously uncharacterized protein, is a cytosolic
peroxin that facilitates the import of PTS2-containing proteins by binding PEX7 and
stabilizing its interaction with cargo proteins containing a PTS2."]

Localization (human, endogenous protein, cell fractionation):
[PMID:40739340 "whereas cellular fractionation revealed that endogenous HsPEX39 is cytosolic"]

Loss-of-function phenotype in human cells (the basis of the IMP):
[PMID:40739340 "Importantly, cellular fractionation revealed that HsPEX39 loss led to an
accumulation of precursor PHYH in the cytosolic fraction and a decrease of mature PHYH in
the organellar fraction, thus demonstrating impaired import of PTS2-containing proteins"]

Pathway selectivity — PTS2 and not PTS1:
[PMID:40739340 "In contrast with the import of PTS2-containing proteins, recombinant HsPEX39
had no effect on the import of PTS1-containing proteins in vitro, as assessed by import of
the PTS1-containing protein SCP2"]

Mechanism part 1, the clamp (in vitro native PAGE with recombinant proteins):
[PMID:40739340 "Collectively, our data indicate that PEX39 stabilizes the interaction between
PEX7 and PTS2-containing proteins, thereby providing a mechanism by which PEX39 facilitates
the import of PTS2-containing proteins."]
The KPWE motif is required: [PMID:40739340 "HsPEX39(4A) could not interact with PEX7 and
failed to stabilize the interaction between PEX7 and the PTS2-containing protein PHYH"]

Mechanism part 2, the handover to PEX13:
[PMID:40739340 "PEX39 and PEX13, a peroxisomal membrane translocon protein, both possess an
(R/K)PWE motif necessary for PEX7 binding."]
[PMID:40739340 "These results suggest that PEX39 must dissociate from PEX7 to allow PEX7 to
bind the N terminus of PEX13 at the peroxisome, a handover mechanism that would be
facilitated if the PEX39–PEX7 interaction were labile."]
[PMID:40739340 "Because of the labile nature of the PEX39–PEX7 interaction via the (R/K)PWE
motif, PEX39 can now be exchanged with the PEX13 N terminus, which also contains a KPWE
motif (steps 4 and 5), thus handing PEX7 over from PEX39 to PEX13."]
[PMID:40739340 "Handover of PEX7 from PEX39 to PEX13 via these motifs provides a new paradigm
for peroxisomal protein import and biogenesis."]

## The one point where GOA over-reaches

GOA carries `GO:0000268 peroxisome signal sequence receptor activity` (IDA, PMID:40739340).
The GO definition of that term is "Binding to a peroxisomal targeting sequence, a short
stretch of amino acids found in a protein that acts as a signal to localize the protein to
the peroxisome." The source paper explicitly reports the opposite for PEX39 in isolation:
[PMID:40739340 "HsPEX39 could not complex with either PEX5 or PHYH alone, per native PAGE"]

PEX39 therefore does not itself read the PTS2; it binds PEX7 (nanomolar, via its KPWE motif)
and its N-terminal region then clamps the PEX7-cargo pair together. A direct PEX39-PTS2
contact is predicted by AlphaFold, and the N-terminal truncation/L21A data are consistent
with it, but it was not measured as an independent binding event.

This is `MODIFY`, not `REMOVE`: the annotation's essence (PEX39 acts in PTS2 receptor
function) is right, the term is simply the receptor term rather than the co-receptor one.
The replacement chosen is `GO:0140597 protein carrier chaperone` (renamed "protein carrier activity" in current GO; "Directly binding to a
protein and delivering it either to an acceptor molecule or to a specific location"), which
is exactly what the handover model describes, and which is the term the budding-yeast PTS2
co-receptor Pex21 (P50091) already carries with IDA evidence in GOA — so this keeps PEX39
consistent with how GO already treats PTS2 co-receptors. `GO:0030674
protein-macromolecule adaptor activity` would also be defensible for the clamp step; the
carrier term was preferred because it captures both the clamp and the delivery to PEX13.

## Consistency with the PEX7 and PEX13 reviews in this repository

- `genes/human/PEX7/PEX7-ai-review.yaml` describes PEX7 as the PTS2 receptor whose cargo-bound
  form requires the co-receptor PEX5L and docks via the PEX13-PEX14 complex. PEX39 slots into
  that description as the cytosolic factor that stabilizes the PEX7-cargo pair before docking;
  the same PTS2 cargoes are named (PHYH, AGPS, thiolase/ACAA1).
- `genes/human/PEX13/PEX13-ai-review.yaml` describes PEX13 as the docking/translocation module
  component with an N-terminal YG-rich IDR and a C-terminal SH3 domain that binds PEX5 via
  WxxxF/Y motifs. The 2025 paper adds a second, PTS2-specific receptor-binding element to that
  picture: a conserved KPWE motif in the PEX13 N terminus that binds PEX7 at the same site as
  the PEX39 KPWE motif. The terminology used here ("(R/K)PWE motif", "handover", "docking/
  translocation module") follows both those files and the paper.

## Curation position taken

- `GO:0005829 cytosol` (IEA and IDA) -> **ACCEPT** for both; this is the site of action, not
  just a residence. Endogenous human PEX39 fractionates as cytosolic.
- `GO:0016560 protein import into peroxisome matrix, docking` (IMP) -> **ACCEPT**, with the
  caveat recorded that the measured phenotype is failure of PTS2 import as a whole
  (`GO:0016558`) and that PEX39's own contribution is cytosolic cargo loading plus the
  PEX7 handover that immediately precedes/enables docking.
- `GO:0000268 peroxisome signal sequence receptor activity` (IDA) -> **MODIFY** to
  `GO:0140597 protein carrier chaperone` (see above).
- `GO:0005515 protein binding` x5 (IPI) -> **MARK_AS_OVER_ANNOTATED** per project guidance.
  Note that these are not all equivalent: four come from binary-interactome screens
  (PMID:25416956, PMID:29892012, PMID:31515488, PMID:32296183) with partners that have no
  known peroxisomal connection, whereas the fifth (PMID:40739340, WITH UniProtKB:O00628 =
  PEX7) is the functionally central interaction. The project rule requires one action per GO
  term, so all five are marked over-annotated and the PEX7 interaction is carried instead by
  the molecular-function and core-function entries, where it is informative.

## Open questions

- Does PEX39 contact the PTS2 nonapeptide directly, as AlphaFold predicts, or only stabilize
  the PEX7 groove allosterically? A PEX39 crosslink to the PTS2 peptide would settle it.
- Human PEX5L is the recognized PTS2 co-receptor; PEX39 and PEX5L are both present in the
  same in vitro complex (PEX7-PHYH-HsPEX39-PEX5). What is the order of events, and is PEX39
  required for PEX5L loading or independent of it?
- No PEX39 patient variants are reported. Since PEX39 loss impairs but does not abolish PTS2
  import, PEX39 is a candidate modifier rather than a primary Zellweger-spectrum gene, which
  is worth testing in unsolved PTS2-import-defect cohorts.
