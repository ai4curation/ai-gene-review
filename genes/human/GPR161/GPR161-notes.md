# GPR161 (human, Q8N6U8) — curation notes

Working journal for the GO annotation review. All assertions carry provenance.
PMIDs marked `[not cached]` are not present in this repository's
`publications/` cache; for those I record only what a machine-readable source
(UniProt entry, QuickGO annotation row, PANTHER PAINT slice) states, and I do
not quote them.

## 1. What the protein is

GPR161 is a 529-residue class A (rhodopsin-like) G protein-coupled receptor,
UniProt Q8N6U8, HGNC:23694, chromosome 1. PANTHER places it in family
PTHR22752 ("G-protein coupled receptor 1"), subfamily PTHR22752:SF10
"G-PROTEIN COUPLED RECEPTOR 161"
(`interpro/panther/PTHR22752/PTHR22752-entries.csv`). Its closest relatives in
that family are the other orphan receptors GPR101, GPR176, GPR135, GPR61 and
GPR62; the family also contains the adrenergic receptors, which is why the
generic InterPro signature IPR000276 (G protein-coupled receptor, rhodopsin-like)
drives several of the IEA rows in the GOA file.

It is an **orphan** receptor in the strict sense: no activating ligand.
[PMID:38326651 "The orphan GPCR GPR161 has been characterized as a unique
example of a constitutively active receptor that is located within the primary
cilium of cells"]. UniProt states the same:
[file:human/GPR161/GPR161-uniprot.txt "it is not activated by a ligand and it
either acts"].

Six isoforms are annotated (Q8N6U8-1 … Q8N6U8-6); none of the GOA rows is
isoform-specific, so no `isoform` field is set on any annotation.

## 2. How it is activated — the 2024 cryo-EM structure

PMID:38326651 (Hoppe, Harrison, Hwang et al., Nat Struct Mol Biol 2024; cached,
full text available) is the single most informative primary reference for the
human protein and is the anchor for every IDA row in the GOA file.

- **Structure of the active, Gs-coupled state.** 2.7 Å cryo-EM reconstruction of
  a GPR161–miniGs fusion complexed with Gβ1γ2 and Nb35. [PMID:38326651 "We
  conclude that our structure of GPR161-miniGs captures the Gs coupled, active
  conformation of the receptor."] This is direct structural demonstration of
  the receptor–G protein interaction that GO:0004930 describes.
- **Self-activation by ECL2.** [PMID:38326651 "the ECL2 of GPR161 forms a beta
  hairpin that folds over the extracellular face of the receptor to completely
  occlude the canonical orthosteric ligand binding pocket"]. Mutating the
  hydrophobic ECL2 residues (M177, V179, W182) abolishes cAMP production, but
  those mutants also fail to reach the cilium, so ECL2 mutants are uninformative
  about ciliary function.
- **A sterol site potentiates Gs coupling.** A cholesterol-like density sits at
  an extrahelical site between TM6 and TM7; photoaffinity labelling with two
  diazirine cholesterol analogues labels K267(6.32) and C319(7.48), and cold
  cholesterol competes the labelling away. [PMID:38326651 "Our combined
  biochemical, simulation, and signaling studies show that cholesterol, and
  potentially other sterols, can bind GPR161 to support interactions with Gs,
  thereby promoting cAMP production."]
- **Constitutive activity confirmed in two orthogonal assays** (GloSensor cAMP,
  miniGs NanoBiT). [PMID:38326651 "The results from these two orthogonal assays
  demonstrate that GPR161 is constitutively active"].

## 3. Two separable activities: Gs coupling and PKA anchoring

This is the key mechanistic result for curation, because it is the reason the
GOA record carries **two** molecular functions for GPR161.

- GPR161 is the only GPCR known to carry an A-kinase anchoring domain.
  [PMID:38326651 "GPR161 is unique among many GPCRs in that it contains a
  PKA-binding AKAP domain."] The AKAP element is an amphipathic helix in the
  C-terminal tail. [PMID:38326651 "Previous studies have identified an
  amphipathic helix in the C-terminus of GPR161 that directly binds PKA
  regulatory subunits type I (RI)"].
- The L465P C-terminal mutant breaks that helix. It still couples to Gs and
  still makes cAMP, but recruits less PKA-RI. [PMID:38326651 "Consistent with
  previous reports, GPR161-L465PC-term recruited less PKA-RI than wild-type
  GPR161"].
- The two functions dissociate cleanly in a `Gpr161`-null NIH 3T3 rescue assay
  scoring GLI2 accumulation at the ciliary tip:
  - the sterol-site triple mutant (AAA 7.52/7.56/8.51), which makes no cAMP,
    **still** represses ciliary GLI2;
  - the L465P AKAP mutant, which makes cAMP normally, **fails** to repress it.
  [PMID:38326651 "was unable to repress GLI2 localization to the ciliary tip in
  the basal condition, indicating that PKA anchoring by GPR161 is critical for
  ciliary Hedgehog pathway control"], and the paper's conclusion:
  [PMID:38326651 "We conclude that GPR161 binding to PKA-RI is essential for
  Hedgehog repression in the primary cilia, while GPR161-induced Gs signaling is
  dispensable."]
- The resting-state model: [PMID:38326651 "In the absence of Hedgehog, GPR161
  bound to PKA is localized to primary cilia. PKA within the cilia
  phosphorylates GLI resulting in processing into its repressor form."] and on
  pathway activation [PMID:38326651 "In the presence of Hedgehog, GPR161 traffics
  out of the cilia, removing PKA-RI with it"].

**Curation consequence.** GOA carries GO:0004930 (G protein-coupled receptor
activity) *and* GO:0035591 (signaling adaptor activity), both IDA on
PMID:38326651. Both are supported, and they are not redundant: they are the two
experimentally separable arms of the same protein. GO:0035591's definition
("A signaling adaptor can bring together both protein and non-protein molecules
within a signaling pathway... tethering signaling components, localizing these
components to specific areas of the cell", OLS) is an exact description of
tethering the PKA type I holoenzyme to the ciliary membrane. The curated GO-CAMs
model it the same way: `gocams/index.tsv` gives GPR161 two activity nodes in
each of models 693b3c0900000157, 693b3c0900000331 and 693b3c0900000434 —
GO:0004930 (part_of GO:0007189, occurs_in GO:0098804) and GO:0035591 (part_of
GO:0045879). Seven further models (693b3c0900000051, 693b3c0900001389,
693b3c0900001501, 693b3c0900001575, 696022cd00001523, 696022cd00001645) carry
only the GO:0004930 node.

A directly-evidenced molecular function that GOA does **not** have is
**GO:0034237 protein kinase A regulatory subunit binding** ("Binding to one or
both of the regulatory subunits of protein kinase A", OLS). PMID:38326651 Fig. 5e
is a PKA-RI recruitment assay on human GPR161 in human cells, and the AKAP
region is the binding element. I propose this as the one `NEW` row; it is the
informative molecular-function term that the five uninformative GO:0005515 rows
fail to provide, and it is neither an ancestor nor a descendant of GO:0035591
(GO:0035591 sits under GO:0060090 molecular adaptor activity; GO:0034237 under
GO:0005515).

## 4. Where it acts

- **Non-motile (primary) cilium membrane, GO:0098804** — the core location.
  [PMID:38326651 "GPR161 localizes to primary cilia in Hedgehog pathway
  responsive NIH 3T3 cells in the basal condition"]. The GOA IDA row for
  GO:0098804 is anchored on PMID:40384633, whose abstract states
  [PMID:40384633 "Specific G-protein-coupled receptors (GPCRs) exist on the
  ciliary membrane."]. That paper is abstract-only in our cache
  (`full_text_available: false`), but UniProt cites it for
  `Cell projection, cilium membrane` with ECO:0000269, i.e. the curator read the
  full text.
- **Ciliary entry requires TULP3/IFT-A.** [PMID:20889716 "TULP3 and IFT-A, in
  turn, promote" / "trafficking of a subset of G protein-coupled receptors
  (GPCRs), but not"] Smoothened, to cilia; Reactome states the GPR161-specific
  case explicitly [Reactome:R-HSA-5610725 "TULP3 and the retrograde complex
  IFT-A are required to recruit GPR161 to the cilium in the absence of Hh
  ligand"].
- **Ciliary exit on pathway activation** is GRK2-phosphorylation →
  β-arrestin → BBSome → IFT-B dependent. [PMID:40384633 "and ARRB2
  double-knockout impairs GPR161 export."] and [PMID:40384633 "demonstrated that
  GRK2 plays a crucial role in GPR161 export."] Note the division of labour
  here: in GO-CAM 693b3c0900000716 the activity-bearers for
  `intraciliary retrograde transport` are GRK2, ARRB1, the BBSome and IFT-B —
  GPR161 is the **cargo**, not an activity node (`gocams/index.tsv`). So no
  transport process term belongs on GPR161; it fails the participation test.
- **Recycling endosome, GO:0055037, `is_active_in`.** GPR161 internalises after
  ciliary exit [PMID:38326651 "Upon Hedgehog pathway activation, GPR161 exits
  cilia by internalizing to the recycling endocytic compartment"] and — the part
  that justifies `is_active_in` rather than merely `located_in` —
  [PMID:38326651 "Both ciliary and extraciliary pools of GPR161 contribute to
  GLI-R formation and regulate tissue-specific repression of Hedgehog pathway in
  mice"], with the mechanism proposed as sterol-supported cAMP production away
  from the cilium: [PMID:38326651 "Sterols are also enriched in the endocytic
  recycling compartment"] and [PMID:38326651 "Therefore, both the plasma membrane
  and periciliary endosomal pools could support cAMP production by GPR161."]
  That last sentence is also the functional justification for keeping
  GO:0005886 plasma membrane.
- **Endocytic vesicle membrane, GO:0030666** (Reactome TAS) is the transit
  compartment of the internalisation step [Reactome:R-HSA-5635102 "Hh signaling
  promotes the removal of the orphan G protein coupled receptor GPR161 from the
  cilium"] — real, but no activity of GPR161 has been demonstrated there, so it
  is kept as non-core.

## 5. Phylogenetic propagation (IBA) — reading the nodes, not the donor counts

The local PAINT slice `interpro/panther/PTHR22752/PTHR22752-paint.tsv` resolves
both IBA rows to real IBD node assertions:

| node | term | taxon scope | IBD seeds |
|---|---|---|---|
| PTN002733799 | GO:0004930 | (unrestricted) | MGI:2685054 (mouse Gpr161), MGI:2685858 (mouse Gpr101), UniProtKB:Q8N6U8 (human GPR161) |
| PTN004562730 | GO:0007189 | taxon:7711 Chordata | MGI:2685054, UniProtKB:Q8N6U8, ZFIN:ZDB-GENE-120215-39 (zebrafish gpr161) |
| PTN004562730 | GO:0055037 | taxon:7711 Chordata | MGI:2685054 |

Two points that are easy to get backwards and that I have deliberately *not*
treated as defects:

1. **Human GPR161 appears in its own WITH/FROM for GO:0004930 and GO:0007189.**
   That is expected: the human IDA rows (PMID:38326651) are among the descendant
   evidences the PAINT curator used to place the IBD. It marks
   experimental grounding on the target itself and is not circular.
2. **GO:0055037 at PTN004562730 is seeded by a single donor (mouse Gpr161).**
   A one-donor node is not weak support — the claim is about where in the tree
   the function arose, and the curator had the whole alignment in view. The
   Chordata taxon restriction is exactly right for a GPR161-clade-specific
   trafficking behaviour.

PTN004562730 is the GPR161-specific (Chordata-restricted) node; PTN002733799 is
the deeper GPR161/GPR101 node, appropriate for the generic receptor activity.
Both placements are consistent with the biology and with the mouse
experimental record.

## 6. ISS propagation from mouse Gpr161 (B2RPY5 / MGI:2685054)

Eleven of the 36 GOA rows are ISS from mouse. I traced every one of them to a
mouse *experimental* annotation via QuickGO (`geneProductId=UniProtKB:B2RPY5`),
so none is a propagation from another inference:

| human ISS term | mouse evidence | mouse reference |
|---|---|---|
| GO:0004930 | IDA (ECO:0000314) | PMID:23332756 `[not cached]` |
| GO:0007189 | IDA | PMID:23332756 `[not cached]` |
| GO:0035591 | IDA | PMID:27357676 `[not cached]` |
| GO:0045879 | IDA | PMID:27357676 `[not cached]`, PMID:38326651 |
| GO:0055037 | IDA | PMID:23332756 `[not cached]` |
| GO:1901621 | IMP (ECO:0000315) | PMID:23332756 `[not cached]` |
| GO:0001501 | IMP | PMID:29222391 `[not cached]` |
| GO:0060173 | IMP | PMID:29222391 `[not cached]` |
| GO:0021549 | IMP | PMID:29386106 `[not cached]` |
| GO:0030900 | IMP | PMID:30914320 `[not cached]` |
| GO:2001222 | IDA | PMID:40737401 `[not cached]` |

Mouse UniProt B2RPY5 records the matching phenotypes: embryonic lethality by
10.5 dpc with increased Shh signalling and neural-tube ventralisation and
defective Gli3 processing (PubMed:23332756); conditional limb deletion →
polysyndactyly (PubMed:29222391); conditional deletion in neural stem cells or
cerebellar granule-cell progenitors → cerebellar tumorigenesis (PubMed:29386106);
conditional deletion in neuroepithelium/radial glia → derepressed Smoothened
signalling throughout forebrain with hydrocephalus, periventricular heterotopia
and polymicrogyria (PubMed:30914320); saltatory neuronal migration driven by
GPR161 acting as a mechanosensor of fluid shear stress (PubMed:40737401). The
human structure paper states the lethality independently:
[PMID:38326651 "Knockout of Gpr161 in mice is embryonically lethal, and the
embryos display severe limb, facial, and early nervous system defects indicative
of hyperactive Hedgehog signaling"].

Human GPR161 is the direct ortholog (same PANTHER subfamily SF10), and the human
and mouse mechanisms agree at the level of both activities, so every one of these
transfers is sound. What differs between them is **coreness**, not correctness:

- GO:0004930, GO:0007189, GO:0035591, GO:0045879, GO:0055037 and GO:1901621 name
  what GPR161 itself does — receptor activity, cAMP-raising signalling, PKA
  anchoring, and the negative regulation of Smoothened signalling (including its
  neural-tube-patterning instance). These are core.
- GO:0001501 skeletal system development, GO:0060173 limb development,
  GO:0021549 cerebellum development, GO:0030900 forebrain development and
  GO:2001222 regulation of neuron migration are whole developmental programmes,
  or the behaviour of other cells, in which GPR161 does not itself perform a
  step. They are correct, well-evidenced (mouse conditional knockouts) tissue
  outcomes of one molecular brake being released, and belong as non-core.

The boundary I drew between GO:1901621 and the tissue terms: GO:1901621 is a
descendant of GO:0045879 and names the *regulatory act itself* in the tissue
where it matters most; "limb development" names a programme that GPR161
modulates but does not execute.

## 7. The five GO:0005515 rows

All five IPI rows come from a single reference, PMID:32296183 (HuRI, the human
binary interactome reference map), with partners UPK1B (O75841), COMT (P21964),
EFNA5 (P52803), CLDN19 (Q8N6F1-2) and SLC30A2 (Q9BRI3). These are systematic
yeast two-hybrid screen hits [PMID:32296183 "We screened this search space a
total of nine times with a panel of three Y2H assay versions"], and the authors
are explicit that function does not follow from detection
[PMID:32296183 "the cellular function of most individual PPIs remains to be
elucidated"].

None of the five partners is a component of any GPR161 mechanism in the
literature — not PRKAR1A/PRKAR1B, not GNAS, not ARRB1/ARRB2, not TULP3, not SMO
— so there is no more informative molecular function to MODIFY these rows to,
and `GO:0005515` on its own carries no functional information. Per the repo
policy the five rows are removed; that is a statement about the annotation's
informativeness, not a claim that the reported interactions are false.

## 8. Module and pathway consistency

`modules/hedgehog_signaling.yaml` models GPR161 as annoton `gpr161_camp_brake`
of the `vertebrate_ciliary_variant`, with function GO:0004930, processes
GO:0007189 and GO:0045879, and location GO:0098804. My review reaches exactly
that set as core and adds GO:0035591 (which the module's own
`gocam_associations` point at, via model 693b3c0900000157 activity
693b3c0900000212, and which `gocams/index.tsv` shows as a second GPR161 node in
the same models). Nothing in this review contradicts the module or the completed
reviews of SMO, SHH, PTCH1, SUFU, GLI2 or GLI3.

## 9. Disease

Germline GPR161 variants predispose to pediatric medulloblastoma
(MIM:155255, UniProt DISEASE block, PubMed:31609649 `[not cached]`), and the
structure paper lists the human allelic spectrum
[PMID:38326651 "GPR161 mutations in humans lead to developmental defects such as
spina bifida"] — also pituitary stalk interruption syndrome (Orphanet:95496) and
medulloblastoma. Disease terms are not GO annotations and no action follows for
this review.

## 10. Open questions carried into the review

- Which pool of GPR161 — ciliary, periciliary-endosomal or plasma-membrane —
  supplies the cAMP that matters in vivo, given that the ciliary Gs arm is
  dispensable for GLI2 repression in NIH 3T3 cells but AKAP function is
  dispensable in zebrafish?
- Is the extrahelical sterol the physiological stimulus, or is mechanical force
  (the mechanosensitive model invoked for neuronal migration) the operative one?
- Whether `GO:0034237 protein kinase A regulatory subunit binding` should be
  added to GOA, and whether the PKA holoenzyme–GPR161 assembly warrants a
  complex term.
