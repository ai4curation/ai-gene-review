# Tac1 (Heterocephalus glaber, A0A0P6JY17) — review journal

Protachykinin-1 (PPT / PPT-A), the precursor of substance P and neurokinin A.
UniProt TrEMBL, 130 aa, `PE 3: Inferred from homology`. Five GOA rows, all IEA,
all electronic; the naked mole rat has essentially no experimental GO annotation.

---

## 1. The framing problem this gene sets

The naked mole rat is repeatedly described in the secondary literature — and in the
title of one of the primary papers — as an animal that "naturally lacks substance P".
Taken at face value that would be a strong claim about *this gene product*, and it
would push a reviewer towards `REMOVE` on the molecular-function annotation.

It is an over-simplification, and the primary papers are careful in a way that their
own titles are not. Every primary source qualifies the absence by **tissue**:

- [PMID:18232734 "naturally lack substance P (SP) and calcitonin gene-related peptide
  (CGRP) in the skin innervation"] — note "in the skin innervation".
- [PMID:18232734 "We initially found that the neuropeptides SP and CGRP are both missing
  from naked mole-rat nociceptors innervating the skin"]
- [PMID:20497578 "We have previously shown that naked mole-rats naturally lack substance
  P (SP) in cutaneous C-fibers, but that the neurokinin-1 receptor is expressed in the
  superficial spinal cord"]
- [PMID:32478202 "naked mole-rats do not express neuropeptides, such as Substance P and
  calcitonin gene-related peptide in their cutaneous C-fibers, effectively making the
  peptidergic pain pathway hypofunctional"]
- [PMID:32880221 "NMRs also lack calcitonin gene-related peptide (CGRP) and substance P
  in nociceptive C fibers"]

And the absence is quantitative rather than absolute even within that compartment:

- [PMID:32206859 "in the naked mole-rat, unmyelinated fibers in the skin were observed
  to be virtually devoid of SP and CGRP immunostaining"]
- [PMID:32206859 "intense CGRP and SP immunoreactivity were essentially absent from
  small diameter"] (i.e. likely nociceptive) neurons.

The decisive sentence, which appears in the discussion of the very paper whose title
says "an animal naturally lacking substance P", is this:

- [PMID:21200438 "although SP is absent from naked mole-rat cutaneous C-fibers, both SP
  and CGRP have been identified in presumptive sensory fibers in the viscera"]
- [PMID:21200438 "The presence of SP and CGRP in some sensory afferents suggests that
  peptidergic neurotransmission does occur in the naked mole-rat"]

So the accurate statement is: **substance P immunoreactivity is absent from cutaneous
sensory fibres and small-diameter DRG/TG somata; it is present elsewhere, including
visceral afferents.** Corroborating, in the colon: [PMID:31992138 "CGRP-positive
extrinsic neuronal varicosities were identified encircling and tracking with blood
vessels within the mesentery supplying the distal colon of NMR"]. The
peptidergic system is regionally reorganised, not abolished.

The "myths" paper (PMID:34476892) does not list "naked mole-rats lack substance P"
among its 28 myths, so it does not adjudicate this claim directly. It does treat the
adjacent over-statement in exactly the way argued here — Myth 10 is "naked mole-rats
feel no pain", and the response emphasises the word *selective*: [PMID:34476892 "Normal
nocifensive responses were reported for noxious heat and mechanical stimuli"]. It also
records that naked mole-rats [PMID:34476892 "have diminished substance P signalling
under hypercapnia"] — *diminished*, and condition-dependent, not absent.

## 2. The gene and the protein are intact — sequence evidence

The TrEMBL record annotates **no `PEPTIDE` features at all**, only `SIGNAL 1..19`,
`CHAIN 20..130`, and two SMART `Tachykinin` domain calls (58..68, 97..107). It
therefore does not itself say whether substance P is in this isoform. I resolved this
directly from the sequence
([file:HETGA/Tac1/Tac1-bioinformatics/RESULTS.md](Tac1-bioinformatics/RESULTS.md)):

| peptide | coords | naked mole-rat | identical to human? |
|---|---|---|---|
| Substance P | 58–68 | `RPKPQQFFGLM` | **yes** |
| Neurokinin A | 98–107 | `HKTDSFVGLM` | **yes** |
| Neuropeptide K | 72–107 | `EADSSIEKQ…FVGLM` | D72E only |
| Neuropeptide gamma, 2nd part | 89–107 | `GHGQISHKRHKTDSFVGLM` | **yes** |
| C-terminal-flanking peptide | 111–126 | `ALNSVAYERNAMQNYE` | S120N only |

The two precursors are the same length bar one C-terminal residue, so the comparison
is gap-free: 125/129 identical (96.9%), substitutions A6V, Y35S, D72E, S120N, none of
which touch substance P or neurokinin A. Both tachykinin cores end in the `F-x-G-L-M`
consensus that the GO definition of `GO:0007217` uses to *define* a tachykinin, and
both are immediately followed by `G-K-R` — the Gly that donates the obligatory
C-terminal amide plus the dibasic prohormone-convertase site. UniProt's own keywords
agree that processing is expected: [file:HETGA/Tac1/Tac1-uniprot.txt "Cleavage on pair
of basic residues"] and the `Amidation` keyword.

Three consequences:

1. This entry has the **beta-preprotachykinin architecture** — it encodes *both*
   substance P and neurokinin A, so the answer to "is substance P in this isoform?" is
   yes. (The alpha form would encode substance P only.) I am **not** claiming which
   splice forms the naked mole rat actually transcribes: the entry declares no
   `ALTERNATIVE PRODUCTS`, and all three cross-referenced RefSeq proteins carry this one
   sequence. Alpha/beta/gamma/delta usage in this species is unestablished.
2. The gene is transcribed: [file:HETGA/Tac1/Tac1-uniprot.txt "Expressed in hypothalamus
   and 3 other cell types or tissues."] (Bgee, `ENSHGLG00000001397`).
3. Nothing in the protein is broken. The "lack of substance P" is a statement about
   *where the peptide is made*, not about what the protein is or does.

## 3. The naked-mole-rat literature positively confirms the projected function

This is the unusual and pleasing part of this gene: the species-specific literature
does not merely fail to contradict the electronic annotations, it *actively confirms
them*, because researchers have repeatedly added substance P back and watched the
pathway work.

- **NK1R is present and functional in naked mole-rat spinal cord.**
  [PMID:18232734 "we were able to detect the neurokinin-1 (NK1) receptor
  immunoreactivity in naked mole-rat superficial spinal cord neurons"];
  [PMID:32206859 "The neurokinin-1 receptor (NK1R) for SP is only present in the
  superficial dorsal horn of the naked mole-rat spinal cord"].
- **Exogenous substance P engages it.** [PMID:21200438 "SP also sensitized foot
  withdrawal responses in naked mole-rats, an effect most clearly observed at the
  highest dose tested"], and the effect is reversed by the NK1R antagonist GR-82334:
  [PMID:21200438 "This shows that NK1 receptors function normally in the naked
  mole-rat"]. Also [PMID:21200438 "These results indicate that spinal neurons in naked
  mole-rats have functional SP and NMDA receptors, but that these receptors do not
  participate in heat-evoked foot withdrawal unless SP is experimentally introduced"].
- **Substance P rescues the missing behaviours.** Itch:
  [PMID:20497578 "following intrathecal SP administration, naked mole-rats displayed
  robust scratching behavior in response to histamine that was significantly greater
  than after intrathecal saline"], via
  [PMID:20497578 "We propose that addition of SP activates superficially located
  neurons expressing neurokinin-1 receptors and thus increases the excitatory drive
  into the superficial laminae"]. Inflammatory pain:
  [PMID:32478202 "here we showed that intrathecal SP administration enhanced the
  formalin-induced pain response in naked mole-rats, suggesting that activation of the
  peptidergic pathway is important for the full behavioral response"].
- **The strongest evidence of all is a gene-level add-back.**
  [PMID:18232734 "we used a neurotropic herpes virus engineered to express the
  preprotachykinin gene (PPT) to infect naked mole-rat DRG neurons innervating one
  paw"] and [PMID:18232734 "We used a neurotropic virus to reintroduce PPT gene
  expression into naked mole-rat sensory neurons and found that capsaicin could now
  induce thermal hyperalgesia in the treated mole-rats"]. Expressing *the gene this
  review is about* in naked mole-rat neurons restores tachykinin-dependent
  nociceptive signalling in the intact animal. (Caveat recorded honestly: the construct
  carried a **rat** β-PPT cDNA, so this establishes that the naked mole-rat downstream
  pathway is competent, not that the naked mole-rat protein was the one assayed.)

Mechanism, as understood by the authors of the naked-mole-rat work:
[PMID:21200438 "the binding of SP to NK1 receptors, which leads to phospholipase C
(PLC) activation and subsequent IP3-mediated calcium release"] — this is a general
mechanistic statement citing prior work, not a naked-mole-rat measurement, and I have
treated it as such. It agrees with UniProt for this entry:
[file:HETGA/Tac1/Tac1-uniprot.txt "activation of G(q) and phosphatidylinositol"]
hydrolysis by phospholipase C.

## 4. The curation question: does a tissue-restricted absence change a GO annotation?

This is the interesting call, so I want the argument on the record.

**No, and it should not.** GO annotates what a gene product *is and does*, not where a
cell chooses to express it. Three points make this concrete here:

1. **The annotations under review are about the protein's activity and pathway
   membership.** `GO:0031835` (substance P receptor binding), `GO:0007217` (tachykinin
   receptor signalling pathway) and `GO:0005576` (extracellular region) are claims about
   the encoded peptide. Every one of them survives the naked-mole-rat evidence intact:
   the peptide is human-identical, the processing signals are conserved, the receptor is
   present, and the receptor responds to the peptide with the expected pharmacology.
2. **The naked-mole-rat finding is an expression-pattern finding.** "Absent from
   cutaneous C-fibres" is `IEP`-shaped information about a cell type. GO has no slot for
   it on the gene product's MF, and encoding it as `REMOVE` would assert something
   false — that this protein cannot bind an NK1 receptor — which the SP add-back
   experiments directly refute.
3. **The rescue experiments are the decisive test.** If the annotation were wrong, adding
   the peptide (or the gene) back would do nothing. It does the opposite: it restores
   itch, capsaicin nocifensive behaviour, thermal hyperalgesia and formalin responses,
   all NK1R-dependent. That is a positive confirmation of the projected annotations, in
   this species, by intervention.

Where the naked-mole-rat finding *does* legitimately bear on curation is on the
**organism-level physiology term**, `GO:0006954` inflammatory response. In other
mammals a large part of the tachykinin contribution to inflammation is *neurogenic* —
substance P released from peptidergic cutaneous C-fibre terminals
([PMID:32478202 "In most mammals, TRPV1+ peptidergic C-fibers synapse in lamina I of
the spinal cord where the neurokinin I receptor (NK1r) for SP is also expressed"]) —
and that arm is precisely the one documented to be hypofunctional here
([PMID:32478202 "effectively making the peptidergic pain pathway hypofunctional"], and
the selective inflammatory-pain insensitivity of PMID:18232734). The term is still
defensible — the capability is retained and is unmasked by SP add-back — but it is not
a *core* function of this protein in this animal. Hence `KEEP_AS_NON_CORE`, not
`REMOVE` and not `ACCEPT`.

The right home for the species-specific finding is therefore: this notes file, the
`description`, and `suggested_questions`/`suggested_experiments` — plus one explicit
sentence in each affected `review.reason` so a future curator does not re-litigate it.

## 5. Actions taken

| GO term | evidence | action | one-line reason |
|---|---|---|---|
| GO:0005576 extracellular region | IEA, GO_REF:0000044 (SubCell SL-0243) | ACCEPT | signal peptide 1..19, UniProt `Secreted`; mature tachykinins act on cell-surface GPCRs |
| GO:0006954 inflammatory response | IEA, GO_REF:0000118 (PTN000134172) | KEEP_AS_NON_CORE | capability retained (SP add-back enhances formalin response) but the cutaneous neurogenic arm is hypofunctional in this species |
| GO:0007217 tachykinin receptor signalling pathway | IEA, GO_REF:0000120 | ACCEPT | both encoded peptides literally satisfy the term's `F-x-G-L-M` definition; NK1R present and antagonist-reversible in NMR |
| GO:0031835 substance P receptor binding | IEA, GO_REF:0000118 (PTN000134172) | ACCEPT | NMR substance P is human-identical; NMR NK1R responds and is blocked by GR-82334 |
| GO:0007204 positive regulation of cytosolic Ca²⁺ | IEA, GO_REF:0000120 (from human P20366) | KEEP_AS_NON_CORE | correct and well-grounded (human IDA + PAINT) but a generic downstream readout of Gq–PLC, not what distinguishes this protein |
| GO:0031837 substance K receptor binding | **NEW** (ISS) | NEW | the set covers only the SP/NK1R arm; the precursor also encodes neurokinin A and UniProt states it is a TACR2 ligand |
| GO:0007209 PLC-activating tachykinin receptor signalling | **NEW** (ISS) | NEW | mechanistic refinement of GO:0007217 that makes the GO:0007204 calcium claim interpretable; human ortholog carries it |

No `REMOVE`, no `MODIFY`, no `UNDECIDED`. Every projected term traces to a PAINT node
(`GO_REF:0000033`) on human `P20366` with experimental grounding beneath it, and
`GO:0007204` additionally has a human IDA (`PMID:8957234`, not cached) — I checked the
human annotation set via QuickGO rather than assuming.

## 6. Deep-research providers: falcon (species-specific) vs affinage (human ortholog)

Two provider records are present in the folder, and they perform very differently.

### 6a. The falcon report — good, and it converged independently

`Tac1-deep-research-falcon.md` is a genuine *Heterocephalus glaber* report (Edison,
2026-09-02, 23 citations). I read it after forming the argument in §4 from the primary
papers, and it reaches the same conclusion by the same route:

- [file:HETGA/Tac1/Tac1-deep-research-falcon.md "In the naked mole-rat, the coding locus
  is apparently intact, but SP expression is selectively absent from cutaneous peptidergic
  C-fibers."]
- [file:HETGA/Tac1/Tac1-deep-research-falcon.md "This should not be generalized to
  complete organism-wide absence: SP- and CGRP-positive presumptive sensory fibers have
  been reported in visceral tissues, suggesting tissue- or neuronal-subtype-specific
  regulation"]

It also handles the identity check properly — it explicitly separates Tac1 from Tac2 and
does not drift onto the *C. elegans* / *Candida* / rice homonyms that swamp the affinage
record. And it flags its own orthology-based inferences as inferences, e.g. on the
neurokinin A arm: [file:HETGA/Tac1/Tac1-deep-research-falcon.md "Production of NKA or
extended NKA peptides is biologically plausible from mammalian conservation but should
remain annotated as **predicted** until naked-mole-rat transcript isoforms and endogenous
processed peptides are established by long-read RNA sequencing and targeted peptidomics."]
That is exactly the standard I applied to the `GO:0031837` proposal.

Two leads it supplied that the cached corpus does not contain, recorded here rather than
curated because neither is verifiable from the local cache:

1. **Zhao, Lee, Gryszkiewicz & Park (2025), "Life without substance P: The naked mole
   rat"** (Elsevier, pp. 275-290, doi:10.1016/b978-0-443-22194-1.00013-6) — a book chapter
   devoted to precisely the question this review turns on. Not in `publications/`, no
   PMID recovered, so nothing here rests on it; it should be fetched before any future
   revision of this gene.
2. **CAP-TAC1** (Wiggenhorn et al. 2023, *Nat Commun*, doi:10.1038/s41467-023-43857-0) —
   [file:HETGA/Tac1/Tac1-deep-research-falcon.md "an N-terminally pyroglutamylated and
   C-terminally amidated TAC1-derived circulating peptide"] reported as a nanomolar
   agonist at multiple tachykinin receptors in mouse and human plasma. This is a *third*
   class of product from the TAC1 locus, beyond substance P and the neurokinin A series.
   The report is explicit that [file:HETGA/Tac1/Tac1-deep-research-falcon.md "CAP-TAC1 has
   **not been demonstrated in *H. glaber***"], so it is not annotated here, but it raises
   a real question: an animal described as lacking substance P in skin could still carry a
   systemic tachykinin tone nobody has measured. Added to `suggested_questions`.

Reservation: the report quotes some numbers loosely (it renders the intrathecal substance
P doses from PMID:21200438 as "1-10 mM" and "100 mM" where the paper says µM), so its
figures should not be copied without checking the source. Nothing in this review depends
on a number taken from it.

## 7. What the affinage human-ortholog record missed

The provided `Tac1-deep-research-affinage-human-ortholog.md` is a human-`TAC1` record,
used here only as a conserved-mechanism baseline. Two problems worth recording, because
this is how provider recall gets measured:

1. **It contains no naked-mole-rat content whatsoever** — which the falcon report, run
   on the same gene, shows was avoidable rather than inherent to the question. Not one of its 36 citations
   is a naked-mole-rat paper, and none of the six decisive papers used above appears in
   it. Everything that actually decides this review — the tissue-restricted absence, the
   visceral SP/CGRP fibres, the intrathecal SP rescues, the HSV-PPT gene add-back — was
   invisible to it. That is expected (affinage is human-only) but it means the record
   contributed nothing to the curation calls, only to background.
2. **Its corpus is contaminated by symbol collisions and it says so itself**: the record
   mixes mammalian *TAC1* (the neuropeptide precursor) with *C. elegans* TAC-1 (a TACC
   microtubule-associated protein), *Candida albicans*/*C. parapsilosis* Tac1 (a
   zinc-cluster transcription factor) and rice *TAC1* (tiller angle control). Roughly a
   third of its "dated findings" table describes proteins unrelated to this gene. It
   flags this in its narrative, but a downstream consumer that imported the table
   wholesale would produce nonsense.
3. Its `mechanism_profile` grounding (`GO:0048018 receptor ligand activity`,
   `GO:0005576 extracellular region`) is not wrong but is coarser than the existing GOA
   set, and per the brief it was not imported. I re-grounded every term independently
   against QuickGO.

Where it *was* useful: the mouse `Tac1`-knockout phenotype literature it collects
(anxiety/depression PMID:12427862, nociceptor mechanical sensitization PMID:31012376,
energy balance PMID:28775376, prolactin secretagogue PMID:20434341) is a good reminder
that this gene is pleiotropic well beyond nociception, which is what motivates the
hypothalamic-expression question in `suggested_questions`.

## 8. Unresolved / knowledge gaps

- **No naked-mole-rat measurement of mature substance P anywhere.** Every naked-mole-rat
  observation about the peptide is immunohistochemical, in skin/DRG/spinal cord. There is
  no LC-MS/MS or RIA quantification of naked-mole-rat SP or NKA in any tissue, so the
  conserved processing sites are inferred to be used, not shown to be used.
- **No naked-mole-rat `Tac1` transcript-level data in the cached literature.** Bgee says
  the gene is expressed in hypothalamus and three other tissues, but I found no paper
  comparing *Tac1* mRNA in naked-mole-rat DRG versus mouse DRG. It is therefore *not*
  established whether the cutaneous absence is transcriptional (the gene is off in those
  neurons), post-transcriptional, or a loss of the peptidergic neuron population itself
  — the third possibility is raised but left open in PMID:32206859.
- **The visceral claim rests on a citation chain.** PMID:21200438 asserts visceral SP+CGRP
  fibres citing Park et al. 2008; PMID:32206859 cites Park et al. 2003 and Hockley et al.
  2020 for visceral CGRP. The cached PMID:31992138 shows colonic CGRP directly, but I did
  **not** find a cached figure showing visceral *substance P* immunoreactivity in the
  naked mole rat. The claim is well-sourced in review prose but I could not verify the
  primary image, so I have cited it as the authors' statement rather than as a primary
  result.
- **Which tachykinin splice form(s) the naked mole rat uses** is unknown (see §2).
- **No evidence either way about neurokinin A / NK2R (TACR2) in the naked mole rat.**
  The entire naked-mole-rat literature is about substance P and NK1R. The neurokinin A
  arm is annotated here by sequence inference only.
