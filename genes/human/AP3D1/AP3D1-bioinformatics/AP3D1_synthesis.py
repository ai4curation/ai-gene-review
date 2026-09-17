"""Top-level synthesis for the AP3D1 review: description, references, core functions, gaps.

Reference *titles* are deliberately absent from this file. ``build_review.py``
reads each title out of the cached ``publications/PMID_*.md`` front matter, so a
title can never be written from memory and can never drift from the cache. What
is supplied here is only the reviewer judgement: relevance, correctness, notes.
"""

from __future__ import annotations

DESCRIPTION = (
    "AP3D1 encodes delta-adaptin, the large delta subunit of the heterotetrameric AP-3 adaptor "
    "protein complex. AP-3 (delta, a beta subunit, a mu subunit and a sigma subunit) is a "
    "cytosolic vesicle coat that is recruited to endosomal membranes by the GTP-bound form of the "
    "small GTPase ARF1, captures transmembrane cargo bearing dileucine- and tyrosine-based sorting "
    "signals, and polymerises into a tubular carrier that delivers that cargo to lysosomes and to "
    "lysosome-related organelles. Unlike the closely related AP-1 and AP-2 complexes, AP-3 does not "
    "require a clathrin lattice: its coat is built from rows of AP-3 arches cross-linked by ARF1 "
    "dimers. Within the complex, delta is the subunit that carries the primary ARF1 contact - two "
    "interfaces on its N-terminal HEAT-repeat trunk, both needed for the complex to stay on "
    "membranes - and, through a hinge in its long disordered linker, a dedicated binding site for "
    "the longin domain of the SNARE VAMP7, which AP-3 transports only when VAMP7 is engaged in a "
    "cis-SNARE complex. Delta also contributes, with the sigma subunit, to the dileucine cargo "
    "pocket. Delta is the only large subunit of AP-3 that is not duplicated in vertebrates: the "
    "ubiquitous complex uses beta-3A and the neuron-specific complex beta-3B, but both contain "
    "delta, so delta loss removes both forms. Characterised cargoes include LAMP1 and LAMP2, CD63, "
    "tyrosinase and TYRP1, VAMP7, CLN3, the zinc transporters ZnT2 and ZnT3, "
    "phosphatidylinositol-4-kinase type II alpha and, postsynaptically, AMPA receptors in complex "
    "with stargazin. Loss of delta-adaptin causes pigment-granule, platelet dense-granule, lytic-"
    "granule and synaptic-vesicle defects: it underlies the Drosophila garnet eye-colour mutant, "
    "the mouse mocha mutant, and human Hermansky-Pudlak syndrome type 10, in which oculocutaneous "
    "albinism and a platelet storage-pool defect are accompanied by neutropenia, impaired cytotoxic "
    "lymphocyte degranulation, seizures, neurodevelopmental delay and hearing loss."
)

