# CBL10 / SCaBP8 (Q7FRS8, At4g33000) review notes

## Deep research status

`just deep-research ARATH CBL10` could not be run: on 2026-10-20 the falcon
(authentication failure), perplexity (provider not available) and openai
(invalid API key) providers all failed for the sister gene CBL4 in the same
session. No deep-research file exists. These notes were compiled manually from
cached PubMed/PMC records in `publications/`.

## Identity

- UniProt Q7FRS8 (CNBLA_ARATH), CBL10, SCaBP8 (SOS3-like calcium binding
  protein 8), At4g33000. Calcineurin B-like family (PANTHER PTHR23056), EF-hand
  calcium sensor with an extended N-terminus that carries tonoplast-targeting
  information. Two splice isoforms in UniProt.

## Literature synthesis

### SOS-pathway Ca2+ sensor in shoots
- [PMID:17449811 "By contrast, the SOS3 homolog SOS3-LIKE CALCIUM BINDING PROTEIN8 (SCABP8)/CALCINEURIN B-LIKE10 functions mainly in the shoot response to salt toxicity."]
- [PMID:17449811 "SCABP8 is further shown to bind calcium, interact with SOS2 both in vitro and in vivo, recruit SOS2 to the plasma membrane, enhance SOS2 activity in a calcium-dependent manner, and activate SOS1 in yeast."]
- Partial redundancy with SOS3
  [PMID:17449811 "These results suggest that SCABP8 and SOS3 are only partially redundant in their function, and each plays additional and unique roles in the plant salt stress response."].
- SOS2 phosphorylates SCaBP8 at Ser237, stabilizing the complex
  [PMID:19448033 "In vivo, this phosphorylation was induced by salt stress, occurred at the membrane, stabilized the SCaBP8-SOS2 interaction, and enhanced plasma membrane Na+/H+ exchange activity."].
- CBL10 also partners CIPK8 to activate SOS1
  [PMID:31858132 "These results suggest that CIPK8-mediated activation of SOS1 is CBL10-dependent and SOS3-independent"].

### Tonoplast branch
- [PMID:17825054 "the CBL10-CIPK24 (SOS2) complex is associated with the vacuolar compartments that are responsible for salt storage and detoxification in plant cells"].
- cbl10 mutants accumulate less Na+ than wild type
  [PMID:17825054 "the Na(+) content of the cbl10 mutant, unlike other salt-sensitive mutants identified thus far, was significantly lower than in the wild type under either normal or high-salt conditions"].
- Tonoplast targeting needs S-acylation by PAT10
  [PMID:31441225 "This study shows that Arabidopsis CBL10, through protein S-acylation by protein S-acyl transferase10, targets to the vacuolar membrane to confer salt tolerance."].
- Localization conflict: Quan et al. (PMID:17449811) report plasma membrane;
  Kim et al. (PMID:17825054) and Batistic et al. (PMID:19832944, per UniProt)
  report tonoplast. Both pools are plausible; the PM-localized pool is the one
  that recruits SOS2 for SOS1 activation.
- CBL4 and CBL10 act in separable pathways
  [PMID:31100786 "suggesting that CBL10 regulates additional unknown transport processes that play distinct roles from the SOS1 in Na+ homeostasis"].

### Kinase-independent targets
- AKT1 K+ channel: direct binding, inhibits current
  [PMID:23331977 "CBL10 may compete with CIPK23 for binding to AKT1 and negatively modulate AKT1 activity"].
  Evidence partly from overexpression lines.
- TOC34 (chloroplast outer membrane GTPase)
  [PMID:28018422 "we also demonstrated that CBL10 physically associates with TOC34 in vitro, resulting in a significant decrease in the GTPase activity of the TOC34 protein"].
- SOS2-SCaBP8 complex phosphorylates/inhibits AtANN4 to shape the Ca2+ signature
  [PMID:30861376 "SCaBP8 promotes the interaction of protein kinase SOS2 with AtANN4, which enhances its phosphorylation by SOS2"].

## GOA issues noted
- GO:0005634 nucleus (ISM, AtSubP prediction): no experimental support;
  CBL10 is membrane-anchored (tonoplast/PM). Removed.
- GO:0005515 protein binding rows replaced with informative terms (kinase
  activator / kinase binding / potassium channel inhibitor).

## Review decisions (2026-10-20)
- Phosphosite numbering: Lin et al. 2009 (PMID:19448033) call the SOS2 site
  Ser237; UniProt lists it as Ser-247.
- Core functions: (1) Ca2+-dependent activator of CIPK24/SOS2 at the plasma
  membrane in shoots (GO:0043539); (2) tonoplast CBL10-CIPK24 complex
  (GO:0019901 protein kinase binding; plant-type vacuole membrane; sodium ion
  homeostasis); (3) kinase-independent AKT1 inhibition (GO:0070320).
- REMOVE: GO:0005634 nucleus (ISM prediction only).
- MODIFY: GO:0005774 -> GO:0009705; GO:0019900 -> GO:0019901; GO:0050801 ->
  GO:0055078; protein-binding IPI rows -> GO:0043539 (SOS2, PMID:17449811),
  GO:0019901 (SOS2, PMID:17825054), GO:0070320 (AKT1, PMID:23331977).
- No suspected source-record errors. No NEW annotations proposed.

## PR #5243 review follow-up

- The second core function's MF is now GO:0043495 protein-membrane adaptor activity, not GO:0019901.
  The row-level MODIFY to GO:0019901 stands. The adaptor role is a NEW IDA row on the CBL targeting
  paper. [PMID:19832944 "distinct targeting signals located in the N-terminal domain of CBL proteins
  determine the spatially discrete localization of CBL/CIPK complexes"]
- Sodium ion homeostasis stays at GO:0055078 here, while CBL4 and CIPK24 use GO:0006883. The cbl10
  phenotype is altered whole-plant Na+ content (lower, unlike other SOS mutants), and GOA's own row
  is the generic ion homeostasis term.
