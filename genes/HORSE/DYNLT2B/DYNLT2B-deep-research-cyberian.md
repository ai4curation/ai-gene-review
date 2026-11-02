---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T02:35:25.476934'
end_time: '2026-10-26T02:44:19.838079'
duration_seconds: 534.36
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: DYNLT2B
  gene_symbol: DYNLT2B
  uniprot_accession: A0A9L0SWY1
  protein_description: 'SubName: Full=Dynein light chain Tctex-type 2B {ECO:0000313|Ensembl:ENSECAP00000080542.1};'
  gene_info: Name=DYNLT2B {ECO:0000313|Ensembl:ENSECAP00000080542.1};
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the dynein light chain Tctex-type family.
  protein_domains: Tctex-1-like. (IPR005334); Tctex-1-like_sf. (IPR038586); Tctex-1
    (PF03645)
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
citation_count: 55
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0SWY1
- **Protein Description:** SubName: Full=Dynein light chain Tctex-type 2B {ECO:0000313|Ensembl:ENSECAP00000080542.1};
- **Gene Information:** Name=DYNLT2B {ECO:0000313|Ensembl:ENSECAP00000080542.1};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the dynein light chain Tctex-type family.
- **Key Domains:** Tctex-1-like. (IPR005334); Tctex-1-like_sf. (IPR038586); Tctex-1 (PF03645)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "DYNLT2B" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'DYNLT2B' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **DYNLT2B** (gene ID: DYNLT2B, UniProt: A0A9L0SWY1) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# DYNLT2B (Dynein light chain Tctex-type 2B) in the horse, *Equus caballus* (UniProt A0A9L0SWY1)

## 1. Introduction and summary

DYNLT2B, formerly called TCTEX1D2 ("Tctex1 domain-containing 2"), is a small dynein light chain of the Tctex-type family. Its main, best-supported role is as the one light chain unique to **cytoplasmic dynein-2**, the minus-end-directed motor that drives retrograde intraflagellar transport (IFT) from the ciliary tip back to the base [asante-2014-dynein2-composition-abstract; schmidts-2015-tctex1d2-jatd-abstract; braschi-2022-dynein-nomenclature-fulltext]. DYNLT2B has no catalytic activity. It acts as a scaffolding light chain. It forms a domain-swapped heterodimer with the shared light chain DYNLT1 (or its paralogue DYNLT3), and that heterodimer binds a conserved segment of the dynein-2 intermediate chain WDR60 (DYNC2I1). In doing so it bridges the N-proximal regions of the two different dynein-2 intermediate chains, WDR60 and WDR34 [hamada-2018-wdr60-tctex1d2-abstract; mukhopadhyay-2024-dynein2-ic-tethering-fulltext]. Losing it weakens but does not abolish retrograde IFT. In humans this produces a partially penetrant skeletal ciliopathy, Jeune asphyxiating thoracic dystrophy / short-rib thoracic dysplasia [schmidts-2015-tctex1d2-jatd-abstract; zschocke-2017-tctex1d2-variable-expressivity-abstract]. A second role, conserved from *Chlamydomonas* to mouse, is as a light chain of the axonemal inner dynein arm I1/f (dynein-f). This role matters most for building the sperm flagellum [schmidts-2015-tctex1d2-jatd-fulltext; harima-2025-tctex1d2-sperm-abstract; lee-2020-dynap-partitioning-fulltext].

No experimental study of horse DYNLT2B was found. The horse entry A0A9L0SWY1 is an unreviewed TrEMBL record predicted by Ensembl from the Thoroughbred reference genome [wade-2009-horse-genome-abstract]. Everything said here about the horse protein is therefore inferred from orthology, mainly with human DYNLT2B (UniProt Q8WW35), mouse Tctex1d2 and *Chlamydomonas* Tctex2b. Section 2 explains why that inference is well founded and also notes problems with the horse gene model.

## 2. Identity of the horse protein and orthology to DYNLT2B/TCTEX1D2

