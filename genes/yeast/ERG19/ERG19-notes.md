# ERG19 / MVD1 (Saccharomyces cerevisiae) — Review Notes

UniProt: **P32377** (MVD1_YEAST) · SGD: S000005326 (MVD1) · ORF: YNR043W · Chr XIV
Standard SGD name **ERG19**; aliases MVD1, MPD. PDB: **1FI4**.

## Identity and core function

ERG19 encodes **diphosphomevalonate decarboxylase** (mevalonate-5-diphosphate
decarboxylase; MDD/MVD), **EC 4.1.1.33**. It catalyzes the third and final step
of the mevalonate module of isoprenoid/ergosterol biosynthesis:

> (R)-5-diphosphomevalonate + ATP → isopentenyl diphosphate (IPP) + ADP + CO2 + phosphate
> (Rhea:RHEA:23732) [UniProt; PMID:8626466 "recombinant ... enzyme is a homodimer of 43-kDa subunits with a specific activity of 2.4 units/mg"]

This is an ATP-dependent decarboxylation: ATP phosphorylates the 3-hydroxyl of
diphosphomevalonate, and the resulting phosphate is eliminated together with the
carboxyl group (decarboxylation), yielding IPP. So although classed as a lyase
(carboxy-lyase, EC 4.1.1.x), the chemistry involves an ATP-dependent
phosphotransfer step — the enzyme is part of the **GHMP kinase superfamily**
(galactokinase, homoserine kinase, mevalonate kinase, phosphomevalonate kinase)
[PMID:15169949 "insight into phosphotransferase reactions catalyzed by a variety
of enzymes in the ... (GHMP kinase) family"].

IPP produced here is the universal C5 building block of all isoprenoids; in yeast
the downstream pathway makes farnesyl diphosphate (FPP), then squalene →
lanosterol → **ergosterol**, plus dolichol, ubiquinone, heme A, and substrates
for protein prenylation [UniProt FUNCTION; PMID:28904410].

## Essentiality and genetics

- **Essential gene** for viability. ERG19 disruption is lethal; ergosterol
  auxotrophy in the pathway cannot bypass the block at this step [PMID:9244250
  "the ERG19 gene, which was shown to be an essential gene for yeast, was disrupted"].
- A temperature-sensitive *erg19* allele carries a single **Leu79→Pro** change in a
  conserved sequence, conferring thermosensitivity [PMID:9244250; UniProt MUTAGEN L79].
- Original *erg19* mutant strains were isolated as ergosterol auxotrophs blocked in
  MDD [PMID:1779710 "mutant strains ... blocked in mevalonate diphosphate
  decarboxylase (erg19)"].
- High-level overexpression of wild-type ERG19 lowers steady-state sterol
  accumulation, suggesting a regulatory role in the mevalonate pathway [PMID:9244250].

## Structure

- Homodimer [PMID:11698677 SUBUNIT; PMID:8626466].
- Crystal structure **PDB 1FI4**, 2.27 Å, residues 1–396, solved as part of a
  structural-genomics effort on sterol/isoprenoid enzymes [PMID:11698677 "Structural
  genomics of enzymes involved in sterol/isoprenoid biosynthesis"].
- Two-domain GHMP-kinase-like fold (N-terminal + GHMP kinase C-terminal domain;
  Gene3D 3.30.230.10 + 3.30.70.890; SUPFAM ribosomal-S5-D2-like + GHMP kinase C).
- Substrate-binding residues (modeled by similarity): 19–22, 74, 153–158, 209
  (bind (R)-5-diphosphomevalonate) [UniProt FT BINDING].

## Active-site / catalytic residues

- **Asp302** is a crucial catalytic residue: D302N and D302A reduce k_cat ~10^3 and
  ~10^5-fold respectively, while still binding nucleotide — assigns a catalytic
  (general base) role to Asp302 [PMID:15169949 "10(3) and 10(5)-fold decreases in
  k(cat) ... support assignment of a crucial catalytic role to Asp 302"].
- **Lys18** influences the active site (K18M: 30-fold activity decrease, 16-fold
  higher K_m for ATP) but is not essential for chemistry [PMID:15169949].
  (Note: this study was on the GHMP/MDD active site generally; numbering per the
  enzyme studied — the conserved Asp/Lys are present in the yeast enzyme.)

## Localization

- Bulk proteomic/GFP data place the protein in the **cytoplasm/cytosol**
  [PMID:14562095 HDA cytoplasm; IBA cytosol GO_Central].
- A **vacuole** annotation (NAS) derives from the ergosterol-biosynthesis review,
  which describes the FPP/"second module" enzymes as acting in the vacuole
  [PMID:28904410]. This is a review-level, non-experimental assertion and conflicts
  with the high-throughput cytosolic localization; treat as weaker evidence. The
  UniProt comment likewise states the second module is "carried out in the vacuole"
  but cites the review, not direct localization of MDD.
- Abundance: ~13,700 molecules/cell in log-phase SD medium [UniProt MISCELLANEOUS,
  PMID:14562106].

## Pathway placement (mevalonate module)

acetyl-CoA → (HMG-CoA, HMG-CoA reductase ERG13/HMG1/HMG2) → mevalonate →
(ERG12, mevalonate kinase) → mevalonate-5-P → (ERG8, phosphomevalonate kinase) →
mevalonate-5-PP → **(ERG19/MVD1) → IPP** → (IDI1 isomerase) → DMAPP →
(ERG20, FPP synthase) → FPP → sterol/ergosterol + dolichol + ubiquinone + prenylation.

UniPathway: UPA00057 / UER00100 (IPP from (R)-mevalonate, step 3/3).

## Annotation review orientation

- **MF (diphosphomevalonate decarboxylase activity, GO:0004163)** — well supported
  by direct biochemistry (IDA PMID:8626466, PMID:15169949) and IMP (PMID:9244250,
  PMID:1779710). Clear **core function**. The multiple redundant IEA/RCA copies are
  acceptable but the IDA/IMP-backed ones are the primary evidence.
- **carboxy-lyase activity (GO:0016831)** — correct parent of GO:0004163, but a
  generalization; MODIFY/redundant relative to the specific term.
- **BP terms**: isopentenyl diphosphate biosynthetic process, mevalonate pathway
  (GO:0019287) is the most precise direct-process term → core. Ergosterol
  biosynthetic process (GO:0006696), sterol biosynthetic process (GO:0016126),
  isoprenoid biosynthetic process (GO:0008299), FPP biosynthetic process,
  mevalonate pathway (GO:0010142) are broader / downstream pathway memberships —
  keep but assess core vs non-core (the enzyme's *direct* product is IPP, not FPP
  or ergosterol; downstream-process terms are pathway-context, candidates for
  KEEP_AS_NON_CORE rather than as the molecular role).
- **CC**: cytosol/cytoplasm well supported; vacuole is weak (NAS from a review).
- ATP binding (GO:0005524, UniProtKB-KW) is correct biochemically (ATP is a
  co-substrate) though not in the GOA stub list — present in UniProt DR lines.

## Provenance note

Automated deep research succeeded on a third attempt:
`ERG19-deep-research-falcon.md` (falcon / "Edison Scientific Literature", 17 citations,
~19 min runtime). The first two attempts failed only because the wrapper's default
600 s cap killed the provider mid-run; re-running with `--timeout 3600` let it finish.
(The `WARNING - agentapi not found in PATH` line in the logs is benign and unrelated to
the timeout.) The review is grounded in the UniProt record (P32377), the six cached
primary publications (PMID:8626466, 15169949, 9244250, 1779710, 28904410, 14562095),
the structural-genomics paper for PDB 1FI4 (PMID:11698677), the PANTHER family data
(PTHR10977), and this deep-research report.

## Deep research (falcon) — corroboration & additions

The falcon report independently confirms the core review and contradicts nothing:

- **Reaction / cofactors:** confirms the ATP-dependent decarboxylation of
  mevalonate-5-diphosphate to IPP, and additionally states the reaction **requires
  Mg2+** and is coupled to ATP hydrolysis (products IPP + CO2 + ADP)
  [Cordier 1999, doi:10.1023/a:1006181720100; Garay 2026 preprint,
  doi:10.20944/preprints202605.0182.v1]. This reinforces the added ATP-binding
  molecular function; Mg2+ dependence is family/review-level here (flagged as inferred
  by the report) and is not annotated as metal binding in UniProt P32377, so no
  metal-ion GO term was added.
- **Mechanism:** GHMP-kinase-superfamily mechanism via ATP-dependent phosphorylation of
  the substrate C3-hydroxyl (transient 3-phospho-MVAPP) then decarboxylation/elimination
  — consistent with the Asp302/Lys18 active-site biochemistry [Garay 2026].
- **Localization:** independently described as a **cytosolic homodimer** / cytoplasmic
  precursor-module enzyme [Johnston 2020 Yeast, doi:10.1002/yea.3452; Garay 2026]. This
  further supports flagging the NAS vacuole annotation (GO:0005773) as over-annotated.
- **Essentiality:** an Arabidopsis MVD cDNA complements a yeast thermosensitive
  MVD-deficient strain and rescues the lethal **ERG19 deletion** [Cordier 1999] —
  additional support for essentiality alongside PMID:9244250.
- **Regulation (context, non-core):** ERG genes including ERG19 are controlled by
  Upc2/Ecm22 (sterol-responsive) and Hap1/Rox1/Mot3 (heme/oxygen); early-module genes
  (ERG8, ERG13, ERG19) are down-regulated as oxygen decreases [Jorda & Puig 2020 Genes,
  doi:10.3390/genes11070795 = PMID:32679672].
- **Applied context (non-core):** ERG19 is included in MVA-pathway overexpression
  cassettes for terpenoid production (e.g. 528 mg/L taxadiene, Karaca 2024) and is
  discussed as part of the essential fungal sterol axis for antifungal targeting
  (Gutierrez-Perez & Cramer 2025; fungal vs human homolog <50% identity).

None of these change the annotation actions; they corroborate the core MF/BP/CC calls
and the vacuole over-annotation flag.
