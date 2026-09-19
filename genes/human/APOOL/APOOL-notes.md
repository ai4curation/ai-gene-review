# APOOL (MIC27, Q6UXV4) — review notes

Human APOOL, HGNC:24009, X chromosome, UniProt Q6UXV4 (`MIC27_HUMAN`, 268 aa, sequence
version 1, entry version 154 of 02-SEP-2026). Accession checked: the fetched record is
`ID   MIC27_HUMAN` with `GN   Name=APOOL; Synonyms=CXorf33, FAM121A, MIC27;`, so this is the
intended protein and not a merged-accession redirect. Secondary accessions Q3KNU7, Q5H9D1.

Despite the name, this is not a plasma apolipoprotein. UniProt: `DE   RecName: Full=MICOS
complex subunit MIC27; AltName: Full=Apolipoprotein O-like;`. The name is a 2003 secreted-protein
discovery-initiative artefact (`RN [1]`, PMID:12975309, "The secreted protein discovery initiative
(SPDI) ... to identify novel human secreted and transmembrane proteins"), and it accounts for two of
the three bad cellular-component rows. The third, SAM complex, is an independent complexome
conflation and has nothing to do with the name.

## 1. What the protein is

PANTHER family **PTHR14564** "MICOS COMPLEX SUBUNIT MIC26 / MIC27 FAMILY MEMBER" (from
`DR   PANTHER; PTHR14564;`), Pfam PF09769 (ApoO), InterPro IPR019166 / IPR033182. The family
holds two mammalian paralogues, MIC26 (APOO, Q9BUR5, 198 aa) and MIC27 (APOOL, Q6UXV4, 268 aa);
PANTHER's representative-member list for the family gives one member per invertebrate genome it
covers (*C. elegans* moma-1 Q21154, *D. melanogaster* Mic26-27 / CG5903 Q9VEY5), and the fly protein
is treated in the literature as the single MIC26/MIC27 orthologue. Huynen et al. place the pair late: [PMID:26477565 "In contrast, Mic23 and Mic27
appear to be the youngest MICOS proteins, as they only occur in opisthokonts."]

Topology (UniProt FT, evidence ECO:0000255 except where noted): TRANSIT 1–27 (mitochondrion),
TOPO_DOM 28–110 intermembrane, TRANSMEM 111–129, TOPO_DOM 130–137 matrix, TRANSMEM 138–155,
TOPO_DOM 156–268 intermembrane, disordered 187–268, phosphoserine at 204
(ECO:0007744|PubMed:24275569). Weber et al. saw the same architecture: [PMID:23704930 "APOOL
contains two hydrophobic stretches which are predicted to represent transmembrane helices"].

## 2. Localization — settled, and settled against the name

Weber et al. 2013 did the whole ladder in HeLa/143B cells. Immunofluorescence plus subcellular
fractionation: [PMID:23704930 "Endogenous APOOL was found to be entirely absent in the cytosolic
fraction and instead was detected in the mitochondrial fraction."] Alkaline carbonate extraction:
[PMID:23704930 "APOOL was found to remain fully in the membrane fraction whereas the chaperone
mtHsp60 was released efficiently, yet not completely, to the soluble fraction"] — i.e. integral or
tightly membrane-associated. Protease protection with graded digitonin: [PMID:23704930 "Taken
together, we conclude that APOOL is located in the intermembrane space consistent with the proposed
location of the Mitofilin/MINOS complex."]

Lubeck et al. 2023 closed the secreted-isoform question for the whole family, in four human cell
lines with four antibodies plus tagged constructs: [PMID:37279200 "We further excluded the presence
of a glycosylated, high-molecular weight MIC27 protein."] and [PMID:37279200 "Taken together, we
conclude that both MIC26 and MIC27 are exclusively localized in mitochondria and that the observed
phenotypes reported previously are exclusively due to their mitochondrial function."] The 55 kDa
"secreted apolipoprotein O" band that motivated the family name turned out to be a non-specific
antibody signal.

This matters because GOA carries two Reactome TAS rows placing APOOL in the **extracellular region**
and the **platelet alpha granule lumen**. I traced them: Reactome still lists Q6UXV4 among the 27
participants of *Platelet degranulation* (R-HSA-114608), with entities R-HSA-8863003 (platelet alpha
granule lumen) and R-HSA-8862979 (extracellular region); the reaction's only PubMed-backed literature
reference is Coppinger et al. 2004, a thrombin-releasate shotgun proteomics screen: [PMID:14630798
"Using a proteomics approach, we have identified more than 300 proteins released by human platelets
following thrombin activation."] That is a 2004 bulk list, nine years before anyone knew the protein
was mitochondrial. Reactome itself now *also* carries Q6UXV4 as R-HSA-8949612 "APOOL (MIC27)" in the
mitochondrial inner membrane under *Cristae formation* (R-HSA-8949613), so the platelet placement is
a stale duplicate rather than a claim Reactome is defending.

Reference-projection check (scripted, QuickGO paginated): `Reactome:R-HSA-481007` supports **134
annotations over 67 distinct gene products**, exactly two terms each — GO:0005576 ×67 and
GO:0031093 ×67. So both APOOL rows are one undifferentiated projection of a pathway membership,
carrying no APOOL-specific observation at all.

## 3. Complex membership

- **MICOS.** Weber et al. reciprocal co-IP from digitonin-solubilised HeLa mitochondria:
  [PMID:23704930 "These experiments revealed that APOOL is co-purified with Mitofilin, MINOS1, and
  SAMM50"]. Guarani et al. recovered it in MICOS IP-MS from 293T and HCT116:
  [PMID:25997101 "The result elicited the generation of an interaction map containing 13 nodes and
  20 edges (interactions) (Figure 1C), wherein we identified 5 core MICOS subunits (MIC60, MIC19,
  MIC25, MIC26 and MIC27), 3 OM known interactors (SAMM50, MTX1 and MTX2) as well as the chaperone
  DNAJC11 and TMEM11 in association with QIL1."] Ott et al. and Koob et al. agree. UniProt's SUBUNIT
  block lists MIC27 among "at least MICOS10/MIC10, CHCHD3/MIC19, CHCHD6/MIC25, APOOL/MIC27,
  IMMT/MIC60, APOO/MIC23/MIC26 and MICOS13/MIC13".
- **Within MICOS, MIC27 belongs to the MIC10 subcomplex**, not the MIC60 module. MIC13/QIL1 is what
  puts it there: [PMID:25997101 "Using quantitative proteomics, we show that loss of QIL1 resulted in
  MICOS disassembly with the accumulation of a MIC60-MIC19-MIC25 sub-complex and degradation of
  MIC10, MIC26, and MIC27."] and independently [PMID:27479602 "MIC13 is required for the assembly of
  MIC10, MIC26, and MIC27 into the MICOS complex."]
- **MIB, not SAM.** Huynen et al.'s complexome profiling resolves three nested forms:
  [PMID:26477565 "We find three main forms of the complex: A) The MICOS complex, containing all the
  MICOS proteins, B) a membrane bridging subcomplex, containing in addition SAMM50, MTX2 and the
  previously uncharacterized MTX3, and C) the complete MIB complex containing in addition DNAJC11 and
  MTX1."] MIC27 is in (A) and therefore in (C); SAMM50/MTX2 are what get *added* on top of MICOS.
  GOA nonetheless carries `part_of GO:0001401 SAM complex` HDA from this very paper. GO:0001401 is
  defined as "A large complex of the mitochondrial outer membrane that mediates sorting of some
  imported proteins to the outer membrane and their assembly in the membrane" (QuickGO). An inner
  membrane protein whose bulk faces the IMS cannot be part of an outer-membrane complex; the
  co-migration that produced the row is the MIB bridge, and the same paper's MIB row (GO:0140275) and
  MICOS row (GO:0061617) already record it correctly. This is the second name-independent defect in
  the set.

## 4. Molecular function: cardiolipin binding, and the hole in GOA

The one molecular activity ever demonstrated for this protein: [PMID:23704930 "GST-APOOL-HIS6 was
found to bind specifically to cardiolipin (CL) but not to any of the other lipids tested, notably
not even to phosphatidylglycerol the precursor of cardiolipin"] — recombinant, affinity-purified,
GST non-fusion control negative on every lipid, triplicate lipid strips.

**GOA has no molecular function for APOOL except three bare `GO:0005515 protein binding` IPI rows.**
GO:1901612 `cardiolipin binding` exists and is not obsolete (QuickGO: "Binding to cardiolipin",
`isObsolete: false`). Neither GOA nor the UniProt `DR GO` block carries it. This is the single
clearest gap in the record and is the one NEW row I add.

Mechanistic corroboration (computational, 2026): [PMID:42647630 "We found that the MIC10 proteins
Mic10, Mic26, and Mic27 strongly recruit cardiolipin at conserved positive loop motifs, driving
oligomerization of these subunits and resulting in the stabilization of curvature in model
membranes."] and [PMID:42647630 "Similar levels of CDL2 interaction were observed with Mic27, having
83% CDL2 occupancy at the connecting loop."] This is AlphaFold3 + coarse-grained/atomistic MD, not
experiment, and I treat it as such.

**Bioinformatics (this review).** `APOOL-bioinformatics/loop_conservation.py` tests the "conserved
positive loop motif" claim against the family alignment, using live UniProt sequences, lengths
asserted against `interpro/panther/PTHR14564/PTHR14564-entries.csv`, and UniProt's own TM
boundaries. The human inter-TM loop is residues **130–137 = RKGSKFKK**, five basic residues, no
acidic residue, net +5. Projected over the nine PTHR14564 representative members plus the fly PAINT
seed Q9VEY5, **10/10 carry ≥2 K/R and a net positive charge in the aligned block**, with human
MIC26 at RGSKIKK (+4) and the alignment placing APOOL R130 opposite MIC26 R129. So APOOL retains —
indeed maximises — the family's lipid-facing basic element: there is no residue-level argument for
divergence, and the retention supports cardiolipin binding as a property of MIC27 itself rather than
of the complex. Limits are stated in `APOOL-bioinformatics/RESULTS.md`: this is conservation and
charge, not a binding demonstration, and no CL-binding-deficient APOOL mutant has been reported.

The three `protein binding` IPI rows (PMID:25764979) resolve to MIC60/IMMT (Q16891), MIC10/MICOS10
(Q5TGZ0) and MIC26/APOO (Q9BUR5) — all verified against UniProt. They are real, but they are
intra-complex contacts already stated by `part_of GO:0061617`, and `protein binding` carries no
functional information. There is no informative MF to promote them to: the mechanistic claim that
would justify one — that MIC27 stabilises MIC10 oligomers — is **yeast** work (see §6), and the
human genetics contradicts transferring it.

## 5. The knockdown/knockout evidence, and the one real conflict in the literature

Three human perturbation studies, and they do not all agree.

1. **Weber 2013, miRNA knockdown, HeLa/143B.** [PMID:23704930 "The frequency of mitochondrial
   sections showing cristae with small concentric structures that appeared branched and
   interconnected was significantly increased upon downregulation of APOOL"], plus grossly reduced
   basal OCR. Overexpression gave the reciprocal perturbation (abstract: "Overexpression of APOOL led
   to fragmentation of mitochondria, a reduced basal oxygen consumption rate, and altered cristae
   morphology"). Both directions are perturbation-of-level experiments — IMP-grade, not IDA, and the
   overexpression arm is ectopic.
2. **Ott 2015, inducible shRNA knockdown, HeLa — negative.** [PMID:25781180 "knockdown of
   Mic25/CHCHD6 or of Mic27/ApoOL had no visible effect on cristae morphology"], and their headline
   conclusion [PMID:25781180 "Mic25/CHCHD6, Mic27/ApoOL and Mic23/ApoO appear to be periphery
   subunits of the MICOS complex, because their depletion does not affect cristae morphology or
   stability of other components."] They note the disagreement with Weber themselves.
3. **Anand 2020, CRISPR knockouts and the double knockout, HAP1 — resolves it.** This is the study
   that reconciles 1 and 2, because it counts crista junctions rather than scoring morphology, and
   because it removes the confound both earlier studies had: MIC26 and MIC27 regulate each other's
   levels, so a single depletion is partially compensated. [PMID:32788226 "We observed that both SKOs
   and DKO cells show significantly reduced CJs per mitochondrial section compared with the
   controls"] and [PMID:32788226 "In addition, the number of cristae per mitochondrial section was
   significantly reduced in all the KO cells compared with control, with a slightly more pronounced
   reduction in DKO cells compared with SKOs"]. The onion-stack MICOS signature appears only in the
   DKO; the single MIC27 KO gives [PMID:32788226 "Longitudinal and vesicular cristae were more
   prevalent in MIC26 KO and MIC27 KO, respectively"].

So: **MIC27 loss does reduce crista junctions in human cells**, Ott's negative result reflects the
insensitivity of qualitative morphology scoring under paralogue compensation, and `cristae formation`
(GO:0042407) is properly asserted for this gene on human experimental grounds — which GOA currently
supports only by IBA, InterPro IEA and a ComplexPortal NAS.

Two things Anand 2020 shows that constrain how far to go:

- [PMID:32788226 "MIC26 and MIC27 are dispensable for the stability and integration of the remaining
  MICOS subunits into the complex suggesting that they assemble late into the MICOS complex."] MIC27
  is therefore **not** a scaffold holding MICOS together in human cells — GO:0140378 protein complex
  scaffold activity would be wrong.
- The OXPHOS phenotype is cooperative and is proposed to be lipid-mediated: [PMID:32788226 "While
  cardiolipin was reduced in DKO cells, overexpression of cardiolipin synthase in DKO restores the
  stability of RCs/SC."] The authors' own framing is "perhaps by modulating the cardiolipin levels".
  A DKO-only, plausibly indirect effect is not a `directly_involved_in` for MIC27; it belongs in the
  knowledge gaps.

## 6. Yeast and fly work — context, not human fact

A large part of the MIC27 mechanistic literature is *S. cerevisiae* and must not be restated as human
biology (Anand 2020 directly contradicts the transfer of the scaffolding claim):

- Zerbes et al. 2016 (PMID:26968360): "Mic27 promotes the stability of the Mic10 oligomers in the
  membrane-sculpting subcomplex, whereas Mic12 is required for the coupling of the two MICOS
  subcomplexes" — yeast; Mic12 has no mammalian orthologue of that name.
- Rampelt et al. 2018 (PMID:29733859): "We report that Mic26 exerts a destabilizing effect on Mic10
  oligomers and thus functions in an antagonistic manner to the stabilizing subunit Mic27" — yeast.
- Eydt et al. 2017 (PMID:28845423): "We observe a positive genetic interaction between Mic27 and
  Mic60 and deletion of Mic27 results in impaired formation of CJs and altered cristae membrane
  curvature" — yeast.
- Friedman et al. 2015 (PMID:25918844): "Our data indicate that Mic27/Mic10/Mic12 assembles at
  cristae junctions in a respiratory complex- and cardiolipin-dependent manner" — yeast.
- *Drosophila*, single-copy member: [PMID:33268479 "We found that CG5903/MIC26-MIC27 colocalizes and
  functions with Mitofilin/MIC60 and QIL1/MIC13 as a Drosophila MICOS component; knocking down
  expression of any of these three genes predictably altered mitochondrial morphology, causing loss of
  cristae junctions, and disruption of cristae packing."] This is the experimental grounding behind
  the `FB:FBgn0038400` IBD seed.

The human-versus-yeast split is the reason I do not promote the `protein binding` IPIs to an
oligomer-stabilisation MF.

## 7. The two IBA rows

Both come from **PANTHER node PTN001803267** in PTHR14564. The local PAINT slice
(`interpro/panther/PTHR14564/PTHR14564-paint.tsv`) has exactly two IBD rows, both at that node, and
no IRD or IKR anywhere in the family:

| node | term | aspect | evidence | seeds |
|---|---|---|---|---|
| PTN001803267 | GO:0061617 MICOS complex | C | IBD | `FB:FBgn0038400`, `UniProtKB:Q6UXV4`, `UniProtKB:Q9BUR5` |
| PTN001803267 | GO:0042407 cristae formation | P | IBD | `UniProtKB:Q9BUR5` |

Donors resolved:

- `UniProtKB:Q9BUR5` = human APOO/MIC26 (UniProt REST, Swiss-Prot, `MIC26_HUMAN`). QuickGO confirms
  the experimental grounding on the donor: MIC26 carries **IDA** for GO:0061617 from PMID:25764979,
  PMID:25781180 and PMID:25997101, and **IMP** for GO:0042407 from PMID:25764979. So the
  cristae-formation IBD rests on a real MIC26 loss-of-function experiment, not on another inference.
- `UniProtKB:Q6UXV4` = the target itself. Expected and correct: APOOL's own IDA/EXP rows for MICOS
  membership are among the descendant evidences the PAINT curator used to place the node. Not
  circular.
- `FB:FBgn0038400` resolves through the UniProt cross-reference to **Q9VEY5**, *D. melanogaster*
  Mic26-27 / CG5903 (TrEMBL, unreviewed) — the protein characterised in PMID:33268479. It is not a
  key in any `interpro/panther/*/*-entries.csv` (those are accession-keyed), so this is a
  cross-reference resolution, and the accession Q9VEY5 itself is then directly usable.

Both transfers land inside the clade that inherited the function: APOOL *is* one of the two human
members of the family, it is experimentally in MICOS, and §4 shows it retains the family's basic
inter-TM loop. Note the asymmetry worth recording — the **cristae-formation** node is seeded by
MIC26 alone, so that IBA is, phylogenetically, MIC26's experiment inherited by MIC27; the
**MICOS-complex** node is seeded by both human paralogues plus the fly single-copy member. Human
MIC27-specific evidence for the inherited process has since arrived independently (Anand 2020,
§5), which is the strongest possible outcome for an IBA review.

## 8. What affinage missed / got right

Affinage trust gates cleared (`✓ APOOL: trust gates clear`), `self_evaluation_pairwise: win`,
`faith_pct: 100.0`, and the record describes the correct protein throughout — no symbol collision.
Its narrative and dated-findings table are accurate as far as they go, and it surfaced the yeast
mechanism papers, the MIC13 dependency and the DKO study that the seeded review file alone would
never have reached.

What it missed, and why it matters here:

- **PMID:42647630** (Sci Adv, Aug 2026) — the MIC10-complex structural/simulation study that supplies
  the cardiolipin-binding *mechanism* and the "conserved positive loop motif" claim my
  bioinformatics analysis tests. Published after the affinage run date (2026-06-09), so this is
  recency, not a search failure.
- **PMID:14630798** — the Coppinger platelet releasate paper. Not about APOOL at all, which is
  exactly why no gene-centred search returns it; it is only reachable by chasing the *Reactome*
  provenance of the two bogus CC rows. Without it the platelet annotations look unexplained rather
  than explained.
- **PMID:33053165** (yeast MICOS subcomplexes at ER contact sites) and **PMID:40751083** (pooled
  imaging screen flagging APOOL as perturbing mitochondrial network morphology) — minor, but both
  are genuine APOOL/Mic27 hits it did not list.

Its `mechanism_profile` proposes GO:0008289 lipid binding and GO:0005198 structural molecule
activity. I did not import either: GO:1901612 cardiolipin binding is the specific child the data
actually support, and "structural molecule activity" is contradicted for human MIC27 by Anand 2020's
dispensability result.

Its citation list contains one non-numeric id, `PMID:bio_10.1101_2025.05.20.655052` (a bioRxiv
preprint on MIC27 APEX2 proximity labelling). Not citable as a PMID and not used.

## 9. Review decisions (27 GOA rows + 1 NEW)

- **REMOVE ×6**: `GO:0005576 extracellular region` and `GO:0031093 platelet alpha granule lumen`
  (Reactome name-era projection, refuted by PMID:37279200 and PMID:23704930); `GO:0001401 SAM
  complex` (inner-membrane protein cannot be part of an outer-membrane complex; the MIB and MICOS
  rows from the same reference already capture the real relationship); and the three bare
  `GO:0005515 protein binding` IPIs. The last three follow the repository's standing policy that
  generic protein binding is not an over-annotation but an uninformative one: MODIFY is the first
  choice and is unavailable here, because the only more specific molecular function on offer is the
  yeast oligomer-stabilisation role that §6 shows does not transfer, so REMOVE applies. Removal is
  not a claim that any of the three interactions is false; all three partners are MICOS subunits and
  the shared membership is already recorded by `GO:0061617`.
- **MODIFY ×1**: `GO:0007007 inner mitochondrial membrane organization` (IC on MIB membership) →
  `GO:0042407 cristae formation`, which is a descendant of GO:0007007 (QuickGO ancestor list for
  GO:0042407 contains GO:0007007) and is already on the gene from three other sources.
- **ACCEPT ×20**: the mitochondrion / inner-membrane / MICOS / MIB / crista-junction /
  cristae-formation rows, including both IBAs.
- **NEW ×1**: `GO:1901612 cardiolipin binding`, IDA, PMID:23704930.

## 10. Open questions

Recorded as `knowledge_gaps` in the review: (i) no cardiolipin-binding-deficient APOOL mutant exists,
so the binding activity has never been tied to any cellular phenotype; (ii) whether the OXPHOS
supercomplex/ATP-synthase destabilisation in the MIC26/MIC27 DKO is a direct role or a downstream
consequence of reduced cardiolipin and lost crista junctions is explicitly unresolved by the authors;
(iii) MIC26 and MIC27 are reciprocally regulated post-transcriptionally and the mechanism is unknown,
which is what made every single-gene depletion study before 2020 hard to interpret.
