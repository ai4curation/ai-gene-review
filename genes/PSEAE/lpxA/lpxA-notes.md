# lpxA (PA3644, Q9X6P4) notes

## Identity

- Acyl-[acyl-carrier-protein]--UDP-N-acetylglucosamine O-acyltransferase
  (UDP-GlcNAc acyltransferase), EC 2.3.1.129, 258 aa, homotrimeric
  left-handed beta-helix of hexapeptide repeats (TIGR01852 lipid_A_lpxA,
  IPR010137, HAMAP MF_00387, PANTHER PTHR43480). Swiss-Prot annotation is
  entirely rule-based (ECO:0000255|HAMAP-Rule:MF_00387).
- Catalyses the first, committed step of lipid A synthesis: transfer of a
  (3R)-hydroxyacyl chain from ACP to the 3-OH of UDP-GlcNAc
  [file:PSEAE/lpxA/lpxA-uniprot.txt "Glycolipid biosynthesis; lipid IV(A) biosynthesis; lipid IV(A)"]

## Pseudomonas-specific enzymology: PMID:9440522

- The P. aeruginosa PAO1 lpxA gene was cloned by expression in E. coli and the
  enzyme characterised; it is acyl-chain-length-specific for C10 rather than
  the C14 of E. coli LpxA
  [PMID:9440522 "Pseudomonas lpxA encodes a 10-carbon-specific UDP-GlcNAc acyltransferase, whereas the E. coli transferase is selective for a 14-carbon acyl chain."]
  [PMID:9440522 "LpxA assays of extracts of this construct indicated that it is > 1,000-fold more selective for 3-hydroxydecanoyl-ACP than for 3-hydroxymyristoyl-ACP."]
  [PMID:9440522 "A plasmid (pGD3) containing the 1.3-kb SalI-PstI fragment complemented E. coli RO138, a temperature-sensitive mutant harboring lpxA2."]
  and the lipid A made in that strain carries 3-hydroxydecanoate at positions 3
  and 3'
  [PMID:9440522 "Mass spectrometry of lipid A isolated from this strain by hydrolysis at pH 4.5 revealed [M-H]- 1,684.5 (versus 1,796.5 for wild-type lipid A), consistent with 3-hydroxydecanoate rather than 3-hydroxymyristate at positions 3 and 3'."]
  This paper is cited in the UniProt entry (reference [1]) but is not used in
  GOA.
- The product specificity matches the native P. aeruginosa lipid A, whose
  3 and 3' positions carry 10:0(3-OH)
  [PMID:1904818 "3-hydroxydecanoic acid groups [10:0(3-OH)] at positions 3 and 3'"]

## The PseudoCAP seed, PMID:1904818

- Kulshin et al. 1991, Eur J Biochem: a chemical/NMR/MS structural
  characterisation of P. aeruginosa lipid A from two wild-type strains and the
  rough mutant PAC 605
  [PMID:1904818 "was investigated using chemical analysis, methylation analysis"]
- The organism is right, but the abstract mentions no lpxA, enzyme assay or
  lpxA mutant: it describes an analysis of the purified glycolipid, published
  before the gene was cloned (1991 vs 1998) and before the PAO1 genome. Only
  the abstract was read (no PMC copy, 2026-10-29), so it is probably, not
  certainly, not a direct assay of PA3644; the WRONG_REFERENCE defect was
  downgraded from CONFIRMED to PROBABLE in the 2026-10-29 audit.
- The claim is nevertheless correct: LpxA catalyses the first step of lipid A
  synthesis, lipid A is the LPS anchor, and the Pseudomonas enzyme's C10
  specificity was demonstrated directly in PMID:9440522. So the right fix is
  to repoint the reference (and the paper that is cited reinforces the
  product: 10:0(3-OH) at 3 and 3').

## PAINT node PTN000602377

- PTHR43480 (268 members, all in subfamily SF1), entirely Gram-negative
  bacteria: Enterobacteriaceae, Burkholderia, Pseudomonas, Rickettsia,
  Brucella, Chlamydia, Campylobacter, Helicobacter, Vibrio, Xanthomonas,
  Neisseria, Rhizobium and so on.
- QuickGO (2026-10-28): the node propagates two terms, GO:0009103 and
  GO:0005829, each to 24 leaves; the GO:0009103 leaves are lpxA genes of
  E. coli, Helicobacter, Chlamydia, Vibrio, Bacteroides, Thermotoga,
  Bradyrhizobium, Shewanella and others, i.e. exactly the lipid-A-making
  clade.
- The MF IBA on this gene comes from a different node, PTN000602373, whose
  seeds are E. coli LpxA and the Arabidopsis locus AT4G29540, i.e. the
  acyltransferase activity is placed deeper than the bacterial LpxA clade.
- E. coli LpxA (P0A722) carries GO:0009245 lipid A biosynthetic process and
  GO:0008780 by IDA (PMID:3549716) but has no experimental GO:0009103, which
  is why the LPS IBD rests on the PseudoCAP row alone.
- Note that GO:0009245 lipid A biosynthetic process is not a descendant of
  GO:0009103 (it sits under lipooligosaccharide/glycolipid biosynthesis), so
  the two are separate claims rather than a general/specific pair; both are
  true of LpxA, and the lipid A term is the more mechanism-specific of the two.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000602377 | GO:0009103 lipopolysaccharide biosynthetic process | 1 (sole seed) | 24 (22 taxa) | GO:0009103, IDA, PMID:1904818 (PseudoCAP) | SOUND (term and node); reference WRONG | The term is correct for LpxA and for the whole node: PTHR43480 is the LpxA family of Gram-negative bacteria, every member catalyses the first step of lipid A synthesis, and lipid A is the LPS anchor, so an LPS-biosynthesis IBD suits the clade. The cited paper, however, is a 1991 structural study of P. aeruginosa lipid A whose abstract mentions no enzyme assay and no lpxA; it predates the cloning of the gene, so the IDA is probably not direct evidence for PA3644 (abstract only read). The direct evidence exists in PMID:9440522, where the cloned PAO1 lpxA is assayed as a 10-carbon-specific UDP-GlcNAc acyltransferase and complements an E. coli lpxA mutant. Recorded as a PROBABLE WRONG_REFERENCE PseudoCAP defect; the IBD itself stands, and would be sharper as GO:0009245 lipid A biosynthetic process, for which E. coli LpxA already has an IDA. |

## Decisions summary

- ACCEPT: acyl-ACP--UDP-GlcNAc O-acyltransferase activity (IBA, IEA), lipid A
  biosynthetic process (IEA), LPS biosynthetic process (IBA, IDA with a
  repointed reference), cytosol (IBA).
- MODIFY: cytoplasm -> cytosol; lipid biosynthetic process -> lipid A
  biosynthetic process; transferase activity -> acyl-ACP--UDP-GlcNAc
  O-acyltransferase activity.
- No REMOVE. One PSEUDOCAP WRONG_REFERENCE defect.
