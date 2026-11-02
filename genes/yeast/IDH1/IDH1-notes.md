# IDH1 (YNL037C, P28834) notes

Evidence journal for the review (no paid deep research; built from UniProt and cached publications).

- NAD-IDH is a hetero-octamer of 4 Idh1 + 4 Idh2 built from Idh1/Idh2 heterodimers [PMID:16884682 "Yeast NAD+-specific isocitrate dehydrogenase (IDH) is an octamer of four IDH1 and four IDH2 subunits, and the basic structural unit of the enzyme is an IDH1/IDH2 heterodimer"].
- Idh1 is regulatory, Idh2 catalytic [PMID:11042198 "IDH2 was previously shown to contain the catalytic site, whereas IDH1 contributes regulatory properties including cooperativity with respect to isocitrate and allosteric activation by AMP"].
- Idh1 residues contribute to the Idh2 catalytic site [PMID:11042198 "each subunit contributes to the isocitrate binding site of the other"].
- Idh1 site binds isocitrate for AMP activation, not catalysis [PMID:11714283 "isocitrate binding by IDH2 for catalysis and with isocitrate binding by IDH1 being a prerequisite for allosteric activation by AMP"].
- Structures: regulatory and catalytic sites at subunit interfaces [PMID:18256028 "homologous but distinct regulatory and catalytic sites positioned at the interfaces between IDH1 and IDH2 subunits"].
- Physiology: idh mutants lose isocitrate/citrate-driven respiration [PMID:2198251 "markedly reduced capacity for utilization of either isocitrate or citrate for respiratory O2 consumption"]; activity correlates with growth on acetate/glycerol, low activity increases petites [PMID:11714283].
- Import: presequence-dependent; cytosolic holoenzyme only with presequence deleted [PMID:8626605 "Each subunit was found to be dependent upon its presequence for mitochondrial localization"]. Reactome TAS rows for cytosol/IMS (import reaction) removed.
- UniProt: "Also binds RNA; specifically to the 5'-untranslated leaders of mitochondrial mRNAs" [UniProt:P28834]. No GOA annotation; raised as a suggested question.
- Curation: IEA "enables" GO:0004449 marked over-annotated (IDH1 non-catalytic; contributes_to is right). NAD binding / CH-OH oxidoreductase IEA from the family signature marked over-annotated for this regulatory subunit.
