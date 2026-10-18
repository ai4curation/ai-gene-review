# CD3D (human, P04234) review notes

Part of the ADAPTIVE_IMMUNITY project, T cell receptor trunk (CD3D, CD3E, CD3G, LCK, ZAP70, LAT, LCP2, PLCG1, NFATC1).

## Session 2026-09-30

### Setup
- `just deep-research-falcon human CD3D --fallback perplexity-lite` FAILED: falcon timed out (600s) and the perplexity-lite fallback errored ("Provider 'perplexity' not available. Available: falcon, asta, openscientist"). No deep-research file exists; the review is based on UniProt, cached publications, Reactome and QuickGO. Re-run deep research later and reconcile.
- `just fetch-gene-pmids human CD3D`: 9/9 GOA PMIDs cached. Only PMID:11390434 and PMID:32296183 have full text; the rest are abstract-only.

### Biology summary
- Single-pass type I membrane protein; extracellular Ig-like domain, TM helix, cytoplasmic tail with one ITAM (Pfam PF02189; InterPro IPR003110). PANTHER PTHR10570:SF5 (CD3 gamma/delta family) (UniProt P04234).
- Assembly: CD3 delta-epsilon dimer pairs with TCR alpha in the ER [PMID:9485181 "The TCR/CD3 complex is assembled after a series of pairwise interactions involving the formation of dimers of CD3 epsilon with either CD3 gamma or CD3 delta."].
- Structure: [PMID:31461748 "The octameric TCR-CD3 complex is assembled with 1:1:1:1 stoichiometry of TCRαβ:CD3γε:CD3δε:CD3ζζ."]; ECD packs against TCR constant domains; TM barrel.
- Signaling: one ITAM per CD3 chain phosphorylated by LCK [Reactome:R-HSA-202165 "the TCR complex include 10 ITAMs with one ITAM in each of the CD3 chains including the three tandem ITAMs in each zeta chains."].
- Ubiquitinated after TCR activation [PMID:1323144 "at least one other TCR subunit, CD3 delta, was also ubiquitinated after activation of the receptor."].
- Disease: IMD19, T-B+NK+ SCID (UniProt).
- UniProt also notes interaction with CD4/CD8 coreceptors (PMID:12215456, not cached; not used).

### Decisions
- Core MF: GO:0004888 transmembrane signaling receptor activity (IBA/IC/IEA accepted), understood as exerted within the complex. Considered whether contributes_to would be more accurate; raised as a suggested question rather than altering.
- NEW MF: GO:0030159 signaling receptor complex adaptor activity (structural role in TCR-CD3 assembly). Participation test: CD3 delta supplies structure the assembly depends on. Comparator: CD3E (NAS, PMID:9886373) and CD3G (NAS, PMID:12794121) already carry GO:0030159 in human GOA (QuickGO query 2026-09-30).
- Core CC: GO:0042105 alpha-beta T cell receptor complex; plasma membrane.
- Core BP: GO:0050852 T cell receptor signaling pathway.
- Protein binding IPI (SGTB, HuRI Y2H) -> REMOVE (uninformative).
- Identical protein binding (in vitro oligomerization of isolated cytoplasmic domain, PMID:14967045) -> MARK_AS_OVER_ANNOTATED; one CD3 delta per complex in cryo-EM.
- MHC class II receptor activity (contributes_to, IDA PMID:1323144; abstract about ubiquitination) -> KEEP_AS_NON_CORE, deferring to curator; MHC-class restriction is not a CD3D property.
- Positive thymic T cell selection (IBA/IEA/ISS from mouse Cd3d) -> KEEP_AS_NON_CORE: TCR-CD3 signaling does the work of selection, so this is participation, but it is a developmental outcome and part of the knockout phenotype is loss of receptor assembly.
- Alpha-beta T cell activation, adaptive immune response, immune system process -> KEEP_AS_NON_CORE (broad/downstream).
- Clathrin-coated endocytic vesicle membrane (Reactome TAS) -> KEEP_AS_NON_CORE (CD3D is cargo).
- Cytoplasm NAS (fetal liver precursor cells with intracellular CD3 delta) -> KEEP_AS_NON_CORE (secretory-pathway pool of a membrane protein).

