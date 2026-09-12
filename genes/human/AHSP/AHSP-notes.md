# AHSP (human, Q9NZD4) — review notes

Working journal for the GO annotation review. Provenance is recorded inline as a
bracketed citation followed by a verbatim quotation from that reference. All 17
such quotes in this file were machine-verified against the cached publications
with the repo's own `SupportingTextValidator` (the code CI uses for the review
YAML), because nothing in CI checks a notes file.

## 1. What AHSP is, in one paragraph

A 102-residue, erythroid-restricted, all-α-helical cytoplasmic protein that binds
free α-globin 1:1, holds it soluble and folded, drives its heme iron into a
redox-inert ferric bis-histidyl hexacoordinate state, and releases it to β-globin
for assembly into HbA. It is one of the best structurally characterised chaperones
in the genome: eight PDB entries that split exactly four/four — **four X-ray
co-crystal structures with α-globin** (1Y01 at 2.8 Å ferrous; 1Z8U at 2.4 Å ferric;
3IA3 at 3.2 Å, the Pro30 cis-peptidyl structure; 3OVU at 2.83 Å, a ternary complex
with *S. aureus* IsdH) and four solution-NMR structures of the free protein (1W09,
1W0A, 1W0B, 1XZY). This count was **derived** by asking PDBe which entries map both
`Q9NZD4` and `P69905`, not read off UniProt's `RN` labels — the first draft of this
review said "two", because only 1Y01 and 1Z8U carry an `IN COMPLEX WITH HBA` line.
See §11b. `PE 1: Evidence at protein level`.

This is the opposite of the usual problem in this campaign. AHSP is not
over-annotated and it is not dark. The interesting question is whether GO can
*express* what is known, and the answer is largely no.

## 2. Row reconciliation (do this first — the stub under-seeds on many genes)

```
wc -l < genes/human/AHSP/AHSP-goa.tsv   -> 25  (24 data rows + 1 header)
grep -c '^- term:' AHSP-ai-review.yaml  -> 24  (stub, before edits)
grep -c 'GO:0005515' AHSP-ai-review.yaml -> 11 (matches the 11 IPI rows in the TSV)
```

Counts agree. The stub did **not** collapse any rows on this gene — all eleven
`GO:0005515` partner rows survived individually. Reported as a negative result
because the ADAMTSL5 / ACTR5 finding says to check.

Final `existing_annotations` count is 24 GOA rows + 2 `NEW` proposals = 26, with
actions **8 ACCEPT · 8 MARK_AS_OVER_ANNOTATED · 7 MODIFY · 1 REMOVE · 2 NEW**.
(The tally shifted from 10/8/5/1/2 after review: the two `GO:0030492` rows moved
from ACCEPT to MODIFY once `GO:0031721` was found — see §6.)

## 3. The chaperone/holdase term situation — checked before proposing anything

Fetched definitions and parentage from QuickGO
(`/ontology/go/terms/<id>/complete`), not labels.

| term | status | why it does or does not fit AHSP |
|---|---|---|
| `GO:0051082` unfolded protein binding | **obsolete** (`isObsolete: true`, no `secondaryIds`) | replaced-by is empty; `consider` lists `GO:0044183` and `GO:0140309` |
| `GO:0140309` unfolded protein holdase activity | current | def is a **`protein carrier activity`** (ancestors `GO:0140597` → `GO:0140104`) that "binds to a protein in an unfolded state and escorts it to an acceptor molecule or to a specific location"; the term comment says a holdase "binds an unfolded protein and **keeps it unfolded**" |
| `GO:0044183` protein folding chaperone | current | "Binding to a protein or a protein-containing complex to assist the protein folding process"; comment: "binds an unfolded protein **to fold it**" |
| `GO:0140597` protein carrier activity | current | "Directly binding to a protein and delivering it either to an acceptor molecule or to a specific location" |
| `GO:0140713` histone chaperone activity | current | child of `GO:0140597`; "Binding to and carrying a histone or a histone complex to unload or deposit it as a nucleosome" |

**The gap.** GO's two chaperone MF terms partition the space by the *client's*
folding state, and AHSP's client is in neither state:

- AHSP does **not keep α-globin unfolded**, so `GO:0140309` is excluded by its own
  comment. Its ferrous and ferric complexes are crystallographically ordered
  globins with all helices present
  [PMID:15931225 "To attain this unusual conformation, segments of alphaHb undergo drastic structural rearrangements, including the repositioning of several alpha-helices"].
