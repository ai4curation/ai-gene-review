# COQ7 (Q99807) — gene review notes

Human COQ7 / CLK-1 (Timing protein clk-1 homolog). HGNC:2244. Chromosome 16. 217 aa precursor
(mitochondrial transit peptide 1-35; mature chain 36-217). Two isoforms (Q99807-1 canonical;
Q99807-2 lacks residues 1-38). EC 1.14.13.253.

## Core biology

COQ7 is the mitochondrial **carboxylate-bridged di-iron hydroxylase** that catalyzes the
**penultimate step of coenzyme Q (ubiquinone / CoQ10) biosynthesis**: hydroxylation of
5-demethoxyubiquinol/5-methoxy-2-methyl-3-(all-trans-polyprenyl)benzoquinone (DMQ) at the C6
position, yielding demethyl-ubiquinol, which is then O-methylated by COQ3 to give CoQ.

- UniProt names it "NADPH-dependent 3-demethoxyubiquinone 3-hydroxylase, mitochondrial"
  [file:human/COQ7/COQ7-uniprot.txt "RecName: Full=NADPH-dependent 3-demethoxyubiquinone 3-hydroxylase, mitochondrial"].
- The di-iron center is a ferritin-like fold (InterPro Ferritin-like_SF; SUPFAM Ferritin-like).
  UniProt cofactor: "Binds 2 iron ions per subunit"
  [file:human/COQ7/COQ7-uniprot.txt "Note=Binds 2 iron ions per subunit."]. Fe-binding residues:
  E60, E90, H93, E142, E178, E181 (BINDING lines).
