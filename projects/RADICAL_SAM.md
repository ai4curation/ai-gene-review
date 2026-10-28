---
title: "Radical SAM Enzymes: GO annotation across the superfamily"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human, ECOLI]
genes: [LIAS, RSAD2, MOCS1, CDKAL1, CDK5RAP1, ELP3, TYW1, TYW1B, RSAD1, bioB, lipA, moaA, nrdG, pflA, rlmN, miaB, rimO, thiH, hemN, hemW, queE, epmB, pflC, ybiY, yjjW, aslB, ydeM, ygiQ, yhcC]
---

# Radical SAM Enzymes

**Bottom line:** across 28 reviewed members of the largest known enzyme
superfamily, the annotation problem is **resolution, not error** — 210 rows
accepted against 49 removed, but 115 modified, almost all pulling a
correct-but-generic term down to the actual reaction. Two findings are
family-wide and machine-fixable. **`GO:1904047` S-adenosyl-L-methionine binding
is absent from GOA for 18 of the 20 members whose catalysis is established**,
although the curated UniProt cofactor note already records SAM as an exchangeable
ligand of the cluster. And **6 members' core activity has no GO term at all** —
three of them for reactions described since 2018, where discovery has simply
outrun the ontology. See [Synthesis](#synthesis).

## Overview

The radical S-adenosyl-L-methionine (SAM) superfamily is the largest known
enzyme superfamily, with hundreds of thousands of members across all domains of
life. Every member shares one chemical trick: a [4Fe-4S] cluster, bound by a
CxxxCxxC (or variant) motif, reductively cleaves SAM to methionine and a
5'-deoxyadenosyl radical, which then abstracts a hydrogen atom from the
substrate. What the radical is used for varies enormously: sulfur insertion
(BioB, LipA), C-C bond rearrangement and cyclisation (MoaA, QueE, ThiH),
glycyl-radical activation (PflA, NrdG), methylation of unactivated carbons
(RlmN, Cfr), methylthiolation of tRNA and ribosomal proteins (MiaB, RimO,
CDKAL1), tRNA acetylation (ELP3), and antiviral nucleotide dehydration (RSAD2,
viperin).

That makes the superfamily a stress test for GO annotation. The shared
radical SAM domain drives a uniform layer of InterPro2GO rows (IPR007197 and
IPR006638 both map to `GO:0003824` catalytic activity and `GO:0051536`
iron-sulfur cluster binding), while the actual reaction is specific to the
subfamily and often to one organism. Many members have an auxiliary cluster
(the second [4Fe-4S] of LipA and MiaB, the [2Fe-2S] of BioB) that is consumed
as a sulfur donor, so "cluster binding" is sometimes cofactor binding and
sometimes substrate binding. A sizeable fraction of members, including several
in *E. coli* K-12, still have no known reaction.

### Goals

1. Review every reviewed (Swiss-Prot) radical SAM protein in **human** (9) and
   ***E. coli* K-12** (20), giving a complete, cross-checkable set for two
   reference proteomes.
2. Settle a **single, consistent treatment** of the domain-driven generic rows
   (`GO:0003824`, `GO:0051536`, `GO:0051539`, `GO:0046872`,
   `GO:1904047` S-adenosyl-L-methionine binding) and apply it to the existing
   radical SAM reviews in this repository.
3. For uncharacterised members (YgiQ, YhcC, RSAD1, the glycyl-radical activase
   paralogs), separate what the domain supports from what is predicted, and
   flag over-annotation from paralogs with known function.
4. Record ontology gaps (missing reaction-level MF terms) as
   `proposed_new_terms` rather than settling for generic terms.

### Scope

Membership is defined by the InterPro **IPR007197 Radical SAM** signature in
reviewed UniProtKB entries, retrieved live on 2026-10-18:

```
https://rest.uniprot.org/uniprotkb/search?query=(xref:interpro-IPR007197)+AND+reviewed:true+AND+organism_id:9606
https://rest.uniprot.org/uniprotkb/search?query=(xref:interpro-IPR007197)+AND+reviewed:true+AND+organism_id:83333
```

Radical SAM reviews from other organisms already in the repository are
included for the consistency pass (Phase 3), not re-reviewed from scratch.

### Starting observation: inconsistent handling of the generic rows

**Resolved by the Phase 3 pass on 2026-10-28; kept here because it is what the
treatment rule below was written to fix.** The 17 radical SAM reviews already in
the repository (matched by IPR007197, PS51918 or IPR058240 in their UniProt
records) treated the same domain-derived terms in contradictory ways:

| Term | Actions used across the 17 reviews |
|---|---|
| `GO:0003824` catalytic activity | MODIFY, MARK_AS_OVER_ANNOTATED, KEEP_AS_NON_CORE, UNDECIDED |
| `GO:0051536` iron-sulfur cluster binding | ACCEPT, MODIFY, KEEP_AS_NON_CORE, MARK_AS_OVER_ANNOTATED |
| `GO:0051539` 4 iron, 4 sulfur cluster binding | ACCEPT, KEEP_AS_NON_CORE, NEW |
| `GO:0046872` metal ion binding | ACCEPT, KEEP_AS_NON_CORE, MARK_AS_OVER_ANNOTATED |

Under the repository guidelines, a true-but-general term is `MODIFY` (to the
specific reaction term the gene carries) or `TOO_GENERAL`, not
`MARK_AS_OVER_ANNOTATED`. `GO:0051536` is a parent of `GO:0051539`, which is
always correct for the radical SAM cluster. Whether `GO:0051539` belongs in
core function (it is the catalytic cofactor) or is non-core was the main
judgement call Phase 3 had to settle; the rule below settles it on catalysis,
and `GO:0051536` is now `MODIFY` on every row that carries it, in both scopes.

### Treatment rule for the generic rows

Adopted 2026-10-18 for all new reviews in this project, and applied to the
pre-existing reviews in the Phase 3 pass (2026-10-28). Hierarchy checked in
QuickGO: `GO:0051539` is_a `GO:0051536`
is_a `GO:0051540` metal cluster binding; `GO:0046872` metal ion binding is
**not** an ancestor of either.

| Term | Action | Replacement / note |
|---|---|---|
| `GO:0003824` catalytic activity | `MODIFY` | The specific reaction MF the gene carries or is shown to have. If no reaction is known (e.g. RSAD1), `KEEP_AS_NON_CORE`: it is already as precise as the evidence allows. |
| `GO:0051536` iron-sulfur cluster binding | `MODIFY` | `GO:0051539`, the descendant the radical SAM cluster always satisfies. |
| `GO:0051539` 4 iron, 4 sulfur cluster binding | `ACCEPT`, or `NEW` where GOA lacks the row | The radical SAM cluster is the catalytic cofactor, so it is core for every active member, and a core cofactor has to be proposable where it is missing (PSEPK/bioB carries `GO:0051537` but not `GO:0051539`). `KEEP_AS_NON_CORE` only where catalysis is not established. |
| `GO:0005506` iron ion binding | `MODIFY` | Same as `GO:0046872`: the iron is bound as a cluster, so replace with `GO:0051539`. |
| `GO:0046872` metal ion binding | `MODIFY` | `GO:0051539` (lateral correction: the iron is bound as a cluster). Keep only if the protein binds a separate metal ion. |
| `GO:1904047` S-adenosyl-L-methionine binding | `ACCEPT`, or `NEW` where GOA lacks the row | Cosubstrate binding, true for every active member. GOA lacks it far more often than not: 18 of the 20 members with established catalysis. |

Never `MARK_AS_OVER_ANNOTATED` for these rows: none of them is false. The same
principle carries to the adjacent generic MF rows that are not in the table
(`GO:0016740` transferase activity, `GO:0016783` sulfurtransferase activity):
they are true, so they are `MODIFY`ed to the reaction term, not flagged.

The rule is enforced in code rather than by reading, over both scopes: for the
29 genes this project reviewed from scratch
(`treatment_rule_deviations`) and for the pre-existing reviews listed in
[`data/phase3_scope.yaml`](RADICAL_SAM/data/phase3_scope.yaml)
(`phase3_rule_conformance.deviations`). Both are asserted empty by
`tests/test_radical_sam_synthesis.py`, so a later edit that breaks the rule
reddens CI instead of going unnoticed. The one sanctioned escape is the rule's
own second branch, recorded as `branch_uses` rather than silently allowed: 17
rows in Phase 4 and 6 in Phase 3, all on members whose catalysis is not
established.

---
# STATUS

Last updated: 2026-10-28 (Phase 3)

## Phase 1: human (9)

- [x] LIAS (O43766): lipoyl synthase, mitochondrial. 21 rows: 11 ACCEPT, 6 MODIFY (incl. 3 obsolete GO:0009107 → GO:0009249), 3 MARK_AS_OVER_ANNOTATED (mouse phenotype ISS), 1 NEW (SAM binding)
- [x] RSAD2 (Q8WXG1): viperin, CTP → ddhCTP dehydratase. 59 rows: 26 ACCEPT, 17 KEEP_AS_NON_CORE (infection-driven mitochondrial/Golgi pools, mouse T-cell rows), 8 REMOVE (protein binding), 3 TOO_GENERAL, 2 MODIFY, 1 MARK_AS_OVER_ANNOTATED, 2 NEW (SAM binding; protein-macromolecule adaptor for IRAK1–TRAF6). Proposed new term: SAM-dependent CTP dehydratase activity (RHEA:65944)
- [x] MOCS1 (Q9NZB8): GTP 3',8-cyclase (MOCS1A) + cPMP synthase (MOCS1B). Reviewed before this project; brought under the treatment rule in Phase 3 (3 generic rows re-actioned, stale `status` corrected)
- [x] CDKAL1 (Q5VV42): cytosolic tRNA t6A37 → ms2t6A methylthiotransferase. 23 rows: 8 ACCEPT, 9 MODIFY, 2 KEEP_AS_NON_CORE, 3 REMOVE (protein binding), 1 NEW (SAM binding). No insulin-secretion terms: upstream necessity, not participation
- [x] CDK5RAP1 (Q96SZ6): mitochondrial tRNA i6A37 → ms2i6A methylthiotransferase. 28 rows: 12 ACCEPT, 6 MODIFY, 4 MARK_AS_OVER_ANNOTATED (nuclear/cytosolic pool, refuted by PMID:28981754), 2 KEEP_AS_NON_CORE, 2 REMOVE (NAS brain development/neuron differentiation), 1 UNDECIDED, 1 NEW (SAM binding)
- [x] ELP3 (Q9H9T3): Elongator catalytic subunit, tRNA U34 acetyltransferase. 42 rows: 12 ACCEPT, 12 MODIFY, 11 KEEP_AS_NON_CORE, 3 MARK_AS_OVER_ANNOTATED (Pol II transcription, cell migration), 4 REMOVE (protein binding), 1 UNDECIDED (nucleolus), 1 NEW (SAM binding)
- [x] TYW1 (Q9NV66): tRNA 4-demethylwyosine synthase. 8 rows: 4 ACCEPT, 3 MODIFY, 2 NEW (cytoplasm IDA PMID:38706838; SAM binding). TYW1-knockout hESCs lack OHyW, so human evidence backs the yeast inference
- [x] TYW1B (Q6NUM6): TYW1 paralog. Activity only inferred; alignment (TYW1B-bioinformatics/) shows TYW1B lacks the FMN phosphate loop and 2 of 3 auxiliary-cluster cysteines. 8 rows: 4 UNDECIDED, 2 KEEP_AS_NON_CORE, 1 MODIFY, 1 REMOVE (protein binding); no core functions asserted
- [x] RSAD1 (Q9HA92): HemW homolog; heme binding (IDA) is the only supported function. 12 rows: 3 ACCEPT, 3 KEEP_AS_NON_CORE, 3 MODIFY, 3 REMOVE (coproporphyrinogen oxidase + porphyrin biosynthesis, transferred from HemN; HemW subfamily lacks that activity)

## Phase 2: *E. coli* K-12 (20 in scope, 19 reviewed)

**lipA is not reviewed.** Its review file is still the `fetch-gene` stub
(`status: INITIALIZED`, 18 `PENDING` rows). Only `lipA-notes.md` was written.
See the 2026-10-19 note below.


Characterised, in priority order:

- [x] bioB (P12996): biotin synthase. 16 rows: 8 ACCEPT, 3 MODIFY, 2 REMOVE (protein binding), 1 KEEP_AS_NON_CORE, 1 NEW (SAM binding, IDA from SAM-bound structure). [2Fe-2S] binding treated as core (sacrificial S donor)
- [ ] lipA (P60716): lipoyl synthase. Notes written; review YAML not started (reviewer stopped; see notes 2026-10-19)
- [x] moaA (P30745): GTP 3',8-cyclase. 17 rows: 11 ACCEPT, 4 MODIFY, 1 KEEP_AS_NON_CORE, 1 MARK_AS_OVER_ANNOTATED (response to heat), 1 REMOVE (cPMP synthase IBA: MoaC's activity, transferred from MOCS1 fusion proteins)
- [x] nrdG (P0A9N8): anaerobic RNR (class III) activase. 23 rows: 8 ACCEPT, 4 MODIFY, 4 MARK_AS_OVER_ANNOTATED (dNTP synthesis: upstream), 4 REMOVE (protein binding; GO:0043365 PflB-activase IEA from IPR012837; GO:0004748 thioredoxin RDP reductase, wrong RNR class), 3 NEW (SAM binding, peptidyl-glycine modification, protein maturation). Proposed new term: anaerobic RNR-activating enzyme activity
- [x] pflA (P0A9N4): pyruvate formate-lyase activase. 22 rows: 12 ACCEPT, 6 MODIFY, 1 KEEP_AS_NON_CORE (K+ binding), 1 MARK_AS_OVER_ANNOTATED (DNA damage response IEP), 2 REMOVE (protein binding), 1 NEW (SAM binding). Sets the activase pattern: MF GO:0043365/GO:0043364, BP GO:0018201 + GO:0051604
- [x] rlmN (P36979): 23S rRNA m2A2503 / tRNA m2A37 methyltransferase. 32 rows: 17 ACCEPT, 7 MODIFY, 3 KEEP_AS_NON_CORE, 7 REMOVE (protein binding), 1 NEW (SAM binding, IDA PMID:21527678)
- [x] miaB (P0AEI1): tRNA ms2i6A37 methylthiotransferase. 19 rows: 9 ACCEPT, 7 MODIFY, 1 REMOVE (protein binding), 1 NEW (SAM binding, ISS: source organism of PMID:15339930 not stated in abstract)
- [x] rimO (P0AEI4): ribosomal protein uS12 Asp89 methylthiotransferase. 17 rows: 10 ACCEPT, 5 MODIFY, 1 REMOVE (tRNA modification IEA from MTTase-wide InterPro; RimO modifies protein), 1 NEW (SAM binding). Core MF GO:0103039; no BP (specific terms obsolete)
- [x] thiH (P30140): 2-iminoacetate synthase (tyrosine lyase). 19 rows: 12 ACCEPT, 3 MODIFY, 1 REMOVE (protein binding), 1 MARK_AS_OVER_ANNOTATED (DNA damage response IEP), 1 NEW (SAM binding). Thiazole synthase left to ThiG
- [x] hemN (P32131): oxygen-independent coproporphyrinogen III oxidase. 14 rows: 8 ACCEPT, 5 MODIFY (GO:0004109 is the O2-dependent HemF reaction → GO:0051989), 1 NEW (SAM binding, IDA structure). InterPro2GO IPR004558 → GO:0004109 should be GO:0051989
- [x] hemW (P52062): heme chaperone. 15 rows: 4 ACCEPT, 6 KEEP_AS_NON_CORE, 1 MODIFY, 4 REMOVE (HemN-derived CPDH + porphyrin biosynthesis; same PTN000358281 IBA as RSAD1). Proposed new term: heme chaperone activity
- [x] queE (P64554): 7-carboxy-7-deazaguanine synthase. 14 rows: 5 ACCEPT, 7 MODIFY, 2 KEEP_AS_NON_CORE (Mg2+; division-inhibitor moonlighting). Proposed new term: 7-carboxy-7-deazaguanine synthase activity (RHEA:27974)
- [x] epmB (P39280): L-lysine 2,3-aminomutase (EF-P modification). 9 rows: 2 ACCEPT, 4 MODIFY, 1 MARK_AS_OVER_ANNOTATED (post-translational protein modification: EpmA/EpmC do the work), 2 NEW (SAM, PLP binding). Proposed new term: (R)-beta-lysine-forming aminomutase (RHEA:44148); GO:0050066 is the (3S) clostridial reaction

