# PNO1 notes

## 2026-09-28 IBA and literature re-review

PNO1/DIM2 has one current IBA annotation, `GO:0005634 nucleus`, propagated from
`PANTHER:PTN000302633` in the `PTHR12826` PNO1/ribonuclease-Y family. The node is
placed at `taxon:2759` Eukaryota for the `PTHR12826:SF13` PNO1 subfamily and is
seeded by fission yeast, budding yeast PNO1 itself, human PNO1, and an additional
eukaryotic descendant; the yeast target's own `WITH/FROM` entry is expected direct
experimental grounding, not circularity. This is biologically consistent with a
conserved eukaryotic Pno1/Dim2 factor that acts in nucleolar/nuclear small-subunit
biogenesis and shuttles to cytoplasmic pre-40S particles. The yeast target itself
also has direct nucleolar/nuclear localization:
Grava et al. reported functional Yor145-GFP that was nuclear and concentrated in
the nucleolus [PMID:10923024 "Yor145-GFP localized to the nucleus, Yor145-GFP
concentrating in the nucleolus"], and Vanrobays et al. later described Dim2p as
associated with both early nucleolar and late cytoplasmic pre-rRNA species
[PMID:15037774 "is associated with early nucleolar and late cytoplasmic pre-rRNA
species"].

The old proteasome rows trace to Tone and Toh-e 2002. Full text confirms that
the paper identified a Pno1-Nob1 complex and proteasome maturation phenotypes in
a `pno1-1` mutant [PMID:12502737 "These data show that Nob1p and Pno1p form a
complex"; PMID:12502737 "Pno1p plays some roles in the maturation of the 20S
proteasome, as does Nob1p."; PMID:12502737 "Nob1p serves as a chaperone to join
the 20S proteasome with the 19S regulatory particle in the nucleus"]. It does
not establish direct unfolded-protein binding by Pno1: the likely nearest rationale
was the paper's nuclear-transfer phenotype for immature 20S proteasome precursors
rather than a Pno1 binding assay. Later work moved the supported Pno1 function
squarely into SSU assembly: Dim2p is a core SSU RRP component required for pre-rRNA processing
[PMID:15037774 "Dim2p, a core constituent of the SSU RRP complex"], Dim2 binds
pre-rRNA through its KH domain and supports pre-40S export
[PMID:18755838 "DIM2 binds pre-rRNAs directly through its KH domain"], and Dim2
directly interacts with Nob1 during the final 18S rRNA maturation module
[PMID:21075849 "Dim2 increases Nob1 RNA affinity."].

I searched for newer PNO1/DIM2 yeast papers and found the 2024 Parker et al.
Rio1 quality-control paper. It reinforces the same final cytoplasmic 40S
maturation model: Pno1 and Nob1 remain on late pre-40S particles, Pno1 stabilizes
Nob1 and blocks the Rps26 site, and Rio1 release of Pno1/Nob1 licenses correctly
processed 18S rRNA for translation [PMID:39038273 "Pno1 stabilizes Nob1 on the
ribosome"].
