# AGFG1 (P52594) — computational analyses supporting the GO review

Every number below is produced by a script in this directory. Re-run order does not
matter; each script is standalone and fetches its own inputs.

| script | question | output |
|---|---|---|
| `arfgap_motif.py` | is the ArfGAP catalytic apparatus intact? | `arfgap_motif.json` |
| `zinc_site.py` | which residues hold the zinc in the AGFG1 structures? | `zinc_site.json` |
| `paralogy.py` | are AGFG1 and AGFG2 really paralogues? | `paralogy.json` |
| `paralog_goa.py` | which GO terms reach both, and from where? | `paralog_goa.json` |
| `node_reach.py` | which PANTHER node carries each IBA term, and whom does it reach? | `node_reach.json` |
| `donors.py` | what evidence does each WITH/FROM donor itself carry? | `donors.json` |
| `reference_projection.py` | how many entities does each cited reference annotate? | `reference_projection.json` |
| `intact.py` | how many *distinct experiments* support each interaction? | `intact.json` |
| `terms.py` | definitions, obsoletion status, and every ancestry claim | `terms.json` |
| `parse_arba.py` | which ARBA condition set actually fires for AGFG1? | (stdout) |
| `retractions.py` | is any relied-on reference retracted or corrected? | `retractions.json` |
| `litsearch.py` | recorded Europe PMC queries behind each stated negative | `litsearch.json` |
| `probe_ids.py` | which identifier forms does QuickGO accept? | (stdout) |
| `audit_review.py` | invariants over the emitted review YAML (`--self-test` break-tests all 7) | (stdout) |
| `grep_file_quotes.py` | byte-exact `grep -F` check of every `file:` supporting_text | (stdout) |
| `check_candidate_quotes.py` | pre-checks `candidate_quotes.tsv` before quotes enter the YAML | (stdout) |
| `patch_affinage_ref.py` | anchor-asserting, idempotent edit that added the affinage reference | (stdout) |

## 1. The ArfGAP catalytic apparatus is intact — the pseudoenzyme hypothesis is NOT confirmed

The anchor is published, not remembered. `PMID:18809720` (the consensus-nomenclature
paper for the 31 human ArfGAPs) states the domain contains *"a characteristic C4-type
zinc finger motif and a conserved arginine that is required for activity, within a
particular spacing (CX2CX16CX2CX4R)"*, and names ArfGAP1's residues as Cys22/25/42/45 +
Arg50.

`arfgap_motif.py` reproduces those published numbers exactly as a positive control
before reporting anything else, and raises if it cannot.

| protein | length | zinc-finger Cys | conserved Arg | apparatus |
|---|---|---|---|---|
| **AGFG1 human (P52594)** | 562 | **29, 32, 49, 52** | **Arg57** | intact |
| AGFG2 human (O95081) | 481 | 47, 50, 67, 70 | Arg75 | intact |
| Agfg1 mouse (Q8K2K6) | 561 | 29, 32, 49, 52 | Arg57 | intact |
| drongo *D. melanogaster* (E1JHR0) | 673 | 30, 33, 50, 53 | Arg58 | intact |
| ARFGAP1 human (Q8N6T3) — control | 406 | 22, 25, 42, 45 | Arg50 | intact |
| ARFGAP2, ARFGAP3, ASAP1, ACAP1, SMAP1, GIT1 | — | — | — | intact |
| ADAP1 human (O75689) | 374 | 21, 24, 41, 44 | Arg49 | intact |

**12/12 panel members retain CX2CX16CX2CX4R.**

The last row is the built-in negative control and it is the point of the table: the same
reference states that *"Arf GAP activity has been demonstrated in vitro for at least one
member of each subfamily, with the exception of the ADAPs, which appear to lack in vitro
GAP activity"* — yet ADAP1's motif is complete. **Sequence retention of the apparatus is
necessary and demonstrably not sufficient**, so it cannot on its own establish
`GO:0005096` for AGFG1, and equally it removes any structural ground for withdrawing it.

## 2. The zinc is really there, and it is held by the four predicted cysteines

`zinc_site.py` computes the Zn coordination shell from the deposited coordinates of both
AGFG1 ArfGAP-domain entries. Author numbering is **not** UniProt numbering (2D9L is
offset by +6), so the offset is read from SIFTS and each converted position is checked
against the UniProt sequence.

| PDB | method | models | auth→UniProt offset | coordinating residues (UniProt numbering) | Zn–SG distances |
|---|---|---|---|---|---|
| 2OLM | X-ray 1.48 Å | 1 | +0 | Cys29, Cys32, Cys49, Cys52 | 2.30–2.40 Å |
| 2D9L | NMR | 20 (model 1 analysed) | +6 | Cys29, Cys32, Cys49, Cys52 | 2.26–2.35 Å |

