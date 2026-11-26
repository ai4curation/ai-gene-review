# HOXB-AS3 peptide (C0HLZ6) - review notes

## 2026-10-03 Tier 2 microprotein review

### Identity
- UniProt C0HLZ6 (HAS3P_HUMAN), Swiss-Prot reviewed, PE1, 53 aa, whole chain predicted
  disordered (MobiDB-lite). Gene HGNC:40283 HOXB-AS3 (HOXB cluster antisense RNA 3), a
  lncRNA gene on 17q21.32 antisense to HOXB5/HOXB6. The UniProt entry is the peptide; the
  lncRNA has no separate UniProt entry, so the folder name `HOXB-AS3` is unambiguous.
- Pfam PF21970 / InterPro IPR054146 (HOXB-AS3 family). No PANTHER/IBA coverage.
- Sequence is rich in Gly/Ser/Pro/Arg; no TM segment, no signal peptide.

### Literature - separate peptide-level from RNA-level work
Most HOXB-AS3 papers are about the lncRNA (ovarian, endometrial, lung, liver cancer, AML).
The review PMID:38213732 says so explicitly: "subsequent studies primarily focused on the RNA
level" and lists only two peptide-level cancer studies (colon PMID:28985503, OSCC
PMID:34457052).

**PMID:28985503 (Huang et al. 2017 Mol Cell)** - founding peptide paper. Only abstract
cached (full_text_available: false; not in PMC/Europe PMC OA). Abstract: the lncRNA "encodes
a conserved 53-aa peptide. The HOXB-AS3 peptide, not lncRNA, suppresses colon cancer (CRC)
growth"; peptide "competitively binds to the ariginine residues in RGG motif of hnRNP A1 and
antagonizes the hnRNP A1-mediated regulation of pyruvate kinase M (PKM) splicing by blocking
the binding of the ariginine residues in RGG motif of hnRNP A1 to the sequences flanking PKM
exon 9, ensuring the formation of lower PKM2". The miR-18a result behind the IDA row is not in
the abstract; UniProt FUNCTION says "Also suppresses HNRNPA1-mediated processing of microRNA
18a (miR-18a)". According to the review PMID:38213732, the peptide was detected with
a specific antibody and by mass spectrometry, and its expression depended on the start codon.
- Note "conserved": the review says the ORF is "conserved across primates" and the peptide is
  "absent in other species" [PMID:38213732].

**PMID:17558416 (Guil & Caceres 2007)** - context: hnRNP A1 "binds specifically to the
primary RNA sequence pri-miR-18a before Drosha processing" and depletion reduces "in vitro
processing activity with pri-miR-18a". So the hnRNP A1 step is pri-miRNA (Drosha)
processing, not pre-miRNA (Dicer) processing. The GOA row GO:2000632 "negative regulation of
pre-miRNA processing" may therefore name the wrong step (GO:2000635 negative regulation of
primary miRNA processing would fit the hnRNP A1 mechanism). Cannot confirm without the Mol Cell
full text, so I left it UNDECIDED.

**PMID:34457052 (Leng et al. 2021 Oncol Lett)**: full text cached. OSCC lines Cal-27/UM2.
shRNA knockdown of the whole transcript lowered proliferation and c-Myc protein; ORF
re-expression restored both ("indicating that the HOXB-AS3 protein, but not HOXB-AS3 mRNA
exerted its oncogenic function"). The IGF2BP2 interaction is one Flag co-IP in 293T ("HOXB-AS3
binds with IGF2BP2 as a whole complex"), with no direct-binding assay despite the title.
Mechanism is framed as **mRNA** stability ("IGF2BP2 is a well-studied m6A reader stabilizing
c-Myc mRNA"), but only c-Myc **protein** level was measured; no mRNA decay or protein
half-life experiment. So the GOA IMP row GO:0050821 "protein stabilization" is not supported:
the paper neither tests protein stability nor claims it (the claim is mRNA stability, itself
untested). Note the paper's direction (pro-proliferative in OSCC) is opposite to Huang
(tumour-suppressive in CRC).

**PMID:40417409 (Lin et al. 2025, COPD)**: describes "HOXB-AS3-32aa", one of three ORFs
predicted by ORF Find; its expression was measured by qRT-PCR (i.e. RNA), and a co-IP
with EZH2 was reported. This is a 32-aa product, not the 53-aa C0HLZ6 chain, and its
relation to C0HLZ6 is not established. Low relevance; not used for annotation.

### Decisions
- protein binding (HNRNPA1, IPI, PMID:28985503) -> MODIFY to GO:0140678 molecular function
  inhibitor activity (competitively blocks hnRNP A1 RGG-box RNA binding).
- protein binding (IGF2BP2, IPI, PMID:34457052) -> REMOVE (single co-IP; no informative MF).
- GO:0043484 regulation of RNA splicing (IMP) -> MODIFY to GO:0000381 regulation of
  alternative mRNA splicing, via spliceosome (PKM exon 9/10 switch). Core.
- GO:0050821 protein stabilization (IMP) -> REMOVE (see above).
- GO:2000632 negative regulation of pre-miRNA processing (IDA) -> UNDECIDED (full text
  unavailable; likely pri-miRNA step).

No NEW terms. Location not established for the peptide (no CC rows; abstract silent).
