# SEPHS1 (human) — review notes

UniProt: P49903 (SPS1_HUMAN). HGNC:19685. Gene: SEPHS1 (synonyms SELD, SPS, SPS1).
392 aa. Chromosome 10.

## Naming / identity nuance

SEPHS1 is a **selenophosphate synthetase homolog** (AIRS / SelD / PurM-like fold;
selenophosphate synthase 1 family, Class II subfamily) and is the paralog of SEPHS2.
Despite the "selenophosphate synthetase 1" name, the current UniProt record (entry
version 204, 2026) has been substantially re-framed: the RecName is now
**"Zincore component SEPHS1"**, reflecting the 2025 discovery that SEPHS1 is a
subunit of the Zincore transcription-coregulator complex.

Key sequence distinction from SEPHS2: SPS1 has an **arginine** at the position
corresponding to the catalytic **selenocysteine** in SPS2
[PMID:20471958 "One of the major differences between SPS1 and SPS2 is that SPS1 has an arginine at the position corresponding to Sec in SPS2"].

## Catalytic activity — uncertain / likely not the in vivo core function

UniProt lists EC 2.7.9.3 (selenide, water dikinase; RHEA:18737) but the catalytic
evidence code is by-similarity (ECO:0000250|UniProtKB:P97364, mouse), NOT direct
experimental demonstration of catalysis for human SEPHS1. UniProt explicitly
qualifies the role:
[file:human/SEPHS1/SEPHS1-uniprot.txt "May also be involved in selenocysteine biosynthesis"]
... [file:human/SEPHS1/SEPHS1-uniprot.txt "Its role in selenocysteine biosynthesis is however"]
[file:human/SEPHS1/SEPHS1-uniprot.txt "unclear and several studies suggest that it does not act as a"]
[file:human/SEPHS1/SEPHS1-uniprot.txt "selenophosphate synthase in vivo or plays an non-essential role"].

Direct biochemical work supports the "not a bona fide selenophosphate synthase"
view: in vitro, SPS2 (not SPS1) synthesizes selenophosphate from selenide + ATP
[PMID:20471958 "In in vitro experiments, SPS2 synthesized SeP from selenide and ATP, but SPS1 did not have this activity"];
and knockdown of SPS1 (unlike SPS2) does not impair selenoprotein biosynthesis
[PMID:20471958 "the inhibition of SPS1 expression did not affect the biosynthesis of selenoprotein"].

Complementation of an E. coli selD mutant by human Sps1 was only weak and required
added L-selenocysteine, leading the authors to propose SPS1 works in a
**selenium/selenocysteine salvage (recycling)** system rather than de novo
selenite assimilation
[PMID:15534230 "the Sps1-encoded enzyme depends on a selenium salvage system that recycles l-selenocysteine, whereas the Sps2 enzyme can function with a selenite assimilation system"].
The original cloning paper (PMID:7665581) reported that human selD transfection
increased Se labeling of type-1 deiodinase and weakly complemented bacterial selD;
this is the basis of the historical IDA "L-selenocysteine biosynthetic process"
annotation, but note human selD "has only 32% homology with the bacterial protein"
and the functional readout was indirect (selenoprotein labeling).

**Conclusion for curation:** treat GO:0004756 (selenide, water dikinase activity)
and GO:0016260 (L-selenocysteine biosynthetic process) as uncertain / at most a
salvage-context, non-core role for the human protein. Keep experimental
annotations (per policy: do not REMOVE IDA/IMP); mark the catalytic MF as
non-core / over-annotated with a note; retain the NOT annotation.

## Newly established core function: Zincore transcription coregulator

2025 Science paper (PMID:40608935): SEPHS1 + QRICH1 form the **Zincore** complex, a
ZNF-specific transcription coregulator essential for embryonic development.
[PMID:40608935 "we identified Zincore, a protein complex consisting of QRICH1 and SEPHS1, as a ZNF-specific coregulator essential for embryonic development in mice and associated with developmental syndromes in humans"].
Mechanism: a **SEPHS1 arginine clamp** recognizes DNA-bound zinc-finger domains and
locks ZNFs onto their cognate DNA motif (CTTTAAR), stabilizing them and enhancing
transcription
[PMID:40608935 "Cryo-electron microscopy of a Zincore-ZFP91-DNA complex revealed a SEPHS1 arginine clamp to recognize the DNA-bound zinc finger domains"]
[PMID:40608935 "This mode of binding explains recognition of different ZNFs and stabilizes ZFP91 onto its cognate DNA motif"].

UniProt captures this as the primary FUNCTION:
[file:human/SEPHS1/SEPHS1-uniprot.txt "acts as a molecular 'grip' to stabilize transcription factors at DNA-"]
[file:human/SEPHS1/SEPHS1-uniprot.txt "finger transcription factors, such as ZFP91, ZNF652, ZNF526 and PRDM15,"]
[file:human/SEPHS1/SEPHS1-uniprot.txt "its arginine clamp, enhancing their DNA-binding stability"].
The arginine clamp is a defined DOMAIN (Arg330, Arg371) and disease variants at
R371 reduce DNA-binding and transcriptional activity of ZFP91 (VERBRAS2).

