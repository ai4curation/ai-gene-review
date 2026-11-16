# FSHR (human, UniProtKB:P23945) — curation notes

Follicle-stimulating hormone receptor / follitropin receptor (FSH-R), gene synonym LGR1.
695 aa precursor; signal peptide 1-17; large N-terminal leucine-rich-repeat ectodomain
(LRRNT 18-46, nine LRRs 49-259, hinge region with sulfotyrosine 335), seven
transmembrane helices 367-630, cytoplasmic tail 631-695
[file:human/FSHR/FSHR-uniprot.txt FT lines].

## 1. Identity and family

- Rhodopsin-like (class A) GPCR of the glycoprotein-hormone receptor subfamily, with
  LHCGR and TSHR: "The glycoprotein hormone receptors (thyrotrophin receptor, TSHr;
  luteinizing hormone/chorionic gonadotrophin receptor, LH/CGr; follicle-stimulating
  hormone receptor, FSHr) constitute a subfamily of rhodopsin-like G protein-coupled
  receptors (GPCRs) with a long N-terminal extracellular extension responsible for
  high-affinity hormone binding" [PMID:11847099].
- PANTHER family PTHR24372 (GLYCOPROTEIN HORMONE RECEPTOR), subfamily PTHR24372:SF5
  (FOLLICLE-STIMULATING HORMONE RECEPTOR) [file:human/FSHR/FSHR-uniprot.txt DR PANTHER].
  The family node PTN000689980 spans glycoprotein-hormone receptors *and* the wider LGR
  clade (Drosophila rk/rickets = bursicon receptor FBgn0003255; relaxin-family
  receptors), while PTN002809188 is the vertebrate FSHR clade
  [interpro/panther/PTHR24372/PTHR24372-paint.tsv].
- UniProt tissue specificity: "Sertoli cells and ovarian granulosa cells"
  [file:human/FSHR/FSHR-uniprot.txt CC TISSUE SPECIFICITY].

## 2. Ligand and ligand specificity

- Agonist is follitropin (FSH), the CGA:FSHB heterodimer. Human receptor expressed in
  HEK293 bound FSH with high affinity and did not respond to LH, hCG or TSH:
  "radioligand receptor analysis revealed the presence of high affinity (Kd, 1.7 x
  10(-9) M) FSH-binding sites on the plasma membrane" and "After incubation of
  transfected cells with hFSH, but not recombinant hLH or hCG, a dose-dependent increase
  (ED50, 10 ng/ml) in extracellular cAMP accumulation was observed, indicating a
  functional coupling of the expressed human receptor with the endogenous adenyl
  cyclase" [PMID:1322283]. The same paper reports species-specific recognition:
  "only hFSH and rFSH interacted effectively with the recombinant hFSH receptor,
  suggesting that species-specific ligand recognition exists between human and rodent
  receptors" [PMID:1322283].
- Structural basis of binding: "The hormone is bound in a hand-clasp fashion to an
  elongated, curved receptor" and "binding specificity is mediated by key interaction
  sites involving both the common alpha- and hormone-specific beta-subunits"
  [PMID:15662415]. The complete ectodomain structure adds the hinge:
  "FSHR then inserts its sTyr (i.e., sulfated Tyr335) into the FSH nascent
  pocket, eventually leading to receptor activation" [PMID:22802634].
- Tyrosine sulfation of the hinge motif is required for agonist recognition in this
  receptor family: "Site-directed mutagenesis experiments indicate that the motif, which
  is conserved in all members of the glycoprotein hormone receptor family, seems to play
  a similar role in the LH/CG and FSH receptors" [PMID:11847099]. Confirmed structurally:
  "A conserved sulfated tyrosine at the hinge loop (Y335 from FSHR, Y331 from LHCGR and
  Y385 from TSHR) was shown to involve in hormone binding and activation of the receptor"
  [PMID:36720854, introduction].

## 3. Transduction

- Gs/cAMP is the principal route. Cryo-EM of the hormone-bound receptor was solved as an
  FSH-FSHR-Gs complex: "Here we report cryo-EM structures of FSHR in both inactive and
  active states, with the active structure bound to FSH and an allosteric agonist
  compound 21 f" [PMID:36720854]. cAMP accumulation and CRE-luciferase induction follow
  FSH in cells expressing the human receptor [PMID:1322283; PMID:24058690].
- PI3K/AKT is a second branch, shown by loss in a patient mutant: "As shown in Figure 7,
  treatment with 100 mIU/L FSH induced phosphorylation of PI3K in FSHwt cells but not in
  either FSHmt or FSHwt/mt cells" [PMID:24058690].
