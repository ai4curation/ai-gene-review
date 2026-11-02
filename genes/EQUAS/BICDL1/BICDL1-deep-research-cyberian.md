---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:17:24.927687'
end_time: '2026-10-25T23:27:14.747185'
duration_seconds: 589.82
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: BICDL1
  gene_symbol: BICDL1
  uniprot_accession: A0A9L0JLY3
  protein_description: 'SubName: Full=BICD family like cargo adaptor 1 {ECO:0000313|Ensembl:ENSEASP00005050982.1};'
  gene_info: Name=BICDL1 {ECO:0000313|Ensembl:ENSEASP00005050982.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Not specified in UniProt
  protein_domains: BICDL1/2-like_C. (IPR060493); Spindly/BICDR_Dynein_Adapter. (IPR051149);
    BICDL2_C (PF27654); Spindly (PF28219)
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
- **UniProt Accession:** A0A9L0JLY3
- **Protein Description:** SubName: Full=BICD family like cargo adaptor 1 {ECO:0000313|Ensembl:ENSEASP00005050982.1};
- **Gene Information:** Name=BICDL1 {ECO:0000313|Ensembl:ENSEASP00005050982.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** BICDL1/2-like_C. (IPR060493); Spindly/BICDR_Dynein_Adapter. (IPR051149); BICDL2_C (PF27654); Spindly (PF28219)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "BICDL1" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'BICDL1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **BICDL1** (gene ID: BICDL1, UniProt: A0A9L0JLY3) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# BICDL1 (BICD family-like cargo adaptor 1) in the donkey, *Equus asinus* (UniProt A0A9L0JLY3)

## 1. Introduction and summary

The donkey protein A0A9L0JLY3 is an unreviewed TrEMBL entry, 573 residues long. It was predicted by Ensembl from the donkey reference genome and is named "BICD family like cargo adaptor 1" with the gene symbol *BICDL1*. Its annotation rests only on automated domain and family assignments: the Spindly/BICDR dynein-adapter family (IPR051149, Pfam PF28219 "Spindly"), a BICDL1/2-like C-terminal domain (IPR060493, Pfam PF27654), three predicted coiled-coil segments, and PANTHER subfamily PTHR32123:SF12 "BICD family-like cargo adapter 1". It has protein-existence level 4 (predicted) [uniprot-a0a9l0jly3-entry]. No study has looked at the donkey protein itself. Everything below about its function therefore comes by orthology from mammalian BICDL1. That gene is also called BICDR1 or BICDR-1 (Bicaudal-D-related protein 1) and, in older nomenclature, CCDC64. Most of the experimental work has been done on the mouse protein, with orthologues studied in zebrafish and *Drosophila* [schlager-2010-bicdr1-rab6; ulker-yilmazer-2026-bicdl1-retina; vazquezpianzola-2024-bicdr-bristle].

The symbol is not ambiguous. BICDL1, BICDR1 and CCDC64 all refer to the same vertebrate gene, and the mouse knock-in study states this equivalence explicitly ("Bicdl1 (BICD family-like cargo adaptor 1, Bicdr1, Ccdc64)") [ulker-yilmazer-2026-bicdl1-retina]. The donkey sequence is nearly identical to human BICDL1 (Q6ZP65) over the N-terminal and C-terminal thirds, and it keeps the key functional motifs (Section 2). It is therefore a true orthologue. More precisely, it is one alternative-splice isoform of the donkey gene, lacking one central coiled-coil exon and including an alternative exon also found in human isoform 2.

Taken together, the literature defines BICDL1 as a coiled-coil **activating adaptor for cytoplasmic dynein-1**. Its N-terminal coiled coil binds dynein and dynactin together, which turns dynein into a processive minus-end-directed motor. Compared with BICD2, BICDL1 strongly favours recruiting **two dynein dimers** per dynactin, which gives faster and more forceful movement [urnavicius-2018-two-dyneins; elshenawy-2019-adaptor-force; chaaban-2022-tandem-adaptor]. Its C-terminal domain is a specific effector of the GTP-bound small GTPase **Rab6** (Rab6A and Rab6B) [schlager-2010-bicdr1-rab6]. Its N-terminal region also binds the tail of the kinesin-3 motor **KIF1C** [schlager-2010-bicdr1-rab6]. In cells, BICDL1 sits on Rab6-positive secretory vesicles clustered around the centrosome. By tipping the balance between opposing motors toward dynein, it gathers these vesicles in the pericentrosomal region and controls where secretion happens. In early neurons this restricts anterograde secretory transport and delays neurite outgrowth [schlager-2010-bicdr1-rab6; schlager-2014-bicd-velocity]. Recent loss-of-function genetics in the mouse shows that it has a non-redundant role in maintaining the outer retina [ulker-yilmazer-2026-bicdl1-retina]. It is also hijacked by polyomaviruses during entry [golgi-bicd-2020-viral-cargo].

## 2. Identity, domain architecture and conservation of the donkey protein

The donkey gene sits on chromosome 8 of the reference proteome (UP000694387). The only literature reference in the entry is the donkey genome paper, which supports the sequence but says nothing about function [uniprot-a0a9l0jly3-entry]. The best-characterised orthologues are human BICDL1 (Q6ZP65, 573 aa) and mouse Bicdl1 (A0JNT9, 577 aa), both Swiss-Prot reviewed. The human annotation is itself transferred "by similarity" from the mouse entry: dynein-dynactin adaptor activity, recruitment of two dyneins, Rab6A/Rab6B and KIF1C binding, and centrosomal localisation [uniprot-q6zp65-entry; uniprot-a0jnt9-entry].

I compared the sequences directly (notes in `SEQUENCE_NOTES.md`). The donkey N-terminal ~250 residues and C-terminal ~270 residues match human BICDL1 almost residue for residue, but the central region differs. Comparison with the other donkey entries settles what this means. UniProt holds five donkey BICDL1 entries of 573–626 residues, and all of them come from the same Ensembl gene, ENSEASG00005007623 [uniprot-a0a9l0jly3-entry; uniprot-a0a9l0i4k1-entry; uniprot-a0a9l0jcr9-entry; uniprot-a0a9l0k8k5-entry; uniprot-a0a8c4lg90-entry]. The 574-residue entry A0A9L0I4K1 has the same architecture as human Q6ZP65 and mouse A0JNT9, so it represents the canonical isoform. A0A9L0JLY3 matches it exactly except for two coordinated changes. First, it lacks 49 residues (IKMLSDRKRELEHRLSATLEENDLLQGTVEELQDRVLILERQGHDKDLQ; canonical donkey residues 256–304) from the long central coiled coil. Second, it carries a 48-residue insertion (SSRRIDDDSLEEQIRQTSEDSRALRELMEGERGKLRQSLEELQRLHSQ) after canonical T438. The insertion is not a prediction artefact. Human isoform 2 carries the same alternative exon inserted after T436 ("TGSRRLDDDSLEEQIRQTSEDSRALRELMEGERGKLRQSLEELQRLHSQ"), and that isoform is supported by a full-length cDNA [uniprot-q6zp65-entry]. A0A9L0JLY3 is therefore best read as an **alternative-splice isoform** of donkey BICDL1: it skips one central coiled-coil exon and includes an alternative exon after the Spindly-motif region. No study has tested the function of this specific isoform (see Section 7 and Open Questions).

The structurally defined dynein- and dynactin-binding motifs of mouse BICDR1 [chaaban-2022-tandem-adaptor] can all be found in A0A9L0JLY3. The HBS1 motif residues Q150 and H153, and the coiled-coil registry marker W166, correspond to donkey Q148, H151 and W164. The first residue of the Spindly motif, mouse L347, corresponds to donkey L296. Because exon 256–304 is skipped, this isoform's Spindly motif sits 49 residues closer to the N-terminal motifs than in the canonical protein. Beyond these, two more motifs that define function are conserved. The first is a CC1-box-like "AARLG" sequence (AAxxG) at donkey residues 114–118, at the start of the first predicted coiled coil (122–220). The CC1 box is the hallmark of the CC1-box subfamily of dynein adaptors, which binds the C-terminal helix of the dynein light intermediate chain (LIC1). Lee et al. place BICDL1 and BICDL2 in this subfamily together with BICD1/2, Spindly, TRAK1/2 and HAP1 [lee-2020-lic1-adaptor]. In dynein-dynactin-BICDR1 structures, the AAxxG CC1 box of the primary BICDR1 contacts LIC helices from both dyneins [rao-2026-three-dyneins]. The second motif is the Rab6-binding lysine. In mouse, K512 is required for Rab6 binding and corresponds to the lysine mutated in a loss-of-function *Drosophila BicD* allele [schlager-2010-bicdr1-rab6]. It maps to donkey K509, in the invariant context LDAIQQ**K**LNLSQQLE inside the Pfam BICDL2_C domain (489–541). The protein should therefore bind Rab6. Lee et al. also note that a short "Spindly motif" at the end of the dynactin-binding coiled coil contacts p25/p27 at the dynactin pointed end. The sequence C-terminal to it is the most divergent part of activating adaptors and carries cargo specificity [lee-2020-lic1-adaptor], which fits the C-terminal Rab6-binding domain in BICDL1.

In evolutionary terms, BICDR-1 was found by homology to Bicaudal-D. It is conserved across vertebrates and has a fly orthologue, whereas its paralogue BICDR-2 (BICDL2) is vertebrate-only [schlager-2010-bicdr1-rab6]. *Drosophila* BicDR (CG32137) keeps the first and third coiled-coil regions of BicD but not the second, and it also keeps the Rab6-binding lysine (K555 in the BicDR-B isoform) [vazquezpianzola-2024-bicdr-bristle].

## 3. Molecular function: an activating adaptor that recruits two dyneins

Cytoplasmic dynein-1 is autoinhibited on its own. It becomes a processive motor only when it assembles with dynactin and a coiled-coil "activating adaptor" that also binds cargo [reckpeterson-2018-dynein-review; olenick-2019-adaptors-glance; canty-2020-dynein-review]. BICDL1 is one of the best-studied examples. In the first characterisation, GFP-BICDR-1 co-immunoprecipitated the main dynein and dynactin subunits from HeLa cells. Overexpression roughly doubled the amount of dynein and dynactin around the centrosome. Pericentrosomal BICDR-1 was lost when dynein heavy chain or p150Glued was depleted (about 15% of knockdown cells kept centrosomal BICDR-1, compared with about 74% of control cells) [schlager-2010-bicdr1-rab6].

Reconstitution and cryo-EM then showed how BICDL1 differs from the prototype adaptor BICD2. Urnavicius et al. used purified mouse BICDR1 (BICDL1). In two-colour single-molecule assays, about 61% of motile dynein-dynactin-BICDR1 (DDR) complexes contained two dyneins, against about 26% for BICD2. By negative-stain EM, about 94% of dynein tail-dynactin-BICDR1 complexes had two dyneins [urnavicius-2018-two-dyneins]. Recruiting a second dynein raised both stall force and velocity. A 3.5 Å reconstruction of the tail-dynactin-BICDR1 complex showed dynactin acting as a scaffold that holds two dyneins side by side. The N-terminus of BICDR1 runs along a "downward" path, stabilised by contacts with CapZβ at the barbed end, which lets the adaptor contact the second dynein [urnavicius-2018-two-dyneins]. Single-molecule stepping and optical-trap work found that two-dynein complexes produce more force and are more likely to win a tug-of-war against kinesin. Velocity, however, is set by the adaptor and by tail–tail interactions between the paired dyneins [elshenawy-2019-adaptor-force]. Lis1 promotes pairing of two dyneins on dynactin, but its effect is small with BICDR1 because DDR complexes are already predisposed to hold two dyneins [elshenawy-2020-lis1-pairing].

Higher-resolution structures on microtubules showed that each DDR complex contains two BICDR1 adaptors. Both make similar contacts with the dyneins but differ in how they contact each other and dynactin [chaaban-2022-tandem-adaptor]. The main adaptor, BICDR-A, runs the full length of dynactin from the barbed end to the pointed end. The second, BICDR-B, covers only about half the complex. The two coiled coils interact over about 30 residues, with their registers offset by about 47 residues. Mass photometry shows that BICDR1 alone is a single coiled-coil dimer, and the second adaptor binds stably only on microtubules: it was present in only ~5% of particles in the earlier off-microtubule data [chaaban-2022-tandem-adaptor]. Three conserved motifs mediate binding. The N-terminal CC1 box (AAXXG) binds the C-terminal helix of the dynein light intermediate chain. The HBS1 motif (QXX[H/Y]) uses Q150 and H153 to contact Y827 of the dynein heavy chain. At the C-terminal end of the dynactin-spanning coiled coil, the Spindly motif, which begins at L347 and is preceded by a break in the coiled coil, docks into a hydrophobic pocket on p25 at the dynactin pointed end [chaaban-2022-tandem-adaptor]. Later structures with the adaptor JIP3 used the BICDR1 HBS1–heavy chain contact as the reference for comparison, and they confirmed that BICDR1 makes few direct contacts with the dynactin filament itself [singh-2024-lis1-assembly]. Unlike BICD2, full-length BICDR1 is not autoinhibited. Purified full-length mouse BicDR1 assembles motile dynein-dynactin complexes in vitro as readily as truncated constructs [hiv-2025-dynein-hijack]. In this arrangement the CC1 box of the primary BICDR1 (BICDR-A) contacts the LIC helices of dynein A2 and dynein B1, while the auxiliary BICDR-B contacts only the A2 LIC and is thought to stabilise the microtubule-bound complex. The dynactin shoulder also has room for a third dynein, as seen with other adaptors [rao-2026-three-dyneins]. A recent structural survey of five other adaptors (it did not include BICDR1) concludes that all activating adaptors use shared contacts: an N-terminal contact at the dynein heavy-chain HBS1 site, contacts along the dynein-dynactin groove, and C-terminal binding at the dynactin pointed end. Adaptor-specific features tune stoichiometry [damico-2026-adaptor-structures]. BICDR1 is now widely used as a reference "double-dynein" adaptor, including for interpreting dynein-dynactin motility in living cells [verma-2026-dynein-living-cells].

## 4. Cargo recognition: Rab6 effector and coupling to KIF1C

The C-terminal domain of BICDL1 makes it a specific Rab6 effector. In a GST pull-down screen against 60 Rab GTPases covering 43 subfamilies, BICDR-1 bound strongly only to Rab6A/B, with marginal binding to Rab11B and Rab12 [schlager-2010-bicdr1-rab6]. Both the full-length protein and the C-terminal fragment (residues 382–577) bound constitutively active Rab6A-Q72R but not GDP-locked Rab6A-T27N. Binding of the purified C-terminus to GST-Rab6A and GST-Rab6B was direct and strongest for the neuron-enriched Rab6B. The K512M mutation abolished binding, and BICDR-1 competed with BICD2 for Rab6 in vitro [schlager-2010-bicdr1-rab6]. BICDL1 therefore probably shares a binding site on Rab6 with the BICD proteins. The ratio of BICD to BICDR-1 on a vesicle could set its direction of transport [schlager-2010-bicdr1-rab6].

The N-terminal half of BICDR-1 (residues 1–353) bound the C-terminal tail of the kinesin-3 KIF1C (residues 811–1090) in yeast two-hybrid assays. It did not bind kinesin-1 (Kif5). Overexpressed BICDR-1 co-precipitated endogenous KIF1C and pulled it into the pericentrosomal region of Vero cells and neurons [schlager-2010-bicdr1-rab6]. BICDL1 is thus a scaffold for both directions of travel on Rab6 carriers. Overexpression drives KIF1C to the cell centre, which suggests that dynein dominates on BICDR-1-bound vesicles [schlager-2010-bicdr1-rab6]. The KIF1C–BICDR1 interaction continues to be cited in recent work on how KIF1C activates and extends dynein movement through other adaptors [abidali-2025-kif1c-fhf].

Cargo specificity extends beyond Rab6 vesicles. In polyomavirus entry, siRNA knockdown of BICDR1 or BICD2 blocked SV40 arrival at the nucleus (by about 70% and 81%), whereas knockdown of HOOK3, ninein, RAB11FIP3 or SPDL1 did not. Mouse BICDR1 rescued the knockdown. BICDR1 bound the capsid protein VP1 and the viral genome directly and was needed for disassembly of the virus once it reached the cytosol, close to Golgi-associated BICD2/BICDR1 [golgi-bicd-2020-viral-cargo]. For HIV-1, the most recent reconstitution work concludes that the capsid binds dynein's tail accessory chains directly rather than through an adaptor. Even so, BicDR1 supported processive movement of more than 80% of microtubule-recruited HIV-1 cores in vitro. Its knockdown cut infectivity by about 30% in A549 cells and about 42% in CHME-5 cells, though not in HeLa TZM-bl cells, and proximity-ligation signal between capsid and BicDR1 rose about 80-fold one to two hours after infection [hiv-2025-dynein-hijack]. In contrast, the *Orientia tsutsugamushi* autotransporter ScaC recruits BICD1 and BICD2 but does not bind BICDR1, which shows that cargo recognition differs within the BICD family [orientia-2025-scac-bicd].

## 5. Subcellular localisation

Endogenous BICDR-1 in kidney-derived Vero cells gave intense perinuclear, punctate staining centred on the γ-tubulin-marked centrosome, at the focus of the radial microtubule array. It did not associate with actin [schlager-2010-bicdr1-rab6]. This localisation needed intact microtubules, γ-tubulin, Rab6A and dynein/dynactin. It was not affected by actin depolymerisation. BICDR-1 co-localised with Rab6 on pericentrosomal vesicles but not on Rab6-positive Golgi stacks, and not with GM130, TGN46, γ-adaptin, galactosyltransferase or EEA1 [schlager-2010-bicdr1-rab6]. The vesicles carry the secretory marker NPY-GFP, so BICDR-1 is a component of Rab6-positive post-Golgi secretory carriers. Live imaging showed mCherry-BICDR-1 on mobile Rab6 vesicles and tubules that docked with larger BICDR-1/Rab6 membrane domains in the neuronal soma [schlager-2010-bicdr1-rab6]. Pull-down and mass spectrometry also enriched centrosomal proteins (data not shown in that paper), raising the possibility of direct centrosomal anchoring [schlager-2010-bicdr1-rab6]. Other cell types have been described as having Golgi-associated pools of BICDR1 [golgi-bicd-2020-viral-cargo]. The donkey protein is therefore expected to act in the cytoplasm on microtubule-borne Rab6 secretory vesicles, concentrated at the centrosome or microtubule-organising centre.

## 6. Biological roles: positioning secretory vesicles, neuronal development, retina

Mouse BICDR-1 mRNA and protein are most abundant in kidney, with moderate levels in brain and testis. Expression is high in early embryos (E10 onward) and falls during development. In situ hybridisation detects it throughout the developing brain, the eye (including the neural retina), dorsal root ganglia and kidney [schlager-2010-bicdr1-rab6]. In cultured hippocampal neurons it is strongly expressed at DIV1–2 and almost undetectable after DIV3, while Rab6 and dynactin levels stay constant or rise [schlager-2010-bicdr1-rab6].

Functionally, BICDL1 sets where secretory carriers are distributed rather than whether they fuse. More BICDR-1 moves Rab6/NPY vesicles progressively toward the centrosome. In neurons it raises somatic Rab6A/B about threefold and empties NPY vesicles from neurites. Exocytosis kinetics are unchanged, but fusion events shift from neurites (or the cell periphery in fibroblasts) to the soma or pericentrosomal region [schlager-2010-bicdr1-rab6]. Keeping BICDR-1 expressed beyond its normal window cut total neurite length by more than 50% at DIV3, affecting both axons and dendrites. The Rab6-binding C-terminal fragment alone also suppressed outgrowth, whereas the K512M version did not, linking the phenotype to Rab6 engagement [schlager-2010-bicdr1-rab6]. The authors propose a model in which high early BICDR-1 holds secretory cargo around the centrosome, and its later decline releases anterograde Rab6 transport needed for neuritogenesis [schlager-2010-bicdr1-rab6]. A commentary placed this finding within the expanding BICD family [terenzio-2010-bicd-family]. Inducible recruitment experiments later showed that BICDR-1 speeds up minus-end-directed Rab6 vesicle movements and changes their distribution, again with reduced axon outgrowth [schlager-2014-bicd-velocity]. The in vitro two-dynein mechanism gives a molecular explanation for why BICDR1 overexpression, but not BICD2 overexpression, overcomes kinesin-driven transport [urnavicius-2018-two-dyneins].

In vivo, morpholino knockdown of zebrafish *bicdr-1* disrupted neural development and blocked eye formation, with more apoptosis but no change in proliferation [schlager-2010-bicdr1-rab6]. In mice, an ENU forward-genetic screen found a recessive splice-donor mutation in *Bicdl1* (the "bargain" allele, at the first base of intron 4) linked to outer retinal thinning. A CRISPR knock-in reproduced it: the transcript was reduced, consistent with nonsense-mediated decay, and the mice showed mild thinning of the outer retina and rod outer segments, more fundus spots and subretinal Iba1+/Tmem119+ cells, a late fall in ERG a-wave amplitude, and fewer RPE mitochondria. Transcriptomic data linked *Bicdl1* levels to oxidative-phosphorylation pathways [ulker-yilmazer-2026-bicdl1-retina]. In *Drosophila*, BicDR works with BicD to build the bristle shaft. It supports actin bundle organisation and the normal levels and distribution of Rab6 and Spn-F, and EF1γ was identified as a candidate cargo. The authors suggest BicDR moves cargo over short distances while BicD handles long-range transport [vazquezpianzola-2024-bicdr-bristle]. Several transcriptomic and prognostic studies in cancer mention *BICDL1*, but they add little mechanistic insight and are not reviewed here.

## 7. Synthesis and pathway context

Integrating these data, the donkey BICDL1 protein can be assigned the following function with good confidence. It is a dimeric coiled-coil activating adaptor for cytoplasmic dynein-1/dynactin. Its CC1 box (donkey AARLG, 114–118) binds dynein LIC1, and its long coiled coil runs along the dynactin filament to the pointed end. It favours a two-dynein, high-force, high-speed motor. Its conserved C-terminal domain (around donkey K509) recruits this motor to GTP-Rab6-positive post-Golgi secretory vesicles, competing with BICD1/2. Its N-terminal region also engages the opposing kinesin-3 KIF1C. Within the Rab6-dependent secretory pathway it acts as a direction-setting switch: it concentrates carriers around the centrosome and so controls where constitutive and neuropeptide secretion occur, notably during early neuronal differentiation and in retinal homeostasis [schlager-2010-bicdr1-rab6; urnavicius-2018-two-dyneins; chaaban-2022-tandem-adaptor; lee-2020-lic1-adaptor; ulker-yilmazer-2026-bicdl1-retina]. Appropriate GO-style descriptors are dynein/dynactin complex binding (activating adaptor), small-GTPase (Rab6) binding, kinesin binding, vesicle transport along microtubule / Golgi-to-secretory-vesicle transport, regulation of neuron projection development, and localisation to cytoplasmic vesicles at the centrosome. All of these are inferred by orthology; none has been tested for the equid protein. One caveat applies specifically to this isoform. In the canonical protein, the coiled coil between the N-terminal dynein-binding motifs (CC1 box, HBS1) and the C-terminal Spindly motif must span the length of the dynactin filament, from the barbed end to the pointed end [chaaban-2022-tandem-adaptor; lee-2020-lic1-adaptor]. A0A9L0JLY3 removes 49 residues from exactly this segment. That would shorten the helix by roughly 7 nm if it stays continuous, which could change or weaken how it bridges dynactin, or alter how two adaptors offset against each other. This is my structural inference, not an experimental result. The Rab6-binding C-terminal domain and the KIF1C-binding N-terminal region are untouched. So the isoform could in principle bind cargo without fully activating dynein, which might modulate the canonical isoform's activity. This remains to be tested.

## Open Questions

Several questions remain for both the donkey protein and the gene family. First, A0A9L0JLY3 is an alternative-splice isoform: it skips the exon encoding canonical residues 256–304 and includes the alternative exon also seen in human isoform 2. How abundant it is in different tissues, and whether it is actually expressed as protein, should be checked with donkey or horse RNA-seq or Iso-Seq. Its biochemistry also needs testing, because the length and register of the coiled coil help set adaptor stoichiometry and dynactin bridging [chaaban-2022-tandem-adaptor; damico-2026-adaptor-structures]. Single-molecule motility assays with the two isoforms would settle whether the short form still activates dynein-dynactin and still recruits two dyneins. Second, BICDL1 expression is regulated during development, but the mechanism behind that regulation, and any post-translational control, is unknown. Third, full-length BICDR1 does not appear to be autoinhibited [hiv-2025-dynein-hijack], and it is unclear how its activity is restrained in cells. The structural basis of Rab6 recognition by the BICDL1 C-terminal domain, and how BICDL1 competes with BICD2, has not been solved. Fourth, it is not known how KIF1C and dynein are coordinated on one BICDL1 scaffold, and whether BICDL1 activates KIF1C as Hook3 and other adaptors do [abidali-2025-kif1c-fhf]. Fifth, the cargo repertoire beyond Rab6 vesicles and polyomavirus capsids (including the possible centrosomal partners and the EF1γ-like cargo seen in flies) has not been mapped systematically [schlager-2010-bicdr1-rab6; vazquezpianzola-2024-bicdr-bristle]. Finally, the high expression in kidney and the retinal phenotype in mice point to unexplored roles in adult epithelial and photoreceptor or RPE trafficking [schlager-2010-bicdr1-rab6; ulker-yilmazer-2026-bicdl1-retina]. Whether equids have any related phenotype is entirely unknown.

## References

- [uniprot-a0a9l0jly3-entry] UniProtKB/TrEMBL A0A9L0JLY3_EQUAS, "BICD family like cargo adaptor 1", *Equus asinus*, entry version 14 (2026). https://rest.uniprot.org/uniprotkb/A0A9L0JLY3.txt (sequence from Wang C. et al., Nat Commun 11:6014 (2020), PMID 33293529).
- [uniprot-q6zp65-entry] UniProtKB/Swiss-Prot Q6ZP65 (BICL1_HUMAN). https://rest.uniprot.org/uniprotkb/Q6ZP65.txt
- [uniprot-a0jnt9-entry] UniProtKB/Swiss-Prot A0JNT9 (BICL1_MOUSE). https://rest.uniprot.org/uniprotkb/A0JNT9.txt
- [schlager-2010-bicdr1-rab6] Schlager MA, Kapitein LC, Grigoriev I, Burzynski GM, Wulf PS, Keijzer N, de Graaff E, Fukuda M, Shepherd IT, Akhmanova A, Hoogenraad CC. Pericentrosomal targeting of Rab6 secretory vesicles by Bicaudal-D-related protein 1 (BICDR-1) regulates neuritogenesis. EMBO J. 2010. PMID: 20360680; PMCID: PMC2876961; DOI: 10.1038/emboj.2010.51
- [terenzio-2010-bicd-family] Terenzio M, Schiavo G. The more, the better: the BICD family gets bigger. EMBO J. 2010. PMID: 20485297; PMCID: PMC2876973; DOI: 10.1038/emboj.2010.78
- [schlager-2014-bicd-velocity] Schlager MA, Serra-Marques A, Grigoriev I, Gumy LF, Esteves da Silva M, Wulf PS, Akhmanova A, Hoogenraad CC. Bicaudal D family adaptor proteins control the velocity of dynein-based movements. Cell Rep. 2014. PMID: 25176647; DOI: 10.1016/j.celrep.2014.07.052
- [urnavicius-2018-two-dyneins] Urnavicius L, Lau CK, Elshenawy MM, Morales-Rios E, Motz C, Yildiz A, Carter AP. Cryo-EM shows how dynactin recruits two dyneins for faster movement. Nature. 2018. PMID: 29420470; PMCID: PMC5988349; DOI: 10.1038/nature25462
- [elshenawy-2019-adaptor-force] Elshenawy MM, Canty JT, Oster L, Ferro LS, Zhou Z, Blanchard SC, Yildiz A. Cargo adaptors regulate stepping and force generation of mammalian dynein-dynactin. Nat Chem Biol. 2019. PMID: 31501589; PMCID: PMC6810841; DOI: 10.1038/s41589-019-0352-0
- [elshenawy-2020-lis1-pairing] Elshenawy MM, Kusakci E, Volz S, Baumbach J, Bullock SL, Yildiz A. Lis1 activates dynein motility by modulating its pairing with dynactin. Nat Cell Biol. 2020. PMID: 32341547; PMCID: PMC7212015; DOI: 10.1038/s41556-020-0501-4
- [lee-2020-lic1-adaptor] Lee IG, Cason SE, Alqassim SS, Holzbaur ELF, Dominguez R. A tunable LIC1-adaptor interaction modulates dynein activity in a cargo-specific manner. Nat Commun. 2020. PMID: 33173051; PMCID: PMC7655957; DOI: 10.1038/s41467-020-19538-7
- [chaaban-2022-tandem-adaptor] Chaaban S, Carter AP. Structure of dynein-dynactin on microtubules shows tandem adaptor binding. Nature. 2022. PMID: 36071160; PMCID: PMC7613678; DOI: 10.1038/s41586-022-05186-y
- [uniprot-a0a9l0i4k1-entry] UniProtKB/TrEMBL A0A9L0I4K1 (donkey BICDL1, 574 aa; Ensembl ENSEASP00005034898.1). https://rest.uniprot.org/uniprotkb/A0A9L0I4K1.txt
- [uniprot-a0a9l0jcr9-entry] UniProtKB/TrEMBL A0A9L0JCR9 (donkey BICDL1, 622 aa; Ensembl ENSEASP00005050984.1). https://rest.uniprot.org/uniprotkb/A0A9L0JCR9.txt
- [uniprot-a0a9l0k8k5-entry] UniProtKB/TrEMBL A0A9L0K8K5 (donkey BICDL1, 626 aa; Ensembl ENSEASP00005061163.1). https://rest.uniprot.org/uniprotkb/A0A9L0K8K5.txt
- [uniprot-a0a8c4lg90-entry] UniProtKB/TrEMBL A0A8C4LG90 (donkey BICDL1, 589 aa; Ensembl ENSEASP00005010809.2). https://rest.uniprot.org/uniprotkb/A0A8C4LG90.txt
- [singh-2024-lis1-assembly] Singh K, Lau CK, Manigrasso G, Gama JB, Gassmann R, Carter AP. Molecular mechanism of dynein-dynactin complex assembly by LIS1. Science. 2024. PMID: 38547289; PMCID: PMC7615804; DOI: 10.1126/science.adk8544
- [hiv-2025-dynein-hijack] Badieyan S, Lichon D, Keceli SK, Andreas MP, Gillies JP, Peng W, Shi J, DeSantis ME, Aiken CR, Böcking T, Giessen TW, Campbell EM, Cianfrocco MA. HIV-1 binds dynein directly to hijack microtubule transport machinery. Sci Adv. 2025. PMID: 40532013; PMCID: PMC12175901; DOI: 10.1126/sciadv.adn6796
- [rao-2026-three-dyneins] Rao L, Liu X, Arnold M, Okada K, McKenney RJ, Stengel K, Sidoli S, Berger F, et al. Adaptor-mediated recruitment of three dyneins to dynactin enhances force generation. Nat Cell Biol. 2026. PMID: 41699082; PMCID: PMC12992115; DOI: 10.1038/s41556-026-01877-0
- [damico-2026-adaptor-structures] d'Amico EA, Chaaban S, Abid Ali F, Michalski L, Carter AP. Structural basis of dynein interaction with diverse activating adaptors. bioRxiv preprint 2026. Europe PMC PPR1212969; DOI: 10.64898/2026.04.25.720804
- [verma-2026-dynein-living-cells] Verma V, Wadsworth P, Maresca TJ. Human dynein-dynactin is a fast processive motor in living cells. eLife. 2026. PMID: 41879034; PMCID: PMC13016606; DOI: 10.7554/elife.94963
- [abidali-2025-kif1c-fhf] Abid Ali F, Zwetsloot AJ, Stone CE, Morgan TE, Wademan RF, Carter AP, Straube A. KIF1C activates and extends dynein movement through the FHF cargo adapter. Nat Struct Mol Biol. 2025. PMID: 39747486; PMCID: PMC11996680; DOI: 10.1038/s41594-024-01418-z
- [golgi-bicd-2020-viral-cargo] Spriggs CC, Badieyan S, Verhey KJ, Cianfrocco MA, Tsai B. Golgi-associated BICD adaptors couple ER membrane penetration and disassembly of a viral cargo. J Cell Biol. 2020. PMID: 32259203; PMCID: PMC7199864; DOI: 10.1083/jcb.201908099
- [orientia-2025-scac-bicd] Manigrasso G, Saharat K, Chaichana P, Kullapanich C, Atwal S, Boulanger J, Morgan TE, Kramer H, Salje J, Carter AP. The intracellular bacterium Orientia tsutsugamushi uses the autotransporter ScaC to activate BICD adaptors for dynein-based motility. Nat Commun. 2025. PMID: 40610402; PMCID: PMC12229497; DOI: 10.1038/s41467-025-61105-5
- [vazquezpianzola-2024-bicdr-bristle] Jejina A, Ayala Y, Beuchle D, Höhener T, Dörig RE, Vazquez-Pianzola P, Hernández G, Suter B. Role of BicDR in bristle shaft construction and support of BicD functions. J Cell Sci. 2024. PMID: 38264934; PMCID: PMC10917063; DOI: 10.1242/jcs.261408
- [ulker-yilmazer-2026-bicdl1-retina] Ulker-Yilmazer G, Kirman DC, Yu T, Turpin ER, Shrestha S, Yuksel S, He YG, Ludwig S, Kumar A, Xing C, Moresco EMY, Beutler BA, Aredo B, Ufret-Vincenty RL. A mutation in Bicdl1 (BICD family-like cargo adaptor 1) leads to mild outer retina thinning and late retinal dysfunction in a mouse model. Mol Vis. 2026. PMID: 42774019; PMCID: PMC13568186; DOI: 10.63500/mv_v32_281
- [reckpeterson-2018-dynein-review] Reck-Peterson SL, Redwine WB, Vale RD, Carter AP. The cytoplasmic dynein transport machinery and its many cargoes. Nat Rev Mol Cell Biol. 2018. PMID: 29662141; PMCID: PMC6457270; DOI: 10.1038/s41580-018-0004-3
- [olenick-2019-adaptors-glance] Olenick MA, Holzbaur ELF. Dynein activators and adaptors at a glance. J Cell Sci. 2019. PMID: 30877148; PMCID: PMC6451413; DOI: 10.1242/jcs.227132
- [canty-2020-dynein-review] Canty JT, Yildiz A. Activation and regulation of cytoplasmic dynein. Trends Biochem Sci. 2020. PMID: 32311337; PMCID: PMC7179903; DOI: 10.1016/j.tibs.2020.02.002


## Citations

1. abidali-2025-kif1c-fhf-abstract.md
2. abidali-2025-kif1c-fhf-fulltext.txt
3. abidali-2025-kif1c-fhf-summary.md
4. canty-2020-dynein-review-abstract.md
5. canty-2020-dynein-review-summary.md
6. chaaban-2022-tandem-adaptor-abstract.md
7. chaaban-2022-tandem-adaptor-fulltext.txt
8. chaaban-2022-tandem-adaptor-summary.md
9. damico-2026-adaptor-structures-abstract.md
10. damico-2026-adaptor-structures-summary.md
11. elshenawy-2019-adaptor-force-abstract.md
12. elshenawy-2019-adaptor-force-summary.md
13. elshenawy-2020-lis1-pairing-abstract.md
14. elshenawy-2020-lis1-pairing-fulltext.txt
15. elshenawy-2020-lis1-pairing-summary.md
16. golgi-bicd-2020-viral-cargo-abstract.md
17. golgi-bicd-2020-viral-cargo-fulltext.txt
18. golgi-bicd-2020-viral-cargo-summary.md
19. hiv-2025-dynein-hijack-abstract.md
20. hiv-2025-dynein-hijack-fulltext.txt
21. hiv-2025-dynein-hijack-summary.md
22. lee-2020-lic1-adaptor-abstract.md
23. lee-2020-lic1-adaptor-fulltext.txt
24. lee-2020-lic1-adaptor-summary.md
25. olenick-2019-adaptors-glance-abstract.md
26. olenick-2019-adaptors-glance-summary.md
27. orientia-2025-scac-bicd-abstract.md
28. orientia-2025-scac-bicd-fulltext.txt
29. orientia-2025-scac-bicd-summary.md
30. rao-2026-three-dyneins-abstract.md
31. rao-2026-three-dyneins-fulltext.txt
32. rao-2026-three-dyneins-summary.md
33. reckpeterson-2018-dynein-review-abstract.md
34. reckpeterson-2018-dynein-review-summary.md
35. schlager-2010-bicdr1-rab6-abstract.md
36. schlager-2010-bicdr1-rab6-fulltext.txt
37. schlager-2010-bicdr1-rab6-summary.md
38. schlager-2014-bicd-velocity-abstract.md
39. schlager-2014-bicd-velocity-summary.md
40. singh-2024-lis1-assembly-abstract.md
41. singh-2024-lis1-assembly-fulltext.txt
42. singh-2024-lis1-assembly-summary.md
43. terenzio-2010-bicd-family-abstract.md
44. terenzio-2010-bicd-family-summary.md
45. ulker-yilmazer-2026-bicdl1-retina-abstract.md
46. ulker-yilmazer-2026-bicdl1-retina-fulltext.txt
47. ulker-yilmazer-2026-bicdl1-retina-summary.md
48. uniprot-a0a8c4lg90-entry.txt
49. uniprot-a0a9l0i4k1-entry.txt
50. uniprot-a0a9l0jcr9-entry.txt
51. uniprot-a0a9l0jly3-entry.txt
52. uniprot-a0a9l0k8k5-entry.txt
53. uniprot-a0jnt9-entry.txt
54. uniprot-q6zp65-entry.txt
55. urnavicius-2018-two-dyneins-abstract.md
56. urnavicius-2018-two-dyneins-fulltext.txt
57. urnavicius-2018-two-dyneins-summary.md
58. vazquezpianzola-2024-bicdr-bristle-abstract.md
59. vazquezpianzola-2024-bicdr-bristle-fulltext.txt
60. vazquezpianzola-2024-bicdr-bristle-summary.md
61. verma-2026-dynein-living-cells-abstract.md
62. verma-2026-dynein-living-cells-fulltext.txt
63. verma-2026-dynein-living-cells-summary.md