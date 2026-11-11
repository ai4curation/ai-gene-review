# Curation Notes for Escherichia phage lambda Gene Z (gpZ, P03731)

## Summary of Gene Product Function
Gene `Z` encodes the tail completion protein gpZ (UniProt: `P03731`, 192 aa, ~21.6 kDa), an essential tail completion protein that acts at the proximal end of the bacteriophage lambda tail. Following polymerization of the hexameric major tail protein (gpV) tube and capping by the tail terminator protein (gpU), gpZ acts on the gpU-capped tail to complete tail morphogenesis and render the tail competent to join the DNA-filled capsid at the portal-neck vertex [file:LAMBD/Z/Z-uniprot.txt, "CC   -!- FUNCTION: Stabilizes the tail structure and acts as a connector between\nCC       the end of tail and the portal vertex of the capsid. {ECO:0000305}."]. Without gpZ action, tails attach to heads morphologically in some conditions to form non-infectious particles incapable of productive DNA injection into *Escherichia coli*.

## Literature & Structural Evidence
- **Cryo-EM structure of Ur-lambda (`PMID:41237242`)**: Although background literature places gpZ at the portal-neck interface, cryo-EM reconstruction of mature Ur-lambda resolved gpB, gpW, gpFII, and gpU at the portal-neck vertex but did not resolve gpZ [PMID:41237242, "Like those previous studies, we did not resolve gpC, gpK, or gpZ."].
- **Classical tail morphogenesis (`PMID:1003470`, UniProt `P03731`)**: Katsura (1976) characterized the assembly pathway and polymorphism of the lambda tail, establishing gpZ as a tail completion factor synthesized in the host cytoplasm that stabilizes the completed tail structure and connects the tail to the capsid portal vertex [file:LAMBD/Z/Z-uniprot.txt, "CC   -!- FUNCTION: Stabilizes the tail structure and acts as a connector between\nCC       the end of tail and the portal vertex of the capsid. {ECO:0000305}."].

## Review of Existing GO Annotations
- `GO:0098015` (`virus tail`, `IDA` from `PMID:1003470` and `IEA` from `GO_REF:0000043`): **ACCEPT**. gpZ acts at the proximal neck/tail junction of the bacteriophage lambda tail.
- `GO:0030430` (`host cell cytoplasm`, `IEA` from `GO_REF:0000044`): **KEEP_AS_NON_CORE**. Newly synthesized gpZ polypeptides reside transiently in the *E. coli* cytoplasm during lytic tail morphogenesis, which is a general biosynthetic location rather than a defining core function.
