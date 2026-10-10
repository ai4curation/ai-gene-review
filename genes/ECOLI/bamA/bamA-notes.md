# bamA / BamA (Omp85, YaeT) — *Escherichia coli* K-12 — curation notes

UniProt: P0A940 (BAMA_ECOLI), gene *bamA*, synonyms *yaeT*, *yzzN*, *yzzY*;
b0177. 810 aa precursor, signal peptide 1–20, mature chain 21–810. The protein
is bipartite: residues 21–424 are periplasmic and carry five POTRA
(polypeptide-transport-associated) domains, and the C-terminal region forms a
discontinuous 16-stranded transmembrane β-barrel (strands annotated from 425 to
808 in UniProt's FT block, loops 6 and 7 being the long extracellular ones).

Essential gene: UniProt's DISRUPTION PHENOTYPE reads "Deletion is lethal.
Depletion results in the accumulation of incorrectly assembled outer membrane
proteins, including TolC, OmpF, OmpC and OmpA".

## What GOA has, and the shape of the gap

50 GOA rows, and the distribution is lopsided:

- **molecular_function**: 27 rows of `GO:0005515 protein binding` (IPI) and one
  row of `GO:0051087 protein-folding chaperone binding` (IPI, SurA). Nothing
  else. The insertase activity — the thing BamA is famous for — has no
  molecular-function annotation at all.
- **biological_process**: `GO:0043165` (IBA, IDA, IEA, IPI), `GO:0051205`
  (IBA, IDA, IEA), `GO:0071709` (IEA).
- **cellular_component**: `GO:0009279` (five EXP, one IDA, one IEA),
  `GO:0016020` (IDA), `GO:0019867` (IEA), `GO:1990063` (IBA + three IDA + IPI).

So the processes and the complex are well covered; the molecular function is
carried entirely by 27 copies of the least informative term in the ontology.

## The molecular function: GO:0032977 is the right term, and the evidence is direct

`GO:0032977 membrane insertase activity` is defined as "Binds transmembrane
domain-containing proteins and mediates their integration into a membrane"
(verified against QuickGO, 2026-10; not obsolete; `is_a GO:0140597` protein
carrier activity `is_a GO:0140104` molecular carrier activity). β-barrel OMPs
are transmembrane proteins, so the definition covers them on its face, and a
search of the ontology turns up no more specific molecular-function term — no
β-barrel insertase term, and `GO:0032977` is the only MF term in GO whose name
contains "insertase".

**The decisive evidence is the reconstitution.** Purified Bam complex in
proteoliposomes folds and inserts OmpT
[PMID:20378773 "We purified the components that fold and insert Escherichia coli outer membrane proteins and reconstituted beta-barrel protein assembly in proteoliposomes using the enzymatic activity of a protein substrate to report on its folding state."],
and the product is genuinely in the bilayer rather than merely stuck to it
[PMID:20378773 "The folded OmpT was resistant to extraction from the pellet by incubation in 100 mM sodium carbonate for 30 minutes, suggesting that the folded protein had been integrated into the membrane."].
The reaction needs no energy source
[PMID:20378773 "The assembly of this protein occurred without an energy source but required a soluble chaperone in addition to the multi-protein assembly complex."],
which matters because it rules out a model in which some other ATPase does the
insertion and BamA only presents the substrate.

**BamA, not a partner, is where the substrate enters the membrane.** The barrel
lumen binds and partly folds substrate
[PMID:24914988 "The 16-stranded barrel surrounds a large cavity which implies a function in OMP substrate binding and partial folding."],
and release is lateral, through the seam of BamA's own barrel
[PMID:24914988 "These findings strongly support a mechanism of OMP biogenesis in which substrates are partially folded inside the barrel cavity and are subsequently released laterally into the lipid bilayer."]
[PMID:24619089 "the transmembrane β strands of OMP substrates may integrate into the outer membrane at the interface of the first and last β strands of the EcBamA barrel"].
A cryoEM structure of a late folding intermediate shows the substrate strand
hydrogen-bonded into BamA's gate directly
[PMID:39218969 "BamA lateral gate forms a continuous β-sheet with residues in the C-terminal region of OmpX"].
Even the isolated BamA barrel conducts
[PMID:16829683 "The full length YaeT and the isolated membrane domain induce pores when reconstituted in planar lipid membranes."],
with the conductance variability read as the signature of the gate
[PMID:16829683 "which could be an essential property of a lateral opening channel releasing proteins into the bacterial outer membrane"].

**The lipoproteins modulate; they do not supply the activity.** Only BamA and
BamD are essential
[PMID:26749448 "Of the five BAM subunits, only BamA and BamD are essential for cell viability."],
BamA is explicitly the central component whose conformation the others tune
[PMID:26744406 "binding of BamCDE modulates the conformation of BamA, the central component, which may serve to regulate the BAM complex"],
including by rotating against the barrel to drive the gate
[PMID:26901871 "these subunits rotate with respect to the integral membrane β-barrel of BamA to induce movement of the β-strands of the barrel and promote insertion of the nascent OMP"],
and BamE acts on BamA's conformation only indirectly, through BamD
[PMID:22178970 "our findings suggest that BamE modulates the conformation of BamA, likely through its interactions with BamD"].
In the reconstitution the four-protein BamACDE complex retained activity and
BamB improved it, i.e. the lipoproteins set efficiency.

### Comparator check: the absence of GO:0032977 from BamA is a gap, not a convention

The rule in CLAUDE.md is to assume a systematic absence encodes a convention
until a comparator query proves otherwise. Here the query settles it the other
way. Querying QuickGO for `GO:0032977` (34,326 annotations, 69 of them with
experimental evidence):

- **Yeast SAM50/Tob55 (P53969) carries GO:0032977 by IMP (PMID:14570913).**
  SAM50 is the Omp85-family β-barrel insertase of the mitochondrial outer
  membrane — the same protein family, the same fold, the same job (inserting
  β-barrels into an outer membrane), in the organelle descended from the
  Gram-negative ancestor. It also carries `GO:0008320 transmembrane protein
  transporter activity` by IDA. This is the comparator standing in exactly the
  same role, and it has the term.
- **E. coli YidC (P25714) carries GO:0032977 by IMP (PMID:10949305) and IDA
  (PMID:23872420)**, plus IBA and IEA. So the term is in routine use for
  bacterial insertases in this organism's own GOA, not reserved for eukaryotes.
- The term's other experimental holders span OXA1/OXA1L, COX18, GET1/GET2, the
  EMC subunits, MIM1/MIM2, TIMM22 and MTCH1/2 — a wide range of insertase
  machineries, which is the opposite of a narrowly-scoped term.

Two negative observations are worth recording honestly. Human SAMM50 (Q9Y512)
has only `protein binding` in the MF aspect, and E. coli TamA (P0ADE4) likewise
has only `protein binding` — so BamA is not uniquely neglected; the whole
Omp85 clade outside yeast SAM50 is under-annotated in the MF aspect. And
SAM50's GO:0032977 is IMP-only, never propagated as IBD/IBA, which is why no
IBA reached BamA. The pattern is best read as **PAINT never placed the node**,
not as a curatorial judgment that the term does not apply.

Verdict recorded in the review: `GO:0032977` is correct for BamA, belongs in
`core_functions` as the molecular function, and is asserted as `enables` rather
than `contributes_to`, following how GO treats SAM50 and YidC — both of which
also work only within larger machines (the SAM complex, the SecYEG holotranslocon)
and both of which carry the term in their own right.

## Substrate scope is broader than "β-barrel OMPs"

Three substrate classes are documented, and they argue for one general activity
rather than three.

1. **β-barrel OMPs**, the canonical class
   [PMID:26901871 "The OMPs in Gram-negative bacteria are inserted and folded into the outer membrane by the β-barrel assembly machinery (BAM)."].
2. **Autotransporter passenger domains.** A stalled EspP translocation
   intermediate crosslinks to BamA, and the authors conclude BAM does both jobs
   [PMID:19850876 "the Bam complex catalyzes both the integration of the beta domain into the OM and the translocation of the passenger domain across the OM in a C- to N-terminal direction"]
   [PMID:19850876 "we found that residues adjacent to the stall point interact with BamA, a component of a heterooligomeric complex (Bam complex) that catalyzes OM protein assembly"].
   Noted independently in the BAM structural literature
   [PMID:21586578 "Because the BAM complex has also implications in folding and export of autotransporters"].
3. **The lipoprotein RcsF**, which is not a β-barrel at all. BAM threads it
   through a partner barrel to the surface
   [PMID:32572278 "BAM also mediates export of the stress sensor lipoprotein RcsF to the cell surface by assembling RcsF-OMP complexes."],
   using the same gate regions
   [PMID:32572278 "RcsF is lodged deep within the lumen of the BamA barrel, binding regions proposed to undergo outward and lateral opening during OMP insertion."],
   and the funnelling is continuous in growing cells
   [PMID:25525882 "In growing cells, BamA continuously funnels RcsF through the β-barrel OmpA, displaying RcsF on the cell surface."].
   The dependency is what makes RcsF a sensor
   [PMID:25525882 "Thus RcsF senses envelope damage by monitoring the activity of the Bam machinery."].

The RcsF case is the one place where `GO:0032977` does not quite fit — RcsF has
no transmembrane domain — so the review records that as an ontology gap rather
than stretching the term.

## BAM versus TAM: what the BamA literature actually says

The question posed by `modules/bacterial_type_v_secretion.yaml`, which now
carries both routes. The honest answer is that **the BamA literature does not
address redundancy or substrate partitioning between BAM and TAM at all.** Of
the 22 references seeded into this review, none mentions TamA or TamB (checked
by grep across the nine with full text; every apparent hit was "β-lactamase").
What can be recorded is the following, and no more:

- The two machines are framed as **parallel modules of one system**, not as
  alternatives: the TAM is "a further module of the β-barrel assembly machinery"
  [PMID:25341963 "The BAM complex and a further module of the β-barrel assembly machinery, the translocation and assembly module (TAM), catalyze the insertion and assembly of nascent membrane proteins into the plane of the outer membrane"].
- TamA is in BamA's protein family
  [PMID:22466966 "it consists of an Omp85-family protein, TamA, in the outer membrane and TamB in the inner membrane of diverse bacterial species"],
  and InterPro makes the shared architecture explicit: `IPR010827` is named
  "POTRA domain, BamA/TamA-like" and is one of the two entries behind BamA's
  InterPro2GO annotations.
- **BAM is demonstrably competent on an autotransporter substrate** (EspP,
  PMID:19850876 above), and TAM is demonstrably required for another (Ag43, per
  `genes/ECOLI/flu/flu-notes.md`, where Ag43 shows no association with a
  membrane lacking the TAM). Two substrates, two machines, no experiment
  comparing them head to head in one background.
- bamA is essential and tamA is not, so the two are certainly not symmetric,
  but that asymmetry is consistent with both a general/specialist split and
  with partial redundancy; it does not discriminate.

Conclusion for the module: keeping both routes under `ONE_OR_MORE` is right,
and the "redundant, sequential or substrate-specific is unresolved" note is
accurate and should stay. Nothing in the BamA corpus licenses narrowing it.
The one substantive addition the BamA side makes is PMID:19850876 — direct
crosslinking evidence that an autotransporter passenger contacts BamA while
translocating — which is stronger than a generic "BAM assembles OMPs" argument
for including the BAM route.

## The CDI receptor role, and why no annotation is proposed for it

UniProt carries a second FUNCTION block, "(Microbial infection) Acts as a
receptor for CdiA-EC93". The evidence is good
[PMID:23882017 "The CdiAEC93 effector protein recognizes the widely conserved BamA protein as a receptor, yet E. coli EC93 does not inhibit other enterobacterial species."],
and mapped to specific surface loops
[PMID:23882017 "Our data indicate that BamA loops 6 and 7 form the CdiAEC93-binding epitope and their variation between species restricts CDIEC93 target cell selection."],
which also independently establishes that those loops face outward — the reason
GOA uses this paper for an EXP `cell outer membrane` row.

No process or function annotation is proposed, for two reasons.

1. **Participation.** In contact-dependent growth inhibition the work is done
   by the attacking cell's CdiA: BamA is the epitope that is recognised. Being
   the thing a process acts on is not participation (CLAUDE.md). BamA's own
   loop sequence determines target range, which is necessity and specificity,
   not activity.
2. **No term fits.** GO has no contact-dependent-growth-inhibition term (the
   "contact inhibition" terms, GO:0060242 and children, are about metazoan cell
   proliferation). The nearest comparator is FhuA, the colicin M / phage T1
   receptor, which GOA gives `GO:0015643 toxic substance binding` (IMP) and
   `GO:0046790 virion binding` (IMP) — both plain binding terms that name the
   ligand without naming a function, so importing that pattern would reproduce
   the `protein binding` problem rather than fix it.

Recorded instead as a suggested question.

## Per-row notes on the 27 `protein binding` rows

They are not 27 independent findings. By interactor:

- **BamB (P77774)** — 11 rows, plus the EcoliWiki `yfgL` row inside the
  three-partner 15851030 annotation. Direct, mapped to POTRA 1-3
  [PMID:22948914 "Pull-down and Western blotting assays indicate that BamB interacts directly with the POTRA 1-3 domain of BamA"]
  and to a specific BamB surface
  [PMID:18165306 "Cysteine-directed cross-linking data show that the region encompassing L173, L175, and R176 makes direct contact with YaeT."].
- **BamD (P0AC02)** — 10 rows. Direct
  [PMID:16824102 "We demonstrate that YfiO and YfgL directly interact with YaeT in vitro, while NlpB interacts directly with YfiO."],
  and localised to POTRA5
  [PMID:26749448 "The POTRA5 domain binds BamD between its tetratricopeptide repeats 3 and 4."].
- **BamC (P0A903), BamE (P0A937)** — within the two multi-partner structural
  rows; both sit peripherally, BamE reaching BamA via BamD (PMID:22178970 above).
- **RcsF (P69411)** — 2 rows, substrate handling, discussed above.

Every one of these says "BamA touches another Bam subunit", which is exactly
what `GO:1990063 Bam protein complex` (already annotated, three IDA rows) says
in a form that carries meaning. So the rows are removed as uninformative rather
than modified: there is no more specific molecular function to promote them to,
because scaffolding the lipoproteins is not BamA's activity — BamA is the
catalytic subunit and the lipoproteins are what attach to it. (Contrast BamE,
which GOA does give `GO:0030674 protein-macromolecule adaptor activity`; that
term is right for a peripheral linker and wrong for the central barrel.)

## Ontology housekeeping

- `GO:0071709 membrane assembly` (IEA from `IPR023707`) is an ancestor of
  `GO:0043165`, which GOA already carries from three other sources. IPR023707 is
  the BamA-specific family entry, so the mapping can be the specific child.
- `GO:0016020 membrane` (IDA) is the ontology root for membranes and is an
  ancestor of `GO:0009279`, which is annotated with six experimental rows.
- `GO:0019867 outer membrane` (IEA from `IPR000184` + `IPR010827`) is also an
  ancestor of `GO:0009279`, but here the broad term is the *honest* mapping:
  both domains occur in mitochondrial and plastid Omp85 proteins (Sam50, Toc75),
  where "cell outer membrane" would be wrong. Kept as-is.
- All three IBA rows cite `PANTHER:PTN000302080|UniProtKB:P0A940`. P0A940
  appearing in its own WITH/FROM is correct and expected — it marks that the
  node was placed partly on this gene's own experimental annotations — and is
  not circularity.

---

## The GOA molecular-function gap is a curation gap, not a knowledge gap

Moved here from `core_functions[0].knowledge_gaps` on PR review. CLAUDE.md
reserves `knowledge_gaps` for things nobody knows, resolvable only by new
experiments; this one is resolvable by curation, so it belongs in notes. The
substance is unchanged.

GOA records no molecular function for BamA beyond protein binding and chaperone
binding, leaving the insertase activity expressed only through process and
component terms. This review proposes `GO:0032977`, which the comparator check
supports: yeast SAM50, the Omp85-family beta-barrel insertase of the
mitochondrial outer membrane, carries the term by IMP, and *E. coli* YidC carries
it by IMP and IDA. The gap appears to be a propagation failure rather than a
curatorial judgment, since SAM50's annotation was never placed as an ancestral
IBD and so no IBA reached the bacterial clade. Human SAMM50 and *E. coli* TamA
are in the same position, with only protein binding in the molecular function
aspect.

**What was asserted instead, and why.** `GO:0032977` as `enables` for BamA, on
the strength of the proteoliposome reconstitution plus the structural evidence
that the substrate strand pairs with BamA's own lateral gate. Not asserted for
the complex as an undifferentiated whole, and not weakened to `contributes_to`,
since GO places the same term on SAM50 and YidC in their own right despite both
working only within larger machines.

**Why it mattered beyond this gene.** The absence of an insertase molecular
function in GOA forced `modules/bacterial_type_v_secretion.yaml` to assert
`GO:0032977` for BamA as an explicit curator synthesis and flag the discrepancy;
the same would apply to any pathway model of outer-membrane protein biogenesis.
Settling the term on the gene removes the need for that synthesis.
