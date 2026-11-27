---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:36:33.772487'
end_time: '2026-10-26T03:44:16.545442'
duration_seconds: 462.77
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: SHLD2
  gene_symbol: SHLD2
  uniprot_accession: A0A9L0RGD6
  protein_description: 'SubName: Full=Shieldin complex subunit 2 {ECO:0000313|Ensembl:ENSECAP00000060865.1};'
  gene_info: Name=SHLD2 {ECO:0000313|Ensembl:ENSECAP00000060865.1};
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: FAM35A. (IPR029715); SHLD2_C. (IPR031589); SHLD2_OB1. (IPR049507);
    SHLD2_OB2. (IPR053944); OB_SHLD2_2nd (PF22779)
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
citation_count: 68
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0RGD6
- **Protein Description:** SubName: Full=Shieldin complex subunit 2 {ECO:0000313|Ensembl:ENSECAP00000060865.1};
- **Gene Information:** Name=SHLD2 {ECO:0000313|Ensembl:ENSECAP00000060865.1};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** FAM35A. (IPR029715); SHLD2_C. (IPR031589); SHLD2_OB1. (IPR049507); SHLD2_OB2. (IPR053944); OB_SHLD2_2nd (PF22779)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SHLD2" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SHLD2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SHLD2** (gene ID: SHLD2, UniProt: A0A9L0RGD6) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SHLD2 (Shieldin complex subunit 2) in the horse, *Equus caballus* (UniProt A0A9L0RGD6)

## 1. Introduction and summary

The horse protein A0A9L0RGD6 is an unreviewed (TrEMBL) entry of 883 residues, named Shieldin complex subunit 2 (gene SHLD2) by automatic transfer from the Ensembl gene model ENSECAG00000001626 on horse chromosome 1, and its existence is only predicted (protein existence level 4)[uniprot-A0A9L0RGD6-entry]. No experimental study of horse SHLD2 was found. What follows therefore relies on orthology. Function is inferred from the well-studied human protein (SHLD2, formerly FAM35A or RINN2, UniProt Q86V20) and the mouse protein. The identification is not ambiguous. The symbol SHLD2 has no competing meaning in the literature, and FAM35A, RINN2 and SHLD2 are all names for the same gene[setiaputra-2019-shieldin-review-abstract][gupta-2018-shieldin-network-abstract]. The horse sequence has the full SHLD2 domain architecture: the FAM35A family signature (IPR029715), two N-terminal OB folds of the C-terminal module (SHLD2_OB1, PF21669, residues 430–563; SHLD2_OB2, PF22779, residues 595–676) and the SHLD2_C domain (PF15793, residues 733–804)[uniprot-A0A9L0RGD6-entry]. A global alignment run for this report gives about 71% identity to human SHLD2 across the full length. The REV7/SHLD3-binding N-terminus is almost invariant, and the two tryptophans that contact ssDNA in human SHLD2 are conserved (see Section 2 and NOTES-orthology.md).

In the human protein, SHLD2 is the central scaffold and the DNA-binding subunit of shieldin. Shieldin is a vertebrate-specific complex of four subunits: SHLD1, SHLD2, SHLD3 and REV7/MAD2L2. It acts downstream of 53BP1 and RIF1 to limit nucleolytic resection of DNA double-strand break (DSB) ends, promote non-homologous end joining (NHEJ) and oppose homologous recombination (HR)[gupta-2018-shieldin-network-abstract][noordermeer-2018-shieldin-abstract][dev-2018-shieldin-brca1-abstract][ghezraoui-2018-rev7-shieldin-abstract][findlay-2018-shld2-rev7-abstract][gao-2018-ob-fold-complex-abstract][tomida-2018-fam35a-abstract]. SHLD2 is not an enzyme. Its main biochemical activity is high-affinity, sequence-nonspecific binding to single-stranded DNA (ssDNA) through a C-terminal array of three OB folds related to those of RPA1 and POT1. In the shieldin–ssDNA interaction this was estimated at about 10 nM, with a clear preference for ssDNA over dsDNA[noordermeer-2018-shieldin-fulltext][dev-2018-shieldin-brca1-fulltext][gao-2018-ob-fold-complex-fulltext]. Through its disordered N-terminus, SHLD2 attaches to the SHLD3–REV7 recruitment module. Through its third OB fold it binds SHLD1, which in turn connects shieldin to the CTC1–STN1–TEN1 (CST)–Polα–primase fill-in machinery[noordermeer-2018-shieldin-fulltext][liang-2020-shieldin-assembly-fulltext][sifri-2023-alphafold-53bp1-fulltext][mirman-2018-cst-fillin-abstract][mirman-2022-cst-polalpha-abstract]. The protein works in the nucleus, concentrated in DNA damage–induced chromatin foci at DSBs[findlay-2018-shld2-rev7-abstract][noordermeer-2018-shieldin-abstract][dev-2018-shieldin-brca1-fulltext]. Physiologically, SHLD2 is needed for immunoglobulin class switch recombination (CSR) and for 53BP1-dependent fusion of unprotected telomeres. It is not needed for V(D)J recombination[ling-2020-shld2-csr-abstract][gupta-2018-shieldin-network-abstract][ghezraoui-2018-rev7-shieldin-abstract]. In BRCA1-deficient cells it mediates sensitivity to PARP inhibitors, and its loss is a recurrent mechanism of PARP-inhibitor resistance[noordermeer-2018-shieldin-abstract][dev-2018-shieldin-brca1-abstract].

