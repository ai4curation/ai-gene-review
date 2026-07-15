# PTPN11 / SHP2 review notes

## Scope and evidence policy

- Review target: human PTPN11 (UniProt Q06124), all 258 seeded GOA rows.
- The available deep-research providers were reported as globally quota-blocked, so no provider was retried and no provider-style file was created. This journal instead uses the reviewed UniProt record and locally cached primary literature.
- Experimental annotations were not rejected merely because a cached paper is abstract-only. Where the annotation is biologically coherent but represents a downstream or tissue-specific outcome, it is retained as `KEEP_AS_NON_CORE`; where a high-throughput localization lacks mechanistic support, it is left `UNDECIDED`.
- All 82 `protein binding` rows preserve the reported interactions but are marked `MARK_AS_OVER_ANNOTATED`, because GO:0005515 does not identify the biologically informative phosphotyrosine-, receptor-, or kinase-binding activity.

## Core molecular mechanism

PTPN11 encodes SHP2, a non-receptor protein tyrosine phosphatase with tandem N-terminal SH2 domains, a catalytic PTP domain, and a regulatory C-terminal tail. In the basal state, the N-SH2 domain occludes the phosphatase active site; phosphotyrosine-ligand binding relieves autoinhibition and recruits the enzyme to signaling complexes. [PMID:32184441 "At the basal state, the N-SH2 domain of SHP-2 binds the phosphatase domain in an auto-inhibitory closed conformation and directly blocks the active phosphatase site."] [PMID:32184441 "Interaction of the N-SH2 domain with phosphotyrosine peptide disrupts the interaction of N-SH2 with the phosphatase active site and activates the enzyme"]

The catalytic activity is experimentally established on physiological protein substrates. Sprouty proteins are direct SHP2/Corkscrew targets, providing a mechanism by which dephosphorylating an RTK feedback inhibitor promotes RTK output. [PMID:16481357 "a purified SHP-2 protein dephosphorylates the critical tyrosine of Sprouty 1."] [PMID:16481357 "These results identify Sprouty proteins as in vivo targets of Corkscrew/SHP-2 tyrosine phosphatases and show how Corkscrew/SHP-2 proteins can promote RTK signaling by inactivating a feedback inhibitor."] SHP2 also dephosphorylates parafibromin and thereby promotes Wnt signaling; disease-associated variants measurably alter this activity. [PMID:26742426 "SHP2 also promotes Wnt signaling by dephosphorylating parafibromin."]

SHP2 is therefore unusual among phosphatases in often acting positively on RAS-ERK output. Activating Noonan-syndrome substitutions increase SHP2 catalytic activity and MAPK signaling. [PMID:28074573 "Expression of the mutant proteins in HEK293T cells documented their activating role on MAPK signaling."] [PMID:28074573 "biochemical data indicated that substitutions at codons 262 and 265 increased the catalytic activity of the phosphatase"]

## Binding and adaptor activities

The tandem SH2 domains confer phosphotyrosine-dependent recruitment and enzyme activation. In the PD-1 system, SHP2 bridges two phosphorylated ITSM motifs and this interaction robustly activates its phosphatase activity. [PMID:32184441 "SHP-2 interaction with two ITSM-pY248 phosphopeptides induced robust enzymatic activation."] This supports phosphotyrosine-residue binding as a core activity while keeping PD-1/T-cell inhibition as one context-specific output.

SHP2 can also act as a molecular adaptor independently of a substrate-product relationship. It binds activated insulin receptor and promotes IRS1 recruitment and glucose uptake. [PMID:7493946 "While the receptor and the phosphatase do not serve as substrates for each other, their interaction promotes IRS-1 binding to the receptor, indicating that PTP1D functions as an adapter for insulin receptor and IRS-1."] In innate immunity, a Siglec1-DAP12 complex recruits SHP2 as a scaffold, which in turn recruits TRIM27 to promote TBK1 degradation. [PMID:26358190 "Siglec1 associates with DAP12 to recruit and activate the scaffolding function of SHP2; SHP2 then recruits E3 ubiquitin ligase TRIM27, which induces TBK1 degradation via K48-linked ubiquitination at Lys251 and Lys372."] These observations support a distinct molecular-adaptor core function while the insulin and antiviral outcomes remain non-core contexts.

## Developmental roles and the cerebellar module

PTPN11 is pleiotropic. Human germline variants cause Noonan syndrome and perturb the balance between inactive and active SHP2 conformations. [PMID:11704759 "missense mutations in PTPN11 (MIM 176876)-a gene encoding the nonreceptor protein tyrosine phosphatase SHP-2, which contains two Src homology 2 (SH2) domains-cause Noonan syndrome"] [PMID:11704759 "This implies that they are gain-of-function changes and that the pathogenesis of Noonan syndrome arises from excessive SHP-2 activity."] Broad brain, craniofacial, cardiac, ear, and genital-development GO annotations are retained as non-core phenotypic/developmental consequences rather than being promoted to SHP2's defining molecular function.

For cerebellar development, conditional mouse genetics gives a cell-type-resolved role. Pan-cerebellar Ptpn11 deletion blocks radial-glia-to-Bergmann-glia transformation, disrupts lamination, and eliminates foliation, whereas GCP-lineage deletion has no phenotype. [PMID:24431450 "Deleting Ptpn11 in the entire cerebellum by En1-cre blocks transformation of RG into BG but preserves other major cerebellar cell types."] [PMID:24431450 "In contrast, removing Ptpn11 in the GCP lineage by Atoh1-cre has no effect on cerebellar development, indicating that Shp2 is not cell autonomously required in GCP."] The study places SHP2 downstream of FGF8 and upstream of ERK in radial glia/nascent Bergmann glia, with active MEK1 rescue. [PMID:24431450 "Ptpn11 interacts with Fgf8 and is essential for ERK activation in RG and nascent BG."] [PMID:24431450 "expressing constitutively active MEK1 rescues BG formation and cerebellar foliation in Shp2-deficient cerebella."] This supports using PTPN11 as the FGF-ERK transducer for Bergmann-glia specification in a top-down cerebellar decomposition, not as a granule-cell-autonomous regulator.

## Curation synthesis

- Core: non-membrane-spanning protein tyrosine phosphatase activity, peptidyl-tyrosine dephosphorylation, phosphotyrosine-residue binding/recruitment, molecular-adaptor activity, cytosolic signaling, and positive regulation of ERK output.
- Non-core but supported contexts: ERBB/EGFR/FGFR/ephrin/insulin/cytokine signaling; immune checkpoint and innate-immune regulation; adhesion/focal-adhesion outputs; vascular mechanotransduction; and developmental phenotypes.
- Unresolved: nucleolar and mitochondrial localization annotations lack enough mechanistic context in the available evidence and remain `UNDECIDED`.
- Over-annotated: generic `protein binding`, generic `protein-containing complex`, and generic positive regulation of intracellular signal transduction do not convey a useful SHP2 activity.
