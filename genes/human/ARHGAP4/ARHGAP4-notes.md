# ARHGAP4 (P98171) — review notes

X-linked RhoGAP at Xq28, formerly `C1` / `RGC1` / `p115` / `KIAA0131`. 946 aa, with
F-BAR (19–317), Rho-GAP (507–695) and SH3 (746–805) domains
[file:human/ARHGAP4/ARHGAP4-uniprot.txt "FT   DOMAIN          507..695"]. Immediately
adjacent to *AVPR2*, which is why almost all human genetic information about it comes
from contiguous-gene deletions.

## Headline: this is a coverage problem, not an over-annotation problem

`reference_coverage.py` queried QuickGO **by reference** for 19 primary ARHGAP4
papers. **16 of 19 produced no GO annotation on ARHGAP4 in any species.** The three
that did:

| PMID | species | rows |
|---|---|---|
| 8570618 Tribioli 1996 | human | 4 × TAS |
| 12414125 Foletta 2002 | **rat** | `GO:0005096` **IDA**, `GO:0007399` IEP, `GO:0035023` NAS, `GO:0005874` IDA |
| 17804252 Vogt 2007 | **rat** | `GO:0010764` IMP, `GO:0030517` IMP, `GO:0030426` IDA |

Human `P98171` therefore has **no experimental molecular-function or biological-process
annotation at all**. Its only IDA rows are localisation (HPA cytosol, LIFEdb cytoplasm).
Everything functional is IBA, Ensembl-projected IEA, or 1996 TAS.

The Ensembl `GO_REF:0000107` rows are not free-floating: every one projects a *curated
rat row*, and the rat rows trace to the two mechanistic papers above. So the human
record is a faithful shadow of rat experiments — which is the right thing for it to be,
and worth stating rather than second-guessing.

## Substrate specificity, and why GO cannot hold it

The only direct activity measurement is rat: "In vitro, recombinant ARHGAP4 stimulated
the GTPase activity of three members of Rho GTPases, Rac1, Cdc42 and RhoA"
[PMID:12414125 "In vitro, recombinant ARHGAP4 stimulated the GTPase\nactivity of three members of Rho GTPases, Rac1, Cdc42 and RhoA."].
Reactome commits further, filing ARHGAP4 under `R-HSA-9013144 RAC1 GAPs stimulate RAC1
GTPase activity`.

