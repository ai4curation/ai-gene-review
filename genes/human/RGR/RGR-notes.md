# RGR (RPE-retinal G protein-coupled receptor) — review notes

Human gene, UniProt **P47804**, HGNC:9990, chromosome 10q23. 291 aa, 7-transmembrane opsin.

## Identity and family

- RGR is the "RPE-retinal G protein-coupled receptor" / "RGR opsin", a member of the
  GPCR class A (rhodopsin) family, opsin subfamily
  [file:human/RGR/RGR-uniprot.txt "Belongs to the G protein-coupled receptor 1 family. Opsin subfamily"].
- 7 transmembrane helices annotated (TRANSMEM 16-36, 53-73, 92-112, 131-151, 176-196,
  220-240, 248-268), consistent with a multi-pass membrane opsin
  [file:human/RGR/RGR-uniprot.txt].
- Carries a covalently bound retinal chromophore via a Schiff base to a conserved lysine
  at position 255 (MOD_RES 255 "N6-(retinylidene)lysine")
  [file:human/RGR/RGR-uniprot.txt "N6-(retinylidene)lysine"].

## Chromophore: binds all-trans-retinal (distinctive)

Unlike signalling opsins (which bind 11-cis-retinal in the dark), RGR preferentially binds
**all-trans-retinal** as its ground-state chromophore and, upon illumination, photoisomerizes
it to 11-cis-retinal:

- [file:human/RGR/RGR-uniprot.txt "Contains a covalently bound retinal chromophore linked via a"] /
  "Schiff base to a conserved lysine, and can bind both all-trans-retinal and 11-cis-retinal"
  and "Upon illumination, mediates photoisomerization of all-trans-retinal to 11-cis-retinal".
- FUNCTION: "Binds all-trans-retinal via a conserved Schiff-base lysine and, upon
  illumination, promotes photoisomerization of all-trans-retinal to 11-cis-retinal required
  for regeneration of visual pigments" [file:human/RGR/RGR-uniprot.txt].
- Founding characterization (not cached): Shen et al. 1994 Biochemistry 33:13117-13125,
  PMID:7947717 "A human opsin-related gene that encodes a retinaldehyde-binding protein"
  (RN [1] in UniProt), which is the ECO:0000269 source UniProt cites for the retinal-binding
  and photoisomerization PTM statements.

## Function in the visual (retinoid) cycle — PMID:18474598 (full text available)

Radu et al. 2008 (J Biol Chem 283:19730-8) is the key experimental paper and the IMP source
for GO:0001523 retinoid metabolic process. Human RPE cells and knock-out mice were used:

