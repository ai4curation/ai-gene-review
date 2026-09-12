# ST8SIA1 (GD3 synthase) review notes

## Identity
- UniProt: Q92185 (SIA8A_HUMAN); gene ST8SIA1; synonyms SIAT8, SIAT8A; HGNC:10869; GeneID 6489; chr 12p12.
- Names: Alpha-N-acetylneuraminide alpha-2,8-sialyltransferase; Ganglioside GD3 synthase; Ganglioside GT3 synthase; Sialyltransferase 8A (SIAT8-A); ST8Sia I; SAT-II. EC 2.4.3.8 (old EC 2.4.99.8).
- Glycosyltransferase 29 (GT29 / CAZy) family; PANTHER PTHR11987:SF3; Pfam PF00777 Glyco_transf_29.
- 356 aa; type II single-pass membrane protein; cytoplasmic 1-29, TM 30-48 (signal-anchor), lumenal 49-356 [file:human/ST8SIA1/ST8SIA1-uniprot.txt "TRANSMEM 30..48 ... Signal-anchor for type II membrane protein"].

## Core molecular function
GD3 synthase transfers a second sialic acid in alpha-2,8 linkage from CMP-N-acetylneuraminate onto the terminal sialic acid of GM3, producing GD3 (+ CMP + H+). It initiates the b-series ganglioside branch. UniProt FUNCTION:
[file:human/ST8SIA1/ST8SIA1-uniprot.txt "Catalyzes the addition of sialic acid in alpha 2,8-linkage to"] ... "the sialic acid moiety of the ganglioside GM3 to form ganglioside GD3".
- Rhea RHEA:41760 (GM3 + CMP-Neu5Ac = GD3 + CMP + H+); generic reaction RHEA:19313; EC 2.4.3.8.
- Can add a further alpha-2,8 sialic acid to GD3 -> GT3 (c-series precursor) [file:human/ST8SIA1/ST8SIA1-uniprot.txt "Can catalyze the addition of a second alpha-2,8-sialic"].
- Broader acceptor specificity in vitro: GM1b->GD1c, GD1a->GT1a, GT1b->GQ1b [file:human/ST8SIA1/ST8SIA1-uniprot.txt "Can use GM1b, GD1a and GT1b"].
- In cancer-cell context can act as oligosialyltransferase making GQ3, GP3 [PMID:22885356 "This indicates that ST8Sia I is able to act as an oligosialyltransferase in a cellular context."].
- The correct current GO MF is GO:0003828 "alpha-N-acetylneuraminate alpha-2,8-sialyltransferase activity" (verified in go.db; child of GO:0008373 sialyltransferase activity).

## Biological process
- Ganglioside biosynthesis; specifically the key regulatory branch-point enzyme for b/c-series gangliosides.
  [PMID:8058740 "GD3 synthase ... which is a key regulatory enzyme determining the prominence of the ganglioside biosynthesis pathway."]
  [PMID:22885356 "ST8Sia I (EC 2.4.99.8, SAT-II, SIAT 8a) is the key enzyme controlling the biosynthesis of b- and c-series gangliosides."]
- Best current BP term: GO:0001574 "ganglioside biosynthetic process" (verified go.db; child of GO:0006688 glycosphingolipid biosynthetic process, itself child of GO:0006665 sphingolipid metabolic process).
- Acts on glycolipids (gangliosides), NOT on N-glycans or glycoproteins -> IBA GO:0006491 (N-glycan processing) and InterPro IEA GO:0009101 (glycoprotein biosynthetic process) are mis-branch/over-annotations.

## Location
- Golgi apparatus membrane; single-pass type II membrane protein [file:human/ST8SIA1/ST8SIA1-uniprot.txt "SUBCELLULAR LOCATION: Golgi apparatus membrane"]. GO:0000139 Golgi membrane.
- TAS "membrane" (GO:0016020, PMID:8195250 ProtInc) is correct but too general vs Golgi membrane.

