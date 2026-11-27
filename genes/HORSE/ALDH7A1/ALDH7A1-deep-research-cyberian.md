---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:47:29.855537'
end_time: '2026-10-26T01:59:34.386130'
duration_seconds: 724.53
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: ALDH7A1
  gene_symbol: ALDH7A1
  uniprot_accession: A0A9L0RRL6
  protein_description: 'RecName: Full=Alpha-aminoadipic semialdehyde dehydrogenase
    {ECO:0000256|ARBA:ARBA00070398}; EC=1.2.1.3 {ECO:0000256|ARBA:ARBA00024226}; EC=1.2.1.31
    {ECO:0000256|ARBA:ARBA00013073}; EC=1.2.1.8 {ECO:0000256|ARBA:ARBA00066671}; AltName:
    Full=Aldehyde dehydrogenase family 7 member A1 {ECO:0000256|ARBA:ARBA00081296};
    AltName: Full=Antiquitin-1 {ECO:0000256|ARBA:ARBA00080350}; AltName: Full=Betaine
    aldehyde dehydrogenase {ECO:0000256|ARBA:ARBA00077960}; AltName: Full=Delta1-piperideine-6-carboxylate
    dehydrogenase {ECO:0000256|ARBA:ARBA00081730};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the aldehyde dehydrogenase family.
  protein_domains: Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_CS_GLU.
    (IPR029510); Ald_DH_N. (IPR016162); Aldehyde_DH_dom. (IPR015590)
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
citation_count: 57
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0RRL6
- **Protein Description:** RecName: Full=Alpha-aminoadipic semialdehyde dehydrogenase {ECO:0000256|ARBA:ARBA00070398}; EC=1.2.1.3 {ECO:0000256|ARBA:ARBA00024226}; EC=1.2.1.31 {ECO:0000256|ARBA:ARBA00013073}; EC=1.2.1.8 {ECO:0000256|ARBA:ARBA00066671}; AltName: Full=Aldehyde dehydrogenase family 7 member A1 {ECO:0000256|ARBA:ARBA00081296}; AltName: Full=Antiquitin-1 {ECO:0000256|ARBA:ARBA00080350}; AltName: Full=Betaine aldehyde dehydrogenase {ECO:0000256|ARBA:ARBA00077960}; AltName: Full=Delta1-piperideine-6-carboxylate dehydrogenase {ECO:0000256|ARBA:ARBA00081730};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the aldehyde dehydrogenase family.
- **Key Domains:** Ald_DH/histidinol_DH. (IPR016161); Ald_DH_C. (IPR016163); Ald_DH_CS_GLU. (IPR029510); Ald_DH_N. (IPR016162); Aldehyde_DH_dom. (IPR015590)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ALDH7A1" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ALDH7A1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ALDH7A1** (gene ID: ALDH7A1, UniProt: A0A9L0RRL6) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ALDH7A1 (antiquitin; α-aminoadipic semialdehyde dehydrogenase) in the horse, *Equus caballus* (UniProt A0A9L0RRL6)

## 1. Introduction and summary

The horse protein A0A9L0RRL6 is the equine ortholog of aldehyde dehydrogenase 7A1 (ALDH7A1), also called antiquitin. Its main job is the NAD⁺-dependent oxidation of L-α-aminoadipic semialdehyde (α-AASA, (S)-2-amino-6-oxohexanoate) to L-2-aminoadipate. This is the last step that the saccharopine and pipecolate routes of lysine catabolism share [mills-2006-antiquitin-pde-abstract][pena-2017-mouse-lysine-saccharopine-abstract]. In solution α-AASA sits in equilibrium with its cyclic Schiff base, Δ1-piperideine-6-carboxylate (P6C). The enzyme is therefore also called the P6C/α-AASA dehydrogenase. Its physiological importance is clearest from human genetics: loss-of-function mutations cause pyridoxine-dependent epilepsy (PDE), in which accumulating P6C inactivates pyridoxal 5′-phosphate [mills-2006-antiquitin-pde-abstract][mills-2010-pde-spectrum-fulltext]. Mammalian ALDH7A1 also oxidises betaine aldehyde to the osmolyte glycine betaine (EC 1.2.1.8). It oxidises a range of lipid-peroxidation-derived aldehydes too, including hexanal, nonanal, 4-hydroxy-2-nonenal and malondialdehyde (EC 1.2.1.3). Through these activities it protects cells against hyperosmotic and oxidative stress [brocker-2010-aldh7a1-hyperosmotic-abstract][brocker-2011-aldh7a1-reactive-aldehyde-fulltext]. ALDH7A1 is one of 19 human members of the ancient ALDH superfamily, whose enzymes detoxify endogenous and exogenous aldehydes and make molecules such as retinoic acid, betaine and GABA [jackson-2011-aldh-superfamily-update-abstract]. The protein is unusual among ALDHs because it works in several compartments: mitochondria, the cytosol and the nucleus [brocker-2010-aldh7a1-hyperosmotic-abstract]. More recent work adds an AMPK-regulated pool on membranes. There the NADH it produces inhibits COPI vesicle fission during energy stress and supplies the ferroptosis suppressor FSP1 [yang-2019-aldh7a1-copi-energy-fulltext][yang-2025-aldh7a1-ferroptosis-fulltext].

