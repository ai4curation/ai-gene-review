# ARHGEF16 (Ephexin-4, NBR) — curation notes

UniProt Q5VV41 (ARHGG_HUMAN), 709 aa, chromosome 1p36.3. Dbl-family Rho guanine
nucleotide exchange factor: DH 284–468, PH 501–620, SH3 629–689, C-terminal
PDZ-binding motif 707–709. Two isoforms; Q5VV41-2 lacks residues 1–288
(`VSP_018149`), i.e. the whole N-terminal regulatory region and the first five
residues of the DH domain.

## 1. What the protein actually does

The direct, measured activity is **guanine-nucleotide exchange on RhoG**, and in
cells it is exclusive to RhoG:

> "Although the DH-PH domain of Ephexin4 did not exchange nucleotide on Rac1, it
> possessed GEF activity of RhoG in vitro"
> [PMID:20679435]

> "Flag-tagged Ephexin4 expressed in HEK293T cells bound to the nucleotide-free
> forms of RhoG and Rac1 but not to those of RhoA and Cdc42"
> [PMID:20679435]

> "However, we could observe no obvious increase in the activities of Rac1 and
> Cdc42 in HEK293T cells by expression of Ephexin4 in pull-down assays with
> GST-fused Cdc42/Rac1 interactive binding (CRIB) domain of Pak to precipitate
> GTP-bound active Rac1 or Cdc42"
> [PMID:20679435]

The Rac1 and Cdc42 negatives were run with Dock180 and Zizimin1 as positive
controls, and the RhoA negative with a Rhotekin-RBD pull-down against Ephexin1 as
the comparator:

> ", 2005), but we could not detect the increase in RhoA activity in cells
> expressing Ephexin4, as measured by pull-down assays with GST-fused Rho-binding
> domain (RBD) of Rhotekin"
> [PMID:20679435]

Rac1 *is* activated downstream, but by DOCK4, not by ARHGEF16: active RhoG
recruits ELMO2 and the Rac GEF Dock4 to EphA2 at the tips of cortactin-rich
protrusions [PMID:20679435]. UniProt encodes this correctly — "mediating the
activation of RAC1 by EPHA2" — and the distinction matters because it is the
difference between an `enables` and an `involved_in`.

Region 275–481 of the human protein is annotated by UniProt as "Required for RHOG
activation and mediates interaction with EPHA2"
(`ECO:0000269|PubMed:20679435`).

## 2. The Ephexin family, and who is who

Five human ephexins, easily confused in the literature and in transfer:

| Protein | UniProt | Gene | GTPase |
|---|---|---|---|
| Ephexin-1 | Q8N5V2 | NGEF | RhoA (also Rac1/Cdc42) |
| Ephexin-2 | Q8IW93 | ARHGEF19 | RhoA |
| Ephexin-3 / TIM | Q12774 | ARHGEF5 | RhoA |
| **Ephexin-4** | **Q5VV41** | **ARHGEF16** | **RhoG only** |
| Ephexin-5 | O94989 | ARHGEF15 | RhoA |

> "The function of Ephexin1 has been characterized relatively well. This protein
> is a GEF for RhoA and functions in axon guidance and spine morphogenesis by
> interacting with EphA4 [9,10,11,12]. Several other Ephexins are also GEFs for
> RhoA [13,14,15]; however, Ephexin4 displays GEF activity for RhoG, rather than
> for RhoA."
> [PMID:30445756]

So ARHGEF16 is the one family member whose substrate is *not* RhoA. Every
substrate-level transfer from a sibling is therefore wrong for this protein, and
the two IBAs that carry sibling donors have to be read with that in mind (§5).

Reference check: all four of affinage's mechanistic citations
([PMID:21139582], [PMID:25063526], [PMID:30305138], [PMID:32811808]) name
ARHGEF16/Arhgef16 explicitly, and [PMID:19707205] mentions it twice, so none of
them is a sibling mix-up. The retrieval failure is the other way round — see §7.

## 3. The defect: a GAP molecular function on a GEF

GOA row: `GO:0005096 GTPase activator activity`, **IDA**, `PMID:21139582`,
assigned by BHF-UCL, dated 2025-02-21.

