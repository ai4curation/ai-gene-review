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
