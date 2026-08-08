# ACTR8 (ARP8, hArp8) — review notes

UniProt: `Q9H981` (ARP8_HUMAN), 624 aa, Swiss-Prot reviewed, `PE 1: Evidence at protein level`.
Family: `[file:human/ACTR8/ACTR8-uniprot.txt "Belongs to the actin family. ARP8 subfamily."]`
Structure: `[file:human/ACTR8/ACTR8-uniprot.txt "DR   PDB; 4FO0; X-ray; 2.60 A; A=34-624."]`

GOA snapshot reviewed: 32 TSV data rows → 31 review rows (GOA carries the
`GO:0031011`/IDA/`PMID:21303910` row **twice**, once from ComplexPortal and once from
UniProt; the seeder de-duplicates it).

---

## 1. Provider record: empty, and that is a provider gap, not a literature gap

The affinage record has `n_discoveries: 0`, `citation_count: 0`, no findings table and no
citations, and no `self_evaluation_pairwise` score; the trust gates were clear only vacuously —
there is nothing to gate. Per the campaign
rule, an empty provider record is **not** evidence that literature is absent, and here it is
demonstrably wrong: the UniProt `RN` list alone carries 13 references including a 2.6 Å crystal
structure paper with `FUNCTION, SUBUNIT, AND ATP-BINDING SITES` in its `RP` line
(`PMID:22977180`). ARP8 is one of the **best-characterised** nuclear actin-related proteins.
Nothing in this review rests on the provider record.

Everything below was assembled from UniProt, the GOA TSV, QuickGO, the PANTHER PAINT file
committed in this repo, ComplexPortal, IntAct and 20 primary papers.

Retraction screen: all 20 PMIDs cited here were checked against PubMed publication types and
an explicit `retracted publication[pt] OR expression of concern[pt]` query over the whole set —
**0 hits**. No reference in this review is retracted or carries an expression of concern. **But
that method is insufficient on its own — see §15**, which records one Publisher Correction it
missed and the check that finds them.

---

## 2. What ARP8 actually is

Two distinct jobs, and the literature separates them cleanly.

**(a) The nucleosome-recognition module of INO80.** ARP8 sits with ARP4, nuclear actin and the
HSA domain of the INO80 ATPase in one of the three modules of the human complex
[PMID:21303910 "the actin-related proteins Arp4 and Arp8, and the GLI-Kruppel family transcription factor YY1"],
and that module is part of the catalytically competent core
[PMID:21303910 "ATP-dependent nucleosome remodeling by the hINO80 complex is catalyzed by a core complex comprising the hIno80 protein HSA/PTH and Snf2 ATPase domains acting in concert with YY1 and the complete set of its evolutionarily conserved subunits"].
A recombinant **human** minimal core containing ARP8 slides nucleosomes
[PMID:27257055 "The complex comprises one subunit each of an N-terminally truncated Ino80, actin, Arp4, Arp5, Arp8, Ies2 and Ies6, together with a single heterohexamer of the Tip49a and Tip49b proteins."],
[PMID:27257055 "This core complex has nucleosome sliding activity that is similar to that of endogenous human and yeast Ino80 complexes"].

The recognition itself is quantified on the purified human protein
[PMID:22977180 "strongly prefer nucleosomes and H3-H4 tetramers over H2A-H2B dimers, suggesting that Arp8 functions as a nucleosome recognition module"].
**Table 2 mixes species and must be read per-species** — see §13, where a cross-species join in my
first draft produced an inverted conclusion. The human rows only:

| ligand | HsArp8 `K_d,app` (nM) | Hill `nH` |
|---|---|---|
| 207-bp nucleosome | **51.0 ± 9.6** | 1.31 ± 0.4 |
| (H3–H4)₂ | **110 ± 40.4** | 1.11 ± 0.3 |
| H2A–H2B | **555 ± 158** | 0.91 ± 0.2 |
| 30-bp dsDNA | **6938 ± 3448** | 2.6 ± 0.6 |

`HsArp8 Δ1–33` is closely comparable (nucleosome 62.6 ± 16, `nH` 2.11 ± 0.4)
[PMID:22977180 "All Arp8 variants bind (H3–H4)2 and nucleosomes with comparable affinity, while the interaction with H2A–H2B is"],
[PMID:22977180 "We conclude that the contribution of Arp8 to the nucleosome-binding ability of INO80 is significant."].
The paper reports cooperativity
[PMID:22977180 "This suggests cooperative binding of more than one Arp8 molecule per nucleosome"],
and this is the biochemical basis of UniProt's dimer statement
`[file:human/ACTR8/ACTR8-uniprot.txt "it may act as a nucleosome recognition module within the complex."]` —
but note the **full-length human** value `nH` = 1.31 ± 0.4 overlaps 1; the unambiguous cooperativity is
in `Δ1–33` (2.11 ± 0.4) and the *yeast* sub-complex (3.13 ± 0.7). The `GO:0031491` proposal therefore
rests on the **affinity**, not on the Hill coefficient.

**(b) A mitotic, INO80-independent role on condensed chromosomes.**
[PMID:18163988 "Here we report that hArp8, but not hArp5, accumulates on mitotic chromosomes."],
[PMID:18163988 "Expression of truncated hArp8 proteins and depletion of endogenous hArp8 by RNA interference caused misalignment of mitotic chromosomes, suggesting that chromosome-associated hArp8 has a role in chromosome behavior."],
and decisively
[PMID:18163988 "In contrast, depletion of hIno80 and hArp5 did not cause misalignment of chromosomes, suggesting that the role of hArp8 at mitotic chromosomes is independent of the activity of hINO80 complexes."].
This is why UniProt records
`[file:human/ACTR8/ACTR8-uniprot.txt "Note=Specifically localizes to mitotic"]` chromosomes,
and why ARP8–ACTR5 co-IP is seen in interphase but not in metaphase-arrested cells.

**Consequence for curation:** GOA has **no** term for (b). `GO:0007080 mitotic metaphase
chromosome alignment` is not a descendant of `GO:0033044 regulation of chromosome organization`
(checked against the QuickGO ancestor list: GO:0007080's ancestors include GO:0051276 but not
GO:0033044), so it is a genuine addition, not a specificity upgrade of an existing row.

---

## 3. Residues, both directions — answered from the human crystal structure, not an alignment

