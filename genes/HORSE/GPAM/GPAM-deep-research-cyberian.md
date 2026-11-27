---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T02:44:21.865525'
end_time: '2026-10-26T02:57:07.532457'
duration_seconds: 765.67
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: GPAM
  gene_symbol: GPAM
  uniprot_accession: A0A9L0TTC1
  protein_description: 'RecName: Full=Glycerol-3-phosphate acyltransferase 1, mitochondrial
    {ECO:0000256|ARBA:ARBA00017577, ECO:0000256|PIRNR:PIRNR000437}; EC=2.3.1.15 {ECO:0000256|ARBA:ARBA00013113,
    ECO:0000256|PIRNR:PIRNR000437};'
  gene_info: Name=GPAM {ECO:0000313|Ensembl:ENSECAP00000089988.1};
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the GPAT/DAPAT family.
  protein_domains: GPAT/DHAPAT. (IPR022284); GPAT/DHAPAT_C. (IPR045520); GPAT/DHAPAT_LPLAT.
    (IPR041728); GPAT_PlsB. (IPR028354); Plipid/glycerol_acylTrfase. (IPR002123)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3303
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 77
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0TTC1
- **Protein Description:** RecName: Full=Glycerol-3-phosphate acyltransferase 1, mitochondrial {ECO:0000256|ARBA:ARBA00017577, ECO:0000256|PIRNR:PIRNR000437}; EC=2.3.1.15 {ECO:0000256|ARBA:ARBA00013113, ECO:0000256|PIRNR:PIRNR000437};
- **Gene Information:** Name=GPAM {ECO:0000313|Ensembl:ENSECAP00000089988.1};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the GPAT/DAPAT family.
- **Key Domains:** GPAT/DHAPAT. (IPR022284); GPAT/DHAPAT_C. (IPR045520); GPAT/DHAPAT_LPLAT. (IPR041728); GPAT_PlsB. (IPR028354); Plipid/glycerol_acylTrfase. (IPR002123)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GPAM" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GPAM' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GPAM** (gene ID: GPAM, UniProt: A0A9L0TTC1) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GPAM (Glycerol-3-phosphate acyltransferase 1, mitochondrial) in the horse, *Equus caballus* (UniProt A0A9L0TTC1)

## 1. Introduction and summary

Horse GPAM (UniProt A0A9L0TTC1) is the equine ortholog of mitochondrial glycerol-3-phosphate acyltransferase 1 (GPAT1; EC 2.3.1.15). This enzyme catalyzes the first, committed and rate-limiting step of de novo glycerolipid synthesis: it transfers a long-chain acyl group from acyl-CoA to the sn-1 position of sn-glycerol 3-phosphate (G3P), producing 1-acyl-sn-glycerol 3-phosphate (lysophosphatidic acid, LPA) and free CoA [wendel-2009-gpat-review-abstract][gimeno-2008-mammalian-gpat-review-abstract][jerkins-1995-gpat-promoter-abstract]. The horse protein is known only as an unreviewed, automatically annotated TrEMBL entry (protein existence level 3, "inferred from homology") predicted from the Thoroughbred reference genome [uniprot-A0A9L0TTC1-entry][wade-2009-horse-genome-abstract]. No biochemical or cell-biological experiment has been done on equine GPAM. Its function must therefore be inferred from orthologs, chiefly mouse, rat and human GPAT1, which are among the best-characterized lipid-synthesis enzymes in mammals.

The symbol is not ambiguous. In every mammalian genome, "GPAM" denotes the mitochondrial, N-ethylmaleimide (NEM)-resistant GPAT1 isoform. It is distinct from the NEM-sensitive mitochondrial paralog GPAT2, from the microsomal GPAT3 and GPAT4 (formerly AGPAT9/AGPAT8 and AGPAT6), and from the peroxisomal dihydroxyacetone-phosphate acyltransferase GNPAT [gimeno-2008-mammalian-gpat-review-abstract][wang-2007-gpat2-cloning-abstract][wendel-2009-gpat-review-fulltext]. The ER paralog GPAT4 (formerly AGPAT6), for example, is NEM-sensitive and uses saturated and unsaturated acyl-CoAs equally, which contrasts with the properties of GPAM [chen-2008-agpat6-microsomal-gpat-abstract]. The horse protein is 90% identical to human GPAT1 over the full human length. It conserves every catalytic, CoA-binding and mitochondrial-targeting residue that has been tested experimentally in the human enzyme [NOTES_sequence_analysis.md][uniprot-Q9HCL2-human-GPAT1-entry]. Its InterPro/Pfam domain composition (Plipid/glycerol_acylTrfase PF01553 with a PlsC acyltransferase domain at residues 224-357, GPAT_C PF19277, GPAT_PlsB and GPAT/DHAPAT) and PANTHER subfamily PTHR12563:SF16 ("Glycerol-3-phosphate acyltransferase 1, mitochondrial") match that identity [uniprot-A0A9L0TTC1-entry].

From the orthologs, horse GPAM is expected to work as a peripheral protein of the cytosolic face of the outer mitochondrial membrane. There it competes with carnitine palmitoyltransferase-1 (CPT1) for the shared pool of long-chain acyl-CoA, and so helps decide whether fatty acids are esterified into triacylglycerol (TAG) and phospholipids or are oxidized [wendel-2009-gpat-review-fulltext][lewin-2005-gpat1-hepatocytes-abstract][hammond-2005-gpat1-liver-acylcoa-abstract]. It prefers saturated acyl-CoAs, especially palmitoyl-CoA (16:0), and so largely sets the saturated sn-1 acyl chain of hepatic glycerolipids [yet-1993-mitochondrial-gpat-p90-abstract][hammond-2002-gpat1-knockout-abstract][johnson-2023-gpat1-structure-abstract]. Its expression is driven by insulin through SREBP-1c. Its activity is acutely suppressed by AMPK and stimulated by CK2 phosphorylation [ericsson-1997-gpat-srebp-abstract][wendel-2009-gpat-review-fulltext][park-2002-ampk-gpat-exercise-abstract][muoio-1999-ampk-gpat-abstract][onorato-2005-gpat1-ck2-abstract]. In horses, the only gene-specific primary data are transcriptomic: GPAM is among the lipid-metabolism genes expressed differently between muscles of Mongolian horses [liu-2026-mongolian-horse-meat-abstract].

## 2. Gene identity, isoforms and evolutionary conservation