## 2. Identity, orthology and domain architecture

The horse entry carries no experimental annotation. Its gene name and description come from Ensembl, and its domain calls come from InterPro/Pfam signatures[uniprot-A0A9L0RGD6-entry]. The reviewed human entry gives the reference functional annotation: SHLD2 is a component of the shieldin complex that, during G1 and S phase, acts downstream of TP53BP1 to promote NHEJ and suppress end resection. Within the complex it forms a scaffold, binding the SHLD3–MAD2L2 subcomplex through its N-terminus and SHLD1 through its C-terminus. It is nuclear and chromosome-associated, and forms nuclear foci after DNA damage[uniprot-Q86V20-human-SHLD2-entry].

To check that the horse protein is the true ortholog, the horse and human sequences were aligned globally (BLOSUM62) in this study. The horse protein is 71.4% identical over 861 aligned positions to the 904-residue human isoform (UniProt Q86V20-2). It is 70.2% identical to the 835-residue canonical isoform, which lacks one in-frame exon in the second OB fold (NOTES-orthology.md). Tomida and colleagues described both human isoforms as ubiquitously expressed products of differential splicing of a single exon that removes 69 residues from OB fold B[tomida-2018-fam35a-fulltext]. The horse model aligns without a gap across this exon, so it corresponds to the long isoform with an intact OB-B. Noordermeer and colleagues found that the natural short splice variant ("SHLD2S"), which disrupts OB-B, binds ssDNA only weakly and abnormally and fails to suppress HR. The long isoform should therefore be the functionally competent form[noordermeer-2018-shieldin-fulltext]. Dev and colleagues identified two tryptophans, W489 and W640, at the predicted ssDNA interface by analogy with RPA1. Mutating both reduced ssDNA binding and abolished complementation of radiosensitivity[dev-2018-shieldin-brca1-fulltext]. Both residues are conserved in horse, at W493 and W644. The N-terminal 60 residues that contact REV7 and SHLD3 are also nearly identical between horse and human (NOTES-orthology.md).

The overall architecture is a long, intrinsically disordered N-terminal region followed by a structured C-terminal region of three OB folds (OB-A, OB-B, OB-C). The last OB fold contains a zinc ribbon with two conserved CxxC pairs, similar to the zinc-binding OB fold of RPA1[tomida-2018-fam35a-fulltext][dev-2018-shieldin-brca1-fulltext]. Structure predictions have compared this module with RPA1 and CTC1[dev-2018-shieldin-brca1-fulltext] and with the triple OB-fold telomeric ssDNA-binding protein POT1[gao-2018-ob-fold-complex-fulltext]. Within the disordered region, an AlphaFold2 analysis found a conserved helix (human residues 237–255) predicted to pack between the second and third OB folds[sifri-2023-alphafold-53bp1-fulltext]. The N-terminal disordered region also carries sites of DNA damage–dependent post-translational modification[tomida-2018-fam35a-fulltext].

On evolution, SHLD2 orthologs have been reported in vertebrate genomes but not in invertebrates or plants[tomida-2018-fam35a-fulltext]. Gupta and colleagues called shieldin a "vertebrate-specific" complex and linked its emergence to the evolution of antibody class switching[gupta-2018-shieldin-network-abstract]. Gao and colleagues reported orthologs in "most vertebrates and a few invertebrates"[gao-2018-ob-fold-complex-fulltext]. Either way, a eutherian mammal such as the horse would be expected to carry a functional, conserved SHLD2, and this is what the sequence shows.

## 3. SHLD2 as the scaffold of the shieldin complex

Shieldin was found almost simultaneously by several groups using complementary methods. These included proximity-labelling proteomics around 53BP1[gupta-2018-shieldin-network-abstract], CRISPR screens for PARP-inhibitor resistance in BRCA1-deficient cells[noordermeer-2018-shieldin-abstract][dev-2018-shieldin-brca1-abstract], and REV7 interaction proteomics[findlay-2018-shld2-rev7-abstract][gao-2018-ob-fold-complex-abstract][tomida-2018-fam35a-abstract][ghezraoui-2018-rev7-shieldin-abstract]. Sequential affinity purification of tagged subunits showed that SHLD1, SHLD2, SHLD3 and REV7 form a single complex[noordermeer-2018-shieldin-fulltext]. Pulldowns with recombinant proteins showed that FAM35A/SHLD2 binds REV7 and SHLD1 directly. This complex is separate from the REV7-containing translesion polymerase ζ, because REV3L, POLD2 and POLD3 were absent from SHLD2 and SHLD1 immunoprecipitates[gao-2018-ob-fold-complex-fulltext].

Dependency and mapping experiments put the subunits in a linear order, SHLD3 → REV7 → SHLD2 → SHLD1. SHLD3 is the most apical subunit and contacts RIF1. The SHLD3–REV7 "recruitment module" binds the first ~50 residues of SHLD2, and the SHLD2 C-terminus (residues 421–904) with SHLD1 forms the "DNA-binding module"[noordermeer-2018-shieldin-fulltext]. SHLD1 binds the third OB fold of SHLD2[sifri-2023-alphafold-53bp1-fulltext], and Dev and colleagues found that SHLD1 reaches damage sites through its interaction with SHLD2[dev-2018-shieldin-brca1-fulltext]. On this basis Xie and colleagues describe SHLD2 as "the scaffold that bridges SHLD3–REV7 and SHLD1"[xie-2021-shieldin-trip13-fulltext].

