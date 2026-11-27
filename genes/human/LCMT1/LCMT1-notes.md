# LCMT1 (human, Q9UIC8) — curation notes

Review opened 2026-10-24 in response to
[geneontology/go-annotation#6632](https://github.com/geneontology/go-annotation/issues/6632),
in which a GO curator questions the four MGI annotations made from PMID:17724024
and the IBA that propagates from one of them.

Automated deep research was unavailable in this environment (no provider API key;
`just deep-research human LCMT1 --provider perplexity` exits 1 with
"No research providers available"). These notes are therefore hand-written from
the cached publications, the UniProt record and the cached Reactome entries, with
provenance for every assertion.

## What the protein is

LCMT1 is a 334-aa SAM-dependent methyltransferase that esterifies the α-carboxyl
group of the C-terminal leucine of the PP2A catalytic subunit (Leu309)
[UniProt Q9UIC8 CC:FUNCTION, "Methylates the carboxyl group of the C-terminal leucine
residue of protein phosphatase 2A catalytic subunits to form alpha-leucine ester residues."].
EC 2.1.1.233, RHEA:48544. Kinetics from the original purification: KM 0.1 µM for
PP2AD, 1.3 µM for AdoMet [UniProt Q9UIC8 CC:BIOPHYSICOCHEMICAL PROPERTIES].

The enzyme was purified from porcine brain and the human cDNA cloned in
[PMID:10600115 "The recombinant protein expressed in bacteria is soluble and the
biophysical, catalytic, and immunological properties are indistinguishable
from the native enzyme."]; the same paper establishes site specificity —
[PMID:10600115 "The methylation of PP2A by the recombinant protein is restricted to Leu(309) of PP2A(C)."]
— and, importantly for the review, that methylation itself does not change
phosphatase activity:
[PMID:10600115 "No direct effects on phosphatase activity changes were observed upon methylation of the dimeric or trimeric forms of PP2A."].

Structures: LCMT1 + AdoMet at 2.0 Å [PMID:21206058], and LCMT1 alone and in complex
with PPP2CA at 1.9 Å [PMID:21292165]. The latter shows the PP2A active site itself
contacts LCMT1 and that active-site engagement stimulates methylation
[PMID:21292165 "We demonstrated that activation of the PP2A active site stimulates methylation, suggesting a mechanism for efficient conversion of activated PP2A into substrate-specific holoenzymes"].

## Substrate scope is wider than PP2A

LCMT-1 is the major methyltransferase not only for PP2A but also for the
PP2A-family phosphatases PP4 and PP6
[PMID:27507813 "Here we use antibodies specific for the unmethylated phosphatases to show that PP6 is carboxyl-methylated and that LCMT-1 is the major methyltransferase for PP2A, PP4, and PP6 in mouse embryonic fibroblasts (MEFs)."].
This matters for term choice: the annotated MF, GO:0018423
*protein C-terminal leucine carboxyl O-methyltransferase activity*, is substrate-generic
and is the right term; a PP2A-specific MF would be too narrow.

## Localization

LCMT1 is predominantly cytoplasmic; the nucleus holds mostly the *demethylated*
PP2A pool and the opposing esterase PME-1
[PMID:17803990 "The results show that PME-1 is predominantly localized in the nucleus and harbors a functional nuclear localization signal, whereas LCMT1 is underrepresented in the nucleus and mainly localizes to the cytoplasm, Golgi region and late endosomes."].
Reactome says the same
[Reactome:R-HSA-8856945 "Methylation and demethylation are spatially separated within mammalian cells, as the majority of LCMT1 is cytoplasmic and PPME1 predominantly localizes in the nucleus (Longin et al. 2008)."].
So GO:0005829 cytosol is core and GO:0005654 nucleoplasm (Reactome TAS) is real but
peripheral.

## The four MGI annotations from PMID:17724024 (Lee & Pallas 2007)

Full text is cached (`full_text_available: true`, PMC3516869), so this review is
not second-guessing a curator from an abstract. What the paper actually shows:

1. **LCMT-1 is the major mammalian PP2A methyltransferase.** shRNA knockdown drops
   steady-state PP2Ac methylation by up to ~70%
   [PMID:17724024 "Collectively, these results show that mammalian LCMT-1 is responsible for the majority of PP2A methylation, similar to the case for the S. cerevisiae LCMT-1 homolog, Ppm1p."].
2. **Knockdown *reduces* PP2A BαAC heterotrimer formation.**
   [PMID:17724024 "Thus, LCMT-1 is important for PP2A B α AC trimer formation in mammalian cells."]
   This is the decisive point for GO:0031333: LCMT1 **promotes** complex assembly.
   The annotated term is *negative* regulation of protein-containing complex assembly.
   That is a sign error, not an over-annotation. Hwang 2016 reaches the same
   conclusion for PP2A, PP4 and PP6
   [PMID:27507813 "Collectively, our data suggest that LCMT-1 coordinately regulates the carboxyl methylation of PP2A-related phosphatases and, consequently, their holoenzyme assembly and function."],
   and so does Reactome
   [Reactome:R-HSA-8856945 "Methylation of the carboxy-termius of PP2A C enhances the affinity of the PP2A core enzyme for some regulatory subunits (Xing et al. 2008)."].
   Comparator: the budding-yeast orthologue PPM1 (Q04081) carries
   GO:0065003 *protein-containing complex assembly* (IMP, PMID:11060018) — the
   positive-sense term — and carries no negative-regulation term (QuickGO, 2026-10-24).
3. **Spindle checkpoint (GO:0090266) is an inference the data do not carry.** The
   only checkpoint-relevant observation is that knockdown cells die more in
   nocodazole, from which the authors *suggest* a role:
   [PMID:17724024 "The increased sensitivity of both LCMT-1 and B α knockdown cells to the spindle-targeting drug, nocodazole, suggests that both of these proteins are important in mammalian cells for the spindle checkpoint, which ensures proper spindle formation and chromosomal attachment before progression from metaphase to anaphase."].
   The paper's own time-lapse argues the other way. A weakened spindle checkpoint
   means cells *cannot hold* a mitotic arrest; what was observed is a *prolonged*
   arrest:
   [PMID:17724024 "In our initial experiments using phase time-lapse microscopy, we found that a subset of LCMT-1 knockdown cells round up as if to enter mitosis, sometimes with a visible metaphase plate, and remain rounded for longer than expected for a normal mitosis, eventually undergoing apoptosis."]
   — i.e. an unsatisfied checkpoint downstream of a spindle/kinetochore defect,
   which is the opposite phenotype. Nocodazole hypersensitivity measured as *death*
   rather than as loss of mitotic arrest does not discriminate the two.
   Comparator check: GO:0090266 in human/mouse/yeast is carried by checkpoint
   machinery assayed directly for arrest maintenance — MAD1, MAD2L1, MAD2L1BP,
   KNL1, NDC80, SKA1, SKA3, TPR, USP44, ANAPC15, AURKB/IPL1, CDC55 (QuickGO,
   2026-10-24). Yeast PPM1 has no such annotation despite the nocodazole-sensitivity
   result in yeast that this paper cites. LCMT1 is the outlier, and it is the one
   case resting on a drug-sensitivity readout alone.
4. **Apoptosis (GO:0042981) is a readout, not a role.** Knockdown kills ~7–8% of
   cells in 24 h with caspase activation, and the killing is abolished by arresting
   cells before mitosis
   [PMID:17724024 "Strikingly, thymidine treatment caused a dramatic reduction in cell death in both LCMT-1 (L2 and L3) and B α knockdown cells ( Fig. 6 ), indicating that the increased cell death observed when cells are treated with nocodazole is specific to mitosis."].
   Death that disappears when you stop cells entering mitosis is a consequence of
   failed mitosis, not evidence that LCMT1 participates in apoptosis regulation.
5. Mouse knockout is embryonic lethal
   [PMID:17724024 "however, although 19 LCMT-1 +/+ mice and 26 LCMT-1 +/− pups were born from these +/− × +/− crosses, no LCMT-1 −/− pups were obtained from any of the crosses, indicating that loss of LCMT-1 is indeed embryonic lethal."].
   Essentiality is necessity evidence; per repo convention it does not license a
   process annotation on its own.

## Position taken in the review

| Term | Action | Why |
|---|---|---|
| GO:0018423 (all 6 rows) | ACCEPT | Core catalytic function, EXP + IBA + structure |
| GO:0003880, GO:0008757, GO:0008168 | MODIFY → GO:0018423 | Correct but general ancestors of the specific term the gene already carries |
| GO:0005515 | REMOVE | Bare protein binding, per repo policy |
| GO:0006481 | ACCEPT | Direct process counterpart of the core MF |
| GO:0006479, GO:0036211 | TOO_GENERAL | Ancestors of GO:0006481 asserted in this review |
| GO:0031333 | MODIFY → GO:0031334 | Sign error; LCMT1 promotes holoenzyme assembly |
| GO:0090266 (IMP + IBA) | REMOVE | Inference contradicted by the paper's own time-lapse; comparator genes all have direct arrest assays |
| GO:0042981 | MARK_AS_OVER_ANNOTATED | Mitosis-dependent death readout, not participation |
| GO:0000086 | MARK_AS_OVER_ANNOTATED | Reactome pathway membership; the G2/M summary does not mention LCMT1 |
| GO:0009966 | MARK_AS_OVER_ANNOTATED | ARBA rule, uninformative grouping term |
| GO:0005829 | ACCEPT · GO:0005654 | KEEP_AS_NON_CORE | Longin 2008 localization |

### Departure from the upstream issue

Issue #6632 asks for GO:0006479 and GO:0006481 to be removed as well, on the
grounds that both are "pending obsoletion". Neither term is obsolete in the
current ontology and neither carries an obsoletion-candidate subset or comment
(QuickGO term records, checked 2026-10-24); the only open go-ontology issue found
on the topic is #32270, about the "pending obsoletion" qualifier itself, not these
two terms. More to the point, `REMOVE` in this repository means the claim is
unlikely to be correct, and the claim here — that LCMT1 methylates a protein
C-terminus — is exactly right. Pending ontology housekeeping is recorded in the
review reasons rather than acted on as a removal. GO:0006479 and GO:0036211 are
marked `TOO_GENERAL` because GO:0006481 entails them.

### Ontology gap

There is no GO term for regulation of PP2A-family holoenzyme assembly;
GO:0031334 is the nearest fit and is three levels too broad for what is a
specific, conserved and well-characterized mechanism. Raised as a
`proposed_new_terms` entry.
