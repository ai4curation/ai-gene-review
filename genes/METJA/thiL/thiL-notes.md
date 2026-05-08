# thiL (METJA) - Research Notes

Gene: thiL (MJ0028)
Organism: Methanocaldococcus jannaschii (strain ATCC 43067 / DSM 2661 / JAL-1 / JCM 10045 / NBRC 100440)
UniProt: Q60337
EC: 2.7.4.16

## Gene identity and function

thiL encodes thiamine-monophosphate kinase (TMP kinase), which catalyzes the final step of thiamine pyrophosphate (TPP) biosynthesis: the ATP-dependent phosphorylation of thiamine monophosphate (TMP) to form thiamine pyrophosphate (TPP), the biologically active form of vitamin B1.

The gene was originally identified as MJ0028 in the M. jannaschii genome sequencing project [PMID:8688087, "Complete genome sequence of the methanogenic archaeon, Methanococcus jannaschii"]. The thiL gene name and function were assigned by homology to the E. coli thiL locus, which was first characterized by Imamura and Nakayama (1982) [PMID:6284709, "the latter lacks thiamine monophosphate kinase activity"].

## Catalytic mechanism

Structural studies of ThiL from Aquifex aeolicus by McCulloch et al. (2008) established the mechanism of the enzyme [PMID:18311927, "The results suggest that AaThiL utilizes a direct, inline transfer of the gamma-phosphate of ATP to TMP rather than a phosphorylated enzyme intermediate"]. This distinguishes ThiL from other members of the PurM-like ATP-binding superfamily (PurM, PurL, HypE, SelD), which are believed to utilize phosphorylated intermediates during catalysis.

The Sullivan et al. (2019) crystal structures of A. baumannii ThiL in complex with substrates and products provided further support for this mechanism at high resolution [PMID:30867460, "The structures further support a previously proposed in-line attack reaction mechanism and show a distinct variability of metal content of the active site"]. Their structures show that the alpha-phosphate of TMP is positioned for in-line attack on the gamma-phosphate of ATP, and that even the product complex closely matches the substrate complex conformationally -- "the transferred phosphate group, the gamma-phosphate in AMPPNP and the beta-phosphate in TPP, barely changes position. The distance between the phosphorous atoms is only 1.0 A."

## Structural features

ThiL belongs to the PurM-like ATP-binding superfamily with a bilobal fold consisting of an N-terminal domain (PurM-like N-terminal fold, IPR016188/IPR036921) and a C-terminal domain (PurM-like C-terminal fold, IPR036676). The active site resides in the cleft between these two domains and also spans the dimer interface [PMID:30867460, "The active site is located in the dimer interface. ATP/ADP is deeply buried in pocket generated at the interface between molecule A and B"].

ThiL functions as a homodimer. The enzyme binds multiple magnesium ions in the active site to coordinate the phosphate groups of ATP and TMP [PMID:30867460, "the active site can accommodate a variety of metals, and that the metal content is in part influenced by the crystallization condition"]. However, magnesium appears to be the physiologically relevant metal, particularly for the transferred phosphate groups.

## Thiamine biosynthesis in archaea

The thiamine biosynthetic pathway in archaea is a chimera of eukaryote- and bacterium-type pathways [PMID:28115546, "In archaea, thiamine biosynthesis is an apparent chimera of eukaryote- and bacterium-type pathways that is not well defined at the level of enzymatic steps or regulatory mechanisms"]. M. jannaschii uses a eukaryote-like Thi4 for thiazole synthesis (which uses iron-dependent sulfide transfer rather than the suicide mechanism of yeast Thi4) [PMID:26928142, "the Thi4 ortholog from Methanococcus jannaschii uses exogenous sulfide and is catalytic"], and a bacterium-like ThiC for pyrimidine synthesis. In contrast, regulation of thiamine biosynthesis in archaea occurs via a transcriptional repressor ThiR rather than the riboswitch mechanism common in bacteria [PMID:28115546, "thiamine biosynthesis in archaea is regulated by a transcriptional repressor, ThiR, and not by a riboswitch"].

Comparative genomics analysis by Rodionov et al. (2002) predicted that archaea, eubacteria, and eukaryota have different pathways for HMP and thiazole biosynthesis [PMID:12376536, "eubacteria, archaea, and eukaryota have different pathways for the HMP and hydroxyethylthiazole biosynthesis"].

## ThiL as a drug target

ThiL is essential in bacteria (demonstrated in A. baumannii by transposon mutagenesis) and has no human homolog, making it an attractive antimicrobial target [PMID:30867460, "Humans lack ThiL, potentially making it an attractive antimicrobial therapeutic target for pathogens"]. Recent computational studies have explored ThiL as a drug target in Leptospira species [PMID:41662777].

## Key points for annotation

1. The M. jannaschii thiL (Q60337) has no direct experimental characterization; all annotations are based on homology (HAMAP, InterPro, UniRule).
2. The enzyme belongs to the thiamine-monophosphate kinase family (IPR006283, TIGR01379, PTHR30270).
3. All current GOA annotations are IEA (inferred from electronic annotation).
4. The protein is a soluble cytoplasmic enzyme with no transmembrane domains or signal peptides.
5. TPP is essential for central carbon metabolism as a cofactor for pyruvate dehydrogenase, transketolase, and alpha-ketoglutarate dehydrogenase.
