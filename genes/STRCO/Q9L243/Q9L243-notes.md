# SCO2678 (Q9L243) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No notes file existed before this session; this is the first entry. ProtNLM2 files and
prediction-evidence folders were not opened. The earlier OpenScientist audit under
`Q9L243-hypotheses/` was written to audit a ProtNLM prediction chain, so it is retained
as a reference but no longer used as support; all claims below rest on my own analysis
(`Q9L243-bioinformatics/RESULTS-rereview.md`) and on PMID:27536007.

### Identity
- Q9L243 is the full-length, sole UniProt entry for SCO2678 (171 aa, TrEMBL, PE 4). It is
  not a fragment, isoform or alternative gene model; the Pfam HAD_SAK_2 match spans
  residues 9-155, i.e. essentially the whole protein.
- The UniProt name "Secreted protein" is a ProtNLM machine label (ECO:0008006) and is not
  evidence. The sequence has no signal peptide, Tat signal or lipobox.

### Family / evolutionary placement
- Only signature: Pfam PF18143 HAD_SAK_2. No PANTHER family, therefore no PAINT node and
  no IBA; no characterized relative can be reached by a phylogenetically grounded route.
- PF18143 was defined by Burroughs & Aravind [PMID:27536007 "The stramenopile Aphanomyces
  fuses a Rnl2-like ligase module with a PAP-like Polβ NTase module, another
  previously-uncharacterized HAD family (Supplementary Material), 2H, P-loop kinase,
  MJ1316, and RWD domains in a single protein"]. The RNA-repair role is a contextual
  prediction for the eukaryotic multidomain proteins, and characterized RNA-ligase
  associated HAD domains (e.g. T4 Pnkp) belong to other HAD families [PMID:27536007
  "Experimentally-characterized RNA ligase-associated HAD domains, in a reaction typical
  of the HAD superfamily (166,167), cleave the cyclic phosphate group from the 3′ end of
  a RNA fragment"]. SCO2678 is a stand-alone bacterial member with no ligase/kinase
  neighbours, so the RNA-repair role is not transferred.
- eggNOG COG1877 (OtsB, trehalose-6-phosphate phosphatase) is a superfamily-level grouping;
  NCBI COG does not place SCO2678 in COG1877 and SCO2678 lacks the OtsB cap/length.
  Not transferred.

### Function
- All four HAD core motifs are intact (D13/D15, T67, K106, D123/D124), so a
  Mg2+-dependent phosphoryl-transfer (phosphatase) activity is the defensible prediction;
  substrate unknown. This supports a generic `phosphatase activity` (GO:0016791) at ISM
  level; nothing more specific is warranted.
- Localization: soluble cytoplasmic protein by absence of any export signal (GO:0005737).
  This is a sequence-based inference, weak but consistent.
- No process term proposed (no pathway evidence, no fitness data available: `just
  fetch-fitness STRCO Q9L243` found no FEBA data).

### GOA
- GOA file has zero annotations for Q9L243; the two rows in the review are NEW proposals.

### Relative
- No PANTHER/PAINT placement and no experimentally characterized PF18143 member exist, so
  no relative can be chosen phylogenetically; reported as none_found.
- No modules in `modules/` reference PF18143 or SCO2678; no PANTHER family review applies.
