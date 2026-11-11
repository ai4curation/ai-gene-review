---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T04:00:10.177872'
end_time: '2026-10-26T04:09:29.162276'
duration_seconds: 558.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: WEE1
  gene_symbol: WEE1
  uniprot_accession: F6TY09
  protein_description: 'RecName: Full=Wee1-like protein kinase {ECO:0000256|PIRNR:PIRNR037281};
    EC=2.7.10.2 {ECO:0000256|PIRNR:PIRNR037281};'
  gene_info: Name=WEE1 {ECO:0000313|VGNC:VGNC:25026};
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the protein kinase superfamily. Ser/Thr protein
  protein_domains: CC_SR_Kinase. (IPR050339); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom.
    (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)
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
citation_count: 86
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** F6TY09
- **Protein Description:** RecName: Full=Wee1-like protein kinase {ECO:0000256|PIRNR:PIRNR037281}; EC=2.7.10.2 {ECO:0000256|PIRNR:PIRNR037281};
- **Gene Information:** Name=WEE1 {ECO:0000313|VGNC:VGNC:25026};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** CC_SR_Kinase. (IPR050339); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "WEE1" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'WEE1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **WEE1** (gene ID: WEE1, UniProt: F6TY09) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# WEE1 (Wee1-like protein kinase) in the horse, *Equus caballus* (UniProt F6TY09): function, localization and pathways

## 1. Introduction and summary

The horse gene *WEE1* (VGNC:25026; NCBI GeneID 100071182; Ensembl ENSECAG00000020774, chromosome 7) encodes a 646-residue protein, UniProt F6TY09, that is annotated as "Wee1-like protein kinase" (EC 2.7.10.2) and placed in the WEE1 subfamily of the protein kinase superfamily [uniprot-2026-f6ty09-entry]. The entry is unreviewed (TrEMBL). Its sequence was predicted from the Thoroughbred genome assembly [wade-2009-horse-genome] and has protein-existence level 3, "inferred from homology" [uniprot-2026-f6ty09-entry]. No primary experimental literature on horse WEE1 itself was found. Searches of Europe PMC for WEE1 together with horse, equine or *Equus caballus* returned only human and rodent cancer and cell-cycle studies. Everything below about horse WEE1 is therefore inferred from its near-identity to human WEE1 (P30291), the best-characterized orthologue, and from conserved findings in yeast, *Xenopus* and mouse.

The identity check is clear-cut. The horse protein is the same length as human WEE1 (646 aa) and aligns without gaps at 95.4% identity. The kinase domain is 98.2% identical. Every catalytic and regulatory residue mapped experimentally in human or *Xenopus* WEE1 is conserved (Section 2; [uniprot-2026-p30291-entry]). On this basis F6TY09 is the horse orthologue of somatic WEE1, sometimes called WEE1A. It is not the oocyte-specific paralogue WEE2/WEE1B or the membrane-bound paralogue PKMYT1.

The core function of WEE1 has been conserved from fission yeast to humans. It is a nuclear protein kinase that adds an inhibitory phosphate to Tyr15 of CDK1 (Cdc2) bound to cyclin B, and to related cyclin–CDK complexes such as CDK2. This holds CDK activity in check during S and G2 phases and prevents premature entry into mitosis [russell-1987-wee1-mitosis; parker-1992-wee1-cdc2-inactivation; mcgowan-1993-wee1-tyr15; watanabe-1995-wee1hu-regulation; heald-1993-wee1-nucleus]. WEE1 is the kinase arm of the switch that sets the timing of the G2/M transition, opposed by the CDC25 phosphatases. It also mediates the G2 DNA-damage checkpoint [oconnell-1997-chk1-wee1; hirai-2009-mk1775]. During normal S phase it limits CDK-driven origin firing and the activity of the MUS81 nuclease, which protects genome integrity [beck-2010-s-phase-cdk; dominguez-kelly-2011-wee1-mus81; sorensen-2012-atr-chk1-wee1-review]. WEE1 is essential for early mammalian embryonic development [tominaga-2006-murine-wee1].

Horse WEE1 is expected to carry out the same activities. The rest of this review sets out the evidence for each claim and points out where the database annotation of F6TY09 is misleading.

## 2. Gene identity, orthology and an annotation caveat

F6TY09 is annotated by the PIRSF037281 "Wee1-like protein kinase" family rule. Its InterPro and CDD signatures match the WEE1 group (IPR017164 Wee1-like protein kinase; cd14138 PTKc_Wee1a), and its CTD cross-reference (7465) is to human *WEE1* [uniprot-2026-f6ty09-entry]. We compared the horse and human (P30291) sequences residue by residue (notes/sequence_comparison.md). The two proteins differ at 30 positions. Most substitutions fall in the intrinsically disordered N-terminal regulatory region (residues 1–298, 91.9% identity). Only five fall in the kinase domain (residues 299–569).

