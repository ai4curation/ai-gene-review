---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:46:23.164264'
end_time: '2026-10-26T04:00:06.997447'
duration_seconds: 823.83
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: TRAF2
  gene_symbol: TRAF2
  uniprot_accession: F7BIV4
  protein_description: 'RecName: Full=TNF receptor-associated factor {ECO:0000256|PIRNR:PIRNR015614};
    EC=2.3.2.27 {ECO:0000256|PIRNR:PIRNR015614};'
  gene_info: Name=TRAF2 {ECO:0000313|VGNC:VGNC:24455};
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the TNF receptor-associated factor family. A
  protein_domains: MATH/TRAF_dom. (IPR002083); TNF_rcpt-assoc_TRAF_met. (IPR012227);
    TRAF-like. (IPR008974); TRAF1-6_MATH_dom. (IPR049342); TRAF2_MATH. (IPR037305)
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
citation_count: 81
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** F7BIV4
- **Protein Description:** RecName: Full=TNF receptor-associated factor {ECO:0000256|PIRNR:PIRNR015614}; EC=2.3.2.27 {ECO:0000256|PIRNR:PIRNR015614};
- **Gene Information:** Name=TRAF2 {ECO:0000313|VGNC:VGNC:24455};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the TNF receptor-associated factor family. A
- **Key Domains:** MATH/TRAF_dom. (IPR002083); TNF_rcpt-assoc_TRAF_met. (IPR012227); TRAF-like. (IPR008974); TRAF1-6_MATH_dom. (IPR049342); TRAF2_MATH. (IPR037305)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TRAF2" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TRAF2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TRAF2** (gene ID: TRAF2, UniProt: F7BIV4) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TRAF2 (TNF receptor-associated factor 2) in the horse, *Equus caballus* (UniProt F7BIV4)

## 1. Introduction and summary

UniProt F7BIV4 is the horse (*Equus caballus*) gene product of *TRAF2* (VGNC:24455). It is an unreviewed (TrEMBL) entry of 516 residues on horse chromosome 25, predicted from the Thoroughbred reference genome. Its name, EC number (2.3.2.27, RING-type E3 ubiquitin transferase), cytoplasmic location and GO terms are all assigned automatically from homology rules [uniprot-2026-F7BIV4-entry][wade-2009-horse-genome-abstract]. I first checked whether the symbol could refer to a different gene. It does not: the domain architecture is an N-terminal C3HC4 RING finger, two TRAF-type zinc fingers, a coiled coil and a C-terminal MATH/TRAF-C domain, with the TRAF2-specific InterPro signatures IPR037305 (TRAF2_MATH), IPR027133 (TRAF2_RING-HC) and IPR032070 (TRAF_BIRC3-bd). This is the canonical TRAF2 architecture [uniprot-2026-F7BIV4-entry]. I aligned F7BIV4 with human TRAF2 (Q12933, 501 residues). They share 92.0% identity over 501 aligned positions, and the only notable difference is a 15-residue insertion in the horse linker just before the coiled coil (see Section 7) [horse-human-alignment]. No experimental biochemistry has been published on horse TRAF2 itself. The only horse literature consists of two immunodetection studies in equine tendon cells [hosaka-2004-equine-tendinocyte-traf-abstract][hosaka-2005-equine-tendinocyte-tnf-abstract]. The functional account below is therefore inferred from extensive work on human and mouse TRAF2, which is justified by the very high sequence conservation. That conservation includes every functionally mapped residue I checked.

In brief, TRAF2 is a cytoplasmic signalling adaptor. It was discovered as a protein that binds directly to the cytoplasmic tail of TNF receptor 2 (TNFR2), and it is recruited to TNFR1 through TRADD [rothe-1994-traf-family-abstract][hsu-1996-tradd-traf2-abstract]. Its trimeric TRAF domain reads short receptor motifs such as SXXE and couples trimerized, ligand-bound receptors to downstream effectors [park-1999-traf2-structure-abstract]. Its most firmly established molecular role is as the obligate docking platform that brings the RING E3 ligases cIAP1 and cIAP2 to receptor complexes, where they ubiquitinate RIPK1 and other substrates [rothe-1995-ciap-tnfr2-abstract][zheng-2010-traf2-ciap2-structure-fulltext][bertrand-2008-ciap-rip1-abstract][varfolomeev-2012-ciap-global-abstract]. Through this TRAF2–cIAP module, TRAF2 does three things. It promotes canonical NF-κB and JNK/p38 MAP kinase signalling downstream of TNF-family receptors. In resting cells, it represses non-canonical NF-κB by targeting the kinase NIK for degradation together with TRAF3 [vallabhapurapu-2008-traf2-traf3-nik-fulltext][zarnegar-2008-noncanonical-nfkb-fulltext]. It also limits TNF-induced apoptosis and necroptosis [yeh-1997-traf2-knockout-abstract][tada-2001-traf2-traf5-abstract][etemadi-2015-traf2-s1p-independent-fulltext]. Whether TRAF2 is itself a catalytic E3 ligase remains contested. The RING of TRAF2 is structurally unable to bind Ubc13-family E2s [yin-2009-traf2-ring-fulltext]. Against this, there are reports of RING-dependent K63 ubiquitination stimulated by sphingosine-1-phosphate (S1P) [alvarez-2010-s1p-traf2-fulltext], and of K48 ubiquitination of caspase-8 [gonzalvez-2012-traf2-caspase8-abstract]. Genetic evidence argues that TRAF2 works independently of the S1P-producing enzyme SphK1 [etemadi-2015-traf2-s1p-independent-fulltext].