The brief's residue check does not need a homology model here: PDB `4FO0` is human ARP8 itself.

**ATP pocket: retained, and the activity was measured.**
[PMID:22977180 "We report the crystal structure of the INO80 complex subunit Arp8 in its ATP-bound form."]
ATP is *observed*, not inferred; UniProt's `BINDING` features (`55`, `56`, `283..286`) carry no
`ECO:0000250` similarity tag and come from this structure
`[file:human/ACTR8/ACTR8-uniprot.txt "FT   BINDING         55"]`. The pocket is functional:
[PMID:22977180 "We tested the structure-based hypothesis that Arp8 harbours weak ATPase activity by a 32P ATP hydrolysis assay."],
[PMID:22977180 "We found that yeast and human Arp8 possess a low basal ATPase activity, while Arp4 did not hydrolyse ATP above background"].
The authors bound their own claim, and I keep the bound:
[PMID:22977180 "In summary, the intact nucleotide-binding site suggests that Arp8, like actin, is an extremely weak ATPase in a monomeric state."],
and no ligand they tested stimulated it
[PMID:22977180 "We did not find a significant stimulation or inhibition"].
Catalytic-activation residues are *substituted*, not conserved: actin's Q137 → E266^Arp8^,
actin's H73 sensor → R187^Arp8^. So hydrolysis exists but has no demonstrated physiological
trigger. Verdict: **ATP binding is established; ATP hydrolysis is measured but functionally
unassigned** — I propose the former and file the latter as a question, not a term.

**Polymerisation interface: not retained, and structurally explained.**
[PMID:22977180 "Human Arp8 has several insertions in the conserved actin fold that explain its inability to polymerize."]
This is the positive structural argument that a cytoskeletal-actin term does not belong on
ARP8 — and it is not needed, because no such term is in GOA and PAINT actively blocks it
(section 5).

**The pocket is not decorative — it gates DNA binding.**
[PMID:25299602 "addition of ATP significantly inhibited the DNA binding activity of the wild-type Arp8"],
and the effect is lost in pocket mutants
[PMID:25299602 "these results suggest that the S55, T56, K288, and S290 residues of Arp8, all of which are located in the ATP binding pocket, might play some regulatory role in the binding of Arp8 to DNA in the presence of ATP"],
i.e. exactly the residues UniProt annotates as ATP-binding. That is a *functional* consequence
of nucleotide occupancy, which is more than most ARPs can show.

**Sibling consistency (checked, not assumed).** ACTR1A and ACTR1B each proposed `GO:0043531
ADP binding` as `NEW`; ACTR10 proposed `GO:0005524 ATP binding` as `NEW`. Same stated method —
annotate the ligand actually resolved — different observed ligand. ARP8's structure resolves
**ATP**, so `GO:0005524` is the consistent choice, not a divergence.

---

## 4. DNA binding: two papers that look contradictory and are not

- 2012, 30-bp duplex, fluorescence titration:
  [PMID:22977180 "Both human and yeast Arp8 bind to DNA with low affinity in the micromolar range, while no interaction with DNA was observed for Arp4."]
  and the complex's DNA affinity is attributed elsewhere:
  [PMID:22977180 "The sub-complex I on the other hand has substantial DNA-binding activity (366 nM), which most likely is accounted for by the HSA/DBINO domain with a potential minor contribution of Arp8"].
- 2014, long linear/circular DNA and ssDNA, gel shift:
  [PMID:25299602 "Gel shift analysis revealed that the full length Arp8 bound to a linearized plasmid DNA"],
  [PMID:25299602 "Gel shift assay revealed that indeed Arp8 forms a stable complex with the ssDNA"],
  [PMID:25299602 "These results suggest that Arp8 binds preferentially to ssDNA and that this property likely contributes to recruiting the INO80 complex to the DSB sites"].

Reconciliation: the 2012 assay used a **30-bp** duplex, the 2014 assay long DNA and ssDNA, and
the binding element is the basic N-terminal extension
[PMID:25299602 "The N-terminal extension of the human Arp8 is abundant in basic amino acids."]
which is dispensable for a 30-mer but required for long duplex
[PMID:25299602 "which lacked the N-terminal extension, was unable to cause any shift in the DNA mobility"].
Independent yeast corroboration of the same element (labelled as yeast, not asserted for human):
[PMID:30120252 "We show that the N-terminus of Arp8, C-terminus of Arp4 and the HSA domain of Ino80 bind extranucleosomal DNA 37-51 base pairs from the edge of nucleosomes and function as a DNA-length sensor that regulates nucleosome sliding by INO80."]

**So the well-founded MF is the specific one, `GO:0003697 single-stranded DNA binding`,** not a
bare `GO:0003677 DNA binding`: ssDNA is the *preferred* ligand in a direct competition assay
(dsDNA vs 3′-overhang vs ssDNA), and it is the ligand whose relevance to DSB-end resection the
authors argue. Neither term is in GOA.

---

## 5. PANTHER node `PTN000234048`: the nuclear-ARP/cytoplasmic-actin question, both directions

This is the check that damaged ACTL8 (a divergent actin mis-placed *inside* the β/γ-actin
subfamily) and ACTR10 (a nuclear term transferred *in* from another subfamily). For ACTR8 both
directions come back **clean**, and the second direction comes back better than clean.

Census, via QuickGO `withFrom=PANTHER:PTN000234048` (paged; `numberOfHits` = **348**, all 348
fetched): **87 distinct gene products, each carrying exactly the same 4 terms** (`GO:0003729`,
`GO:0006302`, `GO:0006355`, `GO:0031011`). Every named member is an ARP8 orthologue —
`ACTR8`/`Actr8`/`actr8`/`arp8`/`ARP8`/`arp-8`/`arpG`, plant `ARP9` — across plants, fungi,
metazoa, *Giardia* and *Paramecium*. **Zero conventional actins**: a regex sweep for
`ACTB|ACTG*|ACTA*|ACT1|ACT2|POTE|ACTL*|ACTR[0-7,9]` over the member symbol list returns an
empty set. So this node is an ARP8-specific orthogroup, not the broad actin node, and no
cytoplasmic-actin cell biology can enter ACTR8 through it.

