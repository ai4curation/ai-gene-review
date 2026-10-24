# amph-1 (amphiphysin/BIN1) curation notes

UniProt Q21004 (TrEMBL, Q21004_CAEEL), WormBase F13A2.? / amph-1; PANTHER
PTHR46514 AMPHIPHYSIN. The only C. elegans amphiphysin/BIN1 family member.
Listed in modules/synaptic_vesicle_endocytosis.yaml as the worm amphiphysin
N-BAR protein, but the worm functional literature is endosomal and nuclear,
not synaptic (see last section).

## Endocytic recycling with RME-1 (Pant et al. 2009, full text)

- [PMID:19915558 "Here we show that endogenous C. elegans AMPH-1, the only C. elegans member of the Amphiphysin/BIN1 family of BAR (Bin1-Amphiphysin-Rvs161p/167p)-domain-containing proteins, colocalizes with RME-1 on recycling endosomes in vivo, that amph-1-deletion mutants are defective in recycling endosome morphology and function, and that binding of AMPH-1 Asn-Pro-Phe(Asp/Glu) sequences to the RME-1 EH-domain promotes the recycling of transmembrane cargo."]
- Localization is specific to recycling endosomes
  [PMID:19915558 "Anti-AMPH-1 staining failed to colocalize with markers for the clathrin coated pits (GFP-tagged CHC-1/clathrin)18, early endosome (GFP-RAB-5)19, late endosome (GFP-RAB-7)19 or Golgi (Mannosidase-GFP)19, indicating that AMPH-1 is specifically enriched on recycling endosomes (Fig."].
- Phospholipid binding / tubulation in vitro
  [PMID:19915558 "In the absence of RME-1, AMPH-1 tubulated 400 nm average diameter PS liposomes into 50 nm wide tubules"]
  [PMID:19915558 "In vitro, we find that purified recombinant AMPH-1-RME-1 complexes produce short, coated membrane tubules that are qualitatively distinct from those produced by either protein alone."].
- Mutant phenotype and model
  [PMID:19915558 "These results indicate a defect in basolateral recycling in the intestinal epithelia of amph-1 mutants, very similar to that found in rme-1 mutants."]
  [PMID:19915558 "AMPH-1, through it’s BAR domain, could function to initiate tubule formation from endosomes, recruiting and activating RME-1 ATPase activity to drive tubule fission."]
  [PMID:19915558 "The loss of RME-1 from recycling endosomes confirmed the amph-1(RNAi) results from the initial screen, suggesting that AMPH-1 functions, at least in part, to recruit RME-1 to the recycling endosome membrane."].
- AMPH-1 co-localizes with SDPN-1 (syndapin) on recycling endosomes and
  sdpn-1 marker distribution is disrupted in amph-1 mutants
  [PMID:19915558 "We also found that loss of amph-1 disrupted another recycling endosome marker SDPN-1-GFP, with greatly reduced SDPN-1-GFP puncta number, and gross enlargement of remaining labeled structures (Fig."].

## RAB-10 / TBC-2 (Liu & Grant 2015, full text)

- [PMID:26393361 "We demonstrate that downstream basolateral recycling regulators, GTPase RAB-10/Rab10 and BAR domain protein AMPH-1/Amphiphysin, bind to TBC-2 and help to recruit it to endosomes."]
- [PMID:26393361 "GST-AMPH-1 can pull down TBC-2 and RAB-10 at the same time"]
- [PMID:26393361 "Colocalization analysis indicated the presence of AMPH-1-GFP and tagRFP-RAB-10 on a significant fraction of the same endosomes, consistent with physiological significance for the AMPH-1/RAB-10 interaction (S3A and S3B Fig)."]

## Nuclear positioning in muscle (D'Alessandro et al. 2015, abstract only)

- [PMID:26506308 "Here, we report that impairment of amphiphysin/BIN1 in Caenorhabditis elegans, mammalian cells, or muscles from patients with centronuclear myopathy alters nuclear position and shape."]
- [PMID:26506308 "We show that AMPH-1/BIN1 binds to nesprin and actin, as well as to the microtubule-binding protein CLIP170 in both species."]
- [PMID:26506308 "Expression of the microtubule-anchoring CAP-GLY domain of CLIP170 fused to the nuclear-envelope-anchoring KASH domain of nesprin rescues nuclear positioning defects of amph-1 mutants."]

## Synaptic localization (only worm synaptic evidence)

- AMPH-1::GFP imaged at release sites in the dorsal nerve cord; distribution
  unchanged in fat-3 mutants
  [PMID:18094048 "We could not detect differences between the distribution patterns of these proteins in fat-3(wa22) mutants and in WT animals ( Figure 4 F), suggesting that the localization and abundance of endophilin and amphiphysin at sites of release are not dependent on LC-PUFAs."].
- No amph-1 synaptic phenotype has been published; the module's placement of
  amph-1 in the synaptic membrane-curvature tier rests on orthology to
  mammalian amphiphysin, not on worm data. Flagged in suggested_questions.

## Review decisions

- 13 GOA rows: 8 ACCEPT, 1 KEEP_AS_NON_CORE (nucleus organization), 3
  MODIFY (protein binding -> small GTPase binding for RAB-10; ->
  protein-macromolecule adaptor activity for ANC-1/nesprin and CLIP-1),
  1 MARK_AS_OVER_ANNOTATED (plasma membrane IBA; worm AMPH-1 is on
  recycling endosomes).
- 2 NEW: GO:0032456 endocytic recycling (IMP, PMID:19915558; AMPH-1 does the
  tubulation and RME-1 recruitment; comparators RME-1 and SDPN-1 carry the
  term) and GO:0098793 presynapse (IDA, PMID:18094048 reporter localization).
