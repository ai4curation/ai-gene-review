# CAD (human, UniProtKB:P27708) review notes

## Summary of biology

CAD is a large (2225 aa) multifunctional cytosolic protein that catalyses the first
three (committed) steps of de novo pyrimidine biosynthesis. It combines four enzymatic
activities across four domains, from N- to C-terminus:

1. **Glutamine amidotransferase (GATase, EC 3.5.1.2)** + **Carbamoyl-phosphate synthetase
   (CPSase)** together constitute the **glutamine-dependent carbamoyl phosphate synthetase II
   (CPS II, EC 6.3.5.5)**: L-glutamine + 2 ATP + HCO3- -> carbamoyl phosphate + L-glutamate
   + 2 ADP + Pi. This is the *cytosolic* pyrimidine CPS, distinct from the mitochondrial
   urea-cycle CPS1 (CPS I). The ammonia-dependent partial reaction is EC 6.3.4.16.
2. **Aspartate transcarbamylase (ATCase, EC 2.1.3.2)**: carbamoyl phosphate + L-aspartate ->
   N-carbamoyl-L-aspartate + Pi.
3. **Dihydroorotase (DHOase, EC 3.5.2.3, Zn2+-dependent)**: N-carbamoyl-L-aspartate ->
   (S)-dihydroorotate (reversible; the cyclization/dehydration step).

The endogenously produced carbamoyl phosphate is channeled from the CPS active site to the
ATCase active site [UniProt FUNCTION]. CAD assembles into a homohexamer (~1.5 MDa)
[PMID:24332717].

## Regulation

- Activity is allosterically regulated (PRPP activates; UMP/UTP inhibit the CPSase reaction).
- **MAP kinase (Erk1/2)** phosphorylates Thr-456 just prior to S phase, activating the pathway;
  PKA phosphorylation downregulates it as cells leave S phase [PMID:15890648; UniProt PTM].
- **mTOR/S6K1 (RPS6KB1)** phosphorylates Ser-1859, promoting oligomerization and stimulating
  the pathway [UniProt PTM; PMID:23429703, PMID:23429704 — mTORC1/S6K1 activates de novo
  pyrimidine synthesis].
- On EGF stimulation, phospho-Thr-456 CAD translocates to the nucleus; nuclear import promotes
  optimal cell growth [PMID:15890648].

## Disease

Biallelic (autosomal recessive) loss-of-function variants cause **CAD deficiency /
Developmental and epileptic encephalopathy 50 (DEE50, MIM:616457)**, a uridine-responsive
epileptic encephalopathy with anemia/anisopoikilocytosis; it is also classified as a
congenital disorder of glycosylation (CAD-CDG) because impaired pyrimidine synthesis
depletes UDP-sugar glycosylation donors [PMID:25678555]. Uridine supplementation rescues the
metabolic and clinical phenotype.

## Interactions

- **Rad9** (checkpoint protein) binds the CPSase domain of CAD and stimulates CPSase activity
  ~2-fold [PMID:15326225] -> supports GO:0019899 enzyme binding (with Rad9, UniProtKB:Q99638).
- **14-3-3 (YWHAZ)** [PMID:15161933, IntAct], **CNTROB** [PMID:35709258, IntAct], and
  self-interaction (homohexamer) [PMID:24332717] — generic protein binding IPIs.
- **Adenovirus preterminal protein (pTP)** binds CAD at nuclear-matrix viral replication
  sites [PMID:9525610] — supports nuclear matrix localization.

## Curation decisions (headline)

Core MFs (all strongly supported by structure/enzymology + IBA + EC/ISS):
- GO:0004088 carbamoyl-phosphate synthase (glutamine-hydrolyzing) activity (CPS II)
- GO:0004087 carbamoyl-phosphate synthase (ammonia) activity (partial CPS reaction)
- GO:0004359 glutaminase activity (GATase partial reaction)
- GO:0004070 aspartate carbamoyltransferase activity (ATCase; EXP PMID:24332717)
- GO:0004151 dihydroorotase activity (DHOase; IDA/EXP PMID:24332717, Zn2+)
Core BP: GO:0044205 'de novo' UMP biosynthetic process; GO:0006207 'de novo' pyrimidine
nucleobase biosynthetic process. Core CC: GO:0005829 cytosol.

Flag / over-annotation:
- GO:0004672 protein kinase activity (ISS from P08955): CAD has NO kinase domain; this is a
  spurious ISS transfer (P08955 is Dictyostelium; CAD is a substrate of kinases, not a kinase).
  MARK_AS_OVER_ANNOTATED (do not REMOVE — ISS, not IEA-EC; but biologically unsupported).
- Bare GO:0005515 protein binding IPIs (14-3-3, CNTROB) and GO:0042802 identical protein
  binding: uninformative; keep experimental but MARK_AS_OVER_ANNOTATED per policy.
- GO:0016020 membrane (HDA, NK-cell membrane proteome) and GO:0070062 extracellular exosome
  (HDA): CAD is cytosolic; these are proteomic co-purification, not genuine locations ->
  over-annotated.
- Ensembl GO_REF:0000107 rat/mouse ortholog transfers (liver development, heart development,
  lactation, response to caffeine/cortisol/insulin/testosterone, xenobiotic metabolism,
  L-citrulline biosynthesis, etc.): these are pleiotropic physiology / whole-animal responses
  transferred electronically; not core. L-citrulline biosynthesis (GO:0019240) and xenobiotic
  metabolism are biologically dubious for the cytosolic pyrimidine CPS -> over-annotated.
