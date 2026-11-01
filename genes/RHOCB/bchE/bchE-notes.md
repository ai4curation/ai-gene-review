# bchE (P26168, *Rhodobacter capsulatus* SB1003) — curation notes

**Provenance note.** No deep-research API keys exist in this container, so
`just deep-research` was not run and no `-deep-research-<provider>.md` file
exists for this gene. All literature below was read directly: the cached
`publications/PMID_*.md` files, PubMed E-utilities, and WebSearch. GONUTS
(gowiki.tamu.edu), the CACAO source wiki, was re-checked on 2026-11-01 and is
now **permanently retired**: `https://gowiki.tamu.edu/wiki/index.php/Main_Page`
returns HTTP 410 and the server serves a notice titled "GONUTS has been
retired" ("The GO wiki that was at gowiki.tamu.edu is no longer online."). The
archived copy at web.archive.org is blocked by this container's egress policy.
Search-engine snippets of the archived `RHOCB:BCHE` page were visible and are
noted below as third-hand context only, never cited as evidence.

## What the gene is

P26168 / RCAP_rcc00669 is the anaerobic (oxygen-independent)
Mg-protoporphyrin IX monomethyl ester (MPE) cyclase, BchE: the enzyme that
installs the C13^1 oxo group and closes the isocyclic fifth (E) ring, taking
MPE to 3,8-divinyl protochlorophyllide a in bacteriochlorophyll *a*
biosynthesis.

