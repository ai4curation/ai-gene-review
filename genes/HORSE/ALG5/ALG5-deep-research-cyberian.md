---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:28:29.731238'
end_time: '2026-10-26T01:43:27.181265'
duration_seconds: 897.45
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: ALG5
  gene_symbol: ALG5
  uniprot_accession: A0A5F5PM72
  protein_description: 'RecName: Full=Dolichyl-phosphate beta-glucosyltransferase
    {ECO:0000256|ARBA:ARBA00070518}; EC=2.4.1.117 {ECO:0000256|ARBA:ARBA00012583};
    AltName: Full=Asparagine-linked glycosylation protein 5 homolog {ECO:0000256|ARBA:ARBA00083115};'
  gene_info: Name=ALG5 {ECO:0000313|Ensembl:ENSECAP00000048984.1, ECO:0000313|VGNC:VGNC:15249};
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the glycosyltransferase 2 family.
  protein_domains: DPG_synthase. (IPR035518); Glyco_trans_2-like. (IPR001173); Nucleotide-diphossugar_trans.
    (IPR029044); Glycos_transf_2 (PF00535)
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
citation_count: 88
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A5F5PM72
- **Protein Description:** RecName: Full=Dolichyl-phosphate beta-glucosyltransferase {ECO:0000256|ARBA:ARBA00070518}; EC=2.4.1.117 {ECO:0000256|ARBA:ARBA00012583}; AltName: Full=Asparagine-linked glycosylation protein 5 homolog {ECO:0000256|ARBA:ARBA00083115};
- **Gene Information:** Name=ALG5 {ECO:0000313|Ensembl:ENSECAP00000048984.1, ECO:0000313|VGNC:VGNC:15249};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the glycosyltransferase 2 family.
- **Key Domains:** DPG_synthase. (IPR035518); Glyco_trans_2-like. (IPR001173); Nucleotide-diphossugar_trans. (IPR029044); Glycos_transf_2 (PF00535)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ALG5" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ALG5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ALG5** (gene ID: ALG5, UniProt: A0A5F5PM72) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ALG5 (Dolichyl-phosphate β-glucosyltransferase) in the Horse, *Equus caballus* (UniProt A0A5F5PM72)

## 1. Introduction and Summary

The horse gene *ALG5* (VGNC:15249; Ensembl ENSECAG00000024592, chromosome 17) encodes dolichyl-phosphate β-glucosyltransferase (EC 2.4.1.117), also called dolichyl-phosphate glucose (Dol-P-Glc) synthase. The UniProt entry A0A5F5PM72 is an unreviewed TrEMBL record whose functional annotation comes entirely from automatic rules (ARBA). It assigns the reaction dolichyl phosphate + UDP-α-D-glucose → dolichyl β-D-glucosyl phosphate + UDP (RHEA:15401), places the protein in the endoplasmic reticulum (ER) membrane as a single-pass protein, assigns it to glycosyltransferase family 2 (GT2), and assigns it to the protein-glycosylation pathway [uniprot-A0A5F5PM72-entry]. The gene model was predicted from the Thoroughbred reference genome [wade-2009-horse-genome-abstract]. No experimental study of the horse protein exists, so everything said here about its function is inferred from orthology. That inference is strong. The horse sequence is about 95% identical to human ALG5 (Q9Y673) across the aligned residues (see `alignment-horse-vs-human-ALG5.txt`). The enzyme's activity, its role and its place in N-glycosylation have been shown directly in yeast, human, *Drosophila* and protist systems [heesen-1994-alg5-yeast-abstract; imbach-1999-alg6-cdg-ic-abstract; haecker-2008-wollknauel-alg5-abstract; grabinska-2008-trichomonas-glcpdol-abstract].

The identity check passed. The symbol ALG5, the protein name, the GT2/DPG_synthase domain architecture (IPR035518, PF00535) and the organism all agree with each other and with the literature. No other gene with the symbol "ALG5" was found that could cause confusion. One caveat is specific to this accession, though. A0A5F5PM72 (294 aa) is one of about ten horse ALG5 transcript models. It lacks a 30-residue segment, corresponding to human residues 95–124 (QKRDPAFTYEVIVVDDGSKDQTSKVAFKYC), that every other horse model and canonical human ALG5 contain. The same segment is absent from human isoform 2 (VSP_041019) [uniprot-Q9Y673-entry; uniprot-horse-ALG5-isoforms-entries]. Section 6 discusses what this may mean.

In short, ALG5 makes the β-linked glucosyl donor Dol-P-Glc from UDP-glucose and dolichyl phosphate on the cytoplasmic face of the ER membrane. After transbilayer movement, Dol-P-Glc is the only glucose donor that the lumenal glucosyltransferases ALG6, ALG8 and ALG10 use to add three glucose residues to Man9GlcNAc2-PP-dolichol. This completes the Glc3Man9GlcNAc2-PP-Dol precursor that oligosaccharyltransferase (OST) transfers to nascent polypeptides [runge-1984-yeast-glucosylation-mutants-abstract; rush-2015-flippases-review-fulltext; aebi-2013-n-glycosylation-er-abstract]. Loss of ALG5 activity leaves N-glycans unglucosylated and reduces glycosylation efficiency. In humans, losing one copy of ALG5 is enough to impair maturation of polycystin-1 and to cause an atypical autosomal dominant polycystic kidney disease (PKD7) [lemoine-2022-alg5-pkd-abstract; elhassan-2024-alg5-adpkd-fulltext].

## 2. Molecular Function: Reaction and Substrate Specificity

