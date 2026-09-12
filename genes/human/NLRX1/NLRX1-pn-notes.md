# NLRX1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q86UT6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-14
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/NLRX1/NLRX1-ai-review.yaml](NLRX1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/NLRX1/NLRX1-ai-review.html
- Gene notes: present - [genes/human/NLRX1/NLRX1-notes.md](NLRX1-notes.md)
- GOA TSV: present - [genes/human/NLRX1/NLRX1-goa.tsv](NLRX1-goa.tsv)
- UniProt record: present - [genes/human/NLRX1/NLRX1-uniprot.txt](NLRX1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/NLRX1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/NLRX1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NLRX1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NLRX1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: NLRX1 (NLR family member X1; also known as NOD5/NOD9 and CLR11.3) is an atypical nucleotide-binding-domain and leucine-rich-repeat-containing (NOD-like) receptor that, unusually for an NLR, localizes to the mitochondrion. An N-terminal mitochondrial transit peptide targets it to the mitochondrial outer membrane, it has a central NACHT NTPase domain, and a C-terminal leucine-rich-repeat region that carries an RNA-binding element; the protein assembles into a homohexamer. NLRX1 functions as a mitochondrial regulator at the intersection of antiviral innate immunity, autophagy, reactive oxygen species and inflammasome control. Its best-characterized role is as a negative regulator of MAVS-mediated (RIG-I-like helicase) antiviral signaling: by interacting with MAVS at the mitochondrial outer membrane it disrupts the virus-induced RIG-I-MAVS interaction and dampens type I interferon production, so that its depletion enhances antiviral interferon responses and reduces viral replication. NLRX1 also promotes autophagy by binding the mitochondrial elongation factor TUFM, which recruits the autophagy machinery (ATG5-ATG12, ATG16L1), linking it to autophagy/mitophagy and to modulation of type I interferon. It additionally restrains MAVS-dependent NLRP3 inflammasome activation, limiting IL-1beta/ IL-18 production and apoptosis, and it modulates reactive oxygen species production with downstream effects on NF-kappaB and JNK signaling. Through these activities NLRX1 acts as a mitochondrial checkpoint that tunes the strength of antiviral, inflammatory and autophagic responses.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 2; MARK_AS_OVER_ANNOTATED: 2

## PN Consistency Summary

- **Consistency:** Partial mismatch on the autophagy framing. Deep research and review converge on NLRX1 as a mitochondrial-outer-membrane regulator: core = negative regulation of MAVS/RIG-I antiviral signaling; secondary = TUFM-dependent PROMOTION of autophagy (recruits ATG5-ATG12/ATG16L1); plus NLRP3-inflammasome restraint and a DISPUTED NF-κB direction (UniProt: enhances via ROS; IBA: negative). The PN places NLRX1 specifically as a "Mitophagy" selective-autophagy RECEPTOR with a LIR motif (Listeria-induced mitophagy, Nat Immunol). The review's notes/YAML do NOT describe NLRX1 as a LIR-bearing mitophagy receptor — they describe TUFM-mediated general autophagy and never cite the Listeria-mitophagy paper. So the PN's mitophagy-receptor story is not reflected in the review.
- **PN story / NEW pressure:** PN projects GO:0000423 mitophagy as new_to_goa (verified real; confirmed ABSENT from NLRX1 GOA — GOA has no autophagy/mitophagy BP at all). The review independently proposes a NEW positive-regulation-of-autophagy term (GO:0010508) from the TUFM mechanism, but does NOT propose mitophagy. These are two different autophagy claims resting on different evidence: review = TUFM/general autophagy (PMID:22749352); PN = LIR-dependent Listeria mitophagy (PN-cited Nat Immunol paper not in the review). NEW autophagy pressure is real either way; the specific MITOPHAGY assertion needs the PN's mitophagy-receptor paper to be verified before adding.
- **Evidence alignment:** Divergent. PN refs = a selective-autophagy/LIR review + "Listeria hijacks host mitophagy" (Nat Immunol) — NEITHER is in the review's reference list. The review's autophagy evidence is PMID:22749352 (NLRX1-TUFM) + PMID:28611246 (TUFM/influenza), which the PN does not cite. This is the most salient divergence.
- **Verdict:** Consistent on antiviral core; the PN mitophagy-receptor story is NOT captured in the review and rests on a paper the review never assessed — verify before treating GO:0000423 as a settled ADD.

## Full Consistency Review

- **UniProt:** Q86UT6 (NOD5/NOD9) · **batch:** proteostasis-batch-2026-06-14 · **review status:** COMPLETE (thorough; mitochondrial NLR; MAVS/RIG-I, TUFM-autophagy, NF-κB direction disputed)
- **PN placement:** `Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy` ; **PN-node mapping:** type→mapped GO:0000423 mitophagy (ancestors no_mapping containers).
- **Consistency:** Partial mismatch on the autophagy framing. Deep research and review converge on NLRX1 as a mitochondrial-outer-membrane regulator: core = negative regulation of MAVS/RIG-I antiviral signaling; secondary = TUFM-dependent PROMOTION of autophagy (recruits ATG5-ATG12/ATG16L1); plus NLRP3-inflammasome restraint and a DISPUTED NF-κB direction (UniProt: enhances via ROS; IBA: negative). The PN places NLRX1 specifically as a "Mitophagy" selective-autophagy RECEPTOR with a LIR motif (Listeria-induced mitophagy, Nat Immunol). The review's notes/YAML do NOT describe NLRX1 as a LIR-bearing mitophagy receptor — they describe TUFM-mediated general autophagy and never cite the Listeria-mitophagy paper. So the PN's mitophagy-receptor story is not reflected in the review.
- **PN story / NEW pressure:** PN projects GO:0000423 mitophagy as new_to_goa (verified real; confirmed ABSENT from NLRX1 GOA — GOA has no autophagy/mitophagy BP at all). The review independently proposes a NEW positive-regulation-of-autophagy term (GO:0010508) from the TUFM mechanism, but does NOT propose mitophagy. These are two different autophagy claims resting on different evidence: review = TUFM/general autophagy (PMID:22749352); PN = LIR-dependent Listeria mitophagy (PN-cited Nat Immunol paper not in the review). NEW autophagy pressure is real either way; the specific MITOPHAGY assertion needs the PN's mitophagy-receptor paper to be verified before adding.
- **Mapping strategy:** The mitophagy leaf→GO:0000423 propagation is internally reasonable for a bona fide mitophagy receptor, but for NLRX1 it hinges on a single PN reference (Listeria mitophagy receptor) that the gene review did not adjudicate. Status `mapped` may over-reach for human NLRX1 if the LIR/mitophagy-receptor role is mouse/infection-specific; recommend confirming before propagating mitophagy as a universal NLRX1 GO assertion. The disputed-NF-κB issue is not in the PN mapping (PN is autophagy-only) so no conflict there.
- **Evidence alignment:** Divergent. PN refs = a selective-autophagy/LIR review + "Listeria hijacks host mitophagy" (Nat Immunol) — NEITHER is in the review's reference list. The review's autophagy evidence is PMID:22749352 (NLRX1-TUFM) + PMID:28611246 (TUFM/influenza), which the PN does not cite. This is the most salient divergence.
- **Verdict:** Consistent on antiviral core; the PN mitophagy-receptor story is NOT captured in the review and rests on a paper the review never assessed — verify before treating GO:0000423 as a settled ADD.
- **Recommended edits:** [REF/WB] obtain and assess the PN-cited "Listeria hijacks host mitophagy through a novel mitophagy receptor" (Nat Immunol) — it is absent from the review; it is the sole basis for the NLRX1 LIR/mitophagy-receptor claim and for GO:0000423. [YAML] if verified, add GO:0000423 mitophagy (and reconcile with the review's existing GO:0010508 proposed_new_term, which currently frames the autophagy role generically via TUFM rather than as mitophagy).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-14
- review_yaml: genes/human/NLRX1/NLRX1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagy substrate selection | Selective autophagy receptor | Mitophagy
- UniProt: Q86UT6
- In branches: ALP
- Notes: Receptor for selective autophagy. NLRX1 and its LIR motif were essential for L. monocytogenes–induced mitophagy.
- PN references (titles):
    - Selective Autophagy: ATG8 Family Proteins, LIR Motifs and Cargo Receptors - ScienceDirect
    - Listeria hijacks host mitophagy through a novel mitophagy receptor to evade killing | Nature Immunology
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000423 mitophagy]
        rationale: This PN path denotes selective-autophagy receptors for mitochondrial cargo. The source category is a mechanistic sub-role within mitophagy, so propagation rather than exact equivalence is the correct scope.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0000423 mitophagy | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Selective autophagy receptor|Mitophagy

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