Paralogs and uncharacterised, where the risk is over-annotation:

- [x] pflC (P32675): "PFL-activating enzyme 2". Partner PflD is a 1,5-anhydromannitol-6-P lyase, not a PFL (PMID:39283600), so GO:0043365 REMOVEd; core MF GO:0043364. 8 rows: 3 ACCEPT, 3 MODIFY, 1 REMOVE, 1 KEEP_AS_NON_CORE. Genome-context analysis in pflC-bioinformatics/ covers all five activase–GRE pairs
- [x] ybiY (P75794): putative PFL-activating enzyme 3. Partner YbiW is a 1,5-anhydroglucitol-6-P lyase (PMID:39283600); GO:0043365 REMOVEd; core MF GO:0043364. 8 rows, same split as pflC
- [x] yjjW (P39409): putative glycyl-radical enzyme activase. Partner YjjI reaction unknown. 10 rows: 3 ACCEPT, 3 MODIFY, 3 REMOVE (protein binding), 1 KEEP_AS_NON_CORE; core MF GO:0043364
- [x] aslB (P25550): anSME homolog. 5 rows: 2 KEEP_AS_NON_CORE, 1 MODIFY, 2 UNDECIDED (substrate untested; conflicting reports). No core functions. Residue mapping in aslB-bioinformatics/: 16/17 anSME catalytic features retained
- [x] ydeM (P76134): anSME homolog. 6 rows: 2 KEEP_AS_NON_CORE, 1 MODIFY, 2 UNDECIDED, 1 MARK_AS_OVER_ANNOTATED (DNA damage IEP). No core functions. Retains 17/17 anSME features; adjacent ydeN mirrors the aslB/aslA arrangement
- [x] ygiQ (Q46861) = **rlmX**. Settled by the PMID:41380683 full text (supplied 2026-10-19): a cobalamin-dependent radical SAM methyltransferase installing hypoxia-induced 5'(S)-ribose C5' methylations at 23S rRNA D2449 and Cm2498. 8 rows: 1 ACCEPT, 3 MODIFY, 4 NEW (SAM, cobalamin, rRNA binding; rRNA methylation). Proposed new term: 23S rRNA ribose-5'-C-methyltransferase activity (no EC/RHEA; all existing GO ribose-MTase terms are 2'-O)
- [x] yhcC (P0ADW6): no longer uncharacterised. PMID:42239373 (preprint, full text) shows YhcC is the MnmL orthologue doing the anaerobic cmnm5s2U->nm5s2U demodification at tRNA position 34. 6 rows: 1 ACCEPT, 2 MODIFY, 3 NEW (tRNA binding, SAM binding, wobble uridine modification). Proposed new term for the demodifying activity

