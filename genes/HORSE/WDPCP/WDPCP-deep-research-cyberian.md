---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:40:35.195976'
end_time: '2026-10-26T03:48:42.675481'
duration_seconds: 487.48
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: WDPCP
  gene_symbol: WDPCP
  uniprot_accession: A0A3Q2KRK8
  protein_description: 'SubName: Full=WD repeat containing planar cell polarity effector
    {ECO:0000313|Ensembl:ENSECAP00000026115.2};'
  gene_info: Name=WDPCP {ECO:0000313|Ensembl:ENSECAP00000026115.2, ECO:0000313|VGNC:VGNC:51427};
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the WD repeat fritz family.
  protein_domains: Frtz. (IPR024511); WD40_repeat_dom_sf. (IPR036322); Frtz (PF11768)
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
citation_count: 63
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A3Q2KRK8
- **Protein Description:** SubName: Full=WD repeat containing planar cell polarity effector {ECO:0000313|Ensembl:ENSECAP00000026115.2};
- **Gene Information:** Name=WDPCP {ECO:0000313|Ensembl:ENSECAP00000026115.2, ECO:0000313|VGNC:VGNC:51427};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the WD repeat fritz family.
- **Key Domains:** Frtz. (IPR024511); WD40_repeat_dom_sf. (IPR036322); Frtz (PF11768)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "WDPCP" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'WDPCP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **WDPCP** (gene ID: WDPCP, UniProt: A0A3Q2KRK8) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# WDPCP (Fritz / BBS15 / CPLANE5) in the Horse, *Equus caballus* (UniProt A0A3Q2KRK8)

## 1. Introduction and Summary

The horse protein A0A3Q2KRK8 is an unreviewed (TrEMBL) entry derived from the Ensembl annotation of the Thoroughbred reference genome. It is named "WD repeat containing planar cell polarity effector" (gene symbol *WDPCP*, VGNC:51427), maps to horse chromosome 15, and is classified in the WD repeat fritz family with the Frtz domain (IPR024511, PF11768) and a WD40-repeat superfamily signature [uniprot-A0A3Q2KRK8-entry][wade-2009-horse-genome-abstract]. The identity check required by this task is satisfied: the symbol, description, family and domains all point to the same protein, the vertebrate orthologue of *Drosophila* Fritz. My own global alignment shows that the 705-residue horse protein is about 88% identical to human WDPCP (O95876) and 78% identical to mouse Wdpcp (Q8C456) [notes-sequence-analysis]. No literature describes horse WDPCP experimentally. Its function therefore has to be inferred from orthologues in human, mouse, *Xenopus* and *Drosophila*. Because the protein is highly conserved and the functional evidence from those species is consistent, that inference is well supported.

Across these species the evidence points to a single description. WDPCP is a non-enzymatic scaffold built from a WD40 β-propeller and an α-solenoid. It is one end of the crescent-shaped CPLANE (ciliogenesis and planar polarity effector) complex, in which it binds Inturned (INTU), which in turn binds Fuzzy (FUZ) and the Rab-like GTPase RSG1 [langousis-2022-cplane-structure-fulltext]. The complex works at the base of the cilium. With JBTS17/CPLANE1 it recruits the peripheral subunits of intraflagellar transport complex A (IFT-A) to basal bodies, which is needed for axonemal IFT, ciliogenesis and Hedgehog signalling [toriyama-2016-cplane-ift-fulltext][choi-2025-wdpcp-residues-fulltext]. WDPCP also regulates the septin and actin cytoskeleton. It is needed to recruit septins (SEPT2, SEPT7) to the ciliary transition zone and to the cell cortex, and to organize actin, focal adhesions and directional cell migration [kim-2010-fritz-septins-abstract][cui-2013-wdpcp-actin-fulltext][park-2015-wdpcp-cortex-abstract]. In flies, where its effects on cilia are minor, Fritz is a planar polarity effector. It works downstream of the core PCP proteins Frizzled, Dishevelled and Strabismus to restrict actin-based hair initiation to the distal edge of each wing cell [collier-2005-fritz-drosophila-abstract][strutt-2008-mwh-abstract]. In humans, loss of WDPCP causes ciliopathies, namely Bardet-Biedl syndrome 15 and an oral-facial-digital spectrum disorder [kim-2010-fritz-septins-abstract][saari-2015-wdpcp-chdthp-abstract][toriyama-2016-cplane-ift-fulltext].

## 2. Identity, Evolution and Domain Architecture

