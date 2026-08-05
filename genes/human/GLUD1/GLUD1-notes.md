# GLUD1 (Glutamate dehydrogenase 1, mitochondrial) — review notes

UniProt: P00367 (DHE3_HUMAN). HGNC:4335. Gene: GLUD1 (Synonym GLUD). 558 aa precursor,
with an N-terminal mitochondrial transit peptide (residues 1..53); mature chain 54..558.
EC 1.4.1.3.

## Core biology (from UniProt P00367 and cited literature)

- **Function.** "Mitochondrial glutamate dehydrogenase that catalyzes the conversion of
  L-glutamate into alpha-ketoglutarate. Plays a key role in glutamine anaplerosis by
  producing alpha-ketoglutarate, an important intermediate in the tricarboxylic acid
  cycle" [file:human/GLUD1/GLUD1-uniprot.txt "Mitochondrial glutamate dehydrogenase that catalyzes the"].
  Also "Plays a role in insulin homeostasis" and "May be involved in learning and memory
  reactions by increasing the turnover of the excitatory neurotransmitter glutamate (By
  similarity)".
- **Catalytic activity (dual cofactor).** UniProt lists two reactions:
  - L-glutamate + NAD(+) + H2O = 2-oxoglutarate + NH4(+) + NADH + H(+) (RHEA:15133), EC 1.4.1.3
  - L-glutamate + NADP(+) + H2O = 2-oxoglutarate + NH4(+) + NADPH + H(+) (RHEA:11612), EC 1.4.1.3
  So the enzyme uses both NAD+ and NADP+ — the umbrella MF is GO:0004353
  "L-glutamate dehydrogenase [NAD(P)+] activity" (parents GO:0004352 NAD+ and GO:0004354 NADP+).
  PMID:11254391 (bovine GDH structures): "only animal GDH utilizes both NAD(H) or NADP(H)
  with comparable efficacy".
- **Reaction direction / reversibility.** Fang et al.: "Glutamate dehydrogenase (GDH)
  catalyses the reversible oxidative deamination of l-glutamate to 2-oxoglutarate in the
  mitochondrial matrix" [PMID:11903050 "catalyses the reversible oxidative deamination of l-glutamate to 2-oxoglutarate in the mitochondrial matrix"].
  Reactome models both directions (R-HSA-70600 forward, R-HSA-70589 reverse).
- **Allosteric regulation.** "Subject to allosteric regulation. Activated by ADP
  (PubMed:11903050). Inhibited by GTP and ATP ... ADP can occupy the NADH binding site and
  activate the enzyme (PubMed:16023112). Inhibited by SIRT4 (PubMed:16959573)"
  [file:human/GLUD1/GLUD1-uniprot.txt]. Leucine is an allosteric activator; ADP sensitizes
  the enzyme to leucine [PMID:11032875 "the presence of ADP (10-50 microM:) sensitized the two isoenzymes to"].
  Nonactivated GLUD1 is potently inhibited by GTP (IC50 = 0.20 microM)
  [PMID:11032875 "Nonactivated GLUD1 GDH was markedly inhibited"].
- **Quaternary structure.** Homohexamer [file:human/GLUD1/GLUD1-uniprot.txt "Homohexamer (By similarity)"];
  ADP-ribosylation occurs on one subunit per catalytically active homohexamer
  [PMID:16023112 "a modification of one subunit per catalytically active homohexamer"].
- **PTM / SIRT4.** "SIRT4 is a mitochondrial enzyme that uses NAD to ADP-ribosylate and
  downregulate glutamate dehydrogenase (GDH) activity" [PMID:16959573 "uses NAD to ADP-ribosylate and \ndownregulate glutamate dehydrogenase (GDH) activity"].
  ADP-ribosylation site is Cys172 in the mature-numbering UniProt feature (paper identifies
  the reactive Cys as "Cys119" in their synthetic-gene numbering) [PMID:16023112 "only Cys119 \nmutants showed a significant reduction in the ADP-ribosylation"].

## Localization

