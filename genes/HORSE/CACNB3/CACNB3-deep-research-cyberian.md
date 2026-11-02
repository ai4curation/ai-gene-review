---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:59:37.387435'
end_time: '2026-10-26T02:07:46.078997'
duration_seconds: 488.69
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: CACNB3
  gene_symbol: CACNB3
  uniprot_accession: A0A5F5PZM5
  protein_description: 'RecName: Full=Voltage-dependent L-type calcium channel subunit
    beta-3 {ECO:0000256|ARBA:ARBA00019004}; AltName: Full=Calcium channel voltage-dependent
    subunit beta 3 {ECO:0000256|ARBA:ARBA00030522};'
  gene_info: Name=CACNB3 {ECO:0000313|VGNC:VGNC:15992};
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the calcium channel beta subunit family.
  protein_domains: CAB1-4_N_A-dom. (IPR046937); CACNB3_SH3. (IPR035760); GK/Ca_channel_bsu.
    (IPR008145); P-loop_NTPase. (IPR027417); SH3-like_dom_sf. (IPR036028)
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
citation_count: 58
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A5F5PZM5
- **Protein Description:** RecName: Full=Voltage-dependent L-type calcium channel subunit beta-3 {ECO:0000256|ARBA:ARBA00019004}; AltName: Full=Calcium channel voltage-dependent subunit beta 3 {ECO:0000256|ARBA:ARBA00030522};
- **Gene Information:** Name=CACNB3 {ECO:0000313|VGNC:VGNC:15992};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the calcium channel beta subunit family.
- **Key Domains:** CAB1-4_N_A-dom. (IPR046937); CACNB3_SH3. (IPR035760); GK/Ca_channel_bsu. (IPR008145); P-loop_NTPase. (IPR027417); SH3-like_dom_sf. (IPR036028)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CACNB3" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CACNB3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CACNB3** (gene ID: CACNB3, UniProt: A0A5F5PZM5) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# CACNB3 (Voltage-dependent L-type calcium channel subunit beta-3) in the horse, *Equus caballus* (UniProt A0A5F5PZM5)

## 1. Introduction and summary

CACNB3 encodes Cavβ3, one of four cytosolic auxiliary β subunits of high-voltage-activated (HVA) voltage-gated Ca2+ channels. The horse protein A0A5F5PZM5 is an unreviewed TrEMBL entry derived from the Thoroughbred genome assembly; it is annotated as "Voltage-dependent L-type calcium channel subunit beta-3", carries the gene name CACNB3 (VGNC:15992), and is assigned to the calcium channel β subunit family on the basis of automatic annotation [uniprot-A0A5F5PZM5-entry][wade-2009-horse-genome-abstract]. No published experimental study of horse CACNB3 was found: PubMed searches for CACNB3 combined with "horse" or "equine" returned no records. Its function therefore has to be inferred from orthologues. That inference is unusually well supported here. Outside its N-terminal segment, the horse sequence is almost identical to human CACNB3 (P54284): in our global alignment, 472 of the 484 human residues that align with the horse protein are identical. Every difference lies in the first ~40 residues of the horse model, which uses a different, longer N-terminal segment (517 aa compared with 484 aa) [alignment-horse-vs-human-CACNB3]. The SH3, HOOK and guanylate-kinase (GK) core, which carries the known functional determinants, is identical in the two species.

Cavβ3 has two kinds of function. In its canonical role it is a cytoplasmic subunit that binds the α-interaction domain (AID) in the I–II intracellular loop of a pore-forming Cavα1 subunit. Through this binding it promotes trafficking of the channel to the plasma membrane and changes its gating: it increases peak current, shifts the voltage dependence of activation and inactivation, and speeds activation and inactivation [castellano-1993-beta3-cloning-abstract][chen-2004-alpha1-beta-structure-abstract][buraei-2010-beta-subunit-review-abstract]. Knockout mice show that Cavβ3 is a major β subunit of neuronal N-type (Cav2.2) channels and of vascular smooth-muscle L-type (Cav1.2) channels [namkung-1998-beta3-knockout-neurons-abstract][murakami-2002-beta3-pain-abstract][murakami-2003-beta3-cardiovascular-abstract]. The second role is a non-canonical one specific to this β isoform. Independently of any channel, Cavβ3 binds the inositol 1,4,5-trisphosphate receptor (IP3R) and makes it less sensitive to low IP3 concentrations, which limits Ca2+ release from the endoplasmic reticulum. This brake has been demonstrated in pancreatic β-cells, fibroblasts and dendritic cells [berggren-2004-beta3-insulin-abstract][belkacemi-2018-beta3-ip3r-abstract][belkacemi-2022-beta3-ip3-specificity-abstract][becker-2021-beta3-beta-cells-fulltext][woo-2023-beta3-dendritic-cell-migration-fulltext]. Cavβ3 acts mainly in the cytoplasm, either at the inner face of the plasma membrane bound to Cavα1 or near ER Ca2+-release channels, and some evidence suggests it can also act in the nucleus [zhang-2010-beta3-pax6-abstract].