`GO:0005096` is the GAP term. GO API definition: "Binds to and increases the
activity of a GTPase, an enzyme that catalyzes the hydrolysis of GTP." Its
synonyms are `Rho GAP activity`, `Rac GAP activity`, `Ras GAP activity` … and its
alternative ids are the merged substrate-specific GAP terms
(`GO:0005097`, `GO:0005098`, `GO:0005100`, `GO:0008060`, `GO:0030675`,
`GO:0046582` …). A GAP accelerates GTP hydrolysis and *switches the GTPase off*.

What [PMID:21139582] measured is nucleotide exchange, i.e. the opposite:

> "In vitro kinetic analysis confirmed that recombinant ARHGEF16 activates Cdc42
> and this was increased by the addition of recombinant Tip-1 and E6."
> [PMID:21139582]

The paper's own title calls ARHGEF16 a GEF ("Guanidine exchange factor
(GEF)-catalysed activation of Rho proteins"), and the protein has no GAP domain —
UniProt lists DH, PH and SH3 only, and the InterPro signatures are `IPR000219`
(DH) and `IPR047271` (Ephexin-like). The annotation looks like the word
"activates" being routed to the *activator* term.

**What makes this a trap rather than carelessness.** The same curator, on the same
paper, chose the correct BP term, and UniProt on the RhoG paper chose the BP term
`GO:0090630 activation of GTPase activity`. That BP term's *name* reads like the
GAP MF, but its definition is exchange-based: "Any process that initiates the
activity of an inactive GTPase through the replacement of GDP by GTP" (GO API),
with synonyms `Rho GTPase activation`, `Cdc42 GTPase activation`. So
`GO:0090630` is the GEF BP and `GO:0005096` is the GAP MF, and the two sit one
word apart. `GO:0090630` on this gene is right; `GO:0005096` is not.

**It has already propagated.** Mouse Arhgef16 (Q3U5C8) carries `GO:0005096`
twice — `ISO` (`GO_REF:0000119`, from `UniProtKB:Q5VV41`) and Ensembl Compara
`IEA` (`GO_REF:0000107`, from `UniProtKB:Q5VV41|ensembl:ENSP00000367629`) — and
mouse has no experimental GO annotation of its own at all. Correcting the human
row clears three rows across two species.

## 4. GO cannot say which GTPase — everywhere

The one fact that distinguishes Ephexin-4 from every sibling is its substrate, and
every GO handle for substrate identity has been merged into a general parent:

| What you want to say | Term | Status |
|---|---|---|
| Rho GEF activity | `GO:0005089` | merged → `GO:0005085` |
| Rac GEF activity | `GO:0030676` | merged → `GO:0005085` |
| Ras / ARF / Rab / Ran GEF activity | `GO:0005088`, `GO:0005086`, `GO:0017112`, `GO:0005087` | merged → `GO:0005085` |
| Rho GTPase binding | `GO:0017048` | merged → `GO:0031267` |
| activation of Rho/Rac/Cdc42 GTPase activity | `GO:0032858`–`GO:0032864` | merged → `GO:0090630` |
| Rho GAP activity | `GO:0005100` (and 8 siblings) | merged → `GO:0005096` |

Cross-checked on two independent services, because the claim is load-bearing:

- GO API: `GO:0005089` is listed among `alternativeIds` of `GO:0005085`;
  `GO:0005085/subgraph` returns 0 descendants.
- OLS4: `GO:0005089` is `is_obsolete: True`, `term_replaced_by: GO_0005085`;
  `hierarchicalChildren` of `GO:0005085` returns `totalElements: 0`.
- QuickGO (third check, and a caution): the children endpoint for `GO:0005085`
  returns two entries, `GO:1905098` by `negatively_regulates` and `GO:0032045` by
  `capable_of` — neither an `is_a` child. Asked for `GO:0017048`, QuickGO silently
  returns `GO:0031267`'s record with `isObsolete: false`, which is the
  merge-resolution behaviour that makes its obsolescence answers unreadable in
  either direction.

Consequence for this review: substrate identity is carried in
`core_functions[].substrates` and as `RO:0002233 has_input` extensions on the
`GO:0005085` rows, and the gap is recorded as an ONTOLOGY knowledge gap. No new
term is proposed — GO merged these deliberately.