This is the best-supported (EXP, structure-based) molecular function and biological
process for human SEPHS1, and best mapped to:
- MF: GO:0003712 transcription coregulator activity
- BP: GO:0006355 regulation of DNA-templated transcription
Localization consistent with this role: Nucleus, Chromosome (PMID:40608935).

## Redox / oxidative-stress homeostasis, proliferation

[PMID:31607477 "hSEPHS1 is a regulator of selenium-mediated redox-signaling in human pluripotent stem cells and plays a role in their survival"];
SEPHS1 knockdown reduced reprogramming efficiency and altered ROS-pathway/apoptosis
gene sets [PMID:31607477 "Transcriptome analysis revealed altered expression of the gene set related to the ROS pathway and apoptosis in SEPHS1-knockdown cells"].
Drosophila SPS1 (patufet) loss is embryonic-lethal and raises ROS; SPS1 modulates
oxidative stress and cell growth
[PMID:20471958 "knockout of SPS1 caused an increase in reactive oxygen species (ROS)"]
[PMID:20471958 "SPS1 participates in the regulation of oxidative stress and cell growth"].
Supports GO:0045454 cell redox homeostasis (IMP, PMID:31607477) as a genuine
biological role.

## Localization and subunit structure

- Homodimer (crystal structures 3FD5/3FD6, PMID:19477186; PMID:20471958).
- Component of a Sec-biosynthesis-associated oligomer with SEPHS2, SEPSECS,
  TRNAU1AP (PMID:16508009; PMID:28414460, BRET/co-IP).
- Component of the Zincore heterotetramer (QRICH1 dimer + SEPHS1 dimer; PMID:40608935).
- Isoform 1 (major type) localized to plasma + nuclear membrane; ΔE2/ΔE8/+E9
  cytoplasmic [PMID:20471958 "MT was localized on both plasma and the nuclear membrane, but the other three types were localized in the cytoplasm homogeneously"].
- Cytoplasm IDA: PMID:28414460. Nucleus/Chromosome EXP: PMID:40608935.

## ATP / nucleotide binding

Well documented: crystal structures with ADP/Mg2+/phosphate (PMID:19477186);
ATP-binding mutagenesis of the P-loop-like region (G273, H274) abolishes/reduces
ATP binding [PMID:7665581 "reduced selenium labeling was due to altered ATP binding properties of the mutant selenophosphate synthetases"].
GO:0005524 ATP binding is solid. The old TAS GO:0005525 "GTP binding" derives from
the 1995 paper describing a "consensus ATP/GTP binding domain"; GTP binding per se
was not demonstrated — treat as over-annotation, not core.

## Disease

Ververi-Brady syndrome 2 (VERBRAS2, MIM:621325): autosomal dominant
neurodevelopmental disorder; de novo missense variants in exon 9 (R371Q/W/G, W352G)
[PMID:38531365; PMID:40608935]. Pathogenic R371 variants map to the arginine clamp
and reduce ZFP91 DNA-binding/transcriptional activity, tying disease to the Zincore
coregulator function.

## Interactome (source of the protein-binding IPI annotations)

IntAct binary-interaction / large-scale interactome papers underlie the
GO:0005515 protein binding and GO:0042802 identical protein binding IPI
annotations:
- PMID:16189514 (self / identical protein binding, homodimer)
- PMID:21516116, PMID:25416956, PMID:32296183, PMID:33961781 (HuRI / interactome maps;
  partners incl. ZBTB25/P24278, QRICH1/Q2TAL8, ZNF202/O95125, XAF1/Q6GPH4,
  ZNF474/Q6S9Z5, ZNF276/Q8N554, ZNF526/Q8TF50, PLAGL2/Q9UPG8, SEPHS2/Q99611).
Notably many partners are zinc-finger proteins/QRICH1, consistent with the Zincore
coregulator function. Per policy, IPI "protein binding" is uninformative and marked
over-annotated (not removed); the QRICH1 and ZNF interactions are biologically the
most meaningful.

## Core function summary (for core_functions)

1. Transcription coregulator activity (GO:0003712) — Zincore/arginine-clamp
   stabilization of DNA-bound zinc-finger TFs. Core MF (EXP/structure).
2. Regulation of DNA-templated transcription (GO:0006355) — Zincore biological role.
3. Cell redox homeostasis (GO:0045454) — IMP; selenium-mediated redox signaling,
   proliferation/survival.
4. ATP binding (GO:0005524) — structurally established nucleotide binding.
5. (Uncertain / non-core) selenide, water dikinase activity (GO:0004756) — ancestral
   family activity; human SEPHS1 likely does not perform de novo SeP synthesis in
   vivo; at most Se/Sec salvage. Kept non-core / flagged over-annotated.

Locations: cytoplasm (GO:0005737), nucleus (GO:0005634).
