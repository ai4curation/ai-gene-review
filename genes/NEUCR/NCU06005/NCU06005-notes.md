# NCU06005: biological evidence

NCU06005 is a glycerol-kinase-family enzyme predicted to phosphorylate glycerol with ATP, producing sn-glycerol-3-phosphate. This reaction initiates glycerol assimilation and supplies an intermediate for carbon and glycerolipid metabolism. Classical Neurospora crassa enzymology identifies a cytosolic glycerokinase in the inducible glycerol-dissimilation pathway; the precise correspondence of that historical glp-4 activity to the modern NCU06005 locus and any additional mitochondrial pool remain unresolved.

- glycerol kinase activity: The glycerol-kinase-specific IPR005999 and PANTHER glycerol-kinase subfamily distinguish this enzyme from generic FGGY carbohydrate kinases. Classical N. crassa experiments establish glycerokinase-dependent glycerol utilization, grounding transfer of ATP-dependent glycerol phosphorylation; a modern target-specific purified assay was not recovered.
- mitochondrion: The mitochondrial IBA is an ancestral localization assertion at PTN000023394, but classical N. crassa enzymology identifies cytosolic glycerokinase and mitochondrial glycerol-3-phosphate dehydrogenase as separate activities. The historical glp-4 to NCU06005 mapping and any dual localization are not fully resolved, so the IBA is neither confirmed nor removed.
- carbohydrate metabolic process: Glycerol phosphorylation is the entry reaction of the experimentally characterized fungal glycerol-dissimilation pathway. Glycerol catabolism describes that established role more precisely than broad carbohydrate or glycerol metabolism.
- glycerol metabolic process: Glycerol phosphorylation is the entry reaction of the experimentally characterized fungal glycerol-dissimilation pathway. Glycerol catabolism describes that established role more precisely than broad carbohydrate or glycerol metabolism.
- glycerol-3-phosphate metabolic process: The kinase produces glycerol-3-phosphate directly, supporting its biosynthetic process rather than unspecified metabolism of that intermediate.
- triglyceride metabolic process: Glycerol kinase supplies glycerol-3-phosphate, a glycerolipid precursor, so the curated triglyceride-metabolism inference is a plausible downstream role. It does not make this enzyme a triglyceride synthase, and target lipid flux was not measured in the retrieved glycerol-utilization studies.
- kinase activity: The diagnostic glycerol-kinase family resolves the phosphoryl acceptor as glycerol and supports the specific kinase activity.
- phosphotransferase activity, alcohol group as acceptor: The diagnostic glycerol-kinase family resolves the phosphoryl acceptor as glycerol and supports the specific kinase activity.
- glycerol catabolic process: ATP-dependent glycerol phosphorylation both initiates glycerol catabolism and directly produces glycerol-3-phosphate. The specific family assignment and classical fungal glycerol-utilization enzymology support this process.
- glycerol-3-phosphate biosynthetic process: ATP-dependent glycerol phosphorylation both initiates glycerol catabolism and directly produces glycerol-3-phosphate. The specific family assignment and classical fungal glycerol-utilization enzymology support this process.

Primary evidence excerpts

- [file:NEUCR/NCU06005/NCU06005-uniprot.txt] “DR   InterPro; IPR005999; Glycerol_kin.”
- [PMID:6284716] “Evidence from the enzymatic characterization of these
mutants indicated that glp-2 and glp-4 were the structural genes encoding the
mitochondrial glycerol-3-phosphate dehydrogenase and cytosolic glycerokinase,
respectively.”

Provenance: live API snapshot 2026-09-09T03:00:51.831347+00:00. Complete API prediction JSON and all emitted claim IDs, text, and original evidence are preserved in the source and provenance JSON files. Current sequence/annotation data are separate comparison snapshots. Annotation overlap records known biology, not demonstrated training membership. All seven gene-focused Falcon jobs completed; the provider reports were inspected and useful primary leads checked. Publication retrieval used Europe PMC metadata/XML when the canonical PubMed fetch returned HTTP 429.

PMID:29563189 lists NCU06005 as glycerol kinase GLK-1 in a cold-sensitive mutant screen. This locus-level phenotype is not a purified kinase or localization assay. The old glp-4 name is not adopted without an authoritative locus mapping. Cytoplasm SL-0086 was emitted with string_match_text GO:0005739 (mitochondrion); the original mismatch is retained and the emitted location is assessed separately.
