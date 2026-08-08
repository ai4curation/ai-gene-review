# ELOVL2 (Very long chain fatty acid elongase 2) — review notes

UniProt: Q9NXB9 (ELOV2_HUMAN), 296 aa. Gene ELOVL2 (synonyms ELG3, SSC2). HGNC:14416.
Chromosome 6. MANE-Select NM_017770.4 / NP_060240.3.

## Identity / family

- RecName "Very long chain fatty acid elongase 2"; AltNames "3-keto acyl-CoA synthase
  ELOVL2", "Very long chain 3-oxoacyl-CoA synthase 2", "ELOVL fatty acid elongase 2"
  [file:human/ELOVL2/ELOVL2-uniprot.txt "RecName: Full=Very long chain fatty acid elongase 2"].
- EC 2.3.1.199 [file:human/ELOVL2/ELOVL2-uniprot.txt "EC=2.3.1.199"].
- Belongs to the ELO family, ELOVL2 subfamily
  [file:human/ELOVL2/ELOVL2-uniprot.txt "Belongs to the ELO family. ELOVL2 subfamily."].
- Multipass ER membrane protein; 7 predicted TM helices; C-terminal di-lysine (KKAQ, res
  293-296) ER-retention motif
  [file:human/ELOVL2/ELOVL2-uniprot.txt "The C-terminal di-lysine motif may confer endoplasmic reticulum"].

## Molecular function (condensing enzyme / rate-limiting step)

- Catalyzes the FIRST and RATE-LIMITING reaction of the four-reaction microsomal fatty
  acid elongation cycle; ER-bound; adds 2 carbons per cycle to long- and very-long-chain
  fatty acids
  [file:human/ELOVL2/ELOVL2-uniprot.txt "Catalyzes the first and rate-limiting reaction of the four"].
- Condensing enzyme synthesizing polyunsaturated very long chain fatty acids (C20- and
  C22-PUFA), acting specifically toward polyunsaturated acyl-CoA, highest activity toward
  C20:4(n-6) acyl-CoA (arachidonoyl-CoA)
  [file:human/ELOVL2/ELOVL2-uniprot.txt "Condensing enzyme that catalyzes the synthesis of"].
- Core reaction (EC 2.3.1.199): a very-long-chain acyl-CoA + malonyl-CoA + H+ = a
  very-long-chain 3-oxoacyl-CoA + CO2 + CoA (RHEA:32727)
  [file:human/ELOVL2/ELOVL2-uniprot.txt "chain 3-oxoacyl-CoA + CO2 + CoA; Xref=Rhea:RHEA:32727,"].
- Substrate-specific reactions in UniProt include 20:4(n-6)->22:4(n-6) (RHEA:36475),
  22:4(n-6)->24:4(n-6) (RHEA:36479), 20:5(n-3)->22:5(n-3) (RHEA:36483), and
  22:5(n-3)->24:5(n-3) (RHEA:36491) — i.e. the C20/C22 PUFA elongations en route to DHA.
- GO:0009922 "fatty acid elongase activity" is defined by exactly this reaction
  (OLS: "a very-long-chain acyl-CoA + H+ + malonyl-CoA = a very-long-chain 3-oxoacyl-CoA
  + CO2 + CoA ... first (condensation) step of the four-step fatty acid elongation cycle").
  This is the correct, specific MF for ELOVL2.

## Experimental evidence for elongase activity / substrate specificity

- Yeast expression of human ELOVL2 ORF elongated both 20- and 22-carbon PUFA: 20:4n-6 ->
  22:4n-6, 22:4n-6 -> 24:4n-6, 20:5n-3 -> 22:5n-3, and 22:5n-3 -> 24:5n-3; identified as
  "very long chain PUFA specific elongation enzymes in the Sprecher pathway for DHA
  synthesis"
  [PMID:12371743 "the conversion of 20:4n-6 to 22:4n-6, 22:4n-6 to 24:4n-6, 20:5n-3 to 22:5n-3, and 22:5n-3 to 24:5n-3"]
  [PMID:12371743 "very long chain PUFA specific elongation enzymes in the Sprecher pathway for DHA synthesis"].
- Comprehensive in-vitro substrate specificity of all seven mammalian ELOVLs: "ELOVL2 and
  ELOVL5 preferentially elongated the polyunsaturated fatty acyl-CoAs" (ELOVL1/3/6 prefer
  saturated) [PMID:19575253 "ELOVL2 and ELOVL5 preferentially elongated the polyunsaturated fatty acyl-CoAs"].
- Ohno et al. determined precise substrate specificities of all ELOVLs by in-vitro
  analyses; the paper's headline gene is ELOVL1 (C24 sphingolipids) but ELOVL2 was assayed
  in the same panel [PMID:20937905 "we determined the precise substrate specificities of all the ELOVLs by in vitro analyses"].
- de Antueno et al. co-expressed human elongase + desaturase genes in yeast; two
  sequential elongations of 20:4n-6 and 20:5n-3 produced 24:4n-6 and 24:5n-3 (the
  ELOVL2-type C20->C22->C24 PUFA elongations feeding Delta6 desaturation)
  [PMID:11734209 "two sequential elongations, produced 24:4n-6 and 24:5n-3, respectively"].
