# GZMM (granzyme M / Met-ase, UniProtKB:P51124) — curation notes

## Provenance of this file

No `-deep-research-*.md` file exists for GZMM. Only `openscientist` and `claude_code` are registered
as providers in this environment, and the one openscientist run attempted in this batch (for GZMK) was
stopped by the session's background limit without producing output. No provider file was written, and
this file is deliberately **not** named as one. These are my own notes from the cached publications,
the UniProt record, QuickGO and OLS, with provenance for each assertion.

## What the protein is

A serine protease of the granules of NK cells and other large granular lymphocytes, named for its
specificity: chymotrypsin-like in fold but cutting after methionine or leucine [PMID:20406824
"Granzyme M (GzmM) is a chymotrypsin-like serine protease that preferentially cuts its substrates
after Met or Leu."]. Its expression pattern separates it from the other granzymes — it is
constitutive in NK cells and barely detectable in activated T cells — and the activity was localised
to the granules in the paper that cloned it [PMID:8245461 "Met-ase activity detected in whole cell
lysates of cytotoxic lymphocytes was associated with the cytoplasmic granules of these cells."].

## Two substrate programmes, different in kind

**Destructive, and self-sufficient.** Granzyme M cleaves the actin-plasma membrane linker ezrin and
alpha-tubulin [PMID:18523284 "GrM directly and efficiently cleaved the actin-plasma membrane linker
ezrin and the microtubule component alpha-tubulin"], disturbing tubulin polymerisation and
disorganising the microtubule network [PMID:18523284 "GrM disturbed tubulin polymerization dynamics in
vitro and induced microtubule network disorganization in tumor cells in vivo."]. These cleavages need
no caspases [PMID:18523284 "These cleavage events occurred independently of caspases or other cysteine
proteases."]. Nucleophosmin is a third substrate, identified through the SERPINB4 work below.

**Permissive rather than executing.** Granzyme M removes four residues from survivin [PMID:20406824
"GzmM hydrolyzes Survivin at Leu-138 to remove the last four C-terminal residues."], which
destabilises the survivin-XIAP complex so that XIAP is degraded and caspase activation is amplified
[PMID:20406824 "Survivin cleavage by GzmM abolishes the stability of the Survivin-XIAP complex and
enhances XIAP hydrolysis, which amplifies caspase-9 and 3 activation of target tumor cells."]. So the
death it causes is caspase-dependent [PMID:20406824 "Our previous work demonstrated that GzmM induces
caspase-dependent apoptosis."] even though its own proteolysis is not, and it never cleaves a caspase.

That split is the reason for two of this review's decisions: `GO:0006915` apoptotic process is
**accepted** here, unlike on granzyme H, because the route is established; and `GO:0051604` protein
maturation is kept but marked **non-core**, because nothing granzyme M cleaves is matured — the one
activation it causes is two steps away and performed by other proteins.

## The inhibitor

SERPINB4 is the only known intracellular inhibitor of granzyme M [PMID:21857942 "we show that SERPINB4
formed a typical serpin-protease SDS-stable complex with both recombinant and native human GrM"]. The
reactive-centre loop mutation experiment is also, incidentally, independent evidence for the Met-ase
specificity: the serpin is itself cleaved after a leucine [PMID:21857942 "Mutation of the P2-P1-P1'
triplet in the SERPINB4 reactive center loop completely abolished complex formation with GrM and
N-terminal sequencing revealed that GrM cleaves SERPINB4 after P1-Leu."]. SERPINB4 blocks cleavage of
the macromolecular substrates [PMID:21857942 "SERPINB4 abolished cleavage of the macromolecular GrM
substrates α-tubulin and nucleophosmin."] and, overexpressed in tumour cells, blocks the death
[PMID:21857942 "Overexpression of SERPINB4 in tumor cells inhibited recombinant GrM-induced as well as
NK cell-mediated cell death"]. Since SERPINB4 is highly expressed by squamous cell carcinomas, this is
a plausible tumour escape route. No GO annotation on this gene records the relationship, and there is
no molecular-function term for being inhibited, which is why the `GO:0005515` row that carries the
interaction is removed under the protein-binding policy rather than re-levelled.

## Two annotations proposed

- `GO:0140507` granzyme-mediated programmed cell death signaling pathway. Comparator check with a
  working positive control: granzyme A, granzyme B and perforin all carry it in their own GOA files and
  granzyme K carries it by IBA; granzyme M and granzyme H are the two that lack it, and both are the
  less-studied granzymes rather than exceptions in kind. Note the repair here differs from granzyme H's
  in the same batch, where the existing apoptotic-process rows were re-levelled onto this term instead;
  here apoptotic process is correct and kept, so the pathway term is added beside it. Checked in the
  ontology: the two do not entail each other.
- `GO:0044194` cytolytic granule. The record's only locations are extracellular region and a membrane
  row this review marks over-annotated; where the protein is *kept* is missing, even though its own
  cloning paper measured it. Every other granule effector in this project carries the term.

## Reference-level note

Two of the three papers that establish what granzyme M does — the ezrin/tubulin study and the survivin
study — are cited by UniProt's `CC:FUNCTION` but by no GOA row on this gene. That is a curation gap
rather than a defect, and it is why this review adds both to the reference list.
