# ple: PAINT node placement on PTHR11473, and the alternatively spliced segment

## 1. PAINT node placement

`paint_node_placement.py` (stdlib Python; copied from
`genes/DROME/tim/tim-bioinformatics/` and extended with `--family-rows` and a
User-Agent header, because pantherdb.org returns HTTP 403 to urllib's default one)
downloads the PANTHER 19.0 tree for PTHR11473 and the pinned PAINT node GAF (`IBD.gaf`,
snapshot 19.0/2026-08-28) and prints the root-to-leaf path with every PAINT row on it.

Command (run 2026-11-17):

```
python paint_node_placement.py PTHR11473 FlyBase:FBgn0005626 WormBase:WBGene00000296 \
    --family-rows --cache-dir <tmp>
```

Output (abridged):

```
## Path to ple FlyBase:FBgn0005626 (Drosophila melanogaster)
PTN008322491  SPECIATION  LUCA  (PTHR11473 root)
    PAINT: GO:0004497 IBD from ... (PAH, TH and TPH seeds)
  PTN000158464 Eukaryota > PTN000158465 Unikonts > PTN000895525 Opisthokonts
  > PTN000895526 Metazoa-Choanoflagellida > PTN000895527 Eumetazoa
            PTN000158466  DUPLICATION   (TH / PAH / TPH split)
              PTN000158532  SPECIATION  Bilateria  subfamily=PTHR11473:SF15  (TH clade: TH, Th, cat-2, ple; 41 leaves)
                  PAINT: GO:0004511 IBD from WB:WBGene00000296|ZFIN:ZDB-GENE-990621-5|UniProtKB:P07101|RGD:3853|FB:FBgn0005626
                  PAINT: GO:0050890 IBD from MGI:MGI:98735|WB:WBGene00000296|RGD:3853
                  PAINT: GO:0001963 IBD from MGI:MGI:98735
                  PAINT: GO:0007617 IBD from FB:FBgn0005626|WB:WBGene00000296|MGI:MGI:98735
                  PAINT: GO:0030424 IBD from MGI:MGI:98735|WB:WBGene00000296|RGD:3853
                  PAINT: GO:0043204 IBD from RGD:3853|MGI:MGI:98735
                  PAINT: GO:0005737 IBD from UniProtKB:P07101|MGI:MGI:98735|RGD:3853
                PTN002607627  SPECIATION  Protostomia
                  PTN000158597  SPECIATION  Ecdysozoa  (cat-2, ple; 7 leaves)
                      PAINT: GO:0006585 IBD from WB:WBGene00000296
                    PTN001690346 Hexapoda-Crustacea > PTN002607628 Endopterygota > PTN000158602 Diptera
                          PTN000158603  Drosophila melanogaster  gene=ple

Other rows in the family that matter here:
  PTN001690342 [Deuterostomia, TH and Th]: GO:0006585 IBD from RGD:3853|MGI:MGI:98735
  PTN000158559 [Teleostei, 2 leaves]: NOT GO:0004511 IRD
```

MGI:MGI:98735 is mouse Th (P24529) and RGD:3853 is rat Th.

### Interpretation

- ple sits in the bilaterian TH clade PTN000158532, below the eumetazoan duplication
  that separates TH from PAH and TPH. The only loss in the clade is a teleost TH2 node;
  nothing below PTN000158532 on the insect path carries a loss.
- GO:0006585 was placed twice, at the Ecdysozoa node (seed: worm cat-2) and at the
  Deuterostomia node (seeds: mouse and rat Th), not at the Bilateria node. ple inherits
  it from the Ecdysozoa node.
- The four non-duplicative IBA terms on ple (GO:0001963, GO:0006585, GO:0043204,
  GO:0050890) are all placed on nodes whose descendants are TH orthologs only, so none
  is a paralog over-propagation; the question for each is whether the term describes
  what the enzyme does, which is judged in the review.

## 2. The alternatively spliced segment (residues 60-130)

`isoform_insert.py` reads `../ple-uniprot.txt` and reports the two UniProt isoforms and
the segment that distinguishes them.

Command: `python isoform_insert.py`

Output:

```
displayed isoform: 579 aa, 65996 Da
VSP_000545 isoform (lacks 60-130): 508 aa, 57862 Da
segment 60-130: 71 aa: NDDSLEDCIVQAQEHIPSEQDVELQDEHANLENLPLEEYVPVEEDVEFESVEQEQSESQSQEPEGNQQPTK
segment D+E = 23 (32%), K+R = 1
rest of protein D+E fraction = 14%
```

### Interpretation

- The segment is the 71-residue acidic insertion in the regulatory domain that Birman et
  al. 1994 (PMID:7929381) and Vie et al. 1999 (PMID:10358021) describe as specific to
  DTH type II, the hypodermal (epidermal) isoform. DTH type I, the CNS isoform, lacks it
  and corresponds to the 1989 cDNA (PMID:2483109), whose predicted 57,861 Da matches the
  57,862 Da computed here for the 508-residue isoform.
- UniProt P18459 names the displayed 579-residue sequence (with the insertion)
  "Neuronal" and VSP_000545 (without it) "Hypodermal", the reverse of the published
  assignment.