The gene symbol is not ambiguous here. UniProt A0A9L0SWY1 is annotated as "Dynein light chain Tctex-type 2B" (gene DYNLT2B), with a Tctex-1 domain (PF03645; InterPro IPR005334/IPR038586). It is assigned to the PANTHER subfamily PTHR21255:SF7 ("dynein light chain Tctex-type protein 2B") and the CDD family cd21459 (DLC-like_TCTEX1D2). It maps to Ensembl gene ENSECAG00000015913 on horse chromosome 19 (UniProt record, retrieved for this report; see `citations/uniprot-A0A9L0SWY1.fasta`). DYNLT2B is the HGNC-approved name that replaced TCTEX1D2 in the 2022 consensus dynein nomenclature [braschi-2022-dynein-nomenclature-fulltext]. That nomenclature splits the Tctex-type light chains into separate clades (DYNLT1/3, DYNLT2, DYNLT2B, DYNLT4, DYNLT5). It places DYNLT2B in the dynein-2 complex and the I1/f inner dynein arm, separate from DYNLT1 and DYNLT3, which are shared with dynein-1 [braschi-2022-dynein-nomenclature-fulltext].

For this report I aligned the horse sequence (245 aa) with human DYNLT2B (Q8WW35, 142 aa) using a local Smith-Waterman alignment (BLOSUM62; `notes-alignment.txt`). Horse residues 120–244 align with human residues 4–127 at 92% identity (114 of 124 positions) with no gaps, covering the whole Tctex-1 fold. Two features of the horse model look like gene-prediction artefacts rather than real biology, and they should be flagged for curators. First, the horse sequence has a roughly 119-residue N-terminal extension, rich in Pro, Ala, Gly, Ser and Arg, which has no counterpart in human DYNLT2B. UniProt predicts much of it to be disordered (positions 23–83). Second, the horse model ends at "…YTHDVFMNK". It lacks the conserved human C-terminal segment "DSLFCVVAAFGCFYY" (human residues 128–142). This segment is conserved at the C-terminal end of the human Tctex-1 domain, and its structural role was not assessed in the sources reviewed here. Ensembl data narrow this down. The horse gene (ENSECAG00000015913, EquCab3.0 chromosome 19) has ten annotated protein-coding transcripts, with predicted products ranging from 132 to 259 residues (`citations/ensembl-ENSECAG00000015913-lookup.json`). A0A9L0SWY1 corresponds to transcript DYNLT2B-203 and is not the Ensembl canonical transcript. Another transcript, DYNLT2B-209 (ENSECAP00000013483), encodes a 142-residue protein that starts with "MAAP…" at the same point as human DYNLT2B, with no N-terminal extension. Across its full length it is 86% identical to the human protein (`notes-alignment-isoforms.txt`). The N-terminal extension in A0A9L0SWY1 is therefore probably an alternative upstream start or exon, not the main protein product. The C-terminal difference, by contrast, is shared by both horse models. Both diverge right after the conserved "…DVFMN" motif, and the 142-residue isoform ends in "IAINKKINQ" instead of the human "DSLFCVVAAFGCFYY". This suggests that the current horse assembly or annotation is missing the conserved last coding exon, or that horse uses a different final exon. The point needs checking against transcript evidence. Even so, the near-identity of the core domain makes it very likely that the horse gene encodes a functional DYNLT2B orthologue, with the same partners and roles described below.

## 3. Molecular function: a Tctex-type scaffolding light chain of dynein-2

Proteomic analysis of the human dynein-2 complex established that WDR34 and WDR60 are its two intermediate chains and identified TCTEX1D2 as a light chain unique to dynein-2 and required for cilia function. The same work found light chains shared with dynein-1 (DYNLT1/3, DYNLRB1/2, DYNLL1/2) and showed that the dynein-1 regulators dynactin, LIS1 and BICD2 are not associated with dynein-2 [asante-2014-dynein2-composition-abstract]. Independently, affinity purification of Tctex1d2 recovered Wdr34, Wdr60 and other subunits of dynein-1 and dynein-2, together with tubulins and centrosomal proteins [gholkar-2015-tctex1d2-ciliogenesis-abstract; gholkar-2015-tctex1d2-ciliogenesis-fulltext]. In *Chlamydomonas*, immunoprecipitation of the IFT dynein intermediate chain D1bIC2 (the WDR34 homologue) co-purified D1bIC1 (the WDR60 homologue), Tctex2b (the TCTEX1D2 homologue), Tctex1 and LC8. All detectable Tctex2b in the fraction was recovered. This showed that Tctex2b is a true subunit of IFT dynein and belongs to an intermediate-chain/light-chain subcomplex [schmidts-2015-tctex1d2-jatd-fulltext].