- AHSP does not fold α-globin to the native state either. With apo-α-globin it
  produces a *partially* folded, conformationally mobile species and holds it there
  until heme arrives
  [PMID:20860551 "Addition of AHSP leads to dissociation of soluble αo aggregates, formation of a stable αo:AHSP dimer, and a dramatic shift from unfolded to partially folded forms of αo."]
  [PMID:20860551 "Thus, AHSP can stabilize αo in solution whilst still retaining a large degree of conformational flexibility in the αo subunit."].

`GO:0044183` is nevertheless the honest partial fit and is GO's own designated
successor to the obsoleted `GO:0051082`: the same paper states the activity
outright [PMID:20860551 "AHSP forms a heterodimeric complex with αo that inhibits αo aggregation and promotes αo folding in the absence of haem"].
So it goes in as a `NEW` row, with the partial-fit caveat stated in the reason,
and the residual gap is recorded as a `KnowledgeGap` of kind `ONTOLOGY` with a
proposed term rather than forced into `GO:0140309`.

The structural precedent for the proposed term is GO's own handling of histone
chaperones: `GO:0140713` sits under `GO:0140597 protein carrier activity` and
describes binding a *folded* client, keeping it soluble, and depositing it into
its final assembly. That is AHSP's mechanism with "nucleosome" replaced by
"hemoglobin tetramer". Hence the proposal `globin chaperone activity` as a sibling.

**The obvious alternative, considered and rejected: annotate `GO:0140597` itself.**
It is an existing term, no proposal needed, and its definition — "Directly binding
to a protein and delivering it either to an acceptor molecule or to a specific
location" — reads as though it fits, since β-globin is an acceptor molecule. Two
reasons not to:

1. **The parent term's own comment defines a carrier by movement:** *"Note that a
   carrier moves with its substrate/cargo, while a transporter does not move with the
   cargo, but facilitates the change in localization"* (`GO:0140104`). AHSP does not
   move anywhere. And the hand-off is not an act of delivery but **competitive
   displacement** — β-globin outcompetes AHSP at the same interface
   [PMID:15550245 "The AHSP-alphaHb interactions are extensive but suboptimal, explaining why beta-hemoglobin can competitively displace AHSP to form HbA"].
   Annotating `GO:0140597` would assert an activity whose mechanism is the reverse of
   what was measured: AHSP is displaced, it does not deliver.
2. **It would drop the part that makes AHSP distinctive.** Every existing child of
   `GO:0140597` is about getting a client somewhere. None involves changing the
   client's chemistry. Suppressing the haem iron's reactivity is not a side effect of
   holding α-globin — it is the reason holding it works, and it is what `GO:0016209`
   cannot express either (§4). A term that captured only the carrier half would leave
   the redox half homeless in both branches.

So `GO:0140597` is cited as the proposed *parent*, not used as the annotation. This is
recorded because it is the first question a reviewer should ask, and "we did not just
reach for the nearest existing term" is only credible if the nearest existing term is
named and dispatched.

### A stale label in a shared cache, and why it is not fixed here

`GO:0140597`'s live primary label is **`protein carrier activity`** (confirmed
independently at QuickGO and OLS; `protein carrier chaperone` is an exact synonym).
The repo disagrees with itself:

| source | label |
|---|---|
| `cache/go/terms.csv` (label cache used by term validation) | `protein carrier chaperone` |
| `cache/ontologies/go.tsv` | `protein carrier activity` |
| `genes/yeast/{RRB1,SQT1,SHQ1}-ai-review.yaml` on `main` | `protein carrier chaperone` |

A reviewer suggested refreshing the stale `terms.csv` row in this PR. **Measured
before deciding**, by editing the row and re-validating a merged file:

```
just validate yeast RRB1   # with the refreshed label
⚠ WARN: Label mismatch for 'GO:0140597':
        expected 'protein carrier activity', got 'protein carrier chaperone'
```

So the refresh is not free — it puts a new warning on **three merged reviews** that
this PR does not otherwise touch, because they use the synonym in a label-validated
`core_functions.molecular_function` slot. A correct fix updates the cache *and* those
three files in one commit; that is shared-infrastructure work, not gene-review work,
and the campaign's standing rule is not to regenerate shared caches inside a gene PR.

