# SUFU (Q9UMX1) — curation notes

Working journal for the GO annotation review of human SUFU (Suppressor of fused homolog,
HGNC:16466, UniProt Q9UMX1). Appended chronologically; every assertion carries provenance.

## 1. What the protein is

SUFU is a 484-residue (isoform 1, Su(fu)484) intracellular protein with no catalytic
domain, no transmembrane segment, and no recognisable enzymatic motif. It is the single
human member of the Suppressor of fused family (PANTHER PTHR10928; UniProt SIMILARITY:
"Belongs to the SUFU family"). It was cloned in parallel by two groups in 1999 as the
vertebrate homolog of *Drosophila* Su(fu)
[PMID:10559945 "Here we identify the human Suppressor-of-Fused (SUFUH) complementary DNA and show that the gene product interacts physically with the transcriptional effector GLI-1, can sequester GLI-1 in the cytoplasm, but can also interact with GLI-1 on DNA."]
and
[PMID:10564661 "Two alternatively spliced isoforms of hSu(fu) were identified, predicting proteins of 433 and 484 amino acids, with a calculated molecular mass of 48 and 54 kDa, respectively."].
The two isoforms differ only by a 52-residue C-terminal extension
[PMID:10564661 "The two proteins differ only by the inclusion or exclusion of a 52-amino-acid extension at the carboxy terminus."],
and sequence identity to the fly protein is modest
[PMID:10564661 "exhibits an overall 37% sequence identity (63% similarity) with the Drosophila protein and 97% sequence identity with the mouse Su(fu)"].

A striking asymmetry: the fly protein is dispensable, the mammalian one is essential.
[PMID:24311597 "Whilst being completely dispensable for Drosophila embryogenesis, this protein is absolutely essential for mammalian development, since knockout of Sufu in mice leads to continuous ligand-independent Hh signalling activity and embryonic lethality at ∼E9.5"]. This matters for the review: the
ancestral PAINT node assertion is about the *mechanism* (sequestering GLI/Ci), not about
the phenotypic weight of the gene in any one lineage.

## 2. Core mechanism — sequestration of GLI, not catalysis

The single best-supported statement about SUFU is that it binds full-length GLI1/GLI2/GLI3
and holds them out of productive transcriptional service. UniProt states this as the
FUNCTION line: "Negative regulator in the hedgehog/smoothened signaling pathway that acts
by sequestering the GLI (GI1, GLI2 and GLI3) transcription factors in the cytoplasm",
citing eleven primary papers.

The DYRK2 paper states the mechanism plainly:
[PMID:38968120 "Another negative regulator, SUFU, inhibits Hh signaling by retaining GLI2 and GLI3 in the cytoplasm and blocking their nuclear translocation."]

The structural work defines the interface. Full-length human SUFU alternates between an
open and a closed state, clamping a short conserved GLI motif:
[PMID:24311597 "Upon GLI binding, SUFU undergoes a large conformational change in which the N- and C-terminal domains come together to clamp highly conserved GLI residues"]
and the minimal recognition element is SYGHL
[PMID:24311597 "Moreover, the tight packing of the leucine next to the histidine in GLI with SUFU residues, coupled with the importance of this leucine in the protection of SUFU from deuteration, strongly suggest that the minimal SUFU binding motif in GLI encompasses the amino acids SYGHL."].
The independent structure paper reaches the same two-state picture and, importantly,
shows that breaking the interface breaks *all* of SUFU's downstream effects at once:
[PMID:24217340 "Mutations of critical interface residues disrupt the Sufu-Gli complex and prevent Sufu from repressing Gli-mediated transcription, tethering Gli in the cytoplasm and protecting Gli from the 26S proteasome-mediated degradation."]

That last sentence is the key curation fact. Transcriptional repression, cytoplasmic
tethering and protection from degradation are not three separate activities — they are
three readouts of one binding event. This is why `GO:0140311 protein sequestering
activity` is the right core molecular function and the transcription-level terms are
consequences rather than independent functions.

An intrinsically disordered loop (IDR) in SUFU is the element through which upstream
signal is relayed:
[PMID:24311597 "Collectively, these results imply that the IDR in SUFU is dispensable for GLI binding and repression activity in cells without upstream pathway activation."]
Deleting it makes repression constitutive and SMO-agonist-resistant
[PMID:24311597 "While activation of cells with SMO agonist (SAG), a Hh pathway activator upstream to SUFU, overrode repression by the full-length protein, it failed to reactivate the pathway in the presence of SUFU-Δ or SUFU-SH (p ≤ 0."].

## 3. Second mechanism — promoting GLI3 processing to the repressor form

