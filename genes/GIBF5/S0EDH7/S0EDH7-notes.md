# S0EDH7 (FFUJ_06423) notes

## Re-review 2026-10-01 (GOA refresh)

- Current GOA snapshot has no rows for S0EDH7; nothing to review or retire.
- core_functions audit: the previous core function asserted GO:0004672 protein kinase
  activity + GO:0006468 protein phosphorylation and cited the ProtNLM predictions review
  with a quote ("both assessed as COR") that is not in that file - the predictions
  review actually assesses both ProtNLM predictions as UNC. Only fold-level kinase-like
  signatures exist (IPR011009, Gene3D 1.10.510.10, SSF56112; no Pfam-level kinase
  family), and the PKL fold includes small-molecule kinases (APH/choline kinase-like).
  Broadened the MF to GO:0016301 kinase activity, dropped the protein phosphorylation
  BP, added a knowledge gap, replaced the non-verbatim quote, and reworded the
  description accordingly.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM output was not opened or used. Identity: S0EDH7 is the only UniProt entry for
FFUJ_06423 (TrEMBL, 342 aa, PE 4, single sequence version); it is not an isoform or
fragment, and no reviewed canonical entry exists.

- GOA: still no rows for S0EDH7; existing_annotations remains empty.
- Deep research (falcon, cached): found no literature on FFUJ_06423; its discussion of
  TOR/MAPK kinases is generic context and was not used as evidence.
- New analysis in S0EDH7-bioinformatics/ (RESULTS.md, kinase_motif_analysis.py and outputs):
  - InterPro API: only IPR011009/SSF56112 (180-311) and Gene3D 1.10.510.10 (258-320);
    no Pfam, PROSITE or PANTHER assignment.
  - Local hmmscan vs 14 kinase-like Pfam HMMs: best is Pkinase PF00069, 29.5 bits
    (below GA 31.7), C-lobe only (HMM 43-143 -> residues 194-309); Kdo and APH weaker but
    on the same segment. N-lobe (glycine-rich loop, beta3 Lys) not aligned in S0EDH7 or 4
    homologs.
  - Catalytic loop WGDGKASN (D288, K290, N293) and DFG (D307) retained; WGDGK..N variant
    conserved across Fusarium, Verticillium, Sclerotinia, Cordyceps homologs.
  - BLAST: strong hits are all uncharacterized Pezizomycotina proteins (one HET-domain
    fusion in PTHR33112); Swiss-Prot hits are weak and scattered (PIM2_DANRE E=0.002,
    PKH1_YEAST E=0.007), so there is no characterized ortholog or PANTHER/PAINT placement
    from which to transfer function.
- Changes to the review: rewrote the description with the motif findings; kept
  GO:0016301 kinase activity as the core MF (protein kinase activity still not asserted);
  removed the supporting quote from the ProtNLM predictions review and replaced it with
  RESULTS.md quotes; added a BP/location knowledge gap; added reference_review for
  PMID:23825955 and the RESULTS.md reference; refreshed questions and experiments.
- Relative: none found (no PANTHER subfamily, no PAINT node, no characterized ortholog).
  No PANTHER family review or module applies.