Every residue whose function has been tested in other species is identical in the horse protein. The glycine-rich ATP-binding loop (residues 301–315) is unchanged, as is the catalytic lysine K328, whose mutation abolishes human WEE1 activity [mcgowan-1993-wee1-tyr15]. The catalytic-loop aspartate D426, which serves as the proton acceptor, and the Mg²⁺-binding D463 of the "DLG" motif are likewise conserved [uniprot-2026-p30291-entry; squire-2005-wee1-structure]. Beyond the catalytic core, the regulatory phosphorylation sites are also preserved: the phosphodegron serines S53 (the PLK1 site) and S121/S123 (the CK2 and CDK sites) [watanabe-2004-scf-btrcp-wee1; watanabe-2005-cdk-destabilizes-wee1], the inhibitory CDK site T239 within the conserved "Wee-box" [okamoto-2007-wee1-t239; li-2010-wee1-nuclear-export], and the C-terminal S642 that SAD/BRSK kinases phosphorylate [lu-2004-sad-wee1; muller-2010-brsk-wee1; uniprot-2026-p30291-entry]. The coiled-coil segment (residues 577–611) is also identical. Because these residues match, regulation observed in human cells can reasonably be expected to apply to horse WEE1.

One part of the F6TY09 entry should be treated with caution. Its FUNCTION comment, generated automatically by an ARBA rule, describes an "oocyte-specific protein tyrosine kinase" that maintains meiotic prophase I arrest and promotes exit from metaphase II [uniprot-2026-f6ty09-entry]. That text describes the paralogue WEE2/WEE1B, an oocyte-specific kinase downstream of PKA that is required for meiotic arrest in mouse oocytes [han-2005-wee1b-oocyte]. Somatic WEE1, by contrast, is expressed in all proliferating human cell lines examined [igarashi-1991-human-wee1]. The "Meiosis" keyword and the description of oocyte specificity are therefore probably annotation errors propagated from the WEE2 subfamily. They should not be used to infer tissue specificity for horse WEE1. A similar caveat applies to the serine/threonine kinase reactions (EC 2.7.11.1) in the entry. They come from a generic PROSITE signature for Ser/Thr kinases, and they conflict with the biochemical evidence that WEE1 acts as a tyrosine-specific kinase on CDK substrates (Section 3).

## 3. Catalytic activity and substrate specificity

WEE1 catalyses the transfer of the γ-phosphate of ATP to a protein tyrosine residue: L-tyrosyl-[protein] + ATP → O-phospho-L-tyrosyl-[protein] + ADP + H⁺ (EC 2.7.10.2), with Mg²⁺ as cofactor [uniprot-2026-p30291-entry; squire-2005-wee1-structure]. The fission yeast enzyme can phosphorylate serine and threonine as well as tyrosine in vitro, which led to a hypothesis that human WEE1 might be dual-specific [mcgowan-1993-wee1-tyr15]. Two independent biochemical studies disproved this.

Parker and Piwnica-Worms produced human WEE1 in bacteria and found it to be a tyrosine-specific kinase. It phosphorylated the p34cdc2–cyclin B complex on Tyr15 but not Thr14, inactivating the complex, and the effect was reversed by the phosphatase Cdc25C [parker-1992-wee1-cdc2-inactivation]. McGowan and Russell likewise showed that purified human WEE1 phosphorylates Cdc2 exclusively on Tyr15, as well as synthetic peptides at the Tyr15-equivalent position. Mutating the catalytic lysine abolished both its in vitro activity and its ability to block cell division [mcgowan-1993-wee1-tyr15]. The Thr14 site is instead phosphorylated by the paralogue Myt1/PKMYT1, a membrane-associated Wee1-family kinase that targets both Thr14 and Tyr15 [mueller-1995-myt1; schmidt-2017-wee1-pkmyt1-review].

The substrates are cyclin-bound CDKs rather than free kinase subunits. Endogenous human WEE1 immunoprecipitated from cells phosphorylated several cyclin-associated CDKs on Tyr15. Its main physiological target before mitosis is cyclin B1–CDK1 [watanabe-1995-wee1hu-regulation], and monomeric CDK1 is not phosphorylated [uniprot-2026-p30291-entry]. WEE1 also phosphorylates CDK2 on Tyr15, and this is central to its role in S phase [sorensen-2012-atr-chk1-wee1-review; beck-2010-s-phase-cdk]. Cyclin A–CDK2 associates physically with WEE1 through RXL cyclin-binding motifs in the disordered N-terminal region [li-2010-wee1-nuclear-export].

Pharmacology supports this assignment of substrate. The selective inhibitor MK-1775 (adavosertib) reduces CDC2 Tyr15 phosphorylation in cells, tumours and hair follicles [hirai-2009-mk1775]. Acute WEE1 inhibition produces a rapid, global rise in CDK-dependent phosphorylation, revealing more than 600 previously uncharacterized CDK sites [petrosius-2023-wee1-phosphoproteomics]. Most cellular effects of WEE1 therefore follow indirectly from releasing CDK activity.

One well-supported non-CDK substrate has been reported. Mahajan and colleagues identified WEE1 as the kinase that phosphorylates histone H2B on Tyr37 upstream of the replication-dependent histone gene cluster *Hist1* in late S phase. This modification excludes the coactivator NPAT and RNA polymerase II, recruits the chaperone HIRA, and shuts down histone transcription. The function is conserved from yeast to mammals [mahajan-2012-h2b-tyr37]. In this role WEE1 acts as a chromatin-modifying tyrosine kinase rather than as a CDK inhibitor. The residues needed for this activity lie in the kinase domain, which is 98% identical in horse.

## 4. Structural basis of tyrosine specificity

