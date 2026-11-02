---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:37:01.659245'
end_time: '2026-10-26T00:46:25.749271'
duration_seconds: 564.09
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: POLD2
  gene_symbol: POLD2
  uniprot_accession: A0A9L0IND0
  protein_description: 'RecName: Full=DNA polymerase delta subunit 2 {ECO:0000256|ARBA:ARBA00017588};
    AltName: Full=DNA polymerase delta subunit p50 {ECO:0000256|ARBA:ARBA00083731};'
  gene_info: Name=POLD2 {ECO:0000313|Ensembl:ENSEASP00005042466.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the DNA polymerase delta/II small subunit
  protein_domains: DNA_pol_a/d/e_bsu. (IPR007185); DNA_pol_D_N. (IPR040663); DNA_pol_delta/II_ssu.
    (IPR024826); PolD2_C. (IPR041863); DNA_pol_D_N (PF18018)
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
citation_count: 78
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0IND0
- **Protein Description:** RecName: Full=DNA polymerase delta subunit 2 {ECO:0000256|ARBA:ARBA00017588}; AltName: Full=DNA polymerase delta subunit p50 {ECO:0000256|ARBA:ARBA00083731};
- **Gene Information:** Name=POLD2 {ECO:0000313|Ensembl:ENSEASP00005042466.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the DNA polymerase delta/II small subunit
- **Key Domains:** DNA_pol_a/d/e_bsu. (IPR007185); DNA_pol_D_N. (IPR040663); DNA_pol_delta/II_ssu. (IPR024826); PolD2_C. (IPR041863); DNA_pol_D_N (PF18018)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "POLD2" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'POLD2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **POLD2** (gene ID: POLD2, UniProt: A0A9L0IND0) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# POLD2 (DNA polymerase delta subunit 2, p50) in the donkey, *Equus asinus* (UniProt A0A9L0IND0): function, localization and pathways

## 1. Introduction and summary

UniProt A0A9L0IND0 is an unreviewed (TrEMBL) entry for the donkey gene *POLD2*. It is annotated as "DNA polymerase delta subunit 2" (also called the p50 subunit), a member of the DNA polymerase delta/II small-subunit family. Its predicted domains are an N-terminal OB-fold (Pfam PF18018, DNA_pol_D_N) and a C-terminal DNA polymerase α/δ/ε subunit-B domain (Pfam PF04042, PolD2_C; CDD MPP_PolD2_C). The entry rests only on homology, with no experimental work on the donkey protein. It derives from the chromosome-level donkey reference genome [wang-2020-donkey-genomes-abstract], which says nothing about POLD2 function. The gene symbol is not ambiguous in this case. The protein description, family and domains all match the well-studied mammalian Pol δ B-subunit. The donkey sequence is 95.5% identical (448/469 residues), without gaps, to reviewed human POLD2 (P49005) (see Section 2). Function can therefore be inferred with high confidence from mammalian, chiefly human and bovine, studies, backed by work on the yeast orthologs Pol31 (*S. cerevisiae*) and Cdc1 (*S. pombe*).

POLD2 has no catalytic activity of its own. It is the obligatory structural "B-subunit" of DNA polymerase δ (Pol δ). Pol δ is the replicative B-family polymerase that synthesizes the lagging strand and does long-patch repair synthesis in the nucleus. The catalytic subunit POLD1/p125 adds deoxynucleotides to a primer terminus (DNA-directed DNA polymerase activity) and proofreads with its 3'→5' exonuclease. The accessory subunits, POLD2/p50 among them, carry no catalytic activity [baranovskiy-2008-p50-p66-xray-fulltext]. Instead p50 acts as the scaffold of the holoenzyme. Through its OB and inactive phosphodiesterase (PDE) domains it docks onto the [4Fe-4S]-containing CysB domain at the C-terminus of p125. It also binds the N-terminal domain of the third subunit, POLD3/p66 (p68), and contacts the fourth subunit, POLD4/p12 [baranovskiy-2008-p50-p66-xray-abstract; netz-2011-iron-sulfur-polymerases-abstract; lancey-2020-human-pold-holoenzyme-fulltext; khandagale-2019-pentameric-pold-abstract]. With p50 in place, Pol δ assembles fully, stays stable, and responds to PCNA, which gives it processivity [sun-1997-p50-expression-abstract; xie-2002-pold-four-subunit-abstract; layer-2020-pold-chromosomal-rearrangements-abstract].

POLD2 also has a second role. With POLD3 it forms a shared accessory module that binds the CysB domain of REV3L, the catalytic subunit of the translesion polymerase Pol ζ, producing the four-subunit Pol ζ4. This complex is much more efficient at extending primers past DNA lesions [baranovskiy-2012-pold-polz-switch-abstract; lee-2014-human-polzeta-abstract; johnson-2012-pol31-pol32-polzeta-abstract; makarova-2012-four-subunit-polzeta-abstract; malik-2020-polzeta-structure-abstract]. POLD2 is a nuclear protein. It works at replication forks and at sites of DNA damage, including ionizing-radiation-induced double-strand breaks [layer-2020-pold-chromosomal-rearrangements-abstract]. It is essential in vivo. Mice lacking *Pold2* die before gastrulation [wu-2023-pold2-knockout-mouse-abstract], and biallelic hypomorphic *POLD2* mutations in humans cause a syndrome combining replicative stress, immunodeficiency and neurodevelopmental abnormalities [conde-2019-pold-deficiency-abstract].

## 2. Identity, conservation and gene-level evidence

Mammalian Pol δ was first purified as a heterodimer of a 125-kDa catalytic subunit and a 50-kDa small subunit. Zhang et al. cloned the bovine and human small-subunit cDNAs and named the human gene *POLD2* (chromosome 7). They found the two predicted ~51 kDa proteins to be 94% identical, a degree of conservation that pointed to an essential function [zhang-1995-pold2-cloning-abstract]. Mouse *Pold2* encodes a 51,336-Da protein that is 93% identical to the other mammalian sequences and 34% identical to the yeast orthologs. Mouse p125 binds human p50 in two-hybrid assays, so the subunit interface works across species [hindges-1997-mouse-pold2-abstract]. In budding yeast the ortholog is Pol31 (58 kDa), which has 23–28% similarity to human p50 and is allelic with *HYS2*/*SDP5* [gerik-1998-pol31-pol32-yeast-abstract].

The donkey protein (487 aa) fits this conserved pattern. I aligned A0A9L0IND0 against human P49005 (469 aa). Donkey residues 19–487 align with human residues 1–469 without gaps, at 95.5% identity: 21 substitutions, nearly all conservative and clustered in the N-terminal region (notes/sequence_comparison.txt). The first 18 donkey residues (MGWSIARGYCCLDTSSTA) have no counterpart in the human protein. They probably reflect an upstream start codon chosen by the Ensembl gene model, and whether they are real is uncertain (see Open Questions). Every structurally characterized feature of human p50 is conserved in the donkey protein. These include the N-terminal MRPFL motif (human residues 61–65, donkey 79–83) proposed to bind PCNA [lu-2002-pcna-p50-interaction-abstract] and the acidic Glu136-Asp137-Glu138 triplet (donkey 154–156) that contacts the p125 CysB domain [lancey-2020-human-pold-holoenzyme-fulltext]. The InterPro and Pfam assignments in the UniProt record (DNA_pol_D_N/OB fold; DNA_pol_E_B/PolD2_C) correspond to the OB and PDE domains defined crystallographically for human p50 [baranovskiy-2008-p50-p66-xray-fulltext]. The literature on human and other mammalian POLD2 can therefore be transferred to the donkey protein with confidence. I found no literature describing the equine protein experimentally.

## 3. Domain architecture: an OB fold and an inactive phosphoesterase that serve as protein-interaction platforms

The first atomic view of p50 came from the 3-Å crystal structure of human p50 bound to the N-terminal 144 residues of p66 (p66N) [baranovskiy-2008-p50-p66-xray-abstract]. In this structure p50 has two domains. One is a phosphodiesterase-like (PDE, also called PHP/metallophosphatase-like) domain built from residues 1–41 and 180–469. The other is an OB (oligonucleotide/oligosaccharide-binding) domain, residues 54–179, a five-stranded β-barrel [baranovskiy-2008-p50-p66-xray-fulltext]. In the archaeal relatives (the DP1 small subunit of archaeal Pol D/Pol II) the PDE domain is an active nuclease. In eukaryotic B-subunits, however, the conserved histidine and aspartate residues that bind metal and catalyse the reaction are replaced, so the domain is catalytically inactive. The authors proposed that it has been repurposed for protein–protein interactions [baranovskiy-2008-p50-p66-xray-fulltext]. One face of the OB β-barrel is exposed, and by analogy with RPA OB folds it may bind DNA or protein [baranovskiy-2008-p50-p66-xray-fulltext].

The p66N domain is a winged helix-turn-helix that extends the β-sheet of the p50 PDE domain. The two subunits bury about 5,400 Å² and form 37 intersubunit hydrogen bonds, making p66N "a natural extension of p50" [baranovskiy-2008-p50-p66-xray-fulltext]. In yeast, mutations in Pol31 designed to break the Pol31–Pol32 interface produced cold sensitivity, hydroxyurea sensitivity and reduced UV mutagenesis, the same phenotypes as deleting *POL32* [baranovskiy-2008-p50-p66-xray-abstract]. The same study compared domain layouts across the family. The second subunits of Pol α, Pol ε and archaeal Pol II all have a three-domain structure resembling the p50·p66N complex as a whole. On this basis the authors proposed that part of the p66 gene arose from the B-subunit gene relatively late in evolution [baranovskiy-2008-p50-p66-xray-abstract]. The evolutionary origin of the PDE domain had been worked out earlier by sequence analysis. Aravind and Koonin found that the small subunits of archaeal Pol II and of eukaryotic Pol α and Pol δ contain a calcineurin-like phosphoesterase domain. Its catalytic motifs are intact in the archaeal proteins but disrupted in the eukaryotic orthologs. They proposed that the degenerate eukaryotic domains took on allosteric or subunit-binding functions, a prediction the p50 structure later confirmed [aravind-1998-phosphoesterase-domains-abstract]. In the Pfam/InterPro annotation of the donkey protein, PF18018 (DNA_pol_D_N) corresponds to this OB fold, and PF04042/IPR041863 to the inactive PDE domain.

## 4. POLD2 as the structural core of the Pol δ holoenzyme

### 4.1 Assembly on the p125 C-terminal CysB [4Fe-4S] domain

Biochemistry first established that p50 binds p125 directly. A monoclonal antibody against p50 inhibited calf-thymus Pol δ, and immunoprecipitation confirmed the p50–p125 interaction [sun-1997-p50-expression-abstract]. In a yeast two-hybrid screen using p125 as bait, p50 was the only positive clone recovered [liu-2003-pdip38-abstract]. The docking site on p125 is its C-terminal domain (CTD). The CTD carries two cysteine-rich motifs: CysA, which binds zinc, and CysB, which binds a [4Fe-4S] cluster. Netz et al. showed that the CysB motif of every yeast B-family polymerase binds an essential [4Fe-4S] cluster. Removing the cluster by mutating its cysteine ligands in Pol3 destabilized the CTD and abolished binding of Pol31 and Pol32. Conversely, overexpressing the accessory subunits increased the amount of Fe-S cluster bound to the CTD [netz-2011-iron-sulfur-polymerases-abstract]. In yeast, deleting the last four residues of Pol3 (LSKW) also breaks the Pol3-CTD–Pol31 contact. This mutant replicates DNA normally but is defective in homologous recombination and break-induced replication, and it is synthetically lethal with *pol32Δ*. Pol31 alleles that interact genetically with it map to a conserved surface patch on Pol31 [brocas-2010-pold-subunit-interactions-abstract]. The interaction between the catalytic and B subunits therefore matters especially for repair.

Cryo-EM structures have since shown this architecture directly. In the 3.2-Å structure of yeast Pol δ caught during DNA synthesis, the Pol3 CysB domain is the "keystone" of the assembly. Both the OB and the PDE domains of Pol31 contact CysB, burying about 2,200 Å² [jain-2019-yeast-pold-cryoem-fulltext]. In the human Pol δ–PCNA–DNA holoenzyme (3.0 Å), CysB and the helices α1 and α2 of the p125 CTD contact the p50 OB domain and the p50 inactive PDE domain. Interface residues include p50 Glu136, Asp137 and Glu138, and a hydrophobic C-terminal tail of p125 that is unique to the human enzyme inserts into a groove beneath p50-PDE [lancey-2020-human-pold-holoenzyme-fulltext]. The 3.65-Å structure of apo human Pol δ shows the same arrangement. The p125 CTD, p50, p66 and p12 together form a "regulatory module" next to the catalytic module [shin-2025-apo-human-pold-fulltext].

### 4.2 Scaffold for POLD3/p66 and POLD4/p12

p50 contacts all three of the other subunits at once, which led Baranovskiy et al. to describe it as the scaffold for Pol δ assembly [baranovskiy-2008-p50-p66-xray-fulltext]. In the human holoenzyme, p12 is a compact domain wedged between p125 and p50 [lancey-2020-human-pold-holoenzyme-fulltext]. Two-hybrid assays detect binding of p12 to both p125 and p50 [khandagale-2019-pentameric-pold-abstract; khandagale-2019-pentameric-pold-fulltext]. Because p50 links p125 to the p66 and p12 subunits, which carry the PCNA-binding motifs, it decides which form of Pol δ is present. Human cells contain two forms. Pol δ4 (p125/p50/p66/p12) predominates outside S phase and is required for D-loop extension during homologous recombination. Pol δ3 (lacking p12) is generated when p12 is degraded after DNA damage or on entry into S phase, and it is implicated in Okazaki fragment synthesis and gap filling [lee-2019-two-forms-pold-review-abstract]. In both forms the p125–p50 core is constant. Hydrodynamic studies of both the yeast heterotrimer and the reconstituted human heterodimer and heterotetramer show that these assemblies are monomeric in solution, with one copy of the B-subunit per catalytic subunit. This resolved an earlier proposal that the third subunit dimerizes the enzyme [johansson-2001-yeast-pold-structure-abstract; xie-2002-pold-four-subunit-abstract].

### 4.3 Contribution to activity, processivity and PCNA coupling

Pol δ is highly processive only in the presence of the PCNA sliding clamp. Recombinant p50 alone stimulates p125 about 2-fold, rising to about 5-fold with PCNA [sun-1997-p50-expression-abstract]. The p125–p50 heterodimer responds only weakly to PCNA, whereas the reconstituted four-subunit complex is strongly stimulated, to activity comparable with the native calf-thymus enzyme [xie-2002-pold-four-subunit-abstract]. p50 therefore appears to make Pol δ PCNA-responsive mainly by tethering p66 and p12 and their PIP boxes. Whether p50 binds PCNA directly has been debated. Co-immunoprecipitation work identified an N-terminal MRPFL-containing motif in p50 as a PCNA-binding site that p21 could compete with [lu-2002-pcna-p50-interaction-abstract]. In yeast, mutating a Pol31 PIP-like motif became lethal once the Pol32 PIP was also lost [acharya-2011-pcna-binding-pold-subunits-abstract]. Two high-resolution cryo-EM structures, however, show only the catalytic subunit contacting a single PCNA protomer, with the p50–p66N (or Pol31–Pol32) module projecting sideways and touching neither PCNA nor the DNA duplex [lancey-2020-human-pold-holoenzyme-abstract; zheng-2020-pold-pcna-structure-abstract; jain-2019-yeast-pold-cryoem-abstract]. These results can be reconciled if p50/Pol31–PCNA contacts are transient or arise in other conformations, for example during polymerase switching or recycling, rather than forming in the canonical elongation complex. Zheng et al. also found that the Pol31–Pol32 subcomplex binds single-stranded DNA, possibly through the Pol31 OB/PDE domains. The OB fold sits about 10 nucleotides from the Pol3 active site, and the authors proposed that this ssDNA binding helps recycle the polymerase from one Okazaki fragment to the next [zheng-2020-pold-pcna-structure-fulltext]. Jain et al. likewise showed that the catalytic and regulatory modules rotate relative to each other, which could let the enzyme adapt to changes in DNA path [jain-2019-yeast-pold-cryoem-abstract].

### 4.4 POLD2 maintains Pol δ stability in cells

In human cells, depleting POLD2 destabilizes the whole complex, and both POLD1 and POLD3 are degraded [layer-2020-pold-chromosomal-rearrangements-abstract]. Mutations in human *POLD2* (or *POLD1*) that impair complex stability and subunit interactions cause impaired cell-cycle progression and replication-associated DNA lesions. Overexpressing Pol δ reverses these defects [conde-2019-pold-deficiency-abstract]. In cells, therefore, the main biochemical job of POLD2 is to hold the active polymerase together.

## 5. A shared subunit: POLD2 in DNA polymerase ζ and translesion synthesis

POLD2's second major role is in damage tolerance, as a subunit of Pol ζ. Pol ζ is the B-family translesion polymerase that extends primers from nucleotides placed opposite lesions. In yeast, two groups independently showed that Pol ζ purifies as a four-subunit complex, Rev3–Rev7–Pol31–Pol32 ("Pol ζ4" or "Pol ζ-d"). In this complex Pol31 is recruited through the Rev3 C-terminus, and the [4Fe-4S] cluster in Rev3 CysB is required for complex formation [johnson-2012-pol31-pol32-polzeta-abstract; makarova-2012-four-subunit-polzeta-abstract]. Mutations that stop Rev3 binding Pol31 abolish Pol ζ-dependent TLS in vivo. Pol31/Pol32 are also needed for Pol ζ to work with PCNA, which explains why *pol32Δ* strains have long been known to be defective in mutagenesis [johnson-2012-pol31-pol32-polzeta-abstract; makarova-2012-four-subunit-polzeta-abstract]. Working on the human proteins, Baranovskiy et al. found that the C-terminal domain of the Pol ζ catalytic subunit binds the Pol δ accessory subunits. They proposed that the switch between polymerases at a blocking lesion happens by exchanging the Pol δ and Pol ζ catalytic subunits on a pre-assembled p50–p66 platform that stays on the DNA [baranovskiy-2012-pold-polz-switch-abstract]. Lee et al. then purified active human Pol ζ and isolated POLD2 and POLD3 as its accessory subunits. The resulting Pol ζ4 (REV3L–REV7–POLD2–POLD3) bypassed a cisplatin 1,2-d(GpG) intrastrand crosslink far more efficiently and processively than Pol ζ2. Full bypass required Pol η to insert and Pol ζ4 to extend [lee-2014-human-polzeta-abstract]. The cryo-EM structure of yeast Pol ζ confirmed the architecture. The five subunits form a ring-like "daisy chain" in which Rev3 CysB recruits Pol31 in the same way Pol3 CysB recruits Pol31 in Pol δ [malik-2020-polzeta-structure-abstract; malik-2020-polzeta-structure-fulltext]. The Ensembl-derived GO annotation of the donkey protein to "zeta DNA polymerase complex" and "error-prone translesion synthesis" rests on this body of work.

POLD2 also contacts the Y-family TLS polymerase Pol η directly. The F1 motif of human Pol η (FF483–484) is required for the Pol η–POLD2 interaction both in vitro and in cells. Mutating it impairs bypass of TT-CPD and AAF adducts and lowers survival of XPV cells after UV [baldeck-2015-poleta-pold2-abstract]. In TLS, then, POLD2 serves as a hub. It is retained on the DNA as part of a p50–p66 platform that can host the catalytic subunit of Pol δ or of Pol ζ, and it helps recruit Pol η.

## 6. Cellular roles, localization and physiological significance

**Subcellular localization.** UniProt assigns A0A9L0IND0 to the nucleus (and GO to nucleoplasm) by automatic annotation. This is consistent with what is known of Pol δ's role. Human POLD1 and POLD2 colocalize with phosphorylated H2AX at ionizing-radiation-induced double-strand breaks [layer-2020-pold-chromosomal-rearrangements-abstract]. Interacting partners recruited through p50, such as PDIP1, are nuclear and colocalize with PCNA at replication foci [he-2001-pdip1-abstract]. Experiments in which WRN was overexpressed show that p50 can also redistribute with p125 to the nucleolus [szekely-2000-wrn-pold-p50-abstract]. POLD2 is therefore expected to act in the nucleus, at replication forks and at sites of DNA repair.

**DNA replication.** Pol δ, of which POLD2 is an obligatory part, replicates the lagging strand. Together with PCNA and FEN1 it processes Okazaki fragments for ligation [lancey-2020-human-pold-holoenzyme-abstract]. It also takes part in leading-strand initiation and in termination [shin-2025-apo-human-pold-abstract]. Essentiality is conserved: mice lacking *Pold2* form morphologically normal blastocysts, but these cannot hatch or grow out and no homozygotes survive to gastrulation. siRNA knockdown reproduces the slowed proliferation and skewed lineage allocation [wu-2023-pold2-knockout-mouse-abstract]. In yeast, conditional *pol31* alleles are lethal in combination with *pol32Δ* [gerik-1998-pol31-pol32-yeast-abstract].

**DNA repair and recombination.** Pol δ is the main long-patch repair synthesis polymerase and is central to surviving replication stress [fuchs-2021-pold-replication-stress-review-abstract]. Depleting POLD2 in human cells reduces homology-directed repair. It also sharply reduces alternative non-homologous end-joining translocations that carry sequence modifications, while translocations with exact joins are unaffected, and both the polymerase and exonuclease activities of POLD1 contribute [layer-2020-pold-chromosomal-rearrangements-abstract]. In yeast, a weakened Pol3–Pol31 interface particularly impairs homologous recombination and break-induced replication [brocas-2010-pold-subunit-interactions-abstract]. Pol δ4, whose assembly depends on p50, is required for D-loop extension in HR [lee-2019-two-forms-pold-review-abstract].

**Chromatin and epigenetic inheritance.** Plants show the same conservation beyond animals. An Arabidopsis *pold2* mutant was recovered in a screen for release of transcriptional silencing. It shows genomic instability, elevated homologous recombination, hypersensitivity to DNA damage and short telomeres. H3K27me3 and H3K4me3 patterns are altered while DNA methylation is unchanged, suggesting that POLD2-dependent replication helps re-establish histone marks [zhang-2016-plant-pold2-abstract].

**Human disease and cancer.** Biallelic *POLD2* or *POLD1* mutations cause an autosomal-recessive syndrome of replicative stress, neurodevelopmental abnormalities and immunodeficiency [conde-2019-pold-deficiency-abstract]. In contrast, *POLD2* and *POLD3* are amplified in a high proportion of tumours, and limiting the non-catalytic subunits is synthetically lethal under replication stress [fuchs-2021-pold-replication-stress-review-abstract]. These findings come from human studies and are cited here only because they show that POLD2 dosage limits Pol δ function.

## 7. Protein-interaction network centred on p50

Besides the core subunits and Pol ζ/Pol η, p50 recruits several regulatory factors. Two-hybrid screens using p50 as bait identified the Pol δ-interacting proteins PDIP1, PDIP38 and PDIP46. PDIP1 is a TNF-α/IL-6-inducible protein that binds p50 and PCNA at the same time and stimulates Pol δ in a PCNA-dependent manner [he-2001-pdip1-abstract; liu-2003-pdip38-abstract]. Baranovskiy et al. also list p21 and WRN among the proteins recruited through p50 [baranovskiy-2008-p50-p66-xray-fulltext]. The WRN interaction has direct experimental support. In a two-hybrid screen with the C-terminus of the Werner syndrome RecQ helicase/exonuclease WRN as bait, p50 was the specific Pol δ partner identified. Native WRN co-immunoprecipitated with p50 and p125 from a nucleolus-enriched fraction. When WRN was overexpressed, p50 and p125 moved to the nucleolus and colocalized with it [szekely-2000-wrn-pold-p50-abstract]. p50 can therefore act as an adaptor through which other genome-maintenance enzymes recruit Pol δ, or relocate it within the nucleus. In p50 the inactive PDE domain and the exposed OB-fold face are the likely docking sites for these partners [baranovskiy-2008-p50-p66-xray-fulltext]. Most of this network was defined with two-hybrid and pull-down assays. Its functional significance in vivo is less well established than that of the core holoenzyme contacts.

## 8. Synthesis: what the donkey POLD2 protein most likely does

The donkey POLD2 protein is almost identical to the human protein, and the structures, biochemistry and genetics of its orthologs are consistent. Taken together, the evidence supports the following model. Donkey POLD2 (A0A9L0IND0) is the non-catalytic B-subunit of nuclear DNA polymerase δ. Its OB and inactive PDE domains clamp onto the [4Fe-4S]-containing CysB domain of POLD1, and it organizes POLD3 and POLD4 into a regulatory module beside the catalytic core. This makes POLD2 indispensable for the stability and PCNA-dependent processivity of the enzyme that synthesizes the lagging strand and fills gaps during DNA repair and recombination. The reaction it supports, catalysed by the POLD1 active site, is template-directed addition of dNMPs to a primer 3'-OH with release of pyrophosphate, with 3'→5' exonucleolytic proofreading. POLD2 itself has no enzymatic activity. Through the same CysB-docking mode, POLD2 and POLD3 also form the accessory module of Pol ζ4 for error-prone translesion extension, and POLD2 contacts Pol η to support polymerase switching. All of this happens in the nucleus. For the donkey protein, the evidence for these assignments is inference from sequence orthology, domain conservation and conserved interface residues. Direct experimental evidence comes from human, bovine, mouse and yeast studies.

## 9. Open Questions

Several points remain unresolved, both for POLD2 in general and for the donkey entry in particular. First, the 18-residue N-terminal extension (MGWSIARGYCCLDTSSTA) of the donkey gene model has no counterpart in the human protein. It should be checked against equine RNA-seq or Ribo-seq data and other *Equus* genomes, because it may be a gene-model artefact. If it were real, it would add sequence N-terminal to the region that Lancey et al. and Baranovskiy et al. place at the PDE domain's start. Second, whether p50 binds PCNA directly is still unsettled. Biochemical evidence for an N-terminal MRPFL motif [lu-2002-pcna-p50-interaction-abstract] and a Pol31 PIP-like contribution [acharya-2011-pcna-binding-pold-subunits-abstract] conflicts with cryo-EM structures in which p50 does not touch PCNA [lancey-2020-human-pold-holoenzyme-abstract; zheng-2020-pold-pcna-structure-abstract]. Structures of other functional states (strand displacement, collision release, polymerase switching) would help. Third, the ssDNA-binding activity of the regulatory module [zheng-2020-pold-pcna-structure-fulltext] has not been mapped to p50 specifically, and its role in polymerase recycling has not been tested in cells. Fourth, the pre-assembled-platform model of polymerase switching [baranovskiy-2012-pold-polz-switch-abstract] needs direct single-molecule or in-cell evidence that a single p50–p66 module exchanges catalytic partners. Fifth, the in vivo functions of p50-recruited partners (PDIPs, Pol η, p21, WRN) and any post-translational regulation of p50 itself remain poorly characterized. The UniProt keywords for acetylation and phosphorylation are inferred automatically and were not examined here. Finally, no equine-specific functional, expression or variant data were found. Equine POLD2 variants could be surveyed in the donkey population genomic data of Wang et al. [wang-2020-donkey-genomes-abstract], and their effect on the conserved CysB-interface residues assessed.

## 10. References

- **[acharya-2011-pcna-binding-pold-subunits]** Acharya N, Klassen R, Johnson RE, et al. (2011). PCNA binding domains in all three subunits of yeast DNA polymerase δ modulate its function in DNA replication. *Proc Natl Acad Sci U S A* 108(44):17927-32. PMID: 22003126; PMCID: PMC3207673; DOI: 10.1073/pnas.1109981108 (https://doi.org/10.1073/pnas.1109981108). https://pubmed.ncbi.nlm.nih.gov/22003126/
- **[aravind-1998-phosphoesterase-domains]** Aravind L, Koonin EV (1998). Phosphoesterase domains associated with DNA polymerases of diverse origins. *Nucleic Acids Res* 26(16):3746-52. PMID: 9685491; PMCID: PMC147763; DOI: 10.1093/nar/26.16.3746 (https://doi.org/10.1093/nar/26.16.3746). https://pubmed.ncbi.nlm.nih.gov/9685491/
- **[baldeck-2015-poleta-pold2]** Baldeck N, Janel-Bintz R, Wagner J, et al. (2015). FF483-484 motif of human Polη mediates its interaction with the POLD2 subunit of Polδ and contributes to DNA damage tolerance. *Nucleic Acids Res* 43(4):2116-25. PMID: 25662213; PMCID: PMC4344513; DOI: 10.1093/nar/gkv076 (https://doi.org/10.1093/nar/gkv076). https://pubmed.ncbi.nlm.nih.gov/25662213/
- **[baranovskiy-2008-p50-p66-xray]** Baranovskiy AG, Babayeva ND, Liston VG, et al. (2008). X-ray structure of the complex of regulatory subunits of human DNA polymerase delta. *Cell Cycle* 7(19):3026-36. PMID: 18818516; PMCID: PMC2605013; DOI: 10.4161/cc.7.19.6720 (https://doi.org/10.4161/cc.7.19.6720). https://pubmed.ncbi.nlm.nih.gov/18818516/
- **[baranovskiy-2012-pold-polz-switch]** Baranovskiy AG, Lada AG, Siebler HM, et al. (2012). DNA polymerase δ and ζ switch by sharing accessory subunits of DNA polymerase δ. *J Biol Chem* 287(21):17281-17287. PMID: 22465957; PMCID: PMC3366816; DOI: 10.1074/jbc.M112.351122 (https://doi.org/10.1074/jbc.M112.351122). https://pubmed.ncbi.nlm.nih.gov/22465957/
- **[brocas-2010-pold-subunit-interactions]** Brocas C, Charbonnier JB, Dhérin C, et al. (2010). Stable interactions between DNA polymerase δ catalytic and structural subunits are essential for efficient DNA repair. *DNA Repair (Amst)* 9(10):1098-111. PMID: 20813592; DOI: 10.1016/j.dnarep.2010.07.013 (https://doi.org/10.1016/j.dnarep.2010.07.013). https://pubmed.ncbi.nlm.nih.gov/20813592/
- **[conde-2019-pold-deficiency]** Conde CD, Petronczki ÖY, Baris S, et al. (2019). Polymerase δ deficiency causes syndromic immunodeficiency with replicative stress. *J Clin Invest* 129(10):4194-4206. PMID: 31449058; PMCID: PMC6763221; DOI: 10.1172/JCI128903 (https://doi.org/10.1172/JCI128903). https://pubmed.ncbi.nlm.nih.gov/31449058/
- **[fuchs-2021-pold-replication-stress-review]** Fuchs J, Cheblal A, Gasser SM (2021). Underappreciated Roles of DNA Polymerase δ in Replication Stress Survival. *Trends Genet* 37(5):476-487. PMID: 33608117; DOI: 10.1016/j.tig.2020.12.003 (https://doi.org/10.1016/j.tig.2020.12.003). https://pubmed.ncbi.nlm.nih.gov/33608117/
- **[gerik-1998-pol31-pol32-yeast]** Gerik KJ, Li X, Pautz A, et al. (1998). Characterization of the two small subunits of Saccharomyces cerevisiae DNA polymerase delta. *J Biol Chem* 273(31):19747-55. PMID: 9677405; DOI: 10.1074/jbc.273.31.19747 (https://doi.org/10.1074/jbc.273.31.19747). https://pubmed.ncbi.nlm.nih.gov/9677405/
- **[he-2001-pdip1]** He H, Tan CK, Downey KM, et al. (2001). A tumor necrosis factor alpha- and interleukin 6-inducible protein that interacts with the small subunit of DNA polymerase delta and proliferating cell nuclear antigen. *Proc Natl Acad Sci U S A* 98(21):11979-84. PMID: 11593007; PMCID: PMC59753; DOI: 10.1073/pnas.221452098 (https://doi.org/10.1073/pnas.221452098). https://pubmed.ncbi.nlm.nih.gov/11593007/
- **[hindges-1997-mouse-pold2]** Hindges R, Hübscher U (1997). Cloning, chromosomal localization, and interspecies interaction of mouse DNA polymerase delta small subunit (PolD2). *Genomics* 44(1):45-51. PMID: 9286699; DOI: 10.1006/geno.1997.4838 (https://doi.org/10.1006/geno.1997.4838). https://pubmed.ncbi.nlm.nih.gov/9286699/
- **[jain-2019-yeast-pold-cryoem]** Jain R, Rice WJ, Malik R, et al. (2019). Cryo-EM structure and dynamics of eukaryotic DNA polymerase δ holoenzyme. *Nat Struct Mol Biol* 26(10):955-962. PMID: 31582849; PMCID: PMC7309520; DOI: 10.1038/s41594-019-0305-z (https://doi.org/10.1038/s41594-019-0305-z). https://pubmed.ncbi.nlm.nih.gov/31582849/
- **[johansson-2001-yeast-pold-structure]** Johansson E, Majka J, Burgers PM (2001). Structure of DNA polymerase delta from Saccharomyces cerevisiae. *J Biol Chem* 276(47):43824-8. PMID: 11568188; DOI: 10.1074/jbc.M108842200 (https://doi.org/10.1074/jbc.M108842200). https://pubmed.ncbi.nlm.nih.gov/11568188/
- **[johnson-2012-pol31-pol32-polzeta]** Johnson RE, Prakash L, Prakash S (2012). Pol31 and Pol32 subunits of yeast DNA polymerase δ are also essential subunits of DNA polymerase ζ. *Proc Natl Acad Sci U S A* 109(31):12455-60. PMID: 22711820; PMCID: PMC3411960; DOI: 10.1073/pnas.1206052109 (https://doi.org/10.1073/pnas.1206052109). https://pubmed.ncbi.nlm.nih.gov/22711820/
- **[khandagale-2019-pentameric-pold]** Khandagale P, Peroumal D, Manohar K, et al. (2019). Human DNA polymerase delta is a pentameric holoenzyme with a dimeric p12 subunit. *Life Sci Alliance* 2(2):None. PMID: 30885984; PMCID: PMC6424025; DOI: 10.26508/lsa.201900323 (https://doi.org/10.26508/lsa.201900323). https://pubmed.ncbi.nlm.nih.gov/30885984/
- **[lancey-2020-human-pold-holoenzyme]** Lancey C, Tehseen M, Raducanu VS, et al. (2020). Structure of the processive human Pol δ holoenzyme. *Nat Commun* 11(1):1109. PMID: 32111820; PMCID: PMC7048817; DOI: 10.1038/s41467-020-14898-6 (https://doi.org/10.1038/s41467-020-14898-6). https://pubmed.ncbi.nlm.nih.gov/32111820/
- **[layer-2020-pold-chromosomal-rearrangements]** Layer JV, Debaize L, Van Scoyk A, et al. (2020). Polymerase δ promotes chromosomal rearrangements and imprecise double-strand break repair. *Proc Natl Acad Sci U S A* 117(44):27566-27577. PMID: 33077594; PMCID: PMC7959522; DOI: 10.1073/pnas.2014176117 (https://doi.org/10.1073/pnas.2014176117). https://pubmed.ncbi.nlm.nih.gov/33077594/
- **[lee-2014-human-polzeta]** Lee YS, Gregory MT, Yang W (2014). Human Pol ζ purified with accessory subunits is active in translesion DNA synthesis and complements Pol η in cisplatin bypass. *Proc Natl Acad Sci U S A* 111(8):2954-9. PMID: 24449906; PMCID: PMC3939873; DOI: 10.1073/pnas.1324001111 (https://doi.org/10.1073/pnas.1324001111). https://pubmed.ncbi.nlm.nih.gov/24449906/
- **[lee-2019-two-forms-pold-review]** Lee MYWT, Zhang S, Wang X, et al. (2019). Two forms of human DNA polymerase δ: Who does what and why? *DNA Repair (Amst)* 81:102656. PMID: 31326365; DOI: 10.1016/j.dnarep.2019.102656 (https://doi.org/10.1016/j.dnarep.2019.102656). https://pubmed.ncbi.nlm.nih.gov/31326365/
- **[liu-2003-pdip38]** Liu L, Rodriguez-Belmonte EM, Mazloum N, et al. (2003). Identification of a novel protein, PDIP38, that interacts with the p50 subunit of DNA polymerase delta and proliferating cell nuclear antigen. *J Biol Chem* 278(12):10041-7. PMID: 12522211; DOI: 10.1074/jbc.M208694200 (https://doi.org/10.1074/jbc.M208694200). https://pubmed.ncbi.nlm.nih.gov/12522211/
- **[lu-2002-pcna-p50-interaction]** Lu X, Tan CK, Zhou JQ, et al. (2002). Direct interaction of proliferating cell nuclear antigen with the small subunit of DNA polymerase delta. *J Biol Chem* 277(27):24340-5. PMID: 11986310; DOI: 10.1074/jbc.M200065200 (https://doi.org/10.1074/jbc.M200065200). https://pubmed.ncbi.nlm.nih.gov/11986310/
- **[makarova-2012-four-subunit-polzeta]** Makarova AV, Stodola JL, Burgers PM (2012). A four-subunit DNA polymerase ζ complex containing Pol δ accessory subunits is essential for PCNA-mediated mutagenesis. *Nucleic Acids Res* 40(22):11618-26. PMID: 23066099; PMCID: PMC3526297; DOI: 10.1093/nar/gks948 (https://doi.org/10.1093/nar/gks948). https://pubmed.ncbi.nlm.nih.gov/23066099/
- **[malik-2020-polzeta-structure]** Malik R, Kopylov M, Gomez-Llorente Y, et al. (2020). Structure and mechanism of B-family DNA polymerase ζ specialized for translesion DNA synthesis. *Nat Struct Mol Biol* 27(10):913-924. PMID: 32807989; PMCID: PMC7554088; DOI: 10.1038/s41594-020-0476-7 (https://doi.org/10.1038/s41594-020-0476-7). https://pubmed.ncbi.nlm.nih.gov/32807989/
- **[netz-2011-iron-sulfur-polymerases]** Netz DJ, Stith CM, Stümpfig M, et al. (2011). Eukaryotic DNA polymerases require an iron-sulfur cluster for the formation of active complexes. *Nat Chem Biol* 8(1):125-32. PMID: 22119860; PMCID: PMC3241888; DOI: 10.1038/nchembio.721 (https://doi.org/10.1038/nchembio.721). https://pubmed.ncbi.nlm.nih.gov/22119860/
- **[shin-2025-apo-human-pold]** Shin Y, Hedglin M, Murakami KS (2025). Cryo-EM structure of apo-form human DNA polymerase δ elucidates its minimal DNA synthesis activity without PCNA. *J Biol Chem* 301(4):108342. PMID: 39993528; PMCID: PMC11982976; DOI: 10.1016/j.jbc.2025.108342 (https://doi.org/10.1016/j.jbc.2025.108342). https://pubmed.ncbi.nlm.nih.gov/39993528/
- **[sun-1997-p50-expression]** Sun Y, Jiang Y, Zhang P, et al. (1997). Expression and characterization of the small subunit of human DNA polymerase delta. *J Biol Chem* 272(20):13013-8. PMID: 9148910; DOI: 10.1074/jbc.272.20.13013 (https://doi.org/10.1074/jbc.272.20.13013). https://pubmed.ncbi.nlm.nih.gov/9148910/
- **[szekely-2000-wrn-pold-p50]** Szekely AM, Chen YH, Zhang C, et al. (2000). Werner protein recruits DNA polymerase delta to the nucleolus. *Proc Natl Acad Sci U S A* 97(21):11365-70. PMID: 11027336; PMCID: PMC17206; DOI: 10.1073/pnas.97.21.11365 (https://doi.org/10.1073/pnas.97.21.11365). https://pubmed.ncbi.nlm.nih.gov/11027336/
- **[wang-2020-donkey-genomes]** Wang C, Li H, Guo Y, et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nat Commun* 11(1):6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7 (https://doi.org/10.1038/s41467-020-19813-7). https://pubmed.ncbi.nlm.nih.gov/33293529/
- **[wu-2023-pold2-knockout-mouse]** Wu X, Liu Y, Wang W, et al. (2023). Early embryonic lethality of mice lacking POLD2. *Mol Reprod Dev* 90(2):98-108. PMID: 36528861; PMCID: PMC9974775; DOI: 10.1002/mrd.23663 (https://doi.org/10.1002/mrd.23663). https://pubmed.ncbi.nlm.nih.gov/36528861/
- **[xie-2002-pold-four-subunit]** Xie B, Mazloum N, Liu L, et al. (2002). Reconstitution and characterization of the human DNA polymerase delta four-subunit holoenzyme. *Biochemistry* 41(44):13133-42. PMID: 12403614; DOI: 10.1021/bi0262707 (https://doi.org/10.1021/bi0262707). https://pubmed.ncbi.nlm.nih.gov/12403614/
- **[zhang-1995-pold2-cloning]** Zhang J, Tan CK, McMullen B, et al. (1995). Cloning of the cDNAs for the small subunits of bovine and human DNA polymerase delta and chromosomal location of the human gene (POLD2). *Genomics* 29(1):179-86. PMID: 8530069; DOI: 10.1006/geno.1995.1229 (https://doi.org/10.1006/geno.1995.1229). https://pubmed.ncbi.nlm.nih.gov/8530069/
- **[zhang-2016-plant-pold2]** Zhang J, Xie S, Cheng J, et al. (2016). The Second Subunit of DNA Polymerase Delta Is Required for Genomic Stability and Epigenetic Regulation. *Plant Physiol* 171(2):1192-208. PMID: 27208288; PMCID: PMC4902588; DOI: 10.1104/pp.15.01976 (https://doi.org/10.1104/pp.15.01976). https://pubmed.ncbi.nlm.nih.gov/27208288/
- **[zheng-2020-pold-pcna-structure]** Zheng F, Georgescu RE, Li H, et al. (2020). Structure of eukaryotic DNA polymerase δ bound to the PCNA clamp while encircling DNA. *Proc Natl Acad Sci U S A* 117(48):30344-30353. PMID: 33203675; PMCID: PMC7720213; DOI: 10.1073/pnas.2017637117 (https://doi.org/10.1073/pnas.2017637117). https://pubmed.ncbi.nlm.nih.gov/33203675/


## Citations

1. acharya-2011-pcna-binding-pold-subunits-abstract.md
2. acharya-2011-pcna-binding-pold-subunits-summary.md
3. aravind-1998-phosphoesterase-domains-abstract.md
4. aravind-1998-phosphoesterase-domains-summary.md
5. baldeck-2015-poleta-pold2-abstract.md
6. baldeck-2015-poleta-pold2-fulltext.txt
7. baldeck-2015-poleta-pold2-summary.md
8. baranovskiy-2008-p50-p66-xray-abstract.md
9. baranovskiy-2008-p50-p66-xray-fulltext.txt
10. baranovskiy-2008-p50-p66-xray-summary.md
11. baranovskiy-2012-pold-polz-switch-abstract.md
12. baranovskiy-2012-pold-polz-switch-summary.md
13. brocas-2010-pold-subunit-interactions-abstract.md
14. brocas-2010-pold-subunit-interactions-summary.md
15. conde-2019-pold-deficiency-abstract.md
16. conde-2019-pold-deficiency-summary.md
17. fuchs-2021-pold-replication-stress-review-abstract.md
18. fuchs-2021-pold-replication-stress-review-summary.md
19. gerik-1998-pol31-pol32-yeast-abstract.md
20. gerik-1998-pol31-pol32-yeast-summary.md
21. he-2001-pdip1-abstract.md
22. he-2001-pdip1-summary.md
23. hindges-1997-mouse-pold2-abstract.md
24. hindges-1997-mouse-pold2-summary.md
25. jain-2019-yeast-pold-cryoem-abstract.md
26. jain-2019-yeast-pold-cryoem-fulltext.txt
27. jain-2019-yeast-pold-cryoem-summary.md
28. johansson-2001-yeast-pold-structure-abstract.md
29. johansson-2001-yeast-pold-structure-summary.md
30. johnson-2012-pol31-pol32-polzeta-abstract.md
31. johnson-2012-pol31-pol32-polzeta-summary.md
32. khandagale-2019-pentameric-pold-abstract.md
33. khandagale-2019-pentameric-pold-fulltext.txt
34. khandagale-2019-pentameric-pold-summary.md
35. lancey-2020-human-pold-holoenzyme-abstract.md
36. lancey-2020-human-pold-holoenzyme-fulltext.txt
37. lancey-2020-human-pold-holoenzyme-summary.md
38. layer-2020-pold-chromosomal-rearrangements-abstract.md
39. layer-2020-pold-chromosomal-rearrangements-summary.md
40. lee-2014-human-polzeta-abstract.md
41. lee-2014-human-polzeta-summary.md
42. lee-2019-two-forms-pold-review-abstract.md
43. lee-2019-two-forms-pold-review-summary.md
44. liu-2003-pdip38-abstract.md
45. liu-2003-pdip38-summary.md
46. lu-2002-pcna-p50-interaction-abstract.md
47. lu-2002-pcna-p50-interaction-summary.md
48. makarova-2012-four-subunit-polzeta-abstract.md
49. makarova-2012-four-subunit-polzeta-fulltext.txt
50. makarova-2012-four-subunit-polzeta-summary.md
51. malik-2020-polzeta-structure-abstract.md
52. malik-2020-polzeta-structure-fulltext.txt
53. malik-2020-polzeta-structure-summary.md
54. netz-2011-iron-sulfur-polymerases-abstract.md
55. netz-2011-iron-sulfur-polymerases-fulltext.txt
56. netz-2011-iron-sulfur-polymerases-summary.md
57. shin-2025-apo-human-pold-abstract.md
58. shin-2025-apo-human-pold-fulltext.txt
59. shin-2025-apo-human-pold-summary.md
60. sun-1997-p50-expression-abstract.md
61. sun-1997-p50-expression-summary.md
62. szekely-2000-wrn-pold-p50-abstract.md
63. szekely-2000-wrn-pold-p50-summary.md
64. wang-2020-donkey-genomes-abstract.md
65. wang-2020-donkey-genomes-fulltext.txt
66. wang-2020-donkey-genomes-summary.md
67. wu-2023-pold2-knockout-mouse-abstract.md
68. wu-2023-pold2-knockout-mouse-fulltext.txt
69. wu-2023-pold2-knockout-mouse-summary.md
70. xie-2002-pold-four-subunit-abstract.md
71. xie-2002-pold-four-subunit-summary.md
72. zhang-1995-pold2-cloning-abstract.md
73. zhang-1995-pold2-cloning-summary.md
74. zhang-2016-plant-pold2-abstract.md
75. zhang-2016-plant-pold2-summary.md
76. zheng-2020-pold-pcna-structure-abstract.md
77. zheng-2020-pold-pcna-structure-fulltext.txt
78. zheng-2020-pold-pcna-structure-summary.md