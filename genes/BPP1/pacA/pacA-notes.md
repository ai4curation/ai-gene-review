# pacA (P28813) Curation Notes — Escherichia phage P1

## Functional Summary
- **Gene symbol**: `pacA` (classical P1 complementation group `9` — amber mutants `am9.16`, `am31`, `am131` map to `pacA`).
- **Protein**: Terminase small subunit (PacA / TerS; 397 aa, ~44.8 kDa).
- **Biological role**: PacA is the DNA-recognition subunit of the heterooligomeric P1 terminase ("pacase") complex (`PacAB`). During lytic development, PacA specifically recognizes and binds the 162-bp packaging initiation site (`pac`), which is embedded within the `pacA` coding sequence itself and contains two clusters of hexanucleotide repeats (`5'-TGATCA/G-3'`) bearing seven `5'-GATC-3'` adenine-methylation targets [PMID:1538406, PMID:15489417].
- **Mechanism**:
  - PacA binds methylated `pac` DNA independently of PacB in a reaction requiring host DNA-bending factors IHF and/or HU, which bind an IHF site adjacent to the central 13-bp cleavage region to bring the two flanking `GATC`-repeat clusters together [PMID:15489417].
  - Both PacA and the large catalytic subunit PacB (`P27753`) are required to cleave `pac` and initiate unidirectional headful DNA packaging into proheads [PMID:1538406, PMID:15489417].
  - LC-MS/MS proteomics of CsCl-purified P1 virions also unexpectedly detected PacA associated with phage particles [PMID:35458408].
- **Relationship to `P40820` (`9`)**: UniProt entry `P40820` (`9`) is a 142-aa N-terminal fragment derived from the 3'-flanking region of `gene 10` (`lpa`) sequenced in Lehnherr et al. 1991 [PMID:1917870], before Skorupski et al. 1992 [PMID:1538406] sequenced the full `pacA` and `pacB` genes and demonstrated that classical `gene 9` (`am9.16`) is `pacA`.

## Review of Existing GOA Annotations
- `GO:0003677` (`DNA binding`, IEA, `GO_REF:0000043` UniProtKB-KW:KW-0238): **ACCEPT**. PacA is the sequence-specific DNA-binding small terminase subunit that recognizes the methylated `pac` site [PMID:1538406, PMID:15489417].
- `GO:0004518` (`nuclease activity`, IEA, `GO_REF:0000043` UniProtKB-KW:KW-0540): **REMOVE**. Although both PacA and PacB are required in vivo and in vitro for `pac` cleavage, in bacteriophage terminase complexes the small subunit (`PacA` / TerS) mediates sequence-specific DNA recognition and recruits the large subunit (`PacB` / TerL, `P27753`), whereas the catalytic Mg2+-dependent endonuclease and ATPase active sites reside in the large subunit (`PacB`) [PMID:1538406, PMID:15489417]. Assigning nuclease catalytic activity directly to the small subunit is an over-attribution from the holoenzyme name "pacase".
- `GO:0016787` (`hydrolase activity`, IEA, `GO_REF:0000043` UniProtKB-KW:KW-0378): **REMOVE**. Propagated from the same UniProt "Hydrolase / Nuclease" keyword assignment; catalytic hydrolysis (both phosphodiester cleavage and ATP hydrolysis) is performed by the large subunit PacB (`P27753`), not PacA.
