---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:36:41.309563'
end_time: '2026-10-25T23:48:17.749020'
duration_seconds: 696.44
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: FLCN
  gene_symbol: FLCN
  uniprot_accession: A0A8C4MM62
  protein_description: 'RecName: Full=Folliculin {ECO:0000256|ARBA:ARBA00021824};'
  gene_info: Name=FLCN {ECO:0000313|Ensembl:ENSEASP00005025924.2};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the folliculin family.
  protein_domains: FLCN/SMCR8_DENN. (IPR037521); FLCN_DENN_C_sf. (IPR044886); Folliculin.
    (IPR021713); Folliculin/SMCR8_longin. (IPR037520); Folliculin_DENN. (IPR032035)
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
citation_count: 79
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A8C4MM62
- **Protein Description:** RecName: Full=Folliculin {ECO:0000256|ARBA:ARBA00021824};
- **Gene Information:** Name=FLCN {ECO:0000313|Ensembl:ENSEASP00005025924.2};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the folliculin family.
- **Key Domains:** FLCN/SMCR8_DENN. (IPR037521); FLCN_DENN_C_sf. (IPR044886); Folliculin. (IPR021713); Folliculin/SMCR8_longin. (IPR037520); Folliculin_DENN. (IPR032035)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "FLCN" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'FLCN' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **FLCN** (gene ID: FLCN, UniProt: A0A8C4MM62) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Folliculin (FLCN) of the donkey, *Equus asinus* (UniProt A0A8C4MM62): a lysosomal RagC/D GTPase-activating protein that gates substrate-specific mTORC1 signalling

## Introduction and summary

UniProt entry A0A8C4MM62 is an unreviewed (TrEMBL) record for folliculin (gene symbol *FLCN*) from the donkey, *Equus asinus*. It is a 578-residue protein predicted from the chromosome-level Dezhou donkey reference genome (chromosome 13) and assigned to the folliculin family with folliculin longin and DENN domains [uniprot-A0A8C4MM62-entry][wang-2020-donkey-genomes-abstract]. There are no experimental studies of folliculin in donkeys or horses. A PubMed search combining "folliculin" with horse, equine or donkey returned no records, and the genome paper behind the sequence does not discuss *FLCN* [wang-2020-donkey-genomes-fulltext]. Everything said here about function therefore comes from orthology. That inference is unusually safe for this protein. The donkey sequence is 94.5% identical to human FLCN (Q8NFG4) over its full length (547 identical positions out of 579 human residues, in a global BLOSUM62 alignment run for this report; see `notes_alignment.txt`). The catalytic arginine finger, Arg164 in the motif LARGFQRW, sits at the same position in both proteins [shen-2019-flcn-fnip2-rag-ragulator-fulltext][lawrence-2019-lfc-structure-fulltext]. The gene symbol is unambiguous: "FLCN" names folliculin, the product of the Birt-Hogg-Dubé (BHD) syndrome gene [nickerson-2002-bhd-gene-abstract], and the UniProt description, family and domain annotations all match that identification.

The main finding of the literature is that folliculin works with a partner, FNIP1 or FNIP2, as a GTPase-activating protein (GAP) for the Rag GTPases RagC and RagD. It does not act on RagA or RagB [tsun-2013-flcn-ragcd-gap-abstract]. By converting RagC/D from the GTP-bound to the GDP-bound state, FLCN–FNIP sets the Rag heterodimer in its active configuration when amino acids are available. The work happens at the cytoplasmic face of the lysosome, where the Rags are anchored by Ragulator [petit-2013-flcn-lysosome-rag-abstract][meng-2018-gator1-flcn-abstract]. Structural studies show that FLCN–FNIP2 adopts two conformations. In amino-acid starvation it forms an inactive, RagA-GDP-bound "lysosomal folliculin complex" (LFC) that serves as a checkpoint [lawrence-2019-lfc-structure-abstract][shen-2019-flcn-fnip2-rag-ragulator-abstract]. When nutrients return it switches to an active complex that places Arg164 in the RagC nucleotide pocket [jansen-2022-flcn-gap-structure-abstract]. The main physiological output is not general mTORC1 activity. It is the mTORC1 phosphorylation of the MiT/TFE transcription factors TFEB and TFE3, which bind active (GDP-loaded) RagC/D directly. Because of this, loss of FLCN drives TFEB/TFE3 into the nucleus and activates lysosomal and autophagy gene programmes, while S6K and 4E-BP1 phosphorylation is largely unaffected [napolitano-2020-substrate-specific-mtorc1-abstract][wada-2016-flcn-adipose-browning-abstract]. Other reported activities are less central: Rab35 GEF activity, lysosome positioning through Rab34–RILP, roles in autophagy, links to AMPK, a ciliary pool, Hsp90-dependent stabilization by the FNIP co-chaperones, and proposed inhibition of lactate dehydrogenase A. These are reviewed below as secondary or context-dependent functions [schmidt-2018-flcn-review-abstract].

## Identity, domain architecture and evolutionary conservation

The donkey protein carries the domain signatures of the folliculin family. InterPro lists the folliculin family (IPR021713), the FLCN/SMCR8 longin domain (IPR037520), the FLCN/SMCR8 DENN domain (IPR037521) and the folliculin C-terminal DENN superfamily (IPR044886). Pfam lists PF11704 (Folliculin) and PF16692 (Folliculin_C). PROSITE predicts a "UDENN FLCN/SMCR8-type" domain spanning residues 86–557 [uniprot-A0A8C4MM62-entry]. MobiDB-lite predicts disordered regions at residues 31–82 and 294–332, the second of which is acidic [uniprot-A0A8C4MM62-entry]. This layout matches the structural description of human FLCN and FNIP1/2 as "DENN module proteins composed of an N-terminal longin and a C-terminal DENN … domain" [lawrence-2019-lfc-structure-fulltext]. The DENN relationship was first seen in the crystal structure of the FLCN C-terminal domain. That structure is distantly related to DENN-family Rab guanine nucleotide exchange factors (GEFs) such as DENND1B, a resemblance that was not visible from sequence alone [nookala-2012-flcn-denn-structure-abstract][schmidt-2018-flcn-review-abstract].