## 2. Identity, gene model and evolutionary conservation

The horse entry was produced by Ensembl gene annotation (ENSECAG00000012018; ENSECAP00000053855.2) of the EquCab genome assembly. Its functional, subunit and subcellular-location comments were propagated by UniProt's automatic rules (ARBA) [uniprot-A0A5F5PZM5-entry]. Its InterPro signatures place it unambiguously in the Cavβ family. These signatures include the Cavβ1–4 N-terminal A domain (IPR046937), a Cavβ3-specific SH3 domain (IPR035760), the guanylate kinase / Ca channel β subunit domain (IPR008145) within a P-loop NTPase-like fold (IPR027417), and the β3-specific signature VDCC_L_b3su (IPR008079) [uniprot-A0A5F5PZM5-entry]. The β3-specific SH3 and family signatures rule out confusion with CACNB1, CACNB2 or CACNB4, and no other gene uses the symbol CACNB3. The gene symbol, protein description, organism and domain architecture therefore all agree.

Human Cavβ3 was cloned from embryonic cDNA and mapped to chromosome 12q13. Its mRNA is found mainly in brain, smooth muscle and ovary, and it modulates VDCC activity when expressed in Xenopus oocytes [collin-1994-human-beta3-cloning-abstract]. Rat β3, cloned earlier, encodes a 484-residue protein expressed predominantly in brain [castellano-1993-beta3-cloning-abstract]. The near-identity of the horse core sequence to these orthologues means that structural and functional findings from rodents and humans can be transferred to the horse protein with high confidence [alignment-horse-vs-human-CACNB3]. The variable N-terminus of the horse model is consistent with the alternative N-terminal splice variants recorded for human CACNB3, which has five annotated isoforms [uniprot-P54284-human-CACNB3-entry]. The horse N-terminus has not been confirmed experimentally and could reflect a gene-model choice rather than a dominant transcript.

## 3. Molecular architecture: a MAGUK-like scaffold that binds the channel's AID

Cavβ proteins are modular. Each has a variable N-terminus, a conserved SH3 domain, a variable HOOK region, a conserved GK domain and a variable C-terminus, an arrangement that places them in the membrane-associated guanylate kinase (MAGUK) family [buraei-2010-beta-subunit-review-abstract]. Three crystallographic studies published in 2004 established how this scaffold engages the channel. Chen and colleagues solved the conserved core of β3 itself, alone and bound to the AID peptide. They showed that the SH3 and GK domains interact with each other and that the AID binds a hydrophobic groove in the GK domain through extensive contacts, which accounts for the very high α1–β affinity. They also showed that the previously proposed "β-interaction domain" holds the fold together but does not contact α1 directly [chen-2004-alpha1-beta-structure-abstract]. Van Petegem and colleagues, working with β2a, named the conserved hydrophobic cleft the α-binding pocket (ABP). They proposed that AID binding positions the β subunit close to the cytoplasmic end of pore-lining segment IS6, which would let β control gating directly [vanpetegem-2004-beta-aid-structure-abstract]. Opatowsky and colleagues showed that the AID becomes helical on binding and that, in Cavβ, the GK fold has lost its catalytic role and been reshaped into a protein-interaction module [opatowsky-2004-beta-core-structure-abstract].

Cavβ3 is therefore not an enzyme. Its GK domain is a non-catalytic protein-binding module, and the "P-loop NTPase" InterPro match reflects the ancestral fold, not ATPase or kinase activity [opatowsky-2004-beta-core-structure-abstract][uniprot-A0A5F5PZM5-entry]. Because the ABP residues are invariant between horse and human Cavβ3 [alignment-horse-vs-human-CACNB3], the horse protein is expected to bind Cavα1 AIDs in the same way. The full channel complex has since been resolved. Gao and colleagues determined cryo-EM structures of the human N-type channel assembled from Cav2.2 α1, α2δ-1 and β3, with and without the pore-blocking analgesic ziconotide. These structures show Cavβ3 as the cytoplasmic subunit of an intact Cav2.2 complex [gao-2021-cav22-cryoem-abstract]. They give direct structural support to the functional pairing of β3 with N-type channels described in Section 4.

## 4. Canonical function: trafficking and gating of high-voltage-activated Ca2+ channels

