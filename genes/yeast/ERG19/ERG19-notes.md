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

Automated deep research (`just deep-research-falcon yeast ERG19 --fallback
perplexity-lite`) did not return output (stalled >10 min and was cancelled), so no
`-deep-research-{provider}.md` file was generated. This review is instead grounded in
the UniProt record (P32377), the six cached primary publications (PMID:8626466,
15169949, 9244250, 1779710, 28904410, 14562095), the structural-genomics paper for
PDB 1FI4 (PMID:11698677), and the PANTHER family data (PTHR10977). For this
well-characterized essential metabolic enzyme these sources are sufficient.
