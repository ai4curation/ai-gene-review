# nadX (MJ0915) - L-aspartate dehydrogenase - Research Notes

## Gene Identity

- UniProt: Q58325 (ASPD_METJA)
- Locus: MJ0915
- Organism: Methanocaldococcus jannaschii (strain ATCC 43067 / DSM 2661)
- EC: 1.4.1.21
- Gene name: nadX

## Core Function: L-aspartate dehydrogenase in de novo NAD biosynthesis

NadX catalyzes the first committed step in the de novo NAD+ biosynthetic pathway from L-aspartate in archaea and some bacteria. It performs the NAD(P)-dependent oxidative deamination of L-aspartate to iminoaspartate, which is the substrate for the next enzyme in the pathway, quinolinate synthase (NadA).

This enzyme represents an alternative to the FAD-dependent L-aspartate oxidase (NadB) used in the classical bacterial NAD biosynthesis pathway (e.g., in E. coli). The key discovery paper is Yang et al. (2003), who identified this novel enzymatic activity in the Thermotoga maritima homolog TM1643 [PMID:12496312 "two different enzymes, an oxidase and a dehydrogenase, may have evolved to catalyze the first step of NAD biosynthesis in prokaryotes. TM1643 establishes a new class of amino acid dehydrogenases"].

## Key Biochemical Features

### Reaction catalyzed

L-aspartate + NAD(P)+ + H2O -> iminoaspartate -> (spontaneous) oxaloacetate + NH4+ + NAD(P)H

The iminoaspartate product is unstable in aqueous solution and spontaneously hydrolyzes to oxaloacetate and ammonia. The biologically relevant product is iminoaspartate, which is channeled to NadA for quinolinate synthesis before it can decompose.

### Cofactor specificity

The enzyme can use either NAD+ or NADP+ as electron acceptor. According to PubMed, kinetic characterization of the A. fulgidus homolog showed Km values for L-aspartate of 0.19 mM (with NAD+) and 4.3 mM (with NADP+), and Km values for NAD and NADP of 0.11 and 0.32 mM respectively [PMID:16731057, DOI:10.1016/j.bbapap.2006.04.006 "The enzyme specifically utilized L-aspartate as the electron donor, while either NAD or NADP could serve as the electron acceptor"].

### Structure

According to PubMed, the crystal structure of the T. maritima homolog (TM1643) revealed an N-terminal Rossmann fold domain with a bound NAD+ cofactor and a C-terminal alpha+beta domain, with the active site at the interface between the two domains [PMID:12496312, DOI:10.1074/jbc.M211892200 "The structure reveals the presence of an N-terminal Rossmann fold domain with a bound NAD(+) cofactor and a C-terminal alpha+beta domain"].

The crystal structure of the A. fulgidus homolog in complex with NAD and citrate (substrate analog) was determined at 1.9 A resolution, showing a dimeric enzyme with a closed conformation upon substrate binding [PMID:17651440, DOI:10.1111/j.1742-4658.2007.05961.x "The dimeric structure of A. fulgidus L-aspDH was refined at a resolution of 1.9 A...each subunit consists of two domains separated by a deep cleft containing an active site"].

### Oligomeric state

The enzyme forms a homodimer. According to PubMed, the A. fulgidus homolog was characterized as "a homodimeric protein with a molecular mass of about 48 kDa" [PMID:16731057, DOI:10.1016/j.bbapap.2006.04.006].

### Thermostability

The enzyme is highly thermostable, consistent with the hyperthermophilic lifestyle of M. jannaschii and related archaea. The A. fulgidus homolog showed an optimum temperature of about 80 degrees C and little loss of activity after incubation for 1 h at up to 80 degrees C [PMID:16731057].

## Pathway Context

The de novo NAD+ biosynthetic pathway from L-aspartate in prokaryotes proceeds:

1. L-aspartate -> iminoaspartate (NadB in bacteria via FAD-dependent oxidation, or NadX in archaea/some bacteria via NAD(P)-dependent dehydrogenation)
2. Iminoaspartate + dihydroxyacetone phosphate -> quinolinate (NadA, quinolinate synthase)
3. Quinolinate -> nicotinate mononucleotide (NadC, quinolinate phosphoribosyltransferase)
4. Further steps to NAD+

The discovery that NadX provides an alternative to NadB was a significant finding in comparative genomics [PMID:12496312 "our studies demonstrate that two different enzymes, an oxidase and a dehydrogenase, may have evolved to catalyze the first step of NAD biosynthesis in prokaryotes"].

## Taxonomic Distribution

Within the archaeal domain, homologs of L-aspartate dehydrogenase occur in many methanogenic species, but not in Thermococcales or Sulfolobales [PMID:16731057, DOI:10.1016/j.bbapap.2006.04.006 "Within the archaeal domain, homologues of this enzyme occurred in many Methanogenic species, but not in Thermococcales or Sulfolobales species"]. Some bacteria (e.g., Thermotoga maritima) also have NadX instead of NadB.

## Genome Context

The M. jannaschii genome was sequenced in 1996 [PMID:8688087, DOI:10.1126/science.273.5278.1058 "Complete genome sequence of the methanogenic archaeon, Methanococcus jannaschii"]. The nadX gene (MJ0915) was identified based on homology. In T. maritima, TM1643 was found in an operon with two other genes encoding enzymes involved in NAD biosynthesis [PMID:12496312].

## Important Note: Not Involved in Chorismate Biosynthesis

The UniProt entry includes a note about a role in chorismate biosynthesis. However, the primary literature does not support a direct role for NadX in chorismate biosynthesis. The enzyme's established function is exclusively in NAD+ biosynthesis, converting L-aspartate to iminoaspartate for quinolinate synthesis. While oxaloacetate (the spontaneous decomposition product) could theoretically enter other metabolic pathways, the biological function of NadX is specifically to produce iminoaspartate for NAD biosynthesis, not to supply oxaloacetate for the shikimate pathway.
