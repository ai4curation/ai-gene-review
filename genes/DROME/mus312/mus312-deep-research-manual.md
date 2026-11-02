# mus312 (Q9VS48, SLX4_DROME) - manual literature synthesis

No deep-research API was available; this synthesis was assembled manually from cached
publications (publications/PMID_*.md) and PubMed searches ("mus312 Drosophila", 8 hits).

## Identity and family
- MUS312 (CG8601, FBgn0002909) is the fly ortholog of yeast Slx4 and vertebrate BTBD12/SLX4/FANCP
  [PMID:19595722 "Based on sequence, expression pattern, conserved protein-protein interactions, and ICL repair function, we determined that the mammalian ortholog of MUS312 is BTBD12"].
- UniProt: 1145 aa, coiled coil 321-372, several disordered regions, Slx4 HTH domain (IPR018574, PF09494), SAP domain (cd22999); "Belongs to the SLX4 family."
- It is non-catalytic [PMID:22022278 "MUS312 is a non-catalytic subunit that interacts with at least two nucleases, SLX1 and MEI-9–ERCC1"].

## Meiotic crossover formation (with MEI-9-ERCC1)
- MUS312 binds MEI-9 (XPF) and mus312 mutants phenocopy mei-9 in meiosis; a mei-9 allele disrupting the interaction abolishes meiotic but not repair functions [PMID:12504024 "A missense mutation in mei-9 that disrupts the MEI-9-MUS312 interaction abolishes the meiotic function of mei-9 but does not affect the DNA repair functions of mei-9"].
- Crossovers are reduced >95% [PMID:19595722 "COs are decreased by >95% in mus312 mutants, but by only 85-90% in mei-9 mutants"].
- MEI-9 bridges ERCC1 and MUS312 in a yeast three-hybrid assay [PMID:15944364 "expression of untagged MEI-9 protein in the same yeast two-hybrid assay does allow ERCC1 and MUS312 to interact"].
- HDM joins the complex [PMID:18957705 "We conclude that HDM, MEI-9, MUS312, and ERCC1 form a complex that resolves meiotic recombination intermediates into crossovers."].
- Crossover-defective mutants including mus312 trigger a PCH2-dependent pachytene checkpoint delaying oocyte selection [PMID:18957704].

## SLX1-SLX4 nuclease and somatic repair
- Y2H interaction of MUS312 with fly SLX1 [PMID:19595722 "In a Y2H assay, Drosophila MUS312 and SLX1 also interact (Figure 1C)"; PMID:19596236 "we detected a strong yeast two hybrid (Y2H) interaction between MUS312 and D. melanogaster SLX1 (Figure 1B)"].
- ICL hypersensitivity, MEI-9-independent [PMID:19595722 "mus312 mutants are mildly hypersensitive to the alkylating agent methyl methanesulfonate (MMS), but are highly hypersensitive to the nitrogen mustard mechloramine (HN2), a bifunctional agent that can cause DNA interstrand crosslinks"].
- Synthetic lethality with mus309 (BLM), phenocopied by slx1 mus309 [PMID:22022278 "We conclude that the inviability of mus312 mus309 double mutants is indeed due to simultaneous loss of DmBLM and MUS312–SLX1."].
- Spontaneous mitotic crossovers in Fancm mutants require MUS312 [PMID:25205745 "crossovers were completely eliminated in double mutants with mus312"]; SLX1 and MUS81 act redundantly downstream.
- RNAi screen implicates MUS312-containing nuclease complexes in the G2-M DNA damage checkpoint [PMID:21205937] (screen-level; not used for annotation).

## Gaps
- No in vitro biochemistry for fly MUS312 complexes (enzyme stimulation not shown).
- The ICL-repair partner nuclease in Drosophila is not established.
- No direct localization data for fly MUS312 (nuclear by similarity).
