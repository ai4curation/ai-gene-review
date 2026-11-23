# ACRV1 (SP-10, P26436): does the Ly6/uPAR domain-like module support a molecular function?

Hypothesis slug: `kgap-acrv1-domain-fold`
Gene: human ACRV1 / acrosomal protein SP-10, UniProt P26436, NCBITaxon:9606
Analysis date: 2026-11-23

## Executive judgment

**Partially supported, and it splits cleanly in two.**

The structural half of the hypothesis is **supported, with high confidence**. Residues 186-265 of ACRV1 form a single, confidently folded Ly6/uPAR (LU) three-finger domain. Residues 22-185 are a disordered acidic repeat stalk with no fold information. The protein is therefore not "largely disordered with no informative fold", and it is also not a globular protein: it is 30% folded domain and 62% disorder.

The functional half of the hypothesis is **not supported**. The confident structural homologs do not converge on a molecular function. Among 99 PDB100 hits, 23 are uPAR, 20 are snake three-finger toxins, 16 are TGF-beta/BMP receptor ectodomains, 4 are C4.4A/LYPD6B, 4 are TEX101 and 2 are GPIHBP1. The highest-scoring experimental hit (GPIHBP1, TM = 0.764) is a lipase transporter; the second-largest class are nicotinic receptor antagonists. The LU fold is a reusable protein-protein interaction scaffold, so fold membership licenses no specific MF term beyond protein binding, which is not an acceptable final recommendation.

One lead survives that the Foldseek run alone did not produce, and it is weaker than it first appeared. Across 66 mammalian species the domain carries 20 invariant solvent-exposed residues that cluster on the face distal to the disulfide core (17.07 Å mean pairwise distance against a 19.27 Å null, p = 0.0022, surviving a sequence-contiguity control at p = 0.013 and a glycine/proline control at p = 0.032; 17.95 Å from the core against 12.63 Å for other exposed residues, p = 0.0013, d = 1.12).

Direct superposition then refuted the interpretation I first put on it. ACRV1 and CD59 have 10 cysteines in 1:1 topological correspondence and superpose at 1.47 Å RMSD on that ladder, so the two can be compared in a common frame. In that frame the ACRV1 patch is **not** closer to the CD59 active site (W40, R53, E56; PMID 9053451) than the other exposed residues are: 15.9 Å against 16.5 Å, p = 0.36. Distal-to-core and CD59-functional-face are two different locations on this fold. Only the C235-C239 loop overlaps, with CD59 W40 mapping onto ACRV1 E236 at 2.0 Å. Gly and Pro are also over-represented in the patch (7 of 20 against 0 of 31 for other exposed residues, Fisher p = 0.001), which is consistent with conserved backbone turn geometry and competes with the binding-site reading.

The patch is therefore a computationally defined conserved surface with explicit coordinates, worth recording as unverified, carrying no argument by analogy to CD59 and supporting no molecular function term.

Three caveats dominate.

1. **The fold assignment is not new.** Pfam PF00021 (u-PAR/Ly-6) already covers 188-264, InterPro IPR016054 covers 188-264, and CDD cd23628 (`TFP_LU_ECD_SP10_like`) covers 187-264. Palfree proposed a C-terminal Ly-6 domain in SP-10 in 1996 (PMID 8883295). The Foldseek run confirms these quantitatively and adds the disorder boundary, the disulfide map and the identity of the nearest structural neighbours, but it does not overturn or extend the existing domain call.
2. **ACRV1 differs from most of its top neighbours in a way that blocks function transfer.** uPAR, GPIHBP1, PSCA, SPACA4 and TEX101 are GPI-anchored cell-surface proteins. ACRV1 has no GPI signal (C-terminal 25 residues are 32% hydrophobic, versus the >60% over ~20 residues that GPI transamidase requires) and no transmembrane segment. It is a soluble acrosomal-lumen protein. The receptor-like interpretations carried by its neighbours do not carry over.
3. **No published assay interrogates the ACRV1 LU domain.** The one function-blocking antibody for SP-10 (mAb pep-SP10) was raised against residues 135-149, which lie inside the disordered stalk, 51 residues N-terminal to the domain (PMID 10775167).

## Key findings with statistical evidence

### 1. A single folded domain at 186-265

AlphaFold DB v6 model `AF-P26436-F1`, mean pLDDT 61.73.

| Segment | Length | Mean pLDDT | Notes |
|---|---|---|---|
| 1-21 signal peptide | 21 | 65.0 | helical, cleaved |
| 22-185 stalk | 164 | 44.62 | 95% of residues below pLDDT 50 |
| 186-265 LU domain | 80 | 96.48 | min 83.9; the only contiguous pLDDT>=70 segment in the protein |

AFDB's own summary metrics agree: `fractionPlddtVeryLow` 0.604, `fractionPlddtVeryHigh` 0.291. UniProt independently annotates 62-181 as disordered, with three nested repeat classes (S-E-H-[GA]-S x3, S-G-E-H x4, [SV]-G-E-Q-[PSA] x9).

### 2. Foldseek: the fold is LU / three-finger, unambiguously

Foldseek web server (search.foldseek.com), 3diaa mode, run 2026-11-23 against pdb100 (20240101), cath50 (4.3.0), afdb-swissprot v6 and afdb50 v6. Two queries: the isolated 186-265 model and the full-length model. TM-scores were recomputed locally from the target CA coordinates returned by the API, using an iterative TM-score refinement over the Foldseek alignment. **Control: the ACRV1 self-hit returns TM = 1.000.**

CATH50 superfamily tally over all 148 hits:

| CATH superfamily | Hits | Name |
|---|---|---|
| **2.10.60.10** | **99 (67%)** | **CD59 / snake-toxin-like, the three-finger LU fold** |
| 2.60.40.10 | 9 | immunoglobulin |
| 2.60.40.150 | 6 | C2 domain |
| all others | 1-2 each | noise |

Top experimental structures (PDB100), by locally computed TM-score, L-normalised to 80:

