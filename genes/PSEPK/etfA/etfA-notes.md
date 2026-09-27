# etfA (Q88F97) curation notes — PSEPK ETF alpha subunit

## Identity

- UniProt Q88F97, locus PP_4201, *Pseudomonas putida* KT2440
  (NCBITaxon:160488).
- RecName "Electron transfer flavoprotein subunit alpha"; AltName "Electron
  transfer flavoprotein large subunit"
  [file:PSEPK/etfA/etfA-uniprot.txt].
- Family: ["Belongs to the ETF alpha-subunit/FixB family."]
- Quaternary structure: ["Heterodimer of an alpha and a beta subunit."]
- Cofactor: ["Name=FAD; Xref=ChEBI:CHEBI:57692;"] — the alpha subunit carries
  the redox-active flavin. Domain support: Pfam PF00766 (ETF_alpha) + PF01012
  (ETF), InterPro IPR001308 (ETF_a/FixB), IPR014731 (ETF_asu_C).
- Genomic context: first gene of the canonical *etfA*(PP_4201)-*etfB*(PP_4202)-
  *etfQO*(PP_4203) locus, so both stages of the ETF relay are encoded together.

## Curation decisions and why

### GO:0009055 electron transfer activity, `enables` — ACCEPT (was MARK_AS_OVER_ANNOTATED)

The first draft marked this over-annotated on the grounds that electron
transfer is a property of the assembled alpha/beta carrier rather than of the
alpha polypeptide alone. That reasoning is defensible in the abstract but is
not how this repository or GO models obligate subunits, and applying it here
would have left etfA with no molecular-function term for its defining activity.

The repo's own completed ortholog reviews settle the ACCEPT call:
`genes/human/ETFA/ETFA-ai-review.yaml` ACCEPTs `enables GO:0009055` three
times over (IBA, InterPro2GO IEA, and IDA from PMID:9334218), and
`genes/human/ETFB/ETFB-ai-review.yaml` ACCEPTs it on the *beta* subunit and
calls it "the core molecular function of the ETF heterodimer, in which the beta
subunit is an integral partner".

One correction to an earlier draft of this note: those two reviews are *not* a
precedent for the `contributes_to_molecular_function` modelling. Both place
GO:0009055 directly in `molecular_function`
(`ETFA-ai-review.yaml` core_functions, `ETFB-ai-review.yaml` core_functions).
Recording it here as `contributes_to_molecular_function` is a deliberate
divergence — the single FAD of the bacterial heterodimer sits at the
alpha/beta interface, so neither polypeptide carries the activity alone — and
the YAML reasons now say so rather than citing a convention the human reviews
do not establish.

### GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase — KEEP_AS_NON_CORE (was MARK_AS_OVER_ANNOTATED)

ETFs are promiscuous acceptors, so the TreeGrafter term names one donor pathway
rather than the subunit's function. But an earlier draft called it
over-annotated while this same note, `PP_4203-notes.md`, and the PP_0312 review
all argued the opposite — that fatty-acid beta-oxidation is the likely major
donor pathway for this locus, since PP_4203 is the obligatory reoxidation node
for the organism's large acyl-CoA dehydrogenase repertoire, and that rejecting
GO:0033539 on PP_0312 depends on those electrons arriving here instead. That is
an internal contradiction: MARK_AS_OVER_ANNOTATED asserts the term overshoots,
which this synthesis denies.

KEEP_AS_NON_CORE is what the evidence actually supports. The involvement is
legitimate on the electron-acceptor basis that `genes/human/ETFB` uses for the
same term; it is non-core because the donor-acceptor pairing has not been
demonstrated experimentally in KT2440 and this ETF is not dedicated to
beta-oxidation. See `genes/PSEPK/PP_4203/PP_4203-notes.md`.

### GO:0050660 flavin adenine dinucleotide binding — ACCEPT

Direct cofactor property of the alpha polypeptide, asserted in the local record
and consistent with the family's FAD-binding architecture.

## Open questions

- Which flavoprotein dehydrogenases actually reduce the EtfAB pair in KT2440,
  and whether donor preference differs from that of the second ETF pair
  PP_0312/PP_0313 (see those notes: the adjacent dgcAB genes point at
  methylated-glycine oxidation for the second pair).
- No experimental data exist for this protein; every annotation is electronic.
  Reconstituting EtfAB with a candidate acyl-CoA dehydrogenase and with PP_4203
  would convert the whole locus from inference to evidence.
