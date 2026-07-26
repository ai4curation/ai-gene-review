# ABR (human, Q12979) — review notes

PAINT + affinage campaign. 32 GOA rows reviewed.

## What the protein is

859 aa, brain-enriched, chromosome 17p. Domain string (UniProt FT): DH 91-284,
PH 301-459, C2 484-613, Rho-GAP 647-845, with the catalytic arginine finger at R683
[file:human/ABR/ABR-uniprot.txt "Arginine finger"]. So one polypeptide carries a
GEF module and a GAP module that act on the same GTPase family in opposite directions
[file:human/ABR/ABR-uniprot.txt "regulatory activities toward small GTP-binding proteins."].

ABR is the paralog of BCR. It lacks BCR's N-terminal oligomerisation/serine-threonine
kinase region — the 1995 biochemistry paper puts it plainly: "The Abr protein is very
similar to Bcr but lacks a structural domain which may influence its biological regulatory
capabilities" [PMID:7479768]. That missing region is the reason a naive paralog transfer
from BCR is hazardous for ABR: BCR's kinase and BCR-ABL-related annotations must not move
across. (In practice GOA does not currently carry any such transfer — see below.)

## The defining biochemistry (PMID:7479768, Chuang et al. 1995)

Recombinant domains, purified separately:

- **DH/GEF domain**: stimulates GTP binding to CDC42Hs, RhoA, Rac1, Rac2
  (rank order CDC42Hs > RhoA > Rac1 = Rac2); inactive toward Rap1A and Ha-Ras.
- **GAP domain**: acts on Rac1, Rac2, CDC42Hs; **inactive toward RhoA**, Rap1A, Ha-Ras.
- Each domain binds substrate non-competitively.

[PMID:7479768 "The Dbl-homology domains of Bcr and Abr were active in stimulating GTP binding to CDC42Hs, RhoA, Rac1, and Rac2 (rank order, CDC42Hs > RhoA > Rac1 = Rac2) but were inactive toward Rap1A and Ha-Ras. Both Bcr and Abr acted as GAPs for Rac1, Rac2, and CDC42Hs but were inactive toward RhoA, Rap1A, and Ha-Ras."]

The earlier 1993 papers had already shown Rac-directed GAP activity for the isolated
domain [PMID:8349582] and identified the brain transcript with both homologies
[PMID:8262969].

**The consequence for curation is the central finding of this review:** none of this
substrate detail is expressible in GO any more. `GO:0030675 Rac GTPase activator activity`,
`GO:0005100 Rho GTPase activator activity` and `GO:0005099 Ras GTPase activator activity`
are all now **secondary ids of `GO:0005096 GTPase activator activity`**; `GO:0005089 Rho
guanyl-nucleotide exchange factor activity` and `GO:0030676 Rac guanyl-nucleotide exchange
factor activity` are secondary ids of `GO:0005085`; and `GO:0017048 Rho GTPase binding` /
`GO:0048365 Rac GTPase binding` are secondary ids of `GO:0031267 small GTPase binding`
(checked against QuickGO `/ontology/go/terms/<id>/complete`, which reports the merges in
`secondaryIds`). ABR is therefore annotated identically to a GAP that is Rho-specific and
Rac-inert — the exact opposite specificity. The information now has to live in `has_input`
extensions / GO-CAM, and GOA carries none for ABR.

## In vivo: predominantly a *negative* regulator of Rac

Every loss-of-function system points the same way.

- Glia: `Abr;Bcr` double null mice have granule cell ectopia and cerebellar foliation
  defects with abnormal Bergmann glia; double-null astroglia show constitutively raised
  p38 MAPK phosphorylation (a Rac-regulated pathway) [PMID:11684658 "the simultaneous disruption of two negative regulators of Rac, Abr and Bcr, in mice leads to specific abnormalities in postnatal cerebellar development"].
- Macrophages: `Abr;Bcr` nulls are elongated, over-motile toward CSF-1, and over-phagocytic,
  with sustained Rac activation; on CSF-1 stimulation Abr and Bcr transiently translocate to
  the plasma membrane, and GAP-dead mutants ring the phagosome
  [PMID:17116687 "in response to CSF-1 stimulation, Abr and Bcr transiently translocated to the plasma membrane"].
  Same paper: "These results identify Abr and Bcr as the only GAPs to date that specifically
  negatively regulate Rac function in vivo in primary macrophages."