## 2. Identity, domain architecture and conservation of the horse protein

The automated annotation of F7BIV4 places a RING-type zinc finger at residues 34–72, TRAF-type zinc fingers at 125–170 and 177–233, a coiled coil at 280–342 and a MATH domain at 366–511 [uniprot-2026-F7BIV4-entry]. These boundaries match the modular design described when TRAF2 was cloned. Rothe and colleagues defined a C-terminal "TRAF domain" shared by TRAF1 and TRAF2, and noted that TRAF2 also has an N-terminal RING finger [rothe-1994-traf-family-abstract]. The horse and human sequences are identical over most of the RING, zinc-finger, coiled-coil and TRAF-C regions, with only scattered conservative substitutions [horse-human-alignment]. Several residues known to carry regulatory modifications in human TRAF2 are conserved in horse at the same positions. These include Thr117, which PKC phosphorylates to recruit IKK, and Lys31, the site of TNF-induced K63-linked ubiquitination [li-2009-pkc-traf2-fulltext][horse-human-alignment]. The TRAF2 segment that contacts cIAP2 (human residues 281–295, including the hydrophobic residues Ile285 and Val288) is invariant in horse, where it corresponds to residues 296–310 (Ile300, Val303) [zheng-2010-traf2-ciap2-structure-fulltext][horse-human-alignment]. The horse-specific insertion lies N-terminal to this interface, in the linker between the second zinc finger and the coiled coil. The RING of F7BIV4 is the same length as the canonical human RING. In mouse, an alternatively spliced variant called TRAF2A carries a 7-residue insert inside the RING, cannot activate NF-κB and acts as a dominant inhibitor of TNFR2 signalling [brink-1998-traf2a-splice-abstract]. The horse protein has no such insert, so it corresponds to the canonical, signalling-competent form and not to TRAF2A [horse-human-alignment]. Taken together, these observations support treating F7BIV4 as a full-length, functional TRAF2 ortholog.

## 3. Structural basis of receptor recognition and oligomerization

The C-terminal TRAF domain is the receptor-binding and self-association module. Park et al. solved crystal structures of the human TRAF2 TRAF domain alone and bound to a TNFR2 peptide. The domain forms a trimer: the coiled-coil stalks pack together and the C-terminal TRAF-C (MATH) domains form an eight-stranded antiparallel β-sandwich "cap". The receptor peptide binds a conserved shallow surface depression on a single TRAF-C protomer, which defined an SXXE consensus for TRAF2 binding [park-1999-traf2-structure-abstract]. Each receptor contact is weak, but the trimer offers three binding sites, so binding is avidity-driven. This explains why TRAF2 recruitment depends on receptor clustering by trimeric TNF-family ligands [park-1999-traf2-structure-abstract]. Ye et al. later solved further co-crystal structures of the TRAF2 TRAF domain with peptides from CD40, CD30, OX40, 4-1BB and the Epstein–Barr virus oncoprotein LMP1. All of these peptides bind in the same way. Together the structures define a major consensus motif, (P/S/A/T)x(Q/E)E, and a minor one, PxQxxD, which between them account for all known TRAF2-binding sequences. This explains how a single adaptor can serve many different TNFR-superfamily receptors [ye-1999-traf2-receptor-recognition-abstract]. TRAF2 can also form heterotypic complexes. TRAF1 reaches TNFR2 only indirectly, by heteromerizing with TRAF2 [rothe-1994-traf-family-abstract], and TRAF1 and TRAF2 preferentially assemble a TRAF1:(TRAF2)2 heterotrimer [zheng-2010-traf2-ciap2-structure-fulltext]. Because the TRAF-C domain of the horse protein is almost identical to the human one, the same mode of receptor engagement can be expected in horse.

## 4. The RING domain and the question of intrinsic E3 ligase activity

The UniProt assignment of EC 2.3.2.27 to F7BIV4 rests on family-level rules [uniprot-2026-F7BIV4-entry]. The direct biochemical evidence for TRAF2 catalysis is conflicting. Early work showed that the RING is essential for signalling: TRAF2 lacking its N-terminal RING acts as a dominant-negative inhibitor of NF-κB activation by TNFR2, CD40 and TNFR1 [rothe-1995-traf2-nfkb-abstract][hsu-1996-tradd-traf2-abstract]. However, the crystal structure of the TRAF2 RING and first zinc finger revealed three differences from the catalytically active TRAF6 RING. Residues at the Ubc13-binding site differ, there are local conformational changes, and a unique nine-residue insertion follows the last zinc-coordinating cysteine. Together these sterically and energetically prevent TRAF2 from binding Ubc13 and related E2s, and TRAF2 failed to bind Ubc13 in yeast two-hybrid assays [yin-2009-traf2-ring-fulltext]. The authors concluded that TRAF2-associated cIAPs might be the actual E3 ligases in NF-κB signalling [yin-2009-traf2-ring-fulltext].

