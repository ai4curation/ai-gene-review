# ureC (P41020, URE1_SPOPA) — Sporosarcina pasteurii urease alpha subunit

## What the protein is

- Reviewed Swiss-Prot entry P41020, 570 aa, strain ATCC 11859 / DSM 33 / NCIB 8841 /
  NCTC 4822 [file:SPOPA/ureC/ureC-uniprot.txt "STRAIN=ATCC 11859 / DSM 33 / NCIB 8841 / NCTC 4822"].
- Alpha (catalytic) chain of the three-chain bacterial urease: "Heterotrimer of UreA
  (gamma), UreB (beta) and UreC (alpha) subunits. Three heterotrimers associate to form
  the active enzyme" [file:SPOPA/ureC/ureC-uniprot.txt]. The entry is at protein-existence
  level 1 with 35 PDB cross-references.
- Catalysed reaction, recorded with experimental evidence
  (ECO:0000269|PubMed:30969470): urea + 2 H2O + H(+) = hydrogencarbonate + 2 NH4(+),
  RHEA:20557, EC 3.5.1.5. Pathway: "Nitrogen metabolism; urea degradation; CO(2) and
  NH(3) from urea (urease route): step 1/1".

## Active site: the nickel chemistry is all on this subunit

- UniProt: "Binds 2 nickel ions per subunit", with BINDING features at His137, His139,
  Lys220 (via carbamate, to both metals), His249, His275 and Asp363, each carrying
  ECO:0000269 evidence from the S. pasteurii structures, plus MOD_RES 220
  "N6-carboxylysine" and "Carboxylation allows a single lysine to coordinate two nickel
  ions" [file:SPOPA/ureC/ureC-uniprot.txt].
- Crystallography: "In the native enzyme, the coordination sphere of each of the two
  nickel ions is completed by a water molecule and a bridging hydroxide"
  [PMID:10368287 "A new proposal for urease mechanism based on the crystal structures of
  the native and inhibited enzyme from Bacillus pasteurii"].
- Independent spectroscopy: "The results indicate the presence of octahedrally
  coordinated Ni2+, in a sphere of six N/O donors at an average distance of 0.203 nm. An
  average of two histidine residues are bound to nickel." [PMID:8706719].
- Substrate complex: fluoride was used "to substitute the hydroxide acting as the
  co-substrate in the reaction, preventing the occurrence of the catalytic steps that
  follow substrate binding", giving the urease-urea structure [PMID:30969470]. UniProt
  records substrate-contact residues His139, Ala170, Lys220, His249 and Asp366 from that
  work, and ACTIVITY REGULATION "Inhibited by fluoride".
- Fluoride kinetics and the ten structures behind that chemistry: "The analysis of these
  structures revealed the presence of two fluoride anions coordinated to the Ni(II) ions
  in the active site, in terminal and bridging positions." [PMID:25113581].
- Further inhibitor complexes resolved on this enzyme: diamidophosphate [PMID:10368287],
  acetohydroxamate [PMID:10766443], phosphate [PMID:11713685], boric acid
  [PMID:15038715], beta-mercaptoethanol [PMID:9761912].

## Review calls

- GO:0009039 (EXP, PMID:30969470) and its IEA duplicate: ACCEPT. The activity is on the
  right subunit and is experimentally grounded in this organism.
- GO:0016151 nickel cation binding: ACCEPT — unlike the gamma-subunit rows (see
  ureA-notes.md), this one sits on the chain that actually holds the metals.
- GO:0016787 and GO:0016810: TOO_GENERAL, both entailed by the accepted GO:0009039.
- GO:0005737 and GO:0043419: ACCEPT.
- GO:0035550 urease complex: added as NEW. GOA gives it only to the beta subunit
  (through InterPro:IPR002019); the alpha chain, which is resolved in the same
  structures, has no complex row.

## CMMMech usage note (no edits made to CMMMech)

Six CMMMech records (calcite, vaterite, strontianite, smithsonite, brushite,
lithium-bearing-geothermal-brine) ground microbially induced calcite precipitation
(MICP) mechanisms to UniProtKB:P41020/P41021/P41022, with `functional_role` for P41020
"Catalytic alpha subunit (UreC; EC 3.5.1.5) of the nickel-dependent urease complex that
hydrolyzes urea into ammonia and carbamate/carbonate". That statement matches the
reviewed UniProt entry and the structural literature. Two caveats worth recording:

1. Each record's own evidence block is explicit that the grounding is representative
   rather than demonstrated in the cited study ("urease genes were not mutated or
   purified in this study", `supports: partial`), and this review found nothing that
   would strengthen it: no S. pasteurii urease knockout, complementation or
   purified-enzyme measurement appears in the MICP sources, and the reviewed entry's
   experimental evidence is structural and spectroscopic rather than phenotypic.
2. The enzyme is cytoplasmic ("SUBCELLULAR LOCATION: Cytoplasm"). Urea hydrolysis
   therefore happens inside the cell, and the carbonate/ammonium that drives
   extracellular mineral precipitation reaches the medium by transport and diffusion.
   A causal graph that places the urease reaction at the mineral surface, or that treats
   carbonate generation and precipitation as one compartment, overstates what the
   protein-level evidence shows.
