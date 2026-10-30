# nrtD review notes

## 2026-10-27: PCC 7942 native-system review

Reviewed all 7 seeded annotation rows for P38046, NCBITaxon:1140 (PCC 7942). Original annotation fields and both raw files were snapshotted before editing and retained. No NEW rows were introduced.

NrtD is the ATP-binding component of the high-affinity NrtABCD nitrate/nitrite transporter in Synechococcus elongatus PCC 7942. It works with NrtC to couple ATP use to substrate passage through NrtB at the cytoplasmic membrane. Native nrtD disruption abolishes the high-affinity uptake phase; NrtD lacks the additional regulatory extension present in NrtC.

One normal Falcon deep-research attempt with perplexity-lite fallback failed; no synthetic provider file was created. Manual primary-source review supplies the evidence below. Normal acquisition logs are in `.cache/module-audit-logs/nitrate-syne7-review/`.

Family grounding: target UniProt membership is PTHR42788:SF7, official PANTHER label **NITRATE ABC TRANSPORTER ATP-BINDING PROTEIN**, checked against `interpro/panther/panther.obo`. Broad family labels do not determine substrate specificity; a chloroplastic family name does not place a cyanobacterial protein in a chloroplast.

- [PMID:8437564 Identification and characterization of a gene cluster involved in nitrate transport in the cyanobacterium Synechococcus sp. PCC7942.] Primary PCC 7942 gene-cluster sequencing and native interruption phenotypes. Abstract read; subunit topology and ATP-binding assignments include sequence inference, not isolated-protein ATPase assays.
  NrtB is the hydrophobic membrane component of the binding-protein-dependent transporter. Supporting text: "NrtB is a hydrophobic protein having structural similarity to the integral membrane components of bacterial transport systems that are dependent on periplasmic substrate-binding proteins."
  NrtC has an N-terminal ATP-binding domain related to NrtD. Supporting text: "The N-terminal portion of NrtC (amino acid residues 1-254) and NrtD are 58% identical to each other in their amino acid sequences, and resemble the ATP-binding components of binding protein-dependent transport systems."
  Loss of NrtD removes the high-affinity phase of nitrate uptake. Supporting text: "The high-affinity phase of nitrate-dependent O2 evolution was absent in the nrtD mutant."
- [PMID:9341163 Involvement of the C-terminal domain of an ATP-binding subunit in the regulation of the ABC-type nitrate/nitrite transporter of the Cyanobacterium synechococcus sp. strain PCC 7942.] Primary PCC 7942 NrtC domain deletion, complementation and nitrate accumulation experiments. Full text read in the separately cached University of Seville PDF; methods specify the plasmid-cured PCC 7942 derivative R2-SPc. C-terminal regulation is not evidence for direct ammonium binding.
  NrtABCD mediates active uptake of both nitrate and nitrite. Supporting text: "an ATP-binding cassette transporter encoded by the genes nrtA, nrtB, nrtC, and nrtD mediates active transport of nitrate and nitrite"
  The C-terminal extension of NrtC participates in ammonium-promoted inhibition. Supporting text: "the C-terminal domain of NrtC is involved in the ammonium-promoted inhibition of the nitrate/nitrite transporter."

Annotation decisions:

- GO:0005524 ATP binding: ACCEPT. The target ABC nucleotide-binding domain and the primary sequence comparison support ATP binding. This is the energy-coupling portion of the transporter; ATP binding is distinct from ATP hydrolysis and is not being removed as a duplicate (PMID:8437564).
- GO:0005886 plasma membrane: ACCEPT. NrtB is the integral membrane component; the ATP-binding components NrtC and NrtD act on the cytoplasmic side of this membrane. This assignment combines native transport genetics with the conserved ABC architecture (PMID:8437564, PMID:9341163); it does not imply that an ATP-binding subunit is itself a transmembrane pore.
- GO:0015112 nitrate transmembrane transporter activity: MODIFY. nrtD contributes its ATP-binding component role to the ATP-coupled NrtABCD complex (PMID:8437564, PMID:9341163). ABC-type nitrate transporter activity is the supported descendant of nitrate transmembrane transporter activity. The complex-level annotation is evaluated as a component contribution, not a claim that this subunit alone transports nitrate.
- GO:0015414 ABC-type nitrate transporter activity: ACCEPT. The native NrtABCD system is an ABC transporter for nitrate and nitrite. nrtD contains the ATP-binding machinery and genetically contributes to uptake; this is a complex contribution rather than autonomous transport by a soluble ATPase (PMID:8437564, PMID:9341163).
- GO:0015706 nitrate transmembrane transport: ACCEPT. Native transporter-gene disruption and uptake measurements establish participation in high-affinity nitrate transport, with subunit roles resolved by sequence and domain studies. Nitrate transport remains a useful process assertion alongside the complex activity (PMID:8437564, PMID:9341163).
- GO:0016020 membrane: MODIFY. The evidence localizes the transporter to the cytoplasmic membrane. The parent membrane term is biologically true but can be refined to plasma membrane, already represented in this review.
- GO:0016887 ATP hydrolysis activity: ACCEPT. NrtC and NrtD are the conserved ABC energy-coupling components supported by native transport genetics and nucleotide-binding-domain architecture. ATPase activity is retained as the subunit-level activity; the cited native studies do not separately measure purified nrtD ATPase kinetics. ABC-type nitrate transporter activity is not an is_a descendant of ATP hydrolysis activity in the checked ontology.
