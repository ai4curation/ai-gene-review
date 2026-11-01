# AFB2 (At3g26810; Q9LW29) curation notes

## 2026-10 review (auxin_nuclear_signaling module)

- Automated deep research (`just deep-research-falcon ARATH AFB2`) failed with HTTP 402 (Payment Required); review written from cached primary literature.
- Identity check: UniProt Q9LW29 AFB2_ARATH, AUXIN SIGNALING F-BOX 2, At3g26810. Correct protein.

### Function
- TIR1/AFB family LRR F-box auxin receptor. AFB1-3 "interact with the Aux/IAA proteins in an auxin-dependent manner" and quadruple mutants are auxin insensitive with mp/bdl-like embryos [PMID:15992545 "Like TIR1, these proteins interact with the Aux/IAA proteins in an auxin-dependent manner"].
- "TIR1 and AFB2 are the dominant auxin receptors in the seedling root" [PMID:20018756].
- Co-receptor: "TIR1 and the Aux/IAA are both necessary and sufficient for auxin binding and act as auxin co-receptors"; AFB2 forms strong Aux/IAA complexes, e.g. "IAA12 interacted specifically with TIR1 and AFB2 at 100 μM IAA" [PMID:22466420].
- Structure (TIR1): InsP6 cofactor; auxin acts as "molecular glue" [PMID:17410169] -> basis for ISS InsP6 binding / auxin binding.
- Localization: "AFB2 through AFB5 are distributed between the nucleus and the cytoplasm" [PMID:32067636]; TIR1 mostly nuclear.
- Redundancy: "functional redundancies between TIR1, AFB2, and AFB3" [PMID:32067636].

### Decisions
- Protein binding (IAA7) IPIs -> MODIFY to GO:1990756 ubiquitin-like ligase-substrate adaptor activity.
- Plant-type vacuole (HDA, vacuole proteomics PMID:17151019) -> MARK_AS_OVER_ANNOTATED.
- InsP6 binding ISS -> KEEP_AS_NON_CORE (structural cofactor).
- Core: auxin receptor activity (GO:0038198) and ligase-substrate adaptor (GO:1990756) in SCF (GO:0019005), auxin-activated signaling (GO:0009734).


## Auxin receptor audit, 2026-10-26

Every original annotation row was assessed; source/evidence/qualifier/term payloads are preserved against `.cache/module-audit-logs/auxin-panel-baseline.json`. No assigned target has a negated original row. Current Falcon requests failed authentication, and the Perplexity-lite fallback returned 401 insufficient quota (logs in `.cache/module-audit-logs/auxin-fetch/`). No provider report was fabricated. Manual research used primary publications and curated sequence/family records; previous valid reports remain discovery aids.

Actual PANTHER IBD assertions were inspected in `interpro/panther/PTHR16134/PTHR16134-paint.tsv`: PTN008357904 supplies Embryophyta auxin-receptor/signaling assertions; PTN009029653 supplies older F-box SCF/adaptor/proteolysis assertions. The latter's mixed donor taxa do not transfer auxin specificity. A target in its own descendant evidence is expected, not circular support. The broad official family label is F-BOX/TPR REPEAT PROTEIN POF3; its name does not restrict the verified receptor subfamilies to Pof3-like physiology.

A separate annotation-reviewer consultation agreed that integral cofactor binding is core, that SCF substrate recruitment differs from independent ubiquitin-transfer catalysis, that nuclear imaging does not exclude vacuolar residence, and that AC activity must distinguish assayed receptor/construct from family inference.

AFB2 Q9LW29 is verified in PTHR16134:SF132 (PROTEIN AUXIN SIGNALING F-BOX 2). Native primary evidence remains strong: PMID15992545 establishes auxin-dependent Aux/IAA interactions; refreshed full PMID20018756 identifies TIR1 and AFB2 as dominant seedling-root receptors; PMID22466420 directly includes AFB2 in partner-selective interaction assays. The TIR1/IAA7 radioligand KD in the latter paper is not an AFB2-specific affinity measurement. InsP6 binding remains explicitly comparative ISS from the TIR1 structure, now ACCEPT as an integral inferred cofactor property. Generic protein binding remains refined to the demonstrated substrate-adaptor role; broad auxin response becomes the supported signaling process.

This section supersedes the earlier MARK_AS_OVER_ANNOTATED vacuole and KEEP_AS_NON_CORE InsP6 conclusions above. The HDA PMID17151019 vacuole assignment is now UNDECIDED, not rejected. The original purification had organelle contamination controls, and nuclear/cytoplasmic localization neither excludes a vacuolar pool nor requires a vacuolar signaling function. The main text does not expose the AFB2 peptide identification. The original supplemental URL `https://www.mcponline.org/cgi/content/full/M600250-MCP200/DC1` returned HTTP403; PMC/EuropePMC attempts did not recover the target table (challenge/error pages). SUBA confirms that this is a curated target-specific localization claim but is not independent primary evidence. No generic contamination explanation substitutes for inspecting that table. Full PMID32067636 states “AFB2 through AFB5 are distributed between the nucleus and the cytoplasm,” in root epidermal cells; retain both positive locations.

No NEW AC activity: complete author manuscript of PMID36289340 says “Due to lack of detectable protein, the AC activity of the other 4 TIR1/AFBs could not be assessed.” In that screen only AFB1/AFB5 expressed detectably; TIR1 was assayed separately from Sf9, but AFB2 was not. AFB2 motif conservation supplies a testable hypothesis, not a negative result and not a direct catalytic measurement. Citation scope is documented rather than copying the family-wide abstract wording into a target-specific assertion.
