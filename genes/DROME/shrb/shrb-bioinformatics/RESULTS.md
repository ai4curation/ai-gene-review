# shrb: PAINT node placement on the PANTHER PTHR22761 tree

## Method

`paint_node_placement.py` (stdlib Python, this folder; copied from
`genes/DROME/tim/tim-bioinformatics/`, with a User-Agent header added because
pantherdb.org returns HTTP 403 to the default Python-urllib agent) downloads the
PANTHER 19.0 tree for PTHR22761
(`pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR22761`) and the pinned
PAINT node-level GAF (`IBD.gaf`, snapshot 19.0/2026-08-28), then prints the
root-to-leaf path for fly shrb (FlyBase:FBgn0086656), human CHMP4B (HGNC:16171)
and human CHMP7 (HGNC:28439), with every PAINT IBD/IKR/IRD row on a node of the
path, and the leaves under PTN008581269, the only node in the family that carries
loss (IRD) annotations.

Command (run 2026-11-17):

```
python paint_node_placement.py PTHR22761 FlyBase:FBgn0086656 HGNC:16171 HGNC:28439 \
    --leaves PTN008581269
```

## Output (fly path and the loss node)

```
## Path to shrb FlyBase:FBgn0086656 (Drosophila melanogaster)
PTN000509386  event=DUPLICATION  taxon=-  subfamily=-  gene=-
    PAINT: GO:0005635 IBD from UniProtKB:Q8WUX9|UniProtKB:Q96FZ7|SGD:S000003585|JaponicusDB:SJAG_01242|UniProtKB:Q9H444|PomBase:SPBC1604.18c|UniProtKB:Q9NZZ3|UniProtKB:Q9BY43|PomBase:SPAC1142.07c|UniProtKB:Q96CF2|JaponicusDB:SJAG_05207|SGD:S000004015
    PAINT: GO:0006900 IBD from SGD:S000004682|AGI_LocusCode:AT5G09260|UniProtKB:Q9BY43|SGD:S000004015|AGI_LocusCode:AT4G29160
    PAINT: GO:0031468 IBD from UniProtKB:Q96CF2|PomBase:SPBC1604.18c|JaponicusDB:SJAG_01242|UniProtKB:Q9H444|UniProtKB:Q9NZZ3|UniProtKB:Q9BY43|JaponicusDB:SJAG_05207|UniProtKB:Q96FZ7|UniProtKB:Q8WUX9
    PAINT: GO:0032511 IBD from PomBase:SPAC1142.07c|PomBase:SPBC215.14c|SGD:S000002894
    PAINT: GO:0005771 IBD from FB:FBgn0086656|AGI_LocusCode:AT3G10640|UniProtKB:Q8WUX9|UniProtKB:Q96FZ7|UniProtKB:Q9H444|UniProtKB:Q9BY43|UniProtKB:Q9NZZ3|UniProtKB:Q96CF2
    PAINT: GO:0000815 IBD from UniProtKB:Q9H444|SGD:S000004015|UniProtKB:Q9BY43|SGD:S000004682|UniProtKB:Q8WUX9|CGD:CAL0000187201|UniProtKB:Q96FZ7
  PTN000509454  event=SPECIATION  taxon=Eukaryota  subfamily=PTHR22761:SF10  gene=-
      PAINT: GO:0009898 IBD from UniProtKB:Q9H444|UniProtKB:Q9BY43
    PTN009052131  event=DUPLICATION  taxon=-  subfamily=-  gene=-
      PTN000509455  event=SPECIATION  taxon=Unikonts  subfamily=-  gene=-
        PTN000509456  event=SPECIATION  taxon=Opisthokonts  subfamily=-  gene=-
          PTN008581213  event=DUPLICATION  taxon=-  subfamily=-  gene=-
            PTN001101736  event=SPECIATION  taxon=Eumetazoa  subfamily=-  gene=-
              PTN000509493  event=SPECIATION  taxon=Bilateria  subfamily=-  gene=-
                PTN002734056  event=SPECIATION  taxon=Protostomia  subfamily=-  gene=-
                  PTN000509567  event=SPECIATION  taxon=Ecdysozoa  subfamily=-  gene=-
                    PTN001101751  event=SPECIATION  taxon=Arthropoda  subfamily=-  gene=-
                      PTN001101752  event=SPECIATION  taxon=Hexapoda-Crustacea  subfamily=-  gene=-
                        PTN002734057  event=SPECIATION  taxon=Endopterygota  subfamily=-  gene=-
                          PTN000509577  event=SPECIATION  taxon=Diptera  subfamily=-  gene=-
                            PTN000509580  event=-  taxon=Drosophila melanogaster  subfamily=-  gene=shrb

## Leaves under PTN008581269  event=SPECIATION  taxon=Unikonts  subfamily=PTHR22761:SF96  gene=-
  Drosophila melanogaster	BcDNA.GH08385	FlyBase:FBgn0027565
  Trichoplax adhaerens	TRIADDRAFT_58634	EnsemblGenome:TriadG58634
  Saccharomyces cerevisiae	YJL049W	SGD:S000003585
  Eremothecium gossypii	AGOS_AEL183C	EnsemblGenome:AGOS_AEL183C
  Schizosaccharomyces pombe	cmp7	PomBase:SPBC1604.18c
  Schizosaccharomyces japonicus	SJAG_05207	EnsemblGenome:SJAG_05207
  Cryptococcus neoformans	CNI02380	EnsemblGenome:CNI02380
  Puccinia graminis	PGTG_01186	EnsemblGenome:PGTG_01186
  Dictyostelium discoideum	chmp7	dictyBase:DDB_G0277133
  PAINT rows on nodes at or below PTN008581269:
    PTN008581269: NOT GO:0009898 IRD from PANTHER:PTN000509454
    PTN008581269: NOT GO:0032511 IRD from PANTHER:PTN000509386
    PTN008581269: GO:0007084 IBD from PomBase:SPBC1604.18c|JaponicusDB:SJAG_05207
    PTN008581269: NOT GO:0006900 IRD from PANTHER:PTN000509386
    PTN008581269: NOT GO:0005771 IRD from PANTHER:PTN000509386
```

