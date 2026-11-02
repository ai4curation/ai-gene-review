# DIABLO / SMAC manual curation notes

## 2026-09-30

- Completed a manual DIABLO/SMAC review from GOA, UniProt, cached PubMed
  records, Reactome events, the PTHR32247 PANTHER family, and annotation-reviewer
  follow-up.
- Canonical DIABLO is a mitochondrial IAP antagonist rather than a caspase or
  ubiquitin-ligase enzyme. The founding SMAC and DIABLO papers identify a
  mitochondrial protein that is released to the cytosol during apoptosis and
  promotes caspase activation by binding IAPs and removing their inhibitory
  activity [PMID:10929711, "Smac promotes caspase-9 activation by binding to
  inhibitor of apoptosis proteins"; PMID:10929712, "DIABLO may promote
  apoptosis by binding to IAPs and preventing them from inhibiting caspases"].
- The molecular surface is the processed N terminus. Structural work showed
  that the SMAC AVPI motif engages IAP BIR grooves and that SMAC dimerization is
  required for strong apoptotic activity [PMID:10972280, "the amino-terminal
  four residues of Smac/DIABLO are indispensable for its function"]. PARL
  cleavage in mitochondria generates the mature N-terminal IAP-binding motif;
  loss of PARL maturation leaves SMAC unable to bind XIAP, while cytosolic
  cleaved SMAC rescues apoptosis in PARL-deficient cells [PMID:28288130].
- GO currently lacks a narrow "IAP antagonist activity" term. Direct XIAP,
  cIAP1/BIRC2, ML-IAP/BIRC7, and BIRC6 rows were therefore narrowed from
  `GO:0005515 protein binding` to broad `GO:0140678 molecular function
  inhibitor activity`; less mechanistic survivin, ARTS-context, PRKCD, AREL1,
  and high-throughput binary interactome rows were removed as generic partner
  edges.
- BIRC6/BRUCE is both a SMAC antagonist and a SMAC substrate context. Bartke et
  al. showed that BRUCE inhibits caspase activity and apoptosis and functions
  as a chimeric E2/E3 ubiquitin ligase with SMAC as a substrate
  [PMID:15200957]. Three recent BIRC6 structures support the inverse side:
  SMAC binds BIRC6 multivalently and competitively displaces caspases or other
  clients from the BIRC6 cavity [PMID:36758104; PMID:36758105; PMID:36758106].
- Ubiquitination rows should stay on the IAP-family E3s. Livin/BIRC7 promotes
  SMAC degradation [PMID:16729033] and AREL1 ubiquitinates cytosolic IAP
  antagonists including SMAC, HtrA2, and ARTS [PMID:23479728], but in both
  settings DIABLO is the bound substrate or client, not the enzyme.
- The apoptosis rows were tightened toward `GO:0097193 intrinsic apoptotic
  signaling pathway`. Broad `GO:0006915 apoptotic process`,
  `GO:0043065 positive regulation of apoptotic process`, and
  `GO:0097190 apoptotic signaling pathway` obscure the same mitochondrial IAP
  antagonist step. The death-receptor row is retained only as a non-core
  downstream sensitization context, because cytosolic SMAC can potentiate TRAIL
  apoptosis at the effector-caspase/IAP checkpoint [PMID:10950947].
- Removed the mouse-transferred CD40 receptor complex and cytoplasmic side of
  plasma membrane rows. That association is separate from canonical
  mitochondrion-to-cytosol SMAC biology and is not supported by the local human
  DIABLO evidence.
- The SMAC3 splice variant has a potentially distinct XIAP-destabilizing
  activity: Smac3 binds XIAP BIR2/BIR3, disrupts processed caspase-9 binding,
  promotes caspase-3 activation, and accelerates XIAP autoubiquitination and
  destruction; unlike canonical SMAC, it lacks exon 4 and therefore residues
  62-105 of the full-length sequence [PMID:14523016].

## 2026-10-03

- Replaced the local `inhibitor-of-apoptosis protein antagonist activity` NTR
  with `GO:1990525 BIR domain binding` after the Drosophila overannotation
  reviews landed on the same branch and exposed the exact same BIR-surface
  antagonism already using `GO:1990525` in `hid` and `grim`.


## 2026-10-17 source-based review update

The [evidence guide](DIABLO-source-guide.md) records the original passages, public interaction and pathway identifiers, actual access limits and product scope used for this update. All 83 imported annotation dictionaries and three splice-product identities are retained. Decisions are 42 MODIFY, 30 KEEP_AS_NON_CORE and 11 ACCEPT, with no NEW annotations. The explicit [ClinGen project instructions](https://github.com/ai4curation/ai-gene-review/blob/98ae322b9bb97f58c6f12c093c97f645ca33da76/projects/CLINGEN_MENDELIAN.md#curation-instructions) govern positive generic binding and supported specificity refinements.

One IAP-antagonism core replaces the overlapping BIR-binding entries. Its active location is cytosol; intermembrane-space storage and MPP/PARL processing remain in the description and localization annotations. A processed canonical chain is not an additional splice product, and DIABLO is not assigned the proteases' processing work. The independently studied Diablo-S and SMAC3 constructs qualify any blanket claim that all alternative products lack activity.

This update supersedes the older generic-binding removals: positive pairs are retained or refined using actual partner function and assay context. Yeast two-hybrid capacity does not establish a native interaction across compartment boundaries. AP–MS is co-complex evidence, with independent domain assays supporting the IAP-specific refinements. The unresolved FADS6 source-sequence discrepancy is retained, rather than explained speculatively.

The original mouse CD40 capture experiments support contextual ISS complex/location assertions; species transfer alone is not a reason to reject them. Actual PAINT placement and donor experiments support the oxidative-stress and neuronal-apoptosis inferences as non-core. Mature-SMAC overexpression in human leukemia cells independently supports the contextual cell-cycle annotation, while the imported structural paper's particular cell-cycle linkage remains unverified.

The older assertion that all four N-terminal residues are indispensable is too absolute: PMID:10972280 Table 2 and deletion experiments retain weak binding and partial activity for del4. The first-residue replacement result and the importance of the motif remain valid. The old PMID:15200957 substrate-only excerpt does not establish antagonism by itself; the paper's abstract separately reports antagonism. These qualifications preserve the earlier notes as a historical record.

Publication cache flags remain literal. Separately recovered original papers, the genuine 2017 publisher supplement and the separately identified 2022 BIRC6 preprint are distinguished in the guide. Normal provider attempts failed through authentication/quota responses; the scientific synthesis here is manual, with no fabricated provider report.


## Follow-up: compartments and positive regulatory control

Canonical SMAC passes through an inner-membrane processing intermediate before mature SMAC occupies the IMS and is released to cytosol. The published PMID:28288130 abstract and genuine publisher S2/S3/S8 evidence support this distinction; the main full text remains unavailable. The predicted W42–A60 segment is not an independent topology measurement. The human SMAC3 original instead infers IMS localization from cytochrome-c colocalization and mitochondrial release (PMID:14523016, Figure 2 and associated Results), without establishing identical PARL processing. MitoCoP/HPA/family observations remain at their actual broader assay resolution while independent target evidence supplies the gene-level refinement.

SMAC performs positive regulation by binding IAPs and relieving their inhibition of procaspase activation and mature caspase activity (PMID:10972280, Figure 3 and the two corresponding Methods sections). The procaspase assay uses mouse XIAP 1–356, while the mature-caspase assay uses human BIR2 124–240. GO:2001244 preserves this positive regulatory role and descends from both original regulatory terms. No caspase activity is assigned to SMAC. The current survivin-complex definition and its PMID:19153467 source xref are documented in the evidence guide; the contextual peptide/domain complex is not evidence for a stable endogenous full-length BIRC5 assembly.

Product descriptions retain the observed sequence and activity facts. Canonical precursor/intermediate/mature states are processing states rather than additional splice isoforms. The human short-product assay retains partial effector-caspase relief, so it does not establish universal inactivity. Tagged SMAC3 localization and recombinant mature-construct binding do not establish identical processing or quantitative activity to the canonical product (PMID:10950947; PMID:14523016). Existing source-cache access flags and all prior notes are preserved.


## 2026-10-26 systematic mammalian apoptosis audit

Reviewed every seeded annotation from the review YAML, preserving every original machine-sourced field and adding no NEW rows. Original terms, evidence, references, relationship fields and supporting entities are unchanged. The gene-level assessment includes functions outside the apoptosis module. Existing source-specific evidence guides and prior history records remain intact.

The review and annotation-reviewer workflow was applied. Default Falcon research and normal publication caching were launched in parallel. Falcon and the perplexity-lite fallback failed for all four targets (provider access errors; command logs under `.cache/module-audit-logs/execution-deep-*`). `fetch-gene-pmids` completed successfully for each. No provider-branded research file was fabricated. This manual notebook and the normal primary publication/UniProt caches supply the research trail.

Preserved the established DIABLO evidence guide, isoform/construct cautions, positive-regulatory refinements and independently supported BIR-domain binding. Mature DIABLO antagonizes IAPs rather than cleaving caspases. PMID:10929712 is the mouse-linked discovery source in curated UniProt; PMID:10972280 contains human SMAC reconstitution with assay-specific human or mouse XIAP reagents, and is not relabeled as an all-mouse experiment. PMID:14512414 establishes cooperative BIR2/BIR3 antagonism: the isolated BIR2 fragment can remain in a ternary caspase/SMAC complex, so a simple universal competitive-blockade cartoon is inadequate.

PMID:14623868 explicitly reports that “the release of endogenous Smac was not sufficient to overcome the XIAP resistance” in sympathetic neurons. Exogenous SMAC plus cytochrome c and the motif control support conditional participation; they do not establish universally sufficient endogenous release. PMID:16085184 supports peroxide-associated mitochondrial redistribution and reciprocal expression/antisense effects in mouse C2C12 cells. PMID:20614026 identifies native SMAC in activated CD40 receptor assemblies in mouse B cells; preserve co-complex presence without claiming direct CD40 binding or a receptor-signaling core.

Mature mitochondrial IMS residence is distinct from the canonical human membrane-processing intermediate. Mouse refinement to IMS is supported by import/release and compartment-marker studies (PMID:15814844; PMID:18385140). The latter full text uses SMAC as an IMS marker while studying phosphatases; a paper foregrounding another protein is not irrelevant. Human PARL evidence (PMID:28288130) is not promoted to a directly demonstrated native mouse processing route. Mouse centriole and sperm midpiece/principal/end-piece ISO assertions list human Q9NR28, but those exact donor measurements were not recovered in the current human review; leave them UNDECIDED rather than deleting a plausible localization.

Current generic-binding policy supersedes the earlier human DIABLO task-specific/ClinGen retention decision for this audit. Bare GO:0005515 rows lacking a supported specific functional refinement are REMOVE only because uninformative. Their actual measured associations, isoforms, and experimental limitations remain in reasons and the source guide; no interaction is declared false. Supported specific refinements, including BIR-domain binding and verified partner-class interactions, are preserved. This supersession is recorded in a new append-only helper-generated history rather than rewriting historical decisions. Mouse BIR binding is independently supported in the core; no redundant annotation is created merely to silence a coverage advisory.


## PR #5558 follow-up: retain mitochondrial assertions (2026-10-26)

Restored 7 existing GO:0005739 rows to ACCEPT under the informative root-organelle exception. Each rationale now identifies the original evidence scope; separate IMS annotations are unchanged. Organelle localization is not defective because a finer compartment is also supported. No original annotation payload, processing/isoform qualifier, or source file was changed. Direct localization, comparative transfer and inventory evidence remain distinct; abstract-only sources are not represented as full-text topology assays.

- Row 52: The original human SMAC3 study localizes the tagged 195-residue splice product to mitochondria by microscopy and fractionation, with cytochrome-c colocalization and stimulus-dependent release. The authors infer IMS residence from colocalization, but these assays do not directly resolve submitochondrial topology. This directly supports the organelle claim. The canonical PARL processing route and inner-membrane intermediate are not assigned to SMAC3 from these experiments.

- Row 53: The MitoCoP workbook includes a DIABLO protein group containing canonical and SMAC3 identifiers through the literature-supported pool, with zero valid localization ratios. It therefore does not independently establish a quantitative localization profile or distinguish products. The organelle claim is nevertheless correct and independently grounded by target localization and processing evidence. Canonical processing intermediates and mature IMS protein must not be conflated, or generalized to every splice product.

- Row 54: The mitochondrial PAINT IBD at PTN001283560 on the lineage leading to human DIABLO is grounded by target and mouse experimental sources. Target self-inclusion is legitimate experimental grounding, not circularity. Mitochondrial residence is inherited and independently supported; more specific processing and mature-chain locations do not constitute a granularity defect in this informative organelle assertion.

- Row 55: The HPA ICC/IF record reports mitochondrial staining and cytosol. This directly supports the organelle-resolution claim without resolving a mitochondrial subcompartment or product-specific processing. Independent processing and mature-chain evidence supplies more specific locations separately.

- Row 56: The published abstract explicitly reports intramembrane cleavage of SMAC by the inner-membrane protease PARL. Genuine publisher supplementary experiments distinguish precursor, intermediate and mature forms in human HEK293 fractionation and HA-SMAC/MPP perturbation assays. These observations support mitochondrial residence. The mature-chain IMS Reactome entity provides separate compartment context. The predicted W42–A60 segment is not an independent topology measurement, and the published main Methods/Results remain unavailable. This neither assigns PARL protease activity to DIABLO nor transfers the processing route to alternative products.

- Row 57: The current InterPro family/fold matches and UniProt location mapping support mitochondrial residence, corroborated by independent target localization and processing evidence. They do not themselves resolve precursor processing or mature-protein topology. Their correct organelle assignment is not a propagation failure merely because finer locations are supported separately.

- Row 58: The published abstract establishes mitochondrial storage and release of SMAC into cytosol during apoptosis; the complete original was not recovered. This supports the existing organelle claim. The mature-DIABLO Reactome entity independently places the release-competent 56–239 chain in IMS, but that separate evidence does not require replacement of mitochondrion or turn the abstract into a topology assay.

This bounded follow-up reused the prior genuine research-provider attempts and cached/source-analysis evidence; provider failure logs remain in `.cache/module-audit-logs/execution-deep-human-DIABLO.log`. Independent annotation-reviewer consultation agreed with retaining root-organelle claims and their separate finer localization evidence.
