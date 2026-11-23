---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T02:57:10.451820'
end_time: '2026-10-26T03:10:04.713229'
duration_seconds: 774.26
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: IRAK3
  gene_symbol: IRAK3
  uniprot_accession: A0A3Q2HDT6
  protein_description: 'SubName: Full=Interleukin 1 receptor associated kinase 3 {ECO:0000313|Ensembl:ENSECAP00000031356.2};'
  gene_info: Name=IRAK3 {ECO:0000313|VGNC:VGNC:19127};
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the protein kinase superfamily. TKL Ser/Thr
  protein_domains: DEATH-like_dom_sf. (IPR011029); Death_dom. (IPR000488); Kinase-like_dom_sf.
    (IPR011009); Prot_kinase_dom. (IPR000719); Death (PF00531)
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
citation_count: 70
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A3Q2HDT6
- **Protein Description:** SubName: Full=Interleukin 1 receptor associated kinase 3 {ECO:0000313|Ensembl:ENSECAP00000031356.2};
- **Gene Information:** Name=IRAK3 {ECO:0000313|VGNC:VGNC:19127};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the protein kinase superfamily. TKL Ser/Thr
- **Key Domains:** DEATH-like_dom_sf. (IPR011029); Death_dom. (IPR000488); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719); Death (PF00531)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "IRAK3" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'IRAK3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **IRAK3** (gene ID: IRAK3, UniProt: A0A3Q2HDT6) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# IRAK3 (IRAK-M) in the horse, *Equus caballus* (UniProt A0A3Q2HDT6): function, localization and pathway role

## 1. Introduction and summary

UniProt A0A3Q2HDT6 is an unreviewed (TrEMBL) horse protein of 567 residues, annotated as "Interleukin 1 receptor associated kinase 3" and encoded by the gene *IRAK3* (VGNC:19127) on horse chromosome 6. It comes from the Thoroughbred reference genome [wade-2009-horse-genome-abstract]. The identity is not in doubt. The gene symbol, the description, the Pelle-subfamily TKL Ser/Thr kinase classification and the domain composition (an N-terminal death domain, Pfam PF00531, followed by a protein-kinase-like domain) all match the well-studied mammalian IRAK3, also called IRAK-M. In this session the horse sequence aligned to human IRAK3 (Q9Y616) at 80.5% identity, which is higher than the human–mouse identity of 76.2% (see `analysis/SEQUENCE_ANALYSIS.md`). No mechanistic study of IRAK3 protein in the horse was found. Horse-specific evidence is limited to transcriptomic and population-genomic studies, plus the sequence and structure-model analyses done here. In horse tenocytes IL-1β induces *IRAK3* [beaumont-2024-equine-tenocyte-il1b-fulltext]. *IRAK3* also turns up in transcriptome studies of equine asthma and foal immunity [padoan-2022-equine-asthma-immunotranscriptome-fulltext; tallmadge-2018-foal-pbmc-transcriptome-fulltext]. It lies next to *HMGA2* in an ECA6 region linked to pony height and insulin [norton-2019-hmga2-irak3-ponies-fulltext]. Everything said here about molecular function therefore comes from orthology with human and mouse IRAK-M.

IRAK-M was found as a new member of the Pelle/IRAK family that is expressed mainly in monomyeloid cells. It has negligible autophosphorylation activity [wesche-1999-irakm-abstract]. Its main physiological role, established in knockout mice, is as an inducible negative-feedback regulator of Toll-like receptor (TLR) and IL-1 receptor (IL-1R) signalling. It is induced by TLR stimulation and holds IRAK1 and IRAK4 on MyD88, which prevents formation of the IRAK1–TRAF6 complex. Without it, cytokine production increases and endotoxin tolerance is impaired [kobayashi-2002-irakm-negative-regulator-abstract]. IRAK-M is a pseudokinase, not an enzyme with a confirmed protein-phosphotransferase activity. Its catalytic HRD motif is replaced by "CGS" and its DFG motif by "DFA" [lange-2021-irak3-dimer-structure-fulltext]. It acts mainly as an adaptor/scaffold inside the cytoplasmic Myddosome. There it can (i) block IRAK1/IRAK2-dependent signalling and (ii) form its own MyD88–IRAK4–IRAK-M Myddosome, which drives a MEKK3-dependent "second wave" of NF-κB activation. That second wave favours transcription of inhibitory genes such as SOCS1, SHIP1, A20 and IκBα [zhou-2013-irakm-mekk3-abstract]. The protein is mostly cytoplasmic, with a smaller nuclear pool [turek-2023-irak3-localization-fulltext; nechama-2018-il33-pin1-irakm-abstract].

One feature specific to this accession needs to be stated at the outset. A0A3Q2HDT6 is an N-terminally truncated isoform of the horse IRAK3 gene. A full-length horse model, F6QZW8 (614 aa; RefSeq XP_023499869.1), comes from the same Ensembl gene (ENSECAG00000026958). A0A3Q2HDT6 is identical to residues 51–614 of F6QZW8 except for its first three residues. So the isoform lacks roughly the first 45 residues of the death domain, including the region equivalent to human D19–A23 (analysis in this session). In human IRAK-M that region is needed for its inhibitory activity in some contexts [du-2014-irakm-death-domain-fulltext].

