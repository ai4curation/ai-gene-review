# EPG5 notes (human, Q9HCE0)

Deep research: not run (falcon times out after 600 s in this environment and perplexity-lite is not
installed). Review based on cached publications, the UniProt record and PubMed abstracts.

## Key findings
- Rab7 effector setting autophagosome fusion specificity [PMID:27588602 "EPG5 is recruited to late endosomes/lysosomes by direct interaction with Rab7 and the late endosomal/lysosomal R-SNARE VAMP7/8"].
- Binds LC3 and STX17-SNAP29; stabilizes trans-SNAREs [PMID:27588602 "EPG5 stabilizes and facilitates the assembly of STX17-SNAP29-VAMP7/8 trans-SNARE complexes, and promotes STX17-SNAP29-VAMP7-mediated fusion of reconstituted proteoliposomes"]. Full text not cached (abstract only).
- Vici syndrome; autophagosome clearance block [PMID:23222957 "Further studies showed a severe block in autophagosomal clearance in muscle and fibroblasts from individuals with mutant EPG5"].
- mEPG5 needed for degradative autolysosomes [PMID:20550938 "EI24 and mEPG5 are required for formation of degradative autolysosomes."].
- Autophagy-independent endolysosomal delivery of CpG to TLR9 compartments [PMID:29130391 "Here we show that EPG5 also plays autophagy-independent roles in the trafficking of molecules from the EEs to LEs and lysosomes."].

## Decisions
- nucleotide transport (IMP) -> MODIFY to endosome to lysosome transport: cargo is a CpG oligonucleotide inside vesicles.
- cellular response to dsDNA -> over-annotated; TLR9 pathway kept as non-core (acts upstream).
- NEW: vesicle membrane tethering activity (core MF), small GTPase binding, SNARE binding (all from PMID:27588602).
