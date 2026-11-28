# Adar: PAINT node placement on the PANTHER PTHR10910 tree

## Method

`paint_node_placement.py` (stdlib Python, this folder; copied from
`genes/DROME/tim/tim-bioinformatics/` and extended with `--family-rows` and a
User-Agent header, because pantherdb.org returns HTTP 403 to urllib's default one)
downloads the PANTHER 19.0 tree for PTHR10910
(`pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR10910`) and the pinned PAINT
node-level GAF (`IBD.gaf`, snapshot 19.0/2026-08-28). It prints the root-to-leaf path for
the named genes with every PAINT IBD/IKR/IRD row on the path, the leaves under named
nodes, and (with `--family-rows`) every PAINT row on any node of the family tree.

Command (run 2026-11-17):

```
python paint_node_placement.py PTHR10910 FlyBase:FBgn0026086 FlyBase:FBgn0028658 HGNC:226 \
    --leaves PTN007471810 PTN007471815 --family-rows --cache-dir <tmp>
```

The UniProt PANTHER cross-references quoted below were read from the UniProt REST
flat files of Q9V3R6 (fly Adat1), Q9BUB4 (human ADAT1), F4HU58 (Arabidopsis TAD1) and
Q9NII1 (fly Adar) on the same day.

## Output (abridged)

```
# PTHR10910: tree root PTN000098822 (Eukaryota)

## Path to Adar FlyBase:FBgn0026086 (Drosophila melanogaster)
PTN000098822  event=SPECIATION  taxon=Eukaryota  subfamily=PTHR10910:SF62
    PAINT: GO:0006382 IBD from WB:WBGene00000079|MGI:MGI:1889575|MGI:MGI:891999|RGD:2033|UniProtKB:P78563|UniProtKB:P55265|WB:WBGene00000080|FB:FBgn0026086
    PAINT: GO:0005730 IBD from UniProtKB:P78563|MGI:MGI:1889575|FB:FBgn0026086|UniProtKB:P55265
    PAINT: GO:0005737 IBD from WB:WBGene00000080|MGI:MGI:1923023|UniProtKB:P55265|MGI:MGI:1889575|WB:WBGene00000079
    PAINT: GO:0003726 IBD from MGI:MGI:891999|RGD:2033|MGI:MGI:1889575|UniProtKB:P78563|FB:FBgn0026086|UniProtKB:P55265|WB:WBGene00000080
    PAINT: GO:0003725 IBD from RGD:2033|UniProtKB:P78563
    PAINT: GO:0006396 IBD from MGI:MGI:1889575|AGI_LocusCode:AT1G01760|MGI:MGI:891999|UniProtKB:P55265|FB:FBgn0028658|UniProtKB:P78563
    PAINT: GO:0008251 IBD from AGI_LocusCode:AT1G01760|FB:FBgn0028658
  PTN000098823  SPECIATION  Unikonts
    PTN000098824  SPECIATION  Opisthokonts
      PTN000098649  DUPLICATION                      (ADAR1 clade vs ADAR2 clade)
        PTN000857167  SPECIATION  Eumetazoa          (ADAR2 clade: ADARB1, ADARB2, adr-1, adr-2, Adar)
          PTN000098826  SPECIATION  Bilateria
            PTN002588860  SPECIATION  Protostomia
              PTN002249517  SPECIATION  Ecdysozoa
                PTN000857100  SPECIATION  Arthropoda
                  PTN000857101  SPECIATION  Hexapoda-Crustacea
                    PTN002588861  SPECIATION  Endopterygota
                      PTN000098948  SPECIATION  Diptera
                        PTN007471810  DUPLICATION
                          PTN000098949  Drosophila melanogaster  gene=Adar

## Path to Adat1 FlyBase:FBgn0028658: identical down to PTN007471810, then
                          PTN000099140  Drosophila melanogaster  gene=Adat1

## Leaves under PTN007471810 (DUPLICATION)
  Drosophila melanogaster  Adat1    FlyBase:FBgn0028658
  Drosophila melanogaster  cg12493  FlyBase:FBgn0035571
  Drosophila melanogaster  Adar     FlyBase:FBgn0026086

## All PAINT rows on nodes of the family tree
  PTN000098822 [Eukaryota root, 189 leaves]: the seven IBDs above
  PTN000099132 [leaf, C. elegans adr-1]: NOT GO:0008251 IKR; NOT GO:0003725 IKR; NOT GO:0003726 IKR
  PTN001331203 [leaf, fly cg12493]: NOT GO:0003726, GO:0003725, GO:0008251, GO:0006382 IRD; NOT GO:0006396 IKR
  PTN004208710 [leaf, Tribolium AUGUSTUS-3.0.2_15220]: NOT GO:0008251, GO:0006382, GO:0003726, GO:0003725 IRD
```

The top of the tree (from the same JSON) splits the root into Unikonts (139 leaves:
the metazoan ADAR1 clade PTN002475003 with ADAR, ADAD1, ADAD2; the ADAR2 clade
PTN000857167 with ADARB1, ADARB2, worm adr-1 and adr-2, fly Adar, Adat1 and cg12493;
three fungal and two amoebozoan leaves) and Bikonts (PTN007471815, 50 leaves, almost all
plant TAD1 orthologs, Arabidopsis TAD1 among them). No vertebrate ADAT1 is a member of
PTHR10910.

UniProt PANTHER cross-references (InterPro HMM assignments):

| Protein | UniProt | PANTHER family in UniProt |
|---|---|---|
| fly Adar | Q9NII1 | PTHR10910:SF62 |
| Arabidopsis TAD1 | F4HU58 | PTHR10910:SF62 |
| fly Adat1 | Q9V3R6 | PTHR46516:SF1 (TRNA-SPECIFIC ADENOSINE DEAMINASE 1) |
| human ADAT1 | Q9BUB4 | PTHR46516:SF1 (TRNA-SPECIFIC ADENOSINE DEAMINASE 1) |
| fly cg12493 | Q9VZ88 | PTHR46205:SF5 (BLANKS-RELATED; LOQUACIOUS family) |

## Interpretation

- All seven Adar IBA rows come from one node, the eukaryotic root PTN000098822. Losses
  were recorded only on three single leaves (worm adr-1, fly cg12493, a Tribolium gene),
  never on a clade.
- **GO:0008251 tRNA-specific adenosine deaminase activity** rests on two seeds, both
  ADAT1-type tRNA A37 deaminases: Arabidopsis TAD1 (the Bikont clade) and fly Adat1. The
  PANTHER 19 tree places fly Adat1 as a Drosophila-specific duplicate of Adar inside the
  ADAR2 clade, while InterPro's own HMM assignment puts it in PTHR46516 with human ADAT1.
  With the IBD at the root and no loss on the ADAR1 or ADAR2 clades, every animal ADAR
  (human ADAR and ADARB1, worm adr-2, fly Adar) inherits a tRNA deaminase activity that
  no ADAR has been shown to have. A placement that only covered Arabidopsis TAD1 and
  fly Adat1 would need either the IBD on the Bikont node plus the Adat1 leaf, or an IRD
  on the ADAR clades once Adat1 is moved out of them.
- **GO:0005737 cytoplasm** is seeded by ADAR1-clade proteins (human and mouse ADAR,
  mouse Adad2) and by worm adr-1 and adr-2; human ADARB1, the closest vertebrate
  relative of fly Adar, is not a seed. The ADAR2-clade seeds and fly Adar itself are the
  seeds of the nucleolus IBD on the same node.
- **GO:0003725 double-stranded RNA binding** is seeded by human and rat ADARB1, the
  orthologs of fly Adar in the ADAR2 clade, and fly Adar has two dsRBDs.
- cg12493 (a Loquacious-family dsRBD protein by InterPro) and fly Adat1 are both nested
  in the ADAR2 clade in this tree, which looks like a tree-construction artefact; this
  analysis does not test it further.

Inputs were downloaded to a temporary cache and are not retained.
