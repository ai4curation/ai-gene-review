# algA Gene Review Notes

## Gene Overview

- Gene: `algA`
- Locus tag: `PP_1277`
- Organism: `Pseudomonas putida KT2440`
- UniProt: `Q88ND5`
- Protein: bifunctional GDP-mannose precursor synthesis enzyme

## Core Molecular Activities

AlgA is a bifunctional enzyme with two clearly supported catalytic activities:

1. Mannose-6-phosphate isomerase activity, converting mannose-6-phosphate and fructose-6-phosphate [file:PSEPK/algA/algA-uniprot.txt "RecName: Full=Mannose-6-phosphate isomerase; EC=5.3.1.8"]
2. Mannose-1-phosphate guanylyltransferase activity, converting mannose-1-phosphate and GTP to GDP-mannose [file:PSEPK/algA/algA-uniprot.txt "RecName: Full=Mannose-1-phosphate guanylyltransferase; EC=2.7.7.13"]

These two activities explain the strongest GO molecular function terms in the current GOA file: GO:0004475 and GO:0004476 [file:PSEPK/algA/algA-goa.tsv "GO:0004475\tmannose-1-phosphate guanylyltransferase (GTP) activity"] [file:PSEPK/algA/algA-goa.tsv "GO:0004476\tmannose-6-phosphate isomerase activity"].

## Process-Level Interpretation

UniProt places AlgA directly in GDP-mannose precursor synthesis rather than a generic polysaccharide pathway step [file:PSEPK/algA/algA-uniprot.txt "PATHWAY: Nucleotide-sugar biosynthesis; GDP-alpha-D-mannose biosynthesis; GDP-alpha-D-mannose from alpha-D-mannose 1-phosphate (GTP route): step 1/1"] [file:PSEPK/algA/algA-uniprot.txt "PATHWAY: Nucleotide-sugar biosynthesis; GDP-alpha-D-mannose biosynthesis; alpha-D-mannose 1-phosphate from D-fructose 6-phosphate: step 1/2"].

The GOA annotation to `GDP-mannose biosynthetic process` is therefore the most direct biological process term [file:PSEPK/algA/algA-goa.tsv "GO:0009298\tGDP-mannose biosynthetic process"].

By contrast, the generic `polysaccharide biosynthetic process` and `polysaccharide metabolic process` terms look broader than the immediate evidence warrants. AlgA supplies GDP-mannose, which can feed alginate and potentially other mannose-containing glycans, so those high-level polysaccharide terms are best treated as over-annotation rather than core function [file:PSEPK/algA/algA-goa.tsv "GO:0000271\tpolysaccharide biosynthetic process"] [file:PSEPK/algA/algA-goa.tsv "GO:0005976\tpolysaccharide metabolic process"].

## Alginate Connection

UniProt explicitly ties AlgA to alginate precursor supply, but the wording is by similarity and phrased at the precursor level rather than as a direct demonstration of polymerization itself [file:PSEPK/algA/algA-uniprot.txt "Produces a precursor for alginate polymerization. The alginate layer provides a protective barrier against host immune defenses and antibiotics (By similarity)."].

That supports describing AlgA as an alginate-associated precursor synthesis enzyme in the free-text summary, while keeping the core GO process annotation focused on GDP-mannose biosynthesis.

## Annotation Decisions

- Keep `GO:0004475 mannose-1-phosphate guanylyltransferase (GTP) activity` as core.
- Keep `GO:0004476 mannose-6-phosphate isomerase activity` as core.
- Keep `GO:0009298 GDP-mannose biosynthetic process` as core.
- Treat `GO:0016779 nucleotidyltransferase activity` as over-annotated because it is a broad parent of the specific guanylyltransferase activity.
- Treat `GO:0000271 polysaccharide biosynthetic process` and `GO:0005976 polysaccharide metabolic process` as over-annotated because the direct evidence is for GDP-mannose precursor synthesis, not a generic polysaccharide program.

## Open Points

- Falcon deep research was started for `algA`, but the provider job had not produced a local output file yet during this review pass.
- If Falcon finishes later with KT2440-specific literature on alginate production, revisit whether a more specific downstream biological process term should also be retained as non-core.