Hamada and colleagues mapped the binding partners more precisely using visible immunoprecipitation assays. They divided dynein-2 into three subcomplexes: DYNC2H1–DYNC2LI1, WDR34–DYNLL1/2–DYNLRB1/2, and WDR60–TCTEX1D2–DYNLT1/DYNLT3. TCTEX1D2 forms a dimer with DYNLT1 or DYNLT3, and this dimer binds a 50-residue segment of WDR60 (residues 473–522) that is highly conserved across vertebrates [hamada-2018-wdr60-tctex1d2-abstract; hamada-2018-wdr60-tctex1d2-fulltext]. Structural work then confirmed and refined this model. The cryo-EM structure of recombinant human dynein-2 (about 1.4 MDa) showed that the WDR60–WDR34 heterodimer and its light chains force the two identical heavy chains into different, asymmetric conformations. A weaker, flexible density in that map was assigned to the TCTEX–TCTEX1D2 dimer [toropova-2019-dynein2-structure-abstract; toropova-2019-dynein2-structure-fulltext]. Mukhopadhyay et al. purified the DYNLT1–DYNLT2B complex and showed by SEC-MALS that it is a heterodimer. They solved its crystal structure at 2 Å, which revealed a domain-swapped heterodimer [mukhopadhyay-2024-dynein2-ic-tethering-fulltext]. This answered a question the nomenclature paper had left open, namely whether DYNLT2B is a homodimer, a heterodimer or a monomer [braschi-2022-dynein-nomenclature-fulltext]. AlphaFold-Multimer modelling, which agrees with the earlier biochemical mapping, predicts that WDR34 residues 37–50 bind an edge strand of DYNLT1. WDR60 residues 469–512 bind an edge strand of DYNLT2B and then form a helix that wraps around the heterodimer. The DYNLT1–DYNLT2B heterodimer therefore holds the N-proximal regions of the two intermediate chains together. This is unusual, because all the other dynein-2 light chains are homodimers [mukhopadhyay-2024-dynein2-ic-tethering-fulltext].

In terms of molecular function, the gene product is best described as a dynein intermediate-chain-binding protein. It is a non-catalytic structural subunit that contributes to the architecture of the dynein-2 tail. It does not itself bind cargo or hydrolyse ATP. This matches the human GO annotations "dynein intermediate chain binding" (IPI) and "cytoplasmic dynein complex" (IDA) (UniProt Q8WW35 record, `citations/uniprot-Q8WW35-entry.txt`).

## 4. Biological process: retrograde intraflagellar transport and ciliogenesis

Dynein-2 powers retrograde IFT. It returns IFT-A/IFT-B trains and cargo from the ciliary tip to the base, and in doing so it controls the protein composition of cilia and ciliary signalling [asante-2014-dynein2-composition-abstract; toropova-2019-dynein2-structure-abstract]. Several lines of evidence place DYNLT2B in this process. Fibroblasts from patients with biallelic TCTEX1D2 loss-of-function variants showed retrograde IFT defects. *Chlamydomonas* tctex2b null cells showed fewer and slower retrograde IFT trains while anterograde IFT was normal, and IFT dynein was partly destabilized [schmidts-2015-tctex1d2-jatd-abstract; schmidts-2015-tctex1d2-jatd-fulltext; antony-2021-ciliary-dyneins-review-fulltext]. In human RPE1 cells, TCTEX1D2 knockout caused IFT88 to accumulate slightly but significantly within cilia and changed the distribution of IFT140. These defects were milder than in WDR60 knockout cells. A WDR60 mutant that cannot bind TCTEX1D2 only restored trafficking to the level seen in TCTEX1D2-KO cells, which links the defect directly to the WDR60–TCTEX1D2 interaction [hamada-2018-wdr60-tctex1d2-abstract; hamada-2018-wdr60-tctex1d2-fulltext]. Fewer cells formed cilia, but cilia that did form were of normal length [hamada-2018-wdr60-tctex1d2-fulltext]. Depleting Tctex1d2 in human cells has also been reported to impair ciliogenesis [gholkar-2015-tctex1d2-ciliogenesis-abstract].

