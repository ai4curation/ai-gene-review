# ADP1 LolA review notes

Q6F8G3/ACIAD2937 is the signal-peptide-bearing LolA carrier (HAMAP MF_00240, TIGR00547, PTHR35869:SF1). Target-derived LolA accepts defined BamE from target-derived LolDF, giving direct evidence for the carrier MF rather than only dependence on a pathway. [PMID:42736309, "To verify ATP-driven lipoprotein transfer to LolA, we performed an in vitro single-cycle transport assay using detergent-purified A baylyi LolDF co-expressed with BamE and purified A baylyi LolA in the presence or absence of ATP and MgCl2."]

The primary uses recombinant mature A. baylyi LolA expressed in E. coli BL21(DE3), with N-terminal His-SUMO removal and a retained Strep tag. It is not an E. coli LolA ortholog transfer. PDB 29EB entity 4 exactly matches Q6F8G3 residues 29–230, although the methods name the construct 29–231. This endpoint discrepancy remains explicit; neither the target sequence nor the paper was silently repaired. [file:analysis/module_audits/bacterial_lol_lipoprotein_trafficking/aciad-consultation/identity-notes.md]

The observed complex has one bound LolA [PMID:42736309, "The cryo-EM map reveals that only a single LolA molecule binds to the LolDF dimer"]. Homodimeric LolF therefore does not imply two simultaneously bound carriers. The transfer assay is a detergent single-cycle BamE handover and does not demonstrate all native cargo, terminal LolB insertion, or complete native flux. The source's general +2 Asp statement is not treated as proof that LolA itself recognizes every sorting signal.

All four original payloads are preserved. The periplasm parent is refined to the existing diderm-periplasm term. One independent carrier MF is added by IDA; it is neither redundant with BP/CC rows nor inferred solely from necessity. No new process is proposed.

## Assay limits, research and lineage checks

The primary's charge substitutions were made in BamE; their binding/extraction results do not establish universal rules for all +3-charged lipoproteins. Lnt-silencing viability and structural accommodation suggest acyl-state tolerance but are not a chemically defined assay proving efficient transport of every diacylated substrate. The observed single LolA, unknown endogenous cargo and detergent single-cycle handover are retained as separate facts.

A genuine Falcon research attempt on 2026-11-07 returned HTTP 403 authentication failure (exit 1). The exact log is preserved under the aciad-consultation audit directory; no provider-named report was fabricated. Existing raw sources and publication caches were not rewritten.

PAINT loss inspection could not resolve the target lineage: no PANTHER family is recorded for LolB, while the other target accessions are absent from the available family trees. The tool's concluding no-loss sentence is not evidence of an absence. The seeded rows are IEA; no unsupported IBA-node judgment is made.
