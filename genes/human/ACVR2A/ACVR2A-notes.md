# ACVR2A review notes

## 2026-10-25 — activin module member audit

Reviewed all 102 seeded annotation rows against retrieved publications, with a
separate activin type II receptor core and BMP receptor core. The review does
not equate a type II receptor with the downstream type I receptor that directly
phosphorylates R-SMADs. No NEW annotations were proposed.

The original PMID titles were synchronized from the fetched publication cache.
Perplexity research failed with insufficient quota; the required Falcon attempt
failed authentication and its perplexity-lite fallback also failed. This file
records manual research; no provider report was fabricated.

- [PMID:1314589](https://pubmed.ncbi.nlm.nih.gov/1314589/), *Molecular cloning and
  binding properties of the human type II activin receptor*: “specifically binds
  activin A with a Kd of 360 pM”. The receptor spans the membrane and has an
  intracellular kinase domain.
- [PMID:8721982](https://pubmed.ncbi.nlm.nih.gov/8721982/), *Formation and activation
  by phosphorylation of activin receptor complexes*: “Phosphorylation of the GS
  domain was dependent upon a functional ActRII.” This anchors the upstream kinase
  step; receptor complex formation alone is not the chemistry.
- [PMID:25368322](https://pubmed.ncbi.nlm.nih.gov/25368322/), *Small molecules
  dorsomorphin and LDN-193189 inhibit myostatin/GDF8 signaling and promote
  functional myoblast differentiation*: full text explicitly says inhibitor
  activities “are not restricted to type I receptors but extend also to the type
  II receptors ActRIIA and ActRIIB”. It expresses human ActRIIA kinase and solves
  the inhibitor-bound structure. Thus the GO:0016361 row is a verified receptor
  class error, corrected to GO:0016362 rather than rejected from a paper title.
  QuickGO definitions checked on 2026-10-25 distinguish downstream type I
  transduction from type II ligand binding/type I phosphorylation.
- [PMID:18436533](https://pubmed.ncbi.nlm.nih.gov/18436533/), *BMP-2/4 and BMP-6/7
  differentially utilize cell surface receptors to induce osteoblastic
  differentiation of human bone marrow-derived mesenchymal stem cells*: receptor
  knockdown shows osteoinductive BMP activities use “the type II receptors ACVR2A
  and BMPR2”. Positive osteogenic annotations are retained as context-specific
  outcomes. This is distinct from activin-dependent suppression of bone formation.
- [PMID:28659341](https://pubmed.ncbi.nlm.nih.gov/28659341/), *Activin receptor type
  2A (ACVR2A) functions directly in osteoblasts as a negative regulator of bone
  mass*: conditional mouse Acvr2a deletion causes “enhanced differentiation
  indicated by alkaline phosphatase activity, mineral deposition”. The negative
  ossification transfer is independently supported; positive and negative bone
  outcomes must retain their ligand and experimental contexts.
- [PMID:19366699](https://pubmed.ncbi.nlm.nih.gov/19366699/), *Bone morphogenetic
  protein (BMP) and activin type II receptors balance BMP9 signals mediated by
  activin receptor-like kinase-1 in human pulmonary artery endothelial cells*:
  “ActR-II) contributed more to BMP9-mediated Smad2 activation.” This is direct
  human evidence for the BMP branch, despite the usual activin/SMAD2 association.
- [PMID:38334613](https://pubmed.ncbi.nlm.nih.gov/38334613/), *The Activation of the
  Fibrodysplasia Ossificans Progressiva-Inducing ALK2-R206H Mutant Depends on the
  Distinct Homo-Oligomerization Patterns of ACVR2B and ACVR2A*: human tagged-receptor
  measurements show “ACVR2A required ActA for homodimerization.” Do not import
  constitutive ACVR2B oligomerization into ACVR2A. Earlier receptor experiments
  (PMID:8612709) independently detected homomeric full-length type IIA complexes.

### PDZ-domain binding evidence

[PMID:16648306](https://pubmed.ncbi.nlm.nih.gov/16648306/) maps ARIP2 isoform
recognition to the ActRIIA C-terminal PDZ-binding motif. The direct human
fragmentomics source [PMID:36115835](https://pubmed.ncbi.nlm.nih.gov/36115835/)
does not name ACVR2A in its main text, but Supplementary Dataset 1 does.
The publisher file `41467_2022_33018_MOESM4_ESM.xlsx` was retrieved through
[Europe PMC supplementary files](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9482650/supplementaryFiles).
The `PDZ-PBM interactome` sheet contains 266 ACVR2A/P27037 rows for the natural
and assayed peptide `VDFPPKESSL`. Its `FP_aver_uM` column gives these direct
fluorescence-polarization affinities (with `FP_stdev_uM`):

| PDZ domain | Mean affinity (µM) | SD (µM) |
|---|---:|---:|
| DLG4_3 | 194.67 | 15.72 |
| SCRIB_1 | 85.41 | 2.82 |
| SNX27 | 47.52 | 4.66 |
| MAST2 | 11.51 | 0.30 |

These data substantiate the specific PDZ-binding class behind the generic binding
rows. They do not make all 266 tested pairs positive, nor establish endogenous
full-length receptor complexes for every screen hit. The review preserves those
limits and retains PDZ binding as a peripheral interaction activity.

### Uncertainty and ontology scope

The ovarian cytoplasmic localization (PMID:14738881), TSC22D1 interaction
(PMID:21791611), and source-specific ActRIIA/ActRIB interaction in PMID:8622651
require full assay inspection. Abstract emphasis on a different receptor does not
establish misattribution; these rows remain UNDECIDED. Other papers independently
establish the general ACVR2A/ACVR1B complex.

Both receptor kinase activities descend from the broad protein kinase terms.
BMP signaling descends from cellular response to BMP/growth-factor stimulus.
These checked relationships justify refinements. Activin binding is not a
descendant of growth factor binding in the checked GO hierarchy, so that binding
row was retained rather than claiming a false descendant refinement.

The IBA refinements express term granularity, not a fault in experimental donors
or a claim that PAINT performs pairwise transfer. Patterning is retained with
mouse double-mutant evidence (PMID:10452853), without equating mouse embryonic
phenotypes to a directly assayed human developmental phenotype.
