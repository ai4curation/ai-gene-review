# bchJ (P26169, *Rhodobacter capsulatus* SB1003) — curation notes

## Provenance of this file

**Deep research was unavailable.** No deep-research API keys exist in this container, so
`just deep-research` was not run and no `-deep-research-<provider>.md` file exists for this
gene. The literature below was assembled directly: from the cached publications, from PubMed
via NCBI E-utilities (`esearch`/`efetch`), from Europe PMC availability queries, from PMC full
text where open, and from web search. Every assertion carries a `[PMID:n "quote"]` or a
UniProt-record pointer.

Papers newly cached for this review with `just fetch-pmid`: 7876113, 17148453, 23252506,
25978726, 20955518. Of these, only PMID:25978726 has `full_text_available: true`; the rest,
and the CACAO-cited PMID:8158642, are abstract-only in the cache.

## What the protein is

213 aa, no transmembrane segments, no cofactor features, protein existence level
`PE 4: Predicted`. Encoded in the ~46 kb *R. capsulatus* photosynthesis gene cluster as
`RCAP_rcc00670`, immediately downstream of `bchE` (`RCAP_rcc00669`) and four genes from
`bchF` (`RCAP_rcc00666`). Single V4R domain (Pfam PF02830, SMART SM00989, InterPro IPR004096),
with a dedicated family signature `NCBIfam TIGR02019 BchJ` and `InterPro IPR010249 BchJ`.
UniProt curates the pathway as
`PATHWAY: Porphyrin-containing compound metabolism; bacteriochlorophyll biosynthesis (light-independent).`
UniProt's `AltName: Full=4-vinyl reductase;` and the domain name V4R ("vinyl-4-reductase") both
preserve an activity assignment that the literature has since withdrawn (see below) — recorded
as a `source_defects` entry against UniProt in the review.

## The CACAO-cited paper: PMID:8158642 (Bollivar, Suzuki, Beatty, Dobrowolski, Bauer 1994)

