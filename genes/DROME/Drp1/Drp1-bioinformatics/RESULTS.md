# Drp1: PAINT node placement and domain architecture

## Methods

Two stdlib Python scripts in this folder, run 2026-11-17.

- `paint_node_placement.py` (copied unchanged from `genes/DROME/tim/tim-bioinformatics/`)
  reads the PANTHER 19.0 tree for PTHR11566 and the pinned PAINT node-level GAF (`IBD.gaf`,
  snapshot 19.0/2026-08-28), and prints the root-to-leaf paths for fly Drp1
  (FlyBase:FBgn0026479), fly shibire (FlyBase:FBgn0003392, classical dynamin) and human
  DNM1L (HGNC:2973), with every PAINT IBD/IKR/IRD row on each path. The two downloads were
  made with `curl` into the cache directory first, because the PANTHER server refused
  Python's default user agent (HTTP 403); the script reads cached files when they exist.

  ```
  python paint_node_placement.py PTHR11566 FlyBase:FBgn0026479 FlyBase:FBgn0003392 HGNC:2973 --cache-dir <cache>
  ```

- `domain_architecture.py` lists the Pfam matches InterPro reports for each protein
  (InterPro API) and the length and proline fraction of the sequence after the last Pfam
  domain (UniProt FASTA). Classical dynamins bind microtubules through their C-terminal
  proline-rich domain; the question is whether fly Drp1 has one.

  ```
  python domain_architecture.py Q9VQE0 P27619 O00429 Q05193
  ```

## Output: PAINT paths (seed lists of the root rows shortened here to their counts)

