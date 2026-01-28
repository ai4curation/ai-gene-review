---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-01-24T00:55:07.694196'
end_time: '2026-01-24T01:08:48.818855'
duration_seconds: 821.12
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ATP5MC3
  gene_symbol: ATP5MC3
  uniprot_accession: P48201
  protein_description: 'RecName: Full=ATP synthase F(0) complex subunit C3, mitochondrial
    {ECO:0000305}; AltName: Full=ATP synthase lipid-binding protein; AltName: Full=ATP
    synthase membrane subunit c locus 3 {ECO:0000312|HGNC:HGNC:843}; AltName: Full=ATP
    synthase proteolipid P3; AltName: Full=ATP synthase proton-transporting mitochondrial
    F(0) complex subunit C3; AltName: Full=ATPase protein 9; AltName: Full=ATPase
    subunit c; Flags: Precursor;'
  gene_info: Name=ATP5MC3 {ECO:0000312|HGNC:HGNC:843}; Synonyms=ATP5G3 {ECO:0000312|HGNC:HGNC:843};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the ATPase C chain family. .
  protein_domains: ATP_synth_F0_csu. (IPR000454); ATP_synth_F0_csu_DDCD_BS. (IPR020537);
    ATP_synth_F0_csu_sf. (IPR038662); ATPase_proteolipid_c-like_dom. (IPR002379);
    F/V-ATP_Csub_sf. (IPR035921)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 19
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P48201
- **Protein Description:** RecName: Full=ATP synthase F(0) complex subunit C3, mitochondrial {ECO:0000305}; AltName: Full=ATP synthase lipid-binding protein; AltName: Full=ATP synthase membrane subunit c locus 3 {ECO:0000312|HGNC:HGNC:843}; AltName: Full=ATP synthase proteolipid P3; AltName: Full=ATP synthase proton-transporting mitochondrial F(0) complex subunit C3; AltName: Full=ATPase protein 9; AltName: Full=ATPase subunit c; Flags: Precursor;
- **Gene Information:** Name=ATP5MC3 {ECO:0000312|HGNC:HGNC:843}; Synonyms=ATP5G3 {ECO:0000312|HGNC:HGNC:843};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the ATPase C chain family. .
- **Key Domains:** ATP_synth_F0_csu. (IPR000454); ATP_synth_F0_csu_DDCD_BS. (IPR020537); ATP_synth_F0_csu_sf. (IPR038662); ATPase_proteolipid_c-like_dom. (IPR002379); F/V-ATP_Csub_sf. (IPR035921)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ATP5MC3" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ATP5MC3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ATP5MC3** (gene ID: ATP5MC3, UniProt: P48201) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ATP5MC3: ATP Synthase F(0) Complex Subunit C3

## Introduction and Summary

ATP5MC3 (formerly ATP5G3) encodes one of three isoforms of the c-subunit of mitochondrial ATP synthase, the enzyme responsible for generating the majority of cellular ATP through oxidative phosphorylation. The gene is located on human chromosome 2 and encodes a precursor protein of 142 amino acids that includes a mitochondrial targeting sequence [yan-1994-atp5g3-cloning-abstract]. Remarkably, despite only 80% nucleotide identity in the coding region compared to ATP5MC1 (ATP5G1) and ATP5MC2 (ATP5G2), all three genes encode an identical 75-amino-acid mature protein after cleavage of their distinct leader peptides [yan-1994-atp5g3-cloning-abstract]. The conservation of the "RFS" motif in the leader peptide is critical for mitochondrial import and maturation.

The c-subunit is a small, extremely hydrophobic protein that oligomerizes to form the c-ring, a central component of the membrane-embedded F0 sector of ATP synthase. In mammals, the c-ring consists of eight identical c-subunits arranged in a ring that spans the inner mitochondrial membrane [pinke-2020-mammalian-atp-synthase-abstract]. This c-ring functions as the rotor of the ATP synthase molecular motor, coupling the flow of protons across the inner mitochondrial membrane to the mechanical rotation that drives ATP synthesis in the F1 catalytic domain [kuhlbrandt-2019-atp-synthase-review-abstract].

