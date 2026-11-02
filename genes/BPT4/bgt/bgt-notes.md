# Curation Notes: Bacteriophage T4 `bgt` (UniProt P04547)

## Identity and Nomenclature
- **Gene symbol:** `bgt` (synonym: `β-gt`)
- **UniProt accession:** `P04547` (`BGT_BPT4`)
- **Protein name:** DNA beta-glucosyltransferase (EC 2.4.1.27)
- **Length:** 351 AA (40,653 Da)
- **Organism:** Enterobacteria phage T4 (`NCBITaxon:10665`)

## Summary of Experimental and Structural Evidence
- **Catalytic Activity and Mechanism:** `bgt` encodes DNA beta-glucosyltransferase (BGT), which transfers a beta-D-glucosyl moiety from UDP-alpha-D-glucose to 5-hydroxymethylcytosine (5hmC) residues in double-stranded T4 DNA (`Reaction=Transfers a beta-D-glucosyl residue from UDP-alpha-D-glucose to a hydroxymethylcytosine residue in DNA.; EC=2.4.1.27;`). BGT modifies approximately 30% of the 5hmC bases in the T4 genome (the remaining ~70% being alpha-glucosylated by AGT). De Waard et al. 1967 (PubMed 6078540) characterized the sequence specificity of T4 beta-glucosyltransferase relative to alpha-glucosyltransferase.
- **Structural Fold and Base Flipping:** Numerous high-resolution crystal structures of BGT in apo, UDP/UDP-glucose-bound, and abasic or 5hmC-DNA-bound states (e.g., PDB `1BGT`, `1BGU`, `1JEJ`, `1JG6`, `1JIX`, `1QKJ`, `2BGT`; Vrielink et al. 1994, PubMed 8020269; Moréra et al. 1999, PubMed 10581246; Larivière & Moréra 2002, PubMed 12218082) established BGT as the founding structural prototype of the **GT-B glycosyltransferase superfamily** (`InterPro:IPR014756`, `Pfam:PF01532`). BGT flips the target 5hmC nucleotide out of the DNA double helix into the catalytic cleft, where Asp100 acts as the general catalytic base and Arg195/Arg307 stabilize the departing UDP leaving group.
- **Role in Counter-Defense:** Like alpha-glucosylation by AGT, beta-glucosylation of 5hmC by BGT protects T4 genomic DNA from phage-encoded cytosine-specific nucleases and host restriction-modification and CRISPR-Cas9 systems (PubMed 22229759, PubMed 26081634).

## Review of Existing GO Annotations
1. `GO:0033821` (`DNA beta-glucosyltransferase activity`, IDA from `PMID:6078540` and IEA from `GO_REF:0000120`): **ACCEPT**. Directly captures the primary catalytic activity (EC 2.4.1.27) of BGT.
2. `GO:0016740` (`transferase activity`, IEA `GO_REF:0000043`) and `GO:0016757` (`glycosyltransferase activity`, IEA `GO_REF:0000043`): **MODIFY** to `GO:0033821` (`DNA beta-glucosyltransferase activity`), which is already annotated to the gene and provides the exact catalytic activity.
3. `GO:0006304` (`DNA modification`, IEA `GO_REF:0000041`): **ACCEPT**. Directly describes the covalent beta-glucosylation of 5hmC residues in T4 DNA.
4. `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`, IEA `GO_REF:0000120`): **ACCEPT**. Beta-glucosylation of 5hmC protects T4 DNA from host restriction endonucleases.
5. `GO:0052031` (`symbiont-mediated perturbation of host defense response`, IEA `GO_REF:0000043`) and `GO:0052170` (`symbiont-mediated suppression of host innate immune response`, IEA `GO_REF:0000043`): **MODIFY** to `GO:0099018` (`symbiont-mediated evasion of host restriction-modification system`), the specific descendant term already present on the gene.
