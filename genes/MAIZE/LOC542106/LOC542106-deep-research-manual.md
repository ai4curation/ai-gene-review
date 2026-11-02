# LOC542106 (maize beta-expansin EXPB1b / "EXPB9", a Zea m 1 group-1 pollen allergen) - manual literature research

No deep-research provider was available; this summary was assembled manually from
cached publications, NCBI Gene, NCBI GenBank and UniProt records.

## Identity

- UniProtKB K7WCD1 (TrEMBL, PE 3; B73 v5 model Zm00001eb391800, chromosome 9) is
  cross-referenced to GeneID 542106, RefSeq NP_001352637.1. fetch-gene resolved K7WCD1
  and the GOA file is keyed to K7WCD1.
- NCBI Gene 542106 (queried via E-utilities esummary, 2026-10-28): name LOC542106,
  description "lo1 pI allergen homolog 1", aliases "ZEAMMB73_Zm00001d047135, EXPB1B,
  EXPB9, GRMZM2G072886, lop1", other designations including "beta-expansin-1b",
  "expansin-B9", "pollen allergen Zea m 1", "Zea mI", "wall loosening protein".
- The reviewed Swiss-Prot entry for EXPB1 / Zea m 1d is a different accession, P58738
  (GeneID 103638968/103638970). Its sequence is identical to GenBank AAO45608
  (AY197353), the EXPB1 cDNA whose product was purified and crystallised.
- Pairwise comparison (own analysis, both 269 aa, ungapped): K7WCD1 differs from
  AAO45608/P58738 at five positions only - A20V (in the signal peptide), Y116F, I149L,
  Y191F, V251I. All are conservative; the K7WCD1 mature chain is ~98% identical to
  Zea m 1d. K7WCD1 is therefore one of the near-identical EXPB1 duplicates, not the
  divergent Zea m 1 class.

## Family and domain architecture (UniProt K7WCD1)

- "Belongs to the expansin family. Expansin B subfamily." (ARBA-only in this TrEMBL
  record; independently supported by PANTHER PTHR31692:SF7, InterPro IPR005795 LolPI,
  IPR007118, IPR007117, PROSITE PS50842/PS50843).
- SignalP signal peptide 1-24; EG45 / DPBB domain 1 (63-169) and expansin
  cellulose-binding-like domain 2 (183-264).
- UniProt CAUTION from PROSITE-ProRule PRU00079 ("Lacks conserved residue(s) required
  for the propagation of feature annotation"); a third PRU00079 disulfide was not
  propagated. Given 98% identity with crystallised EXPB1 this is unlikely to have
  functional consequences.

## Activity of the Zea m 1 / EXPB1 proteins (experiments on the native pollen protein)

- Maize pollen extracts have potent expansin-like wall extension activity, selective
  for grass walls, attributed at least partly to group-1 allergens; "We propose that
  group I allergens facilitate invasion of the pollen tube into the maternal tissues by
  loosening the cell walls of the grass stigma and style" [PMID:9177257, abstract].
- Four Zea m 1 isoforms purified from pollen; "Highly purified Zea m 1d induced
  extension of a variety of grass walls but not dicot walls" [PMID:12913162, abstract].
- Crystal structure of native Zea m 1d (EXPB1, AAO45608): two-domain protein forming a
  shallow polysaccharide-binding groove; "EXPB1 lacks a second aspartate that serves as
  the catalytic base required for hydrolytic activity in GH45 enzymes"; "EXPB1 binds to
  maize cell walls, most strongly to xylans, causing swelling of the cell wall"; "Tests
  for hydrolytic activity by EXPB1 with various wall polysaccharides proved negative"
  [PMID:16984999].
- Binding target: "the protein primarily binds glucuronoarabinoxylan (GAX), the major
  matrix polysaccharide in grass CWs"; binding is electrostatic and cellulose binding is
  very weak [PMID:27729469, abstract].
- Caveat: these preparations were purified from pollen. Because K7WCD1 differs from
  Zea m 1d by only four mature-chain residues, the native "Zea m 1d" spot very likely
  contains the LOC542106 product as well; Valdivia et al. state that "additional genes
  highly similar to EXPB1 (>98.8% nucleotide sequence identity) also code for the same
  isoform" [PMID:17225858].

## Expression

- Zea mI cDNA: "Northern analysis shows expression only in pollen, not in vegetative or
  female floral tissues" [PMID:8406014, abstract]. The probe would not distinguish the
  EXPB1 duplicates.
- Wu et al. 2001: "the beta-expansins ExpB1 (specifically expressed in maize pollen)"
  [PMID:11351085]; again a probe that cannot distinguish near-identical copies.

## Genetics (PMID:17225858, Valdivia et al. 2007, full text read)

- A Mu insertion "in EXPB1 (GenBank Accession AY197353)" near the intron border of the
  fourth exon. The insertion "reduced by 31%" total Zea m 1 in pollen; it had "no
  effect on pollen viability, in vitro pollen tube growth" but under large pollen loads
  "the transposon mutation is vastly underrepresented in the progeny", i.e. reduced
  competitive pollen tube growth in the silk.
- Which of the near-identical genomic copies carries the insertion is not established in
  the paper beyond its identification with AY197353 (whose product is P58738). The
  phenotype is not attributable specifically to LOC542106, and it is a phenotype, not a
  demonstration of which entity performs a process step.

## Nomenclature uncertainty

- Yennawar et al. list the Zea m 1 proteins as "EXPB1, EXPB9, EXPB10, and EXPB11 in two
  rather divergent sequence classes" [PMID:16984999]. NCBI attaches both "EXPB1B" and
  "EXPB9" to GeneID 542106, but K7WCD1 is ~98% identical to EXPB1, so the
  "EXPB1b" designation fits the sequence; whether "EXPB9" is correctly attached is
  unclear.
