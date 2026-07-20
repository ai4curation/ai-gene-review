---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T14:38:49.814739'
end_time: '2026-07-20T14:53:01.258629'
duration_seconds: 851.44
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: moeA
  gene_symbol: moeA
  uniprot_accession: Q88L14
  protein_description: 'RecName: Full=Molybdopterin molybdenumtransferase {ECO:0000256|RuleBase:RU365090};
    EC=2.10.1.1 {ECO:0000256|RuleBase:RU365090};'
  gene_info: Name=moeA {ECO:0000313|EMBL:AAN67736.1}; OrderedLocusNames=PP_2123 {ECO:0000313|EMBL:AAN67736.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MoeA family. {ECO:0000256|ARBA:ARBA00010763,
  protein_domains: MoaB/Mog-like_dom_sf. (IPR036425); MoaB/Mog_dom. (IPR001453); MoCF_biosynth_CS.
    (IPR008284); MoeA-like. (IPR038987); MoeA_C_domain_IV. (IPR005111)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: moeA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: moeA-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88L14
- **Protein Description:** RecName: Full=Molybdopterin molybdenumtransferase {ECO:0000256|RuleBase:RU365090}; EC=2.10.1.1 {ECO:0000256|RuleBase:RU365090};
- **Gene Information:** Name=moeA {ECO:0000313|EMBL:AAN67736.1}; OrderedLocusNames=PP_2123 {ECO:0000313|EMBL:AAN67736.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MoeA family. {ECO:0000256|ARBA:ARBA00010763,
- **Key Domains:** MoaB/Mog-like_dom_sf. (IPR036425); MoaB/Mog_dom. (IPR001453); MoCF_biosynth_CS. (IPR008284); MoeA-like. (IPR038987); MoeA_C_domain_IV. (IPR005111)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "moeA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'moeA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **moeA** (gene ID: moeA, UniProt: Q88L14) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *moeA* (Q88L14 / PP_2123) in *Pseudomonas putida* KT2440

## 1. Summary — Answer to the Research Question

**MoeA (Q88L14, locus PP_2123) is molybdopterin molybdenumtransferase (EC 2.10.1.1), the enzyme that catalyzes the final, metal-insertion step of molybdenum cofactor (Moco) biosynthesis.** It ligates molybdenum into the dithiolene of molybdopterin (MPT) to produce the mature, active molybdenum cofactor. This reaction takes place in the **cytoplasm**, acting on an adenylylated molybdopterin (MPT-AMP) substrate provided by a MogA/MoaB-type adenylyltransferase partner, and delivering finished Moco for insertion into the cell's molybdoenzymes. In obligately aerobic KT2440 these clients are principally **xanthine dehydrogenase, aldehyde oxidoreductases, and formate dehydrogenase** (nitrate/DMSO/sulfite reductases are absent from this strain). MoeA is an ancient, deeply conserved enzyme, the bacterial ancestor of eukaryotic gephyrin/Cnx1.

The gene identity is unambiguous: the symbol *moeA*, the EC number, the MoeA protein family, and the domain architecture (MoaB/Mog-like domain IPR001453; MoeA-like IPR038987; MoeA_C_domain_IV IPR005111) all coincide with the canonical, well-characterized bacterial MoeA. Because MoeA is highly conserved and the *E. coli* ortholog is biochemically and structurally characterized, its function transfers to *P. putida* Q88L14 with high confidence.

## 2. Primary Function — the Catalyzed Reaction

**Organism-specific annotation (UniProt Q88L14 / KEGG ppu:PP_2123):** a 408-residue, single-chain enzyme; EC 2.10.1.1; KEGG ortholog **K03750** (molybdopterin molybdotransferase); orthology group **COG0303 (MoeA)**; FUNCTION "Catalyzes the insertion of molybdate into adenylated molybdopterin with the concomitant release of AMP"; **required cofactor Mg²⁺**; pathway "Cofactor biosynthesis; molybdopterin biosynthesis." The recorded catalytic activity is:

> **adenylyl-molybdopterin (MPT-AMP) + molybdate (MoO₄²⁻) → Mo-molybdopterin (Moco) + AMP + H⁺**  (Mg²⁺-dependent)

MoeA performs this terminal metal-insertion step of Moco biosynthesis:

- In *E. coli*, **MoeA mediates the ligation of Mo to molybdopterin, while MogA enhances this process in an ATP-dependent manner** (Nichols & Rajagopalan 2007, PMID 17198377). MogA adenylylates MPT (forming MPT-AMP); MoeA then inserts molybdenum with concomitant release of AMP.
- This is the **final step of Moco biosynthesis: the incorporation of molybdenum into molybdopterin (MPT), the organic pyranopterin moiety of Moco** (Xiang et al. 2001, PMID 11525167).
- The same reaction — **transfer and insertion of Mo into MPT** — is carried out in eukaryotes by the two-domain proteins Cnx1 (plants) and gephyrin (mammals), whose E-domain is the MoeA homolog (Schwarz et al. 2001, PMID 11554796).

**Substrate specificity:** the organic substrate is molybdopterin / adenylylated molybdopterin (MPT-AMP); the metal substrate is molybdate; Mg²⁺ is required as a catalytic cofactor. Notably, MoeA-family proteins can also handle tungstate: in tungsten-utilizing organisms, specialized MoeA paralogs dedicate biosynthesis toward tungsten cofactors (Debnar-Daumler et al. 2014, PMID 24214948), underscoring that the enzyme's role is metal insertion into the pterin dithiolene.

## 3. Structure–Function Basis

- The *E. coli* MoeA monomer is **highly elongated with four clearly separated domains, one of which is structurally related to MogA** (Xiang et al. 2001, PMID 11525167; Schrag et al. 2001, PMID 11428898). Q88L14's InterPro domains (MoaB/Mog domain; MoeA-like; MoeA C-domain IV) match this architecture.
- **The active form of MoeA is a dimer**, with the putative active site in **a cleft formed between domain II of one monomer and domains III and IV of the second monomer** (Xiang et al. 2001, PMID 11525167) — i.e., a composite, inter-subunit active site requiring homodimerization.
- Mutational analysis maps two functional activities to the active-site cleft, and a variant's Moco-binding ability correlates with activity (Nichols & Rajagopalan 2007, PMID 17198377). Conserved acidic residues are essential: **replacements such as Asp259Ala abolished MoeA function in Mo-molybdopterin formation and stabilization, and the inability to restore nitrate reductase activity** (Sandu & Brandsch 2002, PMID 11934270).

## 4. Localization

Moco biosynthesis is a **cytosolic** process; MoeA is a soluble cytoplasmic enzyme (no signal peptide or transmembrane segments; consistent with UniProt annotation). It carries out metal insertion in the cytoplasm and the resulting Moco is subsequently inserted into apo-molybdoenzymes, some of which are then exported (e.g., periplasmic nitrate reductase NapA) or remain cytoplasmic.

## 5. Pathway Context and Physiological Role

MoeA operates at the **convergence of two branches** of Moco biosynthesis: the pterin branch (MoaA/MoaC → cyclic pyranopterin monophosphate; MoaD/MoaE + MoeB → MPT) and the metal-incorporation branch (MogA/MoaB adenylylation of MPT + MoeA Mo insertion; downstream MobA/MobB further modify Mo-MPT to the molybdopterin-guanine dinucleotide (MGD/bis-MGD) form). Its product Moco is **required for all molybdoenzymes except nitrogenase** (Schwarz et al. 2001, PMID 11554796).

**KT2440 encodes a complete Moco pathway (KEGG mapping):** MoaA (PP_1969, PP_2482, PP_4597), MoaC (PP_1292), MoaB/MogA-like scaffolds (PP_1293; and MoaB paralogs PP_2122, PP_4600), MoeB sulfurtransferase (PP_1294), **MoeA (PP_2123, the target, K03750)**, and downstream MobA (PP_4003) and MobB (PP_3309) for MGD synthesis. Notably a dedicated *mogA* gene (K03831) is absent — the adenylyltransferase partner activity is supplied by MoaB/MogA paralogs, one of which (PP_2122) is operon-coupled to *moeA*. The presence of MobA/MobB confirms that MoeA-derived Mo-MPT is matured to the MGD form used by the Gram-negative DMSO-reductase-family molybdoenzymes.

Physiological evidence from bacteria (illustrating MoeA's essentiality for molybdoenzyme function; note these particular clients differ by organism — see the KT2440-specific survey below):
- In *Burkholderia thailandensis*, a **moeA transposon mutant could not grow anaerobically with nitrate as sole terminal electron acceptor**, with defects in nitrate reductase activity, biofilm formation, and motility, all restored (except motility) by complementation (Andreae et al. 2014, PMID 24239959).
- The rice MoeA homolog OsCNX1, when restored, recovered **MoCo-dependent enzyme activities such as xanthine dehydrogenase, aldehyde oxidase, nitrate reductase and sulfite oxidase** (Liu et al. 2019, PMID 30471121), illustrating the breadth of downstream molybdoenzymes.

**Genomic context in KT2440:** *moeA* (PP_2123, 2,421,713–2,422,939, forward strand) lies immediately downstream of and **overlaps by ~16 bp** with PP_2122 ("molybdenum cofactor biosynthesis protein B," a MogA/MoaB-family gene), indicating translational coupling / co-transcription. This physical pairing mirrors the functional partnership between MoeA and its MogA/MoaB-type adenylyltransferase partner (which generates the MPT-AMP substrate), supporting coordinated expression of the final metal-insertion module.

**Molybdoenzyme clients specific to KT2440 (KEGG survey):** Importantly, obligately aerobic *P. putida* KT2440 **lacks** the nitrate reductases (respiratory NarG, assimilatory, periplasmic NapA), DMSO/TMAO reductase, biotin sulfoxide reductase, and sulfite oxidase that are the prominent Moco clients in facultative anaerobes such as *E. coli* and *Burkholderia*. Instead, its Moco-dependent enzymes are: **xanthine dehydrogenase** (XdhA, PP_3308, with small subunit PP_3310 — flanking MobB PP_3309, i.e., a purine-catabolism/molybdo gene cluster), **aldehyde oxidoreductases** (PaoC-type, PP_2477, PP_3621), and **formate dehydrogenase** (PP_0489, PP_2185). Thus in KT2440, MoeA-derived Moco gates **aerobic purine catabolism, aldehyde oxidation, and formate oxidation** rather than anaerobic nitrate/S-oxide respiration. Consistent with the research brief's emphasis on the precise role rather than pleiotropy, MoeA's effects are pleiotropic only because it is the single gate for cofactor maturation; its own biochemical act is the specific, defined metal-insertion reaction.

## 6. Evolutionary Evidence

MoeA **exists in all domains of life** and is the ancestor of eukaryotic gephyrin (mammals) and Cnx1 (plants), where MogA and MoeA are fused (Xiang et al. 2001, PMID 11525167). Phylogenetic and structural analysis confirms MoeA is an **essential enzyme for Moco biosynthesis**; early eukaryotes acquired MoeA from Bacteria, MogA–MoeA fusion arose in the opisthokont ancestor, and gephyrin later gained receptor-clustering roles at inhibitory synapses (Megrian et al. 2025, PMID 39809875). The *P. putida* protein represents the ancestral, catalytically dedicated bacterial form without the eukaryotic scaffolding functions.

## 7. Supported and Refuted Hypotheses

**Supported**
- H1: Q88L14/MoeA catalyzes molybdenum insertion into molybdopterin (final Moco step). — Strongly supported by structural, biochemical, and mutational data on orthologs.
- H2: MoeA functions as a homodimer with an inter-subunit active-site cleft and conserved catalytic Asp residues. — Supported by crystallography and mutagenesis.
- H3: MoeA acts cytoplasmically and its product Moco is essential for the strain's molybdoenzymes. — Supported by mutant phenotypes across taxa; in KT2440 specifically the clients are xanthine dehydrogenase, aldehyde oxidoreductases, and formate dehydrogenase (KEGG survey), not nitrate/DMSO reductases.
- H4 (organism-specific): KT2440's Moco demand reflects an aerobic lifestyle. — Supported: the strain lacks anaerobic-respiration molybdoenzymes, so MoeA gates aerobic purine/aldehyde/formate oxidation.

**Not applicable / Refuted**
- The *moeA* symbol is NOT ambiguous here; it is not a transporter, structural protein, or signaling molecule. It is a biosynthetic transferase enzyme.
- MoeA is not itself a molybdoenzyme (it does not use Moco); it makes Moco.

## 8. Limitations and Future Directions

- No *P. putida* KT2440-specific biochemical or structural study of PP_2123 was found; functional assignment relies on high-confidence orthology to *E. coli* MoeA and conserved domain architecture. Direct enzymatic characterization or a KT2440 knockout phenotype would confirm substrate specificity (Mo vs W) and downstream molybdoenzyme dependencies in this organism.
- The exact kinetic mechanism (order of Mo insertion vs AMP release; Mg²⁺ requirement) is inferred from ortholog studies.
- Whether *P. putida* MoeA shows any tungstate handling or paralog specialization is untested.
- The molybdoenzyme inventory was derived from KEGG KO markers, which could miss divergent or unannotated enzymes; nonetheless the clear absence of nitrate/DMSO/sulfite-reductase KOs is consistent with KT2440's known obligately aerobic, non-denitrifying physiology.

---
*Citations: PMIDs 17198377, 11525167, 11428898, 11934270, 11554796, 39809875, 24239959, 30471121, 24214948.*


## Artifacts

- [OpenScientist final report](moeA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](moeA-deep-research-openscientist_artifacts/final_report.pdf)