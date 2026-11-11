# Curation Notes: Bacteriophage T4 `denA` (UniProt P07059)

## Identity and Nomenclature
- **Gene symbol:** `denA`
- **UniProt accession:** `P07059` (`DENA_BPT4`)
- **Protein name:** Endonuclease II (EC 3.1.21.8; T4 deoxyribonuclease II; EndoII)
- **Length:** 136 AA (15,794 Da)
- **Organism:** Enterobacteria phage T4 (`NCBITaxon:10665`)

## Summary of Experimental and Structural Evidence
- **Catalytic Activity and Substrate Specificity:** `denA` encodes Endonuclease II (EndoII), a divalent metal ion ($Mg^{2+}$)-dependent, sequence-context-sensitive DNA endonuclease belonging to the GIY-YIG nuclease superfamily (`Pfam:PF01541`, `InterPro:IPR000305`). EndoII catalyzes single-strand nicking (and double-strand cleavage at adjacent nicks) of unmodified cytosine-containing host DNA (`Catalyzes nicking of the bottom strand of double-stranded DNA between the first and second base pair to the right of a top-strand CCGC motif. Does not cleave native phage DNA, which contains 5-hydroxymethylcytosine instead of cytosine.`; Carlson et al., PubMed 18539732, PubMed 19666720).
- **Quaternary Structure and Mechanism:** Crystal structure and biochemical analysis of the catalytically inactive E118A mutant of EndoII (PDB `2WSH`; Andersson et al. 2010, PubMed 20156453; Lagerbäck et al. 2009, PubMed 19666720) demonstrated that EndoII forms a dimer-of-dimers homotetramer that simultaneously binds two dsDNA duplexes (`SUBUNIT: Homotetramer. {ECO:0000269|PubMed:19666720, ECO:0000269|PubMed:20156453}.`).
- **Biological Role in Host DNA Degradation:** EndoII initiates the degradation of the *E. coli* host chromosome during early T4 infection, generating nicked and fragmented host dsDNA that is subsequently degraded by the gp46/gp47 exonuclease complex and Endonuclease IV (`denB`) to scavenge dNMPs for phage DNA synthesis (`Contributes to the degradation of host DNA, permitting the scavenging of host-derived nucleotides for phage DNA synthesis (PubMed:18539732, PubMed:19666720).`).

## Review of Existing GO Annotations
1. `GO:0004519` (`endonuclease activity`, IEA `GO_REF:0000120`): **ACCEPT**. Directly captures the core enzymatic activity of DenA (Endonuclease II, EC 3.1.21.8).
2. `GO:0004518` (`nuclease activity`, IEA `GO_REF:0000043`) and `GO:0016787` (`hydrolase activity`, IEA `GO_REF:0000043`): **MODIFY** to `GO:0004519` (`endonuclease activity`), which is already annotated to the gene and more specific.
3. `GO:0003677` (`DNA binding`, IEA `GO_REF:0000043`): **ACCEPT**. EndoII directly binds cytosine-containing dsDNA recognition sequences (`5'-GRCCG-3'`) as a homotetramer bridging two DNA duplexes.
4. `GO:0046872` (`metal ion binding`, IEA `GO_REF:0000120`): **MODIFY** to `GO:0000287` (`magnesium ion binding`), as UniProt and biochemical studies specifically establish $Mg^{2+}$ as the catalytic cofactor (`Cofactor: Name=Mg(2+); Xref=ChEBI:CHEBI:18420;`).
5. `GO:0099015` (`degradation of host chromosome by virus`, IEA `GO_REF:0000043`): **ACCEPT**. Directly captures the primary biological role of DenA in initiating degradation of the cytosine-containing host chromosome during T4 infection.
6. `GO:0039657` (`symbiont-mediated suppression of host gene expression`, IEA `GO_REF:0000043`): **KEEP_AS_NON_CORE**. While degradation of the host chromosome abolishes host transcription, this is a downstream consequence of host DNA degradation (`GO:0099015`) rather than a direct transcriptional regulatory activity (unlike Alc or AsiA).
