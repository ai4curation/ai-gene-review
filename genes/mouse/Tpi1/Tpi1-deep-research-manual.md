# Manual deep research for mouse Tpi1

Automated Falcon/Perplexity deep research was unavailable for this review, so this file records the literature synthesis used to review mouse `Tpi1`.

## Core function

Mouse `Tpi1` encodes the cytosolic glycolytic enzyme triosephosphate isomerase. UniProt records the canonical EC 5.3.1.1 reaction as reversible interconversion of dihydroxyacetone phosphate and D-glyceraldehyde 3-phosphate, with both glycolysis and gluconeogenesis as pathway contexts.

The `PTHR21139` family review agrees with the PAINT placement of `GO:0004807`, `GO:0006096`, `GO:0006094`, and `GO:0046166` on the TIM family node `PTN000474559`. `just paint-losses mouse Tpi1` reported no IRD or IKR loss on the mouse `P17751` lineage.

## Mouse evidence

Merkle and Pretsch (PMID:2693209) isolated mouse `Tpi1` structural-locus mutants with about 50% lower TPI activity in heterozygous blood. Homozygous mutants were early postimplantation lethal, probably because they totally lacked TPI activity and could not use glucose as an energy source.

Leinwand, Kozak and Ruddle (PMID:566475), plus the parallel somatic-cell-hybrid mapping paper PMID:566476, used expression of mouse TPI enzyme activity to assign the locus to chromosome 6. These are broad early IDA rows, but the assayed activity is specifically triose-phosphate isomerase.

Chen et al. (PMID:17023274) identified oxidized mouse cardiac TPI in an adriamycin cardiotoxicity proteomics experiment and measured cardiac TPI activity. Yang and Pu (PMID:19289113) and Feng et al. (PMID:23665338) are proteomic/localization contexts in mouse brain or hippocampus and do not alter the core assignment.

Sun et al. (PMID:30174313) showed that depletion of the lncRNA `Lncenc1` in mouse naive ESCs reduced expression of glycolysis genes including `Tpi1` and reduced glycolytic activity. The IGI row to obsolete canonical glycolysis is therefore better represented by `GO:0006096` glycolysis.

## Methylglyoxal side reaction

UniProt transfers a methylglyoxal synthase side activity from rabbit TPI1 (`P00939`). The chemistry is real: Iyengar and Rose (PMID:7013790) and Richard (PMID:2021650) describe slow beta-elimination from the TIM-bound enediol phosphate intermediate, yielding methylglyoxal and phosphate; Richard measured this side reaction on rabbit muscle TIM itself and estimated that the enzyme-bound intermediate partitions about 1,000,000-to-1 toward protonation over elimination. I therefore followed the newer rat `Tpi1` precedent and treated `GO:0008929` and `GO:0019242` as over-annotations rather than as non-core curated functions.

## Interactions and oligomeric state

TIM is a functional homodimer; UniProt records `SUBUNIT: Homodimer`, and Wierenga et al. (PMID:20694739) place the catalytic site at the dimer interface. Homodimerization is a useful contextual annotation, not the defining molecular function.

The mouse Caspr2 IPI row comes from a CNTNAP2 interaction proteomics screen (PMID:25707359). The cached abstract does not expose the Tpi1 peptide call, and the bare `GO:0005515` term is removed under the generic protein-binding policy.

The ubiquitin protein ligase binding ISO/IEA rows are transferred from human TPI1/Parkin. The original paper (PMID:19725078) recovered human TPI1 among 14 potential Parkin interactors in a TAP/MS screen. That evidence is too weak to support orthologous E3 ligase binding as a mouse `Tpi1` function, even though the TPI1 orthology is sound.

## GO-CAM context

Model `61e0e55600001225` uses mouse `Tpi1` for `GO:0004807` in `GO:0006094` in the cytosol. The molecular function, gluconeogenesis edge, and cytosolic location are consistent with this review.
