# KYNU (human) — kynureninase — review notes

UniProt: Q16719 (KYNU_HUMAN), 465 aa, EC 3.7.1.3, HGNC:6469, gene MIM 605197.
All cited publications in `publications/` are abstract-only (`full_text_available: false`);
quotes below are verbatim from those abstracts or from the UniProt flat file.

## Identity and catalytic function

KYNU is **kynureninase** (L-kynurenine hydrolase, EC 3.7.1.3), a **pyridoxal-5'-phosphate
(PLP)-dependent** enzyme of the kynurenine pathway of tryptophan catabolism.

- "Kynureninase (L-kynurenine hydrolase), a pyridoxal-5'-phosphate-(pyridoxal-P)-dependent
  enzyme, catalyses the cleavage of L-kynurenine and L-3-hydroxykynurenine into anthranilic
  and 3-hydroxyanthranilic acids, respectively." [PMID:8706755 abstract]
- UniProt FUNCTION: "Catalyzes the cleavage of L-kynurenine (L-Kyn) and L-3-
  hydroxykynurenine (L-3OHKyn) into anthranilic acid (AA) and 3-hydroxyanthranilic acid
  (3-OHAA), respectively. Has a preference for the L-3-hydroxy form. Also has cysteine-
  conjugate-beta-lyase activity." [file:human/KYNU/KYNU-uniprot.txt]

The human (mammalian, "constitutive") enzyme **prefers 3-hydroxy-L-kynurenine** over
L-kynurenine — distinct from the "inducible" prokaryotic kynureninases which prefer
L-kynurenine:
- "The Homo sapiens and other eukaryotic constitutive kynureninases preferentially catalyze
  the hydrolytic cleavage of 3-hydroxy-l-kynurenine to produce 3-hydroxyanthranilate and
  l-alanine, while l-kynurenine is the substrate of many prokaryotic inducible
  kynureninases." [PMID:17300176 abstract]
- Kinetics: much higher affinity for 3-hydroxykynurenine. Recombinant enzyme Km = 28.3 µM
  for 3-hydroxy-DL-kynurenine [PMID:17300176]; "highly specific for 3-hydroxykynurenine
  (Km = 3.0 microm ...) and was inhibited by L-kynurenine (Ki = 20 microm)" [PMID:11985583].
  Native liver enzyme active for both, activity ratio 3-OH-Kyn : Kyn ~15:1 [PMID:6468727].

Reaction directs flux toward **quinolinate → NAD+**:
- "Kynureninase [E.C.3.7.1.3.] is one of the enzymes involved in the biosynthesis of NAD
  cofactors from tryptophan through the kynurenine pathway." [PMID:9180257 abstract]

## Cofactor / structure

PLP is the obligate cofactor; crystal structure solved as PLP-bound holoenzyme:
- UniProt COFACTOR: pyridoxal 5'-phosphate (ECO:0000269|PubMed:17300176)
  [file:human/KYNU/KYNU-uniprot.txt]
- "Kynureninase is a member of a large family of catalytically diverse but structurally
  homologous pyridoxal 5'-phosphate (PLP) dependent enzymes known as the aspartate
  aminotransferase superfamily or alpha-family." [PMID:17300176 abstract]
- "the atomic structure of the PLP-bound holoenzyme was determined" [PMID:17300176 abstract]
- PLP is bound via Schiff base to Lys276 (UniProt MOD_RES 276 "N6-(pyridoxal
  phosphate)lysine"; cloning paper assigned Lys276 as cofactor-binding) [PMID:8706755].

## Quaternary structure

Homodimer:
- UniProt SUBUNIT: "Homodimer." (ECO:0000269|PubMed:17300176) [file:human/KYNU/KYNU-uniprot.txt]
- Crystal structure in complex with PLP with reported homodimerization [PMID:17300176].
- IDA protein homodimerization activity annotation is from PMID:11985583 (purification
  showed monomeric mass 52.4 kDa by MALDI; native ~130,000 by gel filtration in
  PMID:6468727 consistent with a dimer of ~52 kDa subunits).

## Subcellular location

UniProt authoritative call: **Cytoplasm, cytosol** (ECO:0000269|PubMed:8706755;
HAMAP-Rule). [file:human/KYNU/KYNU-uniprot.txt]
- HPA IDA cytosol, Reactome cytosol.
- Older biochemical fractionation reported activity in **both cytosol and mitochondria**
  of human liver, with the same properties: "3-hydroxykynureninase in human liver was
  present in cytosol and mitochondria. The cytosolic enzyme and mitochondrial enzyme had
  the same physiological and enzymic properties." [PMID:6468727 abstract]. This is the
  basis for the IDA mitochondrion annotation; UniProt does not list mitochondrion, so I
  treat cytosol as the core location and mitochondrion as non-core.
