---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:02:51.505251'
end_time: '2026-10-26T01:10:39.363505'
duration_seconds: 467.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: SLC16A11
  gene_symbol: SLC16A11
  uniprot_accession: A0A9L0JV53
  protein_description: 'RecName: Full=Monocarboxylate transporter 11 {ECO:0000256|ARBA:ARBA00073864};
    AltName: Full=Solute carrier family 16 member 11 {ECO:0000256|ARBA:ARBA00078723};'
  gene_info: Name=SLC16A11 {ECO:0000313|Ensembl:ENSEASP00005053015.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the major facilitator superfamily.
  protein_domains: MFS. (IPR011701); MFS_trans_sf. (IPR036259); Proton-linked_MCT.
    (IPR050327); MFS_1 (PF07690)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3301
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 41
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0JV53
- **Protein Description:** RecName: Full=Monocarboxylate transporter 11 {ECO:0000256|ARBA:ARBA00073864}; AltName: Full=Solute carrier family 16 member 11 {ECO:0000256|ARBA:ARBA00078723};
- **Gene Information:** Name=SLC16A11 {ECO:0000313|Ensembl:ENSEASP00005053015.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the major facilitator superfamily.
- **Key Domains:** MFS. (IPR011701); MFS_trans_sf. (IPR036259); Proton-linked_MCT. (IPR050327); MFS_1 (PF07690)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SLC16A11" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SLC16A11' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SLC16A11** (gene ID: SLC16A11, UniProt: A0A9L0JV53) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SLC16A11 (Monocarboxylate Transporter 11) in the Donkey, *Equus asinus* (UniProt A0A9L0JV53)

## 1. Introduction and Summary

The donkey protein A0A9L0JV53 is an unreviewed TrEMBL entry, predicted by Ensembl from the donkey reference genome (Wang et al. 2020), and named Monocarboxylate transporter 11 (MCT11), gene *SLC16A11*, on donkey chromosome 13 [uniprot-A0A9L0JV53-entry; wang-2020-donkey-genomes-abstract]. We checked the identity before starting. The gene symbol, protein name, family assignment (major facilitator superfamily, monocarboxylate porter family TC 2.A.1.13, PANTHER PTHR11360:SF80 "Monocarboxylate transporter 11") and domain content (MFS_1, Pfam PF07690; Proton-linked_MCT, IPR050327) all agree with one another [uniprot-A0A9L0JV53-entry]. Our own pairwise alignment shows the donkey protein is 89% identical to human SLC16A11 (UniProt Q8NCK7) over 335 residues, from human residue 113 to the C-terminus [SEQUENCE_ANALYSIS.md]. The symbol is therefore not ambiguous, and A0A9L0JV53 is the donkey ortholog of human SLC16A11.

We found no experimental study of SLC16A11 in the donkey or in any other equid. The donkey genome paper reports only the genome sequence [wang-2020-donkey-genomes-abstract]. Everything below about function is therefore inferred from orthologs, mainly human, with supporting data from mouse and from a related *Drosophila* transporter. The UniProt annotations on the donkey entry are automatic (ARBA) transfers from the reviewed human entry [uniprot-A0A9L0JV53-entry; uniprot-Q8NCK7-human-SLC16A11-entry].

On this evidence, SLC16A11 is a proton-coupled monocarboxylate transporter in category I of the SLC16 family. It moves pyruvate across the plasma membrane together with H+ (RHEA:64720, pyruvate(out) + H+(out) = pyruvate(in) + H+(in)), and transport runs in both directions [rusu-2017-slc16a11-two-mechanisms-fulltext]. In T cells it also takes up lactate [peralta-2024-mct11-exhausted-tcells-fulltext]. Most of the protein sits in the endoplasmic reticulum (ER) membrane. Only a small fraction reaches the cell surface, and getting there depends on the ancillary glycoprotein basigin (BSG/CD147); the protein also binds embigin [sigma-2014-slc16a11-t2d-mexico-fulltext; rusu-2017-slc16a11-two-mechanisms-fulltext]. In human liver, SLC16A11 activity is linked to fatty acid and glycerolipid metabolism, including triacylglycerol accumulation. Human SLC16A11 variants are a major risk factor for type 2 diabetes in Latin American populations [sigma-2014-slc16a11-t2d-mexico-abstract; rusu-2017-slc16a11-two-mechanisms-abstract]. In mouse, *Slc16a11* is induced in terminally exhausted CD8+ T cells, where it imports lactic acid [peralta-2024-mct11-exhausted-tcells-abstract].

One caveat about the donkey sequence matters for annotation. A0A9L0JV53 is not the main protein product of the donkey gene. Ensembl annotates five protein-coding transcripts for donkey *SLC16A11* (ENSEASG00005017919). The canonical one, ENSEAST00005028528, encodes a 520-residue protein (UniProt A0A8C4PS96) that aligns to all 447 residues of human SLC16A11 with about 91% identity [ensembl-ENSEASG00005017919-donkey-SLC16A11-gene; uniprot-A0A8C4PS96-donkey-SLC16A11-isoform-entry; SEQUENCE_ANALYSIS.md]. A0A9L0JV53 comes from a shorter, non-canonical three-exon transcript, ENSEAST00005059140. Its first ~100 residues are encoded by an alternative 5′ exon and do not match the human N-terminus, so the protein lacks the first two transmembrane helices, and only six helices are predicted for it [uniprot-A0A9L0JV53-entry; SEQUENCE_ANALYSIS.md]. Whether this isoform is a real, functional transcript has not been tested. Without TM1 it may not be able to fold into a working transporter, so its functional annotations rest on the full-length gene product.

## 2. Molecular Identity, Family Membership and Sequence Conservation

The SLC16 gene family has fourteen members. All are predicted to have twelve transmembrane helices, with the N- and C-termini inside the cell and a large cytoplasmic loop between TM6 and TM7 [halestrap-2013-slc16-family-abstract]. The family falls into two functional groups. Category I members (MCT1–4, encoded by *SLC16A1*, *SLC16A7*, *SLC16A8* and *SLC16A3*) are proton-linked carriers of simple monocarboxylates such as L-lactate, pyruvate and ketone bodies, and they need basigin or embigin to reach the plasma membrane. Category II members (MCT8/SLC16A2 and TAT1/SLC16A10) carry thyroid hormones or aromatic amino acids by facilitated diffusion and do not depend on these chaperones [halestrap-2013-slc16-family-abstract; rusu-2017-slc16a11-two-mechanisms-fulltext]. When Halestrap reviewed the family in 2013, the substrate of MCT11 was still unknown [halestrap-2013-slc16-family-abstract].

Rusu and colleagues used sequence features to place SLC16A11 in category I. In MCT1, three charged residues are thought to be key for monocarboxylate translocation: K38 in TM1, and D309 and R313 in TM8. Category I members keep all three charges, while category II members replace K38 and D309 with uncharged residues. Human SLC16A11 has charged residues at all three positions (R57, D290 and R294 in the numbering of that paper), and a homology model puts them in the inner pore [rusu-2017-slc16a11-two-mechanisms-fulltext].

That paper numbers residues 24 positions higher than the canonical 447-residue UniProt human sequence, so these residues are R33, D266 and R270 in Q8NCK7 [SEQUENCE_ANALYSIS.md; uniprot-Q8NCK7-human-SLC16A11-entry]. Our alignment shows that the donkey protein keeps the TM8 pair as D258 and R262. The TM1 arginine falls in the human N-terminal segment, which is missing from A0A9L0JV53 but is kept as R106 in the full-length canonical donkey isoform A0A8C4PS96 [SEQUENCE_ANALYSIS.md; uniprot-A0A8C4PS96-donkey-SLC16A11-isoform-entry]. The canonical donkey protein and the horse protein A0A9L0RBE3 differ at only three positions, so the sequence is almost fixed within *Equus* [SEQUENCE_ANALYSIS.md]. Two residues that carry type 2 diabetes risk substitutions in humans, G316 and P419 in UniProt numbering, are conserved in donkey as G308 and P411 [SEQUENCE_ANALYSIS.md; uniprot-Q8NCK7-human-SLC16A11-entry].

Evolutionary data from invertebrates point the same way. A *Drosophila* screen for solute transporters needed in autophagy-dependent cell death identified CG11665/Hermes, whose closest human relative is SLC16A11. Hermes is a proton-coupled monocarboxylate transporter that prefers pyruvate to lactate [velentzas-2018-hermes-mct-autophagy-abstract]. The full paper adds detail [velentzas-2018-hermes-mct-autophagy-fulltext]. Hermes keeps the three category I signature residues (K74, D503 and R507). In HEK293T cells carrying a pH sensor on the cell surface, Hermes doubled proton-coupled pyruvate transport compared with control cells, but it did not change lactate transport; rat MCT1, tested in parallel, moved both substrates. In fly salivary gland cells, Hermes sits at the plasma membrane, and knocking down basigin with RNAi displaces it. Loss of Hermes enlarged lipid droplets and raised mTOR signalling. A pyruvate-preferring, proton-coupled, basigin-dependent activity therefore seems to be an old property of this clade, and it fits the human data described in the next section.

## 3. Transport Function: Proton-Coupled Pyruvate (and Lactate) Transport

The main direct evidence for SLC16A11 transport activity comes from Rusu et al. (2017), who expressed human SLC16A11 in HEK293T cells and followed intracellular pyruvate in real time with the genetically encoded FRET sensor Pyronic. Cells expressing the reference SLC16A11 took up and released pyruvate about 45% faster than control cells [rusu-2017-slc16a11-two-mechanisms-fulltext]. The MCT inhibitor AR-C155858 abolished the endogenous pyruvate signal in control cells, which shows the assay measures SLC16-type transport.

The authors monitored intracellular pH at the same time with the dye BCECF. Rates of acidification and alkalinization rose by about 40%, mirroring pyruvate influx and efflux. They concluded that SLC16A11 moves H+ together with pyruvate, as in the canonical MCT1–4 mechanism [rusu-2017-slc16a11-two-mechanisms-fulltext]. The effect of SLC16A11 could only be seen at neutral pH, because at acidic pH the endogenous MCTs were activated and masked it [rusu-2017-slc16a11-two-mechanisms-fulltext].

These experiments define the reaction curated in UniProt and transferred to the donkey entry: pyruvate(out) + H+(out) = pyruvate(in) + H+(in) (RHEA:64720) [uniprot-Q8NCK7-human-SLC16A11-entry; uniprot-A0A9L0JV53-entry]. The T2D risk form of the protein, which carries all five coding variants of the risk haplotype, gave about 50% lower pyruvate and proton flux than the reference form [rusu-2017-slc16a11-two-mechanisms-fulltext].

Lactate is also a physiological substrate. Peralta et al. (2024) overexpressed MCT11 in mouse CD8+ T cells and saw increased uptake of [14C]-lactate and its oxidation to CO2. Conditional deletion of *Slc16a11* in T cells reduced lactic acid uptake by exhausted T cells, and a blocking monoclonal antibody against MCT11 reduced lactate oxidation in sorted exhausted cells [peralta-2024-mct11-exhausted-tcells-fulltext]. The authors also note that MCTs can carry other substrates, including pyruvate, ketone bodies and other monocarboxylates, so lactate may not be the only cargo that matters in vivo [peralta-2024-mct11-exhausted-tcells-fulltext].

Several basic transport properties of SLC16A11 have not been measured: kinetic constants (Km, Vmax), the substrate selectivity series (for example pyruvate versus lactate versus ketone bodies) and the stoichiometry. Data from the fly relative, which moves pyruvate but not detectably lactate in the same assay, suggest a preference for pyruvate [velentzas-2018-hermes-mct-autophagy-fulltext]. The mouse T-cell results show, however, that mammalian MCT11 can carry lactate at a level that matters physiologically [peralta-2024-mct11-exhausted-tcells-fulltext]. Direct side-by-side comparisons for the mammalian protein are still lacking.

## 4. Subcellular Localization and the Basigin Partnership

The first localization study expressed C-terminally V5-tagged human SLC16A11 in HeLa cells. The tagged protein co-localized with the ER membrane protein calnexin and overlapped very little with plasma membrane, Golgi or mitochondrial markers. SLC16A13, encoded by the neighbouring gene, localized to the Golgi instead [sigma-2014-slc16a11-t2d-mexico-fulltext]. Because triacylglycerol synthesis happens in the ER, the authors suggested that SLC16A11 might act directly on hepatic lipid metabolism there [sigma-2014-slc16a11-t2d-mexico-fulltext].

Membrane fractionation in HEK293T cells later confirmed that most SLC16A11 is on intracellular membranes, with about 5% at the plasma membrane [rusu-2017-slc16a11-two-mechanisms-fulltext]. Plasma-membrane delivery depends on basigin. In an immunoprecipitation–mass spectrometry interactome, basigin (BSG) and embigin (EMB), the known chaperones of category I MCTs, were among the most enriched interactors. Knocking out BSG reduced plasma-membrane SLC16A11 by about 80%, as measured both by fractionation and by a split β-galactosidase reporter [rusu-2017-slc16a11-two-mechanisms-fulltext].

UniProt annotates the interaction specifically with BSG isoform 2, and lists both "cell membrane" and "endoplasmic reticulum membrane" as locations; both annotations are transferred to the donkey protein [uniprot-Q8NCK7-human-SLC16A11-entry; uniprot-A0A9L0JV53-entry]. Native mouse MCT11 is detected on the surface of exhausted CD8+ T cells by flow cytometry and can be targeted by an extracellular blocking antibody. At least in this cell type, a functionally important pool of the endogenous protein is therefore at the plasma membrane [peralta-2024-mct11-exhausted-tcells-fulltext].

The same interactome analysis found a cluster of proteasome subunits. Overexpressed SLC16A11 was degraded quickly after protein synthesis was blocked and was stabilized by proteasome inhibitors. A Pro2→Asp substitution at a possible N-degron site raised its steady-state level [rusu-2017-slc16a11-two-mechanisms-fulltext]. SLC16A11 protein levels thus appear to be tightly controlled by proteasomal turnover.

A0A9L0JV53 does not contain the human Met1-Pro2 N-terminus. In the canonical donkey isoform, by contrast, the human-like start (MTPKPAG…) is preceded by a 73-residue extension [SEQUENCE_ANALYSIS.md]. This extension resembles the extended N-termini that UniProt flags as erroneous initiation in several human cDNAs [uniprot-Q8NCK7-human-SLC16A11-entry]. The true translation start of donkey SLC16A11, and therefore any N-degron regulation, needs confirmation before N-terminal features are annotated.

## 5. Tissue Expression and Physiological Roles in Hepatic Lipid Metabolism

In humans, *SLC16A11* mRNA is expressed in few tissues. It is detected mainly in liver, salivary gland and thyroid, both by Nanostring profiling and in about 55,000 microarray samples [sigma-2014-slc16a11-t2d-mexico-fulltext]. The human function studies have therefore focused on hepatocytes.

The direction of effect on lipids is inconsistent between experimental systems. Overexpressing SLC16A11 in HeLa cells raised intracellular triacylglycerols strongly, raised diacylglycerols slightly, and lowered lysophosphatidylcholine, cholesterol esters and sphingomyelin [sigma-2014-slc16a11-t2d-mexico-fulltext]. Yet siRNA knockdown of about 90% of SLC16A11 in primary human hepatocytes also raised intracellular acylcarnitines, diacylglycerols and triacylglycerols, along with extracellular (VLDL-associated) triacylglycerols, without changing other MCTs or BSG [rusu-2017-slc16a11-two-mechanisms-fulltext]. Rusu and colleagues read the acylcarnitine rise as a change in mitochondrial fatty acid β-oxidation, and the glycerolipid rise as a shift toward energy storage, a pattern resembling insulin resistance [rusu-2017-slc16a11-two-mechanisms-fulltext].

The mechanism linking pyruvate–H+ transport to lipid handling has not been shown. One plausible link, which has not been tested, is that pyruvate supply to mitochondria or the cytosolic redox and pH state changes how fatty acids are partitioned between oxidation and esterification.

The mouse studies add to the uncertainty. *Slc16a11* knockout mice had no significant metabolic defects. Re-expressing a mutant, but not wild-type, *Slc16a11* in the knockout liver increased hepatic triglycerides and caused insulin resistance through upregulation of lipin 1 [zhao-2019-slc16a11-gain-of-function-abstract]. In a separate study, high-fat feeding induced hepatic *Slc16a11*, and AAV-mediated knockdown improved glucose tolerance, lowered serum and liver triacylglycerols and increased Akt/GSK3β phosphorylation. Endurance exercise lowered hepatic *Slc16a11* expression [zhang-2021-slc16a11-aav-knockdown-abstract].

So the human hepatocyte data suggest that loss of SLC16A11 promotes lipid accumulation, while the mouse data suggest the opposite or no effect. The disagreement may reflect species differences, the type of perturbation (acute siRNA, germline knockout or AAV), or effects of overexpression. Taken together, these data place SLC16A11 in hepatic fatty acid and glycerolipid metabolism as a pyruvate/monocarboxylate transporter, but they do not settle whether its normal role is to restrain or to promote triglyceride storage.

## 6. Human Genetics: SLC16A11 and Type 2 Diabetes

Much of what is known about SLC16A11 comes from genetics. A genome-wide association study of 8,214 Mexicans and other Latin Americans found a risk haplotype spanning *SLC16A11* and *SLC16A13* (OR ≈ 1.29), with the association stronger in younger and leaner patients. The haplotype carries four amino acid substitutions, all in SLC16A11. It is present at about 50% frequency in Native American samples and about 10% in East Asian samples, and it entered modern humans through admixture with Neanderthals [sigma-2014-slc16a11-t2d-mexico-abstract].

Rusu et al. found two separate molecular effects of the haplotype. A cis-eQTL lowers *SLC16A11* expression in liver, by about 42% in heterozygotes and about 66% in homozygotes, with matching allelic imbalance and reduced H3K27ac at the promoter. In addition, the coding variants (V113I, D127G, G340S and P443T in that paper's numbering, which are V89I, D103G, G316S and P419T in UniProt) selectively break the interaction with BSG and reduce plasma-membrane localization by about 60% [rusu-2017-slc16a11-two-mechanisms-fulltext; uniprot-Q8NCK7-human-SLC16A11-entry]. Both effects reduce SLC16A11 function, which led the authors to propose that raising SLC16A11 activity could be therapeutic [rusu-2017-slc16a11-two-mechanisms-abstract].

Zhao et al. disputed this on the basis of their mouse knockout and reconstitution data, arguing for a gain of aberrant function [zhao-2019-slc16a11-gain-of-function-abstract]. Hoch et al. replied that the gain-of-function claim was not supported, because the murine variant model was inaccurate and expression levels were not physiological [hoch-2019-slc16a11-matters-arising-abstract]. Zhao et al. kept their position in a response [zhao-2019-slc16a11-reply-not-lof-abstract].

Human physiology studies have since linked the risk haplotype to lower insulin action, higher serum transaminases and larger adipocytes [almeda-valdes-2019-slc16a11-insulin-action-abstract; aguilar-salinas-2023-slc16a11-review-abstract]. A 2026 review uses SLC16A11 as an example of a T2D effector gene acting in hepatocyte lipid metabolism [maynard-2026-variant-to-function-t2d-abstract]. These human findings do not transfer directly to the donkey, but they show which residues and regulatory features matter for function. Two of the affected residues are conserved in the donkey protein [SEQUENCE_ANALYSIS.md].

## 7. Immunometabolic Role: Lactate Uptake by Exhausted CD8+ T Cells

Mouse studies have revealed a second, unrelated role. In the tumour microenvironment, terminally exhausted CD8+ T cells (PD1hi Tim3+ TOXhi) specifically upregulate *Slc16a11*. Chronic TCR stimulation induces it, hypoxia induces it more strongly through HIF1α, and the exhaustion transcription factors TOX and BATF bind the gene locus. The same cells are found in human head and neck tumour infiltrates [peralta-2024-mct11-exhausted-tcells-fulltext].

Within tumour-infiltrating immune cells, MCT11 expression was restricted to CD8+ T cells, as shown with a GFP-reporting conditional allele [peralta-2024-mct11-exhausted-tcells-fulltext]. Deleting MCT11 in T cells reduced lactate uptake, lowered expression of terminal-exhaustion markers, shifted the transcriptome toward the progenitor-exhausted state, improved cytokine production and increased responses to anti-PD1 therapy. An anti-MCT11 antibody had similar effects and slowed tumour growth [peralta-2024-mct11-exhausted-tcells-abstract].

These results show that MCT11 is a plasma-membrane importer of lactic acid in a physiological setting. They also show that its expression responds to hypoxia and to signals from the TCR and exhaustion programmes.

## 8. Implications for Annotation of the Donkey Protein

For the donkey protein A0A9L0JV53, the evidence supports the following functional annotations, all inferred by orthology with reasonable confidence. The molecular function is proton-coupled monocarboxylate symport, with pyruvate as the experimentally shown substrate (pyruvate:H+ symporter activity, RHEA:64720) and lactate as a further substrate [rusu-2017-slc16a11-two-mechanisms-fulltext; peralta-2024-mct11-exhausted-tcells-fulltext]. The biological processes are pyruvate and monocarboxylate transmembrane transport, with likely involvement in hepatic fatty acid and triglyceride metabolism [rusu-2017-slc16a11-two-mechanisms-fulltext; sigma-2014-slc16a11-t2d-mexico-fulltext]. The cellular components are the ER membrane and the plasma membrane, with basigin required to reach the plasma membrane [sigma-2014-slc16a11-t2d-mexico-fulltext; rusu-2017-slc16a11-two-mechanisms-fulltext].

These are the same annotations UniProt already applies by its automatic ARBA rules, together with the IEA GO terms for ER membrane, plasma membrane and monocarboxylic acid transmembrane transporter activity [uniprot-A0A9L0JV53-entry]. Annotating A0A9L0JV53 in particular should take into account that it is a non-canonical isoform without TM1–TM2. Function is best attached to the gene and its full-length product (A0A8C4PS96). For this isoform, the transporter activity should be treated as uncertain unless the transcript is shown to be expressed and to make a working protein [ensembl-ENSEASG00005017919-donkey-SLC16A11-gene; SEQUENCE_ANALYSIS.md].

## Open Questions

The most immediate open question for this entry is whether the A0A9L0JV53 transcript is real. It lacks the conserved TM1–TM2 region that is present in the canonical 520-residue isoform from the same gene. Donkey liver RNA-seq or long-read transcript data would show whether this alternative 5′ exon is used and whether the shorter protein exists. It would also show where translation of the canonical isoform starts: at the human-equivalent methionine, or 73 residues upstream.

Several questions about the mammalian protein are also unresolved. The kinetic parameters and substrate range (pyruvate, L-lactate, ketone bodies, short-chain fatty acids) have never been measured systematically, and no experimental structure exists. It is unclear whether the ER-resident pool, which is the majority of the overexpressed protein, transports anything across the ER membrane, or whether it is simply a biosynthetic or degradation intermediate. The link between pyruvate–H+ transport and changes in acylcarnitines and glycerolipids has not been established mechanistically. Finally, the conflicting directions of effect between human hepatocyte knockdown, mouse knockout or knockdown, and overexpression need to be reconciled, for example with endogenous-level knock-in models of the human haplotype.

Equid physiology is a promising area for follow-up. Horses and donkeys are prone to insulin dysregulation, equine metabolic syndrome and hyperlipaemia, the last of which is particularly common in donkeys. It would be useful to profile *SLC16A11* expression in equid liver, thyroid and immune cells, and to look for variation in equid populations. Whether exhausted T cells in equids also upregulate MCT11 is unknown.

## References

* [uniprot-A0A9L0JV53-entry] UniProtKB A0A9L0JV53 (A0A9L0JV53_EQUAS), Monocarboxylate transporter 11, *Equus asinus*; unreviewed TrEMBL entry, version 15 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0JV53.txt
* [uniprot-Q8NCK7-human-SLC16A11-entry] UniProtKB/Swiss-Prot Q8NCK7 (MOT11_HUMAN), Monocarboxylate transporter 11, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/Q8NCK7.txt
* [SEQUENCE_ANALYSIS.md] Our own pairwise alignments of donkey and horse SLC16A11 entries against human Q8NCK7, done for this report (Biopython, BLOSUM62).
* [uniprot-A0A8C4PS96-donkey-SLC16A11-isoform-entry] UniProtKB A0A8C4PS96 (A0A8C4PS96_EQUAS), Monocarboxylate transporter 11, *Equus asinus*, 520 aa; unreviewed; Ensembl ENSEAST00005028528.2. https://rest.uniprot.org/uniprotkb/A0A8C4PS96.txt
* [ensembl-ENSEASG00005017919-donkey-SLC16A11-gene] Ensembl gene ENSEASG00005017919 (SLC16A11, *Equus asinus*, chromosome 13:14,702,514-14,710,941), REST lookup. https://rest.ensembl.org/lookup/id/ENSEASG00005017919?expand=1
* [wang-2020-donkey-genomes] Wang C, Li H, Guo Y, et al. Donkey genomes provide new insights into domestication and selection for coat color. Nat Commun. 2020;11:6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7.
* [sigma-2014-slc16a11-t2d-mexico] SIGMA Type 2 Diabetes Consortium; Williams AL, Jacobs SB, et al. Sequence variants in SLC16A11 are a common risk factor for type 2 diabetes in Mexico. Nature. 2014;506(7486):97-101. PMID: 24390345; PMCID: PMC4127086; DOI: 10.1038/nature12828.
* [rusu-2017-slc16a11-two-mechanisms] Rusu V, Hoch E, Mercader JM, et al. Type 2 Diabetes Variants Disrupt Function of SLC16A11 through Two Distinct Mechanisms. Cell. 2017;170(1):199-212.e20. PMID: 28666119; PMCID: PMC5562285; DOI: 10.1016/j.cell.2017.06.011.
* [zhao-2019-slc16a11-gain-of-function] Zhao Y, Feng Z, Zhang Y, et al. Gain-of-Function Mutations of SLC16A11 Contribute to the Pathogenesis of Type 2 Diabetes. Cell Rep. 2019;26(4):884-892.e4. PMID: 30673611; DOI: 10.1016/j.celrep.2018.12.100.
* [hoch-2019-slc16a11-matters-arising] Hoch E, Florez JC, Lander ES, Jacobs SBR. Gain-of-Function Claims for Type-2-Diabetes-Associated Coding Variants in SLC16A11 Are Not Supported by the Experimental Data. Cell Rep. 2019;29(3):778-780. PMID: 31618643; DOI: 10.1016/j.celrep.2019.09.021.
* [zhao-2019-slc16a11-reply-not-lof] Zhao Y, Feng Z, Ding Q. Type 2 Diabetes Variants in the SLC16A11 Coding Region Are Not Loss-of-Function Mutations. Cell Rep. 2019;29(3):781-784. PMID: 31618644; DOI: 10.1016/j.celrep.2019.09.022.
* [zhang-2021-slc16a11-aav-knockdown] Zhang T, Qi Z, Wang H, Ding S. Adeno-Associated Virus-Mediated Knockdown of SLC16A11 Improves Glucose Tolerance and Hepatic Insulin Signaling in High Fat Diet-Fed Mice. Exp Clin Endocrinol Diabetes. 2021;129(2):104-111. PMID: 31185508; DOI: 10.1055/a-0840-3330.
* [peralta-2024-mct11-exhausted-tcells] Peralta RM, Xie B, Lontos K, et al. Dysfunction of exhausted T cells is enforced by MCT11-mediated lactate metabolism. Nat Immunol. 2024;25(12):2297-2307. PMID: 39516648; PMCID: PMC11588660; DOI: 10.1038/s41590-024-01999-3.
* [halestrap-2013-slc16-family] Halestrap AP. The SLC16 gene family - structure, role and regulation in health and disease. Mol Aspects Med. 2013;34(2-3):337-49. PMID: 23506875; DOI: 10.1016/j.mam.2012.05.003.
* [velentzas-2018-hermes-mct-autophagy] Velentzas PD, Zhang L, Das G, Chang TK, Nelson C, Kobertz WR, Baehrecke EH. The Proton-Coupled Monocarboxylate Transporter Hermes Is Necessary for Autophagy during Cell Death. Dev Cell. 2018;47(3):281-293.e4. PMID: 30318245; PMCID: PMC6219939; DOI: 10.1016/j.devcel.2018.09.015.
* [aguilar-salinas-2023-slc16a11-review] Aguilar-Salinas CA, Tusie Luna MT. The role of SLC16A11 variations in diabetes mellitus. Curr Opin Nephrol Hypertens. 2023;32(5):445-450. PMID: 37530085; DOI: 10.1097/MNH.0000000000000914.
* [almeda-valdes-2019-slc16a11-insulin-action] Almeda-Valdes P, et al. The SLC16A11 risk haplotype is associated with decreased insulin action, higher transaminases and large-size adipocytes. Eur J Endocrinol. 2019;180(2):99-107. PMID: 30475225; DOI: 10.1530/EJE-18-0677.
* [kimura-2021-slc16a11-lipid-japanese] Kimura Y, Higuchi I, Kobayashi M, et al. The association between SLC16A11 haplotype and lipid metabolism in Japanese patients with type 2 diabetes. Drug Metab Pharmacokinet. 2021;37:100376. PMID: 33561739; DOI: 10.1016/j.dmpk.2020.100376. (Retrieved for background; not cited in the text.)
* [maynard-2026-variant-to-function-t2d] Maynard AG, Bhardwaj R, Jones TR, Claussnitzer M. Bridging the variant-to-function gap in type 2 diabetes: advances and challenges. Diabetologia. 2026;69(2):274-294. PMID: 41273414; PMCID: PMC12779665; DOI: 10.1007/s00125-025-06600-6.


## Citations

1. aguilar-salinas-2023-slc16a11-review-abstract.md
2. aguilar-salinas-2023-slc16a11-review-summary.md
3. almeda-valdes-2019-slc16a11-insulin-action-abstract.md
4. almeda-valdes-2019-slc16a11-insulin-action-summary.md
5. ensembl-ENSEASG00005017919-donkey-SLC16A11-gene-summary.md
6. ensembl-ENSEASG00005017919-donkey-SLC16A11-gene.json
7. halestrap-2013-slc16-family-abstract.md
8. halestrap-2013-slc16-family-summary.md
9. hoch-2019-slc16a11-matters-arising-abstract.md
10. hoch-2019-slc16a11-matters-arising-summary.md
11. kimura-2021-slc16a11-lipid-japanese-abstract.md
12. kimura-2021-slc16a11-lipid-japanese-summary.md
13. maynard-2026-variant-to-function-t2d-abstract.md
14. maynard-2026-variant-to-function-t2d-summary.md
15. peralta-2024-mct11-exhausted-tcells-abstract.md
16. peralta-2024-mct11-exhausted-tcells-fulltext.txt
17. peralta-2024-mct11-exhausted-tcells-summary.md
18. rusu-2017-slc16a11-two-mechanisms-abstract.md
19. rusu-2017-slc16a11-two-mechanisms-fulltext.txt
20. rusu-2017-slc16a11-two-mechanisms-summary.md
21. sigma-2014-slc16a11-t2d-mexico-abstract.md
22. sigma-2014-slc16a11-t2d-mexico-fulltext.txt
23. sigma-2014-slc16a11-t2d-mexico-summary.md
24. uniprot-A0A8C4PS96-donkey-SLC16A11-isoform-entry.txt
25. uniprot-A0A8C4PS96-donkey-SLC16A11-isoform-summary.md
26. uniprot-A0A9L0J0E5-donkey-SLC16A11-isoform-entry.txt
27. uniprot-A0A9L0JV53-entry.txt
28. uniprot-A0A9L0JV53-summary.md
29. uniprot-Q8NCK7-human-SLC16A11-entry.txt
30. uniprot-Q8NCK7-human-SLC16A11-summary.md
31. velentzas-2018-hermes-mct-autophagy-abstract.md
32. velentzas-2018-hermes-mct-autophagy-fulltext.txt
33. velentzas-2018-hermes-mct-autophagy-summary.md
34. wang-2020-donkey-genomes-abstract.md
35. wang-2020-donkey-genomes-summary.md
36. zhang-2021-slc16a11-aav-knockdown-abstract.md
37. zhang-2021-slc16a11-aav-knockdown-summary.md
38. zhao-2019-slc16a11-gain-of-function-abstract.md
39. zhao-2019-slc16a11-gain-of-function-summary.md
40. zhao-2019-slc16a11-reply-not-lof-abstract.md
41. zhao-2019-slc16a11-reply-not-lof-summary.md