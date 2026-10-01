# NSUN2 (Q08J23) — review notes

## The question this review has to settle

GOA carries two catalytic molecular functions for NSUN2, each with experimental support:

- `GO:0016428 tRNA (cytidine-N5)-methyltransferase activity` — EXP, IBA, IDA x3, IEA
- `GO:0062152 mRNA (cytidine-5-)-methyltransferase activity` — EXP, IBA, IDA x3, IEA

The enzyme is real and nobody disputes it. What is disputed is one of its **substrate classes**.
The position taken here: **tRNA/ncRNA m5C is core; mRNA m5C is real but demoted to non-core**,
with the methodological dispute recorded in `reason` and the unresolved question moved to
`suggested_questions`. Nothing is removed: `GO:0062152` carries an EXP code, and CLAUDE.md
forbids overruling an experimental annotation whose full text I have not read.

## Why the tRNA activity is core

NSUN2 is the human orthologue of yeast Trm4, and the founding paper shows position-specific
catalysis on a defined substrate:

- [PMID:17071714 "We identified a human orthologue of tRNA:m5C methyltransferase from Saccharomyces cerevisiae, which has been previously shown to catalyse the specific modification of C34 in the intron-containing yeast pre-tRNA Leu (CAA)."]
- [PMID:17071714 "Using transcripts of intron-less and intron-containing human pre-tRNA Leu (CAA) genes as substrates, we have shown that m5C34 is introduced only in the intron-containing tRNA precursors when the substrates were incubated in the HeLa extract."]

Human loss-of-function confirms the substrate in vivo:

- [PMID:22577224 "Patient cells lacked NSUN2 protein and there was resultant loss of site-specific 5-cytosine methylation of the tRNA(Asp GTC) at C47 and C48, known NSUN2 targets."]

And the mitochondrial tRNA activity was reconstituted with purified protein — the gold standard,
a defined enzyme plus SAM plus substrate giving a mapped product:

- [PMID:31287866 "In addition, we successfully reconstituted m5C at positions 48-50 of mt-tRNA in vitro with NSUN2 protein in the presence of S-adenosylmethionine."]
- [PMID:31287866 "In this study, we took advantage of mass spectrometric analysis to map 5-methylcytidine (m5C) at positions 48-50 in eight mouse and six human mt-tRNAs."]
- [PMID:31276587 "Here we employ spatially restricted proximity labelling and immunodetection to demonstrate that NSUN2 is imported into the matrix of mammalian mitochondria."]

A third, independent ncRNA substrate — vault RNA VTRNA1.1 C69 — is likewise attributed
exclusively to NSUN2:

- [PMID:31186410 "Methylation of cytosine 69 in VTRNA1.1 occurs frequently in human cells, is exclusively mediated by NSUN2, and determines the processing of VTRNA1.1 into small-vault RNAs (svRNAs)."]

## The mRNA m5C claim: what is solid and what is not

### Evidence that NSUN2 does methylate mRNA

The strongest orthogonal evidence is not bisulfite sequencing at all. The RNABPP chemoproteomics
study used **mechanism-based covalent crosslinking** (5-fluorocytidine traps the enzyme on its
substrate through the catalytic cysteine) combined with oligo-dT capture, and separately measured
nucleoside m5C by LC-MS/MS in NSUN2 knockout cells:

- [PMID:34556860 "Since this approach should primarily enrich for mRNA m5C methyltransferases, we tested this strategy with NSUN2, which methylates both tRNA13, 15 and mRNA16, 17."]
- [PMID:34556860 "Consistent with previous RNA bisulfite sequencing and m5C mass spectrometry that have implicated NSUN2 as the major mRNA m5C-forming enzyme16, 17, we found an 82% reduction in mRNA m5C levels upon NSUN2 knockout"]

A catalysis-dependent rescue exists too — the mRNA export phenotype is restored by wild-type but
not catalytically dead NSUN2, which is the right control and is rarely done in this literature:

- [PMID:28418038 "Dysregulation of ALYREF-mediated mRNA export upon NSUN2 depletion could be restored by reconstitution of wild-type but not methyltransferase-defective NSUN2."]

And in vitro methylation of a defined mRNA fragment was reported for p16:

- [PMID:22395603 "In vitro methylation assays show that NSun2 methylates the p16 3'UTR at A988."]

