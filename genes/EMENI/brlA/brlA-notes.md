# brlA (Aspergillus nidulans) — curation notes

UniProt: P10069 (BRLA_EMENI). C2H2 zinc-finger transcription factor; master
regulator of conidiophore development ("bristle"). Part of the
`conidiation_regulatory_cascade` module.

## Core biology (with provenance)

- **Master switch, necessary and sufficient.** brlA mediates the developmental
  switch from indeterminate apical hyphal growth to the budding growth pattern of
  the conidiophore; misscheduled (forced) expression in vegetative cells activates
  developmentally regulated genes and drives conidiophore/spore formation.
  [PMID:3293800 "brlA is necessary and sufficient to direct conidiophore development"];
  [PMID:3293800 "The brlA gene of A. nidulans mediates the developmental switch from the indeterminate, apical growth pattern of vegetative cells to the budding growth pattern of conidiophores"].
- **C2H2 zinc-finger TF.** 432-aa polypeptide with two directly repeated
  TFIIIA-type Zn(II) coordination motifs.
  [PMID:3293800 "brlA encodes a 432 amino acid polypeptide containing two directly repeated motifs resembling the Zn(II) coordination sites first recognized in Xenopus TFIIIA"].
- **DNA-binding transcriptional regulator (direct).** BrlA binds specific DNA
  response elements (BREs); expressed in yeast it activates a BRE-driven reporter,
  demonstrating sequence-specific transcriptional activation.
  [PMID:8417986 "The brlA gene of Aspergillus nidulans plays a central role in controlling conidiophore development"];
  [PMID:8417986 "to test the hypothesis that brlA encodes a transcriptional regulator and to identify sites of interaction for the BrlA polypeptide"].
- **Top of the brlA→abaA→wetA dependent pathway.** The three genes form a
  dependent pathway regulating asexual reproductive development; brlA expression
  activates abaA and wetA and leads to cessation of vegetative growth and spore
  formation.
  [PMID:2655931 "Aspergillus nidulans brlA, abaA, and wetA form a dependent pathway that regulates asexual reproductive development"];
  [PMID:2655931 "Expression of brlA in vegetative cells leads to activation of abaA and wetA, cessation of vegetative growth, cellular vacuolization, and spore formation"].
- **Two overlapping transcription units brlAα / brlAβ**, individually required for
  conidiophore development.
  [PMID:8508769 "the brlA locus consists of overlapping transcription units, designated alpha and beta"].
- **Induced by the FluG/Flb upstream activators.** Recessive mutations in
  fluG/flbA–E reduce brlA expression (fluffy phenotype), placing brlA downstream
  of the developmental-competence machinery.
  [PMID:9339347 "The initiation of conidiophore development in the filamentous fungus Aspergillus nidulans is a complex process requiring the activities of several genes including fluG, flbA, flbB, flbC, flbD, and flbE"].

## Secondary / non-core roles

- **Secondary metabolism link.** brlA activity also affects sterigmatocystin (ST)
  biosynthesis and secondary-metabolite regulation (dominant mutations affect both
  sporulation and ST). Real but non-core relative to the conidiation master-switch
  function. [PMID:9339347].
- **Autolysis.** Asexual-sporulation signalling (including brlA) modulates
  autolysis via chitinase ChiB. Downstream/non-core. [PMID:19486415].
- **Starvation.** brlA expression is modulated by starvation stress (IEP) — a
  regulatory input to brlA, not brlA acting in the starvation response.
  [PMID:7894714].

## Annotation-review judgments

- Core MF: **DNA-binding transcription factor activity** (GO:0003700 IDA; GO:0000981
  IBA) — ACCEPT.
- Core BP: **positive regulation of conidium formation** (GO:0075307), **conidium
  formation** (GO:0048315), **conidiophore/sporocarp development** (GO:0000905),
  **regulation of transcription by RNA Pol II** (GO:0006357) — ACCEPT.
- Non-core (real): ST/secondary-metabolite regulation (GO:0010913, GO:1900376),
  autolysis (GO:0001896), starvation response IEP (GO:0042594) — KEEP_AS_NON_CORE.
- Over-annotation: **sterigmatocystin biosynthetic process** (GO:0045461) — brlA is
  a *regulator*, not part of ST biosynthesis; the regulation term GO:0010913 already
  captures the real relationship. Also the IBA **response to starvation**
  (GO:0042594, involved_in) is a phylogenetic over-propagation from SGD paralogs.
