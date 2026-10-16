---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ASPRV1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q53RT3
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 7
citation_count: 7
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ASPRV1 (human)

## Current model (mechanistic narrative)

ASPRV1 (SASPase) is a mammalian-specific retroviral-like aspartic protease that controls epidermal barrier formation by processing profilaggrin into filaggrin monomers [PMID:21542132, PMID:39098535]. It is synthesized as an inactive SASP28 precursor that undergoes autocatalytic self-cleavage to generate the active SASP14 protease domain, a step necessary for catalytic activation [PMID:32640672, PMID:39098535]. Active SASP14 has highest activity at neutral pH and high ionic strength, is inhibited by pepstatin A and acetyl-pepstatin, and forms a dimer of lower stability than HIV-1 protease [PMID:32640672]. SASP14 directly cleaves the linker peptide of profilaggrin, and SASPase-deficient mice accumulate aberrantly processed profilaggrin with reduced filaggrin, dry skin, and a thicker, less hydrated stratum corneum [PMID:21542132]; gain-of-function transgenic overexpression conversely accelerates keratinocyte differentiation with increased filaggrin-positive granular keratinocytes [PMID:20237492]. Filaggrin is the only natural substrate identified to date [PMID:39098535]. Missense mutations that abolish protease activity or disrupt residues near the autocatalytic cleavage sites cause ichthyosis through dominant alteration of auto-cleavage and filaggrin processing in human kindreds and in dog [PMID:28249031, PMID:32516568]. Beyond the skin, ASPRV1 is expressed in ICAM1+ macrophage-like neutrophils where it is required nonredundantly for perpetuation of chronic autoimmune CNS inflammation in experimental autoimmune encephalomyelitis [PMID:29212956].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0016787 hydrolase activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** *(none)*
- **pathway (Reactome):** R-HSA-1266738 Developmental Biology
- **partners:** *(none)*
- **complexes:** *(none)*

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2011 | High | SASPase (ASPRV1) directly cleaves the linker peptide of profilaggrin to generate filaggrin monomers; SASPase-deficient hairless mice show accumulation of aberrantly processed profilaggrin, marked decrease of filaggrin, dry skin, and a thicker, less hydrated stratum corneum. Recombinant SASPase directly cleaved recombinant profilaggrin in vitro. Missense mutations (V243A and V187I) in atopic dermatitis patients abolished or markedly reduced protease activity in vitro. | PMID:21542132 | EMBO molecular medicine |
| 2010 | Medium | Transgenic overexpression of Taps (ASPRV1) under the ubiquitin C promoter in mice caused impaired cutaneous wound closure and increased numbers of filaggrin-positive keratinocytes in the stratum granulosum (hypergranulosum-like phenotype) after wound healing or TPA-induced hyperplasia, indicating ASPRV1 modulates keratinocyte differentiation timing. | PMID:20237492 | The Journal of investigative dermatology |
| 2017 | Medium | ASPRV1 is specifically expressed in ICAM1+ extravasated (macrophage-like) neutrophils in the CNS during experimental autoimmune encephalomyelitis (EAE). Mice lacking ASPRV1 immunized with a B cell-dependent myelin antigen developed less severe chronic EAE that faded in many individuals, establishing a nonredundant role for ASPRV1 in neutrophil-mediated perpetuation of autoimmune CNS inflammation. | PMID:29212956 | JCI insight |
| 2017 | Medium | A de novo heterozygous missense variant in ASPRV1 (c.1052T>C, p.Leu351Pro), affecting a residue close to an autoprocessing cleavage site, causes ichthyosis in a dog and alters filaggrin expression pattern in affected skin, confirming ASPRV1's essential role in profilaggrin-to-filaggrin processing and skin barrier formation in vivo. | PMID:28249031 | PLoS genetics |
| 2020 | High | Three heterozygous ASPRV1 missense mutations identified in four unrelated ichthyosis kindreds (dominant inheritance) disrupt protein residues near autocatalytic cleavage sites. Expression of mutant ASPRV1 proteins in vitro demonstrated that all three mutations alter ASPRV1 auto-cleavage and filaggrin processing, establishing a gain-of-function/dominant-negative mechanism affecting autocatalytic activation and substrate cleavage. | PMID:32516568 | American journal of human genetics |
| 2020 | High | ASPRV1 undergoes self-proteolysis (autoprocessing) of its precursor form (SASP28) to generate the active protease domain (SASP14). The SASP14 form shows highest activity at neutral pH and high ionic strength. Pepstatin A and acetyl-pepstatin inhibit the protease. The dimer stability of SASP14 is lower than that of HIV-1 protease based on urea dissociation constants. Homology modeling supported structural interpretation of specificity data. | PMID:32640672 | Biomolecules |
| 2024 | Medium | ASPRV1 self-proteolysis is necessary for autoactivation of the protease domain. Filaggrin is the only natural protein substrate identified so far. ASPRV1 and filaggrin are mammalian-specific proteins, providing unique epidermal features. ASPRV1 is also expressed in macrophage-like neutrophils, indicating skin-independent functions. | PMID:39098535 | The Journal of biological chemistry |

## Citations

- PMID:20237492
- PMID:21542132
- PMID:28249031
- PMID:29212956
- PMID:32516568
- PMID:32640672
- PMID:39098535