The human CHMP4B path runs through the same nodes down to PTN000509493
(Bilateria) and then the Deuterostomia node PTN000509494.

## Reading

- The nuclear envelope (GO:0005635), nuclear membrane reassembly (GO:0031468) and
  vesicle budding from membrane (GO:0006900) IBDs sit on PTN000509386, the root of
  PTHR22761 (the Snf7/CHMP4-CHMP6-CHMP7 family). Their seeds include the CHMP4
  proteins themselves: human CHMP4A (Q9BY43), CHMP4B (Q9H444) and CHMP4C (Q96CF2)
  for the two nuclear-envelope terms, and CHMP4A and yeast Snf7 (SGD:S000004015) for
  vesicle budding.
- The cytoplasmic side of plasma membrane IBD (GO:0009898) sits on PTN000509454
  (Eukaryota, subfamily SF10), seeded by human CHMP4A and CHMP4B.
- Fly shrb descends from both nodes without passing through any loss node. Below
  PTN008581213 it is in the same Eumetazoa clade (PTN001101736) as human CHMP4B, so
  it is a direct CHMP4 ortholog, and the seeds for all four non-duplicative IBA terms
  include members of its own clade.
- The only losses in the family (IRD on PTN008581269) remove the MVB, vesicle
  budding, plasma membrane and late endosome-to-vacuole terms from a Unikont CHMP7
  clade (yeast Chm7, fission yeast Cmp7, Dictyostelium chmp7). That clade contains a
  fly gene, BcDNA.GH08385 (FBgn0027565, CG5498), so flies also have a CHMP7-type
  paralog, the protein that recruits CHMP4 to the reforming nuclear envelope in
  human and yeast cells. Fly shrb is not inside this clade.

The script reports only what is in the PANTHER tree and the PAINT GAF; whether the
fly gene inherits the function is argued in the review from these facts and the
literature.