No experimental study of ALDH7A1 in the horse was found. PubMed searches for "ALDH7A1 AND (horse OR equine OR equus)" and "antiquitin AND (horse OR equine)" returned no records. The horse UniProt record is an unreviewed, Ensembl-derived model. All of its functional annotations come from automatic rule-based (ARBA) transfer [uniprot-A0A9L0RRL6-entry]. The functional account below is therefore an inference by orthology from the human enzyme and other mammals. That inference rests on very high sequence identity and on complete conservation of every catalytically and structurally critical residue examined (Section 2). Where possible, the report separates direct experimental evidence (human or mouse) from what is inferred for the horse protein.

## 2. Identity of the target and conservation with characterised orthologs

The target record describes a 521-residue protein from the Thoroughbred reference genome [wade-2009-horse-genome-abstract]. It is encoded on horse chromosome 14 by Ensembl gene ENSECAG00000010547 (transcript ENSECAT00000119202). The record is named "alpha-aminoadipic semialdehyde dehydrogenase" and carries a Pfam Aldedh (PF00171) domain spanning residues 64–502. It also has a PROSITE ALDH glutamate active-site signature, the PANTHER subfamily PTHR43521:SF1 and the CDD family cd07130 (ALDH_F7_AASADH) [uniprot-A0A9L0RRL6-entry]. These family assignments match the domain list in the request (IPR016161/IPR016162/IPR016163/IPR015590/IPR029510) and place the protein specifically in ALDH family 7. The gene symbol ALDH7A1 therefore points to the correct protein; there is no ambiguity with another gene. Ensembl gives the gene the VGNC-approved symbol ALDH7A1 (VGNC:15239).

To test orthology directly, I aligned the horse sequence globally against reviewed human ALDH7A1 (P49419, 539 residues) using BLOSUM62 (notes/alignment-horse-vs-human-ALDH7A1.txt). Of the 521 aligned positions, 498 are identical (95.6%). Two residue-numbering schemes are in use for human ALDH7A1, and they differ by 28 residues [laciak-2020-glu427-fulltext]. The crystallographic literature uses a numbering in which the catalytic nucleophile is Cys302 [luo-2015-aldh7a1-substrate-structure-fulltext]. UniProt and clinical nomenclature use the full-length isoform-1 numbering, in which the same residue is Cys330 and the general base is Glu296 [uniprot-P49419-entry]. In the horse sequence the nucleophile maps to Cys312 and the general base to Glu278, which UniProt also flags as the active site [uniprot-A0A9L0RRL6-entry]. Several other functionally defined residues are also conserved. These are the PDE-hotspot residue Glu427 (Glu399 in structure numbering; horse Glu409), which binds the NAD⁺ nicotinamide ribose [laciak-2020-glu427-fulltext], and the substrate-site residues Glu121, Asn167 and Ala171 (structure numbering; horse Glu131, Asn177, Ala181) [laciak-2020-pde-mutations-structure-fulltext]. The C-terminal gating residues Ala505 and Gln506 (horse Ala515 and Gln516) are conserved as well [korasick-2017-aldh7a1-cterminus-fulltext]. So is the AMPK phosphorylation site, Ser102 in the numbering of Yang et al. and Ser130 in UniProt (horse Ser112) [yang-2025-aldh7a1-ferroptosis-fulltext][uniprot-P49419-entry].

