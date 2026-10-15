# PFRA (P22225) notes — Trypanosoma brucei brucei 69 kDa paraflagellar rod protein (PFR2)

**Automated deep research was unavailable for this gene** (Falcon authentication and the
OpenAI key both failed in this environment). These notes are a manual literature review
based on the UniProt record, PubMed-verified primary papers and reviews cached in
`publications/`, and ontology lookups (OLS / local GO sqlite).

## Identity and naming

- UniProt P22225 (PFR1_TRYBB, "69 kDa paraflagellar rod protein", AltName PFR-A/PFR-B), 600 aa,
  encoded by two tandem genes with identical ORFs, PFRA and PFRB
  [file:TRYBB/PFRA/PFRA-uniprot.txt "Coded by two tandemly repeated genes with identical ORF:"].
- Naming caution: in T. brucei literature this protein (PFRA) corresponds to **PFR2** of the
  consolidated nomenclature (69 kDa band); the 73 kDa protein is PFRC = PFR1. Confirmed by
  the RNAi literature: the snl-2 line targets PFRA [PMID:10954429 "expresses linked inverted copies of a PFRA
  gene"], and Portman et al. call snl2 a PFR2 knockdown
  [PMID:19888464 "We compared the phenotype of snl4 with the previously described snl2 PFR2 knock down mutant"].
  The UniProt mnemonic PFR1_TRYBB is therefore confusing; anchor to the 69 kDa protein.
- The original cloning paper proposed that one 600-aa protein produced both the 73 and 69 kDa
  bands by conformational difference [PMID:2793936 "This PFR protein can assume two different
  conformations, resulting in two distinct bands"]. This was overturned:
  [PMID:19879876 "Subsequently, molecular evidence was presented for a simpler multigene explanation (Birkett et al., 1992) and a second gene was then characterised (Deflorin et al., 1994)."]
  and PFR1 and PFR2 are distinct paralogs from a duplication predating the
  Euglenida/Kinetoplastida split [PMID:19879876 "both proteins are the result of a single gene duplication event that predates the divergence of Euglenida and Kinetoplastida"].

## Structure / localisation

- Highly helical, coiled-coil-rich [PMID:2793936 "Secondary structure predictions indicate a very high helix content."];
  [PMID:34257277 "more than 80% of the protein is predicted to form helices"].
- The PFR is a trilaminar lattice alongside the axoneme inside the flagellum
  [PMID:19879876 "The Kinetoplastida PFR is a complex, trilaminar lattice-like structure with proximal, intermediate and distal domains defined"].
- Cryo-ET (Zhang et al. 2021) suggests PFR1/PFR2 coiled coils form the "wires" of the distal
  zone lattice [PMID:34257277 "suggesting that multiple subunits of PFR1 and PFR2 molecules could contribute to each arm of the wire"].
- GO has a specific CC term: GO:0097740 paraflagellar rod (part_of GO:0097729 9+2 motile cilium,
  thus part_of GO:0031514 motile cilium; NOT a descendant of GO:0005856 cytoskeleton in GO).

## Function (loss of function)

- PFRA RNAi (snl-1 / snl-2) in procyclic T. brucei: PFR construction fails, cells paralysed
  [PMID:10954429 "new PFRA RNA and PFRA protein quickly disappeared and PFR construction was affected, resulting in cell paralysis"].
- PFR is assembled distally and is a stable cytoskeletal structure
  [PMID:10954429 "The PFR is constructed by a polar assembly process at the distal end of the flagellum resulting in a stable cytoskeletal structure with low turn-over."].
- Non-redundant with PFR1 [PMID:34257277 "PFR1 and PFR2 are essential and non-redundant components of the PFR"].
- snl4 (PFR2 RNAi) [PMID:19888464 "Defective motility is clearly apparent and cells are completely paralysed."]
  and [PMID:19888464 "EM analysis shows that the PFR structure is greatly reduced"].
- Bloodstream form: PFR2 ablation is lethal (cytokinesis failure), in vitro and in mice
  [PMID:19879876 "ablation of PFR2 is lethal in the mammalian bloodstream form both in vitro in culture and in vivo in mouse infections"].
  This is likely an indirect consequence of motility loss — not a direct cytokinesis role.
- PFR2 is also required for incorporation of other PFR components (e.g. PAR1)
  [PMID:19879876 "is not assembled into the flagellum after RNA interference (RNAi – a mechanism that inhibits gene expression) ablation of PFR2"].
- Bastin et al. 1998 Nature letter (PMID:9468133) — "Paraflagellar rod is vital for
  trypanosome motility"; abstract-only cache has no text, used only as background.

## Calmodulin

- IEA calmodulin binding comes from InterPro IPR007824 (Flagellar_rod, Pfam PF05149). UniProt
  marks a predicted CaM-binding region 335-355 (ECO:0000255, sequence analysis only).
- Ridgley et al. 2000 (PMID:10960180; abstract not available in cache) — as summarised by
  Portman & Gull 2010: [PMID:19879876 "A possible interaction between Tryp-calmodulin and PFR1/2 was investigated by passing purified PFR proteins over a calmodulin-Sepharose column in the presence of calcium."]
  with caveats [PMID:19879876 "although the presence in the preparations of proteins of similar molecular weight such as PAR1 and PAR4 homologues may also explain these results"]
  and specificity [PMID:19879876 "PFR protein binding by calmodulin-Sepharose was sensitive to competition by the calmodulin binding peptide from calmodulin kinase II but not an irrelevant peptide"].
- CaM itself is required for PFR assembly [PMID:23787017 "Unexpectedly CaM depletion
  resulted in total and catastrophic failure in PFR assembly"]. Direct CaM binding by PFR2
  (vs PFR1, or co-purifying PAR proteins) is not resolved at the single-protein level.
  -> Calmodulin binding plausible but non-core; keep as non-core.

## Decisions

- GO:0005516 calmodulin binding (IEA InterPro): KEEP_AS_NON_CORE.
- GO:0005856 cytoskeleton (IEA SubCell): MODIFY -> GO:0097740 paraflagellar rod.
- GO:0031514 motile cilium (IEA): MODIFY -> GO:0097740 paraflagellar rod (part_of descendant).
- NEW: GO:0005198 structural molecule activity (core MF; structural constituent of PFR lattice).
  Not GO:0005200 structural constituent of cytoskeleton because that term occurs_in
  GO:0005856 cytoskeleton, and the PFR is not classified under cytoskeleton in GO.
- NEW: GO:0060285 cilium-dependent cell motility (PFR2 supplies the structure on which
  motility depends; RNAi paralysis). Did not add GO:0120268 paraflagellar rod assembly — as a
  structural subunit the assembly phenotype is the expected necessity phenotype; left as
  a suggested question.
- No animal/plant-only terms, no host-process terms, no RNA-editing/trypanothione issues here.

## Deliberately short supporting_text (do not "complete")

Two quotes in this review stop before the end of their source sentence on
purpose. Leave them as they are:

- PMID:34257277 `...major structural components of the PFR are two proteins,
  PFR1 and PFR2` — the source continues `PFR259,60.` where `59,60` are
  superscript reference markers flattened into the text. Completing the
  sentence invents a protein called PFR259. The next sentence of the same
  paragraph (quoted at the `GO:0060285` row) states the claim cleanly. This one
  was expanded and reverted twice.
- PMID:19888464 `EM analysis shows that the PFR structure is greatly reduced`
  — the cached paragraph runs straight into a DOI and a figure caption. Expanded
  once and reverted; the later DOI guard refused it, so it was not expanded again.
