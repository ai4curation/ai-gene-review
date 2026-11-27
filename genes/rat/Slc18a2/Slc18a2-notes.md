# Slc18a2 (rat) curation notes

Session: create review for rat Slc18a2 / VMAT2 / Q01827 (RGD:3694, GeneID 25549).

## Setup

- `just fetch-gene rat Slc18a2` timed out once on rest.uniprot.org, succeeded on retry.
  UniProt id confirmed as Q01827 (`ID VMAT2_RAT`), `DR RGD; 3694; Slc18a2.`,
  `DR GeneID; 25549;` — matches the requested accession, so no accession switch.
- `just fetch-gene-pmids rat Slc18a2` cached 23 publications; PMID:18315567 fetched
  separately (full text available, read).
- No deep-research provider keys in this environment. Literature work done by hand and
  written to `Slc18a2-deep-research-manual.md` (never named `-deep-research-<provider>.md`).

## Full text availability

Full text cached: PMID:18315567, PMID:18992277, PMID:19903816, PMID:20007701,
PMID:25355561, PMID:8753875. All other cited PMIDs are abstract-only, which constrains how
hard any row can be pushed (experimental rows whose full text is unavailable were not
removed).

## Review decisions worth recording

1. **GO:0005335 serotonin:sodium:chloride symporter activity (IBA)** — removed. VMAT2 is an
   electrogenic monoamine/2H+ **antiporter** on the vesicle membrane, not a Na+/Cl--coupled
   plasma-membrane symporter (that is SERT/SLC6A4). The IBA sits on PANTHER node
   PTN000607052 with donors including *Slc18a1* and *C. elegans* cat-1, which are all
   H+-antiporters too, so the node itself is mis-typed rather than mis-propagated to rat.
   Recorded as a `source_defects` WRONG_TERM against GO_CENTRAL, plus `propagation_review`.
2. **GO:0005886 plasma membrane (IDA, PMID:1438304)** — removed. The cited paper measures
   serotonin accumulation in transfected CV-1 cells and concludes the compartment is
   intracellular; ultrastructural work explicitly finds no VMAT2 on the plasma membrane
   (PMID:8753875). Recorded as a `source_defects` WRONG_TERM against RGD.
3. **GO:0071242 cellular response to ammonium ion (IEP, PMID:20534840)** — not removed.
   NH4Cl is the standard dequenching/alkalinizing reagent in pHluorin vesicle-recycling
   imaging, which is what that paper does, so the row most likely captures a reagent rather
   than a biological ammonium response. Full text is not cached, so this is
   MARK_AS_OVER_ANNOTATED with a `source_defects` CHECK (SUSPECTED) and an expert flag
   rather than a REMOVE.
4. **Mast-cell secretion terms (GO:0002552 / GO:0002553, ISO from mouse)** — kept but
   marked over-annotated: the rat paper that established VMAT2 histamine transport reports
   "the apparent absence of VMAT1 and VMAT2 in tissue mast cells" (PMID:8860238), a
   species/tissue mismatch with the mouse donor. Both carry `propagation_review` with
   CONTEXT_OR_TISSUE_MISMATCH.
5. **GO:0030073 insulin secretion (IDA)** — modified to GO:0050796 regulation of insulin
   secretion. VMAT2 does not secrete insulin; tetrabenazine studies show it modulates
   glucose-stimulated insulin release via beta-cell monoamine storage.
6. **GO:0032456 endocytic recycling (IEP)** — marked over-annotated. In PMID:20534840 VMAT2
   is the cargo whose recycling pathway is being read out; it is not shown to perform
   recycling.
7. **GO:0009791 post-embryonic development (ISO)** — marked over-annotated: the mouse
   donor rests on the perinatal failure of VMAT2-null animals, which is necessity, not
   participation in a developmental process.
8. **Amine "uptake" rows (serotonin / histamine / dopamine / norepinephrine uptake)** kept.
   Their definitions say "into a cell", and VMAT2 works on the vesicle membrane, but the
   assays behind them (PMID:1438304, PMID:8125935, PMID:8860238, PMID:20007701) measure
   amine accumulation by intact or permeabilized cells expressing VMAT2, so the claims are
   true as stated and the vesicle-specific process is carried separately by GO:0015842.
   There are vesicle-loading child terms for dopamine, tyramine and octopamine
   (GO:0160310/0160311/0160312) but none for serotonin or histamine — raised as a
   `suggested_questions` item rather than proposing new terms here.
9. **Generality refinements (MODIFY)**: GO:0005275 -> GO:0015311; GO:0006836 -> GO:0015842;
   GO:0008021 -> GO:0030672 (x2); GO:0030658 -> GO:0030672; GO:0031045 -> GO:0099012;
   GO:0044297 -> GO:0043025. Note that GO:0015311 is not currently an is_a descendant of
   GO:0005275 amine transmembrane transporter activity even though monoamines are amines —
   flagged as a question.
10. **GO:1901363 heterocyclic compound binding (IPI with CHEBI entities)** — marked
    over-annotated; serotonin and the inhibitor are substrate/ligand of the transport
    activity already asserted, and IPI with ChEBI `with` entries is the wrong evidence code
    (recorded as a `source_defects` CHECK against RGD).

No bioinformatics analysis was needed: the transport mechanism, substrate range,
topology and localization are all settled experimentally in rat.
