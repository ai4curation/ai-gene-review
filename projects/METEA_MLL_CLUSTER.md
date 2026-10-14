---
title: "Methylorubrum extorquens MLL Cluster Curation Project"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [METEA]
genes: [mllA, mllBC, mllDE, mllF, mllG, mllH, mllJ, mluA, mluI, mluR]
last_reviewed: "2026-10-04"
sidecars:
  slide_assets:
    - METEA_MLL_CLUSTER/slides/lanthanophore-system.svg
    - METEA_MLL_CLUSTER/slides/mluA-review-table.jpg
manifest:
  slides:
    - href: METEA_MLL_CLUSTER/slides/METEA_MLL_CLUSTER-slides.html
      description: AI generated
---

# Methylorubrum extorquens MLL Cluster Curation Project

**Bottom line:** the *Methylorubrum extorquens* AM1 *mll* locus produces
methylolanthanin, a secreted small-molecule lanthanide chelator
(lanthanophore) that helps methylotrophs acquire rare-earth cofactors for
XoxF-type methanol dehydrogenases. The core biosynthetic genes are homologous
to NRPS-independent iron-siderophore enzymes, and automated GO pipelines
therefore mixed a real enzyme-family analogy with incorrect Fe(III)-siderophore
transport terms. The ten current reviews separate those two facts: retain
conservative ligase, carrier, acetyltransferase, TonB-receptor and sigma-factor
functions where they are supported, remove or generalize iron-specific
annotations, and avoid asserting a precise molecular function for uncharacterized
accessory proteins such as mllG and mllJ.

