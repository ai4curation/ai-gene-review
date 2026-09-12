# APOO / MIC26 (Q9BUR5) — review notes

Human APOO, HGNC:28727, X-linked (Xp22.11), UniProt **Q9BUR5 = MIC26_HUMAN**, 198 aa,
PANTHER **PTHR14564** ("MICOS COMPLEX SUBUNIT MIC26 / MIC27 FAMILY MEMBER"), Pfam PF09769
(ApoO), InterPro IPR019166 / IPR033182. Accession verified: the fetched record's ID line is
`ID   MIC26_HUMAN             Reviewed;         198 AA.` — the expected protein, not a merged
accession pointing elsewhere.

Two names, one protein, two incompatible identities in the literature: the plasma
apolipoprotein "ApoO" of 2006, and the MICOS subunit MIC26 of 2013 onwards. Almost every
curation question on this gene turns on which of the two the annotation rests on.

---

## 1. The two identities, and how the field resolved them

### 1.1 The apolipoprotein identity (2006)

APOO was named from a dog obesity cardiac-transcriptome screen and characterised as a secreted
chondroitin-sulfate proteoglycan found in lipoprotein fractions
[PMID:16956892 "We detected this new protein in the following lipoproteins: high density lipoprotein, low density lipoprotein, and very low density lipoprotein."],
glycosylated
[PMID:16956892 "Chondroitinase ABC deglycosylation analysis or cell incubation with p-nitrophenyl-beta-d-xyloside indicated that apolipoprotein O belongs to the proteoglycan family."],
and functional in cholesterol handling
[PMID:16956892 "Apolipoprotein O promoted cholesterol efflux from macrophage cells."].
Everything in that paper about secretion, glycosylation and lipoprotein association was read
off a **55 kDa immunoreactive band**, against a recombinant protein of 22 kDa.

### 1.2 The MICOS identity (2013-2015)

Complexome profiling of mammalian mitochondria placed APOO and APOOL in the Mitofilin/MINOS
(now MICOS) complex [PMID:23704930], and three 2015 papers established MIC26 as a bona fide
subunit:

- Koob et al. [PMID:25764979 "The latter isoform spans the mitochondrial inner membrane and physically interacts with several MICOS complex subunits such as MIC60, MIC27, and MIC10."],
  with the functional consequence
  [PMID:25764979 "MIC26 depletion led to alterations in mitochondrial ultrastructure and caused a significant reduction in the number of crista junctions."].
- Ott et al., who renamed it Mic23 and showed import into the >1 MDa MIB complex
  [PMID:25781180 "We provide additional proof that ApoO indeed is a subunit of the MICOS and MIB complexes and propose the name Mic23 for this protein."].
- Guarani et al., in whose MICOS proteomics MIC26 is degraded when the complex falls apart
  [PMID:25997101 "loss of QIL1 resulted in MICOS disassembly with the accumulation of a MIC60-MIC19-MIC25 sub-complex and degradation of MIC10, MIC26, and MIC27"].

Koob et al. tried to reconcile the two identities by proposing three coexisting forms
[PMID:25764979 "We demonstrate that human MIC26 exists in three distinct forms: (1) a glycosylated and secreted 55kDa protein, (2) an ER/Golgi-resident form thereof, and (3) a non-glycosylated 22kDa mitochondrial protein."].
That three-form model is the direct source of the `Secreted`, `Golgi apparatus membrane` and
`Endoplasmic reticulum membrane` lines still in the UniProt record, and of six GOA rows.

### 1.3 The three-form model was retracted in substance in 2023

Lubeck et al. — **from the same laboratory**, with Anand and Reichert co-authors on both the
2015 and the 2023 paper — went back with the controls the earlier work lacked:

> [PMID:37279200 "In these KOs, we used four anti-MIC26 antibodies and consistently detected the loss of mitochondrial MIC26 (22 kDa) and MIC27 (30 kDa) but not the loss of intracellular or secreted 55 kDa protein. Thus, the protein assigned earlier as 55 kDa MIC26 is nonspecific."]

