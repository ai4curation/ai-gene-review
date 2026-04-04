# mbiA (htgA/htpY) - Research Notes

## Identity and naming

MbiA (P28697, b0012) is a small (161 aa, 17.6 kDa) uncharacterized protein in E. coli K12. It has had a confusing naming history:

- **htgA**: Name assigned by James et al. 1993 [PMID:8400364, "One of the ORFs (htgA) is preceded by a -10 promoter sequence which is identical to that of the dnaK sigma 32 P1 promoter, and thus suggests that htgA could be a heat-shock gene"], based on sequence upstream of dnaK.
- **htpY**: Name assigned by Missiakas et al. 1993 [PMID:8478327, "We have identified a new heat shock gene, designated htpY, located 700 bp upstream of the dnaK dnaJ operon"], who characterized it as a heat shock gene under sigma-32 control.
- **mbiA**: Current name, standing for "modifier of biofilm" based on the Salmonella orthologue Q8XA70 (UniProtKB annotation by similarity, ECO:0000250).

**CRITICAL**: The heat shock role originally attributed to htgA/htpY was later contradicted. Nonaka et al. 2006 [PMID:16818608] showed that mbiA is NOT induced by sigma-32 (rpoH), despite the earlier claims.

## Overlapping gene architecture

MbiA is encoded entirely within the yaaW gene on the opposite (antisense) strand [PMID:18226237]. Delaye et al. 2008 proposed that htgA arose by "overprinting" -- de novo gene birth from point mutations creating a novel ORF within the existing yaaW gene. They coined the term "janolog" for this relationship. [PMID:18226237, "The htgA gene coding for a positive regulator of the sigma 32 heat shock promoter arose by point mutation in a 123/213 phase within an open reading frame (yaaW) of unknown function"]

This means disruptions of one gene typically disrupt the other as well, complicating functional studies.

## Phenotype and functional evidence

Fellner et al. 2014 [PMID:24111745] is the key functional study:
- Both htgA and yaaW promoters are active in E. coli O157:H7 (GFP fusions)
- Strand-specific stop codon mutations in each gene showed differential phenotypes in biofilm formation and metabolite levels
- "Both mutants exhibited differential phenotypes in biofilm formation and metabolite levels in a nontargeted analysis, suggesting that both are functional despite YaaW but not HtgA could be expressed"
- The mbiA/htgA protein itself could NOT be detected by expression studies (YaaW could)
- Full-length htgA is restricted to Escherichia and Shigella
- Shows evidence of purifying selection, indicating it is functional
- Nonessential gene

## InterPro domains

P28697 has NO InterPro domain annotations whatsoever. The protein has no recognizable domains, families, or signatures in InterPro. This is consistent with it being an orphan gene that arose de novo by overprinting.

## Protein expression concerns

The UniProt evidence level is PE 2 (evidence at transcript level), meaning the protein has NOT been directly detected by proteomics or other protein-level methods. Fellner et al. 2014 noted that YaaW but not HtgA could be expressed, raising questions about whether the mbiA protein is actually produced at physiologically relevant levels.

## Key references

1. PMID:8400364 - James et al. 1993 - Original identification of htgA ORF upstream of dnaK
2. PMID:8478327 - Missiakas et al. 1993 - Characterization of htpY as heat shock gene
3. PMID:16818608 - Nonaka et al. 2006 - Showed mbiA is NOT part of sigma-32 regulon
4. PMID:18226237 - Delaye et al. 2008 - Origin by overprinting within yaaW
5. PMID:24111745 - Fellner et al. 2014 - Phenotype: biofilm effects, orphan gene characterization
6. PMID:1630901 - Yura et al. 1992 - Genome sequencing (0-2.4 min region)
7. PMID:9278503 - Blattner et al. 1997 - Complete E. coli K-12 genome
8. PMID:16738553 - Hayashi et al. 2006 - Highly accurate K-12 genome sequences

## Summary assessment

MbiA is a poorly characterized orphan protein with no known molecular function, no recognizable domains, and no direct protein-level detection. The strongest functional evidence comes from Fellner et al. 2014 showing differential biofilm phenotypes upon gene disruption, though the overlapping yaaW gene complicates interpretation. The original heat shock role has been refuted. The "modifier of biofilm" name comes from the Salmonella orthologue Q8XA70 by similarity annotation.
