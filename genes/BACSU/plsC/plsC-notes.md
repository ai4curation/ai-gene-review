# plsC (yhdO, BSU09540; UniProt O07584) — review notes

Part of projects/LIPID_DIVIDE.md (Part B, acyltransferases that accept both enantiomers).

## Sources and search record (2026-11-02)

- No deep-research provider key was available, so no `plsC-deep-research-<provider>.md` was generated.
- `just mod-description-deep-research BACSU plsC` was run: skipped, "no MOD provider configured for organism 'BACSU'".
- Read: PMID:42286214 (Rieche 2026, full text), PMID:17645809 (Yoshimura 2007, full text), PMID:17557823
  (Paoletti 2007, abstract), PMID:15743965 (Nishibori 2005, abstract), the UniProt record, and the committed
  PAINT slice `interpro/panther/PTHR10434/PTHR10434-paint.tsv` plus `PTHR10434-review.yaml`.
- PubMed searches as for plsY; newly cached PMID:35767906 (Palyzová 2022) and PMID:12682299 (Kobayashi 2003),
  both abstract-only.
- Paralog check: UniProt REST query `taxonomy_id:224308 AND xref:pfam-PF01553` returns exactly one protein,
  O07584 (PlsC). So B. subtilis 168 has no second PlsC/AGPAT-family acyltransferase. Combined with the
  phenotype (below) PlsC is the only LPAAT of this organism for phospholipid synthesis. (A non-homologous
  LPAAT cannot be excluded by a domain query alone, but the mutant phenotype leaves no room for one.)

## Function: 1-acyl-G3P (LPA) acyltransferase using acyl-ACP

