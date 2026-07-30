# ACAP3 (Q96P50) — curation notes

Human ACAP3 / centaurin-beta-5 / CENTB5 / KIAA1716. HGNC:16754, chromosome 1p36.33,
834 aa (isoform 1, Q96P50-3, MANE-Select NM_030649.3).

## 1. What the record itself says

UniProt is almost silent on function. The only FUNCTION line is a curator inference
(`ECO:0000305`, i.e. no experimental evidence attached):

- `file:human/ACAP3/ACAP3-uniprot.txt` — "GTPase-activating protein for the ADP ribosylation factor"

There is **no** SUBCELLULAR LOCATION block, no CATALYTIC ACTIVITY block, and no
SIMILARITY block. The UniProt reference list (`RN [1]`–`[6]`) contains only sequencing
and large-scale proteomics papers — no functional study is cited. But the entry is
`PE 1: Evidence at protein level`, so the protein is detected (mass spectrometry from
cervix carcinoma, PMID:16964243); what is missing is *functional/biochemical* data in
the UniProt record, not evidence of existence. HPA records the gene as brain-enhanced:

- `file:human/ACAP3/ACAP3-uniprot.txt` — "DR   HPA; ENSG00000131584; Tissue enhanced (brain)."

The single curated interaction is with its own paralog:

- `file:human/ACAP3/ACAP3-uniprot.txt` — "Q96P50; Q15057: ACAP2; NbExp=4"

Domain architecture (FT table): PH 268–363, Arf-GAP 403–525, C4-type zinc finger
418–441 inside the GAP domain, ANK repeats 702–731 / 735–764 / 768–797, plus an
N-terminal BAR domain recognised at the profile level:

- `file:human/ACAP3/ACAP3-uniprot.txt` — "DR   InterPro; IPR042695; ACAP3_BAR."
- `file:human/ACAP3/ACAP3-uniprot.txt` — "DR   CDD; cd07637; BAR_ACAP3; 1."

So ACAP3 is a full-architecture ACAP: BAR–PH–ArfGAP(Zn)–ANK, exactly like ACAP1 and
ACAP2. The old family name "coiled-coil" for the N-terminal region is the pre-BAR
nomenclature.

## 2. The functional literature (all of it)

There are only four functional papers on ACAP3, two on mouse and two on human tumour
cells. None of them is cited by UniProt, and none of them has been curated into GOA.

**Mouse, molecular function and neurite outgrowth** — Miura et al. 2016:

- [PMID:27330119 "Ectopically expressed ACAP3 in HEK (human embryonic kidney)-293T cells showed the GAP activity specific to Arf6."]
- [PMID:27330119 "In primary cultured mouse hippocampal neurons, knockdown of ACAP3 abrogated neurite outgrowth, which was rescued by ectopically expressed wild-type ACAP3, but not by its GAP activity-deficient mutant."]
- [PMID:27330119 "the level of GTP-bound Arf6 was significantly increased by knockdown of ACAP3 in hippocampal neurons"]
- [PMID:27330119 "These results demonstrate that ACAP3 positively regulates neurite outgrowth through its GAP activity specific to Arf6."]
- [PMID:27330119 "Thus cycling between active and inactive forms of Arf6, which is precisely regulated by ACAP3 in concert with a guanine-nucleotide-exchange factor(s), seems to be required for neurite outgrowth of hippocampal neurons."]

The last point matters for interpretation: the requirement is for Arf6 *cycling*, not for
Arf6 being kept off. A GTP-locked and a GDP-locked Arf6 both failed to rescue; only a
fast-cycling mutant did. ACAP3 is therefore a component of a cycle, and "negative
regulator of Arf6" would be a misreading.

**Mouse, in vivo requirement** — Miura & Kanaho 2017:

- [PMID:28919417 "Knockdown of ACAP3 in the developing cortical neurons of mice in utero significantly abrogated neuronal migration in the cortical layer, which was restored by ectopic expression of wild type of ACAP3, but not by its GAP-inactive mutant."]
- [PMID:28919417 "Furthermore, morphological changes of neurons during migration in the cortical layer were impeded in ACAP3-knocked-down cortical neurons."]
- [PMID:28919417 "These results provide evidence that ACAP3 plays a crucial role in migration of cortical neurons by regulating their morphological change during development of cerebral cortex."]

