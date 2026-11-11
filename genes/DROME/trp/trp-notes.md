# trp review notes

## Session 1 (initial review)

- fetch-gene resolved P19334 (Swiss-Prot, FlyBase FBgn0003861, GeneID 43542); 62 GOA rows.
- Literature work done manually (no deep-research keys); see `trp-deep-research-manual.md`.
- Core picture: TRP is the pore-forming, Ca2+-selective subunit of the major
  light-activated cation channel of the rhabdomere [PMID:17234592 "provide the first
  rigorous demonstration that a TRP protein is a pore-forming subunit in any native
  system"], effector of PLC-mediated phototransduction, and the membrane anchor of the
  INAD signalplex [PMID:16301334 "serves dual roles as a cation channel and as a
  molecular anchor for the PDZ protein, INAD"].
- Homomultimer in vivo [PMID:23687378 "TRP and TRPL assemble exclusively as
  homomultimeric channels in their native environment"]; the heterodimerization row
  (PMID:9215637, in vitro) is therefore over-annotated, not removed.
- Store-operated channel IBA: in vitro only (PMID:9215637); rhabdomere gating is
  store-independent (PMID:22952921 discussion). Axonal store-operated entry is
  suggestive. Marked over-annotated.
- IP3 binding IBA: no evidence for TRP; marked over-annotated.
- Olfactory learning row (UniProt 2005) cites PMID:10995445, whose full text never
  mentions olfaction. UniProt FUNCTION cites PMID:10366618 for olfactory adaptation
  [PMID:10366618 "defective in olfactory adaptation"]. Recorded as WRONG_REFERENCE
  source defect; adaptation is not learning.
- Mitochondrion organization / retina homeostasis (PMID:27054334): consequences of
  Ca2+ overload in the gain-of-function TrpP365 allele [PMID:27054334 "primarily
  resulted from the disruption of mitochondrial function caused by calcium overload"],
  not TRP activity; over-annotated.
- Rhabdomere IMP row (PMID:28314815, abstract only): location row with IMP code; kept
  (location is well established) but flagged evidence code upstream as suspected.
- PMID:22952921 (full text): TRP in photoreceptor axon terminals in lamina by
  immunohistochemistry; proposed NEW axon location (IDA). The exocytosis requirement
  is mutant-phenotype evidence; no NEW process term proposed.
- No GO-CAM model contains trp (gocams/index.tsv).
