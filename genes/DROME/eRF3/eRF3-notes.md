# eRF3 (Q9VK85) review notes

Module context: dmel_erf1_erf3_termination_complex (eRF3 with eRF1).

Note: `just fetch-gene DROME eRF3` resolved to the unreviewed entry M9PD08; the review
was refetched from the expected accession Q9VK85 (`just fetch-gene DROME Q9VK85 --alias eRF3`).

Deep research: the first falcon attempt failed; a retry produced `eRF3-deep-research-falcon.md` (for Q9VK85) after the review was drafted. It agrees with this review (cytoplasmic ribosome-associated termination GTPase with eRF1; eRF3 LR16 G282D nonsense-suppressor allele in the GTP-binding region) and notes a PAM2 (PABP-interacting) motif, which motivates the suggested question on PABP coupling.

- Termination complex: [PMID:14573473 "eRF1 and eRF3 comprise the translation termination complex that recognizes stop codons and catalyzes the release of nascent polypeptide chains from ribosomes"]
- In vivo genetics: [PMID:14573473 "Mutations disrupting the Drosophila eRF1 and eRF3 show a strong maternal-effect nonsense suppression due to readthrough of stop codons and are zygotically lethal during larval stages"]
- Family: UniProt places eRF3 in the classic translation factor GTPase family, EF-Tu/EF-1A subfamily.

Decisions: all annotations accepted (GTPase, release factor activity as a member of the
eRF1-eRF3 complex, translational termination, cytosol, release factor complex). The
core MF is GTPase activity, with release-factor function shared with eRF1.
