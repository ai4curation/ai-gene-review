# MYL10: ProtNLM function-text review

**NPI (score 0): the proposed venom-gland function is organism-inappropriate.**

## Original prediction

[ProtNLM A0A9L0TJE1](https://www.uniprot.org/uniprotkb/A0A9L0TJE1/entry#prot-nlm), frozen API snapshot 2026-09-08.

> May be involved in the cellular control mechanism of the secretion of toxins from the gland into the venom

## Claim and evidence

The claim is regulation of toxin secretion from a venom gland. Horses lack a venom delivery system, so this precise physiological context is refuted. The possibility that an intracellular myosin light chain might participate in ordinary secretion does not validate the venom-specific statement.

The selected horse sequence has the myosin regulatory light-chain family domain IPR050403 and EF-hand motifs. [Human–horse sequence comparison](MYL10-bioinformatics/RESULTS.md) measures 86.5% identity over 192 paired residues, with N-terminal differences; it supports family conservation without asserting full isoform identity. Human [UniProt Q9BUA6](https://www.uniprot.org/uniprotkb/Q9BUA6/entry) provides curated sequence features with calcium-coordinating positions and states “This chain binds calcium.” The calcium-binding statement is by similarity, not a direct horse assay. None of this creates evidence for toxin secretion.

**Error type: TAXON_CONSTRAINT_VIOLATION**, meaning an organism-inappropriate process; no formal GO constraint is asserted for this free text. The identical paragraph on CAPSL is documented in the frozen source, but repetition across two proteins alone does not establish frequency bias or identify a training donor.
