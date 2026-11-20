# actA (Q93P59, *Myxococcus xanthus*) — curation notes

**Provenance note.** No deep-research provider API keys exist in this container, so
`just deep-research*` was not run and no `-deep-research-<provider>.md` file exists for
this gene. All literature below was gathered directly: the cached publications, Europe
PMC / PubMed searches, UniProt REST, QuickGO, and the sequence in
`actA-uniprot.txt`. Three papers were newly cached for this review with
`just fetch-pmid` (PMID:11807078, PMID:17189369, PMID:26369581).

## 1. What the gene is

Q93P59 is an unreviewed (TrEMBL) entry, 342 aa, named "Response regulator ActA",
derived from GenBank AF350253 (`AAK38649.1`), the act-operon sequence published with
PMID:11359579. The entry records the source strain explicitly:
`RC   STRAIN=DK1622 {ECO:0000313|EMBL:AAK38649.1}` [file:MYXXA/actA/actA-uniprot.txt].

Domain architecture (both from PROSITE profiles, `ECO:0000259`):

- 41-157 "Response regulatory" (PS50110), with a predicted phospho-accepting
  Asp at residue 90 (`MOD_RES 90 /note="4-aspartylphosphate"`).
- 207-342 "GGDEF" (PS50887), plus CDD cd01949, Pfam PF00990, NCBIfam TIGR00254.

So ActA is, by architecture, a REC+GGDEF protein: a response-regulator receiver
domain fused to a diguanylate-cyclase-like output domain. The 2016 review states
exactly this: "ActA is a putative response regulator that is predicted to have a
GGDEF-type effector domain, which is found in diguanylate cyclase enzymes"
[PMID:26369581].

**Own sequence check (not from any publication).** The canonical GGDEF A-site motif
GG(D/E)EF is **absent** from the Q93P59 sequence — neither `GGDEF`, `GGEEF`, `GGDQF`,
`SGDEF` nor `AGDEF` occurs anywhere in the 342 residues. Within the PROSITE-delimited
GGDEF domain the closest match at the expected A-site position is `GDCQF`
(…AVARV**GDCQF**ALMLPG…). The receiver-domain Asp90 is present. This is consistent with
a degenerate, probably non-catalytic GGDEF domain acting as a protein-protein /
regulatory module rather than as a diguanylate cyclase, and it is why no diguanylate
cyclase activity (GO:0052621) is proposed in this review. No c-di-GMP measurement on
ActA exists in the literature, so this stays an observation, not an annotation.

Identifier note: `actA` is `MXAN_3213` in the DK1622 reference genome, which the
promoter paper states directly — "actA (MXAN3213)" and "the actA (MXAN3213)
transcription start" [PMID:17189369].

## 2. The act operon and the C-signal circuit

*M. xanthus* starvation triggers fruiting-body development; the C-signal, a
cell-surface-associated morphogen encoded by `csgA`, coordinates aggregation,
rippling and myxospore differentiation. "The C-signal is a morphogen that controls
the assembly of fruiting bodies and the differentiation of myxospores. Production of
this signal, which is encoded by the csgA gene, is regulated by the act operon of four
genes that are co-transcribed from the same start site." [PMID:11359579]

The operon was later extended to five genes: "All act genes, actA to actE , are
expressed together and constitute an operon, because an in-frame deletion of actB
decreased expression of actA and actE to the same extent." [PMID:17189369]

Division of labour inside the operon, from the defining study [PMID:11359579]:

- **actA, actB** set the *maximum level* of C-signal: "The act A and act B genes
  regulate the maximum level of the C-signal, which never rises above one-quarter of
  the maximum wild-type level of CsgA protein in null mutants of either gene."
- **actA, actB** phenotype: "The act A and act B mutants have the same developmental
  phenotype: both aggregate, neither sporulates, both prolong rippling."
- **actC, actD** set the *timing*, not the level: an actC null raises CsgA production
  15 h early, an actD null 6 h late.
- Pathway logic: "the two gene products are part of the same signal transduction
  pathway. That pathway responds to C-signal and also regulates the production of CsgA
  protein, thus creating a positive feedback loop." [PMID:11359579]
- ActA's assignment is by sequence: "By sequence homology, act A encodes a response
  regulator, and act B encodes a sigma-54 activator protein of the NTRC class."
  [PMID:11359579]

This is the key asymmetry for annotation: actA and actB are *level* genes, actC and
actD are *timing* genes. The brief's expectation that actA has an effect on csgA
expression distinct from the downstream act genes is confirmed — but the distinction is
level (actA/actB) versus timing (actC/actD), not a difference in whether csgA is
affected at all.

### Follow-up work by the same lab

The 2002 companion paper restates the 2001 result as transcriptional: "Earlier work has
shown that transcription of the csgA gene, which encodes the C-signal, is directed by
four genes of the act operon." [PMID:11807078] It then shows the act mutations do
**not** touch the early, C-signal-independent program — "Neither the time of first
expression nor the rate of expression increase was changed in actA, actB, actC, or actD
mutant strains" — while "The actA and actB null mutations substantially decreased the
expression of all these reporters" (the four aggregation/sporulation reporters expressed
from 6 h) [PMID:11807078]. So the actA defect is specific to the late,
C-signal-dependent half of development.

