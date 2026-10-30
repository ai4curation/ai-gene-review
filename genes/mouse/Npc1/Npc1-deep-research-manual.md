# Npc1 (mouse, UniProt O35604) — manual literature review

No deep-research provider API keys were available in this environment, so this file
is a hand-assembled literature synthesis from the cached publications in
`publications/` plus the curated UniProt record `Npc1-uniprot.txt`. All assertions
carry inline provenance.

## Gene and protein

Mouse *Npc1* (MGI:1097712, GeneID 18145) encodes a 1277-residue polytopic
glycoprotein of the late endosomal/lysosomal limiting membrane. UniProt O35604
gives a signal peptide (1-22), 13 transmembrane helices, three large lumenal
domains, a sterol-sensing domain (SSD, residues 620-785), a cholesterol-binding
residue at position 41, a region 175-205 "Important for cholesterol binding and
cholesterol transfer from NPC1 to liposomes", and a C-terminal 1274-1277 region
"Required for location in lysosomes"
[file:mouse/Npc1/Npc1-uniprot.txt]. The protein belongs to the patched family
[file:mouse/Npc1/Npc1-uniprot.txt, "Belongs to the patched family"].

The 13-TM topology, with the SSD oriented as in HMG-CoA reductase and SCAP, was
established experimentally [PMID:10821832, "our data indicate that this glycoprotein
contains 13 transmembrane domains, 3 large and 4 small luminal loops, 6 small
cytoplasmic loops, and a cytoplasmic tail"].

## Core molecular function: cholesterol hand-off from NPC2 and export from lysosomes

The accepted mechanism is a "hydrophobic hand-off": LDL-derived cholesterol liberated
in the lysosome lumen is bound by the small soluble protein NPC2 and transferred to
NPC1's N-terminal domain (NTD), from where it reaches the limiting membrane
[PMID:27551080, "second (middle), lumenally oriented domain (MLD) and transfers cholesterol"].

- Direct NPC1-NPC2 binding is through NPC1's second (middle) lumenal domain, is
  cholesterol-dependent and occurs only at lysosomal pH
  [PMID:22065762, "we show here that the second lumenal domain of NPC1 binds directly to NPC2 protein"];
  [PMID:22065762, "Binding to NPC1 domain 2 requires the presence of cholesterol on"].
  Disease mutations in domain 2 (R404Q, R518Q) reduce NPC2 binding while the full-length
  R518Q protein still reaches lysosomes, so the defect is functional rather than a
  folding/trafficking defect [PMID:22065762, "R581Q showed the same punctate, lysosomal distribution as the wild-type protein"].
- The 2.4 Å crystal structure of the NPC1-MLD/NPC2 complex reveals a continuous
  cholesterol transfer tunnel, and the mouse NPC1 MLD residues F503/Y504 are required
  for NPC2 binding and for rescuing cholesterol accumulation in NPC1-null cells
  [PMID:27551080, "These data confirm the physiological importance of F503 and Y504 in NPC1 function in cells"].
- NPC2 catalyses bidirectional cholesterol transfer between NPC1's NTD and lipid
  bilayers in vitro (the molecular basis of the GO:0120020 cholesterol transfer activity
  annotation) [PMID:18772377].
- A higher-resolution NPC1 structure shows the C-terminal lumenal domain (where ~45% of
  disease mutations fall) holds the NTD in the orientation needed to receive cholesterol
  from NPC2 [PMID:28784760].

In the mouse, the cholesterol-binding pocket is genetically required: knocking the
P202A/F203A substitutions into *Npc1* reproduces complete NPC1 deficiency
[PMID:21896731, "reproduce the phenotype of complete NPC1 deficiency when knocked into the mouse"];
[PMID:21896731, "the cholesterol binding site in the N-terminal domain of NPC1 is"].

Quantitative mouse genetics places NPC1 in a sequential lysosomal pathway with LAL and
NPC2 [PMID:21289032, "endosomal/lysosomal (E/L) compartment by the sequential action of lysosomal acid"], and
*Npc1*/*Npc2* double mutants are no worse than either single mutant, i.e. the two
proteins act in one pathway [PMID:15071184, "function in concert to facilitate the intracellular transport of"].

Downstream of lysosomal export, UniProt records that NPC1 "Mediates cholesterol
transfer from lysosomes to endoplasmic reticulum by tethering endosomal/lysosomal
compartments and endoplasmic reticulum membrane contact sites where it interacts with
sterol transport protein GRAMD1B" [file:mouse/Npc1/Npc1-uniprot.txt].

## Localization

Lysosomal/late-endosomal membrane is the functional location
[file:mouse/Npc1/Npc1-uniprot.txt, "Lysosome membrane"]. Mouse liver fractionation
and fibroblast imaging additionally show a second, cholesterol- and caveolin-1-rich
vesicular compartment and a raft-associated pool, with LDL, progesterone or chloroquine
treatment increasing the LAMP1-colocalizing fraction
[PMID:10787428, "a fraction of NPC1 cosediments with caveolin-1 in rafts"];
[PMID:10787428, "Incubation of fibroblasts with low density lipoprotein (LDL) increases"].
Human NPC1 mislocalization studies additionally report ER and perinuclear signal,
mostly for mutant protein [PMID:12554680, "colocalized with Rab7-positive late endosomes whereas NPC1-C113R localized to"].

## Secondary / non-core functions

- **mTORC1 restraint.** NPC1 binds SLC38A9 at the lysosomal surface and inhibits
  cholesterol-driven mTORC1 activation through its sterol-transport function
  [PMID:28336668, "Niemann-Pick C1 (NPC1) protein, which regulates cholesterol export from the"].
- **Filovirus entry receptor.** NPC1 is required for Ebola virus entry; cleaved EboV GP
  binds NPC1-containing late endosome/lysosome membranes, and this requirement is
  independent of NPC1's cholesterol transport activity
  [PMID:21866101, "Thus, EboV entry is strictly dependent on NPC1 expression but not NPC1-dependent cholesterol transport activity"];
  [PMID:21866103]. *Npc1*+/- mice were used in filovirus challenge experiments
  [PMID:21866103, "BALB/c NPC1+/− mice and BALB/c NPC1 +/+ mice (5 to 8 week old)"].
- **Lysosomal amine / xenobiotic handling.** NPC1 knockdown raises cellular chloroquine
  accumulation and abolishes the protection conferred by alpha-tocopherol transfer protein
  [PMID:22147702, "These results indicate that NPC1 is involved in α-TTP-mediated prevention of CQ accumulation"].

## Phenotypes that are consequences, not functions

*Npc1*-null mice sequester unesterified cholesterol in late endosomes/lysosomes, lose
Purkinje cells, develop ataxia and die around 2-3 months
[file:mouse/Npc1/Npc1-uniprot.txt, "Causes age-dependent loss of Purkinje cells, loss of body weight and leads then to ataxia and premature death at a"];
[PMID:21697390]. Intracerebroventricular HP-beta-cyclodextrin prevents the
neurodegeneration by driving cholesterol out of the compartment [PMID:21697390].
Secondary consequences reported in the knockout — increased autophagy via Beclin-1
[PMID:17468177], exacerbation by *Mapt* deletion with gait abnormalities
[PMID:19074461], glycosphingolipid accumulation with impaired endocytic trafficking
[PMID:15078881], reduced cerebellar EAAT protein levels [PMID:29463856] — are
downstream of the cholesterol/sphingolipid storage rather than activities NPC1 itself
performs. These are the basis of several existing GO process annotations that this
review marks as over-annotated.
