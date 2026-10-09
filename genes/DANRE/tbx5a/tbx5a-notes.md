# tbx5a (Q9IAK8) notes

## Setup and provenance

- Gene fetched earlier with `just fetch-gene` on Q9IAK8 (Swiss-Prot). That accession holds all 91 GOA rows.
  The genes were not re-fetched.
- **Deep research failed.** Edison returned 402 Payment Required and the OpenAI key is invalid. It was not
  retried. There is no `-deep-research-*.md` file. The literature research below was done by hand from the
  cached publications and from Europe PMC searches ("tbx5b AND zebrafish", "tbx5a AND tbx5b",
  "tbx5 AND teleost AND duplicat*").
- Extra PMIDs fetched for the pair: 34756968, 30532148, 33482174, 29382818, 27503876, 39079985 (and
  25623069, which turned out to be about mouse isoforms and was not used).

## Identity

- T-box transcription factor TBX5-A, 492 aa. T-box DNA-binding domain at residues 62-237 (UniProt). Synonyms:
  heartstrings (hst), tbx5, tbx5.1. ZFIN ZDB-GENE-991124-7.
- Teleost-genome-duplication (TGD) paralog of tbx5b. The two proteins share 49.2% identity over the full
  length (compare_pair.py) and 83% within the T-box
  [PMID:39079985 "The T-box domain of Tbx5b shares only 83% sequence identity with its Tbx5a counterpart"].

## Alleles (important for interpreting phenotypes)

- **hst (heartstrings):** ENU nonsense allele, premature termination codon (PTC).
  [PMID:12223419 "The heartstrings mutation causes premature termination at amino acid 316."]
  The transcript is lost after 32 hpf, as expected from nonsense-mediated decay
  [PMID:27503876 "The hst mutation is a premature stop codon in tbx5a exon8, and tbx5a is weakly expressed in the LPM of hst embryos until 32 hpf, but undetectable thereafter"].
  Pi-Roig et al. argue it is hypomorphic for laterality
  [PMID:24759614 "Overall, these data demonstrate not only the specificity of the cardiac phenotypes caused by MO-mediated knock-down of tbx5a and/or tbx5b, but also that the hst mutation behaves as a hypomorphic allele with regard to cardiac laterality."]
- **oug (oudegracht, hu6499):** truncated inside the T-box.
  [PMID:34372968 "Indeed, in oug approximately 75% of the gene product is lost, including a large portion of the DNA-binding T-box domain."]
  Jogging is normal in this allele:
  [PMID:34372968 "In such a screen we identified the oudegracht (oug) mutant in which cardiac jogging was unaffected while cardiac looping was compromised."]
- **tpl58 gene trap:** truncates the protein after 50 aa. The authors raise allele-dependent compensation:
  [PMID:29933372 "A particularly intriguing possibility would be that point mutant tbx5ahst but not gene trap mutant tbx5atpl58 may induce genetic compensation [40,41]."]
- **CRISPR F0 knockouts:** [PMID:33416493 "100% (43/43) of the tbx5a F0 larvae did not develop pectoral fins (Figure 4A)."]
- No RNA-less (promoter-deletion) allele has been reported.

## Function

- **Pectoral fin initiation (copy-specific).**
  [PMID:12223419 "Homozygous mutant embryos never develop pectoral fin buds and do not express several markers of early fin differentiation."]
  [PMID:12066188 "Functional knockdown of zebrafish tbx5 through the use of an antisense oligonucleotide resulted in a failure to initiate fin bud formation, leading to the complete loss of pectoral fins."]
  [PMID:12810598 "We show that the zebrafish fgf24 gene, which belongs to the Fgf8/17/18 subfamily of Fgf ligands, acts downstream of tbx5 to activate fgf10 expression in the lateral plate mesoderm."]
  Fin-field migration:
  [PMID:34756968 "In both tbx5a −/− mutants and Tbx5a knock-down embryos, AP convergence of the fin field cells fails to occur; however these same precursors exhibit a robust ML movement that is similar in migration dynamics to that of wt embryos."]
- **Heart.**
  [PMID:12223419 "However, the heart fails to loop and then progressively deteriorates, a process affecting the ventricle as well as the atrium."]
  AV canal: [PMID:34372968 "In the zebrafish oug mutant, the absence of Tbx5a results in the expansion of the AV canal as illustrated by expanded domains of expression of tbx2b, bmp4, and has2"]
  tbx2b: [PMID:19895804 "The presence of a Tbx5-binding-element in the promoter of tbx2b along with the reduction of expression in hst heterozygous mutants and complete loss in homozygotes reveals that Tbx5 regulates tbx2b at the AV boundary."]
  Proepicardium: [PMID:20413782 "We further show that tbx5a mutants also have severe defects in PE specification."]
  Regeneration: [PMID:29933372 "while all tbx5atpl58R/tpl58R fish failed to regenerate their hearts (n = 8)"]
- **Regulators.** Pdlim7 sequesters Tbx5 on actin
  [PMID:19895804 "Regulated by yet unknown signals, Tbx5 exits the nucleus and binds to Pdlim7 along cytoplasmic actin filaments."].
  Kctd10 represses it [PMID:24430697 "We show that Kctd10 directly binds to Tbx5 to repress its transcriptional activity."].
- **Molecular function.** EMSA on the tbx2b enhancer
  [PMID:18347092 "In electromobility shift assays (EMSA) to test DNA-binding affinity, Foxn4 and Tbx5 bound efficiently to their labeled putative binding sites, and binding was efficiently competed with excess unlabeled cognate competitors, but not with mutated oligonucleotides"].
  The extracted text does not state the species of the Tbx5 construct used.
- **Retina (shared with tbx5b, morpholino-only).**
  [PMID:24759614 "suggesting that tbx5 paralogues act redundantly in the dorsal retina to ensure efnb2a expression in this territory."]
- **Not required for the swim bladder.**
  [PMID:30352852 "However, we find that although Tbx5 is required for lung formation, tbx5a / b is not required for SB formation in the zebrafish."]

## Annotation decisions (summary)

- ACCEPT: MF (T-box DNA binding and transcription factor activity), nucleus, heart development, heart
  looping, heart morphogenesis, chamber morphogenesis, proepicardium, pectoral fin development and fin bud
  (limb bud) formation, the regulation-of-transcription terms, and NOT swim bladder development.
- UNDECIDED:
  - heart jogging (IMP/IGI). Morpholino-only, and contradicted by the hst and oug mutants, which jog
    normally. The cause (off-target effect or compensation) is unresolved.
  - GO:0061629 IPI with Kctd10. Kctd10 is not a DNA-binding TF, so the term probably belongs on kctd10.
    Only the abstract is cached.
- MODIFY: GO:0006351 DNA-templated transcription changed to GO:0006357.
- REMOVE: protein binding (uninformative).
- MARK_AS_OVER_ANNOTATED: cardiac left ventricle formation (IBA; teleosts have a single ventricle; given a
  propagation_review), epithelium development (ARBA), protein-containing complex.
- KEEP_AS_NON_CORE: cytoplasm and actin cytoskeleton (Pdlim7 sequestration), AV valve formation and AV
  junction remodeling, optic nerve and retina (double morphants), cardiac muscle cell differentiation (cBAF),
  pericardium morphogenesis, cardiac muscle tissue regeneration, cell fate specification, pattern specification.
- No NEW terms. The fin-initiation and heart terms already present are enough.
