# ANKRD16 notes

- Only one functional paper: Vo et al. 2018 Nature, mouse [PMID:29769718, full text]. A publisher correction (PMID:29925958) relabels figure lanes and markers only. Other PubMed hits for ANKRD16 are GWAS or tumour-sequencing mentions.
- Mechanism: "binds directly to the catalytic domain of AlaRS"; "Serine that is misactivated by AlaRS is captured by the lysine side chains of ANKRD16"; "ANKRD16 acts prior to formation of mischarged tRNA"; "ANKRD16 had no effect on subsequent steps of tRNA mischarging including deacylation of mischarged Ser-tRNAAla". The acceptor lysines are K102, K135 and K165.
- Human: all GOA rows are ISS/IEA from mouse A2AS55. A reproducible alignment (ANKRD16-bioinformatics/) shows K102, K135 and K165 are conserved in human; the proteins are 82% identical and both 361 aa.
- **UniProt discrepancy:** the human and mouse function text says ANKRD16 promotes "hydrolysis of Ser-mischarged tRNA(Ala)". The paper tested this and found no effect on deacylation. The ATP hydrolysis it stimulates is pre-transfer. UniProt reference_review is marked DISPUTED.
- GO:0006400 tRNA modification (IEA, ISS) → MODIFY to GO:0106074 aminoacyl-tRNA metabolism involved in translational fidelity. ANKRD16 alters no tRNA nucleotide. Participation check: ANKRD16 does the work itself, as the covalent acceptor of misactivated serine; it is not merely required.
- No GO MF fits a protein that accepts a misactivated amino acid, so I proposed the new term "misactivated amino acid acceptor activity" (parent enzyme regulator activity) and used it in core_functions.
- Nucleus: kept as non-core; cytoplasm: accepted.
- Affinage: gates clear, accurate summary of the single paper.