So **the activity itself should not be removed**, and indeed the 2026 review that catalogues the
problems in this field still accepts the enzyme assignment:

- [PMID:42587746 "Of the eight m5C RNA methyltransferases in humans, only two, NSUN2 and NSUN6, were found to be capable of modifying the main portion of cellular mRNAs."]

### Evidence that the mRNA m5C *maps* and their biological weight are unreliable

The same RNABPP authors are candid about the main confound in their own headline number:

- [PMID:34556860 "We have employed a rigorous polyA mRNA purification, however since m5C is ~40-fold higher in total RNA than polyA-RNA, and comparably reduced in each sample upon NSUN2 KO (Figure 3b and 3c), we cannot exclude the possibility that contaminating tRNA/rRNA nucleosides may contribute to the measured m5C content."]
- [PMID:34556860 "We also found that NSUN2 installs the majority of m5C sites on total RNA (76% reduction upon NSUN2 KO) (Figure 3b), likely reflective of abundant tRNA m5C sites"]

The 2026 Cells review sets out the mapping problems:

- [PMID:42587746 "However, unlike DNA, free mRNA often has a complex secondary and tertiary structure, which can shield certain regions of the molecule from the action of bisulfite, thus producing false-positive signals in this method."]
- [PMID:42587746 "A comparison of results obtained using Aza-IP, Bis-Seq, and miCLIP revealed that the overlap of methylation sites detected by these methods is very low"]
- [PMID:42587746 "However, it should be noted that all methods do not provide unambiguous results for m5C site mapping and may contain both false-negative and false-positive results."]

and the stoichiometry problem, which is the deeper one because it undermines the reader-based
mechanisms on which most of the downstream literature rests:

- [PMID:42587746 "The key issue is that the frequency of occurrence of m5C residues in mRNA is 1 in several thousand, and therefore it is unclear how the aforementioned proteins, whose affinity for m5C-containing regions in mRNA is only a few times higher than for unmodified regions, which are orders of magnitude more common, can distinguish such mRNAs."]
- [PMID:42587746 "Despite all this, the specific mechanism by which the m5C residue in mRNA physically contributes to a decrease in its degradation remains unclear."]

### The downstream cancer/inflammation literature

A large and still-growing set of papers assigns a phenotype to NSUN2 m5C on one named transcript,
typically read out by YBX1 or ALYREF, e.g.

- [PMID:31358969 "Moreover, NSUN2 and YBX1 are demonstrated to drive UCB pathogenesis by targeting the m5C methylation site in the HDGF 3' untranslated region."]
- [PMID:41707999 "Mechanistically, NSUN2 installs m5C modifications on interleukin 1 beta (IL1B) mRNA."]

These studies essentially never provide orthogonal, site-resolved validation of the single
methylation site (no purified-enzyme in vitro methylation of that site, no site-mutant knock-in,
rarely a catalytically dead rescue). Given the base rate of ~1 m5C per several thousand cytosines
in mRNA and the poor agreement between mapping methods, individual site-level claims of this kind
should be treated as provisional. This does not make the enzyme's mRNA activity false; it makes
the **specific biology attributed to it** weak.

## Decision and the reusable principle

**Principle: separate the enzyme from the substrate class, and demote rather than delete.**

When a well-established enzyme is claimed to act on a second substrate class whose detection
depends on a contested assay:

1. Ask whether the *catalytic assignment* has any evidence that does not depend on the contested
   mapping assay — purified-enzyme in vitro reaction, mechanism-based covalent capture,
   catalytically dead rescue, orthogonal mass spectrometry. For NSUN2/mRNA, several of these
   exist, so the MF term stays.
2. Ask whether the *site maps and the downstream biology* have independent support. For
   NSUN2/mRNA they largely do not, so the term is marked non-core and the dispute is recorded.
3. Never `REMOVE` on this basis when the annotation carries an experimental code, because removal
   asserts the activity does not occur, which is a stronger claim than the evidence supports in
   either direction.

The mirror-image case is NSUN7 (reviewed alongside this gene): there the *enzyme itself* fails —
no cofactor binding, catalytic residue substituted, no change in product on knockout — and the
only methyltransferase annotation is an IEA. That is a `REMOVE`. The contrast is the point: the
action is driven by whether the challenge lands on the catalysis or on the substrate mapping.

