# Ldhb notes

- UniProtKB:P42123 states: FUNCTION: Interconverts simultaneously and stereospecifically pyruvate and lactate with concomitant interconversion of NADH and NAD(+). [UniProtKB:P42123].
- Core interpretation: NAD-dependent interconversion of lactate and pyruvate.
- Accepted direct GO terms include: L-lactate dehydrogenase (NAD+) activity, lactate dehydrogenase activity, lactate metabolic process, pyruvate catabolic process.
- Non-core/context terms are mostly localization, binding/cofactor, inferred pathway context, or exposure-response annotations; generic parent terms are modified when a specific catalytic term is available.

## Re-review 2026-10-10

- GOA refresh added four rows: GO:0004459 L-lactate dehydrogenase (NAD+) activity ISO and GO:0005829 cytosol ISO (both donor-splits from human LDHB, UniProtKB:P07195), GO:1990204 oxidoreductase complex ISO (human LDHB), and GO:0019244 pyruvate fermentation to lactate IBA (PTN000166277; donors mouse Ldha MGI:96759, mouse Ldhc MGI:96764, Drosophila Ldh). Actions: ACCEPT, KEEP_AS_NON_CORE, KEEP_AS_NON_CORE, ACCEPT [UniProtKB:P42123 "PATHWAY: Fermentation; pyruvate fermentation to lactate; (S)-lactate"].
- Retired by GOA (kept): GO:0042867 pyruvate catabolic process IBA, GO:0006089 lactate metabolic process IBA, GO:0005515 protein binding IPI PMID:7138505.
- GO:0005515 protein binding (IPI, PMID:7138505, retired): MARK_AS_OVER_ANNOTATED -> REMOVE per the protein-binding policy. The abstract-only source is an isoenzyme purification/radioimmunoassay paper [PMID:7138505 "We have developed procedures for purifying lactate dehydrogenase isoenzymes from rat tissues"]; subunit self-association is already captured by GO:0042802 IDA from the same paper, so no replacement term.
- Deleted the NEW GO:0005777 peroxisome (ISS, PMID:25247702) row. The readthrough-generated LDHBx peroxisomal pool is real [PMID:25247702 "at least 1.6% of the total cellular LDHB is targeted to the peroxisome by a conserved hidden PTS1"], but the comparator check shows neither human LDHB (P07195), mouse Ldhb (P16125) nor human MDH1 (P40925, the other well-known readthrough-peroxisome case) carries a peroxisome annotation in GOA, and the ISS has no annotated source. Per the NEW-term policy this is kept as the existing suggested question on LDHBx in rat rather than asserted as an annotation.
- Added a UniProt FUNCTION quote as positive support to the four rows citing PMID:17447164 (abstract-only, does not mention LDH); actions unchanged (ACCEPT/KEEP_AS_NON_CORE deferring to the curator).
- Description rewritten as standalone biology. UniProt quotes verified (0 stale; this entry still has DR GO lines).
- Open question: should GO capture readthrough-isoform peroxisomal localization (LDHBx, MDH1x) at all, and on which gene product?
