---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:04:39.011969'
end_time: '2026-10-26T01:15:53.859142'
duration_seconds: 674.85
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: TGFBR3
  gene_symbol: TGFBR3
  uniprot_accession: A0A8C4M6Z6
  protein_description: 'RecName: Full=Transforming growth factor beta receptor type
    3 {ECO:0000256|ARBA:ARBA00074526}; AltName: Full=Betaglycan {ECO:0000256|ARBA:ARBA00083071};
    AltName: Full=Transforming growth factor beta receptor III {ECO:0000256|ARBA:ARBA00082717};'
  gene_info: Name=TGFBR3 {ECO:0000313|Ensembl:ENSEASP00005022721.2};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Not specified in UniProt
  protein_domains: TGFBR3/Endoglin-like_N. (IPR058899); ZP-C. (IPR055355); ZP-C_dom.
    (IPR042235); ZP-N. (IPR055356); ZP_chr. (IPR048290)
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
citation_count: 90
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A8C4M6Z6
- **Protein Description:** RecName: Full=Transforming growth factor beta receptor type 3 {ECO:0000256|ARBA:ARBA00074526}; AltName: Full=Betaglycan {ECO:0000256|ARBA:ARBA00083071}; AltName: Full=Transforming growth factor beta receptor III {ECO:0000256|ARBA:ARBA00082717};
- **Gene Information:** Name=TGFBR3 {ECO:0000313|Ensembl:ENSEASP00005022721.2};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** TGFBR3/Endoglin-like_N. (IPR058899); ZP-C. (IPR055355); ZP-C_dom. (IPR042235); ZP-N. (IPR055356); ZP_chr. (IPR048290)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TGFBR3" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TGFBR3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TGFBR3** (gene ID: TGFBR3, UniProt: A0A8C4M6Z6) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TGFBR3 (Betaglycan) in the Donkey, *Equus asinus* (UniProt A0A8C4M6Z6): A Functional Annotation Review

## 1. Introduction and Summary

The donkey protein in UniProt entry A0A8C4M6Z6 is the *Equus asinus* ortholog of transforming growth factor beta receptor type III (TGFBR3), also called betaglycan. The entry is an unreviewed TrEMBL record. Its sequence is a gene model that Ensembl predicted from the chromosome-level Dezhou donkey genome assembly [wang-2020-donkey-genome-abstract], and that genome paper does not discuss TGFBR3 at all; a full-text search found no mention of TGFBR3 or betaglycan [wang-2020-donkey-genome-fulltext]. I found no experimental study of betaglycan function in donkeys, horses or other equids. The only equid-specific evidence is bioinformatic: a 2026 genome-wide survey of the donkey TGF-beta superfamily lists a donkey TGFBR3 protein [donkey-2026-tgfb-gene-family-fulltext]. There is also transcript-level evidence: single-cell RNA-seq of horse ovaries identifies TGFBR3 as a marker of ovarian stromal cells [kazakh-2025-horse-ovary-scrna-fulltext]. Everything this report says about the donkey protein's function is therefore inferred from orthology. The inference is strong: my alignment of the donkey and human sequences shows about 88% identity. The donkey protein keeps the domain architecture (signal peptide, orphan/endoglin-like N-terminal region, zona pellucida (ZP) domain, single transmembrane helix, short cytoplasmic tail). It also keeps both glycosaminoglycan (GAG) attachment serines, and its transmembrane–cytoplasmic segment is identical to the human one, including the threonine phosphorylated by TGFBR2 and the C-terminal PDZ-binding motif (see `SEQUENCE_NOTES.md`). The gene symbol is not ambiguous here: the UniProt description, InterPro domains (TGFBR3/Endoglin-like_N, ZP-N, ZP-C) and PANTHER family (PTHR14002:SF7) all point to betaglycan.

In mammals, betaglycan is a membrane-anchored proteoglycan and the most abundant cell-surface receptor for TGF-beta. It binds ligand but has no kinase activity of its own. Its main job is to act as a coreceptor, or "accessory receptor", for a subset of TGF-beta superfamily ligands. It binds all three TGF-beta isoforms with particularly high affinity for TGF-beta2. It presents them to the type II signaling kinase TGFBR2 and so potentiates assembly of the TGFBR2–TGFBR1 (ALK5) signaling complex and SMAD2/3 activation [lopezcasillas-1993-presents-ligand-abstract; wieteska-2025-structures-complex-assembly-abstract]. Betaglycan is also the coreceptor that lets inhibin A antagonize activin through activin type II receptors [lewis-2000-betaglycan-binds-inhibin-abstract; li-2018-inhibinA-coreceptor-gonadotropes-abstract], and it can act as a BMP coreceptor [kirkbride-2008-bmp-signal-tbr3-abstract]. Its ectodomain can be shed, and the resulting soluble betaglycan sequesters ligand and antagonizes TGF-beta [lopezcasillas-1994-dual-modulator-abstract; elderbroom-2014-shedding-required-abstract]. The cytoplasmic tail adds a further layer of control. Phosphorylation by TGFBR2 recruits beta-arrestin2 for endocytosis [chen-2003-beta-arrestin2-abstract], and the PDZ protein GIPC binds the tail and stabilizes betaglycan at the surface [blobe-2001-gipc-abstract]. The protein works at the cell surface, on the external side of the plasma membrane, and in endocytic compartments; in its soluble form it is found in the extracellular space and matrix.

## 2. Identity, Domain Architecture and Conservation of the Donkey Protein

Betaglycan was cloned in rat by two groups at the same time. Both described an 853-residue core protein with a large extracellular domain carrying GAG attachment sites, a single hydrophobic transmembrane domain, and a 41-residue cytoplasmic tail with no recognizable signaling motif [lopezcasillas-1991-betaglycan-structure-abstract; wang-1991-type3-expression-cloning-abstract]. When expressed, the protein appeared as a heterogeneous 280–330 kDa proteoglycan [wang-1991-type3-expression-cloning-abstract]. Its transmembrane and cytoplasmic regions resemble those of endoglin, the related endothelial coreceptor [lopezcasillas-1991-betaglycan-structure-abstract]. The murine ortholog (850 residues) is highly similar to the rat protein [ponce-1998-murine-betaglycan-gag-sites-abstract]. Later work divided the extracellular region into two domains: a membrane-distal "orphan" domain related to endoglin, and a juxtamembrane ZP domain related to uromodulin and the sperm receptors ZP2 and ZP3, joined by a disordered linker of about 85 residues [lopezcasillas-1994-dual-modulator-abstract; wieteska-2025-structures-complex-assembly-fulltext].