The catalytic function of ALG5 was established genetically and biochemically in *Saccharomyces cerevisiae*. Runge, Huffaker and Robbins isolated the complementing mutants *alg5-1* and *alg6-1*. Both accumulate Man9GlcNAc2-PP-dolichol in place of the normal Glc3Man9GlcNAc2-PP-dolichol. When microsomes were given UDP-[3H]glucose, only the *alg6* membranes could make dolichol-phosphoglucose. When the same microsomes were given preformed Dol-P-[3H]Glc, the *alg5* membranes, but not the *alg6* membranes, glucosylated the lipid-linked oligosaccharide (LLO) [runge-1984-yeast-glucosylation-mutants-abstract]. This experiment separated two steps: Dol-P-Glc synthesis, which needs ALG5, and transfer of glucose from Dol-P-Glc to the LLO, which needs ALG6. A photoaffinity study with 5-azido-[β-32P]UDP-glucose then labelled a 35-kDa microsomal protein. Labelling was reduced or absent in *alg5* and *dpg1* mutants, rose in step with synthase activity, and was normal in *alg6* membranes. This showed that the synthase polypeptide binds the nucleotide-sugar donor [palamarczyk-1990-glcpdol-35kda-abstract]. Heesen and colleagues cloned *ALG5* by complementing *alg5-1*. It encodes a 38.3-kDa membrane protein. Overexpressing it in yeast or *E. coli* raised UDP-Glc:Dol-P glucosyltransferase activity, and deleting it abolished that activity and caused under-glycosylation of carboxypeptidase Y [heesen-1994-alg5-yeast-abstract]. Activity of the protein expressed in *E. coli*, a host with no endogenous eukaryotic LLO machinery, is good evidence that Alg5p is the catalytic polypeptide itself and not a regulatory subunit.

The enzyme is specific for both of its substrates. The donor is UDP-glucose. The acceptor is the polyisoprenoid monophosphate dolichyl phosphate, which has a saturated α-isoprene unit. The product is β-linked. Work on archaeal homologues summarises earlier acid/base hydrolysis, enzymatic and mass-spectrometric evidence that the Dol-P-Glc made by Alg5, like the Dol-P-Man made by Dpm1, has the β-anomeric configuration [larkin-2013-alternate-pathway-fulltext]. This matches the β-linkage in the recommended name and in the Rhea reaction [uniprot-A0A5F5PM72-entry]. Studies of the next step in mammalian (pig brain) microsomes used water-soluble Glc-P-Dol analogues. They showed that the lumenal Glc-P-Dol-dependent glucosyltransferases prefer short-chain donors with an internal *cis*-isoprene unit in the β-position, consistent with the poly-*cis* structure of natural dolichol [rush-1998-glcpdol-transbilayer-abstract]. ALG5 orthologues from distant eukaryotes keep this activity. Human ALG5 cDNA partially complements the yeast *alg5* defect [imbach-1999-alg6-cdg-ic-abstract]. The *Drosophila* orthologue *wollknäuel* does as well, whereas the two *wol* mutant alleles isolated in the fly screen do not [haecker-2008-wollknauel-alg5-abstract]. Five *Trichomonas vaginalis* ALG5 paralogues have Dol-P-Glc synthase activity as recombinant proteins and correct glycosylation in a yeast *alg5* mutant [grabinska-2008-trichomonas-glcpdol-abstract]. The horse residues are essentially identical to the human ones across the catalytic domain (alignment file), so the horse enzyme can be assigned the same reaction and substrate specificity with high confidence.

Mammalian enzymology agrees with the yeast work and adds kinetic detail. In 1983, Gold and Green purified UDP-glucose:dolichyl-phosphate glucosyltransferase about 1700-fold from rough ER of the murine plasmacytoma MOPC-315. The partially purified enzyme had apparent Km values of 0.79 µM for UDP-glucose and 0.65 µM for dolichyl phosphate. It depended entirely on added Dol-P, was activated by choline-containing phospholipids, had an apparent molecular weight of about 37,000, and made Dol-P-Glc as its only product [gold-1983-plasmacytoma-glucosyltransferase-abstract]. Matern and colleagues later purified the human liver enzyme about 1100-fold to near homogeneity. It ran as a single Mr 36,000 band, was separable from the enzymes that make GlcNAc-PP-Dol and Dol-P-Man, was protected by its competitive inhibitor uridine, and needed phospholipid, with phosphatidylethanolamine the best activator [matern-1990-human-liver-glcpdol-synthase-abstract]. That size fits the 324-residue human ALG5 polypeptide [uniprot-Q9Y673-entry]. Photoaffinity labelling with 5-azido-[β-32P]UDP-glucose consistently picked out a polypeptide of about 35 kDa. In rat liver microsomes, labelling depended on UV light, the intact sugar nucleotide, divalent cations and the level of Dol-P [drake-1990-35kda-glcpdol-abstract]. In lactating rat mammary gland, Dol-P and Mg2+ enhanced labelling, UDP-glucose competed for it specifically, and other sugar nucleotides and glucose-1-phosphate did not compete well [shailubhai-1990-rat-mammary-photoaffinity-abstract]. Taken together, these studies show that mammalian Dol-P-Glc synthase is a roughly 35–37-kDa, divalent-cation- and phospholipid-dependent enzyme with sub-micromolar affinity for both substrates and strict selectivity for UDP-glucose. The downstream lumenal glucosyltransferase also prefers dolichyl-P-glucose over polyprenyl-P-glucose (lower Km, higher Vmax). This shows that the saturated α-isoprene of the ALG5 product matters for its later use [dsouza-schorey-1994-dolichol-vs-polyprenol-abstract].

## 3. Structural Basis: A GT-A-fold Polyprenyl-phosphate Glycosyltransferase

ALG5 belongs to glycosyltransferase family 2. It has a Glyco_trans_2-like (PF00535) catalytic domain with a nucleotide-diphospho-sugar transferase (GT-A) Rossmann-like fold (IPR029044) and a DPG_synthase-specific subfamily signature (IPR035518, CDD cd04188) [uniprot-A0A5F5PM72-entry]. When it was first cloned, yeast Alg5p was noted to resemble Dpm1p, the GDP-mannose:Dol-P mannosyltransferase [heesen-1994-alg5-yeast-abstract]. Archaeal AglK, which makes α-linked Dol-P-GlcNAc, is more than 50% similar to yeast Alg5. This points to a common evolutionary origin for the dolichyl-monophosphate-sugar synthases of the archaeal and eukaryotic domains [larkin-2013-alternate-pathway-fulltext]. A phylogenomic study of how the eukaryotic N-glycosylation pathway arose treated Alg5 and Dpm as GT2 paralogues, both of them polyisoprenol-P-monosaccharide synthases that act on the cytoplasmic side and supply sugars to the opposite side of the membrane. In the GT2 tree, eukaryotic Alg5 fell into a clade dominated by bacteria, which includes the *Paenibacillus* WsfH protein thought to make bactoprenyl-P-glucose. Eukaryotic Dpm grouped instead with archaeal AglJ and AglK. The authors concluded that ALG5 was already present in the last eukaryotic common ancestor but that its prokaryotic origin is unclear, and it might be a eukaryotic innovation [lombard-2016-nglycosylation-evolution-fulltext]. ALG5 is found throughout eukaryotes, from protists to mammals [grabinska-2008-trichomonas-glcpdol-abstract; haecker-2008-wollknauel-alg5-abstract], which supports transferring its function to the horse orthologue.

