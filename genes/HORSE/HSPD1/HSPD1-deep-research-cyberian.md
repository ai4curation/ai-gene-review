---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T02:24:03.557165'
end_time: '2026-10-26T02:44:10.167801'
duration_seconds: 1206.61
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: HSPD1
  gene_symbol: HSPD1
  uniprot_accession: F6Z587
  protein_description: 'RecName: Full=60 kDa heat shock protein, mitochondrial {ECO:0000256|ARBA:ARBA00019981};
    EC=5.6.1.7 {ECO:0000256|ARBA:ARBA00012198}; AltName: Full=60 kDa chaperonin {ECO:0000256|ARBA:ARBA00029756};
    AltName: Full=Chaperonin 60 {ECO:0000256|ARBA:ARBA00031799}; AltName: Full=Heat
    shock protein 60 {ECO:0000256|ARBA:ARBA00030005}; AltName: Full=Mitochondrial
    matrix protein P1 {ECO:0000256|ARBA:ARBA00078324};'
  gene_info: Name=HSPD1 {ECO:0000313|VGNC:VGNC:51461};
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the chaperonin (HSP60) family.
  protein_domains: Chaperonin_Cpn60_CS. (IPR018370); Cpn60/GroEL. (IPR001844); Cpn60/GroEL/TCP-1.
    (IPR002423); GroEL-like_apical_dom_sf. (IPR027409); GROEL-like_equatorial_sf.
    (IPR027413)
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
- **UniProt Accession:** F6Z587
- **Protein Description:** RecName: Full=60 kDa heat shock protein, mitochondrial {ECO:0000256|ARBA:ARBA00019981}; EC=5.6.1.7 {ECO:0000256|ARBA:ARBA00012198}; AltName: Full=60 kDa chaperonin {ECO:0000256|ARBA:ARBA00029756}; AltName: Full=Chaperonin 60 {ECO:0000256|ARBA:ARBA00031799}; AltName: Full=Heat shock protein 60 {ECO:0000256|ARBA:ARBA00030005}; AltName: Full=Mitochondrial matrix protein P1 {ECO:0000256|ARBA:ARBA00078324};
- **Gene Information:** Name=HSPD1 {ECO:0000313|VGNC:VGNC:51461};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the chaperonin (HSP60) family.
- **Key Domains:** Chaperonin_Cpn60_CS. (IPR018370); Cpn60/GroEL. (IPR001844); Cpn60/GroEL/TCP-1. (IPR002423); GroEL-like_apical_dom_sf. (IPR027409); GROEL-like_equatorial_sf. (IPR027413)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HSPD1" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HSPD1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HSPD1** (gene ID: HSPD1, UniProt: F6Z587) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# HSPD1 (60 kDa heat shock protein, mitochondrial; Hsp60) in the horse, *Equus caballus* (UniProt F6Z587)

## 1. Introduction and summary

HSPD1 encodes Hsp60 (also called chaperonin 60, cpn60, or mitochondrial matrix protein P1). It is the large subunit of the group I (type I) chaperonin of the mitochondrial matrix. Together with its co-chaperonin Hsp10 (encoded by HSPE1), it forms a cage that binds non-native polypeptides, closes over them in an ATP-dependent reaction cycle, and lets them fold in isolation from the crowded matrix. Its main clients are proteins newly imported into mitochondria and matrix proteins that have unfolded under stress [cheng-1989-hsp60-yeast-abstract][ostermann-1989-folding-mitochondria-abstract][braxton-2024-apical-domain-abstract]. The reaction is an ATP-driven folding activity. UniProt records it as EC 5.6.1.7, ATP + H2O + an unfolded polypeptide = ADP + phosphate + a folded polypeptide, in an automatic annotation transferred from characterized orthologs [uniprot-F6Z587-entry]. Hsp60 has no single small-molecule substrate. Its "substrates" are a broad range of unfolded or partly folded proteins. In human cells these include about half of all annotated matrix proteins, among them parts of the mitochondrial translation machinery, the respiratory chain and the protein-quality-control system [bie-2020-interactors-abstract].

The identity of the target is not in doubt. The gene symbol HSPD1 (VGNC:51461), the protein name, the chaperonin (HSP60) family assignment and the Cpn60/GroEL InterPro domains all agree, and the horse sequence is almost identical to human HSPD1 (P10809) [uniprot-F6Z587-entry]. Our own alignment found one notable difference: F6Z587 lacks 32 residues that are present in the human protein. Comparison with the Ensembl gene model shows that F6Z587 corresponds to a non-canonical, 11-exon transcript missing one coding exon, while the canonical 12-exon horse transcript encodes a full-length protein (NOTES-sequence-analysis.md). There is little direct experimental work on horse Hsp60. A few equine studies detect the protein in testis, skeletal muscle and joint tissue [cinone-2024-cryptorchid-testis-abstract][kinnunen-2009-lipoic-acid-horse-abstract][linde-2025-equine-oa-abstract]. Almost everything known about its molecular function therefore comes from orthology to the well-studied yeast, human and other mammalian proteins, and from the bacterial paralogue GroEL. This report states that inference explicitly wherever it is used.

## 2. Gene identity, sequence and gene structure in the horse

The UniProt record F6Z587 is an unreviewed TrEMBL entry of 541 amino acids. It derives from the Thoroughbred reference genome [wade-2009-horse-genome-abstract] and sits on horse chromosome 18 [uniprot-F6Z587-entry]. Its protein-existence level is 1 ("evidence at protein level"), based on a PeptideAtlas proteomics identification. Its function, catalytic activity, subunit and subcellular-location statements are all automatic ARBA rules rather than horse-specific curation [uniprot-F6Z587-entry]. The InterPro signatures are a Cpn60/GroEL family domain, a chaperonin Cpn60 conserved site (PROSITE PS00296), two Pfam Cpn60_TCP1 segments, and GroEL-like apical and equatorial domain superfamilies [uniprot-F6Z587-entry]. Together these place the protein firmly in the group I chaperonin family. (Database annotations also include "chaperonin-containing T-complex", which refers to the unrelated group II CCT/TRiC complex of the cytosol. It looks like an over-propagated electronic annotation and should not be read as a localization claim [uniprot-F6Z587-entry].)