SUFU is not only a brake on GLI activator; it actively promotes conversion of full-length
GLI3 into the GLI3R repressor. UniProt: "In absence of smoothened signaling, the SUFU-GLI3
complex is recruited to cilia, leading to the efficient processing of full-length GLI3
into transcription repressor GLI3R: SUFU participates to GLI3 processing by promoting
recruitment of GSK3B to GLI3 (PubMed:24311597, PubMed:28965847)."

The Joubert-syndrome paper provides the human loss-of-function test:
[PMID:28965847 "Functional studies on cellular models and fibroblasts showed that both variants significantly reduced SUFU stability and its capacity to bind GLI3 and promote its cleavage into the repressor form GLI3R."]
with the pathway-level consequence
[PMID:28965847 "In turn, this impaired SUFU-mediated repression of the SHH pathway, as shown by altered expression levels of several target genes."]

This is the evidence base for `GO:0010954 positive regulation of protein processing` and
for the adaptor-activity term `GO:0030674` — SUFU physically links GLI to the kinases and
ubiquitin machinery that process it. The adaptor reading goes back to the original
characterisation:
[PMID:10564661 "The data further suggest that Su(fu) can act by binding to Gli and inhibiting Gli-mediated transactivation as well as by serving as an adaptor protein, which links Gli to the Slimb-dependent proteasomal degradation pathway."]

## 4. How SUFU is released — the inputs

Several independent routes converge on weakening the SUFU–GLI interface. None of these are
SUFU activities; they are things done *to* SUFU or to its partner, and they matter here
only because the cited papers are the evidence for SUFU's own annotations.

- **Fused-family kinases.** STK36 opposes SUFU
  (UniProt: "Interacts with STK36; promoting dissociation between SUFU and GLI (GI1, GLI2
  and GLI3) transcription factors (PubMed:10806483)"). The cached record for
  PMID:10806483 is title-only, so the UniProt statement is the usable provenance.
- **ULK3.** A reciprocal-inhibition relationship, and the basis of the one
  `GO:0019901 protein kinase binding` annotation:
  [PMID:20643644 "We demonstrate that Ulk3 through its kinase domain interacts with Suppressor of Fused (Sufu), a protein required for negative regulation of Gli proteins. Sufu blocks Ulk3 autophosphorylation and abolishes its ability to phosphorylate and positively regulate Gli proteins."]
  Note the direction: SUFU inhibits the kinase, not the other way round, and the
  Sufu-Ulk3 complex promotes GLI2 repressor formation
  [PMID:20643644 "We demonstrate that the Sufu-Ulk3 complex, when co-expressed with Gli2, promotes generation of the Gli2 repressor form"].
- **DYRK2 at the ciliary base.**
  [PMID:38968120 "This phosphorylation induces the dissociation of GLI2/GLI3 from suppressor, SUFU, and their translocation into the nucleus."]
  with a direct affinity measurement
  [PMID:38968120 "In contrast, the phospho-GLI3S313309–345 peptide demonstrated reduced binding to SUFU, with a KD of 5."]
- **ERK2/MAPK crosstalk.**
  [PMID:35831023 "Here we show that MAP kinase-mediated phosphorylation weakens the binding of the GLI1 transcription factor to its negative regulator SUFU."]
  quantitatively
  [PMID:35831023 "these phosphorylations cooperate to weaken the affinity of GLI1-SUFU binding by over 25-fold"].
- **mTOR/S6K1 crosstalk.**
  [PMID:22439934 "we found that an activated mTOR/S6K1 pathway promotes Gli1 transcriptional activity and oncogenic function through S6K1-mediated Gli1 phosphorylation at Ser84, which releases Gli1 from its endogenous inhibitor, SuFu"]
- **SCF(FBXL17)-mediated turnover of SUFU itself.**
  [PMID:27234298 "Here, we show that Fbxl17 (F-box and leucine-rich repeat protein 17) targets Sufu for proteolysis in the nucleus. The ubiquitylation of Sufu, mediated by Fbxl17, allows the release of Gli1 from Sufu for proper Hh signal transduction."]
  UniProt localises the site: "Polyubiquitinated at Lys-257 by the SCF(FBXL17) complex".
  This is the one interaction row where SUFU is the *substrate* of an E3, which makes
  `ubiquitin protein ligase binding` the informative replacement for generic protein
  binding.

## 5. Where SUFU acts

