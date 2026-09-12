# AAMDC (Mth938 domain-containing protein) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider
(`AAMDC-deep-research-affinage.md`, gates passed) plus UniProt Q9H7C9, the GOA TSV and the
primary literature.

## Headline: the IBAs here are *good*, and the `protein binding` set is worthless

This gene is the near-mirror-image of A1BG (reviewed earlier in this campaign), which makes
it a useful calibration point. There, the IBAs were wrong and needed removal. Here they are
the **only** annotations with real evidence behind them, and the experimental-looking `IPI`
annotations are the ones that should be discounted.

## The two IBAs both trace to a genuine mouse ortholog with primary data

Both IBAs cite `MGI:MGI:1913523`, which is **mouse *Aamdc*** — the true ortholog, not a
paralog. Its own GO record carries, from PMID:22279136:

- `GO:0045600 positive regulation of fat cell differentiation` — **IDA *and* IMP**
- `GO:0045944 positive regulation of transcription by RNA polymerase II` — IDA
- `GO:0043066 negative regulation of apoptotic process` — IMP

and `GO:0005737 cytoplasm` by IDA from PMID:21622130.

Reading the source paper confirms the adipogenesis annotation is well-founded and
bidirectional — gain of function *and* loss of function
[PMID:22279136, "Our results indicated that LI2 was sufficient to drive preadipocyte
differentiation via modulating the phosphorylation level and transcriptional activity of
CREB"] and [PMID:22279136, "knockdown of the LI2 protein resulted in preadipocyte apoptosis
via caspase-3 activation during adipogenesis"]. (The mouse gene was called *LOC66273*
isoform 2 / "LI2" in that paper; hence the "adipogenesis associated" in the human gene name.)

So `GO:0045600` is exactly what IBA is for: a solid ortholog phenotype transferred to a human
gene with no experimental data of its own. **ACCEPT.** UniProt's own FUNCTION line for human
AAMDC is `ECO:0000250` (by similarity) for the same reason
[file:human/AAMDC/AAMDC-uniprot.txt, "May play a role in preadipocyte differentiation and"].

## The eight `protein binding` IPIs are all high-throughput, and five are a classic artefact

| Partner | Screen |
|---|---|
| ACY3 (Q96HD9), GORASP2 (Q9H8Y8) | PMID:25416956 (Rolland HI-II-14) Y2H |
| VPS9D1 (Q9Y2B5) | PMID:32296183 HuRI |
| **APP-2, HTT, ATXN3, DNM2-2, GDAP1** | **PMID:32814053** |

The five-partner block from PMID:32814053 is the giveaway. That paper is *"Interactome
Mapping Provides a Network of Neurodegenerative Disease Proteins and Uncovers Widespread
Protein Aggregation in Affected Brains"* — but note that title phrase refers to
aggregation seen in postmortem patient brain tissue, not to the interaction dataset. The
argument against these five rests on the screen design instead: one systematic Y2H pass over
~500 neurodegeneration-related baits, with a single small uncharacterised protein scoring
against five of them and no independent replication or follow-up for any pair. AAMDC has no
described role in neurodegeneration.

The remaining three are single-publication Y2H hits (UniProt's `NbExp=3` counts assay
replicates within one study, not independent studies).

**The most telling observation: not one of the eight recovered RABGAP1L or RAB7A** — the only
AAMDC interaction with functional follow-up in the literature. The GOA binding record for this
gene is entirely orthogonal to its known biology. All eight are marked over-annotated.

## What the human literature actually shows

One substantial human paper, PMID:33772001 (Nat Commun 2021), studying AAMDC as an oncogene in
the 11q13.5–14.1 (IntClust2) amplicon of ER+ breast cancer:

