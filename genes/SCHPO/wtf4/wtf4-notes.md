# wtf4 (SPCC548.03c, Q9P3V0) — curation notes

*S. pombe* 972h-. Reviewed 2026-10-22.

## Identity: three separate naming hazards

`wtf4` is a dangerous symbol. The `wtf` family was numbered independently by
different groups, and UniProt's gene-name lists still carry the collisions:

| Accession | Entry name | Gene names as listed | Organism |
|---|---|---|---|
| **Q9P3V0** | WTF4_SCHPO | `wtf4`, **synonym `wtf13`**, SPCC548.03c | *S. pombe* 972 |
| O74420 | **WTF13_SCHPO** | `wtf13` | *S. pombe* 972 |
| Q8TF80 | **WTF5_SCHPO** | `wtf5`, **`wtf4`**, SPCC794.02 | *S. pombe* 972 |
| A0A218N034 | WTF4_SCHKA | `wtf4` | *S. kambucha* (taxon 204045) |

1. Q9P3V0 lists `wtf13` as a synonym, but **wtf13 is a distinct gene with its own
   accession** (O74420, WTF13_SCHPO, 388 aa).
2. Q8TF80 lists `wtf4` among its gene names although its own entry name is
   `WTF5_SCHPO`.
3. The *S. kambucha* ortholog is a **separate UniProt entry under a separate taxon**,
   and is the protein almost all of the experimental work was actually done on.

PomBase is unambiguous and is the authority used here: `SPCC548.03c` = `wtf4` =
Q9P3V0; `SPCC794.02` = `wtf5` = Q8TF80. PomBase's own product name is itself
two-valued — "wtf meiotic drive antidote Wtf4 OR wtf meiotic drive poison Wtf4" —
because one locus makes both.

## Biology

A natural poison–antidote meiotic driver: one locus, two overlapping transcripts
with distinct start sites, two proteins with **opposing** functions.

- Architecture is **alternative initiation**, not splicing
  [file:SCHPO/wtf4/wtf4-uniprot.txt "Event=Alternative initiation; Named isoforms=2;"].
  Isoform 1 (Q9P3V0-1, 366 aa, displayed) = **antidote**; isoform 2 (Q9P3V0-2) =
  **poison**, which replaces residues 1–44 with `ML` (VSP_060942), i.e. the poison is
  the N-terminally truncated short form.
- [PMID:28631612 "We show that Sk wtf4 generates two transcripts from alternative start sites: a long transcript encoding an antidote and a short transcript encoding a gamete-killing poison."]
- Asymmetry is the whole trick: the poison acts in *trans* on every spore in the
  ascus, the antidote only in the spores that inherit the allele
  [PMID:28631612 "Whereas the poison protein is found in all the gametes, the antidote protein is enriched only in the gametes encoding Sk wtf4"];
  [file:SCHPO/wtf4/wtf4-uniprot.txt "poison component is trans-acting and targets all spores within an ascus"].
- Mechanism: the poison self-assembles into dispersed cytoplasmic aggregates that
  are toxic; the antidote co-assembles with it and reroutes the co-aggregate to the
  vacuole
  [PMID:33108274 "Wtf4poison forms toxic aggregates that are dispersed throughout the cytoplasm."];
  [PMID:33108274 "The Wtf4antidote forms aggregates that are recruited to the vacuole and vacuole-associated inclusions and are largely non-toxic."];
  [PMID:33108274 "When the two Wtf4 proteins are expressed together, the Wtf4antidote and Wtf4poison co-assemble and are trafficked to the vacuole."].
- **Both** steps are required — co-assembly alone does not rescue
  [PMID:33108274 "neutralization of the Wtf4poison requires both co-assembly with the Wtf4antidote"].
- Host pathways are exploited rather than encoded: a *S. cerevisiae* screen
  implicates CVT/autophagy and vacuolar trafficking
  [PMID:33108274 "we found that several genes involved in vesicle transport, endocytosis, and trafficking to the vacuole (e.g. ATG11, SNF7, and multiple VPS genes) are also required for survival when the Wtf4 proteins are expressed"].
- Drive is strong: 93% transmission in a pure *S. kambucha* background
  [PMID:28631612 "We did, however, observe strong drive (93% transmission) of Sk wtf4+ relative to Sk wtf4Δ in diploid 14"].
- Family context: [PMID:32790622 "Different natural isolates contain between 4 and 14 predicted wtf drivers, almost all of which are found on chromosome 3"].
- Specificity is hypersensitive to sequence:
  [PMID:32790622 "even a mismatch of two amino acids within the C-terminus can disrupt the ability of a Wtfantidote to neutralize a Wtfpoison"].

## The species problem (matters for every experimental row in GOA)

**Essentially all of the functional work used the *S. kambucha* allele, not the
reference-strain 972 allele.**

- [PMID:33108274 "The wtf4 meiotic driver used in this work is from S. kambucha, an isolate that is almost identical (99.5% DNA sequence identity) to the commonly studied lab isolate of S. pombe"]
- But the *genes* are far more diverged than the genomes:
  [PMID:28631612 "Sk wtf4 shares only 89% DNA sequence identity (82% amino acid identity) with the gene in the orthologous locus in Sp (Sp wtf4)"]

So the Sp/Sk proteins differ at ~18% of residues in a family where a two-residue
C-terminal mismatch abolishes antidote specificity. UniProt handles this correctly —
its isoform-level FUNCTION and SUBCELLULAR LOCATION statements on Q9P3V0 are
`ECO:0000250|UniProtKB:A0A218N034`, i.e. explicitly by similarity from the
*S. kambucha* entry. PomBase's `IDA`/`IMP` rows on Q9P3V0 are the ones that elide the
distinction.