## 5. The IBAs, read as phylogeny

- `GO:0005085` IBA, node `PTN002656129`, donors `MGI:MGI:3045246`, `O94989`
  (Ephexin-5), `Q12774` (Ephexin-3), `Q8N5V2` (Ephexin-1), and `Q5VV41` itself.
  Sound: DH-domain exchange activity is genuinely family-wide, and the target's
  own accession appearing among the donors is the expected marker that the node
  was seeded partly by ARHGEF16's own IDA. Worth stating plainly, though, that
  this IBA is only correct *because the term is coarse* — at `GO:0005089`
  granularity, three of the four donors would have transferred RhoA specificity to
  a protein that demonstrably does not touch RhoA.
- `GO:0032956 regulation of actin cytoskeleton organization` IBA, same node,
  donors `O94989`, `Q12774`, `Q8IW93` — three ephexin siblings and no
  ARHGEF16-specific evidence. Still supported on this gene by its own literature
  (cortactin-rich protrusions, membrane ruffles), but it is a family-level
  inference, not a core function.
- `GO:0032489 regulation of Cdc42 protein signal transduction` IBA, node
  `PTN002656172`, donors `PTN002656172` and `Q5VV41` only. The node rests entirely
  on ARHGEF16's own IDA from [PMID:21139582] — the contested Cdc42 arm (§6). Not
  circular in the schema's sense (the target's own experimental annotation is
  legitimately one of the descendant evidences), but its support is exactly as
  strong as that one experiment and no stronger.

## 6. The Cdc42 conflict, and how it reconciles

Two papers disagree about Cdc42.

- [PMID:21139582], in vitro kinetics on recombinant protein: ARHGEF16 activates
  Cdc42, "increased by the addition of recombinant Tip-1 and E6"; Cdc42
  co-immunoprecipitated with ARHGEF16 "in the presence of high-risk HPV E6".
- [PMID:20679435], in cells: no increase in Cdc42 activity, and no binding to
  nucleotide-free Cdc42, with Zizimin1 as the positive control.

These are reconcilable rather than mutually destructive. Every positive Cdc42
result in [PMID:21139582] is conditioned on Tip-1 and/or HPV16 E6 being present;
the Cdc42-negative experiments in [PMID:20679435] were done in HEK293T without
either. So the honest reading is that Cdc42 activation is a conditional,
cofactor-dependent activity in an HPV context, not the protein's constitutive
substrate. Both Cdc42 rows are kept, demoted to non-core, with the conflict
recorded. Neither is removed: both are experimental annotations made by curators
with the full text, and `REMOVE` is not for adjudicating a genuine scientific
disagreement.

## 7. Affinage retrieval: gates clean, recall poor

`affinage_deep_research.py human ARHGEF16` reported `trust gates clear`,
`self_evaluation_pairwise: win`, `faith_pct: 100.0`. Every one of its six
citations is genuinely about this protein. But a PubMed query for
`Ephexin4[Title/Abstract] OR ARHGEF16[Title/Abstract] OR "Ephexin-4"[Title/Abstract]`
returns 26 records, and affinage returned **none** of the seven that carry the
protein's mechanism:

| PMID | Year | What it establishes | In affinage? |
|---|---|---|---|
| 20679435 | 2010 | RhoG is the substrate; Rac1/Cdc42/RhoA are not | no |
| 21621533 | 2011 | anoikis suppression via RhoG and PI3K | no |
| 23772378 | 2013 | EphA2 pS897 recruits Ephexin4 | no |
| 28667327 | 2017 | Elmo1 relieves steric autoinhibition | no |
| 30445756 | 2018 | intermolecular autoinhibition; E295A (murine) | no |
| 33597305 | 2021 | crystal structures; double autoinhibition | no |
| 39675713 | 2025 | M-phase chromosome alignment via RhoG | no |

The common feature of all seven is that the title says **Ephexin4**, not
ARHGEF16 — including the one paper that GOA itself cites six times
([PMID:20679435]). A clean gate certified that the six citations returned were
real; it said nothing about the seven that were not. Searching the UniProt `RN`
list, the paralogs and the partners independently is what recovered them.

