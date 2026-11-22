# NaUGT1 sequence and primary-evidence reconciliation

The nicotine-pathway assignment is supported at the **g26396 gene level**. It does
not require the erroneous premise that every UGT709-related protein is an
O-glucosyltransferase. Two complementary checks link the gene to direct assays.

1. **Cell 2026, PMID:41928514:** cloning, qPCR, VIGS and sequencing primers map to
   the same genomic locus as A0A2H4GSI3. The primer-compatible reconstructed ORF
   contains all 485 target residues unchanged after a 45-residue N-terminal
   extension. The full expression construct was not independently deposited in
   the retrieved materials. See [the full identity analysis](identity-cell.md)
   for methods, coordinates, source links and the negative control. Gene-level
   identity is strongly supported; direct activity of the isolated 485-aa
   database form remains untested in the retrieved experiments.
2. **Nature Communications 2026, PMID:42151135:** Supplementary Data 1, Sheet1
   A36:F36, and Data 4, Sheet1 A5:K5 explicitly map the assayed tobacco UGT1/NaGT
   to Nitab4.5_0006222g0020.1, Ntab11g024040-1.1 and A0A1S3YWH6. The paper assigns
   this nicotinate N-glucosyltransferase to UGT709L18. Translation of the supplied
   coding sequence gives a 479-aa native enzyme, verified as the suffix of the
   published tagged protein. Its global alignment to A0A2H4GSI3 has **466
   identical residues over 485 alignment columns (96.08%)**, or 466/479 paired
   positions (97.29%). This independently supports the close-homolog inference;
   it is not a reciprocal-best-hit or gene-tree analysis.

The assayed tobacco UGT1 maps explicitly to A0A1S3YWH6 and is a nicotinate N-glucosyltransferase.

The [primary paper](https://www.nature.com/articles/s41467-026-72705-0) establishes
that glucosylation activates the pyridine precursor in a reconstituted nicotine
biosynthesis cascade. Its substrate result therefore contradicts treating this
close homolog's automated 7-deoxyloganetic-acid name as experimental evidence
against N-glucosylation. The Cell study independently assays the N. attenuata
gene product and genetically tests the mapped locus.

## Reproduce the tobacco comparison

From the repository root:

```sh
uv run --script genes/NICAT/NaUGT1_candidate_UGT85A2_0/NaUGT1_candidate_UGT85A2_0-bioinformatics/analyze_naugt.py
```

The script pins Biopython/requests, reads the original supplementary workbooks,
checks accession consistency, translates the supplied coding sequence and
verifies it against the tagged protein before alignment. It uses global
BLOSUM62 with gap-open -10 and gap-extension -0.5, including terminal gaps in
the denominator. Inputs, source URLs, hashes, exact cells and computed alignment
are preserved in `results-natcom.json` and `natcom-pairwise-alignment.txt`.

## Ontology and process-participation check

QuickGO confirms that GO:0050139 nicotinate-N-glucosyltransferase activity already
exists and is not obsolete. The previous custom term proposal duplicated it.
GO:0042179 nicotine biosynthetic process describes chemical reactions producing
nicotine and descends from biosynthesis/metabolism. The gene product itself
catalyzes an on-pathway reaction, so the process claim is supported by enzymatic
participation as well as perturbation phenotypes.

The same-role comparison finds existing nicotine-biosynthesis annotations for
the catalytic participants PMT1 (Q42963), PMT3 (A0A314LG79), QPT2 (B2RFS9) and
A622 (B7UEU8, including PMID:19011764). The complete two-page QuickGO response,
term definition and ancestors are in `nicotine-term-and-comparators.json`.
No entry for A0A2H4GSI3 was found in the local GO-CAM index. The proposed nicotine
process is not an ancestor or descendant of another process on this gene,
because the five original source assertions are molecular functions.

## Limits and report assessment

The new OpenScientist report was read in full together with its computational
artifact. Its categorical rejection is contradicted by the 2026 primary
papers. Its assertion that no plant nicotinate N-glucosyltransferases had been
characterized also conflicts with PMID:31611893, which assays Arabidopsis
UGT76C4/UGT76C5. These are contextual comparators, not grounds for transferring
their complete substrate profiles to g26396.

The report's code uses average-linkage clustering, not the stated
neighbor-joining tree, and its pairwise identity traceback stops when either
sequence reaches its beginning, potentially omitting terminal overhangs. The
published assayed tobacco sequence is 479 aa; comparing an alternative 524-aa
database model without checking the supplement is not the same experiment.
No reported percentage or tree is adopted without the independent checks above.

Neither nicotinate activity nor the positive pathway assignment establishes
absence of quercetin or 7-deoxyloganetic-acid activity. Those substrate claims
remain unresolved without relevant target assays. The longer N terminus is a
construct/gene-model question; it is not evidence for a different paralog or
proof of the dominant native isoform.