The edit was therefore reverted and only the measurement kept. This review uses the
live label in its own `proposed_parent`, which is the slot under its control. The
three files needing simultaneous update are named above so whoever does the refresh
does not have to rediscover them.

AHSP is therefore another gene stranded by the `GO:0051082`/`GO:0140309` gap
tracked in repo issue #2222 — but the *shape* of its stranding differs from the
sHSP cases, and the difference is the part worth reporting: those genes hold
genuinely unfolded clients and are blocked only by the **carrier** clause,
whereas AHSP is blocked by **both** clauses at once, because its client is folded
*and* it translocates nothing. A fix that only relaxes "escorts it to an acceptor
molecule or to a specific location" would free the sHSPs and still leave AHSP
with no molecular function.

(No count of affected genes is asserted here. The ordinal in the first draft —
"a fifth kind of victim" — was invented; I have not enumerated the genes on
issue #2222, and a number I have not derived does not belong in the notes.)

## 4. The redox / antioxidant framing — tested, and it fails for GO:0016209

AHSP's protection of α-globin is genuinely redox chemistry:

- [PMID:15931225 "conversion to the ferric bis-histidine configuration strongly and specifically inhibits redox chemistry catalysis and haem loss from alphaHb"]
- [PMID:23264625 "AHSP binding also dramatically reduces the redox potential of α-subunits, from +40 to -78 mV in 1 m glycine buffer, pH 6.0, at 8 °C, demonstrating independently that AHSP has a much higher affinity for Fe(III) versus Fe(II) α-subunits."]
- [PMID:26995402 "In the presence of Alpha-hemoglobin stabilizing protein (AHSP), which stabilizes the α-subunit in a redox inactive hexacoordinate conformation (thus unable to undergo the redox ferric/ferryl transition), Cys93 oxidation was substantially reduced in both proteins."]

Affinage's own GO grounding proposes `GO:0016209 antioxidant activity`. **Rejected.**
The definition is "Inhibition of the reactions brought about by dioxygen (O2) or
peroxides. Usually the antioxidant is effective because it can itself be more
easily oxidized than the substance protected. The term is often applied to
components that can trap free radicals". AHSP is neither sacrificially oxidised
nor a radical trap — it has no redox-active group at all; it remodels the
*client's* heme coordination sphere. Consistently, all seven `is_a` children of
`GO:0016209` are redox enzymes (peroxidase, SOD, glutathione-disulfide reductase,
thioredoxin-disulfide reductase, superoxide reductase, glutathione dehydrogenase,
sulfiredoxin). Recorded as the second `ONTOLOGY` knowledge gap: GO has no MF for
suppressing a *bound client's* cofactor reactivity.

**Wrong-ROS-species check: negative.** GOA carries no ROS term on AHSP at all, so
there was nothing to propagate wrongly. Had there been, the generic parent would
have been the correct choice here rather than a species-specific child, because
the literature implicates several distinct species in sequence — O2 autoxidation,
H2O2, ferryl heme and protein-based radicals
[PMID:23264625 "EPR data suggest that protein-based radicals associated with the ferryl oxidation state exist within HbA α- and β-subunits."].
The BP term proposed is therefore `GO:1903427 negative regulation of reactive
oxygen species biosynthetic process` (generic in species, specific in direction),
verified as a descendant of `GO:2000378` and not obsolete.

## 5. The `GO:0005833 hemoglobin complex` row is refuted by its own citation

`GO:0005833` is annotated `part_of`, NAS, citing PMID:12066189. Three independent
grounds to remove it:

1. **The cited paper says the opposite in its abstract.**
   [PMID:12066189 "AHSP) is an abundant, erythroid-specific protein that forms\na stable complex with free alpha-haemoglobin but not with beta-haemoglobin or\nhaemoglobin A (alpha(2)beta(2))"]
2. **UniProt says the opposite**, from two curated structural papers
   (`ECO:0000269|PubMed:15550245, ECO:0000269|PubMed:15931225`).
3. **The term definition excludes it.** `GO:0005833` = "An iron-containing, oxygen
   carrying complex. In vertebrates it is made up of two pairs of associated globin
   polypeptide chains". The AHSP complex is a 1:1 heterodimer of one non-globin
   chain with one globin chain
   [PMID:12192002 "AHSP and alpha-globin are both monomeric in solution as determined by analytical\nultracentrifugation and bind each other to form a complex with 1:1 subunit\nstoichiometry"],
   and it is specifically **not** oxygen-carrying — binding drives α-globin to the
   non-reactive hexacoordinate ferric state.

NAS is a non-experimental code, so the "never REMOVE an experimental annotation you
cannot verify" rule does not engage.

**Why the error happened is the more useful finding:** there is no GO term for the
complex AHSP actually forms. Searching GO for an AHSP/α-globin complex returns
nothing. The curator had a crystallographically defined, stoichiometrically
measured heterodimer to record and the nearest available CC term was the tetramer.
Hence the second proposed new term, `AHSP-alpha-globin complex` under
`GO:0032991`, is filed *with* the REMOVE rather than instead of it.

## 6. `GO:0030492` → `GO:0031721` — and the search error that nearly hid it

**Corrected after review.** The first version of this section concluded that
`GO:0030492 hemoglobin binding` was "the maximal available term", accepted the
tetramer mismatch as a recorded caveat, and used it as the MODIFY target for the
three α-globin `GO:0005515` rows. That was wrong.

**`GO:0031721 hemoglobin alpha binding` exists.** Definition: *"Binding to a
hemoglobin alpha chain."* It is an `is_a` child of `GO:0030492`, not obsolete, and
it is exactly what four X-ray structures resolve. Its sibling `GO:0031722` is
`hemoglobin beta binding`; the third id in that consecutive block, `GO:0031720`, is
`haptoglobin binding`.

**Why the first pass missed it, and the generalisable rule.** I searched OLS for
`"globin binding"` and `"alpha-globin binding"`. Neither can match a label reading
*hemoglobin alpha binding*, because OLS tokenises on words and **"globin" is not a
token of "hemoglobin"** — the string is a substring, not a token. So the search was
incapable of returning the term, and its empty result told me about my query, not
about the ontology.

This repo's own brief states the rule — *"an empty OLS keyword search is NOT
evidence a term is absent"* — and names the fix: confirm with
`get_terms_from_ontology` or QuickGO. **Listing the `is_a` children of `GO:0030492`
returns both `GO:0031721` and `GO:0031722` immediately.** One call. It is the same
error as the structure recount in §11b, in the same review, two hours apart:
*a null result is a claim about the method, and so is a count read off a label.*
Twice is a pattern, and the pattern is **asserting absence from a convenience
query**.

**Consequences of the fix**, all in the same direction — the review gets stronger:

1. The three α-globin `GO:0005515` rows now MODIFY to `GO:0031721`, a strictly more
   specific and definitionally exact term.
2. Both `GO:0030492` GOA rows move from ACCEPT to **MODIFY → `GO:0031721`**.
3. **The definitional asymmetry disappears.** The reviewer's second point was fair:
   §5 removes `GO:0005833` partly *because* its definition requires a tetramer,
   while §6 was accepting a tetramer-defined binding term with only a broad-synonym
   mitigation. Applying the same standard to both rows was not possible while
   `GO:0030492` was believed to be maximal; it is now.
4. One `suggested_question` to the GO editors (should `GO:0030492` be broadened, or
   a free-chain child created?) was asking for a term that already existed, and is
   withdrawn. It is replaced by a better question aimed at **InterPro**: `IPR015317`
   is an orthogroup-specific signature, so retargeting its InterPro2GO mapping from
   `GO:0030492` to `GO:0031721` would fix every AHSP orthologue at once rather than
   one gene at a time.

Note what is *not* affected: the CC gap in §5 is real. `GO:0005833` has **zero
children**, seven independent QuickGO query phrasings return no CC term for an
AHSP or α-globin complex, and ComplexPortal holds **nine** complexes containing
AHSP and **none** containing α-globin (`P69905`) — checked by reading each entry's
participant accessions, because the nine names list AHSP alongside MAPK8IP
scaffolds and are not plausible erythroid complexes on their face. Having just been
caught asserting absence from one query, that absence was checked several ways.

## 7. Propagation: the cleanest IBA set seen in this campaign

All four IBA rows carry `MGI:MGI:2158492|PANTHER:PTN000408386`.

**Donor identity.** `Q9CY02` = `AHSP_MOUSE`, Swiss-Prot reviewed, 102 aa (identical
length to human), gene `Ahsp`, same FUNCTION text. A true one-to-one orthologue,
not a paralogue.

**Donor's own evidence** (QuickGO `geneProductId=UniProtKB:Q9CY02`, 13 annotations,
`numberOfHits == len(results)` so not truncated):