The crystal structure of the human WEE1A catalytic domain has been solved at 1.8 Å resolution in complex with an active-site inhibitor. It shows that WEE1, although functionally a tyrosine kinase, most closely resembles serine/threonine kinases such as CHK1 and PKA in sequence and fold [squire-2005-wee1-structure]. This explains why automated pipelines classify it in the "Ser/Thr protein kinase family", as F6TY09 is [uniprot-2026-f6ty09-entry].

Two WEE1-specific features appear to shape its substrate preference: an activation segment that holds the kinase in a constitutively active conformation, and a key substitution in the glycine-rich loop [squire-2005-wee1-structure]. Further structures of the kinase domain bound to MK-1775, bosutinib and other inhibitors show WEE1 in the active, "DFG-in" conformation [schmidt-2017-wee1-pkmyt1-review]. Activity also depends on an N-terminal element called the "Wee-box", identified in *Xenopus* somatic Wee1. It acts positively on the catalytic domain, which on its own phosphorylates Cdc2 poorly [okamoto-2007-wee1-t239]. The Wee-box sequence, including the threonine–proline motif at T239, is conserved in horse WEE1 (Section 2).

## 5. Regulation of WEE1 activity and abundance

WEE1 activity rises and falls through the cell cycle. In human cells its protein level and kinase activity increase during S and G2. At M phase the protein becomes hyperphosphorylated and activity drops, and protein levels fall at M/G1 through degradation [watanabe-1995-wee1hu-regulation]. Several mechanisms produce this pattern, and each acts through residues conserved in the horse protein.

The first mechanism is direct inhibition by CDKs. CDK1 phosphorylates the Wee-box TP motif (Thr186 in *Xenopus*, corresponding to human Thr239). The phosphorylated motif binds the prolyl isomerase Pin1, which inactivates WEE1 at M phase [okamoto-2007-wee1-t239]. In human cells T239 is phosphorylated in a cyclin A–CDK2-dependent way, and T239A or RXL1 mutants inhibit G2/M more strongly than wild-type WEE1 [li-2010-wee1-nuclear-export]. This forms part of the positive feedback loop that makes CDK1 activation switch-like.

The second mechanism is ubiquitin-dependent degradation. PLK1 phosphorylates S53 and CDK1 phosphorylates S123, creating non-canonical phosphodegrons that the F-box proteins β-TrCP1/2 recognize. SCF^β-TrCP then ubiquitinates WEE1 for proteasomal degradation, which is needed for a normal onset of mitosis [watanabe-2004-scf-btrcp-wee1]. Phospho-S123 also primes PLK1 docking through a polo-box-binding motif and primes CK2 phosphorylation of S121, creating a second degron [watanabe-2005-cdk-destabilizes-wee1]. A second SCF ligase, containing the F-box protein Tome-1, also targets WEE1. Tome-1 is itself destroyed by the APC in G1, which lets WEE1 accumulate during interphase [ayad-2003-tome1]. SCF^β-TrCP and SCF^Tome-1 act redundantly to degrade WEE1 in S and G2 [smith-2007-wee1-degradation].

The third mechanism is positive regulation by checkpoint signalling and 14-3-3 proteins. In fission yeast, Chk1 phosphorylates Wee1, and Wee1 is needed for Chk1-induced G2 arrest [oconnell-1997-chk1-wee1]. In *Xenopus*, Chk1 phosphorylates Wee1 on Ser549, creating a 14-3-3 binding site. A mutant that cannot bind 14-3-3 has reduced kinase activity and an altered distribution within the nucleus [lee-2001-chk1-1433-wee1]. In mammals, a two-hybrid screen with the C-terminal half of mouse Wee1 first isolated 14-3-3ζ, and binding required both the kinase domain and a C-terminal sequence [honda-1997-1433-mouse-wee1]. Human WEE1 likewise binds 14-3-3 proteins mainly in interphase, and loss of binding lowers its enzymatic activity and its ability to impose a G2 delay [rothblum-oviatt-2001-1433-wee1]. Human SAD1 phosphorylates the C-terminal S642 in vitro [lu-2004-sad-wee1], and this residue and its surrounding sequence (MNRSVS642LTIY) are conserved in horse. The 14-3-3-binding site of human WEE1 was not mapped in the sources reviewed here, so whether S642 is the functional equivalent of *Xenopus* Ser549 is an inference that remains to be confirmed.

The fourth mechanism is dephosphorylation. At mitotic exit, the phosphatase Fcp1 (CTDP1) removes the phosphate from T239 and restores WEE1 activity towards cyclin B–CDK1, which helps inactivate MPF [visconti-2012-fcp1-wee1]. During replication stress, CHK1-dependent activation of PP2A-B55α (through phosphorylation of FAM122A) dephosphorylates WEE1 and protects it from degradation [li-2020-fam122a-chk1].

In post-mitotic neurons, SAD-A/SAD-B (BRSK2/BRSK1) phosphorylate WEE1 and trigger its downregulation, which is needed for axon–dendrite polarization [muller-2010-brsk-wee1]. Human SAD1 phosphorylates WEE1A on S642 in vitro [lu-2004-sad-wee1].

## 6. Subcellular localization