## Structure of the ATP Synthase Complex

Mitochondrial F1F0-ATP synthase is a ~600 kDa multi-subunit complex consisting of two functional domains: the membrane-embedded F0 sector and the hydrophilic F1 catalytic sector that protrudes into the mitochondrial matrix [kuhlbrandt-2019-atp-synthase-review-abstract]. The F0 sector contains the c-ring rotor along with subunit a (the stator) and accessory subunits e, f, and g. The F1 sector contains the catalytic subunits alpha and beta arranged in an alternating (αβ)3 hexamer, along with the central stalk subunits gamma (γ), delta (δ), and epsilon (ε) [ruhle-2015-assembly-abstract].

Recent cryo-electron microscopy structures have provided unprecedented insight into the architecture of mammalian ATP synthase. Pinke et al. determined the structure of ovine ATP synthase at atomic resolution, revealing that subunits in the F0 membrane domain are organized into a "proton translocation cluster" attached to the c-ring and a more distant "hook apparatus" containing subunit e [pinke-2020-mammalian-atp-synthase-abstract]. A particularly unexpected finding was that subunit e anchors a lipid "plug" that caps the central pore of the c-ring, potentially serving as a gating mechanism.

The c-subunit itself has two transmembrane helices connected by a short polar loop. Each subunit contains a conserved glutamate residue (E61 in humans, equivalent to E59 in E. coli) located near the center of the membrane, which serves as the proton-binding site essential for the rotary mechanism [blanc-2024-c-ring-rotation-abstract]. This glutamate undergoes protonation and deprotonation cycles as the c-ring rotates past the interface with subunit a.

## The c-Ring and Proton Translocation Mechanism

The c-ring is the central element of the F0 rotor that couples proton translocation to ATP synthesis. During ATP synthesis, protons flow down their electrochemical gradient from the intermembrane space to the matrix through two half-channels in subunit a, driving the rotation of the c-ring [kuhlbrandt-2019-atp-synthase-review-abstract]. Each elementary rotation step of 36° (corresponding to one c-subunit) is coupled to the translocation of one proton.

Blanc and Hummer performed multi-microsecond atomistic molecular dynamics simulations to elucidate the mechanism of proton-powered c-ring rotation [blanc-2024-c-ring-rotation-abstract]. Their work revealed that rotation proceeds by dynamic sliding of the ring over the a-subunit surface, during which interactions with conserved polar residues stabilize distinct intermediates. The essential arginine residue (R239) of the a-subunit plays a critical role in preventing proton leak by separating the two half-channels and creating a ~6 Å barrier. After proton transfer to the c-ring glutamate, this arginine stabilizes the rotated configuration through a salt bridge with the now-deprotonated glutamate of the trailing c-subunit.

The proton transfer itself occurs through a Grotthuss-type mechanism via ordered water chains that form at specific rotational positions [blanc-2024-c-ring-rotation-abstract]. The simulations identified a metastable intermediate state (termed P2, corresponding to cryo-EM structures) where water wires of three molecules optimally connect the proton donor (aE288) and acceptor (cE111) residues. After proton transfer, a high energetic barrier prevents backward rotation while a free energy drop favors forward rotation, ensuring the directionality required for ATP synthesis.

The stoichiometry of the c-ring varies among species (8-17 subunits), which directly determines the bioenergetic cost of ATP synthesis by setting the H+/ATP ratio [nesci-2015-c-ring-review-abstract]. Mammalian ATP synthase contains 8 c-subunits, meaning that 8 protons must translocate for each complete rotation of the c-ring, which synthesizes 3 ATP molecules (one at each catalytic site in F1).

## Isoform-Specific Considerations: ATP5MC1, ATP5MC2, and ATP5MC3

