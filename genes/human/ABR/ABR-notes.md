# ABR (human, Q12979) — review notes

PAINT + affinage campaign. 32 GOA rows, all reviewed; 3 new annotations proposed.

## Provenance of this file

An earlier session did the research for this gene and wrote it up here, but never
transcribed any of it into `ABR-ai-review.yaml` — that file was still the untouched
`fetch-gene` stub (`status: INITIALIZED`, all 32 rows `action: PENDING`). Nothing was
lost, but nothing was finished either. This file has been rewritten after re-verifying
the earlier claims; two of them turned out to be wrong and are corrected below under
"Corrections to the earlier draft".

## What the protein is

859 aa, brain-enriched, chromosome 17p. Domain string (UniProt FT): DH 91-284,
PH 301-459, C2 484-613, Rho-GAP 647-845, with the catalytic arginine finger at R683
[file:human/ABR/ABR-uniprot.txt "Arginine finger"]. So one polypeptide carries a
GEF module and a GAP module acting on the same GTPase family in opposite directions.

Residues confirmed directly against the SQ block: 683 = R, 795 = N, 859 = V, and
683/795 both fall inside the annotated Rho-GAP domain (647-845).

ABR is the paralog of BCR and lacks BCR's N-terminal oligomerisation/serine-threonine
kinase region — stated in three independent places: "The Abr protein is very similar to
Bcr but lacks a structural domain which may influence its biological regulatory
capabilities" [PMID:7479768], "ABR lacks homology to the serine/threonine kinase domain
of BCR" [PMID:8349582], and "it lacks the N-terminal BCR protein kinase domain"
[PMID:8262969]. That missing region is why a naive paralog transfer from BCR is hazardous.
In practice the BCR-specific biology (kinase region, everything downstream of BCR-ABL)
has **not** leaked into ABR's GOA — the paralog hazard is present in the evidence graph
but has not produced a wrong annotation.

## The defining biochemistry (PMID:7479768, Chuang et al. 1995)

Recombinant domains, purified **separately** — this matters, see the Amin reconciliation
below: "We purified as recombinant fusion proteins the GAP- and Dbl-homology domains of
both Abr and Bcr" [PMID:7479768].

- **DH/GEF domain**: stimulates GTP binding to CDC42Hs, RhoA, Rac1, Rac2
  (rank order CDC42Hs > RhoA > Rac1 = Rac2); inactive toward Rap1A and Ha-Ras.
- **GAP domain**: acts on Rac1, Rac2, CDC42Hs; **inactive toward RhoA**, Rap1A, Ha-Ras.
- "Each individual domain bound in a noncompetitive manner to GTP-binding protein
  substrates" [PMID:7479768] — so ABR can engage two GTPases at once.

[PMID:7479768 "The Dbl-homology domains of Bcr and Abr were active in stimulating GTP binding to CDC42Hs, RhoA, Rac1, and Rac2 (rank order, CDC42Hs > RhoA > Rac1 = Rac2) but were inactive toward Rap1A and Ha-Ras. Both Bcr and Abr acted as GAPs for Rac1, Rac2, and CDC42Hs but were inactive toward RhoA, Rap1A, and Ha-Ras."]

Both 1993 papers had already shown the isolated domain has Rac-directed GAP activity
[PMID:8349582 "A domain of ABR with similarity to GAPrho was expressed as a fusion protein in Escherichia coli and was shown to have GAP activity toward rac."]
[PMID:8262969 "The ABR GAP domain expressed as an Escherichia coli fusion protein was active against Rac1 and Cdc42 of the rho subfamily."].

Note the second of these matters for evidence-code purposes: the `GO:0005096` TAS row
citing PMID:8262969 is actually backed by a direct assay *in that paper*, so it is better
supported than TAS implies.

**The GAP activity is not merely licensed by the domain name.** UniProt records
experimental mutagenesis: R683A "Reduces GAP activity", and R683A+N795A causes "Loss of
GAP activity", both `ECO:0000269|PubMed:17116687`. So the arginine finger is confirmed by
mutation, not just transferred by a PROSITE rule (`ECO:0000255`). Per the campaign brief's
rule on domain-name-as-activity in both directions, this is the "residues intact AND
tested" case — neither an unsupported prior nor an untested one.

