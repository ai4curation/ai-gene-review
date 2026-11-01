# FGA database evidence notes

## 2026-10-26 — Structural subunit, ligand and processed product

The Reactome traversal clarified why many signaling-event references support an extracellular FGA location. FGA remains in a fibrin/fibrinogen ligand complex while integrins, kinases and intracellular adaptors execute the named signaling steps. Those event titles do not assign kinase or signaling-adaptor activity to FGA. The precise routes are retained in [the source evidence map](FGA-database-source-evidence.yaml).

Several routes need more specific product interpretation. R-HSA-8870678 and its downstream TLR4 events reach the literal fibrinopeptide A entity, residues 20–35, inside a curated cleaved-fibrinogen ligand set. That model does not independently show that an isolated 16-residue peptide is the active TLR4 agonist. R-HSA-976734 and R-HSA-977136 instead reach a variant FGA amyloid entity. R-HSA-8952289 places FGA in a FAM20C substrate set in the ER lumen; its modeled residues 36–866 are not an independent experiment demonstrating fibrinopeptide release in the ER. R-HSA-481007 represents fibrinogen as alpha-granule cargo, not as the exocytosis machinery.

The HPA Hep-G2 images support the ER compartment during biosynthetic passage. The actual image scope is less precise than the modeled ER-lumen location, and neither source identifies a natural splice product. Platelet-surface fibrin is a different situation: the original PMID:6777381 comparator experiments identify calcium-dependent extracellular association of fibrin chains after thrombin activation. This supports peripheral surface residence and a contextual response, not integral membrane topology or calcium sensing.

## 2026-10-26 — What alpha-C material does in fibrinolysis

The primary alpha-C studies provide a positive participation argument, beyond fibrin merely being cleaved. In PMID:21806028, recombinant human Aα221–610 oligomers bind both tPA and plasminogen and enhance plasmin generation. Soluble monomers have weak activity, and internally cross-linked monomers are intermediate. Results and Figures 5–8 distinguish these preparations. The same paper explicitly disagrees with the earlier immobilized-monomer binding result in PMID:11170397. Untested aggregation of the earlier preparation is suggested as an explanation, not demonstrated as a resolution.

PMID:37082262 provides a complementary experiment on human plasma-derived fibrin preparations. Its Results section 3.3 and Figure 5 show reduced but persistent plasminogen activation after alpha-C truncation. Thus the alpha-C contribution is additional to other fibrin binding sites. These experiments support a binding/template contribution to activation and fibrinolysis. They do not make FGA a protease, establish the physiological assembly state, or identify the experimental fragments as natural splice products.

The actual GO:0030674 definition concerns coordinated contact between macromolecules and explicitly distinguishes protein-complex scaffolds. Its verified child GO:0140767 describes enzyme-substrate adaptor activity. The same alpha-C oligomer preparation binds the enzyme tPA and substrate plasminogen and promotes their coupled reaction, supporting refinement of the existing broad row. Simultaneous ternary occupancy, stoichiometry and comparative substrate preference were not directly measured; the original broad IBD is not relabeled as the child term. The chicken structure in PMID:11601975 shows interchain architecture, but complex membership alone would not establish an adaptor assay. The independent human ligand-binding/cofactor evidence is the useful corroboration. The six literal positive IBD joins are now supplemented by genuine recovered PTHR47221 tree/MSA evidence: human P02671 leaf PTN002499061 descends from PTN008715159, with an exact 866-residue canonical sequence match. Earlier failed retrievals remain preserved. This verifies target descent, not simultaneous ligand occupancy, a child-term ancestral placement or equivalent function of every natural product.

## 2026-10-26 — Complex-level vascular effects

The recovered PMID:15739255 Methods identify human plasma fibrinogen and fragment D in rat vessel experiments. The positive vascular binding and constriction results are conditional effects of those preparations. PMID:19193866 separately tests human fibrinogen on rat heart microvascular endothelial cells and measures endothelin-1/vWF release with ICAM1 and MEK/ERK controls. The receptor/survival experiments in PMID:10903502 include intact fibrinogen but map a contact using a gamma-chain peptide. These observations justify preserving contextual complex-associated effects while avoiding an autonomous alpha-chain receptor-contact claim.

The operative original for the heterotypic-adhesion paper PMID:8100742 remains inaccessible. Its positive original abstract is retained as context, with source-specific uncertainty rather than a biological negation.

## Product and evidence boundaries

The two curated natural splice products remain unchanged. UniProt's displayed precursor has 866 residues; the shorter Alpha product has 644. The official processed-chain end at 866 belongs to the displayed sequence and cannot be assigned to the shorter product. Experimental Aα221–610 numbering is retained as reported, without an unverified conversion to precursor coordinates.

The intake contains six raw PRO-specific annotations that lose product identifiers in the machine seed, including two collapsed source-key groups. [The product-source map](FGA-product-source-map.yaml) retains those exact source joins. Nominal seed rows therefore cannot automatically be interpreted as assertions about the precursor, every splice product or free fibrinopeptide A.

See the [database source guide](FGA-database-source-guide.md), [phylogeny evidence](FGA-phylogeny-evidence.yaml) and [ontology relationships](FGA-ontology-evidence.yaml) for reproducible locators. The genuine provider invocation did not produce a report; these authored notes are not a provider research report. No publication quotations were added.