The reciprocal direction is the interesting half. The repo's own PAINT file shows PAINT has
placed an explicit **negative** at this node:
`[file:interpro/panther/PTHR11937/PTHR11937-paint.tsv "PTHR11937 PTN000234048 GO:0005200 F IRD true PANTHER:PTN000940351"]`
— `IRD`, `NOT`-flagged, against `PTN000940351`, which is the conventional-actin node
`[file:interpro/panther/PTHR11937/PTHR11937-paint.tsv "PTHR11937 PTN000940351 GO:0005200 F IBD false SGD:S000001855|UniProtKB:P61160"]`
(donors include yeast ACT1 and human ACTB `P60709`; 969 annotations over ≥200 gene products, all
`GO:0005200`). PTHR11937 carries **9** `GO:0005200` rows in total, of which **8 are IRD
negatives** at divergent nodes and 1 is the IBD positive at the actin node.

So `GO:0005200 structural constituent of cytoskeleton` is *deliberately blocked* from reaching
ARP8, and that block agrees exactly with the human crystal structure's "inability to polymerize"
finding. ACTL7A and ACTL7B each had to `REMOVE` a `GO:0005200` TAS row; ARP8 never acquired one.
This is PAINT working correctly on the same family where it failed for ACTL8 — worth reporting
upstream as the positive control for that fix.

### The reciprocal direction: is ARP8 a *donor* in the nucleus leak that hit ACTR10?

**No.** ACTR10 merged into `main` mid-review (#2274) with its `GO:0005634 nucleus` IBA set to
`REMOVE` as a paralog transfer, so it was worth asking whether ARP8 — a genuinely nuclear ARP —
was the source. Reading the merged review's `source_entities`, ACTR10's nucleus donors are
`SGD:S000004636` (*S. cerevisiae* ARP9, a SWI/SNF and RSC subunit), `CGD:CAL0000196900`
(*Candida* ARP9), `MGI:MGI:1343051` (mouse Actl7a) and `UniProtKB:Q57ZL0` (an unreviewed
*Trypanosoma* entry), at node **`PTN008986520`** — a different and deeper node than
`PTN000234048`, with **no ARP8 orthologue among them**. Confirmed against ACTR10's own GOA
WITH/FROM field, which lists exactly those five tokens.

So the nuclear leak in PTHR11937 runs through the **ARP9/ACTL7** side of the family, not the
ARP8 side, and ARP8's own nuclear terms are independently earned. Both halves of the brief's
question answered, and both negatives recorded.

### Sibling-review consistency, checked row by row

| gene | protein binding | nucleotide ligand | GO:0005200 |
|---|---|---|---|
| ACTR8 (this) | `KEEP_AS_NON_CORE` ×6 | `GO:0005524` **IDA** (ATP in 4FO0) | absent; PAINT IRD-blocked |
| ACTR10 | `MARK_AS_OVER_ANNOTATED` ×2, `MODIFY` ×1 | `GO:0005524` **ISS** (by alignment) | `ACCEPT` (genuine capping subunit) |
| ACTR1A | `KEEP_AS_NON_CORE` | `GO:0043531` ADP (9B85) | `NEW` |
| ACTR1B | `KEEP_AS_NON_CORE` ×4, `MARK_AS_OVER_ANNOTATED` ×1 | `GO:0043531` ADP | — |
| ACTL7A | `KEEP_AS_NON_CORE` ×2, `MODIFY` ×1 | — | `REMOVE` |
| ACTL7B | `MARK_AS_OVER_ANNOTATED` ×4 | — | `REMOVE` |

None of these is an inconsistency, and each difference is traceable to the evidence rather than
to the rule:

- **Protein binding** — the shared rule is *decide per partner*. ACTR8's two partners (ACTR5,
  UCHL5) are both co-members of its own ComplexPortal complex, each established by a targeted
  experiment; ACTR10's and ACTL7B's were screen singletons. Same rule, different partners.
- **Nucleotide ligand** — the shared rule is *annotate the ligand actually observed*. ARP8's own
  structure resolves ATP, so IDA; ACTR10 had to reconstruct its site by transferring β-actin's
  contacts across an alignment, so ISS; the Arp1 paralogs resolve ADP, so `GO:0043531`. This is
  the "convergent method, divergent term" pattern — no reconciliation needed.
- **`GO:0005200`** — ACTR10 keeps it because Arp11 really is a dynactin filament constituent;
  ACTL7A/7B lose it because their filament interfaces are not conserved; ARP8 never had it
  because PAINT blocked it, in agreement with the human structure. Three outcomes, one criterion.

Per-node term assignment for `PTN000234048` (all 5 rows, from the committed PAINT file):

| term | code | donors | date |
|---|---|---|---|
| `GO:0031011` Ino80 complex | IBD | SGD ARP8, FB Arp8, **human ACTR8**, PomBase arp8 | 2021-11-10 |
| `GO:0003729` mRNA binding | IBD | **SGD ARP8 only** | 2025-08-05 |
| `GO:0005200` structural constituent of cytoskeleton | **IRD (NOT)** | PTN000940351 (actin node) | 2025-08-05 |
| `GO:0006302` double-strand break repair | IBD | **SGD ARP8 only** | 2019-03-01 |
| `GO:0006355` regulation of DNA-templated transcription | IBD | **human ACTR8**, FB Arp8 | 2023-04-05 |

Two of the four positives are **self-referential** (human `Q9H981` is itself in the WITH/FROM
list) → `NO_FAILURE_CORE`, a PAINT curator judging the function core for this gene.

---

## 6. Donor evidence, queried per term (not merely resolved)

All WITH/FROM accessions resolved with `size=5`, `primaryAccession` checked against the request,
and Swiss-Prot/TrEMBL status printed. Every one is a **reviewed** entry; no dead accessions, no
TrEMBL name-provenance traps.

| token | resolves to | status | length |
|---|---|---|---|
| `SGD:S000005667` | `Q12386` ARP8_YEAST, *S. cerevisiae* ARP8 | Swiss-Prot | 881 |
| `FB:FBgn0030877` | `Q9VX09` ARP8_DROME, *D. melanogaster* Arp8 | Swiss-Prot | 607 |
| `PomBase:SPAC664.02c` | `Q9US07` ARP8_SCHPO, *S. pombe* arp8 | Swiss-Prot | 662 |
| `UniProtKB:Q9H981` | the gene itself (self-referential IBA) | Swiss-Prot | 624 |
| `UniProtKB:Q8R2S9` | `Q8R2S9` ARP8_MOUSE, mouse Actr8 | Swiss-Prot | **624** |
| `ensembl:ENSMUSP00000016115` | → `ENSMUST00000016115` `Actr8-201` → `ENSMUSG00000015971` | mouse Actr8 | — |
| `PANTHER:PTN000234048` | internal tree node, **not a protein** | n/a | n/a |
| `UniProtKB:Q9H9F9` (partner) | `Q9H9F9` ARP5_HUMAN, ACTR5 | Swiss-Prot | 607 = canonical |
| `UniProtKB:Q9Y5K5` (partner) | `Q9Y5K5` UCHL5_HUMAN | Swiss-Prot | 329 = canonical |

