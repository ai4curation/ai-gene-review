# Rhp (Q9XYY9): evidence and ProtNLM claim review

Rhophilin is a multidomain Rho-effector-family protein containing HR1 Rho-binding, BRO1, and PDZ domains. This architecture supports a signaling scaffold associated with cytoskeletal regulation, while its exact partners and the conservation of stress-fiber regulation in Drosophila remain incompletely resolved.

Exact input: [Q9XYY9](https://www.uniprot.org/uniprotkb/Q9XYY9/entry), 718 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [Rhp-predictions-source.json](Rhp-predictions-source.json). Source features: [Rhp-uniprot.txt](Rhp-uniprot.txt), with an exact extraction in [Rhp-sequence-evidence.json](Rhp-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR004328; BRO1_dom.
DR   InterPro; IPR038499; BRO1_sf.
DR   InterPro; IPR011072; HR1_rho-bd.
DR   InterPro; IPR036274; HR1_rpt_sf.
DR   InterPro; IPR001478; PDZ.
DR   InterPro; IPR036034; PDZ_sf.
DR   InterPro; IPR047138; RHPN1_2.
FT   DOMAIN          36..110
FT                   /note="REM-1"
FT                   /evidence="ECO:0000259|PROSITE:PS51860"
FT   DOMAIN          121..520
FT                   /note="BRO1"
FT                   /evidence="ECO:0000259|PROSITE:PS51180"
FT   DOMAIN          567..645
FT                   /note="PDZ"
FT                   /evidence="ECO:0000259|PROSITE:PS50106"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Rhophilin-2 | UNC | IPR047138 supports the RHPN1/2 family and the source identifies fly Rhophilin. The vertebrate paralog-specific label Rhophilin-2 is more precise than this evidence establishes; an orthology analysis is needed to distinguish it from a family-level name. |
| Location | Cytoskeleton (SL-0090) | UNC | The Rho-effector architecture and existing stress-fiber-related IBA support cytoskeletal biology but do not establish structural residence at the cytoskeleton. Localization and participation in cytoskeletal regulation are distinct claims. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0007165 signal transduction (IEA): **ACCEPT**. HR1 Rho-binding plus BRO1 and PDZ domains support a scaffold role in signal transduction; this is not an intrinsic Rho GTPase activity.
- GO:0051497 negative regulation of stress fiber assembly (IBA): **UNDECIDED**. The existing IBA is a phylogenetic assertion and is not discounted by donor count. HR1/BRO1/PDZ architecture supports Rho-effector biology but does not by itself establish negative regulation of stress-fiber assembly in the exact fly protein; target-specific functional evidence or the ancestral assertion needs resolution.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `Rhp-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined both GOA rows, description and core functions without using any ProtNLM output.

### Identity
- Q9XYY9 (718 aa, unreviewed TrEMBL) is the only UniProt entry cross-referenced to FlyBase FBgn0026374 (Rhp/CG8497); Q9VXP2 is a merged secondary accession. Both RefSeq products (NP_511168.3, NP_996447.1) map to this entry. It is the canonical full-length product, not a fragment or alternative model: it carries the full HR1/REM-1 (36-110), BRO1 (121-520) and PDZ (567-645) architecture of the rhophilin family.

### Evolutionary placement
- PANTHER places Rhp in PTHR23031:SF15 (LD12055P), distinct from RHPN1 (SF6) and RHPN2 (SF5). The family review `interpro/panther/PTHR23031/PTHR23031-review.yaml` agrees (Rhp is the SF15 representative); no placement disagreement.
- PAINT node PTN001126281 propagates GO:0051497 to fly Rhp, to vertebrate RHPN1 and RHPN2 orthologs, and to other metazoans (QuickGO withFrom query, 2026-10-21). Donors are mouse Rhpn1 (MGI:1098783 = Q61085) and human RHPN2 (Q8IUC4), both IDA from PMID:25071083. The node therefore sits above the vertebrate RHPN1/RHPN2 duplication.
- Pairwise global identity (Rhp-bioinformatics/compare_rhophilins_rereview.py, RESULTS-rereview.md): Rhp is ~34-36% identical to each of human/mouse RHPN1 and RHPN2, which are 41% identical to each other, consistent with Rhp being a pre-duplication co-ortholog of both.

### Literature
- [PMID:12221077 "Rhophilin-1 and Rhophilin-2 interacted with both GDP- and GTP-bound RhoA in vitro"; "Rhophilin-2-expressing HeLa cells showed a loss of actin stress fibers"; "the Bro1 and PDZ domains of Rhophilin-2 were required for disassembly"].
- [PMID:25071083 "Taken together, these results indicate that Rhophilin-1 is an inhibitor of Rho-dependent stress fiber formation in vitro"] — podocyte knockout and overexpression; the IDA source for the PAINT donors.
- [PMID:12975351] S2-cell RNAi screen lists rhophilin under "No effect on lamellae" (depletion not confirmed by immunoblot). Lamella formation is a Rac/SCAR/Arp2/3 readout, not a stress-fibre assay, so this does not contradict GO:0051497.
- [PMID:31792377 "active RhoA binds and dissociates rhophilin and NF2/Kibra from STRIPAK"] — mammalian only; kept as a suggested question, not used for annotation.
- The deep-research report repeats a secondary statement (Peck 2002 full text) that the single fly rhophilin knockout is embryonic lethal; the primary fly data are unpublished (GenBank submission "Mutations in the Drosophila Rhophilin gene at 13E"), so this is not used as evidence.
- Note: PMID:14504265 was fetched into publications/ by mistake (a guessed id; it is an unrelated lamin B1 paper) and is not cited.

### Decisions
- GO:0007165 signal transduction (IEA, InterPro HR1): ACCEPT (unchanged action). As precise as fly evidence allows; no fly Rho1 binding shown, so Rho protein signal transduction would overreach.
- GO:0051497 negative regulation of stress fiber assembly (IBA): changed UNDECIDED -> ACCEPT. Both vertebrate paralogs carry experimental support, so ancestral-node placement is sound; Rhp descends from that node with all required domains intact; no fly evidence of divergence.
- No NEW terms. Rho GTPase binding MF is not proposed: no fly binding data, and PAINT has no MF node for this family to inherit.
- Status set to COMPLETE; description rewritten as a project-independent summary; core_functions added.

### Relative for next review
- Human RHPN2 (Q8IUC4), a PAINT donor for the node Rhp inherits from and a co-ortholog; no review exists in the repo (no genes/*/RHPN* or Rhpn* folders). Mouse Rhpn1 (Q61085) is the alternative co-ortholog donor with in vivo knockout data.
- Modules: no module under modules/ mentions rhophilin; no GO-CAM index entry for Rhp, RHPN1 or RHPN2.
