# DDC (Aromatic-L-amino-acid decarboxylase / AADC / DOPA decarboxylase) — review notes

UniProt: P20711 (DDC_HUMAN). HGNC:2719. EC 4.1.1.28. 480 aa, 53.9 kDa.

## Core identity and function

DDC encodes **aromatic-L-amino-acid decarboxylase (AADC)**, also called **DOPA decarboxylase (DDC)**.
It is a **pyridoxal 5'-phosphate (PLP)-dependent** homodimeric decarboxylase of the group II
(fold type I / PLP-dependent transferase) decarboxylase family.

- FUNCTION (UniProt): "Catalyzes the decarboxylation of L-3,4-dihydroxyphenylalanine (DOPA) to
  dopamine and L-5-hydroxytryptophan to serotonin." [file:human/DDC/DDC-uniprot.txt]
- CATALYTIC ACTIVITY 1: "L-dopa + H(+) = dopamine + CO2" (Rhea:RHEA:12272; EC=4.1.1.28) [file:human/DDC/DDC-uniprot.txt]
- CATALYTIC ACTIVITY 2: "5-hydroxy-L-tryptophan + H(+) = serotonin + CO2" (Rhea:RHEA:18533; EC=4.1.1.28) [file:human/DDC/DDC-uniprot.txt]
- COFACTOR: "Name=pyridoxal 5'-phosphate" (ECO:0000269|PubMed:22143761) [file:human/DDC/DDC-uniprot.txt]
- PATHWAY: "Catecholamine biosynthesis; dopamine biosynthesis; dopamine from L-tyrosine: step 2/2." [file:human/DDC/DDC-uniprot.txt]
- SUBUNIT: "Homodimer." (ECO:0000269|PubMed:22143761) [file:human/DDC/DDC-uniprot.txt]
- KW: Catecholamine biosynthesis; Decarboxylase; Lyase; Pyridoxal phosphate [file:human/DDC/DDC-uniprot.txt]
- MOD_RES 303: "N6-(pyridoxal phosphate)lysine" — the catalytic PLP-Schiff-base lysine (PubMed:22143761) [file:human/DDC/DDC-uniprot.txt]

DDC sits at the **branch point** of monoamine neurotransmitter synthesis: it is the second/last step
of the **catecholamine (dopamine)** branch (after tyrosine hydroxylase makes L-DOPA) and of the
**serotonin/indoleamine** branch (after tryptophan hydroxylase makes 5-HTP). It is thus shared between
the dopamine, noradrenaline, adrenaline (catecholamine) and serotonin/melatonin pathways.
Reactome places it in both "Catecholamine biosynthesis" (R-HSA-209905) and "Serotonin and melatonin
biosynthesis" (R-HSA-209931).

## Structure / catalytic mechanism

- Crystal structure (open conformation) at 2.8 A: PMID:22143761 (Giardina et al. 2011, PNAS),
  "Open conformation of human DOPA decarboxylase reveals the mechanism of PLP addition to Group II
  decarboxylases." Established PLP-binding sites (residues 148, 149, 246, 300 bind PLP; Lys303 forms
  the internal aldimine) and homodimer subunit. [file:human/DDC/DDC-uniprot.txt]
- Belongs to the group II decarboxylase family (SIMILARITY). [file:human/DDC/DDC-uniprot.txt]

## Disease

- DISEASE (UniProt): "Aromatic L-amino-acid decarboxylase deficiency (AADCD) [MIM:608643]: An inborn
  error in neurotransmitter metabolism that leads to combined serotonin and catecholamine deficiency."
  Autosomal recessive; developmental/psychomotor delay, ptosis, oculogyric crises, autonomic
  dysfunction. [file:human/DDC/DDC-uniprot.txt] Numerous AADCD missense variants documented (e.g.
  G102S, S147R, S250F, F309L, R347Q) mapping to catalytic/PLP region.

## Interactions / regulation (moonlighting and modulatory)

