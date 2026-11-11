# ftz-f1 (P33244) family placement and PAINT node check (2026-10-21)

Script: `family_placement.py` (run from the repo root). Inputs are the repo PANTHER
member table `interpro/panther/PTHR24086/PTHR24086-entries.csv` and
`PTHR24086-paint-slice.tsv`, the unmodified output of
`ai-gene-review fetch-panther-paint PTHR24086` (node-level IBD rows).

## Subfamily placement (script output)

```
P33244	ftz-f1	Drosophila melanogaster	PTHR24086:SF15	NUCLEAR HORMONE RECEPTOR FTZ-F1
P49867	FTZ-F1	Bombyx mori	PTHR24086:SF15	NUCLEAR HORMONE RECEPTOR FTZ-F1
Q19345	nhr-25	Caenorhabditis elegans	PTHR24086:SF15	NUCLEAR HORMONE RECEPTOR FTZ-F1
Q05192	Hr39	Drosophila melanogaster	PTHR24086:SF25	NUCLEAR HORMONE RECEPTOR FTZ-F1 BETA
Q13285	NR5A1	Homo sapiens	PTHR24086:SF24	STEROIDOGENIC FACTOR 1
O00482	NR5A2	Homo sapiens	PTHR24086:SF18	NUCLEAR RECEPTOR SUBFAMILY 5 GROUP A MEMBER 2
```

P33244 shares subfamily SF15 with Bombyx FTZ-F1 and C. elegans nhr-25. The mammalian
NR5A proteins (SF-1, LRH-1) are in separate subfamilies (SF24, SF18), and the fly paralog
Hr39 (whose UniProt name is "Nuclear hormone receptor FTZ-F1 beta", not to be confused with
the betaFTZ-F1 isoform of ftz-f1) is in SF25.

## PAINT node-level annotations (script output)

```
PTN000639680	GO:0090575	C	IBD	taxon=taxon:33213	seeds=MGI:MGI:1346833|MGI:MGI:1346834
PTN000639680	GO:0000978	F	IBD	taxon=taxon:33213	seeds=MGI:MGI:1346833|MGI:MGI:1346834
PTN000639680	GO:0006357	P	IBD	taxon=taxon:33213	seeds=FB:FBgn0001078|MGI:MGI:1346833|MGI:MGI:1346834|UniProtKB:O00482|UniProtKB:Q13285|WB:WBGene00003623|ZFIN:ZDB-GENE-010504-1
PTN000639680	GO:0009755	P	IBD	taxon=taxon:33213	seeds=FB:FBgn0001078|RGD:68350
PTN000639680	GO:0009888	P	IBD	taxon=taxon:33213	seeds=MGI:MGI:1346833|MGI:MGI:1346834|ZFIN:ZDB-GENE-990415-79
PTN002916752	GO:0005634	C	IBD	taxon=taxon:	seeds=WB:WBGene00003676|WB:WBGene00003854
PTN002916752	GO:0003700	F	IBD	taxon=taxon:	seeds=WB:WBGene00003854|WB:WBGene00008830
PTN002916752	GO:0006357	P	IBD	taxon=taxon:	seeds=WB:WBGene00003854|WB:WBGene00008830
```

Interpretation: all five IBA rows on P33244 come from PTN000639680, a node placed at
Bilateria (taxon:33213), i.e. the NR5A ancestor of the fly, worm and vertebrate proteins.
The node carries only generic NR5A properties: RNA polymerase II cis-regulatory DNA
binding, regulation of RNA polymerase II transcription, a transcription regulator
complex, hormone-mediated signaling and tissue development. Lineage-specific vertebrate
functions (steroidogenesis, sex determination, bile-acid or phospholipid regulation) are
not placed at this node, so they are not inherited by ftz-f1. The fly gene itself
(FB:FBgn0001078) is one of the seeds for GO:0006357 and GO:0009755.

## Isoforms

The sibling folder `genes/DROME/ftz-f1/` (keyed to M9NFK2) has a sequence comparison
(`ftz-f1-bioinformatics/RESULTS-rereview.md`) showing that M9NFK2 is identical to
P33244-2 (isoform A, the 803-aa betaFTZ-F1 product), and that both isoforms share the
629-aa C-terminal segment containing the DNA-binding domain, FTZ-F1 box and
ligand-binding-type domain. P33244-1 (isoform B, 1027 aa, the displayed canonical
sequence) differs only in its N-terminal region and corresponds to the maternal
alphaFTZ-F1 form.
