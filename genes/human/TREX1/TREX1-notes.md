# TREX1 (Q9NSU2) curation notes

Three-prime repair exonuclease 1 / DNase III. Human, 314 aa (displayed isoform
Q9NSU2-3). Reviewed for the [cGAS-STING project](../../../projects/CGAS_STING_PATHWAY.md)
(issue #3955), where TREX1 is the principal negative regulator of cytosolic DNA
sensing upstream of CGAS.

No deep-research provider was available in this environment
(`just deep-research human TREX1 --provider perplexity` failed: "Provider
'perplexity' not available. Available: claude_code"), so these notes are my own
literature synthesis from the cached publications and the UniProt record. They
are deliberately **not** named `-deep-research-*.md`.

## Literature search performed

Publications read for this review (all cached under `publications/`):

| PMID | full text? | what it establishes |
|---|---|---|
| 10391904 | abstract | TREX1/TREX2 cDNAs; recombinant TREX1 is a 3'→5' exonuclease; substrate preference |
| 10393201 | abstract | independent identification (DNase III) from rabbit liver nuclei; 3'-mispair proofreading in a reconstituted BER system |
| 16713580 | abstract | ATR-ATRIP recruitment to O6-meG/T by MutSα/MutLα — **not a TREX1 paper** (see source defect below) |
| 16818237 | abstract | TREX1 is a SET-complex component; acts with NME1 in granzyme-A death |
| 17293595 | abstract | crystal structure of dimeric mouse TREX1 with ssDNA and dAMP; polyproline II helix |
| 17355961 | abstract | dimeric TREX1-DNA structure; polyproline region binds the CA150 (TCERG1) WW2 domain |
| 17660820 | abstract | C-terminal truncations cause RVCL |
| 18045533 | abstract | Trex1 relocalizes from ER to S-phase nucleus; degrades ssDNA from aberrant replication intermediates |
| 18724932 | full | Trex1 is an essential negative regulator of the IFN-stimulatory-DNA response; retroelement ssDNA accumulates in Trex1-null cells |
| 23979357 | abstract | C-terminal region controls localization through ubiquitination; UBQLN1 interaction |
| 23993650 | abstract | oxidized (8-OHG) DNA resists TREX1 degradation and potentiates STING sensing |
| 25848017 | abstract | structure of TREX1 D18N with dsDNA; DNA-unwinding mechanism; D18N knock-in mice develop lupus |
| 26320659 | full | TREX1 C-terminus binds the ER OST complex (DDOST, RPN1) and restrains LLO hydrolysis; DNase-independent |
| 33476576 | full | ER-tethered TREX1 degrades DNA at ruptured micronuclei and limits cGAS activation |
| 35685777 | full | SET-complex review (cited by ComplexPortal for the granzyme row) |

Reactome entries read: `reactome/R-HSA-3244605.md` (TREX1 binds retroviral-derived
DNA), `reactome/R-HSA-3245943.md` (viral DNA cleavage by TREX1).

## Core biology

**Activity.** TREX1 is the major mammalian 3'→5' DNA exonuclease, a two-Mg(2+)
DEDDh-family enzyme (EC 3.1.11.2). It is DNA-specific: "No activity was detected
using single-stranded RNA or an RNA-DNA partial duplex" [PMID:10391904]. Activity
is highest on a recessed/mispaired 3' end — "The greatest activity of the TREX1
protein was detected using a partial duplex DNA containing five mispaired
nucleotides at the 3' terminus" [PMID:10391904] — but dsDNA is also a genuine
substrate: the D18N–dsDNA structure reveals "a novel DNA-unwinding mechanism to
separate the polynucleotide strands for single-stranded DNA (ssDNA) loading into
the active site", and the authors conclude "these data point to dsDNA as a key
substrate for TREX1" [PMID:25848017]. Catalysis requires two Mg(2+) per subunit
(UniProt COFACTOR, by similarity to mouse Q91XB0) with Asp18, Glu20, His195 and
Asp200 forming the active site.

**Quaternary structure.** An obligate homodimer; both the mouse and human
structures are dimers [PMID:17293595; PMID:17355961], and 12 PDB entries for the
human nuclease domain (7TQN–9O0Y) are dimeric or higher-order assemblies.

**Localization.** The steady-state pool is tail-anchored in the ER membrane with
the nuclease domain facing the cytosol: "TREX1 possesses a single-pass
transmembrane helix at its C-terminus that anchors the protein in the ER and
positions the nuclease domain in the cytosol" [PMID:33476576]. Deleting the
C-terminal 79 residues gives pancellular distribution. A second, regulated pool
translocates into the nucleus: after γ-irradiation or hydroxyurea, "Trex1,
ordinarily associated with the endoplasmic reticulum (ER), relocalizes to the S
phase nucleus" [PMID:18045533], and during granzyme-A death it moves with the SET
complex [PMID:16818237]. The original purification was from "a widely distributed
DNA-specific 3' exonuclease from rabbit liver nuclei" [PMID:10393201], which is
why the oldest annotations are nuclear.

**Principal biological role — restraining cGAS.** TREX1 removes cytosolic DNA
before cGAS can sense it. Loss of Trex1 allows single-stranded DNA from
endogenous retroelements to accumulate: "We show that single-stranded DNA derived
from endogenous retroelements accumulates in Trex1-deficient cells, and that
Trex1 can metabolize reverse-transcribed DNA", and "We define Trex1 as an
essential negative regulator of the ISD response" [PMID:18724932]. The mechanism
at micronuclei is the best-resolved case: "the endoplasmic reticulum
(ER)-associated nuclease TREX1 inhibits cGAS activation at micronuclei by
degrading micronuclear DNA upon micronuclear envelope rupture" [PMID:33476576].
That paper supplies the two human IDA rows in GOA: nucleolytic activity is
required ("indicating that TREX1 nucleolytic activity is necessary to inhibit
cGAS activation in chromosomally unstable cells"), ER tethering is required
("GFP-TREX1 was present at approximately 75% of ruptured MN, while GFP-TREX1ΔC
was never present at MN"), and the readout is interferon ("expression of IFNB1,
ISG56, IFI44, IFIT2, and other Interferon-Stimulated Genes (ISGs) was elevated in
TREX1 KO cells after Mps1 inhibition").

Substrate escape is a regulatory axis in its own right: oxidative damage makes
DNA a poor TREX1 substrate — "The oxidized base 8-hydroxyguanosine (8-OHG), a
marker of oxidative damage in DNA, potentiated cytosolic immune recognition by
decreasing its susceptibility to 3' repair exonuclease 1 (TREX1)-mediated
degradation" [PMID:23993650] — which UniProt links to the photosensitivity of
lupus skin lesions.

**A second, DNase-independent function at the ER.** The C-terminus restrains the
oligosaccharyltransferase complex: "the TREX1 C terminus suppressed immune
activation by interacting with the ER oligosaccharyltransferase (OST) complex and
stabilizing its catalytic integrity", with co-IPs showing "strong interactions
between TREX1 and two subunits, DDOST and RPN1, but failed to detect interaction
with two other subunits, RPN2 and STT3A" [PMID:26320659]. Catalysis is not
involved: ER-localized but nuclease-dead D18N rescues free-glycan accumulation,
"showing that DNase activity is dispensable for TREX1 to suppress free glycan
accumulation" [PMID:26320659]. This is the mechanism proposed for RVCL, where
frameshifts remove the C-terminus but leave the DNase active [PMID:17660820].

**Granzyme-A cell death.** TREX1 is a bona fide SET-complex subunit — "We now
find the 3'-to-5' exonuclease TREX1, but not its close homolog TREX2, in the SET
complex" — and functions as the exonuclease arm of DNA destruction: "After
granzyme A activates NM23-H1 to make single-stranded nicks, TREX1 removes
nucleotides from the nicked 3' end to reduce the possibility of repair by
rejoining the nicked ends" [PMID:16818237]. ComplexPortal records the complex as
CPX-26715.

**Disease.** Biallelic DNase-inactivating variants cause Aicardi-Goutières
syndrome 1; heterozygous variants cause familial chilblain lupus and SLE
susceptibility; C-terminal frameshifts cause retinal vasculopathy with cerebral
leukoencephalopathy (RVCL). The genotype-mechanism split (DNase domain → self-DNA
interferonopathy; C-terminus → OST/ER) is the clinically useful reading.

## Annotation decisions of note

**ATRIP mis-attribution (source defect).** GOA carries two MGI IDA rows on human
TREX1 from PMID:16713580 — GO:0032405 MutLalpha complex binding and GO:0032407
MutSalpha complex binding. That paper is about ATR–ATRIP: "ATR-ATRIP, but not RPA,
is preferentially recruited to O(6)-meG/T mismatches in a MutSalpha- and
MutLalpha-dependent manner" [PMID:16713580]; TREX1 does not appear in it. Three
independent checks point to ATRIP:

1. UniProt itself flags the locus: "The gene for this protein is either identical
   to or adjacent to that of ATRIP. Some of the mRNAs that encode ATRIP also
   encode TREX1 in another reading frame." (`CC:CAUTION`).
2. A QuickGO query (2026-11-03) for GO:0032407 in human returns seven rows; the
   two from PMID:16713580 are on ATR and TREX1. ATR is correct. Human ATRIP
   (Q8WXE1) has **no** annotation from this paper, which is the gene the paper
   actually assays alongside ATR.
3. There is no literature placing TREX1 in MutSα/MutLα complexes.

Recorded as `source_defects` (WRONG_GENE_PRODUCT, MGI, TREX1 → ATRIP,
cause SEQUENCE_MISMAPPING, confidence PROBABLE — the abstract, not the full text,
was available). Both rows are REMOVEd.

**OST complex membership.** GO:0008250 oligosaccharyltransferase complex is
annotated `part_of` (human IEA from the mouse MGI IDA on PMID:26320659). The
evidence is an interaction with two subunits via the TREX1 C-terminus, not
stoichiometric membership in a 7–8 subunit catalytic complex, so this is MODIFYed
to GO:0062062 oligosaccharyltransferase complex binding, which exists and says
exactly what the paper shows.

**NAS rows from PMID:10391904.** UniProt took DNA replication (GO:0006260),
mismatch repair (GO:0006298) and DNA recombination (GO:0006310) from that
paper's closing sentence: "provides the genetic tools to investigate the
physiological roles of these exonucleases in mammalian DNA replication, repair,
and recombination pathways". That is a statement of intent, not a result; all
three are marked over-annotated. The same paper's nuclear-envelope NAS row is not
supported by anything in its abstract either, and TREX1's membrane pool is the ER
membrane (continuous with the outer nuclear membrane), already captured by
GO:0005789.

**GO:0045824 vs GO:0160049.** Both come from PMID:33476576 IDA, and it is
tempting to treat the general one as subsumed. It is not: GO:0160049 negative
regulation of cGAS/STING signaling pathway sits under GO:0039532 (negative
regulation of cytoplasmic pattern recognition receptor signaling pathway) and
GO:0045088, and GO:0045824 negative regulation of innate immune response is
**not** among its ancestors (checked against QuickGO, 2026-11-03). The two rows
are complementary and both are accepted.

**UniProt topology discrepancy.** UniProt records the ER-membrane location as
"Peripheral membrane protein" and carries no TRANSMEM feature, while the paper it
cites for that location states a "single-pass transmembrane helix at its
C-terminus" [PMID:33476576], and the OST paper uses a "TREX1_TM" truncation
throughout [PMID:26320659]. Recorded as a SUSPECTED source defect against UniProt
with `requested_change: CHECK` rather than asserted as fact, since the peripheral
vs. single-pass question is genuinely contested in the literature.

**Ontology gap: the mammalian micronucleus.** GO:0031040 micronucleus is defined
for ciliate germline nuclei and cannot be used for the chromosome
mis-segregation-derived micronucleus where TREX1 and CGAS act. Proposed as a new
CC term; no annotation uses a wrong id in the interim.

## Open questions

- Which substrate pool dominates in a normal, chromosomally stable cell:
  retroelement cDNA, replication-derived ssDNA, or micronuclear DNA? The three
  are established separately, never quantified against each other.
- How does the TREX1 C-terminus bias OST toward transfer over hydrolysis? The
  authors leave this open ("with a yet to be identified role in ER biology that
  may be the underlying cause of RVCL" [PMID:26320659]).
- Is TREX1 a peripheral or an integral single-pass ER membrane protein?