*FLCN* was found by positional cloning of the BHD locus on human 17p11.2. Its transcript is expressed widely, including in kidney, lung and skin, and when it was cloned it was noted to encode a protein "highly conserved across species" [nickerson-2002-bhd-gene-abstract]. The conservation extends to fungi. In budding yeast, Lst7 (the FLCN orthologue) and Lst4 (the FNIP orthologue) form a complex that acts as a GAP for Gtr2, the yeast RagC/D. The complex gathers at the vacuolar membrane when amino acids are scarce and acts on Gtr2 when amino acids such as glutamine are added back [peli-gulli-2015-lst4-lst7-gap-abstract]. Of the arginines in the β4–β5 loops of the FLCN and FNIP2 longin domains, "only Arg164 of FLCN is highly conserved from yeast to human" [lawrence-2019-lfc-structure-fulltext]. The donkey protein keeps this residue. The near-identity of donkey and human FLCN, the conserved catalytic residue, and the conservation of the core mechanism from yeast to mammals together support the inference that donkey FLCN is a functional RagC/D GAP. Of the 32 positions that differ between donkey and human FLCN, six lie in the N-terminal disordered segment (residues 31–82) and 13 lie in or next to the acidic disordered loop (donkey residues 294–346, including a one-residue deletion). Most of the remaining changes are conservative substitutions. The ULK1-induced phosphorylation sites of human FLCN, Ser406, Ser537 and Ser542 [dunlop-2014-flcn-gabarap-ulk1-abstract], are conserved as donkey Ser405, Ser536 and Ser541 (alignment in `notes_alignment.txt`).

## Partners and quaternary structure: the FLCN–FNIP heterodimer

FLCN does not function alone. Its first identified partner, FNIP1, was found by its interaction with FLCN and was also shown to bind AMP-activated protein kinase (AMPK) [baba-2006-fnip1-ampk-abstract]. Two groups then independently identified a paralogue, FNIP2 (also called FnipL). FNIP2 binds the FLCN C-terminus, and BHD-like C-terminal truncations of FLCN cannot bind it [hasumi-2008-fnip2-abstract][takagi-2008-fnipl-abstract]. Binding to FNIP2 changes where FLCN sits in the cell. Overexpressed FLCN alone is mostly nuclear, but with FNIP2 it is retained in the cytoplasm in a reticular pattern [takagi-2008-fnipl-abstract]. The UniProt annotation for the donkey protein, transferred by automatic rules from mammalian orthologues, summarizes these relationships. It describes FLCN as interacting via its C-terminus with FNIP1 or FNIP2 and as a component of the lysosomal folliculin complex with FNIP1/2, GDP-bound RagA/B, GTP-bound RagC/D and Ragulator [uniprot-A0A8C4MM62-entry].

The FNIPs also seem to keep FLCN stable. FLCN is a client of the molecular chaperone Hsp90, and FNIP1 and FNIP2 act as Hsp90 co-chaperones. They slow the Hsp90 ATPase cycle and compete with the activating co-chaperone Aha1, which promotes FLCN binding to Hsp90 and keeps FLCN stable [woodford-2016-fnip-hsp90-abstract]. Silencing either FNIP caused a modest decrease in Hsp90 client levels, FLCN among them [woodford-2016-fnip-hsp90-fulltext]. This may explain why the donkey UniProt record carries a long list of chaperone-system interactors (HSP90AA1, HSP70, STUB1, CDC37, AHSA1, STIP1, PTGES3, PPP5C) transferred from human data [uniprot-A0A8C4MM62-entry]. These interactions most likely reflect how FLCN–FNIP is folded and maintained, not its signalling output.

Cryo-EM shows how the heterodimer is built. FLCN–FNIP2 adopts "an extended conformation with two pairs of heterodimerized domains": the longin domains of FLCN and FNIP2 pair with each other and contact both nucleotide-binding domains of the Rag heterodimer, and the two DENN domains pair at the far end of the complex [shen-2019-flcn-fnip2-rag-ragulator-abstract]. The longin–longin heterodimer resembles the NPRL2–NPRL3 longin pair of GATOR1, the GAP for RagA/B. It is also "the only FLCN:FNIP2 element to directly interact with the Rag GTPases via their G domains" [lawrence-2019-lfc-structure-fulltext]. Lawrence and colleagues describe FLCN–FNIP2 as "the mirror image of the GATOR1 complex," since both are dual-longin GAPs with positive and negative regulatory roles, each acting on a different subunit of the Rag dimer [lawrence-2019-lfc-structure-fulltext].

## Biochemical function: a GTPase-activating protein selective for RagC/D

Folliculin's molecular function was defined by Tsun and colleagues. They showed that RagC/D must be GDP-bound for the Rag heterodimer to bind mTORC1, and they identified "FLCN and its binding partners, FNIP1/2, as Rag-interacting proteins with GAP activity for RagC/D, but not RagA/B" [tsun-2013-flcn-ragcd-gap-abstract]. The reaction is GTP hydrolysis on RagC or RagD, turning RagC/D-GTP into RagC/D-GDP and Pi. FLCN accelerates this reaction but does not consume GTP itself. It has no other known substrate among the Rags, and the yeast Lst4–Lst7 complex shows the same specificity for Gtr2 [peli-gulli-2015-lst4-lst7-gap-abstract]. FLCN therefore works with GATOR1 to produce the active Rag configuration, RagA/B-GTP with RagC/D-GDP: GATOR1 controls the RagA/B side and FLCN–FNIP controls the RagC/D side [meng-2018-gator1-flcn-abstract].

