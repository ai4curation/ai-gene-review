# CHMP6 notes

## Review focus

CHMP6 is the human Vps20 ortholog and a core ESCRT-III pathway component. For the proteostasis network review, its most defensible core role is not a generic "protein binding" or broad ESCRT pleiotropy label, but ESCRT-II-to-ESCRT-III handoff on endosomal membranes, MVB cargo sorting, and VPS4-coupled ESCRT-III remodeling needed for lysosomal degradation of membrane cargo.

## Direct evidence

- CHMP6 is a myristoylated ESCRT-III protein that directly links ESCRT-II to ESCRT-III. Katoh et al. identify it as "a human orthologue of yeast Vps20" and report direct interactions with CHMP4b and EAP20/VPS25; the paper concludes that "CHMP6 acts as an acceptor for ESCRT-II on endosomal membranes and regulates cargo sorting" [PMID:15511219 "CHMP6 acts as an acceptor for ESCRT-II on endosomal membranes and regulates cargo sorting"].
- The same work supports membrane/endosome/MVB localization. Overexpressed CHMP6-GFP localized to punctate cytoplasmic/perinuclear structures, accumulated LBPA in the CHMP6-positive area, and the authors concluded that "membrane-bound CHMP6-GFP colocalized to endosome-like organelles, including MVBs" [PMID:15511219 "membrane-bound CHMP6-GFP colocalized to endosome-like organelles, including MVBs"]. The dominant-negative phenotype caused accumulation of ubiquitinated proteins and endocytosed EGF [PMID:15511219 "Ubiquitinated proteins and endocytosed EGF continuously accumulated in CHMP6-GFP-expressing cells"].
- ESCRT-II depletion work supports CHMP6 in EGFR lysosomal targeting/downregulation. EAP20 bound the N-terminal half of CHMP6/ESCRT-III, and depletion of EAP20/ESCRT-II and CHMP6/ESCRT-III "inhibited lysosomal targeting and downregulation of the epidermal growth factor receptor" [PMID:16973552 "depletion of EAP20/ESCRT-II and CHMP6/ESCRT-III inhibited lysosomal targeting and downregulation of the epidermal growth factor receptor"].
- VPS4 recognition of CHMP6 is mediated by a type-2 MIT-interacting motif (MIM2). The VPS4A MIT-CHMP6 MIM2 structure and mutagenesis show that the CHMP6 170-181 region recruits VPS4; mutations blocking VPS4 MIT-MIM2 binding also block ferroportin downregulation, which supports CHMP6 in cargo delivery through MVB sorting to lysosomal degradation [PMID:18606141 "mutations in the CHMP6 MIM2 element that block VPS4A MIT binding also block ferroportin downregulation"].
- CHMP6 has a conserved ESCRT-III autoinhibited/open behavior. Comparative analysis of core ESCRT-III proteins including hVps20/CHMP6 showed that C-terminal truncation unmasks endosomal membrane association and polymerization, causing ubiquitinated cargo accumulation on enlarged endosomes [PMID:17547705 "removing approximately 40 amino acids from the C-terminus of each protein unmasks a common ability to associate with endosomal membranes and assemble into large polymeric complexes"].
- UniProt summarizes the same core mechanism: CHMP6 is a probable ESCRT-III component involved in MVB formation and ubiquitinated cargo sorting, and "probably serves as an acceptor for the ESCRT-II complex on endosomal membranes" [UniProt:Q96FZ7 "probably serves as an acceptor for the ESCRT-II complex on endosomal membranes"].

## Annotation decisions

- Accept as core: ESCRT III complex, ESCRT III complex assembly, endosome/late endosome/MVB membrane localization, MVB assembly, MVB sorting pathway, ubiquitin-dependent protein catabolic process via MVB sorting, late endosome to lysosome transport, membrane fission, negative regulation of EGFR activity as a direct cargo-degradation consequence, and protein-containing complex binding where it reflects ESCRT-II/ESCRT-III handoff rather than generic binding.
- Modify broad transport terms such as vacuolar transport, late endosome-to-vacuole transport via MVB sorting, vesicle fusion with vacuole, multivesicular body-lysosome fusion, and regulation of protein catabolic process to the more specific MVB sorting / late endosome to lysosome transport / ubiquitin-dependent MVB catabolism terms.
- Mark generic protein binding as over-annotated. The interactions are real, but GO:0005515 erases the meaningful ESCRT-II, CHMP4, and VPS4 context.
- Treat viral budding as over-annotated for CHMP6. Broad ESCRT papers and dominant-negative constructs connect ESCRT-III integrity to budding, but CHMP6-specific depletion did not reduce HIV-1 release/infectivity [PMID:16973552 "HIV-1 release and infectivity were not reduced by efficient small interfering RNA depletion of EAP20/ESCRT-II or CHMP6/ESCRT-III"], and another study explicitly states that "Several ESCRT functions, including HIV budding, are insensitive to CHMP6 depletion" [PMID:18606141 "Several ESCRT functions, including HIV budding, are insensitive to CHMP6 depletion"].
- Keep nuclear envelope sealing/reassembly, nuclear pore, midbody abscission, kinetochore/microtubule, plasma membrane repair, autophagy/macroautophagy/autophagosome/amphisome/lysosomal membrane, cytosol, and extracellular exosome annotations as non-core or over-extended ESCRT family contexts unless the annotation has direct CHMP6-specific evidence. These processes are PN-relevant as ESCRT outputs, but they do not define CHMP6's core proteostasis function as well as endosomal cargo sorting and ESCRT-III assembly/recycling do.
- The negated exosome secretion annotation should be retained as a supported NOT annotation rather than converted into a positive functional claim; the source paper is about syntenin-ALIX exosome biogenesis and does not make CHMP6 a positive regulator of exosome secretion.

## Literature access notes

- A fetch attempt for PMID:14583093 hit an HTTP 429 rate limit, so I did not use that paper as evidence in the review.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording framed CHMP6's endolysosomal cargo-quality-control role as its best-supported Proteostasis Network role.