- Second acylation of PA synthesis: [PMID:42286214 "Subsequently, 1-acyl-sn-glycerol-3-phosphate acyltransferase
  PlsC, belonging to the lysophosphatidic acid acyltransferases (LPAAT) family, catalyzes the attachment of a
  second activated fatty acid to the sn-2 position of the glycerol-phosphate backbone, thereby, converting
  lysophosphatidic acid (LPA) into phosphatidic acid (PA)"].
- Donor specificity: B. subtilis PlsC uses acyl-ACP and not acyl-CoA [PMID:17557823 "whereas PlsC used only
  acyl-ACP as an acyl donor"]; UniProt catalytic activity is written with fatty acyl-[ACP] (Rhea:42296,
  EC 2.3.1.n4, i.e. no official EC number yet). This matters for GO: `GO:0003841` is defined with acyl-CoA as
  donor, and GO already distinguishes donors in the preceding step (`GO:0004366` acyl-CoA GPAT vs `GO:0043772`
  acyl-phosphate GPAT). So the IBA/IEA rows carry a donor-mismatched definition, while the term name is
  donor-neutral and is universal GOA practice for bacterial PlsC. Recorded as an ontology proposal and a
  suggested question rather than by rewriting the annotation.
- Essentiality / sole LPAAT: plsC (yhdO) is in the indispensable set [PMID:17645809 "we showed that 271 genes,
  including plsC (yhdO) and plsX, when inactivated singly, were indispensable for growth in LB medium [10]"]
  (citing Kobayashi 2003, PMID:12682299). A plsC-ts strain accumulates its substrate and stops making
  phospholipid [PMID:17645809 "At the restrictive temperature, however, 1-acyl-G3P accumulation was observed,
  and phospholipid synthesis did not take place (Figure 3B)."]; depletion gives the same result with fatty-acid
  overflow [PMID:17557823 "Phospholipid synthesis ceased following PlsC depletion"].
- Catalytic motif: UniProt FT MOTIF 39..44 HXXXXD, "essential for acyltransferase activity" (ECO:0000250, i.e.
  by similarity, not measured here).

## Location

- UniProt: cell membrane (ECO:0000305), with "Localized in the septal membrane" (ECO:0000269, PMID:15743965).
- The GFP-fusion survey places the lipid synthases, including 1-acyl-glycerol-3-phosphate acyltransferase, in
  septal membranes [PMID:15743965 "The majority of the lipid synthases were also localized in the septal
  membranes; this includes 1-acyl-glycerol-3-phosphate acyltransferase"]. There is no transmembrane feature in
  the entry: PlsC-family enzymes are monotopic/peripheral membrane enzymes, so "membrane" (GO:0016020) is less
  informative than plasma membrane here, and the division-site localization is a real extra claim not in GOA.

## The IBA from the PTHR10434 node

- `PANTHER:PTN000046632` seeds (committed PAINT slice, 20250902): AGI_LocusCode:AT4G30580, MGI:1914762,
  MGI:1932075, SGD:S000002210, UniProtKB:O15120, UniProtKB:P26647, UniProtKB:Q381S0, UniProtKB:Q99943.
  P26647 is *E. coli* PlsC, so the node is not eukaryote-only: it spans bacteria and eukaryotes, which is what
  an ancestral LPAAT node should do, and the B. subtilis enzyme sits inside that clade with the same HXXXXD
  chemistry and the same reaction. The repository's own family review marks both this node's F and P assertions
  SOUND. Donor count is irrelevant; the node placement is the question, and it holds.
  [file:interpro/panther/PTHR10434/PTHR10434-paint.tsv]
- The GO:0006654 IBA at the same node is seeded by MGI:1932075, O15120, P26647, Q99943 — again including EcPlsC.

## Stereochemistry

- BsPlsC acylates both (R)- and (S)-LPA in the coupled liposome assay, with significantly more (R)-PA formed
  [PMID:42286214 "Our data shows that both the E."; "Interestingly, both PlsC proteins appear to synthesize more
  (R)-configurated PA than the other stereoform, suggesting that LPA containing the G3P backbone is the preferred
  substrate."]. The authors themselves caveat the (S) result: [PMID:42286214 "Although this seems to indicate
  that BsPlsC prefers (R)-LPA as substrate, we cannot rule out this result is partially impacted by the lower
  availability of (S)-LPA."] — (S)-LPA is not commercially available and had to be generated in situ by PlsY, so
  substrate supply and enzyme preference are confounded, and no kinetics exist
  [PMID:42286214 "The current in vitro system is, however, unsuitable for such analysis, due to the coupling of
  enzymes."].

### Judgement (in vivo vs promiscuity): more cautious than for PlsY

PlsC's (S)-LPA activity is one tier weaker as evidence than PlsY's G1P activity:

1. It was never measured on a defined (S)-LPA substrate; (S)-LPA was made in situ by PlsY, so its concentration
   was both lower and unknown.
2. The only quantitative comparison (significantly less (S)-PA) is confounded by that supply difference.
3. Unlike PlsY, which was also assayed in detergent with both enantiomers supplied directly, PlsC has no
   assay in which the two substrates were equally available.

If the heterochiral lipids of B. subtilis are real, PlsC must handle (S)-LPA, because it is the organism's only
LPAAT and (S)-LPA would otherwise be a dead end (a point that follows from the single-LPAAT genetics, not from an
experiment). That makes the inference structurally the same as for PlsY but with weaker direct support. So: no
`NEW` annotation, no core function for the (S) reaction, and no separate proposed term for it in this review —
the plsY review's proposed G1P term carries the paired ontology request, and the PlsC half is recorded there and
as a knowledge gap here. Treating it as mere promiscuity would also be wrong: the activity is on the direct
pathway of this organism's only LPAAT, not a side reaction of a paralog.

## GOA rows (8)

- GO:0003841 IBA and IEA: ACCEPT (correct reaction; donor-definition mismatch noted, PAINT node spans bacteria).
- GO:0006654 IBA: ACCEPT (core process).
- GO:0005886 IEA: ACCEPT; GO:0016020 IEA: MODIFY to GO:0005886.
- GO:0006644 IEA, GO:0008654 IEA: MODIFY to GO:0006654.
- GO:0016746 IEA: MODIFY to GO:0003841 (true but entailed by the specific term).
- NEW: GO:0032153 cell division site (IDA, PMID:15743965), septal-membrane localization of the enzyme.