The 55 kDa band survives knockdown with three siRNAs, survives CRISPR knockout in four human
cell lines (HEK293, HepG2, HeLa, HAP1), is not produced by GFP- or myc-tagged MIC26, is
unaffected by mutating the predicted glycosylation sites
[PMID:37279200 "Mutagenesis of predicted glycosylation sites in MIC26 also did not affect the detection of the 55 kDa protein band."],
and contains no MIC26 peptides
[PMID:37279200 "we did not find MIC26-specific peptides in the MS analysis in any of the three samples analysed which included WT, MIC26 and MIC27 KOs"].
Their conclusion:

> [PMID:37279200 "we conclude that both MIC26 and MIC27 are exclusively localized in mitochondria and that the observed phenotypes reported previously are exclusively due to their mitochondrial function"]

They also note the negative external check that had been available all along
[PMID:37279200 "MIC26 was not found to be a part of high-density lipoprotein (HDL)-associated proteins in a proteomic study where other major apolipoproteins could be detected"].

The tell was already visible in the 2015 companion data paper, unremarked
[PMID:26217777 "Our data further demonstrate that depletion of MIC26 primarily affects the level of the 22 kDa mitochondrial isoform of MIC26 but not the amount of the secreted 55 kDa isoform of MIC26."]
— an antibody signal that does not go down when the gene is knocked down is, in hindsight, the
definition of non-specific.

**Curation consequence.** Six GOA rows assert a secretory/ER/Golgi identity: `GO:0005576` x4,
`GO:0000139` x2, `GO:0005789` x2 (eight rows in total across the three terms). All of them
trace to the 55 kDa band, directly (EXP/IDA on PMID:16956892 and PMID:25764979), through
UniProt's subcellular-location vocabulary (the three `GO_REF:0000044` IEAs), or by ISS from a
pig proteomics hit. They are marked REMOVE. This is not second-guessing a curator from an
abstract: it is following the primary literature to the paper, by the original authors, that
withdrew the observation using knockouts.

### 1.4 Sequence-level corroboration (this review's bioinformatics)

UniProt's `SIGNAL 1..25` on Q9BUR5 carries `ECO:0000255` — prediction only. The paralogue
Q6UXV4/MIC27, same family, same complex, same membrane, is annotated `TRANSIT 1..27` instead.
Scored against panels of ten human TRANSIT-annotated and ten human SIGNAL-annotated proteins
(the latter weighted towards plasma apolipoproteins), the MIC26 1-25 segment behaves like a
presequence, not a signal peptide
[file:human/APOO/APOO-bioinformatics/RESULTS.md "On 4 of the 5 metrics the MIC26 1–25 segment sits closer to the mitochondrial-presequence panel than to the secretory-signal-peptide panel."].
The decisive feature is the missing hydrophobic core
[file:human/APOO/APOO-bioinformatics/RESULTS.md "Every one of the ten signal peptides in the panel reaches a 7-residue"]
— MIC26 reaches only +1.70 on that scale, below the entire secretory panel, while its
hydrophobic moment (0.602) is at the mitochondrial panel mean (0.61) and 5.8 SD from the
secretory mean.

Honest caveat recorded in RESULTS.md: MIC26 has only one Arg in the segment, unlike classic
Arg-rich presequences. But MIC27 has the same Arg deficit and UniProt still calls its
N-terminus a transit peptide, so within this family the Arg metric does not separate the
classes. Neither protein has Arg at -2/-3.

This is corroboration, not proof — the knockout/MS evidence in PMID:37279200 is what settles
it. What the sequence analysis adds is a mechanism for the historical error: a
sequence-analysis SIGNAL call on an N-terminus that is really a mitochondrial targeting
sequence, on a protein whose amphipathic helices made "apolipoprotein" a plausible name.

---

## 2. What MIC26 actually does

### 2.1 Position in the complex

