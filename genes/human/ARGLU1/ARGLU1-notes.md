# ARGLU1 (human, Q9NWB6) — review notes

Working notes for the GO annotation review. Provenance is inline as
`[PMID:xxxxxx "verbatim supporting text"]`. Computed claims point at
[`ARGLU1-bioinformatics/RESULTS.md`](ARGLU1-bioinformatics/RESULTS.md) and the
JSON artefacts beside it.

## 1. What kind of gene this is

ARGLU1 is frequently described as uncharacterised, and the 2024 primary
literature still says so: *"Arginine and glutamate rich 1 (ARGLU1) is a poorly
understood cellular protein with functions in RNA splicing and transcription"*
and *"Computational prediction suggests that ARGLU1 contains intrinsically
disordered regions and lacks any known structural or functional domains"*
[PMID:38520408].

But "uncharacterised" and "over-annotated" are different diagnoses, and this gene
is neither, exactly. UniProt marks it `PE 1: Evidence at protein level`, and
there are six primary papers that manipulate the protein and read out a
phenotype. What is genuinely absent is *structural* and *mechanistic* information:
no experimental structure, no catalytic activity, and — measured, not assumed —
**no domain signature of any kind**. The complete signature content of the
Swiss-Prot entry is `IPR033371` (the ARGLU1 family itself), `PF15346` (which
InterPro types as `coiled_coil`, not `domain`) and `PTHR31711:SF1`
(`composition.json`).

So the warning that motivated this review is well founded: *arginine- and
glutamate-rich is a composition, not a function*, and there is nothing in the
fold to reverse-engineer a molecular function from. Every MF claim below rests on
an experiment.

The composition itself is real and sharply partitioned
(`composition_and_features.py`, `composition.json`):

| region (UniProt, `ECO:0000269|PubMed:30698747`) | R | K | R+K | E | E+D | S | RS dipeptides |
|---|---|---|---|---|---|---|---|
| 1–74, "Necessary and sufficient for RNA binding" | 33.8% | 12.2% | 46.0% | 6.8% | 9.5% | 27.0% | 12 RS / 12 SR, longest alternating run 8 |
| 75–273, "Necessary and sufficient for transcriptional regulation" | 14.1% | 12.1% | 26.2% | 24.6% | 27.1% | 4.0% | 1 |

The primary paper describes the same partition: *"The two domains of ARGLU1 have
opposing charges with positively charged arginine residues at the N-terminus and
an abundance of negatively charged glutamate residues at the C-terminus."*
[PMID:30698747].

One thing the composition analysis adds that the literature does not say
explicitly: the N-terminal region is not merely arginine-rich, it is a genuine
**RS-repeat (SR-protein-like) region** — 12 RS plus 12 SR dipeptides with an
unbroken 8-dipeptide alternating run. Three of UniProt's six annotated
phosphoserines/threonines (Ser-58, Ser-60, Thr-61) sit inside it. That matters in
§5.

## 2. The two experimentally separable activities

**Transcription coactivation — C-terminal region.** The gene was found in a
screen for modulators of glucocorticoid signalling, and domain-swap reporter
assays localise the activity: *"These studies revealed that the construct
containing only the C-terminus (ARGLU1C-term) retained the ability to coactivate
GR, comparable to that of the full-length protein; whereas, the construct
containing only the N-terminus (ARGLU1N-term) did not (Figure 2B)."*
[PMID:30698747]. It is not GR-specific — *"To test whether ARGLU1 can coactivate
other members of the NR superfamily, we used the GAL4-NR-LBD/UAS-luciferase
system."* [PMID:30698747] — and it is co-operative rather than autonomous: *"we
observed a synergistic increase in ligand-induced luciferase activity (Figure
2A), implying that ARGLU1 forms a complex with other coactivators and GR to
regulate gene expression."* [PMID:30698747].