An alternative model holds that TRAF2 is an E3 ligase that needs a lipid cofactor. Alvarez et al. reported that S1P, produced by sphingosine kinase 1 (SphK1, a TRAF2 binding partner), binds the TRAF2 RING. In their in vitro assays, S1P but not dihydro-S1P strongly increased recombinant TRAF2-catalysed K63-linked (but not K48-linked) polyubiquitination of RIP1 with UbcH13 or UbcH5a, and a ΔRING TRAF2 was inactive [alvarez-2010-s1p-traf2-fulltext]. They docked S1P into a hydrophobic and basic pocket in the RING. In horse, most of the residues they named are conserved (Arg43, Phe45, Leu58, Leu62, Ala90, Phe91, Arg97), but Ala59 is replaced by threonine [alvarez-2010-s1p-traf2-fulltext][horse-human-alignment]. One caveat is that the reported "F92" does not match the human UniProt sequence, which has proline at position 92, so the published numbering may be offset. A genetic test argues against this model in vivo. Keratinocyte-specific deletion of *Traf2* disrupted TNF-induced NF-κB and MAPK signalling and caused psoriasis-like skin inflammation, whereas loss of *Sphk1* did not. The authors concluded that TRAF2 functions independently of SphK1 [etemadi-2015-traf2-s1p-independent-fulltext].

TRAF2 has also been reported to ubiquitinate caspase-8. At the death-inducing signalling complex (DISC) of DR4, DR5 and Fas, TRAF2 binds caspase-8 and directs RING-dependent K48-linked polyubiquitination of its large catalytic domain. This marks activated caspase-8 for proteasomal degradation and so sets a threshold for extrinsic apoptosis [gonzalvez-2012-traf2-caspase8-abstract]. TRAF2 can also K63-ubiquitinate cIAP1/2 after CD40 or BAFF-R engagement [vallabhapurapu-2008-traf2-traf3-nik-fulltext]. The safest summary is that TRAF2 is a RING protein with at most a context-dependent and possibly cofactor-dependent ligase activity, and that its dominant, well-supported function is as a scaffold for other E3s.

## 5. TRAF2 as the scaffold that recruits cIAP1/cIAP2 E3 ligases

The partnership of TRAF2 with the cellular inhibitor of apoptosis proteins was found biochemically. Purifying the TNFR2 signalling complex yielded c-IAP1 and c-IAP2, which bind TRAF1/TRAF2 through their N-terminal BIR domains rather than contacting the receptor [rothe-1995-ciap-tnfr2-abstract]. Structures of the TRAF2 coiled coil (residues 266–329) with the cIAP2 BIR1 domain show one cIAP2 per TRAF2 trimer, contacted mainly by two TRAF2 chains through residues 281–295 [zheng-2010-traf2-ciap2-structure-fulltext]. Mace et al. found the same 1:3 stoichiometry for cIAP1. They proposed that dimeric cIAPs cross-link TRAF2 trimers, which may help build larger signalling assemblies [mace-2010-asymmetric-ciap-abstract]. Vince et al. mapped a cIAP1/2-interacting motif (CIM) in the TRAF-N region of TRAF2 and used mutants to separate TRAF2's functions [vince-2009-traf2-ciap-binding-abstract]. A CIM-mutant TRAF2 supported less TNFR1-induced canonical NF-κB activation and RIPK1 ubiquitylation, whereas TRAF2 lacking the RING did not lose these functions. The RING and the CIM were both needed to keep NIK unstable, suppressing constitutive non-canonical NF-κB, and both were needed to protect cells from TNF-induced apoptosis [vince-2009-traf2-ciap-binding-abstract]. This genetic separation of functions fits the structural argument that TRAF2's main contribution to canonical NF-κB is to recruit cIAPs, not to catalyse ubiquitination itself [yin-2009-traf2-ring-fulltext][zheng-2010-traf2-ciap2-structure-fulltext]. Once recruited, cIAP1 and cIAP2 act as E3 ligases that directly ubiquitinate RIPK1 [bertrand-2008-ciap-rip1-abstract]. Through their constitutive association with TRAF2, they are required to recruit IKKβ, NEMO and the LUBAC component HOIP to TNFR signalling complexes, and so for canonical NF-κB and MAPK activation by many TNF-family receptors [varfolomeev-2012-ciap-global-abstract]. TRAF2 itself is regulated within this complex. TNF triggers PKC-dependent phosphorylation of TRAF2 at Thr117, which promotes IKKα/β recruitment and K63-linked ubiquitination of TRAF2 at Lys31. That ubiquitination in turn favours binding of TAB2/TAB3 and activation of IKK and JNK [li-2009-pkc-traf2-fulltext]. Both sites are conserved in horse [horse-human-alignment].

## 6. Pathways: canonical NF-κB, MAP kinases, non-canonical NF-κB and cell death

