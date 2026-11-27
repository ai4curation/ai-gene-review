# STK36 (human, Q9NRP7) — curation notes

Working journal for the GO annotation review.

## 1. What the protein is

STK36 (Fused homolog, EC 2.7.11.1) is a 1315-residue serine/threonine protein
kinase with an N-terminal kinase domain (UniProt `DOMAIN 4..254`, catalytic
proton acceptor Asp-125, ATP-binding Lys-33) followed by a long, largely
uncharacterised C-terminal region. It is the vertebrate orthologue of Drosophila
Fused (Fu).

PANTHER classification (authoritative source `interpro/panther/panther-members.tsv`):

```
Q9NRP7	PTHR22983:SF6
```

`PTHR22983:SF6` is `SERINE_THREONINE-PROTEIN KINASE 36`, and Drosophila fu
(P23647) sits in the same subfamily. Sharing a PANTHER subfamily is direct
classification support for the STK36-fu orthology, independent of pathway
reasoning — which matters here, because the vertebrate and fly proteins differ in
how essential they are (section 4). ULK3, the other vertebrate Fused-family
kinase active in Hedgehog signalling, is in a *different* PANTHER family, which is
why `modules/hedgehog_signaling.yaml` records two family ids for its
`fused_family_kinase` annoton (PTHR22983 plus PTHR24348) rather than one. ULK4,
STK36's closest paralogue, is a pseudokinase.

The GOA row `GO:0106310 protein serine kinase activity` is an ISS transferred
directly from Drosophila fu (`UniProtKB:P23647`), so the classification and the
annotation record agree on the orthology.

