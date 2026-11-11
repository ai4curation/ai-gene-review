# CDK5RAP1 (Q96SZ6) curation notes

Reviewed together with its paralog CDKAL1 (Q5VV42) as the two human radical SAM
methylthiotransferases (MTTases), within the RADICAL_SAM project.

## Sources consulted

- The Asta deep-research file (`CDK5RAP1-deep-research-asta.md`) is a raw retrieval and none of the
  20 papers concerns CDK5RAP1. It was not used for any claim. Falcon failed (auth 403) and was not
  re-run.
- Full text in cache: PMID:22422838 (Reiter 2012), PMID:28981754 (Fakruddin 2017), PMID:34800366
  (MitoCoP). Abstract only: PMID:25738458 (Wei 2015 Cell Metab), PMID:10721722, PMID:10915792,
  PMID:11882646, PMID:17491008.

## Enzyme activity: MiaB-type i6A37 methylthiotransferase

- [PMID:22422838 "we detected significantly elevated levels of ms2i6A in the complemented cells
  (Figure 4a), showing that CDK5RAP1 has indeed MiaB-like catalytic properties."] (MTS-less variant
  expressed in a miaB-deficient E. coli strain.)
- Substrate specificity: [PMID:22422838 "Again, the content of ms2t6A is not affected by knockdown of
  CDK5RAP1, proving that t6A is not recognized as a substrate of CDK5RAP1"]. CDKAL1 is the t6A
  enzyme, so the two paralogs have non-overlapping substrates.
- Knockdown: [PMID:22422838 "Transfection with esiRNA resulted indeed in a 78% decrease of ms2i6A
  content after 72 h in comparison to cells treated with esiRNA against green fluorescent protein
  (Figure 4b)."]
- In vivo targets: [PMID:25738458 "In this study, we report that Cdk5 regulatory subunit-associated
  protein 1 (Cdk5rap1) is responsible for 2-methylthio (ms(2)) modifications of mammalian mt-tRNAs
  for Ser(UCN), Phe, Tyr, and Trp codons."]
- UniProt: EC 2.8.4.3, RHEA:37067; two [4Fe-4S] clusters; MiaB subfamily.

## Location: mitochondrion (matrix)

- Mitochondrial targeting sequence (TRANSIT 1-33) on the main isoform; [PMID:22422838 "The confocal
  analysis clearly shows a mitochondrial localization of variant 1."]
- The variant without the MTS (v2) was found in cytoplasm and nucleus when overexpressed, and
  antibody ICC suggested a nuclear preference: [PMID:22422838 "This distribution was confirmed by
  immunocytochemical (ICC) staining of CDK5RAP1, however with a stronger preference for nuclear
  localization (Figure 1c)."]
- Reiter et al. proposed ms2i6A in nuclear RNA (polyA RNA, miRNA). This was refuted by
  [PMID:28981754 "Taken together, we propose that ms2i6A is a mitochondrial tRNA-specific
  modification and is absent from nuclear-encoded RNA species."] (rho0 cells have no ms2i6A; the
  ms2i6A antibody signal co-localizes with mitochondria). Also [PMID:28981754 "However, the
  cytosolic CDK5RAP1_v2 not only lacks mitochondria-targeting signal, but also lacks an important
  cysteine residue in the UPF0004 domain (10)."], so the extra-mitochondrial variant is probably
  inactive.
- UniProt CAUTION records this conflict.
- Mitochondrial proteome (MitoCoP, PMID:34800366) and HPA immunofluorescence corroborate
  mitochondrion.

## Physiology

- [PMID:25738458 "Deficiency in ms(2) modification markedly impaired mitochondrial protein synthesis,
  which resulted in respiratory defects in Cdk5rap1 knockout (KO) mice."] Myopathy and cardiac
  dysfunction under stress; ms2 levels lower in patients with mitochondrial disease.

## CDK5 / neuronal history

- Named C42 in a yeast two-hybrid screen for p35 (CDK5R1) binders (PMID:10721722). GST pull-down
  co-precipitated p35 complexed with Cdk5.
- PMID:11882646: C42 "specifically inhibits the activation of Cdk5 by Nck5a"; co-IP with p35 in
  cultured cells; the inhibitory region is conserved with yeast Pho81. Abstract-only. The
  experiment is in vitro or uses overexpression. The mature enzyme is in the mitochondrial matrix
  and p35 is cytosolic or membrane-associated, so physiological relevance is doubtful. These rows
  are not removed (experimental; full text not read) and are kept as non-core.
- CDKAL1, the paralog, neither binds p35 nor inhibits CDK5 [PMID:21841312, see CDKAL1 notes].
- NAS rows for brain development (PMID:10915792) and regulation of neuron differentiation
  (PMID:10721722) extrapolate CDK5 biology to a binding partner; neither abstract tests CDK5RAP1 in
  any neuronal process. They are removed.
- TAS negative regulation of cell cycle (PMID:17491008): the abstract is about p35 binding
  microtubules and does not mention CDK5RAP1/C42. The full text is not in the cache, so this is
  UNDECIDED.

## Decisions summary

- Generic radical SAM rows: GO:0003824 and GO:0051536 MODIFY; GO:0051539 ACCEPT (RADICAL_SAM
  treatment table). GO:0016740 and GO:0035596 MODIFY to GO:0035597; GO:0006400 and GO:0009451 MODIFY
  to GO:0035600 + GO:0070900.
- Cytosol (IBA, IDA) and nucleoplasm (IDA): MARK_AS_OVER_ANNOTATED. The observations come from an
  MTS-less variant whose activity outside mitochondria was refuted. The cytosol IBA comes from the
  bacterial MiaB node and does not fit the mitochondrially targeted vertebrate clade.
- GO:0051246 regulation of protein metabolic process (ARBA): MARK_AS_OVER_ANNOTATED. CDK5RAP1
  contributes to mitochondrial translation through tRNA modification and does not regulate
  protein metabolism as such.
- Not added: mitochondrial translation (GO:0032543). CDK5RAP1 modifies the tRNA rather than
  performing translation (participation test), and the mitochondrial tRNA modification term already
  covers it. SAM binding (GO:1904047) added as a NEW ISS row from MiaB in vitro reconstitution (PMID:15339930) plus the UniProt PRU00780 exchangeable-SAM note, for consistency with LIAS and ELP3.