The chemistry is a cobalamin-dependent radical-SAM six-electron oxidation that
takes its oxygen from water, EC 1.21.98.3 / RHEA:49096
[file:RHOCB/bchE/bchE-uniprot.txt "Catalyzes the anaerobic formation of the
isocyclic ring (E-ring) in Mg-protoporphyrin monomethyl ester (MPE) to yield
protochlorophyllide a (PChlide a) via a six-electron oxidation and the
formation of an oxo group at position C13 using oxygen from a water molecule"].

**This is the step where misassignment has historically happened.** The same
overall conversion is performed in oxygenic and aerobic organisms by the
structurally and mechanistically unrelated di-iron oxygenase AcsF/CHL27/XanL,
EC 1.14.13.81, which consumes O2 and NADPH. GO has a term for the *aerobic*
reaction only — GO:0048529 "magnesium-protoporphyrin IX monomethyl ester
(oxidative) cyclase activity", whose definition is "Catalysis of the reaction:
magnesium protoporphyrin IX 13-monomethyl ester + 3 NADPH + 3 H+ + 3 O2 =
divinylprotochlorophyllide + 3 NADP+ + 5 H2O" with xrefs EC:1.14.13.81 and
RHEA:33235, and which is_a GO:0016709 (incorporation of molecular oxygen).
There is **no** GO term for EC 1.21.98.3 / RHEA:49096: QuickGO ontology search
for "1.21.98.3", "RHEA:49096" and "anaerobic magnesium-protoporphyrin" returns
nothing matching. Nonetheless GO:0048529 is propagated by IEA to *bchE*
orthologs (e.g. UniProtKB:A0A087S6L6 bchE, GO:0048529 IEA GO_REF:0000003),
which is the misassignment the project flagged. **P26168 itself does not carry
GO:0048529**, so this review has nothing to retract on that score; instead the
gap shows up as a bare `GO:0003824 catalytic activity` row, and this review
proposes the missing term.

*R. capsulatus* has no AcsF at all, which is why BchE is the sole route to
PChlide in this organism [PMID:42748141 "R. capsulatus does not utilize AcsF,
so all production of PChlide must originate through the action of BchE"].

## Evidence that bchE is the MPE cyclase in *R. capsulatus*

- Yang & Bauer 1990 disrupted three PGC reading frames; F1025 (later named
  bchE) blocked the MPE → PChlide step [PMID:2203738 "Three open reading
  frames in the Rhodobacter capsulatus photosynthesis gene cluster, designated
  F0, F108, and F1025, were disrupted by site-directed mutagenesis. Mutants
  bearing insertions in these reading frames were defective in converting
  protoporphyrin IX to magnesium-protoporphyrin monomethyl ester,
  protochlorophyllide to chlorophyllide a, and magnesium-protoporphyrin
  monomethyl ester to protochlorophyllide, respectively."]. The abstract names
  the ORF, not the gene symbol; the identification of that lesion as *bchE* is
  stated independently by Gough et al. [PMID:10841582 "MPE accumulates in
  transposon mutants of the Rhodobacter capsulatus bchE gene, suggesting that
  the encoded protein is required for MPE-cyclase activity"].
- Bollivar et al. 1994 (the CACAO reference) is a **cluster-wide** directed
  mutational analysis: "we have undertaken a systematic directed mutational
  analysis of 12 open reading frames in the photosynthesis gene cluster to
  evaluate whether individual open reading frames have a role in photopigment
  biosynthesis", with "mutations constructed in seven open reading frames
  resulted in a loss of bacteriochlorophyll biosynthesis, concomitant with the
  accumulation of specific intermediates in the Mg-tetrapyrrole biosynthetic
  pathway" [PMID:8158642]. Cached abstract only (`full_text_available: false`).
- Gough et al. 2000 showed the cyclase reaction itself has an absolute
  cobalamin requirement, using B12-auxotroph *bluE*/*bluB* mutants and an in
  vivo assay [PMID:10841582 "Fig. 5 C shows that mutant MPE cyclase activity
  has an absolute demand for exogenous B 12 or AdCob. This experiment shows
  that a cobalamin cofactor acts directly on the cyclase reaction."]. Note
  this paper worked in *R. capsulatus* **37b4** ("Cell growth of capsule-less
  wild-type R. capsulatus 37b4"), not SB1003, and it never touched purified
  BchE protein. Its [4Fe-4S] statement is explicitly a proposal: "This
  cysteine arrangement resembles somewhat an iron–sulfur center as found in
  biotin synthase ( 31 )". UniProt's cofactor and BINDING lines for the
  cluster are correspondingly `ECO:0000305` (curator inference), while the
  adenosylcobalamin cofactor is `ECO:0000269`.
- Wiesselmann et al. 2020 is the strongest gene-specific work: an in vitro
  assay on *R. capsulatus* BchE validated by H2^18O label transfer onto the
  C13^1-oxo group, plus 24 site-directed mutants scored by in vivo
  complementation, which identified "Potential ligands of the [4Fe-4S] cluster
  (Cys204, Cys208, Cys211), of SAM (Phe210, Glu308 and Lys320) and of the
  proposed cobalamin cofactor (Asp248, Glu249, Leu29, Thr71, Val97)"
  [PMID:33211085]. Those three cysteines are exactly UniProt's BINDING
  positions, and in the P26168 sequence they are the canonical radical-SAM
  CxxxCxxC motif (residues 195-215 read `VAIPNMARGCPFTCSFCSQWK`, i.e.
  C204-x3-C208-x2-C211). Abstract-only in the cache.
- York, Zhang & Booker 2026 achieved the first purification and in vitro
  reconstitution, confirming both cofactors spectroscopically: "The enzyme was
  purified anaerobically and characterized by UV–Vis and electron paramagnetic
  resonance spectroscopy to confirm the presence of Cbl and a [Fe4S4]
  cluster." **This was not the *R. capsulatus* protein**: "The enzyme, BchE,
  from Rubrivivax pictus was heterologously expressed in either Escherichia
  coli BL21(DE3) or a modified ΔbtuR knockout strain of BL21(DE3)", after "we
  attempted heterologous expression and purification of BchE homologs from
  eight different organisms; only three yielded any soluble protein, and of
  these, only BchE from Rubrivivax pictum catalyzed the formation of PChlide"
  [PMID:42748141]. So for P26168 the cofactor identities are ortholog evidence
  plus the gene's own conserved motif and mutagenesis, not direct
  spectroscopy. The same paper does contain *R. capsulatus* whole-cell work
  replicating Gough.

## Localization

The TreeGrafter `GO:0005829 cytosol` row is the weakest annotation on this
entry. P26168 has no transmembrane segment and no signal peptide in UniProt,
so a cytosol default is the expected machine output — but direct subcellular
fractionation of *R. capsulatus* says otherwise: "Subcellular fractionation
experiments revealed that membrane-localized BchE requires an additional,
heat-sensitive cytosolic component for activity" [PMID:33211085]. The protein
is also notoriously insoluble when expressed recombinantly [PMID:42748141 "the
inability to obtain soluble, catalytically active enzyme"]. The honest reading
is that BchE is membrane-associated in its native host and partners with a
small (3-10 kDa) soluble component; asserting `cytosol` as the location
overstates what is known, and asserting a membrane term would overstate it in
the other direction from an abstract alone. Flagged as a knowledge gap and a
suggested experiment.

## CACAO row and the cross-isolate hypothesis (screen 2)

The predicted failure shape was: PMID:8158642 is cited by CACAO rows under two
different NCBI taxon ids that both mean *R. capsulatus*, suggesting a result
from one isolate was annotated onto a protein filed under a sibling taxon id
without re-grounding.

QuickGO (`reference=PMID:8158642`, 2026-11-01) returns exactly four
annotations, all CACAO, all `GO:0030494` IMP `involved_in`:

| gene product | symbol | taxon |
|---|---|---|
| UniProtKB:P26165 | bchF | 272942 |
| UniProtKB:P26168 | bchE | 272942 |
| UniProtKB:P26169 | bchJ | 272942 |
| UniProtKB:P26236 | bchM | 1061 |

The two-taxon-id signature is real but it is **not on bchE**. The 1061 row is
bchM, P26236, whose UniProt entry is the older species-level record
`BCHM_RHOCA` (`OS Rhodobacter capsulatus (Rhodopseudomonas capsulata).`,
`OX NCBI_TaxID=1061;`), dating from the 1984 Youvan sequencing paper. bchE,
bchF and bchJ are all on the modern strain-level SB1003 entries (272942). The
split therefore reflects the age and scope of the UniProt entries the students
annotated, not a transfer across isolates — and in any case a strain-level id
within one species would not by itself be a defect.

The neighbour-mis-attribution alternative is also absent. Bollivar et al. 1994
is a cluster-wide analysis of 12 PGC reading frames, so three adjacent genes
(bchF, bchE, bchJ) citing one reference is exactly what that paper supports;
it is not a sign that one gene's result was spread across its neighbours. The
gene's lesion is independently corroborated: *bchE* mutants accumulate MPE,
reported both by Yang & Bauer and restated by Gough. (Search-engine snippets
of the archived GONUTS `RHOCB:BCHE` page describe a table entry for a *bchE*
mutant strain with a 590 nm peak attributed to MPE accumulation — consistent
with the *bchE* transposon strain DB575 that Gough et al. used — but the page
itself is unreachable, so this is context, not evidence.)

**Verdict: the predicted cross-isolate transfer shape is ABSENT for bchE.**
What the screen actually detected is a *taxon-id heterogeneity across one
reference's annotation set*, driven by UniProt entry vintage. That is worth
adding to the taxonomy as a distinct, benign pattern, because it will keep
firing on any multi-gene pathway paper annotated across a mixture of
species-level and strain-level entries.

## Term-level conclusions

- `GO:0003824 catalytic activity` (IEA, InterPro rSAM signatures) — true but
  root-level, and it is standing in for a term GO does not have. MODIFY to a
  proposed new term for EC 1.21.98.3.
- `GO:0030494 bacteriochlorophyll biosynthetic process` (IMP, CACAO) — the
  claim is right and the paper supports it; the entry already carries the more
  specific `GO:0036070`, of which GO:0030494 is an ancestor (QuickGO
  ancestors of GO:0036070 include GO:0030494). MODIFY to GO:0036070.
- `GO:0031419 cobalamin binding` and `GO:0051536 iron-sulfur cluster binding`
  (IEA, InterPro B12-binding and rSAM domains) — both independently supported
  beyond family membership: residue-level mutagenesis on this protein
  [PMID:33211085], in vivo cofactor dependence in this species [PMID:10841582]
  and spectroscopy on a purified ortholog [PMID:42748141]. ACCEPT.
- `GO:0046872 metal ion binding` (IEA, InterPro cobalamin-binding domain) —
  this is the one chemistry claim that is inferred from family membership
  alone and is not entailed by the specific terms. QuickGO ancestors of
  GO:0051536 are GO:0051540 (metal cluster binding), GO:0036094, GO:0005488 —
  **not** GO:0046872; ancestors of GO:0031419 are GO:0046906 (tetrapyrrole
  binding), GO:0019842 (vitamin binding), GO:0036094, GO:0005488 — again not
  GO:0046872. GO deliberately files both cofactors away from "metal ion
  binding", because the cobalt is held inside the corrin ring and the irons
  inside a cluster; neither is a discrete metal ion site. No free metal ion
  site is reported for BchE. MARK_AS_OVER_ANNOTATED (not REMOVE: cobalt and
  iron are genuinely present, so the term is not flatly false).
- `GO:0005829 cytosol` (IEA, TreeGrafter PTN000228879) —
  MARK_AS_OVER_ANNOTATED, see Localization above.
