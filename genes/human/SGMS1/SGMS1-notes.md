# SGMS1 (human) review notes

UniProt: Q86VZ5 (SMS1_HUMAN), gene SGMS1, aka MOB / SMS1 / TMEM23. 413 aa, EC 2.7.8.27.
HGNC:29799. Chromosome 10.

## Core biology (grounded in UniProt file)

SGMS1 is **sphingomyelin synthase 1** = phosphatidylcholine:ceramide cholinephosphotransferase 1.
It catalyzes the final, committed step of sphingomyelin (SM) biosynthesis: transfer of the
phosphocholine head group of **phosphatidylcholine (PC)** onto **ceramide (CER)**, forming
**sphingomyelin (SM)** and **diacylglycerol (DAG)** as by-product. The reaction is reversible and its
direction depends on CER/DAG levels in Golgi membranes.

[file:human/SGMS1/SGMS1-uniprot.txt "Catalyzes the reversible transfer of phosphocholine moiety in sphingomyelin biosynthesis: in the forward reaction transfers phosphocholine head group of phosphatidylcholine (PC) on to ceramide (CER) to form ceramide phosphocholine (sphingomyelin, SM) and diacylglycerol (DAG) as by-product"]

[file:human/SGMS1/SGMS1-uniprot.txt "Major sphingomyelin synthase at the Golgi apparatus"]

Substrate specificity: uses PC (and PE for CPE), **NOT** free phosphorylcholine or CDP-choline.
[file:human/SGMS1/SGMS1-uniprot.txt "Does not use free phosphorylcholine or CDP-choline\nCC       as donor"] (quote spans a wrapped line in the file; see UniProt FUNCTION comment.)

Reaction (RHEA:18765, EC 2.7.8.27):
[file:human/SGMS1/SGMS1-uniprot.txt "an N-acylsphing-4-enine + a 1,2-diacyl-sn-glycero-3-\nCC         phosphocholine = a sphingomyelin + a 1,2-diacyl-sn-glycerol"] (wrapped).

## Localization

Golgi apparatus membrane, multi-pass membrane protein.
[file:human/SGMS1/SGMS1-uniprot.txt "SUBCELLULAR LOCATION: Golgi apparatus membrane"]
[file:human/SGMS1/SGMS1-uniprot.txt "Multi-pass membrane protein"]

SMS1 is the Golgi-localized isoform; its paralog SMS2 is mainly at the plasma membrane
(the isoform doing the plasma-membrane share of SM synthesis).
[PMID:14685263 "Whereas human SMS1 is localised to the Golgi, SMS2 resides primarily at the plasma membrane."]
SMS1 mainly responsible for de novo SM synthesis using CERT-delivered ceramide at the trans-Golgi.
[PMID:30242129 "SMS1 is localized mainly in the medial / trans -Golgi"]
[PMID:30242129 "Newly synthesized Cer is transported to the trans -Golgi in a Cer transport protein (CERT)–dependent manner for SM synthesis."]

## Topology / catalytic residues

6 TM helices; active site residues Ser283/His285/His328/Asp332 (all Ala mutants abolish activity).
[file:human/SGMS1/SGMS1-uniprot.txt "S->A: Completely abolishes enzyme activity."]
SAM domain at N-terminus (aa 7-70). N-terminal SAM mediates heteromeric complex with GCS.

## Functional coupling to signaling lipids

By consuming pro-apoptotic ceramide and generating pro-mitogenic DAG, SMS1 couples SM synthesis
to signaling. SM is a structural component of membrane rafts.
[file:human/SGMS1/SGMS1-uniprot.txt "Regulates receptor-mediated signal transduction via mitogenic DAG and\nCC       proapoptotic CER"] (wrapped)
[PMID:14685263 "This reaction is catalysed by SM synthase, an enzyme whose biological potential can be judged from the roles of diacylglycerol and ceramide as anti- and proapoptotic stimuli, respectively."]
[PMID:17982138 "SMS1 and SMS2 are key factors in the control of SM and DAG levels within the cell and thus influence apoptosis."]

## DAG at Golgi / secretory transport

SMS1 modulates a biologically active Golgi DAG pool that recruits DAG-binding proteins (PKD/PRKD1).
[PMID:18370930 "directly implicate SMS1 and SMS2 as regulators of DAG-binding proteins in the Golgi apparatus."]
[file:human/SGMS1/SGMS1-uniprot.txt "Plays a\nCC       role in secretory transport via regulation of DAG pool at the Golgi\nCC       apparatus and its downstream effects on PRKD1"] (wrapped)