We aligned F6Z587 globally with human HSPD1 (P10809, 573 aa). All 541 horse residues aligned and 527 of them (97.4%) were identical. They included the presequence-like N-terminus (MLRLP…), the GDGTTT nucleotide-binding loop of the equatorial domain, and the C-terminal glycine-methionine-rich tail (…GMGGMGGMGGGMGGGMF) (NOTES-sequence-analysis.md). The single gap was a 32-residue segment, human precursor residues 171–202 (VATISANGDKEIGNIISDAMKKVGRKGVITVK), which is absent from F6Z587. Removing the 26-residue mitochondrial matrix-targeting signal gives a mature protein of 547 residues in human [gomez-llorente-2020-single-double-ring-fulltext]. The missing segment therefore maps to mature residues ~145–176. That falls inside the intermediate (hinge) domain, which spans mature residues 138–191 and 375–411, between the equatorial ATP-binding domain (1–137, 411–526) and the apical domain (192–374) [gomez-llorente-2020-single-double-ring-fulltext]. The Ensembl gene ENSECAG00000008968 has four transcripts. Its canonical 12-exon transcript encodes a 587-residue protein. From the conserved MLRLP start, that protein is the same length as human Hsp60 (573 aa) and 97.6% identical to it, and deleting residues 171–202 from it reproduces F6Z587 exactly. F6Z587 corresponds to an 11-exon transcript (NOTES-sequence-analysis.md). This matches the 12-exon structure reported for human HSPD1 [bross-2016-hspd1-mutations-fulltext]. F6Z587 is therefore most likely an exon-skipped splice model or a gene-prediction artefact, not the main functional product. An intermediate domain lacking about 32 residues of its first strand-helix segment is unlikely to support the hinge movements needed for the folding cycle, though that has not been tested. The canonical model also has a 14-residue extension upstream of the conserved initiator methionine, which may reflect an upstream start-codon prediction (NOTES-sequence-analysis.md).

In humans, HSPD1 and HSPE1 lie head-to-head at 2q33.1 and share a bidirectional promoter. This arrangement is conserved from *C. elegans* to humans and co-regulates the two chaperonin subunits [bross-2016-hspd1-mutations-fulltext]. In the horse, an unnamed protein-coding gene (ENSECAG00000055696) begins on the opposite strand a few hundred bases from the 5′ end of HSPD1, where HSPE1 would be expected. We did not verify its identity (NOTES-sequence-analysis.md). Consistent with this co-regulation, inactivating one Hspd1 allele in mice also lowered Hsp10 expression [christensen-2010-knockout-abstract].

## 3. Molecular function: an ATP-driven protein-folding cage

Hsp60 was first defined as a folding machine through yeast genetics and biochemistry. Cheng and colleagues showed that nuclear-encoded mitochondrial hsp60 is needed for imported matrix proteins to assemble into oligomeric complexes, and recognized it as a relative of *E. coli* GroEL and the chloroplast Rubisco-binding protein [cheng-1989-hsp60-yeast-abstract]. Ostermann and colleagues showed that imported proteins form complexes with hsp60 and fold in a reaction that needs ATP hydrolysis before they are released, and proposed that hsp60 catalyses protein folding [ostermann-1989-folding-mitochondria-abstract]. The human protein was cloned as "P1", a mitochondrial protein 40–50% identical to GroEL, the mycobacterial 65-kDa antigen and the Rubisco-binding protein. Its chaperonin role was proposed from that homology [jindal-1989-human-p1-abstract]. Molecular chaperones as a whole, including the chaperonins, keep proteins folded and soluble (proteostasis) by preventing aggregation and promoting productive folding [hartl-2011-chaperones-abstract].

The mammalian mitochondrial chaperonin works like GroEL but differs from it in important ways. Recombinant mammalian cpn60 purified from *E. coli* formed a single heptameric toroid rather than GroEL's double ring. With K⁺ and MgATP, and with mammalian but not bacterial cpn10, it refolded Rubisco from an unfolded state, showing that a single heptameric ring is the minimal functional unit [viitanen-1992-single-ring-abstract]. GroEL/Hsp60 chimeras showed that Hsp60/Hsp10 can fold proteins *in vitro* and *in vivo* without forming a two-ring structure. In this "one-stroke" mode, Hsp60 releases its co-chaperonin and substrate by a mechanism different from GroEL's two-ring allosteric switch [nielsen-1998-single-ring-abstract]. Even so, human Hsp60–Hsp10 can take over all essential *in vivo* functions of GroEL–GroES in *E. coli* [nielsen-1999-single-ring-substitute-abstract]. This finding underlies the bacterial complementation assay used to test disease variants (Section 7). The mitochondrial chaperonin is also strict about its partner: mitochondrial Hsp60 refolds proteins only with mitochondrial Hsp10. Specific apical-domain substitutions (E321K, or R264K/E358K) let human Hsp60 work with GroES by raising co-chaperonin affinity and altering allosteric signalling [parnas-2012-cochaperonin-specificity-abstract]. Reviews of organellar chaperonins stress these features as the main ways mitochondrial and chloroplast chaperonins differ from the bacterial model [levy-rimler-2002-type1-abstract].

The ATPase activity is what drives the cycle. In solution, mammalian mt-cpn60 is in dynamic equilibrium between monomers, heptameric single rings and tetradecameric double rings, and ATP plus mt-cpn10 favours the double ring [levy-rimler-2001-nucleotides-abstract]. High ADP concentrations inhibited neither malate dehydrogenase refolding nor ATP hydrolysis by mt-cpn60 in the presence of mt-cpn10. This suggests that, unlike GroEL, the mitochondrial system does not bind ADP well at the opposite ("trans") ring [levy-rimler-2001-nucleotides-abstract]. Cell-based work confirms that ATP hydrolysis is needed for function in mammalian cells. An Asp423Ala substitution in the Hsp60 ATPase domain impaired folding of mitochondrially targeted GFP, a model Hsp60 substrate, in human HEK293 cells. It also stopped proliferation and progressively lowered mitochondrial membrane potential [bie-2011-deficiency-model-abstract]. In mechanistic terms, the "enzymatic" function of horse Hsp60 is therefore ATP hydrolysis coupled to the capture, encapsulation and release of non-native polypeptides. The GDGTTT nucleotide-binding loop in the horse protein is fully conserved (Section 2), so this activity is expected to be conserved too.

## 4. Structural basis of the reaction cycle

