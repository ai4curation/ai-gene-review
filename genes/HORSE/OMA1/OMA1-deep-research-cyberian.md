---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:22:37.435334'
end_time: '2026-10-26T03:36:11.233917'
duration_seconds: 813.8
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: OMA1
  gene_symbol: OMA1
  uniprot_accession: A0A9L0R9P8
  protein_description: 'RecName: Full=Metalloendopeptidase OMA1, mitochondrial {ECO:0000256|ARBA:ARBA00040360};
    AltName: Full=Overlapping with the m-AAA protease 1 homolog {ECO:0000256|ARBA:ARBA00042978};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the peptidase M48 family.
  protein_domains: Mito/Outer_Membr_Metalloprot. (IPR051156); Peptidase_M48. (IPR001915);
    Peptidase_M48 (PF01435)
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
citation_count: 89
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0R9P8
- **Protein Description:** RecName: Full=Metalloendopeptidase OMA1, mitochondrial {ECO:0000256|ARBA:ARBA00040360}; AltName: Full=Overlapping with the m-AAA protease 1 homolog {ECO:0000256|ARBA:ARBA00042978};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the peptidase M48 family.
- **Key Domains:** Mito/Outer_Membr_Metalloprot. (IPR051156); Peptidase_M48. (IPR001915); Peptidase_M48 (PF01435)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "OMA1" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'OMA1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **OMA1** (gene ID: OMA1, UniProt: A0A9L0R9P8) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# OMA1 (Metalloendopeptidase OMA1, mitochondrial) in the horse, *Equus caballus* (UniProt A0A9L0R9P8)

## Introduction and summary

UniProt A0A9L0R9P8 is an unreviewed (TrEMBL) protein of 513 residues from the domestic horse. It was predicted by Ensembl from the Thoroughbred reference genome (gene ENSECAG00000009131, chromosome 2) and is annotated by automatic rules as "Metalloendopeptidase OMA1, mitochondrial" (alternative name: "Overlapping with the m-AAA protease 1 homolog"), a member of the peptidase M48 family [uniprot-A0A9L0R9P8; wade-2009-horse-genome-abstract]. No experimental study of horse OMA1 exists. Everything below about function is inferred from the well-studied orthologues in budding yeast, mouse and human cells, using the sequence evidence assembled for this report. On that evidence the identity of the protein is not in doubt. The horse sequence has the M48 zinc-metalloprotease domain with an intact HExxH motif (HEIAH, residues 319–323), a single predicted transmembrane helix (residues 187–205), and an N-terminal mitochondrial targeting region. It is 68.8% identical to reviewed human OMA1 (Q96E52) over the aligned positions and 60.2% identical to mouse Oma1 (Q9D8H7) (notes/alignment_horse_vs_human_mouse.txt). The symbol is not ambiguous. Every paper retrieved concerns the same conserved M48 protease of the mitochondrial inner membrane.

The orthologues define OMA1 as an ATP-independent, zinc-dependent endopeptidase anchored in the mitochondrial inner membrane. It was found in yeast as a protease whose activities overlap with the m-AAA protease in degrading misfolded inner-membrane proteins [kaser-2003-oma1-yeast-abstract]. In mammals its best-characterised job is stress-induced cleavage of the dynamin-like GTPase OPA1 at the S1 site. This converts fusion-competent long OPA1 (L-OPA1) into short soluble forms (S-OPA1), which stops inner-membrane fusion and fragments mitochondria when membrane potential, ATP or redox balance is disturbed [head-2009-oma1-opa1-inactivation-fulltext; ehses-2009-opa1-processing-oma1-fulltext; anand-2014-yme1l-oma1-opa1-fulltext]. OMA1 is mostly dormant in healthy mitochondria. Under stress it becomes strongly active and then cleaves itself to destruction, so the response switches off once the insult passes [baker-2014-oma1-autocatalytic-abstract; zhang-2014-oma1-self-cleavage-abstract]. Its second major role is signalling. Stress-activated OMA1 cleaves the inner-membrane protein DELE1, and the cleaved DELE1 moves to the cytosol, binds the eIF2α kinase HRI and switches on the integrated stress response (ISR) [guo-2020-oma1-dele1-hri-fulltext; fessler-2020-dele1-pathway-abstract]. OMA1 also helps release cytochrome c in apoptosis [jiang-2014-oma1-bax-bak-abstract], works as a backup protease for PINK1 [sekine-2019-tom7-oma1-pink1-abstract], cleaves the bc1-complex assembly factor UQCC3 [desmurs-2015-c11orf83-uqcc3-abstract], and supports respiratory supercomplexes and MICOS-dependent cristae architecture [bohovych-2015-oma1-supercomplexes-fulltext; viana-2021-oma1-micos-fulltext]. In mice it matters for whole-body energy balance and thermogenesis [quiros-2012-oma1-knockout-obesity-abstract]. Recent work shows that OMA1 also relays haem deficiency to HRI [zhang-2026-haem-oma1-dele1-fulltext]. In vivo, its activation can either drive cardiomyocyte death [acin-perez-2018-oma1-heart-failure-abstract] or protect against mitochondrial disease through the ISR [shammas-2022-oma1-chchd10-fulltext; ahola-2022-oma1-isr-ferroptosis-abstract], depending on context.

One caveat about this particular horse record needs stating up front. Its C-terminal ~110 residues (from about residue 400) do not match the conserved C-terminal segment found in human OMA1 and in two other horse OMA1 entries (A0A3Q2KVR1 and F6YE56). Those two entries are 88.8–91.1% identical to A0A9L0R9P8 elsewhere and keep the conserved "…AKACVDVRASSVFWQQMEF…WLSTHPSHG…" sequence that A0A9L0R9P8 lacks (notes/horse_isoform_comparison.txt). A0A9L0R9P8 is therefore probably an alternatively spliced isoform or a mispredicted gene model with an aberrant C-terminal exon, rather than the canonical horse OMA1. This affects interpretation, because the C-terminal region of the orthologues has been linked to stress-triggered activation, redox regulation and autocatalytic processing (see the section on activation and regulation below).

## Identity, domain architecture and evolutionary context

