# mom-4 (C. elegans, Q9XTC6, F52F12.3) review notes

## Deep research

Falcon deep research is known to fail for this batch (HTTP 402) and was not attempted.
No `-deep-research-*.md` file exists; these notes are built from the cached publications
(`publications/PMID_*.md`) and the UniProt record.

## Identity and domain architecture

- 536 aa; N-terminal disordered region (1-34), protein kinase domain 51-305 (STE/TKL-like MAP3K
  kinase domain, ATP-binding 57-65, catalytic Asp176 = HRD proton acceptor), long C-terminal
  disordered region (314-438) (UniProt FT lines).
- UniProt name: Mitogen-activated protein kinase kinase kinase mom-4, EC 2.7.11.25, based on
  PMID:10391246 and PMID:11323434.
- InterPro on UniProt lists only generic kinase signatures (IPR000719, IPR001245, IPR017441,
  IPR011009). It does NOT list the TAK1-specific signatures (IPR049637 MAP3K7; IPR060742
  C-terminal TAB-binding region) used to characterize TAK1 in the PTHR46716 family review. The
  MOM-4 C-terminus is divergent from vertebrate TAK1, consistent with TAP-1 docking differing
  from TAB1 docking (PMID:11323434, Ala-364 vs Phe-484 motif difference).
- PANTHER: UniProt cross-references PTHR46716 / PTHR46716:SF1 (MAP3K7), whereas the PANTHER 19
  classification files place MOM-4 in PTHR23257:SF958 (see family review). Biologically MOM-4 is a
  genuine but divergent TAK1 ortholog: mouse MAP3K7 partially rescues mom-4(or39)
  [PMID:25548171 "Mouse MAP3K7 similarly expressed in EMS from a med-1 promoter-driven transgene was able to rescue the intestinal defects of mom-4(or39) embryos partially"].

## Molecular function: MAP3K that directly phosphorylates the NLK-family MAPK LIT-1

- MOM-4 is the TAK1 homolog and binds a TAB1-related activator
  [PMID:10391246 "encode components of the mitogen-activated protein kinase (MAPK) pathway that are homologous to vertebrate transforming-growth-factor-beta-activated kinase (TAK1) and NEMO-like kinase (NLK), respectively"; "MOM-4 and TAK1 bind related proteins that promote their kinase activities"].
- TAP-1 (TAB1 homolog, G5EEM6) binds and activates MOM-4
  [PMID:11323434 "The C. elegans homolog of TAB1, TAP-1, was able to interact with and activate the C. elegans homolog of TAK1, MOM-4."]. Abstract-only.
- Wnt1 stimulates MOM-4/Tak1 autophosphorylation and activation dependent on TAP-1/Tab1
  [PMID:14960582 "We find that Wnt1 stimulation results in autophosphorylation and activation of MOM-4/Tak1 in a TAP-1/Tab1-dependent fashion."]. Abstract-only; the
  abstract conflates worm/mammalian names, but the curator (IDA GO:0004709) read the full text.
- MOM-4 stimulates WRM-1/LIT-1-dependent POP-1 phosphorylation
  [PMID:10488343 "encodes a MAP kinase kinase kinase-related protein that stimulates the WRM-1/LIT-1-dependent phosphorylation of POP-1"].
- Decisive biochemistry (full text): MOM-4/TAP-1 directly phosphorylates the LIT-1 activation-loop
  T220 (TXE motif) with a kinase-dead D176N control, in vitro and in cells, and T220-P is reduced
  in mom-4(ts) embryos [PMID:25548171 "Second, wild-type, but not kinase-dead (D176N), MOM-4 can phosphorylate bacterially expressed and purified HIS::LIT-1 at T220 in vitro"].
  Because LIT-1/NLK has TXE rather than TXY, a MAP3K can activate it directly without a MAP2K;
  no MAP2K has been found in C. elegans endoderm specification (PMID:25548171 Discussion). So the
  MOM-4 -> LIT-1 "MAPK cascade" is a two-tier MAP3K -> MAPK module.
- MOM-4 is not the only route to LIT-1 activation: LIT-1 can autophosphorylate in a WRM-1-dependent
  way [PMID:25548171 "indicating that activation of LIT-1 is not entirely dependent upon MOM-4"].

## Biological process: Wnt/beta-catenin asymmetry in EMS and other posterior daughters

- mom-4 is required in EMS (responding cell), not in P2
  [PMID:9288749 "mom-1, mom-2, and mom-3 are required in the signaling cell, P2, while mom-4 is required in EMS"].
  Loss gives no endoderm (E -> MS transformation) and excess mesoderm (UniProt disruption phenotype).
- mom-4 and lit-1 downregulate POP-1 in E and other posterior daughters
  [PMID:10391246 "Here we show that the genes mom-4 and lit-1 are also required to downregulate POP-1, not only in E but also in other posterior daughter cells."].
- MOM-4 (with LIT-1) promotes the initial nuclear accumulation of WRM-1/beta-catenin
  [PMID:16077004 "Thus, LIT-1 and MOM-4 appear to play a general role in permitting the initial nuclear accumulation of WRM-1"].
- MOM-4/LIT-1 branch acts upstream of WRM-1 in the Wnt pathway [PMID:20805471 "the MAP kinase cascade, which acts in a separate branch of the pathway immediately upstream of WRM-1"].
- src-1/mes-1 enhance Wnt-pathway mutant endoderm and EMS spindle defects (IGI with src-1)
  [PMID:12110172 "src-1 and mes-1 mutants strongly enhance endoderm and EMS spindle rotation defects associated with Wnt pathway mutants"].

## NF-kappaB

- C. elegans lacks NF-kappaB transcription factors [PMID:31384522 "elegans lacks NF-κB-like transcription factors"].
  No GO NF-kB term exists on mom-4 and none should be propagated.

## Localization

- Only HDA from a muscle GFP "localizome" (PMID:21611156; mom-4 not named in cached text, likely
  supplementary): cytoplasm and striated muscle dense body. No embryonic localization data for
  MOM-4 itself in the cached papers. Treated as non-core.

## Implications for PTHR46716 family review

1. MAP3K activity (GO:0004709) holds for MOM-4 with the strongest direct evidence in the whole
   family for MAP3K -> MAPK phosphorylation (activation loop of LIT-1/NLK), not via MAP2K.
2. TAB1-like activator complex is conserved (TAP-1), but GO:0097076 TAK1 complex is defined via IKK
   and TRAF6, so it is not a good fit for nematodes.
3. NF-kB term exception for nematodes is correct.
4. JNK/p38 cascade roles for MOM-4 are untested in the cached literature (absence of evidence).