Crystal structures have shown how the SHLD2 N-terminus is held. In the 3.5 Å structure of REV7–SHLD3(1–64)–SHLD2(1–52), SHLD3 binds two REV7 molecules, one closed (C-REV7) and one open (O-REV7). The SHLD2 N-terminus forms a β-sheet sandwich with O-REV7 and the SHLD3 N-terminus, occupying the position normally taken by the REV7 "safety belt"[liang-2020-shieldin-assembly-abstract][liang-2020-shieldin-assembly-fulltext]. SHLD2(1–60) bound REV7–SHLD3 only when the REV7 conformational dimer could form. The dimer-breaking REV7 R124A mutation prevented SHLD2 binding, and a dimer-defective REV7 acted as a dominant negative for NHEJ. SHLD3-driven REV7 dimerization is therefore required to recruit SHLD2[liang-2020-shieldin-assembly-fulltext]. An independent structure of a fused SHLD2(1–19)–SHLD3(1–58) peptide bound to REV7 confirmed this. The SHLD2–SHLD3 segment acts as a strap that stabilizes the O-REV7/C-REV7 heterodimer[xie-2021-shieldin-trip13-abstract][xie-2021-shieldin-trip13-fulltext]. Cell-based work agrees that MAD2L2/REV7 dimerization is needed for shieldin assembly and NHEJ, and that SHLD2 promotes this dimerization and speeds up MAD2L2–SHLD3 association[dekrijger-2021-mad2l2-dimer-abstract]. In kinetic reconstitutions, SHLD3 binds the first REV7 slowly, and this is the rate-limiting step. SHLD3 and SHLD2 then bind the second REV7 quickly, without remodelling[susvirkar-2023-shieldin-kinetics-abstract].

Because REV7 must cycle between open and closed states, shieldin can be taken apart. The AAA+ ATPase TRIP13 converts REV7 from the active closed form to the inactive open form, which dissociates REV7–shieldin and favours HR[clairmont-2020-trip13-abstract]. Cryo-EM structures of TRIP13 bound to the SHLD2–SHLD3–REV7 assembly show that TRIP13 engages the REV7 N-terminus and pulls it through its central pore[xie-2021-shieldin-trip13-abstract]. Assembly and disassembly of the SHLD2-containing complex are thus regulated steps in DSB repair pathway choice.

## 4. Molecular function: ssDNA binding by the OB-fold module

SHLD2's main biochemical activity is binding to single-stranded DNA. Three independent studies showed this with purified proteins. Noordermeer and colleagues purified the SHLD2 C-terminus (residues 421–904), alone and with SHLD1. In EMSAs it bound a radiolabelled ssDNA probe, and competition showed a preference for ssDNA over dsDNA. The apparent KD was about 10 nM. SHLD1 was not needed for binding but increased protein yield and changed the mobility of the shifted complex, consistent with SHLD2C–SHLD1 binding ssDNA together[noordermeer-2018-shieldin-fulltext]. Gao and colleagues found that a maltose-binding-protein fusion of the three OB folds (residues 381–904) preferred ssDNA to dsDNA, with competition between 60-nt and 30-nt ssDNA and 60-bp dsDNA[gao-2018-ob-fold-complex-fulltext]. Dev and colleagues showed that the bacterially expressed FAM35A C-terminus preferred ssDNA to dsDNA, and that ssDNA binding dropped when the RPA1-equivalent tryptophans were mutated (W489A/W640A)[dev-2018-shieldin-brca1-fulltext].

The strongest evidence that ssDNA binding is the effector function comes from separation-of-function mutants. Noordermeer and colleagues modelled the SHLD2 OB folds on RPA1 (PDB 4GNX) and designed surface mutants. One of them, m1, completely abolished ssDNA binding but still assembled with the other shieldin subunits and was still recruited to DSBs. It nevertheless failed to suppress RAD51 loading or HR in BRCA1/SHLD2 double-knockout cells. The authors concluded that "ssDNA binding by Shieldin is critical for 53BP1-dependent DSB repair"[noordermeer-2018-shieldin-fulltext]. In the same study, tethering the OB-fold C-terminus of SHLD2 to DSBs with an RNF8 FHA domain was enough to suppress RAD51 recruitment in cells lacking both BRCA1 and 53BP1. The ssDNA-binding module can therefore act alone, without the upstream 53BP1 chromatin platform[noordermeer-2018-shieldin-fulltext]. Dev and colleagues found that the W489A/W640A mutant still bound SHLD1 and formed ionizing radiation–induced foci (IRIF), but the foci were weaker and the mutant did not restore IR resistance. This suggests that, after recruitment through the N-terminus, ssDNA binding helps retain or stabilize SHLD2 at breaks[dev-2018-shieldin-brca1-fulltext].