OMA1 was named in yeast for its activities "overlapping with the m-AAA protease." It was proposed as the founding member of a conserved family of membrane-embedded metallopeptidases with homologues in eukaryotes, eubacteria and archaea [kaser-2003-oma1-yeast-abstract]. The human orthologue was first cloned as "metalloprotease-related protein-1" (MPRP-1). It was described as a hydrophobic protein with a HEXXH zinc-metalloprotease motif, expressed in many organs and most strongly in heart, skeletal muscle, kidney and liver [bao-2003-human-oma1-cdna-abstract]. That study placed it in the endoplasmic reticulum, a conclusion that later work overturned in favour of the mitochondrial inner membrane, as UniProt's curated human entry notes [head-2009-oma1-opa1-inactivation-fulltext; uniprot-A0A9L0R9P8].

OMA1 belongs to the M48 (Ste24/ZMPSTE24-like) family of zincin metalloproteases. Alavi's biochemical review built a homology model of the OMA1 active site on M48 structures and argued from the ZMPSTE24 homology that OMA1 is a true integral membrane protease [alavi-2021-oma1-integral-membrane-abstract]. The horse sequence fits this family assignment. Pfam PF01435 (Peptidase_M48) covers residues 255–409, the CDD model is M48C_Oma1_like (cd07331), and the PANTHER subfamily is PTHR22726:SF1, "metalloendopeptidase OMA1, mitochondrial" [uniprot-A0A9L0R9P8]. Within the catalytic domain the horse sequence keeps the HEIAH zinc-binding motif (H319-E320-x-x-H323). The first histidine aligns with yeast Oma1 His203, whose H203A substitution abolishes catalysis in yeast (notes/alignment_horse_vs_yeast.txt) [bohovych-2015-oma1-supercomplexes-fulltext]. A conserved "LEAEAD" segment (residues ~383–388) downstream likely supplies the third zinc ligand typical of M48 enzymes. This last point is inferred from family structure and has not been tested in OMA1.

The N-terminal part of the protein is less conserved between species. A 2014 study identified an N-terminal stress-sensor domain in mammalian OMA1 that is "only present in homologues of higher eukaryotes" and that modulates OMA1 proteolysis and activation [baker-2014-oma1-autocatalytic-abstract]. The horse sequence keeps the positively charged segment "KWWQALPPNKKE…KKNKWK" immediately before the transmembrane helix, which is almost identical in human and mouse (notes/alignment_horse_vs_human_mouse.txt). A later review describes this positively charged N-terminal region as necessary for OPA1 cleavage after loss of membrane potential [gilkerson-2021-oma1-opa1-gatekeepers-fulltext]. A cardiolipin-binding region that controls OMA1 turnover has also been mapped in neurons [anderson-2020-prohibitin-oma1-abstract]. The horse residues have not been mapped to it directly, but the high conservation of this region suggests the function is kept.

## Catalytic activity and substrate specificity

OMA1 is a zinc-dependent endopeptidase. Unlike the AAA proteases of the inner membrane (the matrix-facing m-AAA protease AFG3L2/SPG7 and the IMS-facing i-AAA protease YME1L), it cleaves without ATP. In yeast, when the m-AAA protease is absent, Oma1 degrades a misfolded variant of the polytopic inner-membrane protein Oxa1 in an ATP-independent manner. Its cleavage sites map to loops on both sides of the membrane [kaser-2003-oma1-yeast-abstract]. This ATP independence is central to how OMA1 works physiologically. Ehses and colleagues showed that the membrane-permeable metal chelator o-phenanthroline blocks OPA1 processing. They proposed that the ATP-dependent m-AAA protease maintains the constitutive balance of long and short OPA1 forms, while OMA1, "acting in an ATP-independent manner, completely converts long OPA1 isoforms into short forms under stress conditions" [ehses-2009-opa1-processing-oma1-fulltext]. OMA1 therefore stays active in exactly the situations, depolarisation and ATP depletion, in which ATP-dependent proteases fail. Rainbolt and colleagues showed that insults which both depolarise mitochondria and deplete ATP stabilise active OMA1 while promoting YME1L degradation [rainbolt-2016-yme1l-oma1-reciprocal-abstract].

No strict cleavage consensus has been defined for OMA1. Its substrate preference looks driven by conformation and context more than by sequence. In yeast, Oma1 degrades the Cox1 subunit of cytochrome c oxidase selectively in coa2Δ cells, where Cox1 is hypohemylated and misfolded. It does not do so in other assembly mutants in which Oma1 is just as active, which led the authors to conclude that substrate selection needs "a combination of Oma1 activation and a susceptible conformation" of the target [khalimonchuk-2012-oma1-cox1-abstract]. In mammals the substrates with the best evidence are OPA1, cleaved at S1 in exon 5, which is present in all OPA1 splice isoforms [head-2009-oma1-opa1-inactivation-fulltext; anand-2014-yme1l-oma1-opa1-fulltext], and DELE1, whose OMA1-dependent cleavage was not affected by a series of short deletions between DELE1 residues 73 and 149 [guo-2020-oma1-dele1-hri-fulltext]. Other reported substrates are UQCC3 (C11orf83), cleaved on depolarisation [desmurs-2015-c11orf83-uqcc3-abstract], and PINK1, which OMA1 cleaves when PINK1 fails to arrest at the outer membrane and is imported into depolarised mitochondria [sekine-2019-tom7-oma1-pink1-abstract]. OMA1 also processes itself (autocatalysis), as described below. The reaction in all these cases is hydrolysis of internal peptide bonds of membrane-associated proteins (EC 3.4.24.-), consistent with the GO term "metalloendopeptidase activity" (GO:0004222) transferred to the horse entry [uniprot-A0A9L0R9P8].

## Subcellular localisation and membrane topology

