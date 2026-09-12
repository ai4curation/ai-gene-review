# mksr-1 (K03E6.4 / WBGene00019364 / Q21191) — research notes

## Identity

- UniProt **Q21191** (Q21191_CAEEL), *Caenorhabditis elegans*, 229 aa.
- RecName: **B9 domain-containing protein 1** (i.e. **B9D1** ortholog) [UniProt Q21191, "RecName: Full=B9 domain-containing protein 1"].
- Gene: **mksr-1** ("MKS-1-related protein 1"); ORF **K03E6.4**; WormBase **WBGene00019364**; on Chromosome X.
- Domain content: a single **B9 (C2-B9-type) domain** (InterPro IPR010796 "C2_B9-type_dom"; Pfam PF07162 "B9-C2"; PROSITE PS51381 C2_B9). PANTHER PTHR12968:SF1 "B9 DOMAIN-CONTAINING PROTEIN 1".
- Belongs to the **B9D family** [UniProt Q21191, "Belongs to the B9D family."].
- NOT an integral membrane protein: no signal peptide, no transmembrane keyword. This distinguishes it from mks-2 (TMEM216, multi-pass membrane). mksr-1 is a peripheral B9/C2-domain component of the MKS module. (UniProt keywords: Cell projection, Cilium biogenesis/degradation, Cytoplasm, Cytoskeleton.)
- UniProt subcellular location: "Cytoplasm, cytoskeleton, cilium basal body" (ARBA electronic).
- UniProt binary interaction: `Q21191; Q9N423: mksr-2; NbExp=3; IntAct=EBI-330284, EBI-330279` — i.e. MKSR-1 binds **MKSR-2 (B9D2, Q9N423)**.

### Nomenclature caution
Older literature uses conflicting names for the three worm B9 proteins. Williams et al. 2008 (PMID:18337471) named them **XBX-7 (MKS1), TZA-1 (B9D2), TZA-2 (B9D1)**. Bialas et al. 2009 (PMID:19208769) and Williams et al. 2011 (PMID:21422230) use the now-standard **MKS-1, MKSR-1/B9D1, MKSR-2/B9D2**. UniProt, WormBase and the CAEEL_CILIOPATHY project all use **mksr-1 = B9D1**, **mksr-2 = B9D2**. I use the standard naming; where a paper uses other names I note the correspondence.

## What is KNOWN

### Family, domain, evolution
- The B9 domain occurs "exclusively within a family of three proteins distributed widely in ciliated organisms" [PMID:19208769 abstract, "this domain occurs exclusively within a family of three proteins distributed widely in ciliated organisms"].
- Structure/fold predictions relate the B9 domain to a **C2 domain** (Ca2+/lipid-binding, synaptotagmin-like) [PMID:21422230, "B9 domains of MKS-1, MKSR-1, and MKSR-2 may be structurally related to C2 domains"; "This motif is predicted to bind Ca2+/lipids and participate—similar to synaptotagmin—in membrane/vesicle trafficking and fusion"]. This is a *predicted* biochemical property; no direct Ca2+/lipid-binding assay for MKSR-1 exists in these papers.

### Localization (experimental)
- All three C. elegans B9 proteins (MKS-1, MKSR-1, MKSR-2) "localize to transition zones/basal bodies of sensory cilia" [PMID:19208769 abstract].
- Direct imaging: MKSR-1/B9D1 localizes to the **ciliary transition zone** in C. elegans sensory neurons [PMID:21422230, "This is evident for MKS-1, MKS-1 related-1 (MKSR-1)/B9D1, MKS-1 related-2 (MKSR-2)/B9D2, MKS-3/meckelin, NPHP-1, and NPHP-4"; GFP-MKSR-1 imaged at TZ, Fig 1–2, Fig 8G]. This is the basis of the WormBase IDA GO:0035869 (ciliary transition zone) annotation (PMID:21422230).
- Localization is **co-dependent** among the B9 proteins: "Their subcellular localization is largely co-dependent, pointing to a functional relationship between the proteins" [PMID:19208769 abstract].
- MKSR-1 TZ localization depends on upstream MKS-5: "mks-5 mutants failed to properly localize MKS-1, MKSR-1, and MKSR-2" [PMID:21422230].
- MKSR-1::tdTomato is used as a TZ comarker [mks-2 review cites PMID:26982032, "MKSR-1::tdTomato and MKS-2::GFP are TZ protein comarkers"].

