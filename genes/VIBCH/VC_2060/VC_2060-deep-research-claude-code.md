---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:32:51.195838'
end_time: '2026-10-30T21:36:35.345880'
duration_seconds: 224.15
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: VIBCH
  gene_id: parP
  gene_symbol: parP
  uniprot_accession: Q9KQE0
  protein_description: 'RecName: Full=CheW-like domain-containing protein {ECO:0000259|PROSITE:PS50851};'
  gene_info: OrderedLocusNames=VC_2060 {ECO:0000313|EMBL:AAF95206.1};
  organism_full: Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
  protein_family: Not specified in UniProt
  protein_domains: CheW-like_dom_sf. (IPR036061); CheW-lke_dom. (IPR002545); UCP020479_CheW.
    (IPR014506); CheW (PF01584)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 5
  num_turns: 10
  total_cost_usd: 0.814500695
  session_id: 8a88b688-bc41-46fe-9ed5-89e0aeaa6ee1
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 10
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9KQE0
- **Protein Description:** RecName: Full=CheW-like domain-containing protein {ECO:0000259|PROSITE:PS50851};
- **Gene Information:** OrderedLocusNames=VC_2060 {ECO:0000313|EMBL:AAF95206.1};
- **Organism (full):** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** CheW-like_dom_sf. (IPR036061); CheW-lke_dom. (IPR002545); UCP020479_CheW. (IPR014506); CheW (PF01584)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "parP" matches the protein description above**
2. **Verify the organism is correct:** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'parP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **parP** (gene ID: parP, UniProt: Q9KQE0) in VIBCH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

I've confirmed that VC_2060 is ParP, which the Ringgaard lab described in PNAS 2014 and eLife 2017. Next I'm pulling the specific findings from those papers.

# ParP (VC_2060, UniProt Q9KQE0) of *Vibrio cholerae* O1 El Tor N16961: research report

## Summary

Q9KQE0 is **ParP**, an adaptor that holds the chemotaxis signalling arrays at the cell pole. It does not catalyse any reaction or transport anything. ParP has two binding modules joined by a linker. The N-terminal domain binds the ParA-like ATPase **ParC**, which sits at the pole. The C-terminal CheW-like domain (SH3-like) inserts into the core signalling unit of the array, where it binds the receptors (MCPs) and the histidine kinase **CheA**. Because one protein carries both modules, building the array is coupled to placing it at the pole. ParP also keeps CheA from leaving the array. Loss of ParP leaves arrays mislocalised and less stable. Earlier work on the operon reported reduced chemotaxis in strains lacking ParC, attributed mainly to ParC's role in positioning ParP ([Ringgaard et al. 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3143943); [Ringgaard et al. 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC3896188)).

---

## 1. Checking that this is the right protein