## The central curation finding: GO's MF/BP asymmetry is biologically right here

Substrate specificity is no longer expressible in the GO **molecular function** branch:

- `GO:0005099` (Ras), `GO:0005100` (Rho), `GO:0030675` (Rac) GTPase activator activity
  are all **secondary ids of `GO:0005096`**, which has **no substrate-specific children**
  (only `GO:1902773 GTPase activator complex` via `capable_of`).
- `GO:0005089` (Rho) and `GO:0030676` (Rac) guanyl-nucleotide exchange factor activity are
  secondary ids of `GO:0005085`.
- `GO:0017048` (Rho) and `GO:0048365` (Rac) GTPase binding are secondary ids of
  `GO:0031267`, along with `GO:0017137` (Rab).
- **Also true on the process side**, which the earlier draft missed: `GO:0032856`–`GO:0032864`,
  the substrate-specific "activation of X GTPase activity" terms, are all secondary ids of
  `GO:0090630`, which now has no children at all.

All checked with QuickGO `/ontology/go/terms/<id>/complete`, reading `secondaryIds` —
OLS reports a MERGED id and an ABSENT id identically, so that endpoint is the one that
settles it.

So ABR is annotated identically to a GAP that is Rho-specific and Rac-inert. **But the
merge turns out to be well-founded**, and that is the interesting part. Amin et al. 2016
assayed 14 RHOGAPs against 12 RHO proteins and concluded:

[PMID:27481945 "We have found that the RHOGAP domain itself is nonselective and in some cases rather inefficient under cell-free conditions."]
[PMID:27481945 "we propose that other domains of RHOGAPs confer substrate specificity and fine-tune their catalytic efficiency in cells"]

Every substrate claim for ABR's GAP domain — the 1993 papers, Chuang 1995, and Amin's own
RHOB result — comes from an **isolated recombinant domain**. So they are measurements of an
intrinsically promiscuous module, not competing claims about ABR's cellular substrate.
Substrate-specific MF terms would be recording an artefact of the assay format.

In cells, by contrast, the selectivity is real and Rac-directed: ABR shRNA in human HeLa
raises active **Rac1 but not Cdc42**
[PMID:36219160 "Intriguingly, in uninfected cells, the Rac1, but not Cdc42 activity levels were increased in the ABR knockdown compared to the Control shRNA-treated cells"].

**Hence: GO merged the substrate-specific GAP/GEF *activity* terms (where specificity is an
assay artefact) but retained substrate-specific *process* terms (where it is real). That
asymmetry is correct, and ABR is a clean demonstration of why.** The consequence for
curation is that the substrate belongs in `has_input` extensions plus the BP term, not in
a narrower MF term — and GOA carries no such extensions for ABR.

## In vivo: predominantly a negative regulator of Rac

- Human epithelial cells (the only human loss-of-function result in the set): ABR shRNA
  (~80% knockdown) raises active Rac1, not Cdc42 [PMID:36219160]. This is what lets
  `GO:0035021` be proposed as **IMP** rather than ISS.
- Glia: `Abr;Bcr` double nulls have granule cell ectopia and cerebellar foliation defects
  with abnormal Bergmann glia; double-null astroglia show constitutively raised p38 MAPK
  phosphorylation [PMID:11684658 "the simultaneous disruption of two negative regulators of Rac, Abr and Bcr, in mice leads to specific abnormalities in postnatal cerebellar development"].
- Macrophages: nulls are elongated, over-motile toward CSF-1, over-phagocytic, with
  sustained Rac activation; on CSF-1 stimulation Abr and Bcr transiently translocate to the
  plasma membrane and GAP-dead mutants ring the phagosome
  [PMID:17116687 "in response to CSF-1 stimulation, Abr and Bcr transiently translocated to the plasma membrane"].
  Same paper: [PMID:17116687 "These results identify Abr and Bcr as the only GAPs to date that specifically negatively regulate Rac function in vivo in primary macrophages."]