As of 2026-10-04, every gene in the local *mll*/*mlu* set has a review file and
deep research. The reviews contain 31 annotation rows: 8 `ACCEPT`, 7
`KEEP_AS_NON_CORE`, 4 `REMOVE`, 3 `MODIFY`, 1 `MARK_AS_OVER_ANNOTATED`, and 8
reviewer-added `NEW` rows. This project is still in progress: only mllDE is
`COMPLETE`, seven reviews are `DRAFT`, and mllF and mllJ remain `INITIALIZED`;
the finishing pass and GO-term requests are tracked in
[#4126](https://github.com/ai4curation/ai-gene-review/issues/4126).

**Organism:** *Methylorubrum extorquens* AM1 (METEA)

**Focus:** methylolanthanin biosynthesis plus the adjacent candidate uptake and
cell-surface signaling module.

## Current review set

### Methylolanthanin biosynthesis and accessory proteins

| Gene | UniProt | Review status | Rows | Current core claim |
|---|---|---:|---:|---|
| mllA | C5B1I4 | `DRAFT` | 2 | IucA/IucC-family acid-amino acid ligase; exact substrate still inferred |
| mllBC | C5B1I5 | `DRAFT` | 4 | NIS-synthetase-like acid-amino acid ligase fusion; removes a wrong o-succinylbenzoate-CoA ligase EC |
| mllDE | C5B1I6 | `COMPLETE` | 3 | ACP-like phosphopantetheine-binding carrier component |
| mllF | C5B1I7 | `INITIALIZED` | 2 | Divergent AsbF-like TIM-barrel enzyme; specific reaction unresolved |
| mllG | C5B1I8 | `DRAFT` | 0 | DUF2218 protein with no supported molecular-function term yet |
| mllH | C5B1I9 | `DRAFT` | 2 | Predicted GNAT N-acetyltransferase acting on a polyamine linker |
| mllJ | C5B1J0 | `INITIALIZED` | 2 | TAT-exported DUF4142/ferritin-like periplasmic accessory protein; precise activity unknown |

### Candidate uptake and regulation system

| Gene | UniProt | Review status | Rows | Current core claim |
|---|---|---:|---:|---|
| mluA | C5B1I1 | `DRAFT` | 8 | TonB-dependent outer-membrane transporter; iron-siderophore rows removed or generalized |
| mluR | C5B1I2 | `DRAFT` | 2 | FecR-family inner-membrane sigma-factor antagonist |
| mluI | C5B1I3 | `DRAFT` | 6 | ECF sigma factor that directs RNA polymerase to cognate promoters |

## Biology

### Lanthanophore production

Methylolanthanin is a lanthanide-binding metallophore built around a citrate
core linked to 4-hydroxybenzoate and acetylated homospermidine moieties. The
META1p4129-META1p4138 region was identified because it is strongly induced
during growth with poorly soluble Nd2O3, and deletion/overexpression of the
locus changes methylolanthanin production and lanthanide bioaccumulation.

The strongest GO calls in the biosynthetic half of the cluster are deliberately
family-level:

| Evidence-backed role | Genes | GO representation |
|---|---|---|
| NRPS-independent-siderophore-like ATP-dependent amide-bond formation | mllA, mllBC | `GO:0016881` acid-amino acid ligase activity |
| Carrier-domain tethering of pathway intermediates | mllDE | `GO:0031177` phosphopantetheine binding |
| Predicted N-acetylation of a methylolanthanin polyamine linker | mllH | `GO:0008080` N-acetyltransferase activity |

Several adjacent proteins are intentionally broader:

| Gene | Current interpretation |
|---|---|
| mllF | Catalytic TIM-barrel enzyme, likely metal-dependent and AsbF-like, but the review avoids an isomerase or 3-dehydroshikimate-dehydratase annotation until the direct reaction is measured. |
| mllG | DUF2218 accessory protein. The UniProt aldolase label is machine-generated and not supported by the methylolanthanin literature, so the current review asserts no molecular function. |
| mllJ | Periplasmic TAT-exported DUF4142/ferritin-like protein associated with the cluster; no metal-binding, ferritin-like storage, or biosynthetic reaction has been demonstrated for the single protein. |

### Uptake and regulation

Methylolanthanin is modeled as part of a TonB-dependent metal-acquisition
system, but the adjacent uptake/signaling module still needs a careful
finishing pass:

| Gene | Supported part | Caveat |
|---|---|---|
| mluA | Outer-membrane TonB-dependent receptor architecture; `GO:0009279` cell outer membrane is accepted. | The exact lanthanide-metallophore ligand assignment remains inferential for UniProt C5B1I1. |
| mluR | FecR-family membrane anti-sigma/pro-sigma transducer architecture. | A cognate lanthanide-responsive MluI partner is inferred, not experimentally mapped for C5B1I2. |
| mluI | ECF sigma-factor domains and sigma-factor activity. | The regulated promoter set and one-to-one assignment to the mluARI model remain inferential for C5B1I3. |

## Annotation actions

### Current action counts

| Action | Count | Main source |
|---|---:|---|
| `ACCEPT` | 8 | acid-amino acid ligase rows on mllA/mllBC, MluA outer membrane, MluI sigma-factor rows, MluR sigma-factor-antagonist activity |
| `KEEP_AS_NON_CORE` | 7 | siderophore-biosynthesis analogy on mllA/mllBC, broad ligase/localization rows, and derivative sigma-factor regulation rows |
| `REMOVE` | 4 | MluA iron/siderophore process rows plus the mllBC o-succinylbenzoate-CoA ligase EC |
| `MODIFY` | 3 | MluA iron-siderophore transporter activities generalized to transmembrane transporter activity; mllH acyltransferase specialized to N-acetyltransferase |
| `MARK_AS_OVER_ANNOTATED` | 1 | MluI generic DNA-binding transcription factor activity |
| `NEW` | 8 | de novo terms for mllDE, mllF, mllH and mllJ |

### What changed

**Iron specificity was the main correction.** Methylolanthanin is a
lanthanide chelator, not an Fe(III)-siderophore. The MluA review therefore
removes `iron ion transport`, `siderophore transport` and
`siderophore-iron import into cell`, and modifies two iron-siderophore
transporter activities to the existing parent `GO:0022857` transmembrane
transporter activity.

**NIS chemistry was kept, but not over-specified.** mllA and mllBC keep
`GO:0016881` acid-amino acid ligase activity because IucA/IucC/NIS synthetase
chemistry is the strongest molecular-function inference, but both reviews note
that the exact single-enzyme substrate sequence has not been reconstituted.

**Machine or family names were not treated as direct biochemistry.** mllF is not
curated as a xylose isomerase; mllG is not curated as the ProtNLM-predicted
aldolase; and mllJ keeps a root `molecular_function` placeholder plus
periplasmic localization because the DUF4142 protein has no demonstrated
single-protein activity.

## GO term gaps

GO has no specific biological-process term for lanthanophore biosynthesis.
Three current reviews propose the same `lanthanophore biosynthetic process`
term, with the existing `GO:0044550` secondary metabolite biosynthetic process
used as the closest available parent for several de novo rows.

The transport side may also need a term below TonB-dependent transmembrane
transporter activity for lanthanide-metallophore import. That request is
blocked on finishing the MluA review in
[#790](https://github.com/ai4curation/ai-gene-review/issues/790), because the
current exact-ligand claim is still inferential.

## Open follow-up

The remaining work is tracked in
[#4126](https://github.com/ai4curation/ai-gene-review/issues/4126):

| Scope | Issue |
|---|---|
| Re-review mllA acid-amino-acid-ligase specificity and siderophore-process handling | [#787](https://github.com/ai4curation/ai-gene-review/issues/787) |
| Re-review mllBC NIS-fusion specificity | [#788](https://github.com/ai4curation/ai-gene-review/issues/788) |
| Re-review mllH acetyltransferase specificity | [#789](https://github.com/ai4curation/ai-gene-review/issues/789) |
| Re-review MluA receptor/transport substrate strength | [#790](https://github.com/ai4curation/ai-gene-review/issues/790) |
| Re-review MluI sigma-factor versus generic transcription-factor terms | [#791](https://github.com/ai4curation/ai-gene-review/issues/791) |
| Re-review MluR anti-sigma model and missing cytoplasmic-membrane location | [#792](https://github.com/ai4curation/ai-gene-review/issues/792) |
| Finish mllF, mllG and mllJ, consolidate the lanthanophore BP NTR, and decide whether MluA supports a lanthanide-metallophore transport term | [#4126](https://github.com/ai4curation/ai-gene-review/issues/4126) |

## Related systems

The [REE](REE.md) project uses this cluster as the native lanthanophore module
in a larger rare-earth-element acquisition design. XoxF/Mxa methanol
dehydrogenase genes, PQQ biosynthesis genes and C1-metabolism genes sit
downstream of lanthanide acquisition; those are curated outside this focused
*mll*/*mlu* page.
