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
genuinely has no flavin and cannot transfer an electron on its own. But an
obligate subunit of a multi-protein carrier is reasonably typed with the
complex's activity, and the repo's completed ortholog review is unambiguous on
exactly this protein:
`genes/human/ETFB/ETFB-ai-review.yaml` ACCEPTs `enables GO:0009055` with the
reason that "electron transfer activity is the defining, experimentally
established molecular function of the ETF complex … and ETFB is an obligate
structural/recognition component of the electron-transferring heterodimer".

Marking it over-annotated would have left this gene with **no
molecular-function term at all** — the worst outcome, since the annotation is
not wrong about what EtfB is for. The subunit-level qualification lives in
`core_functions` as `contributes_to_molecular_function`.

Note that the human review is *not* a precedent for that modelling: it places
GO:0009055 directly in `molecular_function`. Using
`contributes_to_molecular_function` here is a deliberate divergence, because
the heterodimer's single FAD is contributed by EtfA and EtfB supplies the
partner-recognition surface and the structural AMP rather than the redox
centre. The YAML reason now states this instead of citing a convention the
human review does not establish. With GO:0016208 added (below), this core
function also carries the subunit-specific `molecular_function` the schema asks
for alongside `contributes_to_molecular_function`.

### GO:0046395 carboxylic acid catabolic process — kept as MARK_AS_OVER_ANNOTATED, reason rewritten

The original reason said the record "does not identify the physiological donor
dehydrogenase or a particular carboxylic-acid catabolic pathway". That is too
flat: the etfA-etfB-PP_4203 locus does sit at the convergence point of KT2440's
large acyl-CoA dehydrogenase repertoire, so carboxylic-acid catabolism is not
wrong in substance.

An earlier draft of this note justified the call by arguing that EtfB's own
contribution is the upstream electron-carrier step rather than a
carboxylic-acid catabolic reaction, and backed that up with a paraphrase
attributed to project guidance. Both have been removed: the argument does not
need a project rule quoted at it, and no paraphrase should have been presented
as one. On GO's own `involved_in` semantics an obligate electron acceptor for a
pathway's dehydrogenases does part of the work of that pathway, and the human
ortholog review treats ETFB's involvement in GO:0033539 on exactly that basis
(`genes/human/ETFB/ETFB-ai-review.yaml`).

The objection that survives is breadth, not participation. GO:0046395 is a
high-level grouping term reached electronically that covers every carboxylic
acid the organism degrades, including the many routes that never pass through
an ETF; a specific donor-pathway term such as GO:0033539 carries the same claim
without the over-reach. That is why the annotation is now `MODIFY` →
GO:0033539 rather than `MARK_AS_OVER_ANNOTATED`: marking it over-annotated
would have left EtfB with no biological-process term while its obligate partner
etfA keeps GO:0033539 from GOA. As on etfA, GO:0033539 stays out of
`core_functions` — the donor-acceptor pairing is not demonstrated in KT2440.

### GO:0016208 AMP binding — added as NEW

`etfB-uniprot.txt` carries `COFACTOR Name=AMP; Xref=ChEBI:CHEBI:456215`
(ARBA00049933) but GOA has no AMP-binding term for Q88F96. AMP is the canonical
structural cofactor of the ETF beta subunit — the GO definition of GO:0045251
electron transfer flavoprotein complex itself says the complex "usually
contains an alpha and a beta subunit and the structural cofactor adenosine
monophosphate (AMP)". Added as NEW/ISS, parallel to the GO:0050660 gap filled on
PP_4203 in this batch. It also gives this core function a subunit-specific
`molecular_function`, which the schema asks for whenever
`contributes_to_molecular_function` is used. PP_0313 has no COFACTOR line, so no
equivalent term is proposed there; see `PP_0313-notes.md`.

## Open questions

- Does the AMP in the beta subunit have a regulatory role in the bacterial
  enzyme, or is it purely structural as in the mammalian ETF?
- Which dehydrogenases dock on EtfB in KT2440. The beta subunit is the
  recognition surface, so donor specificity is more likely determined here than
  on EtfA.
