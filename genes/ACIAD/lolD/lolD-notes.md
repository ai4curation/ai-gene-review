# ADP1 LolD review notes

Q9EYM2/ACIAD2640 is the 228-residue LolD ATPase. Its official family placement is PTHR42798:SF2, distinct from the PTHR24220 LolD placement used for E. coli/KT2440. PDB LolD entities match target residues 3–226 exactly; the observed terminal truncation in deposited entities is not a different target. Tested K48, Y93, S148, E172 and H205 agree with the current sequence. [file:analysis/module_audits/bacterial_lol_lipoprotein_trafficking/aciad-consultation/identity-notes.md]

The endogenous ADP1 complex is purified through a chromosomal LolD His-Flag tag. Native conditional silencing/complementation, nucleotide-bound structures and ATPase measurements support its catalytic role. [PMID:42736309, "Alanine substitutions of catalytic residues (K48, S148, E172, H205) abolished ATPase activity and cell viability without affecting expression"]. ATP binding is core substrate binding; hydrolysis is the autonomous molecular reaction. Lipoprotein release is a coupled contribution with the LolF dimer, demonstrated by defined BamE transfer to LolA in detergent rather than complete native outer-membrane insertion.

The preserved UniProt CC:SUBUNIT text describes two distinct membrane proteins LolC and LolE. This heteromeric template is contradicted by the native target homodimeric LolF architecture; a structured WRONG_STATEMENT source defect requests checking that specific sentence while preserving the correct target identity and ATPase function. No upstream report was sent. [PMID:42736309, "The LolDF complex forms a homodimer that adopts a characteristic type VII ABC transporter architecture"].

All five original payloads remain ordered. ATP binding, peripheral plasma-membrane association, ATP hydrolysis and lipoprotein localization are accepted, and broad protein localization is refined to the already present lipoprotein-specific process. One independent contribution to release is proposed; no additional BP is needed.

## Assay limits, research and lineage checks

The primary's charge substitutions were made in BamE; their binding/extraction results do not establish universal rules for all +3-charged lipoproteins. Lnt-silencing viability and structural accommodation suggest acyl-state tolerance but are not a chemically defined assay proving efficient transport of every diacylated substrate. The observed single LolA, unknown endogenous cargo and detergent single-cycle handover are retained as separate facts.

A genuine Falcon research attempt on 2026-11-07 returned HTTP 403 authentication failure (exit 1). The exact log is preserved under the aciad-consultation audit directory; no provider-named report was fabricated. Existing raw sources and publication caches were not rewritten.

PAINT loss inspection could not resolve the target lineage: no PANTHER family is recorded for LolB, while the other target accessions are absent from the available family trees. The tool's concluding no-loss sentence is not evidence of an absence. The seeded rows are IEA; no unsupported IBA-node judgment is made.
