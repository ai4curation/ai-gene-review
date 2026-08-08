# ADAM5 (human) — review notes

UniProt `Q6NVV9` · HGNC:212 · NCBI Gene 255926 · Ensembl `ENSG00000196115` · 8p11.22

## 1. The premise checked first: is ADAM5 a pseudogene?

Yes, and from three independent authorities, none of which is the gene's family name.

**HGNC.** `locus_type: pseudogene`, `locus_group: pseudogene`, approved name *"ADAM
metallopeptidase domain 5 (pseudogene)"*, previous symbol `ADAM5P`. The RefSeq accession
is `NR_001448` — an `NR_` prefix, i.e. a non-coding RNA reference sequence, not `NM_`.

**NCBI Gene 255926.** Description *"ADAM metallopeptidase domain 5 (pseudogene)"*.

**UniProt Q6NVV9.** Swiss-Prot reviewed, but `PE 5: Uncertain` — the protein-existence
level reserved for entries whose existence is doubtful — and an explicit caution:

> [file:human/ADAM5/ADAM5-uniprot.txt "CAUTION: Could be the product of a pseudogene. Not expected to have"]

All eleven `DR EMBL` cross-references on the entry are `NOT_ANNOTATED_CDS`: no EMBL record
annotates a coding sequence for this locus. The 412-residue sequence in the entry is a
*putative* conceptual translation, which is why the recommended name begins "Putative".

So the premise held. But the interesting part is what it is a pseudogene *of*, and the two
directions in which the naive inference from "pseudogene" could go wrong.

## 2. The primary literature: a measured protein-level negative

The gene's own primary reference states the conclusion in its title
[PMID:10417343 "Transcripts encoding the sperm surface protein tMDC II are non-functional in the human."].
The abstract gives both the sequence-level and the protein-level evidence:

> [PMID:10417343 "Here we report the existence of multiple isoforms of human tMDC II transcripts in the human, all of which are also non-functional owing to the presence of deletions and in-frame termination codons, when compared with the macaque orthologue, a finding which is further supported by the lack of immunoreactivity on Western blots of human testis and sperm extracts probed with a macaque anti-tMDC II polyclonal antiserum."]

Two things worth separating. The *transcripts exist* — this is a transcribed pseudogene,
not a silent one; the same paper reports multiple alternatively spliced human tMDC II
transcripts, and UniProt records seven isoforms from it. What is absent is the *protein*.
A macaque antiserum raised against the orthologous protein detects nothing on human testis
or sperm extract. That is a measured negative at the protein level, and per this campaign's
experience a measured negative is usually the most decision-relevant evidence available for
a dark gene.

The context is a lineage-wide loss. The same group had already shown fertilin alpha and
tMDC I to be non-functional in humans
[PMID:10417343 "Of these, two (fertilin alpha and tMDC I) have recently been shown to be non-functional in the human."],
and an HGNC census of the testis/epididymis-expressed ADAMs confirms the group is
unusually pseudogene-rich: **ADAM1A, ADAM1B, ADAM3A, ADAM3B, ADAM5 and ADAM6 are all
HGNC-typed pseudogenes**, while ADAM2, ADAM7, ADAM18, ADAM20, ADAM21, ADAM29 and ADAM30
remain protein-coding. Note the pseudogenes are *not* one contiguous cluster - I wrote that
first and the query refuted it. Only ADAM3A and ADAM5 share 8p11.22 (with the coding ADAM2,
ADAM9 and ADAM18); ADAM1A and ADAM1B are at 12q24, ADAM3B at 16q12.1 and ADAM6 at 14q32.33.
The losses are dispersed across four chromosomes, which makes them independent events rather
than one deletion. ADAM5 is the **only pseudogene of the six with a UniProt accession at
all**, which is precisely why it turns up on a protein-keyed worklist while its equally
pseudogenised neighbours do not.

## 3. What the orthologue does — and why that is not this gene's function