- Note: PMID:10970790 (Reactome EXP for GO:0009922) is the cloning of HELO1 = human
  ELOVL5 (299 aa; elongates C18->C20 PUFA e.g. GLA->DGLA), NOT ELOVL2 (296 aa). It is an
  ELO-family elongase paper used by Reactome to support the generic elongase MF; per
  policy an EXP annotation is not removed (kept, flagged in review as likely
  paralog/ELOVL5 source).

## Pathway / biological process

- PATHWAY: "Lipid metabolism; polyunsaturated fatty acid biosynthesis"
  [file:human/ELOVL2/ELOVL2-uniprot.txt "Lipid metabolism; polyunsaturated fatty acid biosynthesis."].
- ELOVL2 performs the PUFA elongations of the omega-3 (and omega-6) very-long-chain
  pathway; it is essential/rate-limiting for the C22:5(n-3)->C24:5(n-3) step that (after
  Delta6 desaturation and peroxisomal beta-oxidation, the Sprecher pathway) yields DHA
  (C22:6 n-3). Reactome maps ELOVL2 to LA metabolism (R-HSA-2046105), ALA metabolism
  (R-HSA-2046106), and synthesis of very-long-chain fatty acyl-CoAs (R-HSA-75876).

## Localization

- Endoplasmic reticulum membrane; multipass membrane protein
  [file:human/ELOVL2/ELOVL2-uniprot.txt "Endoplasmic reticulum membrane"].
- Experimentally localized to ER / ER membrane by Ohno et al. (EXP/IDA PMID:20937905).

## Tissue expression

- UniProt TISSUE SPECIFICITY: liver and testis
  [file:human/ELOVL2/ELOVL2-uniprot.txt "Liver and testis."].
- HPA: tissue enhanced in brain, liver, placenta, retina
  [file:human/ELOVL2/ELOVL2-uniprot.txt "Tissue enhanced (brain, liver, placenta, retina)."].
- Physiologically important in spermatogenesis and retina (VLC-PUFA/DHA supply); ELOVL2
  promoter CpG methylation is a widely used epigenetic aging clock (background, not GO).

## Interactions

- SUBUNIT: interacts with TECR (trans-2-enoyl-CoA reductase), the terminal reductase of
  the elongation cycle [file:human/ELOVL2/ELOVL2-uniprot.txt "Interacts with TECR."]
  [PMID:38422897]. GOA records this as GO:0005515 protein binding IPI (with
  UniProtKB:Q9NZ01 = TECR). PMID:38422897 abstract focuses on HACD1/2-TECR complex and
  ELOVL structural similarity; the TECR-ELOVL2 interaction is the curator-supported claim.
- HuRI binary-interactome hits (PMID:32296183): FXYD6 (Q9H0Q3), IFITM3 (Q01628), MALL
  (Q13021), TMEM218 (A2RU14) — high-throughput Y2H membrane-protein interactions, no known
  functional consequence; bare "protein binding".
- PMID:20937905 IPI with UniProtKB:Q96G23 = CERS2 (ceramide synthase 2). In that paper
  ELOVL1 (not ELOVL2) is the elongase shown regulated by CERS2; the ELOVL2 IPI is a
  high-throughput/adjacent interaction with no established functional role for ELOVL2.

## Annotation review summary (rationale)

- Core MF: GO:0009922 fatty acid elongase activity (= the condensation step, EC 2.3.1.199).
  ACCEPT the EXP/IDA/IBA instances; the IEA/TAS duplicates are redundant but correct.
- Core BP: GO:0034626 fatty acid elongation, polyunsaturated fatty acid (IDA, PMID:12371743
  & PMID:20937905) and GO:0042761 very long-chain fatty acid biosynthetic process (IDA).
  These are the ELOVL2-specific processes.
- GO:0006636 unsaturated fatty acid biosynthetic process (IEA) — correct, general; keep.
- GO:0019367 fatty acid elongation, saturated FA and GO:0034625 monounsaturated FA (IBA/IEA):
  ELOVL2 is PUFA-specific and does NOT prefer saturated/monounsaturated substrates
  (PMID:19575253); these family-level IBA/IEA propagations are over-annotations for ELOVL2.
- GO:0030148 sphingolipid biosynthetic process (IBA): family-level; the C24-sphingolipid
  link is ELOVL1 (PMID:20937905), not ELOVL2 — over-annotation for ELOVL2.
- CC: GO:0005789 ER membrane (EXP/IDA/IBA/IEA) and GO:0005783 ER (IDA/IEA) — correct.
  GO:0016020 membrane (IEA) is a correct but non-informative parent.
- Reactome TAS ER-membrane and elongase-activity entries — correct, redundant with EXP.
- protein binding (IPI) rows: MARK_AS_OVER_ANNOTATED (bare protein binding, uninformative);
  TECR interaction is the one with a defined biological role (elongation-cycle partner).
</content>
</invoke>