- **AKT activation is causal, not correlative** —
  [PMID:33772001, "Ectopic AAMDC expression is sufficient to activate AKT signaling, resulting
  in estrogen-independent tumor growth."] This supports a `NEW` `GO:0051897` annotation, and is
  the only human functional annotation this gene can currently carry.
- **PI3K-AKT-mTOR control and metabolic reprogramming** —
  [PMID:33772001, "We show that AAMDC controls PI3K-AKT-mTOR signaling, regulating the
  translation of ATF4 and MYC and modulating the transcriptional activity of AAMDC-dependent
  promoters."]
- **RABGAP1L/RAB7A endolysosomal platform** —
  [PMID:33772001, "we provide evidence that AAMDC can interact with the RabGTPase-activating
  protein RabGAP1L, and that AAMDC, RabGAP1L, and Rab7a colocalize in endolysosomes."] Note
  the authors' own hedge ("can interact", "provide evidence"). Colocalisation is not
  co-residence in a complex, so `GO:0036019 endolysosome` is proposed but flagged as resting
  on colocalisation from a single study.

## The molecular function is genuinely unknown

Worth stating plainly, because it is the main knowledge gap: **AAMDC has no molecular function
annotation of any kind, and none is currently justifiable.** Mouse *Aamdc* even carries an
explicit `GO:0003674 molecular_function` **ND** (no data). The protein is a small Mth938-domain
protein with a solved structure but no assigned activity, and affinage's `mechanism_profile`
reports `molecular_activity: (none)` — the provider agreeing there is nothing to ground. Every
described effect (adipogenesis, AKT activation, ATF4/MYC translation) is a downstream cellular
consequence, not a biochemical activity. I have deliberately **not** invented an MF term.

### Tested, not just asserted

A negative claim deserves evidence, so I ran a family-wide analysis
(`AAMDC-bioinformatics/analyze_mth938.py` → `RESULTS.md`; every figure fetched at run time
from the InterPro, UniProt and QuickGO REST APIs, re-runnable). Enumerating every reviewed
Swiss-Prot member of AAMDC's Pfam family **PF04430 — aptly named DUF498, "domain of unknown
function"**:

| Reviewed family members | 13 |
|---|---|
| With any experimental MF term (excluding bare protein binding) | **0** |
| With an explicit `GO:0003674` **ND** | 4 |
| With a UniProt CATALYTIC ACTIVITY block | **0** |

The missing molecular function is a property of the **entire family**, not an oversight on
this gene.

### And the family points somewhere specific

The family is not wholly uncharacterised. Its other branch is **NDUFAF3**, with a consistent
function in every organism studied — human, mouse, rat, bovine, zebrafish, Xenopus,
Drosophila — an **assembly factor for mitochondrial complex I**, the Drosophila entry
experimentally supported (PubMed:34386730).

That is informative in a particular way. NDUFAF3 is an assembly factor, *not an enzyme*: it
binds subunits, helps build a complex, has no catalytic activity, and is not part of the
finished product. Consistent with that, no member of this family — NDUFAF3 included — has a
catalytic activity block or an experimental MF term.

So the family signal does **not** suggest a hidden enzymatic activity awaiting discovery. It
suggests a protein-assembly or chaperone-like role — precisely the class of function GO
cannot currently express as a molecular function (see the AAGAB review in this campaign,
where the same gap was filed under `proposed_new_terms`). Two genes in, that is twice the
same structural limitation in GO.

The right experimental question is therefore probably not "what does AAMDC catalyse?" but
"what does it help assemble?"

## Where the localisation bar sits, and why

PMID:33772001 reports three localisation observations; only one is annotated, so the
asymmetry is worth stating.

- **Endolysosome (annotated, non-core).** AAMDC, RABGAP1L and RAB7A colocalise there. Taken,
  because it is tied to a specific named interaction the paper pursues mechanistically —
  with the caveat now in the annotation that `GO:0036019` denotes the *transient hybrid
  organelle* from late-endosome/lysosome fusion, which IF colocalisation with RAB7A (a broad
  late-endosome/lysosome marker) cannot resolve.
- **Nuclear and plasma-membrane staining (not annotated).** The same paper reports AAMDC "in
  both cytoplasmic and nuclear compartments, accompanied by plasma membrane staining
  depending on the cell line analyzed". Cell-line-dependent IHC with no functional experiment
  attached, and not pursued by the paper.
- **Endosomal trafficking (not annotated).** A knockdown lysosomal phenotype is said to
  substantiate "a role of AAMDC in the regulation of endosomal trafficking". Left out: a
  single-sentence interpretation of a phenotype, and a trafficking-regulation annotation on a
  protein with no known molecular function would be exactly the over-reach this review
  otherwise avoids.

The bar: a compartment is annotated when a named, mechanistically pursued interaction puts it
there — not on staining pattern, and not on a phenotype's interpretation alone.

## Actions

| Term | Evidence | Action |
|---|---|---|
| `GO:0045600` positive regulation of fat cell differentiation | IBA | ACCEPT |
| `GO:0005737` cytoplasm | IBA, IEA, ISS | ACCEPT |
| `GO:0005515` protein binding ×8 | IPI | MARK_AS_OVER_ANNOTATED |
| `GO:0051897` positive regulation of PI3K/AKT signal transduction | IDA (proposed) | NEW |
| `GO:0036019` endolysosome | IDA (proposed) | NEW |