- Innate immunity: `abr/bcr` nulls over-produce MPO, elastase, ROS and MMP9 in endotoxemia
  [PMID:19703997 "These data show that Abr and Bcr normally curb very specific functions of mature tissue innate immune cells"].
  Full text adds that both Rac1 and Rac2 are in vivo substrates.
- T cells: **single** `abr-/-` mice get fatal cockroach-allergen asthma; their CD4+ T cells
  carry elevated GTP-bound Rac
  [PMID:24058174 "CD4(+) T cells from CRA-immunized and challenged abr(-/-) mice contained elevated levels of activated GTP-bound Rac compared with wild-type controls."].
- Synapse: **single** `ABR`-null mice show enhanced basal Rac1 activity and selective loss of
  LTP *maintenance*
  [PMID:20962234 "Mice deficient for BCR or ABR show enhanced basal Rac1 activity but only a small increase in spine density."].

The human, T-cell and synaptic data are all single-gene, so this does not rest on the
redundant double mutant. `GO:0035021` is **entirely absent from GOA** and is proposed as NEW.

**Why GO:0035021 is not implied by anything already annotated** (the earlier draft got this
wrong): GO's regulation branch keeps Rho and Rac **disjoint**. `GO:0035021` is NOT a
descendant of `GO:0035023`; it descends via `GO:0035020` → `GO:0051058` → `GO:0051056`.
So the already-present `GO:0035023` covers only the Rho half of ABR's range, and nothing in
GOA entails the Rac-directed negative regulation.

### All ancestry / merge claims, with the QuickGO result

Every load-bearing ontology-structure claim in this review, verified against QuickGO
(`/ontology/go/terms/<id>/complete` for merges, `/ancestors?relations=is_a,part_of` for
ancestry). Recorded in full so none of them rests on assertion:

| Claim | Result |
|---|---|
| `GO:0035021` descendant-of `GO:0035023` | **NO** — the load-bearing disjointness result |
| `GO:0035021` descendant-of `GO:0035020` | YES |
| `GO:0035021` descendant-of `GO:0051056` | YES (via `GO:0051058`) |
| `GO:0035023` descendant-of `GO:0051056` | YES |
| `GO:0035025` descendant-of `GO:0035023` | YES |
| `GO:0035025` descendant-of `GO:0051057` | YES |
| `GO:0051057` descendant-of `GO:0051056` | YES |
| `GO:1900273` descendant-of `GO:1900271` | YES |
| `GO:1900271` descendant-of `GO:0048167` | YES |
| `GO:0048167` descendant-of `GO:0050804` | YES |
| `GO:1900273` descendant-of `GO:0050804` | **YES** — exactly three `is_a` steps |
| `GO:0099092` descendant-of `GO:0014069` | YES |
| `GO:0007264` descendant-of `GO:0007165` | YES |
| `GO:0035023` descendant-of `GO:0007165` | NO (regulation branch is separate) |
| `GO:0051056` descendant-of `GO:0035556` | NO |
| `GO:0005096` children | 1, `GO:1902773` via `capable_of` — no substrate-specific child |
| `GO:0090630` children | **0** |

`GO:0035025` and `GO:0051057` were both confirmed current (not obsolete, no `secondaryIds`)
before being used.

## The GEF side is real but context-restricted

The clean in vivo GEF result is Xenopus single-cell wound repair: Abr is recruited to the
Rho activity zone by binding *active* Rho, amplifies Rho there via its DH domain, and uses
its GAP domain to exclude Cdc42 from that zone
[PMID:21295482 "Within the Rho zone, Abr promotes local Rho activation via its GEF domain and controls local crosstalk via its GAP domain, which limits Cdc42 activity within the Rho zone."].
This is the mechanistic reason ABR carries both modules: a zone-segregation device, not a
bidirectional switch on one GTPase.

## PSD-95 / DLG4 and the PDZ motif

`GO:0005515 protein binding` IPI cites `UniProtKB:P78352` = human DLG4 (PSD-95), which
resolves to the **reviewed canonical entry at the expected 724 aa** — no unreviewed ORFeome
fragment substituted for the canonical partner (the ACRV1 check, run and negative).

