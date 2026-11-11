# BPP2 V (P31340 / SPIKE_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `V`
- **UniProt ID**: `P31340` (`SPIKE_BPP2`)
- **Protein**: Spike protein gpV (211 aa, 21.8 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:7483254** (Haggård-Ljungquist et al., 1995, *Virology*):
   - Sequenced P2 gene `V` and showed that `gpV` forms the small central spike at the tip of the P2 baseplate.
   - Quote: `"The V gene product is the small spike at the tip of the tail, and the J gene product lies at the edge of the baseplate."`
2. **PMID:21821878** (Yamashita et al., 2011, *Acta Crystallogr. F*):
   - Solved the high-resolution crystal structure of the C-terminal domain of P2 gpV (`gpV-C`), revealing an intertwined trimeric β-helix spearhead coordinating iron (`Fe`), calcium (`Ca`), and chloride (`Cl`) ions at its tip, and noted the absence of any ligand-binding pockets or clefts.
   - Quotes:
     - `"The structure is a triangular pyramid and looks like a spearhead composed of an intertwined β-sheet, a triple β-helix and a metal-binding region containing iron, calcium and chloride ions."`
     - `"Unfortunately, we did not find any ligand-binding pockets or clefts in the gpV-C structure."`
3. **PMID:22325780** (Browning et al., 2012, *Structure*):
   - Determined structures of the P2 gpV and phi92 gp138 central tail spikes (~10 Å diameter tip stabilized by an octahedral iron ion coordinated by six conserved histidine residues) and demonstrated that the iron-loaded gpV spike acts as a rigid mechanical drill bit that pierces the host lipid bilayer without unfolding during sheath contraction.
   - Quote: `"Both proteins form compact spikes with a ∼10Å diameter tip that is stabilized by a centrally positioned iron ion bound by six histidine residues. The accumulated data strongly suggest that, in the process of membrane penetration, the spikes are translocated through the lipid bilayer without undergoing major unfolding."`

## Annotation Review Decisions
- `GO:0019062` (`virion attachment to host cell`, IEA): **KEEP_AS_NON_CORE** — While the lateral tail fibers (`gpH`) mediate primary receptor recognition on LPS, the C-terminal apex of `gpV` contacts the host surface during the transition to irreversible binding and membrane puncturing.
- `GO:0044694` (`symbiont genome entry into host cell via pore formation in plasma membrane`, IEA): **MODIFY** to `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`).
- `GO:0046718` (`symbiont entry into host cell`, IEA): **MODIFY** to `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`).
- `GO:0046872` (`metal ion binding`, IEA): **KEEP_AS_NON_CORE** — `gpV` coordinates structural iron (`Fe2+/Fe3+`) and calcium (`Ca2+`) ions at its C-terminal apex to rigidify the membrane-piercing tip (`PMID:21821878`, `PMID:22325780`), which supports its core structural/piercing function (`GO:0039660`).
- `GO:0098003` (`viral tail assembly`, IEA): **ACCEPT** — `gpV` is essential for nucleation of the P2 baseplate hub and tail assembly (`Vam` mutants produce filled heads without tails).
- `GO:0098015` (`virus tail`, IEA): **MODIFY** to `GO:0098025` (`virus tail, baseplate`).
- `GO:0098025` (`virus tail, baseplate`, IEA): **ACCEPT**.
- `GO:0098670` (`entry receptor-mediated virion attachment to host cell`, IEA): **REMOVE** — Crystal structure analysis (`PMID:21821878`, `PMID:22325780`) explicitly demonstrated that `gpV` lacks any receptor/ligand-binding pockets or clefts and functions instead as a mechanical iron-stabilized membrane-piercing needle, while primary receptor binding is mediated by the `gpH` tail fibers.
- **NEW** `GO:0039660` (`structural constituent of virion`, IDA, `PMID:21821878`): X-ray crystal structures (`PMID:21821878`, `PMID:22325780`) and immunoelectron microscopy (`PMID:7483254`) establish `gpV` as the central trimeric spike of the P2 virion baseplate.
- **NEW** `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`, IDA, `PMID:22325780`): `gpV` forms the iron-loaded central baseplate spike that mechanically punctures the host cell outer membrane during sheath contraction to enable genome ejection.
