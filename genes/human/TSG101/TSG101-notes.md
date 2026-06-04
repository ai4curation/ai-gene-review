# TSG101 review notes

## Scope

TSG101 is reviewed in the PN autophagophore sealing branch as an ESCRT-I component. PN entries without PMIDs were used as context only. The main curation problem is that TSG101 has many true but non-core annotations from viral budding, cytokinesis, exosome release, and interaction screens; the conserved core is ESCRT-I ubiquitin/PTAP-motif adaptor function in endosomal sorting and reverse-topology membrane scission, with a PN-relevant role in phagophore/autophagosome closure.

## Evidence synthesis

TSG101 is a core ESCRT-I subunit and ubiquitin-binding adaptor. UniProt states that it is a "Component of the ESCRT-I complex", "Binds to ubiquitinated cargo proteins", and is "required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies" [file:human/TSG101/TSG101-uniprot.txt, "Component of the ESCRT-I complex"; file:human/TSG101/TSG101-uniprot.txt, "Binds to ubiquitinated cargo proteins"; file:human/TSG101/TSG101-uniprot.txt, "required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies"]. It also states that the ESCRT-I complex contains "TSG101, VPS28, a VPS37 protein" and MVB12A/B or UBAP1 [file:human/TSG101/TSG101-uniprot.txt, "which consists of TSG101, VPS28, a VPS37 protein"]. These lines support ESCRT-I complex membership, ubiquitin binding, MVB assembly/sorting, endosome-to-lysosome transport context, and membrane fission.

The endosomal sorting literature supports the same core. Hrs/ESCRT work reports that ESCRT complexes sort membrane proteins into "multivesicular bodies and lysosomes or vacuoles", that Hrs binds the "ESCRT-I subunit Tsg101", and that Hrs mediates "the initial recruitment of ESCRT-I to endosomes" [PMID:12900395, "multivesicular bodies and lysosomes or vacuoles"; PMID:12900395, "ESCRT-I subunit Tsg101"; PMID:12900395, "the initial recruitment of ESCRT-I to endosomes"]. The HIV budding paper also states that the TSG101 UEV domain binds "to ubiquitin" and that TSG101 participates "in the Vps pathway to form multivesicular bodies" [PMID:11595185, "to ubiquitin"; PMID:11595185, "in the Vps pathway to form multivesicular bodies"]. The viral part of that paper supports viral-budding annotations, but those should be treated as non-core host-pathogen exploitation of ESCRT-I.

The PN-specific autophagy connection is best represented as autophagosome assembly/phagophore closure rather than generic macroautophagy. A mammalian phagophore-closure study reports that "VPS37A directs ESCRT recruitment for phagophore closure", identifies "the ESCRT-I subunit VPS37A as a critical component for phagophore closure", and says "the core ESCRT-I components TSG101 and VPS28" are "required for autophagosome completion" [PMID:31519728, "VPS37A directs ESCRT recruitment for phagophore closure"; PMID:31519728, "the ESCRT-I subunit VPS37A as a critical component for phagophore closure"; PMID:31519728, "the core ESCRT-I components TSG101 and VPS28"; PMID:31519728, "required for autophagosome completion"]. The yeast ESCRT closure paper provides conserved mechanistic context by stating that ESCRT "mediates AP sealing" and "catalyzes AP closure" [PMID:31010855, "mediates AP sealing"; PMID:31010855, "catalyzes AP closure"]. Therefore the PN-projected `GO:0000045 autophagosome assembly` is a better new term than broad `macroautophagy` or `autophagosome maturation`.

Many interaction rows should not be accepted as informative molecular functions. The useful molecular functions are ubiquitin binding and ESCRT-I adaptor/scaffold context; generic `protein binding`, `protein-containing complex binding`, and similar binding rows lose the biology. The negated `ubiquitin conjugating enzyme activity` row should be accepted because TSG101 is a UEV-domain protein that binds ubiquitin/PTAP motifs but is not an active E2 enzyme.

## Falcon

Falcon deep research was started for TSG101 on 2026-06-02 but timed out after 600 seconds and did not produce a usable report. The review therefore relies on UniProt, cached primary literature, and PN context rather than Falcon output.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording framed TSG101's autophagy role in the Proteostasis Network context as ESCRT-I participation in phagophore/autophagosome closure, best represented as autophagosome assembly rather than generic macroautophagy.
