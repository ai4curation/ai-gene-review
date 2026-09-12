# SMPD2 (neutral sphingomyelinase 1 / nSMase1) — review notes

UniProt: O60906 (NSMA_HUMAN), gene SMPD2, HGNC:11121, 423 aa, EC 3.1.4.12.

## Identity and family

- RecName in UniProt is **Sphingomyelin phosphodiesterase 2**; EC=3.1.4.12
  [file:human/SMPD2/SMPD2-uniprot.txt "EC=3.1.4.12"]. AltNames include
  **Lyso-platelet-activating factor-phospholipase C (Lyso-PAF-PLC)** and
  **Neutral sphingomyelinase (N-SMase / nSMase1)**
  [file:human/SMPD2/SMPD2-uniprot.txt "AltName: Full=Lyso-platelet-activating factor-phospholipase C"].
- Belongs to the neutral sphingomyelinase family; contains an
  endonuclease/exonuclease/phosphatase (DNase-I-like) catalytic fold (Pfam
  PF03372 Exo_endo_phos; Gene3D 3.60.10.10)
  [file:human/SMPD2/SMPD2-uniprot.txt "Belongs to the neutral sphingomyelinase family"].
- ACT_SITE 272 (proton acceptor, by similarity); BINDING 49 for Mg(2+);
  SITE 180 "Important for substrate recognition"
  [file:human/SMPD2/SMPD2-uniprot.txt "Important for substrate recognition"].
- Cryo-EM structure available (PDB 8J2F, 3.07 Å); two C-terminal
  transmembrane helices (TRANSMEM 330–350, 354–374)
  [file:human/SMPD2/SMPD2-uniprot.txt "TRANSMEM        330..350"].

## Catalytic activity — the SMase vs lysophospholipase nuance

The gene was originally **cloned as a putative neutral sphingomyelinase**
(Tomiuk et al. 1998, PMID:9520418), but the functional characterization that
followed showed its cellular role is more that of a **lyso-PAF phospholipase C**
than a bulk cellular SMase:

- Sawai et al. 1999 (PMID:10608884) showed that although SM → ceramide +
  phosphocholine occurs in vitro, in overexpressing cells "The metabolism of
  ceramide and SM was not apparently affected in overexpressing cells"
  [PMID:10608884 "The metabolism of\nceramide and SM was not apparently affected in overexpressing cells"].
  Instead, radiolabeling showed accumulation of 1-O-alkyl-sn-glycerol and loss
  of alkyl-acyl-PC, and both lyso-PC and lyso-PAF are good in vitro substrates;
  they concluded "the protein acts as lyso-PAF-PLC rather than lyso-PC-PLC or
  N-SMase in cells"
  [PMID:10608884 "these results suggest that the protein acts as lyso-PAF-PLC rather than \nlyso-PC-PLC or N-SMase in cells"].
- Miura et al. 2004 (PMID:14741383) showed nSMase1 (and nSMase2) hydrolyze
  sphingosylphosphocholine (SPC) efficiently under detergent-free conditions
  [PMID:14741383 "nSMase1 and nSMase2,\nhuman neutral sphingomyelinases (SMases), are capable of hydrolyzing SPC \nefficiently under detergent-free conditions"].
  Substrate specificity requires a hydrogen-bond donor at C-2/sn-2 (hence SM,
  SPC, and monoradyl-glycerophosphocholine but not diradyl-GPC are substrates)
  [PMID:14741383 "a hydrogen-bond donor at the C-2 or sn-2 \nposition in the substrate is required for recognition by the enzymes"].

