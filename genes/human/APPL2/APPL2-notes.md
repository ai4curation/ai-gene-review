# APPL2 (DIP13B, Q8NEU8) — curation notes

Human APPL2, "DCC-interacting protein 13-beta" (`DP13B_HUMAN`), 664 aa, HGNC:18242.
Reviewed here against the UniProt record, the 126-row GOA table, the PANTHER PTHR46415
PAINT slice, and the primary literature.

## 0. No affinage deep-research record exists for this gene

The affinage prefetch **refused to write** `APPL2-deep-research-affinage.md`. The log
(`.affinage.log` in the worktree root) records a blocking trust gate:

> `[BLOCKING] Accession mismatch: local review uses 'Q8NEU8' but the Affinage record's
> prefetch UniProt accession is 'Q06481'.`

Q06481 is **APLP2**, amyloid-beta precursor-like protein 2, which carries "APPL2" as a
legacy alias. The Affinage API returned the record for the wrong protein and the
wrong-protein gate correctly blocked the write. There is therefore no deep-research file
to cite, and everything below comes from UniProt, GOA, PANTHER/PAINT and papers I
retrieved and read myself. The same collision has to be filtered out of every literature
search: a PubMed query on the bare string `APPL2` returns amyloid-precursor-family papers
that have nothing to do with this gene. All 59 `APPL2[tiab]` hits were triaged by title;
the adaptor-protein papers are the ones used below. (`DIP13B` as a search term returns
zero PubMed records, so it is useless as a disambiguator.)

Europe PMC REST was unavailable during this review; searches were run through NCBI
E-utilities (`esearch`/`esummary`) instead.

## 1. What the protein is

APPL2 is one of two mammalian BAR-PH-PTB adaptors, the other being APPL1. UniProt assigns
the domains as BAR 3-268, PH 277-375, PID(PTB) 488-637, with a disordered C-terminal tail
(643-664) and no catalytic residues of any kind — it is a scaffold, not an enzyme
[file:human/APPL2/APPL2-uniprot.txt "DOMAIN 3..268 /note="BAR""]. Two crystal structures
exist, both of the N-terminal half: 4H8S (residues 2-384) and 5C5B (1-375).

I measured the sequence relationships directly rather than repeating numbers from reviews
(`APPL2-bioinformatics/appl_orthology.py`, live UniProt fetch, lengths asserted):

- human APPL2 vs mouse Appl2 (Q8K3G9): **92.7%** identity, 614/662 aligned columns
- human APPL1 vs mouse Appl1: 98.3%
- human APPL2 vs human APPL1: **53.9%** (matching the "52% by ClustalW" of
  [PMID:23055524 "share 52% sequence identity by ClustalW pair-wise alignment"])

That pair of numbers sets up the whole review. The mouse-to-human transfer is safe — the
orthology is 1:1 and 93% identical, so the 24 ISS rows and 19 orthology-based IEA rows do
not carry an ortholog-assignment risk. The paralog relationship is not safe: at 54%
identity APPL1 and APPL2 share an architecture and heterodimerise, but they have different
Rab partners, opposite signs in adiponectin signalling, and a documented difference in Akt2
binding. **An experiment that removes both therefore establishes nothing about either.**

## 2. The PANTHER family and what PAINT actually did

`DR PANTHER; PTHR46415; ... ; PTHR46415:SF1; DCC-INTERACTING PROTEIN 13-BETA`. The family
is small and clean: `interpro/panther/PTHR46415/PTHR46415-entries.csv` lists five reviewed
members — human/mouse/rat APPL2 in subfamily **SF1**, human/mouse APPL1 in subfamily
**SF3**.

The PAINT slice (`PTHR46415-paint.tsv`, fetched with `just fetch-panther-paint`) has
exactly **two nodes and four IBD annotations**, and the way they are placed is the single
most informative thing in this review:

| node | taxon | term | aspect | seeds |
|---|---|---|---|---|
| PTN000572460 | 33213 Bilateria | GO:0010008 endosome membrane | C | MGI:MGI:1920243 (mouse Appl1), UniProtKB:Q8NEU8 (human APPL2), UniProtKB:Q9UKG1 (human APPL1) |
| PTN000572460 | 33213 Bilateria | GO:0023052 signaling | P | MGI:MGI:2384914 (mouse Appl2), UniProtKB:Q8NEU8, UniProtKB:Q9UKG1 |
| PTN008708200 | 32523 Tetrapoda | GO:0043422 protein kinase B binding | F | UniProtKB:Q9UKG1 (human APPL1) |
| PTN008708200 | 32523 Tetrapoda | GO:0008286 insulin receptor signaling pathway | P | UniProtKB:Q9UKG1 |

(Taxon ids resolved via the UniProt taxonomy REST service: 33213 = Bilateria, 32523 =
Tetrapoda. MGI ids resolved through UniProt `xref:mgi-…`: MGI:2384914 → Q8K3G9 mouse Appl2,
MGI:1920243 → Q8K3H0 mouse Appl1; both returned the reviewed Swiss-Prot entry at the head of
a multi-hit list of TrEMBL isoforms, so `size=5` was used and the reviewed entry taken.)

PTN000572460 sits at Bilateria, **above the APPL1/APPL2 duplication**, so both IBAs on
APPL2 descend from a node whose seeds include both paralogs. PTN008708200 sits at
Tetrapoda inside the APPL1 (SF3) lineage, and APPL2 is **not** a descendant of it — which
is why APPL2 receives no IBA for protein kinase B binding or insulin receptor signalling.