The horse model differs from human in two ways that matter for annotation. First, it lacks an 18-residue segment corresponding to human residues 65–82 (VITTYCPANNEPIARVRQ), at the N-terminal edge of the catalytic core. The horse gene encodes several protein models, and comparing them shows that this gap belongs to the target model specifically, not to the horse protein in general. UniProt holds five unreviewed horse entries linked to the same Ensembl gene: A0A9L0R3Y5 (566 residues), A0A5F5PY19 and A0A9L0RA17 (552 each), A0A9L0RRL6 (521, the target) and F7CZV6 (502) [uniprot-horse-ALDH7A1-all-isoforms]. Aligned to human ALDH7A1, every one except A0A9L0RRL6 contains the segment VITTYCPANNEPIARVRQ, identical to human, and all are 93–96% identical overall (notes/horse-isoforms-vs-human.txt). The target therefore stands for an Ensembl transcript that skips a short in-frame coding segment, about 54 nucleotides. It is not the canonical form of horse ALDH7A1. A systematic survey of human ALDH splice variants found no well-supported alternative transcripts for ALDH7A1 under its criteria [black-2009-aldh-splice-variants-fulltext]. So an isoform lacking this segment has no known counterpart in humans, and it may be a minor or computationally predicted transcript. It is unknown whether such a protein would fold, tetramerise or show activity. Its catalytic residues are all present, so the functional annotation below applies most securely to the full-length horse ALDH7A1 that this gene encodes. Second, the N-terminal ~26 residues, which in human form a predicted mitochondrial transit peptide [uniprot-P49419-entry], differ more from human than the rest of the protein does. They nevertheless keep a similar amphipathic, Arg-rich composition (MWRVGRQLCVQAAGGIRLSGLWNRPA). The horse record carries the keyword "Transit peptide" by automatic annotation [uniprot-A0A9L0RRL6-entry]. The protein has been detected in horse proteomic data, recorded in PeptideAtlas [uniprot-A0A9L0RRL6-entry].

## 3. Catalytic function and substrate specificity

The defining reaction, inferred for the horse enzyme, is (S)-2-amino-6-oxohexanoate + NAD⁺ + H₂O → L-2-aminoadipate + NADH + 2 H⁺ (EC 1.2.1.31; Rhea:12308) [uniprot-A0A9L0RRL6-entry]. The physiological identity of this activity was established for human antiquitin by Mills and colleagues. Patients with pyridoxine-dependent seizures carry ALDH7A1 mutations that abolish the P6C/α-AASA dehydrogenase activity [mills-2006-antiquitin-pde-abstract]. A larger clinical series later confirmed that antiquitin catalyses the NAD-dependent dehydrogenation of L-α-AASA/L-P6C [mills-2010-pde-spectrum-fulltext]. Kinetic work on purified recombinant human enzyme gives a kcat of about 0.30 s⁻¹, a Km for α-AASA of 64 μM and a kcat/Km of about 4700 M⁻¹ s⁻¹. These values are within a factor of three of other reports [korasick-2017-aldh7a1-cterminus-fulltext]. Coulter-Mackie and colleagues confirmed the importance of this activity independently. They built an assay that uses enzymatically generated α-AASA as the substrate. With it they showed that twelve disease-associated missense variants, all expressed stably in *E. coli*, lacked α-AASA dehydrogenase activity [coultermackie-2012-antiquitin-missense-abstract].

Despite its role in lysine catabolism, ALDH7A1 has fairly broad substrate specificity. Brocker et al. purified recombinant human ALDH7A1 and showed that it efficiently oxidises betaine aldehyde, the osmolyte precursor. It also oxidises lipid-peroxidation-derived aliphatic aldehydes as well as α-AASA [brocker-2010-aldh7a1-hyperosmotic-abstract]. A follow-up study showed that the enzyme metabolises 4-hydroxy-2-nonenal (4HNE). The same study showed that recombinant ALDH7A1 is sensitive to oxidation and that activity is partly restored by thiol reducing agents, consistent with a redox-sensitive catalytic cysteine [brocker-2011-aldh7a1-reactive-aldehyde-fulltext]. Yang et al. extended this to malondialdehyde and 4-HNE in the context of ferroptosis [yang-2025-aldh7a1-ferroptosis-fulltext]. UniProt accordingly lists separate Rhea reactions for hexanal, octanal, nonanal, (E)-non-2-enal, 4-HNE, malondialdehyde and betaine aldehyde. In the horse record all of these are propagated by ARBA rules [uniprot-P49419-entry][uniprot-A0A9L0RRL6-entry]. NAD⁺ is the cofactor, consistent with the GO term "L-aminoadipate-semialdehyde dehydrogenase [NAD(P)+] activity". The horse residues that line the NAD⁺ site (for example the Glu427/Glu399 equivalent) are conserved.

