# SIT2 (UniProtKB:B5YNJ0), Thalassiosira pseudonana — curation notes

No deep-research provider output was available; these notes come from my own reading of the cached
publications and the UniProt entries. Most of the family-level evidence is shared with SIT1; see
`genes/THAPS/SIT1/SIT1-notes.md` for the full literature summary. The sequence comparison for both
paralogs is in `genes/THAPS/SIT1/SIT1-bioinformatics/RESULTS.md`.

## Identity

- B5YNJ0 (475 aa, ORF THAPS_41392, EMBL ACI64637, reference proteome UP000001449) is TpSIT2. It is an
  exact C-terminal suffix of the cDNA-derived TpSIT2 (GenBank ABB81826, UniProtKB Q0QVM7, 528 aa) and
  lacks the first 53 residues, including a probable N-terminal transmembrane/signal segment
  (`SIT1-bioinformatics/RESULTS.md`).
- The TpSIT2 cloning primers in PMID:17172435 encode the Q0QVM7 N-terminus (MSSAEV) and the C-terminus
  shared with B5YNJ0 (EAVDAQA).
- "Pairwise comparison between each SIT revealed 88% amino acid identity and 95% similarity between
  TpSIT1 and TpSIT2" [PMID:17172435].

## SIT2-specific evidence

- Plasma membrane: "Epifluorescence microscopy of transgenic cells expressing SIT1 and SIT2 in
  Si-depleted cultures showed bright eGFP fluorescence in the plasma membrane under Si starvation for
  24 h" [PMID:25380754].
- Lower abundance than SIT1: "The eGFP intensity of SIT1 was higher than that of SIT2 at all time
  points" [PMID:25380754].
- Distinct regulation: "SIT2 had a response distinct from that of SIT1 after replenishment with
  different Si concentrations" — a rise at 3-4 h that tracks S phase; the authors offer preloading of
  silicic acid before valve formation, or another explanation, as hypotheses [PMID:25380754].
- Knockdown evidence is joint with SIT1 (one construct for both): "Separate knockdowns of SIT1 and
  SIT2 could not be pursued with the vector construction design used in this study" [PMID:25380754].
- Not biochemically characterized: TpSIT2 was not among the "11 full-length diatom SIT homologues"
  expressed by Knight et al. [PMID:27305972]. Molecular function is inferred from PtSIT1, NaSIT and
  TpSIT3 (ISS).

## GO decisions

Same as SIT1: ACCEPT GO:0015708 (IEA, InterPro2GO); NEW GO:0005886 plasma membrane (IDA,
PMID:25380754); NEW GO:0015115 silicate transmembrane transporter activity (ISS, PMID:27305972). No
sensing/regulatory process and no cell-wall biogenesis process annotated (hypothesis only; substrate
supply is not participation in silica polymerization).

ISS With/From donors are the same two as for SIT1, verified against the UniProt REST API on
2026-10-28: B7T1F4 (B7T1F4_PHATR, *P. tricornutum*, 512 aa, gene SIT1) and B8C4N0 (B8C4N0_THAPS,
*T. pseudonana*, 437 aa, gene SIT3). The paralog identity of the TpSIT3 donor comes from
[PMID:27305972 "TpSIT3, NaSIT and PtSIT1 were reconstituted into proteoliposomes preloaded with 6 mM Zn acetate"],
and the same paper makes it the weaker donor
[PMID:27305972 "PtSIT1 and NaSIT showed similar activity, but TpSIT3 gave a modest signal change that was only just discernible above background."].
See SIT1-notes.md for the full donor note.

The B5YNJ0 source defect is now `CONFIRMED` rather than `PROBABLE`: for this gene the exact
C-terminal-suffix sequence comparison against the cDNA-derived Q0QVM7 plus the full-text cloning
primer encoding MSSAEV [PMID:17172435] are primary data on their own, without leaning on the
eleven-SIT length range (which covers TpSIT1, not TpSIT2). `requested_change` stays `CHECK`,
because which start codon is used in vivo is untested.

## CMMMech claims (data/records/silicon.yaml)

- functional_role for B5YNJ0: "Silicon transporter SIT2 (THAPSDRAFT_41392) co-mediating silicic acid
  transport and silicon-responsive regulation of frustule biosilicification". Co-mediating silicic acid
  transport is supported (jointly with SIT1). "Silicon-responsive regulation of frustule
  biosilicification" goes beyond the evidence: the regulatory/sensing role is the authors' hypothesis,
  not tested for SIT2 alone, and the knockdown cannot distinguish SIT2 from SIT1.
- The causal-graph node describes SIT2 as "required for low-Si uptake and sensing"; requirement for
  SIT2 specifically was never shown (joint knockdown), and sensing is unproven.
- Locus name: CMMMech writes THAPSDRAFT_41392; UniProt gives the ORF name THAPS_41392 for B5YNJ0
  (the SIT1 entry uses the THAPSDRAFT_ prefix). Minor; worth harmonizing in CMMMech.
- As for SIT1, the CMMMech example is the N-terminally truncated gene-model entry, not the full-length
  cDNA entry Q0QVM7.
