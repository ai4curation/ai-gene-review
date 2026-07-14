# GGT1 (human) — gene review notes

UniProt: **P19440** (GGT1_HUMAN). HGNC:4250. Gene symbol GGT1 (synonym GGT).
Recommended name in UniProt: "Glutathione hydrolase 1 proenzyme" (a precursor that is
autocatalytically processed into a heavy + light chain heterodimer).

## Identity and core biochemistry

GGT1 is **gamma-glutamyltransferase 1 / γ-glutamyl transpeptidase (GGT)**, CD antigen CD224.
It is a **cell-surface (type II single-pass membrane, extracellular-facing) ectoenzyme** of the
N-terminal-nucleophile (Ntn) hydrolase family. The 569-aa precursor undergoes **autocatalytic
cleavage** into a heavy chain and a light chain; the **N-terminal Thr of the light chain
(Thr-381) is the catalytic nucleophile** and the active site resides in the light chain.

- EC assignments in UniProt: **EC 3.4.19.13** (glutathione hydrolase), **EC 2.3.2.2**
  (γ-glutamyltransferase / transpeptidase), **EC 3.4.19.14** (leukotriene-C4 hydrolase).
  [file:human/GGT1/GGT1-uniprot.txt "EC=3.4.19.13", "EC=2.3.2.2", "EC=3.4.19.14"]
- Catalytic nucleophile Thr-381 identified by MS with a mechanism-based inhibitor
  [PMID:17924658 "the first unambiguous identification of Thr381 as the active site nucleophile of human gamma-glutamyltranspeptidase"].
- Heterodimer, active site in light chain
  [file:human/GGT1/GGT1-uniprot.txt "Heterodimer composed of the light and heavy chains. The active"; "site is located in the light chain."].
- Autocatalytic cleavage is essential for activation
  [file:human/GGT1/GGT1-uniprot.txt "the"; "autocatalytic cleavage is essential to the functional activation of the"; "enzyme."].

## Core molecular function

GGT1 catalyzes the **first, rate-limiting step of extracellular glutathione (GSH) catabolism /
the γ-glutamyl cycle**: it cleaves the **γ-glutamyl bond of extracellular glutathione**
(γ-Glu-Cys-Gly), releasing free **glutamate** and the dipeptide **cysteinylglycine** (later
hydrolyzed by dipeptidases to Cys + Gly). This salvages cysteine for intracellular GSH
resynthesis.

- FUNCTION [file:human/GGT1/GGT1-uniprot.txt "Cleaves the gamma-glutamyl bond of extracellular glutathione"].
- Reaction: glutathione + H2O = L-cysteinylglycine + L-glutamate (RHEA:28807, EC 3.4.19.13)
  [file:human/GGT1/GGT1-uniprot.txt "Reaction=glutathione + H2O = L-cysteinylglycine + L-glutamate;"].
- Cysteine/glutathione homeostasis
  [file:human/GGT1/GGT1-uniprot.txt "Contributes to cysteine homeostasis,"; "glutathione homeostasis and in the conversion of the leukotriene LTC4"].
- Km(GSH) 10.6 µM, physiologically relevant; GSH, GSSG, LTC4 all substrates with similar
  catalytic efficiency; hydrolysis predominates at physiologic pH; transpeptidation only at
  high acceptor concentrations
  [PMID:21447318 "The Km for hydrolysis with GSH as a substrate was 10.60 ± 0.07 μM"; "Under physiologic conditions, hydrolysis is the predominate reaction catalyzed by GGT1"].

The enzyme also acts as a **transpeptidase (EC 2.3.2.2)**, transferring the γ-glutamyl moiety
to an acceptor amino acid / dipeptide when these are present at high concentration
[file:human/GGT1/GGT1-uniprot.txt "can also"; "catalyze a transpeptidation reaction, transferring the gamma-glutamyl"; "moiety to an acceptor amino acid to form a new gamma-glutamyl compound"].
This is the classic "γ-glutamyl transpeptidase" activity that gives the enzyme its name and is
the basis of the standard clinical serum-GGT assay.

## Leukotriene / eicosanoid metabolism

