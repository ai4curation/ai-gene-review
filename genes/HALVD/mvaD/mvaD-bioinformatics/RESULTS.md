# PANTHER tree placement of archaeal PTHR10977 members

Script: `panther_tree_placement.py` (standard library only; fetches the live PANTHER
family tree from the pantherdb.org `treeinfo` service and UniRef50 cluster membership
from the UniProt REST API; nothing is cached or hard-coded).

Command (run 2026-11-18):

```
python3 -I panther_tree_placement.py PTHR10977 PTN000104601 D4GXZ3 Q6KZB1 Q9HJS1 Q97UL5
```

Question: the PAINT IBD node for `GO:0004163` diphosphomevalonate decarboxylase
activity, `GO:0019287` and `GO:0005829` in PTHR10977 is PTN000104601
(`interpro/panther/PTHR10977/PTHR10977-paint.tsv`). Which of the four archaeal
SF3 members (H. volcanii mvaD D4GXZ3, P. torridus PTO1356 Q6KZB1, T. acidophilum
Ta0893 Q9HJS1, S. solfataricus SSO2989 Q97UL5) descend from that node?

## Output

```
PANTHER product: {'source': 'PANTHERDB', 'version': 19}
Tree leaves with UniProt accession: 138

== D4GXZ3
   not a leaf of the PTHR10977 reference tree; UniRef50 cluster: UniRef50_D4GXZ3
   tree leaves in the same UniRef50 cluster: ['Q9HRQ4']
   Q9HRQ4 (Halobacterium salinarum; Diphosphomevalonate decarboxylase) - UniRef50 cluster-mate of D4GXZ3
   path: PTN008313801 [Terrabacteria; SPECIATION] > PTN004212759 [-; HORIZ_TRANSFER] > PTN000861789 [-; LEAF]
   descends from PTN000104601: False
   leaves under parent PTN004212759: Q9HRQ4 (Halobacterium salinarum; Diphosphomevalonate decarboxylase); A9WEU8 (Chloroflexus aurantiacus; GHMP kinase domain protein)

== Q6KZB1
   not a leaf of the PTHR10977 reference tree; UniRef50 cluster: UniRef50_Q6KZB1
   tree leaves in the same UniRef50 cluster: none

== Q9HJS1
   not a leaf of the PTHR10977 reference tree; UniRef50 cluster: UniRef50_Q9HJS1
   tree leaves in the same UniRef50 cluster: none

== Q97UL5
   Q97UL5 (Sulfolobus solfataricus; Diphosphomevalonate decarboxylase) - query is a tree leaf
   path: PTN008313801 [Terrabacteria; SPECIATION] > PTN007474433 [-; HORIZ_TRANSFER] > PTN000104601 [Archaea-Eukaryota; SPECIATION] > PTN000104655 [-; LEAF]
   descends from PTN000104601: True
   leaves under parent PTN000104601: 132
```

## Interpretation

- S. solfataricus SSO2989 (Q97UL5) is a leaf of the PANTHER 19 tree and descends from
  PTN000104601, the Archaea-Eukaryota node that carries the diphosphomevalonate
  decarboxylase IBD. It is the only archaeal leaf under that node; the other 131
  leaves are eukaryotic.
- H. volcanii mvaD (D4GXZ3) is not a tree leaf. Its UniRef50 cluster-mate
  Halobacterium salinarum VNG_0593G (Q9HRQ4) is, and it sits outside PTN000104601,
  in node PTN004212759 together with Chloroflexus aurantiacus A9WEU8. Haloarchaea and
  Chloroflexi are the two lineages in which phosphomevalonate decarboxylase (MPD/PMD)
  has been demonstrated (PMID:24375100, PMID:24327557). The PANTHER topology therefore
  separates the haloarchaeal/Chloroflexi MPD clade from the IBD node, and PTN004212759
  carries no IBD in the PAINT file.
- P. torridus PTO1356 (Q6KZB1) and T. acidophilum Ta0893 (Q9HJS1) are not tree leaves,
  and no tree leaf shares their UniRef50 cluster. The Thermoplasmatales are not
  represented in the PANTHER 19 tree, so the tree cannot say where their M3K and MBD
  lineages attach. They are family members by HMM scoring only.
- None of the three non-leaf proteins receives an IBA from PTHR10977 in GOA (checked in
  QuickGO, 2026-11-18), consistent with PAINT propagation reaching only tree members.

Limitations: UniRef50 co-membership is used as a proxy for where a non-leaf protein
would attach; it is not a phylogenetic placement. The PANTHER HMM subfamily
assignment (all four are PTHR10977:SF3) is a separate question from tree placement.
