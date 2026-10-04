# CBL (P22681) review notes

## 2026-10-01 — initial review (context: FGFR signaling module)

### Core biology
- RING E3 that recognises pTyr substrates via its TKB (SH2-like) domain and activates E2 via RING
  [PMID:10514377 "The c-Cbl protein acted as an E3 that can recognize tyrosine-phosphorylated substrates, such as the activated platelet-derived growth factor receptor, through its SH2 domain and that recruits and allosterically activates an E2 ubiquitin-conjugating enzyme through its RING domain."]
- Autoinhibited; linker Tyr371 phosphorylation activates
  [PMID:22266821 "Cbl ubiquitination activity is stimulated by phosphorylation of a linker helix region (LHR) tyrosine residue."]
- TKB pTyr recognition structures (SPRY2, SPRY4, EGFR, SYK, MET)
  [PMID:18273061 "An obligatory, intrapeptidyl H-bond between the phosphotyrosine and the conserved asparagine or adjacent arginine is essential for binding and orients the peptide into a positively charged pocket on c-Cbl."]
- EGFR: ligase activity drives coated-pit entry [PMID:15465819 "Both the ubiquitin ligase activity of c-Cbl and the UIM of Eps15 were necessary for plasma membrane recruitment of Eps15 and entry of ligand-bound EGFR into coated pits and vesicles containing Eps15."]; RASopathy mutants impair it [PMID:25178484 "the p.K382E, p.D390Y, and p.R420Q lesions impaired CBL-mediated EGFR ubiquitylation and degradation"]
- Proline-rich region binds SH3 adaptors [PMID:15090612 "CIN85 src homology 3 domains specifically bind to a proline-arginine (PxxxPR) motif in Cbl"]
- T cells / LAG3 [PMID:40101708 "LAG3 ubiquitination, mediated redundantly by the E3 ligases c-Cbl and Cbl-b, disrupted the membrane binding of the juxtamembrane basic residue-rich sequence"]

### FGFR / FRS2 evidence (for modules/fgfr_signaling.yaml)
- Newly fetched, PubMed-verified via esearch/esummary: PMID:11997436, PMID:18374639, PMID:21596750.
- FRS2alpha-GRB2-CBL ternary complex; CBL ubiquitinates FGFR and FRS2alpha
  [PMID:11997436 "Grb2 bound to tyrosine-phosphorylated FRS2 alpha forms a ternary complex with Cbl by means of its Src homology 3 domains resulting in the ubiquitination of fibroblast growth factor (FGF) receptor and FRS2 alpha in response to FGF stimulation."]
  Caveat: [PMID:11997436 "the partial inhibition of FGF receptor down-regulation in FRS2 alpha-/- cells indicates that the attenuation of signaling by FGF receptor is regulated by redundant or multiple mechanisms."]
- FGFR2-CBL in rafts (osteoblasts) [PMID:18374639 "FGFR2 and Cbl interact in raft micro-domains at the plasma membrane."]; there CBL ubiquitinates PI3K rather than (only) the receptor.
- TKB-dead G306E reduces FGFR2/PDGFRA ubiquitination in hMSCs [PMID:21596750 "decreased Cbl-mediated PDGFRα and FGFR2 ubiquitination"].
- FGFR3: TD-I mutant ubiquitylation appeared c-Cbl independent [PMID:17509076 "ubiquitylation was markedly increased but apparently independent of the E3 ubiquitin-ligase casitas B-lineage lymphoma (c-Cbl)"].
- Proposed NEW GO:0040037 negative regulation of FGFR signaling pathway (IDA, PMID:11997436).
  Participation: CBL catalyses the ubiquitination. Comparator: CBL already carries GO:0042059 for EGFR;
  SPRY1/2 and SULF1 carry GO:0040037 (QuickGO, human/mouse).

### Decisions worth flagging
- No NOT annotations in GOA for CBL.
- 122 'protein binding' IPI rows: MODIFY to specific binding terms where the paper defines the binding mode
  (SH3, SH2, pTyr, RTK, PTK, PI3K p85, 14-3-3, E2); REMOVE for high-throughput screens and uninformative cases.