## 2. Identity, gene model and evolutionary context

Three horse UniProt entries map to one Ensembl gene, ENSECAG00000026958: A0A3Q2HDT6 (567 aa), F6QZW8 (614 aa) and A0A5F5PKF5 (553 aa). F6QZW8 has a full-length death domain and lines up with human IRAK3 from its N-terminus. A0A5F5PKF5/XP_023499870.1 lacks an internal block that covers much of the death domain. A0A3Q2HDT6 starts with "MIT" and joins the shared sequence at a position equivalent to human residue ~46 (ERLSSSWLDV…). All three share the pseudokinase domain and C-terminal region exactly. They also share a 13-residue C-terminal extension (…KKEAISPEDKEESKYC) that human IRAK3 does not have (this session's MAFFT alignment). These isoforms are computational predictions (UniProt PE level 3, "inferred from homology"). Whether the truncated isoform is actually expressed as a protein in horse tissues has not been tested.

The IRAK family evolved by vertebrate expansion. Vertebrates have an IRAK4 lineage and an IRAK1/2/3 lineage. In mammals IRAK1 and IRAK2 (with IRAK4) enhance signalling, and IRAK3 represses it [weng-2024-zebrafish-irak3-abstract]. The truncated isoform is relevant here. In zebrafish, the full-length IRAK3a variant (death domain + pseudokinase + TRAF6-binding region) is a mild positive regulator. The truncated IRAK3b variant is purely inhibitory and competes for MyD88 and TRAF6 [weng-2024-zebrafish-irak3-abstract]. So domain architecture can change the sign of IRAK3 output, and alternative isoforms such as A0A3Q2HDT6 may not have exactly the same function as the full-length protein. Within mammals, mouse and human IRAK-M are 71% identical and behave similarly in signalling assays, which supports transferring function across orthologs [rosati-2002-murine-irakm-abstract].

## 3. Domain architecture and the pseudokinase

IRAK-M has three parts. There is an N-terminal death domain (DD) that mediates Myddosome assembly, a central pseudokinase domain, and an unstructured C-terminal domain that carries a TRAF6-binding motif [du-2014-irakm-death-domain-fulltext; freihat-2019-irak3-guanylate-cyclase-fulltext]. The crystal structure of the human IRAK3 pseudokinase domain shows a closed, "pseudoactive" conformation. In IRAK3 the canonical catalytic "HRD" motif is missing entirely and is replaced by "CGS". The Mg²⁺-binding "DFG" motif becomes "DFA". A conserved cysteine sits in the regulatory spine. The domain forms an unusual head-to-head dimer around the αC-helices, stabilized by disulfide bonds between C202 and C287 [lange-2021-irak3-dimer-structure-fulltext]. A commentary on that structure described this as a new form of kinase/pseudokinase allostery by which IRAK3 might dampen IRAK4 [horne-2021-irak3-preview-abstract].

The horse protein keeps every one of these features. When mapped by alignment, the horse equivalents are CGS at positions 249–251 of A0A3Q2HDT6, DFA at 269–271, the dimer-forming cysteines C160 and C245, and the interface glutamate E172 (human E214). The C-lobe surface residues L358 and R387 are also present. They correspond to human L400 and R429, where asthma-associated variants cluster and where an IRAK3–IRAK4 interaction surface has been proposed [lange-2021-irak3-dimer-structure-fulltext]. The VAIK-equivalent lysine (horse K150) is retained, but the catalytic aspartate is not. On the structural evidence, horse IRAK3 should be treated as a catalytically inactive pseudokinase. Any IEA annotation to "protein serine/threonine kinase activity" (for example the Ensembl-derived GO:0004674 on F6QZW8) is probably over-annotation. The discovery paper did report negligible autophosphorylation [wesche-1999-irakm-abstract]. An early mouse study also mentioned kinase activity comparable to the human protein [rosati-2002-murine-irakm-abstract], so the question is not fully closed for overexpressed protein.

A non-canonical enzymatic activity has been proposed. Freihat and colleagues reported that a guanylate cyclase (GC) centre inside the pseudokinase domain lets IRAK3 make cGMP. In their work, an R372L mutation lowered cGMP production and abolished IRAK3's suppression of LPS-induced NF-κB in a TLR4 reporter line, and cell-permeable cGMP rescued the effect [freihat-2019-irak3-guanylate-cyclase-fulltext]. Follow-up mutagenesis of residues around this centre (S359, G361, R372, D377, D385) showed that GC-impaired mutants do not rescue IRAK3-knockout THP-1 monocytes unless a cGMP analogue is added [turek-2023-irak3-localization-fulltext]. Horse IRAK3 keeps S317, G319 and D343 at the equivalent positions and has conservative substitutions at the other two sites (K330 for R372 and E335 for D377). Whether horse IRAK3 is a guanylate cyclase therefore cannot be decided from sequence alone. The activity itself comes so far from one research group and has not been reconciled with the pseudokinase structure. It should be treated as provisional.

## 4. Death-domain interactions and Myddosome assembly

After TLR/IL-1R activation, MyD88 death domains assemble into a left-handed helical "Myddosome" tower. In this structure MyD88 recruits IRAK4, and the MyD88–IRAK4 platform then recruits IRAK2 or IRAK1. The kinase domains are brought together so that they can be phosphorylated [lin-2010-myddosome-abstract]. IRAK-M enters this assembly through its own DD. Mutational and modelling studies of the human IRAK-M DD found three functional surfaces [gurkan-2023-irakm-death-domain-review-fulltext]. Surface 1 is centred on Trp74 and binds MyD88/IRAK4. Surface 2 is centred on Lys60 and lets IRAK-M form a homotetramer under the MyD88/IRAK4 scaffold. Surface 3 is centred on Arg97. It does not contact MyD88/IRAK4 but is needed for IRAK-M's interaction with IRAK1 and TRAF6 and for about half of the NF-κB output of the IRAK-M Myddosome. Earlier work had shown that W74 is needed for most of IRAK-M's inhibition of TLR2/4-driven cytokines in macrophages. In lung epithelial cells, inhibition of TLR5-driven IL-8 needed instead the D19–A23 stretch and R70, which carry predicted IRAK2 contact points [du-2014-irakm-death-domain-fulltext]. One structural caution applies. A published NMR structure of the IRAK-M DD (PDB 5UKE) has validation anomalies, so models built on it should be treated carefully [poelman-2022-irakm-nmr-anomalies-abstract].

For the horse isoform, the alignment shows that K60, R70, W74 and R97 are all conserved (horse K18, R28, W32 and R55). The D19–A23 segment is not present, because A0A3Q2HDT6 starts downstream of it. The first α-helix of the six-helix death-domain fold also appears to be missing. A0A3Q2HDT6 may therefore keep the MyD88/IRAK4-binding (W74) and IRAK1/TRAF6-related (R97) surfaces while losing a determinant needed for epithelial TLR5 inhibition. This is an inference from sequence only and would need testing; it is also possible that the truncated death domain does not fold properly. The AlphaFold DB models (v6, retrieved in this session) give some support to that concern. In the full-length isoform F6QZW8, the death-domain region (residues 11–112) is predicted with moderate-to-good confidence (mean pLDDT 74.7 for residues 11–62 and 80.3 for 63–112). In A0A3Q2HDT6 the matching remnant (residues 1–65) scores lower (61.4 for 1–15 and 69.7 for 16–65). The pseudokinase domain is predicted with high confidence in both models (mean pLDDT 89.5 and 89.0). The DD–kinase linker (pLDDT ~45) and the C-terminal region (pLDDT ~29) are predicted to be disordered in both, as expected for the unstructured C-terminal domain that carries the TRAF6 motif (`analysis/SEQUENCE_ANALYSIS.md`). The full-length isoform F6QZW8 has the complete death domain.

## 5. Signalling pathway role: negative feedback and the "second wave"

The core function of IRAK-M is to limit MyD88-dependent signalling. In Irak3-/- mice, TLR or IL-1 stimulation and bacterial challenge cause increased cytokine production in cells and increased inflammation in animals. Mechanistically, IRAK-M stops IRAK1 and IRAK4 from dissociating from MyD88, so the IRAK1–TRAF6 complex that activates TAK1, NF-κB and MAP kinases does not form [kobayashi-2002-irakm-negative-regulator-abstract]. Later work refined this picture. IRAK-M can assemble a MyD88–IRAK4–IRAK-M Myddosome that signals through MEKK3 rather than TAK1, producing a delayed second wave of NF-κB activity. This wave is uncoupled from post-transcriptional (mRNA stability and translation) control. As a result it mainly induces inhibitory molecules such as SOCS1, SHIP1, A20 and IκBα. Separately, IRAK-M binds IRAK2 and suppresses translation of TLR7-induced cytokines and chemokines [zhou-2013-irakm-mekk3-abstract]. The overall effect is anti-inflammatory, even though part of the mechanism activates NF-κB. Death-domain mutagenesis matches this. W74 is needed both for IRAK-M's intrinsic NF-κB activation (including A20 transcription) and for its inhibitory function. The C-terminal TRAF6-binding motif P478VEDDE483 contributes to IL-8 output [du-2014-irakm-death-domain-fulltext]. In the horse sequence this motif is P436VENDE441, which still fits the PxExx-acidic TRAF6-binding consensus.

A further structural model proposes direct allosteric inhibition of IRAK4. A conserved C-lobe surface of the IRAK3 pseudokinase looks like the IRAK4 homodimer interface, which suggests that IRAK3–IRAK4 heterodimers could block IRAK4 activation [lange-2021-irak3-dimer-structure-fulltext]. The proposed cGMP mechanism would add a small-molecule output that suppresses NF-κB [freihat-2019-irak3-guanylate-cyclase-fulltext].

In mammals the pathway output that depends most on IRAK-M is endotoxin (LPS) tolerance. After LPS exposure, monocytes and macrophages become refractory to a second challenge. In Irak3-/- cells this tolerance is markedly reduced [kobayashi-2002-irakm-negative-regulator-abstract]. In human monocytes, tolerant cells and cells from septic patients induce IRAK-M much faster on re-challenge, and PI3K signalling modulates this induction [escoll-2003-irakm-endotoxin-abstract]. In experimental human endotoxemia, LPS tolerance goes along with IRAK-M up-regulation, which is largely TNF-dependent in vitro [vantveer-2007-irakm-human-endotoxemia-abstract].

IRAK-M is also a transcriptional target of anti-inflammatory signals. Glucocorticoids induce it through cooperative binding of the glucocorticoid receptor and NF-κB p65 to the IRAK-M promoter. In mice, the protective effect of glucocorticoids against bacterial lung inflammation is lost without IRAK-M [miyata-2015-glucocorticoid-irakm-abstract]. The wider literature on infection and immune homeostasis has been reviewed elsewhere [hubbard-2010-irakm-review-abstract]. These findings bear on equine medicine, where endotoxaemia and glucocorticoid therapy are common, but none of them has been tested in horses. The only equine IRAK-pathway study found blocked IRAK4 pharmacologically in IL-1β-treated tenocytes and saw partial rescue of collagen contraction and IL-6 production [beaumont-2025-equine-irak4-abstract]. That result shows the IL-1R/MyD88/IRAK axis works in horse cells but says nothing directly about IRAK3.

## 6. Expression and subcellular localization

Human IRAK-M was first described as restricted mainly to cells of monomyeloid origin [wesche-1999-irakm-abstract], and its expression rises after TLR stimulation [kobayashi-2002-irakm-negative-regulator-abstract]. Later studies found it in lung and other epithelial cells as well. Expression in mouse is broader, including neutrophils, B cells and intestinal, lung and biliary epithelium [hubbard-2010-irakm-review-fulltext]. For the horse, an automated Bgee record in UniProt lists expression in liver and 21 other tissues or cell types. Several equine transcriptome studies give more specific, if indirect, information. In equine superficial digital flexor tenocytes in 3D collagen culture, IL-1β switched on NF-κB signalling. *IRAK3* was among the 133 genes that IL-1β induced in both the equine and a rat tenocyte model, alongside *NFKBIA*, *NFKBIZ*, *IL6* and *IL1A* [beaumont-2024-equine-tenocyte-il1b-fulltext]. This fits the feedback-gene behaviour of mammalian IRAK-M and shows it can be induced in a non-myeloid horse cell type. In bronchoalveolar lavage cells from horses with severe equine asthma, gene-set enrichment highlighted the asthma and NF-κB pathways. The authors singled out *IRAK3* among the frequent genes of the enriched asthma gene set and noted its status as a human asthma susceptibility candidate [padoan-2022-equine-asthma-immunotranscriptome-fulltext]. In peripheral blood mononuclear cells, *IRAK3* was among the genes whose expression fell significantly between day 1 and day 42 of foal life (listed under the MAPK cascade category). The authors read the neonatal profile as dominated by innate-immune genes, with an overlay of immunosuppressive ones [tallmadge-2018-foal-pbmc-transcriptome-fulltext]. All three are high-throughput observations of mRNA. None measured IRAK3 protein or distinguished the isoforms.

Inside the cell, IRAK3 works where the Myddosome forms, on the cytoplasmic face of activated TLR/IL-1R complexes. It has been described as a cytoplasmic protein [freihat-2019-irak3-guanylate-cyclase-fulltext]. With eGFP tagging in HEK293T cells, wild-type IRAK3 is mainly cytoplasmic with a smaller nuclear fraction. One GC-centre double mutant (S359L/G361L) was largely excluded from the nucleus. The same study cites reports that in resting macrophages a substantial share of IRAK3 sits near the plasma membrane in detergent-resistant membranes [turek-2023-irak3-localization-fulltext]. A regulated nuclear pool has also been shown. In IL-33-stimulated dendritic cells, IRAK1 phosphorylates IRAK-M at Ser110. The prolyl isomerase PIN1 then binds and isomerizes the pS110–P111 motif, which promotes IRAK-M nuclear translocation and induction of selected genes (IL6, CSF3, CXCL2, CCL5) [nechama-2018-il33-pin1-irakm-abstract; nechama-2018-il33-pin1-irakm-fulltext]. In the horse protein, the residue at the position equivalent to human S110 is asparagine (N68–P69), whereas mouse has threonine (T–P). So this particular PIN1 regulatory site does not appear to be conserved in horse IRAK3. The horse protein may lack this route to nuclear translocation, or may use another site. This is an untested prediction from the sequence. The annotations most consistent with the evidence are cytoplasm, specifically the cytosolic face of the receptor-proximal Myddosome, as the primary site of action, with a minor regulated nuclear pool. Both cytoplasm and nucleus are already annotated by UniProt rules on the full-length horse entry F6QZW8.

## 7. Genomic context of IRAK3 in the horse

Horse *IRAK3* is on equine chromosome 6 (ECA6), next to *HMGA2*. Human *IRAK3* is on 12q14 [hubbard-2010-irakm-review-fulltext], which matches the conserved synteny between the two genomes. This neighbourhood has drawn attention in equine genetics. In Welsh ponies, genome-wide association and haplotype analyses found a ~1.3 Mb ECA6 region with a shared ancestral haplotype for both height and baseline insulin. The region accounted for about 40% of the heritability of height and 20% of that of insulin. *HMGA2* and *IRAK3* were ranked as the two biological positional candidates. *IRAK3* was chosen because IRAK3 is down-regulated in human obesity and metabolic syndrome and because *Irak3*-mutant mice have skeletal and glucose-tolerance phenotypes. Sanger sequencing of *IRAK3* promoters and coding exons in a 51-horse panel spanning several breeds found no variants. The functional candidate became the *HMGA2* p.G28E variant [norton-2019-hmga2-irak3-ponies-fulltext]. The skeletal link has support in mouse: IRAK-M-deficient mice develop severe osteoporosis because IL-1R/TLR signalling hyperactivates osteoclasts [li-2005-irakm-osteoclast-abstract]. Two population-genomic studies picked up the same block. One found runs-of-homozygosity islands containing *HMGA2*, *LLPH*, *IRAK3* and *HELB* in Exmoor ponies and Gidran horses [grilzseger-2019-horse-roh-fulltext]. The other found a selection-signature peak on ECA6 that includes *IRAK3*, *HMGA2* and *CAND1* in Chinese Mongolian horse breeds [mongolian-2023-selection-hoof-fulltext]. In all of these studies *IRAK3* is a positional passenger near a strong *HMGA2* signal, and no evidence yet shows that equine *IRAK3* variation is functional. The pony data do show that the coding sequence of horse *IRAK3* was conserved in the panel sequenced, which supports orthology-based transfer of function.

## 8. Implications for functional annotation of A0A3Q2HDT6

Taken together, the evidence supports annotating horse IRAK3 by orthology as a non-catalytic (pseudokinase) negative regulator of MyD88-dependent TLR and IL-1R signalling. Its molecular role is that of a death-domain adaptor that binds MyD88–IRAK4 in the Myddosome. It acts in the cytoplasm, mainly in monocytes and macrophages, and it contributes to endotoxin tolerance. Suitable GO-style terms would include negative regulation of the Toll-like receptor and IL-1-mediated signalling pathways, negative regulation of canonical NF-κB signal transduction, protein homodimerization activity (pseudokinase head-to-head dimer), and protein kinase binding (IRAK1/IRAK4). These are supported by mammalian experimental data [kobayashi-2002-irakm-negative-regulator-abstract; zhou-2013-irakm-mekk3-abstract; lange-2021-irak3-dimer-structure-fulltext]. Annotation to catalytic protein Ser/Thr kinase activity is not supported by the structural evidence. Guanylate cyclase activity remains a provisional proposal [freihat-2019-irak3-guanylate-cyclase-fulltext]. Annotations that depend on the N-terminal death-domain region, or on the S110 PIN1 site, should be applied cautiously to this truncated isoform.

## Open Questions

Whether the A0A3Q2HDT6 transcript (Ensembl ENSECAT00000032597) is really expressed, and in which equine cells, has not been shown. RNA-seq junction support for its alternative first exon, followed by protein-level detection, would settle whether it is a real isoform or a gene-model artefact. If it is real, it would be worth testing whether the N-terminally truncated death domain still folds and binds MyD88/IRAK4. If it does, the isoform could be a dominant inhibitor, like truncated zebrafish IRAK3b [weng-2024-zebrafish-irak3-abstract]. If it does not, it may lose inhibitory capacity in the TLR5/epithelial context that depends on D19–A23 [du-2014-irakm-death-domain-fulltext].

Several other questions are open. It is not known whether IRAK3 induction underlies endotoxin tolerance in equine monocytes, as it does in human and mouse [escoll-2003-irakm-endotoxin-abstract; kobayashi-2002-irakm-negative-regulator-abstract]. That question matters clinically for equine endotoxaemia and laminitis. A related question is whether glucocorticoids induce equine IRAK3 [miyata-2015-glucocorticoid-irakm-abstract]. The horse-specific asparagine at the S110 PIN1 site raises a further question: is IL-33/PIN1-driven nuclear translocation of IRAK3 absent in horse, or does another phosphosite take over [nechama-2018-il33-pin1-irakm-fulltext]? The 13-residue horse-specific C-terminal extension has no assigned function. At the population level, whether *IRAK3* regulatory variation on the *HMGA2*-linked ECA6 haplotype changes IRAK3 expression in equine macrophages could be tested, for example with allele-specific expression. That would show whether IRAK3 adds to the insulin-dysregulation signal attributed so far to *HMGA2* [norton-2019-hmga2-irak3-ponies-fulltext]. The induction of *IRAK3* in equine asthma and in IL-1β-stimulated tenocytes should be confirmed at the protein level, by isoform [padoan-2022-equine-asthma-immunotranscriptome-fulltext; beaumont-2024-equine-tenocyte-il1b-fulltext]. For the family as a whole, the guanylate cyclase activity needs independent confirmation and a structural explanation within the pseudokinase fold [freihat-2019-irak3-guanylate-cyclase-fulltext; lange-2021-irak3-dimer-structure-fulltext]. The proposed IRAK3–IRAK4 C-lobe heterodimer also still needs direct structural evidence. Finally, an AlphaFold-multimer model of the horse protein with equine MyD88 and IRAK4 would be a cheap first test of the predictions above.

## References

- **wade-2009-horse-genome** — Wade CM, Giulotto E, Sigurdsson S, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science* 2009;326:865-867. PMID: 19892987; PMCID: PMC3785132; DOI: 10.1126/science.1178158. https://pubmed.ncbi.nlm.nih.gov/19892987/
- **wesche-1999-irakm** — Wesche H, Gao X, Li X, Kirschning CJ, Stark GR, Cao Z. IRAK-M is a novel member of the Pelle/interleukin-1 receptor-associated kinase (IRAK) family. *J Biol Chem* 1999;274(27):19403-10. PMID: 10383454; DOI: 10.1074/jbc.274.27.19403. https://pubmed.ncbi.nlm.nih.gov/10383454/
- **kobayashi-2002-irakm-negative-regulator** — Kobayashi K, Hernandez LD, Galán JE, Janeway CA Jr, Medzhitov R, Flavell RA. IRAK-M is a negative regulator of Toll-like receptor signaling. *Cell* 2002;110(2):191-202. PMID: 12150927; DOI: 10.1016/s0092-8674(02)00827-9. https://pubmed.ncbi.nlm.nih.gov/12150927/
- **rosati-2002-murine-irakm** — Rosati O, Martin MU. Identification and characterization of murine IRAK-M. *Biochem Biophys Res Commun* 2002;293(5):1472-7. PMID: 12054681; DOI: 10.1016/S0006-291X(02)00411-4. https://pubmed.ncbi.nlm.nih.gov/12054681/
- **lin-2010-myddosome** — Lin SC, Lo YC, Wu H. Helical assembly in the MyD88-IRAK4-IRAK2 complex in TLR/IL-1R signalling. *Nature* 2010;465(7300):885-90. PMID: 20485341; PMCID: PMC2888693; DOI: 10.1038/nature09121. https://pubmed.ncbi.nlm.nih.gov/20485341/
- **zhou-2013-irakm-mekk3** — Zhou H, Yu M, Fukuda K, et al. IRAK-M mediates Toll-like receptor/IL-1R-induced NFκB activation and cytokine production. *EMBO J* 2013;32(4):583-96. PMID: 23376919; PMCID: PMC3579143; DOI: 10.1038/emboj.2013.2. https://pubmed.ncbi.nlm.nih.gov/23376919/
- **du-2014-irakm-death-domain** — Du J, Nicolaes GA, Kruijswijk D, et al. The structure function of the death domain of human IRAK-M. *Cell Commun Signal* 2014;12:77. PMID: 25481771; PMCID: PMC4273448; DOI: 10.1186/s12964-014-0077-3. https://pubmed.ncbi.nlm.nih.gov/25481771/
- **lange-2021-irak3-dimer-structure** — Lange SM, Nelen MI, Cohen P, Kulathu Y. Dimeric structure of the pseudokinase IRAK3 suggests an allosteric mechanism for negative regulation. *Structure* 2021;29(3):238-251.e4. PMID: 33238146; PMCID: PMC7955167; DOI: 10.1016/j.str.2020.11.004. https://pubmed.ncbi.nlm.nih.gov/33238146/
- **horne-2021-irak3-preview** — Horne CR, Murphy JM. For whom the bell tolls: the structure of the dead kinase, IRAK3. *Structure* 2021;29(3):197-199. PMID: 33667374; DOI: 10.1016/j.str.2021.01.011. https://pubmed.ncbi.nlm.nih.gov/33667374/
- **freihat-2019-irak3-guanylate-cyclase** — Freihat LA, Wheeler JI, Wong A, Turek I, Manallack DT, Irving HR. IRAK3 modulates downstream innate immune signalling through its guanylate cyclase activity. *Sci Rep* 2019;9:15468. PMID: 31664109; PMCID: PMC6820782; DOI: 10.1038/s41598-019-51913-3. https://pubmed.ncbi.nlm.nih.gov/31664109/
- **turek-2023-irak3-localization** — Turek I, Nguyen TH, Galea C, et al. Mutations in the vicinity of the IRAK3 guanylate cyclase center impact its subcellular localization and ability to modulate inflammatory signaling in immortalized cell lines. *Int J Mol Sci* 2023;24(10):8572. PMID: 37239919; PMCID: PMC10217915; DOI: 10.3390/ijms24108572. https://pubmed.ncbi.nlm.nih.gov/37239919/
- **gurkan-2023-irakm-death-domain-review** — Gürkan B, Poelman H, Pereverzeva L, et al. The IRAK-M death domain: a tale of three surfaces. *Front Mol Biosci* 2024 (eCollection 2023);10:1265455. PMID: 38268724; PMCID: PMC10806146; DOI: 10.3389/fmolb.2023.1265455. https://pubmed.ncbi.nlm.nih.gov/38268724/
- **poelman-2022-irakm-nmr-anomalies** — Poelman H, Ippel H, Gürkan B, et al. Structural anomalies in a published NMR-derived structure of IRAK-M. *J Mol Graph Model* 2022;111:108061. PMID: 34837785; DOI: 10.1016/j.jmgm.2021.108061. https://pubmed.ncbi.nlm.nih.gov/34837785/
- **nechama-2018-il33-pin1-irakm** — Nechama M, Kwon J, Wei S, et al. The IL-33-PIN1-IRAK-M axis is critical for type 2 immunity in IL-33-induced allergic airway inflammation. *Nat Commun* 2018;9:1603. PMID: 29686383; PMCID: PMC5913134; DOI: 10.1038/s41467-018-03886-6. https://pubmed.ncbi.nlm.nih.gov/29686383/
- **hubbard-2010-irakm-review** — Hubbard LL, Moore BB. IRAK-M regulation and function in host defense and immune homeostasis. *Infect Dis Rep* 2010;2(1):e9. PMID: 21390243; PMCID: PMC3049547; DOI: 10.4081/idr.2010.e9. https://pubmed.ncbi.nlm.nih.gov/21390243/
- **escoll-2003-irakm-endotoxin** — Escoll P, del Fresno C, García L, et al. Rapid up-regulation of IRAK-M expression following a second endotoxin challenge in human monocytes and in monocytes isolated from septic patients. *Biochem Biophys Res Commun* 2003;311(2):465-72. PMID: 14592437; DOI: 10.1016/j.bbrc.2003.10.019. https://pubmed.ncbi.nlm.nih.gov/14592437/
- **vantveer-2007-irakm-human-endotoxemia** — van 't Veer C, van den Pangaart PS, van Zoelen MA, et al. Induction of IRAK-M is associated with lipopolysaccharide tolerance in a human endotoxemia model. *J Immunol* 2007;179(10):7110-20. PMID: 17982103; DOI: 10.4049/jimmunol.179.10.7110. https://pubmed.ncbi.nlm.nih.gov/17982103/
- **miyata-2015-glucocorticoid-irakm** — Miyata M, Lee JY, Susuki-Miyata S, et al. Glucocorticoids suppress inflammation via the upregulation of negative regulator IRAK-M. *Nat Commun* 2015;6:6062. PMID: 25585690; PMCID: PMC4309435; DOI: 10.1038/ncomms7062. https://pubmed.ncbi.nlm.nih.gov/25585690/
- **weng-2024-zebrafish-irak3** — Weng P, Lan M, Zhang H, et al. Both IRAK3 and IRAK1 activate the MyD88-TRAF6 pathway in zebrafish. *J Immunol* 2024;213(3):362-372. PMID: 38847613; DOI: 10.4049/jimmunol.2400054. https://pubmed.ncbi.nlm.nih.gov/38847613/
- **beaumont-2025-equine-irak4** — Beaumont RE, Flood C, Guest DJ. Inhibition of interleukin-1 receptor-associated kinase (IRAK)-4 provides partial rescue of interleukin-1 beta induced functional and gene expression changes in equine tenocytes. *Mol Biol Rep* 2025;53(1):54. PMID: 41196436; PMCID: PMC12592280; DOI: 10.1007/s11033-025-11219-2. https://pubmed.ncbi.nlm.nih.gov/41196436/

- **beaumont-2024-equine-tenocyte-il1b** — Beaumont RE, et al. Exogenous interleukin-1 beta stimulation regulates equine tenocyte function and gene expression in three-dimensional culture which can be rescued by pharmacological inhibition of interleukin 1 receptor, but not nuclear factor kappa B, signaling. *Mol Cell Biochem* 2024;479(5):1059-1078. PMID: 37314623; PMCID: PMC11116237; DOI: 10.1007/s11010-023-04779-z. https://pubmed.ncbi.nlm.nih.gov/37314623/
- **padoan-2022-equine-asthma-immunotranscriptome** — Padoan E, Ferraresso S, Pegolo S, Barnini C, Castagnaro M, Bargelloni L. Gene expression profiles of the immuno-transcriptome in equine asthma. *Animals (Basel)* 2022;13(1):4. PMID: 36611613; PMCID: PMC9817691; DOI: 10.3390/ani13010004. https://pubmed.ncbi.nlm.nih.gov/36611613/
- **tallmadge-2018-foal-pbmc-transcriptome** — Tallmadge RL, Wang M, Sun Q, Felippe MJB. Transcriptome analysis of immune genes in peripheral blood mononuclear cells of young foals and adult horses. *PLoS One* 2018;13(9):e0202646. PMID: 30183726; PMCID: PMC6124769; DOI: 10.1371/journal.pone.0202646. https://pubmed.ncbi.nlm.nih.gov/30183726/
- **norton-2019-hmga2-irak3-ponies** — Norton EM, Avila F, Schultz NE, Mickelson JR, Geor RJ, McCue ME. Evaluation of an HMGA2 variant for pleiotropic effects on height and metabolic traits in ponies. *J Vet Intern Med* 2019;33(2):942-952. PMID: 30666754; PMCID: PMC6430908; DOI: 10.1111/jvim.15403. https://pubmed.ncbi.nlm.nih.gov/30666754/
- **grilzseger-2019-horse-roh** — Grilz-Seger G, Neuditschko M, Ricard A, et al. Genome-wide homozygosity patterns and evidence for selection in a set of European and Near Eastern horse breeds. *Genes (Basel)* 2019;10(7):491. PMID: 31261764; PMCID: PMC6679042; DOI: 10.3390/genes10070491. https://pubmed.ncbi.nlm.nih.gov/31261764/
- **mongolian-2023-selection-hoof** — Han H, Randhawa IAS, MacHugh DE, McGivney BA, Katz LM, et al. Selection signatures for local and regional adaptation in Chinese Mongolian horse breeds reveal candidate genes for hoof health. *BMC Genomics* 2023;24(1):35. PMID: 36658473; PMCID: PMC9854188; DOI: 10.1186/s12864-023-09116-8. https://pubmed.ncbi.nlm.nih.gov/36658473/
- **li-2005-irakm-osteoclast** — Li H, Cuartas E, Cui W, Choi Y, Crawford TD, Ke HZ, Kobayashi KS, Flavell RA, Vignery A. IL-1 receptor-associated kinase M is a central regulator of osteoclast differentiation and activation. *J Exp Med* 2005;201(7):1169-77. PMID: 15809356; PMCID: PMC2213136; DOI: 10.1084/jem.20041444. https://pubmed.ncbi.nlm.nih.gov/15809356/

Database records used: UniProtKB A0A3Q2HDT6, F6QZW8, A0A5F5PKF5, Q9Y616 (human IRAK3), Q8K4B2 (mouse Irak3) (https://rest.uniprot.org); NCBI RefSeq XP_023499869.1 and XP_023499870.1; Ensembl gene ENSECAG00000026958; AlphaFold DB models AF-A0A3Q2HDT6-F1 and AF-F6QZW8-F1 (v6), https://alphafold.ebi.ac.uk.


## Citations

1. beaumont-2024-equine-tenocyte-il1b-abstract.md
2. beaumont-2024-equine-tenocyte-il1b-fulltext.txt
3. beaumont-2024-equine-tenocyte-il1b-summary.md
4. beaumont-2025-equine-irak4-abstract.md
5. beaumont-2025-equine-irak4-fulltext.txt
6. beaumont-2025-equine-irak4-summary.md
7. du-2014-irakm-death-domain-abstract.md
8. du-2014-irakm-death-domain-fulltext.txt
9. du-2014-irakm-death-domain-summary.md
10. escoll-2003-irakm-endotoxin-abstract.md
11. escoll-2003-irakm-endotoxin-summary.md
12. freihat-2019-irak3-guanylate-cyclase-abstract.md
13. freihat-2019-irak3-guanylate-cyclase-fulltext.txt
14. freihat-2019-irak3-guanylate-cyclase-summary.md
15. grilzseger-2019-horse-roh-abstract.md
16. grilzseger-2019-horse-roh-fulltext.txt
17. grilzseger-2019-horse-roh-summary.md
18. gurkan-2023-irakm-death-domain-review-abstract.md
19. gurkan-2023-irakm-death-domain-review-fulltext.txt
20. gurkan-2023-irakm-death-domain-review-summary.md
21. horne-2021-irak3-preview-abstract.md
22. horne-2021-irak3-preview-summary.md
23. hubbard-2010-irakm-review-abstract.md
24. hubbard-2010-irakm-review-fulltext.txt
25. hubbard-2010-irakm-review-summary.md
26. kobayashi-2002-irakm-negative-regulator-abstract.md
27. kobayashi-2002-irakm-negative-regulator-summary.md
28. lange-2021-irak3-dimer-structure-abstract.md
29. lange-2021-irak3-dimer-structure-fulltext.txt
30. lange-2021-irak3-dimer-structure-summary.md
31. li-2005-irakm-osteoclast-abstract.md
32. li-2005-irakm-osteoclast-fulltext.txt
33. li-2005-irakm-osteoclast-summary.md
34. lin-2010-myddosome-abstract.md
35. lin-2010-myddosome-summary.md
36. miyata-2015-glucocorticoid-irakm-abstract.md
37. miyata-2015-glucocorticoid-irakm-fulltext.txt
38. miyata-2015-glucocorticoid-irakm-summary.md
39. mongolian-2023-selection-hoof-abstract.md
40. mongolian-2023-selection-hoof-fulltext.txt
41. mongolian-2023-selection-hoof-summary.md
42. nechama-2018-il33-pin1-irakm-abstract.md
43. nechama-2018-il33-pin1-irakm-fulltext.txt
44. nechama-2018-il33-pin1-irakm-summary.md
45. norton-2019-hmga2-irak3-ponies-abstract.md
46. norton-2019-hmga2-irak3-ponies-fulltext.txt
47. norton-2019-hmga2-irak3-ponies-summary.md
48. padoan-2022-equine-asthma-immunotranscriptome-abstract.md
49. padoan-2022-equine-asthma-immunotranscriptome-fulltext.txt
50. padoan-2022-equine-asthma-immunotranscriptome-summary.md
51. poelman-2022-irakm-nmr-anomalies-abstract.md
52. poelman-2022-irakm-nmr-anomalies-summary.md
53. rosati-2002-murine-irakm-abstract.md
54. rosati-2002-murine-irakm-summary.md
55. tallmadge-2018-foal-pbmc-transcriptome-abstract.md
56. tallmadge-2018-foal-pbmc-transcriptome-fulltext.txt
57. tallmadge-2018-foal-pbmc-transcriptome-summary.md
58. turek-2023-irak3-localization-abstract.md
59. turek-2023-irak3-localization-fulltext.txt
60. turek-2023-irak3-localization-summary.md
61. vantveer-2007-irakm-human-endotoxemia-abstract.md
62. vantveer-2007-irakm-human-endotoxemia-summary.md
63. wade-2009-horse-genome-abstract.md
64. wade-2009-horse-genome-summary.md
65. weng-2024-zebrafish-irak3-abstract.md
66. weng-2024-zebrafish-irak3-summary.md
67. wesche-1999-irakm-abstract.md
68. wesche-1999-irakm-summary.md
69. zhou-2013-irakm-mekk3-abstract.md
70. zhou-2013-irakm-mekk3-summary.md