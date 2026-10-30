# ybbO (STM0505, Q7CR11) — Salmonella Typhimurium LT2 — curation notes

## 2026-10-30 session

- Deep research: `just deep-research-falcon SALTY ybbO --fallback perplexity-lite` failed
  (neither falcon nor perplexity providers are configured in this environment). Literature
  search was done manually (PubMed eutils, QuickGO).
- No Salmonella-specific literature on STM0505 was found. All functional evidence comes
  from the E. coli orthologue YbbO (P0AFP4), 90.6% identical
  (file:SALTY/ybbO/ybbO-bioinformatics/RESULTS.md).
- E. coli YbbO evidence:
  - [PMID:25108218 "YbbO showed broad substrate activity toward all the C2–C10 aldehydes
    with the highest activity toward hexanal and octanal"]; NADPH-dependent, about 10-fold
    lower activity than DkgA and YahK.
  - [PMID:27134112 "deletion of ybbO gene, which encodes NADP(+) dependent aldehyde
    reductase, led to >90% reduction in long chain fatty alcohol production"] and
    "YbbO has wide substrate specificity ranging from C6 to C18 aldehyde".
  - EcoCyc annotates P0AFP4 with GO:0008106 alcohol dehydrogenase (NADP+) activity (IDA)
    from both papers.
- Both studies are metabolic-engineering screens with non-physiological aldehyde loads;
  the natural substrate and physiological role (detoxification of endogenous aldehydes?)
  are unknown.
- PANTHER: PTHR43313 (SDR family 9C), subfamily SF1. The IBA node PTN000672121 is seeded
  by the vertebrate 17beta-HSD / retinol dehydrogenase SDR9C members plus E. coli YbbO, so
  the shared claim is only generic oxidoreductase activity; substrate specificity differs
  across the clade.
- Fitness data could not be fetched (no FEBA source reachable).

## Decision

- GO:0016491 oxidoreductase activity (IBA): correct but general; MODIFY to GO:0008106
  alcohol dehydrogenase (NADP+) activity, supported by orthology to E. coli YbbO.

## OpenScientist sequence-only test (2026-10-30)

Run: `ybbO-hypotheses/seq-only-blinded-activity/` (OpenScientist, 3 iterations, 24.5 min).
Prompt withheld the gene symbol, accession and the local bioinformatics results; it gave
only the sequence, organism and the hypothesis (GO:0008106, with hydroxysteroid and
retinol dehydrogenase as named alternatives).

- **Blinding was broken.** The run computed the UniProt CRC64 checksum, found the exact
  UniParc match (UPI000005A1DF → Q7CR11, ybbO) and then used the E. coli YbbO
  literature. Withholding the name is not enough to blind a sequence; a real
  sequence-only test would need a perturbed sequence or a rule against database
  lookups.
- **Agreement with the local analysis:** classical SDR; 90.6% identity to P0AFP4;
  catalytic machinery intact; GO:0008106 supported by ISS/ISO from P0AFP4; IBA
  GO:0016491 correct but less specific.
- **Disagreement on a residue:** it calls Asn81 (the NNAG Asn) the catalytic Asn. In
  classical SDRs the tetrad Asn is on helix alpha-E (Asn111 in 3alpha/20beta-HSD), which is
  N105 here; NNAG is structural. I made the same mistake on my first pass.
- **New lead:** an R34/K35 basic pair after beta2 as the NADP 2'-phosphate determinant.
  The run itself says the motif evidence is ambiguous because Asp residues follow it.
  NADPH dependence rests on the E. coli assay, not the motif.
- **Retinal:** it judges retinal reduction promiscuous and non-core, citing
  [PMID:34850377 "Expression of human RDH10 and Escherichia coli ybbO led to increase in
  retinol production, but retinal remained as a major product"]. As a result I withdrew the
  NEW GO:0052650 proposal from the E. coli review (see the ECOLI notes).
- It did not do a reciprocal-best-hit, synteny or pocket analysis, so those local results
  have no counterpart in the run.
