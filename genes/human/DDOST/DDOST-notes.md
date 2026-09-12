# DDOST (OST48) — gene review notes

## Identity
- UniProt: **P39656** (OST48_HUMAN); gene **DDOST** (HGNC:2728); synonyms KIAA0115, OST48.
- Full name: Dolichyl-diphosphooligosaccharide--protein glycosyltransferase 48 kDa subunit.
- 456 aa precursor; N-terminal signal (1..42), large lumenal domain (43..427), single TM helix (428..447), short cytoplasmic tail (448..456) → **single-pass type I membrane glycoprotein** of the ER.
  - [file:human/DDOST/DDOST-uniprot.txt "Single-pass type I membrane protein"]
- Belongs to the "DDOST 48 kDa subunit family" (SIMILARITY). Structural coverage: PDB 6S7O/6S7T (OST-A/OST-B cryo-EM), 8B6L, 8PN9, 9N9J, 9YGY.

## Core biology
DDOST/OST48 is a **non-catalytic subunit of the oligosaccharyltransferase (OST) complex**, the ER enzyme that carries out the central step of **N-linked protein glycosylation**: en-bloc transfer of the preassembled Glc3Man9GlcNAc2 glycan from dolichol-pyrophosphate onto Asn within an Asn-X-Ser/Thr sequon in nascent polypeptides.
- [file:human/DDOST/DDOST-uniprot.txt "Subunit of the oligosaccharyl transferase (OST) complex that"]
- [file:human/DDOST/DDOST-uniprot.txt "catalyzes the initial transfer of a defined glycan"]
- [file:human/DDOST/DDOST-uniprot.txt "consensus motif in nascent polypeptide chains, the first step in"]
- Reactome R-HSA-446209: "This reaction is catalyzed by the oligosaccharyltransferase (OST) complex, comprising at least seven proteins; DAD1 ..., DDOST (OST48 in yeast), RPN1 ..., RPN2 ..., OST4, TUSC3 (N33), MAGT1 ... and either STT3A or STT3B ..., which contain the catalytic domain".

The catalytic subunit is **STT3A** or **STT3B**; DDOST itself has no catalytic activity. It is one of the shared **core** subunits (RPN1, RPN2, OST48, OST4, DAD1, TMEM258) present in both complex forms.
- [file:human/DDOST/DDOST-uniprot.txt "OST48, OST4, DAD1 and TMEM258, either STT3A or STT3B as catalytic"]

Two complex forms exist:
- **OST-A** (STT3A-containing, GO:0160226) — cotranslational, associates with Sec61 translocon/ribosome.
- **OST-B** (STT3B-containing, GO:0160227) — posttranslocational.
- [PMID:31831667 "Mammals express two distinct OST complexes that act in a cotranslational (OST-A) or posttranslocational (OST-B) manner"]
- Cryo-EM confirmed DDOST as a component of both (structures OST-A and OST-B). [PMID:31831667]
- Gemmer et al. visualized the STT3A-OST bound to the ER translocon. [PMID:36697828 "Visualization of translation and protein biogenesis at the ER membrane"]
- Lampson et al. determined the STT3A-OST structure and used it to define an NGI-1 druggable pocket. [PMID:38670073]

## Functional requirement / assembly
Roboti & High (siRNA knockdown in mammalian cells) showed **OST48 (and DAD1) are required for assembly of both STT3A- and STT3B-containing OST complexes**; OST48 depletion destabilizes the complex and causes global hypoglycosylation.
- [PMID:22467853 "OST48 and DAD1 are required for the assembly of both STT3A- and STT3B-containing OST complexes"]
- [PMID:22467853 "OST48 and DAD1 are global modulators of OST stability and hence N-glycosylation"]
- UniProt summarizes: [file:human/DDOST/DDOST-uniprot.txt "the assembly of both SST3A- and SS3B-containing OST complexes"]
This IMP is best read as DDOST contributing to complex integrity / OST catalytic activity (i.e. contributes_to the OST glycotransferase activity), NOT as an autonomous "enzyme activator activity" MF. The `enzyme activator activity` (GO:0008047) and `regulation of protein stability` (GO:0031647) IMP annotations from the same paper are over-interpretations of a structural/assembly role.

## Original biochemical characterization
Kumar, Heinemann & Ozols purified human lymphocyte OST; N-terminal sequencing identified ribophorin I, ribophorin II, and "a 50-kDa homologue of Wbp1" (= OST48/DDOST). N-glycosylation activity rose ~10-fold on mitogen/IL-2 activation of T cells.
- [PMID:9642163 "N-glycosylation activity increased 10-fold after mitogen activation of PBLs"]
- [PMID:9642163 "a 50-kDa homologue of Wbp1, a yeast protein essential for N-glycosylation"]
GOA (assigned_by UniProt) derives four IDA annotations from this paper: OST complex membership (GO:0008250), protein N-linked glycosylation (GO:0006487), plus `response to cytokine` (GO:0034097), `T cell activation` (GO:0042110), and `intracellular membrane-bounded organelle` (GO:0043231). The cytokine/T-cell terms reflect the experimental *system* (IL-2-driven T-cell activation) rather than a DDOST-intrinsic function — DDOST does not itself drive T-cell activation; it is the OST enzyme whose *activity* was measured to increase. These are context/over-annotations → KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED.