The 836-residue donkey sequence fits this architecture. UniProt annotates a SignalP signal peptide (residues 1–18), a ZP domain (454–729, PROSITE PS51034) and a Phobius-predicted transmembrane helix (770–794). It also carries InterPro signatures for the TGFBR3/Endoglin-like N-terminal region (IPR058899) and the ZP-N and ZP-C subdomains (IPR055356, IPR055355). In my pairwise alignment with human TGFBR3 (Q03167), the two GAG-attachment serines are conserved. These serines were mapped experimentally to Ser535 and Ser546 in rat [lopezcasillas-1994-dual-modulator-abstract] and Ser533 and Ser544 in mouse [ponce-1998-murine-betaglycan-gag-sites-abstract], and they fall at donkey Ser533 and Ser544. The last 50 residues, covering the transmembrane helix and the whole cytoplasmic tail, are identical between donkey and human. The alignment has one difference worth noting: a 14-residue segment in the juxtamembrane stalk of the human protein (about residues 762–775) is missing from the donkey model. That segment lies outside the mapped ligand-binding regions. Comparison with other ungulates indicates that this gap is most likely an artefact of the gene model, not a real feature of the donkey protein. The horse (F7E1V2) and cattle (E1B9H5) TGFBR3 sequences both contain the segment (horse ...QVESK-GPSIKEPSPISPP-IFHGLDTL...). The donkey model matches the horse sequence exactly on both sides of the gap, as would be expected if a short exon segment had been dropped. An independent annotation of the donkey assembly ASM1607732v2 also reports a 850-residue, ~93.2-kDa donkey TGFBR3 on chromosome 16 [donkey-2026-tgfb-gene-family-fulltext]. That is 14 residues longer than the 836-residue UniProt model and matches the human length closely. The canonical donkey betaglycan is therefore probably about 850 residues long with an intact juxtamembrane stalk (see `SEQUENCE_NOTES.md`). The membrane-proximal stretch upstream of the gap (...SMIWAMMQNKKTFTKPLAV...) is fully conserved. In TβRIII, this is the region where alanine/NAAIRS scanning identified residues needed for ectodomain shedding [elderbroom-2014-shedding-required-fulltext].

## 3. Ligand Recognition: Two Independent Binding Domains and Isoform Selectivity

Betaglycan binds TGF-beta through its core protein. The GAG chains are not needed for this [lopezcasillas-1991-betaglycan-structure-abstract], and GAG-free S535A/S546A mutants still bind TGF-beta and present it to the type II receptor [lopezcasillas-1994-dual-modulator-abstract]. The heparan sulfate chains instead give the proteoglycan a separate ligand-binding function: they bind basic FGF (FGF2). So one membrane proteoglycan can engage two growth-factor families through physically separate parts of the molecule, and cells can selectively tune the heparan sulfate content of betaglycan in response to bFGF [andres-1992-two-growth-factor-families-abstract].

Deletion mapping found two TGF-beta-binding regions. One is the N-terminal endoglin-related (orphan) region [lopezcasillas-1994-dual-modulator-abstract]. The other is a membrane-proximal region of about 253 residues that binds TGF-beta with full-length affinity [pepin-1994-ligand-binding-mapping-abstract]. Both regions prefer TGF-beta2 over TGF-beta1 and both can support TGF-beta2-dependent SMAD2 phosphorylation, but only the orphan region increases ligand labeling of TGFBR2 [esparza-2001-specialized-binding-regions-abstract]. Inhibin A binding sits only in the C-terminal ZP region, with relative affinities TGF-beta2 > inhibin A > TGF-beta1 [esparza-2001-specialized-binding-regions-abstract]. Wiater and colleagues narrowed the inhibin-binding site to residues 591–700 of the ZP domain, where it overlaps the ZP-region TGF-beta site. A single substitution, V614Y, abolished binding of both ligands to this domain. Full-length betaglycan carrying V614Y could no longer mediate inhibin antagonism but could still present TGF-beta to TGFBR2 through the orphan domain, which shows that the two coreceptor functions can be separated [wiater-2006-distinct-binding-sites-abstract]. Soluble recombinant betaglycan binds TGF-beta1 with a Kd of about 3.5 nM, with isoform preference TGF-beta2 > TGF-beta3 > TGF-beta1 [vilchis-2001-soluble-betaglycan-neutralizing-abstract].

Structural studies have explained much of this selectivity. The 2.0-Å crystal structure of the betaglycan ZP-C domain showed an immunoglobulin-like fold whose G strand is formed by the "external hydrophobic patch". Betaglycan also lacks the maturation cleavage site that lets other ZP proteins polymerize into matrix fibrils, which fits its role as a non-polymerizing coreceptor [lin-2011-zpc-structure-abstract]. NMR and binding studies placed the ZP-C binding site on the concave inner surface of the TGF-beta2 "fingers". The key residues there (Ile92, Lys97, Glu99) are specific to TGF-betas and the inhibin alpha subunit, which explains why BMP-2 binds ZP-C only weakly [henen-2019-tgfb2-zp-binding-abstract]. The orphan domain structure showed an insertion that blocks the surface endoglin uses to bind BMP-9. Betaglycan therefore binds its ligands in a completely different way from endoglin. It also exists as a monomer that forms 1:1 complexes with growth factor, whereas endoglin is a dimer forming 2:1 complexes [kim-2019-orphan-domain-abstract]. Wieteska et al. (2025) reported crystal and cryo-EM structures of TGF-beta bound to the betaglycan orphan and ZP-C domains, to full-length betaglycan at low resolution, and to the signaling receptors. These showed that the two domains bind the ligand dimer independently, at interfaces that differ from endoglin's, which reflects evolutionary adaptation for ligand selectivity [wieteska-2025-structures-complex-assembly-abstract]. The same work found no evidence that betaglycan helps release mature TGF-beta from its latent pro-complex, because the prodomain shields the growth-factor surfaces that betaglycan uses [wieteska-2025-structures-complex-assembly-fulltext].