The 2007 promoter paper [PMID:17189369] adds, with full text available:

- Strain: the reporter "integrated by homologous recombination into the act region of
  the chromosome of DK1622, the strain which provided a standard genetic background for
  this work".
- ActA's place in the circuit: "actA encodes a response regulator that works with actB".
- ActA is needed for the operon's own transcription: "act reporter expression is
  substantially and equally depressed in the Δ actA and Δ actB mutants" (the reporter
  pTG027 is explicitly a *transcriptional* actA-lacZ fusion).
- Mechanistic model: "ActA and ActB appear to be part of a signal transduction pathway
  that receives input from C signal on the transmitting cell", with output a
  transcriptionally active ActB; "p17 CsgA on the transmitting cell, via a (currently
  unknown) receptor on the receiving cell, would signal ActA, which, in turn, would
  activate ActB, presumably to ActB∼P."
- And on csgA: "The final level of csgA expression is set by actA and actB"; "the act
  operon activates transcription of the csgA gene".

### An independent, partly dissenting source

The Garza-lab review of *M. xanthus* two-component systems [PMID:26369581] is a
later, independent assessment. It endorses the actA phenotype — "Mutational analyses
indicate that actA and actB are required for sporulation inside nascent fruiting bodies
but not for the formation of aggregates of cells" — and is blunt about how little else
is established: "Little else is known about the function of actA ; however, actB
function has been studied in some detail."

Critically, it disputes the *mechanism*, not the phenotype: having failed to find an
ActB binding site or a sigma-54 promoter consensus upstream of csgA, "Thus, it seems
unlikely that ActB directly regulates developmental expression of csgA ." The only
direct ActB targets identified are the act operon itself and MXAN4899. So the
act -> csgA link is real as a dependency but probably indirect. This matters for term
choice: it argues against giving ActA a transcription- or gene-expression-regulation
term (see section 4).

## 3. CACAO / provenance audit (screen 2: cross-isolate transfer)

PMID:11359579 is cited by CACAO rows on three gene products across two NCBI taxon ids,
which is what put this gene in batch 3:

| accession | symbol | taxon | source EMBL | CACAO rows |
|---|---|---|---|---|
| Q93P59 | actA | 34 (species) | AF350253 | GO:0009966, GO:0043937 |
| Q93P57 | actC | 34 (species) | AF350253 | GO:0009966, GO:0031155, GO:0043937 |
| Q1D7F8 | actB | 246197 (DK1622) | CP000113 (MXAN_3214) | GO:0042594, GO:0043937 |

The predicted shape (one experiment annotated to entries filed under sibling taxon ids
without re-grounding) is **absent**:

1. The two taxon ids denote the same organism *and the same strain*. Q93P59's own
   record says `RC   STRAIN=DK1622`, and the AF350253 sequence it comes from was
   published in PMID:11359579 itself. DK1622 is the standard laboratory strain and the
   reference genome; the 2007 companion from the same lab confirms DK1622 "provided a
   standard genetic background for this work" [PMID:17189369].
2. The loci are the same. Q93P59 (342 aa, AF350253) and Q1D7F9 (342 aa, CP000113,
   `actA MXAN_3213`) are two UniProt entries for one gene, and PMID:17189369 states
   that the AF350253 act sequence "was verified in the complete sequence of the
   M. xanthus genome, GenBank accession number CP000113".
3. The paper assays actA itself, by name, with a dedicated null mutant, and the result
   is in the abstract. There is no operon-level inference being attributed to a single
   gene.

**What is there instead: a redundant-entry split.** UniProt holds two unmerged
unreviewed entries per act locus — the AF350253 submission set (Q93P59 actA, Q93P58
actB, Q93P57 actC; taxon 34) and the DK1622 genome set (Q1D7F9 actA/MXAN_3213,
Q1D7F8 actB/MXAN_3214, Q1D7F7 MXAN_3215; taxon 246197). The CACAO rows from one paper
landed on *different members of these redundant pairs*: actA and actC on the submission
entries, actB on the genome entry. Checked by UniProt REST on 2026-11-01, the
consequences are:

- `Q93P59` (actA, submission entry): GO:0000160 IEA + the two CACAO IMP rows.
- `Q1D7F9` (actA, DK1622 reference-proteome entry, identical length): GO:0000160 IEA
  **only** — the experimental annotations are invisible from the reference proteome.
- `Q93P58` (actB, submission entry): four IEA rows, no CACAO.
- `Q1D7F8` (actB, DK1622 entry): the CACAO rows.

So the taxon spread the screen detected is real but its cause is UniProt entry
redundancy plus inconsistent entry choice by the annotators, not a transfer of
experiments between isolates. The annotation is on the right organism, right strain and
right protein; it is simply on only one of two accessions that stand for that protein.

