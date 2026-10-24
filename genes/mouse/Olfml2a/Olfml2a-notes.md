# Olfml2a (mouse, Q8BHP7) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

### Context
- Reviewed as the experimentally characterised SF29 ortholog (reference donor) for HORSE/OLFML2A and human OLFML2A (Q68BL7). No ProtNLM2 file or prediction-evidence folder was consulted.

### Deep research
- `just deep-research-falcon mouse Olfml2a --fallback perplexity-lite` failed: falcon "Failed to authenticate"; perplexity-lite fallback returned HTTP 401 insufficient_quota. No deep-research file was produced. Review is based on the cached primary literature, the UniProt record and the PANTHER/PAINT data.
- Full text: PMC1180717 (PMID:15836428) and PMC2529034 (PMID:18757743) are not downloadable as XML from PMC (publisher restriction); both cached abstract-only. A web search found no further functional study (a commercial Cas9 knockout strain exists, unpublished phenotype).

### Identity / evolutionary grounding
- UniProt: PANTHER PTHR23192:SF29 (OLFACTOMEDIN-LIKE PROTEIN 2A) ["DR   PANTHER; PTHR23192:SF29; OLFACTOMEDIN-LIKE PROTEIN 2A; 1."]; same subfamily as human Q68BL7. Paralog Olfml2b (photomedin-2) is a separate subfamily member of the OLFML2 clade.
- PAINT root node PTN000573635 carries extracellular region (Olfml2a MGI:2444741 is itself a donor — expected, not circular) and signal transduction (donors myocilin Q99972, MGI:1202864, MGI:1860437; none in the OLFML2 subfamily).
- PAINT did not propagate ECM binding or ECM organization from Olfml2a; the PTHR23192 family review rates ECM organization UNRESOLVED.

### Experimental evidence in mouse
- Secreted disulfide-bonded dimer, O-glycosylated, cleaved mid-molecule after secretion [PMID:15836428 "were secreted as disulphide-bonded dimers (photomedin-1) or oligomers/multimers (photomedin-2) with O-linked carbohydrate chains, although photomedin-1 was proteolytically processed in the middle of the molecule after secretion"].
- Retina: photoreceptor outer segment [PMID:15836428 "In the retina, photomedin-1 was selectively expressed in the outer segment of photoreceptor cells"].
- GAG binding [PMID:15836428 "photomedins preferentially bound to chondroitin sulphate-E and heparin"]; UniProt attributes this to Olfml2a with ECO:0000269.
- ECM screen [PMID:18757743 "These assays screened the candidate proteins for ECM-assembling activities"] — Olfml2a-specific result not visible in abstract.
- Podocyte major processes [PMID:22913984 "These proteins were expressed exclusively by podocytes, wherein they localized to major processes"] (species for this localization not stated in abstract).

### Decisions
- Extracellular region IBA + IEA: ACCEPT. ECM IDA x2: ACCEPT.
- ECM binding IDA: ACCEPT; NEW chondroitin sulfate binding (GO:0035374) and heparin binding (GO:0008201) by IDA from PMID:15836428 (OLS: neither is an is_a descendant of GO:0050840; both under glycosaminoglycan binding).
- Identical protein binding IPI: MODIFY -> protein homodimerization activity GO:0042803 (OLS: is_a descendant of GO:0042802).
- Signal transduction IBA: UNDECIDED (root-node inference, no subfamily support), consistent with human review.
- ECM organization IDA (acts_upstream_of_or_within): UNDECIDED — cannot see the full-text result; not removed, deferring to the curator; not used for transfer.
- For transfer: experimentally established in mouse = secretion/extracellular region, ECM localization, homodimerization, chondroitin sulfate E and heparin binding. Not established = signaling, ECM organization.