Neither commitment can be written as a GO term. `check_gap_terms.py` resolved the
candidate terms across **three independent services** (OLS4, the GO API at
`api.geneontology.org`, and this repo's `cache/go/terms.csv`), because QuickGO
**silently resolves merges** — ask it for `GO:0005100` and it returns `GO:0005096`'s
record flagged `isObsolete: false`, which reads as "the term is fine". It did exactly
that for 7 of the 9 ids queried. Across the independent services:

- `GO:0005100` Rho, `GO:0005099`/`GO:0005098` Ras, `GO:0008060` ARF, `GO:0005097` Rab,
  `GO:0046582` Rap GAP activity — **all merged into `GO:0005096`**;
- `GO:0017048` Rho GTPase binding — merged into `GO:0031267` small GTPase binding, so
  the binding route loses Rho specificity too;
- `GO:0005096` has **zero `is_a` children**. It is not childless: QuickGO reports one
  child, `GO:1902773 GTPase activator complex`, via **`capable_of`** — a complex that is
  capable of the activity, not a more specific activity. OLS4 reports zero direct
  subclasses.
- the merged names survive only as **synonyms** of `GO:0005096` ("Rho GTPase activator
  activity", "Rac GAP activity", …).

So the merge was deliberate and complete, and no term is being requested. Substrate
identity is carried in `core_functions[].substrates` and as `RO:0002233 has_input`
extensions instead. This is the same conclusion the sibling ARHGAP21 review reached, on
the same terms, reached here independently and with the QuickGO caveat added.

## The arginine finger: present, and that settles nothing

`arginine_finger.py` aligns UniProt-delimited Rho-GAP domains to ARHGAP1/p50RhoGAP and
projects the structurally resolved catalytic arginine.

The anchor is verified structurally, not assumed: PDB **1TX4** is the
RHOA·GDP·AlF4⁻·p50RhoGAP transition-state complex; SIFTS maps chain A 1–198 onto
`Q07960` 234–431, so Arg-282 is deposited residue 49 — and the script confirms residue
49 is **ARG** with its guanidinium **2.73 Å** from the AlF4⁻ moiety.

Result: **ARHGAP4 carries R543** at that column. The computed alignment agrees with
UniProt's independent PROSITE-ProRule `SITE` in all 11 panel members, positives and
known-dead alike (ARHGAP36 T258, DEPDC1B I231, OCRL1 Q757, INPP5B Q852 — the same four
Amin et al. 2016 [PMID:27481945] list as lacking the finger).

**But residue identity and curated activity are decoupled in both directions**, and the
script demonstrates both from GOA rather than asserting it:

- *arginine present, activity denied* — **ARHGAP11B** (`Q3KRB8`) retains the arginine at
  the aligned column and carries **two `NOT|enables GO:0005096` IDA rows**
  (PMID:25721503, PMID:27957544). UniProt names it "Inactive Rho GTPase-activating
  protein 11B".
- *arginine absent, activity annotated* — **OCRL1** carries `GO:0005096` by **IDA**,
  ARHGAP36 by IBA, ARAP2 by IEA+IBA, FAM13B by TAS, all without the arginine.

Amin et al. add the mechanistic reason not to over-read the residue:
[PMID:27481945 "We have found that the RHOGAP domain itself is nonselective and in some cases rather inefficient under cell-free conditions."]
and
[PMID:27481945 "Thus, we propose that other domains of RHOGAPs confer substrate specificity and fine-tune their catalytic efficiency in cells."].
ARHGAP4 (listed as "p115", `P98171`, entry 42) appears in that paper's Table 1 of 66
RHOGAPs, inside the 57 that "have a common catalytic domain capable of terminating RHO
protein signaling", but it is **not among the 14 whose kinetics were measured**
[PMID:27481945 "The activity of 14 representatives of the RHOGAP family toward 12 RHO family proteins was determined in real time."].
Verified by grepping the PMC full text, where the exact token `ARHGAP4` occurs once, in
that table. A web-search summary claiming Amin measured an "ARHGAP4-R543K mutant by
FRET" is **not in the paper** and was not used.

So: the residue is intact, the fold is intact, the only activity measurement is a rat
in-vitro assay, and nothing here licenses either "therefore active in human" or
"therefore inactive".

## Loss of function: unremarkable in both species

- **Mouse.** IMPC reports **0 significant phenotypes** for `Arhgap4`
  (MGI:2159577); 17 of 24 physiological systems show no significant impact.
- **Human.** Contiguous Xq28 deletions removing *AVPR2* plus all or part of *ARHGAP4*
  cause nephrogenic diabetes insipidus attributable to *AVPR2*
  [PMID:10425039], [PMID:11754100], [PMID:22965914]. The one SCID case with a 34.4 kb
  deletion is explicitly **not** attributed to ARHGAP4: "Other patients with NDI, but
  without immunodeficiency, have had deletions that remove all ARHGAP4 except exon 1"
  [PMID:16781893 "Other patients with NDI,\nbut without immunodeficiency, have had deletions that remove all ARHGAP4 except\nexon 1"],
  and the authors attribute the SCID to loss of a conserved intergenic regulatory
  element between *ARHGAP4* and *ARD1A*.

Two single-family variant reports exist — `T491M` in an intellectual-disability family
[PMID:26707211] and variants in X-linked early-onset temporal lobe epilepsy
[PMID:39060771, a Letter with no abstract in the PubMed record]. Neither produced a GO
annotation and neither is, on its own, evidence of a molecular function. Note that
T491 lies **outside** the Rho-GAP domain (507–695).

## PANTHER placement and what the IBAs actually assert

ARHGAP4 sits in **PTHR14166 "SLIT-ROBO Rho GTPase-activating protein"** alongside
SRGAP1/2/3 and the hominin-specific SRGAP2B/2C. `resolve_entities.py` joins each
WITH/FROM token onto the family's PAINT export:

| node | term | taxon | seeds |
|---|---|---|---|
| PTN002306152 | `GO:0005096` | Opisthokonta | Srgap2, Srgap1, **Arhgap4(rat)**, SRGAP2, srgp-1 |
| PTN001021265 | `GO:0030336` | Eumetazoa | **Arhgap4(rat)**, SRGAP2, srgp-1 |
| PTN002680572 | `GO:0005737` | Euteleostomi | **ARHGAP4 itself** |
| PTN008351815 | `GO:0007399` | (unscoped) | Srgap2, **Arhgap4(rat)**, SRGAP2, SRGAP2C |
| PTN008351815 | `GO:0051963` | (unscoped) | Srgap2, Srgap3, SRGAP2C, SRGAP2B |
| PTN002680580 | `GO:0043197`, `GO:0098978` | Euteleostomi | **not inherited by ARHGAP4** |

Three things follow.

1. `PTN002680572` is seeded by `UniProtKB:P98171` alone. Per CLAUDE.md this is the
   legitimate marker that experimental grounding exists on the target (ARHGAP4 has
   cytoplasm IDA from LIFEdb), **not** circularity.
2. `GO:0051963 regulation of synapse assembly` is the one inherited assertion whose seed
   set contains **no ARHGAP4-lineage member** — it is Srgap2, Srgap3, and two
   hominin-specific paralogs that arose by partial duplication of *SRGAP2*.
3. The same curator placed the *synaptic localisation* terms on a **sibling** node,
   `PTN002680580`, which ARHGAP4 does **not** inherit. The boundary excluding ARHGAP4
   from the synaptic compartment was therefore drawn deliberately, which makes the
   synapse-assembly inheritance the odd one out rather than part of a consistent
   neuronal package.

## Comparator check — which refuted three of my four candidate MODIFYs

`comparator_terms.py` tests each proposed replacement as a prediction about seven
well-curated RhoGAPs (ARHGAP1, ARHGAP35, ARHGAP17, ARHGAP21, ARHGAP24, SRGAP2, DLC1):

| proposal | comparators on current term | on proposed | verdict |
|---|---|---|---|
| `GO:0007266` → `GO:0035023`/`GO:0035024` | 2/7 | 1/7, 2/7 | **dropped** |
| `GO:0007165` → `GO:0035023` | **7/7** | 1/7 | **dropped** |
| `GO:0005737` → `GO:0005938` cell cortex | 4/7 | **0/7** | **dropped** |
| `GO:0007010` → `GO:0051497` | **0/7** | 1/7 (DLC1 IDA) | **kept** |

`GO:0007266` on a RhoGAP is an established convention (ARHGAP1 TAS, ARHGAP35 IBA), not
an error. `GO:0007165` is a uniform InterPro2GO product on all seven comparators, so
rewriting it on one gene would be idiosyncratic. No comparator carries cell cortex,
despite the 1996 paper describing "a narrow cytoplasmic region just below the plasma
membrane" — so that observation stays a knowledge gap, not an annotation.
`GO:0007010 cytoskeleton organization` is the genuine outlier: **no** comparator carries
it, and the cited observation is inhibition, which is a regulation term.

## Reproducing the analyses

```bash
cd ARHGAP4-bioinformatics
uv run --with biopython --with requests python arginine_finger.py     # -> arginine_finger.json
uv run --with requests python check_gap_terms.py                      # -> gap_terms.json
uv run --with requests python reference_coverage.py                   # -> reference_coverage.json
uv run --with requests python resolve_entities.py                     # -> entities.json
uv run --with requests python comparator_terms.py                     # -> comparator_terms.json
uv run python audit_review.py --self-test                             # invariants, no network
```

Each script takes `--self-test`, which breaks the document or the anchor on purpose and
requires every guard to fire, with negative controls that must stay silent.

## Reference caveat

Affinage cites `PMID:40817404` (NPJ Precis Oncol 2025) for the MYH9/β-catenin/c-Jun
result. An earlier version of the same work, `PMID:40553870`, is **WITHDRAWN** from
*Int J Biol Macromol* — "withdrawn at the request of the author(s) and/or editor due to
an error in the publishing process", i.e. a publishing error, not a data retraction. The
republished version stands, but the pair is worth flagging.

Affinage's record passed its trust gates (accession `P98171`, no non-human organism
token, `self_evaluation_pairwise: win`, `faith_pct: 100`) and its narrative is accurate
as far as it goes, but it returned **11 citations** and missed every human-genetics
paper (PMID:16781893, PMID:18489790, PMID:10425039, PMID:22965914, PMID:26707211,
PMID:39060771) and the family-wide RHOGAP kinetics survey (PMID:27481945). Those were
found by PubMed queries on the symbol and its synonyms, not by the provider.