Both mouse studies are knockdown + rescue with a GAP-dead mutant, i.e. the phenotype is
attributed to the catalytic activity, not to scaffolding.

**Human, receptor trafficking and tumour suppression** — lung adenocarcinoma, 2026:

- [PMID:41520057 "Mechanically, ACAP3 inhibits epidermal growth factor receptor (EGFR) signalling via impairing EGFR recycling and accelerating lysosome-mediated EGFR degradation in a GTPase-activating protein (GAP) activity-dependent manner."]
- [PMID:41520057 "ACAP3 significantly suppresses the proliferation of LUAD cells in vitro and in vivo."]

This is the only mechanistic result obtained on the human protein, and it is again
GAP-activity-dependent. It puts ACAP3 on the endosomal receptor-sorting side of Arf6
biology, which is where its paralogs ACAP1/ACAP2 act.

**Human, papillary thyroid carcinoma** — 2024:

- [PMID:39098591 "ACAP3 level was downregulated in PTC tissues and cells."]
- [PMID:39098591 "ACAP3 overexpression (oe-ACAP3) suppressed viability, proliferation, migration and invasion of PTC cells, facilitated apoptosis"]

This one is overexpression/knockdown in cell lines with downstream Western-blot readouts
(p-AKT, p-p53, Bcl-2/Bax, E-/N-cadherin). It supports a growth-suppressive phenotype but
does not identify a molecular mechanism, and the AKT/p53 read-outs are too far downstream
to annotate.

## 3. Family context (ACAP1/ACAP2), used only as context

ACAP3's paralogs were characterised by the Randazzo lab. This is *family* context, not
ACAP3 data, and is kept out of ACAP3's core functions:

- [PMID:11062263 "In vitro, ACAP1 and ACAP2 preferred Arf6 as a substrate, rather than Arf1 and Arf5, more so than did ASAP1."]
- [PMID:11062263 "All contain phosphoinositide-dependent GAP activity."]
- [PMID:11062263 "ACAP1 and ACAP2 were recruited to peripheral, tubular membranes, where activation of Arf6 occurs to allow membrane recycling back to the plasma membrane."]
- [PMID:11062263 "The GTP-binding protein ADP-ribosylation factor 6 (Arf6) regulates endosomal membrane trafficking and the actin cytoskeleton in the cell periphery."]

The ACAP BAR–PH module has been worked out structurally on ACAP1: it is a dimeric,
membrane-deforming unit that assembles into a lattice on tubulated membrane.

- [PMID:25284369 "The BAR (Bin-Amphiphysin-Rvs) domain undergoes dimerization to produce a curved protein structure, which superimposes onto membrane through electrostatic interactions to sense and impart membrane curvature."]
- [PMID:31291238 "Simulation studies then revealed how ACAP1, which dimerizes into a symmetrical structure in solution, is recruited asymmetrically to the membrane through dynamic behavior."]

That dimeric BAR–PH module is the natural structural explanation for the one curated
ACAP3 interaction being ACAP2 (see §5).

## 4. WITH/FROM resolution — every accession

All ten GOA rows were checked; six are IBA (GO_REF:0000033), two IEA (GO_REF:0000002),
two IPI. Every WITH/FROM identifier was resolved.

