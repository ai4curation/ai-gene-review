# AAMP (angio-associated migratory cell protein) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider
(`AAMP-deep-research-affinage.md`, gates passed) plus UniProt Q13685, the GOA TSV and the
primary literature.

## The self-referential IBA — and why my first reading of it was wrong

`GO:0014909 smooth muscle cell migration` is annotated **twice** — once IBA, once IEP. The IBA's
WITH/FROM field is `PANTHER:PTN001068868|UniProtKB:Q13685`, and **`Q13685` is human AAMP
itself** — the very gene being annotated.

I first read this as circular: the inference seeded by the target's own annotation, transferring
nothing, and recorded it as `EVIDENCE_CIRCULAR_OR_REDUNDANT` / `CIRCULAR_PROPAGATION`.

**That was wrong**, and the repository maintainer corrected it on the PR: *"self-referential IBA
is valid. It means the curator has reviewed the source annotation and thinks it is a core
function, it makes sense evolutionarily (there will be an IBD further up the tree)."*

So the self-reference is not an artefact of the pipeline — it is a curation act. It records that
a PAINT curator inspected the source annotation, judged the function **core** rather than
peripheral, and found the assignment evolutionarily coherent. That is an *independent judgement
layered on* the experimental annotation, not a restatement of it. The correct root cause is
`NO_FAILURE_CORE`, and the review now says so.

Lesson worth carrying: an unusual-looking provenance pattern is not automatically a defect.
I inferred a failure mode from the *shape* of the WITH/FROM field without knowing what PAINT
curators actually do with it.

