# rbcL (P00877, RBL_CHLRE) review notes

## Process log

- 2026-10-03: Gene data were already fetched (uniprot, goa, seeded review). GOA has
  only five IEA rows (GO_REF:0000120 / GO_REF:0000104), so there are no GOA PMIDs
  to cache (`fetch-gene-pmids` reported none).
- Deep research: ran `scripts/deep_research_wrapper.py CHLRE rbcL falcon --fallback
  perplexity-lite` once. Falcon returned HTTP 402 Payment Required. The
  perplexity-lite fallback failed with "Provider 'perplexity' not available". I
  did not retry, and there is no deep-research file. The review is based on
  UniProt plus primary literature cached in `publications/`.
- Cached the following PMIDs after checking them with PubMed esummary: 11641402,
  11866526, 6302265, 9536077, 18664299, 20424165. 6302265 (Dron 1982, rbcL
  sequence) has no abstract in the cache and is not cited in the review.

## Biology summary

- Chlamydomonas Rubisco is L8S8. The ~55 kDa large subunits are encoded by the
  chloroplast rbcL gene and the ~15 kDa small subunits by the nuclear rbcS family
  [PMID:18664299 "eight large subunits (~55 kDa, coded by the chloroplast rbcL
  gene) and eight small subunits (~15 kDa, coded by a family of nuclear rbcS
  genes)"].
- The large subunit contains the active site, and the small subunit modulates
  catalysis [PMID:20424165 "Although the large subunit contains the active site"].
- Crystal structures: 1.4 A structure with L8S8 architecture [PMID:11641402
  "Overall, the structure shows high similarity to the previously determined
  structures of L8S8 Rubisco enzymes."]. Activated enzyme with 2-CABP, where the
  large-subunit fold and active site are like spinach Rubisco [PMID:11866526
  "very similar to the activated spinach structure complexed with 2-CABP in the
  L-subunit folding and active-site conformation"]. PTMs: Hyp104/Hyp151 and
  S-methyl-Cys256/Cys369 [PMID:11866526].
- Mg2+ cofactor, one per subunit, and Lys-201 carbamylation (UniProt, from the
  crystal structures).
- Genetics: the rbcL deletion strain MX3312 (rbcL replaced by aadA) is the host
  for chloroplast transformation with mutant rbcL genes [PMID:18664299 "Mutant
  MX3312, which has the rbcL coding region replaced with the aadA gene conferring
  spectinomycin resistance"]. Rubisco-null mutants are acetate-requiring
  [PMID:18664299 "Mutants that lack Rubisco function can be maintained with
  acetate"].
- Localization: quantitative immunogold shows Rubisco in both the pyrenoid and the
  stroma, about 90% in the pyrenoid at ambient CO2 and about 40% at high CO2
  [PMID:9536077 "about 40% was in the pyrenoid when the cells were grown under
  elevated CO2 and about 90% with ambient CO2"]. Pyrenoidal Rubisco is active
  [PMID:9536077 "it is likely that pyrenoidal Rubisco is active in CO2
  fixation"].
- Pyrenoid packing is a property of the small subunit:
  - Plant small subunits on algal large subunits give catalytically proficient
    Rubisco but no pyrenoid [PMID:20424165 "It appears that small subunits contain
    the structural elements responsible for targeting Rubisco to the algal
    pyrenoid"].
  - Two surface alpha-helices of the SSU determine pyrenoid formation
    [PMID:23112177 "pyrenoid occurrence was shown to be conditioned by the amino
    acid composition of two surface-exposed α-helices of the SSU"].
  - EPYC1 binds the small subunit, unlike carboxysomal linkers, which bind
    between large subunits [PMID:33230314 "EPYC1 binds to the Rubisco small
    subunit"]. One tentative contact with large-subunit E433 is mentioned.
  - Condensed Rubisco remains active [PMID:30498228 "The phase-separated Rubisco
    is functional."].

## Curation decisions

- All five IEA rows are accepted: Mg2+ binding, chloroplast, carbon fixation,
  RuBP carboxylase activity, and reductive pentose-phosphate cycle.
- NEW annotations:
  - GO:0009573 chloroplast Rubisco complex (IDA, crystal structures).
  - GO:1990732 pyrenoid (IDA, immunolocalization, PMID:9536077).
  - GO:0009570 chloroplast stroma (IDA, same paper).
- No pyrenoid assembly or condensate scaffold term is given to rbcL. The large
  subunit is part of the condensed holoenzyme but does not mediate condensation,
  which depends on the SSU helices and EPYC1.
- Photorespiration is not added. The oxygenase reaction takes place at the
  large-subunit active site, so participation is plausible. A comparator check
  against plant RBCL annotations has not been done, so this is raised as a
  question rather than asserted.

## Module (pyrenoid_ccm) consistency

The rubisco_carboxylation annoton asserts complex GO:0009573, large-subunit
function GO:0016984, process GO:0019253 and location GO:1990732. The evidence
supports all four, and all four appear in core_functions. The annoton
correctly makes the small subunit, not the large subunit, the EPYC1-binding
part.
