# dyf-11 (C. elegans) research notes

UniProt: Q17595 (Q17595_CAEEL) | WormBase: WBGene00001127 / C02H7.1 | Chromosome X
Human ortholog: **TRAF3IP1 / MIP-T3 / IFT54**. PANTHER family PTHR31363 (TRAF3-interacting protein 1).
Reactome: R-CEL-5620924 (Intraflagellar transport). ComplexPortal: CPX-1290 (IFT complex B).

## Identity / nomenclature (IMPORTANT)
dyf-11 is the true C. elegans **IFT54** ortholog (= MIP-T3 / TRAF3IP1). The flagship project doc
`projects/CAEEL_CILIOPATHY.md` erroneously lists both dyf-3 and dyf-11 as "IFT54"; dyf-3 is
actually the CLUAP1/IFT38 ortholog. This review curates dyf-11 as IFT54/MIP-T3/TRAF3IP1, which is
the assignment made by the primary cloning paper and by UniProt/InterPro/PANTHER.
[PMID:18369462 "the C. elegans MIP-T3 ortholog DYF-11 is an intraflagellar transport (IFT) protein"]

## Protein features (from UniProt Q17595)
- 535 aa; TRAF3IP1 family. Domains: TRAF3IP1 N-terminal (PF10243, aa 3-111) and TRAF3IP1 C-terminal
  (PF17749, aa 390-535). Long central disordered/charged region (aa ~107-391). C-terminal coiled coil
  (aa 426-520). No catalytic domain.
- SubCellular (ARBA): cilium axoneme; cilium basal body. Keywords: Cilium biogenesis/degradation,
  Coiled coil, Cytoskeleton, Cell projection.
- The family lacks recognizable catalytic motifs.
  [PMID:18369462 "MIP-T3 proteins range in size from 484 to 625 amino acids and have no recognizable domains except for a predicted coiled-coil region near the C-terminus"]

## KNOWN (well supported)

### DYF-11 is an IFT-B (intraflagellar transport subcomplex B) protein
Primary cloning/characterization paper: Li et al. 2008, PLoS Genet (FULL TEXT available).
- dyf-11(mn392) is a nonsense/null allele in C02H7.1 = the MIP-T3 ortholog; the Dyf (dye-filling)
  defect is fully rescued by wild-type C02H7.1::GFP.
  [PMID:18369462 "the dye-filling defect of dyf-11(mn392) is fully rescued by introducing a transgene expressing the wild-type copy of the C02H7.1 coding region"]
- DYF-11 "functions as a novel component of IFT subcomplex B."
  [PMID:18369462 "DYF-11 functions as a novel component of IFT subcomplex B"]
- Plays a critical role in assembling functional kinesin motor-IFT particle complexes.
  [PMID:18369462 "plays a critical role in assembling functional kinesin motor-IFT particle complexes"]

### Localization: transition zone/basal body and ciliary axoneme; undergoes IFT
- DYF-11::GFP "highly enriched at transition zones and within ciliary axonemes."
  [PMID:18369462 "the DYF-11::GFP protein was found to be highly enriched at transition zones and within ciliary axonemes"]
- Moves bidirectionally (IFT) along amphid/phasmid axonemes; anterograde biphasic velocity
  0.74 um/s (middle segment, doublet MTs) and 1.15 um/s (distal segment, singlet MTs).
  [PMID:18369462 "the GFP-tagged protein moves bi-directionally along the length of amphid and phasmid ciliary axonemes"]
- Accumulates at ciliary tips in che-11 (IFT-A/retrograde) mutant → confirms it is an IFT cargo/component.
  Enters distal segment of bbs mutants and osm-3 middle segment → behaves like OSM-3-kinesin/IFT-B.
- Human MIP-T3 (V5-tagged) localizes to basal body (pre-ciliated) and axoneme (ciliated IMCD3 cells).
  [PMID:18369462 "mammalian MIP-T3 localizes to basal bodies and cilia"]
- Expressed in all C. elegans ciliated neurons, under X-box (RFX/daf-19) control.
  [PMID:18245347 "while DYF-11 is expressed in all C. elegans ciliated neurons"]

### Required for cilium assembly and for integrity/assembly of the whole IFT machinery
- dyf-11 null cilia are strongly truncated (amphid 2.4 um, phasmid 2.6 um vs 5.7 um WT), similar to
  IFT-B mutants. In dyf-11, "medial and distal segments are absent."
  [PMID:18245347 "in dyf-11 animals, medial and distal segments are absent"]
- In dyf-11 mutants, IFT components (KAP-1/Kinesin-II, CHE-11/IFT-A, XBX-1/dynein, BBS-7) mislocalize
  and fail to enter cilia; only OSM-3 still enters the residual cilium.
  [PMID:18369462 "CHE-11, XBX-1, and BBS-7 were anchored to transition zones but their signal intensities were significantly reduced compared to wild-type, and none of the proteins were observed to enter the (truncated) amphid and phasmid cilia"]