### Validation
- `just validate human CD3D`: valid, no errors or warnings. All 49 supporting_text quotes checked verbatim against cached publications/Reactome.

## Deep research integration (falcon)

Session 2026-10-01. Report: `CD3D-deep-research-falcon.md` (Edison/falcon, generated 2026-09-30, after the review was written). Treated as LLM-generated secondary literature; it is built mostly from reviews (Menon 2023 Cancers; Xu 2020 PMID:32047259; Mariuzza 2020 PMID:31848223; Love 2025 PMID:40342420; Shah 2021; Hwang 2020; Moskalev 2025) plus one primary structure paper (Xin 2024 PMID:38657677). DOIs resolved to PMIDs via PubMed esearch; PMID:38657677, 32047259, 31848223 (all full text), 14602880 (no abstract in cache) and 16418397 (full text, source of the GO:0042106 NAS rows on CD3E/CD3G/CD247) cached with `just fetch-pmid`.

Note: the GO:0032395 MHC class II receptor activity (contributes_to) row is now MARK_AS_OVER_ANNOTATED (harmonised with CD3E/CD3G), superseding the KEEP_AS_NON_CORE entry in the decisions list above. Core MF stays GO:0030159 contributing to GO:0004888; nothing in the report or the primary papers argues against this.

### Claim classification (21 substantive claims)
- Confirms review (8): CD3 delta-epsilon heterodimer, type I single-pass plasma-membrane protein; 1:1:1:1 octamer stoichiometry; Ig-like ECD packing against TCR alpha constant domain; one ITAM phosphorylated by LCK (and FYN), ZAP-70 docking, 10 ITAMs per alpha-beta TCR; CD3D does not bind antigen and is a non-enzymatic structural/signal-transducing adaptor (consistent with GO:0030159 -> GO:0004888); unassembled chains are retained/degraded so CD3D is needed for surface TCR; CD3D deficiency causes SCID (IMD19), with CD3 delta/epsilon/zeta defects more severe than CD3 gamma; CxxC motif in the connecting peptide aids heterodimer formation (Xu 2020).
- Adds something new (5): ordered assembly (TCR alpha-beta binds CD3 delta-epsilon first) [PMID:32047259 "TCRαβ first binds with CD3δε, then CD3γε joins in the intermediate complex and finally CD3ζζ is incorporated to form the integrated complex"]; uncharged CD3 delta tail is cytosol-exposed and cannot recruit LCK itself [PMID:32047259 "CD3δ CD and CD3γ CD cannot independently recruit Lck, which explains why they are exposed in the cytosol but not spontaneously phosphorylated in resting T cells"]; CD3 delta ECD more compact and more negatively charged than CD3 gamma (verified in Xu 2020); CD3 delta contacts both TCR C-alpha and C-beta (verified in Xu 2020); gamma-delta T cells persist in CD3 delta deficiency (mouse verified in PMID:16418397; human PMID:14602880 has no cached abstract).
- Conflicts with review / with primary data (2): (a) gamma-delta TCR composition - report implies gamma-delta TCRs use a CD3 composition lacking CD3 delta; true for mouse (PMID:16418397) but the human cryo-EM structures in the report's own source contain CD3 delta-epsilon [PMID:38657677 "In humans, the TCRγ and TCRδ chains associate with three CD3 dimeric subunits—CD3εγ, CD3εδ and CD3ζζ—forming an octameric γδ TCR–CD3 complex"]. (b) TCR alpha Lys-258 salt bridge to CD3 delta Asp-111 and Asp-137 - see errors.
- Not relevant / not CD3D-specific (6): downstream Ras-ERK-AP-1, IP3-Ca2+-NFAT, PKC-theta-NF-kB and PI3K-AKT-mTOR branches; catch-bond/mechanosensing and allosteric triggering models; general membrane-lipid sequestration and Ca2+ release of CD3 tails; partial ITAM phosphorylation effects; immunological synapse/microcluster participation (generic, no primary CD3D data); CD3-directed immunotherapy (BiTEs, CAR-T).