## 8. Regulation: why the PDZ and ELMO interactions are not "protein binding"

Ephexin4 is autoinhibited, by two independent modes:

> "The crystal structures of partially and fully autoinhibited Ephexin4 reveal
> that the complete autoinhibition requires both N- and C-terminal inhibitory
> modes, which can operate independently to impede Ras homolog family member G
> (RhoG) access."
> [PMID:33597305]

> "Structural, enzymatic, and cell biological analyses show that phosphorylation
> of a conserved tyrosine residue in its N-terminal inhibitory domain and
> association of PDZ proteins with its C-terminal PDZ-binding motif may
> respectively relieve the two autoinhibitory modes in Ephexin4."
> [PMID:33597305]

The N-terminal mode is intermolecular — Ephexin4 oligomerises and the SH3 domain
of one molecule occludes the N20 region of another:

> "Elmo1 relieves the steric hindrance of Ephexin4 generated by the
> intermolecular interaction of the SH3 domain and makes Ephexin4 more accessible
> to RhoG."
> [PMID:28667327]

> "Mutation of the glutamate residue at position 295, which is a highly conserved
> residue located in the region of Ephexin4 required for the intermolecular
> interaction, to alanine (Ephexin4E295A) disrupted the intermolecular interaction
> and increased binding of RhoG, resulting in augmented RhoG activation."
> [PMID:30445756]

That E295 is **murine** numbering: the methods state "All Ephexin4 mutants were
generated by a polymerase chain reaction (PCR)-based strategy from the murine
Ephexin4 cDNA (NM_001112744)" [PMID:30445756], i.e. Q3U5C8, 713 aa. Human Q5VV41
position 295 is a serine. Pairwise alignment (see
`ARHGEF16-bioinformatics/residue_mapping.py`) puts murine E295 at **human E291**
and murine P271 at **human P267**, a uniform 4-residue offset across that region:
mouse `EERKRQEAIFE(295)ILTSEFSY` against human `EERKRQEAMFE(291)ILTSEFSY`. The
residue claim in the review is anchored on human E291 with the murine construct
position recorded as the source, never on an alignment column.

The practical consequence for curation: `GO:0030165 PDZ domain binding` (IPI,
TAX1BP3) is not an incidental interaction. It is one of the two de-repression
switches for this protein's catalytic activity. Same for the ELMO1/ELMO2
interactions, which are both the de-repressor and the downstream effector.

## 9. The interactome rows

Fifty of the 77 GOA rows are `GO:0005515 protein binding` IPI, and they are not
fifty biological partnerships. They partition almost entirely into three
mechanistic classes, all explained by two short motifs:

- **PDZ-domain screens** — [PMID:36115835] (quantitative fragmentomics, 37 rows),
  [PMID:30126976], [PMID:32203420], [PMID:32296183]. Partners are DLG1-5, MAGI1-3,
  SCRIB, PATJ, MPDZ, PDZD2/7, PDZK1, NHERF2/4, PARD3/3B, TJP1-3, USH1C, WHRN,
  SNTB2, GRIP1/2, LNX1/2, SDCBP/SDCBP2, PTPN13. Every one is a PDZ-domain protein
  binding the C-terminal `707-709` motif — i.e. 30-odd rows reporting one binding
  site.
- **14-3-3 screens** — [PMID:15161933], [PMID:15778465], [PMID:28514442],
  [PMID:33961781], [PMID:36931259]. Partners YWHAZ, YWHAE, SFN. ARHGEF16 carries
  ten mapped phosphoserines (S6, S41, S107, S174, S191, S208, S227, S230, S240 and
  T226), so phospho-dependent 14-3-3 capture is expected.
- **Proteome-scale interactome maps** — [PMID:25416956], [PMID:32296183],
  [PMID:33961781], [PMID:28514442].

`GO:0045296 cadherin binding` (HDA, [PMID:25468996]) is from an E-cadherin
interactome pulldown, not a binary assay. Given that the same C-terminal motif
binds the PDZ scaffolds that organise junctions, an indirect capture in a
cadherin complex is the parsimonious reading.

## 10. Biology absent from GO

Three well-supported functions have no GO annotation on this gene in any species:

