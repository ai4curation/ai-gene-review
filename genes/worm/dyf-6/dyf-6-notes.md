# dyf-6 (Q0G838) research notes

## Identity (from UniProt Q0G838, IFT46_CAEEL)

- **Gene**: dyf-6 (F46F6.4), WormBase WBGene00001122, chromosome X. "dyf" = abnormal **dye filling**.
- **Protein**: Intraflagellar transport protein 46 homolog (IFT46). 471 aa (isoform a). Human ortholog IFT46 = Q9NQC8; mouse Q9CQ63 (used in IBA WITH/FROM).
- **Domain/family**: PANTHER PTHR13376 (INTRAFLAGELLAR TRANSPORT PROTEIN 46 HOMOLOG); Pfam PF12317 (IFT46_B_C); InterPro IPR022088 (Intraflagellar_transp_cmplxB). Large N-terminal disordered/acidic region (res 1–202); no catalytic domain. So DYF-6 is **MF-dark**: a structural/adaptor subunit of IFT-B with no assigned molecular activity (unlike its worm paralog-family neighbor dyf-11/IFT54, which carries an InterPro2GO microtubule-binding transfer — dyf-6 has NO MF annotation at all in GOA).
- **Complex**: Component of IFT complex B (ComplexPortal CPX-1290). UniProt SUBUNIT (from PMID:28479320): "Component of the IFT complex B composed of at least che-2, che-13, dyf-1, dyf-3, dyf-6, dyf-11, dyf-13, ift-20, ift-74, ift-81, ifta-2, osm-1, osm-5 and osm-6."
- **Localization** (UniProt, from PMID:16648645): Cell projection, cilium; Cytoplasm/cytoskeleton, cilium basal body; Cell projection, dendrite; Perikaryon. "Highly expressed in the transition zones between the cilium basal body and the dendrites."
- **Isoforms**: 4 (a Q0G838-1 displayed; b/c/d). dyf-6 is a complex locus; a longer mRNA fuses the dyf-6 ORF to the upstream gene F46F6.3 — the short forms confer full rescue and are the conserved/functional forms.

## KNOWN (well-supported)

1. **DYF-6 is an IFT (intraflagellar transport) protein that moves within cilia.**
   - [PMID:16648645 "Movement of DYF-6::GFP within the ciliated endings of the neurons indicates that DYF-6 is involved in IFT."]
   - [PMID:16648645 "Anterograde movement appeared more apparent than retrograde movement."]

2. **DYF-6 is (very likely) an IFT complex B component.** Bell 2006 inferred this from the OSM-6::GFP mislocalization pattern; Yi 2017/ComplexPortal biochemically place it in IFT-B.
   - [PMID:16648645 "dyf-6 may encode a component of complex B IFT particles"]
   - [PMID:16648645 "The pattern of OSM-6::GFP in dyf-6 mutants therefore more closely resembles that of a complex B IFT component."]
   - UniProt SUBUNIT + ComplexPortal CPX-1290 (from PMID:28479320) list dyf-6 in IFT-B.

3. **DYF-6 is required to build/maintain sensory cilia; loss foreshortens amphid & phasmid cilia.**
   - [PMID:16648645 "the cilia of the amphid and phasmid dendritic endings are foreshortened"]
   - C. elegans sensory cilia are **non-motile**, so the specific process term is non-motile cilium assembly (GO:1905515, WormBase IMP).

4. **DYF-6 acts cell-autonomously in the amphid sensory neurons; loss causes dye-filling/chemotaxis defects.**
   - [PMID:16648645 "genes that affect chemotaxis and the ability of certain sensory neurons to take up fluorescent dyes from the environment"]
   - [PMID:16648645 "genetic mosaic analysis, which indicates that dyf-6 functions in neurons of the amphid sensilla"]

5. **Expression**: DYF-6::GFP in amphid & phasmid (and IL-region) ciliated neurons, plus hypodermis; expressed hatching→adult incl. dauer.
   - [PMID:16648645 "DYF-6::GFP is expressed in amphid and phasmid neurons"]
   - [PMID:16648645 "IFT can be observed in dauer larvae"]

6. **Conservation**: orthologs in fly (CG15161, ciliary) and mammals; human ortholog conserved throughout.
   - [PMID:16648645 "DYF-6, the product of a complex locus, lacks known motifs, but orthologs are present in flies and mammals."]
   - [PMID:16648645 "the human ortholog is conserved throughout and begins at the same methionine"]

7. **DYF-6/IFT-B is needed for dynein-2 ciliary entry** (retrograde IFT context).
   - [PMID:28479320 "intraflagellar transport (IFT)-B complex abolishes dynein-2's ciliary localization"] (abstract-only cache; full text is the source of the IFT-B mass-spec membership)

## NOT known / gaps

