# P. putida Gene Annotation Review Project

## Overview

Systematic AI-assisted review of GO annotations for *Pseudomonas putida*, focusing primarily on the well-characterized KT2440 strain (UniProt: PSEPK). *P. putida* is a metabolically versatile soil bacterium of significant interest for bioremediation, industrial biotechnology, and plant growth promotion. Its annotations are predominantly from automated pipelines (InterPro2GO, UniProtKB-KW, TreeGrafter), with very few experimental annotations (~50 from PMIDs), making careful review essential.

## Organism Details

- **Species:** *Pseudomonas putida*
- **Primary strain:** KT2440 (UniProt taxon code: PSEPK)
- **Other strains:** PSEPU (general *P. putida*)
- **Genome:** ~6.2 Mb, ~5,350 protein-coding genes
- **Key biology:** Aromatic compound degradation, solvent tolerance, plant root colonization, polyhydroxyalkanoate (PHA) biosynthesis, rare earth element utilization

## Completed Reviews

### PSEPK (P. putida KT2440) — 9 genes, 89 annotations reviewed

| Gene | Annotations | Function | Notes |
|------|-------------|----------|-------|
| **BenR** | 8 | Transcriptional regulator, benzoate catabolism | AraC/XylS family |
| **PP_0635** | 9 | Uncharacterized protein | DUF domain analysis |
| **ada** | 16 | Methyltransferase, DNA repair | Adaptive response to alkylation |
| **ampC** | 5 | Beta-lactamase | Antibiotic resistance |
| **ftsY** | 11 | Signal recognition particle receptor | Sec-dependent protein targeting |
| **hglS** | 2 | Hydroxyglutarate synthase | Rare enzymatic function |
| **mrcA** | 16 | Penicillin-binding protein 1a | Peptidoglycan biosynthesis |
| **pedH** | 14 | PQQ-dependent alcohol dehydrogenase | **Rare earth element (lanthanide) utilization** — flagship gene for REE biology |
| **quiC1_qsuB** | 8 | Quinate/shikimate dehydrogenase | Aromatic compound catabolism |

### PSEPU (general P. putida) — 1 gene

| Gene | Annotations | Function |
|------|-------------|----------|
| **Q88CC1** | reviewed | Uncharacterized |

## Priority Genes for Future Review

### Aromatic Catabolism (core P. putida biology)
- **benABCD** — Benzoate dioxygenase complex
- **catABC** — Catechol branch of β-ketoadipate pathway  
- **pcaGHBDCIJF** — Protocatechuate branch
- **nahABCDEF** — Naphthalene degradation (if present in KT2440 derivatives)
- **xylXYZ** — Toluene/xylene degradation (TOL plasmid genes)

### Central Metabolism & Biotechnology
- **phaABCZ** — Polyhydroxyalkanoate biosynthesis
- **glk**, **zwf**, **edd**, **eda** — Glucose catabolism (ED pathway, no EMP)
- **gcd** — Glucose dehydrogenase (periplasmic oxidation)
- **PP_1084** (oleC), **PP_1083** (oleD) — Olefin biosynthesis

### Rare Earth Element Biology
- **pedE** — Ca²⁺-dependent ethanol dehydrogenase (counterpart to pedH)
- **lanM** — Lanmodulin (lanthanide-binding protein)
- **lutH/lutABCDEF** — Lanthanide uptake and transport

### Solvent Tolerance
- **ttgABC**, **ttgDEF**, **ttgGHI** — Toluene efflux pumps (RND family)
- **srpABC** — Solvent resistance regulon

### Plant Interactions
- **pvdABCDES** — Pyoverdine siderophore biosynthesis
- **iaaM/iaaH** — Indole-3-acetic acid biosynthesis (auxin)
- **algABCDEFG** — Alginate biosynthesis

### Stress Response & Regulation
- **rpoS** — Stationary phase sigma factor
- **gacA/gacS** — Global regulatory two-component system
- **fleQ** — Flagellar/biofilm master regulator
- **cbrA/cbrB** — Carbon-nitrogen balance regulation

## Related Projects

- [SPKW-PSEPK](SPKW-PSEPK.md) — Analysis of UniProtKB-KW annotation patterns in P. putida
- [REE](REE.md) — Rare earth element biology (pedH is a key gene)
- [BIOSENSORS](BIOSENSORS.md) — Biosensor applications (BenR is relevant)

## Notes

- P. putida KT2440 uses the Entner-Doudoroff pathway exclusively for glucose catabolism (no Embden-Meyerhof-Parnas pathway). This is important for annotation review — glycolysis terms may need careful handling.
- Many genes are annotated by homology to *P. aeruginosa* (PSEAE), but functional divergence is common — P. putida is non-pathogenic while P. aeruginosa is an opportunistic pathogen. Virulence-associated annotations transferred by homology should be scrutinized.
- The REE/lanthanide biology is relatively recent science (post-2011). Annotations for pedH and related genes may be incomplete or missing entirely.
