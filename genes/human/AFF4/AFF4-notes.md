# AFF4 (Q9UHB7) — review notes

Human AF4/FMR2 family member 4. HGNC:17869, 1163 aa, `AFF4_HUMAN`.
Synonyms: AF5q31, MCEF, HSPC092.

## 0. Identity, verified before anything else

`https://rest.uniprot.org/uniprotkb/Q9UHB7.json` returns `primaryAccession: Q9UHB7`,
`uniProtkbId: AFF4_HUMAN`, `entryType: UniProtKB reviewed (Swiss-Prot)`, `HGNC:17869`
with `GeneName: AFF4`, and **no `secondaryAccessions`**. A `gene_exact:AFF4 AND
organism_id:9606 AND reviewed:true` search returns exactly one entry, the same one.
So there is no merged-accession hazard on this gene — but every UniProt fetch in
`AFF4-bioinformatics/analyze_aff4_annotations.py` still asserts
`primaryAccession == the accession requested`, because a merged accession returns
HTTP 200 with a complete reviewed record for a *different* protein and nothing else
in the payload reveals it.

The worklist name (`human-no-IBA-simple.csv`) is stale, as expected: **AFF4 has five
IBA rows**, all from one PANTHER node. They were adjudicated, not skipped.

## 1. Row census (do this first)

```
wc -l < AFF4-goa.tsv                    # 44 -> 43 data rows
grep -c '^- term:' AFF4-ai-review.yaml  # 34 in the fetch-gene stub
```

43 GOA rows, all 43 distinct on (term, evidence, reference, with/from, qualifier);
the stub seeded **34**. The 9-row gap is entirely the known `GOAValidator.
seed_missing_annotations` collapse: the seeder keys on
`(GO ID, evidence, reference, negated, qualifier)` and omits WITH/FROM, so the
**15** `GO:0005515` IPI rows collapsed to **6** (one per reference). They have been
restored one-per-row so that every partner gets its own verdict, and it mattered:
of the five partners on the single reference `PMID:25416956`, four are unreplicated
screen hits and one (SIAH1) is independently confirmed by a purified-protein binding
assay and is the mechanistic basis of the CHOPS disease mutations.

Final `existing_annotations` count is **43 + 5 `NEW` proposals = 48**.

## 2. What AFF4 is

UniProt: `Key component of the super elongation complex (SEC)`; in the SEC it
`acts as a central scaffold that recruits other factors through direct interactions
with ELL proteins (ELL, ELL2 or ELL3) and the P-TEFb complex`
[file:human/AFF4/AFF4-uniprot.txt, lines 313-320]. The family assignment is
`SIMILARITY: Belongs to the AF4 family. {ECO:0000305}.`

The architecture is an intrinsically disordered N-terminal axis carrying short
interaction motifs, plus one folded C-terminal domain:

| region | what binds / does | structural evidence |
|---|---|---|
| 2-73 | cyclin T1 surface of P-TEFb; adjacent to HIV-1 Tat | `DR   PDB; 4IMY; X-ray; 2.94 A; G/H/I=2-73.` (AFF4+CDK9+CycT1); `4OGR`, `4OR5` (+Tat); `5L1Z`, `6CYT` (+TAR RNA) |
| ~301-351 ("ELLBow") | ELL2 C-terminal domain | `DR   PDB; 5JW9; X-ray; 2.00 A; A=301-351.` |
| 899-1163 (CHD / THD) | AFF4 homodimer, AFF1-AFF4 heterodimer; CDK9 substrate loop | `DR   PDB; 6KN5; X-ray; 2.20 A; A=899-1163.`, `DR   PDB; 6R80; X-ray; 2.20 A; A=899-1163.`, `6K7P` |

The mechanism, in the authors' words:

- **P-TEFb arm.** *"AFF4 meanders over the surface of the P-TEFb cyclin T1 (CycT1)
  subunit but makes no stable contacts with the CDK9 kinase subunit. Interface
  mutations reduced CycT1 binding and AFF4-dependent transcription."*
  [PMID:23471103]. Independently, a CycT1 point mutant that cannot bind Hexim1 or
  CDK9 still binds AFF4, so the AFF4 site on CycT1 is a distinct surface
  [PMID:24985467 "A single point mutation in cyclin T1 eliminates binding to Hexim1, Cdk9 and"].
- **ELL2 arm.** *"Here we report the 2.0-Å resolution crystal structure of the human
  ELL2 C-terminal domain bound to its 50-residue binding site on AFF4, the ELLBow."*
  [PMID:28134250]. Deletion mapping agrees: AFF4(Δ301-400) cannot bind ELL2
  [PMID:22483617].
- **The two arms are one bridge.** *"Through the bridging functions of Tat and AFF4,
  P-TEFb and ELL2 combine to form a bifunctional elongation complex that greatly
  activates HIV-1 transcription."* and, decisively for the host function,
  *"Without Tat, AFF4 can mediate the ELL2-P-TEFb interaction, albeit inefficiently."*
  [PMID:20471948]. That second sentence is the one that licenses an **adaptor**
  molecular function for AFF4 itself rather than only a complex-level one: AFF4
  brings CycT1 and ELL2 together without a viral protein present.