A0A9L0TTC1 is a 790-residue protein encoded by Ensembl gene ENSECAG00000014742 on horse chromosome 1 (transcript ENSECAT00000105322.1, protein ENSECAP00000089988.1). It was annotated from the EquCab genome assembly that descends from the Broad Institute horse genome project [uniprot-A0A9L0TTC1-entry][wade-2009-horse-genome-abstract]. All of its functional annotations come from automatic rules (ARBA and PIRNR000437) and have the evidence code ECO:0000256, not from curation of horse data [uniprot-A0A9L0TTC1-entry]. UniProt lists several other unreviewed horse GPAM products from the same gene. One of them, A0A9L0TCA8, is 828 residues long, exactly the length of human and rat GPAT1 [uniprot-A0A9L0TCA8-entry][uniprot-Q9HCL2-human-GPAT1-entry].

To check the identity, we aligned A0A9L0TTC1 globally with reviewed human GPAT1 (Q9HCL2) and rat GPAT1 (P97564). There were 744 identical positions with human (≈90%) and 712 with rat (≈86%) [NOTES_sequence_analysis.md]. The only structural difference is a single in-frame deletion of 38 residues relative to human (human residues 371-408, …GKPKKNESLWSVARGVIRMLRKNYGCVRVDFAQPFSL…). Because the same gene encodes a full-length 828-residue product, A0A9L0TTC1 most likely represents an exon-skipping splice isoform, not the canonical horse protein [NOTES_sequence_analysis.md][uniprot-A0A9L0TCA8-entry]. This matters for annotation: the deleted segment contains human Met388, and an M388W substitution impairs catalysis [uniprot-Q9HCL2-human-GPAT1-entry]. Whether the 790-residue isoform is active is therefore uncertain (see Open Questions). Alternative transcripts of GPAM have also been reported in cattle, where two different 5′ UTRs were found [roy-2006-bovine-gpam-structure-abstract].

GPAM is highly conserved across mammals. Bovine GPAM encodes an 825-residue protein that is 89-93% similar to the mouse and human proteins [roy-2006-bovine-gpam-structure-abstract]. GPAT1 also shows homology over ~300 residues to the bacterial G3P acyltransferase PlsB of *Escherichia coli* [yet-1993-mitochondrial-gpat-p90-abstract]. A mitochondrial, NEM-resistant, palmitoyl-CoA-preferring GPAT activity that resembles mammalian GPAT1 is present even in the hepatopancreas of the crustacean *Macrobrachium borellii*. This has led to the suggestion that GPAT1 may be the GPAT isoform that appeared first in evolution [pellon-maison-2009-macrobrachium-mtgpat-abstract]. Within mammals, the GPAT1 isoform differs from GPAT2 in sequence (only 27% identity), in NEM sensitivity, in acyl-CoA preference and in tissue distribution [wang-2007-gpat2-cloning-abstract].

## 3. Catalytic function and substrate specificity

The reaction is acyl-CoA + sn-glycerol 3-phosphate → 1-acyl-sn-glycerol 3-phosphate + CoA (RHEA:15325; EC 2.3.1.15) [uniprot-A0A9L0TTC1-entry][jerkins-1995-gpat-promoter-abstract]. The first direct proof that the GPAM gene product is the catalyst came from the Sul laboratory. They identified the refeeding-induced p90 cDNA as mitochondrial GPAT because p90 protein tracked NEM-resistant mitochondrial GPAT activity in liver and in differentiating adipocytes [yet-1993-mitochondrial-gpat-p90-abstract]. They then expressed p90 in insect cells via baculovirus, which sharply increased NEM-resistant mitochondrial GPAT activity, and purified and reconstituted the enzyme in phospholipids [yet-1995-gpat-purification-abstract]. GPAT1 was in fact the only enzyme of the glycerol-3-phosphate pathway to be purified to homogeneity before the molecular-cloning era [coleman-2011-tag-metabolism-review-fulltext].

Substrate preference is the classic biochemical hallmark of the mitochondrial isoform. Early work on subcellular fractions found that the microsomal GPAT activity was NEM-sensitive and showed no acyl-CoA preference. The mitochondrial activity, by contrast, resisted NEM and preferred saturated acyl-CoAs such as 16:0-CoA and 18:0-CoA [wendel-2009-gpat-review-fulltext][yet-1993-mitochondrial-gpat-p90-abstract]. GPAT1 favors palmitoyl-CoA (16:0) in particular [lewin-2008-gpat1-heart-abstract][coleman-2011-tag-metabolism-review-fulltext]. Cryo-EM of human GPAT1 gave a structural explanation: a narrow hydrophobic cleft selects linear (saturated) acyl chains, and catalytic activity is highest with 16-carbon substrates [johnson-2023-gpat1-structure-abstract][uniprot-Q9HCL2-human-GPAT1-entry]. The automatic annotation of the horse entry lists activity with 12:0-, 16:0-, 18:0-, 18:1- and 18:2-CoA [uniprot-A0A9L0TTC1-entry]. This is consistent with a broad long-chain acceptance in which palmitoyl-CoA is preferred.

Gene-deletion studies support the in vivo relevance of this specificity. In Gpam-/- mouse liver, TAG, phosphatidylcholine (PC) and phosphatidylethanolamine (PE) contain less palmitate. Positional analysis showed about 21% less 16:0 at the sn-1 position of PC and PE and 36-40% more arachidonate (20:4) at sn-2 [hammond-2002-gpat1-knockout-abstract]. Similar changes, with less 16:0 and more 20:4n6 in PC, PE and PS/PI, occur in Gpat1-/- hearts [lewin-2008-gpat1-heart-abstract]. The knockout also shifts the remaining acyl chains: PE gains 18:0 and 18:1 at sn-1, and the sn-2 position gains 20:5 and loses 22:6 [wendel-2009-gpat-review-fulltext]. Thus GPAT1 is the main source of saturated sn-1 chains in glycerolipids of lipogenic tissues. Its output indirectly affects which polyunsaturated acyl chains are found at sn-2 [wendel-2009-gpat-review-fulltext][coleman-2011-tag-metabolism-review-fulltext].

## 4. Structure and catalytic mechanism

GPAM belongs to the Pfam PF01553 glycerolipid acyltransferase family. Members share four conserved blocks, first defined bioinformatically and then tested by mutagenesis of *E. coli* PlsB: block I [NX]-H-[RQ]-S-X-[LYIM]-D; block II G-X-[IF]-F-I-[RD]-R; block III F-[PLI]-E-G-[TG]-R-[SX]-[RX]; and block IV [VI]-[PX]-[IVL]-[IV]-P-[VI] [lewin-1999-acyltransferase-motifs-abstract]. The block I histidine and aspartate, the block III glycine and the block IV proline are needed for catalysis. The block II phenylalanine and arginine and the block III glutamate and serine bind G3P [lewin-1999-acyltransferase-motifs-abstract]. Mutagenesis of the corresponding residues in mouse GPAT1 confirmed their importance in the mammalian enzyme [wendel-2009-gpat-review-fulltext]. Horse GPAM carries the block I motif as "HRSHID" at residues 230-235 and the block III "EGTR" at residues 315-318, at the same positions as in human GPAT1 [NOTES_sequence_analysis.md].

