# OAZ1 (YPL052W, UniProt Q02803) notes

## Function
- ODC antizyme: "Binds to ODC/SPE1 monomers, inhibiting the assembly of the functional ODC homodimer, and targets the monomers for ubiquitin-independent proteolytic destruction by the 26S proteasome" [UniProt:Q02803].
- "Degradation of yeast ODC by the proteasome depends on Oaz1." [PMID:15538383]; "Deletion of OAZ1 resulted in a drastic stabilization of ODC, with spermidine having no effect on its stability." [PMID:15538383]
- Feedback: "Polyamines thus appear to mediate an efficient feedback control of their formation by affecting both the synthesis and turnover rates of ODC AZ." [PMID:15538383]
- Yeast vs mammalian proteasome: "We demonstrate that interaction with yAz provokes degradation of yODC by yeast but not by mammalian proteasomes." [PMID:18089576]; only minor effect on polyamine uptake [PMID:18089576].
- Frameshift autoregulation: "the nascent antizyme polypeptide is the relevant polyamine sensor that operates in cis to negatively regulate upstream RFS on the polysomes" [PMID:21900894].

## Pathway / GO-CAM
- No YeastPathways reaction. Module polyamine_metabolism links to S. pombe GO-CAM 67b1629100004168, where spa1 enables GO:0008073 part_of GO:1901305 negative regulation of spermidine biosynthetic process (comparator for the NEW GO:0170066).

## Decisions
- ACCEPT GO:0008073 IDA (core), cytoplasm IC.
- MODIFY GO:0061136 regulation of proteasomal protein catabolic process -> GO:1901800 positive regulation.
- KEEP_AS_NON_CORE GO:2001125 negative regulation of translational frameshifting (self-regulation of its own synthesis).
- NEW GO:0170066 negative regulation of polyamine biosynthetic process (Oaz1 itself inactivates/degrades ODC).