This is a real characterised interaction, not a screen hit:
- Direct interaction [PMID:20962234 "BCR and its close relative active BCR-related (ABR) localize at excitatory synapses and directly interact with PSD-95, an abundant postsynaptic scaffolding protein"], recorded by UniProt with `ECO:0000269`.
- The C-terminus is `...T-L-Y-F-S-T-D-V` — Thr at −2, Val at 0, i.e. a canonical **class I
  PDZ-binding motif**.
- V859A abolishes DLG4 binding while leaving synaptic targeting intact
  [file:human/ABR/ABR-uniprot.txt "V->A: Abolishes interaction with DLG4."].
- Independently described: [PMID:36219160 "ABR possesses a phospholipid-binding C2 domain positioned between the two domains and a PDZ binding motif located at the C-terminus of the protein."]

So `GO:0030165 PDZ domain binding` is the informative replacement for bare protein binding.

**But the PDZ interaction is NOT the synaptic targeting mechanism**, and this is easy to get
backwards. The full UniProt MUTAGEN note reads (FT lines 387-390):

```
FT   MUTAGEN         859
FT                   /note="V->A: Abolishes interaction with DLG4. No effect on
FT                   synaptic localization."
FT                   /evidence="ECO:0000269|PubMed:20962234"
```

Losing DLG4 binding costs ABR *nothing* in synaptic localisation. So ABR reaches the synapse
by some other route, and what the PSD-95 interaction contributes beyond tethering is **open**
— which is why the V859A-versus-R683A/N795A rescue is listed under `suggested_experiments`
rather than being asserted. Note the second half of that FT note spans an `FT` continuation
line, so "No effect on synaptic localization." **cannot be quoted verbatim** from the file;
the claim is carried in prose with the one-line "V->A: Abolishes interaction with DLG4."
fragment as the citation.

## WITH/FROM resolution and donor evidence

Done programmatically and committed: `ABR-bioinformatics/resolve_withfrom.py` +
`RESULTS.md`. All 21 distinct identifiers resolve. Nine are not protein sequences (2 PANTHER
nodes, 4 InterPro signatures, 2 ARBA rules, 3 UniProt SubCell keywords).

| Accession | Resolves to | Status | Relation to ABR |
|---|---|---|---|
| `UniProtKB:Q12979` | human ABR | Swiss-Prot | **self** (valid self-referential IBA) |
| `UniProtKB:P11274` | human BCR | Swiss-Prot | **paralog, same species** |
| `MGI:MGI:107771` | Q5SSL4 mouse Abr, 859 aa | Swiss-Prot | ortholog |
| `MGI:MGI:88141` | Q6PAJ1 mouse Bcr, 1270 aa | Swiss-Prot | paralog |
| `RGD:1306279` | A0A0G2JTR4 rat Abr, 859 aa | Swiss-Prot | ortholog |
| `RGD:1307993` | F1LXF1 rat Bcr, 1270 aa | Swiss-Prot | paralog |
| `UniProtKB:P78352` | human DLG4 / PSD-95, 724 aa | Swiss-Prot | interaction partner |
| `CGD:CAL0000181133` | Q5AGW7 *C. albicans* BEM2, 2252 aa | **TrEMBL** | distant RhoGAP-fold homolog |
| `PANTHER:PTN002754245` | GEF/GAP + Rho-signalling node | — | tree node, not a protein |
| `PANTHER:PTN001142600` | vertebrate synaptic node | — | tree node, not a protein |

Four tokens (both MGI, both RGD) are **multi-hit**, each returning the curated entry plus
unreviewed fragments; the Swiss-Prot entry was taken as canonical and its length matches the
ortholog, so the ambiguity is curated-vs-fragment, not gene-vs-gene. `CGD:CAL0000181133` is
**unreviewed**, so its protein *name* is an automatic label even though its GO annotations
are curated experimental — evidence provenance ≠ name provenance.

**Donor evidence, the decisive result: 20 of 22 protein donor/row pairs carry their own
experimental evidence at the donated term itself.** The two exceptions (rat Abr, rat Bcr on
`GO:0014069`) hold that term only by IBA/ISO/ISS but carry IDA at the more specific
`GO:0099092`. So **no donor lacks experimental grounding at or below the donated term**, and
`SOURCE_WEAK_OR_INFERRED` / `SOURCE_EVIDENCE_WEAK` are factually unavailable on every row.
Any objection has to be about whether a term should *propagate*, not about donor quality.