**No paralogs in the donor set.** All are true ARP8 orthologues. That is unusual for this
campaign and it means every IBA row here has ortholog-strength support available in principle —
the questions are only *which* term and *how many* donors carry it.

Donor evidence for the term each donated, via QuickGO per-accession + per-GO queries:

- `GO:0031011` — yeast ARP8 `IPI` ×3 (`PMID:10952318`, `PMID:24034245`), Drosophila Arp8 `IDA`+`IPI`
  (`PMID:16618800`), *S. pombe* arp8 `IDA` (`PMID:19040720`) + `IPI` (`PMID:19933844`), human
  `IDA` ×3. **Four independent experimental donors plus the target's own IDA.** Unambiguous.
- `GO:0006355` — Drosophila Arp8 `IMP` (`PMID:16618800`); human self.
- `GO:0006302` — yeast ARP8 `IMP` (`PMID:23644470`).
- `GO:0003729` — yeast ARP8 `IDA` (`PMID:20844764`) and nothing else, in any species.

---

## 7. The two findings worth reporting upstream

### 7a. `GO:0003729 mRNA binding` — one yeast RIP-chip hit, propagated to 87 eukaryotes

I expected this to be an unvalidated screen artefact and **it is not** — checking rather than
assuming changed the verdict. Yeast ARP8 is in the paper's confirmed set:
[PMID:20844764 "Novel RBPs identified in the protein microarray experiments and confirmed by IP-microarray experiments."]
[PMID:20844764 "Other candidate RBPs (Vtc1, Arc15, Hsp26, Arp8, Gis2) co-purified with smaller sets of mRNAs, but these small sets of putative mRNA targets shared distinct functional and/or cytotopical themes, increasing our confidence that the RNA-protein interactions we observed were genuine."]
231 targets at FDR ≤ 0.01 **%** — the Methods define the cut-off as a SAM-calculated false
discovery rate *"less than or equal to 0.01%"*, i.e. 100-fold stricter than a bare 0.01 — and only
[PMID:20844764 "Of 35 putative novel RBPs identified by either or both of these methods, 12, including 75% of the eight most highly-ranked candidates, reproducibly associated with specific cellular RNAs."]
So the SGD `IDA` is sound and `SOURCE_EVIDENCE_WEAK` would be **factually wrong**.

What is wrong is the **propagation**, on three independent grounds:

1. **One donor, one study, whole eukaryotic clade.** `GO:0003729` is IBD from `SGD:S000005667`
   alone, added 2025-08-05, and now sits on all 87 members, no member outside *S. cerevisiae*
   having ever been assayed for RNA binding. **A single donor is not by itself the objection** —
   claiming otherwise would contradict this review's own `GO:0006302` row. Donor counts at the
   node are `GO:0031011` 4, `GO:0006355` 2, and `GO:0003729` and `GO:0006302` **one each**, yet
   `GO:0006302` is accepted. What separates them is target-side evidence: human ARP8 has direct
   DSB-repair data and no RNA data at all.
2. **The assay cannot distinguish RNA from DNA binding.** The primary screen is
   [PMID:20844764 "We describe here a proteome-wide approach to identify RNA-protein interactions based on in vitro binding of RNA samples to yeast protein microarrays that represent over 80% of the yeast proteome."]
   — RNA in, RNA out. No DNA competitor was included anywhere in the design. For a protein whose
   nucleic-acid-binding element is a **basic, disordered N-terminal extension** and whose
   demonstrated preference is for *single-stranded* nucleic acid, "binds polyanion" and "binds
   mRNA" are not separable by this experiment.
3. **The binding element differs in size between donor and target — but read the whole
   sentence.** My first draft of this point overstated it, and the correction is worth recording
   because it is the exact failure mode the campaign brief warns about. The tempting quote is
   *"It is rather short in human Arp8 compared to yeast Arp8"*. Continuing to the end of the
   qualifying clause:
   [PMID:22977180 "It is rather short in human Arp8 compared to yeast Arp8, but still comprises 46 mostly charged residues"].
   So the human protein **retains** a substantial basic extension. Yeast ARP8 is 881 aa against
   human 624 aa with much of the difference in this region, which makes the transfer less safe —
   it does not make it impossible. **Grounds (1) and (2) carry the argument; (3) only supports
   it.** A verbatim quote truncated one clause early would have read as a much stronger finding
   than the data support.

Verdict `MARK_AS_OVER_ANNOTATED`, not `REMOVE`: the donor annotation is real and I have no human
negative — no one has assayed human ARP8 with RNA. `REMOVE` would require a positive argument I
cannot supply, and an absence of human RNA data is an absence, not a finding.
`root_cause: PROPAGATION_BAD` (source sound, transfer unsafe), which is what my own reason
argues. `SOURCE_EVIDENCE_WEAK` is deliberately absent from `failure_modes` because my own
analysis contradicts it.

**`GRANULARITY_MISMATCH` — which half of the definition.** The enum definition has two arms:
*"Parent term is true but uninformative, **or** child term overstates specificity."* The brief's
caveat (donors must agree before invoking it) applies to the first arm. I invoke the **second**
arm here: the donor's own term names a ligand class its assay did not discriminate. Each row
using `GRANULARITY_MISMATCH` now states which arm it means — rows `GO:0033044` and `GO:0051052`
use the first (redundant true parent), rows `GO:0003729` and `GO:1904507` the second.
`FUNCTIONAL_DIVERGENCE` is deliberately **not** claimed on the mRNA-binding row: a change of
ligand class in the human protein has not been demonstrated, only that its *characterised*
ligand is a different one, and asserting divergence I have not measured would be the same error
as accepting an activity from a fold name.

