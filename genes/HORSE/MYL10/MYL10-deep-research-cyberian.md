---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:17:47.915428'
end_time: '2026-10-26T03:29:09.282172'
duration_seconds: 681.37
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: MYL10
  gene_symbol: MYL10
  uniprot_accession: A0A9L0TJE1
  protein_description: 'SubName: Full=Myosin light chain 10 {ECO:0000313|Ensembl:ENSECAP00000086465.1};'
  gene_info: Name=MYL10 {ECO:0000313|Ensembl:ENSECAP00000086465.1};
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: EF-hand-dom_pair. (IPR011992); EF_Hand_1_Ca_BS. (IPR018247); EF_hand_dom.
    (IPR002048); Myosin_RLC. (IPR050403); EF-hand_1 (PF00036)
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
citation_count: 43
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0TJE1
- **Protein Description:** SubName: Full=Myosin light chain 10 {ECO:0000313|Ensembl:ENSECAP00000086465.1};
- **Gene Information:** Name=MYL10 {ECO:0000313|Ensembl:ENSECAP00000086465.1};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** EF-hand-dom_pair. (IPR011992); EF_Hand_1_Ca_BS. (IPR018247); EF_hand_dom. (IPR002048); Myosin_RLC. (IPR050403); EF-hand_1 (PF00036)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MYL10" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MYL10' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MYL10** (gene ID: MYL10, UniProt: A0A9L0TJE1) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MYL10 (Myosin Regulatory Light Chain 10) in the Horse, *Equus caballus* (UniProt A0A9L0TJE1)

## Introduction and Summary

The horse protein A0A9L0TJE1 is an unreviewed, computationally predicted 212-residue polypeptide named "Myosin light chain 10" by Ensembl (ENSECAP00000086465.1, gene ENSECAG00000022094 on horse chromosome 13, NCBI GeneID 100060444). Its database cross-reference to CTD 93408 ties it to human MYL10 [uniprot-A0A9L0TJE1]. It carries tandem EF-hand domains, a PROSITE EF-hand calcium-binding signature and the InterPro "Myosin regulatory light chain" family signature (IPR050403; PANTHER PTHR23049, "Myosin regulatory light chain 2") [uniprot-A0A9L0TJE1]. The identity check came out consistent: the gene symbol, the protein description, the domain architecture and the orthology mapping all point to one gene, MYL10. In human and mouse this gene is also called PLRLC or MYLC2PL ("precursor lymphocyte-specific regulatory light chain"; "myosin light chain 2, lymphocyte-specific") [uniprot-Q9BUA6-human-MYL10; uniprot-Q62082-mouse-Myl10]. I found no literature on a different gene sharing this symbol that might cause confusion. I also found no published experimental study of the horse protein. Its UniProt protein-existence level is "predicted", and its only GO annotations are phylogenetically inferred (IBA): cytoplasm, mitochondrion and calcium ion binding [uniprot-A0A9L0TJE1].

The best-supported statement about its primary function is therefore inferred by homology. MYL10 belongs to the regulatory light chain (RLC) family of the class II ("conventional") myosin holoenzyme. RLCs are calmodulin-related EF-hand proteins that wrap around the IQ-motif neck of the myosin heavy chain, adjacent to the essential light chain. There they stabilise the lever arm and act as the principal phosphorylation-dependent switch controlling myosin II activity [heissler-2014-myosin-light-chains; xie-1994-scallop-regulatory-domain]. The protein is not an enzyme. It is a regulatory and structural subunit of an actin-based ATPase motor, and it most likely functions in the cytoplasm, bound to myosin II heavy chains in actomyosin assemblies. The only gene-specific experimental work on MYL10 orthologs comes from mouse. There the transcript was discovered as an IL-7-inducible RLC expressed specifically in precursor B and T lymphocytes, the first RLC with specific expression in non-muscle cells [oltz-1992-plrlc]. Human expression data show very low, narrowly distributed transcription, enriched in skeletal muscle, epididymal principal cells and peritubular myoid cells [hpa-ENSG00000106436-MYL10]. My own sequence comparison (described below) places the horse protein closest to the sarcomeric RLCs MYL2 and MYL11, not to the nonmuscle RLCs MYL9 and MYL12A/B. That result suggests the biochemistry of the horse protein, including its likely phosphorylation site, resembles that of striated-muscle RLCs.

