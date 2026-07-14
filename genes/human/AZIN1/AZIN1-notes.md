# AZIN1 (Antizyme inhibitor 1) — review notes

UniProt: O14977 (AZIN1_HUMAN). Gene: AZIN1; synonyms OAZI, OAZIN. Human (NCBITaxon:9606).
448 aa. HGNC:16432. Chromosome 8.

## Core biology

AZIN1 is **antizyme inhibitor 1**, a positive regulator of polyamine biosynthesis. It is a
**catalytically inactive paralog of ornithine decarboxylase (ODC1)**: it retains the ODC
(Orn/Lys/Arg decarboxylase class-II) fold but has lost ornithine decarboxylase catalytic
activity and does NOT decarboxylate ornithine.

UniProt FUNCTION [file:human/AZIN1/AZIN1-uniprot.txt]:
"Antizyme inhibitor (AZI) protein that positively regulates ornithine decarboxylase (ODC)
activity and polyamine uptake. AZI is an enzymatically inactive ODC homolog that counteracts
the negative effect of ODC antizymes (AZs) OAZ1, OAZ2 and OAZ3 on ODC activity by competing
with ODC for antizyme-binding (PubMed:17900240, PubMed:26305948). Inhibits antizyme-dependent
ODC degradation and releases ODC monomers from their inactive complex with antizymes, leading
to formation of the catalytically active ODC homodimer and restoring polyamine production
(PubMed:17900240)."

Mechanism: antizymes (OAZ1/2/3) bind ODC1 monomers, block ODC homodimerization, and target ODC
for ubiquitin-independent proteasomal degradation, thereby down-regulating polyamine synthesis.
AZIN1 **binds antizyme with higher affinity than ODC does**, sequestering the antizyme and so
**releasing/stabilizing active ODC1** and **restoring polyamine production**. Thus AZIN1's
molecular role is best modeled as **ornithine decarboxylase activator activity (GO:0042978:
"Binds to and increases ornithine decarboxylase activity")** — it activates ODC indirectly, via
antizyme sequestration, not by any catalytic activity of its own.

Note: there is NO dedicated "antizyme binding" GO term. (The id GO:0034452 is "dynactin binding",
not antizyme binding — do not use it.) GO:0042978 is the correct specific MF term and is exactly
what captures the antizyme-sequestration → ODC-activation mechanism.

## Do NOT assign ornithine decarboxylase activity to AZIN1

The defining feature of AZIN1 is that it is **catalytically dead**. Any ornithine decarboxylase
activity (GO:0004586) annotation is an over-annotation propagated from the ODC fold (IBA/IEA from
the decarboxylase family). Likewise "catalytic activity" (GO:0003824), "polyamine biosynthetic
process" (GO:0006596 via InterPro), and "putrescine biosynthetic process from arginine, via
ornithine" (GO:0009446) are decarboxylase-family fold propagations that AZIN1 does not perform
directly. AZIN1 promotes polyamine synthesis only indirectly by protecting active ODC1.

- SubCell family note [file:human/AZIN1/AZIN1-uniprot.txt]:
  "Belongs to the Orn/Lys/Arg decarboxylase class-II family. ODC antizyme inhibitor subfamily."
- InterPro IEA sources for the over-annotations: IPR000183/IPR009006/IPR022644 (catalytic activity),
  IPR002433 (polyamine biosynthetic process), IPR031178 = "Azin1"-specific signature (ODC activator
  activity — this one is appropriate).

## Localization

- Cytoplasm — IBA (GO:0005737), consistent with polyamine metabolism machinery.
- Nucleus — ISS/IEA from mouse ortholog O35484 (GO:0005634). UniProt SUBCELLULAR LOCATION:
  "Nucleus {ECO:0000250|UniProtKB:O35484}" [file:human/AZIN1/AZIN1-uniprot.txt]. By similarity only.
- Centrosomal reports exist in the literature/DR (CD-CODE Centrosome) but are not GOA-annotated here.
- UniProt SUBUNIT: "Monomer" [file:human/AZIN1/AZIN1-uniprot.txt].

## Structure / interaction

- PDB 4ZGZ: X-ray (5.81 Å) of AZIN1 (2-437) in complex with OAZ1 — structural basis of
  antizyme-mediated regulation of polyamine homeostasis [PMID:26305948; UniProt DR].
- UniProt INTERACTION [file:human/AZIN1/AZIN1-uniprot.txt]: OAZ3 (Q9UMX2, NbExp=7) and BMAL1
  (O00327-8, NbExp=3). The OAZ3 interaction is the functionally meaningful antizyme-binding
  interaction; BMAL1 is a high-throughput two-hybrid hit of unclear physiological significance.