### The MKS module / complex
- MKSR-1 is a member of the MKS/MKSR module together with MKS-1, MKSR-2, MKS-3, MKS-6: "MKS/MKSR module ... consisting of MKS-1/MKSR-1/MKSR-2/MKS-3/MKS-6" [PMID:21422230]. Modeled in GO as the **MKS complex (GO:0036038)**.
- The MKS module and the NPHP module (NPHP-1/NPHP-4) are recruited/anchored by the central scaffold MKS-5/RPGRIP1L.

### Function: transition-zone assembly / Y-links / membrane anchoring
- MKSR-1 acts, redundantly with the NPHP module, in building the TZ. The **mksr-1;nphp-4** double mutant has severe TZ ultrastructure defects — TZ not anchored to membrane, missing Y-links: "Phenotypes nearly identical to mks-6;nphp-4 mutants were observed in the mksr-1;nphp-4 strain" [PMID:21422230]. (Table I: mksr-1;nphp-4 shows enlarged TZ membrane diameter and 0% of TZs with Y-links.)
- MKSR-1 is required for the TZ localization of other MKS-module proteins (MKS-6, MKS-3): "disrupting MKSR-1, MKSR-2, or MKS-5 results in TZ delocalization of MKS-6 ... and MKS-3" [PMID:21422230]. This underlies the IMP GO:1904491 (protein localization to ciliary transition zone) and GO:0008104 (intracellular protein localization) annotations.

### Function: ciliary gate / diffusion barrier
- MKSR-1 is required to restrict membrane-associated proteins from entering the cilium (ciliary gate). In the mksr-1 single mutant, three normally-excluded proteins accumulate inside cilia:
  - MKS-3: "accumulates abnormally inside cilia (cil) and at dendritic tips (DT) in mks-5, mksr-1, and mksr-2 mutants" [PMID:21422230, Fig 9L].
  - RPI-2 (RP2 ortholog): "accumulates within cilia of ... mksr-1, mksr-2, mks-5, mks-6, and nphp-4 single mutants" [PMID:21422230, Fig 9M].
  - TRAM-1a: "accumulates within cilia of mksr-1, mksr-2, mks-5, mks-6, nphp-1, and nphp-4 mutants" [PMID:21422230, Fig 9N].
- General model: "TZ proteins normally function to maintain a boundary at the cilium base, establishing the TZ as a bona fide ciliary gate" [PMID:21422230]. This supports a NEW GO:1903565 (negative regulation of protein localization to cilium) annotation, mirroring the mks-2 review.
- Notably, the mksr-1 *single* mutant already shows the gate defect (RPI-2, TRAM-1a, MKS-3 mislocalization) even though gross cilium structure is normal — the gate phenotype is more sensitive than the structural phenotype.

### Redundancy / single-mutant subtlety
- Single, double and triple mks/mksr mutants "do not display overt defects in ciliary structure, intraflagellar transport or chemosensation" [PMID:19208769 abstract].
- B9-gene mutations "do not overtly affect cilia formation unless they are in combination with a mutation in nph-1 or nph-4" [PMID:18337471 abstract]. → basis of the IGI GO:1905515 (non-motile cilium assembly) annotations (mksr-1 × nphp-1/nphp-4, WITH WBGene00011261=nphp-4, WBGene00007490=nphp-1).

### Lifespan / insulin-IGF phenotype
- Double mks/mksr mutants have an increased lifespan phenotype due to abnormal insulin-IGF-I signaling: "we find genetic interactions between all double mks/mksr mutant combinations, manifesting as an increased lifespan phenotype, which is due to abnormal insulin-IGF-I signaling" [PMID:19208769 abstract]. → basis of the IGI GO:0008340 (determination of adult lifespan) annotations. This is an indirect, module-redundancy phenotype (a downstream consequence of impaired ciliary signaling), not a direct molecular function of MKSR-1.

### Larval foraging behavior
- GO:0035177 (larval foraging behavior) IGI annotation from PMID:18337471 (WITH WBGene00011261 = nphp-4). Foraging/roaming behavior in worms depends on functional sensory cilia; a B9×nphp genetic interaction affecting cilia would plausibly affect foraging. The cached record is abstract-only (does not state "foraging" explicitly), so this is a curator judgment from full text — retained (KEEP_AS_NON_CORE), not overruled.

### Protein interactions
- MKSR-1 binds MKSR-2 (B9D2). UniProt binary interaction Q21191–Q9N423 (NbExp=3); IntAct EBI-330284/EBI-330279; DIP-27480N. GOA has IPI GO:0005515 (protein binding) annotations with WITH/FROM UniProtKB:Q9N423 from PMID:14704431 (Li et al. 2004 worm interactome) and PMID:19123269 (Simonis et al. 2009 empirically-controlled interactome), plus one WB IPI from PMID:18337471 (WITH WBGene00021416 = mksr-2). The interaction is real, but `protein binding` is uninformative; the biologically meaningful fact is the B9D1–B9D2 (MKSR-1–MKSR-2) heterodimer within the MKS module.