Two independent structures agree, and both agree with the motif scan of section 1. This
is direct experimental evidence that human AGFG1 binds zinc — a term GOA does **not**
carry (see section 8).

## 3. AGFG1 and AGFG2 are paralogues — verified, not assumed

`paralogy.py`, three independent lines with a scale:

1. **PANTHER**: shared family `PTHR46134`; distinct subfamilies `PTHR46134:SF1` (AGFG1)
   vs `PTHR46134:SF4` (AGFG2).
2. **InterPro**: identical signature sets — `IPR001164`, `IPR037278`, `IPR038508`,
   `IPR052248` — for both.
3. **Pairwise identity** (Biopython global alignment, BLOSUM62):

| pair | full-length | ArfGAP domain |
|---|---|---|
| AGFG1 vs AGFG2 | 48.9% | **71.2%** |
| ARFGAP1 vs ARFGAP3 (accepted paralogue pair, different subfamily) | 35.1% | 48.2% |
| AGFG1 vs ARFGAP1 (cross-subfamily) | 27.4% | 30.0% |
| AGFG1 vs ACTB (negative control) | 19.6% | — |

AGFG1/AGFG2 are *closer* than an accepted ArfGAP paralogue pair, so the shared name is
not the only reason to treat them as one clade.

## 4. One PANTHER node carries three AGFG1-specific spermatid terms to BOTH paralogues

`node_reach.py` asks the two node questions in both directions. `GO:0005737` (593,028 IBA
annotations) and `GO:0031410` (38,628) are **not attempted** — no partial count is
reported for them — because a first-page total read as a whole is exactly the pagination
trap. The three biological-process terms are small enough to enumerate fully.

| term | total IBA annotations | nodes carrying it | AGFG1's node | recipients of that node | human recipients |
|---|---|---|---|---|---|
| `GO:0001675` acrosome assembly | 121 | 5 | `PTN002919572` | 36 | **AGFG1 + AGFG2** |
| `GO:0007289` spermatid nucleus differentiation | 63 | 3 | `PTN002919572` | 36 | **AGFG1 + AGFG2** |
| `GO:0045109` intermediate filament organization | 1124 | 11 | `PTN002919572` | 36 | **AGFG1 + AGFG2** |

The 36 recipients of `PTN002919572` were counted programmatically from the WITH/FROM
fields, not by eye: **21 AGFG1-type, 12 AGFG2-type and 3 unnamed** gene products across
17 species. Mouse *Agfg2* (Q80WC7) and rat *Agfg2* (A0A0G2K7G2) are themselves
recipients, so **no AGFG2 orthologue in any species carries experimental evidence for any
of these three terms.**

Meanwhile `donors.py` shows the entire experimental basis of all three is **mouse Agfg1
(Q8K2K6) alone**:

| term | donor evidence at the exact term |
|---|---|
| `GO:0001675` | Q8K2K6 IMP `PMID:11711676`, IMP `PMID:14724135` |
| `GO:0007289` | Q8K2K6 IMP `PMID:16765935` |
| `GO:0045109` | Q8K2K6 IMP `PMID:14724135` |
| `GO:0031410` | Q8K2K6 IDA `PMID:11711676`; P52594 EXP `PMID:10613896` |
| `GO:0005737` | E1JHR0 (drongo) IDA `PMID:27654348` |

So `PTN002919572` sits at or above the AGFG1/AGFG2 duplication, and AGFG1-specific
spermiogenesis biology has been attached to it. For **AGFG1** the transfer is an
orthologue transfer from a strong mouse null phenotype and is sound. For **AGFG2** it is
a paralogue transfer with no AGFG2 evidence anywhere. Moving the three terms down to the
AGFG1-orthologue node (`PTHR46134:SF1`) would retract them from the 12 AGFG2-named
recipients in one edit and leave all 21 AGFG1-named recipients correct. The 3 unnamed
recipients are not classified either way.

## 5. A byte-identical WITH/FROM is self-referential on AGFG1 and paralogue-derived on AGFG2

`paralog_goa.py`. Two rows carry `UniProtKB:P52594` in their WITH/FROM:

| term | AGFG1's row | AGFG2's row |
|---|---|---|
| `GO:0005737` | `FB:FBgn0020304 \| MGI:MGI:1333754 \| PANTHER:PTN002353603 \| UniProtKB:P52594` — **self-referential** | same tokens — **paralogue-derived** |
| `GO:0031410` | `MGI:MGI:1333754 \| PANTHER:PTN002919572 \| UniProtKB:P52594` — **self-referential** | same tokens — **paralogue-derived** |

A self-referential IBA records a PAINT curator judging the function core for that gene;
the same bytes on the sibling are a transfer from AGFG1. Same field, different evidential
status.

