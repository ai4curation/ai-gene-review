# rexB (P03759) - Curation Notes

## Overview
- **Gene symbol**: `rexB`
- **UniProt ID**: `P03759` (`REXB_LAMBD`)
- **Protein name**: Protein rexB (144 AA)
- **Organism**: Escherichia phage lambda (`NCBITaxon:2681611`)

## Function & Biological Context
- **Polytopic inner-membrane ion channel pore of the RexAB superinfection exclusion system**: `rexB` is co-expressed with `cI` and `rexA` from the lysogenic maintenance promoter `PRM` (`P_M`) in lambda prophages (and can also be transcribed from an internal promoter `PLit` just upstream of `rexB`). RexB is a 144-residue integral membrane protein with four transmembrane alpha-helices localized to the *Escherichia coli* inner (cytoplasmic) membrane [PMID:1372278, "The RexB protein appears to be a polytopic transmembrane protein. We suggest that RexB proteins form ion channels that, in response to lytic growth of bacteriophages, depolarize the cytoplasmic membrane."].
- **RexA-gated membrane depolarization and abortive infection**: Upon superinfection of a lambda lysogen by heterologous phages (such as T4 `rII` mutants) or lambda `ren` mutants, binding of at least two cytoplasmic RexA proteins to RexB opens the RexB transmembrane pore, collapsing the host membrane potential and intracellular ATP levels, halting macromolecular synthesis, and aborting lytic phage development [PMID:1372278; PMID:11790759, "The model of Parma et al. ( 13 ) predicts that RexB protein forms an inner membrane pore that is opened upon direct interaction with at least two RexA proteins"]. Overexpression of RexB alters the RexA:RexB stoichiometry and suppresses Rex exclusion of both T4 `rII` and lambda `ren` mutants [PMID:1372278, "We have determined that overexpression of RexB in lambda lysogens prevents the exclusion of both T4 rII mutants and lambda ren mutants."].
- **Regulation of ClpP-dependent proteolysis and anti-cell death activity**: Independently of `rexA`, RexB stabilizes short-lived proteins degraded by host ClpXP/ClpAP proteases:
  - RexB prevents degradation of the short-lived phage lambda replication initiator protein O [PMID:1828888, "Here we present an additional lambda rexB function: it prevents degradation of the short-lived protein lambda O known to be involved in lambda DNA replication."].
  - RexB also prevents programmed bacterial cell death triggered by toxin-antitoxin addiction modules (such as P1 `phd-doc` and *E. coli* `mazEF`) by inhibiting ClpP-dependent degradation of the labile antitoxins Phd and MazE [PMID:9860994, "Here we show that the product of lambdarexB, one of the few genes expressed in the lysogenic state of bacteriophage lambda, prevents cell death directed by each of two addiction modules, phd-doc of plasmid prophage P1 and the rel mazEF of E. coli"; PMID:9860994, "lambdaRexB inhibits the degradation of the antitoxic labile components Phd and MazE of these systems, which are substrates of ClpP proteases."].

## Review of Existing GO Annotations
- `GO:0033644` (host cell membrane, IEA, `GO_REF:0000044`): **ACCEPT**. RexB is a 4-transmembrane polytopic protein embedded in the *E. coli* inner (cytoplasmic) membrane (`PMID:1372278`).
