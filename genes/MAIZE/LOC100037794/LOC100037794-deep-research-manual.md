# LOC100037794 (ZmrbohB) - manual literature research

No deep-research API was available; this file was compiled manually from cached
publications (`publications/PMID_*.md`), NCBI Gene and NCBI Nucleotide.

## Identity

- UniProt A0A1D6ND49 (TrEMBL, unreviewed, 943 aa), gene symbol LOC100037794,
  NCBI GeneID 100037794, Zm00001eb154010 (B73 v5, chromosome 3), older ids
  Zm00001d043543 / GRMZM2G138152.
- NCBI Gene lists the aliases ZmrbohB / rbohB. GenBank EU807966 is "Zea mays
  respiratory burst oxidase protein B variant beta (rbohB) mRNA", submitted by
  Lin and Jiang (Nanjing Agricultural University), the group that cloned the gene.
- Caution: a 2025 m6A paper (PMID:41514981) calls a different maize gene
  "RBOHB" (Zm00001eb341260, chromosome 8). That paper is not about this locus.

## Cloning and expression (Lin et al. 2009, PMID:19261072, abstract only)

[PMID:19261072 "The full-length cDNA of ZmrbohB encodes a 942 amino acid protein containing
all of the respiratory burst oxidase homolog catalytically critical motifs."]
Two splice isoforms exist; the beta isoform retains intron 11 with a premature stop
codon [PMID:19261072 "Spliced transcript ZmrbohB-beta retains an unspliced
intron 11 that carries a premature termination codon and probably leads to
nonsense-mediated mRNA decay."]. ZmrbohB-alpha is induced by wounding, cold, heat,
UV and salt [PMID:19261072 "The transcripts
of ZmrbohB-alpha accumulated markedly when the maize seedlings were subjected to
various abiotic stimuli"].

## Brassinosteroid signalling (Zhang et al. 2010, PMID:20693409, full text)

BR treatment of maize leaves induces apoplastic H2O2; DPI (NADPH oxidase
inhibitor) and catalase block it, and ZmMPK5 activity is required for the late
phase. ZmrbohB expression was measured by qRT-PCR with GenBank EU807966 primers:
[PMID:20693409 "BR treatment significantly elevated the expression of ZmrbohA–ZmrbohD in leaves of maize plants."]
[PMID:20693409 "These results suggest that BR-induced apoplastic H2O2 accumulation can induce NADPH oxidase gene expression to produce more H2O2 in BR signalling."]
The paper measures transcript levels of four Zmrboh genes together; it does not
measure the activity of the ZmrbohB protein, so it is expression evidence only.

## Other maize expression studies (abstract only unless stated)

- Aphid feeding: [PMID:27178208 "lower elevations were noted in level of rbohB mRNA"].
- ZmRop1 overexpression/silencing alters ZmRBOHB transcript (PMID:36540415, full text).
- Drought plus cold upregulates ZmRbohA and ZmRbohB (PMID:42585738).
- ZmCDPK7 phosphorylates "RBOHB at Ser-99" (PMID:33331695, abstract only). The
  A0A1D6ND49 sequence has Ser at position 99, but the abstract does not give the
  gene id, so assignment to this locus is not confirmed.

## Family-level biochemistry (Arabidopsis orthologs)

Plant RBOHs are gp91phox/NOX2 homologues with an N-terminal extension carrying
EF-hands; Ca2+ binding to the EF-hands activates ROS production
[PMID:18218618 "This activation required a
conformational change in the EF-hand region, as a result of Ca(2+) binding to
the EF-hand motifs."]. Superoxide is the proximal product, H2O2 forms by dismutation
[PMID:11756663 "putative plant plasma membrane NADPH oxidase can produce superoxide"].

## Sequence features (UniProt A0A1D6ND49)

Pfam NADPH_Ox (PF08414, plant RBOH N-terminal regulatory domain), EF-hand
(PROSITE PS50222, 258-293), Ferric_reduct (PF01794, heme-binding TM domain;
His463/His477/His565/His578 heme ligands by PIRSR), FAD_binding_8 and
NAD_binding_6; four Phobius TM helices (the canonical six-TM NOX core is
partially predicted). PANTHER PTHR11972:SF153 (RBOH A subfamily name).