Studies of the orthologues consistently place OMA1 in the mitochondrial inner membrane. In human and mouse cells it cleaves the intermembrane-space-resident OPA1 and is degraded by the IMS-facing i-AAA protease YME1L [head-2009-oma1-opa1-inactivation-fulltext; ehses-2009-opa1-processing-oma1-fulltext; rainbolt-2016-yme1l-oma1-reciprocal-abstract]. Its cleavage of DELE1 happens in mitochondria before DELE1 moves to the cytosol [guo-2020-oma1-dele1-hri-fulltext]. The horse entry correspondingly carries the cellular-component annotations mitochondrial inner membrane (GO:0005743; IBA) and mitochondrial intermembrane space (GO:0005758; IEA), and is predicted to be a single-pass membrane protein with an N-terminal transit peptide [uniprot-A0A9L0R9P8]. Biogenesis involves several processing steps. After import, a ~60 kDa pre-pro-OMA1 is matured to a ~40 kDa pro-OMA1 mainly by the m-AAA protease AFG3L2, which cuts off the N-terminal portion without recognising a specific consensus sequence [consolato-2018-aaa-oma1-abstract]. Head and colleagues had already seen 40 kDa and 60 kDa OMA1 species that changed with CCCP treatment [head-2009-oma1-opa1-inactivation-fulltext].

The topology of the catalytic domain has been debated. The original yeast study reported that Oma1 exposes its proteolytic centre to the matrix side, although it cut Oxa1 on both membrane surfaces [kaser-2003-oma1-yeast-abstract]. More recent mammalian and yeast work describes the C-terminal M48 domain as facing the IMS and the N-terminal stress-sensor domain as facing the matrix [gilkerson-2021-oma1-opa1-gatekeepers-fulltext]. In yeast, the redox-active cysteines that regulate the Oma1 complex are described as IMS-exposed [bohovych-2019-oma1-redox-abstract]. An IMS-facing catalytic domain fits the location of the main substrates OPA1 and DELE1. Alavi's review argues that OMA1 may be an integral (intramembrane) protease rather than one simply tethered to the membrane [alavi-2021-oma1-integral-membrane-abstract]. Without an experimental structure the exact topology and depth of the active site remain unresolved.

## Role in mitochondrial dynamics: OPA1 processing

The best-established function of OMA1 is regulating inner-membrane fusion through OPA1. OPA1 exists as long, membrane-anchored isoforms (L-OPA1) and short isoforms (S-OPA1) produced by cleavage at two sites, S1 and S2. OMA1 cleaves S1 and YME1L cleaves S2 [head-2009-oma1-opa1-inactivation-fulltext; anand-2014-yme1l-oma1-opa1-fulltext; gilkerson-2021-oma1-opa1-gatekeepers-fulltext]. In 2009, two groups independently found OMA1 to be the protease behind inducible OPA1 processing. Head and colleagues showed that OMA1, a protease with a zinc-binding motif, mediates the stress-induced proteolytic inactivation of OPA1 [head-2009-oma1-opa1-inactivation-fulltext]. Ehses and colleagues showed that m-AAA protease isoenzymes and OMA1 together regulate OPA1 processing, with OMA1 converting long to short forms completely under stress [ehses-2009-opa1-processing-oma1-fulltext]. Genetic analysis in knockout mouse embryonic fibroblasts then showed that the S-OPA1 forms c and e are missing in Oma1−/− cells. It also showed that L-OPA1 alone suffices for mitochondrial fusion and normal cristae, while S-OPA1 is associated with fission [anand-2014-yme1l-oma1-opa1-fulltext]. Reconstitution studies later refined this picture. L-OPA1 can dock membranes and drive hemifusion, and S-OPA1 cooperates with it to complete inner-membrane fusion [ge-2020-two-forms-opa1-fulltext]. By turning L-OPA1 into S-OPA1, OMA1 therefore acts as a stress-activated brake on fusion, matching the GO terms "negative regulation of mitochondrial fusion" and "regulation of cristae formation" on the horse entry [uniprot-A0A9L0R9P8].

The physiological weight of this OMA1-OPA1 axis has been shown in mice. Oma1-deficient mice are viable but have defective OPA1 processing, a disturbed fusion-fission balance, increased adiposity, hepatic steatosis, lower energy expenditure and impaired thermogenesis, all most obvious under high-fat feeding or cold [quiros-2012-oma1-knockout-obesity-abstract]. When YME1L is deleted from the heart, OMA1 is activated, OPA1 proteolysis speeds up and mitochondria fragment, leading to dilated cardiomyopathy and heart failure. Deleting Oma1 rescues both cardiac function and mitochondrial morphology [wai-2015-opa1-heart-failure-abstract]. In neurons lacking prohibitin PHB2, loss of OMA1 prevents stress-induced OPA1 processing and delays neurodegeneration [korwitz-2016-oma1-neurodegeneration-fulltext]. The two inner-membrane proteases also regulate each other. OMA1 is degraded through YME1L when mitochondria are depolarised, while combined depolarisation and ATP depletion stabilise OMA1 and drive YME1L degradation [rainbolt-2016-yme1l-oma1-reciprocal-abstract]. The m-AAA and i-AAA complexes together control OMA1 processing and turnover [consolato-2018-aaa-oma1-abstract]. These results come from mouse and human cells. Horse OMA1 is predicted to behave the same way, but this is untested.

## Activation, autocatalysis and regulation

OMA1 works as a stress sensor. It is constitutively active at a low level but becomes much more active after many different insults, including loss of membrane potential, oxidative stress and other mitochondrial damage [baker-2014-oma1-autocatalytic-abstract; bohovych-2014-oma1-c-terminal-abstract]. Activation is linked to autocatalytic cleavage. On depolarisation OMA1 cleaves itself into a short form (S-OMA1) that is degraded quickly, and this processing correlates with OPA1 cleavage at S1 [zhang-2014-oma1-self-cleavage-abstract]. Baker and colleagues found that the autocatalytic degradation starts from both ends of OMA1 and ends in complete turnover of the protease. This makes the response reversible, so OPA1-mediated fusion can resume once the stress resolves [baker-2014-oma1-autocatalytic-abstract]. They also identified the N-terminal stress-sensor domain, specific to higher eukaryotes, that modulates this activation [baker-2014-oma1-autocatalytic-abstract].

Several further layers of regulation have been described. In yeast, stress-induced Oma1 activity involves conformational changes in the Oma1 homo-oligomeric complex that depend on conserved C-terminal residues [bohovych-2014-oma1-c-terminal-abstract]. Oma1 exists in a semi-oxidised state in yeast and mammalian mitochondria. Its activity and the stability of its oligomeric complex are tuned by a disulfide between two conserved IMS-exposed cysteines, Cys272 and Cys332 in yeast [bohovych-2019-oma1-redox-abstract]. The prohibitin complex promotes OMA1 turnover, and OMA1 binds cardiolipin. Deleting the cardiolipin-binding region slows OMA1 turnover, which suggests prohibitins regulate OMA1 through cardiolipin [anderson-2020-prohibitin-oma1-abstract]. Prohibitin knockdown also stabilises S-OMA1 [zhang-2014-oma1-self-cleavage-abstract].

