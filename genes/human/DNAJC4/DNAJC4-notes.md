# DNAJC4 (Q9NNZ3) research notes

## Identity
- DnaJ homolog subfamily C member 4; AltNames DnaJ-like protein HSPF2; MEN1 candidate protein 18 (MCG18).
- 241 aa. Contains a J domain (aa 34-99) [file:human/DNAJC4/DNAJC4-uniprot.txt "DOMAIN 34..99 /note=\"J\""].
- Has a predicted single-pass transmembrane helix (TRANSMEM 156..175) and is annotated as a membrane / single-pass membrane protein [file:human/DNAJC4/DNAJC4-uniprot.txt "SUBCELLULAR LOCATION: Membrane ... Single-pass membrane protein"].
- Tissue: HPA "Tissue enhanced (testis)"; Pharos Tdark (very poorly characterized).
- PAN-GO: 0 GO annotations based on evolutionary models (i.e. family-level functional inference is weak).

## Function status
- A J-domain protein, so by family it is an HSP70 (DnaJ/HSP40) co-chaperone, but there is essentially NO direct experimental characterization of its activity. UniProt does not even provide a FUNCTION comment.
- The original cloning paper [PMID:9473517 "Characterisation of a new human and murine member of the DnaJ family of proteins"] is the basis for the NAS protein-folding and TAS response-to-unfolded-protein / membrane annotations. These are family/inference-level, not demonstrated for DNAJC4 specifically.

## Interactions (GOA / IntAct)
- HTT (huntingtin, P42858); NbExp=12 [file:human/DNAJC4/DNAJC4-uniprot.txt "Q9NNZ3; P42858: HTT; NbExp=12"]. From Huntingtin-interactome screens (PMID:17500595 = Kaltenbach et al., HTT interactors).
- WFS1 (wolframin, O76024); NbExp=3 [file:human/DNAJC4/DNAJC4-uniprot.txt "Q9NNZ3; O76024: WFS1; NbExp=3"]. From PMID:32814053 (neurodegeneration interactome).
- These are high-throughput / focused interactome screens; "protein binding" (GO:0005515) is uninformative; partners (HTT, WFS1) do not define a chaperone client repertoire.

## Curation judgment
- Core MF: J-domain co-chaperone presumed to be an HSP70 ATPase activator, but NOT experimentally supported -> cannot assert ATPase activator as a *verified* core; the only experimentally-supportable molecular role is the J domain unfolded-protein-binding / Hsp70-cochaperone family assignment. Use unfolded protein binding (GO:0051082) cautiously (NAS family-level). Avoid overstating.
- Membrane localization: predicted single-pass TM; reasonable to KEEP_AS_NON_CORE / ACCEPT as predicted.
- protein binding IPI (HTT, WFS1): KEEP_AS_NON_CORE (records real interactions but uninformative; not core).
- response to unfolded protein (TAS) and protein folding (NAS): family/inference-level; keep as non-core.
