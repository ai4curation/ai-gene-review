# klp-20 (C. elegans) — Gene Review Notes

## Identity (verified from UniProt Q965T6)

- UniProt: **Q965T6** (KLP20_CAEEL), 646 aa, "Kinesin-like protein klp-20"
- WormBase: **WBGene00002230**, sequence name **Y50D7A.6**, on Chromosome III
- Family: TRAFAC class myosin-kinesin ATPase superfamily; Kinesin family; **Kinesin II subfamily**
- Domain architecture (UniProt): N-terminal **Kinesin motor domain (6–331)** with the P-loop ATP-binding
  Walker A (BINDING 91..98, ATP); a long **coiled coil (342–552)** stalk; a **klp-11 interaction region
  (525–550)**; and a disordered C-terminal tail (623–646, basic).
- Structure: PDB **9IKB** (X-ray 3.54 Å) covers residues 527–646 (the C-terminal stalk/tail); AlphaFoldDB Q965T6;
  ComplexPortal **CPX-1208 "Kinesin II motor complex"**.

klp-20 is **one of the two motor subunits of heterotrimeric kinesin-II** in *C. elegans*. Kinesin-II is the
heterotrimer **KLP-11 + KLP-20 + KAP-1** (two distinct motor polypeptides + one non-motor accessory subunit KAP).
This is distinct from **OSM-3**, the *homodimeric* kinesin-2 that is the second anterograde IFT motor. klp-20 must be
kept distinct from its heterodimer partner klp-11 (KLP11_CAEEL) — much of the biochemistry was done on the
KLP-11/KLP-20 heterodimer, and where a result is specific to klp-11 alone I note it.

## KNOWN (well supported)

### Kinesin-II complex membership (experimental, klp-20-specific)
- klp-20 is a subunit of the heterotrimeric kinesin-II motor. Purified recombinant kinesin-II behaves as a
  monodisperse heterotrimer of the three named subunits:
  [PMID:17000880 "the KLP-11, KAP-1, and KLP-20 subunits elute as a monodisperse heterotrimeric complex"]
  [PMID:17000880 "consisting of 1 mol each of its subunits KLP-11, KLP-20, and KAP-1 with a native molecular mass of 287 kD"]
- The complex is the **axonemal heterotrimeric kinesin-II complex** (GO:0030993). UniProt SUBUNIT: "Component of the
  kinesin II motor complex, a heterotrimeric complex composed of kap-1, klp-11 and klp-20" (UniProt Q965T6).
- ComplexPortal CPX-1208 records the "Kinesin II motor complex" (NAS, PMID:20498083).

### Microtubule motor / ATPase activity (experimental, complex-level)
- Purified recombinant kinesin-II (containing klp-20) is an **ATP-driven, microtubule plus-end-directed motor**:
  [PMID:17000880 "kinesin-II alone moved MTs at a maximal rate of 0.3 μm/s"]
  and, under optimized conditions, [PMID:17000880 "kinesin-II alone moved at ∼0.5 μm/s"].
- Kinesin-II uses Mg-ATP by Michaelis–Menten kinetics:
  [PMID:17000880 "kinesin-II–driven motility conformed to Michaelis-Menten kinetics"] and
  [PMID:17000880 "indicating that Mg-ATP is the preferred substrate for kinesin-2 motors"].
- Kinesins are plus-end directed motors; anterograde IFT (base→ciliary tip) is toward MT plus ends, so the specific
  MF is **plus-end-directed microtubule motor activity (GO:0008574)** rather than only the parent GO:0003777.
  WormBase made the IDA GO:0003777 "microtubule motor activity" annotation from PMID:17000880.

### Heterodimerization confers processivity; needed for cargo coupling (klp-20/klp-11 heterodimer)
- The KLP-11/KLP-20 heterodimer is the functional unit: one motor domain is unprocessive alone but becomes
  processive on heterodimerization:
  [PMID:20498083 "One motor domain is unprocessive as a homodimer, but heterodimerization with a processive partner generates processivity."]
- Heterodimerization is required to bind KAP-1, which links the motor to cargo:
  [PMID:20498083 "heterodimerization is necessary to bind KAP1, the in vivo link between motor and cargo."]
- The unprocessive subunit contributes asymmetric autoregulation of motor activity:
  [PMID:20498083 "The \"unprocessive\" subunit is kept in this partnership as it mediates an asymmetric autoregulation of the motor activity."]
- UniProt (from PMID:20498083, PMID:21917588) elaborates: the C-termini of klp-20 and klp-11 form a coiled-coil
  stalk necessary for association with kap-1, and prior to cargo binding the heterodimer is autoinhibited by its
  tail folding onto the motor domain; cargo binding relieves autoinhibition. Interaction region on klp-20 = 525–550
  (REGION, ECO:0000269|PubMed:21917588).

### Anterograde IFT along sensory cilia (experimental at the pathway level)
- In *C. elegans* amphid/phasmid sensory neuron cilia, kinesin-II and OSM-3 are the two anterograde IFT motors that
  redundantly build the cilium foundation (middle/initial segment, MT doublets); OSM-3 alone extends the distal
  singlet segment:
  [PMID:17000880 "the IFT particles assembling these sensory cilia are moved by the coordinate action of two anterograde IFT motors called kinesin-II and OSM-3"]
  [PMID:17000880 "either motor but not both being dispensable for this function"]
- Kinesin-II is the slower motor (~0.5 µm/s in vivo) vs OSM-3 (~1.3 µm/s); the two act by mechanical competition,
  with BBS proteins holding IFT-A and IFT-B together against the tension:
  [PMID:17000880 "the slower moving kinesin-II exerting drag on the faster moving OSM-3"]