All of this supports the description of TCTEX1D2 as an auxiliary component of dynein-2: it is needed for fully efficient retrograde trafficking, but it is not essential for the motor to work [hamada-2018-wdr60-tctex1d2-abstract]. The partial redundancy of TCTEX1D2 is thought to explain why human TCTEX1D2 variants that are probably null still give milder or partially penetrant phenotypes than mutations in other dynein-2 subunits [schmidts-2015-tctex1d2-jatd-abstract; antony-2021-ciliary-dyneins-review-fulltext]. One mechanistic idea follows from the structural work. The DYNLT1–DYNLT2B heterodimer sits just C-terminal to the unstructured N-terminal extension of WDR60, which tethers dynein-2 to anterograde IFT trains and helps target it into cilia. DYNLT2B may therefore help hold that tether in the right position relative to the motor [mukhopadhyay-2024-dynein2-ic-tethering-abstract; mukhopadhyay-2024-dynein2-ic-tethering-fulltext]. This mechanistic link is inferred from the structure and has not been tested directly. Because retrograde IFT is needed for primary-cilium-dependent signalling during skeletal development, DYNLT2B's role in skeletal formation probably acts through this pathway [schmidts-2015-tctex1d2-jatd-abstract; antony-2021-ciliary-dyneins-review-fulltext].

## 5. A second role in the axonemal inner dynein arm I1/f and in sperm flagellum assembly

Tctex2b was first characterized in *Chlamydomonas* as a light chain of the axonemal inner-arm dynein I1/f. Tctex2b-null cells swim slowly because of an I1/f defect [schmidts-2015-tctex1d2-jatd-fulltext; yamamoto-2021-chlamydomonas-ida-abstract]. In that alga, Tctex2b co-purifies with I1 through sucrose-gradient and ion-exchange fractionation. It is not needed to assemble I1, but without it the I1 particle falls apart when extracted in high salt, flagellar beat frequency drops, and microtubule sliding by the axonemal dyneins is reduced in vitro [dibella-2004-tctex2b-i1-dynein-abstract]. Cryo-electron tomography and mass spectrometry of tctex2b mutants later showed that Tctex2b is needed for the stable assembly of Tctex1, IC97 and FAP120 into the I1 intermediate-chain/light-chain complex. That region overlaps the IC138 regulatory subcomplex, which controls ciliary bending [fu-2021-i1-ic-lc-structure-abstract]. The pattern resembles dynein-2, where DYNLT2B pairs with a Tctex1-family partner and stabilizes an intermediate-chain/light-chain module rather than being an essential core subunit. When Schmidts et al. found the same protein in IFT dynein, they checked that this was not contamination from I1/f: the I1/f intermediate chain IC140 was absent from the IFT-dynein immunoprecipitates [schmidts-2015-tctex1d2-jatd-fulltext]. The dual role is also seen in vertebrates. In *Xenopus* multiciliated cells, GFP-Tctex1d2 colocalized completely with the IDA-f subunit Wdr78 inside dynein axonemal particles (DynAPs). These are liquid-like cytoplasmic compartments where axonemal dyneins are pre-assembled before they are transported into cilia [lee-2020-dynap-partitioning-fulltext]. This study is the basis for the UniProt subcellular-location annotation "dynein axonemal particle". In mouse testis, TCTEX1D2 co-immunoprecipitated both with dynein-2 subunits (WDR34, WDR60, DYNLT1) and with the IDA intermediate chains WDR63 and WDR78. *Tctex1d2*−/− males were infertile, with disorganized sperm axonemes and mislocalized dynein-2 subunits, while motile cilia in other tissues were normal [harima-2025-tctex1d2-sperm-abstract; harima-2025-tctex1d2-sperm-fulltext]. A human family with a homozygous TCTEX1D2 deletion showed situs inversus, heart defects and mild abnormalities of motile cilia. This suggests that some motile-cilia function may also be affected in humans [zschocke-2017-tctex1d2-variable-expressivity-abstract].

## 6. Subcellular localization

The evidence consistently places the protein in the dynein-2 holoenzyme at the ciliary base and inside cilia, and in the cytoplasm as part of pre-assembled dynein complexes. In human cells, endogenous Tctex1d2 colocalized with Wdr60 at the microtubule-organizing centre in interphase, at spindle poles in mitosis, and at the centrioles/basal body at the base of the primary cilium. Its localization to the ciliary base depended on microtubules and on Wdr60 [gholkar-2015-tctex1d2-ciliogenesis-fulltext]. In mouse spermatids, TCTEX1D2 runs along the developing flagellum and is also found in the manchette, a transient microtubule-based structure used for intramanchette transport [harima-2025-tctex1d2-sperm-fulltext]. In multiciliated cells, it is found in DynAP subcompartments together with IDA-f components [lee-2020-dynap-partitioning-fulltext]. If the horse orthologue behaves in the same way, it would be expected at the basal body, along the ciliary axoneme as part of retrograde IFT trains, in cytoplasmic DynAPs of multiciliated cells, and in the sperm flagellum. All of these horse localizations are predictions.

