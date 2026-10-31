---
title: "CACAO community annotations review"
maturity: IN_PROGRESS
tags: [EVALUATION]
species: [STRP1, EBOZM, yeast, RVFVZ, BUNYW, BPPRD, PSEAE, BPP22, SHIFL, ECOLI, BPPH2, BPT4, BPT5, BPP1, BPPGK, 9CAUD, HHV8P, SENDZ, SINDV, SFVCP, SALTY, TRYCR, NOSB1, BACSU, LAMBD, human, mouse, rat, ARATH, DROME]
genes: [pppL, VP35, VP40, GP, WHI3, NSS, N, XV, fabY, sieA, ipaH4.5, clpX, cha, STM3697, doc, acrIIA5, K3, K5, VPS74, APN1, lysK, gag, SWP7, acs, ybjN, D15, "3", "5.4"]
---

# CACAO community annotations review

**Bottom line:** CACAO (Community Assessment of Community Annotation with
Ontologies) is the GONUTS/Texas A&M course-based curation programme in which
student teams wrote experimental GO annotations from the literature, refereed
by competing teams and instructors. GOA carries 4,373 annotations with
`assigned_by: CACAO` on 2,987 gene products from 658 taxa (snapshot
2026-10-28). They are almost all experimental (2,268 IDA, 1,952 IMP, 86 IGI)
and mostly biological process (2,438 BP, 1,034 MF, 901 CC). Gene reviews
already exist for 281 of these gene products, covering 503 CACAO rows. Those
reviews accepted 263, kept 150 as non-core, modified 47, marked 20
over-annotated, removed 9, left 7 undecided, and called 2 too general; 5 rows
are absent from the review files, which predate them.

**Result so far (30 microbial genes, 143 CACAO rows).**

| | rows | ACCEPT | MODIFY | NON_CORE | OVER_ANN | TOO_GEN | REMOVE |
|---|---:|---:|---:|---:|---:|---:|---:|
| Batch 1 (12 genes) | 71 | 30 | 21 | 11 | 7 | 1 | 1 |
| Batch 2 (18 genes) | 72 | 48 | 12 | 6 | 4 | 0 | 2 |
| Total | 143 | 78 | 33 | 17 | 11 | 1 | 3 |

Batch 1 accepted 42% of rows as written, batch 2 **67%**. The likeliest cause
is literature depth rather than student quality: batch-1 genes (Ebola, RVFV,
ClpX, WHI3) each draw on many papers, often with later work contradicting the
annotated one, while most batch-2 genes rest on one or two well-characterized
studies. If that holds, the predictor of a CACAO error is how much literature
has accumulated since the annotation, not who made it.

**The errors are mostly not CACAO's.** On batch-2 genes the defective rows
were far more often from InterPro2GO, UniProt keywords, ARBA, IntAct, RHEA,
HAMAP, CAFA and UniRule than from students. Three genes (chagasin, STM3697,
P1 Doc) had every CACAO row sound while carrying real defects from automated
pipelines; LysK is the sharpest case, where the students picked the
host-directed interspecies term and InterPro2GO plus a UniProt keyword did
not. Two batch-1 patterns catalogued as student failures turned out to arrive
by those routes too. A project framed as auditing student work is in practice
measuring the whole annotation supply chain, and CACAO is not the weakest link
in it.

**What does fail is provenance, not biology.** Batch 2's recurring problem is
not a wrong claim but a wrong basis for a right claim: the wrong paper cited
(APN1, Gag), the wrong gene's paper (T4 gp5.4), the wrong isolate's
experiments (Gag), the wrong qualifier (AcrIIA5), the wrong evidence code
(SWP7, D15), an artefact paper read as positive evidence (Gag), or a
superseded mechanism (P1 Doc). These are invisible to any check that compares
terms, and they are exactly what downstream automated inference propagates.

**Counting caveat.** Action tallies measure term correctness, not annotation
correctness, and the two come apart. Two of T4 gp5.4's four misattributed
rows name the virion baseplate, which is independently true of gp5.4, so an
inventory scores them as successes while their stated evidence is about a
different protein. Treat the ACCEPT column as a floor on error, not a
measure of it.