The decisive functional paper appeared in 2026 and is a mouse knockout
[PMID:41263505 "ADAM5 is required for sperm-zona pellucida binding and sperm oviduct migration"]:

> [PMID:41263505 "Adam5 knockout (KO) male mice are severely subfertile, despite exhibiting normal testicular morphology, sperm structure, and motility. Adam5 KO sperm failed to transit the uterotubal junction (UTJ) and displayed severe defects in zona pellucida (ZP) binding, phenotypes that resemble those observed in Adam2 and Adam3 knockout mice."]

and the authors themselves draw the human boundary:

> [PMID:41263505 "While ADAM5 is a pseudogene in humans, our results provide valuable insights into the function of ADAM family proteins in mammalian reproduction."]

That is a fourth independent statement of the pseudogene status, from primary literature
published this year, and it is the cleanest one to cite because it comes from authors who
had every incentive to claim human relevance.

The orthologue's mechanism is complex membership rather than catalysis — mouse ADAM5 loss
reduces ADAM2 and ADAM3 levels on sperm
[PMID:41263505 "Western blot analysis revealed a significant reduction in the levels of ADAM2 and ADAM3 in Adam5 KO spermatozoa, supporting the previous finding that ADAM5 interacts with these proteins to form a complex."],
consistent with the earlier review describing an ADAM2–ADAM3–ADAM5 complex
[PMID:22926424 "Some of these sperm ADAMs are assembled into potentially functional complexes, including ADAM1B-ADAM2, ADAM2-ADAM3-ADAM4, ADAM2-ADAM3-ADAM5, and ADAM2-ADAM3-ADAM6."].
In macaque the protein is on the sperm surface and is proteolytically processed during
epididymal transit
[PMID:10645274 "we have localized a number of these MDC proteins (fertilin alpha, fertilin beta, tMDC I, tMDC II and tMDC III) to spermatogenic cells and demonstrated that they are processed as spermatozoa pass through the epididymis"].
Porcine ADAM5 has been identified by LC-MS/MS as a sulfated-Lewis-X-binding sperm protein
[PMID:28296340 "Following bottom-up LC-MS/MS analysis, among the two bands that bound sulfated Lewis X, ADAM5, which spermatozoa, was confidently identified."].

None of this transfers. Every one of these results is in a species whose ADAM5 gene is
intact; transferring them to the human locus is exactly the inference the review must not
make.

## 4. Bioinformatics: what the human locus actually lost

Full analysis and reproducible script in `ADAM5-bioinformatics/`
(`uv run python analyze_adam5.py`; `--self-test` break-tests the guards).

**Ortholog length panel.** Five reviewed ADAM5 entries: macaque 756 aa (PE 1), mouse 751
(PE 1), guinea pig 777, rat 709, human **412** (PE 5). Every non-human entry carries an
annotated Peptidase M12B domain; the human entry has none. Checking length against
orthologues before scoring anything was deliberate — a short reference sequence otherwise
manufactures "substitutions" out of residues that are simply not there.

**Alignment to macaque (Q28483), the species in which tMDC II was characterised.** The
human sequence is not a diverged paralogue: the retained blocks are 96.2% and 83.6%
identical. It is the same gene with a **single 246-residue internal deletion** removing
macaque 196–441, fused after human residue 162, plus loss of macaque 1–43 and 691–756.

Coverage of each macaque feature by the human sequence:

| macaque feature | fraction covered |
|---|---|
| Signal 1–16 | 0.000 |
| Transmembrane 699–719 | 0.000 |
| Peptidase M12B 183–380 | 0.066 |
| Disintegrin 389–478 | 0.411 |
| Propeptide 17–142 | 0.786 |
| EGF-like 630–664 | 1.000 |

So the human putative product has lost the **signal peptide**, the **metalloprotease
domain** and the **transmembrane anchor**, and the disintegrin domain is itself truncated
because the deletion cuts through it. A product with neither secretory targeting nor a
membrane anchor could not reach the sperm surface even if it were translated — which is why
the cellular-component `ND` is as well founded as the molecular-function one.

