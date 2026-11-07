# Msed_1423 (A4YGM9) notes

Metallosphaera sedula DSM 5348, unreviewed UniProt entry A4YGM9, "3-hydroxyacyl-CoA
dehydrogenase" (EC 1.1.1.35), 391 aa.

Automated deep research was unavailable for this review, so no `-deep-research-*.md` file
exists. Literature was found by a Europe PMC full-text search for "Msed_1423" (4 hits:
PMID:32218776, PMID:34290692, PMID:33472982, PMID:25939834) and by reading the cached
papers directly.

## Domain architecture (UniProt)

- Pfam PF02737 3HCDH_N (NAD-binding Rossmann domain) at 3-177; two PF00725 3HCDH
  C-terminal domains at 183-277 and 298-388. No crotonase domain, unlike the bifunctional
  paralog Msed_0399. PANTHER PTHR48075:SF5 "3-hydroxybutyryl-CoA dehydrogenase"; FunFam
  "Fatty oxidation complex, alpha subunit". [file:METS5/Msed_1423/Msed_1423-uniprot.txt]

## Biochemistry (Liu, Huber & Berg 2020)

- Recombinant His-tagged enzyme purified from E. coli. [PMID:32218776 "The heterologously
  produced His10-tagged (S)-3-hydroxybutyryl-CoA dehydrogenases Msed_1423 and Msed_0389 as
  well as crotonyl-CoA hydratases Msed_0336 and Msed_0384 were purified using affinity
  chromatography."]
- Activity and substrate affinity: [PMID:32218776 "The purified recombinant Msed_0389 and
  Msed_1423 catalyzed the NAD-dependent oxidation of (S)-3-hydroxybutyryl-CoA to
  acetoacetyl-CoA and were highly specific for their substrate (Km 2.6 and 5 μM,
  respectively; Table 3)."]
- Table 3 (Msed_1423, extrapolated to 75 °C): (S)-3-hydroxybutyryl-CoA Vmax 96 U/mg,
  Km 0.005 mM, kcat/Km 14,947; NAD Km 0.03 mM, kcat/Km 2,128; NADP Vmax 86 U/mg,
  Km 5.1 mM, kcat/Km 13. So NADP+ is a very poor cosubstrate: about 170-fold higher Km and
  160-fold lower efficiency. This justifies GO:0003857 (NAD+) over GO:0008691 (defined by
  GO with NADP+, EC 1.1.1.157).
- Substrate range: [PMID:32218776 "Both enzymes were not active with
  (S)-3-hydroxyoctanoyl-CoA."] Stereospecificity versus (R)-3-hydroxybutyryl-CoA is not
  reported for Msed_1423 (the (R)-isomer test in Table 4 concerns the crotonases).
- Efficiency vs Msed_0399: [PMID:32218776 "Their kcat/Km values were 3- and 20-fold higher
  than the corresponding value of Msed_0399 in (S)-3-hydroxybutyryl-CoA dehydrogenase
  reaction (Table 3)."]

## Physiological role

- Gene context: [PMID:32218776 "This protein is clustered together with two specific
  enzymes of the HP/HB cycle, succinic semialdehyde reductase Msed_1424 and acryloyl-CoA
  reductase Msed_1426 (Figure 2B), further supporting its involvement in autotrophic CO2
  fixation."]
- Distribution: [PMID:32218776 "The only two genes that are (almost) universally
  distributed in Sulfolobales are the crotonase Msed_0566 gene and the dehydrogenase
  Msed_1423 gene"]; absent only from S. acidocaldarius, which cannot grow autotrophically.
- Conclusion: [PMID:32218776 "show that Msed_1423 is the main (S)-3-hydroxybutyryl-CoA
  dehydrogenase in the HP/HB cycle in Sulfolobales."] Estimated 1.7% of cellular protein.
  The conclusion is inferential (kinetics, gene context, distribution, transcriptomics);
  no mutant exists.
- Restated in [PMID:33472982 "in M. sedula, the (S)-3-hydroxybutyryl-CoA dehydrogenase
  reaction is primarily catalyzed by Msed_1423 (which is universally found in autotrophic
  Sulfolobales)"].
- Thaumarchaeal comparison: Nmar_1028 is homologous (42% identity) but proposed to be
  recruited independently [PMID:34290692 "It appears that despite their homology, these
  three proteins evolved independently from each other, confirming the proposed convergent
  evolution of HP/HB cycle in Cren- and Thaumarchaeota."]
- PMID:25939834 (HhcR regulon, comparative genomics) mentions Msed_1423 in its full text
  per Europe PMC, but only the abstract is cached, so it is not cited in the review.

## Annotation decisions

- GO:0003857 ACCEPT (core). GO:0016491, GO:0016616 MODIFY -> GO:0003857.
- GO:0070403 NAD+ binding KEEP_AS_NON_CORE (correct cofactor, unlike Msed_0709).
- GO:0006631 fatty acid metabolic process MARK_AS_OVER_ANNOTATED: InterPro2GO family
  transfer; enzyme inactive on C8, gene in the CO2-fixation cluster. (Msed_0399, which acts
  on C8 and clusters with beta-oxidation genes, keeps this term as non-core.)
- NEW GO:0015977 carbon fixation (IDA, PMID:32218776), with the proposed
  "carbon fixation by 3-hydroxypropionate/4-hydroxybutyrate cycle" child, as in the
  Msed_0709 and Msed_2001 reviews. GO:0043427 (Chloroflexus cycle) not used.
- The module hbdh step (GO:0003857, Msed_1423 main representative) is consistent with
  this review.
