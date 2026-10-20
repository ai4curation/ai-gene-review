# BUB3 (mitotic checkpoint protein BUB3, UniProt O43684) — review notes

Sources used: `BUB3-uniprot.txt`, `BUB3-goa.tsv` (68 seeded rows), the Edison/falcon deep
research report (`BUB3-deep-research-falcon.md`), the cached publications for every
`original_reference_id`, and QuickGO for term definitions. Exemplars followed:
`genes/human/MAD2L1` and `genes/SCHPO/bub1`.

## What the protein is

BUB3 is a 328-aa WD40-repeat protein (UniProt lists seven WD repeats; Taylor et al. counted
four by the 1998 criteria) that forms a seven-bladed beta-propeller. It has no catalytic
activity. Everything it does it does by binding two kinds of ligand on the top face of the
propeller:

- **GLEBS motifs** of BUB1, BUB1B/BUBR1 and ZNF207/BuGZ, giving constitutive 1:1 complexes
  [PMID:24462187 "Bub1 and BubR1 both interact with Bub3 at the KT through highly conserved
  GLEBS domains"] [PMID:24462186 "Since the GLEBS in Bub1 and BubR1 mediates their direct
  binding to Bub3"].
- **MPS1-phosphorylated MELT repeats of KNL1**, which is how BUB1-BUB3 is docked at
  unattached kinetochores (Primorac et al. 2013, eLife, summarised in the deep research:
  "In a BUB1:BUB3 complex, it binds MPS1-phosphorylated MELT motifs in KNL1 at signaling
  kinetochores; this builds a platform that recruits additional SAC machinery.").

The founding human paper is Taylor, Ha & McKeon 1998. GFP-BUB3 is nuclear in interphase
[PMID:9660858 "During interphase, the GFP fluorescence was diffusely localized in the
nucleus"] and concentrates on kinetochores before alignment [PMID:9660858 "we conclude that
hBub3 localizes to kinetochores during prophase and prometaphase, but not during and after
metaphase"]. The same paper showed that the BUB3-binding region of BUB1 is the kinetochore
targeting region [PMID:9660858 "the 38-amino acid deletion that abolished the ability of
mBub1 to interact with hBub3 also abolished its ability to localize to the kinetochore.
These observations suggest that the Bub1/Bub3 interaction is required for localizing Bub1
to the kinetochore in mitosis"] and that BUBR1 reaches kinetochores only with excess BUB3
[PMID:9660858 "in prometaphase cells coexpressing hBub3 and hBubR1, localization of hBubR1
at kinetochores was observed"]. This is the direct basis of `GO:0034501 protein localization
to kinetochore` and of my choice of **GO:0140483 kinetochore adaptor activity** as the
primary molecular function.

## Two BUB3 modules

1. **BUB1-BUB3** = kinetochore targeting / signalling platform (`GO:1990298 bub1-bub3
   complex`, IBA). In vitro BUB1 and BUB3 form a 1:1 complex that binds and phosphorylates
   MAD1 [PMID:10198256 "In vitro, BUB1 and BUB3 proteins form a complex of monomers of each
   protein."]. The kinase activity belongs to BUB1; UniProt's FUNCTION text about "the
   BUB1/BUB3 complex ... phosphorylating its activator CDC20" (PMID:15525512) should not be
   read as BUB3 kinase activity. No kinase-activity row exists in GOA for BUB3.
2. **BUBR1-BUB3** = MCC effector module. The MCC purified from HeLa cells is a stoichiometric
   BUBR1-BUB3-CDC20-MAD2 complex [PMID:11535616 "This search yielded a single stable complex
   named the mitotic checkpoint complex (MCC), consisting of the proteins hBUBR1, hBUB3,
   CDC20, and MAD2"] and exists even in interphase [PMID:11535616 "Surprisingly, MCC is not
   generated from kinetochores, as it is also present and active in interphase cells"]. In
   the APC/C-MCC cryo-EM structure Bub3 is flexible and dispensable for inhibition
   [PMID:27509861 "both the structure and activity of APC/CMCC with Bub3 and the BubR1
   C-terminus deleted (APC/CminiMCC) are indistinguishable from APC/CMCC"]; likewise BUB3
   does not affect binding of the second CDC20 [PMID:25383541 "including BUB3 in the core
   rMCC made no difference to the amount of CDC20 that was bound"]. Hence BUB3's MF in the
   MCC is scaffolding (`GO:0030674`) that *contributes to* `GO:1990948 ubiquitin ligase
   inhibitor activity`, not the inhibitory activity itself.

## Kinetochore-microtubule attachment

Logarinho et al. 2008 (RNAi in HeLa; cold-stable K-fibres, interkinetochore stretch,
p150Glued/CLIP-170 occupancy, nocodazole washout): [PMID:18199686 "We found that Bub3 is
essential for the establishment of correct K-MT attachments"]; [PMID:18199686 "it appears
that Bub3 is required for efficient establishment rather than the maintenance of bipolar MT
attachment"]; [PMID:18199686 "We propose that Bub3 promotes the formation of stable end-on
bipolar attachments"]. The phenotype tracks BUB1 depletion and is synergistic with it. The
authors are explicit that the mechanism may be indirect [PMID:18199686 "We do not know
whether Bub3 is directly responsible for the K-MT attachments or if it indirectly regulates
the activity of a MT-binding protein"]. I ACCEPT the `GO:0008608` IDA: BUB3 does the work
of docking BUB1 (and hence BUBR1-PP2A-B56, Sgo1/CPC) at kinetochores, which is participation
rather than mere necessity. The mitotic child `GO:0051315` would be an acceptable refinement
but the parent is kept because BUB3 also acts at meiotic kinetochores. The same paper shows
BUB3 is needed for the SAC [PMID:18199686 "depletion of Bub3 to accelerate mitotic
progression, both under normal condition and exposure to nocodazole, indicating that Bub3 is
essential for SAC function"].

## Regulators of BUB3 abundance / localisation (partners whose *activity* is not BUB3's)

- **ZNF207/BuGZ** binds BUB3 through a GLEBS motif, stabilises it and enhances kinetochore
  loading [PMID:24462186 "BuGZ promotes chromosome alignment by directly binding to and
  stabilizing Bub3 via the GLEBS motif"] [PMID:24462187 "Here, we report that the human
  BuGZ/ZNF207 gene encodes a GLEBS domain-containing and KT binding protein that is required
  for Bub3 stability, Bub1 KT function, and chromosome alignment"].
- **WAPL** binds BUB3 (mouse oocytes, HEK293, recombinant proteins) and maintains BUB3 levels
  for the meiosis-I SAC [PMID:32284991 "We verified the interaction between Wapl and Bub3 by
  performing co-immunoprecipitation (co-IP) experiments in oocytes and human embryonic
  kidney (HEK) 293 cells"] [PMID:32284991 "Wapl controls the SAC activity by maintaining
  Bub3 protein level"].
- **DYNLT3** (dynein light chain) binds BUB3 directly and specifically [PMID:17289665 "We
  find that DYNLT3 binds to Bub3, a spindle checkpoint protein."]; GO has `GO:0045503 dynein
  light chain binding`, which I propose in place of protein binding for that row.
- **UBR5** ubiquitinates BUB3 to release the MCC from APC/C (UniProt PTM note, PMID:35217622;
  not in GOA).

## Decisions on the 30 `GO:0005515 protein binding` IPI rows

Policy (annotation-reviewer skill): MODIFY when the cited paper supports a more informative
MF/complex; otherwise REMOVE as uninformative without asserting the interaction is false.

| Partner | Papers | Action | Replacement |
|---|---|---|---|
| BUB1 (O43683) | 10198256, 15525512 | MODIFY | GO:0140483 kinetochore adaptor activity |
| BUBR1 (O60566) | 9660858 | MODIFY | GO:0140483 kinetochore adaptor activity |
| BUBR1 (O60566) | 19407811, 22000412, 25383541 | MODIFY | GO:0030674 adaptor + GO:0033597 MCC |
| DYNLT3 (Q5XI90) | 17289665 | MODIFY | GO:0045503 dynein light chain binding |
| BuGZ/ZNF207 (O43670) | 24462186, 24462187 | REMOVE | activity is BuGZ's; BUB3 is the client |
| WAPL (Q7Z5K2) | 32284991 | REMOVE | activity is Wapl's; no BUB3 MF term |
| APC (P25054), UXT (Q9UBK9), SspH2 (A0A0H3NF38), ATXN1 (P54253) | 11283619, 12762840, 21566117, 25959826, 32814053 | REMOVE | uncharacterised / ambiguous hits |
| HTP screens (BUB1, BUBR1, ZNF207, PSTPIP1) | 21988832, 22365833, 25416956, 25852190, 26496610, 32707033, 33961781, 35271311 | REMOVE | redundant with complex annotations |

For the SspH2 row the authors themselves flag the co-IP as ambiguous [PMID:21566117 "An
interaction between SspH2 and Bub3 was also confirmed by reciprocal co-immunoprecipitation;
however, these data were more ambiguous, as a fraction of cellular Bub3 was precipitated
nonspecifically"].

## The ubiquitin-binding IBA (GO:0043130)

Source node PTN000103837 (Bub3/Rae1 WD40 ancestor); the only descendant evidence is yeast
Bub3 IDA from Pashkova et al. 2010 (PMID:21070969, not cached; abstract fetched from
PubMed: "We further demonstrate that WD40 beta-propellers from a functionally diverse set
of proteins bind ubiquitin in a similar fashion"). No human BUB3 ubiquitin-binding data
exist and no checkpoint role is known. I keep it as NON_CORE (phylogenetically defensible
structural property, not a core function) rather than removing it — the argument against
it would have to be target-specific loss, which I cannot make.

## Reactome `cytosol` TAS rows (24)

All ACCEPTED: the MCC is a soluble cytosolic inhibitor and BUB3 is diffuse in the mitotic
cell after alignment. I distinguish in the summaries the nine reactions where BUB3 is a real
participant (MCC formation, MCC-APC/C binding, MCC-dependent cyclin A / NEK2A handling) from
the fifteen where BUB3 enters only as part of Reactome's composite kinetochore entity
(cohesin phosphorylation, separase cleavage, DIAPH2/formin, EML4-NUDC, etc.); those rows
support the location only, not a role in the reaction.

## Core functions written

1. `GO:0140483 kinetochore adaptor activity` — BUB1-BUB3 complex, kinetochore; involved in
   protein localization to kinetochore, mitotic SAC signalling, attachment of spindle
   microtubules to kinetochore.
2. `GO:0030674 protein-macromolecule adaptor activity`, contributes to `GO:1990948
   ubiquitin ligase inhibitor activity` — mitotic checkpoint complex, cytosol; involved in
   mitotic SAC signalling.

No `NEW` annotations proposed: BUB3's process coverage (SAC signalling, protein localization
to kinetochore, K-MT attachment) and complex coverage (bub1-bub3, MCC) already exist in GOA,
and the adaptor MF terms enter through `MODIFY` of the protein-binding rows.

## Open points

- Partitioning of BUB3 between BUB1 and BUBR1 complexes, and whether the pools exchange.
- Whether human BUB3 binds ubiquitin and whether that competes with GLEBS/phospho-MELT
  binding (would settle the IBA).
- Whether DYNLT3 binding underlies dynein stripping of BUB1/BUB3 from attached kinetochores.
- History record (`just new-history`) was not created because this task was scoped to
  `genes/human/BUB3/` only; it should be added when the PR is assembled.
