# Six new Mla members: evidence adjudication

This consultation preserves ten seeded annotation payloads and adds no NEW rows. A zero-row seed does not imply absence of biological knowledge; independent core functions are supported below. Frozen preflight files remain unchanged.

## Bordetella identities and native evidence

The official UniProt records and the frozen preflight identity proof map Tohama I loci BP3757, BP3758, BP3759, BP3760, BP3761 to Q7VT00, Q7VSZ9, Q7VSZ8, Q7VSZ7, Q7VSZ6, respectively. PMID36518166 Figure1A maps this locus to MlaF/E/D/A/C. Its authentic Supplementary TableS1 identifies B213 as a streptomycin-resistant derivative of Tohama I. This establishes a lineage/locus bridge, not complete sequence identity of every experimental B213 protein. Sources: immutable publications/PMID_36518166.md and preflight/36518166-supp-els.pdf/.txt, official UniProt records and preflight/identity-proof.json.

The native paper perturbs MlaF, not each of the five proteins independently. Cell-surface PE measurements and medium-dependent growth provide physiological evidence for the Mla pathway; the largest asymmetry phenotype involves combined mlaF/pldA loss. These observations support participation by MlaF and conserved cognate machinery, but not a purified target ATPase assay, universal essentiality, exact complex stoichiometry or measured directional flux. No identifiable MlaB homolog was found. The BP3758 UniProt automatic MlaFEDB stoichiometry therefore cannot be transferred literally to Bordetella.

BP3757 has an ABC transporter domain (PROSITE PS50893) and supported ATP-binding site45–52, and official MlaF classification PTHR43023:SF6. Native locus/phenotype plus this specific architecture supports conserved ATPase activity. Its general nucleotide-binding row is refined to the existing ATP-binding term; ATP binding and hydrolysis remain ACCEPT.

BP3758 has NCBIfam TIGR00056/NF033619 MlaE signatures, PF02405 and RuleBase-supported multipass inner-membrane topology. BP3759 has specific MlaD NCBIfam TIGR04430, PF02470, PTHR33371:SF4 and an N-terminal hydrophobic segment. Their phospholipid transport assertions can be refined to the intermembrane pathway, with positive complex contributions. The target domain and locus context, rather than the broad MCE or ABC fold alone, supports the inference. PMID28388411 directly demonstrates phospholipid binding by E. coli MlaD; PMID34873038 directly tests carrier/complex lipid exchange with an ATP-driven retrograde bias. These are ortholog mechanism observations, not Bordetella assays.

BP3760 has MlaA PF04333/IPR007428 plus a predicted lipoprotein signal cleaved at Cys22. Specific MlaA identity and cognate locus provide outer-membrane context beyond the signal peptide alone. The target porin partner remains unknown. PMID40168124 gives direct E. coli MlaA/porin-to-MlaC loading evidence; its contribution does not make the isolated protein a full intermembrane transporter. PMID28388411 protein binding is not itself a lipid-transfer measurement.

## New direct BP3761 structural support

Official RCSB entry/polymer/ligand JSONs were read at https://data.rcsb.org/rest/v1/core/entry/11HY and the corresponding11IF endpoint, with polymer_entity/.../1 and all nonpolymer entities archived here. Both deposited structures are linked to Q7VSZ6 and contain an exact 181-residue match to its mature residues27–207; the construct also contains the prefix MAHHHHHH. The source strain is B. pertussis Tohama I in the official entity record. Both contain the ligand PEF, DI-PALMITOYL-3-SN-PHOSPHATIDYLETHANOLAMINE. The full 189-residue construct is not identical to the 207-residue precursor. `bp3761-structure-proof.json` records the reproducible comparison.

This is direct deposited structural evidence for target phospholipid binding. It is not a peer-reviewed kinetics paper or a native flux measurement. The signal peptide, MlaC-specific PF05494/PIRSF004649 classification, cognate locus and lipid-bound target structure support a soluble periplasmic carrier core. The phospholipid-transfer activity is explicitly a conserved-function inference using the characterized MlaC mechanism, not a claimed direct BP3761 transfer assay. Neither native lipid selectivity nor native occupancy is established by the deposited DPPE complexes.

## PAO1 Ttg2D

Q9HVW4/PA4453 is the exact PAO1 target in PMID33837253. Frozen preflight/identity-proof.json compares the official UniProt sequence with RCSB6HSY/entity1: an exact193-residue mature segment, with construct additions distinguished from the215-residue precursor. Crystallography was performed with heterologously produced protein. Separately, His-tagged Ttg2D with its own signal peptide was recovered from the periplasm of a PAO1 deletion strain expressing the complementing construct. Its cargo and the purified-protein measurements support two diacyl phospholipids or one cardiolipin. Binding/reloading and native-host cargo are direct; membrane-to-membrane net flux and the complete PAO1 partner pair were not reconstituted in that study. The carrier activity is supported by the direct target evidence combined with its specific MlaC architecture and characterized Mla mechanism, with the assay limitation explicit.

No antibiotic export function is inferred from permeability/susceptibility phenotypes. No quantitative PAO1 loading stoichiometry is transferred to the Bordetella carrier.

## Review controls

Fresh QuickGO definitions are archived in go-terms.json. Phospholipid transfer requires movement through an aqueous phase while shielding cargo; binding alone is insufficient. Hence transfer cores above cite specific carrier/interface architecture and cognate system evidence in addition to binding, and are labeled inferred when no target transfer assay exists. Transport-complex subunits have contributes_to_molecular_function rather than an independent complete carrier activity.

Six genuine Falcon attempts each returned403; no generated report was invented. PAINT-loss checks found the five Bordetella proteins absent from cached reference trees, leaving exact lineage losses unassessed; this is not a negative proof of loss. PAO1 Ttg2D has no reported applicable loss. Two initial PAINT commands raced the shared download; sequential retries passed and the initial failures are retained. TreeGrafter sources are not challenged on donor counts or self-reference. Structured ancestry adjudication remains limited by target leaf availability.

The source hash ledger and preservation check establish immutable original rows, source bytes and frozen preflight files. The completed status signifies adjudication of all available rows and a source-bounded core synthesis, not completion of experimental knowledge.