- ERK1/2 is activated by FSH in cells expressing the receptor: "In contrast, ERK1/2 was
  phosphorylated similarly in FSHwt, FSHmt and FSHwt/mt cells when treated with 100
  mIU/L FSH (Figure 8)" [PMID:24058690]. Part of the ERK response is beta-arrestin
  dependent and cAMP independent: "both the A189 V and wild-type (Wt) FSHRs selectively
  activated cAMP-independent ERK phosphorylation when expressed at low plasma membrane
  densities" [PMID:20801186]. beta-arrestin recruitment to the activated human receptor
  is measurable directly [PMID:24692546, PathHunter assay]; in rat primary Sertoli cells
  GRK2 and beta-arrestin 1/2 are recruited to the endogenous receptor [PMID:16899567].
- Adaptors bound by the cytoplasmic face: 14-3-3tau/YWHAQ ("Importantly, 14-3-3tau
  co-immunoprecipitated with FSHR stably expressed in HEK 293 cells. Its association with
  FSHR was follitropin-dependent" [PMID:15196694]), APPL1/APPL2/FOXO1a ("This report
  shows that, in addition to APPL1, FSHR interacts with FOXO1a and APPL2"
  [PMID:17030088]), and the 14-3-3 site overlaps the canonical G-protein site
  [PMID:20600589]. These are interactions, not a molecular function of FSHR, so they do
  not license a more informative MF term than `protein binding` here.

## 4. Oligomeric state — unresolved