**GONUTS.** Re-checked 2026-11-01: `gowiki.tamu.edu` now returns **HTTP 410 Gone** with
the page "GONUTS, the GO wiki, has been retired — The GO wiki that was at
gowiki.tamu.edu is no longer online." This is a permanent retirement, not the temporary
"performing upgrades" message seen in batches 1-2. The Wayback Machine has no snapshot
of `gowiki.tamu.edu/wiki/index.php/MYXXA:actA`, `.../MYXXA:ActA` or `.../Q93P59`. The
students' recorded evidence text for these two rows is therefore not recoverable, and
should be treated as permanently unavailable for the rest of the project.

## 4. Term-by-term reasoning

**GO:0000160 phosphorelay signal transduction system (IEA, InterPro:IPR001789).**
Right. IPR001789 is the response-regulator receiver domain, matched at 41-157 with the
phospho-accepting Asp90 present, and three independent sources call ActA a response
regulator acting in a signal transduction pathway [PMID:11359579; PMID:17189369;
PMID:26369581]. Caveat for the knowledge-gap list, not for the action: no histidine
kinase has been shown to phosphorylate ActA, the C-signal receptor is unknown, and
phosphotransfer onto Asp90 has never been measured.

**GO:0009966 regulation of signal transduction (IMP, PMID:11359579, CACAO).** The claim
is right and the paper supports it for actA specifically; the sign is determined, so the
sign-specific child GO:0009967 (positive regulation of signal transduction) is the
better term: the null mutant has at most a quarter of wild-type maximal C-signal, i.e.
ActA is required for full C-signalling, and the pathway "responds to C-signal and also
regulates the production of CsgA protein, thus creating a positive feedback loop"
[PMID:11359579]. ActA both receives the signal and raises its production; a positive
regulator either way.

**GO:0043937 regulation of sporulation (IMP, PMID:11359579, CACAO).** This is the
granularity question the brief raises, and the answer is that the *shape* of the term is
already right. The students did not pick a developmental-process term that ActA
executes; they picked a *regulation* term, which is exactly what a protein that sets the
level of a morphogen does. The phenotype is gene-specific and unambiguous — "both
aggregate, neither sporulates" [PMID:11359579] — and it is independently endorsed:
"actA and actB are required for sporulation inside nascent fruiting bodies but not for
the formation of aggregates of cells" [PMID:26369581]. What can be improved is the spore
type: *M. xanthus* myxospores are cellular spores, and other *M. xanthus* proteins are
annotated in the GO:0030435 branch, so GO:0042173 (regulation of sporulation resulting
in formation of a cellular spore), a direct child of GO:0043937, is the supported
specific term.

**Why no gene-expression / transcription term is proposed.** The directly measured
readout for actA is csgA expression and CsgA protein level, so GO:0010628 (positive
regulation of gene expression) or GO:0045893 looks tempting, and the 2007 paper even
shows the operon's own *transcriptional* reporter depressed in a ΔactA mutant. Three
reasons not to assert it, in the order CLAUDE.md asks the questions:

1. *Which entity performs the step?* ActA has no DNA-binding domain. The σ54 activator
   ActB is the DNA-binding member of the operon, and the model is that ActA signals to
   ActB, "which, in turn, would activate ActB, presumably to ActB∼P"
   [PMID:17189369]. ActA's contribution is phosphorelay signalling, which GO:0000160
   and GO:0009967 already capture.
2. *Comparator check.* The entity in the DNA-binding role, ActB, is the one that carries
   a transcription-regulation term: Q93P58 has GO:0006355 regulation of DNA-templated
   transcription (IEA, from its EBP/σ54-activator signatures), while neither actA entry
   has anything of the kind. That is the convention, not an oversight.
3. The csgA link is probably *indirect*: no ActB binding site or σ54 consensus could be
   found upstream of csgA, and "it seems unlikely that ActB directly regulates
   developmental expression of csgA" [PMID:26369581]. A gene-expression term asserted on
   the protein two steps upstream of an unidentified transcription factor would be an
   over-reach.

This is recorded as a `suggested_questions` entry rather than an annotation.

**No molecular-function row exists in GOA.** The review's core function uses GO:0000156
phosphorelay response regulator activity, supported by the receiver domain and the three
published descriptions of ActA as a response regulator, with the caveat above stated in
the core function's own knowledge gap. Diguanylate cyclase activity is *not* proposed:
see the motif check in section 1.

## 5. Open questions carried into the review

- What phosphorylates ActA? No histidine kinase, and no C-signal receptor, is known.
- Is Asp90 phosphorylated at all, and is phosphorylation required for function?
- Is the GGDEF domain catalytically dead (the motif check says probably) and if so what
  does it bind?
- What transcription factor actually drives csgA, given that ActB apparently does not
  bind there?
- Does ActA have any role in the prolonged rippling phenotype distinct from its effect
  on C-signal level?