## SMS1-GCS complex (glucosylceramide branch point)

SMS1 forms a heteromeric complex with glucosylceramide synthase (GCS/UGCG); complex increases
SM synthesis and decreases GlcCer synthesis — controls the metabolic fate of ceramide at the Golgi.
[PMID:30242129 "formation of the SMS1–GCS heteromeric complex increases SM synthesis and decreases GlcCer synthesis"]
[file:human/SGMS1/SGMS1-uniprot.txt "Can form\nCC       a heteromeric complex with glucosylceramide synthase (GCS) increasing\nCC       SMS activity and reducing glucosylceramide synthesis"] (wrapped)

This underpins the EXP annotation to GO:0046317 regulation of glucosylceramide biosynthetic process.

## Ancillary catalytic activities

- Ceramide phosphoethanolamine (CPE) synthase activity: transfers phosphoethanolamine from PE onto
  ceramide (By similarity in human; demonstrated for mouse Sms1 in PMID:25605874).
  [PMID:25605874 "expression of Sms1 or Sms2 in SF9 insect cells significantly increased not only SM but also CPE formation, indicating that SMS1 also has CPE synthase activity."]
  NOTE: GO:0002950 (ceramide phosphoethanolamine synthase activity) definition uses CDP-ethanolamine as
  donor, whereas SMS1 uses PE. The GO term is nonetheless the standard CPE-synthase MF term used by GOA.
- PC-phospholipase C (PC-PLC) activity: SMS1 can hydrolyze PC (and PE) to DAG even without ceramide.
  [PMID:37715942 "we found that SMS1 possesses DG-generating activities via hydrolysis of PC and\nphosphatidylethanolamine (PE) in the absence of ceramide"] (wrapped in abstract)
  [PMID:37715942 "SMS1 is a unique enzyme with PC-PLC/PE-PLC/SMS/CPES activities."]
  D609 (PC-PLC/SMS inhibitor) inhibits only the SMS activity; Mn2+ inhibits only PC-PLC.

## GO term-definition caveats (do not REMOVE experimental annotations)

- GO:0047493 "ceramide cholinephosphotransferase activity" is defined as CDP-choline + ceramide =
  CMP + sphingomyelin (a CDP-choline–dependent reaction). SGMS1 explicitly does NOT use CDP-choline
  (UniProt). The chemically correct MF is GO:0033188 sphingomyelin synthase activity (PC donor).
  The IBA + IDA(PMID:14685263) annotations to GO:0047493 are therefore MODIFY → GO:0033188.
  (PMID:14685263 is EXP/full-text; per policy the IDA is MODIFIED, not removed.)

## Isoforms

Isoform 2 (Q86VZ5-2, VSP_027223/VSP_027224) lacks aa 1-199 (most of cytoplasmic + SAM + first TMs);
likely non-catalytic. Not separately GO-annotated in GOA.

## Disease / physiology

SMS1 loss associated (in the primary literature cited by PMID:37715942 abstract) with lipodystrophy,
deafness, thrombasthenia. Overexpression in mouse increases atherogenic potential (UniProt MISCELLANEOUS).

## Reference relevance summary

- PMID:14685263 (Huitema 2004): HIGH — identified SMS family; SMS1 Golgi; PC→ceramide; full text.
- PMID:14976195 (Yamaoka 2004): HIGH — expression cloning of human SMS1, SM synthase activity, growth.
- PMID:17449912 (Tafesse 2007): HIGH — SMS1 = key Golgi SM synthase in HeLa; Golgi localization.
- PMID:17982138 (Ding 2008): HIGH — SMS1 controls cellular SM & DAG; apoptosis link.
- PMID:18370930 (Villani 2008): HIGH — SMS1 regulates Golgi DAG pool / PKD.
- PMID:30242129 (Hayashi 2018): HIGH — SMS1-GCS complex; trans-Golgi; CERT; regulates GlcCer.
- PMID:25605874 (Ding 2015): MEDIUM — CPE synthase activity of SMS1 (mouse in vivo/SF9).
- PMID:37715942 (Suzuki 2023): MEDIUM — PC-PLC activity of human SMS1 (abstract only).
- PMID:19946888 (Ghosh 2010): LOW — large-scale NK-cell membrane proteome; membrane localization only.
- Reactome R-HSA-429798 / R-HSA-1660661: MEDIUM — pathway representation of the SM synthase reaction.
</content>
</invoke>