## Identity, Gene Structure and Evolutionary Placement

The horse sequence comes from the Thoroughbred reference genome [wade-2009-horse-genome] and was predicted by Ensembl; no horse cDNA or protein evidence is recorded [uniprot-A0A9L0TJE1]. Its human ortholog, MYL10 (Q9BUA6, 226 residues, chromosome 7q22.1), is a reviewed Swiss-Prot entry with protein-level existence evidence from proteomics. That entry nonetheless holds little functional annotation beyond "myosin is a hexamer of 2 heavy chains and 4 light chains" and "this chain binds calcium", both by similarity [uniprot-Q9BUA6-human-MYL10]. Pharos classifies human MYL10 as "Tdark", an understudied target [uniprot-Q9BUA6-human-MYL10]. Heissler and Sellers list MYL10 among the eight human RLC genes (MYL2, MYL5, MYL7, MYL9, MYL10, MYL11, MYL12A, MYL12B). They note that RLC gene products are 172–226 residues long, share high structural similarity with calmodulin, and contain four EF-hand motifs, some of them degenerate. Their only remark specific to this gene is that "MYL10 encodes for an RLC that might be a lymphocyte specific precursor" [heissler-2014-myosin-light-chains].

To place the horse protein within this family, I aligned it with human MYL10, MYL9, MYL12A, MYL12B, MYL11 and MYL2 using MAFFT L-INS-i (analysis/rlc.aln.txt; analysis/NOTES.md). Horse residues 46–212 align end-to-end with the canonical RLC fold. Over that region the horse protein is 97.6% identical to human MYL10, 81.3% identical to the ventricular/slow-skeletal RLC MYL2, 73.7% identical to the fast-skeletal RLC MYL11, and only about 55–57% identical to the nonmuscle/smooth-muscle RLCs MYL9, MYL12A and MYL12B (analysis/identity.txt). MYL10 thus belongs to the sarcomeric branch of the RLC family. The alignment also reveals two structural differences from the human protein. First, the canonical human MYL10 isoform carries an insertion of about 34 residues after the conserved QIQEFKE segment, and the horse model lacks it, so the horse protein has the uninterrupted RLC architecture. Second, the horse protein's first ~45 residues form a basic, predicted-disordered extension (UniProt flags 1–59 as disordered with basic compositional bias) that is unrelated to the human N terminus [uniprot-A0A9L0TJE1]. In mouse, Oltz and colleagues reported several PLRLC transcripts that "potentially encode regulatory myosin light chains with unique structural features" [oltz-1992-plrlc], and the mouse UniProt entry records at least three spliced isoforms, with more suspected [uniprot-Q62082-mouse-Myl10]. The variable N-terminal and internal segments seen across species are therefore probably the product of alternative exon usage at this locus. They also mean that the exact horse gene model should be treated cautiously until transcript evidence confirms it.

## Molecular Function: A Calmodulin-Like Regulatory Subunit of Myosin II

The general function of RLCs is understood in detail. Light chains are calmodulin-family proteins that bind the IQ motifs in the neck region of the myosin heavy chain. In class II myosins the essential light chain occupies IQ1 and the regulatory light chain occupies IQ2, with high specificity [heissler-2014-myosin-light-chains]. The crystal structure of the scallop myosin regulatory domain at 2.8 Å showed the two light chains linked in tandem to adjacent IQ-bearing segments of the heavy chain. Their side-chain interactions stabilise the neck and, in scallop, form a composite Ca2+-regulatory site [xie-1994-scallop-regulatory-domain]. RLCs bind divalent cations through their N-terminal EF-hand. Scallop RLC can be stripped gently from IQ2 with the chelator EDTA, and the empty site will accept RLCs from almost any species in vitro [heissler-2014-myosin-light-chains]. The horse MYL10 sequence keeps this cation-binding loop intact (D83-Q-N-R-D-G-F-I-D-K-E-D94). The loop matches human MYL10, MYL2 and MYL11 exactly, and PROSITE annotates it as an EF-hand calcium-binding site (analysis/rlc.aln.txt; [uniprot-A0A9L0TJE1]). The C-terminal EF-hand region is predicted but lacks a recognised calcium-binding signature, consistent with the degenerate EF-hands typical of RLCs [heissler-2014-myosin-light-chains].