## Paralog leakage in the IBA block

Three IBAs on NSUN2 look like NSUN4 functions propagated across a family-wide node
(`PANTHER:PTN000516076`). The `WITH/FROM` column of `NSUN2-goa.tsv` names `MGI:MGI:1919431`,
which is **mouse Nsun4** — the mitochondrial 12S rRNA methyltransferase that partners MTERF4 in
mitoribosome large-subunit assembly:

| IBA term | WITH/FROM | Comment |
|---|---|---|
| GO:0009383 rRNA (cytosine-C5-)-methyltransferase activity | MGI:MGI:1919431, PTN000516076 | Nsun4 substrate; NSUN2 has no reported rRNA substrate |
| GO:0006364 rRNA processing | MGI:MGI:1919431, PTN000516076 | ditto |
| GO:1902775 mitochondrial large ribosomal subunit assembly | MGI:MGI:1919431, PTN000516076 | NSUN4/MTERF4 function |

NSUN2 *is* in the mitochondrial matrix, but its job there is mt-tRNA C48-50, and the same paper
that put it there reports that its loss does not much perturb mitochondrial translation:

- [PMID:31276587 "Finally, we show that inactivation of NSUN2 does not have a profound effect on mitochondrial tRNA stability and oxidative phosphorylation in differentiated cells."]

I have marked these three `MARK_AS_OVER_ANNOTATED` with a `propagation_review` recording only what
I actually checked: the donor gene identity from the GOA `WITH/FROM` column. I did **not** inspect
the PAINT tree, so the PANTHER node is recorded as `UNRESOLVED` rather than being blamed. By
contrast the tRNA-related IBAs (`GO:0016428`, `GO:0002127`) list donors from five clades plus
NSUN2's own experimental annotation, which is the expected and correct pattern for a deeply
conserved Trm4 function, and they are accepted.

## Term-choice problem: GO:0006397 mRNA processing

Four annotations (one ARBA IEA plus three IDAs from PMID:22395603, PMID:28418038, PMID:31358969)
use `GO:0006397 mRNA processing`, whose definition covers conversion of a primary transcript into
mature mRNA — splicing, capping, polyadenylation. None of the three cited papers reports NSUN2
doing any of those: they report mRNA **stabilisation** (p16, HDGF) and nuclear **export**
(ALYREF). This is a term-choice problem, not an evidence problem, so `MODIFY` with replacements
`GO:0048255 mRNA stabilization` and `GO:0010793 regulation of mRNA export from nucleus` (the
latter is already annotated to this gene from PMID:28418038).

## Other decisions

- `GO:0005515 protein binding` (IPI, PMID:33961781, BioPlex) → `MARK_AS_OVER_ANNOTATED` per project
  guidance; a high-throughput AP-MS interaction with no named partner carries no functional content.
- `GO:0005576 extracellular region` (IEA) → `MARK_AS_OVER_ANNOTATED`. It is a subcellular-location
  mapping downstream of the exosome observation, and reads as if a nuclear/cytoplasmic RNA
  methyltransferase were secreted.
- `GO:0070062 extracellular exosome` (IDA, PMID:28341602) → `KEEP_AS_NON_CORE`; the observation is
  real ([PMID:28341602 "Both these proteins are found in exosomes secreted by HEK293 cells."]) but
  peripheral to the enzyme's function.
- `GO:0008168 methyltransferase activity` and `GO:0008173 RNA methyltransferase activity` (IEA) →
  `MODIFY` to `GO:0016428`; correct but under-specific parents where a precise child is established.
- `GO:0048820 hair follicle maturation` and `GO:2000736 regulation of stem cell differentiation`
  (ISS) → `KEEP_AS_NON_CORE`; genuine mouse phenotypes downstream of tRNA hypomodification, not
  activities of the protein.
- `GO:0036416 tRNA stabilization` (ISS) → `ACCEPT`; m5C at C48-50 protects tRNA from stress-induced
  endonucleolytic cleavage and is a direct consequence of the core activity.
- `GO:0005819 spindle` (IEA) → `KEEP_AS_NON_CORE`; reported mitotic localisation, not where the
  characterised catalysis happens.