The β subunit is required for full functional expression of HVA channels. Part of the effect comes from channel trafficking. Bichet and colleagues showed that the α1 I–II loop carries an ER retention signal and that β binding overcomes it, allowing α1 to reach the plasma membrane [bichet-2000-beta-er-retention-abstract]. Reviews describe Cavβ as essential for surface expression and gating of HVA channels and as a site through which G proteins, protein kinases and RGK GTPases modulate the channel [buraei-2010-beta-subunit-review-abstract][dolphin-2012-auxiliary-subunits-review-abstract]. Specifically for β3, co-expression with a cardiac α1 (Cav1.2) in oocytes increased peak current, modulated the voltage dependence of activation and accelerated both activation and, at positive potentials, inactivation [castellano-1993-beta3-cloning-abstract]. UniProt summarises this for both human and horse as a regulatory subunit that increases CACNA1B and CACNA1C peak currents and shifts the voltage dependence of activation and inactivation. In the horse this annotation is an automatic transfer [uniprot-P54284-human-CACNB3-entry][uniprot-A0A5F5PZM5-entry].

Knockout mice show which channels depend on Cavβ3 in vivo. In sympathetic neurons from Cacnb3-null mice, N-type and L-type currents were reduced and the voltage dependence of P/Q-type channel activation was shifted [namkung-1998-beta3-knockout-neurons-abstract]. In dorsal root ganglion neurons, loss of β3 lowered Cav2.2 (α1B) protein and altered Ca2+ currents. The mice showed weaker inflammatory pain and reduced spinal wind-up, consistent with a preferential partnership between β3 and α1B in nociceptive neurons [murakami-2002-beta3-pain-abstract]. In aortic smooth muscle, loss of β3 reduced plasma-membrane L-type α1 and dihydropyridine binding sites, lowered current density by about 30% and slowed inactivation. On a high-salt diet the mice became hypertensive and developed aortic and cardiac hypertrophy [murakami-2003-beta3-cardiovascular-abstract]. In these cells, therefore, Cavβ3 sets how many functional channels reach the membrane as well as how they gate. The negative regulator BARP (CBARP) binds the ABP of every Cavβ isoform and competes with Cavα1. This suppresses channel activity and Ca2+-triggered exocytosis, so Cavβ3–α1 coupling can itself be regulated [beguin-2014-barp-abstract]. UniProt also lists this interaction for horse CACNB3 [uniprot-A0A5F5PZM5-entry]. The two other partners listed in the horse UniProt entry differ in how well they are supported. Binding to α2δ-4 (CACNA2D4) comes from co-expression experiments: α2δ-4 associated with Cav1.2 and β3 in HEK293 cells and increased Ca2+ influx through Cav1.2/β3 channels [qin-2002-alpha2delta4-cloning-abstract]. This is consistent with a complete α1–β3–α2δ assembly. Binding to Fas ligand (FASLG) rests on a phage-display screen of human SH3 domains against the proline-rich N-terminus of FasL. In that screen the CACNB3 SH3 domain was recovered as a single clone and was not validated in cells [voss-2009-fasl-sh3-interactors-fulltext]. This interaction should therefore be treated as speculative.

## 5. A β3-specific, channel-independent role: braking IP3 receptor-mediated Ca2+ release

The most distinctive function of Cavβ3 does not involve any Cav channel. In Cacnb3-null mouse β-cells, glucose-induced [Ca2+]i oscillations were faster and insulin secretion increased. Glucose tolerance improved, the change was traced to more IP3 formation and more Ca2+ mobilisation from intracellular stores, and L-type channel currents were unaffected [berggren-2004-beta3-insulin-abstract]. Belkacemi and colleagues then showed in fibroblasts that Cavβ3 reduces Ca2+ release after stimulation of PLC-coupled receptors. The effect persisted when receptor signalling was bypassed by photolysis of caged IP3, so it acts at or downstream of the IP3 receptor. It required the SH3–HOOK region of Cavβ3 and involved physical interaction with the IP3R. Without β3, fibroblasts migrated faster and skin wounds closed faster [belkacemi-2018-beta3-ip3r-abstract].

