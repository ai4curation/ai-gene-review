# FAH (Fumarylacetoacetase, P16930) — review notes

## Core function (well established)

FAH catalyzes the fifth and final step of the cytosolic L-tyrosine (and L-phenylalanine)
catabolic pathway: hydrolysis of 4-fumarylacetoacetate to fumarate + acetoacetate.

- EC 3.7.1.2, fumarylacetoacetase activity (GO:0004334).
- Reaction (UniProt/Rhea RHEA:10244): "4-fumarylacetoacetate + H2O = acetoacetate + fumarate + H(+)".
- GO:0004334 definition (QuickGO, verified): "Catalysis of the reaction: 4-fumarylacetoacetate + H2O = acetoacetate + fumarate + H+."
- Homodimer; each monomer binds one Ca2+ and one Mg2+ as catalytic cofactors [UniProt COFACTOR/SUBUNIT; Reactome R-HSA-71181 "The enzyme is a homodimer, with each monomer binding one Ca(2+) and one Mg(2+) ion as catalytic cofactors"].
- Cytosolic; mainly expressed in liver and kidney [UniProt TISSUE SPECIFICITY: "Mainly expressed in liver and kidney. Lower levels are also detected in many other tissues."].

### Direct experimental support for catalysis (human enzyme)
[PMID:1998338 "Transient expression of this FAH cDNA in transfected CV-1 mammalian cells resulted in the synthesis of an immunoreactive protein comigrating with purified human liver FAH on SDS-PAGE and having enzymatic activity as shown by the hydrolysis of the natural substrate fumarylacetoacetate."] — TAS annotation to GO:0004334 (PINC). This is the human FAH cloning/expression paper; abstract-only cache but establishes human FAH catalyzes the FAA hydrolysis reaction and that the in vivo dimer is a homodimer.

## Pathway placement / BP

- UniProt PATHWAY: "Amino-acid degradation; L-phenylalanine degradation; acetoacetate and fumarate from L-phenylalanine: step 6/6." (UniPathway UPA00139/UER00341). L-Phe is first converted to L-Tyr (PAH), so FAH is the terminal step of both Tyr and Phe catabolism.
- Reactome R-HSA-71181 "FAH cleaves 4FAA": "This is the final step of tyrosine degradation."
- Tyrosine catabolic pathway (last enzyme): [PMID:9305902 "HT1 is due to mutations in the fumarylacetoacetate hydrolase gene Fah, encoding the last enzyme in the tyrosine catabolic pathway."] — supports GO:0006572 (TAS).

### Homogentisate catabolic process (GO:1902000, IBA)
Homogentisate (2,5-dihydroxyphenylacetate) is the intermediate produced by HPD from
4-hydroxyphenylpyruvate and consumed by HGD in the tyrosine pathway, upstream of FAH.
FAH acts on 4-fumarylacetoacetate, three steps downstream of homogentisate, so it is part
of the same overall pathway but does not itself catabolize homogentisate. The IBA is a
pathway-level (whole-pathway) grouping propagated across the FAH family; keep as non-core
(over-broad relative to FAH's actual biochemical step).

## Disease (Tyrosinemia type I / HT-1)

FAH deficiency causes hepatorenal tyrosinemia type I (TYRSN1, MIM:276700), the most severe
tyrosinemia [UniProt DISEASE]. Loss of the terminal step causes accumulation of upstream
toxic intermediates fumarylacetoacetate (FAA) and maleylacetoacetate (MAA), and the derived
metabolite succinylacetone (SA). FAA triggers hepatocyte apoptosis via mitochondrial
cytochrome c release; SA inhibits ALA dehydratase (porphyria-like crises). Leads to hepatic
necrosis/cirrhosis, hepatocellular carcinoma risk, and renal tubular dysfunction. Treated
with nitisinone (NTBC, an HPD inhibitor blocking the pathway upstream) plus Tyr/Phe-restricted
diet.
- dismech Tyrosinemia_Type_I.yaml: "FAH deficiency leads to accumulation of toxic intermediates including fumarylacetoacetate (FAA), maleylacetoacetate (MAA), and succinylacetone (SA). FAA directly injures hepatocytes through mitochondrial cytochrome c release with caspase-mediated apoptosis."
- Apoptosis mechanism [PMID:9305902 "accumulation of fumarylacetoacetate, maleylacetoacetate, or succinylacetone seems to trigger the endogenous process of apoptosis in hepatocytes that lack fumarylacetoacetate hydrolase activity."]
- Many disease-causing loss-of-activity missense variants documented (e.g. N16I, A134D, C193R, D233V, W234G, R381G) [UniProt VARIANT features].

## Annotation-by-annotation reasoning

- GO:0004334 fumarylacetoacetase activity — CORE MF. Three annotations (IBA, IEA GO_REF:0000120, TAS PMID:1998338). All ACCEPT.
- GO:0006572 L-tyrosine catabolic process — CORE BP (terminal step). IBA + TAS(PMID:9305902) ACCEPT; the GO_REF:0000107 Ensembl-Compara IEA is a redundant ortholog-transfer of the same correct term — ACCEPT (not over-broad).
- GO:0006559 L-phenylalanine catabolic process — Phe feeds into the Tyr pathway (PAH converts Phe→Tyr); FAH is the terminal step of Phe degradation per UniPathway. Correct but the phenylalanine framing is one step removed from FAH's direct substrate. Keep (ACCEPT/non-core) — both IBA and UniPathway IEA supported by UniProt PATHWAY statement.
- GO:1902000 homogentisate catabolic process — IBA, pathway-level grouping; FAH does not act on homogentisate directly. KEEP_AS_NON_CORE.
- GO:0003824 catalytic activity — IEA InterPro, uninformative parent of GO:0004334. MARK_AS_OVER_ANNOTATED (root-ish MF; more specific term exists and is annotated).
- GO:0009072 aromatic amino acid metabolic process — IEA InterPro, broad grouping BP; correct but non-core (Tyr/Phe catabolism captured more specifically). KEEP_AS_NON_CORE.
- GO:0005515 protein binding (x2 refs; IPI) — high-throughput binary interactome screens (PMID:25416956 Rolland/HuRI; PMID:32296183 Luck/HuRI reference map). Bare "protein binding", uninformative; interactors (TCF4, KRTAPs, ADAMTSL4, CHRDL2, SERTAD1, PLEKHF2) have no functional relationship to a cytosolic metabolic hydrolase — classic HT-Y2H artifacts. REMOVE per curation guideline against bare protein binding.
- GO:0070062 extracellular exosome (x2; HDA) — high-throughput proteomics of urinary/prostatic exosomes (PMID:23533145, PMID:19056867). FAH is a cytosolic liver/kidney enzyme; detection in urinary exosomes is a mass-spec catalog finding, not a functional localization. KEEP_AS_NON_CORE (do not remove HDA; keep as non-core secondary location).
- GO:0005829 cytosol (TAS Reactome) — CORE CC. ACCEPT.