Catalysis uses a classic arginine finger. Biochemical work identified "a conserved arginine on FLCN as the catalytic arginine finger" [shen-2019-flcn-fnip2-rag-ragulator-abstract]. The FLCN R164A mutant assembles normally into the lysosomal complex but loses RagC-GAP activity. Lawrence and colleagues concluded that these data "establish FLCNR164 as a catalytically required arginine for canonical FLCN RagC-GAP activity" [lawrence-2019-lfc-structure-fulltext]. In the active-state structure, Arg164 enters the RagC nucleotide-binding domain next to the BeF₃⁻ transition-state analogue, in a geometry like that of arginine fingers in Rab GAP structures [jansen-2022-flcn-gap-structure-fulltext]. The donkey protein has Arg164 in the conserved LARGFQRW context, so it should have the same catalytic mechanism.

Earlier biochemistry assigned FLCN a different activity: GEF activity toward Rab35, consistent with the DENN fold of its C-terminus [nookala-2012-flcn-denn-structure-abstract]. Cell-based work in MDCK II cells later placed FLCN in an FLCN–Rab35–OCRL axis that controls podocalyxin trafficking in two-dimensional culture [kinoshita-2020-flcn-rab35-abstract]. In a separate study, the FLCN DENN domain did not act as a GEF for Rab34. Instead it bound the Rab34 effector RILP directly and loaded active Rab34 onto it [starling-2016-flcn-rab34-rilp-abstract]. These Rab-related activities are less well supported by structural and reconstitution evidence than the RagC/D GAP activity. They are best treated as additional or context-specific functions of the DENN module.

## Subcellular localization and the nutrient-dependent conformational cycle

The main site of FLCN action is the cytoplasmic surface of the lysosome. Petit and colleagues showed that FLCN is "selectively recruited to the surface of lysosomes after amino acid depletion," where it binds RagA directly through its GTPase domain. FNIP1 promotes both the lysosomal recruitment and the Rag binding [petit-2013-flcn-lysosome-rag-abstract]. The recruitment is controlled by the nucleotide state of RagA/B and requires GATOR1. This places FLCN downstream of the amino-acid sensors that act on GATOR1 [meng-2018-gator1-flcn-abstract]. In yeast, Lst4–Lst7 similarly gathers at the vacuolar membrane during starvation and disperses after amino acids are added back [peli-gulli-2015-lst4-lst7-gap-abstract]. Under nutrient-replete conditions, FLCN is largely cytosolic [lawrence-2019-lfc-structure-abstract].

Structures explain why FLCN collects on lysosomes when its GAP output is not needed. The 3.6 Å structure of the lysosomal folliculin complex (FLCN, FNIP2, RagA-GDP:RagC-GTP and Ragulator, as in the starved state) showed that "the RagC-GAP activity of FLCN was inhibited within the LFC, owing to displacement of a catalytically required arginine in FLCN from the RagC nucleotide" [lawrence-2019-lfc-structure-abstract]. In this complex, Arg164 lies more than 20 Å from either nucleotide [lawrence-2019-lfc-structure-fulltext]. The LFC thus acts as a checkpoint. FLCN is held on RagA-GDP in an inactive, pre-loaded state, and when the LFC disassembles, GAP activity is released and mTORC1 can regulate TFE3 [lawrence-2019-lfc-structure-abstract]. A later structure of the active FLCN complex (FNIP2, the N-terminal tail of the arginine sensor SLC38A9, RagA-GDP:RagC-GDP·BeFx and Ragulator) showed that FLCN "reorients by 90°, breaks contact with RagA, and makes previously unseen contacts with RagC that position its Arg164 finger for catalysis" [jansen-2022-flcn-gap-structure-abstract]. Shen and colleagues interpreted their own FLCN–FNIP2–Rag–Ragulator structure as an on-pathway intermediate [shen-2019-flcn-fnip2-rag-ragulator-abstract]. Taken together, these structures describe a cycle. Amino-acid starvation lets GATOR1 load RagA with GDP, and RagA-GDP captures FLCN–FNIP in the inactive LFC. When amino acids return, sensor input (including SLC38A9) moves the complex to the active conformation, RagC GTP is hydrolysed, and FLCN is released into the cytosol.

UniProt also lists cilium, centrosome, spindle, cytosol and nucleus as locations for the donkey protein, transferred by automatic annotation [uniprot-A0A8C4MM62-entry]. The ciliary pool has experimental support in mammalian cells. FLCN is a primary-cilium protein that, under flow stress, recruits LKB1 to activate basal-body AMPK and downregulate mTORC1 [zhong-2016-flcn-cilia-abstract]. Its entry into the cilium requires binding to kinesin-2 through a central loop, and point mutants that cannot bind kinesin-2 lose tumour-suppressor activity in cell assays [zhang-2021-flcn-cilia-kinesin2-abstract]. The nuclear signal seen when FLCN is overexpressed without FNIP partners [takagi-2008-fnipl-abstract] probably reflects the localization of free FLCN rather than a defined nuclear function.

## Pathway context: a dedicated RagC/D branch of mTORC1 that controls TFEB and TFE3

