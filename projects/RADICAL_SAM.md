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
- [x] RSAD2 (Q8WXG1): viperin, CTP → ddhCTP dehydratase. 59 rows: 26 ACCEPT, 17 KEEP_AS_NON_CORE (infection-driven mitochondrial/Golgi pools, mouse T-cell rows), 8 REMOVE (protein binding), 3 TOO_GENERAL, 2 MODIFY, 1 MARK_AS_OVER_ANNOTATED, 2 NEW (SAM binding; protein-macromolecule adaptor for IRAK1–TRAF6). Proposed new term: SAM-dependent CTP dehydratase activity (RHEA:65944)
- [x] MOCS1 (Q9NZB8): GTP 3',8-cyclase (MOCS1A) + cPMP synthase (MOCS1B). Reviewed earlier; include in Phase 3
- [x] CDKAL1 (Q5VV42): cytosolic tRNA t6A37 → ms2t6A methylthiotransferase. 23 rows: 8 ACCEPT, 9 MODIFY, 2 KEEP_AS_NON_CORE, 3 REMOVE (protein binding), 1 NEW (SAM binding). No insulin-secretion terms: upstream necessity, not participation
- [x] CDK5RAP1 (Q96SZ6): mitochondrial tRNA i6A37 → ms2i6A methylthiotransferase. 28 rows: 12 ACCEPT, 6 MODIFY, 4 MARK_AS_OVER_ANNOTATED (nuclear/cytosolic pool, refuted by PMID:28981754), 2 KEEP_AS_NON_CORE, 2 REMOVE (NAS brain development/neuron differentiation), 1 UNDECIDED, 1 NEW (SAM binding)
- [x] ELP3 (Q9H9T3): Elongator catalytic subunit, tRNA U34 acetyltransferase. 42 rows: 12 ACCEPT, 12 MODIFY, 11 KEEP_AS_NON_CORE, 3 MARK_AS_OVER_ANNOTATED (Pol II transcription, cell migration), 4 REMOVE (protein binding), 1 UNDECIDED (nucleolus), 1 NEW (SAM binding)
- [x] TYW1 (Q9NV66): tRNA 4-demethylwyosine synthase. 8 rows: 4 ACCEPT, 3 MODIFY, 2 NEW (cytoplasm IDA PMID:38706838; SAM binding). TYW1-knockout hESCs lack OHyW, so human evidence backs the yeast inference
- [x] TYW1B (Q6NUM6): TYW1 paralog. Activity only inferred; alignment (TYW1B-bioinformatics/) shows TYW1B lacks the FMN phosphate loop and 2 of 3 auxiliary-cluster cysteines. 8 rows: 4 UNDECIDED, 2 KEEP_AS_NON_CORE, 1 MODIFY, 1 REMOVE (protein binding); no core functions asserted
- [x] RSAD1 (Q9HA92): HemW homolog; heme binding (IDA) is the only supported function. 12 rows: 3 ACCEPT, 3 KEEP_AS_NON_CORE, 3 MODIFY, 3 REMOVE (coproporphyrinogen oxidase + porphyrin biosynthesis, transferred from HemN; HemW subfamily lacks that activity)

## Phase 2: *E. coli* K-12 (20)

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