## 6. Two of the four protein-binding partners are one Y2H screen counted three times

`intact.py` expands the IntAct records instead of trusting `NbExp`.

| partner | IntAct records | distinct publications | methods | MI-score | distinct IntAct partners of the partner |
|---|---|---|---|---|---|
| VAMP7 (P51809) | 7 | **1** (`PMID:18775314`) | two hybrid + **isothermal titration calorimetry** + pull down | 0.64 | 65 |
| POLE2 (P56282) | 3 | **1** (`PMID:25416956`) | two hybrid array + two hybrid prey pooling + validated two hybrid | 0.56 | 37 |
| NYAP2 (Q9P242) | 3 | **1** (`PMID:25416956`) | two hybrid array + two hybrid prey pooling + validated two hybrid | 0.56 | 8 |
| NXF3 (Q9H4D5) | **0** | 0 | — (GOA row assigned by UniProt from the primary paper, not via IntAct) | — | 4 |

VAMP7's seven records are one study but **three orthogonal methods**, one of them
quantitative. POLE2's and NYAP2's three records each are one HuRI screen logged as three
*sub-methods of the same experiment* — the `NbExp=3` artefact — with no orthogonal assay.

**The promiscuity arm of the argument comes back negative and is reported as such:**
AGFG1 has 37 IntAct partners, POLE2 37 and NYAP2 8, so neither partner is a hub and
neither is topologically inaccessible to a nuclear/cytoplasmic protein. The case against
those two rows rests on the single-screen evidence alone.

## 7. Reference-projection test

`reference_projection.py`. Entity counts are distinct gene-product ids, never annotation
totals.

| reference | annotations | entities | terms | reading |
|---|---|---|---|---|
| `PMID:7634337` | 3 | **1** (AGFG1) | `GO:0003723`, `GO:0005634`, `GO:0006406` | legacy single-gene ProtInc import |
| `PMID:7637788` | 1 | **1** (AGFG1) | `GO:0005643` | legacy single-gene ProtInc import |
| `PMID:10613896` | 2 | 1 (AGFG1) | `GO:0005634`, `GO:0031410` | focused primary curation |
| `PMID:18775314` | 2 | 2 (AGFG1, VAMP7) | `GO:0005515` | reciprocal pair, focused |
| `PMID:11545741` | 10 | 4 (AGFG1, NXF3, NXF1, XPO1) | 5 terms incl. `GO:0042272` | **coherent multi-protein curation, not a bulk import** |
| `PMID:25416956` | 24,599 | unavailable | — | **projection test UNINFORMATIVE** — too large to enumerate honestly |

The `PMID:11545741` result is worth stating positively: a curator annotated four
different proteins with five different terms from that paper, so the AGFG1↔NXF3 row is a
considered call rather than pipeline output — even though the paper's full text is not
retrievable (Europe PMC: `isOpenAccess N`, `inEPMC N`, no PMC id).

## 8. The mouse orthologue lacks all three legacy human TAS rows

Full annotation set of Q8K2K6 (17 annotations): `GO:0001675`, `GO:0007289`, `GO:0045109`,
`GO:0005634`, `GO:0005737`, `GO:0031410`, `GO:0043025`, and `GO:0005096` (IEA:InterPro).

**Mouse Agfg1 carries zero `GO:0003723` rows, no `GO:0005643`, and no `GO:0006406`.** All
three human rows come from the two 1995 discovery papers via ProtInc/PINC and exist in
one species only.

## 9. UniProt still carries a keyword-derived MF that GOA has dropped — and one it should keep

`AGFG1-uniprot.txt` lists both of these under `DR GO`:

```
DR   GO; GO:0003677; F:DNA binding; IEA:UniProtKB-KW.
DR   GO; GO:0008270; F:zinc ion binding; IEA:UniProtKB-KW.
```

Neither appears among AGFG1's 35 GOA rows — the `IEA:UniProtKB-KW` route was withdrawn
from GOA. The two cases differ in kind:

* **`GO:0003677` DNA binding is not supported.** AGFG1 has no DNA-binding module. Its
  only zinc site is the ArfGAP C4 finger, which section 2 shows is buried and fully
  occupied by structural zinc, and which `PMID:18809720` describes as having *"an
  architectural rather than catalytic role"*. The `KW DNA-binding` keyword appears to
  follow InterPro's remark that the ArfGAP zinc finger *"displays some similarity to the
  C4-type GATA zinc finger"* — a fold resemblance, not a measured activity.
* **`GO:0008270` zinc ion binding is supported and is missing from GOA.** Two structures
  resolve the zinc on four cysteines (section 2).

## 10. The ARBA rule that gives AGFG1 `GO:0005737` fires on a gene-specific FunFam pair