## Phase 3: consistency pass over existing reviews

Done 2026-10-28, over the 17 radical SAM reviews that existed before this
project. **43 rows re-actioned, 10 `NEW` SAM-binding rows added, 29
core-function entries added and one core molecular function withdrawn**, across
17 files. The POPTR trio was the only group already conformant on its actions;
it still gained the SAM row and the cofactor core functions, like the rest.

- [x] Write the treatment rule for the generic rows — adopted 2026-10-18 and
      applied to all 28 Phase 1 and Phase 2 reviews; the table is in the
      Overview above, under "Treatment rule for the generic rows"
- [x] Apply it to BACSU/lipA, METEA/pqqE, POPTR/LIP1, POPTR/LIP1P-1,
      POPTR/LIP1P-2, PSEPK/PP_1969, PSEPK/PP_2482, PSEPK/bioB, PSEPK/hemN,
      PSEPK/lipA, PSEPK/moaA, PSEPK/pqqE, SACEN/eryCV, SCHPO/bio2, STAWA/cfr,
      human/MOCS1 and yeast/BIO2. Both scopes now report zero deviations, and
      the check runs in CI (see the rule table above)
- [x] human/MOCS1 carried `status: INITIALIZED` although its 30 annotations were
      reviewed and it had 4 core functions. Corrected; `data_quality` is now empty