- Innate immunity: `abr/bcr` nulls over-produce MPO, elastase, ROS and MMP9 in endotoxemia
  [PMID:19703997 "These data show that Abr and Bcr normally curb very specific functions of mature tissue innate immune cells"].
- T cells: **single** `abr-/-` mice get fatal cockroach-allergen asthma; `abr-/-` CD4+ T cells
  carry elevated GTP-bound Rac and migrate better toward CCL21
  [PMID:24058174 "CD4(+) T cells from CRA-immunized and challenged abr(-/-) mice contained elevated levels of activated GTP-bound Rac compared with wild-type controls."].
- Synapse: **single** `ABR`-null mice show enhanced basal Rac1 activity and a selective loss
  of LTP *maintenance* [PMID:20962234 "Mice deficient for BCR or ABR show enhanced basal Rac1 activity but only a small increase in spine density."].

The T-cell and synaptic data are single-knockout, so "ABR negatively regulates Rac signalling"
does not rest solely on the redundant double mutant. `GO:0035021 negative regulation of Rac
protein signal transduction` is nonetheless **entirely absent from GOA** — proposed as NEW.

## The GEF side is real but context-restricted

The one clean in-vivo GEF result is Xenopus single-cell wound repair: Abr is recruited to the
Rho activity zone by binding *active* Rho, amplifies Rho there via its DH domain, and uses its
GAP domain to exclude Cdc42 from that zone
[PMID:21295482 "Within the Rho zone, Abr promotes local Rho activation via its GEF domain and controls local crosstalk via its GAP domain, which limits Cdc42 activity within the Rho zone."].
This is the mechanistic reason ABR carries both modules: it is a zone-segregation device, not
a bidirectional switch on one GTPase. A 2024 human study reports ABR as a RhoA activator in
feto-placental endothelium under hyperglycaemia (affinage table, PMID:38776074) — consistent
direction, but not read in full here.

## PSD-95 / DLG4

`GO:0005515 protein binding` IPI cites `UniProtKB:P78352` = human DLG4 (PSD-95). This is a
real, characterised interaction, not a screen hit: the C-terminal valine is a PDZ-binding
motif, and V859A abolishes DLG4 binding
[file:human/ABR/ABR-uniprot.txt "Abolishes interaction with DLG4."] while leaving synaptic
targeting intact. `GO:0030165 PDZ domain binding` is the informative replacement.

## WITH/FROM resolution (every accession)

| Accession | Resolves to | Relation to ABR |
|---|---|---|
| `UniProtKB:Q12979` | human ABR | **self** (valid self-referential IBA) |
| `UniProtKB:P11274` | human BCR | **paralog, same species** |
| `MGI:MGI:107771` | mouse Abr | ortholog |
| `MGI:MGI:88141` | mouse Bcr | paralog |
| `RGD:1306279` | rat Abr | ortholog |
| `RGD:1307993` | rat Bcr | paralog |
| `UniProtKB:Q5SSL4` | mouse Abr | ortholog (all `GO_REF:0000024` ISS except one) |
| `UniProtKB:A0A0G2JTR4` | rat Abr | ortholog (synapse ISS) |
| `UniProtKB:P78352` | human DLG4 / PSD-95 | interaction partner |
| `CGD:CAL0000181133` | *Candida albicans* **BEM2** (Q5AGW7) | distant RhoGAP-fold homolog |
| `PANTHER:PTN002754245` | ancestral node carrying GEF/GAP + Rho-signalling | — |
| `PANTHER:PTN001142600` | ancestral node carrying the synaptic terms | — |

Resolutions done with `rest.uniprot.org/uniprotkb/<ACC>.json`, `informatics.jax.org/marker/<MGI>`,
and a UniProt `xref:cgd-…` / `xref:rgd-…` search.

**Paralog audit result.** Every ABR annotation whose WITH/FROM includes BCR also has either an
ABR ortholog donor in the same set or ABR's own direct experimental evidence — with **one
exception**: `GO:0035023 regulation of Rho protein signal transduction` (IBA) cites only
`PANTHER:PTN002754245|UniProtKB:P11274`, i.e. the human paralog BCR and nothing else. Read
mechanically that is a paralog-only transfer. It survives here only because ABR's own IDA
(PMID:7479768) independently establishes both activities. Flagged in the review rather than
removed. The genuinely BCR-specific biology — the N-terminal oligomerisation/kinase region
and everything downstream of BCR-ABL — has **not** leaked into ABR's GOA, so the paralog
hazard is present in the evidence graph but has not (yet) produced a wrong annotation.

