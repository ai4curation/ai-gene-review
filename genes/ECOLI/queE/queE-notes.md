# queE (P64554) notes, E. coli K-12

Deep research was unavailable for this gene (falcon 403, asta returned nothing in Phase 1
of the RADICAL_SAM project). Notes are built from cached publications, PubMed and UniProt.

## Identity

- UniProt P64554, 7-carboxy-7-deazaguanine (CDG) synthase, EC 4.3.99.3, synonym ygcF,
  b2777. HAMAP MF_00917; proteobacterial QueE subfamily (TIGR04322, IPR027609);
  PANTHER PTHR42836:SF1. Homodimer. One radical SAM [4Fe-4S] cluster (Cys31/35/38) and a
  catalytic Mg2+ [file:ECOLI/queE/queE-uniprot.txt].
- Reaction (RHEA:27974): 6-carboxy-5,6,7,8-tetrahydropterin (CPH4) + H+ = CDG + NH4+, a
  radical ring contraction. Rhea/UniProt write the reaction without net SAM consumption
  (SAM is listed as a cofactor bound to the cluster), which I have not verified from a
  primary paper here.

## Biochemistry (mostly orthologs)

- B. subtilis QueE in vitro converts CPH4 to CDG, SAM- and reductant-dependent
  [PMID:19354300 "The conversion of CPH4 to this new product occurred only in the presence of SAM and dithionite"].
- E. coli QueE crystal structure: head-to-tail homodimer, intermediate between the
  B. multivorans and B. subtilis folds; surface tuned for flavodoxin FldA
  [PMID:30341796 "These structural observations are consistent with the report that Ec FldA does not promote the CDG synthesis activity of all three QueEs uniformly."].
  All QueE homologs tested need Mg2+ [PMID:30341796 "All QueE homologs tested require Mg 2+ for catalysis"].
- 5'-dA shunt chemistry studied in PMID:40015645 (mechanistic context).

## In vivo function in E. coli

- Q biosynthesis: ΔqueE lacks Q-tRNA; complemented by WT queE
  [PMID:38768229 "confirming that QueE is required to produce Q"]. Screen of Keio strains for Q
  pathway genes (PMID:21502530; abstract-only, curator IMP).
- Moonlighting division inhibitor: under PhoQ/PhoP activation (antimicrobial peptides,
  low Mg2+) or overexpression, QueE localizes to the Z-ring and blocks septation
  [PMID:27471053 "However, QueE's effect on cell division is independent of the queuosine biosynthesis pathway"];
  separable by mutation from catalysis (R27A abolishes Q but keeps filamentation; E15A,
  C31A, C35A, K66A keep Q but lose filamentation; E45-W67 region needed for division
  block) [PMID:38768229 "elucidating QueE as a moonlighting protein"].

## Curation decisions

- No GO MF term exists for CDG synthase; proposed NTR "7-carboxy-7-deazaguanine synthase
  activity" (parent GO:0016840, RHEA:27974, EC 4.3.99.3). GO:0016840 and GO:0003824 rows
  MODIFY to the NTR.
- GO:0008616 rows MODIFY to GO:0160253 de novo tRNA queuosine(34) biosynthetic process (E. coli
  makes Q de novo from GTP; GO:0160253 is a child of GO:0008616). Comparator: E. coli QueC
  (P77756) and QueD (P65870) carry GO:0008616 but not GO:0097288 (preQ0 biosynthesis), so I
  did not add GO:0097288 as NEW.
- Division rows kept non-core; negative regulation of cytokinesis refined to
  GO:0010974 negative regulation of division septum assembly (is_a descendant), as the
  block is at septation downstream of Z-ring assembly.
- SAM binding (GO:1904047) already present as IEA; ACCEPT, no NEW row needed.
- The module bacterial_preq1_incorporation_queuosine_maturation places QueE outside its
  boundary (preQ0 supply upstream), consistent with this review.
