# AUH (methylglutaconyl-CoA hydratase, mitochondrial) — review notes

UniProtKB: Q13825 (AUHM_HUMAN); HGNC:890; gene ID 549; chromosome 9.
339 aa precursor; TRANSIT 1..67 (mitochondrion); CHAIN 68..339. Homohexamer.
Enoyl-CoA hydratase/isomerase (crotonase) superfamily. EC 4.2.1.18 (and 4.2.1.56).

## Bifunctional / moonlighting protein — two genuine functions

### 1. Metabolic enzyme: 3-methylglutaconyl-CoA hydratase (core catalytic function)
- Catalyzes the fifth step of leucine degradation: reversible hydration of
  (E)-3-methylglutaconyl-CoA (3-MG-CoA) to (S)-3-hydroxy-3-methylglutaryl-CoA (HMG-CoA).
  EC 4.2.1.18; RHEA:21536. Physiological direction is hydration (right-to-left in RHEA),
  i.e. 3-MG-CoA -> HMG-CoA; reverse reaction runs at much lower rate in vitro.
  [UniProt Q13825 CATALYTIC ACTIVITY / FUNCTION; PMID:16640564]
- Kinetics (PMID:16640564): best substrates (E)-3-MG-CoA (Vmax 3.9 U/mg, Km 8.3 uM,
  kcat 5.1 /s) and (E)-glutaconyl-CoA (Vmax 1.1 U/mg, Km 2.4 uM). Abstract states:
  "giving strong evidence that the AUH gene encodes for the major human 3-MG-CoA
  hydratase in leucine degradation." Also acts on 3-methylcrotonyl-CoA, crotonyl-CoA,
  3-hydroxybutanoyl-CoA in vitro (broad crotonase-family promiscuity; missing carboxylate
  reduces affinity).
- MGCA1 missense A240V produces enzyme with only 9% of wild-type activity
  [PMID:16640564 abstract; PMID:12655555].
- Disease: 3-methylglutaconic aciduria type I (MGCA1, MIM 250950), autosomal recessive
  inborn error of leucine metabolism [UniProt DISEASE; PMID:12434311; PMID:12655555].
  Note: the local dismech disorder file 3-Hydroxy-3-Methylglutaric_Aciduria.yaml is about
  HMGCL (the DOWNSTREAM lyase), not AUH; it confirms the pathway context (leucine
  degradation, HMG-CoA cleavage to acetyl-CoA + acetoacetate) but AUH's own disease is MGCA1.