UniProt records EC 3.1.4.12 with multiple catalytic-activity reactions:
sphingomyelin → ceramide + phosphocholine; sphingosylphosphocholine → sphingoid
base + phosphocholine; and hydrolysis of 1-O-octadecyl-/1-O-hexadecyl-/
1-hexadecanoyl-glycero-3-phosphocholine (lyso-PAF / lyso-PC) → the corresponding
(alkyl/acyl)-glycerol + phosphocholine
[file:human/SMPD2/SMPD2-uniprot.txt "Also hydrolyzes"].
All the lyso-PAF / lyso-PC reactions release **phosphocholine** by cleaving the
phosphodiester bond — i.e. a **phospholipase C**-type cleavage, not a
lysophospholipase (EC 3.1.1.5) acyl-ester hydrolysis. So the appropriate MF for
the lyso-PAF activity is **GO:0004629** (current ontology label
**"C-type glycerophospholipase activity"**, formerly "phospholipase C activity";
def: "cleaves the first phosphodiester bond between the phosphate and glycerol,
producing a mono- or a diacylglycerol, depending on whether the substrate is a
lysoglycerophospholipid or a glycerophospholipid"), a sibling of sphingomyelin
phosphodiesterase activity (both are under phosphoric diester hydrolase activity
GO:0008081).

Cofactor: **Mg(2+)** [file:human/SMPD2/SMPD2-uniprot.txt "Name=Mg(2+)"].
Kinetics: KM 26.2 uM for sphingomyelin; comparable KM (~27 uM) for lyso-PAF
substrates; the enzyme handles SM, SPC, and lyso-PAF/lyso-PC with similar
efficiency [file:human/SMPD2/SMPD2-uniprot.txt "KM=26.2 uM for sphingomyelin"].

## Pathway / process

- UniProt PATHWAY: "Lipid metabolism; sphingolipid metabolism"
  [file:human/SMPD2/SMPD2-uniprot.txt "Lipid metabolism; sphingolipid metabolism"]
  (UniPathway UPA00222). Consistent with sphingomyelin/ceramide metabolism.
- Reactome places SMPD2 (with SMPD3) in sphingomyelin hydrolysis to ceramide and
  in TNFR1-mediated ceramide production / ceramide signalling
  [file:human/SMPD2/SMPD2-uniprot.txt "Reactome; R-HSA-193681; Ceramide signalling"].
- The **major stress-responsive / bulk cellular neutral SMase is SMPD3 (nSMase2)**,
  not SMPD2; SMPD2's physiological role as a bulk cellular SMase is limited and
  debated (see Sawai 1999 above). Care is warranted with broad
  "ceramide biosynthetic process" / "intracellular signal transduction"
  annotations transferred from orthologs.

## Localization

- UniProt SUBCELLULAR LOCATION: **Cell membrane; multi-pass membrane protein**
  (by similarity to mouse O70572)
  [file:human/SMPD2/SMPD2-uniprot.txt "SUBCELLULAR LOCATION: Cell membrane"].
- PAN-GO / IBA phylogenetic annotations place activity at endoplasmic reticulum
  (GO:0005783), cell periphery (GO:0071944), and caveola (GO:0005901). The
  original literature and orthologs describe an ER/Golgi-membrane enzyme; the
  human UniProt subcellular-location call is plasma/cell membrane by similarity.
  Both ER-membrane and plasma-membrane localizations appear in the annotation
  set; the enzyme is an integral membrane protein with two C-terminal TM helices.

## Interactions

Numerous IntAct binary interactions (ARFIP1, CCN1, COQ8A, GAD2, MTHFR, NDRG4,
PBX3, PGRMC2, PITPNC1, SH3GLB1, SLC10A1, SLC7A8, STAR, TMEM14B, TMEM167B)
[file:human/SMPD2/SMPD2-uniprot.txt "O60906; P53367: ARFIP1"]. These are
high-throughput binary/AP-MS screens (HuRI, BioPlex, neurodegeneration
interactome) and do not by themselves define a specific molecular function
beyond generic protein binding.

## Reference assessment

- PMID:10608884 (Sawai 1999) — HIGH relevance; the key functional paper
  establishing lyso-PAF-PLC as the dominant cellular activity. Abstract-only in
  cache; supports EC 3.1.4.12 + lyso-PAF-PLC. VERIFIED (matches UniProt EC/PMID).
- PMID:14741383 (Miura 2004) — HIGH relevance; SPC-PLC / SM hydrolysis and
  substrate-recognition determinant. Abstract-only in cache. VERIFIED.
- Interactome papers (PMID:28514442, 32296183, 32814053, 33961781) — LOW
  relevance (background high-throughput binary interaction screens); support
  only generic protein binding.
- Reactome R-HSA-1606273 / R-HSA-5626981 — plasma-membrane SM hydrolysis and
  TNFR1 complex association; TAS, consistent with membrane localization but
  Reactome models plasma-membrane hydrolysis for the SMPD2/3 pair generically.

## Core function synthesis

1. MF: sphingomyelin phosphodiesterase activity (GO:0004767), Mg2+-dependent,
   in vitro (IDA). Represents the classical/cloned activity.
2. MF: C-type glycerophospholipase activity (GO:0004629, formerly "phospholipase
   C activity") — captures the physiologically preferred lyso-PAF / lyso-PC / SPC
   phospholipase-C activity (IDA to the general phosphoric diester hydrolase
   activity GO:0008081 supports this).
3. BP: sphingomyelin catabolic process (GO:0006685) / sphingolipid metabolic
   process — the UniProt-stated pathway.
4. Location: integral membrane protein (ER/Golgi and plasma/cell membrane).
