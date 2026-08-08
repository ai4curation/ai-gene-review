# ADPRHL1 (ARH2, Q8NDY3) — review notes

Human ADPRHL1 / ARH2, UniProt **Q8NDY3** (`ARHL1_HUMAN`, reviewed, 354 aa, PE 1: evidence at
protein level). Accession verified independently against `projects/paint/human-no-IBA-simple.csv`
(line `human,Q8NDY3,ADPRHL1`) and against the UniProt REST record.

## Row reconciliation, done before reviewing

| source | count |
|---|---|
| `ADPRHL1-goa.tsv` data lines | 7 |
| distinct data lines | 7 |
| `fetch-gene` stub `- term:` entries | 7 |

They reconcile exactly. No stub collapse on this gene — a **non-confirmation** of the
ADAMTSL5 stub-collapse defect. (The stub key is (GO id, evidence, reference, negated,
qualifier); the two `GO:0030017` rows survive as separate entries because their evidence codes
and references differ.)

## The worklist's "no-IBA" name is, for once, accurate — and that is itself the finding

Three genes this campaign were on `human-no-IBA-simple.csv` while carrying IBA rows, so this
was queried rather than assumed. QuickGO returns **7 annotations for `UniProtKB:Q8NDY3`, none
of them IBA**, with `numberOfHits == len(results)` asserted. UniProt agrees:
`[file:human/ADPRHL1/ADPRHL1-uniprot.txt "PAN-GO; Q8NDY3; 0 GO annotations based on evolutionary models."]`.

**Positive control** (a zero and a rejected query look identical): the same call pattern on
`UniProtKB:P54922` (ADPRH) returns 15 annotations of which **2 are IBA**. The endpoint works,
IBAs are visible for this family, and ADPRHL1 genuinely has none.

That absence is not an oversight. `GO:0003875` is propagated by IBA to **20 gene products from
a single node, `PANTHER:PTN009030515`**, seeded by `MGI:MGI:1098234` (mouse Adprh),
`RGD:2052` (rat Adprh) and `UniProtKB:P54922` (human ADPRH) — and **every one of the 20 is an
ADPRH orthologue**. Not one ADPRHL1 orthologue is among them. **PAINT models this family's
catalytic loss correctly and deliberately gave the ARH2 clade nothing.** That is the negative
control that makes the rest of this review an argument rather than an opinion: a curation body
*can* get this right, and one did.

**All 20 recipients were resolved individually rather than read off the symbol column**, and
the Swiss-Prot/TrEMBL split is stated because an unreviewed entry's *name* is an automatic
label and must not be cited as evidence of what a protein does:

| status | n | detail |
|---|---|---|
| reviewed (Swiss-Prot) | 4 | P54922 human, P54923 mouse, Q02589 rat, Q32KR8 bovine — all `ADPRH` |
| unreviewed (TrEMBL) with gene name `ADPRH`/`adprh` | 11 | macaque, opossum, platypus, dog, chicken, pig, gorilla, chimp, *X. tropicalis*, *X. laevis* adprh.L and adprh.S |
| unreviewed, no gene name | 5 | sea urchin, horse, anole, spotted gar, amphioxus `LOC118404985` |

Every one of the 20 is named "ADP-ribosylhydrolase ARH1" and **none is an ARH2**. The
gene-name column carries the claim for 15 of 20; for the remaining 5 it rests on the PANTHER
node placement plus the automatic name, which is weaker — and saying so is the point.

## The central question: does the pseudoenzyme premise hold?

It holds, on four independent lines, one of which is a direct measurement.

### 1. A measured in-vitro negative (not merely an absence of reports)

`[PMID:17075046 "ARH2 and poly(ADP-ribose) glycohydrolase were inactive."]` — Ono *et al.*
assayed recombinant ARH2 against O-acetyl-ADP-ribose alongside ARH1 and ARH3 and found no
activity. The Moss-lab family review restates the position across the whole assay panel:
`[PMID:36497109 "Enzyme properties: ARH2 (so far) does not exhibit any enzymatic activities [70], consistent with differences in primary sequences from critical residues found in ARH1 (e.g., 54-SDDT-57, 302-DSDS-305)"]`
and, on the specific reaction the GO term names,
`[PMID:36497109 "ARH2 does not appear to be responsible for hydrolysis of ADP-ribose-acceptor linkage."]`.
The Xenopus group reach the same conclusion citing the same biochemistry:
`[PMID:32726316 "The sequence changes suggest binding of ADP-ribosylated protein substrates and cation-mediated catalysis are both abolished in Adprhl1 and biochemical assays have confirmed the lack of any comparable enzymatic activity"]`.

