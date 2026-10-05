# ATP6AP2 notes

## Research workflow

- Ran `just fetch-gene human ATP6AP2`, which seeded the UniProt record, GOA file, cached publications, and review YAML.
- Falcon deep research has now completed successfully (`ATP6AP2-deep-research-falcon.md`, 21 citations); see the synthesis section at the end of this file. The original PN-batch attempt timed out before the `deep_research_unified` tool bugs were fixed.
- Used cached UniProt, GOA, publications, and the PN projection artifacts for this review.

## Curation synthesis

- ATP6AP2 is best treated as a V-ATPase accessory/regulatory protein rather than as a canonical chaperone or protease. UniProt summarizes it as "involved in the assembly of the lysosomal proton-transporting V-type ATPase (V-ATPase) and the acidification of the endo-lysosomal system" [file:human/ATP6AP2/ATP6AP2-uniprot.txt].
- The strongest primary evidence comes from ATP6AP2 disease and perturbation studies: missense mutations impair interaction with ATP6AP1 and V-ATPase assembly, with downstream defects in glycosylation and autophagy [PMID:29127204 "Our results suggest that ATP6AP2 has a crucial role in V-ATPase assembly, both in invertebrates and vertebrates."].
- The neuronal disease paper supports the PN proteostasis angle because ATP6AP2 deficiency caused "severe deficiency in lysosomal acidification and protein degradation" and decreased V-ATPase membrane assembly [PMID:30985297 "severe deficiency in lysosomal acidification and protein degradation leading to neuronal cell death"].
- The EV-A71/autophagy paper provides direct knockdown support for lysosomal pH control: ATP6AP2 was described as an auxiliary V-ATPase component, and ATP6AP2 knockdown significantly increased lysosomal pH [PMID:32276428 "ATP6AP2 is an important auxiliary component of the V-ATPase complex and coordinates correct V-ATPase assembly"].
- The PN projection proposes ATP6AP2 to `GO:0060590 ATPase regulator activity` from lysosomal V-ATPase regulator leaves and already recognizes `GO:0007042 lysosomal lumen acidification` as present in GOA [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv].

## PN decision

- Accept ATP6AP2 for the Proteostasis PN batch only through the Autophagy-Lysosome Pathway / lysosomal acidification / V-ATPase regulator branch.
- Add `GO:0060590 ATPase regulator activity` conservatively: ATP6AP2 is not the proton-pumping catalytic subunit, but multiple lines of evidence support an accessory/regulatory role in V-ATPase assembly and lysosomal acidification.
- Add `GO:0070072 vacuolar proton-transporting V-type ATPase complex assembly` because the primary literature explicitly supports assembly-factor biology.
- Keep Wnt signaling, CNS development, angiotensin maturation, MAPK signaling, TGF-beta production, plasma membrane/external side, and high-throughput exosome/granule localizations as non-core or over-broad where appropriate. These are real or plausible contexts but should not be used to broaden the PN proteostasis projection.

## Falcon deep research synthesis (2026-06-21)

The Falcon report (`file:human/ATP6AP2/ATP6AP2-deep-research-falcon.md`) reinforces
the PN decision above (V-ATPase accessory/assembly is the proteostasis-relevant
core; RAS/Wnt/MAPK are non-core elaborations) and adds three useful points.

**Evolutionary argument that the V-ATPase function is ancestral/primary.**
ATP6AP2 is conserved from yeast to human, and homologs that **lack renin-binding
function exist in organisms with no renin-angiotensin system**, indicating the
V-ATPase accessory role is the fundamental, conserved function and the
(pro)renin-receptor/RAS role is a vertebrate-specific elaboration
(falace2024vatpasedysfunctionin; figueiredo2021). This is a strong independent
justification for treating the V-ATPase-assembly / lysosomal-acidification
branch as core and the RAS/angiotensin annotations as non-core.

**Proteolytic processing nuance (relevant to which "form" does what).** In the
trans-Golgi, ATP6AP2 is cleaved by furin / site-1 protease (S1P) / ADAM19 into a
~28-kDa **soluble (pro)renin receptor (sPRR)** and a truncated membrane fragment
**M8.9** that remains associated with V-ATPase. Reviews describe M8.9 as the
V-ATPase-associated portion — i.e. the proteostasis-relevant activity is carried
by the membrane-retained fragment, while the soluble ectodomain participates in
RAS signaling (kourieh2025overviewofrenin). Worth noting when interpreting
isoform/fragment-specific annotations.

