# MPK3 (Arabidopsis thaliana, Q39023, At3g45640) - curation notes

## 2026-10-02 - initial review

Sources: UniProt Q39023, MPK3-deep-research-falcon.md, cached publications (all 32 GOA PMIDs cached; many abstract-only), plus newly cached PMID:17259259 (stomata) and PMID:21498677 (WRKY33). Paralog review genes/ARATH/MPK6 used for consistency.

### Molecular function
- Proline-directed Ser/Thr MAPK; peptide library gives consensus L/P-P/X-S-P-R/K [PMID:22631074 "a preference towards the sequence L/P-P/X-S-P-R/K for both kinases"].
- Activated by H2O2 via ANP1 [PMID:10717008 "a phosphorylation cascade involving two stress MAPKs, AtMPK3 and AtMPK6"], ozone with nuclear translocation [PMID:15500467 "activated AtMPK3 and AtMPK6 are translocated to the nucleus during the early stages of O3 treatment"], osmotic stress [PMID:12220631].

### Immunity (project-relevant)
- FLS2 cascade [PMID:11875555 "a complete plant MAP kinase cascade (MEKK1, MKK4/MKK5 and MPK3/MPK6)"].
- Chitin: downstream of CERK1-PBL27 [PMID:24750441 "Knockout of PBL27 resulted in the suppression of several chitin-induced defense responses, including the activation of MPK3/6"].
- Camalexin: cascade regulates biosynthetic gene transcription, not the chemistry [PMID:18378893 "the MPK3/MPK6 cascade regulates camalexin synthesis through transcriptional regulation of the biosynthetic genes after pathogen infection"]; via WRKY33 [PMID:21498677 "WRKY33 is phosphorylated by MPK3/MPK6 in vivo in response to Botrytis cinerea infection"].
- ACS2/ACS6: direct phosphorylation by MPK3 is less secure than by MPK6 (deep research flags early biochemistry identifying MPK6 not MPK3 as direct ACS6 kinase); left as a suggested question.

### Development
- Stomata [PMID:17259259 "Loss of function of MKK4/MKK5 or MPK3/MPK6 ... resulting in the formation of clustered stomata"]; no stomatal term in GOA for MPK3 - raised as question, not added.
- Inflorescence [PMID:23263767], ovule [PMID:18364464], pollen tube funicular guidance [PMID:24717717], stigma receptivity with MPK4 [PMID:32890733].
- PMID:24717717 explicitly says "mpk3 mpk6 pollen has no developmental defect" -> pollen development IGI marked over-annotated.

### Decisions
- Camalexin biosynthetic process (IMP) -> MODIFY to GO:1901183 positive regulation of camalexin biosynthetic process (necessity vs participation; project question 3).
- MKP2 protein binding -> MODIFY to phosphatase binding (consistent with MPK6). All other protein binding rows REMOVE.
- GO:0002221 pattern recognition receptor signaling pathway was considered as NEW but dropped: same-role comparators (MPK6, MKK4, MKK5) lack it, and BIK1 is a receptor-proximal RLCK, not a same-role comparator. Raised as a suggested question.
- Stress-response and developmental rows KEEP_AS_NON_CORE.
- Stress granule IDA (PMID:30664249) - MPK3 not named in abstract; deferred to curator (KEEP_AS_NON_CORE), consistent with TZF1 recruitment reported in deep research.