The regulatory part of an RLC's function lies in its N-terminal phosphorylation domain. Heissler and Sellers describe the first ~24 residues of the RLC as a "phosphorylation domain" rich in positively charged residues. In smooth-muscle and nonmuscle myosin II, phosphorylation of Ser19 converts the compact, autoinhibited (10S) myosin into an extended conformation that assembles into bipolar filaments and has much higher actin-activated ATPase activity; dephosphorylation by myosin phosphatase reverses this [heissler-2014-myosin-light-chains]. Ser19 phosphorylation increases the actin-activated Mg2+-ATPase by changing head conformation, not actin affinity, and additional phosphorylation of Thr18 raises activity further [vicente-manzanares-2009-nmii]. Ikebe and Hartshorne had first shown, with gizzard myosin, that MLCK phosphorylates Ser19 preferentially and a nearby threonine more slowly, and that the second phosphorylation further raises actin-activated ATPase activity [ikebe-1985-two-sites]. Striated-muscle RLCs follow a related scheme. The equivalent residue (Ser15 in skeletal and human ventricular RLC) is phosphorylated by dedicated Ca2+/calmodulin-dependent kinases, skeletal MLCK (MYLK2) and cardiac MLCK. In those muscles phosphorylation does not switch contraction on; it modulates it, increasing the rate of cross-bridge force generation and the Ca2+ sensitivity of the myofilaments, and producing post-activation force potentiation [stull-2011-skeletal-mlck; scruggs-2011-cardiac-rlc].

## The Putative Phosphorylation Site of Horse MYL10 and Its Kinases

In the horse sequence, Ser61 (in the motif S-S-N-V-F) sits at the position equivalent to Ser19 of MYL9 and Ser15 of MYL2 (analysis/NOTES.md). The surrounding residues resemble the sarcomeric pattern more than the nonmuscle one. The nonmuscle RLCs have K-K-R-P-Q-R-A-T18-S19-N-V-F, with an arginine three residues before the serine and a phosphorylatable threonine immediately before it. Horse MYL10 instead reads R52-K53-R54-A-E-G-A-A-S60-S61-N-V-F, much like MYL2's K-K-R-A-G-G-A-N-S15-N-V-F, though with one extra residue and a glutamate inserted between the basic cluster and the serine (analysis/rlc.aln.txt). Substrate recognition by MLCK depends strongly on such basic residues. Synthetic-peptide studies identified the Lys-Lys-Arg cluster as a primary specificity determinant [kemp-1983-mlck-peptides]. Kemp and Pearson then showed that the position of Arg16 relative to Ser19, and the spacing between the basic cluster and Arg16, profoundly affect both phosphorylation kinetics and which residue (Ser19 or Thr18) is modified [kemp-1985-mlck-basic-residues]. Because horse MYL10 lacks the arginine at −3 and has an altered spacing to its basic cluster, it remains an open question whether it is an efficient MLCK substrate and which kinase targets it. Its sarcomeric-like motif makes a striated-muscle MLCK the most plausible candidate where the protein is co-expressed with sarcomeric myosin [stull-2011-skeletal-mlck]. Its basic N-terminal extension might supply additional recognition determinants. This is a hypothesis from sequence analysis; no data test it.

## Predicted Structure and the Mechanism of RLC-Mediated Regulation

