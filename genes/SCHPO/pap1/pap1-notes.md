# pap1 (Q01663, SPAC1783.07c, caf3) — S. pombe AP-1-like bZIP transcription factor

## Summary
Pap1 (Caffeine resistance protein 3; AP-1-like / Yap1/c-Jun family bZIP) is the principal redox-regulated
transcriptional activator of the oxidative-stress and multidrug-resistance responses in fission yeast.
Under low H2O2 it senses peroxide via the peroxiredoxin Tpx1, which forms a transient disulfide relay that
oxidizes the C-terminal cysteine-rich domain (c-CRD), forming an intramolecular interdomain disulfide
(Cys278–Cys501) that masks the Crm1-dependent nuclear export signal. Nuclear Pap1 binds AP-1/TRE-like
sites (consensus TTACGTAA) and induces antioxidant genes (ctt1 catalase, trr1, trx2, srx1) and
drug-efflux/MDR genes (bfr1/hba2, pmd1, caf5, obr1). At high H2O2 the Sty1/Atf1 pathway dominates.

## Identity / family
- AP-1-like bZIP transcription factor; bZIP family, YAP subfamily [UniProt Q01663].
- "The other gene pap1+ encodes an AP-1-like transcription factor that contains a region rich in basic amino acids followed by a 'leucine zipper' motif." [PMID:1899230]
- bZIP DNA-binding domain crystal structure (PDB 1GD2); binds novel consensus TTACGTAA. [PMID:11017199 "PAP1, a fission yeast AP-1-like transcription factor that binds DNA containing the novel consensus sequence TTACGTAA"]
- Homodimer (PubMed:11017199, UniProt SUBUNIT).

## DNA binding / TF activity
- Binds AP-1 site and a 14-bp palindrome by DNase I footprinting; activates target gene p25. [PMID:1448080 "the pap1 protein binds to the AP-1 site as well as to a 14-bp palindrome sequence"]
- Required for transcription activation: "p25 is overproduced when the pap1+ gene is overexpressed, whereas p25 is not produced at all in the pap1 deletion mutant." [PMID:1448080]
- DNA bending: Pap1 bends DNA ~26° toward protein. [PMID:9070843 "the DNA in the complex was bent about 26 degrees toward the protein-binding surface"]
- Crystallographic characterization of Pap1-DNA complex (DNA-binding domain). [PMID:9757124]
- Genome-wide TF atlas: ChIP-seq DNA binding sites and nucleosome binding (EXP). [PMID:40015273]

## Oxidative stress / redox regulation
- Sty1 regulates Pap1; both required for oxidative-stress and MDR gene expression. [PMID:9585505 "the cellular response to oxidative stress and to treatment with a variety of cytotoxic agents is the result of Sty1 regulation of the Pap1 transcription factor, a bZip protein with structural and DNA binding similarities to the mammalian c-Jun protein"]
- Genes induced incl. hba2/bfr1 and pmd1 (MDR transporters). [PMID:9585505]
- H2O2-induced disulfide bond precedes nuclear accumulation. [PMID:15165244 "the in vivo formation of a hydrogen peroxide-induced disulphide bond in Pap1, which precedes the rapid and reversible nuclear accumulation of the transcription factor"]
- Tpx1 (2-Cys Prx) required for peroxide-induced Pap1 activation. [PMID:15824112 "the 2-Cys peroxiredoxin (2-Cys Prx) Tpx1 is required for the peroxide-induced activation of Pap1"]
- H2O2 reversibly oxidizes Cys278 and Cys501; DEM non-reversibly modifies Cys523/Cys532. [PMID:12100563 "H2O2 reversibly oxidizes two cysteine residues in Pap1 (Cys278 and Cys501)"]
- Pap1 + Prr1 heterodimer needed for antioxidant (but not drug-tolerance) genes. [PMID:22344694 "those coding for the antioxidants catalase, sulfiredoxin or thioredoxin reductase, do need oxidized Pap1 to form a heterodimer with the constitutively nuclear transcription factor Prr1"]
- Methylglyoxal activates Pap1 via c-CRD; nuclear accumulation, target gene activation. [PMID:16141205 "The transcription factor Pap1 also accumulates in the nucleus, activating the expression of its target genes following methylglyoxal treatment"]
- Tpx1 hyperoxidation/Txl1 role in switching off early Pap1 response. [PMID:22245228]

