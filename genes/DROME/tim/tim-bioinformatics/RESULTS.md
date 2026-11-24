# tim: PAINT node placement on the PANTHER PTHR22940 tree

## Method

`paint_node_placement.py` (stdlib Python, this folder) downloads the PANTHER 19.0
tree for PTHR22940 (`pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR22940`)
and the pinned PAINT node-level GAF (`IBD.gaf`, snapshot 19.0/2026-08-28, the same
file `ai_gene_review.etl.panther_families` pins), then prints the root-to-leaf path
for fly tim (FlyBase:FBgn0014396), fly timeout (FlyBase:FBgn0038118) and human
TIMELESS (HGNC:11813), with every PAINT IBD/IKR/IRD row that sits on a node of
the path, and the leaves under the two Bilateria clades below the duplication.

Command (run 2026-11-16):

```
python paint_node_placement.py PTHR22940 FlyBase:FBgn0014396 FlyBase:FBgn0038118 HGNC:11813 \
    --leaves PTN008585096 PTN000533822
```

## Output

```
# PTHR22940: tree root PTN000533813 (Eukaryota)
# IBD.gaf: https://data.pantherdb.org/ftp/downloads/paint/19.0/2026-08-28/IBD.gaf

## Path to tim FlyBase:FBgn0014396 (Drosophila melanogaster)
PTN000533813  event=SPECIATION  taxon=Eukaryota  subfamily=PTHR22940:SF4  gene=-
    PAINT: GO:0000076 IBD from SGD:S000005217
    PAINT: GO:0006281 IBD from SGD:S000005217
    PAINT: GO:0043111 IBD from SGD:S000005217|PomBase:SPBC216.06c
    PAINT: GO:0003677 IBD from PomBase:SPBC216.06c
    PAINT: GO:0031298 IBD from PomBase:SPBC216.06c|SGD:S000005217|UniProtKB:Q9UNS1
  PTN000533814  event=SPECIATION  taxon=Unikonts  subfamily=-  gene=-
    PTN000533815  event=SPECIATION  taxon=Opisthokonts  subfamily=-  gene=-
      PTN001118052  event=SPECIATION  taxon=Metazoa-Choanoflagellida  subfamily=-  gene=-
        PTN001118053  event=SPECIATION  taxon=Eumetazoa  subfamily=-  gene=-
          PTN008585095  event=DUPLICATION  taxon=-  subfamily=-  gene=-
            PTN008585096  event=SPECIATION  taxon=Bilateria  subfamily=PTHR22940:SF5  gene=-
              PTN001118055  event=SPECIATION  taxon=Arthropoda  subfamily=-  gene=-
                  PAINT: GO:0009649 IBD from FB:FBgn0014396
                PTN001118056  event=SPECIATION  taxon=Hexapoda-Crustacea  subfamily=-  gene=-
                  PTN002741604  event=SPECIATION  taxon=Endopterygota  subfamily=-  gene=-
                    PTN000533819  event=SPECIATION  taxon=Diptera  subfamily=-  gene=-
                      PTN000533820  event=-  taxon=Drosophila melanogaster  subfamily=-  gene=tim

## Path to TIMELESS HGNC:11813 (Homo sapiens)
PTN000533813  event=SPECIATION  taxon=Eukaryota  subfamily=PTHR22940:SF4  gene=-
    PAINT: GO:0000076 IBD from SGD:S000005217
    PAINT: GO:0006281 IBD from SGD:S000005217
    PAINT: GO:0043111 IBD from SGD:S000005217|PomBase:SPBC216.06c
    PAINT: GO:0003677 IBD from PomBase:SPBC216.06c
    PAINT: GO:0031298 IBD from PomBase:SPBC216.06c|SGD:S000005217|UniProtKB:Q9UNS1
  PTN000533814  event=SPECIATION  taxon=Unikonts  subfamily=-  gene=-
    PTN000533815  event=SPECIATION  taxon=Opisthokonts  subfamily=-  gene=-
      PTN001118052  event=SPECIATION  taxon=Metazoa-Choanoflagellida  subfamily=-  gene=-
        PTN001118053  event=SPECIATION  taxon=Eumetazoa  subfamily=-  gene=-
          PTN008585095  event=DUPLICATION  taxon=-  subfamily=-  gene=-
            PTN000533822  event=SPECIATION  taxon=Bilateria  subfamily=-  gene=-
              PTN000533823  event=SPECIATION  taxon=Deuterostomia  subfamily=-  gene=-
                PTN009056591  event=SPECIATION  taxon=Chordata  subfamily=-  gene=-
                  PTN008376403  event=SPECIATION  taxon=Craniata-Tunicata  subfamily=-  gene=-
                    PTN002741594  event=SPECIATION  taxon=Euteleostomi  subfamily=-  gene=-
                      PTN008585098  event=SPECIATION  taxon=Tetrapoda  subfamily=-  gene=-
                        PTN001488586  event=SPECIATION  taxon=Amniota  subfamily=-  gene=-
                          PTN000533827  event=SPECIATION  taxon=Mammalia  subfamily=-  gene=-
                            PTN000533828  event=SPECIATION  taxon=Eutheria  subfamily=-  gene=-
                              PTN000533829  event=SPECIATION  taxon=Euarchontoglires  subfamily=-  gene=-
                                PTN000533830  event=SPECIATION  taxon=Catarrhini  subfamily=-  gene=-
                                  PTN002741595  event=SPECIATION  taxon=Homininae  subfamily=-  gene=-
                                    PTN000533831  event=SPECIATION  taxon=Homo-Pan  subfamily=-  gene=-
                                      PTN002505793  event=-  taxon=Homo sapiens  subfamily=-  gene=TIMELESS

## Path to timeout FlyBase:FBgn0038118 (Drosophila melanogaster)
PTN000533813  event=SPECIATION  taxon=Eukaryota  subfamily=PTHR22940:SF4  gene=-
    PAINT: GO:0000076 IBD from SGD:S000005217
    PAINT: GO:0006281 IBD from SGD:S000005217
    PAINT: GO:0043111 IBD from SGD:S000005217|PomBase:SPBC216.06c
    PAINT: GO:0003677 IBD from PomBase:SPBC216.06c
    PAINT: GO:0031298 IBD from PomBase:SPBC216.06c|SGD:S000005217|UniProtKB:Q9UNS1
  PTN000533814  event=SPECIATION  taxon=Unikonts  subfamily=-  gene=-
    PTN000533815  event=SPECIATION  taxon=Opisthokonts  subfamily=-  gene=-
      PTN001118052  event=SPECIATION  taxon=Metazoa-Choanoflagellida  subfamily=-  gene=-
        PTN001118053  event=SPECIATION  taxon=Eumetazoa  subfamily=-  gene=-
          PTN008585095  event=DUPLICATION  taxon=-  subfamily=-  gene=-
            PTN000533822  event=SPECIATION  taxon=Bilateria  subfamily=-  gene=-
              PTN008585101  event=SPECIATION  taxon=Ecdysozoa  subfamily=-  gene=-
                PTN001488598  event=SPECIATION  taxon=Hexapoda-Crustacea  subfamily=-  gene=-
                    PAINT: GO:0009649 IBD from FB:FBgn0038118
                  PTN002741606  event=SPECIATION  taxon=Endopterygota  subfamily=-  gene=-
                    PTN000533851  event=SPECIATION  taxon=Diptera  subfamily=-  gene=-
                      PTN000533852  event=-  taxon=Drosophila melanogaster  subfamily=-  gene=timeout

## Leaves under PTN008585096  event=SPECIATION  taxon=Bilateria  subfamily=PTHR22940:SF5  gene=-
  Strongylocentrotus purpuratus	None	EnsemblGenome:LOC587080
  Drosophila melanogaster	tim	FlyBase:FBgn0014396
  Anopheles gambiae	None	EnsemblGenome:AGAP008288
  Tribolium castaneum	AUGUSTUS-3.0.2_13997	EnsemblGenome:TC013997
  Daphnia pulex	DAPPUDRAFT_103010	EnsemblGenome:DAPPUDRAFT_103010
  Daphnia pulex	DAPPUDRAFT_235857	EnsemblGenome:DAPPUDRAFT_235857
  Daphnia pulex	DAPPUDRAFT_313767	EnsemblGenome:DAPPUDRAFT_313767
  Daphnia pulex	DAPPUDRAFT_308128	EnsemblGenome:DAPPUDRAFT_308128
  Daphnia pulex	DAPPUDRAFT_97364	EnsemblGenome:DAPPUDRAFT_97364
  Daphnia pulex	DAPPUDRAFT_309208	EnsemblGenome:DAPPUDRAFT_309208
  Daphnia pulex	DAPPUDRAFT_236054	EnsemblGenome:DAPPUDRAFT_236054
  Daphnia pulex	DAPPUDRAFT_243157	EnsemblGenome:DAPPUDRAFT_243157
  Daphnia pulex	DAPPUDRAFT_318263	EnsemblGenome:DAPPUDRAFT_318263
  Ixodes scapularis	IscW_ISCW007376	EnsemblGenome:ISCW007376
  PAINT rows on nodes at or below PTN008585096:
    PTN001118055: GO:0009649 IBD from FB:FBgn0014396

## Leaves under PTN000533822  event=SPECIATION  taxon=Bilateria  subfamily=-  gene=-
  Homo sapiens	TIMELESS	HGNC:11813
  Pan troglodytes	TIMELESS	Ensembl:ENSPTRG00000022963.4
  Gorilla gorilla gorilla	TIMELESS	Ensembl:ENSGGOG00000016556.3
  Macaca mulatta	TIMELESS	Ensembl:ENSMMUG00000021878.4
  Mus musculus	Timeless	MGI:MGI=1321393
  Rattus norvegicus	Timeless	RGD:620939
  Bos taurus	TIMELESS	Ensembl:ENSBTAG00000020459.5
  Sus scrofa	TIMELESS	Ensembl:ENSSSCG00000000399.5
  Equus caballus	TIMELESS	Ensembl:ENSECAG00000002892.4
  Felis catus	TIMELESS	Ensembl:ENSFCAG00000012024.6
  Canis lupus familiaris	TIMELESS	Ensembl:ENSCAFG00845008229.1
  Ornithorhynchus anatinus	TIMELESS	Ensembl:ENSOANG00000012531.4
  Gallus gallus	TIMELESS	Ensembl:ENSGALG00010024989.1
  Anolis carolinensis	TIMELESS	Ensembl:ENSACAG00000016465.4
  Xenopus laevis	timeless.S	Gene:timeless.S
  Xenopus laevis	timeless.L	Gene:timeless.L
  Xenopus tropicalis	timeless	Xenbase:XB-GENE-985242
  Oryzias latipes	timeless	Ensembl:ENSORLG00000015066.2
  Danio rerio	Tim	ZFIN:ZDB-GENE-030131-8978
  lepisosteus oculatus	None	Ensembl:ENSLOCG00000004180.1
  Ciona intestinalis	None	Ensembl:ENSCING00000002042.3
  Branchiostoma floridae	LOC118403034	Gene:LOC118403034
  Strongylocentrotus purpuratus	None	EnsemblGenome:LOC579123
  Caenorhabditis elegans	tim-1	WormBase:WBGene00006571
  Caenorhabditis briggsae	tim-1	Gene_ORFName:CBG03593
  Pristionchus pacificus	WBGene00114688	EnsemblGenome:WBGene00114688
  Drosophila melanogaster	timeout	FlyBase:FBgn0038118
  Anopheles gambiae	None	EnsemblGenome:AGAP010787
  Tribolium castaneum	tim2	EnsemblGenome:TC000593
  Daphnia pulex	DAPPUDRAFT_382	EnsemblGenome:DAPPUDRAFT_382
  PAINT rows on nodes at or below PTN000533822:
    PTN001488598: GO:0009649 IBD from FB:FBgn0038118
```

