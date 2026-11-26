---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:58:52.082791'
end_time: '2026-10-26T00:09:53.234437'
duration_seconds: 661.15
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: IRF9
  gene_symbol: IRF9
  uniprot_accession: A0A9L0I7X9
  protein_description: 'RecName: Full=Interferon regulatory factor 9 {ECO:0000256|ARBA:ARBA00067361};
    AltName: Full=IFN-alpha-responsive transcription factor subunit {ECO:0000256|ARBA:ARBA00082071};
    AltName: Full=ISGF3 p48 subunit {ECO:0000256|ARBA:ARBA00081569}; AltName: Full=Interferon-stimulated
    gene factor 3 gamma {ECO:0000256|ARBA:ARBA00077133}; AltName: Full=Transcriptional
    regulator ISGF3 subunit gamma {ECO:0000256|ARBA:ARBA00076458};'
  gene_info: Name=IRF9 {ECO:0000313|Ensembl:ENSEASP00005036572.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the IRF family. {ECO:0000256|PROSITE-
  protein_domains: Interferon_reg_fac_CS. (IPR019817); Interferon_reg_fact_DNA-bd_dom.
    (IPR001346); Interferon_reg_factor-3. (IPR019471); SMAD-like_dom_sf. (IPR017855);
    SMAD_FHA_dom_sf. (IPR008984)
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
- **UniProt Accession:** A0A9L0I7X9
- **Protein Description:** RecName: Full=Interferon regulatory factor 9 {ECO:0000256|ARBA:ARBA00067361}; AltName: Full=IFN-alpha-responsive transcription factor subunit {ECO:0000256|ARBA:ARBA00082071}; AltName: Full=ISGF3 p48 subunit {ECO:0000256|ARBA:ARBA00081569}; AltName: Full=Interferon-stimulated gene factor 3 gamma {ECO:0000256|ARBA:ARBA00077133}; AltName: Full=Transcriptional regulator ISGF3 subunit gamma {ECO:0000256|ARBA:ARBA00076458};
- **Gene Information:** Name=IRF9 {ECO:0000313|Ensembl:ENSEASP00005036572.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the IRF family. {ECO:0000256|PROSITE-
- **Key Domains:** Interferon_reg_fac_CS. (IPR019817); Interferon_reg_fact_DNA-bd_dom. (IPR001346); Interferon_reg_factor-3. (IPR019471); SMAD-like_dom_sf. (IPR017855); SMAD_FHA_dom_sf. (IPR008984)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "IRF9" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'IRF9' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **IRF9** (gene ID: IRF9, UniProt: A0A9L0I7X9) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Interferon Regulatory Factor 9 (IRF9) of the Donkey, *Equus asinus* (UniProt A0A9L0I7X9)

## 1. Introduction and Summary

The protein encoded by UniProt accession A0A9L0I7X9 is the donkey (*Equus asinus*) ortholog of interferon regulatory factor 9 (IRF9), also known as ISGF3γ or p48, the DNA-binding subunit of the heterotrimeric transcription factor ISGF3 (interferon-stimulated gene factor 3). The UniProt entry is an unreviewed TrEMBL record derived from the Ensembl annotation of the chromosome-level Dezhou donkey reference genome; it is a 421-residue protein encoded on donkey chromosome 2, and every functional statement it carries (ISGF3 subunit, STAT2 binding, nuclear localization, RNA polymerase II-specific DNA-binding transcription factor activity) is assigned automatically by homology, with protein existence level 3 ("inferred from homology") [uniprot-A0A9L0I7X9-entry; wang-2020-donkey-genomes-abstract]. Identity verification was therefore the first task of this review. The gene symbol IRF9 is not ambiguous in the way some symbols are: the protein description, the InterPro/Pfam domain composition (an IRF tryptophan-pentad DNA-binding domain followed by an IRF-3-type IRF-association domain of the SMAD/FHA fold), the PANTHER subfamily assignment (PTHR11949:SF26, interferon regulatory factor 9) and the cross-reference to human gene CTD 10379 all agree [uniprot-A0A9L0I7X9-entry]. My own pairwise alignment shows that the donkey protein is about 80% identical to human IRF9 (Q00978) over the length of the human protein, with 107 of 117 residues identical in the DNA-binding domain (SEQUENCE_ANALYSIS_NOTES.md). The literature search found no experimental study of IRF9 protein in donkeys, and the only equid work addresses IRF9 mRNA levels in horse cells infected by equid herpesviruses [oladunni-2019-ehv1-ifn-equine-abstract; oladunni-2020-ehv4-ifn-abstract]. The functional description below therefore rests mainly on well-characterized human and mouse orthologs and is transferred to the donkey protein because of strong sequence and structural conservation, including conservation of the experimentally defined STAT2-binding interface.

In short, IRF9 is a sequence-specific transcription factor that connects type I (IFN-α/β) and type III (IFN-λ) interferon receptor signalling to the transcription of interferon-stimulated genes (ISGs). It has no enzymatic activity. Its N-terminal DNA-binding domain recognizes the GAAA core repeats of the IFN-stimulated response element (ISRE), and its C-terminal IRF-association domain binds the coiled-coil domain of STAT2 with high affinity and selectivity. When interferon triggers JAK1/TYK2-mediated tyrosine phosphorylation of STAT1 and STAT2, IRF9 joins the STAT1:STAT2 heterodimer to form ISGF3, which accumulates in the nucleus and activates ISRE-containing genes that establish the antiviral state [veals-1992-isgf3gamma-irf-myb-abstract; kessler-1990-isgf3-nuclear-translocation-abstract; rengachari-2018-irf9-stat2-structure-abstract; paul-2018-irf9-structure-regulation-fulltext]. IRF9 also works in non-canonical STAT2/IRF9 complexes and in unphosphorylated ISGF3 (U-ISGF3), which control basal and prolonged ISG expression [fink-2013-stat2-irf9-beyond-isgf3-abstract; cheon-2013-unphosphorylated-isgf3-abstract; platanitis-2019-stat2-irf9-switch-abstract]. Loss of IRF9 in mice and in humans abolishes ISGF3 formation and severely impairs antiviral defence, most strikingly against influenza A virus in humans [kimura-1996-p48-knockout-abstract; hernandez-2018-irf9-deficiency-influenza-abstract].

## 2. Identity, Gene Model and Evolutionary Conservation of Donkey IRF9

The donkey IRF9 gene model (Ensembl ENSEASG00005011944; RefSeq XP_014724060.1; NCBI GeneID 106848581) comes from the reference assembly of Wang et al., who sequenced a male Dezhou donkey to chromosome level in a study focused on domestication and coat-colour genetics [wang-2020-donkey-genomes-abstract; uniprot-A0A9L0I7X9-entry]. That genome paper contains no IRF9-specific analysis, so the entry has no direct experimental support beyond the gene prediction. UniProt annotates an IRF tryptophan-pentad repeat domain at residues 9–116 and a disordered, low-complexity region at residues 114–197, and it maps the remainder to the IRF-3 (IAD) family and the SMAD/FHA superfamily [uniprot-A0A9L0I7X9-entry]. This arrangement matches the canonical IRF architecture: an N-terminal helix-turn-helix DNA-binding domain with five conserved tryptophans, a flexible linker, and a C-terminal IRF-association domain that mediates protein–protein interaction [paul-2018-irf9-structure-regulation-fulltext].

Comparative sequence analysis supports a one-to-one orthology with human and mouse IRF9. The five tryptophans of the DNA-binding domain, at positions 15, 30, 42, 62 and 80 in human IRF9 [paul-2018-irf9-structure-regulation-fulltext], occupy identical positions in the donkey sequence, and lysine 81, whose CBP-mediated acetylation is reported to be needed for IRF9 DNA binding and ISGF3 formation [paul-2018-irf9-structure-regulation-fulltext; tang-2007-acetylation-ifnar-abstract], is conserved as well (SEQUENCE_ANALYSIS_NOTES.md). Most of the divergence among the donkey, human and mouse proteins lies in the linker. This agrees with the early observation that the middle region of mouse ISGF3γ differs considerably from the human protein even though the mouse protein is functional in ISGF3 reconstitution [suhara-1996-mouse-isgf3gamma-cdna-abstract]. The donkey model also carries a C-terminal extension of about 28 residues beyond the human C-terminus. It lies outside the structurally defined IAD core that Rengachari et al. resolved, residues 197–385 of mouse IRF9 [rengachari-2018-irf9-stat2-structure-fulltext]. Two lines of evidence argue that this extension is not a donkey gene-model artefact. First, it is predicted independently by Ensembl and by NCBI's Gnomon pipeline, which annotates the identical RefSeq protein XP_014724060.1 as "interferon regulatory factor 9 isoform X2" [refseq-XP_014724060-record; uniprot-A0A9L0I7X9-entry]. It is also present in every donkey IRF9 entry and in most horse IRF9 entries [uniprot-equus-IRF9-isoforms-sequences]. Second, and more decisively, bovine IRF9 sequences derived from mRNA/cDNA clones (UniProt Q58D50, from EMBL BC102047 and BT021680, and Q0V886), as well as a pig model, end in a homologous C-terminal extension [uniprot-other-laurasiatheria-IRF9-sequences; equus-IRF9-isoforms-summary]. The extended C-terminus therefore appears to be a transcript-supported feature of laurasiatherian IRF9 that canonical human and mouse IRF9 lack (SEQUENCE_ANALYSIS_NOTES.md). No functional study has addressed it.

The gene models also show that A0A9L0I7X9 is one of several equid splice isoforms, and not necessarily the most canonical one. A 445-residue donkey isoform (A0A9L0I9K1) contains a 24-residue linker segment (GTDKTEAPVQGDQGSLELLSSPD) that aligns with human IRF9 residues ~192–214 and is absent from A0A9L0I7X9, and a second 421-residue donkey entry (A0A8C4PN15) differs from A0A9L0I7X9 throughout residues 193–230 [uniprot-equus-IRF9-isoforms-sequences]. Consequently the 445-residue isoform is more similar to human IRF9 (326 versus 312 identical residues). In human/mouse coordinates the segment missing from A0A9L0I7X9 sits immediately N-terminal to, and partly overlapping, the start of the crystallized IAD. All isoforms, however, retain the IAD core and the STAT2-binding residues discussed below (SEQUENCE_ANALYSIS_NOTES.md).

## 3. Molecular Function: A DNA-Binding Subunit That Supplies Promoter Specificity to ISGF3

IRF9 was first identified biochemically. Purification of ISGF3 from interferon-treated HeLa cells revealed a 48-kDa DNA-binding protein together with 84-, 91- and 113-kDa polypeptides that had no DNA-binding activity of their own; [fu-1990-isgf3-multiple-chains-abstract]; these larger polypeptides correspond to STAT1 (α or β) and STAT2 [kimura-1996-p48-knockout-abstract; martinez-moczygemba-1997-stat2-p48-abstract]. Kessler and colleagues separated the factor into a cytoplasmic ISGF3α component, the STATs, and ISGF3γ, a 48-kDa polypeptide with intrinsic but low-affinity ISRE-binding activity. Assembly with activated ISGF3α kept the same sequence specificity and raised the affinity for the ISRE about 25-fold [kessler-1990-isgf3-nuclear-translocation-abstract]. Cloning of the ISGF3γ cDNA showed that its amino-terminal 117 residues resemble the IRF family and the imperfect tryptophan repeats of the c-Myb DNA-binding domain. Recombinant ISGF3γ bound DNA with the same specificity as the native protein and assembled into mature ISGF3 with HeLa ISGF3α [veals-1992-isgf3gamma-irf-myb-abstract]. Deletion analysis then showed that the N-terminal IRF-homology region alone suffices for sequence-specific ISRE binding, and that a separate C-terminal region of about 160 residues mediates association with ISGF3α and can transfer this property to a heterologous protein. Formation of the complex also changed the DNA-binding specificity, which implies that STAT subunits make additional base contacts [veals-1993-isgf3gamma-two-domains-abstract].

The ISRE consensus, 5′-A/GNGAAANNGAAACT-3′, is recognized jointly by the DNA-binding domains of IRF9 and STAT1 within ISGF3, while STAT2 contacts non-consensus flanking sequence [paul-2018-irf9-structure-regulation-fulltext]. The structural model of ISGF3 on the ADAR ISRE places a STAT1 protomer on the first 5′-GGAA-3′ half-site and the IRF9 DNA-binding domain on the second GAAA repeat, by analogy to DNA-bound IRF3 [rengachari-2018-irf9-stat2-structure-fulltext]. IRF9 itself provides little transactivation. A GAL4–IRF9 fusion activated a reporter only when cellular STAT1 and STAT2 were present, but fusing IRF9 to the C-terminal transactivation domain of STAT2, or to the VP16 acidic activation domain, produced a constitutively active, ISGF3-like activator. This hybrid bound endogenous ISGF3 target loci, induced ISGs and established an antiviral state against both RNA and DNA viruses without autocrine interferon [kraus-2003-irf9-stat2-hybrid-abstract]. The best-supported functional assignment for IRF9 is therefore "sequence-specific DNA-binding transcription factor subunit": IRF9 provides promoter recognition, and STAT2 contributes most of the transcriptional activation potential of the complex.

## 4. Structural Basis of the Selective IRF9–STAT2 Interaction

IRF9's partner selectivity has a clear structural explanation. Co-immunoprecipitation showed that p48 associates specifically with STAT2, and not with STAT1, both before and after IFN-α stimulation, and STAT2/STAT1 chimeras mapped the binding site to the N-terminal coiled-coil region of STAT2 [martinez-moczygemba-1997-stat2-p48-abstract]. Rengachari et al. solved crystal structures of the mouse IRF9 IAD alone and bound to the STAT2 coiled-coil domain [rengachari-2018-irf9-stat2-structure-abstract]. The IRF9 IAD has the MH2/SMAD fold, a central β-sandwich flanked by helices and loops, but it lacks the C-terminal autoinhibitory segment that keeps IRF3 latent until phosphorylation [rengachari-2018-irf9-stat2-structure-fulltext]. This explains why IRF9, unlike IRF3, IRF5 and IRF7, does not need activating phosphorylation to engage its partner and is pre-associated with STAT2 in unstimulated cells [rengachari-2018-irf9-stat2-structure-fulltext; paul-2018-irf9-structure-regulation-fulltext]. STAT2 binds a hydrophobic patch on the convex surface of the IAD β-sandwich, called interface IF1. Mutating IF1 residues (L233A, R236E, L274A, F283A in mouse IRF9) reduced or abolished STAT2 binding in vitro and abolished ISGF3 activity on an IFIT1 promoter reporter in IRF9/IRF3-deficient mouse fibroblasts [rengachari-2018-irf9-stat2-structure-fulltext]. Isothermal titration calorimetry gave a dissociation constant of 10 nM for STAT2 and 5 µM for STAT1. Swapping a single coiled-coil residue (STAT2 V171E, or the reciprocal STAT1 E169V) largely inverted this preference, showing that a small number of divergent surface residues encode the specificity of the pairing [rengachari-2018-irf9-stat2-structure-fulltext].

The interface is conserved among vertebrate IRF9 orthologs and divergent among IRF paralogs [rengachari-2018-irf9-stat2-structure-abstract]. In donkey IRF9 all four IF1 residues are conserved, as L234, R237, L275 and F284 (SEQUENCE_ANALYSIS_NOTES.md), which strongly predicts that the donkey protein binds STAT2 in the same way. The interface is also a target for viral antagonism. Zika and dengue virus NS5 proteins enclose the STAT2 coiled-coil domain in an interdomain cleft and so prevent STAT2 from associating with IRF9 [wang-2020-flavivirus-ns5-stat2-abstract]. Rengachari et al. also note that the region of the IRF9 IAD corresponding to the pLxIS-binding site that IRF3 uses to engage the adaptors STING, MAVS and TRIF is structurally present in IRF9 [rengachari-2018-irf9-stat2-structure-fulltext], but no adaptor-binding role has been shown for IRF9. A further reported interaction is the docking of the IRF9 IAD (IH2 domain) on CBP-acetylated Lys399 of IFNAR2, which was proposed to initiate ISGF3 assembly at the receptor [tang-2007-acetylation-ifnar-abstract]. The same study reported that CBP acetylates the DNA-binding domain of IRF9 and that this acetylation is critical for ISGF3 activity [tang-2007-acetylation-ifnar-abstract].

## 5. Subcellular Localization and Nucleocytoplasmic Dynamics

UniProt assigns donkey IRF9 to the nucleus by automatic annotation [uniprot-A0A9L0I7X9-entry]. Experimental data from human cells give a more dynamic picture. Even in early fractionation studies ISGF3γ partitioned between cytoplasm and nucleus in unstimulated cells, whereas the STAT components entered the nucleus only after IFN-α stimulation. Stimulation led to nuclear accumulation of both components as a stable ISGF3–ISRE complex [kessler-1990-isgf3-nuclear-translocation-abstract]. Lau et al. found that GFP-tagged p48 is efficiently and constitutively targeted to the nucleus by a bipartite basic nuclear localization signal within amino acids 50–100 of its DNA-binding domain, and that this targeting does not require DNA-binding ability. Co-expressed STAT2 overrode this intrinsic targeting and held p48 in the cytoplasm as a pre-formed STAT2:p48 complex [lau-2000-irf-nls-abstract]. In turn, the constitutive association with IRF9 drives nuclear import of latent, unphosphorylated STAT2, which shuttles continuously and is exported by a CRM1-dependent nuclear export signal in the STAT2 C-terminus. After tyrosine phosphorylation, STAT2 dimerizes with phosphorylated STAT1 and accumulates in the nucleus [banninger-2004-stat2-trafficking-abstract].

The classical model holds that ISGF3 assembles in the cytoplasm and then moves to the nucleus [kessler-1990-isgf3-nuclear-translocation-abstract; paul-2018-irf9-structure-regulation-fulltext]. Platanitis et al. revised this picture in mouse macrophages. Using ChIP-seq, transcriptomics and in vivo proximity labelling, they showed that pre-formed STAT2–IRF9 complexes occupy ISG promoters under homeostatic conditions, and that type I IFN or IFN-γ causes a complete STAT1–STAT2–IRF9 complex to bind those promoters. They proposed that ISGF3 assembles on DNA rather than in the cytoplasm [platanitis-2019-stat2-irf9-switch-abstract]. Taken together, these studies indicate that IRF9 acts in the nucleus, at ISRE-containing regulatory regions of RNA polymerase II-transcribed genes, while a cytoplasmic pool bound to STAT2 stands ready for rapid signalling.

## 6. Pathway Context: Type I and Type III Interferon Signalling and Non-Canonical Complexes

In the canonical type I IFN pathway, IFN-α/β binding to IFNAR1/IFNAR2 activates TYK2 and JAK1, which phosphorylate STAT1 on Tyr701 and STAT2 on Tyr690. The phosphorylated heterodimer then recruits IRF9 to form ISGF3 [paul-2018-irf9-structure-regulation-fulltext]. Type III interferons (IFN-λ1–3) signal through a separate receptor complex, IFNLR1/IL-10R2, which also activates the JAK–STAT pathway [kotenko-2003-ifn-lambda-receptor-abstract], and ISGF3 is the shared transcriptional effector of type I and type III IFN responses [fink-2013-stat2-irf9-beyond-isgf3-abstract; hernandez-2018-irf9-deficiency-influenza-abstract]. Genetic studies in mice show that IRF9 is required for this output. Embryonic fibroblasts from p48-knockout mice had no ISRE-binding activity and were severely impaired in ISG induction and in establishing an antiviral state in response to IFN-α. Unexpectedly, IFN-γ responses were also impaired, and IRF9 and IRF-1 were found to have complementary, non-redundant roles [kimura-1996-p48-knockout-abstract].

Beyond canonical ISGF3, IRF9 forms STAT1-independent STAT2/IRF9 complexes, including STAT2 homodimer/IRF9 assemblies, which direct transcription of ISRE-containing genes in response to IFN-I [fink-2013-stat2-irf9-beyond-isgf3-abstract; michalska-2018-isg-amplifier-abstract]. When a high dose of IFN-β raises the levels of IRF9, STAT1 and STAT2, these proteins form unphosphorylated ISGF3 (U-ISGF3). U-ISGF3 sustains prolonged expression of a subset of antiviral genes driven by distinct ISREs and confers resistance to DNA damage, after the initial phosphorylated-ISGF3 response has been switched off [cheon-2013-unphosphorylated-isgf3-abstract]. The relative weight of these complexes is still debated. Genome-wide RNA-seq and ChIP-seq in human cell lines indicate that phosphorylated ISGF3 and STAT2/IRF9 dominate both early and prolonged ISG expression and antiviral protection, and that U-ISGF3 acts in a threshold-dependent way on constitutive responses [nowicka-2023-isgf3-stat2-irf9-genome-abstract]. Michalska et al. integrate these observations into a proposed positive-feedback "amplifier circuit" of phosphorylated and unphosphorylated ISGF3, STAT2/IRF9, GAF and IRF1. Because IRF9, STAT1 and STAT2 are themselves ISGs, such a circuit would shape long-term cellular responsiveness to interferons [michalska-2018-isg-amplifier-abstract].

## 7. Physiological Significance: Antiviral Immunity in Humans, Mice and Equids

Human genetics has shown which functions of IRF9 are non-redundant. A child homozygous for a loss-of-function IRF9 allele (c.991G>A, which affects the final nucleotide of exon 7) developed life-threatening influenza pneumonitis [hernandez-2018-irf9-deficiency-influenza-abstract; hernandez-2018-irf9-deficiency-influenza-fulltext]. The patient's cells still formed GAF (STAT1 homodimers) but not ISGF3 in response to IFN-α2b. They induced a much narrower IFN transcriptome and failed to control influenza A virus, parainfluenza virus and respiratory syncytial virus in vitro. Wild-type IRF9 rescued these defects, and silencing IRF9 in control cells increased viral replication. The authors concluded that human IRF9- and ISGF3-dependent type I and III IFN pathways are essential for controlling influenza A virus, although the child controlled several other common viruses in vivo [hernandez-2018-irf9-deficiency-influenza-abstract]. A second family with complete IRF9 deficiency and impaired control of multiple viral infections has been reported [bravo-garcia-morato-2019-irf9-deficiency-pubmed-record], and reviews of inborn errors of immunity group IRF9 deficiency with IRF7 deficiency as causes of severe influenza [mogensen-2018-irf-stat-review-abstract].

For equids, evidence is indirect but consistent with a conserved pathway. In equine endothelial cells, the neuropathogenic equid herpesvirus 1 strain T953 significantly reduced IRF9 mRNA at 6 and 12 hours post-infection. It also reduced TYK2 and blocked IFN-induced STAT2 phosphorylation and nuclear translocation, which suggests that the virus targets the ISGF3 axis to escape the type I IFN response [oladunni-2019-ehv1-ifn-equine-abstract]. The less pathogenic EHV-4, by contrast, induced variable amounts of IRF9 without suppressing it, while transiently interfering with STAT1/STAT2 phosphorylation [oladunni-2020-ehv4-ifn-abstract]. These horse studies measured transcripts rather than IRF9 protein activity, and none used donkey cells. They nonetheless indicate that equid IRF9 is part of an interferon-regulated antiviral signalling network that equid pathogens antagonize.

## 8. Synthesis: Functional Annotation of A0A9L0I7X9

Combining the orthology evidence with the experimental literature on mammalian IRF9 gives a coherent functional annotation for donkey IRF9. Its core molecular function is sequence-specific binding to ISRE cis-regulatory DNA (GAAA repeats) as an RNA polymerase II-specific DNA-binding transcription factor subunit, together with high-affinity binding to STAT2 through the IAD [veals-1993-isgf3gamma-two-domains-abstract; rengachari-2018-irf9-stat2-structure-abstract]. It is a component of the ISGF3 complex [fu-1990-isgf3-multiple-chains-abstract; kessler-1990-isgf3-nuclear-translocation-abstract]. It functions mainly in the nucleus at ISG promoters, and a STAT2-bound pool shuttles through the cytoplasm [lau-2000-irf-nls-abstract; banninger-2004-stat2-trafficking-abstract; platanitis-2019-stat2-irf9-switch-abstract]. The biological processes it serves are the type I interferon-mediated and type III interferon-mediated signalling pathways, positive regulation of ISG transcription, and defence against viruses [kimura-1996-p48-knockout-abstract; hernandez-2018-irf9-deficiency-influenza-abstract]. All of these assignments for the donkey protein are inferences from sequence and structural conservation (the experimentally defined STAT2 interface, the tryptophan pentad and the acetylation site are all conserved) rather than direct experimental observations in *Equus asinus*. One further caveat applies to this particular accession: A0A9L0I7X9 represents a predicted splice isoform (RefSeq isoform X2) that lacks a short, human-conserved segment at the linker–IAD boundary. The functional inferences are strongest for the shared DNA-binding domain and IAD core, and the isoform-specific contribution of the variable linker remains untested [refseq-XP_014724060-record; uniprot-equus-IRF9-isoforms-sequences].

## Open Questions

The most basic open question is experimental: the donkey IRF9 protein has never been expressed, localized or tested functionally, so it has not been shown directly that it reconstitutes ISGF3 with equid STAT1 and STAT2 or binds the ISRE. Reconstitution assays in IRF9-deficient cells, or electrophoretic mobility shift assays with recombinant donkey IRF9 and equid STATs, would confirm the inferred function. A second question concerns isoforms. The roughly 28-residue C-terminal extension is supported by bovine cDNA and conserved across equid gene models, so it is probably real. Its function is unknown, and it would be worth testing whether it affects STAT2 binding, nuclear export or transcriptional activity, since human and mouse IRF9 end shortly after the structured IAD. Similarly, the target accession A0A9L0I7X9 corresponds to RefSeq "isoform X2" and lacks a human-conserved 24-residue segment at the linker–IAD boundary that the 445-residue isoform retains. Donkey RNA-seq or long-read transcript data are needed to establish which isoforms are expressed, in which tissues and at what ratio, and whether isoform X2 assembles into ISGF3 as efficiently as the canonical form. Third, it is unclear whether equid IRF9 has the same mix of canonical ISGF3, STAT2/IRF9 and U-ISGF3 activities described in human and mouse cells; given the current debate over the role of unphosphorylated complexes [cheon-2013-unphosphorylated-isgf3-abstract; nowicka-2023-isgf3-stat2-irf9-genome-abstract], ChIP-seq of IRF9 in equid cells would be informative. Fourth, the horse studies show that EHV-1 lowers IRF9 transcript levels [oladunni-2019-ehv1-ifn-equine-abstract], but the viral gene products responsible, and whether donkey herpesviruses or other equid viruses such as equine arteritis virus target IRF9 protein or the IRF9–STAT2 interface the way flavivirus NS5 does in humans [wang-2020-flavivirus-ns5-stat2-abstract], remain unknown. Equine arteritis virus is a relevant candidate: arterivirus nsp1 subunits, including those of EAV, suppress interferon responses, and porcine reproductive and respiratory syndrome virus nsp1β degrades karyopherin-α1, the importin that mediates ISGF3 nuclear import [han-2014-arterivirus-nsp1-abstract]. Whether EAV nsp1 acts on IRF9-containing complexes in equid cells has not been tested. Finally, the reported acetylation-dependent docking of IRF9 on IFNAR2 [tang-2007-acetylation-ifnar-abstract] and the suggestion of DNA-on assembly of ISGF3 [platanitis-2019-stat2-irf9-switch-abstract] offer two quite different models for where ISGF3 assembles. How the two models fit together, in any species, is still unresolved.

## References

* **banninger-2004-stat2-trafficking**: Banninger G, Reich NC. STAT2 nuclear trafficking. *The Journal of biological chemistry 2004;279:39199-206*. PMID: 15175343. DOI: 10.1074/jbc.M400815200. https://pubmed.ncbi.nlm.nih.gov/15175343/
* **bravo-garcia-morato-2019-irf9-deficiency**: Bravo García-Morato M, Calvo Apalategi A, Bravo-Gallego LY et al. Impaired control of multiple viral infections in a family with complete IRF9 deficiency. *The Journal of allergy and clinical immunology 2019;144:309-312.e10*. PMID: 30826365. DOI: 10.1016/j.jaci.2019.02.019. https://pubmed.ncbi.nlm.nih.gov/30826365/
* **cheon-2013-unphosphorylated-isgf3**: Cheon H, Holvey-Bates EG, Schoggins JW et al. IFNβ-dependent increases in STAT1, STAT2, and IRF9 mediate resistance to viruses and DNA damage. *The EMBO journal 2013;32:2751-63*. PMID: 24065129. DOI: 10.1038/emboj.2013.203. PMCID: PMC3801437. https://pubmed.ncbi.nlm.nih.gov/24065129/
* **fink-2013-stat2-irf9-beyond-isgf3**: Fink K, Grandvaux N. STAT2 and IRF9: Beyond ISGF3. *JAK-STAT 2013;2:e27521*. PMID: 24498542. DOI: 10.4161/jkst.27521. PMCID: PMC3906322. https://pubmed.ncbi.nlm.nih.gov/24498542/
* **fu-1990-isgf3-multiple-chains**: Fu XY, Kessler DS, Veals SA et al. ISGF3, the transcriptional activator induced by interferon alpha, consists of multiple interacting polypeptide chains. *Proceedings of the National Academy of Sciences of the United States of America 1990;87:8555-9*. PMID: 2236065. DOI: 10.1073/pnas.87.21.8555. PMCID: PMC54995. https://pubmed.ncbi.nlm.nih.gov/2236065/
* **hernandez-2018-irf9-deficiency-influenza**: Hernandez N, Melki I, Jing H et al. Life-threatening influenza pneumonitis in a child with inherited IRF9 deficiency. *The Journal of experimental medicine 2018;215:2567-2585*. PMID: 30143481. DOI: 10.1084/jem.20180628. PMCID: PMC6170168. https://pubmed.ncbi.nlm.nih.gov/30143481/
* **kessler-1990-isgf3-nuclear-translocation**: Kessler DS, Veals SA, Fu XY et al. Interferon-alpha regulates nuclear translocation and DNA-binding affinity of ISGF3, a multimeric transcriptional activator. *Genes & development 1990;4:1753-65*. PMID: 2249773. DOI: 10.1101/gad.4.10.1753. https://pubmed.ncbi.nlm.nih.gov/2249773/
* **kimura-1996-p48-knockout**: Kimura T, Kadokawa Y, Harada H et al. Essential and non-redundant roles of p48 (ISGF3 gamma) and IRF-1 in both type I and type II interferon responses, as revealed by gene targeting studies. *Genes to cells : devoted to molecular & cellular mechanisms 1996;1:115-24*. PMID: 9078371. DOI: 10.1046/j.1365-2443.1996.08008.x. https://pubmed.ncbi.nlm.nih.gov/9078371/
* **kotenko-2003-ifn-lambda-receptor**: Kotenko SV, Gallagher G, Baurin VV et al. IFN-lambdas mediate antiviral protection through a distinct class II cytokine receptor complex. *Nature immunology 2003;4:69-77*. PMID: 12483210. DOI: 10.1038/ni875. https://pubmed.ncbi.nlm.nih.gov/12483210/
* **kraus-2003-irf9-stat2-hybrid**: Kraus TA, Lau JF, Parisien JP et al. A hybrid IRF9-STAT2 protein recapitulates interferon-stimulated gene expression and antiviral response. *The Journal of biological chemistry 2003;278:13033-8*. PMID: 12574168. DOI: 10.1074/jbc.M212972200. https://pubmed.ncbi.nlm.nih.gov/12574168/
* **lau-2000-irf-nls**: Lau JF, Parisien JP, Horvath CM et al. Interferon regulatory factor subcellular localization is determined by a bipartite nuclear localization signal in the DNA-binding domain and interaction with cytoplasmic retention factors. *Proceedings of the National Academy of Sciences of the United States of America 2000;97:7278-83*. PMID: 10860992. DOI: 10.1073/pnas.97.13.7278. PMCID: PMC16536. https://pubmed.ncbi.nlm.nih.gov/10860992/
* **martinez-moczygemba-1997-stat2-p48**: Martinez-Moczygemba M, Gutch MJ, French DL et al. Distinct STAT structure promotes interaction of STAT2 with the p48 subunit of the interferon-alpha-stimulated transcription factor ISGF3. *The Journal of biological chemistry 1997;272:20070-6*. PMID: 9242679. DOI: 10.1074/jbc.272.32.20070. https://pubmed.ncbi.nlm.nih.gov/9242679/
* **michalska-2018-isg-amplifier**: Michalska A, Blaszczyk K, Wesoly J et al. A Positive Feedback Amplifier Circuit That Regulates Interferon (IFN)-Stimulated Gene Expression and Controls Type I and Type II IFN Responses. *Frontiers in immunology 2018;9:1135*. PMID: 29892288. DOI: 10.3389/fimmu.2018.01135. PMCID: PMC5985295. https://pubmed.ncbi.nlm.nih.gov/29892288/
* **mogensen-2018-irf-stat-review**: Mogensen TH. IRF and STAT Transcription Factors - From Basic Biology to Roles in Infection, Protective Immunity, and Primary Immunodeficiencies. *Frontiers in immunology 2018;9:3047*. PMID: 30671054. DOI: 10.3389/fimmu.2018.03047. PMCID: PMC6331453. https://pubmed.ncbi.nlm.nih.gov/30671054/
* **nowicka-2023-isgf3-stat2-irf9-genome**: Nowicka H, Sekrecka A, Blaszczyk K et al. ISGF3 and STAT2/IRF9 Control Basal and IFN-Induced Transcription through Genome-Wide Binding of Phosphorylated and Unphosphorylated Complexes to Common ISRE-Containing ISGs. *International journal of molecular sciences 2023;24*. PMID: 38139463. DOI: 10.3390/ijms242417635. PMCID: PMC10743977. https://pubmed.ncbi.nlm.nih.gov/38139463/
* **oladunni-2019-ehv1-ifn-equine**: Oladunni FS, Sarkar S, Reedy S et al. Equid Herpesvirus 1 Targets the Sensitization and Induction Steps To Inhibit the Type I Interferon Response in Equine Endothelial Cells. *Journal of virology 2019;93*. PMID: 31511388. DOI: 10.1128/JVI.01342-19. PMCID: PMC6854505. https://pubmed.ncbi.nlm.nih.gov/31511388/
* **oladunni-2020-ehv4-ifn**: Oladunni FS, Reedy S, Balasuriya UBR et al. The effect of equine herpesvirus type 4 on type-I interferon signaling molecules. *Veterinary immunology and immunopathology 2020;219:109971*. PMID: 31739157. DOI: 10.1016/j.vetimm.2019.109971. https://pubmed.ncbi.nlm.nih.gov/31739157/
* **paul-2018-irf9-structure-regulation**: Paul A, Tang TH, Ng SK et al. Interferon Regulatory Factor 9 Structure and Regulation. *Frontiers in immunology 2018;9:1831*. PMID: 30147694. DOI: 10.3389/fimmu.2018.01831. PMCID: PMC6095977. https://pubmed.ncbi.nlm.nih.gov/30147694/
* **platanitis-2019-stat2-irf9-switch**: Platanitis E, Demiroz D, Schneller A et al. A molecular switch from STAT2-IRF9 to ISGF3 underlies interferon-induced gene transcription. *Nature communications 2019;10:2921*. PMID: 31266943. DOI: 10.1038/s41467-019-10970-y. PMCID: PMC6606597. https://pubmed.ncbi.nlm.nih.gov/31266943/
* **rengachari-2018-irf9-stat2-structure**: Rengachari S, Groiss S, Devos JM et al. Structural basis of STAT2 recognition by IRF9 reveals molecular insights into ISGF3 function. *Proceedings of the National Academy of Sciences of the United States of America 2018;115:E601-E609*. PMID: 29317535. DOI: 10.1073/pnas.1718426115. PMCID: PMC5789952. https://pubmed.ncbi.nlm.nih.gov/29317535/
* **suhara-1996-mouse-isgf3gamma-cdna**: Suhara W, Yoneyama M, Yonekawa H et al. Structure of mouse interferon stimulated gene factor 3 gamma (ISGF3 gamma/p48) cDNA and chromosomal localization of the gene. *Journal of biochemistry 1996;119:231-4*. PMID: 8882710. DOI: 10.1093/oxfordjournals.jbchem.a021227. https://pubmed.ncbi.nlm.nih.gov/8882710/
* **tang-2007-acetylation-ifnar**: Tang X, Gao JS, Guan YJ et al. Acetylation-dependent signal transduction for type I interferon receptor. *Cell 2007;131:93-105*. PMID: 17923090. DOI: 10.1016/j.cell.2007.07.034. https://pubmed.ncbi.nlm.nih.gov/17923090/
* **veals-1992-isgf3gamma-irf-myb**: Veals SA, Schindler C, Leonard D et al. Subunit of an alpha-interferon-responsive transcription factor is related to interferon regulatory factor and Myb families of DNA-binding proteins. *Molecular and cellular biology 1992;12:3315-24*. PMID: 1630447. DOI: 10.1128/mcb.12.8.3315-3324.1992. PMCID: PMC364572. https://pubmed.ncbi.nlm.nih.gov/1630447/
* **veals-1993-isgf3gamma-two-domains**: Veals SA, Santa Maria T, Levy DE et al. Two domains of ISGF3 gamma that mediate protein-DNA and protein-protein interactions during transcription factor assembly contribute to DNA-binding specificity. *Molecular and cellular biology 1993;13:196-206*. PMID: 8417326. DOI: 10.1128/mcb.13.1.196-206.1993. PMCID: PMC358899. https://pubmed.ncbi.nlm.nih.gov/8417326/
* **wang-2020-donkey-genomes**: Wang C, Li H, Guo Y et al. Donkey genomes provide new insights into domestication and selection for coat color. *Nature communications 2020;11:6014*. PMID: 33293529. DOI: 10.1038/s41467-020-19813-7. PMCID: PMC7723042. https://pubmed.ncbi.nlm.nih.gov/33293529/
* **wang-2020-flavivirus-ns5-stat2**: Wang B, Thurmond S, Zhou K et al. Structural basis for STAT2 suppression by flavivirus NS5. *Nature structural & molecular biology 2020;27:875-885*. PMID: 32778820. DOI: 10.1038/s41594-020-0472-y. PMCID: PMC7554153. https://pubmed.ncbi.nlm.nih.gov/32778820/
* **uniprot-A0A9L0I7X9-entry**: UniProt Consortium. UniProtKB/TrEMBL entry A0A9L0I7X9 (IRF9, *Equus asinus*), entry version 15 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0I7X9.txt ; https://www.uniprot.org/uniprotkb/A0A9L0I7X9
* **SEQUENCE_ANALYSIS_NOTES.md**: Pairwise alignment analysis performed for this report using UniProt sequences A0A9L0I7X9, Q00978 (human IRF9; https://rest.uniprot.org/uniprotkb/Q00978.fasta) and Q61179 (mouse Irf9; https://rest.uniprot.org/uniprotkb/Q61179.fasta).
* **han-2014-arterivirus-nsp1**: Han M, Yoo D. Modulation of innate immune signaling by nonstructural protein 1 (nsp1) in the family Arteriviridae. *Virus research 2014;194:100-9*. PMID: 25262851. DOI: 10.1016/j.virusres.2014.09.007. PMCID: PMC7114407. https://pubmed.ncbi.nlm.nih.gov/25262851/
* **refseq-XP_014724060-record**: NCBI RefSeq protein XP_014724060.1, "interferon regulatory factor 9 isoform X2 [Equus asinus]", MODEL REFSEQ (Gnomon), annotation GCF_041296235.1-RS_2024_12. https://www.ncbi.nlm.nih.gov/protein/XP_014724060.1
* **uniprot-equus-IRF9-isoforms-sequences**: UniProtKB sequences for IRF9 in *Equus asinus* (A0A9L0I7X9, A0A8C4PN15, A0A9L0I9K1) and *Equus caballus* (F6Z2B0, A0A9L0SN53, A0A9L0STH9, A0A9L0SUN9, A0A9L0TC51). https://rest.uniprot.org/uniprotkb/stream?query=gene_exact:IRF9+AND+(taxonomy_id:9796+OR+taxonomy_id:9793)&format=fasta
* **uniprot-other-laurasiatheria-IRF9-sequences**: UniProtKB sequences Q58D50 (*Bos taurus*, from EMBL BC102047/BT021680 mRNA), Q0V886 (*Bos taurus*, from EMBL BT026333 mRNA) and A0A8D1G4V5 (*Sus scrofa*). https://www.uniprot.org/uniprotkb/Q58D50 ; https://www.uniprot.org/uniprotkb/Q0V886 ; https://www.uniprot.org/uniprotkb/A0A8D1G4V5
* **equus-IRF9-isoforms-summary**: Author's summary of the isoform comparison (citations/equus-IRF9-isoforms-summary.md), based on the UniProt and RefSeq records above.


## Citations

1. banninger-2004-stat2-trafficking-abstract.md
2. banninger-2004-stat2-trafficking-summary.md
3. bravo-garcia-morato-2019-irf9-deficiency-pubmed-record.md
4. bravo-garcia-morato-2019-irf9-deficiency-summary.md
5. cheon-2013-unphosphorylated-isgf3-abstract.md
6. cheon-2013-unphosphorylated-isgf3-fulltext.txt
7. cheon-2013-unphosphorylated-isgf3-summary.md
8. equus-IRF9-isoforms-summary.md
9. fink-2013-stat2-irf9-beyond-isgf3-abstract.md
10. fink-2013-stat2-irf9-beyond-isgf3-summary.md
11. fu-1990-isgf3-multiple-chains-abstract.md
12. fu-1990-isgf3-multiple-chains-summary.md
13. han-2014-arterivirus-nsp1-abstract.md
14. han-2014-arterivirus-nsp1-summary.md
15. hernandez-2018-irf9-deficiency-influenza-abstract.md
16. hernandez-2018-irf9-deficiency-influenza-fulltext.txt
17. hernandez-2018-irf9-deficiency-influenza-summary.md
18. kessler-1990-isgf3-nuclear-translocation-abstract.md
19. kessler-1990-isgf3-nuclear-translocation-summary.md
20. kimura-1996-p48-knockout-abstract.md
21. kimura-1996-p48-knockout-summary.md
22. kotenko-2003-ifn-lambda-receptor-abstract.md
23. kotenko-2003-ifn-lambda-receptor-summary.md
24. kraus-2003-irf9-stat2-hybrid-abstract.md
25. kraus-2003-irf9-stat2-hybrid-summary.md
26. lau-2000-irf-nls-abstract.md
27. lau-2000-irf-nls-summary.md
28. martinez-moczygemba-1997-stat2-p48-abstract.md
29. martinez-moczygemba-1997-stat2-p48-summary.md
30. michalska-2018-isg-amplifier-abstract.md
31. michalska-2018-isg-amplifier-summary.md
32. mogensen-2018-irf-stat-review-abstract.md
33. mogensen-2018-irf-stat-review-summary.md
34. nowicka-2023-isgf3-stat2-irf9-genome-abstract.md
35. nowicka-2023-isgf3-stat2-irf9-genome-fulltext.txt
36. nowicka-2023-isgf3-stat2-irf9-genome-summary.md
37. oladunni-2019-ehv1-ifn-equine-abstract.md
38. oladunni-2019-ehv1-ifn-equine-summary.md
39. oladunni-2020-ehv4-ifn-abstract.md
40. oladunni-2020-ehv4-ifn-summary.md
41. paul-2018-irf9-structure-regulation-abstract.md
42. paul-2018-irf9-structure-regulation-fulltext.txt
43. paul-2018-irf9-structure-regulation-summary.md
44. platanitis-2019-stat2-irf9-switch-abstract.md
45. platanitis-2019-stat2-irf9-switch-fulltext.txt
46. platanitis-2019-stat2-irf9-switch-summary.md
47. refseq-XP_014724060-record.gp
48. rengachari-2018-irf9-stat2-structure-abstract.md
49. rengachari-2018-irf9-stat2-structure-fulltext.txt
50. rengachari-2018-irf9-stat2-structure-summary.md
51. suhara-1996-mouse-isgf3gamma-cdna-abstract.md
52. suhara-1996-mouse-isgf3gamma-cdna-summary.md
53. tang-2007-acetylation-ifnar-abstract.md
54. tang-2007-acetylation-ifnar-summary.md
55. uniprot-A0A9L0I7X9-entry.txt
56. uniprot-A0A9L0I7X9-sequence.fasta
57. uniprot-A0A9L0I7X9-summary.md
58. uniprot-Q00978-human-IRF9-sequence.fasta
59. uniprot-Q61179-mouse-IRF9-sequence.fasta
60. uniprot-equus-IRF9-isoforms-sequences.fasta
61. uniprot-other-laurasiatheria-IRF9-sequences.fasta
62. veals-1992-isgf3gamma-irf-myb-abstract.md
63. veals-1992-isgf3gamma-irf-myb-summary.md
64. veals-1993-isgf3gamma-two-domains-abstract.md
65. veals-1993-isgf3gamma-two-domains-summary.md
66. wang-2020-donkey-genomes-abstract.md
67. wang-2020-donkey-genomes-summary.md
68. wang-2020-flavivirus-ns5-stat2-abstract.md
69. wang-2020-flavivirus-ns5-stat2-summary.md