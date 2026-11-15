# KISS1 (KiSS-1, kisspeptin precursor, metastin) — curation notes

UniProt Q15726. Human 138-aa secreted precursor (signal peptide 1-19), PANTHER PTHR16955
(METASTASIS-SUPPRESSOR KISS-1, subfamily SF6), InterPro IPR020207, Pfam PF15152 (Kisspeptin).
Every primary claim below traces to a cached publication, the cached UniProt record, or a
cached Reactome entry.

## Identity

Unambiguous symbol. KISS1 is the **ligand** gene; KISS1R (GPR54/AXOR12/hOT7T175, Q969F8) is the
receptor and a separate locus — much of the kisspeptin disease and signalling literature is about
the receptor, so each claim has to be assigned to the right side. The receptor was reviewed
separately in this repository (`genes/human/KISS1R/`); its core MF is `GO:0008188` neuropeptide
receptor activity.

## Gene product: a precursor of several RF-amide peptides

UniProt records four processed peptides inside the 138-aa precursor: Metastin/kisspeptin-54
(68-121), kisspeptin-14 (108-121), kisspeptin-13 (109-121) and kisspeptin-10 (112-121), with
`MOD_RES 121 Phenylalanine amide` (ECO:0000269|PubMed:11385580) and
`REGION 112..121 /note="Essential for receptor binding and receptor activation"`.

Ohtaki purified the active species from human placenta: KiSS-1 "encodes a carboxy-terminally
amidated peptide with 54 amino-acid residues, which we have isolated from human placenta as the
endogenous ligand of an orphan G-protein-coupled receptor (hOT7T175) and have named 'metastin'"
[PMID:11385580]. Kotani independently isolated the 54-, 14- and 13-residue forms and named them
kisspeptins: "These 54-, 14,- and 13-amino acid peptides, with a common RF-amide C terminus,
derive from the product of KiSS-1, a metastasis suppressor gene for melanoma cells, and were
therefore designated kisspeptins" [PMID:11457843]. Wu's 2024 structural paper states the
pharmacophore plainly: "Kisspeptins belong to RF amide peptides because of the specific C-terminal
domain that required for binding and activating KISS1R" [PMID:39151001].

**Processing enzymes are not the gene's own function.** The dibasic-site cleavages and the
C-terminal amidation are done by other gene products (prohormone convertases, PAM); KISS1 is the
substrate. By the participation rule, KISS1 must not carry a peptide-hormone-processing process
term. The one processing step with a named enzyme set in UniProt is MMP cleavage, which *destroys*
activity: "Active MMP-2, MMP-9, MT1-MMP, MT3-MMP and MT5-MMP cleaved the Gly118-Leu119 peptide
bond of not only full-length KiSS-1 protein but also metastin decapeptide" and "digestion of
metastin decapeptide by MMP abolished its ligand activity" [PMID:12879005].

## Molecular function: KISS1R agonist

Three groups deorphanised GPR54 with KiSS-1-derived peptides in 2001.
- Kotani: the peptides "bound with low nanomolar affinities to rat and human GPR54 expressed in
  Chinese hamster ovary K1 cells and stimulated PIP(2) hydrolysis, Ca(2+) mobilization,
  arachidonic acid release, ERK1/2 and p38 MAP kinase phosphorylation, and stress fiber formation
  but inhibited cell proliferation" [PMID:11457843]. This is direct evidence, on the **human**
  receptor, that the human peptides are agonists that drive a PLC-activating GPCR pathway.
- Muir (AXOR12): "High potency agonism, indicative of a cognate ligand, was evident from peptides
  derived from the gene KiSS-1" [PMID:11387329]. Highest KiSS-1 expression "in placenta and
  brain"; the receptor in "brain, pituitary gland, and placenta".
- Ohtaki (metastin/hOT7T175) [PMID:11385580], above.

So on the ligand side the molecular activity is receptor-ligand/hormone activity, and the
receptor activity belongs to KISS1R. GO's own records agree: the two cached GO-CAMs
(`gocams/68d5ebd600001111`, `gocams/68d5ebd600001504`) give the human kisspeptin-10 chain
`GO:0048018 receptor ligand activity`, `occurs_in GO:0005576`, `part_of GO:0007200`, with
`GO:0004930` on KISS1R; mouse (Q6Y4S4) and rat (Q7TSB7) Kiss1 also carry `GO:0048018` by ISO.
Human Q15726 itself has **no** ligand/hormone MF row — only `GO:0031773 kisspeptin receptor
binding` (IBA) and two bare `GO:0005515` rows. That is the gap this review fills.