- **Dimerisation.** *"AFF4-CHD mediates the formation of an AFF4 homodimer or an
  AFF1-AFF4 heterodimer"* [PMID:31147444]; *"single mutations of either Phe1014 or
  Tyr1096 of AFF4 to"* alanine impair dimer formation [PMID:32128251]. Note the two
  groups name the **same** C-terminal region differently — CHD (Chen & Cramer) and
  THD (Tang et al.); UniProt/InterPro use CHD (`IPR043640`, Pfam `PF18876`). PDBe
  reports 2 AFF4 copies in the deposited assembly of `6R80` and `6K7P`, 1 in `6KN5`.
- **Regulation of the scaffold.** CDK9 phosphorylates a surface loop of AFF4-CHD,
  *"which triggers release of polymerase II from promoter-proximal pausing sites"*
  [PMID:31147444]; UniProt records Ser-549 dephosphorylation by PNUTS-PP1 as
  pause-release-promoting, citing PubMed:39603240 — a paper whose cached copy is
  **abstract-only and does not mention AFF4 in the abstract**, so that claim rests
  on the UniProt curation, not on anything I can read.
- **Output.** AFF4 knockdown *"decreased not only cellular level but also global
  chromatin occupancy of CTD serine 2 phosphorylated Pol II"* and *"AFF4 loss also
  increased promoter-proximal pause of Pol II on several hundred HS and thousands of
  non-HS genes"* [PMID:37609817]. AFF4 disruption *"results in slow elongation and
  early termination in a subset of AFF4-bound active genes"* [PMID:37528066].

## 3. The headline finding: AFF4's GO record has almost none of this

`AFF4-bioinformatics/RESULTS.md` §5b measures it. For each of 20 papers that
establish something about human AFF4, how many GO annotations exist anywhere in GOA
from that reference, and is AFF4 among the annotated entities?

**15 of 20 have produced no GO annotation anywhere in GOA; 18 of 20 have produced
none on AFF4.** The exceptions are `PMID:12065898` (nucleus + chromosome EXP) and
`PMID:22195968` (`GO:0008023` IDA).

Consequences visible in AFF4's own record (RESULTS.md §6):

- **AFF4 has zero experimental biological-process annotations.** Not one.
- Its only experimental molecular-function rows are **six bare `GO:0005515 protein
  binding` IPI** rows. There is no MF row describing what the protein does.
- `GO:0032783 super elongation complex` reaches AFF4 **only by IBA**, from a PANTHER
  node covering the whole family.

And the sharpest single instance: `PMID:20159561` is titled *"AFF4, a component of
the ELL/P-TEFb elongation complex and a shared subunit of MLL chimeras, can link
transcription elongation to leukemia"*, its abstract states *"SEC includes ELL,
P-TEFb, AFF4, and several other factors. AFF4 is required for SEC stability and
proper transcription by poised RNA polymerase II in metazoans."* — and the whole of
GOA carries **exactly one annotation** from it: `GO:0032783` IDA on **AFF1**.

Same shape for `PMID:39603240`: it yields `GO:0032968` IDA on the four PNUTS-PP1
components (PPP1CA, PPP1R10, TOX4, WDR82) and nothing on AFF4, although AFF4 Ser-549
is the substrate UniProt curates from it.

This is the inverse of the usual finding in this campaign. There is no
over-propagation to unwind here; there is a **coverage gap**, and it is the review's
main deliverable. Five `NEW` rows are proposed to close the part of it that current
GO terms can express.

## 4. WITH/FROM: every token resolved

RESULTS.md §2. All 24 distinct tokens resolved or classified; none dropped.

| token | resolves to |
|---|---|
| `PANTHER:PTN000829417` | a PANTHER tree node, not a protein |
| `FB:FBgn0041111` | `Q9VQI9` **lilli** (Drosophila), Swiss-Prot, 1673 aa — the single fly AF4 family member |
| `MGI:MGI:1100819` | `O88573` mouse **Aff1**, Swiss-Prot (10 candidates; the reviewed one chosen) |
| `MGI:MGI:1202294` | `O55112` mouse **Aff2**, Swiss-Prot |
| `MGI:MGI:106927` | `P51827` mouse **Aff3**, Swiss-Prot |
| `UniProtKB:P51825` | human **AFF1**, Swiss-Prot |
| `UniProtKB:Q9ESC8` | mouse **Aff4**, Swiss-Prot — the genuine orthologue |
| `UniProtKB:A0A8I6GGV9` | rat **Aff4**, **TrEMBL** (unreviewed) |
| `ARBA:ARBA00026330` · `InterPro:IPR007797` · `InterPro:IPR043640` · `UniProtKB-SubCell:SL-0191/SL-0468` · two `ensembl:` protein ids | rules / signatures / vocabulary terms, not proteins |

MGI tokens arrive as `MGI:MGI:1100819`; UniProt's `xref:mgi-` index needs the bare
number (a query containing the inner colon returns HTTP 400). Every lookup asked for
up to 10 hits, never `size=1`, and the number of candidates is printed — `MGI:1100819`
has ten, and picking one silently would have been a coin flip dressed as a fact.