A consequence worth flagging to UniProt: the human entry's own `DOMAIN 111..199
Disintegrin` **straddles the deletion junction at 162/163**. Its N-terminal half aligns to
macaque 144–195, upstream of the macaque disintegrin domain, and only its C-terminal ~37
residues to real disintegrin sequence (macaque 442–478). The human disintegrin call is a
fusion artefact of the deletion, not a conserved intact domain.

**Catalytic motif scan, controls in both directions.** No `HExxHxxGxxHD`, and no `HExxH`
substring at all, anywhere in the 412 residues. The scan discriminates: ADAM10, ADAM17,
ADAM9 and ADAM19 all return an intact motif (`HEVGHNFGSPHD`, `HELGHNFGAEHD`,
`HELGHNLGMNHD`, `HEMGHNFGMTHD`), while every sperm ADAM UniProt calls non-catalytic returns
none. A scan that could only fail one way would not be worth running.

## 5. Two predicted defects that were NOT present — reported as non-confirmations

The brief flagged two live routes by which a pseudogene acquires a bogus molecular
function. Both were tested and neither is present on this gene.

**Bulk TAS import (the ADGRA2/GDB pattern).** No TAS row exists on Q6NVV9, from
`PMID:15203201` or anything else. Nothing to run the reference-projection test against.

**InterPro2GO fold-to-activity mapping.** No `IEA:InterPro` row exists either. QuickGO,
fully paginated with `numberOfHits == len(results)` asserted, returns **exactly three
annotations** for Q6NVV9, matching the local GOA TSV row-for-row: `GO:0003674`, `GO:0005575`
and `GO:0008150`, all `ND` against `GO_REF:0000015`. `DR PAN-GO; Q6NVV9; 0 GO annotations
based on evolutionary models` — so the "no-IBA" worklist label happens to be correct here,
though I verified it rather than trusting it.

There is therefore **no molecular-function, cellular-component or biological-process claim
on this gene to retract**. GOA's treatment is already correct, and the reflex to find a
catalytic over-annotation on a pseudogene would have manufactured a finding that is not
there.

## 6. Where the defect actually lives: a negative control that identifies the rule

The right question was not "did the error hit ADAM5?" but "which relatives did it hit, and
what boundary separates them?"

A detector was built for *fold present + zinc site absent + `GO:0004222` nevertheless
annotated*, and run across the panel:

- **Fires** on all four non-human ADAM5 orthologues (macaque, mouse, rat, guinea pig) and
  on human **ADAM2**, **ADAM18** and **ADAM7** — every one of which has an annotated
  Peptidase M12B domain, **no `HExxH` core at all**, and 2 × `GO:0004222` by `IBA` + `IEA`.
- **Clean** on ADAM10/17/9/19 (zinc motif intact — the term is correct there) and on human
  ADAM5 (no fold, no term).

Mouse Adam5 is the sharpest case: UniProt says of the very same entry
`CAUTION: Not expected to have protease activity`, and GOA gives it `GO:0004222
metalloendopeptidase activity` by `IEA:InterPro` from `IPR001590` *and* by `IBA` from
`PANTHER:PTN000224844`. The record contradicts itself, in GOA rather than only upstream in
UniProt.

The boundary identifies the rule the pipeline applied: **it keys on presence of the M12B
fold, not on integrity of the zinc-binding site.**

**Measured, not just inferred.** The panel above is hand-picked, so the rule was re-tested
over **all 331 Swiss-Prot reviewed members** of PANTHER PTHR11905 — the reviewed subset of a
**29,886-protein** family, so these are statements about reviewed entries, not about the
family. Of the members carrying the Peptidase M12B fold, **204/204 (100%)** with an intact
`HExxH` site carry `GO:0004222`, and **37/40 (92%)** *without* any `HExxH` site carry it too.
If the annotation discriminated on the catalytic site the second figure would be near zero.
Note the family-wide measure (exact `GO:0004222` in the UniProt GO cross-references) is a
*different metric* from the panel's descendant-aware QuickGO count, so the script requires the
family run to reproduce the panel's verdict on all 10 panel members present in the reviewed
set before the wider number is reported. ADAM10 and ADAM17 turn out not to be in PTHR11905 at
all — they are classified in another PANTHER family — which is recorded rather than quietly
dropped. Human ADAM5 escaped not because any
pipeline recognised it as non-catalytic, but because pseudogenisation deleted the very fold
the pipeline matches on. That inverts the campaign's usual finding — the pseudogene is the
*clean* member of its family — and it means the correctable defect is real but sits on
ADAM5's relatives, not on ADAM5. Raised in `suggested_questions` rather than acted on,
since none of those genes is in scope here.

I should note the term definition was checked rather than inferred from the label:
`GO:0004222` is defined as *"Catalysis of the hydrolysis of internal, alpha-peptide bonds in
a polypeptide chain by a mechanism in which water acts as a nucleophile, one or two metal
ions hold the water molecule in place…"* — it does assert catalysis and metal-ion
coordination, so a protein with no zinc-binding residues cannot satisfy it. Unlike
`GO:0019825 oxygen binding`, the label here is not misleading.

## 7. The mirror error, tested: is there real expression or protein evidence?

A pseudogene call can be contested, and some annotated pseudogenes carry genuine
transcript- or protein-level evidence. Both were checked.

**Transcript level — positive, and it matters.** The locus is genuinely transcribed:
multiple spliced testis transcripts (PMID:10417343), two independent MGC full-length cDNA
clones from testis [PMID:15489334], RefSeq `NR_001448`, 16 exons. This is a *transcribed*
unitary pseudogene, not a decayed relic. There is even a proposed regulatory role for the
transcript itself: inherited copy-number variation at the ADAM3A/ADAM5 pseudogene pair
associates with oropharyngeal cancer risk, with a suggested ceRNA mechanism
[PMID:36553675 "ADAM5 shared a highly homologous sequence with the ADAM9 3'-UTR, predicted to be a binding site for miR-122b-5p."].
That is an association plus a *predicted* binding site, not a demonstrated activity — it is
recorded as a knowledge gap, not as a function, and it would be an RNA-level function in any
case.

**Protein level — negative, with positive controls.** The EBI Proteins API `proteomics`
endpoint (mapped MS peptides) returns **HTTP 404** for Q6NVV9. On its own a 404 is
uninterpretable, so it was controlled: the same endpoint returns HTTP 200 with 53 peptide
features for human ADAM2, 13 for ADAM18, 6 for mouse Adam5 and 393 for ACTB. The 404 is
therefore a genuine absence of mapped peptide evidence, not an API artefact. This matters
because the UniProt entry does carry `DR PeptideAtlas` and `DR TopDownProteomics` lines,
which look like protein evidence but are database-membership cross-references; UniProt's own
verdict on the same record is `PE 5: Uncertain`.

Note the campaign's `PE 1` rule cuts the other way here and is worth stating explicitly:
this gene is **not** a case where "no experimental data of any kind" would be an overstatement
about the protein. There is abundant experimental data about the *locus* and its
*transcripts*, and a measured negative about the protein.

## 8. Provider record

`affinage_deep_research.py human ADAM5 --write` returned **`no Affinage record content for
ADAM5`** — an empty record, so no `-deep-research-affinage.md` file exists and there is no
`gates_passed` value to report. Per the campaign rule, an empty provider record is not
evidence that literature is absent, and it was not treated as such: the UniProt `RN` list
supplied PMID:10417343, and independent PubMed searches on the *family* and on the
*orthologue* (`ADAM5 AND (sperm OR testis)`, `tMDC II AND sperm`, `ADAM5 zona pellucida`)
surfaced the 2026 mouse knockout PMID:41263505 and the CNV paper PMID:36553675, neither of
which any provider returned. Recorded here so the provider's recall is measurable.

## 9. Checks run, including the ones that came back negative

- **GOA/stub reconciliation.** GOA TSV is 4 lines = 3 data rows; the `fetch-gene` stub
  seeded 3 `- term:` entries. They reconcile exactly — no collapsed `GO:0005515` partner
  rows, because there are none. Verified before starting the review.
- **QuickGO agrees with the local TSV**, 3 annotations, fully paginated with the
  truncation assertion.
- **Retraction / erratum / expression-of-concern.** All seven cited PMIDs checked via
  `CommentsCorrections/RefType` on each article's own PubMed record: zero corrections of
  any type. The three load-bearing DOIs were additionally resolved at Crossref and their
  `update-to` / `updated-by` / `relation` fields inspected, to catch a correction with a
  null PubMed id: all empty.
- **My own tooling bug, caught by a value that refused to add up.** A first pass at the
  correction check read `.//ArticleId` unanchored and returned DOI `10.1002/pros.23950`
  (*The Prostate*) for PMID:36553675, which is published in *Genes*. The unanchored XPath
  had matched a DOI inside the article's own **reference list**. Anchoring to
  `PubmedData/ArticleIdList/ArticleId` gives the correct `10.3390/genes13122408`. Same
  shape as the campaign's substring-needs-an-anchor lesson; the journal mismatch was the
  bug report.
