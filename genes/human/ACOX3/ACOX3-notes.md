# ACOX3 (Peroxisomal acyl-coenzyme A oxidase 3) — review notes

UniProt: O15254 (ACOX3_HUMAN). Gene: ACOX3; synonyms BRCOX, PRCOX. HGNC:121. Chromosome 4p15.3.
700 aa; EC 1.3.3.6. Belongs to the acyl-CoA oxidase family.

## Identity / naming

- RecName "Peroxisomal acyl-coenzyme A oxidase 3"; AltName "Branched-chain acyl-CoA oxidase"
  (Short "BRCACox"); AltName "Pristanoyl-CoA oxidase" [file:human/ACOX3/ACOX3-uniprot.txt
  "AltName: Full=Pristanoyl-CoA oxidase"].
- Historical note: an earlier human "branched-chain acyl-CoA oxidase" (BRCACox) was characterized
  as the human homologue of *rat trihydroxycoprostanoyl-CoA oxidase* — this is actually the gene now
  called ACOX2, not ACOX3. ACOX3 was first identified as a distinct *pristanoyl-CoA oxidase* gene
  [PMID:9271077 "these compounds are oxidized by a single enzyme, branched-chain acyl-CoA oxidase,
  which according to its amino acid sequence is the human homologue of rat
  trihydroxycoprostanoyl-CoA oxidase"; and "the gene for human pristanoyl-CoA oxidase was mapped at
  chromosome position 4p15.3"]. The GOA "BRCOX/branched-chain acyl-CoA oxidase" naming in UniProt
  reflects this tangled history; the modern, well-supported molecular activity is a
  2-methyl-branched-chain / pristanoyl-CoA oxidase.

## Molecular function

- FAD-dependent acyl-CoA oxidase; catalyzes the first, rate-limiting dehydrogenation of peroxisomal
  beta-oxidation: a 2,3-saturated acyl-CoA + O2 -> a (2E)-enoyl-CoA + H2O2 (EC 1.3.3.6)
  [file:human/ACOX3/ACOX3-uniprot.txt "Reaction=a 2,3-saturated acyl-CoA + O2 = a (2E)-enoyl-CoA +
  H2O2"]. FAD cofactor [file:human/ACOX3/ACOX3-uniprot.txt "Name=FAD; Xref=ChEBI:CHEBI:57692"].
- Preferred physiological substrates are multi-methyl-branched (2-methyl-branched) fatty acyl-CoAs,
  notably (2S)-pristanoyl-CoA [file:human/ACOX3/ACOX3-uniprot.txt "Metabolizes multi-methyl-branched
  fatty acyl-CoA esters such as (2S)-pristanoyl-CoA"; and "Oxidizes the CoA-esters of 2-methyl-branched
  fatty acids"]. Pristanoyl-CoA reaction: (2S)-pristanoyl-CoA + O2 = (2E)-pristenoyl-CoA + H2O2
  [file:human/ACOX3/ACOX3-uniprot.txt "Reaction=(2S)-pristanoyl-CoA + O2 = (2E)-pristenoyl-CoA + H2O2"].
- Can also oxidize straight-chain (mono- and dicarboxylyl) acyl-CoAs with lower efficiency; the
  straight-chain reactions in UniProt (decanoyl-, hexadecanoyl-, tetracosanoyl-, hexadecanedioyl-CoA)
  are largely By-similarity/inferred rather than the physiological role [file:human/ACOX3/ACOX3-uniprot.txt
  "Can oxidize straight-chain mono- and dicarboxylyl fatty acyl-CoAs with lower efficiency (By
  similarity)"].
- Substrate-specificity study of ACOX1/2/3 concluded ACOX1 handles straight-chain fatty acids, ACOX2
  handles bile-acid intermediates, and both ACOX2 and ACOX3 handle branched-chain fatty acids
  [PMID:29287774 "ACOX1 is responsible for the oxidation of straight-chain fatty acids with different
  chain lengths, ACOX2 is the only human acyl-CoA oxidase involved in bile acid biosynthesis, and both
  ACOX2 and ACOX3 are involved in the degradation of the branched-chain fatty acids"].

## Biological process

- Peroxisomal fatty-acid beta-oxidation, specifically the acyl-CoA-oxidase-dependent branch (H2O2
  generated instead of feeding electrons to a respiratory chain) [file:human/ACOX3/ACOX3-uniprot.txt
  "PATHWAY: Lipid metabolism; peroxisomal fatty acid beta-oxidation"]. Pristanoyl-CoA (from
  alpha-oxidation of dietary phytanic acid) is degraded by three cycles of peroxisomal beta-oxidation
  [reactome:R-HSA-389887 "Pristanoyl-CoA, generated in the peroxisome by alpha-oxidation of dietary
  phytanic acid, is further catabolized by three cycles of peroxisomal beta-oxidation"].

## Cellular component

- Peroxisomal matrix protein; C-terminal PTS1 (SKL) targeting signal
  [file:human/ACOX3/ACOX3-uniprot.txt "SUBCELLULAR LOCATION: Peroxisome"; "MOTIF 698..700
  /note=\"Microbody targeting signal\""; PMID:9271077 "harbouring a peroxisomal C-terminal-targeting
  signal (SKL)"]. Reactome models it as a matrix enzyme imported by the PEX5 pathway (hence transient
  cytosol/matrix-translocation TAS annotations).

## Expression / tissue specificity

- Long believed nearly silent in human tissues (mRNA undetectable by routine Northern blot; protein
  undetectable by immunoblot) [PMID:9271077 "expressed to such a low extent in liver that its mRNA
  cannot be detected by routine Northern-blot analysis and that its product remains undetected by
  standard immunoblotting or by enzyme activity measurements"]. Ferdinandusse et al. 2018 later
  demonstrated ACOX3 expression in normal human tissues at both mRNA and protein level
  [PMID:29287774 "We report for the first time expression of ACOX3 in normal human tissues at the mRNA
  and protein level"]. UniProt records protein-level expression in liver, kidney, lung, brain and heart
  [file:human/ACOX3/ACOX3-uniprot.txt "Expressed in liver, kidney, lung, brain (cortex and cerebellum)
  and heart (at protein level)"]. Reactome (older) notes ACOX3 protein/activity detectable in prostate
  tumors but historically undetectable in normal prostate, liver, kidney [reactome:R-HSA-389891
  "ACOX3 protein and enzyme activity have been observed in prostate tumors, but are undetectable in
  normal prostate tissue as well as in liver and kidney"].

## Annotation review reasoning

Core MF: pristanoyl-CoA oxidase activity (GO:0016402) and the parent acyl-CoA oxidase activity
(GO:0003997); FAD binding (GO:0071949 / GO:0050660). Core BP: fatty acid beta-oxidation using acyl-CoA
oxidase (GO:0033540) / fatty acid beta-oxidation (GO:0006635). Core CC: peroxisome (GO:0005777) /
peroxisomal matrix (GO:0005782).

Over-annotations / caveats:
- "fatty acid binding" (GO:0005504, IBA + InterPro IEA): the enzyme binds fatty **acyl-CoA** thioesters,
  not free fatty acids; this is a generic family-propagated MF that does not describe ACOX3's actual
  ligand — MARK_AS_OVER_ANNOTATED.
- The Rhea-derived very-long-chain / long-chain / medium-chain acyl-CoA oxidase MF terms (GO:0044535,
  GO:0120524, GO:0120523) come from By-similarity straight-chain reactions and are lower-efficiency /
  non-physiological for this branched-chain-specialist enzyme — KEEP_AS_NON_CORE.
- GO:0016627 (oxidoreductase, CH-CH group of donors) is a correct but very general parent — KEEP_AS_NON_CORE.
- GO:0016020 "membrane" (HDA, PMID:19946888, NK-cell membrane proteome): ACOX3 is a soluble peroxisomal
  matrix protein; membrane co-purification is likely non-specific. Do not REMOVE (experimental HDA) —
  MARK_AS_OVER_ANNOTATED.
- GO:0005829 "cytosol" (Reactome TAS): reflects the transient cytosolic stage of PEX5-mediated matrix
  import, not a steady-state cytosolic localization — KEEP_AS_NON_CORE.
