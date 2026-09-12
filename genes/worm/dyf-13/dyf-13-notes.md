# dyf-13 (C. elegans) research notes

UniProt: Q95QT8 (IFT56_CAEEL). WormBase: WBGene00001129 / C27H5.7. Gene name from Starich
et al. 1995 dye-filling-defective screen.

## Molecular identity (verified from UniProt record)

- `RecName: Intraflagellar transport protein 56 homolog`; `AltName: Abnormal dye filling
  protein 13`. Belongs to the **IFT56 family** (SIMILARITY block). PANTHER family
  **PTHR14781 "INTRAFLAGELLAR TRANSPORT PROTEIN 56"**; InterPro **IPR030511 TTC26**.
- Therefore dyf-13 is the C. elegans ortholog of vertebrate **TTC26 / IFT56 / IFT-B protein
  56**. 574 aa, contains multiple **TPR repeats** (UniProt annotates TPR 1/2/3; Pfam
  PF14559 TPR_19; SUPFAM TPR-like). Architecture = tetratricopeptide-repeat (α-solenoid)
  scaffold protein, the canonical fold of many IFT-B peripheral subunits.
- Two isoforms by alternative splicing: Q95QT8-1 (displayed) and Q95QT8-2 ("b", VSP_057361,
  missing residues 1–22). No evidence of isoform-specific function.
- ComplexPortal: CPX-1290 "Intraflagellar transport complex B".

## KNOWN (well supported)