### Adopted (where)
- Description: ordered assembly (Xu 2020), human gamma-delta TCR-CD3 membership (Xin 2024), CD3 does not bind antigen / transduces signal (Mariuzza 2020), uncharged non-sequestered CD3 delta tail that does not recruit LCK (Xu 2020), two ITAM tyrosines.
- core_functions[0] supported_by: PMID:31848223, PMID:32047259 (LCK recruitment), report quote (adaptor, non-enzymatic).
- core_functions[1] supported_by: PMID:32047259 (assembly order), PMID:38657677 (gamma-delta complex).
- existing_annotations: GO:0030159 NEW row + PMID:32047259 assembly-order quote; GO:0032395 MARK_AS_OVER_ANNOTATED row + PMID:31848223 quote (TCR recognises pMHC, CD3 transduces). No action changed.
- references: added PMID:31848223, PMID:32047259, PMID:38657677, PMID:16418397 and the falcon report (reference_review MEDIUM / LOW_QUALITY).

### Not acted on
- NEW part_of GO:0042106 gamma-delta T cell receptor complex: primary human evidence (Xin 2024) supports it, but QuickGO (2026-10-01) shows the human term on CD3E, CD3G, CD247, TRDC, TRGC1/2 (NAS PMID:16418397) and not on CD3D - an apparently deliberate omission based on murine stoichiometry. Per the "do not add what curators declined" rule, raised as a suggested question + experiment instead of asserting NEW.
- Dadi 2003 (PMID:14602880) human CD3 delta SCID with gamma-delta T cells: cached record has no abstract, so not quoted.
- Generic downstream pathway, mechanotransduction and immunotherapy content: not CD3D-specific; no annotation implications.
- No new MF/BP term suggested by the report beyond those already present.

### Report errors detected
- "TCRα Lys-258 ... bifurcated salt bridge with CD3δ Asp-111 and Asp-137" attributed to Mariuzza 2020 pages 8-9: the cached full text names TCR alpha Arg-253 and Lys-258 but contains no Asp-111/Asp-137 statement; Asp-137 lies in the CD3 delta cytoplasmic domain (UniProt TM 106-126), so it cannot be a TM salt-bridge partner. Xu 2020 instead says the TCR alpha lysine interacts with two aspartates in the CD3 delta-epsilon TM domains (one per chain). Likely hallucinated/garbled detail.
- gamma-delta claim overgeneralises mouse data and contradicts the human structures in the report's own cited Xin 2024 paper.
- Mariuzza 2020 cited with DOI 10.1016/s0021-9258(17)49904-2 (Elsevier JBC alias); canonical DOI 10.1074/jbc.REV119.009411 (PMID:31848223).

### Validation
- `just validate human CD3D`: valid, no errors or warnings after integration.


## Whole reassessment — 2026-10-05

The preceding journal remains unchanged. This reassessment supersedes earlier judgments where they differ. All 62 distinct raw GOA assertions, including qualifiers and supporting entities, are preserved, together with the one historical NEW adaptor proposal. The reviewed P04234 sequence and its two annotated alternative products remain exact; the interval missing in product 2 includes the canonical transmembrane helix, but no untested isoform-specific function is assigned. All existing source caches, provider output and history records remain unchanged.

