# ARC (human) — curation notes

Accession **Q7LC44** (`ARC_HUMAN`, 396 aa, Swiss-Prot entry version 156, 02-SEP-2026).
Verified against `ARC-uniprot.txt`: `ID   ARC_HUMAN               Reviewed;         396 AA.` and
`AC   Q7LC44; Q9UJW6; Q9Y469;`. HGNC:648, chromosome 8q24.3, gene id 23237. This is the
neuronal immediate-early gene *ARC*/*Arg3.1*, **not** *NOL3* (see next section).

## 0. No affinage deep-research record for this gene

The affinage prefetch was refused by the wrong-protein trust gate. `.affinage.log` reads:

```
⚠️  ARC: trust gate(s) tripped — record this in the review's reference_review, NOT in the deep-research file:
    - [BLOCKING] Accession mismatch: local review uses `Q7LC44` but the Affinage record's prefetch UniProt accession is `O60936`.
❌ refusing to write /Users/cjm/worktrees/wt-ARC/genes/human/ARC/ARC-deep-research-affinage.md
```

O60936 is **NOL3** (nucleolar protein 3, "apoptosis repressor with CARD domain"), whose
common alias is also *ARC*. The gate did its job: the record described a different protein,
and had it been written into the gene folder a later review would have ingested it. There is
therefore **no `ARC-deep-research-affinage.md`**, and no `file:human/ARC/ARC-deep-research-affinage.md`
reference in the review. Everything below is from UniProt, the GOA seed, PANTHER/PAINT,
QuickGO and primary literature that I retrieved and read myself.

The same symbol collision contaminates literature search. Every PubMed query below was
checked for apoptosis-repressor/NOL3/CARD hits and none were carried through; the papers
cited here are all about the activity-regulated cytoskeleton-associated protein.

Europe PMC REST was unavailable, so all searching used NCBI E-utilities
(`esearch`/`esummary`/`efetch`), plus QuickGO REST, UniProt REST, InterPro and RCSB.

## 1. What the protein is

Arc is the product of a **domesticated Ty3/gypsy retrotransposon Gag gene**. UniProt's DOMAIN
block states it directly: *"it contains large N- and C-terminal domains that form a bi-lobar
architecture similar to the capsid domain of human immunodeficiency virus (HIV) gag protein"*
and *"Tetrapod and fly Arc protein-coding genes originated independently from distinct lineages
of Ty3/gypsy retrotransposons."*

The structural claim is directly evidenced. Zhang et al. solved the two lobes
[PMID:25864631, "We report crystal structures of Arc subdomains that form a bi-lobar architecture
remarkably similar to the capsid domain of human immunodeficiency virus (HIV) gag protein."] and
named them: [PMID:25864631, "We term RnArc (207-278) Arc N-lobe, and RnArc (278-370) Arc C-lobe;
together they form the Arc Gag domain."]. The human entry carries eight PDB structures
(`6TN7`, `6TNQ`, `6TQ0`, `6YTU`, `7R1Z`, `7R23`, `8QF4`, `8QF5`), i.e. the Gag lobes and the
oligomerisation coil have been solved **on the human sequence**.

Functionally, Arc is two things at once:

1. **A capsid protein.** It self-assembles into virus-like particles that encapsidate RNA,
   is released from neurons in extracellular vesicles, and delivers its own mRNA into
   recipient neurons [PMID:29328916, "Endogenous Arc protein is released from neurons in
   extracellular vesicles that mediate the transfer of Arc mRNA into new target cells, where
   it can undergo activity-dependent translation."; "Purified Arc capsids are endocytosed and
   are able to transfer Arc mRNA into the cytoplasm of neurons."]. RNA is required for
   assembly [PMID:29328916, "Stripping RNA resulted in significantly fewer fully-formed
   capsids (Figure 2E), suggesting that Arc capsids require RNA for normal assembly."], and
   the RNA it takes is not sequence-selective [PMID:29328916, "suggesting that prArc capsids
   show little specificity for a particular mRNA, but encapsulate abundant RNA according to
   stoichiometry."]. Intact capsids are needed for uptake [PMID:29328916, "Strikingly,
   prArc(RNA−) was unable to be taken up but instead coated the outside of neurons (Figure S6),
   further suggesting that intact Arc capsids are required for uptake and transfer."].

2. **A postsynaptic effector of AMPA-receptor removal.** Arc binds endophilin 2/3 and dynamin 2
   and accelerates AMPAR endocytosis [PMID:17088211, "Here, we demonstrate that Arc/Arg3.1
   protein interacts with dynamin and specific isoforms of endophilin to enhance receptor
   endocytosis."], with the loss-of-function direction shown in the same paper [PMID:17088211,
   "Conversely, Arc KO neurons display increased levels of surface AMPARs and decreased rates
   of endocytosis."]. This is the mechanism behind homeostatic downscaling [PMID:17088213,
   "Overexpression of Arc blocks the upregulation of surface AMPARs and mEPSCs induced by
   chronic neuronal inactivity."; "Conversely, loss of Arc results in increased AMPAR function
   and abolishes homeostatic scaling of AMPARs."].

The bridge between the two is oligomerisation. The 7-residue motif in the N-terminal coil that
drives capsid formation is also required for Arc-facilitated endocytosis [PMID:33175445,
"The NT coil-coil interaction was also validated in live neurons using fluorescence lifetime
FRET imaging, and mutation of the oligomerization motif disrupted Arc-facilitated endocytosis."],
and CaMKII phosphorylation of the Gag N-lobe switches it off [PMID:31151856, "CaMKII
phosphorylates the N-lobe of the Arc GAG domain and disrupts an interaction surface essential
for high-order oligomerization."].

Other established roles: LTP maintenance and long-term memory consolidation [PMID:10818134,
"Our studies show that disruption of Arc protein expression impairs the maintenance phase of
LTP without affecting its induction and impairs consolidation of LTM for spatial water task
training without affecting task acquisition or short-term memory."]; LTD [PMID:17088210,
"In addition, long-term depression is significantly impaired."]; nuclear signalling
[PMID:23749147, "Arc localization to the nucleus promotes an activity-induced increase in the
expression of promyelocytic leukemia nuclear bodies, which decreases GluA1 (also called Gria1)
transcription and synaptic strength."]; developmental synapse elimination [PMID:23791196,
"We conclude that Arc mediates the final stage of CF synapse elimination downstream of P/Q-type
VDCCs by removing CF synapses from PC somata."]; and, outside neurons, skin dendritic-cell
migration [PMID:28783680, "Mechanistically, Arc/Arg3.1 was required for accelerated DC
migration during inflammation because it regulated actin dynamics through nonmuscle myosin II."].

Membrane attachment is by palmitoylation of a cysteine cluster [PMID:29264923, "We further show
that Arc can be palmitoylated on cysteines clustered in a motif, 94CLCRC98."], which puts a
substantial pool of synaptic Arc in rafts [PMID:29264923, "We confirmed that ~50% of
synaptosomal Arc that is not extracted by cold Triton X-100 associates with membrane rafts
(Figure 1C)."]. Targeting to *inactive* synapses is via CaMKIIβ [PMID:22579289, "Here, we show
targeting of Arc to inactive synapses via a high-affinity interaction with CaMKIIβ that is not
bound to calmodulin."]. Levels are limited by RNF216/Triad3A ubiquitination [PMID:24945773,
"Here, we demonstrate that the RING domain ubiquitin ligase Triad3A/RNF216 ubiquitinates Arc,
resulting in its rapid proteasomal degradation."], which UniProt maps to Lys-268/Lys-269
(`CROSSLNK 268`, `CROSSLNK 269`, `MUTAGEN 268 K->A: Complete loss of RNF216-mediated
ubiquitination; when associated by A-269.`).

## 2. The PANTHER family and the six IBAs — does fly dArc contaminate the tetrapod node?

This is the question the family composition raises, and the answer is a clean **no**, but the
reason is worth recording because the family *does* mix the two independently domesticated
lineages.

**The family does lump them.** `ARC-uniprot.txt` gives `DR   PANTHER; PTHR15962;` and
`PTHR15962:SF0`. The fetched family index
(`interpro/panther/PTHR15962/PTHR15962-entries.csv`) has five reviewed members, and one of
them is the fly:

| accession | organism | gene | length | subfamily |
|---|---|---|---|---|
| Q7LC44 | *Homo sapiens* | ARC | 396 | PTHR15962:SF0 |
| Q9WV31 | *Mus musculus* | Arc | 396 | PTHR15962:SF0 |
| Q63053 | *Rattus norvegicus* | Arc | 396 | PTHR15962:SF0 |
| Q8AWC3 | *Gallus gallus* | ARC | 404 | PTHR15962:SF0 |
| **Q7K1U0** | ***Drosophila melanogaster*** | **Arc1 (dArc1)** | **254** | **PTHR15962:SF0** |

dArc1 is not merely in the family, it is in the *same subfamily* as vertebrate Arc. PANTHER's
HMM is picking up the retained Gag fold, which is genuine homology — but homology to a shared
*retroelement* ancestor, not orthology of a cellular gene. The phylogenomics is explicit
[PMID:29328916, "Phylogenetically, tetrapod Arc genes cluster with Ty3/gypsy retrotransposons
from fish, while the fly Arc homologs group with a separate lineage of Ty3/gypsy
retrotransposons from insects (Figure 1A)."; "These results indicate that the tetrapod and fly
Arc genes originated independently from distinct lineages of Ty3/gypsy retrotransposons but
still share significant homology in the retroviral Gag domain."]. Zhang et al. reach the same
conclusion from the structures and add a functional caveat [PMID:25864631, "This suggests that
Arc domestication in insects followed a different functional path, and is consistent with
studies of Dme Arc that define a role in stress-induced behavior but not learning and memory
(Mattaliano et al., 2007)."].

**The PAINT node does not.** `just fetch-panther-paint PTHR15962` returns exactly one node with
six IBD assertions (`interpro/panther/PTHR15962/PTHR15962-paint.tsv`):

| node | GO | aspect | seeds (WITH/FROM of the IBD) | node taxon | date |
|---|---|---|---|---|---|
| PTN008562333 | GO:0005886 plasma membrane | C | MGI:MGI:88067 \| RGD:62037 \| UniProtKB:Q7LC44 | taxon:32523 | 20260529 |
| PTN008562333 | GO:0071598 neuronal ribonucleoprotein granule | C | MGI:MGI:88067 | taxon:32523 | 20250620 |
| PTN008562333 | GO:0170047 virus-like capsid | C | UniProtKB:Q7LC44 | taxon:32523 | 20250620 |
| PTN008562333 | GO:0005198 structural molecule activity | F | UniProtKB:Q7LC44 | taxon:32523 | 20250620 |
| PTN008562333 | GO:0048168 regulation of neuronal synaptic plasticity | P | RGD:62037 | taxon:32523 | 20170906 |
| PTN008562333 | GO:1900271 regulation of long-term synaptic potentiation | P | MGI:MGI:88067 \| RGD:62037 | taxon:32523 | 20170922 |

`taxon:32523` resolves (UniProt taxonomy REST) to **Tetrapoda (clade)**. The curator placed the
IBD at the tetrapod ancestor, not at the family root — which is exactly where the phylogenomics
puts the vertebrate domestication event [PMID:29328916, "Highly conserved, unique orthologs of
the murine Arc genes were identified throughout the tetrapods (mammals, birds, reptiles,
amphibians), but were conspicuously absent from all fish lineages and other deuterostomes
examined (94 species)."]. No IRD or IKR is needed anywhere in this family, and none exists —
the node placement alone quarantines the fly lineage. All six assertions are `negated=false`.

**Verified empirically in both directions.** Querying QuickGO for dArc1 (`Q7K1U0`) returns 19
annotations and **not one IBA**: dArc1's GO:0170047, GO:0110077, GO:0051028, GO:0048168,
GO:1903561 and GO:0003729 rows are all `IDA` from FlyBase/UniProt on PMID:29328915,
PMID:31907439 and PMID:37326306. Nothing descends to it from PTN008562333. Conversely, no
`FB:` identifier appears in any WITH/FROM of the six human IBA rows. The striking thing is that
dArc1 has experimentally earned nearly the *same term set* as human Arc — capsid, mRNA binding,
intercellular vesicle transport, mRNA transport, extracellular vesicle, regulation of neuronal
synaptic plasticity — entirely independently [PMID:29328915, "Here, we report that the
Drosophila Arc1 protein forms capsid-like structures that bind darc1 mRNA in neurons and is
loaded into extracellular vesicles that are transferred from motorneurons to muscles."]. Had
the IBD been placed at the family root the convergence would have been invisible, laundered
into inheritance. It was not.

So: the family mixes the lineages, the node does not, and every one of the six IBAs is
correctly scoped for human ARC. What remains to judge per-term is the strength and the
*aboutness* of each seed.

### Seed-by-seed

Donor identities resolved via UniProt REST (`xref:mgi-88067` → `Q9WV31` ARC_MOUSE, reviewed;
`xref:rgd-62037` → `Q63053` ARC_RAT, reviewed). Note that `MGI:MGI:88067` and `UniProtKB:Q9WV31`
are **the same entity** under two identifiers, as are `RGD:62037` and `UniProtKB:Q63053`; donor
counts below do not double-count them.

- **GO:0005198 structural molecule activity** and **GO:0170047 virus-like capsid** — single
  seed, `UniProtKB:Q7LC44`, i.e. **human ARC itself**. Tracing it in QuickGO: human ARC carries
  `IDA GO:0170047` and `IDA GO:0005198`, both assigned by FlyBase on PMID:33175445. This is the
  textbook self-referential IBA: the target's own experimental annotation is one of the
  descendant evidences the PAINT curator used to place the node, so it legitimately appears in
  the WITH/FROM of the IBA it later receives. It is *not* circular and the short donor list is
  not weakness — it says the function has experimental grounding on the target and is inherited
  rather than lineage-specific. (FlyBase as the assigning database for a human annotation is
  normal: FlyBase curates the Arc capsid literature and annotates the non-fly proteins the same
  papers characterise.)
- **GO:0005886 plasma membrane** — three gene-level donors (mouse Arc, rat Arc, human ARC). Rat
  Arc's support is SynGO IDA/IMP on PMID:17088211, and the EM is unambiguous [PMID:17088211,
  "Arc immuno-EM gold particles were present throughout the spine but were enriched over the
  postsynaptic density (PSD) where they appeared at, or very near, the plasma membrane"]. Mouse Arc's is `EXP` on PMID:22036569. Human ARC's own is the IDA on
  PMID:21834987 (see §4 for its weakness). Strong node, `is_active_in` is apt given the
  palmitoyl anchor.
- **GO:1900271 regulation of long-term synaptic potentiation** — two gene-level donors, mouse
  and rat Arc. Rat: `IMP PMID:10818134` (antisense knockdown, both LTP maintenance and LTM
  consolidation impaired). Mouse: `IMP PMID:31151856` (CaMKII-site knock-in). Two independent
  perturbation studies in two species; as solid as an IBA seed set gets.
- **GO:0048168 regulation of neuronal synaptic plasticity** — one gene-level donor, rat Arc,
  and its evidence is `IEP PMID:7857651`, the original Lyford discovery paper. IEP is an
  expression-pattern code and that paper's own conclusion is hedged [PMID:7857651, "Our
  observations suggest that Arc may play a role in activity-dependent plasticity of dendrites."].
  On its own that is thin support for an `involved_in` process annotation. It is however
  overwhelmingly corroborated by later Arc-specific perturbation work in both rodents
  (PMID:10818134, PMID:17088210, PMID:17088213, PMID:17898216, PMID:31151856), so the node
  placement and the term are right even though the recorded seed is the weakest of the six.
  I record this as `NO_FAILURE_CORE` with the seed weakness noted on the donor entry rather
  than inventing a failure.
- **GO:0071598 neuronal ribonucleoprotein granule** — one gene-level donor, mouse Arc, whose
  evidence is `IDA PMID:23936366`. **This seed is about the transcript, not the protein.** The
  paper is a conditional knockout of *TOG*/*Ckap5*; Arc appears in it as the A2RE reporter RNA
  [PMID:23936366, "ARC RNA was used as a reporter RNA for granule assembly and translation in
  control and TOG cKO neurons because it contains an A2RE sequence, is incorporated into granules
  and exhibits bursty translation in hippocampal neurons"]. Arc *protein* enters the analysis
  only as a nascent translation readout at granules [PMID:23936366, "Translational output per
  granule was analyzed by single molecule imaging of newly synthesized Venus-ARC protein
  molecules in the vicinity of each granule as described previously"] and as a steady-state
  immunostaining intensity [PMID:23936366, "ARC protein levels were measured in control and TOG
  cKO neurons (n = 8) after immunostaining with anti-ARC and a fluorescent secondary antibody."].
  There is no demonstration in that paper that the Arc protein is a constituent of a dendritic
  transport granule. Arc protein certainly forms an RNA-containing assembly, but the assembly
  that is demonstrated is the **virus-like capsid** (GO:0170047), which is a different structure
  from GO:0071598's "transports translationally silenced mRNAs to dendritic synapses". Kept,
  non-core, with `SOURCE_WEAK_OR_INFERRED` / `SOURCE_EVIDENCE_WEAK`. Not removed: the protein's
  RNA-granule association is plausible on independent grounds and MGI read the full text.

## 3. Donor tracing for the non-IBA propagated rows

Every ISS in this file is `GO_REF:0000024` from rat Arc (`Q63053`) or mouse Arc (`Q9WV31`);
every `GO_REF:0000107` IEA is Ensembl Compara from mouse Arc; every `GO_REF:0000044` IEA is a
UniProt SubCell keyword mapping; the one `GO_REF:0000002` is InterPro2GO from `IPR023263` (the
Arc family signature). QuickGO tracing of the donor's own experimental evidence:

| term | donor | donor's experimental evidence |
|---|---|---|
| GO:0003729 mRNA binding | Q63053 | IDA PMID:29328916 |
| GO:0007616 long-term memory | Q63053 / Q9WV31 | IMP PMID:10818134 / IMP PMID:31151856 |
| GO:0014069 postsynaptic density | Q63053 | SynGO IDA + IMP, EXP — all PMID:17088211 |
| GO:0031901 early endosome membrane | Q63053 | EXP PMID:17088211 |
| GO:0043197 dendritic spine | Q9WV31 | IDA PMID:31151856 |
| GO:0045121 membrane raft | Q9WV31 | IDA PMID:29264923 |
| GO:0045202 synapse | Q63053 | many; incl. IDA/IMP PMID:17088211, IDA/IMP PMID:17898216, EXP PMID:22579289 |
| GO:0045211 postsynaptic membrane | Q9WV31 | EXP PMID:22036569 |
| GO:0050804 modulation of chemical synaptic transmission | Q9WV31 | IMP PMID:31151856, IDA PMID:29264923 |
| GO:0051028 mRNA transport | Q63053 | IDA PMID:29328916 |
| GO:0051260 protein homooligomerization | Q63053 | IDA PMID:29328916 |
| GO:0061001 regulation of dendritic spine morphogenesis | Q63053 | IGI PMID:15537891 (ARUK-UCL) |
| GO:0071598 neuronal RNP granule | Q9WV31 | IDA PMID:23936366 (see §2) |
| GO:0098978 glutamatergic synapse | Q9WV31 | SynGO IDA + IMP PMID:17088211 |
| GO:0099149 reg. postsynaptic receptor internalization | Q9WV31 | SynGO IDA + IMP PMID:17088211 |
| GO:0110077 vesicle-mediated intercellular transport | Q63053 | IDA PMID:29328916 |
| GO:1900452 regulation of long-term synaptic depression | Q9WV31 | IDA PMID:29264923 |
| GO:1903561 extracellular vesicle | Q63053 | IDA PMID:29328916 |
| GO:0030425 dendrite | Q9WV31 | IDA PMID:23936366, IDA PMID:31151856 |

Two observations. First, this is an unusually clean propagation set: nearly every ISS traces to
a named, readable, Arc-specific experimental paper in rat or mouse, and Arc is 396 aa in human,
mouse and rat alike (PTHR15962 entries index) with no paralogue in mammals [PMID:21834987,
"Unlike the other PMM genes we analysed in detail, ARC (activity-regulated cytoskeleton-associated
protein) and ZRANB1 are each unique genes without closely related isoforms in mammals."], so
there is no wrong-paralogue risk. Second, **the human-evidence base is thin**: see §4.

## 4. How much of this is actually human evidence?

Only three primary papers contribute human-protein evidence, and each has a caveat:

- **PMID:33175445** (Eriksen 2021, FEBS J) — the source of all three human IDAs
  (GO:0170047, GO:0005198, GO:0003729). Cache is abstract-only (`full_text_available: false`).
  The abstract says "mammalian Arc" throughout and does not name a species for the capsid
  preparations. The human anchor is structural: UniProt cross-references
  `PDB; 6YTU; X-ray; 0.95 A; A/B=99-132` to Q7LC44, and RCSB confirms 6YTU's polymer entity is
  *Homo sapiens* "Activity-regulated cytoskeleton-associated protein" with the sequence
  `XQETIANLERWVKREMHVWREVFYRLERWADRLES`, which is the human 99–132 stretch. The oligomerisation
  coil in the paper's title was therefore solved on the human protein. FlyBase curators read the
  full text; per project policy the IDAs are accepted, with the species limitation noted.
- **PMID:21834987** (Bai 2011, BMC Biol) — the source of the human IDAs for GO:0005737 and
  GO:0005886, and (via UniProt) of the cytoskeleton SubCell keyword. The localisation data are
  GFP-ARC **overexpression in PC3 prostate carcinoma cells**, a cell type that does not express
  ARC natively [PMID:21834987, "GFP-ARC, FAM40A, FAM40B and FMNL3 proteins showed cytoplasmic
  localization with some enrichment on the plasma membrane compared to GFP alone (Figure 8B)."].
  The paper additionally carries a 2024 **author correction** specifically about its ARC panels
  [PMID:39390519, "The images for siARC were incorrect and were the same as the siZRANB images."]
  — that error is in Fig 6 (HeLa knockdown), not Fig 8 (the localisation figure the annotations
  rest on), and the authors state "The conclusions of the paper are unaffected", but it is a
  data-integrity event on this gene's panels and is recorded in `reference_review`.
  Note also that UniProt's `Cytoplasm, cytoskeleton {ECO:0000269|PubMed:21834987}` over-reads
  this paper: Fig 8B shows diffuse cytoplasmic plus plasma-membrane signal, not cytoskeletal
  localisation. The genuine cytoskeletal evidence is rodent [PMID:7857651, "the full-length
  protein, prepared by in vitro transcription/translation, coprecipitates with F-actin"].
- **PMID:32296183** (Luck 2020, HuRI) — four binary Y2H interactions. See §5.
- One further human-protein paper that GOA does not use: **PMID:25748042** (Myrum 2015) purified
  recombinant **human** Arc and showed self-association directly [PMID:25748042, "hArc appears to
  be pyramid-shaped as a monomer and is capable of reversible self-association, forming large
  soluble oligomers."]. It is cited in support of GO:0051260, which GOA carries only as ISS.

Everything else — AMPAR endocytosis, LTP/LTD, homeostatic scaling, memory, capsid-mediated RNA
transfer, nuclear PML signalling, cerebellar synapse elimination, dendritic-cell migration —
is rat or mouse. That is not a defect in the annotations (ISS/IBA is the honest code for it),
but it is the single most important thing to know about this gene's GO record.

## 5. The four `protein binding` IPI rows

All four are from the HuRI binary interactome [PMID:32296183] and are recorded in UniProt's
INTERACTION block with `NbExp=3` — three replicates within one study, not three studies:

```
Q7LC44; Q16527: CSRP2; NbExp=3; IntAct=EBI-750550, EBI-2959737;
Q7LC44; P25815: S100P; NbExp=3; IntAct=EBI-750550, EBI-743700;
Q7LC44; Q9H788: SH2D4A; NbExp=3; IntAct=EBI-750550, EBI-747035;
Q7LC44; O95935: TBX18; NbExp=3; IntAct=EBI-750550, EBI-12085364;
```

Partners resolved via UniProt REST: **Q16527** CSRP2 (cysteine and glycine-rich protein 2, a LIM
protein), **P25815** S100P, **Q9H788** SH2D4A (SH2 domain-containing protein 4A), **O95935**
TBX18 (T-box transcription factor 18). None is a neuronal protein, none appears in the Arc
mechanistic literature, and none has functional follow-up with Arc. Meanwhile the partners that
*do* have mechanism — endophilin 2/3 (SH3GL2/SH3GL3), dynamin 2, CaMKIIβ, PSEN1 — are recorded
in UniProt only as `By similarity` and have no human IPI row at all.

All four rows are `REMOVE`, following the protein-binding policy in
`.claude/skills/annotation-reviewer/SKILL.md` (added to main while this review was in progress):
`GO:0005515` is not an over-annotation, because its problem is absence of functional information
rather than a claim exceeding the evidence, so `MARK_AS_OVER_ANNOTATED` is the wrong action.
`MODIFY` is unavailable here — an all-by-all two-hybrid screen with no follow-up supports no
specific molecular function for these pairs, and inventing one from interaction evidence alone is
what the policy forbids. Removal says the term is uninformative, not that the interaction is
false; the interactions remain in IntAct and in UniProt's INTERACTION block. The informative MF
the record was actually missing is added separately as `GO:0030674` on the characterised
partners (see §7).

## 6. Per-row issues found

Actions across the 57 GOA rows plus 5 NEW rows (62 entries): 38 ACCEPT, 13 KEEP_AS_NON_CORE,
4 REMOVE, 1 MARK_AS_OVER_ANNOTATED, 1 MODIFY, 5 NEW. The four REMOVEs are all `GO:0005515`
protein binding and are removals on informativeness grounds under the skill's protein-binding
policy (§5), not because anything is contradicted: no substantive claim in this record is
refuted, and the weak rows are weak by provenance rather than wrong in substance. 48 rows carry a
`propagation_review` (all 6 IBAs, all 23 ISS including the 5 NEW rows, and all 19 IEAs — i.e.
every row with `supporting_entities`), enumerating 70 source entities in total. Root causes are
35 `NO_FAILURE_CORE`, 9 `NO_FAILURE_NON_CORE`, 3 `SOURCE_WEAK_OR_INFERRED` and 1
`TERM_SCOPING_PROBLEM`; the only failure modes used are `SOURCE_EVIDENCE_WEAK` (×3) and
`COMPARTMENT_OR_COMPLEX_MISMATCH` (×1). Every count in this paragraph is produced by
`.scratch/count_actions.py`, not asserted.

Specific calls worth flagging:

- **GO:0030665 clathrin-coated vesicle membrane (IEA, SubCell SL-0071) → MODIFY to GO:0005905
  clathrin-coated pit.** UniProt's `Cytoplasmic vesicle, clathrin-coated vesicle membrane
  {ECO:0000269|PubMed:24945773}` cites Mabb 2014, and what that paper shows is pit association
  [PMID:24945773, "Using TIRF microscopy, we found that a pool of Arc localizes to CCPs in COS7
  cells."; "The transient association of Arc with clathrin-coated pits (CCPs) is similar to the
  reported dynamics of its interacting partners, endophilin-3 and dynamin-2 (Perrais and
  Merrifield, 2005)."]. GO:0005905 is defined as the invagination *before* budding; GO:0030665
  is the membrane of the budded vesicle. The evidence supports the former.
- **GO:0060997 dendritic spine morphogenesis (TAS, PMID:15537891) → MARK_AS_OVER_ANNOTATED.**
  The cited statement is a hedged citation of someone else's overexpression result
  [PMID:15537891, "Arc protein is coupled to F-actin and linked functionally to spine morphology,
  and its chronic overexpression has been suggested to generate abnormal spine structure ( Kelly
  and Deadwyler, 2003 )."]. Arc acting *in* spine morphogenesis is not established; the
  regulation-of sibling GO:0061001 is already on the gene and carries the defensible claim.
- **GO:0001669 acrosomal vesicle (IEA, SubCell SL-0007)** — this is a mouse-only,
  single-study finding [PMID:12493697, "In isolated mature sperm, arc is present in the acrosomal
  region of the sperm head, the centriole region of the neck, and the principal piece of the
  tail."] that reaches human via UniProt's `{ECO:0000250|UniProtKB:Q9WV31}` and then through the
  SubCell→GO mapping, i.e. an IEA built on a by-similarity assertion. Kept as non-core with the
  chain recorded.
- **Reference projection test.** PMID:15537891 carries four ARUK-UCL TAS rows, which is the
  profile of a generic reference used across many genes. It is not: paginating QuickGO by
  `reference=PMID:15537891` returns 16 annotations over **4 distinct entities** — human ARC, rat
  Arc, and two ComplexPortal complexes. Gene-specific, so the TAS rows are judged on their own
  content rather than dismissed as a projection.

## 7. Gaps filled with NEW rows

- **GO:0005634 nucleus** — Arc is at least as abundant in the nucleus as at the synapse and has
  a defined NLS, nuclear retention domain and NES [PMID:23749147]. GOA has no nuclear CC at all
  for human ARC. Coded ISS on mouse Arc.
- **GO:0060292 long-term synaptic depression** — GOA carries only the regulation-of parent
  (GO:1900452). Arc is a required component of the process itself; Arc-null mice lose it
  [PMID:17088210]. Coded ISS on mouse Arc.
- **GO:0098883 synapse pruning** — developmental climbing-fibre elimination [PMID:23791196] has
  no counterpart anywhere in the human record. Coded ISS on mouse Arc.
- **GO:0036336 dendritic cell migration** — UniProt's FUNCTION block already asserts the immune
  role, but GO has nothing [PMID:28783680]. Coded ISS on mouse Arc; non-core.
- **GO:0030674 protein-macromolecule adaptor activity** — the molecular-function record for this
  gene is four bare `protein binding` Y2H rows plus mRNA binding and structural molecule
  activity, none of which says what Arc does at the synapse. Chowdhury et al. mapped the
  endophilin and dynamin interactions to distinct regions (UniProt: residues 89–100 and 195–214)
  and showed both are required for vesicle association [PMID:17088211, "Distinct Regions of Arc
  are Required for Interactions with Endophilin and Dynamin, and Both Interactions are Required
  for Association with Vesicles"], and Wu et al. state the recruitment outright. GO:0030674 is
  defined as bringing macromolecules into contact so they can act in a coordinated way, with
  "protein recruiting activity" among its synonyms. This is the term the four uninformative
  `protein binding` rows would ideally have become — except their partners are not the adaptor
  partners, so it is added rather than substituted. Coded ISS on rat Arc.

One deliberate near-miss on internal consistency is worth recording. The GO:0005886 IDA row
(Bai 2011, GFP-ARC in PC3 cells) was initially graded `KEEP_AS_NON_CORE` while the GO:0005886 IBA
row was `ACCEPT`; validation flags divergent actions on one term, and on reflection the validator
is right. The action records what should happen to the annotation, and plasma membrane is core for
Arc regardless of which row you look at. Both are now `ACCEPT`, with the evidence weakness of the
Bai row stated in its `reason` rather than encoded as a different action.

## 8. Ontology gap

GO has `GO:0170047 virus-like capsid` (CC) — whose definition names Arc explicitly: *"Fly and
tetrapod Arc (ancestrally-related to retrotransposon Gag) are examples of proteins that can
self-assemble into capsid-like structures which encapsulate Arc mRNA and mediate the
intercellular transmission of RNA."* — but the corresponding **process** and **molecular
function** terms are viral-only: `GO:0019069 viral capsid assembly` and `GO:0039660 structural
constituent of virion`. There is no non-viral counterpart for either (searched QuickGO
`ontology/go/search` for "virus-like capsid", "capsid assembly", "RNA encapsidation"). Arc's
assembly step is therefore forced onto `GO:0051260 protein homooligomerization` and its
capsid role onto the bare `GO:0005198 structural molecule activity`. Two terms are proposed in
`proposed_new_terms`.

`GO:0110077 vesicle-mediated intercellular transport` does exist and does cover the
Arc-EV-mediated mRNA transfer ("transported substances are moved in extracellular vesicles
between cells"), so no new term is needed for the intercellular-transfer half.

## 9. What the missing affinage record cost

Nothing that could be recovered by searching. Because the gate refused the NOL3 record there
was no lead list at all, so the entire reference set below was assembled by hand from: the
UniProt reference block; the GOA seed's four PMIDs; QuickGO donor tracing for every ISS/IEA/IBA
row (which is what surfaced PMID:23936366, PMID:29264923, PMID:22579289, PMID:17898216,
PMID:22036569 and PMID:31151856 — none of them findable from the gene symbol alone); the PAINT
slice; and targeted E-utilities searches on "Arc Arg3.1", "activity-regulated
cytoskeleton-associated protein", "Arc capsid", "Arc Gag", "Arc AMPA receptor endocytosis" and
"Arc acrosome sperm".

Worth noting for the campaign: **donor tracing, not keyword search, found the decisive papers
here.** The single seed behind GO:0071598 (PMID:23936366) is titled for *tumor overexpressed
gene* and would never surface in an Arc query; it is the only reason that row's weakness is
visible. Likewise PMID:29264923 (palmitoylation/rafts) is the sole evidence behind two separate
human rows and is reachable only through the mouse donor.
