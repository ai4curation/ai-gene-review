# PFKM (human) review notes

UniProtKB: P08237. HGNC:8877. Muscle isoform of 6-phosphofructokinase (PFK-1), EC 2.7.1.11.

## Core biology (from UniProt P08237 + literature)

- Catalyzes the committed, rate-limiting step of glycolysis: ATP-dependent phosphorylation of
  D-fructose 6-phosphate to fructose 1,6-bisphosphate. [file:human/PFKM/PFKM-uniprot.txt "Catalyzes the phosphorylation of D-fructose 6-phosphate to fructose 1,6-bisphosphate by ATP, the first committing step of glycolysis."]
- Reaction: beta-D-fructose 6-phosphate + ATP = beta-D-fructose 1,6-bisphosphate + ADP + H+ (Rhea:16109, EC 2.7.1.11). Requires Mg2+ cofactor.
- Allosteric enzyme: activated by ADP, AMP, or fructose 2,6-bisphosphate; inhibited by ATP or citrate.
  [file:human/PFKM/PFKM-uniprot.txt "Allosterically activated by ADP, AMP, or fructose 2,6-bisphosphate, and allosterically inhibited by ATP or citrate."]
- Two-domain protein: N-terminal catalytic PFK domain 1 (res 2-390) and C-terminal regulatory PFK domain 2 (res 402-780); the C-terminal domain binds the F-2,6-BP allosteric activator.
- Active enzyme is a tetramer built from three subunit types (PFKM/muscle, PFKL/liver, PFKP/platelet).
  Muscle = M4 homotetramer; erythrocytes = mixture M4, M3L, M2L2, ML3, L4. [PMID:6444721]
- Cytoplasmic/cytosolic. [file:human/PFKM/PFKM-uniprot.txt "Cytoplasm"]

## Disease
- Glycogen storage disease type VII (Tarui disease, MIM:232800): exercise intolerance, muscle cramps,
  exertional myopathy and compensated hemolysis; caused by PFKM variants. M-subunit is absent/deficient;
  in erythrocytes only L4 remains. [PMID:6444532] [PMID:2960695] [PMID:7825568]

## Key experimental evidence in cached publications
- PMID:6444721 (Vora 1980, PNAS): five-membered PFK isozyme system from M and L subunits; muscle and
  liver PFKs are distinct homotetramers M4 and L4. Basis for the M4 complex + identical protein binding
  + kinase (PFKL) binding annotations. Abstract-only (full_text_available:false).
- PMID:6444532 (Vora 1980, Blood): molecular basis of Tarui disease; M-subunits absent in patient.
  Basis for IMP MF/BP/muscle homeostasis annotations. Abstract-only.
- PMID:7825568 (Raben 1995): functional expression of mutant PFK-M in yeast; Gly209Asp completely
  inactive. Direct evidence PFKM confers 6-PFK activity. Abstract-only.
- PMID:2960695 (Vora 1987): late-onset PFK-M deficiency, "leaky" mutation. Abstract-only.
- PMID:24817713 (Kloos 2014): crystallization of human muscle PFK, "the main regulator of glycolysis";
  catalyzes Mg-ATP-dependent formation of F1,6BP from F6P; full text available. Basis for M4 complex (ComplexPortal).
- PMID:8780720 (Durante 1996): isozyme analysis of leukocyte PFK; kinetics incl. F-6-P affinity, ATP
  inhibition. Abstract-only. UniProt cites as IDA for 6-PFK activity, ATP binding, fructose binding.
- PMID:25796446 (Enzo 2015, EMBO J): PFK1 binds YAP/TAZ cofactors TEADs and promotes their activity;
  aerobic glycolysis tunes YAP/TAZ. Source of nucleus/positive-reg-transcription/kinase-related IPIs (CAFA).
  Abstract-only. Moonlighting/context-dependent, not core muscle glycolytic function.
- PMID:12649290 (Su 2003): a4/a1 subunit of V-ATPase interacts with PFK-1; PFK-1 co-immunolocalized at
  apical membrane of alpha-intercalated cells (kidney). Source of apical plasma membrane IDA + protein binding IPI.
  Abstract-only. Kidney-specific localization, non-core for muscle enzyme.

## Interactome (bare protein binding IPIs — high-throughput)
- PMID:21988832, 25416956, 28514442, 33961781, 36115835: proteome-scale interactome screens
  (liver PPI map, HuRI, BioPlex 2.0/3.0, fragmentomics/PDZ affinity). Many PDZ-domain partners in
  UniProt INTERACTION block (DLG1-4, MAGI1/2, SCRIB, PATJ, etc.) — mostly high-throughput; treat bare
  "protein binding" as uninformative -> MARK_AS_OVER_ANNOTATED (do not REMOVE per policy).

## Annotation decisions summary
- ACCEPT core: 6-PFK activity (all evidence codes), ATP binding, F6P binding, fructose binding,
  glycolytic process / canonical glycolysis / F6P & F1,6BP metabolic process, 6-PFK complex (M4),
  cytosol. phosphofructokinase activity (GO:0008443, parent of 0003872) ACCEPT (broader IEA is fine).
- KEEP_AS_NON_CORE: muscle cell cellular homeostasis (IMP, downstream physiology); glycolytic process
  through fructose-6-phosphate (specific but fine).
- MARK_AS_OVER_ANNOTATED: bare protein binding IPIs; identical protein binding & kinase binding
  (informative-ish but peripheral to core enzyme function — kept but non-core); apical plasma membrane
  (kidney-specific, IDA but not muscle enzyme core); membrane (IBA, is_active_in); nucleus + positive
  regulation of transcription by RNA pol II (moonlighting, CAFA IMP, context-specific/non-core);
  sperm principal piece (mouse-transfer IEA).
