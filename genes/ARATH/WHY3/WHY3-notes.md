# WHY3 review notes

## 2026-10-28 initial review

- fetch-gene resolved Q66GR6 (TAIR AT2G02740, GeneID 814803), 28 GOA rows.
- Literature compiled manually in WHY3-deep-research-manual.md (no deep-research API keys).
- Core view: plastid (and in vitro also mitochondrial) ssDNA-binding Whirly tetramer that,
  redundantly with WHY1, protects plastid DNA against microhomology-mediated illegitimate
  recombination during DSB repair [PMID:19666500 "We suggest that AtWhy1 and AtWhy3 function as
  antirecombination proteins, contributing to safeguard plastid genome integrity."].
- All in vivo genetic evidence uses the why1 why3 double mutant; single why3 KO has milder
  increase in illegitimate recombination [PMID:19666500].
- Decisions:
  - DNA binding rows -> MODIFY to single-stranded DNA binding (EMSA of KO1 extracts, which
    contain only WHY3, still bind ssDNA).
  - DNA repair rows -> MODIFY to double-strand break repair (ciprofloxacin/bleomycin DSB-inducing
    treatments, MMBIR model) [PMID:20551348].
  - Defense response (IEA, TAS) -> over-annotated; defense role established for AtWHY1/StWHY1.
  - SA-mediated signaling IDA -> over-annotated; abstract supports only SA induction of the
    transcript. Suspected wrong term recorded as source defect (CHECK).
  - NOT nucleus -> UNDECIDED; GFP negative but ChIP implies a nuclear pool.
  - Mitochondrion: supported by in organello import [PMID:32490348]; non-core.
- Considered NEW "negative regulation of DNA recombination" (GO:0045910); not added because
  evidence is mutant-phenotype based; raised as a question instead.