These regulatory elements bear directly on the horse record. Aligning horse A0A9L0R9P8 with yeast Oma1 puts yeast Cys272 at horse Cys408, on the edge of the divergent C-terminal segment. Yeast Cys332 and the downstream C-terminal region have no counterpart in this horse model (notes/alignment_horse_vs_yeast.txt). The C-terminal region of mammalian OMA1 also carries the autocatalytic processing site that UniProt transfers to human OMA1 from mouse, at residues 447–456 [uniprot-A0A9L0R9P8]. Because A0A9L0R9P8 replaces the conserved C-terminal segment with an unrelated sequence that the other horse OMA1 models (A0A3Q2KVR1, F6YE56) lack, this isoform may differ from canonical OMA1 in redox control, oligomer stability or autocatalytic turnover. It could even be non-functional or not expressed. This prediction rests on sequence analysis alone.

## Signalling functions: the OMA1–DELE1–HRI pathway, apoptosis and other substrates

Two 2020 studies showed that OMA1 does more than control morphology: it relays mitochondrial stress to the cytosol. Using CRISPR screens with an ATF4 reporter, Guo and colleagues found that mitochondrial stress triggers OMA1-dependent cleavage of DELE1 into a short form (DELE1S). DELE1S accumulates in the cytosol, where it binds HRI and activates its eIF2α-kinase activity. HRI was both necessary and sufficient for this relay [guo-2020-oma1-dele1-hri-fulltext]. Fessler and colleagues used haploid genetics and a CHOP reporter and independently identified OMA1, DELE1 and HRI as the missing pathway. They showed that the C-terminal portion of cleaved DELE1 binds and activates HRI, and that blocking the pathway can help or harm depending on the type of mitochondrial perturbation [fessler-2020-dele1-pathway-abstract]. Through this pathway OMA1 links mitochondrial dysfunction to eIF2α phosphorylation and the ISR, consistent with the "HRI-mediated signaling" annotation transferred to the horse protein [uniprot-A0A9L0R9P8]. Later work refined how DELE1 is handled and widened the inputs the axis responds to. Zhang and colleagues describe OMA1 cleaving DELE1 during its import, which sends DELE1 to the cytosol. They also showed that haem scarcity, caused by inhibiting haem synthesis pharmacologically or by genetic loss of ferrochelatase (FECH), activates HRI only when OMA1 and DELE1 are present, in every human cell system they tested. In the cytosol DELE1 releases inhibitory haem from HRI [zhang-2026-haem-oma1-dele1-fulltext]. This suggests that HRI's long-recognised response to haem deficiency is at least partly routed through mitochondria by OMA1 [zhang-2026-haem-oma1-dele1-fulltext]. The relationship is not simple, though. In iron deficiency, DELE1 can signal to HRI by a different route: its import into mitochondria stalls, so it is no longer degraded by the matrix protease LONP1 and builds up on the mitochondrial surface [sekine-2023-dele1-iron-abstract]. DELE1 relay therefore has both OMA1-cleavage-dependent and import-arrest-dependent modes, and which one dominates depends on the stress.

OMA1 also takes part in intrinsic apoptosis. After BAX and BAK oligomerise, OMA1 is activated in a BAX/BAK-dependent manner and cleaves OPA1. This remodels cristae, and knocking down or knocking out OMA1 reduces cytochrome c release [jiang-2014-oma1-bax-bak-abstract]. In line with this, Oma1−/− fibroblasts are less sensitive to H2O2-induced apoptosis [anand-2014-yme1l-oma1-opa1-fulltext], and OMA1 loss protects prohibitin-deficient cells from apoptosis [korwitz-2016-oma1-neurodegeneration-fulltext]. OMA1's other substrates tie it to quality control and bioenergetics. It cleaves the cardiolipin-binding bc1-assembly factor UQCC3 on depolarisation [desmurs-2015-c11orf83-uqcc3-abstract], and it cleaves PINK1 that has been imported into depolarised mitochondria, in a "tug of war" with Tom7 that decides whether PINK1 builds up on the outer membrane to start mitophagy [sekine-2019-tom7-oma1-pink1-abstract]. Independently of its protease function on OPA1, OMA1 is needed for respiratory supercomplex stability in yeast and mouse fibroblasts [bohovych-2015-oma1-supercomplexes-fulltext]. It also associates dynamically with the MICOS complex through MIC60, independently of OPA1, which supports inner-outer membrane contacts, bioenergetic output and apoptosis [viana-2021-oma1-micos-fulltext]. Reviews describe OMA1 as a central inner-membrane quality-control protease and, together with OPA1, a "gatekeeper" of mitochondrial structure and the cellular stress response [levytskyy-2017-imm-metalloproteases-abstract; gilkerson-2021-oma1-opa1-gatekeepers-fulltext].

## OMA1 as a stress sentinel in vivo: disease models, evolution and pharmacology