Which ligand MF? Checked in OLS: `GO:0005184` neuropeptide hormone activity is_a `GO:0005179`
hormone activity (and `GO:0160041` neuropeptide activity), and `GO:0005179` is_a `GO:0048018`
receptor ligand activity. `GO:0005184` is defined as "any peptide hormone that acts in the central
nervous system". Comparators in the same class: OXT (P01178) carries `GO:0005184` (IBA); GNRH1
(P01148) carries `GO:0005179` + `GO:0005183`; TAC3 (Q9UHF0) carries `GO:0048018` (IDA); PDYN
carries `GO:0001515` opioid peptide activity. So a ligand/hormone MF is the convention for this
class of gene and its absence on human KISS1 is a gap.

The review proposes the parent, `GO:0048018`, not `GO:0005184`, for three reasons. This gene
product acts in three modes — CNS neuropeptide on GnRH neurons, circulating placenta-derived
hormone, and local paracrine ligand on neighbouring trophoblast — and only the parent is true of
all three; the placenta, not the brain, is the highest-expressing human tissue; and `GO:0048018`
is the term GO itself already uses for this protein, on the kisspeptin-10 chain in both cached
GO-CAMs and in the mouse and rat ISO rows that name human KISS1 as donor. `GO:0005184` is a
defensible refinement for the hypothalamic arm (human infundibular KISS1 neurons, Rometo;
kisspeptin-54 infusion driving the human axis, Dhillo) and is raised as a suggested question
rather than asserted.

## Where it acts: extracellular

Secreted. UniProt `SUBCELLULAR LOCATION: Secreted {ECO:0000269|PubMed:15020672}`. Bilban detected
the peptide in trophoblast secretions: "We identified Kp-10, a dekapeptide derived from the
primary translation product, in conditioned medium of first trimester human trophoblast"
[PMID:15020672]. Horikoshi measured it in plasma and localised the source: "Histochemical studies
of human placenta localized metastin mRNA and immunoreactivity to the syncytiotrophoblasts", with
plasma immunoreactive metastin rising from ~1.3 fmol/ml outside pregnancy to 9590 +/- 1640
fmol/ml in the third trimester, concluding "evidence for metastin as a novel placenta-derived
hormone in humans" [PMID:12574233]. The target receptor is on the plasma membrane of the
responding cell, which is why the ligand's location is the extracellular region and not the
membrane.

## Human sites of expression

Placenta highest (UniProt TISSUE SPECIFICITY; PMID:8944003 northern blots; PMID:11387329 qRT-PCR).
Human hypothalamus: Rometo mapped KISS1 transcripts in human autopsy tissue — "Examination of
human hypothalamic sections revealed that KiSS-1 neurons were located predominantly in the
infundibular nucleus", with hypertrophy and increased KISS1 expression after loss of ovarian
steroids in women and in ovariectomised monkeys, reversed by estrogen [PMID:17488799]. This is the
human evidence that KISS1 is expressed by CNS neurons, which the `GO:0005184` reading needs.

## Physiology

**Reproductive axis (core).** Human loss of function: "We describe an inactivating mutation in
KISS1 in a large consanguineous family that results in failure of pubertal progression, indicating
that functional kisspeptin is important for puberty and reproduction in humans" [PMID:22335740];
UniProt records the variant as HH13 N115K with "severely decreased receptor ligand activity".
Human pharmacology: "Kisspeptin-54 infusion significantly increased plasma LH, FSH, and
testosterone concentrations compared with saline infusion" in male volunteers [PMID:16174713].
Rat: metastin given s.c. "increased the plasma levels of gonadotropins (follicle-stimulating
hormone and luteinizing hormone) and induced ovulation", and crucially "This action was abolished
by pretreatment with a GnRH antagonist, and was accompanied by induction of c-Fos immunoreactivity
in GnRH neurons" [PMID:15219839] — i.e. the ligand acts on GnRH neurons and the gonadotropin rise
is downstream of GnRH. UniProt CC FUNCTION states the same mechanism with ECO:0000269 evidence.

Note on term choice: GO has **no** term for GnRH secretion or its regulation (checked in OLS:
only `GO:0097210` response to GnRH, `GO:0032274` gonadotropin secretion and the GnRH-neuron
development terms). The proximal claim therefore cannot be annotated; the available terms are
`GO:0033686` positive regulation of luteinizing hormone secretion (the existing IBA row) and its
parent `GO:0032278`. Since `GO:0033686` is a descendant of `GO:0032278` (OLS ancestor check), a
parent row would be redundant and is not proposed — even though kisspeptin raises FSH as well as
LH.