## Subcellular location & export control
- Negatively regulated by Crm1/exportin 1. [PMID:1448080 "pap1+ is apparently negatively regulated by crm1+"]
- Oxidant-sensitive NES in c-CRD; Cys532 + two Leu + Ile important. [PMID:10329722 "the hydrophobic amino acid-rich region containing two important cysteines in Pap1 serves as a novel NES, which is sensitive to oxidative stress"]
- Cytoplasm in unstressed cells; relocalizes to nucleus on oxidative stress (Sty1-dependent at high dose). [PMID:9585505]
- Hba1 (Ran-binding) loss → constitutive nuclear Pap1, MDR. [PMID:12896976 "either multiple copies or deletion of the hba1 gene induces nuclear accumulation of Pap1"]
- Genome-wide localization (cytosol/cytoplasm). [PMID:16823372]

## Drug / caffeine / multidrug resistance
- pap1 first isolated as staurosporine-resistance gene; required for spk1-conferred resistance. [PMID:1899230 "The pap1+ gene is required for spk1(+)-conferred staurosporine resistance"]
- Int6 overexpression drug resistance is Pap1-dependent. [PMID:11071922]
- Pap1 a key TF for fission yeast MDR. [PMID:22840777]
- Genes required for caffeine tolerance; Pap1 and efflux pumps. [PMID:19672306]
- pof14 transcription induced by H2O2 requires Pap1. [PMID:17016471]
- ctt1 catalase induction by oxidative stress via Pap1 (element A). [PMID:10731689 "The factor responsible for the induction of the gene by oxidative stress via element A was identified as the transcription factor Pap1"]

## Disulfide stress / Oxs1
- Pap1–Oxs1 pathway for diamide/Cd disulfide stress; Oxs1 + Pap1 form complex, co-required for promoter binding. [PMID:27664222 "Oxs1 and Pap1 form a complex when cells are exposed to diamide or Cd that causes disulfide stress... effective Pap1 binding to these targets requires Oxs1, and vice versa"]

## Atf1 cross-talk
- A subset of stress genes co-controlled by Atf1 and Pap1. [PMID:28652406 "impaired transcription of a subset of stress genes whose expression is also controlled by another transcription factor, Pap1"]

## Review decisions (overview)
- Core MF: DNA-binding transcription activator activity RNA pol II-specific (GO:0001228) — ACCEPT (IDA/IMP/EXP, many refs).
- Core BP: positive regulation of transcription by RNA pol II (GO:0045944) and cellular response to oxidative stress (GO:0034599) — ACCEPT.
- Sequence-specific RNA pol II cis-reg DNA binding (GO:0000978), cis-reg region binding (GO:0000976) — ACCEPT.
- CC nucleus/cytoplasm/cytosol/chromatin — ACCEPT (well supported; reflect shuttling).
- DNA binding, bending (GO:0008301) — ACCEPT (IDA, FRET).
- nucleosome binding (GO:0031491) — KEEP_AS_NON_CORE (EXP atlas; peripheral to TF core function).
- RNA pol II transcription regulator complex (GO:0090575) — ACCEPT/KEEP (Prr1 heterodimer, Oxs1 complex).
- protein binding (GO:0005515) — bare term; MARK as uninformative; note real partners (Prr1, Oxs1, Crm1, Tpx1).
- Generic IEA terms (GO:0003700, GO:0006355, GO:0000981, GO:0005634/0005737 IEA) — ACCEPT but non-core/redundant where a more specific experimental term exists.
