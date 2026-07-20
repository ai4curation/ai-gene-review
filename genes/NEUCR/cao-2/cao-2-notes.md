# cao-2 (CAO2_NEUCR, A7UXI1 / NCU11424) — review notes

## Gene identity and function

cao-2 encodes CAO-2, the second carotenoid cleavage oxygenase (CCO) of *Neurospora crassa* and the
**paralog of cao-1**. Unlike cao-1 (a stilbenoid cleaver), CAO-2 is a genuine **carotenoid-cleaving
enzyme**: it is a **torulene dioxygenase** (EC 1.13.11.59) that catalyzes the committed cleavage step of
the **neurosporaxanthin (apocarotenoid) biosynthetic pathway**.

- **Reaction:** torulene (a C40 carotene) + O2 → 4'-apo-β-carotenal (β-apo-4'-carotenal, C35) +
  3-methyl-2-butenal. The C35 apocarotenal is then oxidized to the xanthophyll neurosporaxanthin by
  the aldehyde dehydrogenase YLO-1.
- **Pathway:** Carotenoid biosynthesis (neurosporaxanthin branch); KEGG `ncr00906`; KEGG KO **K17842**
  (torulene dioxygenase).
- **Localization:** cytosol (UniProt Cytoplasm, cytosol).

## Key experimental evidence — PMID:17610084 (Saelices et al. 2007)

CAO-2 was identified and characterized by genetics + biochemistry:
- Torulene-accumulating, neurosporaxanthin-lacking mutants map to cao-2; targeted disruption gives
  [PMID:17610084 "the identical phenotype found upon targeted disruption of cao-2"].
- Direct in vitro assay with purified enzyme:
  [PMID:17610084 "cleaved torulene to produce beta-apo-4'-carotenal, the corresponding aldehyde of neurosporaxanthin"].
- Substrate specificity: [PMID:17610084 "lack of gamma-carotene-cleaving activity in vitro"].
- Regulation: [PMID:17610084 "cao-2 mRNA was induced by light in a WC-1 and WC-2 dependent manner"] —
  the **opposite** of cao-1 (light-independent), as expected for a genuine carotenoid-pathway gene.
- Conclusion: [PMID:17610084 "CAO-2 is the enzyme responsible for the oxidative cleavage of torulene in the neurosporaxanthin biosynthetic pathway"].

## Two IBA lessons in one paralog pair (cross-link to IBA_REVIEW.md)

CAO-2 is the **positive-control paralog** of cao-1. Both carry the identical family IBA terms
(GO:0010436 carotenoid dioxygenase activity, GO:0016121 carotene catabolic process; both from
GO_REF:0000033), because they share PANTHER family PTHR10543. For **cao-1 those terms are wrong**
(refuted; it cleaves stilbenes); for **cao-2 they are correct** (it cleaves the carotene torulene). The
same phylogenetic inference is right for one paralog and wrong for the other — only target-specific
experimental evidence separates them.

But CAO-2 also illustrates the **inverse** IBA problem — **under-curation / IBA incompleteness**.
Despite a full experimental characterization (disruption phenotype + purified-enzyme assay,
PMID:17610084), GOA carries **only IBA/IEA** annotations for CAO-2 — no IDA. The experimental
torulene-dioxygenase activity and the neurosporaxanthin/apocarotenoid-biosynthesis role are not
captured as experimental annotations. So the same gene is simultaneously a case where IBA is *correct*
and a case where experimental biology that should be annotated is *missing*.

## Annotation review decisions (4 GOA annotations)

| GO term | Evidence | Decision | Rationale |
|---|---|---|---|
| GO:0010436 carotenoid dioxygenase activity | IBA | **ACCEPT (core)** | Correct; CAO-2 is a torulene dioxygenase (EC 1.13.11.59). Experimentally supported (PMID:17610084) though currently only IBA. No specific torulene-dioxygenase GO term exists. |
| GO:0016121 carotene catabolic process | IBA | **ACCEPT** | Torulene (a carotene) is cleaved. Accurate but partial: the informative process is apocarotenoid/neurosporaxanthin biosynthesis (GO:0043289), captured in core_functions. |
| GO:0005829 cytosol | IEA | **ACCEPT** | Consistent with UniProt cytoplasm/cytosol. |
| GO:0016702 oxidoreductase (2 O atoms; dioxygenase) | IEA | **ACCEPT** | Correct general dioxygenase MF, corroborates GO:0010436. |

Core function: torulene dioxygenase (GO:0010436; EC 1.13.11.59) in apocarotenoid biosynthetic process
(GO:0043289) / neurosporaxanthin biosynthesis; cytosol. Under-annotated experimentally — an
apocarotenoid-biosynthesis BP and IDA upgrades from PMID:17610084 are warranted.
