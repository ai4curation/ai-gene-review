# EIF2B1 evidence reconstruction

The saved inputs recover all 53 imported source contexts, two natural products, four ancestral PAINT assertions, 23 interaction-context joins and two target-resolved Reactome annotations. The analysis supports the identities and relationships below; experimental interpretation also uses the primary-source scopes in the [source guide](../EIF2B1-source-guide.md).

## Natural products and PAINT inheritance

Reconstructing the official alternative-sequence features and comparing both FASTAs gives Q14232-1 at 305 residues and Q14232-2 at 222 residues. The second product retains residues 1–161, replaces the segment corresponding to 162–222 and lacks the canonical segment 223–305. This is sequence evidence, not proof that both products have equivalent biochemical activity.

The PTHR45860 tree contains 242 nodes. The human target PTN002469365 descends from PTN000028064, and its alignment sequence exactly matches the 305-residue reference. Four literal IBD entries occur at that ancestor. They support the eIF2B complex, contribution to exchange-factor activity, translation initiation, and contribution to initiation-factor activity. The last IBD uses the human target's own experimental annotation as its descendant premise; that is legitimate experimental grounding, not circular propagation. The full node path, donor fields and original GAF line numbers are in `records.json`.

The complete captured rat Q64270 QuickGO response also retains experimental premises for heat, glucose and peptide-hormone responses. These support the preserved orthology-based contexts. The available donor abstracts concern regulation of the whole eIF2B complex, and do not establish isolated alpha-subunit sensing or a direct human experiment.

## Interaction records and partner classes

The IntAct response contains 204 records. Exact source PMID and participant matching produces 23 source-context joins, comprising 55 selected record occurrences. A record can support more than one imported context; this occurrence count is not a count of independent experiments. All 110 participant reference-checksum occurrences match the saved official protein sequences and taxa. Full MITAB fields, methods, host, taxa, negative flags, feature intervals and record identifiers remain in the output.

These checks authenticate the curated reference sequences. They do not establish that every experimental insert was independently sequenced, that a whole protein was used when a fragment is recorded, or that a screen pair received an orthogonal retest. A missing IntAct record is not a negative experiment: the human alpha-homodimer evidence in PMID:29599213 is assessed from its original reconstitution and structural work.

The following independent partner classifications justify the eight binding refinements. The same positive-association standard is applied to retained generic interactions; subclass selection does not transfer the partner's activity to EIF2B1.

| Source indices (zero-based) | Partner | Independently established class and limit | Binding term |
|---|---|---|---|
| 8, 12, 18 | [NTAQ1, Q96HA8](https://www.uniprot.org/uniprotkb/Q96HA8/entry) | Protein N-terminal glutamine amidohydrolase; the human catalytic assignment is inferred by similarity to mouse Q80WB5. It is not a protease assignment. | GO:0019899 enzyme binding |
| 16 | [TRIM59, Q8IWR1](https://www.uniprot.org/uniprotkb/Q8IWR1/entry) | Ubiquitin E3 ligase activity has experimental support in the official record. Association does not identify EIF2B1 as a ubiquitination substrate. | GO:0031625 ubiquitin protein ligase binding |
| 21 | [MED29, Q9NX70](https://www.uniprot.org/uniprotkb/Q9NX70/entry) | Mediator transcriptional coactivator subunit; no transcriptional activity is transferred to EIF2B1. | GO:0001223 transcription coactivator binding |
| 22 | [ATF5, Q9Y2D1](https://www.uniprot.org/uniprotkb/Q9Y2D1/entry) | DNA-binding transcription factor. Additional centrosomal functions do not invalidate that partner class. | GO:0140297 DNA-binding transcription factor binding |
| 23 | [Mouse Adra2b, P30545](https://www.uniprot.org/uniprotkb/P30545/entry) | Alpha-2B adrenergic receptor. Human EIF2B1 was tested against mouse receptor-tail constructs; the interaction does not demonstrate receptor agonism. | GO:0031695 alpha-2B adrenergic receptor binding |
| 24 | [Mouse Adra2a, Q01338](https://www.uniprot.org/uniprotkb/Q01338/entry) | Alpha-2A adrenergic receptor, with the same cross-species and tail-construct limits. | GO:0031694 alpha-2A adrenergic receptor binding |

RD3 is an enzyme regulator rather than a demonstrated enzyme; a PDZ domain in GORASP2 does not establish which domain contacts EIF2B1; TRIML2 and C1orf50 lack a sufficiently established relevant class for a narrower binding assignment here. Their positive associations remain non-core protein binding under the [ClinGen project instruction](../../../../projects/CLINGEN_MENDELIAN.md).

The unreviewed UBE2I-related Q7KZS0 sequence is 184 residues, with only its first 137 residues identical to canonical P63279 (158 residues). The divergent tail is explicitly reproduced in the output. A correct reference-checksum match supports the imported pair identity but does not establish canonical SUMO E2 activity of this particular sequence. Its association remains generic rather than being mislabeled as ubiquitin-conjugating-enzyme binding.

## Target-resolved Reactome localization

Reaction R-HSA-72670 has input complex 72526, which contains target entity 72517. Reaction R-HSA-72722 points through catalyst activity 72528 to the same complex; its input 72529 also contains that complex. Entity 72517 itself identifies human Q14232, residues 1–305, and cytosol GO:0005829. Thus the compartment is attached to the target rather than merely copied from the event. The exchange catalyst is the assembled eIF2B complex.

## Ontology and limitations

All 14 selected refinements retain the imported term in the replacement term's saved `is_a`/`part_of` ancestor closure. This verifies relatedness; it is not a substitute for the source-specific biological reasoning. No new annotation is generated by the script.

The sequence, tree, interaction and reaction projections agree with the independently prepared source assessments. Human reconstitution supports an integrated structural/regulatory contribution to translation initiation. The natural shorter product, exact historical experimental inserts, untested orthogonal pairs and unresolved source-specific developmental/T-cell assertions remain outside what these database joins establish.
