# FPS1 (At5g47770; UniProt Q09152) - manual literature research

Deep-research API providers were not available for this session; this file was
compiled manually from cached publications (`publications/`) and PubMed searches
(query "Arabidopsis farnesyl diphosphate synthase FPS1", 6 hits).

## Identity and gene structure
- FPS1 encodes farnesyl diphosphate synthase (EC 2.5.1.10 / 2.5.1.1), a member of the
  FPP/GGPP synthase (trans-isoprenyl diphosphate synthase, head-to-tail) family
  [UniProt Q09152 "Belongs to the FPP/GGPP synthase family."].
- Alternative translation initiation yields two isoforms: FPS1L (mitochondrial, with a
  41-residue N-terminal transit peptide) and FPS1S (cytosolic)
  [PMID:9182568 "Translation of the FPS1L mRNA from the upstream AUG codon generates a novel FPS1 isoform (FPS1L) with an NH2-terminal extension of 41 amino acid residues, which has all the characteristics of a mitochondrial transit peptide."].
- Transit peptide function was tested by import into yeast mitochondria in vivo and into
  purified plant mitochondria in vitro [PMID:9182568, abstract].
- The paralog FPS2 (At4g17190) shares ~90.6% identity and is cytosolic [PMID:8631820].

## Biochemical activity
- Purified recombinant FPS1S (and FPS2) were kinetically characterised; Km values for IPP,
  DMAPP and GPP in the micromolar range, with preference for GPP over DMAPP as allylic
  substrate [PMID:23145086 "Both enzymes displayed typical Michaelis-Menten behaviour, as observed for other FPSs, and exhibited similar K m values in the µmolar range (from 8.3 to 31.5 µM) for both IPP and the allylic substrates DMAPP and GPP."].
- FPS2 is the more efficient catalyst; FPS1S is less thermostable and less NaCl sensitive
  [PMID:23145086 abstract].
- FPS1 cDNA was originally isolated by functional complementation of a yeast FPS-deficient
  (erg20) strain [PMID:8631820 abstract; PMID:7858223 per UniProt].
- Mg2+-dependent; DDxxD motifs and binding residues inferred by similarity to avian FPS
  P14324 [UniProt FT BINDING, ECO:0000250].

## Localization
- FPS1S N- and C-terminal GFP fusions are exclusively cytosolic in N. benthamiana
  [PMID:23145086 "Under our experimental conditions all the four fusion proteins localized exclusively in the cytosol (Figure 5)."].
- FPS1L mitochondrial (import experiments, PMID:9182568).
- Proteomic size-exclusion profiling detected FPS1 in the crude cytosolic fraction of leaves
  (PMID:25293756, HDA cytosol) and in a membrane-associated proteome that TAIR mapped to
  plastid (PMID:28887381, HDA plastid). There is no plastid targeting signal and no
  targeted experiment supporting plastid localization.

## Physiological role (genetics)
- fps1 and fps2 single knockouts have no major phenotype; the double knockout is
  embryo-lethal (arrest pre-globular) and impairs male transmission
  [PMID:20497375 "Here we show that simultaneous knockout of both FPS genes is lethal for Arabidopsis, and embryo development is arrested at the pre-globular stage, demonstrating that FPP-derived isoprenoid metabolism is essential."].
- FPS1 activity predominates for most of the life cycle; FPS2 predominates in seeds
  [PMID:20497375 abstract]. FPS1S expressed from the FPS2 promoter rescues fps2 seed
  phenotypes [PMID:23145086 "Altogether, these results demonstrated that FPS1S is able to functionally replace FPS2."].
- FPS1 promoter-GUS is widely expressed in all tissues [PMID:11202437].
- Simultaneous amiRNA knockdown of FPS1/FPS2 causes chlorosis, altered chloroplasts and
  sterol-dependent induction of JA- and Fe-deficiency responses; these are indirect
  consequences of sterol depletion [PMID:27382138 abstract].
- FPP supplies sterols, brassinosteroids, ubiquinone side chains, polyprenols,
  sesquiterpenes and farnesylated proteins (review in PMID:23145086 introduction).
