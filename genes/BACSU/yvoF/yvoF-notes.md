# YvoF evidence and curation notes

## 2026-11-07 primary review

YvoF acetylates the glyceryl hydroxyls of HepG using acetyl-CoA. The 2016 study identifies yvoF through loss of native lipid acetylation and characterizes recombinant activity; MAT is a related enzyme with overlapping in vitro scope but fails to rescue the yvoF deletion. This supports lipid O-acetylation as the physiological role, not an additional maltose metabolic function. [PMID:27226549]

The 2025 study directly connects YvoF-dependent carrier loading with lipoprotein acetylation. Native yvoF deletion changes FrxB N-terminal peptide mass by an acetyl unit and complementation restores it. The biochemical reconstitution uses recombinant YvoF, a geranylgeranyl C20 analogue of the native C35 carrier, calf intestinal alkaline phosphatase and recombinant LhaT-containing E. coli membranes. It does not identify the native phosphatase, establish which monoacetyl regioisomer/diacetyl species LhaT prefers, or demonstrate the membrane-crossing mechanism. [PMID:40626731]

The 2016 primary localization paragraph, independently accessible through the PMC search index, reports activity in membrane-containing fractions and none in the soluble fraction. Its high-salt extraction and sequence/structure comparison favor peripheral association; the physical tether remains unknown. The 2025 cytoplasmic loading model is compatible with membrane-associated YvoF rather than a freely soluble cytosolic enzyme. Side-of-membrane assignment is mechanistic inference, not a direct topology map. A short excerpt and access provenance are archived in `yvoF-source-analysis/PMID27226549-reading.md`.

The sole seeded GO:0016407 IBA is MODIFY to GO:0016413 O-acetyltransferase. The generic inherited chemistry is correct; target biochemical evidence supplies acceptor-atom specificity. `just paint-losses BACSU yvoF` found no IRD/IKR on this lineage. This is not a complete ancestral-node reconstruction and no loss is inferred. No NEW rows are necessary. The plasma-membrane core location reflects functional association, not transmembrane topology.

No TLR2 regulatory or immune-process annotation is added: the enzyme modifies a bacterial lipid carrier; downstream lipoprotein chemotypes are the receptor ligands. Necessity in a reporter screen alone would not establish an immune-signaling activity of YvoF. The 2025 paper's figure alternative text occasionally simplifies mutant results; scientific decisions use the Results and Methods text, not those summaries.

## Research access

A genuine `just deep-research BACSU yvoF --provider falcon` attempt failed with HTTP403 authentication. No provider report was fabricated. The full 2025 primary and cached 2016 abstract were read. Direct PMC2016 access returned CAPTCHA, publisher access403, and EuropePMC fullTextXML500; indexed primary Results supplied only the localization passage. These failed responses are not biological evidence, and the publication cache remains unchanged. Logs are in `.cache/module-audit-logs/hepg-20261107/new-bacillus-members/`.

Official QuickGO definitions were retrieved for acetyltransferase, O-acetyltransferase, N-acetyltransferase and donor-specific N-terminal acetyltransferase terms; responses are archived in the consultation audit directory. The original single annotation payload/order and raw source hashes are retained in the seed baseline.
