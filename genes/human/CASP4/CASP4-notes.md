# CASP4 (human caspase-4, P49662) — review journal

Reviewer: AI curation pass, 2026-09-17. 99 GOA annotations reviewed.

## 1. What CASP4 is

Human CASP4 (originally cloned as ICH-2 / TX / ICE(rel)-II in 1995) is an inflammatory
caspase of the caspase-1 subfamily, encoded in the CASP1/CASP4/CASP5 cluster on 11q22.
It has an N-terminal CARD followed by a p20/p10 catalytic protease domain with the
canonical cysteine nucleophile, and it cleaves after Asp at P1.

The founding papers already showed it is a bona fide protease that is not an IL-1β
converting enzyme in the classical sense:
[PMID:7797510 "Purified ICH-2 is functional as a protease in vitro."] and
[PMID:7743998 "Transfection experiments demonstrate that TX is a protease which is able to
cleave itself and the p30 ICE precursor, but not to generate mature IL-1 beta from
pro-IL-1 beta."]

Its defining modern role is as the effector of the **non-canonical inflammasome**: it is a
cytosolic receptor for bacterial LPS that, on engaging LPS, oligomerizes, autoprocesses,
and cleaves GSDMD to drive pyroptosis
[PMID:26375003 "Caspase-1 and caspase-4/5/11 specifically cleaved the linker between the
amino-terminal gasdermin-N and carboxy-terminal gasdermin-C domains in GSDMD, which was
required and sufficient for pyroptosis."].
Autoprocessing is mechanistically required, not incidental
[PMID:32109412 "we show site-specific caspase-4/11 autoprocessing, generating a p10
product, is required and sufficient for cleaving GSDMD and inducing pyroptosis."] and
[PMID:37558421 "Here, we show that caspase-4 first dimerises then self-cleaves at two
sites-D270 and D289-in the interdomain linker to acquire full proteolytic activity, cleave
GSDMD, and induce cell death."].

It also directly matures pro-IL-18, which two independent 2023 structures established
[PMID:37993714 "Caspase-4 cleaves the same tetrapeptide site in pro-IL-18 as caspase-1."]
[PMID:37993712 "Here we demonstrate that the lipopolysaccharide receptor caspase-4 from
humans and other mammalian species (except rodents) can cleave pro-IL-18"].

## 2. Contested question A — what does CASP4 actually engage?

GOA carries `GO:0001530 lipopolysaccharide binding` (IDA, PMID:25119034 and PMID:37993712)
and its parent `GO:0008289 lipid binding` (IDA ×3). The IDA rests on the 2014 Nature paper
[PMID:25119034 "Human caspase-4 and the mouse homologue caspase-11 (hereafter referred to
as caspase-4/11) and also human caspase-5, directly bound to LPS and lipid A with high
specificity and affinity."], i.e. a direct, high-affinity molecular interaction with lipid A.

The 2026 Broz-lab paper reframes the ligand as a **membrane surface with geometry**:
[PMID:41702406 "Fragmented LPS micelles presented additional micelle tips that served as
binding and activation sites for caspase-4, indicating that caspase-4 engages LPS membranes
with defined geometry rather than individual LPS molecules."] and
[PMID:41702406 "Thus, GBP-mediated deformation of the LPS-rich outer bacterial membrane
generates regions of positive curvature that expose lipid A, enabling caspase-4 binding,
oligomerization, and activation."], with GBP1 an obligate upstream mechanoenzyme
[PMID:41702406 "GBP1 was essential for caspase-4 activation during infection."].

**My reading: these are not contradictory at the level GO annotates.** The same paper still
calls lipid A the cognate ligand [PMID:41702406 "we investigated how caspase-4 accesses its
cognate ligand, the hydrophobic lipid A moiety of LPS"], and the concurrent Sci Adv study
localises the chemical recognition event to a lipid-binding pocket in the CARD
[PMID:41477831 "Using HDX-MS, we identified a hydrophobic pocket formed by helices α1, α2,
and α5 in caspase-4/11 CARD that is critical for recognizing the acyl chains of LPS."].
The curvature result constrains **presentation and avidity** (how many lipid A moieties are
accessible, and where), not whether the CARD chemically binds LPS. It is also entirely
consistent with the older GBP1 work, which had already framed GBP1's job as unmasking lipid A
[PMID:32510692 "Binding of polymerizing hGBP1 to the bacterial surface disrupts the
O-antigen barrier, thereby unmasking lipid A, eliciting caspase-4 recruitment"] and
[PMID:31268602 "GBP1 facilitated caspase-4 recruitment to Salmonella leading to its enhanced
activation and pyroptosis."]; and with 2026 work putting caspase-4 recruitment at LPS-bearing
surfaces of *extracellular* bacteria [PMID:42265284 "GBP1 promotes caspase-4 recruitment to
actin-rich pedestals, leading to pyroptosis and IL-18 release."].

Decision: **ACCEPT `GO:0001530`** (do not MODIFY, do not REMOVE), and record the curvature
caveat in the annotation `reason` and in `suggested_questions`. GO has no term for "binding
to a curved lipid membrane surface", and inventing one on a single paper would be premature
— a `membrane curvature sensing` style term would be the thing to propose if the result is
replicated. `GO:0008289 lipid binding` is MODIFY→`GO:0001530`: all three IDA rows derive from
LPS/lipid A binding experiments and the specific child is already present.

Caveat against that MODIFY worth flagging: a 2025 Cell Reports paper reports a non-LPS lipid
ligand [PMID:41264415 "we have identified SM C12 as a ligand for caspase-4"]. If that holds,
the generic `lipid binding` parent is independently informative rather than redundant.

## 3. Contested question B — stoichiometry and the "receptor" abstraction

Two 2026 structural papers agree that there is no clean 1:1 receptor–ligand complex.
[PMID:41477831 "caspase-4/11 CARDs are intrinsically unstructured in their resting state and
adopt an α-helical conformation upon LPS engagement."] — folding-on-binding, then
polymerization; and
[PMID:42546204 "we determine the stoichiometry of the non-canonical inflammasome showing that
it is heterogeneous, comprised of three major complexes with different numbers of LPS and
caspase molecules."]. The protease domain is monomeric until assembly
[PMID:42546204 "The NMR results presented establish that the protease domain of caspase-11 is
monomeric in isolation."].

This does not change any GO term, but it does mean `GO:0160074 non-canonical inflammasome
complex` should be read as a heterogeneous assembly, not a defined stoichiometric complex.
Note that the PNAS NMR work is on **caspase-11** CARD, not caspase-4 (see §5).

## 4. Contested question C — what does CASP4 cleave?

New substrate claim, 2026:
[PMID:42044191 "intracellular LPS and the gram-negative bacterial pathogen Salmonella
activate CASP4/5 in macrophages to directly cleave and activate CASP3 and CASP7."], with a
direct biochemical demonstration using catalytically dead substrates and site mutants
[PMID:42044191 "CASP1, CASP4, CASP5 and to a lesser extent, CASP11, processed CASP3C163A and
CASP7C186A but failed to process the D175A and D198A mutants"], feeding into GSDME
[PMID:42044191 "Activated CASP3 subsequently cleaves gasdermin E (GSDME)."] and concluding
[PMID:42044191 "defining CASP4/5 as dual apoptotic initiator and inflammatory caspases in
innate immunity."].

The same paper demotes the textbook CASP4→GSDMD axis in cells:
[PMID:42044191 "In CASP1 KO cells, GSDMD processing was nearly abolished suggesting most
GSDMD cleavage downstream of non-canonical inflammasome activation is mediated by CASP1"],
which they say is consistent with their own earlier work
[PMID:42044191 "This is consistent with our previous findings that GSDMD is cleaved less
efficiently in cells by CASP4 and CASP5 than by CASP1"].

**My reading.** This is a *relative flux* claim in THP-1 cells, not a claim that CASP4 cannot
cleave GSDMD — the same paper's own in vitro control shows it does
[PMID:42044191 "As expected, the inflammatory caspases efficiently processed GSDMD at both
time points, confirming their catalytic activity"] (verbatim text checked in cached full
text). Direct CASP4→GSDMD cleavage is established by reconstitution and structure
(PMID:26375003, PMID:32109412) and those remain unchallenged as *biochemistry*. So
`GO:0004197` and the GSDMD-maturation annotations stand. What is genuinely unresolved is the
*quantitative* division of labour in intact human macrophages, and whether CASP3/CASP7 should
be curated as CASP4 substrates on the strength of one study. I did **not** add a NEW
annotation for CASP3/7 activation — one paper, and it is the exact point in dispute. It is
recorded in `suggested_questions` and in the `reason` on `GO:0006915`.

A second, older substrate dispute worth flagging: UniProt asserts CASP4 "does not directly
process IL1B (PubMed:7743998, PubMed:7797510, PubMed:7797592)", whereas
[PMID:37558421 "caspase-4 dimerisation and self-cleavage at D289 generate a caspase-4 p34/p9
protease species that directly cleaves pro-IL-1β, resulting in its maturation and secretion
independently of the NLRP3 inflammasome in primary human myeloid and epithelial cells."].
Both positions are in the record; no GO term currently turns on it.

## 5. Mouse Casp11 is not a 1:1 ortholog — which annotations depend on it?

Mouse has a single *Casp4* gene (MGI:107700, protein commonly called caspase-11); human has
the paralog pair CASP4/CASP5. Functional divergence is documented in the primary literature:
[PMID:37993714 "Here we show that activated human caspase-4, but not mouse caspase-11,
directly and efficiently processes IL-18 in vitro and during bacterial infections."], and
PMID:37993712 restricts pro-IL-18 cleavage to mammals "except rodents". PMID:42044191 finds
CASP11 processes CASP3/7 only "to a lesser extent". Conversely, cross-species complementation
does work for the core LPS→pyroptosis axis
[PMID:25119034 "LPS-induced cytotoxicity was mediated by human caspase-4 that could
functionally complement murine caspase-11."].

Annotations whose support runs through mouse Casp4/11 (checked against the PAINT file
`interpro/panther/PTHR47901/PTHR47901-paint.tsv`):

| term | IBD node | seeds |
|---|---|---|
| GO:0070269 pyroptotic inflammatory response | PTN002573059 | UniProtKB:P49662 (CASP4 itself), MGI:MGI:107700, zebrafish caspa/caspb |
| GO:0050729 positive reg. of inflammatory response | PTN002573059 | UniProtKB:P49662 (itself), MGI:MGI:107700 |
| GO:0072558 NLRP1 inflammasome complex | PTN002573059 | UniProtKB:P51878 (CASP5), zebrafish caspa/caspb |
| GO:0005829 cytosol | PTN008306143 | includes P49662 itself, P51878, MGI:MGI:107700 |
| GO:0043525 positive reg. of neuron apoptotic process | PTN000047947 | RGD:2275 Casp3, RGD:620945 Casp8, RGD:69274 Casp2, RGD:70967 Casp6, MGI:MGI:1277950 Casp9, WB:WBGene00000417 ced-3 |

Donor identities resolved via mygene.info; P51878 confirmed as CASP5 via UniProt REST.

The first three rows include CASP4's **own** experimental annotation among the IBD seeds,
which per project guidance is the expected, non-circular marker that the node is
experimentally grounded on the target itself. Those are ACCEPTed. The last two are the
problematic ones:

- **GO:0072558 NLRP1 inflammasome complex** — the GO definition itself names only caspase-1
  and caspase-5 ("An inflammasome complex that consists of two components, NLRP1 (NALP1) and
  caspase-1 or caspase-5"). The IBD was seeded by CASP5 plus two zebrafish caspases; there is
  no experimental placement of human CASP4 in an NLRP1 inflammasome. Marked
  MARK_AS_OVER_ANNOTATED with a structured propagation_review (paralog transfer + complex
  mismatch). CASP4's complex is GO:0160074.
- **GO:0043525 positive regulation of neuron apoptotic process** — seeded exclusively by
  apoptotic caspases (Casp2/3/6/8/9, ced-3) at the deep pan-caspase node PTN000047947, and
  propagated to an LPS-sensing inflammatory caspase. Marked MARK_AS_OVER_ANNOTATED with a
  structured propagation_review.

## 6. Other calls worth recording

- `GO:0005576 extracellular region` (IEA + EXP, PMID:22246630) looked suspicious but is
  grounded: [PMID:22246630 "we show that caspase-4 expression is required for UVB-induced
  activation of proIL-1β and for unconventional protein secretion by skin-derived
  keratinocytes."] and UniProt records "Released in the extracellular milieu by keratinocytes
  following UVB irradiation". KEEP_AS_NON_CORE, not removed.
- ER/mitochondrion localisation and ER-stress apoptosis come from a coherent older literature
  [PMID:15123740 "We found that human caspase-4, a member of caspase-1 subfamily that includes
  caspase-12, is localized to the ER membrane, and is cleaved when cells are treated with ER
  stress-inducing reagents, but not with other apoptotic reagents."] and
  [PMID:23661706 "TMEM214 was localized on the outer membrane of the ER and constitutively
  associated with procaspase 4, which was also critical for ER stress-induced apoptosis."].
  All KEEP_AS_NON_CORE — real, reproduced, but a separate arm from LPS sensing.
- `GO:2000494 positive regulation of interleukin-18-mediated signaling pathway` (IDA,
  PMID:33377178) is the wrong abstraction: CASP4 makes mature IL-18, it does not act inside
  the IL-18 receptor signalling pathway. MODIFY → `GO:0032741 positive regulation of
  interleukin-18 production`.
- `GO:1903265 positive regulation of tumor necrosis factor-mediated signaling pathway` (IDA,
  PMID:16920334) comes from a HeLa overexpression study whose actual finding is a CARD–CARD
  interaction [PMID:16920334 "in addition to the known interaction of Cop and caspase-1, we
  demonstrated a novel interaction of Cop with caspase-4."]. MARK_AS_OVER_ANNOTATED.
- Three bare `GO:0005515 protein binding` IPI rows (BioPlex PMID:33961781 with Q17R89;
  cathepsin G PMID:29077095; SERPINB1 PMID:30692621) → MARK_AS_OVER_ANNOTATED per project
  guidance. The SERPINB1 and cathepsin G interactions are real and mechanistically meaningful
  [PMID:30692621 "Here we report that serpin family B member 1 (SERPINB1) limited the activity
  of those caspases by suppressing their caspase-recruitment domain (CARD) oligomerization and
  enzymatic activation."] — the objection is to the uninformative term, not the experiment.
- `GO:0032991 protein-containing complex` (IDA) is likewise uninformative →
  MARK_AS_OVER_ANNOTATED.
- `GO:0061702 canonical inflammasome complex` is kept non-core: CASP4 does feed NLRP3/NLRP6
  canonical inflammasomes [PMID:26508369 "Here we report that caspase-4 and caspase-5 mediate
  IL-1α and IL-1β release from human monocytes after LPS stimulation."]
  [PMID:33377178 "After LPS priming, cytosolic Streptococcus mutans LTA triggered
  NLRP6-caspase 4 inflammasome activation."], but its own complex is the non-canonical one.

## 7. What I could not resolve

1. Whether the ligand of CASP4 should be curated as an LPS molecule or an LPS-membrane
   surface of defined curvature. Kept as `lipopolysaccharide binding`; flagged.
2. Whether CASP3/CASP7 are genuine physiological CASP4 substrates. One paper, direct
   biochemistry, but it is the disputed point; no NEW annotation added.
3. Whether CASP4 or CASP1 carries most GSDMD cleavage in human macrophages. Does not change
   the MF annotation but would change how a GO-CAM should wire the pathway.
4. Whether CASP4 directly processes pro-IL-1β (PMID:37558421 yes; UniProt/1995 papers no).