A distinctive feature of the c-subunit in mammals is that it is encoded by three nuclear genes: ATP5MC1 (chromosome 17), ATP5MC2 (chromosome 12), and ATP5MC3 (chromosome 2) [yan-1994-atp5g3-cloning-abstract]. All three genes encode precursor proteins with distinct mitochondrial targeting sequences (presequences) but identical 75-amino-acid mature proteins. This redundancy in the genome with identical mature products raises interesting questions about tissue-specific expression, regulation, and potential functional implications.

The presequences of the three isoforms differ significantly, with ATP5MC3 (P3) showing only 80% DNA sequence identity to ATP5MC1 (P1) and ATP5MC2 (P2) in the mature peptide-encoding region despite encoding the same protein [yan-1994-atp5g3-cloning-abstract]. Each presequence contains the conserved "RFS" motif essential for mitochondrial import and processing by mitochondrial processing peptidases. The existence of multiple genes encoding the same mature protein may provide robustness to the assembly of the c-ring or allow for differential regulation in different tissues or under different metabolic conditions.

Analysis of tissue-specific expression data from the Human Protein Atlas reveals that ATP5MC3 is classified as "tissue enhanced" with preferential expression in heart muscle and tongue. The highest RNA expression levels are observed in heart muscle (1149 nTPM), tongue (1015 nTPM), and skeletal muscle (728 nTPM), consistent with the high energy demands of these contractile tissues [human-protein-atlas-atp5mc3]. Moderate expression is found in metabolically active tissues including parathyroid gland, kidney, liver, and gastrointestinal tract. In the brain, ATP5MC3 shows low regional specificity with relatively uniform distribution across brain regions, with the choroid plexus showing the highest expression among neural tissues. At the single-cell level, parietal cells in the stomach display notably high expression, reflecting their intensive ATP requirements for acid secretion. The gene is evolutionarily conserved, with 221 organisms having orthologs of human ATP5MC3, including all major vertebrate lineages from fish to primates [genecards-atp5mc3].

He et al. demonstrated that cells lacking all three c-subunit genes (ATP5G1, ATP5G2, and ATP5G3) can still assemble a vestigial ATP synthase complex containing the F1 catalytic domain and peripheral stalk but lacking the membrane-embedded c-ring [he-2017-ptp-without-c-subunit-abstract]. This finding confirms that the three genes are the sole sources of c-subunit in human cells and that none contain cryptic alternative forms.

## Subcellular Localization

The c-subunit is synthesized in the cytoplasm as a precursor protein containing an N-terminal mitochondrial targeting sequence. Upon import into mitochondria, the presequence is cleaved by mitochondrial processing peptidases to generate the mature 75-amino-acid c-subunit. The mature protein is extremely hydrophobic and inserts into the inner mitochondrial membrane, where it oligomerizes to form the c-ring.

Within the inner mitochondrial membrane, the c-ring is specifically localized to cristae, the invaginations that increase membrane surface area and house the respiratory chain complexes and ATP synthase [kuhlbrandt-2019-atp-synthase-review-abstract]. ATP synthase dimers and higher-order oligomers are preferentially located at the curved edges of cristae, where they contribute to shaping membrane curvature. This organization optimizes the efficiency of oxidative phosphorylation by localizing the proton gradient and ATP synthesis machinery.

Gene Ontology annotations for ATP5MC3 (UniProtKB:P48201) confirm its molecular functions, biological processes, and cellular localization. The protein is annotated with proton transmembrane transporter activity (GO:0015078) and lipid binding (GO:0008289), consistent with its role in the membrane-embedded c-ring and its interactions with the surrounding lipid bilayer. Physical interaction evidence (IPI) also supports protein binding activity (GO:0005515), reflecting the subunit's assembly into the multi-protein ATP synthase complex. For biological processes, ATP5MC3 participates in proton motive force-driven ATP synthesis (GO:0015986) and proton transmembrane transport (GO:1902600). The cellular component annotations confirm localization to the mitochondrial inner membrane (GO:0005743) and the proton-transporting ATP synthase complex (GO:0045259).