The AlphaFold model of the horse protein supports this domain picture (AF-A0A9L0TJE1-F1, v6). Global mean pLDDT is 71. About 66% of residues are modelled with confident or very high confidence, and 28% with very low confidence [alphafold-A0A9L0TJE1]. When the downloaded per-residue scores are averaged by region, the N-terminal extension (residues 1–45, mean pLDDT 38) and the phosphorylation domain (46–65, mean 47) come out as disordered. The N-terminal EF-hand lobe (66–140, mean 87) and the C-terminal lobe (141–212, mean 83) form well-predicted globular domains (analysis/alphafold_plddt.txt). This is the expected shape for a calmodulin-like RLC modelled without its heavy-chain partner. The two lobes would clamp onto the IQ2 helix of the heavy chain, as in the scallop regulatory-domain structure [xie-1994-scallop-regulatory-domain]. The flexible N-terminal phosphorylation domain is the part that changes position on phosphorylation in other RLCs.

Biochemical work on smooth-muscle myosin explains how such an N-terminal segment controls the motor. Wu and colleagues photocross-linked single-cysteine RLC mutants within heavy meromyosin. In the dephosphorylated state, Gln15, Ala23 and Cys108 of one head's RLC lie within about 9 Å of the RLC on the partner head, and thiophosphorylation abolishes that proximity [wu-1999-rlc-crosslinking]. Li and colleagues built a heavy meromyosin with one complete head and one head reduced to the RLC-binding neck and its bound RLC. This construct was still switched off when dephosphorylated and activated by phosphorylation. The interaction between the RLC domains of the two heads, or between an RLC domain and the partner motor domain, is therefore sufficient to inhibit the motor, and the RLC domain alone can drive the transition between folded and extended conformations [li-2000-rlc-head-interaction]. By analogy, if MYL10 is incorporated into a myosin II hexamer, its N-terminal region (including the S60–S61 pair and the basic extension unique to the horse model) would be the element that couples phosphorylation to head–head interactions. Whether the long disordered extension enhances or interferes with this mechanism cannot be predicted from the available data.

## Pathway Context: The MLCK/MLCP Signalling Axis

If MYL10 behaves like other RLCs, its activity state would be set by the pathways that control RLC phosphorylation generally. For smooth-muscle and nonmuscle myosin II, Somlyo and Somlyo describe the Ca2+ sensitivity of contraction as the ratio of MLCK to myosin light-chain phosphatase (MLCP) activity. Ca2+/calmodulin activates MLCK. The RhoA/Rho-kinase pathway, acting downstream of Gq/G12/13-coupled receptors, inhibits MLCP directly or through the inhibitor protein CPI-17, which raises RLC phosphorylation independently of Ca2+, while cGMP-dependent kinase opposes this sensitisation [somlyo-2003-ca-sensitivity]. More than a dozen kinases, including MLCK, ROCK, citron kinase, ZIPK and MRCK, can phosphorylate nonmuscle RLCs and thereby integrate signals controlling adhesion, migration and tissue architecture [vicente-manzanares-2009-nmii]. In striated muscle the corresponding axis is narrower: a dedicated Ca2+/calmodulin-activated skeletal or cardiac MLCK opposes a muscle-specific phosphatase (MYPT2 in heart) [stull-2011-skeletal-mlck; scruggs-2011-cardiac-rlc]. Reactome assigns human MYL10 to its "Smooth Muscle Contraction" pathway [uniprot-Q9BUA6-human-MYL10]. That assignment almost certainly reflects family membership, not gene-specific evidence.

## Expression and Subcellular Localisation

The single gene-specific functional study comes from mouse. Oltz and colleagues cloned PLRLC as a regulatory myosin light chain gene expressed specifically in precursor B and T lymphocytes. Expression was induced by interleukin-7 in adult bone-marrow-derived pre-B cells, but was absent from fetal-liver-derived pre-B cells and pre-B clones, so the gene marked distinct pre-B subsets [oltz-1992-plrlc]. The mouse UniProt entry carries these observations as experimentally supported tissue specificity and induction annotations [uniprot-Q62082-mouse-Myl10]. In human tissues the picture differs. The Human Protein Atlas detects MYL10 RNA at very low levels, with "tissue enhanced" expression in skeletal muscle (about 1.3 nTPM). At single-cell resolution the gene is enriched in epididymal principal cells and testicular peritubular myoid cells, and among blood cells modestly in basophils [hpa-ENSG00000106436-MYL10]. In Chinese perch, a gene annotated myl10 was preferentially transcribed in slow muscle [fang-2026-perch-myl-family]. That abstract does not establish orthology to mammalian MYL10, so the observation is at most suggestive of a muscle-associated expression pattern in vertebrates. No expression data specific to the horse protein were found.

