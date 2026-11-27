# ETFDH (human, UniProtKB:Q16134) — review notes

## Summary of gene function

ETFDH encodes **electron transfer flavoprotein-ubiquinone oxidoreductase (ETF-QO / ETF
dehydrogenase; EC 1.5.5.1)**, a monotopic iron-sulfur flavoprotein of the mitochondrial
**inner membrane**. It accepts electrons from reduced electron-transfer flavoprotein (ETF,
the matrix-soluble ETFA/ETFB heterodimer) and transfers them to **ubiquinone** in the
respiratory chain. This is the terminal step of an electron-transfer relay that couples
~10-11 mitochondrial FAD-dependent flavoprotein dehydrogenases (fatty-acid beta-oxidation
acyl-CoA dehydrogenases; amino-acid and choline catabolism dehydrogenases) to oxidative
phosphorylation.

Cofactors: one **FAD** and one **[4Fe-4S] cluster**; both redox centers are in a 64-kDa
mature monomer.

## Key provenance

- Reaction / linkage to respiratory chain:
  [file:UniProt Q16134 FUNCTION "Links fatty acid beta-oxidation and amino acid catabolism to the respiratory chain by transferring electrons from the electron transfer flavoprotein (ETF) to ubiquinone."]
- Inner membrane localization & mechanism (both cofactors in 64-kDa monomer):
  [PMID:8306995 "Electron-transfer flavoprotein-ubiquinone oxidoreductase (ETF-QO) in the inner mitochondrial membrane accepts electrons from electron-transfer flavoprotein which is located in the mitochondrial matrix and reduces ubiquinone in the mitochondrial membrane. The two redox centers in the protein, FAD and a [4Fe4S]+2,+1 cluster, are present in a 64-kDa monomer."]
- Component of electron-transfer system linking 10 dehydrogenases to bc1:
  [PMID:12049629 "Electron transfer flavoprotein-ubiquinone oxidoreductase (ETF-QO) is an iron-sulphur flavoprotein and a component of an electron-transfer system that links 10 different mitochondrial flavoprotein dehydrogenases to the mitochondrial bc1 complex via electron transfer flavoprotein (ETF) and ubiquinone."]
- Quinone/ubiquinone binding, single site per monomer:
  [PMID:14640977 "consistent with one ubiquinone-binding site per ETF-QO monomer"]
- 4Fe-4S flavoprotein, inner membrane, catalyzes UQ reduction by ETF:
  [PMID:17050691 "Electron transfer flavoprotein-ubiquinone oxidoreductase (ETF-QO) is a 4Fe4S flavoprotein located in the inner mitochondrial membrane. It catalyzes ubiquinone (UQ) reduction by ETF, linking oxidation of fatty acids and some amino acids to the mitochondrial respiratory chain."]
- Single [4Fe-4S] and one FAD per monomer, links primary flavoprotein dehydrogenases with
  main respiratory chain:
  [PMID:18037314 "Human, porcine, and Rhodobacter sphaeroides ETF-QO each contain a single [4Fe-4S](2+,1+) cluster and one equivalent of FAD"]
- MADD / secondary CoQ10 deficiency (disease → beta-oxidation involvement):
  [PMID:17412732 "All of our patients carried autosomal recessive mutations in ETFDH, suggesting that ETFDH deficiency leads to a secondary CoQ10 deficiency."]

## Disease

Biallelic loss-of-function → **glutaric acidemia type II / multiple acyl-CoA dehydrogenase
deficiency (MADD)**, a disorder of fatty acid, amino acid and choline metabolism; the
late-onset myopathic form is frequently **riboflavin-responsive** and is associated with a
**secondary (myopathic) CoQ10 deficiency** (PMID:17412732). Corroborated by the disorder KB
(`dismech/kb/disorders/Multiple_Acyl-CoA_Dehydrogenase_Deficiency.yaml`), which also notes an
ETFDH-CIII-COQ2 metabolon that routes lipid-derived electrons into the respiratory chain.

## Annotation review reasoning

- **MF core = GO:0004174** electron-transferring-flavoprotein dehydrogenase activity (EC
  1.5.5.1). Directly supported by IDA (PMID:12049629, PMID:8306995, PMID:14640977). IBA/IEA/TAS
  duplicates ACCEPT.
- Cofactor binding: **GO:0050660 FAD binding** (ISS, supported by structure/homolog + UniProt
  BINDING features); **GO:0051539 4 iron, 4 sulfur cluster binding** (IDA PMID:18037314);
  **GO:0051536 iron-sulfur cluster binding** (IEA) is the parent of 0051539 — accept as broader.
- **GO:0048039 ubiquinone binding** (IDA, PMID:14640977) — specific & supported; core.
  **GO:0048038 quinone binding** is its parent (IDA same paper) — accept as broader.
- **GO:0009055 electron transfer activity** (IDA x2) — accurate; the enzyme is an electron
  carrier. Keep (non-core relative to the specific dehydrogenase MF, but correct).
- **GO:0016491 oxidoreductase activity** (IDA) — correct but very general parent of GO:0004174;
  MARK_AS_OVER_ANNOTATED (root-ish MF).
- CC: **GO:0005743 mitochondrial inner membrane** (IBA is_active_in, IDA PMID:8306995, IEA
  SubCell, TAS Reactome) — core location. **GO:0031966 mitochondrial membrane** (IDA) and
  **GO:0005739 mitochondrion** (IDA/HTP/IEA) are broader parents — accept as broader / non-core.
