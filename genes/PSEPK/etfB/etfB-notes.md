# etfB (Q88F96) curation notes — PSEPK ETF beta subunit

## Identity

- UniProt Q88F96, locus PP_4202, *Pseudomonas putida* KT2440
  (NCBITaxon:160488).
- RecName "Electron transfer flavoprotein subunit beta"; AltName "Electron
  transfer flavoprotein small subunit" [file:PSEPK/etfB/etfB-uniprot.txt].
- Family: ["Belongs to the ETF beta-subunit/FixA family."]
- Quaternary structure: ["Heterodimer of an alpha and a beta subunit."]
- Cofactor: ["Name=AMP; Xref=ChEBI:CHEBI:456215;"] — AMP, not a flavin. The
  beta subunit carries no redox centre of its own; it supplies the structural
  scaffold and the docking surface for partner dehydrogenases. Domain support:
  Pfam PF01012 (ETF), InterPro IPR012255 (ETF_b), IPR033948 (ETF_beta_N).
- Genomic context: middle gene of the *etfA*(PP_4201)-*etfB*(PP_4202)-
  *etfQO*(PP_4203) locus.

## Curation decisions and why

### GO:0009055 electron transfer activity, `enables` — ACCEPT (was MARK_AS_OVER_ANNOTATED)

The over-annotation call was the harder one to reverse here, because EtfB
genuinely has no flavin and cannot transfer an electron on its own. But GO's
convention for an obligate subunit of a multi-protein carrier is to type the
subunit with the complex's activity and record the dependency separately, and
the repo's completed ortholog review is unambiguous on exactly this protein:
`genes/human/ETFB/ETFB-ai-review.yaml` ACCEPTs `enables GO:0009055` with the
reason that "electron transfer activity is the defining, experimentally
established molecular function of the ETF complex … and ETFB is an obligate
structural/recognition component of the electron-transferring heterodimer".

Marking it over-annotated would have left this gene with **no
molecular-function term at all** — the worst outcome, since the annotation is
not wrong about what EtfB is for. The subunit-level qualification lives in
`core_functions` as `contributes_to_molecular_function`, which was already
present and is unchanged.

### GO:0046395 carboxylic acid catabolic process — kept as MARK_AS_OVER_ANNOTATED, reason rewritten

The original reason said the record "does not identify the physiological donor
dehydrogenase or a particular carboxylic-acid catabolic pathway". That is too
flat: the etfA-etfB-PP_4203 locus does sit at the convergence point of KT2440's
large acyl-CoA dehydrogenase repertoire, so carboxylic-acid catabolism is not
wrong in substance. The objection is narrower and now stated as such —
GO:0046395 is a very broad pathway-level term reached electronically, and
EtfB's own contribution is the upstream electron-carrier step rather than any
carboxylic-acid catabolic reaction. This is the CLAUDE.md "does the gene product
do any of the work of that process" test: it does not.

## Open questions

- Does the AMP in the beta subunit have a regulatory role in the bacterial
  enzyme, or is it purely structural as in the mammalian ETF?
- Which dehydrogenases dock on EtfB in KT2440. The beta subunit is the
  recognition surface, so donor specificity is more likely determined here than
  on EtfA.