This is the difference between this gene and the ADGRA2 case. ADGRA2's coupling was
**unmeasured**; ADPRHL1's hydrolase activity was **measured and not found**. Per the campaign's
own calibration that is the condition under which `REMOVE` is earned rather than
`MARK_AS_OVER_ANNOTATED`.

**And the field's own caveat is recorded rather than suppressed:**
`[PMID:36497109 "However, the lack of ARH2 catalytic activity may be the result of the use of model substrates."]`
That caveat is why nothing in this review claims ADPRHL1 is inert; it claims the *arginine
hydrolase* reaction is refuted. Those are different statements, and only the second is
annotatable.

### 2. UniProt curates the loss on this exact entry

`[file:human/ADPRHL1/ADPRHL1-uniprot.txt "lacks the metal-binding and substrate-binding residues"]`
(CAUTION) and
`[file:human/ADPRHL1/ADPRHL1-uniprot.txt "showing no activity against O-acetyl-ADP-ribose"]`
(FUNCTION). The feature table carries **zero** `BINDING` and **zero** `ACT_SITE` features.
For comparison ADPRH (P54922) has 14 such features spanning **20 distinct residue
positions**, and ADPRS/ARH3 (Q9NX46) 14 spanning **17** — the census works in positions,
because `binding_sites()` expands ranged features.

### 3. My own residue census, with an identity-matched positive control

`genes/human/ADPRHL1/ADPRHL1-bioinformatics/catalytic_site_census.py` (committed, self-testing,
regenerates `RESULTS.md` byte-identically) maps all 20 of ADPRH's UniProt-annotated ligand
positions through a global alignment onto 17 family members.

| clade | n | % id to ADPRH | identical of 20 | disruptive+gap | Mg(2+) donor kept of 6 |
|---|---|---|---|---|---|
| ARH1 / ADPRH (active; positive control) | 5 | 48.4–100 | 13–20 | 0–3 | 6 |
| **ARH2 / ADPRHL1 (subject)** | **7** | **42.6–47.7** | **6–7** | **7–8** | **2–3** |
| ARH3 / ADPRS (active; discriminating control) | 4 | 26.6–28.1 | 7–8 | 7–9 | 6 |
| DraG (active, arginine; low-identity control) | 1 | 27.5 | 9 | 8 | 6 |

The **identity-matched control** is the load-bearing part. *Dictyostelium* ADPRH is a genuine
ARH1 at **48.4%** identity — the same distance from human ADPRH as ADPRHL1's 42.6–47.7% — and
keeps 13 of 20 sites with 3 disruptive. Every ADPRHL1 orthologue keeps 6–7 with 7–8 disruptive.
So retention is not tracking sequence distance. Two low-identity *active* enzymes make the same
point from the other side: DraG at 27.5% keeps 9, more than ADPRHL1 keeps at nearly twice the
identity.

Two external checks that the alignment method is sane, both reproducing published figures:
measured 46.6% vs `[PMID:32726316 "the 357 amino acid ADPRH and 354 aa ADPRHL1 share 46% sequence identity"]`,
and measured 74.6% vs `[PMID:32726316 "Xenopus Adprhl1 being 75% identical to human ADPRHL1"]`.

Site by site, the Mg²⁺ centre is dismantled: **D56→N58, D304→A306, S305→A307** lose the
coordinating oxygen; S54→S56, D55→D57 and D302→E304 keep it. The one that decides it is
**D56→N58**, because aspartate-to-asparagine at a vicinal catalytic aspartate is exactly the
substitution the field uses to *kill* this family's activity — PMID:17075046 abolishes ARH3's
reaction by replacing D77/D78 with asparagine. BLOSUM62 scores D→N at +1 and calls it
conservative; the mechanism does not. This is why the script reports a third, mechanism-anchored
`donor_group` column and rests on that rather than on a generic substitution matrix.

