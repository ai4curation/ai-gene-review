# Hmt-1 evidence notes

Q9VF20 is the 866-residue PA product of FBgn0038376 (AAF55241/NP_650503), the single currently annotated protein. [FlyBase](https://flybase.org/reports/FBgn0038376). The exact source sequence has the ABCB6 N-terminal domain (IPR032410), transmembrane ABC domain and ABC nucleotide-binding cassette; it is not identified solely by its automated full name.

[PMID:19001374](https://pubmed.ncbi.nlm.nih.gov/19001374/) directly studies DmHMT-1 expressed in Schizosaccharomyces pombe. The abstract states that it “suppresses the Cd2+ hypersensitivity of S. pombe hmt-1 mutants and localizes to the vacuolar membrane but does not transport Cd.PC complexes.” This supports the existing IGI detoxification and IDA localization annotations with the explicit heterologous-system qualification. The cache remains abstract-only after a forced retrieval attempt; no full-text assay details are invented. In particular, cadmium tolerance is not equated with transport of free Cd2+ or a phytochelatin complex.

[PMID:35950458](https://pmc.ncbi.nlm.nih.gov/articles/PMC9385563/) is cached with full text. It resolves human ABCB6 with coproporphyrin III and hemin, including hemin coordinated with glutathione. This gives substrate-level biological grounding for the curated ABCB6 ancestral assignment, supported by target family architecture. Heme binding/transport is retained as a non-core conserved capability; the best demonstrated target role is cadmium tolerance. Broad ProtNLM ABC transporter activity is therefore LSP relative to the supported family-specific activity, rather than uncertain simply because the exact fly physiological solute is unknown.

The extensive automated location list is not treated as ten independent observations. Yeast vacuolar targeting does not establish extracellular, mitochondrial, Golgi, ER, plasma-membrane or individual endosomal locations in the fly. These specific rows remain UNDECIDED pending target localization or a conserved targeting mechanism. Lysosomal membrane is plausible as a homologous compartment, but the experiment itself uses a yeast vacuole; the existing vacuolar annotation is the resolved level.

The Falcon report completed and was inspected. It correctly separates yeast-complementation evidence from native fly localization and emphasizes unresolved metal speciation. Its heme discussion lacks the substrate-resolved 2022 ABCB6 study used here, so the review retains a qualified conserved heme-handling capability rather than requiring a new fly assay for every family property. The provider's broad metal-selectivity discussion is not imported: in the cached primary abstract, the Hg/As comparison is explicitly about SpHMT-1-deficient cells. The provider's 2024 cadmium-structure lead is useful, but not counted as a replicated DmHMT-1 transport experiment.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this pass; everything below rests on the primary literature, PAINT and the UniProt/FlyBase records.

### Identity
- Q9VF20 is the canonical full-length product of FBgn0038376 (CG4225): 866 aa, starts with Met, single annotated polypeptide (FlyBase: "There is only one protein coding transcript and one polypeptide associated with this gene"). Not a fragment, isoform or alternative gene model. Architecture: ABCB6_N/TMD0 (IPR032410, Pfam MTABC_N), ABC transmembrane type-1 domain (252-542), ABC cassette (576-810, PROSITE ABC signature), 10 Phobius TM helices.
- PANTHER PTHR24221:SF654 (ABCB6). PAINT: PTN008609345 (Opisthokonta) vacuolar membrane, seeded by fly, rat, human, worm; PTN001199916 (Eumetazoa, taxon 6072) ABC-type heme transporter activity, heme binding, heme transport, seeded by human ABCB6 Q9NP58 only. Hmt-1 lies inside both clades.

### Literature
- PMID:19001374 (abstract only): DmHMT-1 complements S. pombe hmt-1 Cd2+ hypersensitivity, localizes to the yeast vacuolar membrane, does not transport Cd.PC; the fly genome lacks PCS, so the role is PC-independent ["invoke a PC-independent role for these transporters in Cd2+ detoxification"].
- PMID:38822018 (full text, newly cached): human ABCB6 core binds Cd(II):GSH and Cd(II):PC2; Cd:GSH stimulates ATPase, E752Q abolishes it, and active ABCB6 protects Sf9 cells from Cd ["also functions as a heavy metal efflux pump"]. So the cadmium role is shared across the clade, not a fly oddity.
- PMID:35950458: human ABCB6 structures with CPIII and hemin; hemin:GSH stimulates ATPase about sixfold.
- PMID:17006453 (newly cached): ABCB6 as a mitochondrial outer-membrane porphyrin uptake transporter. PMID:22655043 (newly cached): endogenous ABCB6 is endo/lysosomal, absent from mitochondria, and in the erythrocyte plasma membrane and reticulocyte exosomes. Mitochondrial localization is therefore disputed even in mammals.

### Changes from the previous review
- Heme terms: ABC-type heme transporter activity (IBA + IEA) moved from KEEP_AS_NON_CORE to ACCEPT, and made a second core function, because the PAINT IBD at the eumetazoan node is a phylogenetic judgement that Hmt-1 falls under, with no fly evidence of loss. It is flagged as untested in the fly. Heme binding stays non-core. Heme transport (IBA) is MODIFY to heme transmembrane transport (its is_a child, already on the gene).
- Generic transmembrane transport (IBA + IEA): ACCEPT changed to MODIFY → heme transmembrane transport (rule: correct but general = MODIFY).
- Locations from ARBA SubCell rules (copied from mammalian ABCB6's itinerary): extracellular region REMOVE (multipass membrane protein; mammalian basis is reticulocyte exosomes); mitochondrial outer membrane, Golgi, ER, plasma membrane MARK_AS_OVER_ANNOTATED (PAINT curators propagated only vacuolar membrane; mammalian evidence contested or erythrocyte-specific); lysosomal, endosome, early/late endosome, MVB membranes left UNDECIDED (plausible on the endolysosomal route, untested in fly).
- Core MF for cadmium kept at ABC-type transporter activity: the transported Cd species is unknown, so a substrate-specific term is not warranted.

### Relative and family
- Closest experimentally characterised relative by phylogeny: human ABCB6 (Q9NP58), the seed of both PAINT nodes and in the same PANTHER subfamily SF654. No human ABCB6 review exists in the repo.
- interpro/panther/PTHR24221/PTHR24221-review.yaml places Hmt-1 in SF654, in agreement with UniProt. Its FAMILY_WIDE ABC-type transporter assessment is consistent with this review; its statement that a heme substrate cannot be assigned family-wide concerns the whole PTHR24221 family (mostly bacterial exporters), not the ABCB6 eumetazoan node, so it does not conflict with accepting the heme IBA here.
- No module in modules/ covers ABCB6/HMT-1, heme transport or cadmium detoxification.