The 2023 cryo-EM structures of human GPAT1 (residues 80-828), with a substrate analog or product bound, show an N-terminal acyltransferase domain holding the catalytic motifs and a tightly associated C-terminal domain that is critical for folding [johnson-2023-gpat1-structure-abstract]. The HXXXXD motif contacts both the cysteamine moiety of acyl-CoA and the phosphate of G3P. Substitutions H230A, H233W, G273L, R278A, F313A and R318A each abolish activity, and M388W impairs it [uniprot-Q9HCL2-human-GPAT1-entry]. The structural work also revealed a hydrophobic channel inside GPAT1 that may conduct the lipid product toward the membrane [johnson-2023-gpat1-structure-abstract]. Earlier biochemistry had already shown that the C-terminal domain is essential: serial C-terminal truncations of rat GPAT1 were correctly targeted to mitochondria but inactive, and crosslinking showed that the N- and C-terminal regions interact [pellon-maison-2006-gpat1-cterminal-abstract]. All of the human residues listed above (H230, H233, R278, R279, K288, E315-R318) are identical in horse A0A9L0TTC1 [NOTES_sequence_analysis.md]. Met388 is absent from the 790-residue isoform because of the 38-residue deletion, but it is presumably present in the 828-residue product [NOTES_sequence_analysis.md][uniprot-A0A9L0TCA8-entry].

## 5. Subcellular localization and membrane topology

GPAT1 is defined by its location on the mitochondrial outer membrane. p90 was detected in liver mitochondrial fractions, and the polyhistidine-tagged recombinant protein still reached mitochondria in insect cells [yet-1993-mitochondrial-gpat-p90-abstract][yet-1995-gpat-purification-abstract]. Protease-protection and epitope-accessibility studies on rat GPAT1 in CHO cells and isolated liver mitochondria placed the catalytic N-terminal domain on the cytosolic face of the outer mitochondrial membrane. These studies proposed a model with two transmembrane segments and an intermembrane-space loop [gonzalez-baro-2001-gpat-topology-abstract]. That model was later revised. The human GPAT1 cryo-EM structures contain no transmembrane helices. Instead the enzyme binds the membrane through an amphipathic surface patch and an N-terminal loop-helix region that carries a mitochondrial-targeting signal [johnson-2023-gpat1-structure-abstract]. Charge-reversal of a cluster of basic residues in this region (R89, H98, R100, H101, R102, R107, R108, R118) abolishes mitochondrial localization. UniProt accordingly classifies GPAT1 as a peripheral protein of the mitochondrial outer membrane [uniprot-Q9HCL2-human-GPAT1-entry]. All eight basic residues are conserved in horse GPAM [NOTES_sequence_analysis.md], so the equine protein should localize the same way, as the automatic annotation of the horse entry also predicts [uniprot-A0A9L0TTC1-entry]. The cytosolic orientation of the active site is common to both topology models. It means GPAT1 draws on the same cytosolic acyl-CoA pool that CPT1 uses at the outer membrane [wendel-2009-gpat-review-fulltext].

## 6. Pathway context: the glycerol-3-phosphate (Kennedy) pathway and acyl-CoA partitioning

The LPA made by GPAT1 enters the glycerol-3-phosphate pathway. Acylglycerol-3-phosphate acyltransferases (AGPATs) acylate LPA to phosphatidic acid (PA). Lipin phosphatidic-acid phosphatases convert PA to diacylglycerol (DAG), and DGAT enzymes convert DAG to TAG. PA and DAG are also the branch points for synthesis of PC, PE, PS, PI, phosphatidylglycerol and cardiolipin, partly via CDP-DAG [wendel-2009-gpat-review-fulltext][coleman-2011-tag-metabolism-review-fulltext]. For this reason, the horse entry assigns GPAM to step 1 of 3 of CDP-diacylglycerol biosynthesis [uniprot-A0A9L0TTC1-entry]. GPAT1 sits on the outer mitochondrial membrane, while the terminal enzyme of TAG synthesis, DGAT, sits on the endoplasmic reticulum. Even so, many studies support an important role for GPAT1 in TAG synthesis [wendel-2009-gpat-review-fulltext]. This implies that GPAT1-derived intermediates move between organelles, a step whose mechanism the sources reviewed here do not define.

A second, equally important function of GPAT1 is to partition acyl-CoA. GPAT1 and CPT1 are both outer-membrane enzymes that appear to compete for the same long-chain acyl-CoAs. GPAT1 sends them into esterification, and CPT1 sends them into mitochondrial β-oxidation [wendel-2009-gpat-review-fulltext]. Overexpressing rat GPAT1 13-fold in primary hepatocytes more than doubled oleate incorporation into TAG and lowered oleate oxidation by about 40% [lewin-2005-gpat1-hepatocytes-abstract]. Conversely, Gpam-/- livers contain three times more acyl-CoA, more acylcarnitines and more β-hydroxybutyrate, and less TAG [hammond-2005-gpat1-liver-acylcoa-abstract]. Liver-directed overexpression of GPAT1 in mice caused a 12-fold rise in hepatic TAG and a 7-fold rise in DAG, lowered fatty-acid oxidation and doubled TAG secretion. A catalytically inactive mutant did not have these effects [linden-2006-gpat1-liver-overexpression-abstract]. GPAT1 contributes 30-50% of total GPAT activity in liver but only about 10% in most other tissues [coleman-2011-tag-metabolism-review-fulltext][linden-2006-gpat1-liver-overexpression-abstract]. Even so, it contributes substantially to TAG synthesis in heart [lewin-2008-gpat1-heart-abstract] and adipose tissue [hammond-2002-gpat1-knockout-abstract].

## 7. Regulation of expression and activity

Transcriptional control of GPAM is well defined in rodents. Mouse Gpam mRNA rises about 20-fold when fasted mice are refed carbohydrate, and the promoter contains insulin/glucose-responsive sequences within 322 bp of the transcription start [wendel-2009-gpat-review-fulltext][jerkins-1995-gpat-promoter-abstract]. The proximal promoter binds SREBP-1 (ADD1) and NF-Y, and both factors are required for transactivation [ericsson-1997-gpat-srebp-abstract]. Hepatic induction by refeeding is lost in SREBP-1-null mice. It is unchanged in ChREBP-null mice, which identifies insulin-driven SREBP-1c, not ChREBP, as the main driver [wendel-2009-gpat-review-fulltext]. Gpam is also strongly induced during adipocyte differentiation [yet-1993-mitochondrial-gpat-p90-abstract][ericsson-1997-gpat-srebp-abstract].