TRAF2 enters TNFR1 signalling through TRADD, which binds TRAF2 and FADD and thereby splits the pathway into a survival/NF-κB branch and an apoptotic branch [hsu-1996-tradd-traf2-abstract]. TRAF2 is also a common mediator of NF-κB activation by TNFR2 and CD40 [rothe-1995-traf2-nfkb-abstract]. Loss-of-function genetics shows that its role in canonical NF-κB is partly redundant. *Traf2*-null mice are runted, die prematurely, and have thymic and splenic atrophy and elevated serum TNF. Their cells show a severe loss of TNF-induced JNK activation but only a mild NF-κB defect, and they are highly sensitive to TNF-induced death [yeh-1997-traf2-knockout-abstract]. A lymphocyte-restricted dominant-negative TRAF2 similarly blocked JNK but not NF-κB activation and caused lymphoid hyperplasia [lee-1997-traf2-jnk-abstract]. Deleting *Traf2* and *Traf5* together severely impaired TNF-induced (but not IL-1-induced) NF-κB nuclear translocation, which shows that TRAF5 compensates for TRAF2 in this branch [tada-2001-traf2-traf5-abstract].

In the MAP kinase branch, TNF induces rapid association of endogenous TRAF2 with the MAP3K ASK1, and kinase-dead ASK1 blocks TRAF2-driven JNK activation [nishitoh-1998-ask1-traf2-abstract]. TRAF2 also couples endoplasmic-reticulum stress to JNK. The cytoplasmic region of the ER-resident kinase IRE1 binds TRAF2, and dominant-negative TRAF2 suppresses IRE1-induced JNK activation [urano-2000-ire1-traf2-abstract]. This is the basis of the "IRE1–TRAF2–ASK1 complex" GO term on the horse entry [uniprot-2026-F7BIV4-entry].

TRAF2 has an opposite, inhibitory role in non-canonical NF-κB signalling. In resting cells, TRAF3 binds the kinase NIK while TRAF2 recruits cIAP1/2. This assembles an E3 complex that ubiquitinates NIK and sends it for proteasomal degradation, preventing processing of p100 to p52 [zarnegar-2008-noncanonical-nfkb-fulltext]. When CD40 or BAFF-R are engaged, TRAF2 K63-ubiquitinates the cIAPs, which redirects them to degrade TRAF3. NIK then accumulates and drives p100 processing. TRAF2 and TRAF3 are non-redundant in this cascade [vallabhapurapu-2008-traf2-traf3-nik-fulltext]. Receptors that activate this pathway move cIAPs, TRAF2 and TRAF3 from the cytosol to membranes, where they are degraded [varfolomeev-2012-ciap-global-abstract]. In vivo, keratinocyte-specific TRAF2 loss causes skin inflammation that depends on TNF, cell death, non-canonical NF-κB and adaptive immunity [etemadi-2015-traf2-s1p-independent-fulltext]. TRAF2 also suppresses necroptosis. When TRAF2 was disrupted in mouse fibroblasts, TNFα produced more necrosome assembly and more RIPK3–MLKL association, and so more necroptotic death [petersen-2015-traf2-necroptosis-abstract]. TRAF2 bound the necroptosis executioner MLKL constitutively, through its C-terminal region and independently of its RING and CIM. TNFα released this binding through CYLD-dependent deubiquitination of TRAF2 [petersen-2015-traf2-necroptosis-abstract]. Inducible deletion of TRAF2 in adult mice caused rapid death with increased necrosome assembly in the liver. Co-deleting RIPK3 delayed death, and the delayed deaths were accompanied by elevated intestinal caspase-8 activity [petersen-2015-traf2-necroptosis-abstract][lalani-2018-traf-inflammation-review-fulltext]. TRAF2 therefore restrains all three outcomes of death-receptor signalling: caspase-8-driven apoptosis, RIPK3–MLKL-driven necroptosis, and inappropriate activation of non-canonical NF-κB. A broad review of these receptor-specific positive and negative functions is given by Borghi et al. [borghi-2016-traf2-review-abstract].

## 7. Beyond TNF receptors: ubiquitin-dependent control of mTOR complexes

The horse UniProt entry carries GO annotations for "TORC1 complex assembly" and "TORC2 complex disassembly" [uniprot-2026-F7BIV4-entry]. These come from more recent work in human and mouse cells. Wang et al. showed that TRAF2 promotes K63-linked polyubiquitination of GβL (mLST8), a subunit shared by both mTOR complexes. This ubiquitination blocks GβL from binding SIN1, which is specific to mTORC2, and so shifts assembly toward mTORC1. The deubiquitinase OTUD7B removes these chains and promotes mTORC2 assembly and AKT activation in response to growth factors [wang-2017-traf2-mtorc2-fulltext]. In liver cancer cells, TRAF2 was reported to K63-ubiquitinate the autophagy adaptor p62/SQSTM1 at Lys420. This promoted formation of a p62–mTORC1–Rag complex and moved mTORC1 to the lysosome, and TRAF2 depletion lowered mTORC1 activity and slowed tumour cell growth [liang-2023-traf2-p62-mtorc1-fulltext]. Both studies assume that TRAF2 acts as the E3 ligase, which conflicts with the structural evidence against an intrinsic Ubc13-dependent activity described in Section 4 [yin-2009-traf2-ring-fulltext]. It has not been settled whether these modifications are made by TRAF2 directly or by associated ligases. These findings suggest that TRAF2 links inflammatory signalling to growth control, but the evidence comes from cultured and cancer cells and has not been tested in horse.

## 8. Subcellular localization and the horse-specific evidence

