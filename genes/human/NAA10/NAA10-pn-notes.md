# NAA10 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P41227
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/NAA10/NAA10-ai-review.yaml](NAA10-ai-review.yaml)
- AIGR review HTML: present - [genes/human/NAA10/NAA10-ai-review.html](NAA10-ai-review.html)
- Gene notes: present - [genes/human/NAA10/NAA10-notes.md](NAA10-notes.md)
- GOA TSV: present - [genes/human/NAA10/NAA10-goa.tsv](NAA10-goa.tsv)
- UniProt record: present - [genes/human/NAA10/NAA10-uniprot.txt](NAA10-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/NAA10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/NAA10.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NAA10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NAA10.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: NAA10 (N-alpha-acetyltransferase 10, ARD1A) is the catalytic subunit of the NatA N-terminal acetyltransferase complex, the major co-translational N-terminal acetyltransferase in human cells. In complex with its auxiliary subunit NAA15, which anchors the enzyme to the ribosome, NAA10 transfers an acetyl group from acetyl-CoA to the free alpha-amino group of nascent polypeptide N-termini that begin with small residues (Ser, Ala, Thr, Gly, Cys, Val) exposed after initiator-methionine excision. This irreversible modification affects protein folding, stability, complex assembly, targeting and degradation. NatA activity is further modulated by the associated factors HYPK and NAA50 (the NatE catalytic subunit). NAA10 acts predominantly in the cytoplasm on ribosome-associated nascent chains, with an additional nuclear pool. The free (NAA15-unbound) form has been reported to perform internal (lysine) acetylation of selected substrates (e.g. HIF1A, HSPA1A/B, histone H4), and NAA10 has been implicated in several context-dependent regulatory roles. NAA10 is X-linked (Xq28); pathogenic variants cause Ogden syndrome and related N-terminal acetyltransferase deficiency disorders.
- Existing/core annotation action counts: ACCEPT: 25; KEEP_AS_NON_CORE: 25; MARK_AS_OVER_ANNOTATED: 6

## PN Consistency Summary

- **Consistency:** Excellent agreement for the core. Review (catalytic NatA subunit), notes, and PN all agree NAA10 is the **catalytic** NatA subunit: NatA complex (GO:0031415, IDA/IPI accepted) and N-terminal acetyltransferase activity (GO:0004596/GO:1990189/GO:0008999, EXP/IDA accepted). The ALP/mTORC1-via-TSC2 role is a documented moonlighting function; the PN correctly maps it to nothing (no_mapping), and the review treats the analogous moonlighting (Hsp70 acetylation GO:1904592, sister-chromatid GO:2000719) as KEEP_AS_NON_CORE. No contradictions.
- **PN story / NEW pressure:** The Nt-acetylation BP GO:0006474 is flagged `more_specific_than_existing_goa` (new_to_goa for that exact term) but is the parent of NAA10's existing specific EXP terms (GO:1990189 Ser, GO:0008999 Ala) — so it is **already captured** at finer granularity; adding the generic parent adds nothing. No genuine NEW pressure. The TSC2/mTOR/autophagy story (PN ALP row) is real but moonlighting and correctly left unmapped; not a defensible universal GO assertion.
- **Evidence alignment:** PN ALP row cites the ARD1/TSC2/mTOR Science Signaling paper (Kim et al.); the review does not cite that specific paper but captures equivalent moonlighting via PMID:27708256 (Hsp70) and PMID:27422821 (cohesion). PN TR row carries no titles. Core NatA evidence (PMID:15496142, 19480662, 25489052, 29754825) is robust and VERIFIED. Note: review flags PMID:25732826 as WRONG_IDENTIFIER (resolves to a Naa60 paper) — a citation issue already adjudicated, unrelated to PN.
- **Verdict:** Consistent; catalytic-subunit role correct; moonlighting correctly non-core/unmapped. No edits. (The PN GO:0006474 projection is redundant given NAA10's specific Ser/Ala EXP terms.)

## Full Consistency Review

- **UniProt:** P41227 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** two rows — `Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide|NatA/NatE complex component` (TR) and `Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|mTORC1 signal integration` (ALP). **PN-node mapping:** NatA/NatE subtype→GO:0031415 NatA complex (mapped, CC); Nt-acetylation type→GO:0006474 N-terminal protein amino acid acetylation (mapped, BP); ALP nodes all no_mapping/context_only.
- **Consistency:** Excellent agreement for the core. Review (catalytic NatA subunit), notes, and PN all agree NAA10 is the **catalytic** NatA subunit: NatA complex (GO:0031415, IDA/IPI accepted) and N-terminal acetyltransferase activity (GO:0004596/GO:1990189/GO:0008999, EXP/IDA accepted). The ALP/mTORC1-via-TSC2 role is a documented moonlighting function; the PN correctly maps it to nothing (no_mapping), and the review treats the analogous moonlighting (Hsp70 acetylation GO:1904592, sister-chromatid GO:2000719) as KEEP_AS_NON_CORE. No contradictions.
- **PN story / NEW pressure:** The Nt-acetylation BP GO:0006474 is flagged `more_specific_than_existing_goa` (new_to_goa for that exact term) but is the parent of NAA10's existing specific EXP terms (GO:1990189 Ser, GO:0008999 Ala) — so it is **already captured** at finer granularity; adding the generic parent adds nothing. No genuine NEW pressure. The TSC2/mTOR/autophagy story (PN ALP row) is real but moonlighting and correctly left unmapped; not a defensible universal GO assertion.
- **Mapping strategy:** No node change needed. GO:0031415 NatA complex is exact for NAA10. GO:0006474 projection is a broader parent of the gene's specific MF terms — acceptable as a node-level label but redundant at gene level. NAA10 is the right anchor (catalytic subunit) for the NatA node.
- **Evidence alignment:** PN ALP row cites the ARD1/TSC2/mTOR Science Signaling paper (Kim et al.); the review does not cite that specific paper but captures equivalent moonlighting via PMID:27708256 (Hsp70) and PMID:27422821 (cohesion). PN TR row carries no titles. Core NatA evidence (PMID:15496142, 19480662, 25489052, 29754825) is robust and VERIFIED. Note: review flags PMID:25732826 as WRONG_IDENTIFIER (resolves to a Naa60 paper) — a citation issue already adjudicated, unrelated to PN.
- **Verdict:** Consistent; catalytic-subunit role correct; moonlighting correctly non-core/unmapped. No edits. (The PN GO:0006474 projection is redundant given NAA10's specific Ser/Ala EXP terms.)

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/NAA10/NAA10-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Translation | Cytosolic translation | Nascent peptide husbandry | N-terminal acetylation of nascent peptide | NatA/NatE complex component
- UniProt: P41227
- In branches: TR, ALP
- PN-node mapping records (path + ancestors):
    - [subtype] Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide|NatA/NatE complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0031415 NatA complex]
        rationale: This subtype is an exact cellular-component match: members are subunits of the NatA N-terminal acetyltransferase complex. The parent maps the BP (GO:0006474 N-terminal protein amino acid acetylation); this node adds the complementary, non-redundant complex-membership CC term.
    - [type] Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006474 N-terminal protein amino acid acetylation]
        rationale: This PN type denotes N-terminal acetyltransferase machinery acting on nascent peptides. The GO N-terminal acetylation process is the direct target.
    - [group] Translation|Cytosolic translation|Nascent peptide husbandry
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Autophagy-Lysosome Pathway | Pre-initiation autophagy signaling | mTORC1 pathway, upstream | mTORC1 signal integration
- UniProt: P41227
- In branches: TR, ALP
- Notes: aka ARD1. Arrest-defective protein 1 (ARD1) physically interacts with, acetylates, and stabilizes TSC2, thereby repressing mTOR activity. The inhibition of mTOR by ARD1 inhibits cell proliferation and increases autophagy, thereby inhibiting tumorigenicity.
- PN references (titles):
    - ARD1 Stabilization of TSC2 Suppresses Tumorigenesis Through the mTOR Signaling Pathway | Science Signaling (sciencemag.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream|mTORC1 signal integration
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a contextual PN role. The label is useful for curator triage, but by itself does not support a universal GO assertion for all member genes beyond curated ancestor or child mappings.
    - [group] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway, upstream
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling
        status=context_only scope=too_broad_to_propagate GO=[GO:0010506 regulation of autophagy]
        rationale: This class organizes upstream signaling inputs to autophagy initiation. Because the subtree contains generic insulin, AMPK, mTORC1, nutrient-sensing, and miscellaneous signaling components, class-level propagation to regulation of autophagy would over-annotate many genes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0006474 N-terminal protein amino acid acetylation | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