This role is specific to the β3 isoform. When each of the four Cavβ isoforms was expressed in COS-7 cells, which lack endogenous Cavβ, only Cavβ3 reduced ATP-induced store Ca2+ release [belkacemi-2022-beta3-ip3-specificity-abstract]. In the rat insulinoma β-cell line INS-1, CRISPR deletion of Cacnb3 left Cav currents unchanged. It did increase IP3-dependent Ca2+ release, Ca2+ oscillation frequency, CREB activity, MAFA protein and glucose-induced insulin secretion, and adding Cavβ3 back reversed these changes in a dose-dependent way [becker-2021-beta3-beta-cells-abstract]. In the same cells Cavβ3 co-immunoprecipitated with IP3R3 in both directions [becker-2021-beta3-beta-cells-fulltext]. In disease models, diabetic mouse islets over-expressed Cavβ3, and removing or knocking down Cacnb3 restored Ca2+ dynamics and insulin secretion, while over-expression in human islets impaired secretion [lee-2018-beta3-diabetes-abstract]. In migratory dendritic cells, Cacnb3 is a selective marker, and CACNB3 limits IP3R-mediated ER Ca2+ release after ATP stimulation without changing IP3 production, measured as IP1 [woo-2023-beta3-dendritic-cell-migration-fulltext]. CACNB3 was nevertheless needed for ATP-induced downregulation of CD11b and CD44, for cell detachment and for migration to lymph nodes, which shows that the brake shapes the Ca2+ signal rather than simply suppressing it [woo-2023-beta3-dendritic-cell-migration-fulltext]. Together these studies define a second molecular function for Cavβ3. It binds IP3R, most clearly shown for IP3R3, and raises the threshold for IP3-evoked Ca2+ release from the ER. This places it in the Gq/PLC → IP3 → IP3R signalling pathway as a negative regulator.

## 6. Other non-canonical activities: NMDA receptor signalling and nuclear transcriptional regulation

Two further channel-independent activities have been reported, each with less supporting evidence. Cacnb3-null mice learned hippocampus-dependent tasks better and showed larger NMDA receptor currents and NMDAR-dependent LTP, with a slight increase in NR2B. Hippocampal Ca2+ current density was unchanged, which suggests that Cavβ3 restrains NMDAR signalling by an unknown mechanism [jeon-2008-beta3-ltp-memory-abstract]. Separately, a primate-conserved Pax6 isoform, Pax6(S), binds Cavβ through its C-terminal "S tail". Cavβ3 suppressed Pax6(S) transcriptional activity and moved from the cytoplasm to the nucleus when Pax6(S) was present, which supports a role for Cavβ as a transcriptional regulator [zhang-2010-beta3-pax6-abstract][dolphin-2012-auxiliary-subunits-review-abstract]. Because Pax6(S) is highly conserved only in primates [zhang-2010-beta3-pax6-abstract], this interaction may not apply to the horse.

## 7. Subcellular localization and tissue context

Cavβ3 has no transmembrane segment and is cytoplasmic. Both the human and the horse UniProt entries give "Cytoplasm" as its location [uniprot-P54284-human-CACNB3-entry][uniprot-A0A5F5PZM5-entry]. In the human entry this location is supported by the Cav2.2–α2δ-1–β3 cryo-EM structure [uniprot-P54284-human-CACNB3-entry][gao-2021-cav22-cryoem-abstract]. When it acts as a channel subunit, it is held at the inner face of the plasma membrane by binding the Cavα1 AID [chen-2004-alpha1-beta-structure-abstract][bichet-2000-beta-er-retention-abstract]. These channel complexes sit in presynaptic terminals and cell bodies of neurons, including sympathetic and DRG neurons, and in the sarcolemma of vascular smooth muscle [namkung-1998-beta3-knockout-neurons-abstract][murakami-2002-beta3-pain-abstract][murakami-2003-beta3-cardiovascular-abstract]. When it acts as an IP3R brake, it must reach IP3 receptors in the ER membrane, as the co-immunoprecipitation results imply [becker-2021-beta3-beta-cells-fulltext][belkacemi-2018-beta3-ip3r-abstract]. In the presence of a suitable partner it can also enter the nucleus [zhang-2010-beta3-pax6-abstract]. Expression is highest in brain, including the hippocampus, and is also found in smooth muscle, ovary, pancreatic β-cells, fibroblasts and migratory dendritic cells [collin-1994-human-beta3-cloning-abstract][jeon-2008-beta3-ltp-memory-abstract][berggren-2004-beta3-insulin-abstract][woo-2023-beta3-dendritic-cell-migration-abstract]. No equine expression or localization data were found.

## 8. Implications for functional annotation of horse CACNB3

Orthology, sequence identity and conserved domains all support the following annotation of A0A5F5PZM5. The protein is an auxiliary, non-pore-forming, cytoplasmic subunit of the HVA voltage-gated Ca2+ channel complex. Its molecular function is binding the AID of Cav1.2 (L-type) and Cav2.2 (N-type) α1 subunits, and through that binding it enhances surface expression and modulates gating. In this sense it is a regulator of voltage-gated calcium channel activity, not a transporter in its own right. A second, isoform-specific function is binding the IP3 receptor and negatively regulating IP3-induced release of sequestered Ca2+ from the ER. All of this is inferred from orthologues and no experiment has been done in the horse. The IBA GO annotation "high voltage-gated calcium channel activity" (GO:0008331) on the horse entry [uniprot-A0A5F5PZM5-entry] is best read as membership of the channel complex rather than activity of Cavβ3 alone, since the pore is formed by α1. The biological processes best supported by experimental evidence in orthologues are regulation of calcium ion transport via voltage-gated channels (neuronal N-type and smooth-muscle L-type), negative regulation of IP3R-mediated store Ca2+ release, and the downstream physiology of insulin secretion, nociception, vascular tone and cell migration.

