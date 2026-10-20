# CDC16 (P09798, YKL022C) — curation notes

Working notes for the GO annotation review of *Saccharomyces cerevisiae* CDC16 /
Apc6. Inputs: `CDC16-uniprot.txt`, `CDC16-goa.tsv`, `CDC16-deep-research-falcon.md`
(Edison/falcon deep research, present), cached publications, and the finished
human CDC27 and yeast CDC20/CDH1/PDS1 reviews as comparators.

## Identity

- Essential TPR subunit of the APC/C; orthologue of human ANAPC6/CDC16 and *S. pombe*
  Cut9. Not to be confused with *S. pombe* cdc16 (septation-initiation network GAP),
  a completely unrelated protein
  [file:yeast/CDC16/CDC16-deep-research-falcon.md "It is important not to confuse
  this protein with the unrelated *Schizosaccharomyces pombe* gene named **cdc16**"].
- 840 aa, 14 TPR repeats (UniProt FT REPEAT 229..737), disordered N-terminus
  carrying the Cdc28 sites (S44, S59, S95, S103, T115, T406; PMID:10871279, not
  cached). PANTHER PTHR12558 "CELL DIVISION CYCLE 16,23,27", subfamily SF9.

## Holistic picture

1. **Structural subunit, no catalysis.** Cdc16 is one of the three TPR subunits
   (Cdc27, Cdc16, Cdc23) that with Apc4/Apc5 and Apc1 form the TPR lobe / "arc
   lamp"; catalysis is in Apc2 (cullin) + Apc11 (RING).
   [PMID:16481473 "the three TPR subunits display a sequential binding dependency,
   with Cdc27 the most peripheral, Cdc23 the most internal, and Cdc16 between"]
   [PMID:21186364 "the arc lamp domain consists of the TPR proteins Cdc16, Cdc23,
   Cdc27 and, in case of the vertebrate APC/C, presumably also Apc7"]
   [file:yeast/CDC16/CDC16-deep-research-falcon.md "Cdc16 is **not an enzyme by
   itself** and has no known substrate-specific catalytic reaction."]
2. **Assembly dependencies.** cdc16Δ APC/C loses Cdc16 and Cdc27 (and Cdc26); the
   TPR subcomplex is stable without Apc1; Swm1/Apc13 and Cdc26 stabilise the
   Cdc16/Cdc27 pair.
   [PMID:16481473 "cdc16 Δ strains lacked both Cdc16 and Cdc27"]
   [PMID:16481473 "Our data suggest that Cdc26 associates directly with Cdc16"]
   [PMID:15060174 "Our data suggest that Cdc16, Cdc27, Apc9, Swm1/Apc13, and Cdc26
   form a stable subcomplex whose association with the APC/C requires Cdc23."]
3. **Required for coactivator binding and for any activity.**
   [PMID:16481473 "Complexes from cdc16 Δ and cdc23 Δ strains also showed no Cdh1
   interaction."]
   [PMID:16481473 "cdc16 Δ APC lacks any measurable activity"]
   [PMID:16481473 "Our data suggest that the essential role of Cdc16 in APC function
   is not in binding the IR of Cdh1, since IR mutants retain activity, whereas APC
   from cdc16 Δ strains do not."]
4. **Direct contact with Doc1/Apc10** (the substrate co-receptor with the
   coactivator) — photo-crosslinking from Doc1 S128/K129/R182 to Cdc16; Doc1 IR
   tail (F244) goes to Cdc27.
   [PMID:21186364 "In crosslinking experiments we identified Cdc27, Cdc16 and Apc1
   as binding partners of Doc1."]
   [PMID:21186364 "Our results suggest that substrates are recruited to the APC/C by
   binding to a bipartite substrate receptor composed of a coactivator protein and
   Doc1."]
5. **Founding APC/C biochemistry.** Cdc16p/Cdc23p/Cdc27p complex required for
   anaphase and cyclin proteolysis; APC/C composition by MS.
   [PMID:8895471 "containing the tetratricopeptide repeat proteins Cdc16p, Cdc23p,
   and Cdc27p."]
   [PMID:9469814 "including the previously identified proteins Apc1p, Cdc16p,
   Cdc23p, Cdc26p, and"]
   [PMID:12477395 "total number of identified APC subunits to 13 in both yeasts"]
6. **Phospho-regulation.** Cdc28 phosphorylates Cdc16/Cdc23/Cdc27; the combined
   phospho-site mutant loses Cdc20-dependent but not Cdh1-dependent activity
   (Rudner & Murray 2000, PMID:10871279 not cached; captured via UniProt and the
   deep research).
   [file:yeast/CDC16/CDC16-uniprot.txt "Phosphorylated by CDC28, which is required
   for the early mitotic"]
   [file:yeast/CDC16/CDC16-deep-research-falcon.md "Simultaneous substitution of
   candidate Cdk1 sites across these three TPR subunits makes APC/C resistant to
   normal phosphorylation and compromises its mitotic Cdc20-dependent activity"]
7. **Meiosis.** Cdc16-myc co-IPs Ama1-HA; cdc16-1 diploids arrest before meiosis I;
   Pds1 stabilised in meiotic cdc16 cells.
   [PMID:11114178 "Ama1p-HA was detected in the Cdc16-myc immunoprecipitates,
   indicating that these two proteins interact in vivo"]
   [PMID:11114178 "Pds1p was stabilized in the cdc16 mutant, indicating that, similar
   to vegetative cells, the APC/C is required for Pds1p destruction during meiosis."]
8. **Localisation.** Nuclear (Huh 2003 via UniProt; GFP screen of Dastidar 2012),
   cytosolic under hypoxia.
   [PMID:22932476 "YKL022CCDC16Subunit of the anaphase-promoting complex/cyclosome"
   — Table 1, "Nuclear proteins that relocalized to the cytosol in response to
   hypoxia in a shorter time period"]
9. **Re-replication claim.** cdc16-ts arrests re-fire origins per Heichman &
   Roberts; contested by Pichler et al. 1997; no mechanism.
   [PMID:9660930 "that CDC16 is required to prevent inappropriate firing of
   replication origins."]
   [PMID:9660930 "in cdc16 mutants is largely chromosomal, as we originally
   reported."]

## Annotation decisions (36 rows)

| Term | Evidence / ref | Action | Note |
|---|---|---|---|
| GO:0005515 protein binding (Doc1) | IPI PMID:21186364 | MODIFY → GO:0160072 | Direct crosslink to Doc1; Cdc16 scaffolds the substrate-receptor module onto the ligase (same replacement as human CDC27). |
| GO:0005515 protein binding (Doc1) | IPI PMID:16429126, 21107322, 23267104, 37968396, 9469814 | REMOVE | Uninformative; complex membership already annotated. PMID:23267104 is an *S. pneumoniae* interactome paper with no yeast content in the cache — flagged in `reference_review`. PMID:21107322 full text never names Cdc16. |
| GO:0005515 protein binding (Tyc1) | IPI PMID:29883473 | REMOVE | Cdc16-TAP was only the purification handle; Tyc1 binds the holo-APC/C. |
| GO:0005634 nucleus | IDA PMID:22932476; IEA | ACCEPT | Site of function (closed mitosis). |
| GO:0005829 cytosol | IDA PMID:22932476 | KEEP_AS_NON_CORE | Hypoxia-induced relocalisation. |
| GO:0005737 cytoplasm | IBA PTN000285227 | KEEP_AS_NON_CORE | Node seeded by human ANAPC6 (open mitosis); real but not the yeast site of function. |
| GO:0005680 APC/C | IBA, IDA, IEA, IPI, NAS ×2 | ACCEPT | Core identity. |
| GO:0007346 regulation of mitotic cell cycle | NAS PMID:16481473 | MODIFY → GO:0007091 | Too general; the step is the metaphase/anaphase transition (+ mitotic exit). |
| GO:0016567 protein ubiquitination | IBA, IDA, IEA, IMP, NAS ×2 | ACCEPT | Structural subunit without which the E3 has no activity. |
| GO:0031145 APC/C-dependent catabolic process | IBA, IDA ×2, IMP, NAS ×2 | ACCEPT | Core process. |
| GO:0032297 neg. reg. of DNA replication initiation | IMP PMID:9660930 | MARK_AS_OVER_ANNOTATED | Necessity-only, contested, mechanism unknown; likely indirect consequence of APC/C loss. Reference marked DISPUTED. |
| GO:0045842 pos. reg. of mitotic M/A transition | IBA PTN000285227 | ACCEPT | Yeast evidence agrees (Pds1 stabilisation). |
| GO:0051301 cell division | IBA PTN001757014 | ACCEPT | Broad but correct. |
| GO:0051445 regulation of meiotic cell cycle | NAS PMID:11114178 | KEEP_AS_NON_CORE | Genuine (APC/C-Ama1), specialised deployment. |
| GO:0061630 ubiquitin protein ligase activity | IMP PMID:16481473 (contributes_to) | ACCEPT | cdc16Δ APC/C inactive; qualifier is exactly right. |
| GO:0140767 enzyme-substrate adaptor activity | IBA PTN002649387 (ANAPC7 seed) | MODIFY → GO:0160072 | Cdc16 binds Doc1 and the TPR neighbours, not degrons; scaffold term, as for human CDC27. |

Totals: ACCEPT 23, REMOVE 6, MODIFY 3, KEEP_AS_NON_CORE 3, MARK_AS_OVER_ANNOTATED 1.

## Core functions written

1. Ubiquitin ligase complex scaffold activity (GO:0160072) in the APC/C, contributing
   to ubiquitin protein ligase activity; directly involved in APC/C-dependent
   catabolic process, metaphase/anaphase transition of the mitotic cell cycle and
   protein ubiquitination; nucleus.
2. Cdc28-phosphorylated TPR platform for APC/C-Cdc20 activation (contributes_to
   GO:0061630; GO:0007091). No dedicated MF term exists.

## Open points / not done

- `proposed_new_terms: []` — no new term proposed. A NEW annotation for
  GO:0007091 was considered but is covered by the MODIFY on the ComplexPortal
  NAS row and by the IBA GO:0045842.
- PMID:7925276 (Lamb 1994), PMID:10871279 (Rudner & Murray 2000), PMID:12928868
  and PMID:2404612 are in the UniProt reference list but are not cached; they were
  not fetched because only files under `genes/yeast/CDC16/` were to be edited.
  PMID:15060174 (Schwickart 2004) is cached and was added to `references`.
- No history record was written (outside the permitted directory); one should be
  scaffolded with `just new-history` when this review is committed.
- Validation: `just validate yeast CDC16` → ✓ Valid, no warnings. Rendered to
  `CDC16-ai-review.html`.
