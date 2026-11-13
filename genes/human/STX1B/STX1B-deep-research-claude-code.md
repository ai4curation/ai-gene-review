---
provider: claude_code
cached: false
start_time: '2026-11-13T15:49:27.705983'
end_time: '2026-11-13T15:51:44.016504'
duration_seconds: 136.31
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: STX1B
  gene_symbol: STX1B
  uniprot_accession: P61266
  protein_description: 'RecName: Full=Syntaxin-1B; AltName: Full=Syntaxin-1B1; AltName:
    Full=Syntaxin-1B2;'
  gene_info: Name=STX1B; Synonyms=STX1B1, STX1B2;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the syntaxin family. .
  protein_domains: SNARE. (IPR010989); Syntaxin. (IPR045242); Syntaxin/epimorphin_CS.
    (IPR006012); Syntaxin_N. (IPR006011); T_SNARE_dom. (IPR000727)
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
  web_search_requests: 16
  num_turns: 19
  total_cost_usd: 2.2525250999999997
  session_id: 712cbafd-bb7b-48e8-b32b-2d6ddfa32fe0
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 26
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P61266
- **Protein Description:** RecName: Full=Syntaxin-1B; AltName: Full=Syntaxin-1B1; AltName: Full=Syntaxin-1B2;
- **Gene Information:** Name=STX1B; Synonyms=STX1B1, STX1B2;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the syntaxin family. .
- **Key Domains:** SNARE. (IPR010989); Syntaxin. (IPR045242); Syntaxin/epimorphin_CS. (IPR006012); Syntaxin_N. (IPR006011); T_SNARE_dom. (IPR000727)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "STX1B" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'STX1B' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **STX1B** (gene ID: STX1B, UniProt: P61266) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# STX1B (Syntaxin-1B; UniProt P61266) in *Homo sapiens*: research report for functional annotation

## 1. Identity verification

The target is unambiguous. STX1B (synonyms STX1B1, STX1B2; chromosome 16p11.2; MIM 601485) encodes syntaxin-1B, a member of the syntaxin family with an N-terminal Habc domain (Syntaxin_N, IPR006011) and a t-SNARE coiled-coil homology domain (IPR000727). The literature retrieved matches this protein and its rodent and zebrafish orthologues; no conflicting gene with the same symbol was found.

Scope of the evidence:

- **Direct human evidence** is limited to disease genetics, a splice-isoform localisation study, and interaction screens.
- **Mechanistic evidence** comes mostly from mouse *Stx1b* models, and structurally from the ~84%-identical paralogue syntaxin-1A (STX1A).
- **Verification level:** findings below were checked against abstracts and search summaries in this session, not full texts. Entries marked "from memory" in the source list were not retrieved in this session, and their identifiers should be confirmed before reuse.

## 2. Key concepts: what the protein is

Syntaxin-1B is a neuronal plasma-membrane Qa-SNARE (t-SNARE). It is not an enzyme or transporter; its molecular function is SNAP receptor (SNARE) activity.

Domain organisation, as established for syntaxin-1:

- **N-peptide:** a short N-terminal segment that contributes to Munc18-1 (STXBP1) binding.
- **Habc domain:** an autoinhibitory three-helix bundle that folds back onto the SNARE motif to give a "closed" conformation bound by Munc18-1.
- **SNARE motif (H3):** contributes one helix (Qa) to the four-helix SNARE bundle formed with SNAP-25 (Qb, Qc) and synaptobrevin/VAMP2 (R). Zippering of this bundle drives fusion of the synaptic vesicle with the presynaptic plasma membrane.
- **Juxtamembrane region and C-terminal transmembrane anchor:** a tail-anchored (type IV) topology with the functional domains in the cytoplasm.

The atomic structures behind this model (the neuronal SNARE core complex and the Munc18-1–syntaxin closed complex) were solved with syntaxin-1A. Applying them to STX1B is an inference from homology, supported by the mouse genetics below.

