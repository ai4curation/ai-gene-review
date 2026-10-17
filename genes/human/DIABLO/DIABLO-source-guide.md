# DIABLO evidence guide

DIABLO/SMAC antagonizes inhibitor-of-apoptosis proteins after mitochondrial release. One BIR-binding core summarizes this activity, including XIAP and BIRC6, in the cytosol. Mature SMAC occupies the mitochondrial intermembrane space; its canonical processing intermediate is associated with the inner membrane. MPP and PARL perform the precursor cleavage; DIABLO is not assigned their protease activity.

This review applies the [ClinGen project curation instructions](https://github.com/ai4curation/ai-gene-review/blob/98ae322b9bb97f58c6f12c093c97f645ca33da76/projects/CLINGEN_MENDELIAN.md#curation-instructions). Positive interaction evidence is retained as non-core when no supported, more informative molecular-function term is available. A partner-class refinement describes binding capacity; it does not assign the partner's catalytic or transport activity to DIABLO. Broader sound annotations use MODIFY with supported replacements, including where the specific term is already represented. No new annotation is proposed.

## Primary mechanism and product scope

| Source and actual access | Evidence used and limits |
|---|---|
| [PMID:10929711](https://pubmed.ncbi.nlm.nih.gov/10929711/), published abstract | IAP antagonism and mitochondrial release; complete original was not recovered. |
| [PMID:10972280](https://doi.org/10.1038/35022514), [author-uploaded original](https://www.researchgate.net/publication/232749020_Structural_and_biochemical_basis_of_apoptotic_activation_by_SmacDIABLO), Results/Figures 3–5, Table 2 and Methods | Purified SMAC binding to XIAP BIR2/BIR3 and relief of caspase inhibition. Procaspase-3 reconstitution uses mouse XIAP 1–356; the mature-caspase-3 assay uses human XIAP 124–240. The free-SMAC crystal is not an IAP co-crystal. The del4 construct retains weak binding and partial activity, qualifying the older notes' absolute claim about four indispensable residues. |
| [PMID:28288130](https://doi.org/10.1038/ncb3488), published abstract and [publisher supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fncb3488/MediaObjects/41556_2017_BFncb3488_MOESM16_ESM.pdf), S2/S3/S6/S7/S8 | Human-cell processing/fractionation, MPP/PARL perturbations and XIAP-depletion controls. The complete main article was unavailable. S8 includes construct/pathway diagrams; the mature-SMAC rescue conclusion also depends on the published abstract, not the diagram alone. |
| [PMID:36758106](https://doi.org/10.1126/science.ade8840), published abstract; separately, [2022 preprint](https://www.researchgate.net/publication/363182857_Structural_basis_for_antagonism_of_the_ubiquitin_ligase_BIRC6_by_SMAC), DOI 10.1101/2022.08.30.505748, Results pp. 7–8 and Methods pp. 20–21 | The published abstract establishes SMAC competition with caspases for BIRC6. The preprint supplies separately attributed BIR/DOC-interface and construct context: bacterial SMAC 56–239 with removable His–SUMO. A tested docked pose is not resolved atomic density. Published full text was not recovered. |
| [PMID:15200957](https://pubmed.ncbi.nlm.nih.gov/15200957/), published abstract | Reports both SMAC antagonism of BRUCE/BIRC6 and SMAC ubiquitination. The old substrate-only quotation is insufficient to support antagonism; this does not invalidate the paper's other findings. |

The [official Q9NR28 record](https://www.uniprot.org/uniprotkb/Q9NR28/entry) distinguishes three splice products. Canonical Q9NR28-1 has 239 residues; its 22–239 intermediate and 56–239 mature chain are processing states. Q9NR28-2/Diablo-S has 186 residues after replacement of canonical 1–60 by MKSDFYF. Q9NR28-3/SMAC3 has 195 residues after deletion of 62–105. Canonical processing is not automatically assigned to both alternatives.

The [PMID:10950947 author-uploaded original](https://www.researchgate.net/publication/12369918_Molecular_Determinants_of_the_Caspase-promoting_Activity_of_SmacDIABLO_and_Its_Role_in_the_Death_Receptor_Pathway), Methods and short-product/TRAIL Results, supports a cytosolic short product with weak initiation but partial effector-caspase relief. The TRAIL experiment uses an engineered caspase-8-cleavable GFP–SMAC construct. It supports a contextual death-receptor-pathway contribution, not receptor binding or a separate core.

The [PMID:14523016 author-uploaded original](https://www.researchgate.net/publication/9068810_Smac3_a_Novel_SmacDIABLO_Splicing_Variant_Attenuates_the_Stability_and_Apoptosis-inhibiting_Activity_of_X-linked_Inhibitor_of_Apoptosis_Protein), Methods and localization/binding Results, identifies human SMAC3 by RT-PCR and tests tagged localization, release and XIAP BIR2/BIR3 binding. N-terminal tags impair the binding assay. Its Results/Figure 2 explicitly infer IMS residence from cytochrome-c colocalization, but do not directly resolve submitochondrial topology or establish canonical PARL processing for SMAC3. Neither alternate product is labeled universally inactive.

## Interaction evidence

Specific IAP binding is supported by domain/peptide experiments and independent mechanistic studies. [PMID:16282325](https://www.researchgate.net/publication/7486709_Distinct_BIR_Domains_of_cIAP1_Mediate_Binding_to_and_Ubiquitination_of_Tumor_Necrosis_Factor_Receptor-associated_Factor_2_and_Second_Mitochondrial_Activator_of_Caspases), Methods, BIR-mutant Results and Figure 6, separates BIRC2 BIR3 recognition of SMAC from BIR1 recognition of TRAF2. [PMID:21536684](https://pubmed.ncbi.nlm.nih.gov/21536684/) and [PMID:23251006](https://pubmed.ncbi.nlm.nih.gov/23251006/) provide recombinant/cellular binding comparisons. A BIR-containing interface does not imply that every isolated BIR fragment suffices. The PRKCD pair in [PMID:22465666](https://pubmed.ncbi.nlm.nih.gov/22465666/) is refined to serine/threonine-kinase binding from its verified partner class and positive co-immunoprecipitation, without assigning kinase activity to DIABLO.

For the high-throughput maps, [PMID:25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/) specifies at least three positive attempts among four sequence-confirmed retests. [HuRI, PMID:32296183](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/), main text describing retesting, establishes quadruplicate testing and sequence confirmation; the earlier paper's numerical threshold is not transferred to HuRI. The exact DIABLO pairs have validated two-hybrid, array and pooled-screen records. Their mapped DIABLO sequence is the 239-residue precursor, not automatically the mature 184-residue chain. Yeast fusion assays establish binding capacity without demonstrating native compartment access, endogenous coexpression, quantitative stoichiometry or pair-specific orthogonal validation.

The table identifies the HuRI partner products and the supported interpretation. Public interaction records can be queried through [IntAct for Q9NR28](https://www.ebi.ac.uk/intact/search?query=Q9NR28), using the partner accession and PMID:32296183 together; an interaction accession alone need not uniquely identify a binary expansion.

| Partner | Tested accession | Interpretation |
|---|---|---|
| MPC2 | O95563 | Transmembrane-transporter binding; no pyruvate-transport regulation claim. |
| SYP | P08247 | Non-core; synaptic-vesicle protein does not establish a DIABLO neurotransmission role. |
| ATP6V0C | P27449 | Transmembrane-transporter binding to the proton-pore component, not ATPase catalysis. |
| APOC4 | P55056 | Non-core; native encounter with a secreted protein remains unresolved. |
| EHHADH | Q08426 | Enzyme binding; native peroxisomal encounter and DIABLO beta-oxidation activity are unproven. |
| ARL6IP1 | Q15041 | Non-core; membrane shaping does not make the partner a small GTPase. |
| MTFR1 | Q15390 | Non-core; association does not establish mitochondrial-fission work by DIABLO. |
| MIC13 | Q5XKP0 | Non-core; MICOS assembly component, without demonstrated DIABLO complex membership. |
| RHBDD2 | Q6NTF9-3 | Non-core; 223-residue product lacks canonical 1–141; protease activity is not established. |
| AGTRAP | Q6RW13-2 | Non-core; 152-residue product, also represented in the earlier isoform map. |
| DGAT2L6 | Q6ZPD8 | Enzyme binding; no native ER encounter or DIABLO lipid-synthesis claim. |
| HSD17B13 | Q7Z5P4 | Enzyme binding; mapped 300-residue displayed product is named isoform 2 by UniProt. |
| CMTM4 | Q8IZR5-2 | Non-core; 208-residue product lacks canonical 209–234. |
| SLC66A2 | Q8N2U9 | Non-core; a solute-carrier name alone does not establish transport activity. |
| FADS6 | Q8N9I5 | Non-core; three source checksums differ from the current 368-residue sequence; cause unresolved. |
| SFT2A | Q8WV19 | Non-core; no DIABLO vesicle-fusion mechanism demonstrated. |
| SEC22A | Q96IW7 | Non-core; a SNARE-family partner is not necessarily a syntaxin. |
| DHRS1 | Q96LJ7 | Enzyme binding; no native ER encounter or DIABLO oxidoreductase activity demonstrated. |
| RMDN2 | Q96LZ7 | Non-core; source marks partner residues 14–410 as sufficient binding region. |
| SLC17A9 | Q9BYT1 | Transmembrane-transporter binding; no native vesicular encounter or transport regulation claim. |
| DERL2 | Q9GZP9 | Non-core; ERAD association alone does not establish a catalytic or transporter class. |
| STMN4 | Q9H169-2 | Non-core; reconstructed 216-residue product, without a DIABLO microtubule function. |
| TIMMDC1 | Q9NPL8 | Non-core; respiratory-complex assembly is not protein-folding chaperone activity. |
| FKBP7 | Q9Y680 | Enzyme binding; the normal ER-lumen context is not recreated by the yeast assay. |

The applicable current definitions are [transmembrane transporter binding, GO:0044325](https://www.ebi.ac.uk/QuickGO/term/GO:0044325), [enzyme binding, GO:0019899](https://www.ebi.ac.uk/QuickGO/term/GO:0019899) and [protein serine/threonine kinase binding, GO:0120283](https://www.ebi.ac.uk/QuickGO/term/GO:0120283). Each refinement uses the specific tested partner's documented function, rather than its name alone.

[BioPlex, PMID:33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/), uses C-terminally tagged human baits in HEK293T/HCT116. [PMID:40205054](https://pubmed.ncbi.nlm.nih.gov/40205054/) supplies U2OS AP–MS and a [public network](https://www.ndexbio.org/viewer/networks/95bc75d5-d1d1-11ee-8a40-005056ae23aa): DIABLO node 615838 has XIAP edge 618114, BIRC2 edge 618120 and MTFR1 edge 618122. These establish co-complex association. XIAP/BIRC2 BIR refinements also rely on independent domain experiments; the AP–MS studies alone do not show direct binary binding.

## Localization and pathway records

IMS localization is supported by the maturation literature and mature-chain Reactome entities. The canonical inner-membrane processing intermediate is separately supported by the intramembrane-cleavage result in PMID:28288130. Broad gene-level rows cover both compartments; SMAC3 and the mature release-focused source retain their narrower IMS scope. These refinements do not claim that every source resolves submitochondrial location or that each splice product follows canonical processing. HPA microscopy reports mitochondria and cytosol. The [MitoCoP original supplementary workbook](https://ars.els-cdn.com/content/image/1-s2.0-S1550413121005295-mmc2.xlsx), sheet A row 309 and sheet B row 281, includes DIABLO through the literature-supported pool with no valid localization ratios; it is not an independent new IMS measurement. The protein group includes Q9NR28 and Q9NR28-3, without resolving their individual behavior.

| Public Reactome event | Target entity and role |
|---|---|
| [R-HSA-114307](https://reactome.org/content/detail/R-HSA-114307) | Release of mature DIABLO: [entity 64637](https://reactome.org/ContentService/data/query/64637), residues 56–239 in IMS, becomes [114298](https://reactome.org/ContentService/data/query/114298) in cytosol. The event's outer-membrane compartment is not the protein's steady-state location. |
| [R-HSA-9627106](https://reactome.org/content/detail/R-HSA-9627106) | [Dimer 9627054](https://reactome.org/ContentService/data/query/9627054) contains two copies of cytosolic entity 114298. |
| [R-HSA-9627350](https://reactome.org/content/detail/R-HSA-9627350) | XIAP binding yields [complex 9627391](https://reactome.org/ContentService/data/query/9627391), containing the DIABLO dimer and XIAP. |
| [R-HSA-114354](https://reactome.org/content/detail/R-HSA-114354) | DIABLO binds the XIAP–caspase-7 assembly to form [114353](https://reactome.org/ContentService/data/query/114353). |
| [R-HSA-114392](https://reactome.org/content/detail/R-HSA-114392) | Dissociation releases caspase-7 and retains the DIABLO–XIAP complex. These roles do not assign caspase catalysis to DIABLO. |

## Propagation and contextual processes

The PAINT [PTHR32247 family](https://www.pantherdb.org/panther/family.do?clsAccession=PTHR32247) places the mitochondrial, oxidative-stress-apoptosis and neuronal-apoptosis IBDs at ancestral node PTN001283560, on the human lineage. Human leaf PTN002529272 and mouse leaf PTN000790380 descend from it. Human DIABLO appearing as an experimental source for mitochondrial localization is legitimate target grounding. The aligned mature N-terminal AVPI motif is human 56–59 and mouse 54–57; conservation supports compatibility, not automatic proof of every cellular context.

The oxidative-stress donor is supported by [PMID:16085184](https://pubmed.ncbi.nlm.nih.gov/16085184/), abstract only: C2C12 expression/antisense and peroxide experiments. [PMID:14623868](https://pubmed.ncbi.nlm.nih.gov/14623868/), selected original Methods/Results, tests recombinant SMAC plus cytochrome c in mouse sympathetic neurons with a motif control. Endogenous SMAC release alone is insufficient in the tested wild-type context. Both process inferences are retained as contextual, non-core roles; neither a short donor list nor target self-inclusion invalidates PAINT placement.

[PMID:20614026](https://pubmed.ncbi.nlm.nih.gov/20614026/), original Table 1, recruitment Results and capture Methods, detects mouse SMAC in activated CD40 complexes. Tail deletion and TRAF2 controls support the contextual complex and membrane-side ISS annotations. The human-ectodomain/mouse-tail chimera does not turn this into a human-cell experiment, and co-complex recruitment does not prove direct CD40 binding.

[PMID:12642862](https://www.nature.com/articles/1206322), published abstract, reports G0/G1 arrest and reduced BrdU incorporation after mature-SMAC overexpression in human K562/CEM cells. This independently supports a non-core cell-cycle effect. The imported PMID:19153467 cell-cycle linkage remains explicitly unverified; no physiological mechanism or second core is inferred.

The current [survivin-complex definition, GO:1990713](https://www.ebi.ac.uk/QuickGO/term/GO:1990713), specifies an anti-apoptotic complex and states: “Complex contains a component which belongs to the family of baculoviral IAP (inhibitor of apoptosis) repeat-containing proteins.” Its definition xrefs include [PMID:19153467](https://pubmed.ncbi.nlm.nih.gov/19153467/). The current BIRC5 example and narrow survivin-homodimer synonym do not replace that broader definition. The original abstract and curated peptide/domain records ([IM-22028-2](https://www.ebi.ac.uk/intact/search?query=IM-22028-2), [IM-22028-4](https://www.ebi.ac.uk/intact/search?query=IM-22028-4)) establish human SMAC 56–61 peptide association with BIRC2 BIR3, without establishing an endogenous full-length BIRC5 assembly. The annotation remains contextual and non-core.

The official [ARBA00027745](https://www.uniprot.org/arba/ARBA00027745) and [ARBA00028303](https://www.uniprot.org/arba/ARBA00028303) condition sets include target-matching FunFam 1.20.58.70:FF:000012, with Vertebrata and Mammalia respectively. Their broad positive-apoptosis and intrinsic-signaling conclusions are distinguished. InterPro family/fold mappings through [IPR015142](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR015142/) and [IPR009062](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR009062/) support broad localization/process calls; independent target experiments support the specific refinements.

## Access and quotation scope

The [review YAML](DIABLO-ai-review.yaml) records source-specific assessments for every PMID. Abstract-only cache flags are unchanged even when an original was separately read. Author-uploaded originals, publisher supplements and the BIRC6 preprint are labeled by their actual form above. Short quotations appear in the YAML once per intended claim; inherited notes remain unchanged. The combined quotation budget includes those inherited notes. Failed provider access produced no provider-named research text.

## Regulatory refinement and product-specific location

[GO:2001244](https://www.ebi.ac.uk/QuickGO/term/GO:2001244), positive regulation of intrinsic apoptotic signaling pathway, is a typed is_a/part_of descendant of both GO:0043065 and GO:0042981. It preserves the positive-control meaning of the broad annotations. PMID:10972280, Figure 3 and Methods headed Assay for activation of procaspase-3 and Assay for enzymatic activity of mature caspase-3, reconstitutes relief of XIAP inhibition. The former uses mouse XIAP 1–356; the latter uses human XIAP BIR2 124–240. Pathway membership GO:0097193 alone does not provide the regulatory ancestry.

The ATP6V0C and DGAT2L6 partner-class refinements retain their binary-assay and native-context limits. The [ATP6V0C official FUNCTION/SUBUNIT record](https://www.uniprot.org/uniprotkb/P27449/entry) identifies the protein as a proton-pore component of the transporter complex, and GO:0044325 includes transporter proteins or complexes. The [DGAT2L6 official FUNCTION record](https://www.uniprot.org/uniprotkb/Q6ZPD8/entry) contains experimentally supported acyltransferase activity; the conclusion does not rest on its name alone. The single IAP-antagonism core already describes the performed mechanism; no duplicate sequestering core is added.