- [x] Cross-check against the relevant modules — findings below

### What the conflicts turned out to be

Every conflict listed when the rule was adopted resolved in the direction the
rule names, and almost all in the same direction: **a true row had been marked
false, or a core cofactor had been filed as peripheral.** Not one needed the rule
bent. The 43 transitions, as computed from the diff:

| Term | From | To | n | Genes |
|---|---|---|--:|---|
| `GO:0003824` | MARK_AS_OVER_ANNOTATED | MODIFY | 5 | PSEPK/bioB, PSEPK/lipA, PSEPK/pqqE, STAWA/cfr, human/MOCS1 |
| `GO:0003824` | UNDECIDED | KEEP_AS_NON_CORE | 2 | PSEPK/PP_1969, PSEPK/PP_2482 |
| `GO:0003824` | KEEP_AS_NON_CORE | MODIFY | 1 | METEA/pqqE |
| `GO:0003824` | MARK_AS_OVER_ANNOTATED | KEEP_AS_NON_CORE | 1 | SACEN/eryCV |
| `GO:0051536` | TOO_GENERAL | MODIFY | 4 | PSEPK/PP_1969, PSEPK/PP_2482, SCHPO/bio2, yeast/BIO2 |
| `GO:0051536` | ACCEPT | MODIFY | 3 | BACSU/lipA, METEA/pqqE, SACEN/eryCV |
| `GO:0051536` | KEEP_AS_NON_CORE | MODIFY | 3 | PSEPK/hemN, PSEPK/pqqE, human/MOCS1 |
| `GO:0051536` | MARK_AS_OVER_ANNOTATED | MODIFY | 3 | PSEPK/bioB, PSEPK/lipA, PSEPK/moaA |
| `GO:0046872` | KEEP_AS_NON_CORE | MODIFY | 6 | METEA/pqqE, PSEPK/PP_1969, PSEPK/PP_2482, PSEPK/hemN, PSEPK/moaA, human/MOCS1 |
| `GO:0046872` | ACCEPT | MODIFY | 1 | BACSU/lipA |
| `GO:0046872` | MARK_AS_OVER_ANNOTATED | MODIFY | 1 | PSEPK/pqqE |
| `GO:0005506` | KEEP_AS_NON_CORE | MODIFY | 2 | METEA/pqqE, PSEPK/pqqE |
| `GO:0005506` | MARK_AS_OVER_ANNOTATED | MODIFY | 1 | PSEPK/bioB |
| `GO:0051539` | KEEP_AS_NON_CORE | ACCEPT | 4 | PSEPK/hemN, PSEPK/lipA, PSEPK/moaA, STAWA/cfr |
| `GO:0051539` | ACCEPT | KEEP_AS_NON_CORE | 1 | SACEN/eryCV |
| `GO:1904047` | KEEP_AS_NON_CORE | ACCEPT | 1 | PSEPK/moaA |
| `GO:0051537` | KEEP_AS_NON_CORE | ACCEPT | 1 | PSEPK/bioB |
| `GO:0016783` | ACCEPT | MODIFY | 1 | BACSU/lipA |
| `GO:0016783` | MARK_AS_OVER_ANNOTATED | MODIFY | 1 | PSEPK/lipA |
| `GO:0016740` | ACCEPT | MODIFY | 1 | BACSU/lipA |

