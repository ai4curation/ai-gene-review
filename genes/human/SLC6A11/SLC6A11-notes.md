# SLC6A11 (GAT-3 / GAT3) curation notes

UniProt: P48066 (S6A11_HUMAN), 632 aa. Gene: SLC6A11 (synonyms GABT3, GAT3).
HGNC:11044. Chromosome 3p25.3. Batch 9 canonical-surfaceome backfill.

## Identity and family

- SLC6A11 encodes the Na+- and Cl--dependent GABA transporter 3 (GAT-3), a member
  of the SLC6 / sodium:neurotransmitter symporter (SNF) family (TC 2.A.22;
  neurotransmitter:sodium symporter, NSS). 12 transmembrane helices (LeuT fold),
  cytoplasmic N- and C-termini.
  [file:human/SLC6A11/SLC6A11-uniprot.txt "Belongs to the sodium:neurotransmitter symporter (SNF)"]
  [PMID:1400419 "can be modeled with 12 transmembrane"]
- This is a **secondary-active symporter** (ion-gradient driven), NOT an antiporter,
  uniporter, channel or heteromeric transporter. No heavy chain, no obligate complex
  partner. Cryo-EM structures of human GAT-3 now exist (PDB 9CP4/9CP5/9LK7-9/9QO8/9QO9).

## Transport mechanism and substrates

- Mediates sodium- and chloride-dependent transport of GABA.
  [file:human/SLC6A11/SLC6A11-uniprot.txt "Mediates sodium- and chloride-dependent transport of gamma-"]
- Stoichiometry ~2 Na+ : 1 Cl- : 1 GABA, confirmed by the UniProt/Rhea catalytic-activity
  reaction: "4-aminobutanoate(out) + chloride(out) + 2 Na(+)(out) = 4-aminobutanoate(in) +
  chloride(in) + 2 Na(+)(in)" (Rhea:70687; ChEBI GABA=CHEBI:59888, Na+=CHEBI:29101,
  Cl-=CHEBI:17996).
  [file:human/SLC6A11/SLC6A11-uniprot.txt "chloride(out) + 2 Na(+)(out)"]
- High affinity for GABA (Km ~10 uM in the rat orthologs cloned alongside).
  [PMID:1400419 "display high affinity for GABA (Km approximately 10 microM)"]
  [PMID:1400419 "Both transporters require sodium and chloride for transport"]
- Human GAT-3 cloned and functionally expressed; inhibited by (S)-SNAP-5114 (selective
  GAT-3 inhibitor, IC50 ~5 uM).
  [PMID:7874447 "In the present communication we describe the cloning and expression"]
- **Secondary substrates** (same Na+/Cl- symport mechanism, physiologically lower
  priority than GABA): beta-alanine, and to a lower extent taurine and hypotaurine
  (UniProt catalytic-activity entries, mostly By similarity to mouse P31650).
  [file:human/SLC6A11/SLC6A11-uniprot.txt "of beta-alanine and to a lower extent that of taurine and hypotaurine"]
- **Guanidinoacetate (GAA)** is a genuine substrate: human GAT3 (and GAT2/SLC6A13)
  expressed in CHO cells take up GAA in a Na+/Cl--dependent, GABA-sensitive manner;
  astrocytic GAT2/GAT3 are proposed to be major routes of GAA handling in brain. GAA is
  a monocarboxylic acid, hence the GO:0008028/GO:0015718 "monocarboxylic acid transport"
  IDA rows. This is a real but secondary activity, not the gene's core evolved function.
  [PMID:29175673 "GAT3/SLC6A11 and BGT1/SLC6A12 exhibited GAA transport"]
  [PMID:29175673 "GAA uptake by rat brain slices was Na+- and Cl--dependent"]
  [PMID:29175673 "play major roles in GAA uptake as regulatory"]

## Localization

- Plasma-membrane (cell-membrane), multi-pass integral membrane protein.
  [file:human/SLC6A11/SLC6A11-uniprot.txt "Cell membrane"]
  [file:human/SLC6A11/SLC6A11-uniprot.txt "Multi-pass membrane protein"]
