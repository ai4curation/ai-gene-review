# ALDH5A1 (SSADH) review notes

UniProtKB: P51649 (SSDH_HUMAN). HGNC:408. EC 1.2.1.24. 535 aa precursor with an
N-terminal mitochondrial transit peptide (1..47); mature chain 48..535.

## Core biology
ALDH5A1 encodes **succinate-semialdehyde dehydrogenase, mitochondrial (SSADH)**, the
NAD+-dependent enzyme catalysing the **final step of GABA degradation** (the GABA shunt):
oxidation of **succinate semialdehyde -> succinate**, which then enters the TCA cycle,
routing GABA carbon into central energy metabolism.

- Catalytic activity (UniProt/Rhea RHEA:13217): succinate semialdehyde + NAD(+) + H2O =
  succinate + NADH + 2 H(+); EC 1.2.1.24 [file:human/ALDH5A1/ALDH5A1-uniprot.txt].
- "Mitochondrial NAD(+)-dependent succinic semialdehyde dehydrogenase (ALDH5A1, SSADH)
  represents the last enzyme in the GABA catabolism and irreversibly oxidizes SSA to
  succinate" [PMID:12208142].
- "Succinic semialdehyde dehydrogenase (SSADH) is involved in the final degradation step
  of the inhibitory neurotransmitter gamma-aminobutyric acid by converting succinic
  semialdehyde to succinic acid in the mitochondrial matrix" [PMID:19300440].
- Homotetramer of identical subunits [PMID:16199352; UniProt SUBUNIT].
- Km(SSA) 6.3 uM, Km(NAD+) 125 uM; recombinant enzyme characterised [PMID:16199352].
- Redox-regulated via a reversible Cys340-Cys342 disulfide on a dynamic catalytic loop;
  inhibited under oxidizing conditions / by H2O2 [PMID:19300440].
- Member of the aldehyde dehydrogenase superfamily [PMID:7814412].

## Localization
Mitochondrion / mitochondrial matrix. TransitPeptide 1..47. UniProt subcellular location:
Mitochondrion. Reactome places the reaction in the mitochondrial matrix (R-HSA-888548).
Confirmed by IDA (HPA), HDA/HTP proteomics (PMID:20833797 muscle mito phosphoproteome;
PMID:34800366 MitoCoP high-confidence mito proteome), and IBA.

## Disease
SSADH deficiency (SSADHD; MIM:271980) = 4-hydroxybutyric (gamma-hydroxybutyric, GHB)
aciduria. Autosomal recessive; accumulation of GABA and GHB; developmental delay,
hypotonia, intellectual disability, ataxia, seizures, behavioural disturbance
[PMID:9683595, PMID:12208142, PMID:14635103, PMID:15037717].

## Annotation review decisions (summary)
- MF GO:0004777 succinate-semialdehyde dehydrogenase (NAD+) activity: CORE. Multiple EXP
  (12208142, 14635103, 19300440), IDA (16199352, 9683595), ISS, IEA, IBA all converge.
  All ACCEPT.
- MF GO:0009013 succinate-semialdehyde dehydrogenase [NAD(P)+] activity (IEA/InterPro):
  human enzyme is NAD+-specific (name, EC 1.2.1.24, kinetics). NAD(P)+ term is broader/
  the bacterial (EC 1.2.1.16) flavour. MARK_AS_OVER_ANNOTATED (not wrong at family level
  but less precise than the NAD+-specific term).
- MF GO:0016491 oxidoreductase activity (IEA): correct but generic parent of GO:0004777.
  MARK_AS_OVER_ANNOTATED.
- MF GO:0042802 identical protein binding (IPI, 16199352): supported (homotetramer) but
  bare binding term; per policy do not REMOVE experimental IPI -> KEEP_AS_NON_CORE.
- BP GO:0009450 GABA catabolic process: CORE. IBA + IDA (9683595). ACCEPT.
- BP GO:0006540 GABA shunt (IMP, 15037717): correct process; ACCEPT (arguably the more
  informative pathway term). 15037717 is a case report of SSADHD showing GABA/GHB
  accumulation, supporting the pathway role.
- BP GO:0006105 succinate metabolic process (ISS): product is succinate; correct but
  broad/generic vs the GABA catabolic framing. KEEP_AS_NON_CORE.
- BP GO:0006536 glutamate metabolic process (ISS): weaker — glutamate is upstream of GABA
  (glutamate -> GABA via GAD), not a direct substrate/product of SSADH. The ISS is a
  transfer from mouse ortholog. MARK_AS_OVER_ANNOTATED (indirect at best).
- BP GO:0007417 central nervous system development (IMP, 9683595): 9683595 identifies
  splicing mutations causing SSADHD; the neurological disease phenotype is a downstream
  consequence of loss of GABA catabolism, not evidence that SSADH drives CNS development.
  This is a pleiotropic/disease-derived process. KEEP_AS_NON_CORE (do not REMOVE an
  experimental IMP whose full text we cannot read).
- CC GO:0005739 mitochondrion (IBA, IEA, IDA/HPA, HDA, HTP) and GO:0005759 mitochondrial
  matrix (TAS Reactome): all ACCEPT; matrix is the more precise, correct location.