WEE1 carries out its main function in the nucleus. The F6TY09 entry assigns it to the nucleus by family rule [uniprot-2026-f6ty09-entry], which is consistent with experimental data in human cells. Heald and colleagues showed that human WEE1 is nuclear while its antagonist Cdc25C and its target cyclin B1 are cytoplasmic in interphase. They proposed that WEE1 "protects the nucleus" from cyclin B–CDK1 activated in the cytoplasm until the G2/M transition, so that DNA replication finishes before mitosis [heald-1993-wee1-nucleus].

Immunolocalization in HeLa and IMR90 cells showed that WEE1 is almost exclusively nuclear in interphase. It moves into the cytoplasm at mitotic entry, gathers at the mitotic equator during division, and ends up associated with midbody bridges in a microtubule-dependent manner [baldin-1995-wee1-localisation]. WEE1 also moves between nucleus and cytoplasm in interphase. A CRM1-dependent nuclear export signal overlapping the RXL1 cyclin-binding motif mediates export, which is promoted by cyclin A–CDK activity and blocked by leptomycin B [li-2010-wee1-nuclear-export]. Reviews agree that WEE1 is mostly nuclear, with a smaller cytoplasmic pool [schmidt-2017-wee1-pkmyt1-review].

Its chromatin-associated activity on H2B Tyr37 at the *Hist1* locus places part of WEE1 function directly on chromatin [mahajan-2012-h2b-tyr37]. The Ensembl-derived "nucleolus" and family-level "cytoplasm" GO terms on F6TY09 [uniprot-2026-f6ty09-entry] fit this picture of a mainly nucleoplasmic and chromatin-associated kinase that shuttles to the cytoplasm. They have no horse-specific support.

## 7. Pathways and biological roles

### 7.1 The G2/M transition and mitotic timing

WEE1 is a dose-dependent inhibitor of mitosis. Loss of function makes cells enter mitosis prematurely at a small size, and overexpression delays mitosis [russell-1987-wee1-mitosis]. Human WEE1 rescues yeast *wee1* mutants and delays G2/M when overexpressed [igarashi-1991-human-wee1]. In human cells, overexpression blocks division [mcgowan-1993-wee1-tyr15].

Within the cyclin B–CDK1 activation network, WEE1 (together with PKMYT1) and CDC25 set the level of inhibitory phosphorylation on CDK1 [schmidt-2017-wee1-pkmyt1-review]. Rising CDK1 and PLK1 activity at G2/M inactivates and degrades WEE1, making mitotic entry abrupt and irreversible [watanabe-2004-scf-btrcp-wee1; okamoto-2007-wee1-t239]. Fcp1-dependent reactivation of WEE1 later helps reset the cycle at mitotic exit [visconti-2012-fcp1-wee1].

### 7.2 The G2 DNA-damage checkpoint

Under DNA damage, CHK1 phosphorylates WEE1, which helps maintain Tyr15 phosphorylation and G2 arrest [oconnell-1997-chk1-wee1; lee-2001-chk1-1433-wee1]. Mouse *Wee1⁻/⁻* embryos have a defective G2/M checkpoint after γ-irradiation [tominaga-2006-murine-wee1]. Pharmacological WEE1 inhibition abrogates the G2 DNA-damage checkpoint and forces damaged cells into mitosis. This selectively sensitizes p53-deficient cells, which lack a G1 checkpoint, to DNA-damaging chemotherapy [hirai-2009-mk1775]. Later phosphoproteomic work showed that WEE1 adjusts CDK activity so that 53BP1 can be recruited to chromatin, linking WEE1 to the choice of DNA double-strand-break repair pathway [petrosius-2023-wee1-phosphoproteomics].

### 7.3 S-phase genome maintenance

WEE1 also acts outside mitosis. A kinome-wide siRNA screen found that WEE1 depletion rapidly produces DNA damage and single-stranded DNA in newly replicated DNA. This damage depends on CDK1/2 and on the replication factors MCM2 and CDT1 [beck-2010-s-phase-cdk]. WEE1 loss slows replication forks and causes S-phase accumulation and a DNA-damage response that depend on the MUS81–EME1 endonuclease, which physically interacts with WEE1 [dominguez-kelly-2011-wee1-mus81].

The current model is that WEE1, ATR and CHK1 together hold back CDK activity during normal S phase. When they fail, unscheduled origin firing produces structures that nucleases cleave into double-strand breaks [sorensen-2012-atr-chk1-wee1-review]. WEE1 and CHK1 do this in different ways: WEE1 mainly limits CDK activity, while CHK1 mainly limits CDC45 loading [hauge-2017-wee1-chk1-cdc45]. WEE1 inhibition also triggers CDK-driven degradation of the ribonucleotide reductase subunit RRM2, causing dNTP depletion. Cells lacking H3K36me3 cannot compensate, which makes them highly sensitive to WEE1 inhibitors [pfister-2015-wee1-h3k36me3]. The H2B Tyr37 pathway adds a further S-phase role: limiting histone gene transcription once DNA synthesis is complete [mahajan-2012-h2b-tyr37].

### 7.4 Development and differentiation

In mammals, *Wee1* is essential. Knockout mouse embryos die by apoptosis before E3.5, and acute deletion of *Wee1* in embryonic fibroblasts causes aneuploidy, γ-H2AX foci, CHK2 activation and cell death [tominaga-2006-murine-wee1]. In post-mitotic neurons, WEE1 must be downregulated by SAD kinases for neuronal polarity to form [muller-2010-brsk-wee1]. This shows a role for WEE1 regulation outside the cell cycle.