- **Predominantly astrocytic/glial.** GAT-3 localizes to (perisynaptic) astrocytic
  processes, in contrast to GAT-1 (SLC6A1) which is the mainly neuronal/presynaptic
  transporter. Immunogold and human-hippocampus studies place GAT-3 in protoplasmic
  astrocytes; only some GAT-3+ astrocytic processes abut GABAergic profiles (Frontiers
  Neuroanat 2014, 10.3389/fnana.2014.00072; human epileptogenic hippocampus,
  PMID:16456667). Not a verbatim-cited reference here, used only to judge localization rows.
- Consequence for annotation: `is_active_in GABA-ergic synapse` / `synapse` are
  defensible (perisynaptic astrocytic membrane participating in GABA clearance at
  GABAergic synapses) but peripheral (KEEP_AS_NON_CORE). `presynaptic membrane`
  (GO:0042734) and `postsynaptic membrane` (GO:0045211), transferred electronically
  from rodent orthologs, are over-annotations for a glial transporter
  (MARK_AS_OVER_ANNOTATED).
- Tissue: widespread in brain (brain-enriched per HPA).
  [file:human/SLC6A11/SLC6A11-uniprot.txt "Widespread distribution in the brain"]

## Function / role

- Core role: Na+/Cl--driven reuptake/clearance of GABA from the extracellular/synaptic
  space (termination/recycling of GABAergic signalling), performed mainly by astrocytes.
  Core process modelled as GABA reuptake (GO:0051936) / GABA import (GO:0051939); the
  gene product is the entity that performs the transport step.

## GO-term ontology checks (OLS)

- GO:0005332 (GABA:sodium:chloride symporter activity) is_a ancestors include
  GO:0005283 (amino acid:sodium symporter) and GO:0015370 (solute:sodium symporter) ->
  both are strictly-asserted is_a ancestors, so with GO:0005332 ACCEPTed they are
  TOO_GENERAL. GO:0015378 (sodium:chloride symporter) is NOT an ancestor of GO:0005332
  (and is not annotated here).
- GO:0051936 (GABA reuptake) is_a ancestors include GO:0001504 (neurotransmitter
  uptake), GO:0006836 (neurotransmitter transport), GO:0006865 (amino acid transport),
  GO:0015812 (GABA transport) -> these broader process rows are TOO_GENERAL once
  GABA reuptake is accepted.
- GO:0003333 (amino acid transmembrane transport) is NOT an ancestor of GABA reuptake
  (different branch), so TOO_GENERAL cannot be anchored; it is a correct-but-general
  substrate statement -> MODIFY to GO:0015812 (GABA transport, substrate refinement).
  No BP "GABA transmembrane transport" term exists (only MF GO:0015185).
- GO:0016020 (membrane) -> MODIFY to GO:0005886 (plasma membrane), the supported
  specific location.

## Action summary (29 GOA rows)

- Core MF: GO:0005332 GABA:sodium:chloride symporter activity (ACCEPT; IDA PMID:7874447 + IBA + TAS).
- Core CC: GO:0005886 plasma membrane (ACCEPT x4).
- Core BP: GO:0051936 GABA reuptake (ACCEPT; Reactome TAS) = GABA clearance.
- TOO_GENERAL: GO:0005283, GO:0015370 (MF symporter ancestors); GO:0001504, GO:0006836 (x2),
  GO:0006865 (BP transport ancestors).
- MODIFY: GO:0003333 -> GO:0015812; GO:0016020 (x2) -> GO:0005886.
- KEEP_AS_NON_CORE: GO:0005369 + GO:0015734 (taurine, secondary); GO:0008028 + GO:0015718
  (GAA/monocarboxylate, secondary); GO:0035725 (Na+ cotransport, part of symport);
  GO:0045202 synapse; GO:0098982 GABAergic synapse.
- MARK_AS_OVER_ANNOTATED: GO:0016597 amino acid binding (mechanistic substrate binding,
  uninformative); GO:0009410 response to xenobiotic stimulus (peripheral electronic
  transfer); GO:0042734 presynaptic membrane, GO:0045211 postsynaptic membrane (neuronal
  compartments, GAT-3 is glial).
- No bare GO:0005515 protein binding present; no REMOVE actions warranted.
