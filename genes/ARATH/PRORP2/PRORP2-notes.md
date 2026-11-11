# PRORP2 (At2g16650, Q680B9) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: PRORP2 is the closest experimentally characterised relative of the tobacco
protein A0A1S3Y076 (same PANTHER subfamily PTHR13547:SF13). This review covers PRORP2 in
its own right. ProtNLM2 output was not consulted.

### Provenance / process
- `just fetch-gene ARATH PRORP2`: the first run timed out on an EBI call; the re-run created the stub (15 GOA rows).
- Deep research failed. `just deep-research-falcon ARATH PRORP2 --fallback perplexity-lite`
  stopped with falcon "Exception: Failed to authenticate" (Edison auth) and perplexity
  HTTP 401 (quota exceeded). There is no deep-research file, so the review rests on
  primary literature I read directly.
- Literature: a PubMed search (`PRORP2 AND (Arabidopsis OR plant)`) found the papers below.
  I re-fetched PMID:22549728 with force=True, which gave the full text from PMC (previously
  abstract-only). Newly cached: 37945696 (abstract only), 28874505, 28696260, 28499021,
  30414965, 35022261, 26527263. PMID:38453211 (2024 review) returned HTTP 429 and was not cached.

### Evolutionary grounding
- PANTHER: Q680B9 is in PTHR13547:SF13 "PROTEINACEOUS RNASE P 2"
  (`interpro/panther/PTHR13547/PTHR13547-entries.csv`). PRORP3 (F4JKB6) is in SF20;
  PRORP1 (Q66GI4) and human PRORP (O15091) are in SF1.
- PAINT (`interpro/panther/PTHR13547/PTHR13547-paint.tsv`): node PTN001005190
  (taxon:2759) has IBD GO:0004526 ribonuclease P activity, seeded by AT2G16650, AT2G32230,
  AT4G21900, FBgn0029858, O15091, Q386L0 and Q38E68. It also has IBD GO:0001682 tRNA
  5'-leader removal, seeded by the three Arabidopsis PRORPs. PAINT did not propagate
  nucleus, mRNA processing or snoRNA processing; I treat these omissions as deliberate.

### Experimentally established for PRORP2 itself (Arabidopsis)
- RNase P activity in vitro on nuclear pre-tRNA(Asp)/(Gln), with cleavage at +1;
  D-to-A catalytic mutants are inactive [PMID:22549728 "In the presence of PRORP2 or of
  PRORP3, the tRNA leader sequences were clipped off"].
- Catalysis is Mg2+/Mn2+-dependent; Ca2+ and Zn2+ do not support it. Crystal structure
  at 3.2 Å; monomer in solution [PMID:26655022 "Our biochemical studies indicate that
  PRORP2 requires Mg(2+) for catalysis"].
- Nuclear localisation by YFP fusion and immunodetection [PMID:20473316 "PRORP2 and
  PRORP3, two paralogs of PRORP1, are both localized in the nucleus"].
- Redundant with PRORP3; the double mutant is lethal [PMID:22549728 "This result shows
  that PRORP2 and PRORP3 have redundant functions in the nucleus and that this function
  is essential."].
- PRORP2/3 VIGS: nuclear tRNAs fall and organellar tRNAs are unaffected; snoR43 falls
  and the tRNA(Gly)-snoR43 precursor accumulates [PMID:22549728].
- In vivo complex with TRM1A/TRM1B [PMID:37945696 "PRORP2 occurs in a complex with the
  tRNA methyl transferases TRM1A and TRM1B in vivo"]. Not annotated, because no
  informative MF term fits.
- E. coli complementation works but depends on growth conditions [PMID:28499021].

### Key curation calls
- mRNA processing (IMP, PMID:22549728, and ARBA IEA): MARK_AS_OVER_ANNOTATED. The paper's
  in vivo mRNA evidence (nad6) is from PRORP1 VIGS plants: "snoRNA and mRNA in the
  nucleus and mitochondria, respectively". I recorded a PROBABLE WRONG_GENE_PRODUCT
  source defect for TAIR with requested_change CHECK, because the supplement was not seen.
- chloroplast (ISM, AtSubP): REMOVE. Experiments show PRORP2 is nuclear only.
- snoRNA processing: KEEP_AS_NON_CORE. It extends the RNase P cleavage to a dicistronic
  precursor.
- No NEW terms proposed.

### Notes for transfer to the tobacco SF13 member
- Safe to transfer, given the eukaryote-wide PAINT node plus SF13 membership: ribonuclease P
  activity and tRNA 5'-leader removal.
- Nucleus is experimentally established for PRORP2 and PRORP3. Before transferring it,
  check the tobacco protein for any organellar targeting signal.
- Do not transfer: mRNA processing (PRORP1-specific evidence). Transfer snoRNA processing
  only with caution, because it depends on Arabidopsis-specific tRNA-snoRNA dicistronic genes.