Given the 95% sequence identity and conserved regulatory sites, horse WEE1 is predicted to be essential in early equine embryos and to act in the same pathways. The Bgee annotation of expression in the horse inner cell mass and 23 other cell types or tissues fits this prediction [uniprot-2026-f6ty09-entry]. None of these roles has been tested directly in horse cells.

### 7.5 Paralogues and division of labour

Vertebrates have three WEE-family kinases. Nuclear WEE1 phosphorylates Tyr15 only. Membrane-associated PKMYT1 phosphorylates both Thr14 and Tyr15 of CDK1 [mueller-1995-myt1; schmidt-2017-wee1-pkmyt1-review]. Oocyte-specific WEE2/WEE1B maintains meiotic arrest downstream of PKA [han-2005-wee1b-oocyte]. Reviews summarize WEE1 and PKMYT1 as tumour suppressors in normal cells and as "pseudo-oncogenes" in cancers that depend on them, and both are clinical drug targets [ghelli-2020-wee1-family-review]. This division of labour should guide functional annotation. Horse WEE1 should be annotated with protein tyrosine kinase activity, negative regulation of the G2/M transition of the mitotic cell cycle, and nuclear localization. It should not be annotated as meiosis-specific.

## 8. Open Questions

Horse WEE1 has no direct experimental characterization, so the most basic open question is whether its biochemistry, cell-cycle regulation and localization match those of human WEE1. That would require at least one experiment in horse cells, for example a Tyr15-CDK1 immunoblot after adavosertib treatment of equine fibroblasts, or immunofluorescence for WEE1. Commercial antibodies raised against human WEE1 epitopes would probably cross-react given the 95% identity, but this needs checking.

The 30 horse–human substitutions cluster in the disordered N-terminal regulatory region (residues 16–20, 93–104, 131–170, 210–274). Some lie close to mapped regulatory elements, such as substitutions at 243 and 245 near the T239 Wee-box and RXL1/NES region, and at 131–170 among documented human phosphosites. Whether these changes alter phosphorylation, cyclin A–CDK2 binding or nuclear export kinetics in the horse is unknown.

The automated ARBA function comment on F6TY09, which describes oocyte-specific meiotic WEE2 activity, should be reported to UniProt for correction. Horse WEE2 should be annotated separately, and equine oocyte biology, which is of interest in assisted reproduction, may be better served by studying WEE2 and PKMYT1.

Within the wider WEE1 field, the full range of non-CDK substrates (beyond H2B Tyr37) is not settled. Nor is it fully understood how WEE1 physically restrains MUS81–EME1, or how WEE1-dependent CDK tuning connects to 53BP1-mediated repair. Pharmacological inhibitors could be used to address these questions in comparative or veterinary oncology. Equine tumours such as sarcoids and melanomas are examples, but no such studies were found.

## 9. References

