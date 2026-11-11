# Eif4ebp1 (rat, Q62622) - manual literature synthesis

No deep-research provider API keys were available in this session, so this file is a
manual synthesis from the cached publications (publications/PMID_*.md) and the UniProt
record (Eif4ebp1-uniprot.txt). Only the papers listed below were read; abstract-only papers
are marked as such.

## Identity and family

- Rat 4E-BP1 / PHAS-I, 117 aa, member of the eIF4E-binding protein family (Pfam PF05456
  eIF_4EBP; InterPro IPR008606; PANTHER PTHR12669:SF14).
  [file:rat/Eif4ebp1/Eif4ebp1-uniprot.txt "Belongs to the eIF4E-binding protein family."]
- Cloned from rat adipocytes as a prominent insulin-stimulated phosphoprotein.
  [PMID:8170978 "In this report we describe a cDNA encoding one of the most prominent insulin-stimulated phosphoproteins in rat adipocytes." (abstract only)]
- Contains the canonical YXXXXLphi eIF4E-binding motif (53-59) and a C-terminal TOS motif
  (113-117) that docks RPTOR/mTORC1 (both "By similarity" in UniProt).

## Molecular function: eIF4E-binding translational repressor

- Rat PHAS-I binds eIF4E when unphosphorylated and inhibits protein synthesis; MAP kinase
  phosphorylation at Ser64 blocks binding.
  [PMID:7939721 "Nonphosphorylated PHAS-I bound to initiation factor 4E (eIF-4E) and inhibited protein synthesis." (abstract only)]
- UniProt function summary: competes with eIF4G for eIF4E and prevents eIF4F assembly.
  [file:rat/Eif4ebp1/Eif4ebp1-uniprot.txt "Repressor of translation initiation that regulates EIF4E activity by preventing its assembly into the eIF4F complex"]
- Caspase cleavage after Asp24 yields Delta4E-BP1 that stays bound to eIF4E and is a potent
  inhibitor of cap-dependent translation; an N-terminal RAIP motif is required for efficient
  phosphorylation.
  [PMID:11865047 "Therefore, Delta4E-BP1 acts as a potent inhibitor of cap-dependent translation." (abstract only; full text not retrievable from PMC via the PubMed tool)]

## Regulation by phosphorylation (rat brain, full text read)

- PMID:20736160 (Ayuso et al. 2010, full text read): in rat cerebral cortex and hippocampal
  CA1, 4E-BP1 phosphorylation follows a hierarchy Thr69 -> Thr36/Thr45 -> Ser64. Thr69
  phosphorylation alone still allows eIF4E binding; additional Thr36/Thr45 phosphorylation
  dissociates 4E-BP1 from eIF4E and allows eIF4E-eIF4G association.
  [PMID:20736160 "Our results demonstrate that Thr69 phosphorylation alone allows binding to eIF4E, and subsequent Thr36/Thr45 phosphorylation is sufficient to dissociate 4E-BP1 from eIF4E."]
- 15 min global ischemia (I15) dephosphorylates 4E-BP1 (Akt and mTOR phosphorylation fall)
  and the hypophosphorylated alpha form binds eIF4E; 30 min reperfusion re-phosphorylates it
  and releases eIF4E for eIF4G.
  [PMID:20736160 "In the I15 group, the α form of 4E-BP1 associated with eIF4E was marked."]
  [PMID:20736160 "R30 induced a significant decrease in 4E-BP1 bound to eIF4E when compared with the SHC control or I15 condition, and accordingly, induced a significant increase in eIF4G/eIF4E association (Fig."]
- This paper shows m7GTP-Sepharose co-purification of 4E-BP1 with eIF4E from rat brain
  (physical association in tissue) and that changes in 4E-BP1 state are a response to
  ischemia-reperfusion; it does not test 4E-BP1 loss of function.

## Stress / physiological contexts (rat, abstracts only)

- Hypoxia in rat hepatocytes increases 4E-BP1-eIF4E association with 4E-BP1
  dephosphorylation. [PMID:10100614 "Incubation of hepatocytes under hypoxia increases binding of translation initiation factor eIF-4E to its inhibitory regulator 4E-BP1, and this correlates with dephosphorylation of 4E-BP1."]
  The authors note that this pathway is unlikely to account for the global fall in protein
  synthesis under hypoxia.
- Essential amino-acid deficient diets reduce hepatic 4E-BP1 phosphorylation (PMID:11500297).
- Acute ethanol increases the 4E-BP1-eIF4E complex in rat heart (PMID:15388509).
- Perinatal lung: 4E-BP1-eIF4E association falls at birth, eIF4E-eIF4G rises (PMID:18952566).
- PP2A catalytic subunit co-immunoprecipitates with 4E-BP1 in rat Nb2 lymphoma cells;
  4E-BP1 is proposed to be a PP2A substrate (PMID:16899564).
- 4E-BP1 immunostaining in hippocampal dendrites overlaps PSD-95 at synapses (PMID:11756682).

All of these are readouts of 4E-BP1 phosphorylation/eIF4E-binding state downstream of
mTORC1; they show 4E-BP1 is the effector through which these signals control cap-dependent
initiation, not that 4E-BP1 performs separate stress-response or developmental functions.

## Subcellular location

- Cytoplasm and nucleus by similarity to mouse (Q60876); nuclear localization independent of
  phosphorylation. [file:rat/Eif4ebp1/Eif4ebp1-uniprot.txt "Localization to the nucleus is unaffected by phosphorylation status."]
- Its eIF4E-sequestering activity on cap-dependent initiation is cytosolic.