These data, together with the OB-fold homology to RPA1 and POT1, led to an early "end-capping" model. In this model SHLD2 binds the ssDNA produced by initial resection and, like POT1 at telomeres, blocks further processing by long-range resection nucleases[gao-2018-ob-fold-complex-abstract][setiaputra-2019-shieldin-review-abstract]. In agreement, loss of SHLD2 increased RPA and BrdU-ssDNA signals at damage sites, increased BLM recruitment and raised RPA2 S4/S8 phosphorylation. This hyper-resection required CtIP and BLM[dev-2018-shieldin-brca1-fulltext]. Loss of shieldin also lifted the block on BRCA2 and RAD51 loading in BRCA1-deficient cells. This suggests that SHLD2-bound ssDNA resists the RPA-to-RAD51 exchange that starts HR[dev-2018-shieldin-brca1-fulltext][dev-2018-shieldin-brca1-abstract].

## 5. Subcellular localization and recruitment to DNA breaks

SHLD2 works in the nucleus. Experimental support for nuclear and chromosome localization in human cells comes from damage-induced focus formation[uniprot-Q86V20-human-SHLD2-entry][noordermeer-2018-shieldin-abstract][findlay-2018-shld2-rev7-abstract]. FAM35A relocalized within damaged nuclei[tomida-2018-fam35a-abstract], and GFP-FAM35A formed IRIF that super-resolution microscopy placed next to 53BP1 domains[dev-2018-shieldin-brca1-fulltext]. Recruitment follows a hierarchy. Shieldin reaches DSBs through the ATM–RNF8–RNF168–53BP1–RIF1 axis[gupta-2018-shieldin-network-abstract], and SHLD2 accumulation at DSBs needs 53BP1, RIF1 and REV7[findlay-2018-shld2-rev7-abstract][noordermeer-2018-shieldin-abstract]. The link from RIF1 to shieldin was first predicted with AlphaFold2 and then validated experimentally. It is a direct contact between the RIF1 HEAT-repeat domain and the eIF4E-like domain of SHLD3. Mutations at this interface stopped SHLD3 and SHLD2 from localizing to IR-induced foci and blocked CSR and PARP-inhibitor sensitivity[sifri-2023-alphafold-53bp1-abstract][sifri-2023-alphafold-53bp1-fulltext]. Recruitment of SHLD2 therefore depends on its N-terminal binding to SHLD3–REV7. The SHLD2 C-terminus with its ssDNA-binding activity then contributes to retention[noordermeer-2018-shieldin-fulltext][dev-2018-shieldin-brca1-fulltext]. Shieldin acts mainly in G1 and S phase, when 53BP1 dominates over BRCA1[uniprot-Q86V20-human-SHLD2-entry]. Live-cell kinetics refine this picture: shieldin arrives at only a subset of 53BP1-marked breaks, hours after the 53BP1-associated resection inhibitor DYNLL1, and mainly in G1 cells. Its localization requires MRE11 nuclease activity and is tuned by the DYNLL1–MRE11 interaction. This implies that SHLD2 is loaded onto ends that have already undergone limited MRE11-initiated processing, consistent with its preference for single-stranded DNA[swift-2023-dynll1-mre11-abstract].

The horse protein is predicted to have the same nuclear, DSB-associated localization, since every recruitment determinant characterized in human SHLD2 is conserved in its N-terminus (Section 2). The horse UniProt entry itself has no localization annotation[uniprot-A0A9L0RGD6-entry].

## 6. Pathway context: from end protection to fill-in synthesis

The current view places SHLD2 in a linear pathway, 53BP1 → RIF1 → SHLD3–REV7 → SHLD2–SHLD1 → CST–Polα–primase, with further downstream factors. The first models treated shieldin as a direct cap on ends. Mirman and colleagues then showed that the RPA-like CTC1–STN1–TEN1 complex, an accessory factor of Polα–primase, acts downstream of 53BP1–RIF1–shieldin. CST interacts with shieldin and localizes with Polα to damage sites in a shieldin-dependent way, and depleting CST increases resection[mirman-2018-cst-fillin-abstract]. Later work in BRCA1-deficient cells showed BrdU incorporation at DSBs that depended on shieldin, CST, Polα and primase. Artificially tethering CST near DSBs bypassed the need for 53BP1 or shieldin. The authors concluded that in this setting shieldin acts "primarily by recruiting CST" so that CST–Polα–primase can fill in resected ends[mirman-2022-cst-polalpha-abstract]. In mouse genetics, shieldin-null and CST-null animals have equivalent immune phenotypes. ATM signalling induces physical contact between shieldin and CST, which King and colleagues interpret as shieldin acting as a "DSB-responsive CST adaptor". Polymerase ζ also acts downstream of shieldin, which led them to propose fill-in DNA synthesis as the physiological function of shieldin–CST[king-2025-shieldin-cst-tailed-abstract]. The best-mapped contact to CST is the SHLD1 N-terminus binding CTC1, and an SHLD1 mutant that cannot bind CST is inactive in BRCA1-deficient cells[mirman-2022-cst-polalpha-abstract][sifri-2023-alphafold-53bp1-fulltext]. AlphaFold2 also predicted a second contact between the third SHLD2 OB fold and CTC1, compatible with SHLD1 binding, but it was not confirmed in yeast two-hybrid assays[sifri-2023-alphafold-53bp1-fulltext]. King and colleagues note that CST recruitment to telomeres depends on CTC1 binding the triple OB-fold region of POT1. They suggest that the similar triple OB-fold region of SHLD2 might recruit CST to DSBs in the same way[king-2025-shieldin-cst-tailed-fulltext]. The two models need not conflict. SHLD2 binding to ssDNA could both slow resection and place CST–Polα–primase on the 3′ overhang for fill-in.