Structural studies over the past decade have explained how the mammalian chaperonin cycles. The first crystal structure of any mammalian type I chaperonin complex (3.15 Å) captured a double-ring, football-shaped human Hsp60₁₄–(Hsp10₇)₂ complex. It showed asymmetry between subunits within each ring, the same nucleotide state in both rings, and a different inter-ring subunit arrangement from GroEL. The authors interpreted it as an early dissociation intermediate [nisemblat-2015-football-abstract]. Later work produced a crystal structure of an ATP ground-state mimic (ADP:BeF₃) football, plus cryo-EM structures of an ADP football and a single-ring "half-football" [gomez-llorente-2020-single-double-ring-abstract]. These structures explain why ring formation depends on nucleotide. They also show that both rings carry the same nucleotide, which fits the absence of the negative inter-ring cooperativity typical of GroEL. In the ground state, a two-fold-symmetric hydrogen bond and a salt bridge hold the two rings together. In the ADP football only the hydrogen bond remains, and the rings are ready to split [gomez-llorente-2020-single-double-ring-abstract]. Engineered variants locked as single or double rings were both active in refolding assays, and the single-ring variant complemented GroEL-deficient bacteria as well as the wild type. Single- and double-ring complexes therefore coexist in the functional cycle [gomez-llorente-2020-single-double-ring-abstract]. The obligate-ring variants assisted citrate synthase folding as well as wild type but were impaired with malate dehydrogenase. Different clients may therefore depend on different parts of the cycle [gomez-llorente-2020-single-double-ring-fulltext].

Cryo-EM of the hyperstable SPG13 variant V72I captured client protein inside the chaperonin [braxton-2024-apical-domain-abstract]. Client density appeared in three distinct states. Clients contacted the inward-facing hydrophobic surfaces of the apical domains (helix I and the segment beneath it) and the disordered C-terminal tails that project into the base of the cavity [braxton-2024-apical-domain-fulltext]. The horse protein has these C-terminal Gly-Met-rich tails (Section 2). In the ATP state the apical domains alternated "up" and "down". The up domains provide a platform for Hsp10 to dock, while the down domains keep hold of the client, so the client is not released prematurely as the lid assembles. The client then becomes fully enclosed in the Hsp60–Hsp10 complex, with contacts at two discrete sites [braxton-2024-apical-domain-abstract]. A recent preprint adds apo, ATP-bound and ATP/Hsp10-bound cryo-EM structures. In these, ATP binding to the single-ring apo heptamer sets off coordinated changes in the intermediate and apical domains and flattens the equatorial surface, which allows the two rings to join [tascon-2025-double-ring-assembly-abstract]. This preprint has not been peer reviewed. Its emphasis on the intermediate domain as the relay between ATP binding and assembly is directly relevant to the horse F6Z587 model, which lacks part of that domain (Section 2).

## 5. Position in the mitochondrial import and folding pathway

Hsp60 acts at a defined step in the biogenesis of mitochondrial proteins. Most matrix proteins are encoded in the nucleus, made in the cytosol and imported through the outer- and inner-membrane translocases. In isolated yeast mitochondria, every imported precursor tested bound transiently to the matrix Hsp70 (mhsp70). Release from mhsp70 needed ATP but did not by itself produce a folded protein. Proteins such as the Mas2p subunit of the matrix processing peptidase, and the incoming Hsp60 subunits themselves, then passed in sequence to Hsp60 before folding and assembly [manning-krieg-1991-sequential-chaperones-abstract]. Not every client goes through this route. Imported mouse dihydrofolate reductase, a small soluble monomer, did not detectably associate with hsp60 under standard conditions [manning-krieg-1991-sequential-chaperones-abstract]. This fits the client survey (Section 6), which links Hsp60 to about half, not all, of the matrix proteome [bie-2020-interactors-abstract]. The chaperonin also builds itself. In the yeast hsp60 mutant mif4, newly imported wild-type subunits could not assemble on their own. Existing functional 14-mer was needed to assemble new subunits, and this happened with a half-time of 5–10 min, which points to a catalysed reaction [cheng-1990-own-assembly-abstract].

Mammalian work on medium-chain acyl-CoA dehydrogenase (MCAD), a flavoprotein of fatty-acid β-oxidation, gives the clearest example of the pathway for a single client. MCAD precursor imported into rat liver mitochondria first formed a transient complex with mitochondrial Hsp70. It then moved to a ~700-kDa Hsp60 complex and was released in an ATP-dependent step to form the mature tetramer [saijo-1994-mcad-folding-abstract]. The common disease variant K304E bound and transferred normally but stayed on Hsp60 much longer and assembled poorly. Hsp60 therefore acts at the step where folding-defective variants stall [saijo-1994-mcad-folding-abstract]. In intact human cells, shRNA knockdown of Hsp60 lowered both total and folded MCAD, for the wild-type and two disease variants, and had a similar effect on short-chain acyl-CoA dehydrogenase (SCAD). The knockdown acted specifically on proteins targeted to mitochondria [corydon-2005-mcad-rnai-abstract]. Hsp60 thus sits downstream of the import motor and matrix Hsp70 in the pathway that matures nuclear-encoded matrix proteins. The fatty-acid oxidation and respiratory-chain enzymes that make up much of its client load depend on it. Given the conserved sequence (Section 2), the same pathway is expected in horse mitochondria.

## 6. Subcellular localization and the client spectrum

The canonical site of action is the mitochondrial matrix. The protein is made in the cytosol as a precursor with a cleavable 26-residue N-terminal matrix-targeting signal, which is removed on import to give the mature subunit [gomez-llorente-2020-single-double-ring-fulltext]. UniProt assigns horse F6Z587 to the mitochondrial matrix and flags a transit peptide [uniprot-F6Z587-entry], and the horse N-terminus closely matches the human presequence (Section 2). The yeast experiments that defined Hsp60 function were performed specifically on proteins imported into the matrix [cheng-1989-hsp60-yeast-abstract][ostermann-1989-folding-mitochondria-abstract].

