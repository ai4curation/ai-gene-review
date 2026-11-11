---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:27:55.720383'
end_time: '2026-10-26T00:38:25.890417'
duration_seconds: 630.17
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: NUMB
  gene_symbol: NUMB
  uniprot_accession: A0A9L0IQ95
  protein_description: 'RecName: Full=Protein numb homolog {ECO:0000256|PIRNR:PIRNR017607};'
  gene_info: Name=NUMB {ECO:0000313|Ensembl:ENSEASP00005042293.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Not specified in UniProt
  protein_domains: Numb/numb-like. (IPR016698); PH-like_dom_sf. (IPR011993); PTB/PI_dom.
    (IPR006020); PID (PF00640)
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
citation_count: 108
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0IQ95
- **Protein Description:** RecName: Full=Protein numb homolog {ECO:0000256|PIRNR:PIRNR017607};
- **Gene Information:** Name=NUMB {ECO:0000313|Ensembl:ENSEASP00005042293.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Numb/numb-like. (IPR016698); PH-like_dom_sf. (IPR011993); PTB/PI_dom. (IPR006020); PID (PF00640)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NUMB" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NUMB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NUMB** (gene ID: NUMB, UniProt: A0A9L0IQ95) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# NUMB (Protein numb homolog) of the donkey, *Equus asinus* — UniProt A0A9L0IQ95

## 1. Introduction and summary

The donkey gene *NUMB* encodes a 506-residue protein, UniProt A0A9L0IQ95, that is an unreviewed TrEMBL entry predicted from the chromosome-level Dezhou donkey reference genome, with protein-existence level 4 ("predicted") [uniprot-A0A9L0IQ95-entry; wang-2020-donkey-genomes-abstract]. No experimental study of donkey NUMB exists. The genome paper that is the entry's only literature reference addresses domestication and coat colour and says nothing about NUMB [wang-2020-donkey-genomes-abstract]. Everything this report says about function therefore comes from orthologues: mainly the human, mouse and rat proteins and the founding *Drosophila* protein. That inference is well supported, because the identification checks pass cleanly. The symbol is unambiguous, the description "Protein numb homolog" matches, and the protein has the diagnostic Numb/Numb-like family signature (IPR016698; PIRSF017607) together with an N-terminal phosphotyrosine-binding (PTB/PID) domain at residues 37–173 [uniprot-A0A9L0IQ95-entry]. My alignment of the donkey sequence against human NUMB (P49757) shows that it corresponds almost exactly to human isoform 5, with roughly 97% identity [uniprot-A0A9L0IQ95-summary].

NUMB is best understood as a membrane-associated endocytic adaptor protein, not an enzyme or a transporter. Its PTB domain binds the cytoplasmic tails of transmembrane cargo, including Notch, integrin β subunits, NPC1L1 and the Drosophila protein Sanpodo. Its C-terminal half carries short linear motifs that recruit the clathrin endocytic machinery: a DPF motif binds the appendage ("ear") of the AP-2 α-adaptin subunit, and an NPF motif binds the EH domains of Eps15 [santolini-2000-numb-endocytic-abstract; santolini-2000-numb-endocytic-fulltext]. By linking cargo to clathrin-coated pits, and by steering internalised cargo toward degradation rather than recycling, NUMB lowers the amount of specific receptors on the cell surface [mcgill-2009-numb-notch1-trafficking-abstract; sorensen-2008-aak1-numb-abstract]. Its best-known physiological target is the Notch receptor. NUMB is segregated asymmetrically during cell division, and in the daughter cell that inherits it NUMB suppresses Notch signalling, which biases the two daughters toward different fates [rhyu-1994-asymmetric-numb-abstract; guo-1996-numb-notch-interaction-abstract; zhong-1996-mammalian-numb-cortex-abstract]. In mammals NUMB also acts as a scaffold for ubiquitination. It cooperates with the HECT E3 ligase Itch to ubiquitinate Notch1 and the Hedgehog transcription factor Gli1 [mcgill-2003-numb-notch1-ubiquitination-abstract; di-marcotullio-2006-numb-gli1-itch-abstract], and it protects p53 from MDM2-mediated degradation through a NUMB–p53–MDM2 tricomplex [colaluca-2008-numb-p53-abstract]. Within the cell, NUMB sits on the cytoplasmic face of the plasma membrane (basolateral in polarised epithelia), in clathrin-coated structures, and on early, recycling and late endosomes. Atypical PKC (aPKC) and AAK1 phosphorylation regulate where it is found [dho-1999-numb-isoforms-abstract; smith-2007-apkc-numb-phosphorylation-abstract; sorensen-2008-aak1-numb-abstract]. Physiologically, NUMB and its paralogue NUMBL maintain neural progenitor pools during neurogenesis [petersen-2002-numb-numblike-progenitor-abstract; li-2003-numb-numblike-forebrain-abstract], and NUMB acts as a tumour suppressor in mammary epithelium [pece-2004-numb-breast-cancer-abstract; tosoni-2015-numb-p53-mammary-abstract].

## 2. Identity, domain architecture and isoform assignment of donkey NUMB

The donkey entry is annotated automatically. PIRSF rule PIRNR017607 assigns the function "plays a role in the process of neurogenesis" and the localisation "cell membrane; peripheral membrane protein; cytoplasmic side". Its GO terms (basolateral plasma membrane, cytoplasmic vesicle, positive regulation of neurogenesis) are all IEA annotations from TreeGrafter or UniRule [uniprot-A0A9L0IQ95-entry]. The entry places the gene on donkey chromosome 7 (Ensembl ENSEASG00005004756) and assigns it to PANTHER subfamily PTHR47368:SF5, "Protein numb homolog". This subfamily separates NUMB from its paralogue NUMBL [uniprot-A0A9L0IQ95-entry]. Mammals have two Numb-family genes, *Numb* and *Numblike*. Numblike is cytoplasmic, is not asymmetrically localised, and in the cortex is found mainly in postmitotic neurons [zhong-1997-numb-numblike-expression-abstract], so the PANTHER assignment matters for interpreting the donkey gene.

Mammalian *NUMB* produces several isoforms by alternative splicing. The best-studied variation involves two cassette inserts. The first is an 11-residue insert in the PTB domain. The second is a 48-residue insert in the central proline-rich region (PRR). Together they generate the classic p65, p66, p71 and p72 proteins [dho-1999-numb-isoforms-abstract; verdi-1999-numb-isoforms-differentiation-abstract]. Human UniProt P49757 also records an exon, residues 219–316, that is skipped in isoforms 5–8 [uniprot-P49757-human-NUMB-entry]. Comparing sequences, I found that the donkey 506-residue product keeps the 11-residue PTB insert (human residues 68–78) and lacks both the 219–316 segment and the 48-residue PRR insert (366–413). That pattern matches human isoform 5 (505 residues), and 490 aligned residues are identical [uniprot-A0A9L0IQ95-summary]. This has two functional consequences. First, the PTB insert is the feature Dho and colleagues linked to constitutive plasma-membrane association in polarised MDCK cells, possibly through binding to acidic phospholipids. Isoforms without it are cytoplasmic [dho-1999-numb-isoforms-abstract]. The donkey isoform should therefore be membrane-associated, which agrees with the UniRule localisation. Second, the short ("type I") PRR is the variant Verdi and colleagues associated with promoting neuronal differentiation rather than proliferation [verdi-1999-numb-isoforms-differentiation-abstract]. Whether other donkey transcripts encode long-PRR isoforms cannot be determined from this single entry.

The donkey sequence retains the motifs that the mechanistic literature has shown to matter. These include Ser7, the main aPKC phosphorylation site studied by Sato and colleagues [sato-2011-numb-ecadherin-fulltext], and Thr102 in the PTB domain, the AAK1 phosphorylation site [sorensen-2008-aak1-numb-abstract]. They also include a C-terminal DPF motif at residue 469, which corresponds to the α-adaptin-binding DPF at residues 566–568 of the protein studied by Santolini and colleagues and is conserved in *Drosophila* Numb, and an NPF motif at residue 492 that binds the EH domain of Eps15 [santolini-2000-numb-endocytic-fulltext; uniprot-A0A9L0IQ95-summary]. Because the 219–316 segment is missing, the donkey isoform lacks the residues equivalent to human Ser276 and Ser295. UniProt annotates these as CaMK1 sites by similarity [uniprot-P49757-human-NUMB-entry]. Any CaMK1-dependent regulation reported for long isoforms may therefore not apply to this product.

The PTB domain is the cargo-recognition module. Peptide-library screening showed that the *Drosophila* Numb PTB domain prefers a GP(p)Y motif over the canonical NPXpY motif bound by Shc and IRS-1. Binding has low-micromolar affinity, and tyrosine phosphorylation strengthens it but is not required [li-1997-numb-ptb-gpy-motif-abstract]. The NMR structure of a Numb PTB–GPpY peptide complex showed that very different ligands bind a common surface site with comparable affinity. These ligands include the LDNPAY sequence of LNX and a non-NPXY sequence of the Numb-associated kinase. In the complex, the peptide adopts a helical turn and does not form the β-strand augmentation typical of other PTB domains [li-1998-numb-ptb-structure-abstract]. This promiscuity helps explain why one PTB domain can engage Notch, Sanpodo, integrins, NPC1L1, LNX and other partners. It also fits the general finding that the PTB domain is required for most Numb functions, including binding to Notch and Sanpodo, Notch1 ubiquitination, and fate specification [guo-1996-numb-notch-interaction-abstract; hutterer-2005-numb-sanpodo-abstract; mcgill-2003-numb-notch1-ubiquitination-abstract].

## 3. Core molecular function: a clathrin endocytic adaptor

Santolini and colleagues gave the key biochemical demonstration that NUMB is an endocytic protein. Mammalian Numb localised to endocytic organelles and moved together with internalising receptors. It bound the appendage domain of α-adaptin, the AP-2 subunit, through a C-terminal DPF motif, and it bound Eps15 and Eps15R through an NPF motif. Numb fragments acted as dominant negatives on both constitutive and ligand-induced receptor internalisation [santolini-2000-numb-endocytic-abstract; santolini-2000-numb-endocytic-fulltext]. Genetic evidence in *Drosophila* matched this. α-Adaptin binds Numb and is localised asymmetrically in a Numb-dependent way, and α-Adaptin mutants that cannot bind Numb cause numb-like defects in asymmetric division [berdnik-2002-alpha-adaptin-numb-abstract]. Taken together, these results define the molecular function of NUMB as a monomeric clathrin-associated sorting protein, or cargo-specific endocytic adaptor. The PTB domain binds cargo and the C-terminal motifs bind core coat components.

Kinases control this adaptor activity. Adaptor-associated kinase 1 (AAK1), which also phosphorylates the AP-2 μ2 subunit, binds NUMB and phosphorylates it at Thr102. When AAK1 is overexpressed, NUMB moves to perinuclear endosomes. When AAK1 is depleted, NUMB accumulates at the plasma membrane. A non-phosphorylatable T102A mutant stays at the plasma membrane with coated-pit markers and strongly inhibits transferrin and LDL uptake, but it does not affect EGF uptake [sorensen-2008-aak1-numb-abstract]. The authors proposed that phosphorylation promotes coated-pit maturation [sorensen-2008-aak1-numb-abstract]. UniProt's curated function statement for human NUMB, "regulates clathrin-mediated receptor endocytosis", rests on this study [uniprot-P49757-human-NUMB-entry].

Cargo selection by NUMB extends well beyond Notch. In migrating cells, NUMB binds integrin β subunits and concentrates in clathrin-coated structures on the substrate-facing surface of the leading edge. Depleting NUMB impairs integrin endocytosis and directional migration [nishimura-2007-numb-integrin-abstract]. In epithelial cells, NUMB binds p120-catenin and promotes E-cadherin internalisation [sato-2011-numb-ecadherin-abstract]. In enterocytes, NUMB recognises a YVNXXF motif in the C-terminal tail of the cholesterol transporter NPC1L1. That motif becomes exposed when cholesterol binds NPC1L1, and NUMB then recruits clathrin to internalise it. Mice lacking NUMB in the intestine absorb less dietary cholesterol and have lower plasma cholesterol [li-2014-numb-npc1l1-cholesterol-abstract]. The NPC1L1 result is notable because it ties NUMB adaptor activity directly to the uptake of a specific nutrient. NUMB is not the transporter; it controls when the transporter is internalised.

NUMB also acts after internalisation. Mammalian Notch1 is constantly internalised and sorted to either recycling or late endosomes. Overexpressing NUMB sends more Notch1 to late endosomes for degradation, whereas depleting NUMB increases Notch1 recycling [mcgill-2009-numb-notch1-trafficking-abstract]. *Drosophila* studies agree. Numb is not needed to internalise Notch or Sanpodo; instead it inhibits their recycling, working with the AP-1 complex and the Rab11 recycling pathway, and it promotes their trafficking to Rab7 late endosomes [couturier-2013-numb-endosomes-notch-abstract; cotton-2013-numb-sanpodo-recycling-abstract; johnson-2016-numb-notch-recycling-abstract]. NUMB's adaptor role therefore spans two steps of the endocytic pathway: entry at coated pits and the sorting choice between recycling and degradation. Studies in nematodes show the same thing. In *C. elegans*, the Numb homologue NUM-1A sits on the basolateral surfaces of polarised epithelial cells in the hypodermis and intestine. It inhibits basolateral endocytic recycling downstream of RAB-10, while leaving endocytic uptake unchanged, and losing num-1A bypasses the need for the recycling regulator RME-1 [nilsson-2008-num1-recycling-abstract]. Because three distantly related animals (fly, worm and mammal) show this anti-recycling activity, it is probably an ancestral property of the Numb family. In neurons, NUMB binds the microtubule-associated protein CRMP-2 and the adhesion molecule L1. CRMP-2 is needed for L1 endocytosis at axonal growth cones and for axon growth, which extends NUMB-dependent polarised endocytosis to axon development [nishimura-2003-crmp2-numb-axon-abstract].

## 4. Antagonism of Notch signalling and asymmetric cell division

Numb is named after the *Drosophila* mutant phenotype. In *numb* embryos, sensory neurons are transformed into the non-neuronal support cells of their lineage [uemura-1989-numb-sensory-organ-abstract]. Rhyu, Jan and Jan showed that Numb is a membrane-associated protein that gathers in one half of the dividing sensory organ precursor (SOP) and is inherited by only one daughter. Loss and gain of function produce opposite transformations [rhyu-1994-asymmetric-numb-abstract]. Epistasis analysis then placed Numb upstream of Notch as an inhibitor. In the CNS MP2 lineage, *Notch; numb* double mutants resemble *Notch* mutants, so Numb works by antagonising Delta–Notch signalling [spana-1996-numb-antagonizes-notch-abstract]. In SOP lineages, Numb's inhibition of Notch probably involves direct binding through the Numb PTB domain to the RAM23 region or the C-terminus of Notch. In the daughter cell that does not inherit Numb, Notch then activates *tramtrack* [guo-1996-numb-notch-interaction-abstract].

Later work showed that much of this antagonism runs through endocytosis. Numb binds the four-pass transmembrane protein Sanpodo, which itself binds Notch, and keeps Sanpodo off the plasma membrane in the Numb-inheriting cell [oconnor-giles-2003-numb-sanpodo-abstract; hutterer-2005-numb-sanpodo-abstract]. Live imaging revealed that unequal inheritance of Numb produces asymmetric Notch at the cytokinetic furrow and directional signalling at cytokinesis. During that period, Numb moves from the basal cortex to subapical endosomes in an α-adaptin-dependent way, where it blocks Notch recycling [couturier-2012-numb-notch-cytokinesis-abstract; couturier-2013-numb-endosomes-notch-abstract]. The exact step Numb controls has been debated. One model has Numb driving Sanpodo internalisation via α-Adaptin [hutterer-2005-numb-sanpodo-abstract]. Later internalisation assays found that bulk Sanpodo endocytosis is normal in *numb* mutants, and that Numb instead acts with AP-1 to limit Sanpodo recycling [cotton-2013-numb-sanpodo-recycling-abstract]. The two views can be reconciled in a model where Numb's main effect is on post-endocytic sorting rather than entry, consistent with the mammalian Notch1 data [mcgill-2009-numb-notch1-trafficking-abstract; johnson-2016-numb-notch-recycling-abstract].

Mammalian NUMB keeps this function. Mouse m-Numb is localised asymmetrically to the apical membrane of dividing cortical ventricular progenitors, rescues *Drosophila numb* mutants, and binds Notch1 [zhong-1996-mammalian-numb-cortex-abstract]. Rat mNUMB produces the same fate transformations as dNUMB when misexpressed in flies [verdi-1996-mammalian-numb-adapter-abstract]. In mammalian cells NUMB also promotes ubiquitination of membrane-tethered Notch1 and degradation of the Notch intracellular domain (NICD) after activation, which reduces *Hes1* reporter activity. This depends on the PTB domain and on Itch, and it is independent of the Sel10/PEST pathway that operates in the nucleus [mcgill-2003-numb-notch1-ubiquitination-abstract]. NUMB mutants that cannot bind Itch, or that lack the endocytic motifs, fail to promote Notch1 degradation, which links the ubiquitination and trafficking models [mcgill-2009-numb-notch1-trafficking-abstract]. Asymmetric NUMB segregation also controls self-renewing divisions of mammary stem cells. There NUMB is partitioned into the daughter that keeps stem identity [tosoni-2015-numb-p53-mammary-abstract], and losing NUMB from mammary epithelium releases Notch signalling [pece-2004-numb-breast-cancer-abstract]. How the conserved polarity machinery positions Numb is described in reviews of asymmetric stem cell division. Segregating fate determinants such as Numb into one daughter is one of two general strategies for making daughters unequal; the other is orienting the division relative to a niche. The molecules are conserved, but how they act differs between tissues and between vertebrates and invertebrates [knoblich-2008-asymmetric-stem-division-abstract]. In *Drosophila*, the adaptor Partner of Numb (PON) binds Numb, colocalises with it at mitosis, and directs it to the basal side [lu-1998-pon-numb-abstract].

## 5. NUMB as a ubiquitination scaffold: Hedgehog/Gli1 and p53/MDM2

Besides Notch, NUMB regulates the stability of key transcription factors by bringing them together with E3 ubiquitin ligases. In cerebellar granule cell progenitors, NUMB inhibits the Hedgehog pathway. It targets the transcription factor Gli1 for Itch-dependent ubiquitination and degradation, which stops growth and promotes differentiation. NUMB is downregulated both in early progenitors and in cancer cells derived from granule cell progenitors [di-marcotullio-2006-numb-gli1-itch-abstract]. NUMB therefore limits the strength and duration of Hedgehog signalling at a stage when progenitors respond to Sonic hedgehog, and it uses the same partner, Itch, that it recruits to Notch1 [mcgill-2003-numb-notch1-ubiquitination-abstract].

In the p53 pathway NUMB does the opposite: it protects. Human NUMB was first isolated as an MDM2-binding protein, and MDM2 can itself ubiquitinate NUMB [yogosawa-2003-numb-mdm2-abstract]. Colaluca and colleagues showed that NUMB forms a tricomplex with p53 and HDM2/MDM2 that blocks p53 ubiquitination and degradation. This raises p53 levels and activity. In primary breast tumour cells, loss of NUMB lowers p53 and increases chemoresistance [colaluca-2008-numb-p53-abstract]. In NUMB-deficient breast cancers, the same single event therefore activates NOTCH and weakens p53 [colaluca-2008-numb-p53-abstract]. Tosoni and colleagues extended this circuit to normal tissue. Asymmetrically inherited NUMB keeps p53 activity high in the daughter mammary stem cell, and the expanded stem cell compartment and tumourigenicity of NUMB-knockout mammary glands can be reversed by restoring p53 [tosoni-2015-numb-p53-mammary-abstract]. Reviews treat the Notch, Hedgehog and p53 roles as three outputs of one network built from endocytosis and ubiquitination [gulino-2010-multiple-functions-numb-abstract; pece-2011-numb-cancer-review-abstract].

## 6. Subcellular localisation and its regulation

Several kinds of evidence agree on where NUMB is found. In *Drosophila* SOPs, Numb is a membrane-associated protein concentrated in one cortical crescent [rhyu-1994-asymmetric-numb-abstract]. In dividing mouse cortical progenitors, m-Numb sits at the apical membrane [zhong-1996-mammalian-numb-cortex-abstract]. At the ultrastructural and light-microscopic level, mammalian NUMB is found on endocytic organelles and clathrin-coated structures [santolini-2000-numb-endocytic-abstract; nishimura-2007-numb-integrin-abstract]. It is also found on perinuclear endosomes in an AAK1-dependent manner [sorensen-2008-aak1-numb-abstract]. In fly SOPs it moves to subapical endosomes during cytokinesis [couturier-2013-numb-endosomes-notch-abstract]. In polarised epithelial cells NUMB is basolateral and is excluded from the apical domain, where aPKC accumulates [smith-2007-apkc-numb-phosphorylation-abstract]. Sato and colleagues additionally saw NUMB at intercellular adhesion sites and at the apical membrane in their epithelial model [sato-2011-numb-ecadherin-abstract]. Membrane association depends on the isoform. PTB-insert isoforms, such as the donkey product, bind the plasma membrane constitutively, whereas isoforms without the insert are cytoplasmic [dho-1999-numb-isoforms-abstract]. The IEA annotations on the donkey entry (cell membrane, cytoplasmic side; basolateral plasma membrane; cytoplasmic vesicle) are therefore consistent with the experimental record from orthologues [uniprot-A0A9L0IQ95-entry].

Polarity kinases set this distribution. The Par complex (Par3, Par6, aPKC) phosphorylates Numb, and mammalian Numb lacking two PKC sites (Numb2A) spreads evenly around the cortex instead of being polarised [smith-2007-apkc-numb-phosphorylation-abstract]. aPKC phosphorylation releases NUMB from clathrin-coated structures and from integrins [nishimura-2007-numb-integrin-abstract]. It also blocks binding to p120-catenin and α-adaptin, which limits E-cadherin endocytosis and helps maintain apicobasal polarity [sato-2011-numb-ecadherin-abstract]. In *Drosophila* neural precursors, a defined cascade links this phosphorylation to the cell cycle. At mitosis, Aurora-A phosphorylates Par-6 and so activates aPKC. aPKC first phosphorylates Lgl, which releases Lgl from the complex and lets Bazooka/Par-3 bind instead. This switches aPKC's substrate preference toward Numb, which is then phosphorylated and released from the apical cortex, so that Numb forms a crescent on the opposite side [wirtz-peitz-2008-aurora-par-numb-abstract]. Bailey and Prehoda explained biophysically how phosphorylation removes Numb from the membrane. *Drosophila* Numb, like Lgl and Miranda, has a short basic-hydrophobic (BH) motif that binds negatively charged phospholipids directly and is needed for cortical localisation. The motif overlaps the aPKC sites Ser48 and Ser52, so phosphorylation changes its electrostatic character and weakens lipid binding. The same study noted that the Numb PTB domain can also bind lipids but is not enough for cortical localisation on its own [bailey-2015-par-membrane-motifs-abstract; bailey-2015-par-membrane-motifs-fulltext]. In donkey NUMB, the main mammalian aPKC site, Ser7, sits in a strongly basic N-terminal stretch (MNKLRQSFRRKK) [uniprot-A0A9L0IQ95-entry]. By analogy, this stretch may work as a phospho-regulated membrane-binding motif. That is my own inference from the sequence and has not been tested experimentally. Phosphomimetic Ser7 mutants are lost from the lateral membrane and fail to bind E-cadherin, p120 or α-adaptin [sato-2011-numb-ecadherin-fulltext]. In dividing neural progenitors, the Golgi protein ACBD3 is released into the cytosol when the Golgi fragments at mitosis. It then binds NUMB and acts together with it to specify fate, linking NUMB activity to the cell cycle [zhou-2007-golgi-acbd3-numb-abstract].

NUMB levels are also controlled by ubiquitin-dependent proteolysis. The RING/PDZ E3 ligase LNX binds the NUMB PTB domain through an NPXY-type motif, ubiquitinates NUMB, and causes its proteasomal degradation, which enhances Notch signalling [nie-2002-lnx-e3-numb-abstract; li-1998-numb-ptb-structure-abstract]. MDM2 can also ubiquitinate NUMB [yogosawa-2003-numb-mdm2-abstract]. In about half of human mammary carcinomas, NUMB is lost through excessive ubiquitination and proteasomal degradation [pece-2004-numb-breast-cancer-abstract]. Splicing adds another layer of control. RBM5, RBM6 and RBM10 regulate the choice of the *NUMB* PRR exon in opposite directions, and that choice affects cancer cell proliferation [bechara-2013-rbm-numb-splicing-abstract].

## 7. Physiological roles relevant to the donkey protein

The best-established physiological role of mammalian NUMB, and the one the donkey UniRule annotation records, is in neurogenesis. Mouse *Numb* and *Numblike* are redundantly required throughout embryonic neurogenesis to keep progenitor cells as progenitors. When both genes are removed from the nervous system, early neurons form on schedule but progenitors are almost completely depleted [petersen-2002-numb-numblike-progenitor-abstract]. Removing *Numb* from the dorsal forebrain of *Numblike*-null mice at a later stage causes hyperproliferation, delayed cell-cycle exit, impaired differentiation and malformation of the cortex [li-2003-numb-numblike-forebrain-abstract]. That NUMB can both maintain progenitors and promote differentiation, depending on stage and isoform [zhou-2007-golgi-acbd3-numb-abstract; verdi-1999-numb-isoforms-differentiation-abstract], fits its role as a context-dependent adaptor rather than a fixed switch. NUMB is also required after birth. Inducible deletion of *Numb* and *Numblike* from postnatal subventricular zone (SVZ) progenitors and ependymal cells damages the wall of the lateral ventricle and reduces neuroblast survival. Progenitors that escaped deletion later repair the niche [kuo-2006-numb-svz-repair-abstract]. This is the experimental basis for UniProt's annotation that NUMB regulates SVZ neuroblast survival and ependymal wall integrity [uniprot-P49757-human-NUMB-entry].

Outside the nervous system, NUMB maintains the balance of mammary stem and progenitor cells and suppresses tumours through both Notch and p53 [pece-2004-numb-breast-cancer-abstract; tosoni-2015-numb-p53-mammary-abstract; colaluca-2008-numb-p53-abstract]. It controls cell migration through integrin endocytosis [nishimura-2007-numb-integrin-abstract] and epithelial polarity through E-cadherin trafficking [sato-2011-numb-ecadherin-abstract]. It is also needed for intestinal cholesterol absorption through NPC1L1 endocytosis [li-2014-numb-npc1l1-cholesterol-abstract]. Reviews of NUMB isoforms in cancer stem cells note that NUMB loss expands the stem cell pool through combined Notch activation and p53 reduction, and that specific isoforms can favour tumourigenesis [choi-2021-numb-isoforms-cancer-review-abstract]. None of these roles has been studied in equids. The donkey protein is about 97% identical to human isoform 5 and keeps every functional motif analysed above except the residues in the 219–316 segment. On that basis it is reasonable to predict that donkey NUMB acts as a membrane-associated clathrin endocytic adaptor that antagonises Notch and supports neural progenitor maintenance, as its orthologues do [uniprot-A0A9L0IQ95-summary].

## 8. Open Questions

The first gap is basic: whether the donkey protein is expressed, and in which tissues, has not been shown. A0A9L0IQ95 is a gene-model prediction at evidence level 4 [uniprot-A0A9L0IQ95-entry]. Equine RNA-seq or proteomics data could confirm the transcript and show whether other isoforms exist in donkey tissues, especially PTB-insert-negative (cytoplasmic) forms and long-PRR forms. The relative abundance of such isoforms is known to shift between proliferating and differentiating cells [dho-1999-numb-isoforms-abstract; verdi-1999-numb-isoforms-differentiation-abstract]. A second gap is that the functional significance of the human 219–316 segment, which this isoform lacks and which carries the CaMK1 sites Ser276/Ser295, is poorly studied [uniprot-P49757-human-NUMB-entry]. Comparing isoform 5-like proteins with full-length NUMB in endocytosis, Notch-inhibition and p53-stabilisation assays would show whether this exon tunes any particular output.

At the mechanistic level, the exact endocytic step through which NUMB antagonises Notch remains unresolved. One view emphasises internalisation [berdnik-2002-alpha-adaptin-numb-abstract; hutterer-2005-numb-sanpodo-abstract]. The other emphasises inhibition of recycling and sorting to late endosomes [cotton-2013-numb-sanpodo-recycling-abstract; couturier-2013-numb-endosomes-notch-abstract; johnson-2016-numb-notch-recycling-abstract; mcgill-2009-numb-notch1-trafficking-abstract]. There is also no structural explanation yet for how one PTB domain discriminates among its many ligands [li-1998-numb-ptb-structure-abstract], nor for how the NUMB–p53–MDM2 tricomplex is put together [colaluca-2008-numb-p53-abstract]. The Itch-dependent ubiquitination of Gli1 and Notch1 raises a further question about how NUMB activates or positions a HECT ligase on such different substrates [di-marcotullio-2006-numb-gli1-itch-abstract; mcgill-2003-numb-notch1-ubiquitination-abstract]. Finally, the cholesterol-absorption role [li-2014-numb-npc1l1-cholesterol-abstract] has not been examined in herbivores such as equids, whose dietary sterol intake differs from that of mice and humans. That would be a natural comparative follow-up. It would also help to show directly that the basic N-terminal region of mammalian NUMB around Ser7 is the functional counterpart of the phospho-regulated BH motif described in *Drosophila* Numb [bailey-2015-par-membrane-motifs-abstract]. A literature search of Europe PMC combining NUMB with equine, horse, donkey or *Equus* found no relevant equid studies, so every functional statement about the donkey protein in this report remains an inference from orthologues.

## 9. References

* **bailey-2015-par-membrane-motifs** — Bailey MJ, Prehoda KE. Establishment of Par-Polarized Cortical Domains via Phosphoregulated Membrane Motifs. *Developmental cell* 2015;35(2):199-210. PMID: 26481050; PMCID: PMC4624610; DOI: 10.1016/j.devcel.2015.09.016 (https://doi.org/10.1016/j.devcel.2015.09.016). https://pubmed.ncbi.nlm.nih.gov/26481050/
* **bechara-2013-rbm-numb-splicing** — Bechara EG, Sebestyén E, Bernardis I, Eyras E, Valcárcel J. RBM5, 6, and 10 differentially regulate NUMB alternative splicing to control cancer cell proliferation. *Molecular cell* 2013;52(5):720-733. PMID: 24332178; DOI: 10.1016/j.molcel.2013.11.010 (https://doi.org/10.1016/j.molcel.2013.11.010). https://pubmed.ncbi.nlm.nih.gov/24332178/
* **berdnik-2002-alpha-adaptin-numb** — Berdnik D, Török T, González-Gaitán M, Knoblich JA. The endocytic protein alpha-Adaptin is required for numb-mediated asymmetric cell division in Drosophila. *Developmental cell* 2002;3(2):221-231. PMID: 12194853; DOI: 10.1016/s1534-5807(02)00215-0 (https://doi.org/10.1016/s1534-5807(02)00215-0). https://pubmed.ncbi.nlm.nih.gov/12194853/
* **choi-2021-numb-isoforms-cancer-review** — Choi HY, Seok J, Kang GH, Lim KM, Cho SG. The role of NUMB/NUMB isoforms in cancer stem cells. *BMB reports* 2021;54(7):335-343. PMID: 34078527; PMCID: PMC8328821. https://pubmed.ncbi.nlm.nih.gov/34078527/
* **colaluca-2008-numb-p53** — Colaluca IN, Tosoni D, Nuciforo P, Senic-Matuglia F, Galimberti V, Viale G, Pece S, Di Fiore PP. NUMB controls p53 tumour suppressor activity. *Nature* 2008;451(7174):76-80. PMID: 18172499; DOI: 10.1038/nature06412 (https://doi.org/10.1038/nature06412). https://pubmed.ncbi.nlm.nih.gov/18172499/
* **cotton-2013-numb-sanpodo-recycling** — Cotton M, Benhra N, Le Borgne R. Numb inhibits the recycling of Sanpodo in Drosophila sensory organ precursor. *Current biology : CB* 2013;23(7):581-587. PMID: 23523246; DOI: 10.1016/j.cub.2013.02.020 (https://doi.org/10.1016/j.cub.2013.02.020). https://pubmed.ncbi.nlm.nih.gov/23523246/
* **couturier-2012-numb-notch-cytokinesis** — Couturier L, Vodovar N, Schweisguth F. Endocytosis by Numb breaks Notch symmetry at cytokinesis. *Nature cell biology* 2012;14(2):131-139. PMID: 22267085; DOI: 10.1038/ncb2419 (https://doi.org/10.1038/ncb2419). https://pubmed.ncbi.nlm.nih.gov/22267085/
* **couturier-2013-numb-endosomes-notch** — Couturier L, Mazouni K, Schweisguth F. Numb localizes at endosomes and controls the endosomal sorting of notch after asymmetric division in Drosophila. *Current biology : CB* 2013;23(7):588-593. PMID: 23523245; DOI: 10.1016/j.cub.2013.03.002 (https://doi.org/10.1016/j.cub.2013.03.002). https://pubmed.ncbi.nlm.nih.gov/23523245/
* **dho-1999-numb-isoforms** — Dho SE, French MB, Woods SA, McGlade CJ. Characterization of four mammalian numb protein isoforms. Identification of cytoplasmic and membrane-associated variants of the phosphotyrosine binding domain. *The Journal of biological chemistry* 1999;274(46):33097-33104. PMID: 10551880; DOI: 10.1074/jbc.274.46.33097 (https://doi.org/10.1074/jbc.274.46.33097). https://pubmed.ncbi.nlm.nih.gov/10551880/
* **di-marcotullio-2006-numb-gli1-itch** — Di Marcotullio L, Ferretti E, Greco A, De Smaele E, Po A, Sico MA, Alimandi M, Giannini G, Maroder M, Screpanti I, Gulino A. Numb is a suppressor of Hedgehog signalling and targets Gli1 for Itch-dependent ubiquitination. *Nature cell biology* 2006;8(12):1415-1423. PMID: 17115028; DOI: 10.1038/ncb1510 (https://doi.org/10.1038/ncb1510). https://pubmed.ncbi.nlm.nih.gov/17115028/
* **gulino-2010-multiple-functions-numb** — Gulino A, Di Marcotullio L, Screpanti I. The multiple functions of Numb. *Experimental cell research* 2010;316(6):900-906. PMID: 19944684; DOI: 10.1016/j.yexcr.2009.11.017 (https://doi.org/10.1016/j.yexcr.2009.11.017). https://pubmed.ncbi.nlm.nih.gov/19944684/
* **guo-1996-numb-notch-interaction** — Guo M, Jan LY, Jan YN. Control of daughter cell fates during asymmetric division: interaction of Numb and Notch. *Neuron* 1996;17(1):27-41. PMID: 8755476; DOI: 10.1016/s0896-6273(00)80278-0 (https://doi.org/10.1016/s0896-6273(00)80278-0). https://pubmed.ncbi.nlm.nih.gov/8755476/
* **hutterer-2005-numb-sanpodo** — Hutterer A, Knoblich JA. Numb and alpha-Adaptin regulate Sanpodo endocytosis to specify cell fate in Drosophila external sensory organs. *EMBO reports* 2005;6(9):836-842. PMID: 16113648; PMCID: PMC1369167; DOI: 10.1038/sj.embor.7400500 (https://doi.org/10.1038/sj.embor.7400500). https://pubmed.ncbi.nlm.nih.gov/16113648/
* **johnson-2016-numb-notch-recycling** — Johnson SA, Zitserman D, Roegiers F. Numb regulates the balance between Notch recycling and late-endosome targeting in Drosophila neural progenitor cells. *Molecular biology of the cell* 2016;27(18):2857-2866. PMID: 27466320; PMCID: PMC5025272; DOI: 10.1091/mbc.e15-11-0751 (https://doi.org/10.1091/mbc.e15-11-0751). https://pubmed.ncbi.nlm.nih.gov/27466320/
* **knoblich-2008-asymmetric-stem-division** — Knoblich JA. Mechanisms of asymmetric stem cell division. *Cell* 2008;132(4):583-597. PMID: 18295577; DOI: 10.1016/j.cell.2008.02.007 (https://doi.org/10.1016/j.cell.2008.02.007). https://pubmed.ncbi.nlm.nih.gov/18295577/
* **kuo-2006-numb-svz-repair** — Kuo CT, Mirzadeh Z, Soriano-Navarro M, Rasin M, Wang D, Shen J, Sestan N, Garcia-Verdugo J, Alvarez-Buylla A, Jan LY, Jan YN. Postnatal deletion of Numb/Numblike reveals repair and remodeling capacity in the subventricular neurogenic niche. *Cell* 2006;127(6):1253-1264. PMID: 17174898; PMCID: PMC1876765; DOI: 10.1016/j.cell.2006.10.041 (https://doi.org/10.1016/j.cell.2006.10.041). https://pubmed.ncbi.nlm.nih.gov/17174898/
* **li-1997-numb-ptb-gpy-motif** — Li SC, Songyang Z, Vincent SJ, Zwahlen C, Wiley S, Cantley L, Kay LE, Forman-Kay J, Pawson T. High-affinity binding of the Drosophila Numb phosphotyrosine-binding domain to peptides containing a Gly-Pro-(p)Tyr motif. *Proceedings of the National Academy of Sciences of the United States of America* 1997;94(14):7204-7209. PMID: 9207069; PMCID: PMC23792; DOI: 10.1073/pnas.94.14.7204 (https://doi.org/10.1073/pnas.94.14.7204). https://pubmed.ncbi.nlm.nih.gov/9207069/
* **li-1998-numb-ptb-structure** — Li SC, Zwahlen C, Vincent SJ, McGlade CJ, Kay LE, Pawson T, Forman-Kay JD. Structure of a Numb PTB domain-peptide complex suggests a basis for diverse binding specificity. *Nature structural biology* 1998;5(12):1075-1083. PMID: 9846878; DOI: 10.1038/4185 (https://doi.org/10.1038/4185). https://pubmed.ncbi.nlm.nih.gov/9846878/
* **li-2003-numb-numblike-forebrain** — Li HS, Wang D, Shen Q, Schonemann MD, Gorski JA, Jones KR, Temple S, Jan LY, Jan YN. Inactivation of Numb and Numblike in embryonic dorsal forebrain impairs neurogenesis and disrupts cortical morphogenesis. *Neuron* 2003;40(6):1105-1118. PMID: 14687546; DOI: 10.1016/s0896-6273(03)00755-4 (https://doi.org/10.1016/s0896-6273(03)00755-4). https://pubmed.ncbi.nlm.nih.gov/14687546/
* **li-2014-numb-npc1l1-cholesterol** — Li PS, Fu ZY, Zhang YY, Zhang JH, Xu CQ, Ma YT, Li BL, Song BL. The clathrin adaptor Numb regulates intestinal cholesterol absorption through dynamic interaction with NPC1L1. *Nature medicine* 2014;20(1):80-86. PMID: 24336247; DOI: 10.1038/nm.3417 (https://doi.org/10.1038/nm.3417). https://pubmed.ncbi.nlm.nih.gov/24336247/
* **lu-1998-pon-numb** — Lu B, Rothenberg M, Jan LY, Jan YN. Partner of Numb colocalizes with Numb during mitosis and directs Numb asymmetric localization in Drosophila neural and muscle progenitors. *Cell* 1998;95(2):225-235. PMID: 9790529; DOI: 10.1016/s0092-8674(00)81753-5 (https://doi.org/10.1016/s0092-8674(00)81753-5). https://pubmed.ncbi.nlm.nih.gov/9790529/
* **mcgill-2003-numb-notch1-ubiquitination** — McGill MA, McGlade CJ. Mammalian numb proteins promote Notch1 receptor ubiquitination and degradation of the Notch1 intracellular domain. *The Journal of biological chemistry* 2003;278(25):23196-23203. PMID: 12682059; DOI: 10.1074/jbc.m302827200 (https://doi.org/10.1074/jbc.m302827200). https://pubmed.ncbi.nlm.nih.gov/12682059/
* **mcgill-2009-numb-notch1-trafficking** — McGill MA, Dho SE, Weinmaster G, McGlade CJ. Numb regulates post-endocytic trafficking and degradation of Notch1. *The Journal of biological chemistry* 2009;284(39):26427-26438. PMID: 19567869; PMCID: PMC2785331; DOI: 10.1074/jbc.m109.014845 (https://doi.org/10.1074/jbc.m109.014845). https://pubmed.ncbi.nlm.nih.gov/19567869/
* **nie-2002-lnx-e3-numb** — Nie J, McGill MA, Dermer M, Dho SE, Wolting CD, McGlade CJ. LNX functions as a RING type E3 ubiquitin ligase that targets the cell fate determinant Numb for ubiquitin-dependent degradation. *The EMBO journal* 2002;21(1-2):93-102. PMID: 11782429; PMCID: PMC125803; DOI: 10.1093/emboj/21.1.93 (https://doi.org/10.1093/emboj/21.1.93). https://pubmed.ncbi.nlm.nih.gov/11782429/
* **nilsson-2008-num1-recycling** — Nilsson L, Conradt B, Ruaud AF, Chen CC, Hatzold J, Bessereau JL, Grant BD, Tuck S. Caenorhabditis elegans num-1 negatively regulates endocytic recycling. *Genetics* 2008;179(1):375-387. PMID: 18493060; PMCID: PMC2390616; DOI: 10.1534/genetics.108.087247 (https://doi.org/10.1534/genetics.108.087247). https://pubmed.ncbi.nlm.nih.gov/18493060/
* **nishimura-2003-crmp2-numb-axon** — Nishimura T, Fukata Y, Kato K, Yamaguchi T, Matsuura Y, Kamiguchi H, Kaibuchi K. CRMP-2 regulates polarized Numb-mediated endocytosis for axon growth. *Nature cell biology* 2003;5(9):819-826. PMID: 12942088; DOI: 10.1038/ncb1039 (https://doi.org/10.1038/ncb1039). https://pubmed.ncbi.nlm.nih.gov/12942088/
* **nishimura-2007-numb-integrin** — Nishimura T, Kaibuchi K. Numb controls integrin endocytosis for directional cell migration with aPKC and PAR-3. *Developmental cell* 2007;13(1):15-28. PMID: 17609107; DOI: 10.1016/j.devcel.2007.05.003 (https://doi.org/10.1016/j.devcel.2007.05.003). https://pubmed.ncbi.nlm.nih.gov/17609107/
* **oconnor-giles-2003-numb-sanpodo** — O'Connor-Giles KM, Skeath JB. Numb inhibits membrane localization of Sanpodo, a four-pass transmembrane protein, to promote asymmetric divisions in Drosophila. *Developmental cell* 2003;5(2):231-243. PMID: 12919675; DOI: 10.1016/s1534-5807(03)00226-0 (https://doi.org/10.1016/s1534-5807(03)00226-0). https://pubmed.ncbi.nlm.nih.gov/12919675/
* **pece-2004-numb-breast-cancer** — Pece S, Serresi M, Santolini E, Capra M, Hulleman E, Galimberti V, Zurrida S, Maisonneuve P, Viale G, Di Fiore PP. Loss of negative regulation by Numb over Notch is relevant to human breast carcinogenesis. *The Journal of cell biology* 2004;167(2):215-221. PMID: 15492044; PMCID: PMC2172557; DOI: 10.1083/jcb.200406140 (https://doi.org/10.1083/jcb.200406140). https://pubmed.ncbi.nlm.nih.gov/15492044/
* **pece-2011-numb-cancer-review** — Pece S, Confalonieri S, R Romano P, Di Fiore PP. NUMB-ing down cancer by more than just a NOTCH. *Biochimica et biophysica acta* 2011;1815(1):26-43. PMID: 20940030; DOI: 10.1016/j.bbcan.2010.10.001 (https://doi.org/10.1016/j.bbcan.2010.10.001). https://pubmed.ncbi.nlm.nih.gov/20940030/
* **petersen-2002-numb-numblike-progenitor** — Petersen PH, Zou K, Hwang JK, Jan YN, Zhong W. Progenitor cell maintenance requires numb and numblike during mouse neurogenesis. *Nature* 2002;419(6910):929-934. PMID: 12410312; DOI: 10.1038/nature01124 (https://doi.org/10.1038/nature01124). https://pubmed.ncbi.nlm.nih.gov/12410312/
* **rhyu-1994-asymmetric-numb** — Rhyu MS, Jan LY, Jan YN. Asymmetric distribution of numb protein during division of the sensory organ precursor cell confers distinct fates to daughter cells. *Cell* 1994;76(3):477-491. PMID: 8313469; DOI: 10.1016/0092-8674(94)90112-0 (https://doi.org/10.1016/0092-8674(94)90112-0). https://pubmed.ncbi.nlm.nih.gov/8313469/
* **santolini-2000-numb-endocytic** — Santolini E, Puri C, Salcini AE, Gagliani MC, Pelicci PG, Tacchetti C, Di Fiore PP. Numb is an endocytic protein. *The Journal of cell biology* 2000;151(6):1345-1352. PMID: 11121447; PMCID: PMC2190585; DOI: 10.1083/jcb.151.6.1345 (https://doi.org/10.1083/jcb.151.6.1345). https://pubmed.ncbi.nlm.nih.gov/11121447/
* **sato-2011-numb-ecadherin** — Sato K, Watanabe T, Wang S, Kakeno M, Matsuzawa K, Matsui T, Yokoi K, Murase K, Sugiyama I, Ozawa M, Kaibuchi K. Numb controls E-cadherin endocytosis through p120 catenin with aPKC. *Molecular biology of the cell* 2011;22(17):3103-3119. PMID: 21775625; PMCID: PMC3164458; DOI: 10.1091/mbc.e11-03-0274 (https://doi.org/10.1091/mbc.e11-03-0274). https://pubmed.ncbi.nlm.nih.gov/21775625/
* **smith-2007-apkc-numb-phosphorylation** — Smith CA, Lau KM, Rahmani Z, Dho SE, Brothers G, She YM, Berry DM, Bonneil E, Thibault P, Schweisguth F, Le Borgne R, McGlade CJ. aPKC-mediated phosphorylation regulates asymmetric membrane localization of the cell fate determinant Numb. *The EMBO journal* 2007;26(2):468-480. PMID: 17203073; PMCID: PMC1783459; DOI: 10.1038/sj.emboj.7601495 (https://doi.org/10.1038/sj.emboj.7601495). https://pubmed.ncbi.nlm.nih.gov/17203073/
* **sorensen-2008-aak1-numb** — Sorensen EB, Conner SD. AAK1 regulates Numb function at an early step in clathrin-mediated endocytosis. *Traffic (Copenhagen, Denmark)* 2008;9(10):1791-1800. PMID: 18657069; DOI: 10.1111/j.1600-0854.2008.00790.x (https://doi.org/10.1111/j.1600-0854.2008.00790.x). https://pubmed.ncbi.nlm.nih.gov/18657069/
* **spana-1996-numb-antagonizes-notch** — Spana EP, Doe CQ. Numb antagonizes Notch signaling to specify sibling neuron cell fates. *Neuron* 1996;17(1):21-26. PMID: 8755475; DOI: 10.1016/s0896-6273(00)80277-9 (https://doi.org/10.1016/s0896-6273(00)80277-9). https://pubmed.ncbi.nlm.nih.gov/8755475/
* **tosoni-2015-numb-p53-mammary** — Tosoni D, Zecchini S, Coazzoli M, Colaluca I, Mazzarol G, Rubio A, Caccia M, Villa E, Zilian O, Di Fiore PP, Pece S. The Numb/p53 circuitry couples replicative self-renewal and tumor suppression in mammary epithelial cells. *The Journal of cell biology* 2015;211(4):845-862. PMID: 26598619; PMCID: PMC4657167; DOI: 10.1083/jcb.201505037 (https://doi.org/10.1083/jcb.201505037). https://pubmed.ncbi.nlm.nih.gov/26598619/
* **uemura-1989-numb-sensory-organ** — Uemura T, Shepherd S, Ackerman L, Jan LY, Jan YN. numb, a gene required in determination of cell fate during sensory organ formation in Drosophila embryos. *Cell* 1989;58(2):349-360. PMID: 2752427; DOI: 10.1016/0092-8674(89)90849-0 (https://doi.org/10.1016/0092-8674(89)90849-0). https://pubmed.ncbi.nlm.nih.gov/2752427/
* **verdi-1996-mammalian-numb-adapter** — Verdi JM, Schmandt R, Bashirullah A, Jacob S, Salvino R, Craig CG, Program AE, Lipshitz HD, McGlade CJ. Mammalian NUMB is an evolutionarily conserved signaling adapter protein that specifies cell fate. *Current biology : CB* 1996;6(9):1134-1145. PMID: 8805372; DOI: 10.1016/s0960-9822(02)70680-5 (https://doi.org/10.1016/s0960-9822(02)70680-5). https://pubmed.ncbi.nlm.nih.gov/8805372/
* **verdi-1999-numb-isoforms-differentiation** — Verdi JM, Bashirullah A, Goldhawk DE, Kubu CJ, Jamali M, Meakin SO, Lipshitz HD. Distinct human NUMB isoforms regulate differentiation vs. proliferation in the neuronal lineage. *Proceedings of the National Academy of Sciences of the United States of America* 1999;96(18):10472-10476. PMID: 10468633; PMCID: PMC17913; DOI: 10.1073/pnas.96.18.10472 (https://doi.org/10.1073/pnas.96.18.10472). https://pubmed.ncbi.nlm.nih.gov/10468633/
* **wang-2020-donkey-genomes** — Wang C, Li H, Guo Y, Huang J, Sun Y, Min J, Wang J, Fang X, Zhao Z, Wang S, Zhang Y, Liu Q, Jiang Q, Wang X, Guo Y, Yang C, Wang Y, Tian F, Zhuang G, Fan Y, Gao Q, Li Y, Ju Z, Li J, Li R, Hou M, Yang G, Liu G, Liu W, Guo J, Pan S, Fan G, Zhang W, Zhang R, Yu J, Zhang X, Yin Q, Ji C, Jin Y, Yue G, Liu M, Xu J, Liu S, Jordana J, Noce A, Amills M, Wu DD, Li S, Zhou X, Zhong J. Donkey genomes provide new insights into domestication and selection for coat color. *Nature communications* 2020;11(1):6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7 (https://doi.org/10.1038/s41467-020-19813-7). https://pubmed.ncbi.nlm.nih.gov/33293529/
* **wirtz-peitz-2008-aurora-par-numb** — Wirtz-Peitz F, Nishimura T, Knoblich JA. Linking cell cycle to asymmetric division: Aurora-A phosphorylates the Par complex to regulate Numb localization. *Cell* 2008;135(1):161-173. PMID: 18854163; PMCID: PMC2989779; DOI: 10.1016/j.cell.2008.07.049 (https://doi.org/10.1016/j.cell.2008.07.049). https://pubmed.ncbi.nlm.nih.gov/18854163/
* **yogosawa-2003-numb-mdm2** — Yogosawa S, Miyauchi Y, Honda R, Tanaka H, Yasuda H. Mammalian Numb is a target protein of Mdm2, ubiquitin ligase. *Biochemical and biophysical research communications* 2003;302(4):869-872. PMID: 12646252; DOI: 10.1016/s0006-291x(03)00282-1 (https://doi.org/10.1016/s0006-291x(03)00282-1). https://pubmed.ncbi.nlm.nih.gov/12646252/
* **zhong-1996-mammalian-numb-cortex** — Zhong W, Feder JN, Jiang MM, Jan LY, Jan YN. Asymmetric localization of a mammalian numb homolog during mouse cortical neurogenesis. *Neuron* 1996;17(1):43-53. PMID: 8755477; DOI: 10.1016/s0896-6273(00)80279-2 (https://doi.org/10.1016/s0896-6273(00)80279-2). https://pubmed.ncbi.nlm.nih.gov/8755477/
* **zhong-1997-numb-numblike-expression** — Zhong W, Jiang MM, Weinmaster G, Jan LY, Jan YN. Differential expression of mammalian Numb, Numblike and Notch1 suggests distinct roles during mouse cortical neurogenesis. *Development (Cambridge, England)* 1997;124(10):1887-1897. PMID: 9169836; DOI: 10.1242/dev.124.10.1887 (https://doi.org/10.1242/dev.124.10.1887). https://pubmed.ncbi.nlm.nih.gov/9169836/
* **zhou-2007-golgi-acbd3-numb** — Zhou Y, Atkins JB, Rompani SB, Bancescu DL, Petersen PH, Tang H, Zou K, Stewart SB, Zhong W. The mammalian Golgi regulates numb signaling in asymmetric cell division by releasing ACBD3 during mitosis. *Cell* 2007;129(1):163-178. PMID: 17418793; DOI: 10.1016/j.cell.2007.02.037 (https://doi.org/10.1016/j.cell.2007.02.037). https://pubmed.ncbi.nlm.nih.gov/17418793/


## Citations

1. _metadata.json
2. bailey-2015-par-membrane-motifs-abstract.md
3. bailey-2015-par-membrane-motifs-fulltext.txt
4. bailey-2015-par-membrane-motifs-summary.md
5. bechara-2013-rbm-numb-splicing-abstract.md
6. bechara-2013-rbm-numb-splicing-summary.md
7. berdnik-2002-alpha-adaptin-numb-abstract.md
8. berdnik-2002-alpha-adaptin-numb-summary.md
9. choi-2021-numb-isoforms-cancer-review-abstract.md
10. choi-2021-numb-isoforms-cancer-review-fulltext.txt
11. choi-2021-numb-isoforms-cancer-review-summary.md
12. colaluca-2008-numb-p53-abstract.md
13. colaluca-2008-numb-p53-summary.md
14. cotton-2013-numb-sanpodo-recycling-abstract.md
15. cotton-2013-numb-sanpodo-recycling-summary.md
16. couturier-2012-numb-notch-cytokinesis-abstract.md
17. couturier-2012-numb-notch-cytokinesis-summary.md
18. couturier-2013-numb-endosomes-notch-abstract.md
19. couturier-2013-numb-endosomes-notch-summary.md
20. dho-1999-numb-isoforms-abstract.md
21. dho-1999-numb-isoforms-summary.md
22. di-marcotullio-2006-numb-gli1-itch-abstract.md
23. di-marcotullio-2006-numb-gli1-itch-summary.md
24. gulino-2010-multiple-functions-numb-abstract.md
25. gulino-2010-multiple-functions-numb-summary.md
26. guo-1996-numb-notch-interaction-abstract.md
27. guo-1996-numb-notch-interaction-summary.md
28. hutterer-2005-numb-sanpodo-abstract.md
29. hutterer-2005-numb-sanpodo-summary.md
30. johnson-2016-numb-notch-recycling-abstract.md
31. johnson-2016-numb-notch-recycling-fulltext.txt
32. johnson-2016-numb-notch-recycling-summary.md
33. knoblich-2008-asymmetric-stem-division-abstract.md
34. knoblich-2008-asymmetric-stem-division-summary.md
35. kuo-2006-numb-svz-repair-abstract.md
36. kuo-2006-numb-svz-repair-summary.md
37. li-1997-numb-ptb-gpy-motif-abstract.md
38. li-1997-numb-ptb-gpy-motif-summary.md
39. li-1998-numb-ptb-structure-abstract.md
40. li-1998-numb-ptb-structure-summary.md
41. li-2003-numb-numblike-forebrain-abstract.md
42. li-2003-numb-numblike-forebrain-summary.md
43. li-2014-numb-npc1l1-cholesterol-abstract.md
44. li-2014-numb-npc1l1-cholesterol-summary.md
45. lu-1998-pon-numb-abstract.md
46. lu-1998-pon-numb-summary.md
47. mcgill-2003-numb-notch1-ubiquitination-abstract.md
48. mcgill-2003-numb-notch1-ubiquitination-summary.md
49. mcgill-2009-numb-notch1-trafficking-abstract.md
50. mcgill-2009-numb-notch1-trafficking-summary.md
51. nie-2002-lnx-e3-numb-abstract.md
52. nie-2002-lnx-e3-numb-summary.md
53. nilsson-2008-num1-recycling-abstract.md
54. nilsson-2008-num1-recycling-summary.md
55. nishimura-2003-crmp2-numb-axon-abstract.md
56. nishimura-2003-crmp2-numb-axon-summary.md
57. nishimura-2007-numb-integrin-abstract.md
58. nishimura-2007-numb-integrin-summary.md
59. oconnor-giles-2003-numb-sanpodo-abstract.md
60. oconnor-giles-2003-numb-sanpodo-summary.md
61. pece-2004-numb-breast-cancer-abstract.md
62. pece-2004-numb-breast-cancer-fulltext.txt
63. pece-2004-numb-breast-cancer-summary.md
64. pece-2011-numb-cancer-review-abstract.md
65. pece-2011-numb-cancer-review-summary.md
66. petersen-2002-numb-numblike-progenitor-abstract.md
67. petersen-2002-numb-numblike-progenitor-summary.md
68. rhyu-1994-asymmetric-numb-abstract.md
69. rhyu-1994-asymmetric-numb-summary.md
70. santolini-2000-numb-endocytic-abstract.md
71. santolini-2000-numb-endocytic-fulltext.txt
72. santolini-2000-numb-endocytic-summary.md
73. sato-2011-numb-ecadherin-abstract.md
74. sato-2011-numb-ecadherin-fulltext.txt
75. sato-2011-numb-ecadherin-summary.md
76. smith-2007-apkc-numb-phosphorylation-abstract.md
77. smith-2007-apkc-numb-phosphorylation-summary.md
78. sorensen-2008-aak1-numb-abstract.md
79. sorensen-2008-aak1-numb-summary.md
80. spana-1996-numb-antagonizes-notch-abstract.md
81. spana-1996-numb-antagonizes-notch-summary.md
82. tosoni-2015-numb-p53-mammary-abstract.md
83. tosoni-2015-numb-p53-mammary-fulltext.txt
84. tosoni-2015-numb-p53-mammary-summary.md
85. uemura-1989-numb-sensory-organ-abstract.md
86. uemura-1989-numb-sensory-organ-summary.md
87. uniprot-A0A9L0IQ95-entry.fasta
88. uniprot-A0A9L0IQ95-entry.txt
89. uniprot-A0A9L0IQ95-summary.md
90. uniprot-P49757-human-NUMB-entry.txt
91. uniprot-P49757-human-NUMB.fasta
92. verdi-1996-mammalian-numb-adapter-abstract.md
93. verdi-1996-mammalian-numb-adapter-summary.md
94. verdi-1999-numb-isoforms-differentiation-abstract.md
95. verdi-1999-numb-isoforms-differentiation-summary.md
96. wang-2020-donkey-genomes-abstract.md
97. wang-2020-donkey-genomes-fulltext.txt
98. wang-2020-donkey-genomes-summary.md
99. wirtz-peitz-2008-aurora-par-numb-abstract.md
100. wirtz-peitz-2008-aurora-par-numb-summary.md
101. yogosawa-2003-numb-mdm2-abstract.md
102. yogosawa-2003-numb-mdm2-summary.md
103. zhong-1996-mammalian-numb-cortex-abstract.md
104. zhong-1996-mammalian-numb-cortex-summary.md
105. zhong-1997-numb-numblike-expression-abstract.md
106. zhong-1997-numb-numblike-expression-summary.md
107. zhou-2007-golgi-acbd3-numb-abstract.md
108. zhou-2007-golgi-acbd3-numb-summary.md