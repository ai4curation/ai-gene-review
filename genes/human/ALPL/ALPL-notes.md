# ALPL (human) — review notes

UniProt: P05186 · HGNC:438 · TNAP / TNSALP / AP-TNAP · EC 3.1.3.1 (and EC 3.9.1.1 by
similarity to mouse P09242).

## What the protein is

GPI-anchored (Ser501, `LIPID 501 /note="GPI-anchor amidated serine"` in the UniProt
record), N-glycosylated, obligate-homodimeric alkaline phosphomonoesterase on the outer
leaflet of the plasma membrane. Belongs to the alkaline phosphatase family (IPR001952,
PF00245).

Ecto-orientation was settled experimentally in human fibroblasts by three independent
arguments [PMID:2220817, "Normal fibroblast ALP is linked to the outside of the plasma
membrane, since in intact cell monolayers (1) dephosphorylation rates of the
membrane-impermeable substrates PEA and PLP in the medium at physiologic pH were similar
to those observed with disrupted cell monolayers, (2) brief exposure to acidic medium
resulted in greater than 90% inactivation of the total ALP activity, and (3) digestion
with phosphatidylinositol-specific phospholipase C (PI-PLC) released about 80% of the ALP
activity."]. This is the fact that GOA does not record — every location row says "plasma
membrane" and none says which face — hence the proposed GO:0009897 annotation.

Metal centre: two Zn(2+) plus one Mg(2+) in the catalytic site, and a separate
mammalian-specific structural Ca(2+) site. Now directly observed in human TNAP structures
[PMID:41145834, "The same divalent cations were identified, including the three essential
cations in the catalytic site (two zinc ions and one magnesium ion), along with a calcium
ion at the CA cluster, as seen in the apo structure of the enzyme (PDB codes 7YIV or
7YIW)."]. GOA has calcium ion binding but no zinc or magnesium term — a clear gap, hence
two more proposed NEW rows.

The calcium site is structural, not catalytic; the UniProt DOMAIN comment says
"Calcium-binding is structural and does not influence the [activity]". That is why the
existing GO:0005509 IDA is marked KEEP_AS_NON_CORE rather than ACCEPT.

Dimerisation is a functional requirement, not incidental oligomerisation. N417S is
glycosylated and surface-delivered yet monomeric and dead [PMID:23688511, "Importantly,
this mutant failed to assemble into a dimer structure, which is needed for the catalytic
function of TNSALP, as evidenced by newly developed SDS-PAGE as well as
sucrose-density-gradient centrifugation."], and P108L behaves the same way independently
[PMID:25982064, "Importantly, TNSALP (WT) largely formed a functional dimeric structure,
while TNSALP (P108L) was found to be present as a monomer in the cell."]. This is what
makes dominant hypophosphatasia possible, e.g. G82R [PMID:33821301, "TNSALP with the novel
ALPL mutation (c.244G > A p.Gly82Arg) completely lost its enzymatic activity and suppressed
that of wild-type TNSALP, corroborating its dominant negative effect."]. Normally I would
avoid a protein-binding term, but GO:0042803 here is the only annotation that explains the
dominant inheritance, so it was added.

## Substrate hierarchy

Broad specificity, but the physiologically important substrates are few, and the mutant
panel in PMID:12162492 shows the branches are genetically separable — some alleles keep
PPiase and lose PLPase activity ["Three mutations ( E174G, E174K, and E281K) were found to
retain normal or slightly subnormal catalytic efficiency toward pNPP and PPi but not
against PLP."], which maps onto the skeletal versus seizure arms of the disease.

- **PPi** — core. Removing the hydroxyapatite-propagation inhibitor is the reaction that
  explains hypophosphatasia. In matrix vesicles TNAP is the responsible enzyme
  [PMID:19874193, "We conclude that TNAP is the enzyme that hydrolyzes both ATP and PP(i)
  in the MV compartment."].
- **PLP** — core. Gates cellular vitamin B6 uptake; basis of B6-responsive seizures.
- **Phosphoethanolamine / phosphocholine** — promoted to core on the strength of the 2025
  paper [PMID:41145834, "Recombinant TNAP hydrolyzes phosphocholine and phosphoethanolamine
  with similar efficiency than PPi."] plus its physiological readout ["In summary, TNAP is
  the phosphatase enabling cellular choline uptake during fasting, participating in hepatic
  lipid metabolism."]. PEA has been known as a TNAP substrate since 1990 and is a
  diagnostic marker; what is new is the choline/VLDL link and the kinetic parity with PPi.
- **ATP / ADP / AMP** — real but ancillary; shared with ENPP/CD39/CD73. Kept non-core.
- **N-phosphocreatine** — mouse only (futile creatine cycle in thermogenic fat). Kept
  non-core across all five related rows (GO:0005758, GO:0031966, GO:0050187, GO:0140651,
  GO:0120162), since every human annotation for these is ISS or IEA from mouse P09242.

## The one REMOVE: GO:0140928

`GO:0140928 inhibition of non-skeletal tissue mineralization` (IEA, GO_REF:0000107,
involved_in) is directionally inverted. Tracing the propagation: the human IEA comes from
Ensembl Compara transfer; the seed is a mouse Alpl IDA from PMID:21490328. I pulled that
abstract — it says "Overexpression of TNAP increased calcification of cultured aortas" and
"Hydrolysis of PP(i) was reduced 25% by β,γ-methylene-ATP and 50% by inhibition of TNAP".
So TNAP promotes ectopic calcification by destroying PPi; the paper's *inhibitory* arm is
about NPP1 and ANK, which appear on the same term legitimately.

Independent human-relevant confirmation of the direction [PMID:28592560, "A selective and
orally bioavailable TNAP inhibitor prevented calcification in ABCC6 mutant cells in vitro
and attenuated both the development and progression of calcification in Abcc6-/- mice in
vivo, without the deleterious effects on bone associated with other proposed treatment
strategies."]. An inhibitor that blocks the process cannot be blocking a protein that
performs it.

Checked GO for a term in the opposite direction — searched "mineralization" via QuickGO;
there is no "promotion of non-skeletal tissue mineralization" and no ectopic-calcification
term other than GO:0140928 itself. Hence a `proposed_new_terms` entry rather than a MODIFY.

## Other non-obvious calls

- **GO:0001649 osteoblast differentiation (HDA, PMID:16210410)** →
  MARK_AS_OVER_ANNOTATED. The paper measures a 27-fold rise in ALP abundance during
  induced differentiation. That makes ALPL a differentiation marker; it does not show
  participation. In Alpl-null models osteoblasts differentiate and deposit osteoid — what
  fails is mineralisation of it.
- **GO:0016462 pyrophosphatase activity** (three rows) → MODIFY to GO:0004427. Confirmed
  via QuickGO that GO:0004427 is a descendant of GO:0016462. The experiments measured
  inorganic PPi specifically, and the broad parent also covers nucleoside triphosphatases,
  which is a different physiological story.
- **GO:0001501 skeletal system development (TAS)** → MODIFY to GO:0030282. HPP is a
  mineralisation disorder, not a patterning disorder.
- **GO:0016791 phosphatase activity** (InterPro2GO) and **GO:0016020 membrane** (HDA) →
  MODIFY to the specific terms both are parents of.
- **GO:0071529 cementum mineralization** → ACCEPT, not non-core. Premature loss of primary
  teeth is a major HPP diagnostic criterion and acellular cementum is the tissue that
  fails, so this specific term has direct human clinical support.
- **GO:0065010 extracellular membrane-bounded organelle, is_active_in** → ACCEPT. This is
  the matrix vesicle, a genuine second site of action, distinct from the two GO:0070062
  extracellular-exosome rows which are untargeted proteomic inventory hits and were kept
  non-core.
- **GO:0016887 ATP hydrolysis activity** → KEEP_AS_NON_CORE rather than REMOVE. TNAP does
  hydrolyse ATP, but the term normally connotes energy-coupled ATPases; flagging non-core
  records the chemistry without implying TNAP is an ATPase.
- The six `response to X` rows (LPS, insulin, vitamin B6, M-CSF, glucocorticoid, sodium
  phosphate) all describe regulation *of* ALPL, not function *of* ALPL. Kept non-core;
  none has evidence against it.

## The other three isozymes

ALPI, ALPP and ALPG were reviewed in the same pass; see their own notes files. Decisions
taken consistently across all four:

- `GO:0016791 phosphatase activity` (InterPro2GO) → MODIFY to `GO:0004035` in every gene.
  The signature that generates it is the alkaline phosphatase domain itself, so the parent
  term throws away what the signature actually says.
- `GO:0009897 external side of plasma membrane` proposed as NEW in all four. Every gene has
  plasma-membrane rows and none records which face, although ecto-orientation is what makes
  these enzymes act on extracellular substrates. Evidence differs per gene: PMID:2220817
  (ALPL, PI-PLC + membrane-impermeable substrates), PMID:29567797 (ALPI, flow cytometry of
  a GPI-signal truncation), PMID:2153284 (ALPP, the saturation mutagenesis that worked out
  GPI attachment at Asp-484), PMID:2162249 (ALPG, PI-PLC release of the Nagao isozyme).
- `GO:0042803 protein homodimerization activity` proposed as NEW in all four. Normally a
  binding term would not earn a place, but the dimer is functionally load-bearing family-wide:
  ALPL monomeric mutants are dead and dominant-negative, the ALPP structure credits the
  interface with mammalian-specific allostery, and ALPI disease alleles act partly by
  impairing dimerization.
- Metal terms: ALPL was missing zinc and magnesium; ALPP and ALPI have them but not calcium;
  ALPG had no metal term at all. Proposed the missing ones in each, with IDA where a human
  structure resolves the metal (ALPL, ALPP) and ISS where it was resolved in a paralogue
  (ALPG).
- Interactome-derived `GO:0005515 protein binding` rows on ALPI and ALPP →
  MARK_AS_OVER_ANNOTATED. All are binary Y2H maps and the partner lists are dominated by
  keratin-associated proteins.

The contrast in what can be *asserted* is the main finding of doing all four together. ALPL
supports three core functions with named substrates and processes. ALPI supports one, with
LPS and TLR4 attached, on Mendelian evidence GOA has not yet cited. ALPP and ALPG support
only chemistry and topology — no physiological substrate is known for either — so their core
functions carry a `knowledge_gaps` entry and no `directly_involved_in`, which is the honest
representation rather than an omission.

## Process notes

- `just deep-research-falcon` failed twice before working: first a uv HTTP timeout
  (fixed with `UV_HTTP_TIMEOUT=300 uv sync`), then `uvx` resolving Python 3.11 while
  deep-research-client requires >=3.12. Worked around with
  `DEEP_RESEARCH_CLIENT_CMD="uvx --python 3.13 --from deep-research-client[cyberian]==0.2.7rc1 deep-research-client"`.
  Worth fixing in `scripts/deep_research_wrapper.py` so the uvx invocation pins a Python.
- No OLS MCP was available in this session; GO term definitions, ancestry and the
  GO:0140928 annotation provenance were checked against the QuickGO REST API instead.
- All 14 cited PMIDs are cached. Ten are abstract-only; PMID:19874193, PMID:28592560,
  PMID:41145834 and PMID:23533145 have full text. No experimental annotation was
  overruled on the basis of an abstract-only cache.