- An IBA mitochondrion annotation (GO_REF:0000033, PANTHER:PTN001019478) is a phylogenetic
  inference not specifically supported for the human protein; treated as over-annotation.

## Pathway / biological process

- Tryptophan/kynurenine catabolism → quinolinate → de novo NAD+ biosynthesis.
- UniProt PATHWAY: "Cofactor biosynthesis; NAD(+) biosynthesis; quinolinate from
  L-kynurenine: step 2/3." [file:human/KYNU/KYNU-uniprot.txt]
- Cell-type kynureninase activity is a determinant of quinolinate production, and is
  induced by IFN-gamma: "High activities of kynurenine 3-hydroxylase, kynureninase or
  3-hydroxyanthranilate 3,4-dioxygenase were found in interferon-gamma-stimulated
  macrophages" ... "Kynurenine 3-hydroxylase and, in some cells, kynureninase and
  3-hydroxyanthranilate 3,4-dioxygenase are important determinants of whether a cell can
  make quinolinate." [PMID:9291104 abstract]. This supports both the quinolinate
  biosynthetic process (IDA) and response to type II interferon (IDA) annotations.

## Disease

Two Mendelian phenotypes caused by KYNU variants (both in UniProt DISEASE):

1. **Hydroxykynureninuria (HYXKY, MIM 236800)** — inborn error of amino-acid metabolism;
   massive urinary excretion of kynurenine, 3-hydroxykynurenine and xanthurenic acid.
   - First molecular case: homozygous T198A reduces activity: "Mutation analysis of KYNU
     encoding kynureninase of the index case revealed homozygosity for a c.593 A > G
     substitution leading to a threonine-to-alanine (T198A) shift." [PMID:17334708 abstract]
   - UniProt VARIANT 198 T->A "(in HYXKY; reduced 3-hydroxykynureninase activity)".

2. **Vertebral, cardiac, renal and limb defects syndrome 2 (VCRL2, MIM 617661)** —
   autosomal-recessive congenital malformation syndrome from loss-of-function KYNU (and
   HAAO) variants causing NAD deficiency:
   - "Variants were identified in two genes that encode enzymes of the kynurenine pathway,
     3-hydroxyanthranilic acid 3,4-dioxygenase (HAAO) and kynureninase (KYNU)." ... "The
     mutant enzymes had greatly reduced activity in vitro." ... "The patients had reduced
     levels of circulating NAD." ... "Niacin supplementation during gestation prevented
     the malformations in mice." [PMID:28792876 abstract]
   - This paper supports the IMP NAD+ biosynthetic process annotation and the IDA
     kynureninase activity annotation (in-vitro activity of mutant enzymes), and the
     UniProt "quinolinate from L-kynurenine: step 2/3" pathway involvement in NAD.

## Vitamin B6 dependence

Kynureninase is PLP-dependent, and its activity falls in vitamin-B6 deficiency:
- "lymphocyte kynureninase activity in a group (n = 12) of vitamin B6-deficient men was
  5.04 ... significantly (p = 0.005) lower than the 6.69 ... in men with a normal vitamin
  B6 status. This indicates that lymphocyte kynureninase activity is depressed during a
  vitamin B6 deficiency." [PMID:1939450 abstract]. Basis for the IMP "response to vitamin
  B6" annotation (GO:0034516). This is an indirect, cofactor-dependency observation rather
  than a demonstration that KYNU mediates a cellular response to vitamin B6; kept as
  non-core.

## Summary of curation decisions

Core molecular functions: **GO:0030429 kynureninase activity** (EXP/IDA, multiple refs) and
**GO:0030170 pyridoxal phosphate binding** (obligate cofactor). Homodimerization
(GO:0042803) is a real structural property but structural, kept as non-core MF.

Core biological process: tryptophan/kynurenine catabolism feeding de novo NAD+ biosynthesis
(GO:0006569 L-tryptophan catabolic process; GO:0019805 quinolinate biosynthetic process;
GO:0034354 'de novo' NAD+ biosynthetic process from L-tryptophan; GO:0009435 NAD+
biosynthetic process). Core location: cytosol (GO:0005829).

Non-core / over-annotations: mitochondrion (IBA over-annotated; IDA kept non-core),
response to type II interferon (context/inducibility, non-core), response to vitamin B6
(cofactor-dependency phenomenon, non-core), NAD+ biosynthetic process is a valid but
higher-level process that is accepted as core context.
