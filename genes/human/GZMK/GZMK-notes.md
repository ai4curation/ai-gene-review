# GZMK (granzyme K, UniProtKB:P49863) — curation notes

## Provenance of this file

No `-deep-research-*.md` file exists for GZMK. `just deep-research-falcon human GZMK` failed
immediately (`ERROR - Provider 'falcon' not available. Available: openscientist, claude_code`), and
`just deep-research human GZMK --provider openscientist` was then started and ran for about fifty
minutes without producing output before it was stopped by the session's background limit (exit 143).
No provider file was written, and this file is deliberately **not** named as one. These are my own
notes from the cached publications, the UniProt record, QuickGO and OLS. Every assertion carries its
source.

## What the protein is

A tryptase-like serine protease of CD8 T cells, cleaving after arginine. It and granzyme A are the
only two tryptic granzymes [PMID:19059912 "GrK is similar to GrA in that they are the only granzymes
that display tryptase-like activity"], and they are not redundant: the two cleave SET at similar
sites but differ on hnRNP K, and granzyme K alone cuts beta-tubulin, after two distinct arginines
[PMID:19059912 "GrK, but not GrA, cleaved the microtubule network protein beta-tubulin after two
distinct Arg residues"]. The same paper found no clear consensus around P1 and concluded that
specificity comes from exosite contacts, which is worth holding onto: it explains how one tryptase
can select substrates as unalike as beta-tubulin, a protease-activated receptor and complement C2.

## The two arms, and which one the record should lead with

**Intracellular, cytotoxic.** Delivered through the perforin pore, granzyme K cleaves Bid to tBid,
breaching the outer mitochondrial membrane so that cytochrome c and endonuclease G are released; the
death is caspase-independent and involves reactive oxygen species [PMID:17308307 "GzmK targets
mitochondria by cleaving Bid to generate its active form tBid, which disrupts the outer mitochondrial
membrane leading to the release of cytochrome c and endonuclease G"].

**Extracellular, pro-inflammatory.** This is where the protein's documented importance now lies.

- *Complement.* GZMK cleaves C2 and C4; the C4b and C2b fragments assemble a C3 convertase, which
  runs the cascade to C3a, C5a, C4b, C3b and the membrane attack complex [PMID:39914456 "we show that
  GZMK can activate the complement cascade by cleaving the C2 and C4 proteins"]. It binds membranes
  first, through heparan sulfate, which is why the convertases form on surfaces rather than in the
  fluid phase [PMID:39914456 "GZMK directly binds to plasma membranes to trigger formation of
  membrane-bound C3 convertases and to elicit efficient opsonization of target surfaces"]. In vivo,
  `Gzmk`-null mice are protected from arthritis and dermatitis [PMID:39914456 "Gzmk-deficient mice are
  significantly protected from inflammatory disease, exhibiting reduced arthritis and dermatitis, with
  concomitant decreases in complement activation"]. The airway study independently reports cleavage of
  C2, C3, C4 and C5 and shows the asthma phenotype depends on the proteolysis [PMID:39814882].
- *Protease-activated receptors.* GZMK cleaves PAR1 and PAR2 at the canonical arginine through exosite
  interactions, signalling via beta-arrestin and ERK rather than a calcium flux, and releasing IL-6 and
  IL-8 [PMID:35881628 "GzmK and, to a lesser extent the related protease GzmA, are capable of
  activating PAR1 and PAR2"]. PAR1 is required for the IL-6, IL-8 and MCP-1 release from lung
  fibroblasts [PMID:21760880 "PAR-1 is essential for GrK-induced IL-6, IL-8 and MCP-1 release"].
- *LPS, with no catalysis at all.* GZMK binds Gram-negative bacteria and LPS, disaggregates LPS
  micelles and augments LPS-CD14 complex formation [PMID:24711407 "we show that granzyme K (GrK) binds
  to Gram-negative bacteria and their cell-wall component lipopolysaccharide (LPS)"], and the effect is
  independent of catalytic activity [PMID:24711407 "these extracellular effects are independent of GrK
  catalytic activity"]. This is the one part of the protein's function that its molecular-function
  annotations cannot express, since all of them are about proteolysis.

The authors of the receptor work state the shift explicitly [PMID:35881628 "These data suggest that
during an immune response GzmK acts as a pro-inflammatory regulator, rather than as a cytotoxin"].
That is why this review marks the two death-signalling rows (`GO:0090200`, `GO:0140507`) non-core
while accepting the complement and inflammation rows as core.

## The UniProt sentence that two GO rows rest on

UniProt's `CC:FUNCTION` says GZMK "First acts as a pattern recognition receptor, which specifically
recognizes and binds heparan sulfate glycosaminoglycans on the pathogen surface to drive opsonization
(PubMed:39914456)". Checked against the full text of that paper, which is cached:

- Heparan sulfate glycosaminoglycans are **host** molecules. Bacteria do not display them. The paper's
  binding experiments are on human endothelial cells, synovial fibroblasts and THP-1 monocytes
  [PMID:39914456 "we found abundant GZMK on the surface of nearly 100% of the cells"].
- The paper's only mention of pattern recognition receptors is background about the **soluble**
  receptors that initiate the classical and lectin pathways, which the authors contrast with GZMK.
- Counting occurrences across the whole text: "pathogen" appears six times, twice inside "disease
  pathogenesis", once as "pathogenesis", and three times in the mouse housing description
  ("pathogen-free housing"). No LPS. No microbe is assayed.

So the sentence looks like a conflation of this paper with PMID:24711407, which is cited elsewhere in
the same FUNCTION block and which does show bacterial and LPS binding. Recorded as a `WRONG_STATEMENT`
source defect against UniProt at `PROBABLE` with `requested_change: CHECK`, on the `GO:0038187` row.

Consequences for two GOA rows, both cited to PMID:39914456:

- `GO:0038187` pattern recognition receptor activity. The term requires combining with a PAMP. The
  *claim* is true of GZMK — LPS is the canonical PAMP and GZMK binds it — but the *cited paper* does
  not support it. Row kept, support re-pointed to PMID:24711407.
- `GO:0106139` symbiont cell surface. Same shape. The term is carried properly by the LPS paper's row;
  the complement paper's row is kept for consistency with its support re-pointed.

## Comparator checks run for this review

Both were run by term id with a verified positive control, following the ruling added to `CLAUDE.md`
after the GZMB false negative.

| Question | Result |
|---|---|
| Should `GO:0070493` thrombin-activated receptor signaling pathway be proposed, since GZMK activates PAR1? | **No.** The definition is "initiated by thrombin binding to its receptor". Thrombin itself carries the term (2 IDA rows), so the query returns positives and the convention admits the activating protease — but GZMK is not thrombin. |
| Should `GO:0032755`/`GO:0032757` (positive regulation of IL-6/IL-8 production) be proposed? | **No.** Thrombin, the closest same-role comparator, carries neither (0 hits each), nor `GO:0050729`. For receptor-activating proteases GO annotates the receptor (`F2RL1` carries `GO:0032757`) and the downstream signalling, not the protease. |
| Is `GO:0044194` cytolytic granule a real gap? | **Yes.** PRF1, GZMA, GZMB, GZMH and GNLY all carry it in their own GOA files; GZMK and GZMM do not. Proposed as `NEW` for both, from each gene's own purification paper. |

## Ontology observation worth raising

`GO:0160257` complement activation, GZMK pathway is defined as a pathway "which allows for the direct
killing of microbes and the regulation of other immune processes". Neither paper behind the term shows
microbial killing: both are disease studies, and the knockout phenotype is protection from
inflammation. The definition may be describing complement in general rather than what was demonstrated
for this pathway. Raised as a `suggested_questions` entry rather than asserted as a defect.

## Reference-level problems flagged

- `PMID:39914456` — `VERIFIED` overall, but the wrong support for the `GO:0038187` and one `GO:0106139`
  row, as above. Read in full for this review.
- `PMID:3262682` — the 1988 esterase purification. GOA cites it for `GO:0005576` extracellular region,
  but what the paper reports is the opposite end of the journey [PMID:3262682 "The esterase activity,
  localized in the cytoplasmic granules, was purified and characterized."]. It is the right support for
  the proposed cytolytic granule row and a poor fit for the one it currently carries.
