# AZI2 (NAP1) review notes

UniProt: Q9H6S1. Gene: AZI2 (5-azacytidine-induced protein 2); synonyms NAP1 (NAK-associated
protein 1), TBKBP2, TILP. 392 aa. Two coiled-coil regions (40-76, 102-196), a homodimerization
region (1-197), and a TBK1/IKKε-binding region (216-257; the "TBD" Pfam PF12845 TBK1-binding
domain). Cytoplasmic. Subject to K48-linked polyubiquitination by TRIM38 (by similarity, mouse).

## Core function: adapter/positive regulator of TBK1 and IKKε

[PMID:14560022 "we identify NAP1 (for NAK-associated protein 1), a protein that interacts with
NAK and its relative IKK epsilon (also known as IKKi). NAP1 activates NAK and facilitates its
oligomerization."] — This is the foundational identification. NAP1 binds TBK1 (NAK) and IKBKE
(IKKε), activates TBK1, facilitates its oligomerization, and the NAK-NAP1 complex phosphorylates
Ser536 of p65/RELA. NAP1 enhances NF-κB-dependent reporter activation; depletion reduces it.
[PMID:14560022 "Depletion of NAP1 reduced NF-kappaB-dependent reporter gene expression"].
UniProt FUNCTION: "Adapter protein which binds TBK1 and IKBKE playing a role in antiviral innate
immunity. Activates serine/threonine-protein kinase TBK1 and facilitates its oligomerization.
Enhances the phosphorylation of NF-kappa-B p65 subunit RELA by TBK1."

## Innate antiviral immunity / type I IFN

[PMID:17142768 (Sasai et al., abstract-only in cache) "NAK-associated protein 1 participates in
both the TLR3 and the cytoplasmic pathways in type I IFN induction"] — NAP1 is a shared adaptor
downstream of TLR3 (via TICAM1/TRIF) and the cytoplasmic RIG-I/MDA5 pathway feeding IRF3
activation and type I IFN (IFN-β). This paper is the ComplexPortal source for the NAS annotations:
defense response to virus (GO:0051607), type I IFN-mediated signaling (GO:0060337), and
serine/threonine protein kinase complex (GO:1902554, the TBK1/IKKε-NAP1 complex CPX-6038).

NAP1 also participates in IFN-β promoter activation via TICAM1/TRIF (UniProt FUNCTION,
PubMed:15611223 — not in cache, abstract elsewhere). [PMID:21931631 "Functional dissection of the
TBK1 molecular network"] confirms NAP1 in the TBK1 interactome and functional network.

## Selective autophagy adaptor link

[PMID:30459273 "Mechanistic insights into the interactions of NAP1 with the SKICH domains of NDP52
and TAX1BP1"] — Crystal structures (5Z7G, 5Z7L) of NAP1 33-75 bound to the SKICH domains of the
autophagy receptors NDP52 (CALCOCO2) and TAX1BP1 (TAXBP1). NAP1 (and its paralog SINTBAD) bridge
these cargo receptors to TBK1, recruiting/activating TBK1 at autophagic cargo. This places NAP1 in
the selective-autophagy axis as a TBK1-recruiting adaptor.

## Interactions (basis for IPI protein binding annotations)

- PMID:14743216 — TNF-α/NF-κB pathway physical+functional map: interaction with TBK1 (Q9UHD2).
- PMID:21903422 — dynamic innate-immunity interaction network (type I IFN): TBK1 (Q9UHD2).
- PMID:21931555 — vaccinia virus C6 binds TBK1 adaptors (NAP1/TANK/SINTBAD); IPI with C6
  (OPG029/P17362) and TBK1 (Q9UHD2). C6 is a viral antagonist of IRF3/IRF7 activation.
- PMID:22014111 — flavivirus NS3/NS5 Y2H screen: interaction with a flavivirus protein (Q9E7P0).
- PMID:29251827 — TBK1 interactome (TTC4 study): TBK1 (Q9UHD2).
- PMID:32707033 — kinase interaction network: TBK1 (Q9UHD2).
Most IPI "protein binding" annotations record the central TBK1 interaction (functionally important
but uninformative as bare GO:0005515).

## Negative regulation of NF-κB (IEA from mouse ortholog)

GO:0043124 (negative regulation of canonical NF-κB signaling), IEA via Ensembl Compara from mouse
ortholog Q9QYP6 (ECO:0000265, GO_REF:0000107). This is interesting because the human characterization
(PMID:14560022) shows NAP1 *potentiates* NF-κB. The mouse-derived "negative regulation" may reflect a
context-specific role. Keep as non-core given the dominant positive/adaptor role and the
ortholog-transfer basis; do not remove an Ensembl orthology-based annotation without contradicting
evidence (the human paper shows positive regulation, which is a different assay context).

## Summary of action plan
- Core: TBK1/IKKε adaptor and positive regulator (no clean MF GO term for "kinase activator/adaptor";
  the best capture is the kinase complex CC + the IFN/antiviral BP). Bare protein binding -> KEEP_AS_NON_CORE.
- Cytoplasm (EXP, IBA) -> ACCEPT (core localization where the complex acts) / IBA is_active_in ACCEPT.
- IEA cytoplasm -> KEEP_AS_NON_CORE (redundant electronic).
- defense response to virus, type I IFN signaling, kinase complex (NAS, ComplexPortal) -> ACCEPT (core).
- negative regulation of canonical NF-κB (IEA ortholog) -> KEEP_AS_NON_CORE.
</content>
</invoke>