The earlier paper reached the same place from the estrogen receptor:
*"We found that ARGLU1 (arginine and glutamate rich 1) not only colocalizes with
MED1 in the nucleus, but also directly interacts with a far C-terminal region of
MED1."* and *"Importantly, ARGLU1 is recruited, in a ligand-dependent manner, to
endogenous estrogen receptor target gene promoters and is required for their
expression."* [PMID:21454576].

**A useful negative.** The obvious mechanistic guess — that the coactivation runs
through the LXXLL motifs — was tested and failed. UniProt records the mutagenesis
as `LLEEL->AAEEA: Does not disrupt nuclear receptor coactivator activity` and the
paper concludes: *"These data suggest that while the C-terminal domain is
important for activation, these motifs alone cannot account for the ARGLU1
mediated transactivation of GR, thus, other non-canonical interactions are likely
involved."* [PMID:30698747]. This is worth stating in the review because a
domain/motif-name-derived mechanism is exactly the failure mode this gene invites.

**Splicing regulation and RNA binding — N-terminal region.** In vitro:
*"Computational analysis of the microarray data found full length ARGLU1
preferentially bound to CGG(A/G)GG type k-mers (Figure 3C, Supplementary Figure
S9)."* [PMID:30698747]. In cells, by cross-linking RIP: *"Our results showed that
full-length ARGLU1 and ARGLU1N-term (but not ARGLU1C-term) pulldowns enrich Lpin1
and Bin1 pre-mRNA (both are alternatively spliced in an ARGLU1-dependent manner
and contain G-rich sequences near ARGLU1-dependent splice sites) (Supplementary
Figure S9E)."* [PMID:30698747]. With a specificity control: *"In contrast, Brwd3
pre-mRNA (undergoes ARGLU1-dependent AS but does not contain G-rich sequences
near splice sites) is not enriched (Supplementary Figure S9E)."* [PMID:30698747].

The authors' own summary of the division of labour: *"Biochemical studies
determined that ARGLU1 interacts with GR through its C-terminal domain; whereas,
the N-terminal domain mediates interactions with splicing factors and contributes
to both basal and GC-dependent splicing outcomes."* [PMID:30698747].

## 3. The partner set is coherent, not screen noise

GOA carries ten `GO:0005515` rows naming four partners. The partner audit
(`intact_partner_audit.py`, `intact_partners.json`) ran the three checks this
campaign has standardised, and **two of them came back negative** — which is
itself the finding:

1. **Canonicality — no defect.** All four (SRPK2 `P78362`, U2AF2 `P26368`,
   PUF60 `Q9UHX1`, JMJD6 `Q6NYC1`) resolve to reviewed Swiss-Prot entries at
   canonical length. No unreviewed partial-ORFeome substitution.
2. **Topological plausibility — no defect.** All four are nuclear, and SRPK2 is
   itself annotated to nuclear speckles, the compartment ARGLU1 occupies. The
   partner set reflects ARGLU1's biology, not a bait panel's design.