- Subcellular location: UniProt SUBCELLULAR LOCATION = cilium (Cell projection), with a note that it localizes to the
  base and transition zone of cilia (ECO:0000269|PubMed:28479320); also Cytoplasm/cytoskeleton (by similarity).

## NOT established / KNOWLEDGE GAPS (for klp-20 specifically)

1. **Which subunit of the heterodimer is the "unprocessive" one?** PMID:20498083 shows the KLP-11/KLP-20 heterodimer
   pairs a processive with an unprocessive motor domain and that the unprocessive subunit mediates asymmetric
   autoregulation, but the abstract (only the abstract is cached; full text not available from PMC) does not, in the
   cached text, assign the unprocessive/processive role to klp-20 vs klp-11 by name. So whether klp-20 itself is the
   processive or the unprocessive head — and thus the residue-level basis of its individual duty ratio — is not
   pinned down here. (Later biophysical work partly addresses this, but is not in our cache.)

2. **klp-20-specific (vs klp-11-specific) contribution to autoinhibition / cargo release.** UniProt annotates two
   sites on klp-20 (444, 445) as "May be required for autoinhibition within the klp-11/klp-20 heterodimer"
   (ECO:0000269|PubMed:20498083), but the mechanism by which klp-20 (as opposed to klp-11 or KAP-1) triggers
   release of autoinhibition upon cargo binding is not resolved.

3. **Direct ciliary cargo of the klp-20-containing motor.** UniProt notes the kinesin-II complex delivers specific
   ciliary cargo (e.g. che-3/dynein) to ciliary tips "likely mediated by IFT complexes A and B" (PMID:28479320) —
   i.e. the direct, klp-20-motor-selected cargo repertoire is inferred through the IFT particle, not directly
   enumerated for klp-20.

## Annotation review plan (22 GOA rows)

MF:
- GO:0003777 microtubule motor activity — 3 rows (IBA GO_REF:0000033; IEA GO_REF:0000120; **IDA PMID:17000880**).
  Core. IDA is the strongest; MF is really plus-end-directed. ACCEPT the IDA as core; the IBA/IEA are redundant
  same-term support (KEEP_AS_NON_CORE / ACCEPT). Propose GO:0008574 as the more specific MF in core_functions.
- GO:0016887 ATP hydrolysis activity (IBA) — ACCEPT, part of motor mechanism (supported by PMID:17000880 kinetics).
- GO:0005524 ATP binding (IEA) — ACCEPT (Walker A motif present; molecular-mechanism support).
- GO:0008017 microtubule binding — 2 rows (IBA, IEA) — ACCEPT (motor must bind MT track).

CC:
- GO:0030993 axonemal heterotrimeric kinesin-II complex (**IPI PMID:17000880**) — ACCEPT, core complex membership.
- GO:0016939 kinesin II complex (NAS PMID:20498083) — ACCEPT, complex membership (more general than 0030993).
- GO:0005871 kinesin complex (IBA) — ACCEPT/KEEP_AS_NON_CORE (general parent of the above).
- GO:0032991 protein-containing complex (IEA ARBA) — over-general; MARK_AS_OVER_ANNOTATED (root-level).
- GO:0005929 cilium (IEA) — ACCEPT, location (consistent with UniProt SUBCELLULAR LOCATION cilium).
- GO:0005874 microtubule (IBA) — KEEP_AS_NON_CORE (track, not really a "location" of the protein per se).
- GO:0005737 cytoplasm (IBA) — KEEP_AS_NON_CORE (broad; consistent with cytoplasm-by-similarity).
- GO:0005856 cytoskeleton (IEA) — KEEP_AS_NON_CORE (general).
- GO:1904115 axon cytoplasm (IEA GO_REF:0000108, inferred from GO:0008089) — this is inferred solely from the
  anterograde axonal transport BP, which itself is an IBA over-propagation (see below). klp-20 acts in sensory
  cilia, not documented axonal transport in worm. MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE.

BP:
- GO:0035720 intraciliary anterograde transport (NAS PMID:20498083) — ACCEPT, core.
- GO:0060271 cilium assembly (IBA) — ACCEPT/KEEP_AS_NON_CORE (kinesin-II builds the cilium foundation; PMID:17000880).
- GO:0007018 microtubule-based movement — 3 rows (IBA; IEA; **IDA PMID:17000880**; NAS PMID:20498083 also) — ACCEPT
  (parent of the specific transport; IDA strongest). Somewhat general vs 0035720.
- GO:0008089 anterograde axonal transport (IBA) — the phylogenetic transfer from KIF3/kinesin-II in neurons brings
  in an axonal-transport term. In *C. elegans* the documented role is ciliary IFT, not classical axonal transport;
  this is a likely IBA over-propagation. MARK_AS_OVER_ANNOTATED (or KEEP_AS_NON_CORE) — but do NOT remove the
  underlying experimental terms; this is the electronic/IBA one only.

Kinesin modeling (per task): model motor via in_complex (GO:0030993 axonemal heterotrimeric kinesin-II complex) +
contributes_to_molecular_function (GO:0008574 plus-end-directed MT motor / GO:0016887 ATP hydrolysis), keeping a
specific MT motor MF (not protein binding). Directly_involved_in: GO:0035720 intraciliary anterograde transport,
GO:0060271 cilium assembly.

## Deep research
- falcon deep-research launched (foreground) with perplexity-lite fallback; see klp-20-deep-research-*.md if produced.
  Primary review rests on the cached full text of PMID:17000880 and the abstract of PMID:20498083 plus UniProt Q965T6.
</content>
