---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARL14EP
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q8N8R7
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 5
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARL14EP (human)

## Current model (mechanistic narrative)

ARL14EP (ARF7EP/C11orf46) is a bifunctional adaptor protein that operates both in cytoplasmic vesicle transport and in chromatin-based transcriptional repression [PMID:21458045, PMID:31511512]. In human dendritic cells it acts as an effector of the GTPase ARL14/ARF7, bridging the activated GTPase to the motor protein myosin 1E to drive actin-based movement of MHC-II vesicles [PMID:21458045]. In neurons it is a nuclear protein that associates with the SETDB1 repressor complex to silence axonal guidance genes such as Sema6a, an activity required for transcallosal axonal connectivity; an intellectual-disability-associated R236H mutant fails to rescue this connectivity, and locus-specific recruitment via dCas9-SunTag normalizes SEMA6A expression through repressive chromatin remodeling [PMID:31511512]. Its conserved cysteine-rich domain mediates this chromatin role by docking onto the non-canonical methyl-CpG-binding domain of SETDB2, which has lost methylated-DNA binding and instead presents a basic concave surface, an arginine finger, and an intermolecular β-sheet as a protein–protein interaction interface that stabilizes the methyltransferase at chromatin [PMID:38159574, PMID:38458157]. This methyltransferase-stabilizing function is conserved to the C. elegans ortholog ARLE-14, which promotes chromatin association of MET-2/SETDB1 together with LIN-65/ATF7IP to regulate the timing of heterochromatin formation and to antagonize SET-25-driven monoallelic silencing during embryogenesis [PMID:30140741, PMID:41315265, PMID:38328214].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity
- **localization:** GO:0005634 nucleus, GO:0031410 cytoplasmic vesicle
- **pathway (Reactome):** R-HSA-4839726 Chromatin organization, R-HSA-5653656 Vesicle-mediated transport
- **partners:** ARL14, MYO1E, SETDB1, SETDB2, MET-2, LIN-65, ATF7IP
- **complexes:** SETDB1 repressor complex, ARL14–ARF7EP–myosin 1E complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | Medium | ARL14EP (ARF7EP) functions as an effector protein of the GTPase ARL14/ARF7, forming a complex that recruits the motor protein myosin 1E; this ARL14–ARF7EP–myosin 1E complex drives movement of MHC-II vesicles along the actin cytoskeleton in human dendritic cells. | PMID:21458045 | Cell |
| 2018 | Medium | The C. elegans ortholog ARLE-14 (ARL14EP) binds to the histone H3K9 methyltransferase MET-2 (SETDB1 ortholog) and promotes its stable association with chromatin; together with LIN-65, this complex regulates the timing of heterochromatin domain formation during embryogenesis. | PMID:30140741 | Science advances |
| 2019 | High | C11orf46 (ARL14EP) is a nuclear protein required for transcallosal axonal connectivity; knockdown causes dysconnectivity rescued by wild-type but not the C11orf46-R236H intellectual-disability mutant; C11orf46 represses axonal development genes (e.g., Sema6a) through association with the SETDB1 repressor complex, and locus-specific recruitment of C11orf46 via dCas9-SunTag normalizes SEMA6A expression and rescues connectivity via repressive chromatin remodeling. | PMID:31511512 | Nature communications |
| 2023 | High | The crystal structure of human SETDB2 methyl-CpG-binding domain (MBD) in complex with the cysteine-rich domain of C11orf46 (ARL14EP) reveals that the non-canonical MBD has lost methylated-DNA-binding ability and instead uses its conserved basic concave surface, an arginine finger motif, a unique N-terminal extension, and intermolecular β-sheet formation to engage the cysteine-rich domain of C11orf46 as a protein–protein interaction surface. | PMID:38159574, PMID:38458157 | Structure (London, England : 1993) |
| 2024 | Medium | In C. elegans, ARLE-14 (ARL14EP ortholog) works with MET-2/SETDB1 and LIN-65/ATF7IP to antagonize SET-25-driven random monoallelic silencing; MET-2's catalytic SET domain is required, and ARLE-14 promotes MET-2 chromatin association, placing ARL14EP in a pathway that prevents somatic monoallelic expression during embryonic development. | PMID:41315265, PMID:38328214 | Nature communications |

## Citations

- PMID:21458045
- PMID:30140741
- PMID:31511512
- PMID:38159574
- PMID:38328214
- PMID:38458157
- PMID:41315265
