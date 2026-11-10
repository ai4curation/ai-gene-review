# daf-7 (C. elegans, UniProt P92172) - manual literature synthesis

No deep-research provider API was available for this review, so this summary was
assembled by hand from the cached publications in `publications/` and PubMed
searches. Every assertion carries a provenance tag; quotes are verbatim from the
cached record.

## Identity and family

- daf-7 (B0412.2, WBGene00000903) encodes a 350-aa TGF-beta superfamily
  precursor ("Belongs to the TGF-beta family", UniProt P92172). The
  characteristic C-terminal cysteine-knot ligand domain follows a prodomain;
  dominant-negative transgenes mutating the conserved pre-protein cleavage site
  and ligand-domain residues show that the canonical TGF-beta processing logic
  applies [PMID:23526825 "TGF-β ligands are widely divergent yet retain a set of
  core conserved features, specifically, a pre-protein cleavage site and several
  conserved ligand domain residues, the disruption of which produces a dominant
  negative phenotype"].
- Cloning paper: [PMID:8910282 "daf-7 gene, required for transducing
  environmental cues that support continuous development with plentiful food,
  encodes a transforming growth factor-beta (TGF-beta) superfamily member"].

## Expression and secretion

- Expressed in the ASI chemosensory neuron pair [PMID:8893028 "We find that
  daf-7::GFP fusions are expressed specifically in ASI and that expression is
  regulated by dauer-inducing sensory stimuli"].
- Pheromone represses and food activates transcription [PMID:8910282
  "Dauer-inducing pheromone inhibits daf-7 expression and promotes dauer
  formation, whereas food reactivates daf-7 expression and promotes recovery from
  the dauer state"].
- Transcriptional inputs in ASI: DAF-11 guanylyl cyclase / cGMP [PMID:11677050
  "daf-11 acts cell autonomously in ASI chemosensory neurons for daf-7
  expression"]; CREB/CRH-1 binds a CRE in the daf-7 promoter [PMID:34260587
  "CRH-1 directly binds upstream of the daf-7 TGF-β locus and promotes its
  expression in the ASI neurons"]; ascaroside icas#9 via SRX-43 [PMID:27799655
  "Expression of a daf-7::GFP reporter was significantly reduced by icas#9
  treatment"].
- Induced in ASJ by Pseudomonas aeruginosa secondary metabolites via GPA-2/GPA-3
  [PMID:25303524 "Secondary metabolites phenazine-1-carboxamide and pyochelin
  activate a G-protein-signaling pathway in the ASJ chemosensory neuron pair that
  induces expression of the neuromodulator DAF-7/TGF-β"], and male-specifically
  in ASJ, downstream of PDF-1 [PMID:30024377].
- Secreted: DAF-7::mCherry is taken up by coelomocytes, the scavenger cells that
  endocytose body-cavity fluid [PMID:26218657 "DAF-7::mCherry was hardly detected
  in ASI neurons (Fig 6a and 6c), and it accumulated in the coelomocytes of
  wild-type animals at the adult stage"].

## Receptors and signal transduction

- Signals through the type I receptor DAF-1 and the type II receptor DAF-4 to the
  R-Smads DAF-8/DAF-14, antagonising the Co-Smad DAF-3 and the Sno/Ski DAF-5
  [PMID:32182864 "the TGFβ homolog DAF-7 signals through the DAF-1 Type I and
  DAF-4 Type II receptors to phosphorylate downstream R-SMADs DAF-8 and DAF-14"].
  DAF-4 is the sole type II receptor and is shared with the DBL-1 BMP-like pathway;
  DAF-4 binds human BMP-2/BMP-4 when expressed in COS cells [PMID:8413626 "When
  expressed in monkey COS cells, the daf-4 receptor binds human BMP-2 and
  BMP-4"]. Direct DAF-7 binding to DAF-1/DAF-4 has, to my knowledge, not been
  demonstrated biochemically; the ligand-receptor relationship rests on genetics
  and family membership.
- Target cells: mainly the nervous system [PMID:10625546 "these experiments
  suggest the nervous system as a target of DAF-7 signaling and that the nervous
  system in turn regulates dauer formation by other tissues"], interneurons RIM and
  RIC for feeding and fat [PMID:18680713], and the gonadal distal tip cell for
  germline proliferation [PMID:28811311 "Neuronal DAF-7/TGFβ causes a
  DAF-1/TGFβR signaling cascade in the gonadal distal tip cell (DTC)"].

## Biological roles (all are phenotypes of loss of a secreted signal)

1. Inhibition of dauer entry, the core and best-supported role. All daf-7
   alleles are Daf-c (temperature-sensitive) [PMID:6583682 "All known mutations
   in daf-4 (eight alleles) and daf-7 (five alleles) produce a ts
   dauer-constitutive phenotype"]. Epistasis places daf-7 downstream of the
   chemosensory step [PMID:1732156].
2. Lifespan: Daf-c TGF-beta mutants are long-lived in a daf-16-dependent manner
   [PMID:17900898].
3. Feeding/fat: daf-7 mutants have reduced pumping and increased fat
   [PMID:18680713]; quiescence/satiety [PMID:18316030].
4. Behaviour: pathogen (P. aeruginosa) lawn avoidance [PMID:25303524],
   foraging/exploration [PMID:27799655], male mate searching [PMID:30024377],
   CO2 avoidance (UniProt; PMID:18524955, not cached).
5. Other outputs: chemoreceptor gene expression [PMID:12464635], GLR-1 abundance,
   systemic autophagy, germline stem-cell niche (lag-2 expression) [PMID:28811311].

## Note on PMID:23705068

Zhu et al. 2013 (eLife) is a sphingolipid/TORC1 paper; daf-7 appears only in a
supplementary epistasis figure showing that the mmBCFA/GlcCer/TORC1 pathway is
independent of DAF-7/TGF-beta [PMID:23705068 "Our additional analysis also
suggests that the GlcCer/TORC1 pathway is DAF-7/TGF-β pathway independent"]. It
does not establish any DAF-7 function and does not back a GO annotation.
