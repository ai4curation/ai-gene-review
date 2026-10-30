---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:05:39.595088'
end_time: '2026-10-25T23:16:55.881936'
duration_seconds: 676.29
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: APP
  gene_symbol: APP
  uniprot_accession: A0A9L0JJJ9
  protein_description: 'RecName: Full=Amyloid-beta A4 protein {ECO:0000256|RuleBase:RU367156};'
  gene_info: Name=APP {ECO:0000313|Ensembl:ENSEASP00005053379.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the APP family. {ECO:0000256|ARBA:ARBA00009449,
  protein_domains: Amyloid_Cu-bd_sf. (IPR036669); Amyloid_glyco. (IPR008155); Amyloid_glyco_Abeta.
    (IPR013803); Amyloid_glyco_Abeta_sf. (IPR037071); Amyloid_glyco_Cu-bd. (IPR011178)
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
citation_count: 76
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0JJJ9
- **Protein Description:** RecName: Full=Amyloid-beta A4 protein {ECO:0000256|RuleBase:RU367156};
- **Gene Information:** Name=APP {ECO:0000313|Ensembl:ENSEASP00005053379.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the APP family. {ECO:0000256|ARBA:ARBA00009449,
- **Key Domains:** Amyloid_Cu-bd_sf. (IPR036669); Amyloid_glyco. (IPR008155); Amyloid_glyco_Abeta. (IPR013803); Amyloid_glyco_Abeta_sf. (IPR037071); Amyloid_glyco_Cu-bd. (IPR011178)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "APP" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'APP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **APP** (gene ID: APP, UniProt: A0A9L0JJJ9) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# APP (Amyloid-beta A4 protein / amyloid-beta precursor protein) in the donkey, *Equus asinus* (UniProt A0A9L0JJJ9)

## 1. Introduction and summary

The donkey protein A0A9L0JJJ9 is an unreviewed UniProtKB/TrEMBL entry named "Amyloid-beta A4 protein", encoded by the gene *APP* (Ensembl ENSEASG00005008167, donkey chromosome 18) and predicted from the chromosome-level donkey reference genome; its protein existence level is "inferred from homology" and every functional annotation in the record is automatic [uniprot-A0A9L0JJJ9-entry][wang-2020-donkey-genome-abstract]. The gene symbol is not ambiguous here. The protein description, the APP family assignment and the InterPro domain set (amyloid glycoprotein E1 growth-factor-like and copper-binding subdomains, Kunitz/BPTI domain, E2 domain, Aβ region and conserved intracellular domain) all point to the amyloid-beta precursor protein, the type I transmembrane glycoprotein first cloned as the precursor of the Alzheimer's disease A4/Aβ peptide [uniprot-A0A9L0JJJ9-entry][kang-1987-app-cloning-abstract]. My own pairwise comparison of the 770-residue donkey sequence with human APP770 (P05067) shows 754 of 770 positions identical (97.9%), with no insertions or deletions. The whole C-terminal segment from residue 627 to 770, which contains the Aβ sequence, the transmembrane helix and the APP intracellular domain (AICD), is identical to human. This level of conservation means the experimental literature on human and mouse APP can be transferred to the donkey protein with high confidence. I found no donkey-specific molecular or cell-biological studies of APP. The only equid-specific work is neuropathological and biomarker-based [malbon-2022-donkey-alzheimer-pathology-abstract][capucchio-2010-equine-brain-abstract][gazzano-2025-horse-blood-abeta-abstract].

By homology, donkey APP is a cell-surface, single-pass type I membrane protein. Its primary role is that of a multifunctional receptor/adhesion molecule and a precursor for regulated intramembrane proteolysis. It has no enzymatic activity of its own. Instead it carries several ligand-binding and effector modules. The N-terminal growth-factor-like domain and the E2 domain bind heparin and heparan sulfate proteoglycans and promote neurite outgrowth [small-1994-heparin-neurite-abstract][rossjohn-1999-gfld-structure-abstract][wang-2004-e2-dimer-abstract]. The copper-binding domain binds and reduces Cu(II) [multhaup-1996-copper-reduction-abstract][barnham-2003-cubd-structure-abstract]. The Kunitz domain present in the 770/751 isoforms makes the shed ectodomain the serine-protease inhibitor protease nexin-II [kitaguchi-1988-kpi-abstract][oltersdorf-1989-protease-nexin-abstract][vannostrand-1989-protease-nexin-abstract]. The E1 and E2 domains mediate cis/trans dimerization that supports cell-cell and synaptic adhesion [soba-2005-dimerization-adhesion-abstract][wang-2009-synaptogenesis-abstract]. Ectodomain shedding by ADAM10 (α-secretase) or BACE1 (β-secretase), followed by presenilin-dependent γ-secretase cleavage, releases soluble sAPP, the Aβ peptide and the AICD [esch-1990-alpha-secretase-abstract][kuhn-2010-adam10-abstract][vassar-1999-bace-abstract][destrooper-1998-presenilin-abstract][haass-2012-app-processing-abstract]. These fragments have signalling roles of their own. Secreted sAPP is a presynaptic ligand of the GABA_B receptor subunit 1a [rice-2019-gabab-ligand-fulltext], and the cytoplasmic YENPTY motif docks the PTB-domain adaptors Fe65 and X11/Mint1 [fiore-1995-fe65-ptb-abstract][borg-1996-x11-fe65-yenpty-abstract]. The AICD also assembles a transcriptionally active complex with Fe65 and Tip60 [cao-2001-aicd-fe65-abstract]. In vivo, most of the physiological functions of APP that knockout mice reveal (body and brain weight, grip strength, locomotion, spatial learning, LTP) can be supplied by the secreted ectodomain alone [zheng-1995-app-knockout-abstract][ring-2007-sappalpha-rescue-abstract][muller-2017-app-physiology-abstract]. In donkeys specifically, amyloid plaques and neurofibrillary-tangle-like lesions occur in aged animals, which shows that the endogenous protein is processed amyloidogenically in this species [malbon-2022-donkey-alzheimer-pathology-abstract].

## 2. Identity, gene model and evolutionary conservation

The A0A9L0JJJ9 sequence comes from the Ensembl annotation of the donkey genome (proteome UP000694387). That genome is a de novo chromosome-level assembly of a male Dezhou donkey, published together with resequencing data from 126 domestic donkeys and seven wild asses [wang-2020-donkey-genome-abstract][uniprot-A0A9L0JJJ9-entry]. The genome paper is about domestication and coat colour and does not discuss *APP* [wang-2020-donkey-genome-fulltext]. The predicted protein has a signal peptide (1–17), a mature chain of 18–770, a single helical transmembrane segment (701–723), an E1 domain (28–189) subdivided into the growth-factor-like domain (GFLD, 28–123) and copper-binding domain (CuBD, 131–189), an acidic, disordered region (about 194–284), a BPTI/Kunitz inhibitor domain (291–341), an E2 domain (374–565) and a short cytoplasmic tail [uniprot-A0A9L0JJJ9-entry]. Disulfide bonds are propagated from the PROSITE rules for the E1 and Kunitz domains [uniprot-A0A9L0JJJ9-entry]. At 770 residues and with a Kunitz domain, the donkey model corresponds to the human APP770 isoform. In humans that isoform is one of three major splice products (APP695, APP751 and APP770), and the two longer forms contain the Kunitz-type insert [oltersdorf-1989-protease-nexin-abstract][kitaguchi-1988-kpi-abstract]. A0A9L0JJJ9 is not the only donkey APP product. UniProt lists six unreviewed donkey *APP* entries, all from separate Ensembl transcripts on chromosome 18 of the same reference proteome: A0A9L0JJJ9 (770 residues), A0A8C4LMJ3 (752), A0A8C4LJG7 (751), A0A8C4LI26 (714), A0A9L0KAH7 (708) and A0A8C4LGI7 (695) [uniprot-donkey-APP-entries-search]. I checked these sequences myself. All six share the same N-terminus and contain an Aβ1–42 sequence identical to human. Only the 695-residue model lacks the Kunitz domain, so it corresponds to the neuronal APP695 isoform, while the 751- and 770-residue models correspond to the KPI-containing APP751 and APP770. This means the donkey gene annotation reproduces the splice architecture of human *APP*, in which exons 7 and 8 (the Kunitz domain and the adjacent segment) are spliced alternatively [rohandesilva-1997-isoform-cells]. A0A9L0JJJ9 is the longest, full-length isoform.

My alignment of the donkey and human sequences (no gaps required) puts the 16 substitutions in a few places. One is in the signal peptide (L8V). Six are in the GFLD (R40K, N49T, D53E, D64G, P109A, F111I). Three are conservative acidic-residue swaps in the acidic region (E233D, E236D, D243E). Four lie in the linker just after the Kunitz domain (A344V, T353P, A358P, R359Q), and two in the juxtamembrane stretch preceding Aβ (S623P, A626V). The functionally defined motifs are all preserved. The heparin-binding loop retains K99, R100 and R102, which mutagenesis showed are needed for heparin binding of human APP [small-1994-heparin-neurite-abstract][uniprot-P05067-entry]. The copper-coordinating residues identified in the human CuBD structure (H147, H151, Y168) are conserved [barnham-2003-cubd-structure-abstract][uniprot-P05067-entry]. The 17-residue GABA_B R1a-binding peptide of the extension domain (DDSDVWWGGADTDYADG, positions 204–220) is identical to human, including the V208/W209 pair that contacts the receptor's sushi-1 pocket in the NMR model [rice-2019-gabab-ligand-fulltext]. Rice and colleagues numbered these residues on APP695, but because they lie N-terminal to the alternatively spliced Kunitz insert the numbering also holds for APP770. The Aβ1–42 sequence (DAEFRHDSGYEVHHQKLVFFAEDVGSNKGAIIGLMVGGVVIA, residues 672–713) is identical to human. Unlike rodent Aβ, it keeps R5, Y10 and H13. The β-site flank (K670-M671-D672-A673) is also human-like, including A673, the residue at which the protective Icelandic A673T variant reduces β-cleavage [jonsson-2012-a673t-abstract]. The C-terminal internalization and adaptor-binding motif YENPTY (757–762) is conserved [ring-2007-sappalpha-rescue-abstract][borg-1996-x11-fe65-yenpty-abstract]. These observations fit an older cross-species survey. Johnstone and colleagues found that the Aβ sequence is conserved in dog, polar bear and other mammals that form plaques, whereas mouse and rat Aβ differ and are predicted to have lower β-sheet propensity [johnstone-1991-abeta-conservation-abstract]. Donkey Aβ belongs to the conserved, human-like group. Taken together, the sequence evidence supports strict functional orthology with human APP.

## 3. Domain architecture and molecular functions of the ectodomain

The founding description of APP noted that the 695-residue precursor has the features of a glycosylated cell-surface receptor [kang-1987-app-cloning-abstract], and the domain structures solved since then account for most of its ligand-binding repertoire. The N-terminal GFLD (human residues 28–123) has a 1.8 Å crystal structure. It shows a highly basic surface suited to glycosaminoglycan binding next to a hydrophobic surface proposed to mediate dimerization or ligand binding, and the fold resembles cysteine-rich growth factors [rossjohn-1999-gfld-structure-abstract]. Functionally, substratum-bound APP stimulates neurite outgrowth of sympathetic and hippocampal neurons as effectively as laminin. This requires heparan sulfate proteoglycans and depends on the 96–110 heparin-binding region [small-1994-heparin-neurite-abstract]. All three critical basic residues are conserved in the donkey protein (Section 2).

The adjacent CuBD binds copper. Human APP, or a peptide spanning its copper-binding site, reduces bound Cu(II) to Cu(I) in a reaction coupled to disulfide-bond formation in APP [multhaup-1996-copper-reduction-abstract]. The NMR structure of the CuBD revealed a surface-exposed site that favours Cu(I) and a fold resembling copper chaperones [barnham-2003-cubd-structure-abstract]. Genetic data support a role in metal homeostasis: APP-knockout mice have raised cortical copper and APP-overexpressing mice have less, and copper binding to APP lowers Aβ production in vitro [barnham-2003-cubd-structure-abstract]. On this basis the CuBD has been proposed to act as a neuronal metallotransporter [barnham-2003-cubd-structure-abstract]. The donkey record's "transition metal ion binding" (GO:0046914) and copper/zinc keywords come from this conserved module [uniprot-A0A9L0JJJ9-entry].

The KPI-containing isoforms, which the 770-residue donkey model represents, carry a 56–57-residue Kunitz-type serine-protease inhibitor domain encoded by alternatively spliced exons [kitaguchi-1988-kpi-abstract][oltersdorf-1989-protease-nexin-abstract]. The secreted ectodomain of APP751 is identical to protease nexin-II (PN-II). It forms stable inhibitory complexes with trypsin, which secreted APP695 does not [oltersdorf-1989-protease-nexin-abstract]. PN-II inhibits chymotrypsin with a Ki of about 6 × 10⁻¹⁰ M and forms SDS-resistant complexes with EGF-binding protein and the γ-subunit of NGF [vannostrand-1989-protease-nexin-abstract]. For the donkey protein, then, the annotation "serine-type endopeptidase inhibitor activity" is well supported by homology. That activity belongs to the shed, extracellular ectodomain [oltersdorf-1989-protease-nexin-abstract][vannostrand-1989-protease-nexin-abstract].

The E2 domain is the largest conserved ectodomain module. It has two coiled-coil substructures joined by a continuous helix in a spectrin-like arrangement. It dimerizes reversibly in an antiparallel orientation and binds heparan sulfate at a conserved basic site near the dimer interface [wang-2004-e2-dimer-abstract]. Between E1 and E2 lies the flexible acidic region and extension domain. Rice and colleagues found that this linker, and not the GFLD, CuBD or E2, binds the sushi-1 domain of GABA_B R1a [rice-2019-gabab-ligand-fulltext]. A conserved 17-residue peptide bound with a KD of 810 nM and a 9-residue core with a KD of 2.3 µM. Binding also stabilized the otherwise unstructured sushi-1 domain [rice-2019-gabab-ligand-fulltext].

## 4. Proteolytic processing, trafficking and subcellular localization

APP matures through the secretory pathway and reaches the sites where its processing enzymes, the secretases, are most active [haass-2012-app-processing-abstract]. In the non-amyloidogenic route, constitutive α-secretase cleavage inside the Aβ sequence releases the ectodomain and rules out Aβ formation [esch-1990-alpha-secretase-abstract]. Knockdown of ADAM10, but not ADAM9 or ADAM17, abolished α-cleavage in cell lines and primary neurons, and ADAM10 can also cut the β-secretase-derived C-terminal fragment. ADAM10 is therefore the physiological constitutive α-secretase [kuhn-2010-adam10-abstract]. In the amyloidogenic route, the transmembrane aspartic protease BACE (BACE1) cleaves at the β-site [vassar-1999-bace-abstract]. γ-Secretase then cuts within the membrane, and this step depends on presenilin-1: PS1-deficient neurons accumulate APP C-terminal fragments and make about five-fold less Aβ, while α- and β-cleavage are unchanged [destrooper-1998-presenilin-abstract]. β- and γ-secretase thus act in sequence to liberate Aβ, whereas α-secretase precludes it [haass-2012-app-processing-abstract]. Every cleavage-site region (β-site, α-site within Aβ, transmembrane γ-sites) is identical between donkey and human (Section 2), so donkey APP should be a substrate for all three secretase activities.

The cytoplasmic YENPTY motif regulates trafficking. In knock-in mice lacking the last 15 residues (APPΔCT15), holo-APP turned over more slowly, surface APP increased and brain Aβ fell sharply. The authors attributed this to reduced processing in the endocytic pathway [ring-2007-sappalpha-rescue-abstract]. These data fit the localizations transferred to the donkey record by automatic annotation: plasma membrane and cell surface, clathrin-coated pits, early endosomes, Golgi apparatus, endoplasmic reticulum, growth cones, perikaryon and secreted [uniprot-A0A9L0JJJ9-entry]. Holo-APP therefore works at the cell surface and in the secretory/endocytic membrane system. Its shed ectodomain (sAPP, including the PN-II form) works in the extracellular space, and the AICD can signal towards the nucleus (Section 5). APP is also abundant at presynaptic terminals of both excitatory and inhibitory hippocampal synapses [rice-2019-gabab-ligand-fulltext]. Which isoform is present depends on cell type, and that matters for the KPI-containing A0A9L0JJJ9 product. In human tissues the brain has the highest APP expression and is rich in APP695. The APP770:APP751:APP695 mRNA ratio in control cortex is about 1:10:20, so APP770 is a minor brain isoform [tanaka-1989-isoform-tissue-abstract]. In rat, APP695 predominates in cultured neurons. KPI-containing APP770 and APP751 predominate in astrocytes, which hold about three-fold more KPI-APP protein, and KPI-APP is found in reactive astrocytes after hippocampal lesion [rohandesilva-1997-isoform-cells-abstract]. By analogy, the 770-residue donkey isoform is expected to be mainly a glial and non-neural product whose shed ectodomain can act as protease nexin-II. The KPI-lacking 695-residue model (A0A8C4LGI7) is expected to be the main neuronal and synaptic form. This expression pattern is inferred and has not been measured in donkeys.

## 5. Signalling roles of APP and its fragments

Several APP-derived products are signalling molecules with defined partners. The best characterized extracellular pathway is the action of sAPP on presynaptic GABA_B receptors. sAPP binds the sushi-1 domain found only in the GABA_B R1a isoform. Acute sAPPα lowered the frequency, but not the amplitude, of miniature excitatory and inhibitory postsynaptic currents in hippocampal neurons, reduced synaptic vesicle release and enhanced short-term facilitation at Schaffer-collateral synapses [rice-2019-gabab-ligand-fulltext]. The 17-residue APP peptide suppressed spontaneous hippocampal activity in vivo [rice-2019-gabab-ligand-fulltext]. This pathway gives sAPP a defined role as a ligand that tunes presynaptic release through GABA_B R1a. It also offers a mechanism for the long-standing observation that the physiological synaptic functions of APP are carried by its secreted form [rice-2019-gabab-ligand-fulltext][muller-2017-app-physiology-abstract]. The binding peptide is identical in the donkey sequence.

In the intracellular direction, the short cytoplasmic domain is a docking site for phosphotyrosine-binding (PTB/PID) domain adaptors. A yeast two-hybrid screen with the PTB-domain region of Fe65 recovered the APP C-terminus, and the binding site centred on the NPTY sequence [fiore-1995-fe65-ptb-abstract]. Borg and colleagues then showed that the PTB domains of both X11 (Mint1) and Fe65 bind the YENPTY motif. Unlike Shc binding to growth-factor receptors, this binding does not need tyrosine phosphorylation, and mutations within YENPTY affect X11 and Fe65 binding differently, which points to distinct binding modes [borg-1996-x11-fe65-yenpty-abstract]. Once γ-secretase cleavage releases the cytoplasmic tail, it forms a multimeric complex with the adaptor Fe65 and the histone acetyltransferase Tip60, which strongly activates transcription when tethered to heterologous DNA-binding domains. This finding suggested a gene-regulatory role for the AICD [cao-2001-aicd-fe65-abstract]. A trans-synaptic adhesion pathway also exists. In mixed-culture assays, APP on non-neuronal cells induced presynaptic differentiation in contacting axons. This activity required neuronal APP and both the extracellular and intracellular domains, and the intracellular domain complexed with Mint1 and CASK [wang-2009-synaptogenesis-abstract]. The donkey record's automatic annotations of APP as a cell-surface receptor and as an enhancer of neuronal apoptosis via γ-CTF/C31 fragments come from human-centred rules [uniprot-A0A9L0JJJ9-entry]. Of these, the apoptosis claim had no primary support among the sources examined here, and it should be treated as lower confidence.

## 6. Adhesion, synapse formation and in vivo physiology

APP and its paralogues APLP1 and APLP2 form homo- and heterocomplexes. Their trans-interaction promotes cell-cell adhesion, and the complexes are found together in synaptically enriched membranes in brain [soba-2005-dimerization-adhesion-abstract]. Structural data showing dimerization through the GFLD hydrophobic surface and the antiparallel E2 dimer [rossjohn-1999-gfld-structure-abstract][wang-2004-e2-dimer-abstract] supply a molecular basis for this adhesion. Genetic dissection at the neuromuscular junction showed that removing APP from either the presynaptic motor neuron or the postsynaptic muscle (on an APLP2-null background) disrupted synapses. Postsynaptic APP was required for presynaptic targeting of the high-affinity choline transporter and for synaptic transmission, which identifies APP as a synaptic adhesion molecule [wang-2009-synaptogenesis-abstract].

Whole-animal loss of function in mice gives a mild but informative phenotype. APP-null mice are viable and fertile but 15–20% lighter, with reduced locomotor activity and grip strength and reactive gliosis [zheng-1995-app-knockout-abstract]. Mice that express only sAPPα from the endogenous locus largely or completely rescue these defects, as well as the impairments in spatial learning and hippocampal LTP. So the secreted ectodomain carries most of the APP functions measured in these assays, and the C-terminus is dispensable for them [ring-2007-sappalpha-rescue-abstract]. The wider knockout literature, reviewed by Müller, Deller and Korte, assigns the APP family roles in CNS development, synapse formation and function, neuroprotection after injury, and ageing. It also shows substantial functional redundancy with the APLPs [muller-2017-app-physiology-abstract]. Combined knockouts make this redundancy explicit. APP/APLP2 and APLP1/APLP2 double-knockout mice die early after birth, whereas APP/APLP1 double knockouts are viable and look normal. APLP1/APP-null mice that lack even one APLP2 allele are also lethal [heber-2000-app-family-knockouts-abstract]. APP's essential functions are therefore shared with APLP2, which explains the mildness of the single APP knockout. The different outcomes of the double mutants also show that APP has functions distinct from APLP2 [heber-2000-app-family-knockouts-abstract]. Because UniProt classifies the donkey protein in the APP family alongside these paralogues [uniprot-A0A9L0JJJ9-entry], any loss-of-function variant in equids would likewise be expected to be buffered by APLP2. No equivalent genetic work exists for equids, and these conclusions apply to donkey APP only by orthology.

## 7. Amyloidogenic processing and neuropathology in equids

In humans, the clinical relevance of APP processing is shown by coding variants that change β-cleavage. The A673T substitution next to the β-site lowers amyloidogenic peptide production by about 40% in vitro and protects against both Alzheimer's disease and age-related cognitive decline [jonsson-2012-a673t-abstract]. Donkey APP carries the ancestral A673 and an Aβ sequence identical to human (Section 2). This makes the species a plausible natural host for human-like Aβ aggregation. Neuropathology supports this. Among 13 donkeys over 30 years old, amyloid plaques were found in the parietal cortex of nine, preferentially in deep sulci, and neurofibrillary-tangle-like structures in seven. Neither lesion appeared in two younger controls, and this was reported as the first finding of both plaques and tangles in an equid [malbon-2022-donkey-alzheimer-pathology-abstract]. The authors relate this to the donkey's exceptional longevity and its predisposition to human-like abnormalities of insulin metabolism [malbon-2022-donkey-alzheimer-pathology-abstract]. In horses (*Equus caballus*) aged 7–23 years, methenamine-positive diffuse "preamyloid" plaques and tau-positive hippocampal neurons were seen, but Congo red did not detect fibrillar amyloid [capucchio-2010-equine-brain-abstract]. A pilot serum study in 23 Arabian horses, using commercial horse-specific ELISAs, measured Aβ40 at 67–744 pg/mL and found no detectable Aβ42 and no correlation with age [gazzano-2025-horse-blood-abeta-abstract][gazzano-2025-horse-blood-abeta-fulltext]. Aβ itself may also have a physiological job. In hippocampal slices, neuronal activity increases Aβ formation and secretion, and Aβ in turn depresses excitatory synaptic transmission in an NMDA-receptor-dependent manner. Kamenetz and colleagues proposed that this negative feedback loop normally limits neuronal hyperactivity [kamenetz-2003-activity-abeta-abstract]. The equid data therefore show that APP is processed through the β/γ-secretase route in vivo and that Aβ can deposit in very old animals. The molecular species, their abundance and their relationship to clinical decline are still poorly characterized.

## 8. Open Questions

The main gap is that no experiment has been done on donkey APP itself. All molecular functions in this report are inferred from a protein that is 97.9% identical to human APP770, so direct biochemical confirmation in equid cells or tissues would be needed to move these annotations beyond inference. First, the donkey gene annotation predicts 695-, 751- and 770-residue isoforms analogous to the human ones [uniprot-donkey-APP-entries-search], but these are computational models. Nobody has shown that they are expressed, or that donkey neurons and glia split them the way rodent cells do [rohandesilva-1997-isoform-cells-abstract]. Isoform-resolved long-read RNA-seq or quantitative RT-PCR of donkey brain regions and peripheral tissues would settle this. It also bears on how much of the protein acts as the protease inhibitor PN-II, and on whether KPI-isoform expression rises with age, as reported in human Alzheimer's disease brain [tanaka-1989-isoform-tissue-abstract]. Second, six of the 16 substitutions cluster in the heparin-binding GFLD (including P109A and F111I right next to the 96–110 heparin-binding loop). Whether these change glycosaminoglycan affinity, dimerization or neurite-promoting activity could be tested with recombinant donkey GFLD in binding and neurite-outgrowth assays. Third, two substitutions (S623P, A626V) lie in the juxtamembrane stretch shortly before the Aβ sequence. Their effect on ADAM10 and BACE1 accessibility, and hence on the Aβ/sAPPα ratio, is unknown. Cell-based processing assays comparing donkey and human APP would show whether equid APP is intrinsically more or less amyloidogenic.

At the organismal level, the plaques and tangle-like lesions in aged donkeys need biochemical characterization. Open points are the Aβ40/Aβ42 ratio, N-terminal truncation and pyroglutamate modification, whether the tangle-like structures contain hyperphosphorylated tau as in human disease, and whether the lesions correlate with the insulin dysregulation to which donkeys are predisposed [malbon-2022-donkey-alzheimer-pathology-abstract]. The horse serum data rest on commercial ELISAs without published validation against equine Aβ standards, and Aβ42 was undetectable, so a validated mass-spectrometric method for equid plasma and CSF Aβ is needed before blood biomarkers can be interpreted [gazzano-2025-horse-blood-abeta-fulltext]. Finally, it is unclear whether the sAPP–GABA_B R1a pathway, the YENPTY-dependent Fe65/X11 adaptor interactions and the AICD–Fe65 transcriptional complex and the copper-homeostasis role of the CuBD work in equids as in rodents. Because the relevant motifs are conserved, these are reasonable predictions, but they are unverified. It would also be worth reconciling the automatic GO annotations on A0A9L0JJJ9, many of them inflammatory and immune processes propagated from Ensembl, with the core functions supported by primary data. Several of those terms describe downstream effects of Aβ rather than activities of the APP protein itself [uniprot-A0A9L0JJJ9-entry].

## 9. References

- **barnham-2003-cubd-structure**: Barnham KJ, McKinstry WJ, Multhaup G et al. (2003). Structure of the Alzheimer's disease amyloid precursor protein copper binding domain. A regulator of neuronal copper homeostasis. *The Journal of biological chemistry* 278(19):17401-7. PMID: 12611883; DOI: 10.1074/jbc.M300629200. https://pubmed.ncbi.nlm.nih.gov/12611883/
- **borg-1996-x11-fe65-yenpty**: Borg JP, Ooi J, Levy E et al. (1996). The phosphotyrosine interaction domains of X11 and FE65 bind to distinct sites on the YENPTY motif of amyloid precursor protein. *Molecular and cellular biology* 16(11):6229-41. PMID: 8887653; DOI: 10.1128/MCB.16.11.6229; PMCID: PMC231626. https://pubmed.ncbi.nlm.nih.gov/8887653/
- **cao-2001-aicd-fe65**: Cao X, Südhof TC (2001). A transcriptionally [correction of transcriptively] active complex of APP with Fe65 and histone acetyltransferase Tip60. *Science (New York, N.Y.)* 293(5527):115-20. PMID: 11441186; DOI: 10.1126/science.1058783. https://pubmed.ncbi.nlm.nih.gov/11441186/
- **capucchio-2010-equine-brain**: Capucchio MT, Márquez M, Pregel P et al. (2010). Parenchymal and vascular lesions in ageing equine brains: histological and immunohistochemical studies. *Journal of comparative pathology* 142(1):61-73. PMID: 19744668; DOI: 10.1016/j.jcpa.2009.07.007. https://pubmed.ncbi.nlm.nih.gov/19744668/
- **destrooper-1998-presenilin**: De Strooper B, Saftig P, Craessaerts K et al. (1998). Deficiency of presenilin-1 inhibits the normal cleavage of amyloid precursor protein. *Nature* 391(6665):387-90. PMID: 9450754; DOI: 10.1038/34910. https://pubmed.ncbi.nlm.nih.gov/9450754/
- **esch-1990-alpha-secretase**: Esch FS, Keim PS, Beattie EC et al. (1990). Cleavage of amyloid beta peptide during constitutive processing of its precursor. *Science (New York, N.Y.)* 248(4959):1122-4. PMID: 2111583; DOI: 10.1126/science.2111583. https://pubmed.ncbi.nlm.nih.gov/2111583/
- **fiore-1995-fe65-ptb**: Fiore F, Zambrano N, Minopoli G et al. (1995). The regions of the Fe65 protein homologous to the phosphotyrosine interaction/phosphotyrosine binding domain of Shc bind the intracellular domain of the Alzheimer's amyloid precursor protein. *The Journal of biological chemistry* 270(52):30853-6. PMID: 8537337; DOI: 10.1074/jbc.270.52.30853. https://pubmed.ncbi.nlm.nih.gov/8537337/
- **gazzano-2025-horse-blood-abeta**: Gazzano V, Curadi MC, Capsoni S et al. (2025). A Pilot Study on Blood Concentration of β-Amyloid (40 and 42) and Phospho-Tau 181 in Horses. *Veterinary sciences* 12(7):None. PMID: 40711270; DOI: 10.3390/vetsci12070610; PMCID: PMC12300970. https://pubmed.ncbi.nlm.nih.gov/40711270/
- **haass-2012-app-processing**: Haass C, Kaether C, Thinakaran G et al. (2012). Trafficking and proteolytic processing of APP. *Cold Spring Harbor perspectives in medicine* 2(5):a006270. PMID: 22553493; DOI: 10.1101/cshperspect.a006270; PMCID: PMC3331683. https://pubmed.ncbi.nlm.nih.gov/22553493/
- **heber-2000-app-family-knockouts**: Heber S, Herms J, Gajic V et al. (2000). Mice with combined gene knock-outs reveal essential and partially redundant functions of amyloid precursor protein family members. *The Journal of neuroscience : the official journal of the Society for Neuroscience* 20(21):7951-63. PMID: 11050115; DOI: 10.1523/JNEUROSCI.20-21-07951.2000; PMCID: PMC6772747. https://pubmed.ncbi.nlm.nih.gov/11050115/
- **johnstone-1991-abeta-conservation**: Johnstone EM, Chaney MO, Norris FH et al. (1991). Conservation of the sequence of the Alzheimer's disease amyloid peptide in dog, polar bear and five other mammals by cross-species polymerase chain reaction analysis. *Brain research. Molecular brain research* 10(4):299-305. PMID: 1656157; DOI: 10.1016/0169-328x(91)90088-f. https://pubmed.ncbi.nlm.nih.gov/1656157/
- **jonsson-2012-a673t**: Jonsson T, Atwal JK, Steinberg S et al. (2012). A mutation in APP protects against Alzheimer's disease and age-related cognitive decline. *Nature* 488(7409):96-9. PMID: 22801501; DOI: 10.1038/nature11283. https://pubmed.ncbi.nlm.nih.gov/22801501/
- **kamenetz-2003-activity-abeta**: Kamenetz F, Tomita T, Hsieh H et al. (2003). APP processing and synaptic function. *Neuron* 37(6):925-37. PMID: 12670422; DOI: 10.1016/s0896-6273(03)00124-7. https://pubmed.ncbi.nlm.nih.gov/12670422/
- **kang-1987-app-cloning**: Kang J, Lemaire HG, Unterbeck A et al. (1987). The precursor of Alzheimer's disease amyloid A4 protein resembles a cell-surface receptor. *Nature* 325(6106):733-6. PMID: 2881207; DOI: 10.1038/325733a0. https://pubmed.ncbi.nlm.nih.gov/2881207/
- **kitaguchi-1988-kpi**: Kitaguchi N, Takahashi Y, Tokushima Y et al. (1988). Novel precursor of Alzheimer's disease amyloid protein shows protease inhibitory activity. *Nature* 331(6156):530-2. PMID: 2893291; DOI: 10.1038/331530a0. https://pubmed.ncbi.nlm.nih.gov/2893291/
- **kuhn-2010-adam10**: Kuhn PH, Wang H, Dislich B et al. (2010). ADAM10 is the physiologically relevant, constitutive alpha-secretase of the amyloid precursor protein in primary neurons. *The EMBO journal* 29(17):3020-32. PMID: 20676056; DOI: 10.1038/emboj.2010.167; PMCID: PMC2944055. https://pubmed.ncbi.nlm.nih.gov/20676056/
- **malbon-2022-donkey-alzheimer-pathology**: Malbon AJ, Sordo L, Wilson LA et al. (2022). Alzheimer-like pathology in the parietal cortex and hippocampus of aged donkeys. *Neurobiology of aging* 113:7-14. PMID: 35278749; DOI: 10.1016/j.neurobiolaging.2022.01.007. https://pubmed.ncbi.nlm.nih.gov/35278749/
- **muller-2017-app-physiology**: Müller UC, Deller T, Korte M (2017). Not just amyloid: physiological functions of the amyloid precursor protein family. *Nature reviews. Neuroscience* 18(5):281-298. PMID: 28360418; DOI: 10.1038/nrn.2017.29. https://pubmed.ncbi.nlm.nih.gov/28360418/
- **multhaup-1996-copper-reduction**: Multhaup G, Schlicksupp A, Hesse L et al. (1996). The amyloid precursor protein of Alzheimer's disease in the reduction of copper(II) to copper(I). *Science (New York, N.Y.)* 271(5254):1406-9. PMID: 8596911; DOI: 10.1126/science.271.5254.1406. https://pubmed.ncbi.nlm.nih.gov/8596911/
- **oltersdorf-1989-protease-nexin**: Oltersdorf T, Fritz LC, Schenk DB et al. (1989). The secreted form of the Alzheimer's amyloid precursor protein with the Kunitz domain is protease nexin-II. *Nature* 341(6238):144-7. PMID: 2506449; DOI: 10.1038/341144a0. https://pubmed.ncbi.nlm.nih.gov/2506449/
- **rice-2019-gabab-ligand**: Rice HC, de Malmazet D, Schreurs A et al. (2019). Secreted amyloid-β precursor protein functions as a GABABR1a ligand to modulate synaptic transmission. *Science (New York, N.Y.)* 363(6423):None. PMID: 30630900; DOI: 10.1126/science.aao4827; PMCID: PMC6366617. https://pubmed.ncbi.nlm.nih.gov/30630900/
- **ring-2007-sappalpha-rescue**: Ring S, Weyer SW, Kilian SB et al. (2007). The secreted beta-amyloid precursor protein ectodomain APPs alpha is sufficient to rescue the anatomical, behavioral, and electrophysiological abnormalities of APP-deficient mice. *The Journal of neuroscience : the official journal of the Society for Neuroscience* 27(29):7817-26. PMID: 17634375; DOI: 10.1523/JNEUROSCI.1026-07.2007; PMCID: PMC6672885. https://pubmed.ncbi.nlm.nih.gov/17634375/
- **rohandesilva-1997-isoform-cells**: Rohan de Silva HA, Jen A, Wickenden C et al. (1997). Cell-specific expression of beta-amyloid precursor protein isoform mRNAs and proteins in neurons and astrocytes. *Brain research. Molecular brain research* 47(1-2):147-56. PMID: 9221912; DOI: 10.1016/s0169-328x(97)00045-4. https://pubmed.ncbi.nlm.nih.gov/9221912/
- **rossjohn-1999-gfld-structure**: Rossjohn J, Cappai R, Feil SC et al. (1999). Crystal structure of the N-terminal, growth factor-like domain of Alzheimer amyloid precursor protein. *Nature structural biology* 6(4):327-31. PMID: 10201399; DOI: 10.1038/7562. https://pubmed.ncbi.nlm.nih.gov/10201399/
- **small-1994-heparin-neurite**: Small DH, Nurcombe V, Reed G et al. (1994). A heparin-binding domain in the amyloid protein precursor of Alzheimer's disease is involved in the regulation of neurite outgrowth. *The Journal of neuroscience : the official journal of the Society for Neuroscience* 14(4):2117-27. PMID: 8158260; DOI: 10.1523/JNEUROSCI.14-04-02117.1994; PMCID: PMC6577125. https://pubmed.ncbi.nlm.nih.gov/8158260/
- **soba-2005-dimerization-adhesion**: Soba P, Eggert S, Wagner K et al. (2005). Homo- and heterodimerization of APP family members promotes intercellular adhesion. *The EMBO journal* 24(20):3624-34. PMID: 16193067; DOI: 10.1038/sj.emboj.7600824; PMCID: PMC1276707. https://pubmed.ncbi.nlm.nih.gov/16193067/
- **tanaka-1989-isoform-tissue**: Tanaka S, Shiojiri S, Takahashi Y et al. (1989). Tissue-specific expression of three types of beta-protein precursor mRNA: enhancement of protease inhibitor-harboring types in Alzheimer's disease brain. *Biochemical and biophysical research communications* 165(3):1406-14. PMID: 2514687; DOI: 10.1016/0006-291x(89)92760-5. https://pubmed.ncbi.nlm.nih.gov/2514687/
- **vannostrand-1989-protease-nexin**: Van Nostrand WE, Wagner SL, Suzuki M et al. (1989). Protease nexin-II, a potent antichymotrypsin, shows identity to amyloid beta-protein precursor. *Nature* 341(6242):546-9. PMID: 2507928; DOI: 10.1038/341546a0. https://pubmed.ncbi.nlm.nih.gov/2507928/
- **vassar-1999-bace**: Vassar R, Bennett BD, Babu-Khan S et al. (1999). Beta-secretase cleavage of Alzheimer's amyloid precursor protein by the transmembrane aspartic protease BACE. *Science (New York, N.Y.)* 286(5440):735-41. PMID: 10531052; DOI: 10.1126/science.286.5440.735. https://pubmed.ncbi.nlm.nih.gov/10531052/
- **wang-2004-e2-dimer**: Wang Y, Ha Y (2004). The X-ray structure of an antiparallel dimer of the human amyloid precursor protein E2 domain. *Molecular cell* 15(3):343-53. PMID: 15304215; DOI: 10.1016/j.molcel.2004.06.037. https://pubmed.ncbi.nlm.nih.gov/15304215/
- **wang-2009-synaptogenesis**: Wang Z, Wang B, Yang L et al. (2009). Presynaptic and postsynaptic interaction of the amyloid precursor protein promotes peripheral and central synaptogenesis. *The Journal of neuroscience : the official journal of the Society for Neuroscience* 29(35):10788-801. PMID: 19726636; DOI: 10.1523/JNEUROSCI.2132-09.2009; PMCID: PMC2757256. https://pubmed.ncbi.nlm.nih.gov/19726636/
- **wang-2020-donkey-genome**: Wang C, Li H, Guo Y et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nature communications* 11(1):6014. PMID: 33293529; DOI: 10.1038/s41467-020-19813-7; PMCID: PMC7723042. https://pubmed.ncbi.nlm.nih.gov/33293529/
- **zheng-1995-app-knockout**: Zheng H, Jiang M, Trumbauer ME et al. (1995). beta-Amyloid precursor protein-deficient mice show reactive gliosis and decreased locomotor activity. *Cell* 81(4):525-31. PMID: 7758106; DOI: 10.1016/0092-8674(95)90073-x. https://pubmed.ncbi.nlm.nih.gov/7758106/
- **uniprot-A0A9L0JJJ9-entry**: UniProt Consortium. UniProtKB/TrEMBL entry A0A9L0JJJ9_EQUAS, "Amyloid-beta A4 protein", *Equus asinus* (entry version 15, 02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0JJJ9.txt
- **uniprot-donkey-APP-entries-search**: UniProt Consortium. UniProtKB search results for gene APP in *Equus asinus* (taxon 9793), listing entries A0A9L0JJJ9, A0A8C4LMJ3, A0A8C4LJG7, A0A8C4LI26, A0A9L0KAH7 and A0A8C4LGI7. https://rest.uniprot.org/uniprotkb/search?query=gene:APP+AND+organism_id:9793
- **uniprot-P05067-entry**: UniProt Consortium. UniProtKB/Swiss-Prot entry P05067 (A4_HUMAN), Amyloid-beta precursor protein, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/P05067.txt


## Citations

1. _metadata.json
2. barnham-2003-cubd-structure-abstract.md
3. barnham-2003-cubd-structure-summary.md
4. borg-1996-x11-fe65-yenpty-abstract.md
5. borg-1996-x11-fe65-yenpty-summary.md
6. cao-2001-aicd-fe65-abstract.md
7. cao-2001-aicd-fe65-summary.md
8. capucchio-2010-equine-brain-abstract.md
9. capucchio-2010-equine-brain-summary.md
10. destrooper-1998-presenilin-abstract.md
11. destrooper-1998-presenilin-summary.md
12. esch-1990-alpha-secretase-abstract.md
13. esch-1990-alpha-secretase-summary.md
14. fiore-1995-fe65-ptb-abstract.md
15. fiore-1995-fe65-ptb-summary.md
16. gazzano-2025-horse-blood-abeta-abstract.md
17. gazzano-2025-horse-blood-abeta-fulltext.txt
18. gazzano-2025-horse-blood-abeta-summary.md
19. haass-2012-app-processing-abstract.md
20. haass-2012-app-processing-summary.md
21. heber-2000-app-family-knockouts-abstract.md
22. heber-2000-app-family-knockouts-summary.md
23. johnstone-1991-abeta-conservation-abstract.md
24. johnstone-1991-abeta-conservation-summary.md
25. jonsson-2012-a673t-abstract.md
26. jonsson-2012-a673t-summary.md
27. kamenetz-2003-activity-abeta-abstract.md
28. kamenetz-2003-activity-abeta-summary.md
29. kang-1987-app-cloning-abstract.md
30. kang-1987-app-cloning-summary.md
31. kitaguchi-1988-kpi-abstract.md
32. kitaguchi-1988-kpi-summary.md
33. kuhn-2010-adam10-abstract.md
34. kuhn-2010-adam10-summary.md
35. malbon-2022-donkey-alzheimer-pathology-abstract.md
36. malbon-2022-donkey-alzheimer-pathology-summary.md
37. muller-2017-app-physiology-abstract.md
38. muller-2017-app-physiology-summary.md
39. multhaup-1996-copper-reduction-abstract.md
40. multhaup-1996-copper-reduction-summary.md
41. oltersdorf-1989-protease-nexin-abstract.md
42. oltersdorf-1989-protease-nexin-summary.md
43. rice-2019-gabab-ligand-abstract.md
44. rice-2019-gabab-ligand-fulltext.txt
45. rice-2019-gabab-ligand-summary.md
46. ring-2007-sappalpha-rescue-abstract.md
47. ring-2007-sappalpha-rescue-summary.md
48. rohandesilva-1997-isoform-cells-abstract.md
49. rohandesilva-1997-isoform-cells-summary.md
50. rossjohn-1999-gfld-structure-abstract.md
51. rossjohn-1999-gfld-structure-summary.md
52. small-1994-heparin-neurite-abstract.md
53. small-1994-heparin-neurite-summary.md
54. soba-2005-dimerization-adhesion-abstract.md
55. soba-2005-dimerization-adhesion-summary.md
56. tanaka-1989-isoform-tissue-abstract.md
57. tanaka-1989-isoform-tissue-summary.md
58. uniprot-A0A9L0JJJ9-entry-summary.md
59. uniprot-A0A9L0JJJ9-entry.txt
60. uniprot-P05067-entry-summary.md
61. uniprot-P05067-entry.txt
62. uniprot-donkey-APP-entries-search-summary.md
63. uniprot-donkey-APP-entries-search.tsv
64. vannostrand-1989-protease-nexin-abstract.md
65. vannostrand-1989-protease-nexin-summary.md
66. vassar-1999-bace-abstract.md
67. vassar-1999-bace-summary.md
68. wang-2004-e2-dimer-abstract.md
69. wang-2004-e2-dimer-summary.md
70. wang-2009-synaptogenesis-abstract.md
71. wang-2009-synaptogenesis-summary.md
72. wang-2020-donkey-genome-abstract.md
73. wang-2020-donkey-genome-fulltext.txt
74. wang-2020-donkey-genome-summary.md
75. zheng-1995-app-knockout-abstract.md
76. zheng-1995-app-knockout-summary.md