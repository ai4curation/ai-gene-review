---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ALKBH6
affinage_run_date: 2026-06-09T22:02:43
uniprot_accession: Q3KRA9
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 6
citation_count: 5
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ALKBH6 (human)

## Current model (mechanistic narrative)

ALKBH6 is a FeII/2-oxoglutarate-dependent dioxygenase that acts as a nucleotide demethylase and contributes to the cellular response to alkylation damage [PMID:35120926, PMID:40885392]. It specifically demethylates N-7-methyl-GMP and N-1-methyl-AMP, with strict dependence on a substrate phosphate group, as it shows no activity toward methylated bases or nucleosides; both modified nucleotides are confirmed endogenous substrates, and catalytic and substrate-binding residues have been defined by kinetics and active-site mutagenesis [PMID:40885392]. Its 2-oxoglutarate decarboxylation activity has been directly measured through uncoupled succinate production, and the enzyme is inhibited by Ni(II) as well as by succinate and the oncometabolite 2-hydroxyglutarate [PMID:39845104, PMID:40885392]. Crystal structures show that ALKBH6 carries sequence- and conformationally divergent Flip1/Flip2 nucleotide recognition lid domains and a unique Flip3 domain that discriminates against double-stranded nucleic acids, occludes the active center, and mediates protein interactions [PMID:35120926]. Functionally, ALKBH6 complements an AlkB-deficient E. coli strain to restore alkylation resistance, and its loss in pancreatic cancer cells increases alkylating-agent-induced DNA damage and reduces survival, linking it to alkylation damage repair [PMID:33897761]. ALKBH6 physically interacts with the transcription repressor and tumor suppressor ZMYND11 through ZMYND11's PHD and CC-MYND domains, connecting nucleic acid modification to histone-based epigenetic regulation [PMID:35120926, PMID:41591843].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0140098 catalytic activity, acting on RNA, GO:0016491 oxidoreductase activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-73894 DNA Repair
- **partners:** ZMYND11
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2022 | High | Crystal structures of human ALKBH6 (holo and ligand-bound) revealed that its Flip1 and Flip2 nucleotide recognition lid (NRL) domains are distinct in sequence and conformation from other AlkB family members, and that its unique Flip3 domain discriminates against double-stranded nucleic acids, blocks the active center, and mediates protein–protein interactions. Structural analyses also indicate ALKBH6 may function as a nucleic acid demethylase. | PMID:35120926 | The Journal of biological chemistry |
| 2022 | Medium | ALKBH6 interacts with the transcription repressor ZMYND11, revealing cross-talk between nucleic acid modification and histone modification in epigenetic regulation and tumor suppression. | PMID:35120926, PMID:41591843 | The Journal of biological chemistry |
| 2021 | Medium | ALKBH6 complements an E. coli AlkB-deficient strain, increasing resistance to alkylating agents, demonstrating that it functions as a DNA damage repair enzyme capable of reversing alkylation damage. Loss of ALKBH6 in human pancreatic cancer cells increases alkylating agent-induced DNA damage and decreases cell survival. | PMID:33897761 | Frontiers in genetics |
| 2024 | Medium | ALKBH6 enzymatic activity (2-oxoglutarate decarboxylation) was confirmed by measuring uncoupled succinate production in the absence of substrate, and Ni(II)-mediated inhibition of ALKBH6 was verified using this assay. | PMID:39845104 | Biology methods & protocols |
| 2025 | High | ALKBH6 is a nucleotide demethylase that specifically demethylates N-7-methyl-GMP and N-1-methyl-AMP; the presence of a phosphate group in the substrate is essential for activity (no activity toward methylated bases or methylated nucleosides). Catalytic and substrate-binding residues were identified by enzyme kinetic analysis. Succinate and the oncometabolite 2-hydroxyglutarate act as inhibitors. N-7-methyl-GMP and N-1-methyl-AMP were confirmed as endogenous substrates. | PMID:40885392 | The Journal of biological chemistry |
| 2026 | Medium | Both the PHD domain and the CC-MYND domain of tumor suppressor ZMYND11 interact with ALKBH6, providing structural evidence for a previously uncharacterized epigenetic mechanism linking ZMYND11 to nucleic acid repair. | PMID:41591843 | Nucleic acids research |

## Citations

- PMID:33897761
- PMID:35120926
- PMID:39845104
- PMID:40885392
- PMID:41591843
