# P3H2 (Prolyl 3-hydroxylase 2; LEPREL1) — review notes

UniProt: Q8IVL5 (P3H2_HUMAN), 708 aa precursor, EC 1.14.11.7. Synonyms: LEPREL1, MLAT4 (Leprecan-like protein 1 / myxoid liposarcoma-associated protein 4). HGNC:19317. Member of the leprecan/prolyl 3-hydroxylase family (P3H1/P3H2/P3H3).

## Core molecular function

P3H2 is an ER-lumenal 2-oxoglutarate/Fe(II)-dependent dioxygenase that catalyzes the post-translational formation of (trans-)3-hydroxyproline on collagen prolyl residues.

- Catalytic reaction (UniProt): "L-prolyl-[collagen] + 2-oxoglutarate + O2 = trans-3-hydroxy-L-prolyl-[collagen] + succinate + CO2" [EC 1.14.11.7; ECO:0000269|PubMed:18487197].
- UniProt FUNCTION: "Prolyl 3-hydroxylase that catalyzes the post-translational formation of 3-hydroxyproline on collagens (PubMed:18487197)." and "Catalyzes hydroxylation of the first Pro in Gly-Pro-Hyp sequences where Hyp is 4-hydroxyproline (PubMed:18487197). Has no activity on substrates that lack 4-hydroxyproline in the third position (PubMed:18487197)."
- Substrate preference for basement-membrane collagen IV: UniProt "Has high activity with the type IV collagen COL4A1, and lower activity with COL1A1 (PubMed:18487197)."

Experimental characterization [PMID:18487197 "A large amount of P3H activity was found in the P3H2 samples with (Gly-Pro-4Hyp)5 as a substrate"] and [PMID:18487197 "P3H2 hydroxylated more effectively two synthetic peptides corresponding to sequences that are hydroxylated in collagen IV than a peptide corresponding to the 3-hydroxylation site in collagen I. These findings suggest that P3H2 is responsible for the hydroxylation of collagen IV, which has the highest 3-hydroxyproline content of all collagens."]. The enzyme is distinct from P3H1 in that it does not require CRTAP for activity [PMID:18487197 "coexpression with CRTAP did not enhance the solubility or activity of the recombinant P3H2"], and its 2-oxoglutarate Km/Ki resemble lysyl hydroxylases rather than C-P4Hs [PMID:18487197 "The Km and Ki values of P3H2 for 2-oxoglutarate and its certain analogues resembled those of the LHs rather than the C-P4Hs"].

## Cofactors (catalytic supporting, non-core)

As a 2-OG/Fe(II) dioxygenase, P3H2 requires Fe(II) and uses L-ascorbate (vitamin C) as cofactor.
- UniProt COFACTOR "Name=Fe cation" and "Name=L-ascorbate" [ECO:0000305|PubMed:18487197]; kinetic parameters "KM=0.5 uM for Fe(2+)" and "KM=110 uM for ascorbate".
- UniProt KW: "Iron; Metal-binding; Oxidoreductase; Vitamin C." and the Fe2OG dioxygenase domain (residues 557-671) with Fe-binding residues 580/582/652.
Iron ion binding (GO:0005506), L-ascorbic acid binding (GO:0031418), and the oxidoreductase-on-paired-donors parent (GO:0016705) are accurate catalytic/structural attributes but subsidiary to the informative MF (procollagen-proline 3-dioxygenase activity, GO:0019797).

## Subcellular location

ER lumen / ER is the site of action (collagen modification occurs co/post-translationally in the ER before secretion). UniProt: "SUBCELLULAR LOCATION: Endoplasmic reticulum ... Sarcoplasmic reticulum ... Golgi apparatus." Contains a C-terminal ER-retention signal (residues 705-708, "Prevents secretion from ER"; PROSITE ER_TARGET; the KDEL-type motif).
- ER + Golgi localization shown by IF [PMID:15063763 "LEPREL1 is localized to the ER and Golgi network and over-expressing it affects normal protein disulfide isomerase staining patterns in the ER."].
- Reactome (TAS) places it in ER lumen (R-HSA-1980233, R-HSA-8948226, R-HSA-8948230) — consistent and the most precise CC term.
- Sarcoplasmic reticulum is the specialized ER of muscle; consistent with strong muscle expression and the 200 kDa muscle-specific transcript [PMID:15063763 "Muscle tissue contains a specific 6.5 kb transcript and a 200 kDa protein"]. Keep but non-core.
- Basement membrane (GO:0005604, ISS/IEA from mouse ortholog Q8CG71) is the location of the COLLAGEN IV substrate/product, not where the enzyme itself acts; the enzyme is ER-resident. Treat as non-core (mark over-annotated) — P3H2 acts in the ER on procollagen, not in the assembled basement membrane.

## Biological process

- collagen metabolic process (GO:0032963) and peptidyl-proline hydroxylation (GO:0019511) — both correct and directly supported by IDA [PMID:18487197].
- Contributes to 3-hydroxylation of COL4A1 and COL1A1 in tendon, eye sclera, lens capsule (UniProt, by similarity).