This reproduces the paper's own residue list independently:
`[PMID:27217161 "Three of the four critical aspartates of ADPRH have been lost in mammalian ADPRHL1 (hADPRH D56, D302, D304 lost, only D55 is conserved), suggesting that ADPRHL1 cation binding may be compromised."]`

### 4. Reproducing the sibling ADPRH review's panel, and the one place we differ

`paint/ADPRH` (PR #2332) published a five-position census over the same family. Its calls for
the five accessions the two analyses share were reproduced **before** anything else was
reported.

- **Residue and mapped position: identical on all 25 calls.** Two independently written
  alignments put the same amino acid at the same place.
- **Class label: 7 differences, all of metric, none of data.** `paint/ADPRH` uses hand-defined
  conservative groups; this script uses `BLOSUM62 > 0`. Every difference is a BLOSUM62-positive
  substitution (D→N, S→A) that nonetheless deletes a coordinating oxygen. **The sibling's
  "disruptive" call is the biologically correct one**, and the `donor_group` column agrees with
  it — vindicated by an experiment inside the family rather than by a matrix. Reported as a
  metric difference and not silently absorbed, per the ACTG2 lesson.

### The mirror error, tested and avoided

A lost active site is not a lost function, and ADPRHL1's function is real, essential and
independent of catalysis:

- `[PMID:27217161 "Recombinant Adprhl1 can localize to stripes adjacent to the Z-disc"]`, and
  morpholino knockdown in *Xenopus* blocks striated myofibril assembly and ventricle outgrowth.
- `[PMID:32726316 "Mutant alleles encode discrete loss of 1, 3 or 4 amino acids from a di-arginine (Arg271-Arg272) containing peptide loop at the centre of the ancestral ADP-ribosylhydrolase site."]`
  — CRISPR deletions in that loop abolish ventricular myofibril assembly. So the *cleft*
  matters even though the *chemistry* is gone.
- The alignment reproduces the structural claim behind that from UniProt features alone:
  ADPRH's two adjacent adenosine-ribose-binding serines **S269/S270 align to ADPRHL1
  R271/R272**, matching
  `[PMID:32726316 "The critical Adprhl1 deletion covers the exact structural position where in the active enzyme Adprh, two adjacent serines that support adenosine-ribose substrate binding are located."]`.
  The subsite is not merely degraded — two small hydroxyls have been replaced by two long
  cationic side chains, which is a *change of function*, not a decay.

So the correct reading is **"catalysis refuted, function retained and relocated to the vestigial
cleft"**, not "pseudoenzyme, therefore nothing".

### The one hedge that survives, stated as a hedge

`[PMID:27217161 "Of particular note is the aspartate, D100, that could provide an alternative coordination site for metals but whose presence interferes with the phosphate groups of forcibly docked ADP."]`
D100 is a *modelling suggestion*, hedged with "could", presented in the source as an obstacle to
substrate docking rather than as a functional metal site, and never tested. It does not rescue
`GO:0000287`, whose provenance is the ancestral catalytic Mg²⁺ site — but it is why the
`GO:0000287` verdict is argued from the annotation's *derivation* rather than from an
unqualified claim that ADPRHL1 binds no metal.

## How the three catalytic terms actually got here — two routes, neither residue-aware

### Route 1: InterPro2GO, and the entry supplies its own negative control

Downloading `interpro2go` and looking up each of the four signatures ADPRHL1 matches:

| signature | type | interpro2go mapping |
|---|---|---|
| **IPR012108** ADP-ribosylarginine hydrolase | family (backed by **PIRSF016939** alone) | **GO:0000287, GO:0003875, GO:0051725** |
| IPR050792 ADP-ribosylglycohydrolase | family | *none* |
| IPR005502 Ribosyl_crysJ1 | domain | *none* |
| IPR036705 Ribosyl_crysJ1 superfamily | homologous superfamily | *none* |

So this is not "InterPro2GO is careless". Three of four signatures map to nothing; InterPro2GO
exercises restraint on the fold- and family-level entries. **One specific entry carries a
mapping stronger than its own membership warrants.**

And the membership is measurable. `IPR012108` has **1282 proteins**, of which **11 are reviewed
(Swiss-Prot) — 0.9%**. Of those 11:

| Swiss-Prot name | n |
|---|---|
| "ADP-ribosylhydrolase ARH1" | 4 |
| **"Inactive ADP-ribosyltransferase ARH2"** | **7** |

**A majority of the InterPro entry's own reviewed members are entries Swiss-Prot itself names
"Inactive" and annotates with a CAUTION that they lack the catalytic residues — and the entry
still maps to the activity.** Note also what the entry gets *right*: ADPRS/ARH3 is excluded from
IPR012108 altogether, so InterPro does separate ARH3 from ARH1. It just does not separate ARH2.

### Route 2: an ARBA rule keyed on a CATH FunFam **name**

`GO_REF:0000120`'s WITH/FROM cites `ARBA:ARBA00088955`. Fetching the rule
(`https://rest.uniprot.org/arba/ARBA00088955`) gives, verbatim, a single condition set:

```
FunFam id = 1.10.4080.10:FF:000002   AND   taxon = Mammalia   ->   GO:0003875
```

And ADPRHL1's own cross-reference reads
`DR   FunFam; 1.10.4080.10:FF:000002; ADP-ribosylarginine hydrolase isoform X1; 1.`

**The FunFam does not separate the active ARH1 from the dead ARH2** — P54922, Q8NDY3, Q8BGK2,
Q5XIB3, Q3ZBM1, Q5RCJ0, Q6AZR2 and Q5XJB9 all match `FF:000002`, while ARH3 sits in a different
FunFam (`FF:000001`). The FunFam's *name* asserts the activity; nothing in the rule examines a
residue. This is the campaign's "a domain's NAME is not an activity" trap in its purest form.

**The rule's taxon clause makes a falsifiable prediction, and GOA confirms it.** If
ARBA00088955 is restricted to Mammalia, the five mammalian ARH2 entries should get `GO:0003875`
via `GO_REF:0000120` and the two non-mammals via `GO_REF:0000002` instead. Queried:

| accession | species | GO:0003875 | GO:0000287 | GO:0051725 |
|---|---|---|---|---|
| Q8NDY3 | human | IEA(GO_REF:0000120) | IEA(GO_REF:0000002) | IEA(GO_REF:0000002) |
| Q8BGK2 | mouse | IEA(GO_REF:0000120) | IEA(GO_REF:0000002) | IEA(GO_REF:0000002) |
| Q5XIB3 | rat | IEA(GO_REF:0000120) | IEA(GO_REF:0000002) | IEA(GO_REF:0000002) |
| Q3ZBM1 | bovine | IEA(GO_REF:0000120) | IEA(GO_REF:0000002) | IEA(GO_REF:0000002) |
| Q5RCJ0 | orangutan | IEA(GO_REF:0000120) | IEA(GO_REF:0000002) | IEA(GO_REF:0000002) |
| Q6AZR2 | *X. laevis* | IEA(GO_REF:0000002) | IEA(GO_REF:0000002) | IEA(GO_REF:0000002) |
| Q5XJB9 | zebrafish | IEA(GO_REF:0000002) | IEA(GO_REF:0000002) | IEA(GO_REF:0000002) |

Exactly as predicted. **21 annotations across 7 species, every one IEA, not one with any
experimental, IBA or ISS support anywhere in the family.**

Positive controls that the endpoint and the terms are alive: human ADPRH carries `GO:0003875`
by IBA + IDA + IEA + IMP, and human ADPRS carries `GO:0140290` by IBA + IDA + IEA.

Negative with control: **no ARH2 orthologue carries any ARH3-type term** (`GO:0140290`,
`GO:0004649`, `GO:0140292` all return zero for all seven). So the mis-assignment is
specifically to the arginine specificity — there is no reading on which ADPRHL1 is a
mis-filed serine/PAR hydrolase instead. My Part-2 census agrees: ADPRHL1 keeps only 6–7 of
ARH3's 17 sites while the ARH3 clade keeps 14–17. **It fails against both active references.**

## The ISS rows: a legitimate ortholog transfer with a split-donor problem behind it

All three ISS rows cite `UniProtKB:Q6AZR2` = `ARHL1_XENLA`, reviewed Swiss-Prot, 354 aa,
*Xenopus laevis* adprhl1 — a true 1:1 ortholog at 74.6% identity, not a paralog. The transfer
is sound. WITH/FROM entity type is correct for ISS (the sequence-similar entity, not a partner).

Fully-paginated reference-projection test on the underlying paper:
**`PMID:27217161` → 3 annotations over 1 entity** (Q6AZR2: `GO:0003242`, `GO:0055003`,
`GO:0030017`, all IMP). One curator reading one paper about one gene — not a bulk import, and
no phenotype spreading across a set. The benign shape, reported because the check was run.

**But the same test on the 2020 CRISPR paper found a real defect.**
**`PMID:32726316` → 10 annotations over 2 entities**, and the two entities are
`A0A8J0UG54` and `A0A8J0UIM8` — **TrEMBL accessions for `adprhl1.L`, the same *Xenopus laevis*
gene**, curated by **Xenbase**, not the Swiss-Prot entry `Q6AZR2` that UniProt's ISS pipeline
transfers from. Terms curated there and nowhere else in the family:

- `GO:0055005` **ventricular cardiac myofibril assembly** (IMP) — a child of the `GO:0055003`
  that human does receive
- `GO:0030041` actin filament polymerization (IMP)
- `GO:0036342` post-anal tail morphogenesis (IMP) — *Xenopus*-specific, not transferable

So the human record inherits the 2016 paper and is blind to the 2020 one, **because the two
papers were curated onto different accessions of the same frog gene.** That is a fixable
curation defect and it is the reason `GO:0055005` is proposed here as a NEW row rather than
found in GOA.

`GO:0030041` was considered and **declined for human**: the *Xenopus* IMP is a morphological
inference from myofibril phenotypes rather than a polymerization assay, and the human
mechanism places any actin effect downstream of ROCK–myosin II. Recording the declined lead
rather than taking it.

## The largest coverage gap: the only human experiment is absent from GOA

`PMID:37880701` — a CRISPR knockout of ADPRHL1 in human H9 embryonic stem cells differentiated
to cardiomyocytes — **contributes zero annotations to GOA** (reference-projection test:
0 annotations, 0 entities). It is the only functional experiment ever performed on the *human*
protein. Its results:

- `[PMID:37880701 "Our results indicate that the expression of β1-integrin was significantly decreased in KO-CM, suggesting that ADPRHL1 deficiency disrupts the FAs in these cells"]`
- `[PMID:37880701 "the expression of Paxillin, a structural protein in FAs, in KO-CM was markedly reduced"]`
- `[PMID:37880701 "ADPRHL1 deficiency disrupted the formation of focal adhesions in cardiomyocytes by excessively upregulating the ROCK"]`–myosin II pathway
- `[PMID:37880701 "the arrangement of sarcomeres was less regular"]` in knockout cardiomyocytes
- `[PMID:37880701 "Our results demonstrated that ADPRHL1-deficient cardiomyocytes exhibited abnormal adhesion, calcium transients and electrophysiological activity."]`

Direction: knockout *decreases* focal adhesion formation, so wild-type ADPRHL1 *promotes* it —
hence `GO:0051894 positive regulation of focal adhesion assembly`, not the bare
`GO:0048041`, since ADPRHL1 is not a structural FA component and the paper's mechanism is
regulatory.

## Checks run that came back negative — recorded so the next reviewer knows they were run

- **Logical-opposite citation cross-product.** No positive/negative regulation pair exists among
  the 7 rows, so there is nothing to intersect. Nothing found because there was nothing to find.
- **Reaction direction / "who modifies whom".** Checked explicitly, because this family is where
  it bites: no row on ADPRHL1 asserts that it *performs* ADP-ribosylation. `GO:0051725` is
  correctly the removal direction; it is wrong here for a different reason (no activity at all),
  not because the arrow points the wrong way. Note the UniProt **name** does invert it — see the
  naming defect below.
- **IntAct.** `findInteractions/Q8NDY3` returns **0** interactions. **Positive control:**
  the identical call returns **17** for P54922 (ADPRH) and **35** for Q9NX46 (ADPRS), both
  HTTP 200. So the zero is real, not a rejected query. Consistent with GOA carrying no
  `GO:0005515` row for this gene. (UniProt's `DR BioGRID; 125253; 2.` records two BioGRID
  entries that have not reached IntAct or GOA; not enough for any annotation.)
- **Retraction / erratum / expression-of-concern sweep.** All **10** cited PMIDs were fetched
  by efetch (all HTTP 200) and both `PublicationType` and `CommentsCorrections/RefType` were
  read: **zero** retractions, errata, corrections or expressions of concern. Crossref
  `update-to`/`relation` additionally clean for **all 10** DOIs, all HTTP 200 (so the check
  ran rather than silently 404ing). The first pass covered only the 8 PMIDs and 7 DOIs held
  at that point, and the two references added later (`PMID:36497109`, `PMID:16278211`) plus
  three unchecked DOIs were swept afterwards rather than assumed — the count that did not
  match the citation list was the prompt to re-run it.
- **Pagination.** Every QuickGO call asserts `numberOfHits == len(results)`. The assertion
  earned its keep once: an unrestricted `GO:0003875` query reports 1728 hits and would have
  silently returned 100.

## affinage

`gates_passed: True`, 6 citations, all numeric PMIDs (no `PMID:bio_*` preprint ids).
**All six verified to concern ADPRHL1/ARH2 specifically** — checked because on the sibling gene
ADPRH the provider returned two citations that resolve to papers about entirely different
proteins. Here they are clean, and the narrative is broadly accurate.

**Its recall is the problem, as usual.** Absent from the affinage record, and decisive here:

| missed | why it mattered |
|---|---|
| `PMID:17075046` | the **only direct measurement** that ARH2 is inactive — and it is titled for **ARH3** |
| `PMID:36497109` | the family review that states the negative across the whole assay panel *and* supplies the "model substrates" caveat |
| `PMID:16278211` | Oka *et al.* 2006, the reference both *Xenopus* papers cite for ARH2's lack of activity |

The first is the campaign's "a paper titled for a PARALOG can hold your gene's answer" pattern
exactly: no ADPRHL1-keyed search returns a paper called "The 39-kDa poly(ADP-ribose)
glycohydrolase ARH3 hydrolyzes O-acetyl-ADP-ribose". It was found by searching the *family*.

## A UniProt naming defect worth reporting

Q8NDY3's RecName is **"Inactive ADP-ribosyltransferase ARH2"** (`ECO:0000305`), and the same
name is on all seven ARH2 orthologues. **"Transferase" is the wrong direction.** The entry's own
`SIMILARITY` line places it in the ADP-ribosyl**glyco**hydrolase family, its own AltName is
"[Protein ADP-ribosylarginine] hydrolase-like protein 1", and no ARH-family member has ever been
proposed to *add* ADP-ribose. Naming a dead hydrolase after the opposite reaction is the same
"who modifies whom" confusion the campaign flags for annotations, occurring in a protein name —
and it is the name GOA prints in the `GENE NAME` column of every one of these rows. Suggested
correction: "Inactive ADP-ribosylhydrolase ARH2", matching `ADPRH_HUMAN`'s
"ADP-ribosylhydrolase ARH1" and `ADPRS_HUMAN`'s "ADP-ribosylhydrolase ARH3".

## Other literature, weighed and mostly not annotated

- **`PMID:35816343`** (prostate cancer): a recurrent germline `p.D78V` allele in African-American
  families; `[PMID:35816343 "expression of the wild-type ADPRHL1 in prostate cancer cells suppressed cell proliferation and oncogenesis"]`
  and `[PMID:35816343 "the ADPRHL1 mutant activates PARP1"]`. This is ectopic expression in
  cancer cell lines, one variant, one ancestry group; the direction (WT restrains PAR
  accumulation) is intriguing given the family, but there is no demonstration that ADPRHL1
  itself acts on ADP-ribose. **Not proposed as an annotation.** D78 is not one of the residues
  in the census's site set.
- **`PMID:40801020`** (lung adenocarcinoma):
  `[PMID:40801020 "ARH2 promotes M2 macrophage polarization and suppresses immune responses by regulating the FPR2/PI3K/AKT signaling pathway"]`.
  siRNA in a nanoparticle-delivery study; a tissue and direction opposite to the prostate work.
  Affinage itself rates it Low confidence. **Not proposed.**
- **`PMID:34492228`** (HDAC4/MEF2/SUV39H1 repression of the *Adprhl1* promoter): this is about
  regulation **of** the gene, not a function **of** the protein. Cached abstract-only
  (`full_text_available: false`), so nothing is asserted about its full text. **Not annotated**
  — a promoter being a target is not a gene product function.
- **An `Arh2`-knockout mouse exists only as a bioRxiv preprint** (`10.1101/2023.02.07.527494`,
  "ADP-ribose-acceptor hydrolase 2 (Arh2) deficiency results in cardiac dysfunction,
  tumorigenesis, inflammation, and decreased survival"), with **no PubMed id**. Not cited as a
  PMID and nothing rests on it, per the campaign's preprint rule. Worth knowing because the 2022
  review says `Thus far, an Arh2-deficient mouse model has not been reported.` and the mouse
  evidence in GOA is limited to
  `[PMID:32726316 "Mice lacking Adprhl1 exons 3-4 are normal but production of the smaller ADPRHL1 species is unaffected"]`
  — which is **not a null allele**, so it does not contradict the cardiac requirement.
- **`PMID:12070318`** is UniProt's reference [1] for the isoform-1 mRNA only. It is a survey of
  the *ecto-ADP-ribosyltransferase* (ARTC) family — a **different** family from the ARH
  hydrolases — and is the most likely origin of the "ADP-ribosyltransferase" in the RecName.
  No functional claim about ARH2 is drawn from it here.

## Verdict summary

| # | term | evidence | route | action |
|---|---|---|---|---|
| 1 | GO:0000287 magnesium ion binding | IEA | InterPro2GO / IPR012108 | **REMOVE** |
| 2 | GO:0003875 ADP-ribosylarginine-[protein] hydrolase activity | IEA | ARBA00088955 + IPR012108 | **REMOVE** |
| 3 | GO:0030017 sarcomere | IEA | SubCell SL-0313 | ACCEPT |
| 4 | GO:0051725 protein de-ADP-ribosylation | IEA | InterPro2GO / IPR012108 | **REMOVE** |
| 5 | GO:0003242 cardiac chamber ballooning | ISS | Q6AZR2 | ACCEPT |
| 6 | GO:0030017 sarcomere | ISS | Q6AZR2 | ACCEPT |
| 7 | GO:0055003 cardiac myofibril assembly | ISS | Q6AZR2 | ACCEPT |
| 8 | GO:0055005 ventricular cardiac myofibril assembly | ISS | Xenbase-curated *X. laevis* adprhl1 | **NEW** |
| 9 | GO:0051894 positive regulation of focal adhesion assembly | IMP | human hESC-CM knockout | **NEW** |

The two `GO:0030017` rows take the same action, as the repo's "same term, same action" rule
requires; they are two routes to one underlying observation (UniProt's `SUBCELLULAR LOCATION:
Cytoplasm, myofibril, sarcomere` line is itself `ECO:0000250|UniProtKB:Q6AZR2`, so the SubCell
IEA and the ISS row are the same datum arriving twice).

No molecular function term is proposed. ADPRHL1's MF is genuinely unknown: no ligand, no
substrate, no verified partner, zero IntAct interactions. Proposing `GO:0098772` or
`GO:0008092` (affinage's own grounding) would be inventing an annotation to express a hunch.
That gap is recorded in `knowledge_gaps` instead.

## Process log

- Worktree `/private/tmp/wt-ADPRHL1`, branch `paint/ADPRHL1`, cut from `origin/main` at
  `89e6622d4`.
- `git --version` is 2.37.0, so `git merge-tree --write-tree` is unavailable; conflict probing
  uses `git merge origin/main --no-edit` + `git diff --diff-filter=U`.
- The census script's break-test caught a defect **in the break-test itself** on its first run:
  an unanchored `"56D" in m` substring test also matched the other orthologues' rows. Anchored on
  the accession. Same shape as the brief's `"reviewed" in entryType` and
  `"reference_id:" in line` traps.