| PDB | Protein | TM | Foldseek E | seq id |
|---|---|---|---|---|
| 6oaz_E | GPIHBP1 bound to lipoprotein lipase | **0.764** | 7.8e-4 | 25.3% |
| 6e7k_D | GPIHBP1 | 0.726 | 6.9e-3 | 26.5% |
| 4p7u | TGFBR2 ectodomain | 0.641 | 4.5e-1 | 10.7% |
| 6mac | ActRIIB ectodomain | 0.621 | 6.8e-2 | 21.8% |
| 6gbi | LU protein in Wnt signalling | 0.621 | 4.9e-2 | 17.7% |
| 6zso | LYPD6B LU domain (NMR) | 0.605 | 7.2e-2 | 17.6% |
| 3laq | uPAR / PLAUR | 0.602 | 4.3e-1 | 25.5% |
| 3evs | BMPR-IB ectodomain | 0.590 | 2.1e-1 | 19.2% |
| 7e17, 2fd6, 1ywh | uPAR | 0.54-0.57 | | |
| 3hh7 | snake three-finger neurotoxin | 0.530 | 3.7e-2 | 20.0% |
| 6iom | C4.4A / LYPD3 | 0.522 | 3.3e-2 | 22.0% |
| 7bps | mouse TEX101 | | 1.4e-1 | 15.0% |

Every hit above the TM = 0.5 same-fold threshold is an LU/three-finger protein.

Top non-ortholog AFDB-SwissProt hits (ACRV1 orthologs P26436 isoforms, baboon Q06990, mouse P50289, fox P53353 all score TM 0.94-1.00 and are excluded): PATE14 (TM 0.941, E 3.0e-8), SLURP-family Ly-6 protein P83107 (E 2.4e-8), PIP-1 (E 8.9e-8), PATE3 (E 3.1e-7), PATE1 (E 5.7e-7), PATE4, PSCA, LY6G5B/LY6G5C/LY6G6C, GPIHBP1, **SPACA4** (human E 5.3e-3, mouse E 3.1e-3), **Bouncer** (medaka, E 2.6e-3). All 40 top non-ortholog hits are Ly6/uPAR superfamily members.

### 3. Canonical LU disulfide architecture

Computed from the P26436 sequence and the AlphaFold SG atoms.

Domain sequence (186-265):
`TILNCYTCAYMNDQGKCLRGEGTCITQNSQQCMLKKIFEGGKLQFMVQGCENMCPSMNLFSHGTRMQIICCRNQSFCNKI`

Exactly 10 cysteines (190, 193, 202, 209, 217, 235, 239, 255, 256, 262), **all 10 paired**, zero free cysteines. AlphaFold SG-SG distances: 190-217 (2.02 A), 193-202 (2.02 A), 209-235 (2.04 A), 239-255 (2.02 A), 256-262 (2.03 A). The chain terminates in `CCRNQSFCN`, matching the LU-domain diagnostic CC-x4-CN motif.

Composition contrast:

| Segment | D+E | K+R | net charge | Cys | hydrophobic | S/T/G/P/Q |
|---|---|---|---|---|---|---|
| stalk 22-185 | 19.5% | 0.6% | **-31** | 0 | 17.7% | 53.0% |
| LU 186-265 | 5.0% | 10.0% | +4 | 10 | 43.8% | 31.2% |

### 4. The LU domain is the conserved part of the protein

117 mammalian ACRV1 entries from UniProt, each aligned segment-wise to human P26436 (Needleman-Wunsch, match +4, mismatch -2, gap -8).

Mean identity to human: **LU domain 91.7%, stalk 67.0%**. Paired difference **+24.7 percentage points** (95% CI +22.7 to +26.8), Wilcoxon signed-rank **p = 1.54e-19**, paired Cohen's d = 2.16. The gap widens with distance: pig 95.0% vs 58.5%, dog 95.0% vs 51.5%, while chimp is 98.8% vs 97.5%.

Alternative splicing agrees. UniProt lists 11 isoforms of P26436; every annotated alternative-sequence event (41-224, 41-184, 41-135, 41-110, 41-95, 111-155, 121-165, 166-184, 185-224) falls in or upstream of the stalk. No isoform alters residues 225-265.

### 5. A conserved solvent-exposed patch sits on the distal face of the domain

This is the one result that goes past confirming the existing Pfam call, and it was produced by re-doing finding 4 with proper domain boundaries instead of positional ones.

Every ACRV1 ortholog that could be extracted (115 of 120 UniProt Mammalia entries) carries the identical 10-cysteine spacing, `[3,9,7,8,18,4,16,1,6]`, with zero insertions or deletions. The disulfide scaffold is therefore invariant across 66 species, and the domain can be aligned column-wise with no gap ambiguity. Mean pairwise identity is 0.889 (minimum 0.688) and 37 of 80 columns are fully invariant.

Per-residue relative solvent accessibility was computed by Shrake-Rupley (200 points, 1.4 Å probe, Tien 2013 maxima) on the isolated domain 186-265. Conservation tracks burial, as expected for a disulfide-stapled core: Spearman rho = -0.421, p = 1.02e-4; buried residues (n = 33) average 0.978 conservation against 0.888 for exposed residues (n = 47), Mann-Whitney p = 4.45e-5, Cohen's d = 0.83.

Against that background, 20 of the 47 exposed residues are invariant or near-invariant (conservation ≥ 0.95): G200, L203, G205, E206, G207, E224, G225, G226, K227, Q229, E236, N237, P240, M242, L244, S246, H247, G248, T249, R250.

Those 20 are spatially clustered, and the clustering is not an artefact of their sequence contiguity:

| Test | Observed | Null | p |
|---|---|---|---|
| Mean pairwise distance, free permutation (20000 draws of 20 exposed residues) | 17.07 Å | 19.27 ± 0.70 Å, z = -3.14 | 0.0022 |
| Same, circular-shift control preserving sequence contiguity of the conserved set | 17.07 Å | 18.92 ± 0.84 Å, 1 of 79 shifts ≤ observed | 0.013 |
| Distance from the SG centroid of the five disulfides, patch vs other exposed | 17.95 ± 5.88 Å vs 12.63 ± 3.67 Å | Mann-Whitney, d = 1.12 | 0.0013 |