## 7. Disease relevance and other proposed functions

In humans, biallelic DYNLT2B/TCTEX1D2 variants cause short-rib thoracic dysplasia 17 with or without polydactyly (SRTD17; MIM 617405). The first variants found were a canonical splice-site change (c.113+2C>G), a nonsense variant (p.Arg88*) and a frameshift (c.100delinsCT), and inheritance was partially penetrant [schmidts-2015-tctex1d2-jatd-fulltext]. Reviews describe TCTEX1D2 as a rare cause of dynein-2-related skeletal ciliopathies [antony-2021-ciliary-dyneins-review-fulltext; rao-2024-dynein-noncatalytic-review-fulltext]. No horse disease association was found. One single-laboratory study in 3T3-L1 adipocytes reported a non-ciliary role. In that study Tctex1d2 bound syntaxin 4 in an insulin-dependent way and blocked Doc2b–syntaxin 4 binding, acting as a negative regulator of insulin-stimulated GLUT4 translocation [shimoda-2015-tctex1d2-glut4-abstract]. This has not been confirmed independently and has no structural basis yet, so it should be treated as provisional rather than as a core function.

## 8. Summary for functional annotation of the horse protein

Taking these sources together, the horse DYNLT2B protein (A0A9L0SWY1) can be annotated by orthology as follows. Molecular function: dynein intermediate chain binding (to DYNC2I1/WDR60), and heterodimerization with DYNLT1/DYNLT3. Cellular component: cytoplasmic dynein-2 complex, cilium/ciliary basal body, dynein axonemal particle, and the axonemal inner dynein arm I1/f. Biological process: intraciliary retrograde transport, cilium assembly, and sperm flagellum assembly [asante-2014-dynein2-composition-abstract; hamada-2018-wdr60-tctex1d2-abstract; mukhopadhyay-2024-dynein2-ic-tethering-fulltext; harima-2025-tctex1d2-sperm-abstract]. The protein has no enzymatic activity or transport substrate. Its role is structural: it is the dynein-2-specific half of a Tctex heterodimer that bridges the two intermediate chains in the motor's tail.

## Open Questions

Several points remain unresolved and would be worth following up. First, the horse gene model should be checked against horse RNA-seq or Iso-Seq data and against other equid genomes. That would show which of the ten Ensembl transcripts is the main one and whether the conserved C-terminal exon is really missing in EquCab3.0. If that segment really is missing, it would be worth testing whether the horse protein can still fold and form the heterodimer with DYNLT1. Second, it is still unclear mechanistically why DYNLT2B is needed for fully efficient retrograde IFT. Does it stabilize the WDR60 N-terminal tether, adjust dynein-2 autoinhibition, or help load dynein-2 onto IFT trains at the ciliary base? Cryo-ET of IFT trains from DYNLT2B-null cells could test this. Third, it is not known how the same light chain is sorted between dynein-2 and dynein-f/I1 in cells that build both, or whether DYNLT1 and DYNLT3 partner it differently in the two complexes. Fourth, the proposed syntaxin-4/GLUT4 role needs independent confirmation. Finally, nothing is known about DYNLT2B expression, variation or phenotype in horses. Screening equine skeletal dysplasias or stallion subfertility cases for DYNLT2B variants would be a natural, if speculative, next step.

## References