- RGR-opsin mediates **light-dependent mobilization of all-trans-retinyl esters** in RPE cells;
  RNAi knockdown of RGR in human RPE cells abolishes the light-dependent depletion of
  all-trans-REs [PMID:18474598 "these data suggest that RGR-opsin mediates light-dependent
  mobilization of\n all- trans- REs by RPE cells"] (verbatim in full text: "RGR-opsin mediates
  light-dependent mobilization of").
- Genetic epistasis: light-dependent all-trans-RE mobilization seen in rpe65-/- mice is
  abolished in rpe65-/-,rgr-/- double knockouts [PMID:18474598 "the light-dependent depletion of
  all- trans- REs seen in rpe65 - / - mice was\n abolished in rpe65 - / - , rgr - / - mice"].
- Proposed mechanism: RGR-opsin translocates all-trans-retinyl esters from a lipid-droplet
  storage pool to an "isomerase pool" in ER membranes, where they are used as substrate for
  synthesis of new visual chromophore [PMID:18474598 "RGR-opsin mediates light-dependent
  translocation of\n all- trans- retinyl esters from a storage pool in lipid droplets to an\n
  isomerase pool in membranes\n of the endoplasmic reticulum"].
- In the dark, RGR-opsin inhibits LRAT (lecithin:retinol acyltransferase) and all-trans-retinyl
  ester hydrolase in vitro; inhibition is released on light exposure [PMID:18474598 "in the dark,
  RGR-opsin inhibits lecithin:retinol\n acyltransferase\n and all- trans- retinyl ester hydrolase
  in vitro and that this\n inhibition is released upon exposure to light"].
- Reduced isomerase activity (~3-fold) in rgr-/- RPE, explaining slower rhodopsin regeneration
  [PMID:18474598 "Isomerase\n activity was ...3-fold lower in the rgr - / - versus wild-type
  homogenates"].
- The paper explicitly states RGR functions as a **photoisomerase**, independent of RPE65:
  [PMID:18474598 "RGR does not require Rpe65 for\n synthesis of its chromophore because RGR
  functions as a photoisomerase"].

## G-protein signalling: NOT well supported

Although structurally a class-A GPCR opsin, RGR is not a canonical signalling GPCR:

- [file:human/RGR/RGR-uniprot.txt "Although RGR is structurally a"] /
  "GPCR-family opsin, there is no consistent evidence that RGR activates G proteins or initiates
  a canonical second-messenger signaling cascade".
- The paper notes RGR has variant, non-canonical G-protein-coupling motifs: it "contains the
  variant\n motifs GRY and NA XX Y" (vs the canonical D(E)RY / NPxxY), i.e. impaired canonical
  G-protein coupling [PMID:18474598].
- Consequence: GPCR-signalling / phototransduction annotations (GO:0007186, GO:0007602,
  GO:0004930, GO:0008020) are best treated as family-level electronic/phylogenetic
  over-propagations rather than RGR's demonstrated core function. RGR's demonstrated role is
  photoisomerization / retinoid metabolism, not G-protein signal transduction.

## Localization

- SUBCELLULAR LOCATION: "Membrane; Multi-pass membrane protein"
  [file:human/RGR/RGR-uniprot.txt "Membrane"]. Functionally RGR is an ER/microsomal (RPE
  endoplasmic-reticulum) membrane protein; PMID:18474598 lists RGR-opsin among ER-associated
  retinoid-processing proteins ("Several retinoid-processing\n proteins are associated with the
  ER, including LRAT\n ..., 11- cis- RDH\n ..., RGR-opsin"). The GOA "plasma membrane" (IBA/TAS)
  annotations are phylogenetic transfers from signalling opsins and are not the biologically
  demonstrated location; "membrane" (GO:0016020) is defensible but non-specific.

## Tissue expression

- Preferentially expressed at high levels in the retinal pigment epithelium (RPE) and Müller
  cells of the neural retina [file:human/RGR/RGR-uniprot.txt "retinal pigment epithelium (RPE)
  and Mueller cells of the neural"; PMID:8641686 "expressed in Müller cells and the retinal
  pigment epithelium"].

## Disease

- Mutations cause **Retinitis pigmentosa 44 (RP44)** [MIM:613769]; variant Ser66Arg (VAR_017034)
  reported in RP patients [file:human/RGR/RGR-uniprot.txt "Retinitis pigmentosa 44 (RP44)";
  PMID:10581022 "Mutations in RGR, encoding a light-sensitive opsin homologue, in patients with
  retinitis pigmentosa"].

## Protein interaction (PMID:16189514) — abstract-only

- GOA GO:0005515 IPI is from Rual et al. 2005 high-throughput yeast two-hybrid interactome
  (CCSB-HI1); WITH/FROM UniProtKB:Q96EK5 (KIFBP). The cached record is abstract-only
  (full_text_available: false); no RGR-specific interaction detail is in the abstract. UniProt
  INTERACTION section lists P47804:Q96EK5 (KIFBP), consistent. Bare "protein binding" is
  uninformative — MARK_AS_OVER_ANNOTATED (do not REMOVE an IPI).

## Curation summary of GOA (20 annotations)

Core, demonstrated function = light-driven retinoid photoisomerization / retinoid metabolism +
all-trans-retinal (chromophore) binding, in RPE/Müller-cell membranes (ER). GPCR-signalling and
phototransduction annotations are family-level propagations that RGR does not biochemically
support and are marked as over-annotations (KEEP_AS_NON_CORE for phylogenetic IBA; REMOVE only
for clearly wrong IEA electronic propagations). Experimental/IPI annotations are never removed.

### Core function term ids chosen
- MF: GO:0005503 all-trans retinal binding (chromophore; more specific than GO:0016918).
- BP: GO:0106434 retinal isomerization (light-driven all-trans -> 11-cis).
- BP: GO:0001523 retinoid metabolic process (experimentally supported, IMP PMID:18474598).