| Check | Result |
|---|---|
| UniProt entry | Q9KQE0_VIBCH. TrEMBL (unreviewed), 338 aa, protein existence level 4 (Predicted). Named only "CheW-like domain-containing protein", locus VC_2060 |
| Does the symbol match? | **Yes.** Alvarado et al. (2017) give "parP NCBI GeneID 2613440 (vc2060)". The UniProt record cross-references DNASU 2613440, the same gene ID |
| Organism | *V. cholerae* O1 El Tor N16961 (taxon 243277). This is the strain used by the Waldor and Ringgaard labs |
| Domains | One CheW-like domain (PROSITE PS50851), residues 192–329. PIRSF020479 (UCP020479_CheW). Pfam PF01584 CheW. SMART SM00260. This matches the published C-terminal "CheW-like / SH3-like" array-integration domain |
| Neighbouring genes | parC (VC_2061, GeneID 2613441) lies directly upstream, cheW (VC_2059, GeneID 2613439) directly downstream, and cheA1 (VC_2063) nearby, all in chemotaxis operon/cluster II ([Alvarado et al. 2017](https://elifesciences.org/articles/31058); [Ringgaard et al. 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3143943)) |

**Other "ParP" names.** The symbol could be confused with unrelated "ParP"/"Par" proteins, such as plasmid partition proteins or poly(ADP-ribose) polymerases. All of the literature used here is specifically about the *Vibrio* chemotaxis protein ParP. No conflicting literature was used.

---

## 2. Domain architecture

UniProt residue ranges are given for the protein's 338 residues. Functional assignments come from [Alvarado et al. 2017](https://elifesciences.org/articles/31058).

1. **N-terminal ParC-interaction domain.** This domain is needed for ParP's own polar localisation and for recruiting arrays to the pole. It "enables polar recruitment of arrays and facilitates its own polar localization." Ringgaard et al. (2014) also report that ParP can dimerise through its N-terminus. The specific ParC-contacting residues have not been mapped.
2. **Long linker.** This region is rich in proline and acidic residues; the sequence around residues ~40–190 is low-complexity and Glu/Pro-rich. The paper describes "an N-terminal domain that is separated from AIF by a long proline-rich linker."
3. **C-terminal AIF domain** ("array integration and formation" domain), residues ~192–329. This is a predicted SH3-like fold "similar to CheW and the P5 domain of CheA." It has two separate binding surfaces:
   - **MCP-binding groove.** Residues L196, L209 and L212 are "almost 100% conserved amongst ParP proteins." The substitution **L209A** abolishes binding to MCPs but leaves CheA binding intact. I215A has no effect.
   - **CheA-binding surface.** The substitution **W305A** abolishes binding to CheA ("V. cholerae ParPW305A did not interact with CheA") and has little effect on MCP binding. L209 and W305 are "predicted to be positioned on opposite sides of the AIF domain." This was modelled on *Thermotoga maritima* CheW (PDB 3UR1).
   - The double mutant **ParP2PM** (L209A + W305A) binds neither partner. Neither substitution, alone or combined, prevents binding to ParC.

ParP is therefore a **natural fusion of a polar-anchor-binding module with a CheW-like coupling module**. UniProt's IPR014506/PIRSF020479 ("UCP020479_CheW") family captures this architecture, and it differs from the canonical standalone CheW.

---

## 3. Molecular function

### 3.1 Coupling to ParC, the polar anchor
- ParC (VC_2061) is a ParA/MinD-family ATPase in the same operon. It moves to the pole and actively promotes polar localisation of the chemotaxis proteins encoded with it. In newborn cells it sits at the flagellated old pole. As the cell matures it relocates to the new pole by a "diffusion and capture" mechanism ([Ringgaard et al. 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3143943)).
- ParP binds ParC. Ringgaard et al. (2014) conclude that "ParC's principal contribution to chemotaxis appears to be via positioning of ParP" ([PMC3896188](https://pmc.ncbi.nlm.nih.gov/articles/PMC3896188)). ParC is itself held at the pole by the landmark protein HubP (Yamaichi et al. 2012, as cited in the [2018 J. Bacteriol. review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6040185)). The resulting chain is **HubP → ParC → ParP → array**.

### 3.2 Integration into the core signalling unit of the array
- ParP's C-terminus "integrates into the core-unit of signaling arrays through interactions with MCP-proteins and CheA" ([Alvarado et al. 2017](https://elifesciences.org/articles/31058)).
- **MCPs.** A two-hybrid screen found 15 of the roughly 45 predicted *V. cholerae* MCPs as ParP partners; VC1898 gave the strongest signal. The interaction depends on conserved residues at the MCP signalling tip: VC1898 L518R, L521R, N522R and A524R disrupt it. These are the same tip residues that CheW and CheA-P5 contact. Eleven peer reviewers' comments (eLife) noted that the data suggest **ParP, CheA and CheW compete for the same MCP tip binding site**. The authors themselves "cannot rule out the possibility that ParP also is able to compete with CheW for integration into the core unit."
- **CheA.** ParP binds CheA (CheA1, VC_2063) through W305. Ringgaard et al. (2014), working mainly in *V. parahaemolyticus*, mapped the interaction to a CheA region called the "CheA-LID". This region occurs only in CheA proteins from organisms that have the ParC/ParP system, and a single ParP residue was critical for the contact. This is as cited secondhand in Alvarado et al. 2017; the PNAS full text could not be retrieved.

### 3.3 Holding CheA in the array
- After ParC recruits it to the pole, ParP "captures" CheA and **prevents its dissociation from arrays**. ParP also stabilises these complexes without ParC, so part of its activity does not depend on ParC ([Ringgaard et al. 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC3896188)).
- The authors propose a **tripartite ParC–ParP–CheA interaction network** that localises arrays to the pole and keeps them there in bacteria with a polar flagellum.

### 3.4 Promoting array formation (scaffold-like role)
- In Δ*cheA1* cells, arrays still form at the poles, mostly as in wild type. In **Δ*parP* Δ*cheA1*** cells, or with ParP lacking its AIF domain, chemotaxis clusters do not form: "formation of signaling arrays is severely compromised in the absence of both ParP and CheA." ParP's insertion into core units "stimulates array formation," which partly overlaps with CheA's role in building the array ([Alvarado et al. 2017](https://elifesciences.org/articles/31058)).
- Swapping ParP's AIF domain for the P5 domain of CheA restored polar clusters in 65% of Δ*parP*/Δ*cheA1* cells, compared with 0% without the swap. This shows the AIF domain works as a CheW/P5-type coupling module.

**What kind of function this is (for GO).** ParP is a non-enzymatic adaptor/scaffold. Its activities are protein–protein binding to ParC, to the MCP cytoplasmic tip and to CheA, and its role is structural: it organises the chemosensory array and anchors it to the pole. There is no evidence that it modulates CheA kinase activity directly, the way CheW couples receptors to the kinase. Alvarado et al. did not test kinase output.

---

## 4. Localisation

- **Cytoplasmic face of the cell pole.** YFP-ParP is polar in about 97% of wild-type cells. The array-interaction mutant (ParP2PM) is diffuse in about 40% of cells, so the array itself helps keep ParP at the pole ([Alvarado et al. 2017](https://elifesciences.org/articles/31058)).
- **Exchange at the pole (FRAP).** ParP exchanges with the polar pool continuously and reaches steady state in about 5 minutes. ParP2PM is released faster.
- **Effect on ParC.** In the *parP2PM* background, about 20% of cells show diffuse YFP-ParC, compared with about 4% in wild type. Integration into the array therefore stabilises the polar retention of both ParP and ParC. In the authors' words, ParP is "a critical nexus that regulates the localization dynamics of its network constituents."
- ParP has no transmembrane segment or signal peptide. It reaches the polar membrane region only through protein–protein contacts with ParC, the MCPs and the array.

---

## 5. Pathway context and phenotypes

**Pathway.** ParP belongs to the *V. cholerae* chemosensory system encoded in **chemotaxis cluster II**, the only one of the three clusters needed for chemotaxis toward chemoattractants. The pathway runs MCPs → CheW1/CheA1 → CheY3 → flagellar motor. ParP does not relay signals itself. It is an accessory organiser that sets **where** the array is assembled and how stably it holds together ([Ringgaard et al. 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3143943); [Alvarado et al. 2017](https://elifesciences.org/articles/31058)).

**Phenotypes:**

| Strain or allele | Phenotype | Source |
|---|---|---|
| Δ*parP* | Arrays (YFP-CheW1 reporter) not recruited to the poles; mislocalised along the cell length or absent in 74% of cells | Alvarado 2017 |
| *parP2PM* (L209A/W305A) | Similar to Δ*parP*: 65% of cells with mislocalised or absent arrays | Alvarado 2017 |
| L209A alone / W305A alone | Milder: 9% and 20% of cells affected, compared with about 6% in wild type | Alvarado 2017 |
| Δ*parP* Δ*cheA1*, or ΔAIF Δ*cheA1* | No arrays form | Alvarado 2017 |
| Δ*parP* (*V. parahaemolyticus*) | CheA dissociates from arrays; arrays not held at the pole | Ringgaard 2014 |
| Δ*parC* (functions upstream of ParP) | Chemotaxis protein foci mislocalised, chemotaxis reduced, motility altered, colonisation of the proximal small intestine in the infant-mouse cholera model increased | Ringgaard 2011 |

**Inference about inheritance.** Because arrays are not anchored to the poles in Δ*parP* cells, the authors expect that each daughter cell will not reliably inherit an array at division. They describe this as an inference, not a measured result.

---

## 6. Evolution and conservation

- ParP orthologs are encoded in chemotaxis operons, directly downstream of *parC*. The ParC/ParP pair is found in polarly flagellated γ-proteobacteria, including *V. cholerae*, *V. parahaemolyticus* and other Vibrionaceae ([Ringgaard et al. 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3143943); [Alvarado et al. 2017](https://elifesciences.org/articles/31058)).
- The MCP-binding residues of the AIF domain are almost invariant across ParP proteins. The CheA-LID region of CheA appears only in CheA proteins from genomes that have ParC/ParP, which points to co-evolution of the ParP–CheA interface (Ringgaard 2014, cited in Alvarado 2017).
- The [2018 J. Bacteriol. review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6040185) places ParP among the "CheW-like" array proteins. These include CheW, CheV and the CheA P5 domain, all of which bind MCP tips through the same SH3-like fold.

---

## 7. Notes for GO annotation

Existing annotations (GOA) are two IEA rows from InterPro2GO: **GO:0006935 chemotaxis** and **GO:0007165 signal transduction**.

- **Chemotaxis (GO:0006935).** Supported. ParP is a dedicated part of the cluster II chemotaxis machinery, and parP/parC mutants have altered chemotaxis and array organisation. This is the core process.
- **Signal transduction (GO:0007165).** Broad and only partly apt. ParP organises the signalling complex rather than relaying a signal. It is best treated as a non-core or general term.
- **Possible additions.** These should be grounded in Alvarado 2017 and Ringgaard 2014, and the term IDs should be checked in OLS before use:
  - A process term for organising or localising chemosensory arrays at the pole: protein localisation to the cell pole, or array assembly.
  - A cellular-component term for the cell pole (believed to be GO:0060187; not checked in OLS).
  - Molecular-function terms for adaptor or scaffold activity, rather than bare "protein binding". The binding partners are ParC, the MCP tip and CheA.
- **Evidence caveats.**
  - The CheA-retention data in Ringgaard 2014 come largely from *V. parahaemolyticus* ParP, which would support ISS-type transfer to this protein.
  - The array-formation and localisation data in Alvarado 2017 are direct *V. cholerae* experiments (VC_2060).
  - The ParP–MCP and ParP–CheA interaction data come mainly from bacterial two-hybrid assays.
- **Open questions.**
  - Which ParC residues and which N-terminal ParP residues form the ParC–ParP interface?
  - Does ParP displace CheW from some core units, and does that change kinase activation or receptor specificity?
  - How much of the ParC and ParP function is relevant during host colonisation?

---

## References

1. Ringgaard S, Zepeda-Rivera M, Wu X, Schirner K, Davis BM, Waldor MK. **ParP prevents dissociation of CheA from chemotactic signaling arrays and tethers them to a polar anchor.** *PNAS* 111(2):E255–E264. Published online Dec 30, 2013; issue dated Jan 14, 2014. PMID 24379357 (taken from secondary listings, not checked against PubMed). doi:10.1073/pnas.1315722111. https://pmc.ncbi.nlm.nih.gov/articles/PMC3896188 (the full text could not be fetched because of a bot-check page; the findings above come from the abstract, as described in search results, and from citations in Alvarado 2017).
2. Alvarado A, Kjær A, Yang W, Mann P, Briegel A, Waldor MK, Ringgaard S. **Coupling chemosensory array formation and localization.** *eLife* 6:e31058 (2017). doi:10.7554/eLife.31058. https://elifesciences.org/articles/31058 (full text read; also at https://pmc.ncbi.nlm.nih.gov/articles/PMC5706961; peer reviews at https://elifesciences.org/articles/31058/peer-reviews).
3. Ringgaard S, Schirner K, Davis BM, Waldor MK. **A family of ParA-like ATPases promotes cell pole maturation by facilitating polar localization of chemotaxis proteins.** *Genes Dev* 25:1544–1555 (2011). https://pmc.ncbi.nlm.nih.gov/articles/PMC3143943
4. Review of chemosensory array architecture and CheW-like proteins, *J. Bacteriol.* 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6040185
5. Ringgaard lab research page: Polar localization of chemotactic signaling arrays in *V. cholerae* and *V. parahaemolyticus*. https://www.mpi-marburg.mpg.de/ringgaard/research-area/chemotactic-signaling-arrays
6. Heidelberg JF et al. **DNA sequence of both chromosomes of the cholera pathogen *Vibrio cholerae*.** *Nature* 406:477–483 (2000). PMID 10952301 (genome annotation source for VC_2060).
7. UniProtKB Q9KQE0, entry version 88 (28 Jan 2026): domain annotations (PROSITE PS50851, Pfam PF01584, PIRSF020479, IPR014506) and DNASU 2613440 cross-reference.

Other sources consulted: Harvard DASH records for refs. 1 and 3 (https://dash.harvard.edu/entities/publication/b9ff9879-509d-457a-be14-986590cc4ccb ; https://dash.harvard.edu/entities/publication/ff71f76b-c99f-4412-8fef-2e6f875693e6) and the Marburg dissertation archive (https://archiv.ub.uni-marburg.de/diss/z2018/0533).

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC3143943
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC3896188
3. https://elifesciences.org/articles/31058
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC6040185
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC5706961
6. https://elifesciences.org/articles/31058/peer-reviews
7. https://www.mpi-marburg.mpg.de/ringgaard/research-area/chemotactic-signaling-arrays
8. https://dash.harvard.edu/entities/publication/b9ff9879-509d-457a-be14-986590cc4ccb
9. https://dash.harvard.edu/entities/publication/ff71f76b-c99f-4412-8fef-2e6f875693e6
10. https://archiv.ub.uni-marburg.de/diss/z2018/0533