* [schmidts-2015-tctex1d2-jatd]: Schmidts M, Hou Y, Cortés CR, Mans DA, Huber C, Boldt K, Patel M, van Reeuwijk J, Plaza JM, van Beersum SE, Yap ZM, Letteboer SJ, Taylor SP, Herridge W, Johnson CA, Scambler PJ, Ueffing M, Kayserili H, Krakow D, King SM, UK10K, Beales PL, Al-Gazali L, Wicking C, Cormier-Daire V, Roepman R, Mitchison HM, Witman GB. (2015). TCTEX1D2 mutations underlie Jeune asphyxiating thoracic dystrophy with impaired retrograde intraflagellar transport. *Nature communications* 6(None):7074. PMID:26044572; PMCID:PMC4468853; DOI:10.1038/ncomms8074; https://pubmed.ncbi.nlm.nih.gov/26044572/
* [gholkar-2015-tctex1d2-ciliogenesis]: Gholkar AA, Senese S, Lo YC, Capri J, Deardorff WJ, Dharmarajan H, Contreras E, Hodara E, Whitelegge JP, Jackson PK, Torres JZ. (2015). Tctex1d2 associates with short-rib polydactyly syndrome proteins and is required for ciliogenesis. *Cell cycle (Georgetown, Tex.)* 14(7):1116-1125. PMID:25830415; PMCID:PMC4614626; DOI:10.4161/15384101.2014.985066; https://pubmed.ncbi.nlm.nih.gov/25830415/
* [asante-2014-dynein2-composition]: Asante D, Stevenson NL, Stephens DJ. (2014). Subunit composition of the human cytoplasmic dynein-2 complex. *Journal of cell science* 127(Pt 21):4774-4787. PMID:25205765; PMCID:PMC4215718; DOI:10.1242/jcs.159038; https://pubmed.ncbi.nlm.nih.gov/25205765/
* [hamada-2018-wdr60-tctex1d2]: Hamada Y, Tsurumi Y, Nozaki S, Katoh Y, Nakayama K. (2018). Interaction of WDR60 intermediate chain with TCTEX1D2 light chain of the dynein-2 complex is crucial for ciliary protein trafficking. *Molecular biology of the cell* 29(13):1628-1639. PMID:29742051; PMCID:PMC6080652; DOI:10.1091/mbc.e18-03-0173; https://pubmed.ncbi.nlm.nih.gov/29742051/
* [toropova-2019-dynein2-structure]: Toropova K, Zalyte R, Mukhopadhyay AG, Mladenov M, Carter AP, Roberts AJ. (2019). Structure of the dynein-2 complex and its assembly with intraflagellar transport trains. *Nature structural & molecular biology* 26(9):823-829. PMID:31451806; PMCID:PMC6774794; DOI:10.1038/s41594-019-0286-y; https://pubmed.ncbi.nlm.nih.gov/31451806/
* [mukhopadhyay-2024-dynein2-ic-tethering]: Mukhopadhyay AG, Toropova K, Daly L, Wells JN, Vuolo L, Mladenov M, Seda M, Jenkins D, Stephens DJ, Roberts AJ. (2024). Structure and tethering mechanism of dynein-2 intermediate chains in intraflagellar transport. *The EMBO journal* 43(7):1257-1272. PMID:38454149; PMCID:PMC10987677; DOI:10.1038/s44318-024-00060-1; https://pubmed.ncbi.nlm.nih.gov/38454149/
* [harima-2025-tctex1d2-sperm]: Harima R, Hara K, Tanemura K. (2025). TCTEX1D2 is essential for sperm flagellum formation in mice. *Scientific reports* 15(1):2413. PMID:39827215; PMCID:PMC11743150; DOI:10.1038/s41598-024-83424-1; https://pubmed.ncbi.nlm.nih.gov/39827215/
* [braschi-2022-dynein-nomenclature]: Braschi B, Omran H, Witman GB, Pazour GJ, Pfister KK, Bruford EA, King SM. (2022). Consensus nomenclature for dyneins and associated assembly factors. *The Journal of cell biology* 221(2):e202109014. PMID:35006274; PMCID:PMC8754002; DOI:10.1083/jcb.202109014; https://pubmed.ncbi.nlm.nih.gov/35006274/
* [zschocke-2017-tctex1d2-variable-expressivity]: Zschocke J, Schossig A, Bosshardt DD, Karall D, Glueckert R, Kapferer-Seebacher I. (2017). Variable expressivity of TCTEX1D2 mutations and a possible pathogenic link of molar-incisor malformation to ciliary dysfunction. *Archives of oral biology* 80(None):222-228. PMID:28475963; PMCID:None; DOI:10.1016/j.archoralbio.2017.04.009; https://pubmed.ncbi.nlm.nih.gov/28475963/
* [shimoda-2015-tctex1d2-glut4]: Shimoda Y, Okada S, Yamada E, Pessin JE, Yamada M. (2015). Tctex1d2 Is a Negative Regulator of GLUT4 Translocation and Glucose Uptake. *Endocrinology* 156(10):3548-3558. PMID:26200093; PMCID:PMC5398638; DOI:10.1210/en.2015-1120; https://pubmed.ncbi.nlm.nih.gov/26200093/
* [mukhopadhyay-2015-tctex1d2-commentary]: Mukhopadhyay S. (2015). TCTEX1D2, a potential link to skeletal ciliopathies. *Cell cycle (Georgetown, Tex.)* 14(3):293-294. PMID:25590661; PMCID:PMC4353232; DOI:10.1080/15384101.2015.1006548; https://pubmed.ncbi.nlm.nih.gov/25590661/
* [yamamoto-2021-chlamydomonas-ida]: Yamamoto R, Hwang J, Ishikawa T, Kon T, Sale WS. (2021). Composition and function of ciliary inner-dynein-arm subunits studied in Chlamydomonas reinhardtii. *Cytoskeleton (Hoboken, N.J.)* 78(3):77-96. PMID:33876572; PMCID:PMC8217317; DOI:10.1002/cm.21662; https://pubmed.ncbi.nlm.nih.gov/33876572/
* [rao-2024-dynein-noncatalytic-review]: Rao L, Gennerich A. (2024). Structure and Function of Dynein's Non-Catalytic Subunits. *Cells* 13(4):330. PMID:38391943; PMCID:PMC10886578; DOI:10.3390/cells13040330; https://pubmed.ncbi.nlm.nih.gov/38391943/
* [antony-2021-ciliary-dyneins-review]: Antony D, Brunner HG, Schmidts M. (2021). Ciliary Dyneins and Dynein Related Ciliopathies. *Cells* 10(8):1885. PMID:34440654; PMCID:PMC8391580; DOI:10.3390/cells10081885; https://pubmed.ncbi.nlm.nih.gov/34440654/
* [lee-2020-dynap-partitioning]: Lee C, Cox RM, Papoulas O, Horani A, Drew K, Devitt CC, Brody SL, Marcotte EM, Wallingford JB. (2020). Functional partitioning of a liquid-like organelle during assembly of axonemal dyneins. *eLife* 9(None):e58662. PMID:33263282; PMCID:PMC7785291; DOI:10.7554/elife.58662; https://pubmed.ncbi.nlm.nih.gov/33263282/
* [wade-2009-horse-genome]: Wade CM, Giulotto E, Sigurdsson S, Zoli M, Gnerre S, Imsland F, Lear TL, Adelson DL, Bailey E, Bellone RR, Blöcker H, Distl O, Edgar RC, Garber M, Leeb T, Mauceli E, MacLeod JN, Penedo MC, Raison JM, Sharpe T, Vogel J, Andersson L, Antczak DF, Biagi T, Binns MM, Chowdhary BP, Coleman SJ, Della Valle G, Fryc S, Guérin G, Hasegawa T, Hill EW, Jurka J, Kiialainen A, Lindgren G, Liu J, Magnani E, Mickelson JR, Murray J, Nergadze SG, Onofrio R, Pedroni S, Piras MF, Raudsepp T, Rocchi M, Røed KH, Ryder OA, Searle S, Skow L, Swinburne JE, Syvänen AC, Tozaki T, Valberg SJ, Vaudin M, White JR, Zody MC, Broad Institute Genome Sequencing Platform, Broad Institute Whole Genome Assembly Team, Lander ES, Lindblad-Toh K. (2009). Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science (New York, N.Y.)* 326(5954):865-867. PMID:19892987; PMCID:PMC3785132; DOI:10.1126/science.1178158; https://pubmed.ncbi.nlm.nih.gov/19892987/
* [dibella-2004-tctex2b-i1-dynein]: DiBella LM, Smith EF, Patel-King RS, Wakabayashi K, King SM. (2004). A novel Tctex2-related light chain is required for stability of inner dynein arm I1 and motor function in the Chlamydomonas flagellum. *The Journal of biological chemistry* 279(20):21666-21676. PMID:15020587; PMCID:None; DOI:10.1074/jbc.m313540200; https://pubmed.ncbi.nlm.nih.gov/15020587/
* [fu-2021-i1-ic-lc-structure]: Fu G, Scarbrough C, Song K, Phan N, Wirschell M, Nicastro D. (2021). Structural organization of the intermediate and light chain complex of Chlamydomonas ciliary I1 dynein. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology* 35(6):e21646. PMID:33993568; PMCID:PMC8820979; DOI:10.1096/fj.202001857r; https://pubmed.ncbi.nlm.nih.gov/33993568/
* [ensembl-ENSECAG00000015913]: Ensembl gene ENSECAG00000015913 (DYNLT2B, EquCab3.0), REST lookup and protein ENSECAP00000013483, https://rest.ensembl.org/lookup/id/ENSECAG00000015913 (accessed 2026-10-26).
* [uniprot-A0A9L0SWY1]: UniProtKB/TrEMBL entry A0A9L0SWY1 (DYNLT2B, Equus caballus), https://rest.uniprot.org/uniprotkb/A0A9L0SWY1 (accessed 2026-10-26).
* [uniprot-Q8WW35]: UniProtKB/Swiss-Prot entry Q8WW35 (DYT2B_HUMAN), https://rest.uniprot.org/uniprotkb/Q8WW35 (accessed 2026-10-26).