QuickGO's annotation search rejects MGI and RGD gene-product ids outright (HTTP 400), so
donors were queried through their resolved canonical UniProt accessions. Recording that
substitution because it is a real methodological limitation: an MGI-only annotation never
projected onto a UniProt accession would be invisible to this query.

### Paralog audit result

Every ABR annotation whose WITH/FROM includes BCR also has either an ABR ortholog donor in
the same set or ABR's own direct experimental evidence — with **one exception**:
`GO:0035023` (IBA) cites only `PANTHER:PTN002754245|UniProtKB:P11274`, i.e. the human
paralog BCR and a tree node, with **no ABR ortholog among the donors**. Read mechanically
that is a paralog-only, same-species transfer. It survives because ABR's own IDA
[PMID:7479768] independently establishes RhoA-directed GEF activity. Flagged in the review
and raised as a PAINT question rather than actioned.

Note that BCR itself carries `GO:0035023` by **IMP**, so the donor is sound; the issue is
the path, not the source. Root cause recorded as `NO_FAILURE_CORE` with no failure mode, so
that `root_cause` and `failure_modes` agree with the prose.

### Two PANTHER nodes, correctly split

`PTN002754245` is the GEF/GAP/Rho-signalling node (donors: mouse Abr, mouse Bcr, human BCR,
human ABR, *C. albicans* BEM2). `PTN001142600` is a vertebrate-only synaptic node (mouse
Abr, mouse Bcr, rat Abr, rat Bcr). Splitting the biochemistry from the synaptic localisation
across two nodes is the right call — the BEM2 donor supports GAP activity but obviously not
the postsynaptic density. This is a case of PAINT node placement being *correct*, worth
recording since the campaign has mostly found the opposite.

### The GO:0014069 downward-propagation check

Ran the ACRV1 check (does the propagation land above its donors?) and it is **positive but
not actionable**: mouse Bcr has IDA at `GO:0014069` itself, while rat Abr and rat Bcr carry
their IDA at the child `GO:0099092 postsynaptic density, intracellular component`.
`GO:0014069` is therefore the **LCA of what the donors demonstrate**, so per the AADACL4
lesson the general term is the ontology working correctly, not a granularity defect. The
definitions differ meaningfully — `GO:0014069` is "within and adjacent to the postsynaptic
membrane" whereas `GO:0099092` is only "adjacent to" — and for a soluble PSD-95-binding
protein the child is arguably more accurate, but the human evidence does not distinguish
the sub-compartment. Left as ACCEPT with the question raised for PAINT.

## Reactome placements

- `R-HSA-9014296 RAC2 GEFs activate RAC2` → `GO:0005085`. Credits "ABR (Chuang et al. 1995)"
  = PMID:7479768. Traceable and correct (Rac2 is at the weak end of the measured rank order
  but was measured).
- `R-HSA-9013022 RHOB GAPs stimulate RHOB GTPase activity` → `GO:0005096`. Lists ABR as a
  **confirmed** RHOB GAP ("Amin et al. 2016, supported by Bagci et al. 2020") while listing
  **BCR only as a candidate** ("binds to active RHOB"). Neither cached abstract
  (PMID:27481945, PMID:31871319) mentions ABR at all, so the ABR-specific claim is not
  verifiable from the abstracts. Reconciled, not contradicted: see the isolated-domain
  argument above. Kept and flagged.
- `R-HSA-205039 p75NTR indirectly activates RAC and Cdc42 via a guanyl-nucleotide exchange
  factor` → `GO:0005829`. The reaction summary names no GEF; ABR sits in an unnamed
  candidate set. Carries no ABR-specific information; the cytosol term itself is fine.
- `R-HSA-419166 GEFs activate RhoA,B,C` → `GO:0005829`. Consistent with the measured RhoA
  GEF activity.
- `R-HSA-9012999 RHO GTPase cycle` → `GO:0051056`, which is the **LCA of ABR's regulatory
  range** and the chosen MODIFY target for the four vague process rows.