No experimental structure of any eukaryotic ALG5 has been reported in the sources reviewed here. The closest structural model is the 3.0-Å crystal structure of GtrB from *Synechocystis*, a glucose-specific polyisoprenyl-phosphate glycosyltransferase (PI-GT) in the same class as DPMS. GtrB forms a tetramer, and each protomer contributes two helices to a membrane-spanning bundle. The active site lies about 15 Å from the membrane surface and coordinates Mn2+ and UDP through conserved aspartate (D94, D96, D157) and arginine (R122, R200) residues. Mutating these residues abolishes activity, and the reaction does not need a catalytic base. A conserved juxtamembrane domain, which carries disease mutations in human DPM1, was proposed to shield the polyisoprenyl phosphate and move it into the active site [ardiccioni-2016-gtrb-structure-fulltext]. This geometry, a soluble catalytic domain that reaches a lipid acceptor in the membrane, fits the predicted topology of mammalian ALG5. In that model a short N-terminal lumenal stretch is followed by a signal-anchor helix (human residues 8–28) and a large cytoplasmic catalytic domain (residues 29–324) [uniprot-Q9Y673-entry]. Early topology studies of yeast Alg5p suggested several membrane spans [heesen-1994-alg5-yeast-abstract]. That disagreement has not been settled experimentally.

Pathogenic missense variants in human ALG5 also inform the structure–function picture. Elhassan and colleagues placed p.R79W, together with the earlier variants at R208 and R212, on the AlphaFold model AF-Q9Y673-F1. They superposed it on archaeal DPMS crystal structures to locate the catalytic regions and substrates. All three variants replace arginines close to the "A-loop", which governs glucosyltransferase activity. R79 is invariant across species [elhassan-2024-alg5-adpkd-fulltext]. UniProt records R208H as a loss-of-function variant for N-linked glycosylation that cannot rescue PKD1 glycosylation in ALG5-deficient cells [uniprot-Q9Y673-entry]. Horse ALG5 keeps these arginines (alignment file).

## 4. Subcellular Localisation and Membrane Topology of the Reaction

ALG5 is an ER membrane protein. UniProt annotates human ALG5 to the ER membrane on the basis of Imbach et al. [uniprot-Q9Y673-entry; imbach-1999-alg6-cdg-ic-abstract]. Immunofluorescence of normal human kidney sections found ALG5 exclusively in the ER, where it co-localised with protein disulfide isomerase in every nephron segment examined [elhassan-2024-alg5-adpkd-fulltext]. The horse annotation of "ER membrane; single-pass membrane protein" is inherited from this evidence [uniprot-A0A5F5PM72-entry]. In yeast, Alg5p is an ER membrane protein that is not part of the OST complex. In the split-ubiquitin membrane two-hybrid system, it was used as an ER-resident protein that does not interact with the OST subunit Wbp1p, whereas Wbp1p and Ost1p interact specifically [stagljar-1998-split-ubiquitin-abstract]. So ALG5 acts on its own at the ER membrane and is not a stable subunit of the oligosaccharyltransferase.

The topology of the reaction matters for understanding ALG5's role. Rush and Waechter tested this directly in sealed ER vesicles from pig brain, using the latency of the lumenal processing glucosidases I and II to confirm the vesicles were intact. In sealed vesicles, trypsin inactivated Glc-P-Dol synthase, which means its active site faces the cytoplasm. The three Glc-P-Dol:Glc0-2Man9GlcNAc2-PP-Dol glucosyltransferases were protected, which places them in the lumen [rush-1998-glcpdol-topology-abstract; rush-1998-glcpdol-transbilayer-abstract]. This arrangement means that, after ALG5 has made it, Dol-P-Glc must be moved ("flipped") across the bilayer. A water-soluble analogue, Glc-P-citronellol, enters sealed rat-liver and pig-brain ER vesicles through a system that is time-dependent, saturable, bidirectional, trypsin-sensitive, stereoselective and enriched in the ER. It does not enter liposomes or erythrocytes, which indicates a dedicated Glc-P-Dol flippase [rush-1998-glcpdol-transbilayer-abstract; rush-2015-flippases-review-fulltext]. The protein responsible has still not been identified [rush-2015-flippases-review-fulltext]. The cytosolic location of ALG5's catalytic domain also places it where UDP-glucose is made, so no ER UDP-Glc transporter is needed for Dol-P-Glc synthesis. Lumenal UDP-glucose transported into the ER has a separate role, in glycoprotein reglucosylation by UGGT. That process was demonstrated in yeast *alg5* and *alg6* mutants, which transfer unglucosylated Man9GlcNAc2 to protein [castro-1999-udpglc-er-transport-abstract].

## 5. Pathway Context: Assembly of the N-glycan Precursor and the Dolichol Cycle

N-linked glycosylation in the ER is a conserved two-phase process. An oligosaccharide is first assembled on dolichyl pyrophosphate and is then transferred en bloc by OST to Asn-X-Ser/Thr sequons. Assembly begins on the cytoplasmic side of the ER membrane and finishes in the lumen [aebi-2013-n-glycosylation-er-abstract; burda-1999-dolichol-pathway-abstract]. The three glucose residues at the non-reducing end of the A-branch are the final additions. Each comes from Dol-P-Glc: ALG6 adds the first α1,3-glucose, ALG8 the second α1,3-glucose, and ALG10 the terminal α1,2-glucose [runge-1984-yeast-glucosylation-mutants-abstract; runge-1986-alg8-glucosylation-abstract; uniprot-Q9Y673-entry]. Each of these glycosyltransferases is strictly specific for its acceptor structure, which enforces an ordered pathway in which mostly complete oligosaccharide is transferred to protein [burda-1999-ordered-llo-assembly-abstract]. ALG5 is therefore the branch point that supplies all glucose for LLO completion. Without it, cells transfer Man9GlcNAc2 instead of Glc3Man9GlcNAc2 [runge-1984-yeast-glucosylation-mutants-abstract].

