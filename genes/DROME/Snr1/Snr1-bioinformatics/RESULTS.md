# Snr1: PAINT node placement on the PANTHER PTHR10019 tree

## Method

`paint_node_placement.py` (stdlib Python, this folder; copied from
`genes/DROME/tim/tim-bioinformatics/`, with a User-Agent header added because
pantherdb.org returns HTTP 403 to the default Python-urllib agent) downloads the
PANTHER 19.0 tree for PTHR10019
(`pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR10019`) and the pinned
PAINT node-level GAF (`IBD.gaf`, snapshot 19.0/2026-08-28), then prints the
root-to-leaf path for fly Snr1 (FlyBase:FBgn0011715) and human SMARCB1
(HGNC:11103), with every PAINT IBD/IKR/IRD row on a node of the path, and the
leaves under the Protostomia node.

Command (run 2026-11-17):

```
python paint_node_placement.py PTHR10019 FlyBase:FBgn0011715 HGNC:11103 \
    --leaves PTN002558537
```

## Output (fly path and protostome leaves)

```
## Path to Snr1 FlyBase:FBgn0011715 (Drosophila melanogaster)
PTN008936265  event=-  taxon=-  subfamily=-  gene=-
  PTN004120562  event=DUPLICATION  taxon=-  subfamily=-  gene=-
      PAINT: GO:0006338 IBD from PomBase:SPCC16A11.14|UniProtKB:Q12824|SGD:S000004313
      PAINT: GO:0003712 IBD from UniProtKB:Q12824
      PAINT: GO:0005634 IBD from PomBase:SPCC16A11.14|AGI_LocusCode:AT3G17590|SGD:S000004313|UniProtKB:Q12824|PomBase:SPAC2F7.08c|FB:FBgn0011715|MGI:MGI:1328366|CGD:CAL0000186865
      PAINT: GO:0006357 IBD from UniProtKB:Q12824|CGD:CAL0000195495|FB:FBgn0011715
    PTN000001217  event=SPECIATION  taxon=Eukaryota  subfamily=PTHR10019:SF5  gene=-
      PTN000001218  event=SPECIATION  taxon=Unikonts  subfamily=-  gene=-
        PTN000001219  event=SPECIATION  taxon=Opisthokonts  subfamily=-  gene=-
          PTN000001220  event=SPECIATION  taxon=Bilateria  subfamily=-  gene=-
              PAINT: GO:0071564 IBD from MGI:MGI:1328366
              PAINT: GO:0035060 IBD from FB:FBgn0011715
              PAINT: GO:0071565 IBD from MGI:MGI:1328366
              PAINT: GO:0003713 IBD from UniProtKB:Q12824
            PTN002558537  event=SPECIATION  taxon=Protostomia  subfamily=-  gene=-
              PTN000001254  event=SPECIATION  taxon=Ecdysozoa  subfamily=-  gene=-
                PTN000797504  event=SPECIATION  taxon=Arthropoda  subfamily=-  gene=-
                  PTN002558538  event=SPECIATION  taxon=Endopterygota  subfamily=-  gene=-
                    PTN000001258  event=SPECIATION  taxon=Diptera  subfamily=-  gene=-
                      PTN000001259  event=-  taxon=Drosophila melanogaster  subfamily=-  gene=Snr1

## Leaves under PTN002558537  event=SPECIATION  taxon=Protostomia  subfamily=-  gene=-
  Caenorhabditis elegans	snfc-5	WormBase:WBGene00011111
  Caenorhabditis briggsae	snfc-5	Gene_ORFName:CBG18075
  Pristionchus pacificus	WBGene00205972	EnsemblGenome:WBGene00205972
  Drosophila melanogaster	Snr1	FlyBase:FBgn0011715
  Anopheles gambiae	1282012	EnsemblGenome:AGAP001154
  Tribolium castaneum	AUGUSTUS-3.0.2_15634	EnsemblGenome:TC015634
  Ixodes scapularis	IscW_ISCW008377	EnsemblGenome:ISCW008377
  helobdella robusta	20210210	EnsemblGenome:HelroG185604
  PAINT rows on nodes at or below PTN002558537:
```

The human SMARCB1 path runs through the same PTN000001220 node and then the
Deuterostomia node PTN000001221.

## Reading

- The four IBDs behind Snr1's non-duplicative and brahma-complex IBA rows sit on
  PTN000001220, a speciation node at Bilateria, above the split into Protostomia
  (fly, worm, mosquito, beetle, tick, leech) and Deuterostomia (vertebrates).
- GO:0071564 npBAF complex and GO:0071565 nBAF complex were placed on this node
  from a single seed, mouse Smarcb1 (MGI:MGI:1328366). No protostome gene seeds them.
  The node therefore asserts that the neural-progenitor and neuron-specific BAF
  assemblies existed in the bilaterian ancestor. Each protostome in the tree has a
  single SMARCB1-family gene, and PAINT has recorded no loss (IKR/IRD) anywhere below
  PTN002558537.
- GO:0003713 transcription coactivator activity sits on the same node, seeded by
  human SMARCB1 (UniProtKB:Q12824). GO:0035060 brahma complex is seeded by fly Snr1
  itself.
- The family root PTN004120562 carries the broad nuclear, chromatin-remodeling,
  RNA polymerase II regulation and transcription-coregulator (GO:0003712) IBDs, all
  with fly Snr1 or yeast/plant/human experimental seeds.

The script reports only what is in the PANTHER tree and the PAINT GAF; whether the
fly gene inherits the function is argued in the review from these facts and the
literature.