## 4. Mechanism of TGF-beta Signal Potentiation: Ligand Presentation and Hand-off

The TGF-beta signaling receptor is a heteromeric complex of type II and type I serine/threonine kinases, and on its own it binds ligand poorly. This is especially true for TGF-beta2. López-Casillas, Wrana and Massagué showed that membrane betaglycan presents TGF-beta directly to the type II receptor kinase and forms a high-affinity ternary complex. This increases TGF-beta binding to the signaling receptor, enhances cell responsiveness, and removes the marked biological differences between TGF-beta isoforms [lopezcasillas-1993-presents-ligand-abstract]. Earlier expression in L6 myoblasts had already shown that the type III receptor raises the amount of ligand cross-linked to type II receptors [wang-1991-type3-expression-cloning-abstract]. Presentation needs membrane anchorage, but neither the GAG chains nor the cytoplasmic domain [lopezcasillas-1994-dual-modulator-abstract].

The 2025 structures give a stepwise model of this process. TGF-beta2 first binds the orphan domain and then the ZP-C domain. The orphan domain leaves one TGFBR2 site on the ligand open and raises TGF-beta2's affinity for TGFBR2. When TGFBR2 binds, it recruits TGFBR1 through the composite TGF-beta:TGFBR2 interface, and this displaces the orphan domain ("hand-off"). Because ZP-C blocks the binding sites of both TGFBR1 and TGFBR2 on its side of the dimer, it must also be displaced for the full heterotetrameric signaling complex to form [wieteska-2025-structures-complex-assembly-fulltext]. The model is consistent with earlier biochemistry showing that betaglycan selectively binds autophosphorylated TGFBR2, encourages it to pair with the type I receptor, and then dissociates from the active complex [blobe-2001-cytoplasmic-domain-abstract]. Computational and experimental work referenced in the 2025 paper describes a biphasic effect: low betaglycan levels potentiate TGF-beta2 signaling, while high levels oppose it [wieteska-2025-structures-complex-assembly-fulltext].

Genetic evidence supports a non-redundant role in TGF-beta2 signaling. Fibroblasts from Tgfbr3-null mouse embryos are selectively less sensitive to TGF-beta2, with weaker growth inhibition, reporter activation and SMAD2 nuclear localization, while responses to other ligands are unchanged [stenvers-2003-knockout-heart-liver-abstract]. In avian heart explants, antibodies against TβRIII blocked endocardial epithelial–mesenchymal transformation (EMT). Expressing TβRIII in ventricular endothelial cells, which normally do not transform, made them transform in response to TGF-beta2 [brown-1999-endocardial-transformation-abstract].

## 5. Coreceptor Functions Beyond TGF-beta: Inhibin A and BMPs

Activins signal through ActRII/IIB and ALK4, and inhibins antagonize them by binding ActRII without recruiting ALK4. Lewis et al. showed that betaglycan binds inhibin with high affinity, forms cross-linked complexes with inhibin and ActRII, and makes otherwise poorly responsive cells sensitive to inhibin. Betaglycan is therefore the coreceptor that makes inhibin a functional activin antagonist [lewis-2000-betaglycan-binds-inhibin-abstract]. In primary rat gonadotropes, knocking down or immunoneutralizing endogenous betaglycan cut the potency of inhibin A against activin-stimulated FSH secretion by more than 1000-fold, without changing activin responsiveness [wiater-2009-endogenous-betaglycan-gonadotropes-abstract]. Conditional deletion of Tgfbr3 in mouse gonadotropes refined this picture. Inhibin A, but not inhibin B, lost its ability to suppress FSH, and knockout females were supra-fertile [li-2018-inhibinA-coreceptor-gonadotropes-abstract]. The inhibin B coreceptor later turned out to be TGFBR3L, a separate gonadotrope-restricted protein. Mice lacking both TGFBR3L and betaglycan are infertile [brule-2021-tgfbr3l-inhibinB-abstract]. The "inhibin-betaglycan-ActRII complex" (GO:0034673) assigned to the donkey entry by electronic annotation therefore has strong experimental support in rodents.

Betaglycan also binds several BMP-family ligands directly. Kirkbride et al. reported binding to BMP-2, BMP-4, BMP-7 and GDF-5 through the same domains used for TGF-beta. Betaglycan increased ligand binding to BMP type I receptors, and silencing it weakened BMP-induced SMAD1 phosphorylation [kirkbride-2008-bmp-signal-tbr3-abstract]. It also controls where BMP type I receptors go in the cell. It binds ALK3 mainly through the ectodomain and keeps ALK3 at the cell surface. With ALK6, binding needs both the ectodomain and the cytoplasmic domain, and betaglycan drives beta-arrestin2-dependent internalization of ALK6, which gives maximal ALK6 signaling. The T841A mutant cannot support this [lee-2009-alk3-alk6-trafficking-abstract]. The BMP coreceptor role should be weighed against the structural finding that the betaglycan ZP-C domain binds BMP-2 "weakly or not at all" [henen-2019-tgfb2-zp-binding-abstract]. BMP engagement may therefore depend more on other parts of the protein, or on cellular context, than TGF-beta binding does.

## 6. The Cytoplasmic Domain: Phosphorylation, beta-Arrestin2, GIPC and Kinase-Independent Signaling

