# Rac1 (rat, UniProt Q6RUV5) - manual literature synthesis

No deep-research API was available for this review. This synthesis was written by hand from
the cached publications in `publications/`, the rat UniProt record (`Rac1-uniprot.txt`) and a
local sequence comparison (`Rac1-bioinformatics/RESULTS.md`). Quotes are verbatim.

## Identity and family

- Rat Rac1 is a 192-residue Rho-family small GTPase with a C-terminal CAAX box; the last three
  residues are removed after prenylation. UniProt: "Belongs to the small GTPase superfamily. Rho
  family." [UniProtKB:Q6RUV5]
- InterPro/Pfam signatures: P-loop NTPase, Small_GTPase, Small_GTPase_Rho (IPR003578), Pfam
  PF00071 (Ras), PROSITE PS51420 (RHO), PANTHER PTHR24072 (RHO FAMILY GTPASE).
- Rat, human (P63000) and mouse (P63001) canonical sequences are identical over all 192
  residues [file:rat/Rac1/Rac1-bioinformatics/RESULTS.md]. ISO/ISS transfers from human or
  mouse therefore carry no sequence risk; only the biological appropriateness of the source
  term matters.

## Molecular function: a GTP/GDP molecular switch

- UniProt FUNCTION: "Plasma membrane-associated small GTPase which cycles between active
  GTP-bound and inactive GDP-bound states." "In its active state, binds to a variety of effector
  proteins to regulate cellular responses" [UniProtKB:Q6RUV5].
- Activity regulation: GEFs, GAPs and GDIs; "GTP hydrolysis is stimulated by ARHGAP30 and
  ARHGAP44." [UniProtKB:Q6RUV5, ECO:0000269 PubMed:25498153].
- Rat hippocampal neurons (Galic et al. 2014, eLife): "A GAP domain in ArhGAP44 triggers local
  Rac-GTP hydrolysis" [PMID:25498153]. This is the experimental basis of UniProt's EC 3.6.5.2
  and the EXP GTPase activity row. Hydrolysis is the off-switch of the cycle; the biologically
  relevant activity is G protein (switch) activity, of which GTPase activity is a part.
- RhoGDI: in rat embryo fibroblasts, recombinant RhoGDIalpha pulls down endogenous Rac1; "When
  Ser-34 was mutated to Asp, there was significantly reduced RhoGDIα binding to RhoA (by around
  75%) but not Rac1 or Cdc42." [PMID:20472934]. PKC phosphorylation of RhoGDIalpha Ser34
  selectively releases RhoA, whereas PAK phosphorylation at Ser101/Ser174 releases Rac1 (cited
  in the same paper's discussion). In INS-1E beta cells, "Rac1 binding to RhoGDI-α decreased
  after MPA treatment, and Rac1 was induced and subsequently activated by MPA." [PMID:22564631].
  Glioma cells: "Sema5A promotes Rac1 recruitment to RhoGDIα and reduces its membrane
  localization in a plexin-B3-dependent manner" [PMID:20696765; abstract only; the title states
  human glioma cells].
- Effector/partner binding documented in rat material: Rab7 (GTP form) by yeast two-hybrid and
  co-localization at the osteoclast ruffled border [PMID:16040606]; CDKL5 "colocalized and
  formed a protein complex with Rac1" [PMID:20861382]; HDAC3 "Antigen stimulation led to an
  interaction between HDAC3 and Rac1 at the membrane" (RBL-2H3) [PMID:22679019]; ATP7A
  "Co-immunoprecipitation analysis showed that ATP7A associated with Rac1 in the basal state"
  (rat VSMC) [PMID:20671235]; SH3RF2 (UniProt, PubMed:22128169).

## Locations

- Plasma membrane (inner leaflet, prenyl anchor), ruffles and lamellipodia; cytosol in the GDI
  complex; nucleus after activation (polybasic region; by similarity to human)
  [UniProtKB:Q6RUV5].
- Synapse: "We also show that Rac is locally activated in dendritic spines using fluorescence
  resonance energy transfer." [PMID:15800193, rat hippocampal neurons].
- GABAergic synapse: "We find that Rac1 activity stabilizes GABAARs at inhibitory synapses while
  disrupting GIT1, Rac1 or PAK all lead to impaired inhibitory transmission." [PMID:25284783].
- Osteoclast ruffled border: "Rab7 colocalizes with Rac1 at the fusion zone of the ruffled border
  in bone-resorbing osteoclasts" [PMID:16040606].
- Golgi membranes (in vitro reconstitution): "activated ARF1 can stimulate Arp2/3 recruitment to
  Golgi membranes through coatomer, Cdc42 or Rac, and N-WASP." [PMID:15147909].

## Processes (what Rac1 itself does)

1. Rac signal transduction to the actin cytoskeleton: lamellipodia and ruffles via WAVE/Arp2/3
   and PAK. Rat VSM cells: "equibiaxial stretch inhibited lamellipodia formation through
   deactivation of Rac" and "GAP-resistant, constitutively active V12Rac reversed this
   inhibition" [PMID:12105187]. Rat osteoclasts: "Rac-GTPases are present in rat osteoclasts and
   are involved in the organization of the actin cytoskeleton and in resorptive activity."
   [PMID:10350213].
2. Neuronal spine/synapse cytoskeleton: GIT1/PIX/Rac/PAK module [PMID:15800193, PMID:25284783];
   ArhGAP44 restricts Rac activity in dendritic filopodia [PMID:25498153]; netrin-1/DCC recruits
   Rac1 into a complex and activates it during growth-cone expansion [PMID:15788770].
3. NADPH oxidase (NOX2) regulatory subunit: "the small GTPase Rac1, an intrinsic component of the
   NOX complex" (rat NR8383 macrophages) [PMID:16055727]; ROS generation needed for LTB4
   chemotaxis "stable expression of Rac(N17), a dominant negative Rac1 mutant, completely blocks
   leukotriene B(4)-induced ROS generation" [PMID:11756405].
4. Many downstream physiological readouts are documented in rat systems with dominant-negative
   or knockdown tools: mast-cell chemotaxis to eotaxin [PMID:12413953], hepatocyte DNA synthesis
   via JNK [PMID:9487126], cardiomyocyte hypertrophy via ASK1/NF-kB [PMID:12672819],
   glucose-stimulated insulin secretion by F-actin remodelling in INS-1 cells [PMID:23412604],
   VSMC migration [PMID:20671235]. These place Rac1 upstream of the readout; they are non-core
   process annotations.

## Mouse/human-derived processes (ISO)

RGD transfers a large set of MGI and human process annotations by ISO. Those that describe
cytoskeletal or migratory cell behaviour (neuron migration, axon guidance, dendrite
morphogenesis, phagocytic engulfment, cell spreading, ruffle/lamellipodium assembly) follow
directly from the switch function and are retained as non-core. Organismal or tissue
phenotypes from knockouts (erythrocyte enucleation, cochlea morphogenesis, ovarian follicle
development, homeostasis of cell number, hyperosmotic response, etc.) are pleiotropic downstream
outcomes of Rac1 loss rather than processes Rac1 performs.
