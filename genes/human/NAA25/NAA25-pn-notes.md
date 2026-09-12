# NAA25 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q14CX7
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/NAA25/NAA25-ai-review.yaml](NAA25-ai-review.yaml)
- AIGR review HTML: present - [genes/human/NAA25/NAA25-ai-review.html](NAA25-ai-review.html)
- Gene notes: present - [genes/human/NAA25/NAA25-notes.md](NAA25-notes.md)
- GOA TSV: present - [genes/human/NAA25/NAA25-goa.tsv](NAA25-goa.tsv)
- UniProt record: present - [genes/human/NAA25/NAA25-uniprot.txt](NAA25-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/NAA25.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/NAA25.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NAA25.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/NAA25.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: NAA25 (N-alpha-acetyltransferase 25; also MDM20, NAP1, p120) is the large non-catalytic auxiliary subunit of the human NatB N-terminal acetyltransferase complex. NatB is composed of the catalytic subunit NAA20 and the auxiliary subunit NAA25, and it co-translationally acetylates the alpha-amino group of N-terminal methionine residues that are retained in front of acidic or amide side chains (Met-Asp, Met-Glu, Met-Asn and Met-Gln N-termini). NAA25 is a TPR-repeat/alpha-solenoid protein that cradles and stabilizes the catalytic NAA20 subunit and anchors the complex to ribosomes, positioning it to act on nascent polypeptides. It is a cytoplasmic protein and is required for normal cell-cycle progression. Loss of NatB activity (e.g. NAA20 variants) is associated with neurodevelopmental disease, underscoring the physiological importance of NatB-mediated N-terminal acetylation.
- Existing/core annotation action counts: ACCEPT: 6; KEEP_AS_NON_CORE: 3

## PN Consistency Summary

- **Consistency:** Strong agreement. Review, notes, and PN concur NAA25 is the **auxiliary, non-catalytic** subunit of NatB (catalytic subunit is NAA20, not NAA25): NatB complex (GO:0031416, IBA/IPI/ComplexPortal accepted), activator activity (GO:0010698 IBA accepted), cytoplasm. Critically the PN subtype is correctly **NatB** (GO:0031416), not NatA — distinct from NAA10/NAA15. No contradictions.
- **PN story / NEW pressure:** Modest. The PN BP GO:0006474 is flagged new_to_goa for NAA25 (NAA25's GOA has GO:0031416, GO:0010698, GO:0007010, localizations, GO:0005515 — but no GO:0006474). So "N-terminal protein amino acid acetylation" as a process annotation would be genuinely new to NAA25's GOA. It is defensible as process participation (NAA25 is required for NatB activity), but for a non-catalytic scaffold the review prefers the activator MF + complex CC. Verdict: borderline ADD vs already-captured-by-proxy; lean **already captured** via GO:0010698 + GO:0031416, since GO:0006474 risks implying catalytic involvement by the auxiliary subunit.
- **Evidence alignment:** PN row carries no reference titles. Review anchors on PMID:18570629 (hNatB identification, VERIFIED) and PMID:34230638 (NAA20 disease variants, VERIFIED, contextual). Good overlap with the primary NatB literature; no divergence.
- **Verdict:** Consistent; auxiliary NatB-subunit identity correct and properly distinguished from NatA. No edits. The PN GO:0006474 BP projection is new-to-GOA but optional — the activator MF + NatB CC already convey the function without over-attributing catalysis.

## Full Consistency Review

- **UniProt:** Q14CX7 · **batch:** proteostasis-batch-2026-06-07c · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide|NatB complex component` (TR only). **PN-node mapping:** subtype→GO:0031416 NatB complex (mapped, CC); type→GO:0006474 N-terminal protein amino acid acetylation (mapped, BP); group no_mapping; class/branch context_only.
- **Consistency:** Strong agreement. Review, notes, and PN concur NAA25 is the **auxiliary, non-catalytic** subunit of NatB (catalytic subunit is NAA20, not NAA25): NatB complex (GO:0031416, IBA/IPI/ComplexPortal accepted), activator activity (GO:0010698 IBA accepted), cytoplasm. Critically the PN subtype is correctly **NatB** (GO:0031416), not NatA — distinct from NAA10/NAA15. No contradictions.
- **PN story / NEW pressure:** Modest. The PN BP GO:0006474 is flagged new_to_goa for NAA25 (NAA25's GOA has GO:0031416, GO:0010698, GO:0007010, localizations, GO:0005515 — but no GO:0006474). So "N-terminal protein amino acid acetylation" as a process annotation would be genuinely new to NAA25's GOA. It is defensible as process participation (NAA25 is required for NatB activity), but for a non-catalytic scaffold the review prefers the activator MF + complex CC. Verdict: borderline ADD vs already-captured-by-proxy; lean **already captured** via GO:0010698 + GO:0031416, since GO:0006474 risks implying catalytic involvement by the auxiliary subunit.
- **Mapping strategy:** GO:0031416 NatB complex (CC) is exact and the correct shared term — properly distinguishes NAA25 (NatB) from the NAA10/NAA15 NatA node. The cytoskeleton-organization IBA (GO:0007010, from yeast/fly NatB substrate acetylation) is correctly KEEP_AS_NON_CORE; the PN does not project it. No node change needed.
- **Evidence alignment:** PN row carries no reference titles. Review anchors on PMID:18570629 (hNatB identification, VERIFIED) and PMID:34230638 (NAA20 disease variants, VERIFIED, contextual). Good overlap with the primary NatB literature; no divergence.
- **Verdict:** Consistent; auxiliary NatB-subunit identity correct and properly distinguished from NatA. No edits. The PN GO:0006474 BP projection is new-to-GOA but optional — the activator MF + NatB CC already convey the function without over-attributing catalysis.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/NAA25/NAA25-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Nascent peptide husbandry | N-terminal acetylation of nascent peptide | NatB complex component
- UniProt: Q14CX7
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [subtype] Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide|NatB complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0031416 NatB complex]
        rationale: Exact cellular-component match: members are subunits of the NatB N-terminal acetyltransferase complex. Complements the parent BP mapping with the complex-membership CC term.
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

## Projected GO annotations (1)
- GO:0006474 N-terminal protein amino acid acetylation | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Nascent peptide husbandry|N-terminal acetylation of nascent peptide

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
