# Sirt1: PAINT node placement on the PANTHER PTHR11085 tree

## Method

`paint_node_placement.py` (stdlib Python, this folder; same script as in
`genes/DROME/tim/tim-bioinformatics/`) downloads the PANTHER 19.0 tree for
PTHR11085 and the pinned PAINT node-level GAF (`IBD.gaf`, snapshot
19.0/2026-08-28), then prints the root-to-leaf path for fly Sirt1
(FlyBase:FBgn0024291), human SIRT1 (HGNC:14929) and budding yeast SIR2
(SGD:S000002200), with every PAINT IBD/IKR/IRD row on the path, and the leaves
under PTN000872223.

Command (run 2026-11-16):

```
python paint_node_placement.py PTHR11085 FlyBase:FBgn0024291 HGNC:14929 SGD:S000002200 \
    --leaves PTN000872223
```

## Output

```
# PTHR11085: tree root PTN000119154 (LUCA)
# IBD.gaf: https://data.pantherdb.org/ftp/downloads/paint/19.0/2026-08-28/IBD.gaf

## Path to SIRT1 HGNC:14929 (Homo sapiens)
PTN000119154  event=SPECIATION  taxon=LUCA  subfamily=PTHR11085:SF10  gene=-
  PTN008718612  event=SPECIATION  taxon=Archaea-Eukaryota  subfamily=-  gene=-
      PAINT: GO:0017136 IBD from PomBase:SPAC1783.04c|FB:FBgn0037802|FB:FBgn0024291|MGI:MGI:1354161|UniProtKB:Q57V41|SGD:S000005936|PomBase:SPBC16D10.07c|UniProtKB:Q9NRC8|UniProtKB:Q8N6T7|UniProtKB:Q96EB6|RGD:1308542|SGD:S000005429|SGD:S000002200|UniProtKB:C8V3W5|SGD:S000002599|UniProtKB:Q8IXJ6|MGI:MGI:2135607|PomBase:SPCC132.02|FB:FBgn0038788|SGD:S000005551|MGI:MGI:2385849
    PTN008492176  event=DUPLICATION  taxon=-  subfamily=-  gene=-
        PAINT: GO:0005634 IBD from MGI:MGI:1927664|dictyBase:DDB_G0289967|MGI:MGI:2135607|UniProtKB:Q8IXJ6|FB:FBgn0038788|WB:WBGene00004803|SGD:S000002599|CGD:CAL0000190389|SGD:S000002200|SGD:S000005429|UniProtKB:Q96EB6|MGI:MGI:1354161|PomBase:SPAC1783.04c|FB:FBgn0037802|PomBase:SPBC16D10.07c|WB:WBGene00004800|dictyBase:DDB_G0270928|UniProtKB:Q8IE47|UniProtKB:Q9NRC8|RGD:1308542|UniProtKB:Q8N6T7|UniProtKB:Q7XWV4|UniProtKB:Q57V41|FB:FBgn0024291|AGI_LocusCode:AT5G55760|CGD:CAL0000181323|SGD:S000005936
      PTN000872222  event=SPECIATION  taxon=Eukaryota  subfamily=PTHR11085:SF9  gene=-
          PAINT: GO:0003714 IBD from MGI:MGI:2135607|UniProtKB:Q96EB6
          PAINT: GO:0031509 IBD from PomBase:SPBC16D10.07c|SGD:S000002200
          PAINT: GO:0046970 IBD from UniProtKB:Q96EB6|PomBase:SPBC16D10.07c|SGD:S000002200|UniProtKB:C8V3W5
          PAINT: GO:0006974 IBD from MGI:MGI:2135607|WB:WBGene00004800|SGD:S000002200|UniProtKB:Q96EB6
          PAINT: GO:0046969 IBD from PomBase:SPBC16D10.07c|SGD:S000002200|UniProtKB:Q96EB6|MGI:MGI:2135607
          PAINT: GO:0032041 IBD from SGD:S000002200|PomBase:SPBC16D10.07c|UniProtKB:Q96EB6
        PTN000119300  event=SPECIATION  taxon=Unikonts  subfamily=-  gene=-
          PTN000119301  event=SPECIATION  taxon=Opisthokonts  subfamily=-  gene=-
            PTN000872223  event=SPECIATION  taxon=Metazoa-Choanoflagellida  subfamily=-  gene=-
                PAINT: GO:0045892 IBD from UniProtKB:Q96EB6|MGI:MGI:2135607
                PAINT: GO:0033553 IBD from UniProtKB:Q96EB6
                PAINT: GO:0005654 IBD from UniProtKB:Q96EB6|FB:FBgn0024291
                PAINT: GO:0005637 IBD from UniProtKB:Q96EB6
              PTN000872224  event=SPECIATION  taxon=Eumetazoa  subfamily=-  gene=-
                PTN000119302  event=SPECIATION  taxon=Bilateria  subfamily=-  gene=-
                  PTN000119303  event=SPECIATION  taxon=Deuterostomia  subfamily=-  gene=-
                    PTN001338932  event=SPECIATION  taxon=Chordata  subfamily=-  gene=-
                      PTN008492200  event=SPECIATION  taxon=Craniata-Tunicata  subfamily=-  gene=-
                        PTN002595008  event=SPECIATION  taxon=Euteleostomi  subfamily=-  gene=-
                          PTN008718623  event=SPECIATION  taxon=Tetrapoda  subfamily=-  gene=-
                            PTN000119307  event=SPECIATION  taxon=Amniota  subfamily=-  gene=-
                              PTN008718624  event=SPECIATION  taxon=Mammalia  subfamily=-  gene=-
                                PTN001338933  event=SPECIATION  taxon=Theria  subfamily=-  gene=-
                                  PTN000119308  event=SPECIATION  taxon=Eutheria  subfamily=-  gene=-
                                    PTN000119309  event=SPECIATION  taxon=Euarchontoglires  subfamily=-  gene=-
                                      PTN000119310  event=SPECIATION  taxon=Catarrhini  subfamily=-  gene=-
                                        PTN002595009  event=SPECIATION  taxon=Homininae  subfamily=-  gene=-
                                          PTN000119311  event=SPECIATION  taxon=Homo-Pan  subfamily=-  gene=-
                                            PTN002476412  event=-  taxon=Homo sapiens  subfamily=-  gene=SIRT1

## Path to Sirt1 FlyBase:FBgn0024291 (Drosophila melanogaster)
PTN000119154  event=SPECIATION  taxon=LUCA  subfamily=PTHR11085:SF10  gene=-
  PTN008718612  event=SPECIATION  taxon=Archaea-Eukaryota  subfamily=-  gene=-
      PAINT: GO:0017136 IBD from PomBase:SPAC1783.04c|FB:FBgn0037802|FB:FBgn0024291|MGI:MGI:1354161|UniProtKB:Q57V41|SGD:S000005936|PomBase:SPBC16D10.07c|UniProtKB:Q9NRC8|UniProtKB:Q8N6T7|UniProtKB:Q96EB6|RGD:1308542|SGD:S000005429|SGD:S000002200|UniProtKB:C8V3W5|SGD:S000002599|UniProtKB:Q8IXJ6|MGI:MGI:2135607|PomBase:SPCC132.02|FB:FBgn0038788|SGD:S000005551|MGI:MGI:2385849
    PTN008492176  event=DUPLICATION  taxon=-  subfamily=-  gene=-
        PAINT: GO:0005634 IBD from MGI:MGI:1927664|dictyBase:DDB_G0289967|MGI:MGI:2135607|UniProtKB:Q8IXJ6|FB:FBgn0038788|WB:WBGene00004803|SGD:S000002599|CGD:CAL0000190389|SGD:S000002200|SGD:S000005429|UniProtKB:Q96EB6|MGI:MGI:1354161|PomBase:SPAC1783.04c|FB:FBgn0037802|PomBase:SPBC16D10.07c|WB:WBGene00004800|dictyBase:DDB_G0270928|UniProtKB:Q8IE47|UniProtKB:Q9NRC8|RGD:1308542|UniProtKB:Q8N6T7|UniProtKB:Q7XWV4|UniProtKB:Q57V41|FB:FBgn0024291|AGI_LocusCode:AT5G55760|CGD:CAL0000181323|SGD:S000005936
      PTN000872222  event=SPECIATION  taxon=Eukaryota  subfamily=PTHR11085:SF9  gene=-
          PAINT: GO:0003714 IBD from MGI:MGI:2135607|UniProtKB:Q96EB6
          PAINT: GO:0031509 IBD from PomBase:SPBC16D10.07c|SGD:S000002200
          PAINT: GO:0046970 IBD from UniProtKB:Q96EB6|PomBase:SPBC16D10.07c|SGD:S000002200|UniProtKB:C8V3W5
          PAINT: GO:0006974 IBD from MGI:MGI:2135607|WB:WBGene00004800|SGD:S000002200|UniProtKB:Q96EB6
          PAINT: GO:0046969 IBD from PomBase:SPBC16D10.07c|SGD:S000002200|UniProtKB:Q96EB6|MGI:MGI:2135607
          PAINT: GO:0032041 IBD from SGD:S000002200|PomBase:SPBC16D10.07c|UniProtKB:Q96EB6
        PTN000119300  event=SPECIATION  taxon=Unikonts  subfamily=-  gene=-
          PTN000119301  event=SPECIATION  taxon=Opisthokonts  subfamily=-  gene=-
            PTN000872223  event=SPECIATION  taxon=Metazoa-Choanoflagellida  subfamily=-  gene=-
                PAINT: GO:0045892 IBD from UniProtKB:Q96EB6|MGI:MGI:2135607
                PAINT: GO:0033553 IBD from UniProtKB:Q96EB6
                PAINT: GO:0005654 IBD from UniProtKB:Q96EB6|FB:FBgn0024291
                PAINT: GO:0005637 IBD from UniProtKB:Q96EB6
              PTN000872224  event=SPECIATION  taxon=Eumetazoa  subfamily=-  gene=-
                PTN000119302  event=SPECIATION  taxon=Bilateria  subfamily=-  gene=-
                  PTN002595017  event=SPECIATION  taxon=Protostomia  subfamily=-  gene=-
                    PTN000119330  event=SPECIATION  taxon=Ecdysozoa  subfamily=-  gene=-
                      PTN000872233  event=SPECIATION  taxon=Arthropoda  subfamily=-  gene=-
                        PTN000872234  event=SPECIATION  taxon=Hexapoda-Crustacea  subfamily=-  gene=-
                          PTN002595018  event=SPECIATION  taxon=Endopterygota  subfamily=-  gene=-
                            PTN000119332  event=-  taxon=Drosophila melanogaster  subfamily=-  gene=Sirt1

## Path to SIR2 SGD:S000002200 (Saccharomyces cerevisiae)
PTN000119154  event=SPECIATION  taxon=LUCA  subfamily=PTHR11085:SF10  gene=-
  PTN008718612  event=SPECIATION  taxon=Archaea-Eukaryota  subfamily=-  gene=-
      PAINT: GO:0017136 IBD from PomBase:SPAC1783.04c|FB:FBgn0037802|FB:FBgn0024291|MGI:MGI:1354161|UniProtKB:Q57V41|SGD:S000005936|PomBase:SPBC16D10.07c|UniProtKB:Q9NRC8|UniProtKB:Q8N6T7|UniProtKB:Q96EB6|RGD:1308542|SGD:S000005429|SGD:S000002200|UniProtKB:C8V3W5|SGD:S000002599|UniProtKB:Q8IXJ6|MGI:MGI:2135607|PomBase:SPCC132.02|FB:FBgn0038788|SGD:S000005551|MGI:MGI:2385849
    PTN008492176  event=DUPLICATION  taxon=-  subfamily=-  gene=-
        PAINT: GO:0005634 IBD from MGI:MGI:1927664|dictyBase:DDB_G0289967|MGI:MGI:2135607|UniProtKB:Q8IXJ6|FB:FBgn0038788|WB:WBGene00004803|SGD:S000002599|CGD:CAL0000190389|SGD:S000002200|SGD:S000005429|UniProtKB:Q96EB6|MGI:MGI:1354161|PomBase:SPAC1783.04c|FB:FBgn0037802|PomBase:SPBC16D10.07c|WB:WBGene00004800|dictyBase:DDB_G0270928|UniProtKB:Q8IE47|UniProtKB:Q9NRC8|RGD:1308542|UniProtKB:Q8N6T7|UniProtKB:Q7XWV4|UniProtKB:Q57V41|FB:FBgn0024291|AGI_LocusCode:AT5G55760|CGD:CAL0000181323|SGD:S000005936
      PTN000872222  event=SPECIATION  taxon=Eukaryota  subfamily=PTHR11085:SF9  gene=-
          PAINT: GO:0003714 IBD from MGI:MGI:2135607|UniProtKB:Q96EB6
          PAINT: GO:0031509 IBD from PomBase:SPBC16D10.07c|SGD:S000002200
          PAINT: GO:0046970 IBD from UniProtKB:Q96EB6|PomBase:SPBC16D10.07c|SGD:S000002200|UniProtKB:C8V3W5
          PAINT: GO:0006974 IBD from MGI:MGI:2135607|WB:WBGene00004800|SGD:S000002200|UniProtKB:Q96EB6
          PAINT: GO:0046969 IBD from PomBase:SPBC16D10.07c|SGD:S000002200|UniProtKB:Q96EB6|MGI:MGI:2135607
          PAINT: GO:0032041 IBD from SGD:S000002200|PomBase:SPBC16D10.07c|UniProtKB:Q96EB6
        PTN000119300  event=SPECIATION  taxon=Unikonts  subfamily=-  gene=-
          PTN000119301  event=SPECIATION  taxon=Opisthokonts  subfamily=-  gene=-
            PTN000872240  event=SPECIATION  taxon=Fungi  subfamily=-  gene=-
              PTN000872241  event=SPECIATION  taxon=Dikarya  subfamily=-  gene=-
                PTN000119333  event=SPECIATION  taxon=Ascomycota  subfamily=-  gene=-
                  PTN000119334  event=SPECIATION  taxon=Pezizomycotina-Saccharomycotina  subfamily=-  gene=-
                    PTN000872242  event=SPECIATION  taxon=Saccharomycetales  subfamily=-  gene=-
                      PTN000872243  event=SPECIATION  taxon=Saccharomycetaceae-Candida  subfamily=-  gene=-
                        PTN000119335  event=SPECIATION  taxon=Saccharomycetaceae  subfamily=-  gene=-
                          PTN000119336  event=DUPLICATION  taxon=-  subfamily=-  gene=-
                            PTN000119338  event=-  taxon=Saccharomyces cerevisiae  subfamily=-  gene=SIR2

## Leaves under PTN000872223  event=SPECIATION  taxon=Metazoa-Choanoflagellida  subfamily=-  gene=-
  Homo sapiens	SIRT1	HGNC:14929
  Pan troglodytes	SIRT1	Ensembl:ENSPTRG00000051532.1
  Gorilla gorilla gorilla	SIRT1	Ensembl:ENSGGOG00000010187.3
  Macaca mulatta	SIRT1	Ensembl:ENSMMUG00000030531.3
  Mus musculus	Sirt1	MGI:MGI=2135607
  Rattus norvegicus	Sirt1	RGD:1308542
  Bos taurus	SIRT1	Ensembl:ENSBTAG00000014023.6
  Sus scrofa	SIRT1	Ensembl:ENSSSCG00000010235.5
  Equus caballus	SIRT1	Ensembl:ENSECAG00000013909.4
  Felis catus	SIRT1	Ensembl:ENSFCAG00000012373.6
  Canis lupus familiaris	SIRT1	Ensembl:ENSCAFG00845001191.1
  Monodelphis domestica	SIRT1	Ensembl:ENSMODG00000017248.4
  Ornithorhynchus anatinus	SIRT1	Ensembl:ENSOANG00000050156.1
  Gallus gallus	SIRT1	Ensembl:ENSGALG00010009252.1
  Anolis carolinensis	sirt1	Ensembl:ENSACAG00000041427.1
  Xenopus laevis	sirt1.L	Gene:sirt1.L
  Xenopus laevis	sirt1.S	Gene:sirt1.S
  Xenopus tropicalis	sirt1	Gene:sirt1
  Oryzias latipes	sirt1	Ensembl:ENSORLG00000013667.2
  Danio rerio	sirt1	ZFIN:ZDB-GENE-070801-2
  lepisosteus oculatus	None	Ensembl:ENSLOCG00000011271.1
  Ciona intestinalis	None	Ensembl:ENSCING00000015552.2
  Branchiostoma floridae	LOC118410981	Gene:LOC118410981
  Strongylocentrotus purpuratus	None	EnsemblGenome:LOC105443501
  Strongylocentrotus purpuratus	None	EnsemblGenome:LOC591711
  Caenorhabditis elegans	sir-2.1	WormBase:WBGene00004800
  Caenorhabditis briggsae	sir-2.1	WormBase:WBGene00042025
  Pristionchus pacificus	WBGene00108481	EnsemblGenome:WBGene00108481
  Drosophila melanogaster	Sirt1	FlyBase:FBgn0024291
  Tribolium castaneum	AUGUSTUS-3.0.2_02584	EnsemblGenome:TC002584
  Daphnia pulex	SIR2	EnsemblGenome:DAPPUDRAFT_290541
  Ixodes scapularis	IscW_ISCW006267	EnsemblGenome:ISCW006267
  helobdella robusta	20213973	EnsemblGenome:HelroG66888
  Nematostella vectensis	NEMVEDRAFT_v1g136467	EnsemblGenome:NEMVEDRAFT_v1g136467
  Monosiga brevicollis	MONBRDRAFT_1942	EnsemblGenome:MONBRDRAFT_1942
  PAINT rows on nodes at or below PTN000872223:
    PTN000872223: GO:0045892 IBD from UniProtKB:Q96EB6|MGI:MGI:2135607
    PTN000872223: GO:0033553 IBD from UniProtKB:Q96EB6
    PTN000872223: GO:0005654 IBD from UniProtKB:Q96EB6|FB:FBgn0024291
    PTN000872223: GO:0005637 IBD from UniProtKB:Q96EB6
```

## Interpretation

- Fly Sirt1 descends from PTN000872222 (Eukaryota, subfamily SF9 "NAD-DEPENDENT
  PROTEIN DEACETYLASE SIRTUIN-1") through speciation nodes only; it is the single
  fly member of the metazoan SIRT1 clade PTN000872223 and the 1:1 ortholog of
  human SIRT1 and worm sir-2.1.
- PTN000872222 carries GO:0003714, GO:0006974, GO:0031509, GO:0032041, GO:0046969 and
  GO:0046970. The GO:0031509 subtelomeric heterochromatin formation IBD is seeded
  only by the two yeasts (SGD:S000002200 SIR2, PomBase:SPBC16D10.07c sir2).
- PTN000872223 (Metazoa-Choanoflagellida) carries GO:0045892, GO:0033553,
  GO:0005654 and GO:0005637. GO:0033553 rDNA heterochromatin and GO:0005637 nuclear
  inner membrane are seeded only by human SIRT1 (UniProtKB:Q96EB6).
- No IKR/IRD loss annotation exists on the path to fly Sirt1.
