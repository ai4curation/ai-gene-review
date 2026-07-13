# COX18 (human) — curation notes

UniProtKB: Q8N8Q8 · HGNC:26801 · Gene: COX18 (syn. OXA1L2) · 333 aa · Chr 4.
Family: OXA1/ALB3/YidC membrane protein insertase family; COX18 sub-branch (as opposed
to OXA1L sub-branch). TCDB 2.A.9.1.3 (YidC/Alb3/Oxa1 insertase family). InterPro
IPR001708 (YidC/ALB3/OXA1/COX18); Pfam PF02096 (60KD_IMP); CDD cd20069 (5TM_Oxa1-like).

## Verified function
COX18 is a mitochondrial inner-membrane protein-insertion machinery component required
for cytochrome c oxidase (respiratory chain Complex IV) assembly. It mediates the
membrane insertion / translocation of the C-terminal portion (C-tail, apo-CuA site) of
the newly synthesised core subunit MT-CO2 (COX2) across the inner membrane, acting after
COX20-mediated stabilisation of MT-CO2 and before the SCO1/SCO2/COA6 copper-metallation
step. Its molecular function is a membrane insertase / protein-transmembrane-transporter
(translocase) activity, not a purely structural role.

- OXA1/YidC insertase family membership; acts as COX2 assembly factor:
  [PMID:28330871 "COX18 is an additional COX2 assembly factor that belongs to the"] Oxa1
  family of membrane protein insertases.
- Mechanism — transient interaction with COX2, translocation of C-tail across IMM:
  [PMID:28330871 "transiently interacts with COX2 to promote translocation across the inner"]
  membrane of the COX2 C-tail that contains the apo-CuA site.
- Yeast Cox18p inserts Cox2p COOH-tail into IMM (conserved function):
  [PMID:16212937 "Cox18p catalyses the insertion of Cox2p COOH-tail into the"] mitochondrial
  inner membrane.
- Family members facilitate membrane insertion of hydrophobic proteins; Oxa1 and Cox18
  play successive roles in Cox2 assembly:
  [PMID:16911509 "Oxa1 and Cox18, which play successive roles"] in Cox2 assembly;
  [PMID:16911509 "facilitate the membrane insertion of various hydrophobic"] proteins.
- Human disease / loss-of-function reduces Complex IV:
  [PMID:40830826 "translocates the C-terminal tail of MTCO2 across"] the mitochondrial inner
  membrane; mutant "impairs Complex IV assembly and activity";
  [PMID:40830826 "reduced assembly and activity of Complex IV"];
  [PMID:40830826 "reduced ability to translocate MTCO2 C-terminus"];
  the amphipathic/insertase helix is [PMID:40830826 "essential for the insertase function of proteins from the same family"].

## Localisation
Mitochondrion inner membrane, multi-pass (UniProt SUBCELLULAR LOCATION; 3 TM helices,
matrix/IMS topology). Confirmed IDA [PMID:16212937], EXP [PMID:28330871].
Broad GO:0005739 mitochondrion (HTP, PMID:34800366) and GO:0016020 membrane (IEA) are
correct but less informative parents of GO:0005743.

## Interactions
Complex with TMEM177, COA6, MT-CO2, COX20, SCO1, SCO2 (PMID:29154948); transient with
MT-CO2 and COX20-dependent interaction (PMID:28330871). The IPI GO:0005515 "protein
binding" (with O75880=COX20, P00403=MT-CO2, Q5RI15=TMEM177) is uninformative as an MF —
its real functional meaning is captured by the insertase MF + assembly BP; MARK_AS_OVER_ANNOTATED.

## Disease
- MC4DN25 (mitochondrial complex IV deficiency, nuclear type 25): neonatal
  encephalopathy, hypertrophic cardiomyopathy, myopathy, axonal sensory neuropathy
  (PMID:37468577).
- CMT2MM (Charcot-Marie-Tooth, axonal, type 2MM): autosomal recessive axonal
  sensorimotor peripheral neuropathy (PMID:40830826).

## Annotation-review summary
- MF core = GO:0032977 membrane insertase activity (multiple lines: IBA, IEA, IMP, EXP,
  IGI, IDA) — ACCEPT.
- BP core = GO:0033617 mitochondrial respiratory chain complex IV assembly (IBA, IMP,
  TAS, IMP) and GO:0032979 protein insertion into mito inner membrane from matrix
  (IBA, IDA) — ACCEPT.
- GO:0008535 respiratory chain complex IV assembly (IGI) is a broader/parent-style term
  of GO:0033617 → MODIFY to GO:0033617. GO:0051204 / GO:0051205 protein insertion into
  (mitochondrial) membrane are broader parents of GO:0032979 → MODIFY / KEEP_AS_NON_CORE.
- CC core = GO:0005743 mitochondrial inner membrane (IBA, IEA, EXP, TAS, IDA) — ACCEPT.
  GO:0005739 mitochondrion (HTP) and GO:0016020 membrane (IEA) broader → KEEP_AS_NON_CORE.
- GO:0005515 protein binding (IPI) → MARK_AS_OVER_ANNOTATED (uninformative bare term).
</content>