Other effectors act downstream of shieldin. ASTE1 is a structure-specific endonuclease that cleaves ssDNA and 3′ overhangs. It is recruited to damage sites in a shieldin-dependent way and interacts with SHLD2. Its loss causes hyper-resection, NHEJ and CSR defects, and PARP-inhibitor resistance. This suggests that the SHLD2-bound 3′ overhang can be trimmed as well as protected[zhao-2021-aste1-abstract][uniprot-Q86V20-human-SHLD2-entry]. CCAR2/DBC1 co-purifies with shieldin and acts downstream of it to limit resection and support refill of resected DSBs. Forcing CCAR2 to DSBs re-sensitized BRCA1/SHLD2 double-knockout cells to PARP inhibitors[iyer-2022-ccar2-abstract]. In B-cell CSR, CTC1 and SHLD1 are epistatic in preventing excess resection and genomic instability. However, the SHLD1 CST-binding motif is not needed for CSR, which points to additional, SHLD1-independent ways of engaging CST at switch-region breaks[lescale-2025-cst-csr-abstract][mirman-2022-cst-polalpha-abstract].

Shieldin also has a function beyond the classic 53BP1 axis. In mouse ES cells lacking the BRCA1 BRCT domain, deleting Shld2 or Shld3, but not 53bp1, conferred PARP-inhibitor resistance and partly restored HR at replication-coupled DSBs. This 53BP1-independent activity required CST[feng-2026-shieldin-brca1-abstract]. Conversely, in BARD1- and BRCA1-deficient mouse models, 53BP1 suppressed HR partly independently of shieldin. SHLD2 loss therefore gave weaker PARP-inhibitor resistance than 53BP1 loss in those settings[king-2025-shieldin-cst-tailed-abstract][king-2025-shieldin-cst-tailed-fulltext].

## 7. Physiological roles revealed by loss of function

The clearest physiological role of SHLD2 is in antibody class switch recombination. Knocking out Shld2 in CH12F3-2 B cells impaired CSR, and the defect was epistatic with 53bp1 and Shld1 loss[noordermeer-2018-shieldin-fulltext]. FAM35A depletion compromised CSR in B cells[findlay-2018-shld2-rev7-abstract], and shieldin is essential for REV7-dependent end protection during CSR[ghezraoui-2018-rev7-shieldin-abstract]. Shld2-/- mice are defective for CSR in vivo but have normal lymphocyte development and normal RAG-mediated V(D)J recombination. A fraction of switching Shld2-/- B cells permanently lose immunoglobulin expression because over-active resection deletes exons of the acceptor constant region. SHLD2 therefore preserves the Igh locus during CSR by restricting resection of AID-induced breaks[ling-2020-shld2-csr-abstract]. Work on SHLD1 and REV7 likewise shows that shieldin is not needed for V(D)J recombination. This supports a model in which 53BP1 promotes synapsis within chromatin independently of shieldin, while shieldin protects the ssDNA ends of AID-generated breaks[vincendeau-2022-shld1-abstract][ghezraoui-2018-rev7-shieldin-abstract].

Beyond CSR, shieldin promotes NHEJ of intrachromosomal breaks and the fusion of unprotected (TRF2-deficient) telomeres[gupta-2018-shieldin-network-abstract][dev-2018-shieldin-brca1-fulltext]. SHLD2 loss impairs random plasmid integration, which depends largely on NHEJ[noordermeer-2018-shieldin-fulltext]. Cells lacking SHLD2 are hypersensitive to etoposide, ionizing radiation and especially cisplatin, with more FANCD2 foci. This differs from 53BP1-null cells and suggests that SHLD2 has functions outside the canonical 53BP1 axis[noordermeer-2018-shieldin-fulltext][dev-2018-shieldin-brca1-fulltext]. Shieldin is not needed for REV7's separate role in interstrand-crosslink repair through polymerase ζ[ghezraoui-2018-rev7-shieldin-abstract].

The best-known consequence of SHLD2 activity is in BRCA1-deficient cells. There it promotes "toxic" NHEJ, blocks HR and makes cells sensitive to PARP inhibitors. SHLD2 loss restores RAD51 loading and HR, causes strong PARP-inhibitor resistance approaching that of 53BP1 loss, and rescues the genomic instability of BRCA1-null cells[noordermeer-2018-shieldin-fulltext][dev-2018-shieldin-brca1-abstract][gupta-2018-shieldin-network-abstract][tomida-2018-fam35a-abstract]. In the mouse, loss of SHLD2 suppresses the embryonic lethality of the Brca1Δ11 allele[ling-2020-shld2-csr-abstract]. Reduced SHLD2 expression was seen in PARP-inhibitor-resistant patient-derived xenografts[dev-2018-shieldin-brca1-abstract]. FAM35A is absent from the BRCA1-mutant HCC1937 cell line and is frequently altered in prostate cancer[tomida-2018-fam35a-abstract]. These findings come from human and mouse systems. They are included here because they define the core activity of SHLD2, controlling the fate of ssDNA at DSBs, which the horse ortholog is expected to share.

## 8. Implications for functional annotation of horse SHLD2