The patch is one-sided (mean angular spread 56° about its centroid direction against 89° for all exposed residues; 15 of 20 within 90°) and it is built from four separate inter-cysteine loops that converge on the face distal to the disulfide core: C202-C209 (L203, G205, E206, G207), C217-C235 (E224, G225, G226, K227, Q229), C235-C239 (E236, N237) and C239-C255 (P240, M242, L244, S246, H247, G248, T249, R250). H247 is the most distal residue in the domain at 26.8 Å from the core.

### 6. The patch does not coincide with the CD59 functional face

My first reading of finding 5 was that the patch sits where LU proteins bind ligands, since CD59's active site sits on "the glycosylated, membrane-distal face of the disk-like extra-cellular domain" (PMID 9053451) and three-finger toxin function maps to "its three hydrophobic loop tips" (PMID 36927291). That inference rested on distance from the disulfide core, which is a proxy. Testing it directly refutes it.

ACRV1 and CD59 (PDB 1CDQ chain A) both have exactly 10 cysteines in 1:1 topological correspondence:

| | Cysteine ladder, relative to the first Cys |
|---|---|
| CD59 | 0, 3, 10, 16, 23, 36, 42, 60, 61, 66 |
| ACRV1 | 0, 3, 12, 19, 27, 45, 49, 65, 66, 72 |

Kabsch superposition on those 10 CA atoms gives **RMSD 1.47 Å**, so the domains can be compared in one frame. The experimentally mapped CD59 active site (W40, R53, E56, from 16 single-substitution mutants, PMID 9053451) was transformed into that frame.

| Residue set | Distance from the CD59 active site | |
|---|---|---|
| ACRV1 patch (n = 20) | 15.9 ± 4.2 Å | |
| Other exposed ACRV1 residues (n = 29) | 16.5 ± 3.8 Å | |
| | Mann-Whitney p = 0.361, Cohen's d = 0.14 | **not closer** |

Residue-centroid distances give the same answer (15.9 vs 17.0 Å, p = 0.195). Nearest-neighbour mapping shows the overlap is local and partial: CD59 W40 maps onto ACRV1 E236 at 2.0 Å and R53 onto E236 at 8.4 Å, both patch residues in the C235-C239 loop, while CD59 E56 maps onto ACRV1 M251 at 5.5 Å, which is buried and outside the patch.

Two controls on the patch itself:

| Control | Result |
|---|---|
| Exclude the 6 Gly and 1 Pro; test the remaining 13 against a null pool of non-Gly/Pro exposed residues (n = 44) | 16.52 Å vs 18.69 ± 1.11 Å, p = 0.0316. **Clustering is not a glycine artifact** |
| Gly/Pro composition, patch vs other exposed | 7/20 vs 0/31, Fisher exact p = 0.001, OR infinite. **Patch is Gly/Pro enriched** |

The glycine enrichment cuts against the binding-site reading. A surface built partly from invariant glycines and a proline is consistent with conserved backbone turn geometry holding the loops in place, which is a structural explanation for the conservation competing with a functional one.

What finding 5 still licenses after this: a conserved, clustered, solvent-exposed surface exists at defined coordinates (the C239-C255 loop P240-R250, with E206, E224 and E236 giving it acidic character), and it survives three independent controls. What it no longer licenses: any argument by analogy to CD59's binding mode. It names no ligand and supports no GO molecular function term.

## Evidence matrix