## Kinetics / functional sites (PMID:18348864)
- Homology-model + mutagenesis of Asn188, Pro189, Ser190, Arg272 (between L and S sialylmotifs) determine alpha2,8-linkage specificity. IDA GD3-synthase activity confirmed [PMID:18348864 "these sites are involved in determining the alpha2,8-linkage specificity of GD3-synthase."]. KM 83 uM GM3, 88 uM CMP-Neu5Ac (UniProt).

## Cloning / catalytic-activity primary evidence
- PMID:8195250 (Sasaki 1994, JBC): expression cloning GM3-specific alpha-2,8-ST (GD3 synthase); "specifically converts GM3 to GD3"; gene on chr 12. EXP GO:0003828.
- PMID:8058740 (Nara 1994, PNAS): expression cloning GD3 synthase; transfected cells express GD3. EXP GO:0003828.
- PMID:7937974 (Haraguchi 1994, PNAS): isolation of GD3 synthase gene via anti-GD2 mAb; directs GD3/GD2 expression. EXP GO:0003828.
- PMID:8631981 (Nakayama 1996, JBC): GD3 and GT3 made by a single enzyme (GD3/GT3ST); polysialyltransferase; brain-restricted expression. EXP GO:0003828 (also supports GT3 synthase activity).
- PMID:8706663 (Nara 1996, Eur J Biochem): acceptor specificity; makes GD1c/GT1a/GQ1b; SAT II + SAT V activity. IDA GO:0003828.
- PMID:22885356 (Steenackers 2012, Molecules): full text available; GD3S+ MCF-7 make b/c-series + GQ3/GP3; oligosialyltransferase. IDA GO:0003828.

## Interaction
- IntAct IPI GO:0005515 "protein binding" with OPTN (Q96CV9), from PMID:32814053 (Haenig 2020, Cell Rep) — a large-scale neurodegenerative-disease Y2H/interactome map. Bare protein binding; not part of the core catalytic function -> MARK_AS_OVER_ANNOTATED. UniProt records the interaction (Q92185; Q96CV9: OPTN; NbExp=3).

## Tissue / biology context
- Strongly expressed in melanoma lines, adult & fetal brain, lesser in lung [file:human/ST8SIA1/ST8SIA1-uniprot.txt "Strongly expressed in melanoma cell lines, adult"]. GD3 is a tumor-associated antigen (melanoma) and a b-series ganglioside precursor important in neurodevelopment and apoptosis modulation.

## Term decisions summary
- GO:0003828 (MF, all evidence lines): ACCEPT — core.
- GO:0008373 sialyltransferase activity (TAS PMID:8195250; IEA GO_REF:0000120): MODIFY -> GO:0003828 (parent, too general).
- GO:0001574 ganglioside biosynthetic process: proposed as core BP (new synthesis term).
- GO:0006688 glycosphingolipid biosynthetic process (TAS PMID:8195250): MODIFY -> GO:0001574 (more specific) / KEEP as broader correct.
- GO:0006665 sphingolipid metabolic process (IEA UniPathway): KEEP_AS_NON_CORE — correct but general ancestor.
- GO:0005975 carbohydrate metabolic process (TAS PMID:8195250): KEEP_AS_NON_CORE — very general but true.
- GO:0009311 oligosaccharide metabolic process (IBA): MARK_AS_OVER_ANNOTATED — gangliosides are glycolipids; over-broad.
- GO:0006491 N-glycan processing (IBA): REMOVE-worthy but IBA -> MARK_AS_OVER_ANNOTATED (wrong substrate class; ST8SIA1 acts on glycolipids, family-level over-propagation).
- GO:0009101 glycoprotein biosynthetic process (IEA InterPro): REMOVE — clearly-wrong IEA (acts on glycolipids not glycoproteins).
- GO:0000139 Golgi membrane (TAS Reactome; IEA SubCell): ACCEPT — core location.
- GO:0016020 membrane (TAS PMID:8195250): MODIFY -> GO:0000139 (too general).
- GO:0005515 protein binding (IPI OPTN): MARK_AS_OVER_ANNOTATED.
</content>