## Open Questions

No study has yet examined Cavβ3 in the horse. Transcript data from equine tissues, such as RNA-seq atlases from FAANG-type projects, would show which N-terminal exon is used. That would test whether the 517-residue Ensembl model, with its different first ~40 residues, is a real dominant isoform or an annotation artefact, and would establish the tissue distribution in the horse. The structural basis of the Cavβ3–IP3R interaction is still unknown. The SH3–HOOK region is required, but it is not known which IP3R isoform or region is contacted, how binding raises the IP3 threshold, or why Cavβ1, β2 and β4 lack the activity despite their similar cores. The mechanism behind the NMDAR phenotype is also unresolved, and it should be tested whether it, too, works through IP3R-dependent Ca2+ signalling. The balance between Cavβ3's role as a channel subunit and its role as an IP3R regulator in a given cell, for example how much Cavβ3 is free rather than bound to α1, has not been measured. Finally, Cavβ3 appears to be a druggable target in diabetes and inflammation in rodents. Whether CACNB3 variants affect equine traits such as metabolic syndrome or insulin dysregulation, exercise-related vascular physiology or pain, which are clinically important in horses, is unexplored and could be a useful line of follow-up.

## References

In the text, each citation key carries a suffix naming the file it rests on (`-abstract`, `-fulltext`, or a database entry). The keys below are the base names, and the matching files are in `citations/`.