The glucose residues are important for at least two reasons. First, OST prefers fully glucosylated LLO. In yeast, *alg5* and *alg6* mutants transfer oligosaccharides with no glucose, and *alg8* mutants transfer oligosaccharides with one glucose. All three secrete under-glycosylated forms of exoglucanase, but a single glucose already makes transfer more efficient. The glucotriose cap also affects which sequons are occupied [munoz-1994-alg-glucosylation-sequons-abstract]. Even CHO Lec15 cells, which lack Dol-P-Man synthase and accumulate truncated Man5GlcNAc2-PP-Dol, glucosylate a small fraction of that LLO, and that minor glucosylated fraction is what is mainly transferred to protein in vivo [stoll-1992-lec15-glucosylated-abstract]. Second, once transferred, the glucoses are trimmed by glucosidases I and II, which feeds the calnexin/calreticulin folding quality-control cycle. In yeast, oligosaccharides that lack the normal glucosylation are processed more slowly [runge-1986-alg8-glucosylation-abstract; aebi-2013-n-glycosylation-er-abstract].

ALG5 also depends on the dolichol cycle for its lipid substrate. Dol-P released in the lumen by the glucosyltransferases, together with Dol-P made by Dol-PP phosphatase after OST transfer, returns to the cytoplasmic leaflet. There it is reused for Glc-P-Dol, Man-P-Dol and GlcNAc-PP-Dol synthesis without passing through dolichol kinase. Generating lumenal Dol-PP in sealed calf-brain vesicles proportionally increased the rate of Glc-P-Dol synthesis [rush-2008-dolp-recycling-abstract; rush-2015-flippases-review-fulltext]. ALG5 thus competes with DPM1 (Dol-P-Man synthase, a GT2 paralogue) and with DPAGT1 for a shared, limited cytoplasmic pool of Dol-P [rush-2015-flippases-review-fulltext; maeda-2008-dpm-synthase-review-abstract]. In Lec35 (MPDU1-deficient) CHO cells, both Man-P-Dol and Glc-P-Dol are poorly used in vivo even though they are synthesised. Anand and colleagues showed that Lec35p, an ER membrane protein, is needed for all known Dol-P-monosaccharide-dependent reactions, including Glc-P-Dol-dependent glucosylation of the LLO. It is not needed for the transfer chemistry itself, and it seems to control how the donor is oriented in the membrane. Lec35p was more selective for Man-P-Dol than for Glc-P-Dol, so the authors suggested that an additional factor specific to Glc-P-Dol remains to be identified [anand-2001-lec35-mpdu1-abstract; rush-2015-flippases-review-fulltext]. MPDU1 is therefore a further requirement, downstream of ALG5, for using the ALG5 product. Recent reviews of dolichol synthesis and use place ALG5 in the same network of dolichol-linked donors and the disorders that affect it [pieters-2025-dolichol-disorders-review-abstract].

In organisms other than mammals, Dol-P-Glc can be put to other uses. *Trichomonas vaginalis* has very high Dol-P-Glc synthase activity and many ALG5 paralogues but no ALG6/8/10. It uses Dol-P-Glc as a donor for O-glycans [grabinska-2008-trichomonas-glcpdol-abstract]. There is no evidence for such a role in mammals, and the horse protein is expected to act in N-glycan precursor assembly.

## 6. Physiological Significance and Phenotypes of ALG5 Deficiency; Horse-specific Considerations

In vivo studies in animals and human genetics show what ALG5 contributes physiologically. In *Drosophila*, maternal loss of the ALG5 orthologue *wollknäuel* lowers N-glycosylation, causes ER stress and activates the unfolded protein response, and increases eIF2α phosphorylation. Embryos show posterior segmentation defects (through reduced translation of Caudal), reduced Dpp signalling and abnormal gastrulation [haecker-2008-wollknauel-alg5-abstract]. Later in development, *wol* mutants have reduced glucosylation and lower levels of N-glycosylated proteins such as the cuticle organiser Knickkopf, and their cuticle layering and apical plasma-membrane organisation are disrupted [shaik-2011-wollknauel-epidermis-abstract]. These effects are downstream consequences of the enzyme's main role, which is to supply the glucose donor that drives efficient N-glycosylation.

In humans, heterozygous loss-of-function variants in *ALG5* cause an atypical form of the ADPKD spectrum (PKD7). It presents with multiple small cysts in non-enlarged kidneys, few or no liver cysts, progressive interstitial fibrosis and late-onset kidney failure. Losing one ALG5 allele is enough to alter N-glycan synthesis in renal epithelial cells. ALG5 is needed for maturation of polycystin-1 and for its localisation to the plasma membrane and cilia [lemoine-2022-alg5-pkd-abstract]. An independent Irish cohort with the missense variant p.R79W confirmed the phenotype. In that cohort ALG5 was mislocalised between the ER and Golgi, N-glycosylated uromodulin was retained in the ER, and urinary uromodulin was reduced, whereas O-glycosylated MUC1 was unaffected. This specificity fits a defect confined to N-glycosylation [elhassan-2024-alg5-adpkd-fulltext]. Tissue surveys detected human ALG5 in pancreas, placenta, liver, heart, brain, kidney, skeletal muscle and lung [uniprot-Q9Y673-entry]. In a different domestic mammal, a genome-wide CRISPR screen in porcine intestinal epithelial cells identified ALG5 and ALG6 as host factors that the coronavirus TGEV needs, through N-glycosylation-dependent effects on its receptor aminopeptidase N [feng-2025-crispr-tgev-alg5-abstract]. Higher ALG5 expression in aged macaque hippocampus has been linked to N-glycosylation-dependent metabolic adaptation [zhu-2025-stt3a-alg5-macaque-abstract]. In human bone-marrow mesenchymal stem cells, knocking down ALG5 reduced N-glycosylation and stability of the glycine transporter SLC6A9 and shifted differentiation from bone-forming to fat-forming cells. Overexpressing ALG5 from an AAV vector reduced bone loss in ovariectomised mice [li-2025-alg5-slc6a9-osteoporosis-abstract]. In bovine mammary epithelial cells, which come from another domestic ungulate, silencing ALG5 lowered lipogenic gene expression and PI3K/AKT/mTOR signalling [meng-2024-alg5-milk-fat-abstract]. Both are best read as effects on particular ALG5-dependent client glycoproteins. These findings are correlative and pleiotropic, and they say nothing new about the enzyme's molecular function.