```
# PTHR11566: tree root PTN000170013 (None)
# IBD.gaf: https://data.pantherdb.org/ftp/downloads/paint/19.0/2026-08-28/IBD.gaf
## Path to DNM1L HGNC:2973 (Homo sapiens)
PTN000170013  event=DUPLICATION  taxon=-  subfamily=-  gene=-
    PAINT: GO:0005737 IBD from 45 seeds incl. FB:FBgn0026479|FB:FBgn0261276|FB:FBgn0003392
    PAINT: GO:0008017 IBD from FB:FBgn0003392
    PAINT: GO:0003924 IBD from 21 seeds (no fly seed)
    PAINT: GO:0005874 IBD from UniProtKB:P50570|WB:WBGene00001130|AGI_LocusCode:AT5G42080
    PAINT: GO:0016020 IBD from 32 seeds incl. FB:FBgn0003392
  PTN000902162  event=SPECIATION  taxon=Eukaryota  subfamily=PTHR11566:SF21  gene=-
    PTN008520527  event=SPECIATION  taxon=Unikonts  subfamily=-  gene=-
        PAINT: GO:0016559 IBD from UniProtKB:O00429|SGD:S000001709|MGI:MGI:1921256|SGD:S000003924
      PTN008520528  event=SPECIATION  taxon=Opisthokonts  subfamily=-  gene=-
        PTN008973342  event=DUPLICATION  taxon=-  subfamily=-  gene=-
          PTN002480309  event=SPECIATION  taxon=Metazoa-Choanoflagellida  subfamily=-  gene=-
              PAINT: GO:0000266 IBD from WB:WBGene00001093|UniProtKB:O00429|FB:FBgn0026479|MGI:MGI:1921256
              PAINT: GO:0048312 IBD from UniProtKB:O00429|RGD:620416
              PAINT: GO:0005739 IBD from WB:WBGene00001093|RGD:620416|UniProtKB:Q2KIA5|UniProtKB:O00429|FB:FBgn0026479|MGI:MGI:1921256
            PTN000902165  event=SPECIATION  taxon=Eumetazoa  subfamily=-  gene=-
              PTN000170088  event=SPECIATION  taxon=Bilateria  subfamily=-  gene=-
                PTN000170089  event=SPECIATION  taxon=Deuterostomia  subfamily=-  gene=-
                  PTN001357286  event=SPECIATION  taxon=Chordata  subfamily=-  gene=-
                    PTN008324415  event=SPECIATION  taxon=Craniata-Tunicata  subfamily=-  gene=-
                      PTN001357257  event=DUPLICATION  taxon=-  subfamily=-  gene=-
                        PTN002611464  event=SPECIATION  taxon=Euteleostomi  subfamily=PTHR11566:SF39  gene=-
                            PAINT: GO:0043653 IBD from UniProtKB:O00429|RGD:620416
                          PTN000170098  event=SPECIATION  taxon=Tetrapoda  subfamily=-  gene=-
                            PTN000170099  event=SPECIATION  taxon=Amniota  subfamily=-  gene=-
                              PTN000170100  event=SPECIATION  taxon=Mammalia  subfamily=-  gene=-
                                PTN000170101  event=SPECIATION  taxon=Theria  subfamily=-  gene=-
                                  PTN000170102  event=SPECIATION  taxon=Eutheria  subfamily=-  gene=-
                                    PTN000170103  event=SPECIATION  taxon=Euarchontoglires  subfamily=-  gene=-
                                      PTN000170247  event=SPECIATION  taxon=Catarrhini  subfamily=-  gene=-
                                        PTN002611465  event=SPECIATION  taxon=Homininae  subfamily=-  gene=-
                                          PTN000902167  event=SPECIATION  taxon=Homo-Pan  subfamily=-  gene=-
                                            PTN002480311  event=-  taxon=Homo sapiens  subfamily=-  gene=DNM1L
## Path to Drp1 FlyBase:FBgn0026479 (Drosophila melanogaster)
PTN000170013  event=DUPLICATION  taxon=-  subfamily=-  gene=-
    PAINT: GO:0005737 IBD from 45 seeds incl. FB:FBgn0026479|FB:FBgn0261276|FB:FBgn0003392
    PAINT: GO:0008017 IBD from FB:FBgn0003392
    PAINT: GO:0003924 IBD from 21 seeds (no fly seed)
    PAINT: GO:0005874 IBD from UniProtKB:P50570|WB:WBGene00001130|AGI_LocusCode:AT5G42080
    PAINT: GO:0016020 IBD from 32 seeds incl. FB:FBgn0003392
  PTN000902162  event=SPECIATION  taxon=Eukaryota  subfamily=PTHR11566:SF21  gene=-
    PTN008520527  event=SPECIATION  taxon=Unikonts  subfamily=-  gene=-
        PAINT: GO:0016559 IBD from UniProtKB:O00429|SGD:S000001709|MGI:MGI:1921256|SGD:S000003924
      PTN008520528  event=SPECIATION  taxon=Opisthokonts  subfamily=-  gene=-
        PTN008973342  event=DUPLICATION  taxon=-  subfamily=-  gene=-
          PTN002480309  event=SPECIATION  taxon=Metazoa-Choanoflagellida  subfamily=-  gene=-
              PAINT: GO:0000266 IBD from WB:WBGene00001093|UniProtKB:O00429|FB:FBgn0026479|MGI:MGI:1921256
              PAINT: GO:0048312 IBD from UniProtKB:O00429|RGD:620416
              PAINT: GO:0005739 IBD from WB:WBGene00001093|RGD:620416|UniProtKB:Q2KIA5|UniProtKB:O00429|FB:FBgn0026479|MGI:MGI:1921256
            PTN000902165  event=SPECIATION  taxon=Eumetazoa  subfamily=-  gene=-
              PTN000170088  event=SPECIATION  taxon=Bilateria  subfamily=-  gene=-
                PTN002611477  event=SPECIATION  taxon=Protostomia  subfamily=-  gene=-
                  PTN000170124  event=SPECIATION  taxon=Ecdysozoa  subfamily=-  gene=-
                    PTN008324416  event=SPECIATION  taxon=Arthropoda  subfamily=-  gene=-
                      PTN000902177  event=SPECIATION  taxon=Hexapoda-Crustacea  subfamily=-  gene=-
                        PTN002611478  event=SPECIATION  taxon=Endopterygota  subfamily=-  gene=-
                          PTN000170128  event=SPECIATION  taxon=Diptera  subfamily=-  gene=-
                            PTN000170129  event=-  taxon=Drosophila melanogaster  subfamily=-  gene=Drp1
## Path to shi FlyBase:FBgn0003392 (Drosophila melanogaster)
PTN000170013  event=DUPLICATION  taxon=-  subfamily=-  gene=-
    PAINT: GO:0005737 IBD from 45 seeds incl. FB:FBgn0026479|FB:FBgn0261276|FB:FBgn0003392
    PAINT: GO:0008017 IBD from FB:FBgn0003392
    PAINT: GO:0003924 IBD from 21 seeds (no fly seed)
    PAINT: GO:0005874 IBD from UniProtKB:P50570|WB:WBGene00001130|AGI_LocusCode:AT5G42080
    PAINT: GO:0016020 IBD from 32 seeds incl. FB:FBgn0003392
  PTN008520579  event=SPECIATION  taxon=Eukaryota  subfamily=PTHR11566:SF212  gene=-
      PAINT: GO:0005886 IBD from MGI:MGI:107384|RGD:71096|WB:WBGene00001130|UniProtKB:Q05193|FB:FBgn0003392|RGD:727949|UniProtKB:P50570|RGD:2513
    PTN008520476  event=SPECIATION  taxon=Opisthokonts  subfamily=-  gene=-
      PTN000902092  event=SPECIATION  taxon=Metazoa-Choanoflagellida  subfamily=-  gene=-
        PTN000902093  event=SPECIATION  taxon=Eumetazoa  subfamily=-  gene=-
            PAINT: GO:0016185 IBD from FB:FBgn0003392
            PAINT: GO:0045202 IBD from FB:FBgn0003392|RGD:727949|RGD:2513|UniProtKB:P50570|MGI:MGI:1341299|MGI:MGI:107384|WB:WBGene00001130|RGD:71096
          PTN000170172  event=SPECIATION  taxon=Bilateria  subfamily=-  gene=-
            PTN002611568  event=SPECIATION  taxon=Protostomia  subfamily=-  gene=-
              PTN002480308  event=SPECIATION  taxon=Ecdysozoa  subfamily=-  gene=-
                PTN000902114  event=SPECIATION  taxon=Arthropoda  subfamily=-  gene=-
                  PTN000902115  event=SPECIATION  taxon=Hexapoda-Crustacea  subfamily=-  gene=-
                    PTN002611569  event=SPECIATION  taxon=Endopterygota  subfamily=-  gene=-
                      PTN000170314  event=SPECIATION  taxon=Diptera  subfamily=-  gene=-
                        PTN000170315  event=-  taxon=Drosophila melanogaster  subfamily=-  gene=shi
```