| Citation | Evidence type | Direction | Claim tested | Key finding | Context | Confidence and limitations |
|---|---|---|---|---|---|---|
| This analysis, Foldseek run 2026-11-23 (`provenance/acrv1/foldseek_hits_all.tsv`) | Computational / structural | **Supports** | ACRV1 contains a folded LU-like module | 186-265 mean pLDDT 96.5; 67% of CATH hits in 2.10.60.10; TM 0.764 vs GPIHBP1 6oaz; self-hit control TM = 1.000 | AlphaFold DB v6 model, no experimental ACRV1 structure exists | High for fold assignment. Query is a prediction, not an experimental structure. Foldseek E-values for short 80-residue queries are weak (1e-4 to 1e-1); the fold call rests on the convergent CATH tally and TM-scores, not on E-value alone |
| This analysis, 10 Cys / 5 disulfides / `CCRNQSFCN` | Computational / sequence | Supports | The module is a genuine LU domain, not a chance fold match | All 10 Cys paired, canonical CC-x4-CN terminus | P26436 sequence + AlphaFold SG atoms | High. Disulfide pairing is AlphaFold-predicted, not experimentally mapped |
| PMID 8883295 (Palfree 1996) | Review / sequence analysis | Supports, and pre-dates | A C-terminal Ly-6 domain exists in SP-10 | Title-level claim; no abstract available in PubMed | Sequence analysis | Moderate. Shows the fold call is 30 years old, so Foldseek confirms rather than discovers |
| Pfam PF00021 188-264, InterPro IPR016054, CDD cd23628 187-264 | Database | Supports, and pre-dates | LU domain boundaries | Boundaries agree with the pLDDT-defined 186-265 to within 2 residues | Automated HMM/PSSM annotation on P26436 | High for concordance; database-level support only |
| PMID 18508598 (Kjaergaard 2008) | Review | **Qualifies** | What an LU domain implies | "These domains belong to the Ly-6/uPAR (LU) protein domain family, which is defined by a consensus sequence predominantly based on disulfide connectivities, and they adopt a characteristic three-finger fold" and uPAR sits in "a cluster of 6 homologous genes encoding proteins with multiple LU-domains" | Human uPAR structural biology | High. Establishes LU as a reused scaffold, blocking fold-to-function transfer |
| This analysis, functional tally of 99 PDB100 hits | Computational | **Refutes** the function clause | Structural homologs suggest a molecular function | 23 uPAR, 20 snake toxins, 16 TGF-beta/BMP receptor ectodomains, 4 C4.4A/LYPD6B, 4 TEX101, 2 GPIHBP1; no class above 23% | PDB100 | High. Classification by target title keyword; 29/99 left unclassified |
| This analysis, GPI check | Computational | **Qualifies** | ACRV1 is a receptor-like LU protein as its top hits are | C-terminal 25 aa only 32% hydrophobic; no GPI site or TM segment in UniProt | P26436 | Moderate-high. Negative prediction, not an experimental test of membrane attachment |
| PMID 10775167 (Hamatani 2000) | Direct assay (antibody blocking) | **Qualifies / competing** | SP-10 mediates sperm-oolemma binding | mAb against "the 135th and 149th amino acids" blocked sperm-oolemma binding in the hamster egg penetration test but not sperm-zona binding in the hemizona assay; oolemmal ligand is not a beta1 integrin | Human sperm, zona-free hamster oocytes | Moderate for the phenotype. **The epitope lies in the disordered stalk, not in the LU domain**, so this does not test the folded module |
| PMID 7888499 (Foster 1994) | Localization / biochemistry | Qualifies | The stalk and the LU domain stay on one polypeptide | 45 kDa testis precursor processed to 32/30/28/26 kDa, then 25-18 kDa from caput epididymal sperm onward | Human testis and epididymal sperm | Moderate. Shows mature sperm carry fragments; which fragment carries the LU domain was not mapped |
| PMID 34556579 (Fujihara 2021) | Mutant phenotype | Competing / contextual | A sperm LU protein has a defined fertilisation role | "Male knockout mice are severely subfertile, and sperm lacking SPACA4 fail to fertilize wild-type eggs in vitro"; rescued by removing the zona | Mouse Spaca4 knockout | High for SPACA4. SPACA4 is a structural neighbour (E 3.1e-3), not ACRV1; no transfer licensed |
| PMID 22402205 (Margalit 2012) | Direct assay (antibody blocking) | Supports a scaffold-binding reading | PATE-like proteins, "homologous to SP-10, the acrosomal vesicle protein also named ACRV1", act in gamete interaction | Anti-PATE left hemizona index at 89.6 +/- 10% and 87 +/- 36%, but cut hamster egg penetration index from 7 +/- 3.9 to 0.6 +/- 1.2 (P < 0.001) | Human sperm, 95 testis biopsies | Moderate. PATE14 is the top non-ortholog structural neighbour (TM 0.941). Same oolemma-not-zona pattern as SP-10 |
| This analysis, 117 mammalian orthologs | Structural / evolutionary | Supports domain primacy | The LU domain, not the stalk, is constrained | LU 91.7% vs stalk 67.0% identity, +24.7 pp, Wilcoxon p = 1.54e-19, d = 2.16 | UniProt Mammalia | Moderate-high. Primate-heavy sample; ortholog segment boundaries set positionally (C-terminal 85 aa) rather than by HMM alignment |
| This analysis, 66-species gap-free domain alignment (`provenance/acrv1_lu_conservation_sasa.tsv`) | Computational / evolutionary | Supports a candidate interface | The LU domain has a conserved surface, not only a conserved core | 115/115 orthologs share Cys spacing [3,9,7,8,18,4,16,1,6] with zero indels; conservation vs rSASA rho = -0.421, p = 1.0e-4; 20 invariant exposed residues cluster at 17.07 Å vs null 19.27 ± 0.70 Å (p = 0.0022), surviving a sequence-contiguity control (p = 0.013) | UniProt Mammalia, 66 species, one per species | Moderate. Mammals only at 88.9% mean identity, so low divergence limits power; the shift-control p sits at the 1/79 resolution floor; rSASA from an AlphaFold model of the excised domain |
| This analysis, patch geometry (`provenance/acrv1_lu_patch_table.tsv`) | Computational / structural | Supports a candidate interface | The conserved surface occupies the ligand-binding face of the LU fold | Patch 17.95 ± 5.88 Å from the disulfide core vs 12.63 ± 3.67 Å for other exposed residues (p = 0.0013, d = 1.12); drawn from four inter-cysteine loops; one-sided (56° vs 89° angular spread) | AF-P26436-F1-model_v6, residues 186-265 | Moderate. Geometry is internally consistent and matches the LU paradigm, but no ligand is identified and no experimental structure exists |
| PMID 9053451 (Bodian 1997) | Direct assay (mutagenesis) | Qualifies / contextual | Where LU-domain function maps on the fold | "CD59 has a single active site that includes Trp-40, Arg-53, and Glu-56 of the glycosylated, membrane-distal face of the disk-like extra-cellular domain" | 16 single-substitution CD59 mutants | High for CD59. Supplies the reference site used in the superposition test below |
| This analysis, CD59 superposition (`provenance/acrv1_cd59_superposition.tsv`) | Computational / structural | **Refutes** the fold-equivalence reading of the patch | The ACRV1 patch occupies the face that carries the CD59 active site | ACRV1 and CD59 1CDQ superpose at 1.47 Å RMSD on 10 topologically corresponding cysteines, but patch residues are 15.9 ± 4.2 Å from the CD59 active site vs 16.5 ± 3.8 Å for other exposed residues (p = 0.361, d = 0.14). Only E236/N237 overlap; CD59 W40 maps to ACRV1 E236 at 2.0 Å | AF-P26436-F1-model_v6 vs experimental CD59 NMR structure | High for the negative. Single comparator; CD59's site is one LU functional site among several possible ones, so this refutes the CD59-specific analogy rather than every binding-site hypothesis |
| This analysis, glycine control | Computational | Qualifies | The patch clustering is an artifact of conserved glycines | Excluding 6 Gly and 1 Pro, the remaining 13 residues still cluster (16.52 vs 18.69 ± 1.11 Å, p = 0.0316), but Gly/Pro are enriched 7/20 vs 0/31 (Fisher p = 0.001) | ACRV1 domain 186-265 | High. The clustering survives, but the Gly/Pro enrichment supplies a competing backbone-geometry explanation for part of the conservation |
| PMID 36927291 (Misuan 2023) | Computational / biophysical | Contextual | Where three-finger function maps on the fold | "The functional site of the toxin is located at its three hydrophobic loop tips." | Cobra cytotoxin docking and fluorescence titration | Moderate. Review-level statement of an established fact about three-finger toxins, used only for fold geometry |
| IMPC `genotype-phenotype` query, marker_symbol:Acrv1 | Database | Gap | A mouse knockout phenotype exists | 0 phenotype records; gene status "Selected for production" | IMPC | High that no IMPC data exist today |
| PMID 9241046 (Olson 1997) | Localization / biochemistry | Contextual | SP-10-related protein in the acrosomal matrix | Bovine OMC32 N-terminal sequence "indicated a structural relationship to the SP-10 polypeptide"; localises to the stable matrix, not released at the acrosome reaction | Bovine ejaculated sperm | Moderate. Supports a matrix-resident, non-membrane role, consistent with the absent GPI anchor |

