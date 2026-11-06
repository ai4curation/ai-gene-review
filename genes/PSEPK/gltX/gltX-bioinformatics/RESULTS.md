# Reassessment of the GltX zinc-binding annotation

## Corrected primary premise

The prior analysis described an E. coli four-cysteine cluster. That is incorrect. PMID:7797500 identifies Cys98, Cys100, Cys125 and His127: three cysteines and one histidine. Full PMID:25686371 discusses this canonical site and alternative bacterial zinc-coordination motifs, as well as functional zinc-free GluRS proteins. Losing the canonical ligands is evidence against propagating this site; it is not a direct assay excluding every possible metal interaction.

## Reproducible sequence comparison

The unmodified KT2440 Q88LF6 raw UniProt record supplies the target sequence. Normal UniProt FASTA retrieval supplies E. coli P04805 and the independently curated zinc-binding PAO1 Q9XCL6 comparison. `data/provenance.json` records source URLs and checksums. MAFFT aligns the three proteins; `map_reference_sites.py` reports numbered residues without encoding biological conclusions. Run `just all` here to retrieve/align/map, or `just align map` against the retained inputs.

The primary E. coli ligands C98/C100/C125/H127 map to KT2440 C107/C109/A134/L136. The same alignment preserves PAO1 C107/C109/C134/H136. Thus KT2440 replaces the third cysteine and fourth histidine of this experimentally characterized site with alanine and leucine. This is specific site divergence, not loss inferred merely from bacterial taxonomy or the absence of a UniProt metal annotation.

The electronic zinc-binding transfer to Q88LF6 is not supported by conservation of the experimentally characterized GluRS site. However, this site-specific divergence is insufficient to exclude all native zinc binding. Full PMID:25686371 also reports zinc binding by an E. coli chimera carrying the T. elongatus domain despite absent zinc in the native T. elongatus structure, distinguishing occupancy, sequence motif and binding capacity. No KT2440 zinc-content/affinity measurement was found. The appropriate broader zinc-binding judgment is UNDECIDED; the earlier categorical exclusion is retracted. Zinc-independent glutamylation remains entirely compatible with the primary comparative study. This result does not challenge zinc-binding assignments to PAO1 or Bacillus GluRS.

## Quality checklist

- [x] Generic preparation and mapping scripts accept explicit input paths, accession identifiers and residue positions; no biological conclusion is encoded in their output.
- [x] Mapping was run independently with both E. coli and PAO1 reference sites, reproducing the target substitutions and the positive-control conserved ligands.
- [x] MAFFT alignment and both mappings completed normally.
- [x] Input FASTAs, provenance and direct TSV/alignment outputs are retained here.
- [x] Primary-site identity and the distinction between site divergence and an unperformed native binding assay are explicit.

The legacy `check_zinc_module.sh` remains a two-sequence visualization helper; the numbered three-sequence mapping above supersedes its previous qualitative interpretation.
