---
name: obsoletion_reannotation
description: Process and procedures for reannotating GO annotations when BP terms are obsoleted in favor of new MF terms
type: project
---

# GO Obsoletion Reannotation Process

## Overview

When GO BP (Biological Process) terms are deprecated in favor of new MF (Molecular Function) terms, existing annotations in the affected terms must be reviewed and transferred to appropriate replacement terms.

## Input

- A TSV of annotations to the obsoleted terms, fetched from the GOA/QuickGO database. File naming convention: `annotations/<GO_IDs_hyphen_separated>.tsv`
- The obsoletion rationale: which new MF term(s) replace the old BP terms, and why
- The definition and comment of the new replacement term(s), including PMID of the key reference

## Column structure of annotation TSVs

Standard columns: `assigned_by`, `bioentity`, `bioentity_label`, `reference`, `qualifier`, `annotation_class`, `annotation_class_label`, `evidence_type`, `evidence_with`, `bioentity_isoform`, `panther_family`, `date`, `annotation_extension_class`, `taxon`

## Procedure

1. **Read the annotation TSV** to understand the scope (proteins, organisms, evidence types, references).

2. **Check publication cache**: For each unique PMID, check `publications/PMID_<id>.md`. For non-cached PMIDs, use WebSearch/WebFetch (PubMed eutils API: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=PMID&rettype=abstract&retmode=text`).

3. **Classify each annotation** using the following actions:
   - `TRANSFER <GO:ID> <label>` — evidence supports the new replacement MF term
   - `TRANSFER <other GO:ID> <label>` — evidence better fits a different MF term (e.g., tethering vs. docking)
   - `REVIEW` — weak/indirect evidence (NAS with only indirect support, IEP, TAS), or protein's role is regulatory/structural rather than directly molecular
   - `REMOVE` — annotation is clearly incorrect based on the reference
   - `NOT <GO:ID> <label>` — for negated annotations (qualifier = "not"), preserve as NOT annotation to the new term

4. **Key biological distinctions for vesicle trafficking MF terms**:
   - **Vesicle tethering activity (GO:0099023)**: long-range initial capture, SNARE-independent (e.g., exocyst complex, USO1/p115, Rab GTPases). The exocyst is explicitly a *tethering* complex per PMID:22420621.
   - **Vesicle docking activity (GO:0160321)**: stable close-apposition of vesicle to target membrane, succeeds tethering, precedes fusogenic activity. Supported by: SNAREs (syntaxins, VAMPs, SNAP25), SM proteins (Munc18/Stxbp family, SEC1, unc-18), synaptotagmin (Syt1), RIM/RIMS proteins, Liprin-α/PPFIA, active zone scaffolds.
   - **Negative regulators** (e.g., SNPH/syntaphilin): annotate as `NOT GO:0160321` or negative regulatory MF, not the direct activity term.

5. **Group repeated annotations**: Many entries (e.g., all exocyst subunits from the same PMID) share identical reasoning — document once and apply uniformly.

6. **Write output TSV** with two new columns appended:
   - `reannotation_action`: e.g., `TRANSFER GO:0160321 vesicle docking activity`
   - `reannotation_reasoning`: 1–3 sentences with key excerpt from or about the reference

   Output file naming: append `-reannotated` to the input filename.

7. **Label format**: Always include both GO ID and term label in the action column (e.g., `TRANSFER GO:0160321 vesicle docking activity`, not just `TRANSFER GO:0160321`).

## Critical: Always verify GO term IDs

**Never guess GO IDs.** Always look up terms using the OLS MCP or the local ontology cache (`cache/ontologies/go.tsv`) before assigning them. A plausible-sounding ID may be a completely different term (e.g., a CC instead of an MF).

If the correct replacement MF term does not exist yet (e.g., "vesicle tethering activity"), flag those annotations as `REVIEW` with a note explaining what kind of term is needed, rather than inventing an ID.

## Example from vesicle docking obsoletion (2026-04)

Obsoleted terms: GO:0048278, GO:0048211, GO:0090384, GO:0106020/21/22, GO:0006904, GO:0016081, GO:0061790
New replacement MF: GO:0160321 vesicle docking activity (PMID:28237810)

Annotation file: `annotations/GO_0006904-GO_0016081-GO_0048211-GO_0048278-GO_0061790-GO_0090384-GO_0106020-GO_0106021-GO_0106022.tsv`
Reannotated file: same with `-reannotated` suffix

Result distribution (130 annotations):
- 48 → TRANSFER GO:0160321 vesicle docking activity (SNAREs, SM proteins, Syt1, RIMs, active zone proteins)
- 57 → TRANSFER GO:7770062 vesicle membrane tethering activity (all exocyst subunits, USO1, YPT1 — newly created MF term; BP tethering terms for reference: GO:0099022 vesicle tethering, GO:0090522 vesicle tethering involved in exocytosis)
- 22 → REVIEW (weak/indirect evidence)
- 3 → NOT GO:0160321 (SNPH negative regulator; Unc13a/b NOT for LDCV docking)