- [ayad-2003-tome1] Ayad NG, Rankin S, Murakami M, Jebanathirajah J, Gygi S, Kirschner MW. Tome-1, a trigger of mitotic entry, is degraded during G1 via the APC. Cell 2003;113(1):101-113. PMID: 12679038. DOI: 10.1016/s0092-8674(03)00232-0.
- [baldin-1995-wee1-localisation] Baldin V, Ducommun B. Subcellular localisation of human wee1 kinase is regulated during the cell cycle. J Cell Sci 1995;108(Pt 6):2425-2432. PMID: 7673359. DOI: 10.1242/jcs.108.6.2425.
- [beck-2010-s-phase-cdk] Beck H, Nähse V, Larsen MS, Groth P, Clancy T, Lees M, Jørgensen M, Helleday T, Syljuåsen RG, Sørensen CS. Regulators of cyclin-dependent kinases are crucial for maintaining genome integrity in S phase. J Cell Biol 2010;188(5):629-638. PMID: 20194642. PMCID: PMC2835936. DOI: 10.1083/jcb.200905059.
- [dominguez-kelly-2011-wee1-mus81] Domínguez-Kelly R, Martín Y, Koundrioukoff S, Tanenbaum ME, Smits VA, Medema RH, Debatisse M, Freire R. Wee1 controls genomic stability during replication by regulating the Mus81-Eme1 endonuclease. J Cell Biol 2011;194(4):567-579. PMID: 21859861. PMCID: PMC3160579. DOI: 10.1083/jcb.201101047.
- [ghelli-2020-wee1-family-review] Ghelli Luserna di Rorà A, Cerchione C, Martinelli G, Simonetti G. A WEE1 family business: regulation of mitosis, cancer progression, and therapeutic target. J Hematol Oncol 2020;13(1):126. PMID: 32958072. PMCID: PMC7507691. DOI: 10.1186/s13045-020-00959-2.
- [han-2005-wee1b-oocyte] Han SJ, Chen R, Paronetto MP, Conti M. Wee1B is an oocyte-specific kinase involved in the control of meiotic arrest in the mouse. Curr Biol 2005;15(18):1670-1676. PMID: 16169490. DOI: 10.1016/j.cub.2005.07.056.
- [honda-1997-1433-mouse-wee1] Honda R, Ohba Y, Yasuda H. 14-3-3 zeta protein binds to the carboxyl half of mouse wee1 kinase. Biochem Biophys Res Commun 1997;230(2):262-265. PMID: 9016762. DOI: 10.1006/bbrc.1996.5933.
- [hauge-2017-wee1-chk1-cdc45] Hauge S, Naucke C, Hasvold G, Joel M, Rødland GE, Juzenas P, Stokke T, Syljuåsen RG. Combined inhibition of Wee1 and Chk1 gives synergistic DNA damage in S-phase due to distinct regulation of CDK activity and CDC45 loading. Oncotarget 2017;8(7):10966-10979. PMID: 28030798. PMCID: PMC5355238. DOI: 10.18632/oncotarget.14089.
- [heald-1993-wee1-nucleus] Heald R, McLoughlin M, McKeon F. Human wee1 maintains mitotic timing by protecting the nucleus from cytoplasmically activated Cdc2 kinase. Cell 1993;74(3):463-474. PMID: 8348613. DOI: 10.1016/0092-8674(93)80048-j.
- [hirai-2009-mk1775] Hirai H, Iwasawa Y, Okada M, et al. Small-molecule inhibition of Wee1 kinase by MK-1775 selectively sensitizes p53-deficient tumor cells to DNA-damaging agents. Mol Cancer Ther 2009;8(11):2992-3000. PMID: 19887545. DOI: 10.1158/1535-7163.mct-09-0463.
- [igarashi-1991-human-wee1] Igarashi M, Nagata A, Jinno S, Suto K, Okayama H. Wee1(+)-like gene in human cells. Nature 1991;353(6339):80-83. PMID: 1840647. DOI: 10.1038/353080a0.
- [lee-2001-chk1-1433-wee1] Lee J, Kumagai A, Dunphy WG. Positive regulation of Wee1 by Chk1 and 14-3-3 proteins. Mol Biol Cell 2001;12(3):551-563. PMID: 11251070. PMCID: PMC30963. DOI: 10.1091/mbc.12.3.551.
- [li-2010-wee1-nuclear-export] Li C, Andrake M, Dunbrack R, Enders GH. A bifunctional regulatory element in human somatic Wee1 mediates cyclin A/Cdk2 binding and Crm1-dependent nuclear export. Mol Cell Biol 2010;30(1):116-130. PMID: 19858290. DOI: 10.1128/mcb.01876-08.
- [li-2020-fam122a-chk1] Li F, Kozono D, Deraska P, et al. CHK1 Inhibitor Blocks Phosphorylation of FAM122A and Promotes Replication Stress. Mol Cell 2020;80(3):410-422.e6. PMID: 33108758. PMCID: PMC7761918. DOI: 10.1016/j.molcel.2020.10.008.
- [lu-2004-sad-wee1] Lu R, Niida H, Nakanishi M. Human SAD1 kinase is involved in UV-induced DNA damage checkpoint function. J Biol Chem 2004;279(30):31164-31170. PMID: 15150265. DOI: 10.1074/jbc.m404728200.
- [mahajan-2012-h2b-tyr37] Mahajan K, Fang B, Koomen JM, Mahajan NP. H2B Tyr37 phosphorylation suppresses expression of replication-dependent core histone genes. Nat Struct Mol Biol 2012;19(9):930-937. PMID: 22885324. PMCID: PMC4533924. DOI: 10.1038/nsmb.2356.
- [mcgowan-1993-wee1-tyr15] McGowan CH, Russell P. Human Wee1 kinase inhibits cell division by phosphorylating p34cdc2 exclusively on Tyr15. EMBO J 1993;12(1):75-85. PMID: 8428596. PMCID: PMC413177. DOI: 10.1002/j.1460-2075.1993.tb05633.x.
- [mueller-1995-myt1] Mueller PR, Coleman TR, Kumagai A, Dunphy WG. Myt1: a membrane-associated inhibitory kinase that phosphorylates Cdc2 on both threonine-14 and tyrosine-15. Science 1995;270(5233):86-90. PMID: 7569953. DOI: 10.1126/science.270.5233.86.
- [muller-2010-brsk-wee1] Müller M, Lutter D, Püschel AW. Persistence of the cell-cycle checkpoint kinase Wee1 in SadA- and SadB-deficient neurons disrupts neuronal polarity. J Cell Sci 2010;123(Pt 2):286-294. PMID: 20026642. DOI: 10.1242/jcs.058230.
- [oconnell-1997-chk1-wee1] O'Connell MJ, Raleigh JM, Verkade HM, Nurse P. Chk1 is a wee1 kinase in the G2 DNA damage checkpoint inhibiting cdc2 by Y15 phosphorylation. EMBO J 1997;16(3):545-554. PMID: 9034337. PMCID: PMC1169658. DOI: 10.1093/emboj/16.3.545.
- [okamoto-2007-wee1-t239] Okamoto K, Sagata N. Mechanism for inactivation of the mitotic inhibitory kinase Wee1 at M phase. Proc Natl Acad Sci USA 2007;104(10):3753-3758. PMID: 17360425. PMCID: PMC1820656. DOI: 10.1073/pnas.0607357104.
- [parker-1992-wee1-cdc2-inactivation] Parker LL, Piwnica-Worms H. Inactivation of the p34cdc2-cyclin B complex by the human WEE1 tyrosine kinase. Science 1992;257(5078):1955-1957. PMID: 1384126. DOI: 10.1126/science.1384126.
- [petrosius-2023-wee1-phosphoproteomics] Petrosius V, Benada J, Nielsen O, Schoof EM, Sørensen CS. Temporal phosphoproteomics reveals WEE1-dependent control of 53BP1 pathway. iScience 2023;26(1):105806. PMID: 36632060. PMCID: PMC9827073. DOI: 10.1016/j.isci.2022.105806.
- [pfister-2015-wee1-h3k36me3] Pfister SX, Markkanen E, Jiang Y, et al. Inhibiting WEE1 Selectively Kills Histone H3K36me3-Deficient Cancers by dNTP Starvation. Cancer Cell 2015;28(5):557-568. PMID: 26602815. PMCID: PMC4643307. DOI: 10.1016/j.ccell.2015.09.015.
- [rothblum-oviatt-2001-1433-wee1] Rothblum-Oviatt CJ, Ryan CE, Piwnica-Worms H. 14-3-3 binding regulates catalytic activity of human Wee1 kinase. Cell Growth Differ 2001;12(12):581-589. PMID: 11751453.
- [russell-1987-wee1-mitosis] Russell P, Nurse P. Negative regulation of mitosis by wee1+, a gene encoding a protein kinase homolog. Cell 1987;49(4):559-567. PMID: 3032459. DOI: 10.1016/0092-8674(87)90458-2.
- [schmidt-2017-wee1-pkmyt1-review] Schmidt M, Rohe A, Platzer C, Najjar A, Erdmann F, Sippl W. Regulation of G2/M Transition by Inhibition of WEE1 and PKMYT1 Kinases. Molecules 2017;22(12):2045. PMID: 29168755. PMCID: PMC6149964. DOI: 10.3390/molecules22122045.
- [smith-2007-wee1-degradation] Smith A, Simanski S, Fallahi M, Ayad NG. Redundant ubiquitin ligase activities regulate wee1 degradation and mitotic entry. Cell Cycle 2007;6(22):2795-2799. PMID: 18032919. DOI: 10.4161/cc.6.22.4919.
- [sorensen-2012-atr-chk1-wee1-review] Sørensen CS, Syljuåsen RG. Safeguarding genome integrity: the checkpoint kinases ATR, CHK1 and WEE1 restrain CDK activity during normal DNA replication. Nucleic Acids Res 2012;40(2):477-486. PMID: 21937510. PMCID: PMC3258124. DOI: 10.1093/nar/gkr697.
- [squire-2005-wee1-structure] Squire CJ, Dickson JM, Ivanovic I, Baker EN. Structure and inhibition of the human cell cycle checkpoint kinase, Wee1A kinase: an atypical tyrosine kinase with a key role in CDK1 regulation. Structure 2005;13(4):541-550. PMID: 15837193. DOI: 10.1016/j.str.2004.12.017.
- [tominaga-2006-murine-wee1] Tominaga Y, Li C, Wang RH, Deng CX. Murine Wee1 plays a critical role in cell cycle regulation and pre-implantation stages of embryonic development. Int J Biol Sci 2006;2(4):161-170. PMID: 16810330. PMCID: PMC1483124. DOI: 10.7150/ijbs.2.161.
- [uniprot-2026-f6ty09-entry] UniProt Consortium. UniProtKB/TrEMBL entry F6TY09 (F6TY09_HORSE), Wee1-like protein kinase, *Equus caballus*; entry version 82 (02-Sep-2026). https://rest.uniprot.org/uniprotkb/F6TY09.txt
- [uniprot-2026-p30291-entry] UniProt Consortium. UniProtKB/Swiss-Prot entry P30291 (WEE1_HUMAN), Wee1-like protein kinase, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/P30291.txt
- [visconti-2012-fcp1-wee1] Visconti R, Palazzo L, Della Monica R, Grieco D. Fcp1-dependent dephosphorylation is required for M-phase-promoting factor inactivation at mitosis exit. Nat Commun 2012;3:894. PMID: 22692537. PMCID: PMC3621406. DOI: 10.1038/ncomms1886.
- [wade-2009-horse-genome] Wade CM, Giulotto E, Sigurdsson S, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. Science 2009;326(5954):865-867. PMID: 19892987. PMCID: PMC3785132. DOI: 10.1126/science.1178158.
- [watanabe-1995-wee1hu-regulation] Watanabe N, Broome M, Hunter T. Regulation of the human WEE1Hu CDK tyrosine 15-kinase during the cell cycle. EMBO J 1995;14(9):1878-1891. PMID: 7743995. PMCID: PMC398287. DOI: 10.1002/j.1460-2075.1995.tb07180.x.
- [watanabe-2004-scf-btrcp-wee1] Watanabe N, Arai H, Nishihara Y, Taniguchi M, Watanabe N, Hunter T, Osada H. M-phase kinases induce phospho-dependent ubiquitination of somatic Wee1 by SCFbeta-TrCP. Proc Natl Acad Sci USA 2004;101(13):4419-4424. PMID: 15070733. PMCID: PMC384762. DOI: 10.1073/pnas.0307700101.
- [watanabe-2005-cdk-destabilizes-wee1] Watanabe N, Arai H, Iwasaki J, Shiina M, Ogata K, Hunter T, Osada H. Cyclin-dependent kinase (CDK) phosphorylation destabilizes somatic Wee1 via multiple pathways. Proc Natl Acad Sci USA 2005;102(33):11663-11668. PMID: 16085715. PMCID: PMC1187955. DOI: 10.1073/pnas.0500410102.