## GO curation implications

**All items below are leads requiring curator verification.**

| GO aspect | Candidate term | Suggested action | Reasoning |
|---|---|---|---|
| **MF** | none | **Do not add an MF term on the basis of this analysis.** | The LU fold supports only `protein binding` (GO:0005515), which is excluded as a final recommendation. No homolog class reaches a majority, and the one highest-TM neighbour (GPIHBP1, a GPI-anchored lipase transporter) is mechanistically inapplicable to a soluble acrosomal protein. P26436 currently has no MF term; that is the correct state given present evidence. |
| **CC** | GO:0001669 acrosomal vesicle | **Retain.** IDA from HPA, consistent with UniProt's "Nascent acrosomal vesicle of Golgi phase spermatids". | Unaffected by this analysis. |
| **CC** | GO:0005737 cytoplasm, GO:0031982 vesicle | **Treat as non-core.** Both are IBA and strictly less informative than GO:0001669. | Generalisations of an already-annotated, better-supported term. |
| **BP** | GO:0007283 spermatogenesis | **Weak, flag for review.** Current evidence code is NAS. | Expression is spermatid-specific (PMID 31290539, 8373955), but expression is not participation. No Acrv1 mutant phenotype exists (IMPC: 0 records). A cleaner alternative, if the curator wants a BP term, is to downgrade to a CC-plus-expression statement and leave BP unannotated. |
| **BP** | GO:0007342 fusion of sperm to egg plasma membrane, or GO:0035036 sperm-egg recognition | **Do not add.** | The supporting data (PMID 10775167) is antibody inhibition against a stalk epitope in a heterologous zona-free hamster assay, with no mutant phenotype and no identified ligand. This is below the bar for a BP term, and it would in any case be a cell-level phenotype, not the gene product's direct activity. |
| **Domain annotation (non-GO)** | LU / Ly6-uPAR domain, residues 186-265 | **Add or confirm as a structural statement in the review.** | Supported here at TM 0.76 against an experimental structure, 67% CATH concordance, 10 Cys / 5 disulfides, CCxxxxCN terminus, and 91.7% ortholog identity. It agrees with Pfam PF00021 (188-264) to within 2 residues. Worth stating explicitly that residues 22-185 are disordered, because that is the part that review text and assay design have historically treated as functional. |
| **Sequence feature (non-GO)** | Conserved surface patch on the distal face: G200, L203, G205, E206, G207, E224, G225, G226, K227, Q229, E236, N237, P240, M242, L244, S246, H247, G248, T249, R250 | **Record as a candidate interface in the review's free text, flagged as computational and unverified.** | 20 invariant exposed residues clustering at 17.07 Å against a 19.27 Å null (p = 0.0022), surviving a sequence-contiguity control (p = 0.013) and a glycine/proline control (p = 0.032), and sitting 17.95 Å from the disulfide core against 12.63 Å for other exposed residues (p = 0.0013, d = 1.12). Record the coordinates, and record with them that the patch does **not** coincide with the CD59 active-site face on direct superposition (p = 0.361) and is Gly/Pro enriched (Fisher p = 0.001), so it carries no analogy-based functional argument. It is not evidence for an MF term. |

The net curation outcome: this hypothesis **should not change any GO term**. It should change the review's free text, by replacing any implication that ACRV1 is an unstructured acrosomal protein, or that its LU domain implies a receptor-like function, with the specific two-part architecture, an explicit statement that the fold is not function-diagnostic, and the coordinates of the conserved surface that any future binding claim should be required to engage.

## Mechanistic scope

**Direct gene-product property being tested:** whether the ACRV1 polypeptide folds, and if so into what. Answer: residues 186-265 fold into a disulfide-stapled LU three-finger module; residues 22-185 do not fold. This is a property of the protein, established computationally.

**Immediate molecular function implied:** at most, presentation of a rigid protein-binding surface. LU domains have no intrinsic catalytic activity; the three fingers are a binding platform. ACRV1 lacks the GPI anchor that converts that platform into a cell-surface receptor in uPAR, GPIHBP1, PSCA, SPACA4 and TEX101, so the platform is displayed from the acrosomal lumen on a 164-residue acidic tether.

**Where on the protein that surface is:** the 20 invariant exposed residues of finding 5 occupy the face distal to the disulfide core, built from four inter-cysteine loops, at P240-R250 plus E206, E224, E236, K227, Q229 and H247. Finding 6 shows this face is not the one carrying the CD59 active site, so the position is defined by ACRV1's own conservation pattern and not by homology to a characterised site. This is a positional claim about where a binding site would be if one exists. It does not establish that one does, and the glycine and proline enrichment means part of the conservation is explained by backbone geometry.

**Separated from the above, not established:**
- Sperm-oolemma binding (PMID 10775167) is a cell-level phenotype measured by antibody inhibition against a stalk epitope. It is downstream of, and not attributable to, the LU domain.
- Participation in fertilisation is inferred from homolog knockouts (SPACA4, PMID 34556579) and from paralog antibody blocking (PATE, PMID 22402205). Neither is ACRV1 evidence.
- Acrosomal matrix structural roles (PMID 9241046, bovine OMC32) are inferred from an N-terminal sequence relationship, not from ACRV1 itself.
- No ligand, no binding partner with a defined interface, and no mutant phenotype are known for ACRV1 in any species. The two IntAct partners listed by UniProt (CISD2, PANK2) are cytoplasmic and mitochondrial proteins reported from a high-throughput screen, topologically incompatible with a secreted acrosomal protein, and should be treated as artefacts.

## Conflicts and alternatives

1. **The fold-to-function inference competes with itself.** uPAR and GPIHBP1 argue for high-affinity capture of a protein ligand; snake three-finger toxins and SLURP/LYPD6 argue for receptor modulation; TGF-beta/BMP receptor ectodomains argue for growth-factor binding. These are mutually exclusive readings of the same scaffold. The seed hypothesis implicitly assumes convergence that the data do not show.

