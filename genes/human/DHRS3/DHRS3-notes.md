# DHRS3 (Short-chain dehydrogenase/reductase 3; retSDR1 / RDH17 / SDR16C1) — review notes

UniProt: O75911 (DHRS3_HUMAN), 302 aa, HGNC:17693, gene on chromosome 1.

## Core biochemistry

DHRS3 is a microsomal, membrane-bound short-chain dehydrogenase/reductase (SDR) that
catalyzes the **NADPH-dependent reduction of all-trans-retinaldehyde to all-trans-retinol**.

- UniProt FUNCTION: "Catalyzes the reduction of all-trans-retinal to all-trans-
  retinol in the presence of NADPH." [file:human/DHRS3/DHRS3-uniprot.txt]
- UniProt CATALYTIC ACTIVITY: "Reaction=all-trans-retinol + NADP(+) = all-trans-retinal + NADPH +
  H(+); ... EC=1.1.1.300; Evidence={ECO:0000269|PubMed:9705317}" [file:human/DHRS3/DHRS3-uniprot.txt]
- This maps exactly to GO:0052650 all-trans-retinol dehydrogenase (NADP+) activity
  (def: "all-trans-retinol + NADP+ = all-trans-retinal + NADPH + H+"; OLS-verified MF).
- The enzyme uses **NADPH**, not NADH; the IBA GO:0004745 "all-trans-retinol dehydrogenase
  (NAD+) activity" therefore has the wrong cofactor and should be MODIFIED to GO:0052650.
- Cofactor: UniProt KW "NADP"; a classical Rossmann fold for nucleotide binding was predicted
  by homology modeling: "predicted a classical Rossmann fold for the nucleotide binding"
  [PMID:9705317]. Supports GO:0050661 NADP binding as the specific cofactor-binding MF
  (the existing GO:0000166 nucleotide binding is the uninformative parent).

## Original characterization (PMID:9705317, Haeseleer et al. 1998; abstract only, full_text_available: false)

- Cloned "retSDR1", an SDR that reduces all-trans-retinal; "localizes predominantly in cone
  photoreceptors" and "retSDR1 expressed in insect cells displayed substrate specificities of
  the photoreceptor all-trans-retinol dehydrogenase." [PMID:9705317]
- "Homology modeling of retSDR1 using the carbonyl reductase structure as a scaffold predicted
  a classical Rossmann fold for the nucleotide binding, and an N-terminal extension that could
  facilitate binding of the enzyme to the cell membranes." [PMID:9705317]
- "The presence of retSDR1 in a subset of inner retinal neurons and in other tissues suggests
  that the enzyme may also be involved in retinol metabolism outside of photoreceptors."
  [PMID:9705317] — i.e. the retina/visual role is only one context; retinol metabolism is the
  general function.
- The GOA TAS annotations attributed to this paper for GO:0009055 electron transfer activity
  and GO:0000166 nucleotide binding are legacy over-general mappings: the abstract describes a
  retinaldehyde reductase (hydride transfer to/from NADP), not a dedicated electron carrier,
  and "nucleotide binding" is the uninformative parent of NADP binding.

## Role in retinoic-acid homeostasis and development (PMID:40519748, Hashimoto et al. 2025; full_text_available: true)

- DHRS3 opposes the retinaldehyde dehydrogenases: "dehydrogenase/reductase 3 (DHRS3, also named
  SDR16C1; encoded by DHRS3, HGNC:17693) is the major embryonic enzyme catalyzing the opposite
  reaction (RAL to ROL)." [PMID:40519748]
- Physiological role = buffering RA synthesis; the paper's abstract frames DHRS3 as "limiting
  excessive RA synthesis." [PMID:40519748] Loss of DHRS3 therefore *raises* RA:
  "Cells transfected with a DHRS3-Val171Met construct exhibited reduced retinaldehyde reduction
  capacity compared with wild-type, yielding reduced retinol and elevated RA" [PMID:40519748].
- Mutually activating complex with RDH10 in the ER membrane: "RDH10 and DHRS3 function together
  as a molecular complex inserted within the membrane of the endoplasmic reticulum." [PMID:40519748]
  This supports the ER-membrane localization (GO:0005789).