## Provenance for existing-annotation review

- PMID:17900240 (Kanerva et al. 2008, Biochem J): abstract-only in cache
  (full_text_available: false). Abstract states the assayed protein is **ODCp = AZIN2**
  ("Here, we report that human ODCp is a novel AZI (AZIN2)"), demonstrating AZ1-3 binding, ODC
  activity/degradation rescue, and lack of ADC activity. GOA attributes IDA annotations
  (GO:0042978 ODC activator activity; GO:0042177 negative regulation of protein catabolic process)
  to AZIN1 from this reference. The function is biologically correct for AZIN1 (AZIN1 is the
  canonical antizyme inhibitor), but the primary experimental subject in the cached abstract is
  the paralog AZIN2. Per policy I do not REMOVE an experimental annotation on the basis of an
  abstract that foregrounds a paralog; the function is sound, so ACCEPT with a note. UniProt also
  cites PubMed:17900240 for AZIN1's FUNCTION and PTM(ubiquitination), so AZIN1 data are plausibly
  in the full text.
- PMID:18508777 (López-Contreras et al. 2008, J Biol Chem): abstract-only
  (full_text_available: false). Explicitly about **AZIN2/ODCp** stimulating polyamine uptake
  ("Transfection of COS7 cells with mouse or human AZIN2 ... markedly stimulated polyamine
  uptake"). GOA attributes GO:1902269 (positive regulation of polyamine transmembrane transport)
  IDA to AZIN1 from this reference. This is an AZIN2 phenotype; AZIN1's own effect on polyamine
  uptake is far less established. Keep as non-core / flag the citation as pointing to the paralog.
- Interactome IPI "protein binding" (GO:0005515), all IntAct, bare (no specific partner term):
  - PMID:25416956 (Rolland et al., interactome map) — with OAZ3 (Q9UMX2)
  - PMID:28514442 (Huttlin et al., BioPlex communities) — with OAZ3 (Q9UMX2)
  - PMID:31515488 (Fragoza et al., variant interactome) — with OAZ3 (Q9UMX2)
  - PMID:32296183 (Luck et al., HuRI) — with BMAL1 (O00327-8) and OAZ3 (Q9UMX2-2)
  - PMID:33961781 (Huttlin et al., BioPlex 3.0) — with OAZ3 (Q9UMX2)
  All are large-scale two-hybrid/AP-MS datasets; AZIN1 is not discussed by name in the text
  (interactions are in supplementary data). Bare "protein binding" is uninformative; per policy
  mark as over-annotated rather than remove. The recurrent OAZ3 hits corroborate AZIN1's
  antizyme-binding function (better captured by GO:0042978).

## GOA annotation inventory (20 rows)

MF: GO:0004586 ornithine decarboxylase activity (IBA) — OVER-ANNOTATION (catalytically dead);
    GO:0003824 catalytic activity (IEA InterPro) — OVER-ANNOTATION;
    GO:0042978 ornithine decarboxylase activator activity (IDA PMID:17900240; IBA; IEA InterPro) — CORE MF;
    GO:0005515 protein binding ×5 (IPI) — over-annotated bare binding.
BP: GO:0009446 putrescine biosynthetic process (IBA) — over-annotation (decarboxylase fold);
    GO:0006596 polyamine biosynthetic process (IEA InterPro) — over-annotation (indirect only);
    GO:0042177 negative regulation of protein catabolic process (IDA PMID:17900240; IBA) — CORE BP
      (blocks antizyme-dependent ODC degradation);
    GO:1902269 positive regulation of polyamine transmembrane transport (IDA PMID:18508777; IEA; IEA) — AZIN2 phenotype, non-core.
CC: GO:0005737 cytoplasm (IBA) — accept; GO:0005634 nucleus (ISS ×2, IEA) — accept by similarity.

## Proposed core functions

1. MF GO:0042978 ornithine decarboxylase activator activity — binds ODC antizymes (OAZ1/2/3),
   sequestering them, releasing/stabilizing catalytically active ODC1; the defining molecular role.
2. BP GO:0042177 negative regulation of protein catabolic process — inhibits antizyme-dependent
   (proteasomal) degradation of ODC1.
3. BP GO:0010967 regulation of polyamine biosynthetic process (positive) — net effect of
   antizyme sequestration is up-regulation of ODC-mediated polyamine synthesis; also
   GO:0010509 intracellular polyamine homeostasis as the higher-level role.
Location: cytoplasm (GO:0005737); nucleus by similarity (GO:0005634).
