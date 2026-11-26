# PA0328 (AaaA) — review notes

Locus PA0328, UniProt Q9I6G3, *Pseudomonas aeruginosa* PAO1. 647 aa, unreviewed.

## Provider deep research is absent, and why

`just deep-research PSEAE PA0328 --provider perplexity` reports `Provider 'perplexity' not
available. Available: asta, openscientist, claude_code`. The `asta` run completed but retrieved
nothing about this gene: all 20 papers it returned were database and annotation-tooling papers
(Avian Immunome DB, WormBase, FlyBase, LIPID MAPS, a network-pharmacology study of saffron), and
the same pool came back for three other unrelated *P. aeruginosa* genes requested in the same
batch. The retrieval had matched the prompt template's own boilerplate ("Gene Research for
Functional Annotation", "user-friendly interface for extracting genetic information") rather than
the gene, so the output was deleted rather than committed as research. Nearly identical hit lists
across four unrelated genes is the tell. An `openscientist` run was attempted and did not finish
within the time available.

What follows is therefore my own reading of the primary literature and the record, with provenance
on every assertion, per the project rule for when deep research fails.

## Identity: PA0328 is AaaA

The entry has no gene name — only `OrderedLocusNames=PA0328 {ECO:0000313|EMBL:AAG03717.1}`, which
is an unreviewed submitter import — and its protein name is the PROSITE-derived
"Autotransporter domain-containing protein". The primary paper names it:

[PMID:22927813 "Hence, we have assigned PA0328 with the name AaaA, for arginine-specific
autotransporter of P. aeruginosa."]

Full text is cached and available, which matters for everything below.

## Architecture

Three-domain autotransporter, with the parts in the expected places:

- signal peptide 1..22 (`FT   SIGNAL          1..22`)
- passenger domain carrying the catalytic site, N-terminal
- `FT   DOMAIN          344..647` autotransporter β-barrel, C-terminal
  (`DR   PROSITE; PS51208; AUTOTRANSPORTER; 1.`, `DR   NCBIfam; TIGR01414; autotrans_barl; 1.`)

The paper states the general rule and locates the active site accordingly:

[PMID:22927813 "The passenger domains of ATs characteristically bear the functional active site."]

Peptidase assignment is M28, by two independent signatures
(`DR   InterPro; IPR007484; Peptidase_M28.`, `DR   Pfam; PF04389; Peptidase_M28; 1.`,
`DR   InterPro; IPR045175; M28_fam.`), and the paper places it in the M28C / M28.005 subfamily
alongside *Streptomyces griseus* aminopeptidase A and *Vibrio proteolyticus* leucine
aminopeptidase.

## The activity: arginine-specific, metal-dependent aminopeptidase

[PMID:22927813 "AaaA is an AT that is tethered to the surface of P. aeruginosa and specifically
removes amino terminal arginine from peptides."]

The specificity claim is not merely sequence-based. The paper reports conserved active-site
residues and then mutates them:

[PMID:22927813 "Predicted active site catalytic and ligand binding site residues are 100%
conserved between AaaA and the other members of the M28.005 family (Figure 3A,B), strongly
suggesting that AaaA has an aminopeptidase activity."]

[PMID:22927813 "AaaA is a member of the M28 family of aminopeptidases and site directed
mutagenesis confirms that predicted active site residues of AaaA contribute to arginine
aminopeptidase activity."]

The residues mutated are H100, D102, E147, E149, D176, D277, plus a surface-loop control (G89).
UniProt's own `FT BINDING` features sit at 100, 115, 147, 148, 176 and 277 — four of the six
positions agree exactly. The two that differ (102 vs 115, 149 vs 148) are not a uniform offset, so
this is not a numbering-frame discrepancy; the record's features come from a rule predicting metal
ligands while the paper's list is "catalytic and ligand binding site residues", and the two sets
need not coincide. Not recorded as a defect: nothing here shows either side wrong.

M28 is a co-catalytic metallopeptidase clan, so the metal dependence and the aminopeptidase
chemistry are the same claim. `GO:0070006` metalloaminopeptidase activity is the GO class for
exactly that conjunction, and OLS confirms it is a child of both `GO:0004177` aminopeptidase
activity and `GO:0008235` metalloexopeptidase activity — the two terms GOA currently carries
separately on this gene.

**GO has no arginine-specific aminopeptidase term.** Checked rather than assumed, and with a
positive control so the negative is readable: a search for "aminopeptidase activity" returns 8
classes including the residue-specific children `GO:0016285` alanyl aminopeptidase activity,
`GO:0004230` glutamyl aminopeptidase activity and `GO:0004239` initiator methionyl aminopeptidase
activity, while a search for "arginine aminopeptidase activity" returns nothing. So the pattern
exists in GO for other residues and is absent for arginine. That is an ontology gap, recorded as a
`proposed_new_terms` entry rather than forced into an ill-fitting id.

## Localisation

Shown directly, in two ways. Mutant proteins were fractionated
([PMID:22927813 "Two of these were localised to the outer membrane (E147 and E149, Figure 2)."]),
and the paper's conclusion states the surface disposition:

[PMID:22927813 "Clearly AaaA is located on the surface of P. aeruginosa, probably by virtue of its
AT domain, and has arginine-specific aminopeptidase activity that can be used to release arginine
to provide a growth fitness advantage."]

`GO:0019867` outer membrane (IEA from `IPR006315`) is therefore independently supported by data,
not only by the signature.

## The biological role: nitrogen scavenging from N-terminally-arginine peptides

The decisive growth experiment:

[PMID:22927813 "Interestingly, and in support of our hypothesis, when the peptide Arg-Gly-Asp was
included in MMP as the sole source of carbon and nitrogen, the ΔaaaA mutant could not grow
although the wild type P. aeruginosa PAO1 grew well"]

A defined tripeptide, a defined deletion, growth abolished and restored by the wild type. This is
the cleanest statement of what the enzyme is for.

## `GO:0048870` cell motility has no basis in the cited paper

This is the batch's main finding and it is worth setting out in full, because the full text is
available and settles it rather than leaving a suspicion.

GOA carries `GO:0048870` cell motility on PA0328 by **IDA** from PMID:22927813. The paper contains
no motility assay of any kind. Counting every motility-family word in the cached full text:

| word | occurrences |
|---|---|
| `motilit` | 2 |
| `swarm` | 2 |
| `swimming` | 2 |
| `twitch` | 2 |
| `motile` | 0 |
| `flagell` | 0 |
| `chemotax` | 0 |
| `pili` / `pilus` | 0 |

The counts of two are the cached body's own duplication, not two independent mentions: every one
of them lies in a **single** sentence, and that sentence is about a different protein —

[PMID:22927813 "One of these, the esterase EstA, functions to alter the levels of extracellular
rhamnolipids, modulates twitching, swimming and swarming motility and influences the formation and
architecture of biofilms [35], [36]."]

EstA is another *P. aeruginosa* autotransporter, introduced in this paper's own background as a
contrast to AaaA, and even that claim is attributed to references [35] and [36] rather than
reported here. There is no flagellum, no pilus, no swarm plate and no chemotaxis experiment in the
paper.

The absence of a flagellar or pilus word anywhere is what makes this safe to assert. A motility
phenotype cannot be reported without naming the appendage or the assay, so the possibility that
the claim sits in a part of the paper I did not read does not arise — I read all of it, and the
vocabulary is simply not there.

Two further things follow:

- A **repoint to EstA on this reference would also be wrong.** The EstA motility claim is cited to
  [35],[36]; this paper is not its source. So the correction is a row deletion, not a transfer.
- Biofilm is the same shape and is *not* annotated, correctly: biofilm appears only as Discussion
  speculation ([PMID:22927813 "We are currently investigating the biofilm formation of the ΔaaaA
  mutant in vitro"]), with no assay. Whatever produced the motility row did not produce a biofilm
  row, which argues for a single mis-keyed annotation rather than a systematic reading of the
  background section.

## Is `GO:0055085` transmembrane transport right for a self-translocator?

Worth asking explicitly, because the row is an inference (`GO_REF:0000108`) computed from
`GO:0015474` autotransporter activity rather than an independent claim, and because "transports
itself" looks like the kind of necessity-versus-participation case the project rules warn about.

It holds. `GO:0015474` autotransporter activity is defined as "Transports a passenger protein from
the periplasm to the external milieu; the passenger protein and the porin are the N- and C-terminal
regions of the same protein, respectively" — so the gene product's β-barrel *is* the translocator
that does the work, and the passenger crossing the outer membrane is a real transmembrane transport
event. The protein is not merely required for a transport its partners perform; it performs it. The
unusual part is only that substrate and transporter are one polypeptide, which the GO term's own
definition anticipates.

## Open questions

- Which peptides are the physiological substrates in an infected wound? Arg-Gly-Asp is a defined
  reagent, not a host peptide, and the paper's model is explicitly speculative about the
  anaerobic-arginine route.
- Whether the released arginine is consumed by the bacterium, by host iNOS, or both. The paper
  raises the competition but does not resolve it
  ([PMID:22927813 "If only some of the released arginine is utilized by"] — the sentence continues
  into an unresolved model).
