# GO:0007263 family review and recommended actions

Date: 2026-03-10
Input seed: `GO_0007263-transfer-review.yaml` (QuickGO-derived)

## Scope reviewed

- GO:0007263 nitric oxide mediated signal transduction
- GO:0010749 regulation of nitric oxide mediated signal transduction
- GO:0010750 positive regulation of nitric oxide mediated signal transduction
- GO:0010751 negative regulation of nitric oxide mediated signal transduction

## Curation summary

- Seed contained 48 rows but collapsed to 23 unique focal assertions (duplicates in seed).
- Recommended action totals across 23 unique assertions:
  - TRANSFER: 16
  - REMOVE: 4
  - MARK_AS_OVER_ANNOTATED: 1
  - UNDECIDED: 1
  - KEEP_AS_IS: 0
  - NTR: 1 (term-family gap noted below)
- Dominant migration pattern:
  - Upstream NO production biology → `GO:0006809` / `GO:0045428` / `GO:0045429` / `GO:0045019`
  - NO-sGC-cGMP cascade biology → `GO:0038060` / `GO:0141151`
  - NO-triggered cellular chemistry → `GO:0071732` / `GO:0035606`
- Rat `Rasd1` note:
    - No focal assertion for rat `Rasd1` was present in the reviewed seed set used for this file.
    - For the corrected citation (`PMID:11086993`), QuickGO returns rat `Rasd1` with `IDA` support to `GO:0071732` (cellular response to nitric oxide), not to `GO:0007263`.
    - **Recommended action if encountered as GO:0007263 + Rasd1 + PMID:11086993:** `TRANSFER` to `GO:0071732`.

## Recommended actions (unique assertions)

Format: **current term | gene (taxon) | PMID | action | proposed replacement**

1. GO:0007263 | nos1 (Danio rerio) | PMID:19450519 | **TRANSFER** | GO:0006809 nitric oxide biosynthetic process  
   Rationale: nos1 is required upstream to generate NO for HSC development.

2. GO:0007263 | nos1 (Danio rerio) | PMID:28951000 | **TRANSFER** | GO:0006809 nitric oxide biosynthetic process  
   Rationale: behavioral phenotype is linked to loss of NO production by Nos1.

3. GO:0007263 | Rilpl1 (Rattus norvegicus) | PMID:19607794 | **TRANSFER** | GO:0035606 peptidyl-cysteine S-trans-nitrosylation  
   Rationale: evidence is specific to NO-dependent S-nitrosylation biology.

4. GO:0010749 | tnnt2a (Danio rerio) | PMID:19450519 | **TRANSFER** | GO:0045428 regulation of nitric oxide biosynthetic process  
   Rationale: blood-flow/cardiac upstream regulation of NO environment.

5. GO:0010750 | Gucy1a2 (Mus musculus) | PMID:16614755 | **TRANSFER** | GO:0038060 nitric oxide-cGMP-mediated signaling  
   Rationale: direct NO receptor (sGC alpha subunit) in NO-cGMP cascade.

6. GO:0007263 | CNGC2 (Arabidopsis thaliana) | PMID:17384171 | **TRANSFER** | GO:0045429 positive regulation of nitric oxide biosynthetic process  
   Rationale: CNGC2-dependent Ca2+ events act upstream of NO production.

7. GO:0010750 | INS (Homo sapiens) | PMID:14615391 | **TRANSFER** | GO:0045429 positive regulation of nitric oxide biosynthetic process  
   Rationale: insulin increases NO synthesis and cGMP in vascular smooth muscle.

8. GO:0010750 | INS (Homo sapiens) | PMID:15792832 | **REMOVE** | —  
   Rationale: paper indicates insulin-stimulated transport is not blocked by NOS/GC inhibition.

9. GO:0010749 | Rln1 (Rattus norvegicus) | PMID:19073841 | **TRANSFER** | GO:0045429 positive regulation of nitric oxide biosynthetic process  
   Rationale: relaxin acts via nNOS-NO-cGMP pathway.