- Mitochondrion + endoplasmic reticulum. UniProt SUBCELLULAR LOCATION: "Mostly translocates
  into the mitochondria, only a small amount of the protein localizes to the endoplasmic
  reticulum" [file:human/GLUD1/GLUD1-uniprot.txt "only a small amount of the protein"].
  Experimental basis PMID:19448744: "while most of the hGDHs translocate into the
  mitochondria (a process associated with cleavage of the signal sequence), part of the
  protein localizes to the endoplasmic reticulum" [PMID:19448744 "part of the protein localizes to the endoplasmic reticulum"].
- Reactome places the active enzyme in the mitochondrial matrix (GO:0005759).
- Cytoplasm (GO:0005737, IDA PMID:18688271): Rosso et al. showed "GLUD1 localizes to the
  mitochondria as well as the cytoplasm" whereas GLUD2 is mitochondria-specific
  [PMID:18688271 "GLUD1 localizes to the mitochondria as well as the cytoplasm"]. This is a
  minor pool; the mitochondrial matrix is the primary site of function.

## Disease

- **Hyperinsulinemic hypoglycemia, familial, 6 (HHF6 / HI/HA syndrome; MIM:606762).** Autosomal
  dominant, "hypoglycemia due to congenital hyperinsulinism combined with persistent
  hyperammonemia" [file:human/GLUD1/GLUD1-uniprot.txt "combined with"]. Caused by gain-of-function
  regulatory mutations that desensitize GDH to GTP inhibition: "Mutations of glutamate
  dehydrogenase cause the hyperinsulinism/hyperammonemia syndrome by desensitizing glutamate
  dehydrogenase to allosteric inhibition by GTP" [PMID:11502802 "by desensitizing glutamate \ndehydrogenase to allosteric inhibition by GTP"]. Loss of GTP inhibition leaves leucine
  activation unopposed, producing exaggerated leucine-stimulated insulin release
  [PMID:11502802 "excessively increased insulin \nresponses to leucine"].

## Interactions

- KLHL22 (Q53GT1): cryo-EM structure of CUL3(KLHL22)-RBX1 bound to a GDH1 hexamer;
  "CULLIN3KLHL22-RBX1 ligase mediated the polyubiquitination of GDH1 in vitro"
  [PMID:37788672 "CULLIN3KLHL22-RBX1 ligase mediated the polyubiquitination of GDH1 in vitro"].
  So KLHL22 is a CUL3 substrate-adapter that ubiquitinates GDH1. UniProt records this
  IntAct interaction (NbExp=10).
- GLUD2 (P49448): paralog; recorded IntAct interaction.
- High-throughput interactome IPIs (BioPlex: PMID:28514442, PMID:33961781; cell-map:
  PMID:40205054) contribute generic "protein binding" annotations.

## Annotation review reasoning (summary)

- Core molecular function = **GO:0004353 L-glutamate dehydrogenase [NAD(P)+] activity**
  (dual cofactor). The cofactor-specific children GO:0004352 (NAD+) and GO:0004354 (NADP+)
  are experimentally supported (NAD+ EXP/IDA in multiple papers; NADP+ EXP PMID:11032875)
  and kept as ACCEPT / non-core specializations.
- Regulatory-ligand binding (ADP GO:0043531, GTP GO:0005525, L-leucine GO:0070728, NAD+
  GO:0070403) are genuine allosteric/cofactor-binding functions; ADP binding is core to the
  ADP-activated physiological state, others kept as accepted non-core.
- Localization: mitochondrion/mitochondrial matrix are core; ER and cytoplasm are minor real
  pools kept as non-core.
- Insulin-secretion and substantia-nigra/neuro terms are real physiology but downstream/
  tissue-specific → KEEP_AS_NON_CORE (or over-annotation for HEP proteomics).
- Bare "protein binding" (GO:0005515) IPIs → MARK_AS_OVER_ANNOTATED (uninformative; the
  meaningful partner KLHL22 is captured structurally but the GO term itself is not
  informative).
- No experimental annotation is REMOVEd. Wrong-branch / redundant IEA (oxidoreductase
  activity, generic amino acid metabolic process) → MODIFY or KEEP_AS_NON_CORE per policy.
</content>
</invoke>