Post-translational control is also prominent. In rat tissues, GPAT1 mRNA, protein and specific activity are discordant. Fasting lowers, and refeeding raises above baseline, GPAT1 protein and activity in a tissue-specific way, which suggests acute regulation [lewin-2001-gpat-feeding-regulation-abstract]. AMPK activation by exercise or AICAR lowers GPAT activity by about 50% in liver and adipose tissue, in parallel with inhibition of acetyl-CoA carboxylase and activation of malonyl-CoA decarboxylase [park-2002-ampk-gpat-exercise-abstract]. The selectivity of this effect was established earlier. In rat hepatocytes, AICA riboside lowered mitochondrial GPAT activity by 22-34% within 15-30 minutes without changing microsomal GPAT, DGAT or acyl-CoA synthetase. Purified recombinant AMPKα1 and AMPKα2 inhibited hepatic mitochondrial GPAT in a time- and ATP-dependent manner, and in hepatocytes and soleus muscle AICA riboside shifted oleate from TAG synthesis to oxidation [muoio-1999-ampk-gpat-abstract]. Together these results favor oxidation over esterification at the outer mitochondrial membrane. They strongly suggest that AMPK phosphorylates GPAT1, but no AMPK site on GPAT1 has been mapped, so direct phosphorylation remains formally unproven [wendel-2009-gpat-review-fulltext]. Casein kinase 2 (CK2), in contrast, has been shown biochemically to phosphorylate GPAT1. In rat liver mitochondria, CK2 labels an ~85-kDa protein identified as mitochondrial GPAT by immunoprecipitation, and it stimulates GPAT activity. The CK2 inhibitors heparin and DRB block both effects, and outer mitochondrial membranes incubated with cytosol also phosphorylate the enzyme [onorato-2005-gpat1-ck2-abstract]. CK2 increases GPAT1 activity by 50-200% in liver and T lymphocytes, but because it also activates CPT1, it does not reciprocally partition acyl-CoA in the way AMPK does [wendel-2009-gpat-review-fulltext]. The UniProt keywords "Phosphoprotein" and "Acetylation" are transferred to the horse entry by automatic annotation [uniprot-A0A9L0TTC1-entry]. Specific sites, such as Ser695 phosphorylation found in human liver phosphoproteomics, have been mapped only in human [uniprot-Q9HCL2-human-GPAT1-entry].

## 8. Physiological roles in mammals and evidence from horses and other livestock

Loss-of-function mice define the physiological role of GPAT1. Gpam-/- mice weigh less, have smaller gonadal fat pads, lower hepatic and plasma TAG, and lower VLDL-TAG secretion [hammond-2002-gpat1-knockout-abstract]. They are protected from high-fat-diet hepatic steatosis and hepatic insulin resistance, possibly because less DAG accumulates to activate PKC [neschen-2005-gpat1-ko-steatosis-abstract]. These protective effects depend on sex and diet. In a separately derived line they were seen mainly in chow-fed females and disappeared with long-term high-fat feeding [yazdi-2008-gpat1-highfat-abstract]. Beyond lipid storage, GPAT1-dependent phospholipid synthesis is needed for the metabolic activation of CD4+ T cells. GPAT1-null T cells show lower oxygen consumption, glycolytic flux, spare respiratory capacity and mitochondrial membrane potential after stimulation [faris-2014-gpat1-tcell-abstract]. In humans, a common intronic variant in GPAM (rs10787429) is associated with liver injury, alcohol-related and fatty liver disease, and higher plasma cholesterol. Single-cell data place GPAM expression mainly in VLDL-producing hepatocytes [hakim-2021-gpam-variant-liver-abstract][hakim-2021-gpam-variant-liver-fulltext].

Livestock work shows that the TAG-synthesizing role of GPAM holds in ungulates, though expression patterns can differ by species. In cattle, GPAM mRNA is highest in adipose tissue and lung and barely detectable in liver, unlike rodents [roy-2006-bovine-gpam-structure-abstract]. GPAM knockdown lowers TAG synthesis in bovine fibroblasts and mammary epithelial cells, overexpression raises it, and GPAM polymorphisms are associated with intramuscular fat composition, marbling and milk-fat traits [yu-2017-bovine-gpam-abstract][yu-2021-bovine-gpam-milk-abstract]. Horses are non-ruminant hindgut fermenters, and the bovine liver-expression pattern cannot be assumed for them. Direct tissue-expression data for horse GPAM are lacking.

The only primary horse study that names GPAM is a 2026 transcriptomic and meat-quality analysis of Mongolian horses. RNA-seq of forelimb versus hindlimb muscle found 513 differentially expressed genes, enriched in glycerophospholipid metabolism and PPAR signaling. GPAM was among four candidate lipid- and meat-quality genes (with SLC16A7, FABP3 and TNNC1) that were markedly up-regulated in forelimb muscle, which had better tenderness, and the difference was confirmed by RT-qPCR [liu-2026-mongolian-horse-meat-abstract][liu-2026-mongolian-horse-meat-fulltext]. The authors suggest that GPAM, as the rate-limiting enzyme of TAG and phospholipid synthesis, may contribute to intramuscular fat deposition [liu-2026-mongolian-horse-meat-fulltext]. This evidence is correlative and does not test enzyme function. Taken together, the functional annotation of horse GPAM rests on strong orthology to experimentally characterized mammalian GPAT1 and on conservation of experimentally validated residues, supported by consistent livestock data.

## Open Questions