10. GO:0007263 | Mt2 (Mus musculus) | PMID:11792622 | **TRANSFER** | GO:0071732 cellular response to nitric oxide  
    Rationale: NO-triggered zinc homeostasis response mediated by MT.

11. GO:0007263 | Mt1 (Mus musculus) | PMID:11792622 | **TRANSFER** | GO:0071732 cellular response to nitric oxide  
    Rationale: same as MT2; response-level evidence.

12. GO:0007263 | Gapdh (Rattus norvegicus) | PMID:19607794 | **TRANSFER** | GO:0035606 peptidyl-cysteine S-trans-nitrosylation  
    Rationale: direct GAPDH S-nitrosylation in reported pathway.

13. GO:0010751 | THBS1 (Homo sapiens) | PMID:16150726 | **TRANSFER** | GO:0141151 negative regulation of nitric oxide-cGMP mediated signal transduction  
    Rationale: direct inhibition of NO-responsive endothelial responses in cGMP-dependent context.

14. GO:0010751 | Spink1 (Mus musculus) | PMID:22228629 | **TRANSFER** | GO:0045019 negative regulation of nitric oxide biosynthetic process  
    Rationale: endogenous NO levels are reduced; NO donors reverse phenotype.

15. GO:0010749 | VEGFA (Homo sapiens) | PMID:16150726 | **REMOVE** | —  
    Rationale: VEGFA is contextual background, not directly tested in the core claim.

16. GO:0010749 | Rln1 (Mus musculus) | PMID:19073841 | **TRANSFER** | GO:0045429 positive regulation of nitric oxide biosynthetic process  
    Rationale: upstream nNOS-NO-cGMP activation.

17. GO:0010750 | smarca4a (Danio rerio) | PMID:32738093 | **TRANSFER** | GO:0045429 positive regulation of nitric oxide biosynthetic process  
    Rationale: Brg1 loss damages NO microenvironment; NO donor partial rescue supports upstream role.

18. GO:0010749 | Pde5a (Mus musculus) | PMID:16150726 | **REMOVE** | —  
    Rationale: pharmacologic PDE context; not strong gene-specific evidence for PDE5A.

19. GO:0007263 | NDNF (Homo sapiens) | PMID:24706764 | **TRANSFER** | GO:0045429 positive regulation of nitric oxide biosynthetic process  
    Rationale: NDNF effect depends on Akt/eNOS and is lost with NOS/eNOS disruption.

20. GO:0010749 | Cbs (Mus musculus) | PMID:10953023 | **MARK_AS_OVER_ANNOTATED** | —  
    Rationale: indirect NO bioavailability effect in oxidative-stress disease model.

21. GO:0010749 | Pde2a (Mus musculus) | PMID:16150726 | **REMOVE** | —  
    Rationale: same issue as PDE5A; weak gene-specific assignment.

22. GO:0010750 | Gucy1a1 (Mus musculus) | PMID:16614755 | **TRANSFER** | GO:0038060 nitric oxide-cGMP-mediated signaling  
    Rationale: direct NO receptor component in canonical cascade.

23. GO:0007263 | WRKY27 (Arabidopsis thaliana) | PMID:18702671 | **UNDECIDED** | —  
    Rationale: abstract-level evidence is indirect (potential NO-generation targets), insufficient for confident transfer.

## Ontology gap / NTR recommendation

For several transferred assertions currently moved to biosynthesis-regulation terms due to obsoletion constraints, curator intent suggests a missing family around the NO-cGMP branch:

- Proposed NTR candidate labels:
  - positive regulation of nitric oxide-cGMP-mediated signaling
  - regulation of nitric oxide-cGMP-mediated signaling

This would preserve mechanistic directionality when evidence is clearly on NO→sGC→cGMP pathway modulation rather than NO production.

## Execution order recommendation

1. Apply all high-confidence TRANSFER actions first.
2. Remove low-specificity PDE2A/PDE5A/VEGFA assertions.
3. Flag CBS as over-annotated for curator review queue.
4. Keep WRKY27 as UNDECIDED pending fuller text/figure-level evidence.
5. Submit NTR request for positive/regulation forms of NO-cGMP-mediated signaling.
