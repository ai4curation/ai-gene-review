# GZMH (granzyme H, UniProtKB:P20718) — curation notes

## Provenance of this file

No `-deep-research-*.md` file exists for GZMH. Only `openscientist` and `claude_code` are registered
as providers in this environment (`falcon` and `perplexity` both fail immediately), and the one
openscientist run attempted in this batch, for GZMK, was stopped by the session's background limit
without producing output. No provider file was written, and this file is deliberately **not** named as
one. These are my own notes from the cached publications, the UniProt record, QuickGO and OLS, with
provenance for each assertion.

## What the protein is

A chymotrypsin-like serine protease stored in the cytolytic granules of NK cells, where it is
expressed constitutively rather than on activation [PMID:23269243 "Granzyme H (GzmH) is constitutively
expressed in NK cells and induces target cell death"]. Its specificity is the narrowest of the human
granzymes and was resolved structurally: a Thr-Gly-Gly triad in the S1 pocket selects bulky aromatic
residues at P1 [PMID:22156497 "The Thr(189), Gly(216), and Gly(226) specificity triad in the S1 pocket
of GzmH defines its preference for bulky, aromatic residues (Tyr and Phe) at the P1 position"], and an
RKR motif unique to this granzyme adds a second requirement on the leaving side of the bond
[PMID:22156497 "an unusual RKR motif (Arg(39)-Lys(40)-Arg(41)), conserved only in GzmH, helps define
the S3' and S4' binding regions, indicating the preference for acidic residues at the P3' and P4'
sites"]. Disrupting either the motif or those substrate residues abolishes activity, so the
requirement is a property of the enzyme and not an artefact of the peptides tested.

Activity inside the killer cell is restrained by SERPINB1, which forms a covalent complex with it
[PMID:23269243 "we identified SERPINB1 as a potent intracellular inhibitor for GzmH"].

## The one paper that gave it a function

Granzyme H was an orphan granzyme until Andrade et al. showed it cleaving two adenoviral proteins in
infected cells [PMID:17363894 "granzyme H (gzmH), an orphan granzyme without known function, directly
cleaves the adenovirus DNA-binding protein (DBP), a viral component absolutely required for viral DNA
replication"]. Two findings, and they are different in kind:

1. Cleaving the viral DNA-binding protein cuts viral DNA replication, and the causal link was isolated
   with an engineered virus carrying a granzyme H-resistant version of that protein [PMID:17363894
   "This virus demonstrated that gzmH directly induces an important decay in viral DNA replication."].
   That control is what separates a consequence of the cleavage from a correlation.
2. Cleaving the adenoviral 100K protein removes an inhibitor of granzyme B [PMID:17363894 "gzmH also
   cleaves the adenovirus 100K assembly protein, a major inhibitor of gzmB, and relieves gzmB
   inhibition"]. So granzyme H can act by restoring another protease rather than by killing anything
   itself — the one case in the granule module where two granzymes are not merely parallel.

The authors frame it as the first evidence of its kind [PMID:17363894 "These results provide the first
evidence that granzymes can mediate antiviral activity through direct cleavage of viral substrates"].

## Two annotations proposed, and why both

- `GO:0051607` defense response to virus. Participation is direct: granzyme H does the cleaving.
  Comparator check with a working positive control — of the seven granule effectors reviewed in this
  project, perforin carries `GO:0051607` three times in its own GOA file and the six granzymes plus
  granulysin carry it zero times. The absence is best explained by this gene's annotation state (twelve
  GOA rows in total, and an "orphan granzyme" history) rather than by a convention: perforin's rows
  rest on knockout mice failing to clear a virus, which is necessity evidence, where granzyme H's rest
  on direct cleavage of the viral substrate.
- `GO:0045071` negative regulation of viral genome replication. Checked in the ontology rather than
  assumed: the ancestors of `GO:0045071` run through regulation of viral genome replication, viral life
  cycle and viral process, and `GO:0051607` is **not** among them, so the two are not redundant. This
  is the better-controlled of the two findings, because of the resistant-substrate virus.

## A UniProt citation that does not match its statement

UniProt's `CC:FUNCTION` carries "Participates in the antiviral response via direct cleavage of several
proteins essential for viral replication." evidenced to `PubMed:22156497` and `PubMed:23269243`.
Neither abstract mentions a virus: the first is the crystal-structure and specificity study, the second
identifies SERPINB1. The sentence describes PMID:17363894, which that record does not cite. Located by
a PubMed title search and read at abstract level; recorded as a `WRONG_REFERENCE` source defect at
`PROBABLE` with `requested_change: CHECK`, since both cited entries are cached abstract-only and their
full texts cannot be ruled out from here.

## Decisions worth recording

- The two `GO:0006915` apoptotic-process rows are `NAS` from the 1990 cloning papers, whose own words
  are a postulate [PMID:2193684 "in keeping with the postulated involvement in cytolysis, transcripts
  were detected only in cytotoxic cells"]. Re-levelled to `GO:0140507`, which this gene lacked. That
  replacement is a **lateral** correction, not a refinement: checked in the ontology, `GO:0140507` sits
  under programmed cell death and signaling, not under apoptotic process. It also avoids committing the
  gene to the apoptotic route, which its own literature does not establish — no host substrate of
  granzyme H is known, so how it kills is open.
- `GO:0051604` protein maturation (IBA) is kept but marked **non-core**, unlike on granzyme K, granzyme
  A and granzyme B. Every established granzyme H substrate is destroyed rather than matured; the one
  case that looks like maturation is indirect, since relieving the 100K inhibition restores granzyme B
  without cleaving it.
- `GO:0016020` membrane (HDA, NK membrane proteome) is marked over-annotated, as the same row was on
  granzyme B. `TOO_GENERAL` does not apply: that action needs a more specific membrane term asserted
  elsewhere in the review, and this gene has none.