The horse *WDPCP* gene model (ENSECAG00000019956) comes from the 2009 horse genome assembly. The UniProt entry has no curated functional annotation. Its subcellular location (cell membrane; cilium axoneme) is assigned automatically by ARBA rules [uniprot-A0A3Q2KRK8-entry][wade-2009-horse-genome-abstract]. The reviewed human orthologue, O95876, is described as a probable PCP effector that regulates the septin cytoskeleton in ciliogenesis and collective cell movement. It is a core CPLANE component that recruits peripheral IFT-A proteins to basal bodies, and it binds monophosphorylated phosphoinositides [uniprot-O95876-human-WDPCP-entry]. UniProt notes that the human initiator methionine may be Met-1 or Met-34. The horse protein begins at a position equivalent to the shorter mouse form. It lacks the roughly 35-residue N-terminal extension that the cryo-EM study found unresolved in human WDPCP [notes-sequence-analysis][langousis-2022-cplane-structure-fulltext].

Fritz was first described in *Drosophila* as "a novel but evolutionarily conserved coiled-coil WD40 protein" [collier-2005-fritz-drosophila-abstract]. Fritz, Inturned and Fuzzy are conserved across metazoans [toriyama-2016-cplane-ift-fulltext]. The cnidarian orthologues of Intu, Fuz and Wdpcp resemble their vertebrate counterparts more closely than the *Drosophila* proteins do. Orthologues of the CPLANE partners Rsg1 and Jbts17 are found in cnidarians but not in *Drosophila*. Adler and Wallingford argue from this that the fly situation is derived and that a ciliogenic role is ancestral [adler-2017-ppe-cplane-review-fulltext]. Kim et al. had earlier predicted a β-propeller fold for human Fritz (then called C2orf86) [kim-2010-fritz-septins-fulltext]. The cryo-EM structure clarified the fold. WDPCP forms a seven-bladed WD40 β-propeller closed by an unusual N- and C-terminal "Velcro" strand arrangement. This is followed by an array of α-helices classified as an α-solenoid. The C-terminal ~100 residues are predicted to be intrinsically disordered and were not resolved [langousis-2022-cplane-structure-fulltext]. Langousis and colleagues noted that a β-propeller followed by an α-solenoid is typical of vesicle-trafficking and protocoatomer-associated proteins [langousis-2022-cplane-structure-fulltext]. AlphaFold2 models of mouse WDPCP predict the same propeller and C-terminal helices. In those models, a conserved D481/W482 motif (human N512/W513) lies at the junction of two α-helices in the linker region [choi-2025-wdpcp-residues-fulltext]. WDPCP has no catalytic motif. Its "primary function" is therefore that of a structural adaptor and scaffold within a multiprotein complex, not that of an enzyme or transporter.

## 3. The CPLANE Complex: Molecular Partners and Biochemistry

The main molecular context for WDPCP is the CPLANE complex. In *Drosophila*, Inturned, Fuzzy and Fritz interact physically and modulate each other's accumulation [wang-2014-ppe-interact-abstract]. Inturned binds both Fuzzy and Fritz in yeast two-hybrid assays, and anti-Frtz antibodies co-immunoprecipitate Inturned from fly tissue [wang-2014-ppe-interact-fulltext]. The complex is therefore held together by direct In–Frtz and In–Fy interactions [wang-2017-fritz-dishevelled-abstract]. In mammalian cells, LAP-tag affinity purification from ciliated IMCD3 cells showed that Intu, Fuz and Wdpcp co-purify reciprocally in all combinations. They also associate with the ciliopathy protein Jbts17 (CPLANE1), the GTPase Rsg1, and all six IFT-A subunits [toriyama-2016-cplane-ift-fulltext]. Toriyama and colleagues named this module CPLANE [toriyama-2016-cplane-ift-abstract]. Later work refined the composition of the complex. In IMCD3 cells, affinity purification with GTP-competent Rsg1 recovers Fuz, Intu, Wdpcp and Jbts17, as well as the transition-zone BAR-domain protein Fam92. GDP-locked Rsg1(T69N) loses all of these CPLANE interactions, so RSG1's association with the WDPCP-containing complex depends on its nucleotide state [vazquez-2025-rsg1-tz-fulltext]. A deep-learning model of the complete five-subunit complex, including the large JBTS17 subunit, predicts that JBTS17 contacts three other CPLANE members directly [gardner-2026-cplane-predicted-abstract]. That model has not yet been tested experimentally for WDPCP.

Langousis et al. (2022) reconstituted the human WDPCP–INTU–FUZ complex and the mouse Wdpcp–Intu–Fuz–Rsg1 complex from full-length recombinant proteins. They solved both by cryo-EM at 3.35 Å. The complex is crescent-shaped, with subunits arranged linearly as Wdpcp–Intu–Fuz–Rsg1 [langousis-2022-cplane-structure-fulltext]. WDPCP sits at one end of the crescent. Its α-helical domain makes a large interface of about 2,609 Å² with longin domain 2 of INTU, stabilized by charge complementarity between a positively charged WDPCP patch (H466, R502, K541, R544 in human) and a negatively charged INTU surface [langousis-2022-cplane-structure-fulltext]. WDPCP does not contact RSG1 directly. INTU and FUZ form a heterodimer through triplicated longin domains. Bioinformatic and biochemical studies show this heterodimer is homologous to the Mon1–Ccz1/HPS1–HPS4 ("HerMon") family and can act as a GEF for Rab23 [sanchezpulido-2020-hexalongin-abstract][gerondopoulos-2019-rab23-gef-abstract]. Langousis et al. therefore proposed that CPLANE acts as a Rab signalling hub. In this model the complex is an effector of RSG1 at the FUZ site and a GEF for Rab23 at the INTU–FUZ site, while WDPCP provides a binding platform and a membrane-binding module [langousis-2022-cplane-structure-fulltext].