2. **Paralog carry-over risk is real and runs both ways.** PATE1/PATE2/PATE3/PATE4/PATE14 are described in the literature as "homologous to SP-10" (PMID 22402205) and are this analysis's top non-ortholog structural neighbours. Functional claims about SP-10 and about PATE proteins have the same shape (anti-X blocks oolemma penetration, not zona binding) and are at risk of being read as corroborating each other when they are two instances of the same weak assay design.

3. **Isoform and processing confusion.** P26436 has 11 isoforms, and human SP-10 is processed from 45 kDa to species as small as 18 kDa (PMID 7888499). An 18 kDa fragment cannot contain both the 164-residue stalk and the 80-residue domain. Published antibody results do not state which fragment carries the epitope, so assay readouts cannot be assigned to a defined molecular species.

4. **The 135-149 epitope conflict.** The main functional claim about SP-10 rests on an epitope that this analysis places in a region with mean pLDDT 44.6 and net charge -31. Antibody binding to a long acidic disordered tether can block adhesion sterically or by charge, without the tether itself being a binding determinant. This is an alternative explanation of PMID 10775167 that the original study could not exclude.

5. **Organism-specific difference in the closest functional comparator.** Bouncer is egg-expressed in fish; its mammalian ortholog SPACA4 is sperm-expressed (PMID 34556579). The same LU protein changes which gamete it sits on. This is direct evidence that LU-domain sperm proteins do not retain function or even cellular context across lineages, and it further weakens homolog-based transfer to ACRV1.

6. **One database mis-assignment worth noting.** The single best CATH50 hit, the mouse ACRV1 ortholog, is deposited as `af_P50289_184_259_2.40.10.10`, i.e. assigned to the trypsin-like serine protease superfamily. Every other ACRV1-like hit is 2.10.60.10. The 2.40.10.10 label on the mouse ortholog is an automated CATH-AlphaFold error and should not be propagated into any curation statement about ACRV1 having a protease-related fold.

## Knowledge gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No experimental structure of ACRV1 | UniProt cross-references list no PDB entry for P26436 | The entire fold call rests on one AlphaFold model. pLDDT 96.5 makes misfolding unlikely, but the disulfide pairing in particular is predicted, not observed | A crystal or NMR structure of residues ~180-265, or mass-spectrometric disulfide mapping of recombinant or sperm-derived SP-10 |
| No binding partner for the LU domain | UniProt IntAct partners (CISD2, PANK2) are topologically implausible; PubMed searches for SP-10 ligands returned only antibody-inhibition studies | Without a partner, no MF term above `protein binding` can ever be justified | Pull-down or BioID from acrosomal fractions using the isolated 186-265 domain as bait; AlphaFold-Multimer screen of the domain against the oolemmal and zona proteomes |
| No loss-of-function phenotype | IMPC `genotype-phenotype` for Acrv1 returns 0 records (status "Selected for production"); PubMed returned no Acrv1 knockout | The BP term GO:0007283 is NAS-supported only, and nothing anchors ACRV1 to fertilisation causally | An Acrv1 knockout mouse with fertility, IVF, zona-binding and oolemma-fusion readouts; the SPACA4 study (PMID 34556579) is the template |
| Which processed fragment carries the LU domain | PMID 7888499 reports sizes but not epitope or domain mapping of the 32-18 kDa species | Determines whether the folded domain is present on mature sperm at the time of the acrosome reaction, and whether it is still attached to the stalk | N-terminal sequencing or LC-MS/MS of the 25-18 kDa sperm species, probed with a domain-specific antibody |
| Whether the 135-149 antibody effect is domain-independent | Mapped the epitope onto the disorder profile; the original study did not test domain constructs | The single most-cited functional claim about SP-10 may not be about the functional part of SP-10 | Repeat the hamster egg penetration test with a domain-directed (186-265) antibody and with recombinant domain alone as a competitor |
| Whether the acidic stalk has a function of its own | Composition computed (net -31, 0 Cys, 53% S/T/G/P/Q); conservation measured (67% vs 91.7%) | If the stalk is a Ca2+-buffering or matrix-assembly element rather than a spacer, that is a separate curation statement | Calcium-binding assays on the isolated stalk; test whether stalk deletion affects acrosomal matrix incorporation |

## Discriminating tests

Ranked by how efficiently they separate the live alternatives.

1. **AlphaFold-Multimer or Foldseek-Multimer screen of ACRV1 186-265 against the zona pellucida proteins (ZP1-ZP4), the oolemmal surface proteome (JUNO/FOLR4, CD9, IZUMO1R), and the acrosomal matrix proteins (ACRBP, ZPBP, SPACA1, SPACA4).** This is cheap, directly targets the one gap that blocks an MF term, and discriminates between "ACRV1 binds an egg ligand" and "ACRV1 is a matrix structural component". A confident interface prediction would convert the current `protein binding`-only ceiling into a specific binding MF. Finding 5 supplies a weak prior on where to look (the conserved distal-face patch, P240-R250 plus E206, E224, E236), but finding 6 shows that prior should not be enforced as an acceptance criterion: the patch does not occupy the CD59 functional face, so a predicted interface elsewhere on the domain is not automatically wrong. Score predictions on interface quality first and on patch overlap second.

