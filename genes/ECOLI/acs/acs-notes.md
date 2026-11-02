# acs (Escherichia coli K-12, P27550) — curation notes

**Provenance note.** No deep-research API keys are available in this container, so
`just deep-research` could not be run and no `-deep-research-<provider>.md` file exists
for this gene. The literature below was assembled by reading the cached publications in
`publications/`, by PubMed searches (PubMed MCP), and from the curated UniProt record
`acs-uniprot.txt`. This file is the research record for the review.

Curation context: this gene was reviewed for the [CACAO](../../../projects/CACAO.md)
project, which audits GO annotations carrying `assigned_by: CACAO`. acs carries four
such rows (see "CACAO rows" below).

## 1. What Acs is

Acetyl-coenzyme A synthetase (acetate--CoA ligase, AMP-forming; EC 6.2.1.1), a 652-residue
cytoplasmic member of the ATP-dependent AMP-binding (ANL) enzyme superfamily. It ligates
acetate to CoA at the expense of ATP in two half reactions through a covalently bound
acetyl-adenylate intermediate:

> "Catalyzes the conversion of acetate into acetyl-CoA (AcCoA), an essential intermediate
> at the junction of anabolic and catabolic pathways" ... "In the first half reaction, Acs
> combines acetate with ATP to form acetyl-adenylate (AcAMP) intermediate. In the second
> half reaction, it can then transfer the acetyl group from AcAMP to the sulfhydryl group
> of CoA, forming the product AcCoA"
> [file:ECOLI/acs/acs-uniprot.txt, CC:FUNCTION]

Reaction: `acetate + ATP + CoA = acetyl-CoA + AMP + diphosphate` (Rhea:RHEA:23176),
Mg(2+)-dependent, pH optimum 8.5, KM 0.2 mM acetate / 0.2 mM CoA / 0.15 mM ATP
[file:ECOLI/acs/acs-uniprot.txt, CC:CATALYTIC ACTIVITY, CC:COFACTOR,
CC:BIOPHYSICOCHEMICAL PROPERTIES].

The original enzymological identification of this activity in *E. coli* is Brown,
Jones-Mortimer & Kornberg: [PMID:21941 "An inducible acetyl-CoA synthetase [acetate: CoA
ligase (AMP-forming); EC 6.2.1.1] effects this uptake of acetate"].

## 2. Gene identification and the acetate-activation role (PMID:7751300)

Kumari *et al.* cloned the ORF, deleted it, and purified the product:

- [PMID:7751300 "we conclude that this open reading frame encodes the acetate-activating
  enzyme, Acs"]
- [PMID:7751300 "the E. coli enzyme activated acetate across a wide range of
  concentrations in a coenzyme A-dependent manner"] — the IDA basis for
  `GO:0003987 acetyl-CoA synthetase activity`.
- [PMID:7751300 "those deleted for acs grew poorly on low concentrations"] (≤10 mM
  acetate) and [PMID:7751300 "those deleted for acs, ackA, and pta did not grow on acetate
  at any concentration tested"] — the IMP basis for `GO:0045733 acetate catabolic process`.

Acs is the high-affinity (low-acetate) arm of acetate activation; AckA–Pta is the
low-affinity (high-acetate) arm. UniProt's disruption phenotype records the same split
[file:ECOLI/acs/acs-uniprot.txt, CC:DISRUPTION PHENOTYPE]. Acs is therefore a genuine
participant in acetate catabolism — it performs the committed activation step — which is
*not* the "downstream consequence of a knockout" pattern.

Transcriptionally Acs is induced by CRP and FNR in response to rising cAMP, falling
oxygen and changes in carbon flux [file:ECOLI/acs/acs-uniprot.txt, CC:INDUCTION;
PMID:10894724].

## 3. Second substrate: propionate

E. coli Acs also activates propionate, and is required for growth on it:

- [PMID:24835953 "deletion of acs in E. coli results in blockage of propionate
  utilization"]
- [PMID:24835953 "reversible acetylation also modulates the propionyl-CoA synthetase
  activity of Acs"]

Together with the EcoCyc IDA row on `GO:0050218 propionate-CoA ligase activity` from the
purified-enzyme characterization [PMID:15327942 "The enzyme exhibited characteristics
typical of prokaryotic Acs enzymes"], this makes short-chain (C2/C3) acyl-CoA ligase
activity a real, second catalytic capability rather than a stray in-vitro promiscuity.

## 4. Acs is a *substrate* of protein acetylation, and is regulated by it

This is the best-documented protein-acetylation link for Acs, and it runs the opposite
way from the CACAO rows:

- Acs Lys609 (the active-site lysine) is acetylated by the GNAT acetyltransferase
  Pat/PatZ/YfiQ, which inactivates the enzyme: [PMID:15236963 "The Pat enzyme uses
  acetyl-CoA as substrate to modify residue Lys609 of Acs"] (*Salmonella*; the
  *E. coli* orthologue PatZ is structurally characterized in [PMID:40498448]).
- The sirtuin CobB deacetylates Lys609 and thereby activates Acs; Acs and CobB form a
  1:1 complex [file:ECOLI/acs/acs-uniprot.txt, CC:PTM, CC:SUBUNIT; PMID:15019790;
  PMID:20345663].

So in the Pat/CobB axis Acs is the modified protein, not the modifier.

## 5. The CheY-acetylation claim, and why it needs hedging

A single group (Eisenbach/Wolfe and co-workers) reported that Acs acetylates the
chemotaxis response regulator CheY:

- [PMID:1390767 "Acetylated CheY was stable in the presence of the strong nucleophiles
  hydroxylamine or ethanolamine, indicative of N-acetylation"] — but note the paper's own
  title attributes the chemistry to *acetyladenylate or its derivative*, i.e. to the
  small-molecule intermediate Acs produces, not unambiguously to Acs as an enzyme.
- [PMID:15327942 "it could use either acetate or AcCoA as an acetyl donor for CheY
  acetylation"]; [PMID:15327942 "the acetylation sites of CheY are clustered at the C
  terminus of the protein, with lysine residues 91, 92, 109, 119, 122 and 126 being the
  main acetylation sites"]; [PMID:15327942 "The Acs-catalyzed acetylation of CheY was
  reversible"].
- [PMID:11359578 "The Deltaacs mutant exhibited much reduced sensitivity to chemotactic
  stimuli"] — the in-vivo chemotaxis phenotype.
- [PMID:16630631 "Like CheY acetylated by Acs, autoacetylated CheY could be deacetylated
  by Acs"] — the reverse direction, used as the basis of the CACAO
  `protein lysine deacetylase activity` row.

Three caveats, all from independent work:

1. **The Δacs chemotaxis phenotype did not replicate.** Li *et al.*, testing the same
   semi-solid-agar assay in W3110 and in the AJW613/AJW803 pair, found
   [PMID:20345663 "In contrast, the Δacs mutant was indistinguishable from the W3110
   parental strain"]. They attribute the chemotaxis effect to CobB-mediated CheY
   deacetylation instead. This directly disputes PMID:11359578 and the
   phenotype sentence in PMID:16630631.
2. **CheY is acetylated without Acs.** [PMID:16630631 "this protein is partially
   acetylated in spite of the absence of Acs, suggesting that CheY can be
   post-translationally acetylated in vivo by additional means"] — the same paper shows
   CheY autoacetylates from AcCoA at a rate comparable to the Acs-mediated rate.
3. **Most bacterial lysine acetylation is non-enzymatic.** [PMID:23830618 "AcP can
   chemically acetylate lysine residues in vitro"], and global acetylation tracks
   acetyl-phosphate levels rather than acetyltransferase activity. Since Acs makes
   acetyl-adenylate and acetyl-CoA, an Acs-dependent increase in CheY acetylation can
   arise from acyl-donor supply rather than from catalysis by Acs. The dedicated
   *E. coli* protein acetyltransferase is PatZ, not Acs [PMID:15236963; PMID:40498448].

**Mechanistic point relevant to the deacetylase term.** `GO:0033558 protein lysine
deacetylase activity` sits under `GO:0019213 deacetylase activity`, defined as
"Catalysis of the hydrolysis of an acetyl group from a substrate molecule" (OLS,
2026-10-29). Acs has no hydrolase chemistry: what PMID:15327942 and PMID:16630631
describe is the *reverse* of Acs's own acetyl-transfer reaction (acetyl group returned to
CoA/AMP), which is exactly what "reversible" means in the 2004 abstract. A reversible
transferase is annotated to the transferase term, not to a separate deacetylase term;
`GO:0061733 protein-lysine-acetyltransferase activity` is the term that covers both
directions of this one reaction.

## 6. Localization

Cytoplasmic/cytosolic. The IDA row rests on the *E. coli* cytosolic proteome
[PMID:18304323 "we identified 1103 proteins from the cytosolic fraction of the
Escherichia coli strain MC4100"]; Acs itself is named only in that paper's supplementary
abundance table, not in the cached body text, so the row is accepted on EcoCyc's reading
of the supplementary data plus the absence of any TM segment, signal peptide or membrane
feature in `acs-uniprot.txt`.

## 7. CACAO rows (four)

| GO term | Evidence | Reference | Verdict |
|---|---|---|---|
| GO:0003987 acetyl-CoA synthetase activity | IDA | PMID:7751300 | correct and core (also carried by EcoCyc on the same paper) |
| GO:0018394 peptidyl-lysine acetylation | IDA | PMID:15327942 | right paper, right assay, peripheral and donor-supply-confounded → keep as non-core |
| GO:0034421 post-translational protein acetylation | IDA | PMID:15327942 | same single experiment annotated a second time on the timing axis; the residue-specific term is the informative one |
| GO:0033558 protein lysine deacetylase activity | IDA | PMID:16630631 | claim is in the abstract, but the term's parent requires hydrolysis; this is reverse acetyl-transfer → acetyltransferase term |

GONUTS wiki check: `gowiki.tamu.edu` was still serving only the "temporarily offline"
notice on 2026-10-29 (consistent with the note in `projects/CACAO.md`), so the students'
own evidence pages for PMID:15327942, PMID:16630631 and PMID:7751300 could not be read.
All four rows were judged from the papers and the surrounding literature. Re-check when
GONUTS returns.

## 8. Open questions

- Is Acs a *bona fide* protein acetyltransferase, or does it raise CheY acetylation by
  supplying acetyl-adenylate/acetyl-CoA for non-enzymatic modification? No experiment
  separating catalysis from donor supply (e.g. a catalytically dead Acs variant that
  still produces no AcAMP vs. one that does) has been reported.
- Why do PMID:11359578 and PMID:20345663 disagree on the Δacs chemotaxis phenotype?
- Does Acs contribute measurably to propionyl-CoA formation in vivo relative to PrpE,
  and does Lys609 acetylation regulate both activities identically [PMID:24835953]?
