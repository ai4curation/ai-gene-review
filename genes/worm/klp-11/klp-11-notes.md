# klp-11 (C. elegans) — Gene Review Notes

## Identity (verified from UniProt Q19633)
- UniProt: Q19633 (Q19633_CAEEL), 782 aa, TrEMBL/unreviewed.
- Gene: klp-11; ORF F20C5.2; WormBase WBGene00002222; RefSeq NP_001369897.1.
- Chromosome IV. Taxon: C. elegans, NCBITaxon:6239.
- Family: TRAFAC class myosin-kinesin ATPase superfamily, kinesin family (PROSITE
  PRU00283; RuleBase RU000394). Kinesin motor domain FT 13..343; ATP-binding P-loop 99..106.
- ComplexPortal CPX-1208 "Kinesin II motor complex"; GO:0030993 axonemal heterotrimeric
  kinesin-II complex (IPI:WormBase).
- PDB 9IKB (X-ray 3.54 Å of residues 537-782): "Crystal structure of heterotrimeric Kinesin-2"
  (stalk/tail region), consistent with klp-11 being a subunit of a heterotrimer.

klp-11 encodes one of the two motor (heavy-chain) subunits of C. elegans heterotrimeric
kinesin-II. The holoenzyme is a heterotrimer: KLP-11 + KLP-20 (the two distinct motor
subunits) + KAP-1 (the non-motor kinesin-associated protein / accessory subunit). This is the
orthologue of the vertebrate KIF3A/KIF3B/KAP3 kinesin-II. Kinesin-II is one of two
anterograde IFT motors in the worm; the other is homodimeric OSM-3 (KIF17 orthologue).

## KNOWN (well-supported)

### Molecular function: microtubule plus-end motor / ATPase, as part of the heterotrimer
- Purified recombinant C. elegans kinesin-II (KLP-11/KLP-20/KAP-1) is an active
  plus-end-directed MT motor in gliding assays; it obeys Michaelis-Menten kinetics with
  Mg-ATP as preferred substrate.
  [PMID:17000880 "In MT gliding assays, kinesin-II–driven motility conformed to Michaelis-Menten kinetics with a nucleotide profile very similar to that of kinesin-1 (Cohn et al., 1989), indicating that Mg-ATP is the preferred substrate for kinesin-2 motors"]
- Kinesin-II moves relatively slowly (~0.5 µm/s in vivo, ~0.3–0.5 µm/s in vitro), vs OSM-3 ~1.3 µm/s.
  [PMID:17000880 "kinesin-II alone moved MTs at a maximal rate of 0.3 μm/s, and OSM-3 alone moved them at 0.7 μm/s"]
  [PMID:17000880 "kinesin-II alone moved at ∼0.5 μm/s, whereas OSM-3 alone (wild type or the G444E mutant) moved at ∼1.1 μm/s ... very close to the rates of transport driven by kinesin-II (0.5 μm/s) and OSM-3 (1.3 μm/s) in vivo"]
- The purified holoenzyme is a monodisperse heterotrimer of KLP-11, KLP-20 and KAP-1
  (1:1:1 stoichiometry; ~287 kD), matching native kinesin-II.
  [PMID:17000880 "Purified kinesin-II behaved as a monodisperse, heterotrimeric complex on sucrose gradients (Fig. 1 F) and gel filtration columns (Fig. 1 G) consisting of 1 mol each of its subunits KLP-11, KLP-20, and KAP-1 with a native molecular mass of 287 kD"]
- WormBase makes an IDA microtubule motor activity annotation (GO:0003777) and an IDA
  microtubule-based movement annotation to klp-11 from PMID:17000880 (in vitro motility of the
  purified holoenzyme containing KLP-11).

### Heterodimerization mechanism (why two distinct motor subunits)
- The KLP-11 motor domain is UNPROCESSIVE as a homodimer; heterodimerization with the
  processive KLP-20 partner generates processivity. The "unprocessive" KLP-11 subunit is
  retained because it mediates asymmetric autoregulation of motor activity, and
  heterodimerization is required to bind KAP-1 (the motor-cargo link).
  [PMID:20498083 "One motor domain is unprocessive as a homodimer, but heterodimerization with a processive partner generates processivity. The \"unprocessive\" subunit is kept in this partnership as it mediates an asymmetric autoregulation of the motor activity. Finally, heterodimerization is necessary to bind KAP1, the in vivo link between motor and cargo."]
  (Note: PMID:20498083 is abstract-only in cache; full_text_available: false. The abstract
  explicitly names KLP11/KLP20 of C. elegans, so the identity is certain.)

### Cellular component / complex
- Subunit of the axonemal heterotrimeric kinesin-II complex (GO:0030993); IPI annotation by
  WormBase from PMID:17000880 with KLP-20 (WBGene00002230) and KAP-1 (WBGene00002182) as the
  with/from partners.
