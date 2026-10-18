---
title: "Radical SAM Enzymes: GO annotation across the superfamily"
maturity: SCOPING
tags: [PIPELINE]
species: [human, ECOLI]
genes: [LIAS, RSAD2, MOCS1, CDKAL1, CDK5RAP1, ELP3, TYW1, TYW1B, RSAD1, bioB, lipA, moaA, nrdG, pflA, rlmN, miaB, rimO, thiH, hemN, hemW, queE, epmB, pflC, ybiY, yjjW, aslB, ydeM, ygiQ, yhcC]
---

# Radical SAM Enzymes

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

The 17 radical SAM reviews already in the repository (matched by IPR007197,
PS51918 or IPR058240 in their UniProt records) treat the same domain-derived
terms in contradictory ways:

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
core function (it is the catalytic cofactor) or is non-core is the main
judgement call to fix in Phase 3.

### Treatment rule for the generic rows

Adopted 2026-10-18 for all new reviews in this project, and to be applied in
the Phase 3 pass. Hierarchy checked in QuickGO: `GO:0051539` is_a `GO:0051536`
is_a `GO:0051540` metal cluster binding; `GO:0046872` metal ion binding is
**not** an ancestor of either.

| Term | Action | Replacement / note |
|---|---|---|
| `GO:0003824` catalytic activity | `MODIFY` | The specific reaction MF the gene carries or is shown to have. If no reaction is known (e.g. RSAD1), `KEEP_AS_NON_CORE`: it is already as precise as the evidence allows. |
| `GO:0051536` iron-sulfur cluster binding | `MODIFY` | `GO:0051539`, the descendant the radical SAM cluster always satisfies. |
| `GO:0051539` 4 iron, 4 sulfur cluster binding | `ACCEPT` | The radical SAM cluster is the catalytic cofactor, so it is core for every active member. `KEEP_AS_NON_CORE` only where catalysis is not established. |
| `GO:0046872` metal ion binding | `MODIFY` | `GO:0051539` (lateral correction: the iron is bound as a cluster). Keep only if the protein binds a separate metal ion. |
| `GO:1904047` S-adenosyl-L-methionine binding | `ACCEPT` | Cosubstrate binding, true for every active member. |

Never `MARK_AS_OVER_ANNOTATED` for these rows: none of them is false.

---
# STATUS

Last updated: 2026-10-18

## Phase 1: human (9)

- [x] LIAS (O43766): lipoyl synthase, mitochondrial. 21 rows: 11 ACCEPT, 6 MODIFY (incl. 3 obsolete GO:0009107 → GO:0009249), 3 MARK_AS_OVER_ANNOTATED (mouse phenotype ISS), 1 NEW (SAM binding)
- [ ] RSAD2 (Q8WXG1): viperin, CTP → ddhCTP dehydratase
- [x] MOCS1 (Q9NZB8): GTP 3',8-cyclase (MOCS1A) + cPMP synthase (MOCS1B). Reviewed earlier; include in Phase 3
- [ ] CDKAL1 (Q5VV42): cytosolic tRNA t6A37 → ms2t6A methylthiotransferase
- [ ] CDK5RAP1 (Q96SZ6): mitochondrial tRNA i6A37 → ms2i6A methylthiotransferase
- [x] ELP3 (Q9H9T3): Elongator catalytic subunit, tRNA U34 acetyltransferase. 42 rows: 12 ACCEPT, 12 MODIFY, 11 KEEP_AS_NON_CORE, 3 MARK_AS_OVER_ANNOTATED (Pol II transcription, cell migration), 4 REMOVE (protein binding), 1 UNDECIDED (nucleolus), 1 NEW (SAM binding)
- [ ] TYW1 (Q9NV66): tRNA 4-demethylwyosine synthase
- [ ] TYW1B (Q6NUM6): TYW1 paralog. Check whether activity is demonstrated or inferred
- [x] RSAD1 (Q9HA92): HemW homolog; heme binding (IDA) is the only supported function. 12 rows: 3 ACCEPT, 3 KEEP_AS_NON_CORE, 3 MODIFY, 3 REMOVE (coproporphyrinogen oxidase + porphyrin biosynthesis, transferred from HemN; HemW subfamily lacks that activity)

## Phase 2: *E. coli* K-12 (20)

Characterised, in priority order:

- [ ] bioB (P12996): biotin synthase
- [ ] lipA (P60716): lipoyl synthase
- [ ] moaA (P30745): GTP 3',8-cyclase
- [ ] nrdG (P0A9N8): anaerobic RNR (class III) activase
- [ ] pflA (P0A9N4): pyruvate formate-lyase activase
- [ ] rlmN (P36979): 23S rRNA m2A2503 / tRNA m2A37 methyltransferase
- [ ] miaB (P0AEI1): tRNA ms2i6A37 methylthiotransferase
- [ ] rimO (P0AEI4): ribosomal protein uS12 Asp89 methylthiotransferase
- [ ] thiH (P30140): 2-iminoacetate synthase (tyrosine lyase)
- [ ] hemN (P32131): oxygen-independent coproporphyrinogen III oxidase
- [ ] hemW (P52062): heme chaperone. Check for over-annotation from HemN
- [ ] queE (P64554): 7-carboxy-7-deazaguanine synthase
- [ ] epmB (P39280): L-lysine 2,3-aminomutase (EF-P modification)

Paralogs and uncharacterised, where the risk is over-annotation:

- [ ] pflC (P32675): PFL-activating enzyme 2
- [ ] ybiY (P75794): putative PFL-activating enzyme 3
- [ ] yjjW (P39409): putative glycyl-radical enzyme activase
- [ ] aslB (P25550): anaerobic sulfatase-maturating enzyme homolog
- [ ] ydeM (P76134): anaerobic sulfatase-maturating enzyme homolog
- [ ] ygiQ (Q46861): UPF0313
- [ ] yhcC (P0ADW6): uncharacterised

## Phase 3: consistency pass over existing reviews

- [ ] Write the treatment rule for the generic rows (see "Starting observation")
- [ ] Apply to: BACSU/lipA, METEA/pqqE, POPTR/LIP1, POPTR/LIP1P-1, POPTR/LIP1P-2,
      PSEPK/PP_1969, PSEPK/PP_2482, PSEPK/bioB, PSEPK/hemN, PSEPK/lipA,
      PSEPK/moaA, PSEPK/pqqE, SACEN/eryCV, SCHPO/bio2, STAWA/cfr, human/MOCS1,
      yeast/BIO2
- [ ] Cross-check against the relevant modules (biotin_biosynthesis,
      endogenous_protein_lipoylation, molybdenum_cofactor_biosynthesis,
      heme_biosynthesis, pqq_biosynthesis, bacterial_preq1_incorporation_queuosine_maturation,
      thiamine_diphosphate_biosynthesis)

## Phase 4: synthesis

- [ ] Superfamily-level summary: reaction classes, which have GO MF terms, which
      need `proposed_new_terms`
- [ ] Notes on IBA/PAINT node placement for the paralog-rich subfamilies
      (PFL activases, MTTases, HemN/HemW)

# NOTES

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