| propagated term | donor's own evidence | same term? |
|---|---|---|
| `GO:0005737` cytoplasm | **IDA** PMID:12066189 | yes |
| `GO:0006457` protein folding | **IDA** PMID:12066189 | yes |
| `GO:0030218` erythrocyte differentiation | **IMP** PMID:12066189 | yes |
| `GO:0050821` protein stabilization | **IDA** PMID:12066189 | yes |

Every donor annotation is experimental and sits at **exactly** the propagated term
— no granularity drop (the ACRV1 defect), no upward generalisation, no paralogue
transfer. So no `propagation_review` is required and all four are ACCEPT.

**Family.** `PTHR15914` has a single subfamily (`SF0`) and **170 proteins across
144 proteomes**; the InterPro reviewed-protein endpoint returns **3** Swiss-Prot
members (human, mouse, bovine AHSP), i.e. 1.8% of the family — that CSV is the
reviewed subset, not the family. There are no non-AHSP members and no paralogues,
so none of the family-heterogeneity caveats (AADACL2/3/4) or mis-clustered-member
defects (ACAP2 `blow`, ACTL8) can apply here. Reported as a negative result.

**Node-placement check (the AADACL/ACTG2 reciprocal question): negative.** There is
only one node with any human reach in this family, and the terms on it are the same
terms the sole experimental orthologue holds. There is no node whose reach is a
subset of the family and no term stranded at the wrong level.