Genetic studies in mice show that whether OMA1 activation helps or harms depends on context, and these results clarify what the protease actually does. In some settings activation is maladaptive. In three different mouse models of heart failure (tachycardiomyopathy, heart failure with preserved ejection fraction, and ischaemia with hypertrophy), more mitochondrial reactive oxygen species were followed by cristae damage and cardiomyocyte death, and ablating OMA1 prevented that death in all three [acin-perez-2018-oma1-heart-failure-abstract]. The same pattern holds when YME1L is lost from the heart [wai-2015-opa1-heart-failure-abstract]. In primary mitochondrial disease, by contrast, OMA1 is protective. In knock-in mice carrying the myopathy-causing CHCHD10 G58R mutation, aggregated CHCHD10 stresses the inner membrane and activates OMA1 in every tissue examined. Activation shows up as loss of L-OPA1 bands a and b and gain of the OMA1-generated S-OPA1 bands c and e. Survival of these mice depends on OMA1, which acts locally by fragmenting mitochondria and globally by cleaving DELE1 to induce the ISR [shammas-2022-oma1-chchd10-fulltext]. Likewise, in mice lacking the cytochrome c oxidase assembly factor Cox10 in the heart, Oma1 drives an Oma1–Dele1–Atf4 ISR. Deleting Oma1 or Dele1 makes the cardiomyopathy worse, because without the ISR glutathione metabolism and selenium-dependent Gpx4 accumulation fail and the heart undergoes ferroptosis [ahola-2022-oma1-isr-ferroptosis-abstract]. AFG3L2 loss, which also matures OMA1 in normal cells [consolato-2018-aaa-oma1-abstract], over-activates OMA1. This raises OMA1-dependent DELE1 processing and ISR signalling in fibroblasts from patients with spastic ataxia type 5 and in the Afg3l2−/− mouse cerebellum, and silencing DELE1 or HRI harms the patient cells [franchino-2024-oma1-isr-spax5-fulltext]. Taken together, OMA1's main role in vivo is to convert inner-membrane proteotoxic or bioenergetic stress into two outputs: remodelling of the mitochondrial network through OPA1, and remodelling of cytosolic translation through DELE1–HRI.

Two further findings separate OMA1's functions. First, the OPA1 and DELE1 arms can be uncoupled. In lymphoma cells treated with the OMA1-activating compound BTM-3566, ISR activation was lost in OMA1- and DELE1-knockout cells but kept in cells whose OPA1 lacks the S1 site [schwarzer-2023-oma1-activation-lymphoma-fulltext]. That study also identified the mitochondrial protein FAM210B as a negative regulator of OMA1 activation by these compounds [schwarzer-2023-oma1-activation-lymphoma-fulltext]. An earlier cell-based screen with an engineered inner-membrane luciferase substrate found both activators and inhibitors of OMA1, including ten kinase-targeted cancer drugs that triggered OMA1 activity [alavi-2021-oma1-hts-abstract]. Second, OMA1 has a pro-survival role after nuclear DNA damage that does not need OMA1 activation or cleavage of OPA1 or DELE1. OMA1-deficient cells show less glycolysis, accumulate OXPHOS proteins and are more prone to p53-dependent apoptosis under nucleotide deficiency [rivera-mejias-2023-oma1-dna-damage-abstract]. This points to a function of unknown mechanism, possibly non-catalytic.

Evolution places the signalling role of OMA1 deep in animal history. Zhang and colleagues report that OMA1 is conserved down to fungi. DELE1 and HRI are missing from yeast, *Drosophila* and *C. elegans* but have structural relatives in bloodless invertebrates such as *Hydra vulgaris*, and the hydra orthologues of OMA1, DELE1 and HRI can rebuild the human haem-sensing circuit in human cells [zhang-2026-haem-oma1-dele1-fulltext]. So the proteolytic quality-control function of the M48 protease is ancient and shared with yeast [kaser-2003-oma1-yeast-abstract], while its coupling to DELE1–HRI signalling arose in the animal lineage, long before haemoglobin. A horse orthologue would be expected to keep both functions.

## Synthesis for the horse protein

Taken together, the evidence supports the following functional annotation for horse A0A9L0R9P8, all of it inferred by orthology and none experimental for the horse. The protein is predicted to be a zinc-dependent, ATP-independent M48 metalloendopeptidase of the mitochondrial inner membrane, with its catalytic domain probably facing the intermembrane space. It is predicted to stay largely latent under normal conditions and to be activated by depolarisation, ATP depletion, oxidative stress or pro-apoptotic BAX/BAK signalling. Once active it would cleave L-OPA1 at S1, stopping fusion and remodelling cristae. It would also cleave DELE1 to start HRI-dependent integrated stress signalling, and possibly cleave PINK1 and UQCC3, before switching itself off by autocatalytic degradation. The catalytic core of the horse model (transmembrane helix, positively charged N-terminal stress-sensor region, HEIAH motif and LEAEAD segment) is highly conserved with human and mouse, so the predicted enzymatic activity is well supported. The divergent C-terminus of this particular record is the main uncertainty. Other horse OMA1 records with a canonical C-terminus (A0A3Q2KVR1, F6YE56) are probably better representatives of the main horse gene product. Whether the A0A9L0R9P8 isoform is expressed, and whether it is regulated normally, cannot be settled with current data.

## Open Questions

The most pressing question for this record is whether A0A9L0R9P8 corresponds to a real horse transcript. The alternative C-terminal exon could be checked against horse RNA-seq or long-read transcript data (for example the Ensembl/FAANG horse annotations) to tell genuine alternative splicing apart from a gene-model error. If the isoform is real, a useful test would be whether it is still processed by AFG3L2 [consolato-2018-aaa-oma1-abstract], whether it autocatalytically turns over on depolarisation [baker-2014-oma1-autocatalytic-abstract; zhang-2014-oma1-self-cleavage-abstract], and whether it forms the redox-regulated oligomer described for yeast and mammalian OMA1 [bohovych-2019-oma1-redox-abstract]. That could be done by expressing it in Oma1−/− mouse fibroblasts, a system already used to dissect OPA1 processing [anand-2014-yme1l-oma1-opa1-fulltext].

More broadly, OMA1 still has no experimental three-dimensional structure. The topology of its catalytic domain and its cleavage rules remain debated [alavi-2021-oma1-integral-membrane-abstract; kaser-2003-oma1-yeast-abstract], and the exact mechanism by which the N-terminal stress-sensor domain detects loss of membrane potential is unknown [baker-2014-oma1-autocatalytic-abstract]. A cryo-EM structure of the OMA1 oligomer in its latent and activated states, combined with cleavage-site proteomics, would address both. In the horse, OMA1 may also have physiological relevance. Given its role in thermogenesis and energy expenditure in mice [quiros-2012-oma1-knockout-obesity-abstract], in cardiomyocyte survival [wai-2015-opa1-heart-failure-abstract] and in the integrated stress response [guo-2020-oma1-dele1-hri-fulltext], horse-specific questions such as variation in OMA1 or OPA1 processing in equine metabolic syndrome, exertional myopathies or the highly oxidative muscle of athletic breeds would be worth exploring. No such equine studies were found in this search. Haem sensing raises a further question. The OMA1–DELE1 axis senses haem scarcity in human erythroid progenitors [zhang-2026-haem-oma1-dele1-fulltext], and the horse has an unusually large erythrocyte reserve and high erythropoietic demand, so equine OMA1 could plausibly take part in erythroid stress responses; this has not been tested. Finally, it remains unclear how much of OMA1's DNA-damage-protective role is independent of its catalytic activity [rivera-mejias-2023-oma1-dna-damage-abstract], and how FAM210B restrains OMA1 activation [schwarzer-2023-oma1-activation-lymphoma-fulltext]. It is also unknown what decides whether DELE1 reaches the cytosol by OMA1 cleavage or by import arrest [sekine-2023-dele1-iron-abstract]. Each of these bears on what the predicted horse enzyme does in vivo.

