# mqo2 (PA4640) — review notes

UniProt Q9HVF1, reviewed, 507 aa. *Pseudomonas aeruginosa* PAO1. Synonym `mqoB`.

## Provider deep research is absent, and why

`perplexity` is not available in this environment (`Available: asta, openscientist, claude_code`).
The `asta` run returned 20 papers, none about this gene or even about *Pseudomonas* — the same pool
of database and annotation-tooling papers came back for three other unrelated genes in the same
batch, because the retrieval matched the prompt template's boilerplate rather than the gene. That
output was deleted rather than committed. An `openscientist` run was attempted and did not finish
in the time available. What follows is my own reading, with provenance.

## Identity is explicit in the primary paper

The paper worked in strain ATCC 17933 and maps its gene to the PAO1 locus in its closing sentence:

[PMID:12480887 "mqo of P. aeruginosa ATCC 17933 corresponds to mqoB (PA4640) of the P. aeruginosa
PAO1 genome project."]

The entry's own `GN` line carries `Synonyms=mqoB; OrderedLocusNames=PA4640`, so the two sides agree
and no inference is needed to connect paper to accession.

## Family and reaction

Reviewed entry, and the family assignment is from curated systems rather than a loose signature:

- `DR   HAMAP; MF_00212; MQO; 1.`
- `DR   NCBIfam; TIGR01320; mal_quin_oxido; 1.`
- `DR   InterPro; IPR006231; MQO.`
- `DR   Pfam; PF06039; Mqo; 1.`

The curated reaction is `(S)-malate + a quinone = a quinol + oxaloacetate` (RHEA:46012, EC 1.1.5.4),
FAD as cofactor, and the pathway statement puts it at "tricarboxylic acid cycle; oxaloacetate from
(S)-malate (quinone route): step 1/1".

Note what the evidence tags on all of that say: every one is `ECO:0000255|HAMAP-Rule:MF_00212`. The
record's functional content is entirely rule-derived.

## The experimental evidence, which the record does not carry

PMID:12480887 provides both an activity measurement and a mutant phenotype in this species:

[PMID:12480887 "A mutant with an interrupted putative mqo gene, in which malate:quinone
oxidoreductase (MQO), an enzyme involved in the citric acid cycle/glyoxylate cycle, was defective,
showed a severe growth defect on ethanol and was unable to grow on acetate."]

[PMID:12480887 "Complementation of the mutant by the wild-type allele of the mqo gene restored
wild-type behaviour. The wild-type expressed the dye-dependent MQO and NAD(P)-dependent malic
enzymes (MEs)."]

So: deletion, phenotype, complementation, and a measured dye-dependent activity in the wild type.
The paper also establishes the specificity negatively —

[PMID:12480887 "However, an NAD-dependent malate dehydrogenase activity could not be detected."]

— which matters, because it separates the quinone-dependent enzyme (`GO:0008924`) from the
NAD-dependent malate dehydrogenase (`GO:0016615`) that the same metabolic step can be carried by in
other organisms. *P. aeruginosa* has the quinone route and not the NAD one.

And the paper notes its own novelty:

[PMID:12480887 "To the authors' knowledge, this is the first time that a specific mutant MQO
phenotype has been observed, caused by the inactivation of a gene encoding MQO activity."]

## UniProt has the sequence from that study but not its findings

The entry's reference list is two items: an EMBL submission (`Submitted (JUL-2002)`, AY129296) and
the PAO1 genome paper (PMID:10984043). **PMID:12480887 is not cited anywhere in the record.**

The submission date is the tell: AY129296 was deposited in July 2002 and the paper appeared in
December 2002, so the entry carries that group's sequence deposit while missing the characterisation
it was deposited for. The consequences are visible on the record:

- the protein name is "**Probable** malate:quinone oxidoreductase 2"
- `PE   3: Inferred from homology`
- every CC statement is HAMAP-rule evidence

all of which understate what has been shown in this species. Filed as a `MISSING_STATEMENT` defect
against UniProt. Confidence is `PROBABLE` rather than `CONFIRMED` for one honest reason: the work
was done in ATCC 17933 while the entry is PAO1, and whether UniProt treats a different strain of
the same species as "evidence at protein level" for this entry is their editorial call, not mine.
The paper's own locus mapping is what makes the request worth filing at all.

## `GO:0016614` is TOO_GENERAL here, not REMOVE — and the contrast with soxA is the point

The ARBA row `GO:0016614` oxidoreductase activity, acting on CH-OH group of donors looked at first
like the same defect found on *soxA* in batch 4, where `GO:0016614` was **removed** as the wrong
oxidoreductase branch. It is not. Checked in OLS rather than assumed:

- `GO:0008924`'s ancestors are `GO:0016901` (CH-OH donor, quinone acceptor) → **`GO:0016614`** →
  `GO:0016491`. So `GO:0016614` is a true ancestor of the accepted activity.
- soxA's accepted activity `GO:0008115` sarcosine oxidase sits under `GO:0016645` (CH-**NH** donors)
  instead, with `GO:0016614` nowhere among its ancestors — which is why that row was a wrong-branch
  removal.

Same term, opposite verdicts, decided by looking rather than by analogy. Malate oxidation does act
on a CH-OH group; sarcosine oxidation does not.

The three merged *P. putida* siblings reached the same conclusion independently: `mqo1`, `mqo2` and
`mqo3` all mark `GO:0016614` `TOO_GENERAL` and all `ACCEPT` `GO:0008924` and `GO:0006099`. This
review follows them, which is unanimity rather than a majority.

## The family review's open question, which this gene answers

`interpro/panther/PTHR43104/PTHR43104-review.yaml` leaves the `GO:0005737` cytoplasm node
(PTN000354057) unresolved, with the stated reason that "no reviewed TCA member receives it" — only
human FOXRED1, which treats the term as too general. PSEAE mqo2 is a reviewed TCA-cycle member that
*does* receive it, so the gap the family review recorded is now fillable.

I have not edited the family review here. The cross-check only conflicts when a family review scopes
a term over a gene whose review removes it, and this review keeps the row, so nothing forces a
shared-file edit in this PR. The observation belongs in a family-review pass.

On the row itself: the donor list is eukaryotic (fly, mouse, rat, yeast, *Arabidopsis*, four human
accessions) and contains no MQO, so this is a deep node asserting a compartment rather than a
transfer from a characterised malate:quinone oxidoreductase. "Cytoplasm" is nonetheless true of a
bacterial MQO's catalytic face, so the row is kept rather than pruned — but it is as coarse as the
node that produced it. The reaction needs a membrane quinone, so the enzyme has to work at the inner
membrane, and nothing in the record or the paper localises it: there is no `SUBCELLULAR LOCATION`
line on the entry at all, and the dye-dependent assay does not say which fraction it was in. That
is a genuine gap, not a curation one.
