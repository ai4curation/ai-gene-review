# Kcnj10 (rat, P49655; Kir4.1) - manual literature synthesis

No deep-research provider was available for this review; this file was compiled by hand from
cached publications in `publications/` and the UniProt record (`Kcnj10-uniprot.txt`). Each
assertion carries its source.

## Identity and family

- Rat Kcnj10 (RGD:61822, GeneID 29718) encodes Kir4.1 (also KAB-2, BIRK1, BIR10), a 379-aa
  member of the inward rectifier K+ channel family (TC 1.A.2.1), KCNJ10 subfamily
  [file:rat/Kcnj10/Kcnj10-uniprot.txt "Belongs to the inward rectifier-type potassium channel"].
- Topology: two transmembrane helices (M1 62-88, M2 141-166) flanking a pore-forming re-entrant
  loop with the K+ selectivity filter (128-133), with cytoplasmic N- and C-termini
  [file:rat/Kcnj10/Kcnj10-uniprot.txt, FT TRANSMEM/INTRAMEM/MOTIF; cryo-EM PDB:8I5M, PMID:38355723].

## Channel activity (molecular function)

- Cloned from rat brain; expression in Xenopus oocytes gives a classical inward rectifier K+
  current [PMID:7608203 "Xenopus oocytes injected with cRNA derived from this clone expressed a
  K+ current, which showed classical inward rectifier K+ channel characteristics"].
- Rat Kir4.1 forms functional homomeric channels and also heteromeric Kir4.1/Kir5.1 (Kcnj16)
  channels with distinct properties: homomers are weakly pH-sensitive with ~10 pS conductance,
  heteromers strongly pH-sensitive with ~45 pS conductance [PMID:19665991 "homomeric Kir4.1
  channels are only mildly sensitive to intracellular pH"; "Kir5.1 co-assembles with Kir4.1 to
  form novel heteromeric Kir4.1/Kir5.1 channels which are thought to form the basolateral small
  conductance K+ channel in the distal nephron"]. Kir5.1 alone does not form channels
  [PMID:19665991 "The Kir5.1 subunit does not form functional channels by itself"].
- Gating: activated by PtdIns(4,5)P2 and inhibited by intracellular acidification; a TM1 lysine
  (K67) H-bond at the helix-bundle crossing controls PIP2/pH gating kinetics [PMID:18690035].
  The cryo-EM structure (rat, 2.85 A) shows PIP2 bound at R36, K168, K171 etc.
  [file:rat/Kcnj10/Kcnj10-uniprot.txt FT BINDING, ECO:0000269|PubMed:38355723] and a homotetramer
  [UniProt SUBUNIT "Homotetramer (PubMed:38355723)"]; the antidepressant lead Lys05 blocks in the
  central cavity [PMID:38355723].
- EAST/SeSAME disease mutations studied in rat Kir4.1 compromise channel function, several by
  alkaline-shifting pH sensitivity [PMID:20807765 "All of the mutations compromised channel
  function"].

## Physiological roles

- Astrocytes: Kir4.1 is the dominant K+ conductance that sets the very negative resting potential
  of astrocytes and mediates K+ spatial buffering. RNAi in rat cortical astrocytes depolarised the
  cells and impaired K+ flux and, secondarily, glutamate uptake [PMID:17091490 "Kir4.1 channels
  are primarily responsible for significant hyperpolarization of cortical astrocytes and are
  likely to play a major role in potassium buffering"; "highlights the role of membrane
  hyperpolarization in this process"]. Mouse conditional knockout confirms depolarisation,
  impaired K+ and glutamate uptake, ataxia, seizures, early death and enhanced short-term
  synaptic potentiation [PMID:17942730]. Hippocampal astrocytes of Kir4.1-/- mice lack
  Ba2+-sensitive currents [PMID:19515915].
- Localisation in glia: perivascular end-feet and fine processes of astrocytes in rat optic nerve,
  and oligodendrocyte cell bodies [PMID:15198689 "Astrocyte expression of Kir4.1 is localized to
  perivascular end-feet and fine processes"]; astrocyte membrane domains facing pia and blood
  vessels, or processes around synapses, as homomers or Kir4.1/5.1 heteromers [PMID:15310750].
- Retina (Mueller glia): Kir4.1 is the principal Mueller cell K+ channel, concentrated in endfeet
  and perivascular processes; tethered with AQP4 to the dystrophin-glycoprotein complex
  [PMID:16206160; PMID:10908613]. Its loss abolishes the slow PIII ERG component but spares the
  b-wave [PMID:10908613]. Expression changes after blue-light injury [PMID:18450590] and
  aldosterone (moves Kir4.1 to apical microvilli) [PMID:20466875] are responses of the cell, not
  activities of the channel.
- Kidney: basolateral Kir4.1/Kir5.1 heteromer is the principal basolateral K+ channel of the distal
  nephron, recycling K+ for the Na+/K+-ATPase; scaffolded by MAGI-1a through the C-terminal PDZ
  motif, with Ser377 phosphorylation disrupting it [PMID:18303016]. The Ca2+-sensing receptor
  binds Kir4.1 and reduces its surface expression via Galphaq/caveolin-1 [PMID:21084311]. In mouse
  DCT, Kir4.1 is required for sensing plasma K+ [PMID:31736353].
- Stomach: Kir4.1 colocalises with H+/K+-ATPase and moves to the apical membrane of parietal cells
  on stimulation [PMID:18395087].
- Primary cilia: a mouse siRNA screen in IMCD3 cells found Kcnj10 needed for ciliogenesis,
  independent of its channel function, with localisation at the ciliary base [PMID:26546361].
- Interactors: PDZ proteins (MAGI-1, syntrophins, CIPP/PATJ) [PMID:18303016; PMID:15310750;
  PMID:9647694]; MLC1 pull-down [PMID:19931615].

## Assessment for GO

- Core MF: inward rectifier potassium channel activity (GO:0005242), as homotetramer and as part
  of Kir4.1/Kir5.1 heteromers.
- Core BP: potassium ion import across plasma membrane / K+ transmembrane transport; regulation of
  resting membrane potential; potassium ion homeostasis (spatial buffering).
- Peripheral or over-annotated: glutamate uptake (indirect via hyperpolarisation), myelination,
  oligodendrocyte development, behaviour, synaptic plasticity, ciliogenesis, hormone/light
  responses (expression changes).