## Localization
- ER membrane is the authoritative location (SUBCELLULAR LOCATION). [file:human/DDOST/DDOST-uniprot.txt "Endoplasmic reticulum membrane"]
- HPA IDA to endoplasmic reticulum (GO:0005783) — consistent.
- Reactome TAS "endoplasmic reticulum membrane" (multiple pathway-specific reactions) — consistent, redundant.
- `membrane` (GO:0016020) IEA/HDA — correct but non-informative parent.
- **Azurophil granule membrane (GO:0035577)** and **plasma membrane (GO:0005886)** (Reactome "Neutrophil degranulation" / azurophil-granule exocytosis, R-HSA-6798739) are large-scale granule-proteome inclusions, not the site of DDOST's molecular function. Over-annotations (neutrophil granule proteomics sweep OST subunits in); keep as non-core / over-annotated. Not experimental for DDOST specifically here (TAS from Reactome).

## Interactions (IPI "protein binding")
- **STING1 (Q86WV6)** — DDOST appears in the STING1 innate-immunity interactome (HI5). UniProt records `P39656; Q86WV6: STING1` in the INTERACTION block; GOA IPI GO:0005515 WITH UniProtKB:Q86WV6 from PMID:21903422 (Li et al., innate-immunity interactome; STING/UNC93B1 pull down many ER membrane/translocation proteins).
  - [file:human/DDOST/DDOST-uniprot.txt "P39656; Q86WV6: STING1; NbExp=2; IntAct=EBI-358866, EBI-2800345"]
  - [PMID:21903422 "STING and UNC93B1 interacted with 10 common binding partners and most of them are ER membrane proteins involved in protein translocation"]
- **SMIM22 / CASIMO1 (K7EJ46)** — GOA IPI GO:0005515 WITH UniProtKB:K7EJ46 from PMID:29765154; UniProt SUBUNIT "Interacts with SMIM22". The cached paper is about CASIMO1/SQLE and does not narrate a DDOST-functional consequence, so this binding is not a core function.
  - [file:human/DDOST/DDOST-uniprot.txt "SMIM22 (PubMed:29765154)"]
Both are bare "protein binding" IPIs → MARK_AS_OVER_ANNOTATED (per policy, never REMOVE a protein-binding IPI). They inform interactome context, not DDOST's molecular function.

## Disease
DDOST deficiency causes **Congenital disorder of glycosylation type 1R (CDG1R / DDOST-CDG)**, MIM 614507; variant Gly217Asp identified by whole-exome sequencing (Jones et al. 2012, PMID:22305527).
- [file:human/DDOST/DDOST-uniprot.txt "Congenital disorder of glycosylation 1R (CDG1R) [MIM:614507]"]

## Curation summary (actions)
- Core (ACCEPT / represent core): OST complex membership (GO:0008250 IDA/IBA/IPI/ISS), OST-A (GO:0160226) & OST-B (GO:0160227) IDA, protein N-linked glycosylation (GO:0006487 IDA/IMP/IBA), ER membrane location (GO:0005789), ER (GO:0005783 IDA).
- Redundant-but-correct IEA/TAS for own function → ACCEPT (e.g. GO:0005789 IEA/ISS/TAS, GO:0006487 IEA).
- Broad parents → KEEP_AS_NON_CORE (GO:0016020 membrane; GO:0043231 intracellular membrane-bounded organelle; GO:0009101 glycoprotein biosynthetic process ISS).
- Over-annotations (not DDOST's molecular role) → MARK_AS_OVER_ANNOTATED: GO:0008047 enzyme activator activity, GO:0031647 regulation of protein stability, GO:0034097 response to cytokine, GO:0042110 T cell activation, GO:0035577 azurophil granule membrane, GO:0005886 plasma membrane, GO:0005515 protein binding (STING1, SMIM22).

## Core function model (non-catalytic subunit)
- in_complex: GO:0008250 oligosaccharyltransferase complex (CC protein complex; def: "A protein complex that is found in the endoplasmic reticulum membrane of eukaryotes...").
- contributes_to_molecular_function: GO:0004579 dolichyl-diphosphooligosaccharide-protein glycotransferase activity (MF; the OST catalytic activity, carried by STT3A/B, to which DDOST contributes structurally).
- directly_involved_in / BP: GO:0006487 protein N-linked glycosylation.
- location: GO:0005789 endoplasmic reticulum membrane.
- NOTE: GO:0018279 ("protein N-linked glycosylation via asparagine") is **OBSOLETE** (merged into GO:0006487) — use GO:0006487.
</content>
</invoke>
