# FGF8 review notes

## Scope and source availability

- This is a manual evidence review. Automated deep-research providers were globally quota-blocked, so no provider output was retried or fabricated.
- The seeded GOA set contains 193 rows. Of these, 150 are distinct Reactome-referenced copies of `GO:0005576 extracellular region`; all rows must remain separate because they preserve distinct source records.
- No seeded row is isoform-specific or negated. UniProt nevertheless records four human splice isoforms: FGF-8E (`P55075-1`), FGF-8A (`P55075-2`), FGF-8B (`P55075-3`), and FGF-8F (`P55075-4`). [file:human/FGF8/FGF8-uniprot.txt, "Event=Alternative splicing; Named isoforms=4"]
- The 11 GOA PMID caches were inspected. Only PMID:22235191 has cached full text; the other ten are abstract-only. Publisher full text was additionally inspected for PMID:18596921 and PMID:20702560, but YAML `supporting_text` is restricted to text present in the local publication caches.

## Core molecular identity

- FGF8 is a secreted precursor in the heparin-binding FGF family. UniProt records direct interactions with FGFR1, FGFR2, FGFR3, and FGFR4 and notes that heparan-sulfate glycosaminoglycans increase FGF-FGFR affinity. [file:human/FGF8/FGF8-uniprot.txt, "Interacts with FGFR1, FGFR2, FGFR3 and FGFR4. Affinity between fibroblast growth factors (FGFs) and their receptors is increased by heparan sulfate glycosaminoglycans that function as coreceptors."]
- The FGF8b-FGFR2c crystal structure directly establishes receptor engagement. FGF8b residue F32 creates an extra receptor contact also available in FGFR1c, FGFR3c, and FGFR4, explaining the stronger organizer activity of FGF8b relative to FGF8a. [PMID:16384934, "The FGF8b-FGFR2c structure shows that alternative splicing permits a single additional contact between phenylalanine 32 (F32) of FGF8b and a hydrophobic groove within Ig domain 3 of the receptor that is also present in FGFR1c, FGFR3c, and FGFR4."]
- The same study reports physiological FGF8b-FGFR1c interaction during midbrain-hindbrain development and shows that reducing FGF8b receptor affinity converts its patterning behavior toward that of FGF8a. [PMID:16384934, "we show that the FGF8 mode of receptor binding appeared as early as in nematodes and has been preserved throughout evolution"]
- Family-wide mitogenic assays establish that mammalian FGF signaling depends on ligand-receptor splice specificity and heparan-sulfate cofactors. [PMID:16597617, "FGF signaling activity is regulated by the binding specificity of ligands and receptors and is modulated by extrinsic cofactors such as heparan sulfate proteoglycans."]
- The core function should therefore be represented as extracellular FGF-receptor binding that directly participates in the FGFR signaling pathway. Growth, differentiation, migration, and tissue-patterning annotations are downstream or context-specific consequences rather than separate intrinsic activities.

## Developmental evidence relevant to annotation review

- Human FGF8 variants with reduced in-vitro activity and a mouse hypomorphic allele establish a dose-sensitive requirement in GnRH-neuron ontogeny. [PMID:18596921, "The mutant FGF8b and FGF8f ligands exhibited decreased biological activity in vitro."] [PMID:18596921, "mice homozygous for a hypomorphic Fgf8 allele lacked GnRH neurons in the hypothalamus"]
- The publisher full text of PMID:18596921 attributes hypogonadism primarily to GnRH deficiency. It also reports low bone mass in two variant carriers but explicitly calls a direct FGF8 effect on bone development possible rather than established. Consequently, `gonad development` and `bone development` are retained as non-core developmental/clinical consequences, not elevated to core molecular functions.
- Recombinant FGF8 promotes dopaminergic differentiation of human fetal mesencephalic neural progenitors, especially with forskolin. [PMID:15193767, "When NPCs were treated with FGF8 alone, the DAergic phenotype was expressed lightly."]
- In human neural cultures, the cached abstract describes FGF8/SHH specification before terminal differentiation; this is consistent with, but does not make, neuroepithelial differentiation a defining FGF8 activity. [PMID:17309880, "alpha-synuclein cytotoxicity appeared most pronounced following FGF8/SHH specification"]
- Human embryonic tooth-germ expression supports an odontogenesis context but is expression evidence, not a direct mechanistic assay. [PMID:17394220, "FGF8 expression remained in the dental epithelium at the cap stage"]
- Human mesonephric and metanephric expression supports kidney-development contexts, again as expression evidence. [PMID:18437684, "In the metanephros, FGF-8 first appeared only in the metanephric mesenchyme"]
- Full text of PMID:22235191 states that inner-hair-cell FGF8 signals through FGFR3 to induce pillar-cell differentiation, supporting FGFR signaling and a context-specific positive differentiation outcome. [PMID:22235191, "FGF8 is expressed in IHCs where it induces differentiation of PCs and formation of one row of OHCs through signaling to FGFR3"]
- Publisher full text of PMID:20702560 shows that recombinant FGF8 maintains proliferative anterior-heart-field progenitors and represses premature cardiomyocyte differentiation. This supports the negative cardiac-development annotation as a context-specific output rather than a core activity. [PMID:20702560, "FGF signaling blocks premature differentiation of cardiac progenitors in the AHF."]
- Full text of PMID:24431302 describes hindbrain-side FGF8 at the isthmic organizer, maintenance/induction of Wnt1, and Wnt1-dependent induction of midbrain dopaminergic neurons. These annotations are valid developmental outputs but not separate intrinsic molecular functions.
- The early human-gene study describes embryonic expression patterns associated with gastrulation, brain regionalization, limb/face organogenesis, and adult gonadal restriction; the cited GO annotation is an author-statement inference rather than a direct gastrulation assay. [PMID:8700553, "The temporal and spatial expression patterns of the FGF-8 gene suggest its involvement in gastrulation, regionalization of the brain, and organogenesis of the limb and face as an embryonic epithelial factor."]

## Cerebellum-module context

- For the slide-driven top-down decomposition, FGF8 belongs in the territorial-allocation layer as an isthmic-organizer signal, not as a cerebellum-specific intracellular pathway component. Conditional mouse genetics show that sustained isthmic Fgf8 represses hindbrain Otx2 and permits isthmus and cerebellum formation. [PMID:19793884, "One crucial role for sustained Fgf8 function is in repressing Otx2 in the hindbrain, thereby allowing the isthmus and cerebellum to form."]
- This cerebellar role is a tissue-specific output of the same extracellular FGFR-ligand activity. The generic receptor-to-ERK machinery remains factored into `modules/fgfr_signaling.yaml`; it should not be recopied into the FGF8 gene review.

## Curation judgments

- Core: FGFR1/FGFR2 binding, growth-factor activity, extracellular location, and participation in FGFR signaling.
- Non-core but supported: proliferation, MAPK activation, migration/chemotaxis, neurogenesis and neural patterning, dopaminergic differentiation, cardiac, gonadal, skeletal, tooth, kidney, gastrulation, and broad morphogenesis contexts.
- Over-annotation/uncertainty: `cytoplasm` describes precursor biosynthesis rather than the active secreted ligand; the broad rat-ortholog transfers for oxidative-stress and xenobiotic responses have no exposed source experiment and are left undecided.
- The obsolete `GO:0005615 extracellular space` must not be used in authored core functions; current `GO:0005576 extracellular region` is retained.