## Post-Translational Modifications

The c-subunit undergoes a functionally significant post-translational modification: trimethylation of lysine 43. Chen et al. first demonstrated that lysine 43, located in the polar loop linking the two transmembrane α-helices, is invariably trimethylated in bovine ATP synthase subunit c [chen-2004-trimethyllysine-abstract]. This modification adds 42 Da to the molecular mass and is conserved throughout vertebrate sequences. Importantly, the same trimethylation was found in subunit c isolated from lysosomal storage bodies in Batten disease, demonstrating that this modification is not an aberrant phenomenon associated with disease pathology but rather a normal post-translational modification that occurs during or after mitochondrial import.

The enzyme responsible for this modification was subsequently identified as FAM173B, a mitochondrial methyltransferase that localizes to mitochondria via an atypical, non-cleavable targeting sequence [chen-2019-fam173b-methyltransferase-abstract]. CRISPR/Cas9-mediated knockout of FAM173B in mammalian cells completely abrogated Lys-43 trimethylation. The functional consequences of losing this modification are significant: cells lacking ATPSc methylation show improper incorporation of subunit c into ATP synthase complexes, reduced mitochondrial ATP synthesis capacity, and decreased oxygen consumption rates. The modification appears to be ubiquitous among metazoans, and the C. elegans orthologue of FAM173B can restore methylation in knockout cells, demonstrating evolutionary conservation of this regulatory mechanism. Based on its enzymatic function, researchers have proposed renaming FAM173B to ATPSc-KMT (ATP synthase c-subunit Lysine Methyltransferase).

The precise mechanism by which Lys-43 trimethylation enhances ATP synthase function remains incompletely understood. The modified residue is positioned at the beginning of the C-terminal α-helix, in the lipid head-group region of the membrane. This location suggests the modification may affect protein-lipid interactions or the stability of the c-ring assembly. Notably, this modification is specific to higher organisms and is not conserved in all ATP synthases, indicating that its role in enzyme assembly and function may have evolved in metazoans.

## Role in Disease

### Mitochondrial Diseases and Movement Disorders

Pathogenic variants in ATP5MC3 have recently been identified as causes of neurological disease. Zech et al. reported three patients with de novo heterozygous missense variants in ATP5MC3 (p.Gly79Val and p.Asn106Lys) that caused variable neurological phenotypes including dystonia, developmental delay, intellectual disability, and hyperlactatemia [zech-2022-atp-synthase-variants-abstract]. Functional studies in patient fibroblasts demonstrated diminished ATPase activity and defective ATP synthase assembly.

Neilson et al. described a large family with autosomal dominant spastic paraplegia and dystonia caused by the ATP5MC3 c.318C>G (p.Asn106Lys) variant [neilson-2021-atp5mc3-dystonia-abstract]. Patient fibroblast studies showed impaired complex V activity, reduced ATP generation, and decreased oxygen consumption. Studies in Drosophila carrying orthologous mutations confirmed reduced mobility and impaired mitochondrial function, validating the pathogenicity of these variants.

### Neuronal Ceroid Lipofuscinoses (Batten Disease)

The c-subunit has long been recognized as the major component of the storage material that accumulates in lysosomes in several forms of neuronal ceroid lipofuscinoses (NCLs), a group of fatal inherited neurodegenerative disorders also known as Batten disease [ezaki-1995-ncl-subunit-c-abstract]. Ezaki et al. demonstrated that in late infantile NCL, the degradation of subunit c is markedly delayed, leading to its accumulation first in mitochondria and subsequently in lysosomes through autophagic processes.

Palmer et al. noted that subunit c accumulation is a defining feature of multiple NCL forms and is associated with defects in intracellular vesicle trafficking and lysosomal function [palmer-2013-ncl-mechanisms-abstract]. The extreme hydrophobicity of the c-subunit, which is an adaptation for its function in the lipid bilayer, may make it particularly resistant to lysosomal proteases when misdirected to lysosomes.