- **Two guard formulations refuted by their own measurement.** The domain-loss check first
  asserted "M12B is the least-covered macaque feature" — false, Signal and Transmembrane
  are 0.000. It was then reformulated as "coverage is bimodal, place a threshold in the
  largest gap" — also false, because the disintegrin domain is genuinely intermediate at
  0.411 (the deletion cuts through it), so no clean gap exists and any threshold would have
  been invented. What survives is threshold-free: every feature the review calls lost is
  less covered than every feature it calls retained, margin 0.345, with an assertion that
  no reference feature is left unclassified. Both wrong versions were caught by running the
  check, not by reading it.
- **Self-test proven able to fail.** Disabling the motif-discrimination guard in a copy of
  the script makes `--self-test` report exactly the two expected failures; the guard was
  restored and the self-test returns 0.
- **Report reproducibility.** A fresh `analyze_adam5.py` run reproduces the committed
  `RESULTS.md` and `results.json` byte-identically (verified by `diff`).
- **A shipped factual error, and a committed guard for it.** The first pushed version of this
  review described the six human ADAM pseudogenes as a single contiguous cluster at one locus.
  An HGNC location query refuted it: only ADAM3A and ADAM5 sit at 8p11.22, while ADAM1A and
  ADAM1B are at 12q24, ADAM3B at 16q12.1 and ADAM6 at 14q32.33 — four chromosomes, so these
  are independent pseudogenisation events, not one deletion. `audit_adam5_claims.py` now pins
  every numeric claim in this review to `results.json` and keeps the retracted wording dead;
  `--against-shipped-defect 4d92ca329` runs it against the exact blob that carried the bug and
  confirms it fires there while staying clean on the current tree. The audit declares its own
  limitation: it matches fixed phrases and cannot catch a paraphrase, so prose still needs
  re-reading when a claim is withdrawn. Note the guard's own side-effect, which caught me
  immediately: because it forbids the literal string outright, I cannot quote the retracted
  wording here even to document it, and my first draft of this bullet failed the audit. That
  is the correct trade — teaching it to permit the phrase "in a citation context" would open
  exactly the bypass the guard exists to close.

## 10. Verdicts

All three GOA rows are `ND` root annotations against `GO_REF:0000015`, and all three are
**ACCEPT**. This is the correct curatorial state for this locus and there is nothing to
modify or remove: `ND` records that a curator looked and found no data, which is exactly
true of the human gene product. No `core_functions` are asserted — inventing one to silence
the "no core functions" warning would be precisely the over-annotation this review exists to
avoid. The substantive findings are carried by `knowledge_gaps`, `suggested_questions` and
`suggested_experiments`.