MICOS has seven mammalian subunits in two subcomplexes bridged by MIC13: MIC60-MIC19-MIC25 and
MIC10-MIC26-MIC27. MIC26 sits in the MIC10 subcomplex. The MICOS complex connects through
MIC60 to SAM50 in the outer membrane to form the ~2 MDa MIB complex, and complexome profiling
resolves the assembly ladder
[PMID:26477565 "We find three main forms of the complex: A) The MICOS complex, containing all the MICOS proteins, B) a membrane bridging subcomplex, containing in addition SAMM50, MTX2 and the previously uncharacterized MTX3, and C) the complete MIB complex containing in addition DNAJC11 and MTX1."].
MIC26 and MIC27 are the family's late additions in evolution
[PMID:26477565 "Mic23 and Mic27 appear to be the youngest MICOS proteins, as they only occur in opisthokonts."],
which is exactly what PANTHER encodes: PTHR14564 contains only opisthokont MIC26/MIC27
sequences.

### 2.2 Crista junction formation — core, but partially redundant with MIC27

Three human datasets, with a real tension between them:

- Koob 2015, siRNA in HeLa: significant reduction in CJ number [PMID:25764979, quoted above].
- Ott 2015, shRNA in HEK293: no effect
  [PMID:25781180 "Mic25/CHCHD6, Mic27/ApoOL and Mic23/ApoO appear to be periphery subunits of the MICOS complex, because their depletion does not affect cristae morphology or stability of other components."].
- Anand 2020, CRISPR knockout in HAP1 — the cleanest design, single and double knockouts side
  by side: [PMID:32788226 "SKOs and DKO cells have significant reduction in CJs per mitochondrial section."]
  with the double knockout worse than either single.

The knockout data break the tie in favour of a real but redundant contribution: MIC26 alone is
dispensable for complex integrity
[PMID:32788226 "we found that MIC26 and MIC27 are dispensable for the stability and integration of the remaining MICOS subunits into the complex suggesting that they assemble late into the MICOS complex"]
yet its loss still measurably costs crista junctions. Human genetics agrees: a missense
I117T
[PMID:32439808 "The mutation caused impaired processing of the protein during import and faulty insertion into the IMM. This was associated with altered MICOS assembly and cristae junction disruption."]
and a C-terminal nonsense E178\*
[PMID:37649161 "MIC26 KO cells expressing MIC26 harboring the respective APOO/MIC26 mutation showed mitochondria with perturbed cristae architecture and fragmented morphology resembling MIC26 KO cells."]
both cause mitochondrial disease through cristae disruption.

So `GO:0042407 cristae formation` is core for MIC26 specifically, not merely inherited from the
complex — the single-gene knockout phenotype is the evidence that distinguishes the two.

### 2.3 Cardiolipin: regulate, yes; bind, not demonstrated for MIC26

This is the easiest place on this gene to over-annotate, because the paralogue really does bind
cardiolipin and the two are routinely discussed together.

- **MIC27/APOOL binds cardiolipin in vitro** [PMID:23704930 "It specifically binds to cardiolipin in vitro but not to the precursor lipid phosphatidylglycerol."].
  That is APOOL, a different gene.
- Anand 2020 restates the attribution unambiguously
  [PMID:32788226 "MIC26 and MIC27 are part of the subcomplex of MICOS, MIC13-MIC10-MIC26-MIC27 where MIC27 was shown to bind to cardiolipin (CL)"].
- What MIC26 does do is **set cardiolipin levels**, and it does so in its own single knockout
  [PMID:32788226 "We found significantly reduced levels of cardiolipin in DKO and MIC26 KO cells, whereas they remain normal in MIC27 KO cells"],
  with cardiolipin causally upstream of the OXPHOS phenotype
  [PMID:32788226 "While cardiolipin was reduced in DKO cells, overexpression of cardiolipin synthase in DKO restores the stability of RCs/SC."].
  Koob 2015 independently linked MIC26 levels to tafazzin.
- A 2026 simulation study predicts that Mic26 (human sequence: they model residues up to 198)
  recruits cardiolipin at a positive loop
  [PMID:42647630 "We found that the MIC10 proteins Mic10, Mic26, and Mic27 strongly recruit cardiolipin at conserved positive loop motifs, driving oligomerization of these subunits and resulting in the stabilization of curvature in model membranes."],
  but that is coarse-grained molecular dynamics on an AlphaFold model
  [PMID:42647630 "Using structure prediction tools and multiscale simulations, we examined the role of the MIC10 subcomplex of the mitochondrial contact site and cristae organizing system (MICOS)."],
  not a binding assay.

