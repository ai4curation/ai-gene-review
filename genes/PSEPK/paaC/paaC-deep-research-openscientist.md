---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T11:53:34.229411'
end_time: '2026-07-23T12:17:22.847341'
duration_seconds: 1428.62
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: paaC
  gene_symbol: paaC
  uniprot_accession: Q88HS7
  protein_description: 'SubName: Full=Ring 1,2-phenylacetyl-CoA epoxidase beta subunit
    {ECO:0000313|EMBL:AAN68883.1}; EC=1.14.13.149 {ECO:0000313|EMBL:AAN68883.1};'
  gene_info: Name=paaC {ECO:0000313|EMBL:AAN68883.1}; OrderedLocusNames=PP_3276 {ECO:0000313|EMBL:AAN68883.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Aromatic_CoA_ox/epox. (IPR052703); Ferritin-like. (IPR012347);
    Ferritin-like_SF. (IPR009078); PaaA_PaaC. (IPR007814); PaaC. (IPR011882)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
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
  path: paaC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: paaC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88HS7
- **Protein Description:** SubName: Full=Ring 1,2-phenylacetyl-CoA epoxidase beta subunit {ECO:0000313|EMBL:AAN68883.1}; EC=1.14.13.149 {ECO:0000313|EMBL:AAN68883.1};
- **Gene Information:** Name=paaC {ECO:0000313|EMBL:AAN68883.1}; OrderedLocusNames=PP_3276 {ECO:0000313|EMBL:AAN68883.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Aromatic_CoA_ox/epox. (IPR052703); Ferritin-like. (IPR012347); Ferritin-like_SF. (IPR009078); PaaA_PaaC. (IPR007814); PaaC. (IPR011882)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "paaC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'paaC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **paaC** (gene ID: paaC, UniProt: Q88HS7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: paaC (Q88HS7 / PP_3276) in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

- **UniProt:** Q88HS7 — "Ring 1,2-phenylacetyl-CoA epoxidase beta subunit"; EC 1.14.13.149
- **Gene:** *paaC*; OrderedLocusName **PP_3276**
- **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125)
- **Domains (InterPro):** Aromatic_CoA_ox/epox. (IPR052703); Ferritin-like (IPR012347); Ferritin-like_SF (IPR009078); PaaA_PaaC (IPR007814); PaaC (IPR011882)

**Verification outcome — CONFIRMED.** The gene symbol *paaC*, the "phenylacetyl-CoA epoxidase beta subunit" description, the ferritin-like/PaaC domain signatures, and the EC number all point consistently to the **β (structural) subunit of the bacterial phenylacetyl-CoA oxygenase/epoxidase complex** of the phenylacetic acid (PAA) catabolic pathway. This pathway is present in *E. coli* and *P. putida* and is among the best-characterized aerobic aromatic-degradation systems, so authoritative primary literature is abundant and directly applicable. The nomenclature (PaaA/B/C/D/E) is conserved between *E. coli* and *P. putida*; mechanistic and structural work performed in *E. coli* and *Azoarcus*/*Thermus* orthologs is transferable to the *P. putida* KT2440 protein.

---

## 1. Summary (Answer to the Research Question)

**paaC encodes the structural β subunit of the multicomponent phenylacetyl-CoA oxygenase/epoxidase (PaaABC(D)E).** The complex catalyzes the first committed, ring-activating step of aerobic phenylacetate catabolism: the O₂- and NADPH-dependent **1,2-epoxidation of the aromatic ring of phenylacetyl-CoA** to form ring-1,2-epoxyphenylacetyl-CoA (EC 1.14.13.149); the same complex can also deoxygenate this reactive epoxide. **PaaC itself is catalytically silent** — the diiron oxygen-activating center resides in the α subunit PaaA — but PaaC is **structurally indispensable**: it forms the PaaAC catalytic core, scaffolds and stabilizes the PaaA active site, participates in the higher-order PaaAC/PaaACB assembly, and is required for productive electron transfer from the reductase PaaE. The reaction takes place in the **cytoplasm**, acting on a cytoplasmic CoA-thioester substrate.

---

## 2. Primary Function and Substrate Specificity

### 2.1 The reaction
The PaaABC(D)E complex activates the otherwise inert aromatic ring of **phenylacetyl-CoA** by inserting an oxygen across the C1–C2 bond, producing **ring-1,2-epoxyphenylacetyl-CoA**:

> phenylacetyl-CoA + NADPH + H⁺ + O₂ → ring-1,2-epoxyphenylacetyl-CoA + NADP⁺ + H₂O  (EC 1.14.13.149)

Teufel *et al.* (2010) established that "the aromatic ring of phenylacetyl-CoA becomes activated to a ring 1,2-epoxide by a distinct multicomponent oxygenase," which is then isomerized to a seven-membered oxepin-CoA and hydrolytically cleaved (PMID 20660314). Teufel, Friedrich & Fuchs (2012) biochemically characterized the complex, showing PaaABCE "not only transforms phenylacetyl-CoA into its ring-1,2-epoxide, but also mediates the NADPH-dependent removal of the epoxide oxygen, regenerating phenylacetyl-CoA with formation of water" via "a catalytic di-iron centre" — i.e., it is a **bifunctional oxygenase/deoxygenase** that provides an intrinsic escape from its own toxic epoxide product (PMID 22398448).

### 2.2 Substrate specificity
The physiological substrate is the **CoA thioester** phenylacetyl-CoA, not free phenylacetate — a defining feature of this "hybrid" aerobic pathway in which all intermediates are CoA-activated (PMID 20660314). Crystallographic work with the *E. coli* ortholog captured the enzyme in complex with the true substrate phenylacetyl-CoA as well as related acyl-CoAs (CoA, 3-hydroxybutyryl-CoA, benzoyl-CoA), showing an active-site route adapted for a CoA-linked substrate (PMID 20823522, PMID 21247899).

### 2.3 Role of PaaC specifically
- **PaaA = catalytic α subunit; PaaC = structural β subunit.** "PaaAC forms a catalytic core with a monooxygenase fold with PaaA being the catalytic α subunit and PaaC, the structural β subunit" (Grishin *et al.* 2011, PMID 21247899).
- **PaaC is required for catalysis.** In vitro reconstitution showed "each of the PaaA, B, C, and E subunits are necessary for catalysis, whereas PaaD is not essential" (PMID 21247899).
- **Fold/family.** PaaC adopts a **ferritin-like/diiron (bacterial multicomponent monooxygenase-like) fold** but functions as the non-catalytic β partner; the enzyme constitutes "the prototype of a new and distinct group of the large bacterial diiron multicomponent oxygenase family" (PMID 16997993) — a "new family of monooxygenases" differing in subunit organization (PMID 24055609). This is consistent with the InterPro ferritin-like and PaaA_PaaC/PaaC domain annotations for Q88HS7.

---

## 3. Quaternary Structure and Molecular Mechanism

- **Catalytic core.** PaaAC forms heterotetramers "organized very differently from other known multisubunit monooxygenases" (PMID 21247899).
- **Higher-order assembly.** With PaaB, "the PaaACB complex forms heterohexamers, with a homodimer of PaaB bridging two PaaAC heterodimers" (Grishin *et al.* 2013, PMID 24055609).
- **Electron transfer.** The reductase PaaE feeds electrons to PaaA's diiron center; a conserved "lysine bridge" near the Fe site is part of the electron-transfer path, and mutants show 20–50× reduced activity (PMID 24055609). PaaC scaffolds this core and thereby enables oxygen activation.
- **Interpretation of PaaC's role.** PaaC lacks a complete iron-liganding set (it is the structural β subunit) but is an integral, obligatory component of the oligomeric catalytic machine: it positions and stabilizes PaaA's diiron active site and contributes to assembly competent for reductase coupling.

---

## 4. Biological Process and Pathway Context

paaC operates within the **phenylacetic acid "catabolon"**, "the best characterized aerobic hybrid route involved in the bacterial degradation of aromatic compounds" (Fernández *et al.* 2014, PMID 24983528). The pathway:

1. **Activation:** phenylacetate → phenylacetyl-CoA (phenylacetyl-CoA ligase, PaaK/PaaF).
2. **Ring epoxidation (this enzyme):** phenylacetyl-CoA → ring-1,2-epoxyphenylacetyl-CoA (PaaABC(D)E; PaaC = β subunit).
3. **Isomerization:** epoxide → oxepin-CoA.
4. **Ring cleavage:** hydrolytic cleavage by PaaZ (bifunctional oxepin-CoA hydrolase/aldehyde dehydrogenase; PMID 21296885).
5. **β-oxidation:** to **acetyl-CoA + succinyl-CoA**, feeding the TCA cycle (PMID 20660314).

This route is the **funneling hub** for catabolism of upstream aromatics including **phenylalanine, styrene/ethylbenzene, 2-phenylethylamine, and n-phenylalkanoic acids**, allowing *P. putida* to use them as carbon and energy sources (PMID 20660314). The reactive epoxide/aldehyde branch intermediates are also the biosynthetic entry point to tropone/tropolone natural products in some bacteria (PMID 21296885, PMID 34196542), underscoring the pathway's metabolic importance.

**Regulation in *P. putida* KT2440 (target organism):** paa genes are inducible by PAA and repressed by a PaaX-type regulator responsive to phenylacetyl-CoA (PMID 24983528). PAA metabolism is under **carbon catabolite repression** in KT2440, with intracellular 2-keto-3-deoxy-6-phosphogluconate (KDPG) identified as the CCR signal — glucose/gluconate suppress paa expression and phenylacetyl-CoA ligase activity (Kim *et al.* 2009, PMID 19406896). PAA is additionally a **chemoattractant** for *P. putida* F1, sensed by the energy-taxis receptor Aer2 and dependent on active PAA metabolism (PMID 23377939).

---

## 5. Subcellular Localization

The enzyme is a **soluble, cytoplasmic** multicomponent oxygenase. Two lines of evidence support cytoplasmic action: (i) the substrate is a **cytoplasmic CoA thioester** (phenylacetyl-CoA), and CoA-activated intermediates are membrane-impermeant metabolites of central carbon metabolism; and (ii) the complex has been purified as soluble subunits/subcomplexes and crystallized (PaaAC, PaaACB), with no membrane-spanning segments reported (PMID 21247899, PMID 24055609). No signal-peptide or transmembrane features are indicated for the paaC β subunit. Thus paaC carries out its structural role **inside the cytoplasm**, as part of the soluble PAA-degradation machinery.

---

## 6. Supported and Refuted Hypotheses

**Supported**
- *paaC is the structural β subunit of the phenylacetyl-CoA oxygenase/epoxidase* — supported by crystallographic and reconstitution data (PMID 21247899, 24055609, 16997993).
- *The complex epoxidizes the phenylacetyl-CoA ring (EC 1.14.13.149) and can deoxygenate the epoxide* — supported by direct biochemistry (PMID 22398448, 20660314).
- *paaC acts in the cytoplasm within the aerobic PAA catabolon* — supported by pathway biochemistry and substrate chemistry (PMID 20660314, 24983528).

**Refuted / corrected**
- *"Ring hydroxylase" (simple aromatic hydroxylation)* — the older annotation (e.g., "hydroxylates phenylacetyl-CoA," PMID 16997993) was **superseded**: the true product is a **ring-1,2-epoxide**, not a phenol (PMID 20660314, 22398448). The UniProt "epoxidase" naming reflects this correction.
- *PaaC is catalytic* — refuted; catalysis (diiron chemistry) resides in **PaaA**, with PaaC serving a structural role (PMID 21247899).

---

## 7. Limitations and Future Directions

- Direct biochemical/structural characterization has been performed largely on *E. coli* (and *Azoarcus/Thermus/Aromatoleum*) orthologs; the specific *P. putida* KT2440 PaaC has been characterized chiefly by genomic/regulatory studies and by orthology, not by its own crystal structure. Given the high conservation of the paa cluster, transfer of function is well justified but not experimentally proven for PP_3276 in isolation.
- The precise contribution of PaaC residues to diiron-site geometry and to PaaE coupling in *P. putida* would benefit from targeted mutagenesis and a *P. putida*-specific structure (e.g., cryo-EM of PaaABCE).
- Note on nomenclature: some *P. putida* literature (e.g., the Luengo group's *P. putida* U studies) uses alternative gene labels for the oxygenase subunits; care is needed when mapping names across strains, but the KT2440 UniProt annotation (paaC = β subunit) is internally consistent with the *E. coli* PaaABCDE scheme.

---

## Key References
- Teufel R, *et al.* Bacterial phenylalanine and phenylacetate catabolic pathway revealed. *PNAS* 2010. **PMID 20660314**
- Teufel R, Friedrich T, Fuchs G. An oxygenase that forms and deoxygenates toxic epoxide. *Nature* 2012. **PMID 22398448**
- Grishin AM, *et al.* Structural and functional studies of the *E. coli* phenylacetyl-CoA monooxygenase complex. 2011. **PMID 21247899**
- Grishin AM, *et al.* Family of phenylacetyl-CoA monooxygenases differs in subunit organization. 2013. **PMID 24055609**
- Grishin AM, *et al.* Crystallization/X-ray analysis of PaaAC. 2010. **PMID 20823522**
- Fernández C, *et al.* Genetic characterization of the phenylacetyl-CoA oxygenase from *E. coli*. 2006. **PMID 16997993**
- Teufel R, *et al.* Studies on the mechanism of ring hydrolysis (PaaZ). 2011. **PMID 21296885**
- Fernández C, Díaz E, García JL. Regulation of the phenylacetate degradation pathway from *E. coli*. 2014. **PMID 24983528**
- Kim J, *et al.* KDPG is the signal for CCR of PAA metabolism in *P. putida* KT2440. 2009. **PMID 19406896**
- Luu RA, *et al.* Taxis of *P. putida* F1 toward phenylacetic acid via Aer2. 2013. **PMID 23377939**


## Artifacts

- [OpenScientist final report](paaC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](paaC-deep-research-openscientist_artifacts/final_report.pdf)