# regA focused report incorporation, 2026-09-20

The complete [OpenScientist report](regA-hypotheses/function-hypothesis-go-0047555/openscientist.md)
and both artifact provenance JSON files were read. GO:0047555 remains
**UNDECIDED**. The report is marked **DISPUTED** and no duplicate was requested.

The report correctly documents cAMP as the principal physiological substrate,
the phosphorelay-regulated receiver/PDE architecture, and the distinct GbpA/GbpB
pathway. It is also right that cAMP turnover and cGMP turnover must be assessed
separately. Its inference that “no primary paper reports cGMP as a substrate”
does not address PMID:34063491, already in the gene review. That paper calls the
RegA-RD complex broadly specific and demonstrates cGMP-dependent displacement
in Figure 1v. The key measured result is: “addition of cGMP (lilac plot) resulted
in only a partial decrease in FP that remained stable over time.”

The primary assay was re-read, including the recombinant-protein Methods and
the separate PDE-Glo methods. The RegA experiment measures fluorescent cyclic
nucleotide displacement from the kinase/PDE complex; partial displacement does
not prove cGMP hydrolysis or identify which composite binding site changed.
The PDE-Glo product-linked assay in this paper uses human PDE5/PDE8c, not RegA.
Thus the later study is relevant contrary literature, not conclusive cGMP
turnover evidence. Conversely, an absence of product measurement in this assay
does not establish absent catalytic capacity.

The older kinetic summary in PMID:12429832 gives a selectivity **lower bound**,
whereas PMID:34063491 describes selectivity as approximately 200. Treating that
number as an exact positive turnover ratio or as proof of zero cGMP activity is
unwarranted. The cached table caption defines selectivity in terms of the ratio
of Vmax/Km for the two substrates. cAMP remains the supported core substrate;
weak cGMP capacity remains unresolved.

The PAINT table was re-read: both cAMP and cGMP PDE IBDs occur at **PTN001682918**
in **PTHR11347**. The report neither locates a RegA-specific loss nor establishes
that the Gbp enzymes belong to this class-I ancestral lineage. Their ability to
perform the organism's principal cGMP turnover does not exclude additional
weak activity in another enzyme. The delivered plots are code-rendered,
hardcoded evidence-category tables, not a new phylogenetic or kinetic analysis.

Human follow-up should resolve substrate-specific product formation and limits
of detection under matched conditions. No NOT annotation is warranted from
the report's evidence-tier comparison or from cAMP preference alone.
