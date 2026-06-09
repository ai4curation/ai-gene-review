# EEF2K (eukaryotic elongation factor 2 kinase) — research notes

UniProt O00418. Alpha-kinase (NOT classical eukaryotic protein-kinase superfamily fold); calcium/calmodulin-dependent.

## Core function
- [PMID:9144159 "we report the existence and wide occurrence in eukaryotes of a protein kinase with a completely different structure ... eEF-2 kinase ... do not contain any sequence motifs characteristic of the eukaryotic protein kinase superfamily ... homologous to the catalytic domain of the recently described myosin heavy chain kinase A (MHCK A)"]
- UniProt FUNCTION: "Threonine kinase that regulates protein synthesis by controlling the rate of peptide chain elongation. Upon activation ... phosphorylates the elongation factor EEF2 at a single site, renders it unable to bind ribosomes and thus inactive. In turn, the rate of protein synthesis is reduced."
- Catalytic activity: eEF2 + ATP -> eEF2-phosphate + ADP; EC=2.7.11.20 [PMID:11015200, PMID:9144159]. Phosphorylates eEF2 on Thr56 [PMID:23184662 "phosphorylation of eukaryotic elongation factor 2 (eEF2) on threonine 56 (T56) by eEF2 kinase (eEF2K)"].
- CaM strictly required [PMID:11015200]. Autophosphorylates (Thr348 major; Thr-348/Thr-56? autophos at multiple residues).

So core MF: elongation factor-2 kinase activity (GO:0004686). Core BP: negative regulation of translational elongation.

## Annotation issues
- GO:0004674 protein serine/threonine kinase activity (IEA) — EEF2K is an ALPHA-kinase, not a conventional Ser/Thr kinase; functionally it phosphorylates Thr but the term implies the classical fold. KEEP_AS_NON_CORE (it is a Ser/Thr-directed kinase) but core is the specific eEF2 kinase activity.
- GO:0008135 translation factor activity, RNA binding (TAS 9144159) — WRONG: EEF2K is a kinase, not a translation factor / RNA-binding factor. Its substrate eEF2 is the translation factor. REMOVE/MARK_AS_OVER_ANNOTATED.
- GO:0046777 protein autophosphorylation (IDA 23184662) — PMID:23184662 is actually about CDK2 phosphorylating eEF2 at S595; it does not primarily document EEF2K autophosphorylation. The 9144159 IDA autophosphorylation is the solid one. Flag 23184662 citation as possibly miscited for autophosphorylation; KEEP but note.
- Synaptic / GO_REF:0000107 IEA terms (postsynaptic density, regulation of translation at postsynapse, dendritic spine, glutamatergic synapse, etc.) — EEF2K does have a documented role in synaptic/dendritic translation control; these are plausible but non-core (neuronal context). KEEP_AS_NON_CORE.
- response to ischemia/anoxia/insulin/cAMP/calcium/BDNF/prolactin (GO_REF:0000107 IEA) — phenotype/context associations; KEEP_AS_NON_CORE or over-annotated. EEF2K is activated by energy stress (AMPK) so anoxia/ischemia context is plausible non-core.
- GO:0004686 elongation factor-2 kinase activity (IBA, IEA, EXP 11015200, IDA 9144159) — ACCEPT core.
- calmodulin binding (IEA, IDA 9144159) — ACCEPT (CaM-dependent kinase; required for activity).
- calcium ion binding (IEA) — via CaM regulation; KEEP_AS_NON_CORE.
- ATP binding (IEA) — kinase cofactor; ACCEPT/KEEP.