### Mitochondrial Permeability Transition and Cell Death

A major area of ongoing research and controversy concerns the potential role of the c-ring in forming the mitochondrial permeability transition pore (mPTP), a non-selective channel that opens in response to calcium overload and causes cell death. Several lines of evidence support a role for the c-ring in mPT:

Mnatsakanyan et al. demonstrated that purified human c-ring forms a large multi-conductance (~1.5 nS), voltage-gated ion channel when reconstituted in lipid bilayers [mnatsakanyan-2022-c-ring-leak-channel-abstract]. Addition of the purified F1 subcomplex inhibited channel activity, suggesting that F1 acts as a gate. During excitotoxic neuronal death, F1 dissociated from F0, and this dissociation was prevented by cyclosporin A, a well-known inhibitor of mPT. Knockdown of c-subunit genes eliminated high-conductance mPT-like channel activity.

Bonora et al. showed that ATP synthase dimers dissociate during mPT induction and that mutations in the c-subunit that alter c-ring conformation sensitize cells to mPT [bonora-2017-mpt-c-ring-abstract]. Stabilizing ATP synthase dimers through genetic approaches inhibited mPT.

Pinke et al. observed that calcium exposure of ATP synthase caused retraction of subunit e and disassembly of the c-ring in cryo-EM structures, leading them to propose that subunit e pulls the lipid plug out of the c-ring to enable pore opening [pinke-2020-mammalian-atp-synthase-abstract].

However, important counter-evidence challenges the c-ring hypothesis. He et al. generated cells lacking all three c-subunit genes and found that these cells retained characteristic mPT properties, indicating that the c-subunit is not essential for pore formation [he-2017-ptp-without-c-subunit-abstract]. Zhou et al. used molecular dynamics simulations to argue that the biophysical properties of a correctly assembled c-ring are inconsistent with those attributed to the mPTP [zhou-2017-c-ring-not-mpt-abstract].

## Open Questions

Several important questions remain regarding ATP5MC3 and the c-subunit:

1. **Isoform-specific regulation**: Although all three c-subunit genes encode identical mature proteins, what determines the differential tissue expression patterns observed (e.g., ATP5MC3 being enhanced in heart and tongue)? Are there specific transcription factors or regulatory elements that control expression of each isoform, and does this have functional consequences for mitochondrial bioenergetics in different tissues?

2. **mPT mechanism**: The role of the c-ring in forming the mitochondrial permeability transition pore remains controversial. How can the conflicting evidence from c-subunit knockout studies (where mPT persists) and purified c-ring electrophysiology (where c-ring forms a large channel) be reconciled? Does the c-ring contribute to mPT under some conditions but not others?

3. **Disease mechanisms**: For the pathogenic ATP5MC3 variants causing dystonia and spastic paraplegia (p.Gly79Val, p.Asn106Lys), what is the precise molecular mechanism? Do missense mutations affect c-ring assembly, rotation efficiency, proton translocation, or interactions with other ATP synthase subunits? Why do these mutations preferentially affect the nervous system?

4. **Trimethylation function**: What is the precise molecular mechanism by which Lys-43 trimethylation enhances ATP synthase function? Does the modification affect c-ring stability, assembly kinetics, lipid interactions, or the proton translocation mechanism? Why is this modification specific to metazoans?

5. **Storage material in NCL**: Why is subunit c particularly prone to lysosomal accumulation in certain NCL forms? Is this related to its extreme hydrophobicity, its trimethylation status, or specific recognition by autophagy receptors? Can interventions targeting its degradation be therapeutically beneficial?

6. **Therapeutic targeting**: Given the essential role of c-subunit in ATP synthesis and potential role in cell death, can the c-ring be therapeutically targeted to modulate mPT in ischemia-reperfusion injury or neurodegeneration without compromising normal ATP production?

## References