GGT1 hydrolyzes **leukotriene C4 (LTC4) to LTD4** (EC 3.4.19.14), a step in the cysteinyl
leukotriene pathway (inflammatory lipid mediators).
- Reaction: leukotriene C4 + H2O = leukotriene D4 + L-glutamate (RHEA:31563)
  [file:human/GGT1/GGT1-uniprot.txt "Reaction=leukotriene C4 + H2O = leukotriene D4 + L-glutamate;"].
- Km(LTC4) 10.8 µM, comparable to GSH; human GGT1 is actually a MORE active
  γ-glutamyl leukotrienase than GGT5 in vitro
  [PMID:21447318 "The Km for LTC4 was 10.8 ± 0.1 μM"; "our data demonstrate that human GGT1 is more active as a gamma-glutamyl leukotrienase than human GGT5"].
- Human GGT-deficient patients show complete deficiency of LTD4 biosynthesis: urinary LTC4
  elevated, LTE4 undetectable, and monocytes fail to convert [3H]LTC4 → [3H]LTD4
  [PMID:14754911 "Our data demonstrate a complete deficiency of LTD4 biosynthesis in patients with a genetic deficiency of GGT"; "The formation of [(3)H]LTD(4) from [(3)H]LTC(4) in monocytes was completely deficient"].
  This is a human in-vivo IMP-grade demonstration of the LTC4→LTD4 (leukotriene-C4 hydrolase)
  activity and of the role in LTD4 biosynthesis.

GGT1 also cleaves other GSH S-conjugates including the maresin conjugate MCTR1
[(13R)-S-glutathionyl-...docosahexaenoate], part of specialized pro-resolving mediator
biosynthesis, and drug/xenobiotic mercapturate (GSH-conjugate) processing (aflatoxin-SG,
acetaminophen-SG, etc. — see Reactome).
- [file:human/GGT1/GGT1-uniprot.txt "glutathione conjugates (such as maresin conjugate"].
- [PMID:27791009 title "Maresin conjugates in tissue regeneration biosynthesis enzymes in human macrophages"] (UniProt-cited; not independently read here).

## Localization

- **Plasma membrane**, single-pass type II membrane protein, catalytic domain facing the
  extracellular space (an ectoenzyme); apical/brush-border in polarized epithelia.
  [file:human/GGT1/GGT1-uniprot.txt "SUBCELLULAR LOCATION: Cell membrane"; "Single-pass type II membrane protein"].
- Plasma-membrane localization demonstrated experimentally
  [PMID:23682772 "fail to localize to the plasma membrane" — re GGT2; hGGT1 by contrast localizes to plasma membrane and is the functional comparator].
- Detected in extracellular fluids / exosomes (colostrum, prostatic-secretion exosomes,
  B-cell exosomes) by proteomics — consistent with an ectoenzyme that can be shed/released;
  these are HDA proteomic detections, non-core.

## Disease and physiology

- **Glutathionuria (GLUTH, MIM:231950)**: rare autosomal-recessive GGT1 deficiency;
  glutathione in urine, mild-moderate intellectual disability, behavioral disturbance
  [file:human/GGT1/GGT1-uniprot.txt "Glutathionuria (GLUTH) [MIM:231950]"; "generalized gamma-glutamyl"; "transpeptidase deficiency"].
  Caused by a large homozygous intragenic GGT1 deletion in one family [PMID:29483667].
- Elevated **serum GGT** is a widely used clinical biomarker of hepatobiliary disease
  (background, not a GO function).
- Tissue: kidney and liver enhanced; also pancreas, stomach, intestine, placenta, lung
  [file:human/GGT1/GGT1-uniprot.txt "Detected in fetal and adult kidney and liver, adult"; "pancreas, stomach, intestine, placenta and lung."].

## Paralog caution (GGT2 / GGT5)

GGT2 (P36268) is 94% identical to GGT1 but does **not** autocleave and is **catalytically
inactive** — microarray "GGT2 induction" should not be read as functional GGT activity
[PMID:23682772 "hGGT2 does not encode a functional enzyme"; "do not autocleave into heterodimers, fail to localize to the plasma membrane, and do not metabolize γ-glutamyl substrates"].
The GOA IPI "protein binding" to GGT2P (P36268; PMID:33961781, BioPlex AP-MS) reflects the
near-identical sequence of the two paralogs and is uninformative about GGT1 function.