## Disease

Loss-of-function variant (G508V) causes autosomal-recessive high myopia with cataract and vitreoretinal degeneration (MCVD, MIM:614292) [UniProt DISEASE; PubMed:21885030]. Consistent with a role in basement-membrane/eye collagen biogenesis.

## Cancer / proliferation annotation (PMID:19436308)

P3H2 (and P3H3) are epigenetically silenced by promoter CpG methylation in breast cancer; ectopic re-expression suppresses colony formation, suggesting a tumor-suppressor-like activity [PMID:19436308 "Ectopic expression of P3H2 and P3H3 in cell lines with silencing of the endogenous gene results in suppression of colony growth."]. This is the basis for the GO:0008285 (negative regulation of cell population proliferation) IDA annotation. The colony-suppression assay is real and gene-specific (P3H2 cDNA into MCF7 and T47D), so the experimental annotation should not be removed; however this is a context-dependent/indirect phenotype (overexpression in cancer cell lines), not the enzyme's core ER collagen-modifying function. Keep as non-core. Full text available and verified.

## Annotation strategy summary

- Core MF: GO:0019797 procollagen-proline 3-dioxygenase activity — ACCEPT as core (IDA PMID:18487197; IBA; IEA all converge).
- ER (GO:0005783) / ER lumen (GO:0005788) — ACCEPT (IDA, TAS); ER lumen is most precise.
- collagen metabolic process (GO:0032963), peptidyl-proline hydroxylation (GO:0019511) — ACCEPT.
- iron ion binding (GO:0005506), L-ascorbic acid binding (GO:0031418), oxidoreductase activity on paired donors (GO:0016705) — KEEP_AS_NON_CORE (catalytic cofactor/structural support).
- Golgi (GO:0005794), sarcoplasmic reticulum (GO:0016529) — KEEP_AS_NON_CORE (secondary localizations).
- basement membrane (GO:0005604) — MARK_AS_OVER_ANNOTATED (location of substrate, not enzyme; ortholog transfer).
- negative regulation of cell population proliferation (GO:0008285) — KEEP_AS_NON_CORE (real IDA but indirect tumor-suppressor phenotype).
- No bare protein binding (GO:0005515) annotation present in this GOA.

## Falcon deep-research findings (incorporated 2026-06)

Falcon surfaced three genuinely new, verified P3H2-specific references (all PubMed-confirmed; none in publications cache, so added as reference ids without paraphrased supporting_text):

- In vivo confirmation that P3H2 is the principal collagen IV 3-hydroxylase, via a P3H2-knockout cell line: "we confirm that P3H2 is the major, but not the only 3-Hyp-modifying enzyme of type IV collagen" [PMID:29491144 (DOI 10.1074/jbc.RA117.000406)]. This corroborates the existing IDA collagen IV substrate-specificity annotation with knockout (rather than recombinant-peptide) evidence.
- 3-Hyp on collagen IV modulates its protein interactions: reduced 3-Hyp increases glycoprotein VI (GP6) binding, whereas 3-Hyp is required for nidogen 1/2 binding [PMID:29491144 "binding data consistent with a major role of 3-Hyp in interactions of collagen IV with glycoprotein VI and nidogens 1 and 2"]. Mechanistic link between P3H2 activity and basement-membrane assembly partners (not previously in review).
- New renal disease association: P3H2 is a glomerular basement membrane (GBM) modifier; podocyte-specific loss in mice causes thin basement membrane nephropathy (TBMN) with progressive microhematuria/microalbuminuria, and P3H2 loss/mutation causes TBMN and FSGS in mice and humans [PMID:35499085 (DOI 10.1172/JCI147253) "P3H2 protein is the first identified GBM modifier, and loss or mutation of P3H2 causes TBMN and focal segmental glomerulosclerosis in mice and humans"]. Complements the previously-noted ocular MCVD high-myopia phenotype; in vivo proof of collagen IV as the physiological substrate (GBM proteomics shows decreased collagen IV subchains on P3H2 loss). Added as HIGH relevance.
- Angiogenesis role: P3H2 is induced by VEGF-A via VEGFR-2/p38 MAPK in endothelial cells and, through its collagen IV activity, supports angiogenesis; knockdown reduces pathological choroidal neovascularization in vivo [PMID:33918807 (DOI 10.3390/ijms22083896) "P3H2 is a new molecular player involved in new vessels formation and could be considered as a potential target for anti-angiogenesis therapy"]. Added as MEDIUM relevance (context-dependent physiological role downstream of the core MF).
- These are additive references only; no `action:` changes (review was COMPLETE). The findings reinforce, rather than alter, the core MF (GO:0019797, collagen IV-preferring prolyl 3-hydroxylase) and the ER site of action. The Aypek/Montgomery in vivo evidence further supports that "basement membrane" (GO:0005604) is the destination of the collagen IV substrate, consistent with the existing MARK_AS_OVER_ANNOTATED decision for that CC term on the enzyme itself.