**Observation worth stating plainly: not one of the five IBA rows names an AFF4
orthologue among its seeds.** The seeds are lilli (the fly family member, which is
equally the orthologue of all four human paralogs) plus mouse Aff1/Aff2/Aff3 and
human AFF1. Mouse Aff4 (`Q9ESC8`) *is* a co-recipient of the same node, and it does
hold experimental annotations — but it is not used as a seed for any of them. So the
family-level terms AFF4 receives are inferred from its paralogs, not from its
orthologue.

## 5. Donor evidence, per row (RESULTS.md §3)

Queried with `goUsage=descendants` so a donor whose experiment sits *below* the
propagated term is visible.

| row | donors with their own experimental evidence for the term or a descendant |
|---|---|
| `GO:0003712` coregulator | lilli `GO:0003712` **IMP** [PMID:11171404] — the donor's own experiment is at the exact term |
| `GO:0006354` elongation | human AFF1 `GO:0006354` **EXP** [PMID:22547686] |
| `GO:0006355` reg. transcription | lilli IMP; mouse Aff3 IDA+IMP [PMID:25162227]; human AFF1 IMP at the descendants `GO:0032786`/`GO:0032968` [PMID:41062835] |
| `GO:0032783` SEC | lilli `GO:0032783` **IPI** [PMID:22195968] |
| `GO:0050877` nervous system | lilli `GO:0007611` IMP [PMID:18310460]; mouse Aff2 `GO:0007611` IMP [PMID:11923441 "Impaired conditioned fear and enhanced long-term potentiation in Fmr2 knock-out mice"] |
| `GO:0000791` euchromatin (ISS **and** IEA) | mouse Aff4 `GO:0000791` **IDA** [PMID:22195968] |
| `GO:0034976` ER stress | rat Aff4 `GO:0034976` **IEP** [PMID:31466050] — and nothing else |

So "the donors only carry the same family-level inference" is **false on every row**
— it was tested, not assumed. Four rows are ACCEPTed on that basis. Two rows are not:

**`GO:0050877 nervous system process` → KEEP_AS_NON_CORE.** Both donor experiments
are at the descendant `GO:0007611 learning or memory` (verified: `GO:0007611`'s
ancestor closure contains `GO:0050877`), and both are on **paralogs** — mouse Aff2,
i.e. FMR2, the FRAXE intellectual-disability gene, and fly lilli. AFF4 has its own
reason to touch the nervous system (cognitive impairment is the "C" of CHOPS
syndrome), so the term is not wrong; but its support in GOA is paralog-derived and
it is not what AFF4 does. Note also that the *"missense mutation in the ALF homology
domain of Aff1 (Af4) ... reported in the robotic mouse, an ataxia mouse model"*
[PMID:25730767] belongs to **AFF1**, not AFF4 — I had to check this rather than
assume it, and it is exactly the sort of paralogue transfer this row invites.

**`GO:0034976 response to endoplasmic reticulum stress` → MARK_AS_OVER_ANNOTATED.**
The donor *is* the genuine rat orthologue, so this is not a paralog transfer. The
problem is one level down, in what the donor's own annotation rests on:

- its sole evidence is a single **IEP** (inferred from expression pattern) curated by
  RGD from `PMID:31466050`, *"Genipin attenuates mitochondrial-dependent apoptosis,
  endoplasmic reticulum stress, and inflammation via the PI3K/AKT pathway in acute
  lung injury"* — a drug-intervention study in a rat lung-injury model in which Aff4
  is not the subject;
- the projection test on that reference returns **1 annotation over 1 entity** in the
  whole of GOA, so it is one curation from one expression experiment, not a
  many-entity import;
- the donor entry is **TrEMBL**, so its protein name is an automatic label (its GO
  annotations are separately real; the two are different questions);
- a transcript changing abundance under ER stress does not establish that the gene
  product *participates in* the ER-stress response, and no human AFF4 study reports
  one.

`MARK_AS_OVER_ANNOTATED`, not `REMOVE`: AFF4's involvement is **unmeasured**, not
refuted, and the pipeline behaved as documented.

A related asymmetry, recorded as a question rather than a claim: Ensembl Compara
(`GO_REF:0000107`) projected the rat IEP row to human AFF4, but did **not** project
mouse Aff4's `GO:0007286 spermatid development` **IMP** [PMID:16024815 "Here, we show
that AF5q31 is essential for spermatogenesis."]. The mouse row carries
`acts_upstream_of_or_within` rather than `involved_in`, which is a plausible
technical reason, so this is a question for the pipeline's maintainers and not a
defect I am asserting.

## 6. The PANTHER node, and the reciprocal question

`PANTHER:PTN000829417` — **395 annotations over 79 recipient gene products**, and the
assignment is **uniform**: all five terms go to all 79. Recipients include all four
human paralogs (AFF1 `P51825`, AFF2 `P51816`, AFF3 `P51826`, AFF4 `Q9UHB7`), mouse
Aff1-4, and lilli.

The reciprocal question the campaign keeps rewarding — *which node's reach is exactly
my gene set, and what did it give them?* — has a clean answer here: **there is no such
node.** AFF4's `PTHR10528:SF15` subfamily carries no GOA annotations; the only node in
AFF4's WITH/FROM is the whole-family one. That is why every IBA row on AFF4 is
family-level and none is AFF4-specific, and it is a coverage observation rather than a
misplacement: the AADACL-style "right term, wrong node" defect is **absent here**, and
so is the ACTG2-style "a node reaching exactly my genes gave them something wrong".
Checked, negative, reported.