**No `GO:1901612 cardiolipin binding` annotation is proposed for APOO.** One NEW row is
proposed: `GO:1900208 regulation of cardiolipin metabolic process`, IMP, on the human
single-knockout lipidomics.

### 2.4 MIC10 oligomer regulation — yeast, so far

[PMID:29733859 "We report that Mic26 exerts a destabilizing effect on Mic10 oligomers and thus functions in an antagonistic manner to the stabilizing subunit Mic27."]
That is *Saccharomyces cerevisiae* Mic26. The human counterpart is the reciprocal protein-level
regulation seen by Koob and Anand (knocking out one raises the other, post-transcriptionally),
which is not the same claim. Not annotated on human APOO.

### 2.5 Mitochondrial morphology — MIC26-specific, mechanism unknown

MIC26 knockout fragments mitochondria in human HAP1 cells and MIC27 knockout does not
[PMID:32788226 "MIC26 KO and DKO cells show a similar increase in the extent of mitochondrial fragmentation"],
with fusion machinery unaffected. The authors decline to interpret it
[PMID:32788226 "Further experiments are required to understand why and how MIC26 specifically regulates mitochondrial dynamics."].
Mouse macrophage knockout reaches the same phenotype by a different route
[PMID:37995600 "Mechanistically, the loss of MIC26 resulted in an abnormal mitochondrial inner membrane structure, increased mitochondrial fission, and decreased mitochondrial membrane potential."].
Recorded as a knowledge gap and a suggested experiment rather than a GO annotation: it is a
reproducible steady-state morphology phenotype whose mechanistic relation to MIC26's structural
role is exactly what the primary authors say is unknown.

### 2.6 Physiology (non-core)

Transgenic human APOO in mouse heart promotes lipotoxic cardiomyopathy [PMID:24743151];
adipocyte-specific knockout impairs BAT thermogenesis
[PMID:37088120 "APOO deficiency disrupted mitochondrial structure in brown adipocytes and impaired oxidative phosphorylation, thereby inducing a shift from oxidative to glycolytic metabolism, increasing lipogenic enzyme levels and BAT whitening."];
macrophage-specific knockout increases efferocytosis [PMID:37995600]. These are mouse,
tissue-specific, downstream of the cristae/OXPHOS defect, and none is annotated in the current
GOA set. They are not proposed as new human annotations.

---

## 3. The two IBA rows

Family PAINT slice fetched to `interpro/panther/PTHR14564/PTHR14564-paint.tsv`. The family has
**one** PAINT node carrying **two** IBD annotations — exactly the two IBAs on APOO:

| node | GO term | aspect | IBD seeds | date |
|---|---|---|---|---|
| PTN001803267 | GO:0061617 MICOS complex | C | `FB:FBgn0038400`, `UniProtKB:Q6UXV4`, `UniProtKB:Q9BUR5` | 2024-07-30 |
| PTN001803267 | GO:0042407 cristae formation | P | `UniProtKB:Q9BUR5` | 2018-05-10 |

Donors resolved:

- `FB:FBgn0038400` -> UniProt **Q9VEY5**, *Drosophila melanogaster* **Mic26-27** (CG5903,
  dApoO; TrEMBL, unreviewed). The fly has a single pre-duplication gene covering both paralogues.
  QuickGO shows Q9VEY5 carries `GO:0061617` **IMP** from PMID:32439808 and **IGI** from
  PMID:38253420 — experimental grounding on the fly side.
- `UniProtKB:Q6UXV4` = human **APOOL/MIC27**. QuickGO shows two independent **IDA**
  `GO:0061617` annotations (PMID:25781180, PMID:25997101).
- `UniProtKB:Q9BUR5` = **APOO itself**. The target appearing in its own WITH/FROM is expected:
  its four direct IDA `GO:0061617` rows and its IMP `GO:0042407` row are among the descendant
  evidences the PAINT curator weighed when placing the IBD. Not circular, and not to be marked
  `CIRCULAR_OR_REDUNDANT`.