The structural and signaling roles form one coherent core. Human CD3 delta-epsilon supplies extracellular and transmembrane assembly contacts, and its cytoplasmic ITAM provides a signaling interface. The complete alpha-beta receptor is an octamer; only the CD3 signaling subassembly is a hexamer. The 2019 structure resolves extracellular and transmembrane regions, not all cytoplasmic ITAM tails. Its official 2021 correction adds omitted subunit sequences and construct information; its text does not overturn the assembly result. Corrected complete construct details were not reread. [PMID:31461748](https://pubmed.ncbi.nlm.nih.gov/31461748/); [official correction](https://doi.org/10.1038/s41586-021-03245-4)

The former MHC class II OVER decision confused autonomous ligand contact with a contributes_to assertion. The official function and relation semantics permit a necessary signaling subunit of the active receptor complex. Production GO-CAM 685de18700003492 activity 685de18700003493 assigns GO:0032395 to the alpha-beta TCR complex and explicitly includes UniProtKB:P04234, with PMID:1323144 for activity and PMID:31461748 for composition. The 1992 cache is abstract-only and its exact clone/class restriction was not reconstructed. ACCEPT respects the existing curator scope; it does not make CD3D independently MHC-binding or exclusively class-II-specific. [GO:0032395](https://amigo.geneontology.org/amigo/term/GO:0032395); [GO-CAM](https://amigo.geneontology.org/amigo/model/685de18700003492); [PMID:1323144](https://pubmed.ncbi.nlm.nih.gov/1323144/)

The historical NEW signaling receptor complex adaptor activity is retained on direct structural work, not solely knockout necessity. An independent consultation recovered exact signed-main human CD3E and CD3G GOA comparators: GO:0030159 NAS PMID:9886373 and NAS PMID:12794121, respectively. Their prior AI MHCII rationales repeat the same direct-contact error and are not independent counterevidence. No additional process or redundant adaptor ancestor/descendant is proposed. [GO:0030159](https://amigo.geneontology.org/amigo/term/GO:0030159)

Supported generic binding follows the explicit project instruction. The SGTB/Q96EQ0 HuRI association changes REMOVE to KEEP_AS_NON_CORE, with exact-pair reviewed UniProt corroboration and the uninspected target supplementary entry disclosed. This is neither a new chaperone function nor a claim of physiological necessity. Recombinant CD3 delta cytoplasmic-domain oligomerization changes OVER to KEEP_AS_NON_CORE: the abstract explicitly includes delta, while the numerical affinities reported there describe zeta. No full-length physiological homomer is inferred. [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/); [PMID:14967045](https://pubmed.ncbi.nlm.nih.gov/14967045/)

Fetal-liver intracellular CD3 staining does not resolve ER/Golgi localization. The human FL121/125 clone observation and adult CD3-negative NK controls are retained without that inference. The TRIM paper's surface TCR/CD3 readout supports plasma membrane, while its separate co-IP does not detect delta: no TRIM-delta binding is invented. Reactome rows remain locations of receptor-associated material, not transfers of LCK, ZAP70, phosphatase, clathrin or dynamin catalysis. Endocytic-vesicle CD3D is cargo; the reviewed CD3 gamma dileucine motif is not reassigned to delta. [PMID:1831653](https://pubmed.ncbi.nlm.nih.gov/1831653/); [PMID:11390434](https://pubmed.ncbi.nlm.nih.gov/11390434/); [PMID:32047259](https://pubmed.ncbi.nlm.nih.gov/32047259/)

The 1998 double-TCR-heterodimer interpretation is not adopted, while its CD3 association evidence remains relevant. PAINT assertions are inherited-node judgments; target self-reference is not circular, and original IBD placement was not reconstructed. Mouse positive-selection transfers retain their provenance and developmental scope, without newly claiming a specific arrest stage or a directly verified CD4/CD8 interface. [PMID:9485181](https://pubmed.ncbi.nlm.nih.gov/9485181/)

Human gamma-delta structures explicitly contain CD3 delta-epsilon. The 2024 study separates G115 Vgamma9Vdelta2 and 9C2 Vgamma5Vdelta1 structural systems from Jurkat76/K562 activation controls. Its Expi293F ligand-production paragraph is not receptor-complex production. The 2006 murine delta-absence observation does not establish human absence; the independently inspected 2007 human study also reports delta-containing primary/cultured receptors. No unverified claim about gamma-delta preservation in human SCID is retained, and no additional complex annotation is proposed here. GO:0042101 covers the supported human alpha-beta and gamma-delta receptor contexts in the core function, but the child term GO:0042106 remains an open curation question. [PMID:38657677](https://pubmed.ncbi.nlm.nih.gov/38657677/); [PMID:16418397](https://pubmed.ncbi.nlm.nih.gov/16418397/); [PMID:17923503](https://pubmed.ncbi.nlm.nih.gov/17923503/)

Access is source-specific: all available abstracts and cached Reactome summaries were read; selected load-bearing primary/review sections are identified in reference assessments. Abstract-only caches were not rewritten as full text. The HuRI target table, complete 1992 and 1994 target experiments, all structural figure pixels and complete supplements were not independently inspected. Existing Falcon output is background only; its topology and human/mouse errors do not supply core evidence. The frozen ClinGen AR Definitive association with immunodeficiency 19 remains unchanged. This reassessment does not reinterpret the clinical classification.
