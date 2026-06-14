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

### PSEPK (P. putida KT2440) — 18 genes reviewed

| Gene | Annotations | Function | Notes | PR |
|------|-------------|----------|-------|----|
| **BenR** | 8 | Transcriptional regulator, benzoate catabolism | AraC/XylS family | — |
| **PP_0635** | 9 | Uncharacterized protein | DUF domain analysis | — |
| **ada** | 16 | Methyltransferase, DNA repair | Adaptive response to alkylation | — |
| **ampC** | 5 | Beta-lactamase | Antibiotic resistance | — |
| **ftsY** | 11 | Signal recognition particle receptor | Sec-dependent protein targeting | — |
| **hglS** | 2 | Hydroxyglutarate synthase | Rare enzymatic function | — |
| **mrcA** | 16 | Penicillin-binding protein 1a | Peptidoglycan biosynthesis | — |
| **pedH** | 14 | PQQ-dependent alcohol dehydrogenase | REE/lanthanide utilization | — |
| **quiC1_qsuB** | 8 | Quinate/shikimate dehydrogenase | Aromatic compound catabolism | — |
| **rpoS** | — | Stationary phase sigma factor | GO:0016987 core; added starvation/biofilm terms; DRAFT | [#159](https://github.com/ai4curation/ai-gene-review/pull/159) |
| **fleQ** | — | Flagellar/biofilm master regulator | Sigma-54 associated; added flagellum assembly/biofilm terms | [#162](https://github.com/ai4curation/ai-gene-review/pull/162) |
| **pvdA** | — | L-ornithine N5-monooxygenase | Pyoverdine biosynthesis; COMPLETE | [#163](https://github.com/ai4curation/ai-gene-review/pull/163) |
| **algD** | — | GDP-mannose 6-dehydrogenase | Alginate biosynthesis | [#157](https://github.com/ai4curation/ai-gene-review/pull/157) |
| **gacA** | — | GacS/GacA response regulator | Phosphorelay; biofilm/T6SS regulation | [#155](https://github.com/ai4curation/ai-gene-review/pull/155) |
| **pcaG** | — | Protocatechuate 3,4-dioxygenase α subunit | Iron-binding terms corrected (β subunit) | [#160](https://github.com/ai4curation/ai-gene-review/pull/160) |
| **phaC** | — | PHA synthase (phaC-II, Q88D23) | Corrected to PHA biosynthetic process | [#161](https://github.com/ai4curation/ai-gene-review/pull/161) |
| **cbrB** | — | CbrA/CbrB response regulator | Carbon catabolite repression; COMPLETE | [#158](https://github.com/ai4curation/ai-gene-review/pull/158) |
| **xylR** | — | TOL plasmid regulator (P06519) | Not native KT2440; organism mismatch noted | [#156](https://github.com/ai4curation/ai-gene-review/pull/156) |

### PSEPU (general P. putida) — 1 gene

| Gene | Annotations | Function |
|------|-------------|----------|
| **Q88CC1** | reviewed | Uncharacterized |

## Batch 2 — Selected for Review (50 new genes)

Fifty additional well-characterized KT2440 (taxon 160488) genes selected to broaden
functional coverage beyond the initial aromatic-catabolism/biotechnology focus, into
central carbon metabolism, stress response, DNA repair, motility, and membrane transport.
All were seeded via `fetch-gene` (UniProt + GOA). None overlap with previously present
gene folders.

**Status: reviews complete.** Each gene has a Falcon (Edison Scientific) deep-research
report (`*-deep-research-falcon.md`) and a fully reviewed `*-ai-review.yaml` — all GOA
annotations adjudicated (no `PENDING`), with descriptions, `core_functions`, and
references. The review pass corrected a number of mis-annotations and citation errors
surfaced in the raw reports (e.g. wrong PMIDs in exbB/fur/relA/pilA/hpd; cofactor terms
in fur (Zn→Fe(II)) and icd (NADP-specific); TreeGrafter/InterPro2GO over-propagations in
mdh, sdhA, groES, hfq, pvdQ; sigma-factor GO convention for rpoD/rpoH).

### Stress response, chaperones & global regulation (12)

| Gene | UniProt | Function |
|------|---------|----------|
| **dnaK** | Q88DU2 | Hsp70 chaperone (protein folding) |
| **groEL** | Q88N55 | GroEL chaperonin |
| **groES** | Q88N56 | GroES co-chaperonin |
| **grpE** | Q88DU1 | DnaK nucleotide-exchange factor |
| **htpG** | Q88FB9 | Hsp90 chaperone |
| **rpoH** | Q7CCA6 | Heat-shock sigma factor (σ32) |
| **rpoD** | Q88QU7 | Primary/housekeeping sigma factor (σ70) |
| **fur** | Q88DT9 | Ferric uptake regulator |
| **oxyR** | Q88C74 | Peroxide-responsive transcription regulator |
| **relA** | Q88MB8 | (p)ppGpp synthetase (stringent response) |
| **hfq** | Q88DD3 | RNA chaperone / sRNA-mediated regulation |
| **ppk** | Q88CG4 | Polyphosphate kinase |

### DNA repair & recombination (7)

| Gene | UniProt | Function |
|------|---------|----------|
| **recA** | Q88ME4 | Recombinase / SOS response |
| **recB** | Q88DZ5 | Exonuclease V β subunit |
| **ruvB** | Q88NJ0 | Holliday junction branch-migration helicase |
| **uvrB** | Q88LF9 | Excinuclease ABC subunit B (NER) |
| **uvrC** | Q88FJ7 | Excinuclease ABC subunit C (NER) |
| **mutL** | Q88DD1 | DNA mismatch repair (MutL) |
| **mutS** | Q88ME7 | DNA mismatch repair (MutS) |

### Central carbon metabolism — TCA cycle (8)

| Gene | UniProt | Function |
|------|---------|----------|
| **gltA** | Q88FA4 | Citrate synthase |
| **acnB** | Q88KF1 | Aconitase B |
| **icd** | Q88FS2 | Isocitrate dehydrogenase |
| **sucA** | Q88FA9 | 2-oxoglutarate dehydrogenase E1 |
| **sucC** | Q88FB2 | Succinyl-CoA synthetase β |
| **sdhA** | Q88FA7 | Succinate dehydrogenase flavoprotein |
| **fumC** | Q88M20 | Fumarase C |
| **mdh** | Q88Q44 | Malate dehydrogenase |

### Glycolysis / ED / anaplerotic & overflow metabolism (9)

| Gene | UniProt | Function |
|------|---------|----------|
| **gapA** | Q88P44 | Glyceraldehyde-3-phosphate dehydrogenase |
| **pgk** | Q88D64 | Phosphoglycerate kinase |
| **eno** | Q88MF9 | Enolase |
| **tpiA** | Q88DV4 | Triosephosphate isomerase |
| **pykA** | Q88N54 | Pyruvate kinase |
| **ppc** | Q88MR4 | PEP carboxylase (anaplerotic) |
| **pgl** | Q88P30 | 6-phosphogluconolactonase (ED/PPP) |
| **aceA** | Q88FI0 | Isocitrate lyase (glyoxylate shunt) |
| **pta** | Q88PS4 | Phosphate acetyltransferase (acetate overflow) |

### Chemotaxis & motility (4)

| Gene | UniProt | Function |
|------|---------|----------|
| **cheY** | Q88EW2 | Chemotaxis response regulator |
| **cheZ** | Q88EW3 | CheY-P phosphatase |
| **fliG** | Q88ET5 | Flagellar motor switch (C-ring) |
| **pilA** | Q88Q62 | Type IV pilin |

### Membrane transport, iron & nitrogen acquisition (8)

| Gene | UniProt | Function |
|------|---------|----------|
| **oprD** | Q88NK1 | Outer-membrane porin D |
| **oprE** | Q88R99 | Outer-membrane porin E (anaerobically induced) |
| **tonB** | Q88C75 | TonB (energization of OM transport) |
| **exbB** | Q88C77 | ExbB (TonB system) |
| **amtB** | Q88CE8 | Ammonium transporter |
| **glnK** | Q88CE7 | PII nitrogen-regulatory protein |
| **pvdQ** | Q88IU8 | Pyoverdine maturation acylase |
| **fpvA** | Q88F81 | Ferripyoverdine TonB-dependent receptor |

### Aromatic / aromatic-amino-acid catabolism (2)

| Gene | UniProt | Function |
|------|---------|----------|
| **hpd** | Q88HC7 | 4-hydroxyphenylpyruvate dioxygenase |
| **fcs** | Q88HK0 | Feruloyl-CoA synthetase (ferulate catabolism) |

## Batch 3 — Aromatic Amino Acid (AAA) Biosynthesis Pathway (16 genes)

The shikimate → chorismate → Trp/Phe/Tyr biosynthetic pathway in KT2440 (taxon
160488). Complements the existing aromatic *catabolism* coverage (ben/cat/pca) with the
*anabolic* route to aromatic amino acids. Seeded via `fetch-gene`; Falcon (Edison)
deep-research reports generated per gene. **Status: reviews complete** — all
annotations adjudicated, descriptions/core_functions/references populated (e.g. trpC and
aroQ over-propagation fixes; aroA bifunctional EPSPS/TyrA module captured). Name variants not resolving as primary UniProt
symbols in KT2440 are covered by a resolved paralog (aroD→aroQ, aroF/aroG→aroH, aroL→aroK)
or are differently named / fused in *Pseudomonas* (trpG, pheC, tyrA).

### Shikimate trunk (common pathway, 7)

| Gene | UniProt | Function |
|------|---------|----------|
| **aroH** | Q88LR3 | DAHP synthase (3-deoxy-D-arabino-heptulosonate-7-P synthase) |
| **aroB** | Q88CV2 | 3-dehydroquinate synthase |
| **aroQ** | Q88IJ6 | 3-dehydroquinate dehydratase (type II) |
| **aroE** | Q88IJ7 | Shikimate dehydrogenase |
| **aroK** | Q88CV1 | Shikimate kinase |
| **aroA** | Q88M05 | EPSP synthase (3-phosphoshikimate 1-carboxyvinyltransferase) |
| **aroC** | Q88LU7 | Chorismate synthase |

### Tryptophan branch (6)

| Gene | UniProt | Function |
|------|---------|----------|
| **trpE** | Q88QS1 | Anthranilate synthase component I |
| **trpD** | Q88QR7 | Anthranilate phosphoribosyltransferase |
| **trpC** | Q88QR6 | Indole-3-glycerol-phosphate synthase |
| **trpF** | Q88LE0 | N-(5'-phosphoribosyl)anthranilate isomerase |
| **trpA** | Q88RP7 | Tryptophan synthase α |
| **trpB** | Q88RP6 | Tryptophan synthase β |

### Phe/Tyr branch & aromatic aminotransferases (3)

| Gene | UniProt | Function |
|------|---------|----------|
| **pheA** | Q88M06 | Chorismate mutase / prephenate dehydratase (P-protein) |
| **tyrB** | Q88LG1 | Aromatic-amino-acid aminotransferase |
| **hisC** | Q88P86 | Histidinol-phosphate / aromatic aminotransferase |

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

- [SPKW-PSEPK](SPKW/SPKW-PSEPK.md) — Analysis of UniProtKB-KW annotation patterns in P. putida
- [REE](REE.md) — Rare earth element biology (pedH is a key gene)
- [BIOSENSORS](BIOSENSORS.md) — Biosensor applications (BenR is relevant)

## Notes

- P. putida KT2440 uses the Entner-Doudoroff pathway exclusively for glucose catabolism (no Embden-Meyerhof-Parnas pathway). This is important for annotation review — glycolysis terms may need careful handling.
- Many genes are annotated by homology to *P. aeruginosa* (PSEAE), but functional divergence is common — P. putida is non-pathogenic while P. aeruginosa is an opportunistic pathogen. Virulence-associated annotations transferred by homology should be scrutinized.
- The REE/lanthanide biology is relatively recent science (post-2011). Annotations for pedH and related genes may be incomplete or missing entirely.
