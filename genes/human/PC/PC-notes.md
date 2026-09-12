# PC (Pyruvate carboxylase, mitochondrial) — review notes

UniProt: P11498 (PYC_HUMAN); HGNC:8636; EC 6.4.1.1; 1178 aa precursor, mitochondrial transit peptide 1-20.

## Core biology (verified)

- Biotin-dependent, ATP-dependent carboxylation of pyruvate to oxaloacetate:
  hydrogencarbonate + pyruvate + ATP = oxaloacetate + ADP + phosphate + H+ (RHEA:20844).
  [file:UniProt CATALYTIC ACTIVITY; ECO:0000269|PubMed:9585002]
- Two-step mechanism: ATP-dependent carboxylation of covalently attached biotin (biotin
  carboxylase / BC domain), then carboxyl transfer to pyruvate (carboxyltransferase / CT
  domain). Biotin covalently attached at Lys-1144 (BCCP / biotinyl-binding domain).
  [file:UniProt FUNCTION; PMID:18297087]
- Homotetramer; F1077 required for tetramerization/activity (F1077A/E = inactive dimer).
  Mn(2+) cofactor (1 per subunit); biotin cofactor. [PMID:18297087]
- Allosterically activated by acetyl-CoA; inhibited by 2-oxoglutarate/L-malate/L-glutamate.
  [reactome:R-HSA-70501]
- Anaplerotic: replenishes TCA-cycle oxaloacetate; committed first step of gluconeogenesis
  from pyruvate/lactate (liver, kidney). Also feeds lipogenesis (adipose, liver, brain),
  neurotransmitter synthesis, insulin secretion. [file:UniProt FUNCTION; PMID:18297087;
  reactome:R-HSA-3323111]
- Subcellular location: mitochondrial matrix. [file:UniProt SUBCELLULAR LOCATION; PMID:9585002]

## Disease
- Pyruvate carboxylase deficiency (MIM:266150; MONDO:0009949), autosomal recessive:
  lactic acidosis, hypoglycemia, neurologic dysfunction/intellectual disability, death.
  Types A (infantile), B (severe neonatal), C (benign). [file:UniProt DISEASE;
  ~/repos/dismech/kb/disorders/Pyruvate_Carboxylase_Deficiency_Disease.yaml]

## Annotation assessment highlights

- Catalytic + gluconeogenesis + mito matrix + biotin/ATP/metal binding are all strongly
  supported (EXP/IMP/IBA/TAS + UniProt + structure). Core.
- CYTOSOL / CYTOPLASM annotations: PC is canonically mitochondrial matrix. A cytosolic
  pool participates in the cytosolic "hydride transfer complex" (HTC: MDH1 + ME1 +
  cytosolic PC) that shuttles reducing equivalents NADH->NADP+ in cancer/hypoxic cells
  [PMID:34547241]. Cytosol/cytoplasm annotations kept as non-core (context-specific,
  minor pool) rather than removed.
- NAD+/NADP+ metabolic process (IDA, ComplexPortal, PMID:34547241): via the cytosolic HTC.
  Real but non-core / context-specific (cancer, senescence bypass).
- Viral process IMPs (viral RNA genome packaging GO:0019074, viral release GO:0019076,
  host-mediated activation of viral process GO:0044794, negative regulation of gene
  expression GO:0010629; all IMP, PMID:23861867): PC is a host metabolic enzyme that HCV
  NS5A binds (via PC biotin carboxylase domain) and whose promoter NS5A downregulates;
  silencing PC reduces infectious particle production. These are indirect
  metabolic-dependency / host-pathogen effects, not core PC molecular functions ->
  MARK_AS_OVER_ANNOTATED. Note GO:0010629 is actually NS5A downregulating PC's own
  promoter (PC is the target, not the actor) — over-annotation.
- protein binding (GO:0005515) IPIs: uninformative; MARK_AS_OVER_ANNOTATED per policy
  (do not REMOVE). identical protein binding (GO:0042802) reflects the homotetramer —
  genuine, keep as non-core supporting detail.
- IEA catalytic activity (GO:0003824) is a correct but over-general parent of the specific
  pyruvate carboxylase activity -> MODIFY to GO:0004736.

## Deep research
- `just deep-research-falcon human PC` failed: scripts/deep_research_wrapper.py uses
  PEP 604 `dict | None` type syntax incompatible with the interpreter (TypeError at import).
  No PC-deep-research-falcon.md produced. Grounded review in UniProt, GOA, cached
  publications, disorders KB, and cached Reactome entries instead.
</content>
