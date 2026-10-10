# Ar1 (M9PF61) notes

- Ar1 = Akr1B = CG6084, AKR1B-family aldose reductase.
- Polyol pathway glucose -> sorbitol -> fructose supports Mondo glucose sensing; AR double mutants (CG6084 + CG10638)
  reduce hemolymph sorbitol [PMID:35687590 "Levels of sorbitol in the hemolymph were reduced in AR mutants and were increased in Sodh mutants"].
- Hemocyte AR makes sugar alcohol alarmins for gut-fat body immune communication
  [PMID:31350199 "Aldose reductase (AR) in hemocytes, the rate-limiting enzyme of the polyol pathway, is necessary and sufficient for the increase of plasma sugar alcohols."].
- Akr1B is the PGF2alpha synthase needed in border cells [PMID:38283991 "the PGF2α synthase Akr1B is required in the border cells for on-time migration"];
  cytoplasmic in follicle cells.
- Decisions: aldose reductase, sorbitol biosynthesis, fructose biosynthesis (polyol pathway), cytosol core; broad AKR
  activities (allyl/aryl alcohol, glycerol, retinol dehydrogenase, PGH2 reductase) non-core; AKR1A1-derived
  glucuronate terms and retinol metabolic process marked over-annotated; IDA extracellular region UNDECIDED.

- Falcon deep research (Ar1-deep-research-falcon.md) is consistent; it explains the IDA extracellular region row (Yang et al.
  describe AR as secreted and detect reductase activity in hemolymph) but notes secretion of intact Ar1 is not demonstrated,
  so the row stays UNDECIDED. It also mentions preprint-level evidence for a glial role.
- PR #4484 review: GO:0046173 polyol biosynthetic process (IMP) changed from MODIFY (to sorbitol biosynthesis) to ACCEPT, because the cited experiment measured both sorbitol and galactitol; PGF2alpha-synthase MF and BP rows now share one rationale (secondary, non-core).