Cytoplasm and nucleus are both experimentally established in human cells (UniProt
SUBCELLULAR LOCATION: "Cytoplasm {ECO:0000269|PubMed:10559945, ECO:0000269|PubMed:28965847}.
Nucleus {ECO:0000269|PubMed:10559945, ECO:0000269|PubMed:28965847}."). The nuclear pool is
not incidental — the original paper showed SUFU engages GLI1 on DNA as well as sequestering
it (PMID:10559945, quoted in §1), and FBXL17 degrades SUFU specifically in the nucleus
(PMID:27234298, §4).

Ciliary localisation is inferred by similarity in UniProt ("Cell projection, cilium
{ECO:0000250|UniProtKB:Q9Z0P7}") but is mechanistically load-bearing in the vertebrate
implementation of the pathway, and Reactome curates the trafficking explicitly
(R-HSA-5610766 "The intraflagellar transport A (IFT-A) complex is required for the transit
of GLI:SUFU complexes to the ciliary base"; R-HSA-5610767, the IFT-B counterpart to the
tip; R-HSA-5635860 "GLI:SUFU translocates to the ciliary tip in response to Hh signaling").
The DYRK2 work places the relevant phosphorylation at the ciliary base and observes SUFU
mislocalisation when the kinase is lost
[PMID:38968120 "In our previous study, GLI2, GLI3, and SUFU showed abnormal localization in Dyrk2−/− MEFs, whereas SMO localization remained unaffected (28)."].
So `cilium`, `ciliary base` and `ciliary tip` are all defensible; the cytoplasmic/nuclear
pools remain the sites of the core activity.

## 6. Phylogeny — reading the IBA rows

The local PAINT slice `interpro/panther/PTHR10928/PTHR10928-paint.tsv` records node
PTN000859153 with IBD support for five terms:

| term | aspect | seeds |
|---|---|---|
| GO:0005634 nucleus | C | fly Su(fu), mouse Sufu, human SUFU |
| GO:0005737 cytoplasm | C | fly Su(fu), mouse Sufu, human SUFU |
| GO:0140311 protein sequestering activity | F | mouse Sufu, human SUFU |
| GO:0000122 neg. reg. of Pol II transcription | P | mouse Sufu, human SUFU |
| GO:0045879 neg. reg. of smoothened signaling | P | fly Su(fu), mouse Sufu, zebrafish, human SUFU |

Three points follow, and they are the ones easiest to get backwards:

1. Human SUFU appearing in its own `WITH/FROM` is **expected**. SUFU has experimental
   annotations for nucleus, cytoplasm, GO:0140311 and GO:0045879; those experimental rows
   are among the descendant evidences the PAINT curator used to place the IBD. The IBA
   then says something *additional* — that the function is inherited from the eumetazoan
   node rather than being a vertebrate novelty. This is not circularity.
2. The `GO:0140311` node is seeded by only two descendants (mouse and human). A short
   donor list is not weak support: PTHR10928 is a small, single-copy family and the
   curator had the whole alignment in view.
3. The node is placed at taxon:6072 (Eumetazoa), which is consistent with the module's
   framing of Hedgehog signaling as pan-metazoan. `modules/hedgehog_signaling.yaml` cites
   exactly this node for the `sufu_sequestration` annoton, with the same MF (GO:0140311),
   the same process (GO:0045879) and the same location (GO:0005737). Nothing in the
   literature reviewed here contradicts that annoton.

One divergence worth flagging: the local PAINT slice carries an IBD for `GO:0000122` at
PTN000859153 (dated 2026-07-24), but the human GOA snapshot in `SUFU-goa.tsv` has no
corresponding IBA row for that term — human SUFU has GO:0000122 only by IDA, ARBA/IEA and
TAS. That is a snapshot-lag observation, not a defect in either file, and it does not
change any action.

## 7. GO-CAM grounding

`gocams/index.tsv` places SUFU in five curated human models (693b3c0900001389,
693b3c0900001501, 693b3c0900001575, 696022cd00001523, 696022cd00001645). Every one of
them types SUFU identically: MF `GO:0140311 protein sequestering activity`, BP
`GO:0045879 negative regulation of smoothened signaling pathway`, CC `GO:0005737
cytoplasm`. The models differ only in which Fused-family/DYRK kinase and which GLI
paralog they instantiate. Independent curator judgment therefore converges on the same
core triple that the PAINT node and the module use, which is a strong reason to treat
that triple as the core and everything else as consequence or context.

## 8. Judgments made in this review, and why

**Transcription terms.** `GO:0000122` (negative regulation of Pol II transcription) is
ACCEPTed: SUFU binds the GLI transcription factor directly and the repression is a direct
consequence of that binding, demonstrated in reporter assays in the cited paper. By
contrast `GO:0006355 regulation of DNA-templated transcription` is the uninformative
parent — SUFU only ever regulates *negatively*, and only at Pol II promoters — so those
two rows are MODIFY → GO:0000122.

`GO:0003714 transcription corepressor activity` is kept but as **non-core**. It is not
wrong: SUFU is found on DNA with GLI1 (PMID:10559945) and UniProt records a DNA-bound
corepressor complex with SAP18 and SIN3 (by similarity to mouse). But both GOA rows are
TAS, the chromatin-corepressor mechanism is much less established than sequestration, and
the sequestering activity accounts for the repression readout on its own (PMID:24217340,
§2). Calling it core would put a secondary mechanism on the same footing as the one the
PAINT node, the module and all five GO-CAMs agree on.

**`GO:0007165 signal transduction`.** Both rows MODIFY → `GO:0045879`. This is not a case
of "IEA is allowed to be broad"; `signal transduction` is so general it carries no
information about a protein whose entire role is one specific negative step of one
specific pathway.

**Rat-derived IEA rows.** Two GO_REF:0000107 rows trace to the rat ortholog
(UniProtKB:A0A8I6A606). Tracing the donor annotations in QuickGO shows both rest on **IEP**
(expression-pattern) evidence:
- `GO:0007286 spermatid development` ← rat IEP from PMID:21893610, "Hedgehog signalling
  promotes germ cell survival in the rat testis". Marked over-annotated: Hedgehog signaling
  genuinely operates in the testis, so the term is not absurd, but an expression
  correlation in rat does not establish that human SUFU executes a function in spermatid
  development.
- `GO:2001040 positive regulation of cellular response to drug` ← rat IEP from
  PMID:30790292, "Oroxylin A increases the sensitivity of temozolomide on glioma cells by
  hypoxia-inducible factor 1α/hedgehog pathway under hypoxia". Removed: this is a
  cell-line pharmacology observation, propagated first as an expression-pattern annotation
  in rat and then electronically into human. It asserts a physiological function that no
  evidence supports.

**`GO:0008013 beta-catenin binding`.** Kept as non-core. UniProt records the CTNNB1
complex and the beta-catenin-regulation role only "By similarity" from mouse, and it sits
outside the Hedgehog axis that defines the protein.

**Generic `protein binding` (74 rows).** Per repository policy these are never ACCEPTed.
Thirteen rows whose partner is a GLI transcription factor (GLI1 P08151, GLI3 P10071, mouse
Gli2 Q0VGT2) become MODIFY → `GO:0140297 DNA-binding transcription factor binding`: GLIs
are sequence-specific zinc-finger transcription factors, the interaction is the single
most replicated fact about SUFU, and the replacement term states something the bare term
does not. Three kinase-partner rows become informative MF terms — STK36 (×2) →
`GO:0019901 protein kinase binding`, and FBXL17 in the mechanistic EMBO J study →
`GO:0031625 ubiquitin protein ligase binding`, the standard GO treatment of a substrate
that engages an SCF complex. The remaining ~58 rows come from large-scale interactome
surveys (PMID:16189514, 20211142, 25416956, 28514442, 31403225, 31515488, 32296183,
32814053, 33961781, 35140242, 40205054) and name partners with no established connection
to SUFU biology — keratins, ZNF/KRAB proteins, RCN3, PEX26, STX19, SLC41A3 and so on.
Those are REMOVE: the measurements may well be real, but a bare `protein binding` row
carries no functional information, and inventing a specific function from a single Y2H or
AP-MS hit is exactly what the guidelines forbid. One further row, BRAF from
PMID:35512704 ("Systematic discovery of mutation-directed neo-protein-protein interactions
in cancer"), is a *neo*-interaction of a mutant protein; it is removed for the same reason
and would not justify a kinase-binding term even if kept.

**No `NEW` annotations proposed.** The three things one might be tempted to add all fail
the tests in CLAUDE.md. `GO:0007224 smoothened signaling pathway` is an ancestor of
`GO:0045879`, which SUFU already carries eight times — redundancy, not coverage.
`GO:0140416 transcription regulator inhibitor activity` is tempting, but SUFU's inhibition
of GLI is already expressed by `GO:0140311` plus `GO:0000122`, and adding it would assert a
second molecular function where the structural work says there is one binding event with
several readouts (PMID:24217340, §2). Terms for the developmental phenotypes of SUFU loss
(neural tube, limb, cerebellum) describe outcomes of deregulated GLI activity in other
cells and tissues, not steps SUFU performs.

## 9. Open questions carried into the review

- Which of the four documented release mechanisms (STK36, ULK3, DYRK2, ERK2/S6K1) dominates
  in a normal Hedgehog response in a given human tissue, and are they redundant or
  sequential? PMID:38968120 explicitly leaves this open ("it is plausible that other sites
  must undergo PTMs in a coordinated and sequential manner to achieve complete SUFU
  dissociation").
- Is the DNA-bound corepressor role (SAP18/SIN3) a genuine human mechanism or a
  mouse-specific/overexpression artefact? It is the difference between `GO:0003714` being
  non-core and being wrong.
- The isoforms: `Q9UMX1-1` (484 aa) is the major isoform and `Q9UMX1-2` (433 aa) is
  enriched in fetal testis (PMID:10564661). Both bind GLI1 in IntAct. No GOA row is
  isoform-qualified, so no `isoform` field was added.
