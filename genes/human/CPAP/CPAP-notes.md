# CPAP research notes

## 2026-10-12 — Biological synthesis

CPAP (formerly CENPJ; HGNC:17272, Q9HC77) binds tubulin and couples its incorporation to centriole construction. The strongest integrated description is controlled centriole elongation, with a tubulin-binding molecular activity, centriolar location and membership in a CPAP–STIL procentriole assembly complex. Replication, elongation and localization annotations describe related aspects of that work; they are not independent enzymes.

The original aster assay combines human centrosomes with bovine tubulin. It supports CPAP contribution to astral nucleation but does not show that purified CPAP alone nucleates microtubules. Native gamma-tubulin co-IP/cosedimentation supports association with a broad gamma-tubulin complex. The paper explicitly leaves precise composition unresolved, so the small-complex source assignment is generalized while gamma-tubulin binding remains positive non-core context ([PMID:11003675](https://pmc.ncbi.nlm.nih.gov/articles/PMC86375/)).

The direction of microtubule effects depends on what was tested. Human PN2-3(311–422) and high full-length expression inhibited assembly in the original experiments ([PMID:15047868](https://pmc.ncbi.nlm.nih.gov/articles/PMC420094/): "this 112-residue CPAP also binds to tubulin dimers"). Later engineered CPAPmini/CPAPlong reconstitution showed slower growth with stabilization, whereas human PN2-3EX121–1060 modestly enhanced growth in another configuration. Full-length cellular experiments connect these tubulin contacts to centriole length, but neither a universal polymerase nor a universal depolymerase label captures the evidence ([PMID:27219064](https://pubmed.ncbi.nlm.nih.gov/27219064/); [PMID:27306797](https://pubmed.ncbi.nlm.nih.gov/27306797/)).

Human CPAP coiled-coil residues 897–1056 form a dimer. That result is distinct from dilute G-box monomers, zebrafish G-box/STIL crystals and a proposed higher-order molecular-ruler model ([PMID:24076405](https://pmc.ncbi.nlm.nih.gov/articles/PMC3824074/)). The public evidence index supplies a short original Results anchor with the exact construct and section.

## Assembly partners and process boundaries

CPAP is a substrate of PLK2/PLK4; phosphorylation modulates its assembly contribution rather than giving CPAP kinase activity ([PMID:20531387](https://pubmed.ncbi.nlm.nih.gov/20531387/): "PLK2 phosphorylates the S589 and S595 residues of CPAP"). Actual STIL interaction, endogenous complex and CPAP depletion/overexpression experiments support centriole replication and elongation. Cell-cycle synchronization in the STIL paper does not itself establish the CDK-activating G1/S signaling pathway ([PMID:22020124](https://pmc.ncbi.nlm.nih.gov/articles/PMC3243611/)). The 2007 Plk4 study supplies positive human localization/assembly Results; the independently read author thesis is separately identified rather than called the journal paper ([PMID:17681131](https://doi.org/10.1016/j.devcel.2007.07.002); [author thesis](https://edoc.ub.uni-muenchen.de/10088/1/Kleylein_Sohn_Julia.pdf)).

CEP135 and STIL binding is supported by defined assays, with human and zebrafish constructs distinguished ([PMID:23511974](https://pmc.ncbi.nlm.nih.gov/articles/PMC3630357/); [PMID:25385835](https://pubmed.ncbi.nlm.nih.gov/25385835/)). CPAP loss impairs CEP295 recruitment, but the source did not detect strong CPAP–CEP295 co-IP and suggested a CEP135-mediated route; the process annotation does not become a direct adaptor/binding assertion ([PMID:27185865](https://pubmed.ncbi.nlm.nih.gov/27185865/)).

The two spindle-regulation assertions citing PMID:17576815 remain unresolved. Its complete main text assays SIL/STIL in zebrafish and human cells, not CPAP. That is a source-specific mismatch; it does not disprove a CPAP spindle contribution. Aster nucleation and centriole construction alone do not resolve the precise regulatory relations ([original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC1952118/)).

## Binding and contextual activities

Positive partner-class refinements retain the original assays and all source fields. EPB41 is a cytoskeletal component; CEP135, CEP152, STIL and BCCIP are cytoskeletal regulators; YWHAG is a 14-3-3 protein; PLK2 and TNKS are enzymes. The GFI1B and CIC screen pairs narrow to RNA polymerase II DNA-binding transcription-factor binding. Those classifications do not assign partner catalytic/transcriptional activities to CPAP or establish native encounters from screens.

The source-specific distinctions matter: BioID reports proximity; OpenCell reports IP-MS associations; HuRI reports binary two-hybrid interactions; separate small-scale studies supply direct or co-complex evidence. All 41 selected interaction records retain their 42 literal fields, and 82 assayed participant ROGIDs match the official displayed sequences. Fragment and mutation fields still constrain interpretation. The original OpenCell YWHAG–CENPJ row groups several CPAP identifiers, including Q9HC77-2, and cannot resolve individual product activity. The LYST domain-specific binding row remains undecided because its actual target/domain mapping was not recovered ([PMID:11984006](https://pubmed.ncbi.nlm.nih.gov/11984006/)).

CPAP also increases STAT5-dependent reporter output in the tested human-cell system. This genuine coactivator result is retained as non-core, with the human CPAP/mouse STAT5 and reporter context explicit; upstream kinase activation and endogenous target genes remain unestablished ([PMID:12198240](https://doi.org/10.1210/me.2002-0108): "CPAP was found to augment Stat5-mediated transcription.").

## Products, phylogeny and electronic sources

The official products reconstruct exactly to 1338 and 1086 amino acids. Product 2 retains PN2-3 but replaces 1073–1086 and lacks 1087–1338, removing part of the STIL-interaction region. Sequence retention is not proof of equivalent centriole construction, gamma-complex association or STAT5 function. No product-specific GO assertion is manufactured from those sequence features.

The actual current PANTHER tree/MSA places the human target below PTN000817566 and the target sequence matches the official 1338-residue product. The current IBD GAF has five positive assertions there; a separate loss node is outside the target path. Display annotations with a NOT suffix were not used to invent a target loss. Human self-evidence in WITH/FROM is legitimate descendant support. Current donor records and historical node evidence are kept distinct.

All three current ARBA rules genuinely match the official CPAP FunFam: ARBA00088571 branch 8 also requires Mammalia, and ARBA00092134 branch 2/ARBA00088865 branch 4 require Metazoa. The broad organelle-assembly prediction is refined to the experimentally supported centriole process. Current rule matches do not reconstruct historical versions. The 23 Reactome cytosol rows have actual target paths through modeled physical entities; CPAP is not assigned the catalytic activity of every enclosing event.

## Access and inspectable evidence

The [manually assembled evidence index](CPAP-source-evidence.yaml) preserves all 82 original source objects, complete current GOA records, products, literal interaction/donor/rule evidence, typed Reactome paths, public source URLs and short excerpt locators. It distinguishes selected caches from separately recovered original main text and from independently read source consultations. Full-text flags on protected machine caches were not rewritten.

Important remaining limits are the complete journal Methods for 17681131, full target/domain evidence for 11984006, the exact 21399614 supplementary target table, complete 16713569/20852615 Methods, and complete 32296183/35271311 Methods in this reading. Attempted PDFs/spreadsheets or pages that returned HTML challenges are recorded as failures, not as usable scientific data. Positive original evidence or current curated records are retained where they independently establish the asserted scope; unavailable material is never treated as negative evidence.