A proteome-wide interaction survey in human cells defines what the chaperonin folds. Crosslinking and HSP60 immunoprecipitation identified 323 interactors, mostly matrix-localized. They covered about half of all proteins annotated to the matrix, across mitochondrial protein synthesis, the respiratory chain, metabolism and protein quality control. Nineteen abundant matrix proteins took up more than 60% of chaperonin capacity [bie-2020-interactors-abstract]. Studies of Hsp60-deficient patient and model cells further point to individual dependent clients. These include the respiratory-chain complex III subunit UQCRC1, whose levels fell in Hsp60-deficient cells while its transcript did not, and manganese superoxide dismutase SOD2 [bross-2016-hspd1-mutations-fulltext].

Within the horse, the best tissue-level data come from the male reproductive tract, where the pattern fits a mitochondrial protein. In equine testis, HSP60 immunostaining was seen in spermatogonia and Leydig cells, both rich in mitochondria, but not in spermatocytes, spermatids or Sertoli cells. It was lowest in spermatogonia of heat-stressed cryptorchid testes [cinone-2024-cryptorchid-testis-abstract]. In mature stallion spermatozoa, as in boar, dog and cat, Hsp60 immunoreactivity was confined to the midpiece, where the mitochondrial sheath sits, and it did not change during capacitation or the acrosome reaction [volpe-2008-sperm-hsp-abstract]. A year-long study of equine semen found that HSP60, HSP70 and HSP90 levels tracked ambient temperature and humidity, peaking in summer and in the breeding season. They also correlated with sperm concentration and some motility measures, but not with mitochondrial membrane potential [albrizio-2020-equine-sperm-hsp-abstract]. A review of heat stress in stallion fertility brings these observations together [shakeel-2023-stallion-heat-stress-fulltext].

Hsp60 has also been reported outside mitochondria, and these reports should be read with care. In apoptotic human cell lines, Hsp60 co-purified with a caspase-3/caspase-6 activation complex and sped up the ATP-dependent maturation of pro-caspase-3 *in vitro*. That would be a foldase-like role in the cytosol [xanthoudakis-1999-procaspase3-abstract]. Cytosolic HSP60 builds up in many apoptotic settings, with or without detectable release from mitochondria. Depending on context it can promote either death or survival [chandra-2007-cytosolic-hsp60-abstract]. Recombinant human HSP60 was proposed as an endogenous ligand of Toll-like receptor 4 on macrophages [ohashi-2000-tlr4-abstract]. However, later analysis argued that the cytokine-inducing activity of such putative endogenous TLR ligands, heat shock proteins included, can be explained by contaminating microbial products such as lipopolysaccharide [tsan-2007-pamp-contamination-abstract]. That claim remains contested, and none of these extramitochondrial activities has been studied in the horse. Immune recognition of Hsp60 is, however, documented in horses. In spontaneous equine osteoarthritis, synovial-fluid and plasma antibodies recognized intracellular antigens of chondrocytes and synoviocytes. Proteomics of the immunoreactive 60-kDa band identified HSP60 together with vimentin and calreticulin, both known autoantigens in rheumatoid arthritis [linde-2025-equine-oa-abstract]. The authors classified HSP60 as a mitochondrial protein [linde-2025-equine-oa-fulltext]. An earlier study had found antibodies to the mycobacterial chaperonin homologue HSP65 raised only in synovial fluid from traumatised equine joints, and they tracked total IgG, so no pathogenic role could be inferred [carter-1995-equine-joint-antibodies-abstract]. This immune cross-recognition matches the observation, made when human P1 was first cloned, that its homology to the mycobacterial 65-kDa antigen might link it to autoimmunity [jindal-1989-human-p1-abstract]. Taken together, these observations describe tissue distribution and immune recognition. They do not establish a separate, non-mitochondrial molecular function in the horse.

## 7. Physiological and genetic evidence for the essential folding role

Genetic data from mammals show that the folding function is essential and dose-sensitive. In mice, homozygous inactivation of Hspd1 by gene-trap insertion caused death shortly after implantation (E6.5–7.5). Heterozygotes were viable and had reduced Hsp60, along with reduced Hsp10 in most tissues [christensen-2010-knockout-abstract]. In humans, the dominant missense variant V72I causes the pure hereditary spastic paraplegia SPG13. Wild-type HSP60 with HSP10 supported growth of *E. coli* lacking groES/groEL, but HSP60-V72I did not [hansen-2002-spg13-abstract]. A homozygous D29G variant causes an autosomal-recessive, early-onset, lethal hypomyelinating leukodystrophy, MitCHAP-60 disease. D29G-Hsp60 complemented *E. coli* poorly, especially at high temperature [magen-2008-mitchap60-abstract]. A recurrent de novo heterozygous variant, p.Leu47Val, located near the ATP-binding site, was found in a patient with hypomyelinating leukodystrophy. The variant protein was stable in patient fibroblasts but nonfunctional in the bacterial complementation assay [comert-2020-leukodystrophy-abstract][comert-2020-leukodystrophy-fulltext]. Reviews of these disorders conclude that different degrees of reduced chaperonin function give distinct neurological phenotypes, and that strongly deleterious or dominant-negative alleles are incompatible with life [bross-2016-hspd1-mutations-abstract]. V72I is described in mature-protein numbering and corresponds to p.Val98Ile in the precursor, whereas D29G (p.Asp29Gly) and p.Leu47Val use precursor numbering [bross-2016-hspd1-mutations-fulltext][comert-2020-leukodystrophy-fulltext]. Precursor residues Val98, Asp29 and Leu47 are all conserved in horse F6Z587 (alignment in NOTES-alignment-F6Z587-vs-P10809.txt). The same constraints very likely apply to the horse protein.

Expression of HSPD1 is controlled by mitochondrial protein-folding stress rather than by the general heat-shock response alone. In mammalian cells, unfolded protein accumulating in the matrix switched on nuclear genes for chaperonin 60, chaperonin 10, mtDnaJ and the ClpP protease, but not endoplasmic-reticulum stress proteins. This defined the mitochondrial unfolded protein response [zhao-2002-mitochondrial-stress-response-abstract]. A CHOP element in the shared chaperonin 60/10 bidirectional promoter was identified as the mitochondrial stress-response element, acting together with C/EBPβ [zhao-2002-mitochondrial-stress-response-abstract]. HSPD1 and HSPE1 therefore respond together to matrix proteotoxic stress, fitting their shared promoter [bross-2016-hspd1-mutations-fulltext].