- PMID:5668240 (IPI with INPPL1) is a 1968 peracetic acid paper: wrong identifier.
- GO:0043066 IMP (PMID:18070883): REMOVE — full text shows SPRY2 sequesters CBL to preserve survival; CBL acts in the
  pro-apoptotic direction [PMID:18070883 "endogenous hSPRY2-mediated regulation of apoptosis requires c-Cbl and is manifested by the ability of hSPRY2 to sequester c-Cbl and thereby augment signaling via growth factor receptors."]
- GO:0051897 IMP (PMID:17003487): MODIFY to negative regulation (GO:0051898) [PMID:17003487 "Twist haploinsufficiency results in decreased Cbl-mediated PI3K degradation in osteoblasts, causing PI3K accumulation and activation of PI3K/Akt-dependent osteoblast growth."]
- GO:0045742 positive regulation of EGFR signaling (Reactome PTK6 pathway): REMOVE, inverts CBL's role.
- Rat Compara 'response to X' IEAs: REMOVE (expression-type annotations; no mechanism).
- GO:0050821 protein stabilization (IDA PMID:40101708 + ARBA IEA): UNDECIDED; abstract says ubiquitination does not cause degradation.


## 2026-10-04 — whole-gene reassessment

This entry supersedes the biological judgments in the earlier journal entry where they conflict. The original entry is retained verbatim as historical provenance. The current review retains all 305 machine assertions and the single pre-existing author proposal for negative regulation of FGFR signaling. It does not create another annotation or reinterpret that historical proposal as a new machine assertion. The frozen project association remains autosomal dominant CBL-related disorder, classified Definitive in the frozen inventory; no disease-validity status is changed here.

### E3 chemistry and two distinct recognition functions

CBL is a RING ubiquitin E3 ligase. It recruits an E2 and promotes ubiquitin transfer rather than acting as an E2 or forming the catalytic thioester intermediate characteristic of HECT E3s. The primary biochemical source establishes E2-dependent ligase activity (PMID:10514377). Human CBL structures and biochemical controls in PMID:22266821 distinguish an autoinhibited arrangement from Tyr371-phosphorylated CBL, including changes in E2 affinity and positioning. Selected original structural Results and Methods were read; those assays use purified fragments and peptides, not a complete native receptor signaling assembly.

The TKB module recognizes selected phosphotyrosine motifs. PMID:18273061 supplies positive peptide structures and binding comparisons for several partners, but its wild-type FLT1 peptide does not bind under the tested conditions; engineered substitutions restore binding. The FLT1 source row therefore remains uncertain rather than being forced into the positive group. The APS distinction also matters: Figure 5A directly measures APS phosphopeptide binding by calorimetry, including a pH-dependent comparison, while Figure 4G uses full-length CBL, rat myc-tagged APS and IR-B in a mutational binding assay. The independent CBL–APS phosphopeptide crystal structure and additional calorimetry are from PMID:15737992. The source row's partner identifier remains unchanged.

CBL's proline-rich sequences engage SH3 domains on partners such as CIN85, intersectin, SRC and ABI1. These are supported domain-binding refinements, not claims that CBL possesses those SH3 domains. Conversely, CRK/CRKL or PI3K p85 can recognize phosphorylated CBL through their own SH2 domains. That direction does not give CBL phosphotyrosine-reader activity on the CRK/p85 edge. The same distinction applies to 14-3-3 proteins recognizing serine-phosphorylated CBL. The three core functions summarize E3 chemistry, TKB phosphotyrosine recognition and binding to partner SH3 domains; they do not duplicate every downstream signaling outcome. Key sources include PMID:15090612, PMID:16914641, PMID:17094785, PMID:8524328, PMID:8626543, PMID:9160881 and PMID:9092538.

### Receptor trafficking, signaling direction and disease context

CBL ubiquitination supports receptor sorting and attenuation, with substrate- and cell-dependent alternatives. PMID:15465819 distinguishes routes by which CBL directs activated EGFR into Eps15-containing pits. Its experiments do not make every CBL-associated protein a ubiquitination substrate. Human CBL disease-associated substitutions tested in COS-7 cells impair EGFR ubiquitination, internalization and degradation and increase ERK signaling (PMID:25178484). This is construct evidence for the tested variants, not proof that every clinical CBL allele has the same quantitative effect. The Noonan-like/JMML context is also recorded in reviewed UniProt; the frozen clinical association is preserved separately from individual assay conclusions.