- **Anoikis suppression.** "Knockdown of Ephexin4 promoted anoikis in HeLa cells,
  and experiments using a knockdown-rescue approach showed that activation of
  RhoG, phosphatidylinositol 3-kinase (PI3K), and Akt was required for the
  Ephexin4-mediated suppression of anoikis" [PMID:21621533]; corroborated in
  [PMID:23772378]. Human cells, knockdown plus rescue. Proposed as `NEW`,
  `GO:2000811 negative regulation of anoikis`.
- **M-phase chromosome alignment.** "The Ephexin4 knockdown caused chromosome
  misalignment and reduced the RhoG localization to the plasma membrane. These
  phenotypes were rescued by re-expression of wild type and phospho-mimic S41E
  mutant, but not the S41A mutant" [PMID:39675713]. Human HeLa and A549, published
  2025 and not yet curated. S41 is one of the phosphosites already in UniProt
  (`MOD_RES 41 Phosphoserine`, from [PMID:18669648] and [PMID:20068231]).
- **Apoptotic cell clearance.** [PMID:25063526], [PMID:28667327], [PMID:30445756].
  These used **murine** Ephexin4 cDNA in hamster LR73 phagocytes, so the function
  belongs to mouse Arhgef16, and mouse Arhgef16 has zero experimental GO
  annotations — its entire GO record is projected from human. Recorded as a
  CURATION gap rather than proposed on the human gene.

## 11. Reactome places this protein on the wrong GTPase

The two `GO:0005829 cytosol` TAS rows trace to `Reactome:R-HSA-419166 "GEFs
activate RhoA,B,C"` and `Reactome:R-HSA-205039 "p75NTR indirectly activates RAC
and Cdc42 via a guanyl-nucleotide exchange factor"`. The catalyst of R-HSA-419166
is a 48-member `DefinedSet` of essentially every human Dbl-family GEF — it
contains ARHGEF16 alongside TIAM1/TIAM2 (Rac-only), FGD1–FGD4 and ITSN1
(Cdc42-only), SOS1/SOS2 and RASGRF2 (Ras), and all five ephexins. Membership is by
DH domain, not by measured specificity, and the reaction's output is
`RHOA/B/C:GTP` — the one thing [PMID:20679435] explicitly failed to detect for
this protein.

The GO consequence is limited: only the `cytosol` CC term reaches GOA, and that is
uncontroversial. But it is the same shape as the ARHGAP11B case — a set-level
pathway entity conferring a substrate specificity that the member does not have —
and a reader of the Reactome page is told ARHGEF16 activates RhoA. Recorded as
provenance on the TAS rows, not as a GO error.

## 12. Disease and cancer literature

- HPV16 E6 upregulates ARHGEF16 at protein level; E6/Tip-1/ARHGEF16 may cooperate
  to activate Cdc42 [PMID:21139582].
- GLI2 binds the ARHGEF16 promoter; ARHGEF16 promotes glioma migration and
  proliferation via CKAP5 [PMID:30305138].
- FYN binds ARHGEF16 and is required for its pro-proliferative effect in colon
  cancer [PMID:32811808]; expression correlates with colon cancer proliferation,
  migration, invasion [PMID:38192976].
- ARHGEF16 overexpression transforms NIH3T3 cells; suppressed by Y27632 analogues
  [PMID:19707205]. ROCK-inhibitor pharmacology paper, ARHGEF16 used as a model.
- One missense in the PDZ-binding domain in a single oligodendroglioma; not a
  recurrent driver [PMID:21760942].
- Originally cloned as `NBR`, a neuroblastoma candidate at 1p36.3 (UniProt Ref. 1).

None of these support a GO process term for the gene product itself; they are
expression/association findings or pathway context. Kept out of
`existing_annotations` and out of `core_functions`.

## 13. DH/PH catalytic assessment

See `ARHGEF16-bioinformatics/RESULTS.md`. Reported in both directions there: the
DH surface residues that contact the GTPase in solved Dbl-family complexes, which
of them ARHGEF16 retains, what the positive comparators show, and — explicitly —
why retention does not by itself establish activity and loss would not by itself
refute it. For this protein the residue analysis is confirmatory only: the
activity is directly measured on purified DH-PH protein [PMID:20679435], so the
sequence never had to carry the argument.
