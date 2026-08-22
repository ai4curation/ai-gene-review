# AAD3 (YCR107W) — S. cerevisiae — Curation Notes

Journal of research and reasoning for the AI GO-annotation review. Provenance recorded inline.

## 2026-08 re-review correction

The original review missed a decisive later primary study. Yang et al. purified all seven
*S. cerevisiae* AAD proteins and found aldehyde-reductase activity only for Aad4 and Aad14.
Aad3 carries Cys73 in place of a catalytically essential tyrosine; replacing Cys73 with Tyr
still did not produce a functional enzyme [PMID:29079624, "correction of the missense
mutation in ScAadCys73Tyrp failed to produce a functional enzyme"]. The paper classifies
the other five family members, including AAD3, as undergoing pseudogenization.

This evidence supersedes the earlier inference below that a full-length AKR fold warrants a
broad positive oxidoreductase annotation. Fold membership describes ancestry, not retained
activity. The final review therefore:

- removes both GO:0047681 activity annotations and GO:0006081 aldehyde metabolism;
- withdraws the proposed GO:0016616 annotation and leaves `core_functions` empty;
- retains only the ND cellular-component placeholder; and
- reframes the knowledge gap around possible residual or nonenzymatic roles rather than an
  assumed functional reductase.

## Deep research status (provenance)

Automated deep research was attempted but did not produce a report:
- `just deep-research-falcon yeast AAD3 --fallback perplexity-lite`: falcon timed out at 600s;
  perplexity-lite fallback returned HTTP 401 "insufficient_quota" (billing/quota exhausted).
- Retry `just deep-research-falcon yeast AAD3`: falcon timed out again (SIGTERM at the 600s cap).

No `-deep-research-{provider}.md` file was fabricated (per repo policy). The initial review used
the UniProt record, GOA, PMID:10572264, and family metadata. The re-review additionally searched
the literature and retrieved the full text of PMID:29079624, which provides the decisive direct
biochemical and catalytic-site evidence above. A focused OpenScientist job then tested the
proposed broad oxidoreductase term. It independently found PMID:29079624 and rejected GO:0016616
as an asserted molecular function because even the broad term claims catalysis contradicted by
the direct Aad3 assays. The report is retained as an audited secondary analysis; the curation
decision rests on the primary paper.

## Identity

- **Gene**: AAD3 (SGD standard name); systematic name **YCR107W** (chromosome III).
- **UniProt**: P25612 (AAD3_YEAST), Reviewed/Swiss-Prot.
- **Length / MW**: 363 aa; 40911 Da. CHAIN 1..363 (full-length; no signal peptide, no reported fragment/truncation).
- **Name meaning**: "Putative aryl-alcohol dehydrogenase AAD3"; EC=1.1.1.- (partial/unassigned).
- **Family (UniProt SIMILARITY)**: "Belongs to the aldo/keto reductase family. Aldo/keto reductase 2 subfamily." (ECO:0000305 = curator inference from sequence).
- **Domain**: Pfam PF00248 (Aldo_ket_red), full-length match; Gene3D 3.20.20.100 (NADP-dependent oxidoreductase domain); SUPFAM SSF51430 (NAD(P)-linked oxidoreductase); CDD cd19147 (AKR_AKR9A3_9B1-4); InterPro IPR050523 (AKR_Detox_Biosynth), IPR023210, IPR036812.
- **PANTHER**: PTHR43364 ("NADH-SPECIFIC METHYLGLYOXAL REDUCTASE-RELATED" / family name "Aldo/Keto Reductase Detoxification and Biosynthesis") and subfamily PTHR43364:SF2 ("ARYL-ALCOHOL DEHYDROGENASE AAD10-RELATED").
- **PE (protein existence)**: PE=3, "Inferred from homology" — i.e. no protein-level or transcript-level experimental evidence recorded in UniProt for AAD3 itself.

## The AAD gene family in S. cerevisiae (important — separate AAD3 from paralogs)

The AAD (Aryl-Alcohol Dehydrogenase) genes are a family of paralogous ORFs in S. cerevisiae,
most located in subtelomeric regions. Members include AAD3 (YCR107W), AAD4 (YDL243C),
AAD6 (YFL056C), AAD10 (YJR155W), AAD14 (YNL331C), AAD15 (YOL165C), AAD16 (YFL057C).
They were identified by in-silico similarity to a *bona fide* fungal enzyme. Later biochemical
work showed that Aad4 and Aad14 are active enzymes, while Aad3 and four other members are
pseudogenizing [PMID:29079624]. Evidence must therefore be resolved per paralog.

## KNOWN (evidence-supported)

1. **AAD3 is a member of the aldo/keto reductase (AKR) superfamily.** Sequence/domain evidence:
   Pfam PF00248 covers the full 363-aa ORF; AKR fold assignments (Gene3D, SUPFAM, CDD, InterPro
   IPR050523). This is solid at the level of *fold/superfamily membership*, not specific catalysis.
   [UniProt P25612 DR lines: Pfam PF00248; Gene3D 3.20.20.100; SUPFAM SSF51430; InterPro IPR050523]

2. **The AAD family was defined by similarity to the *Phanerochaete chrysosporium* aryl-alcohol
   dehydrogenase (AAD), a lignin-degradation enzyme.** The ISS annotations on AAD3 use
   `with/from = UniProtKB:Q01752`, which is the *P. chrysosporium* AAD (a white-rot fungus enzyme),
   NOT a yeast protein. [PANTHER PTHR43364-entries.csv: "Q01752 ... Phanerodontia chrysosporium ...
   Aryl-alcohol dehydrogenase [NADP(+)]"] [PMID:10572264 abstract: "seven open reading frames (ORFs)
   in Saccharomyces cerevisiae whose protein products show a high degree of amino acid sequence
   similarity to the aryl alcohol dehydrogenase (AAD) of the lignin-degrading fungus Phanerochaete
   chrysosporium"].

3. **Deletion of the seven yeast AAD genes (including AAD3) produced NO aryl-aldehyde-degradation
   phenotype.** [PMID:10572264 abstract: "None of the knock-out strains revealed any mutant phenotype
   when tested for the degradation of aromatic aldehydes using both spectrophotometry and high
   performance liquid chromatography (HPLC)."] Ergosterol/phospholipid profiles, mating and
   sporulation were also unaffected in the septuple deletant. Note: the stationary-phase aryl-alcohol
   dehydrogenase activity observed in wild-type yeast [same abstract] was NOT abolished by deleting
   all seven AAD genes, implying the measured cellular AAD activity is contributed by other (non-AAD)
   enzymes, and that the AAD genes are functionally redundant or silent under the conditions tested.

4. **Aad3 is inactive in the expected chemistry and has an eroded catalytic site.** Only Aad4
   and Aad14 reduced the tested aldehydes with NADPH. Aad3 substitutes Cys for the essential
   catalytic Tyr73, and restoring Tyr73 did not rescue activity [PMID:29079624].

## NOT known / open (knowledge gaps)

- Whether Aad3 retains an untested residual activity or a nonenzymatic role. The published
  aldehyde panel and catalytic-site repair were negative, so any positive function now requires
  new direct evidence.
- The physiological substrate and biological role (if any). The "aryl-alcohol dehydrogenase" name is
  purely a homology transfer from the *P. chrysosporium* enzyme; S. cerevisiae is not a lignin
  degrader, so the ancestral aryl-alcohol/lignin-related context does not obviously apply.
- Subcellular localization is unassigned (GOA has an ND `is_active_in cellular_component` root
  annotation, GO_REF:0000015).
- Whether AAD3 is a functional gene, a conditionally-expressed paralog, or a degenerate/relic
  subtelomeric duplicate. The AAD family expansion sits in subtelomeric regions that are hotspots
  for gene duplication, rapid evolution, and pseudogenization.

## Domain / truncation reasoning (inline bioinformatics)

I inspected the UniProt sequence directly (no sub-agent).

- **Full length, not truncated**: FT CHAIN 1..363 spans the whole sequence; MW 40911 is typical of a
  complete ~360-aa AKR (AKRs are ~320-360 aa). There is no `FT ... FRAGMENT`, no premature-stop
  evidence, and the Pfam PF00248 match covers the full ORF. So AAD3 is NOT a truncated ORF/relic at
  the sequence level; it is an intact reading frame.
- **Catalytic-site erosion despite an intact fold**: PMID:29079624 aligned the family against the
  active reference enzyme and showed that Aad3 has Cys73 where the essential catalytic tyrosine
  should occur. Native recombinant Aad3 was inactive, and Cys73-to-Tyr repair did not rescue it.
  Thus the intact ORF/fold does not justify even a broad positive oxidoreductase claim.

## Annotation-by-annotation reasoning

GOA (AAD3-goa.tsv) has 4 annotations:

1. `GO:0047681 aryl-alcohol dehydrogenase (NADP+) activity` / IEA / GO_REF:0000117 (ARBA machine rule).
   Electronic family transfer contradicted by direct Aad3 biochemistry. → REMOVE.

2. `GO:0006081 aldehyde metabolic process` / ISS / PMID:10572264, with Q01752.
   ISS from the *P. chrysosporium* AAD. Family-level; not demonstrated for AAD3. Aldehyde metabolism
   depends on an activity that direct assays did not detect. → REMOVE.

3. `GO:0047681 aryl-alcohol dehydrogenase (NADP+) activity` / ISS / PMID:10572264, with Q01752.
   Same specific-activity over-annotation as (1), but via ISS from the fungal enzyme. The deletion
   phenotype directly argues against a demonstrable aryl-aldehyde activity for the yeast AAD genes.
   Direct biochemical evidence shows loss/divergence of the donor activity. → REMOVE without a
   replacement term.

4. `GO:0005575 cellular_component` (root) / ND / GO_REF:0000015.
   Root "no data" placeholder. Standard. → ACCEPT (keep as-is; it is the GO ND convention for
   unknown localization).

## Term-id notes

- existing_annotations ids are from GOA and are trusted (not rewritten).
- GO:0016616 is a valid GO term, but it is not a valid AAD3 annotation on current evidence. The
  review leaves `core_functions` empty rather than turning fold ancestry into a function claim.