- The isolated ectodomain crystallises as a dimer [PMID:15662415: "The FSH-FSHR(HB)
  complexes form dimers in the crystal and at high concentrations in solution"] and, with
  the hinge included, as a trimer [PMID:22802634: "a potential exosite resulting from
  putative receptor trimerization"]. Jiang et al. built a functional trimer model and
  tested its predictions pharmacologically [PMID:24692546].
- The full-length cryo-EM structures contradict a signalling trimer: "The full-length
  FSHR structures we solved in the active and inactive states were both in monomeric
  states" and "the presence of FSH and Gs protein would prevent receptor dimerization or
  trimerization in the same convex membrane layer (Supplementary Fig. 5a, b) as observed
  in the crystal structures" [PMID:36720854].
- So the GO:0043235 `signaling receptor complex` row (IDA, PMID:24692546) rests on a
  claim the later structures dispute. Kept as non-core: the ligand-bound FSHR-Gs assembly
  is real, the homotrimer is not established in a membrane.

## 5. Where it acts

- Plasma membrane, ectodomain out: cell-surface FSH-binding sites on the human receptor
  [PMID:1322283]; UniProt records "SUBCELLULAR LOCATION: Cell membrane" and
  "Multi-pass membrane protein" [file:human/FSHR/FSHR-uniprot.txt CC SUBCELLULAR LOCATION,
  citing PMID:11847099 and PMID:24692546].
- Endosomes after agonist-driven internalisation, with recycling: "the majority of the
  internalized FSH-FSHR complex accumulates in endosomes and subsequently recycles back
  to the cell surface", detected "in heterologous (human kidney 293T) cells transfected
  with the rat (r) or human (h) FSHR" [PMID:12907758]; the human receptor internalises
  into small APPL1-type endosomes in HEK293 [PMID:24375413: "Targeting receptors to these
  small endosomes was not a specific feature of the LHR because both the FSHR and B1AR
  also internalized to endosomes with a similar physical profile"].
- Note on participation: being internalised and recycled, or carried across an
  endothelium, is something done *to* the receptor by the trafficking machinery. That is
  not participation in the sense GO `involved_in` requires, so no NEW receptor-recycling
  row was proposed; the endosome location row carries the fact.

## 6. Physiology and human genetics

- Loss of function causes hypergonadotropic ovarian dysgenesis (ODG1, MIM:233300).
  "A C566T transition in exon 7 of FSHR predicting an Ala to Val substitution at residue
  189 in the extracellular ligand-binding domain segregated perfectly with the disease
  phenotype" and "Expression of the gene in transfected cells demonstrated a dramatic
  reduction of binding capacity and signal transduction, but apparently normal
  ligand-binding affinity of the mutated receptor" [PMID:7553856].
- Males homozygous for the same allele are subfertile rather than azoospermic: "They have
  variable degrees of spermatogenic failure, but, surprisingly, do not show azoospermia
  or absolute infertility" [PMID:9020851]. The same paper states the female conclusion:
  "Hence, lack of FSH function is incompatible with ovarian follicular maturation and
  female fertility."
- Mouse knockouts agree and localise the block: "FSH-R-deficient females display thin
  uteri and small ovaries and are sterile because of a block in folliculogenesis before
  antral follicle formation" while "FSH-R-deficient males are fertile but display small
  testes and partial spermatogenic failure" [PMID:9811848]; "In conclusion, ovarian
  follicular development cannot progress beyond the preantral stage without FSH"
  [PMID:10803590].
- Gain of function / loss of ligand selectivity causes spontaneous ovarian
  hyperstimulation syndrome (OHSS, MIM:608115) [file:human/FSHR/FSHR-uniprot.txt CC
  DISEASE, citing PMID:12930927 among others]. The M512I variant in PMID:24058690 was
  found in a sOHSS patient but is hypoactive, not activating: "This mutant appears to be
  inactive in that it inhibited FSH-induced cAMP production and PI3K activation."
- So the asymmetry matters for term choice: the ovarian claim is follicle-level
  (GO:0001541) and well supported; the testicular claim is support of spermatogenic
  efficiency via Sertoli cells, which is real but neither essential nor executed by the
  receptor-bearing cell's own gametogenesis.

## 7. Extragonadal claims — treated as non-core or over-annotation

- Bone. "Neither FSHbeta nor FSH receptor (FSHR) null mice have bone loss despite severe
  hypogonadism" and "Osteoclasts and their precursors possess G(i2alpha)-coupled FSHRs
  that activate MEK/Erk, NF-kappaB, and Akt to result in enhanced osteoclast formation
  and function" [PMID:16630814]. A systematic critique finds the expression evidence
  weak: "Firstly, protein expression of FSHR was performed solely with
  immunohistochemistry (IHC) using either an unavailable "in house" FSHR323 monoclonal
  antibody or poorly validated polyclonal antibodies, usually without additional
  methodological quality control and confirmations" and "Taken together, further studies
  are needed to determine whether the FSH-FSHR system action in bone resorption is really
  functional, only species-specific, a probable indirect effect of inflammatory cytokines
  such as tumor necrosis factor α (TNF-α) (69) or an unidentified off-target
  effect of the FSH antibodies used" [PMID:30778333]. GOA carries no bone term for human
  FSHR and none was proposed here; recorded as a knowledge gap and a suggested
  experiment instead.
- Pancreatic islets. Mouse Fshr knockout impairs glucose-stimulated insulin secretion
  [PMID:37914684: "Blocking FSH signaling by Fshr knock-out led to impaired glucose
  tolerance owing to decreased insulin secretion, while high FSH levels caused
  insufficient insulin secretion as well"], and the paper reports FSHR in human islets.
  The human GO row is an Ensembl Compara projection of the mouse IMP, so it asserts for
  human what only mouse genetics shows: marked as over-annotation.
- Transcytosis. Receptor-mediated FSH transcytosis was shown across *rat* testicular
  endothelium [PMID:15050368]; no human data, and endothelial FSHR identity is part of
  the contested set [PMID:30778333]. Marked as over-annotation.

## 8. Term-choice decisions worth recording

- `GO:0008528 G protein-coupled peptide receptor activity` (IBA from PTN000689980, seeded
  by Drosophila rk and rat Lhcgr) is in the wrong branch for this receptor: GO files
  `GO:0004963` under `GO:0016500 protein-hormone receptor activity` (checked in OLS), not
  under the peptide-receptor branch, and FSH is a heterodimeric glycoprotein. Modified to
  `GO:0004963`, which the gene already carries.
- `GO:0004963` lacks the `GO:0004930 G protein-coupled receptor activity` parent that its
  two siblings `GO:0004964 luteinizing hormone receptor activity` and `GO:0004996
  thyroid-stimulating hormone receptor activity` both carry (OLS, 2026-11-13). The
  InterPro IEA row for `GO:0004930` is therefore *not* redundant with the FSHR activity
  rows, and was accepted rather than called too general; an `EDGE_CREATION` request is
  recorded in `proposed_ontology_changes`.
- `GO:0042699 follicle-stimulating hormone signaling pathway` is `part_of GO:0001541
  ovarian follicle development` in GO (OLS, 2026-11-13). That makes every FSH-signalling
  annotation entail ovarian follicle development, which is false for Sertoli cells — the
  receptor and the pathway both operate in the testis. An `EDGE_DELETION` request is
  recorded.
- `GO:0009755 hormone-mediated signaling pathway` is *not* an ancestor of `GO:0042699`
  (GO:0042699's parents are `GO:0007186` and `GO:0022602`), so it is not redundant and
  was accepted.

## 9. Isoforms

Four UniProt isoforms: Long/R1 (displayed), Short (E9Del), 3 (E6Del), 4 (E8'Inc). A
review of FSH biology states that "FSHR1 transcript contains all the ten exons and is
known as the major isoform that actively participates in steroidogenesis, follicular
development, and spermatogenesis" [PMID:35002517]. No GOA row is isoform-scoped, and the
shorter forms lack transmembrane exons, so no isoform-specific annotation was made.