### Core identity: a novel core IFT component required for cilium function
- dyf-13 was cloned by Blacque et al. 2005 and shown to be the gene disrupted in dyf-13(mn396):
  [PMID:15916950 "we demonstrate that the ciliary structural defect of C. elegans dyf-13(mn396)
  mutants is caused by a mutation in C27H5.7a"]. The gene product **undergoes IFT** like other
  IFT proteins: [PMID:15916950 "One of these, C27H5.7a, encodes a ciliary protein that undergoes
  IFT. As with other IFT proteins, its ciliary localization and transport is disrupted by
  mutations in IFT and bbs genes."] Conclusion of that paper:
  [PMID:15916950 "DYF-13, an evolutionarily conserved protein, is a novel core IFT component
  required for cilia function."]

### Localization: cilium / undergoes IFT
- DYF-13::GFP is a bona fide IFT reporter that localizes along amphid channel cilia (TZ, middle
  and distal segments) and is transported: [PMID:18316409 "Localization of both DYF-1∷GFP (g1–g3)
  and DYF-13∷GFP (g1–g4) appears normal."] (used as an IFT reporter, strain Ex[DYF-13∷GFP]).
- UniProt SUBCELLULAR LOCATION: Cell projection, cilium (by similarity to mouse Q5PR66).
- ComplexPortal (NAS, PMID:28479320) locates it to the cilium.

### Part of IFT-B complex
- Yi et al. 2017 identified dyf-13 as a component of IFT complex B by affinity purification /
  mass spectrometry: UniProt SUBUNIT: "Component of the IFT complex B composed of at least che-2,
  che-13, dyf-1, dyf-3, dyf-6, dyf-11, dyf-13, ift-20, ift-74, ift-81, ifta-2, osm-1, osm-5 and
  osm-6" {ECO:0000269|PubMed:28479320}. The paper shows disruption of the IFT-B complex abolishes
  dynein-2's ciliary localization: [PMID:28479320 "Disruption of the dynein-2 tail domain, light
  intermediate chain, or intraflagellar transport (IFT)-B complex abolishes dynein-2's ciliary
  localization, revealing their important roles in ciliary entry of dynein-2."]
- Mammalian TTC26/IFT56 was assigned to the IFT-B core subcomplex by Katoh et al. 2016:
  [PMID:26980730 "we identified TTC26/IFT56 and Cluap1/IFT38, neither of which was included with
  certainty in previous models of the IFT-B complex, as integral components of the core and
  peripheral subcomplexes, respectively."]

### Function: anterograde transport / cilium assembly
- UniProt FUNCTION: "Component of the intraflagellar transport (IFT) complex B required for
  transport of proteins in the motile cilium (PubMed:15916950, PubMed:28479320). May be required
  for ciliary entrance and transport of specific ciliary cargo proteins such as che-3 which are
  related to motility (PubMed:28479320)." Note: the "motile cilium" phrasing is UniProt boilerplate
  transferred from the vertebrate ortholog; C. elegans sensory cilia are non-motile, but the
  IFT/assembly role is conserved.
- Disruption phenotype (structural): UniProt DISRUPTION PHENOTYPE "Structural cilia defect: cilia
  are short and lack distal portions." {ECO:0000269|PubMed:15916950}. Consistent with an IFT-B/
  anterograde defect (distal-segment loss).
- The dyf-13 mutant shows partial IFT-cargo defects: [PMID:18316409 "The dyf-13 mutant, similar to
  nphp-4 animals, occasionally lacks OSM-6∷GFP in amphid distal segments (Blacque et al., 2005;
  Ou et al., 2005)."]

### Dye-filling / sensory phenotype and X-box regulation
- Named for the Dyf (dye-filling defective) phenotype indicative of general cilium structural
  defects; part of the dyf-1..dyf-13 class: [PMID:16957054 "this class of ciliary mutants, which
  is comprised of 13 members, dyf-1 to dyf-13."] dyf-13 is a DAF-19/RFX X-box-regulated ciliary
  gene, cloned via the X-box motif: [PMID:16957054 "threedyfgenes (dyf-1,dyf-3anddyf-13) were
  cloned and their importance for the development of cilia has been demonstrated"].
- Conserved IFT component enriched in the Chlamydomonas flagellar proteome:
  [PMID:18369462 "several other proteins associated with and necessary for the function of the IFT
  machinery and cilium formation have been discovered in C. elegans , namely DYF-1 [32] DYF-2 [33],
  DYF-3 [34], DYF-13 [35], and IFTA-1 [36]. Like known IFT particle subcomplex A/B components,
  orthologs of these C. elegans proteins are enriched within the membrane-plus-matrix fraction of
  the recently identified Chlamydomonas flagellar proteome"].

## NOT known / open questions

- **Molecular activity beyond "IFT-B particle binding" is undefined.** dyf-13/TTC26/IFT56 is a
  TPR-scaffold subunit; which specific IFT-B subunit(s) it contacts and which cargo(es) it directly
  binds within the worm complex are not experimentally mapped. UniProt frames cargo specificity as
  a hypothesis ("May be required for ... transport of specific ciliary cargo proteins such as che-3").
  This is the classic structural-subunit MF-dark/ontology-gap situation described in
  projects/FUNCTION_KNOWLEDGE_GAPS.md.
- **Core vs. peripheral position of the worm protein is not directly determined.** Mammalian
  TTC26/IFT56 was placed in the IFT-B *core* by Katoh 2016 (PMID:26980730); whether C. elegans
  dyf-13 occupies the same sub-architectural position has not been shown biochemically.
- **No direct enzymatic activity** is expected or reported (TPR scaffold; no catalytic motifs).
- Basal body vs. ciliary-base pool: the IBA annotations place it at the ciliary basal body and
  ciliary base, but there is no worm-specific experimental sub-ciliary localization beyond
  "along the cilium".

## Annotation review orientation

GOA has 11 annotations:
- 6 IBA (GO_REF:0000033) from PANTHER PTHR14781: ciliary basal body, intraciliary transport
  particle B, intraciliary anterograde transport, intraciliary transport involved in cilium
  assembly, ciliary base, intraciliary transport particle B binding. All consistent with an
  IFT-B subunit — ACCEPT (the last three are core; basal body/base are supporting locations).
- 1 IEA (GO_REF:0000044, UniProt SubCell) cilium — ACCEPT (redundant with NAS cilium).
- 4 NAS (PMID:28479320, ComplexPortal): cilium, intraciliary transport particle B, intraciliary
  transport, cilium assembly. All consistent — ACCEPT; the two most specific (IFT particle B,
  cilium assembly / intraciliary transport) are core.

No REMOVE candidates: every annotation is on-pathway for an IFT-B/TTC26 ortholog. No experimental
annotations are being second-guessed. The IBA/NAS evidence is coherent with strong primary
experimental literature (PMID:15916950, PMID:28479320).

## References used
- PMID:15916950 Blacque et al. 2005, Curr Biol — cloning of dyf-13; core IFT component. HIGH.
- PMID:28479320 Yi et al. 2017, Curr Biol — dyf-13 in IFT-B by MS; IFT-B needed for dynein-2 entry. HIGH.
- PMID:18316409 Jauregui et al. 2008, JCB — DYF-13::GFP IFT reporter, cargo (OSM-6) defect. MEDIUM.
- PMID:16957054 Efimenko/Blacque et al. 2006, Mol Biol Cell — dyf gene class, X-box regulation. MEDIUM.
- PMID:18369462 Bacaj et al. 2008 (DYF-11), Curr Biol — DYF-13 as conserved IFT component. LOW/MEDIUM.
- PMID:26980730 Katoh et al. 2016, Mol Biol Cell — mammalian TTC26/IFT56 IFT-B architecture. MEDIUM (ortholog).
</content>
</invoke>

## Deep research (falcon / Edison) synthesis — added after review draft

A genuine falcon deep-research report (`dyf-13-deep-research-falcon.md`, Edison Scientific
Literature, ~28 min, 10 citations) completed and corroborates the review. Key points (its
internal citation keys, e.g. `ishikawa2014ttc26dyf13isan`, `xin2017ift56regulatesvertebrate`,
`zhang2012knockdownofttc26`, are falcon-internal and were NOT independently verified against
cached PMIDs, so they are not used as `supporting_text` in the YAML):

- IFT56/TTC26/DYF-13 is a **cargo-selective IFT-B adapter**, not an enzyme; TPR/α-solenoid
  scaffold. Placed in the IFT-B1 (B1b) branch (with IFT46, IFT52, IFT70, IFT88).
- Cross-species nuance: in *Chlamydomonas* and some vertebrate systems IFT56/TTC26 is
  **dispensable for basic IFT train assembly/motility** but required for import of a subset of
  cargo (notably motility-related axonemal proteins). This contrasts with the *C. elegans*
  dyf-13(mn396) structural phenotype (short cilia lacking distal segments; Blacque 2005,
  PMID:15916950), which the review anchors on. The species difference (cargo-selectivity vs.
  overt structural defect) is itself part of the open question about DYF-13's precise role.
- Vertebrate orthologs: mouse Ift56/hop mutants mislocalize Gli2/Gli3 (Hedgehog signaling);
  zebrafish ttc26 morphants have short photoreceptor/pronephric cilia; human TTC26/IFT56 linked
  to severe biliary ciliopathy. These are ortholog data, not C. elegans-specific.

This supports the two knowledge_gaps recorded (undefined direct cargo/partner contacts; core vs
peripheral sub-architecture of the worm protein) and the framing of DYF-13 as an IFT-B
structural/adapter subunit.
