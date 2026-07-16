# GFPT2 (O94808) review notes

## Identity and family
- Human **GFPT2** = "Glutamine--fructose-6-phosphate aminotransferase [isomerizing] 2" (GFAT2), EC 2.6.1.16, 682 aa, HGNC:4242, chromosome 5q [file:human/GFPT2/GFPT2-uniprot.txt].
- Paralog of the ubiquitously expressed GFPT1 (Q06210). GFAT2 was cloned as a "novel subtype" of GFAT; human GFAT1 vs GFAT2 share ~75.6% amino-acid identity [PMID:10198162 "homologies between the human GFAT1 and GFAT2 ... were 75.6"]. The eLife paper gives the paralog identity as 75–80% [PMID:35229715 "The two mammalian GFPT paralogs GFPT1 and GFPT2 show 75%–80% amino acid sequence identity"].
- Domain architecture (UniProt): N-terminal glutamine amidotransferase type-2 domain (2–288) plus two SIS domains (360–499, 531–672); CDD hit `cd00714 GFAT`; PANTHER subfamily PTHR10937:SF10 "GLUTAMINE--FRUCTOSE-6-PHOSPHATE AMINOTRANSFERASE [ISOMERIZING] 2" [file:human/GFPT2/GFPT2-uniprot.txt].

## Molecular function (core)
- **Rate-limiting enzyme of the hexosamine biosynthetic pathway (HBP)**: catalyzes the first, committed step converting D-fructose 6-phosphate + L-glutamine -> D-glucosamine 6-phosphate + L-glutamate [file:human/GFPT2/GFPT2-uniprot.txt "Rate-limiting enzyme of the hexosamine biosynthetic pathway"; "catalyzes the formation of glucosamine-6-phosphate from"; CATALYTIC ACTIVITY Rhea:RHEA:13237, EC=2.6.1.16].
- GO term for this activity: **GO:0004360** "L-glutamine:D-fructose-6-phosphate transaminase (isomerizing) activity" (label confirmed current in local go.db; namespace = molecular_function).
- Direct experimental support for the catalytic activity comes from PMID:35229715, which purified recombinant human GFPT2 and measured kinetics [PMID:35229715 "we generated recombinant human GFPT1 and GFPT2 with an internal His6tag and characterized the proteins in activity assays"; "Kinetic measurements confirmed that both proteins were fully functional and revealed different substrate affinities of GFPT2 compared to GFPT1"]. This is the basis of the IDA GO:0004360 annotation (assigned by FlyBase) and the UniProt EC=2.6.1.16 {ECO:0000269|PubMed:35229715}.
- Kinetic parameters (UniProt BIOPHYSICOCHEMICAL PROPERTIES, from PMID:35229715): KM = 0.5 mM for L-glutamine, KM = 0.29 mM for D-fructose 6-phosphate; kcat 3.7 s-1 (Gln) / 1.8 s-1 (F6P) [file:human/GFPT2/GFPT2-uniprot.txt].

## Regulation (feedback inhibition) — a key GFPT2 vs GFPT1 distinction
- GFPT2 is feedback-inhibited by the pathway end product UDP-GlcNAc, but **less strongly than GFPT1** [file:human/GFPT2/GFPT2-uniprot.txt "Exhibits feedback inhibition by"; "UDP-N-acetylglucosamine (UDP-GlcNAc), although to a lesser extent than"].
- Quantitatively: UDP-GlcNAc IC50 for GFPT2 = 367.3 uM vs 57.0 uM for GFPT1 [PMID:35229715 "we found a significantly higher IC50 value for GFPT2 (367.3–43.6/+49.5 µM) compared to GFPT1 (57.0–8.3/+9.7 µM)"; "GFPT2 shows a lower sensitivity to UDP-GlcNAc feedback inhibition compared to GFPT1"]. In cells that use GFPT2 rather than GFPT1 for HBP entry, the deacetylase AMDHD2 is required to balance flux [PMID:35229715 "a configuration of the HBP that uses GFPT2 as the key enzyme"].

## Biological process (core)
- First step of UDP-N-acetyl-alpha-D-glucosamine biosynthesis via glucosamine 6-phosphate (UniProt PATHWAY: "Nucleotide-sugar biosynthesis; UDP-N-acetyl-alpha-D-glucosamine biosynthesis; alpha-D-glucosamine 6-phosphate from D-fructose 6-phosphate: step 1/1") [file:human/GFPT2/GFPT2-uniprot.txt].
- GO BP terms: **GO:0006048** "UDP-N-acetylglucosamine biosynthetic process" (the whole-pathway process this step initiates; IDA in GOA from PMID:35229715, plus IBA and Reactome TAS) and **GO:0006002** "fructose 6-phosphate metabolic process" (the substrate-consuming process; IDA from PMID:35229715). Both are supported and appropriate.
- Downstream, HBP output (UDP-GlcNAc) supplies precursors for N-/O-linked protein glycosylation [file:human/GFPT2/GFPT2-uniprot.txt "likely regulates the availability of precursors for N- and O-linked" / "protein glycosylation" (By similarity)]. The IBA GO:0006487 "protein N-linked glycosylation" annotation in UniProt DR is a downstream/context BP, not a direct GFPT2 function; it is not in this GOA seed.