It does have one consequence worth flagging upstream. The node gives
`GO:0032783 super elongation complex` to **all 79** recipients, including AFF2 and
AFF3 — whose only experimental annotations are, respectively, G-quadruplex RNA binding
plus nuclear-speckle localisation, and DNA-binding transcription-factor activity
(RESULTS.md §6). Neither has been shown to be an SEC subunit. AFF4 and AFF1 have; the
term's own definition names *"an AFF family protein or distant relative"*, which is
why the propagation is defensible rather than plainly wrong — but the uniformity is
worth a PAINT question.

Because the node is genuinely heterogeneous in function, the **general** terms it
supplies are the correct LCA for it. So the four family-level rows are ACCEPTed as
correct-at-the-level-the-inference-supports, and the AFF4-specific specific terms are
added as `NEW` rows resting on AFF4's own human data, rather than by MODIFYing an IBA
to be more precise than its own inference. That is the AADACL4 lesson applied: before
proposing a specificity upgrade on a broad term, check whether the donor set is
heterogeneous.

## 7. `GO:0008023` IDA — the projection test came back NEGATIVE

`PMID:22195968` (`GO:0008023 transcription elongation factor complex`, IDA, assigned
by UniProt) is exactly the shape that produced the ACTR8 defect: **61 annotations over
26 entities**, with `GO:0008023` IDA on **16**. It is nevertheless sound, and the
discriminator is the second question, not the first:

1. all 16 `GO:0008023` recipients are genuine elongation-complex subunits — human
   AFF1, AFF4, CDK9, EAF1, EAF2, ELL, ELL2, ELL3, MLLT1, MLLT3 and the Drosophila
   SEC/LEC set (CycT, Eaf, Ell, Ice1, Ice2, lilli); there is no bystander in the list;
