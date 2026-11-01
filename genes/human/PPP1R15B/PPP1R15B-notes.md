# PPP1R15B (CReP) — curation notes

UniProt: Q5SWA1 (PR15B_HUMAN), 713 aa, chromosome 1. HGNC:14951. Gene also known as
**CReP** ("constitutive repressor of eIF2alpha phosphorylation").

Deep research note: `just deep-research human PPP1R15B --provider perplexity` failed in
this environment (`ERROR - Provider 'perplexity' not available. Available: claude_code`),
so no `-deep-research-*.md` file exists. These notes are the hand-written substitute, as
CLAUDE.md requires; nothing here is named as provider deep research.

## 1. What the protein is

PPP1R15B is one of the two **non-catalytic (regulatory) subunits of the mammalian
eIF2alpha holophosphatase**; the other is PPP1R15A/GADD34. Neither is catalytic. The
catalytic subunit is PP1 (PPP1CA/PPP1CB/PPP1CC).

[PMID:34847777 "In mammals, the phosphorylation levels of eIF2α are tuned to cellular
needs through the antagonistic actions of four different eIF2α kinases, PKR, HRI, PERK and
GCN2 and two eIF2α phosphatases"]

[PMID:34847777 "The latter are composed of the catalytic subunit PP1 bound to one of two
related non-catalytic subunits PPP1R15A"]

The division of labour between the two R15 paralogues is the key point for scoping GO
terms:

[PMID:26159176 "the constitutive repressor of eIF2α phosphorylation (CReP), encoded by
PPP1R15B, acts under basal conditions (8), while GADD34, encoded by PPP1R15A, is activated
by eIF2α phosphorylation and feeds back negatively on PERK signaling to promote the
recovery of protein synthesis as the stress response wanes (9)"]

UniProt states the function in the same terms
[file:human/PPP1R15B/PPP1R15B-uniprot.txt "Maintains low levels of EIF2S1 phosphorylation
in unstressed cells by promoting its dephosphorylation by PP1."].

Family: PPP1R15 (PANTHER PTHR16489, subfamily SF11; Pfam PF10472 `CReP_N` +
PF10488 `PP1c_bdg`)
[file:human/PPP1R15B/PPP1R15B-uniprot.txt "Belongs to the PPP1R15 family."].

## 2. Molecular architecture — a two-module adaptor

Hodgson et al. mapped the modules in cells with FLAG-tagged truncations:

[PMID:34847777 "R15B340–639 binds eIF2α while the carboxy-terminal region R15B639–713
binds PP1"]

[PMID:34847777 "Similarly, full-length R15B1–713 as well as R15B340–713 were highly
active"] — i.e. activity requires **both** modules; either alone is inactive (the middle
module alone becomes a phospho-substrate trap and *raises* P-eIF2alpha).

The mechanistic conclusion is explicitly an enzyme–substrate adaptor statement:

[PMID:34847777 "PP1 can dephosphorylate eIF2α but its activity is enhanced by the middle
region of R15 which serves as a selective substrate receptor"]

Fatalska et al. then showed what the middle module grips, using HDX-MS, NMR and
AlphaFold2 with purified trimeric eIF2:

[PMID:38159565 "we integrated diverse approaches to elucidate how the PP1 non-catalytic
subunit PPP1R15B (R15B) captures its full trimeric eIF2 substrate"]

[PMID:38159565 "H1 and H2 form a clamp that grasps the substrate in a region remote from
the phosphorylated residue"]

[PMID:38159565 "Unexpectedly, binding of R15B to eIF2 protected residues 294–309 and
405–436 at C-terminal end of eIF2γ"]

[PMID:38159565 "H1 of R15B binds at the interface between the G-domain and DIII of eIF2γ"]

So the substrate is the **eIF2 trimer** (contacts on eIF2gamma and the eIF2alpha CTD), not
an isolated eIF2alpha peptide — `GO:0071074 eukaryotic initiation factor eIF2 binding` is
the right MF, not an eIF2alpha-subunit binding term.

Actin is **not** required for substrate recruitment, despite an earlier model:
[PMID:34847777 "the middle region of R15, which lacks the canonical actin-binding motif
described in the carboxy-terminal regions of R15s, binds eIF2 in absence of actin"].
Useful caveat: PMID:26159176 still describes G-actin as an "essential cofactor"; the 2021
cell-based work post-dates and corrects that framing.

PP1 affinity differs between the paralogues
[PMID:34847777 "the affinity of PP1 is approximately 10-fold higher for R15A than R15B"].

## 3. Two disease variants dissect the two modules

This is the cleanest genetic evidence that the adaptor has two separable jobs.

**R658C** (MSSGM2, MIM:616817; two independent families) hits the C-terminal PP1-binding
module:

[PMID:26159176 "The R658C mutation decreases PP1 binding and eIF2α dephosphorylation and
results in β-cell apoptosis."]

[PMID:26159176 "It is located in the conserved COOH-terminal functional core of PPP1R15B
that specifies interaction with PP1"]

[PMID:26307080 "We found that PPP1R15B–PPP1C binding was virtually abolished in patient
cells, indicating that the p.R658C protein change significantly influences this
interaction"]

[PMID:26307080 "patient cells have greatly diminished levels of PPP1R15B-PPP1C
interaction, which results in increased eIF2α phosphorylation and resistance to cellular
stress"]

**N423D** hits the substrate-recruitment module:

[PMID:38159565 "both H1A and N423D mutants captured significantly less eIF2α than the WT
R15B411–613 fragment or full-length protein"]

[PMID:38159565 "Both N423D and H1A mutants captured PP1 at levels comparable with the WT
R15B"]

[PMID:38159565 "The N423D variant has no effect on PP1 binding but decreases substrate
recruitment and dephosphorylating activity, whereas the R658C reduces dephosphorylation by
decreasing PP1 binding."]

Same clinical syndrome, two different broken modules — a textbook separation-of-function
pair.

## 4. Loss of function: what it does to the cell

[PMID:26159176 "basal eIF2α phosphorylation was increased in PPP1R15B-deficient INS-1E
cells"]

[PMID:26159176 "Thus, PPP1R15B silencing increases eIF2α phosphorylation and induces
downstream ATF3 protein expression."]

[PMID:26159176 "PPP1R15B deficiency induces apoptosis through the proapoptotic BH3-only
proteins DP5, PUMA, and Bim"] — downstream consequence of chronic ISR activation in
beta-cells, not a PPP1R15B activity; it should not become an apoptosis annotation.

Although "constitutive", R15B is itself stress-regulated in beta-cells:
[PMID:26159176 "PPP1R15B was induced by different synthetic ER stressors and the saturated
FFA palmitate"] (PERK-dependent in that study). This is what keeps `GO:0034976 response to
endoplasmic reticulum stress` defensible for R15B as well as R15A.

## 5. Pharmacology

[file:human/PPP1R15B/PPP1R15B-uniprot.txt "The phosphatase activity of the PPP1R15B-PP1
complex toward EIF2S1 is specifically inhibited by Salubrinal, a drug that protects cells
from endoplasmic reticulum stress."] Salubrinal was found as an inhibitor of eIF2alpha
dephosphorylation [PMID:15705855 "we identified salubrinal, a selective inhibitor of
cellular complexes that dephosphorylate eukaryotic translation initiation factor 2 subunit
alpha (eIF2alpha)"]. Raphin1 is the R15B-selective inhibitor reported by the same group.

## 6. Localization — what the evidence actually says

GOA carries `GO:0005783 endoplasmic reticulum` only as `is_active_in` **IBA**
(GO_REF:0000033), seeded from `FB:FBgn0034948` and `UniProtKB:O75807` (R15A). R15A's ER
localization is directly annotated (IDA) and its N-terminal region is the ER-targeting
determinant; the Bertolotti group states the family generalization
[PMID:34847777 "full-length proteins, which localize to the endoplasmic reticulum"].

For human R15B itself the only localization experiment in the cached literature is
non-committal: [PMID:26307080 "Immunofluorescence staining demonstrated that PPP1R15B was
localized throughout the cell as punctate foci in both control and patient cells."] —
punctate foci, no ER marker co-stain.

Conclusion for the review: keep the ER row (the organelle claim is family-level sound and
ER is a root organelle term, so per `projects/ORGANELLES.md` it is never `TOO_GENERAL` and
is never to be `MODIFY`-ed to a sub-compartment), but treat it as non-core — the
dephosphorylation reaction acts on cytosolic eIF2, and there is no second independent line
for R15B that would justify adding an ER-membrane sub-compartment term as `NEW`.

## 7. GO-CAM

`gocams/index.tsv` already places PPP1R15B in model `61e0e55600000407` ("SP_GADD34-
PPP1CA"), typed `GO:0060090 molecular adaptor activity`, with
`RO:0002629 directly_positively_regulates` onto the PPP1CA `GO:0016791 phosphatase
activity` activity, which in turn regulates the EIF2S1 activity node. PPP1R15A is modelled
identically. The model's adaptor framing is right; the review only refines the term to the
adaptor subclass GO has since created (`GO:0140767 enzyme-substrate adaptor activity`),
which keeps the curators' intent and the model's causal edge intact.

## 8. Ontology gap

`GO:0140467 integrated stress response signaling` has four branch children (PERK, GCN2,
HRI, PKR) but **regulation children exist only for the PERK branch** (`GO:1903897/8/9`).
R15B acts at the shared node — phospho-eIF2alpha — downstream of all four kinases
[PMID:34847777 "In mammals, the phosphorylation levels of eIF2α are tuned to cellular
needs through the antagonistic actions of four different eIF2α kinases, PKR, HRI, PERK and
GCN2 and two eIF2α phosphatases"], so the only term available
(`GO:1903898 negative regulation of PERK-mediated unfolded protein response`, held by TAS
from an IRE1alpha review) names one branch out of four. The review proposes
"negative regulation of integrated stress response signaling" under `GO:0140467` and uses
it as the MODIFY replacement.

Note `GO:0036497 eIF2alpha dephosphorylation in response to endoplasmic reticulum stress`
exists but has **zero annotations** in QuickGO (checked 2026-10-31) and is ER-stress
scoped, so it was not used.

## 9. Comparator check (PPP1R15A/GADD34, O75807)

Run against QuickGO to see what GO curators give the sibling subunit in the same role:
`GO:0000164` (IBA/IDA/IPI), `GO:0008157` (IDA/IPI), `GO:0019888` (IBA/IDA/IEP/ISS),
`GO:0060090` (IDA), `GO:0071074` (IPI), `GO:0072542` (IDA), `GO:0006446` (IDA),
`GO:0032058` (IDA), `GO:0036490` (IDA), `GO:0043558` (IDA/ISS), `GO:0034976` (IBA/IDA),
`GO:1903898` (TAS), `GO:0051246` (IEA). Notably **not** `GO:0006470 protein
dephosphorylation` and **not** `GO:0036497`.

Two conclusions drawn from this:

- The convention for an R15 subunit is the regulator/adaptor framing, not the
  `protein dephosphorylation` BP. So no `GO:0006470` was proposed for R15B.
- `GO:0006446 regulation of translational initiation` is what R15A carries by IDA for the
  translational output of the same reaction. R15B's own data support the same claim
  (silencing raises P-eIF2alpha and induces ATF3; patient cells have elevated P-eIF2alpha),
  so it is listed as a replacement term for the uselessly broad ARBA row
  `GO:0051246 regulation of protein metabolic process` rather than as a free-standing
  proposal.

## 10. Evidence-code defect noticed

GOA row `GO:0019888 / IEP / PMID:34847777` (assigned_by DisProt). PMID:34847777 contains
no expression-pattern experiment; it is overexpression, co-immunoprecipitation and
in-cell dephosphorylation activity assays in HEK293T. The claim is right, the code is
not — recorded as a `source_defects` entry (`WRONG_EVIDENCE_CODE`, IEP → IMP).