The equine physiological data fit this picture. In Standardbred trotters, five weeks of α-lipoic acid supplementation raised resting HSP90 and post-exercise HSP70 in skeletal muscle but did not change HSP60 levels [kinnunen-2009-lipoic-acid-horse-abstract]. In horse testis, HSP60 responded differently from HSP70 and HSP90 to the raised temperature of cryptorchid gonads [cinone-2024-cryptorchid-testis-abstract], whereas in stallion semen all three chaperones varied with season and ambient temperature [albrizio-2020-equine-sperm-hsp-abstract]. These limited findings suggest that horse Hsp60 is present at substantial baseline levels in metabolically active tissues and is less acutely induced than the cytosolic HSP70 and HSP90 chaperones. That fits a housekeeping role in mitochondrial biogenesis controlled mainly by the mitochondrial unfolded protein response. The comparison is indirect, however, and comes from small studies.

## 8. Synthesis: what the horse HSPD1 gene product does

The horse HSPD1 gene very likely encodes the sole group I chaperonin of the mitochondrial matrix. Evidence for this comes from orthology, sequence conservation (about 97–98% identity with human), domain architecture and the conserved head-to-head arrangement with the Hsp10 gene. After import and removal of its presequence, the protein assembles into heptameric rings. With ATP and the heptameric Hsp10 lid, these rings form single-ring "half-football" and double-ring "football" complexes, which enclose newly imported or stress-denatured matrix proteins and release them folded after ATP hydrolysis [viitanen-1992-single-ring-abstract][levy-rimler-2001-nucleotides-abstract][gomez-llorente-2020-single-double-ring-abstract][braxton-2024-apical-domain-abstract]. Its biochemical "reaction" is ATP hydrolysis coupled to polypeptide folding (EC 5.6.1.7) [uniprot-F6Z587-entry]. Its "substrate specificity" is broad, covering roughly half the matrix proteome, with a strong bias toward abundant metabolic and respiratory-chain proteins and the mitochondrial translation apparatus [bie-2020-interactors-abstract]. It acts downstream of matrix Hsp70 in the maturation of imported proteins such as acyl-CoA dehydrogenases [manning-krieg-1991-sequential-chaperones-abstract][saijo-1994-mcad-folding-abstract][corydon-2005-mcad-rnai-abstract]. It is needed to assemble new chaperonin [cheng-1990-own-assembly-abstract]. With HSP10 it is induced by the mitochondrial unfolded protein response [zhao-2002-mitochondrial-stress-response-abstract]. It also takes part in mitochondrial protein quality control, and it is essential for development and for normal myelinating and motor neurons in mammals [christensen-2010-knockout-abstract][hansen-2002-spg13-abstract][magen-2008-mitchap60-abstract]. Horse-specific evidence is limited to detecting the protein in testis, the sperm midpiece, muscle and joint tissue, to seasonal variation in semen, and to its recognition as an autoantigen in osteoarthritis [cinone-2024-cryptorchid-testis-abstract][volpe-2008-sperm-hsp-abstract][albrizio-2020-equine-sperm-hsp-abstract][kinnunen-2009-lipoic-acid-horse-abstract][linde-2025-equine-oa-abstract]. One curation point stands out. The F6Z587 sequence itself lacks part of the intermediate domain. Annotations should therefore be attached to the gene, which also produces a full-length canonical transcript, and not taken as evidence that this particular 541-residue isoform is functional.

## Open Questions

Several gaps would be worth following up. The most immediate is the gene model. It is unclear whether the 11-exon transcript behind F6Z587 is a real, expressed splice isoform in horse tissues or an annotation artefact. Horse RNA-seq junction data, or targeted RT-PCR across the exon encoding human residues 171–202, would settle this. Proteomic peptide evidence specific to the exon-skipping junction would show whether the shorter protein is ever made. If it is, it would be informative to test whether it can assemble into rings or act as a dominant-negative subunit, since the intermediate domain is central to ATP-driven ring assembly [tascon-2025-double-ring-assembly-abstract]. The 14-residue N-terminal extension in the canonical Ensembl model should likewise be checked against transcript start sites. The unnamed gene head-to-head with HSPD1 on chromosome 18 should be confirmed as HSPE1, and the shared promoter characterized.

On the biological side, no horse study has measured chaperonin activity, oligomeric state or client binding directly. The equine expression data are sparse and rely on antibodies raised against other species. A systematic analysis of Hsp60 abundance in horse skeletal and cardiac muscle across training and heat stress would be valuable, given the exceptional mitochondrial capacity of equine athletes. So would analysis of how it relates to mitochondrial unfolded-protein-response markers. The finding of anti-HSP60 antibodies in equine osteoarthritis raises the question of how a matrix protein becomes exposed to the immune system in joint tissue. It is also unclear whether these antibodies recognize equine-specific or conserved epitopes, and whether they contribute to disease or simply mark tissue damage [linde-2025-equine-oa-abstract]. Neither the cytosolic pro- or anti-apoptotic activities nor the proposed TLR4 signalling of Hsp60 has been tested with equine protein. Any such study would need endotoxin-free preparations, given the contamination concerns [tsan-2007-pamp-contamination-abstract]. Finally, it is not known whether horses carry HSPD1 variants analogous to the human SPG13 or MitCHAP-60 alleles in breeds with neurological or myelin disorders. Equine genomic resources [wade-2009-horse-genome-abstract] could now be used to look for them.

## References