### 7b. A complex-level phenotype became a subunit "IMP" and was then transferred across species

Five of ACTR8's 31 rows (`GO:0000723`, `GO:0006282`, `GO:0045739`, `GO:0045995`, `GO:1904507`)
are `IEA`/`GO_REF:0000107` from mouse Actr8. Tracing the mouse side:

- All five mouse Actr8 annotations come from **one** paper, `PMID:23979016`, and all five are
  `assignedBy: ComplexPortal`.
- Querying `reference=PMID:23979016` in QuickGO returns **80 annotations = 16 entities × 5
  terms**: `ComplexPortal:CPX-878` (mouse INO80 complex) plus **all 15 subunits**, byte-identical
  term/evidence sets on `Ino80`, `Ino80b/c/d/e`, `Ruvbl1/2`, `Yy1`, `Tfpt`, `Nfrkb`, `Mcrs1`,
  `Uchl5`, `Actl6a`, `Actr5` and `Actr8`.
- The paper's experiment is an **Ino80** knockout:
  [PMID:23979016 "Here, we use a conditional knockout approach to explore the cellular and organismal functions of mIno80."]
  The embryonic phenotype behind `GO:0045995` is an *Ino80*-null phenotype:
  [PMID:23979016 "mouse embryos die early during embryogenesis, while conditional deletion of mIno80 in adult mice results in weight loss and premature death"]
  and the telomere conclusions behind `GO:0000723`/`GO:1904507` are stated for the complex:
  [PMID:23979016 "Our studies suggest that the mIno80 chromatin remodeling complex plays important roles in telomere replication, HDR-mediated repair of dysfunctional telomeres, and maintenance of genome stability."]
  `Actr8` is not named in the abstract, and no *Actr8* mouse knockout exists.

ComplexPortal's own layer is a documented convention — it annotates the complex and projects to
members, and the complex context is recoverable from `CPX-878`. The defect is the **second**
step: Ensembl Compara consumes the projected subunit annotation as if it were gene-specific
mouse experimental evidence and re-projects it onto human ACTR8, at which point the complex
context is gone. Two inferences stacked, presented as one `IEA` from an ortholog. Hence
`root_cause: EVIDENCE_CIRCULAR_OR_REDUNDANT` with `CIRCULAR_PROPAGATION` + `ROLE_CONFLATION`:
the transfer depends on another inference, not on independent mouse-gene evidence.

Split by whether the term survives on ACTR8's *own* evidence:

- `GO:0006282` / `GO:0045739` (regulation / positive regulation of DNA repair) — **do** survive
  independently, on human ARP8-specific data
  [PMID:20971067 "We also found that an actin-related protein, ARP8, is an important subunit that is required for the recruitment of the mammalian INO80 complex to the DNA damage sites"]
  and [PMID:25299602 "This result suggests that knockout of Arp8 probably impairs DNA repair, which probably takes place via the HR or an HR-like repair process."].
  → `KEEP_AS_NON_CORE`, with the bad route recorded rather than the term deleted.
- `GO:0000723`, `GO:1904507`, `GO:0045995` — have **no** ARP8-specific support in any organism.
  → `MARK_AS_OVER_ANNOTATED`. Not `REMOVE`: ARP8 is a core INO80 subunit and I cannot show it is
  dispensable for these complex functions. The honest statement is that the specificity is
  unearned, not that the biology is false.

Generalisation for PAINT/GOA: **wherever ComplexPortal projects a complex phenotype to N
subunits, Ensembl Compara multiplies it by the number of species with 1:1 orthologues.** For
CPX-878 alone that is 15 subunits × 5 terms; ACTR8 is one of 15 human genes receiving the same
five rows by the same route. Stated once here, for all affected genes.

---

## 8. Interaction rows: the ACRV1/ACRBP checks, run and reported including the nulls

IntAct `findInteractions/Q9H981`: `totalElements` **82**. Methods: `anti tag coip` 55,
`anti bait coip` 18, `proximity-dependent biotin identification` 4, `tap` 2,
`2h fragment pooling` 1, `pull down` 1, `affinity chrom` 1.

- **Not one screen counted several ways.** The 82 records span **14 distinct publications**, and
  the two GOA partners are supported by *targeted* experiments, not only by maps: ACTR5 by
  `anti bait coip` in `PMID:18163988` at MI-score **0.67** (`physical association`), UCHL5 by the
  dedicated `PMID:18922472` study. So the ACRV1 pattern (one Y2H logged under three sub-method
  names) does **not** apply here.
- **Partner accessions are canonical.** `Q9H9F9` = reviewed ACTR5, 607 aa = canonical length;
  `Q9Y5K5` = reviewed UCHL5, 329 aa = canonical length. No TrEMBL clones, no ORFeome fragments,
  no dead accessions. This check came back negative and is recorded as such.
- **Both partners are bona fide complex co-members.** ComplexPortal `CPX-846` (human INO80
  chromatin remodeling complex) has 15 participants and **both** `Q9H9F9` and `Q9Y5K5` are among
  them, alongside `Q9H981`. So every `GO:0005515` row on ACTR8 is a within-complex contact whose
  informative content is already carried by `GO:0031011`.
- **A result worth recording, and a correction to my own first draft.** I initially wrote that
  INO80E is *"the most reproducibly detected ACTR8 partner in IntAct"*. **That was false** — an
  unverified superlative built on true constituents, which is the campaign's dominant failure
  shape. Ranking partners by distinct supporting publications:

  | partner | distinct pubs | MI-score(s) | in GOA `GO:0005515`? |
  |---|---|---|---|
  | YY1 | 5 | 0.80 | **no** |
  | INO80E | 5 | 0.79 | **no** |
  | UCHL5 | 4 | 0.35, 0.71 | yes |
  | RUVBL1 | 4 | 0.73 | no |
  | RUVBL2 | 4 | 0.73 | no |
  | ACTR5 | 3 | 0.67 | yes |

  YY1 ties INO80E on publication count and *beats* it on MI-score, so the superlative was wrong.
  The corrected statement is a **stronger** finding: **both** best-attested partners are absent
  from GOA, and the two that are recorded rank 6th and 3rd. The omission of YY1 is the sharpest
  case — `PMID:18026119` is *already cited on this gene* for the Ino80-complex IDA, and YY1 is the
  bait that paper used, so the contact rests on a reference GOA has in hand. Not a defect in the
  strong sense (curators select what to annotate), but it settles the direction: these six rows
  **under**-represent the interaction data.