At the subcellular level, myosin RLCs act in the cytoplasm as stoichiometric subunits of myosin II hexamers. In muscle cells these hexamers sit within sarcomeric thick filaments, and in non-muscle cells within cortical and stress-fibre actomyosin [heissler-2014-myosin-light-chains; vicente-manzanares-2009-nmii]. The cytoplasm annotation on the horse entry is consistent with this [uniprot-A0A9L0TJE1]. The mitochondrion annotation propagated to the horse protein traces back to a direct-assay annotation on human MYL10 sourced from LIFEdb, a high-throughput localisation resource, [uniprot-Q9BUA6-human-MYL10]. No precise study supports it, and it should be regarded as unconfirmed. It could be an artefact of overexpression or of the unusual N-terminal extensions in some isoforms.

## Synthesis

Taken together, the evidence supports annotating horse A0A9L0TJE1 as a myosin II regulatory light chain. Its molecular function is divalent cation (Ca2+/Mg2+) binding through a conserved N-terminal EF-hand, together with binding of the myosin heavy chain IQ2 motif, and it probably acts as a phosphorylation-regulated modulator of myosin motor activity in the cytoplasm. These assignments rest on homology and domain architecture [uniprot-A0A9L0TJE1; heissler-2014-myosin-light-chains; xie-1994-scallop-regulatory-domain], not on direct experiments with the horse protein. Its closest paralogs are the sarcomeric RLCs, and its putative phosphoserine motif resembles theirs, which points to a striated-muscle-type mode of regulation [stull-2011-skeletal-mlck; scruggs-2011-cardiac-rlc]. Its unusual expression (pre-lymphocytes in mouse [oltz-1992-plrlc], very low and patchy expression in human [hpa-ENSG00000106436-MYL10]) and its isoform-variable N terminus suggest a specialised or minor role relative to the dominant RLCs MYL2, MYL9 and MYL12A/B. Assigning it a biological process beyond "myosin II regulation" is not justified by current evidence.

## Open Questions

Many basic facts about MYL10 remain unknown, in horse and in other mammals. The horse gene model first needs transcript support: RNA-seq or long-read data from horse muscle and lymphoid tissues would show whether the 45-residue basic N-terminal extension and the absence of the human-type internal insertion reflect real isoforms. Second, it is unknown whether MYL10 assembles with myosin II heavy chains in vivo. If it does, which heavy chains it pairs with could be tested by co-immunoprecipitation or proteomics of purified myosin from tissues that express it. Third, whether Ser61 (horse numbering) is phosphorylated, and by which kinase, should be tested biochemically with skeletal MLCK, smooth/nonmuscle MLCK and ROCK, given the altered basic-residue spacing. Fourth, the cation-binding properties of its EF-hand (Ca2+ versus Mg2+ affinity) have not been measured. Fifth, the lymphocyte-precursor expression reported in mouse in 1992 has not, to my knowledge, been revisited with modern single-cell atlases, and its relevance to horse or human haematopoiesis is unknown. Finally, the high-throughput mitochondrial localisation should be checked with endogenous-protein methods. Useful follow-ups include structural modelling of MYL10 bound to an IQ2 segment (the AlphaFold model exists for A0A9L0TJE1), a phylogenetic analysis resolving whether fish "myl10" genes are true orthologs, and mining equine muscle proteomics datasets for MYL10 peptides.

## References

[uniprot-A0A9L0TJE1] UniProtKB/TrEMBL entry A0A9L0TJE1_HORSE, "Myosin light chain 10" (Equus caballus), entry version 15. https://rest.uniprot.org/uniprotkb/A0A9L0TJE1.txt

[uniprot-Q9BUA6-human-MYL10] UniProtKB/Swiss-Prot entry Q9BUA6 (MYL10_HUMAN), "Myosin regulatory light chain 10", entry version 170. https://rest.uniprot.org/uniprotkb/Q9BUA6.txt

