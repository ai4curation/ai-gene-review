# traC (F plasmid, *Escherichia coli* K-12) — curation notes

UniProt: P18004 (TRAC_ECOLI), 875 aa, encoded on plasmid F. UniProt gives one
functional statement, "Required for the assembly of mature F-pilin subunits
into extended F pili", and one location, "Cell inner membrane; Peripheral
membrane protein".

The sequencing paper agrees on both the length and the function
[PMID:2265751 "The traC gene of the F plasmid tra operon is required for the assembly of mature F-pilin subunits into extended F pili."],
reporting "a deduced coding region of 875 amino acids", which matches the
entry exactly.

## What the genetics establishes

The traC1044 mutant is the informative allele. It abolishes F pili, leaves
pilin itself intact, and reduces DNA transfer
[PMID:2885308 "Mutant cells were able to pair with recipient cells during bacterial conjugation, but transfer of conjugal DNA occurred at a greatly reduced frequency."].
Because mature pilin subunits are still present in the membrane, the defect is
in assembly rather than in processing
[PMID:2885308 "Membranes of hosts carrying the F' mutation contained a full complement of mature F-pilin subunits, so the product of traC is presumably required for pilus assembly but not for pilin processing."],
and the authors read the combined phenotype as placing TraC in a
membrane-spanning complex
[PMID:2885308 "suggests that traC may be part of a membrane-spanning tra protein complex responsible for pilus assembly and disassembly and conjugal DNA transmission."].
Complementation confirms the assignment to traC
[PMID:2885308 "When a plasmid carrying traC was introduced into hosts harboring the F' mutation, phage sensitivity, the ability to elaborate F pili, and conjugation efficiency were restored."].

So both a pilus-assembly role and a conjugative-transfer role are supported by
mutant phenotype for this protein, and neither is currently in GOA.

## Membrane association is conditional

TraC is not an integral membrane protein. Expressed on its own it is
cytoplasmic; expressed from F, in the presence of the other Tra proteins, it
partitions with the membrane
[PMID:1350587 "However, when TraC was expressed from the F plasmid, much of it appeared associated with the bacterial membrane fraction."],
which the authors attribute to protein-protein interaction rather than to a
membrane anchor
[PMID:1350587 "These data suggest that TraC is normally associated with the membrane through interactions with other proteins specified by the tra region."].
The same work excludes TraC from the pilus tip
[PMID:1350587 "TraC does not appear to be part of the tip of the F pilus, as neither anti-TraC antibodies nor purified TraC had any effect on the infection of F-containing bacteria by the filamentous bacteriophage f1."].
UniProt's "Peripheral membrane protein" qualifier captures this correctly.

## The molecular function is unresolved, and that matters

TraC is conventionally called the VirB4-family ATPase of the F system, and
`modules/bacterial_type_iv_secretion_apparatus.yaml` assigns it that role by
family while deliberately grounding the ATPase molecular function on
*Agrobacterium* VirB4 (P0A3W0) instead. This review confirms that was the right
call. Searching the F TraC literature returns the sequencing paper, the
traC1044 genetics, and the localization study, and none of them assays
nucleotide binding or hydrolysis. GOA holds no molecular function for P18004 at
all.

Two further observations sharpen the gap rather than closing it:

- PANTHER's own sequence classification does not place P18004 with VirB4.
  P18004 falls in PTHR38467, which PANTHER has not named, whereas VirB4
  (P0A3W0) falls in PTHR30121. The module records this split.
- The nearest biochemical characterisation of an F-type VirB4 counterpart is of
  the pKM101 protein, confusingly also called TraB, and even there hydrolysis
  depended on the preparation (see `genes/ECOLI/traB/traB-notes.md`).

Conclusion: assert the pilus-assembly and conjugation processes, which mutant
phenotype supports directly, and assert no molecular function. This is a clean
MF_DARK case: a protein with a sharp, reproducible loss-of-function phenotype
and no known activity.