The reaction follows the canonical ALDH mechanism. The catalytic cysteine attacks the aldehyde carbonyl to form a thiohemiacetal. Hydride is transferred to NAD⁺ to give a thioester, which a glutamate-activated water molecule then hydrolyses [luo-2015-aldh7a1-substrate-structure-fulltext]. Chemical evidence for the essential cysteine comes from 4-diethylaminobenzaldehyde (DEAB), which inactivates ALDH7A1 covalently and irreversibly by forming a stable adduct with that residue [luo-2015-deab-inactivator-abstract].

## 4. Structural basis of substrate recognition and oligomeric regulation

Crystal structures of human ALDH7A1 explain why the enzyme prefers α-AASA. In the complex with the product α-aminoadipate, the ε-carboxylate occupies the oxyanion hole and hydrogen-bonds to the backbone of Cys302. The aliphatic chain packs into an "aromatic box", and the distal α-amino/α-carboxylate end is anchored by electrostatic interactions with five conserved residues. The binding mode resembles that of glutamate in the proline-catabolic enzyme ALDH4A1 [luo-2015-aldh7a1-substrate-structure-fulltext]. Mutational and structural analysis of PDE variants in this pocket showed that Glu121 ion-pairs with the substrate amino group. The A171V variant, which disrupts this pairing, reduces catalytic efficiency about 2000-fold. N167S and W175G cause milder defects by misaligning the substrate [laciak-2020-pde-mutations-structure-fulltext]. All of these residues are identical in the horse protein (Section 2), so the substrate pocket, and hence the substrate specificity, is expected to be conserved.

ALDH7A1 works as a dimer of dimers, and its active site is put together dynamically. When product binds, the C-terminus moves about 16 Å into the active site of the neighbouring protomer and stabilises the aldehyde "anchor loop". In apo structures the C-terminus and anchor loop are disordered, which suggests that the active site is disassembled when the aldehyde site is empty [luo-2015-aldh7a1-substrate-structure-fulltext]. In the closed state, Ala505 and Gln506 contact the anchor loop of the neighbouring subunit. Mutating these residues, or truncating the C-terminus, raises the Km for α-AASA sharply and impairs tetramerisation [korasick-2017-aldh7a1-cterminus-fulltext]. Cofactor binding regulates this as well. NAD⁺ shifts the dimer–tetramer equilibrium toward the tetramer at concentrations used in assays, which suggests that the active tetramer is assembled "on demand" [korasick-2018-nad-tetramer-fulltext]. Pathogenic substitutions at Glu427 both prevent the nicotinamide from adopting the catalytic pose and reduce the fraction of active tetramer [laciak-2020-glu427-fulltext]. The horse record's "homotetramer" annotation [uniprot-A0A9L0RRL6-entry] is consistent with this, and the C-terminal gate residues are conserved.

## 5. Pathways: lysine catabolism, betaine synthesis and aldehyde detoxification

ALDH7A1 sits at a junction in lysine degradation. In mammals lysine is catabolised by the saccharopine pathway, mainly in liver and kidney, and the pipecolate pathway, thought to matter in brain. Both converge on α-AASA/P6C, which ALDH7A1 oxidises to α-aminoadipate [pena-2017-mouse-lysine-saccharopine-abstract]. Isotope tracing in mice with ε-¹⁵N- and α-¹⁵N-lysine indicated that most α-AASA/P6C and aminoadipate arise through the hepatic and renal saccharopine pathway. Cerebral pipecolate did not appear to be oxidised further to AASA [pena-2017-mouse-lysine-saccharopine-abstract]. The consequence of losing the enzyme is a metabolic block. Aldh7a1-knockout mice accumulate P6C, α-AASA and pipecolic acid in brain and liver, as patients do. On a high-lysine, low-pyridoxine diet they develop seizures and die quickly, and pyridoxine rescues them [alshekaili-2020-mouse-model-pde-abstract]. The pathogenic mechanism is chemical: P6C condenses with PLP in a Knoevenagel reaction, depleting the cofactor needed by PLP-dependent enzymes of neurotransmitter metabolism [mills-2006-antiquitin-pde-abstract].