[uniprot-Q62082-mouse-Myl10] UniProtKB/Swiss-Prot entry Q62082 (MYL10_MOUSE), "Myosin regulatory light chain 10". https://rest.uniprot.org/uniprotkb/Q62082.txt

[hpa-ENSG00000106436-MYL10] Human Protein Atlas, MYL10 (ENSG00000106436) record. https://www.proteinatlas.org/ENSG00000106436.json

[oltz-1992-plrlc] Oltz EM, Yancopoulos GD, Morrow MA, Rolink A, Lee G, Wong F, Kaplan K, Gillis S, Melchers F, Alt FW. A novel regulatory myosin light chain gene distinguishes pre-B cell subsets and is IL-7 inducible. EMBO J. 1992;11(7):2759-67. PMID: 1628631; PMCID: PMC556751; DOI: 10.1002/j.1460-2075.1992.tb05341.x

[heissler-2014-myosin-light-chains] Heissler SM, Sellers JR. Myosin light chains: Teaching old dogs new tricks. Bioarchitecture. 2014;4(6):169-88. PMID: 26155737; PMCID: PMC4914028; DOI: 10.1080/19490992.2015.1054092

[vicente-manzanares-2009-nmii] Vicente-Manzanares M, Ma X, Adelstein RS, Horwitz AR. Non-muscle myosin II takes centre stage in cell adhesion and migration. Nat Rev Mol Cell Biol. 2009;10:778-90. PMID: 19851336; PMCID: PMC2834236; DOI: 10.1038/nrm2786

[stull-2011-skeletal-mlck] Stull JT, Kamm KE, Vandenboom R. Myosin light chain kinase and the role of myosin light chain phosphorylation in skeletal muscle. Arch Biochem Biophys. 2011;510(2):120-8. PMID: 21284933; PMCID: PMC3101293; DOI: 10.1016/j.abb.2011.01.017

[scruggs-2011-cardiac-rlc] Scruggs SB, Solaro RJ. The significance of regulatory light chain phosphorylation in cardiac physiology. Arch Biochem Biophys. 2011;510:129-34. PMID: 21345328; PMCID: PMC3114105; DOI: 10.1016/j.abb.2011.02.013

[xie-1994-scallop-regulatory-domain] Xie X, Harrison DH, Schlichting I, Sweet RM, Kalabokis VN, Szent-Györgyi AG, Cohen C. Structure of the regulatory domain of scallop myosin at 2.8 A resolution. Nature. 1994;368(6469):306-12. PMID: 8127365; DOI: 10.1038/368306a0

[somlyo-2003-ca-sensitivity] Somlyo AP, Somlyo AV. Ca2+ sensitivity of smooth muscle and nonmuscle myosin II: modulated by G proteins, kinases, and myosin phosphatase. Physiol Rev. 2003;83:1325-58. PMID: 14506307; DOI: 10.1152/physrev.00023.2003

[ikebe-1985-two-sites] Ikebe M, Hartshorne DJ. Phosphorylation of smooth muscle myosin at two distinct sites by myosin light chain kinase. J Biol Chem. 1985;260(18):10027-31. PMID: 3839510

[kemp-1983-mlck-peptides] Kemp BE, Pearson RB, House C. Role of basic residues in the phosphorylation of synthetic peptides by myosin light chain kinase. Proc Natl Acad Sci U S A. 1983;80(24):7471-5. PMID: 6584865; PMCID: PMC389973; DOI: 10.1073/pnas.80.24.7471

[kemp-1985-mlck-basic-residues] Kemp BE, Pearson RB. Spatial requirements for location of basic residues in peptide substrates for smooth muscle myosin light chain kinase. J Biol Chem. 1985;260(6):3355-9. PMID: 3838312

[wade-2009-horse-genome] Wade CM, Giulotto E, Sigurdsson S, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. Science. 2009;326:865-7. PMID: 19892987; PMCID: PMC3785132; DOI: 10.1126/science.1178158

[fang-2026-perch-myl-family] Fang Y, Zhang L, Pan Y, Zhu X, Li H, Bao L, Chu W. Genome-wide characterisation of the myosin light chain gene family in Chinese perch (Siniperca chuatsi) and its expression patterns in muscle fibre types and injury response. Comp Biochem Physiol Part D Genomics Proteomics. 2026;60:101899. PMID: 42284893; DOI: 10.1016/j.cbd.2026.101899