- **DJ-1 (PARK7, Q99497)** directly binds DDC and positively regulates its activity in human
  dopaminergic cells [PMID:19703902 "we found that DJ-1 directly bound to TH and DDC and positively
  regulated their activities in human dopaminergic cells"]. This paper (full text available) also
  measured DDC / L-DOPA decarboxylase activity directly (IDA) and dopamine synthesis, and describes a
  ternary complex of DJ-1, TH (tyrosine hydroxylase, P07101) and DDC [PMID:19703902 "A ternary complex
  among DJ-1, TH, and DDC was found"]. This grounds the enzyme-binding IPI to TH (P07101).
- **Androgen receptor (AR, P10275)**: DDC was identified as an AR-interacting protein that enhances AR
  transactivation in prostate cancer cells [PMID:12864730 "DDC (L-dopa decarboxylase) was detected
  multiple times as a novel AR-interacting protein... transient transfection of DDC in prostate cancer
  cells strongly enhanced ligand-dependent AR transcriptional activity"]. This is a proposed
  moonlighting / coactivator role, not the core enzymatic function; captured in UniProt INTERACTION
  (P20711; P10275: AR). Non-core.

## Localization

- Cytosolic / cytoplasmic enzyme (Reactome cytosol TAS; PAN-GO/IBA cytoplasm). [file:human/DDC/DDC-uniprot.txt DR GO lines]
- Detected in **urinary exosomes** by large-scale proteomics [PMID:19056867], HDA extracellular
  exosome — consistent with a soluble cytosolic protein being captured in secreted vesicles;
  non-core localization.

## Enzyme-assay / activity references

- PMID:16338639 (Duan et al. 2005): assay of hTH, hGCH1 and hAADC activities for ex vivo PD gene
  therapy; measured AADC activity directly (IDA GO:0004058 / GO:0036467). Abstract focuses on dopamine
  synthesis; serotonin/5-HTP not explicitly assayed in the abstract, but this is an experimental (IDA)
  annotation — retained, not removed. [PMID:16338639]
- PMID:7567987 (Rorsman et al. 1995): identifies AADC (EC 4.1.1.28) as a beta-cell autoantigen and
  restates its catalytic role: "Aromatic L-amino acid decarboxylase catalyzes the decarboxylation of
  L-5-hydroxytryptophan to serotonin and that of L-3,4-dihydroxyphenylalanine to dopamine." TAS support
  for GO:0004058. [PMID:7567987]

## Annotation-review summary (actions)

Core molecular functions:
- GO:0004058 aromatic-L-amino-acid decarboxylase activity (the general MF; IDA/TAS/IBA) — ACCEPT.
- GO:0036468 L-dopa decarboxylase activity (dopamine branch, IDA/ISS) — ACCEPT.
- GO:0036467 5-hydroxy-L-tryptophan decarboxylase activity (serotonin branch, IDA/ISS) — ACCEPT.
- GO:0030170 pyridoxal phosphate binding (cofactor; IEA but structurally verified) — ACCEPT.

Core biological processes:
- GO:0042416 dopamine biosynthetic process (IDA/ISS/IEA) — ACCEPT.
- GO:0042427 serotonin biosynthetic process (IBA) — ACCEPT.
- GO:0006584 catecholamine metabolic process (IBA) — ACCEPT (parent process; core).

Location: GO:0005737 cytoplasm (IBA), GO:0005829 cytosol (TAS) — ACCEPT.

Non-core / general / moonlighting (KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED):
- GO:0006520 amino acid metabolic process; GO:0016830 carbon-carbon lyase; GO:0016831 carboxy-lyase;
  GO:0042401 biogenic amine biosynthetic process — general parent terms (IEA), non-core.
- GO:0005515 protein binding (x2, IPI, AR and DJ-1) — MARK_AS_OVER_ANNOTATED (uninformative bare term;
  underlying interactions real).
- GO:0019899 enzyme binding (IPI, TH via DJ-1 ternary complex) — KEEP_AS_NON_CORE.
- GO:0070062 extracellular exosome (HDA) — KEEP_AS_NON_CORE.
</content>
</invoke>