# id -> (relevance, correctness, review_notes)
REFERENCE_REVIEWS: dict[str, tuple[str, str, str]] = {
    "GO_REF:0000002": ("LOW", "VERIFIED", "InterPro2GO. Two of its three uses here run through the delta-specific entries IPR010474 and IPR017105, which is as tight as an InterPro mapping gets; the third runs through IPR002553, a domain shared with all four adaptin large-subunit families, and can only support top-level terms."),
    "GO_REF:0000024": ("MEDIUM", "VERIFIED", "Curator sequence-similarity transfer. Both uses take mouse Ap3d1 (O54774) as donor, and human/mouse delta are reciprocal 1:1 orthologs in PTHR22781:SF12 that align residue-for-residue across the ARF1 and VAMP7 interfaces, so the similarity judgement is easy to sustain."),
    "GO_REF:0000033": ("HIGH", "VERIFIED", "PAINT/IBA. The ten IBA rows trace to exactly ten IBD rows in the committed PTHR22781 PAINT slice, split between a Eukaryota node (PTN000513025) and a Bilateria node (PTN000513028); every seed resolves to a real experimental annotation on an AP-3 delta ortholog. Nine of the ten are sound; only GO:0006896 carries a compartment that does not transfer to mammals."),
    "GO_REF:0000044": ("LOW", "VERIFIED", "UniProt subcellular-location keyword mapping. Both uses are faithful to the UniProt record; the Golgi-membrane statement it maps is itself flagged By similarity (ECO:0000250), which is why that row is kept as non-core."),
    "GO_REF:0000107": ("MEDIUM", "VERIFIED", "Ensembl Compara orthology transfer, mouse Ap3d1 -> human. Fourteen rows, all with the same donor pair (UniProtKB:O54774 plus its Ensembl translation ENSMUSP00000020420 - one donor under two identifiers). Most transfer genuine mouse experimental annotations; the GO:1990742 row transfers a donor annotation whose GO term is mis-scoped, and the GO:0035651 row transfers a part/whole inversion."),
    "GO_REF:0000117": ("LOW", "LOW_QUALITY", "ARBA machine-learned rules. Of the six uses, four fire on a single AP3D1-specific CATH FunFam (3.30.450.50:FF:000001) and give reasonable terms; one (ARBA00092758, GO:0010496 intercellular transport) gives a term with the wrong topology from the same evidence; and one (ARBA00028739, GO:0032502) cannot be reproduced from any of the rule's 893 published condition sets."),
    "GO_REF:0000120": ("MEDIUM", "VERIFIED", "Combined automated annotation. The five uses bundle ARBA and Ensembl arms; where they disagree in strength the Ensembl arm (mouse experimental donor) is the one carrying the claim, as noted per row."),

    "PMID:9151686": ("HIGH", "VERIFIED", "The paper that named AP-3 and identified delta as the p160 subunit, with an antibody raised against delta itself. Source of the Golgi-apparatus TAS, the intracellular-protein-transport TAS and the AP-3-complex NAS. Projects to only 14 distinct gene products in QuickGO, so it is a genuine subunit-level citation rather than a mass projection."),
    "PMID:9303295": ("HIGH", "VERIFIED", "Identified human delta-adaptin, showed it is an AP-3 subunit, and linked it to the Drosophila garnet pigment-granule phenotype. Cited for complex membership and for the melanosome/pigment-granule rows."),
    "PMID:9250663": ("MEDIUM", "VERIFIED", "Yeast suppressor screen defining the four subunits of yeast AP-3; the experimental grounding (IMP+IPI on APL5) behind the GO:0030123 IBD seed. Title foregrounds casein kinase suppression, which is why a symbol-based search does not find it."),
    "PMID:9335339": ("MEDIUM", "VERIFIED", "The yeast ALP-pathway screen; the IMP behind the GO:0006896 IBD seed. Correctly cited and scientifically sound - the reason the IBA is modified is that the Golgi-to-vacuole route it establishes is yeast-specific, not that the paper is wrong."),
    "PMID:9545220": ("MEDIUM", "DISPUTED", "Correctly cited for AP-3 binding clathrin, and the binding is real, but its functional inference ('AP-3 function in protein sorting may depend on clathrin') has been superseded: PMID:23761069 shows the association is dispensable and PMID:42139345 shows AP3:ARF1 builds carriers with no clathrin lattice. Also note the interaction it maps is beta3's appendage, not delta's."),
    "PMID:9679139": ("HIGH", "VERIFIED", "Established that ARF1 controls AP-3 membrane recruitment. Does not resolve which subunit, which the 2024/2026 structures do; cited as background to the NEW small-GTPase-binding row."),
    "PMID:9697856": ("HIGH", "VERIFIED", "The mocha mouse: a null allele of AP-3 delta linking endosomal transport to storage deficiency in platelets, melanosomes and synaptic vesicles. The single most important loss-of-function reference for this gene, and one the affinage record missed."),
    "PMID:11588176": ("MEDIUM", "VERIFIED", "Shows that only the NEURONAL form of AP-3 makes synaptic vesicles from endosomes in vitro - the result that makes the SV terms a beta-3B property shared with delta rather than a delta-specific one. The IDA/IMP behind the mouse GO:0016182 seed."),
    "PMID:15051738": ("HIGH", "VERIFIED", "Immuno-EM localisation of AP-3 to budding profiles on a tubular endosomal compartment, and the LAMP-1/LAMP-2 recycling phenotype. The central evidence that the mammalian AP-3 exit site is endosomal rather than Golgi."),
    "PMID:15109702": ("LOW", "VERIFIED", "A gravity-receptor study across five otoconia-deficient mouse strains, one of which is mocha; the IMP behind the mouse GO:0048840 annotation. Correctly cited, but it is a vestibular-physiology paper, not an AP-3 paper, so it says nothing about mechanism."),
    "PMID:15537701": ("HIGH", "VERIFIED", "The beta3A vs beta3B knockout comparison. Correctly cited and important, but it is also the source of the mis-scoped GO:0016183 synaptic-vesicle-coating NAS: nothing in the paper concerns clathrin-coated pits at the presynaptic membrane."),
    "PMID:15598649": ("MEDIUM", "VERIFIED", "CLN3 dileucine-motif binding to AP-1 and AP-3 and the sequential sorting requirement. The IPI partner (UniProtKB:Q13286) resolves to CLN3/battenin. Abstract-only in the cache."),
    "PMID:15860731": ("MEDIUM", "VERIFIED", "Vglut1/ZnT3 co-targeting in PC12 cells; the IMP behind the mouse GO:0048499 seed. Abstract-only in the cache."),
    "PMID:16162817": ("HIGH", "VERIFIED", "Direct localisation of AP-3 to clathrin-coated buds on tubular early endosomes in melanocytes, plus the tyrosinase mis-sorting phenotype. The IDA on human AP3D1 for endosome membrane, and one of the descendant evidences behind the PTN000513025 IBD. Abstract-only in the cache despite a PMC id (the publisher restricts full-text access)."),
    "PMID:16760431": ("MEDIUM", "DISPUTED", "Sound cell biology - AP-3 and BLOC-1 on shared small vesicles, and mistargeting of LAMP1, PI4KIIalpha and VAMP7-TI. What is disputed is the GO term derived from it: the paper's 'microvesicles' are intracellular transport intermediates, whereas GO:1990742 denotes an extracellular vesicle shed from the plasma membrane."),
    "PMID:17349999": ("MEDIUM", "VERIFIED", "AP3D1-specific siRNA in human fibroblastoid cells; the IMP behind GO:0140916. Correctly cited and methodologically sound - the objection is to the term, not the experiment, since the paper's own rescue result shows ZnT2 is the importer and AP-3 the delivery machinery."),
    "PMID:17895371": ("MEDIUM", "VERIFIED", "Yeast and mammalian NPC protein targeting via AP-3; the IMP behind the GO:0006623 IBD seed. Title foregrounds Niemann-Pick disease, which is why affinage did not surface it."),
    "PMID:17897319": ("LOW", "VERIFIED", "Placental lysosomal-membrane proteome. Correctly cited for the HDA, but it projects onto 242 distinct gene products, so it is a compartment survey."),
    "PMID:18634783": ("LOW", "VERIFIED", "Dictyostelium VAMP7 sorting by multiple AP complexes; the IDA behind the dictyBase seed of the GO:0030123 IBD. Interesting in retrospect, since the delta-VAMP7 link was later shown structurally in human."),
    "PMID:19010779": ("MEDIUM", "VERIFIED", "Crosslinking/MS of AP-3 complexes, identifying PI4KIIalpha and the BLOC complexes as AP-3 associates. The source of the mouse GO:0035651 IDA; the experiment supports the partners binding AP-3, which is why applying the term to a subunit of AP-3 is a role inversion."),
    "PMID:19144828": ("MEDIUM", "VERIFIED", "Early-endosomal compartments shared by synaptic-vesicle and lysosomal cargo with AP-3; the IDA behind the mouse GO:0098830 seed. Abstract-only in the cache."),
    "PMID:19946888": ("LOW", "LOW_QUALITY", "NK-cell membrane proteome. Correctly cited as an HDA, but a full QuickGO reference projection returns 1142 distinct gene products, and the paper itself notes that much of its catalogue is only transiently membrane-associated. Not informative about AP3D1."),
    "PMID:20089890": ("HIGH", "VERIFIED", "Quantitative immuno-EM placing most AP-3 in presynaptic axonal compartments and showing brain-region-specific control of synaptic-vesicle size by AP-3 and BLOC-1. The IDA behind four mouse localisation annotations transferred to human. Abstract-only in the cache."),
    "PMID:21998198": ("MEDIUM", "VERIFIED", "BLOC-1/AP-3 sorting of PI4KIIalpha from cell bodies to the synapse; the IMP behind the mouse GO:0008089 and GO:0048490 annotations."),
    "PMID:22511774": ("MEDIUM", "VERIFIED", "Rab32/Rab38 cooperation with AP-1, AP-3 and BLOC-2 in melanosome cargo delivery; the source of the GO:0035646 and GO:0072657 IMPs and, by inference, the GO:0032438 IC. Abstract-only in the cache, so the experimental detail behind the AP3D1 IMPs was not verifiable here and the curator is deferred to."),
    "PMID:22521722": ("HIGH", "VERIFIED", "The crystal structure of the delta-adaptin hinge bound to the VAMP7 longin domain (PDB 4AFI; UniProt maps chains A/B to O14617 680-729), with interface mutagenesis and rescue in mocha fibroblasts. The primary evidence for the NEW SNARE-binding row and the only structurally defined delta-specific cargo receptor."),
    "PMID:22539861": ("MEDIUM", "VERIFIED", "AP-1 and AP-3 requirement for generating synaptic vesicles from activity-dependent bulk endosomes in rat neurons; the IDA/IMP behind the rat RGD:1308659 seed of GO:0016182. Abstract-only in the cache."),
    "PMID:23247405": ("LOW", "VERIFIED", "A short review, correctly cited by ComplexPortal for four NAS rows. It projects onto 48 distinct gene products, so it is a general-machinery citation; its statements about AP-3 are accurate but second-hand, and the platelet dense-granule claim in particular is about HPS generally rather than about AP-3 directly."),
    "PMID:23761069": ("HIGH", "VERIFIED", "Acute chemical-genetic inactivation of clathrin leaving AP-3 endosomal budding intact. The decisive functional test against the clathrin-dependence premise of GO:0035654."),
    "PMID:24217640": ("MEDIUM", "VERIFIED", "Stargazin-AP-3A routing of AMPA receptors to late endosomes/lysosomes during LTD; the IDA/IEP/IMP behind the mouse GO:0098943 and GO:0098978 annotations and the postsynaptic localisation. Abstract-only in the cache."),
    "PMID:26744459": ("HIGH", "VERIFIED", "The HPS10 paper: homozygous AP3D1 mutation, AP-3 destabilisation, impaired CD8+ T-cell and NK-cell degranulation, and full rescue by retroviral AP3D1 reconstitution. Primary evidence for both NEW degranulation rows and the source of UniProt's FUNCTION and DISEASE blocks. Full text available."),
    "PMID:30472485": ("MEDIUM", "VERIFIED", "Second HPS10 family, confirming the platelet storage-pool defect that the first report could not assess. Abstract-only in the cache but the abstract states the platelet finding directly."),
    "PMID:33886957": ("HIGH", "VERIFIED", "Shows in melanocytes that sorting of the STX13-VAMP7 cis-SNARE complex into transport carriers requires recognition of VAMP7 by the AP-3 delta subunit or of STX13 by BLOC-1 pallidin. The in vivo counterpart to the 4AFI structure; supports the NEW SNARE-binding row."),
    "PMID:36445457": ("MEDIUM", "VERIFIED", "A homozygous AP3D1 missense variant presenting as sensorineural hearing loss, extending the HPS10 phenotypic spectrum. Cited as corroboration for the inner-ear/otolith row rather than as its basis."),
    "PMID:39705307": ("HIGH", "VERIFIED", "Cryo-EM of reconstituted human AP-3 with Arf1 and cargo, including the hemicomplex pulldowns that localise the primary Arf1 site to delta and the stepwise activation series. PDB 9C58/9C59/9C5B/9C5C map to O14617, confirming human numbering."),
    "PMID:42139345": ("HIGH", "VERIFIED", "Cryo-ET of the AP3:ARF1 coat, naming both delta ARF1 interfaces by residue, testing them in HeLa cells, and demonstrating carrier formation without a clathrin lattice. The basis for the NEW small-GTPase-binding row, the GO:0035654 modification and the NEW lysosomal-targeting row."),

    "PMID:31268833": ("MEDIUM", "VERIFIED", "AP-3 is required for Vangl2 trafficking and inner-ear planar cell polarity in mouse. Cited only in a knowledge gap, as the current best lead for the cochlear cargo; it does not support any annotation in this review."),

    "file:human/AP3D1/AP3D1-uniprot.txt": ("HIGH", "VERIFIED", "UniProt O14617 (AP3D1_HUMAN, entry version 224, 1153 aa). Accession and identifier checked against the fetched record, so this is not a merged-accession redirect. Quoted for complex composition and for the HPS10 disease statement."),
    "file:human/AP3D1/AP3D1-bioinformatics/RESULTS.md": ("MEDIUM", "VERIFIED", "This review's own reproducible analysis: MAFFT conservation of the three mapped delta interfaces across the PTHR22781 family versus out-of-family adaptin large subunits, plus the GOA-to-YAML reconciliation. Scripts fetch live from UniProt and assert every claimed residue before aligning."),
    "file:human/AP3D1/AP3D1-deep-research-affinage.md": ("LOW", "VERIFIED", "Affinage LLM deep-research record. Trust gates clear (.affinage.log), self_evaluation_pairwise 'win', faith 100%, and the narrative is genuinely about AP-3 delta with no symbol collision - its recent-cargo material (IFNGR1/OPTN, DRAM2, RNF13, TGFbeta2, zebrafish crasher) is useful context. Marked LOW relevance because it is precision-not-recall: it missed the mocha mouse, the garnet/delta-adaptin discovery, the entire AP-3 structural literature (both the ARF1 and VAMP7 interfaces), the clathrin papers and every PAINT donor paper. No claim in this review rests on it; the ones it suggested were re-verified against their own PMIDs."),
}

