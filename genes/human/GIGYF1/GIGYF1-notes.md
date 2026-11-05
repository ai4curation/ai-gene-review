# GIGYF1 (O75420) research notes

GRB10-interacting GYF protein 1 (PERQ1). Paralog of GIGYF2. Member of the GIGYF family.

## Core function
GIGYF1 is a scaffolding/adaptor protein that nucleates a translational repression and
co-translational mRNA decay module together with the non-canonical cap-binding protein
4EHP/EIF4E2, the DEAD-box helicase DDX6, and the collision sensor E3 ligase ZNF598.

- The 4EHP-GIGYF1/2 complex triggers co-translational mRNA decay on transcripts with
  ribosome pausing/stalling: [PMID:33053355 "Here, we show that 4EHP-GIGYF1/2 complexes trigger co-translational mRNA decay. Human cells lacking these proteins accumulate mRNAs with prominent ribosome pausing."] and [PMID:33053355 "4EHP-GIGYF1/2 complexes fail to reduce mRNA levels in the absence of ribosome stalling or upon disruption of their interaction with the cap structure, DDX6, and ZNF598."]
- Co-translational binding of GIGYF1/2 marks transcripts with perturbed elongation for decay:
  [PMID:33053355 "co-translational binding of GIGYF1/2 to the mRNA marks transcripts with perturbed elongation to decay."]
- GIGYF proteins have an N-terminal 4EHP-binding region and a central GYF domain that mediates
  interaction with ZNF598, TTP, or TNRC6 proteins: [PMID:31439631 "These proteins possess an N-terminal 4EHP-binding region (4EHP-BR) and a central compacted GYF domain ... that mediates the interaction with ZNF598, tristetraprolin (TTP), or the microRNA (miRNA)-induced silencing complex-associated TNRC6 proteins"]
- GIGYF contains a motif necessary and sufficient for direct interaction with Me31B/DDX6;
  4EHP-GIGYF-DDX6 assembly is required for TTP-mediated repression of an AU-rich mRNA:
  [PMID:31439631 "we report that GIGYF contains a motif necessary and sufficient for direct interaction with Me31B/DDX6" ; "4EHP-GIGYF-DDX6 complex assembly is required for tristetraprolin-mediated down-regulation of an AU-rich mRNA"]
- DDX6 interaction confirmed for GIGYF1 with mutagenesis of W294/F306/F312 abolishing it
  (UniProt, PMID:31439631).

## IGF/GRB10 signaling (legacy function)
Originally identified via GRB10 as a modulator of IGF-I receptor signaling
[PMID:12771153 "Two novel proteins that are linked to insulin-like growth factor (IGF-I) receptors by the Grb10 adapter and modulate IGF-I signaling."]. UniProt FUNCTION: "May act
cooperatively with GRB10 to regulate tyrosine kinase receptor signaling. May increase IGF1
receptor phosphorylation". This is the basis of the IBA GO:0048009 (IGF receptor signaling)
annotation. It is a real but secondary/less-characterized role relative to the translational
repression module.

## ComplexPortal
- CPX-2336: 4EHP-GIGYF1 co-translational mRNA decay complex, ZNF598 variant
- CPX-2342: 4EHP-GIGYF1 co-translational mRNA decay complex, DDX6 variant
Basis of NAS GO:1990261 (pre-mRNA catabolic process) and IDA GO:0032991 (complex).

## Annotation assessment
- GO:0045947 negative regulation of translational initiation (IBA): ACCEPT, core. 4EHP binding
  represses cap-dependent initiation.
- GO:0005829 cytosol (IBA): ACCEPT.
- GO:0048009 IGF receptor signaling pathway (IBA): KEEP_AS_NON_CORE — legacy GRB10/IGF role.
- protein binding (IPI) x many: mostly interactome screens. The functionally meaningful one is
  EIF4E2/DDX6/ZNF598. PMID:31439631 (DDX6) -> capture as eIF4E2/DDX6 binding informative MF;
  others KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED (HT screens).
- GO:1990261 pre-mRNA catabolic process (NAS, ComplexPortal): the complex mediates
  co-translational mRNA decay; MODIFY toward mRNA catabolic / translation-coupled decay would be
  more accurate but pre-mRNA catabolic is arguably wrong (it's mature mRNA). Keep as
  KEEP_AS_NON_CORE / note imprecision.
- GO:0032991 protein-containing complex (IDA): uninformative top-level term -> KEEP_AS_NON_CORE.

## Core MF/BP for review
- MF: GO:0008190 eukaryotic initiation factor 4E binding (binds 4EHP/EIF4E2) — well supported.
- BP: GO:0045947 negative regulation of translational initiation; GO:0017148 negative regulation
  of translation; co-translational mRNA decay (GO:0006515 / mRNA catabolic).


## 2026-11-05 — Translation repression and source-specific interactions

GIGYF1 participates in cytosolic translation repression and selected mRNA decay. Human GIGYF1 activity involving eIF3 complements the 4EHP/DDX6 interaction pathway (PMID:39018414; PMID:28698298; PMID:31439631; PMID:33053355). The GYF domain recognizes proline-rich protein regions, including the experimentally tested SNRPB interface (PMID:38225382).

Growth-factor signaling is retained as contextual: the original GRB10-dependent effect used a mouse GIGYF1 fragment, while human signaling-complex association is independently documented (PMID:12771153; PMID:20878056). It does not establish universal receptor stimulation by full-length human GIGYF1.

Earlier notes and the PN notes remain historical. The current synthesis preserves positive interaction records while removing generic binding labels that lack useful functional definition. It also separates the actual PAINT restriction on direct RNA-binding repression from inherited process/location assertions. Full assay and construct boundaries, including the unresolved NEK6 product crosswalk and 2020 resource-table accession, are centralized in [external evidence](GIGYF1-external-evidence.md). Current and historical source contexts are preserved in the [archive](GIGYF1-context-archive.json); no historical quote is silently discarded or reused as fresh endorsement.


## 2026-11-05 — Adaptor mechanism and historical binding terminology

The new GO:0030674 assessment and its source-specific assay limits are documented in [external evidence](GIGYF1-external-evidence.md). This specific child of GO:0060090 complements the translation-repressor assertion while retaining the existing source-specific interaction decisions.

The earlier journal statement assigning GO:0008190 to 4EHP binding is superseded by the source-specific distinction between 4EHP/EIF4E2 and EIF4E1. The current GO:0031369 refinement retains the established 4EHP interaction without conflating these factors (PMID:28698298). The historical text is preserved. Named ComplexPortal assemblies and positive ZNF598 associations remain documented; neither alone supplies a contact-specific ligase-binding mechanism or an unverified GO complex identifier.

## 2026-11-05: recruitment-assay clarification

TTP depletion reduces joint recruitment of GIGYF1 and eIF3 to target RNA. The GYF mutant instead retains eIF3 association while reducing TTP interaction and target recruitment. These complementary assay results support selective bridging (PMID:39018414). The independently mapped eIF3 and EIF4E2 contacts remain distinct; retaining the adaptor mechanism does not require a second assertion of the same general binding term.
