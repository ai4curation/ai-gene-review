# MYC3 (At5g46760; UniProt Q9FIP9) curation notes

## 2026-10-06 — initial review (jasmonate_coi1_jaz_signaling module)

- Fetched with `just fetch-gene ARATH MYC3`; UniProt record checked: MYC3_ARATH, Q9FIP9, At5g46760 (bHLH005, ATR2).
- `just deep-research-falcon ARATH MYC3` failed (HTTP 402); review based on cached publications.

### Key evidence
- JAZ target, nuclear, G-box binding like MYC2, acts additively with MYC2 [PMID:21335373 "Our results show that MYC3 and MYC4 are activators of JA-regulated programs that act additively with MYC2 to regulate specifically different subsets of the JA-dependent transcriptional response."].
- Nearly identical DNA specificity to MYC2 [PMID:21335373 "These results indicate that MYC2 and MYC3 have almost identical DNA binding specificities"].
- Transactivates JAZ promoters [PMID:21321051 "MYC2, MYC3, and MYC4 were all capable of inducing expression of JAZ::GUS reporter constructs following transfection of carrot protoplasts."].
- Structure: JAZ9 Jas helix binds MYC3 N-terminus and blocks MED25 [PMID:26258305 "In this position, the Jas helix competitively inhibits MYC3 interaction with the MED25 subunit of the transcriptional Mediator complex."].
- Represses FT in photoperiodic flowering [PMID:31178399, abstract only].

### Decisions
- Protein binding rows resolved by partner (supporting_entities): JAZ partners -> MODIFY to GO:0001222 transcription corepressor binding; MED25 -> MODIFY to GO:0001223 transcription coactivator binding; FT-paper row (AT1G65480) -> REMOVE (uninformative; repo policy disallows MARK_AS_OVER_ANNOTATED for protein binding).
- response to jasmonic acid -> MODIFY to GO:0009867 for consistency with MYC2 review.
