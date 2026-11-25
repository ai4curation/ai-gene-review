---
provider: manual
date: 2026-11-25
---

# Manual deep research for S. pombe mas2

The Falcon deep-research provider and the Perplexity fallback were unavailable in this checkout, so this file records a manual synthesis of the cached literature and database records used for the review.

S. pombe mas2 encodes the noncatalytic alpha-MPP subunit of mitochondrial processing peptidase.

## Core conserved activity

The S. pombe protein O94745 is the `PTHR11851:SF49` alpha-MPP ortholog. Its UniProt record describes Mas2 as the substrate recognition and binding subunit of essential mitochondrial processing peptidase, places it in a heterodimer with the catalytic beta subunit mas1, and localizes it to the mitochondrial matrix.

The key alpha-MPP publication cached from the PomBase NOT row is Shimokata et al. (`PMID:9737975`). Using recombinant yeast MPP, that study found that mutations in conserved acidic residues in alpha-MPP have substrate-dependent effects on precursor cleavage and concluded that alpha-MPP recognizes basic residues in mitochondrial presequences distal to the beta-MPP cleavage site. That supports peptidase activator activity, MPP complex membership, and involvement in mitochondrial protein processing while agreeing with the NOT metalloendopeptidase row on Mas2 itself.

The PTHR11851 family review already judged the PAINT `GO:0017087 mitochondrial processing peptidase complex` IBD at `PTN000220169` sound for the eukaryotic alpha/beta-MPP duplication node. `just paint-losses SCHPO mas2` found no IRD or IKR on the S. pombe mas2 lineage, so the MPP complex IBA is current.

## GO-CAM context

GO-CAM 69729a3800007453 models `PomBase:SPBC18E5.12c` as enabling peptidase activator activity (`GO:0016504`), part of mitochondrial protein processing (`GO:0034982`), occurring in the mitochondrial matrix (`GO:0005759`), and directly positively regulating the mas1 signal peptidase activity. The gene review agrees with this split of the MPP heterodimer: Mas2 is the noncatalytic activator, and mas1 is the catalytic signal peptidase subunit.
