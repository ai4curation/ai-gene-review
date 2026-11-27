# PPOX (P50336) review notes

Human protoporphyrinogen oxidase (EC 1.3.3.4), seventh step of heme biosynthesis.

Deep research: no `-deep-research-*.md` provider output exists for this gene and none was
generated in this pass; the review is grounded in the UniProt record, cached abstracts/full
texts and Reactome. (Claude (AI-assisted), 2026-11-10)

## Core biology (with provenance)

- Activity: "Protoporphyrinogen oxidase (PPO; EC 1.3.3.4) is the enzyme that catalyzes in the
  penultimate step in the heme biosynthetic pathway." [PMID:7713909]; transfected COS-1 cells
  "had much higher PPO activity than an extract of control cells, and this activity was inhibited
  by acifluorfen, a specific inhibitor of PPO" [PMID:7713909].
- Location: "Human protoporphyrinogen IX oxidase (hPPO), a mitochondrial inner membrane protein,
  converts protoporphyrinogen IX to protoporphyrin IX in the heme biosynthetic pathway."
  [PMID:21048046]; Reactome R-HSA-189423: "The protein resides on the outer surface of the inner
  mitochondrial membrane."
- Cofactor: UniProt COFACTOR "Binds 1 FAD per subunit." (PubMed:21048046).

## Completion pass decisions

- Supported_by quotes completed on every row; PANTHER PTHR42923 cited for the IBA rows.
- porphyrin-containing compound biosynthetic process (IEA, IDA) -> MODIFY to heme biosynthetic
  process; oxidoreductase activity -> MODIFY to GO:0004729; mitochondrial membrane (IEA, IMP)
  -> MODIFY to mitochondrial inner membrane (these were MARK_AS_OVER_ANNOTATED or ACCEPT with
  reasons that argued "correct but general").
- mitochondrial intermembrane space (ARBA IEA, Reactome TAS) kept MARK_AS_OVER_ANNOTATED: the
  protein is inner-membrane peripheral, facing the intermembrane space.
- response to xenobiotic stimulus (Compara) kept non-core: acifluorfen inhibition is direct.
