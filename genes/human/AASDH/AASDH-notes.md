# AASDH (ACSF4-U26, beta-alanine-activating enzyme) — review notes

PAINT no-IBA project review, using the `affinage` deep-research provider
(`AASDH-deep-research-affinage.md`, gates passed) plus UniProt Q4L235, the GOA TSV and the
primary literature.

## One annotation, and it is wrong

AASDH's entire GO record is **a single annotation**: `GO:0006631 fatty acid metabolic process`,
ISS. Resolving its WITH/FROM shows the problem immediately — the source is **`UniProtKB:Q4G176`,
which is ACSF3, a human *paralog*, not an ortholog.**

ACSF3 is a genuine fatty-acid enzyme: malonyl-CoA synthetase, which
"catalyzes the initial reaction in intramitochondrial fatty acid synthesis, by activating
malonate and methylmalonate". Fatty acid metabolism is correct *for ACSF3*.

AASDH is not that enzyme. It is a **β-alanine-activating enzyme**:

- [PMID:24467666, "We conclude that ACSF4-U26 is a β-alanine-activating enzyme"]
- Near-absolute specificity —
  [PMID:24467666, "Competition experiments with various amino acids indicated that the reaction was
  almost specific for β-alanine, and a KM of ~ 5 μm was calculated for this
  reaction."]
- Mechanism requires the phosphopantetheine arm —
  [PMID:24467666, "The bond was
  not formed in a point mutant lacking the phosphopantetheine attachment site."]

**β-alanine is a β-amino acid, not a fatty acid.** So the one annotation this gene has
describes its paralog's substrate, not its own. The shared basis is the ATP-dependent
AMP-binding adenylation fold and the family naming ("Acyl-CoA synthetase family member 4" vs
"member 3") — a textbook `WRONG_ORTHOLOG_OR_PARALOG` transfer.

Note the same assumption has leaked into UniProt's keywords, which include `Fatty acid
metabolism` and `Lipid metabolism` despite UniProt's own FUNCTION line describing β-alanine
activation. Worth flagging upstream.

**Action: `REMOVE`.** This is one of the sanctioned uses — a demonstrably wrong sequence-based
inference, argued on biological grounds against direct enzymology of the gene itself. Removing
it leaves AASDH with zero annotations, so three `NEW` terms are proposed to replace it with what
the enzymology actually supports.

## What AASDH actually does, and what remains unknown

Established biochemistry (mouse recombinant enzyme, PMID:24467666):

1. ATP-dependent activation of β-alanine → covalent thioester with the enzyme's own
   phosphopantetheine group. UniProt states it directly
   [file:human/AASDH/AASDH-uniprot.txt, "CC   -!- FUNCTION: Covalently binds beta-alanine in an ATP-dependent manner to"].
2. Domain architecture matches: an adenylation domain plus a **Carrier domain (553–630)** —
   the phosphopantetheine attachment point — plus ATP-binding sites.

What is **not** known, and must not be invented: the physiological acceptor. The paper is
careful about this — transfer onto thiols was observed but judged
[PMID:24467666, "physiologically irrelevant"], and UniProt says the product is transferred "to
an, as yet, unknown acceptor". So no downstream pathway or process annotation is proposed beyond
β-alanine metabolism itself.

Proposed:

| Term | Aspect | Why |
|---|---|---|
| `GO:0016878` acid-thiol ligase activity | MF | ATP-dependent formation of a thioester bond to a carrier thiol — exactly the demonstrated chemistry |
| `GO:0031177` phosphopantetheine binding | MF | carrier domain, and the point mutant that loses the attachment site loses the reaction |
| `GO:0019482` beta-alanine metabolic process | BP | the substrate is β-alanine with near-absolute specificity |

`GO:0005524 ATP binding` is deliberately **not** proposed despite four annotated ATP-binding
sites: it adds little over the ligase term, which already entails ATP dependence.

## Affinage assessment

Gates passed. Its narrative is accurate and appropriately restrained — it identifies the
β-alanine specificity, the phosphopantetheine dependence, the domain that carries the activity,
and it says plainly that "no downstream pathway or in vivo role for AASDH has been established".
Its GO grounding (`GO:0140657 ATP-dependent activity`, `GO:0016874 ligase activity`) is correct
but two levels too general, as expected; `GO:0016878` is the specific descendant the evidence
supports.

Notably, affinage says **nothing** about fatty acids — a second instance (after A1BG) of the
provider's silence being informative about a bad existing annotation, though as before it gives
no positive signal that the annotation exists.
