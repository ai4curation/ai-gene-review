# APOC4 (human) — research notes

UniProt P55056 · HGNC:611 · GeneID 346 · chromosome 19, APOE/APOC1/APOC4/APOC2 cluster
· PANTHER PTHR32288 (APOLIPOPROTEIN C-IV), subfamily SF0 · Pfam PF15119 · InterPro IPR028120
· 127 aa precursor, signal 1–27, mature chain 28–127.

Accession check: `APOC4-uniprot.txt` header reads `ID   APOC4_HUMAN             Reviewed;         127 AA.`
and `AC   P55056; B3KWY6; Q53YY8;` — the expected reviewed human APOC4 entry, not a merged
redirect to another protein.

## 1. What the protein is

APOC4 encodes apolipoprotein C-IV, the fourth and least-studied member of the low-molecular-weight
apoC group. It was found by walking the apoE/C-I/C-II locus rather than by biochemistry: a 3.3-kb
three-exon gene whose 3' end sits 555 bp upstream of APOC2 in the same transcriptional orientation
[PMID:8530039 "Nucleotide sequence analysis of genomic DNA and liver cDNA clones revealed a 3.3-kb
gene consisting of three exons and two introns. Its 3' terminus lies 555 bp upstream of APOC2, giving
both genes the same transcriptional orientation."]. The same paper predicted the protein from sequence
alone — "The predicted apoC-IV protein sequence, comprising 127 amino acid residues, contains a
putative 25-residue signal peptide and two potential amphipathic alpha-helical domains" — and noted
"relatively low apoC-IV mRNA levels in human liver, compared to apoC-II mRNA levels". UniProt places
the signal peptide at 1..27 by similarity to the rabbit orthologue (`FT   SIGNAL          1..27` with
`/evidence="ECO:0000250|UniProtKB:P55057"`), one of several small discrepancies with the 1995
prediction.

UniProt's own functional statement is a single hedged line — `CC   -!- FUNCTION: May participate in
lipoprotein metabolism.` — with `CC   -!- SUBCELLULAR LOCATION: Secreted.` and `CC   -!- TISSUE
SPECIFICITY: Expressed by the liver and secreted in plasma.` That hedge is the correct starting
posture: a 2023 review of the apoC quartet puts it bluntly, "Contrarily, almost nothing is known
about APOC4" [PMID:37226733], and explains the neglect: "The APOC4 gene was discovered and
characterized nearly 25 years ago,78 but so far has not attracted much attention, perhaps because
plasma levels of APOC4 are at least an order of magnitude lower than those of APOC1, APOC2 and
APOC3" [PMID:37226733].

The protein carries one N-glycosylation site, `FT   CARBOHYD        63` /
`/note="N-linked (GlcNAc...) asparagine"`, evidenced from plasma glycoproteomics
(ECO:0000269|PubMed:16335952) — i.e. the site was mapped on protein actually circulating in blood,
not on a recombinant construct.

## 2. Direct evidence on the human protein

There is more than the affinage record suggests, and it is worth separating by what it establishes.

**Plasma isolation and particle distribution (the decisive paper).** Kotite et al. isolated human
apoC-IV from apoVLDL and sequenced it: the abstract states "Human apoC-IV, isolated from apo VLDL by
DEAE-cellulose chromatography and two-dimensional electrophoresis, was identified by microsequencing
four tryptic peptides" and gives the distribution directly — "In normolipidemic plasma, greater than
80% of the protein is in VLDL (0.7% of total apo VLDL), with most of the remainder in HDL"
[PMID:12700345]. The same paper reports the two glycoforms ("The protein exhibits two major isoforms;
one is N-glycosylated, and both are variably sialylated"), the concentration range and its
relationship to triglyceride ("The concentration of apoC-IV in the plasma and lipoproteins of rho <
1.21 g/ml is closely related to plasma triglyceride concentration up to 1,770 mg/dl, varying from
0.1-1.9 mg/dl"), and — importantly for the IBA donors below — that the same is true across species:
"We show that apoC-IV is a basic protein in human, monkey, and mouse plasma, present as a minor apoC
component of VLDL".

This paper also corrects the earlier record. Allan & Taylor had reported "apoC-IV was not detected in
normal adult human plasma or isolated plasma lipoproteins, a finding consistent with our previous
observation of very low levels of human apoC-IV mRNA in human liver" [PMID:8827523] — an
immunoblot-sensitivity limit, not an absence, as the 2003 isolation shows.

**Independent VLDL proteomics.** A 2-DE/MALDI-TOF-TOF map of human VLDL identified "three isoforms of
apoC-IV" among the VLDL-associated apolipoproteins [PMID:17154273], a second, methodologically
unrelated detection of the protein on human VLDL.

**HDL proteomics (not in GOA, and not found by affinage).** Two later human studies detect apoC-IV as
an HDL cargo protein: "Specifically, our work identified 5 HDL-bound apolipoproteins that were
significantly decreased in patients with NAFLD and advanced fibrosis: ApoC-I, ApoC-IV, ApoM, LCAT,
and SAA4" [PMID:36173828], and APOC4 appears among HDL proteins tracked after stroke — "Changes in
nine proteins (APOE, APOF, APOL1, APMAP, APOC4, APOM, LPA, PCYOX1, PON1) significantly correlated"
[PMID:32844720]. These matter because the HDL claim in GOA rests on a single clause of a single 2003
abstract; two independent proteomic datasets now corroborate it.

**Transgenic overexpression.** Human apoC-IV expressed from a cDNA transgene in mice associates with
lipoproteins and causes hypertriglyceridaemia: "Human apoC-IV was found associated with plasma
lipoproteins (d < 1.21 g/ml), mainly in very low density lipoproteins (VLDL), and higher molecular
mass isoforms were present, due to N-linked glycosylation and variable sialylation of apoC-IV" and
"Human apoC-IV transgenic mice were hypertriglyceridemic compared to nontransgenic controls; the
accumulated plasma triglycerides were present mainly in VLDL" [PMID:8827523]. The authors' own summary
of what this establishes is a lipid-binding claim, not a mechanism: "our analysis of transgenic mice
provides unequivocal evidence that human apoC-IV is a lipid-binding protein belonging to the
apolipoprotein family and that it has the potential to alter lipoprotein metabolism".

Grade this as IMP/gain-of-function, not IDA, and read the dose caveat in the later review: "Endogenous
APOC4 is thought to increase plasma triglyceride levels because overexpression of human APOC4 at
supraphysiological levels in mice causes elevated levels of VLDL" [PMID:37226733]. There is no
apoC-IV knockout in any species — a Europe PMC search for apoC-IV with knockout/deficient terms
returns only reviews and HDL-proteomics papers, none reporting a targeted deletion.

**Hepatoma overexpression and steatosis.** Transient transfection of the APOC4 cDNA into Huh-7 cells
produced lipid droplets and a measurable triglyceride rise: "The enzymatic assay revealed a moderate
increase in triglyceride in cells transfected with ApoC-IV gene as compared to mock transfected cells
(Fig. 7B, left, p = 0.024). Considering the transfection efficiency of about 40%, the triglyceride
content in ApoC-IV transfected cells was approximately 2.7-fold higher than that in vector transfected
cells." [PMID:18809223]. The bulk of that paper is about what regulates APOC4 — HCV core protein, Ku70/Ku80
and PPARγ/RXRα acting on a 163-bp promoter element — so APOC4 is mostly the *readout*; the transfection
experiment is the one place it is the agent, and it is a single ectopic gain-of-function in a transformed
hepatoma line. The in vivo arm is explicitly correlative: "the ApoC-IV transcript levels correlated with
the concentration of intracellular triglycerides in the HCV infected livers as revealed by a coefficient
of determination (R2 = 0.78)".

**Genetics.** Three coding variants (Leu36Pro, Gly52Asp, Leu96Arg) with "a significant association of
the Leu36Pro and the Leu96Arg polymorphisms with triglyceride levels in women" [PMID:10996355]; the
effect is small — "the contribution of APOC4 genetic variation to plasma triglycerides was only 2%"
[PMID:37226733]. Locus-level GWAS signals at APOE-APOC1-APOC4-APOC2 cannot be assigned to APOC4
specifically and are not used here.

## 3. Family context: the rabbit protein carries the biophysics

The one place apoC-IV has been characterised as a protein rather than a plasma marker is the rabbit,
where it is abundant. Zhang, Kotite & Havel showed the mature protein "is associated with the
lipoproteins of blood plasma, primarily very low density and high density lipoproteins", that "It
contains two potential amphipathic helices characteristic of plasma apolipoproteins and forms
discoidal micelles with phosphatidylcholine", that expression is liver-restricted ("Northern analysis
shows a single 0.6-kilobase apolipoprotein C-IV mRNA, detected only in the liver"), that it is
secreted ("Sialylated apolipoprotein C-IV is secreted from transfected mammalian cells"), and that
the gene "has been highly conserved during mammalian evolution" [PMID:8576182].

Discoidal-micelle formation with phosphatidylcholine is the classical demonstration that an
exchangeable apolipoprotein binds and solubilises phospholipid. It is the only direct lipid-binding
measurement anywhere in this family — and it is invisible to GO. Rabbit APOC4 (P55057) carries
**five GO annotations, all IEA** (QuickGO, 2026-09-12): GO:0005576 from the UniProt subcellular-location
pipeline, and GO:0010890, GO:0070328, GO:0034361, GO:0034364 all from GO_REF:0000118 via
PANTHER:PTN001284070. Nothing experimental. So PAINT could not use the rabbit protein as an IBD seed
even though it is the best-characterised member of the family. That is a curation gap worth reporting,
not an IBA defect.

## 4. The four IBAs: one node, one family, no C-II/C-III leakage

The prior worry was that apoC-IV's IBAs might be inherited from a mixed apolipoprotein-C family node
carrying apoC-II or apoC-III biology. They are not. PTHR32288 is named APOLIPOPROTEIN C-IV, has a
single subfamily (SF0), and `interpro/panther/PTHR32288/PTHR32288-entries.csv` names every reviewed
member "Apolipoprotein C-IV". APOC1/C2/C3 are in other families.

All four IBA rows descend from one node. From `interpro/panther/PTHR32288/PTHR32288-paint.tsv`:

| term | node | IBD seeds | node taxon | IBD date |
|---|---|---|---|---|
| GO:0034361 very-low-density lipoprotein particle | PTN000792756 | `MGI:MGI:87878` + `UniProtKB:P55056` | taxon:9347 | 2017-02-28 |
| GO:0034364 high-density lipoprotein particle | PTN000792756 | `UniProtKB:P55056` | taxon:9347 | 2017-02-28 |
| GO:0070328 triglyceride homeostasis | PTN000792756 | `UniProtKB:P55056` | taxon:9347 | 2017-02-28 |
| GO:0019915 lipid storage | PTN000792756 | `UniProtKB:P55056` | taxon:9347 | 2025-06-24 |

Donor resolution:

- `MGI:MGI:87878` → `Q61268` = APOC4_MOUSE (reviewed), via
  `rest.uniprot.org/uniprotkb/search?query=xref:mgi-87878` — the mouse orthologue, not a paralog.
- `UniProtKB:P55056` is the target itself. Per the project's IBA rules this is correct and expected:
  the human gene's own experimental annotations are among the descendant evidences the PAINT curator
  used to place the IBD, so the target legitimately appears among its own sources. It is a marker
  that experimental grounding exists on the target, not circularity.
- `P55057` (rabbit) is **not** a seed, for the reason in §3.

Node placement checks out on two independent grounds. Taxonomically, taxon:9347 is Eutheria, and the
family is essentially eutherian: 185 of 189 InterPro-assigned members, and 146 of 149 source organisms,
are inside Eutheria; the exceptions are three marsupial apoC-IV sequences and one uncharacterised
*Tetrahymena* protein (see `file:human/APOC4/APOC4-bioinformatics/RESULTS.md`). That matches the
published phylogeny — "ApoC-IV first arose in Eutheria" [PMID:31722659] — so the node sits at or just
inside the family's own origin and every mammalian APOC4 is inside the inheriting clade by
construction. The node propagates all four terms to exactly 11 gene products (human, mouse, rat, chimp,
gorilla, macaque, cat, dog, horse, pig, cow), counted from the cached PAINT GAF; there is no IRD or
IKR anywhere in the slice, and nothing to suggest apoC-IV has been lost or diverged in the human
lineage.

What the node placement does **not** fix is the strength of the seeds, and this is where the four rows
differ:

- **GO:0034361 (VLDL)** has two gene-level donors, and both trace to the same publication. Mouse Apoc4
  (Q61268) carries exactly one experimental annotation in QuickGO — `GO:0034361 IDA PMID:12700345` —
  which is the mouse-plasma clause of the very paper that supports the human IDA. So "two donors" here
  means two species observed in one study, not two independent studies. The claim is nonetheless solid:
  it is a direct isolation, replicated independently on human VLDL by PMID:17154273.
- **GO:0034364 (HDL)** rests on a single seed and, within that seed, on one clause — "with most of the
  remainder in HDL". Corroborated since by PMID:36173828 and PMID:32844720, but it is the minor pool:
  >80% of apoC-IV is on VLDL.
- **GO:0070328 (triglyceride homeostasis)** rests on a single seed whose evidence is the transgenic
  overexpression phenotype, at supraphysiological dose.
- **GO:0019915 (lipid storage)** rests on a single seed whose evidence is one transfection of a
  hepatoma line. The IBD is dated 2025-06-24, seven months after the BHF-UCL IMP (2024-11-01), so the
  chain is: one 2008 Huh-7 experiment → 2024 human IMP → 2025 IBD at Eutheria → IBA back onto the human
  gene and ten other species. That is a lot of taxonomic reach for one cell-culture result.

A related asymmetry worth flagging: rabbit APOC4 carries GO:0010890 (positive regulation of triglyceride
storage) from a different PANTHER node (PTN001284070, via the GO_REF:0000118 IEA pipeline, which is not
PAINT), while the human gene carries the broader GO:0019915. Nothing in this review turns on it.

## 5. What does not belong to apoC-IV, checked rather than assumed

**Lipase regulation.** No lipoprotein-lipase term appears anywhere in APOC4's 41 GOA rows, and that is
correct. The mechanism proposed for the transgenic phenotype is displacement of apoE, explicitly not
lipase inhibition: "The mechanism of the elevated VLDL levels in APOC4 transgenic mice was suggested to
be due to displacement of APOE, resulting in reduced hepatic clearance of VLDL, rather than to a
reduction in lipase activity" [PMID:37226733]. Lipase activation is apoC-II biology — QuickGO gives
APOC2 (P02655) GO:0060230 lipoprotein lipase activator activity and GO:0016004 phospholipase activator
activity, neither of which appears on APOC4 — and lipase inhibition is apoC-III biology. A Europe PMC search for apolipoprotein C-IV together with
lipoprotein lipase returns proteomics surveys and reviews, no assay of apoC-IV on lipase.

The apoE-displacement idea is itself a hypothesis in a review ("are believed to slow the clearance of
TRLs and their remnants in part by interfering with APOE binding to the hepatic receptors, LDLR ... and
LRP1" [PMID:37226733]), asserted for APOC1/C3/C4 as a group. It is not measured for apoC-IV and must
not become a GO annotation.

**Chylomicron.** GO:0042627 is absent from APOC4 and there is no evidence for adding it: every direct
measurement places apoC-IV on VLDL and HDL.

**The APOC4-APOC2 readthrough.** This was checked directly rather than assumed. The readthrough locus
has its own UniProt entry — `K7ER74_HUMAN`, unreviewed, 178 aa, gene name `APOC4-APOC2`, and UniProt
names the product "Apolipoprotein C-II", i.e. the readthrough translates apoC-II, not apoC-IV. K7ER74
carries its own seven IEA rows in QuickGO, including exactly the apoC-II-flavoured terms one would
worry about leaking: GO:0008047 enzyme activator activity (GO_REF:0000002), GO:0042627 chylomicron and
GO:0006869 lipid transport (GO_REF:0000120), GO:0034361 and GO:0034362 (GO_REF:0000104). **None of those
terms appears on P55056.** The two accessions are cleanly separated and no row in this review derives
from the readthrough transcript. The GWAS literature's "APOC4-APOC2" is a locus label, not this
transcript.

**GO:0005515 protein binding ×23.** All 23 rows come from one reference, PMID:32296183 (HuRI), the
CCSB yeast two-hybrid reference interactome — "yeast two-hybrid (Y2H) represents the only binary PPI
assay that can be operated at sufficient throughput to systematically screen the human proteome for
binary PPIs". Reference-projection test (QuickGO `downloadSearch?reference=PMID:32296183`, full
export): **85,343 annotations across 6,769 distinct gene products, of which 84,937 are GO:0005515.**
APOC4's 23 rows are 23 of those.

Resolving every partner in UniProt (subcellular location field, by
`APOC4-bioinformatics/huri_partner_topology.py`, whose per-partner output is committed as
`huri_partners.tsv`) gives a topologically impossible set for a secreted plasma apolipoprotein.
Counted rather than eyeballed:
**0 of 23 have a curated Secreted or Extracellular location, 10 of 23 carry a curated mitochondrial
location** (IFI27, MICOS10, MICOS13, LETMD1, MAIP1, BCL2L2, TIMMDC1, DIABLO, NFU1, RSAD2), **10 of 23
have a transmembrane segment, 1 (THBD) has a cleaved signal peptide, and 1 (SYT16) has no curated
location at all**. The remainder are cytosolic, nuclear or endomembrane (GAD2, TPRG1, APOL2, UBQLN1,
UBQLN2, SENP2, SNAP47, GSDMA, PORCN, TBC1D20, TMEM14B). Not one is a plasma or lipoprotein-associated
protein. The load-bearing distinction is not "intracellular" — APOC4's mature chain does transit the ER
and Golgi lumen on the way out of the hepatocyte — but which *face* of the compartment: APOC4 is lumenal
then extracellular, and never faces the cytosol, the mitochondrial matrix or the nucleus, which is where
all 23 partners work. Five (MICOS10, MICOS13, MAIP1, BCL2L2, TIMMDC1) are curated exclusively to the
mitochondrion, which has no secretory-pathway connection at all. THBD is the single partial exception
worth stating: as a single-pass type I membrane protein it does present an extracellular domain to
flowing blood, so an encounter is not topologically absurd — but that is precisely the topology a nuclear
Gal4 two-hybrid cannot test. A reader checking UniProt will see `NbExp=3` on every one of these pairs;
that is HuRI's own screen-and-retest count from this single publication, not three independent studies.
APOC4 carries a cleaved signal
peptide (`FT   SIGNAL          1..27`) and never occupies the compartment in which any of these was
tested; in Y2H both partners are expressed as Gal4 fusions in the yeast nucleus, so the assay cannot
put apoC-IV where its own biology happens. HuRI itself notes "the majority of PPIs in HuRI were found
in only one screen". No functional follow-up exists for any of the 23 pairs. These are over-annotations
of an uninformative term, not evidence of a moonlighting function — and per project policy the fix is
`MARK_AS_OVER_ANNOTATED`, not `REMOVE` of experimental rows.

## 6. Bioinformatics done here

See `file:human/APOC4/APOC4-bioinformatics/RESULTS.md`. Two live analyses:

1. **Family taxonomic span** — corroborates the Eutheria node placement (185/189 members inside
   Eutheria; the only non-eutherian apoC-IVs are three marsupial sequences).
2. **Amphipathic-helix scan** — Eisenberg hydrophobic moment over 18-residue windows on mature chains.
   The discriminating statistic is the density of non-overlapping μH ≥ 0.35 segments: exchangeable
   apolipoproteins (APOA1, APOC1, APOC2, APOC3, and apoC-IV from human, rabbit and mouse) fall at
   0.0206–0.0351 per residue, globular controls (β2-microglobulin, thioredoxin) at 0.0096–0.0101.
   The groups do not overlap; the script derives the separation as 2.04× at the narrowest and 3.66×
   at the widest. Human apoC-IV is 0.0300, about three times the controls (2.97–3.12×), 0.0009 from
   rabbit apoC-IV and 0.0021 from APOA1. A single strongest window does not
   discriminate — the negative controls reach μH ≈ 0.46–0.48 too — which is why density is the reported
   metric.

This supports the sequence half of the 1995 amphipathic-helix inference and, with the rabbit
discoidal-micelle result, supports proposing phospholipid binding by similarity. It is not itself an
assay and cannot substitute for one on the human protein.

## 7. Curation decisions taken

Propagation verdicts (seven `propagation_review` blocks — four IBA, two IEA-with-WITH/FROM, one
authored ISS):

| row | root_cause | why |
|---|---|---|
| GO:0034361 VLDL, IBA | `NO_FAILURE_CORE` | correct node, correct clade, corroborated by the target's own IDAs |
| GO:0034364 HDL, IBA | `NO_FAILURE_NON_CORE` | correct, but the minor (<20%) pool |
| GO:0070328 TG homeostasis, IBA | `NO_FAILURE_NON_CORE` | in vivo phenotype, but gain-of-function at supraphysiological dose |
| GO:0019915 lipid storage, IBA | `SOURCE_WEAK_OR_INFERRED` / `SOURCE_EVIDENCE_WEAK` | one 2025 IBD from one 2008 Huh-7 transfection, now reaching 11 species |
| GO:0005576, IEA GO_REF:0000044 | `NO_FAILURE_CORE` | SL-0243 "Secreted" is right and the mapping is right |
| GO:0034361, IEA GO_REF:0000107 | `EVIDENCE_CIRCULAR_OR_REDUNDANT` | donor's own IDA is the same paper as the target's; and the two WITH/FROM ids are one donor |
| GO:0005543, NEW ISS | `NO_FAILURE_CORE` | rabbit orthologue, direct measurement, conserved helix architecture |


- GO:0005319 lipid carrier activity (TAS): **ACCEPT**. The term was renamed from "lipid transporter
  activity" to "lipid carrier activity" on 2026-02-09 and now carries `apolipoprotein` as a narrow
  synonym; its `replaces` list covers the obsoleted GO:0005321 and GO:0005323 (the old high-density
  and very-low-density lipoprotein MF terms) and it is the `consider` target for the obsoleted
  GO:0005320 "apolipoprotein" (QuickGO `/ontology/go/terms/GO:0005319/complete`). It is the designated apolipoprotein MF term.
  The 1995 TAS is prediction-level, but the claim is independently supported by PMID:8827523's
  lipid-binding conclusion and by the plasma isolation.
- GO:0034361 VLDL particle: **ACCEPT** on all rows; this is the core localisation (>80% of the protein).
- GO:0034364 HDL particle: **KEEP_AS_NON_CORE**; genuine but the minor pool.
- GO:0070328 triglyceride homeostasis: **KEEP_AS_NON_CORE**; supported only by supraphysiological
  overexpression, with no loss-of-function anywhere.
- GO:0019915 lipid storage: **KEEP_AS_NON_CORE**; single ectopic overexpression in a hepatoma line.
- GO:0006629 lipid metabolic process (TAS): **KEEP_AS_NON_CORE**; true but uninformative.
- GO:0005576 extracellular region (5 rows): **ACCEPT**; secretion into plasma is directly established.
- GO:0005515 ×23: **MARK_AS_OVER_ANNOTATED**, per §5.
- GO:0034361 IEA (GO_REF:0000107, Ensembl Compara from mouse Q61268): correct, but the donor's own
  GO:0034361 IDA is from PMID:12700345 — the same publication that gives the human its direct IDA. The
  row re-derives by orthology a claim the target already holds from the same experiment.
- **NEW** GO:0005543 phospholipid binding, ISS from rabbit P55057 (PMID:8576182 discoidal micelles with
  phosphatidylcholine), supported at the sequence level by the helix scan. Coded ISS rather than IDA
  because the measurement is on the orthologue, not on the human protein.

## 8. What the affinage record missed

Trust gates cleared (`.affinage.log`: "APOC4: trust gates clear"), `faith_pct: 100.0`,
`self_evaluation_pairwise` is empty, and the narrative correctly describes *this* protein — no symbol
collision. But recall is the problem, exactly as the campaign brief predicts. Its four citations are
PMID:8530039, PMID:10996355, PMID:29580721 and PMID:33705959. It therefore missed:

APOC4 has 29 experimental GOA rows, but 23 of those are the single HuRI two-hybrid screen; only six
(3 IDA + 3 IMP) come from hypothesis-driven work, and they trace to exactly four references. Affinage
cited **none of those four**:

- **PMID:12700345** — the isolation of apoC-IV from human plasma VLDL and the >80% VLDL / remainder HDL
  distribution. This is the single most important experimental paper on the protein and the basis of
  two GOA rows (VLDL IDA, HDL IDA).
- **PMID:8827523** — the transgenic-mouse hypertriglyceridaemia study, basis of two more (VLDL IMP,
  triglyceride-homeostasis IMP).
- **PMID:18809223** and **PMID:17154273** — the remaining two experimental rows (lipid-storage IMP,
  VLDL IDA).
- **PMID:8576182** — the rabbit characterisation carrying the only direct lipid-binding measurement in
  the family.
- **PMID:37226733** — the review that states the apoE-displacement mechanism and the
  not-a-lipase-effect negative.
- **PMID:31722659** — the phylogeny placing apoC-IV's origin at Eutheria.

Its narrative claim that "no enzymatic activity, receptor interaction, or reconstituted mechanism for
apoC-IV has been characterized in the available corpus" is true as stated, but it leads with the 1995
prediction and the 2000 SSCP study while omitting every paper that actually measured the protein. The
two low-confidence 2018/2021 findings it does surface (hydroxyapatite binding in sub-RPE deposits;
a miR-372-3p target axis) are single-study associations that support no GO annotation and are not used
here. Its `mechanism_profile` is empty, so there was no GO grounding to import.

## 9. Open questions

- No loss-of-function model exists in any species. Every functional claim about apoC-IV rests on
  gain-of-function at non-physiological dose.
- Is the apoE-displacement mechanism real for apoC-IV specifically, or inherited by analogy from
  APOC1/C3? A direct binding/competition experiment would settle whether apoC-IV deserves any
  receptor-clearance annotation.
- Does human apoC-IV bind phospholipid directly, as the rabbit protein does? A discoidal-complex assay
  on the human mature chain would convert the proposed ISS row into an IDA.
- What is the function of the N-glycan at Asn-63 and of the sialoform heterogeneity, conserved from
  rabbit to human?
- Why is apoC-IV abundant in rabbit plasma but an order of magnitude below the other apoCs in human?
  Kotite et al. suggest a promoter answer — a rabbit-specific GAGA-box repeat — but it has not been
  tested.