Taken together, the evidence supports the following annotation of A0A9L0RGD6 by orthology to human Q86V20, with high confidence given the ~71% sequence identity and full conservation of functional motifs. For molecular function: single-stranded DNA binding through the C-terminal OB-fold module, which is direct, sequence-nonspecific and nanomolar affinity in the human protein[noordermeer-2018-shieldin-fulltext][dev-2018-shieldin-brca1-fulltext][gao-2018-ob-fold-complex-fulltext], plus protein binding to REV7/MAD2L2, SHLD3 and SHLD1 as the complex scaffold[liang-2020-shieldin-assembly-fulltext][xie-2021-shieldin-trip13-fulltext][noordermeer-2018-shieldin-fulltext]. For cellular component: shieldin complex, nucleus, and DNA damage–induced foci at the site of double-strand break[uniprot-Q86V20-human-SHLD2-entry][findlay-2018-shld2-rev7-abstract]. For biological process: negative regulation of DSB end resection, positive regulation of double-strand break repair by NHEJ, negative regulation of double-strand break repair by homologous recombination, and isotype switching (class switch recombination)[noordermeer-2018-shieldin-abstract][dev-2018-shieldin-brca1-abstract][ling-2020-shld2-csr-abstract]. The horse protein lacks any catalytic domain, and the literature describes no enzymatic activity for SHLD2. It should not be annotated with a catalytic function. The nuclease activity linked to shieldin belongs to the separate effector ASTE1[zhao-2021-aste1-abstract].

## Open Questions

Several questions remain open, both about SHLD2 in general and about the horse ortholog. First, no study of the horse protein exists. Basic checks would be confirming the 883-residue transcript model by RNA-seq, testing whether a short isoform lacking the OB-B exon is also expressed in horse tissues as in human[tomida-2018-fam35a-fulltext], and showing nuclear focus formation of horse SHLD2 after irradiation in equine cells. Second, there is no experimental high-resolution structure of the SHLD2 OB-fold module bound to ssDNA. Current interface models rely on homology to RPA1 and POT1 and on AlphaFold predictions[noordermeer-2018-shieldin-fulltext][sifri-2023-alphafold-53bp1-fulltext]. Such a structure would settle the footprint, the polarity (3′ versus 5′ end preference) and how SHLD1 shapes the DNA-binding surface. Third, the relative weight of end-capping and CST–Polα–primase fill-in, and whether SHLD2's own OB-C contacts CTC1 like POT1 does, remain unresolved[mirman-2022-cst-polalpha-abstract][king-2025-shieldin-cst-tailed-fulltext][lescale-2025-cst-csr-abstract]. Fourth, how post-translational modification of the long disordered N-terminus controls SHLD2 is mostly unexplored, apart from the initial observation of damage-dependent modification sites[tomida-2018-fam35a-fulltext]. Fifth, the 53BP1-independent function of SHLD2 at replication-coupled breaks and its hypersensitivity to cisplatin point to roles beyond the canonical pathway that need mechanistic definition[feng-2026-shieldin-brca1-abstract][dev-2018-shieldin-brca1-fulltext]. Finally, the reported presence of SHLD2 in "a few invertebrates"[gao-2018-ob-fold-complex-fulltext], against claims that it is vertebrate-specific[tomida-2018-fam35a-fulltext][gupta-2018-shieldin-network-abstract], deserves a systematic phylogenetic analysis. Such an analysis would clarify whether shieldin co-evolved with class switch recombination.

## References