- DYF-11 "may function at an early stage of IFT-B particle assembly."
  [PMID:18245347 "DYF-11 undergoes IFT-like movement and may function at an early stage of IFT-B particle assembly"]
- IFT-B complex disruption abolishes dynein-2 ciliary entry (dyf-11 is part of that IFT-B module).
  [PMID:28479320 "intraflagellar transport (IFT)-B complex abolishes dynein-2's ciliary localization"]

### Sensory / physiological phenotypes (downstream consequences of loss of functional cilia)
- Chemotaxis-defective and osmotic-avoidance-defective (Che, Osm).
  [PMID:18369462 "dyf-11 mutants are defective in both chemotaxis and osmo-avoidance"]
  [PMID:18245347 "These mutants fail to concentrate lipophilic dyes from their surroundings in sensory neurons and are chemotaxis defective"]
- Dauer-formation defective (Daf-d) at 20 and 25 C.
  [PMID:18369462 "we found that dyf-11 mutants are Daf-d at both temperatures"]
- Increased intestinal lipid (Nile Red) accumulation, rescued by DYF-11::GFP → cilia–lipid link.
  [PMID:18369462 "dyf-11 mutants also show, compared to the wild-type and rescue strains, a pronounced increase in Nile Red staining within intestinal cells, indicative of an increased lipid accumulation phenotype"]
- Normal lifespan; no gross morphological/locomotory defects → the role is highly cilia-specific.

### Conserved developmental role in vertebrates
- Zebrafish mipt3 morphants show gastrulation/convergent-extension defects and act synergistically
  with bbs4, consistent with a conserved cilia/basal-body role.
  [PMID:18369462 "zebrafish mipt3 functions synergistically with the Bardet-Biedl syndrome protein Bbs4 to ensure proper gastrulation"]

## NOT known / uncertain
- The **specific molecular function** of DYF-11 within IFT-B is undefined: no catalytic domain, only
  a C-terminal coiled coil; whether it directly binds microtubules in the worm (family = "Microtubule-
  Interacting Protein"; human MIP-T3 binds MTs) or bridges specific IFT-B subunits (vertebrate IFT54
  binds IFT20) is not established in C. elegans.
  [PMID:18369462 "Whether DYF-11 operates as an integral IFT component, or potentially as an associated 'cargo' protein that affects the core machinery, remains to be determined"]
- Whether DYF-11 has an **IFT-independent** role (e.g. dendrite/neurite trafficking, analogous to the
  vertebrate MIP-T3–DISC1 axis) in the worm is untested.
  [PMID:18369462 "Whether C. elegans DYF-11 has dendrite-associated functions whose disruption could affect ciliogenesis represents an interesting question that will need to be addressed"]
- The mechanism by which DYF-11 promotes loading/assembly of Kinesin-II onto IFT trains is unknown.
  [PMID:18369462 "may help with the assembly of Kinesin-II onto the IFT complex"]

## Annotation review reasoning (see YAML)
- CORE: IFT particle B membership (GO:0030992), intraciliary transport (GO:0042073), (non-motile)
  cilium assembly (GO:0060271 / GO:1905515), axoneme/basal body/cilium localization, microtubule
  binding (GO:0008017, family/InterPro MF), IFT complex assembly (GO:0065003), protein localization
  to cilium.
- MODIFY: GO:0045184 "establishment of protein localization" is too general → GO:0061512 "protein
  localization to cilium" (dyf-11 mutants fail to deliver IFT proteins into cilia).
- NON-CORE (pleiotropic downstream sensory phenotypes): chemotaxis, hyperosmotic response, dauer
  entry, associative learning, lipid homeostasis — all secondary to loss of functional sensory cilia.
- OVER-ANNOTATED (vague/ARBA/electronic): animal organ development, system development (ARBA, not
  informative for a worm ciliary protein); regulation of microtubule cytoskeleton organization
  (IBA+ARBA) over-generalizes DYF-11's structural axoneme-assembly role, better captured by cilium
  assembly.
- GO:0020837997 (associative learning, PMID:20837997): the cached record is abstract-only and the
  abstract does not mention dyf-11; the paper is about ASE salt-chemotaxis plasticity. Kept as
  non-core (indirect sensory consequence), flagged full_text_unavailable; not removed (experimental
  IMP; defer to curator).

## Deep research
`just deep-research-falcon worm dyf-11 --fallback perplexity-lite` completed successfully
(falcon / Edison Scientific, ~24 min, 24 citations) → `dyf-11-deep-research-falcon.md`. Review is
grounded primarily in the four cached primary publications above plus UniProt/GOA/InterPro/PANTHER;
the falcon report corroborates the IFT-B/IFT54 assignment and cilium-assembly role.