Several questions remain about the horse protein specifically. First, the annotated entry A0A9L0TTC1 lacks 38 residues (human 371-408) that are present in an 828-residue product of the same gene. Whether this isoform is expressed as protein, which tissues use it, and whether it is active are unknown. The missing segment contains Met388, whose substitution impairs catalysis in human GPAT1 [uniprot-Q9HCL2-human-GPAT1-entry]. RT-PCR across the affected exon in equine liver, adipose and muscle, followed by recombinant expression of both isoforms and NEM-resistant GPAT assays with 16:0-CoA versus 18:1-CoA, would settle the question and show whether the equine enzyme keeps the palmitoyl-CoA preference. Second, the tissue distribution of GPAM expression and NEM-resistant GPAT activity in horses has not been measured. This matters because ruminants express GPAM mainly in adipose tissue rather than liver [roy-2006-bovine-gpam-structure-abstract], unlike rodents. Given GPAT1's role in hepatic TAG synthesis and VLDL secretion in mice and humans [hammond-2002-gpat1-knockout-abstract][hakim-2021-gpam-variant-liver-abstract], equine GPAM is a plausible but untested candidate in equine disorders of lipid and insulin metabolism; no study has examined it in that context. Third, it would be useful to know whether SREBP-1c-driven transcription and AMPK-mediated suppression work the same way in equine liver and muscle. This is especially relevant in exercised horses, since exercise-induced AMPK activation suppresses GPAT activity in rodents [park-2002-ampk-gpat-exercise-abstract]. Fourth, the Mongolian-horse transcriptomic link between GPAM and muscle-site meat quality needs replication in other breeds and functional follow-up, and population-level association studies (as done for cattle and humans) have not yet been reported for horse GPAM variants. Finally, at the general level, the way GPAT1-derived LPA moves from the outer mitochondrial membrane to ER-resident AGPAT/lipin/DGAT enzymes, and the exact residues phosphorylated by AMPK and CK2, remain unresolved questions for all mammals. Mapping these sites in human or rodent GPAT1 would show whether they are conserved in horse GPAM.

## References