Node placement: PTHR14564 contains only MIC26 and MIC27 orthologues (9 entries in
`PTHR14564-entries.csv`: human/mouse/bovine MIC26, human/mouse/bovine/orangutan/chicken MIC27,
*C. elegans* moma-1). Both human paralogues and the single fly gene receive IBA from
PTN001803267, so the node sits at or near the family root, before the MIC26/MIC27 duplication.
APOO is inside the inheriting clade with its own experimental evidence for both terms, and
there is no IRD/IKR anywhere in the slice. Both IBAs: `NO_FAILURE_CORE`.

The cristae-formation IBD is seeded by a single gene — human APOO itself. Per
`projects/IBA_REVIEW.md`, a short donor list is not weak evidence; the claim is about where the
function arose, and the curator had the whole tree. Nothing in the family contradicts it, and
the fly and worm members are cristae-shaping proteins.

---

## 4. The SAM complex row is a complexome-profiling projection

`GO:0001401 SAM complex`, HDA, PMID:26477565. Queried QuickGO by
`reference=PMID:26477565&goId=GO:0001401`: **12 entities**, resolved individually —
MIC10 (Q5TGZ0), MIC13 (Q5XKP0), MIC19 (Q9NX63), MIC25 (Q9BRQ6), MIC26 (Q9BUR5), MIC27 (Q6UXV4),
MIC60 (Q16891), SAMM50 (Q9Y512), MTX1 (Q13505), MTX2 (O75431), MTX3 (Q5HYI7), HSPA9 (P38646).
That is the whole MIB complex, not the SAM complex: everything that co-migrated in one
complexome profile received the SAM term. The SAM complex is defined as "A large complex of the
mitochondrial outer membrane"; MIC26 is a single-pass **inner**-membrane protein. The same
reference already produces the correct `GO:0140275 MIB complex` row for APOO, so nothing is
lost by removing the SAM row.

---

## 5. GO term definitions consulted (QuickGO `/ontology/go/terms/<id>/complete`)

- `GO:0042407` cristae formation: "The assembly of cristae, the inwards folds of the inner
  mitochondrial membrane." Descendant of `GO:0007007` (ancestor list confirmed via
  `/ancestors?relations=is_a,part_of`). Not obsolete; no secondary ids.
- `GO:0061617` MICOS complex: names MIC26 among the *S. cerevisiae* subunits in its own
  definition.
- `GO:0007007` inner mitochondrial membrane organization: the parent of cristae formation —
  true here, but strictly less informative than the IMP-supported child, hence MODIFY.
- `GO:0001401` SAM complex: "A large complex of the mitochondrial outer membrane…".
- `GO:0140275` MIB complex: "…components of the MICOS complex in the inner mitochondrial
  membrane, the SAM complex in the outer membrane, a conserved DNAJ protein (human DNAJC11) and
  Metaxin 1." Exactly right.
- `GO:0044284` mitochondrial crista junction; `GO:0005743`; `GO:0005739`; `GO:0005576`;
  `GO:0000139`; `GO:0005789`; `GO:0005198`; `GO:0180020`; `GO:1900208` — all checked, none
  obsolete.

InterPro2GO (`GO_REF:0000002`): IPR019166 "MICOS complex subunit MIC26/MIC27" and IPR033182
"MICOS complex subunit MIC26/MIC27, animal" both map to exactly `GO:0042407` + `GO:0061617`.
Correct family, correct terms.

ARBA (`GO_REF:0000120`): ARBA00026962 asserts `GO:0005739`; it has 380 condition sets, and
condition set 26 is `InterPro id IPR019166` + `taxon Eukaryota`. APOO satisfies it.

---

## 6. The affinage record

`self_evaluation_pairwise: win`, `faith_pct: 100.0`, trust gates clear (`.affinage.log`:
"APOO: trust gates clear"). The narrative is about the right protein — MIC26, Q9BUR5 — with no
symbol collision, and it correctly foregrounds the 2023 refutation of the secreted isoform,
which is the single most important fact about this gene's annotations. Substantively strong.

**Two defects found:**

