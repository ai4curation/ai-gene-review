# FZR1 (Cdh1) curation notes

Working notes for the human FZR1 (Q9UM11) review. Nomenclature: in the APC/C
literature the protein is almost always called Cdh1; the HGNC symbol is FZR1
(CDH1 is E-cadherin). Sources: `FZR1-uniprot.txt`, `FZR1-goa.tsv`,
`FZR1-deep-research-falcon.md`, and the cached publications listed below.

## Identity and architecture

- Cdc20/Fizzy-family WD40 beta-propeller coactivator of the APC/C; the second
  coactivator after CDC20. Docks via the N-terminal C-box and C-terminal IR tail
  [PMID:27120157 "both coactivators associate with the APC/C through their common
  C-box and Ile-Arg tail motifs"]; coactivators "recognize substrate degrons, and
  enhance the affinity of the APC/C for its cognate E2" [PMID:27120157].
- Cryo-EM of human APC/C-Cdh1 (PDB 4UI9; UniProt "STRUCTURE BY ELECTRON
  MICROSCOPY (3.60 ANGSTROMS) IN COMPLEX WITH APC/C").
- Substrates are recruited "by binding to a bipartite substrate receptor composed
  of a coactivator protein and Doc1" [PMID:21186364].
- Not catalytic: reconstituted APC/C ubiquitination of TK1 needs both APC/C and
  Cdh1: "No ubiquitinylated ladders occurred if APC/C or Cdh1 was omitted in the
  reaction (lane 1 and 2), and complex containing Cdc20 did not support
  polyubiquitinylation of His-hTK1" [PMID:14701726].

## Cell-cycle timing and regulation

- "in late M, Cdc20 is replaced by Cdh1, the second activator of APC/C. During G1,
  APC/CCdh1 remains active to ensure that certain positive regulators of the cell
  cycle do not accumulate prematurely" [PMID:18662541].
- Off-switch at G1/S by cyclin A/CDK2 phosphorylation:
  "Phosphorylation-deficient mutant Cdh1 or immunodepletion of cyclin A resulted
  in assembly of active Cdh1-APC even in S-phase cells" [PMID:10548110];
  "phosphorylation of Cdh1 prevents its association with the APC/C" [PMID:27120157].
- Emi1/FBXO5: "human Emi1 (hEmi1) functions to promote cyclin A accumulation and S
  phase entry in somatic cells by inhibiting the APC(Cdh1) complex"
  [PMID:11988738]; Cdh1 overexpression imposes a G1 block that hEmi1 can override
  [PMID:11988738 "can override a G1 block caused by overexpression of Cdh1"].
  Emi1 is a pseudosubstrate that "binds to the D-box receptor site on the APC/C
  Cdh1 , and competes with APC/C substrates for D-box binding" [PMID:16921029]
  and also blocks ubiquitin transfer/chain elongation [PMID:23708001].
- MAD2L2/MAD2B "inhibits both CDH1-APC and CDC20-APC. This inhibition is targeted
  to CDH1 and CDC20, but not directly to APC" [PMID:11459826]; Shigella IpaB
  relieves Mad2L2 inhibition [PMID:17719540].
- USP37 "binds CDH1 and removes degradative polyubiquitin from cyclin A" in G1 and
  in mitosis "switched from an antagonist to a substrate of APC(CDH1) and was
  modified with degradative K11-linked polyubiquitin" [PMID:21596315].
- SIRT2 "regulates the anaphase-promoting complex/cyclosome activity through
  deacetylation of its coactivators, APC(CDH1) and CDC20" [PMID:22014574]; UniProt:
  Lys-69/Lys-159 deacetylation enhances CDC27 binding.
- Nuclear PTEN "promotes APC/C association with CDH1" [PMID:21241890]; Pten-loss
  senescence "is dependent on the Cdh1-Ets2-p16 pathway" [PMID:21241890]. The
  mouse IMPs for GO:0008284 and GO:2000773 both come from this paper.
- MAK phosphorylates CDH1 ("CDH1 is indeed phosphorylated by wild-type MAK")
  [PMID:21986944].
- SCF(cyclin F) degrades Cdh1 ("Cdh1 is itself a substrate of SCF(cyclin F)")
  while cyclin F is an APC/C substrate in G1 [PMID:27653696] -- a reciprocal
  feedback circuit at S-phase entry.

## Substrates documented in the cited papers

- TK1 (KEN box) [PMID:14701726]; PLK1 (D-box) and Claspin [PMID:18662541];
  RAD17 [PMID:20424596]; SKP2 (residues 46-90 Cdh1-interaction motif; K68/K71
  acetylation blocks binding) [PMID:22770219]; NEDL2/HECW2 (D-box, mitotic exit)
  [PMID:24163370]; HsSAS-6 (via CCDC84) [PMID:31722219]; cyclin F [PMID:27653696];
  RRM2 (KEN box, mouse R2 cited in PMID:14701726; the cached PMID:22632967 abstract
  covers only the cyclin F arm); pVHL, hedged ("appeared to be a ubiquitylation
  substrate for APC/CCdh1") [PMID:20802534].

## DNA-damage G2 checkpoint

- "in response to genotoxic stress in G2, the phosphatase Cdc14B translocates from
  the nucleolus to the nucleoplasm and induces the activation of the ubiquitin
  ligase APC/C(Cdh1), with the consequent degradation of Plk1" [PMID:18662541];
  "Cdh1-dependent degradation of Plk1 is required for an efficient DNA
  damage-induced G2 checkpoint" [PMID:18662541]. Cdh1(4xA) makes Cdc14B
  dispensable. Supports ACCEPT for GO:0007095 IDA.

## Localisation

- "FZR1 expression was detected in the nucleus, with a weaker diffuse signal in
  the cytoplasm" [PMID:34788397]; UniProt isoform 2 nucleus, isoform 3 cytoplasm.
  HPA: nucleoplasm and nuclear membrane. Nuclear membrane has no orthogonal
  support -> KEEP_AS_NON_CORE.

## Disease / neuronal roles

- "heterozygous loss-of-function of FZR1 leads to developmental and epileptic
  encephalopathies" (DEE109) [PMID:34788397]. Neuronal chromatin-protein clearance
  (INCENP, Aurora B, Ki-67, TOP2A) is from mouse (deep research, Ledvin 2023);
  some proposed neuronal substrates were not confirmed by APC4 deletion (Day
  2024). No neuronal GO annotations exist on human FZR1 and none are proposed.

## Curation decisions (summary)

- 31 GO:0005515 IPI rows: CDC27 rows (5) -> MODIFY to GO:0010997; substrate rows
  (PLK1, CLSPN, RAD17, RRM2, SKP2, HECW2, CCNF, SASS6; 8) -> MODIFY to GO:1990756;
  regulator/inhibitor rows (MAD2L2 x2, FBXO5 x3, USP37, MAK, SIRT2), hedged VHL
  x3, and proteome-scale AP-MS rows (BioPlex x3, U2OS cell map x4) -> REMOVE as
  uninformative (interaction not disputed).
- GO:1904668 IDA -> MODIFY to GO:1990757 + GO:1905786 (direct coactivation is an
  MF, already carried by IBA).
- GO:0007346 NAS -> MODIFY to GO:2000134 (comparator: pombe srw1/ste9 carries
  GO:2000134 by IGI).
- GO:0008284 IEA (mouse IMP transfer) -> MARK_AS_OVER_ANNOTATED; GO:2000773
  IEA/ISS -> KEEP_AS_NON_CORE; GO:0051445 NAS -> KEEP_AS_NON_CORE; GO:0031965
  HPA -> KEEP_AS_NON_CORE.
- All IBA rows (PTN000460086), all Reactome TAS locations, IDA/NAS process rows
  and InterPro/UniPathway IEAs -> ACCEPT.
