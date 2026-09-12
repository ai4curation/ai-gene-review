# HSD3B7 (Q9H2F3) review notes

Human 3 beta-hydroxysteroid dehydrogenase type 7 / 3-beta-hydroxy-Delta(5)-C27-steroid
oxidoreductase (C27 3beta-HSD). EC 1.1.1.181. HGNC:18324. Chromosome 16p11.2-12.

## Established biology (provenance)

- **Second enzyme of bile-acid biosynthesis.** Acts on the 7alpha-hydroxylated sterols
  produced by CYP7A1/CYP7B1, oxidising the 3-beta-hydroxyl and isomerising the Delta5
  double bond so that 7alpha-hydroxycholesterol -> 7alpha-hydroxy-4-cholesten-3-one
  (a 3-oxo-Delta4 intermediate). Confirmed in vivo by loss-of-function disease
  [PMID:11067870 abstract, "a single C(27) 3beta-HSD enzyme can participate in all known
  pathways of bile acid synthesis"; Reactome R-HSA-192097 "7alpha-hydroxycholesterol and
  NAD+ react to form 4-cholesten-7alpha-ol-3-one, NADH, and H+, in a reaction catalyzed by
  HSD3B7"].
- **Substrate specificity is C27 bile-acid precursors, not steroidogenic C19/C21 steroids.**
  Active against four 7alpha-hydroxylated sterols; does not metabolise C19/21 steroids
  [PMID:11067870, "active against four 7alpha-hydroxylated sterols"; "The expressed enzyme
  did not metabolize several different C(19/21) steroids as substrates"; UniProt Q9H2F3
  "HSD VII is active against four 7-alpha-hydroxylated sterols. Does not metabolize several
  different C(19/21) steroids as substrates"]. This distinguishes it from the steroidogenic
  paralogs HSD3B1/HSD3B2 (which it shares only 34% identity with).
- **Localisation: endoplasmic reticulum membrane, multi-pass.** [UniProt Q9H2F3 SUBCELLULAR
  LOCATION "Endoplasmic reticulum membrane; Multi-pass membrane protein"; two predicted TM
  helices 289-309, 311-331; PMID:11067870 "microsomal"]. HPA reports a lipid-droplet IF
  signal (GO:0005811, IDA); ER is the primary, mechanistically-supported compartment.
- **Disease.** Congenital bile acid synthesis defect type 1 (CBAS1, MIM:607765): neonatal
  cholestasis, progressive liver disease, fat-soluble-vitamin malabsorption
  [PMID:11067870; PMID:12679481, characterised loss-of-activity variant E147K].
- **B-cell / lymphocyte positioning (by similarity).** Mouse ortholog Q9EQC1 degrades the
  EBI2/GPR183 ligand 7alpha,25-dihydroxycholesterol, shaping lymphoid chemotaxis gradients;
  human enzyme also acts on 7alpha,25-OHC in vitro (Rhea:RHEA:47156 in UniProt). The
  "B cell chemotaxis" (GO:0035754) annotations are transferred from mouse (ISS/IEA), a
  physiological consequence rather than the molecular function.

## Molecular function / pathway ids (verified in local go.db)
- GO:0003854 3-beta-hydroxy-Delta5-steroid dehydrogenase (NAD+) activity — core MF (GOA TAS Reactome; UniProt NAS).
- GO:0047016 cholest-5-ene-3-beta,7-alpha-diol 3-beta-dehydrogenase activity (EC 1.1.1.181) — specific MF (GOA EXP PMID:11067870).
- GO:0006699 bile acid biosynthetic process — core BP.
- GO:0005789 endoplasmic reticulum membrane — core CC.
- GO:0006694 steroid biosynthetic process — parent BP (IEA, retain as broad/non-core).
- GO:0016616 oxidoreductase acting on CH-OH, NAD/NADP acceptor — parent MF (IBA/IEA).

## Annotation judgments
- Bare `protein binding` (GO:0005515) IPIs from the two high-throughput interactome maps
  (PMID:25416956 HuRI/CCSB; PMID:32296183 HuRI) are uninformative for function ->
  MARK_AS_OVER_ANNOTATED (not REMOVE, per policy; experimental HT screens, not verifiable
  as functional).
- B cell chemotaxis (GO:0035754) ISS/IEA from mouse -> KEEP_AS_NON_CORE (real physiology,
  not HSD3B7's core catalytic role; transferred, not directly demonstrated in human).
- lipid droplet (GO:0005811) IDA/HPA -> KEEP_AS_NON_CORE (IF localisation; ER membrane is
  the mechanistically-supported primary compartment).