For FGFR, PMID:11997436 supports recruitment through FRS2alpha–GRB2 and receptor/adaptor ubiquitination, while PMID:21596750 provides human mesenchymal-cell perturbation evidence involving FGFR2 and PDGFRA. The FGFR3 disease-mutant study PMID:17509076 reports a context in which receptor ubiquitination appears CBL independent. That result limits universal substrate claims; it does not contradict CBL's established E3 activity. The genuine historical FGFR-downregulation proposal remains. The earlier SPRY/SULF comparison was not a same-role E3 comparison and is not used to manufacture further process coverage. The two exact target-containing cached GO-CAMs inspected here concern LAG3, not FGFR; they do not establish absence from every external model.

The source-specific PI3K direction is corrected in the human Saethre–Chotzen osteoblast study. CBL re-expression reverses elevated PI3K/Akt signaling, supporting negative regulation for that assertion (PMID:17003487). This does not exclude PI3K recruitment or activation in different CBL complexes. The Reactome PTK6 pathway's specific positive-EGFR assertion remains uncertain because its CBL-specific causal role was not resolved; CBL's usual inhibitory role alone is insufficient to reject a curated pathway context.

### LAG3 and the unresolved stabilization term

PMID:40101708 distinguishes nondegradative ubiquitination from receptor clearance. The available canonical cache is abstract-only. Selected primary Results, figure captions and Methods were read in the [author-paper reproduction](https://www.researchgate.net/publication/389910533_Ligand-induced_ubiquitination_unleashes_LAG3_immune_checkpoint_function_by_hindering_membrane_sequestration_of_signaling_motifs). Human Jurkat double-knockout/reconstitution and primary T-cell experiments support redundancy between CBL and CBLB. Single-gene loss does not recapitulate all double-loss effects. K63-specific antibody and ubiquitin-mutant controls support K63 chains; the abstract's broader non-K48 wording alone would not establish that linkage. The cell-derived substrate ubiquitination experiment is not represented as an entirely purified binary CBL–LAG3 assay. K11 and possible quality-control K48 observations are not generalized into new CBL chain-specific functions.

The study found no increased LAG3 half-life, but the current GO:0050821 definition includes structural integrity as well as protection from degradation or aggregation. The paper proposes a membrane-dissociated signaling-tail conformation. The two inspected cached LAG3 GO-CAMs explicitly model CBL-dependent ubiquitination within protein stabilization and T-cell signaling. Those positive curator models are a material counterweight to a simple half-life-based rejection. Whether the conformational mechanism meets the term's structural-integrity meaning remains unresolved; both stabilization rows remain UNDECIDED rather than being removed.

### What the rat and mouse donor experiments actually establish

The new normal cache of PMID:16301331 contains XML text. Its complete relevant Results, Discussion and Methods were read; figure captions were read as text, without independently inspecting all image pixels or supplements. The rat experiments manipulate androgen availability with flutamide, hypophysectomy and testosterone replacement, and use Sertoli/germ-cell cultures. The mouse Cbl knockout adds a functional androgen-withdrawal/apoptosis phenotype. This supports a bounded non-core testosterone response; it is more than an expression observation. It does not show direct CBL binding to androgen or prove that Bim/Smac are direct CBL ubiquitination substrates. The paper's failed direct substrate tests and the imbalance between pro- and anti-apoptotic factors remain relevant limits.

The same study reports disorganized adult seminiferous architecture, germ-cell abnormalities and male hypofertility. The old assertion that the mice were simply fertile or lacked gonadal evidence is not retained. The exact male-gonad-development term concerns development of the mature structure, however, and the distinction between developmental establishment and adult maintenance is not settled by these results. The proposed early postnatal apoptosis explanation was not the demonstrated endpoint. That source row remains UNDECIDED with a concrete developmental-stage question.

The irradiation experiment has a different purpose. Local irradiation progressively removes testicular cell populations, allowing the authors to localize the source of CBL transcript/protein expression. The observed abundance changes do not demonstrate CBL executing a gamma-radiation response. The corresponding electronic transfer is marked over-annotated on this inspected experimental scope, not because IEP evidence is intrinsically invalid or because CBL could never respond to radiation.

The second new XML cache, PMID:19546888, contains actual perturbation evidence. In rat neuronal systems, CBL/CBLB knockdown sensitizes cells to NGF deprivation and DNA damage; loss of protein abundance is not the only observation. Human HEK293 experiments and construct controls also place c-Cbl upstream of MLK-to-MKK/JNK signaling. WT and RING-defective c-Cbl can protect against MLK-driven death in the tested context, and c-Cbl does not simply degrade MLK3 there. CBLB does not reproduce every c-Cbl overexpression phenotype. Endogenous POSH co-immunoprecipitation was unsuccessful, whereas other association assays were positive; a purified universal binary interaction is not asserted. The DNA-damage, NGF and negative-apoptosis transfers are retained as bounded non-core biology.

That protective setting does not erase the opposite causal direction in PMID:18070883. In the inspected human SW13 experiments, SPRY2 sequestration of CBL preserves growth-factor receptor signaling and survival; dominant-negative CBL rescues the receptor/survival effect of SPRY2 depletion. The specific negative-apoptosis annotation is over-annotated for that source. This is not a claim that CBL cannot suppress apoptosis elsewhere, as PMID:19546888 shows. Unread hypoxia, starvation, ethanol and other donor-specific mechanisms are left uncertain rather than being rejected using an expression-code shortcut.

### Binding, location and access boundaries

All 122 generic binding rows were reviewed individually. Supported generic associations are kept as non-core under the project's explicit standing instruction; 41 are refined where evidence establishes the relevant binding activity, and two remain uncertain. The second uncertainty is the INPPL1 row carrying PMID:5668240: the actual cached publication concerns peracetic acid, but the intended citation has not been verified. No replacement PMID is invented. Exact partner identifiers, including xenolog and tested-product identifiers, remain unchanged. Curated UniProt edges can corroborate a qualitative association; they do not convert an unread original high-throughput target table into a verified primary assay or a direct binary interface.

PMID:21706016 is an affinity-purification/selected-reaction-monitoring study of GRB2 complexes in HEK293T cells. AP-SRM is a method name, not evidence of APS-driven recruitment. Its source-specific CBL table remains uninspected; independent CBL–GRB2 evidence supports retaining that qualitative edge. The corrected final rationale distinguishes those facts.

CBL is retained in cytosol and at the cytoplasmic side of plasma-membrane signaling complexes. Reactome source rows retain the original curated locations with independent CBL trafficking support; an event named for another enzyme does not confer that enzyme's activity on CBL. The complete 78 unique cached Reactome summaries were read, but the entire physical-entity hierarchy was not re-fetched. Golgi/ciliary observations in PMID:29237719 include human CBL constructs in mouse cells and endogenous mouse contexts; they are kept as contextual locations without pretending every image is endogenous human protein. Flotillin-complex membership and the exact CBL target in the E-cadherin proteomics source remain unresolved.

Every reference receives a manual assessment. All 80 canonical publication headers and complete available abstracts were read. A true full-text flag does not guarantee complete extraction: PMID:18070883 contains abstract/Discussion but lacks cached Results/Methods; PMID:18273061 likewise lacks the cached original Results/Methods used in the finer structural assessment; the richer external readings are identified separately. PMID:25468996 does not expose the decisive target table in its available cache. Original screen-table uncertainty remains explicitly UNVERIFIED where appropriate, even if an association is independently retained.

The PMID:11997436 correction changes an author's name, and PMID:17509076 has an authorship correction; neither was treated as an experimental retraction. The corrected Figures 2/3 associated with PMID:14661060 were not independently inspected, so their unresolved detail does not support a confident new interface claim. The historical Falcon report is preserved as orientation, not substituted for primary evidence. Newly authored short anchors in the YAML were verified against exact canonical bytes, with at most 25 aggregate words per publication; this appendix adds no repeated quotation. Earlier journal quotations remain untouched historical text.
