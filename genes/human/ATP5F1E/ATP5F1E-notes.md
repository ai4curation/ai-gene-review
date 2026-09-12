# ATP5F1E (P56381) review notes

Human ATP synthase F1 subunit epsilon, mitochondrial. HGNC:838 (former symbol ATP5E).
51-aa nuclear-encoded protein, chr 20q13.3. Evidence at protein level.

## Function / structure

- Epsilon is the smallest subunit of the F1 catalytic head of mitochondrial
  ATP synthase (Complex V, F1Fo-ATP synthase). It is one of the three central-stalk
  subunits (gamma, delta, epsilon) that rotate inside the F1 head and couple proton
  translocation through Fo to ATP synthesis in F1.
  UniProt SUBUNIT: "linked by a central stalk (subunits gamma, delta, and epsilon)
  rotating inside the F1 region" [file:human/ATP5F1E/ATP5F1E-uniprot.txt].
- It is a **structural, non-catalytic** subunit — the catalytic sites are on the
  alpha3beta3 head. Hence GOA uses `contributes_to` for the rotational-mechanism MF
  (GO:0046933), not `enables`.
- Cryo-EM structure of the human ATP synthase resolves epsilon (chain I) in the central
  stalk [PMID:37244256 "Biological energy currency ATP is produced by F1Fo-ATP synthase";
  UniProt RN[11]].
- Immunocaptured functionally active human F1Fo contained a full complement of subunits;
  complex V displayed oligomycin/IF1-sensitive ATP hydrolysis
  [PMID:12110673 "immunoprecipitated F(1)F(0) contained a full complement of";
  "captured complex V displayed ATP hydrolysis activity that was"].
  In vivo the enzyme synthesizes ATP; ATP-hydrolase activity is an artificial in-vitro
  reversal (UniProt FUNCTION).

## Assembly role

- Knockdown/mutation of epsilon reduces the assembled ATP synthase and causes
  accumulation of subunit c, indicating a role in F1 biogenesis and incorporation of
  subunit c into the rotor [PMID:20566710 "essential role of the epsilon subunit in the
  biosynthesis and assembly of the F1"; "incorporation of subunit c to the rotor structure
  of the mammalian"]. (PMID:20026007, Havlickova 2010, same finding by knockdown; not cached.)
- Central rotor shaft (F1-c-ring) and stator stalk (b-e-g) assemble as separate
  intermediates before joining [PMID:26297831 "the central rotor shaft and the stator
  stalk are formed"].

## Disease

- Mitochondrial complex V (ATP synthase) deficiency, nuclear type 3 (MC5DN3; MIM 614053).
  Homozygous p.Tyr12Cys in ATP5E; neonatal onset, lactic acidosis, 3-methylglutaconic
  aciduria, peripheral neuropathy; patient fibroblasts show 60-70% decrease in
  oligomycin-sensitive ATPase activity and mitochondrial ATP synthesis
  [PMID:20566710 "3-methylglutaconic aciduria, mild mental retardation and developed
  peripheral"; "Patient fibroblasts showed 60-70% decrease"; "first case of a mitochondrial
  disease due to a mutation in a nuclear ... encoded structural subunit of the ATP synthase"].
  Second family / variable neurologic phenotype PMID:34954817 (not cached).

## Localization

- Mitochondrial inner membrane / matrix face; part of Complex V embedded in the inner
  membrane. GO:0005743 (inner membrane) is the anatomical location. GO:0005759
  (matrix, Reactome TAS) is compatible (the F1 head with epsilon projects into the matrix)
  but the specific structural location for the complex is the inner membrane.

## Annotation-review decisions (summary)

- Core: located_in GO:0005743 (inner membrane); part_of GO:0045259 (proton-transporting
  ATP synthase complex, current term the GOA carries); involved_in GO:0042776 / GO:0015986
  (proton motive force-driven ATP synthesis); contributes_to GO:0046933 (rotational MF).
- `enables GO:0046933` (IEA/InterPro) over-annotates: epsilon is non-catalytic, so
  `contributes_to` is correct, not `enables`. MARK_AS_OVER_ANNOTATED.
- Bare `protein binding` GO:0005515 IPIs (interactome high-throughput; partner ATP5F1D /
  AGTRAP) — uninformative; MARK_AS_OVER_ANNOTATED per curation policy (do not REMOVE IPIs).
- core MF: GO:0005198 structural molecule activity (non-catalytic structural subunit) as
  the directly-enabled MF, plus contributes_to GO:0046933.
</content>
</invoke>