[li-2000-rlc-head-interaction] Li XD, Saito J, Ikebe R, Mabuchi K, Ikebe M. The interaction between the regulatory light chain domains on two heads is critical for regulation of smooth muscle myosin. Biochemistry. 2000;39(9):2254-60. PMID: 10694391; DOI: 10.1021/bi9924617

[wu-1999-rlc-crosslinking] Wu X, Clack BA, Zhi G, Stull JT, Cremo CR. Phosphorylation-dependent structural changes in the regulatory light chain domain of smooth muscle heavy meromyosin. J Biol Chem. 1999;274(29):20328-35. PMID: 10400655; DOI: 10.1074/jbc.274.29.20328

[alphafold-A0A9L0TJE1] AlphaFold Protein Structure Database, model AF-A0A9L0TJE1-F1 (version 6), prediction metadata and per-residue confidence. https://alphafold.ebi.ac.uk/api/prediction/A0A9L0TJE1 ; https://alphafold.ebi.ac.uk/files/AF-A0A9L0TJE1-F1-confidence_v6.json

Own analysis files: analysis/rlc.fasta, analysis/rlc.aln.fasta, analysis/rlc.aln.txt, analysis/identity.txt, analysis/NOTES.md (MAFFT L-INS-i alignment of UniProt sequences), analysis/alphafold_plddt.txt (regional pLDDT means).


## Citations

1. alphafold-A0A9L0TJE1-confidence.json
2. alphafold-A0A9L0TJE1-prediction.json
3. alphafold-A0A9L0TJE1-summary.md
4. fang-2026-perch-myl-family-abstract.md
5. fang-2026-perch-myl-family-summary.md
6. heissler-2014-myosin-light-chains-abstract.md
7. heissler-2014-myosin-light-chains-fulltext.txt
8. heissler-2014-myosin-light-chains-summary.md
9. hpa-ENSG00000106436-MYL10-record.json
10. hpa-ENSG00000106436-MYL10-summary.md
11. ikebe-1985-two-sites-abstract.md
12. ikebe-1985-two-sites-summary.md
13. kemp-1983-mlck-peptides-abstract.md
14. kemp-1983-mlck-peptides-summary.md
15. kemp-1985-mlck-basic-residues-abstract.md
16. kemp-1985-mlck-basic-residues-summary.md
17. li-2000-rlc-head-interaction-abstract.md
18. li-2000-rlc-head-interaction-summary.md
19. oltz-1992-plrlc-abstract.md
20. oltz-1992-plrlc-summary.md
21. scruggs-2011-cardiac-rlc-abstract.md
22. scruggs-2011-cardiac-rlc-fulltext.txt
23. scruggs-2011-cardiac-rlc-summary.md
24. somlyo-2003-ca-sensitivity-abstract.md
25. somlyo-2003-ca-sensitivity-summary.md
26. stull-2011-skeletal-mlck-abstract.md
27. stull-2011-skeletal-mlck-fulltext.txt
28. stull-2011-skeletal-mlck-summary.md
29. uniprot-A0A9L0TJE1-entry.txt
30. uniprot-A0A9L0TJE1-summary.md
31. uniprot-Q62082-mouse-Myl10-entry.txt
32. uniprot-Q62082-mouse-Myl10-summary.md
33. uniprot-Q9BUA6-human-MYL10-entry.txt
34. uniprot-Q9BUA6-human-MYL10-summary.md
35. vicente-manzanares-2009-nmii-abstract.md
36. vicente-manzanares-2009-nmii-fulltext.txt
37. vicente-manzanares-2009-nmii-summary.md
38. wade-2009-horse-genome-abstract.md
39. wade-2009-horse-genome-summary.md
40. wu-1999-rlc-crosslinking-abstract.md
41. wu-1999-rlc-crosslinking-summary.md
42. xie-1994-scallop-regulatory-domain-abstract.md
43. xie-1994-scallop-regulatory-domain-summary.md