## Retraction check

Explicit negative result, recorded because the check was run: **no cited paper is retracted.**
Two carry ordinary author errata — PMID:21295482 (Curr Biol 21(7):623) and PMID:31871319
(Nat Cell Biol 22(3):353) — and neither has "Retracted Publication" among its PubMed
publication types. The word "retraction" in PMID:21295482 is biological (cell protrusion and
retraction), not bibliographic.

## Decisions summary

32 GOA rows: **ACCEPT 19 · KEEP_AS_NON_CORE 7 · MODIFY 5 · MARK_AS_OVER_ANNOTATED 1 ·
REMOVE 0**, plus **3 NEW**.

- **MODIFY ×5**:
  - `GO:0007165 signal transduction` (IEA, from the RhoGAP domain signature),
    `GO:0035556 intracellular signal transduction` (IEA, from the DH signature), and **both**
    `GO:0007264 small GTPase-mediated signal transduction` rows (IEA + TAS) →
    **`GO:0051056`**. Two reasons: role conflation (GO:0007264 is defined as the cassette in
    which the GTPase *relays* the signal; ABR regulates it), and GO:0051056 is the true LCA
    given that GO keeps the Rho/Rac/Cdc42 regulation branches disjoint. Deliberately *not*
    `GO:0035023`, which would silently narrow the annotation to the Rho half.
  - `GO:0005515 protein binding` (IPI, DLG4) → **`GO:0030165 PDZ domain binding`**.
- **MARK_AS_OVER_ANNOTATED ×1**: `GO:0016020 membrane` (HDA). ABR has no transmembrane
  segment, and the source study's own abstract says only "approximately 40% of the identified
  proteins were predicted as plausible membrane proteins", with the rest expected to be
  "transiently associated with membranes" [PMID:19946888] — which is exactly what ABR is, and
  what the separately annotated `GO:0005886` with `is_active_in` already captures. Not removed:
  the peptides were genuinely detected and HDA is an experimental code.
- **KEEP_AS_NON_CORE ×7**: `GO:0030424 axon` (IEA), `GO:0045202 synapse` (IEA and ISS —
  redundant with the specific children), and the four `GO:0005829 cytosol` TAS rows (correct
  resting-state pool; the activity-bearing compartments are separately annotated).
- **No REMOVE.** Nothing in the set is demonstrably wrong, and every propagated row has an
  experimentally-annotated donor.
