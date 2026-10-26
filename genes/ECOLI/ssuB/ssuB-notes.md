# E. coli ssuB: manual source-based review

SsuB is the ATP-binding component of the Escherichia coli SsuABC alkanesulfonate importer. Its conserved ABC nucleotide-binding machinery supplies the energy-coupling role at the inner membrane, working with SsuC and the periplasmic substrate-binding protein SsuA to acquire alternative sulfur sources during sulfate limitation. Transport specificity is a property of the assembled system rather than SsuB alone.

## Evidence and decisions

- Row 1, GO:0005524 (IEA; GO_REF:0000002): **ACCEPT**. The original ABC-family inference is supported independently by the SsuB nucleotide-binding architecture and curated HAMAP substrate-binding feature, together with native SsuABC transport genetics. PMID:9593292 is an ABC-protein inventory, not a purified SsuB binding experiment; the ATP-binding claim is retained as a well-supported mechanistic inference.
- Row 2, GO:0005524 (ISM; PMID:9593292): **ACCEPT**. The original ABC-family inference is supported independently by the SsuB nucleotide-binding architecture and curated HAMAP substrate-binding feature, together with native SsuABC transport genetics. PMID:9593292 is an ABC-protein inventory, not a purified SsuB binding experiment; the ATP-binding claim is retained as a well-supported mechanistic inference.
- Row 3, GO:0005524 (RCA; PMID:10506196): **ACCEPT**. The original ABC-family inference is supported independently by the SsuB nucleotide-binding architecture and curated HAMAP substrate-binding feature, together with native SsuABC transport genetics. PMID:9593292 is an ABC-protein inventory, not a purified SsuB binding experiment; the ATP-binding claim is retained as a well-supported mechanistic inference.
- Row 4, GO:0005886 (IEA; GO_REF:0000044): **ACCEPT**. Curated HAMAP annotation identifies SsuB as a peripheral inner-membrane component, consistent with its ATP-coupling role and native transport genetics.
- Row 5, GO:0010438 (NAS; PMID:10781534): **ACCEPT**. The sulfur-starvation response includes execution of alternative-sulfur uptake by SsuABC, supported by native genetics and operon regulation. This is not a claim that the transporter is the Cbl transcriptional sensor or regulator.
- Row 6, GO:0016020 (NAS; PMID:10781534): **MODIFY**. Curated HAMAP annotation identifies SsuB as a peripheral inner-membrane component, consistent with its ATP-coupling role and native transport genetics. Refine generic membrane to the already represented plasma-membrane term.
- Row 7, GO:0016887 (IEA; GO_REF:0000002): **ACCEPT**. The ABC nucleotide-binding/catalytic architecture and HAMAP-curated importer function support ATP hydrolysis as the energy-coupling activity of SsuB. This is a component-level catalytic inference corroborated by native system genetics, not an assertion that the 2000 growth study directly measured purified SsuB ATP turnover.
- Row 8, GO:0042918 (EXP; PMID:10781534): **ACCEPT**. PMID:10781534 tests native in-frame deletions and complementation, with SsuABC substrate specificity distinct from TauABC. ssuB executes ATP-dependent energy coupling within that importer. This supports transmembrane transport without treating the subunit as independently sufficient.
- Row 9, GO:0042918 (IEA; GO_REF:0000117): **ACCEPT**. PMID:10781534 tests native in-frame deletions and complementation, with SsuABC substrate specificity distinct from TauABC. ssuB executes ATP-dependent energy coupling within that importer. This supports transmembrane transport without treating the subunit as independently sufficient.
- Row 10, GO:0042959 (EXP; PMID:10781534): **ACCEPT**. The native deletion/complementation evidence in PMID:10781534 establishes the SsuABC transport system and its substrate range. ssuB contributes ATP-dependent energy coupling; the accepted activity is interpreted at the functional complex level, not as isolated-subunit transport. The core explicitly records this component contribution. Ordinary machine relationship fields are preserved.
- Row 11, GO:0055052 (NAS; PMID:10781534): **ACCEPT**. The component-specific genetic experiments support ssuB as a member of the SsuABC system. The periplasmic binding protein, membrane permease and ATP-binding component are distinguished in the primary text. Exact subunit copy numbers were inferred by analogy and are not claimed as directly determined here.

## Acquisition and provenance

All original ordered annotation payloads and both raw files are retained. No NEW annotations were proposed. The genuine Falcon and perplexity-lite attempts failed authentication; actual FEBA attempts returned no usable mapped data (foundation job logs). These failures are not evidence about function. Publication caches were read as retrieved, never hand-edited. Primary abstracts are distinguished from normally recovered full PMC URL text. No GOA assertion or protein name is cited as biological support. Ordinary relationship fields were not used to reject a complex contribution.

PMID:10781534 full text was read at https://pmc.ncbi.nlm.nih.gov/articles/PMC101965/. Native E. coli EC1250 deletions and complementation support the assembled importer, not individual ATP-independent transport. Hybrid Tau/Ssu component combinations failed for tested shared substrates; this does not establish all cross-species combinations fail. Residual propanesulfonate/butanesulfonate entry in double deletions is an unresolved alternative uptake mechanism. Predicted homodimeric transporter subunits are not treated as measured stoichiometry. PMID:10506196 is an operon-level deletion/regulation study.

## Source findings

- [file:ECOLI/ssuB/ssuB-uniprot.txt] SsuB contains the conserved ABC ATP-binding machinery. “DR   InterPro; IPR003439; ABC_transporter-like_ATP-bd.”
- [file:ECOLI/ssuB/ssuB-uniprot.txt] SsuB is the peripheral ATP-binding component at the inner membrane. “Cell inner membrane {ECO:0000255|HAMAP-
CC       Rule:MF_01724}; Peripheral membrane protein {ECO:0000255|HAMAP-
CC       Rule:MF_01724}.”
- [url:https://pmc.ncbi.nlm.nih.gov/articles/PMC101965/] SsuB contains the conserved ABC ATP-binding machinery. “The sequences of TauB and SsuB and of TauC and SsuC are significantly similar to those of ATP-binding proteins and integral membrane components, respectively, of members of the ABC transporter superfamily (6).”
- [url:https://pmc.ncbi.nlm.nih.gov/articles/PMC101965/] SsuABC mediates adaptive sulfur-source acquisition during sulfur limitation. “As documented by the mechanisms regulating gene expression in these systems, they both are involved in scavenging sulfur for growth.”
- [PMID:10480865] SsuABC mediates adaptive sulfur-source acquisition during sulfur limitation. “The Escherichia coli ssuEADCB gene cluster is required for the utilization of
alkanesulfonates as sulfur sources, and is expressed under conditions of sulfate
or cysteine starvation.”