- Biallelic hypomorphic DHRS3 variants cause a novel RA embryopathy (coronal craniosynostosis,
  facial dysmorphism, congenital heart disease, scoliosis); mouse Dhrs3-/- is embryonic-lethal
  with ~40% increased embryonic RA. This is the IMP evidence (ECO:0000315) for the GOA
  annotation GO:0002138 retinoic acid biosynthetic process (involved_in). Because DHRS3's direct
  action drains the retinaldehyde pool and thus *down*-regulates RA synthesis, its participation
  in the RA pathway is regulatory/negative; GO:1900053 negative regulation of retinoic acid
  biosynthetic process is a biologically more precise term for the developmental phenotype,
  but per policy the experimental IMP annotation is retained (not removed).

## Retinoic-acid inducibility and expression (PMID:11861404, Cerignoli et al. 2002; not cited in GOA seed)

- UniProt INDUCTION: "By retinoic acid." [file:human/DHRS3/DHRS3-uniprot.txt] — this makes DHRS3
  a RA-inducible negative-feedback buffer on RA levels.
- UniProt TISSUE SPECIFICITY: "Widely expressed ... In the retina, expressed in cone but not rod
  outer segments." [file:human/DHRS3/DHRS3-uniprot.txt]
- UniProt MISCELLANEOUS: located in a chromosome-1 region often deleted in aggressive
  neuroblastoma. [file:human/DHRS3/DHRS3-uniprot.txt]

## Subcellular localization

- UniProt SUBCELLULAR LOCATION: "Membrane {ECO:0000305}; Multi-pass membrane protein
  {ECO:0000305}." [file:human/DHRS3/DHRS3-uniprot.txt] Four predicted TM helices (FT TRANSMEM
  9..29, 170..190, 195..215, 253..273).
- ER membrane is the informative curated location (Reactome R-HSA-5419165; and the RDH10/DHRS3
  complex is ER-membrane-inserted per PMID:40519748). GO:0016020 membrane (IEA subcell mapping)
  is correct but is the general parent of GO:0005789 endoplasmic reticulum membrane.
- Reactome R-HSA-2465940 places the atRAL->atROL reduction step at the photoreceptor outer
  segment membrane in the visual (retinoid) cycle; retina-specific, non-core.

## Annotation decision summary

| Term | Evid | Action | Rationale |
|------|------|--------|-----------|
| GO:0052650 all-trans-retinol dehydrogenase (NADP+) activity | EXP/TAS/IEA | ACCEPT (core MF) | matches EC 1.1.1.300 / UniProt reaction |
| GO:0004745 (NAD+) activity | IBA | MODIFY -> GO:0052650 | wrong cofactor (enzyme is NADPH-dependent) |
| GO:0000166 nucleotide binding | TAS | MARK_AS_OVER_ANNOTATED | uninformative parent; better = GO:0050661 NADP binding |
| GO:0009055 electron transfer activity | TAS | MARK_AS_OVER_ANNOTATED | reductase, not electron carrier |
| GO:0001523 retinoid metabolic process | IBA/TAS | ACCEPT | correct pathway context |
| GO:0042572 retinol metabolic process | TAS | ACCEPT (core BP) | direct product/substrate |
| GO:0002138 retinoic acid biosynthetic process | IMP | KEEP_AS_NON_CORE | experimental; DHRS3 negatively regulates RA synthesis |
| GO:0048385 regulation of RAR signaling | IBA | KEEP_AS_NON_CORE | downstream of RA-level control |
| GO:0007601 visual perception | TAS | KEEP_AS_NON_CORE | retina/cone context only |
| GO:0005789 endoplasmic reticulum membrane | TAS | ACCEPT (core loc) | RDH10/DHRS3 ER complex |
| GO:0016020 membrane | IEA | KEEP_AS_NON_CORE | correct but general parent of ER membrane |
| GO:0005811 lipid droplet | IBA | KEEP_AS_NON_CORE | family-level; plausible for lipid-metabolizing SDR |
| GO:0042622 photoreceptor outer segment membrane | TAS | KEEP_AS_NON_CORE | retina-specific visual-cycle context |

## Core functions

- MF: GO:0052650 all-trans-retinol dehydrogenase (NADP+) activity (retinaldehyde reductase, EC 1.1.1.300)
- MF: GO:0050661 NADP binding (cofactor)
- BP: GO:0042572 retinol metabolic process / GO:0001523 retinoid metabolic process; regulatory role in retinoic-acid homeostasis (buffering RA synthesis, essential in development)
- CC: GO:0005789 endoplasmic reticulum membrane
</content>
</invoke>