The main downstream consequence of FLCN GAP activity is control of the MiT/TFE transcription factors. In nutrient-replete cells, TFE3 and TFEB are recruited to lysosomes through active Rag GTPases and phosphorylated by mTORC1. They are then held in the cytosol by 14-3-3 proteins. Upon starvation they move to the nucleus and activate CLEAR-element genes for lysosomal biogenesis and autophagy [martina-2014-tfe3-autophagy-abstract]. Two early findings linked FLCN to this system. FLCN inactivation was found to increase nuclear TFE3 and TFE3 transcriptional activity, with lower TFE3 phosphorylation, in renal cells and kidney tumours [hong-2010-flcn-tfe3-abstract]. FLCN was also shown to be required for mTORC1-dependent phosphorylation and cytoplasmic retention of TFEB [petit-2013-flcn-lysosome-rag-abstract].

Napolitano and colleagues explained why this branch depends so heavily on FLCN. Classic mTORC1 substrates such as S6K and 4E-BP1 are recruited to mTORC1 through Raptor-binding TOS motifs. TFEB has no TOS motif. It is instead brought to mTORC1 by binding directly to active, GDP-bound RagC/D. As a result, TFEB phosphorylation "is strictly dependent on the amino-acid-mediated activation of RagC and RagD GTPases, but is insensitive to RHEB activity induced by growth factors" [napolitano-2020-substrate-specific-mtorc1-abstract]. In RagC-knockout cells, only the active RagC mutant (S75L) restored TFEB phosphorylation and TFEB binding. The GTP-locked mutant (Q120L) still supported S6K/4E-BP1 phosphorylation and mTORC1 lysosomal localization [napolitano-2020-substrate-specific-mtorc1-fulltext]. Adding a TOS motif to a Rag-binding-deficient TFEB restored its phosphorylation [napolitano-2020-substrate-specific-mtorc1-fulltext]. FLCN, as the RagC/D activator, therefore controls a substrate-specific arm of mTORC1. Structural mutants make the same point. Disrupting the active-complex-specific contacts of FLCN and FNIP2 with RagC abolished GAP activity and kept TFE3 in the nucleus, "with no effect on mTORC1 substrates S6K or 4E-BP1" [jansen-2022-flcn-gap-structure-abstract]. The GAP-dead R164A mutant likewise failed to restore cytoplasmic TFE3 [lawrence-2019-lfc-structure-fulltext]. In adipose tissue, the same FLCN–mTOR–TFE3 branch controls PGC-1α/β expression, mitochondrial biogenesis and browning. It is sensitive to amino acids, driven by RagC/D, independent of TSC and growth-factor signalling, and separable from S6K [wada-2016-flcn-adipose-browning-abstract].

Other pathway links have been reported but are less direct. FNIP1 and FNIP2 bind AMPK, and FLCN phosphorylation responds to AMPK inhibitors, rapamycin and amino-acid starvation [baba-2006-fnip1-ampk-abstract][hasumi-2008-fnip2-abstract]. These results tie the complex to energy sensing, but the mechanistic meaning of the AMPK interaction is still unclear. FLCN loss moderately impairs basal autophagic flux. ULK1 promotes FLCN phosphorylation at Ser406, Ser537 and Ser542, and FLCN binds GABARAP in a FNIP-dependent way [dunlop-2014-flcn-gabarap-ulk1-abstract]. Some of these autophagy effects may be indirect consequences of MiT/TFE regulation. FLCN also controls where lysosomes sit in the cell: on nutrient withdrawal it promotes perinuclear clustering by bridging Rab34 and RILP [starling-2016-flcn-rab34-rilp-abstract][dodding-2017-flcn-review-abstract]. This ties its starvation-induced lysosomal localization to organelle transport. A separate, Rag-independent metabolic activity has also been proposed. FLCN binds lactate dehydrogenase A (LDHA) and acts as an uncompetitive inhibitor of it, and it inhibits the dimeric but not the tetrameric enzyme [woodford-2021-flcn-ldha-abstract][woodford-2021-flcn-ldha-fulltext]. The LDHA-binding residues map to an intrinsically disordered loop, FLCN residues 216–248, and a decapeptide from this loop (residues 219–228) inhibits LDHA by itself [woodford-2021-flcn-ldha-fulltext]. This loop is identical in donkey and human FLCN (`notes_alignment.txt`), so the interaction could in principle be conserved. However, the finding comes from one group and has not been reconciled with the structural model of FLCN as a Rag GAP. For now it should be treated as a candidate secondary function.

## Physiological and pathological significance

In humans, germline loss-of-function *FLCN* mutations cause Birt-Hogg-Dubé syndrome: hair-follicle hamartomas (fibrofolliculomas), lung cysts with spontaneous pneumothorax, and renal tumours [nickerson-2002-bhd-gene-abstract][schmidt-2018-flcn-review-abstract]. Most pathogenic mutations truncate the C-terminus [nookala-2012-flcn-denn-structure-abstract], which removes the DENN domain and FNIP binding [hasumi-2008-fnip2-abstract]. In mice, complete *Flcn* loss is lethal at E5.5–6.5. Heterozygous mice develop kidney cysts and tumours with loss of heterozygosity [hasumi-2009-bhd-knockout-abstract]. Mouse genetics confirm that the TFEB branch drives disease. In a kidney-specific *Flcn* model, constitutively active TFEB caused the cysts, the apparent mTORC1 hyperactivity and the lethality, and depleting TFEB fully rescued them [napolitano-2020-substrate-specific-mtorc1-abstract]. The model that best fits the evidence is that FLCN suppresses tumours by keeping MiT/TFE factors out of the nucleus through RagC/D-dependent mTORC1 phosphorylation. The tumour-suppressor role is also seen in mammals other than humans and mice, which strengthens the case for extending it to equids. In German Shepherd dogs, hereditary multifocal renal cystadenocarcinoma and nodular dermatofibrosis (RCND) is a naturally occurring syndrome that resembles BHD. It maps to the canine *BHD* (*FLCN*) locus and is associated with an exon 7 missense mutation that changes a highly conserved amino acid. There is also evidence that the mutation is lethal in the homozygous state [lingaas-2003-canine-bhd-abstract]. In the Nihon rat, a germline single-nucleotide insertion in *Bhd* causes dominantly inherited renal carcinoma and embryonic lethality in homozygotes. Both phenotypes are rescued by a wild-type *Bhd* transgene [togashi-2006-nihon-rat-rescue-abstract]. No *FLCN*-associated disease has been reported in equids. Given the conservation described above, and the matching phenotypes in dogs, rats, mice and humans, the same dependence would be expected in donkeys.

