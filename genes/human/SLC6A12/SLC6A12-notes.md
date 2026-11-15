# SLC6A12 (BGT1 / BGT-1) curation notes

UniProt: P48065 (S6A12_HUMAN). HGNC:11045. 614 aa. Chromosome 12p13.
"Sodium- and chloride-dependent betaine transporter"; AltName BGT-1,
Na(+)/Cl(-) betaine/GABA transporter, Solute carrier family 6 member 12.

## Core biology

BGT1 is a secondary-active, Na+- and Cl--dependent symporter of the
SLC6/neurotransmitter:sodium symporter (SNF, TC 2.A.22) family, SLC6A12
subfamily. It co-transports its organic substrate together with Na+ and Cl-
down the Na+ electrochemical gradient (symport, NOT antiport or uniport). It is
a single-subunit 12-TM polytopic membrane protein with no heavy chain / no
obligate heteromeric partner (contrast SLC7/SLC3 heteromeric amino-acid
transporters). PDB cryo-EM structures 9LNM/9LNN/9LNO/9W97-9W9C (2.6-3.2 A).

Two genuine physiological substrates:
- **GABA (4-aminobutanoate)** — high affinity. Km = 20 uM for GABA transport,
  coupling stoichiometry 3 Na+ : 2 Cl- : 1 GABA
  [PMID:7589472 "Functional studies reveal a Km = 20 microM for GABA transport and a coupling to Na+ and Cl- with a stoichiometry 3 Na+:2 Cl-:1 GABA"].
  Human BGT1 brain clone: high affinity for GABA (IC50 ~30 uM)
  [PMID:7861179 "The transporter displays high affinity for GABA (IC50 of 30 microM)"].
- **Glycine betaine (betaine)** — the osmolyte substrate, LOW affinity in human
  (betaine ~25-fold weaker than GABA, IC50 ~1 mM)
  [PMID:7861179 "The osmolyte betaine is approximately 25-fold weaker than GABA, displaying an IC50 of approximately 1 mM"].
  UniProt records a betaine symport reaction (glycine betaine + 2 Cl- + 3 Na+)
  by similarity to canine BGT1 (P27799) [UniProt CC CATALYTIC ACTIVITY,
  ECO:0000250|UniProtKB:P27799].

ChEBI / Rhea (from UniProt record):
- GABA reaction RHEA:70731: 4-aminobutanoate CHEBI:59888, chloride CHEBI:17996,
  Na+ CHEBI:29101. Evidence ECO:0000269|PubMed:7589472 (experimental).
- Betaine reaction RHEA:71175: glycine betaine CHEBI:17750, chloride CHEBI:17996,
  Na+ CHEBI:29101. Evidence ECO:0000250|UniProtKB:P27799 (by similarity).

## Expression / localization

Expressed in kidney (inner medulla), liver, heart, skeletal muscle, placenta,
and widespread in brain [PMID:7589472; UniProt TISSUE SPECIFICITY]. HPA: group
enriched kidney, liver. Subcellular: basolateral cell membrane; in kidney it
localizes to basolateral membranes of renal medulla, in liver to hepatocyte
cell membrane [UniProt CC SUBCELLULAR LOCATION, ECO:0000250|UniProtKB:P31651].
Multi-pass membrane protein (12 TM). Physiological role of the betaine branch is
osmoregulatory (accumulation of the compatible osmolyte betaine in hyperosmotic
renal medulla; probable renal/hepatic osmotic regulation) [UniProt CC FUNCTION].
In brain, BGT1 is a low-affinity/low-abundance GABA transporter that is
predominantly non-neuronal (leptomeningeal / extrasynaptic glial); UniProt only
hedges a possible presynaptic GABA-reuptake role ("May have a role in regulation
of GABAergic transmission ... through the reuptake of GABA into presynaptic
terminals").

## Guanidinoacetate (GAA) — the "monocarboxylic acid" annotations

GO:0008028 (monocarboxylic acid transmembrane transporter activity, IDA) and
GO:0015718 (monocarboxylic acid transport, IDA), both ARUK-UCL from
PMID:29175673, are NOT betaine/GABA. They encode **guanidinoacetate (GAA)**
transport. GAA is a guanidino-substituted monocarboxylic acid, so the
substrate->term mapping is chemically correct (this is NOT a resource/mapping
defect). However the paper shows BGT1's GAA transport is real but minor:
- "CHO cells expressing human GAT2/SLC6A13, GAT3/SLC6A11 and BGT1/SLC6A12
  exhibited GAA transport, whereas CHO cells expressing GAT1/SLC6A1 did not."
- "our results suggest that astrocytic GAT2/Slc6a13 and GAT3/Slc6a11 play major
  roles in GAA uptake ... while TauT/Slc6a6, BGT1/Slc6a12, and CRT/Slc6a8 make
  relatively small contributions."
Decision: MARK_AS_OVER_ANNOTATED (not REMOVE: the activity is genuinely
demonstrated for human BGT1; not ACCEPT: it is a minor, physiologically
uncertain secondary activity captured by an over-generic "monocarboxylic acid"
genus term that misrepresents a betaine/GABA transporter). No source_defect.

## Interactions (protein binding IPI rows)

GO:0005515 bare "protein binding": SCRIB (Q14160; PDZ scaffold; PMID:21525870,
PMID:24550280 PDZ phage-display / specificity screens), REL (Q04864;
PMID:25416956 interactome), CD79A (P11912; PMID:32296183 binary interactome).
BGT1 has a C-terminal PDZ ligand (...ETHL) consistent with SCRIB/LIN7C binding
(UniProt SUBUNIT: interacts with LIN7C, by similarity). All are uninformative
bare protein-binding rows from large-scale screens -> REMOVE per the
protein-binding policy (sanctioned REMOVE exception). No informative adapter MF
is established.

## Ontology is_a checks (OLS, go)

- GO:0005332 (GABA:Na:Cl symporter) is_a GO:0015171 (amino acid TM transporter
  activity) and is_a GO:0015370 (solute:sodium symporter activity) -> both
  GO:0015171 (Reactome TAS) and GO:0015370 (ARBA IEA) are TOO_GENERAL.
- GO:0015812 (GABA transport) is_a GO:0006865 (amino acid transport) -> GO:0006865
  (IBA + TAS) TOO_GENERAL. GO:0015812 is NOT under GO:0003333 (amino acid
  transmembrane transport) nor under GO:0006836 -> cannot TOO_GENERAL those via it.
- GO:0051936 (GABA reuptake) is_a GO:0006836 (neurotransmitter transport) AND
  is_a GO:0006865 -> GO:0006836 (InterPro IEA) TOO_GENERAL (descendant GO:0051936).
- GO:0003333 (amino acid transmembrane transport, IEA GO_REF:0000108 inferred
  from MF GO:0015171): no ACCEPTed strict is_a descendant among the annotations
  -> MODIFY (lateral, substrate-specific) to GO:0015812 (GABA transport), the
  specific substrate class the gene is experimentally shown to move.
- GO:0005886 plasma membrane is_a GO:0016020 membrane -> GO:0016020 MODIFY to
  GO:0005886.

## Action summary rationale

Core MFs: GO:0005332 (GABA:Na:Cl symporter, high-affinity, IDA-grounded) and
GO:0140814 (glycine betaine:Na:Cl symporter, osmolyte, ISS/by-similarity).
Betaine/osmoregulation is the better-characterized dominant physiological role
in kidney; GABA transport is the higher-affinity, experimentally directly
measured activity. Both retained as core.
