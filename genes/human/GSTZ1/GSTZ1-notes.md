# GSTZ1 (O43708, MAAI_HUMAN) review notes

## Identity
- Human glutathione S-transferase zeta 1 (GSTZ1-1) = maleylacetoacetate isomerase (MAAI).
- Bifunctional cytosolic enzyme of the GST superfamily, Zeta family (216 aa, homodimer).
- EC 5.2.1.2 (MAAI isomerase) and EC 2.5.1.18 (GST). Requires glutathione as cofactor for MAAI activity.
- HGNC:4643; chromosome 14q24.3. PDB 1FW1, 8E8P.

## Core physiological role: MAAI, step 5 of Phe/Tyr catabolism
- Catalyzes cis-trans isomerization of 4-maleylacetoacetate -> 4-fumarylacetoacetate,
  the penultimate step of tyrosine/phenylalanine degradation (glutathione-dependent).
- [PMID:9417084 "characterize at the cDNA level the human gene for maleylacetoacetate isomerase (MAAI, EC 5.2.1.2), the only as yet unidentified structural gene of the phenylalanine catabolic pathway"] — human homologue of A. nidulans maiA; MAAI activity when expressed in E. coli.
- [PMID:10373324 "The gene for maleylacetoacetate isomerase (MAAI) (EC 5.2.1.2) was the last gene in the mammalian phenylalanine/tyrosine catabolic pathway to be cloned"] — gene expressed ubiquitously though pathway restricted to liver/kidney; "suggests a possible second role."
- UniProt PATHWAY: "L-phenylalanine degradation; acetoacetate and fumarate from L-phenylalanine: step 5/6." UniProt KW: Tyrosine catabolism, Phenylalanine catabolism.
- UniProt DR includes GO:0006572 L-tyrosine catabolic process (IEA UniProtKB-KW) and Reactome R-HSA-8963684 Tyrosine catabolism.

## GST / xenobiotic role
- [PMID:9396740 "Recombinant human GSTZ1-1 ... minimal glutathione-conjugating activity with ethacrynic acid and 7-chloro-4-nitrobenz-2-oxa-1,3-diazole. Although low in comparison with other GSTs, GSTZ1-1 has glutathione peroxidase activity with t-butyl and cumene hydroperoxides."] — defines Zeta class GST; low GST + low GPx activity.
- [PMID:10739172] — functional polymorphism (GSTZ1*A K32/R42 vs variants); GSTZ1a-1a has 3.6-fold higher DCA activity. UniProt FUNCTION cites this for both catalytic activities and DCA oxygenation.
- Crystal structure with GSH [PMID:11327815] "molecular basis for its remarkable catalytic promiscuity"; homodimer.

## Dichloroacetate (DCA) biotransformation — clinically important
- GSTZ1 dehalogenates/biotransforms DCA to glyoxylate; DCA inactivates GSTZ1 (mechanism-based) -> reduced clearance on repeat dosing.
- [PMID:20884751 "Repeated doses of DCA result in reduced drug clearance, probably through inhibition of glutathione transferase zeta1 (GSTZ1), a cytosolic enzyme that converts DCA to glyoxylate"; "the mitochondrion is a novel site of DCA biotransformation catalyzed by GSTZ1, an enzyme colocalized in cytosol and mitochondrial matrix"].
- Original DCA oxygenation report: PMID:9531472 (not cached) "Glutathione transferase zeta catalyses the oxygenation of the carcinogen dichloroacetic acid to glyoxylic acid."

## Localization
- Primary = cytosol (UniProt SUBCELLULAR LOCATION: Cytoplasm). GO:0005829 cytosol IDA (FlyBase, PMID:20884751), plus Reactome TAS.
- Also mitochondrial matrix: IDA (PMID:20884751 submitochondrial fractionation, rat), HTP (PMID:34800366 mito proteome), TAS Reactome, ISS, IBA. Real but secondary/non-canonical -> KEEP_AS_NON_CORE.

## Deficiency (MAAID)
- [UniProt DISEASE] Maleylacetoacetate isomerase deficiency (MAAID) [MIM:617596], autosomal recessive; mild elevations of succinylacetone in blood/urine, usually caught by newborn screening; normal liver function; "MAAID is a benign disorder." {PubMed:27876694}. Variants Met-99, Val-150 have decreased MAAI activity.
- Consistent with biochemically mild phenotype (succinylacetone, maleylacetone excretion) rather than severe tyrosinemia.

## Protein-binding annotations
- GO:0005515 protein binding (IPI, PMID:17474147 SH3 peptide array; PMID:32296183 HuRI binary interactome) and GO:0042802 identical protein binding (PMID:16189514, 25416956, 32296183 HuRI). Interactors NCK1, QARS1, TRAF2, GORASP2, PLEKHG4, TCP11, ZMYND12, CLVS2 are high-throughput binary-interactome hits with no established functional consequence -> uninformative `protein binding`; MARK_AS_OVER_ANNOTATED.
- GO:0042802 identical protein binding + GO:0042803 protein homodimerization: the enzyme IS a homodimer (crystal structure PMID:11327815; PMID:10739172 IPI self). Homodimerization is a genuine, structurally-supported property -> KEEP_AS_NON_CORE (homodimer is the functional unit but not the "core function" MF).

## Action plan for GOA lines
- GO:0016034 MAAI activity (IBA, IEA, IDA PMID:10739172, TAS PMID:10373324): core MF -> ACCEPT (IDA is the anchor).
- GO:0004364 glutathione transferase activity (IBA, IEA, IDA PMID:10739172, TAS PMID:9396740): real but low/secondary -> KEEP_AS_NON_CORE (biochemically genuine; the GST activity toward classic substrates is weak).
- GO:0004602 glutathione peroxidase activity (TAS PMID:9396740): low activity -> KEEP_AS_NON_CORE.
- GO:0003824 catalytic activity (IEA InterPro): too general -> MARK_AS_OVER_ANNOTATED (or MODIFY to MAAI). Root-ish MF; mark over-annotated.
- GO:0006559 L-phenylalanine catabolic process (IBA, IEA UniPathway, TAS PMID:9417084): correct pathway -> ACCEPT (this is the Phe/Tyr common pathway).
- GO:0006749 glutathione metabolic process (IBA, IDA PMID:10739172): GSH is cofactor/substrate -> KEEP_AS_NON_CORE.
- GO:0009072 aromatic amino acid metabolic process (IEA InterPro): broader parent of Phe/Tyr catabolism -> ACCEPT (correct, if general).
- GO:0098869 cellular oxidant detoxification (IEA GOC from GO:0004602): tied to weak GPx activity -> KEEP_AS_NON_CORE.
- GO:1990748 cellular detoxification (IDA PMID:20884751): DCA detox -> KEEP_AS_NON_CORE.
- CC cytosol (IDA, TAS): core location -> ACCEPT.
- CC cytoplasm (IEA): correct but general -> ACCEPT.
- CC mitochondrion / mitochondrial matrix (IBA, IDA, HTP, TAS, ISS): real secondary loc -> KEEP_AS_NON_CORE.
- protein binding / identical protein binding (IPI HuRI/SH3): uninformative -> MARK_AS_OVER_ANNOTATED.
- protein homodimerization activity (IPI PMID:10739172): genuine homodimer -> KEEP_AS_NON_CORE.
