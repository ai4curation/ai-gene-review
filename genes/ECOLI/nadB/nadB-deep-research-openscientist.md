---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T03:51:23.617885'
end_time: '2026-11-12T04:04:08.754442'
duration_seconds: 765.14
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: ECOLI
  gene_id: P10902
  gene_symbol: nadB
  uniprot_accession: P10902
  protein_description: 'RecName: Full=L-aspartate oxidase {ECO:0000303|PubMed:7033218};
    Short=LASPO {ECO:0000303|PubMed:10425677}; EC=1.4.3.16 {ECO:0000269|PubMed:11294641,
    ECO:0000269|PubMed:12200425, ECO:0000269|PubMed:20149100, ECO:0000269|PubMed:2187483,
    ECO:0000269|PubMed:2841129, ECO:0000269|PubMed:7033218, ECO:0000269|PubMed:8706749,
    ECO:0000269|PubMed:8706750}; AltName: Full=L-aspartate:fumarate oxidoreductase
    {ECO:0000303|PubMed:8706750}; EC=1.5.99.- {ECO:0000269|PubMed:11294641, ECO:0000269|PubMed:12200425,
    ECO:0000269|PubMed:20149100, ECO:0000269|PubMed:8706750}; AltName: Full=Quinolinate
    synthetase B {ECO:0000303|PubMed:2841129};'
  gene_info: Name=nadB {ECO:0000303|PubMed:2841129}; Synonyms=nicB; OrderedLocusNames=b2574,
    JW2558;
  organism_full: Escherichia coli (strain K12).
  protein_family: Belongs to the FAD-dependent oxidoreductase 2 family. NadB
  protein_domains: FAD-dep_OxRdtase_2_FAD-bd. (IPR003953); FAD/NAD-bd_sf. (IPR036188);
    Fum_R/Succ_DH_flav-like_C_sf. (IPR037099); Fum_Rdtase/Succ_DH_flav-like_C. (IPR015939);
    NadB. (IPR005288)
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
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: nadB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: nadB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** P10902
- **Protein Description:** RecName: Full=L-aspartate oxidase {ECO:0000303|PubMed:7033218}; Short=LASPO {ECO:0000303|PubMed:10425677}; EC=1.4.3.16 {ECO:0000269|PubMed:11294641, ECO:0000269|PubMed:12200425, ECO:0000269|PubMed:20149100, ECO:0000269|PubMed:2187483, ECO:0000269|PubMed:2841129, ECO:0000269|PubMed:7033218, ECO:0000269|PubMed:8706749, ECO:0000269|PubMed:8706750}; AltName: Full=L-aspartate:fumarate oxidoreductase {ECO:0000303|PubMed:8706750}; EC=1.5.99.- {ECO:0000269|PubMed:11294641, ECO:0000269|PubMed:12200425, ECO:0000269|PubMed:20149100, ECO:0000269|PubMed:8706750}; AltName: Full=Quinolinate synthetase B {ECO:0000303|PubMed:2841129};
- **Gene Information:** Name=nadB {ECO:0000303|PubMed:2841129}; Synonyms=nicB; OrderedLocusNames=b2574, JW2558;
- **Organism (full):** Escherichia coli (strain K12).
- **Protein Family:** Belongs to the FAD-dependent oxidoreductase 2 family. NadB
- **Key Domains:** FAD-dep_OxRdtase_2_FAD-bd. (IPR003953); FAD/NAD-bd_sf. (IPR036188); Fum_R/Succ_DH_flav-like_C_sf. (IPR037099); Fum_Rdtase/Succ_DH_flav-like_C. (IPR015939); NadB. (IPR005288)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nadB" matches the protein description above**
2. **Verify the organism is correct:** Escherichia coli (strain K12).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nadB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nadB** (gene ID: P10902, UniProt: P10902) in ECOLI.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# NadB (L-Aspartate Oxidase) of *Escherichia coli* K-12 — Functional Annotation Report