- Mechanism (Lippard, PMID:23445365): the enzyme is a **5-demethoxyubiquinone hydroxylase** using
  a **carboxylate-bridged diiron center**; DMQ binding mediates reduction of the diiron center by
  NADH and initiates O2 activation for subsequent DMQ hydroxylation. This is a **di-iron**, NOT a
  flavin, enzyme. [PMID:23445365 "GB1-hCLK-1 functions as a 5-demethoxyubiquinone-hydroxylase,
  utilizing its carboxylate-bridged diiron center"; "The binding of DMQn (n = 0 or 2) to
  GB1-hCLK-1 mediates reduction of the diiron center by nicotinamide adenine dinucleotide (NADH)
  and initiates O2 activation for subsequent DMQ hydroxylation."]

## COQ synthome / partners

- Part of the eukaryotic **CoQ biosynthetic (COQ) metabolon / synthome** on the matrix face of the
  inner mitochondrial membrane, comprising COQ3, COQ4, COQ5, COQ6, COQ7, COQ9
  [PMID:38425362 "a composite of COQ proteins bands together on the matrix side of the inner
  mitochondrial membrane to build the final aromatic ring of CoQ. These include COQ3, COQ4, COQ5,
  COQ6, COQ7 and COQ9"]. GO:0110142 (ubiquinone biosynthesis complex) definition explicitly lists
  COQ3-7,9.
- **COQ9** is a lipid-binding protein that binds and presents the lipophilic DMQ substrate to COQ7
  [PMID:25339443 "COQ9 specifically interacts with COQ7 through a series of conserved residues";
  "suggesting that COQ9 might serve to present its bound lipid to COQ7"]. COQ9 boosts COQ7
  catalytic efficiency in vitro [PMID:38425362 "addition of COQ9 increased catalytic efficiency by
  1.5-fold, substantiating its role for COQ7 function"].
- In vitro reconstitution confirms COQ7 as the **NADH-dependent hydroxylase with a
  carboxylate-bridged diiron centre** converting substrate 5 to 6 (C6 step)
  [PMID:38425362 "COQ7 is an NADH-dependent hydroxylase that possesses a carboxylate-bridged diiron
  centre and converts 5 to 6"].
- UniProt SUBUNIT: interacts with COQ8B and COQ6 (PMID:24270420), COQ9 (PMID:25339443); IntAct
  binary partners COQ3, COQ4, COQ5, COQ6, COQ9. The cryo-EM structure is a multimeric
  COQ7:COQ9 octamer (PDB 7SSP/7SSS; PMID:36306796).
- Floyd et al. mito-interaction map identified the dynamic human CoQ biosynthetic complex
  [PMID:27499296 "we identified a dynamic human CoQ biosynthetic complex involving multiple MXPs"].

## Localization

- Canonical: **mitochondrion inner membrane**, peripheral membrane protein, matrix side
  [file:human/COQ7/COQ7-uniprot.txt "Mitochondrion inner membrane"]. Confirmed by ComplexPortal
  IDA (GO:0005743), Reactome TAS, and mito-proteome HTP (PMID:34800366, MitoCoP).
- A distinct **nuclear** pool of uncleaved COQ7/CLK-1 exists and has a moonlighting retrograde-
  signaling role independent of ubiquinone biosynthesis [PMID:25961505 "we have uncovered a
  distinct nuclear form of CLK-1 that independently regulates lifespan"; "COQ7 has a biologically
  relevant nuclear role that is independent of its characterised mitochondrial function in
  ubiquinone biosynthesis"]. This pool associates with chromatin
  [PMID:25961505 "the nuclear pool of COQ7 can directly associate with chromatin"] and modulates
  ROS metabolism and the UPRmt via gene expression. This is a genuine but non-core secondary
  function; the primary, disease-relevant function is the mitochondrial CoQ hydroxylase step.

## Disease

- **Primary CoQ10 deficiency-8 (COQ10D8, MIM:616733)**, autosomal recessive: decreased CoQ10 from
  loss of COQ7 hydroxylase activity; multisystem (renal, cardiac, neuropathy). Variants V141E,
  L111P, R107W, R54Q, Y149C etc. Pathogenic variants lower CoQ and enzyme activity
  [PMID:28409910 "both mutations lead to loss of protein stability and decreased levels of
  ubiquinone"]. DHB (2,4-dihydroxybenzoate) bypass can rescue.
- **Distal hereditary motor neuronopathy AR-9 (HMNR9, MIM:620402)** (PMID:36758993, 37392700).

## Annotation review orientation (GOA has 37 rows)

- **Core MF**: GO:0160224 3-demethoxyubiquinone 3-hydroxylase (NADH) activity — EXP (PMID:23445365),
  IDA (PMID:38425362), plus IBA/IEA. The GO term's reaction definition exactly matches the UniProt
  Rhea reaction. ACCEPT.
- **Iron ion binding**: GOA has only generic GO:0046872 metal ion binding (IEA-KW). The di-iron
  center is well documented; GO:0005506 iron ion binding is the accurate specific MF — propose in
  core_functions and MODIFY the metal-ion-binding IEA toward it. (No existing GO:0005506 row.)
- **Core BP**: GO:0006744 ubiquinone biosynthetic process — IDA (PMID:38425362), IMP (PMID:28409910),
  plus IBA/IEA/NAS. ACCEPT.
- **GO:0004497 monooxygenase activity** (IEA InterPro) and **GO:0016709** (IEA UniRule) are correct
  parent MF terms but less informative than GO:0160224 → MARK_AS_OVER_ANNOTATED (redundant generic
  parents; not wrong — COQ7 IS a monooxygenase; note it is di-iron, not flavin/heme).
- **GO:0005743 mitochondrial inner membrane** (many rows: IDA ComplexPortal, IBA, IEA, 6x Reactome
  TAS): correct core location. Accept the experimental/curated ones; the 6 Reactome TAS rows are
  redundant duplicates → KEEP_AS_NON_CORE (accurate but low added value). GO:0031314 extrinsic
  component of mitochondrial inner membrane (IEA) is a more precise topology consistent with
  "peripheral membrane protein; matrix side" → ACCEPT/KEEP.
- **GO:0005739 mitochondrion** (IEA, IDA PMID:25961505, HTP PMID:34800366): correct but less
  specific than inner membrane → KEEP_AS_NON_CORE.
- **GO:0005634 nucleus** (IBA, IEA-SubCell, EXP PMID:25961505, IDA LIFEdb) and **GO:0005694
  chromosome** (IEA-SubCell, EXP PMID:25961505): real moonlighting location (PMID:25961505) →
  KEEP_AS_NON_CORE. The IBA "is_active_in nucleus" is over-propagated to a mitochondrial enzyme
  family → MARK_AS_OVER_ANNOTATED.
- **GO:0110142 ubiquinone biosynthesis complex** (IPI, ComplexPortal PMID:27499296): correct
  complex membership → ACCEPT (in_complex in core_functions).
- **GO:0005515 protein binding** (5x IPI): all to COQ synthome partners (COQ9=O75208, COQ5=Q5HYK3,
  COQ3=Q9NZJ6, COQ6=Q9Y2Z9, COQ4=Q9Y3A0). Real but uninformative bare "protein binding" →
  MARK_AS_OVER_ANNOTATED (do NOT remove IPI; policy). The biology (COQ9 presenting substrate) is
  captured better as complex membership + substrate presentation.
- **GO:0008340 determination of adult lifespan** (IBA): CLK-1/clk-1 longevity is genuine in worm/
  mouse but is largely a consequence of altered CoQ/ROS, and a nuclear moonlighting effect
  (PMID:25961505) → KEEP_AS_NON_CORE.
- **GO:2000377 regulation of ROS metabolic process** (IBA): supported for the nuclear pool
  (PMID:25961505) → KEEP_AS_NON_CORE.
- **GO:0009410 response to xenobiotic stimulus** (IEA, Ensembl ortholog from rat Q63619): weak
  electronic ortholog transfer, not supported for human COQ7 core function →
  MARK_AS_OVER_ANNOTATED (electronic, do not REMOVE recklessly; keep as caution).
</content>