The only defined biochemical activity of WDPCP is lipid binding. The CPLANE complex and each of its subunits, including isolated mouse Wdpcp, bind phosphoinositides with a single phosphate on the inositol ring. The order of preference is PI(3)P > PI(5)P > PI(4)P [langousis-2022-cplane-structure-fulltext]. A C-terminal WDPCP fragment (human residues 485–746, the helical/disordered region) is enough for this binding. The BBS-associated variant S708F, in the PIP-binding C-terminal tail, increases PIP binding without changing specificity [langousis-2022-cplane-structure-fulltext]. Disease missense variants mapped onto the structure did not prevent assembly of the complex in vitro [langousis-2022-cplane-structure-fulltext]. This suggests that at least some pathogenic variants change how the complex is regulated or engages membranes, not whether it forms. The horse protein is 88% identical to human WDPCP and contains the full propeller–solenoid region and C-terminal tail [notes-sequence-analysis]. It is therefore expected to assemble the same complex and bind lipids in the same way, although this has not been tested.

## 4. Function in Ciliogenesis and Intraflagellar Transport

In vertebrates, the best-documented role of WDPCP is in building primary and motile cilia. Kim et al. (2010) showed in *Xenopus* that Fritz is required for ciliogenesis and that it acts by controlling where septins localize [kim-2010-fritz-septins-abstract]. In multiciliated epidermal cells, Fritz and Sept7 were found along axonemes and in ring-like foci near basal bodies. These foci are consistent with the septin diffusion barrier at the ciliary base. After Fritz knockdown, cells had fewer and shorter cilia, the Sept7 structures were smaller and abnormally shaped, and Sept2 and Sept7 spread through the cytoplasm instead of staying at the apical surface. Knockdown of Sept2 or Sept7 also impaired ciliogenesis [kim-2010-fritz-septins-fulltext]. In mice, the ENU-induced *Wdpcp^Cys40* mutant has few cilia in kidney collecting duct, neuroepithelium and embryonic fibroblasts [cui-2013-wdpcp-actin-fulltext]. An antibody to Wdpcp labelled the ciliary axoneme and a ring at the ciliary base in IMCD3 cells. In the rare cilia that formed in mutant cells, the transition-zone proteins Sept2 and Mks1 were missing and Nphp1 was mislocalized to the basal body. This indicates that Wdpcp is needed to recruit transition-zone components [cui-2013-wdpcp-actin-fulltext]. Because septin rings at the transition zone act as a diffusion barrier for the ciliary compartment, failure to recruit Sept2 offers one mechanism for the ciliogenesis defect [cui-2013-wdpcp-actin-fulltext].

Toriyama et al. (2016) identified a second, IFT-specific mechanism. In *Xenopus* multiciliated cells, CPLANE proteins localize around basal bodies, and their recruitment is hierarchical. Jbts17 is at the top. Wdpcp and Intu come next and each needs the other to localize to the basal body. Fuz and Rsg1 lie downstream [toriyama-2016-cplane-ift-fulltext]. Without CPLANE, the peripheral IFT-A subunits are not recruited to basal bodies, an IFT-A core lacking those subunits enters the axoneme, and IFT-B forms stationary accumulations. Knockdown of Wdpcp alone disrupts IFT-B movement [toriyama-2016-cplane-ift-fulltext]. Disrupting CPLANE subunits also impairs basal-body docking, and CPLANE is generally required for normal transition-zone architecture [vazquez-2025-rsg1-tz-abstract][vazquez-2025-rsg1-tz-fulltext]. RSG1 acts at the most downstream step: its loss allows docking to ciliary vesicles but blocks extension of the axoneme. RSG1 needs INTU, TTBK2 and its own GTPase activity to reach the mother centriole [agbu-2018-rsg1-abstract]. Wdpcp therefore acts at the basal body and transition zone, where it helps assemble IFT trains, rather than in the axoneme.