1. **yan-1994-atp5g3-cloning**: Yan WL, Lerner TJ, Haines JL, Gusella JF. Sequence analysis and mapping of a novel human mitochondrial ATP synthase subunit 9 cDNA (ATP5G3). Genomics. 1994;24(2):375-7. PMID: 7698763. [DOI: 10.1006/geno.1994.1631](https://doi.org/10.1006/geno.1994.1631)

2. **zech-2022-atp-synthase-variants**: Zech M, Kopajtich R, Steinbrücker K, et al. Variants in Mitochondrial ATP Synthase Cause Variable Neurologic Phenotypes. Ann Neurol. 2022;91(2):225-237. PMID: 34954817. [DOI: 10.1002/ana.26293](https://doi.org/10.1002/ana.26293)

3. **neilson-2021-atp5mc3-dystonia**: Neilson DE, Zech M, Hufnagel RB, et al. A Novel Variant of ATP5MC3 Associated with Both Dystonia and Spastic Paraplegia. Mov Disord. 2021;37(2):375-383. PMID: 34636445. [DOI: 10.1002/mds.28821](https://doi.org/10.1002/mds.28821)

4. **kuhlbrandt-2019-atp-synthase-review**: Kühlbrandt W. Structure and Mechanisms of F-Type ATP Synthases. Annu Rev Biochem. 2019;88:515-549. PMID: 30901262. [DOI: 10.1146/annurev-biochem-013118-110903](https://doi.org/10.1146/annurev-biochem-013118-110903)

5. **mnatsakanyan-2022-c-ring-leak-channel**: Mnatsakanyan N, Park HA, Wu J, et al. Mitochondrial ATP synthase c-subunit leak channel triggers cell death upon loss of its F1 subcomplex. Cell Death Differ. 2022;29(9):1874-1887. PMID: 35322203. [DOI: 10.1038/s41418-022-00972-7](https://doi.org/10.1038/s41418-022-00972-7)

6. **blanc-2024-c-ring-rotation**: Blanc FEC, Hummer G. Mechanism of proton-powered c-ring rotation in a mitochondrial ATP synthase. Proc Natl Acad Sci USA. 2024;121(11):e2314199121. PMID: 38451940. [DOI: 10.1073/pnas.2314199121](https://doi.org/10.1073/pnas.2314199121)

7. **bonora-2017-mpt-c-ring**: Bonora M, Morganti C, Morciano G, et al. Mitochondrial permeability transition involves dissociation of F1F0 ATP synthase dimers and C-ring conformation. EMBO Rep. 2017;18(7):1077-1089. PMID: 28566520. [DOI: 10.15252/embr.201643602](https://doi.org/10.15252/embr.201643602)

8. **he-2017-ptp-without-c-subunit**: He J, Ford HC, Carroll J, et al. Persistence of the mitochondrial permeability transition in the absence of subunit c of human ATP synthase. Proc Natl Acad Sci USA. 2017;114(13):3409-3414. PMID: 28289229. [DOI: 10.1073/pnas.1702357114](https://doi.org/10.1073/pnas.1702357114)

9. **pinke-2020-mammalian-atp-synthase**: Pinke G, Zhou L, Sazanov LA. Cryo-EM structure of the entire mammalian F-type ATP synthase. Nat Struct Mol Biol. 2020;27(11):1077-1085. PMID: 32929284. [DOI: 10.1038/s41594-020-0503-8](https://doi.org/10.1038/s41594-020-0503-8)

10. **nesci-2015-c-ring-review**: Nesci S, Trombetti F, Ventrella V, Pagliarani A. The c-Ring of the F1FO-ATP Synthase: Facts and Perspectives. J Membr Biol. 2015;249(1-2):11-21. PMID: 26621635. [DOI: 10.1007/s00232-015-9860-3](https://doi.org/10.1007/s00232-015-9860-3)

11. **ezaki-1995-ncl-subunit-c**: Ezaki J, Wolfe LS, Ishidoh K, Kominami E. Abnormal degradative pathway of mitochondrial ATP synthase subunit c in late infantile neuronal ceroid-lipofuscinosis (Batten disease). Am J Med Genet. 1995;57(2):254-9. PMID: 7668341. [DOI: 10.1002/ajmg.1320570229](https://doi.org/10.1002/ajmg.1320570229)

12. **palmer-2013-ncl-mechanisms**: Palmer DN, Barry LA, Tyynelä J, Cooper JD. NCL disease mechanisms. Biochim Biophys Acta. 2013;1832(11):1882-93. PMID: 23707513. [DOI: 10.1016/j.bbadis.2013.05.014](https://doi.org/10.1016/j.bbadis.2013.05.014)

13. **ruhle-2015-assembly**: Rühle T, Leister D. Assembly of F1F0-ATP synthases. Biochim Biophys Acta. 2015;1847(9):849-60. PMID: 25667968. [DOI: 10.1016/j.bbabio.2015.02.005](https://doi.org/10.1016/j.bbabio.2015.02.005)

14. **zhou-2017-c-ring-not-mpt**: Zhou W, Marinelli F, Nief C, Faraldo-Gómez JD. Atomistic simulations indicate the c-subunit ring of the F1FO ATP synthase is not the mitochondrial permeability transition pore. eLife. 2017;6:e23781. PMID: 28186490. [DOI: 10.7554/eLife.23781](https://doi.org/10.7554/eLife.23781)

15. **chen-2004-trimethyllysine**: Chen R, Fearnley IM, Peak-Chew SY, Walker JE. Lysine 43 is trimethylated in subunit C from bovine mitochondrial ATP synthase and in storage bodies associated with Batten disease. J Biol Chem. 2004;279(21):21883-7. PMID: 15010464. [DOI: 10.1074/jbc.M311950200](https://doi.org/10.1074/jbc.M311950200)

16. **chen-2019-fam173b-methyltransferase**: Chen R, Fearnley IM, Palmer DN, Walker JE. Lysine methylation by the mitochondrial methyltransferase FAM173B optimizes the function of mitochondrial ATP synthase. J Biol Chem. 2019;294(4):1128-1138. PMID: 30530489. [DOI: 10.1074/jbc.RA118.005473](https://doi.org/10.1074/jbc.RA118.005473)

17. **human-protein-atlas-atp5mc3**: The Human Protein Atlas. ATP5MC3 protein expression summary. Available at: [https://www.proteinatlas.org/ENSG00000154518-ATP5MC3](https://www.proteinatlas.org/ENSG00000154518-ATP5MC3)

18. **genecards-atp5mc3**: GeneCards. ATP5MC3 Gene. Available at: [https://www.genecards.org/cgi-bin/carddisp.pl?gene=ATP5MC3](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ATP5MC3)


## Citations

1. blanc-2024-c-ring-rotation-abstract.md
2. bonora-2017-mpt-c-ring-abstract.md
3. chen-2004-trimethyllysine-abstract.md
4. chen-2019-fam173b-methyltransferase-abstract.md
5. ezaki-1995-ncl-subunit-c-abstract.md
6. he-2017-ptp-without-c-subunit-abstract.md
7. kuhlbrandt-2019-atp-synthase-review-abstract.md
8. mnatsakanyan-2022-c-ring-leak-channel-abstract.md
9. mnatsakanyan-2022-c-ring-leak-channel-summary.md
10. neilson-2021-atp5mc3-dystonia-abstract.md
11. neilson-2021-atp5mc3-dystonia-summary.md
12. nesci-2015-c-ring-review-abstract.md
13. palmer-2013-ncl-mechanisms-abstract.md
14. pinke-2020-mammalian-atp-synthase-abstract.md
15. pinke-2020-mammalian-atp-synthase-summary.md
16. ruhle-2015-assembly-abstract.md
17. yan-1994-atp5g3-cloning-abstract.md
18. zech-2022-atp-synthase-variants-abstract.md
19. zhou-2017-c-ring-not-mpt-abstract.md