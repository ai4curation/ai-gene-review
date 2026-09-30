# LRATD2 literature notes

## Search and identity boundaries

Primary literature was searched manually in PubMed through 2026-08-13 using LRATD2,
FAM84B, BCMP101, and NSE2 names. Provider deep research was skipped as permitted; no
provider file was created. The most direct mechanistic studies found address vesicular
trafficking, N-myristoylation, an LRAT-like-region deletion, and NPM1 binding. Much of
the remaining literature concerns amplified tumor-cell contexts rather than normal
physiology.

LRATD2 is FAM84B/BCMP101 and has historically been called NSE2. The NSE2 alias is not
evidence that LRATD2 is NSMCE2/MMS21, the SUMO-ligase subunit of the SMC5/6 complex.
This collision has propagated into the LRATD2 cancer literature: PMID:26759717 states
that FAM84B forms DNA-repair complexes, but provides no LRATD2-specific experiment for
that claim. DNA-repair/SUMO-ligase functions must not be assigned to LRATD2 on this
basis.

LRATD1/FAM84A is a paralog, not an interchangeable name or functional donor. A direct
chemical-proteomics study tested both separately [PMID:34956690, "Alk12 labeling
signals decreased with the treatment of NMT inhibitor in LRATD1, LRATD2, and ERICH5
and were completely removed in G2A mutants, confirming LRATD1, LRATD2, and ERICH5 as
substrates of NMT1/2 (Figure 4C)."] LRATD1 morphology, motility, Ser38, localization,
or tissue-expression claims therefore cannot be transferred to LRATD2.

UniProtKB Q96KN1 has no curated named alternative protein isoforms. Multiple Ensembl
transcripts alone do not establish expressed or functionally distinct LRATD2 protein
isoforms, and the reviewed functional papers do not provide an isoform comparison.

## Direct cellular role: vesicular trafficking

The strongest focused functional study places human LRATD2 among cytosolic proteins
that associate with vesicle membranes in a GTP-dependent manner. Tagged LRATD2 was
partly cytoplasmic and partly at a juxtanuclear Golgi region [PMID:34433667, "HA-tagged
FAM84B/LRATD2 (FAM84B-HA) was partially located at the cytoplasm and partially located
at the juxtanuclear Golgi area colocalized with TGN46 (SI Appendix, Fig. S1A)."] In
cross-linked co-IP it associated with AP1gamma1 and Sec23A/B but not Sar1A
[PMID:34433667, "FAM84B-HA coimmunoprecipitated with AP1γ1 and Sec23A/B, but not
Sar1A in the presence of a cross-linker (Fig. 3B)."] These assays used tagged protein
in HEK293T cells and do not by themselves prove a stable endogenous coat complex.

Knockdown and rescue provide stronger functional evidence: [PMID:34433667, "Knockdown
of FAM84B/LRATD2 caused a significant delay of EGFR transport from the ER to the Golgi
in the RUSH transport system (Fig. 3C and SI Appendix, Fig. S3 A and B). The defects
were rescued by expressing a siRNA-resistant construct of FAM84B-HA (Fig. 3 D and E)."]
The lack of defects for ShhN and IGF2 demonstrates cargo selectivity rather than a
universal secretory-pathway requirement. The initial in vitro vesicle-discovery assay
used rat liver cytosol with permeabilized human HEK293T donor membranes, whereas the
cellular knockdown/rescue evidence concerns human LRATD2 in HEK293T cells.

## N-myristoylation and LRAT-like domain boundaries

LRATD2 is a substrate of human NMT1/2 in HEK293T chemical-labeling assays. Labeling was
hydroxylamine-resistant, reduced by NMT inhibition, and abolished by the Gly2-to-Ala
mutation [PMID:34956690, "However, three proteins LRATD1 (LRAT domain-containing 1,
also called FAM84A or neurological sensory protein 1 NSE1), LRATD2 (FAM84B/NSE2), and
ERICH5 (glutamate-rich protein 5) demonstrated clear fluorescence signals in the Alk12
treated samples compared to the control without Alk12 treatment, and the signals were
hydroxylamine-resistant, suggesting that they are potentially N-myristoylated."]. This
is a modification received by LRATD2, not lipid-metabolic catalysis performed by it.
Endogenous modification occupancy and its effect on membrane recruitment or trafficking
remain untested.

LRATD2 contains a sequence-classified LRAT-like domain, but no LRAT/HRASLS catalytic
reaction has been demonstrated. The prostate-cancer study notes that the catalytic
cysteine is absent and therefore infers loss of HRASLS phospholipase/O-acyltransferase
activities [PMID:31205500, "Since the catalytic residue Cys is not conserved (Figure
2), FAM84B is unlikely to have either enzymatic activities, which implies that FAM84B
facilitates Ras signaling."]. The final Ras-signaling clause is speculation, not direct
mechanistic evidence.

Deleting the LRAT/HRASLS-homologous region abolished overexpression-dependent invasion
and soft-agar growth in DU145 prostate-cancer cells [PMID:31205500, "FAM84B but not
FAM84B (ΔHRASLS) increased DU145 cell invasion and growth in soft agar."]. This supports
a structural requirement in that assay, not catalytic activity. Tagged full-length and
deletion constructs also co-precipitated, suggesting self-association under
overexpression conditions; endogenous oligomeric state and stoichiometry remain open.

## Cancer-context partners and phenotypes

In ESCC models, LRATD2 directly interacted with the NPM1 C terminus and increased
nuclear NPM1 [PMID:35396552, "A direct interaction between FAM84B and the C-terminal
(189-294aa) of NPM1 was identified, which increased the NPM1 nuclear expression."].
This is focused partner evidence, but the amplified/perturbed cancer context prevents
assuming a universal normal-tissue complex.

LRATD2 amplification and perturbation repeatedly affect tumor-cell behavior. ESCC
knockdown reduced growth, migration, and invasion [PMID:26759717, "Knockdown of FAM84B
in ESCC cell lines significantly reduced in vitro cell growth, migration and invasion."].
In PDAC, knockdown affected mitochondrial function and glycolysis [PMID:32291380,
"FAM84B knockdown also suppressed mitochondrial function and glycolysis of PDAC cells."].
These are downstream, disease-context phenotypes. They do not establish LRATD2 as a
metabolic enzyme, a direct Wnt/beta-catenin component, or a normal motility factor.

The seeded interactome sources report AP1M1, CHEK2, DDIT4L, NMT2, RAD51, TAX1BP1, and
UROD screen contacts. NMT2 is biologically reconciled by the direct substrate study;
the other high-throughput contacts lack focused endogenous validation. In particular,
CHEK2/RAD51 screen contacts do not rescue the NSE2/NSMCE2 naming problem or establish
DNA-repair-complex membership.

## Evidence-weighted conclusion

LRATD2 is best supported as a cytosolic/peripheral, N-myristoylatable protein that
participates in cargo-selective anterograde trafficking of EGFR in a human-cell assay.
Its LRAT-like region is required for several cancer-cell phenotypes but has no
demonstrated catalytic activity. NPM1 binding and diverse tumor phenotypes are useful
contextual evidence, while normal-tissue physiology, endogenous complex composition,
isoform diversity, and the functional consequence of myristoylation remain unresolved.