No phenotype or functional data on *ALG5* in horses were found. Horse-specific inference therefore has to rest on sequence. The pairwise alignment shows that A0A5F5PM72 matches human ALG5 residues 1–94 and 125–324 almost exactly (about 95% identity) but lacks residues 95–124 (alignment file). The other horse models (e.g., F6RYM5, A0A9L0R8Q6, A0A9L0TRZ9) contain this segment, with the motif "VIVVDDGS". Each of those models has its own shorter gaps elsewhere, so no single current horse model covers the full 324-residue canonical protein [uniprot-horse-ALG5-isoforms-entries]. The skipped segment exactly matches the alternatively spliced exon that is missing from human isoform 2 [uniprot-Q9Y673-entry]. It sits within the N-terminal part of the GT2 catalytic domain, where homologous GT-A enzymes such as GtrB place conserved aspartate residues that bind the divalent cation and the UDP-sugar [ardiccioni-2016-gtrb-structure-fulltext]. Its precise structural role in ALG5 has not been mapped. A0A5F5PM72 keeps the downstream "DADG" DxD-type motif and the PKD-associated arginines. However, losing an evolutionarily conserved ~30-residue segment from the catalytic core could reduce or abolish activity. Whether this isoform is catalytically active has not been tested in any species. The functional annotation in this report (EC 2.4.1.117, ER membrane, N-glycan precursor glucosylation) should therefore be read as applying to the horse ALG5 gene product in general. For this specific splice form it is an orthology-based inference that still needs confirmation.

## 7. Synthesis and Evidence Assessment

Taken together, the evidence gives a consistent picture of horse ALG5. The protein is an ER membrane GT2 glycosyltransferase whose catalytic domain faces the cytosol. It transfers glucose from UDP-α-D-glucose to dolichyl phosphate, making β-D-glucosyl phosphodolichol. This is the only glucosyl donor for the ALG6/ALG8/ALG10 steps that complete Glc3Man9GlcNAc2-PP-Dol, the substrate OST uses for protein N-glycosylation. The core evidence is experimental and comes from other species. It includes yeast genetics and enzymology [runge-1984-yeast-glucosylation-mutants-abstract; heesen-1994-alg5-yeast-abstract], photoaffinity labelling and purification of the mammalian enzyme [palamarczyk-1990-glcpdol-35kda-abstract; drake-1990-35kda-glcpdol-abstract; shailubhai-1990-rat-mammary-photoaffinity-abstract; gold-1983-plasmacytoma-glucosyltransferase-abstract; matern-1990-human-liver-glcpdol-synthase-abstract], cross-species complementation by human, fly and protist orthologues [imbach-1999-alg6-cdg-ic-abstract; haecker-2008-wollknauel-alg5-abstract; grabinska-2008-trichomonas-glcpdol-abstract], membrane topology studies in mammalian microsomes [rush-1998-glcpdol-topology-abstract; rush-1998-glcpdol-transbilayer-abstract], and human genetics with cell-biological follow-up [lemoine-2022-alg5-pkd-abstract; elhassan-2024-alg5-adpkd-fulltext]. Structural and evolutionary understanding is still indirect and comes from bacterial and archaeal homologues and from phylogenomics [ardiccioni-2016-gtrb-structure-fulltext; larkin-2013-alternate-pathway-fulltext; lombard-2016-nglycosylation-evolution-fulltext]. For the horse, the evidence is limited to sequence orthology and automatic annotation [uniprot-A0A5F5PM72-entry], and the transcript model for this accession raises the specific splice-isoform question described above. Suitable GO-style annotations by orthology would be: molecular function, dolichyl-phosphate β-glucosyltransferase activity (GO:0004581); cellular component, endoplasmic reticulum membrane (GO:0005789); and biological process, protein N-linked glycosylation / dolichol-linked oligosaccharide biosynthesis.

## Open Questions

Several questions remain open, both about ALG5 in general and about the horse gene. The most immediate is whether the 294-residue isoform represented by A0A5F5PM72, which lacks the conserved segment corresponding to human residues 95–124, is a real, expressed and catalytically competent horse transcript. RNA-seq or long-read support for exon skipping in horse tissues, followed by expression and assay of both the full-length and the exon-skipped horse proteins in a yeast *alg5Δ* complementation system, would settle this. It would also tell us whether human isoform 2 has any activity. A related problem is that no current horse gene model encodes the full canonical 324-residue protein, which suggests that the horse ALG5 annotation should be curated against the human RefSeq and long-read data.

Several mechanistic questions also remain for ALG5 in general. No experimental eukaryotic ALG5 structure has been determined, so the substrate-binding residues, the A-loop, and the way the soluble catalytic domain reaches dolichyl phosphate in the membrane are known only from homology with GtrB and DPMS. Membrane topology is still uncertain, with a single signal-anchor helix predicted for mammalian ALG5 and several spans proposed for yeast Alg5p. The Glc-P-Dol flippase that moves the ALG5 product into the lumen has not been identified, nor has the proposed Glc-P-Dol-selective counterpart of the Lec35/MPDU1 utilisation factor, and neither has any physical coupling between ALG5, that flippase and the lumenal ALG6/8/10 glucosyltransferases. In kidney, it is unclear why haploinsufficiency for a housekeeping enzyme mainly affects heavily glycosylated proteins such as polycystin-1 and uromodulin, and whether horses carry comparable loss-of-function alleles linked to renal cystic disease. Equine population-genomic data could be used to look for such variants. Mammalian enzymology dates largely from the 1980s and 1990s and used partially purified or native enzyme. A modern kinetic characterisation of recombinant mammalian ALG5 is missing, including its preferences for dolichol chain length, its divalent-cation requirement and its phospholipid dependence. Finally, regulation of ALG5 expression and of the Dol-P pool it shares with DPM1 and DPAGT1 has not been studied in horses or in other non-model mammals.

## References

