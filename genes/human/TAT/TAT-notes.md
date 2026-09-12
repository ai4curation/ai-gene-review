# TAT (Tyrosine aminotransferase, P17735) — review notes

## Core biology (verified from UniProt record + cached pubs)

- Cytosolic, liver-expressed, PLP (pyridoxal-5'-phosphate)-dependent aminotransferase; class-I
  PLP-dependent aminotransferase family. HPA: "Tissue enriched (liver)".
- Catalyzes the FIRST/committed step of L-tyrosine catabolism:
  L-tyrosine + 2-oxoglutarate = 3-(4-hydroxyphenyl)pyruvate + L-glutamate. EC 2.6.1.5; RHEA:15093.
  [UniProt P17735 CATALYTIC ACTIVITY, "L-tyrosine + 2-oxoglutarate = 3-(4-hydroxyphenyl)pyruvate + L-glutamate"]
- FUNCTION (UniProt): "Transaminase involved in tyrosine breakdown. Converts tyrosine to
  p-hydroxyphenylpyruvate. Can catalyze the reverse reaction, using glutamic acid, with 2-oxoglutarate
  as cosubstrate (in vitro). Has much lower affinity and transaminase activity towards phenylalanine."
  {ECO:0000269|PubMed:16640556, ECO:0000269|PubMed:7999802}
- Cofactor: pyridoxal 5'-phosphate; PLP-lysine Schiff base at Lys-280 (MOD_RES 280,
  "N6-(pyridoxal phosphate)lysine"; PDB 3DYD).
- SUBUNIT: Homodimer. {ECO:0000305|Ref.8} — supports GO:0042802 identical protein binding.
- PATHWAY (UniProt): "Amino-acid degradation; L-phenylalanine degradation; acetoacetate and
  fumarate from L-phenylalanine: step 2/6." (Phe catabolism proceeds via Phe->Tyr then Tyr catabolism;
  TAT is the Tyr-catabolism step, hence the phenylalanine-catabolism pathway membership annotation.)

## Enzyme substrate specificity — narrow, with weak Phe activity
- PMID:16640556 (Sivaraman & Kirsch 2006) title: "The narrow substrate specificity of human tyrosine
  aminotransferase -- the enzyme deficient in tyrosinemia type II." (abstract-only in cache; full text
  not available). Supports narrow Tyr specificity, plus weak phenylalanine transamination; mutagenesis
  of Ile-294 reduced activity. This underpins treating aromatic-AA / phenylalanine activities as
  secondary (KEEP_AS_NON_CORE / broad-parent) rather than core.

## Expression cloning / functional demonstration
- [PMID:7999802 "The expressed protein catalyzed specifically the conversion of L-[14C]tyrosine into
  p-[14C]hydroxyphenylpyruvate."] — human TAT cDNA expressed in HeLa; IDA basis for GO:0004838 MF and
  the tyrosine catabolic process / 2-oxoglutarate + glutamate metabolic annotations (products/cosubstrates).
- [PMID:1973834 "The human TAT gene is predicted to code for a 454 amino acid protein of molecular weight
  50,399 dalton."] — gene structure; also documents glucocorticoid response elements (GRE) context:
  "Two functional glucocorticoid response elements (GREs) reside 2.5 kb upstream of the rat TAT gene."
  NAS basis for GO:0004838.

## Disease
- Tyrosinemia type II (TYRSN2, Richner-Hanhart syndrome), MIM:276600: oculocutaneous tyrosinemia —
  palmoplantar keratosis, painful corneal ulcers, intellectual disability, from elevated plasma/urine
  tyrosine. [UniProt DISEASE, "palmoplantar keratosis, painful corneal ulcers, and intellectual disability"]
  Variant G362V (VAR_000560) in TYRSN2 [PMID:1357662].

## Regulation (classic glucocorticoid/glucagon/cAMP-inducible gene)
- TAT is a textbook glucocorticoid- and cAMP-inducible hepatic gene. The Ensembl-Compara IEA
  (GO_REF:0000107) response terms (glucocorticoid, cortisol, cAMP, dexamethasone, insulin, retinoic acid,
  ethanol, mercury, oxidative stress, liver regeneration) are transferred largely from rat/mouse orthologs
  (P04694 rat, Q8QZR1 mouse). These are hormonal-regulation *responses* of the gene, biologically plausible
  for the rodent orthologs but are regulatory/physiological context, not TAT's core molecular activity or
  its direct catabolic process. Treat as KEEP_AS_NON_CORE (regulation/response context transferred by
  orthology), not core function.

## Interactions (IPI, IntAct high-throughput)
- IntAct/interactome IPI annotations (protein binding GO:0005515) with UBE3A (Q05086), GLUL (P15104),
  GRN (P28799) and self (P17735) come from systematic interactome maps
  (PMID:24722188, 25910212, 31515488, 32296183, 32814053, 25502805). TAT appears in these as one node in
  genome-scale Y2H/AP-MS screens; body text of the papers does not discuss TAT specifically. Bare
  "protein binding" is uninformative for MF (curation guideline) -> MARK_AS_OVER_ANNOTATED.
- GO:0042802 identical protein binding is corroborated by the documented homodimer
  [UniProt SUBUNIT "Homodimer."] -> ACCEPT (self-association is real biology), though non-core.

## Deep research provenance
- Falcon deep research (TAT-deep-research-falcon.md) did NOT land within the 8-minute poll
  window (2026-07-05). Review grounded in UniProt P17735, seeded GOA, cached publications
  (PMID_7999802, PMID_1973834, interactome PMIDs), and local go.db term labels/definitions.

## Term-label notes (current ontology, from local go.db)
- GO:0004838 = "L-tyrosine:2-oxoglutarate transaminase activity" (def matches RHEA:15093 reaction). CORE MF.
- GO:0006572 = "L-tyrosine catabolic process". CORE BP.
- GO:0005829 = "cytosol". CORE location.
- GO:0030170 = "pyridoxal phosphate binding" (cofactor binding). ACCEPT.
- GO:0009074 current primary label = "aromatic amino acid family catabolic process" (GOA seed label is
  "aromatic amino acid catabolic process" — GOA label retained in existing_annotations as trusted).