What *is* directly established for the Sp 972 gene itself:
- meiotic transcription and the two-start-site architecture
  [PMID:28631612 "This revealed that Sp wtf4 is transcribed during meiosis and generates two major overlapping transcripts with different start sites"];
- vacuolar plus cytoplasmic-inclusion localization on overexpression
  [PMID:33108274 "Interestingly, S. pombe wtf4, the homolog of the S. kambucha wtf4 allele used in this study, was previously shown to localize both inside the vacuole and as large cytoplasmic inclusions when overexpressed in S. pombe vegetative growth (Matsuyama et al., 2006)."]
  — which independently vindicates the otherwise-suspect HDA rows from PMID:16823372.

Not directly demonstrated for the Sp 972 allele: that it drives. Keeping the drive
annotations is still right (the gene is a wtf driver by architecture, expression and
family membership, and PomBase curators read the full text), but the strength of
evidence is weaker than an `IMP` row suggests. Logged as a question, not a REMOVE.

## Ontology findings

Three verified facts from QuickGO drove three of the annotation actions.

1. **`GO:0140549` spore inner membrane is `only_in_taxon` Bacteria**, and defined as
   "The membrane surrounding the spore core (endospore core)". It cannot apply to a
   fission yeast ascospore. The annotation exists because UniProt's "Spore membrane"
   location text matches this term's `spore membrane` **synonym**. → REMOVE.
   If a spore-delimiting membrane is what was intended, the Ascomycota term is
   `GO:0005628` prospore membrane (`only_in_taxon` Ascomycota; its definition names
   *S. pombe* as the exemplar) — but the imaging resolves vacuole, ER and dispersed
   aggregates, not a membrane rim, so nothing independently supports that transfer
   and no replacement is asserted.

2. **`GO:0090729` toxin activity is `never_in_taxon` Schizosaccharomyces**, and its
   definition requires acting on "another (target) organism, initiating pathogenesis".
   `GO:0097351` toxin sequestering activity is `never_in_taxon` Eukaryota. So neither
   the obvious MF for the poison nor the obvious MF for the antidote-as-antitoxin is
   available. GO has **no MF term for an intra-organismal gamete killer** — a real
   ontology gap, and almost certainly why PomBase carries `GO:0003674` with `ND`
   (re-affirmed 2026-07-24). Proposed a new term rather than forcing a wrong one.

3. **`GO:0072324` ascus epiplasm has no `cytoplasm` ancestor** (ancestors are only
   `GO:0110165` and `GO:0005575`), despite being defined as "Ascus cytoplasm that is
   not packaged into ascospores". So `GO:0005737` cytoplasm is *not* formally entailed
   by the epiplasm annotation and cannot be called `TOO_GENERAL` on that basis. Logged
   as an ontology observation; it is a plausible missing `part_of`.

For the antidote, `GO:0140311` **protein sequestering activity** ("Binding to a
protein to prevent it from interacting with other partners or **to inhibit its
localization to the area of the cell or complex where it is active**", no taxon
constraints) is a near-exact fit for co-assembly plus rerouting to the vacuole. Used
as the MF in `core_functions` and proposed as the replacement for the `ND` row.

## ER localization is probably an artifact of the starvation regime

`GO:0005789` has only ISS/IEA support, and the authors of the source work doubt their
own observation: [PMID:33108274 "We speculate this colocalization with the ER is due to nitrogen starvation which is required to induce meiosis and promotes organelle autophagy in S. pombe"].
In vegetative cells the antidote shows essentially **no** ER correlation
[PMID:33108274 "Wtf4antidote-mCherry and CMAC shows a Pearson coefficient of approximately 0.69, while Wtf4antidote-mCherry and Sec63-YFP shows −0.1."]
while the vacuole correlation in spores is 0.89. → MARK_AS_OVER_ANNOTATED, not REMOVE
(the colocalization was really seen, it just probably is not a functional site).

## Curation gaps (not knowledge gaps)

- GOA carries **no isoform-qualified rows at all**, although UniProt's FUNCTION and
  SUBCELLULAR LOCATION statements are fully isoform-resolved and the two isoforms have
  *opposing* functions. `isoform:` is deliberately left unset on the existing
  annotations here, because it records what GOA says was tested and GOA says nothing;
  the resolution is captured in `functional_isoforms` instead.
- ER-membrane and vacuole localization in spores is `IDA`-grade in PMID:33108274
  (Figure 1—figure supplement 2) but reaches GOA only as ISS/IEA.
- `FunctionalIsoformTypeEnum` has no value for **alternative initiation** — only
  SPLICE_VARIANT, SPLICE_CLASS, CLEAVAGE_PRODUCT, MODIFICATION_STATE,
  CONFORMATIONAL_STATE. `SPLICE_VARIANT` is used here as the closest available value
  and is *wrong on mechanism*; the poison/antidote pair is the textbook
  alternative-initiation case. Worth a schema addition.

## Gene-drive relevance

The source papers frame this work as groundwork for engineered drives:
[PMID:33108274 "However, the molecular mechanisms employed by most meiotic drivers are unknown."]
and the Discussion argues wtf genes are good drive candidates because they are small
(~1 kb) and autonomous. This is the natural-driver counterpart to the engineered
gene-drive material elsewhere in the repo (`genes/ANOGA/*`, `genes/STRP1/cas9`).