## Open Questions

Several questions remain for the donkey protein and for folliculin in general. For *Equus asinus*, the sequence comes from an automated gene model with protein-level existence inferred from homology (PE=3), and UniProt lists ten RefSeq transcript models [uniprot-A0A8C4MM62-entry]. It would be useful to confirm the dominant isoform with equine RNA-seq or proteomics, and to check whether the residues that differ from human FLCN, which cluster in the two disordered segments (including the donkey-specific changes around residues 309–346), affect regulatory modification or partner binding. A direct test would be to measure the RagC-GAP activity of recombinant donkey FLCN–FNIP2, or to rescue TFE3 cytoplasmic retention in FLCN-null cells. Equine veterinary genetics might also look for BHD-like phenotypes in horses and donkeys: renal oncocytic tumours, lung cysts, follicular hamartomas, or the renal cystadenocarcinoma with nodular dermatofibrosis seen in dogs [lingaas-2003-canine-bhd-abstract].

For folliculin biology more broadly, the most important open problem is the exact signal that switches FLCN–FNIP2 from the inactive LFC to the active complex. SLC38A9 takes part in the active structure [jansen-2022-flcn-gap-structure-abstract], but the contributions of other amino-acid sensors, and the coupling to GATOR1 [meng-2018-gator1-flcn-abstract], need quantitative definition. The roles of the AMPK interaction [baba-2006-fnip1-ampk-abstract], the ULK1 phosphorylation sites [dunlop-2014-flcn-gabarap-ulk1-abstract], the DENN-mediated Rab35 GEF and Rab34–RILP activities [nookala-2012-flcn-denn-structure-abstract][starling-2016-flcn-rab34-rilp-abstract], and ciliary signalling [zhong-2016-flcn-cilia-abstract] are still unresolved. Each of these needs separation-of-function mutants that leave RagC-GAP activity intact. It is also not known whether FNIP1 and FNIP2 give the GAP complex tissue-specific properties [hasumi-2008-fnip2-abstract]. It is also unclear whether FLCN's proposed inhibition of LDHA [woodford-2021-flcn-ldha-abstract] can coexist with its Rag-bound states, because the LDHA-binding loop would have to be free of the Rag interface. Finally, the active-complex structure suggests a route to small molecules that selectively block MiT/TFE phosphorylation [jansen-2022-flcn-gap-structure-abstract], and their pharmacology remains to be explored.

## References