`parse_arba.py` evaluates all **2414** condition sets of `ARBA00026971` against AGFG1's
own signature/taxon profile, distinguishing sets that *fire* from sets that merely
*mention* one of its signatures.

* **fires (1)**: `FunFam id=1.10.220.150:FF:000005 AND FunFam id=3.30.450.50:FF:000005`
* mentions but does not fire (1): `IPR001164 AND IPR037278 AND IPR051718` — AGFG1 has
  `IPR052248`, not `IPR051718`
* the rule grants exactly one term: `GO:0005737`

Both FunFams in the firing set are named for AGFG1 itself, so this is a gene-specific
rule granting a location AGFG1 independently has by experiment. No defect.

## 11. A fusion-construct crystal structure has given AGFG1 a phantom Longin domain

Gene3D/CATH assigns **`G3DSA:3.30.450.50` "Longin domain" to AGFG1 residues 154–234**.
That region is annotated `REGION 145..193 Disordered` (MobiDB-lite) and
`COMPBIAS 176..191 Polar residues` in `AGFG1-uniprot.txt`, and `PMID:18775314` says the
VAMP7-binding stretch *"is contained within the region that follows the ArfGAP domain,
which is predicted to lack stable secondary structural elements"*.

The origin is traceable. PDBe reports that each of chains A–D of **2VX8** is a single
169-residue polypeptide mapping to **two** UniProt entries:

```
P52594 AGFG1_HUMAN  chains A-D  unp 136-175
P70280 VAMP7_MOUSE  chains A-D  unp 1-120
```

and the paper describes making exactly that construct: *"a cDNA encoding the fragment of
Hrb mapped as binding VAMP7 longin domain (residues 136–176) was cloned onto the 5′ end
of the VAMP7 longin domain cDNA"*. The longin fold belongs to VAMP7; the domain call has
crossed the fusion junction into AGFG1.

**Negative control:** AGFG2 — same family, same InterPro set, 71.2% identical over the
ArfGAP domain — has **no** `3.30.450.50` assignment. The error is keyed on having a
chimeric PDB entry, not on family membership. It is not currently producing a wrong GO
term (the FunFam pair grants only `cytoplasm`), so it is reported as a
CATH/Gene3D–UniProt correction rather than a GO action.

## 12. Retraction / erratum check

`retractions.py` checks all 20 relied-on PMIDs by two routes — `CommentsCorrections`
`RefType` on each *cited* article's own record, and `PublicationType` — with
`PMID:32125225` (known retracted) as a positive control, which fires.

**0/20 carry a retraction, erratum or expression-of-concern flag.** A correction can
carry a null PubMed id and be visible only through Crossref, so this is "none found by
these two routes", not "none exists".

## 13. Checks that came back negative, recorded so they are known to have been run

* **Logical-opposite cross-product** (a term and its `negative regulation of` twin
  sharing references): AGFG1's GOA contains no such pair. Not applicable.
* **Promiscuity / topological-inaccessibility** argument against the two HuRI partners:
  negative (section 6).
* **Partner-accession substitution** (TrEMBL clones or partial ORFeome constructs posing
  as canonical partners): negative. All four partners resolve to reviewed Swiss-Prot
  entries at canonical length — VAMP7 220 aa, POLE2 527 aa, NYAP2 653 aa, NXF3 531 aa.
* **IBA landing above its donor**: negative. Every IBA term AGFG1 receives is the same
  term the donor holds; no downward `MODIFY` is warranted.
* **Circularity**: negative. All five IBA rows have at least one donor with its own
  experimental annotation at the exact term (section 4).
* **Direct evidence that AGFG1 binds RNA**: a recorded Europe PMC query
  (`litsearch.py`, key `agfg1_rna_binding`, 234 hits) returned no study reporting
  RNA binding by AGFG1/hRIP. This is a statement about that query, not about the world.
* **QuickGO identifier forms**: `probe_ids.py` confirms MOD ids (`MGI:MGI:1333754`,
  `MGI:1333754`, `FB:FBgn0020304`, `FlyBase:FBgn0020304`) are rejected with **HTTP 400**
  while UniProt accessions return 200 — so every MOD donor was resolved to a UniProt
  accession first, with `UniProtKB:P52594` (35 hits) as the positive control.

## 14. Recall of the affinage record

`AGFG1-deep-research-affinage.md` reports `gates_passed: True` with **2** citations
(`PMID:10613896`, `PMID:18819912`). Neither of the two papers that decide this review is
among them: `PMID:18775314` (the VAMP7 structure, ITC and depletion phenotype) and
`PMID:11711676` (the mouse null with no acrosome). Nor is `PMID:18809720`, the family
reference that supplies the catalytic-motif anchor, nor `PMID:38606629`, the only human
dataset placing AGFG1 with ARF1/ARF3/ARF6. A passing gate bounds precision and says
nothing about recall.
