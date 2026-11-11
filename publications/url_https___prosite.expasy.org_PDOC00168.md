---
reference_id: url:https://prosite.expasy.org/PDOC00168
extractor_version: 1
url_source_version: 2
title: PROSITE
content_type: url
---

# PROSITE

## Content

PROSITE
Home
ScanProsite
Browse
Browse by documentation entries
Browse by ProRule description
Browse by taxonomic scope
Browse by number of hits
ProRule
Description
Browse by ProRule description
Browse by enzyme class
Browse by UniProtKB feature key
Browse by GO term
Browse by keyword
Browse by taxonomic scope
Browse by PROSITE entry name
Documentation
Downloads
About
Contact
PROSITE documentation PDOC00168
2-oxo acid dehydrogenases acyltransferase component lipoyl binding site
View entry in original PROSITE document format
View entry in raw text format (no links)
PURL: https://purl.expasy.org/prosite/documentation/PDOC00168
Description
Technical section
References
Copyright
Miscellaneous
Description
The 2-oxo acid dehydrogenase multienzyme complexes [1,2] from bacterial and eukaryotic sources catalyze the oxidative decarboxylation of 2-oxo acids to the corresponding acyl-CoA. The three members of this family of multienzyme complexes are:
Pyruvate dehydrogenase complex (PDC).
2-oxoglutarate dehydrogenase complex (OGDC).
Branched-chain 2-oxo acid dehydrogenase complex (BCOADC).
These three complexes share a common architecture: they are composed of multiple copies of three component enzymes - E1, E2 and E3. E1 is a thiamine pyrophosphate-dependent 2-oxo acid dehydrogenase, E2 a dihydrolipamide acyltransferase, and E3 an FAD-containing dihydrolipamide dehydrogenase.
E2 acyltransferases have an essential cofactor, lipoic acid, which is covalently bound via a amide linkage to a lysine group. The E2 components of OGCD and BCOACD bind a single lipoyl group, while those of PDC bind either one (in yeast and in Bacillus), two (in mammals), or three (in Azotobacter and in Escherichia coli) lipoyl groups [3].
In addition to the E2 components of the three enzymatic complexes described above, a lipoic acid cofactor is also found in the following proteins:
H-protein of the glycine cleavage system (GCS) [4]. GCS is a multienzyme complex of four protein components, which catalyzes the degradation of glycine. H protein shuttles the methylamine group of glycine from the P protein to the T protein. H-protein from either prokaryotes or eukaryotes binds a single lipoic group.
Mammalian and yeast pyruvate dehydrogenase complexes differ from that of other sources, in that they contain, in small amounts, a protein of unknown function - designated protein X or component X. Its sequence is closely related to that of E2 subunits and seems to bind a lipoic group [5].
Fast migrating protein (FMP) (gene acoC) from Alcaligenes eutrophus [6]. This protein is most probably a dihydrolipamide acyltransferase involved in acetoin metabolism.
We developed a signature pattern which allows the detection of the lipoyl-binding site.
Note:
The domain around the lipoyl-binding lysine residue is evolutionary related to that around the biotin-binding lysine residue of biotin requiring enzymes (see <PDOC00167>).
Last update:
April 2006 / Pattern revised.
-------------------------------------------------------------------------------
Technical section
PROSITE method (with tools and information) covered by this documentation:
LIPOYL, PS00189; 2-oxo acid dehydrogenases acyltransferase component lipoyl binding site (PATTERN)
Consensus pattern:
[GDN]-x(2)-[LIVF]-x(3)-{VH}-{M}-[LIVMFCA]-x(2)-[LIVMFA]-{LDFY}-{KPE}-x-K-[GSTAIVW]-[STAIVQDN]-x(2)-[LIVMFS]-x(5)-[GCN]-x-[LIVMFY]
K is the lipoyl-binding site
Sequences in UniProtKB/Swiss-Prot known to belong to this class: 586
detected by PS00189: 531 (true positives)
undetected by PS00189: 55 (50 false negatives and 5 'partials')
Other sequence(s) in UniProtKB/Swiss-Prot detected by PS00189:
42 false positives.
Retrieve an alignment of UniProtKB/Swiss-Prot true positive hits:
Clustal format, color, condensed view / Clustal format, color / Clustal format, plain text / Fasta format
Retrieve the sequence logo from the alignment
Taxonomic distribution of all UniProtKB (Swiss-Prot + TrEMBL) entries matching PS00189
Retrieve a list of all UniProtKB (Swiss-Prot + TrEMBL) entries matching PS00189
Scan UniProtKB (Swiss-Prot and/or TrEMBL) entries against PS00189
Matching PDB structures: pdb_00001dxm pdb_00001fyc pdb_00001ghj pdb_00001ghk ... [ALL]
References
1 | Authors | Yeaman S.J.
Title | The 2-oxo acid dehydrogenase complexes: recent advances.
Source | Biochem. J. 257:625-632(1989).
PubMed ID | 2649080
2 | Authors | Yeaman S.J.
Source | Trends Biochem. Sci. 11:293-296(1986).
3 | Authors | Russel G.C. Guest J.R.
Source | Biochim. Biophys. Acta 1076:225-232(1991).
4 | Authors | Fujiwara K. Okamura-Ikeda K. Motokawa Y.
Title | Chicken liver H-protein, a component of the glycine cleavage system. Amino acid sequence and identification of the N epsilon-lipoyllysine residue.
Source | J. Biol. Chem. 261:8836-8841(1986).
PubMed ID | 3522581
5 | Authors | Behal R.H. Browning K.S. Hall T.B. Reed L.J.
Title | Cloning and nucleotide sequence of the gene for protein X from Saccharomyces cerevisiae.
Source | Proc. Natl. Acad. Sci. U.S.A. 86:8732-8736(1989).
PubMed ID | 2682658
6 | Authors | Priefert H. Hein S. Kruger N. Zeh K. Schmidt B. Steinbuechel A.
Title | Identification and molecular characterization of the Alcaligenes eutrophus H16 aco operon genes involved in acetoin catabolism.
Source | J. Bacteriol. 173:4056-4071(1991).
PubMed ID | 2061286
Copyright
PROSITE is copyrighted by the SIB Swiss Institute of Bioinformatics and distributed under the Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND 4.0) License, see prosite_license.html.
Expasy is operated by the SIB Swiss Institute of Bioinformatics
Terms of Use | Privacy policy
Back to the top