**UniProt:** [P10902](https://www.uniprot.org/uniprotkb/P10902) | **Gene:** *nadB* (synonym *nicB*; b2574, JW2558) | **EC:** 1.4.3.16 / 1.5.99.- | **Organism:** *Escherichia coli* (strain K-12)

---

## Summary

**NadB is L-aspartate oxidase (LASPO), a soluble, cytoplasmic, monomeric FAD-dependent flavoenzyme that catalyzes the first committed and rate-limiting step of de novo NAD⁺ biosynthesis in *Escherichia coli*.** It oxidizes (desaturates) L-aspartate at the C2–C3 position to yield **iminoaspartate** (α-iminosuccinate). This labile intermediate is handed off to the [4Fe-4S] enzyme quinolinate synthase (NadA), which condenses it with dihydroxyacetone phosphate (DHAP) to form **quinolinic acid** — the universal precursor of the pyridine ring of NAD⁺. Gene identity is unambiguous: the gene symbol *nadB*, the organism (*E. coli* K-12), the FAD-dependent oxidoreductase 2 / NadB family, and the diagnostic SDH/FRD-like flavoprotein domains all align precisely with the extensive primary literature on L-aspartate oxidase. No ambiguity or mistaken-identity issue was encountered.

A defining feature of NadB is its **bifunctionality in electron acceptors**. Aerobically, it uses molecular O₂ as the oxidant, producing H₂O₂ as an adventitious byproduct — and it is, in fact, a quantitatively significant endogenous source of H₂O₂ in *E. coli*. Anaerobically, it operates as an **L-aspartate:fumarate oxidoreductase** (a specialized fumarate reductase), transferring electrons from its reduced flavin to fumarate to produce succinate. This dual behavior is explained by its membership in the succinate dehydrogenase/fumarate reductase (SDH/FRD) flavoprotein family: crystallographic and biochemical work shows NadB shares the three-domain fold, the FAD-induced domain-closure mechanism, and the active-site architecture of respiratory fumarate reductases, with a single strictly conserved active-site glutamate (E121) adapting that ancestral scaffold for L-aspartate oxidation.

NadB function is tightly integrated into cellular NAD homeostasis. It is feedback-inhibited by physiological concentrations of NAD(H) at the enzyme level and transcriptionally repressed within the **NadR regulon** at the gene level. Loss-of-function *nadB* mutations cause NAD/nicotinamide auxotrophy, genetically confirming that NadB is indispensable for the de novo route. Together, these data give a complete mechanistic, structural, regulatory, and physiological annotation of NadB as the gatekeeper enzyme of bacterial de novo NAD⁺ biosynthesis.

---

## Key Findings

### 1. NadB catalyzes the first committed step of de novo NAD⁺ biosynthesis: L-aspartate → iminoaspartate

L-Aspartate oxidase (LASPO; EC 1.4.3.16) is the entry enzyme of the de novo NAD⁺ biosynthetic pathway. It is an FAD-dependent flavoenzyme that converts L-aspartate to **iminoaspartate** (α-iminosuccinate). As stated directly in the structural review of the enzyme, *"The first reaction in the pathway is catalysed by L-aspartate oxidase (LASPO), a flavoenzyme that converts aspartate to iminoaspartate using either molecular oxygen or fumarate as electron acceptors"* ([PMID: 10425677](https://pubmed.ncbi.nlm.nih.gov/10425677/)). The *nadB* gene (ordered locus b2574) encodes a 60.3 kDa monomeric protein.

The product of the NadB/NadA system — quinolinate (pyridine-2,3-dicarboxylate) — is the biosynthetic precursor of the pyridine ring of NAD ([PMID: 2841129](https://pubmed.ncbi.nlm.nih.gov/2841129/)). Early radiotracer work established the chemical logic of the pathway: *"Quinolinic acid (pyridine 2,3-dicarboxylic acid) which is an immediate precursor of the pyridine nucleotides, is synthesised from L-aspartate and dihydroxyacetone phosphate in Escherichia coli"* ([PMID: 238844](https://pubmed.ncbi.nlm.nih.gov/238844/)). NadB supplies the L-aspartate–derived half of this condensation.

This establishes NadB's **primary function** unambiguously: it is an oxidoreductase that removes two hydrogen equivalents from L-aspartate to form the imine, committing aspartate carbon and nitrogen to pyridine-nucleotide biosynthesis.

### 2. NadB is bifunctional in its electron acceptor: O₂ aerobically, fumarate anaerobically

NadB oxidizes L-aspartate under both aerobic and anaerobic conditions, but it uses different terminal electron acceptors depending on oxygen availability. Under aerobic conditions, molecular O₂ reoxidizes the reduced flavin. Under anaerobic conditions, NadB functions as a genuine **fumarate reductase**: *"A new fumarate reductase activity of L-aspartate oxidase is reported using benzylviologen or L-aspartate as reductants and fumarate as oxidant"* ([PMID: 8706750](https://pubmed.ncbi.nlm.nih.gov/8706750/)). The enzyme binds the C4-dicarboxylates fumarate and succinate with comparable, physiologically relevant affinities — *"L-Aspartate oxidase binds succinate and fumarate with Kd values of 0.24 mM and 0.22 mM, respectively"* ([PMID: 8706750](https://pubmed.ncbi.nlm.nih.gov/8706750/)) — and reduces fumarate to succinate, confirmed with radiolabeled substrate.

The thermodynamic basis for this behavior was defined by redox titration. The midpoint potential of the enzyme-bound flavin is **−216 mV**: *"A value of -216 mV was calculated for the midpoint potential of the couple FAD/FADH2 bound to the enzyme. This result perfectly explains why L-aspartate oxidase may be considered as a very particular fumarate reductase unable to use succinate as the electron donor"* ([PMID: 9405056](https://pubmed.ncbi.nlm.nih.gov/9405056/)). In other words, the flavin potential makes fumarate reduction (not succinate oxidation) favorable — NadB is a "one-way" fumarate reductase. In vitro, quinones can also serve as alternative acceptors: *"L-Aspartate oxidase binds menadione and 2,3-dimethoxy-5-methyl-p-benzoquinone with Kd values of 11.5 and 2.4 microM, respectively"* ([PMID: 9405056](https://pubmed.ncbi.nlm.nih.gov/9405056/)). This dual-acceptor flexibility lets the de novo pathway operate under both aerobic and anaerobic growth.

| Condition | Electron acceptor | Product of acceptor reduction | Evidence |
|-----------|-------------------|-------------------------------|----------|
| Aerobic | O₂ | H₂O₂ | [PMID: 10425677](https://pubmed.ncbi.nlm.nih.gov/10425677/), [PMID: 20149100](https://pubmed.ncbi.nlm.nih.gov/20149100/) |
| Anaerobic | Fumarate | Succinate | [PMID: 8706750](https://pubmed.ncbi.nlm.nih.gov/8706750/) |
| In vitro | Quinones (menadione, DMK analog) | Quinol | [PMID: 9405056](https://pubmed.ncbi.nlm.nih.gov/9405056/) |

### 3. NadB is a monomeric FAD flavoprotein with the three-domain SDH/FRD fold

The active form of the enzyme is *"a monomer of 60,284 Da and contains one molecule of FAD and nine cysteine residues, four of which built up two disulfide bonds"* ([PMID: 2187483](https://pubmed.ncbi.nlm.nih.gov/2187483/)). The 2.2 Å crystal structure of the apo form revealed a distinctive architecture: *"The enzyme shows a novel fold for an FAD-dependent protein, comprising a three-domain structure: an FAD-binding domain with the dinucleotide-binding fold, a C-terminal three-helical bundle domain, and an alpha + beta capping domain"* ([PMID: 10425677](https://pubmed.ncbi.nlm.nih.gov/10425677/)). The active site lies in the cleft between the FAD-binding domain and the capping domain.

Critically, this structure placed NadB firmly within a functionally and structurally coherent enzyme class: *"LASPO, SDH and FRD form a class of functionally and structurally related oxidoreductases that are all able to reduce fumarate and to oxidise a dicarboxyla[te]"* ([PMID: 10425677](https://pubmed.ncbi.nlm.nih.gov/10425677/)). The strong primary- and tertiary-structure similarity to the flavoprotein subunits of succinate dehydrogenase and fumarate reductase, together with conserved active-site residues, implies a **shared catalytic mechanism** across the family and rationalizes NadB's fumarate-reductase side activity.

### 4. Active-site determinants separate the two catalytic functions: E121 for oxidase, R290/R386/H244/H351 for fumarate handling

Site-directed mutagenesis cleanly dissected the two activities. The strictly conserved glutamate **E121** — present in LASPO but replaced by apolar residues in SDH/FRD — is essential specifically for aspartate oxidation: *"All mutants retain fumarate reductase activity. On the contrary, all mutants lack L-aspartate oxidase activity, although retaining the ability to bind L-aspartate (except for E121K)"* ([PMID: 20600565](https://pubmed.ncbi.nlm.nih.gov/20600565/)). Mechanistically, *"the roles of E121 in catalysis include orienting L-aspartate in a productive binding mode and favouring proton abstraction from C2 by an active site base"* ([PMID: 20600565](https://pubmed.ncbi.nlm.nih.gov/20600565/)). E121 is therefore the molecular adaptation that converts an ancestral fumarate-reductase scaffold into an aspartate oxidase.

Among the basic active-site residues governing the fumarate-reduction/dicarboxylate half-reaction, their roles were distinguished kinetically: *"R290, on the contrary, is mainly involved in catalysis and not in substrate binding since its mutation abolishes the catalytic activity without lowering the affinity of the enzyme for the substrate"* ([PMID: 11294641](https://pubmed.ncbi.nlm.nih.gov/11294641/)). R386, H244, and H351 contribute mainly to substrate (fumarate) binding. Importantly, the redox properties of these mutants were identical to wild type, showing that these residues act in substrate orientation/catalysis rather than tuning the flavin.

| Residue | Primary role | Effect of mutation | Evidence |
|---------|--------------|--------------------|----------|
| E121 | Orient L-Asp; promote C2 proton abstraction | Loses oxidase activity; keeps fumarate reductase | [PMID: 20600565](https://pubmed.ncbi.nlm.nih.gov/20600565/) |
| R290 | Catalysis (fumarate half-reaction) | Abolishes activity without lowering affinity | [PMID: 11294641](https://pubmed.ncbi.nlm.nih.gov/11294641/) |
| R386, H244, H351 | Substrate (fumarate) binding | Reduce affinity | [PMID: 11294641](https://pubmed.ncbi.nlm.nih.gov/11294641/) |

### 5. FAD binding drives domain closure that builds the active site — confirming the fumarate-reductase-like mechanism

The catalytically competent FAD-bound holoenzyme (solved using the R386L variant at 2.5 Å, alone and with succinate) revealed how cofactor binding templates catalysis: *"cofactor incorporation leads to the ordering of two polypeptide segments (residues 44-53 and 104-141) and to a 27 degree rotation of the capping domain. This motion results in the formation of the active site cavity, located at the interface between the capping domain and the FAD-binding domain"* ([PMID: 11863440](https://pubmed.ncbi.nlm.nih.gov/11863440/)). This induced-fit closure converts the open apoenzyme into the closed, substrate-competent holoenzyme.

The holoenzyme structure also independently confirmed the mechanistic role of E121 that mutagenesis had inferred: *"Glu121, which is strictly conserved among Laspo sequences, is positioned to interact with the L-Asp alpha-amino group"* ([PMID: 11863440](https://pubmed.ncbi.nlm.nih.gov/11863440/)). Most importantly, the overall active-site geometry matched the respiratory enzymes: *"The architecture of the active site of the Laspo holoenzyme is remarkably similar to that of respiratory fumarate reductases, providing strong evidence for a common mechanism of catalysis in Laspo and flavoproteins of the succinate dehydrogenase/fumarate reductase family"* ([PMID: 11863440](https://pubmed.ncbi.nlm.nih.gov/11863440/)). This closes the loop between structure, mechanism, and family assignment.

### 6. NadB is cytoplasmic, functionally coupled to NadA, and feedback-inhibited by NAD(H)

NadB (historically the "B protein" of quinolinate synthetase) is a separable soluble protein, not part of a stable obligate complex: *"The facile separation of the wild-type quinolinate synthetase A and B proteins out of a nadC mutant suggests that quinolinate synthetase does not exists as a tightly bound complex"* ([PMID: 238844](https://pubmed.ncbi.nlm.nih.gov/238844/)). Nonetheless, NadB must deliver its labile iminoaspartate product to NadA. This handoff is functional and conserved across species: *"the interaction between NadA and NadB is not species-specific between B. subtilis and Escherichia coli"* ([PMID: 18959769](https://pubmed.ncbi.nlm.nih.gov/18959769/)).

The pathway is regulated at the protein level by its end product: *"The partially purified quinolinate synthetase is inhibited by physiological concetrations of NAD and NADH but not by NADP or NADPH"* ([PMID: 238844](https://pubmed.ncbi.nlm.nih.gov/238844/)). This NAD(H)-specific feedback inhibition ties NadB flux directly to the cellular NAD pool. The location of this activity is cytoplasmic/soluble — overexpression studies show the gene product accumulates as a large fraction of soluble cell protein, and high-copy *nadA/nadB* raises quinolinate ~15-fold, confirming both are rate-limiting and soluble.

### 7. NadB is a quantitatively significant endogenous source of H₂O₂

Because NadB's normal (anaerobic) oxidant is fumarate, its reaction with O₂ aerobically is a mechanistic accident that generates H₂O₂. This contributes measurably to the oxidative burden of the cell: *"H(2)O(2) production diminished by 25-30% when NadB turnover was eliminated"* ([PMID: 20149100](https://pubmed.ncbi.nlm.nih.gov/20149100/)) in a strain lacking H₂O₂ scavengers. The mechanism was described explicitly: *"The flavin-dependent desaturating dehydrogenase, NadB uses fumarate as an electron acceptor in anaerobic cells. Experiments showed that aerobic NadB turnover depends upon its oxidation by molecular oxygen, with H(2)O(2) as a product. This reaction appears to be mechanistically adventitious"* ([PMID: 20149100](https://pubmed.ncbi.nlm.nih.gov/20149100/)). This is tolerated only because de novo NAD flux through NadB is low. This finding reframes NadB not just as a biosynthetic enzyme but as a notable contributor to endogenous oxidative stress.

### 8. *nadB* expression is controlled by the NAD-responsive regulator NadR

Beyond product inhibition at the enzyme level, de novo NAD synthesis is controlled transcriptionally. Classical genetics defined *nadR*: *"The latter group is tentatively designated nadR based on its regulation of the unlinked nadA gene. The nadR gene maps adjacent to nadB between purI and tyrA"* ([PMID: 4349027](https://pubmed.ncbi.nlm.nih.gov/4349027/)). NadR is a multifunctional protein whose DNA-binding activity represses NAD biosynthesis genes: *"the full-size multifunctional NadR protein (as in Escherichia coli) is composed of (i) an N-terminal DNA-binding domain involved in the transcriptional regulation of NAD biosynthesis"* ([PMID: 12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/)), while its central NMN adenylyltransferase (NMNAT) and C-terminal ribosylnicotinamide kinase (RNK) domains participate in NAD salvage. NadB is thus co-regulated with the broader NAD biosynthetic/salvage network, layering transcriptional control on top of the allosteric NAD(H) feedback.

### 9. Loss-of-function genetics prove NadB is essential for de novo NAD biosynthesis

*nadB* is genetically indispensable for the de novo pathway: *"NAD auxotrophy can be rendered by mutation in any of the three genes nadB, nadA and nadC"* ([PMID: 22174382](https://pubmed.ncbi.nlm.nih.gov/22174382/)). A precise natural example comes from uropathogenic *E. coli* UTI89, where *"A mutation in the nadB gene, encoding L-aspartate oxidase, was shown to be responsible for the nicotinamide requirement of UTI89"* ([PMID: 22174382](https://pubmed.ncbi.nlm.nih.gov/22174382/)) — a single Ala28Val substitution abolishes de novo synthesis, and growth is restored by wild-type K-12 *nadB* or by Val28Ala revertants. Cross-species complementation further confirms conserved function: *"Pa nadB complemented the growth requirement for nicotinic acid in a nadB mutant strain of E. coli, suggesting that this gene encodes a functional homologue of L-aspartate oxidase"* ([PMID: 7737518](https://pubmed.ncbi.nlm.nih.gov/7737518/)). These genetics establish causality — NadB activity is required to make NAD de novo.

### 10. NadB's product is consumed by the [4Fe-4S] enzyme NadA to form quinolinate

The downstream fate of iminoaspartate completes the pathway picture. NadA (quinolinate synthase) is a [4Fe-4S]-cluster enzyme that condenses NadB's product with DHAP: *"Its synthesis comprises the condensation of dihydroxyacetone phosphate (DHAP) and iminoaspartate (IA), which involves dephosphorylation, isomerization, cyclization, and two dehydration steps"* ([PMID: 34609124](https://pubmed.ncbi.nlm.nih.gov/34609124/)). The identity of the triose was clarified mechanistically: *"we demonstrate that DHAP is the triose that condenses with IA to form QA"* ([PMID: 26455817](https://pubmed.ncbi.nlm.nih.gov/26455817/)), with NadA's intrinsic triose-phosphate-isomerase activity explaining earlier apparent use of glyceraldehyde-3-phosphate. This pins NadB precisely within the two-enzyme de novo quinolinate route.

---

## Mechanistic Model / Interpretation

### The de novo NAD⁺ pathway and NadB's place in it

```
                    NadB (L-aspartate oxidase, FAD)
                    EC 1.4.3.16 / 1.5.99.-
                    ┌─────────────────────────────┐
   L-Aspartate ─────┤  oxidation (desaturation)   ├────► Iminoaspartate (α-iminosuccinate)
                    │  FAD → FADH2                 │            │
                    └──────────┬──────────────────┘            │
                               │ FADH2 reoxidized by:          │ (labile intermediate, handoff)
                   aerobic:  O2  → H2O2                         ▼
                   anaerobic: fumarate → succinate       NadA (quinolinate synthase, [4Fe-4S])
                                                               │  + DHAP
                                                               ▼
                                                         Quinolinate (QA)
                                                               │  NadC (quinolinate phosphoribosyltransferase)
                                                               ▼
                                                   Nicotinate mononucleotide → ... → NAD⁺
```

NadB performs a **two-electron desaturation** of L-aspartate: it abstracts hydrogens from C2 and C3 to install the C=N imine, reducing its FAD to FADH₂. The strictly conserved **E121** orients the substrate's α-amino group and promotes proton abstraction from C2 by an active-site base, the single key adaptation distinguishing the oxidase from its SDH/FRD relatives. The reduced flavin must then be reoxidized to regenerate active enzyme — and this is where NadB's bifunctionality matters. Thermodynamically (flavin Em ≈ −216 mV), the enzyme can pass electrons onto fumarate (→ succinate) anaerobically, making it a dedicated one-way fumarate reductase, or onto O₂ (→ H₂O₂) aerobically. The second half-reaction occupies the same dicarboxylate-binding subsite served by R290/R386/H244/H351, exactly as in true fumarate reductases.

### A moonlighting metabolic link to the TCA cycle

Because NadB reduces fumarate to succinate, it provides a minor metabolic bridge between aspartate catabolism and the TCA-cycle dicarboxylate pool under anaerobiosis. This is the same chemistry run by the SDH/FRD respiratory enzymes, which NadB structurally mirrors. The enzyme is essentially a fumarate-reductase flavoprotein domain that has acquired (via E121) the ability to oxidize aspartate on the "substrate" side while retaining fumarate reduction on the "acceptor" side.

### Integrated regulation

NadB flux is controlled at two levels that both sense the NAD pool:

| Level | Mechanism | Sensor | Evidence |
|-------|-----------|--------|----------|
| Protein (allosteric) | Feedback inhibition | NAD, NADH (not NADP/H) | [PMID: 238844](https://pubmed.ncbi.nlm.nih.gov/238844/) |
| Gene (transcriptional) | Repression within NadR regulon | NadR (NAD-responsive) | [PMID: 4349027](https://pubmed.ncbi.nlm.nih.gov/4349027/), [PMID: 12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/) |

This dual control keeps de novo synthesis low when NAD is plentiful — consistent with the low flux that makes the adventitious H₂O₂ production tolerable.

### Localization

All evidence points to a **cytoplasmic, soluble** enzyme: NadB is readily purified as a soluble monomer, accumulates as a large fraction of soluble protein when overexpressed, and participates in a cytoplasmic biosynthetic pathway with the soluble NadA. There is no evidence of membrane anchoring or periplasmic/extracellular localization.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|------|-----------------|--------------|
| [10425677](https://pubmed.ncbi.nlm.nih.gov/10425677/) | *Structure of L-aspartate oxidase: implications for the SDH/FRD family* | Apo crystal structure (2.2 Å), three-domain fold, SDH/FRD family assignment, reaction definition |
| [8706750](https://pubmed.ncbi.nlm.nih.gov/8706750/) | *L-aspartate oxidase II: C4-dicarboxylic acids and novel L-aspartate:fumarate oxidoreductase* | Discovery of anaerobic fumarate reductase activity; fumarate/succinate Kd values |
| [9405056](https://pubmed.ncbi.nlm.nih.gov/9405056/) | *Redox potentials and quinone reductase activity of LASPO* | Flavin Em = −216 mV; explains one-way fumarate reductase behavior; quinone acceptors |
| [2187483](https://pubmed.ncbi.nlm.nih.gov/2187483/) | *Expression of nadB and characterization of LASPO* | Monomeric 60,284 Da protein, one FAD, cysteine/disulfide content |
| [20600565](https://pubmed.ncbi.nlm.nih.gov/20600565/) | *Catalytic role of E121* | E121 essential for oxidase but not fumarate reductase; substrate orientation/proton abstraction |
| [11294641](https://pubmed.ncbi.nlm.nih.gov/11294641/) | *Basic residues in fumarate reduction* | R290 catalytic; R386/H244/H351 bind substrate |
| [11863440](https://pubmed.ncbi.nlm.nih.gov/11863440/) | *FAD-bound LASPO structure* | Holoenzyme (2.5 Å); FAD-induced 27° domain closure; E121 positioned at α-amino group; fumarate-reductase-like active site |
| [238844](https://pubmed.ncbi.nlm.nih.gov/238844/) | *De novo NAD biosynthesis: separating nadB from nadA* | NadB separable/soluble; NAD(H) feedback inhibition; aspartate + DHAP → quinolinate |
| [18959769](https://pubmed.ncbi.nlm.nih.gov/18959769/) | *LASPO and quinolinate synthase from B. subtilis* | NadA–NadB interaction functional, not species-specific |
| [20149100](https://pubmed.ncbi.nlm.nih.gov/20149100/) | *Two sources of endogenous H₂O₂ in E. coli* | NadB contributes 25–30% of endogenous H₂O₂; mechanism "adventitious" |
| [4349027](https://pubmed.ncbi.nlm.nih.gov/4349027/) | *Recognition of nadR* | NadR regulates NAD biosynthesis; *nadB* maps adjacent to *nadR* |
| [12446641](https://pubmed.ncbi.nlm.nih.gov/12446641/) | *Ribosylnicotinamide kinase domain of NadR* | NadR N-terminal DNA-binding domain controls NAD biosynthesis transcription |
| [22174382](https://pubmed.ncbi.nlm.nih.gov/22174382/) | *Nicotinamide dependence of UPEC UTI89* | nadB point mutation → NAD auxotrophy; complementation/reversion proof |
| [7737518](https://pubmed.ncbi.nlm.nih.gov/7737518/) | *P. aeruginosa nadB linkage* | Cross-species complementation confirms functional LASPO homolog |
| [2841129](https://pubmed.ncbi.nlm.nih.gov/2841129/) | *Cloning nadA and nadB* | Quinolinate = precursor of NAD pyridine ring; gene cloning |
| [34609124](https://pubmed.ncbi.nlm.nih.gov/34609124/) | *Transient second active-site cavity in NadA* | NadA condenses DHAP + iminoaspartate via dephosphorylation/isomerization/cyclization/dehydration |
| [26455817](https://pubmed.ncbi.nlm.nih.gov/26455817/) | *Dual activity of quinolinate synthase* | DHAP (not G3P) is the triose condensing with iminoaspartate |

Supporting context (same family / related activity): the flavocytochrome *c* fumarate reductase structure ([PMID: 10581551](https://pubmed.ncbi.nlm.nih.gov/10581551/)) documents the capping-domain/FAD-binding-domain catalytic mechanism that NadB shares, and recent work on *Synechocystis* L-aspartate oxidase ([PMID: 42742094](https://pubmed.ncbi.nlm.nih.gov/42742094/)) independently confirms the L-aspartate:fumarate oxidoreductase (succinate-generating) activity in a second organism, reinforcing the generality of this NadB side-reaction.

All cited snippets were verified against stored abstracts. The literature is internally consistent — there are no contradictory findings among the primary sources on NadB's core function.

---

## Limitations and Knowledge Gaps

1. **Physiological significance of fumarate reduction in vivo.** The fumarate reductase / L-aspartate:fumarate oxidoreductase activity is well documented biochemically in vitro and in *Synechocystis*, but its quantitative contribution to anaerobic succinate/fumarate metabolism in *E. coli* in vivo (relative to the dedicated Frd complex) has not been rigorously measured.

2. **Kinetic parameters not consolidated here.** While binding constants (Kd for fumarate/succinate/quinones) and the flavin midpoint potential are established, a consolidated set of steady-state kinetic constants (kcat, Km for L-aspartate) under physiological conditions was not a focus of this investigation.

3. **Direct iminoaspartate channeling.** NadA and NadB are not a tight complex, yet iminoaspartate is labile. Whether there is transient/functional channeling or simply rapid diffusive transfer in the cytoplasm remains mechanistically open, though the cross-species functional pairing suggests a conserved transfer interface.

4. **Regulatory quantitation.** The NadR-mediated transcriptional control of *nadB* specifically (vs. *nadA*) and the exact operator/promoter architecture were inferred from classical genetics and the broader regulon; promoter-level quantitation for *nadB* itself was not independently examined here.

5. **Structural coverage.** Crystal structures exist for the apo and FAD-bound (plus succinate) states, but a true Michaelis complex with L-aspartate (rather than succinate as an analog) and the catalytic intermediate have not been directly visualized.

---

## Proposed Follow-up Experiments / Actions

1. **In vivo flux dissection of the fumarate reductase role.** Use ¹³C-labeled aspartate and fumarate in anaerobic *E. coli* strains (wild type, Δ*nadB*, Δ*frd*) to quantify how much succinate derives from NadB versus the respiratory fumarate reductase, resolving Limitation #1.

2. **Complete steady-state kinetic characterization.** Determine kcat/Km for L-aspartate with O₂, fumarate, and quinone acceptors at matched conditions to build a unified kinetic model of the aerobic/anaerobic switch.

3. **Michaelis-complex and intermediate structures.** Trap and solve the L-aspartate–bound holoenzyme (e.g., with a non-oxidizable substrate analog or rapid cryo-trapping) to directly visualize the proposed E121/base geometry and the proton-abstraction step.

4. **Test functional channeling to NadA.** Use rapid-mixing/coupled-assay kinetics and crosslinking/interaction mapping to determine whether iminoaspartate is channeled or freely diffuses, and define the NadA–NadB interaction surface.

5. **Dissect H₂O₂ production physiologically.** Measure how the 25–30% endogenous H₂O₂ contribution from NadB varies with growth phase, oxygen tension, and de novo vs. salvage NAD conditions — connecting biosynthetic flux to oxidative stress.

6. **Promoter-level regulation of *nadB*.** Use reporter fusions and NadR binding assays on the *nadB* promoter specifically to quantify its transcriptional control within the NadR regulon and its response to NAD pool perturbation.

---

## Conclusion

The gene identity is fully confirmed: *nadB* (P10902) of *E. coli* K-12 encodes **L-aspartate oxidase (LASPO)**, the FAD-dependent entry enzyme of de novo NAD⁺ biosynthesis. Its primary function — oxidizing L-aspartate to iminoaspartate for condensation with DHAP by NadA to form quinolinate — is supported by convergent enzymological, structural, genetic, and regulatory evidence. Its defining mechanistic peculiarity is bifunctionality in electron acceptors (O₂ aerobically, fumarate anaerobically), rooted in its structural identity as a member of the succinate dehydrogenase/fumarate reductase flavoprotein family, adapted for aspartate oxidation by the single conserved glutamate E121. It is a soluble cytoplasmic enzyme, feedback-controlled by NAD(H) and transcriptionally regulated through NadR, and its loss causes NAD auxotrophy.


## Artifacts

- [OpenScientist final report](nadB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](nadB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:10425677
2. PMID:2841129
3. PMID:8706750
4. PMID:9405056
5. PMID:20149100
6. PMID:2187483
7. PMID:20600565
8. PMID:11294641
9. PMID:11863440
10. PMID:18959769
11. PMID:4349027
12. PMID:12446641
13. PMID:22174382
14. PMID:7737518
15. PMID:34609124
16. PMID:26455817
17. PMID:10581551
18. PMID:42742094