* **uniprot-A0A9L0TTC1-entry**: UniProtKB/TrEMBL entry A0A9L0TTC1_HORSE, "Glycerol-3-phosphate acyltransferase 1, mitochondrial", *Equus caballus*, entry version 14 (10-JUN-2026). https://rest.uniprot.org/uniprotkb/A0A9L0TTC1.txt
* **uniprot-A0A9L0TCA8-entry**: UniProtKB/TrEMBL entry A0A9L0TCA8 (horse GPAM, 828 aa; Ensembl ENSECAP00000084732.1). https://rest.uniprot.org/uniprotkb/A0A9L0TCA8.txt
* **uniprot-Q9HCL2-human-GPAT1-entry**: UniProtKB/Swiss-Prot entry Q9HCL2 (GPAT1_HUMAN), Glycerol-3-phosphate acyltransferase 1, mitochondrial, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/Q9HCL2.txt
* **NOTES_sequence_analysis.md**: Sequence alignment notes made for this report (Biopython global alignment of A0A9L0TTC1 against Q9HCL2 and P97564; UniProt FASTA sequences).
* **chen-2008-agpat6-microsomal-gpat**: Chen YQ, Kuo MS, Li S, Bui HH, Peake DA, Sanders PE, Thibodeaux SJ, Chu S, Qian YW, Zhao Y, Bredt DS, Moller DE, Konrad RJ, Beigneux AP, Young SG, Cao G. AGPAT6 is a novel microsomal glycerol-3-phosphate acyltransferase. *The Journal of biological chemistry* 2008;283(15):10048-10057. PMID: 18238778; PMCID: PMC2442282; DOI: [10.1074/jbc.m708151200](https://doi.org/10.1074/jbc.m708151200). https://pubmed.ncbi.nlm.nih.gov/18238778/
* **coleman-2011-tag-metabolism-review**: Coleman RA, Mashek DG. Mammalian triacylglycerol metabolism: synthesis, lipolysis, and signaling. *Chemical reviews* 2011;111(10):6359-6386. PMID: 21627334; PMCID: PMC3181269; DOI: [10.1021/cr100404w](https://doi.org/10.1021/cr100404w). https://pubmed.ncbi.nlm.nih.gov/21627334/
* **ericsson-1997-gpat-srebp**: Ericsson J, Jackson SM, Kim JB, Spiegelman BM, Edwards PA. Identification of glycerol-3-phosphate acyltransferase as an adipocyte determination and differentiation factor 1- and sterol regulatory element-binding protein-responsive gene. *The Journal of biological chemistry* 1997;272(11):7298-7305. PMID: 9054427; DOI: [10.1074/jbc.272.11.7298](https://doi.org/10.1074/jbc.272.11.7298). https://pubmed.ncbi.nlm.nih.gov/9054427/
* **faris-2014-gpat1-tcell**: Faris R, Fan YY, De Angulo A, Chapkin RS, deGraffenried LA, Jolly CA. Mitochondrial glycerol-3-phosphate acyltransferase-1 is essential for murine CD4(+) T cell metabolic activation. *Biochimica et biophysica acta* 2014;1842(10):1475-1482. PMID: 25066474; PMCID: PMC4169305; DOI: [10.1016/j.bbalip.2014.07.009](https://doi.org/10.1016/j.bbalip.2014.07.009). https://pubmed.ncbi.nlm.nih.gov/25066474/
* **gimeno-2008-mammalian-gpat-review**: Gimeno RE, Cao J. Thematic review series: glycerolipids. Mammalian glycerol-3-phosphate acyltransferases: new genes for an old activity. *Journal of lipid research* 2008;49(10):2079-2088. PMID: 18658143; DOI: [10.1194/jlr.r800013-jlr200](https://doi.org/10.1194/jlr.r800013-jlr200). https://pubmed.ncbi.nlm.nih.gov/18658143/
* **gonzalez-baro-2001-gpat-topology**: Gonzalez-Baro MR, Granger DA, Coleman RA. Mitochondrial glycerol phosphate acyltransferase contains two transmembrane domains with the active site in the N-terminal domain facing the cytosol. *The Journal of biological chemistry* 2001;276(46):43182-43188. PMID: 11557771; DOI: [10.1074/jbc.m107885200](https://doi.org/10.1074/jbc.m107885200). https://pubmed.ncbi.nlm.nih.gov/11557771/
* **hakim-2021-gpam-variant-liver**: Hakim A, Moll M, Brancale J, Liu J, Lasky-Su JA, Silverman EK, Vilarinho S, Jiang ZG, Pita-Juárez YH, Vlachos IS, Zhang X, Åberg F, Afdhal NH, Hobbs BD, Cho MH. Genetic Variation in the Mitochondrial Glycerol-3-Phosphate Acyltransferase Is Associated With Liver Injury. *Hepatology (Baltimore, Md.)* 2021;74(6):3394-3408. PMID: 34216018; PMCID: PMC8639615; DOI: [10.1002/hep.32038](https://doi.org/10.1002/hep.32038). https://pubmed.ncbi.nlm.nih.gov/34216018/
* **hammond-2002-gpat1-knockout**: Hammond LE, Gallagher PA, Wang S, Hiller S, Kluckman KD, Posey-Marcos EL, Maeda N, Coleman RA. Mitochondrial glycerol-3-phosphate acyltransferase-deficient mice have reduced weight and liver triacylglycerol content and altered glycerolipid fatty acid composition. *Molecular and cellular biology* 2002;22(23):8204-8214. PMID: 12417724; PMCID: PMC134068; DOI: [10.1128/mcb.22.23.8204-8214.2002](https://doi.org/10.1128/mcb.22.23.8204-8214.2002). https://pubmed.ncbi.nlm.nih.gov/12417724/
* **hammond-2005-gpat1-liver-acylcoa**: Hammond LE, Neschen S, Romanelli AJ, Cline GW, Ilkayeva OR, Shulman GI, Muoio DM, Coleman RA. Mitochondrial glycerol-3-phosphate acyltransferase-1 is essential in liver for the metabolism of excess acyl-CoAs. *The Journal of biological chemistry* 2005;280(27):25629-25636. PMID: 15878874; DOI: [10.1074/jbc.m503181200](https://doi.org/10.1074/jbc.m503181200). https://pubmed.ncbi.nlm.nih.gov/15878874/
* **jerkins-1995-gpat-promoter**: Jerkins AA, Liu WR, Lee S, Sul HS. Characterization of the murine mitochondrial glycerol-3-phosphate acyltransferase promoter. *The Journal of biological chemistry* 1995;270(3):1416-1421. PMID: 7836409; DOI: [10.1074/jbc.270.3.1416](https://doi.org/10.1074/jbc.270.3.1416). https://pubmed.ncbi.nlm.nih.gov/7836409/
* **johnson-2023-gpat1-structure**: Johnson ZL, Ammirati M, Wasilko DJ, Chang JS, Noell S, Foley TL, Yoon H, Smith K, Asano S, Hales K, Wan M, Yang Q, Piotrowski MA, Farley KA, Gilbert T, Aschenbrenner LM, Fennell KF, Dutra JK, Xu M, Guo C, Varghese AE, Bellenger J, Quinn A, Am Ende CW, West GM, Griffor MC, Bennett D, Calabrese M, Steppan CM, Han S, Wu H. Structural basis of the acyl-transfer mechanism of human GPAT1. *Nature structural & molecular biology* 2023;30(1):22-30. PMID: 36522428; DOI: [10.1038/s41594-022-00884-7](https://doi.org/10.1038/s41594-022-00884-7). https://pubmed.ncbi.nlm.nih.gov/36522428/
* **lewin-1999-acyltransferase-motifs**: Lewin TM, Wang P, Coleman RA. Analysis of amino acid motifs diagnostic for the sn-glycerol-3-phosphate acyltransferase reaction. *Biochemistry* 1999;38(18):5764-5771. PMID: 10231527; DOI: [10.1021/bi982805d](https://doi.org/10.1021/bi982805d). https://pubmed.ncbi.nlm.nih.gov/10231527/
* **lewin-2001-gpat-feeding-regulation**: Lewin TM, Granger DA, Kim JH, Coleman RA. Regulation of mitochondrial sn-glycerol-3-phosphate acyltransferase activity: response to feeding status is unique in various rat tissues and is discordant with protein expression. *Archives of biochemistry and biophysics* 2001;396(1):119-127. PMID: 11716470; DOI: [10.1006/abbi.2001.2604](https://doi.org/10.1006/abbi.2001.2604). https://pubmed.ncbi.nlm.nih.gov/11716470/
* **lewin-2005-gpat1-hepatocytes**: Lewin TM, Wang S, Nagle CA, Van Horn CG, Coleman RA. Mitochondrial glycerol-3-phosphate acyltransferase-1 directs the metabolic fate of exogenous fatty acids in hepatocytes. *American journal of physiology. Endocrinology and metabolism* 2005;288(5):E835-44. PMID: 15598672; DOI: [10.1152/ajpendo.00300.2004](https://doi.org/10.1152/ajpendo.00300.2004). https://pubmed.ncbi.nlm.nih.gov/15598672/
* **lewin-2008-gpat1-heart**: Lewin TM, de Jong H, Schwerbrock NJ, Hammond LE, Watkins SM, Combs TP, Coleman RA. Mice deficient in mitochondrial glycerol-3-phosphate acyltransferase-1 have diminished myocardial triacylglycerol accumulation during lipogenic diet and altered phospholipid fatty acid composition. *Biochimica et biophysica acta* 2008;1781(6-7):352-358. PMID: 18522808; PMCID: PMC3285559; DOI: [10.1016/j.bbalip.2008.05.001](https://doi.org/10.1016/j.bbalip.2008.05.001). https://pubmed.ncbi.nlm.nih.gov/18522808/
* **linden-2006-gpat1-liver-overexpression**: Lindén D, William-Olsson L, Ahnmark A, Ekroos K, Hallberg C, Sjögren HP, Becker B, Svensson L, Clapham JC, Oscarsson J, Schreyer S. Liver-directed overexpression of mitochondrial glycerol-3-phosphate acyltransferase results in hepatic steatosis, increased triacylglycerol secretion and reduced fatty acid oxidation. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology* 2006;20(3):434-443. PMID: 16507761; DOI: [10.1096/fj.05-4568com](https://doi.org/10.1096/fj.05-4568com). https://pubmed.ncbi.nlm.nih.gov/16507761/
* **liu-2026-mongolian-horse-meat**: Liu Y, Wang X, Tan G, Dugarjaviina M, Zhang X. Meat Quality Characteristics of Mongolian Horses in Inner Mongolia: Regional Superiority and Transcriptomic Insights into Tenderness Differences Between Muscular Locations. *Animals : an open access journal from MDPI* 2026;16(12):1788. PMID: 42353398; PMCID: PMC13295530; DOI: [10.3390/ani16121788](https://doi.org/10.3390/ani16121788). https://pubmed.ncbi.nlm.nih.gov/42353398/
* **muoio-1999-ampk-gpat**: Muoio DM, Seefeld K, Witters LA, Coleman RA. AMP-activated kinase reciprocally regulates triacylglycerol synthesis and fatty acid oxidation in liver and muscle: evidence that sn-glycerol-3-phosphate acyltransferase is a novel target. *The Biochemical journal* 1999;338 ( Pt 3):783-791. PMID: 10051453; PMCID: PMC1220117; DOI: [10.1042/bj3380783](https://doi.org/10.1042/bj3380783). https://pubmed.ncbi.nlm.nih.gov/10051453/
* **neschen-2005-gpat1-ko-steatosis**: Neschen S, Morino K, Hammond LE, Zhang D, Liu ZX, Romanelli AJ, Cline GW, Pongratz RL, Zhang XM, Choi CS, Coleman RA, Shulman GI. Prevention of hepatic steatosis and hepatic insulin resistance in mitochondrial acyl-CoA:glycerol-sn-3-phosphate acyltransferase 1 knockout mice. *Cell metabolism* 2005;2(1):55-65. PMID: 16054099; DOI: [10.1016/j.cmet.2005.06.006](https://doi.org/10.1016/j.cmet.2005.06.006). https://pubmed.ncbi.nlm.nih.gov/16054099/
* **onorato-2005-gpat1-ck2**: Onorato TM, Chakraborty S, Haldar D. Phosphorylation of rat liver mitochondrial glycerol-3-phosphate acyltransferase by casein kinase 2. *The Journal of biological chemistry* 2005;280(20):19527-19534. PMID: 15778226; DOI: [10.1074/jbc.m410422200](https://doi.org/10.1074/jbc.m410422200). https://pubmed.ncbi.nlm.nih.gov/15778226/
* **park-2002-ampk-gpat-exercise**: Park H, Kaushik VK, Constant S, Prentki M, Przybytkowski E, Ruderman NB, Saha AK. Coordinate regulation of malonyl-CoA decarboxylase, sn-glycerol-3-phosphate acyltransferase, and acetyl-CoA carboxylase by AMP-activated protein kinase in rat tissues in response to exercise. *The Journal of biological chemistry* 2002;277(36):32571-32577. PMID: 12065578; DOI: [10.1074/jbc.m201692200](https://doi.org/10.1074/jbc.m201692200). https://pubmed.ncbi.nlm.nih.gov/12065578/
* **pellon-maison-2006-gpat1-cterminal**: Pellon-Maison M, Coleman RA, Gonzalez-Baró MR. The C-terminal region of mitochondrial glycerol-3-phosphate acyltransferase-1 interacts with the active site region and is required for activity. *Archives of biochemistry and biophysics* 2006;450(2):157-166. PMID: 16620760; DOI: [10.1016/j.abb.2006.03.009](https://doi.org/10.1016/j.abb.2006.03.009). https://pubmed.ncbi.nlm.nih.gov/16620760/
* **pellon-maison-2009-macrobrachium-mtgpat**: Pellon-Maison M, Garcia CF, Cattaneo ER, Coleman RA, Gonzalez-Baro MR. Macrobrachium borellii hepatopancreas contains a mitochondrial glycerol-3-phosphate acyltransferase which initiates triacylglycerol biosynthesis. *Lipids* 2009;44(4):337-344. PMID: 19130111; PMCID: PMC2823129; DOI: [10.1007/s11745-008-3275-1](https://doi.org/10.1007/s11745-008-3275-1). https://pubmed.ncbi.nlm.nih.gov/19130111/
* **roy-2006-bovine-gpam-structure**: Roy R, Ordovas L, Taourit S, Zaragoza P, Eggen A, Rodellar C. Genomic structure and an alternative transcript of bovine mitochondrial glycerol-3-phosphate acyltransferase gene (GPAM). *Cytogenetic and genome research* 2006;112(1-2):82-89. PMID: 16276094; DOI: [10.1159/000087517](https://doi.org/10.1159/000087517). https://pubmed.ncbi.nlm.nih.gov/16276094/
* **wade-2009-horse-genome**: Wade CM, Giulotto E, Sigurdsson S, Zoli M, Gnerre S, Imsland F, Lear TL, Adelson DL, Bailey E, Bellone RR, Blöcker H, Distl O, Edgar RC, Garber M, Leeb T, Mauceli E, MacLeod JN, Penedo MC, Raison JM, Sharpe T, Vogel J, Andersson L, Antczak DF, Biagi T, Binns MM, Chowdhary BP, Coleman SJ, Della Valle G, Fryc S, Guérin G, Hasegawa T, Hill EW, Jurka J, Kiialainen A, Lindgren G, Liu J, Magnani E, Mickelson JR, Murray J, Nergadze SG, Onofrio R, Pedroni S, Piras MF, Raudsepp T, Rocchi M, Røed KH, Ryder OA, Searle S, Skow L, Swinburne JE, Syvänen AC, Tozaki T, Valberg SJ, Vaudin M, White JR, Zody MC, Broad Institute Genome Sequencing Platform, Broad Institute Whole Genome Assembly Team, Lander ES, Lindblad-Toh K. Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science (New York, N.Y.)* 2009;326(5954):865-867. PMID: 19892987; PMCID: PMC3785132; DOI: [10.1126/science.1178158](https://doi.org/10.1126/science.1178158). https://pubmed.ncbi.nlm.nih.gov/19892987/
* **wang-2007-gpat2-cloning**: Wang S, Lee DP, Gong N, Schwerbrock NM, Mashek DG, Gonzalez-Baró MR, Stapleton C, Li LO, Lewin TM, Coleman RA. Cloning and functional characterization of a novel mitochondrial N-ethylmaleimide-sensitive glycerol-3-phosphate acyltransferase (GPAT2). *Archives of biochemistry and biophysics* 2007;465(2):347-358. PMID: 17689486; PMCID: PMC2133398; DOI: [10.1016/j.abb.2007.06.033](https://doi.org/10.1016/j.abb.2007.06.033). https://pubmed.ncbi.nlm.nih.gov/17689486/
* **wendel-2009-gpat-review**: Wendel AA, Lewin TM, Coleman RA. Glycerol-3-phosphate acyltransferases: rate limiting enzymes of triacylglycerol biosynthesis. *Biochimica et biophysica acta* 2009;1791(6):501-506. PMID: 19038363; PMCID: PMC2737689; DOI: [10.1016/j.bbalip.2008.10.010](https://doi.org/10.1016/j.bbalip.2008.10.010). https://pubmed.ncbi.nlm.nih.gov/19038363/
* **yazdi-2008-gpat1-highfat**: Yazdi M, Ahnmark A, William-Olsson L, Snaith M, Turner N, Osla F, Wedin M, Asztély AK, Elmgren A, Bohlooly-Y M, Schreyer S, Lindén D. The role of mitochondrial glycerol-3-phosphate acyltransferase-1 in regulating lipid and glucose homeostasis in high-fat diet fed mice. *Biochemical and biophysical research communications* 2008;369(4):1065-1070. PMID: 18339309; DOI: [10.1016/j.bbrc.2008.02.156](https://doi.org/10.1016/j.bbrc.2008.02.156). https://pubmed.ncbi.nlm.nih.gov/18339309/
* **yet-1993-mitochondrial-gpat-p90**: Yet SF, Lee S, Hahm YT, Sul HS. Expression and identification of p90 as the murine mitochondrial glycerol-3-phosphate acyltransferase. *Biochemistry* 1993;32(36):9486-9491. PMID: 8369314; DOI: [10.1021/bi00087a029](https://doi.org/10.1021/bi00087a029). https://pubmed.ncbi.nlm.nih.gov/8369314/
* **yet-1995-gpat-purification**: Yet SF, Moon YK, Sul HS. Purification and reconstitution of murine mitochondrial glycerol-3-phosphate acyltransferase. Functional expression in baculovirus-infected insect cells. *Biochemistry* 1995;34(22):7303-7310. PMID: 7779773; DOI: [10.1021/bi00022a003](https://doi.org/10.1021/bi00022a003). https://pubmed.ncbi.nlm.nih.gov/7779773/
* **yu-2017-bovine-gpam**: Yu H, Zhao Z, Yu X, Li J, Lu C, Yang R. Bovine lipid metabolism related gene GPAM: Molecular characterization, function identification, and association analysis with fat deposition traits. *Gene* 2017;609:9-18. PMID: 28131819; DOI: [10.1016/j.gene.2017.01.031](https://doi.org/10.1016/j.gene.2017.01.031). https://pubmed.ncbi.nlm.nih.gov/28131819/
* **yu-2021-bovine-gpam-milk**: Yu H, Zhao Y, Iqbal A, Xia L, Bai Z, Sun H, Fang X, Yang R, Zhao Z. Effects of polymorphism of the GPAM gene on milk quality traits and its relation to triglyceride metabolism in bovine mammary epithelial cells of dairy cattle. *Archives animal breeding* 2021;64(1):35-44. PMID: 34084902; PMCID: PMC8161264; DOI: [10.5194/aab-64-35-2021](https://doi.org/10.5194/aab-64-35-2021). https://pubmed.ncbi.nlm.nih.gov/34084902/


## Citations

1. chen-2008-agpat6-microsomal-gpat-abstract.md
2. chen-2008-agpat6-microsomal-gpat-summary.md
3. coleman-2011-tag-metabolism-review-abstract.md
4. coleman-2011-tag-metabolism-review-fulltext.txt
5. coleman-2011-tag-metabolism-review-summary.md
6. ericsson-1997-gpat-srebp-abstract.md
7. ericsson-1997-gpat-srebp-summary.md
8. faris-2014-gpat1-tcell-abstract.md
9. faris-2014-gpat1-tcell-fulltext.txt
10. faris-2014-gpat1-tcell-summary.md
11. gimeno-2008-mammalian-gpat-review-abstract.md
12. gimeno-2008-mammalian-gpat-review-summary.md
13. gonzalez-baro-2001-gpat-topology-abstract.md
14. gonzalez-baro-2001-gpat-topology-summary.md
15. hakim-2021-gpam-variant-liver-abstract.md
16. hakim-2021-gpam-variant-liver-fulltext.txt
17. hakim-2021-gpam-variant-liver-summary.md
18. hammond-2002-gpat1-knockout-abstract.md
19. hammond-2002-gpat1-knockout-summary.md
20. hammond-2005-gpat1-liver-acylcoa-abstract.md
21. hammond-2005-gpat1-liver-acylcoa-summary.md
22. jerkins-1995-gpat-promoter-abstract.md
23. jerkins-1995-gpat-promoter-summary.md
24. johnson-2023-gpat1-structure-abstract.md
25. johnson-2023-gpat1-structure-summary.md
26. lewin-1999-acyltransferase-motifs-abstract.md
27. lewin-1999-acyltransferase-motifs-summary.md
28. lewin-2001-gpat-feeding-regulation-abstract.md
29. lewin-2001-gpat-feeding-regulation-summary.md
30. lewin-2005-gpat1-hepatocytes-abstract.md
31. lewin-2005-gpat1-hepatocytes-summary.md
32. lewin-2008-gpat1-heart-abstract.md
33. lewin-2008-gpat1-heart-summary.md
34. linden-2006-gpat1-liver-overexpression-abstract.md
35. linden-2006-gpat1-liver-overexpression-summary.md
36. liu-2026-mongolian-horse-meat-abstract.md
37. liu-2026-mongolian-horse-meat-fulltext.txt
38. liu-2026-mongolian-horse-meat-summary.md
39. muoio-1999-ampk-gpat-abstract.md
40. muoio-1999-ampk-gpat-summary.md
41. neschen-2005-gpat1-ko-steatosis-abstract.md
42. neschen-2005-gpat1-ko-steatosis-summary.md
43. onorato-2005-gpat1-ck2-abstract.md
44. onorato-2005-gpat1-ck2-summary.md
45. park-2002-ampk-gpat-exercise-abstract.md
46. park-2002-ampk-gpat-exercise-summary.md
47. pellon-maison-2006-gpat1-cterminal-abstract.md
48. pellon-maison-2006-gpat1-cterminal-summary.md
49. pellon-maison-2009-macrobrachium-mtgpat-abstract.md
50. pellon-maison-2009-macrobrachium-mtgpat-summary.md
51. roy-2006-bovine-gpam-structure-abstract.md
52. roy-2006-bovine-gpam-structure-summary.md
53. uniprot-A0A9L0TCA8-entry.txt
54. uniprot-A0A9L0TCA8-summary.md
55. uniprot-A0A9L0TTC1-entry.txt
56. uniprot-A0A9L0TTC1-summary.md
57. uniprot-Q9HCL2-human-GPAT1-entry.txt
58. uniprot-Q9HCL2-human-GPAT1-summary.md
59. wade-2009-horse-genome-abstract.md
60. wade-2009-horse-genome-fulltext.txt
61. wade-2009-horse-genome-summary.md
62. wang-2007-gpat2-cloning-abstract.md
63. wang-2007-gpat2-cloning-summary.md
64. wendel-2009-gpat-review-abstract.md
65. wendel-2009-gpat-review-fulltext.txt
66. wendel-2009-gpat-review-summary.md
67. yazdi-2008-gpat1-highfat-abstract.md
68. yazdi-2008-gpat1-highfat-summary.md
69. yet-1993-mitochondrial-gpat-p90-abstract.md
70. yet-1993-mitochondrial-gpat-p90-summary.md
71. yet-1995-gpat-purification-abstract.md
72. yet-1995-gpat-purification-summary.md
73. yu-2017-bovine-gpam-abstract.md
74. yu-2017-bovine-gpam-summary.md
75. yu-2021-bovine-gpam-milk-abstract.md
76. yu-2021-bovine-gpam-milk-fulltext.txt
77. yu-2021-bovine-gpam-milk-summary.md