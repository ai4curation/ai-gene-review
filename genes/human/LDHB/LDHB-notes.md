# LDHB (L-lactate dehydrogenase B chain, P07195) — review notes

## Core biology
LDHB encodes the B / H ("heart") subunit of L-lactate dehydrogenase (LDH; EC 1.1.1.27).
Active LDH is a tetramer assembled from LDHA (M) and LDHB (H) subunits, giving rise to
the classic five isoenzymes (M4, M3H1, M2H2, M1H3, H4). LDHB-rich isoenzymes (H4)
kinetically favour oxidation of L-lactate back to pyruvate, suiting oxidative tissues
(heart, kidney) that consume lactate as fuel.

- Catalytic reaction (UniProt CATALYTIC ACTIVITY, RHEA:23444, EC 1.1.1.27):
  `(S)-lactate + NAD(+) = pyruvate + NADH + H(+)`. Reversible; UniProt notes both
  left-to-right (RHEA:23445) and right-to-left (RHEA:23446) physiological directions.
- UniProt FUNCTION [ECO:0000269|PubMed:27618187]: "Interconverts simultaneously and
  stereospecifically pyruvate and lactate with concomitant interconversion of NADH and
  NAD(+)."
- SUBUNIT: Homotetramer (PubMed:11276087). Interacts with the PTEN-uORF micropeptide
  MP31, which inhibits mitochondrial LDH activity (PubMed:33406399).
- Tissue specificity: "Predominantly expressed in aerobic tissues such as cardiac
  muscle" [ECO:0000305|PubMed:11276087]. HPA: tissue-enhanced heart muscle, kidney.

## Kinetic / structural basis (PMID:11276087)
Read et al. crystallised human LDH-M and LDH-H ternary complexes with NADH + oxamate.
"Lactate dehydrogenase (LDH) interconverts pyruvate and lactate with concomitant
interconversion of NADH and NAD(+)." The two isoforms are structurally
indistinguishable at the active site; kinetic differences arise from peripheral charged
surface residues. Confirms homotetramer, NAD+ binding, and MF = L-lactate dehydrogenase
(NAD+) activity. [full_text_available: false — abstract only]

## Mitochondrial association (PMID:27618187, Chen et al. Nat Chem Biol 2016)
Full text available. Key verbatim findings:
- "Functional LDH is a homo or hetero tetramer composed of LDHA and LDHB subunits"
- "LDHB is the predominant isoform found in heart muscle and is often referred to as the
  H subunit"
- "it has been suggested that LDHA preferentially reduces pyruvate to lactate, while
  LDHB supports conversion of lactate to pyruvate in cells that utilize lactate as a
  nutrient source for oxidative metabolism or gluconeogenesis"
- TEM immunogold: "gold-labeled LDHB localizes to the inner mitochondrial membrane"
- LDHB activity detected in whole-cell and isolated mitochondrial lysates.
This is the experimental basis for the IDA GO:0004459 and IDA GO:0005743 (mito inner
membrane) annotations. Note this is a specific, somewhat contested localization; the
dominant/canonical localization remains cytosolic (glycolytic enzyme).

## MP31 interaction (PMID:33406399)
MP31 is a micropeptide from the PTEN uORF that "limits lactate-pyruvate conversion in
mitochondria by competing with mitochondrial lactate dehydrogenase (mLDH) for
nicotinamide adenine dinucleotide (NAD+)." UniProt: interaction abolished by LDHB
mutants D53A and R100A. Supports a real, functionally meaningful protein-protein
interaction (regulatory), curated by UniProt as GO:0005515 IPI with C0HLV8 (MP31).

## Disease
LDHB deficiency (LDHBD, MIM:614128): "A condition with no deleterious effects on
health." Clinically mild/asymptomatic; laboratory-medicine interest (LDH isoenzyme
misdiagnosis). Many missense variants documented in UniProt (K7E, R107W inactive, etc.).

## Annotation assessment summary
- MF core: GO:0004459 L-lactate dehydrogenase (NAD+) activity — strongly supported
  (EXP PMID:11276087, IDA PMID:27618187, IBA, IEA, TAS). ACCEPT.
- GO:0004457 lactate dehydrogenase activity — parent term, ACCEPT (broader is fine).
- BP: GO:0006089 lactate metabolic process, GO:0042867 pyruvate catabolic /
  GO:0019244 pyruvate fermentation to lactate, GO:0019674 NAD+ metabolic process —
  all consistent. IBA pyruvate fermentation to lactate reflects the PANTHER family node;
  for LDHB (H4) the physiologically favoured direction is lactate->pyruvate, so
  "fermentation to lactate" is somewhat directionally biased toward LDHA, but the
  reaction is the same and reversible — keep, mark non-core where over-specific.
- CC: cytosol GO:0005829 (IDA HPA, IEA, TAS Reactome) — core canonical location.
  cytoplasm GO:0005737 — ACCEPT (broader). mitochondrion / mito inner membrane
  (IBA + IDA PMID:27618187) — real but non-canonical; keep as non-core. exosome /
  membrane / membrane raft — mass-spec / proteomics HDA/IDA; over-annotations for a
  soluble glycolytic enzyme, mark over-annotated.
- protein binding (GO:0005515) IPIs — bare, uninformative; MARK_AS_OVER_ANNOTATED
  (do NOT REMOVE per policy). The MP31 one (PMID:33406399) is the most biologically
  meaningful.
- identical protein binding GO:0042802 — reflects homotetramerization; keep as
  non-core (informative-ish, supports tetramer).
- kinase binding / NAD binding (Ensembl IEA GO_REF:0000107) — NAD binding is correct
  (NAD-dependent enzyme); kinase binding is an orthology-transferred over-annotation,
  mark over-annotated.
</content>
