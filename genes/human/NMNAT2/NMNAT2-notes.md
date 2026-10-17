# NMNAT2 (human) — review notes

UniProt: Q9BZQ4 (NMNA2_HUMAN), gene NMNAT2 (HGNC:16789), 307 aa, chromosome 1q25.
Synonyms: C1orf15, KIAA0479. EC 2.7.7.1 and EC 2.7.7.18.

## Core identity

NMNAT2 is one of three human nicotinamide/nicotinate mononucleotide adenylyltransferase
isoforms (NMNAT1 nuclear, NMNAT2 Golgi/cytosolic, NMNAT3 mitochondrial). It catalyzes the
central, rate-committing adenylyl-transfer step of NAD+ biosynthesis, common to both the
salvage and de novo routes:
- NMN + ATP -> NAD+ + PPi (EC 2.7.7.1, GO:0000309)
- NaMN + ATP -> NaAD (deamido-NAD+) + PPi (EC 2.7.7.18, GO:0004515)

The UniProt record names it "Nicotinamide/nicotinic acid mononucleotide adenylyltransferase 2"
with both EC numbers experimentally supported [file:human/NMNAT2/NMNAT2-uniprot.txt "EC=2.7.7.1 {ECO:0000269|PubMed:16118205, ECO:0000269|PubMed:17402747}"].

The functional summary in UniProt:
[file:human/NMNAT2/NMNAT2-uniprot.txt "Nicotinamide/nicotinate-nucleotide adenylyltransferase that acts as an axon maintenance factor"]
and
[file:human/NMNAT2/NMNAT2-uniprot.txt "Catalyzes the formation of NAD(+) from nicotinamide mononucleotide (NMN) and ATP"]
plus lower-efficiency use of the deamidated substrate
[file:human/NMNAT2/NMNAT2-uniprot.txt "Can also use the deamidated form; nicotinic acid mononucleotide (NaMN) as substrate but with a lower efficiency"].

## Catalytic evidence (PMID:16118205, PMID:17402747)

Both are abstract-only in the local cache (`full_text_available: false`), but they are the
ECO:0000269 experimental references cited by UniProt for EC 2.7.7.1/2.7.7.18 and for the
Golgi/cytoplasm localization. UniProt attributes FUNCTION, CATALYTIC ACTIVITY,
BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY and SUBCELLULAR LOCATION to
PubMed:16118205, and FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION and COFACTOR to
PubMed:17402747 [file:human/NMNAT2/NMNAT2-uniprot.txt "RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE"].

Berger et al. 2005 (PMID:16118205) abstract: "Nicotinamide mononucleotide adenylyltransferase
(NMNAT) is the central enzyme of the NAD biosynthetic pathway" and localized NMNAT2 "to the
Golgi complex" [PMID:16118205 "NMNAT2 and -3 were localized to the Golgi complex and the mitochondria, respectively"].

Sorci et al. 2007 (PMID:17402747) abstract: gives kinetic mechanism and confirms NMNAT2 as a
Golgi apparatus isozyme of NMNAT (EC 2.7.7.1) [PMID:17402747 "Golgi apparatus NMNAT2"]; NMNH
conversion by NMNAT2 is "much slower" and TrMP is not a substrate for NMNAT2, consistent with
UniProt's "Cannot use triazofurin monophosphate (TrMP) as substrate".

KM values (UniProt, from PMID:16118205/17402747): NMN 32 uM, NaMN 14.5 uM, ATP 204 uM;
Mg2+ is the preferred cofactor; monomeric active form; pH optimum 6.0–9.0.

## Subcellular location

UniProt SUBCELLULAR LOCATION: Golgi apparatus membrane (lipid-anchor), cytoplasmic vesicle
membrane (lipid-anchor), cytoplasm, and cell projection/axon
[file:human/NMNAT2/NMNAT2-uniprot.txt "SUBCELLULAR LOCATION: Golgi apparatus membrane"].
Delivered to axons with Golgi-derived cytoplasmic vesicles
[file:human/NMNAT2/NMNAT2-uniprot.txt "Delivered to axons with Golgi-"].
Palmitoylation (Cys164/Cys165) is required for membrane association
[file:human/NMNAT2/NMNAT2-uniprot.txt "Palmitoylated; palmitoylation is required for membrane"].
Cytosolic localization is also supported by HPA immunofluorescence (GOA IDA, GO_REF:0000052,
GO:0005829). The axon and cytoplasmic-vesicle-membrane C annotations are By-similarity/ISS to
mouse Q8BNJ3, consistent with the axonal-transport biology.

## Axon maintenance / survival factor

This is the best-known physiological role of NMNAT2 and is central, not incidental. UniProt:
"Axon survival factor required for the maintenance of healthy axons: acts by delaying Wallerian
axon degeneration" [file:human/NMNAT2/NMNAT2-uniprot.txt "Axon survival"]. NMNAT2 is a labile
protein whose continuous replenishment from the soma maintains axonal NAD+ and keeps the
pro-degenerative NADase SARM1 inactive; when NMNAT2 is depleted, NMN accumulates, SARM1 is
activated, and Wallerian-type axon degeneration ensues.

