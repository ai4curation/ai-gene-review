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