## Localization
- **Cytosol** (GO:0005829), from Reactome TAS. HBP enzymes act in the cytosol; consistent with a soluble metabolic enzyme with no predicted TM/signal features. ACCEPT.

## Tissue expression
- GFPT2 has restricted expression relative to GFPT1: predominantly CNS (esp. spinal cord), heart, and placenta [file:human/GFPT2/GFPT2-uniprot.txt "Predominantly expressed throughout the central" / "nervous system, especially in the spinal cord"; "highly expressed in heart and placenta"; PMID:10198162 "GFAT2 was expressed throughout the central nervous system, especially in the spinal cord"]. UniProt HPA: "Tissue enhanced (adipose)". The GFPT2:GFPT1 ratio is high in embryonic stem cells and decreases upon differentiation [PMID:35229715].

## Interactions / "protein binding" (GO:0005515 IPI) — over-annotations of MF
Three IPI "protein binding" annotations are bare (uninformative MF). Per curation policy these are marked MARK_AS_OVER_ANNOTATED (not removed):
- PMID:21044950 — genome-wide YFP fluorescence-complementation screen for telomere-signaling regulators; WITH = UniProtKB:Q9NUX5 (POT1). Matches the UniProt INTERACTION line "O94808; Q9NUX5: POT1". High-throughput screen; no specific molecular function for GFPT2 established.
- PMID:33961781 — BioPlex dual proteome-scale interactome (AP-MS); WITH = UniProtKB:Q06210 (GFPT1). Matches UniProt INTERACTION line "O94808; Q06210: GFPT1". GFPT1/GFPT2 heteromer plausible (both form the GFAT enzyme, which is oligomeric) but the term captures only "protein binding".
- PMID:40205054 — multimodal cell maps (MuSIC/AP-MS + imaging); WITH = UniProtKB:Q06210 (GFPT1). High-throughput; bare "protein binding".

## IEA / electronic annotations assessment
- GO:0004360 IEA (GO_REF:0000120, ARBA/InterPro/RHEA/EC 2.6.1.16): correct MF, redundant with IDA/IBA/TAS — KEEP_AS_NON_CORE (accurate but superseded by experimental evidence).
- GO:0006048 IEA (GO_REF:0000120, ARBA/UniPathway UPA00113): correct BP, redundant — KEEP_AS_NON_CORE.
- GO:0006002 IEA (GO_REF:0000117, ARBA): correct BP, redundant — KEEP_AS_NON_CORE.
- GO:0097367 "carbohydrate derivative binding" IEA (GO_REF:0000002, InterPro SIS domains IPR001347/IPR046348): true (binds F6P/UDP-GlcNAc via SIS domains) but a very general MF that does not describe the catalytic function — MARK_AS_OVER_ANNOTATED.
- GO:1901135 "carbohydrate derivative metabolic process" IEA and GO:1901137 "carbohydrate derivative biosynthetic process" IEA (GO_REF:0000002, InterPro): correct but very general parents of the specific HBP terms — KEEP_AS_NON_CORE.
- **GO:0006112 "energy reserve metabolic process"** — appears twice (IEA GO_REF:0000117 ARBA:ARBA00026613, and TAS PMID:10198162 via PINC). This is misleading: GFAT2 feeds the HBP (an anabolic branch of glycolysis toward UDP-GlcNAc), not glycogen/energy-reserve (starch/glycogen) metabolism. The 1999 cloning paper (PMID:10198162, abstract-only) does not support an energy-reserve role; the abstract discusses the hexosamine pathway, glucose toxicity and diabetes complications. The IEA copy is a clearly-wrong electronic assignment -> REMOVE. The TAS copy rests on an experimental/curator (PINC) attribution to a primary paper whose full text I cannot read -> MARK_AS_OVER_ANNOTATED (do not REMOVE a TAS annotation on incomplete evidence).

## References verified
- file:human/GFPT2/GFPT2-uniprot.txt — authoritative UniProt record (read locally).
- PMID:35229715 (eLife 2022, Kroef et al.) — full text available; primary source for GFPT2 catalytic activity, kinetics, UDP-GlcNAc feedback, HBP flux role. HIGH relevance, VERIFIED.
- PMID:10198162 (Oki et al., Genomics 1999) — abstract-only (full_text_available: false); cloning, tissue distribution, hexosamine-pathway framing. HIGH relevance; supports MF/BP via TAS but abstract does not support energy-reserve BP.
- PMID:21044950, PMID:33961781, PMID:40205054 — high-throughput interaction/mapping studies underlying the IPI "protein binding" annotations; LOW relevance to core function.
- Reactome:R-HSA-449715 and Reactome:R-HSA-446210 — pathway TAS sources; titles left exactly as fetched.
