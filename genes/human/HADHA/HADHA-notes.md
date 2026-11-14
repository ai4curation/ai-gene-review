# HADHA (P40939) Review Notes

Gene: HADHA (HGNC), UniProt P40939, "Trifunctional enzyme subunit alpha, mitochondrial"
(ECHA_HUMAN). Synonym HADH; AltName "78 kDa gastrin-binding protein", "TP-alpha".

## Core identity / function

HADHA is the alpha subunit of the mitochondrial trifunctional protein (MTP/TFP), an
alpha2-beta2 heterotetramer with HADHB. The alpha subunit carries TWO of the three
catalytic activities of long-chain fatty acid beta-oxidation:
- Long-chain enoyl-CoA hydratase (LCEH), EC 4.2.1.17 (step 2 of each cycle)
- Long-chain 3-hydroxyacyl-CoA dehydrogenase (LCHAD), EC 1.1.1.211 (step 3)
The beta subunit (HADHB) carries the 3-ketoacyl-CoA thiolase (step 4).

[UniProt P40939 DE: "Includes: RecName: Full=Long-chain enoyl-CoA hydratase; Short=LCEH;
EC=4.2.1.17" and "RecName: Full=Long chain 3-hydroxyacyl-CoA dehydrogenase; Short=LCHAD;
EC=1.1.1.211"]

[UniProt FUNCTION: "the trifunctional enzyme subunit alpha/HADHA described here carries the
2,3-enoyl-CoA hydratase and the 3-hydroxyacyl-CoA dehydrogenase activities while the
trifunctional enzyme subunit beta/HADHB bears the 3-ketoacyl-CoA thiolase activity"]

## Key experimental evidence

Subunit-specific activity assignment — the definitive paper:
[PMID:8135828 "Expression of this cDNA in mammalian cells yielded a polypeptide with the
long-chain enoyl-CoA hydratase and long-chain 3-hydroxyacyl-CoA dehydrogenase activities."
(alpha-subunit); and beta-subunit cDNA "yielded a polypeptide with the long-chain
3-ketoacyl-CoA thiolase activity."] This is the basis for assigning hydratase+dehydrogenase
to HADHA and thiolase to HADHB.

Original multifunctional-enzyme characterization (whole complex, did not separate subunit
activities; full_text_unavailable):
[PMID:1550553 "In addition to 3-hydroxyacyl-CoA dehydrogenase activity, the enzyme possesses
2-enoyl-CoA hydratase and 3-ketoacyl-CoA thiolase activities which cannot be separated from
the dehydrogenase."] Also: "gives maximum activity with 3-ketoacyl-CoA substrates of C10 to
C16 acyl-chain length" — long-chain specificity.

Catalytic heterogeneity in patient enzymes (full_text_unavailable):
[PMID:8163672 "We examined the enzyme protein and biosynthesis of human trifunctional protein
harboring enoyl-CoA hydratase, 3-hydroxyacyl-CoA dehydrogenase, and 3-ketoacyl-CoA thiolase
activity in cultured skin fibroblasts from two patients with long-chain 3-hydroxyacyl-CoA
dehydrogenase deficiency."]

## Structure / complex / localization

Cryo-EM (full_text_unavailable):
[PMID:29915090 "The mitochondrial trifunctional protein (TFP) catalyzes three reactions in
the fatty acid beta-oxidation process." / "Here we report a 4.2-Å cryo-electron microscopy
α2β2 tetrameric structure of the human TFP." / "A concave surface of the TFP tetramer
interacts with the detergent molecules in the structure, suggesting that this region is
involved in associating with the membrane."]

Crystal structure / metabolon, places active sites (full_text_unavailable):
[PMID:30850536 "Membrane-bound mitochondrial trifunctional protein (TFP) catalyzes
β-oxidation of long chain fatty acyl-CoAs, employing 2-enoyl-CoA hydratase (ECH),
3-hydroxyl-CoA dehydrogenase (HAD), and 3-ketothiolase (KT) activities consecutively." /
"The biological unit of the protein is α2β2" / "two α-subunits are bound to each side of the
β2 dimer, creating an arc, which binds on its concave side to the mitochondrial
innermembrane." / "The catalytic residues in all three active sites are arranged similarly to
those of the corresponding, soluble monofunctional enzymes."] ECH and HAD active sites are in
the alpha subunit; KT in beta.

These two structural papers and ComplexPortal support: located_in mitochondrial inner
membrane (GO:0005743) and part_of mitochondrial fatty acid beta-oxidation multienzyme complex
(GO:0016507).

## Cardiolipin remodeling (independent moonlighting activity of alpha alone)

[PMID:23152787 "We previously identified a human monolysocardiolipin acyltransferase activity
which remodels CL via acylation of monolysocardiolipin (MLCL) to CL and was identical to the
alpha subunit of trifunctional protein (αTFP) lacking the first 227 amino acids." / "Purified
human recombinant αTFP exhibited acyl-CoA acyltransferase activity in the acylation of MLCL to
CL with linoleoyl-CoA, oleoyl-CoA and palmitoyl-CoA as substrates." / "we provide a link
between mitochondrial β-oxidation and CL remodeling."] Supports GO:0035965 cardiolipin
acyl-chain remodeling (IDA). UniProt assigns EC=2.3.1.- (MLCL acyltransferase) on ECO:0000305.

iPSC cardiomyocyte model confirms requirement for both BOTH beta-oxidation and CL remodeling:
[PMID:31604922 "HADHA (tri-functional protein alpha), a monolysocardiolipin
acyltransferase-like enzyme, is required for fatty acid beta-oxidation and cardiolipin
remodeling, essential for functional mitochondria in human cardiomyocytes."] Supports
GO:0006635 (IMP) and GO:0035965 (IMP).

## Questionable / over-annotations identified

1. GO:0052816 "long-chain fatty acyl-CoA hydrolase activity" IDA / PMID:22586271. The cited
   paper (full_text_available: true) is about the Hotdog-fold thioesterase Them5/Acot15 and
   makes NO mention of HADHA/TFP/P40939 anywhere in the abstract or full text. This is a
   wrong-paper attribution; HADHA is not a thioesterase. -> REMOVE; reference flagged
   WRONG_IDENTIFIER/MISCITED for this claim.
   [PMID:22586271 abstract is entirely about: "a new mammalian mitochondrial thioesterase,
   Them5"; "Them5 shows strong thioesterase activity with long-chain acyl-CoAs."]

2. GO:0003985 "acetyl-CoA C-acetyltransferase activity" TAS / PMID:8135828. This is the
   THIOLASE activity, which PMID:8135828 explicitly localizes to the BETA subunit (HADHB),
   NOT the alpha subunit (HADHA). An old PINC annotation that incorrectly attributes a beta
   activity to alpha. -> REMOVE (contradicted by the very paper cited and by structure).

3. GO:0003857 "(3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity" — this is correct for
   HADHA (the dehydrogenase). But the more specific GO:0016509 "long-chain (3S)-3-hydroxyacyl-
   CoA dehydrogenase (NAD+) activity" is preferred because HADHA is long-chain specific.

4. GO:0018812 "3-hydroxyacyl-CoA dehydratase activity" (EXP, PMID:1550553/8135828; and IEA
   RHEA). NOTE: this term is the trans-2-enoyl-CoA hydratase reaction (RHEA:16105) which is
   the SAME reaction as enoyl-CoA hydratase (GO:0004300). The "dehydratase" framing is the
   reverse direction. This is the alpha hydratase activity; correct in essence but
   GO:0004300 (enoyl-CoA hydratase activity) is the conventional MF term. Treat the
   GO:0018812 entries as MODIFY -> GO:0004300, or KEEP_AS_NON_CORE since it captures the same
   reaction. I will MODIFY to enoyl-CoA hydratase.

5. GO:0042645 "mitochondrial nucleoid" IDA / PMID:18063578. The paper found metabolic
   proteins in native nucleoid preps but they did NOT cross-link to mtDNA (peripheral
   association). Keep as non-core. [PMID:18063578 "Several other metabolic proteins and
   chaperones identified in native nucleoids, including ATAD3, were not observed to
   cross-link to mtDNA."]

6. protein binding (GO:0005515) x7 IPI — generic; KEEP_AS_NON_CORE per curation guidelines
   (avoid endorsing bare protein binding as core). Partners include P55084 (HADHB, the
   obligate complex partner; PMID:28514442, 29915090, 30850536, 33961781, 40205054) and
   autophagy/interactome partners (PMID:20562859, 32814053).

## Disease

HADHA deficiency causes isolated LCHAD deficiency and generalized MTP deficiency:
hypoketotic hypoglycemia, cardiomyopathy, peripheral neuropathy, pigmentary retinopathy;
maternal HELLP/AFLP (acute fatty liver of pregnancy) when carrying an affected fetus. The
common mutation is E510Q (Glu510Gln) [UniProt VARIANT LCHAD DEFICIENCY GLN-510; PMID:7811722,
PMID:7846063]. Disease relationships are background, not GO MF/BP/CC annotations.

## Core function conclusion

Two MF core functions for HADHA:
- GO:0004300 enoyl-CoA hydratase activity (LCEH, EC 4.2.1.17)
- GO:0016509 long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity (LCHAD, EC 1.1.1.211)
Both: directly_involved_in GO:0006635 fatty acid beta-oxidation; locations GO:0005743
mitochondrial inner membrane; in_complex GO:0016507.
A third, independent (subunit-beta-independent) activity: monolysocardiolipin acyltransferase
in cardiolipin remodeling (GO:0035965), arguably a secondary/non-core but well-supported
moonlighting function.


## 2026-11-11: evidence and annotation-context audit

This audit supersedes the earlier restrictive chain-length, reaction-direction,
wrong-paper and HADHA-specific DNA-crosslink claims above; the original notes
and 2026-11-10 history are preserved as provenance.

- Fresh native GOA seeding retains 60 contexts, including four distinct
  PMID:20562859 ATG8-family partners previously collapsed into one context.
- PMID:1550553 reports C6-and-longer activity and maximal measured dehydrogenase
  activity at C10-C16, not a strict C10-C16 substrate boundary. QuickGO defines
  GO:0018812 under GO:0004300; both use dehydration equations. Valid parent
  terms, NAD+ binding and broad mitochondrial location remain core assertions.
- Keep the HADHA thiolase REMOVE on subunit-specific experimental grounds;
  GO:0003985 has a C4 reaction scope and should not be mechanically reassigned
  to the long-chain thiolase HADHB.
- Set the GO:0052816/PMID:22586271 annotation to UNDECIDED. The original main
  text was inspected, but the complete supplement could not be read. The
  partial cache's full-text flag did not justify the earlier universal-absence
  or wrong-gene claims. GO-CAM 67b1629100002092 repeats this hydrolase assertion
  with tetralinoleoyl cardiolipin as output; ask the curator to reconcile the
  activity, reference and output mapping rather than declaring a repair.
- PMID:23152787 assays full-length recombinant HADHA separately from truncated
  MLCLAT1. Figure 2 favors linoleoyl-CoA, despite native UniProt prose favoring
  oleoyl-CoA. The native record is unchanged. GO:0071617 better describes this
  core MLCL acyltransferase chemistry; no NEW annotation is added. The broader
  term does not imply activity on other tested lysophospholipids.
- PMID:22453275 provides positive human HEK293T purification/SILAC evidence for
  nucleoid association, without proving HADHA DNA binding or a nucleic-acid
  function. Retain non-core association and original PMID:18063578 provenance.
- PMID:8651282 is present in the retained cache; the older absence note is stale.
  Other target-specific supplemental proteomics assertions not inspected are
  explicitly distinguished from independently supported location/binding.

See HADHA-deep-research-manual.md for primary-source links, access limits and
provider failure details. The draft has 47 ACCEPT, 11 KEEP_AS_NON_CORE,
1 REMOVE and 1 UNDECIDED; all 28 inherited quotations are preserved.


## PR #6313 review follow-up — 2026-11-11

Refine nine broad MF rows with MODIFY to the supported specific activities: GO:0004300 → GO:0018812 (four contexts); GO:0003857, GO:0016491 and GO:0016616 → GO:0016509 (four contexts); GO:0003824 → all three supported catalytic activities. The hydratase core uses GO:0018812 with explicit physiological reverse-hydration semantics. This does not deny the broader chemistry or measured medium-chain activity. Retain the informative pathway-level fatty acid metabolic process and root mitochondrial locations; neither needs to be demoted simply because a more specific process or compartment is also known.

Propose one NEW GO:0071617 molecular-function annotation, supported by direct full-length recombinant HADHA MLCL acylation in PMID:23152787. This fills a distinct catalytic branch, not a new process claim inferred from necessity or a missing database row. Keep donor and acceptor limits explicit, distinguish truncated MLCLAT1, and retain the unresolved GO:0052816 hydrolase assertion as UNDECIDED. The existing separation-of-function experiment remains the appropriate prospective test; no broader claim that the literature has established every mechanistic relationship is added.

Final accounting supersedes the preceding candidate: 60 preserved native GOA contexts plus 1 NEW; 38 ACCEPT, 11 KEEP_AS_NON_CORE, 9 MODIFY, 1 REMOVE, 1 UNDECIDED, 1 NEW. The description is phrased as biology rather than a study narrative. A fresh history links PR #6313 with correctly spaced counts; existing history records remain append-only. Native source files and publication caches are unchanged.

## 2026-11-14 UTC — PR #6313 review follow-up

Restore four GO:0004300 rows to ACCEPT and use enoyl-CoA hydratase activity for the
first core function and generic catalytic replacement. Retain all three GO:0018812
rows: this is a genuine narrower (2E)-reaction child, not a synonym or wrong-direction
annotation. Replace the unsupported policy attribution for GO:0006631 with the
biological rationale. Add a bounded BIOLOGY gap about separation of HADHA activities
in the reviewed cardiomyocyte experiments, with primary-source provenance. All 60
native contexts, one NEW molecular-function row, native fields and sources are
preserved. No family or cached-source edit is made. This supersedes earlier notes
that directed every hydratase parent row to GO:0018812.
