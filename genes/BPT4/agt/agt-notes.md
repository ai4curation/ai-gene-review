# Curation Notes: Bacteriophage T4 `agt` (UniProt P04519)

## Identity and Nomenclature
- **Gene symbol:** `agt` (synonym: `α-gt`)
- **UniProt accession:** `P04519` (`AGT_BPT4`)
- **Protein name:** DNA alpha-glucosyltransferase (EC 2.4.1.26)
- **Length:** 400 AA (46,657 Da)
- **Organism:** Enterobacteria phage T4 (`NCBITaxon:10665`)

## Summary of Experimental and Structural Evidence
- **Catalytic Activity and Substrate Specificity:** `agt` encodes DNA alpha-glucosyltransferase (AGT), which catalyzes the transfer of an alpha-D-glucosyl residue from UDP-alpha-D-glucose to 5-hydroxymethylcytosine (5hmC) residues in double-stranded T4 DNA (`Reaction=Transfers an alpha-D-glucosyl residue from UDP-alpha-D-glucose to a hydroxymethylcytosine residue in DNA.; EC=2.4.1.26;`). About 70% of 5hmC residues in T4 genomic DNA are alpha-glucosylated by AGT, while the remaining ~30% are beta-glucosylated by BGT (`bgt`). The specificity of T4 alpha- and beta-glucosyltransferases on hydroxymethylcytosine DNA was characterized biochemically by de Waard et al. 1967 (PubMed 6078540).
- **Structural Fold:** Crystal structures of T4 AGT (PDB `1NVK`, `1NZD`, `1NZF`, `1YA6`; Larivière et al. 2003, PubMed 12547206; Larivière et al. 2005, PubMed 15701522) show that AGT is a monomer adopting the two-domain GT-B glycosyltransferase fold (`InterPro:IPR045017`, `Pfam:PF06508`).
- **Coupling to DNA Replication:** Sommer et al. 2004 (PubMed 15381072) demonstrated that AGT interacts directly with the T4 sliding clamp protein gp45, coupling 5hmC alpha-glucosylation to ongoing DNA replication immediately after synthesis.
- **Role in Counter-Defense:** Glucosylation of 5hmC into glucosyl-5-hydroxymethylcytosine (glc-HMC) protects the T4 genome from T4's own cytosine-specific nucleases (such as DenA and DenB) and from host restriction-modification systems, and also impedes host CRISPR-Cas9 cleavage (Bryson et al. 2015, PubMed 26081634; Vlot et al. 2018).

## Review of Existing GO Annotations
1. `GO:0033820` (`DNA alpha-glucosyltransferase activity`, IDA from `PMID:6078540` and IEA from `GO_REF:0000003`): **ACCEPT**. Directly captures the primary catalytic activity (EC 2.4.1.26) of AGT.
2. `GO:0016740` (`transferase activity`, IEA `GO_REF:0000043`) and `GO:0016757` (`glycosyltransferase activity`, IEA `GO_REF:0000043`): **MODIFY** to `GO:0033820` (`DNA alpha-glucosyltransferase activity`), which is already annotated to the gene and provides the precise enzymatic activity.
3. `GO:0006304` (`DNA modification`, IEA `GO_REF:0000041`): **ACCEPT**. Accurately describes the core biological process of post-replicative covalent modification of 5hmC in phage DNA.
4. `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`, IEA `GO_REF:0000043`): **ACCEPT**. Glucosylation of 5hmC blocks cleavage by host restriction endonucleases.
5. `GO:0098672` (`symbiont-mediated suppression of host CRISPR-cas system`, IEA `GO_REF:0000043`): **ACCEPT**. Glucosylation of 5hmC inhibits CRISPR-Cas9 targeting of T4 DNA (PubMed 26081634).
6. `GO:0039504` (`symbiont-mediated suppression of host adaptive immune response`, IEA `GO_REF:0000043`): **MODIFY** to `GO:0098672` (`symbiont-mediated suppression of host CRISPR-cas system`), the specific descendant already annotated on the gene.
7. `GO:0052170` (`symbiont-mediated suppression of host innate immune response`, IEA `GO_REF:0000043`): **MODIFY** to `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`), the specific descendant already annotated on the gene.
8. `GO:0052031` (`symbiont-mediated perturbation of host defense response`, IEA `GO_REF:0000043`): **MODIFY** to both `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`) and `GO:0098672` (`symbiont-mediated suppression of host CRISPR-cas system`).
