# SLC25A15 / ORNT1 (Q9Y619) review notes

## Identity and family
- Mitochondrial ornithine transporter 1 (ORNT1); Solute carrier family 25 member 15.
- 301 aa, mitochondrial carrier (SLC25 / TC 2.A.29) family: three Solcar repeats, six TM helices, MCP domain (UniProt Q9Y619).
- TCDB 2.A.29.19.2. Paralog SLC25A2/ORNT2 (~88% identical, retrotransposon-derived) has overlapping, broader specificity and partially compensates for ORNT1 loss.

## Core molecular function
- Mitochondrial inner-membrane ornithine/citrulline antiporter: imports cytosolic L-ornithine into the matrix in exchange for exporting matrix L-citrulline (with an H+ making transport electroneutral).
- UniProt FUNCTION: "Mitochondrial ornithine-citrulline antiporter ... Catalyzes the exchange between cytosolic ornithine and mitochondrial citrulline plus an H(+), the proton compensates the positive charge of ornithine thus leading to an electroneutral transport. Plays a crucial role in the urea cycle, by connecting the cytosolic and the intramitochondrial reactions of the urea cycle" (UniProt Q9Y619, [PubMed:12807890], [PubMed:22262851]).
- Rhea catalytic activity: RHEA:70787 L-citrulline(in) + L-ornithine(out) + H+(in) = L-citrulline(out) + L-ornithine(in) + H+(out).

## Broad basic-amino-acid specificity (in vitro)
- [PMID:12807890 "Both transport L-isomers of ornithine, lysine, arginine, and citrulline by exchange and by unidirectional mechanisms, and they are inactivated by the same inhibitors."] ORC1=ORNT1; ORC2=ORNT2.
- [PMID:12807890 "ORC2 has a broader specificity than ORC1, and L- and D-histidine, L-homoarginine, and D-isomers of ornithine, lysine, and ornithine are all substrates."]
- Km values (UniProt, PubMed:12807890): ornithine 0.22 mM, lysine 0.8 mM, arginine 1.58 mM, citrulline 2.52 mM — ornithine highest affinity, consistent with ornithine being the primary physiological substrate.
- Additional Rhea reactions in UniProt: L-arginine/L-ornithine antiport (RHEA:34991, EXP PubMed:12807890), L-ornithine/L-lysine antiport (RHEA:70799, EXP PubMed:12807890), plus by-similarity ornithine/H+ and lysine/H+ uniport.

## Substrate-specificity determinants
- [PMID:22262851 title "Substrate specificity of the two mitochondrial ornithine carriers can be swapped by single mutation in substrate binding site."] Mutagenesis (R179, E180, W224) alters relative ornithine vs arginine/lysine transport (UniProt MUTAGEN features).

## Localization
- Mitochondrial inner membrane; multi-pass membrane protein (UniProt SUBCELLULAR LOCATION; ISS from yeast ortholog Q12375). Original disease paper localized to mitochondrial membrane (EXP PubMed:10369256). HTP mito proteome (PMID:34800366).

## Urea cycle role & disease
- [PMID:10369256 "Our results show that ORNT1 encodes the mitochondrial ornithine transporter involved in UC function and is defective in HHH syndrome."]
- Neurospora crassa ARG13 / S. cerevisiae ARG11 are the fungal orthologs; identified ORNT1 by orthology; expression high in liver and dietary-protein regulated ([PMID:10369256]).
- HHH syndrome (hyperornithinemia-hyperammonemia-homocitrullinuria; MIM:238970; MONDO:0009393): autosomal recessive urea-cycle disorder from biallelic SLC25A15 LoF. Confirmed by dismech KB (Hyperornithinemia_Hyperammonemia_Homocitrullinuria_Syndrome.yaml). Many pathogenic HHH variants (G27R, E180K, F188del, R275Q, etc.) abolish/reduce transport.
- [PMID:12948741 "ORNT1, the gene defective in the hyperornithinemia-hyperammonemia-homocitrullinuria (HHH) syndrome, a urea cycle disorder"] ORNT2 rescues defective ornithine metabolism in HHH patient fibroblasts.

## GO term verification (OLS, current labels)
- GO:0000064 L-ornithine transmembrane transporter activity — MF, correct core.
- GO:1990575 mitochondrial L-ornithine transmembrane transport — BP; "L-ornithine is transported across a mitochondrial membrane" — correct core BP.
- GO:0000050 urea cycle — BP, correct.
- GO:0005743 mitochondrial inner membrane — CC, correct core location.
- GO:0043858 arginine:ornithine antiporter activity — MF; direction matches RHEA:34991; EXP-supported.
- GO:0015189 L-lysine / GO:0061459 L-arginine transmembrane transporter activity — IDA-supported broad specificity; non-core (physiological role is ornithine/citrulline).
- GO:0015297 antiporter activity — parent MF; correct but general.
- No dedicated "ornithine:citrulline antiporter" MF term exists in GO (searched OLS).

## Curation stance
- Core: GO:0000064 (MF), ornithine/citrulline antiport captured by GO:0043858 + GO:0015297, GO:1990575 (BP ornithine transport), GO:0000050 (urea cycle BP), GO:0005743 (CC).
- Non-core but experimentally real: lysine/arginine transporter MF + BP (broad basic-AA specificity in reconstituted system).
- Keep general CC (mitochondrion, mitochondrial membrane, membrane) as ACCEPT/non-core supporting the specific inner-membrane call.
- Reactome R-HSA-9956519 "SLC25A15 variants don't translocate ornithine and citrulline" is a variant/disease reaction but is used here to support the WT normal function annotations (GO:0005743, GO:0000064) — accept, these are correct for the gene.
