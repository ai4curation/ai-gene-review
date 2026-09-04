# GND1 (Candida albicans SC5314, A0A1D8PFS4) curation notes

## 2026-09-04 - enzyme specificity review (projects/ENZYME_SPECIFICITY.md)

GND1 was the last pending gene in the Enzyme Specificity project. It was chosen as a
check on **cofactor specificity** (project category 3): GO:0004616 is defined as the
NADP+-dependent reaction (EC 1.1.1.44), whereas 6PGDH enzymes also occur as NAD+-specific
and dual-specificity forms [PMID:35234135 "Some bacterial 6PGDHs are specific for NAD+,
while others can use both NAD+ and NADP+"].

### Identity and reaction
- UniProt A0A1D8PFS4 = GND1 / orf19.12491 / CAALFM_C113860CA, 495 aa, 6PGDH family,
  EC 1.1.1.44, RHEA:10116 (from the UniProt record).
- Gnd1 is one of the two NADPH-producing dehydrogenases of the oxidative PPP in
  C. albicans [PMID:22094058 "NADPH is produced by the two dehydrogenases in the oxidative
  branch of the PPP: glucose-6-phosphate dehydrogenase (Zwf1) and 6-phosphogluconate
  dehydrogenase (Gnd1)"]. The deep-research report states that the Strijbis 2012 assay
  used 6-phosphogluconate + NADP+ with NADPH monitored at 340 nm; that paper is
  abstract-only in our cache so the assay text itself could not be quoted.
- Garg et al. 2025 (full text cached) measure oxidative-PPP NADPH production in C. albicans
  lysates with 0.4 mM NADP+ and glucose-6-phosphate, noting that "ZWF1 catalysis provides
  the 6-phosphogluconate substrate for GND1" [PMID:40183578]; GND1 is markedly induced
  under iron starvation.

### Cofactor-specificity check (GND1-bioinformatics/)
- Hanau & Helliwell 2022 describe the determinants of NADP+ specificity: the
  Gly-X-Ala-X-Met-Gly fingerprint and the Asn-Arg-Thr turn whose Asn/Arg bind the
  2'-phosphate; NAD+-preferring enzymes carry Asp-Arg-Asp [PMID:35234135 "Mutagenesis of
  the conserved arginine and asparagine in Lactococcus lactis and Gluconobacter oxydans
  6PGDH demonstrated their role in specificity for NADP+ over NAD+"].
- C. albicans Gnd1 has GLAVMG at 13-18 and NRT at 36-38, coinciding with the UniProt
  NADP(+) BINDING features; no Asp-Arg-Asp. Verdict: NADP+-specific determinants present.
  See `GND1-bioinformatics/RESULTS.md`.
- Conclusion: GO:0004616 is the correct cofactor-specific MF; no specificity error.

### Substrate over-generalisation caught (project category 1)
- `GO:0019521 D-gluconate metabolic process` (IEA, GO_REF:0000043) comes from the UniProt
  keyword "Gluconate utilization" (ARBA00023064 / RuleBase RU000485). The keyword reflects
  bacterial gluconate catabolism (gluconate -> gluconokinase -> 6-phosphogluconate -> Gnd),
  but Gnd1's substrate is 6-phospho-D-gluconate, and in the yeast oxidative PPP it is
  supplied by Zwf1/6-phosphogluconolactonase, not from free D-gluconate. No C. albicans
  evidence for gluconate assimilation via Gnd1 was retrieved. Changed from
  KEEP_AS_NON_CORE to MARK_AS_OVER_ANNOTATED.

### Localization
- Predominantly cytosolic, with a minor PTS2 splice isoform in peroxisomes (about 5%)
  [PMID:22094058 "the majority is cytosolic, but a small fraction is peroxisome
  associated"; PMID:34065948 "approximately 10% and 5% of the proteins, respectively,
  were localized in peroxisomes"]. Cytosol ACCEPT; peroxisome KEEP_AS_NON_CORE.
- Biofilm-matrix detection (PMID:27609602) is a proteomic survey hit; KEEP_AS_NON_CORE.

### Outcome
- Status set to COMPLETE. Two references added (PMID:34065948, PMID:35234135, both
  verified via PubMed) plus the bioinformatics RESULTS file.