1. **A wrong PMID, used twice.** Affinage cites `PMID:26217776` alongside PMID:25764979 for the
   MIC26 crista-junction and MIC26/MIC27-antagonism findings, labelling it *Biochimica et
   biophysica acta*. PMID:26217776 is in fact "Mass spectrometry analysis of K63-ubiquitinated
   targets in response to oxidative stress" (Silva & Vogel, *Data Brief* 2015) — an unrelated
   yeast ubiquitination dataset. The intended paper is almost certainly **PMID:26217777**,
   "Data supporting the role of the non-glycosylated isoform of MIC26 in determining cristae
   morphology" (Koob, Barrera, Anand, Reichert, *Data Brief* 2015) — one digit away, correct
   authors, correct content. Verified by fetching both. Nothing in this review is cited to
   26217776.
2. **Imported GO grounding not reused.** Affinage's `mechanism_profile` proposes
   `GO:0005198 structural molecule activity` and `GO:0005739 mitochondrion`. Both were
   re-derived here from the primary literature and term definitions rather than imported; they
   happen to agree, which is reassuring but was not assumed.

**What affinage missed** (found by independent PubMed E-utilities searches on `APOO AND
mitochondria`, `MIC26 MICOS`, `apolipoprotein O cristae` — Europe PMC REST was unavailable):

- **PMID:23704930** (Weber 2013) — the paper that identified APOO in the Mitofilin/MINOS complex
  by complexome profiling in the first place, *and* the source of the cardiolipin-binding claim
  that belongs to APOOL rather than APOO. Its absence is precisely the failure mode the brief
  warns about: the decisive paper is titled for the paralogue.
- **PMID:26477565** (Huynen 2016) — the origin of three GOA rows (MICOS, MIB and the erroneous
  SAM complex) and of the opisthokont-restriction fact that explains the PANTHER family.
- **PMID:42647630** (2026, *Sci Adv*) — the current structural model of the MIC10 subcomplex and
  the only source making any cardiolipin-recruitment claim about MIC26 itself.
- **PMID:26217777** — the intended target of the wrong citation above.
- **PMID:25781180** and **PMID:25997101** — both cited by GOA, both absent from the affinage
  citation list, and PMID:25781180 is the one paper reporting a *negative* cristae result for
  MIC26 depletion.

---

## 7. Reconciliation checks run

- GOA rows ↔ YAML entries: 35 ↔ 35, matched on
  (term id, evidence code, reference, normalized WITH/FROM), scripted, no leftovers either side.
- Every `supporting_text` verified as a verbatim substring of its cache file with
  `checkquotes.py` (which also checks `file:` references, unlike CI).
- Interaction partners resolved against UniProt: Q16891 = IMMT/MIC60 (758 aa), Q5TGZ0 =
  MICOS10/MIC10 (78 aa), Q6UXV4 = APOOL/MIC27 (268 aa). ISS donor F1SPZ9 = *Sus scrofa* APOO,
  TrEMBL, 166 aa (shorter than the 198 aa human protein); its own `GO:0005576` is an **HDA**
  from the same PMID:22261194 porcine ECM proteomics run, i.e. the human ISS is transferred
  from a single high-throughput detection in an ECM-enriched cardiac fraction — a preparation
  in which abundant mitochondrial proteins are a standard contaminant, from a tissue that is
  ~30% mitochondria by volume. `SOURCE_WEAK_OR_INFERRED`.
- Ortholog-side check: UniProt's mouse entry Q9DCZ4 (Mic26) already lists **only**
  "Mitochondrion inner membrane" as its subcellular location, while the human entry still lists
  Secreted/Golgi/ER. The correction has reached one species' record and not the other.

## 8. Open items flagged for UniProt / GOA

- Q9BUR5 `SUBCELLULAR LOCATION` still carries Secreted, Golgi apparatus membrane and
  Endoplasmic reticulum membrane with `ECO:0000269|PubMed:16956892` / `PubMed:25764979`,
  and the `PTM` line still carries the chondroitin-sulfate O-glycosylation. PMID:37279200
  withdraws all of it. While those lines stand, `GO_REF:0000044` will keep regenerating the
  three IEA rows removed here.
- `SIGNAL 1..25` on Q9BUR5 versus `TRANSIT 1..27` on the paralogue Q6UXV4 is an internal
  inconsistency in the family (see §1.4).
