# TAP65 / p65 (*Tetrahymena thermophila*, UniProt W7X6T2) — curation notes

> **Automated deep research was unavailable for this gene.** The configured providers all
> failed (perplexity is not registered; falcon returns an authentication error; openai
> returns `invalid_api_key`). What follows is a **manual literature review** assembled from
> the cached publications in `publications/`, the UniProt flat file
> (`TAP65-uniprot.txt`), and QuickGO term/annotation lookups. No file named
> `*-deep-research-*.md` was created, per `CLAUDE.md`.

## 1. Identity

- UniProt **W7X6T2** (`LARP7_TETTS`), 542 aa, gene **TAP65** (`TTHERM_000318539`),
  "Telomerase-associated protein of 65 kDa", **p65**.
- Domain architecture (UniProt features): HTH La-type RNA-binding domain 112–239,
  RRM 247–335, **xRRM** 374–542. PANTHER `PTHR22792:SF62` (LA-RELATED PROTEIN 7).
- Family: LARP7 (La-related protein 7). The *Tetrahymena* protein is the founding
  structural example of the **xRRM** domain, which was subsequently recognised in genuine
  La and LARP7 proteins [PMID:22705372 "Additionally, our studies define a structurally
  homologous domain (xRRM) in genuine La and LARP7 proteins"].

## 2. Core biology established in *Tetrahymena*

### 2.1 p65 is a stable, stoichiometric subunit of the telomerase holoenzyme

p65 was identified by affinity purification of endogenously assembled *Tetrahymena*
telomerase, and reciprocal immunodepletion showed it is not a loose associate:
[PMID:15131081 "This finding demonstrates that both proteins are stable telomerase RNP
components"]. RNase sensitivity mapping later showed p65 is the subunit that stays behind
when the RNA is destroyed — i.e. everything else in the holoenzyme hangs off TER
[PMID:19941821 "RNase treatment of p65fzz holoenzyme depleted all holoenzyme subunits
except p65"].

Architecturally, p65 belongs to the **catalytic core**, a ternary TERT–TER–p65 complex:
[PMID:22705372 "The catalytic core of Tetrahymena telomerase comprises a ternary complex
of telomerase RNA (TER), telomerase reverse transcriptase (TERT), and the essential La
family protein p65."]; [PMID:23552895 "The EM results together with reconstituted enzyme
activity assays suggest a subdivision of holoenzyme functional units: the TERT-TER-p65
catalytic core, p50-Teb1, and 7-1-4."]; [PMID:19941821 "a biologically stable assembly of
the RNP catalytic core (p65-TER-TERT) associates directly with a second holoenzyme protein
subcomplex (p75-p45-p19)"]. The full holoenzyme is TERT + TER + six proteins
[PMID:26472759 "In addition to TERT and TER, the Tetrahymena telomerase holoenzyme contains
six other known proteins: p65, p75, p45, p19, p50, and Teb1"].

### 2.2 p65 binds TER specifically — not RNA polymerase III transcripts generally

This is the key point distinguishing p65 from genuine La. Affinity-purified p65 recovers
essentially only TER [PMID:15131081 "The similarity of the TERT- and p65-associated RNA
profiles suggests that both proteins are preferentially associated with telomerase RNA."],
and knockdown depletes TER without touching other Pol III transcripts
[PMID:15131081 "whereas telomerase RNA level decreased in p65 knockdown strains, the
accumulation of other RNA polymerase III transcripts was unaffected"].

In vitro the affinity is high and the specificity is sequence-based:
[PMID:15696174 "we determined that p65 bound TER with an affinity of ~2–5 nM under a range
of conditions including physiological ionic strength"];
[PMID:15696174 "These results demonstrate that p65 recognizes the sequence of proximal
stem IV."]; and a size-matched, structured control RNA does not compete
[PMID:15696174 "we determined that Escherichia coli 5S RNA was incapable of p65 mobility
shift competition"]. Four separable modules of the protein contribute
[PMID:16507983 "We demonstrate that four modules of p65 contribute affinity for TER,
including a C-terminal domain that recognizes the conserved dinucleotide bulge of central
stem IV."], with La-RRM1 reading the 3′ tail [PMID:26472759 "The p65 La-RRM1 binds the 3′
polyU tail"].

### 2.3 Three separable jobs: 3′-end protection, RNA folding, TERT loading

The clearest statement of the division of labour is in the structural paper, which lists
them explicitly: [PMID:22705372 "it protects the 3’ end of TER from degradation"],
[PMID:22705372 "it acts as a chaperone to correctly fold TER for protein binding"], and the
bending of stem-loop IV to present it to TERT.

- **3′-end protection / RNA stabilization.** In vivo, p65 is what sets the steady-state TER
  level: [PMID:15131081 "telomerase RNA accumulation in the p65 knockdown strain was
  inhibited dramatically under selective pressure"];
  [PMID:15131081 "These findings provide genetic evidence that p65 functions in vivo to
  promote telomerase RNA accumulation"];
  [PMID:22705372 "Tetrahymena p65 is a telomerase holoenzyme protein essential for TER
  accumulation in vivo"]. TERT accumulation also falls, but as a secondary consequence of
  TER loss [PMID:19941821 "In vivo depletion of the La motif-containing p65, but not p45 or
  p75, reduced the biological accumulation of TERT and TER."].
- **RNA folding chaperone.** p65 binding remodels TER:
  [PMID:22705372 "RNA recognition is achieved by a combination of single- and
  double-stranded RNA binding, which induces a 105° bend in TER"];
  [PMID:17322903 "interaction with the telomerase holoenzyme protein p65 induces structural
  rearrangement of telomerase RNA, which in turn directs the binding of the telomerase
  reverse transcriptase to form the functional ternary complex"];
  [PMID:20713447 "by sequestering stems I and IV, p65 limits the ensemble of structural
  conformations of TER, thereby presenting TERT with the active conformation of TER"].
  Critically, this is *chaperone-like* in the strict sense — it rescues misfolding, not
  merely stabilises: [PMID:20713447 "Several TER mutants exhibited telomerase activity only
  in the presence of p65"]. It also persists in the assembled particle
  [PMID:20713447 "p65 acts as a molecular buttress within the assembled RNP, mutually
  stabilizing TER and TERT in catalytically active conformations"].
- **Hierarchical TERT loading.** [PMID:15696174 "Notably, the p65–TER complex recruits TERT
  much more efficiently than does TER alone."]; quantitatively
  [PMID:15696174 "TERT(1–516) bound to the p65–TER complex with ~30-fold greater affinity
  and more homogeneity than it bound to TER alone"], by a defined mechanism
  [PMID:15696174 "These assays reveal that p65 promotes TERT RNP assembly by a mechanism
  requiring the TER central stem IV dinucleotide bulge."]. The order of events is fixed
  [PMID:16507983 "we show that p65 and TERT assemble on TER with hierarchical rather than
  cooperative binding"], and the xRRM alone suffices for this step
  [PMID:16507983 "This C-terminal domain is necessary and sufficient for p65's function in
  enhancing the recruitment of TERT to TER."]. The cryo-EM structure shows the same thing
  at the holoenzyme level [PMID:26472759 "inducing a large bend in the RNA that facilitates
  assembly of TERT with TER to form the RNP catalytic core"].

### 2.4 Physiological output: telomere length maintenance

*TAP65* is essential [PMID:15131081 "The persistence of the wild-type loci through
phenotypic assortment indicates that both p65 and p45 are encoded by essential genes"], and
knockdown gives the telomerase-loss phenotype
[PMID:15131081 "We found that telomeres were dramatically shorter in p65 and p45 knockdown
strains"].

## 3. Curation judgements and the traps checked for

### 3.1 Is catalytic activity transferred onto a non-catalytic subunit?

**No.** p65 carries no `GO:0003721`/`GO:0003720` (telomerase / RNA-directed DNA polymerase)
annotation in GOA, which is correct: the active site is TERT's, and p65 does not alter
primer-extension chemistry — [PMID:15696174 "Coassembly of p65 did not affect the
primer-extension activity of T. thermophila TERT reconstituted with TER in RRL"]. The
`COMPLEX_ACTIVITY_TRANSFER` failure mode that CLAUDE.md warns about **has not occurred
here**; no action is needed, and none was invented.

### 3.2 Is human LARP7 biology imported onto the ciliate protein?

**No.** There is no `GO:0097322` (7SK snRNA binding), no `GO:0032786`/`GO:0034244`
(transcription-elongation regulation), no `GO:0000494`/snRNA processing and no Cajal-body
term in the GOA. The three IEA rows are family-generic nucleic-acid/RNA binding plus a
subcellular-location mapping, all of which are true of the *Tetrahymena* protein on its own
evidence. This Track A/B failure pattern did not materialise, and nothing was removed on
speculative grounds.

### 3.3 Generic binding terms

`GO:0003676` nucleic acid binding (InterPro IPR035979) and `GO:0003723` RNA binding
(InterPro IPR000504/IPR014886 + PANTHER PTN008582015) are both true but strictly less
specific than what is demonstrated. The specific descendant `GO:0070034 telomerase RNA
binding` is already carried by the gene six times over by IDA, and QuickGO confirms
`GO:0070034` has ancestors `GO:0003723` and `GO:0003676`. Per CLAUDE.md these are
**MODIFY** with `GO:0070034` as the replacement, not `KEEP_AS_NON_CORE`.

There are no `GO:0005515 protein binding` rows in this GOA, so that policy does not apply.

### 3.4 `GO:0000781 chromosome, telomeric region`

IEA from the UniProt subcellular-location mapping (`SL-0276`), which itself rests on
UniProt's `ECO:0000305` inference, not on an observation. The holoenzyme demonstrably
elongates telomeres and p65 is a constitutive core subunit, so the claim is reasonable; but
every assayed p65 activity (3′-end protection, TER folding, TERT loading) belongs to RNP
**biogenesis**, upstream of telomere engagement, and no direct imaging of p65 on telomeric
chromatin in *Tetrahymena* has been published. Kept, marked non-core.

### 3.5 The one proposed addition: `GO:0140691 RNA folding chaperone`

**Participation test.** p65 is not merely required for TER to fold; it performs the
remodelling itself, by direct contact — the 105° bend is made by its own xRRM helix α3x
wedging the GA bulge open [PMID:22705372 "RNA recognition is achieved by a combination of
single- and double-stranded RNA binding, which induces a 105° bend in TER"], and misfolded
TER variants are rescued to activity by p65 [PMID:20713447 "Several TER mutants exhibited
telomerase activity only in the presence of p65"]. It does the work. Passes.

**Comparator test.** QuickGO shows 36 experimental annotations to `GO:0140691`, including
**WRAP53/TCAB1** (`Q9BUR4`, IDA, PMID:19179534 and PMID:29804836) and mouse Wrap53
(`Q8VC51`) — i.e. a telomerase-RNP biogenesis factor acting on telomerase RNA already
carries this exact term. The term is also carried by Hfq, Lsm2/3/4/8, IMP3/IMP4 and plant
cold-shock proteins. So this is **not** a systematic absence that would signal a convention
I have misread; the term is routinely applied to proteins in p65's role.

**Non-redundancy.** `GO:0140691` is an MF whose ancestors are `GO:0003674` and (via
part_of) the BP `GO:0034337 RNA folding`. It is **not** under `GO:0003723 RNA binding`, so
it is not entailed by the accepted `GO:0070034`, and it is not entailed by the BP
`GO:1904868`. The parent BP `GO:0034337` is deliberately *not* proposed — it would be
redundant with `GO:0140691`.

### 3.6 Considered and deliberately NOT proposed

- **`GO:0000333 telomerase catalytic core complex`.** p65 is unambiguously in the
  TERT–TER–p65 catalytic core, and this CC is more informative than `GO:0005697`. But
  QuickGO confirms `GO:0000333` is a `part_of` descendant of `GO:0005697`, which the gene
  already carries nine times by IDA. CLAUDE.md: "Reject a term that is an ancestor or
  descendant of another you are proposing, or of one the gene already carries." Raised as a
  `suggested_questions` item instead, since this is a curation/ontology-practice question
  for GO, not a wet-lab unknown.
- **`GO:1905323 telomerase holoenzyme complex assembly`.** p65's demonstrated assembly role
  is the *catalytic core* step (TER + TERT), which `GO:1904868` already captures exactly.
  Recruitment of p50/Teb1/p75-p45-p19 is not attributed to p65.
- **`GO:0034337 RNA folding`** — redundant with the proposed `GO:0140691` (see above).
- **Anything about 7SK, P-TEFb or Pol II elongation** — human LARP7 biology, not shown here.

## 4. Open questions carried into the review

- Can the 3′-end-protection and the stem-IV-bending functions be genetically separated?
  The 2005 paper explicitly flags this as unresolved
  [PMID:15696174 "Distinguishing the relative importance of these two roles for p65 will
  require the discovery of p65 or TER variants that retain wild-type p65-TER and TERT-TER
  interaction yet eliminate p65 enhancement of TERT RNP assembly."]
- Does p65 remain bound at telomeres during elongation in vivo, or does it act only in
  biogenesis? No published *Tetrahymena* localization data settle this.
- Is there a separate *Tetrahymena* genuine La? The 2004 paper notes a second La-motif
  locus of unknown status [PMID:15131081 "Whether this region produces an mRNA transcript
  and corresponding protein, and if so whether the protein represents ciliate La, remain to
  be determined."]

## 5. Coordination note (TERT, O77448)

TERT is being reviewed in parallel. Shared claims that should read the same way in both
files: (a) `GO:0005697 telomerase holoenzyme complex` is the right complex term for both,
and `GO:0000333` was declined on redundancy grounds here; (b) `GO:1904868 telomerase
catalytic core complex assembly` is appropriate for p65 as the agent that drives it — if
TERT also carries it, that is fine, both subunits participate; (c) catalysis
(`GO:0003721`) belongs to TERT alone and must not appear on p65.

## Comparator query behind the GO:0140691 NEW row (2026-10-22)

Recorded so the figures in that row's `reason` are auditable rather than asserted. QuickGO
annotation search, `goId=GO:0140691`, `goUsage=exact`, `evidenceCode=ECO:0000269` with
`evidenceCodeUsage=descendants` (i.e. experimental evidence only):

```
https://www.ebi.ac.uk/QuickGO/services/annotation/search?goId=GO%3A0140691&goUsage=exact&evidenceCode=ECO%3A0000269&evidenceCodeUsage=descendants&limit=100
```

Re-run 2026-10-22: `numberOfHits: 36` across 32 distinct gene products, including
`UniProtKB:Q9BUR4` WRAP53 (IDA) and `UniProtKB:Q8VC51` mouse Wrap53 (IDA). Those two are the
load-bearing comparators: telomerase-RNP biogenesis factors acting on telomerase RNA, the same
role p65 occupies, so the term is applied to proteins in p65's position and its absence here
reads as a gap rather than a convention.

The counts move as GO annotation advances; what matters for the row is the presence of the
WRAP53 pair, not the exact total.