The second pathway role is the final step of glycine betaine synthesis from choline, betaine aldehyde → betaine (UniProt pathway "betaine biosynthesis via choline pathway; step 1/1") [uniprot-A0A9L0RRL6-entry]. Brocker et al. showed that expressing human ALDH7A1 in Chinese hamster ovary cells reduced apoptosis caused by high extracellular NaCl or sucrose. They proposed that ALDH7A1 protects by generating osmolytes and removing toxic aldehydes [brocker-2010-aldh7a1-hyperosmotic-abstract]. This matches the function of the plant ortholog ALDH7B1 (the pea "26g turgor protein"), which is induced by dehydration and salinity. The conservation between plant and animal proteins gave antiquitin its name [lee-1994-antiquitin-pea-abstract][brocker-2010-aldh7a1-hyperosmotic-abstract]. The third role is detoxifying reactive aldehydes from lipid peroxidation. CHO cells expressing mitochondrial or cytosolic ALDH7A1 better survive hexanal, 4HNE and H₂O₂ [brocker-2011-aldh7a1-reactive-aldehyde-fulltext].

## 6. Subcellular localisation and stress-regulated membrane functions

ALDH7A1 is found in several compartments. In mouse tissues the protein is in the cytosol, nucleus and mitochondria, which Brocker et al. called unique among ALDH enzymes. They also detected mitochondrial and cytosolic transcripts, expressed differently across tissues [brocker-2010-aldh7a1-hyperosmotic-abstract]. In human, isoform 1 carries a predicted N-terminal mitochondrial transit peptide (residues 1–26). Isoform 2 lacks residues 1–28 and corresponds to the cytosolic form [uniprot-P49419-entry]. Protein levels are highest in mouse liver, kidney and brain, followed by pancreas and testis [brocker-2010-aldh7a1-hyperosmotic-abstract]. Early mRNA studies likewise found the highest levels in rat kidney and liver [lee-1994-antiquitin-pea-abstract]. The horse model includes an N-terminal extension resembling a transit peptide. Its automatic annotations (mitochondrion, cytosol, nucleus, plasma membrane, Golgi membrane) are transferred from the human data [uniprot-A0A9L0RRL6-entry]. No localisation data exist for horse tissues.

Two recent studies from the Hsu laboratory define a regulated membrane pool of ALDH7A1. Here what matters is the NADH product rather than the carboxylic acid. During hypoxia or starvation, NADH generated by ALDH7A1 targets BARS to inhibit COPI vesicle fission. This broadly slows intracellular transport (ER–Golgi, Golgi–plasma membrane and endocytic routes) and saves cellular energy [yang-2019-aldh7a1-copi-energy-fulltext]. Under ferroptotic stress, a fall in ATP activates AMPK, which phosphorylates ALDH7A1 at Ser102 (Ser130 in UniProt numbering). This moves ALDH7A1 to the plasma membrane, ER, Golgi and lipid droplets. There it produces a membrane-associated NADH pool that FSP1 uses as cofactor, it stabilises FSP1 on membranes, and it directly consumes 4-HNE and malondialdehyde [yang-2025-aldh7a1-ferroptosis-fulltext]. UniProt attributes these membrane functions to the cytosolic isoform 2 [uniprot-P49419-entry]. The phosphoserine and surrounding sequence (QVLGSLVSLE) are identical in horse, so this regulation may be conserved, but it is untested.

## 7. Implications for the horse and annotation recommendations

From orthology, the best-supported annotation for A0A9L0RRL6 is NAD⁺-dependent L-aminoadipate-semialdehyde dehydrogenase activity (EC 1.2.1.31), acting in L-lysine catabolism to aminoadipate. Betaine-aldehyde dehydrogenase activity (EC 1.2.1.8) and broad aldehyde dehydrogenase (NAD⁺) activity toward medium-chain and lipid-peroxidation aldehydes (EC 1.2.1.3) are well-supported secondary activities. All rest on experiments with the human enzyme [brocker-2010-aldh7a1-hyperosmotic-abstract][brocker-2011-aldh7a1-reactive-aldehyde-fulltext][mills-2006-antiquitin-pde-abstract]. Mitochondrial matrix, cytosol and nucleus are the best-supported locations. Membrane association (plasma membrane, Golgi) is a regulated, stress-induced state, so it is better treated as conditional than as constitutive [brocker-2010-aldh7a1-hyperosmotic-abstract][yang-2025-aldh7a1-ferroptosis-fulltext]. Physiologically, horse diets can be high in lysine, and in human and mouse ALDH7A1 deficiency is a dietary-lysine-sensitive, pyridoxine-responsive epilepsy [alshekaili-2020-mouse-model-pde-abstract]. ALDH7A1 is therefore a reasonable candidate gene for any pyridoxine-responsive neonatal seizure phenotype in foals, though no such association has been reported. The annotations for ferroptosis suppression and COPI inhibition rest on cell-line studies in human cells [yang-2019-aldh7a1-copi-energy-fulltext][yang-2025-aldh7a1-ferroptosis-fulltext]. They should be treated as more provisional than the core enzymatic function.

