# MMAB (Q96EY8) — curation notes

Human MMAB / cblB, mitochondrial **ATP:cob(I)alamin adenosyltransferase (ATR)**. HGNC:19331. Chromosome 12.

## Core biology (verified)

- MMAB is the mitochondrial adenosyltransferase (ATR) that catalyses the **final step of
  adenosylcobalamin (AdoCbl / coenzyme B12) synthesis**: it transfers the 5'-deoxyadenosyl group
  from ATP to reduced cob(I)alamin, producing adenosylcob(III)alamin (AdoCbl) plus inorganic
  triphosphate. AdoCbl is the essential cofactor of methylmalonyl-CoA mutase (MMUT/MCM).
  - UniProt CATALYTIC ACTIVITY (Rhea:56796): "cob(I)alamin-[corrinoid adenosyltransferase] + ATP =
    apo-[corrinoid adenosyltransferase] + adenosylcob(III)alamin + triphosphate" [ECO:0000269|PubMed:12514191].
  - [PMID:12514191 abstract, "ATP:cob(I)alamin adenosyltransferase (ATR) catalyzes the terminal step
    in the conversion of cobalamins into Ado-B12"]. Human cDNA complemented an ATR-deficient bacterial
    mutant; recombinant enzyme showed 98 nmol/min/mg ATR activity.
- **Homotrimer** with active sites at subunit interfaces; ATP-bound crystal structures (PMID:17176040,
  PDB 2IDX; also 6D5K/6D5X/7RUT). [PMID:33797888 "ATR, an 81 kDa homotrimer with active sites housed
  at the subunit interfaces...catalyzes the adenosylation of cob(I)alamin by ATP"].
- **Escort / direct hand-off**: ATR does not just synthesize AdoCbl, it delivers it directly to MCM
  (avoiding release into solution); transfer is stimulated by ATP binding to MMAB and gated by MMAA
  (cblA G-protein). [PMID:30282455 "ATR also delivers the AdoCbl product directly to MCM, thereby
  averting cofactor loss by release into solution"]; [PMID:28497574 abstract "gating the transfer of
  AdoCbl from MMAB to MUT"].
- **Cobalamin binding / coordination chemistry**: ATR binds cobalamin in the base-off state; ATP
  binding organizes a high-affinity cob(II)alamin pocket and, via a 4-coordinate square-planar Co(II)
  state, raises the Co2+/1+ redox potential to allow reduction to cob(I)alamin before adenosylation.
  [PMID:15913339 abstract "the interaction between Co2+Cbl and hATR promotes partial conversion of the
  cofactor to its 'base-off' form...leading to the formation of an unprecedented Co2+Cbl species with
  spectroscopic signatures consistent with an essentially four-coordinate, square-planar Co2+ center"].
  UniProt cites PMID:28497574 for adenosylcobalamin-binding (GO:0031419 IDA).
- **Sacrificial homolysis / cofactor conservation**: if MCM is unavailable, ATR homolytically cleaves
  the newly formed Co–C bond of AdoCbl (reverse of the SN2 making reaction) to give tightly-bound
  cob(II)alamin, sequestering the precious cofactor. [PMID:30282455], [PMID:33797888].

## Localization

- Mitochondrion / mitochondrial matrix. N-terminal transit peptide (1–32) cleaved. Supported by
  UniProt SUBCELLULAR LOCATION, Reactome, and high-confidence mitochondrial proteome
  [PMID:34800366, HTP mitochondrion].

## Disease

- **Methylmalonic aciduria, cblB type (MACB; MIM:251110)** — autosomal recessive, defective AdoCbl
  synthesis; frequently vitamin B12-responsive (Orphanet 79311 "Vitamin B12-responsive methylmalonic
  acidemia type cblB"). Confirmed in dismech disorder KB Methylmalonic_Acidemia.yaml (MMAB listed
  under MMUT/AdoCbl pathway molecular-function deficiency; [PMID:27653704 "genes encoding the enzymes
  responsible for the generation of 5-deoxyadenosylcobalamin (AdoCbl) cofactor of Mut (MMAA and MMAB)"]).

## GOA annotation notes

- GO:0008817 corrinoid adenosyltransferase activity — core MF, multiple independent EXP/IDA + IBA + IEA. ACCEPT.
- GO:0016765 transferase activity, transferring alkyl or aryl groups (IDA, PMID:12514191) — correct
  but a **parent** of GO:0008817 (entailed_edge confirms GO:0008817 ⊆ GO:0016765). Too general → MODIFY to GO:0008817.
- GO:0009235 cobalamin metabolic process — BP; ACCEPT (multiple lines). MMAB acts in AdoCbl (coenzyme
  B12) synthesis; humans do not perform de novo corrin biosynthesis so "cobalamin metabolic process"
  is the right-grain BP (not GO:0009236 de novo biosynthetic).
- GO:0031419 cobalamin binding (IDA, PMID:28497574) — ACCEPT; ATR demonstrably binds AdoCbl/cobalamin.
- GO:0005739 mitochondrion (IEA + HTP) / GO:0005759 mitochondrial matrix (TAS Reactome) — ACCEPT.
- 7 GO:0005515 protein binding IPIs (IntAct high-throughput interactome/proteome screens: CBY2, CALR,
  DBT, DLST, NEK7, OPTN, DBT). Uninformative bare protein binding; per policy MARK_AS_OVER_ANNOTATED
  (not REMOVE). None of the cited papers (25910212, 32814053, 33961781, 40205054) discuss MMAB function;
  they are large-scale networks reporting the interaction in supplementary data only.
- ATP binding (GO:0005524, UniProt-KW) is in UniProt DR but NOT in GOA TSV — add as NEW (structurally
  established, PMID:17176040 ATP-bound structure; UniProt BINDING features). MF.

## Deep research

falcon deep-research file (MMAB-deep-research-falcon.md) was ABSENT at review time (polled up to 8 min).
Review grounded in UniProt (Q96EY8), seeded GOA TSV, cached publications PMID_*.md, and the dismech
disorder KB Methylmalonic_Acidemia.yaml.
