# VPS4B notes

## Local evidence reviewed

- `just fetch-gene human VPS4B` created the review stub, UniProt record, GOA table, and cached publications. GOA seeded 94 annotations, including ATPase activity, ESCRT/MVB sorting, ESCRT-III disassembly, endosome-to-lysosome transport, viral budding, exosome secretion, cell-division/centrosome terms, autophagy terms, and generic protein-binding rows.
- `just deep-research-falcon human VPS4B` timed out after 600 seconds and did not produce a usable report. The review below is based on local UniProt, GOA, cached publication, Reactome, and PN-context evidence.
- UniProt identifies VPS4B as an AAA-family vacuolar protein sorting ATPase. Its function comment states that VPS4B recognizes membrane-associated ESCRT-III assemblies and catalyzes ATP-dependent disassembly, redistributing ESCRT-III components for further MVB sorting [UniProt:O75351, "Recognizes membrane-associated ESCRT-III assemblies and catalyzes their ATP-dependent disassembly"; UniProt:O75351, "Redistributes the ESCRT-III components to the cytoplasm for further rounds of MVB sorting."].
- VPS4B has direct biochemical support for the ESCRT-III disassembly mechanism. CHMP2A and CHMP3 form helical tubular structures, and VPS4 binds inside those tubes and disassembles them upon ATP hydrolysis [PMID:18687924, "the AAA-type adenosine triphosphatase VPS4 could bind on the inside of the tubule and disassemble the tubes upon adenosine triphosphate hydrolysis."].
- Mammalian VPS4A and VPS4B complement yeast vps4 defects and cause dominant-negative vacuolar sorting defects when ATPase-domain glutamate mutants are expressed, supporting conserved late endosomal protein transport [PMID:11563910, "both human VPS4 proteins are involved in intracellular protein trafficking, presumably at a late endosomal protein transport step"].
- VPS4B supports endosome-to-lysosome sorting of non-ubiquitinated GPCR cargo. Dominant-negative Vps4/Skd1 inhibited agonist-induced proteolysis of the delta opioid receptor, supporting late lysosomal sorting via VPS machinery rather than a direct cargo-specific transport function [PMID:15024011, "Agonist-induced proteolysis of DOR was significantly inhibited by dominant negative mutant versions of Vps4/Skd1"].
- Cholesterol depletion promotes NPC1 ubiquitylation and association with SKD1/Vps4, while dominant-negative SKD1/Vps4 accumulates ubiquitylated NPC1 [PMID:16757520, "SKD1(E235Q), a dominant-negative mutant of SKD1/Vps4 that inhibits disassembly of the endosomal sorting complex required for transport (ESCRT), caused an accumulation of ubiquitylated NPC1."]. This supports an endosomal ESCRT response to lipid/cholesterol state, but not a direct lipid-response or cholesterol-transport core function for VPS4B.
- VPS4B MIT-domain/ESCRT-III recognition and viral budding are supported by VPS4 ATPase interaction studies. MIM-binding mutations impair VPS4 recruitment, lysosomal protein targeting, and HIV-1 budding [PMID:18606141, "Mutations that block VPS4 MIT-MIM2 interactions inhibit VPS4 recruitment, lysosomal protein targeting, and HIV-1 budding."].
- VPS4B cell-division/centrosome rows are supported by the ESCRT-III/VPS4 depletion study, but they should be treated as non-core ESCRT-output phenotypes. The paper reports that depletion of VPS4A, VPS4B, or CHMP proteins inhibited abscission and altered centrosome/spindle pole numbers [PMID:20616062, "depletion of VPS4A, VPS4B, or any of the 11 different human ESCRT-III (CHMP) proteins inhibited abscission"; PMID:20616062, "VPS4 proteins concentrated at spindle poles during mitosis and then at midbodies during cytokinesis"].
- VPS4B has context-dependent exosome annotations. UniProt reports that VPS4A/B are required for exosomal release of SDCBP, CD63 and syndecan [UniProt:O75351, "VPS4A/B are required for the exosomal release of SDCBP, CD63 and syndecan"]. A separate ESCRT RNAi screen found that VPS4B depletion augmented EV-associated CD63 and MHC II secretion in HeLa-CIITA cells [PMID:24105262, "depletion of VPS4B augmented this secretion while not altering the features of EVs."]. These are both non-core, cargo/cell-context-dependent exosome outputs.
- Autophagy-related rows require caution as in VPS4A. Cached evidence is yeast-only or review-level: yeast VPS4 deletion affected pAPI maturation via autophagy/Cvt [PMID:17428789, "deletion of VPS4 and VPS36 caused impaired maturation of the vacuolar proaminopeptidase I (pAPI) via autophagy or the cytosol to vacuole targeting pathway"], and ESCRT-III membrane neck cleavage was reviewed as probably important for autophagy [PMID:20588296, "ESCRT-III-mediated membrane neck cleavage is crucial for many processes, including the biogenesis of multivesicular bodies, viral budding, cytokinesis, and probably autophagy."].
- The PN projection to `GO:0000815 ESCRT III complex` should not be added for VPS4B. VPS4B is an AAA ATPase that remodels/disassembles ESCRT-III assemblies, not an ESCRT-III core subunit.