Reading it by pattern rather than by row:

- **12 rows had been `MARK_AS_OVER_ANNOTATED`**, which the rule forbids outright:
  none of these terms is false. Eleven become `MODIFY` to the reaction or cluster
  term the entry already carries. The twelfth is eryCV, where no reaction is
  established, so there is nothing to refine to and the row is already as precise
  as the evidence allows (`KEEP_AS_NON_CORE`).
- **4 `TOO_GENERAL` rows become `MODIFY`**, so the replacement is stated rather
  than implied. In SCHPO/bio2 and yeast/BIO2 the action was also simply wrong:
  `TOO_GENERAL` requires a more specific term asserted elsewhere in the review,
  and neither review asserted any 4Fe-4S row at all — the parent was the only
  cluster claim they made.
- **6 rows move the catalytic cofactor into core**: `GO:0051539` in PSEPK/hemN,
  PSEPK/lipA, PSEPK/moaA and STAWA/cfr, `GO:1904047` in PSEPK/moaA, and
  `GO:0051537` in PSEPK/bioB. The cluster is not a prerequisite of these
  activities, it *is* what performs the chemistry. PSEPK/bioB's auxiliary
  [2Fe-2S] cluster is the sulfur that ends up in biotin and is destroyed in the
  turnover, which ECOLI/bioB had already treated as core on direct evidence; the
  `biotin_biosynthesis` module independently lists both clusters as cofactors of
  `GO:0004076`, so that is the same judgement reached twice.
- **2 `UNDECIDED` rows on `GO:0003824` become `KEEP_AS_NON_CORE`.** The enum
  reserves `UNDECIDED` for annotations whose supporting publications could not be
  read. For PP_1969 and PP_2482 the cluster and SAM sites are intact, so
  catalysis is not what is in doubt — only its reaction, which is why there is no
  specific term to refine to.
- **3 rows on terms outside the rule table** (`GO:0016740`, `GO:0016783`) follow
  the same principle and the same precedent: human/LIAS already `MODIFY`s
  `GO:0016783` sulfurtransferase activity to `GO:0016992`.

Two changes went beyond flipping an action:

- **SACEN/eryCV asserts no core molecular function and no core process.** It had
  `GO:0051539` as its only core MF, on a protein that is `PE 4: Predicted`,
  whose sole name is an unreviewed submitter annotation, whose GOA reaction row
  (`GO:0016841`) this review leaves `UNDECIDED`, and whose cluster is inferred
  from Pfam and NCBIfam signatures rather than measured. Asserting cluster
  binding as *the* core function of such a protein overstates what is known; the
  project's other uncharacterised members (PSEPK/PP_1969, PSEPK/PP_2482, TYW1B,
  aslB, ydeM) assert none, and eryCV now matches them. Its `GO:0051539` row
  moves the other way from the four above, to `KEEP_AS_NON_CORE`. The entry's
  `directly_involved_in: GO:1901115` erythromycin biosynthetic process went with
  it, for the same reason one field up: the reviewed record has no `CC:PATHWAY`
  line and no erythromycin keyword, so the only thing placing this protein in the
  pathway is the submitter gene name `eryCV` — the annotation this review
  discounts when it declines to name a molecular function. A review cannot
  discount a source in one field and lean on it in the next.