### 2. AU-rich element (ARE) RNA-binding protein (second, moonlighting function)
- Original identification: affinity-purified on an AUUUA matrix; recombinant protein
  binds specifically to AU-rich transcripts (IL-3, GM-CSF, c-fos, c-myc 3'UTRs).
  Name AUH = AU-binding protein / enoyl-CoA Hydratase. [PMID:7892223]
- AREs direct rapid mRNA degradation / deadenylation. Hydratase and AU-binding functions
  are on distinct domains of a single polypeptide (immobilized protein still enzymatically
  active) [PMID:7892223].
- Crystal structure (PDB 1HZD, 2ZQQ, 2ZQR): homohexamer; single-stranded RNA-binding homolog
  of enoyl-CoA hydratase; RNA-binding region 105..119; mutagenesis K105N/K109E/K113Q abolishes
  RNA-binding [PMID:11738050; UniProt FT REGION 105..119 + MUTAGEN].

### 3. Possible itaconyl-CoA hydratase activity (C5-dicarboxylate / itaconate detox)
- May convert itaconyl-CoA to (S)-citramalyl-CoA (EC 4.2.1.56; RHEA:13785) in the
  C5-dicarboxylate catabolism pathway that detoxifies macrophage-derived itaconate
  (an anti-microbial metabolite / B12-poisoning precursor) [UniProt FUNCTION;
  PMID:29056341 states the itaconyl-CoA<->citramalyl-CoA hydration is catalyzed by AUH].
  Evidence is TAS/inference (ECO:0000303) — a secondary, context-dependent activity.

## Localization
- Mitochondrion / mitochondrial matrix. N-terminal transit peptide 1..67.
  [UniProt SUBCELLULAR LOCATION; Reactome R-HSA-70785, R-HSA-9914271; PMID:34800366 HTP
  mito proteome]. Note PMID:34800366 full text is a large proteome dataset; AUH not found
  by simple grep of the cached markdown (supplementary/table-based); rely on UniProt +
  Reactome for the matrix localization. Use TAS/HTP annotations as ACCEPT (matrix is the
  more specific, correct compartment).

## Annotation strategy
- CORE MF: GO:0004490 methylglutaconyl-CoA hydratase activity (IDA PMID:16640564 + IBA/IEA).
- GO:0004300 enoyl-CoA hydratase activity: parent/family-level activity; the IDA (PMID:7892223)
  is the historical "low degree of enzymatic activity" observation — real but less precise than
  the physiological 3-MG-CoA hydratase. Keep, mark as over-annotated / accept as family-level.
- GO:0003730 mRNA 3'-UTR binding (IDA PMID:7892223): genuine second function — ACCEPT.
  GO:0003723 RNA binding (IEA): parent, accept.
- GO:0006552 L-leucine catabolic process (IMP PMID:16640564, IEA): core BP — ACCEPT.
- GO:0009083 branched-chain amino acid catabolic process (IEA): parent of leucine catabolism,
  correct, less specific — accept.
- GO:0006635 fatty acid beta-oxidation (IBA): AUH is a crotonase-family member but its
  physiological role is leucine catabolism, NOT fatty-acid beta-oxidation; the IBA is a
  family-level over-propagation (the enoyl-CoA hydratase step of FAO is done by ECHS1/EHHADH,
  not AUH). MARK_AS_OVER_ANNOTATED.
- GO:0050011 itaconyl-CoA hydratase activity (IEA + TAS PMID:29056341) and
  GO:0110052 toxic metabolite repair (TAS PMID:29056341): keep as non-core (secondary,
  inferred activity in itaconate detox).
- GO:0170035 obsolete L-amino acid catabolic process (IEA): term is OBSOLETE -> REMOVE.
- GO:0003824 catalytic activity (IEA, InterPro): uninformative root-level MF, subsumed by
  the specific hydratase term. MARK_AS_OVER_ANNOTATED.
- GO:0005739 mitochondrion (multiple) — accept; GO:0005759 mitochondrial matrix (TAS) is the
  more specific correct compartment — ACCEPT as core location.


## 2026-09-30 UTC — Source-based reassessment

This reassessment supersedes the earlier annotation-strategy judgments above. All 23 original annotation objects and both normal alternative-product records are preserved; the review now records 12 ACCEPT, 6 KEEP_AS_NON_CORE, 4 MODIFY and 1 UNDECIDED. Broad catalysis, RNA binding and amino-acid catabolism are refined to demonstrated activities. No new annotation is proposed. Weak but measured enoyl-CoA hydratase activity is retained as non-core, rather than treated as incorrect because methylglutaconyl-CoA is preferred.

The two core molecular activities are methylglutaconyl-CoA hydration in mitochondrial leucine degradation and binding to AU-rich transcript 3′-UTRs. The original recombinant assays establish RNA binding, while the later structure and mutagenesis identify an exposed lysine-rich surface within the crotonase fold. The older statement that a separate folded RNA-binding domain was demonstrated is withdrawn. ARE binding alone does not establish AUH-driven RNA decay. Sources: [PMID:16640564](https://pubmed.ncbi.nlm.nih.gov/16640564/), [PMID:7892223](https://pubmed.ncbi.nlm.nih.gov/7892223/), [PMID:11738050](https://pubmed.ncbi.nlm.nih.gov/11738050/). These three sources were read at complete-abstract level; no new full-paper inspection is claimed.

The original main text, assay methods, table and figure captions of [PMID:12434311](https://pmc.ncbi.nlm.nih.gov/articles/PMC378594/) were read. Human MBP-AUH showed strong methylglutaconyl-CoA activity and weaker butenoyl-CoA activity in the tested assays; the comparison crotonase was bovine. The reverse-direction assay does not invalidate hydration as the physiological leucine-catabolic direction. The record cites an erratum whose contents remain uninspected. [PMID:12655555](https://pubmed.ncbi.nlm.nih.gov/12655555/) was read at complete-abstract level for the human gene/disease association and variable presentation, without independently reclassifying variants.

Selected original Methods, Results and Discussion of [PMID:24598254](https://pmc.ncbi.nlm.nih.gov/articles/PMC4027184/) identify human NM_001698 constructs in 143B cells, including tagged/untagged expression and E209A/A240V variants. Subfractionation supports predominant matrix localization and an inner-membrane-associated fraction, not integral membrane topology. RNA/ribosome copurification supports association; it does not establish every binary RNA contact. Both depletion and excess AUH perturb mitochondrial translation. The physiological RNA targets and the relationship between catalysis and translation remain explicit questions. Engineered constructs are not equated with natural isoforms; the deletion of residues 140–168 in Q13825-2 is preserved without inventing an isoform-specific function.

The [CLYBL study, PMID:29056341](https://pubmed.ncbi.nlm.nih.gov/29056341/) attributes itaconyl-CoA hydration to AUH through earlier enzymology; its direct experiments center on CLYBL and MUT. The existing TAS assertions for secondary hydratase activity and toxic-metabolite repair remain non-core. The cached production GO-CAM model 68b0f0d000007160 already includes AUH as the hydratase participant, so no pathway-completeness annotation is added. The complete normal abstract and selected AUH Results/Discussion passages were read. The MitoCoP [PMID:34800366](https://pubmed.ncbi.nlm.nih.gov/34800366/) HTP localization is retained in agreement with independent localization; its AUH-specific supplement row was not independently inspected.

All 11 cached family PAINT IBD rows were examined. PTN000234999 supports the hydratase/mitochondrial assertions, with AUH itself providing legitimate experimental grounding. The fatty-acid beta-oxidation placement at PTN000941828 remains UNDECIDED because the full tree/MSA and AUH-specific loss or divergence were not established. Another principal pathway and a short donor list do not disprove the ancestral assertion. The earlier confident overpropagation diagnosis is withdrawn. The official AmiGO record independently confirmed that GO:0170035 is obsolete; its machine-sourced identifier is retained and its underlying process refined to leucine catabolism.

Four missing normal publication records and both cited Reactome records were recovered without altering their fetched bytes. Full-text availability remains two abstract-only records (11738050, 12655555), one HTML extraction (12434311) and one XML extraction (24598254). Both Reactome summaries and machine titles were read and preserved, including their original wording. New YAML excerpts are exact cache substrings totaling at most 25 words per source. Historical notes above remain unchanged.

The prescribed Falcon/perplexity-lite launcher attempt did not produce a report because dependency resolution failed. A subsequent installed-client attempt for ATXN2 established separate provider authentication/DNS failures in this environment; no provider report was fabricated for AUH. This review uses the primary reading described here. Focused schema, reference and best-practice validation and HTML rendering are recorded after their actual results below.

Focused `just validate human AUH` passed on 2026-09-30 UTC with one advisory: the unresolved beta-oxidation IBA lacks a structured propagation review. The supporting IBD rows were inspected, but a full tree/MSA audit was not performed, so a specific evolutionary failure mode is not invented. Reference and best-practice checks passed. No repository-wide validation success is claimed.


## Prospective response to the first AUH review (2026-09-30)

The exact-head feedback was checked against the existing normal caches and selected original passages. All 23 source assertions and both recorded products are preserved. Summaries now state the biological conclusion and evidence route. Ten selected annotation anchors cover the principal biochemical and localization facts; the quote allowance is shared with core and reference excerpts, rather than repeating each fact on every inference.

The only proposed action change retains broad RNA binding (GO:0003723) as ACCEPT. The structural evidence establishes RNA binding but does not delimit all physiological substrates to transcript 3′-UTRs. The mitochondrial copurification experiments in PMID:24598254 demonstrate association, not purified binary binding to each mitochondrial RNA. The separate, directly established 3′-UTR-binding core remains, with its physiological compartment explicitly unresolved. No cytosolic or matrix location is invented for that specific activity.

The AUH-specific supplementary entry in PMID:34800366 was not read. Its reference assessment is therefore UNVERIFIED for target-specific support, while the curated mitochondrial annotation remains supported independently by PMID:24598254. The latter excerpt is identified as independent corroboration, not a replacement for the HTP study's data. The PAINT beta-oxidation assignment remains UNDECIDED; distinct node placement is recorded without using donor count or target self-inclusion as a verdict.

Read scope: complete normal abstracts for PMID:7892223,16640564,11738050,12655555,34800366; selected normal original Methods/Results/Discussion for PMID:24598254 and12434311; the AUH attribution passage in PMID:29056341; both complete fetched Reactome summaries. Existing root full-text reading claims are preserved as their historical scope, not expanded into a new independent whole-paper reading. Reactome source wording/coordinates are not silently corrected.

Official term checks: [RNA binding](https://amigo.geneontology.org/amigo/term/GO:0003723), [mRNA 3′-UTR binding](https://amigo.geneontology.org/amigo/term/GO:0003730), and [mRNA 3′-UTR AU-rich region binding](https://amigo.geneontology.org/amigo/term/GO:0035925). The last is an available specific term, but is not introduced here. The [official PMID:24598254 record](https://pubmed.ncbi.nlm.nih.gov/24598254/) was checked for its abstract and displayed figure captions, without claiming inspection of figure pixels or every supplementary result.

The review's suggestion that refining an annotation to a term already represented is inherently invalid is not adopted: source-specific evidence routes can support the same term. The prospective RNA decision instead rests on substrate-scope uncertainty. The original focused validation's recorded advisory count is not rewritten based on a reviewer's prediction. Focused validation, rendering and history must follow any root-approved canonical application.