- [aebi-2013-n-glycosylation-er] Aebi M. N-linked protein glycosylation in the ER. *Biochim Biophys Acta* 2013. PMID: 23583305. DOI: 10.1016/j.bbamcr.2013.04.001.
- [anand-2001-lec35-mpdu1] Anand M, Rush JS, Ray S, Doucey MA, Weik J, Ware FE, Hofsteenge J, Waechter CJ, Lehrman MA. Requirement of the Lec35 gene for all known classes of monosaccharide-P-dolichol-dependent glycosyltransferase reactions in mammals. *Mol Biol Cell* 2001;12(2):487-501. PMID: 11179430. PMCID: PMC30958. DOI: 10.1091/mbc.12.2.487.
- [ardiccioni-2016-gtrb-structure] Ardiccioni C, Clarke OB, Tomasek D, et al. Structure of the polyisoprenyl-phosphate glycosyltransferase GtrB and insights into the mechanism of catalysis. *Nat Commun* 2016;7:10175. PMID: 26729507. PMCID: PMC4728340. DOI: 10.1038/ncomms10175.
- [burda-1999-dolichol-pathway] Burda P, Aebi M. The dolichol pathway of N-linked glycosylation. *Biochim Biophys Acta* 1999. PMID: 9878760. DOI: 10.1016/s0304-4165(98)00127-5.
- [burda-1999-ordered-llo-assembly] Burda P, Jakob CA, Beinhauer J, Hegemann JH, Aebi M. Ordered assembly of the asymmetrically branched lipid-linked oligosaccharide in the endoplasmic reticulum is ensured by the substrate specificity of the individual glycosyltransferases. *Glycobiology* 1999;9(6):617-25. PMID: 10336995. DOI: 10.1093/glycob/9.6.617.
- [castro-1999-udpglc-er-transport] Castro O, Chen LY, Parodi AJ, Abeijón C. Uridine diphosphate-glucose transport into the endoplasmic reticulum of *Saccharomyces cerevisiae*: in vivo and in vitro evidence. *Mol Biol Cell* 1999;10(4):1019-30. PMID: 10198054. PMCID: PMC25230. DOI: 10.1091/mbc.10.4.1019.
- [drake-1990-35kda-glcpdol] Drake R, Palamarczyk G, Haley B, Lennarz WJ. Evidence for the involvement of a 35-kDa membrane protein in the synthesis of glucosylphosphoryldolichol. *Biosci Rep* 1990;10(1):61-8. PMID: 2140279. DOI: 10.1007/BF01116852.
- [dsouza-schorey-1994-dolichol-vs-polyprenol] D'Souza-Schorey C, McLachlan KR, Krag SS, Elbein AD. Mammalian glycosyltransferases prefer glycosyl phosphoryl dolichols rather than glycosyl phosphoryl polyprenols as substrates for oligosaccharide synthesis. *Arch Biochem Biophys* 1994;308(2):497-503. PMID: 8109980. DOI: 10.1006/abbi.1994.1070.
- [elhassan-2024-alg5-adpkd] Elhassan EAE, Kmochová T, Benson KA, Fennelly NK, Barešová V, et al. A Novel Monoallelic ALG5 Variant Causing Late-Onset ADPKD and Tubulointerstitial Fibrosis. *Kidney Int Rep* 2024. PMID: 39081747. PMCID: PMC11284371. DOI: 10.1016/j.ekir.2024.04.031.
- [feng-2025-crispr-tgev-alg5] Feng Z, He X, Lin M, et al. Genome-wide CRISPR screen identifies ALG5, ALG6, NF2, and FUT8 as key host proteins involved in transmissible gastroenteritis virus infection. *Int J Biol Macromol* 2025. PMID: 41205942. DOI: 10.1016/j.ijbiomac.2025.148770.
- [gold-1983-plasmacytoma-glucosyltransferase] Gold P, Green M. Partial purification and properties of a murine plasmacytoma glucosyltransferase. *J Biol Chem* 1983;258(21):12967-75. PMID: 6226662.
- [grabinska-2008-trichomonas-glcpdol] Grabińska KA, Ghosh SK, Guan Z, Cui J, Raetz CR, Robbins PW, Samuelson J. Dolichyl-phosphate-glucose is used to make O-glycans on glycoproteins of *Trichomonas vaginalis*. *Eukaryot Cell* 2008;7(8):1344-51. PMID: 18552282. PMCID: PMC2519777. DOI: 10.1128/EC.00061-08.
- [haecker-2008-wollknauel-alg5] Haecker A, Bergman M, Neupert C, Moussian B, Luschnig S, Aebi M, Mannervik M. Wollknauel is required for embryo patterning and encodes the Drosophila ALG5 UDP-glucose:dolichyl-phosphate glucosyltransferase. *Development* 2008;135(10):1745-9. PMID: 18403407. DOI: 10.1242/dev.020891.
- [heesen-1994-alg5-yeast] Heesen S, Lehle L, Weissmann A, Aebi M. Isolation of the ALG5 locus encoding the UDP-glucose:dolichyl-phosphate glucosyltransferase from *Saccharomyces cerevisiae*. *Eur J Biochem* 1994;224(1):71-9. PMID: 8076653. DOI: 10.1111/j.1432-1033.1994.tb19996.x.
- [imbach-1999-alg6-cdg-ic] Imbach T, Burda P, Kuhnert P, Wevers RA, Aebi M, Berger EG, Hennet T. A mutation in the human ortholog of the *Saccharomyces cerevisiae* ALG6 gene causes carbohydrate-deficient glycoprotein syndrome type-Ic. *Proc Natl Acad Sci U S A* 1999;96(12):6982-7. PMID: 10359825. PMCID: PMC22030. DOI: 10.1073/pnas.96.12.6982.
- [larkin-2013-alternate-pathway] Larkin A, Chang MM, Whitworth GE, Imperiali B. Biochemical evidence for an alternate pathway in N-linked glycoprotein biosynthesis. *Nat Chem Biol* 2013. PMID: 23624439. PMCID: PMC3661703. DOI: 10.1038/nchembio.1249.
- [lemoine-2022-alg5-pkd] Lemoine H, Raud L, Foulquier F, Sayer JA, Lambert B, Olinger E, et al. Monoallelic pathogenic ALG5 variants cause atypical polycystic kidney disease and interstitial fibrosis. *Am J Hum Genet* 2022;109(8):1484-1499. PMID: 35896117. PMCID: PMC9388391. DOI: 10.1016/j.ajhg.2022.06.013.
- [li-2025-alg5-slc6a9-osteoporosis] Li Q, Liu W, Zhang Y, et al. ALG5 downregulation inhibits osteogenesis and promotes adipogenesis by regulating the N-glycosylation of SLC6A9 in osteoporosis. *Cell Mol Life Sci* 2025;82(1):35. PMID: 39760914. DOI: 10.1007/s00018-024-05566-9.
- [lombard-2016-nglycosylation-evolution] Lombard J. The multiple evolutionary origins of the eukaryotic N-glycosylation pathway. *Biol Direct* 2016;11:36. PMID: 27492357. PMCID: PMC4973528. DOI: 10.1186/s13062-016-0137-2.
- [maeda-2008-dpm-synthase-review] Maeda Y, Kinoshita T. Dolichol-phosphate mannose synthase: structure, function and regulation. *Biochim Biophys Acta* 2008. PMID: 18387370. DOI: 10.1016/j.bbagen.2008.03.005.
- [matern-1990-human-liver-glcpdol-synthase] Matern H, Bolz R, Matern S. Isolation and characterization of UDP-glucose dolichyl-phosphate glucosyltransferase from human liver. *Eur J Biochem* 1990;190(1):99-105. PMID: 2163838. DOI: 10.1111/j.1432-1033.1990.tb15551.x.
- [meng-2024-alg5-milk-fat] Meng Y, Lyu CC, He YT, Che HY, Jiang H, Zhang JB, Tang HY, Yuan B. ALG5 Regulates STF-62247-Induced Milk Fat Synthesis via the mTOR Signaling Pathway. *J Agric Food Chem* 2024;72(26):14620-14629. PMID: 38885170. DOI: 10.1021/acs.jafc.3c07812.
- [munoz-1994-alg-glucosylation-sequons] Muñoz MD, Hernández LM, Basco R, Andaluz E, Larriba G. Glycosylation of yeast exoglucanase sequons in alg mutants deficient in the glucosylation steps of the lipid-linked oligosaccharide. Presence of glucotriose unit in Dol-PP-GlcNAc2Man9Glc3 influences both glycosylation efficiency and selection of N-linked sites. *Biochim Biophys Acta* 1994;1201(3):361-6. PMID: 7803465. DOI: 10.1016/0304-4165(94)90063-9.
- [palamarczyk-1990-glcpdol-35kda] Palamarczyk G, Drake R, Haley B, Lennarz WJ. Evidence that the synthesis of glucosylphosphodolichol in yeast involves a 35-kDa membrane protein. *Proc Natl Acad Sci U S A* 1990;87(7):2666-70. PMID: 2138781. PMCID: PMC53751. DOI: 10.1073/pnas.87.7.2666.
- [pieters-2025-dolichol-disorders-review] Pieters E, Jaeken J, Wilson MP. Genetic disorders of dolichol synthesis and utilization. *Mol Genet Metab* 2025;146(1-2):109226. PMID: 40902550. DOI: 10.1016/j.ymgme.2025.109226.
- [runge-1984-yeast-glucosylation-mutants] Runge KW, Huffaker TC, Robbins PW. Two yeast mutations in glucosylation steps of the asparagine glycosylation pathway. *J Biol Chem* 1984;259(1):412-7. PMID: 6423630. DOI: 10.1016/s0021-9258(17)43676-3.
- [runge-1986-alg8-glucosylation] Runge KW, Robbins PW. A new yeast mutation in the glucosylation steps of the asparagine-linked glycosylation pathway. Formation of a novel asparagine-linked oligosaccharide containing two glucose residues. *J Biol Chem* 1986;261(33):15582-90. PMID: 3536907. DOI: 10.1016/s0021-9258(18)66754-7.
- [rush-1998-glcpdol-topology] Rush JS, Waechter CJ. Topological studies on the enzymes catalyzing the biosynthesis of Glc-P-dolichol and the triglucosyl cap of Glc3Man9GlcNAc2-P-P-dolichol in microsomal vesicles from pig brain: use of the processing glucosidases I/II as latency markers. *Glycobiology* 1998;8(12):1207-13. PMID: 9858642. DOI: 10.1093/glycob/8.12.1207.
- [rush-1998-glcpdol-transbilayer] Rush JS, van Leyen K, Ouerfelli O, Wolucka B, Waechter CJ. Transbilayer movement of Glc-P-dolichol and its function as a glucosyl donor: protein-mediated transport of a water-soluble analog into sealed ER vesicles from pig brain. *Glycobiology* 1998;8(12):1195-205. PMID: 9858641. DOI: 10.1093/glycob/8.12.1195.
- [rush-2008-dolp-recycling] Rush JS, Gao N, Lehrman MA, Waechter CJ. Recycling of dolichyl monophosphate to the cytoplasmic leaflet of the endoplasmic reticulum after the cleavage of dolichyl pyrophosphate on the lumenal monolayer. *J Biol Chem* 2008;283(7):4087-93. PMID: 18077451. DOI: 10.1074/jbc.M707067200.
- [rush-2015-flippases-review] Rush JS. Role of Flippases in Protein Glycosylation in the Endoplasmic Reticulum. *Lipid Insights* 2015. PMID: 26917968. PMCID: PMC4762491. DOI: 10.4137/LPI.S31784.
- [shaik-2011-wollknauel-epidermis] Shaik KS, Pabst M, Schwarz H, Altmann F, Moussian B. The Alg5 ortholog Wollknäuel is essential for correct epidermal differentiation during Drosophila late embryogenesis. *Glycobiology* 2011;21(6):743-56. PMID: 21199819. DOI: 10.1093/glycob/cwq213.
- [shailubhai-1990-rat-mammary-photoaffinity] Shailubhai K, Illeperuma C, Tayal M, Vijay IK. Photoaffinity labeling of glucosyltransferase of the dolichol cycle from rat mammary gland. *J Biol Chem* 1990;265(24):14105-8. PMID: 2143759.
- [stagljar-1998-split-ubiquitin] Stagljar I, Korostensky C, Johnsson N, te Heesen S. A genetic system based on split-ubiquitin for the analysis of interactions between membrane proteins in vivo. *Proc Natl Acad Sci U S A* 1998;95(9):5187-92. PMID: 9560251. PMCID: PMC20236. DOI: 10.1073/pnas.95.9.5187.
- [stoll-1992-lec15-glucosylated] Stoll J, Cacan R, Verbert A, Krag SS. Lec15 cells transfer glucosylated oligosaccharides to protein. *Arch Biochem Biophys* 1992;299(2):225-31. PMID: 1444460. DOI: 10.1016/0003-9861(92)90268-2.
- [wade-2009-horse-genome] Wade CM, Giulotto E, Sigurdsson S, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science* 2009;326:865-867. PMID: 19892987. PMCID: PMC3785132. DOI: 10.1126/science.1178158.
- [zhu-2025-stt3a-alg5-macaque] Zhu GH, He R, Yang ZY, et al. Compensatory roles of STT3A and ALG5 in glucose metabolism of aged macaque hippocampus. *Brain* 2025. PMID: 40908792. DOI: 10.1093/brain/awaf282.
- [uniprot-A0A5F5PM72] UniProt Consortium. UniProtKB/TrEMBL entry A0A5F5PM72 (ALG5, *Equus caballus*), entry version 28. https://rest.uniprot.org/uniprotkb/A0A5F5PM72.txt
- [uniprot-Q9Y673] UniProt Consortium. UniProtKB/Swiss-Prot entry Q9Y673 (ALG5_HUMAN). https://rest.uniprot.org/uniprotkb/Q9Y673.txt
- [uniprot-horse-ALG5-isoforms] UniProt Consortium. UniProtKB search results for gene ALG5 in *Equus caballus* (taxon 9796), FASTA. https://rest.uniprot.org/uniprotkb/search?query=gene:ALG5+AND+organism_id:9796&format=fasta


