# cdsA (P0ABG1, *Escherichia coli* K-12) — curation notes

Branch: `cdsa-review`. Review target recorded as the outstanding gap in
[LIPID_DIVIDE](../../../projects/LIPID_DIVIDE.md) and in
`modules/bacterial_phosphatidic_acid_synthesis-notes.md`.

## Why this gene, and where it sits

`modules/bacterial_phosphatidic_acid_synthesis.yaml` deliberately ends at
phosphatidic acid (PA); `modules/bacterial_phosphatidylglycerol_cardiolipin_biosynthesis.yaml`
and `modules/bacterial_phosphatidylethanolamine_biosynthesis.yaml` both begin at
CDP-diacylglycerol (CDP-DAG). CdsA is the single reaction in that join and was
modelled in no bacterial module and reviewed in no bacterial gene folder (only
`genes/yeast/CDS1`). This review supplies the gene-level half of that join. It
does not create a module; that remains a curation item for the project page.

## Search log (2026-11-11)

No deep-research provider key is available, so no `-deep-research-<provider>.md`
file exists and none was authored by hand (CLAUDE.md forbids it).

- `just mod-description-deep-research ECOLI cdsA` → `cdsA skipped: no MOD
  provider configured for organism 'ECOLI'`. Expected: ECOLI is not one of the
  worm/fly/yeast MOD-description organisms.
- Sources actually used: the cached UniProt flat file `cdsA-uniprot.txt`
  (entry version 122, 04-NOV-2026), `cdsA-goa.tsv`, the four GOA-cited
  publications, and the four further UniProt-cited publications fetched here.
- PMIDs fetched this session with `uv run ai-gene-review fetch-pmid`:
  30718729 (full text from PMC), 30739787 (abstract only, no PMC record),
  30936205 (abstract only, full text not available from PMC), 2995358
  (abstract only, no PMC record).
- Local resources checked: `interpro/panther/PTHR46382/` (entries CSV +
  metadata; **no `-paint.tsv`**), `genes/yeast/CDS1/CDS1-goa.tsv` (for the
  sibling PAINT node), `grep -r PTN000349517` across the repository.

### Full-text limitation (stated because it bounds several rows)

All four GOA-cited publications are **abstract-only** in `publications/`
(`full_text_available: false`): PMID:2995359, PMID:30751 (PMC218635 returned
403 on fetch), PMID:6273438, PMID:15919996. Every `supporting_text` quoted from
them is therefore an abstract-level statement, and no claim in this review
depends on an unseen figure. Where the abstract does not settle a detail
(e.g. which detergent-solubilised fraction PMID:30751 assayed, or whether
PMID:15919996 reported a full topology model for b0175 rather than only the
C-terminal reporter result), the review defers to the curator rather than
second-guessing, per CLAUDE.md.

## Core biology

CdsA is the CDP-diacylglycerol synthase of *E. coli*: it activates phosphatidic
acid with CTP to give CDP-diacylglycerol plus pyrophosphate
[file:ECOLI/cdsA/cdsA-uniprot.txt, CC:CATALYTIC ACTIVITY, "a 1,2-diacyl-sn-glycero-3-phosphate + CTP + H(+) = a CDP-1,2-"].
UniProt places it at "step 3/3" of CDP-diacylglycerol biosynthesis from
sn-glycerol 3-phosphate [file:ECOLI/cdsA/cdsA-uniprot.txt, CC:PATHWAY].

- **Purified enzyme.** Sparrow & Raetz purified it to ~90% homogeneity from an
  overproducing strain [PMID:2995359, "has been purified to 90% homogeneity from Escherichia coli cells"],
  established a sequential (not ping-pong) mechanism and surface-dilution
  kinetics in Triton X-100 [PMID:2995359, "The pure enzyme displays surface dilution kinetics when assayed in the presence of Triton X-100."],
  and matched the amino-acid composition to the *cds* gene product of the
  companion cloning paper [PMID:2995358].
- **Earlier partial purification.** Langley & Kennedy solubilised the activity
  from the cell envelope with digitonin and purified it ~70-fold
  [PMID:30751, "was solubilized from the cell envelope by a differential extraction procedure involving the detergent digitonin"].
  The same enzyme uses CTP and dCTP competitively, making both CDP- and
  dCDP-diglyceride [PMID:30751, "It therefore appears that a single enzyme catalyzes synthesis of both CDP-diglyceride and"],
  and catalyses the reverse pyrophosphorolysis
  [PMID:30751, "The enzyme also catalyzes a pyrophosphorolysis of"]. UniProt
  records the physiological direction as left-to-right (PA → CDP-DAG)
  [file:ECOLI/cdsA/cdsA-uniprot.txt, CC:CATALYTIC ACTIVITY, "PhysiologicalDirection=left-to-right"],
  so the reverse reaction is an in vitro property, not a second function.