* **[becker-2021-beta3-beta-cells]** Becker A, Wardas B, Salah H, Amini M, Fecher-Trost C, Sen Q, Martus D, Beck A, Philipp SE, Flockerzi V, Belkacemi A. (2021). Cavβ3 Regulates Ca2+ Signaling and Insulin Expression in Pancreatic β-Cells in a Cell-Autonomous Manner. *Diabetes* 70(11):2532-2544. PMID: 34426509; PMCID: PMC8564405; DOI: 10.2337/db21-0078. https://pubmed.ncbi.nlm.nih.gov/34426509/
* **[beguin-2014-barp]** Béguin P, Nagashima K, Mahalakshmi RN, Vigot R, Matsunaga A, Miki T, Ng MY, Ng YJ, Lim CH, Tay HS, Hwang LA, Firsov D, Tang BL, Inagaki N, Mori Y, Seino S, Launey T, Hunziker W. (2014). BARP suppresses voltage-gated calcium channel activity and Ca2+-evoked exocytosis. *The Journal of cell biology* 205(2):233-249. PMID: 24751537; PMCID: PMC4003244; DOI: 10.1083/jcb.201304101. https://pubmed.ncbi.nlm.nih.gov/24751537/
* **[belkacemi-2018-beta3-ip3r]** Belkacemi A, Hui X, Wardas B, Laschke MW, Wissenbach U, Menger MD, Lipp P, Beck A, Flockerzi V. (2018). IP3 Receptor-Dependent Cytoplasmic Ca2+ Signals Are Tightly Controlled by Cavβ3. *Cell reports* 22(5):1339-1349. PMID: 29386119; DOI: 10.1016/j.celrep.2018.01.010. https://pubmed.ncbi.nlm.nih.gov/29386119/
* **[belkacemi-2022-beta3-ip3-specificity]** Belkacemi A, Beck A, Wardas B, Weissgerber P, Flockerzi V. (2022). IP3-dependent Ca2+ signals are tightly controlled by Cavβ3, but not by Cavβ1, 2 and 4. *Cell calcium* 104:102573. PMID: 35366519; DOI: 10.1016/j.ceca.2022.102573. https://pubmed.ncbi.nlm.nih.gov/35366519/
* **[berggren-2004-beta3-insulin]** Berggren PO, Yang SN, Murakami M, Efanov AM, Uhles S, Köhler M, Moede T, Fernström A, Appelskog IB, Aspinwall CA, Zaitsev SV, Larsson O, de Vargas LM, Fecher-Trost C, Weissgerber P, Ludwig A, Leibiger B, Juntti-Berggren L, Barker CJ, Gromada J, Freichel M, Leibiger IB, Flockerzi V. (2004). Removal of Ca2+ channel beta3 subunit enhances Ca2+ oscillation frequency and insulin exocytosis. *Cell* 119(2):273-284. PMID: 15479643; DOI: 10.1016/j.cell.2004.09.033. https://pubmed.ncbi.nlm.nih.gov/15479643/
* **[bichet-2000-beta-er-retention]** Bichet D, Cornet V, Geib S, Carlier E, Volsen S, Hoshi T, Mori Y, De Waard M. (2000). The I-II loop of the Ca2+ channel alpha1 subunit contains an endoplasmic reticulum retention signal antagonized by the beta subunit. *Neuron* 25(1):177-190. PMID: 10707982; DOI: 10.1016/s0896-6273(00)80881-8. https://pubmed.ncbi.nlm.nih.gov/10707982/
* **[buraei-2010-beta-subunit-review]** Buraei Z, Yang J. (2010). The ß subunit of voltage-gated Ca2+ channels. *Physiological reviews* 90(4):1461-1506. PMID: 20959621; PMCID: PMC4353500; DOI: 10.1152/physrev.00057.2009. https://pubmed.ncbi.nlm.nih.gov/20959621/
* **[castellano-1993-beta3-cloning]** Castellano A, Wei X, Birnbaumer L, Perez-Reyes E. (1993). Cloning and expression of a third calcium channel beta subunit. *The Journal of biological chemistry* 268(5):3450-3455. PMID: 7679112; DOI: 10.1016/s0021-9258(18)53715-7. https://pubmed.ncbi.nlm.nih.gov/7679112/
* **[chen-2004-alpha1-beta-structure]** Chen YH, Li MH, Zhang Y, He LL, Yamada Y, Fitzmaurice A, Shen Y, Zhang H, Tong L, Yang J. (2004). Structural basis of the alpha1-beta subunit interaction of voltage-gated Ca2+ channels. *Nature* 429(6992):675-680. PMID: 15170217; DOI: 10.1038/nature02641. https://pubmed.ncbi.nlm.nih.gov/15170217/
* **[collin-1994-human-beta3-cloning]** Collin T, Lory P, Taviaux S, Courtieu C, Guilbault P, Berta P, Nargeot J. (1994). Cloning, chromosomal location and functional expression of the human voltage-dependent calcium-channel beta 3 subunit. *European journal of biochemistry* 220(1):257-262. PMID: 8119293; DOI: 10.1111/j.1432-1033.1994.tb18621.x. https://pubmed.ncbi.nlm.nih.gov/8119293/
* **[dolphin-2012-auxiliary-subunits-review]** Dolphin AC. (2012). Calcium channel auxiliary α2δ and β subunits: trafficking and one step beyond. *Nature reviews. Neuroscience* 13(8):542-555. PMID: 22805911; DOI: 10.1038/nrn3311. https://pubmed.ncbi.nlm.nih.gov/22805911/
* **[jeon-2008-beta3-ltp-memory]** Jeon D, Song I, Guido W, Kim K, Kim E, Oh U, Shin HS. (2008). Ablation of Ca2+ channel beta3 subunit leads to enhanced N-methyl-D-aspartate receptor-dependent long term potentiation and improved long term memory. *The Journal of biological chemistry* 283(18):12093-12101. PMID: 18339621; PMCID: PMC3774114; DOI: 10.1074/jbc.m800816200. https://pubmed.ncbi.nlm.nih.gov/18339621/
* **[lee-2018-beta3-diabetes]** Lee K, Kim J, Köhler M, Yu J, Shi Y, Yang SN, Ryu SH, Berggren PO. (2018). Blocking Ca2+ Channel β3 Subunit Reverses Diabetes. *Cell reports* 24(4):922-934. PMID: 30044988; PMCID: PMC6083041; DOI: 10.1016/j.celrep.2018.06.086. https://pubmed.ncbi.nlm.nih.gov/30044988/
* **[murakami-2002-beta3-pain]** Murakami M, Fleischmann B, De Felipe C, Freichel M, Trost C, Ludwig A, Wissenbach U, Schwegler H, Hofmann F, Hescheler J, Flockerzi V, Cavalié A. (2002). Pain perception in mice lacking the beta3 subunit of voltage-activated calcium channels. *The Journal of biological chemistry* 277(43):40342-40351. PMID: 12161429; DOI: 10.1074/jbc.m203425200. https://pubmed.ncbi.nlm.nih.gov/12161429/
* **[murakami-2003-beta3-cardiovascular]** Murakami M, Yamamura H, Suzuki T, Kang MG, Ohya S, Murakami A, Miyoshi I, Sasano H, Muraki K, Hano T, Kasai N, Nakayama S, Campbell KP, Flockerzi V, Imaizumi Y, Yanagisawa T, Iijima T. (2003). Modified cardiovascular L-type channels in mice lacking the voltage-dependent Ca2+ channel beta3 subunit. *The Journal of biological chemistry* 278(44):43261-43267. PMID: 12920136; DOI: 10.1074/jbc.m211380200. https://pubmed.ncbi.nlm.nih.gov/12920136/
* **[namkung-1998-beta3-knockout-neurons]** Namkung Y, Smith SM, Lee SB, Skrypnyk NV, Kim HL, Chin H, Scheller RH, Tsien RW, Shin HS. (1998). Targeted disruption of the Ca2+ channel beta3 subunit reduces N- and L-type Ca2+ channel activity and alters the voltage-dependent activation of P/Q-type Ca2+ channels in neurons. *Proceedings of the National Academy of Sciences of the United States of America* 95(20):12010-12015. PMID: 9751781; PMCID: PMC21756; DOI: 10.1073/pnas.95.20.12010. https://pubmed.ncbi.nlm.nih.gov/9751781/
* **[opatowsky-2004-beta-core-structure]** Opatowsky Y, Chen CC, Campbell KP, Hirsch JA. (2004). Structural analysis of the voltage-dependent calcium channel beta subunit functional core and its complex with the alpha 1 interaction domain. *Neuron* 42(3):387-399. PMID: 15134636; DOI: 10.1016/s0896-6273(04)00250-8. https://pubmed.ncbi.nlm.nih.gov/15134636/
* **[vanpetegem-2004-beta-aid-structure]** Van Petegem F, Clark KA, Chatelain FC, Minor DL. (2004). Structure of a complex between a voltage-gated calcium channel beta-subunit and an alpha-subunit domain. *Nature* 429(6992):671-675. PMID: 15141227; PMCID: PMC3076333; DOI: 10.1038/nature02588. https://pubmed.ncbi.nlm.nih.gov/15141227/
* **[wade-2009-horse-genome]** Wade CM, Giulotto E, Sigurdsson S, Zoli M, Gnerre S, Imsland F, Lear TL, Adelson DL, Bailey E, Bellone RR, Blöcker H, Distl O, Edgar RC, Garber M, Leeb T, Mauceli E, MacLeod JN, Penedo MC, Raison JM, Sharpe T, Vogel J, Andersson L, Antczak DF, Biagi T, Binns MM, Chowdhary BP, Coleman SJ, Della Valle G, Fryc S, Guérin G, Hasegawa T, Hill EW, Jurka J, Kiialainen A, Lindgren G, Liu J, Magnani E, Mickelson JR, Murray J, Nergadze SG, Onofrio R, Pedroni S, Piras MF, Raudsepp T, Rocchi M, Røed KH, Ryder OA, Searle S, Skow L, Swinburne JE, Syvänen AC, Tozaki T, Valberg SJ, Vaudin M, White JR, Zody MC, Broad Institute Genome Sequencing Platform, Broad Institute Whole Genome Assembly Team, Lander ES, Lindblad-Toh K. (2009). Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science (New York, N.Y.)* 326(5954):865-867. PMID: 19892987; PMCID: PMC3785132; DOI: 10.1126/science.1178158. https://pubmed.ncbi.nlm.nih.gov/19892987/
* **[woo-2023-beta3-dendritic-cell-migration]** Woo MS, Ufer F, Sonner JK, Belkacemi A, Tintelnot J, Sáez PJ, Krieg PF, Mayer C, Binkle-Ladisch L, Engler JB, Bauer S, Kursawe N, Vieira V, Mannebach S, Freichel M, Flockerzi V, Vargas P, Friese MA. (2023). Calcium channel β3 subunit regulates ATP-dependent migration of dendritic cells. *Science advances* 9(38):eadh1653. PMID: 37729408; PMCID: PMC10511199; DOI: 10.1126/sciadv.adh1653. https://pubmed.ncbi.nlm.nih.gov/37729408/
* **[zhang-2010-beta3-pax6]** Zhang Y, Yamada Y, Fan M, Bangaru SD, Lin B, Yang J. (2010). The beta subunit of voltage-gated Ca2+ channels interacts with and regulates the activity of a novel isoform of Pax6. *The Journal of biological chemistry* 285(4):2527-2536. PMID: 19917615; PMCID: PMC2807309; DOI: 10.1074/jbc.m109.022236. https://pubmed.ncbi.nlm.nih.gov/19917615/
* **[gao-2021-cav22-cryoem]** Gao S, Yao X, Yan N. (2021). Structure of human Cav2.2 channel blocked by the painkiller ziconotide. *Nature* 596(7870):143-147. PMID: 34234349; PMCID: PMC8529174; DOI: 10.1038/s41586-021-03699-6. https://pubmed.ncbi.nlm.nih.gov/34234349/
* **[qin-2002-alpha2delta4-cloning]** Qin N, Yagel S, Momplaisir ML, Codd EE, D'Andrea MR. (2002). Molecular cloning and characterization of the human voltage-gated calcium channel alpha(2)delta-4 subunit. *Molecular pharmacology* 62(3):485-496. PMID: 12181424; DOI: 10.1124/mol.62.3.485. https://pubmed.ncbi.nlm.nih.gov/12181424/
* **[voss-2009-fasl-sh3-interactors]** Voss M, Lettau M, Janssen O. (2009). Identification of SH3 domain interaction partners of human FasL (CD178) by phage display screening. *BMC immunology* 10:53. PMID: 19807924; PMCID: PMC2763855; DOI: 10.1186/1471-2172-10-53. https://pubmed.ncbi.nlm.nih.gov/19807924/
* **[uniprot-A0A5F5PZM5-entry]** UniProtKB/TrEMBL entry A0A5F5PZM5_HORSE (entry version 26, 02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A5F5PZM5.txt
* **[uniprot-P54284-human-CACNB3-entry]** UniProtKB/Swiss-Prot entry P54284 (CACB3_HUMAN). https://rest.uniprot.org/uniprotkb/P54284.txt
* **[alignment-horse-vs-human-CACNB3]** Global pairwise alignment (Biopython PairwiseAligner, BLOSUM62, gap open -10/extend -0.5) of A0A5F5PZM5 vs P54284, generated in this study; file citations/alignment-horse-vs-human-CACNB3.txt.


## Citations

1. alignment-horse-vs-human-CACNB3.txt
2. becker-2021-beta3-beta-cells-abstract.md
3. becker-2021-beta3-beta-cells-fulltext.txt
4. becker-2021-beta3-beta-cells-summary.md
5. beguin-2014-barp-abstract.md
6. beguin-2014-barp-fulltext.txt
7. beguin-2014-barp-summary.md
8. belkacemi-2018-beta3-ip3r-abstract.md
9. belkacemi-2018-beta3-ip3r-summary.md
10. belkacemi-2022-beta3-ip3-specificity-abstract.md
11. belkacemi-2022-beta3-ip3-specificity-summary.md
12. berggren-2004-beta3-insulin-abstract.md
13. berggren-2004-beta3-insulin-summary.md
14. bichet-2000-beta-er-retention-abstract.md
15. bichet-2000-beta-er-retention-summary.md
16. buraei-2010-beta-subunit-review-abstract.md
17. buraei-2010-beta-subunit-review-summary.md
18. castellano-1993-beta3-cloning-abstract.md
19. castellano-1993-beta3-cloning-summary.md
20. chen-2004-alpha1-beta-structure-abstract.md
21. chen-2004-alpha1-beta-structure-summary.md
22. collin-1994-human-beta3-cloning-abstract.md
23. collin-1994-human-beta3-cloning-summary.md
24. dolphin-2012-auxiliary-subunits-review-abstract.md
25. dolphin-2012-auxiliary-subunits-review-summary.md
26. gao-2021-cav22-cryoem-abstract.md
27. gao-2021-cav22-cryoem-summary.md
28. jeon-2008-beta3-ltp-memory-abstract.md
29. jeon-2008-beta3-ltp-memory-summary.md
30. lee-2018-beta3-diabetes-abstract.md
31. lee-2018-beta3-diabetes-fulltext.txt
32. lee-2018-beta3-diabetes-summary.md
33. murakami-2002-beta3-pain-abstract.md
34. murakami-2002-beta3-pain-summary.md
35. murakami-2003-beta3-cardiovascular-abstract.md
36. murakami-2003-beta3-cardiovascular-summary.md
37. namkung-1998-beta3-knockout-neurons-abstract.md
38. namkung-1998-beta3-knockout-neurons-summary.md
39. opatowsky-2004-beta-core-structure-abstract.md
40. opatowsky-2004-beta-core-structure-summary.md
41. qin-2002-alpha2delta4-cloning-abstract.md
42. qin-2002-alpha2delta4-cloning-summary.md
43. uniprot-A0A5F5PZM5-entry.txt
44. uniprot-A0A5F5PZM5.fasta
45. uniprot-P54284-human-CACNB3-entry.txt
46. uniprot-P54284-human-CACNB3.fasta
47. vanpetegem-2004-beta-aid-structure-abstract.md
48. vanpetegem-2004-beta-aid-structure-summary.md
49. voss-2009-fasl-sh3-interactors-abstract.md
50. voss-2009-fasl-sh3-interactors-fulltext.txt
51. voss-2009-fasl-sh3-interactors-summary.md
52. wade-2009-horse-genome-abstract.md
53. wade-2009-horse-genome-summary.md
54. woo-2023-beta3-dendritic-cell-migration-abstract.md
55. woo-2023-beta3-dendritic-cell-migration-fulltext.txt
56. woo-2023-beta3-dendritic-cell-migration-summary.md
57. zhang-2010-beta3-pax6-abstract.md
58. zhang-2010-beta3-pax6-summary.md