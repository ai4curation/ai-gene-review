# Gene symbols in module reasoning

The module compiler and module validator share one symbol-label rule. A
participant.gene or family representative_members descriptor can supply a
symbol through either a single-token preferred_term, such as MetXS, or a
symbol followed by a parenthetical qualifier, such as MetXS (PSEPK).

Other multiword labels, including PSEPK MetXS, human ALDH2, and
Mycobacterium tuberculosis MetX, do not supply a symbol. The compiler does not
guess which word names the gene. Verify the intended symbol before normalizing
a label; do not mechanically move the final word of arbitrary prose.

An explicit, readable gene symbol takes precedence over family representatives.
For a family-only participant, only representatives satisfying the same rule
contribute symbols. UniProt accessions remain available through Atom.uniprots
even when a descriptor's symbol cannot be read. Symbol-based predicates therefore
cannot match an ambiguous label; accession-based predicates can still use it.

Module validation emits a SYMBOL_LABEL warning with the descriptor's path for
every unresolved gene/representative label, including members nested in
complexes. The warning is advisory because an accession-grounded descriptor
remains valid. The runtime exclusion is unconditional: skipping validation does
not allow organism tokens from multiword labels into gene_symbols or
gap_candidates.

This rule defines a readable label format, not biological identifier validation.
A single token is not proof of a correct gene symbol. Literature, database
identifiers, and other curation checks remain necessary.
