# Curation Notes: Bacteriophage T4 `stp` (UniProt P62765)

## Identity and Nomenclature
- **Gene symbol:** `stp` (synonym: `ac.6`)
- **UniProt accession:** `P62765` (`STP_BPT4`)
- **Protein name:** T4 Suppressor of prr (PrrC nuclease activation protein)
- **Length:** 26 AA (3,189 Da)
- **Organism:** Enterobacteria phage T4 (`NCBITaxon:10665`)

## Summary of Experimental Evidence
- **Inhibition of Host Type IC Restriction Systems (EcoPrrI and EcoR124I):** `stp` encodes a 26-amino-acid early phage polypeptide (`Pfam:PF08133`, `Nuclease_act`; `InterPro:IPR012585`, `Stp`) whose conserved N-proximal 18 residues bind the host Type IC restriction-modification complex EcoPrrI (`hsdRMS`), selectively abolishing its DNA restriction endonuclease activity without inhibiting its DNA methyltransferase activity (`Plays a role in the inactivation of several host DNA restriction systems including EcoprrI or EcoR124I. As a consequence, it activates the host anticodon nuclease PrrC. However, the phage-encoded RNA repair enzymes normally offset the damage. {ECO:0000269|PubMed:14507369, ECO:0000269|PubMed:1639077, ECO:0000269|PubMed:7791212}.`; Penner et al. 1995, PubMed 7791212).
- **Consequent Activation of the Latent Host PrrC Anticodon Nuclease:** In *E. coli* strains carrying the `prr` locus, the latent anticodon nuclease PrrC is kept inactive by association with the EcoPrrI (`HsdRMS`) restriction complex. When T4 Stp binds EcoPrrI to inhibit DNA restriction, it triggers a conformational change (together with dTTP and GTP hydrolysis) that unmasks PrrC, which then cleaves host $tRNA^{Lys}$ at the anticodon loop. Wild-type T4 repairs the cleaved $tRNA^{Lys}$ using its polynucleotide kinase/phosphatase (`pseT` / Pnkp) and RNA ligase 1 (`rli` / RnlA); in `pseT` or `rli` mutants, `prr` restricts T4 growth unless `stp` is mutated (`suppressor of prr`; Kaufmann 2000; Amitsur et al., PubMed 1639077, PubMed 14507369).
- **Critical Curation Finding — Mis-annotated `GO:0004518` (`nuclease activity`) from InterPro2GO:** Because Pfam `PF08133` (`Nuclease_act`, "PrrC nuclease activation protein") has "nuclease" in its description, `GO_REF:0000002` (InterPro2GO) erroneously mapped `GO:0004518` (`nuclease activity`) to `P62765`. Stp is a 26-residue regulatory peptide that inhibits the host EcoPrrI restriction endonuclease and allosterically activates the host PrrC anticodon nuclease; Stp itself has no catalytic nuclease activity.

## Review of Existing GO Annotations
1. `GO:0004518` (`nuclease activity`, IEA `GO_REF:0000002`): **REMOVE**. Stp is a 26-amino-acid regulatory peptide (`PF08133`) that inhibits the host EcoPrrI restriction enzyme and triggers activation of the host PrrC anticodon nuclease; Stp itself is not a nuclease.
2. `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`, IEA `GO_REF:0000043`): **ACCEPT**. Captures the primary adaptive function of Stp in inhibiting host Type IC restriction-modification systems (EcoPrrI and EcoR124I).
3. `GO:0050792` (`regulation of viral process`, IEA `GO_REF:0000002`), `GO:0052031` (`symbiont-mediated perturbation of host defense response`, IEA `GO_REF:0000043`), and `GO:0052170` (`symbiont-mediated suppression of host innate immune response`, IEA `GO_REF:0000043`): **MODIFY** to `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`), the specific descendant process already annotated on the gene.