- [uniprot-F6Z587-entry] UniProt Consortium. UniProtKB/TrEMBL entry F6Z587_HORSE, "60 kDa heat shock protein, mitochondrial", gene HSPD1, *Equus caballus*; entry version 93 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/F6Z587.txt (local copy: citations/uniprot-F6Z587-entry.txt; human comparator P10809, https://rest.uniprot.org/uniprotkb/P10809.fasta).
- [NOTES-sequence-analysis.md] Sequence and gene-model analysis performed for this report using UniProt F6Z587, UniProt P10809 and Ensembl ENSECAG00000008968 / ENSECAP00000072491 (https://rest.ensembl.org/lookup/id/ENSECAG00000008968; https://rest.ensembl.org/sequence/id/ENSECAP00000072491).
- [albrizio-2020-equine-sperm-hsp] Albrizio M, Lacalandra GM, Volpe S, Nicassio M, Cinone M. Heat SHOCK proteins in equine spermatozoa: Expression and correlation to kinetic and environmental parameters. Theriogenology (2020) 155:185-196. PMID: 32711220; DOI: 10.1016/j.theriogenology.2020.05.042. https://pubmed.ncbi.nlm.nih.gov/32711220/
- [bie-2011-deficiency-model] Bie AS, et al. A cell model to study different degrees of Hsp60 deficiency in HEK293 cells. Cell Stress Chaperones (2011). PMID: 21717087; PMCID: PMC3220388; DOI: 10.1007/s12192-011-0275-5. https://pubmed.ncbi.nlm.nih.gov/21717087/
- [bie-2020-interactors] Bie AS, et al. An inventory of interactors of the human HSP60/HSP10 chaperonin in the mitochondrial matrix space. Cell Stress Chaperones (2020). PMID: 32060690; PMCID: PMC7192978; DOI: 10.1007/s12192-020-01080-6. https://pubmed.ncbi.nlm.nih.gov/32060690/
- [braxton-2024-apical-domain] Braxton JR, et al. Asymmetric apical domain states of mitochondrial Hsp60 coordinate substrate engagement and chaperonin assembly. Nat Struct Mol Biol (2024). PMID: 38951622; PMCID: PMC11638070; DOI: 10.1038/s41594-024-01352-0. https://pubmed.ncbi.nlm.nih.gov/38951622/
- [bross-2016-hspd1-mutations] Bross P, Fernandez-Guerra P. Disease-Associated Mutations in the HSPD1 Gene Encoding the Large Subunit of the Mitochondrial HSP60/HSP10 Chaperonin Complex. Front Mol Biosci (2016). PMID: 27630992; PMCID: PMC5006179; DOI: 10.3389/fmolb.2016.00049. https://pubmed.ncbi.nlm.nih.gov/27630992/
- [carter-1995-equine-joint-antibodies] Carter SD, Osborne AC, May SA, Bennett D. Rheumatoid factor, anti-heat shock protein (65 kDa) antibodies and anti-nuclear antibodies in equine joint diseases. Equine Vet J (1995). PMID: 8536665; DOI: 10.1111/j.2042-3306.1995.tb03079.x. https://pubmed.ncbi.nlm.nih.gov/8536665/
- [chandra-2007-cytosolic-hsp60] Chandra D, Choy G, Tang DG. Cytosolic accumulation of HSP60 during apoptosis with or without apparent mitochondrial release: evidence that its pro-apoptotic or pro-survival functions involve differential interactions with caspase-3. J Biol Chem (2007). PMID: 17823127; DOI: 10.1074/jbc.M702777200. https://pubmed.ncbi.nlm.nih.gov/17823127/
- [cheng-1989-hsp60-yeast] Cheng MY, et al. Mitochondrial heat-shock protein hsp60 is essential for assembly of proteins imported into yeast mitochondria. Nature (1989). PMID: 2645524; DOI: 10.1038/337620a0. https://pubmed.ncbi.nlm.nih.gov/2645524/
- [cheng-1990-own-assembly] Cheng MY, Hartl FU, Horwich AL. The mitochondrial chaperonin hsp60 is required for its own assembly. Nature (1990). PMID: 1978929; DOI: 10.1038/348455a0. https://pubmed.ncbi.nlm.nih.gov/1978929/
- [christensen-2010-knockout] Christensen JH, et al. Inactivation of the hereditary spastic paraplegia-associated Hspd1 gene encoding the Hsp60 chaperone results in early embryonic lethality in mice. Cell Stress Chaperones (2010). PMID: 20393889; PMCID: PMC3024079; DOI: 10.1007/s12192-010-0194-x. https://pubmed.ncbi.nlm.nih.gov/20393889/
- [cinone-2024-cryptorchid-testis] Cinone M, Albrizio M, Guaricci AC, Lacitignola L, Desantis S. Testicular expression of heat shock proteins 60, 70, and 90 in cryptorchid horses. Theriogenology (2024) 217:83-91. PMID: 38262223; DOI: 10.1016/j.theriogenology.2024.01.019. https://pubmed.ncbi.nlm.nih.gov/38262223/
- [comert-2020-leukodystrophy] Cömert C, et al. A recurrent de novo HSPD1 variant is associated with hypomyelinating leukodystrophy. Cold Spring Harb Mol Case Stud (2020). PMID: 32532876; PMCID: PMC7304351; DOI: 10.1101/mcs.a004879. https://pubmed.ncbi.nlm.nih.gov/32532876/
- [corydon-2005-mcad-rnai] Corydon TJ, Hansen J, Bross P, Jensen TG. Down-regulation of Hsp60 expression by RNAi impairs folding of medium-chain acyl-CoA dehydrogenase wild-type and disease-associated proteins. Mol Genet Metab (2005). PMID: 15927499; DOI: 10.1016/j.ymgme.2005.04.003. https://pubmed.ncbi.nlm.nih.gov/15927499/
- [gomez-llorente-2020-single-double-ring] Gomez-Llorente Y, et al. Structural basis for active single and double ring complexes in human mitochondrial Hsp60-Hsp10 chaperonin. Nat Commun (2020). PMID: 32317635; PMCID: PMC7174398; DOI: 10.1038/s41467-020-15698-8. https://pubmed.ncbi.nlm.nih.gov/32317635/
- [hansen-2002-spg13] Hansen JJ, et al. Hereditary spastic paraplegia SPG13 is associated with a mutation in the gene encoding the mitochondrial chaperonin Hsp60. Am J Hum Genet (2002). PMID: 11898127; PMCID: PMC447607; DOI: 10.1086/339935. https://pubmed.ncbi.nlm.nih.gov/11898127/
- [hartl-2011-chaperones] Hartl FU, Bracher A, Hayer-Hartl M. Molecular chaperones in protein folding and proteostasis. Nature (2011). PMID: 21776078; DOI: 10.1038/nature10317. https://pubmed.ncbi.nlm.nih.gov/21776078/
- [jindal-1989-human-p1] Jindal S, et al. Primary structure of a human mitochondrial protein homologous to the bacterial and plant chaperonins and to the 65-kilodalton mycobacterial antigen. Mol Cell Biol (1989). PMID: 2568584; PMCID: PMC363030; DOI: 10.1128/mcb.9.5.2279-2283.1989. https://pubmed.ncbi.nlm.nih.gov/2568584/
- [kinnunen-2009-lipoic-acid-horse] Kinnunen S, et al. alpha-Lipoic acid supplementation enhances heat shock protein production and decreases post exercise lactic acid concentrations in exercised standardbred trotters. Res Vet Sci (2009). PMID: 19427659; DOI: 10.1016/j.rvsc.2009.04.009. https://pubmed.ncbi.nlm.nih.gov/19427659/
- [levy-rimler-2001-nucleotides] Levy-Rimler G, et al. The effect of nucleotides and mitochondrial chaperonin 10 on the structure and chaperone activity of mitochondrial chaperonin 60. Eur J Biochem (2001). PMID: 11422376; DOI: 10.1046/j.1432-1327.2001.02243.x. https://pubmed.ncbi.nlm.nih.gov/11422376/
- [levy-rimler-2002-type1] Levy-Rimler G, et al. Type I chaperonins: not all are created equal. FEBS Lett (2002). PMID: 12354603; DOI: 10.1016/s0014-5793(02)03178-2. https://pubmed.ncbi.nlm.nih.gov/12354603/
- [linde-2025-equine-oa] Linde P, et al. Identification of Antibodies to Chondrocyte and Synoviocyte Antigens in Equine Osteoarthritis. J Orthop Res (2025). PMID: 41117710; PMCID: PMC12604456; DOI: 10.1002/jor.70085. https://pubmed.ncbi.nlm.nih.gov/41117710/
- [magen-2008-mitchap60] Magen D, et al. Mitochondrial hsp60 chaperonopathy causes an autosomal-recessive neurodegenerative disorder linked to brain hypomyelination and leukodystrophy. Am J Hum Genet (2008). PMID: 18571143; PMCID: PMC2443844; DOI: 10.1016/j.ajhg.2008.05.016. https://pubmed.ncbi.nlm.nih.gov/18571143/
- [manning-krieg-1991-sequential-chaperones] Manning-Krieg UC, Scherer PE, Schatz G. Sequential action of mitochondrial chaperones in protein import into the matrix. EMBO J (1991). PMID: 1915294; PMCID: PMC453052; DOI: 10.1002/j.1460-2075.1991.tb04891.x. https://pubmed.ncbi.nlm.nih.gov/1915294/
- [nielsen-1998-single-ring] Nielsen KL, Cowan NJ. A single ring is sufficient for productive chaperonin-mediated folding in vivo. Mol Cell (1998). PMID: 9702195; DOI: 10.1016/s1097-2765(00)80117-3. https://pubmed.ncbi.nlm.nih.gov/9702195/
- [nielsen-1999-single-ring-substitute] Nielsen KL, et al. A single-ring mitochondrial chaperonin (Hsp60-Hsp10) can substitute for GroEL-GroES in vivo. J Bacteriol (1999). PMID: 10482535; PMCID: PMC94114; DOI: 10.1128/JB.181.18.5871-5875.1999. https://pubmed.ncbi.nlm.nih.gov/10482535/
- [nisemblat-2015-football] Nisemblat S, et al. Crystal structure of the human mitochondrial chaperonin symmetrical football complex. Proc Natl Acad Sci U S A (2015). PMID: 25918392; PMCID: PMC4434751; DOI: 10.1073/pnas.1411718112. https://pubmed.ncbi.nlm.nih.gov/25918392/
- [ohashi-2000-tlr4] Ohashi K, Burkart V, Flohé S, Kolb H. Cutting edge: heat shock protein 60 is a putative endogenous ligand of the toll-like receptor-4 complex. J Immunol (2000). PMID: 10623794; DOI: 10.4049/jimmunol.164.2.558. https://pubmed.ncbi.nlm.nih.gov/10623794/
- [ostermann-1989-folding-mitochondria] Ostermann J, et al. Protein folding in mitochondria requires complex formation with hsp60 and ATP hydrolysis. Nature (1989). PMID: 2528694; DOI: 10.1038/341125a0. https://pubmed.ncbi.nlm.nih.gov/2528694/
- [parnas-2012-cochaperonin-specificity] Parnas A, et al. Identification of elements that dictate the specificity of mitochondrial Hsp60 for its co-chaperonin. PLoS One (2012). PMID: 23226518; PMCID: PMC3514286; DOI: 10.1371/journal.pone.0050318. https://pubmed.ncbi.nlm.nih.gov/23226518/
- [saijo-1994-mcad-folding] Saijo T, Welch WJ, Tanaka K. Intramitochondrial folding and assembly of medium-chain acyl-CoA dehydrogenase (MCAD). Demonstration of impaired transfer of K304E-variant MCAD from its complex with hsp60 to the native tetramer. J Biol Chem (1994). PMID: 7905878. https://pubmed.ncbi.nlm.nih.gov/7905878/
- [shakeel-2023-stallion-heat-stress] Shakeel M, Yoon M. Heat stress and stallion fertility. J Anim Sci Technol (2023). PMID: 37970501; PMCID: PMC10640949; DOI: 10.5187/jast.2023.e29. https://pubmed.ncbi.nlm.nih.gov/37970501/
- [tascon-2025-double-ring-assembly] Tascón I, et al. Structural basis for ATP-driven double-ring assembly of the human mitochondrial Hsp60 chaperonin. bioRxiv preprint (2025). PMID: 41256524; PMCID: PMC12621666; DOI: 10.1101/2025.10.04.680452. https://pubmed.ncbi.nlm.nih.gov/41256524/
- [tsan-2007-pamp-contamination] Tsan MF, Gao B. Pathogen-associated molecular pattern contamination as putative endogenous ligands of Toll-like receptors. J Endotoxin Res (2007). PMID: 17621541; DOI: 10.1177/0968051907078604. https://pubmed.ncbi.nlm.nih.gov/17621541/
- [viitanen-1992-single-ring] Viitanen PV, et al. Mammalian mitochondrial chaperonin 60 functions as a single toroidal ring. J Biol Chem (1992). PMID: 1346131. https://pubmed.ncbi.nlm.nih.gov/1346131/
- [volpe-2008-sperm-hsp] Volpe S, Galeati G, Bernardini C, Tamanini C, Mari G, Zambelli D, Seren E, Spinaci M. Comparative immunolocalization of heat shock proteins (Hsp)-60, -70, -90 in boar, stallion, dog and cat spermatozoa. Reprod Domest Anim (2008). PMID: 18226022; DOI: 10.1111/j.1439-0531.2007.00918.x. https://pubmed.ncbi.nlm.nih.gov/18226022/
- [wade-2009-horse-genome] Wade CM, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. Science (2009) 326:865-867. PMID: 19892987; DOI: 10.1126/science.1178158. https://pubmed.ncbi.nlm.nih.gov/19892987/
- [xanthoudakis-1999-procaspase3] Xanthoudakis S, Roy S, Rasper D, Hennessey T, Aubin Y, Cassady R, Tawa P, Ruel R, Rosen A, Nicholson DW. Hsp60 accelerates the maturation of pro-caspase-3 by upstream activator proteases during apoptosis. EMBO J (1999). PMID: 10205159; DOI: 10.1093/emboj/18.8.2049. https://pubmed.ncbi.nlm.nih.gov/10205159/
- [zhao-2002-mitochondrial-stress-response] Zhao Q, Wang J, Levichkin IV, Stasinopoulos S, Ryan MT, Hoogenraad NJ. A mitochondrial specific stress response in mammalian cells. EMBO J (2002). PMID: 12198143; PMCID: PMC126185; DOI: 10.1093/emboj/cdf445. https://pubmed.ncbi.nlm.nih.gov/12198143/


## Citations

1. albrizio-2020-equine-sperm-hsp-abstract.md
2. albrizio-2020-equine-sperm-hsp-summary.md
3. bie-2011-deficiency-model-abstract.md
4. bie-2011-deficiency-model-summary.md
5. bie-2020-interactors-abstract.md
6. bie-2020-interactors-summary.md
7. braxton-2024-apical-domain-abstract.md
8. braxton-2024-apical-domain-fulltext.txt
9. braxton-2024-apical-domain-summary.md
10. bross-2016-hspd1-mutations-abstract.md
11. bross-2016-hspd1-mutations-fulltext.txt
12. bross-2016-hspd1-mutations-summary.md
13. carter-1995-equine-joint-antibodies-abstract.md
14. carter-1995-equine-joint-antibodies-summary.md
15. chandra-2007-cytosolic-hsp60-abstract.md
16. chandra-2007-cytosolic-hsp60-summary.md
17. cheng-1989-hsp60-yeast-abstract.md
18. cheng-1989-hsp60-yeast-summary.md
19. cheng-1990-own-assembly-abstract.md
20. cheng-1990-own-assembly-summary.md
21. christensen-2010-knockout-abstract.md
22. christensen-2010-knockout-summary.md
23. cinone-2024-cryptorchid-testis-abstract.md
24. cinone-2024-cryptorchid-testis-summary.md
25. comert-2020-leukodystrophy-abstract.md
26. comert-2020-leukodystrophy-fulltext.txt
27. comert-2020-leukodystrophy-summary.md
28. corydon-2005-mcad-rnai-abstract.md
29. corydon-2005-mcad-rnai-summary.md
30. ensembl-ENSECAG00000008968-lookup.json
31. ensembl-ENSECAP00000072491-protein.fasta
32. ensembl-horse-chr18-HSPD1-neighborhood.json
33. gomez-llorente-2020-single-double-ring-abstract.md
34. gomez-llorente-2020-single-double-ring-fulltext.txt
35. gomez-llorente-2020-single-double-ring-summary.md
36. hansen-2002-spg13-abstract.md
37. hansen-2002-spg13-summary.md
38. hartl-2011-chaperones-abstract.md
39. hartl-2011-chaperones-summary.md
40. jindal-1989-human-p1-abstract.md
41. jindal-1989-human-p1-summary.md
42. kinnunen-2009-lipoic-acid-horse-abstract.md
43. kinnunen-2009-lipoic-acid-horse-summary.md
44. levy-rimler-2001-nucleotides-abstract.md
45. levy-rimler-2001-nucleotides-summary.md
46. levy-rimler-2002-type1-abstract.md
47. levy-rimler-2002-type1-summary.md
48. linde-2025-equine-oa-abstract.md
49. linde-2025-equine-oa-fulltext.txt
50. linde-2025-equine-oa-summary.md
51. magen-2008-mitchap60-abstract.md
52. magen-2008-mitchap60-summary.md
53. manning-krieg-1991-sequential-chaperones-abstract.md
54. manning-krieg-1991-sequential-chaperones-summary.md
55. nielsen-1998-single-ring-abstract.md
56. nielsen-1998-single-ring-summary.md
57. nielsen-1999-single-ring-substitute-abstract.md
58. nielsen-1999-single-ring-substitute-summary.md
59. nisemblat-2015-football-abstract.md
60. nisemblat-2015-football-summary.md
61. ohashi-2000-tlr4-abstract.md
62. ohashi-2000-tlr4-summary.md
63. ostermann-1989-folding-mitochondria-abstract.md
64. ostermann-1989-folding-mitochondria-summary.md
65. parnas-2012-cochaperonin-specificity-abstract.md
66. parnas-2012-cochaperonin-specificity-fulltext.txt
67. parnas-2012-cochaperonin-specificity-summary.md
68. saijo-1994-mcad-folding-abstract.md
69. saijo-1994-mcad-folding-summary.md
70. shakeel-2023-stallion-heat-stress-abstract.md
71. shakeel-2023-stallion-heat-stress-fulltext.txt
72. shakeel-2023-stallion-heat-stress-summary.md
73. tascon-2025-double-ring-assembly-abstract.md
74. tascon-2025-double-ring-assembly-summary.md
75. tsan-2007-pamp-contamination-abstract.md
76. tsan-2007-pamp-contamination-summary.md
77. uniprot-F6Z587-entry.txt
78. uniprot-F6Z587-summary.md
79. uniprot-F6Z587.fasta
80. uniprot-P10809-human.fasta
81. viitanen-1992-single-ring-abstract.md
82. viitanen-1992-single-ring-summary.md
83. volpe-2008-sperm-hsp-abstract.md
84. volpe-2008-sperm-hsp-summary.md
85. wade-2009-horse-genome-abstract.md
86. wade-2009-horse-genome-summary.md
87. xanthoudakis-1999-procaspase3-abstract.md
88. xanthoudakis-1999-procaspase3-summary.md
89. zhao-2002-mitochondrial-stress-response-abstract.md
90. zhao-2002-mitochondrial-stress-response-summary.md