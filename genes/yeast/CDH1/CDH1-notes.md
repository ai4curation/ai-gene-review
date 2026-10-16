# CDH1 (Hct1) — curation notes

Saccharomyces cerevisiae CDH1/HCT1, YGL003C, UniProt P53197. APC/C activator protein CDH1
(Cdc20/Fizzy family, PANTHER PTHR19918:SF1). **Not** E-cadherin: in yeast the symbol refers to
the second WD40 coactivator of the anaphase-promoting complex/cyclosome.

## Identity and architecture

- 566 aa; N-terminal regulatory region with the C-box (APC/C docking, ~aa 55-61) and multiple
  Cdk1 sites; C-terminal seven-bladed WD40 propeller (repeats from aa 258) ending in the
  invariant Ile-Arg (IR) tail [file:yeast/CDH1/CDH1-uniprot.txt "The C-box is required for the
  association with the APC/C complex"].
- Structures: 4BH6 (WD40 domain), 5A31 and 8A3T (cryo-EM of yeast APC/C with Cdh1 bound).

## Core function 1: APC/C substrate receptor

- Schwab et al. 2001: Hct1 co-immunoprecipitates Clb2, Clb3 and Cdc5 but not Pds1 or Clb5; a
  Clb2 deletion that cannot bind Hct1 is stabilised in G1; C-box and C-terminal mutants that
  cannot bind the APC still bind Clb2 [PMID:11566880 "This study provides evidence that Hct1
  functions as a substrate receptor that recognizes target proteins and recruits them to the APC
  for ubiquitylation and subsequent proteolysis"; "Thus, alterations of Hct1 at the N- or
  C-terminus are compatible with the binding of Hct1 to Clb2, but interfere with binding to the
  APC, suggesting that different domains of Hct1 are responsible for substrate recognition and
  APC association"].
- Interestingly the Clb2 destruction box was neither necessary nor sufficient for Hct1 binding
  in that study; later work (Hsl1, Acm1) established D-box/KEN-box recognition by the WD40
  propeller [PMID:21460798 "Cdc20 and Cdh1 are WD40-containing APC co-activators that bind
  destruction boxes (DB) and KEN boxes within substrates to recruit them to the APC for
  ubiquitination"].
- Known substrates: Clb2, Clb3, Cdc5, Cdc20, Ase1, Cin8, Kip1, Fin1, Hsl1, Iqg1, Spo12, Nrm1,
  Yhp1, plus candidates Tos4, Pdr3, Fir1, Mps1, Ybr138C (deep research).

## Core function 2: APC/C coactivator for mitotic exit and G1

- Visintin, Prinz and Amon 1997: cdh1Δ is impaired in Ase1/Clb2 degradation, not Pds1; CDH1
  overexpression induces APC-dependent proteolysis out of phase [PMID:9334304 "cdh1Delta mutants
  were impaired in the degradation of Ase1 and Clb2 but not in that of Pds1"].
- Zachariae et al. 1998: cyclin proteolysis requires Hct1 binding to the APC; Cdk
  phosphorylation blocks the interaction; proteolysis runs from anaphase through G1 [PMID:9831566
  "Proteolysis commences during anaphase, persisting throughout G1 until it is terminated by
  cyclin-dependent kinases (CDKs) as cells enter S phase"].
- Reconstitution: purified TAP-APC/C ubiquitinates Clb2/Pds1 only with Cdh1 added, and not with
  the IR-tail mutant Cdh1-IK [PMID:15060174 "whereas Cdh1 triggered ubiquitination of both Pds1
  and Clb2"]. Half-maximal activation at ~50 nM Cdh1; IR tail binds the Cdc27 TPR groove, Cdc23
  provides a second site; ΔC-box and ΔIR strongly reduce activity [PMID:19362536 "The
  concentration of Cdh1 required for half-maximal stimulation of wild-type APC/C was about 50 nM,
  as seen in previous studies"].
- Mitotic exit: Clb2 destruction by APC/C-Cdh1 and Sic1 binding are the two redundant routes to
  CDK inactivation [PMID:18172166 "The final step in CDK inactivation that triggers exit from
  mitosis is brought about by two redundant mechanisms: degradation of Clb cyclins by the
  APC/C-Cdh1 and binding of the Clb–CDK inhibitor Sic1 to the kinase complex"]. Cdc14 activates
  Cdh1 by dephosphorylation and APC/C-Cdh1 then degrades Cdc5, returning Cdc14 to the nucleolus
  (negative feedback) [PMID:18172166 "Our results indicate that the APC/C-Cdh1 promotes the
  return of Cdc14 into the nucleolus by degrading Cdc5"].

## Regulation

- Cdk1 multisite phosphorylation (Cdc28-Clb5 predominantly) blocks APC/C binding and drives
  Msn5-dependent nuclear export; Cdc14 reverses it at mitotic exit [PMID:12456658 "Nuclear export
  of Cdh1p is regulated by phosphorylation and requires active Cdc28p kinase"].
- Acm1 (with Bmh1) is a pseudosubstrate inhibitor binding the WD40 propeller via a D-box, KEN box
  and A-motif [PMID:21460798 "Acm1 is an APC(Cdh1) inhibitor that utilizes a DB and a KEN box to
  bind Cdh1 and prevent substrate binding, although Acm1 itself is not a substrate"; PMID:17178718
  "The assembly of the ternary complex inhibits ubiquitination of Clb2 in vitro by blocking the
  interaction of Cdh1 with Clb2"].

## Localisation

- Nuclear in G1 (active window), cytoplasmic from S to end of M; Pse1 import, Msn5 export; a
  transient bud-neck pool after bud emergence [PMID:12456658 "Here we show that Cdh1p is nuclear
  during the G(1) phase of the cell cycle, but redistributes to the cytoplasm between S phase and
  the end of mitosis"]. Compartment-targeted reporters show APC/C-Cdh1 activity is nuclear
  (deep research, citing Ostapenko et al. 2012).

## Non-core outputs of substrate turnover

- SPB separation: persistently active APC/C-Cdh1 in Cdk1-activation mutants degrades Cin8, Kip1
  and Ase1 and prevents SPB separation; cdh1Δ suppresses, and spindles form slightly early in
  cdh1Δ [PMID:16688214 "We show that cells that fail to activate Cdk1 are devoid of spindles due
  to persistently active APCCdh1, which targets microtubule-associated proteins Cin8, Kip1 and
  Ase1 for degradation"]. Kept as non-core.
- Actomyosin ring: in cdh1Δ the ring contracts at a normal rate but is not disassembled during
  or after contraction; Iqg1 destruction contributes [PMID:19109423 "In cells lacking the APC
  activator Cdh1, the actomyosin ring contracts at a normal rate, but ring constituents are not
  disassembled normally during or after contraction"]. GO has no ring-disassembly term, so the
  three GO:1903473 rows (positive regulation of ring *contraction*) are modified to GO:0044837
  and a new term is proposed. The APC2 row from the same paper has the same problem.
- SAC antagonism: Nagai and Ushimaru 2014 (abstract only) report partial APC/C-Cdh1 activity
  toward securin in SAC-arrested metaphase cells [PMID:25025567 "These results indicate that Cdh1
  opposes the SAC and promotes anaphase transition"]. This is bypass rather than checkpoint
  silencing, so GO:1902426 is modified to its parent GO:0045842; low confidence, raised as a
  question.

## Annotation decisions (summary)

- ACCEPT: nucleus/cytoplasm (IDA, IEA), APC/C part_of (IBA, 2x IPI with Cdc23/Cdc16), APC/C
  binding (IBA, IEA), cyclin binding (IDA), APC/C-dependent catabolic process (IBA), positive
  regulation of APC/C-dependent catabolic process (IBA, IMP, IGI), ubiquitin ligase activator
  activity (IBA, 2x IDA), ubiquitin-protein transferase activator activity (IEA).
- KEEP_AS_NON_CORE: negative regulation of mitotic SPB separation (IMP, IGI with CDC28).
- MODIFY: GO:0045732 and GO:2000060 (generic catabolic regulation) -> GO:1905786; GO:0045842
  (IMP, PMID:9831566) -> GO:0031536 positive regulation of exit from mitosis (the paper concerns
  anaphase-to-G1 cyclin proteolysis; Cdh1 is dispensable for securin degradation and anaphase
  onset); GO:1902426 -> GO:0045842; 3x GO:1903473 -> GO:0044837.
- REMOVE: bare protein binding with Acm1 (uninformative; inhibitor binding belongs on ACM1).
- NEW: GO:1990756 ubiquitin-like ligase-substrate adaptor activity (IDA, PMID:11566880), the
  term human CDC20/FZR1 carry for the same activity; flagged as a convention question for SGD.

## Open points

- Whether SGD wants GO:1990756 on yeast activators, or prefers cyclin binding + activator
  activity.
- Snf1-dependent Cdh1 turnover during sporulation (Ostapenko and Solomon preprints) is not yet
  peer-reviewed and was not used.
