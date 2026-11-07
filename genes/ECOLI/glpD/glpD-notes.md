# glpD review notes

## Scope

- Target: `glpD`, UniProt P13035, E. coli K-12.
- Reviewed target files: `glpD-ai-review.yaml` and `glpD-uniprot.txt`.
- Comparative/module context: `genes/PSEPK/glpD/glpD-ai-review.yaml` and `modules/bacterial_glycerol_uptake_catabolism.yaml`.

## Functional synthesis

GlpD is the single-subunit, aerobic FAD-dependent sn-glycerol-3-phosphate dehydrogenase of the E. coli glycerol regulon. It carries out the GlpF/GlpK/GlpD route's final catabolic reaction by oxidizing sn-glycerol 3-phosphate to DHAP at the cytoplasmic membrane and passing electrons through FAD to respiratory quinone. The 1978 biochemical work purified the membrane-associated flavoprotein and showed FAD content, activity with artificial electron acceptors, functional reconstitution with E. coli membrane vesicles, and phospholipid or nondenaturing detergent dependence [PMID:340460]. Yeh et al. later solved structures of active E. coli GlpD that show the G3P site, a likely ubiquinone-binding hydrophobic plateau, membrane-interacting surfaces, and a physiologically relevant dimer [PMID:18296637].

The Kistler and Lin physiology should be read as a distinction between the particulate GlpD enzyme and the soluble GlpABC anaerobic enzyme. GlpD supports aerobic glycerol/G3P growth and nitrate-coupled anaerobic growth, but GlpABC is required for fumarate-coupled anaerobic use of glycerol substrates [PMID:4945192]. Cozzarelli et al. provide older mutant-physiology support that losing the G3P dehydrogenase step blocks productive use of glycerol-derived intracellular L-alpha-glycerophosphate [PMID:5321485].

## Curation decisions

- `GO:0004368` is the core molecular function and should be retained for IBA, IDA, and EC/Rhea/InterPro-derived IEA rows. No NAD-dependent glycerol-3-phosphate dehydrogenase activity is supported for P13035.
- `GO:0046168` is the direct catabolic process because GlpD consumes sn-glycerol 3-phosphate to make DHAP. The parent `GO:0006072` is valid but should be narrowed to that term.
- `GO:0019563` glycerol catabolism is true for the whole pathway but is less direct than the G3P catabolic step because GlpF and GlpK do the uptake and phosphorylation steps.
- `GO:0005886` is the specific location. Broad `cytoplasm` and `membrane` IEAs are less precise than the experimentally supported bacterial plasma membrane association.
- `GO:0009331`, `GO:0042803`, `GO:0071949`, and `GO:0009055` capture real complex, assembly, cofactor, and electron-transfer aspects of GlpD, but only the quinone-dependent dehydrogenase activity is the compact core molecular function.
- The generic Dam and AzuC `GO:0005515` rows do not add useful molecular-function annotations. The Dam hits come from high-throughput AP-MS datasets with no specific GlpD mechanism in the local evidence [PMID:15690043; PMID:19402753]. The AzuC row reports a real interaction that modulates GlpD activity [PMID:35239434], but the interaction still points back to GlpD's established dehydrogenase activity.

## 2026-11-03 review completion (Claude, AI-assisted)

No deep-research provider file exists for this gene. The review rests on the
cached publications: PMID:18296637 and PMID:35239434 (full text), and
PMID:340460, PMID:4945192, PMID:5321485 and PMID:15690043 (abstract only). It
was reviewed together with `genes/PSEPK/glpD`.

- GO:0009331 (IDA PMID:18296637): ACCEPT kept. The GO definition explicitly
  includes "a GlpD homodimer that functions in aerobic conditions". The PSEPK IEA
  row on the same term was moved from UNDECIDED to ACCEPT to match.
- GO:0005515 IPI PMID:15690043 (Dam): UNDECIDED -> REMOVE under the bare
  protein-binding policy. The AP-MS method is quoted from the abstract, and the
  Dam pair is in UniProt's INTERACTION comment (NbExp=3). The other two
  protein-binding rows stay REMOVE, now with supported_by.
- GO:0004368 IEA (GO_REF:0000120): replaced the DR GO-line quote with the
  UniProt CATALYTIC ACTIVITY, InterPro IPR000447 and PMID:18296637 quotes.
- GO:0005737 cytoplasm (IEA, from UniProt SubCell "Cytoplasm"):
  MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0005886. GlpD has a soluble pool but
  is fully active only on the cytoplasmic membrane (PMID:35239434), into which
  it embeds about 12-15 Å (PMID:18296637). Recorded a UniProt source defect on
  the SUBCELLULAR LOCATION line.
- GO:0016020 membrane (ARBA): MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0005886.
- GO:0006072 (InterPro2GO): MARK_AS_OVER_ANNOTATED -> MODIFY to GO:0046168.
- GO:0019563 glycerol catabolic process (UniPathway): KEEP_AS_NON_CORE ->
  ACCEPT. GlpD catalyzes a step of the GlpF/GlpK/GlpD glycerol degradation
  route, and GO:0046168 is not a descendant of it. Added to
  core_functions.directly_involved_in.
- GO:0009055 electron transfer activity (IDA PMID:340460): KEEP_AS_NON_CORE ->
  MARK_AS_OVER_ANNOTATED. The assayed "electron transfer" is GlpD's own
  G3P:acceptor oxidoreduction, already captured by GO:0004368, not a carrier
  function.
- All other actions kept, with quotes completed. Status set to COMPLETE, the
  resolved Dam suggested question replaced, and one suggested experiment added.


## 2026-11-07 comparative glycerol audit

Rechecked all 19 rows. Current GO0009055 includes enzymatic electron-transfer reactions, so GlpD electron transfer is accepted rather than restricted to autonomous shuttle proteins. Retained the genuine soluble pool as non-core cytoplasm and the active membrane-associated pool as core. Direct respiratory electron entry and functional homodimerization are core-associated. The aerobic enzyme designation does not exclude nitrate-respiratory growth (PMID4945192); quinone analog structures do not constitute a native ubiquinone-bound structure. Physiological terminal electron acceptors are downstream of GlpD, not direct GlpD substrates.

Default Falcon attempted via normal workflow and failed HTTP403 authentication; no provider output was fabricated. All original ordered annotation payloads are preserved, with no new GO rows. Focused validation, source preservation, and helper-history results are recorded in analysis/module_audits/bacterial_glycerol_uptake_catabolism/existing-member-consultation/. COMPLETE denotes completed adjudication, including explicit unresolved claims.


## PR6162 review follow-up (2026-11-07 UTC)

Current official GO0009055 includes enzymatic metabolic electron transfer and is not an ancestor of GO0004368. Retained this directly supported core claim and made electron transfer, functional homodimerization and aerobic respiratory participation explicit in core functions, without excluding nitrate respiration.

Original ordered annotation payloads, raw/provider/publication bytes and historical NEW assertions are preserved. No new GO row was added.