These ciliary defects impair Hedgehog (Hh) signalling. In *Wdpcp-Z11* mice, which lack the conserved D481/W482 residues, ventral neural tube patterning is lost. Mutant fibroblasts do not induce *Gli1* in response to Smoothened agonist and cannot suppress GLI3 repressor processing. The mutant protein is made but fails to dock at the apical cell surface [choi-2025-wdpcp-residues-fulltext][choi-2025-wdpcp-residues-abstract]. Limb-mesenchyme-specific deletion of *Wdpcp* causes polydactyly, loss of Hh responsiveness and proliferation in skeletal progenitors, and delayed chondrogenesis and ossification [langhans-2021-wdpcp-limb-abstract]. In human sinonasal epithelium, WDPCP knockdown reduces the number and length of motile cilia along with Septin7 levels [ma-2017-wdpcp-sinonasal-abstract].

## 5. Planar Cell Polarity, Septins and the Actin Cytoskeleton

WDPCP was first identified as a planar polarity effector. In the *Drosophila* pupal wing, Fritz acts cell-autonomously downstream of the core PCP proteins. It controls both where prehairs initiate and how many form [collier-2005-fritz-drosophila-abstract]. The PPE proteins Inturned, Fuzzy and Fritz accumulate at the proximal cell edge as directed by the core PCP proteins. There, the proximal core protein Strabismus acts through them to stabilize Multiple Wing Hairs, an FH3-domain protein that suppresses actin, in apico-proximal regions. This confines hair formation to the distal vertex [strutt-2008-mwh-abstract][wang-2014-ppe-interact-abstract]. Fritz probably binds Dishevelled directly, which may connect core PCP to PPE localization. Fritz also has activity independent of Inturned, because mild Fritz overexpression partly rescues a precise *inturned* deletion [wang-2017-fritz-dishevelled-abstract]. Endogenously tagged Fritz is dynamic and concentrates in membrane puncta [wang-2017-fritz-dishevelled-abstract].

In vertebrates, WDPCP links PCP signalling to the septin and actin cytoskeleton. In *Xenopus*, Fritz-dependent septin localization is needed for convergent-extension cell movements [kim-2010-fritz-septins-abstract]. Fritz morphant mesodermal cells still aligned mediolaterally but failed to elongate, and their membranes undulated unstably. Knockdown of Sept2 or Sept7, or the septin inhibitor forchlorfenuron, reproduced these defects. Sept2 co-immunoprecipitated with Fritz from embryos, both proteins were concentrated at the cell cortex, and cortical Sept2 was reduced in Fritz morphants. Fritz therefore controls a specific subset of PCP behaviours, namely cell shape and cortical stability rather than polarization itself [kim-2010-fritz-septins-fulltext]. In epithelia, Wdpcp controls cortical septin localization and acts through actomyosin to maintain cortical tension and basolateral membrane stability [park-2015-wdpcp-cortex-abstract]. Mouse cell biology supports a direct cytoskeletal role. Cytoplasmic Wdpcp localizes along actin filaments, at the cell cortex and at focal adhesions, where it colocalizes with vinculin. It interacts with Sept2 and is required to recruit Sept2 to actin filaments. Mutant fibroblasts show reorganized actin, small rounded focal contacts, reduced membrane ruffling, failure to polarize, and loss of directional migration [cui-2013-wdpcp-actin-abstract][cui-2013-wdpcp-actin-fulltext]. *Wdpcp* mutant cochleae have PCP defects, including misoriented stereocilia and reduced asymmetric Vangl2, even though their kinocilia are normal. Cui et al. concluded that the PCP phenotype is a direct cytoskeletal effect, not a secondary effect of cilia loss [cui-2013-wdpcp-actin-fulltext]. Related work on the CPLANE partner Fuzzy shows that it recruits the RhoGAP ARHGAP35 to the basal body to limit actin polymerization during ciliogenesis [sharma-2024-fuzzy-actin-abstract]. This suggests a shared, complex-level mechanism by which CPLANE controls actin near the cilium. Langousis et al. noted that the role of CPLANE proteins in core vertebrate PCP signalling is "limited, if any" compared with their essential role in ciliogenesis [langousis-2022-cplane-structure-fulltext]. Even so, WDPCP is the CPLANE subunit most clearly linked to vertebrate PCP. Its loss disrupts the localization of the core PCP proteins Vangl2 in the mouse cochlea and Prickle2 in *Xenopus* multiciliated cells [adler-2017-ppe-cplane-review-fulltext]. The relative weight of the PCP and ciliary functions in mammals therefore remains under discussion [adler-2017-ppe-cplane-review-abstract].

## 6. Subcellular Localization