CORE_FUNCTIONS = [
    dict(
        description=(
            "As the delta subunit of AP-3, contributes to the complex's cargo-adaptor activity: "
            "AP-3 binds sorting signals in the cytosolic tails of transmembrane cargo and links them "
            "to a self-assembling coat, concentrating the cargo into a carrier. Delta's own "
            "contribution is the dileucine-binding surface it forms with sigma-3 and, in the hinge of "
            "its disordered linker, a separate receptor that binds the longin domain of VAMP7 when "
            "that SNARE is in a cis-SNARE complex."
        ),
        contributes_to_molecular_function=("GO:0140312", "cargo adaptor activity"),
        molecular_function=("GO:0000149", "SNARE binding"),
        directly_involved_in=[
            ("GO:0006622", "protein targeting to lysosome"),
            ("GO:0008333", "endosome to lysosome transport"),
        ],
        locations=[("GO:0010008", "endosome membrane")],
        in_complex=("GO:0030123", "AP-3 adaptor complex"),
        supported_by=[
            ("PMID:22521722", "We show that the linker of the δ-adaptin subunit of AP3 binds the VAMP7 longin domain and determines the structure of their complex."),
            ("PMID:33886957", "Sorting requires either recognition of VAMP7 by the AP-3δ subunit of AP-3 or of STX13 by the pallidin subunit of BLOC-1, but not both."),
            ("PMID:42139345", "The known cargo binding sites on C-μ3 and σ3/δ are adjacent to the membrane, and the electron microscopy density suggests that they are occupied by cargo"),
        ],
    ),
    dict(
        description=(
            "Binds ARF1-GTP through two interfaces on its N-terminal HEAT-repeat trunk. This is the "
            "primary ARF1 contact of the whole complex - the delta-sigma3 hemicomplex binds ARF1 "
            "almost as well as intact AP-3, while the beta3-mu3 hemicomplex barely binds at all - and "
            "it is what recruits and retains AP-3 on the endosomal membrane. Mutating either "
            "interface in human cells sends delta back to the cytosol."
        ),
        molecular_function=("GO:0031267", "small GTPase binding"),
        directly_involved_in=[("GO:0006901", "vesicle coating")],
        locations=[("GO:0010008", "endosome membrane"), ("GO:0005737", "cytoplasm")],
        in_complex=("GO:0030123", "AP-3 adaptor complex"),
        supported_by=[
            ("PMID:39705307", "This suggests that the primary Arf1 binding site on AP-3 is on δ"),
            ("PMID:42139345", "These data indicate that δ requires both ARF1 interfaces for correct membrane recruitment"),
            ("PMID:9679139", "we demonstrate that membrane association of the recently described AP-3 adaptor is regulated by ARF1"),
        ],
    ),
    dict(
        description=(
            "Contributes to assembly of the AP-3 membrane coat. Once two ARF1 molecules are bound and "
            "cargo is engaged, AP-3 dimerises and polymerises into spiralling rows of arches "
            "cross-linked by ARF1 dimers, tubulating the donor membrane into a carrier. The coat "
            "requires no clathrin lattice, which distinguishes AP-3 from AP-1 and AP-2; breaking the "
            "lattice interfaces by point mutation abolishes carrier formation and lysosomal cargo "
            "delivery in human cells."
        ),
        contributes_to_molecular_function=("GO:0140312", "cargo adaptor activity"),
        directly_involved_in=[
            ("GO:0006901", "vesicle coating"),
            ("GO:0035459", "vesicle cargo loading"),
        ],
        locations=[("GO:0010008", "endosome membrane")],
        in_complex=("GO:0030123", "AP-3 adaptor complex"),
        supported_by=[
            ("PMID:42139345", "we demonstrate that AP3:ARF1 spontaneously remodels membranes containing cargo and the phosphoinositide PI(3,5)P2 into tubular structures coated in spiraling rows of AP3 arches and ARF1 dimers"),
            ("PMID:42139345", "By demonstrating that AP3:ARF1 can generate carriers without using a clathrin lattice, we explain the clathrin independence of AP3-mediated trafficking."),
            ("PMID:39705307", "Finally, binding of the second Arf1 molecule provides the template for AP-3 dimerization, providing a glimpse into the first step of coat polymerization."),
        ],
    ),
    dict(
        description=(
            "Required for the integrity of AP-3 itself, and therefore for both the ubiquitous "
            "(beta-3A) and the neuronal (beta-3B) complexes. Loss of delta destabilises the whole "
            "heterotetramer in mouse mocha fibroblasts and in HPS10 patient cells, and re-expression "
            "of wild-type delta restores complex formation and function. This non-redundancy is why "
            "delta loss produces a combined pigmentary, platelet, immune and neurological phenotype "
            "while loss of beta-3A alone (HPS2) spares the nervous system."
        ),
        contributes_to_molecular_function=("GO:0140312", "cargo adaptor activity"),
        molecular_function=("GO:0005198", "structural molecule activity"),
        directly_involved_in=[("GO:0006901", "vesicle coating")],
        locations=[("GO:0010008", "endosome membrane")],
        in_complex=("GO:0030123", "AP-3 adaptor complex"),
        supported_by=[
            ("PMID:22521722", "The absence of δ-adaptin causes destabilization of the AP3 complex in mouse mocha fibroblasts and mislocalization of VAMP7."),
            ("PMID:26744459", "AP3D1 codes for the AP3δ subunit of the complex, which is essential for both forms."),
            ("PMID:26744459", "AP3 complex formation and the degranulation defect in patient T cells were restored by retroviral reconstitution."),
        ],
    ),
]

