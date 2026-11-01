---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:21:33.876651'
end_time: '2026-10-26T01:28:26.341348'
duration_seconds: 412.46
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: USP36
  gene_symbol: USP36
  uniprot_accession: A0A9L0JCH5
  protein_description: 'RecName: Full=Ubiquitin carboxyl-terminal hydrolase {ECO:0000256|PROSITE-ProRule:PRU10092};
    EC=3.4.19.12 {ECO:0000256|PROSITE-ProRule:PRU10092};'
  gene_info: Name=USP36 {ECO:0000313|Ensembl:ENSEASP00005051006.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the peptidase C19 family. {ECO:0000256|PROSITE-
  protein_domains: Papain-like_cys_pep_sf. (IPR038765); Peptidase_C19. (IPR050164);
    Peptidase_C19_UCH. (IPR001394); USP. (IPR028889); USP_CS. (IPR018200)
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
citation_count: 84
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0JCH5
- **Protein Description:** RecName: Full=Ubiquitin carboxyl-terminal hydrolase {ECO:0000256|PROSITE-ProRule:PRU10092}; EC=3.4.19.12 {ECO:0000256|PROSITE-ProRule:PRU10092};
- **Gene Information:** Name=USP36 {ECO:0000313|Ensembl:ENSEASP00005051006.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the peptidase C19 family. {ECO:0000256|PROSITE-
- **Key Domains:** Papain-like_cys_pep_sf. (IPR038765); Peptidase_C19. (IPR050164); Peptidase_C19_UCH. (IPR001394); USP. (IPR028889); USP_CS. (IPR018200)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "USP36" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'USP36' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **USP36** (gene ID: USP36, UniProt: A0A9L0JCH5) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# USP36 (Ubiquitin carboxyl-terminal hydrolase 36) in the donkey, *Equus asinus* (UniProt A0A9L0JCH5)

## 1. Introduction and summary

A0A9L0JCH5 is an unreviewed (TrEMBL) entry for donkey USP36. It is a 1,156-residue protein predicted from the chromosome-level genome assembly of a Dezhou donkey [wang-2020-donkey-genomes-abstract], and its Ensembl gene model (ENSEASG00005005026) maps to donkey chromosome 13 (UniProt record, `uniprot_A0A9L0JCH5.txt`). Its annotation as a "ubiquitin carboxyl-terminal hydrolase" (EC 3.4.19.12) of the peptidase C19 family rests entirely on automatic PROSITE and InterPro rules, which detect a USP catalytic domain at residues 122–456. No experimental study of USP36 in the donkey, the horse or any other equid could be found: a PubMed search for USP36 combined with horse, equine, donkey or *Equus* returned no records. Everything said below about function is therefore an inference from orthologs, chiefly human USP36 (Q9P275), mouse Usp36, *Drosophila* dUSP36/Scrawny and the yeast homolog Ubp10.

That inference is strong. The gene symbol is not ambiguous: USP36 names a single, well-defined deubiquitinase family member in vertebrates. My own global alignment found the donkey protein 78% identical to human USP36 over its full length and 96% identical within the catalytic USP domain (`SEQUENCE_NOTES.md`). The catalytic nucleophile (Cys131), the proton-acceptor histidine (human His382, donkey His415) and the triad asparagine are all conserved, as is the C-terminal basic nucleolar localization signal. Human USP36 can functionally replace yeast Ubp10 [richardson-2012-rna-pol-i-abstract], which supports deep conservation of the core function.

In summary, the orthologs show that USP36 is a nucleolar cysteine protease of the USP class. It removes ubiquitin from nucleolar substrates and so protects them from proteasomal degradation. Substrates include nucleophosmin/B23 and fibrillarin [endo-2009-nucleolar-structure-abstract], the RNA polymerase I large subunit [richardson-2012-rna-pol-i-abstract], the DHX33 helicase [fraile-2018-dhx33-lethality-abstract] and c-Myc [sun-2015-usp36-cmyc-abstract]. USP36 also removes the ubiquitin-like protein FUBI from the FUBI–eS30 ribosomal fusion protein, a step needed for 40S subunit maturation [vandenheuvel-2021-fubi-processing-abstract; odea-2023-fubi-crossreactivity-abstract]. Unusually for a deubiquitinase, it also promotes SUMOylation of several nucleolar RNA-processing factors, acting in a SUMO E3-ligase-like way [ryu-2021-snorna-sumoylation-abstract; chen-2023-exosc10-sumoylation-abstract]. Through these activities USP36 sustains rRNA transcription and processing, ribosome production and cell growth. It is essential for preimplantation development in mice [fraile-2018-dhx33-lethality-abstract]. A conserved secondary role in chromatin, removing monoubiquitin from histone H2B, has been shown in flies and human cells [buszczak-2009-scrawny-h2b-abstract; devine-2018-h2b-deubiquitinase-abstract].

## 2. Identity, domain architecture and evolutionary conservation

USP36 belongs to the ubiquitin-specific protease (USP) family, clan CA peptidase C19. It was first cloned in humans as one of 22 new USPs. That study showed broad tissue expression and found deubiquitylating activity against a ubiquitin–β-galactosidase fusion for many family members [quesada-2004-cloning-usps-abstract]. An independent cloning from ovarian cancer cells confirmed that USP36 cleaves ubiquitin, and showed that it carries a PEST motif and is itself polyubiquitinated [kim-2005-usp36-pest-abstract].

The donkey protein has the canonical USP36 layout: a short N-terminal region, the papain-like USP catalytic domain, and a long, mostly disordered central and C-terminal extension (MobiDB-lite predicts residues 463–1048 as disordered) ending in a lysine/arginine-rich tail (UniProt record; `SEQUENCE_NOTES.md`). In yeast Ubp10 and human USP36, intrinsically disordered regions flank the catalytic domain and carry separate binding modules that recruit partners for gene silencing and ribosome biogenesis [reed-2015-disordered-regions-ubp10-abstract]. In human USP36, the C-terminal region (residues 801–1121) binds EXOSC10 [chen-2023-exosc10-sumoylation-fulltext], Las1L and Nol9 [li-2024-las1l-sumoylation-fulltext]. A proteome-wide comparison of 30 DUBs in *Xenopus* egg extracts placed USP36 among five "high-impact" enzymes with broad, overlapping substrate ranges, and the candidate substrates of these enzymes were enriched for disordered regions [rossio-2024-dub-specificity-abstract].

Ortholog relationships are well supported. Human USP36 rescues RNA polymerase I stability, pre-rRNA processing and growth in *ubp10Δ* yeast [richardson-2012-rna-pol-i-abstract]. The *Drosophila* gene *scrawny* (also called dUsp36) shares the H2B-deubiquitinating activity of Ubp10 [buszczak-2009-scrawny-h2b-abstract]. In *C. elegans*, USP-33 is the fibrillarin-stabilizing deubiquitinase, and parallel experiments link it functionally to human USP36 [chen-2020-p53-caspase-usp36-abstract]. One unusual feature of the donkey model is a 33-residue segment inside the USP domain (after residue ~252) that is absent from human USP36. It accounts for the longer annotated domain (122–456 versus 122–423 in human). The segment lies between catalytic-box regions, away from the conserved Cys and His residues. Comparing the other UniProt models of the same locus helps here. A second donkey entry, A0A9L0I9H9 (1,123 residues), matches A0A9L0JCH5 exactly at every aligned position and lacks only this segment. A third, A0A8C4LEG8, likewise lacks it. The horse USP36 model F6W2H6 (Ensembl ENSECAG00000016116) is the same length as human USP36, about 98.7% identical to the donkey protein, and also lacks the segment (`SEQUENCE_NOTES.md`). A0A9L0JCH5 is therefore best seen as an alternatively spliced or over-predicted transcript model of a normal-length equid USP36, not a sign that the donkey protein has a divergent catalytic domain. No transcript evidence has been checked to tell which of these explanations is correct (see Open Questions).

## 3. Catalytic activity and substrate specificity

The reaction assigned to A0A9L0JCH5 is the thiol-dependent hydrolysis of the isopeptide (or peptide) bond after the C-terminal Gly76 of ubiquitin (EC 3.4.19.12). For human USP36 this activity is supported experimentally: purified or overexpressed enzyme deubiquitinates its substrates, and a catalytically inactive C131A mutant does not [li-2024-las1l-sumoylation-fulltext; chen-2023-exosc10-sumoylation-fulltext]. The enzyme does not appear to be restricted to one chain type. It reverses K48-linked chains, which mark proteins for proteasomal degradation, on substrates such as CEP63 [ling-2022-cep63-abstract]. It removes K29-linked chains from the DNA-damage-tolerance primase-polymerase PrimPol [yan-2020-primpol-abstract]. It also removes single ubiquitins, for example the monoubiquitin on histone H2B [devine-2018-h2b-deubiquitinase-abstract]. The *Xenopus* profiling data likewise point to a promiscuous enzyme whose specificity comes more from location and binding partners than from linkage type [rossio-2024-dub-specificity-abstract].

The best-defined specificity feature of USP36 is that it cleaves both ubiquitin and FUBI. FUBI is a ubiquitin-like protein made as an N-terminal fusion to ribosomal protein eS30 (encoded by *FAU*). Van den Heuvel and colleagues showed that non-cleavable FUBI–eS30 mutants disrupt late cytoplasmic steps of 40S maturation. Affinity purification identified USP36 as the processing enzyme: depleting it impaired FUBI–eS30 cleavage, and purified USP36 cut the fusion *in vitro* [vandenheuvel-2021-fubi-processing-abstract]. O'Dea and colleagues then solved crystal structures of the USP36 catalytic domain bound covalently to FUBI-propargylamide (PDB 8BS3) and to ubiquitin-propargylamide (PDB 8BS9). The structures show that a flexible blocking loop and an arginine–tyrosine motif on helix α5, shared only with USP16, accommodate FUBI's distinctive hydrophobic surface. This explains why other USPs cannot process FUBI [odea-2023-fubi-crossreactivity-abstract; odea-2023-fubi-crossreactivity-fulltext]. Because the donkey USP domain is 96% identical to the human one, it very likely shares this dual specificity.

## 4. Subcellular localization: a nucleolar enzyme with minor extranucleolar pools

Human USP36 is concentrated in the nucleolus. Nucleolar targeting depends on its C-terminal region, which contains basic amino-acid stretches. A dominant-negative USP36 causes ubiquitin conjugates to build up in nucleoli, which marks the nucleolus as the main site of USP36 activity [endo-2009-nucleolar-structure-abstract]. The nucleolar localization signal was mapped to RGKEKKIKKFKREKRR. This motif binds the central acidic region of nucleophosmin/B23, and depleting NPM1 releases USP36 from nucleoli, so NPM1 serves as the nucleolar anchoring platform [endo-2009-nucleophosmin-usp36-abstract]. The donkey sequence has the equivalent basic motif (RGKEKKVKKLKREKKR) at the same C-terminal position (`SEQUENCE_NOTES.md`), so nucleolar localization is a confident prediction. The automatic GO terms on the donkey entry (nucleolus, nuclear speck, cytosol; all IEA) agree with this.

Smaller pools outside the nucleolus have also been reported. USP36 binds the cytoplasmic E3 ligase NEDD4L (Nedd4-2) and changes how it acts on the TrkA neurotrophin receptor and on Kv7.2/3 potassium channels [anta-2016-usp36-nedd4l-abstract]. USP36 also stabilizes the mitochondrial antioxidant enzyme SOD2 [kim-2011-sod2-usp36-abstract]. *Drosophila* dUsp36 makes alternative isoforms: dUSP36-B carries a nuclear export signal and is cytoplasmic, dUSP36-C and -D are nuclear, and endogenous dUSP36-D is nucleolar. Only the nucleolar D isoform is needed for cell and organismal growth [thevenon-2020-nucleolar-isoform-dusp36-fulltext]. Whether mammals, and equids in particular, make comparable non-nucleolar isoforms is unknown. The consistent picture is that the essential growth-related functions are carried out in the nucleolus.

## 5. Role in ribosome biogenesis: deubiquitination of the rRNA-production machinery

The central physiological role of USP36 is to support ribosome biogenesis. In human cells, USP36 deubiquitinates and stabilizes nucleophosmin/B23 and the box C/D methyltransferase fibrillarin. Its depletion lowers rRNA transcription and processing, leaves nucleoli less developed, slightly reduces cytoplasmic ribosome levels and slows proliferation [endo-2009-nucleolar-structure-abstract]. Yeast Ubp10 is nucleolar and deubiquitinates the largest subunit of RNA polymerase I (Rpa190), keeping enough polymerase available for rRNA synthesis. Human USP36 can do the same job in yeast, which suggests that controlling RNA polymerase I stability is an ancient function of this lineage [richardson-2012-rna-pol-i-abstract].

Mouse genetics confirm that the function is essential. *Usp36*-null embryos arrest at the morula-to-blastocyst transition. USP36 lowers ubiquitination of the DEAH-box helicase DHX33 and increases its stability; DHX33 is needed for rRNA synthesis and mRNA translation. Loss of USP36 reduces rRNA and protein synthesis, as shown by Northern blotting, O-propargyl-puromycin labelling and electron microscopy [fraile-2018-dhx33-lethality-abstract]. USP36 also stabilizes the Las1L–Nol9 endonuclease–kinase complex through deubiquitination; this complex cleaves internal transcribed spacer 2 (ITS2) during 60S maturation [li-2024-las1l-sumoylation-abstract]. Under ribotoxic stress, JNK signalling activates USP36, which stabilizes nucleolar Snail1. Snail1 in turn supports ribosome biogenesis and cell survival, a pathway that makes solid tumours resistant to the translation inhibitor homoharringtonine [qin-2023-snail1-nucleolar-abstract].

USP36 also targets c-Myc, the main transcriptional driver of ribosome biogenesis. In the nucleolus, USP36 binds and deubiquitinates c-Myc in cells and *in vitro*, preventing its degradation. It interacts with the nucleolar Fbw7γ isoform but not the nucleoplasmic Fbw7α. *USP36* is itself a c-Myc target gene, so the two form a positive feedback loop [sun-2015-usp36-cmyc-abstract; sun-2015-deubiquitinating-cmyc-commentary-abstract]. The same three-way relationship of USP36, MYC and Fbw7 (called AGO in flies) is conserved in *Drosophila*. There, nucleolar dUSP36-D binds dMYC and AGO, controls their ubiquitination and stability, and removes ubiquitin from itself [thevenon-2020-nucleolar-isoform-dusp36-abstract]. USP36 thus works at two levels: it stabilizes the transcription factor that switches on ribosome-biogenesis genes, and it stabilizes the nucleolar machinery that carries out the work.

## 6. A SUMO-ligase-like activity in nucleolar RNA processing

Since 2021 a second enzymatic activity has been described. Ryu and colleagues found that USP36 binds SUMO2 and the SUMO E2 enzyme Ubc9, increases SUMOylation in the nucleolus, and directly SUMOylates the snoRNP components Nop58 and Nhp2 (as well as Nop56 and DKC1) in cells and *in vitro*. This SUMOylation helps these proteins bind snoRNAs, and loss of USP36 impairs rRNA processing and translation [ryu-2021-snorna-sumoylation-abstract]. Later work extended the list of SUMO targets. USP36 binds the C-terminal Lasso domain of the exosome nuclease EXOSC10 through its own C-terminal region and SUMOylates EXOSC10 at K583. This modification is needed for EXOSC10 to bind pre-rRNA and to process rRNA, but USP36 does not change EXOSC10 protein levels [chen-2023-exosc10-sumoylation-abstract; chen-2023-exosc10-sumoylation-fulltext]. USP36 SUMOylates Las1L at K565, which is required for ITS2 cleavage [li-2024-las1l-sumoylation-abstract]. It also SUMOylates DGCR8 with SUMO2, which promotes pri-miRNA binding and miRNA biogenesis [li-2023-microprocessor-sumoylation-abstract]. A 2025 preprint identifies the nucleolar GTPase GNL3 as a further USP36 SUMO target needed for DNA end resection in homologous recombination [yang-2025-gnl3-sumoylation-abstract].

These studies support a model in which USP36 controls nucleolar RNA processing by "group SUMOylation" as well as by stabilizing proteins [yang-2024-review-sumoylation-abstract; shao-2025-review-ribosome-biogenesis-abstract]. The mechanism is still unclear. No mutation has yet been found that removes the SUMO-ligase activity while leaving deubiquitinase activity intact [yang-2024-review-sumoylation-fulltext]. Genetic evidence from flies shows that part of USP36's function does not need catalysis. *dUsp36*-null flies die as larvae with severe growth defects. Flies carrying an endogenous catalytically dead C181S allele survive to adulthood with only minor growth defects, although the males are infertile [coirry-2025-drosophila-catalytic-abstract; coirry-2025-drosophila-catalytic-fulltext]. This suggests that the growth-supporting functions of USP36 depend partly on scaffolding or non-catalytic activity, with deubiquitinase activity required for specific processes such as spermatogenesis.

## 7. Chromatin, stress and quality-control functions

The yeast homolog Ubp10 deubiquitinates histone H2B in silent chromatin, and this function is conserved. *Drosophila* Scrawny deubiquitinates H2B and is needed in germline, epithelial and intestinal stem cells. Mutant cells have raised H2Bub1 and H3K4me3 and switch on differentiation genes, including Notch targets, too early [buszczak-2009-scrawny-h2b-abstract]. Human USP36 binds H2B and deubiquitinates H2Bub1 *in vitro* and in cells. Depleting it raises H2Bub1 across the gene body of *CDKN1A* (p21), induces p21 and slows proliferation [devine-2018-h2b-deubiquitinase-abstract]. USP36 may therefore act as a transcriptional repressor at selected loci through the H2B ubiquitination–H3K4 methylation crosstalk pathway.

Several other roles have been reported, mostly from single studies in cancer cell lines. In flies and human cells, loss of USP36 activates p62/SQSTM1-dependent selective autophagy independently of TOR, together with build-up of ubiquitinated nuclear and cytoplasmic proteins [taillebourg-2012-selective-autophagy-abstract]. USP36 knockdown impairs Parkin-dependent mitophagy, apparently by lowering Beclin-1/ATG14L expression and H2B K120 monoubiquitination, while USP36 itself stays nucleolar [geisler-2019-mitophagy-abstract]. During replication stress, USP36 is itself deubiquitinated and in turn stabilizes PrimPol [yan-2020-primpol-abstract]. In *C. elegans* and human cells, a non-apoptotic p53–caspase pathway cleaves the fibrillarin-stabilizing DUB (USP-33 in worms, USP36 in humans), which shrinks nucleoli and increases resistance to bacterial infection. This links USP36 to nucleolar control of innate immunity [chen-2020-p53-caspase-usp36-abstract]. Further substrates and pathways in tumours are listed in recent reviews [niu-2024-review-cancer-abstract; shao-2025-review-ribosome-biogenesis-abstract]. These are best seen as extensions of a broadly acting nucleolar and nuclear DUB rather than as defining functions.

## 8. Implications for annotating donkey USP36

For functional annotation of A0A9L0JCH5, the strongest inference is as follows. The molecular function is a cysteine-type deubiquitinase (ubiquitin-specific protease; EC 3.4.19.12) able to cleave both ubiquitin and FUBI. The protein is located mainly in the nucleolus, anchored by NPM1 through a conserved C-terminal basic signal. The core processes are ribosome biogenesis (rRNA transcription and pre-rRNA processing, including ITS2 processing and FUBI–eS30 maturation for the 40S subunit), stabilization of nucleolar proteins and c-Myc, and nucleolar SUMOylation of snoRNP and exosome components. Histone H2B deubiquitination and transcriptional repression are a well-supported secondary role. All of this rests on human, mouse, fly and yeast data together with the very high sequence conservation and the conserved catalytic and targeting residues described above. None of it has been tested directly in equids. Peripheral reported roles (SOD2, NEDD4L, autophagy, PrimPol and others) should be treated with caution, as each comes from limited studies.

## Open Questions

There are no experimental data on equid USP36, so the first question is whether the donkey gene model is correct. The 33-residue insertion inside the USP domain is absent from human USP36, from the horse model and from the other donkey models of the same locus, which otherwise match A0A9L0JCH5 exactly. It could be checked against horse (*Equus caballus*) gene models, donkey RNA-seq or Iso-Seq data, and AlphaFold models to see whether it is a real exon and whether it changes the catalytic fold. It would also help to know whether equids express alternative USP36 isoforms with different localizations, as *Drosophila* does. At the mechanistic level, the main open problem is how USP36 promotes SUMOylation: whether it is a true SUMO E3 ligase and which surfaces are involved. This is important because the fly C181S allele shows that much of USP36's growth-supporting function does not need deubiquitinase activity. A separation-of-function mutant and a structure of full-length USP36 bound to a SUMO substrate, Ubc9 and RNA would settle this. Other unresolved points are the relative importance of ubiquitin versus FUBI processing *in vivo*, how USP36 and USP16 divide FUBI–eS30 maturation between nucleolus and cytoplasm, whether the many cancer-cell substrates are direct and physiological, and whether USP36 activity responds to nutrient or stress signals (JNK, ribotoxic stress, replication stress) in the same way across mammals. For equid biology, follow-up could include checking USP36 expression in donkey tissue transcriptome atlases and looking for USP36 variants in donkey population genomic data [wang-2020-donkey-genomes-abstract], keeping in mind that loss of function is expected to be lethal in early embryos [fraile-2018-dhx33-lethality-abstract].

## References

- **anta-2016-usp36-nedd4l** — Anta B, Martín-Rodríguez C, Gomis-Perez C, Calvo L, López-Benito S, Calderón-García AA, et al. (2016). Ubiquitin-specific Protease 36 (USP36) Controls Neuronal Precursor Cell-expressed Developmentally Down-regulated 4-2 (Nedd4-2) Actions over the Neurotrophin Receptor TrkA and Potassium Voltage-gated Channels 7.2/3 (Kv7.2/3). *The Journal of biological chemistry* 291:19132-45. PMID: 27445338; PMCID: PMC5009282; DOI: 10.1074/jbc.M116.722637; https://doi.org/10.1074/jbc.M116.722637; https://pubmed.ncbi.nlm.nih.gov/27445338/
- **buszczak-2009-scrawny-h2b** — Buszczak M, Paterno S, Spradling AC (2009). Drosophila stem cells share a common requirement for the histone H2B ubiquitin protease scrawny. *Science (New York, N.Y.)* 323:248-51. PMID: 19039105; PMCID: PMC2759887; DOI: 10.1126/science.1165678; https://doi.org/10.1126/science.1165678; https://pubmed.ncbi.nlm.nih.gov/19039105/
- **chen-2020-p53-caspase-usp36** — Chen PH, Chen YT, Chu TY, Ma TH, Wu MH, Lin HH, et al. (2020). Nucleolar control by a non-apoptotic p53-caspases-deubiquitinylase axis promotes resistance to bacterial infection. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology* 34:1107-1121. PMID: 31914708; DOI: 10.1096/fj.201901959R; https://doi.org/10.1096/fj.201901959R; https://pubmed.ncbi.nlm.nih.gov/31914708/
- **chen-2023-exosc10-sumoylation** — Chen Y, Li Y, Dai RS, Savage JC, Shinde U, Klimek J, et al. (2023). The ubiquitin-specific protease USP36 SUMOylates EXOSC10 and promotes the nucleolar RNA exosome function in rRNA processing. *Nucleic acids research* 51:3934-3949. PMID: 36912080; PMCID: PMC10164564; DOI: 10.1093/nar/gkad140; https://doi.org/10.1093/nar/gkad140; https://pubmed.ncbi.nlm.nih.gov/36912080/
- **coirry-2025-drosophila-catalytic** — Coirry C, Manessier J, Clot C, Mortier M, Fauvarque MO, Taillebourg E (2025). The deubiquitinase USP36 funtions through catalytic-dependent and catalytic-independent mechanisms in Drosophila. *Genetics* 231. PMID: 40646716; PMCID: PMC12406001; DOI: 10.1093/genetics/iyaf131; https://doi.org/10.1093/genetics/iyaf131; https://pubmed.ncbi.nlm.nih.gov/40646716/
- **devine-2018-h2b-deubiquitinase** — DeVine T, Sears RC, Dai MS (2018). The ubiquitin-specific protease USP36 is a conserved histone H2B deubiquitinase. *Biochemical and biophysical research communications* 495:2363-2368. PMID: 29274341; PMCID: PMC5771408; DOI: 10.1016/j.bbrc.2017.12.107; https://doi.org/10.1016/j.bbrc.2017.12.107; https://pubmed.ncbi.nlm.nih.gov/29274341/
- **endo-2009-nucleolar-structure** — Endo A, Matsumoto M, Inada T, Yamamoto A, Nakayama KI, Kitamura N, et al. (2009). Nucleolar structure and function are regulated by the deubiquitylating enzyme USP36. *Journal of cell science* 122:678-86. PMID: 19208757; DOI: 10.1242/jcs.044461; https://doi.org/10.1242/jcs.044461; https://pubmed.ncbi.nlm.nih.gov/19208757/
- **endo-2009-nucleophosmin-usp36** — Endo A, Kitamura N, Komada M (2009). Nucleophosmin/B23 regulates ubiquitin dynamics in nucleoli by recruiting deubiquitylating enzyme USP36. *The Journal of biological chemistry* 284:27918-27923. PMID: 19679658; PMCID: PMC2788843; DOI: 10.1074/jbc.M109.037218; https://doi.org/10.1074/jbc.M109.037218; https://pubmed.ncbi.nlm.nih.gov/19679658/
- **fraile-2018-dhx33-lethality** — Fraile JM, Campos-Iglesias D, Rodríguez F, Astudillo A, Vilarrasa-Blasi R, Verdaguer-Dot N, et al. (2018). Loss of the deubiquitinase USP36 destabilizes the RNA helicase DHX33 and causes preimplantation lethality in mice. *The Journal of biological chemistry* 293:2183-2194. PMID: 29273634; PMCID: PMC5808777; DOI: 10.1074/jbc.M117.788430; https://doi.org/10.1074/jbc.M117.788430; https://pubmed.ncbi.nlm.nih.gov/29273634/
- **geisler-2019-mitophagy** — Geisler S, Jäger L, Golombek S, Nakanishi E, Hans F, Casadei N, et al. (2019). Ubiquitin-specific protease USP36 knockdown impairs Parkin-dependent mitophagy via downregulation of Beclin-1-associated autophagy-related ATG14L. *Experimental cell research* 384:111641. PMID: 31550441; DOI: 10.1016/j.yexcr.2019.111641; https://doi.org/10.1016/j.yexcr.2019.111641; https://pubmed.ncbi.nlm.nih.gov/31550441/
- **kim-2005-usp36-pest** — Kim MS, Kim YK, Kim YS, Seong M, Choi JK, Baek KH (2005). Deubiquitinating enzyme USP36 contains the PEST motif and is polyubiquitinated. *Biochemical and biophysical research communications* 330:797-804. PMID: 15809067; DOI: 10.1016/j.bbrc.2005.03.051; https://doi.org/10.1016/j.bbrc.2005.03.051; https://pubmed.ncbi.nlm.nih.gov/15809067/
- **kim-2011-sod2-usp36** — Kim MS, Ramakrishna S, Lim KH, Kim JH, Baek KH (2011). Protein stability of mitochondrial superoxide dismutase SOD2 is regulated by USP36. *Journal of cellular biochemistry* 112:498-508. PMID: 21268071; DOI: 10.1002/jcb.22940; https://doi.org/10.1002/jcb.22940; https://pubmed.ncbi.nlm.nih.gov/21268071/
- **li-2023-microprocessor-sumoylation** — Li Y, Carey TS, Feng CH, Zhu HM, Sun XX, Dai MS (2023). The Ubiquitin-specific Protease USP36 Associates with the Microprocessor Complex and Regulates miRNA Biogenesis by SUMOylating DGCR8. *Cancer research communications* 3:459-470. PMID: 36950067; PMCID: PMC10026737; DOI: 10.1158/2767-9764.CRC-22-0344; https://doi.org/10.1158/2767-9764.CRC-22-0344; https://pubmed.ncbi.nlm.nih.gov/36950067/
- **li-2024-las1l-sumoylation** — Li Y, Yang Y, Sears RC, Dai MS, Sun XX (2024). USP36 SUMOylates Las1L and Promotes Its Function in Pre-Ribosomal RNA ITS2 Processing. *Cancer research communications* 4:2835-2845. PMID: 39356143; PMCID: PMC11523043; DOI: 10.1158/2767-9764.CRC-24-0312; https://doi.org/10.1158/2767-9764.CRC-24-0312; https://pubmed.ncbi.nlm.nih.gov/39356143/
- **ling-2022-cep63** — Ling H, Cao CH, Han K, Lv YR, Ma XD, Cao JH, et al. (2022). CEP63 upregulates YAP1 to promote colorectal cancer progression through stabilizing RNA binding protein FXR1. *Oncogene* 41:4433-4445. PMID: 35989368; DOI: 10.1038/s41388-022-02439-y; https://doi.org/10.1038/s41388-022-02439-y; https://pubmed.ncbi.nlm.nih.gov/35989368/
- **niu-2024-review-cancer** — Niu MY, Liu YJ, Shi JJ, Chen RY, Zhang S, Li CY, et al. (2024). The Emerging Role of Ubiquitin-Specific Protease 36 (USP36) in Cancer and Beyond. *Biomolecules* 14. PMID: 38785979; PMCID: PMC11118191; DOI: 10.3390/biom14050572; https://doi.org/10.3390/biom14050572; https://pubmed.ncbi.nlm.nih.gov/38785979/
- **odea-2023-fubi-crossreactivity** — O'Dea R, Kazi N, Hoffmann-Benito A, Zhao Z, Recknagel S, Wendrich K, et al. (2023). Molecular basis for ubiquitin/Fubi cross-reactivity in USP16 and USP36. *Nature chemical biology* 19:1394-1405. PMID: 37443395; PMCID: PMC10611586; DOI: 10.1038/s41589-023-01388-1; https://doi.org/10.1038/s41589-023-01388-1; https://pubmed.ncbi.nlm.nih.gov/37443395/
- **qin-2023-snail1-nucleolar** — Qin K, Yu S, Liu Y, Guo R, Guo S, Fei J, et al. (2023). USP36 stabilizes nucleolar Snail1 to promote ribosome biogenesis and cancer cell survival upon ribotoxic stress. *Nature communications* 14:6473. PMID: 37833415; PMCID: PMC10575996; DOI: 10.1038/s41467-023-42257-8; https://doi.org/10.1038/s41467-023-42257-8; https://pubmed.ncbi.nlm.nih.gov/37833415/
- **quesada-2004-cloning-usps** — Quesada V, Díaz-Perales A, Gutiérrez-Fernández A, Garabaya C, Cal S, López-Otín C (2004). Cloning and enzymatic analysis of 22 novel human ubiquitin-specific proteases. *Biochemical and biophysical research communications* 314:54-62. PMID: 14715245; DOI: 10.1016/j.bbrc.2003.12.050; https://doi.org/10.1016/j.bbrc.2003.12.050; https://pubmed.ncbi.nlm.nih.gov/14715245/
- **reed-2015-disordered-regions-ubp10** — Reed BJ, Locke MN, Gardner RG (2015). A Conserved Deubiquitinating Enzyme Uses Intrinsically Disordered Regions to Scaffold Multiple Protein Interaction Sites. *The Journal of biological chemistry* 290:20601-12. PMID: 26149687; PMCID: PMC4536463; DOI: 10.1074/jbc.M115.650952; https://doi.org/10.1074/jbc.M115.650952; https://pubmed.ncbi.nlm.nih.gov/26149687/
- **richardson-2012-rna-pol-i** — Richardson LA, Reed BJ, Charette JM, Freed EF, Fredrickson EK, Locke MN, et al. (2012). A conserved deubiquitinating enzyme controls cell growth by regulating RNA polymerase I stability. *Cell reports* 2:372-85. PMID: 22902402; PMCID: PMC3638920; DOI: 10.1016/j.celrep.2012.07.009; https://doi.org/10.1016/j.celrep.2012.07.009; https://pubmed.ncbi.nlm.nih.gov/22902402/
- **rossio-2024-dub-specificity** — Rossio V, Paulo JA, Liu X, Gygi SP, King RW (2024). Specificity profiling of deubiquitylases against endogenously generated ubiquitin-protein conjugates. *Cell chemical biology* 31:1349-1362.e5. PMID: 38810651; PMCID: PMC11260241; DOI: 10.1016/j.chembiol.2024.05.001; https://doi.org/10.1016/j.chembiol.2024.05.001; https://pubmed.ncbi.nlm.nih.gov/38810651/
- **ryu-2021-snorna-sumoylation** — Ryu H, Sun XX, Chen Y, Li Y, Wang X, Dai RS, et al. (2021). The deubiquitinase USP36 promotes snoRNP group SUMOylation and is essential for ribosome biogenesis. *EMBO reports* 22:e50684. PMID: 33852194; PMCID: PMC8183414; DOI: 10.15252/embr.202050684; https://doi.org/10.15252/embr.202050684; https://pubmed.ncbi.nlm.nih.gov/33852194/
- **shao-2025-review-ribosome-biogenesis** — Shao L, Guo M, Kou Q, Guo Y, Li X, Li F (2025). The role of USP36 in ribosome biogenesis and other pathophysiological processes. *Frontiers in molecular biosciences* 12:1650908. PMID: 40909126; PMCID: PMC12404947; DOI: 10.3389/fmolb.2025.1650908; https://doi.org/10.3389/fmolb.2025.1650908; https://pubmed.ncbi.nlm.nih.gov/40909126/
- **sun-2015-deubiquitinating-cmyc-commentary** — Sun XX, Sears RC, Dai MS (2015). Deubiquitinating c-Myc: USP36 steps up in the nucleolus. *Cell cycle (Georgetown, Tex.)* 14:3786-93. PMID: 26697836; PMCID: PMC4825782; DOI: 10.1080/15384101.2015.1093713; https://doi.org/10.1080/15384101.2015.1093713; https://pubmed.ncbi.nlm.nih.gov/26697836/
- **sun-2015-usp36-cmyc** — Sun XX, He X, Yin L, Komada M, Sears RC, Dai MS (2015). The nucleolar ubiquitin-specific protease USP36 deubiquitinates and stabilizes c-Myc. *Proceedings of the National Academy of Sciences of the United States of America* 112:3734-9. PMID: 25775507; PMCID: PMC4378440; DOI: 10.1073/pnas.1411713112; https://doi.org/10.1073/pnas.1411713112; https://pubmed.ncbi.nlm.nih.gov/25775507/
- **taillebourg-2012-selective-autophagy** — Taillebourg E, Gregoire I, Viargues P, Jacomin AC, Thevenon D, Faure M, et al. (2012). The deubiquitinating enzyme USP36 controls selective autophagy activation by ubiquitinated proteins. *Autophagy* 8:767-79. PMID: 22622177; DOI: 10.4161/auto.19381; https://doi.org/10.4161/auto.19381; https://pubmed.ncbi.nlm.nih.gov/22622177/
- **thevenon-2020-nucleolar-isoform-dusp36** — Thevenon D, Seffouh I, Pillet C, Crespo-Yanez X, Fauvarque MO, Taillebourg E (2020). A Nucleolar Isoform of the Drosophila Ubiquitin Specific Protease dUSP36 Regulates MYC-Dependent Cell Growth. *Frontiers in cell and developmental biology* 8:506. PMID: 32637412; PMCID: PMC7316882; DOI: 10.3389/fcell.2020.00506; https://doi.org/10.3389/fcell.2020.00506; https://pubmed.ncbi.nlm.nih.gov/32637412/
- **vandenheuvel-2021-fubi-processing** — van den Heuvel J, Ashiono C, Gillet LC, Dörner K, Wyler E, Zemp I, et al. (2021). Processing of the ribosomal ubiquitin-like fusion protein FUBI-eS30/FAU is required for 40S maturation and depends on USP36. *eLife* 10. PMID: 34318747; PMCID: PMC8354635; DOI: 10.7554/eLife.70560; https://doi.org/10.7554/eLife.70560; https://pubmed.ncbi.nlm.nih.gov/34318747/
- **wang-2020-donkey-genomes** — Wang C, Li H, Guo Y, Huang J, Sun Y, Min J, et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nature communications* 11:6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7; https://doi.org/10.1038/s41467-020-19813-7; https://pubmed.ncbi.nlm.nih.gov/33293529/
- **yan-2020-primpol** — Yan Y, Xu Z, Huang J, Guo G, Gao M, Kim W, et al. (2020). The deubiquitinase USP36 Regulates DNA replication stress and confers therapeutic resistance through PrimPol stabilization. *Nucleic acids research* 48:12711-12726. PMID: 33237263; PMCID: PMC7736794; DOI: 10.1093/nar/gkaa1090; https://doi.org/10.1093/nar/gkaa1090; https://pubmed.ncbi.nlm.nih.gov/33237263/
- **yang-2024-review-sumoylation** — Yang Y, Li Y, Sears RC, Sun XX, Dai MS (2024). SUMOylation regulation of ribosome biogenesis: Emerging roles for USP36. *Frontiers in RNA research* 2. PMID: 38764604; PMCID: PMC11101209; DOI: 10.3389/frnar.2024.1389104; https://doi.org/10.3389/frnar.2024.1389104; https://pubmed.ncbi.nlm.nih.gov/38764604/
- **yang-2025-gnl3-sumoylation** — Yang Y, Li Y, Dai RS, Chen C, Zientek K, Reddy A, et al. (2025). GNL3 SUMOylation is essential for DNA double-strand break repair by homologous recombination. *bioRxiv : the preprint server for biology* (no volume/pages). PMID: 41279596; PMCID: PMC12637502; DOI: 10.1101/2025.11.04.686352; https://doi.org/10.1101/2025.11.04.686352; https://pubmed.ncbi.nlm.nih.gov/41279596/
- **UniProt A0A9L0JCH5** — UniProtKB/TrEMBL entry, Ubiquitin carboxyl-terminal hydrolase (USP36), *Equus asinus*; https://rest.uniprot.org/uniprotkb/A0A9L0JCH5.txt (local copy `uniprot_A0A9L0JCH5.txt`)
- **UniProt A0A9L0I9H9 / A0A8C4LEG8 / F6W2H6** — additional UniProtKB/TrEMBL USP36 entries for donkey (A0A9L0I9H9, A0A8C4LEG8) and horse (F6W2H6); retrieved via https://rest.uniprot.org/uniprotkb/search?query=gene_exact:USP36+AND+organism_id:9793 and organism_id:9796 (local copies `donkey_all.fasta`, `horse.fasta`, `uniprot_F6W2H6_horse.txt`)
- **UniProt Q9P275** — UniProtKB/Swiss-Prot entry, Ubiquitin carboxyl-terminal hydrolase 36, *Homo sapiens*; https://rest.uniprot.org/uniprotkb/Q9P275.txt (local copy `uniprot_Q9P275_human.txt`)
- **SEQUENCE_NOTES.md** — pairwise alignment of A0A9L0JCH5 and Q9P275 carried out for this report (own analysis)


## Citations

1. anta-2016-usp36-nedd4l-abstract.md
2. anta-2016-usp36-nedd4l-summary.md
3. buszczak-2009-scrawny-h2b-abstract.md
4. buszczak-2009-scrawny-h2b-summary.md
5. chen-2020-p53-caspase-usp36-abstract.md
6. chen-2020-p53-caspase-usp36-summary.md
7. chen-2023-exosc10-sumoylation-abstract.md
8. chen-2023-exosc10-sumoylation-fulltext.txt
9. chen-2023-exosc10-sumoylation-summary.md
10. coirry-2025-drosophila-catalytic-abstract.md
11. coirry-2025-drosophila-catalytic-fulltext.txt
12. coirry-2025-drosophila-catalytic-summary.md
13. devine-2018-h2b-deubiquitinase-abstract.md
14. devine-2018-h2b-deubiquitinase-fulltext.txt
15. devine-2018-h2b-deubiquitinase-summary.md
16. endo-2009-nucleolar-structure-abstract.md
17. endo-2009-nucleolar-structure-summary.md
18. endo-2009-nucleophosmin-usp36-abstract.md
19. endo-2009-nucleophosmin-usp36-summary.md
20. fraile-2018-dhx33-lethality-abstract.md
21. fraile-2018-dhx33-lethality-summary.md
22. geisler-2019-mitophagy-abstract.md
23. geisler-2019-mitophagy-summary.md
24. kim-2005-usp36-pest-abstract.md
25. kim-2005-usp36-pest-summary.md
26. kim-2011-sod2-usp36-abstract.md
27. kim-2011-sod2-usp36-summary.md
28. li-2023-microprocessor-sumoylation-abstract.md
29. li-2023-microprocessor-sumoylation-fulltext.txt
30. li-2023-microprocessor-sumoylation-summary.md
31. li-2024-las1l-sumoylation-abstract.md
32. li-2024-las1l-sumoylation-fulltext.txt
33. li-2024-las1l-sumoylation-summary.md
34. ling-2022-cep63-abstract.md
35. ling-2022-cep63-summary.md
36. meta.json
37. niu-2024-review-cancer-abstract.md
38. niu-2024-review-cancer-fulltext.txt
39. niu-2024-review-cancer-summary.md
40. odea-2023-fubi-crossreactivity-abstract.md
41. odea-2023-fubi-crossreactivity-fulltext.txt
42. odea-2023-fubi-crossreactivity-summary.md
43. qin-2023-snail1-nucleolar-abstract.md
44. qin-2023-snail1-nucleolar-fulltext.txt
45. qin-2023-snail1-nucleolar-summary.md
46. quesada-2004-cloning-usps-abstract.md
47. quesada-2004-cloning-usps-summary.md
48. reed-2015-disordered-regions-ubp10-abstract.md
49. reed-2015-disordered-regions-ubp10-summary.md
50. richardson-2012-rna-pol-i-abstract.md
51. richardson-2012-rna-pol-i-fulltext.txt
52. richardson-2012-rna-pol-i-summary.md
53. rossio-2024-dub-specificity-abstract.md
54. rossio-2024-dub-specificity-fulltext.txt
55. rossio-2024-dub-specificity-summary.md
56. ryu-2021-snorna-sumoylation-abstract.md
57. ryu-2021-snorna-sumoylation-summary.md
58. shao-2025-review-ribosome-biogenesis-abstract.md
59. shao-2025-review-ribosome-biogenesis-fulltext.txt
60. shao-2025-review-ribosome-biogenesis-summary.md
61. sun-2015-deubiquitinating-cmyc-commentary-abstract.md
62. sun-2015-deubiquitinating-cmyc-commentary-summary.md
63. sun-2015-usp36-cmyc-abstract.md
64. sun-2015-usp36-cmyc-summary.md
65. taillebourg-2012-selective-autophagy-abstract.md
66. taillebourg-2012-selective-autophagy-summary.md
67. thevenon-2020-nucleolar-isoform-dusp36-abstract.md
68. thevenon-2020-nucleolar-isoform-dusp36-fulltext.txt
69. thevenon-2020-nucleolar-isoform-dusp36-summary.md
70. vandenheuvel-2021-fubi-processing-abstract.md
71. vandenheuvel-2021-fubi-processing-fulltext.txt
72. vandenheuvel-2021-fubi-processing-summary.md
73. wang-2020-donkey-genomes-abstract.md
74. wang-2020-donkey-genomes-fulltext.txt
75. wang-2020-donkey-genomes-summary.md
76. yan-2020-primpol-abstract.md
77. yan-2020-primpol-fulltext.txt
78. yan-2020-primpol-summary.md
79. yang-2024-review-sumoylation-abstract.md
80. yang-2024-review-sumoylation-fulltext.txt
81. yang-2024-review-sumoylation-summary.md
82. yang-2025-gnl3-sumoylation-abstract.md
83. yang-2025-gnl3-sumoylation-fulltext.txt
84. yang-2025-gnl3-sumoylation-summary.md