- **NEW ×3**: `GO:0035021 negative regulation of Rac protein signal transduction` (IMP, human
  HeLa knockdown — the dominant in vivo role, absent from GOA and not implied by any existing
  term); `GO:0035025 positive regulation of Rho protein signal transduction` (IDA — the GEF
  half's known direction, which GOA records only as the undirected `GO:0035023`, proposed
  additively because that row's donor holds only the undirected term); and `GO:1900273
  positive regulation of long-term synaptic potentiation` (ISS from mouse Abr; ABR-null mice
  lose LTP maintenance specifically).
- **No `proposed_new_terms`.** Both new terms already exist in GO, so they are `action: NEW`
  annotations, not ontology requests. Deliberately did **not** propose a substrate-specific
  GAP child — those were merged away on purpose.

## Corrections to the earlier draft

1. **`GO:0035021` is not under `GO:0035023`.** The earlier draft planned to MODIFY the vague
   process rows to `GO:0035023` *and* propose `GO:0035021`, implicitly treating the latter as
   a refinement of the former. GO keeps the Rac and Rho regulation branches disjoint, so
   `GO:0035023` would have narrowed those rows to the Rho half and left the Rac-directed
   function unrepresented. Target changed to `GO:0051056`.
2. **"Each domain binds substrate non-competitively" was a paraphrase, not a quote.** The
   paper says "Each individual domain bound in a noncompetitive manner to GTP-binding protein
   substrates." The earlier wording came from the affinage table and would have failed quote
   validation.
3. The earlier draft's header claimed "32 GOA rows reviewed" while the YAML had all 32 at
   `action: PENDING`.
4. The merge finding was stated for the MF branch only; `GO:0090630` has undergone the same
   consolidation (`GO:0032856`–`GO:0032864`).
5. The arginine finger was cited only via the `ECO:0000255` PROSITE-derived SITE feature. The
   experimental `MUTAGEN` evidence (`ECO:0000269|PubMed:17116687`) is much stronger and is
   what makes the GAP call rest on tested residues.

## Corrections made in review round 2

Three of these were found by the PR reviewer, and all three were real.

6. **A `core_function` asserted a mechanism the cited mutagenesis rules out.** The PDZ core
   function said the motif "recruits ABR's GAP activity into the postsynaptic density" — but
   V859A abolishes DLG4 binding with *no effect on synaptic localisation*. The review stated
   this correctly in the annotation row and listed the rescue as an open experiment, so the
   file contradicted itself. This is the campaign's recurring failure shape: every constituent
   quote verbatim, the error in the **join**. Reworded to "tethering", and the
   `GO:1900273` link was moved off the PDZ-binding function onto the GAP function, where the
   Rac1-restraint effector activity actually sits.
7. **The GEF core function was the one place this review's own argument was not applied.** It
   listed four substrates but `directly_involved_in: GO:0035023` alone — undirected, and
   covering only the Rho half, which is precisely the reasoning used to retarget four MODIFY
   rows away from `GO:0035023`. Now `GO:0035025` (positive regulation of Rho protein signal
   transduction), **plus a matching NEW annotation** so `core_functions` is backed by the
   annotation set rather than asserting a process nothing else records.
   Deliberately *not* widened to `GO:0051057`/Rac/Cdc42: the DH domain does load GTP onto
   CDC42, RAC1 and RAC2, but that is isolated-domain biochemistry, and by the same argument
   this review makes about the GAP side, that does not establish an in-cell sign — in cells
   ABR's net effect on Rac is *negative*. Applying my own rule symmetrically was the point.
8. **The top-level description overstated the arginine finger.** It gave "stabilises the
   transition state for GTP hydrolysis" as fact; in UniProt that is `SITE 683` with
   `ECO:0000255|PROSITE-ProRule`, i.e. inferred. Reworded so the measured claim (R683A reduces,
   R683A/N795A abolishes GAP activity) and the inferred mechanism are distinguished.
9. **A supporting quote was dropped rather than truncated.** The fix for item 6 initially cited
   `"No effect on"` — a fragment ending mid-sentence at the very negation it was meant to
   support, and unquotable in full because the span crosses an `FT` continuation. Removed; the
   claim now travels in prose.

## Not annotated, deliberately

- **Phagocytosis.** Mouse `Abr;Bcr` double nulls over-phagocytose [PMID:17116687]; human
  trabecular-meshwork siRNA *reduces* phagocytosis by ~40% (affinage table, PMID:31516309).
  Opposite signs, one from a redundant double mutant, one from a single siRNA experiment in
  one cell type. Left for `suggested_experiments`.
- Mitotic fidelity in hESCs (PMID:28579391), osteoclast differentiation (PMID:37507586),
  hypoxic pulmonary remodelling (PMID:23152932), GDM/hyperglycaemia RhoA activation
  (PMID:38776074) — all single-report, downstream of the Rac/Rho activity change, and
  pleiotropic. Not annotated.
- EspH (PMID:36219160) identifies ABR as the native host target of an EPEC effector binding
  the ABR GAP domain. Real and well-controlled, but a pathogen-side function; the host-side GO
  content is "ABR has a GAP domain that restrains Rac1/Cdc42", which *is* now captured — this
  paper supplies the human IMP for `GO:0035021`.

## Provider record (affinage)

`self_evaluation_pairwise: win` with clear trust gates, `faith_pct: 100.0`, 15 citations, all
numeric PubMed ids (no bioRxiv
DOIs in PMID-shaped fields). Its corpus-level conclusion matches the primary literature and
is cited once, for that corpus-level direction only. **It does not cite Amin et al. 2016
(PMID:27481945)** — the paper that reconciles the substrate conflict and that Reactome relies
on for the RHOB assignment. That was found via the Reactome entry, not the provider narrative.
No mechanistic claim in this review rests on a provider sentence.