| WITH/FROM | resolves to | relationship to ACAP3 |
|---|---|---|
| MGI:MGI:2153589 | mouse **Acap3** | **1:1 orthologue** ("Orthologous to human ACAP3", Alliance) |
| UniProtKB:Q15057 | human **ACAP2** | **paralogue** |
| RGD:1562939 | rat **Acap2** | **paralogue** (orthologue of ACAP2) |
| WB:WBGene00000565 | *C. elegans* **cnt-1** | invertebrate centaurin-beta (single-copy) |
| PomBase:SPBC17G9.08c | *S. pombe* **cnt5** | fungal centaurin/ArfGAP |
| dictyBase:DDB_G0279649 | *D. discoideum* Q54WI0 | amoebal ACAP-architecture ArfGAP |
| dictyBase:DDB_G0276395 | *D. discoideum* Q551Q8 | amoebal ACAP-architecture ArfGAP |
| SGD:S000002932 | *S. cerevisiae* **AGE1** | ArfGAP, but ASAP-type (Alliance: orthologous to ASAP1/ASAP2), not an ACAP |
| AGI_LocusCode:AT5G13300 | *A. thaliana* **AGD3** (Q5W7F2) | plant ArfGAP |
| AGI_LocusCode:AT5G61980 | *A. thaliana* **AGD1** (Q9FIT8) | plant ArfGAP |
| FB:FBgn0004133 | *D. melanogaster* **blow** (blown fuse) | **PH-domain-only protein; not an ArfGAP** |
| PANTHER:PTN001142372 | superfamily node | the deep centaurin/ArfGAP node |
| PANTHER:PTN002754173 | ACAP3 subfamily node | only ever carries MGI:2153589 |
| InterPro:IPR001164 | ArfGAP domain | matches FT DOMAIN 403..525 |
| InterPro:IPR045258 | ACAP1/2/3-like | subfamily signature, correct |
| InterPro:IPR004148 | BAR domain | correct feature, but mapped to `cytoplasm` |

### 4a. Two PANTHER nodes, two grades of evidence

The six IBAs split cleanly by node, and this is the most useful structural fact in the
GOA record:

- **PTN002754173** (ACAP3 subfamily) → `neuron migration`, `regulation of neuron
  projection development`. WITH/FROM is `MGI:2153589` only, i.e. the true 1:1 mouse
  orthologue, and the mouse annotations trace to PMID:28919417 and PMID:27330119. These
  are the best-supported annotations on the gene.
- **PTN001142372** (deep superfamily) → `GTPase activator activity`, `plasma membrane`,
  `endosome membrane`, `actin cytoskeleton organization`. These are superfamily-level
  statements spanning plants, fungi, amoebae and animals.

