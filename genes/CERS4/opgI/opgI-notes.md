# OpgI review notes

2026-11-06. Standard fetch using accession Q3J1N3 and alias opgI completed normally with zero annotations. Seed/raw hashes were checked before review. The authored symbol opgI follows PMID:12027885; the current raw record has only locus RSP_0126 and was not altered. See the source analysis and corrected-start JSON for the exact66-residue sequence bridge, versus the older 106-residue orfX annotation.

Native 2.4.1 nonpolar genetic rescue supports the locus requirement. It does not by itself identify the protein as an activator, scaffold or catalyst, so no NEW BP or MF was added and core_functions remains empty. This preserves the characterized biological dependency without inventing its molecular work. The paper's ACP analogy is a hypothesis; the Ecoli reconstruction also retains a translational-coupling caveat. No family ID is guessed: current raw UniProt contains no PANTHER or InterPro family assignment.

Default Falcon request with --provider falcon genuinely failed 403 authentication. An initial wrapper invocation without provider failed argument validation before the actual request; both logs are retained. No provider report was manufactured. Manual primary research supplies this completed assessment.