## Citations

1. aebi-2013-n-glycosylation-er-abstract.md
2. aebi-2013-n-glycosylation-er-summary.md
3. anand-2001-lec35-mpdu1-abstract.md
4. anand-2001-lec35-mpdu1-summary.md
5. ardiccioni-2016-gtrb-structure-abstract.md
6. ardiccioni-2016-gtrb-structure-fulltext.txt
7. ardiccioni-2016-gtrb-structure-summary.md
8. burda-1999-dolichol-pathway-abstract.md
9. burda-1999-dolichol-pathway-summary.md
10. burda-1999-ordered-llo-assembly-abstract.md
11. burda-1999-ordered-llo-assembly-summary.md
12. castro-1999-udpglc-er-transport-abstract.md
13. castro-1999-udpglc-er-transport-summary.md
14. drake-1990-35kda-glcpdol-abstract.md
15. drake-1990-35kda-glcpdol-summary.md
16. dsouza-schorey-1994-dolichol-vs-polyprenol-abstract.md
17. dsouza-schorey-1994-dolichol-vs-polyprenol-summary.md
18. elhassan-2024-alg5-adpkd-abstract.md
19. elhassan-2024-alg5-adpkd-fulltext.txt
20. elhassan-2024-alg5-adpkd-summary.md
21. feng-2025-crispr-tgev-alg5-abstract.md
22. feng-2025-crispr-tgev-alg5-summary.md
23. gold-1983-plasmacytoma-glucosyltransferase-abstract.md
24. gold-1983-plasmacytoma-glucosyltransferase-summary.md
25. grabinska-2008-trichomonas-glcpdol-abstract.md
26. grabinska-2008-trichomonas-glcpdol-summary.md
27. haecker-2008-wollknauel-alg5-abstract.md
28. haecker-2008-wollknauel-alg5-summary.md
29. heesen-1994-alg5-yeast-abstract.md
30. heesen-1994-alg5-yeast-summary.md
31. imbach-1999-alg6-cdg-ic-abstract.md
32. imbach-1999-alg6-cdg-ic-summary.md
33. karaoglu-1995-ost3-abstract.md
34. karaoglu-1995-ost3-summary.md
35. larkin-2013-alternate-pathway-abstract.md
36. larkin-2013-alternate-pathway-fulltext.txt
37. larkin-2013-alternate-pathway-summary.md
38. lemoine-2022-alg5-pkd-abstract.md
39. lemoine-2022-alg5-pkd-summary.md
40. li-2025-alg5-slc6a9-osteoporosis-abstract.md
41. li-2025-alg5-slc6a9-osteoporosis-summary.md
42. lombard-2016-nglycosylation-evolution-abstract.md
43. lombard-2016-nglycosylation-evolution-fulltext.txt
44. lombard-2016-nglycosylation-evolution-summary.md
45. maeda-2008-dpm-synthase-review-abstract.md
46. maeda-2008-dpm-synthase-review-summary.md
47. matern-1990-human-liver-glcpdol-synthase-abstract.md
48. matern-1990-human-liver-glcpdol-synthase-summary.md
49. meng-2024-alg5-milk-fat-abstract.md
50. meng-2024-alg5-milk-fat-summary.md
51. munoz-1994-alg-glucosylation-sequons-abstract.md
52. munoz-1994-alg-glucosylation-sequons-summary.md
53. palamarczyk-1990-glcpdol-35kda-abstract.md
54. palamarczyk-1990-glcpdol-35kda-summary.md
55. pieters-2025-dolichol-disorders-review-abstract.md
56. pieters-2025-dolichol-disorders-review-summary.md
57. runge-1984-yeast-glucosylation-mutants-abstract.md
58. runge-1984-yeast-glucosylation-mutants-summary.md
59. runge-1986-alg8-glucosylation-abstract.md
60. runge-1986-alg8-glucosylation-summary.md
61. rush-1998-glcpdol-topology-abstract.md
62. rush-1998-glcpdol-topology-summary.md
63. rush-1998-glcpdol-transbilayer-abstract.md
64. rush-1998-glcpdol-transbilayer-summary.md
65. rush-2008-dolp-recycling-abstract.md
66. rush-2008-dolp-recycling-summary.md
67. rush-2015-flippases-review-abstract.md
68. rush-2015-flippases-review-fulltext.txt
69. rush-2015-flippases-review-summary.md
70. shaik-2011-wollknauel-epidermis-abstract.md
71. shaik-2011-wollknauel-epidermis-summary.md
72. shailubhai-1990-rat-mammary-photoaffinity-abstract.md
73. shailubhai-1990-rat-mammary-photoaffinity-summary.md
74. stagljar-1998-split-ubiquitin-abstract.md
75. stagljar-1998-split-ubiquitin-summary.md
76. stoll-1992-lec15-glucosylated-abstract.md
77. stoll-1992-lec15-glucosylated-summary.md
78. uniprot-A0A5F5PM72-entry.fasta
79. uniprot-A0A5F5PM72-entry.txt
80. uniprot-A0A5F5PM72-summary.md
81. uniprot-Q9Y673-entry.txt
82. uniprot-Q9Y673-summary.md
83. uniprot-horse-ALG5-isoforms-entries.fasta
84. uniprot-horse-ALG5-isoforms-summary.md
85. wade-2009-horse-genome-abstract.md
86. wade-2009-horse-genome-summary.md
87. zhu-2025-stt3a-alg5-macaque-abstract.md
88. zhu-2025-stt3a-alg5-macaque-summary.md