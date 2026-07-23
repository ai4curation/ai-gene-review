# ERCC4 (XPF) — gene review notes

UniProt: Q92889 (XPF_HUMAN); HGNC:3436; Gene: ERCC4 (syn. ERCC11, XPF, FANCQ). 916 aa.
EC=3.1.-.- (Mg2+ dependent hydrolase/endonuclease).

## Core biology (verified against cached publications)

XPF/ERCC4 is the **catalytic subunit** of the ERCC1-XPF structure-specific DNA
endonuclease. It houses the nuclease active site and makes the **5' incision** on the
damaged strand at ss/ds DNA junctions. ERCC1 is the non-catalytic partner that provides
additional DNA binding.

- UniProt FUNCTION: "Catalytic component of a structure-specific DNA repair endonuclease
  responsible for the 5-prime incision during DNA repair, and which is essential for
  nucleotide excision repair (NER) and interstrand cross-link (ICL) repair."
- Cofactor: Mg(2+) [PMID:10413517].
- Heterodimer with ERCC1; C-terminal (HhH)2 domain mediates dimerization; N-terminal
  nuclease/helicase-like region carries the catalytic domain.

### Endonuclease / catalytic subunit
- [PMID:8797827 "The XPF protein was purified from mammalian cells in a tight complex with ERCC1. This complex is a structure-specific endonuclease responsible for the 5' incision during repair."]
- [PMID:8797827 "...solve the catalytic function of the XPF-containing complex."]
- [PMID:10413517 "...determined that it is an endonuclease and can bind DNA in the absence of the ERCC1 subunit."]
- [PMID:10413517 "the N-terminal 378 amino acids of XPF are capable of binding and hydrolyzing DNA, while the C-terminal 214 residues are capable of binding specifically to ERCC1."]
- [PMID:10413517 "We propose that the N-terminal domain of XPF contributes to the junction-specific endonuclease activity observed during DNA repair and recombination events."]
- [PMID:22547097 "ERCC1-XPF is a heterodimeric, structure-specific endonuclease that cleaves single-stranded/double-stranded DNA junctions and has roles in nucleotide excision repair (NER), interstrand crosslink (ICL) repair, homologous recombination, and possibly other pathways."]
- [PMID:22547097 "In NER, ERCC1-XPF is recruited to DNA lesions by interaction with XPA and incises the DNA 5' to the lesion."]
- [PMID:16076955 "Human XPF-ERCC1 is a DNA endonuclease that incises a damaged DNA strand on the 5' side of a lesion during nucleotide excision repair and has additional role(s) in homologous recombination and DNA interstrand crosslink repair."]

### ssDNA binding / substrate recognition (ss/ds junction)
- [PMID:22483113 "Human XPF/ERCC1 is a structure-specific DNA endonuclease that nicks the damaged DNA strand at the 5' end during nucleotide excision repair."]
- [PMID:22483113 "A positively charged region within the second helix of the first HhH motif contacts the ssDNA phosphate backbone. One guanine base is flipped out of register..."]
- [PMID:16076955 "The central domain of ERCC1 binds ssDNA/dsDNA junctions with a defined polarity, preferring a 5' single-stranded overhang."] (ERCC1 side)
- ssDNA binding by XPF: [PMID:10413517] (binds DNA in absence of ERCC1).

### NER
- [PMID:8797827 "Nucleotide excision repair, which is defective in xeroderma pigmentosum (XP), involves incision of a DNA strand on each side of a lesion."]
- [PMID:22547097 "...mutations in the helix-hairpin-helix domain of ERCC1 and the nuclease domain of XPF abolished cleavage activity on model substrates."]
- [PMID:17055345 "...wild type XPF can complement XPF-deficient cells for repair of UV-induced DNA damage whereas the nuclease-inactive XPF proteins fail to do so, indicating that the nuclease activity of XPF is essential for nucleotide excision repair."]

### Interstrand crosslink (ICL) repair — 5' and 3' unhooking incisions
- [PMID:11790111 "XPF forms a heterodimeric complex with ERCC1 and is required for the repair of DNA interstrand cross-links. In association with ERCC1, it is involved in production of the 5' incision at the site of a psoralen interstrand cross-link as well as the 3' incision."]
- [PMID:14728600 "These results suggest that the XPF protein has important roles in the psoralen ICL-mediated DNA repair and mutagenesis."]
- [PMID:16678501 "These results indicate that XPF is required to form gamma-H2AX and likely double strand breaks in response to interstrand crosslinks in human cells."]
- [PMID:32034146 "The XPF-ERCC1 heterodimer is a structure-specific endonuclease that is essential for nucleotide excision repair (NER) and interstrand crosslink (ICL) repair in mammalian cells."]
- FANCA/spectrin recruitment to ICL foci: [PMID:12571280 "...FANCA and the known DNA repair protein XPF localize to the same nuclear foci."]