- Localizes to sensory cilia (UniProt: Cell projection, cilium; ARBA). C. elegans kinesin-II
  operates on axonemal microtubule doublets of the middle (initial) segment of amphid channel
  cilia.
  [PMID:17000880 "C. elegans amphid channel ciliary axonemes are made up of two domains: an initial segment (called the middle segment) containing 4-μm–long MT doublets ... and a distal segment comprising 2.5-μm–long MT singlets"]

### Biological process: anterograde IFT of the ciliary middle segment (redundant with OSM-3)
- Kinesin-II (with KLP-11) and OSM-3 are the two anterograde IFT motors; they act
  cooperatively/redundantly to move IFT particles along the middle segment and build the
  cilium foundation; either motor alone suffices for the middle segment (redundant), while
  OSM-3 alone extends the distal singlet segment.
  [PMID:17000880 "These motors function redundantly to move the same IFT particles along the initial segment and build the cilium foundation, with either motor but not both being dispensable for this function"]
  [PMID:17000880 "the IFT particles assembling these sensory cilia are moved by the coordinate action of two anterograde IFT motors called kinesin-II and OSM-3, which are both members of the kinesin-2 family"]
- klp-11 single mutants have near full-length cilia (because OSM-3 compensates in the middle
  segment and builds the distal segment), unlike osm-3 mutants which lack distal segments.
  [PMID:17000880 "the bbs-7/-8;klp-11 double mutants have almost full-length cilia, which is similar to the klp-11 mutants, and the bbs-7/-8;osm-3 double mutants have truncated cilia similar to the osm-3 mutants"]
  [PMID:17000880 "OSM-6∷GFP moves at OSM-3's fast rate in klp-11 mutants"]
- Motors coordinate by "mechanical competition": slow kinesin-II drags fast OSM-3 and vice
  versa; this tension, antagonized by BBS proteins, is what dissociates IFT-A/IFT-B in bbs
  mutants. This is a kinesin-II holoenzyme (KLP-11-containing) property.
  [PMID:17000880 "the slower moving kinesin-II exerting drag on the faster moving OSM-3, whereas the faster moving OSM-3 tends to pull the slower moving kinesin-II along"]

## NOT known / gaps
- No klp-11-SPECIFIC (subunit-resolved) in vivo function beyond the holoenzyme: the motility,
  IFT, and localization data are for the intact KLP-11/KLP-20/KAP-1 heterotrimer or the
  KLP-11/KLP-20 heterodimer, not for a KLP-11 activity independent of its partners. Because
  KLP-11 is unprocessive as a homodimer (PMID:20498083), it does NOT have an autonomous
  processive motor activity — its motor role is realized only in the heterodimer/heterotrimer.
- The IFT cargo(es) directly linked to kinesin-II via KAP-1 in the worm, and how loading is
  regulated, are not resolved by the cached primary literature.
- Structure of the full assembled worm heterotrimer / the KLP-11 head–partner interface at
  atomic resolution: only a 3.54 Å partial (residues 537-782, stalk/tail) structure (PDB
  9IKB) is available; the mechanistic basis of asymmetric autoregulation is not solved.
- No evidence klp-11 acts outside cilia/IFT in the worm (no non-ciliary transport role
  established); vertebrate KIF3 paralogues have additional roles (melanosome transport,
  Hedgehog, left-right asymmetry) not demonstrated for C. elegans klp-11.

## Annotation review reasoning
- Core (retain as core function): microtubule motor / plus-end motor activity and ATP
  hydrolysis contributed as part of the kinesin-II heterotrimer; membership of the axonemal
  heterotrimeric kinesin-II complex (GO:0030993) / kinesin II complex (GO:0016939); microtubule
  binding; anterograde IFT (GO:0035720) / microtubule-based movement; cilium localization.
- IBA/IEA generic parents (cytoplasm, cytoskeleton, microtubule, nucleotide binding,
  cytoskeletal motor activity, protein-containing complex) — ACCEPT as correct-but-general, or
  MODIFY where a more specific curated term is warranted; protein-containing complex → MODIFY to
  kinesin II complex.
- cilium assembly (GO:0060271, IBA): klp-11 single mutants have near-full-length cilia (OSM-3
  redundancy), so klp-11 contributes to but is individually dispensable for ciliogenesis; keep
  as involved (assembly is redundant), not the sharpest term — the sharpest is anterograde IFT.
- No REMOVE of the experimental IDA/IPI/NAS annotations — all are consistent with the
  holoenzyme evidence.

## Provenance discipline
- All supporting_text above are verbatim substrings of the cached publications
  (publications/PMID_17000880.md full text; publications/PMID_20498083.md abstract).
- PMID:20498083 is abstract-only in cache; NAS annotations from it (ComplexPortal) are
  supported by the abstract's explicit statements about KLP11/KLP20/KAP1.
