# ccmC (Q8EK42, Shewanella oneidensis MR-1) — curation notes

## Identity

- UniProtKB **Q8EK42** (`Q8EK42_SHEON`), unreviewed (TrEMBL), 248 aa, protein
  existence `PE 3: Inferred from homology`.
- Gene symbol `ccmC`; UniProt and KEGG give the ordered locus as **SO_0261**
  (`DR KEGG; son:SO_0261`, `GN OrderedLocusNames=SO_0261`).
- Family: CcmC/CycZ/HelC (`CC SIMILARITY: Belongs to the CcmC/CycZ/HelC family.`),
  NCBIfam `TIGR01191 ccmC`, Pfam `PF27518 CcmC`,
  InterPro `IPR003557` (Cyt_c_biogenesis_CcmC) and `IPR045062`
  (Cyt_c_biogenesis_CcsA/CcmC), PANTHER `PTHR30071` (HEME EXPORTER PROTEIN C).
- Topology: six helical transmembrane segments annotated by UniRule RuleBase
  (`RU364092`), consistent with the experimentally established six-TMS topology of
  the CcmC family in *E. coli* [PMID:29518410 "The CcmC protein, comprised of six
  TMDs, is necessary for heme delivery to CcmE"].

## What CcmC does (System I cytochrome c biogenesis)

CcmC is one of the eight integral membrane proteins of System I (CcmA–H). It works
at step 1: heme is handed to the periplasmic heme chaperone CcmE, which CcmC binds
in a heme-dependent way.

- The conserved periplasmic tryptophan-rich **WWD domain** of CcmC is the heme
  binding site: alanine substitutions of its invariant tryptophans perturb the heme
  spectrum and abolish heme binding and function
  [PMID:20599545 "We conclude that the WWD domain and the conserved tryptophans that
  define this superfamily directly interact with heme, forming the specific heme
  binding site."].
- Heme is liganded by two external histidines of CcmC (His60/His184 in *E. coli*
  numbering); the double mutant binds no heme, co-purifies no CcmE and is
  non-functional [PMID:20599545 "These results are consistent with His60 and His184
  as axial ligands to the heme iron, at least one of which is required for stable
  binding of heme."].
- CcmC is the protein that attaches heme to apoCcmE
  [PMID:20599545 "CcmC is necessary to attach heme to apoCcmE; thus, it is sometimes
  referred to as the holoCcmE synthase."].
- Release of holoCcmE from CcmC requires the ATPase CcmA with CcmB, i.e. the
  CcmA2B1C1 complex; in the absence of CcmA or CcmB a stable CcmC:heme:CcmE dead-end
  complex accumulates [PMID:16824107 "In the absence of CcmA or CcmB, holo(haem)CcmE
  binds to CcmC in a stable dead-end complex, indicating high affinity binding of
  haem to CcmC."].
- Cysteine/heme crosslinking maps endogenous heme to the WWD domain and supports
  trafficking of heme by CcmC [PMID:29518410 "We conclude that CcmC trafficks heme
  via its WWD domain and propose the structural basis for stereochemical attachment
  of heme."].

### Is CcmC a heme *transmembrane transporter*?

The historical name "heme exporter protein C" and the InterPro2GO mapping to
`GO:0015232 heme transmembrane transporter activity` both assert an activity that
the primary literature still treats as unproven. The route by which heme reaches the
periplasmic WWD domain is explicitly open [PMID:20599545 "It is still unclear how
heme travels to the CcmC WWD domain to interact with CcmE."], and no heme-binding
site within the membrane-spanning helices was found, in contrast to the System II
protein CcsBA. The CcmABCD ABC complex hydrolyses ATP to *release holoCcmE*, not to
pump heme [PMID:16824107 "This ABC transporter is composed of the ABC subunit CcmA,
and two membrane proteins, CcmB and CcmC."; the abstract frames the ABC function as
"required for release of the periplasmic haem chaperone CcmE"]. The 2018 review of
the field still calls the step "putative heme transport through CcmC"
[PMID:29518410 "In System I, composed of eight integral membrane proteins (CcmA–H),
the first step in biogenesis involves putative heme transport through CcmC via the
CcmABCD complex"]. The review therefore keeps the heme-binding and heme-trafficking
claims and marks the transmembrane-transporter molecular function as an
over-annotation rather than removing it outright.

Note also that all of this mechanism is *E. coli* biochemistry. No biochemical study
of the *S. oneidensis* protein itself exists. Its assignment does not rest on family
membership alone, however: the characterised heme-binding site is present in the
MR-1 sequence itself. A pairwise global alignment of Q8EK42 against *E. coli*
P0ABM1, computed in `ccmC-bioinformatics/` and summarised in
`ccmC-bioinformatics/RESULTS.md`, is gap-free from the N-terminus through residue
184 at 58.8% identity and maps both axial histidines onto His60 and His184 *of
Q8EK42*, with the WWD motif intact as `WWVWD` at Q8EK42 122-126
[file:SHEON/ccmC/ccmC-bioinformatics/RESULTS.md "Both axial histidines are conserved
and fall at the **same positions in Q8EK42**, His60 and His184."]. These are
positions in the reviewed sequence, established by that alignment, not the *E. coli*
numbers carried across by assumption — they happen to coincide because the two
proteins align without gaps over that span. The mutant phenotype below corroborates
the assignment; the heme-attachment chemistry itself remains unassayed for this
protein.

## Shewanella-specific evidence

Marshall et al. 2006 used an MR-1 `CcmC−` mutant as the "no c-type cytochromes"
control in the U(VI)-reduction experiments
[PMID:16875436 "we evaluated a mutant lacking all functionally active c-type
cytochromes"; "we used an S. oneidensis MR-1 mutant lacking the ability to
covalently incorporate heme into nascent apocytochromes (CcmC"]. That mutant was
the only strain that **abolished** U(VI) reduction; single and double outer-membrane
cytochrome deletions only slowed it
[PMID:16875436 "none of the mutants tested abolished the ability to reduce U(VI) as
was seen with the CcmC"].

This is a maturation-pathway phenotype: the mutant lacks holo-cytochromes, so every
c-type-cytochrome-dependent activity in the cell fails. It establishes that CcmC is
**required for** c-type cytochrome maturation in MR-1, which is a genuine and
specific claim about this gene. It does **not** make CcmC a participant in metal
reduction: the electrons are moved by CymA, MtrA/MtrB/MtrC and OmcA, and CcmC does
none of that chemistry. No `NEW` metal-reduction or uranium-related process term was
proposed for this gene (CLAUDE.md participation test).

## Relation to the CMMMech record

`data/records/uraninite.yaml` grounds the node `ccmc_heme_exporter` on this
accession with:

> Cytochrome c biogenesis heme exporter CcmC (SO_0266) required for covalent heme
> attachment and maturation of multiheme c-type cytochromes including MtrC, OmcA,
> and CymA.

Assessment (CMMMech is read-only here; these are notes, not edits):

1. **"required for … maturation of multiheme c-type cytochromes"** — supported for
   MR-1 by the Marshall 2006 `CcmC−` control strain, which lacks all functionally
   active c-type cytochromes. Correct, and correctly scoped to a requirement rather
   than to uranium chemistry.
2. **"heme exporter"** — stronger than the evidence. The UniProt protein name is a
   RuleBase/ARBA-propagated legacy name, and the transport step itself is still
   described as putative in the primary literature (see above). "Heme-handling /
   heme-trafficking membrane protein that delivers heme to CcmE" would be the
   defensible phrasing.
3. **Locus number `SO_0266` appears to be wrong.** UniProt Q8EK42 gives
   `GN OrderedLocusNames=SO_0261` and `DR KEGG; son:SO_0261`. The CMMMech record
   (both the `protein_examples` entry and the causal-graph node label
   "CcmC cytochrome c maturation heme exporter (SO_0266)") says SO_0266. This is a
   CMMMech-side field error, not a GOA/UniProt/InterPro defect, so it is recorded
   here and in the PR report rather than in `review.source_defects`.
4. The record's `protein_examples` entry also lists `Pfam:PF27518` and the two
   InterPro ids, all of which match the current UniProt record.

## The catalase annotations

`GO:0004096 catalase activity` (IBA) and its logical consequence
`GO:0098869 cellular oxidant detoxification` (IEA, GO_REF:0000108) are propagated
onto Q8EK42 from PANTHER node `PTN001247822`. The PAINT IBD for that term was seeded
from a single donor, `UniProtKB:Q9I3N5` (`CCMC_PSEAE`, *Pseudomonas aeruginosa*
ccmC/PA1477):

```
PTHR30071	PTN001247822	GO:0004096	F	IBD	false	UniProtKB:Q9I3N5	taxon:	20260424
```

A QuickGO query on Q9I3N5 (2026-10-28) shows that donor annotation is
`GO:0004096 enables, IMP, PMID:16824107, assigned by PseudoCAP`, and that it comes
in a block of five further IMP rows from the same reference: `GO:0002049` pyoverdine
biosynthetic process, `GO:0009247` glycolipid biosynthetic process, `GO:0043107`
type IV pilus-dependent motility, `GO:0071977` and `GO:0071978` flagellum-dependent
swimming and swarming motility. That set is the phenotype profile of a strain with
no mature c-type cytochromes, recorded as if each phenotype were a function of
CcmC — and `catalase activity` is a molecular function, which a mutant phenotype
cannot establish at all. The cited paper is moreover a biochemical study of System I
CcmABC-mediated release of holoCcmE and does not report any of these
*P. aeruginosa* phenotypes
[PMID:16824107 "We have previously shown evidence that the system I pathway has a
higher affinity for haem than system II for cytochrome c biogenesis."].
The cached record for PMID:16824107 is abstract-only (`full_text_available: false`)
and its abstract names no organism at all — a case-insensitive search for
`Escherichia`/`coli` in `publications/PMID_16824107.md` returns nothing — so no
organism is attributed to that study anywhere in this review. An earlier draft said
it was an *E. coli* study; that was an inference the cached abstract does not
support, and it was removed from the review, from the two `source_defects`
explanations and from the `reference_review` notes. The `REMOVE` does not depend on
it: it rests on the two independent arguments that a mutant phenotype cannot
establish a molecular function and that no WWD-superfamily member dismutates H2O2.

Catalase (EC 1.11.1.6) is a soluble heme enzyme with a distinct fold; a six-TMS
integral membrane protein of the WWD heme-handling superfamily has no catalase
active site, and no CcmC homologue has ever been reported to dismutate hydrogen
peroxide. Both rows are therefore `REMOVE`, with `source_defects` filed against
GO_CENTRAL (the IBD row on `PTN001247822` — its *placement* is not what is faulted;
the request is that the row be deleted) and against the PseudoCAP donor row.

## Divergence from the sibling review, `genes/PSEPK/ccmC/ccmC-ai-review.yaml`

`Q88EX7` (*Pseudomonas putida* KT2440) is reviewed in this repository as `ccmC` too,
and it is a close comparator rather than a distant one: by its own UniProt
`DR PANTHER` lines it sits in `PTHR30071` and in subfamily `PTHR30071:SF1`, the same
family and subfamily as Q8EK42. Its GOA rows come from the same InterPro signatures,
`IPR003557` and `IPR045062`, by `GO_REF:0000002`. Six terms are shared between the two
reviews and four of them are called differently:

| Term | `genes/PSEPK/ccmC` | this review (SHEON) |
|------|--------------------|---------------------|
| GO:0020037 heme binding | ACCEPT | ACCEPT |
| GO:0005886 plasma membrane | ACCEPT | ACCEPT |
| GO:0015232 heme transmembrane transporter activity | REMOVE | MARK_AS_OVER_ANNOTATED |
| GO:0015886 heme transport | MARK_AS_OVER_ANNOTATED | ACCEPT |
| GO:0016020 membrane | MARK_AS_OVER_ANNOTATED | MODIFY → GO:0005886 |
| GO:0017004 cytochrome complex assembly | MODIFY → GO:1903607 | ACCEPT (both terms kept) |

Reconciling the two is a follow-up, not part of this review, and the PSEPK file
carries `status: DRAFT`, so this is a divergence against a draft rather than against
a settled review — which bears on how urgent reconciliation is, though not on whether
it is owed. Neither file should be read as having been checked against the other until
that work is done.

Where the divergence is weakest, and what I think is right:

- **`GO:0015232`** is the one that cannot simply be left standing. Both reviews argue
  from **family-level** biology and neither has an assay on its own protein: PSEPK says
  "literal transmembrane transporter activity is not established"; this review says the
  route to the WWD domain is explicitly open and that no heme site was found within the
  membrane-spanning helices [PMID:20599545]. That is one argument, and one argument
  cannot licence `REMOVE` in one file and `MARK_AS_OVER_ANNOTATED` in the other. I
  think `MARK_AS_OVER_ANNOTATED` is the right call and the PSEPK `REMOVE` is the one to
  change. "Not established" is not "refuted": the mechanism by which heme crosses to the
  WWD domain is an open question in the primary literature, CcmC is genuinely the protein
  at which heme appears on the periplasmic face, and `REMOVE` is reserved for functions
  that are contradicted or for electronic mappings that are demonstrably wrong. Nothing
  here contradicts heme crossing the membrane via CcmC; what is unsupported is the claim
  that CcmC is the transporter that does the moving.
- **`GO:0015886` heme transport** turns on whether holding heme at an external site and
  attaching it to apoCcmE counts as doing some of the work of heme transport. This review
  says yes and accepts it; PSEPK marks it over-annotated on the ground that the broad term
  "can imply unsupported membrane translocation". Both readings are defensible, and this
  one is at least internally consistent with marking the transporter MF over-annotated.
- **`GO:0016020` membrane** and **`GO:0017004`** are the smaller two. For `GO:0016020`,
  the repository rule is explicit that a correct-but-general non-organelle term is
  `MODIFY` to the supported descendant, which `GO:0005886` is and which both genes
  already carry; `MARK_AS_OVER_ANNOTATED` in PSEPK does not fit that rule. For
  `GO:0017004`, `GO:1903607` is not an ancestor of it, so keeping both says two different
  things, and replacing one with the other discards a claim.

## Suggested follow-up

- Biochemical confirmation that the MR-1 protein forms the CcmC:heme:CcmE complex
  (no *Shewanella* CcmC has been purified).
- Whether the *Shewanella* Ccm system, which matures an unusually large multiheme
  cytochrome complement (~40 c-type cytochromes), is rate-limiting for extracellular
  electron transfer.
