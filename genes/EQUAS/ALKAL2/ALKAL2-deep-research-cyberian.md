---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:05:22.737057'
end_time: '2026-10-25T23:12:06.447849'
duration_seconds: 403.71
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: ALKAL2
  gene_symbol: ALKAL2
  uniprot_accession: A0A9L0J5U7
  protein_description: 'SubName: Full=ALK and LTK ligand 2 {ECO:0000313|Ensembl:ENSEASP00005045397.1};'
  gene_info: Name=ALKAL2 {ECO:0000313|Ensembl:ENSEASP00005045397.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the ALKAL family.
  protein_domains: ALKL1/2. (IPR029364); ALKL1_2 (PF15129)
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
citation_count: 56
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0J5U7
- **Protein Description:** SubName: Full=ALK and LTK ligand 2 {ECO:0000313|Ensembl:ENSEASP00005045397.1};
- **Gene Information:** Name=ALKAL2 {ECO:0000313|Ensembl:ENSEASP00005045397.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the ALKAL family.
- **Key Domains:** ALKL1/2. (IPR029364); ALKL1_2 (PF15129)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ALKAL2" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ALKAL2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ALKAL2** (gene ID: ALKAL2, UniProt: A0A9L0J5U7) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ALKAL2 (ALK and LTK ligand 2; augmentor-α; FAM150B) in the donkey, *Equus asinus* — UniProt A0A9L0J5U7

## 1. Introduction and summary

A0A9L0J5U7 is an unreviewed TrEMBL entry of 160 amino acids. It was predicted from the donkey reference genome and named ALKAL2 ("ALK and LTK ligand 2") by Ensembl (ENSEASP00005045397.1; gene ENSEASG00005022004 on chromosome 6). The entry places the protein in the ALKAL family and gives it a single ALKL1_2 domain (Pfam PF15129; InterPro IPR029364) [uniprot-A0A9L0J5U7-entry]. The underlying genome comes from the donkey domestication study of Wang et al., but that paper does not discuss this gene [wang-2020-donkey-genomes-summary]. No published experimental work exists on donkey ALKAL2. Identity was therefore checked by comparing sequences with the well-studied human orthologue, ALKAL2/FAM150B/augmentor-α (Q6UX46), and the check gives a clear answer. The gene symbol, protein description, family and domain all agree. The donkey protein is 86% identical to human ALKAL2 across its full length, and its C-terminal augmentor domain is identical residue for residue, including every residue that experiments have shown to bind the receptor, the membrane, or other ligand molecules [uniprot-A0A9L0J5U7-summary]. The literature reviewed below, all from human, mouse, zebrafish and Drosophila systems, describes the same protein family, and the symbol is not ambiguous here. Function in the donkey is inferred from orthology, which this sequence conservation supports strongly.

In mammals, ALKAL2 is a small secreted cytokine. It acts as the high-affinity activating ligand of two receptor tyrosine kinases (RTKs): anaplastic lymphoma kinase (ALK) and leukocyte tyrosine kinase (LTK). ALKAL2 binds the receptors' extracellular cytokine-binding segment and brings two receptor molecules together. This activates the intracellular kinase, which then phosphorylates tyrosines in its own tail and switches on downstream pathways such as ERK1/2 MAP kinase and AKT [zhang-2014-ltk-deorphanization-abstract; guan-2015-fam150-alk-ligands-abstract; reshetnyak-2015-augmentor-ligands-abstract; demunck-2021-alk-cytokine-structure-abstract; reshetnyak-2021-alk-activation-mechanism-abstract]. The protein has no enzymatic activity. Its molecular function is "receptor tyrosine kinase activator / cytokine": it is made by secreting cells, works in the extracellular space, and, once bound to ALK, sits at the outer face of the plasma membrane of the target cell [reshetnyak-2021-alk-activation-mechanism-summary]. Studies in animals link ALKAL2–ALK signalling to neural-crest development (zebrafish pigment cells), hypothalamic control of body weight and energy expenditure, sensitization of pain-sensing neurons, and, when the pathway is overactive, neuroblastoma and colorectal cancer [mo-2017-zebrafish-iridophore-abstract; fadeev-2018-alkals-neural-crest-abstract; ahmed-2022-hypothalamic-augmentor-alpha-abstract; defaye-2022-alkal2-pain-abstract; borenas-2021-alkal2-neuroblastoma-abstract].

## 2. Identity, sequence architecture and conservation of the donkey protein

The donkey sequence has the domain layout seen in the mammalian ALKAL2 proteins studied so far. A predicted N-terminal signal peptide (residues 1–24) is followed by a variable region (VR) of low conservation and then a conserved C-terminal augmentor domain (AD), which corresponds to the ALKL1_2 Pfam domain [uniprot-A0A9L0J5U7-entry]. In human ALKAL2, the four conserved cysteines of the AD form two intramolecular disulfides (Cys111–Cys147 and Cys125–Cys134). A fifth cysteine, Cys66 in the VR, is found only in primates and links two ALKAL2 molecules into a covalent dimer [reshetnyak-2018-alkal2-active-fragment-abstract; uniprot-Q6UX46-human-ALKAL2-entry]. Reshetnyak and colleagues noted that in other vertebrates Cys66 is usually replaced by a hydrophobic residue, typically tyrosine. They also showed that the human C66Y variant still forms non-covalent homodimers (apparent Kd about 38 µM), so the disulfide is not needed for dimerization [reshetnyak-2021-alk-activation-mechanism-fulltext].

A global pairwise alignment (BLOSUM62; script `alignment.py`, output `alignment_output.txt`) matches this pattern exactly. Donkey and human ALKAL2 share 131 of 152 human residues (86.2%). The donkey protein carries Tyr67 at the position of human Cys66, as expected for a non-primate. All four AD cysteines are conserved (donkey Cys113, Cys127, Cys136, Cys149). So are the site-1 arginines Arg123 and Arg136 (donkey Arg125 and Arg138), the site-2 residues Phe97 and His100, the dimer-interface residues Ile127 and Tyr130, and the basic membrane-contact patch Lys94/Lys96/Lys99/His100 (donkey Lys96/Lys98/Lys101/His102) [uniprot-A0A9L0J5U7-summary]. The only notable difference is a seven-residue C-terminal extension (…EDK**RAEPEEP**) predicted for donkey but absent from human. A comparison with other mammalian orthologues points to the gene model as the likely cause. The horse protein A0A3Q2I4Q6 (152 residues) is almost identical to the donkey protein up to the final conserved cysteine, but it ends …SPVCMEG. Cattle ALKAL2 ends …SPMCMEDK and mouse ALKAL2 (Q80UG6) ends …SPMCMER. No orthologue carries the RAEPEEP tail. Other horse gene models at this locus also disagree with one another, at both the N- and C-termini [uniprot-alkal2-orthologs-summary]. The tail is therefore best treated as uncertain. The ALK-binding segment ends at the conserved C-terminal cysteine, so the extension probably falls outside the folded domain. Because every functionally mapped residue is conserved, the donkey protein can be expected to fold like its human orthologue and to bind and activate equine ALK and LTK in the same way. The donkey entry's automatic annotations agree: secreted, cell membrane, receptor tyrosine kinase binding, and receptor signalling protein tyrosine kinase activator activity. These annotations come from ARBA, InterPro and TreeGrafter rules rather than direct experiment [uniprot-A0A9L0J5U7-entry].

## 3. Discovery as an activating ligand of ALK and LTK

ALK and LTK were "orphan" RTKs in vertebrates for many years. Their invertebrate counterparts had known ligands: Jelly belly in Drosophila and HEN-1 in *C. elegans* [guan-2015-fam150-alk-ligands-fulltext]. Zhang et al. resolved this for LTK by testing 3,191 individually expressed extracellular proteins for their ability to trigger LTK phosphorylation. Only two related secreted proteins worked, FAM150A and FAM150B (now ALKAL1 and ALKAL2), and FAM150A bound the LTK ectodomain with picomolar affinity (K_D = 28 pM) [zhang-2014-ltk-deorphanization-abstract]. Two groups then showed that these proteins also activate ALK. Guan et al. found that FAM150A and FAM150B bind the ALK extracellular domain. They induced phosphorylation of ALK Tyr1604 and of ERK1/2, and drove ALK-dependent neurite outgrowth in PC12 cells, whether co-expressed with the receptor or added in conditioned medium. They also activated human ALK in a Drosophila eye assay and further boosted constitutively active ALK mutants from neuroblastoma [guan-2015-fam150-alk-ligands-abstract; guan-2015-fam150-alk-ligands-fulltext]. Reshetnyak et al. named FAM150B "augmentor-α" (AUG-α) and set out the ligand–receptor hierarchy. AUG-α/ALKAL2 binds ALK with high affinity and activates both ALK and LTK at subnanomolar potency. FAM150A/AUG-β/ALKAL1, by contrast, is LTK-selective and binds ALK only weakly. AUG-α expression also transformed NIH/3T3 cells and made Ba/F3 cells grow without IL-3, both in an ALK-dependent way [reshetnyak-2015-augmentor-ligands-abstract]. A later review summarizes the potency differences: augmentor-α activates ALK and LTK at picomolar concentrations, whereas augmentor-β activates LTK at picomolar but ALK only at nanomolar concentrations [katic-2023-alk-augmentor-review-fulltext]. ALKAL2 is therefore the main physiological ALK agonist, and both ligands can act on LTK.

The minimal active unit was then defined. Reshetnyak et al. (2018) showed that a human AUG-α fragment lacking the N-terminal variable region, i.e. the augmentor domain alone, dimerizes poorly. Even so, it stimulates ALK and LTK tyrosine phosphorylation, the MAPK response in L6 cells, ALK-dependent soft-agar colony formation, and neuronal differentiation of NB1 neuroblastoma and PC12 cells almost as well as the full-length protein [reshetnyak-2018-alkal2-active-fragment-abstract]. This matters for interpreting the donkey protein. Its AD, which carries the receptor-activating function, is identical to the human AD. The VR, where donkey differs most and lacks Cys66, is not needed for activity in cell assays.

## 4. Structural mechanism of receptor activation

Three structural studies from 2021–2025 show how ALKAL2 activates its receptors. De Munck et al. solved crystal structures of the cytokine-binding segments of human ALK and LTK. This segment is a new fold: a permuted TNF-like module bracing a glycine-rich subdomain built from polyglycine type II helices, followed by a membrane-proximal EGF-like domain [demunck-2021-alk-cytokine-structure-abstract]. In their structures, the ALKAL1 and ALKAL2 C-terminal domains are monomeric, disulfide-stabilized three-helix bundles with an unusually open fold. One cytokine bridges two receptors. Helices B and C contact the TNF-like module of one receptor (site 1), and helix A contacts the second receptor (site 2), giving a 2:1 receptor–ligand assembly that holds the cytokine close to the membrane [demunck-2021-alk-cytokine-structure-fulltext]. Charge-reversal mutations at the conserved site-1 arginines (ALKAL2 R123E, R136E) strongly reduced affinity for both ALK and LTK, while site-2 mutations (F97E, H100A) had smaller effects. The membrane-proximal EGF-like domain explains why ALK prefers ALKAL2. The authors also noted that in vertebrate ALK, activation by ALKAL2 is further regulated by glycosaminoglycans (heparin/heparan sulfate) binding to an N-terminal heparin-binding domain on the receptor [demunck-2021-alk-cytokine-structure-fulltext].

Working independently with full-length ligand, Reshetnyak et al. (2021) used cryo-EM, NMR and crystallography. In their model, dimeric ALKAL2 forms a 2:2 ALK–ALKAL2 heterotetramer, while monomeric ALKAL1 or the isolated ALKAL2 AD first forms 1:1 complexes that then dimerize through receptor–receptor contacts [reshetnyak-2021-alk-activation-mechanism-abstract; reshetnyak-2021-alk-activation-mechanism-fulltext]. Ligand binding triggers a large rearrangement: an 80° bend at the TNF-like/EGF-like hinge and a 160° rotation. This leaves the ALK extracellular region lying parallel to the membrane. A conserved, positively charged patch on helix α1 of ALKAL2 (Lys94, Lys96, Lys99, His100) is predicted to face the negatively charged membrane. Reversing these charges left high-affinity binding to ALK intact in vitro but impaired ALK activation in cells. The ligand therefore acts at the membrane and helps to position the receptor there, which adds a fourth contact to the mechanism [reshetnyak-2021-alk-activation-mechanism-fulltext; katic-2023-alk-augmentor-review-fulltext]. UniProt accordingly annotates human ALKAL2 as associating with the cell membrane after it binds ALK [uniprot-Q6UX46-human-ALKAL2-entry].

The two models disagreed on stoichiometry (2:1 versus 2:2), and Felix et al. (2025) largely resolved this by reanalysing the public cryo-EM dataset (EMPIAR-10930). About 60% of ALK–ALKAL2 particles fell into a 2:1 assembly, now resolved to 3.2 Å, and about 40% into the published 2:2 form. Both stoichiometries therefore exist, built on a shared receptor dimerization mode for ALK and LTK [felix-2025-alk-cryoem-reanalysis-abstract; felix-2025-alk-cryoem-reanalysis-fulltext]. For the donkey protein, it is relevant that non-primate ALKAL2 lacks the dimerizing Cys66. The mechanism found to work for monomeric ligand (ALKAL1, ALKAL2 AD, C66Y), either 2:1 bridging or 1:1 complexes that then dimerize, is probably the relevant mode in equids.

## 5. Localization and signalling pathway

All available evidence places ALKAL2 outside the cell. Its N-terminal signal peptide directs it into the secretory pathway. It is released into culture medium, and medium conditioned by ALKAL2-expressing cells activates ALK on separate target cells [guan-2015-fam150-alk-ligands-fulltext; reshetnyak-2018-alkal2-active-fragment-abstract]. On target cells it binds the ALK/LTK ectodomain and, through its basic α1 patch, the outer leaflet of the plasma membrane [reshetnyak-2021-alk-activation-mechanism-fulltext]. Its action can be autocrine or paracrine, and over longer range neuronal. In the nervous system it appears to work like a neuropeptide-type signal released from nerve terminals: ALKAL2 made by AgRP neurons in the arcuate nucleus acts on Alk-expressing neurons in the paraventricular nucleus (PVN) [ahmed-2022-hypothalamic-augmentor-alpha-abstract]. ALKAL2 made by dorsal root ganglion (DRG) nociceptors activates ALK in the spinal dorsal horn [defaye-2022-alkal2-pain-abstract]. In the PVN, Fam150b and Alk are expressed in separate neurons and not in the same cells, which supports a paracrine or transsynaptic arrangement [gueissaz-2026-fam150b-hypothalamus-abstract]. The donkey entry's automatic "secreted" and "cell membrane" annotations are consistent with this [uniprot-A0A9L0J5U7-entry].

Downstream, ALKAL2 activates the ALK kinase. Activation has been measured as autophosphorylation (for example ALK pTyr1604) followed by ERK1/2 MAP kinase activation [guan-2015-fam150-alk-ligands-fulltext; reshetnyak-2018-alkal2-active-fragment-abstract]. In colorectal cancer cells of consensus molecular subtype 1 (CMS1), an autocrine ALKAL2–ALK loop signals mainly through AKT [mazzeschi-2022-alkal2-autocrine-crc-abstract]. The donkey protein's TreeGrafter-based GO terms, "positive regulation of ERK1 and ERK2 cascade" and "positive regulation of ERK5 cascade", agree with the ERK1/2 data [uniprot-A0A9L0J5U7-entry]. The ERK5 term could not be traced to a specific primary study in this review. In cells, the functional readouts are neuronal differentiation and neurite outgrowth (PC12 and NB1 cells, DRG neurons), increased neuronal excitability, and proliferation or transformation of cells that express ALK [guan-2015-fam150-alk-ligands-abstract; reshetnyak-2018-alkal2-active-fragment-abstract; defaye-2022-alkal2-pain-abstract].

## 6. Physiological roles revealed by genetic models

Zebrafish gave the first in vivo evidence that ALKALs are ALK-family ligands. Zebrafish have three augmentor genes (aug-α1, aug-α2, aug-β). Losing them impairs development of iridophores, a neural-crest-derived pigment cell, and this phenocopies ltk mutants. The effect works entirely through Ltk and not Alk, and different ligands are needed in different tissues [mo-2017-zebrafish-iridophore-abstract]. Fadeev et al. found the same independently: overexpressing alkals produced ectopic iridophores, and alkal triple mutants lacked iridophores entirely and died as larvae, like ltk nulls [fadeev-2018-alkals-neural-crest-abstract]. These results tie the ligand–receptor pair to neural-crest development, though the receptor involved differs between lineages. In fish, the pigmentation function goes through LTK. In mammals, the best-characterized ALKAL2 functions go through ALK.

In mice, the main role found so far is metabolic. Orthofer et al. identified ALK as a thinness gene in humans and showed that Alk-deficient mice are thin and resist obesity through hypothalamic, sympathetic control of fat breakdown (lipolysis) in adipose tissue [orthofer-2020-alk-thinness-abstract]. Ahmed et al. then showed that knocking out the ligand gives a similar picture. Augα (Alkal2) knockout mice and Augα/Augβ double knockouts were thin, resisted diet-induced obesity, and were more physically active, whereas Augβ single knockouts were normal [ahmed-2022-hypothalamic-augmentor-alpha-abstract]. Augα was strongly expressed in hunger-promoting AgRP neurons of the arcuate nucleus and increased with fasting, and AgRP projections reach Alk-expressing PVN neurons [ahmed-2022-hypothalamic-augmentor-alpha-fulltext]. A recent study added that Fam150b is expressed in some PVN CRH neurons and is induced by inflammation-associated stress in a glucocorticoid-dependent (mifepristone-sensitive) way. This suggests ALKAL2–ALK signalling may connect stress to feeding [gueissaz-2026-fam150b-hypothalamus-abstract]. In these models ALKAL2 is therefore the main endogenous ligand through which ALK controls energy expenditure.

ALKAL2 also acts in the peripheral nervous system. Defaye et al. found ALKAL2 enriched in peptidergic TRPV1+ nociceptors of mouse and human DRG, with expression rising after inflammation or nerve injury. ALKAL2 increased nociceptor excitability and neurite outgrowth, and intrathecal ALKAL2 phosphorylated ALK in the lumbar dorsal horn. Knocking down ALKAL2 in the DRG, or giving the ALK inhibitors crizotinib or lorlatinib, reversed inflammatory heat hyperalgesia and neuropathic mechanical allodynia [defaye-2022-alkal2-pain-abstract].

## 7. Pathological gain of function: cancer

Because ALK is an established oncogene, too much ALKAL2 can be oncogenic even when ALK itself is normal. In humans, ALKAL2 sits on 2p25, inside the "2p-gain" region of neuroblastoma that also contains ALK and MYCN. Borenäs et al. showed that transgenic ALKAL2 overexpression in mice speeds up MYCN-driven neuroblastoma without any ALK mutation, and that the tumours respond to ALK tyrosine kinase inhibitors [borenas-2021-alkal2-neuroblastoma-abstract]. In colorectal cancer, an autocrine ALKAL2–ALK loop supports CMS1 tumour growth through AKT [mazzeschi-2022-alkal2-autocrine-crc-abstract]. ALKAL2 released by TRPV1+ sensory neurons activates mucosal ALK and drives colitis-associated colorectal cancer, and lorlatinib reduced tumour burden by about 90% in that model [delanne-cumenal-2025-alkal2-colitis-cancer-abstract]. These disease findings rest on the same molecular function described above, ligand-driven activation of the ALK kinase, and make that function clearer rather than showing a separate role. No equine disease association with ALKAL2 was found.

## 8. Synthesis: functional annotation of donkey ALKAL2

Taken together, the evidence supports annotating A0A9L0J5U7 as a secreted cytokine whose primary molecular function is binding and activating receptor tyrosine kinases. Specifically, it is a high-affinity agonist of ALK and also of LTK [reshetnyak-2015-augmentor-ligands-abstract; guan-2015-fam150-alk-ligands-abstract; zhang-2014-ltk-deorphanization-abstract]. It works in the extracellular space and at the outer surface of the target-cell plasma membrane. There, its three-helix augmentor domain bridges two receptor ectodomains and its basic α1 patch contacts the membrane [demunck-2021-alk-cytokine-structure-fulltext; reshetnyak-2021-alk-activation-mechanism-fulltext]. Receptor activation leads to the ERK1/2 MAPK and AKT pathways [guan-2015-fam150-alk-ligands-fulltext; mazzeschi-2022-alkal2-autocrine-crc-abstract]. The best-supported biological processes, based on mouse and zebrafish orthologues, are hypothalamic regulation of energy expenditure and body weight, neuronal differentiation and neurite outgrowth, sensitization of nociceptors, and development of neural-crest derivatives [ahmed-2022-hypothalamic-augmentor-alpha-abstract; defaye-2022-alkal2-pain-abstract; fadeev-2018-alkals-neural-crest-abstract]. Transferring these findings to the donkey depends on orthology alone. It is well supported, because the functional domain is 100% identical to human and every experimentally mapped residue is conserved [uniprot-A0A9L0J5U7-summary]. Two donkey-specific features are worth noting. Lacking Cys66, the donkey protein is expected to dimerize only non-covalently, which matches the monomeric-ligand mechanism. Its predicted C-terminal extension needs to be confirmed against transcript evidence.

## Open Questions

Several points remain open, both for the donkey protein and for the family in general. First, no equine study has examined ALKAL2 expression, secretion or activity. It would help to confirm the Ensembl gene model, in particular the C-terminal RAEPEEP extension, which no horse, cattle, mouse or human orthologue shares [uniprot-alkal2-orthologs-summary], and the start site, using donkey or horse RNA-seq. One could also test recombinant donkey ALKAL2 on equine ALK and LTK in a cell phosphorylation assay. Second, the active oligomeric state of the native ligand is still unsettled. Human ALKAL2 is a covalent dimer, but non-primate ALKAL2 lacks Cys66, and 2:1 and 2:2 complexes coexist in vitro [reshetnyak-2021-alk-activation-mechanism-fulltext; felix-2025-alk-cryoem-reanalysis-abstract]. Whether non-primate ALKAL2 works mainly as a monomer in vivo, and whether this changes potency or the balance between ALK and LTK, has not been tested. Third, more work is needed on the contribution of heparan sulfate binding to the ALK heparin-binding domain and of ligand–membrane contacts under physiological conditions [demunck-2021-alk-cytokine-structure-fulltext]. Fourth, in mammals the in vivo role of ALKAL2 signalling through LTK, as opposed to ALK, is far less well defined than in zebrafish [mo-2017-zebrafish-iridophore-abstract]. Fifth, the regulators of ALKAL2 secretion and processing are unknown, as are the cell types that make it outside the nervous system in large mammals. Human data point to high expression in the adrenal gland [uniprot-Q6UX46-human-ALKAL2-entry]. Finally, given the metabolic phenotypes in mice, it could be worth asking whether ALKAL2 or ALK variants are linked to body condition or energy balance in equids. The donkey genome resources now available would make such analyses possible [wang-2020-donkey-genomes-summary].

## References

- **uniprot-A0A9L0J5U7-entry** — UniProtKB/TrEMBL entry A0A9L0J5U7_EQUAS, "ALK and LTK ligand 2" (Equus asinus), entry version 15 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0J5U7.txt ; Ensembl ENSEASP00005045397.1.
- **uniprot-Q6UX46-human-ALKAL2-entry** — UniProtKB/Swiss-Prot entry Q6UX46 (ALKL2_HUMAN). https://rest.uniprot.org/uniprotkb/Q6UX46.txt
- **uniprot-alkal2-orthologs-search / uniprot-alkal2-orthologs-summary** — UniProt REST search for ALKAL2 in horse, cattle and mouse (A0A3Q2I4Q6, F6XWZ3, A0A9L0SHF3, A0A3Q2L2L8, A0A3Q1LFV9, Q80UG6). https://rest.uniprot.org/uniprotkb/search?query=gene:ALKAL2+AND+(taxonomy_id:9796+OR+taxonomy_id:10090+OR+taxonomy_id:9913)
- **uniprot-A0A9L0J5U7-summary** — Author's alignment and summary (this work; `alignment.py`, `alignment_output.txt`).
- **wang-2020-donkey-genomes** — Wang C, Li H, Guo Y, et al. Donkey genomes provide new insights into domestication and selection for coat color. Nat Commun 11:6014 (2020). PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7.
- **zhang-2014-ltk-deorphanization** — Zhang H, Pao LI, Zhou A, et al. Deorphanization of the human leukocyte tyrosine kinase (LTK) receptor by a signaling screen of the extracellular proteome. PNAS (2014). PMID: 25331893; PMCID: PMC4226105; DOI: 10.1073/pnas.1412009111.
- **guan-2015-fam150-alk-ligands** — Guan J, Umapathy G, Yamazaki Y, et al. FAM150A and FAM150B are activating ligands for anaplastic lymphoma kinase. eLife (2015). PMID: 26418745; PMCID: PMC4658194; DOI: 10.7554/eLife.09811.
- **reshetnyak-2015-augmentor-ligands** — Reshetnyak AV, Murray PB, Shi X, et al. Augmentor α and β (FAM150) are ligands of the receptor tyrosine kinases ALK and LTK: Hierarchy and specificity of ligand-receptor interactions. PNAS (2015). PMID: 26630010; PMCID: PMC4702955; DOI: 10.1073/pnas.1520099112.
- **reshetnyak-2018-alkal2-active-fragment** — Reshetnyak AV, Mohanty J, Tomé F, et al. Identification of a biologically active fragment of ALK and LTK-Ligand 2 (augmentor-α). PNAS (2018). PMID: 30061385; PMCID: PMC6099872; DOI: 10.1073/pnas.1807881115.
- **mo-2017-zebrafish-iridophore** — Mo ES, Cheng Q, Reshetnyak AV, Schlessinger J, Nicoli S. Alk and Ltk ligands are essential for iridophore development in zebrafish mediated by the receptor tyrosine kinase Ltk. PNAS (2017). PMID: 29078341; PMCID: PMC5692561; DOI: 10.1073/pnas.1710254114.
- **fadeev-2018-alkals-neural-crest** — Fadeev A, Mendoza-Garcia P, Irion U, et al. ALKALs are in vivo ligands for ALK family receptor tyrosine kinases in the neural crest and derived cells. PNAS (2018). PMID: 29317532; PMCID: PMC5789956; DOI: 10.1073/pnas.1719137115.
- **borenas-2021-alkal2-neuroblastoma** — Borenäs M, Umapathy G, Lai WY, et al. ALK ligand ALKAL2 potentiates MYCN-driven neuroblastoma in the absence of ALK mutation. EMBO J (2021). PMID: 33411331; PMCID: PMC7849294; DOI: 10.15252/embj.2020105784.
- **demunck-2021-alk-cytokine-structure** — De Munck S, Provost M, Kurikawa M, et al. Structural basis of cytokine-mediated activation of ALK family receptors. Nature (2021). PMID: 34646012; PMCID: PMC9343967; DOI: 10.1038/s41586-021-03959-5.
- **reshetnyak-2021-alk-activation-mechanism** — Reshetnyak AV, Rossi P, Myasnikov AG, et al. Mechanism for the activation of the anaplastic lymphoma kinase receptor. Nature (2021). PMID: 34819673; PMCID: PMC8639797; DOI: 10.1038/s41586-021-04140-8.
- **felix-2025-alk-cryoem-reanalysis** — Felix J, De Munck S, Bazan JF, Savvides SN. Reanalysis of cryo-EM data reveals ALK-cytokine assemblies with both 2:1 and 2:2 stoichiometries. PLoS Biol (2025). PMID: 40208865; PMCID: PMC12017499; DOI: 10.1371/journal.pbio.3003124.
- **orthofer-2020-alk-thinness** — Orthofer M, Valsesia A, Mägi R, et al. Identification of ALK in Thinness. Cell (2020). PMID: 32442405; DOI: 10.1016/j.cell.2020.04.034.
- **ahmed-2022-hypothalamic-augmentor-alpha** — Ahmed M, Kaur N, Cheng Q, et al. A hypothalamic pathway for Augmentor α-controlled body weight regulation. PNAS (2022). PMID: 35412887; PMCID: PMC9169862; DOI: 10.1073/pnas.2200476119.
- **gueissaz-2026-fam150b-hypothalamus** — Gueissaz L, Sideromenos S, Tretiakov EO, Schnell R, Harkany T. Alk-Fam150b (augmentor α) expression in the paraventricular nucleus of the mouse hypothalamus at molecular resolution, and its sensitivity to acute stress. J Neuroendocrinol (2026). PMID: 41856795; PMCID: PMC13002349; DOI: 10.1111/jne.70159.
- **defaye-2022-alkal2-pain** — Defaye M, Iftinca MC, Gadotti VM, et al. The neuronal tyrosine kinase receptor ligand ALKAL2 mediates persistent pain. J Clin Invest (2022). PMID: 35608912; PMCID: PMC9197515; DOI: 10.1172/JCI154317.
- **mazzeschi-2022-alkal2-autocrine-crc** — Mazzeschi M, Sgarzi M, Romaniello D, et al. The autocrine loop of ALK receptor and ALKAL2 ligand is an actionable target in consensus molecular subtype 1 colon cancer. J Exp Clin Cancer Res (2022). PMID: 35351152; PMCID: PMC8962179; DOI: 10.1186/s13046-022-02309-1.
- **delanne-cumenal-2025-alkal2-colitis-cancer** — Delanne-Cuménal M, Defaye M, Delanne-Cuménal A, et al. Neuronal ALKAL2 and its ALK receptor contribute to the development of colitis-associated colorectal cancer. PNAS (2025). PMID: 40493183; PMCID: PMC12184428; DOI: 10.1073/pnas.2500632122.
- **katic-2023-alk-augmentor-review** — Katic L, Priscan A. Multifaceted Roles of ALK Family Receptors and Augmentor Ligands in Health and Disease: A Comprehensive Review. Biomolecules (2023). PMID: 37892172; PMCID: PMC10605310; DOI: 10.3390/biom13101490.


## Citations

1. ahmed-2022-hypothalamic-augmentor-alpha-abstract.md
2. ahmed-2022-hypothalamic-augmentor-alpha-fulltext.txt
3. ahmed-2022-hypothalamic-augmentor-alpha-summary.md
4. borenas-2021-alkal2-neuroblastoma-abstract.md
5. borenas-2021-alkal2-neuroblastoma-fulltext.txt
6. borenas-2021-alkal2-neuroblastoma-summary.md
7. defaye-2022-alkal2-pain-abstract.md
8. defaye-2022-alkal2-pain-fulltext.txt
9. defaye-2022-alkal2-pain-summary.md
10. delanne-cumenal-2025-alkal2-colitis-cancer-abstract.md
11. delanne-cumenal-2025-alkal2-colitis-cancer-fulltext.txt
12. delanne-cumenal-2025-alkal2-colitis-cancer-summary.md
13. demunck-2021-alk-cytokine-structure-abstract.md
14. demunck-2021-alk-cytokine-structure-fulltext.txt
15. demunck-2021-alk-cytokine-structure-summary.md
16. fadeev-2018-alkals-neural-crest-abstract.md
17. fadeev-2018-alkals-neural-crest-fulltext.txt
18. fadeev-2018-alkals-neural-crest-summary.md
19. felix-2025-alk-cryoem-reanalysis-abstract.md
20. felix-2025-alk-cryoem-reanalysis-fulltext.txt
21. felix-2025-alk-cryoem-reanalysis-summary.md
22. guan-2015-fam150-alk-ligands-abstract.md
23. guan-2015-fam150-alk-ligands-fulltext.txt
24. guan-2015-fam150-alk-ligands-summary.md
25. gueissaz-2026-fam150b-hypothalamus-abstract.md
26. gueissaz-2026-fam150b-hypothalamus-fulltext.txt
27. gueissaz-2026-fam150b-hypothalamus-summary.md
28. katic-2023-alk-augmentor-review-abstract.md
29. katic-2023-alk-augmentor-review-fulltext.txt
30. katic-2023-alk-augmentor-review-summary.md
31. mazzeschi-2022-alkal2-autocrine-crc-abstract.md
32. mazzeschi-2022-alkal2-autocrine-crc-fulltext.txt
33. mazzeschi-2022-alkal2-autocrine-crc-summary.md
34. mo-2017-zebrafish-iridophore-abstract.md
35. mo-2017-zebrafish-iridophore-summary.md
36. orthofer-2020-alk-thinness-abstract.md
37. orthofer-2020-alk-thinness-summary.md
38. reshetnyak-2015-augmentor-ligands-abstract.md
39. reshetnyak-2015-augmentor-ligands-summary.md
40. reshetnyak-2018-alkal2-active-fragment-abstract.md
41. reshetnyak-2018-alkal2-active-fragment-summary.md
42. reshetnyak-2021-alk-activation-mechanism-abstract.md
43. reshetnyak-2021-alk-activation-mechanism-fulltext.txt
44. reshetnyak-2021-alk-activation-mechanism-summary.md
45. uniprot-A0A9L0J5U7-entry.fasta
46. uniprot-A0A9L0J5U7-entry.txt
47. uniprot-A0A9L0J5U7-summary.md
48. uniprot-Q6UX46-human-ALKAL2-entry.fasta
49. uniprot-Q6UX46-human-ALKAL2-entry.txt
50. uniprot-alkal2-orthologs-search.tsv
51. uniprot-alkal2-orthologs-summary.md
52. wang-2020-donkey-genomes-abstract.md
53. wang-2020-donkey-genomes-fulltext.txt
54. wang-2020-donkey-genomes-summary.md
55. zhang-2014-ltk-deorphanization-abstract.md
56. zhang-2014-ltk-deorphanization-summary.md