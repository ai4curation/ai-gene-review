# Curation Notes for Escherichia phage Mu A (P07636)

## Summary of Gene Function
- **Gene symbol**: `A` (locus tag `Mup03`; UniProt `P07636`, DDE-recombinase A / MuA transposase)
- **Organism**: *Escherichia phage Mu* (`NCBITaxon:2681603`)
- **Function**: MuA (`A`) is the 663-aa catalytic DDE-family transposase of bacteriophage Mu. It catalyzes both the initial non-replicative integration ("conservative" nick-join-repair transposition) of the incoming linear viral genome into the host chromosome and the subsequent ~100 rounds of lytic replicative transposition that amplify the phage genome [PMID:7912831, PMID:1847140, PMID:20167799, file:BPMU/A/A-uniprot.txt].
- **Domain Architecture & Mechanism**:
  - **Domain Ialpha (1-76)**: Winged HTH domain that binds the internal activation sequence (`IAS` / transpositional enhancer) overlapping operators `O1` and `O2`, competing directly with the lysogenic repressor Repc (`repc`) in the latency-replication decision [file:BPMU/A/A-uniprot.txt].
  - **Domain Ibeta-gamma (77-247)**: Binds the six attL (`L1-L3`) and attR (`R1-R3`) transposon end sequences [file:BPMU/A/A-uniprot.txt].
  - **Domain II (248-490)**: RNase H-like catalytic core housing the conserved acidic triad (`Asp-269`, `Glu-392`, `Asp-336`) that coordinates divalent cations (`Mg2+` or `Mn2+`) to catalyze 3'-end donor DNA nicking and concerted strand transfer into target DNA [PMID:7912831, file:BPMU/A/A-uniprot.txt].
  - **Domain IIIalpha (575-600) & IIIbeta (601-663)**: Domain IIIalpha harbors a cryptic `double-stranded DNA endonuclease activity` (`GO:1990238`) that works with host ClpX chaperone during initial infection to cleave the 5' flanking host DNA flaps attached to the incoming viral genome (`PMID:20167799`). Domain IIIbeta binds the target-selector ATPase MuB (`B`) and the host unfoldase ClpX [file:BPMU/A/A-uniprot.txt].

## Literature & Reference Notes
- **PMID:7912831** (Baker & Luo, 1994, PNAS): Identified `Asp-269` and `Glu-392` (along with `Asp-336`) as essential catalytic active-site residues of MuA transposase that coordinate divalent metal ions (`Mg2+`/`Mn2+`) for both donor DNA cleavage and strand transfer without impairing tetramer assembly.
- **PMID:1847140** (Surette et al., 1991, JBC): Demonstrated that MuB stimulates MuA-mediated strand cleavage and that nicking at both Mu ends is required for stable type 1 cleaved-donor transpososome complex formation.
- **PMID:20167799** (Choi & Harshey, 2010, PNAS): Discovered that the cryptic endonuclease activity in domain IIIalpha (`575-600`) of MuA removes the 5'-attached flanking DNA flaps after non-replicative integration of the infecting phage genome, requiring MuB and ClpX.

## Annotation Review Decisions
- `GO:0016874` (`ligase activity`, IEA from `KW-0436` / `EC=6.5.1.-`): `REMOVE`. MuA is a DDE-family transposase (`GO:0004803`) that catalyzes one-step isoenergetic transesterification (strand transfer) where the cleaved 3'-OH viral ends directly attack phosphodiester bonds in target DNA without ATP or NAD+ cofactor hydrolysis. Post-integration gap filling and covalent nick sealing are carried out by host DNA polymerase and ligase (`PMID:20167799`). Assigning `ligase activity` (`EC 6.5.1.-`) is a well-known UniProt keyword/EC mapping artifact on integrases/transposases.
- `GO:0004803` (`transposase activity`, IEA & IMP `PMID:7912831`): `ACCEPT` (both rows).
- `GO:1990238` (`double-stranded DNA endonuclease activity`, IDA `PMID:1847140` & IMP `PMID:20167799`): `ACCEPT` (both rows).
- `GO:0003677` (`DNA binding`, IEA): `ACCEPT`.
- `GO:0046872` (`metal ion binding`, IEA): `MODIFY` to `GO:0000287` (`magnesium ion binding`) (supported by `PMID:7912831` and UniProt `COFACTOR: Name=Mg(2+)`).
- `GO:0006313` (`DNA transposition`, IEA): `ACCEPT`.
- `GO:0015074` (`DNA integration`, IEA): `ACCEPT` (core step in both conservative integration of infecting phage DNA and replicative cointegrate formation).
- `GO:0039693` (`viral DNA genome replication`, IEA): `ACCEPT` (phage Mu replicates its genome strictly via MuA-catalyzed replicative transposition).
- `GO:0098689` (`latency-replication decision`, IEA): `ACCEPT` (MuA domain Ialpha competes with Repc at the IAS enhancer).
- `GO:0030430` (`host cell cytoplasm`, IEA): `ACCEPT`.
- `GO:0006281` (`DNA repair`, IEA): `KEEP_AS_NON_CORE` (MuA's domain IIIalpha 5'-flap endonuclease participates in post-integration resection of flanking host DNA flaps during repair of the integration intermediate, `PMID:20167799`).
- Broad parent IEA terms (`GO:0003676` `nucleic acid binding`, `GO:0004518` `nuclease activity`, `GO:0006260` `DNA replication`, `GO:0006310` `DNA recombination`, `GO:0016787` `hydrolase activity`, `GO:0032196` `transposition`, `GO:0140097` `catalytic activity, acting on DNA`): `TOO_GENERAL` as they are entailed by the accepted specific annotations.
- `NEW` `GO:0075713` (`establishment of integrated proviral latency`, `involved_in`): MuA catalyzes integration of the incoming phage genome into the host chromosome to establish the integrated prophage state.