**Sibling/paralogue cross-check: not applicable, and verified beyond the reviewed
subset.** Querying UniProt for *all* human members of the family
(`xref:panther-PTHR15914 AND organism_id:9606`, not just Swiss-Prot) returns three
entries — `Q9NZD4` (reviewed, 102 aa), `Q549J4` (unreviewed, 102 aa) and `H3BSK6`
(unreviewed, 57 aa) — and **all three are AHSP itself**, a duplicate entry and an
isoform fragment of the same gene. So there is genuinely no human paralogue to
cross-check identical rows against, which is the one campaign technique unavailable on
this gene. Checked explicitly rather than inferred from the 3-row reviewed CSV, because
that CSV is the Swiss-Prot subset (3 of 170) and would not have shown an unreviewed
paralogue.

## 8. InterPro2GO provenance (`GO_REF:0000002`)

`IPR015317` is "Alpha-haemoglobin stabilising protein" — a **family-specific**
signature covering the AHSP orthogroup, not a bare fold. Its four mappings,
confirmed against the live `interpro2go` file, are exactly the four IEA rows in
GOA:

```
InterPro:IPR015317 ... > GO:hemoglobin binding ; GO:0030492
InterPro:IPR015317 ... > GO:protein folding ; GO:0006457
InterPro:IPR015317 ... > GO:erythrocyte differentiation ; GO:0030218
InterPro:IPR015317 ... > GO:protein stabilization ; GO:0050821
```

Family-specific signature + terms that the one experimentally characterised member
actually holds = well-founded. Three of the four are ACCEPTed; they are redundant
with the IBA rows but not wrong.

The fourth, `GO:0030492`, is **MODIFY → `GO:0031721`** (§6). The mapping is not
wrong, only one level too general — and because `IPR015317` matches the AHSP
orthogroup and nothing else, the specific child is safe family-wide. That makes
this a fixable defect *upstream* rather than per gene: retargeting one line of
`interpro2go` would correct every AHSP orthologue in one edit, which is why it is
raised as a question for InterPro rather than only as a MODIFY here. Same shape as
the PAINT node-placement findings elsewhere in this campaign — the annotation is
right, the level it is attached at is not.

`GO_REF:0000120` (combinatorial, **not** ARBA) supplies the second `GO:0005737`
row, from `UniProtKB:Q9CY02` + `ensembl:ENSMUSP00000159842` +
`UniProtKB-SubCell:SL-0086`. Same mouse orthologue, whose cytoplasm annotation is
its own IDA. ACCEPT.

## 9. The eleven `GO:0005515` rows: one real partner, seven screen singletons

IntAct (`/intact/ws/interaction/findInteractions/Q9NZD4`, 39 records read of 39
reported) resolves this cleanly. Counting **distinct experiments**, not
`NbExp`:

| partner | methods | distinct publications | verdict |
|---|---|---|---|
| P69905 HBA1/HBA2 | **x-ray diffraction**, **bio-layer interferometry**, **anti-tag coIP** | 3 (15550245, 25156257, 40205054) | real; MI 0.71; typed `direct interaction` |
| Q5D1E8 ZC3H12A | two hybrid pooling; two hybrid array + prey pooling + validated | 2 (16189514, 25416956) | screen only |
| P62942 FKBP1A | array + prey pooling + validated | 1 (25416956) | screen only |
| Q05086-2 UBE3A-2 | array + prey pooling + validated | 1 (25416956) | screen only |
| P17024 ZNF20 | array + prey pooling + validated | 1 (32296183) | screen only |
| P20618 PSMB1 | array + prey pooling + validated | 1 (32296183) | screen only |
| Q8IUQ0 CLVS1 | array + prey pooling + validated | 1 (32296183) | screen only |
| Q9Y2B5 VPS9D1 | array + prey pooling + validated | 1 (32296183) | screen only |

**Third confirmed instance of the `NbExp` trap** (after ACRV1 and ADAMTSL5): for
six of the seven screen partners, UniProt's `NbExp=3` is *one* Y2H screen logged as
`two hybrid array` + `two hybrid prey pooling approach` + `validated two hybrid`.
ZC3H12A's `NbExp=4` is two screens, but both are CCSB Y2H against the same human
ORFeome, so the repeat is assay reproducibility, not orthogonal confirmation.

**Expression-domain check.** AHSP is erythroid-restricted
[PMID:12066189 "Stabilizing Protein (AHSP) is an abundant, erythroid-specific protein"];
UniProt's TISSUE SPECIFICITY line says "Expressed in blood and bone marrow" and HPA calls
it "Tissue enriched (bone)". CLVS1 is a neuron-restricted protein
("Required for normal morphology of late endosomes and/or lysosomes in neurons"),
ZNF20 is a nuclear zinc finger, VPS9D1 is endosomal. None shares a compartment or
a cell type with a 12 kDa erythroid cytosolic chaperone whose entire measured
biochemistry is with one ligand.

**Partner-accession discipline (the ACRV1 check): all clean.** Every one of the
eight accessions resolves to a **reviewed Swiss-Prot canonical** entry of the
expected length — no TrEMBL substitutions, no partial ORFeome clones. The single
non-canonical token is `Q05086-2`, which is an explicitly declared *isoform*
identifier for UBE3A isoform 2, not a truncated clone; recorded on the row.

**Erratum check on the AP-MS partner.** `PMID:40205054` carries an unflagged
`ErratumIn -> PMID:41039152`. Read the correction rather than assuming scope: it
corrects the fourth equation in the "Loss functions" section of the Methods
(`Ty`/`Sy` → `Tx`/`Sx`) and nothing else. It does not touch the AP-MS interaction
data, so the AHSP–HBA row stands. Affinage did not cite this paper at all, so the
provider's failure here is recall, not an unflagged retraction. **Twenty-seven PMIDs**
were checked via `CommentsCorrections/RefType` on each article's own record (the
only way a Publisher Correction is discoverable) — 26 in the first sweep plus
`PMID:19706593` when it was added later — and this was the only flag.

**Projection test (`reference=PMID:12066189`): negative, and informative.** Eight
annotations over **two** distinct entities — human AHSP and mouse Ahsp. Not a
ComplexPortal-style projection. What it does show is that one paper produced
*experimental* codes on the mouse protein and *NAS* on the human one, which is
exactly the asymmetry that then propagated back to human as IBA.
`reference=PMID:40205054` returns 3026 annotations and paginates beyond a readable
limit, so its entity count is **unavailable** and its projection test is reported
as unreliable rather than estimated from a page.

## 9b. No `file:` supporting_text is used anywhere in this review

The first draft quoted `AHSP-uniprot.txt` in four places. Those were all replaced with
PMID quotes, so the review contains **zero** `file:` supporting_text entries and the
one unvalidated fabrication surface in this repo is simply not used here.

Two reasons, one practical and one principled:

- **Practical.** The repo's pre-write hook validates against the *main* checkout's
  project root (`Path(__file__).parent.parent.parent` from `.claude/hooks/`), not the
  agent worktree, so a `file:human/AHSP/...` reference for a gene folder that exists only
  in the worktree is reported as a non-existent file and blocks the write. Worth knowing
  for any new gene created in a worktree.
- **Principled.** CI verifies `supporting_text` verbatim only for `PMID:` references;
  `file:` quotes are unchecked. Every statement that had a UniProt quote also has a
  primary-literature source, so nothing was lost by moving to PMIDs - and the one
  UniProt statement that could *not* be quoted safely (the SUBUNIT negative, whose
  "Does / not bind beta-hemoglobin nor alpha(2)beta(2) hemoglobin A" crosses a `CC`
  continuation line and reads as its own opposite if truncated) is carried by
  PMID:12066189's abstract instead.

Both the review YAML and this notes file were then checked with a strict-duplicate-key
loader plus the repo's own `SupportingTextValidator`: **66 quotes in the YAML and 17 in
the notes, 0 problems, raw `supporting_text` key count equal to the parsed count** (so no
duplicate YAML key silently discarded provenance). The checker was tested by breaking
it - mutating one quoted word made it exit 1 and name the row - before its clean run was
believed.

## 10. Species discipline on the two NEW rows

The mouse knockout literature for AHSP is abundant and it is *not* usable as IMP on
the human protein. Both `NEW` rows are anchored to experiments on human material:

- `GO:0044183` — **IDA**. Purified human proteins: AHSP is the 102-residue native
  human sequence and [PMID:20860551 "Hb A, αh and βh were obtained from human blood."].
  Note this is also why the row is IDA rather than IMP: the assay is biochemical, on
  purified components, not a perturbation of a cell.
- `GO:1903427` — **IDA**. Purified human AHSP and human α-subunits
  [PMID:23264625 "α-Hemoglobin stabilizing protein (AHSP) is a molecular chaperone that binds\nmonomeric α-subunits of human hemoglobin A (HbA) and modulates heme iron\noxidation and subunit folding states."].

A human IMP is also available for the ROS row from shRNA knockdown in human K562
and human CD34+ erythroblasts
[PMID:18179859 "AHSP-knockdown cells demonstrated an increased ROS production and\nincreased rate of apoptosis."],
recorded as a second supporting reference rather than a second row.

## 11. What affinage got right and what it missed

`gates_passed: True` (precision only — there is no recall gate). 19 citations, all
numeric PMIDs, no `PMID:bio_*` preprint ids, none retracted.

Missed, and each mattered:

- **`PMID:12066189`** — the discovery paper, the source of four of the 24 GOA rows,
  and the paper whose abstract refutes the `GO:0005833` annotation. Absent from the
  affinage citation list entirely.
- **`PMID:12192002`** — the 1:1 stoichiometry and Ka measurement underpinning the
  proposed complex term.
- **`PMID:15178680`** — the free-protein NMR structure.
- **`PMID:19706593`** — a *third* co-crystal structure paper (PDB 3IA3), and the one
  that actually demonstrates the Pro30 mechanism affinage attributes to the later
  NMR/EXAFS paper. See §11b: this one was found only by recounting the structures.
- **`PMID:40205054`** and the three interactome papers — i.e. every reference behind
  the eleven `GO:0005515` rows.

Got right and worth keeping: the Pro30 strain mechanism, the redox-potential shift,
the V56G kinetic defect, and the αo chaperone result. Its GO grounding proposed
`GO:0016209` (rejected, §4), `GO:0140313` molecular sequestering activity (rejected
— the definition is "to prevent it from interacting with other partners or to
inhibit its localization"; AHSP's purpose is the *opposite*, to preserve α-globin
for its partner) and `GO:0140110` transcription regulator activity (rejected —
AHSP is a *target* of STAT3 and NRF2/MAFG, not a regulator; PMID:24740453 and
PMID:35092867 both measure AHSP promoter occupancy *by* those factors).

## 11b. A number I had asserted from a label, recounted from the data — and it was wrong

The first draft said, in four places, that AHSP has "two co-crystal structures". That
came from reading UniProt's `RN` block, where exactly two entries carry
`X-RAY CRYSTALLOGRAPHY ... IN COMPLEX WITH HBA`. Deriving the number instead — asking
PDBe which of the eight entries map **both** `Q9NZD4` and `P69905` — gives **four**:

| PDB | method | resolution | chains mapped | citation |
|---|---|---|---|---|
| 1Y01 | X-ray | 2.80 Å | AHSP + HBA | PMID:15550245 |
| 1Z8U | X-ray | 2.40 Å | AHSP + HBA | PMID:15931225 |
| 3IA3 | X-ray | 3.20 Å | AHSP + HBA | **PMID:19706593** |
| 3OVU | X-ray | 2.83 Å | AHSP + HBA + `Q6G8J7` IsdH (*S. aureus*) | unpublished |
| 1W09, 1W0A, 1W0B, 1XZY | solution NMR | — | AHSP only | PMID:15178680 / PMID:15550245 |

Two consequences, and the second is the point:

1. **The count was understated by half**, and it is load-bearing — it appears in the
   `ONTOLOGY` knowledge gap ("GO can say only that it binds haemoglobin, despite …"),
   in the proposed complex term's justification, and in the ComplexPortal suggestion.
   Corrected with a script that asserts each anchor is present before replacing and
   re-greps for the retracted phrasing afterwards — **and it still landed in 4 of 5
   sites.** A fifth occurrence in `suggested_questions` read "GO:0030492 has two
   co-crystal structures", which the post-edit grep missed because the retracted-phrase
   list contained `"two crystal structures"` and not `"two co-crystal structures"`. This
   is the campaign's "fixed in N places, landed in N−1" recurrence happening to a script
   that was written specifically to prevent it: **anchoring on enumerated phrasings
   inherits whatever the author failed to imagine.** The fix was to lint for the
   *pattern* — a cardinal number word within 40 characters of a structure noun, across
   the review, the notes, the history record and the PR body — rather than for
   sentences. That lint found the miss immediately, and its own first run produced four
   false positives (digits inside `2.8 A`, PMIDs and GO ids), which is why digits are
   excluded from the pattern and only count *words* are matched. It is self-tested by
   mutating `four` back to `two` and requiring the lint to fail.
2. **Recounting surfaced a paper nothing else had.** `PMID:19706593` (Gell *et al.*,
   JBC 2009) is absent from UniProt's `RN` list, absent from GOA, and absent from the
   affinage report — yet it is a crystal structure *plus* the mutagenesis that
   establishes the Pro30 mechanism, and its abstract states the ROS claim in one
   sentence: [PMID:19706593 "AHSP forms a specific complex with alphaHb and suppresses the heme-catalyzed evolution of reactive oxygen species by converting alphaHb to a conformation in which the heme is coordinated at both axial positions by histidine side chains (bis-histidyl coordination)."]
   It is now cited on the `GO:1903427` row and in `core_functions`.

This is the campaign's "a number that refuses to add up is the bug report" lesson in a
mild form — nothing disagreed loudly, the number was simply never derived. **A structure
count taken from a reference list is a claim about the reference list.** The generalisable
check is one API call: for any gene whose argument leans on structures, ask the structure
database which entries contain the gene *and its partner*, and reconcile that against
whatever the review asserts.

The unpublished 3OVU is worth noting separately: it is a ternary complex of AHSP·αHb with
*Staphylococcus aureus* IsdH, i.e. a bacterial haem-scavenging receptor caught acting on
the AHSP-protected subunit. Not used for any annotation — there is no paper — but it is a
further independent determination of the heterodimer, which is why it counts toward the
proposed complex term.

## 12. Deliberately not annotated

**`GO:0005634` nucleus.** [PMID:32629835 "sub-cellular location of AHSP is both in the cytoplasm and nucleus in the early erythroblasts\nwhile in the late stages of maturation AHSP is found predominantly in the\nnucleus, being expelled with it during enucleation."]
Human primary erythroblasts, Amnis image-based flow cytometry, two independent cell
sources. Not carried into GO because: it is a single antibody-based imaging study
from one laboratory; AHSP has no NLS and at 11.8 kDa can enter the nucleus by
passive diffusion, so "found in the nucleus" does not imply a nuclear function; and
every measured activity of the protein is on a cytoplasmic ligand. Recorded as a
`BIOLOGY` knowledge gap and a suggested experiment instead of an annotation.

**`GO:0042541` as an additional row.** Handled by MODIFYing the vague
`GO:0020027 hemoglobin metabolic process` NAS row downward instead, since
`GO:0042541` is a verified descendant of `GO:0020027` and adding it would leave the
parent redundant.