Handling: all six `KEEP_AS_NON_CORE`, matching how the merged siblings treated *real, replicated*
partners (ACTR1A, ACTR1B, ACTL7A all used `KEEP_AS_NON_CORE`; `MARK_AS_OVER_ANNOTATED` was
reserved for singleton screen hits in ACTL8/ACTL7B). No divergence from sibling practice.

---

## 9. Where GOA's molecular-function coverage stands

QuickGO for `Q9H981`, `aspect=molecular_function`: **7 rows total** — 6 × `GO:0005515 protein
binding` and 1 × `GO:0003729 mRNA binding` (IBA). An explicit query for `GO:0005524` with
`goUsage=descendants` returns `total: 0`.

So the entire molecular-function record of a protein with a 2.6 Å ATP-bound crystal structure, a
measured ATPase, quantified nucleosome and histone-tetramer affinities and a demonstrated ssDNA
preference consists of "protein binding" six times plus one cross-kingdom RNA inference. The
`GO:0005524; F:ATP binding; IEA:UniProtKB-KW` line still present in the UniProt `DR` block is
**not** in GOA — consistent with the withdrawal of Swiss-Prot-keyword-derived annotations
(`GO_REF:0000043`) from GOA; `GO:0051301 cell division`, `GO:0006310 DNA recombination` and
`GO:0006351 DNA-templated transcription` disappeared from ACTR8 the same way.

That makes the MF gap the substantive deliverable, and it is filled from *human* experiments on
the *human* protein, not from the fold name. Proposed as `NEW`:

| term | evidence | source |
|---|---|---|
| `GO:0031491` nucleosome binding | IDA, `K_d,app` 51 nM, cooperative | `PMID:22977180` |
| `GO:0042393` histone binding | IDA, (H3–H4)₂ 110 nM vs H2A–H2B 555 nM | `PMID:22977180` |
| `GO:0003697` single-stranded DNA binding | IDA, preferred over dsDNA in direct competition | `PMID:25299602` |
| `GO:0005524` ATP binding | IDA, ATP resolved in PDB 4FO0; pocket mutants lose ATP-dependent regulation | `PMID:22977180`, `PMID:25299602` |
| `GO:0007080` mitotic metaphase chromosome alignment | IMP, RNAi → misalignment, INO80-independent | `PMID:18163988` |
| `GO:0000793` condensed chromosome | IDA, mitotic-chromosome accumulation | `PMID:18163988` |

`GO:0000793` is **additive**, not a replacement for the existing `GO:0005694 chromosome` row:
ARP8 is also on interphase chromatin as an INO80 subunit (it is required for INO80 recruitment to
laser-induced damage in interphase), so the general term remains the correct cover and the
condensed-chromosome pool is an extra.

`GO:0016887 ATP hydrolysis activity` is deliberately **not** proposed. It was measured on the
human protein, but the authors themselves place it at "extremely weak … in a monomeric state"
with no ligand able to stimulate it, so its physiological status is unresolved; it belongs in
`suggested_questions`, not in the annotation set. Accepting a hydrolase term off a measured but
functionally unassigned trace activity is the mirror of accepting one off a fold name.

---

## 10. Complex-subunit schema decisions

- INO80 membership goes in `core_functions[].in_complex` (`GO:0031011`), **never** `locations` —
  the latter is bound to a location enum and would fail validation. Verified `GO:0031011` is
  present in `cache/enums/goproteincontainingcomplexenum_*.csv`.
- `molecular_function` vs `contributes_to_molecular_function`: ARP8's binding activities were
  measured on the **isolated purified protein** (`Kd` values for nucleosome, (H3–H4)₂, H2A–H2B,
  DNA; ssDNA gel shifts on recombinant ARP8 alone), so ARP8 *independently enables* them and
  `molecular_function` is correct per the schema's `enables` definition. The one activity it does
  **not** independently enable is nucleosome remodelling — that is the INO80 ATPase's — so the
  remodelling core function is stated as a BP (`GO:0006338`) with the complex in `in_complex`,
  and no remodeller MF is claimed for ARP8.

---

## 11. Rows where I deliberately did not upgrade specificity

- `GO:0006355 regulation of DNA-templated transcription` (IBA) stays as-is even though ACTR8 has
  its own `IMP` to the child `GO:0045893`. The complex works in **both** directions — it
  activates [PMID:27641337 "It occupies enhancer regions near lung cancer-associated genes, and its occupancy correlates with increased genome accessibility and enhanced expression of downstream genes."]
  and it represses [PMID:26340092 "we first demonstrate that INO80 complex negatively regulates the p21Waf1/Cip1 (p21) expression in a p53-mediated mechanism"].
  A direction-neutral parent is the correct LCA, so `GRANULARITY_MISMATCH` does not apply: the
  donors and the target's own data do **not** agree on sign.
- `GO:0005694 chromosome` (IEA) → not modified to `GO:0000793`; see §9.
- `GO:0051052 regulation of DNA metabolic process` (ARBA) is true but wholly subsumed by the
  separately annotated `GO:0006275` and `GO:0006282`. Kept non-core rather than flagged as
  over-annotation: a redundant true parent is not an over-annotation.

## 12. Three claims of my own that a self-audit retracted

Recorded because the corrections are the useful part, and because each is a *composite* claim —
every constituent quote verbatim, the join unsupported. None would have been caught by quote
validation.

1. **"the most reproducibly detected ACTR8 partner in IntAct is INO80E"** — false; YY1 ties on
   publication count and beats it on MI-score. See §8; the corrected version is a stronger
   finding.
2. **"ARP8 was the only INO80 subunit whose depletion abolished recruitment"** — the source says
   [PMID:25299602 "among all the tested subunits only Arp8 was indispensable for recruiting the INO80 complex to DSB in human cells"].
   The qualifier is **"tested"**. Dropping it converts a screen result into a claim about every
   subunit. Restored in all three places the claim appears (the `GO:0006302` IBA row, the
   `GO:0006282` row, and core function 2), and the sentence is now quoted rather than paraphrased.
3. **"the only reported function of a nuclear actin-related protein detached from its remodelling
   complex"** — an unverifiable negative over the whole nuclear-ARP literature. Softened to
   "rarely reported … one of the few instances with genetic controls behind the claim", with the
   limitation stated inline.

