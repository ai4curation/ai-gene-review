# Cyb5r3 notes

- UniProtKB:P20070 states: FUNCTION: Catalyzes the reduction of two molecules of cytochrome b5 using NADH as the electron donor. [UniProtKB:P20070].
- Core interpretation: NADH-dependent reduction of cytochrome b5.
- Accepted direct GO terms include: cytochrome-b5 reductase activity, acting on NAD(P)H, cytochrome-b5 reductase activity, acting on NADH.
- Non-core/context terms are mostly localization, binding/cofactor, inferred pathway context, or exposure-response annotations; generic parent terms are modified when a specific catalytic term is available.

## Re-review 2026-10-10

- GOA refresh added 8 ISO rows (GO_REF:0000121), all donor-splits of terms already reviewed: GO:0004128 and GO:0090524 cytochrome-b5 reductase activities from pig CYB5R3 (RGD:14151460; RGD species key 9) and human CYB5R3 (UniProtKB:P00387) -> ACCEPT; GO:0071949 FAD binding from pig, human, and human plus soluble isoform P00387-2 -> KEEP_AS_NON_CORE; GO:0005789 ER membrane (located_in) from human -> KEEP_AS_NON_CORE. Existing dog-donor rows use RGD:12254858 (RGD species key 6). Support: [UniProtKB:P20070 "Catalyzes the reduction of two molecules of cytochrome b5 using NADH as the electron donor."], [UniProtKB:P20070 "COFACTOR: Name=FAD;"], [UniProtKB:P20070 "[Isoform 1]: Endoplasmic reticulum membrane"].
- Retired by GOA: GO:0004128 IEA (GO_REF:0000117, ARBA). Review kept with a retirement note.
- No existing actions changed. AMP/ADP binding (IDA, PMID:14609324) stay MARK_AS_OVER_ANNOTATED: the paper shows the FAD prosthetic group's own ADP moiety displaced into the NADH site in a mutant [PMID:14609324 "the adenosine diphosphate (ADP) moiety of the FAD prosthetic group is displaced into the corresponding ADP binding site of the physiological substrate, NADH"], not binding of free nucleotides.
- Description rewritten as standalone biology (isoforms, ER/mitochondrial outer membrane anchoring, erythroid soluble form). UniProt quotes verified (0 stale).