1b. **Alanine or charge-reversal scanning, patch versus a matched off-patch control set.** E206A, E224A, E236A, K227A, R250A and H247A, against an equal number of exposed non-patch residues, assayed for whatever binding activity test 1 or test 2 identifies. The control set matters because finding 6 leaves open that the patch is conserved for backbone geometry. Scanning the patch alone cannot distinguish a binding surface from a conformationally constrained one; scanning both can.
2. **Recombinant domain competition in the zona-free hamster penetration assay.** If purified 186-265 competes with sperm for oolemma binding but the recombinant stalk does not, the LU domain carries the adhesion function and PMID 10775167 was reading a steric effect. If neither competes, the SP-10 adhesion claim should be downgraded in the review.
3. **Acrv1 knockout mouse, or the existing IMPC line once produced, phenotyped for fertility, IVF with and without zona, and oolemma fusion.** This is the only test that can support a BP term. The SPACA4 result (PMID 34556579) shows exactly which readouts discriminate a zona-penetration defect from an oolemma-fusion defect.
4. **Disulfide mapping of sperm-derived SP-10 by non-reducing LC-MS/MS.** Confirms or refutes the five predicted bonds and, at the same time, tells you which processed fragment the domain sits on. Two gaps closed by one experiment.
5. **Domain-swap or Cys-mutant rescue.** Replacing the ACRV1 LU domain with the SPACA4 LU domain, or breaking the 190-217 disulfide, in a transgenic rescue of an Acrv1 null would test whether the fold itself (rather than the protein's presence) is required.
6. **Per-site dN/dS across the mammalian orthologs, using the gap-free codon alignment that finding 5 makes available.** The identity contrasts reported here (91.7% vs 67.0% by segment; 0.978 vs 0.888 conservation by burial) are not selection tests. Because all 115 orthologs share identical cysteine spacing with zero indels, the domain codon alignment is unambiguous, so site-model dN/dS can be run directly. The informative outcome is whether the distal-face patch is under purifying selection (dN/dS well below 1, consistent with a maintained interface) or whether the finger tips carry positively selected sites as Bouncer does (PMID 37316475), which would point at a gamete-recognition interface under antagonistic coevolution. Extending the alignment beyond Mammalia would supply the divergence that the present 88.9%-identity sample lacks.

## Curation leads

All items are leads requiring curator verification.

**Candidate references, with exact snippets to verify:**

- PMID 18508598, Kjaergaard et al. 2008: "These domains belong to the Ly-6/uPAR (LU) protein domain family, which is defined by a consensus sequence predominantly based on disulfide connectivities, and they adopt a characteristic three-finger fold." Use for the domain-architecture statement and for the argument that LU membership does not imply a function.
- PMID 10775167, Hamatani et al. 2000: "We therefore established a monoclonal antibody (mAb pep-SP10) against a peptide (pep-SP10) that included the most hydrophilic portion of human SP-10 between the 135th and 149th amino acids." and "Monoclonal Ab pep-SP10 inhibited sperm-oolemma binding in the zona-free hamster egg penetration test, but it did not inhibit sperm-zona binding in the hemizona assay." Use to qualify, not support, any adhesion claim.
- PMID 7888499, Foster et al. 1994: "These results indicate that a full-length 45-kDa SP-10 precursor protein is present in the testis and that SP-10 peptides of 32, 30, 28, and 26 kDa result from proteolytic processing of the SP-10 precursor protein in the testis and/or alternative splicing."
- PMID 34556579, Fujihara et al. 2021: "Male knockout mice are severely subfertile, and sperm lacking SPACA4 fail to fertilize wild-type eggs in vitro." Use as comparator for what ACRV1 evidence would need to look like, explicitly labelled as about SPACA4.
- PMID 22402205, Margalit et al. 2012: "They are localized in the sperm head and are homologous to SP-10, the acrosomal vesicle protein also named ACRV1." Use when discussing paralog overannotation risk.
- PMID 9241046, Olson et al. 1997: "N-terminal sequence analysis of OMC32 indicated a structural relationship to the SP-10 polypeptide". Use for the acrosomal-matrix context, labelled as bovine and as a sequence relationship only.
- PMID 8883295, Palfree 1996, "Ly-6-domain proteins--new insights and new members: a C-terminal Ly-6 domain in sperm acrosomal protein SP-10." No abstract is available in PubMed, so the curator must check the full text before citing it as the origin of the domain call.
- PMID 9053451, Bodian et al. 1997: "Analysis of 16 CD59 mutants with single, highly nonconservative substitutions suggests that CD59 has a single active site that includes Trp-40, Arg-53, and Glu-56 of the glycosylated, membrane-distal face of the disk-like extra-cellular domain". Use only to state where function maps on an LU fold, explicitly labelled as about CD59.
- PMID 9075580, Petranka et al. 1996: "the members of the superfamily have a similar structure that includes four (in mammals five) disulfide bridges that maintain a three-dimensional conformation consisting of a central core, three finger-like "loops" extending from it and a small loop near the coboxyl end". Use for the architecture statement; ACRV1 matches with five disulfides.

**Candidate GO actions:**

- MF: add nothing. Record in the review that the LU fold was tested and found non-diagnostic.
- CC GO:0001669 acrosomal vesicle: retain, IDA.
- CC GO:0005737, GO:0031982: mark non-core (IBA generalisations).
- BP GO:0007283 spermatogenesis: flag as NAS-only, no mutant phenotype available. Consider demoting to non-core pending an Acrv1 knockout.
- Do not add GO:0007342 or GO:0035036.

**Suggested questions for the curator:**

1. Does the review currently assert or imply a receptor-like or ligand-binding function for ACRV1 on the basis of the Ly6/uPAR domain? If so, it should be qualified with the functional heterogeneity shown here and with the absent GPI anchor.
2. Does the review cite PMID 10775167 as functional support? If so, note that the epitope is at 135-149, outside the LU domain.
3. Should the two IntAct partners (CISD2, PANK2) be explicitly marked as high-throughput artefacts, given the topological incompatibility with a secreted acrosomal protein?

**Suggested experiments:** items 1-4 under Discriminating Tests, in that order.

## Supported and refuted hypotheses

| Hypothesis | Verdict |
|---|---|
| ACRV1 contains a folded LU domain-like module | **Supported.** Residues 186-265, mean pLDDT 96.5, 67% CATH 2.10.60.10, TM 0.764 vs GPIHBP1, 10 Cys / 5 disulfides, CCxxxxCN terminus |
| ACRV1 is largely disordered with no informative fold | **Refuted as stated, partly true.** 62% of the chain (22-185) is disordered, but the remaining 30% is a well-defined, highly conserved domain |
| Structural homologs of ACRV1 suggest a molecular function | **Refuted.** Homologs span protease receptors, lipase transporters, growth-factor receptor ectodomains and ion-channel toxins; no class exceeds 23% of hits |
| The folded domain is the functionally constrained part of ACRV1 | **Supported.** 91.7% vs 67.0% ortholog identity, +24.7 pp, p = 1.54e-19, d = 2.16; excluded from all 9 annotated alternative-splicing events |
| ACRV1 is a GPI-anchored cell-surface LU receptor like uPAR, GPIHBP1 or SPACA4 | **Refuted.** C-terminal 25 aa only 32% hydrophobic; no GPI site or TM segment; UniProt places it in the acrosomal vesicle lumen |
| The domain is conserved only for folding, so its surface carries no functional constraint | **Refuted.** Conservation does track burial (rho = -0.421, p = 1.0e-4, d = 0.83), but 20 exposed residues are invariant and clustered beyond both a free permutation null (p = 0.0022) and a sequence-contiguity control (p = 0.013) |
| The patch clustering is an artifact of conserved glycines | **Refuted.** The 13 non-Gly/Pro patch residues still cluster against a non-Gly/Pro null pool (16.52 vs 18.69 ± 1.11 Å, p = 0.0316), though Gly/Pro are enriched 7/20 vs 0/31 (Fisher p = 0.001) |
| The conserved exposed residues sit where LU proteins bind ligands, i.e. on the CD59 active-site face | **Refuted.** After a 1.47 Å RMSD superposition on 10 topologically matched cysteines, patch residues are no closer to the CD59 active site than other exposed residues (15.9 vs 16.5 Å, p = 0.361, d = 0.14). Only E236 and N237 overlap |
| The conserved patch identifies ACRV1's molecular function | **Unresolved, and weaker than finding 5 alone suggested.** It localises a conserved surface but names no ligand, carries no homology-based functional argument, and has a competing backbone-geometry explanation. Discriminating tests 1, 1b and 6 would resolve it |

## Limitations

The query structure is an AlphaFold prediction, not an experimental model, and no experimental structure of ACRV1 exists in any species. Foldseek E-values for an 80-residue query are weak in absolute terms (best PDB hit 7.8e-4); the fold conclusion rests on the convergence of the CATH superfamily tally, the recomputed TM-scores and the independent 10-Cys/CCxxxxCN sequence signature, rather than on any single statistic. The functional classification of the 99 PDB hits used target-title keywords and left 29 unclassified.

The finding-4 ortholog analysis used positional segment boundaries (C-terminal 85 aa) rather than aligned domain boundaries, and its 117-entry sample is primate-heavy, so its absolute identity figures are approximate; the direction and magnitude survive because the largest gaps come from the most distant species. Finding 5 repeats the conservation analysis without those two defects, using cysteine-anchored domain boundaries and one sequence per species.

Finding 5 carries three limitations of its own. The 66 species are all mammals and the domain alignment is 88.9% identical on average, so divergence is low and the power to separate purifying selection from insufficient elapsed time is limited; a dN/dS test on a deeper taxon sample is the proper version of this analysis. The circular-shift control has only 79 possible shifts, so its p-value of 0.013 is the smallest the test can return and should be read as "survives the control" rather than as a precise probability. Relative solvent accessibility was computed on an AlphaFold model of the domain excised from a protein whose N-terminal 185 residues are disordered, so residues scored as exposed here may be occluded in vivo by the stalk, by processing intermediates or by the acrosomal matrix.

The CD59 superposition test of finding 6 used a single comparator. CD59's active site is one LU functional site among several that different family members use, so the negative result refutes the CD59-specific analogy and does not exclude every binding-site hypothesis for the ACRV1 patch. Superposing against uPAR, GPIHBP1 and a three-finger toxin with mapped functional residues would generalise it. The superposition anchored on 10 cysteine CA atoms rather than a full structural alignment; the 1.47 Å RMSD indicates the anchor is sound, but a full alignment could shift individual residue correspondences.

Disulfide pairings are AlphaFold-predicted. No wet-lab data were generated.

## Provenance

| File | Contents |
|---|---|
| `provenance/acrv1/AF-P26436-F1-model_v6.pdb` | AlphaFold DB v6 model used as query |
| `provenance/acrv1/AF-P26436-F1-predicted_aligned_error_v6.json` | PAE matrix |
| `provenance/acrv1/ACRV1_dom186_265.pdb` | Isolated folded domain used as the second query |
| `provenance/acrv1/plddt_P26436.json` | Per-residue pLDDT |
| `provenance/acrv1/foldseek_hits_all.tsv` | All 2867 Foldseek hits, both queries, 4 databases, with E-value, identity, alignment span |
| `provenance/acrv1/foldseek_domain_nocoords.json`, `foldseek_full_nocoords.json` | Raw Foldseek API responses, coordinates stripped |
| `provenance/plot_1.png` | pLDDT profile and TM-scores vs experimental structures |
| `provenance/plot_2.png` | Functional classes of structural neighbours; domain map with the mAb epitope |
| `provenance/plot_3.png` | Paired ortholog conservation, LU domain vs stalk |
| `provenance/acrv1_lu_conservation_sasa.tsv` | Per-residue table for 186-265: amino acid, Shannon entropy, conservation across 66 species, absolute and relative SASA, exposed flag |
| `provenance/acrv1_lu_patch_table.tsv` | Same table plus residue centroid coordinates, distance from the disulfide-core centroid, inter-cysteine loop assignment and patch membership |
| `provenance/plot_4.png` | Conservation vs solvent accessibility; per-residue conservation with cysteine ladder; free-permutation null for patch clustering |
| `provenance/plot_5.png` | Free-permutation and circular-shift nulls side by side; domain projection coloured by conservation, sized by exposure, patch ringed |
| `provenance/plot_6.png` | Conservation vs distance from the disulfide core by inter-cysteine loop; per-residue distance from core with cysteine ladder |
| `provenance/acrv1_cd59_superposition.tsv` | ACRV1 186-265 residues with coordinates transformed into the CD59 1CDQ frame, distance from the CD59 active site, exposure and patch membership |
| `provenance/plot_7.png` | Glycine/proline control null; patch vs other exposed distance from the CD59 active site; ACRV1 projected into the CD59 frame with the active site marked |

Each `provenance/plot_N.json` carries the full executed source for the corresponding figure under its `code` key, alongside the description and timestamp, so every number in this report can be regenerated from the saved code rather than from the figure alone.

Foldseek job tickets (search.foldseek.com, 2026-11-23): domain query `yXBid0PUXggiyh_CgkcU8h_2_2K-7mKqCsythw`, full-length query `iEwgWme4NlLqNS__gE61CcaJX97I9T6M3qaoJA`.
