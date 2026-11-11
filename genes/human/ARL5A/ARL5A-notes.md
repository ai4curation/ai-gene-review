# ARL5A (human, Q9Y689) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally characterised relative of
XENTR/F6WPT1 (Xenopus arl5a; same PANTHER subfamily PTHR11711:SF147, inside the
ARL5-clade PAINT node PTN000195484). No ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon human ARL5A --fallback perplexity-lite` failed: falcon
raised "Exception: Failed to authenticate" (Edison auth), and the perplexity-lite
fallback returned HTTP 401 "You exceeded your current quota". No deep-research
file exists. The review was built from cached primary literature read directly
(below), plus UniProt and the PTHR11711 family review.

### Evolutionary grounding

- PANTHER: PTHR11711 (ARF family). Subfamily PTHR11711:SF147 (vertebrate ARL5A);
  paralog ARL5B is SF146; invertebrate single-copy Arl5 (Drosophila Q9VSG8,
  C. elegans arl-5) is SF31 (`interpro/panther/PTHR11711/PTHR11711-review.yaml`).
- PAINT: PTN000195484 (ARL5 clade) asserts GO:0005802 trans-Golgi network (seed
  Drosophila Arl5) and GO:1903292 protein localization to Golgi membrane (seeds
  Drosophila Arl5, human ARL5A, human ARL5B). Deeper nodes PTN000917851 (GTP
  binding, cytoplasm) and PTN000918181 (vesicle-mediated transport,
  intracellular protein transport) are family-wide generic assertions.
- Human ARL5A is itself a seed of PTN000195484, so the TGN / GARP-recruitment
  function is grounded on the target's own experiments, not only transferred.

### What is experimentally established for human ARL5A itself

- Localisation to trans-Golgi: [PMID:22245584 "Here we show that Arl5a and Arl5b are
  localised to the trans-Golgi in mammalian cells"] (abstract only cached).
  [PMID:30478271 "C-terminally GFP-tagged wt, QL and TN mutant forms of Arl5a, Arl5b or
  mouse Arl5c ... localized to the Golgi, although TN form had reduced Golgi localization
  with concomitantly increased cytosolic pool"].
- GARP recruitment: Arl5a-GFP rescues GARP (myc-Vps54) TGN targeting after
  ARL5B knockdown [PMID:25795912 "When Arl5a-GFP was expressed in HeLa cells treated
  with Arl5b siRNA then it fully restored targeting of myc-Vps54 indicating that both
  proteins can direct GARP recruitment"]. ARL5A single knockdown had no effect in
  HeLa, attributed to low ARL5A abundance there (ARL5A not detected by proteomics in
  HeLa).
- ARL5A/ARL5B double KO abolishes GARP at the TGN and impairs TGN46 and STxB
  retrograde delivery [PMID:31575603]. These are paralog-combined data; ARL5A-only
  rescue in the KO was done with ARL5B, not ARL5A.
- ARMH3 effector: active (WT, Q70L) but not inactive (T30N) ARL5A binds ARMH3 in
  MitoID, Y2H and GST pulldown; ARL5A-ARMH3 bridges to PI4KB [PMID:39580461].
  ARMH3 activates PI4KB at the TGN; ARMH3 is not required for retrograde cargo
  transport. ARL5's role in PI4P synthesis is indirect (effector recruitment).
- Ragulator: GST-Arl5a pulls down Lamtor1-GFP; single shRNA depletion of Arl5a
  inhibited amino-acid-stimulated endosome-to-Golgi trafficking of CD8a-furin
  [PMID:30478271 "Single depletion of either Arl5a or Arl5b using alternative shRNAs
  resulted in similar inhibitory effect"]. Ragulator proposed as ARL5 GEF (not shown).
- Upstream activation: SYS1-ARFRP1 required for ARL5 membrane association
  [PMID:31575603].
- Structure: crystal structure of human ARL5 with bound GDP3'P [PMID:15896705];
  canonical G-domain switch; G1/G3/G4 motifs intact (family review g_domain site).
  No direct measurement of intrinsic GTP hydrolysis or a GAP/GEF for ARL5A found.

### Uncertain / not adopted

- PMID:12414990 (Lin et al. 2002, abstract only): "hARL5" nuclear/nucleolar,
  importin-alpha and HP1alpha binding. Mutants are named T35N and Q80L, which do
  not match ARL5A numbering (T30/Q70), so it is unclear which construct/protein
  this was; the nuclear role has not been reproduced by later work, which places
  ARL5A at the TGN. Not used for annotation; flagged as a question.
- PI4P synthesis / GOLPH3 recruitment: downstream of ARMH3/PI4KB; ARL5A does not
  perform the kinase step. Not proposed as process annotation (CLAUDE.md
  participation rule).

### Annotation decisions (summary)

- GTP binding (IBA, IEA): ACCEPT.
- GTPase activity (IEA): ACCEPT as the conventional MF for a nucleotide switch, noting
  hydrolysis is inferred (motifs intact; Q70L used as a GTP-locked mutant) not measured.
- trans-Golgi network (IBA): ACCEPT.
- cytoplasm (IBA): KEEP_AS_NON_CORE (cytosolic GDP pool).
- protein localization to Golgi membrane (IBA, IEA, IGI): ACCEPT (GARP and ARMH3
  recruitment to TGN).
- vesicle-mediated transport (IBA): MODIFY -> GO:0042147 retrograde transport,
  endosome to Golgi (a descendant).
- intracellular protein transport (IBA): KEEP_AS_NON_CORE (true but generic; no
  descendant specifically warranted).