2. the paper's **functional** term does not spread. `GO:0042795 snRNA transcription by
   RNA polymerase II` IMP sits on **7** entities — ELL, ELL2, ELL3, mouse Ell, fly
   Ell, ICE1, fly Ice1 — i.e. the LEC subunits actually perturbed, and **not** on
   AFF4. That is correct biology: the paper's point is that *"LEC subunits are highly
   enriched at RNA Pol II-transcribed small nuclear RNA (snRNA) genes"* while SEC is
   the mRNA-gene complex, and UniProt's own note for AFF4 says it *associates to
   transcriptionally active chromatin but not at snRNA genes*.

So: complex membership spread with the biochemistry (right), the phenotype stayed with
the perturbed genes (right). `ACCEPT`. Reporting the null explicitly because a sibling
subunit review in this campaign found the opposite.

## 8. `GO:0005515`: nine partners, three different verdicts

RESULTS.md §7. AFF4 has **207 IntAct interaction records over 86 distinct partner
molecules**; GOA exports **9** as `GO:0005515` IPI rows across 15 GOA lines.
`NbExp` is not used anywhere in this review — it has been shown to count sub-methods
of one screen, replicates, and even domains of one protein. Distinct publications and
distinct (publication, method) pairs are counted instead.

**(a) Four partners are one Y2H screen counted three ways → MARK_AS_OVER_ANNOTATED.**
AP2B1, GOLGA2, TRAF2 and MTUS2 each have exactly 3 IntAct records, all from
`PMID:25416956` (HuRI), logged as `two hybrid array` + `two hybrid prey pooling
approach` + `validated two hybrid` — three sub-methods of a single experiment — at
MI-score 0.56, with no orthogonal assay and no mention in any AFF4 paper. UniProt
reports `NbExp=3` for each, which is that same screen. All four are cytoplasmic or
Golgi/membrane-trafficking proteins, against a protein UniProt localises to
nucleus/chromosome and whose EGFP fusion *"localized exclusively to the nucleus"*
[PMID:17389929]. Their IntAct record counts are 537 / 2335 / 1727 / 1476 against
AFF4's 207 — these are *record* counts, not partner counts, and they are reported as
such, but the hub character is plain. This follows the repo's established convention
(554 of 803 merged HuRI `GO:0005515` rows are `MARK_AS_OVER_ANNOTATED`).

**(b) SIAH1 is the same screen and must NOT be treated the same way → MODIFY.**
Its GOA support is the identical HuRI triple. But `PMID:22483617` demonstrates the
interaction with purified proteins: *"The addition of increasing amounts of AFF4 into
the binding reactions gradually decreased the levels of ELL2 bound to Siah1, and at
the same time increased the amounts of AFF4 retained on the Siah1 beads"*, and the
authors call it *"The direct Siah1-AFF4 interaction detected in these two reactions"*.
It is also the mechanism of the disease: the CHOPS missense variants *"create a
resistance to ubiquitination-dependent proteasomal degradation, resulting in excessive
amounts of mutant AFF4 protein accumulation"* [PMID:25730767]. SIAH1 is an
E3 ubiquitin-protein ligase, so `GO:0031625 ubiquitin protein ligase binding`
(*"Binding to a ubiquitin protein ligase enzyme, any of the E3 proteins"*) is an exact
and informative replacement. **Deciding per partner rather than per screen is what
separates this row from the four above.**

**(c) CCNT1, MLLT1, MLLT3 → MODIFY to `GO:0030674 protein-macromolecule adaptor
activity`.** These come from focused biochemistry, not screens: CCNT1 has 8 records
across 4 publications (MI 0.81), MLLT1 11 records across 3 (MI 0.76), MLLT3 4 across
2 — and the reference-projection test shows `PMID:20153263` annotates only **6
entities** and `PMID:21729782` only **17**, i.e. small directed studies. CLAUDE.md
directs `protein binding` to be replaced by an informative MF and names adapter
function as the example. Note this is a change of **kind**, not a specialisation:
`GO:0030674` sits under `GO:0060090 molecular adaptor activity` and its ancestor
closure does **not** contain `GO:0005515` (asserted in RESULTS.md §9). The claim it
makes is licensed by the evidence above: AFF4 engages CycT1 and ELL2 through separate,
separately-crystallised sites and can *"mediate the ELL2-P-TEFb interaction"* on its
own [PMID:20471948].

**(d) HIV-1 Tat → KEEP_AS_NON_CORE.** GOA's support is `PMID:22190034`, an AP-MS
survey that annotates **104 entities** — screen-scale. But three crystal structures
resolve AFF4 and Tat in the same complex (`4OGR`, `4OR5`, and with TAR `5L1Z`/`6CYT`),
and *"Tat and AFF4 fold on the surface of CycT1 and interact directly"*
[PMID:24843025]. So the interaction is real and far better supported than the row that
records it — a screen row rescued by structure, which is the opposite of (a). It is
kept, and kept **non-core**, because a host-pathogen interaction is not what the human
gene is for. The functional consequence is proposed separately as
`GO:0043923` (§10).

**(e) What is missing is more striking than what is there.** AFF4's `GO:0005515` set
contains **no ELL2 row** — despite a 2.0 Å co-crystal of the AFF4-ELL2 interface
(`5JW9`) and UniProt's `Interacts with ELL2; the interaction is direct`. Nor CDK9,
EAF1, EAF2, ELL, ELL3, AFF1, MED26 or HEXIM1, all of which are IntAct partners
(RESULTS.md §7 lists 77 such partners). The reason is mechanical and defensible:
those IntAct records are **spoke-expanded** from co-immunoprecipitation of a complex,
and GOA does not export spoke-expanded records as IPI — i.e. the pipeline is correctly
refusing to turn complex co-purification into pairwise binding. The gap is therefore
not "GOA is careless" but "the one paper that measured a *binary* AFF4-ELL2 interaction
and crystallised it (`PMID:28134250`) has never been curated", which is filable.

## 9. CHOPS syndrome: function is not phenotype, and sufficiency is not requirement

The disease mutations are Thr254Ala, Thr254Ser and Arg258Trp, in the ALF homology
domain [UniProt VARIANT features; PMID:25730767]. Their mechanism is *"a resistance to
ubiquitination-dependent proteasomal degradation, resulting in excessive amounts of
mutant AFF4 protein accumulation"*, and the transcriptome consequence is
*"opposite to that observed in AFF4 knock-down experiments"*.

That is a statement about **regulation of AFF4 abundance**, not about a new molecular
activity: a stabilising missense with a gain-of-function phenotype tells you AFF4 dose
is limiting for its normal job, and nothing about the protein acquiring a new function.
So no molecular-function term is derived from CHOPS anywhere in this review. What the
CHOPS data *do* support is that AFF4 binds chromatin with cohesin and RNAP2
(*"similar alterations of genome-wide binding of AFF4, cohesin and RNAP2"*), which
supports the chromosome/chromatin location rows.

Directional bookkeeping for the process claims, since GO's evidence codes do not
record it:

| claim | what the experiment was | shows |
|---|---|---|
| AFF4 promotes Pol II pause release / elongation | RNAi knockdown, ChIP-seq/PRO-seq [PMID:37609817]; AFF4 disruption [PMID:37528066] | **requirement** |
| AFF4 promotes adipogenesis via ATG5/ATG16L1 | knockdown *and* overexpression *and* adipose-specific `Aff4` knockout [PMID:36149892] | requirement **and** sufficiency |
| CHOPS transcriptional activation | stabilised protein, patient fibroblasts [PMID:25730767] | **sufficiency of excess dose**, not requirement |
| Aff4 in spermiogenesis | mouse null [PMID:16024815] | requirement, **in mouse** — a Sertoli-cell function, not annotated on the human gene |

## 10. Terms: what fits, what does not, and why

Every relation below was fetched and asserted (RESULTS.md §9); none is inferred from a
label.

- **`GO:0003711 transcription elongation factor activity` and `GO:0003712 transcription
  coregulator activity` are SIBLINGS** under `GO:0140110` — neither closure contains
  the other. So they are not redundant, and adding `GO:0003711` is not a granularity
  refinement of the existing IBA. `GO:0003711` (*"stimulates the elongation properties
  of the RNA polymerase during the elongation phase"*) is what SEC does, and AFF4
  contributes to it as the scaffold rather than enabling it alone — hence
  `contributes_to_molecular_function`, and `qualifier: contributes_to` on the NEW row.
  Human AFF1 already holds `GO:0003711` by IMP [PMID:41062835], so GO has accepted this
  term for an AFF scaffold; AFF4 not having it is an inconsistency, not a precedent
  question.
  `GO:0003712` is nevertheless kept: the donor lilli holds it by its own IMP, and
  AFF4/SEC is *"normally recruited to MLL-target chromatin to facilitate
  transcription"* [PMID:20153263], which is recruitment to a specific locus by a
  locus-specific factor as the definition requires.
- **`GO:0006368 transcription elongation by RNA polymerase II` is a descendant of
  `GO:0006354`** (asserted), and **`GO:0032968 positive regulation of transcription
  elongation by RNA polymerase II` is a descendant of `GO:0006355`** (asserted). Both
  are proposed as `NEW` rows on AFF4's own human evidence rather than as MODIFYs of the
  family-level IBAs, for the LCA reason in §6.
- **`GO:0030332 cyclin binding` cannot be used for cyclin T1.** Its definition
  specifies cyclins *"whose levels in a cell varies markedly during the cell cycle,
  rising steadily until mitosis, then falling abruptly to zero"*, which is not the
  transcriptional cyclin T1. Usage agrees and was measured with a positive control:
  **CDK9, HEXIM1 and BRD4 — the three canonical cyclin T1 binders — carry 0
  `GO:0030332` annotations each, while the cell-cycle kinase CDK2 carries 5**
  (RESULTS.md §10). So GO has no term for binding a transcriptional cyclin. Filed as a
  question; not forced.
- **`GO:0043923 host-mediated activation of viral transcription`** is proposed as a
  `NEW` BP row, and this is a *consistency* fix rather than a request for new
  precedent: of the 20 human annotations to that term, **CCNT1 and CDK9 both hold it by
  IDA** — AFF4's own P-TEFb partners, for the same HIV-1 Tat mechanism — as do SNW1,
  EP300, SP1 and SMARCA4/SMARCB1 (RESULTS.md §11). AFF4 holds it: **False**. Caveat
  recorded honestly: the CCNT1/CDK9 rows are `assignedBy: ComplexPortal` from
  `PMID:10866664`, i.e. themselves a complex-level projection; the non-projected
  precedents are SNW1 (IDA + IMP), EP300 (IDA) and the SWI/SNF pair (IMP).
- **`GO:0042803 protein homodimerization activity`** is proposed on the two crystal
  structures of the C-terminal domain plus the F1014A/Y1096A mutants.
- **`GO:0060090`/`GO:0030674`**: `GO:0030674 protein-macromolecule adaptor activity` is
  the child used, since the bridged entities are proteins.

## 11. Locations

HPA's own classification (`https://www.proteinatlas.org/api/search_download.php`) is
the cleanest way to grade the three `GO_REF:0000052` IDA rows, because it distinguishes
main from additional:

```
Subcellular main location:        Nucleoplasm
Subcellular additional location:  Nucleoli fibrillar center, Nuclear bodies
```

- `GO:0005654 nucleoplasm` — HPA **main** location, and independently the compartment
  where SEC acts. `ACCEPT`. The 11 Reactome `TAS` rows carry the same term from 11
  separate Pol II elongation reactions; they are 11 restatements of one fact (AFF4's
  membership of Reactome's elongation complex) and are ACCEPTed with that stated. The
  repo validator enforces one action per term outside `GO:0005515`, so all twelve share
  it — which is correct here rather than merely convenient.
- `GO:0016604 nuclear body` — HPA **additional**. Independently corroborated:
  *"Live cell imaging demonstrates that FUS co-localizes with AFF4 within nuclear
  punctuate"* structures [PMID:31238957]. Real, but not where the elongation function
  is executed → `KEEP_AS_NON_CORE`.
- `GO:0001650 fibrillar center` — HPA **additional**. The fibrillar centre is the
  Pol **I** rDNA transcription zone; SEC's substrate is Pol II, and no AFF4 role in
  rRNA transcription is reported. The observation stands (it is an IDA from curated
  immunofluorescence) but it is not core → `KEEP_AS_NON_CORE`. I am not calling it
  wrong: I cannot see the images, and per this project's rules an experimental
  annotation I cannot re-examine is not mine to delete.
- `GO:0000791 euchromatin` (ISS **and** IEA, both from mouse Aff4) — donor holds it by
  IDA from `PMID:22195968`; UniProt's note says AFF4 *associates to transcriptionally
  active chromatin but not at snRNA genes*. This is the functionally meaningful
  location. `ACCEPT` for both rows.
- `GO:0005634 nucleus` (EXP + IEA) and `GO:0005694 chromosome` (EXP + IEA) — `ACCEPT`.
  On the `GO:0005634` `GO_REF:0000120` row, note the ADISSP point: a combinatorial
  reference is only as independent as its tokens. Its three tokens are
  `ARBA:ARBA00026330`, `InterPro:IPR043640` and `UniProtKB-SubCell:SL-0191`, and
  fetching the rule (`https://rest.uniprot.org/arba/ARBA00026330`) shows that of its
  **1309** condition sets exactly **one** matches AFF4 — `InterPro id=IPR007797 AND
  InterPro id=IPR043640 AND taxon=Eukaryota → GO:0005634`. And `IPR043640` *separately*
  carries its own interpro2go mapping to `GO:0005634` (RESULTS.md §11b). So the ARBA
  token and the InterPro token are the **same witness reached by two routes**, while
  `SL-0191` derives from UniProt's
  `SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:12065898}.` line, i.e. the same
  experiment as the EXP row. Three tokens, two witnesses, and the row is redundant
  rather than independent. Correct, so ACCEPTed; the non-independence is recorded, not
  used to downgrade it.

## 12. Cross-checks run, including the ones that came back empty

- **Retraction / erratum / expression-of-concern**: 30 PMIDs checked by two routes
  (PublicationType *and* `CommentsCorrections/RefType`, because a Publisher Correction
  is invisible to a pubtype search and a corrigendum can carry a null PMID). **Zero
  flagged.** Three positive controls fired in the same call pattern — `32125225`
  (retracted), `36563143` (`ErratumIn` with a PMID), `17994018` (corrigendum with a
  **null** PMID) — so this zero is a measurement rather than a broken query.
- **Logical-opposite citation cross-product** (positive vs negative regulation of the
  same process sharing references): AFF4's GOA contains **no** positive/negative
  regulation pair at all, so the check is vacuous here. Stated rather than skipped.
- **Fold-to-activity propagation**: the lead does not apply, and this was measured
  rather than assumed (RESULTS.md §11b — a first draft of this note asserted that only
  one of the three signatures maps, which the download refuted). AFF4's InterPro
  content is `IPR007797` (AF4/FMR2), `IPR043640` (AF4/FMR2_CHD) and `IPR043639`
  (AF4_int) — all three **family-specific** signatures, not bare folds. Against the
  30122-line `interpro2go` release, `IPR007797` maps to `GO:0010468 regulation of gene
  expression` (BP), `IPR043640` maps to `GO:0005634 nucleus` (CC), and `IPR043639` maps
  to **nothing**. `any_molecular_function_mapped: False` — **no activity term is
  manufactured from any of the three**, and the unmapped signature is the control
  showing the pipeline is capable of restraint. Non-confirmation, reported as such.
- **Paralogue transfer in the AFF4 → AFF1 direction**: checked and **absent**. Nothing
  in AFF1's GOA record derives from an AFF4 reference. The traffic runs the other way
  (§3): `PMID:20159561`, an AFF4-titled paper, produced AFF1's `GO:0032783` IDA.
- **Sibling review comparison — run, and it found one divergence worth keeping.**
  `paint/AFF1` (PR #2348) appeared while this review was being finalised, so the
  identical-row comparison this campaign recommends was run against it.

  The two reviews were derived independently and **converge on everything that
  matters**, including the schema question this gene was flagged for: both chose
  `GO:0030674 protein-macromolecule adaptor activity` as the scaffold's own
  `molecular_function`, both put `GO:0003711 transcription elongation factor activity`
  in `contributes_to_molecular_function` rather than claiming it for the subunit, both
  use `GO:0032783` as `in_complex`, both propose `GO:0006368` + `GO:0032968` as the
  process terms, and both resolve `GO:0050877 nervous system process` to
  `KEEP_AS_NON_CORE` with `NO_FAILURE_NON_CORE`. On the five shared IBA rows they agree
  on four.

  **They differ on `GO:0006354 DNA-templated transcription elongation`**: AFF1 MODIFYs it
  to `GO:0006368`; this review ACCEPTs it and adds `GO:0006368` as a separate `NEW` row.
  The net GO content is the same; what differs is whether an IBA may be made more precise
  than the inference behind it.

  Rather than converge by fiat, I checked whether the two genes differ in a way that
  justifies differing verdicts, and they do. **The WITH/FROM field is byte-identical on
  both genes — `PANTHER:PTN000829417|UniProtKB:P51825` — and it is SELF-REFERENTIAL on
  AFF1 and PARALOGUE-DERIVED on AFF4.** Verified directly:

  ```
  AFF4 GO:0006354 IBA withFrom=['PANTHER:PTN000829417', 'UniProtKB:P51825']  self-referential? NO
  AFF1 GO:0006354 IBA withFrom=['PANTHER:PTN000829417', 'UniProtKB:P51825']  self-referential? YES
  ```

  So on AFF1 the row records a PAINT curator's judgement about AFF1 itself, and refining
  it stays inside that judgement; on AFF4 the only protein named is a paralogue, and
  refining it asserts more about AFF4 than the inference carries. That is a real,
  checkable, gene-specific distinction rather than an inconsistency — and it generalises:
  **a byte-identical WITH/FROM field can be self-referential on one recipient of a node
  and paralogue-derived on another, and that changes how much precision the row can
  carry.** Worth adding to the campaign's WITH/FROM checklist.

  **The AFF1 review also makes an argument against my position that I had not
  considered, and it is a good one**: the same node hands `GO:0032783` to all 79
  recipients, and that term's definition is explicitly about RNA polymerase II, so the
  node is not in fact behaving as though its clade were polymerase-agnostic — which
  weakens my "heterogeneous node, so the general term is the LCA" framing. I have
  recorded it in the row's `reason` rather than suppressing it, and declined to lean on
  it, because this review separately questions whether that complex term should reach
  AFF2 and AFF3 at all and it would be circular to rest on an assignment it doubts.
  Flagged for the coordinator to adjudicate; a reviewer who prefers MODIFY here would be
  taking a defensible position.

  `AFF2` and `AFF3` still have no review on `main`, so no comparison was possible for
  them.

## 13. What I would ask, and what the affinage record missed

The affinage report (`AFF4-deep-research-affinage.md`) has `gates_passed: True` and 26
numeric PMIDs. As the campaign's calibration predicts, a passing gate is a floor on
precision and says nothing about recall — and here it is mostly *good* recall, because
AFF4's famous literature and its annotation-relevant literature are the same papers.
Three notes:

- It returned **no PMID** for its MeCP2/SEC finding (a bioRxiv preprint), correctly
  marked `—`. Nothing in this review rests on it.
- Its dates are unreliable: the `PMID:32139123` row is labelled **2027** for a 2020
  BBRC paper. Dates were re-derived from PubMed, not taken from the table.
- It reports *"increases the affinity of Tat-P-TEFb for TAR RNA 30-fold"*
  [PMID:24843025] and *"enhances TAR binding to the SEC 50-fold"* [PMID:27731797] in
  one sentence. Both figures are in their own abstracts and describe the same
  phenomenon measured by two groups; they are **not** two arms of one comparison, and
  neither is used numerically in this review. Recording the check because the ADPRS
  lesson is that a provider's *arithmetic* contaminates even when none of its text is
  quoted.
- Papers it did not return that this review uses: `PMID:22483617` (the direct
  Siah1-AFF4 binding that decides the SIAH1 row), `PMID:22195968`, `PMID:22547686`,
  `PMID:41062835`, `PMID:11923441`, `PMID:31466050`. The last two were found only by
  chasing donor evidence out of the WITH/FROM column, which no literature search would
  have surfaced.

Questions filed in the review: the GOA/GO-Central coverage gap (§3); the absent
AFF4-ELL2 binding row (§8e); the uniform `GO:0032783` assignment to AFF2/AFF3 (§6); the
missing transcriptional-cyclin binding term (§10); and the Compara qualifier asymmetry
(§5).

## 14. What the committed gates caught, including in themselves

`AFF4-bioinformatics/audit_aff4_review.py` runs eight invariant checks over the
**emitted** review YAML (not over any generator), with twelve break-tests. Recording
what it found, because a guard's value is measured by the defects it catches and not
by its passing:

1. **Two real omissions in the review, both in the direction that would otherwise go
   unwritten.** Check G has two halves: every `core_functions` term must be backed by
   an annotation row, *and* every ACCEPT or NEW row's term must either appear in
   `core_functions` or have its absence explained. The second half fired twice — on
   `GO:0043923` (a NEW row I had deliberately kept out of `core_functions` as a
   host-pathogen process, without saying so) and then on `GO:0006354` (an ACCEPT row
   that is the verified ancestor of a term `core_functions` does record, again without
   saying so). Neither was found by re-reading.
2. **A defect in the guard itself, of the exact class this campaign catalogues.** My
   first version of that check matched a **whitelist of accepted phrasings**
   ("ancestor", "not restated", …) — a literal-phrase pin, which the first legitimate
   rewording defeats. It rejected "deliberately absent from core_functions" as
   unexplained. The fix was structural, not another phrase: key the check on the
   literal **field name** `core_functions`, which is a stable token and does not get
   reworded, and **state the limitation in the file** — it verifies that the reason
   *addresses* the omission, not that the argument is sound. Re-keying it immediately
   exposed defect (1)'s second instance, which the phrase whitelist had been passing.
3. **A break-test fixture that would not have exercised its own check.** The
   CC-continuation test asserts the mutated quote is whitespace-normalised-*present*
   before asserting it is not on one physical line; that assertion failed, because my
   first fixture omitted the `CC` marker the flat file interposes and so would have
   tripped the *verbatim* check instead. A mutation coarser than the distinction it
   certifies proves only that the checker reads its input.
4. **An unenumerated-slot guard.** Removing `locations` from the swept slot list makes
   check G fail loudly rather than silently stop covering it — which matters because
   the hedge sweep as usually framed is scoped to molecular-function slots, and
   `locations` is where a "not core" judgement is most easily contradicted.

Both scripts also refuse vacuous passes: `uniprot_quote_check` raises on an empty
quote list, `correction_status` raises with no positive controls, and every check that
iterates raises rather than returning success when it iterated over nothing.

Also worth noting what the analysis script's own assertions rejected: a first draft of
§12 of these notes claimed only one of AFF4's three InterPro signatures carries an
interpro2go mapping. Downloading the mapping file refuted it — `IPR043640` maps to
`GO:0005634` as well. The conclusion (no molecular function is manufactured from any
signature) survived; the stated fact did not, and would have shipped.

## 15. Reproducing this

```
cd genes/human/AFF4/AFF4-bioinformatics
uv run --with requests python analyze_aff4_annotations.py --self-test   # 8 break-tests
uv run --with requests python analyze_aff4_annotations.py               # rewrites RESULTS.md + results.json
uv run --with requests python audit_aff4_review.py                      # gates over the emitted YAML
uv run --with requests python audit_aff4_review.py --self-test          # break-tests for those gates
```

`RESULTS.md` is generated; do not hand-edit it, and re-run `checkquotes.py` after any
regeneration, because a `file:` quote into a generated artifact is a two-way dependency.