Mechanistically the receptor cell does the work: Gq/PLC/Ca2+ in GnRH neurons, plus a
beta-arrestin arm — "we conclude that KISS1R signals via Gaq/11 and beta-arrestin to regulate
GnRH secretion" [PMID:25147978]. Those are KISS1R's rows, not KISS1's.

**Placenta.** Kp-10 is made by villous trophoblast and restrains invasion of the neighbouring
extravillous trophoblast: "Kp-10 inhibited trophoblast migration in an explant as well as transwell
assay without affecting proliferation", with suppressed gelatinolytic activity [PMID:15020672].

**Anti-metastatic / anti-motility (the original description).** KiSS-1 was found by subtractive
hybridisation in chromosome-6-complemented melanoma cells; re-expression "suppressed metastasis in
an expression-dependent manner" without affecting tumorigenicity [PMID:8944003], and the same held
in a breast carcinoma line [PMID:9192814]. Mechanistically this is receptor-dependent in every
assay that tested it: metastin acts on hOT7T175-transfected cells [PMID:11385580], "Metastin
significantly suppressed motility in a chemotaxis assay and wound healing assay at 10-100 nM order
concentrations" in CHO cells transfected with the receptor [PMID:11527393], and GPR54 stimulation
by kisspeptin-10 "promoted apoptosis while no significant change was observed after B(2) receptor
activation" [PMID:15596153]. So the metastasis-suppressor phenotype is the ligand acting through
KISS1R, not a receptor-independent intracellular activity.

**Bone.** Mouse Kiss1/Gpr54 with human giant-cell-tumour osteoclast confirmation underlies the
`GO:0045779` ISS row [PMID:38346942]; peripheral to the gene's core role and kept as non-core,
matching the KISS1R review.

## The cytoskeleton row

`GO:0007010 cytoskeleton organization` is a legacy ProtInc TAS from Lee & Welch 1997. That paper
reports the opposite of a motility phenotype — "Invasion and motility were unaffected by KiSS-1" —
and offers the cytoskeletal mechanism as speculation from the *predicted* intracellular structure
of the protein (a polyproline SH3-ligand domain): "Based on the predicted structure of the KiSS-1
protein, our results imply a mechanism whereby KiSS-1 regulates events downstream of cell-matrix
adhesion, perhaps involving cytoskeletal reorganization" [PMID:9192814]. The predicted
intracellular SH3-ligand mechanism was superseded in 2001 when the gene product turned out to be a
secreted peptide hormone acting on a GPCR. Actin effects are real but are executed by the
receptor-bearing cell: "Metastin decapeptide induced formation of focal adhesion and actin stress
fibers in cells expressing the receptor" [PMID:12879005]; Kotani saw stress-fibre formation in
GPR54-expressing CHO cells [PMID:11457843]. Marked as over-annotated rather than removed: the
downstream effect exists, but the ligand does not organise the cytoskeleton.

## Decisions

- `GO:0031773` kisspeptin receptor binding (IBA): ACCEPT, core. Human affinity data in Kotani.
- `GO:0005576` extracellular region (EXP, IBA, IEA, 4x Reactome TAS): ACCEPT, core location.
- `GO:0007186` GPCR signalling pathway (IBA): MODIFY to `GO:0007200` (human IDA in Kotani) and
  `GO:0007218` (neuropeptide signalling pathway); both are supported descendants, siblings of each
  other, and the same two terms used on the receptor side.
- `GO:0033686` positive regulation of LH secretion (IBA): ACCEPT, core physiology.
- `GO:0045779` negative regulation of bone resorption (ISS from mouse): KEEP_AS_NON_CORE.
- `GO:0007010` cytoskeleton organization (TAS): MARK_AS_OVER_ANNOTATED.
- `GO:0005515` with Q969F8 (KISS1R, Muir): MODIFY to `GO:0031773`.
- `GO:0005515` with Q9UHD9 (UBQLN2, HuRI): REMOVE under the protein-binding policy.
- NEW `GO:0048018` receptor ligand activity: the missing ligand MF (agonism, as distinct from the
  binding already annotated), at the level true of all three modes of action.

## Ontology and knowledge gaps

- GO has no kisspeptin receptor signalling pathway term, although `GO:0007217` (tachykinin) and
  `GO:0090663` (galanin, the one existing child of `GO:0007218`) set the precedent. Proposed in the
  review.
- Which convertase(s) cut the human precursor, and whether hypothalamic neurons and
  syncytiotrophoblast make the same mix of KP-54/-14/-13/-10, is not established in the cited
  literature; the peptide forms differ in half-life, so this determines what reaches each receptor
  pool. A genuine wet-lab gap.
- What the thousand-fold pregnancy rise in circulating metastin does, given that KISS1R
  desensitises, is unresolved: Horikoshi establishes the concentrations but not a target.
