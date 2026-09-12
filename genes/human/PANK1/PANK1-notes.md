# PANK1 (human) — gene review notes

UniProt: Q8TE04 (PANK1_HUMAN). Gene symbol PANK1 (HGNC:8598). Taxon: Homo sapiens (NCBITaxon:9606).

## Identity and core function

PANK1 is **pantothenate kinase 1** (EC 2.7.1.33), a type II pantothenate kinase.
It catalyses the **first and rate-determining (rate-limiting) step of coenzyme A (CoA)
biosynthesis**: ATP-dependent phosphorylation of pantothenate (vitamin B5) to
4'-phosphopantothenate.

- Reaction (UniProt CATALYTIC ACTIVITY): "(R)-pantothenate + ATP = (R)-4'-phosphopantothenate + ADP + H(+)" — RHEA:16373, EC 2.7.1.33 [file:human/PANK1/PANK1-uniprot.txt CC CATALYTIC ACTIVITY].
- FUNCTION (Isoform 1): "Catalyzes the phosphorylation of pantothenate to generate 4'-phosphopantothenate in the first and rate-determining step of coenzyme A (CoA) synthesis." [file:human/PANK1/PANK1-uniprot.txt, ECO:0000269|PubMed:14523052, ECO:0000269|PubMed:17631502].
- PATHWAY: "Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 1/5." (UniPathway UPA00241, UER00352) [file:human/PANK1/PANK1-uniprot.txt].
- SIMILARITY: "Belongs to the type II pantothenate kinase family." [file:human/PANK1/PANK1-uniprot.txt].

Mammals have three PanK genes (PANK1, PANK2, PANK3) expressing four catalytically
active isoforms (PanK1α, PanK1β, PanK2, PanK3); PANK1 alone yields two isoforms
(PanK1α = isoform 1; PanK1β = isoform 2) from alternate initiation exons sharing a
common C-terminal catalytic core [PMID:23152917 "three genes express four catalytically active isoforms in mammals: PanK1α, PanK1β, PanK2 and PanK3"; "The α and β isoforms of PanK1 are encoded by different transcripts that arise from alternate initiation exons within the Pank1 gene"].

## Allosteric regulation (feedback inhibition)

- ACTIVITY REGULATION: "Regulated by feedback inhibition by CoA and its thioesters." [file:human/PANK1/PANK1-uniprot.txt, ECO:0000269|PubMed:17631502].
- Crystal structures of the PanK1α and PanK3 catalytic cores in complex with acetyl-CoA (a feedback inhibitor) explain the allosteric regulation [PMID:17631502 "we report the homodimeric structures of the catalytic cores of PanK1alpha and PanK3 in complex with acetyl-CoA, a feedback inhibitor... the inhibitor-bound structures explain the basis for the allosteric regulation by CoA thioesters"]. This is the basis of the IDA **acetyl-CoA binding** (GO:1905502) annotation and the FT acetyl-CoA BINDING sites at residues 417/420/432.
- Enzyme is a **homodimer** [file:human/PANK1/PANK1-uniprot.txt SUBUNIT: "Homodimer." ECO:0000269|PubMed:17631502; PMID:17631502 "homodimeric structures of the catalytic cores"]. Basis of GO:0042803 protein homodimerization activity (IDA). Each monomer adopts an actin-kinase / actin-like ATPase fold [PMID:17631502 "Each monomer adopts a fold of the actin kinase superfamily"].

## Subcellular localization (isoform-specific)

Localization is isoform-specific and was systematically mapped by Alfonso-Pecchio et al.
2012 (PMID:23152917), full text available (PMC3496714):

- **PanK1α (isoform 1, Q8TE04-1): nuclear / nucleolar.** "Both human and mouse PanK1α proteins were nuclear" and PanK1α "isoforms were exclusively nuclear, with preferential association with the granular component of the nucleolus during interphase" [PMID:23152917]. NLS mapped to residues 218–233 (matches UniProt MOTIF 218..235 nucleolar localization signal; MUTAGEN 218..233 → loss of nuclear localization). Also associates with the perichromosomal region on condensing chromosomes during mitosis.
- **PanK1β (isoform 2, Q8TE04-2): cytosolic, partially on clathrin-coated vesicles and recycling endosomes.** "Both human and mouse PanK1β localized to the cytosol"; "A portion of PanK1β associated with clathrin-coated structures... the localization of another portion of PanK1β with recycling endosomes was indicated by co-localization with the marker Rab11 GTPase" [PMID:23152917]. Recycling-endosome identity confirmed by Rab11 co-localization.
- UniProt SUBCELLULAR LOCATION mirrors this: general "Cytoplasm" [ECO:0000269|PubMed:14523052]; Isoform 1 → Nucleus, nucleolus [PubMed:23152917]; Isoform 2 → Cytoplasm/cytosol, clathrin-coated vesicle, recycling endosome [PubMed:23152917] [file:human/PANK1/PANK1-uniprot.txt].