## Open Questions

Several points need follow-up. The most immediate is the horse gene model. The other four horse protein models from the same gene contain the 18-residue segment that A0A9L0RRL6 lacks (human residues 65–82). It remains unclear whether the shorter transcript is supported by horse RNA-seq reads that span the splice junction, or whether it is a computational artefact. This matters because the segment lies at the N-terminal edge of the catalytic domain, and no equivalent human isoform has been described [black-2009-aldh-splice-variants-fulltext]. A related question is which horse start codon is used. The 552- and 566-residue models begin with an upstream extension (MGCPGRGAGLYF…) ahead of the MWR… start that matches human isoform 1, and this extension would change any prediction of mitochondrial targeting. ALDH7A1 also has a history of pseudogenes and retroduplication in primates [jackson-2011-aldh-superfamily-update-fulltext], so it would help to check whether the horse genome carries processed ALDH7A1 copies that could confuse expression or proteomic assignments. It would also help to establish whether horse makes both the mitochondrial (transit-peptide-containing) and cytosolic isoforms, and in which tissues, as Brocker et al. showed for mouse.

Beyond the gene model, horse ALDH7A1 has never been characterised biochemically. Expressing it recombinantly and measuring kinetics with α-AASA/P6C, betaine aldehyde and 4-HNE would turn the orthology-based annotation into direct evidence. Horse-specific physiology raises further questions: lysine flux through the saccharopine pathway in a hindgut-fermenting herbivore, betaine synthesis in kidney during the dehydration and osmotic stress of exercise, and the relative importance of ALDH7A1 against other betaine aldehyde dehydrogenases (such as ALDH9A1) in equine tissues. Whether AMPK-dependent membrane recruitment and the FSP1-NADH ferroptosis axis work in non-human species is unknown. Finally, screening equine genomes for ALDH7A1 loss-of-function variants, and testing foals with idiopathic neonatal seizures for urinary α-AASA, could show whether a PDE-like disorder exists in horses.

## References