Mouse Acap3 is *absent* from the WITH/FROM of `endosome membrane`, even though it is
present for the neuronal terms — so PAINT itself did not have orthologue evidence for
the endosomal compartment. The mammalian experimental donor there is rat **Acap2**
(GO:0010008 IDA, PMID:23572513), a paralogue, alongside worm cnt-1 (GO:0031901 early
endosome membrane IDA, PMID:22869721). Interestingly the mouse orthologue's own recorded
location is the **growth cone** (Alliance automated description: "Located in growth
cone."), not the endosome.

### 4b. A PANTHER mis-clustering: *Drosophila* `blow`

`blow` (FBgn0004133) is the WITH/FROM donor for `GO:0030036 actin cytoskeleton
organization`. Its InterPro content is **IPR011993 + IPR001849 only** — a PH domain and
nothing else. It has no ACAP1/2/3-like signature, no ArfGAP domain, no BAR domain and no
ankyrin repeats, so it cannot be an Arf GAP. All four TrEMBL isoform entries (A1Z714,
P91678, E1JGZ4, Q8MSU1; 532–644 aa) give the same two signatures, so this is not an
artefact of picking one entry. FlyBase describes it as a cytoplasmic
myoblast-fusion protein acting through WASp–Vrp1 complex stability, and its actin
annotation is an IMP from that myoblast-fusion work. PTHR23180 (CENTAURIN/ARF) has
clustered it in on the PH domain alone.

The reciprocal damage is visible on `blow` itself, which now carries `GO:0005096 GTPase
activator activity` by IBA (GO_REF:0000033) despite having no GAP domain. That is the
clearer of the two errors and is worth reporting upstream.

The ACAP3 actin annotation nevertheless survives, because the other two donors —
*Dictyostelium* Q54WI0 and Q551Q8 — are full-architecture ACAPs with genuine experimental
actin annotations (Q54WI0: GO:0030036 IMP PMID:23264736 and IGI PMID:20062541, plus
GO:0031941 filamentous actin IDA, GO:0051489 regulation of filopodium assembly IMP).

Full audit, reproducible: `ACAP3-bioinformatics/RESULTS.md` and
`check_iba_source_architecture.py`.

## 5. The two `protein binding` rows

Both `GO:0005515` IPI rows name the same partner, `UniProtKB:Q15057` = **ACAP2**, from two
independent proteome-scale datasets — BioPlex 3.0 AP-MS (PMID:33961781) and OpenCell
endogenous split-tag IP-MS (PMID:35271311). The pair is reciprocal (it appears in ACAP2's
GOA record from the same two papers) and UniProt curates it with `NbExp=4`. Neither
cached full text names ACAP3 in its body; the pair is in the supplementary interactomes,
so the claim is anchored on the UniProt INTERACTION line and the GOA/IntAct records
rather than on a quotable sentence.

This is not a lone screen artefact, and there is a structural reason to expect a real
association: the ACAP BAR–PH module is a dimerisation module (§3), and ACAP2 and ACAP3
both carry it.

`GO:0046982 protein heterodimerization activity` was the obvious upgrade, was taken, and was
then withdrawn during review. Its definition is "Binding to a nonidentical protein to form a
heterodimer", and neither AP-MS nor split-tag IP-MS measures stoichiometry — both are equally
consistent with a direct dimer, with co-residence in a larger assembly, and with two BAR
proteins sharing a membrane surface. The structural precedent is weaker than it first appears
too: what has actually been solved is ACAP1 dimerising with **itself**, a homotypic
interaction, and co-purification of BAR-domain paralogues is a known route to exactly this
signal without a direct dimer. So both rows stay at `GO:0005515`, as `KEEP_AS_NON_CORE`.

The loss from staying at `GO:0005515` is smaller than it looks, because the partner identity
travels in the WITH/FROM field: the annotation is not "binds something" but "binds
UniProtKB:Q15057". What is genuinely missing is a GO term for "physically associates with a
named paralogue" that does not also assert a stoichiometry — recorded as a knowledge gap. The
heterodimer hypothesis lives in `suggested_experiments`, with SEC-MALS and mass photometry as
the discriminating measurement, and `GO:0032403 protein-containing complex binding` named as
the term to use if the answer turns out to be a larger assembly rather than a dimer.

## 6. Ontology finding: Arf specificity can no longer be expressed as an MF

The single most important fact about ACAP3's molecular function — that its GAP activity is
**specific to Arf6** — cannot currently be recorded as a GO molecular function.
`GO:0008060 ARF GTPase activator activity` has been **merged** into
`GO:0005096 GTPase activator activity`; QuickGO
(`/ontology/go/terms/GO:0005096/complete`) lists it among the `secondaryIds`, together
with every other substrate-specific GAP term (GO:0005097 Rab, GO:0005098 Ras, GO:0005100
Rho, GO:0005099, GO:0005101, GO:0017123, GO:0030675, GO:0046582). OLS reports GO:0008060
as obsolete with no label, which alone would not distinguish a merge from a plain
obsoletion — the `secondaryIds` list is what identifies it as a merge.

So `GO:0005096` is now the terminal GAP term and ACAP3's Arf6 specificity has to live in
an annotation extension (`has_input` ARF6, UniProtKB:P62330) or be lost. This is recorded
as an ONTOLOGY knowledge gap.

## 7. Annotations absent from GOA that should exist

- `GO:0008270 zinc ion binding`. ACAP3 has a C4-type zinc finger (FT ZN_FING 418..441)
  inside its ArfGAP domain, and the UniProt entry still carries
  "DR   GO; GO:0008270; F:zinc ion binding; IEA:UniProtKB-KW." but GOA does not: the
  keyword-derived annotations (GO_REF:0000043) were withdrawn for cellular organisms, and
  InterPro2GO did not fill the gap (IPR001164 maps only to `GO:0005096`). Now proposed as a
  `NEW` ISM row — the only proposal here that rests on ACAP3's own sequence rather than on
  orthology. Coded ISM rather than an experimental code because the basis is the PROSITE
  ARFGAP profile call (PS50115 / ProRule PRU00288), not a metal-binding measurement on ACAP3;
  the family-level mutational evidence that the motif is functionally required is
  [PMID:8533093 "The GAP function required an intact zinc finger and additional
  amino-terminal residues."]. Deliberately left out of `core_functions`: zinc coordination
  here is a structural requirement of the ArfGAP fold, not a distinct activity of ACAP3.
- `GO:0030426 growth cone`. On the UniProt entry as
  "DR   GO; GO:0030426; C:growth cone; IEA:Ensembl." and on mouse Acap3 at MGI, but absent
  from human GOA.
- No lipid- or phosphoinositide-binding annotation at all, despite a PH domain and a BAR
  domain, and despite the family's GAP activity being phosphoinositide-dependent
  (PMID:11062263). No direct lipid-binding assay has been done on ACAP3 itself, so this
  is left as a suggested experiment rather than asserted.
- Related, and larger than ACAP3: `GO:0180020 membrane bending activity` is a current MF
  term defined as "The activity of bending or deforming a membrane", and it has **four**
  human annotations in total (CHMP2A, CHMP3, OPA1 — QuickGO, checked 2026-07-25). Not one
  BAR-domain protein carries it, although BAR domains are the canonical membrane-bending
  module and ACAP1's BAR-PH tandem has been shown directly to tubulate liposomes
  (PMID:25284369). ACAP3 has no such assay so it cannot be annotated here, but the gap is
  worth flagging: the term exists and the family that most obviously needs it is absent.
- Nothing from the four functional papers (§2): no `GTPase activator activity` from
  PMID:27330119, no experimental neuronal-migration annotation from PMID:28919417, no
  receptor-recycling annotation from PMID:41520057. Every annotation ACAP3 has is
  inferred.

## 8. What goes in the review's `references` list

Every PMID appearing anywhere in `ACAP3-ai-review.yaml` — including inside `review.summary`
prose and `propagation_review.comment` strings — is present in the top-level `references`
list, checked by script rather than by eye. Three classes:

1. **Evidence about ACAP3**: PMID:27330119, PMID:28919417, PMID:41520057, PMID:39098591.
   `relevance: HIGH` (the thyroid paper LOW, since it identifies no mechanism).
2. **Family / structural context**: PMID:11062263, PMID:25284369, PMID:31291238,
   PMID:8533093, plus the two interactome papers. Each `review_notes` states explicitly that
   the paper is about ACAP1/ACAP2 or about the family, and not about ACAP3.
3. **WITH/FROM donor provenance**: PMID:23572513, PMID:22869721, PMID:19076239,
   PMID:30905672, PMID:23264736, PMID:20062541, PMID:25383666, PMID:15743878, PMID:21118984,
   PMID:28646092. `relevance: LOW`, each naming which donor annotation it supplies and
   stating that it is not evidence about ACAP3. These are what make the propagation-quality
   argument in §4 checkable rather than merely asserted.

`source_entities` in each `propagation_review` covers **every** entry of that row's GOA
WITH/FROM field, verified by a script that diffs the two sets. This matters: the
hand-maintained version of that list had silently drifted on three of the six IBA rows before
the check was run — `GO:0005886` documented 4 of 7 donors, `GO:0005096` 3 of 6, and
`GO:0010008` was missing the PANTHER node. Do not maintain this list by hand.

## 9. Affinage record

`ACAP3-deep-research-affinage.md` has `self_evaluation_pairwise: win` and clear trust gates,
five numeric PMIDs, no
bioRxiv-DOI-in-a-PMID-field entries. Its narrative is accurate on the four functional
papers and was useful for finding PMID:41520057 and PMID:39098591, which the UniProt
reference list does not contain. Its own GO grounding is coarse (`GO:0098772 molecular
function regulator activity`, no localisation) and was not used. Its fifth finding
(PMID:21105360, the UPS29 minisatellite enhancer assay in rat astrocytes) is about an
intron of the gene, not the protein, and has no annotation consequence. No affinage
sentence is quoted as `supporting_text` anywhere in the review.