KNOWLEDGE_GAPS = [
    dict(
        gap_statement=(
            "It is not established whether the amphipathic helix at the delta N-terminus actually "
            "deforms the membrane or merely binds it. Both structural papers stop at a proposal, and "
            "the 2026 coat paper attributes the helix array to mu3 'and possibly' delta."
        ),
        boundary=(
            "What is established: AP-3 has low intrinsic membrane affinity and is recruited by "
            "ARF1-GTP through delta; the AP3:ARF1 coat does tubulate liposomes in vitro; and AlphaFold "
            "plus cryo-EM density support a helical N-terminal extension on delta in a position "
            "analogous to membrane-binding regions of other AP complexes."
        ),
        gap_kind=["BIOLOGY"],
        dark_aspect="MF_DARK",
        status="OPEN",
        significance=(
            "It decides whether delta contributes an active membrane-bending activity "
            "(GO:0180020) or only a recruitment and cargo-capture function. Asserting the former "
            "from the current evidence would be an over-annotation, so the term is deliberately not "
            "proposed in this review."
        ),
        resolution=(
            "Helix-deleted and hydrophobic-face-mutant delta in a liposome tubulation assay with "
            "purified AP-3 and ARF1, read out by cryo-ET, separating tubulation from recruitment."
        ),
        provenance=[
            ("PMID:42139345", "Our AP3:ARF1 coat structure also suggests that there is an additional array of amphipathic helices is contributed by μ3 and possibly by δ."),
        ],
    ),
    dict(
        gap_statement=(
            "Whether mammalian AP-3 has a functional trans-Golgi pool that performs the "
            "Golgi-to-lysosome route its yeast ortholog performs, or whether the tubular sorting "
            "endosome is the only productive site, is unresolved."
        ),
        boundary=(
            "Established: yeast AP-3 buds alkaline phosphatase and Vam3p from the late Golgi; "
            "mammalian AP-3 is caught by immuno-EM budding from a tubular endosomal compartment and "
            "concentrates LAMP-1/LAMP-2 there; anti-delta immunofluorescence nevertheless shows a "
            "Golgi-region signal as well as peripheral structures."
        ),
        gap_kind=["BIOLOGY", "CURATION"],
        dark_aspect="BP_DARK",
        status="NARROWING",
        significance=(
            "It is the reason GO:0006896 Golgi to vacuole transport is propagated onto human AP3D1 "
            "from a yeast-seeded node. If a mammalian TGN pool is productive the IBA is fine as it "
            "stands; if not, the human annotation should be the endosomal route."
        ),
        resolution=(
            "Compartment-restricted acute depletion - e.g. TGN-anchored versus endosome-anchored "
            "ARF1-GAP recruitment, or a nanobody-based delta trap targeted to one compartment - with "
            "readout of newly synthesised LAMP1 arrival at lysosomes."
        ),
        provenance=[
            ("PMID:15051738", "The adaptor protein (AP) 3 adaptor complex has been implicated in the transport of lysosomal membrane proteins, but its precise site of action has remained controversial."),
            ("PMID:9151686", "These peripheral structures show only limited colocalization with endosomal markers and may correspond to a postTGN biosynthetic compartment."),
        ],
    ),
    dict(
        gap_statement=(
            "No function is assigned to the ~200-residue disordered, heavily phosphorylated region of "
            "delta C-terminal to the VAMP7-binding hinge (UniProt REGION 726-920, with phosphoserines "
            "at S758, S759 and elsewhere). It is not known what phosphorylates it or what the "
            "modification changes."
        ),
        boundary=(
            "Established: the trunk (HEAT repeats 1-11, residues 34-585) carries the ARF1 and "
            "dileucine sites; the hinge at 680-729 binds VAMP7; the C-terminal appendage is the ear. "
            "The region between hinge and ear is disordered by MobiDB-lite and is the densest "
            "phosphosite cluster in the protein."
        ),
        gap_kind=["BIOLOGY"],
        dark_aspect="RESIDUAL_SUBGAP",
        status="OPEN",
        significance=(
            "AP-1 and AP-2 are regulated by conformational switching that AP-3 does not use - AP-3 is "
            "constitutively open - so whatever tunes AP-3 activity must be something else, and a "
            "phosphorylated linker adjacent to the cargo-binding hinge is the obvious candidate."
        ),
        resolution=(
            "Phosphosite mapping on endosome-bound versus cytosolic AP-3, then phospho-null and "
            "phospho-mimetic delta in a VAMP7-sorting and LAMP1-delivery assay."
        ),
        provenance=[
            ("PMID:39705307", "A structural explanation for why AP-3 is natively open is unclear."),
            ("file:human/AP3D1/AP3D1-uniprot.txt", "FT   REGION          726..920"),
        ],
    ),
    dict(
        gap_statement=(
            "The cargo whose mis-sorting causes the hearing loss in AP3D1-deficient humans and the "
            "otoconial and inner-ear defects in mocha mice has not been identified."
        ),
        boundary=(
            "Established: mocha mice have inner-ear degeneration and graded otoconial deficits; HPS10 "
            "includes impaired hearing, and one family presents with sensorineural hearing loss as "
            "the leading manifestation; AP-3 is required for Vangl2 trafficking and inner-ear planar "
            "cell polarity in mouse."
        ),
        gap_kind=["BIOLOGY"],
        dark_aspect="BP_DARK",
        status="NARROWING",
        significance=(
            "Hearing loss is a presenting feature that can occur without the classic albinism-plus-"
            "bleeding picture, so it changes who gets tested for AP3D1 variants."
        ),
        resolution=(
            "Cochlear and vestibular proteomics of conditional Ap3d1-null inner ear, prioritising "
            "dileucine-motif transmembrane proteins, with Vangl2 as the current lead."
        ),
        provenance=[
            ("PMID:36445457", "Loss-of-function variants in AP3D1 have been linked to Hermansky-Pudlak syndrome (HPS) 10, a severe multisystem disorder characterized by oculocutaneous albinism, immunodeficiency, neurodevelopmental delay, hearing loss (HL), and neurological abnormalities, fatal in early childhood."),
            ("PMID:31268833", "However, the machinery that regulates the asymmetric partition of PCP proteins remains largely unknown."),
        ],
    ),
    dict(
        gap_statement=(
            "Why BLOC-1 controls AP-3-dependent synaptic-vesicle biogenesis in the dentate gyrus but "
            "not in the striatum is unknown, even though both complexes are ubiquitously expressed."
        ),
        boundary=(
            "Established: AP-3 and BLOC-1 physically associate, share vesicles and cargo, and form a "
            "super-complex that sorts a cis-SNARE complex; loss of AP-3 decreases synaptic-vesicle "
            "size in striatum but increases it in dentate gyrus; BLOC-1 loss reduces presynaptic AP-3 "
            "in dentate gyrus only."
        ),
        gap_kind=["BIOLOGY"],
        dark_aspect="BP_DARK",
        status="OPEN",
        significance=(
            "It is the clearest evidence that AP-3 output is regulated by something other than its "
            "own subunit composition, and it bears on the dysbindin/BLOC-1 link to schizophrenia."
        ),
        resolution=(
            "Region-resolved comparison of the AP-3 interactome and cargo repertoire between striatum "
            "and dentate gyrus in wild-type and BLOC-1-null mice."
        ),
        provenance=[
            ("PMID:20089890", "However, here we report that AP-3 and BLOC-1 differentially regulate the composition of presynaptic terminals in the striatum and dentate gyrus of the hippocampus."),
        ],
    ),
]