- [mills-2006-antiquitin-pde] Mills PB, Struys E, Jakobs C, Plecko B, Baxter P, Baumgartner M, Willemsen MA, Omran H, Tacke U, Uhlenberg B, et al. Mutations in antiquitin in individuals with pyridoxine-dependent seizures. *Nat Med* 2006;12:307–309. PMID: 16491085. DOI: 10.1038/nm1366.
- [mills-2010-pde-spectrum] Mills PB, Footitt EJ, Mills KA, et al. Genotypic and phenotypic spectrum of pyridoxine-dependent epilepsy (ALDH7A1 deficiency). *Brain* 2010;133:2148–2159. PMID: 20554659. PMCID: PMC2892945. DOI: 10.1093/brain/awq143.
- [brocker-2010-aldh7a1-hyperosmotic] Brocker C, Lassen N, Estey T, Pappa A, Cantore M, Orlova VV, Chavakis T, Kavanagh KL, Oppermann U, Vasiliou V. Aldehyde dehydrogenase 7A1 (ALDH7A1) is a novel enzyme involved in cellular defense against hyperosmotic stress. *J Biol Chem* 2010. PMID: 20207735. PMCID: PMC2881771. DOI: 10.1074/jbc.M109.077925.
- [brocker-2011-aldh7a1-reactive-aldehyde] Brocker C, et al. Aldehyde dehydrogenase 7A1 (ALDH7A1) attenuates reactive aldehyde and oxidative stress induced cytotoxicity. *Chem Biol Interact* 2011. PMID: 21338592. PMCID: PMC3387551. DOI: 10.1016/j.cbi.2011.02.016.
- [luo-2015-aldh7a1-substrate-structure] Luo M, Tanner JJ. Structural basis of substrate recognition by aldehyde dehydrogenase 7A1. *Biochemistry* 2015;54:5513–5522. PMID: 26260980. PMCID: PMC4565128. DOI: 10.1021/acs.biochem.5b00754.
- [luo-2015-deab-inactivator] Luo M, Gates KS, Henzl MT, Tanner JJ. Diethylaminobenzaldehyde is a covalent, irreversible inactivator of ALDH7A1. *ACS Chem Biol* 2015. PMID: 25554827. DOI: 10.1021/cb500977q.
- [korasick-2017-aldh7a1-cterminus] Korasick DA, Wyatt JW, Luo M, Laciak AR, Ruddraraju K, Gates KS, Henzl MT, Tanner JJ. Importance of the C-terminus of aldehyde dehydrogenase 7A1 for oligomerization and catalytic activity. *Biochemistry* 2017. PMID: 29045138. PMCID: PMC5928510. DOI: 10.1021/acs.biochem.7b00803.
- [korasick-2018-nad-tetramer] Korasick DA, White TA, Chakravarthy S, Tanner JJ. NAD⁺ promotes assembly of the active tetramer of aldehyde dehydrogenase 7A1. *FEBS Lett* 2018. PMID: 30184263. PMCID: PMC6188814. DOI: 10.1002/1873-3468.13238.
- [laciak-2020-pde-mutations-structure] Laciak AR, Korasick DA, Wyatt JW, Gates KS, Tanner JJ. Structural and biochemical consequences of pyridoxine-dependent epilepsy mutations that target the aldehyde binding site of aldehyde dehydrogenase ALDH7A1. *FEBS J* 2020. PMID: 31302938. PMCID: PMC6944758. DOI: 10.1111/febs.14997.
- [laciak-2020-glu427] Laciak AR, Korasick DA, Gates KS, Tanner JJ. Structural analysis of pathogenic mutations targeting Glu427 of ALDH7A1, the hot spot residue of pyridoxine-dependent epilepsy. *J Inherit Metab Dis* 2020;43:635–644. PMID: 31652343. PMCID: PMC7182499. DOI: 10.1002/jimd.12184.
- [yang-2019-aldh7a1-copi-energy] Yang JS, Hsu JW, Park SY, Lee SY, Li J, Bai M, Alves C, Tseng W, Michelet X, Ho IC, Hsu VW. ALDH7A1 inhibits the intracellular transport pathways during hypoxia and starvation to promote cellular energy homeostasis. *Nat Commun* 2019. PMID: 31492851. PMCID: PMC6731274. DOI: 10.1038/s41467-019-11932-0.
- [yang-2025-aldh7a1-ferroptosis] Yang JS, Morris AJ, Kamizaki K, Chen J, Stark J, Oldham WM, Nakamura T, Mishima E, Loscalzo J, Minami Y, Conrad M, et al. ALDH7A1 protects against ferroptosis by generating membrane NADH and regulating FSP1. *Cell* 2025. PMID: 40233740. PMCID: PMC12085291. DOI: 10.1016/j.cell.2025.03.019.
- [alshekaili-2020-mouse-model-pde] Al-Shekaili HH, et al. A novel mouse model for pyridoxine-dependent epilepsy due to antiquitin deficiency. *Hum Mol Genet* 2020. PMID: 32969477. PMCID: PMC7689292. DOI: 10.1093/hmg/ddaa202.
- [pena-2017-mouse-lysine-saccharopine] Pena IA, et al. Mouse lysine catabolism to aminoadipate occurs primarily through the saccharopine pathway; implications for pyridoxine dependent epilepsy (PDE). *Biochim Biophys Acta Mol Basis Dis* 2017. PMID: 27615426. DOI: 10.1016/j.bbadis.2016.09.006.
- [lee-1994-antiquitin-pea] Lee P, et al. Homology between a human protein and a protein of the green garden pea. *Genomics* 1994. PMID: 8088832. DOI: 10.1006/geno.1994.1279.
- [wade-2009-horse-genome] Wade CM, Giulotto E, Sigurdsson S, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science* 2009;326:865–867. PMID: 19892987. PMCID: PMC3785132. DOI: 10.1126/science.1178158.
- [coultermackie-2012-antiquitin-missense] Coulter-Mackie MB, Li A, Lian Q, Struys E, Stockler S, Waters PJ. Overexpression of human antiquitin in E. coli: enzymatic characterization of twelve ALDH7A1 missense mutations associated with pyridoxine-dependent epilepsy. *Mol Genet Metab* 2012. PMID: 22784480. DOI: 10.1016/j.ymgme.2012.06.008.
- [jackson-2011-aldh-superfamily-update] Jackson B, Brocker C, Thompson DC, Black W, Vasiliou K, Nebert DW, Vasiliou V. Update on the aldehyde dehydrogenase gene (ALDH) superfamily. *Hum Genomics* 2011. PMID: 21712190. PMCID: PMC3392178. DOI: 10.1186/1479-7364-5-4-283.
- [black-2009-aldh-splice-variants] Black WJ, Stagos D, Marchitti SA, Nebert DW, Tipton KF, Bairoch A, Vasiliou V. Human aldehyde dehydrogenase genes: alternatively spliced transcriptional variants and their suggested nomenclature. *Pharmacogenet Genomics* 2009. PMID: 19823103. PMCID: PMC3356695. DOI: 10.1097/FPC.0b013e3283329023.
- [uniprot-horse-ALDH7A1-all-isoforms] UniProtKB entries for horse Ensembl gene ENSECAG00000010547 (A0A9L0R3Y5, A0A5F5PY19, A0A9L0RA17, A0A9L0RRL6, F7CZV6). https://rest.uniprot.org/uniprotkb/stream?query=xref:ensembl-ENSECAG00000010547&format=fasta
- [uniprot-A0A9L0RRL6-entry] UniProtKB/TrEMBL A0A9L0RRL6 (A0A9L0RRL6_HORSE), entry version 15 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0RRL6.txt
- [uniprot-P49419-entry] UniProtKB/Swiss-Prot P49419 (AL7A1_HUMAN). https://rest.uniprot.org/uniprotkb/P49419.txt


