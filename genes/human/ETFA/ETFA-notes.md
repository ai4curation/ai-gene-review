# ETFA (human) review notes

UniProtKB:P13804 — Electron transfer flavoprotein subunit alpha, mitochondrial (Alpha-ETF).
HGNC:3481. Gene MIM 608053; disease MIM 231680 (Glutaric aciduria 2A). 333 aa precursor;
transit peptide 1..19; mature chain 20..333.

## Verified biology (from -uniprot.txt and cached publications)

- ETF is a soluble mitochondrial-matrix FAD-containing **heterodimer** of ETFA (alpha) +
  ETFB (beta), binding one FAD and one AMP per dimer
  [Reactome R-HSA-169260 "63kDa heterodimer composed of alpha and beta subunits and binds
  one FAD and one AMP per dimer"; PMID:8962055 "Mammalian electron transfer flavoproteins
  (ETF) are heterodimers containing a single equivalent of flavin adenine dinucleotide (FAD)"].
- Most of the FAD binds in the C-terminal (Domain II) portion of the alpha subunit
  [PMID:8962055 "most of the FAD molecule residing in the C-terminal portion of the alpha
  subunit"]. UniProt lists ~16 FAD BINDING residues on ETFA (223..319).
- ETF is the common electron acceptor for at least a dozen mitochondrial matrix FAD-dependent
  acyl-CoA dehydrogenases of fatty-acid beta-oxidation (ACADM/MCAD, ACADVL, etc.) and of
  amino-acid catabolism (IVD, GCDH), plus choline-pathway dehydrogenases (DMGDH, SARDH); it
  passes electrons to ETF-ubiquinone oxidoreductase (ETFDH / ETF-QO), funneling them to the
  respiratory-chain ubiquinone pool
  [PMID:25416781 full text "ETF acts as a mobile electron carrier that shuttles electrons
  between several FAD-containing dehydrogenases present in the mitochondrial matrix and the
  membrane-bound ETF:quinone oxidoreductase ... Altogether, there are 13 human dehydrogenases
  that interact with ETF ... it is the third major provider of electrons to the ubiquinone
  pool of the mitochondrial respiratory chain"].
- UniProt FUNCTION: "Heterodimeric electron transfer flavoprotein that accepts electrons from
  several mitochondrial dehydrogenases, including acyl-CoA dehydrogenases, glutaryl-CoA and
  sarcosine dehydrogenase ... transfers the electrons to the main mitochondrial respiratory
  chain via ETF-ubiquinone oxidoreductase (ETF dehydrogenase) ... Required for normal
  mitochondrial fatty acid oxidation and normal amino acid metabolism."
- SUBCELLULAR LOCATION: Mitochondrion matrix [PMID:3760196]. ETF resides on the matrix face
  of the inner membrane [Reactome].
- Deficiency (ETFA/ETFB/ETFDH) => multiple acyl-CoA dehydrogenase deficiency (MADD) /
  glutaric acidemia type II [MONDO:0009282; dismech MADD KB].

## Annotation decisions summary

Core (ACCEPT): GO:0009055 electron transfer activity (IDA/IBA/IEA); GO:0050660 FAD binding
(IDA/IBA/IEA); GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase (IDA/IBA);
GO:0009063 amino acid catabolic process (IDA); GO:0022904 respiratory electron transport
chain (IDA); GO:0045251 electron transfer flavoprotein complex (IPI); GO:0005759
mitochondrial matrix (IDA/NAS/TAS). Mitochondrion terms (GO:0005739) KEEP_AS_NON_CORE or
ACCEPT (broader parent of matrix; HPA/HTP/HDA localization support).

protein binding (GO:0005515) IPIs: bare, uninformative. Most are high-throughput
interactome/CFTR proximity screens => MARK_AS_OVER_ANNOTATED (policy: not REMOVE). The
ETFRF1 (PMID:27499296) and MBTPS1 (PMID:35362222) interactions are functionally meaningful
(ETFRF1 promotes FAD dissociation; MBTPS1/S1P stabilizes the ETFA/ETFB heterodimer and
promotes FAD binding) but the GO term itself is still bare "protein binding" =>
MARK_AS_OVER_ANNOTATED with notes pointing to informative partners; better captured by
proposed complex/regulation terms rather than protein binding.

## Deep research
Falcon DR file did NOT arrive within the 8-min poll window (timed out, no file). Review is
grounded in UniProt (P13804), GOA, cached publications (PMID:8962055, 9334218, 10423253,
25416781, 3760196, 8504797, 3170610, 8617498, 27499296, 35362222, 34800366, 20833797),
Reactome R-HSA-169260/169270, and the dismech MADD KB.

## Final result
Validation clean (`just validate human ETFA` => Valid) on first run. 35 existing annotations
reviewed: 20 ACCEPT, 6 KEEP_AS_NON_CORE, 9 MARK_AS_OVER_ANNOTATED (all bare protein-binding
IPIs). 4 core_functions (electron transfer activity x3 contexts: respiratory ETC / fatty-acid
beta-ox / amino-acid catabolism; + FAD binding), all in mitochondrial matrix / ETF complex.
19 reference_review blocks added.


## 2026-10-24 — Current source review and preserved history

All 36 current imported contexts are reviewed: 21 ACCEPT, eight MODIFY, two KEEP_AS_NON_CORE and five UNDECIDED. The 35 historical row positions remain fixed. The historical location assertion absent from the current GOA remains in place with retired status and a biological MODIFY to mitochondrial matrix; source absence is not evidence of functional loss. One previously aggregated interaction is now represented by explicit ETFB and LYRM5 contexts, with ETFB retaining the prior row whose summary named that partner and LYRM5 appended independently. The new current ARBA complex assertion is also appended. There are 37 total rows, including one historical row, and no NEW annotation.

All 32 inherited quotation paths, texts and reference associations remain unchanged. The old interaction quotation about LYRM5 is retained at its original position as historical context; it is not the specific proof of ETFB heterodimerization. Accepted independent support follows the inherited support prefix. The source guide separates the actual partner assays and access limits. All 26 reference identities, titles and findings are preserved; 21 references receive the accepted manual access assessments. The original description, four ordered cores, two natural products, questions, experiments and status remain unchanged pending separate synthesis.

Human mature Δ19-alpha/His6-beta DCIP experiments establish ETF electron-carrier function, distinct from ETFDH-mediated ubiquinone reduction, autonomous alpha activity and the untested 284-residue alternative product. The 1996 Q21 label differs from current P13804 Q20/S21; other checked contact residues match. Historical residue statements are retained as paper numbering, without a universal offset. No publication cache or machine source was edited.

### 2026-10-24 — Database-origin annotation assessment

Eleven database-origin contexts were assessed: nine are supported as written, and two broad mitochondrial locations are refined to mitochondrial matrix using explicit human ETFA participant records and the official UniProt location mapping. The HPA observations themselves remain mitochondrial-resolution evidence. Actual PAINT ancestry and canonical sequence support all four inherited assertions; human self-WITH is expected. The current versus captured electron-transfer donor-list difference is retained without rewriting the source.

The human ETF structure establishes alpha-subunit FAD contacts and alpha/beta complex membership. The independent human mature Δ19-alpha/His6-beta assay establishes electron transfer from MCAD or GCDH to DCIP. ETFDH performs the subsequent ubiquinone reaction in the Reactome model. These roles are kept distinct. The current ARBA rule is unavailable, but the ETF complex assertion is independently supported; no rule conditions were invented.

The two natural ETFA products remain separate. Neither the human heterodimer experiments nor antibody antigen overlap establishes equal function or location of the 284-residue product. No new process annotation, core function, publication quotation or normal publication-cache alteration was made in this assessment. The source guide records actual article sections, image inspection and access limits.


## 2026-10-24: Core attribution and assay scope

The four inherited core positions remain ordered as electron transfer, FAD binding, fatty-acid oxidation context and amino-acid catabolic context. They describe two molecular facets and two metabolic settings of the same ETF carrier, not four independent enzymes. Electron transfer is attributed to ETFA as a contribution within the ETFA–ETFB complex; direct alpha-subunit FAD contacts support the separate FAD-binding facet. All seven inherited core quotation anchors and all 32 quotations across the review remain at their original paths. The 37 accepted annotation reviews, 26 reference objects and two natural-product records are unchanged. No annotation or publication quotation is added.

The human ETF crystal structure resolves a composite cofactor environment. The human biochemical preparation uses mature Δ19-alpha plus full-length His6-beta; MCAD/octanoyl-CoA and GCDH/glutaryl-CoA reactions reduce DCIP. These are positive redox-step assays, not complete respiratory or catabolic flux measurements. ETF is itself an electron carrier, rather than a passive substrate whose necessity alone motivates the process attribution. The matrix ETF complex passes electrons to inner-membrane ETFDH; ubiquinone reduction is ETFDH chemistry. The 284-residue alternative product remains untested by these experiments. The original Q21 sequence-numbering inconsistency remains local; other checked contacts agree with the current sequence, and no universal offset is imposed.

The core terms were checked against current official GO definitions and separately filtered is_a and is_a/part_of ancestry. The three process terms have no ancestor/descendant pair among them. Their placement is contextual, not a claim of separate catalytic activities. The 1997/1999 inherited quotation sources retain their previously documented access limits; their preservation does not represent a new original-paper read. Independent human structural and coupled-assay evidence and target-specific Reactome roles support the refined attribution.

Canonical validation: all six status, schema/GOA, strict-term, ontology-component and render checks passed. All 82 authored narratives occur in the private HTML rendering. Computed DRAFT retains two supported generic protein-binding advisories under the explicit [campaign convention](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions). All 32 inherited quotation paths/text/reference associations remain exact; no new publication quotations or NEW annotations were introduced. The two source-machine files are genuine fetched refreshes; the other 38 selected normal dependencies retain their acquired bytes.


## PR feedback clarification, 2026-10-24

The biological summary now describes the one-FAD/one-AMP ETF heterodimer, its fatty-acid/amino-acid/choline electron donors, transfer through ETFDH to ubiquinone and mitochondrial precursor processing. Assay and alternative-product uncertainty remain in the reviews, questions and source guide. The earlier note that the original description and four cores remained unchanged recorded the annotation-integration phase; subsequent accepted synthesis changed the description and cores. It was not a statement about the final published version.

All 32 inherited quotation paths, values and reference associations remain exact under the campaign’s [curation instructions](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions). The FAD-row excerpt from PMID:9334218 describes upstream acyl-CoA dehydrogenases and is explicitly marked contextual rather than FAD evidence in both the row and reference assessment. Independent human structural evidence continues to support FAD binding. The inherited PMID:24606901 motif fragment is likewise non-target-specific; contrary to the external review’s occurrence claim, it appears in the abstract and Discussion as well as the title. The ETFA supplementary target record remains unavailable, and the interaction remains UNDECIDED. No quotation was deleted, replaced, moved or added.

The retired mitochondrial row’s historical GOA source is recoverable as ARBA:ARBA00026962 from the archived TSV, although its imported YAML source lacks supporting_entities. Its historical conditions are not reconstructed, and its absence from fresh GOA does not establish functional loss. This is distinct from current ARBA00092488 complex membership. Source fields remain unchanged. For the latter row, the bare GO_REF method citation is omitted from supported_by because acceptance relies on independent structural/Reactome evidence; its source ID and unavailable-rule provenance remain recorded.

The four ordered core entries are preserved. Three describe the same heterodimer electron-transfer activity in respiratory, fatty-acid and amino-acid contexts; consolidating them would move inherited quotation anchors. The separate alpha FAD-binding facet remains. The broad amino-acid process is retained to cover multiple donor systems rather than narrowing all ETF biology to the reconstituted GCDH reaction. A few repetitive preparation details were shortened without changing action, source scope or scientific conclusions. Supported generic binding continues to follow the campaign’s specific-refinement/non-core rule.

These are authored evidence-context and prose corrections. All 37 source objects, 36 current contexts, historical retirement, 26 reference identities/titles, two products, four cores and review actions are preserved. Whole-gene canonical validation and publication are subsequent operations and are not claimed here.

Revised canonical validation passes all six checks, with all 82 authored narratives present in the private rendering. Computed DRAFT retains two supported generic-binding advisories. All 37 imported source objects (36 active and one retired), 26 reference identities, two natural products, four ordered cores and 32 inherited quotation anchors remain exact. All 40 selected normal sources and eight unrelated baseline files/modes remain unchanged.