- **10 `NEW` `GO:1904047` rows.** Phase 4's headline finding is that GOA is
  missing SAM binding for 18 of the 20 members with established catalysis; the
  pre-existing reviews were missing it too. Coded `IC`, grounded in each entry's
  own curated cofactor note ("coordinated with 3 cysteines and an exchangeable
  S-adenosyl-L-methionine") and its `4Fe-4S-S-AdoMet` binding features, not in an
  electronic GO line. The three uncharacterised members get no such row, which is
  what keeps them in the rule's second branch.

### Module cross-check

The seven named modules reference 11 of these reviews as representative members.
Where a module states a molecular function for a radical SAM step, **it agrees
with the review's core MF in every case** — including the two that matter most:

- `heme_biosynthesis/hemn_route` types HemN with `GO:0051989`
  coproporphyrinogen **dehydrogenase** activity, not the O<sub>2</sub>-dependent
  `GO:0004109`. That is the same correction this project filed against
  InterPro2GO IPR004558, reached independently by the module curator.
- `molybdenum_cofactor_biosynthesis` splits `GO:0061798` (moaA node) from
  `GO:0061799` (moaC node, different representative members), which is exactly
  the basis on which ECOLI/moaA and PSEPK/moaA `REMOVE` the cPMP-synthase row.
- `thiamine_diphosphate_biosynthesis` puts `GO:1990107` thiazole synthase on
  ThiG and `GO:0036355` on ThiH, matching ECOLI/thiH's decision to leave thiazole
  synthase to ThiG.
- `biotin_biosynthesis/bioB_activity` (`GO:0004076`) and
  `endogenous_protein_lipoylation` (three `GO:0016992` nodes) agree with all six
  biotin- and lipoyl-synthase reviews.

Four **module** gaps follow, recorded here rather than as `knowledge_gaps`,
because a curator closes them by annotating, not by experiment:

1. **ECOLI/queE is in no module.** `bacterial_preq1_incorporation_queuosine_maturation`
   has no QueE annoton, although QueE performs the radical SAM ring
   contraction that makes CDG. queE's core MF is a `proposed_new_terms` entry
   (7-carboxy-7-deazaguanine synthase activity), so the module node would need
   `proposed_molecular_function`.
2. **Cofactors are recorded unevenly.** The bioB, moaA, hemN and thiH annotons
   list their Fe-S clusters; the three lipoylation nodes and the
   `pqqe_peptide_cyclase` node list none, although UniProt records 2× [4Fe-4S]
   for the lipoyl synthases and [4Fe-4S] for both METEA/pqqE and PSEPK/pqqE.
   Phase 3 has just made `GO:0051539` a core function in every one of those
   reviews, so the asymmetry is now visible from the gene side too.
3. **`moaA_gtp_38_cyclase` has no family descriptor**, while its sibling moaC
   annoton has `PANTHER:PTHR22960:SF29`. Per the repository rule, omitting the
   id is the right call when the family is not established — but MoaA's is
   (PTHR22960 is the MoaA/MoaC-containing family), so this looks like an
   omission rather than a judgement.
4. **Reviewed orthologues are missing from representative-member lists.**
   human/MOCS1 is absent from both molybdopterin annotons although it is the
   human MoaA–MoaC fusion; METEA/pqqE is absent from the
   `pqqe_peptide_cyclase` annoton although it is reviewed and better
   characterised than PSEPK/pqqE; the three POPTR
   lipoyl synthases are absent from the lipoylation module, which has bacterial,
   *Bacillus* and human variants but no plant one.

HemW and RSAD1 are correctly absent from `heme_biosynthesis`: they are heme
chaperones, not enzymes of the pathway, which is the whole point of this
project's HemN/HemW finding.

## Phase 4: synthesis

- [x] Superfamily-level summary: reaction classes, which have GO MF terms, which
      need `proposed_new_terms` — see [Synthesis](#synthesis) below
- [x] Notes on IBA/PAINT node placement for the paralog-rich subfamilies — see
      [What the IBAs got right, and where they reach too deep](#what-the-ibas-got-right-and-where-they-reach-too-deep)

Every figure below is computed from the reviews by
[`rsam_synthesis.py`](RADICAL_SAM/rsam_synthesis.py), which takes its gene list
from this page's own frontmatter and writes
[`data/synthesis.yaml`](RADICAL_SAM/data/synthesis.yaml). No *result* is
hardcoded; the project's own editorial choices are (the treatment rule itself,
and which asserted values count as PflB-substrate pushes). Classifications are
keyed on evidence codes rather than on lists of term ids wherever possible. Editing any of the 29
reviews changes these figures, so re-run the script and commit the regenerated
data in the same change — `tests/test_radical_sam_synthesis.py` fails until you
do, and also checks that the totals quoted here actually partition.

# Synthesis

## What was covered

29 proteins in scope, **28 reviewed** across **500 annotation rows**. A gene
counts as reviewed here when it has rows and none is still `PENDING`, which
deliberately ignores `status:`, which can go stale: MOCS1 was fully reviewed
while still carrying `status: INITIALIZED`, and the script reported that
separately under `data_quality` rather than letting it skew the arithmetic
(Phase 3 has since corrected it, and `data_quality` is now empty). lipA is the
one genuine gap, and its 18 `PENDING` rows are excluded throughout. Actions
across the 500:

| Action | n |
|---|---:|
| ACCEPT | 210 |
| MODIFY | 115 |
| KEEP_AS_NON_CORE | 65 |
| REMOVE | 49 |
| NEW | 28 |
| MARK_AS_OVER_ANNOTATED | 20 |
| UNDECIDED | 10 |
| TOO_GENERAL | 3 |

`MODIFY` at 115 is the signature of this family: a quarter of all rows were true
but pitched at the wrong level, which is exactly what a shared catalytic domain
with unshared chemistry produces.

## The resolution gap: 6 core activities have no GO term

25 of the 28 reviewed genes assert at least one core function. Of those, **6 name
an activity GO cannot express** and carry a `proposed_new_terms` entry instead:

| Gene | Activity with no GO term | Why GO has none |
|---|---|---|
| RSAD2 | SAM-dependent CTP dehydratase (ddhCTP) | reaction described in 2018; no EC, no term |
| queE | 7-carboxy-7-deazaguanine synthase | EC 4.3.99.3 and RHEA:27974 exist, term does not |
| epmB | L-lysine 2,3-aminomutase, (R)-β-lysine-forming | GO:0050066 is defined as the (3S) clostridial product |
| hemW | heme chaperone activity | `GO:0016530` covers metal *ions*; no heme-carrier term |
| ygiQ | 23S rRNA ribose-5'-C-methyltransferase | every GO ribose-MTase term is 2'-O |
| yhcC | tRNA cmnm5s2U(34) demodifying activity | no SAM-dependent RHEA for the demodification |

A seventh proposal is additive rather than a gap-filler: nrdG keeps the existing
`GO:0043364` and proposes a substrate-specific child for the anaerobic-RNR
activase, which would give the uncharacterised activases an obvious pattern.

Two things are worth separating here. `queE` and `epmB` are **ontology lag** —
the chemistry is settled and even has an EC or RHEA identifier, so the term is a
request, not research. `RSAD2`, `ygiQ` and `yhcC` are **recent discoveries**
(2018, 2026, 2026), where GO has not had time. Only `hemW` is a genuine modelling
question: GO has no vocabulary for a protein that carries a cofactor to an
apo-enzyme without chemistry.

The remaining breakdown: **19 genes' core functions use existing GO terms**, one
of which (RSAD1) is `GO:0020037` heme binding with no reaction established; and
TYW1B, aslB and ydeM assert **no core function at all**, deliberately.

## The scaffold is universal; GOA records half of it

`GO:0051539` (4Fe-4S binding) and `GO:1904047` (SAM binding) are each core in **20**
of the reviewed genes — the superfamily's defining pair. But `GO:1904047` appears
as a `NEW` row, meaning absent from GOA, in **18** of those, against only **2**
(moaA and queE) where GOA already carried it.

That is a systematic, machine-fixable gap, not 18 independent oversights. The
curated PROSITE/HAMAP cofactor note on these records already says SAM is an
exchangeable ligand of the cluster, so the assertion is sitting in UniProt
unexploited. It is the single highest-leverage item this project found and is
worth raising with GO/UniProt as a rule rather than gene by gene.

The **eight** reviewed genes that did not get it — RSAD1, TYW1B, aslB, hemW, pflC,
ybiY, ydeM and yjjW — are exactly the set whose catalysis the reviews did not
establish. That partition was read off the reviews one gene at a time, not asserted:
each of the eight was independently judged to lack a demonstrated reaction, and the
script simply reports the result. lipA is **excluded, not unestablished** — it is
lipoyl synthase (EC 2.8.1.8), the same enzyme as human LIAS, and lacks a row only
because it is unreviewed; it is reported under `not_reviewed_so_not_classified`.

## The treatment rule held

Across the 28 reviewed genes (lipA's `PENDING` rows excluded), the
domain-derived generic rows came out as:

| Term | MODIFY | ACCEPT | KEEP_AS_NON_CORE | other |
|---|---:|---:|---:|---|
| `GO:0003824` catalytic activity | 22 | – | 5 | 1 |
| `GO:0051536` iron-sulfur cluster binding | 28 | – | 1 | – |
| `GO:0051539` 4Fe-4S binding | – | 31 | 12 | – |
| `GO:0046872` metal ion binding | 1 | – | 1 | – |
| `GO:0005506` iron ion binding | 3 | – | – | – |
| `GO:1904047` SAM binding | – | 2 | – | 18 NEW |

The 5 `KEEP_AS_NON_CORE` on `GO:0003824` and the 12 on `GO:0051539` are the rule's
own "catalysis not established" branch (RSAD1, TYW1B, hemW, aslB, ydeM and the
activase paralogs), not departures from it.

The script encodes the rule and emits `treatment_rule_deviations`, so this is
checked rather than asserted. It currently reports **exactly three, all MOCS1's**
— `GO:0003824 MARK_AS_OVER_ANNOTATED`, `GO:0046872` and `GO:0051536`
`KEEP_AS_NON_CORE` — in the pre-existing review that predates the rule. The other
17 non-primary actions are recorded separately as `treatment_rule_branch_uses`.
That makes the Phase 3 worklist measurable: re-running the script after Phase 3
should drive the deviation count to zero.

## What the IBAs got right, and where they reach too deep

18 IBA rows carry a `propagation_review`. Sorted by what the review concluded:

- **4 are propagation failures** (`PROPAGATION_BAD`). Two are the same node:
  `PANTHER:PTN000358281` places porphyrin biosynthesis deep enough to reach both
  *E. coli* hemW and human RSAD1, although the HemW subfamily was shown
  experimentally to lack that chemistry. moaA's is `ROLE_CONFLATION` — MoaC's
  cPMP-synthase activity transferred from the MOCS1 fusion proteins, which have a
  MoaC domain that *E. coli* MoaA does not. CDK5RAP1's is a compartment mismatch.
- **9 are scoping problems** (`TERM_SCOPING_PROBLEM`), mostly
  `GRANULARITY_MISMATCH`: the node is placed correctly and the term is simply
  more general than the gene warrants. These became `MODIFY`, not `REMOVE`.
- **4 are no failure at all**, recorded to show the node was checked and holds.
- **1 is unresolved** (TYW1B), where the sequence argues against the inherited
  activity but nothing has been tested.

The generalisable lesson is the HemN/HemW case, and it is a precise one: **when a
subfamily loses an activity, the molecular function is usually re-placed correctly
and the biological process is not.** PAINT put coproporphyrinogen dehydrogenase on
the HemN-only node `PTN000358335`, but left porphyrin biosynthesis on the parent
`PTN000358281` that both subfamilies descend from. So the MF stops at HemN while
the BP leaks onto HemW. Checking whether a family's MF and BP sit on the *same*
node is a cheap, mechanical test that would have caught this, and it generalises
to any subfamily that has lost its ancestral chemistry.

The paralog-rich subfamilies otherwise behaved differently from each other, and
not as expected:

- **PFL activases** — the IBAs were sound. The damage came from UniProt RHEA/EC
  assignments and an InterPro2GO mapping pushing PflB-specific substrate terms
  onto proteins whose partner is not PflB — **5 of the 10 source defects**, on
  pflC, ybiY and nrdG.
- **MTTases** — the IBAs were sound at family level; the one failure was a
  compartment claim on CDK5RAP1 from a splice variant lacking its targeting
  sequence.
- **HemN/HemW** — the only subfamily where node *placement* itself was wrong.

## Upstream, not ours: 10 source defects

The reviews recorded 10 defects — 5 against UniProt (RHEA and EC assignments on
pflC/ybiY, and a query on an *L. lactis* donor), 4 against InterPro2GO mappings
and 1 against an EcoliWiki GOA row. The InterPro defects sit on just **three
distinct entries** (IPR004559 carries two wrong mappings), and each propagates to
every member of its signature, so correcting three entries fixes far more genes
than the 29 here. `SourceResourceEnum` has no `INTERPRO` value, so those four are
filed as `resource: OTHER` with InterPro named in each explanation.

`just export-source-defects` turns them into per-resource reports.

## What this says about the superfamily

Three claims the data supports, and one it does not.

1. **The family's annotation problem is resolution, not error.** 210 ACCEPT
   against 49 REMOVE — and only **3 of those 49** overturned a claim anyone had
   actually asserted about the gene. The rest were uninformative `protein
   binding` (**34**) or terms that had propagated in rather than been asserted
   (**12**: 8 `IEA` signature/EC mappings, 3 `IBA`, 1 `ISS`). The 3 are nrdG's
   `IMP` ribonucleoside-diphosphate reductase row, removed because the activase
   is necessary for the reaction without performing it, and two `NAS` rows on
   CDK5RAP1 projecting CDK5 neuronal biology onto a mitochondrial tRNA enzyme.
   The split is computed from each row's **evidence code** — how the row arose,
   not which term it carries (`remove_breakdown`).
2. **The shared domain is an attractor for over-general annotation.** 115 MODIFY,
   almost all pulling a correct-but-generic term down to the specific reaction.
3. **Discovery is outrunning the ontology.** Three of the six missing terms are
   for reactions described in 2018 or later, two of them in 2026.
4. **What the data does *not* support** is the intuition that IBA is the main
   culprit for paralog over-annotation in this family. Only 4 of 18 reviewed IBAs
   were propagation failures, while signature-based IEA mappings produced more
   wrong claims and reached further. PAINT curators had generally made the harder
   judgement correctly.

# NOTES

## 2026-10-19

- Phase 2 started. Fetched all 20 E. coli K-12 genes (`just fetch-gene ECOLI
  <gene>`, standard lower-case-first symbols); every accession matches the
  UniProt scope query.
- Deep research: falcon still 403; perplexity not configured; asta was empty
  for all of Phase 1, so not re-run. openscientist is being tried on ygiQ
  (slow, >10 min). Reviews proceed from primary literature, as in Phase 1.
- 8 reviewers by subfamily: bioB + lipA (sulfur insertion); moaA + queE + thiH
  (cofactor rearrangements); nrdG + pflA (characterised glycyl-radical
  activases, which set the pattern); pflC + ybiY + yjjW (activase paralogs);
  miaB + rimO (MTTases, matched to CDKAL1/CDK5RAP1); rlmN + epmB; hemN + hemW
  (matched to RSAD1); aslB + ydeM + ygiQ + yhcC (uncharacterised).
- **lipA left unreviewed.** The bioB + lipA reviewer completed bioB, wrote
  `lipA-notes.md`, and was then interrupted by a safety classifier partway
  through writing the lipA review file, with an instruction not to reproduce
  that content. It stopped rather than retrying. The lipA review file is
  therefore still the untouched stub. The block looks like a false positive:
  bioB (nearly identical chemistry) and human LIAS (the same enzyme) both
  completed in the same session, and lipA reviews already exist for PSEPK and
  BACSU. A second, unrelated classifier interruption occurred later in the same
  session while summarising the aslB/ydeM/ygiQ/yhcC results in chat, so the
  trigger does not appear to be lipA's subject matter. The task was not handed
  to another reviewer, because reissuing blocked content through a different
  agent would route around the decision rather than resolve it. lipA is left
  for a separate session.

## 2026-10-18

- Created the project. Membership pulled live from UniProt (IPR007197, reviewed):
  9 human and 20 *E. coli* K-12 entries. None of the *E. coli* entries has a
  review yet; MOCS1 is the only human one.
- Found 17 existing radical SAM reviews (mostly PSEPK) and tabulated their
  actions on the generic domain-derived rows; see "Starting observation". This
  is the motivating finding for Phase 3.
- InterPro2GO for IPR007197 and IPR006638: `GO:0003824` + `GO:0051536`. For
  IPR005839 (MTTase) and IPR006463 (MiaB): `GO:0016740`, `GO:0051539`,
  `GO:0006400`.
- Fetched all 8 Phase 1 human genes (`just fetch-gene`).
- **Falcon deep research is unavailable**: the Edison API returns 403 at
  `/auth/login` (host reachable, key rejected). Ran `just deep-research-asta`
  for all 8 instead. Asta is literature retrieval, not a synthesis, so reviewers
  lean more on the cached papers and UniProt. Re-run falcon once the key is
  fixed.
- Adopted the treatment rule for the generic rows (see Overview) before the
  Phase 1 reviews so they are consistent from the start.
- Phase 1 reviews dispatched: LIAS, RSAD2, ELP3, RSAD1, TYW1 + TYW1B (one
  reviewer, paralogs), CDKAL1 + CDK5RAP1 (one reviewer, MTTase paralogs).
- **Phase 1 complete** (all 8 validate with 0 errors). Cross-cutting findings:
  - The asta files contained nothing on any of the 8 genes (all 20 retrieved
    papers per gene were generic database/methods papers). Every review was
    built from cached primary literature, PubMed and UniProt. Each review
    carries the harmless "deep research not cited" warning for this reason.
  - The generic-row rule applied cleanly everywhere; no gene needed an
    exception. `GO:0046872` did not occur in any human GOA set.
  - `GO:1904047` S-adenosyl-L-methionine binding is absent from GOA for every
    human radical SAM enzyme. Added as NEW to the 7 with established catalysis
    (LIAS, RSAD2, ELP3, CDKAL1, CDK5RAP1, TYW1; MOCS1 already had it as core
    function). Not added to RSAD1 or TYW1B. Worth raising with GO/UniProt as a
    systematic gap: the curated PROSITE/HAMAP cofactor note ("exchangeable
    S-adenosyl-L-methionine") could drive it.
  - Homology over-annotation found in both uncharacterised members: RSAD1
    carried HemN coproporphyrinogen-oxidase and porphyrin-biosynthesis rows
    (removed; the HemW subfamily lacks that activity, PMID:22142238); TYW1B
    carries TYW1 activity by ECO:0000250 transfer although it lacks the FMN
    loop and auxiliary-cluster cysteines (left UNDECIDED, alignment in
    `genes/human/TYW1B/TYW1B-bioinformatics/`).
  - Ontology gap: no GO MF term for viperin's ddhCTP synthase reaction
    (checked QuickGO/OLS 2026-10-18); proposed in the RSAD2 review.
- Next: Phase 2 (E. coli K-12), starting with bioB, lipA, moaA.
- 2026-10-19: ygiQ re-reviewed as rlmX once the user supplied the Mol Cell PDF;
  full text now cached in publications/PMID_41380683.md. The openscientist
  report's central claim (ygiQ = rlmX) was right, but its two-[4Fe-4S]-cluster
  model is contradicted (3.69 Fe/protein = one cluster; the C453/C458/C464
  surface triad is a putative zinc/RNA-recognition site). Nothing was annotated
  from the machine report; the file is marked LOW_QUALITY.