## Interpretation

- All five replication-related IBDs (GO:0000076 DNA replication checkpoint signaling,
  GO:0003677 DNA binding, GO:0006281 DNA repair, GO:0031298 replication fork
  protection complex, GO:0043111 replication fork arrest) sit on the family root
  PTN000533813 (Eukaryota). Their seeds are yeast Tof1 (SGD:S000005217), fission
  yeast Swi1 (PomBase:SPBC216.06c) and human TIMELESS (UniProtKB:Q9UNS1).
- Below the Eumetazoa node the tree has a duplication, PTN008585096 / PTN000533822.
  PTN000533822 (Bilateria) holds the TIMELESS-homolog clade: human, mouse and
  zebrafish TIMELESS, C. elegans tim-1 and fly timeout. PTN008585096 (Bilateria,
  subfamily SF5 "PROTEIN TIMELESS") holds fly tim, mosquito, beetle, Daphnia, tick
  and sea urchin sequences.
- Fly tim therefore inherits the root IBDs only through the ancestor of both
  paralogs. PAINT has recorded no IKR/IRD loss anywhere in the SF5 clade; the only
  PAINT row inside that clade is GO:0009649 entrainment of circadian clock at
  PTN001118055 (Arthropoda), seeded by fly tim itself.
- The tree does not show which paralog kept the ancestral replication role. That
  comes from the literature on the two fly genes and on clock gene loss (see the
  review): timeout is essential for chromosome integrity, tim null flies are viable,
  and several lineages (mammals, honey bee) have lost the tim1-type gene while
  keeping the timeout-type one.