## What is NOT known

- **No molecular-function GO term** captures what MKSR-1 does. It is a structural/scaffold subunit of the TZ MKS module (diffusion-barrier / Y-link scaffold). GO has no "structural constituent of the ciliary transition zone" MF term; `structural molecule activity` (GO:0005198) is the closest placeholder. (Ontology gap — shared across MKS/NPHP-module genes; cf. the mks-2 review.)
- Whether the **predicted C2/B9 Ca2+/lipid-binding** activity is real for MKSR-1 (no direct biochemical assay).
- MKSR-1's **direct binding partners** beyond MKSR-2 in the worm TZ, and its precise position within the MKS-module architecture (super-resolution / proteomics not resolved for MKSR-1 specifically).
- Whether MKSR-1 has any **non-redundant** sub-function distinct from the other core MKS-module proteins (single mutants near-normal structurally; phenotypes emerge in nphp double mutants), though the single-mutant gate leak (RPI-2/TRAM-1a) indicates at least some non-fully-redundant barrier contribution.

## Annotation review plan (summary)

| GO term | Evid | Ref | Planned action |
|---|---|---|---|
| GO:0036038 MKS complex (part_of) | IBA | GO_REF:0000033 | ACCEPT (core; corroborated by direct imaging/genetics) |
| GO:0060271 cilium assembly (involved_in) | IBA | GO_REF:0000033 | MODIFY → GO:1905515 non-motile cilium assembly (worm sensory cilia are non-motile; more specific) |
| GO:0005929 cilium (located_in) | IEA | GO_REF:0000117 | MODIFY → GO:0035869 ciliary transition zone (specific; IDA-supported) / or KEEP_AS_NON_CORE |
| GO:0005515 protein binding (enables) ×3 | IPI | PMID:14704431 / 19123269 / 18337471 | KEEP_AS_NON_CORE (real MKSR-1–MKSR-2 interaction; uninformative term; do not remove experimental IPI) |
| GO:1905515 non-motile cilium assembly (involved_in) ×2 | IGI | PMID:18337471 / 21422230 | ACCEPT (core, redundant module function) |
| GO:1904491 protein localization to ciliary transition zone (involved_in) ×2 | IMP | PMID:26595381 / 21422230 | ACCEPT (PMID:21422230 shows MKSR-1 required for MKS-6/MKS-3 TZ localization; PMID:26595381 abstract-only, defer to curator) |
| GO:0035869 ciliary transition zone (located_in) | IDA | PMID:21422230 | ACCEPT (core CC; direct imaging) |
| GO:0008340 determination of adult lifespan (involved_in) ×4 | IGI | PMID:19208769 | KEEP_AS_NON_CORE (indirect insulin-IGF phenotype in double mutants; not a core function) |
| GO:0008104 intracellular protein localization (involved_in) | IMP | PMID:18337471 | MODIFY → GO:1904491 (the specific process is protein localization to the TZ) |
| GO:0035177 larval foraging behavior (involved_in) | IGI | PMID:18337471 | KEEP_AS_NON_CORE (downstream sensory-cilium behavior; curator full-text judgment; abstract-only cache) |

Proposed NEW: GO:1903565 negative regulation of protein localization to cilium (ciliary gate; RPI-2/TRAM-1a/MKS-3 exclusion) — mirrors mks-2 review, directly supported in the mksr-1 single mutant.

## Deep research
- Falcon deep research launched via `just deep-research-falcon worm mksr-1 --fallback perplexity-lite`. The wrapper reported a 600s timeout and the perplexity-lite fallback failed with a 401 quota error, but the underlying falcon (Edison) client actually completed at 1120s and wrote a genuine 50KB report (`mksr-1-deep-research-falcon.md`, 32 citations, artifacts folder). I read it: it independently confirms MKSR-1 = B9D1, a soluble single-B9-domain protein, obligate B9 complex with MKS-1/MKSR-2, TZ/basal-body localization and MKS-module/ciliopathy role — fully consistent with this review. It cites some additional non-cached sources (okazaki2020, zhang2010); I did NOT add those as citations since they are not in the publications cache and the review is anchored to verified cached PMIDs. This is a genuine late falcon file (kept per ground rules).
- Review grounded primarily on cached primary literature (PMID:21422230 full text; PMID:19208769, 18337471, 26595381 abstracts) and UniProt/GOA.