SUGGESTED_QUESTIONS = [
    dict(
        question=(
            "Does the delta N-terminal amphipathic helix contribute membrane-bending activity to the "
            "AP3:ARF1 coat, or is its role limited to membrane association? The 2024 and 2026 "
            "structures reach opposite degrees of confidence on this."
        ),
        experts=["Baker RW", "Briggs JAG", "Owen DJ"],
    ),
    dict(
        question=(
            "In mammalian cells, is there a productive trans-Golgi pool of AP-3, or is the tubular "
            "sorting endosome the only site where AP-3 makes carriers?"
        ),
        experts=["Peden AA", "Klumperman J", "Bonifacino JS"],
    ),
    dict(
        question=(
            "AP-3 is constitutively open, unlike AP-1 and AP-2, so what regulates when and where it "
            "engages cargo? Is the phosphorylated disordered linker of delta the switch?"
        ),
        experts=["Ungermann C", "Raunser S", "Baker RW"],
    ),
    dict(
        question=(
            "Beyond VAMP7, which cargoes does the delta hinge itself select, as opposed to the "
            "dileucine and YxxPhi cargoes captured by the sigma3/delta and mu3 sites?"
        ),
        experts=["Owen DJ", "Marks MS", "Peden AA"],
    ),
    dict(
        question=(
            "Which AP-3 cargo underlies the cochlear phenotype of HPS10 patients and the otoconial "
            "deficit of mocha mice - is Vangl2 sufficient to explain it?"
        ),
        experts=["Faundez V", "Chen P", "Parzefall T"],
    ),
]

