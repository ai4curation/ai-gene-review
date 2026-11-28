# Atg8a: PAINT node placement and sequence checks

## Methods

Two stdlib Python scripts in this folder, run 2026-11-17.

- `paint_node_placement.py` (copied unchanged from `genes/DROME/tim/tim-bioinformatics/`)
  reads the PANTHER 19.0 tree for PTHR10969
  (`pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR10969`) and the pinned PAINT
  node-level GAF (`IBD.gaf`, snapshot 19.0/2026-08-28). It prints the root-to-leaf path
  for fly Atg8a (FlyBase:FBgn0052672) with every PAINT IBD/IKR/IRD row on the path, and the
  leaves under two named nodes. The two downloads were made with `curl` into the cache
  directory first, because the PANTHER server refused Python's default user agent (HTTP 403);
  the script reads cached files when they exist.

  ```
  python paint_node_placement.py PTHR10969 FlyBase:FBgn0052672 \
      --leaves PTN000861087 PTN000861057 --cache-dir <cache>
  ```

- `atg8a_sequence_check.py` fetches UniProt sequences and, for each protein, reports the
  residue aligned to Atg8a Gly116, the residues aligned to Atg8a K48/Y49 (the LIR docking
  site mutated in PMID:35649355), the C-terminal residues, and percent identity to Atg8a from
  a simple global alignment (match 1, mismatch 0, gap -1).

  ```
  python atg8a_sequence_check.py Q9W2S2 Q9VEG5 O95166 P60520 Q9GZQ8 Q9H492
  ```

## Output: PAINT path to fly Atg8a

```
## Path to Atg8a FlyBase:FBgn0052672 (Drosophila melanogaster)
PTN000103522  event=SPECIATION  taxon=Eukaryota  subfamily=PTHR10969:SF4  gene=-
    PAINT: GO:0000423 IBD from UniProtKB:Q9GZQ8
    PAINT: GO:0097352 IBD from dictyBase:DDB_G0286191|UniProtKB:Q9BXW4|UniProtKB:Q9GZQ8|UniProtKB:Q9H492|dictyBase:DDB_G0290491
    PAINT: GO:0000045 IBD from UniProtKB:P60520|UniProtKB:Q9GZQ8|RGD:735183|UniProtKB:Q582K6|SGD:S000000174|UniProtKB:Q9H492
    PAINT: GO:0006995 IBD from dictyBase:DDB_G0286191
    PAINT: GO:0000421 IBD from UniProtKB:P60520|UniProtKB:Q9GZQ8|WB:WBGene00002981|UniProtKB:O95166|RGD:621315|dictyBase:DDB_G0286191|WB:WBGene00002980|RGD:735183|MGI:MGI:1915661|dictyBase:DDB_G0290491
    PAINT: GO:0008429 IBD from SGD:S000000174|UniProtKB:Q9BXW4|UniProtKB:O95166|UniProtKB:P60520|UniProtKB:Q9GZQ8
  PTN000103523  event=SPECIATION  taxon=Unikonts  subfamily=-  gene=-
    PTN000103524  event=SPECIATION  taxon=Opisthokonts  subfamily=-  gene=-
      PTN007473779  event=SPECIATION  taxon=Metazoa-Choanoflagellida  subfamily=-  gene=-
        PTN000103525  event=DUPLICATION  taxon=-  subfamily=-  gene=-
            PAINT: GO:0031625 IBD from UniProtKB:O95166|UniProtKB:Q9H0R8|UniProtKB:P60520|UniProtKB:Q9GZQ8|UniProtKB:Q9BXW4|UniProtKB:Q9H492
          PTN000861087  event=SPECIATION  taxon=Eumetazoa  subfamily=PTHR10969:SF33  gene=-
              PAINT: GO:0050811 IBD from RGD:61911|UniProtKB:O95166
            PTN000103619  event=SPECIATION  taxon=Bilateria  subfamily=-  gene=-
              PTN002590206  event=SPECIATION  taxon=Protostomia  subfamily=-  gene=-
                PTN000103716  event=SPECIATION  taxon=Ecdysozoa  subfamily=-  gene=-
                  PTN000861095  event=SPECIATION  taxon=Arthropoda  subfamily=-  gene=-
                    PTN002590207  event=SPECIATION  taxon=Endopterygota  subfamily=-  gene=-
                      PTN000103720  event=SPECIATION  taxon=Diptera  subfamily=-  gene=-
                        PTN000103721  event=DUPLICATION  taxon=-  subfamily=-  gene=-
                          PTN000103723  event=-  taxon=Drosophila melanogaster  subfamily=-  gene=Atg8a
```

## Output: leaves under the two Eumetazoa nodes below the duplication PTN000103525

Leaf lists filtered with grep to human, mouse, worm and fly leaves; PAINT rows unfiltered.

