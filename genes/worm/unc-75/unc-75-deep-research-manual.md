# unc-75 (C. elegans) - manual literature synthesis

No deep-research API was available, so this summary was compiled by hand from the
cached publications and the UniProt record G5EE68 (unreviewed TrEMBL; WormBase
WBGene00006807, C17D12.2; GeneID 182722).

## Identity and family

- UNC-75 is a 514-aa CELF (CUG-BP and ETR-3-like factor) family RNA-binding protein with
  three RRM domains (PROSITE PS50102 at 29-110, 124-204 and 429-507), a divergent linker
  domain between RRM2 and RRM3, and a C-terminal PY-type nuclear localization signal.
  UniProt places it in the CELF3/4/5/6 RRM1 InterPro subfamily (IPR034648) and PANTHER
  PTHR24012.
  [PMID:23468662 "UNC-75 belongs to the CUG-BP and ETR-3-like factor (CELF) family of RNA-binding proteins, which have two N-terminal RNA recognition motifs (RRMs) followed by a so-called divergent domain and the third RRM at the C-terminus."]

## Expression and localization

- Pan-neuronal and neurosecretory gland expression; nuclear speckles.
  [PMID:12906792 "unc-75 encodes an RRM domain-containing RNA binding protein that is exclusively expressed in the nervous system and neurosecretory gland cells"]
  [PMID:12906792 "localizes to dynamic nuclear speckles"]
- The C-terminal PY-NLS is required for nuclear localization.
  [PMID:23468662 "The substitution of the three residues in the PY element of UNC-75 (Figure 4A) disrupted the nuclear localization of UNC-75 (Figure 4B, 4C), confirming that the C-terminal motif of UNC-75 functions as the PY-NLS."]
- No study reports a cytoplasmic pool or a cytoplasmic function of UNC-75 (in contrast to
  vertebrate CELF1/CELF2, which also act on mRNA stability and translation).

## Molecular function: sequence-specific pre-mRNA (intronic) binding

- Kuroyanagi et al. 2013 (PMID:23468662; full text read): EMSA with recombinant FLAG-UNC-75
  maps direct, specific binding to a short element in unc-32 intron 7a containing a
  UUGUUGUGUUGU stretch; RRM3 alone binds, and RRM1/RRM2 missense mutations from the genetic
  screen reduce binding.
  [PMID:23468662 "demonstrate that UNC-75 specifically binds via its three RNA recognition motifs to the element including a UUGUUGUGUUGU stretch"]
  [PMID:23468662 "indicating that only RRM3 can bind to Probe 2-1-1 by itself"]
- Norris et al. 2014 (PMID:24910101; full text read): RNAcompete consensus U[G/A]UUGUG; GST-UNC-75
  EMSAs bind consensus-containing RNA oligos and lose binding when the motif is mutated;
  the UNC-75 motif in the unc-16 intron downstream of exon 16 is required for exon inclusion.
  [PMID:24910101 "The UNC-75 and EXC-7 consensus sequences identified were U[G/A]UUGUG and UAAGUU, respectively"]

## Biological process: neuronal alternative splicing regulation

- unc-32 (V-ATPase a subunit) exon 7a selection and exon 4b selection in neurons require UNC-75.
  [PMID:23468662 "Thus, UNC-75 is the critical splicing factor for the nervous system to specifically select unc-32 exon 4b in vivo."]
  UNC-75 both activates and represses particular splice sites:
  [PMID:23468662 "UNC-75 represses splicing of exon 3 to exon 4c and exon 4a to exon 5 and promotes splicing of exon 4b to exons 3 and 5."]
- Autoregulation: UNC-75 represses its own exon 8.
  [PMID:23468662 "consistent with the idea that UNC-75 negatively regulates its own expression by repressing exon 8"]
- Genome-wide: UNC-75 and EXC-7 (Hu/ELAV) regulate overlapping exon networks in GABAergic
  and cholinergic motor neurons; UNC-75 generally stimulates inclusion by binding downstream
  intronic sequences.
  [PMID:24910101 "UNC-75 generally stimulates exon inclusion by binding to downstream intronic sequences"]
  Targets include unc-64/syntaxin mutually exclusive final exons.
  [PMID:24910101 "These results indicate that unc-64 isoforms A and B have non-overlapping functions, and that the relative proportions of these isoforms are fine-tuned by UNC-75."]

## Organismal phenotypes (downstream)

- unc-75 mutants are uncoordinated and aldicarb resistant (reduced cholinergic transmission),
  with GABAergic defects; not required for neuronal development.
  [PMID:12906792 "unc-75 mutant animals display neuroanatomical and behavioral defects indicative of a role in modulating GABAergic and cholinergic neurotransmission but not neuronal development"]
  [PMID:24910101 "unc-75 mutants exhibit severe neuronal phenotypes, including uncoordination and altered aldicarb sensitivity."]
- Original aldicarb-resistance screen: PMID:7498734 (abstract only in cache).

## Open questions

- Whether UNC-75 has any cytoplasmic (mRNA stability / translation) role like CELF1/2.
- How UNC-75 recognizes the unc-32 exon 4 cluster, where no high-affinity site was found
  (cooperative factors postulated by the authors).