SUGGESTED_EXPERIMENTS = [
    dict(
        hypothesis=(
            "The delta N-terminal amphipathic helix inserts into the outer leaflet and contributes to "
            "membrane deformation, so removing it will uncouple AP-3 recruitment from tubulation."
        ),
        description=(
            "Purify human AP-3 carrying wild-type delta, a helix-deleted delta, and a delta whose "
            "helix hydrophobic face is mutated to serine. Reconstitute with myristoylated ARF1-GTP on "
            "PI(3,5)P2-containing, cargo-bearing liposomes and score, by cryo-electron tomography, "
            "recruitment (AP-3 density per unit membrane) and tubulation (fraction of tubulated "
            "membrane, tube radius) as separate readouts. Wild-type delta and an ARF1-site-2 mutant "
            "are the positive and recruitment-null controls."
        ),
        experiment_type="in vitro reconstitution and cryo-electron tomography",
    ),
    dict(
        hypothesis=(
            "The mammalian AP-3 budding step happens only on tubular sorting endosomes, so removing "
            "AP-3 selectively from the trans-Golgi will not delay lysosomal delivery of newly "
            "synthesised LAMP1."
        ),
        description=(
            "In HeLa cells with endogenous AP3D1 knocked out, re-express delta fused to an "
            "FKBP-rapamycin dimerisation module and acutely sequester it either at a TGN-anchored or "
            "at an endosome-anchored FRB. Follow a RUSH-released LAMP1-SBP-GFP reporter to lysosomes "
            "by live imaging. Rescue with untagged delta and with the ARF1 double-site mutant give "
            "the response range."
        ),
        experiment_type="acute compartment-selective depletion with synchronised cargo release",
    ),
    dict(
        hypothesis=(
            "Phosphorylation of the delta linker (S758/S759 and neighbouring sites) gates cargo "
            "capture rather than membrane recruitment."
        ),
        description=(
            "Map phosphosites by mass spectrometry on delta purified from cytosolic versus "
            "membrane-bound AP-3 fractions. Then complement AP3D1-knockout cells with phospho-null "
            "and phospho-mimetic delta and measure, separately, membrane recruitment (delta puncta "
            "per cell) and cargo capture (co-immunoprecipitation of VAMP7 and LAMP1, and lysosomal "
            "delivery of each)."
        ),
        experiment_type="phosphoproteomics with phospho-mutant complementation",
    ),
    dict(
        hypothesis=(
            "The delta hinge selects additional SNARE or SNARE-complex cargoes beyond VAMP7, which "
            "would explain why delta-specific and complex-wide phenotypes differ."
        ),
        description=(
            "Use the delta hinge (residues 650-797) and the VAMP7-non-binding mut1/mut2 versions as "
            "baits in a proximity-labelling (TurboID) experiment in cells, and in parallel as GST "
            "baits against brain and melanocyte cytosol. Hits enriched on wild-type but not mut1/mut2 "
            "are candidate hinge cargoes; validate the top hits by testing whether their lysosomal "
            "delivery is rescued by wild-type but not by mut1/mut2 delta in AP3D1-knockout cells."
        ),
        experiment_type="interface-mutant differential proximity labelling and pulldown",
    ),
    dict(
        hypothesis=(
            "The hearing loss of AP3D1 deficiency is caused by mis-sorting of a specific "
            "dileucine-motif transmembrane cargo in the cochlea, with Vangl2 the leading candidate."
        ),
        description=(
            "Compare the surface and lysosomal proteomes of cochlear and vestibular epithelium from "
            "conditional Ap3d1-null and control mice at the onset of the phenotype, filtering for "
            "transmembrane proteins with cytosolic [DE]xxxL[LI] motifs. Test the top candidates plus "
            "Vangl2 for AP-3-dependent localisation, and for rescue of the polarity defect by "
            "motif-mutant versions that bypass AP-3."
        ),
        experiment_type="tissue-restricted knockout proteomics with candidate validation",
    ),
]