## Curation synthesis

The core molecular/cellular role of VPS4B is ATP hydrolysis-driven ESCRT-III polymer remodeling and disassembly. This role supports endosomal/MVB sorting, ESCRT-III recycling, and topologically related membrane-remodeling outputs. `GO:0016887 ATP hydrolysis activity`, `GO:1904903 ESCRT III complex disassembly`, `GO:0051261 protein depolymerization` only as a less-specific proxy, and MVB/endosome sorting terms are central. A new more specific molecular-function annotation to `GO:0140545 ATP-dependent protein disaggregase activity` is justified by PMID:18687924.

Generic `GO:0005515 protein binding` rows should not be retained as informative molecular functions. VPS4B interactions with ESCRT-III, VPS4A, VTA1, ZFYVE19/ANCHR, and high-throughput partners are useful context, but the curated function should focus on ATP-dependent ESCRT-III disassembly and complex binding when supported.

Viral budding, exosome secretion, plasma membrane repair, cytokinesis/midbody, nuclear-envelope, and centrosome/spindle terms are real ESCRT-output contexts but should be marked non-core unless the row overstates a downstream phenotype. Autophagy rows remain conservative pending Falcon and direct human evidence.

## 2026-10-25: inflammasome lead assessed (litscan #3920)

A 2026 report proposes a non-ESCRT role for VPS4B at the ASC speck: Vps4B is
described as a component of the NLRP3 and AIM2 inflammasomes that interacts
endogenously with ASC and caspase-1, is recruited to the speck by Ca2+ signalling
downstream of NLRP3/ASC polymerisation, and forms a ring encircling the ASC filament
that disassembles and liberates the spent caspase-1 CARD, allowing continuous
caspase-1 recruitment [PMID:42714851, "we identified the ATPase Vps4B as a central
component of the inflammasome that endogenously interacts with ASC and caspase-1";
PMID:42714851, "Vps4B forms a ring-like structure encircling the ASC filament and
catalyzes the disassembly and liberation of the used caspase-1 CARD domain."].

**No change made to this review.** The claimed activity is mechanistically continuous
with the established core function - ATP-dependent disassembly of a protein polymer
through the central pore of stacked VPS4 rings - but the evidence does not yet support
an annotation here:

- Single primary report, cached abstract-only (`full_text_available: false`), no
  independent replication. GOA carries no inflammasome or pyroptosis row for VPS4B,
  and VPS4B appears in no cached GO-CAM.
- The functional unit is unsettled. UniProt records that VPS4B "Interacts with VPS4A;
  the interaction suggests a heteromeric assembly with VPS4A" [UniProt:O75351,
  CC:SUBUNIT], and ComplexPortal CPX-338 is the VPS4A/B complex; the abstract does not
  address whether VPS4A is at the speck or redundant there.
- No ATPase-dead separation of function is reported, so it is not established that the
  inflammasome phenotype requires ATP hydrolysis by VPS4B rather than its presence.
- Substrate selectivity is unexplained: the ring is placed on the ASC filament while
  the substrate is said to be the caspase-1 CARD polymer.

The assessment, the reopening conditions, and the admission path (a regulatory annoton
on the `casp1_autoactivation` step) are recorded in
`modules/canonical_nlrp3_inflammasome.yaml` - note (9) and a structured
`knowledge_gaps` entry. That module, not `modules/nlr_signaling.yaml`, is the right
home: `nlr_signaling` is the coarse sensor-layer sketch and delegates the NLRP3 branch.
If the role is confirmed, the candidate terms to weigh are `GO:0140545 ATP-dependent
protein disaggregase activity` (already proposed as NEW here for the ESCRT-III
activity) or `GO:0051261 protein depolymerization`, with `GO:0072559 NLRP3
inflammasome complex` as location - but only after replication.
