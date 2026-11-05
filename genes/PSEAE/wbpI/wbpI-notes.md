# wbpI (PA3148, G3XD61) review notes

## Sources and research (2026-11-05)

Manual research (no deep-research provider). Sources: UniProt G3XD61 (Swiss-Prot), the GOA
file, cached abstracts of PMID:10930727 and PMID:17346239 (the PubMed MCP returned no PMC body
for PMC1925246; PMID:10930727 has no PMC copy). A PubMed search for further WbpI papers failed
(API error).

- The serotype O5 B-band O antigen contains di-N-acetylated mannosaminuronic acids. Knockout
  of wbpI abolishes B-band LPS, and E. coli wecB cannot replace it
  [PMID:10930727 "Specific knockout mutations in the putative UDP-D-N-acetylglucosamine (UDP-D-GlcNAc) epimerase gene, wbpI, or the putative UDP-D-N-acetylmannosamine dehydrogenase gene, wbpA, resulted in strains that no longer produced B-band lipopolysaccharide, confirming the essential roles of these genes in B-band O antigen synthesis."];
  [PMID:10930727 "These results imply that the P. aeruginosa UDP-D-GlcNAc precursor may be di-N-acetylated prior to further modification, preventing the E. coli enzymes from recognizing it as a substrate."].
- Purified His6-WbpI 2-epimerizes UDP-GlcNAc3NAcA to UDP-ManNAc3NAcA (CE and NMR), and does
  not use UDP-GlcNAc
  [PMID:17346239 "Neither enzyme utilized UDP-alpha-D-GlcNAc, UDP-alpha-D-GlcNAcA (UDP-2-acetamido-2,3-dideoxy-alpha-D-glucuronic acid) or UDP-alpha-D-GlcNAc3NAc (UDP-2,3-diacetamido-2,3-dideoxy-alpha-D-glucose) as substrates."];
  [PMID:17346239 "Data collected from one- and two-dimensional NMR experiments showed that His6-WbpI catalysed the 2-epimerization of UDP-alpha-D-GlcNAc3NAcA, converting it into UDP-alpha-D-ManNAc3NAcA."].
- The reaction is EC 5.1.3.23, RHEA:24764 (UniProt CC:CATALYTIC ACTIVITY, ECO:0000269,
  PubMed:17346239). GO has no term for it: go-basic.obo (`.cache/paint`, 2026-11-05) has no
  term with EC:5.1.3.23 or RHEA:24764 xrefs. GO:0008761 is defined as UDP-GlcNAc =
  UDP-ManNAc (EC:5.1.3.14) and GO:0050378 as UDP-glucuronate = UDP-galacturonate (a
  4-epimerase). Neither fits. Closest existing parent: GO:0016857 racemase and epimerase
  activity, acting on carbohydrates and derivatives.
- A live UniProt query (2026-11-05, organism_id 208964 and Pfam PF02350) returns only
  G3XD61 wbpI PA3148: PAO1 has no WecB-type UDP-GlcNAc 2-epimerase.

## PseudoCAP IBA-seed assessment

Seeds of PTN001056041 (`.cache/paint/IBD.gaf`, column 8): both GO:0000271 and GO:0008761 are
seeded by P27828 (E. coli WecB) and G3XD61 (this gene). QuickGO (2026-11-05): WecB has
GO:0008761 IDA (EcoCyc, PMID:15210128) and GO:0009246 enterobacterial common antigen
biosynthetic process IMP (EcoCyc, PMID:2166030). The 41 leaves (`.cache/paint/leaf.gaf.gz`)
are mostly WecB/MnaA-type genes (wecB, mnaA, siaA, uae and many locus-tag-only leaves),
with WbpI as a divergent member.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001056041 | GO:0008761 UDP-N-acetylglucosamine 2-epimerase activity | 2 | 41 (29 taxa) | GO:0008761, IMP, PMID:10930727 (PseudoCAP); also GO:0008761 IDA PMID:17346239 (UniProt) | WRONG | The IMP rests on loss of B-band LPS, a phenotype, and the gene's 2000 annotation as a "putative" UDP-GlcNAc epimerase. The cited abstract itself proposes a di-N-acetylated substrate, and the purified enzyme does not use UDP-GlcNAc (PMID:17346239). The UniProt IDA row uses the same wrong term for the 2007 data. | E. coli WecB (EcoCyc IDA) | Yes, for the WecB-type leaves: WecB alone supports the term. But the term does not suit WbpI: GO_CENTRAL MISSING_NEGATION (PROBABLE) for G3XD61 on the IBA row. |
| PTN001056041 | GO:0000271 polysaccharide biosynthetic process | 2 | 41 (29 taxa) | GO:0000271, IMP, PMID:10930727 (PseudoCAP); also GO:0009243 O antigen biosynthetic process IMP | SOUND | WbpI makes a nucleotide-sugar precursor of the O antigen and its knockout loses B-band LPS; the enzyme performs a step of O-antigen synthesis. The broad node term suits a clade whose members feed ECA, teichoic acid, capsule and O antigen. | E. coli WecB (ECA biosynthesis IMP) | Yes. No GO_CENTRAL defect. |

Defects recorded (all on wbpI rows):
- PSEUDOCAP WRONG_TERM, GO:0008761 IMP (PMID:10930727), CONFIRMED: the 2007 abstract states
  the enzyme does not use UDP-GlcNAc.
- PSEUDOCAP WRONG_TERM, GO:0050378 EXP (PMID:17346239), CONFIRMED: the abstract states a
  2-epimerization of UDP-GlcNAc3NAcA; GO:0050378 is a UDP-glucuronate 4-epimerase.
- UNIPROT WRONG_TERM, GO:0008761 IDA (PMID:17346239), CONFIRMED: same abstract.
- GO_CENTRAL MISSING_NEGATION at PTN001056041 for G3XD61, PROBABLE (the fact is in the
  abstract; the right tree-level fix, a NOT on WbpI or on a WbpI/WlbD subclade, depends on
  the tree).

All three GO:0008761 rows and the GO:0050378 row are MODIFY to a proposed new term,
"UDP-2,3-diacetamido-2,3-dideoxy-alpha-D-glucuronate 2-epimerase activity" (EC 5.1.3.23,
RHEA:24764), parent GO:0016857.