**Structural placement (Abbas 2020; Wang 2020).** Cryo-EM of mammalian/human
V-ATPase places the ATP6AP2/PRR transmembrane anchor inside the V0 c-ring
alongside the cleaved ATP6AP1/Ac45 anchor (enzyme ATP:H+ ratio 3:10), confirming
ATP6AP2 as a structural/assembly contributor to the membrane sector rather than a
catalytic subunit — consistent with the `GO:0070072` V-ATPase-assembly and
`GO:0060590` ATPase-regulator calls already made.

**Other corroborated (non-core) roles:** trafficking/stabilization of
LRP6/β-catenin and N-cadherin/β-catenin at the membrane (Wnt; xiong2024),
megalin/cubilin receptor-mediated endocytosis in renal proximal tubule
(figueiredo2021), and tissue-specific KO phenotypes (osteoblast bone formation,
placental trophoblast invasion, endothelial tip-cell polarity/angiogenesis). No
change to the core call.


## CLINGEN Mendelian re-review — 2026-09-29

This assessment supersedes the earlier project-specific core-function decisions above. All 67 source annotations are preserved, including qualifiers, original evidence codes and reference IDs. The two documented alternative products O75787-1 and O75787-2 are unchanged; proteolytic fragments are not additional splice isoforms. The decisions are 38 ACCEPT, 23 KEEP_AS_NON_CORE, five UNDECIDED and one MODIFY. Two earlier reviewer-authored NEW proposals are withdrawn; no GOA assertion is removed and no new annotation is added.

The synthesis has two core functions: a qualified contribution to the V-ATPase proton-pumping activity and signaling-receptor activity. The latter is supported by the original human renin/prorenin experiments, irrespective of the earlier Proteostasis project scope. The pump core uses `contributes_to_molecular_function`, not independent ATP hydrolysis or ATPase-regulator activity. ER localization remains supported, but ER is not listed as a site of the proton-pumping core. Angiotensin-maturation annotations are retained through receptor-associated cofactor action: REN performs cleavage; ATP6AP2 is neither the protease nor the substrate.

The five unresolved source assertions are the two high-throughput binding records (HuRI and the 2025 multimodal map), Golgi-lumen acidification, and the parotid-saliva and EPS-urine exosome records. Their exact target evidence was not recovered. These are explicit uncertainties, not claims that the original curators made errors. Verified generic interactions with TMEM9, ATP6AP1/VMA21 and Wnt-associated proteins are retained as non-core. Generic renin binding is refined to the existing signaling-receptor term. The original PAINT node assertions are retained without donor-count or self-evidence objections; no tree reconstruction is claimed.

### Source and assay boundaries