The short cytoplasmic tail was once thought to be functionally inert, but it has several regulatory roles. TGFBR2 binds the betaglycan tail and phosphorylates it in a kinase-dependent way. A betaglycan lacking the tail can still bind TGF-beta and TGFBR2 and can still enhance ligand binding, but it cannot enhance TGF-beta2 signaling [blobe-2001-cytoplasmic-domain-abstract]. Phosphorylation, most likely at Thr841 in rat numbering, creates a binding site for beta-arrestin2. This is analogous to the GRK–arrestin system of G protein-coupled receptors, except that the kinase here is TGFBR2 rather than a GRK. Beta-arrestin2 binding leads to co-internalization of betaglycan and TGFBR2 and down-regulation of TGF-beta signaling [chen-2003-beta-arrestin2-abstract]. Separately, the PDZ domain protein GIPC binds a class I PDZ-binding motif at the C-terminus. This raises betaglycan levels at the cell surface and enhances TGF-beta responses; removing the motif abolishes both effects [blobe-2001-gipc-abstract]. In endocardial cushion explants, betaglycan-mediated EMT in response to TGF-beta2 or BMP-2 needed the cytoplasmic domain, in particular the three C-terminal residues that bind GIPC. It also needed GIPC itself and the type I receptors ALK2, ALK3 and ALK5 [townsend-2012-gipc-endocardial-emt-abstract]. The donkey cytoplasmic tail is identical to the human one, so these interaction motifs (the phosphoacceptor threonine, donkey Thr825, and the C-terminal ...STA PDZ ligand) are expected to work in donkey cells too.

Through beta-arrestin2, betaglycan also has functions that do not need TGF-beta. It activates Cdc42, remodels the actin cytoskeleton and reduces directional persistence, and so inhibits random migration of epithelial and cancer cells [mythreye-2009-cdc42-abstract]. It forms a complex with active integrin α5β1 and drives beta-arrestin2-dependent internalization of α5β1 and its trafficking to nascent focal adhesions. This promotes adhesion to fibronectin and fibronectin fibrillogenesis without requiring TGF-beta or BMP [mythreye-2013-integrin-a5b1-abstract]. These scaffolding activities explain several UniProt subunit annotations (ITGA5:ITGB1, ARRB2, CDC42 activation) and the GO terms for regulation of cell migration.

## 7. Ectodomain Shedding and Soluble Betaglycan as a Ligand Antagonist

The betaglycan ectodomain can be released as a soluble proteoglycan [lopezcasillas-1991-betaglycan-structure-abstract], and soluble betaglycan occurs naturally in serum and extracellular matrix [vilchis-2001-soluble-betaglycan-neutralizing-abstract]. Shedding also depends on the GAG chains. A GAG-free S534A/S545A betaglycan is not shed, and the heparan sulfate chain in particular is required. Without shedding, betaglycan can no longer suppress TGF-beta signaling, and the metalloproteinase inhibitor TIMP3 was identified as an inhibitor of betaglycan shedding [choi-2024-gag-shedding-abstract]. Several proteases can generate soluble betaglycan. Pervanadate-stimulated shedding produces a 120-kDa fragment and a 90-kDa fragment, and MT1-MMP (or MT3-MMP) can generate the 90-kDa form. That form still prefers TGF-beta2 over TGF-beta1 [velasco-2004-shedding-mt1mmp-abstract]. Plasmin selectively cleaves betaglycan, but not TβRI or TβRII, releasing a 60-kDa fragment that carries TGF-beta from the cell surface [lamarre-1994-plasmin-cleaves-abstract]. After shedding, the remaining transmembrane–cytoplasmic stub is stable and is processed by gamma-secretase, and its accumulation blunts TGF-beta2 signaling [blair-2011-gamma-secretase-abstract].

Membrane-bound betaglycan presents ligand to the signaling receptors, but soluble betaglycan binds ligand without bringing it to the membrane. It therefore inhibits TGF-beta binding to cell-surface receptors and blocks TGF-beta action, most strongly for TGF-beta2 [lopezcasillas-1994-dual-modulator-abstract]. Recombinant soluble betaglycan neutralizes TGF-beta2 about ten times more potently than TGF-beta1 [vilchis-2001-soluble-betaglycan-neutralizing-abstract]. Mutants that cannot be shed, or are shed more readily, showed that the balance between soluble and membrane betaglycan is a key determinant of TGF-beta responsiveness and of betaglycan's suppressive effects on cancer cell migration, invasion and metastasis [elderbroom-2014-shedding-required-abstract]. Betaglycan is thus a "dual modulator": it enhances signaling at the membrane and antagonizes it once shed [lopezcasillas-1994-dual-modulator-abstract]. This explains why the donkey entry is annotated both to the external side of the plasma membrane and to the extracellular matrix and space.

## 8. Physiological Roles Revealed by Loss of Function

Knockout studies in mice show that betaglycan has essential roles in development. Tgfbr3-null embryos die in midgestation. From embryonic day 13.5 they develop lethal proliferative defects in the heart and apoptosis in the liver, the main embryonic sites of Tgfbr3 expression [stenvers-2003-knockout-heart-liver-abstract]. An independent null allele causes death at about E14.5 because coronary vasculogenesis fails. These embryos have an irregular, hypercellular epicardium and persistent blood islands, while yolk-sac and other embryonic vessels form normally [compton-2007-coronary-vessel-abstract]. Explant studies tie these phenotypes to betaglycan's role in endocardial and epicardial EMT driven by TGF-beta2 and BMP-2 [brown-1999-endocardial-transformation-abstract; townsend-2012-gipc-endocardial-emt-abstract]. In adults, betaglycan controls reproduction as the inhibin A coreceptor in pituitary gonadotropes [li-2018-inhibinA-coreceptor-gonadotropes-abstract; brule-2021-tgfbr3l-inhibinB-abstract]. Loss of betaglycan expression in many human cancers, and its tumor-suppressor-like activity, have been reviewed in detail [bernabeu-2009-coreceptors-cancer-review-abstract]. Equid phenotypes have not been studied. TGFBR3 transcripts are prominent in horse ovarian stromal cells [kazakh-2025-horse-ovary-scrna-fulltext], which fits a role in ovarian TGF-beta and inhibin signaling. The essential cardiovascular and reproductive roles are likely conserved, given that betaglycan is conserved from fish to mammals [kim-2019-orphan-domain-fulltext; wieteska-2025-structures-complex-assembly-fulltext].

## 9. Synthesis for Functional Annotation of A0A8C4M6Z6

