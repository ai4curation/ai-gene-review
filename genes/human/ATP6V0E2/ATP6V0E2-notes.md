# ATP6V0E2 (Q8NHE4) research notes

## Identity
- Human gene ATP6V0E2 (synonyms ATP6V0E2L, C7orf32), HGNC:21723, chromosome 7.
- Encodes "V-type proton ATPase subunit e 2" (e2), an 81-aa, ~9.2 kDa integral membrane protein.
- [UniProt "RecName: Full=V-type proton ATPase subunit e 2; Short=V-ATPase subunit e 2; AltName: Full=Lysosomal 9 kDa H(+)-transporting ATPase V0 subunit e2"].

## Function / complex
- It is one of two e-subunit forms (e1 = ATP6V0E1; e2 = ATP6V0E2) of the V0 membrane sector of the vacuolar H+-ATPase (V-ATPase).
- V-ATPase is a two-sector rotary pump: peripheral V1 hydrolyzes ATP, membrane-integral V0 translocates protons.
  [UniProt "Subunit of the V0 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons"].
- The V0 sector includes "the proton transport subunit a, a ring of proteolipid subunits c9c'', rotary subunit d, subunits e and f, and the accessory subunits ATP6AP1/Ac45 and ATP6AP2/PRR" [UniProt SUBUNIT].
- V-ATPase "is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it is responsible for acidifying the extracellular environment" [UniProt FUNCTION].
- Belongs to the V-ATPase e1/e2 subunit family [UniProt SIMILARITY].

## Evidence that e2 is functionally essential for the pump
- PMID:17350184 cloned ATP6V0E2 and tested it functionally by yeast complementation:
  [PMID:17350184 "We show by complementation studies in a yeast strain deficient for the ortholog of this subunit, that either form of the e-subunit is essential for proper proton pump function."]
  This is the basis for the IGI annotations to GO:0046961 (proton-transporting ATPase activity, rotational mechanism) and GO:1902600 (proton transmembrane transport), with WITH=UniProtKB:Q3E7B6 (yeast/ortholog e-subunit).
- The same paper notes the gene has a restricted tissue distribution distinct from the ubiquitous e1:
  [PMID:17350184 "in contrast to the ubiquitously expressed gene encoding the e1 subunit (previously called e), this novel gene is expressed in a more restricted tissue distribution, particularly kidney and brain."]
- UniProt TISSUE SPECIFICITY: [UniProt "Isoform 1 is expressed at high levels in heart, brain and kidney and also detected in inner ear epithelium, vestibule, testis, epididymis and bladder."]

## Localization
- UniProt SUBCELLULAR LOCATION: Membrane; Multi-pass membrane protein. Cytoplasmic vesicle, clathrin-coated vesicle membrane (by similarity to Q5EB76). Cytoplasmic vesicle, secretory vesicle, synaptic vesicle membrane (by similarity to Q5EB76).
  [UniProt "SUBCELLULAR LOCATION: Membrane {ECO:0000255}; Multi-pass membrane protein {ECO:0000255}. Cytoplasmic vesicle, clathrin-coated vesicle membrane {ECO:0000250|UniProtKB:Q5EB76}"].
- Topology: two transmembrane helices (8-28, 36-56), N-terminus lumenal, C-terminus lumenal [UniProt FT TRANSMEM/TOPO_DOM]. (Note: UniProt "Multi-pass" but the chain shows 2 TM helices.)
- Reactome places the V-ATPase (and thus this subunit) on lysosomal membrane, endosome membrane, and phagocytic (phagosome) membrane in the context of organelle acidification reactions and mTORC1/amino-acid-sensing reactions. These are TAS pathway-context annotations transferred to the whole complex.

## Annotation assessment summary
- Core molecular function: contribute to proton-transporting ATPase activity (rotational mechanism) as a V0 membrane subunit; core process: proton transmembrane transport / vacuolar acidification; core localization: V0 domain / membrane of acidified organelles.
- IBA (GO_REF:0000033) and ISS (GO_REF:0000024 from Q2KIB5/Q3E7B6) and IGI (PMID:17350184) annotations to proton transport, V0 domain membership, and rotational ATPase activity are all consistent and well-supported by the experimental complementation data and structural family assignment.
- GO:0046961 with qualifier "contributes_to"/"enables" is appropriate because a single subunit contributes to the holoenzyme activity rather than enabling it alone. The IBA uses contributes_to (correct); the IEA/IGI use enables (acceptable per GOA convention for complex subunits but contributes_to is more precise).
- The various Reactome lysosomal/endosomal/phagosomal membrane TAS annotations are consistent with the known localization of V-ATPase; they are acceptable as non-core compartment annotations.
- The Reactome mTORC1/amino-acid-sensing reactions (R-HSA-9639286 etc.) annotate the V-ATPase complex's location to lysosomal membrane; these are reasonable as compartment annotations but reflect the mTORC1 signaling literature, not a direct e2-specific role.
- GO:0016241 regulation of macroautophagy (NAS, PMID:22982048): the cited paper (Höhn et al.) is a lipofuscin/autophagy study in senescent fibroblasts that does NOT mention ATP6V0E2 specifically; it concerns general lysosomal/autophagy biology. This is a weak/over-broad annotation for this subunit — V-ATPase acidification is upstream of autophagy generally, but assigning "regulation of macroautophagy" to this specific subunit from this reference is an over-annotation. Mark as over-annotated.
- GO:0042625 (ATPase-coupled ion transmembrane transporter activity, ISS): generic; the more specific GO:0046961 (rotational-mechanism proton ATPase) is the better term, and e2 contributes to rather than enables transporter activity. Treat as a less-specific overlap; keep as non-core / over-annotated relative to GO:0046961.
- No bare "protein binding" (GO:0005515) annotation present in this GOA.

## Proposed actions (high level)
- ACCEPT: proton transmembrane transport (IBA, IGI), V0 domain membership (IBA, ISS, IEA GO:0033179), rotational ATPase activity (IBA contributes_to; IGI), membrane (NAS/IEA), vacuolar acidification (ISS).
- KEEP_AS_NON_CORE: lysosomal membrane, endosome membrane, phagocytic vesicle membrane, clathrin-coated vesicle membrane, synaptic vesicle membrane (compartment annotations).
- MARK_AS_OVER_ANNOTATED: regulation of macroautophagy (NAS from non-specific ref); ATPase-coupled ion transmembrane transporter activity (generic, superseded by GO:0046961).