## References

- [uniprot-A0A9L0R9P8] UniProt Consortium. UniProtKB entry A0A9L0R9P8_HORSE, "Metalloendopeptidase OMA1, mitochondrial", *Equus caballus*, entry version 15 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0R9P8.txt (local copy: notes/uniprot_A0A9L0R9P8.txt). Comparative entries: human Q96E52, mouse Q9D8H7, yeast P36163, horse A0A3Q2KVR1 and F6YE56 (https://rest.uniprot.org/uniprotkb/).
- [wade-2009-horse-genome] Wade CM, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science* 2009;326:865-867. PMID: 19892987; PMCID: PMC3785132; DOI: 10.1126/science.1178158.
- [kaser-2003-oma1-yeast] Kaser M, Kambacheld M, Kisters-Woike B, Langer T. Oma1, a novel membrane-bound metallopeptidase in mitochondria with activities overlapping with the m-AAA protease. *J Biol Chem* 2003. PMID: 12963738; DOI: 10.1074/jbc.M305584200.
- [bao-2003-human-oma1-cdna] Bao YC, et al. Identification of a human cDNA sequence which encodes a novel membrane-associated protein containing a zinc metalloprotease motif. *DNA Res* 2003. PMID: 12886954; DOI: 10.1093/dnares/10.3.123.
- [head-2009-oma1-opa1-inactivation] Head B, Griparic L, Amiri M, Gandre-Babbe S, van der Bliek AM. Inducible proteolytic inactivation of OPA1 mediated by the OMA1 protease in mammalian cells. *J Cell Biol* 2009. PMID: 20038677; PMCID: PMC2806274; DOI: 10.1083/jcb.200906083.
- [ehses-2009-opa1-processing-oma1] Ehses S, et al. Regulation of OPA1 processing and mitochondrial fusion by m-AAA protease isoenzymes and OMA1. *J Cell Biol* 2009. PMID: 20038678; PMCID: PMC2806285; DOI: 10.1083/jcb.200906084.
- [quiros-2012-oma1-knockout-obesity] Quirós PM, et al. Loss of mitochondrial protease OMA1 alters processing of the GTPase OPA1 and causes obesity and defective thermogenesis in mice. *EMBO J* 2012. PMID: 22433842; PMCID: PMC3343468; DOI: 10.1038/emboj.2012.70.
- [anand-2014-yme1l-oma1-opa1] Anand R, et al. The i-AAA protease YME1L and OMA1 cleave OPA1 to balance mitochondrial fusion and fission. *J Cell Biol* 2014. PMID: 24616225; PMCID: PMC3998800; DOI: 10.1083/jcb.201308006.
- [baker-2014-oma1-autocatalytic] Baker MJ, et al. Stress-induced OMA1 activation and autocatalytic turnover regulate OPA1-dependent mitochondrial dynamics. *EMBO J* 2014. PMID: 24550258; PMCID: PMC3989652; DOI: 10.1002/embj.201386474.
- [zhang-2014-oma1-self-cleavage] Zhang K, Li H, Song Z. Membrane depolarization activates the mitochondrial protease OMA1 by stimulating self-cleavage. *EMBO Rep* 2014;15(5):576-85. PMID: 24719224; PMCID: PMC4210089; DOI: 10.1002/embr.201338240.
- [khalimonchuk-2012-oma1-cox1] Khalimonchuk O, Jeong MY, Watts T, Ferris E, Winge DR. Selective Oma1 protease-mediated proteolysis of Cox1 subunit of cytochrome oxidase in assembly mutants. *J Biol Chem* 2012. PMID: 22219186; PMCID: PMC3293553; DOI: 10.1074/jbc.M111.313148.
- [bohovych-2014-oma1-c-terminal] Bohovych I, et al. Stress-triggered activation of the metalloprotease Oma1 involves its C-terminal region and is important for mitochondrial stress protection in yeast. *J Biol Chem* 2014. PMID: 24648523; PMCID: PMC4036336; DOI: 10.1074/jbc.M113.542910.
- [bohovych-2015-oma1-supercomplexes] Bohovych I, et al. Metalloprotease OMA1 fine-tunes mitochondrial bioenergetic function and respiratory supercomplex stability. *Sci Rep* 2015. PMID: 26365306; PMCID: PMC4568518; DOI: 10.1038/srep13989.
- [bohovych-2019-oma1-redox] Bohovych I, Dietz JV, Swenson S, Zahayko N, Khalimonchuk O. Redox regulation of the mitochondrial quality control protease Oma1. *Antioxid Redox Signal* 2019. PMID: 31044600; PMCID: PMC6653804; DOI: 10.1089/ars.2018.7642.
- [consolato-2018-aaa-oma1] Consolato F, Maltecca F, Tulli S, Sambri I, Casari G. m-AAA and i-AAA complexes coordinate to regulate OMA1, the stress-activated supervisor of mitochondrial dynamics. *J Cell Sci* 2018. PMID: 29545505; DOI: 10.1242/jcs.213546.
- [jiang-2014-oma1-bax-bak] Jiang X, Jiang H, Shen Z, Wang X. Activation of mitochondrial protease OMA1 by Bax and Bak promotes cytochrome c release during apoptosis. *Proc Natl Acad Sci U S A* 2014. PMID: 25275009; PMCID: PMC4205663; DOI: 10.1073/pnas.1417253111.
- [desmurs-2015-c11orf83-uqcc3] Desmurs M, et al. C11orf83, a mitochondrial cardiolipin-binding protein involved in bc1 complex assembly and supercomplex stabilization. *Mol Cell Biol* 2015. PMID: 25605331; PMCID: PMC4355537; DOI: 10.1128/MCB.01047-14.
- [sekine-2019-tom7-oma1-pink1] Sekine S, et al. Reciprocal roles of Tom7 and OMA1 during mitochondrial import and activation of PINK1. *Mol Cell* 2019. PMID: 30733118; DOI: 10.1016/j.molcel.2019.01.002.
- [ge-2020-two-forms-opa1] Ge Y, et al. Two forms of Opa1 cooperate to complete fusion of the mitochondrial inner-membrane. *eLife* 2020. PMID: 31922487; PMCID: PMC7299343; DOI: 10.7554/eLife.50973.
- [fessler-2020-dele1-pathway] Fessler E, et al. A pathway coordinated by DELE1 relays mitochondrial stress to the cytosol. *Nature* 2020;579:433-437. PMID: 32132706; PMCID: PMC7116715; DOI: 10.1038/s41586-020-2076-4.
- [guo-2020-oma1-dele1-hri] Guo X, et al. Mitochondrial stress is relayed to the cytosol by an OMA1-DELE1-HRI pathway. *Nature* 2020. PMID: 32132707; PMCID: PMC7147832; DOI: 10.1038/s41586-020-2078-2.
- [rainbolt-2016-yme1l-oma1-reciprocal] Rainbolt TK, Lebeau J, Puchades C, Wiseman RL. Reciprocal degradation of YME1L and OMA1 adapts mitochondrial proteolytic activity during stress. *Cell Rep* 2016. PMID: 26923599; PMCID: PMC4785047; DOI: 10.1016/j.celrep.2016.02.011.
- [korwitz-2016-oma1-neurodegeneration] Korwitz A, et al. Loss of OMA1 delays neurodegeneration by preventing stress-induced OPA1 processing in mitochondria. *J Cell Biol* 2016. PMID: 26783299; PMCID: PMC4738383; DOI: 10.1083/jcb.201507022.
- [wai-2015-opa1-heart-failure] Wai T, et al. Imbalanced OPA1 processing and mitochondrial fragmentation cause heart failure in mice. *Science* 2015;350(6265). PMID: 26785494; DOI: 10.1126/science.aad0116.
- [alavi-2021-oma1-integral-membrane] Alavi MV. OMA1—An integral membrane protease? *Biochim Biophys Acta Proteins Proteom* 2021. PMID: 33130089; PMCID: PMC7770061; DOI: 10.1016/j.bbapap.2020.140558.
- [gilkerson-2021-oma1-opa1-gatekeepers] Gilkerson R, et al. Mitochondrial OMA1 and OPA1 as gatekeepers of organellar structure/function and cellular stress response. *Front Cell Dev Biol* 2021. PMID: 33842456; PMCID: PMC8027119; DOI: 10.3389/fcell.2021.626117.
- [levytskyy-2017-imm-metalloproteases] Levytskyy RM, Bohovych I, Khalimonchuk O. Metalloproteases of the inner mitochondrial membrane. *Biochemistry* 2017. PMID: 28806058; PMCID: PMC5792295; DOI: 10.1021/acs.biochem.7b00663.
- [viana-2021-oma1-micos] Viana MP, et al. Protease OMA1 modulates mitochondrial bioenergetics and ultrastructure through dynamic association with MICOS complex. *iScience* 2021. PMID: 33644718; PMCID: PMC7892988; DOI: 10.1016/j.isci.2021.102119.
- [anderson-2020-prohibitin-oma1] Anderson CJ, et al. Prohibitin levels regulate OMA1 activity and turnover in neurons. *Cell Death Differ* 2020. PMID: 31819158; PMCID: PMC7244729; DOI: 10.1038/s41418-019-0469-4.
- [acin-perez-2018-oma1-heart-failure] Acin-Perez R, et al. Ablation of the stress protease OMA1 protects against heart failure in mice. *Sci Transl Med* 2018;10(434):eaan4935. PMID: 29593106; DOI: 10.1126/scitranslmed.aan4935.
- [shammas-2022-oma1-chchd10] Shammas MK, et al. OMA1 mediates local and global stress responses against protein misfolding in CHCHD10 mitochondrial myopathy. *J Clin Invest* 2022;132(14):e157504. PMID: 35700042; PMCID: PMC9282932; DOI: 10.1172/JCI157504.
- [ahola-2022-oma1-isr-ferroptosis] Ahola S, Rivera Mejías P, Hermans S, Chandragiri S, Giavalisco P, Nolte H, Langer T. OMA1-mediated integrated stress response protects against ferroptosis in mitochondrial cardiomyopathy. *Cell Metab* 2022;34(11):1875-1891.e7. PMID: 36113464; DOI: 10.1016/j.cmet.2022.08.017.
- [franchino-2024-oma1-isr-spax5] Franchino CA, et al. Sustained OMA1-mediated integrated stress response is beneficial for spastic ataxia type 5. *Brain* 2024;147(3):1043-1056. PMID: 37804316; PMCID: PMC10907083; DOI: 10.1093/brain/awad340.
- [schwarzer-2023-oma1-activation-lymphoma] Schwarzer A, et al. Targeting aggressive B-cell lymphomas through pharmacological activation of the mitochondrial protease OMA1. *Mol Cancer Ther* 2023;22(11):1290-1303. PMID: 37643767; PMCID: PMC10723637; DOI: 10.1158/1535-7163.MCT-22-0718.
- [alavi-2021-oma1-hts] Alavi MV. OMA1 high-throughput screen reveals protease activation by kinase inhibitors. *ACS Chem Biol* 2021;16(11):2202-2211. PMID: 34672515; PMCID: PMC8604787; DOI: 10.1021/acschembio.1c00350.
- [rivera-mejias-2023-oma1-dna-damage] Rivera-Mejías P, et al. The mitochondrial protease OMA1 acts as a metabolic safeguard upon nuclear DNA damage. *Cell Rep* 2023;42(4):112332. PMID: 37002921; DOI: 10.1016/j.celrep.2023.112332.
- [sekine-2023-dele1-iron] Sekine Y, Houston R, Eckl EM, Fessler E, Narendra DP, Jae LT, Sekine S. A mitochondrial iron-responsive pathway regulated by DELE1. *Mol Cell* 2023;83(12):2059-2076.e6. PMID: 37327776; PMCID: PMC10329284; DOI: 10.1016/j.molcel.2023.05.031.
- [zhang-2026-haem-oma1-dele1] Zhang X, Schuler MH, et al. An ancient mitochondrial program tunes translation to haem availability. *Nature* 2026;657(8133):1027-1034. PMID: 42557333; PMCID: PMC13600944; DOI: 10.1038/s41586-026-10885-x.


## Citations

1. acin-perez-2018-oma1-heart-failure-abstract.md
2. acin-perez-2018-oma1-heart-failure-summary.md
3. ahola-2022-oma1-isr-ferroptosis-abstract.md
4. ahola-2022-oma1-isr-ferroptosis-summary.md
5. alavi-2021-oma1-hts-abstract.md
6. alavi-2021-oma1-hts-summary.md
7. alavi-2021-oma1-integral-membrane-abstract.md
8. alavi-2021-oma1-integral-membrane-summary.md
9. anand-2014-yme1l-oma1-opa1-abstract.md
10. anand-2014-yme1l-oma1-opa1-fulltext.txt
11. anand-2014-yme1l-oma1-opa1-summary.md
12. anderson-2020-prohibitin-oma1-abstract.md
13. anderson-2020-prohibitin-oma1-summary.md
14. baker-2014-oma1-autocatalytic-abstract.md
15. baker-2014-oma1-autocatalytic-summary.md
16. bao-2003-human-oma1-cdna-abstract.md
17. bao-2003-human-oma1-cdna-summary.md
18. bohovych-2014-oma1-c-terminal-abstract.md
19. bohovych-2014-oma1-c-terminal-summary.md
20. bohovych-2015-oma1-supercomplexes-abstract.md
21. bohovych-2015-oma1-supercomplexes-fulltext.txt
22. bohovych-2015-oma1-supercomplexes-summary.md
23. bohovych-2019-oma1-redox-abstract.md
24. bohovych-2019-oma1-redox-summary.md
25. consolato-2018-aaa-oma1-abstract.md
26. consolato-2018-aaa-oma1-summary.md
27. desmurs-2015-c11orf83-uqcc3-abstract.md
28. desmurs-2015-c11orf83-uqcc3-summary.md
29. ehses-2009-opa1-processing-oma1-abstract.md
30. ehses-2009-opa1-processing-oma1-fulltext.txt
31. ehses-2009-opa1-processing-oma1-summary.md
32. fessler-2020-dele1-pathway-abstract.md
33. fessler-2020-dele1-pathway-summary.md
34. franchino-2024-oma1-isr-spax5-abstract.md
35. franchino-2024-oma1-isr-spax5-fulltext.txt
36. franchino-2024-oma1-isr-spax5-summary.md
37. ge-2020-two-forms-opa1-abstract.md
38. ge-2020-two-forms-opa1-fulltext.txt
39. ge-2020-two-forms-opa1-summary.md
40. gilkerson-2021-oma1-opa1-gatekeepers-abstract.md
41. gilkerson-2021-oma1-opa1-gatekeepers-fulltext.txt
42. gilkerson-2021-oma1-opa1-gatekeepers-summary.md
43. guo-2020-oma1-dele1-hri-abstract.md
44. guo-2020-oma1-dele1-hri-fulltext.txt
45. guo-2020-oma1-dele1-hri-summary.md
46. head-2009-oma1-opa1-inactivation-abstract.md
47. head-2009-oma1-opa1-inactivation-fulltext.txt
48. head-2009-oma1-opa1-inactivation-summary.md
49. jiang-2014-oma1-bax-bak-abstract.md
50. jiang-2014-oma1-bax-bak-summary.md
51. kaser-2003-oma1-yeast-abstract.md
52. kaser-2003-oma1-yeast-summary.md
53. khalimonchuk-2012-oma1-cox1-abstract.md
54. khalimonchuk-2012-oma1-cox1-summary.md
55. korwitz-2016-oma1-neurodegeneration-abstract.md
56. korwitz-2016-oma1-neurodegeneration-fulltext.txt
57. korwitz-2016-oma1-neurodegeneration-summary.md
58. levytskyy-2017-imm-metalloproteases-abstract.md
59. levytskyy-2017-imm-metalloproteases-summary.md
60. quiros-2012-oma1-knockout-obesity-abstract.md
61. quiros-2012-oma1-knockout-obesity-summary.md
62. rainbolt-2016-yme1l-oma1-reciprocal-abstract.md
63. rainbolt-2016-yme1l-oma1-reciprocal-summary.md
64. rivera-mejias-2023-oma1-dna-damage-abstract.md
65. rivera-mejias-2023-oma1-dna-damage-summary.md
66. schwarzer-2023-oma1-activation-lymphoma-abstract.md
67. schwarzer-2023-oma1-activation-lymphoma-fulltext.txt
68. schwarzer-2023-oma1-activation-lymphoma-summary.md
69. sekine-2019-tom7-oma1-pink1-abstract.md
70. sekine-2019-tom7-oma1-pink1-summary.md
71. sekine-2023-dele1-iron-abstract.md
72. sekine-2023-dele1-iron-summary.md
73. shammas-2022-oma1-chchd10-abstract.md
74. shammas-2022-oma1-chchd10-fulltext.txt
75. shammas-2022-oma1-chchd10-summary.md
76. uniprot-A0A9L0R9P8-entry.txt
77. uniprot-A0A9L0R9P8-summary.md
78. viana-2021-oma1-micos-abstract.md
79. viana-2021-oma1-micos-fulltext.txt
80. viana-2021-oma1-micos-summary.md
81. wade-2009-horse-genome-abstract.md
82. wade-2009-horse-genome-summary.md
83. wai-2015-opa1-heart-failure-abstract.md
84. wai-2015-opa1-heart-failure-summary.md
85. zhang-2014-oma1-self-cleavage-abstract.md
86. zhang-2014-oma1-self-cleavage-summary.md
87. zhang-2026-haem-oma1-dele1-abstract.md
88. zhang-2026-haem-oma1-dele1-fulltext.txt
89. zhang-2026-haem-oma1-dele1-summary.md