The localization data are consistent across systems. In mammalian cells, WDPCP is found at the ciliary transition zone, as a ring at the ciliary base, and in the axoneme [cui-2013-wdpcp-actin-fulltext]. In multiciliated cells it is concentrated around basal bodies [toriyama-2016-cplane-ift-fulltext]. Outside cilia it lies at the cell cortex and plasma membrane, along actin filaments, and at focal adhesions [cui-2013-wdpcp-actin-fulltext][park-2015-wdpcp-cortex-abstract]. Correct docking at the apical cell surface requires the conserved helical linker [choi-2025-wdpcp-residues-fulltext]. In fly wing cells, Fritz is enriched at the proximal cell edge and in membrane puncta [wang-2014-ppe-interact-abstract][wang-2017-fritz-dishevelled-abstract]. Its binding to PI(3)P and other monophosphorylated phosphoinositides offers a likely mechanism for its association with membranes [langousis-2022-cplane-structure-fulltext]. The automatic UniProt locations for the horse protein, cell membrane and cilium axoneme, agree with this picture but leave out the basal body and transition zone, which are probably its main sites of action [uniprot-A0A3Q2KRK8-entry][uniprot-O95876-human-WDPCP-entry].

## 7. Physiological Roles and Disease Relevance

Loss of WDPCP function in mammals produces a ciliopathy. *Wdpcp* mutant mice have anophthalmia, central polydactyly, kidney and other cysts, cardiac outflow tract and cloacal septation defects, and cochlear PCP defects, resembling Meckel-Gruber and Bardet-Biedl syndromes [cui-2013-wdpcp-actin-fulltext]. They also show oral-facial-digital features such as Y-shaped metacarpals and tongue and palate anomalies [toriyama-2016-cplane-ift-fulltext]. Wdpcp is needed in the epicardium for epithelial–mesenchymal transition and migration of epicardium-derived cells during coronary artery remodelling [liu-2018-wdpcp-epicardium-abstract]. In humans, *WDPCP* variants have been linked to Bardet-Biedl syndrome (BBS15) and as modifiers of BBS and MKS [kim-2010-fritz-septins-abstract][uniprot-O95876-human-WDPCP-entry]. The evidence is an enrichment of non-synonymous variants in MKS and BBS patients (6 alleles in 192 patients versus 0 in 384 controls) and a homozygous variant that segregated with disease in one BBS family [kim-2010-fritz-septins-fulltext]. Variants in all five CPLANE subunits have now been linked to ciliopathy, mostly within the oral-facial-digital spectrum [vazquez-2025-rsg1-tz-abstract]. Compound heterozygous variants cause congenital heart defects, tongue hamartomas and polysyndactyly (CHDTHP, OMIM 217085) [saari-2015-wdpcp-chdthp-abstract], and an OFD-like phenotype has also been reported [toriyama-2016-cplane-ift-fulltext]. No equine phenotype or variant in *WDPCP* has been reported in the sources reviewed here.

## 8. Inferred Function of Horse WDPCP

Several lines of evidence support transferring this functional model to the horse protein. Family membership and domain content match, the sequence is highly conserved (88% identical to human), and the full β-propeller, α-solenoid and C-terminal PIP-binding tail are present [notes-sequence-analysis][langousis-2022-cplane-structure-fulltext]. Function is also conserved from flies to mammals [collier-2005-fritz-drosophila-abstract][toriyama-2016-cplane-ift-fulltext]. Horse WDPCP is therefore expected to act as a non-catalytic scaffold subunit of the CPLANE complex, bound directly to INTU. With JBTS17/CPLANE1 at the basal body it would recruit peripheral IFT-A proteins and transition-zone and septin components needed for cilium assembly and Hh signalling. It would also act at the cell cortex and focal adhesions to organize septins and actin for polarized and collective cell movement. Membrane association would probably occur through binding to PI(3)P and related phosphoinositides. Appropriate GO-style annotations would include cilium assembly, septin cytoskeleton organization, establishment of planar polarity, and phosphatidylinositol-3-phosphate binding. Suitable localizations would be the ciliary basal body and transition zone, the axoneme, the cell cortex and focal adhesions, and membership of the CPLANE complex. All of these are inferred from orthologues, not shown for the horse protein.

## Open Questions

Several questions remain open. First, no study has examined horse WDPCP directly. Its expression pattern (Bgee lists oviduct epithelium among 23 tissues [uniprot-A0A3Q2KRK8-entry]), splice isoforms and naturally occurring variants are uncharacterized. Equine genomic resources could be screened for *WDPCP* variants in horses with polydactyly, retinal degeneration, renal cysts or congenital heart disease. Second, the molecular mechanism of WDPCP inside CPLANE is unclear. It is not known whether WDPCP only bridges INTU to membranes or whether it regulates the Rab23 GEF activity of INTU–FUZ or effector binding by RSG1, and no assay has yet tested how WDPCP affects this activity [langousis-2022-cplane-structure-fulltext][gerondopoulos-2019-rab23-gef-abstract]. Third, it is not known how the PCP/actin–septin function and the IFT-recruitment function are separated at the molecular level. Separation-of-function alleles, such as the D481/W482 linker deletion, together with structures of WDPCP bound to septins or JBTS17, would help answer this [choi-2025-wdpcp-residues-fulltext][cui-2013-wdpcp-actin-fulltext]. Fourth, it is unclear why the BBS-associated S708F variant increases phosphoinositide binding and how stronger membrane binding causes disease [langousis-2022-cplane-structure-fulltext]. The predicted structure of the complete complex with JBTS17 needs experimental testing, to find out whether WDPCP contacts JBTS17 directly and whether that contact accounts for the JBTS17-dependent recruitment of WDPCP to the basal body [gardner-2026-cplane-predicted-abstract][toriyama-2016-cplane-ift-fulltext]. It is also unknown whether WDPCP's lipid binding works together with the membrane-shaping transition-zone protein FAM92, which is recruited through RSG1 [vazquez-2025-rsg1-tz-fulltext]. Finally, the direct Fritz–Dishevelled interaction described in *Drosophila* has not been tested in vertebrates [wang-2017-fritz-dishevelled-abstract].