## 3. Primary function: evidence from mouse genetics

### 3.1 Syntaxin-1B is the principal syntaxin-1 for central synaptic transmission

- *Stx1b*-null mice die within two weeks of birth, whereas *Stx1a*-null mice are viable. In cultured null neurons, spontaneous quantal release is less frequent and the paired-pulse ratio is higher at both glutamatergic and GABAergic synapses. The paper's title conclusion is that syntaxin 1B, but not 1A, is necessary for regulating synaptic vesicle exocytosis and the readily releasable pool. Munc18-1 levels fall with *Stx1b* gene dosage. ([Mishima et al. 2014, PLoS ONE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3938564))
- An independent knockout line gave the same lethality: mice weighed less from postnatal day 5 and all died before day 13. Removing STX1B only from forebrain excitatory neurons also caused premature death. STX1B was dispensable for forming the neuromuscular junction but required for efficient transmission there. ([Wu et al. 2015, J Neurophysiol](https://pubmed.ncbi.nlm.nih.gov/26203110/); [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4620129))

### 3.2 Conformational gating of fusion (shown directly on syntaxin-1B)

Gerber et al. made mice expressing only a constitutively "open" syntaxin-1B on a syntaxin-1A-knockout background. In these synapses:

- Munc18-1 binding to syntaxin-1 was impaired.
- The readily releasable pool was smaller, yet the rate of vesicle fusion was strongly increased.
- Chromaffin granule docking was impaired, but synaptic vesicle docking was not.

The authors concluded that the closed conformation of syntaxin-1 gates the initiation of fusion. ([Gerber et al. 2008, Science](https://utsouthwestern.elsevierpure.com/en/publications/conformational-switch-of-syntaxin-1-controls-synaptic-vesicle-fus))

### 3.3 Separable roles in docking, priming/fusion and neuronal maintenance

- Loss of all syntaxin-1 severely reduces neuronal viability in both developing and mature neurons, as well as abolishing transmission. A mutant forming less stable SNARE complexes restored survival and docking but not fusion. The authors concluded that full SNARE assembly is needed for priming and fusion, while partial assembly suffices for docking and maintenance. ([Vardar et al. 2016, J Neurosci](https://pmc.ncbi.nlm.nih.gov/articles/PMC6601879))
- The Habc domain is required for syntaxin-1 stability or expression and therefore for release; the N-peptide is not indispensable. Loss of syntaxin-1 severely reduces Munc18-1, and either STX1A or STX1B restores it. ([Vardar et al. 2021, eLife](https://pmc.ncbi.nlm.nih.gov/articles/PMC8416022))
- Earlier work on the N-peptide and Habc domain reached a partly different view of their essential roles. ([Zhou et al. 2013](https://pubmed.ncbi.nlm.nih.gov/23188083/))
- A 2022 eLife study from the same group examined the juxtamembrane and transmembrane regions of syntaxin-1. Search returned only the link, so I did not verify its findings. ([Vardar et al. 2022, eLife](https://pmc.ncbi.nlm.nih.gov/articles/PMC9183232))

### 3.4 Neuronal survival and a possible glial role

- Hippocampal *Stx1b*-null neurons showed lower viability after 9 days in culture than wild-type or *Stx1a*-null neurons. They survived on wild-type glia or with added BDNF or neurotrophin-3. BDNF localisation and secretion were disrupted in null glia. The authors proposed that STX1B supports survival partly by regulating neurotrophin secretion from glia. ([Kofuji et al. 2014, J Neurochem](https://zendy.io/title/10.1111/jnc.12722))
- Wu et al. also concluded that STX1B is essential for neuronal survival in vitro, attributing reduced GABAergic event frequency in knockout cerebellar cultures mostly to fewer surviving neurons. ([Wu et al. 2015](https://pubmed.ncbi.nlm.nih.gov/26203110/))

The glial BDNF finding rests on a single group and is best treated as a secondary, less established role.

### 3.5 Inhibitory transmission and temperature sensitivity

Heterozygous *Stx1b* mice are more susceptible to febrile and drug-induced seizures. In wild-type cultured hippocampal neurons, hyperthermia reduced recurrent bursting in a GABA-dependent manner; this was lost in *Stx1b*+/− neurons. A companion report found reduced spontaneous quantal GABA release. ([Mishima et al. 2021, J Neurochem](https://zendy.io/title/10.1111/jnc.15159))

A 2024 Tübingen PhD thesis, which is not peer-reviewed, reports a larger hyperthermia-induced rise in neuronal activity in *Stx1b*+/− mice than in wild type. ([thesis record](https://publikationen.uni-tuebingen.de/xmlui/handle/10900/159674))

## 4. Localisation

- **Canonical isoform 1 (288 aa):** a tail-anchored membrane protein of the presynaptic plasma membrane and active zone, with cytoplasmic functional domains. UniProt records "Membrane; single-pass type IV" for the human protein by inference; the presynaptic assignment comes from rodent work.
- **Regional distribution** differs from syntaxin-1A:
  - In rat CNS, isoform-specific antibodies gave distinct patterns in the olfactory system, hippocampus, striatum, thalamus, spinal cord and white-matter commissures. ([Ruiz-Montasell et al. 1996, Eur J Neurosci](https://www.scilit.net/publications/be7690ab92e41336e956ac9ac5929953))
  - In rat PNS, sensory terminals reaching the spinal cord were enriched in syntaxin-1A, while motor endplates and muscle spindles stained only for syntaxin-1B; enteric plexuses had both. ([Aguado et al. 1999, Neuroscience](https://data.zhenzhi.com/details/1/883030327))
  - This fits the neuromuscular junction defect in *Stx1b* knockouts.
- **Isoform 2 (STX1B-ΔTMD, 277 aa):** a human splice variant in which the transmembrane domain is replaced by a glycine-rich C-terminus that acts as an unconventional nuclear localisation signal. UniProt (citing PMID:18691641) records it in the nucleus with lamin A/C and NuMA, and at the pericentrosomal region of the mitotic spindle with NuMA and γ-tubulin. ([Pereira et al. 2008, Gene 423:160–171; DOI 10.1016/j.gene.2008.07.010](https://doi.org/10.1016/j.gene.2008.07.010))

The nucleus, nucleoplasm, nuclear lamina, centrosome and spindle annotations in GOA all trace to this one isoform-2 study. They describe a minor soluble variant of unknown function, not the site of the core SNARE function.

## 5. Pathway and interaction context

- **Pathway:** the synaptic vesicle cycle, at the docking, priming and Ca²⁺-triggered fusion steps. Partners are SNAP-25, VAMP2/synaptobrevin-2, Munc18-1 (chaperone and fusion template), Munc13 (opens syntaxin), and downstream synaptotagmin and complexin. The Munc13, synaptotagmin and complexin steps are the standard model and were not retrieved in this session.
- **Human interaction data (UniProt/IntAct):** binary interactions with VAMP1, VAMP2, VAMP5, SNAP29, SNAP47, STX2, STX4, BET1 and NAPB (β-SNAP) are consistent with SNARE and SNARE-recycling biology. These are high-throughput and identify no function on their own.
- **By-similarity statements in UniProt:** interaction with otoferlin, Ca²⁺-dependent interaction with SYT6 and SYT8, a possible role in the sperm acrosome reaction, and phosphorylation by CK2. I could not retrieve the primary papers for these. One sperm study does report trans-SNARE complexes of VAMP3, syntaxin 1B and SNAP-23 forming during capacitation in boar sperm. ([PLoS ONE study](https://pmc.ncbi.nlm.nih.gov/articles/PMC2887851))
- **Toxin substrate:** botulinum neurotoxin C cleaves syntaxin-1A at Lys253–Ala254 and syntaxin-1B at Lys252–Ala253, only when membrane-inserted. This underlies the Reactome pathway R-HSA-5250971 and independently confirms that syntaxin-1 is required for release. ([Schiavo et al. 1995](https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/pubmed/7737992); [cleavage-site review table](https://pmc.ncbi.nlm.nih.gov/articles/PMC2730986/table/T1))

In all of these, syntaxin-1B is a working component of the fusion machinery: its SNARE motif forms part of the bundle that does the fusing. For BoNT/C it is only the substrate.

## 6. Human disease

### 6.1 Fever-associated epilepsy (GEFS+9, MIM 616172)

- Exome sequencing in large pedigrees found co-segregating STX1B variants predicted to truncate the protein or cause an in-frame insertion/deletion. Three further nonsense or missense variants and a de novo microdeletion were found among 449 additional cases.
- Zebrafish *stx1b* knockdown produced seizure-like behaviour and epileptiform discharges that were highly temperature-sensitive. Wild-type human syntaxin-1B rescued this; a mutant did not. This is the main direct functional evidence for the human protein.

([Schubert et al. 2014, Nat Genet](https://researchinformation.umcutrecht.nl/en/publications/mutations-in-stx1b-encoding-a-presynaptic-protein-cause-fever-ass/))

### 6.2 Clinical spectrum

- A series of 49 patients in 23 families with 17 new variants described four phenotypic groups, from benign febrile/afebrile seizure syndromes to intractable epilepsy with developmental regression, plus a few focal epilepsies.
- Loss-of-function variants were more often found in benign syndromes; missense variants in the SNARE motif went with more severe phenotypes.

([Wolking et al. 2019, Neurology](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6511102/))

Haploinsufficiency has also been linked to myoclonic-astatic epilepsy. ([Vlaskamp et al. 2016](https://api-pubmed-ncbi.laibokeji.com/26818399))

### 6.3 Variant mechanisms

Vardar et al. tested three patient variants in mouse neurons and found three distinct mechanisms:

| Variant | Clinical severity | Effect |
|---|---|---|
| G226R | Epileptic encephalopathy | Strongly impairs Munc18-1 interaction; lowers both proteins, the readily releasable pool and Ca²⁺-triggered release |
| V216E | Milder | Slightly reduces Munc18-1 and Munc13 interactions; increases fusogenicity and release probability |
| Habc insertion/deletion | — | Unfolded protein unable to sustain transmission |

Synaptic output was unchanged in excitatory *Stx1b*+/− neurons expressing the mutants. ([Vardar et al. 2020, Brain](https://zendy.io/title/10.1093/brain/awaa151))

### 6.4 Parkinson's disease association

A 2011 IPDGC meta-analysis identified a 16p11 risk locus with lead SNP rs4889603. The nearest gene is SETD1A; the authors named the locus STX1B because it lies 18 kb away and is a more plausible candidate, and they reported that the risk allele correlated with methylation of a CpG site in STX1B. ([IPDGC 2011, PLoS Genet](https://pmc.ncbi.nlm.nih.gov/articles/PMC3128098))

A later Chinese case-control study replicated rs4889603. ([RIT2 and STX1B polymorphisms study](https://www.bohrium.com/paper-details/the-rit2-and-stx1b-polymorphisms-are-associated-with-parkinson-s-disease/814669321123921920-11663)) This is a statistical association with a locus, not evidence about the protein's function.

## 7. Recent developments (2020–2024)

- The main mechanistic advances are the variant-mechanism study (2020), the Habc/N-peptide re-examination (2021) and the GABA-release/hyperthermia work in heterozygous mice (2021), all cited above.
- A [2021 Frontiers in Neurology mini-review](https://www.frontiersin.org/articles/10.3389/fneur.2021.806506) summarises the genotype–phenotype picture.
- I found no peer-reviewed 2023–2024 zebrafish or iPSC functional study of STX1B. The one 2024 item is the unreviewed thesis above. A direct PubMed query would be needed to confirm that nothing was missed.

## 8. Synthesis for annotation

**Core function (well supported):**

- **Molecular function:** SNAP receptor activity and SNARE binding, as the Qa-SNARE of the neuronal SNARE complex with SNAP-25 and VAMP2, regulated by Munc18-1.
- **Process:** synaptic vesicle priming and Ca²⁺-triggered fusion with the presynaptic active-zone membrane, i.e. neurotransmitter secretion at glutamatergic, GABAergic and neuromuscular synapses.
- **Location:** presynaptic active-zone plasma membrane, in the SNARE complex.

**Points that bear on reviewing the existing GO annotations:**

- **Docking:** the syntaxin-1B open mutant did not impair synaptic vesicle docking, though it impaired chromaffin granule docking; the 2016 study ties docking to partial SNARE assembly. A "vesicle docking activity" annotation is defensible but less directly supported than priming and fusion.
- **"Negative regulation of synaptic vesicle recycling" and "positive regulation of spontaneous neurotransmitter secretion"** (Ensembl IEA): the knockout data show reduced spontaneous release, consistent with a positive role, but I found nothing supporting an effect on recycling.
- **Nuclear, lamina, centrosome and spindle terms:** isoform 2 only, single study, no functional consequence shown.
- **"Negative regulation of neuron projection development", "regulation of gene expression", "protein kinase binding", "negative regulation of macropinocytosis"** (ISS, ParkinsonsUK-UCL): I did not identify the source orthologue papers; they need checking against the cited rodent references.
- **"Synaptic vesicle membrane"** (NAS, ComplexPortal): syntaxin-1 is predominantly a plasma-membrane SNARE; nothing retrieved here addresses a vesicular pool for STX1B specifically.
- **"Cytosol"** (Reactome TAS): conflicts with the tail-anchored topology of isoform 1 and probably reflects the cytosolic orientation of the domains or the toxin pathway context.
- **Neuronal survival:** robustly shown but mechanistically unresolved (cell-autonomous Munc18-1/SNARE role versus glial neurotrophin secretion); better treated as non-core.

**Open questions:**

- Why syntaxin-1A cannot compensate for 1B loss in vivo (expression pattern versus intrinsic differences).
- The basis of the temperature sensitivity.
- Whether the nuclear isoform has any function.

## Sources

Retrieved in this session:

- [Mishima et al. 2014, PLoS ONE (PMC3938564)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3938564)
- [Wu et al. 2015, J Neurophysiol 114:2404–2417 (PMID 26203110)](https://pubmed.ncbi.nlm.nih.gov/26203110/) and [PMC4620129](https://pmc.ncbi.nlm.nih.gov/articles/PMC4620129)
- [Kofuji et al. 2014, J Neurochem 130:514–525](https://zendy.io/title/10.1111/jnc.12722) ([PMID 24666284 record](https://pesquisa.bvsalud.org/brasil/resource/en/mdl-24666284))
- [Gerber et al. 2008, Science 321:1507–1510, DOI 10.1126/science.1163174](https://utsouthwestern.elsevierpure.com/en/publications/conformational-switch-of-syntaxin-1-controls-synaptic-vesicle-fus)
- [Vardar et al. 2016, J Neurosci 36:7911–7924 (PMC6601879)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6601879)
- [Vardar et al. 2020, Brain, DOI 10.1093/brain/awaa151](https://zendy.io/title/10.1093/brain/awaa151) ([PMID 32572454 record](https://pesquisa.bvsalud.org/bvsvs/resource/es/mdl-32572454))
- [Vardar et al. 2021, eLife 69498 (PMC8416022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8416022)
- [Vardar et al. 2022, eLife 78182 (PMC9183232)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9183232) — link only, content not verified
- [Zhou et al. 2013 (PMID 23188083)](https://pubmed.ncbi.nlm.nih.gov/23188083/)
- [Schubert et al. 2014, Nat Genet 46:1327–1332, DOI 10.1038/ng.3130](https://researchinformation.umcutrecht.nl/en/publications/mutations-in-stx1b-encoding-a-presynaptic-protein-cause-fever-ass/)
- [Wolking et al. 2019, Neurology 92:e1238–e1249 (PMC6511102)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6511102/)
- [Vlaskamp et al. 2016 (PMID 26818399)](https://api-pubmed-ncbi.laibokeji.com/26818399)
- [Mishima et al. 2021, J Neurochem, DOI 10.1111/jnc.15159](https://zendy.io/title/10.1111/jnc.15159)
- [Frontiers in Neurology mini-review, 2021](https://www.frontiersin.org/articles/10.3389/fneur.2021.806506)
- [Tübingen PhD thesis, 2024](https://publikationen.uni-tuebingen.de/xmlui/handle/10900/159674)
- [Ruiz-Montasell et al. 1996, Eur J Neurosci 8:2544–2552](https://www.scilit.net/publications/be7690ab92e41336e956ac9ac5929953)
- [Aguado et al. 1999, Neuroscience 88:437–446](https://data.zhenzhi.com/details/1/883030327)
- [Schiavo et al. 1995 (PMID 7737992)](https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/pubmed/7737992)
- [BoNT cleavage-site table (PMC2730986)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2730986/table/T1)
- [Sperm trans-SNARE study, PLoS ONE (PMC2887851)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2887851)
- [IPDGC 2011, PLoS Genet (PMC3128098)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3128098)
- [RIT2 and STX1B polymorphisms in Parkinson's disease](https://www.bohrium.com/paper-details/the-rit2-and-stx1b-polymorphisms-are-associated-with-parkinson-s-disease/814669321123921920-11663)
- Local UniProt record for P61266 (`genes/human/STX1B/STX1B-uniprot.txt`), for function, subunit, isoform, localisation, disease and interaction statements.

From memory, not retrieved in this session:

- Pereira et al. 2008, Gene 423:160–171 (PMID 18691641). The identifiers are confirmed by the UniProt record, but the first-author name is from memory and search results gave conflicting author lists.
- The syntaxin-1A structural papers behind section 2 (SNARE core complex; Munc18-1–syntaxin-1A complex) and the original syntaxin cloning papers.

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC3938564
2. https://pubmed.ncbi.nlm.nih.gov/26203110/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC4620129
4. https://utsouthwestern.elsevierpure.com/en/publications/conformational-switch-of-syntaxin-1-controls-synaptic-vesicle-fus
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC6601879
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC8416022
7. https://pubmed.ncbi.nlm.nih.gov/23188083/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC9183232
9. https://zendy.io/title/10.1111/jnc.12722
10. https://zendy.io/title/10.1111/jnc.15159
11. https://publikationen.uni-tuebingen.de/xmlui/handle/10900/159674
12. https://www.scilit.net/publications/be7690ab92e41336e956ac9ac5929953
13. https://data.zhenzhi.com/details/1/883030327
14. https://doi.org/10.1016/j.gene.2008.07.010
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC2887851
16. https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/pubmed/7737992
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC2730986/table/T1
18. https://researchinformation.umcutrecht.nl/en/publications/mutations-in-stx1b-encoding-a-presynaptic-protein-cause-fever-ass/
19. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6511102/
20. https://api-pubmed-ncbi.laibokeji.com/26818399
21. https://zendy.io/title/10.1093/brain/awaa151
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC3128098
23. https://www.bohrium.com/paper-details/the-rit2-and-stx1b-polymorphisms-are-associated-with-parkinson-s-disease/814669321123921920-11663
24. https://www.frontiersin.org/articles/10.3389/fneur.2021.806506
25. https://pesquisa.bvsalud.org/brasil/resource/en/mdl-24666284
26. https://pesquisa.bvsalud.org/bvsvs/resource/es/mdl-32572454