### Homologous recombination / single-strand annealing (SSA)
- [PMID:14734547 "The XPF/ERCC1 heterodimer is a DNA structure-specific endonuclease that participates in nucleotide excision repair and homology-dependent recombination reactions, including DNA single strand annealing and gene targeting."]
- [PMID:14734547 "Complex formation between hRad52 and XPF/ERCC1 concomitantly stimulates the DNA structure-specific endonuclease activity of XPF/ERCC1..."]
- Meiotic recombination (phylogenetic, yeast Rad1/Rad16/Mei-9): [PMID:10644440 "...support a distinct role for the XPF/ERCC1 junction-specific endonuclease during meiosis, most likely in the resolution of heteroduplex intermediates that arise during recombination."]

### SLX4 (FANCP) coordination
- [PMID:19596235 "Human SLX4 forms a multiprotein complex with the ERCC4(XPF)-ERCC1, MUS81-EME1, and SLX1 endonucleases..."]
- [PMID:24012755 "SLX4 assembles a telomere maintenance toolkit by bridging multiple endonucleases with telomeres."] and maps SLX4 interactions with SLX1, XPF, MUS81.
- Also PMID:19596236, PMID:19595721, PMID:19595722 (SLX4/BTBD12 binds XPF-ERCC1).

### Telomere functions (3' overhang removal; specialized/non-core)
- [PMID:14690602 "ERCC1/XPF-deficient cells retained the telomeric overhang after TRF2 inhibition, identifying this nucleotide excision repair endonuclease as the culprit in overhang removal."]
- [PMID:14690602 "...overhang processing is a prerequisite for NHEJ of telomeres."] and represses Telomeric DNA-containing Double Minute chromosomes (TDMs).
- [PMID:18812185 "overexpression of XPF induces telomere shortening... XPF-ERCC1 can function as a negative mediator of telomere length maintenance."]
- [PMID:18812185] shows two distinct mechanisms: TRF2 control (nuclease-dependent) vs telomere-length modulation (nuclease-independent). Establishes the NOT annotation for telomerase inhibitor activity — XPF does NOT act as a telomerase inhibitor.
- [PMID:17055345 "...both wild type XPF and nuclease-inactive XPF proteins... are able to rescue TRF2-mediated telomere shortening... reveal an unanticipated nuclease-independent function of XPF in TRF2-mediated telomere shortening."]

### Regulation / PTM
- Acetylation at Lys911 by KAT5/TIP60 promotes XPF-ERCC1 assembly by disrupting the
  Glu907-Lys911 salt bridge, exposing a second ERCC1 binding site; deacetylated by SIRT1
  [PMID:32034146].

## Disease (all reflect the same endonuclease deficiency)
- Xeroderma pigmentosum group F (XP-F, MIM:278760)
- XFE progeroid syndrome (XFEPS, MIM:610965) — R153P [PMID:17183314]
- XPF/Cockayne syndrome (XPF/CS) [PMID:23623389]
- Fanconi anemia complementation group Q (FANCQ, MIM:615272) — L230P, R689S, S786F
  [PMID:23623386, PMID:24027083]

## Curation decisions summary
- Core MF = structure-specific 5' incision endonuclease (ss/ds junction); catalytic subunit.
  Best specific MF ids: GO:0000014 (single-stranded DNA endodeoxyribonuclease activity),
  GO:1990599 (3' overhang ssDNA endonuclease activity, telomere).
- All GO:0005515 "protein binding" (and GO:0042802 identical protein binding) → MARK_AS_OVER_ANNOTATED
  (uninformative; functional partners ERCC1/SLX4/RAD52/TRF2/FANCA captured elsewhere).
- Telomere / recombination / meiotic / NHEJ processes → KEEP_AS_NON_CORE (genuine but specialized).
- Negated GO:0010521 telomerase inhibitor activity → ACCEPT the negation (informative NOT).
- No REMOVE and no UNDECIDED: all key claims verifiable in cached abstracts.
</content>
</invoke>