Taken together, the evidence supports annotating the donkey TGFBR3 product as follows. It is a single-pass type I transmembrane proteoglycan coreceptor, located at the cell surface (external side of the plasma membrane) and, once shed, in the extracellular space and matrix. Its molecular functions are TGF-beta binding (strongest for TGF-beta2), type III TGF-beta receptor (coreceptor) activity, inhibin binding and coreceptor activity within the inhibin–betaglycan–ActRII complex, binding to the type II TGF-beta receptor, BMP binding, and binding of FGF2 through its heparan sulfate GAG chains. Its main biological role is to positively regulate TGF-beta receptor signaling by presenting and handing off ligand, and in particular to potentiate TGF-beta2–TGFBR2–ALK5–SMAD2/3 signaling. It also mediates inhibin A antagonism of activin signaling and modulates BMP–SMAD1/5/8 signaling. It can negatively regulate the same pathways through ectodomain shedding and beta-arrestin2-mediated endocytosis, and it regulates cell migration and adhesion through beta-arrestin2, Cdc42 and integrin α5β1 independently of ligand. None of these functions has been tested in donkey; they are transferred by orthology from rat, mouse and human, and the near-complete conservation of the relevant residues and domains supports the transfer. Betaglycan is not an enzyme. It has no catalytic activity, and its "receptor" function is ligand capture and presentation, not signal transduction by a kinase.

## 10. Open Questions

There is no experimental characterization of betaglycan in any equid. Ortholog comparison and an independent 850-residue donkey annotation suggest that the 836-residue Ensembl model (ENSEAST00005024650.2) lacks a short juxtamembrane exon segment [donkey-2026-tgfb-gene-family-fulltext]. This should be confirmed by mapping donkey RNA-seq reads (for example BioProject PRJNA1017964, used in that study) across the exon junction, and if confirmed the UniProt sequence should be corrected. A related question is whether a shorter splice isoform without the segment exists. Because the gap is in the stalk region near the shedding-sensitive juxtamembrane area [lopezcasillas-1991-betaglycan-structure-abstract; velasco-2004-shedding-mt1mmp-abstract], one could test whether it changes ectodomain shedding by MT1-MMP or plasmin. The donkey GAG composition (heparan sulfate versus chondroitin sulfate at Ser533/Ser544) is also unknown. Because heparan sulfate chains are needed for shedding [choi-2024-gag-shedding-abstract], tissue-specific GAG modification could set the balance between membrane-bound and soluble betaglycan in equid tissues. Equine reproductive endocrinology is economically important, so the balance of betaglycan (inhibin A) and TGFBR3L (inhibin B) coreceptor function in equid gonadotropes [li-2018-inhibinA-coreceptor-gonadotropes-abstract; brule-2021-tgfbr3l-inhibinB-abstract] deserves study. At the mechanistic level, several questions remain open in any species: how betaglycan engages BMPs given that ZP-C binds BMP-2 weakly [kirkbride-2008-bmp-signal-tbr3-abstract; henen-2019-tgfb2-zp-binding-abstract], how inhibin A binds ZP-C in structural terms, and whether the ZP-C domain is fully displaced or stays bound in active signaling complexes [wieteska-2025-structures-complex-assembly-fulltext]. Finally, an AlphaFold model exists for A0A8C4M6Z6. Comparing it with the experimental rat/zebrafish orphan-domain and ZP-C structures would be a low-cost way to confirm that the donkey ligand-binding interfaces are conserved.

## 11. References