## Annotation review summary / rationale

Core, well-supported functions:
1. **Glutathione hydrolase activity (GO:0036374)** — MF, extensive IDA (PMID:21447318,
   PMID:20622017, PMID:24047895, PMID:23682772, PMID:17924658) + IBA + Reactome TAS. CORE.
2. **Transpeptidase / gamma-glutamyltransferase (EC 2.3.2.2) activity** — GGT1 also transfers
   the gamma-glutamyl moiety to acceptor amino acids/dipeptides. NOTE: the dedicated GO term
   **GO:0003840 "gamma-glutamyltransferase activity" is OBSOLETE** (consider → GO:0036374), so
   this transpeptidation activity is now represented by GO:0036374 rather than a separate MF.
   The existing IDA to **GO:0000048 peptidyltransferase activity** (a ribosomal translation
   term) is a mis-mapping of this transpeptidase activity → MODIFY to GO:0036374 (glutathione
   hydrolase activity), the current catalytic MF.
3. **Leukotriene-C(4) hydrolase activity (GO:0002951)** — MF, IDA (PMID:21447318) + human
   IMP (PMID:14754911). CORE (secondary MF).
4. **Glutathione catabolic process (GO:0006751)** — BP, IDA/IBA/IEA. CORE.
5. **Plasma membrane (GO:0005886)** — CC, EXP/IDA/IBA. CORE location.

Non-core / supporting:
- glutamate metabolic process, leukotriene metabolic process, leukotriene D4 biosynthetic
  process, fatty acid metabolic process, amino acid metabolic process — true downstream
  consequences of the catalytic activity; KEEP_AS_NON_CORE (or ACCEPT where the direct
  product is glutamate).
- zymogen activation / proteolysis — refer to the autocatalytic self-cleavage that activates
  GGT1 (not a general protease role). KEEP_AS_NON_CORE.
- extracellular exosome / extracellular region (HDA proteomics) — KEEP_AS_NON_CORE
  (shed ectoenzyme; not the primary functional compartment).

Over-annotations / to fix:
- **GO:0005515 protein binding** (2× IPI: PMID:33961781 vs GGT2P; PMID:15528406 vs Q12791
  KCNMA1) — bare, uninformative; MARK_AS_OVER_ANNOTATED (never REMOVE per policy).
  PMID:15528406 is a hemoxygenase-2/BK-channel paper; the GGT1↔KCNMA1 IPI is a spurious
  high-throughput interaction unsupported by that paper's biology.
- **GO:0000048 peptidyltransferase activity** IDA — wrong-branch term (ribosomal); MODIFY →
  GO:0003840 gamma-glutamyltransferase activity.
- ISS block transferred from mouse Ggt1 (UniProtKB:Q60928): regulation of immune system
  process, glutathione biosynthetic process, spermatogenesis, L-cysteine biosynthetic
  process, regulation of inflammatory response. GGT1 does NOT biosynthesize glutathione
  (it catabolizes it) — GO:0006750 glutathione biosynthetic process is misleading and is a
  candidate for MARK_AS_OVER_ANNOTATED. Cysteine "biosynthesis" (GO:0019344) is really
  cysteine salvage; KEEP_AS_NON_CORE with caveat. Immune/inflammatory regulation and
  spermatogenesis are indirect, mouse-derived, pleiotropic phenotypes → KEEP_AS_NON_CORE.
- IBA GO:0002682 regulation of immune system process, GO:0031179 peptide modification,
  GO:0050727 regulation of inflammatory response — high-level IBA process terms, indirect;
  KEEP_AS_NON_CORE (peptide modification is a weak descriptor of the transpeptidation).

Reactome R-HSA-5602984 / R-HSA-9035966 are "Defective GGT1 does NOT hydrolyse..." reactions
but are annotated (correctly) to the normal GO:0036374 MF that GGT1 enables — ACCEPT as
non-core TAS duplicates of the glutathione hydrolase MF.
