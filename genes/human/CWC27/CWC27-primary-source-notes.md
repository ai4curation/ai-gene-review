# CWC27: primary experimental evidence and public locators

This guide distinguishes observed CWC27 results from interpretation. The linked papers are the primary evidence; this authored guide and the [source index](CWC27-source-evidence.json) provide navigation. Original publication caches are unchanged. The 2002 and 2021 caches contain abstracts, so public copies of the original articles are linked below. Selected relevant main sections were read; this is not a claim to have read every supplementary experiment.

## Post-first-step target detection: PMID:11991638

[Jurica et al., 2002](https://doi.org/10.1017/S1355838202021088); [author-hosted original PDF](https://grigoriefflab.umassmed.edu/sites/default/files/Jurica_RNA2002.pdf).

The decisive target entry is Table 1, printed p.431 (PDF p.6). NY-CO-10, accession O60529, has five unique peptides in the C column and a dash in H. O60529 is a secondary accession of human CWC27/Q6UX04 in the official record. The table and its unique-peptide footnote were visually inspected. This is positive target identification, not a claim that the peptide count measures abundance or resolves the two official splice products.

Purification Results on printed p.428 (PDF p.3) describe an AG-to-GG 3′ splice-site mutation that arrests before the second catalytic step, followed by RNase H depletion of earlier complexes. The affinity eluate contains equimolar exon and lariat intermediates comprising 75–85% of labeled RNA. The separate glycerol-gradient characterization on pp.429–430 (PDF pp.4–5) reports 96% at its peak. Those are RNA measurements at different stages, not CWC27 purity; the target MS result is not specifically assigned to that gradient peak. The MS Results on p.430 and Methods on p.437 (PDF p.12) describe excised SDS-PAGE sections, trypsin digestion and LC-MS/MS. The H preparation lacks ATP/creatine phosphate and is assembled on ice.

These observations support contextual C-complex membership. Later Bact structures do not, by themselves, demonstrate that the earlier target peptides were contamination. The reason for the differing occupancy remains unresolved.

## Pre-branching minor Bact: PMID:33509932

[Bai et al., 2021](https://doi.org/10.1126/science.abg0879); [author-hosted early-release PDF](https://zhanglab.net/files/2021_Science.pdf). The page numbers here refer to the early-release PDF, whose footer explicitly states that pagination was not final.

Results on pp.1–2 describe a HeLa-extract minor-spliceosome preparation in which MINX-U12 is truncated 18 nucleotides beyond the branch-point sequence. Removing the PRP2-binding region prevents its remodeling and enriches a pre-branching Bact state. Page 2 lists 45 modeled proteins and explicitly includes CWC27/NY-CO-10. Figure 1A's component list on p.12 also includes CWC27; its caption on p.13 distinguishes the gray dashed boxes for absent major-spliceosome components. That component list was visually inspected. The Methods on p.6 detail substrate construction, 4-hour assembly, affinity purification and glycerol-gradient stabilization.

The paper's use of a PPI class name is not a catalytic assay of CWC27. Its preparation supports U12-type spliceosomal membership, while the existing post-first-cleavage term GO:0071018 is too specific for this source. The broader replacement GO:0005689 preserves the demonstrated membership; no activity is transferred from PPIL2, PRP2 or the RNA catalytic center.

## Catalytic inactivity and the folding inference: PMID:20676357

[Human cyclophilin-family experiments](https://pmc.ncbi.nlm.nih.gov/articles/PMC2911226/), main Results on substrate/CsA assays, supplementary Figure S1 caption (pbio.1000439.s002), and NMR Methods.

The human SDCCAG-10/CWC27 cyclophilin domain does not accelerate the tested AAPF, AFPF or AGPF cis–trans exchanges. The NMR setup uses 0.075 mM protein and 2 mM substrate at 25°C, with phosphate buffer at pH 7. Peptide-associated chemical shifts nevertheless show positive binding. Thus the existing NOT PPIase annotation retains its actual assay scope. Active-site comparisons and a PPIA mutant are not a CWC27 rescue establishing sole causation by one residue. Exact Text S2 domain endpoints and figure pixels were not independently inspected.

The [IPR020892 conserved-site mapping](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR020892/) includes protein folding and PPIase activity, while its family description also mentions noncatalytic chaperone function. CWC27-specific folding has not been demonstrated by these peptide assays or by CWC22 stabilization. The broad process inference is therefore over-annotated at the available target evidence; this is not a demonstration that every possible noncatalytic folding role is absent.

## Direct CWC22 binding and product specificity: PMID:32329775

[Human CWC27/CWC22 reconstitution and structure](https://pmc.ncbi.nlm.nih.gov/articles/PMC7261170/), recombinant-protein Methods, Figure 3 and associated Results, and the following minimal-complex structural Results.

The Methods identify full-length human CWC27, Q6UX04 residues 1–472, expressed in bacteria, alongside CWC22-S residues 100–665. Reciprocal affinity retention establishes direct CWC27–CWC22 binding with or without EIF4A3. The tested CWC27 C-terminal segment 354–472 also binds. The 390-residue Q6UX04-2 product is explicitly tested and fails CWC22 retention. The minimal structure resolves a C-terminal CWC27 helix against the CWC22 MIF4G domain, on the side opposite EIF4A3, with no direct CWC27–EIF4A3 contact. No figure-pixel or complete SI read is claimed here.

These experiments justify a NEW GO:1990935 splicing-factor-binding IPI scoped to Q6UX04-1. They do not imply equal function of both products. CWC27 enhances the CWC22-associated assembly, but an isolated direct EIF4A3 interaction is not established; no broader adaptor activity is added. The existing core molecular function and the new annotation describe the same measured function, not two independent activities.

## Transient major-spliceosome occupancy: PMID:29360106 and PMID:39068178

[2018 major Bact structures](https://pmc.ncbi.nlm.nih.gov/articles/PMC5835773/), Results comparing early/mature/late states and Figure 3 discussion: CWC27/NY-CO-10 is strongest early, weaker mature and absent late. In the mature complex, the endonuclease-like domain of PRP8 contacts NY-CO-10. The shortened MINX-15 preparation and remodeling interpretation are described in the Methods and transition model. CWC27 is not assigned RNF113A's RNA-contact function.

[2024 activation series](https://pmc.ncbi.nlm.nih.gov/articles/PMC11283556/), Results and Figure 4 caption: CWC27 is recruited in Bact-I and released in Bact-II. These state series establish transient activated-spliceosome occupancy, but their labels are not forced into a universal dissociation time. They do not make the target a member of every intermediate enumerated in either paper. Selected main text and caption text were read, not the complete supplementary protein tables or image pixels.

## Positive recruitment-module evidence: PMID:42635127

[2026 cellular EJC assembly study](https://pmc.ncbi.nlm.nih.gov/articles/PMC13501132/), main HEK293T coIP/RNase Methods and the Results on pladienolide B inhibition, CWC27/CWC22 and EJC components.

CWC27 and CWC22 remain associated with EIF4A3 under treatment that blocks spliceosome assembly before pre-B. CWC27 also co-precipitates with HA-tagged RBM8A and MAGOH. These findings positively corroborate a CWC27–CWC22 module associated with EIF4A3 recruitment and EJC components, while showing that some associations can precede spliceosome activation. The proposed routes and conformational changes are models. CoIP in cells does not establish a direct binary CWC27–EIF4A3 interface or equivalent activity of both official products. Selected main text and captions were read; no complete SI or image-pixel read is claimed.