Note (important): the isoform whose N-terminal extension carries the NLS is **PanK1α =
UniProt isoform 1 (Q8TE04-1)**. In the paper's nomenclature "PANK1a" is used loosely; the
UniProt `AltName` mapping shows isoform 1 = PanK1-alpha/PANK1a and isoform 2 =
PanK1-beta/PANK1a — the synonyms are muddled in the record, but the biology is
unambiguous: the LONGER α protein (isoform 1, 598 aa) is nuclear/nucleolar and the shorter
β protein (isoform 2) is cytosolic/vesicular. Nucleus + recycling-endosome EXP annotations
(PMID:23152917) are therefore isoform-specific but reflect genuine biology of the protein.

The IDA "cytoplasm" (GO:0005737) annotation from PMID:14523052 reflects the earlier study,
where increased hPanK1α protein was "localized in the cytoplasm" [PMID:14523052 "higher hPanK1 protein, localized in the cytoplasm"]. Alfonso-Pecchio 2012 explicitly notes this earlier cytoplasmic interpretation conflated abundant cytosolic PanK1β with the minor nuclear PanK1α [PMID:23152917 "the majority of the PanK1 was cytosolic PanK1β rather than the minor nuclear PanK1α component"]. Both cytoplasm/cytosol and nucleus/nucleolus are retained as real (isoform-dependent) locations.

## Tissue expression / regulation

- Isoform 1 expressed at high levels in brain, heart, kidney, liver, skeletal muscle, testis [file:human/PANK1/PANK1-uniprot.txt TISSUE SPECIFICITY, PubMed:11809413, PubMed:14523052].
- Induced by bezafibrate, a PPARα agonist; PANK1α mRNA specifically up-regulated, raising CoA biosynthetic flux and steady-state CoA in HepG2 cells [PMID:14523052 "Bezafibrate (BF)... specifically increased hPANK1alpha mRNA expression"; "The enhanced hPANK1alpha gene expression translated into increased activity of the CoA biosynthetic pathway and established a higher steady-state CoA level"]. Establishes PPARα-PANK1α axis as a control point for hepatic CoA. This is a transcriptional/regulatory context, not a molecular function of the PANK1 protein itself.

## Disease context

- Reviewed in Cavestro et al. 2023 (PMID:36983025). The CoA-biosynthesis inborn errors involve the first (PANK2 → PKAN) and last (COASY → CoPAN) enzymes; PANK1 itself is not the primary NBIA gene, but PANK1 is the paralogous first-step enzyme. The EXP pantothenate kinase activity annotation attributed to PMID:36983025 (assigned by Reactome) reflects PanK enzymology described in that review.

## GO review summary (see PANK1-ai-review.yaml)

Core functions:
1. GO:0004594 pantothenate kinase activity (MF), directly_involved_in GO:0015937 coenzyme A biosynthetic process; requires GO:0005524 ATP binding; feedback-inhibited (GO:1905502 acetyl-CoA binding).

Actions:
- ACCEPT: pantothenate kinase activity (IBA, EXP×2, IDA), CoA biosynthetic process (IBA, TAS), cytosol (IBA), acetyl-CoA binding (IDA), protein homodimerization activity (IDA), ATP binding (IEA), nucleus (EXP), recycling endosome (EXP), cytoplasm (IDA).
- KEEP_AS_NON_CORE: nucleus (IBA/IEA), nucleolus (IEA), cytoplasm (IEA), cytosol (IEA/TAS), clathrin-coated vesicle (IEA), recycling endosome (IEA) — real isoform-specific / general locations but not the enzyme's core catalytic function.
- No REMOVEs: all IEAs here are consistent with experimental/UniProt evidence; the pantothenate kinase activity IEA/IBA and ATP binding IEA are correct.

MF core is unambiguous: pantothenate kinase, first/rate-limiting step of CoA biosynthesis.