The audit that found these was a grep for superlatives and absolutes (`the most`, `the only`,
`never`, `none of`, `no one has`, `all N`) over every string in the review plus these notes,
followed by re-deriving each hit from its source. Twelve numeric claims were re-derived
independently against QuickGO, ComplexPortal, IntAct and the committed PAINT file — node census
348/87/4 terms, MF row count 7, `GO:0005524` count 0, `PMID:23979016` 80 = 16 × 5, CPX-846 15
participants, IntAct 82 records / 14 publications, PTHR11937 9 `GO:0005200` rows = 8 IRD + 1 IBD,
and the two ontology-ancestry claims — all confirmed. The three failures above were all
*qualitative* superlatives, not numbers.

## 13. The error the reviewer caught: a cross-species join inside one table

Worth recording in full, because it is the single sharpest instance in this review of the failure
class the campaign says dominates — **every constituent number verbatim and correct, the join
invalid** — and no mechanical check could catch it.

I wrote, in the `GO:0031491` NEW reason:

> *"the isolated Arp8-Arp4-actin-HSA sub-complex binds nucleosomes at 64 nM, so ARP8 accounts for
> essentially all of the module's nucleosome affinity."*

Both numbers are real. The inference is not, because **`PMID:22977180` Table 2 is a mixed-species
table** and the paper says so in its own methods sentence: it assayed *"full-length and
N-terminally truncated human Arp8 as well as **yeast** Arp8, Arp4 and the Arp8–Arp4–actin-HSA
sub-complex I"*. The relevant rows, 207-bp nucleosome:

| protein | species | `K_d,app` (nM) |
|---|---|---|
| Arp8, full length | **Hs** | 51.0 ± 9.6 |
| Arp8 | **Sc** | **314 ± 35** |
| Arp8–Arp4–actin-HSA sub-complex | **Sc** | 63.6 ± 6.2 |

I had set the human 51 nM beside the **yeast** module's 63.6 nM. Matched within species the
comparison **inverts**: the module binds ~4.9× *tighter* than ScArp8 alone, so far from ARP8
accounting for "essentially all" of the module's affinity, assembly *increases* it. ARP8's
fractional contribution simply cannot be derived from these data, and the defensible statement is
the authors' own hedged one, which I already quote.

**Three further species labels were missing for the same reason**, all now fixed and each verified
against the source:

| claim | species, per the source |
|---|---|
| "ARP4 shows the opposite preference" (H3–H4 74.3 nM vs nucleosome 204 nM) | **Sc**Arp4 — a cross-species contrast |
| "ARP4 does not hydrolyse ATP above background" | **yeast** Arp4; Figure 3's caption says *"yeast and human Arp8 but not for yeast Arp4"* |
| sub-complex DNA binding "366 nM … mainly the HSA/DBINO domain" | **Sc** sub-complex; bounds the human claim only by analogy |

**Generalisable lesson: when a table's header enumerates species (`Hs`/`Sc`), treat every
cross-row comparison as cross-species until proved otherwise, and re-derive any ratio within one
species.** The affected verdicts did **not** change — `GO:0031491` IDA with `enables` rests on
HsArp8 at 51 ± 9.6 nM measured on the purified human protein — which is exactly why the error
survived my own audit: it sat in the *justification*, not in the term, the evidence code or the
qualifier, and my superlative sweep (§12) was looking for absolutes rather than for species.

Two smaller reviewer corrections accepted on the same pass:

- **FDR units.** `PMID:20844764`'s cut-off is FDR **≤ 0.01 %**, not 0.01 — its Methods define
  *"a SAM-calculated False Discovery Rate (FDR) less than or equal to 0.01%"*. This makes the donor
  annotation **stricter** than I had described, which strengthens the finding that the source is
  sound and the fault lies in the propagation.
- **Boilerplate.** The shared protein-binding and Compara blocks were ~200 and ~230 words repeated
  across 6 and 5 rows respectively, burying the per-row reasoning. Both are now compact pointers
  into §8 and §7b, with each row keeping only what is specific to it (the 17 records from
  `PMID:16230350`, the MI 0.67 targeted co-IP, `NbExp=5`, the YY1/INO80E ranking, the negative
  regulatory arm, the *Ino80*-null embryonic phenotype, the three conjoined claims).

## 14. Two parallel PRs, one new term, one duplicate — a gate that cannot fire per-PR

Found while re-running the gates for this follow-up. `cache/go/terms.csv` on `main` carried
**`GO:0031011` twice**:

| line | timestamp | added by |
|---|---|---|
| 3456 | `13:43:14` | ACTR5 #2291, in sorted position |
| 9070 | `13:40:43` | ACTR8 #2290, appended at EOF |

ARP5 and ARP8 are both INO80 subunits, so **both reviews needed the same new term for
`core_functions.in_complex`**. Each branch's duplicate gate
(`cut -d, -f1 cache/go/terms.csv | sort | uniq -d`) passed in isolation, because within either
branch the term appeared once — and they landed in *different positions*, so git auto-merged both
without a conflict. The duplicate exists only in the merge result.

This is a **new variant** of the known duplicate failure mode: the documented one is self-inflicted
within a single branch (hand-insert, then a later `just validate` re-appends because the appender is
blind to the inserted row). This one is *inter-branch*, and no per-PR check can see it — the
per-branch gate is not wrong, it is simply looking at the wrong artefact. The EOF duplicate is
removed here, keeping the sorted-position row, so the term appears exactly once.

**Two generalisations worth carrying:**
1. **Related genes reviewed in parallel are the high-risk case**, because they are precisely the
   ones that need the same new terms. Whenever a sibling PR is in flight, expect a `terms.csv`
   collision on whatever complex or activity term they share.