The second observation from that pair does stand, and the maintainer agreed with it
(*"However, IEP is a little suspect"*): the direct annotation is coded **IEP** (expression
pattern), which *understates*
   its own paper. PMID:18634987 is not an expression study: it reports
   [PMID:18634987, "The AAMP overexpression increases, while both treatment with anti-rAAMP-ab
   and transfection with siRNA decreases SMC migration."] plus in-vivo antibody blockade
   reducing neointima formation in apoE−/− mice. That is IMP-grade evidence. Flagged as a
   `suggested_question` for the responsible curator rather than silently re-coded here.

## What AAMP actually does — a Rho-family GTPase regulator

The GOA record describes AAMP through its *phenotypes* (migration, angiogenesis) and one
biochemical property (heparin binding). It has **no molecular function connected to the
mechanism**, which the modern literature has worked out in some detail:

- **RhoA.** AAMP binds RhoA directly and shields it from degradation
  [PMID:34901393, "AAMP stabilized RhoA by binding to it and suppressing its SMURF2-mediated
  ubiquitination and degradation."] — raising the active RhoA pool.
- **CDC42.** [PMID:33279622, "AAMP interacted with cell division cycle 42 (CDC42) and promoted
  its activation, resulting in the formation of cellular protrusions."] Affinage adds that this
  works by impeding the ARHGAP1–CDC42 interaction.
- **Pathway context.** [PMID:26350504, "Furthermore, we identified RhoA/Rho kinase signaling as
  an important factor that contributes to the action of AAMP in regulating endothelial cell
  migration and angiogenesis."] and, in smooth muscle,
  [PMID:18634987, "Knockdown of AAMP decreases RhoA activity in the membrane fraction of SMCs."]

Three independent groups, two GTPases, two cell types, consistent direction. This supports
three `NEW` annotations: `GO:0031267 small GTPase binding` (MF), `GO:0050821 protein
stabilization` and `GO:0051057 positive regulation of small GTPase mediated signal transduction`
(BP). Together they convert AAMP from "protein associated with migration" to a protein with a
stated mechanism.

**Term check worth recording:** `GO:0017048 Rho GTPase binding` would have been the more
specific MF, but a direct id lookup shows it is **obsolete**. `GO:0031267 small GTPase binding`
is the correct live term. (This check was added to the workflow after the AAGAB review, where
the reverse error — assuming a term was absent because a keyword search missed it — cost a
review round.)

## The `protein binding` annotations, again orthogonal to the biology

All four `GO:0005515` IPI annotations report the same partner: **AEN** (Q8WTP8), an
apoptosis-enhancing nuclease, from four large-scale interactome papers. There is no functional
follow-up and no described connection between AAMP and AEN.

Meanwhile **none of the four recovered RHOA, RHOB, CDC42 or NOD2** — every partner with
actual mechanistic follow-up. This is the third gene in this campaign (after AAGAB and AAMDC)
where the high-throughput binding record and the functionally characterised interactions are
disjoint sets. The pattern is worth naming: proteome-scale screens populate `GO:0005515` for
these genes without touching what is actually known about them.

Marked `MARK_AS_OVER_ANNOTATED` rather than `REMOVE` — four screens is real reproducibility,
and the pair may yet mean something.

## Localisation

Cytosol, cytoplasm, plasma membrane and cell surface are all annotated and all consistent with
UniProt [file:human/AAMP/AAMP-uniprot.txt, "SUBCELLULAR LOCATION: Cell membrane. Cytoplasm."].
The cell-surface/extracellular pool is genuine and functionally relevant — it is where heparin
binding and heparin-sensitive cell adhesion happen, and where the blocking antibody acts.

## Correction: GO:0017048 was merged, not obsoleted

The MF term choice rests on `GO:0017048 Rho GTPase binding` not being available, and my first
statement of why was imprecise. I ran an OLS lookup, got `label=GO_0017048, is_obsolete=true,
is_root=true`, and wrote "obsolete". The reviewer challenged that — reasonably, since a bare
CURIE-as-label plus `is_root: true` is also what you see for an id absent from the loaded
ontology slice — and suggested the term might be a live child of `GO:0031267`.

Checking QuickGO settles it, and **neither reading was right**:

```
GET /QuickGO/services/ontology/go/terms/GO:0017048
  -> id: GO:0031267   name: small GTPase binding   isObsolete: False
GET /QuickGO/services/ontology/go/terms/GO:0031267/complete
  -> secondaryIds: [GO:0005084, GO:0008536, GO:0017016, GO:0017031,
                    GO:0017048, GO:0017049, GO:0017137, GO:0017160,
                    GO:0030306, GO:0034989, GO:0048365]
  -> synonyms includes: "Rho GTPase binding"
```

`GO:0017048` was **merged into** `GO:0031267` — it is a secondary id, and "Rho GTPase binding"
survives as a synonym of the merged term. It is neither obsolete-and-detached nor a live child.
A QuickGO search for "Rho GTPase binding" returns no separate live term.

So the outcome is unchanged but the reason is better: **there is no Rho-specific binding term to
prefer**, because GO deliberately merged that granularity away. `GO:0031267` *is* that term now.

Method note for the campaign: OLS's response for a merged id is genuinely ambiguous — it reports
`is_obsolete: true` with a CURIE label. QuickGO's `/complete` endpoint, which lists
`secondaryIds`, distinguishes merged from obsoleted. Use it when a term-availability claim is
load-bearing.

## Actions

| Term | Evidence | Action |
|---|---|---|
| `GO:0014909` smooth muscle cell migration | IBA, IEP | ACCEPT (IBA flagged circular) |
| `GO:0010595` positive regulation of endothelial cell migration | ISS | ACCEPT |
| `GO:0008201` heparin binding | IDA | ACCEPT |
| `GO:0001525` angiogenesis | NAS | ACCEPT |
| `GO:0009986` cell surface | IDA | ACCEPT |
| cytosol / cytoplasm / plasma membrane | IEA, IDA, TAS | ACCEPT |
| `GO:0005515` protein binding ×4 (all AEN) | IPI | MARK_AS_OVER_ANNOTATED |
| `GO:0031267` small GTPase binding | IPI (proposed) | NEW |
| `GO:0050821` protein stabilization | IMP (proposed) | NEW |
| `GO:0051057` positive regulation of small GTPase mediated signal transduction | IMP (proposed) | NEW |
| `GO:1903141` negative regulation of establishment of endothelial barrier | IMP (proposed) | NEW |
| `GO:0070432` regulation of NOD2 signaling pathway | IMP (proposed) | NEW |

## Two further arms, added after review

- **Endothelial barrier (PMID:39404373).** siRNA depletion of AAMP *increases* trans-endothelial
  electrical resistance, so AAMP is a **negative** regulator of barrier function. The mechanism
  is the same Rho axis: depletion lowers RhoA and RhoB activity, reducing actomyosin contraction
  in resting endothelium. This paper is also the third independent lab to report AAMP-dependent
  Rho regulation, and it extends it to RhoB.
- **NOD2/NF-κB (PMID:19535145).** I had originally left this unannotated because the mechanism
  is unresolved. That conflated *mechanism* with *evidence*: GO regulation terms do not require a
  resolved mechanism, and the paper has overexpression plus siRNA in HEK293T. Annotated to the
  **unsigned parent** `GO:0070432`, because the paper says "modulates" and never establishes a
  direction — `GO:0070434`/`GO:0070433` would assert more than the data support.

**CD276/B7-H3 dropped from the review entirely** (description and the protein-binding summary). It came from the affinage narrative citing
PMID:35919070, which is neither cited nor cached here. An unverifiable partner should not sit in
a description.