- BP: **GO:0022900 electron transport chain** (IBA/IDA/IEA) and **GO:0022904 respiratory
  electron transport chain** (TAS Reactome) — core process; ETF-QO feeds UQ pool.
  **GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase** (IMP PMID:17412732) —
  ETFDH is required for FAO flux (electron sink); accept as the biologically central linked
  process (its role is to accept the electrons from the acyl-CoA dehydrogenation step).
- **GO:0006979 response to oxidative stress** (IEA from mouse ortholog Ensembl; ISS from mouse
  Q921G7) — this is an ortholog-transferred phenotype-adjacent term, not a direct molecular
  function of ETF-QO; not core. Keep as non-core (mouse ETFDH KO shows oxidative-stress
  phenotype; over-propagated but not clearly wrong) — MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE.
- **GO:0005515 protein binding** (IPI x7, PMID:32296183 HuRI Y2H) — bare protein binding to
  keratin-associated proteins, transcription factors (OTX1, GSC2, ZNF581), MYH7B, TRIM69 — no
  functional relevance to a mitochondrial inner-membrane oxidoreductase; classic high-throughput
  Y2H artifacts. Per policy: MARK_AS_OVER_ANNOTATED (not REMOVE), and per curation guideline the
  bare "protein binding" term is uninformative.

Deep research (falcon) file was NOT produced within the 8-min poll window; grounding is from
UniProt Q16134, seeded GOA, the cached experimental publications above, and the MADD disorder KB.


## Annotation integration, 24 October 2026

All 37 current contexts have now been reviewed: 16 ACCEPT, 12 MODIFY, seven KEEP_AS_NON_CORE and two UNDECIDED. The original 31 positions remain fixed. The previous single HuRI context expands to seven exact partner contexts: the first fresh context, MYH7B, occupies original position 8 and the other six are appended at positions 31–36. The inherited paper-title quotation is citation context only and is not evidence for any particular interaction or exact clone identity. The actual HuRI pair/method records support the contextual interactions. The archived MYH7B clone does not match the current short A7E2Y1-2 sequence, so no current-product equivalence is asserted.

Earlier statements above that dismiss HuRI hits as artifacts because of their expected compartment, or describe a mouse ETFDH knockout oxidative-stress phenotype, are historical and superseded by this evidence assessment. The seven supported interactions are retained as non-core; expected localization does not erase a measured screen interaction. The two oxidative-stress contexts remain UNDECIDED because their actual mouse source, PMID:17023274, reports oxidative modification and the complete response-role experiment remains inaccessible. The inherited GO_REF quotations describe transfer methods and do not resolve that biological role. This applies the campaign's [supported-binding instruction](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions) and the standing instruction to add no new publication quotations.

Specificity refinements use independently established ETFDH dehydrogenase activity, respiratory electron transport, inner mitochondrial membrane and 4Fe–4S binding. Broader quinone binding remains supported by actually tested alternative quinones. The revised assessments distinguish human protein expressed in yeast or Sf9 cells, native porcine structure, clinical evidence, protein-group proteomics and database participant models. PMID:8306995 remains marked full-text-unavailable because only the specified original pages were recovered; that limit does not negate those operative experiments.

All 42 inherited quotation paths, text and reference associations are preserved. No new publication quotation was added. The two natural product records and five ordered legacy core objects remain unchanged at this annotation checkpoint; descriptions and cores will be assessed in the subsequent synthesis phase. This is an annotation integration checkpoint, not a computed final status or publication claim. Normal sources are preserved, including the genuine additive PMID:17023274 record. Direct URLs, assay locators and access limits are collected in ETFDH-source-guide.md.


## Core synthesis, 24 October 2026

The five ordered core slots are retained as facets of one ETFDH redox enzyme: ETF-to-ubiquinone catalysis, ubiquinone binding, FAD binding, 4Fe–4S binding and the fatty-acid oxidation context of the same catalytic activity. This ordering preserves the seven inherited core quotation anchors; it does not assert five independent enzymes. The fatty-acid branch now also cites the actual human MCAD/ETF/ETFDH coupled assay (PMID:12049629) as bare supporting evidence for executed electron-transfer work. Clinical PMID:17412732 provides physiological context rather than, alone, establishing that chemical step.

Human full-cDNA ETFDH was expressed in yeast or Sf9 cells in the original experiments; the atomic structure is native porcine enzyme. The paired cofactors and quinone chemistry are well supported, while a compulsory internal electron-transfer order, universal native dimerization and physiological use of every tested alternative quinone are not asserted. The processed canonical chain and the alternative 570-residue product remain distinct. Product processing and the role of oxidative modification are retained as explicit questions.

All 37 accepted annotation/source/review objects and nineteen reference identities, findings and access judgments remain exact. All 42 inherited supporting-text paths and reference associations remain exact; new support consists only of bare reference IDs. The two response-to-oxidative-stress annotations remain UNDECIDED. The normal publication caches are immutable. Separately captured genuine GOA/UniProt refreshes are proposed machine inputs, with both preimages and diffs retained; their use is not represented as unchanged machine bytes. Three genuine PAINT auxiliary normal records are also included as source-chain dependencies alongside the eleven citation records.

Final canonical validation passes all six checks, with all 82 authored narratives present in the private rendering. Computed DRAFT retains 7 advisories. All 37 current source contexts have reviewed decisions, including two explicitly unresolved oxidative-stress transfers. All 42 inherited quotation paths, texts and reference associations, two natural products and five ordered core facets remain preserved. The 14 selected publication/Reactome/PAINT normal files and two genuinely refreshed machine inputs remain exact to the accepted selections; all 27 private normal dependency files and eight unrelated baseline paths remain unchanged.