- [PMID:12045255, original JCI study](https://www.jci.org/articles/view/14276): human receptor cDNA and human ligands, receptor-transfected mesangial cells, binding, angiotensin-generation kinetics and ERK readouts were inspected. Receptor association decreases apparent renin Km and kcat while increasing kcat/Km. Thus improved catalytic efficiency must not be rewritten as increased intrinsic turnover. Renin-dependent ERK signaling under angiotensin-pathway blockade is a separate readout. The normal cache remains abstract-only; no figure-pixel or raw-data inspection is claimed.
- [PMID:15746149](https://pubmed.ncbi.nlm.nih.gov/15746149/): the complete cached abstract describes a human splice-altered receptor that retains renin binding/catalytic enhancement but has impaired ERK signaling. Original full Methods were not independently inspected. Existing experimental annotations are retained with that limit and independent corroboration from the original receptor study.
- [PMID:30985297, original JCI study](https://www.jci.org/articles/view/79990): targeted Results, Fig. 9 legend and fractionation/proton-pumping Methods distinguish human HeLa V1B2:V0a1 membrane association and rescue, human HEK293T lysosomal proton pumping, patient-derived neurons and conditional mouse-brain deletion. Proton pumping is not an isolated ATP6AP2 ATP-hydrolysis assay. The normal cache remains abstract-only.
- [PMID:29127204](https://pmc.ncbi.nlm.nih.gov/articles/PMC5716037/): selected human partner/localization Results and construct/IP Methods support HEK293T association with ATP6AP1 and VMA21, including endogenous ATP6AP1 co-IP, and HeLa ER/Golgi localization. Fly fat-body acidification/autophagy and mouse liver findings retain their model boundaries. The introductory synthesis sentence is labeled INTRODUCTION in the review, not ABSTRACT. Interaction with assembly factors alone does not identify a dedicated assembly step.
- [PMID:32276428](https://pmc.ncbi.nlm.nih.gov/articles/PMC7232526/): the PHB2-titled paper actually tests ATP6AP2 depletion in human RD cells and calibrated lysosomal pH. Its assembly sentence cites prior work within Results section 3.4; that sentence is background, not an assembly experiment performed here. No wrong-gene inference is made from the title.
- [PMID:33065002](https://pmc.ncbi.nlm.nih.gov/articles/PMC7655608/): human V-ATPase structural incorporation supports complex contribution. The local extraction includes abstract, Introduction and Discussion but lacks Results/Methods despite its availability flag; original indexed human HEK293F structural/purification information was checked separately. Neither structural presence nor dependence of acidification establishes autonomous ATPase catalysis.
- [PMID:20093472, original author-hosted Science reprint](https://www.researchgate.net/publication/41111578_Requirement_of_Prorenin_Receptor_and_Vacuolar_H_-ATPase-Mediated_Acidification_for_Wnt_Signaling): targeted Results and figure legends support human HEK293T Wnt responses and endogenous PRR associations with LRP6 and V0 components. Xenopus developmental phenotypes rescued with human PRR mRNA remain a distinct experimental setting. No new Wnt-ligand receptor activity is asserted.
- [PMID:30374053, original author-laboratory PDF](https://www.jparklab.org/_files/ugd/859c99_a8d90bb1adab435c9f87f9dd92bcbb06.pdf): selected Results, Fig. 3 caption and ATPase Methods support ATP6AP2 interactions and depletion-dependent Wnt effects. ATPase measurements use ATP6AP2-associated complexes while varying TMEM9; they do not isolate ATP6AP2 modulation of an otherwise fixed enzyme.
- [PMID:16374430](https://pubmed.ncbi.nlm.nih.gov/16374430/): the complete abstract includes human and rat mesangial-cell responses, with receptor-siRNA explicitly in rat. This is retained as a downstream cellular context, without inventing a human receptor-knockdown experiment.

All 15 cached PMID abstracts and four cached Reactome summaries were inspected in the independent annotation consultation. No complete-paper, full supplemental-screen or figure-pixel coverage is claimed. Reference entries record the individual reading limits and preserve cache-availability flags. Quotes are literal substrings of the existing source files; externally read text is not represented as cached full text. The Falcon report was used for research leads, not as primary assay evidence. Its earlier claim of ATP6AP2 conservation from yeast to human is not adopted without an appropriate phylogenetic analysis.

### Target-level database checks

The [original NIH/NHLBI urinary-exosome inventory](https://esbl.nhlbi.nih.gov/UrinaryExosomes/) identifies ATP6AP2, historical NP_005756, one peptide and reference 2, linked to PMID:19056867. This supports contextual occurrence; it does not establish spectra quality, modern isoform identity, topology or vesicular activity. The distinct PMID:19199708 and PMID:23533145 target-table entries remain unverified.

Official human Reactome records [R-HSA-6799717](https://reactome.org/content/detail/R-HSA-6799717), [R-HSA-6800921](https://reactome.org/content/detail/R-HSA-6800921) and [R-HSA-2022356](https://reactome.org/content/detail/R-HSA-2022356) resolve ATP6AP2 target membership in tertiary-granule, ficolin-rich granule and plasma-membrane sets. The generic cached event prose alone did not establish those target-level memberships. Exocytosis membership is not an exocytosis-catalyst function.

Mouse Q9CYN9, rat Q6AXS4 and bovine P81134 donor identities were checked in official database records; underlying donor assays were not all independently read. The [official mouse Atp6ap2 record](https://www.informatics.jax.org/marker/gograph/MGI:1917745) corroborates donor synaptic-vesicle acidification annotations. No O75787/ATP6AP2 hit was found in the local GO-CAM index, which is not a claim of global absence.

### Withdrawn proposals and remaining mechanistic questions

The earlier `GO:0060590 ATPase regulator activity` NEW proposal over-interpreted assembly/acidification dependence as binding-mediated ATP-hydrolysis regulation. The earlier human IMP `GO:0070072` proposal did not resolve a dedicated assembly step from stable-complex abundance and perturbation. Withdrawal of these authored proposals does not refute assembly biology.

A positive research lead remains: [DOI:10.1091/mbc.E18-04-0234](https://doi.org/10.1091/mbc.E18-04-0234). The official abstract and Fig. 1 caption describe fly ATP6AP2 with a Voa1 signal peptide rescuing a sensitized yeast strain, improved by fly ATP6AP1 coexpression. Growth and quinacrine acidification are measured, with an ER-retrieval dependence. This is stronger assembly-support evidence, but is not the prior human IMP experiment. Its full normal-pipeline source is not cached and no annotation is added from this lead. A future species-aware assembly assessment should resolve the performed step and use appropriate comparators.

The bounded comparator check found an assembly annotation for mouse Vma21 and no exact matching term in the inspected local ATP6AP1 review. A broader QuickGO comparison did not return usable evidence; no systematic absence across species is claimed. Official GO definitions support the two retained core activities and distinguish receptor signaling, peptidase activation and complex assembly. No extra peptidase-activator core or redundant parent/child annotation is added.


## PR 3548 follow-up: receptor cofactor activity and core specificity

The two existing angiotensin-maturation annotations remain ACCEPT and are now represented in the receptor core. Re-reading the original [JCI receptor study](https://www.jci.org/articles/view/14276), particularly the ligand/activity Methods and kinetic Results, confirms increased renin-associated catalytic efficiency in membrane experiments normalized for renin quantity. This is cofactor participation, not merely necessity. Both apparent Km and kcat decrease; the efficiency increase must not be described as increased turnover. The receptor-negative membrane controls support the receptor-associated effect without proving a uniquely allosteric mechanism. The already cached abstract quotation is used in the core. No NEW annotation or protease function is added.

The receptor MF and existing renin-binding replacement now use [GO:0004888 transmembrane signaling receptor activity](https://amigo.geneontology.org/amigo/term/GO:0004888). The endolysosomal pump core uses [GO:0016471 vacuolar proton-transporting V-type ATPase complex](https://zfin.org/GO:0016471), retaining the qualified contribution to proton-pumping activity. Plasma membrane remains the receptor location: the [current GO topology guidance](https://geneontology.org/docs/faq/#how-are-membrane-proteins-described-in-go) assigns transmembrane proteins to the membrane itself. The older displayed external-side definition is broader; existing experimentally curated external-side assertions are preserved rather than mechanically replaced.

Four broad location annotations are retained as non-core context. Vacuolar acidification, intracellular pH reduction and proton transport remain core processes: their central mechanistic role is not made peripheral by the use of specific acidification terms in a concise core synthesis. The resulting 67 source rows are 34 ACCEPT, 27 KEEP_AS_NON_CORE, five UNDECIDED and one MODIFY. Both alternative products and every source assertion remain unchanged.

The HuRI WITH/FROM partners are O00526, O95183, P21854, P42857, P53801, Q01453, Q16617, Q5BJF2, Q969S6, Q96IW7 and Q9NPL8; the 2025 map lists O00526. The uncertainty is at the individual assay/construct level, not the partner-identifier level. The separate exosome studies retain source-specific judgments: a verified urinary entry does not itself verify an entry from a distinct fluid and study.

The generic-binding policy difference remains explicit. The three experimentally supported partner interactions stay KEEP_AS_NON_CORE under the project action definitions, rather than using REMOVE to label uninformative but supported interactions incorrect. Their withdrawn ATPase-regulator/assembly replacements remain withdrawn. No change to the shared policy is included in this gene PR. The fourteen existing UNVERIFIED reference judgments remain unchanged: a reviewer suggestion and matching cached metadata alone do not constitute new source verification. A bounded independent annotation/core consultation supports the receptor cofactor and specificity changes; no whole-paper, figure-pixel or full supplementary-data reading is claimed.