That restraint is correct, and there is direct human evidence for it:
[PMID:17030088 "Though APPL1 and APPL2 show some similarity in primary sequence, APPL1
associates with Akt2, whereas APPL2 does not. This is the first documented difference in
function between APPL1 and APPL2."] A PAINT curator who had placed AKT binding at the
Bilateria node would have produced a false APPL2 annotation; placing it one node down
avoided that. This is worth recording as a case where the phylogenetic judgment behind an
IBD was made at the right depth.

The consequence for the `GO:0023052 signaling` IBA is the one that is easy to get backwards.
"Signaling" is a very high-level term, and the reflex is to call that a granularity
mismatch. It is not. The node's seeds are APPL1 and APPL2, and their signalling roles
**disagree in sign** — APPL1 potentiates adiponectin/Akt signalling, APPL2 antagonises it
(§3). Any child term specific enough to be informative would be wrong for one of the two
seeds. The generic parent is the honest least common ancestor, so this is
`NO_FAILURE_NON_CORE` with no failure mode, not `GRANULARITY_MISMATCH`.

Both IBA rows carry `UniProtKB:Q8NEU8` — the target's own accession — in their WITH/FROM.
That is expected and correct: APPL2 has its own experimental annotations for endosome
membrane (two IDA rows, PMID:21645192 and PMID:15016378, plus an EXP row for early endosome
membrane), and those descendant evidences are part of what the PAINT curator used to place
the IBD. It is a marker that experimental grounding exists on the target itself, not
circularity.

## 3. The adiponectin literature and the sign-inversion trap

This is the flagged risk for this gene, and it resolves cleanly.

APPL2 is a **negative** regulator of adiponectin signalling, the mirror image of APPL1:
[PMID:19661063 "APPL2, an isoform of APPL1 that forms a dimer with APPL1, can interacts
with both AdipoR1 and AdipoR2 and acts as a negative regulator of adiponectin signaling in
muscle cells"], and mechanistically [PMID:19661063 "In addition to targeting directly to
and competing with APPL1 in binding with the adiponectin receptors, APPL2 also suppresses
adiponectin and insulin signaling by sequestrating APPL1 from these two pathways"]. The
perturbation runs in both directions: overexpression inhibits the APPL1-AdipoR1 interaction
and down-regulates signalling, while [PMID:19661063 "suppressing APPL2 expression by RNAi
significantly enhances adiponectin-stimulated glucose uptake and fatty acid oxidation"].

The transferred term is `GO:0033211 adiponectin-activated signaling pathway`, which is
**sign-neutral** — "The series of molecular signals initiated by adiponectin binding to its
receptor…". Involvement in the pathway is exactly what the mouse data support, and no sign
is asserted, so there is no regulatory-sign inversion in the ISS/IEA transfer. The rows that
*do* carry a sign — `GO:0046322 negative regulation of fatty acid oxidation` and
`GO:1900077 negative regulation of cellular response to insulin stimulus` — carry the
**correct** sign, the one the RNAi direction establishes.

I checked whether GO offers a signed child that would be more informative. It does not:
a QuickGO ontology search for "regulation of adiponectin" returns only the
secretion branch (GO:0070163/0070164/0070165), `GO:0055100 adiponectin binding` and
`GO:0033211` itself. There is no "negative regulation of adiponectin-activated signaling
pathway" term. This is a genuine ontology gap and is recorded in `proposed_new_terms`; it
is the reason APPL2's best-characterised metabolic function has to be carried by a neutral
parent rather than stated outright.

## 4. Rab effector status and compartment specificity

APPL1 and APPL2 were identified together as Rab5 effectors on a distinct endosome
subpopulation [PMID:15016378 "This pathway operates via APPL1 and APPL2, two Rab5
effectors, which reside on a subpopulation of endosomes"]. The compartment is a real
subpopulation of early endosomes, not a separate organelle:
[PMID:21645192 "APPL endosomes are a recently identified subpopulation of early endosomes
characterized by the presence of two homologous Rab5 effector proteins APPL1 and APPL2.
They exhibit only limited colocalization with EEA1, another Rab5 effector and a marker of
the canonical early endosomes."]

**There is no GO term for "APPL endosome."** GO's available compartments are
`GO:0010008 endosome membrane` (the IBA and two IDAs) and `GO:0031901 early endosome
membrane` (the EXP row and a SubCell IEA). Since APPL endosomes are by the authors' own
definition a subpopulation of early endosomes, both terms are true statements about APPL2
and neither over-reaches; the more specific one is supported by the original Zerial
characterisation. So the "APPL endosome vs early endosome" question does not produce a
correction here — it produces a `proposed_new_terms` entry.

APPL2's Rab repertoire is **not** APPL1's, which matters for how the protein-binding rows
should be re-termed. A yeast two-hybrid screen against 46 Rabs found
[PMID:23055524 "For APPL2, the yeast two-hybrid screen revealed interactions with Rabs 5,
22a, 24, and 31"] and [PMID:23055524 "APPL2 did not bind the APPL1 partners Rab21 and none
of the novel APPL2-interacting Rabs were found to interact with APPL1."] The Rab31
interaction was then measured: [PMID:23055524 "ITC and found that two Rab31 molecules bind
one hAPPL2 BARPH dimer ( n = 0.98 ± 0.01) with a binding affinity, K d , of 140 ± 30 n m"].
In macrophages the same pairing is seen at the protein level, with a direct GTP preference
[PMID:25568335 "Moreover, APPL2 showed a preference for binding to GTP-loaded Rab31
compared with its GDP-bound form (Figure 5A)."] and a threefold preference over Rab5a.

So the four GOA `protein binding` IPI rows whose partners are RAB5A, RAB5C, RAB22A and
RAB31 are all instances of one informative molecular function. The current term for it is
`GO:0031267 small GTPase binding` — I checked QuickGO, and **GO:0017137 "Rab GTPase
binding" is not a live term: it appears in GO:0031267's `secondaryIds` list, i.e. it was
merged into small GTPase binding**, not obsoleted without replacement. GO:0031267 is the id
to use.

A compartment caveat worth recording: in macrophages APPL2 is *not* on endosomes.
[PMID:25568335 "This contrasts with the predominant and stronger labeling of
mCherry-APPL2 on phagosomes and its general absence from endosomes (Figure 7A)."] The
endosomal localisation is real but cell-type dependent, which is consistent with UniProt's
own "Absent of endosome in macrophage" note.

## 5. Where the sole-source experiments actually are

I went through every paper behind a functional row and asked whether APPL2 was perturbed on
its own. The answers split three ways.

**APPL2-specific perturbation exists (rows are sound):**

- *Insulin-stimulated glucose uptake / GLUT4.* Both directions, plus a tissue-specific
  knockout: [PMID:24879834 "insulin-evoked plasma membrane recruitment of GLUT4 and glucose
  uptake are impaired by APPL2 overexpression but enhanced by APPL2 knockdown. Likewise,
  conditional deletion of APPL2 in skeletal muscles enhances insulin sensitivity, leading to
  an improvement in glucose tolerance."] and the mechanism is a specific, mapped interaction:
  [PMID:24879834 "Insulin stimulates TBC1D1 phosphorylation on serine 235, leading to
  enhanced interaction with the BAR domain of APPL2, which in turn suppresses insulin-evoked
  TBC1D1 phosphorylation on threonine 596"]. This is the best-evidenced single function of
  the gene.
- *FcγR-mediated phagocytosis.* APPL2 siRNA alone: [PMID:25568335 "siRNA depletion of either
  Rab31 or APPL2 reduces FcγR-mediated phagocytosis"], with localisation to match
  [PMID:25568335 "APPL2 was immunolabeled in the cytoplasm, on cell surface ruffles, and on
  early, actin-rich phagosomes (Figure 5, C and D)"].
- *Innate immune restraint.* An Appl2 knockout mouse: [PMID:25328665 "When challenged with
  lipopolysaccharides (LPS), Appl2 KO mice exhibited more severe symptoms of endotoxin shock,
  accompanied by increased production of proinflammatory cytokines."]
- *TLR4 signalling / cytokine output.* Single-adaptor depletions:
  [PMID:27219021 "By depleting cells of each adaptor respectively we show separate and
  opposing functions for APPL1 and 2 in Akt and MAPK signaling. Specifically, APPL2 has a
  dominant role in nuclear translocation of NF-KB p65 and it serves to constrain the
  secretion of pro- and anti-inflammatory cytokines."]
- *Adaptive thermogenesis.* A conditional, neuron-restricted deletion:
  [PMID:29467283 "Genetic ablation of APPL2 in RIP-Cre neurons diminishes beiging in sWAT
  without affecting BAT, leading to cold intolerance and obesity in mice."]
- *HGF response and fibroblast migration.* I initially read this as a double-knockout-only
  result from the title, and it is not: [PMID:26445298 "Interestingly, Appl1 KO, Appl2 KO,
  and especially Appl1/2 DKO MEFs showed consistently decreased Akt activation upon
  stimulation with HGF (Fig."] The single Appl2 KO has the phenotype. The migration and
  invasion assays are reported for "Appl-deficient MEFs" collectively, so the Akt result is
  the APPL2-specific anchor and the migration row inherits a little of the ambiguity.

**Perturbation is APPL1+APPL2 together (rows keep a caveat):**

- *TGFβ receptor signalling and nuclear transport of TβRI-ICD.* Every functional experiment
  in this paper silences both adaptors at once — "siRNA-mediated silencing of APPL1 and
  APPL2", "treated, or not, with APPL1 and APPL2 siRNA" — and the physical interaction work
  is on APPL1 alone: [PMID:26583432 "In this report, we identify APPL1 as a TβRI- and PKCζ-
  associated protein and show that APPL1 and APPL2 are required for the nuclear translocation
  of TβRI-ICD, and thereby promote progression of prostate cancer cells."] APPL2's individual
  contribution is unresolved. The gene is genuinely required in combination, so this is not a
  removal — but it is not a core function either. Both the `GO:0007179` IMP and the
  `GO:0006606` IDA rest on this design.

**Gain-of-function-weighted (rows keep a caveat):**

- *Neurogenesis.* The in vivo evidence is an APPL2 **transgenic overexpression** mouse, not a
  loss-of-function: [PMID:28965332 "APPL2 Tg mice had decreased hippocampal neurogenesis that
  was reversed by GR antagonist RU486."] A matching loss-of-function exists only in vitro:
  [PMID:32468397 "APPL2 overexpression resulted in NSCs switching from neuronal
  differentiation to gliogenesis while APPL2 knockdown promoted neurogenesis."] Both
  directions therefore exist, but the animal-level claim is driven by overexpression.

## 6. A homotetramer that the paper does not report

`GO:0051289 protein homotetramerization` is annotated IDA to PMID:23055524, and UniProt
likewise states "Homotetramer (PubMed:23055524)". The word "tetramer" does not occur
anywhere in the full text of that paper. What the paper reports is a crystallographic
observation — [PMID:23055524 "hAPPL2 BARPH crystallized in the P 2 1 2 1 2 1 space group
with two dimers in the asymmetric unit."] — and every solution measurement it makes says
**dimer**: [PMID:23055524 "Chemical cross-linking performed using bis(sulfosuccinimidyl)
suberate suggested that hAPPL2 BARPH is predominantly a dimer in solution (data not
shown)."] and, by light scattering, [PMID:23055524 "95.1 kDa ± 2.0% for hAPPL2 BARPH
(theoretical mass of 92.1 for dimer)"]. Two dimers in an asymmetric unit is a statement
about crystal packing, not about the assembly state of the protein.

The only tetramer in the paper is a **hetero**tetramer with the Rab: "the formation of a
complex comprising an hAPPL2 BARPH dimer and two Rab31-Gpp(NH)p monomers", which is not
homotetramerization either. The row is therefore a misreading of the asymmetric unit, and
the well-supported claim in its place is homodimerization — which is independently
established by two methods in a different paper [PMID:18034774 "Results of these experiments
demonstrated that the APPL minimal BAR domains were necessary and sufficient for mediating
APPL1-APPL1, APPL2-APPL2 and APPL1-APPL2 interactions in the yeast two-hybrid system"] and
already annotated as `GO:0042803` and `GO:0042802`. I propose `GO:0051260 protein
homooligomerization` as the replacement rather than deleting the row, since the BAR domain
does oligomerize and the paper's own conclusion is a defined dimer.

Note this row is the one place where I am overruling both a curator and UniProt. I am
comfortable doing so only because the cached text is the complete full text, the decisive
sentences are quotable verbatim, and the disagreement is about arithmetic on an asymmetric
unit rather than about biology I cannot see.

## 7. Membrane binding: what is full-length and what is an isolated domain

`GO:0035091 phosphatidylinositol binding` is solid for the intact protein:
[PMID:18034774 "APPL1 and APPL2 full-length proteins, isolated PH domains and isolated PTB
domains all bound to membrane-immobilized PtdIns(3)P, PtdIns(4)P, PtdIns(5)P, PtdIns(3,4)P 2
and PtdIns(3,5)P 2 ( Figure 4A )."] The three PH-domain residues the structure paper
nominates as the contact surface are present and conserved (§9).

`GO:0001786 phosphatidylserine binding` is weaker and is specifically an isolated-domain
result: [PMID:18034774 "APPL isolated PTB domains also bound to membrane-immobilized
phosphatidylserine (PS, spot 15)."] — the full-length protein did not, and the authors
themselves flag the discrepancy ("It is possible that APPL-APPL interactions and/or the
overall conformation of the full-length proteins may inhibit PTB domain-mediated PS
binding"). Real activity of the domain; not established for the protein. Non-core.

Similarly `GO:0005886 plasma membrane` IDA rests on overexpressed isolated domains
[PMID:18034774 "We found that APPL1 and APPL2 isolated PH domains localized to the plasma
membrane, cytosolic vesicles and distinct nuclear and perinuclear structures"], i.e. ectopic
fragments, not the native protein. The endogenous-protein localisation evidence is
endosomal, nuclear and (in macrophages) phagosomal.

## 8. The bulk-proteomics and interactome rows

Two projection tests, both run against QuickGO by `reference=` and paginated to completion:

- **PMID:19056867** (urinary exosome proteomics, the HDA row for `GO:0070062 extracellular
  exosome`) projects **1016 annotations onto 1016 distinct gene products** — one
  `GO:0070062` annotation per protein in the dataset. This is a whole-fraction inventory,
  not a claim about APPL2, and it is the textbook `MARK_AS_OVER_ANNOTATED` case.
- The gene-specific papers do **not** behave that way, which is the useful control:
  PMID:15016378 → 20 annotations / 4 entities; PMID:18034774 → 23/3; PMID:21645192 → 11/4;
  PMID:23055524 → 3/2; PMID:26583432 → 13/4; PMID:24879834 → 15/5; PMID:19433865 → 15/6.
  None of these is a projection.

Thirty-nine of the 124 review rows are `GO:0005515 protein binding` IPI. Resolving every
partner accession through UniProt gives: APPL1 (Q9UKG1, 11 rows), the four Rabs above,
SUV39H2 (Q9H5I1 and its isoform -2), CRADD (P78560), MAPRE3 (Q9UPY8), PRR35 (P0CG20),
EPM2AIP1 (Q7L775), KIFC3 isoform (Q9BVG8-5), ANXA2 (P07355), TBC1D1 (human Q86TI0 and mouse
Q60949), FSHR (P23945), RAB5A (P20339), RUVBL2 (Q9Y230), and one row whose WITH/FROM is the
CTNNB1/HDAC1/HDAC2/APPL1 set. The great majority come from systematic screens — Y2H
(PMID:16189514, PMID:23414517, PMID:23455924, PMID:25416956, PMID:31515488, PMID:32296183),
Y2H with kinase co-expression (PMID:25814554), AP-MS (PMID:28514442, PMID:33961781) and
endogenous tagging (PMID:35271311) — with no functional follow-up for APPL2. Those stay as
`MARK_AS_OVER_ANNOTATED`; the rows whose partner is a Rab, or APPL2 itself, or a partner
with a mapped mechanism (ANXA2, TBC1D1, RUVBL2), are re-termed or accepted.

Note that IntAct's `NbExp=23` for the APPL1 interaction is a count of experiments, several
of which come from the same studies; it is not 23 independent publications.

## 9. Residue-level checks

Run in `APPL2-bioinformatics/appl_orthology.py`, all against live UniProt sequences with
lengths asserted first:

- The three PH-domain residues King et al. nominate as the candidate non-canonical
  inositol-phosphate contact surface — [PMID:23055524 "hAPPL2 BARPH has Lys-289, Arg-287,
  and Trp-297"] — are **present at exactly those positions** in Q8NEU8 (R287, K289, W297),
  all inside the UniProt PH span 277-375, and all conserved in mouse Appl2. They are
  *equally* conserved in human APPL1, so this patch does not distinguish the paralogs and
  must not be used to argue that lipid binding is APPL2-specific.
- The putative NLS quoted for APPL2 — [PMID:23055524 "a putative nuclear localization
  sequence has been identified in the APPL2 sequence 151 PKKKENE 157"] — is present
  verbatim at 151-157, lies inside the BAR domain, and is conserved in mouse Appl2
  (PKKKENE) but **diverges in human APPL1**, whose aligned span is SKKREND. This is one of
  the few positions examined where the paralogs genuinely differ, and the crystal structure
  places it on a face masked by the PH domain — the basis for the authors' speculation that
  PH-domain rotation gates its accessibility.

These support the phosphoinositide-binding and nucleus rows but are *not* evidence that
APPL2 binds Ins(1,4,5)P3: no liganded APPL2 structure exists, and the assignment is a
superposition on ARHGAP9.

## 10. The IEA machinery

Four IEA pipelines contribute 38 rows.

- **GO_REF:0000107** (19 rows, Ensembl Compara orthology projection). Every one has
  WITH/FROM `UniProtKB:Q8K3G9|ensembl:ENSMUSP00000020500`. Those are **two identifiers for
  one donor** — I confirmed `ENSMUSP00000020500` maps to Q8K3G9 — so these rows have a
  single source, mouse Appl2, and pair one-for-one with the GO_REF:0000024 ISS rows. Same
  claim, two pipelines; not independent support.
- **GO_REF:0000024** (24 ISS rows, UniProt manual ortholog transfer), all from Q8K3G9.
- **GO_REF:0000044** (5 rows) projects UniProt Swiss-Prot subcellular-location keywords:
  SL-0191 nucleus, SL-0100 endosome membrane, SL-0093 early endosome membrane, SL-0205
  phagocytic vesicle membrane, SL-0206 phagocytic vesicle. These re-state UniProt's own
  curated locations, which are themselves drawn from the papers above.
- **GO_REF:0000117** (ARBA machine-learned rules) and **GO_REF:0000120** (combined methods).
  I fetched each rule from `https://rest.uniprot.org/arba/<id>` and counted its condition
  sets, which is a fair proxy for how promiscuous a rule is:

  | rule | term | condition sets | taxonomic span |
  |---|---|---|---|
  | ARBA00027801 | GO:0005886 plasma membrane | **686** | bacteria → plants → fungi → metazoa |
  | ARBA00027281 | GO:0098588 bounding membrane of organelle | **171** | very broad |
  | ARBA00027526 | GO:0042592 homeostatic process | **135** | very broad |
  | ARBA00028568 | GO:0005768 endosome | 97 | broad eukaryote |
  | ARBA00026540 | GO:0030659 cytoplasmic vesicle membrane | 72 | broad eukaryote |
  | ARBA00028627 | GO:0006606 protein import into nucleus | 14 | metazoa + fungi |
  | ARBA00085361 | GO:0007179 TGF-beta receptor signaling | 14 | metazoa |
  | ARBA00026346 | GO:0035091 phosphatidylinositol binding | 7 | eukaryote |
  | ARBA00033889 | GO:2000045 regulation of G1/S transition | 7 | primates, rodents, yeast |
  | ARBA00089669 | GO:0001786 phosphatidylserine binding | 5 | primates, fungi |
  | ARBA00093152 | GO:0046325 neg. reg. of D-glucose import | 4 | narrow |

  The top three are rules so broad that firing on APPL2 says essentially nothing about
  APPL2: `GO:0042592 homeostatic process` in particular is a term with no discriminating
  content, reached by a rule spanning bacteria to plants. Those are the IEA rows I mark as
  over-annotated. The narrow rules (4-14 condition sets) happen to reproduce conclusions
  that the experimental rows already support, so they are kept as redundant-but-correct.

## 11. What I think the core functions are

1. **Rab effector on APPL endosomes and on early phagosomes.** Binds GTP-loaded Rab5A/5C,
   Rab22A and, with highest affinity, Rab31 (Kd 140 nM), through the BAR-PH unit; this is
   what puts APPL2 on membranes. `GO:0031267` + `GO:0010008`.
2. **BAR-domain-mediated homo- and hetero-dimerization scaffold**, binding
   phosphoinositides through PH and PTB. `GO:0042803`, `GO:0035091`.
3. **Negative regulation of insulin-stimulated glucose uptake in muscle** via the
   phospho-Ser235-dependent TBC1D1 interaction. The one function with both perturbation
   directions and a tissue-specific knockout.
4. **Antagonist of APPL1 in adiponectin signalling** — competing for AdipoR1/R2 and
   sequestering APPL1. Carried by `GO:0033211` because GO lacks a signed child.
5. **Restraint of innate immune output and promotion of FcγR phagocytosis in macrophages** —
   two roles with opposite effects on the same Akt axis in the same cell type, depending on
   whether the trigger is TLR4 or FcγR, which is itself worth flagging to experts.

## 12. Open questions

- The PI3K/Akt sign problem. Appl2 KO macrophages show **increased** Akt phosphorylation
  after LPS [PMID:25328665 "phosphorylation of Akt and its downstream effector NF-κB was
  significantly enhanced"], while APPL2-depleted macrophages show **reduced** Akt
  recruitment and phosphorylation after FcγR engagement [PMID:25568335 "The reduced
  recruitment of Akt is thus in keeping with reduced levels of PI(3,4,5)P3 and a reduction
  in phosphorylated Akt during FcγR signaling."] Same cell type, opposite sign, different
  receptor. No annotation can capture this and neither paper reconciles it.
- Whether APPL2 recruits a PI3K directly is explicitly unresolved:
  [PMID:25568335 "It is not known whether these or any other PI3K subunits are recruited or
  regulated by APPL2, and this remains to be elucidated in future studies."]
- Whether the 151-PKKKENE-157 NLS is functional has never been tested:
  [PMID:26583432 "A possible nuclear localization signal in APPL2 has recently been observed
  in silico [43], but its functional role has not been tested experimentally."]
- APPL2's individual contribution to TGFβ-driven TβRI-ICD nuclear transport is unknown
  because the only experiments are double knockdowns (§5).
- PMID:18034774 carries an erratum (Traffic 2008;9(4):623-4) whose content is not in the
  cached record; I have not been able to check what it corrected, so quotes from that paper
  are taken from the main text sections only.

## 13. What the review does

Counted, not asserted, by `APPL2-bioinformatics/check_goa_reconciliation.py`:

- 126 GOA lines collapse to 124 distinct rows (two exact-duplicate lines differing only in
  ASSIGNED BY), all reviewed, plus 2 NEW rows.
- Actions: **ACCEPT 40, KEEP_AS_NON_CORE 49, MODIFY 22, MARK_AS_OVER_ANNOTATED 13, NEW 2.**
  No REMOVE, and no UNDECIDED — every cited paper was retrievable and read.
- 65 `propagation_review` blocks: the 2 IBAs, all 24 seeded ISS rows, all 38 IEA rows, and
  the one NEW ISS row. `source_entities` is generated from each row's own
  `supporting_entities` by script, so the two lists cannot drift.

The 22 MODIFY rows are all `GO:0005515 protein binding` IPIs where the partner is
identifiable: 9 rows whose partner is a Rab (RAB5A, RAB5C, RAB22A, RAB31) go to
`GO:0031267 small GTPase binding`, and 12 rows whose partner is APPL1 go to
`GO:0046982 protein heterodimerization activity`. The 23rd MODIFY is the
homotetramerization row (§6), proposed to become `GO:0051260 protein homooligomerization`.

The 13 over-annotated rows are the urinary-exosome HDA row (1016-entity projection), the
three broad-ARBA rows (`GO:0042592 homeostatic process`, `GO:0098588 bounding membrane of
organelle`) and 10 protein-binding IPIs from systematic screens with no APPL2 follow-up.

Two NEW rows: `GO:0090263 positive regulation of canonical Wnt signaling pathway` (IMP,
PMID:19433865 — GOA carries the Reptin and β-catenin/HDAC interactions but no process row
for what they do) and `GO:0140311 protein sequestering activity` (ISS from mouse Appl2,
PMID:19661063 — no molecular function currently names the activity by which APPL2
antagonises APPL1).

One judgement went against both a curator and UniProt: `GO:0051289 protein
homotetramerization` (§6). Everything else defers to the existing annotation where the
evidence could not be checked, and the two rows resting on APPL1+APPL2 double knockdowns
are kept with the limitation recorded rather than removed.
