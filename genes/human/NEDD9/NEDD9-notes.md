# NEDD9 (HEF1 / CAS-L, Q14511) - curation notes

## Deep research status

- Falcon deep research first launched with `--fallback perplexity-lite` (600 s timeout; fallback unavailable),
  then relaunched with `--timeout 2400`. See "Deep research outcome" at the end of this file.
- Review written from cached publications, UniProt Q14511, and two papers added to the cache during this review
  (PMID:16184168 HEF1 activates Aurora A; PMID:17174122 Chat-H/CasL in T-cell trafficking).

## Summary of function

- Cas-family docking protein: SH3 domain binds FAK
  [PMID:8668148 "an interaction of the SH3 domain of HEF1 with two discrete proline-rich regions of focal adhesion kinase"].
- Family: [PMID:9584194 "HEF1, p130(Cas), and Efs/Sin constitute a family of multidomain docking proteins that have been implicated in coordinating the regulation of cell adhesion"].
- Integrin-induced tyrosine phosphorylation by FAK then Src-family kinases
  [PMID:9360983 "We show here that p130(Cas) and Cas-L are FAK substrates"; "the phosphorylated YDYVHL sequence is a binding site for Src family protein-tyrosine kinases"].
- Localization: [PMID:9584194 "While p105(HEF1) and p115(HEF1) are predominantly cytoplasmic and localize to focal adhesions, p55(HEF1) unexpectedly is shown to associate with the mitotic spindle"].
- Migration: [PMID:24574519 "knockdown of NEDD9 in highly metastatic tumor cells drastically reduces their migratory capacity due to disruption of actin dynamics at the leading edge"];
  NEDD9 scaffolds a NEDD9-AURKA-CTTN complex [PMID:24574519 "NEDD9 binds to and regulates acetylation of CTTN in an Aurora A kinase (AURKA)/HDAC6-dependent manner"].
- Lymphocytes: Abl-dependent HEF1 phosphorylation for chemokine-induced migration and Rap1 activation [PMID:22810897].
- Mitosis: relocalizes to spindle, regulates RhoA via ECT2 [PMID:16394104 "HEF1 associates with the RhoA-GTP exchange factor ECT2"].
- Aurora A activation: [PMID:16184168 "We show that HEF1 associates with and controls activation of AurA"];
  in vitro: [PMID:16184168 "we titrated the GST-HEF1 1-363 minimal AurA-interacting domain versus GST into an in vitro kinase reaction containing recombinant AurA purified from bacteria"];
  [PMID:16184168 "In cells depleted for HEF1, AurA does not become activated, suggesting the association with HEF1 is functionally important"].

## Cilium disassembly (non-dominant function)

- [PMID:17604723 "interactions between the prometastatic scaffolding protein HEF1/Cas-L/NEDD9 and the oncogenic Aurora A (AurA) kinase at the basal body of cilia causes phosphorylation and activation of HDAC6, a tubulin deacetylase, promoting ciliary disassembly"].
- NEDD9's contribution is the activator step (kinase activator activity toward AURKA), which I proposed as a NEW
  MF annotation (GO:0043539 protein serine/threonine kinase activator activity, IDA PMID:16184168). No NEW process
  terms were proposed.

## Key curation decisions

- `protein binding` IPIs: REMOVE for most (incl. high-throughput Y2H/AP-MS, SMAD3/ITCH, ECT2, BCAR3, MICAL1,
  PLK1 docking). MODIFY where the paper supports something more specific: FYN and ABL1 -> protein tyrosine kinase
  binding (GO:1990782); PTPN11/SHP-2 -> protein phosphatase binding (GO:0019903); NEDD9-AURKA-CTTN scaffold ->
  protein-macromolecule adaptor activity (GO:0030674).
- `negative regulation of cell migration` ISS: UNDECIDED (conflicts with strong positive evidence; source not inspected).
- `actin filament bundle assembly` NAS [PMID:11827972]: MARK_AS_OVER_ANNOTATED (paper links CasL to vimentin
  intermediate filaments via MICAL, not to actin bundling).
- Mouse-derived ISS process terms (learning/memory, dendritic spine maintenance, osteoclast differentiation,
  lymphocyte homing/chemotaxis, immunological synapse): KEEP_AS_NON_CORE.
- Nuclear, Golgi, spindle, spindle pole: KEEP_AS_NON_CORE. Focal adhesion, cytoplasm, ciliary basal body: ACCEPT.

## HPA cilium atlas vs module role

- HPA v25 (member_evidence.md): no cilium, basal-body or centrosome call; main locations Cytosol; Nucleoplasm.
  The GOA GO_REF:0000052 rows (cytosol, nucleoplasm) were accepted / kept as non-core.
- PMID:41005307 (Hansen et al. 2025, HPA cilium atlas) does not mention NEDD9/HEF1 in its cached text.
- Module (stage 7): NEDD9 as an Aurora A activator at the basal body (with CIMAP3), function "kinase activator".
- Comparison: the HPA atlas does not detect NEDD9 at the basal body; the basal-body localization rests on
  PMID:17604723 (IDA) and on cell-type/stimulus-dependent recruitment (serum-induced resorption). The absence of an
  HPA basal-body call is not a contradiction (NEDD9's basal-body pool is likely transient and small relative to its
  focal-adhesion/cytosolic pool), but it means the module role is supported by a single lab's work rather than by
  independent localization data.
- Module caution: NEDD9 is primarily a focal-adhesion Cas scaffold; its ciliary role is real but non-dominant. The
  module's "kinase activator" function maps to GO:0043539 (proposed here as NEW).