- **Molecular function of DYF-6/IFT46 is undefined.** No catalytic domain; large disordered N-terminus. Which IFT-B subunit(s) it directly contacts in the worm, and whether it (like Chlamydomonas IFT46, which uses its N-terminal domain to load outer dynein arms) has a cargo-adaptor activity, is not established here. GO MF aspect cannot currently express "structural subunit of IFT-B" (ontology gap). [PMID:16648645 "DYF-6, the product of a complex locus, lacks known motifs"]
- **Function of the long dyf-6/F46F6.3 fusion isoform is unknown.** [PMID:16648645 "The function, if any, of the larger dyf-6 gene product remains unknown."]
- **Whether DYF-6 has any non-ciliary role** (it is also seen in dendrite/perikaryon/cell body) is untested.

## Annotation-review plan (19 GOA annotations)

- CORE (ACCEPT): intraciliary transport particle B (IBA part_of; NAS part_of), intraciliary transport (IBA/IEA/NAS/IDA involved_in), cilium assembly (IBA/NAS involved_in), non-motile cilium assembly (IMP involved_in), cilium (IEA/NAS located_in).
- MODIFY: microtubule organizing center (IBA is_active_in) → ciliary basal body GO:0036064 (documented basal-body/transition-zone localization).
- MARK_AS_OVER_ANNOTATED: motile cilium (IBA is_active_in) — C. elegans has NO motile cilia (mammalian-biased IBA over-propagation; worm cilia are non-motile sensory); plasma membrane bounded cell projection GO:0120025 (ARBA IEA) — over-general grouping parent of cilium+dendrite already annotated.
- KEEP_AS_NON_CORE (real but not core location/route): dendrite (IEA/IDA), perikaryon (IEA/EXP), neuronal cell body (IDA).

## Provenance note
Cache: PMID:16648645 full text available (Bell et al. 2006, Genetics, PMC1526656). PMID:28479320 abstract-only (Yi et al. 2017, Curr Biol) — IFT-B membership rests on full-text mass-spec not in cache; annotations from it are ComplexPortal NAS, accepted deferring to curator/ComplexPortal.

## Falcon deep research (dyf-6-deep-research-falcon.md, 2026-07-04) — additional context

Genuine, gene-correct report (40 citations, 2 artifacts). Key points that refine but do not
contradict the review:

- **IFT-B1 core architecture**: IFT46's conserved C-terminal IFT46_B_C domain (PF12317) directly
  binds IFT52, and IFT46–IFT52–IFT88 form a stable ternary core module of IFT-B1 (Lucker et al.
  2010 J Biol Chem; Lv et al. 2017 J Cell Sci; Taschner & Lorentzen 2016). So DYF-6 is not
  partner-less — but these interactions are characterized in Chlamydomonas/human, not the worm,
  and GO MF has no term for the structural role. [falcon: "IFT46 directly interacts with IFT52
  through large hydrophobic surfaces at their carboxy-terminal domains"]
- **Basal-body targeting**: IFT52 recruits IFT46 to the basal body; the IFT46 C-terminal BBTS3
  segment (~aa 246–321) is the basal-body/ciliary targeting sequence; L285/L286 are key for IFT52
  binding (Lv et al. 2017). Supports the MTOC→ciliary basal body MODIFY.
- **N-terminal ODA16 cargo-adaptor role is MOTILE-cilia-specific** (Chlamydomonas ODA transport),
  hence NOT expected in C. elegans non-motile sensory cilia — independent support for marking the
  IBA "motile cilium" annotation as over-annotated. [falcon: "the N-terminal region involved in
  ODA16 binding is specifically conserved in organisms with motile cilia"; "Since C. elegans
  possesses only non-motile sensory cilia that lack dynein arms, the ODA transport function of
  IFT46's N-terminus may be less relevant in nematodes"]
- **Worm-specific ARL-13 trafficking (NOT in GOA)**: Cevik et al. 2013 report that dyf-6 mutants
  mislocalize the Joubert-syndrome protein ARL-13/ARL13B (reduced in ciliary middle segment,
  accumulates at periciliary membrane), via the IFT46–IFT56 dimer that binds ARL13B (Nozaki et al.
  2017). This is a genuine dyf-6 functional finding but the primary papers are not in the
  publications cache, so it is recorded here as context only (not added as verbatim-supported
  annotation).
- **Transcriptional control**: ciliary genes incl. IFT-B are DAF-19/RFX (X-box) targets; dyf-6's
  Drosophila ortholog CG15161 is an RFX target (consistent with X-box regulation of ciliary genes).
- **Anthelmintic uptake**: dyf-6 among ciliary genes needed for avermectin uptake via amphid cilia
  (Brinzer et al. 2021) — a downstream/pleiotropic sensory readout, not a core function.

Not independently re-verified (LLM synthesis with internal citation keys); used as supporting
context. The two ontology/biology knowledge gaps in the review reflect this: partners known in
other species but (a) no GO MF term and (b) worm-specific contacts/adaptor role unproven.
