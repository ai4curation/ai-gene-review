# pvdY curation notes

PvdY (`Q88F54`, PP_4245) lies next to `pvdS` and `pvdL` in the KT2440
pyoverdine region. UniProt carries the submitted name `Hydroxyproline
acetylase`, but the record has only genome-sequence references and no direct
functional study [file:PSEPK/pvdY/pvdY-uniprot.txt, "SubName:
Full=Hydroxyproline acetylase"].

The sequence supports an MbtK/IucB-like acyltransferase fold
(`IPR019432`, `PTHR31438:SF1`). The current cytoplasm, acyltransferase, and
siderophore-biosynthesis GOA rows are all electronic. The family architecture
and locus support a precursor-tailoring role, but they do not establish
hydroxyproline as the physiological acceptor, the transferred acyl group, or
the product in KT2440.

## Curation boundary

- Retain broad acyltransferase and siderophore-pathway participation only to the
  extent supported after literature adjudication.
- Do not create a substrate-specific MF or module reaction from the submitted
  product name alone.
- Keep the exact physiological reaction as a knowledge gap unless direct or
  strong pathway-specific homolog evidence resolves it.

## Literature adjudication

PMID:16585778 directly establishes that the type II *P. aeruginosa* PvdYII
ortholog is required for pyoverdine synthesis and that combined bioinformatic,
genetic, and biochemical evidence indicates hydroxyornithine acetylation. This
supports the same role for PP_4245 by orthology and pathway context, but it is
not direct KT2440 enzymology. The module and review therefore retain the
specific reaction as an explicit inference and keep donor specificity and the
exact modified KT2440 residue as knowledge gaps. [PMID:16585778
"Bioinformatic, genetic, and biochemical approaches indicate that the PvdYII
enzyme catalyzes acetylation of hydroxyornithine."]