* **[uniprot-A0A8C4MM62-entry]** UniProtKB/TrEMBL entry A0A8C4MM62_EQUAS, Folliculin, *Equus asinus* (entry version 15, 02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A8C4MM62.txt. Local copies: `citations/uniprot-A0A8C4MM62-entry.txt` and `citations/uniprot-A0A8C4MM62.fasta`. Human comparator UniProt Q8NFG4: https://rest.uniprot.org/uniprotkb/Q8NFG4.fasta (`citations/uniprot-Q8NFG4-human-FLCN.fasta`).
* **[wang-2020-donkey-genomes]** Wang C, Li H, Guo Y, et al. Donkey genomes provide new insights into domestication and selection for coat color. *Nature communications* 2020;11:6014. PMID: 33293529 (https://pubmed.ncbi.nlm.nih.gov/33293529/); DOI: 10.1038/s41467-020-19813-7 (https://doi.org/10.1038/s41467-020-19813-7); PMCID: PMC7723042.
* **[nickerson-2002-bhd-gene]** Nickerson ML, Warren MB, Toro JR, et al. Mutations in a novel gene lead to kidney tumors, lung wall defects, and benign tumors of the hair follicle in patients with the Birt-Hogg-Dubé syndrome. *Cancer cell* 2002;2:157-64. PMID: 12204536 (https://pubmed.ncbi.nlm.nih.gov/12204536/); DOI: 10.1016/s1535-6108(02)00104-6 (https://doi.org/10.1016/s1535-6108(02)00104-6).
* **[baba-2006-fnip1-ampk]** Baba M, Hong SB, Sharma N, et al. Folliculin encoded by the BHD gene interacts with a binding protein, FNIP1, and AMPK, and is involved in AMPK and mTOR signaling. *Proceedings of the National Academy of Sciences of the United States of America* 2006;103:15552-7. PMID: 17028174 (https://pubmed.ncbi.nlm.nih.gov/17028174/); DOI: 10.1073/pnas.0603781103 (https://doi.org/10.1073/pnas.0603781103); PMCID: PMC1592464.
* **[hasumi-2008-fnip2]** Hasumi H, Baba M, Hong SB, et al. Identification and characterization of a novel folliculin-interacting protein FNIP2. *Gene* 2008;415:60-7. PMID: 18403135 (https://pubmed.ncbi.nlm.nih.gov/18403135/); DOI: 10.1016/j.gene.2008.02.022 (https://doi.org/10.1016/j.gene.2008.02.022); PMCID: PMC2727720.
* **[takagi-2008-fnipl]** Takagi Y, Kobayashi T, Shiono M, et al. Interaction of folliculin (Birt-Hogg-Dubé gene product) with a novel Fnip1-like (FnipL/Fnip2) protein. *Oncogene* 2008;27:5339-47. PMID: 18663353 (https://pubmed.ncbi.nlm.nih.gov/18663353/); DOI: 10.1038/onc.2008.261 (https://doi.org/10.1038/onc.2008.261).
* **[hasumi-2009-bhd-knockout]** Hasumi Y, Baba M, Ajima R, et al. Homozygous loss of BHD causes early embryonic lethality and kidney tumor development with activation of mTORC1 and mTORC2. *Proceedings of the National Academy of Sciences of the United States of America* 2009;106:18722-7. PMID: 19850877 (https://pubmed.ncbi.nlm.nih.gov/19850877/); DOI: 10.1073/pnas.0908853106 (https://doi.org/10.1073/pnas.0908853106); PMCID: PMC2765925.
* **[hong-2010-flcn-tfe3]** Hong SB, Oh H, Valera VA, et al. Inactivation of the FLCN tumor suppressor gene induces TFE3 transcriptional activity by increasing its nuclear localization. *PloS one* 2010;5:e15793. PMID: 21209915 (https://pubmed.ncbi.nlm.nih.gov/21209915/); DOI: 10.1371/journal.pone.0015793 (https://doi.org/10.1371/journal.pone.0015793); PMCID: PMC3012117.
* **[nookala-2012-flcn-denn-structure]** Nookala RK, Langemeyer L, Pacitto A, et al. Crystal structure of folliculin reveals a hidDENN function in genetically inherited renal cancer. *Open biology* 2012;2:120071. PMID: 22977732 (https://pubmed.ncbi.nlm.nih.gov/22977732/); DOI: 10.1098/rsob.120071 (https://doi.org/10.1098/rsob.120071); PMCID: PMC3438538.
* **[petit-2013-flcn-lysosome-rag]** Petit CS, Roczniak-Ferguson A, Ferguson SM. Recruitment of folliculin to lysosomes supports the amino acid-dependent activation of Rag GTPases. *The Journal of cell biology* 2013;202:1107-22. PMID: 24081491 (https://pubmed.ncbi.nlm.nih.gov/24081491/); DOI: 10.1083/jcb.201307084 (https://doi.org/10.1083/jcb.201307084); PMCID: PMC3787382.
* **[tsun-2013-flcn-ragcd-gap]** Tsun ZY, Bar-Peled L, Chantranupong L, et al. The folliculin tumor suppressor is a GAP for the RagC/D GTPases that signal amino acid levels to mTORC1. *Molecular cell* 2013;52:495-505. PMID: 24095279 (https://pubmed.ncbi.nlm.nih.gov/24095279/); DOI: 10.1016/j.molcel.2013.09.016 (https://doi.org/10.1016/j.molcel.2013.09.016); PMCID: PMC3867817.
* **[martina-2014-tfe3-autophagy]** Martina JA, Diab HI, Lishu L, et al. The nutrient-responsive transcription factor TFE3 promotes autophagy, lysosomal biogenesis, and clearance of cellular debris. *Science signaling* 2014;7:ra9. PMID: 24448649 (https://pubmed.ncbi.nlm.nih.gov/24448649/); DOI: 10.1126/scisignal.2004754 (https://doi.org/10.1126/scisignal.2004754); PMCID: PMC4696865.
* **[dunlop-2014-flcn-gabarap-ulk1]** Dunlop EA, Seifan S, Claessens T, et al. FLCN, a novel autophagy component, interacts with GABARAP and is regulated by ULK1 phosphorylation. *Autophagy* 2014;10:1749-60. PMID: 25126726 (https://pubmed.ncbi.nlm.nih.gov/25126726/); DOI: 10.4161/auto.29640 (https://doi.org/10.4161/auto.29640); PMCID: PMC4198360.
* **[peli-gulli-2015-lst4-lst7-gap]** Péli-Gulli MP, Sardu A, Panchaud N, et al. Amino Acids Stimulate TORC1 through Lst4-Lst7, a GTPase-Activating Protein Complex for the Rag Family GTPase Gtr2. *Cell reports* 2015;13:1-7. PMID: 26387955 (https://pubmed.ncbi.nlm.nih.gov/26387955/); DOI: 10.1016/j.celrep.2015.08.059 (https://doi.org/10.1016/j.celrep.2015.08.059).
* **[starling-2016-flcn-rab34-rilp]** Starling GP, Yip YY, Sanger A, et al. Folliculin directs the formation of a Rab34-RILP complex to control the nutrient-dependent dynamic distribution of lysosomes. *EMBO reports* 2016;17:823-41. PMID: 27113757 (https://pubmed.ncbi.nlm.nih.gov/27113757/); DOI: 10.15252/embr.201541382 (https://doi.org/10.15252/embr.201541382); PMCID: PMC4893818.
* **[zhong-2016-flcn-cilia]** Zhong M, Zhao X, Li J, et al. Tumor Suppressor Folliculin Regulates mTORC1 through Primary Cilia. *The Journal of biological chemistry* 2016;291:11689-97. PMID: 27072130 (https://pubmed.ncbi.nlm.nih.gov/27072130/); DOI: 10.1074/jbc.M116.719997 (https://doi.org/10.1074/jbc.M116.719997); PMCID: PMC4882437.
* **[wada-2016-flcn-adipose-browning]** Wada S, Neinast M, Jang C, et al. The tumor suppressor FLCN mediates an alternate mTOR pathway to regulate browning of adipose tissue. *Genes & development* 2016;30:2551-2564. PMID: 27913603 (https://pubmed.ncbi.nlm.nih.gov/27913603/); DOI: 10.1101/gad.287953.116 (https://doi.org/10.1101/gad.287953.116); PMCID: PMC5159669.
* **[dodding-2017-flcn-review]** Dodding MP. Folliculin - A tumor suppressor at the intersection of metabolic signaling and membrane traffic. *Small GTPases* 2017;8:100-105. PMID: 27355777 (https://pubmed.ncbi.nlm.nih.gov/27355777/); DOI: 10.1080/21541248.2016.1204808 (https://doi.org/10.1080/21541248.2016.1204808); PMCID: PMC5464117.
* **[schmidt-2018-flcn-review]** Schmidt LS, Linehan WM. FLCN: The causative gene for Birt-Hogg-Dubé syndrome. *Gene* 2018;640:28-42. PMID: 28970150 (https://pubmed.ncbi.nlm.nih.gov/28970150/); DOI: 10.1016/j.gene.2017.09.044 (https://doi.org/10.1016/j.gene.2017.09.044); PMCID: PMC5682220.
* **[meng-2018-gator1-flcn]** Meng J, Ferguson SM. GATOR1-dependent recruitment of FLCN-FNIP to lysosomes coordinates Rag GTPase heterodimer nucleotide status in response to amino acids. *The Journal of cell biology* 2018;217:2765-2776. PMID: 29848618 (https://pubmed.ncbi.nlm.nih.gov/29848618/); DOI: 10.1083/jcb.201712177 (https://doi.org/10.1083/jcb.201712177); PMCID: PMC6080935.
* **[shen-2019-flcn-fnip2-rag-ragulator]** Shen K, Rogala KB, Chou HT, et al. Cryo-EM Structure of the Human FLCN-FNIP2-Rag-Ragulator Complex. *Cell* 2019;179:1319-1329.e8. PMID: 31704029 (https://pubmed.ncbi.nlm.nih.gov/31704029/); DOI: 10.1016/j.cell.2019.10.036 (https://doi.org/10.1016/j.cell.2019.10.036); PMCID: PMC7008705.
* **[lawrence-2019-lfc-structure]** Lawrence RE, Fromm SA, Fu Y, et al. Structural mechanism of a Rag GTPase activation checkpoint by the lysosomal folliculin complex. *Science (New York, N.Y.)* 2019;366:971-977. PMID: 31672913 (https://pubmed.ncbi.nlm.nih.gov/31672913/); DOI: 10.1126/science.aax0364 (https://doi.org/10.1126/science.aax0364); PMCID: PMC6945816.
* **[kinoshita-2020-flcn-rab35]** Kinoshita R, Homma Y, Fukuda M. Rab35-GEFs, DENND1A and folliculin differentially regulate podocalyxin trafficking in two- and three-dimensional epithelial cell cultures. *The Journal of biological chemistry* 2020;295:3652-3663. PMID: 31992598 (https://pubmed.ncbi.nlm.nih.gov/31992598/); DOI: 10.1074/jbc.RA119.011646 (https://doi.org/10.1074/jbc.RA119.011646); PMCID: PMC7076212.
* **[napolitano-2020-substrate-specific-mtorc1]** Napolitano G, Di Malta C, Esposito A, et al. A substrate-specific mTORC1 pathway underlies Birt-Hogg-Dubé syndrome. *Nature* 2020;585:597-602. PMID: 32612235 (https://pubmed.ncbi.nlm.nih.gov/32612235/); DOI: 10.1038/s41586-020-2444-0 (https://doi.org/10.1038/s41586-020-2444-0); PMCID: PMC7610377.
* **[zhang-2021-flcn-cilia-kinesin2]** Zhang Y, Liu Y, Dai Y, et al. Ciliary localization of folliculin mediated via a kinesin-2-binding motif is required for its functions in mTOR regulation and tumor suppression. *FEBS letters* 2021;595:123-132. PMID: 33064845 (https://pubmed.ncbi.nlm.nih.gov/33064845/); DOI: 10.1002/1873-3468.13959 (https://doi.org/10.1002/1873-3468.13959); PMCID: PMC7980781.
* **[jansen-2022-flcn-gap-structure]** Jansen RM, Peruzzo R, Fromm SA, et al. Structural basis for FLCN RagC GAP activation in MiT-TFE substrate-selective mTORC1 regulation. *Science advances* 2022;8:eadd2926. PMID: 36103527 (https://pubmed.ncbi.nlm.nih.gov/36103527/); DOI: 10.1126/sciadv.add2926 (https://doi.org/10.1126/sciadv.add2926); PMCID: PMC9473554.
* **[lingaas-2003-canine-bhd]** Lingaas F, Comstock KE, Kirkness EF, et al. A mutation in the canine BHD gene is associated with hereditary multifocal renal cystadenocarcinoma and nodular dermatofibrosis in the German Shepherd dog. *Human molecular genetics* 2003;12:3043-53. PMID: 14532326 (https://pubmed.ncbi.nlm.nih.gov/14532326/); DOI: 10.1093/hmg/ddg336 (https://doi.org/10.1093/hmg/ddg336).
* **[togashi-2006-nihon-rat-rescue]** Togashi Y, Kobayashi T, Momose S, et al. Transgenic rescue from embryonic lethality and renal carcinogenesis in the Nihon rat model by introduction of a wild-type Bhd gene. *Oncogene* 2006;25:2885-9. PMID: 16369488 (https://pubmed.ncbi.nlm.nih.gov/16369488/); DOI: 10.1038/sj.onc.1209317 (https://doi.org/10.1038/sj.onc.1209317).
* **[woodford-2016-fnip-hsp90]** Woodford MR, Dunn DM, Blanden AR, et al. The FNIP co-chaperones decelerate the Hsp90 chaperone cycle and enhance drug binding. *Nature communications* 2016;7:12037. PMID: 27353360 (https://pubmed.ncbi.nlm.nih.gov/27353360/); DOI: 10.1038/ncomms12037 (https://doi.org/10.1038/ncomms12037); PMCID: PMC4931344.
* **[woodford-2021-flcn-ldha]** Woodford MR, Baker-Williams AJ, Sager RA, et al. The tumor suppressor folliculin inhibits lactate dehydrogenase A and regulates the Warburg effect. *Nature structural & molecular biology* 2021;28:662-670. PMID: 34381247 (https://pubmed.ncbi.nlm.nih.gov/34381247/); DOI: 10.1038/s41594-021-00633-2 (https://doi.org/10.1038/s41594-021-00633-2); PMCID: PMC9278990.


## Citations

1. baba-2006-fnip1-ampk-abstract.md
2. baba-2006-fnip1-ampk-summary.md
3. dodding-2017-flcn-review-abstract.md
4. dodding-2017-flcn-review-summary.md
5. dunlop-2014-flcn-gabarap-ulk1-abstract.md
6. dunlop-2014-flcn-gabarap-ulk1-summary.md
7. hasumi-2008-fnip2-abstract.md
8. hasumi-2008-fnip2-summary.md
9. hasumi-2009-bhd-knockout-abstract.md
10. hasumi-2009-bhd-knockout-summary.md
11. hong-2010-flcn-tfe3-abstract.md
12. hong-2010-flcn-tfe3-fulltext.txt
13. hong-2010-flcn-tfe3-summary.md
14. jansen-2022-flcn-gap-structure-abstract.md
15. jansen-2022-flcn-gap-structure-fulltext.txt
16. jansen-2022-flcn-gap-structure-summary.md
17. kinoshita-2020-flcn-rab35-abstract.md
18. kinoshita-2020-flcn-rab35-summary.md
19. lawrence-2019-lfc-structure-abstract.md
20. lawrence-2019-lfc-structure-fulltext.txt
21. lawrence-2019-lfc-structure-summary.md
22. lingaas-2003-canine-bhd-abstract.md
23. lingaas-2003-canine-bhd-summary.md
24. martina-2014-tfe3-autophagy-abstract.md
25. martina-2014-tfe3-autophagy-fulltext.txt
26. martina-2014-tfe3-autophagy-summary.md
27. meng-2018-gator1-flcn-abstract.md
28. meng-2018-gator1-flcn-fulltext.txt
29. meng-2018-gator1-flcn-summary.md
30. metadata.json
31. napolitano-2020-substrate-specific-mtorc1-abstract.md
32. napolitano-2020-substrate-specific-mtorc1-fulltext.txt
33. napolitano-2020-substrate-specific-mtorc1-summary.md
34. nickerson-2002-bhd-gene-abstract.md
35. nickerson-2002-bhd-gene-summary.md
36. nookala-2012-flcn-denn-structure-abstract.md
37. nookala-2012-flcn-denn-structure-fulltext.txt
38. nookala-2012-flcn-denn-structure-summary.md
39. peli-gulli-2015-lst4-lst7-gap-abstract.md
40. peli-gulli-2015-lst4-lst7-gap-summary.md
41. petit-2013-flcn-lysosome-rag-abstract.md
42. petit-2013-flcn-lysosome-rag-fulltext.txt
43. petit-2013-flcn-lysosome-rag-summary.md
44. schmidt-2018-flcn-review-abstract.md
45. schmidt-2018-flcn-review-fulltext.txt
46. schmidt-2018-flcn-review-summary.md
47. shen-2019-flcn-fnip2-rag-ragulator-abstract.md
48. shen-2019-flcn-fnip2-rag-ragulator-fulltext.txt
49. shen-2019-flcn-fnip2-rag-ragulator-summary.md
50. starling-2016-flcn-rab34-rilp-abstract.md
51. starling-2016-flcn-rab34-rilp-fulltext.txt
52. starling-2016-flcn-rab34-rilp-summary.md
53. takagi-2008-fnipl-abstract.md
54. takagi-2008-fnipl-summary.md
55. togashi-2006-nihon-rat-rescue-abstract.md
56. togashi-2006-nihon-rat-rescue-summary.md
57. tsun-2013-flcn-ragcd-gap-abstract.md
58. tsun-2013-flcn-ragcd-gap-fulltext.txt
59. tsun-2013-flcn-ragcd-gap-summary.md
60. uniprot-A0A8C4MM62-entry.txt
61. uniprot-A0A8C4MM62.fasta
62. uniprot-Q8NFG4-human-FLCN.fasta
63. wada-2016-flcn-adipose-browning-abstract.md
64. wada-2016-flcn-adipose-browning-fulltext.txt
65. wada-2016-flcn-adipose-browning-summary.md
66. wang-2020-donkey-genomes-abstract.md
67. wang-2020-donkey-genomes-fulltext.txt
68. wang-2020-donkey-genomes-summary.md
69. woodford-2016-fnip-hsp90-abstract.md
70. woodford-2016-fnip-hsp90-fulltext.txt
71. woodford-2016-fnip-hsp90-summary.md
72. woodford-2021-flcn-ldha-abstract.md
73. woodford-2021-flcn-ldha-fulltext.txt
74. woodford-2021-flcn-ldha-summary.md
75. zhang-2021-flcn-cilia-kinesin2-abstract.md
76. zhang-2021-flcn-cilia-kinesin2-fulltext.txt
77. zhang-2021-flcn-cilia-kinesin2-summary.md
78. zhong-2016-flcn-cilia-abstract.md
79. zhong-2016-flcn-cilia-summary.md