3. **`NbExp` inflation — mixed.** SRPK2's three rows are three *orthogonal*
   methods from three independent labs (in vitro kinase assay, yeast two-hybrid,
   AP-MS), so `NbExp=3` is honest here. JMJD6's five rows are all `anti tag
   coip`, three of them spoke-expanded BioPlex rows from two releases of one
   pipeline.

U2AF2, PUF60 and JMJD6 have directed, reciprocal evidence in the primary paper:
*"The MS results were confirmed with co-IP western blotting experiments in which
ARGLU1 was found to interact with PUF60, U2AF2 and JMJD6 (Figure 3B)."* and
*"Reverse IPs with the FLAG antibody led to the HA-ARGLU1 being pulled down with
FLAG-PUF60 and FLAG-U2AF2."* [PMID:30698747]. Their identity is mechanistically
apt: *"PUF60 and U2AF2 (also known as U2AF65) bind polypyrimidine tract sequences
adjacent to 3′ splice sites and facilitate the recruitment of U2 snRNP during
spliceosome assembly, whereas JMJD6 is an enzyme which has been found to
hydroxylate U2AF2 and alter its activity (35–37)."* [PMID:30698747].

## 4. Two rows that do not survive

### 4a. `GO:0005739` mitochondrion (IBA) — a *Candida* Mediator-tail paralog

This is the review's main curation finding, and the argument is entirely
measured (`panther_node_audit.py`, `results.json`).

ARGLU1 receives `GO:0005654` nucleoplasm and `GO:0005739` mitochondrion by IBA
**from the same PANTHER node**, `PTN001271790`. The node's reach is identical for
both — 111 gene products across 64 taxa. The donor pools are not:

| term | donors with their own experimental evidence |
|---|---|
| `GO:0005654` nucleoplasm | 3 — human ARGLU1, mouse Arglu1, *Drosophila* Arglu1, all Swiss-Prot ARGLU1 orthologs |
| `GO:0005739` mitochondrion | **1** — *Candida albicans* **TLO16** (`A0A1D8PRM3`, TrEMBL), IDA from `PMID:22923044` |

All 111 mitochondrion rows name `CGD:CAL0000179812` in WITH/FROM, so the entire
family's mitochondrial annotation — plants, green algae, *Selaginella*,
*Marchantia*, *Trichoplax*, *Daphnia*, all vertebrates — rests on that one
protein.

TLO16 is not an ARGLU1 ortholog in architecture. InterPro gives it
`IPR021017` *Mediator complex, subunit Med2, fungi* (`PF11214`) and `IPR027267`
AH/BAR superfamily **in addition to** `IPR033371`; human ARGLU1 has only
`IPR033371`. And the source paper restricts the localisation to one clade of a
lineage-specific expansion: *"The telomere-associated TLO gene family underwent a
recent expansion from one or two copies in other CUG clade members to 14 expressed
copies in C. albicans."*; *"The 14 expressed TLO gene family members have a
conserved Med2 domain at the N terminus, suggesting a role in general
transcription."*; *"clade α and clade β have no introns and encode proteins that
localize primarily to the nucleus; clade γ sometimes undergoes splicing, and the
gene products localize within the mitochondria as well as the nuclei."*
[PMID:22923044].

So the localisation is not even uniform across the TLO family inside one species,
let alone across eukaryotes. Human ARGLU1 has no mitochondrial evidence of any
kind: its UniProt `SUBCELLULAR LOCATION` is Nucleus / Nucleus speckle /
Chromosome, and all four of its experimentally supported CC terms are nuclear.

**Divergence noted deliberately:** 213 merged reviews in this repo carry a
`GO:0005739` IBA row and their modal verdict is `ACCEPT` (127)
(`sibling_verdicts.json`). This review removes it anyway, because for most of
those genes the donor pool is genuinely mitochondrial and here it is one
*Candida* TLO protein. The corpus trend is not an argument about this node.

### 4b. `GO:0045296` cadherin binding (HDA) — proximity read as binding

`PMID:25468996` is a proximity-biotinylation study: *"We used proximity
biotinylation and quantitative proteomics to identify 561 proteins in the
vicinity of the cytoplasmic tail of E-cadherin."* [PMID:25468996]. The assay
measures proximity within the labelling radius; the paper says *"in the vicinity
of"*, and the annotation says *binds cadherin*.

Scope, measured (`reference_scope_audit.py`, `reference_scope.json`): that one
reference produced **272 `GO:0045296` annotations over 272 distinct gene
products**, 271 of them HDA, all assigned by `BHF-UCL`. The control in the same
table is the ARGLU1 primary paper, which annotates **4** gene products.

ARGLU1 is nuclear in every curated location it has. Nothing else in its
literature places it at a junction.

Corpus check (`sibling_verdicts.json`): 38 merged reviews carry this exact row;
verdicts are `MARK_AS_OVER_ANNOTATED` 21, `KEEP_AS_NON_CORE` 11, `REMOVE` 3,
`UNDECIDED` 1, `ACCEPT` 1, `PENDING` 1. This review takes the modal
`MARK_AS_OVER_ANNOTATED` rather than `REMOVE`, for consistency — the interaction
data are not being called false, only the binding term unsupported.

## 5. The autoregulatory sisRNA circuit, and what GO does not capture

Two papers establish that ARGLU1 controls its own expression through its own
pre-mRNA. *"We demonstrate that the ARGLU1 gene expresses at least three distinct
RNA splice isoforms - a fully spliced isoform coding for the protein, an isoform
containing a retained intron that is detained in the nucleus, and an isoform
containing an alternative exon that targets the transcript for nonsense mediated
decay."* and *"Further, overexpression of the ARGLU1 protein shifted the splicing
of endogenous ARGLU1 mRNA, resulting in an increase in the retained intron
isoform and nonsense mediated decay susceptible isoform and a decrease in the
fully spliced isoform."* [PMID:27899669].

The second paper closes the loop with the RNA product: *"Mechanistically, Arglu1
sisRNA represses the splicing-inhibitory activity of ARGLU1 protein by binding to
ARGLU1 protein and promoting its localization to nuclear speckles, away from the
Arglu1 gene locus."* [PMID:36533631]. It also makes the human-vs-fly distinction
explicit — *"In humans, Arglu1 sisRNA retains the entire intron 2 and promotes
host gene splicing. … In contrast, Drosophila dArglu1 sisRNA forms via premature
cleavage of intron 2 and represses host gene splicing."* [PMID:36533631] — which
is worth holding onto, because the fly ortholog is a WITH/FROM donor on the
nucleoplasm IBA and its sisRNA mechanism is *not* the human one.

Two GO consequences:

- ARGLU1 binds a **stable intronic sequence RNA**, i.e. a non-coding RNA, not a
  pre-mRNA. GOA carries only `GO:0036002` pre-mRNA binding. The sisRNA binding is
  a separate, experimentally supported RNA-binding event and the honest parent is
  `GO:0003723` RNA binding.
- The sisRNA circuit's *direction* on the host gene is repressive — the protein
  promotes intron retention and NMD of its own transcript — which `GO:0000381`
  (unsigned) does not express. `GO:0048025` negative regulation of mRNA splicing,
  via spliceosome does.

**Speculative, flagged as such:** SRPK2 phosphorylates ARGLU1 in vitro (IntAct
types the `PMID:23602568` record as `phosphorylation`, method `protein kinase
assay`, host `In vitro`), ARGLU1's N-terminus is a bona fide RS-repeat region
(§1), and SRPK-family kinases control nuclear-speckle partitioning of RS-domain
proteins. That is a coherent hypothesis for how speckle localisation is set — but
no paper has tested it on ARGLU1, so it goes to `suggested_experiments`, not to a
GO term. A second kinase input is now published: *"we identified and confirmed
that PAK1 phosphorylated ARGLU1 at Ser 77"* [PMID:42641889], which is the same
Ser-77 that five independent phosphoproteomics studies report in UniProt.

## 6. Provider record (affinage) — what it got right and what it missed

`gates_passed: true`, 11 citations, all numeric PMIDs (no `PMID:bio_*` preprint
ids). The narrative is broadly accurate and its mechanistic claims match UniProt
and the primary papers. Two problems:

1. **It cites a RETRACTED paper without flagging it.** `PMID:35082911`
   ("miR-335-5p Inhibits Progression of Uterine Leiomyoma by Targeting ARGLU1")
   is `Retracted Publication` with `RetractionIn: PMID:37503407`. The affinage
   record lists it as a "Medium" confidence dated finding with no flag. Nothing in
   this review rests on it; it is recorded in `references` with
   `is_invalid: true`. (Separately, `PMID:39251607` — a GOA IPI reference —
   carries an erratum, `PMID:39468017`; noted, and nothing load-bearing depends on
   the erratum's scope.)
2. **Recall.** A PubMed search for `ARGLU1` returns **28** records; affinage
   returned 11. Of the 17 it did not return, one is substantive and post-dates
   nothing in the record: `PMID:42641889` (2026), which identifies ARGLU1 as a
   PAK1 substrate phosphorylated at Ser-77 and shows an S77A mutant lowers E-box
   promoter activity and MCM gene expression. Also missing: `PMID:42346151` (2026,
   ARGLU1 in glioma) and `PMID:33165823` (miR-3613-3p). This is the expected
   shape — `gates_passed` is a precision gate with no recall component.

## 7. Term choices checked before use

- `GO:0030374` "nuclear receptor coactivator activity" is **obsolete** (QuickGO
  `isObsolete: true`). It is the term a reader would reach for given that ARGLU1's
  best-characterised activity is nuclear-receptor-specific. `GO:0003713`
  transcription coactivator activity, which GOA already carries, is the correct
  and maximal term. No `proposed_new_terms` entry to re-create it.
- `GO:0035259` "nuclear glucocorticoid receptor binding" is also **obsolete**;
  `GO:0016922` nuclear receptor binding absorbed `GO:0035257` and `GO:0035258`
  and has **no children**, so it is already maximal for "binds GR".
- There is **no** "regulation of transcription pausing" term. `GO:0160239`
  transcription pausing by RNA polymerase II exists but has no children and no
  regulation-level parent for this purpose; the expressible claim is
  `GO:0034243` / `GO:0034244` at the elongation level. Recorded as a knowledge
  gap rather than forced.
- **`GO:1990935 splicing factor binding` exists, and an earlier draft of this
  review wrongly said it did not.** The draft searched for *"spliceosomal complex
  binding"*, which returns only CC and BP terms, and concluded on that basis that
  all six U2AF2/PUF60/JMJD6 rows had no informative MF to be modified into. GO's
  search is **token-based**: *spliceosomal complex* is not a token of *splicing
  factor*, so that query could never have returned the term no matter how it was
  phrased. Verified by walking the ontology instead — `GO:1990935` is active, MF,
  defined as *"Binding to a protein involved in the process of removing sections
  of the primary RNA transcript to form the mature form of the RNA"*.

  Which partners qualify was then settled by measurement rather than by the
  partners' reputations — QuickGO annotations under `GO:0008380` RNA splicing:

  | partner | annotations under RNA splicing | verdict |
  |---|---|---|
  | U2AF2 `P26368` | **IDA** to `GO:0000398`, plus NAS/IC/IBA/IEA | splicing factor → `GO:1990935` |
  | PUF60 `Q9UHX1` | 2 × IBA | splicing factor → `GO:1990935` (weaker support, recorded) |
  | JMJD6 `Q6NYC1` | **zero** | *not* a splicing factor → term withheld, row stays `REMOVE` |
  | SRPK2 `P78362` | 2 × IDA | also a splicing factor, but the in vitro kinase assay makes `GO:0019901` the better-evidenced call |

  So five rows became `MODIFY` and the two JMJD6 rows keep `REMOVE` — now on a
  JMJD6-specific measured ground (an oxygenase that hydroxylates a splicing factor
  is not itself one) rather than on a false general claim. The lesson is the
  AHSP one and I walked straight into it: **a failed keyword search is not
  evidence that a term is absent.** Walk the ontology; search the compound word,
  not only the fragment.

## 8. Row-count reconciliation

`ARGLU1-goa.tsv` has **29** data rows (30 lines, one header). The `fetch-gene`
stub seeded **28** `existing_annotations`. The missing row is the second
`GO:0005515` / `IPI` / `PMID:30698747` / `UniProtKB:P26368` row — GOA has two,
one assigned by `IntAct` and one by `UniProt`, and the stub's seed key ignores
`ASSIGNED BY` so they collapsed. Restored, giving 29 reviewed existing rows plus
the review's own `NEW` proposals.