Human disease: homozygous loss of function causes primary ciliary dyskinesia 46
(CILD46), with a central-pair axonemal defect and no laterality abnormality
[PMID:28543983 "We identified homozygous loss-of-function mutations in STK36 in
one PCD-affected individual with situs solitus."].

## 2. Established catalytic activity and its regulation

STK36 is a genuine, active kinase, and the activity has been measured rather than
inferred. Zhou et al. 2023 assayed immunopurified STK36 on a GST-Gli2N substrate,
identified the activation-loop autophosphorylation sites, and used the
kinase-dead and phospho-mutant forms as controls:

- [PMID:38096226 "In an in vitro kinase assay, we found that immunopurified Stk36 phosphorylated GST-Gli2N equally well regardless of whether it interacted with Ulk4 or not, suggesting that Ulk4 does not regulate Stk36 kinase activity."]
- [PMID:38096226 "As shown in Figure 3D, Shh induced phosphorylation of CFP-Stk36WT but not CFP-Stk36KR on T158/S159, suggesting that Shh promotes the phosphorylation of Stk36 AL via its kinase activity, likely through trans-autophosphorylation as are the cases for other kinases."]
- [PMID:38096226 "We found that the phospho-mimetic mutation (Stk36EE) increased, whereas phospho-deficient mutation (Stk36AA) abolished Stk36 kinase activity as determined by both Stk36 T158/S159 phosphorylation and Gli2 S230/S232 phosphorylation"]
- [PMID:38096226 "Like Fu, Stk36 is phosphorylated on multiple sites in the activation loop of its kinase domain in response to Shh likely through trans-autophosphorylation, and activation loop phosphorylation is essential for its kinase activation."]
- [PMID:38096226 "Hence, phosphorylation of T158/S159 can be used as a readout for Stk36 kinase activation."]

UniProt records both half-reactions with experimental evidence codes — the Ser
reaction (Rhea:RHEA:17989, the same reaction id behind the `GO:0106310` Rhea-based
IEA row) from PMID:31279575 and PMID:38096226, and the Thr reaction
(Rhea:RHEA:46608) from PMID:38096226 — and records the autophosphorylation:
[file:human/STK36/STK36-uniprot.txt "Autophosphorylated at Thr-158 and Ser-159, activating the protein"].

Two substrates are established: GLI2 (on Ser230/Ser232, conserved with the
Fu sites on Ci) and ULK4 (on Thr1021/Thr1023).

- [PMID:31279575 "Furthermore, we provide evidence that Sonic hedgehog (Shh) activates Gli2 by stimulating its phosphorylation on conserved sites through the Fu-family kinases ULK3 and mFu/STK36 in a manner depending on Gli2 ciliary localization."]
- [PMID:31279575 "Hence, Fu-family kinase-mediated phosphorylation of Ci/Gli serves as a conserved mechanism that activates the Hh pathway transcription factor."]
- [PMID:38096226 "To confirm T1021 phosphorylation by Stk36, we carried out an in vitro kinase assay using immunopurified Fg-Stk36 as kinase and GST fusion protein containing hUlk4 sequence from aa1017 to aa1036 (GST-hUlk4C) as substrate."]
- [file:human/STK36/STK36-uniprot.txt "Interacts with ULK4; promoting association with GLI2 substrate"]

Because `GO:0004674` is directly supported by assay, the InterPro-derived
`GO:0004672 protein kinase activity` row is one level too general and should be
replaced rather than merely accepted.

There is also a UniProt-recorded *non-catalytic* requirement, from the original
Murone paper: [file:human/STK36/STK36-uniprot.txt "ULK4 adapter (PubMed:38096226). GLI2 requires an additional function of"]
— continuing "STK36 to become transcriptionally active, but the enzyme does not
need to possess an active kinase catalytic site for this to occur". This is worth
flagging as an open question rather than annotating, since no molecular activity
has been attached to it.

## 3. Where STK36 acts: ciliary tip, with ULK4

Zhou et al. established the compartment and made it mutually dependent with ULK4:

- [PMID:38096226 "In response to Hh, both Ulk4 and Stk36 colocalize with Gli2 at ciliary tip, and Ulk4 and Stk36 depend on each other for their ciliary tip accumulation."]
- [PMID:38096226 "Although dispensable for Hh-induced Stk36 kinase activation, Ulk4 is essential for Stk36 ciliary tip localization, Gli2 phosphorylation, and activation."]
- [PMID:38096226 "In this study, we found that Stk36 accumulated to the tip of primary cilium and colocalized with Gli2 in response to Shh stimulation, consistent with Gli2 being converted into Gli2A at the ciliary tip."]
- [PMID:38096226 "Adding back wild type Stk36 (Stk36WT) but not its kinase inactive form (Stk36AA) restored Shh-induced Ulk4-HA ciliary tip accumulation in DKO cells"]
- [file:human/STK36/STK36-uniprot.txt "dependent for localization to ciliary tip (PubMed:38096226). Low levels"]

This is exactly the arrangement the GO-CAM model records: `gocams/index.tsv`
lists STK36 in model `696022cd00001645` with `GO:0004674` / `GO:0045880` /
`GO:0097542`, and ULK4 in the same model with `GO:0030674` /
`GO:0045880` / `GO:0097542` — the kinase and its bridging adaptor at the same
location. The `modules/hedgehog_signaling.yaml` `fused_family_kinase` annoton
carries the same `GO:0004674` + `GO:0045880` pairing, so nothing here contradicts
the module.

STK36 is additionally cytoplasmic, present at low levels in the nucleus
(both from PMID:10806483, recorded in UniProt), and — in motile cilia — an
axonemal protein: [file:human/STK36/STK36-uniprot.txt "Cytoplasm, cytoskeleton, cilium axoneme"]
and [PMID:28543983 "Transmission electron microscopy analysis demonstrates that
STK36 is required for cilia orientation in human respiratory epithelial cells,
with a probable localization of STK36 between the RS and CP."]

## 4. The evolutionary complication, and how to read the Hedgehog annotations

This is the part of STK36 biology a reviewer has to get right, because the
literature looks contradictory until the redundancy is taken into account.

**Mouse knockouts are Hedgehog-normal.** Two independent mouse studies found no
embryonic Hedgehog phenotype:

- [PMID:16055717 "fused knockouts develop normally, being born in Mendelian ratios, but fail to thrive within 2 weeks, displaying profound growth retardation with communicating hydrocephalus and early mortality."]
- [PMID:16055717 "Specification of neuronal cell fates by Hh in the neural tube was normal in fused knockouts, and induction of Hh target genes in numerous tissues is not affected by the loss of mFu."]
- [PMID:16055717 "These results show that the mFu homologue is not required for Hh signaling during embryonic development but is required for proper postnatal development, possibly by regulating the CSF homeostasis or ciliary function."]
- [PMID:19305393 "Mouse Fu (also known as Stk36) mutants are viable and seem to respond normally to Hh signalling."]
- [PMID:19305393 "yet Fu does not have a conserved role in Hh signalling in mammals"]

**But the biochemistry is conserved, and the reason the knockout looks normal is
paralogue redundancy with ULK3.** Han et al. showed Fu-family phosphorylation of
Ci/Gli is the conserved activation mechanism and that in mammals two kinases do
it (PMID:31279575, quoted in section 2); Zhou et al. then showed the genetic
epistasis directly — ULK4 and STK36 act in one linear pathway, ULK3 in parallel:
[PMID:38096226 "Consistent with Ulk4 acting in a liner pathway with Stk36 but in
parallel with Ulk3, double KD of Ulk4 and Stk36 decreased S230/232
phosphorylation similarly to single KD of either Ulk4 or Stk36, whereas double KD
of Ulk3 and Ulk4 further decreased Shh-induced S230/232 phosphorylation compared
with single KD of Ulk3 or Ulk4"]. A single-gene knockout of one of two redundant
kinases is expected to be phenotypically silent, so the mouse results are not
evidence against the annotation.

Two further points close the loop. First, the intermediate mouse literature
already saw the cell-context dependence: [PMID:18600476 "In one cell line with
reduced mFu expression the Hedgehog signaling was severely hampered, indicating
that mFu may have a role in Hedgehog signaling and Gli regulation in some
cellular situations."] and [PMID:18600476 "However, in transient overexpression
analyses mFu was able to enhance Gli induced transcription in a manner similar to
hFU."] — this is the mouse IMP behind the human ISS rows for `GO:0007224` and
`GO:0045880`. Second, zebrafish Fu *does* have a non-redundant Hedgehog role and
mouse Fu can supply it: [PMID:19305393 "We also demonstrated that zebrafish Fu is
required both for Hh signalling and cilia biogenesis in Kupffer's vesicle."] and
[PMID:19305393 "Mouse Fu rescued both Hh-dependent and -independent defects in
zebrafish."] The mammalian protein therefore retains the activity; what changed
is the degree to which the organism depends on it alone.

Conclusion for the review: the `GO:0007224` and `GO:0045880` rows are correct and
core, and the IBA at node PTN001122621 (donors including Drosophila fu, mouse
Stk36, human STK36 and zebrafish) is sound. The redundancy belongs in the
rationale, not in a downgrade.

## 5. The second, separable function: motile ciliogenesis

STK36 has a Hedgehog-independent role that is, if anything, the more essential
one in mammals.

- [PMID:19305393 "Here we show that mouse Fu is essential for construction of the central pair apparatus of motile, 9+2 cilia and offers a new model of human primary ciliary dyskinesia."]
- [PMID:19305393 "We found that mouse Fu physically interacts with Kif27, a mammalian Cos2 orthologue, and linked Fu to known structural components of the central pair apparatus, providing evidence for the first regulatory component involved in central pair construction."]
- [PMID:28543983 "A minor PCD subgroup including defects of the radial spokes (RS) and central pair (CP) is hallmarked by the absence of laterality defects, subtle beating abnormalities, and unequivocally apparent ultrastructural defects of the ciliary axoneme, making their diagnosis challenging."]
- [file:human/STK36/STK36-uniprot.txt "Essential for construction of the central pair"]
- [PMID:37584603 "The hypomorph mutant of Stk36 (Stk36tmE4-/- ) also developed progressive hydrocephalus postnatally and dysfunctional CSF flow, with multiple defects of motile cilia, including reduced ciliary number, disorganized ciliary orientation, defected axonemal structure and inconsistent base body (BB) orientation."]
- [PMID:37584603 "Stk36tmE4-/- also disturbed the expression of Foxj1 transcription factor and a range of other ciliogenesis-related genes."]
- [PMID:37584603 "we conclude that both Stk36 and Ulk4 are crucial for CSF flow, they cooperate by direct binding with their kinase domain to regulate the Foxj1 transcription factor pathways for ciliogenesis and cilia function, not limited to CSF flow"]

Note the interesting symmetry: STK36 partners with a Costal-2-family kinesin in
*both* of its functions — KIF7 in the vertebrate Hedgehog module (through the
shared GLI-SUFU tip complex) and KIF27, the other mammalian Cos2 orthologue, in
central-pair construction (UniProt: "Interacts with SPAG16 and KIF27 (By
similarity)").

This is why the cilium-assembly annotations should be made motile-specific.
`GO:0060271 cilium assembly` is generic and covers primary cilia, but STK36-null
cells build primary cilia perfectly well — that is precisely why Hedgehog
signalling still works in them. Every ciliary phenotype reported for STK36 loss
is in motile 9+2 cilia: respiratory epithelium, ependyma, Kupffer's vesicle.
`GO:0044458 motile cilium assembly` states this correctly and remains a
descendant of `GO:0060271`, so nothing is lost.

## 6. The interaction rows

STK36 has ten bare `GO:0005515` rows, in three groups.

**(a) SUFU, two rows** (PMID:10806483 co-immunoprecipitation; PMID:25241761 in
situ proximity ligation on endogenous protein in HeLa cells). The same GOA record
already carries a more informative term for this contact from the same 2000 paper:
`GO:0001222 transcription corepressor binding`. UniProt confirms the interaction
independently: [file:human/STK36/STK36-uniprot.txt "Q9NRP7; Q9UMX1: SUFU; NbExp=3; IntAct=EBI-863797, EBI-740595;"].
The proximity-ligation row is a genuinely independent, endogenous-protein
confirmation: [PMID:25241761 "Signal transduction pathways in the cell require protein-protein interactions (PPIs) to respond to environmental cues."]

**(b) ULK4, two rows** (PMID:32707033 kinase-interactome mass spectrometry;
PMID:37584603 yeast two-hybrid plus co-IP). This is not a generic contact: ULK4
is an STK36 substrate and its bridging adaptor.
[PMID:37584603 "Here, we report that serine/threonine kinase 36 (STK36), a paralog of ULK4, directly interacts with ULK4 and this was demonstrated by yeast two-hybrid (Y2H) in yeast and coimmunoprecipitation (co-IP) assays in HEK293T cells, respectively."]
and [PMID:37584603 "The interaction region was confined to their respective N-terminal kinase domain."]
The informative molecular function is the kinase activity STK36 exerts on ULK4.

**(c) DMWD, KLF11, GFAP, ATXN3 and SPRED1, five rows, all from PMID:32814053.**
A systematic yeast two-hybrid screen of neurodegeneration-related proteins:
[PMID:32814053 "Here, we report on an interactome map that focuses on neurodegenerative disease (ND), connects ~5,000 human proteins via ~30,000 candidate interactions and is generated by systematic yeast two-hybrid interaction screening of ~500 ND-related proteins and integration of literature interactions."]
None has any functional follow-up for STK36, none is a Hedgehog or ciliary
protein, and none supports a more informative molecular function. These are the
removal case.

## 7. Notes on evidence availability

The cached record for PMID:10806483 (Murone et al. 2000) contains **title and
citation metadata only — no abstract** (`full_text_available: false`, and the
Abstract section holds just the citation block). Six GOA rows cite it: the
`GO:0001222` IDA, the `GO:0004674` and `GO:0005524` TAS rows, the `GO:0005515`
SUFU IPI, and the `GO:0005634` and `GO:0005737` IDA rows. Rather than leave all
six UNDECIDED, each was adjudicated against the *structured* UniProt annotations
that cite that same paper with experimental evidence codes — `SUBUNIT` "Interacts
with GLI1, GLI2 and GLI3 (PubMed:10806483)", `SUBCELLULAR LOCATION` cytoplasm and
nucleus with `ECO:0000269|PubMed:10806483`, `BINDING 33` ATP with
`ECO:0000305|PubMed:10806483`, and the reference-block line
`RP   ... FUNCTION, INTERACTION WITH GLI1; GLI2; GLI3 AND SUFU, TISSUE
SPECIFICITY, SUBCELLULAR LOCATION, AND MUTAGENESIS OF LYS-33` — all of which are
deterministic records of what that paper reported. Every one of the six
conclusions is independently corroborated by a later experimental row, so no
action depends on the missing abstract.

## 8. Decisions taken, and the ones deliberately not taken

Actions: 20 ACCEPT (the kinase activity, ATP binding, cilium/axoneme/ciliary-tip
locations, the smoothened-pathway and positive-regulation rows, axoneme
assembly); 9 MODIFY (`GO:0004672` to `GO:0004674`; the two SUFU protein-binding
rows to `GO:0001222`; the two ULK4 protein-binding rows to `GO:0004674`;
`GO:0007017` to `GO:0035082`; all three `GO:0060271` rows to `GO:0044458`);
5 REMOVE (the yeast two-hybrid neurodegeneration interactors); 7
KEEP_AS_NON_CORE (`GO:0001222`, nucleus x2, cytoplasm x3, cytosol); 2
MARK_AS_OVER_ANNOTATED (both `GO:0009791 post-embryonic development` rows).
Nothing left UNDECIDED.

Candidate `NEW` terms considered and rejected:

- **`GO:0090660 cerebrospinal fluid circulation`.** Two mouse studies tie STK36
  loss to hydrocephalus and defective CSF flow, and one of them puts the phrase
  in its title. It fails the participation test: STK36 does not move
  cerebrospinal fluid. The ependymal motile cilia do, and STK36's contribution is
  to build them. Annotating the fluid-flow process would be annotating a
  two-step-downstream organismal consequence — the same error as the
  `post-embryonic development` rows already marked over-annotated. The
  motile-cilium-assembly replacement is where this evidence belongs.
- **`GO:0003341 cilium movement` / `GO:0003356 regulation of cilium beat
  frequency`.** Same objection, one step closer: the axoneme and its dyneins
  generate the beat; STK36 assembles the central pair that constrains it. The
  comparator check supports this reading — mouse Stk36 carries `GO:0003351`
  (epithelial cilium movement involved in extracellular fluid movement) from a
  hydrocephalus-survey paper (PMID:21746835) and that is the *only* movement term
  on the whole family record, with no corresponding human annotation in two
  decades of curation.
- **`GO:0140693 molecular condensate scaffold activity` or an adaptor term for the
  non-catalytic GLI2 requirement.** UniProt records that GLI2 needs a function of
  STK36 that does not require an active catalytic site. That is intriguing but no
  molecular activity has been identified for it, and inventing one from a
  kinase-dead rescue result would be exactly the sort of unsupported assertion the
  guidance warns against. Raised in `suggested_questions` instead.

Terms verified against QuickGO before use (label, aspect, non-obsolete status, and
ancestry where it mattered): `GO:0044458 motile cilium assembly` (a direct child
of `GO:0060271` and a sibling rather than an ancestor of `GO:0035082`),
`GO:0035082 axoneme assembly` (a descendant of both `GO:0060271` and
`GO:0007017`), `GO:0004674`, `GO:0106310`, `GO:0001222`.