```
## Leaves under PTN000861087  event=SPECIATION  taxon=Eumetazoa  subfamily=PTHR10969:SF33  gene=-
  Homo sapiens	GABARAPL1	HGNC:4068
  Mus musculus	Gabarapl1	MGI:MGI=1914980
  Homo sapiens	GABARAPL3	HGNC:4069
  Homo sapiens	GABARAP	HGNC:4067
  Mus musculus	Gabarap	MGI:MGI=1861742
  Caenorhabditis elegans	lgg-1	WormBase:WBGene00002980
  Drosophila melanogaster	Atg8b	FlyBase:FBgn0038539
  Drosophila melanogaster	Atg8a	FlyBase:FBgn0052672
  PAINT rows on nodes at or below PTN000861087:
    PTN000861087: GO:0050811 IBD from RGD:61911|UniProtKB:O95166
## Leaves under PTN000861057  event=SPECIATION  taxon=Eumetazoa  subfamily=PTHR10969:SF37  gene=-
  Homo sapiens	MAP1LC3A	HGNC:6838
  Mus musculus	Map1lc3a	MGI:MGI=1915661
  Homo sapiens	MAP1LC3B2	HGNC:34390
  Homo sapiens	MAP1LC3B	HGNC:13352
  Mus musculus	Map1lc3b	MGI:MGI=1914693
  Caenorhabditis elegans	lgg-2	WormBase:WBGene00002981
  PAINT rows on nodes at or below PTN000861057:
    PTN000861057: GO:0008017 IBD from RGD:621315
```

## Output: sequence check

```
# reference Q9W2S2: >tr|Q9W2S2|Q9W2S2_DROME Autophagy-related 8a, isoform A OS=Drosophila melanogaster OX=7227 GN=Atg8a PE=1 SV=1
# reference residue 116 = G, residues after it = 'MAKIN', K48/Y49 = KY
accession	length	identity_to_ref	res_at_ref116	res_at_ref48_49	C-terminal 8 aa
Q9W2S2	121	100.0%	G	KY	VYGMAKIN
#   >tr|Q9W2S2|Q9W2S2_DROME Autophagy-related 8a, isoform A OS=Drosophila melanogaster OX=7227 GN=Atg8a PE=1 SV=1
Q9VEG5	120	79.3%	G	KY	DENVYGRQ
#   >tr|Q9VEG5|Q9VEG5_DROME Autophagy-related 8b, isoform A OS=Drosophila melanogaster OX=7227 GN=Atg8b PE=3 SV=1
O95166	117	88.4%	G	KY	SDESVYGL
#   >sp|O95166|GBRAP_HUMAN Gamma-aminobutyric acid receptor-associated protein OS=Homo sapiens OX=9606 GN=GABARAP PE=1 SV=1
P60520	117	55.4%	G	KY	SGENTFGF
#   >sp|P60520|GBRL2_HUMAN Gamma-aminobutyric acid receptor-associated protein-like 2 OS=Homo sapiens OX=9606 GN=GABARAPL2 PE=1 SV=1
Q9GZQ8	125	31.4%	G	KF	TFGMKLSV
#   >sp|Q9GZQ8|MLP3B_HUMAN Microtubule-associated protein 1 light chain 3 beta OS=Homo sapiens OX=9606 GN=MAP1LC3B PE=1 SV=3
Q9H492	121	30.6%	G	KF	ASQETFGF
#   >sp|Q9H492|MLP3A_HUMAN Microtubule-associated protein 1 light chain 3 alpha OS=Homo sapiens OX=9606 GN=MAP1LC3A PE=1 SV=2
```

## Interpretation

- Six IBDs sit at the family root PTN000103522 (Eukaryota): autophagosome assembly,
  autophagosome membrane, mitophagy, autophagosome maturation, cellular response to
  nitrogen starvation and phosphatidylethanolamine binding. The nitrogen-starvation IBD has a
  single seed, Dictyostelium atg8a (dictyBase:DDB_G0286191); the mitophagy IBD has a single
  seed, human MAP1LC3B (UniProtKB:Q9GZQ8).
- Ubiquitin protein ligase binding sits at PTN000103525, the duplication node that separates
  the metazoan GABARAP and LC3 clades, seeded only by human Atg8-family proteins.
- Below that duplication, PTN000861087 (Eumetazoa, subfamily SF33) is the GABARAP clade:
  human GABARAP, GABARAPL1 and GABARAPL3, mouse Gabarap and Gabarapl1, worm lgg-1 and fly
  Atg8a and Atg8b. GABA receptor binding is asserted at this node from rat and human GABARAP
  only. The sister node PTN000861057 (the LC3 clade: MAP1LC3A, MAP1LC3B, worm lgg-2) carries
  the microtubule-binding IBD, which fly Atg8a does not inherit.
- Fly Atg8a and Atg8b arose from a Diptera-level duplication (PTN000103721). No IKR or IRD
  (loss) row sits on the path to Atg8a, and the repository's family PAINT file
  (`interpro/panther/PTHR10969/PTHR10969-paint.tsv`) lists only non-negated IBD rows.
- Atg8a has Gly116 followed by five residues (MAKIN), the stretch Atg4 removes before PE
  conjugation, and K48/Y49 at the LIR docking site. It is 88% identical to human GABARAP and
  about 31% identical to LC3A/LC3B, so it is a GABARAP-subfamily protein by sequence as well as
  by tree position.
