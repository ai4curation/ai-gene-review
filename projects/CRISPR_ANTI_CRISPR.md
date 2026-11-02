---
title: "CRISPR-Cas immunity and anti-CRISPR counter-defence"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [BPZF4]
genes: [AcrF8]
autolink_gene_symbols: false
---

# CRISPR-Cas immunity and anti-CRISPR counter-defence

**Two module documents, curated as a matched pair: the host pathway
([crispr_cas_adaptive_immunity](../modules/crispr_cas_adaptive_immunity.html)) and
the phage counter-defence that targets it
([anti_crispr_suppression](../modules/anti_crispr_suppression.html)). Keeping them
separate is the substantive modelling decision — each is reusable alone, and the
pairing makes visible that anti-CRISPR mechanisms are individuated by *which step
of the host pathway they attack*, not by homology, because they have none.**

## Why two modules rather than one

Suppression could have been an optional regulatory part of the host module. It is
not, for three reasons:

1. **Different organisms.** The host module is bacterial and archaeal
   (`NCBITaxon:2`, `NCBITaxon:2157`); the suppression module is viral
   (`NCBITaxon:10239`), acting in `GO:0030430` host cell cytoplasm. A single
   module would have to assert both taxon scopes at once.
2. **Different GO branches.** The host pathway sits under `GO:0099048` CRISPR-cas
   system → `GO:0099046` clearance of foreign intracellular nucleic acids.
   Suppression sits under `GO:0098672` → `GO:0052031` symbiont-mediated
   perturbation of host defense response. These are not parent and child; they
   are assertions about two different agents.
3. **Independent reuse.** The host module is the right target for curating any
   *cas* locus; the suppression module is the right target for any phage genome.
   Folding one into the other would make each half unusable on its own.

The cost is that `connections` are document-scoped, so no edge can be drawn from
an Acr node to the host node it inhibits. Each suppression part names its host
target in prose instead, and the correspondence is tabulated below.

## The attack surface, step by step

Every characterised anti-CRISPR class maps onto exactly one step of the host
pathway. That is the organising claim of the pair, and it is falsifiable: a
mechanism that attacked no step of the host module would mean the host module is
missing a part.

| Host step (host module) | Suppression part | Mechanism | Exemplar |
|---|---|---|---|
| Adaptation (Cas1–Cas2 integration) | *none curated* | — | — |
| crRNA biogenesis | enzymatic subversion | guide-RNA cleavage | AcrVA1 (`UniProtKB:A0A5H1ZR47`) |
| Interference — target recognition | recognition blockade | Csy-complex and crRNA binding | AcrIF8 (`UniProtKB:H9C181`) |
| Interference — target recognition | recognition blockade | DNA mimicry at the PAM site | AcrIIA4 (`UniProtKB:A0A247D711`) |
| Interference — Cas3 recruitment | nuclease neutralisation | Cas3 sequestration (`GO:0140311`) | AcrF3-family (`UniProtKB:L7P7R7`) |
| Interference — Cas9 cleavage | nuclease neutralisation | HNH-domain occlusion | AcrIIC1 (`UniProtKB:A0A2D0TCG3`) |
| Interference — cOA signalling | enzymatic subversion | cOA ring nuclease | AcrIII-1 (`UniProtKB:Q8QL27`) |

Two asymmetries in that table are worth reading as biology rather than as gaps in
the curation.

**Nothing attacks adaptation.** Every characterised Acr acts on biogenesis or
interference — the stages that happen during the current infection. Blocking
adaptation would spare the phage's descendants but not the phage, which is the
wrong incentive; killing the effector is what saves the infecting genome. This is
a prediction, not just an absence: an Acr that blocked Cas1–Cas2 integration
should be expected in temperate phages and prophages, where the element persists
in a lineage whose future immunity it has an interest in, rather than in lytic
ones.

**Cas3 sequestration has no class 2 counterpart.** It cannot have one. In class 1
systems recognition and destruction live in different proteins, so there is a
recruitment step to intercept; in class 2 they live in the same protein, and the
equivalent attack has to be domain occlusion (AcrIIC1) instead. The mechanism
repertoire is constrained by the host architecture, which is an argument for
modelling the effector classes as variants of one slot rather than as separate
modules — the variants are what make the constraint visible.

## Stoichiometric versus catalytic inhibition

The module separates blockers from enzymes, and the distinction does real work.
AcrIF8, AcrIIA4, AcrF3 and AcrIIC1 each occupy their target and must therefore be
present in molar excess of it. AcrVA1 and AcrIII-1 are enzymes: they destroy the
crRNA guide and the cOA messenger respectively, and one molecule can disarm many
targets. This predicts different expression requirements — and bears directly on
the Aca autoregulatory loop, since a catalytic Acr can tolerate much earlier
repression than a stoichiometric one.

