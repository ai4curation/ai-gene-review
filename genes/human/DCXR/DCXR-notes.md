# DCXR (human, Q7Z4W1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: DCXR is the experimentally characterised 1:1 ortholog of zebrafish dcxr
(Q567K5) and will serve as the reference for transfer. ProtNLM2 output was not
opened or used.

### Deep research

`just deep-research-falcon human DCXR --fallback perplexity-lite` failed: falcon
did not return, and the perplexity-lite fallback timed out after 600 s. No
deep-research file exists. The review is based on the UniProt record and the
cached publications listed below.

### Evolutionary placement

- PANTHER PTHR44252 (D-ERYTHRULOSE REDUCTASE), subfamily PTHR44252:SF2
  (L-XYLULOSE REDUCTASE) [file:human/DCXR/DCXR-uniprot.txt "PANTHER; PTHR44252:SF2; L-XYLULOSE REDUCTASE; 1."].
  The zebrafish ortholog sits in SF3, the C. elegans dhs-21 protein also in SF3.
- PAINT node PTN001211870 carries four IBA terms that reach human DCXR:
  GO:0050038 L-xylulose reductase (NADPH) activity, GO:0004090 carbonyl
  reductase (NADPH) activity, GO:0005997 xylulose metabolic process and
  GO:0006006 glucose metabolic process. Human DCXR is itself an experimental
  donor (UniProtKB:Q7Z4W1 in WITH/FROM). The same four IBA terms reach zebrafish
  Q567K5 (genes/DANRE/dcxr/dcxr-goa.tsv), so these are the node-level claims.
- Not propagated by PAINT: D-glucuronate catabolic process (human IMP only),
  the brush-border/apical-membrane localisations (mouse IDA, reaching human by
  Ensembl Compara), and the quinone/ROS annotations from PMID:19442656. These
  rest on species-level evidence only and should not be transferred to other
  vertebrates as if PAINT had placed them.

### Experimental evidence in human

- Recombinant human DCXR (with mouse, rat, hamster, guinea pig) is a ~100 kDa
  homotetramer with NADPH-linked alpha-dicarbonyl reductase activity and
  xylitol/L-xylulose oxidoreductase activity [PMID:11882650 "The
  purified recombinant proteins of the five species were about 100-kDa
  homotetramers with NADPH-linked reductase activity for alpha-dicarbonyl
  compounds, catalyzed the oxidoreduction between xylitol and l-xylulose"].
  Abstract-only cache; kinetic constants are in UniProt (KM 0.21 mM L-xylulose,
  0.077 mM diacetyl, 0.002 mM NADPH).
- Crystal structures (1PR9, 1WNT, 3D3W) with NADP(H): Rossmann fold, SDR
  catalytic tetrad Asn107/Ser136/Tyr149/Lys153 conserved; Asn107 needed for
  coenzyme binding [PMID:15103634]. Tetramer held by Arg203-Cys244 salt bridges
  [PMID:15906319]. Reversible Cys138-Cys150 disulfide and S-cysteinylation
  modulate activity [PMID:19337691].
- Loss-of-function in human: pentosuria (Garrod's fourth inborn error).
  Homozygous/compound-heterozygous DCXR c.583delC and c.52+1G>A; no detectable
  enzyme, high serum xylulose [PMID:22042873].
- Pathway: DCXR reduces L-xylulose to xylitol in the glucuronate/pentose
  pathway, downstream of CRYL1 (L-gulonate 3-dehydrogenase) and C11orf54
  (beta-keto-L-gulonate decarboxylase) [PMID:40737316 "The product of the BKGD
  reaction is substrate of L-xylulose reductase (DCXR)."]. That paper also
  confirmed recombinant DCXR activity on xylitol/NADP+ by NMR.
- Identical protein binding (Y2H, HuRI) is consistent with the crystallographic
  homotetramer.
- P34H: human DCXR is the epididymal sperm-surface protein P34H, linked to
  sperm-zona pellucida interaction [PMID:10385429]; the function of the enzyme on
  sperm is unknown. Not annotated as process participation.

### Annotation decisions (summary)

- ACCEPT: L-xylulose reductase (NADPH) (all evidence), carbonyl reductase
  (NADPH), xylulose metabolic process, D-glucuronate catabolic process.
- KEEP_AS_NON_CORE: glucose metabolic process (pathway-level IBA), the
  localisation rows (cytosol, apical membrane, brush border, microvillus,
  acrosome, plasma membrane, exosome, mitochondrion), identical protein binding,
  quinone reductase activity from PMID:19442656.
- MODIFY: oxidoreductase activity, acting on CH-OH group of donors to the two
  specific activities.
- MARK_AS_OVER_ANNOTATED: positive regulation of ROS metabolic process (redox
  cycling of a xenobiotic quinone; the study attributes the effect to AKR1C3),
  nucleus (sperm-nucleus proteome), cytoplasmic microtubule (overexpression
  ORFeome localisation screen).
- REMOVE: bare protein binding (GLRX2 Y2H) per policy.
