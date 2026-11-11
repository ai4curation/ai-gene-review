---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:15:06.191708'
end_time: '2026-10-26T00:23:48.057155'
duration_seconds: 521.87
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: NADK2
  gene_symbol: NADK2
  uniprot_accession: A0A9L0K2P4
  protein_description: 'RecName: Full=NAD kinase 2, mitochondrial {ECO:0000256|ARBA:ARBA00068714};
    EC=2.7.1.23 {ECO:0000256|ARBA:ARBA00012120}; AltName: Full=Mitochondrial NAD kinase
    {ECO:0000256|ARBA:ARBA00080688}; AltName: Full=NAD kinase domain-containing protein
    1, mitochondrial {ECO:0000256|ARBA:ARBA00077019};'
  gene_info: Name=NADK2 {ECO:0000313|Ensembl:ENSEASP00005059781.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the NAD kinase family.
  protein_domains: ATP-NAD_kinase_N. (IPR017438); NAD/diacylglycerol_kinase_sf. (IPR016064);
    NADK. (IPR002504); NAD_kinase (PF01513)
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
citation_count: 63
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0K2P4
- **Protein Description:** RecName: Full=NAD kinase 2, mitochondrial {ECO:0000256|ARBA:ARBA00068714}; EC=2.7.1.23 {ECO:0000256|ARBA:ARBA00012120}; AltName: Full=Mitochondrial NAD kinase {ECO:0000256|ARBA:ARBA00080688}; AltName: Full=NAD kinase domain-containing protein 1, mitochondrial {ECO:0000256|ARBA:ARBA00077019};
- **Gene Information:** Name=NADK2 {ECO:0000313|Ensembl:ENSEASP00005059781.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the NAD kinase family.
- **Key Domains:** ATP-NAD_kinase_N. (IPR017438); NAD/diacylglycerol_kinase_sf. (IPR016064); NADK. (IPR002504); NAD_kinase (PF01513)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NADK2" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NADK2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NADK2** (gene ID: NADK2, UniProt: A0A9L0K2P4) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# NADK2 (Mitochondrial NAD Kinase) in the Donkey, *Equus asinus* (UniProt A0A9L0K2P4): Function, Localization and Pathways

## 1. Introduction and Summary

UniProt entry A0A9L0K2P4 is an unreviewed, computationally annotated (protein existence level 3, "inferred from homology") 506-residue protein from the donkey, *Equus asinus*, encoded by the gene *NADK2* on donkey chromosome 10 and derived from the donkey reference genome assembly [uniprot-A0A9L0K2P4-entry]. Its name, EC number (2.7.1.23), reaction (NAD+ + ATP = ADP + NADP+ + H+), homodimeric subunit structure and mitochondrial location are all assigned by automatic rules rather than by experiments on the donkey protein [uniprot-A0A9L0K2P4-entry]. No published study has examined donkey NADK2 directly. As this report shows, though, the protein is unambiguously the donkey ortholog of human NADK2 (also called MNADK or C5orf33; UniProt Q4G0N4). The gene symbol is not ambiguous in mammals, and the literature on the mammalian enzyme can be carried over by orthology, with one caveat about this particular isoform, set out below.

Taken together, the mammalian literature shows that NADK2 is the only known NAD kinase in the mitochondrial matrix. It makes mitochondrial NADP+ de novo by phosphorylating the 2′-hydroxyl of NAD+ (and, at least in vitro, NADH), using ATP or inorganic polyphosphate as the phosphoryl donor [ohashi-2012-human-mitochondrial-nadk-abstract; zhang-2013-mnadk-liver-enriched-abstract; du-2022-nadk2-structure-atypical-assembly-abstract]. NADP(H) cannot cross the inner mitochondrial membrane, so each compartment needs its own NAD kinase, and NADK2 provides the matrix NADP(H) pool [zhang-2015-mnadk-long-awaited-abstract; zhang-2023-mito-nadk-review-abstract]. That pool supplies reducing equivalents to NADPH-dependent matrix enzymes. Through them it drives proline biosynthesis at the pyrroline-5-carboxylate synthase (P5CS) step, mitochondrial fatty-acid synthesis and protein lipoylation [kim-2025-mito-nadph-mtfas-lipoylation-abstract], lysine degradation, oxidation of polyunsaturated fatty acids by 2,4-dienoyl-CoA reductase (DECR1), and broader fatty-acid oxidation and redox homeostasis [tran-2021-mito-nadp-proline-abstract; zhu-2021-mito-nadph-proline-abstract; houten-2014-nadk2-decr-deficiency-abstract; zhang-2018-mnadk-hepatic-steatosis-abstract]. Structurally, animal NADK2 is unusual among NAD kinases: it is a constitutively active, non-cooperative homodimer, not a tetramer, because of an animal-specific dimerization insert [du-2022-nadk2-structure-atypical-assembly-abstract; mary-2022-nadk2-crystal-acetylation-abstract].

The key caveat for this accession is that A0A9L0K2P4 lacks a 32-residue segment. That segment matches residues 288–319 of human NADK2, which contain the conserved TGSxAW substrate-binding motif and the Trp-319 that stacks against the nicotinamide ring of NAD(P)+ (this analysis; [mary-2022-nadk2-crystal-acetylation-fulltext; du-2022-nadk2-structure-atypical-assembly-fulltext]). The same segment is absent from human isoform 2 [uniprot-Q4G0N4-human-entry.txt]. Other donkey NADK2 entries (A0A8C4M4D0, A0A8C4M5G3) keep it. So A0A9L0K2P4 probably represents an alternatively spliced or mispredicted transcript, and whether it is catalytically active is uncertain. The functional description in this report applies to the canonical donkey NADK2 gene product.

## 2. Identity Verification and Sequence Features of A0A9L0K2P4

The gene symbol, the protein name and the domain content of A0A9L0K2P4 all agree. The entry carries the Pfam NAD_kinase domain (PF01513), the InterPro ATP-NAD kinase N-terminal (IPR017438) and NADK (IPR002504) signatures, and the PANTHER subfamily PTHR13158:SF5 "NAD kinase 2, mitochondrial" [uniprot-A0A9L0K2P4-entry]. A global pairwise alignment (BLOSUM62) against human NADK2 (442 aa) found 396 identical positions. Once the donkey-specific N-terminal extension and the internal gap are set aside, the identity over the aligned region is about 97% (notes-alignment.txt). The catalytic and regulatory residues defined in human structural and mutational studies are conserved at their expected positions. In donkey numbering, these are: the catalytic aspartate of the GGDG motif (human D161 → donkey D257); the active-site Lys-76 (→ K172), which is regulated by acetylation; Ser-188 (→ S284), which is required for catalysis; His-191 (→ H287), which stacks the adenosine; the S-nitrosylated Cys-193 (→ C289); and the dimer-interface residues Val-331, Val-334, Arg-378 and Glu-379 (→ V395, V398, R442, E443) (notes-alignment.txt; [du-2022-nadk2-structure-atypical-assembly-fulltext; mary-2022-nadk2-crystal-acetylation-fulltext; kim-2022-mnadk-energy-demand-abstract]).

The donkey sequence differs from human NADK2 in two places. First, it has a roughly 96-residue N-terminal extension upstream of the methionine that matches human Met-1 (MTCYRGF…). This extension is predicted to be disordered [uniprot-A0A9L0K2P4-entry], and the horse NADK2 gene models share it (A0A3Q2GYY5, F7DCV0). It most likely reflects an upstream in-frame start codon chosen by the automated gene model. Notably, the human Met-1 start codon is the functionally relevant one: a homozygous p.Met1Val start-loss variant in the 442-residue primary human transcript causes NADK2 deficiency [pomerantz-2018-nadk2-start-loss-abstract]. Human NADK2 targets mitochondria through its N-terminal ~62 residues [ohashi-2012-human-mitochondrial-nadk-fulltext], and the donkey sequence keeps this targeting region intact downstream of the extension.

Second, A0A9L0K2P4 lacks the 32 residues corresponding to human 288–319 (ASYYEISVDDGPWEKQKSSGLNLCTGTGSKAW). Human isoform 2 (VSP_027193) lacks exactly the same segment [uniprot-Q4G0N4-human-entry.txt]. The horse entry A0A3Q2H586 has the same exon-skipped structure, while the donkey entries A0A8C4M4D0 (538 aa) and A0A8C4M5G3 (560 aa) contain the full TGTGSKAW motif (notes-alignment.txt). Ensembl gene-model data confirm the basis of this difference: donkey *NADK2* (ENSEASG00005014681, chromosome 10) has three protein-coding transcripts, and the one encoding A0A9L0K2P4 (ENSEAST00005075574, 11 exons) is non-canonical. Compared with the 12-exon, 538-residue transcript, it simply omits a single 96-bp exon (chr10:61,875,864–61,875,959) that encodes exactly the 32 missing residues [ensembl-ENSEASG00005014681-summary; ensembl-ENSEASG00005014681-gene.json]. A0A9L0K2P4 is therefore an exon-skipping splice model, not a sequencing artefact or a distinct gene. Ensembl does not record whether this junction is supported by donkey transcript data. The structural work makes this deletion significant. In the NADP+-bound crystal structure, the adenine of NADP+ is sandwiched between D161, A318 and N276; A318 belongs to the conserved NADK "TGSxAw" motif (human residues 314–319); Trp-319 stacks the nicotinamide moiety; and Ala-288 from the partner subunit helps hold the nicotinamide [mary-2022-nadk2-crystal-acetylation-fulltext]. The independent structure of Du and colleagues also identified W319 as the residue that π-stacks the nicotinamide group [du-2022-nadk2-structure-atypical-assembly-fulltext]. Among 65 animal and protist NADK2 homologues, Trp-319 is completely conserved [ohashi-2012-human-mitochondrial-nadk-fulltext]. Lys-304, which is regulated by acetylation and points into the partner subunit's NADP+ site, also falls inside the missing segment [mary-2022-nadk2-crystal-acetylation-fulltext]. A protein without this segment would therefore be expected to have a badly compromised NAD+-binding site. Consistent with this, a human patient homozygous for a splice variant that removes an exon at Trp-319 (c.956+6T>C; p.Trp319Cysfs*21) had NADK2 deficiency, although that variant also causes a frameshift and loss of mRNA [tort-2016-lysine-restriction-nadk2-patient-abstract]. The literature provides no direct activity data for the isoform-2-like product. Its function should therefore be treated as unknown, and A0A9L0K2P4 should not be assumed to share the catalytic activity of the canonical protein.

## 3. Enzymatic Function: Reaction, Substrate Specificity and Phosphoryl Donors

NAD kinase (EC 2.7.1.23) is the only known enzyme that synthesizes NADP+ de novo. It transfers a phosphoryl group from ATP or inorganic polyphosphate to the 2′-hydroxyl of the adenosine ribose of NAD+ [ohashi-2012-human-mitochondrial-nadk-fulltext; oka-2023-nadk-review-abstract]. Ohashi, Kawai and Murata first showed that human C5orf33 (now NADK2) has this activity. Recombinant protein lacking the targeting sequence phosphorylated NAD+ using ATP, other nucleoside triphosphates, or polyphosphates (metaphosphate, hexametaphosphate, tetrapolyphosphate), but not ADP, trimetaphosphate, phosphoenolpyruvate or phosphocreatine [ohashi-2012-human-mitochondrial-nadk-fulltext]. Its polyphosphate-dependent activity was comparable to its ATP-dependent activity, which is unusual for a eukaryotic NAD kinase [ohashi-2012-human-mitochondrial-nadk-fulltext]. The enzyme is specific to pyridine dinucleotides: it showed no detectable activity on nicotinic acid adenine dinucleotide, ADP-ribose, adenosine or AMP, and no sphingosine, diacylglycerol or 6-phosphofructokinase activity [ohashi-2012-human-mitochondrial-nadk-fulltext]. Zhang independently showed by mass spectrometry that recombinant MNADK produces NADP+ [zhang-2013-mnadk-liver-enriched-abstract].

The two studies disagree on how well NADK2 uses the reduced dinucleotide NADH. In the original coupled-enzyme assay, NADH kinase activity was about 10% of NAD+ kinase activity [ohashi-2012-human-mitochondrial-nadk-fulltext]. A later direct assay that followed radiolabelled NADP+ formation found that NADK2 uses NAD+ and NADH as roughly equivalent substrates, whereas cytosolic NADK prefers NAD+ [du-2022-nadk2-structure-atypical-assembly-fulltext]. Accordingly, recent reviews describe NADK2 as phosphorylating "NAD(H)" to produce mitochondrial NADP(H) [zhang-2023-mito-nadk-review-abstract; zhu-2021-mito-nadph-proline-abstract]. The kinetic constants are also disputed. Ohashi et al. reported a Km for NAD+ of 22 µM and a Km for ATP of 1.7 mM [ohashi-2012-human-mitochondrial-nadk-fulltext]. Du et al. confirmed a Km for ATP of 2.2 mM, but measured an apparent Km for NAD+ of about 30–60 mM, roughly 1,000-fold higher than the earlier indirect estimate and comparable to that of cytosolic NADK [du-2022-nadk2-structure-atypical-assembly-fulltext]. Product feedback also differs between the two human kinases. NADK2 was inhibited by NADH, NADPH and especially NADP+, whereas cytosolic NADK is not inhibited by NADP+ [ohashi-2012-human-mitochondrial-nadk-fulltext]. Mary et al. found that catalysis needs a dicationic metal (Mg2+, Ca2+ or Fe3+ were observed in crystals) and proceeds in a substrate-assisted manner [mary-2022-nadk2-crystal-acetylation-fulltext].

Mutagenesis has identified the catalytic residues. Changing the catalytic GGDG aspartate D161 to the isosteric asparagine (D161N) reduced activity to trace levels, and removing the diphosphate-contacting Lys-76 (K76A) reduced it about tenfold [du-2022-nadk2-structure-atypical-assembly-fulltext]. Ser-188 is essential: S188A, S188D and S188E all abolish activity in vitro [kawabata-2015-ser188-phosphomimetic-abstract], and S188A NADK2 cannot support proline synthesis in cells [mary-2022-nadk2-crystal-acetylation-fulltext]. All of these residues are conserved in donkey NADK2 (Section 2).

## 4. Structure and Quaternary Organization

Two crystal structures of human NADK2 were published in 2022, one with NAD+ and one with NADP+. They show the canonical NAD kinase fold, but a quaternary arrangement not seen in other NAD kinases [du-2022-nadk2-structure-atypical-assembly-abstract; mary-2022-nadk2-crystal-acetylation-abstract]. More than 70 NAD kinases from bacteria, the eukaryotic cytosol and yeast mitochondria have had their structures solved, and all of them assemble as tetramers (dimers of dimers). NADK2, by contrast, forms a stable homodimer in crystals, in solution (by SAXS, SEC-MALS, size-exclusion chromatography and mass photometry) and in cells (by chemical crosslinking) [du-2022-nadk2-structure-atypical-assembly-fulltext; mary-2022-nadk2-crystal-acetylation-fulltext]. The NADP+-binding site lies at the dimer interface, in a groove formed by the N- and C-terminal domains of one subunit and the C-terminal domain of the other, so each dimer has two composite active sites [mary-2022-nadk2-crystal-acetylation-fulltext; du-2022-nadk2-structure-atypical-assembly-fulltext].

The dimer is held together by a helical hairpin, residues ~325–365 in the human protein. Du and colleagues named it the EMKA element (for its conservation in mitochondrial kinases of animals). Its helices cross-pair with those of the partner subunit, nearly doubling the dimer interface and sterically blocking the surface that other NAD kinases use to tetramerize [du-2022-nadk2-structure-atypical-assembly-abstract; mary-2022-nadk2-crystal-acetylation-fulltext]. A sequence survey showed that the α8–α9 insert is only 3 residues long in bacterial, cytosolic and yeast mitochondrial NAD kinases, but 22–47 residues long in the mitochondrial NAD kinases of all animals examined [du-2022-nadk2-structure-atypical-assembly-fulltext]. Removing EMKA, or mutating its interface (V331Y, V331A+V334A+L335A, Δ325–365, or V334R/R378Q), produces monomers that are catalytically inactive in vitro and cannot support proline synthesis or proline-independent growth in NADK2-deficient cells [du-2022-nadk2-structure-atypical-assembly-fulltext; mary-2022-nadk2-crystal-acetylation-fulltext]. Two N-ethyl-N-nitrosourea (ENU)-induced mouse alleles in this region, S326L and S330P, cause severe neuromuscular disease, which underlines its importance in vivo [murray-2022-nadk2-mouse-models-abstract]. Dimerization also changes the enzyme's kinetic behaviour. Cytosolic NADK is activated cooperatively by self-association (Hill coefficient ~1.7), whereas NADK2 is non-cooperative (Hill coefficient ~1). NADK2 is thus a constitutively active dimer whose output is buffered against changes in protein concentration [du-2022-nadk2-structure-atypical-assembly-fulltext]. Donkey A0A9L0K2P4 keeps the entire EMKA segment (human 320–365), including V331, V334 and R378 (notes-alignment.txt), so the isoform-2-like deletion described above lies just N-terminal to the dimerization hairpin and would not by itself be expected to remove it.

## 5. Subcellular Localization: The Mitochondrial Matrix

Several independent lines of evidence place mammalian NADK2 in mitochondria. Full-length human C5orf33 fused to FLAG localized to mitochondria in HEK293A cells, whereas a variant lacking the N-terminal 62 residues did not. The same pattern held for expression in yeast, which shows that this N-terminal region is a functional mitochondrial targeting sequence [ohashi-2012-human-mitochondrial-nadk-fulltext]. Zhang independently showed mitochondrial localization of MNADK in HepG2 hepatoma cells by fluorescence imaging [zhang-2013-mnadk-liver-enriched-abstract]. Deleting the internal helical extensions does not change mitochondrial targeting [mary-2022-nadk2-crystal-acetylation-fulltext]. Functional assays on rapidly immunopurified mitochondria (MITO-Tag) combined with [13C3-15N]nicotinamide tracing show that NADK2 loss removes most newly synthesized mitochondrial NADP+ and NADPH, confirming that the enzyme acts in the matrix NADP(H) pool [tran-2021-mito-nadp-proline-fulltext; mary-2022-nadk2-crystal-acetylation-fulltext]. The donkey entry's Gene Ontology annotation to "mitochondrial matrix" (GO:0005759) rests on automatic rules [uniprot-A0A9L0K2P4-entry], but it agrees with this experimental evidence from human and mouse. Because NADP(H) does not cross the inner mitochondrial membrane, this compartment-specific enzyme is needed. Yeast and plants solve the same problem with separate, non-orthologous mitochondrial NAD kinases: Pos5 in yeast and NADK3 homologues in plants. Animals and some protists instead carry NADK2 homologues, while plants and fungi lack them [ohashi-2012-human-mitochondrial-nadk-abstract; zhang-2015-mnadk-long-awaited-abstract]. NADK2 mRNA is expressed widely and is more abundant than cytosolic NADK mRNA in almost all human tissues [ohashi-2012-human-mitochondrial-nadk-abstract]. In mice, expression is highest in liver, followed by brown fat, heart, muscle and kidney, all of which are rich in mitochondria [zhang-2013-mnadk-liver-enriched-abstract].

## 6. Metabolic Pathways Dependent on NADK2-Derived Mitochondrial NADP(H)

Most of NADK2's physiological role can be traced to a handful of NADPH-dependent enzymes in the matrix: P5CS, MECR, DECR1 and the lysine-degrading reductase. The clearest case is proline biosynthesis. Two independent 2021 studies showed that deleting NADK2 makes human cells proline auxotrophs [tran-2021-mito-nadp-proline-abstract; zhu-2021-mito-nadph-proline-abstract]. Tracing with [13C5]glutamine showed that NADK2 loss nearly abolishes conversion of glutamine to proline. The block lies at the NADPH-dependent reduction of glutamate to pyrroline-5-carboxylate by P5CS (ALDH18A1). Ornithine, which reaches P5C through ornithine aminotransferase and bypasses P5CS, restored proline synthesis and proliferation, showing that the downstream PYCR reductases do not depend strictly on NADK2 [tran-2021-mito-nadp-proline-fulltext]. Zhu and colleagues further found that NADK2 deletion did not measurably change mitochondrial folate-pathway activity, TCA-cycle activity or mitochondrial oxidative stress in their cell lines. They concluded that a primary function of the mitochondrial NADP(H) pool is to support proline synthesis for cytosolic protein synthesis, including collagen production by mesenchymal cells [zhu-2021-mito-nadph-proline-abstract]. In NADK2-deficient cells, proline then becomes limiting for both nucleotide and protein synthesis [tran-2021-mito-nadp-proline-abstract]. A patient with a hypomorphic NADK2 allele had plasma proline 2.5 times the upper limit of normal, consistent with altered proline metabolism in vivo [pomerantz-2018-nadk2-start-loss-abstract].

The second set of dependent pathways is lysine degradation and polyunsaturated fatty-acid oxidation, which are what reveal human NADK2 deficiency. Houten and colleagues found a causal NADK2 mutation in a patient with the syndrome previously called "2,4-dienoyl-CoA reductase deficiency with hyperlysinemia". They showed that the patient's fibroblasts had reduced mitochondrial NADP(H) and DECR activity, and that functional NADK2, but not other manipulations, rescued DECR [houten-2014-nadk2-decr-deficiency-abstract]. The first step of lysine degradation, catalysed by the NADPH-dependent lysine-ketoglutarate reductase activity, also relies on matrix NADPH, which explains the hyperlysinemia [houten-2014-nadk2-decr-deficiency-abstract]. The authors also proposed that NADPH stabilizes DECR in a chaperone-like way, beyond its role as cosubstrate [houten-2014-nadk2-decr-deficiency-abstract]. The same biochemical signature, raised lysine and C10:2 (decadienoyl)-carnitine, appears in later patients and in Nadk2 knockout and ENU mutant mice [tort-2016-lysine-restriction-nadk2-patient-abstract; zhang-2018-mnadk-hepatic-steatosis-abstract; murray-2022-nadk2-mouse-models-abstract].

A third, more recently defined pathway is mitochondrial fatty-acid synthesis (mtFAS) and the protein lipoylation that depends on it. Kim and colleagues found that NADK2 loss in several human cancer cell lines and in xenograft tumours lowered pyruvate oxidation and the activity of the pyruvate dehydrogenase (PDH) and 2-oxoglutarate dehydrogenase (OGDH) complexes. The cause was markedly reduced lipoylation of their E2 subunits, for example DLAT at Lys-132 and Lys-259 [kim-2025-mito-nadph-mtfas-lipoylation-abstract; kim-2025-mito-nadph-mtfas-lipoylation-fulltext]. Several controls pinned the defect on NADK2's catalytic product in the matrix. Lipoylation was not restored by antioxidants or proline, nor by a catalytically inactive D161A NADK2. It was restored by cytosolic NADK redirected to mitochondria with a targeting sequence. Depleting other matrix NADPH sources (NNT, IDH2 or GLUD1) did not impair lipoylation [kim-2025-mito-nadph-mtfas-lipoylation-fulltext]. The mtFAS enoyl reductase MECR binds NADPH with sub-micromolar affinity (Kd ≈ 0.96 µM), and a new mass-spectrometry assay showed that NADK2 deficiency depletes acyl-ACP species much as MECR deficiency does. NADK2 loss also impaired assembly of electron-transport-chain complexes, respiration and mitochondrial translation. In DepMap, NADK2 is coessential with MECR, MCAT, OXSM, LIPT1, LIPT2 and the P5CS gene ALDH18A1 [kim-2025-mito-nadph-mtfas-lipoylation-fulltext]. This pathway offers a mechanistic explanation for the reduced oxygen consumption first seen in NADK2-deficient patient fibroblasts [houten-2014-nadk2-decr-deficiency-abstract]. NADK2 should not be seen as the only route to matrix NADPH, however. In human gliomas, NADH-to-NADPH transhydrogenation by NNT supplies the mitochondrial NADPH used for proline accumulation and antioxidant defence, particularly under hypoxia [nnt-2026-proline-glioma-abstract]. The two fit together: NADK2 sets the size of the mitochondrial NADP(H) pool, while NNT and other dehydrogenases set its reduction state. How much each contributes probably varies with tissue and conditions.

The fourth area is mitochondrial redox balance and energy metabolism, which has been studied mainly in liver. Mnadk-knockout mice have defective fatty-acid oxidation during fasting, reduced activation of the transcription factors CREBH and PPARα, and lower activity of mitochondrial sirtuins. On an atherogenic high-fat diet they develop increased hepatic reactive oxygen species and features of non-alcoholic fatty liver disease [zhang-2018-mnadk-hepatic-steatosis-abstract]. Under increased energy demand (endurance exercise or fasting), knockout mice show lower fat oxidation and energy expenditure, lower mitochondrial NADP(H), higher ROS, and hyperacetylation of hepatic metabolic enzymes. This fits a link between NADK2, SIRT3 activity and fatty-acid oxidation [kim-2022-mnadk-energy-demand-abstract; zhang-2023-mito-nadk-review-abstract]. Other contexts implicate NADK2-dependent NADPH as well. In human neurons, tau oligomers upregulate NADK2 and de novo mitochondrial NADPH synthesis, which in turn controls expression of the tau receptor LRP1 [pardo-2026-nadk2-tau-uptake-abstract]. In yeasts, the analogous (non-orthologous) mitochondrial NAD kinase Pos5 is needed for coenzyme Q biosynthesis, which suggests that other matrix NADPH-consuming biosyntheses may also depend on mitochondrial NAD kinase activity [nishihara-2026-pos5-coq-abstract]. The importance of NADK2 for mitochondrial ROS defence is still debated, given the negative result of Zhu et al. in cultured cells [zhu-2021-mito-nadph-proline-abstract] and the positive results in stressed mouse liver [zhang-2018-mnadk-hepatic-steatosis-abstract].

## 7. Regulation of NADK2 Activity and Expression

Mammalian NADK2 is regulated by post-translational modifications at or near its active site and by nutritional state. Mapping by LC-MS/MS identified many acetylation, succinylation and phosphorylation sites. The acetylation-mimetic substitutions K76Q and K304Q abolished catalytic activity, lowered mitochondrial NADP(H) and proline synthesis, and prevented proline-independent growth, without disrupting the dimer [mary-2022-nadk2-crystal-acetylation-abstract]. In the structure, K76 from one subunit and K304 from the other point into the shared NADP+/ATP site. Neutralizing their charge by acetylation is therefore expected to occlude the site [mary-2022-nadk2-crystal-acetylation-fulltext]. Phosphomimetic substitutions at Ser-289 and Ser-376 reduce activity, and Ser-188 is essential, which raises the possibility of inhibitory phosphorylation at these sites [kawabata-2015-ser188-phosphomimetic-abstract]. However, Mary et al. did not detect S188 phosphorylation in HEK293E cells [mary-2022-nadk2-crystal-acetylation-fulltext]. A high-fat diet induces S-nitrosylation of MNADK at Cys-193 in mouse liver, and an S-nitrosylation-resistant C193S variant protects against diet-induced steatosis [kim-2022-mnadk-energy-demand-abstract]. Methotrexate inhibits MNADK activity in hepatocytes and liver [zhang-2018-mnadk-hepatic-steatosis-abstract]. At the expression level, fasting raises hepatic and adipose MNADK, obesity lowers it in fat, and it is suppressed in human liver tumours [zhang-2013-mnadk-liver-enriched-abstract]. Of the regulatory residues, K76, S188 and C193 are conserved in donkey A0A9L0K2P4 (as K172, S284 and C289). K304 and S289 (human numbering) fall in the region missing from this isoform, and S376 corresponds to donkey S440 (notes-alignment.txt).

## 8. Evolutionary Context and Inference for the Donkey Protein

The NAD kinase family is ancient and found in archaea, bacteria, plants and animals [oka-2023-nadk-review-abstract]. NADK2 belongs to a distinct lineage: phylogenetic analysis places NADK2 homologues from animals and protists in a clade separate from both plant NADK3 and the cytosolic NADK lineage [ohashi-2012-human-mitochondrial-nadk-fulltext]. Within animals, the EMKA dimerization insert is a synapomorphy of mitochondrial NAD kinases [du-2022-nadk2-structure-atypical-assembly-fulltext]. The donkey protein has the EMKA insert, the GGDG and NE/D motifs, the conserved active-site lysine and serine residues, and the region that (in the canonical sequence) carries the mitochondrial targeting signal (Section 2). Together with about 97% identity to the experimentally characterized human enzyme over the aligned region, this supports transferring the following annotations to the canonical donkey NADK2 gene product: NAD+ kinase activity (GO:0003951) with ATP or polyphosphate as donor, an NADP+ biosynthetic process (GO:0006741), location in the mitochondrial matrix (GO:0005759), and homodimerization. Roles in proline biosynthesis, mitochondrial fatty-acid synthesis and protein lipoylation, lysine catabolism and fatty-acid β-oxidation can be inferred indirectly, through the supply of mitochondrial NADPH. For the specific isoform A0A9L0K2P4, the missing TGSxAW/Trp-319 segment means that catalytic activity is a reasonable default prediction only at the gene level. Any experimental or curated annotation of this particular protein product should note that it is a probable splice isoform or gene-model variant whose activity has not been tested.

## Open Questions

Several questions remain. The most immediate for this accession is whether the exon-skipped transcript behind A0A9L0K2P4 (equivalent to human isoform 2, lacking residues 288–319) is expressed as protein in donkey tissues, and whether it has any NAD kinase activity. Losing the TGSxAW motif and Trp-319 predicts severe loss of function, but the protein could still form heterodimers with the full-length enzyme and act as a dominant-negative regulator. That could be tested by expressing recombinant protein and measuring NADP+ formation directly, by co-immunoprecipitation with canonical NADK2, and by checking donkey RNA-seq for junction reads. Similarly, whether the ~96-residue N-terminal extension in the donkey and horse gene models is real or an artefact of start-codon prediction could be settled with Ribo-seq or proteomics data from equids. If the extension were translated, its effect on mitochondrial import would need testing.

At the level of mammalian NADK2 in general, the Km for NAD+ (22 µM versus tens of mM) and the relative use of NAD+ versus NADH in vivo remain unresolved between assays. Settling them matters for modelling whether matrix NADP+ synthesis responds to the matrix NADH/NAD+ ratio. Also unknown is the physiological phosphoryl donor in the matrix, ATP or inorganic polyphosphate (which is produced and hydrolysed in mitochondria). How acetylation of K76/K304 is reversed, and whether SIRT3 or another sirtuin deacetylates NADK2 and so forms a feedback loop with NADPH-dependent sirtuin activity, has not been shown directly. The contribution of NADK2 to mitochondrial antioxidant capacity in vivo, relative to the nicotinamide nucleotide transhydrogenase (NNT) and the NADP+-dependent isocitrate dehydrogenase IDH2, still needs reconciling given the conflicting cell-culture and mouse-liver data. Whether the lipoylation and mtFAS defects seen in cultured cancer cells [kim-2025-mito-nadph-mtfas-lipoylation-abstract] also occur in NADK2-deficient patient tissues or mouse models, and contribute to their neurological phenotype, has not been tested. Finally, nothing is known about NADK2 in equine physiology. Equids have high muscular oxidative capacity and distinctive lipid metabolism, so it would be informative to ask whether NADK2 expression or variants relate to exercise-induced myopathies, hyperlipaemia in donkeys and ponies, or lysine and proline metabolism in equine collagen-rich tissues.

## References

- [uniprot-A0A9L0K2P4-entry] UniProt Consortium. UniProtKB entry A0A9L0K2P4 (A0A9L0K2P4_EQUAS), NAD kinase 2, mitochondrial, *Equus asinus*; entry version 15 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0K2P4.txt. Sequence derived from Wang C. et al. (2020) Donkey genomes provide new insights into domestication and selection for coat color. Nat Commun 11:6014, PMID:33293529.
- [uniprot-Q4G0N4-human-entry] UniProt Consortium. UniProtKB/Swiss-Prot entry Q4G0N4 (NADK2_HUMAN). https://rest.uniprot.org/uniprotkb/Q4G0N4.txt
- Additional sequence records used for comparison: UniProtKB A0A8C4M4D0 and A0A8C4M5G3 (donkey NADK2), A0A3Q2GYY5, A0A3Q2H586, F7DCV0 (horse NADK2), Q8C5H8 (mouse NADK2); https://rest.uniprot.org/
- [ensembl-ENSEASG00005014681] Ensembl. Gene ENSEASG00005014681 (NADK2, *Equus asinus*), transcripts ENSEAST00005023262, ENSEAST00005023265, ENSEAST00005075574. Retrieved via https://rest.ensembl.org/lookup/id/ENSEASG00005014681?expand=1
- [kim-2025-mito-nadph-mtfas-lipoylation] Kim D, Kesavan R, Ryu K, et al. (2025) Mitochondrial NADPH fuels mitochondrial fatty acid synthesis and lipoylation to power oxidative metabolism. Nat Cell Biol 27:790–800. PMID:40258949; PMCID:PMC12331256; DOI:10.1038/s41556-025-01655-4
- [nnt-2026-proline-glioma] Vettore LA, Boufersaoui A, Lyu Y, et al. (2026) Nicotinamide nucleotide transhydrogenase directly couples redox homeostasis to proline biosynthesis in human glioma. Mol Cell 86:4032–4042.e8. PMID:42628532; PMCID:PMC13650111; DOI:10.1016/j.molcel.2026.07.031
- [ohashi-2012-human-mitochondrial-nadk] Ohashi K, Kawai S, Murata K. (2012) Identification and characterization of a human mitochondrial NAD kinase. Nat Commun 3:1248. PMID:23212377; PMCID:PMC3535332; DOI:10.1038/ncomms2262
- [zhang-2013-mnadk-liver-enriched] Zhang R. (2013) MNADK, a novel liver-enriched mitochondrion-localized NAD kinase. Biol Open 2:432–438. PMID:23616928; PMCID:PMC3625872; DOI:10.1242/bio.20134259
- [houten-2014-nadk2-decr-deficiency] Houten SM, Denis S, Te Brinke H, et al. (2014) Mitochondrial NADP(H) deficiency due to a mutation in NADK2 causes dienoyl-CoA reductase deficiency with hyperlysinemia. Hum Mol Genet 23:5009–5016. PMID:24847004; DOI:10.1093/hmg/ddu218
- [zhang-2015-mnadk-long-awaited] Zhang R. (2015) MNADK, a long-awaited human mitochondrion-localized NAD kinase. J Cell Physiol 230:1697–1701. PMID:25641397; DOI:10.1002/jcp.24926
- [kawabata-2015-ser188-phosphomimetic] Kawabata Y, Murata K, Kawai S. (2015) Significance of Ser-188 in human mitochondrial NAD kinase as determined by phosphomimetic and phosphoresistant amino-acid substitutions. Biochem Biophys Res Commun 468:691–695. PMID:26577408; DOI:10.1016/j.bbrc.2015.11.017
- [tort-2016-lysine-restriction-nadk2-patient] Tort F, Ugarteburu O, Torres MA, et al. (2016) Lysine restriction and pyridoxal phosphate administration in a NADK2 patient. Pediatrics 138:e20154534. PMID:27940755; DOI:10.1542/peds.2015-4534
- [pomerantz-2018-nadk2-start-loss] Pomerantz DJ, Ferdinandusse S, Cogan J, et al. (2018) Clinical heterogeneity of mitochondrial NAD kinase deficiency caused by a NADK2 start loss variant. Am J Med Genet A 176:692–698. PMID:29388319; PMCID:PMC6185736; DOI:10.1002/ajmg.a.38602
- [zhang-2018-mnadk-hepatic-steatosis] Zhang K, Kim H, Fu Z, et al. (2018) Deficiency of the mitochondrial NAD kinase causes stress-induced hepatic steatosis in mice. Gastroenterology 154:224–237. PMID:28923496; PMCID:PMC5742027; DOI:10.1053/j.gastro.2017.09.010
- [tran-2021-mito-nadp-proline] Tran DH, Kesavan R, Rion H, et al. (2021) Mitochondrial NADP+ is essential for proline biosynthesis during cell growth. Nat Metab 3:571–585. PMID:33833463; PMCID:PMC9210447; DOI:10.1038/s42255-021-00374-y
- [zhu-2021-mito-nadph-proline] Zhu J, Schwörer S, Berisa M, et al. (2021) Mitochondrial NADP(H) generation is essential for proline biosynthesis. Science 372:968–972. PMID:33888598; PMCID:PMC8241437; DOI:10.1126/science.abd5491
- [du-2022-nadk2-structure-atypical-assembly] Du J, Estrella M, Solorio-Kirpichyan K, Jeffrey PD, Korennykh A. (2022) Structure of human NADK2 reveals atypical assembly and regulation of NAD kinases from animal mitochondria. Proc Natl Acad Sci USA 119:e2200923119. PMID:35733246; PMCID:PMC9245612; DOI:10.1073/pnas.2200923119
- [mary-2022-nadk2-crystal-acetylation] Mary C, Soflaee MH, Kesavan R, et al. (2022) Crystal structure of human NADK2 reveals a dimeric organization and active site occlusion by lysine acetylation. Mol Cell 82:3299–3311.e8. PMID:35868311; PMCID:PMC10353453; DOI:10.1016/j.molcel.2022.06.026
- [kim-2022-mnadk-energy-demand] Kim H, Fu Z, Yang Z, et al. (2022) The mitochondrial NAD kinase functions as a major metabolic regulator upon increased energy demand. Mol Metab 64:101562. PMID:35944895; PMCID:PMC9403569; DOI:10.1016/j.molmet.2022.101562
- [murray-2022-nadk2-mouse-models] Murray GC, Bais P, Hatton CL, et al. (2022) Mouse models of NADK2 deficiency analyzed for metabolic and gene expression changes to elucidate pathophysiology. Hum Mol Genet 31:4055–4074. PMID:35796562; PMCID:PMC9703942; DOI:10.1093/hmg/ddac151
- [zhang-2023-mito-nadk-review] Zhang R, Zhang K. (2023) Mitochondrial NAD kinase in health and disease. Redox Biol 60:102613. PMID:36689815; PMCID:PMC9873681; DOI:10.1016/j.redox.2023.102613
- [oka-2023-nadk-review] Oka SI, Titus AS, Zablocki D, Sadoshima J. (2023) Molecular properties and regulation of NAD+ kinase (NADK). Redox Biol 59:102561. PMID:36512915; PMCID:PMC9763689; DOI:10.1016/j.redox.2022.102561
- [pardo-2026-nadk2-tau-uptake] Pardo E, Kim T, Wallrabe H, et al. (2026) Mitochondrial NADK2-dependent NADPH controls tau oligomer uptake in human neurons. Alzheimers Dement 22:e71594. PMID:42304136; PMCID:PMC13272107; DOI:10.1002/alz.71594
- [nishihara-2026-pos5-coq] Nishihara S, Nishida I, Matsuo Y, Kaino T, Kawamukai M. (2026) Mitochondrial NAD kinase Pos5 is required for CoQ biosynthesis in yeasts. PLoS One 21:e0346295. PMID:41926382; PMCID:PMC13046142; DOI:10.1371/journal.pone.0346295


## Citations

1. du-2022-nadk2-structure-atypical-assembly-abstract.md
2. du-2022-nadk2-structure-atypical-assembly-fulltext.txt
3. du-2022-nadk2-structure-atypical-assembly-summary.md
4. ensembl-ENSEASG00005014681-gene.json
5. ensembl-ENSEASG00005014681-summary.md
6. houten-2014-nadk2-decr-deficiency-abstract.md
7. houten-2014-nadk2-decr-deficiency-summary.md
8. kawabata-2015-ser188-phosphomimetic-abstract.md
9. kawabata-2015-ser188-phosphomimetic-summary.md
10. kim-2022-mnadk-energy-demand-abstract.md
11. kim-2022-mnadk-energy-demand-fulltext.txt
12. kim-2022-mnadk-energy-demand-summary.md
13. kim-2025-mito-nadph-mtfas-lipoylation-abstract.md
14. kim-2025-mito-nadph-mtfas-lipoylation-fulltext.txt
15. kim-2025-mito-nadph-mtfas-lipoylation-summary.md
16. mary-2022-nadk2-crystal-acetylation-abstract.md
17. mary-2022-nadk2-crystal-acetylation-fulltext.txt
18. mary-2022-nadk2-crystal-acetylation-summary.md
19. murray-2022-nadk2-mouse-models-abstract.md
20. murray-2022-nadk2-mouse-models-summary.md
21. nishihara-2026-pos5-coq-abstract.md
22. nishihara-2026-pos5-coq-fulltext.txt
23. nishihara-2026-pos5-coq-summary.md
24. nnt-2026-proline-glioma-abstract.md
25. nnt-2026-proline-glioma-summary.md
26. ohashi-2012-human-mitochondrial-nadk-abstract.md
27. ohashi-2012-human-mitochondrial-nadk-fulltext.txt
28. ohashi-2012-human-mitochondrial-nadk-summary.md
29. oka-2023-nadk-review-abstract.md
30. oka-2023-nadk-review-fulltext.txt
31. oka-2023-nadk-review-summary.md
32. pardo-2026-nadk2-tau-uptake-abstract.md
33. pardo-2026-nadk2-tau-uptake-fulltext.txt
34. pardo-2026-nadk2-tau-uptake-summary.md
35. pomerantz-2018-nadk2-start-loss-abstract.md
36. pomerantz-2018-nadk2-start-loss-fulltext.txt
37. pomerantz-2018-nadk2-start-loss-summary.md
38. tort-2016-lysine-restriction-nadk2-patient-abstract.md
39. tort-2016-lysine-restriction-nadk2-patient-summary.md
40. tran-2021-mito-nadp-proline-abstract.md
41. tran-2021-mito-nadp-proline-fulltext.txt
42. tran-2021-mito-nadp-proline-summary.md
43. uniprot-A0A8C4M4D0-donkey-entry.fasta
44. uniprot-A0A8C4M5G3-donkey-entry.fasta
45. uniprot-A0A9L0K2P4-entry.fasta
46. uniprot-A0A9L0K2P4-entry.txt
47. uniprot-Q4G0N4-human-entry.fasta
48. uniprot-Q4G0N4-human-entry.txt
49. uniprot-Q8C5H8-mouse-entry.txt
50. zhang-2013-mnadk-liver-enriched-abstract.md
51. zhang-2013-mnadk-liver-enriched-fulltext.txt
52. zhang-2013-mnadk-liver-enriched-summary.md
53. zhang-2015-mnadk-long-awaited-abstract.md
54. zhang-2015-mnadk-long-awaited-summary.md
55. zhang-2018-mnadk-hepatic-steatosis-abstract.md
56. zhang-2018-mnadk-hepatic-steatosis-fulltext.txt
57. zhang-2018-mnadk-hepatic-steatosis-summary.md
58. zhang-2023-mito-nadk-review-abstract.md
59. zhang-2023-mito-nadk-review-fulltext.txt
60. zhang-2023-mito-nadk-review-summary.md
61. zhu-2021-mito-nadph-proline-abstract.md
62. zhu-2021-mito-nadph-proline-fulltext.txt
63. zhu-2021-mito-nadph-proline-summary.md