- [uniprot-A0A9L0RGD6-entry] UniProtKB/TrEMBL entry A0A9L0RGD6_HORSE, "Shieldin complex subunit 2", *Equus caballus*; entry version 14 (10-JUN-2026). https://rest.uniprot.org/uniprotkb/A0A9L0RGD6.txt (genome source: Wade CM et al., Science 326:865-867 (2009), PMID 19892987, DOI 10.1126/science.1178158).
- [uniprot-Q86V20-human-SHLD2-entry] UniProtKB/Swiss-Prot entry SHLD2_HUMAN (Q86V20). https://rest.uniprot.org/uniprotkb/Q86V20.txt
- [gupta-2018-shieldin-network] Gupta R, Somyajit K, Narita T, et al. DNA Repair Network Analysis Reveals Shieldin as a Key Regulator of NHEJ and PARP Inhibitor Sensitivity. Cell (2018). PMID 29656893; PMCID PMC8108093; DOI 10.1016/j.cell.2018.03.050.
- [noordermeer-2018-shieldin] Noordermeer SM, Adam S, Setiaputra D, et al. The shieldin complex mediates 53BP1-dependent DNA repair. Nature 560:117-121 (2018). PMID 30022168; PMCID PMC6141009; DOI 10.1038/s41586-018-0340-7.
- [dev-2018-shieldin-brca1] Dev H, Chiang TW, Lescale C, et al. Shieldin complex promotes DNA end-joining and counters homologous recombination in BRCA1-null cells. Nat Cell Biol 20:954-965 (2018). PMID 30022119; PMCID PMC6145444; DOI 10.1038/s41556-018-0140-1.
- [ghezraoui-2018-rev7-shieldin] Ghezraoui H, Oliveira C, Becker JR, et al. 53BP1 cooperation with the REV7-shieldin complex underpins DNA structure-specific NHEJ. Nature 560:122-127 (2018). PMID 30046110; PMCID PMC6989217; DOI 10.1038/s41586-018-0362-1.
- [mirman-2018-cst-fillin] Mirman Z, Lottersberger F, Takai H, et al. 53BP1-RIF1-shieldin counteracts DSB resection through CST- and Polα-dependent fill-in. Nature 560:112-116 (2018). PMID 30022158; PMCID PMC6072559; DOI 10.1038/s41586-018-0324-7.
- [findlay-2018-shld2-rev7] Findlay S, Heath J, Luo VM, et al. SHLD2/FAM35A co-operates with REV7 to coordinate DNA double-strand break repair pathway choice. EMBO J 37:e100158 (2018). PMID 30154076; PMCID PMC6138439; DOI 10.15252/embj.2018100158.
- [tomida-2018-fam35a] Tomida J, Takata KI, Bhetawal S, et al. FAM35A associates with REV7 and modulates DNA damage responses of normal and BRCA1-defective cells. EMBO J 37:e99543 (2018). PMID 29789392; PMCID PMC6003645; DOI 10.15252/embj.201899543.
- [gao-2018-ob-fold-complex] Gao S, Feng S, Ning S, et al. An OB-fold complex controls the repair pathways for DNA double-strand breaks. Nat Commun (2018). PMID 30254264; PMCID PMC6156606; DOI 10.1038/s41467-018-06407-7.
- [setiaputra-2019-shieldin-review] Setiaputra D, Durocher D. Shieldin - the protector of DNA ends. EMBO Rep 20:e47560 (2019). PMID 30948458; PMCID PMC6501030; DOI 10.15252/embr.201847560.
- [liang-2020-shieldin-assembly] Liang L, Feng J, Zuo P, et al. Molecular basis for assembly of the shieldin complex and its implications for NHEJ. Nat Commun 11:1972 (2020). PMID 32332881; PMCID PMC7181697; DOI 10.1038/s41467-020-15879-5.
- [xie-2021-shieldin-trip13] Xie W, Wang S, Wang J, et al. Molecular mechanisms of assembly and TRIP13-mediated remodeling of the human Shieldin complex. Proc Natl Acad Sci U S A (2021). PMID 33597306; PMCID PMC7923543; DOI 10.1073/pnas.2024512118.
- [dai-2020-shld3-rev7] Dai Y, Zhang F, Wang L, et al. Structural basis for shieldin complex subunit 3-mediated recruitment of the checkpoint protein REV7 during DNA double-strand break repair. J Biol Chem (2020). PMID 31796627; PMCID PMC6952594; DOI 10.1074/jbc.ra119.011464. (Consulted for background; abstract in citations/.)
- [dekrijger-2021-mad2l2-dimer] de Krijger I, Föhr B, Pérez SH, et al. MAD2L2 dimerization and TRIP13 control shieldin activity in DNA repair. Nat Commun 12:5421 (2021). PMID 34521823; PMCID PMC8440562; DOI 10.1038/s41467-021-25724-y.
- [clairmont-2020-trip13] Clairmont CS, Sarangi P, Ponnienselvan K, et al. TRIP13 regulates DNA repair pathway choice through REV7 conformational change. Nat Cell Biol 22:87-96 (2020). PMID 31915374; PMCID PMC7336368; DOI 10.1038/s41556-019-0442-y.
- [susvirkar-2023-shieldin-kinetics] Susvirkar V, Faesen AC. Shieldin complex assembly kinetics and DNA binding by SHLD3. Commun Biol (2023). PMID 37031298; PMCID PMC10082759; DOI 10.1038/s42003-023-04757-7.
- [sifri-2023-alphafold-53bp1] Sifri C, Hoeg L, Durocher D, Setiaputra D. An AlphaFold2 map of the 53BP1 pathway identifies a direct SHLD3-RIF1 interaction critical for shieldin activity. EMBO Rep (2023). PMID 37306046; PMCID PMC10398656; DOI 10.15252/embr.202356834.
- [zhao-2021-aste1] Zhao F, Kim W, Gao H, et al. ASTE1 promotes shieldin-complex-mediated DNA repair by attenuating end resection. Nat Cell Biol 23:894-904 (2021). PMID 34354233; DOI 10.1038/s41556-021-00723-9.
- [mirman-2022-cst-polalpha] Mirman Z, Sasi NK, King A, Chapman JR, de Lange T. 53BP1-shieldin-dependent DSB processing in BRCA1-deficient cells requires CST-Polα-primase fill-in synthesis. Nat Cell Biol (2022). PMID 35027730; PMCID PMC8849574; DOI 10.1038/s41556-021-00812-9.
- [king-2025-shieldin-cst-tailed] King A, Reichl PI, Metson JS, et al. Shieldin and CST co-orchestrate DNA polymerase-dependent tailed-end joining reactions independently of 53BP1-governed repair pathway choice. Nat Struct Mol Biol (2025). PMID 39227718; PMCID PMC11753365; DOI 10.1038/s41594-024-01381-9.
- [iyer-2022-ccar2] Iyer DR, Harada N, Clairmont C, et al. CCAR2 functions downstream of the Shieldin complex to promote double-strand break end-joining. Proc Natl Acad Sci U S A (2022). PMID 36442094; PMCID PMC9894118; DOI 10.1073/pnas.2214935119.
- [lescale-2025-cst-csr] Lescale C, Marton T, Vaysse A, et al. CST Is Epistatic With Shieldin to Limit DNA Double-Strand Break End Resection and Promote Repair During Igh Class Switch Recombination. Eur J Immunol (2025). PMID 40178294; PMCID PMC11967320; DOI 10.1002/eji.202451585.
- [feng-2026-shieldin-brca1] Feng YL, Wang M, Li G, et al. 53BP1-independent Shieldin-BRCA1 antagonism at replication-coupled double-strand breaks. Nat Commun (2026). PMID 42374033; PMCID PMC13457598; DOI 10.1038/s41467-026-74867-3.
- [vincendeau-2022-shld1] Vincendeau E, Wei W, Zhang X, et al. SHLD1 is dispensable for 53BP1-dependent V(D)J recombination but critical for productive class switch recombination. Nat Commun 13:3707 (2022). PMID 35764636; PMCID PMC9240092; DOI 10.1038/s41467-022-31287-3.
- [swift-2023-dynll1-mre11] Swift ML, Zhou R, Syed A, et al. Dynamics of the DYNLL1-MRE11 complex regulate DNA end resection and recruitment of Shieldin to DSBs. Nat Struct Mol Biol (2023). PMID 37696958; PMCID PMC10686051; DOI 10.1038/s41594-023-01074-9.
- [ling-2020-shld2-csr] Ling AK, Munro M, Chaudhary N, Li C, Berru M, Wu B, Durocher D, Martin A. SHLD2 promotes class switch recombination by preventing inactivating deletions within the Igh locus. EMBO Rep 21:e49823 (2020). PMID 32558186; PMCID PMC7403657; DOI 10.15252/embr.201949823.