A cluster-wide mutational survey, not a single-gene paper:
[PMID:8158642 "In this study we have undertaken a systematic directed mutational analysis of 12
open reading frames in the photosynthesis gene cluster to evaluate whether individual open
reading frames have a role in photopigment biosynthesis."] Its readouts are exactly loss of
BChl and accumulation of pathway intermediates:
[PMID:8158642 "mutations constructed in seven open reading frames resulted in a loss of
bacteriochlorophyll biosynthesis, concomitant with the accumulation of specific intermediates
in the Mg-tetrapyrrole biosynthetic pathway"] and
[PMID:8158642 "One mutation was observed to result in partial disruption of bacteriochlorophyll
biosynthesis, leading to the accumulation of bacteriochlorophyll as well as an intermediate in
the biosynthetic pathway."]

The cache is abstract-only and the abstract does not name the 12 ORFs, so I cannot read off
which category bchJ fell into. The partial-disruption phenotype is, however, precisely what the
same laboratory reported for bchJ one year later (below: reduced BChl **plus** an accumulating
intermediate, rather than loss of BChl), which makes bchJ the natural candidate for that single
partial mutant. I state this as an inference, not as a quotation from the 1994 paper.

## bchJ-specific mutant phenotype

[PMID:7876113 "we also observed that directed insertion and deletion mutations in bchJ, a gene
located in the photosynthesis gene cluster, affected the ratio of monovinyl and divinyl
protochlorophyllide"] and, decisively for the process claim,
[PMID:7876113 "bchJ-disrupted strains accumulate reduced levels of bacteriochlorophyll
concomitant with the accumulation of divinyl protochlorophyllide"]. Note that *both* an
insertion and a deletion allele were used, which weakens (though does not exclude) a purely
polar explanation.

Confirmed from the *R. capsulatus* literature by a later group:
[PMID:25978726 "Previous study demonstrated that ΔbchJ mutant of the purple bacterium
R. capsulatus accumulated 8V-PChlide a16, and therefore BchJ was first thought to work as DVR."]

## The contested chemistry: BchJ is not the C8-vinyl (4-vinyl) reductase

The divinyl-protochlorophyllide accumulation above was read as BchJ *being* the 8-vinyl
(divinyl) reductase, DVR. Three lines retract that:

1. **Green sulfur bacteria.** Insertional inactivation of both candidate genes in
   *Chlorobium tepidum* put the activity on CT1063, not bchJ:
   [PMID:17148453 "These data demonstrate that CT1063, renamed bciA, encodes a C-8 divinyl
   reductase in C. tepidum."] The bchJ mutant still made C8-reduced pigments:
   [PMID:17148453 "The bchJ mutant produces detectable amounts of Chl a(PD), BChl a(P), and
   BChl c(F), all of which have reduced C-8 substituents, but the mutant cells secrete large
   amounts of 3,8-divinyl-protochlorophyllide a into the growth medium and have a greatly
   reduced BChl c(F) content."] Their conclusion:
   [PMID:17148453 "The results suggest that BchJ may play an important role in substrate
   channeling and/or regulation of Chl biosynthesis but show that it is not a vinyl reductase."]
2. **A heterologous complementation test.** In *R. sphaeroides*,
   [PMID:23252506 "mutants in which one or both genes were deleted still retained the ability
   to synthesize C8-ethyl bacteriochlorophyll"], and in a cyanobacterial vinyl-reductase mutant
   [PMID:23252506 "R. sphaeroides rsp_3070 was able to restore synthesis of the WT (wild-type)
   C8-ethyl chlorophyll a in the mutant, whereas bchJ did not."] Hence
   [PMID:23252506 "there remains no direct evidence for the activity of BchJ as a C8-vinyl
   reductase"].
3. **Who does it in *Rhodobacter*.** The C8-vinyl reduction in *Rhodobacter* is carried by
   chlorophyllide a oxidoreductase (COR, BchXYZ) and by BciA where present:
   [PMID:25978726 "COR of R. capsulatus can work like DVR, i.e., it has the 8-vinyl-reduction
   ability912."] and in the *R. sphaeroides* ΔbchJ/bciA double mutant
   [PMID:25978726 "This suggests that the intrinsic a-COR present in the double mutant works as
   DVR, as previously reported912, instead of the deleted BciA."]

The **polar-mutation hypothesis** named in this review's brief — that the original 4-vinyl
reductase assignment rested on an insertion that was polar on downstream genes — I could not
substantiate in any source I could read. Chew & Bryant, Canniffe et al. and Tsukatani et al.
all argue from *mutant pigment composition and heterologous complementation*, not from
polarity. PMID:7876113 used a deletion as well as an insertion. Hahn et al. have argued that
bchE and bchJ lie in one operon whose promoter is upstream of bchE, so polarity is a coherent
worry, but it is not the argument the field actually made, and I record no claim about it in
the review.

## What BchJ positively does (still unresolved)

- **Binds a Mg-tetrapyrrole, on the *R. capsulatus* protein itself.**
  [PMID:20955518 "Purified recombinant Rhodobacter capsulatus BchJ and BchM were found to cause
  a shift in the equilibrium amount of Mg-protoporphyrin IX formed in a magnesium chelatase
  assay."] and [PMID:20955518 "BchJ bound magnesium-protoporphyrin IX or formed a ternary
  complex with BchH and magnesium-protoporphyrin IX."] Stoichiometry:
  [PMID:20955518 "Analysis of this shift revealed that it was always in a 1 : 1 ratio with
  either of these proteins and the BchH subunit of the magnesium chelatase."] Proposed role:
  [PMID:20955518 "These results suggest that BchJ may play a role as a general magnesium
  porphyrin carrier, similar to one of the roles of GUN4 in oxygenic organisms."] Note the
  authors' framing: [PMID:20955518 "BchJ may play a similar role to Gun4 in Rhodobacter, as it
  has no currently assigned function in the established pathway."]
- **Raises the effective throughput of the intrinsic COR.** In *R. sphaeroides*, an exogenous
  B. viridis BchYZ competes with the intrinsic enzyme only once BchJ is gone:
  [PMID:25978726 "These results from the two mutants suggest that BchJ in R. sphaeroides
  facilitates the catalytic activity of only the intrinsic a-COR."] The mechanism is explicitly
  open: [PMID:25978726 "Further investigation is still needed to learn whether the exact
  function of BchJ is as a substrate carrier, a scaffold protein to form tertiary complexes, or
  a chaperon for pigment biosynthesis proteins."] and
  [PMID:25978726 "Thus, the function of BchJ in BChl biosynthesis has been enigmatic."]
- The pathway-level membership is not in doubt:
  [PMID:25978726 "BchJ is known to be involved in BChl biosynthesis, although how is still
  unclear."]

## GO term checks (QuickGO, 2026-11-01)

- `GO:0030494` bacteriochlorophyll biosynthetic process. Ancestors: GO:0015995, GO:0015994,
  GO:0042440, GO:0046148, GO:0033013, GO:0033014, GO:0006778, GO:0006779, GO:0009058,
  GO:0008152. **GO:0015979 photosynthesis is not among them.**
- `GO:0015979` photosynthesis — "The synthesis by organisms of organic chemical compounds,
  especially carbohydrates, from carbon dioxide (CO2) using energy obtained from light rather
  than from the oxidation of chemical compounds." BchJ performs no step of this; it supplies the
  pigment. The InterPro2GO mapping IPR010249 → GO:0015979 is therefore pigment-supply read as
  pathway participation, and the review MODIFYs it to GO:0030494 (a lateral correction, since
  the replacement is not a descendant).
- `GO:0036070` light-independent bacteriochlorophyll biosynthetic process **is** a descendant of
  GO:0030494, and matches the UniProt pathway line, so it is the most specific correct term.
- No GO molecular-function term exists for a Mg-porphyrin carrier/channelling activity. The
  children of `GO:0046906` tetrapyrrole binding are only chlorophyll binding, heme binding and
  cobalamin binding; no "magnesium protoporphyrin IX binding" term exists. `GO:0046906` is
  therefore the most specific MF the binding data support, and it is proposed as a NEW row.

## CACAO / GONUTS status (checked 2026-11-01)

`gowiki.tamu.edu` has moved from "temporarily offline" to **permanently retired**. The site
returns HTTP **410 Gone** with the page title "GONUTS has been retired" and the text
"The GO wiki that was at gowiki.tamu.edu is no longer online." EcoliWiki and OMP from the same
lab are still up. The project page's instruction to "re-check the abstract-only rows when GONUTS
returns" is therefore no longer actionable: for CACAO rows whose cached publication is
abstract-only, the paper itself is now the only check available.

## Cross-isolate transfer screen (batch-3 screen 2) — result

PMID:8158642 is cited by four CACAO rows, all `involved_in GO:0030494` / IMP / dated 20111120:

| accession | symbol | taxon id | entry |
|---|---|---|---|
| P26165 | bchF | 272942 | BCHF_RHOCB |
| P26168 | bchE | 272942 | BCHE_RHOCB |
| P26169 | bchJ | 272942 | BCHJ_RHOCB |
| P26236 | bchM | 1061  | BCHM_RHOCA |

The two taxon ids are both *Rhodobacter capsulatus*: 272942 is the strain-level
ATCC BAA-309 / NBRC 16581 / SB1003 reference proteome, 1061 the species node. The split is a
UniProt entry-level artefact, not a curation decision: `BCHM_RHOCA` is a 1992 Swiss-Prot entry
built on the Youvan et al. 1984 sequence (PMID:6744416) that was never re-filed under the
SB1003 proteome, whereas the other three carry `OrderedLocusNames=RCAP_rcc006xx` and sit in
`UP000002361`. All four genes are in the one photosynthesis gene cluster that PMID:8158642
mutated gene by gene, and P26169's own sequence (EMBL Z11165, Burke/Alberti/Armstrong/Hearst)
is from SB1003 — the same strain lineage whose cluster the paper worked in. **The predicted
cross-isolate shape is absent**, and the neighbour-mis-attribution alternative is absent too:
four genes citing one cluster-wide mutational survey is legitimate, not over-harvesting.
