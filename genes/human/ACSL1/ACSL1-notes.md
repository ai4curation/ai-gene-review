# ACSL1 (P33121) curation notes

**Provenance note:** provider deep research (Falcon) failed with HTTP 402 Payment
Required, and perplexity is not configured in this environment. No
`ACSL1-deep-research-*.md` file exists. This manual synthesis, built from the UniProt
record, the cached publications in `publications/`, and targeted PubMed searches (papers
fetched into the cache with `just fetch-pmid`), replaces it.

## Identity and family

- Long-chain-fatty-acid--CoA ligase 1, EC 6.2.1.3; ANL superfamily (AMP-binding domain),
  one of five ACSL isoforms (ACSL1, 3, 4, 5, 6). Three isoforms by alternative splicing.
- Mg2+-dependent; reaction: long-chain fatty acid + ATP + CoA = long-chain acyl-CoA + AMP +
  PPi [file:human/ACSL1/ACSL1-uniprot.txt "Reaction=a long-chain fatty acid + ATP + CoA = a long-chain fatty acyl-"].
- Tissue: high in liver, heart, skeletal muscle, kidney, adipose; erythroid cells.

## Activity and substrate range

- UniProt: "Catalyzes the conversion of long-chain fatty acids to their active form
  acyl-CoAs for both synthesis of cellular lipids, and degradation via beta-oxidation";
  human ACSL1 "Preferentially uses palmitoleate, oleate and linoleate" (PMID:24269233).
- Human ACSL1 complements the yeast faa1 faa4 acyl-CoA synthetase mutant in the
  sphingosine-1-phosphate to glycerophospholipid pathway (activation of
  trans-2-hexadecenoic acid and palmitate) [PMID:24269233 "in addition to the previously
  identified ACSL family members (ACSL1, 3, 4, 5, and 6), we found that ACSVL1, ACSVL4, and
  ACSBG1 also restored metabolism"; PMID:22633490 "mammalian ACSL family members are
  acyl-CoA synthetases involved in the sphingolipid-to-glycerolipid metabolic pathway"].
- Overexpression in hepatoma cells increases ACS activity [PMID:22022213 "Overexpression
  of FATP2, FATP4 and ACSL1 highly increased ACS activity as well as the uptake of"].
- Arachidonate, EETs/HETEs, phytanate and pristanate activities are inferred from the rat
  ortholog (P18163; rat IDA annotations exist in QuickGO) — "By similarity" in UniProt.

## Subcellular location

- Mitochondrial outer membrane (rat IDA; human hepatoma IF) [PMID:22022213 "ACSL1 was
  located at mitochondria in both cell lines"; PMID:24503477 "intracellular localization of
  FATP4 to the endoplasmic reticulum, and of ACSL1 to mitochondria"].
- ER membrane (human, HeLa expression) [PMID:24269233 "All 8 ACSs were localized either
  exclusively or partly to the endoplasmic reticulum (ER)"]. In liver ~50% of ACSL1 is on ER
  [PMID:30190326 "In the liver, however, about 50% of ACSL1 is located on the endoplasmic
  reticulum (ER)"].
- Peroxisomal membrane: rat IDA only; not shown for human.
- **Lipid droplet: NOT experimentally established for ACSL1 protein.** BioID in mouse
  hepatocytes found lipid-droplet proteins among ACSL1 proximity partners
  [PMID:30190326 "We found subsets of peroxisomal and lipid droplet proteins, tethering
  proteins, and vesicle proteins"], which is proximity, not residency. Haney et al. 2024
  call ACSL1 "the lipid droplet-associated enzyme" and a regulator of LD biogenesis, but
  their data are expression (snRNA-seq, IF of ACSL1 in IBA1+ microglia), a CRISPR screen and
  triacsin C inhibition — none shows ACSL1 protein on the LD surface
  [PMID:38480892 "ACSL1 is a key enzyme in LD biogenesis and overexpression of ACSL1 is
  sufficient to induce triglyceride-specific LD formation in several cell types"]. The
  canonical LD-resident ACSL is ACSL3. No GO lipid droplet (GO:0005811) annotation exists for
  ACSL1 in human, mouse or rat in GOA.

## Physiological roles (mostly mouse knockouts)

- Partitioning FAs toward beta-oxidation:
  - Adipose KO: [PMID:20620995 "ACSL1 has a specific function in directing the metabolic
    partitioning of FAs toward beta-oxidation in adipocytes"]; cold intolerance.
  - Heart KO: [PMID:21245374 "ACSL1 is required to synthesize the acyl-CoAs that are
    oxidized by the heart"].
  - Liver KO: 50% loss of hepatic ACSL activity, lower TAG incorporation in hepatocytes and
    lower beta-oxidation [PMID:19648649 "hepatic ACSL1 is important for mitochondrial
    beta-oxidation of long chain fatty acids"].
- Glycerolipid (TAG) synthesis / lipid droplet accumulation: in hepatocytes ACSL1 loss
  reduces oleate incorporation into TAG [PMID:19648649]; in human iPSC microglia, fibrillar
  amyloid-beta induces ACSL1 and TAG synthesis, and triacsin C reverses LD accumulation
  [PMID:38480892 "An ACSL1 inhibitor (Triacin C) reversed the accumulation of LD in APOE4/4
  iMG on fAβ challenge"]. ACSL1 here supplies acyl-CoA substrate for TAG synthesis
  (participation in triglyceride biosynthesis); LD formation itself is downstream.
- Fatty acid uptake: ACSL1 enhances uptake indirectly by metabolic trapping
  [PMID:24503477 "the intracellular acyl-CoA synthetases FATP4 and ACSL1 enhance fatty acid
  uptake indirectly by metabolic trapping"].
- Inflammation: myeloid ACSL1 promotes inflammatory macrophage phenotype in diabetic mice
  [PMID:22308341]. ACSL1-high microglia (LDAM) in APOE4/4 Alzheimer disease brain
  [PMID:38480892].

## Curation decisions summary

- Core: GO:0004467 long-chain fatty acid-CoA ligase activity at MOM (GO:0005741) and ER
  membrane (GO:0005789); process GO:0035338 / GO:0001676; supply of acyl-CoA to TAG synthesis
  (GO:0019432).
- Uptake/transport terms kept as non-core (indirect, metabolic trapping).
- IEP-derived "response to" IEA terms removed.
- No NEW lipid droplet / lipid droplet organization annotations: localization not shown;
  LD formation is a downstream consequence of TAG synthesis (fails participation test as a
  direct LD-organization actor; comparator genes like GPAT/DGAT carry TAG synthesis).