TRAF2 is a soluble cytoplasmic protein with no transmembrane segment or signal peptide, and the horse entry is annotated to the cytoplasm and cytosol [uniprot-2026-F7BIV4-entry]. It acts at the cytoplasmic face of membranes when signalling. TRAF2 is recruited to the cytoplasmic tails of ligand-activated TNFR superfamily receptors at the plasma membrane [rothe-1994-traf-family-abstract][park-1999-traf2-structure-abstract]. Activation of non-canonical-NF-κB receptors moves TRAF2, cIAPs and TRAF3 from the cytosol into membrane fractions [varfolomeev-2012-ciap-global-abstract]. TRAF2 is also found in the death receptor DISC [gonzalvez-2012-traf2-caspase8-abstract] and in complex with IRE1 at the ER membrane [urano-2000-ire1-traf2-abstract]. In horse, immunohistochemistry and Western blotting detected TRAF2 in cultured superficial digital flexor tendon (SDFT) tendinocytes from Thoroughbreds. Signal was stronger after equine TNFα treatment, in parallel with NF-κB [hosaka-2004-equine-tendinocyte-traf-abstract]. In tissue, TRAF2 was abundant in normal tendinocytes and increased in inflamed SDFT together with TNF-R1 and caspase-3, but was low in scar tissue. The authors proposed that TNF-R1 drives both survival and apoptotic signalling in equine tendon [hosaka-2005-equine-tendinocyte-tnf-abstract]. These studies are correlative and depend on antibody cross-reactivity, but they show that TRAF2 is expressed in horse cells and regulated by TNF. The Bgee expression summary on the UniProt entry adds broad expression, including in leukocytes [uniprot-2026-F7BIV4-entry]. The 15-residue horse insertion (about residues 260–276) lies in the linker immediately N-terminal to the cIAP-binding coiled coil [horse-human-alignment]. Its functional consequence is unknown. All three horse RefSeq protein models (XP_023485172.1, XP_023485173.1 and XP_070106529.1) are named "isoform X1" and are identical to the 516-residue F7BIV4 sequence [refseq-horse-traf2-isoforms][uniprot-2026-F7BIV4-entry]. The insertion is therefore present in every current gene model, although none of them has been confirmed experimentally. It could be a genuine species-specific exon extension or a shared annotation artefact.

## 9. Open Questions

The most basic open question is whether the 516-residue model, with its 15-residue linker insertion, is the predominant horse isoform. Its relationship to the alternatively spliced TRAF2 forms of other mammals is also unclear. This could be resolved by checking horse RNA-seq or Iso-Seq junctions and comparing the three RefSeq transcripts. A related structural question is whether the insertion changes the geometry or flexibility of the coiled coil, and so the stoichiometry or affinity of cIAP1/2 binding, given that the TRAF2–cIAP2 contact residues themselves are invariant. AlphaFold models and binding assays with recombinant horse TRAF2 could test this.

The second question concerns catalysis. It remains unresolved whether TRAF2 has intrinsic E3 activity in vivo, given the Ubc13-incompatible RING structure, the contested S1P-cofactor model and the K48 caspase-8 ubiquitination data. For horse, it would be informative to test whether the Ala59→Thr substitution near the proposed S1P pocket matters. RING-domain point mutants that separate scaffolding from catalysis, studied in knock-in models, remain the key experiment for the family as a whole.

A third question is how far TRAF2's mTOR-regulating activities, described so far only in cell lines, matter in normal tissues. A related unknown is whether TRAF2's binding to MLKL, which needs the C-terminal region but not the RING, can be mapped onto the conserved TRAF-C surface of the horse protein.

Fourth, essentially no functional work exists on TRAF2 in equine cells. Equine tendinopathy, laminitis, equine asthma and sepsis all involve TNF-driven inflammation. Loss-of-function studies (for example CRISPR in equine fibroblasts or tendinocytes) and IAP-antagonist (SMAC mimetic) experiments could test whether the TRAF2–cIAP–NIK axis and its protection against necroptosis work in horse as they do in mice. They would also show whether TRAF2 levels in tendon lesions are mechanistically linked to tendinocyte survival or apoptosis.

## References