- [wang-2020-donkey-genome] Wang C, Li H, Guo Y, et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nature Communications* 11:6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7. https://europepmc.org/article/MED/33293529
- [lopezcasillas-1991-betaglycan-structure] López-Casillas F, Cheifetz S, Doody J, Andres JL, Lane WS, Massagué J. (1991). Structure and expression of the membrane proteoglycan betaglycan, a component of the TGF-beta receptor system. *Cell* 67:785-795. PMID: 1657406; DOI: 10.1016/0092-8674(91)90073-8.
- [wang-1991-type3-expression-cloning] Wang XF, Lin HY, Ng-Eaton E, Downward J, Lodish HF, Weinberg RA. (1991). Expression cloning and characterization of the TGF-beta type III receptor. *Cell* 67:797-805. PMID: 1657407; DOI: 10.1016/0092-8674(91)90074-9.
- [andres-1992-two-growth-factor-families] Andres JL, DeFalcis D, Noda M, Massagué J. (1992). Binding of two growth factor families to separate domains of the proteoglycan betaglycan. *J Biol Chem* 267:5927-5930. PMID: 1556106; DOI: 10.1016/s0021-9258(18)42643-9.
- [lopezcasillas-1993-presents-ligand] López-Casillas F, Wrana JL, Massagué J. (1993). Betaglycan presents ligand to the TGF beta signaling receptor. *Cell* 73:1435-1444. PMID: 8391934; DOI: 10.1016/0092-8674(93)90368-z.
- [lopezcasillas-1994-dual-modulator] López-Casillas F, Payne HM, Andres JL, Massagué J. (1994). Betaglycan can act as a dual modulator of TGF-beta access to signaling receptors: mapping of ligand binding and GAG attachment sites. *J Cell Biol* 124:557-568. PMID: 8106553; PMCID: PMC2119924; DOI: 10.1083/jcb.124.4.557.
- [pepin-1994-ligand-binding-mapping] Pepin MC, Beauchemin M, Plamondon J, O'Connor-McCourt MD. (1994). Mapping of the ligand binding domain of the transforming growth factor beta receptor type III by deletion mutagenesis. *PNAS* 91:6997-7001. PMID: 8041735; PMCID: PMC44325; DOI: 10.1073/pnas.91.15.6997.
- [lamarre-1994-plasmin-cleaves] Lamarre J, Vasudevan J, Gonias SL. (1994). Plasmin cleaves betaglycan and releases a 60 kDa transforming growth factor-beta complex from the cell surface. *Biochem J* 302:199-205. PMID: 8068006; PMCID: PMC1137210; DOI: 10.1042/bj3020199.
- [ponce-1998-murine-betaglycan-gag-sites] Ponce-Castañeda MV, Esparza-López J, Vilchis-Landeros MM, Mendoza V, López-Casillas F. (1998). Murine betaglycan primary structure, expression and glycosaminoglycan attachment sites. *Biochim Biophys Acta* 1384:189-196. PMID: 9659379; DOI: 10.1016/s0167-4838(98)00033-8.
- [brown-1999-endocardial-transformation] Brown CB, Boyer AS, Runyan RB, Barnett JV. (1999). Requirement of type III TGF-beta receptor for endocardial cell transformation in the heart. *Science* 283:2080-2082. PMID: 10092230; DOI: 10.1126/science.283.5410.2080.
- [lewis-2000-betaglycan-binds-inhibin] Lewis KA, Gray PC, Blount AL, MacConell LA, Wiater E, Bilezikjian LM, Vale W. (2000). Betaglycan binds inhibin and can mediate functional antagonism of activin signalling. *Nature* 404:411-414. PMID: 10746731; DOI: 10.1038/35006129.
- [esparza-2001-specialized-binding-regions] Esparza-Lopez J, Montiel JL, Vilchis-Landeros MM, Okadome T, Miyazono K, López-Casillas F. (2001). Ligand binding and functional properties of betaglycan, a co-receptor of the transforming growth factor-beta superfamily. Specialized binding regions for transforming growth factor-beta and inhibin A. *J Biol Chem* 276:14588-14596. PMID: 11278442; DOI: 10.1074/jbc.m008866200.
- [vilchis-2001-soluble-betaglycan-neutralizing] Vilchis-Landeros MM, Montiel JL, Mendoza V, Mendoza-Hernández G, López-Casillas F. (2001). Recombinant soluble betaglycan is a potent and isoform-selective transforming growth factor-beta neutralizing agent. *Biochem J* 355:215-222. PMID: 11256966; PMCID: PMC1221729; DOI: 10.1042/0264-6021:3550215.
- [blobe-2001-cytoplasmic-domain] Blobe GC, Schiemann WP, Pepin MC, Beauchemin M, Moustakas A, Lodish HF, O'Connor-McCourt MD. (2001). Functional roles for the cytoplasmic domain of the type III transforming growth factor beta receptor in regulating transforming growth factor beta signaling. *J Biol Chem* 276:24627-24637. PMID: 11323414; DOI: 10.1074/jbc.m100188200.
- [blobe-2001-gipc] Blobe GC, Liu X, Fang SJ, How T, Lodish HF. (2001). A novel mechanism for regulating transforming growth factor beta (TGF-beta) signaling. Functional modulation of type III TGF-beta receptor expression through interaction with the PDZ domain protein, GIPC. *J Biol Chem* 276:39608-39617. PMID: 11546783; DOI: 10.1074/jbc.m106831200.
- [chen-2003-beta-arrestin2] Chen W, Kirkbride KC, How T, Nelson CD, Mo J, Frederick JP, Wang XF, Lefkowitz RJ, Blobe GC. (2003). Beta-arrestin 2 mediates endocytosis of type III TGF-beta receptor and down-regulation of its signaling. *Science* 301:1394-1397. PMID: 12958365; DOI: 10.1126/science.1083195.
- [stenvers-2003-knockout-heart-liver] Stenvers KL, Tursky ML, Harder KW, et al. (2003). Heart and liver defects and reduced transforming growth factor beta2 sensitivity in transforming growth factor beta type III receptor-deficient embryos. *Mol Cell Biol* 23:4371-4385. PMID: 12773577; PMCID: PMC156130; DOI: 10.1128/mcb.23.12.4371-4385.2003.
- [velasco-2004-shedding-mt1mmp] Velasco-Loyden G, Arribas J, López-Casillas F. (2004). The shedding of betaglycan is regulated by pervanadate and mediated by membrane type matrix metalloprotease-1. *J Biol Chem* 279:7721-7733. PMID: 14672946; DOI: 10.1074/jbc.m306499200.
- [wiater-2006-distinct-binding-sites] Wiater E, Harrison CA, Lewis KA, Gray PC, Vale WW. (2006). Identification of distinct inhibin and transforming growth factor beta-binding sites on betaglycan: functional separation of betaglycan co-receptor actions. *J Biol Chem* 281:17011-17022. PMID: 16621788; DOI: 10.1074/jbc.m601459200.
- [compton-2007-coronary-vessel] Compton LA, Potash DA, Brown CB, Barnett JV. (2007). Coronary vessel development is dependent on the type III transforming growth factor beta receptor. *Circ Res* 101:784-791. PMID: 17704211; DOI: 10.1161/circresaha.107.152082.
- [kirkbride-2008-bmp-signal-tbr3] Kirkbride KC, Townsend TA, Bruinsma MW, Barnett JV, Blobe GC. (2008). Bone morphogenetic proteins signal through the transforming growth factor-beta type III receptor. *J Biol Chem* 283:7628-7637. PMID: 18184661; DOI: 10.1074/jbc.m704883200.
- [bernabeu-2009-coreceptors-cancer-review] Bernabeu C, Lopez-Novoa JM, Quintanilla M. (2009). The emerging role of TGF-beta superfamily coreceptors in cancer. *Biochim Biophys Acta* 1792:954-973. PMID: 19607914; DOI: 10.1016/j.bbadis.2009.07.003.
- [lee-2009-alk3-alk6-trafficking] Lee NY, Kirkbride KC, Sheu RD, Blobe GC. (2009). The transforming growth factor-beta type III receptor mediates distinct subcellular trafficking and downstream signaling of activin-like kinase (ALK)3 and ALK6 receptors. *Mol Biol Cell* 20:4362-4370. PMID: 19726563; PMCID: PMC2762132; DOI: 10.1091/mbc.e09-07-0539.
- [mythreye-2009-cdc42] Mythreye K, Blobe GC. (2009). The type III TGF-beta receptor regulates epithelial and cancer cell migration through beta-arrestin2-mediated activation of Cdc42. *PNAS* 106:8221-8226. PMID: 19416857; PMCID: PMC2688894; DOI: 10.1073/pnas.0812879106.
- [wiater-2009-endogenous-betaglycan-gonadotropes] Wiater E, Lewis KA, Donaldson C, Vaughan J, Bilezikjian L, Vale W. (2009). Endogenous betaglycan is essential for high-potency inhibin antagonism in gonadotropes. *Mol Endocrinol* 23:1033-1042. PMID: 19372236; PMCID: PMC2703594; DOI: 10.1210/me.2009-0021.
- [blair-2011-gamma-secretase] Blair CR, Stone JB, Wells RG. (2011). The type III TGF-β receptor betaglycan transmembrane-cytoplasmic domain fragment is stable after ectodomain cleavage and is a substrate of the intramembrane protease γ-secretase. *Biochim Biophys Acta* 1813:332-339. PMID: 21167215; PMCID: PMC3026071; DOI: 10.1016/j.bbamcr.2010.12.005.
- [lin-2011-zpc-structure] Lin SJ, Hu Y, Zhu J, Woodruff TK, Jardetzky TS. (2011). Structure of betaglycan zona pellucida (ZP)-C domain provides insights into ZP-mediated protein polymerization and TGF-beta binding. *PNAS* 108:5232-5236. PMID: 21402931; PMCID: PMC3069177; DOI: 10.1073/pnas.1010689108.
- [townsend-2012-gipc-endocardial-emt] Townsend TA, Robinson JY, How T, DeLaughter DM, Blobe GC, Barnett JV. (2012). Endocardial cell epithelial-mesenchymal transformation requires Type III TGFβ receptor interaction with GIPC. *Cell Signal* 24:247-256. PMID: 21945156; PMCID: PMC3208316; DOI: 10.1016/j.cellsig.2011.09.006.
- [mythreye-2013-integrin-a5b1] Mythreye K, Knelson EH, Gatza CE, Gatza ML, Blobe GC. (2013). TβRIII/β-arrestin2 regulates integrin α5β1 trafficking, function, and localization in epithelial cells. *Oncogene* 32:1416-1427. PMID: 22562249; PMCID: PMC3835656; DOI: 10.1038/onc.2012.157.
- [elderbroom-2014-shedding-required] Elderbroom JL, Huang JJ, Gatza CE, Chen J, How T, Starr M, Nixon AB, Blobe GC. (2014). Ectodomain shedding of TβRIII is required for TβRIII-mediated suppression of TGF-β signaling and breast cancer migration and invasion. *Mol Biol Cell* 25:2320-2332. PMID: 24966170; PMCID: PMC4142606; DOI: 10.1091/mbc.e13-09-0524.
- [choi-2024-gag-shedding] Choi AS, Jenkins-Lane LM, Barton W, et al. (2024). Glycosaminoglycan modifications of betaglycan regulate ectodomain shedding to fine-tune TGF-β signaling responses in ovarian cancer. *Cell Commun Signal* 22:128. PMID: 38360757; PMCID: PMC10870443; DOI: 10.1186/s12964-024-01496-y.
- [kazakh-2025-horse-ovary-scrna] Ren W, Zhou J, Zhu J, Zhang J, Zhao X, Yao X. (2025). Exploring the Abnormal Characteristics of the Ovaries During the Estrus Period of Kazakh Horses Based on Single-Cell Transcriptome Technology. *Biology* 14:1351. PMID: 41154754; PMCID: PMC12562243; DOI: 10.3390/biology14101351.
- [donkey-2026-tgfb-gene-family] Nasir T, Tariq M, Tharwat M, Safdar M, Junejo Y, Alshanbari FA. (2026). Genome-Wide Characterization of the TGF-β Gene Family in Donkey (*Equus asinus*) Reveals Lineage-Specific Gene Duplications and Deleterious Mutations. *Animals* 16:2028. PMID: 42450734; PMCID: PMC13359590; DOI: 10.3390/ani16132028.
- [hinck-2016-structural-biology-review] Hinck AP, Mueller TD, Springer TA. (2016). Structural Biology and Evolution of the TGF-β Family. *Cold Spring Harb Perspect Biol* 8:a022103. PMID: 27638177; PMCID: PMC5131774; DOI: 10.1101/cshperspect.a022103.
- [li-2018-inhibinA-coreceptor-gonadotropes] Li Y, Fortin J, Ongaro L, Zhou X, Boehm U, Schneyer A, Bernard DJ, Lin HY. (2018). Betaglycan (TGFBR3) Functions as an Inhibin A, but Not Inhibin B, Coreceptor in Pituitary Gonadotrope Cells in Mice. *Endocrinology* 159:4077-4091. PMID: 30364975; PMCID: PMC6372943; DOI: 10.1210/en.2018-00770.
- [henen-2019-tgfb2-zp-binding] Henen MA, Mahlawat P, Zwieb C, et al. (2019). TGF-β2 uses the concave surface of its extended finger region to bind betaglycan's ZP domain via three residues specific to TGF-β and inhibin-α. *J Biol Chem* 294:3065-3080. PMID: 30598510; PMCID: PMC6398128; DOI: 10.1074/jbc.ra118.005210.
- [kim-2019-orphan-domain] Kim SK, Whitley MJ, Krzysiak TC, et al. (2019). Structural Adaptation in Its Orphan Domain Engenders Betaglycan with an Alternate Mode of Growth Factor Binding Relative to Endoglin. *Structure* 27:1427-1442.e4. PMID: 31327662; PMCID: PMC6726503; DOI: 10.1016/j.str.2019.06.010.
- [brule-2021-tgfbr3l-inhibinB] Brûlé E, Wang Y, Li Y, et al. (2021). TGFBR3L is an inhibin B co-receptor that regulates female fertility. *Science Advances* 7:eabl4391. PMID: 34910520; PMCID: PMC8673766; DOI: 10.1126/sciadv.abl4391.
- [wieteska-2025-structures-complex-assembly] Wieteska Ł, Taylor AB, Punch E, et al. (2025). Structures of TGF-β with betaglycan and signaling receptors reveal mechanisms of complex assembly and signaling. *Nature Communications* 16:1778. PMID: 40011426; PMCID: PMC11865472; DOI: 10.1038/s41467-025-56796-9.
- UniProt entries used for sequence analysis: A0A8C4M6Z6 (https://rest.uniprot.org/uniprotkb/A0A8C4M6Z6.txt), Q03167 (human), F7E1V2 (horse), E1B9H5 (cattle), O88393 (mouse) and P26342 (rat), retrieved from https://rest.uniprot.org.


## Citations

1. _metadata.json
2. andres-1992-two-growth-factor-families-abstract.md
3. andres-1992-two-growth-factor-families-summary.md
4. bernabeu-2009-coreceptors-cancer-review-abstract.md
5. bernabeu-2009-coreceptors-cancer-review-summary.md
6. blair-2011-gamma-secretase-abstract.md
7. blair-2011-gamma-secretase-fulltext.txt
8. blair-2011-gamma-secretase-summary.md
9. blobe-2001-cytoplasmic-domain-abstract.md
10. blobe-2001-cytoplasmic-domain-summary.md
11. blobe-2001-gipc-abstract.md
12. blobe-2001-gipc-summary.md
13. brown-1999-endocardial-transformation-abstract.md
14. brown-1999-endocardial-transformation-summary.md
15. brule-2021-tgfbr3l-inhibinB-abstract.md
16. brule-2021-tgfbr3l-inhibinB-fulltext.txt
17. brule-2021-tgfbr3l-inhibinB-summary.md
18. chen-2003-beta-arrestin2-abstract.md
19. chen-2003-beta-arrestin2-summary.md
20. choi-2024-gag-shedding-abstract.md
21. choi-2024-gag-shedding-fulltext.txt
22. choi-2024-gag-shedding-summary.md
23. compton-2007-coronary-vessel-abstract.md
24. compton-2007-coronary-vessel-summary.md
25. donkey-2026-tgfb-gene-family-abstract.md
26. donkey-2026-tgfb-gene-family-fulltext.txt
27. donkey-2026-tgfb-gene-family-summary.md
28. elderbroom-2014-shedding-required-abstract.md
29. elderbroom-2014-shedding-required-fulltext.txt
30. elderbroom-2014-shedding-required-summary.md
31. esparza-2001-specialized-binding-regions-abstract.md
32. esparza-2001-specialized-binding-regions-summary.md
33. henen-2019-tgfb2-zp-binding-abstract.md
34. henen-2019-tgfb2-zp-binding-summary.md
35. hinck-2016-structural-biology-review-abstract.md
36. hinck-2016-structural-biology-review-summary.md
37. kazakh-2025-horse-ovary-scrna-abstract.md
38. kazakh-2025-horse-ovary-scrna-fulltext.txt
39. kazakh-2025-horse-ovary-scrna-summary.md
40. kim-2019-orphan-domain-abstract.md
41. kim-2019-orphan-domain-fulltext.txt
42. kim-2019-orphan-domain-summary.md
43. kirkbride-2008-bmp-signal-tbr3-abstract.md
44. kirkbride-2008-bmp-signal-tbr3-summary.md
45. lamarre-1994-plasmin-cleaves-abstract.md
46. lamarre-1994-plasmin-cleaves-summary.md
47. lee-2009-alk3-alk6-trafficking-abstract.md
48. lee-2009-alk3-alk6-trafficking-summary.md
49. lewis-2000-betaglycan-binds-inhibin-abstract.md
50. lewis-2000-betaglycan-binds-inhibin-summary.md
51. li-2018-inhibinA-coreceptor-gonadotropes-abstract.md
52. li-2018-inhibinA-coreceptor-gonadotropes-summary.md
53. lin-2011-zpc-structure-abstract.md
54. lin-2011-zpc-structure-summary.md
55. lopezcasillas-1991-betaglycan-structure-abstract.md
56. lopezcasillas-1991-betaglycan-structure-summary.md
57. lopezcasillas-1993-presents-ligand-abstract.md
58. lopezcasillas-1993-presents-ligand-summary.md
59. lopezcasillas-1994-dual-modulator-abstract.md
60. lopezcasillas-1994-dual-modulator-summary.md
61. mythreye-2009-cdc42-abstract.md
62. mythreye-2009-cdc42-summary.md
63. mythreye-2013-integrin-a5b1-abstract.md
64. mythreye-2013-integrin-a5b1-fulltext.txt
65. mythreye-2013-integrin-a5b1-summary.md
66. pepin-1994-ligand-binding-mapping-abstract.md
67. pepin-1994-ligand-binding-mapping-summary.md
68. ponce-1998-murine-betaglycan-gag-sites-abstract.md
69. ponce-1998-murine-betaglycan-gag-sites-summary.md
70. stenvers-2003-knockout-heart-liver-abstract.md
71. stenvers-2003-knockout-heart-liver-summary.md
72. townsend-2012-gipc-endocardial-emt-abstract.md
73. townsend-2012-gipc-endocardial-emt-fulltext.txt
74. townsend-2012-gipc-endocardial-emt-summary.md
75. velasco-2004-shedding-mt1mmp-abstract.md
76. velasco-2004-shedding-mt1mmp-summary.md
77. vilchis-2001-soluble-betaglycan-neutralizing-abstract.md
78. vilchis-2001-soluble-betaglycan-neutralizing-summary.md
79. wang-1991-type3-expression-cloning-abstract.md
80. wang-1991-type3-expression-cloning-summary.md
81. wang-2020-donkey-genome-abstract.md
82. wang-2020-donkey-genome-fulltext.txt
83. wang-2020-donkey-genome-summary.md
84. wiater-2006-distinct-binding-sites-abstract.md
85. wiater-2006-distinct-binding-sites-summary.md
86. wiater-2009-endogenous-betaglycan-gonadotropes-abstract.md
87. wiater-2009-endogenous-betaglycan-gonadotropes-summary.md
88. wieteska-2025-structures-complex-assembly-abstract.md
89. wieteska-2025-structures-complex-assembly-fulltext.txt
90. wieteska-2025-structures-complex-assembly-summary.md