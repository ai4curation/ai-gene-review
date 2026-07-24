---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/FANCE
affinage_run_date: 2026-06-09T23:54:43
uniprot_accession: Q9HB96
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 10
citation_count: 10
gates_passed: True
note: >-
  Machine-fetched from the Affinage API (Cheeseman Lab). This is external
  precomputed research to be treated as a preliminary source, NOT a curated
  annotation. Affinage is human-only and LLM-generated; verify claims against
  the cited PMIDs before use.
---

# Affinage mechanistic annotation for FANCE (human)

## Current model (mechanistic narrative)

FANCE is a nuclear subunit of the Fanconi anemia (FA) core complex that functions as a molecular bridge coupling the core complex to its downstream substrate, the FANCD2-FANCI heterodimer [PMID:12093742, PMID:16127171]. It binds FANCC directly and, through a distinct region, contacts FANCD2, thereby recruiting the substrate for monoubiquitination; FANCE is required for nuclear accumulation of FANCC, formation of the FANCA-FANCC complex, FANCD2 monoubiquitination, and FANCD2 nuclear foci assembly [PMID:12093742, PMID:12239156, PMID:16513431]. The FANCC-binding and FANCD2-binding surfaces are separable, and the extreme C-terminal residue phenylalanine 522 is the critical determinant of the FANCD2/FANCI interaction required for substrate monoubiquitination and DNA cross-link repair [PMID:16513431, PMID:24451376]. Structurally FANCE adopts a repeated helical (HEAT-like) fold, and disease-associated mutations map to this domain and disrupt the FANCE-FANCD2 interaction [PMID:17308347]. Beyond its scaffolding role, FANCE is directly phosphorylated by Chk1 at threonine 346 and serine 374 upon DNA damage, an event dispensable for FANCD2 monoubiquitination but required for cross-link repair, defining a separable monoubiquitination-independent function [PMID:17296736]. The FANCC-FANCE-FANCF subcomplex is evolutionarily conserved and additionally acts to suppress meiotic crossovers [PMID:36652992].

## Affinage mechanism profile (its own GO/Reactome grounding)

_Recorded for reference. The AIGR evaluation found this grounding is coarse (collapses to general parents) and can contradict the narrative — do not import these GO ids directly; re-ground from the narrative + PMIDs._

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0140096 catalytic activity, acting on a protein
- **localization:** GO:0005634 nucleus
- **pathway (Reactome):** R-HSA-73894 DNA Repair
- **partners:** FANCC, FANCD2, FANCA, FANCG, FANCF, FANCI, CHEK1
- **complexes:** FA core complex, FANCC-FANCE-FANCF subcomplex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2002 | High | FANCE is a component of the nuclear FA core complex, binding directly to both FANCC and FANCD2. FANCE is required for nuclear accumulation of FANCC, formation of the FANCA-FANCC complex, monoubiquitination of FANCD2, and FANCD2 nuclear foci assembly. Disease-associated FANCC mutants that do not bind FANCE cannot accumulate in the nucleus and are unable to prevent chromosome breakage. | PMID:12093742 | The EMBO journal |
| 2002 | High | FANCE promotes nuclear accumulation of FANCC and is itself a nuclear protein that co-immunoprecipitates with FANCA, FANCC, and FANCG (but not FANCD2) in normal cells. FANCE is required for monoubiquitination of FANCD2 and downstream events in the FA pathway. | PMID:12239156 | Blood |
| 2005 | High | FANCE mediates a ternary complex with FANCC and FANCD2. Using yeast three-hybrid and two-hybrid systems confirmed in human cells, FANCE bridges FANCC and FANCD2. FANCE mutants that interact with FANCC but not FANCD2 abolish FANCD2 monoubiquitination and sensitize cells to DNA cross-linkers. FANCE also mediates interaction between FANCC and FANCF within the core complex. | PMID:16127171 | The Journal of biological chemistry |
| 2007 | High | In response to DNA damage, Chk1 directly phosphorylates FANCE at two conserved sites: threonine 346 and serine 374. Phosphorylated FANCE assembles into nuclear foci and co-localizes with FANCD2. A non-phosphorylatable FANCE mutant (T346A/S374A) permits FANCD2 monoubiquitination and foci formation but fails to complement MMC hypersensitivity, indicating a FANCD2 monoubiquitination-independent function of Chk1-mediated FANCE phosphorylation in DNA cross-link repair. | PMID:17296736 | Molecular and cellular biology |
| 2007 | High | Crystal structure of human FANCE reveals a repeated helical motif (HEAT-like repeats). The crystallographically defined portion of FANCE is sufficient for interaction with FANCD2. Disease-associated mutations in FANCE disrupt the FANCE-FANCD2 interaction, providing structural insight into FA pathogenesis. | PMID:17308347 | Nucleic acids research |
| 2006 | Medium | Nuclear accumulation of FANCE depends on FANCC but not on other FA proteins (FANCA, FANCG, FANCF). Adding a nuclear export signal does not prevent FANCE nuclear localization, indicating the NLS motifs alone are not sufficient. The region of FANCE that binds FANCC is distinct from the region that binds FANCD2, supporting a model in which FANCE recruits FANCD2 to the core complex independently of FANCC binding. | PMID:16513431 | DNA repair |
| 2014 | High | The extreme C-terminus of FANCE (phenylalanine 522) is a critical residue for mediating monoubiquitination of the FANCD2-FANCI complex. An interaction-deficient FANCE mutant (disrupting FANCE-FANCD2 binding at the C-terminus) confers cellular sensitivity to cisplatin comparable to FANCE-null cells. Ectopic expression of the FANCE C-terminus fragment alone in normal cells disrupts DNA repair, confirming the FANCE-FANCD2 interaction is required for DNA cross-link repair. | PMID:24451376 | The Journal of biological chemistry |
| 1999 | Medium | The FANCE gene was mapped to chromosome 6p21-22 using homozygosity mapping and genetic linkage analysis in FA complementation group E families. | PMID:10205272 | American journal of human genetics |
| 2015 | Medium | A splice isoform of FANCE (FANCEΔ4, lacking exon 4) is expressed in normal and breast cancer cell lines. FANCEΔ4 is translated into a nuclear protein but cannot support FANCD2 or FANCI monoubiquitination, fails to rescue MMC-induced G2/M block or cell survival in FANCE-deficient cells, and promotes degradation of FANCD2 protein. FANCEΔ4 interacts with wild-type FANCE and may act as a dominant negative regulator of FANCE activity. | PMID:26277624 | Journal of molecular biology |
| 2023 | Medium | The FANCC-FANCE-FANCF subcomplex is evolutionarily conserved from vertebrates to plants (Arabidopsis). In Arabidopsis meiosis, FANCC, FANCE, and FANCF form a physical complex and act together as anti-crossover factors. Loss of any one of the three genes partially rescues CO-defective mutants and causes synthetic meiotic catastrophe with the pro-CO factor MUS81. | PMID:36652992 | Nucleic acids research |

## Citations

- PMID:10205272
- PMID:12093742
- PMID:12239156
- PMID:16127171
- PMID:16513431
- PMID:17296736
- PMID:17308347
- PMID:24451376
- PMID:26277624
- PMID:36652992