- [uniprot-2026-F7BIV4-entry] UniProt Consortium. UniProtKB entry F7BIV4_HORSE (TRAF2, *Equus caballus*), entry version 96, 02-SEP-2026. https://rest.uniprot.org/uniprotkb/F7BIV4.txt (local copy: citations/uniprot-2026-F7BIV4-entry.txt).
- [horse-human-alignment] Pairwise global alignment (Biopython PairwiseAligner, BLOSUM62, gap open −10/extend −0.5) of UniProt F7BIV4 versus human TRAF2 Q12933 (https://rest.uniprot.org/uniprotkb/Q12933.fasta), performed for this report; output in citations/horse-human-alignment.txt.
- [wade-2009-horse-genome] Wade CM, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. Science. 2009;326(5954):865-867. PMID: 19892987; PMCID: PMC3785132; DOI: 10.1126/science.1178158.
- [hosaka-2004-equine-tendinocyte-traf] Hosaka Y, Sakamoto Y, Kirisawa R, Watanabe T, Ueda H, Takehana K, Yamaguchi M. Distribution of TNF receptors and TNF receptor-associated intracellular signaling factors on equine tendinocytes in vitro. Jpn J Vet Res. 2004;52(3):135-144. PMID: 15631011.
- [hosaka-2005-equine-tendinocyte-tnf] Hosaka Y, Kirisawa R, Ueda H, Yamaguchi M, Takehana K. Differences in tumor necrosis factor (TNF)alpha and TNF receptor-1-mediated intracellular signaling factors in normal, inflamed and scar-formed horse tendons. J Vet Med Sci. 2005;67(10):985-991. PMID: 16276053; DOI: 10.1292/jvms.67.985.
- [rothe-1994-traf-family] Rothe M, Wong SC, Henzel WJ, Goeddel DV. A novel family of putative signal transducers associated with the cytoplasmic domain of the 75 kDa tumor necrosis factor receptor. Cell. 1994;78(4):681-692. PMID: 8069916; DOI: 10.1016/0092-8674(94)90532-0.
- [rothe-1995-traf2-nfkb] Rothe M, Sarma V, Dixit VM, Goeddel DV. TRAF2-mediated activation of NF-kappa B by TNF receptor 2 and CD40. Science. 1995;269(5229):1424-1427. PMID: 7544915; DOI: 10.1126/science.7544915.
- [rothe-1995-ciap-tnfr2] Rothe M, Pan MG, Henzel WJ, Ayres TM, Goeddel DV. The TNFR2-TRAF signaling complex contains two novel proteins related to baculoviral inhibitor of apoptosis proteins. Cell. 1995;83(7):1243-1252. PMID: 8548810; DOI: 10.1016/0092-8674(95)90149-3.
- [hsu-1996-tradd-traf2] Hsu H, Shu HB, Pan MG, Goeddel DV. TRADD-TRAF2 and TRADD-FADD interactions define two distinct TNF receptor 1 signal transduction pathways. Cell. 1996;84(2):299-308. PMID: 8565075; DOI: 10.1016/s0092-8674(00)80984-8.
- [yeh-1997-traf2-knockout] Yeh WC, et al. Early lethality, functional NF-kappaB activation, and increased sensitivity to TNF-induced cell death in TRAF2-deficient mice. Immunity. 1997;7(5):715-725. PMID: 9390694; DOI: 10.1016/s1074-7613(00)80391-x.
- [lee-1997-traf2-jnk] Lee SY, Reichlin A, Santana A, Sokol KA, Nussenzweig MC, Choi Y. TRAF2 is essential for JNK but not NF-kappaB activation and regulates lymphocyte proliferation and survival. Immunity. 1997;7(5):703-713. PMID: 9390693; DOI: 10.1016/s1074-7613(00)80390-8.
- [nishitoh-1998-ask1-traf2] Nishitoh H, et al. ASK1 is essential for JNK/SAPK activation by TRAF2. Mol Cell. 1998;2(3):389-395. PMID: 9774977; DOI: 10.1016/s1097-2765(00)80283-x.
- [park-1999-traf2-structure] Park YC, Burkitt V, Villa AR, Tong L, Wu H. Structural basis for self-association and receptor recognition of human TRAF2. Nature. 1999;398(6727):533-538. PMID: 10206649; DOI: 10.1038/19110.
- [urano-2000-ire1-traf2] Urano F, Wang X, Bertolotti A, Zhang Y, Chung P, Harding HP, Ron D. Coupling of stress in the ER to activation of JNK protein kinases by transmembrane protein kinase IRE1. Science. 2000;287(5453):664-666. PMID: 10650002; DOI: 10.1126/science.287.5453.664.
- [tada-2001-traf2-traf5] Tada K, et al. Critical roles of TRAF2 and TRAF5 in tumor necrosis factor-induced NF-kappa B activation and protection from cell death. J Biol Chem. 2001;276(39):36530-36534. PMID: 11479302; DOI: 10.1074/jbc.M104837200.
- [bertrand-2008-ciap-rip1] Bertrand MJ, et al. cIAP1 and cIAP2 facilitate cancer cell survival by functioning as E3 ligases that promote RIP1 ubiquitination. Mol Cell. 2008;30(6):689-700. PMID: 18570872; DOI: 10.1016/j.molcel.2008.05.014.
- [vallabhapurapu-2008-traf2-traf3-nik] Vallabhapurapu S, et al. Nonredundant and complementary functions of TRAF2 and TRAF3 in a ubiquitination cascade that activates NIK-dependent alternative NF-kappaB signaling. Nat Immunol. 2008;9(12):1364-1370. PMID: 18997792; PMCID: PMC2671996; DOI: 10.1038/ni.1678.
- [zarnegar-2008-noncanonical-nfkb] Zarnegar BJ, et al. Noncanonical NF-kappaB activation requires coordinated assembly of a regulatory complex of the adaptors cIAP1, cIAP2, TRAF2 and TRAF3 and the kinase NIK. Nat Immunol. 2008;9(12):1371-1378. PMID: 18997794; PMCID: PMC2676931; DOI: 10.1038/ni.1676.
- [li-2009-pkc-traf2] Li S, Wang L, Dorf ME. PKC phosphorylation of TRAF2 mediates IKKalpha/beta recruitment and K63-linked polyubiquitination. Mol Cell. 2009;33(1):30-42. PMID: 19150425; PMCID: PMC2643372; DOI: 10.1016/j.molcel.2008.11.023.
- [yin-2009-traf2-ring] Yin Q, Lamothe B, Darnay BG, Wu H. Structural basis for the lack of E2 interaction in the RING domain of TRAF2. Biochemistry. 2009;48(44):10558-10567. PMID: 19810754; PMCID: PMC2830148; DOI: 10.1021/bi901462e.
- [alvarez-2010-s1p-traf2] Alvarez SE, et al. Sphingosine-1-phosphate is a missing cofactor for the E3 ubiquitin ligase TRAF2. Nature. 2010;465(7301):1084-1088. PMID: 20577214; PMCID: PMC2946785; DOI: 10.1038/nature09128.
- [zheng-2010-traf2-ciap2-structure] Zheng C, Kabaleeswaran V, Wang Y, Cheng G, Wu H. Crystal structures of the TRAF2: cIAP2 and the TRAF1: TRAF2: cIAP2 complexes: affinity, specificity, and regulation. Mol Cell. 2010;38(1):101-113. PMID: 20385093; PMCID: PMC2855162; DOI: 10.1016/j.molcel.2010.03.009.
- [mace-2010-asymmetric-ciap] Mace PD, Smits C, Vaux DL, Silke J, Day CL. Asymmetric recruitment of cIAPs by TRAF2. J Mol Biol. 2010;400(1):8-15. PMID: 20447407; DOI: 10.1016/j.jmb.2010.04.055.
- [varfolomeev-2012-ciap-global] Varfolomeev E, et al. Cellular inhibitors of apoptosis are global regulators of NF-κB and MAPK activation by members of the TNF family of receptors. Sci Signal. 2012;5(216):ra22. PMID: 22434933; DOI: 10.1126/scisignal.2001878.
- [gonzalvez-2012-traf2-caspase8] Gonzalvez F, et al. TRAF2 sets a threshold for extrinsic apoptosis by tagging caspase-8 with a ubiquitin shutoff timer. Mol Cell. 2012;48(6):888-899. PMID: 23142077; DOI: 10.1016/j.molcel.2012.09.031.
- [etemadi-2015-traf2-s1p-independent] Etemadi N, et al. TRAF2 regulates TNF and NF-κB signalling to suppress apoptosis and skin inflammation independently of Sphingosine kinase 1. eLife. 2015;4:e10592. PMID: 26701909; PMCID: PMC4769158; DOI: 10.7554/eLife.10592. (Correction: eLife 2017;6:e29849, PMID: 28654421.)
- [borghi-2016-traf2-review] Borghi A, Verstrepen L, Beyaert R. TRAF2 multitasking in TNF receptor-induced signaling to NF-κB, MAP kinases and cell death. Biochem Pharmacol. 2016;116:1-10. PMID: 26993379; DOI: 10.1016/j.bcp.2016.03.009.
- [brink-1998-traf2a-splice] Brink R, Lodish HF. Tumor necrosis factor receptor (TNFR)-associated factor 2A (TRAF2A), a TRAF2 splice variant with an extended RING finger domain that inhibits TNFR2-mediated NF-kappaB activation. J Biol Chem. 1998;273(7):4129-4134. PMID: 9461607; DOI: 10.1074/jbc.273.7.4129.
- [ye-1999-traf2-receptor-recognition] Ye H, Park YC, Kreishman M, Kieff E, Wu H. The structural basis for the recognition of diverse receptor sequences by TRAF2. Mol Cell. 1999;4(3):321-330. PMID: 10518213; DOI: 10.1016/s1097-2765(00)80334-2.
- [vince-2009-traf2-ciap-binding] Vince JE, et al. TRAF2 must bind to cellular inhibitors of apoptosis for tumor necrosis factor (TNF) to efficiently activate NF-κB and to prevent TNF-induced apoptosis. J Biol Chem. 2009;284(51):35906-35915. PMID: 19815541; PMCID: PMC2791019; DOI: 10.1074/jbc.M109.072256.
- [petersen-2015-traf2-necroptosis] Petersen SL, Chen TT, Lawrence DA, Marsters SA, Gonzalvez F, Ashkenazi A. TRAF2 is a biologically important necroptosis suppressor. Cell Death Differ. 2015;22(11):1846-1857. PMID: 25882049; PMCID: PMC4648330; DOI: 10.1038/cdd.2015.35. (Correction: Cell Death Differ. 2026;33(3):672, PMID: 41203823.)
- [wang-2017-traf2-mtorc2] Wang B, et al. TRAF2 and OTUD7B govern a ubiquitin-dependent switch that regulates mTORC2 signalling. Nature. 2017;545(7654):365-369. PMID: 28489822; PMCID: PMC5695540; DOI: 10.1038/nature22344.
- [liang-2023-traf2-p62-mtorc1] Liang X, et al. The TRAF2-p62 axis promotes proliferation and survival of liver cancer by activating mTORC1 pathway. Cell Death Differ. 2023;30(6):1550-1562. PMID: 37081115; PMCID: PMC10244464; DOI: 10.1038/s41418-023-01164-7.
- [refseq-horse-traf2-isoforms] NCBI RefSeq protein records XP_023485172.1, XP_023485173.1, XP_070106529.1 (TNF receptor-associated factor 2 isoform X1, *Equus caballus*), retrieved via NCBI E-utilities efetch; local copy citations/refseq-horse-traf2-isoforms.fasta.
- [lalani-2018-traf-inflammation-review] Lalani AI, Zhu S, Gokhale S, Jin J, Xie P. TRAF molecules in inflammation and inflammatory diseases. Curr Pharmacol Rep. 2018;4(1):64-90. PMID: 29527458; PMCID: PMC5839642; DOI: 10.1007/s40495-017-0117-y.


## Citations

1. alvarez-2010-s1p-traf2-abstract.md
2. alvarez-2010-s1p-traf2-fulltext.txt
3. alvarez-2010-s1p-traf2-summary.md
4. bertrand-2008-ciap-rip1-abstract.md
5. bertrand-2008-ciap-rip1-summary.md
6. borghi-2016-traf2-review-abstract.md
7. borghi-2016-traf2-review-summary.md
8. brink-1998-traf2a-splice-abstract.md
9. brink-1998-traf2a-splice-summary.md
10. etemadi-2015-traf2-s1p-independent-abstract.md
11. etemadi-2015-traf2-s1p-independent-fulltext.txt
12. etemadi-2015-traf2-s1p-independent-summary.md
13. gonzalvez-2012-traf2-caspase8-abstract.md
14. gonzalvez-2012-traf2-caspase8-summary.md
15. horse-human-alignment-summary.md
16. horse-human-alignment.txt
17. horse.fasta
18. hosaka-2004-equine-tendinocyte-traf-abstract.md
19. hosaka-2004-equine-tendinocyte-traf-summary.md
20. hosaka-2005-equine-tendinocyte-tnf-abstract.md
21. hosaka-2005-equine-tendinocyte-tnf-summary.md
22. hsu-1996-tradd-traf2-abstract.md
23. hsu-1996-tradd-traf2-summary.md
24. human.fasta
25. index.tsv
26. lalani-2018-traf-inflammation-review-abstract.md
27. lalani-2018-traf-inflammation-review-fulltext.txt
28. lalani-2018-traf-inflammation-review-summary.md
29. lee-1997-traf2-jnk-abstract.md
30. lee-1997-traf2-jnk-summary.md
31. li-2009-pkc-traf2-abstract.md
32. li-2009-pkc-traf2-fulltext.txt
33. li-2009-pkc-traf2-summary.md
34. liang-2023-traf2-p62-mtorc1-abstract.md
35. liang-2023-traf2-p62-mtorc1-fulltext.txt
36. liang-2023-traf2-p62-mtorc1-summary.md
37. mace-2010-asymmetric-ciap-abstract.md
38. mace-2010-asymmetric-ciap-summary.md
39. nishitoh-1998-ask1-traf2-abstract.md
40. nishitoh-1998-ask1-traf2-summary.md
41. park-1999-traf2-structure-abstract.md
42. park-1999-traf2-structure-summary.md
43. petersen-2015-traf2-necroptosis-abstract.md
44. petersen-2015-traf2-necroptosis-summary.md
45. refseq-horse-traf2-isoforms.fasta
46. rothe-1994-traf-family-abstract.md
47. rothe-1994-traf-family-summary.md
48. rothe-1995-ciap-tnfr2-abstract.md
49. rothe-1995-ciap-tnfr2-summary.md
50. rothe-1995-traf2-nfkb-abstract.md
51. rothe-1995-traf2-nfkb-summary.md
52. tada-2001-traf2-traf5-abstract.md
53. tada-2001-traf2-traf5-summary.md
54. uniprot-2026-F7BIV4-entry.txt
55. urano-2000-ire1-traf2-abstract.md
56. urano-2000-ire1-traf2-summary.md
57. vallabhapurapu-2008-traf2-traf3-nik-abstract.md
58. vallabhapurapu-2008-traf2-traf3-nik-fulltext.txt
59. vallabhapurapu-2008-traf2-traf3-nik-summary.md
60. varfolomeev-2012-ciap-global-abstract.md
61. varfolomeev-2012-ciap-global-summary.md
62. vince-2009-traf2-ciap-binding-abstract.md
63. vince-2009-traf2-ciap-binding-summary.md
64. wade-2009-horse-genome-abstract.md
65. wade-2009-horse-genome-summary.md
66. wang-2017-traf2-mtorc2-abstract.md
67. wang-2017-traf2-mtorc2-fulltext.txt
68. wang-2017-traf2-mtorc2-summary.md
69. ye-1999-traf2-receptor-recognition-abstract.md
70. ye-1999-traf2-receptor-recognition-summary.md
71. yeh-1997-traf2-knockout-abstract.md
72. yeh-1997-traf2-knockout-summary.md
73. yin-2009-traf2-ring-abstract.md
74. yin-2009-traf2-ring-fulltext.txt
75. yin-2009-traf2-ring-summary.md
76. zarnegar-2008-noncanonical-nfkb-abstract.md
77. zarnegar-2008-noncanonical-nfkb-fulltext.txt
78. zarnegar-2008-noncanonical-nfkb-summary.md
79. zheng-2010-traf2-ciap2-structure-abstract.md
80. zheng-2010-traf2-ciap2-structure-fulltext.txt
81. zheng-2010-traf2-ciap2-structure-summary.md