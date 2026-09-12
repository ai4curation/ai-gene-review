# AHSP (human, Q9NZD4) — review notes

Working journal for the GO annotation review. Provenance is recorded inline as a
bracketed citation followed by a verbatim quotation from that reference. All 15
such quotes in this file were machine-verified against the cached publications
with the repo's own `SupportingTextValidator` (the code CI uses for the review
YAML), because nothing in CI checks a notes file.

## 1. What AHSP is, in one paragraph

A 102-residue, erythroid-restricted, all-α-helical cytoplasmic protein that binds
free α-globin 1:1, holds it soluble and folded, drives its heme iron into a
redox-inert ferric bis-histidyl hexacoordinate state, and releases it to β-globin
for assembly into HbA. It is one of the best structurally characterised chaperones
in the genome: eight PDB entries, including two crystal structures of the complex
with α-globin (1Y01 at 2.8 Å, ferrous; 1Z8U at 2.4 Å, ferric) and four NMR
structures of the free protein. `PE 1: Evidence at protein level`.

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

Final `existing_annotations` count is 24 GOA rows + 2 `NEW` proposals = 26.

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

AHSP is therefore a fifth kind of victim of the `GO:0051082`/`GO:0140309` gap
tracked in repo issue #2222 — but note the difference from the sHSP cases: those
genes hold genuinely unfolded clients and are blocked only by the *carrier*
clause, whereas AHSP is blocked by **both** clauses (its client is folded and it
does not translocate).

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

## 6. `GO:0030492 hemoglobin binding` — kept, with the definitional mismatch recorded

Same shape as §5 but resolves the other way. The definition again names the
tetramer ("an oxygen carrying, conjugated protein containing four heme groups and
globin"), which AHSP demonstrably does not bind. But:

- the term carries the broad synonym **"globin binding"**, so GO itself licenses
  the looser reading;
- both GOA and InterPro2GO already use it for exactly this (`IPR015317` →
  `GO:0030492`);
- an OLS search for any α-globin-specific or free-globin-chain binding term returns
  nothing.

So `GO:0030492` is the maximal available term and is ACCEPTed, with the mismatch
noted on the row. Do not propose a child to fix it — the activity terms in §3 are
the right place to put the information, per CLAUDE.md's rule against uninformative
binding terms.

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
actually holds = well-founded. ACCEPT all four; they are redundant with the IBA
rows but not wrong.

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
provider's failure here is recall, not an unflagged retraction. Twenty-six PMIDs
were checked via `CommentsCorrections/RefType` on each article's own record (the
only way a Publisher Correction is discoverable); this was the only flag.

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
loader plus the repo's own `SupportingTextValidator`: **60 quotes in the YAML and 15 in
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