## Citations

1. ayad-2003-tome1-abstract.md
2. ayad-2003-tome1-summary.md
3. baldin-1995-wee1-localisation-abstract.md
4. baldin-1995-wee1-localisation-summary.md
5. beck-2010-s-phase-cdk-abstract.md
6. beck-2010-s-phase-cdk-fulltext.txt
7. beck-2010-s-phase-cdk-summary.md
8. dominguez-kelly-2011-wee1-mus81-abstract.md
9. dominguez-kelly-2011-wee1-mus81-fulltext.txt
10. dominguez-kelly-2011-wee1-mus81-summary.md
11. ghelli-2020-wee1-family-review-abstract.md
12. ghelli-2020-wee1-family-review-fulltext.txt
13. ghelli-2020-wee1-family-review-summary.md
14. han-2005-wee1b-oocyte-abstract.md
15. han-2005-wee1b-oocyte-summary.md
16. hauge-2017-wee1-chk1-cdc45-abstract.md
17. hauge-2017-wee1-chk1-cdc45-fulltext.txt
18. hauge-2017-wee1-chk1-cdc45-summary.md
19. heald-1993-wee1-nucleus-abstract.md
20. heald-1993-wee1-nucleus-summary.md
21. hirai-2009-mk1775-abstract.md
22. hirai-2009-mk1775-summary.md
23. honda-1997-1433-mouse-wee1-abstract.md
24. honda-1997-1433-mouse-wee1-summary.md
25. igarashi-1991-human-wee1-abstract.md
26. igarashi-1991-human-wee1-summary.md
27. lee-2001-chk1-1433-wee1-abstract.md
28. lee-2001-chk1-1433-wee1-summary.md
29. li-2010-wee1-nuclear-export-abstract.md
30. li-2010-wee1-nuclear-export-summary.md
31. li-2020-fam122a-chk1-abstract.md
32. li-2020-fam122a-chk1-summary.md
33. lu-2004-sad-wee1-abstract.md
34. lu-2004-sad-wee1-summary.md
35. mahajan-2012-h2b-tyr37-abstract.md
36. mahajan-2012-h2b-tyr37-fulltext.txt
37. mahajan-2012-h2b-tyr37-summary.md
38. mcgowan-1993-wee1-tyr15-abstract.md
39. mcgowan-1993-wee1-tyr15-summary.md
40. mueller-1995-myt1-abstract.md
41. mueller-1995-myt1-summary.md
42. muller-2010-brsk-wee1-abstract.md
43. muller-2010-brsk-wee1-summary.md
44. oconnell-1997-chk1-wee1-abstract.md
45. oconnell-1997-chk1-wee1-summary.md
46. okamoto-2007-wee1-t239-abstract.md
47. okamoto-2007-wee1-t239-summary.md
48. parker-1992-wee1-cdc2-inactivation-abstract.md
49. parker-1992-wee1-cdc2-inactivation-summary.md
50. petrosius-2023-wee1-phosphoproteomics-abstract.md
51. petrosius-2023-wee1-phosphoproteomics-fulltext.txt
52. petrosius-2023-wee1-phosphoproteomics-summary.md
53. pfister-2015-wee1-h3k36me3-abstract.md
54. pfister-2015-wee1-h3k36me3-fulltext.txt
55. pfister-2015-wee1-h3k36me3-summary.md
56. rothblum-oviatt-2001-1433-wee1-abstract.md
57. rothblum-oviatt-2001-1433-wee1-summary.md
58. russell-1987-wee1-mitosis-abstract.md
59. russell-1987-wee1-mitosis-summary.md
60. schmidt-2017-wee1-pkmyt1-review-abstract.md
61. schmidt-2017-wee1-pkmyt1-review-fulltext.txt
62. schmidt-2017-wee1-pkmyt1-review-summary.md
63. smith-2007-wee1-degradation-abstract.md
64. smith-2007-wee1-degradation-summary.md
65. sorensen-2012-atr-chk1-wee1-review-abstract.md
66. sorensen-2012-atr-chk1-wee1-review-fulltext.txt
67. sorensen-2012-atr-chk1-wee1-review-summary.md
68. squire-2005-wee1-structure-abstract.md
69. squire-2005-wee1-structure-summary.md
70. tominaga-2006-murine-wee1-abstract.md
71. tominaga-2006-murine-wee1-fulltext.txt
72. tominaga-2006-murine-wee1-summary.md
73. uniprot-2026-f6ty09-entry.txt
74. uniprot-2026-p30291-entry.txt
75. visconti-2012-fcp1-wee1-abstract.md
76. visconti-2012-fcp1-wee1-fulltext.txt
77. visconti-2012-fcp1-wee1-summary.md
78. wade-2009-horse-genome-abstract.md
79. wade-2009-horse-genome-fulltext.txt
80. wade-2009-horse-genome-summary.md
81. watanabe-1995-wee1hu-regulation-abstract.md
82. watanabe-1995-wee1hu-regulation-summary.md
83. watanabe-2004-scf-btrcp-wee1-abstract.md
84. watanabe-2004-scf-btrcp-wee1-summary.md
85. watanabe-2005-cdk-destabilizes-wee1-abstract.md
86. watanabe-2005-cdk-destabilizes-wee1-summary.md