2. **The duplicate check belongs in CI on `main`, not only in each PR**, since only the merge
   result can exhibit the fault. A per-PR approximation is to re-run the check after
   `git merge origin/main` immediately before pushing — which this review did on three merges, but
   ACTR5 had not yet merged at that point, so the collision was still invisible. Filed as
   [issue #2294](https://github.com/ai4curation/ai-gene-review/issues/2294) rather than fixed here,
   because the workflow is shared CI config outside gene-review scope; the issue records that
   `main` already carries two pre-existing duplicates (`GO:0001675`, `GO:0009566`) which a bare
   "must be empty" assertion would trip over, and that the file must not be re-sorted.

## 15. The correction screen used the wrong instrument

Prompted by a cross-gene note that provider records cite corrected papers unflagged. Re-running
the screen properly found one item my round-1 method could not have found, and the **method** is
the transferable part.

**What round 1 did:** an `esearch` over the 20 cited PMIDs `AND (published erratum[pt] OR
corrected and republished article[pt] OR retracted publication[pt] OR expression of concern[pt])`.
Re-run now, that query returns **`Count: 0`**.

**Why it is wrong:** those publication types sit on the *erratum record*, not on the article being
corrected. Querying the cited set therefore asks "is any paper I cite itself an erratum?", which
is never the question. The right field is `CommentsCorrections/RefType` **on each cited article**,
read from `efetch&retmode=xml`, matching `ErratumIn`, `RetractionIn`, `ExpressionOfConcernIn`,
`CorrectedAndRepublishedIn`, `RepublishedIn`, `PartialRetractionIn`.

**What that found**, across all 20:

| PMID | `RefType` | target |
|---|---|---|
| `PMID:18922472` | `CommentIn` | commentary, not a correction |
| `PMID:26496610` | `CommentIn` | commentary, not a correction |
| **`PMID:40205054`** | **`ErratumIn`** | **`PMID:41039152`** |

`PMID:41039152` is a **Publisher Correction** (*Nature* 646:E16, Oct 2025) to "Multimodal cell maps
as a foundation for structural and functional genomics" — a publisher-side correction, **not** a
data- or figure-integrity notice, and the article is not retracted. The single claim this review
rests on it is an ACTR8–UCHL5 association independently established by `PMID:18922472` and by
`CPX-846` membership, so nothing changes. `is_invalid` is deliberately **not** set: that flag is
for retracted or replaced references, and using it here would misrepresent a typesetting-class
correction as an integrity problem.

**Rule to carry forward: screen corrections by reading `CommentsCorrections` on each cited
article, never by a publication-type query over the cited set.** The two `CommentIn` hits also
show why the `RefType` must be matched rather than merely counted — a commentary is not a
correction.

The correction record itself is now cached at `publications/PMID_41039152.md`, so its existence and
its `Erratum for` linkage to `PMID:40205054` are verifiable from the repository rather than resting
on a network call — a reviewer flagged that it was otherwise uncheckable offline, which was fair.
It is deliberately **not** added to the `references:` list: it is a correction notice, not a source
of any claim here, and listing it would imply this review draws evidence from it. The consequence,
also deliberate, is that `PMID:41039152` appears only in `review_notes` prose and so will not be
picked up by a programmatic sweep over `references` — the right place to catch it is the
`CommentsCorrections` scan described above, run against each cited article.

## 16. Two cross-gene claims checked, and one refuted

Both arrived as cross-gene guidance while this review was in flight. Recorded with outcomes
because a check whose result is not written down reads the same as a check never run.

**Confirmed, and it distinguishes ACTR8 from ACTR5.** `PMID:25016522`'s ComplexPortal-assigned
rows (`GO:0006275`, `GO:0060382`) are `ACCEPT`ed here rather than kept non-core, on the grounds
that the paper assayed ARP8 itself. Counting occurrences in the cached full text settles it:
**27 × "Arp8", 0 × "Arp5"/"ACTR5"**. The paper has a dedicated results section *"Effect of Arp8
depletion on recovery after replication stress"*, an esiRNA against human Arp8 (485–916,
`NM_022899.3`), its own qPCR primers, a 4-fold increase in discontinued forks by fibre labelling,
and the conclusion that *"depletion of the Arp8 subunit had the same consequences as Ino80
deficiency"*. So the same rows that are complex-level projections for ARP5 are gene-level evidence
for ARP8 — the asymmetry is real and is why the two reviews should **not** be harmonised on these
rows.

**Refuted.** A suggestion that ARP8 should take no nucleotide term without a structural check,
because it has "1 of 5 catalytic positions with no resolved nucleotide". The structural check was
done, and it is stronger than an alignment: human ARP8 has exactly **one** PDB entry, `4FO0`,
whose own deposited title is *"Human actin-related protein Arp8 in its ATP-bound state"* and whose
ligand list contains **ATP** and **MG** (the physiological Mg²⁺ counter-ion). Add the omit map
computed for the bound ATP, an ATPase measured on the human protein, and ATP occupancy gating DNA
binding through the annotated pocket residues, and `GO:0005524` is IDA-grade. The residue
observation is nonetheless correct and is already reflected: actin's catalytic Gln137 and sensor
His73 **are** substituted in ARP8 (Glu266, Arg187), which is precisely why `GO:0016887` ATP
hydrolysis activity is withheld. Binding and hydrolysis are separate claims and the review
separates them; "no nucleotide term at all" does not follow.

**Null result, recorded as one.** A concern that the seeded stub can silently collapse duplicate
`GO:0005515` rows, so annotations must be counted against the GOA TSV rather than the stub. Checked
per `(term, evidence, reference)` key: all **31** distinct GOA keys are present in the review, all
**6** `GO:0005515` rows survive with their own verdicts, and no review row lacks a GOA counterpart.
The only multiplicity difference is the `GO:0031011`/IDA/`PMID:21303910` row that GOA banks twice
(once ComplexPortal, once UniProt), documented at the top of these notes. **No collapse occurred
here** — but the check is what establishes that, not the absence of a symptom.

## 17. Core-vs-non-core rule applied consistently

`ACCEPT` where the supporting experiment manipulated or measured **ARP8/Actr8 itself**;
`KEEP_AS_NON_CORE` where the only evidence is a complex-level manipulation (INO80 knockdown,
CPX-846/CPX-878 projection) or a redundant general parent. Applied uniformly, this puts
`GO:0006275` and `GO:0060382` in the ACCEPT column (Arp8 was assayed:
[PMID:25016522 "we found that cells deficient for Ino80 and Arp8 had impaired replication restart after treatment with replication inhibitors and accumulated double-strand breaks"])
and `GO:0033044`, `GO:0045893`, `GO:0051726` in the KEEP_AS_NON_CORE column (INO80 RNAi only).
The rule is stated here so the pairing of a core parent (`GO:0006355`) with a non-core child
(`GO:0045893`) reads as deliberate rather than inconsistent.