## Output: domain architecture

```
accession	length	pfam_domains	PH_domain(PF00169)	C-term_after_last_domain	Pro_fraction_C-term
Q9VQE0	735	PF00350 Dynamin family 28-216; PF01031 Dynamin central region 224-504; PF02212 Dynamin GTPase effector domain 639-729	False	6 aa	0.00
#   >tr|Q9VQE0|Q9VQE0_DROME dynamin GTPase OS=Drosophila melanogaster OX=7227 GN=Drp1 PE=1 SV=1
P27619	877	PF00350 Dynamin family 29-202; PF01031 Dynamin central region 210-497; PF00169 PH domain 514-617; PF02212 Dynamin GTPase effector domain 647-736	True	141 aa	0.21
#   >sp|P27619|DYN_DROME Dynamin OS=Drosophila melanogaster OX=7227 GN=shi PE=1 SV=2
O00429	736	PF00350 Dynamin family 28-217; PF01031 Dynamin central region 225-509; PF02212 Dynamin GTPase effector domain 639-730	False	6 aa	0.00
#   >sp|O00429|DNM1L_HUMAN Dynamin-1-like protein OS=Homo sapiens OX=9606 GN=DNM1L PE=1 SV=2
Q05193	864	PF00350 Dynamin family 34-207; PF01031 Dynamin central region 215-501; PF00169 PH domain 520-621; PF02212 Dynamin GTPase effector domain 656-744	True	120 aa	0.30
#   >sp|Q05193|DYN1_HUMAN Dynamin-1 OS=Homo sapiens OX=9606 GN=DNM1 PE=1 SV=2
```

## Interpretation

- The family root PTN000170013 is a duplication node above the split between the DNM1L/Drp1
  clade (PTN000902162, subfamily SF21) and the classical dynamin clade (PTN008520579, which
  holds fly shibire). Five IBDs sit on this root: GTPase activity, cytoplasm, membrane,
  microtubule and microtubule binding. The microtubule-binding IBD has a single seed, fly
  shibire (FB:FBgn0003392). The microtubule IBD is seeded by human DNM2 (P50570), worm dyn-1
  (WBGene00001130) and Arabidopsis DRP1A (AT5G42080), none of them in the DNM1L/Drp1 clade.
- Peroxisome fission is asserted at PTN008520527 (Unikonts) inside the DNM1L/Drp1 clade, from
  human DNM1L, mouse Dnm1l and yeast Dnm1 and Vps1. Mitochondrial fission, mitochondrion and
  intracellular distribution of mitochondria are asserted at PTN002480309
  (Metazoa-Choanoflagellida); fly Drp1 is itself a seed of the first two. Fly Drp1 descends
  from both nodes, and no IKR or IRD (loss) row sits on its path.
- Fly Drp1, like human DNM1L, has only the GTPase, middle (central) and GED Pfam domains, no
  PH domain, and 6 residues after the GED. Fly shibire and human DNM1 have a PH domain and a
  C-terminal tail of 120-141 residues that is 21-30% proline (the proline-rich domain). The
  microtubule-binding seed therefore has a domain that the Drp1 clade lacks.