Gilley, Mayer, Yu & Coleman 2019 (PMID:30304512), abstract-only in cache, is the ISS source
reference for GO:0061564 (axon development). Abstract: "Nicotinamide mononucleotide
adenylyltransferase 2 (NMNAT2) is an endogenous axon maintenance factor that preserves axon
health by blocking Wallerian-like axon degeneration" [PMID:30304512 "an endogenous axon
maintenance factor that preserves axon health by blocking Wallerian-like axon degeneration"];
"Mice lacking NMNAT2 die at birth with severe axon defects" [PMID:30304512 "Mice lacking NMNAT2
die at birth with severe axon defects"]; reduced levels "compromises the development of
peripheral axons and increases their vulnerability to stresses" [PMID:30304512 "compromises the
development of peripheral axons"].

Turnover: NMNAT2 is degraded after neurite injury via polyubiquitination by the MYCBP2 (PHR/PAM)
E3 ligase after recognition by FBXO45 [file:human/NMNAT2/NMNAT2-uniprot.txt "Degradation is
caused by polyubiquitination by MYCBP2 after recognition"] (PMID:29643511, PMID:29997255).

Disease: biallelic loss-of-function NMNAT2 variants cause a childhood-onset polyneuropathy with
erythromelalgia / skeletal abnormalities (not in cached publications; consistent with the axon-
maintenance role). Recorded as a suggested-question / disease context, not annotated here.

## PARP16 adaptor / translation role (PMID:34314702, full text available)

Challa et al. 2021 (Cell) is the IDA source for two annotations:
- GO:0140768 protein ADP-ribosyltransferase-substrate adaptor activity
- GO:2000766 negative regulation of cytoplasmic translation

Full text supports both. NMNAT2 supplies cytosolic NAD+ that "supports the catalytic activity of
the mono(ADP-ribosyl) transferase (MART) PARP-16, which mono(ADP-ribosyl)ates (MARylates)
ribosomal proteins" [PMID:34314702 "NMNAT-2 supports the catalytic activity of the mono(ADP-ribosyl)
transferase (MART) PARP-16, which mono(ADP-ribosyl)ates (MARylates) ribosomal proteins"]. NMNAT2
and PARP-16 physically interact and "only wild-type and not catalytically dead mutant NMNAT-2
(W92G) enhances PARP-16 auto-MARylation" [PMID:34314702 "only wild-type and not catalytically
dead mutant NMNAT-2 (W92G) enhances PARP-16 auto-MARylation"]. Functionally, "NMNAT-2, which
supports ribosomal protein MARylation, acts to inhibit protein synthesis in a manner that
depends on its catalytic activity" [PMID:34314702 "acts to inhibit protein synthesis in a manner
that depends on its catalytic activity"].

Note on GO:0140768: the effect is mediated through NAD+ production feeding PARP16 (catalytic-
activity dependent, W92G-sensitive), plus a direct NMNAT2–PARP16 interaction. This is a
context-specific (ovarian cancer / high-PARP16) moonlighting activity, not the core evolved
function; the primary MF remains the NMN/NaMN adenylyltransferase. Both annotations are
experimental IDA and are KEPT (non-core). Retained per policy (do not REMOVE experimental
annotations); marked KEEP_AS_NON_CORE.

## Annotation-by-annotation disposition (summary)

Core MF (adenylyltransferase): GO:0000309 and GO:0004515.
Core BP: GO:0009435 NAD+ biosynthetic process (and salvage-route child GO:0034355).
Core location: Golgi apparatus / Golgi membrane / cytosol.
Non-core but genuine: axon development (GO:0061564), axon/cytoplasmic-vesicle-membrane location,
PARP16 adaptor (GO:0140768), negative regulation of cytoplasmic translation (GO:2000766),
nucleotide biosynthetic process (GO:0009165, general parent).
Over-annotated / too-general: GO:0003824 catalytic activity (IEA, root-level MF).

## Term label verifications (OLS, 2026-07)

- GO:0000309 nicotinamide-nucleotide adenylyltransferase activity — current, matches.
- GO:0004515 nicotinate-nucleotide adenylyltransferase activity — current, matches.
- GO:0009435 NAD+ biosynthetic process — current.
- GO:0034355 NAD+ biosynthetic process via the salvage pathway — current.
- GO:0061564 axon development — current (covers axonogenesis + axon regeneration).
- GO:2000766 negative regulation of cytoplasmic translation — current.
- GO:0140768 protein ADP-ribosyltransferase-substrate adaptor activity — current.
- GO:0005794 Golgi apparatus / GO:0000139 Golgi membrane — current.

## 2026-10-09 — weekly compliance pass

Evidence-aware compliance (`just compliance-all`) had NMNAT2 at 46.10 weighted,
the largest file in this batch (28 annotations, 13 references). **No annotation
action was changed** — the prior review's calls hold. The pass added
justification, provenance and the missing suggestion blocks.

- **`review.reason` added to all 28 annotations.** Several deserve recording:

  - **The two IBA nodes differ, and the split is the interesting finding.** The
    two catalytic activities and the salvage process come from the *deep* node
    **PANTHER:PTN000247701**, whose descendants span plant (AT5G55810), yeast
    (S000003242, S000004320), fly (FBgn0039254), mouse, *bacterial NadD*
    (P0A752) and the human paralogs NMNAT1 (Q9HAN9) and NMNAT3 (Q96T66). Golgi
    localization comes from a *much shallower* node, **PANTHER:PTN002635346**,
    seeded only by mouse Nmnat2 and human NMNAT2. That is correct, not sloppy:
    the activity is ancestral and shared with both paralogs, whereas Golgi
    anchoring is the isoform-specific trait and depends on palmitoylation of
    Cys-164/165 rather than on the catalytic fold. A short donor list is not weak
    support when the transferred trait is itself lineage-restricted.
  - **Q9BZQ4 appears in its own `WITH/FROM`** on two IBA rows. Per
    `projects/IBA_REVIEW.md` this is expected and correct — NMNAT2's own
    experimental annotations are among the descendant evidences the PAINT curator
    used to place the IBD — and is explicitly *not* marked circular.
  - **Signature specificity determines term specificity.** `GO:0003824` (root)
    fires on **IPR004821**, the broad cytidylyltransferase-like fold; the specific
    activity rows fire on **IPR045094**, family-specific for eukaryotic NMN
    adenylyltransferases. Same pipeline family, opposite outcome — recorded in the
    reasons so the differing actions are legible.
  - **`GO:0005737` cytoplasm is ACCEPT, not MODIFY → cytosol.** NMNAT2 genuinely
    occupies several cytoplasmic compartments (soluble pool, cytoplasmic face of
    the Golgi membrane, Golgi-derived axonal vesicles). Collapsing onto cytosol
    would *lose* the membrane-anchored pools, not sharpen the claim.
  - **`GO:0061564` axon development stays non-core, and the reason says why the
    strong evidence does not promote it.** Null mice die at birth with severe axon
    defects; compound heterozygotes already have fewer myelinated sensory axons at
    1.5 months [PMID:30304512]. That is powerful *necessity* evidence. But what
    NMNAT2 contributes is NAD+ — it does not itself extend or guide an axon; it
    sustains a metabolite pool whose depletion activates SARM1. Real, indirect,
    mediated by the catalytic function already annotated.

- **Term-fit concern flagged for a curator, action deliberately unchanged:
  `GO:0140768`.** The term is defined as "An enzyme-substrate adaptor that bings
  together a protein ADP-ribosyl transferase and its substrate" (OLS), which
  implies bridging *separable from catalysis*. But UniProt's mutagenesis data from
  the same paper show H24D and W92G abolish **both** adenylyltransferase activity
  **and** the ability to promote ribosome mono-ADP-ribosylation
  (ECO:0000269|PubMed:34314702). Catalysis-dependence points to local NAD+ supply,
  not adaptor bridging. The curator read the full text, so this is recorded as a
  `suggested_question` plus a mechanism-separating experiment rather than acted on
  unilaterally.

- **`findings` added to all 13 references** — 3 on PMID:16118205, 3 on
  PMID:17402747, 2 on PMID:30304512, 4 on PMID:34314702, 1 each on the two
  Reactome entries, plus the 7 GO_REFs. Note the useful *negative* results now
  captured from Sorci et al.: TrMP is a substrate only for NMNAT1 and NMNAT3, and
  NMNH conversion by NMNAT2 is much slower — the exclusions that justify
  annotating exactly these two activity terms.

- **TAS rows now quote the primary source they trace to.** A TAS is only as good
  as the statement behind it, so both Reactome Golgi-membrane rows now carry the
  Berger et al. quote alongside Reactome's own. The cytosol (HPA) and cytoplasm
  (EXP) rows gained Challa et al.'s "NMNAT-2, a cytosolic NAD+ synthase" as
  independent corroboration — labelled as corroboration, since neither row cites
  that paper.

- **`alternative_products` descriptions.** Isoform 2 (VSP_015571) replaces the
  first 28 residues, removing NAD-binding residues 16/17 **and the critical
  ATP-binding His-24**. Since H24A alone reduces activity by 95%, it would be
  expected catalytically dead — stated as an expectation, since it is untested.

- **6 `suggested_questions` (was 3) and 3 `suggested_experiments` (was 2, both
  lacking `hypothesis`).** New ones cover the GO:0140768 term fit, regulation of
  Cys-164/165 palmitoylation given MYCBP2/FBXO45-driven turnover, and isoform 2.

Result: 46.10 → **96.62** weighted, `just validate` clean — including the four
pre-existing folded-scalar warnings (`cytidylyltransferase- like`,
`palmitoylation- dependent`, `ADP- ribosyltransferase-substrate`, `activity-
independent`), all rewrapped. The only remaining gaps are the seven GO_REF
`findings[].supporting_text` slots; those documents are not cached, so any quote
would be unverifiable.
