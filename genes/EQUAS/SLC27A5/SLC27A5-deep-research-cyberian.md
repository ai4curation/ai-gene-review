---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:55:12.139178'
end_time: '2026-10-26T01:04:36.178498'
duration_seconds: 564.04
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: SLC27A5
  gene_symbol: SLC27A5
  uniprot_accession: A0A9L0JNL2
  protein_description: 'RecName: Full=long-chain-fatty-acid--CoA ligase {ECO:0000256|ARBA:ARBA00026121};
    EC=6.2.1.3 {ECO:0000256|ARBA:ARBA00026121}; AltName: Full=Long-chain-fatty-acid--CoA
    ligase {ECO:0000256|ARBA:ARBA00041297};'
  gene_info: Name=SLC27A5 {ECO:0000313|Ensembl:ENSEASP00005053988.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the ATP-dependent AMP-binding enzyme family.
  protein_domains: AMP-b_sf. (IPR045851); AMP-bd_C. (IPR025110); AMP-binding_CS. (IPR020845);
    AMP-dep_synth/lig_dom. (IPR000873); ANL_N_sf. (IPR042099)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3302
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 69
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0JNL2
- **Protein Description:** RecName: Full=long-chain-fatty-acid--CoA ligase {ECO:0000256|ARBA:ARBA00026121}; EC=6.2.1.3 {ECO:0000256|ARBA:ARBA00026121}; AltName: Full=Long-chain-fatty-acid--CoA ligase {ECO:0000256|ARBA:ARBA00041297};
- **Gene Information:** Name=SLC27A5 {ECO:0000313|Ensembl:ENSEASP00005053988.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the ATP-dependent AMP-binding enzyme family.
- **Key Domains:** AMP-b_sf. (IPR045851); AMP-bd_C. (IPR025110); AMP-binding_CS. (IPR020845); AMP-dep_synth/lig_dom. (IPR000873); ANL_N_sf. (IPR042099)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SLC27A5" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SLC27A5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SLC27A5** (gene ID: SLC27A5, UniProt: A0A9L0JNL2) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SLC27A5 (FATP5 / bile acyl-CoA synthetase) in the donkey, *Equus asinus* (UniProt A0A9L0JNL2)

## 1. Introduction and summary

UniProt A0A9L0JNL2 is an unreviewed, computationally annotated 700-residue protein from the donkey reference genome. Ensembl names its gene SLC27A5, and it lies on chromosome 26 (Ensembl ENSEASG00005023631; NCBI GeneID 106846663) [uniprot-A0A9L0JNL2-entry]. The donkey genome assembly behind the prediction came from the donkey population-genomics project [wang-2020-donkey-genomes-abstract]. The entry's descriptive name, "long-chain-fatty-acid--CoA ligase (EC 6.2.1.3)", is a generic automatic (ARBA) label. Its GO annotations are all inferred electronically. No experimental study of the donkey protein exists, so everything said here about its function comes from orthology with the well-studied human and mouse SLC27A5 proteins.

**Identity check.** The gene symbol, protein family and domains are consistent with each other, and none of the literature reviewed below concerns a different gene with the same symbol. The donkey protein belongs to the ATP-dependent AMP-binding enzyme (ANL) superfamily. It has a Pfam AMP-binding domain (residues 130–453) and an AMP-binding C-terminal domain (576–652), and it falls in PANTHER subfamily PTHR43107:SF25, "long-chain fatty acid transport protein 5" [uniprot-A0A9L0JNL2-entry]. In my own pairwise alignment, the donkey sequence is 81.3% identical to human SLC27A5/FATP5 (Q9Y2P5) and 71.0% identical to mouse Slc27a5 (Q4LDG0). It also keeps the AMP-binding signature motif IYTSGTTGLPK (SEQUENCE_NOTES.md). So the protein is the donkey orthologue of mammalian FATP5, also called bile acyl-CoA synthetase (BACS), bile acid-CoA ligase (BACL/BAL) and very-long-chain acyl-CoA synthetase homolog 2 (VLCS-H2/ACSVL6) [uniprot-Q9Y2P5-human-SLC27A5-entry].

**Summary of function.** Mammalian SLC27A5 is a liver-specific membrane enzyme. It joins coenzyme A to a carboxylic acid using ATP, releasing AMP and pyrophosphate. Its physiologically dominant substrates are C24 bile acids. The primary bile acids cholate and chenodeoxycholate are activated, and so are the secondary bile acids deoxycholate and lithocholate [steinberg-2000-cholate-coa-ligase-abstract; mihalik-2002-bacs-bile-acid-synthesis-abstract]. Forming the bile acid-CoA thioester is the obligatory first step of bile acid amidation; BAAT then transfers the bile acid to glycine or taurine [setchell-2013-conjugation-defects-fulltext]. In vivo, SLC27A5 is needed mainly to *reconjugate* bile acids that return to the liver through the enterohepatic circulation, not for de novo bile acid synthesis [hubbard-2006-fatp5-ko-bile-conjugation-abstract]. The protein also activates long- and very-long-chain fatty acids [steinberg-1999-vlcsh2-cloning-abstract]. It promotes long-chain fatty acid uptake into hepatocytes at the sinusoidal (basal) plasma membrane [doege-2006-fatp5-ko-hepatic-lipid-abstract]. Most recently it has been shown to supply acyl-CoA for hepatic N-acyl taurine synthesis [kuentzel-2026-fatp5-n-acyl-taurines-abstract]. The donkey orthologue is expected to do the same jobs in equine hepatocytes.

## 2. Molecular identity, family and domain architecture

SLC27A5 is one of six mammalian fatty acid transport proteins (FATP1–6, SLC27A1–6). These are integral membrane proteins that increase cellular uptake of long-chain and very-long-chain fatty acids [stahl-2004-slc27-review-abstract]. The family was defined when four new murine FATPs were cloned. One of them was expressed only in liver, and it increased fatty acid uptake when expressed in mammalian cells; this liver-specific member is the gene now called FATP5. The family is conserved from mycobacteria to humans [hirsch-1998-fatp-family-abstract]. A genome-wide survey of human acyl-CoA synthetases found 26 genes and grouped them into subfamilies by sequence similarity, which also matched their acyl chain-length preference. SLC27A5 falls in the very-long-chain (ACSVL) subfamily [watkins-2007-26-acs-genes-abstract; watkins-2008-vlcs-review-abstract]. FATPs are 20–40% identical to long-chain acyl-CoA synthetase ACSL1, and several have measurable acyl-CoA synthetase activity [kazantzis-2012-fatp-review-fulltext].

The donkey protein has the domain layout typical of the family. An N-terminal hydrophobic region is predicted as a signal peptide (1–31) and two transmembrane helices (41–66, 73–90). The large ANL-type adenylate-forming domain contains the AMP-binding consensus, and the C-terminal AMP-binding domain follows [uniprot-A0A9L0JNL2-entry]. In ANL enzymes these two domains together catalyse a two-step reaction. The acid is first adenylated with ATP to an acyl-AMP intermediate, and CoA then attacks that intermediate to form the thioester. The SignalP "signal peptide" call should be read with caution. Mammalian FATP5 is not known to be secreted or cleaved; the N-terminal hydrophobic segment more likely anchors the protein in the membrane. The donkey gene model also has a 10-residue N-terminal extension in front of the Met that lines up with human Met1, which suggests the predicted start codon may be wrong (SEQUENCE_NOTES.md). His338 in the human protein is mutated in the first known human bile acid-CoA ligase deficiency [chong-2012-bacs-deficiency-abstract], and it is conserved in the donkey protein (His348) (SEQUENCE_NOTES.md).

### Structural inference from the paralogue FATP2

No experimental structure of any FATP5 exists. In 2026, however, cryo-EM structures were published for its closest structurally characterized paralogue, human FATP2, and they give a direct template. Li and colleagues solved FATP2a in nanodiscs in two states: an intermediate state with bound oleoyl-AMP (2.93 Å) and a pre-catalytic state, captured with the catalytic-lysine mutant K572A, with bound ATP (2.76 Å). The protein has four parts. A membrane association domain, made of an N-terminal transmembrane helix and a reclining helix lying on the membrane, anchors it. A cytosolic N-terminal domain, a core catalytic domain and a C-terminal domain sit below. Fatty acids reach the catalytic centre from the membrane through a hydrophobic tunnel in a two-step translocation, and FATP2 fatty acid transport strictly depended on its acyl-CoA synthetase activity [li-2026-fatp2-structure-abstract; li-2026-fatp2-structure-fulltext]. The authors report that the catalytic-centre residues binding Mg2+, ATP and the AMP moiety are conserved in all six human FATPs. Residues lining the acyl-binding tunnel differ more, which may explain differences in substrate preference [li-2026-fatp2-structure-fulltext]. An independent preprint describes FATP2 as a membrane-anchored "lollipop" that recruits fatty acids directly from the membrane interface. In that work the C-terminal domain rotates about 130° during catalysis and acyl-CoA product inhibits the enzyme [zhang-2026-fatp2-mechanism-abstract].

The donkey sequence supports transferring this model. Donkey SLC27A5 is 46.9% identical to human FATP2 in my alignment, and FATP2 catalytic Lys572 aligns with donkey Lys652 (SEQUENCE_NOTES.md). The N-terminal hydrophobic segment that SignalP and Phobius flag in the donkey entry [uniprot-A0A9L0JNL2-entry] corresponds to the FATP membrane association domain. It is therefore best read as a membrane anchor, with the catalytic domains facing the cytosol, rather than as a cleavable signal peptide. These structures also make it more likely that FATP5's effect on hepatic fatty acid uptake comes from its synthetase activity (vectorial acylation), not from a separate transporter function. That is an inference from a paralogue and has not been tested on FATP5. The wider tunnel needed to fit a steroid nucleus, which FATP5 must have if it accepts C24 bile acids, is not explained by the FATP2 structures. No such data exist for FATP5.

## 3. Catalytic activity and substrate specificity

The enzymology of SLC27A5 was worked out mainly on the human protein, then known as hVLCS-H2. Human SLC27A5 encodes a 690-residue protein that is 44–45% identical to peroxisomal VLCS (SLC27A2). When stably expressed in COS-1 cells it increased acyl-CoA synthetase activity towards stearate (C18:0), arachidate (C20:0), lignocerate (C24:0) and hexacosanoate (C26:0) [steinberg-1999-vlcsh2-cloning-abstract]. Two features, its liver-specific expression and its ER localization, led to the idea that it might be the long-sought bile acid:CoA ligase. COS-1 cells expressing hVLCS-H2 did show cholate:CoA ligase (choloyl-CoA synthetase) activity, whereas other long- and very-long-chain acyl-CoA synthetases could not activate cholate. Endogenous choloyl-CoA synthetase activity was found in liver-derived HepG2 cells but not in COS-1 cells [steinberg-2000-cholate-coa-ligase-abstract]. The substrate range was later widened to chenodeoxycholate, deoxycholate, lithocholate, and the C27 cholic acid precursor 3α,7α,12α-trihydroxy-5β-cholestanoic acid (THCA). In contrast, VLCS (SLC27A2) activated THCA but none of the C24 bile acids [mihalik-2002-bacs-bile-acid-synthesis-abstract]. The curated human entry lists a Km of 2.8 µM for cholate and notes that THCA inhibits cholate activation [uniprot-Q9Y2P5-human-SLC27A5-entry]. The core reaction is therefore

bile acid (e.g., cholate) + ATP + CoA → bile acyl-CoA (choloyl-CoA) + AMP + PPi (EC 6.2.1.7),

with a parallel, less prominent reaction on long/very-long-chain fatty acids (EC 6.2.1.3) [uniprot-Q9Y2P5-human-SLC27A5-entry]. The donkey entry carries only the generic EC 6.2.1.3 label [uniprot-A0A9L0JNL2-entry]. That label understates the bile acid-CoA ligase activity that best characterizes the orthologue.

New evidence extends the substrates to fatty acids activated for taurine conjugation. In mice, siRNA knockdown of Fatp5 reduced biliary N-acyl taurines (NATs) as much as loss of BAAT did. Knockdown did not change NAT synthase activity when acyl-CoA was supplied in the assay. Together these results put FATP5 upstream of BAAT, as the source of the acyl-CoA (for example polyunsaturated C22:6-CoA) [kuentzel-2026-fatp5-n-acyl-taurines-abstract; kuentzel-2026-fatp5-n-acyl-taurines-fulltext].

## 4. Role in bile acid conjugation and the enterohepatic circulation

Bile acid amidation with glycine or taurine is the last step of bile acid synthesis. It lowers the pKa and keeps bile acids in solution in the proximal intestine, which allows efficient micellar uptake of lipids and fat-soluble vitamins. Two enzymes are involved: a bile acid-CoA ligase (SLC27A5) first makes the CoA thioester, and BAAT then transfers the bile acid to the amino acid [setchell-2013-conjugation-defects-fulltext]. Mihalik and colleagues proposed a division of labour based on substrate preferences. SLC27A5 would mainly reactivate and recycle C24 bile acids, while VLCS (SLC27A2) would serve the de novo pathway by activating THCA before its peroxisomal side-chain cleavage [mihalik-2002-bacs-bile-acid-synthesis-abstract].

Knockout mice confirmed this model. In Fatp5-null mice, total bile acid levels in bile, liver, urine and faeces were unchanged, but most gallbladder bile acids were unconjugated. The small remaining conjugated fraction held only primary bile acids. This means FATP5 is specifically needed to reconjugate bile acids that intestinal bacteria have deconjugated (and, for secondary bile acids, dehydroxylated) during enterohepatic recirculation [hubbard-2006-fatp5-ko-bile-conjugation-abstract]. The bile acid pool showed no biosynthetic block, so FATP5 is either redundant with or not required for the de novo THCA activation step [kazantzis-2012-fatp-review-fulltext]. Liver-targeted knockdown gave the same picture. About 90% Slc27a5 silencing reduced reconjugation of a D4-cholate tracer to D4-taurocholate [castroperez-2011-slc27a5-reconjugation-abstract], and siRNA against Fatp5 raised the unconjugated fraction of bile acids about 100-fold [ason-2011-apob-sirna-fatp5-abstract].

Human genetics shows the same function in people. A child of consanguineous parents was homozygous for SLC27A5 c.1012C>T (p.H338Y) and had >85% unconjugated bile acids in plasma and urine. Her sibling had the same genotype and the same biochemical phenotype but no liver disease. The authors suggested that the more severe cholestatic disease in the proband reflected added factors: prematurity, parenteral nutrition, and a homozygous ABCB11 variant [chong-2012-bacs-deficiency-abstract]. Conjugation defects of this kind cause fat-soluble vitamin malabsorption and growth failure. Bile acid-CoA ligase deficiency is now listed with BAAT deficiency among the amidation defects in reviews of inborn errors of bile acid synthesis. Both present with cholestasis, normal γ-glutamyl transpeptidase and malabsorption of fat-soluble vitamins [clayton-2011-bile-acid-synthesis-disorders-abstract]. Telling a ligase (SLC27A5) defect apart from a transferase (BAAT) defect requires gene sequencing or liver immunostaining, because the two give nearly identical urinary mass spectra [setchell-2013-conjugation-defects-fulltext].

## 5. Hepatic long-chain fatty acid uptake

FATP5 was first named for its ability to increase cellular long-chain fatty acid uptake [hirsch-1998-fatp-family-abstract]. Whether that is a separate transport function or a consequence of acyl-CoA synthetase activity remains debated. In mouse liver, FATP5 is expressed only in hepatocytes and sits at the basal plasma membrane, which faces the sinusoids. Overexpression increased [14C]oleate uptake. Hepatocytes from Fatp5-knockout mice took up less long-chain fatty acid, and the knockout livers contained less triglyceride and free fatty acid, despite higher expression of fatty acid synthase [doege-2006-fatp5-ko-hepatic-lipid-abstract]. Reviews place FATP5 on hepatocyte microvilli in the space of Disse. Knockout hepatocytes show a 40–50% reduction in uptake, and oral [14C]oleate is redirected from liver towards muscle and heart [kazantzis-2012-fatp-review-fulltext]. AAV-shRNA knockdown of hepatic FATP5 in adult mice lowered dietary fatty acid uptake into the liver. It both prevented and reversed diet-induced fatty liver, and it improved glucose homeostasis [doege-2008-fatp5-silencing-abstract]. A cell-based screen for human FATP5 uptake inhibitors found the bile acids chenodiol and ursodiol as hits [zhou-2010-fatp4-fatp5-hts-abstract]. This finding links the protein's two kinds of ligand.

How FATPs increase uptake is unresolved. One model holds that they act as true transporters. In the "vectorial acylation" model, they promote uptake by rapidly converting incoming fatty acids to acyl-CoA, which traps them inside the cell [kazantzis-2012-fatp-review-fulltext]. Reviewers have described FATP5 as bifunctional, required both for hepatic fatty acid uptake and for bile acid reconjugation [gimeno-2007-fatp-review-abstract]. The uptake phenotype also depends on context. In one setting, Fatp5 knockdown did not prevent the steatosis caused by ApoB knockdown, a situation in which triglyceride accumulates because export is blocked rather than because influx increases [ason-2011-apob-sirna-fatp5-abstract].

## 6. Subcellular and tissue localization

Across species, SLC27A5 is expressed only, or almost only, in the liver [steinberg-1999-vlcsh2-cloning-abstract; doege-2006-fatp5-ko-hepatic-lipid-abstract; kazantzis-2012-fatp-review-fulltext]. Two membrane locations have been reported within hepatocytes. With epitope-tagged human protein in COS-1 and HepG2 cells, indirect immunofluorescence showed endoplasmic reticulum membrane staining and no peroxisomal staining [steinberg-1999-vlcsh2-cloning-abstract]. Topographic studies were consistent with the proposed role in bile acid recycling [mihalik-2002-bacs-bile-acid-synthesis-abstract]. In intact mouse liver, by contrast, FATP5 was found at the basal (sinusoidal) plasma membrane [doege-2006-fatp5-ko-hepatic-lipid-abstract]. A 2026 fractionation study detected FATP5 in plasma membrane-enriched fractions and also in peroxisome-enriched fractions, which fits peroxisomal BAAT-dependent conjugation [kuentzel-2026-fatp5-n-acyl-taurines-fulltext]. The donkey entry's electronic GO terms reflect these findings: "basal plasma membrane" and "endoplasmic reticulum membrane" (Ensembl IEA), plus a keyword-level "cell membrane" [uniprot-A0A9L0JNL2-entry]. A plausible synthesis is that the protein is made and partly resides in the ER, while a sinusoidal plasma-membrane pool takes up fatty acids and bile acids returning from portal blood. The partitioning in equine liver has not been studied.

## 7. Regulation and broader physiological context

The liver-enriched nuclear receptor HNF4α directly controls Slc27a5 transcription. Mice without hepatic HNF4α had much lower levels of the mouse bile acid-CoA ligase transcript (VLACSR) and of Bat, and their bile contained more unconjugated bile acids. HNF4α bound the VLACSR promoter directly [inoue-2004-hnf4a-conjugation-abstract]. Glucocorticoid metabolism also affects the gene. Mice lacking 11β-HSD1 had less hepatic Fatp5 and more circulating unconjugated bile acids, by a mechanism that appeared independent of the glucocorticoid receptor [penno-2014-11bhsd1-fatp5-abstract].

Several phenotypes follow from the catalytic roles but are secondary to them. Fatp5-null mice resisted weight gain on a high-fat diet, through lower food intake and higher energy expenditure [hubbard-2006-fatp5-ko-bile-conjugation-abstract]. In humans, a promoter variant (rs56225452) has been associated with higher ALT, insulin resistance and dyslipidaemia [auinger-2010-fatp5-promoter-polymorphism-abstract]. In hepatocellular carcinoma, SLC27A5 is silenced by promoter hypermethylation. Its loss changes the cell's lipid composition towards polyunsaturated species, raises lipid peroxidation and 4-HNE adduction of KEAP1, and activates NRF2 [gao-2020-slc27a5-hcc-nrf2-abstract]. FATP5 deficiency has also been linked to AMPK–mTOR-dependent metabolic reprogramming and metastasis [wang-2021-fatp5-hcc-abstract]. These studies come from rodents and human tissue. For the donkey they mainly show how central the enzyme is to hepatic lipid handling, rather than describing separate primary functions.

## 8. Implications for the donkey orthologue

The donkey protein is highly conserved, keeps the catalytic motifs and the disease-relevant histidine, and is classified in the FATP5 subfamily. Its main molecular function is therefore best stated as bile acid-CoA ligase (cholate–CoA ligase, EC 6.2.1.7) acting on C24 primary and secondary bile acids, with secondary long-/very-long-chain fatty acid–CoA ligase activity (EC 6.2.1.3). Its biological roles would be reconjugation of bile acids during enterohepatic circulation and protein-facilitated hepatic uptake of long-chain fatty acids. It would be located in the hepatocyte ER membrane and the basal (sinusoidal) plasma membrane [steinberg-2000-cholate-coa-ligase-abstract; mihalik-2002-bacs-bile-acid-synthesis-abstract; hubbard-2006-fatp5-ko-bile-conjugation-abstract; doege-2006-fatp5-ko-hepatic-lipid-abstract]. A comparative caveat follows from bile salt evolution. Across reptiles and mammals, bile salt profiles track phylogeny rather than diet. Most mammals use C24 5β-bile acids, the substrate class of SLC27A5. The same survey, however, lists rhinoceroses, which belong to the order Perissodactyla along with equids, among taxa whose biliary bile salts are entirely bile alcohols [hagey-2010-bile-salt-diversity-abstract; hagey-2010-bile-salt-diversity-fulltext]. Bile alcohols are sulfated rather than amidated. If any perissodactyl relies mainly on bile alcohols, then the C24-bile-acid reconjugation role of SLC27A5 would carry less physiological weight in that lineage than in rodents or humans. I did not find equid bile salt profiles in the main text of that survey, so whether donkeys mainly make amidated C24 bile acids still needs to be checked directly. One equine-specific point is relevant. Horses and donkeys have no gallbladder, so bile flows continuously into the duodenum. The enterohepatic return of deconjugated bile acids, and with it hepatic reconjugation, may therefore differ in rate from that of gallbladder-bearing species. This is an inference, not a measured result; I found no literature on equid bile acid conjugation enzymes.

## Open Questions

Every functional statement about A0A9L0JNL2 rests on orthology. No biochemical, localization or expression data exist for the equine protein. Useful follow-up work would include: (i) recombinant expression of donkey SLC27A5 to measure choloyl-CoA synthetase kinetics and chain-length preference, including whether glycine or taurine conjugation dominates in equids and whether THCA is a meaningful substrate; (ii) characterizing the equine (or human) FATP5 structure, to see how its acyl tunnel fits the steroid nucleus of C24 bile acids compared with the fatty-acid-only tunnel of FATP2 [li-2026-fatp2-structure-fulltext], and whether Lys652 is required for the bile acid ligase activity; (iii) determining the biliary bile salt profile of donkeys and horses, given that rhinoceroses are reported to secrete only bile alcohols [hagey-2010-bile-salt-diversity-fulltext]; (iv) checking the gene model, especially the 10-residue N-terminal extension and the signal-peptide prediction, against donkey liver RNA-seq; (v) confirming liver-restricted expression and sinusoidal versus ER localization in equine hepatocytes; (vi) comparing the bile acid pool and conjugation pattern of gallbladder-less equids with rodent knockout phenotypes; and (vii) settling the general mechanistic question of whether FATP5 "transport" activity can be separated from its acyl-CoA synthetase activity (vectorial acylation versus true translocation). The 2026 finding that FATP5 provides acyl-CoA for N-acyl taurine synthesis [kuentzel-2026-fatp5-n-acyl-taurines-abstract] also raises the question of which acyl substrates (bile acids or PUFA) predominate in vivo, and whether that balance differs among species.

## References

- [uniprot-A0A9L0JNL2-entry] UniProtKB/TrEMBL A0A9L0JNL2_EQUAS, entry version 15 (02-Sep-2026). https://rest.uniprot.org/uniprotkb/A0A9L0JNL2.txt
- [uniprot-Q9Y2P5-human-SLC27A5-entry] UniProtKB/Swiss-Prot Q9Y2P5 (S27A5_HUMAN). https://rest.uniprot.org/uniprotkb/Q9Y2P5.txt
- [wang-2020-donkey-genomes] Wang C, et al. Donkey genomes provide new insights into domestication and selection for coat color. Nat Commun. 2020;11:6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7
- [hirsch-1998-fatp-family] Hirsch D, Stahl A, Lodish HF. A family of fatty acid transporters conserved from mycobacterium to man. Proc Natl Acad Sci U S A. 1998;95:8625-8629. PMID: 9671728; PMCID: PMC21126; DOI: 10.1073/pnas.95.15.8625
- [steinberg-1999-vlcsh2-cloning] Steinberg SJ, Wang SJ, McGuinness MC, Watkins PA. Human liver-specific very-long-chain acyl-coenzyme A synthetase: cDNA cloning and characterization of a second enzymatically active protein. Mol Genet Metab. 1999;68:32-42. PMID: 10479480; DOI: 10.1006/mgme.1999.2883
- [steinberg-2000-cholate-coa-ligase] Steinberg SJ, Mihalik SJ, Kim DG, Cuebas DA, Watkins PA. The human liver-specific homolog of very long-chain acyl-CoA synthetase is cholate:CoA ligase. J Biol Chem. 2000;275:15605-15608. PMID: 10749848; DOI: 10.1074/jbc.c000015200
- [mihalik-2002-bacs-bile-acid-synthesis] Mihalik SJ, et al. Participation of two members of the very long-chain acyl-CoA synthetase family in bile acid synthesis and recycling. J Biol Chem. 2002;277:24771-24779. PMID: 11980911; DOI: 10.1074/jbc.m203295200
- [stahl-2004-slc27-review] Stahl A. A current review of fatty acid transport proteins (SLC27). Pflugers Arch. 2004;447:722-727. PMID: 12856180; DOI: 10.1007/s00424-003-1106-z
- [inoue-2004-hnf4a-conjugation] Inoue Y, Yu AM, Inoue J, Gonzalez FJ. Hepatocyte nuclear factor 4alpha is a central regulator of bile acid conjugation. J Biol Chem. 2004;279:2480-2489. PMID: 14583614; DOI: 10.1074/jbc.m311015200
- [doege-2006-fatp5-ko-hepatic-lipid] Doege H, et al. Targeted deletion of FATP5 reveals multiple functions in liver metabolism: alterations in hepatic lipid homeostasis. Gastroenterology. 2006;130:1245-1258. PMID: 16618416; DOI: 10.1053/j.gastro.2006.02.006
- [hubbard-2006-fatp5-ko-bile-conjugation] Hubbard B, et al. Mice deleted for fatty acid transport protein 5 have defective bile acid conjugation and are protected from obesity. Gastroenterology. 2006;130:1259-1269. PMID: 16618417; DOI: 10.1053/j.gastro.2006.02.012
- [gimeno-2007-fatp-review] Gimeno RE. Fatty acid transport proteins. Curr Opin Lipidol. 2007;18:271-276. PMID: 17495600; DOI: 10.1097/mol.0b013e3281338558
- [watkins-2007-26-acs-genes] Watkins PA, Maiguel D, Jia Z, Pevsner J. Evidence for 26 distinct acyl-coenzyme A synthetase genes in the human genome. J Lipid Res. 2007;48:2736-2750. PMID: 17762044; DOI: 10.1194/jlr.m700378-jlr200
- [watkins-2008-vlcs-review] Watkins PA. Very-long-chain acyl-CoA synthetases. J Biol Chem. 2008;283:1773-1777. PMID: 18024425; DOI: 10.1074/jbc.r700037200
- [doege-2008-fatp5-silencing] Doege H, et al. Silencing of hepatic fatty acid transporter protein 5 in vivo reverses diet-induced non-alcoholic fatty liver disease and improves hyperglycemia. J Biol Chem. 2008;283:22186-22192. PMID: 18524776; PMCID: PMC2494916; DOI: 10.1074/jbc.m803510200
- [falcon-2010-fatp2-hepatic] Falcon A, et al. FATP2 is a hepatic fatty acid transporter and peroxisomal very long-chain acyl-CoA synthetase. Am J Physiol Endocrinol Metab. 2010;299:E384-93. PMID: 20530735; PMCID: PMC2944282; DOI: 10.1152/ajpendo.00226.2010 (downloaded for paralog context; not cited in the text)
- [zhou-2010-fatp4-fatp5-hts] Zhou W, Madrid P, Fluitt A, Stahl A, Xie XS. Development and validation of a high-throughput screening assay for human long-chain fatty acid transport proteins 4 and 5. J Biomol Screen. 2010;15:488-497. PMID: 20448275; PMCID: PMC2887688; DOI: 10.1177/1087057110369700
- [auinger-2010-fatp5-promoter-polymorphism] Auinger A, et al. A promoter polymorphism in the liver-specific fatty acid transport protein 5 is associated with features of the metabolic syndrome and steatosis. Horm Metab Res. 2010;42:854-859. PMID: 20945272; DOI: 10.1055/s-0030-1267186
- [castroperez-2011-slc27a5-reconjugation] Castro-Perez JM, et al. Attenuation of Slc27a5 gene expression followed by LC-MS measurement of bile acid reconjugation using metabolomics and a stable isotope tracer strategy. J Proteome Res. 2011;10:4683-4691. PMID: 21819150; DOI: 10.1021/pr200475g
- [ason-2011-apob-sirna-fatp5] Ason B, et al. ApoB siRNA-induced liver steatosis is resistant to clearance by the loss of fatty acid transport protein 5 (Fatp5). Lipids. 2011;46:991-1003. PMID: 21826528; PMCID: PMC3213337; DOI: 10.1007/s11745-011-3596-3
- [kazantzis-2012-fatp-review] Kazantzis M, Stahl A. Fatty acid transport proteins, implications in physiology and disease. Biochim Biophys Acta. 2012;1821:852-857. PMID: 21979150; PMCID: PMC3274620; DOI: 10.1016/j.bbalip.2011.09.010
- [chong-2012-bacs-deficiency] Chong CP, et al. Bile acid-CoA ligase deficiency--a new inborn error of bile acid metabolism. J Inherit Metab Dis. 2012;35:521-530. PMID: 22089923; DOI: 10.1007/s10545-011-9416-3
- [setchell-2013-conjugation-defects] Setchell KD, et al. Genetic defects in bile acid conjugation cause fat-soluble vitamin deficiency. Gastroenterology. 2013;144:945-955.e6. PMID: 23415802; PMCID: PMC4175397; DOI: 10.1053/j.gastro.2013.02.004
- [penno-2014-11bhsd1-fatp5] Penno CA, et al. 11β-Hydroxysteroid dehydrogenase-1 is involved in bile acid homeostasis by modulating fatty acid transport protein-5 in the liver of mice. Mol Metab. 2014;3:554-564. PMID: 25061560; PMCID: PMC4099504; DOI: 10.1016/j.molmet.2014.04.008
- [gao-2020-slc27a5-hcc-nrf2] Gao Q, et al. SLC27A5 deficiency activates NRF2/TXNRD1 pathway by increased lipid peroxidation in HCC. Cell Death Differ. 2020;27:1086-1104. PMID: 31367013; PMCID: PMC7206086; DOI: 10.1038/s41418-019-0399-1
- [wang-2021-fatp5-hcc] Wang MD, et al. Fatty acid transport protein-5 (FATP5) deficiency enhances hepatocellular carcinoma progression and metastasis by reprogramming cellular energy metabolism and regulating the AMPK-mTOR signaling pathway. Oncogenesis. 2021;10:74. PMID: 34772914; PMCID: PMC8589992; DOI: 10.1038/s41389-021-00364-5
- [kuentzel-2026-fatp5-n-acyl-taurines] Kuentzel KB, et al. The bile acid-CoA ligase, FATP5, is necessary for the synthesis of N-acyl taurines in the liver. J Lipid Res. 2026;67:101012. PMID: 41780593; PMCID: PMC13050040; DOI: 10.1016/j.jlr.2026.101012
- [clayton-2011-bile-acid-synthesis-disorders] Clayton PT. Disorders of bile acid synthesis. J Inherit Metab Dis. 2011;34:593-604. PMID: 21229319; DOI: 10.1007/s10545-010-9259-3
- [hagey-2010-bile-salt-diversity] Hagey LR, Vidal N, Hofmann AF, Krasowski MD. Evolutionary diversity of bile salts in reptiles and mammals, including analysis of ancient human and extinct giant ground sloth coprolites. BMC Evol Biol. 2010;10:133. PMID: 20444292; PMCID: PMC2886068; DOI: 10.1186/1471-2148-10-133
- [li-2026-fatp2-structure] Li A, Shi J, Xu X, Yang Y, Feng S, Ma D. Structural basis of fatty acid activation and transport by human FATP2. Nat Commun. 2026;17:9718. PMID: 42722660; PMCID: PMC13562550; DOI: 10.1038/s41467-026-76658-2
- [zhang-2026-fatp2-mechanism] Zhang Z, et al. Mechanism of fatty acid uptake and inhibition in human FATP2. bioRxiv 2026 (preprint). PMID: 42465254; DOI: 10.64898/2026.07.06.736331


## Citations

1. ason-2011-apob-sirna-fatp5-abstract.md
2. ason-2011-apob-sirna-fatp5-fulltext.txt
3. ason-2011-apob-sirna-fatp5-summary.md
4. auinger-2010-fatp5-promoter-polymorphism-abstract.md
5. auinger-2010-fatp5-promoter-polymorphism-summary.md
6. castroperez-2011-slc27a5-reconjugation-abstract.md
7. castroperez-2011-slc27a5-reconjugation-summary.md
8. chong-2012-bacs-deficiency-abstract.md
9. chong-2012-bacs-deficiency-summary.md
10. clayton-2011-bile-acid-synthesis-disorders-abstract.md
11. clayton-2011-bile-acid-synthesis-disorders-summary.md
12. doege-2006-fatp5-ko-hepatic-lipid-abstract.md
13. doege-2006-fatp5-ko-hepatic-lipid-summary.md
14. doege-2008-fatp5-silencing-abstract.md
15. doege-2008-fatp5-silencing-summary.md
16. falcon-2010-fatp2-hepatic-abstract.md
17. falcon-2010-fatp2-hepatic-summary.md
18. gao-2020-slc27a5-hcc-nrf2-abstract.md
19. gao-2020-slc27a5-hcc-nrf2-summary.md
20. gimeno-2007-fatp-review-abstract.md
21. gimeno-2007-fatp-review-summary.md
22. hagey-2010-bile-salt-diversity-abstract.md
23. hagey-2010-bile-salt-diversity-fulltext.txt
24. hagey-2010-bile-salt-diversity-summary.md
25. hirsch-1998-fatp-family-abstract.md
26. hirsch-1998-fatp-family-summary.md
27. hubbard-2006-fatp5-ko-bile-conjugation-abstract.md
28. hubbard-2006-fatp5-ko-bile-conjugation-summary.md
29. inoue-2004-hnf4a-conjugation-abstract.md
30. inoue-2004-hnf4a-conjugation-summary.md
31. kazantzis-2012-fatp-review-abstract.md
32. kazantzis-2012-fatp-review-fulltext.txt
33. kazantzis-2012-fatp-review-summary.md
34. kuentzel-2026-fatp5-n-acyl-taurines-abstract.md
35. kuentzel-2026-fatp5-n-acyl-taurines-fulltext.txt
36. kuentzel-2026-fatp5-n-acyl-taurines-summary.md
37. li-2026-fatp2-structure-abstract.md
38. li-2026-fatp2-structure-fulltext.txt
39. li-2026-fatp2-structure-summary.md
40. mihalik-2002-bacs-bile-acid-synthesis-abstract.md
41. mihalik-2002-bacs-bile-acid-synthesis-summary.md
42. penno-2014-11bhsd1-fatp5-abstract.md
43. penno-2014-11bhsd1-fatp5-fulltext.txt
44. penno-2014-11bhsd1-fatp5-summary.md
45. setchell-2013-conjugation-defects-abstract.md
46. setchell-2013-conjugation-defects-fulltext.txt
47. setchell-2013-conjugation-defects-summary.md
48. stahl-2004-slc27-review-abstract.md
49. stahl-2004-slc27-review-summary.md
50. steinberg-1999-vlcsh2-cloning-abstract.md
51. steinberg-1999-vlcsh2-cloning-summary.md
52. steinberg-2000-cholate-coa-ligase-abstract.md
53. steinberg-2000-cholate-coa-ligase-summary.md
54. uniprot-A0A9L0JNL2-entry.txt
55. uniprot-A0A9L0JNL2-summary.md
56. uniprot-Q9Y2P5-human-SLC27A5-entry.txt
57. uniprot-Q9Y2P5-human-SLC27A5-summary.md
58. wang-2020-donkey-genomes-abstract.md
59. wang-2020-donkey-genomes-summary.md
60. wang-2021-fatp5-hcc-abstract.md
61. wang-2021-fatp5-hcc-summary.md
62. watkins-2007-26-acs-genes-abstract.md
63. watkins-2007-26-acs-genes-summary.md
64. watkins-2008-vlcs-review-abstract.md
65. watkins-2008-vlcs-review-summary.md
66. zhang-2026-fatp2-mechanism-abstract.md
67. zhang-2026-fatp2-mechanism-summary.md
68. zhou-2010-fatp4-fatp5-hts-abstract.md
69. zhou-2010-fatp4-fatp5-hts-summary.md