Two distinct PANTHER nodes are in play. `PTN002754245` is the GEF/GAP/Rho-signalling node
(donors: mouse Abr, mouse Bcr, human BCR, human ABR, C. albicans BEM2). `PTN001142600` is a
synaptic node (donors: mouse Abr, mouse Bcr, rat Abr, rat Bcr — vertebrate only). Splitting
the biochemistry and the synaptic localisation across two nodes is the right call: the
C. albicans BEM2 donor supports GAP activity but obviously not the postsynaptic density.

## Reactome placements

- `R-HSA-9014296 RAC2 GEFs activate RAC2` → `GO:0005085`. Reactome credits "ABR (Chuang et al.
  1995)" = PMID:7479768. Traceable and correct (Rac2 is at the weak end of the measured rank
  order but was measured).
- `R-HSA-9013022 RHOB GAPs stimulate RHOB GTPase activity` → `GO:0005096`. Reactome lists ABR
  as a *confirmed* RHOB GAP ("Amin et al. 2016, supported by Bagci et al. 2020") while listing
  **BCR only as a candidate** ("binds to active RHOB"). Amin et al. 2016 = PMID:27481945;
  Bagci et al. 2020 = PMID:31871319 (both abstract-only in the cache, neither abstract names
  ABR, so the ABR-specific claim could not be verified here). This is in tension with
  PMID:7479768, which found the ABR GAP domain inactive toward RhoA. RhoB is not RhoA, so it
  is not a formal contradiction, but the generic GO term is doing the work: `GO:0005096` is
  true of ABR regardless, and the RHOB substrate assignment is invisible to GO. Kept, flagged,
  not removed.
- `R-HSA-205039 p75NTR indirectly activates RAC and Cdc42 via a guanyl-nucleotide exchange
  factor` → `GO:0005829`. The Reactome reaction summary is one sentence and names no GEF; ABR
  sits in an unnamed candidate-GEF set. Carries no ABR-specific information; the cytosol term
  itself is fine.
- `R-HSA-419166 GEFs activate RhoA,B,C` → `GO:0005829`. Consistent with the measured RhoA GEF
  activity.
- `R-HSA-9012999 RHO GTPase cycle` → `GO:0051056`, the redundant parent of `GO:0035023`.

## Decisions summary

- **MODIFY ×4**: `GO:0007165 signal transduction` (IEA) and both `GO:0007264 small
  GTPase-mediated signal transduction` rows (IEA + TAS) → `GO:0035023`, because ABR *regulates*
  the cascade rather than transducing it (role conflation); `GO:0005515 protein binding` (IPI,
  DLG4) → `GO:0030165 PDZ domain binding`.
- **MARK_AS_OVER_ANNOTATED ×2**: `GO:0035556 intracellular signal transduction` (uninformative
  parent) and `GO:0016020 membrane` (HDA from an NK-cell membrane-proteome sweep; ABR is a
  soluble peripheral protein and the specific `GO:0005886` is separately annotated).
- **No REMOVE.** Nothing in the set is demonstrably wrong.
- **NEW ×2**: `GO:0035021 negative regulation of Rac protein signal transduction` (the
  dominant in vivo role, missing entirely) and `GO:1900273 positive regulation of long-term
  synaptic potentiation` (ABR-null mice lose LTP maintenance).

## Not annotated, deliberately

- Phagocytosis. Mouse `Abr;Bcr` double nulls over-phagocytose [PMID:17116687]; human
  trabecular-meshwork siRNA *reduces* phagocytosis by ~40% (affinage table, PMID:31516309).
  Opposite signs, one from a redundant double mutant, one from a single siRNA experiment in
  one cell type. Left for `suggested_experiments`.
- Mitotic fidelity in hESCs (PMID:28579391), osteoclast differentiation (PMID:37507586),
  hypoxic pulmonary remodelling (PMID:23152932), GDM/hyperglycaemia (PMID:38776074) — all
  single-report, downstream of the Rac/Rho activity change, and pleiotropic. Not annotated.
- EspH (PMID:36219160) identifies ABR as the native host target of an EPEC effector that binds
  the ABR GAP domain. Real and well-controlled, but it is a pathogen-side function; the
  host-side GO content is just "ABR has a GAP domain that controls Rac1/Cdc42", already
  captured.
