# Curation Notes: Bacillus phage phi29 Gene 9 (Tail knob protein gp9, P04331)

## Summary of Gene Function
- **Product**: Tail knob protein gp9 (UniProt `P04331`, 599 aa, ~67.7 kDa).
- **Structure & Stoichiometry**: Present in 6 copies (homohexamer) at the distal end of the phi29 tail, forming the bulk of the cylindrical tail knob distal to the dodecameric `gp11` lower collar and enclosing the distal tail-tip peptidoglycan hydrolase `gp13` prior to DNA ejection ([PMID:18606992](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_18606992.md), [9-uniprot.txt](file:///Users/cjm/.gemini/antigravity-cli/brain/4b846598-3920-4c66-ba84-db24d924c2d1/scratch/prd1_phi29/genes/BPPH2/9/9-uniprot.txt)).
- **Mechanism in DNA Ejection & Membrane Pore Formation**: Prior to infection, six flexible hydrophobic loops (L1 loops) plug the distal end of the tail tube, retaining the highly pressurized dsDNA genome. Upon adsorption and cell wall penetration, these hydrophobic loops exit the tube lumen and insert into the *Bacillus subtilis* cytoplasmic membrane to assemble a trans-envelope channel/pore (`GO:0044694`, `GO:0099002`) through which the viral genome is ejected into the host cytoplasm.

## Review of Existing GO Annotations
1. `GO:0044694` (`symbiont genome entry into host cell via pore formation in plasma membrane`, IEA `GO_REF:0000043`): **ACCEPT** — Directly reflects the hexameric hydrophobic loop channel formed by gp9 across the host plasma membrane during genome ejection.
2. `GO:0046718` (`symbiont entry into host cell`, IEA `GO_REF:0000043`): **TOO_GENERAL** — Entailed by the more specific entry terms `GO:0044694` and `GO:0099002` on this record.
3. `GO:0098015` (`virus tail`, IDA `PMID:18606992` and IEA `GO_REF:0000043`): **ACCEPT** — Supported by cryo-EM reconstruction of the phi29 tail in [PMID:18606992](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_18606992.md).
4. `GO:0098026` (`virus tail, tube`, IEA `GO_REF:0000043`): **ACCEPT** — gp9 forms the distal hexameric tube/knob structure continuous with the proximal `gp11` tail tube.
5. `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`, IEA `GO_REF:0000043`): **ACCEPT** — Core biological process mediated by the gp9 distal tail knob/tube.