## Citations

1. antony-2021-ciliary-dyneins-review-abstract.md
2. antony-2021-ciliary-dyneins-review-fulltext.txt
3. antony-2021-ciliary-dyneins-review-summary.md
4. asante-2014-dynein2-composition-abstract.md
5. asante-2014-dynein2-composition-fulltext.txt
6. asante-2014-dynein2-composition-summary.md
7. braschi-2022-dynein-nomenclature-abstract.md
8. braschi-2022-dynein-nomenclature-fulltext.txt
9. braschi-2022-dynein-nomenclature-summary.md
10. dibella-2004-tctex2b-i1-dynein-abstract.md
11. dibella-2004-tctex2b-i1-dynein-summary.md
12. ensembl-ENSECAG00000015913-lookup.json
13. ensembl-horse-DYNLT2B-isoforms.fasta
14. fu-2021-i1-ic-lc-structure-abstract.md
15. fu-2021-i1-ic-lc-structure-summary.md
16. gholkar-2015-tctex1d2-ciliogenesis-abstract.md
17. gholkar-2015-tctex1d2-ciliogenesis-fulltext.txt
18. gholkar-2015-tctex1d2-ciliogenesis-summary.md
19. hamada-2018-wdr60-tctex1d2-abstract.md
20. hamada-2018-wdr60-tctex1d2-fulltext.txt
21. hamada-2018-wdr60-tctex1d2-summary.md
22. harima-2025-tctex1d2-sperm-abstract.md
23. harima-2025-tctex1d2-sperm-fulltext.txt
24. harima-2025-tctex1d2-sperm-summary.md
25. hou-2015-dynein-ift-review-abstract.md
26. hou-2015-dynein-ift-review-summary.md
27. lee-2020-dynap-partitioning-abstract.md
28. lee-2020-dynap-partitioning-fulltext.txt
29. lee-2020-dynap-partitioning-summary.md
30. metadata.json
31. mukhopadhyay-2015-tctex1d2-commentary-abstract.md
32. mukhopadhyay-2015-tctex1d2-commentary-summary.md
33. mukhopadhyay-2024-dynein2-ic-tethering-abstract.md
34. mukhopadhyay-2024-dynein2-ic-tethering-fulltext.txt
35. mukhopadhyay-2024-dynein2-ic-tethering-summary.md
36. rao-2024-dynein-noncatalytic-review-abstract.md
37. rao-2024-dynein-noncatalytic-review-fulltext.txt
38. rao-2024-dynein-noncatalytic-review-summary.md
39. schmidts-2015-tctex1d2-jatd-abstract.md
40. schmidts-2015-tctex1d2-jatd-fulltext.txt
41. schmidts-2015-tctex1d2-jatd-summary.md
42. shimoda-2015-tctex1d2-glut4-abstract.md
43. shimoda-2015-tctex1d2-glut4-summary.md
44. toropova-2019-dynein2-structure-abstract.md
45. toropova-2019-dynein2-structure-fulltext.txt
46. toropova-2019-dynein2-structure-summary.md
47. uniprot-A0A9L0SWY1.fasta
48. uniprot-Q8WW35-entry.txt
49. uniprot-Q8WW35.fasta
50. wade-2009-horse-genome-abstract.md
51. wade-2009-horse-genome-summary.md
52. yamamoto-2021-chlamydomonas-ida-abstract.md
53. yamamoto-2021-chlamydomonas-ida-summary.md
54. zschocke-2017-tctex1d2-variable-expressivity-abstract.md
55. zschocke-2017-tctex1d2-variable-expressivity-summary.md