## Citations

1. alshekaili-2020-mouse-model-pde-abstract.md
2. alshekaili-2020-mouse-model-pde-summary.md
3. black-2009-aldh-splice-variants-abstract.md
4. black-2009-aldh-splice-variants-fulltext.txt
5. black-2009-aldh-splice-variants-summary.md
6. brocker-2010-aldh7a1-hyperosmotic-abstract.md
7. brocker-2010-aldh7a1-hyperosmotic-summary.md
8. brocker-2011-aldh7a1-reactive-aldehyde-abstract.md
9. brocker-2011-aldh7a1-reactive-aldehyde-fulltext.txt
10. brocker-2011-aldh7a1-reactive-aldehyde-summary.md
11. coultermackie-2012-antiquitin-missense-abstract.md
12. coultermackie-2012-antiquitin-missense-summary.md
13. jackson-2011-aldh-superfamily-update-abstract.md
14. jackson-2011-aldh-superfamily-update-fulltext.txt
15. jackson-2011-aldh-superfamily-update-summary.md
16. korasick-2017-aldh7a1-cterminus-abstract.md
17. korasick-2017-aldh7a1-cterminus-fulltext.txt
18. korasick-2017-aldh7a1-cterminus-summary.md
19. korasick-2018-nad-tetramer-abstract.md
20. korasick-2018-nad-tetramer-fulltext.txt
21. korasick-2018-nad-tetramer-summary.md
22. laciak-2020-glu427-abstract.md
23. laciak-2020-glu427-fulltext.txt
24. laciak-2020-glu427-summary.md
25. laciak-2020-pde-mutations-structure-abstract.md
26. laciak-2020-pde-mutations-structure-fulltext.txt
27. laciak-2020-pde-mutations-structure-summary.md
28. lee-1994-antiquitin-pea-abstract.md
29. lee-1994-antiquitin-pea-summary.md
30. luo-2015-aldh7a1-substrate-structure-abstract.md
31. luo-2015-aldh7a1-substrate-structure-fulltext.txt
32. luo-2015-aldh7a1-substrate-structure-summary.md
33. luo-2015-deab-inactivator-abstract.md
34. luo-2015-deab-inactivator-summary.md
35. mills-2006-antiquitin-pde-abstract.md
36. mills-2006-antiquitin-pde-summary.md
37. mills-2010-pde-spectrum-abstract.md
38. mills-2010-pde-spectrum-fulltext.txt
39. mills-2010-pde-spectrum-summary.md
40. pena-2017-mouse-lysine-saccharopine-abstract.md
41. pena-2017-mouse-lysine-saccharopine-summary.md
42. uniprot-A0A9L0RRL6-entry-summary.md
43. uniprot-A0A9L0RRL6-entry.txt
44. uniprot-A0A9L0RRL6.fasta
45. uniprot-P49419-entry-summary.md
46. uniprot-P49419-entry.txt
47. uniprot-P49419.fasta
48. uniprot-horse-ALDH7A1-all-isoforms-summary.md
49. uniprot-horse-ALDH7A1-all-isoforms.fasta
50. wade-2009-horse-genome-abstract.md
51. wade-2009-horse-genome-summary.md
52. yang-2019-aldh7a1-copi-energy-abstract.md
53. yang-2019-aldh7a1-copi-energy-fulltext.txt
54. yang-2019-aldh7a1-copi-energy-summary.md
55. yang-2025-aldh7a1-ferroptosis-abstract.md
56. yang-2025-aldh7a1-ferroptosis-fulltext.txt
57. yang-2025-aldh7a1-ferroptosis-summary.md