## The Aca feedback loop

`aca` genes are co-transcribed with `acr` genes from a shared promoter, and the
Aca repressor then shuts that promoter down: the inhibitor's own expression
produces the switch that turns it off. The module records this as a closed loop
(`recognition_blockade → aca_autoregulation → recognition_blockade`), which the
renderer's feedback check confirms. Pectobacterium phage ZF40 supplies both
halves from one locus — `acrIF8` (`UniProtKB:H9C181`, reviewed under
`genes/BPZF4/AcrF8/`) and `aca2` (`UniProtKB:H9C180`) — which is why it is the
exemplar for the regulatory part.

## Ontology gaps

Six knowledge gaps are recorded across the two modules. Three are ontology gaps
that between them make the defining properties of this entire domain
unrepresentable in GO:

- **No molecular function for guide-RNA-directed recognition.** Cas9 is annotated
  `GO:0004520` DNA endonuclease activity and the Cascade complex `GO:0003690`
  double-stranded DNA binding — terms that do not distinguish a programmable
  RNA-guided nuclease from any unguided one. The single most consequential
  property of every Cas effector is invisible.
- **No molecular function for cyclic oligoadenylate synthase activity.** Cas10's
  Palm domain output cannot be stated. `GO:0001730` 2'-5'-oligoadenylate
  synthetase activity is the metazoan interferon enzyme — different chemistry,
  different product — and must not be reused here. The matching gap in the
  suppression module is the absence of a ring nuclease term for degrading the
  same messenger.
- **No molecular function for mimicry-based competitive inhibition.** `GO:0140311`
  protein sequestering activity genuinely fits AcrF3, and `GO:0140721` nuclease
  inhibitor activity fits AcrIIC1 — this page previously claimed nothing in GO
  covered the latter, which was wrong. What remains unexpressible for AcrIIC1 is
  only the domain-level specificity, better pursued as an extension of
  `GO:0140721` than as a new term. Mimicry is the real gap, and the reviews now
  draft a term for it.

Where no term exists, these modules assert no id. That is a deliberate choice: an
omitted id says "not established", whereas a plausible-looking wrong id says
something false in a field other tooling will believe.

The remaining gaps are curation-shaped. Most characterised Acr proteins have no
reviewed UniProt entry, and two of the exemplars used here have published
structures bound to their targets yet are named only "Phage protein" (`L7P7R7`)
and "Anti-CRISPR protein" (`A0A2D0TCG3`). InterPro has caught up faster, with
mechanism-bearing family names such as IPR049085 "Cas3 inhibitor AcrF3-like" —
which is why both modules ground families in InterPro and leave the member labels
as fetched.

## Status and next steps

Both modules validate and render with no leaf-grounding gaps. **All 35 UniProt
groundings now have gene reviews** — the 33 added in this batch plus the two that
existed. Nine are `DRAFT` rather than `COMPLETE`, deliberately: the Cascade and
class 2 sets each turn on a judgement call that wants a second opinion rather
than on anything mechanical.

Five ontology terms are drafted across the reviews, each argued as a missing
member of an existing series rather than a one-off: cyclic oligoadenylate
synthase activity and cyclic oligoadenylate binding (type III), guide
RNA-directed target recognition and guide RNA-dependent nucleic acid
endonuclease activity (kept as a complementary pair, since a catalytically dead
but guide-loaded effector retains the first and loses the second), and nucleic
acid mimicry-based competitive inhibitor activity (converged on independently by
three sequence-unrelated anti-CRISPR families). A CRISPR RNA-guided surveillance
complex CC term is requested too, on the finding that GO's entire CRISPR
vocabulary is biological-process terms.

Reviewing the exemplars corrected the modules in eight places, which is the
argument for doing it: Cas2 does have a molecular function, Cas3's asserted
function was the wrong one of its two activities, Cas12a's GOA term imports
DNase I chemistry it does not have, AcrF2's blocked surface *is* established and
makes it the strongest cross-class mimicry case, AcrVA1's catalyst is not
established enough to be a family membership criterion, `GO:0140721` covers
AcrIIC1, both complexes can be grounded at `GO:1990904`, and the AcrIII-1
accession was resolvable after all.

The remaining work is curation of the drafted terms with GO, and the open
questions each review records.

Neither module has a `-deep-research-*.md` report, and neither do the gene
reviews: no provider API keys are configured in this environment, so findings
went to `GENE-notes.md` files with verbatim `[PMID:x "..."]` provenance instead
of a fabricated provider file. The QC panel reports the absence.
