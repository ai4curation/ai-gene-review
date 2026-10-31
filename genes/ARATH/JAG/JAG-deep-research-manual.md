# JAG (JAGGED, At1g68480; UniProt Q6S591) - manual literature synthesis

No deep-research API was available; this synthesis was compiled manually from the
cached publications in `publications/` and PubMed searches (query
`JAGGED[Title] AND Arabidopsis`, 2026-10-28). Papers on JAGGED LATERAL ORGANS
(JLO, an unrelated LBD gene) and on Brassica napus JAG genome editing were excluded.

## Identity and domain architecture

- 253 aa nuclear protein of the plant-specific C1-1i (SUPERMAN-like) family of
  single C2H2 zinc-finger transcription factors; C2H2 zinc finger at residues 51-73
  (UniProt FT ZN_FING, PROSITE-ProRule PRU00042); N-terminal disordered region 1-46
  (MobiDB-lite). [file:ARATH/JAG/JAG-uniprot.txt]
- Cloning paper: "encodes a protein similar in structure to SUPERMAN with a single
  C(2)H(2)-type zinc finger, a proline-rich motif and a short leucine-rich repressor
  motif" [PMID:14973281].
- C1-1i members "consist of one zinc-finger and one to two EAR domains, connected by
  large intrinsically disordered regions (IDR)", with TOPLESS/TPR as known
  co-repressors [PMID:39260627, abstract].
- Closest paralog NUBBIN (NUB, At1g13400) acts redundantly in stamens and carpels
  [PMID:16554365].

## Expression and localization

- "JAG mRNA is localized to lateral organ primordia throughout the plant but is not
  found in the shoot apical meristem" [PMID:14973281].
- Expression "is restricted to the growing regions of lateral organs" and "notably
  absent from the cryptic bract" [PMID:14973282].
- Nucleus (UniProt, ECO:0000269 from PMID:14973281 and PMID:14973282).

## Molecular function: direct transcriptional repressor

- JAG-GR repression of BP and BEL1 is cycloheximide-independent, and "In both cases,
  reproducible binding was seen to specific regions upstream of the starting codon"
  by ChIP [PMID:22902754, full text].
- ChIP-seq plus transcriptome: "JAG directly repressed genes involved in meristem
  development, such as CLAVATA1 and HANABA TARANU ... BLADE ON PETIOLE 2 and the
  GROWTH REGULATORY FACTOR pathway", and "JAG directly repressed KIP RELATED PROTEIN 4
  (KRP4) and KRP2"; krp2/krp4 suppress jag growth defects [PMID:24497510, abstract].
- PTL "is directly repressed by JAG" [PMID:23653565].
- No in vitro DNA-binding (EMSA/SELEX) data for JAG were found; DNA binding is
  inferred from the ChIP data and the SUPERMAN-type zinc finger.

## Biological roles (all downstream of the repressor activity)

- Lateral organ shape and growth: loss of function gives "serrated leaves, narrow
  floral organs, and petals that contain fewer but more elongate cells"; misexpression
  causes ectopic leaf-like outgrowths [PMID:14973281]. JAG "suppresses the premature
  differentiation of tissues, which is necessary for the formation of the distal
  region" [PMID:14973282].
- Bract suppression: jag suppresses bract formation in lfy/ap1/ap2; ectopic JAG
  induces bracts [PMID:14973281, PMID:14973282].
- Primordium growth: JAG is required for anisotropic growth and decoupling of DNA
  synthesis from cell volume in sepal primordia [PMID:22902754]; promotes distal
  enhancement of petal growth rates [PMID:23653565].
- Stamens and carpels, with NUB: "NUB acts redundantly with JAG to promote the growth
  of the pollen-bearing microsporangia of the anthers and the carpel walls"
  [PMID:16554365].
- Sepal/petal boundary genes: AS1, AS2 and JAG "repress boundary-specifying genes"
  PTL, CUC1, CUC2; as1 jag double mutants have tiny sepals and petals
  [PMID:18156293].
- Fruit patterning: FIL and YAB3 "activate FUL and SHP redundantly with JAGGED (JAG)"
  [PMID:16192305]; JAG/FIL activity "negatively regulates BP expression in medial
  domains", while BP represses JAG/FIL genes; as1 jag fruits show synergistic valve
  reduction [PMID:23133401, full text].
- HAN interaction: HAN interacts with JAG in yeast two-hybrid and BiFC and "directly
  stimulates the expression of JAG and BOP2"; han-2 jag-3 double mutants have reduced
  petal number [PMID:26390296, full text].

## Things the literature does not show

- No evidence that JAG specifies floral organ identity: mutant organs are mis-shaped
  but retain their identity [PMID:14973281, PMID:14973282].
- No evidence in the available abstracts for a role in abaxial cell fate
  specification; NUB and JAG promote "differentiation of adaxial cell types in the
  carpel walls" [PMID:16554365].