- **In vivo requirement.** Conditionally lethal *cds* mutants accumulate PA to
  ~30% of membrane lipid above pH 8 while PE and PG synthesis stops
  [PMID:6273438, "Above pH 8, GN80 accumulates phosphatidic acid to about 30% of the total membrane lipid"],
  which the authors call "definitive physiological proof that CDP-diglyceride is
  an obligatory precursor for over 90% of the phosphatidylethanolamine and
  phosphatidylglycerol". The gene is essential and cannot be deleted
  [file:ECOLI/cdsA/cdsA-uniprot.txt, CC:DISRUPTION PHENOTYPE].

## Topology and location

UniProt: "Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane
protein {ECO:0000255}", eight predicted helical TRANSMEM segments, and one
experimentally determined `TOPO_DOM 285 /note="Periplasmic"
/evidence="ECO:0000269|PubMed:15919996"` from the Daley et al. global
C-terminal-reporter study [PMID:15919996, "we established the periplasmic or cytoplasmic locations of the C termini for 601 inner membrane proteins"].

In a diderm bacterium the inner (cytoplasmic) membrane **is** the plasma
membrane, so `GO:0005886` is the right CC term and `GO:0016020` membrane is a
strict parent of it. The integral/multi-pass character has two independent
lines: the experimental C-terminal topology assignment above, and the
biochemistry — the protein required a different detergent at every purification
step, "illustrating the refractory hydrophobic nature of this protein"
[PMID:2995359], and had to be extracted from the cell envelope with digitonin
[PMID:30751]. That supports adding `GO:0005887` integral component of plasma
membrane as an IC row beside the root rows, which is what the review does. It
does **not** support a side-of-membrane term: the single experimental topology
datum is the C-terminus, and the catalytic site has not been localised to a
face.

No magnesium, metal-binding or lipid-binding row exists in GOA, and the UniProt
record has no BINDING, metal or ACT_SITE features at all. The 1985 purification
reports "Apparent physical effects of EDTA on the enzyme" [PMID:2995359] but
does not establish a catalytic metal requirement for the *E. coli* enzyme, so
nothing about Mg(2+) is asserted here. (Structural work on the *Thermotoga*
CdsA establishing a bound metal was not checked and would be a separate review.)

## The MPIase branch — a second, genuinely downstream role

Three papers from the Nishiyama group, all cited by UniProt's FUNCTION with
ECO:0000269, implicate CdsA in biosynthesis of MPIase, the glycolipid
"membrane protein integrase" of the *E. coli* inner membrane.

- Cytidine deprivation lowers MPIase; CdsA overproduction raises CdsA and
  MPIase ~3-fold [PMID:30718729, "we observed a ~3-fold increase in both the CdsA and MPIase levels"].
- Inverted membrane vesicles from CdsA overproducers, and partially purified
  CdsA8 (Y207H), convert [14C]PA + CTP + GlcNAc-1-phosphate into compound I
  (GlcNAc-PP-DAG), identified against a synthetic reference by TLC in two
  solvent systems and by LC-MS/MS; CDP-DAG appears to stay on the enzyme
  [PMID:30718729, "These observations strongly suggest that CDP-DAG is synthesized and then converted to compound I on CdsA."].
- *cdsA* depletion abolishes detectable MPIase and blocks M13 procoat
  processing [PMID:30718729, "We found that MPIase was hardly detected in both the cdsA and cdsA/ynbB knockouts"].
- The paralogue YnbB restores MPIase but not phospholipid synthesis under CdsA
  depletion, i.e. it is "dedicated to MPIase biosynthesis"
  [PMID:30739787]; and both genes are described as "rate-limiting enzymes for
  MPIase biosynthesis" controlling the cold-induced rise in MPIase
  [PMID:30936205].

**Why this gets a NEW process row and not a NEW molecular function.**
Against CLAUDE.md's `NEW` bar, the entity performing the GlcNAc-1-phosphate
transfer step is reported to be CdsA itself, not another gene product, so this
is participation rather than the "my gene is merely required" pattern. The
process term asserted is `GO:0009247` glycolipid biosynthetic process (IMP,
PMID:30718729): the depletion result is the cleanest evidence, and MPIase has no
GO term of its own. What is **not** asserted:

- No MF term for compound I (GlcNAc-PP-DAG) synthase activity, and no
  `proposed_new_terms` entry for one. The chemistry was shown with inverted
  vesicles and with a *mutant* enzyme (CdsA8, Y207H) at non-permissive high pH,
  from one group; and YnbB, not CdsA, is the paralogue said to be dedicated to
  the branch. Proposing a GO term would commit the ontology to a division of
  labour the data do not yet settle. This is recorded as a BIOLOGY knowledge gap
  with a paired experiment instead.
- No protein-integration or protein-translocation process term. CdsA makes a
  lipid; MPIase is what acts on the substrate protein. Annotating CdsA to
  `GO:0032978`-type integration terms would be exactly the necessity-for-the-
  outcome error the `NEW` bar warns about.

