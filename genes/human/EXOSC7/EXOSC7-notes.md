# EXOSC7 notes

EXOSC7/RRP42 is one of the six RNase PH-like subunits of the human Exo-9 RNA exosome core. It is a non-catalytic scaffold component: the human core binds and presents RNA substrates, while hydrolysis is carried by associated DIS3, DIS3L, and EXOSC10/RRP6 ribonucleases rather than by EXOSC7 itself [PMID:20531389, "The nine-subunit core of the eukaryotic exosome is catalytically inactive and may have an architectural function and mediate substrate binding."].

The accepted complex calls are nuclear, nucleolar, and cytoplasmic variants of the RNA exosome. Human core-exosome preparations and ComplexPortal records place EXOSC7 with EXOSC8 and EXOSC9 in all of those variants, and the Reactome cytosolic/nuclear/nucleolar events all use the same Exo-9 core with different cofactors or catalytic subunits.

The GO:0035925 mRNA 3'-UTR AU-rich region binding IBA is over-propagated to EXOSC7. The PANTHER IBD is at PTN000120503, above the human RRP42, RRP43 and RRP45 leaves, but the human direct seeds in PMID:16912217 support AU-rich RNA binding by PM-Scl-75/EXOSC9 and OIP2/EXOSC8, plus EXOSC4/RRP41, not EXOSC7/RRP42.

The bare GO:0005515 IPI rows are preserved one-for-one, including the duplicate PMID:11812149 / UniProtKB:Q9Y3B2 row that appears in the GOA feed once from IntAct and once from UniProt. They are all removed only under the project protein-binding policy; the WITH/FROM values stay on the rows as the interaction receipts.

The PTHR11097 family review records two well-supported PAINT nodes for exosome complex propagation and an over-broad PAINT node for AU-rich RNA binding. No production GO-CAM in `gocams/index.tsv` names EXOSC7, EXOSC8 or EXOSC9, and the RNA exosome is a large reusable machinery rather than a compact new module for just this PANTHER family.