## References

- **uniprot-A0A3Q2KRK8-entry**: UniProtKB/TrEMBL entry A0A3Q2KRK8_HORSE (WDPCP, *Equus caballus*), entry version 35. https://rest.uniprot.org/uniprotkb/A0A3Q2KRK8.txt
- **uniprot-O95876-human-WDPCP-entry**: UniProtKB/Swiss-Prot entry O95876 (WDPCP, *Homo sapiens*). https://rest.uniprot.org/uniprotkb/O95876.txt
- **notes-sequence-analysis**: Author's own pairwise alignment of A0A3Q2KRK8 vs O95876 and Q8C456 (file `notes-sequence-analysis.md`).
- **collier-2005-fritz-drosophila**: Collier S, Lee H, Burgess R et al. (2005). The WD40 repeat protein fritz links cytoskeletal planar polarity to frizzled subcellular localization in the Drosophila epidermis. *Genetics* 169:2035-45. PMID: 15654087; PMCID: PMC1449578; DOI: 10.1534/genetics.104.033381 (https://doi.org/10.1534/genetics.104.033381)
- **kim-2010-fritz-septins**: Kim SK, Shindo A, Park TJ et al. (2010). Planar cell polarity acts through septins to control collective cell movement and ciliogenesis. *Science* 329:1337-40. PMID: 20671153; PMCID: PMC3509789; DOI: 10.1126/science.1191184 (https://doi.org/10.1126/science.1191184)
- **cui-2013-wdpcp-actin**: Cui C, Chatterjee B, Lozito TP et al. (2013). Wdpcp, a PCP protein required for ciliogenesis, regulates directional cell migration and cell polarity by direct modulation of the actin cytoskeleton. *PLoS Biol* 11:e1001720. PMID: 24302887; PMCID: PMC3841097; DOI: 10.1371/journal.pbio.1001720 (https://doi.org/10.1371/journal.pbio.1001720)
- **park-2015-wdpcp-cortex**: Park TJ, Kim SK, Wallingford JB (2015). The planar cell polarity effector protein Wdpcp (Fritz) controls epithelial cell cortex dynamics via septins and actomyosin. *Biochem Biophys Res Commun* 456:562-6. PMID: 25436430; PMCID: PMC4429777; DOI: 10.1016/j.bbrc.2014.11.078 (https://doi.org/10.1016/j.bbrc.2014.11.078)
- **wang-2014-ppe-interact**: Wang Y, Yan J, Lee H et al. (2014). The proteins encoded by the Drosophila Planar Polarity Effector genes inturned, fuzzy and fritz interact physically and can re-pattern the accumulation of "upstream" Planar Cell Polarity proteins. *Dev Biol* 394:156-69. PMID: 25072625; PMCID: PMC4163512; DOI: 10.1016/j.ydbio.2014.07.013 (https://doi.org/10.1016/j.ydbio.2014.07.013)
- **wang-2017-fritz-dishevelled**: Wang Y, Naturale VF, Adler PN (2017). Planar Cell Polarity Effector Fritz Interacts with Dishevelled and Has Multiple Functions in Regulating PCP. *G3 (Bethesda)* 7:1323-1337. PMID: 28258110; PMCID: PMC5386880; DOI: 10.1534/g3.116.038695 (https://doi.org/10.1534/g3.116.038695)
- **toriyama-2016-cplane-ift**: Toriyama M, Lee C, Taylor SP et al. (2016). The ciliopathy-associated CPLANE proteins direct basal body recruitment of intraflagellar transport machinery. *Nat Genet* 48:648-56. PMID: 27158779; PMCID: PMC4978421; DOI: 10.1038/ng.3558 (https://doi.org/10.1038/ng.3558)
- **langousis-2022-cplane-structure**: Langousis G, Cavadini S, Boegholm N et al. (2022). Structure of the ciliogenesis-associated CPLANE complex. *Sci Adv* 8:eabn0832. PMID: 35427153; PMCID: PMC9012472; DOI: 10.1126/sciadv.abn0832 (https://doi.org/10.1126/sciadv.abn0832)
- **gerondopoulos-2019-rab23-gef**: Gerondopoulos A, Strutt H, Stevenson NL et al. (2019). Planar Cell Polarity Effector Proteins Inturned and Fuzzy Form a Rab23 GEF Complex. *Curr Biol* 29:3323-3330.e8. PMID: 31564489; PMCID: PMC6864590; DOI: 10.1016/j.cub.2019.07.090 (https://doi.org/10.1016/j.cub.2019.07.090)
- **sanchezpulido-2020-hexalongin**: Sanchez-Pulido L, Ponting CP (2020). Hexa-Longin domain scaffolds for inter-Rab signalling. *Bioinformatics* 36:990-993. PMID: 31562761; PMCID: PMC7703760; DOI: 10.1093/bioinformatics/btz739 (https://doi.org/10.1093/bioinformatics/btz739)
- **choi-2025-wdpcp-residues**: Choi YJ, Hwang S, Lee C et al. (2025). Identification of conserved residues essential for the ciliogenic functions of WDPCP. *Dis Model Mech* 18:. PMID: 41268724; PMCID: PMC12673966; DOI: 10.1242/dmm.052149 (https://doi.org/10.1242/dmm.052149)
- **langhans-2021-wdpcp-limb**: Langhans MT, Gao J, Tang Y et al. (2021). Wdpcp regulates cellular proliferation and differentiation in the developing limb via hedgehog signaling. *BMC Dev Biol* 21:10. PMID: 34225660; PMCID: PMC8258940; DOI: 10.1186/s12861-021-00241-9 (https://doi.org/10.1186/s12861-021-00241-9)
- **liu-2018-wdpcp-epicardium**: Liu X, Wang Y, Liu F et al. (2018). Wdpcp promotes epicardial EMT and epicardium-derived cell migration to facilitate coronary artery remodeling. *Sci Signal* 11:. PMID: 29487191; DOI: 10.1126/scisignal.aah5770 (https://doi.org/10.1126/scisignal.aah5770)
- **saari-2015-wdpcp-chdthp**: Saari J, Lovell MA, Yu HC et al. (2015). Compound heterozygosity for a frame shift mutation and a likely pathogenic sequence variant in the planar cell polarity—ciliogenesis gene WDPCP in a girl with polysyndactyly, coarctation of the aorta, and tongue hamartomas. *Am J Med Genet A* 167A:421-7. PMID: 25427950; DOI: 10.1002/ajmg.a.36852 (https://doi.org/10.1002/ajmg.a.36852)
- **adler-2017-ppe-cplane-review**: Adler PN, Wallingford JB (2017). From Planar Cell Polarity to Ciliogenesis and Back: The Curious Tale of the PPE and CPLANE proteins. *Trends Cell Biol* 27:379-390. PMID: 28153580; PMCID: PMC5403552; DOI: 10.1016/j.tcb.2016.12.001 (https://doi.org/10.1016/j.tcb.2016.12.001)
- **martinsalazar-2022-cplane-review**: Martín-Salazar JE, Valverde D (2022). CPLANE Complex and Ciliopathies. *Biomolecules* 12:. PMID: 35740972; PMCID: PMC9221175; DOI: 10.3390/biom12060847 (https://doi.org/10.3390/biom12060847)
- **strutt-2008-mwh**: Strutt D, Warrington SJ (2008). Planar polarity genes in the Drosophila wing regulate the localisation of the FH3-domain protein Multiple Wing Hairs to control the site of hair production. *Development* 135:3103-11. PMID: 18701542; PMCID: PMC2556872; DOI: 10.1242/dev.025205 (https://doi.org/10.1242/dev.025205)
- **sharma-2024-fuzzy-actin**: Sharma R, Kalot R, Levin Y et al. (2024). The CPLANE protein Fuzzy regulates ciliogenesis by suppressing actin polymerization at the base of the primary cilium via p190A RhoGAP. *Development* 151:. PMID: 38546045; PMCID: PMC11006408; DOI: 10.1242/dev.202322 (https://doi.org/10.1242/dev.202322)
- **ma-2017-wdpcp-sinonasal**: Ma Y, Sun Y, Jiang L et al. (2017). WDPCP regulates the ciliogenesis of human sinonasal epithelial cells in chronic rhinosinusitis. *Cytoskeleton (Hoboken)* 74:82-90. PMID: 28001338; DOI: 10.1002/cm.21351 (https://doi.org/10.1002/cm.21351)
- **wade-2009-horse-genome**: Wade CM, Giulotto E, Sigurdsson S et al. (2009). Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science* 326:865-7. PMID: 19892987; PMCID: PMC3785132; DOI: 10.1126/science.1178158 (https://doi.org/10.1126/science.1178158)
- **gardner-2026-cplane-predicted**: Gardner T, Prolomova A, Lee C et al. (2026). Predicted structure of the complete CPLANE complex reveals novel interactors and mechanisms of Jbts17 during ciliogenesis. *Mol Biol Cell* :mbcE26050212. PMID: 42911922; DOI: 10.1091/mbc.E26-05-0212 (https://doi.org/10.1091/mbc.E26-05-0212)
- **vazquez-2025-rsg1-tz**: Vazquez N, Lee C, Valenzuela I et al. (2025). The human ciliopathy protein RSG1 links the CPLANE complex to transition zone architecture. *Nat Commun* 16:5701. PMID: 40593758; PMCID: PMC12219219; DOI: 10.1038/s41467-025-61005-8 (https://doi.org/10.1038/s41467-025-61005-8)
- **agbu-2018-rsg1**: Agbu SO, Liang Y, Liu A et al. (2018). The small GTPase RSG1 controls a final step in primary cilia initiation. *J Cell Biol* 217:413-427. PMID: 29038301; PMCID: PMC5748968; DOI: 10.1083/jcb.201604048 (https://doi.org/10.1083/jcb.201604048)


## Citations

1. adler-2017-ppe-cplane-review-abstract.md
2. adler-2017-ppe-cplane-review-fulltext.txt
3. adler-2017-ppe-cplane-review-summary.md
4. agbu-2018-rsg1-abstract.md
5. agbu-2018-rsg1-summary.md
6. choi-2025-wdpcp-residues-abstract.md
7. choi-2025-wdpcp-residues-fulltext.txt
8. choi-2025-wdpcp-residues-summary.md
9. collier-2005-fritz-drosophila-abstract.md
10. collier-2005-fritz-drosophila-summary.md
11. cui-2013-wdpcp-actin-abstract.md
12. cui-2013-wdpcp-actin-fulltext.txt
13. cui-2013-wdpcp-actin-summary.md
14. gardner-2026-cplane-predicted-abstract.md
15. gardner-2026-cplane-predicted-summary.md
16. gerondopoulos-2019-rab23-gef-abstract.md
17. gerondopoulos-2019-rab23-gef-fulltext.txt
18. gerondopoulos-2019-rab23-gef-summary.md
19. kim-2010-fritz-septins-abstract.md
20. kim-2010-fritz-septins-fulltext.txt
21. kim-2010-fritz-septins-summary.md
22. langhans-2021-wdpcp-limb-abstract.md
23. langhans-2021-wdpcp-limb-fulltext.txt
24. langhans-2021-wdpcp-limb-summary.md
25. langousis-2022-cplane-structure-abstract.md
26. langousis-2022-cplane-structure-fulltext.txt
27. langousis-2022-cplane-structure-summary.md
28. liu-2018-wdpcp-epicardium-abstract.md
29. liu-2018-wdpcp-epicardium-summary.md
30. ma-2017-wdpcp-sinonasal-abstract.md
31. ma-2017-wdpcp-sinonasal-summary.md
32. martinsalazar-2022-cplane-review-abstract.md
33. martinsalazar-2022-cplane-review-fulltext.txt
34. martinsalazar-2022-cplane-review-summary.md
35. park-2015-wdpcp-cortex-abstract.md
36. park-2015-wdpcp-cortex-fulltext.txt
37. park-2015-wdpcp-cortex-summary.md
38. saari-2015-wdpcp-chdthp-abstract.md
39. saari-2015-wdpcp-chdthp-summary.md
40. sanchezpulido-2020-hexalongin-abstract.md
41. sanchezpulido-2020-hexalongin-fulltext.txt
42. sanchezpulido-2020-hexalongin-summary.md
43. sharma-2024-fuzzy-actin-abstract.md
44. sharma-2024-fuzzy-actin-fulltext.txt
45. sharma-2024-fuzzy-actin-summary.md
46. strutt-2008-mwh-abstract.md
47. strutt-2008-mwh-summary.md
48. toriyama-2016-cplane-ift-abstract.md
49. toriyama-2016-cplane-ift-fulltext.txt
50. toriyama-2016-cplane-ift-summary.md
51. uniprot-A0A3Q2KRK8-entry.txt
52. uniprot-O95876-human-WDPCP-entry.txt
53. vazquez-2025-rsg1-tz-abstract.md
54. vazquez-2025-rsg1-tz-fulltext.txt
55. vazquez-2025-rsg1-tz-summary.md
56. wade-2009-horse-genome-abstract.md
57. wade-2009-horse-genome-summary.md
58. wang-2014-ppe-interact-abstract.md
59. wang-2014-ppe-interact-fulltext.txt
60. wang-2014-ppe-interact-summary.md
61. wang-2017-fritz-dishevelled-abstract.md
62. wang-2017-fritz-dishevelled-fulltext.txt
63. wang-2017-fritz-dishevelled-summary.md