## Citations

1. clairmont-2020-trip13-abstract.md
2. clairmont-2020-trip13-summary.md
3. dai-2020-shld3-rev7-abstract.md
4. dai-2020-shld3-rev7-summary.md
5. dekrijger-2021-mad2l2-dimer-abstract.md
6. dekrijger-2021-mad2l2-dimer-fulltext.txt
7. dekrijger-2021-mad2l2-dimer-summary.md
8. dev-2018-shieldin-brca1-abstract.md
9. dev-2018-shieldin-brca1-fulltext.txt
10. dev-2018-shieldin-brca1-summary.md
11. feng-2026-shieldin-brca1-abstract.md
12. feng-2026-shieldin-brca1-fulltext.txt
13. feng-2026-shieldin-brca1-summary.md
14. findlay-2018-shld2-rev7-abstract.md
15. findlay-2018-shld2-rev7-fulltext.txt
16. findlay-2018-shld2-rev7-summary.md
17. gao-2018-ob-fold-complex-abstract.md
18. gao-2018-ob-fold-complex-fulltext.txt
19. gao-2018-ob-fold-complex-summary.md
20. ghezraoui-2018-rev7-shieldin-abstract.md
21. ghezraoui-2018-rev7-shieldin-summary.md
22. gupta-2018-shieldin-network-abstract.md
23. gupta-2018-shieldin-network-summary.md
24. iyer-2022-ccar2-abstract.md
25. iyer-2022-ccar2-fulltext.txt
26. iyer-2022-ccar2-summary.md
27. king-2025-shieldin-cst-tailed-abstract.md
28. king-2025-shieldin-cst-tailed-fulltext.txt
29. king-2025-shieldin-cst-tailed-summary.md
30. lescale-2025-cst-csr-abstract.md
31. lescale-2025-cst-csr-fulltext.txt
32. lescale-2025-cst-csr-summary.md
33. liang-2020-shieldin-assembly-abstract.md
34. liang-2020-shieldin-assembly-fulltext.txt
35. liang-2020-shieldin-assembly-summary.md
36. ling-2020-shld2-csr-abstract.md
37. ling-2020-shld2-csr-summary.md
38. mirman-2018-cst-fillin-abstract.md
39. mirman-2018-cst-fillin-summary.md
40. mirman-2022-cst-polalpha-abstract.md
41. mirman-2022-cst-polalpha-fulltext.txt
42. mirman-2022-cst-polalpha-summary.md
43. noordermeer-2018-shieldin-abstract.md
44. noordermeer-2018-shieldin-fulltext.txt
45. noordermeer-2018-shieldin-summary.md
46. setiaputra-2019-shieldin-review-abstract.md
47. setiaputra-2019-shieldin-review-summary.md
48. sifri-2023-alphafold-53bp1-abstract.md
49. sifri-2023-alphafold-53bp1-fulltext.txt
50. sifri-2023-alphafold-53bp1-summary.md
51. susvirkar-2023-shieldin-kinetics-abstract.md
52. susvirkar-2023-shieldin-kinetics-fulltext.txt
53. susvirkar-2023-shieldin-kinetics-summary.md
54. swift-2023-dynll1-mre11-abstract.md
55. swift-2023-dynll1-mre11-summary.md
56. tomida-2018-fam35a-abstract.md
57. tomida-2018-fam35a-fulltext.txt
58. tomida-2018-fam35a-summary.md
59. uniprot-A0A9L0RGD6-entry.txt
60. uniprot-Q86V20-human-SHLD2-entry.txt
61. vincendeau-2022-shld1-abstract.md
62. vincendeau-2022-shld1-fulltext.txt
63. vincendeau-2022-shld1-summary.md
64. xie-2021-shieldin-trip13-abstract.md
65. xie-2021-shieldin-trip13-fulltext.txt
66. xie-2021-shieldin-trip13-summary.md
67. zhao-2021-aste1-abstract.md
68. zhao-2021-aste1-summary.md