## Lineage check (asked for explicitly)

- The IBA rows carry `PANTHER:PTN000349517|UniProtKB:P0ABG1`. The sibling node
  used for the eukaryotic CDS enzymes is **PTN000349519** (seen in
  `genes/yeast/CDS1/CDS1-goa.tsv`, seeded by human CDS1/CDS2, *Drosophila*,
  mouse, rat, *S. pombe* and plant genes). The two are distinct nodes in the
  same family, PTHR46382, so the *E. coli* rows are **not** eukaryotic
  propagations.
- `PTN000349517` appears nowhere in the repository except this gene's GOA and
  review, and `interpro/panther/PTHR46382/` contains only `-entries.csv` and
  `-metadata.yaml`, **no `-paint.tsv`**. So the IBD at the node cannot be read
  locally and its exact placement is not asserted here; the node is cited only
  as the GOA WITH/FROM value, never with an invented label or clade claim.
- PTHR46382 membership of P0ABG1 is confirmed independently from the protein's
  own `DR PANTHER; PTHR46382; PTHR46382:SF1` line and from
  `PTHR46382-entries.csv`, which lists P0ABG1 (and *B. subtilis* O31752,
  *Aquifex* O67292, *Chlamydia* O84457) under subfamily SF1.
- **P0ABG1 in its own WITH/FROM is expected, not circular** (CLAUDE.md): the
  gene's EXP/IDA annotations are among the descendant evidences the PAINT
  curator used. No row is marked `CIRCULAR_OR_REDUNDANT`.
- **No row conflates CdsA with eukaryotic CDS1/CDS2 or with Tam41.** Tam41 is
  the unrelated mitochondrial CDP-DAG synthase and appears in no WITH/FROM here;
  it is relevant only as a complementation tool in PMID:30718729 (and that paper
  also shows human and yeast Cds1p complementing Δ*cdsA* when co-expressed with
  Tam41p, which is convergent chemistry, not shared ancestry with Tam41).

## Decisions on the 14 GOA rows

| Term | Evid | Ref | Action |
|---|---|---|---|
| GO:0004605 | EXP | PMID:2995359 | ACCEPT — purified enzyme, EC 2.7.7.41 |
| GO:0004605 | IDA | PMID:30751 | ACCEPT — partially purified activity |
| GO:0004605 | IBA | GO_REF:0000033 | ACCEPT — node inside family, own EXP among seeds |
| GO:0004605 | IEA | GO_REF:0000120 | ACCEPT — Rhea/EC mapping matches the assayed reaction |
| GO:0016024 | IDA | PMID:30751 | ACCEPT (+ WRONG_QUALIFIER defect) |
| GO:0016024 | IMP | PMID:6273438 | ACCEPT — PA accumulation, liponucleotide pool collapse |
| GO:0016024 | IBA | GO_REF:0000033 | ACCEPT |
| GO:0016024 | IEA | GO_REF:0000041 | ACCEPT — UniPathway UPA00557 |
| GO:0005886 | IDA | PMID:15919996 | ACCEPT — inner membrane proteome/topology |
| GO:0005886 | IDA | PMID:30751 | ACCEPT — activity in the cell envelope |
| GO:0005886 | IBA | GO_REF:0000033 | ACCEPT — `is_active_in`; the chemistry is membrane-embedded |
| GO:0005886 | IEA | GO_REF:0000044 | ACCEPT — SL-0037 cell inner membrane |
| GO:0016020 | IEA | GO_REF:0000002 | MODIFY → GO:0005886 (already carried) |
| GO:0016772 | IEA | GO_REF:0000002 | MODIFY → GO:0004605 (already carried) |

Plus two `NEW` rows: `GO:0005887` (IC) and `GO:0009247` (IMP, PMID:30718729).

Nothing is REMOVEd. Every row here is a true claim about the gene; the two
MODIFYs are refinements to terms the gene already carries, as CLAUDE.md
directs, not deduplication.

## Qualifier defect

The two EcoCyc `GO:0016024` rows use `acts_upstream_of_or_within`. For the IDA
row (PMID:30751) that is too weak: CdsA *performs* the committed reaction of
CDP-DAG biosynthesis, so `involved_in` is the right qualifier. Recorded as a
`WRONG_QUALIFIER` source defect against ECOCYC on that row (confidence
PROBABLE, since we cannot see the full text the curator used and the IMP row's
mutant-phenotype evidence can justify the weaker qualifier).

## Not verified

- PMC218635 (full text of PMID:30751) returned 403; worked from the abstract.
- The PAINT IBD at PTN000349517 (no local `-paint.tsv` for PTHR46382).
- Any structural/metal work on CdsA orthologues; no metal claim is made.
- Whether the compound I synthase step is CdsA's own active site in the wild-
  type enzyme in vivo (see the knowledge gap).
