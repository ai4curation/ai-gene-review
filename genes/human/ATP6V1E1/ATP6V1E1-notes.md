# ATP6V1E1 Research Notes

## Gene Identity
- UniProt: P36543 (VATE1_HUMAN)
- Gene symbol: ATP6V1E1 (also known as ATP6E, ATP6E2)
- Protein: V-type proton ATPase subunit E 1; 226 amino acids, ~26 kDa
- Three isoforms from alternative splicing (P36543-1, P36543-2, P36543-3)

## Core V-ATPase Biology

ATP6V1E1 encodes the E subunit of the V1 peripheral sector of the vacuolar-type H+-ATPase (V-ATPase). Subunit E, together with subunit G, forms the three peripheral stalks that hold the catalytic head fixed relative to the membrane-embedded V0 domain during rotation.

[PMID:33065002 "The V1 complex consists of three catalytic AB heterodimers that form a heterohexamer, three peripheral stalks each consisting of EG heterodimers, one central rotor including subunits D and F, and the regulatory subunits C and H"]

[PMID:32001091 "V-ATPases are membrane-embedded protein complexes that function as ATP hydrolysis-driven proton pumps. V-ATPases are the primary source of organellar acidification in all eukaryotes, making them essential for many fundamental cellular processes."]

The E subunit structure has been resolved in the complete human V-ATPase cryo-EM structures (PDB: 6WLZ, 6WM2, 6WM3, 6WM4), confirming its position in three peripheral stalk EG heterodimers.

## Interaction with Aldolase

Lu et al. (2001) identified aldolase (ALDOC) as a direct binding partner of the V-ATPase E subunit using yeast two-hybrid and confirmed it biochemically. This may couple glycolytic ATP supply to V-ATPase activity.

[PMID:11399750 "A screen for proteins that bind the V-ATPase E subunit using the yeast two-hybrid assay identified the cDNA clone coded for aldolase, an enzyme of the glycolytic pathway."]

[PMID:11399750 "In yeast cells deficient in aldolase, the peripheral V(1) domain of V-ATPase was found to dissociate from the integral membrane V(0) domain, indicating direct coupling of glycolysis to the proton pump."]

## Interaction with RAB11B and Acidosis-Induced Trafficking

Oehlke et al. (2011) showed the E subunit interacts with RAB11B (Rab11b) and its effector Rip11, which regulate V-ATPase trafficking to the apical membrane of salivary duct cells under acidosis conditions.

[PMID:20717956 - abstract: "Rab11b and its effector Rip11 regulate the acidosis-induced traffic of V-ATPase in salivary ducts."]

## Subcellular Localization

- Primary: lysosomal membrane, as part of V-ATPase complex
- Also: apical plasma membrane in kidney and salivary duct epithelial cells (important for urinary acidification / acid-base homeostasis)
- Also: endosomes, clathrin-coated vesicle membrane, synaptic vesicle membrane

[PMID:29993276 - localization to apical membrane of thick ascending limb and distal convoluted tubule in kidney]

## Role in mTORC1 Amino Acid Sensing

Like subunit D, subunit E is part of the V1 sector that interacts with the Ragulator complex on lysosomes to facilitate mTORC1 activation by amino acids.

[PMID:22053050 "Immunoblot assays with antibodies to endogenous V0 (c and d1) and V1 (A, B2, and D) subunits confirmed that Ragulator co-immunoprecipitates with the V0 and V1 domains"]

## Disease Association: Cutis Laxa (ARCL2C)

Loss-of-function variants in ATP6V1E1 cause autosomal recessive cutis laxa type 2C (ARCL2C; MIM:617402). Patients show congenital skin laxity, delayed fontanelle closure, facial dysmorphism, hypotonia, and cardiovascular involvement.

[PMID:28065471 - "Mutations in ATP6V1E1 or ATP6V1A cause autosomal-recessive cutis laxa."]

The variants Pro-128 and Trp-212 (substitution of normal residues) are causative. Disease phenotype reflects widespread V-ATPase dysfunction in connective tissue remodeling pathways.

## Tissue Distribution

Ubiquitous expression (housekeeping); highest expression in skin; also present in kidney distal nephron (thick ascending limb and distal convoluted tubule). A testis-specific isoform exists (from separate gene ATP6V1E2).

[PMID:12036578 - "A human gene, ATP6E1, encoding a testis-specific isoform of H(+)-ATPase subunit E."]

## Curation Notes

- The "protein binding" annotations from interactome studies (IPI from PMID:16169070, PMID:35271311) are generic high-throughput entries; the most informative specific interaction is ATPase binding (GO:0051117) via interaction with RAB11B documented in PMID:20717956.
- The PMID:21784977 "protein binding" annotation is suspicious for ATP6V1E1 — that paper concerns tristetraprolin (ZFP36) and CCL3 mRNA regulation, not V-ATPase; likely a curation error.
- The apical plasma membrane annotation (EXP from PMID:29993276) is well-supported for kidney epithelium where V-ATPase functions in acid excretion.
- Regulation of macroautophagy (NAS from PMID:22982048) is an indirect V-ATPase class effect; no specific evidence for subunit E in macroautophagy regulation beyond lysosomal acidification.