**Microbes first.** Microbial proteins (bacteria, archaea, viruses and phages,
fungi and protists) carry 2,166 CACAO rows on 1,617 gene products, half the
corpus, but only 116 of them are reviewed, against 151 of 1,107 animal
proteins. They are also where the judged rows fail hardest: 8 of the 9
CACAO removals so far are on microbial genes, out of 199 microbial rows
judged (137 accepted, 20 non-core, 21 modified, 4 over-annotated, 8 removed,
2 undecided, 2 too general, 5 missing). For many of these proteins, notably
phage and virus proteins, the CACAO row is the only experimental GO
annotation, so an error there is not diluted by other curation. The review
order is therefore microbes first, ranked by CACAO row count; the animal and
plant genes follow.

The question for this project is whether CACAO rows fail in a characteristic
way that differs from professional curation, and how often. After two batches the taxonomy has eighteen shapes, grouped below. Only the
first was expected; the rest were found by reading papers against term
definitions. Several arrive from automated pipelines as often as from
students, so the taxonomy classifies *annotation* failures, not CACAO ones.

**Wrong claim about the biology**

- **Phenotype read as process.** An effect several steps downstream of the
  gene's activity, annotated as the process itself: `positive regulation of
  cyclase activity` on MAPK3, MAPK8 and MAPK14 from one paper
  (PMID:22027397); WHI3 `positive regulation of translation` from a
  protein-level change; clpX `cell division` from a genetic interaction the
  authors read as modulation.
- **Precursor supply read as pathway participation.** The variant a
  pleiotropic metabolic knockout produces: fabY starves many pathways of
  acyl-ACP, and each downstream product became its own process term (quorum
  sensing, siderophore biosynthesis, lipid A biosynthesis), none of them a
  step FabY performs.
- **Sign inverted.** The term asserts the opposite of the result. pppL
  `positive regulation by symbiont of entry into host` rests on an adherence
  proxy while the invasion data show the mutant is sixfold *more* invasive;
  Bunyamwera NSs carries both `viral gene expression` and `negative
  regulation of viral genome replication` from one figure showing ~10x *more*
  viral protein, so the two rows contradict each other.
- **Wrong arm of a bidirectional pathway.** Five rows on `GO:0039502
  suppression of type I interferon signalling` whose papers assay interferon
  *production*: VP35 once (its companion paper explicitly shows VP35 cannot
  block receptor signalling, which is VP24's job), RVFV NSs twice, Bunyamwera
  NSs twice. **The shape is not uniformly an ontology gap**, and the three
  reviews resolve it three ways for good reasons. For VP35 the right terms
  already existed (`GO:0039540` RIG-I and `GO:0039548` IRF3, the
  mechanism-specific induction-side terms), so that row is an ordinary
  term-choice error. The two NSs proteins antagonise no sensor or IRF at all
  — IRF-3, NF-kappaB and AP-1 all activate normally and the lesion is a
  global block on host RNA polymerase II — so no existing term fits them, and
  the gap is specifically the absence of a **mechanism-agnostic production
  term**, a symbiont-mediated counterpart of `GO:0032480`. The RVFV NSs review
  files that term as `proposed_new_terms`; the Bunyamwera rows go to
  `GO:0052170` for now and say they should move to the new term if GO creates
  it. The gap is also not CACAO's fault: UniProt IDA rows and KW-1114 IEA
  rows land on `GO:0039502` the same way.
- **Right pathway, wrong molecular step.** ipaH4.5 `symbiont-mediated
  suppression of host translation` where the readout is an NF-kB reporter and
  cytokine output: host gene expression, not translation. The term is a
  sibling inside the correct neighbourhood, the paper is the right paper and
  the evidence code fits, so only the term definition catches it.
- **Own-process term for a host-directed activity.** PRD1 endolysin
  `cell wall disassembly`, which is an organism disassembling *its own* wall;
  a phage has none. The interspecies branch (GO:0052009) is where it belongs.
  Likely systematic across phage and effector annotations.
- **Parent-level restatement.** The same experiment annotated twice, once at
  the specific term and once at its ancestor: sieA `regulation of viral entry`
  beside `superinfection exclusion`; VP40 `host cell membrane` three times
  where every assay is plasma-membrane specific. True, redundant, and
  `MODIFY` rather than a failure.
- **Mechanism paper read as a localization.** The mirror image of
  phenotype-as-process, found on Ebola GP: an IDA cellular-component row
  whose paper images only host machinery (clathrin, transferrin, Eps15) and
  never localizes the viral protein at all.
- **Actor substitution across the host/symbiont boundary.** KSHV K3 and K5
  both carry `endocytosis involved in viral entry` from the same paper: what
  is endocytosed is the *host* lectin the ligase destroys, and the entry
  effect is the lectin's. The mirror of the own-process shape above. (The two
  reviews first treated it differently — K5 removed the row, K3 repointed it —
  and the split was resolved in K3's favour on review: K5's own paper shows it
  drives DC-SIGN endocytosis in the dynasore-washout assay, with the RING-CH
  mutant as comparator, so both genes now MODIFY to GO:0044077 and both file
  the CACAO defect. Removing would have dropped a real claim, since neither of
  K5's remaining rows from that paper carries it.)
- **Overexpression-only phenotype on a mutant-phenotype code.** YbjN
  `negative regulation of cell growth`, where ~20x overexpression slows
  growth and the deletion grows like wild type. Distinct from
  phenotype-as-process: the asserted phenotype does not exist.
- **Heterologous-system localization read as a host location.** Sindbis 6K at
  the plasma membrane, assayed in frog oocytes; phi29 p3 in the *host cell
  nucleus*, assayed in mammalian cells when the host is *B. subtilis*, which
  has no nucleus.
- **Reaction run backwards read as a second enzyme class.** Acs annotated as
  a protein-lysine *deacetylase*: the claim is in the abstract, but the term's
  parent demands hydrolysis and Acs is a ligase running its own transfer in
  reverse. Likely recurs wherever a reversible-enzyme paper says a substrate
  was "demodified by X".

**Wrong term for a right claim**

Two shapes catalogued before batch 1 did not recur in it: **one paper applied
to genes it does not assay** (PMID:25313396 for fliH, fliY and swrD; see
[BACSU](BACSU.md)) and **single-assay localization** (SNAP23 mitochondrion,
KRT19 plasma membrane). Every batch-1 paper was about its gene.

- **Structure-blind term for a structure-specific activity.** T5 D15
  `double-stranded DNA endonuclease` sits on a different branch from the
  flap-endonuclease terms, so no ancestor/descendant redundancy check flags
  it, yet the bare reading is contradicted by a later paper. Our own tooling
  cannot see this class.
- **Wrong parent structure.** Sindbis `icosahedral viral capsid, spike`: the
  right assembly under the wrong parent, since alphavirus spikes sit in the
  envelope. Driven by a real gap — GO has no envelope-spike term.
- **No term exists to correct it.** YbjN's inverted `pilus assembly` cannot be
  repaired: GO's pilus regulation terms cover only type IV pili. A wrong row
  that needs ontology work, not a re-term.

**Wrong provenance for a right claim** (batch 2's dominant group)

- **Over-harvesting one paper.** APN1's four rows all cite one 2003 paper;
  three name activities it does not assay but the protein genuinely has, each
  shown in a *different* paper. SGD curated the same paper and took exactly
  one term, sourcing the rest properly — a direct professional comparator on
  identical input.
- **Adjacent-locus identifier confusion.** All four T4 gp5.4 rows come from
  papers about gp5, the product of the neighbouring gene; "gp5"/"gp 5"
  resolved to the entry named `5.4`. Numeric phage gene names make this cheap
  to audit and easy to commit.
- **Right term, wrong paper.** Gag's chromatin row cites a paper with no
  chromatin assay; the result is in another paper from the same lab.
- **Artefact paper read as positive evidence.** Another Gag row cites a paper
  that demonstrates its own nuclear signal is a fixation artefact.
- **Cross-isolate experimental transfer.** All four Gag rows put IDA/IMP on
  the chimpanzee isolate from prototype-foamy-virus experiments; ISS is the
  right code. UniProt virus entries are isolate-level while the literature
  works in reference strains, so this should recur across CACAO's virus rows.
- **Wrong qualifier, right term.** AcrIIA5's 2025 row uses
  `acts_upstream_of_or_within_positive_effect` for a process the protein
  executes; the same group's earlier rows use `involved_in`. Queryable
  corpus-wide without reading anything.
- **One assay under two evidence codes.** SWP7's adhesion row submitted as
  both IDA and IMP three weeks apart, where no mutant can exist
  (microsporidia are untransformable). Unlike parent-level restatement, the
  term is identical.
- **Mechanism superseded, term unaffected.** P1 Doc's translation-suppression
  row rests on a 30S-occlusion mechanism later overturned; the term asserts
  the outcome, so the row survives for a reason the student did not intend.
  Recorded as a `finding_review`, not an action change.

**A CACAO error does not stay put.** VP40's `intracellular transport of virus`
row, which has no transport assay behind it, has already seeded an
inter-ontology IEA (GO_REF:0000108), and K5's removed viral-entry row is now
restated by an ARBA rule. Two of 143 rows examined have been amplified
downstream, so error rates counted on CACAO rows alone understate the
footprint.

**Two near-misses on the curator-deference rule.** AcrIIA5 cites a paper whose
title and abstract are about a different anti-CRISPR protein (AcrIIA6); only
the full text shows this protein was co-assayed. VPS74 cites a mammalian
GOLPH3 paper that contains a genuine yeast panel. Both would have been
recorded as wrong-gene errors from the abstract alone, so batch 1's
"paper not about the gene" counts should be re-checked against full text.

CACAO annotations are experimental, so the
[curator-deference rule](../CLAUDE.md) applies: the student read the full
text, and a `REMOVE` needs the paper itself, not its abstract. The GONUTS wiki
(`gowiki.tamu.edu`) keeps a page per paper and per protein for CACAO
annotations (the ALDH4A1 review used both), and is the first thing to check
when the cached publication is abstract-only. **As of 2026-10-29 that check
is unavailable**: gowiki.tamu.edu serves only "This site is temporarily
offline while we perform upgrades", and the Internet Archive has no snapshot
of the relevant pages. Every batch-1 row was therefore judged from the paper
alone. Re-check the abstract-only rows when GONUTS returns.

## Project files

- [`CACAO/data/cacao-quickgo-2026-10-28.tsv`](CACAO/data/cacao-quickgo-2026-10-28.tsv):
  QuickGO download of every annotation with `assignedBy=CACAO`.
- [`CACAO/data/taxon-groups.yaml`](CACAO/data/taxon-groups.yaml): each of the
  658 taxa assigned to a broad group (Bacteria, Archaea, Viruses, Fungi,
  Metazoa, Viridiplantae, Other eukaryote) from its UniProt taxonomy lineage.
  Regenerate with `uv run python projects/CACAO/scripts/fetch_taxon_groups.py`.
- [`CACAO/cacao-inventory.yaml`](CACAO/cacao-inventory.yaml): per gene review,
  the action given to each CACAO row, matched on term, evidence code and
  reference; counts by group; and the top 100 unreviewed microbial gene
  products by CACAO row count. Regenerate with
  `uv run python projects/CACAO/scripts/cacao_inventory.py`.

## Coverage

| Group | CACAO rows | Gene products | Reviewed |
|-------|-----------:|--------------:|---------:|
| Metazoa | 1,847 | 1,107 | 151 |
| Bacteria | 1,238 | 975 | 34 |
| Viruses (incl. phages) | 612 | 409 | 54 |
| Viridiplantae | 360 | 263 | 14 |
| Fungi | 236 | 170 | 28 |
| Other eukaryotes (protists) | 56 | 42 | 0 |
| Archaea | 24 | 21 | 0 |

Top taxa:

| Taxon | CACAO rows | Gene products without a review |
|-------|-----------:|-------------------------------:|
| *Homo sapiens* (human) | 741 | 346 |
| *Mus musculus* (mouse) | 672 | 320 |
| *Bacillus subtilis* 168 (BACSU) | 160 | 98 |
| *Escherichia coli* K-12 (ECOLI) | 156 | 102 |
| *Arabidopsis thaliana* (ARATH) | 144 | 94 |
| *Rattus norvegicus* (rat) | 107 | 75 |
| *Saccharomyces cerevisiae* (yeast) | 106 | 45 |
| *Drosophila melanogaster* (DROME) | 73 | 37 |
| *Oryza sativa* japonica | 70 | 43 |
| Phage T4 (BPT4) | 48 | 21 |

## Approach

1. Review microbial genes first, those with the most CACAO rows at the top,
   so each review judges several student annotations at once. Batch 1 is
   every unreviewed microbial gene product with at least five CACAO rows.
   Most microbial proteins carry only one or two CACAO rows (1,174 of the
   1,501 unreviewed have one), so later batches should group them by
   organism or by cited paper rather than by row count. Animal and plant
   genes come after.
2. Use the standard workflow (`just fetch-gene`, deep research, the
   annotation-reviewer agent). In each review, note in the CACAO rows'
   `reason` what the cited paper shows and, where the cache is abstract-only,
   what the GONUTS page records.
3. After each batch, rerun the inventory script and update the counts and
   failure shapes above.
4. Once enough rows are judged, compare the CACAO acceptance rate with that of
   experimental rows from other groups on the same genes.

---
# STATUS

Snapshot 2026-10-29: 311/2,987 CACAO gene products reviewed; 646/4,373 rows
judged. Microbial: 146/1,617 reviewed. Batches 1 and 2 complete except phage
phi29 p6 (blocked, below).

## Batch 1: microbes, at least five CACAO rows

Organism codes are UniProt mnemonics, for `just fetch-gene <CODE> <gene>`.
Counts are total review rows / CACAO rows.

- [x] STRP1 pppL (Q99YM9), *Streptococcus pyogenes* M1 SP-STP, 13/8
- [x] EBOZM VP35 (Q05127), Zaire ebolavirus, 32/8
- [x] EBOZM VP40 (Q05128), Zaire ebolavirus, 34/6
- [x] yeast WHI3 (P34761), 33/6
- [x] RVFVZ NSS (P21698), Rift Valley fever virus, 24/6
- [x] BUNYW N (P16494, entry NSS_BUNYW), Bunyamwera virus, 9/6
- [x] BPPRD XV (P13559), phage PRD1 endolysin P15, 15/6
- [x] PSEAE fabY (Q9HU15), *Pseudomonas aeruginosa* PAO1, 11/5
- [x] BPP22 sieA (Q38674), phage P22 superinfection exclusion, 7/5
- [x] EBOZM GP (Q05320), Zaire ebolavirus glycoprotein, 33/5
- [x] SHIFL ipaH4.5 (P18009), *Shigella flexneri*, 13/5
- [x] ECOLI clpX (P0A6H1), 36/5
- [ ] BPPH2 6 (P03685), phage phi29 nucleoid protein p6, 5 CACAO rows —
  **blocked** — tracked in issue #5733. Notes are written
  (`genes/BPPH2/6/6-notes.md`) but two attempts to write the review YAML were
  stopped by a safety classifier, in two sessions. Needs a human to look at
  the notes and finish or drop the gene.

## Upstream reports from batches 1 and 2

Recorded as `source_defects` / `proposed_new_terms`; run
`just export-source-defects` for the per-resource reports.

- [ ] GO: no symbiont-mediated counterpart of GO:0032480 *interferon
  production* (proposed in the RVFV NSs review; of the five rows across three
  viruses that land on the signalling term, the four on RVFV and Bunyamwera
  NSs need it, while VP35's is covered by existing induction-side terms).
- [ ] **This repo, not GO:** `GOCellularLocationEnum` cannot express
  GO:0055036 virion membrane or GO:0019031 viral envelope in
  `core_functions.locations`, which is where a virion surface protein's
  activity happens (found on GP). Checked against OLS: both sit under
  GO:0044423 *virion component*, a direct child of GO:0005575 outside the
  GO:0110165 *cellular anatomical entity* branch the enum materialises from
  (`src/ai_gene_review/schema/gene_review.yaml`), so GO is self-consistent
  and the fix is to add GO:0044423 as a second source node here. The GP review
  now states the omission in its core-function description rather than
  substituting a host-cell term.
- [ ] GO/EBI: UniProt keyword KW-0081 maps phage endolysins to GO:0042742
  *defense response to bacterium*, inverting the interaction direction (XV).
- [ ] UniProt: P18009 AltName "Probable RING-type E3 ubiquitin transferase"
  contradicts its own NEL domain and Cys379 active site (ipaH4.5).
- [ ] CAFA: ClpX assigned to GO:0009376 HslUV complex from an SspB/ClpXP
  paper; an IBA rests on that row (clpX).
- [ ] GO Central: the IBD on PANTHER node PTN000137358 asserts GO:0051301
  *cell division*, but its donor evidence is FtsZ modulation, so the node
  term should be GO:0051302 *regulation of cell division* — correcting every
  IBA inherited from it, not just clpX's row.
- [ ] RVFV NSs GO:0039689 row contradicted by its own cited abstract.
- [ ] UniProt: KW-1114 maps to type I interferon suppression, but the keyword
  is interferon-class neutral; KSHV K3 and K5 both target the type II
  receptor. Affects every entry carrying the keyword.
- [ ] InterPro: IPR002502/IPR036505 and IPR018110 map muralytic and
  enolase-superfamily domains to own-process metabolic terms
  (GO:0009253, GO:0009063) with no taxon constraint (LysK, STM3697).
- [ ] UniProt: phi29 p3 carries four keyword rows from a superseded
  attribution — the peptidoglycan hydrolase is tail protein gp13 (P15132).
- [ ] UniProt: P1 Doc has a DNA-binding keyword the literature contradicts,
  and a RHEA serine-kinase mapping where the only acceptor shown is a
  threonine.
- [ ] GONUTS/CACAO: T4 gp5.4's four rows belong on P16009 (gp5); AcrIIA5's
  2025 row has the wrong qualifier; SWP7 and D15 each have a wrong evidence
  code; Gag's four rows need ISS, not IDA/IMP.
- [ ] GO: no envelope-spike CC term (Sindbis); no pilus-assembly regulation
  terms outside type IV (YbjN); no threonine sibling of GO:0106310 (Doc);
  no host-cell-nucleoid term (phi29 p3); no microsporidian exospore or
  endospore terms (SWP7); no term for SieA's activity (batch 1).

## Batch 2: microbes, four CACAO rows — all 18 complete

Total review rows / CACAO rows. Folder names follow the CLAUDE.md conventions
for entries with no usable gene symbol.

- [x] TRYCR cha (Q966X9), *T. cruzi* chagasin, 11/4 — all 4 sound
- [x] SALTY STM3697 (Q8ZL58), L-talarate/galactarate dehydratase, 12/4 — all 4 sound
- [x] BPP1 doc (Q06259), phage P1 Doc toxin, 16/4 — all 4 sound
- [x] 9CAUD acrIIA5 (A0A220GHA5), phage D4276 anti-CRISPR, 6/3 — all 3 sound
- [x] BPPH2 3 (P03681), phi29 terminal protein p3, 17/4 — all 4 sound
- [x] HHV8P K3 (P90495), KSHV MIR1, 21/4
- [x] HHV8P K5 (P90489), KSHV MIR2, 23/4
- [x] SENDZ V__P69282 (P69282), Sendai virus V, 14/4
- [x] yeast VPS74 (Q06385), 39/4
- [x] yeast APN1 (P22936), 21/4
- [x] BPPGK lysK (Q6Y7T6), phage K endolysin, 16/4
- [x] SFVCP gag (Q87039), simian foamy virus Gag, 22/4
- [x] NOSB1 SWP7 (B3STP1), *Nosema bombycis* spore wall protein, 11/4
- [x] ECOLI acs (P27550), acetyl-CoA synthetase, 16/4
- [x] ECOLI ybjN (P0AAY6), 8/4
- [x] BPT5 D15 (P06229), phage T5 flap endonuclease, 38/4
- [x] SINDV P03316 (P03316), structural polyprotein, 50/4
- [x] BPT4 5.4 (P39234), baseplate puncturing device, 8/4 — all 4 misattributed

## Batch 3 (not started)

1,174 of the 1,501 unreviewed microbial gene products carry a single CACAO
row, so ranking by row count is exhausted. Group them instead, and prefer
groupings that test a batch-2 finding:

- [ ] **Phage genes with numeric names**, for adjacent-locus identifier
  confusion (the T4 gp5.4 shape). Cheap to screen: compare each cited paper's
  gene designation against the entry's.
- [ ] **Virus rows whose cited paper used a different isolate**, for the
  cross-isolate transfer shape (Gag). Also screenable without reading.
- [ ] **All CACAO rows with a non-`involved_in` qualifier**, for the
  wrong-qualifier shape (AcrIIA5). One query over the snapshot.
- [ ] By organism, for the remaining bacteria (941 unreviewed gene products)
  and *E. coli* / *B. subtilis* in particular, where MOD curation gives a
  professional comparator on the same genes.

## Later: animals and plants (top by CACAO row count)

mouse Reln (20), Shank3 (18), Sirt6 (14), Nlgn3 (13), Wnt5a (11), Pafah1b1
(9), Zbtb20 (8); rat Nlgn1 (9); human GOLPH3 (6), PLAUR (6).

## Follow-ups on existing reviews

- [ ] Add the 5 CACAO rows missing from existing reviews (phage T4 genes 9,
  11 and 18, lambda stf, phi6 P9); four have no evidence code in GOA.
- [ ] Resolve the 7 `UNDECIDED` CACAO rows (DNM1L, CASK, APC, Gpdh1, Sirt5,
  and fliH x2) using the GONUTS records.
- [ ] Re-check batch 1's "paper not about the gene" judgments against full
  text where it exists. Two batch-2 near-misses (AcrIIA5, whose cited paper's
  title is about a different anti-CRISPR, and VPS74, whose mammalian GOLPH3
  paper contains a real yeast panel) would both have been recorded as
  wrong-gene errors from the abstract alone.

# NOTES

## 2026-10-29 (session 2: batch 2)

All 18 batch-2 genes reviewed, validating with 0 errors; 349 review rows, 72
CACAO rows judged (48 ACCEPT, 11 MODIFY, 6 non-core, 4 over-annotated, 3
REMOVE). Acceptance rose from 42% to 67%, and the taxonomy grew from 8 shapes
to 18, now grouped by what is actually wrong: the claim, the term, or the
provenance. See the summary for the two conclusions that matter — most
defective rows on these genes come from automated pipelines rather than
students, and batch 2's own failures are provenance failures.

Hypotheses carried into batch 2 from batch 1, and how they fared:

- *Endolysins mistake host-directed for own-process terms* — **wrong about
  the culprit.** LysK's CACAO rows chose correctly; InterPro2GO and a UniProt
  keyword did not.
- *Virus rows confuse the two interferon arms* — **not confirmed.** Sendai V's
  papers assay production and nobody annotated signalling. The GO gap is real
  (confirmed twice) but does not reliably produce the error.
- *Paralogous ligases invite mis-attribution (K3/K5)* — **not confirmed.**
  Both papers assay their protein with its own mutant series.
- *Promiscuous screen-derived enzymes over-annotate (STM3697)* — **wrong.**
  Dual substrate use in one active site, replicated independently.
- *Central-metabolism knockouts spawn downstream process terms (fabY shape)*
  — **not present in acs**, which catalyses the entry step of both pathways.

Four of five transferred hypotheses came back negative. Worth stating because
the agents tested them rather than confirming them; a framing handed to a
reviewer is a prediction, not a finding.

## 2026-10-29

Batch 1 reviewed: 12 of 13 genes complete and validating with 0 errors, 260
review rows, 71 CACAO rows judged. One gene (phage phi29 p6) is blocked as
above. Results and the eight-shape failure taxonomy are in the summary.

Method notes for later batches:

- **GONUTS is offline**, so the student-evidence check that the plan relies on
  is unavailable. Revisit the abstract-only rows when it returns.
- **No deep-research provider keys in this container**, so reviews were done
  from cached publications plus PubMed/PMC and web search. Recorded in each
  notes file; no `-deep-research-*.md` files were created.
- **Re-fetching upgrades the cache.** Two pppL papers went from abstract-only
  to full text on a forced re-fetch; worth doing routinely before judging.
- **Do not run corpus-wide cache scripts.** `scripts/warm_reference_cache.py`
  ignores `--help` and starts warming everything; a run during batch 1
  rewrote 20 unrelated `publications/` files, stripping cached full text.
  They were restored, but the damage was briefly committed.

## 2026-10-28

Project started. Downloaded all 4,373 CACAO annotations from QuickGO and
matched them to the 9,353 existing gene reviews by UniProt accession. 281
gene products already reviewed; their CACAO rows were judged in passing,
not as a CACAO-focused audit. Actions on those rows: ACCEPT 263,
KEEP_AS_NON_CORE 150, MODIFY 47, MARK_AS_OVER_ANNOTATED 20, REMOVE 9,
UNDECIDED 7, TOO_GENERAL 2, not in review 5.

The nine removals: swrD, fliY (PMID:25313396), phage T4 E lysozyme GO:0003796,
yeast HAP4 GO:0098803, LRO1 GO:0046027 (ISO), spoVAD GO:0031160, ECOLI traB
GO:0016887, lambda Rz1 GO:0045861, ARATH DELTA-OAT GO:0051646. Each should be
rechecked against its GONUTS record before the failure taxonomy is fixed.

Later the same day, at the user's request, the review order was switched to
microbes first. Added `fetch_taxon_groups.py`, which assigns every taxon to a
broad group from its UniProt lineage, and extended the inventory with
per-group counts and a ranked list of unreviewed microbial gene products.
Batch 1 is now the 13 microbial proteins with five or more CACAO rows; the
animal batch moved to the end of the queue.
