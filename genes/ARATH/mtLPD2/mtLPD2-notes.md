# mtLPD2 (At3g17240, UniProt Q9M5K2) - curation notes

**Deep research could not be run** in this environment (no provider API keys).
These notes are a manual literature summary built only from the cached
publications in `publications/`, the UniProt record (`mtLPD2-uniprot.txt`) and
PubMed searches. No `-deep-research-*.md` file exists for this gene.

## Identity and naming caution

- UniProt Q9M5K2 (DLDH2_ARATH), "Dihydrolipoyl dehydrogenase 2, mitochondrial"
  (AtmLPD2, mtLPD2), EC 1.8.1.4; gene LPD2, locus At3g17240.
- The folder is named `mtLPD2` because UniProt also uses the gene name LPD2 for
  the **chloroplastic** E3 At4g16155 (F4JLP5, PLPD2_ARATH, ptLPD2). Everything here
  is about the mitochondrial At3g17240 protein.
- The mitochondrial paralog is mtLPD1, At1g48030 (UniProt Q9M5K3, DLDH1_ARATH).
- Mitochondrial transit peptide 1..36 (experimentally determined, ECO:0000269
  PubMed:25732537); class-I pyridine nucleotide-disulfide oxidoreductase family;
  FAD and NAD binding sites (by similarity); redox-active disulfide.

## Biochemical function

- Dihydrolipoyl dehydrogenase (E3, L protein): reoxidizes protein-bound
  dihydrolipoamide using NAD+ via an FAD cofactor (RHEA:15045; UniProt evidence
  ECO:0000269 PubMed:11598235).
  [PMID:22303256 "This reaction is catalyzed by L-protein, a homodimeric dihydrolipoamide dehydrogenase (EC 1.8.1.4). Electrons are first transferred to the co-factor FAD that is re-oxidized by NAD + resulting in the formation of NADH"].
- Mitochondrial LPD is shared among the 2-oxoacid dehydrogenase complexes (PDC,
  2-oxoglutarate dehydrogenase, branched-chain 2-oxoacid dehydrogenase) and the
  glycine decarboxylase complex (GDC)
  [PMID:26116608 "Mitochondrial dihydrolipoyl dehydrogenase (mtLPD; L-protein) is an integral component of several multienzyme systems involved in the tricarboxylic acid (TCA) cycle, photorespiration, and the degradation of branched-chain α-ketoacids"].
- Branched-chain 2-oxoacid dehydrogenase activity exists in Arabidopsis
  mitochondria (Taylor et al. 2004), which also uses an E3, but that study does not
  assign the E3 to a specific gene.

## mtLPD1 vs mtLPD2 division of labour

- Arabidopsis has two mitochondrial LPD genes; the Arabidopsis Book review lists
  both as L-protein genes
  [PMID:22303256 "two genes each for P-protein (At4g33010 and At2g26080) and L-protein (At3g17240 and At1g48030)"].
- Lutziger & Oliver 2001 (abstract only in cache): mtLPD1 mRNA is high in green
  leaves and strongly light-induced; mtLPD2 shows the inverse pattern (higher in
  roots) and only moderate light induction. The authors hypothesize that mtLPD1
  is the GDC-associated isoform and mtLPD2 is incorporated into 2-oxoacid
  dehydrogenase complexes, but that the two proteins are interchangeable; the
  mtlpd2 T-DNA knockout has no visible phenotype
  [PMID:11598235 "we hypothesize that mtLPD1 encodes the protein most often associated with the Gly decarboxylase complex, and mtLPD2 encodes the protein incorporated into alpha-ketoacid dehydrogenase complexes"]
  [PMID:11598235 "we assume that the proteins, once in the mitochondrial matrix, are interchangeable among the different multienzyme complexes"]
  [PMID:11598235 "a T-DNA knockout mutant, mtlpd2, which shows no apparent phenotypic change under laboratory growth conditions"].
- Later photorespiration work by the Bauwe/Timm group focused on mtLPD1 as the
  GDC L protein of leaves [PMID:38861078 "in illuminated, photosynthesizing tissue a vast amount of mtLPD1 is necessary for glycine decarboxylase (GDC), the key enzyme of photorespiration"] and
  [PMID:38518065 "a shared regulation mechanism mainly on mitochondrial dihydrolipoamide dehydrogenase (mtLPD1)-dependent pathways"].
  Timm et al. 2015 overexpressed the GDC L protein and saw faster photorespiration
  and growth [PMID:26116608 "The majority of the mtLPD present in photosynthesizing tissue is used for glycine decarboxylase (GDC), necessary for the high-flux photorespiratory glycine-into-serine conversion"];
  the abstract does not name the isoform, but the same group's later methods paper
  names mtLPD1 as the isoform used by GDC in photosynthesizing tissue (PMID:38861078).
- Conclusion: the experimental evidence ties mtLPD2 to E3 activity and the
  mitochondrion. Its participation in GDC is plausible (interchangeability) but
  not directly demonstrated, and the dominant photorespiratory L protein in leaves
  is most likely mtLPD1 (At1g48030). No NEW photorespiration or GDC annotation is
  proposed for mtLPD2.

## Localization

- Mitochondrial matrix (UniProt, ECO:0000269 PubMed:14671022, PubMed:14764908).
  Repeatedly found in mitochondrial proteomes (PMID:11743114, PMID:11743115,
  PMID:14671022, PMID:17137349, PMID:18385124, PMID:22923678, PMID:25293756).
- Complex I association (IDA, PMID:20197505) is explicitly called a contaminant by
  the authors [PMID:20197505 "a few contaminating proteins like prohibitin, the β-subunit of ATP synthase (complex V), Ser hydroxymethyltransferase, and lipoamide dehydrogenase"].
- NOT Golgi (RCA, PMID:22430844): the Golgi proteome classified it as a
  non-Golgi contaminant; consistent with matrix localization.
- Cytosol (HDA, PMID:28887381) is likely fractionation carry-over.

## Ligand-affinity proteomics

- Cu/Zn/Co binding (HDA, PMID:20018591) from immobilized metal affinity
  chromatography of mitochondrial proteins; ATP binding (HDA, PMID:17137349) from
  immobilized-ATP capture. Neither metal nor ATP is a known physiological ligand of
  LPD (FAD and NAD+ are). These are affinity-capture observations, not functions.

## Expression / regulation

- Preferential expression in roots, flowers and siliques (UniProt, PMID:11598235).
- Induced by cadmium (UniProt, PMID:16502469, not cached).

## Module cross-check

- `modules/glycine_cleavage_system.yaml` L-protein role: GO:0004148,
  PANTHER PTHR22912:SF151; representative members are bacterial, yeast and human;
  no Arabidopsis member is named. Consistent with the MF assigned here.
- `modules/photorespiration_c2_cycle.yaml` (step 5 description) names
  "mitochondrial LPD2 (UniProtKB:Q9M5K2)" as the Arabidopsis L protein. The
  literature reviewed here suggests that mtLPD1 (At1g48030, Q9M5K3) is the main
  GDC/photorespiratory L protein in leaves, while mtLPD2 is proposed to work mainly
  with 2-oxoacid dehydrogenase complexes. mtLPD2 may still contribute to GDC
  because the proteins are thought to be interchangeable. **Disagreement to report:**
  the C2 module should probably cite mtLPD1 (Q9M5K3) as the primary leaf L
  protein, with mtLPD2 as a possible redundant contributor.
