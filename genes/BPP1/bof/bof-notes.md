# bof (P22499) — Curation Notes

## Summary
- **Gene symbol**: `bof` (renamed `lxc` in the complete P1 genome sequence, `PMID:15489417`)
- **UniProtKB**: `P22499` (`BOF_BPP1`, 82 aa, 9.7 kDa)
- **Organism**: Escherichia phage P1 (`NCBITaxon:2886926`)
- **Function**: C1 repressor modulator / transcriptional corepressor protein Bof (Lxc) encoded in the `immT` ("tertiary immunity") region. Does not bind DNA by itself, but forms a ternary complex with C1 repressor and operator DNA that increases the affinity of C1 for operators, strongly enhances DNA looping between paired C1-bound operators, promotes `c1` autorepression, and counteracts Coi-mediated dissociation of C1-operator complexes.

## Literature Evidence
- **Schaefer & Hays 1990 (`PMID:2345146`)**:
  - Cloned and sequenced the P1 `bof` gene (`M32693`), showing that it encodes an 82-codon reading frame initiated at a `TTG` start codon and preceded by a putative C1 repressor binding site (`Op2b`), and demonstrated in vivo that Bof makes C1-mediated repression of `coi::lacZ` and `ban::lacZ` fusions more complete.
  - Quote: `"The bofDNA sequence encodes an 82-codon reading frame that begins with a TTG codon"`
  - Quote: `"Repression of both fusion genes by plasmid-encoded C1 plus Bof or by a P1 bof+ prophage was more complete."`
- **Velleman, Heirich,לה & Schuster 1990 (`PMID:2211715`)**:
  - Demonstrated by electrophoretic mobility shift assays (EMSA) that purified Bof protein enhances the binding of C1 repressor to `c1`, `ban`, `coi`, and `sit` operators by forming a ternary C1-Bof-operator DNA complex, shifting C1 synthesis to a lower steady-state level via enhanced autorepression.
  - Quote: `"Using a DNA mobility shift assay, we show that bof protein enhances the binding of c1 repressor to the operator of the c1 gene."`
  - Quote: `"We conclude that bof acts as a modulator protein in the repression of a multitude of c1-controlled operators in the P1 genome."`
- **Łobocka et al. 2004 (`PMID:15489417`)**:
  - Renamed `bof` to `lxc` (modulator of `immC` expression). Showed that Lxc forms a ternary complex with C1 and operator DNA, strongly enhances DNA looping between nearby operators (especially bivalent operators), and inhibits inactivation of C1 by Coi.
  - Quote: `"The ImmT region, distant from ImmC and ImmI, contains a small gene, lxc , whose product modulates the function of C1 by formation of a ternary complex with C1 and operator DNA"`
  - Quote: `"Participation of Lxc in the C1-operator complexes that control c 1 expression increases the affinity of the repressor for the operator and down-regulates the synthesis of C1 itself"`

## Annotation Review Decisions
- No existing GOA annotations (`existing_annotations: []`).
- **Core function**: `GO:0003714` (`transcription corepressor activity`), `directly_involved_in`: `GO:0045892` (`negative regulation of DNA-templated transcription`), `in_complex`: `GO:0032993` (`protein-DNA complex`).
