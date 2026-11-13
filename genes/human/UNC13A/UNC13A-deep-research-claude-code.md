---
provider: claude_code
cached: false
start_time: '2026-11-13T01:31:10.714847'
end_time: '2026-11-13T01:32:51.545357'
duration_seconds: 100.83
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: UNC13A
  gene_symbol: UNC13A
  uniprot_accession: Q9UPW8
  protein_description: 'RecName: Full=Protein unc-13 homolog A {ECO:0000305}; AltName:
    Full=Munc13-1;'
  gene_info: Name=UNC13A {ECO:0000312|HGNC:HGNC:23150}; Synonyms=KIAA1032;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the unc-13 family. .
  protein_domains: C1-like_sf. (IPR046349); C2_dom. (IPR000008); C2_domain_sf. (IPR035892);
    MUN_dom. (IPR010439); Munc13_1. (IPR014770)
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
  web_search_requests: 6
  num_turns: 9
  total_cost_usd: 1.7385643
  session_id: 49f1482c-005b-495b-aa88-1efad7e34397
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 14
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q9UPW8
- **Protein Description:** RecName: Full=Protein unc-13 homolog A {ECO:0000305}; AltName: Full=Munc13-1;
- **Gene Information:** Name=UNC13A {ECO:0000312|HGNC:HGNC:23150}; Synonyms=KIAA1032;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the unc-13 family. .
- **Key Domains:** C1-like_sf. (IPR046349); C2_dom. (IPR000008); C2_domain_sf. (IPR035892); MUN_dom. (IPR010439); Munc13_1. (IPR014770)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "UNC13A" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'UNC13A' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **UNC13A** (gene ID: UNC13A, UniProt: Q9UPW8) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# UNC13A (Munc13-1; UniProt Q9UPW8, *Homo sapiens*): Functional Research Report

## Scope and sourcing

- **Identity check:** the symbol UNC13A matches "Protein unc-13 homolog A / Munc13-1", human, unc-13 family, with C1, C2 and MUN domains. No symbol ambiguity was found.
- **Species of evidence:** most mechanistic evidence comes from rat and mouse Munc13-1 and from *C. elegans* UNC-13. Human-specific evidence is mainly genetic (neurodevelopmental disease, ALS/FTD) plus a few cell studies.
- **Citations:** web searches in this session confirmed the items marked † in the source list. Other citations and all PMIDs except three (PMID:32643828, PMID:35197626, and PMID:41125872 from the local UniProt record) are from memory and should be checked against PubMed before reuse. Where I was unsure of a PMID I give author, journal and year only.

## 1. Summary

UNC13A is a large (about 1,700 residues) peripheral-membrane protein of the presynaptic active zone. It is not an enzyme or transporter. Its core function is to prime synaptic vesicles: it bridges the vesicle and the plasma membrane and catalyses the transition of syntaxin-1 from its closed, Munc18-1-bound state into the SNARE complex. This makes docked vesicles fusion-competent, creating the readily releasable pool (RRP). Its regulatory domains integrate diacylglycerol (DAG), Ca²⁺/phospholipid, Ca²⁺/calmodulin and RIM signals to tune release probability and short-term plasticity.

## 2. Domain architecture and molecular function

Residue numbers below refer to rat Munc13-1, the sequence used in most structural work.

| Domain | Activity | Key evidence |
|---|---|---|
| N-terminal C2A (does not bind Ca²⁺) | Forms an autoinhibitory homodimer; switches to a heterodimer with the RIM zinc finger, which activates priming and anchors Munc13-1 at the active zone | Betz 2001 (PMID:11343654); Lu 2006 (PMID:16732694); Deng 2011 (PMID:21262469); Camacho 2017 |
| Calmodulin-binding region | Ca²⁺/calmodulin binding speeds RRP refilling and shapes short-term plasticity | Junge 2004 (PMID:15315753); Lipstein 2013 |
| C1 | Binds DAG and phorbol esters; mediates phorbol-ester potentiation of release (H567K knock-in) | Betz 1998 (PMID:9697857); Rhee 2002 (PMID:11792326) |
| C2B | Binds Ca²⁺ and phosphoinositides (PIP/PIP₂); activity-dependent regulator of release | Shin 2010 (PMID:20154707); Lipstein 2021 |
| MUN (MHD1/2; related to CATCHR tethering factors) | Minimal priming module; opens syntaxin-1 and promotes ordered SNARE assembly | Basu 2005 (PMID:16228007); Ma 2011 (PMID:21499244); Yang 2015 (PMID:26030875) |
| C-terminal C2C (does not bind Ca²⁺) | Binds the vesicle membrane; needed for membrane bridging and priming | Liu 2016; Quade 2019 |

**Syntaxin opening.**
- The MUN domain accelerates the transition from the closed syntaxin-1/Munc18-1 complex to the SNARE complex (Ma 2011).
- Two conserved residues (N1128, F1131: the "NF pocket") are required; they engage R151/I155 in the syntaxin-1 linker (Yang 2015; Wang 2020, PMID:32643828).
- Linker opening extends Munc18-1 domain 3a, which then templates synaptobrevin-2 and syntaxin-1 (Wang 2020).
- In *C. elegans*, an open syntaxin mutant partly bypasses the need for UNC-13 (Richmond 2001).
- In reconstitution, Munc18-1 plus Munc13-1 make SNARE assembly resistant to NSF/α-SNAP disassembly and impose the correct parallel arrangement (Ma 2013, PMID:23258414; Lai 2017).

**Membrane bridging.**
- The C1-C2B-MUN crystal structure is a rod about 19.5 nm long (Xu 2017, PMID:28177287).
- The C1-C2B end binds the plasma membrane and C2C binds the vesicle. DAG and Ca²⁺ are proposed to change the rod's tilt, bringing the membranes closer (Xu 2017; Quade 2019; Michelassi 2017).
- Cryo-electron microscopy shows the C1-C2B-MUN-C2C fragment forming hexagonal assemblies between bilayers (Grushin 2022, PDB 7T7C; follow-up in Nat Commun 2025).

**Suggested GO framing.** Syntaxin-1 binding and SNARE-assembly chaperone/tethering activity, DAG binding, Ca²⁺-dependent phospholipid binding (C2B only) and calmodulin binding. Two UniProt statements deserve scrutiny:
- The DOMAIN note that the C2 domains "are not involved in calcium-dependent phospholipid binding" is outdated for C2B (Shin 2010), although it holds for C2A and C2C.
- "Interacts with the N-termini of STX1A/STX1B" comes from early binding studies. Later structural work places the functional contact at the syntaxin linker and SNARE motif.

## 3. Biological process

- **Synaptic vesicle priming.** Munc13-1 knockout mice die at birth. Their glutamatergic hippocampal neurons lose about 90% of the RRP and of evoked release, while synapse number and structure are normal (Augustin 1999, PMID:10440375).
- **Total dependence on Munc13s.** Munc13-1/2 double knockout abolishes both spontaneous and evoked release at glutamatergic and GABAergic synapses, with normal synapse formation (Varoqueaux 2002, PMID:12070347). GABAergic synapses use Munc13-1 and Munc13-2 redundantly, which is why UNC13A loss alone mainly affects excitatory synapses.
- **Docking.** With high-pressure freezing and electron tomography, Munc13-deficient synapses lack membrane-attached vesicles, so molecular priming and tight docking are the same step (Siksou 2009; Imig 2014).
- **Release-site identity.** Munc13-1 forms nanoclusters; their number equals the number of release sites, and they recruit syntaxin-1 (Sakamoto 2018, DOI 10.1038/s41593-017-0041-9). Munc13-1 content per site varies between synapses (Karlócai 2021, eLife).
- **Short-term plasticity and RRP refilling.** DAG/C1, Ca²⁺-calmodulin and Ca²⁺-phospholipid/C2B signalling accelerate replenishment and lower the fusion energy barrier (Rhee 2002; Junge 2004; Lipstein 2013, 2021; Rosenmund 2002). DAG and phorbol-ester potentiation of release acts through Munc13, not protein kinase C (Rhee 2002).
- **Dense-core vesicles.** Munc13-1/2 facilitate neuronal dense-core vesicle fusion and set where release occurs, but are not strictly required (van de Bospoort 2012, J Cell Biol).
- **Insulin secretion.** Munc13-1 is expressed in human and rodent islets and primes insulin granules (Sheu 2003, PMID:12871971; Kwan 2006; Kang 2006). This is a genuine secondary role.
- **Melanocyte dendrite extension** (PMID:23999003). This is a single knockdown study, peripheral to the core function.

## 4. Localization

- Munc13-1 is concentrated at the presynaptic active zone: on the cytoplasmic face of the presynaptic plasma membrane, at the interface with docked vesicles. It is found at most central synapses and at neuromuscular junctions (Betz 1998; Kalla 2006, EYFP knock-in mice).
- Recruitment depends on RIM (C2A–zinc finger), and Munc13-1 belongs to the RIM/ELKS/Bassoon scaffold.
- It is a soluble or peripheral protein that translocates to the plasma membrane on DAG or phorbol-ester binding.
- The existing "synaptic vesicle membrane" annotation reflects transient C2C contact with the vesicle, not residence on it.
- Protein level is controlled by FBXO45-mediated ubiquitination (Tada 2010).

## 5. Human disease evidence

- **Recessive loss of function.** A homozygous truncating variant caused microcephaly, cortical hyperexcitability and fatal myasthenia with impaired neuromuscular release (Engel 2016, PMID:27648472).
- **Dominant gain of function.** De novo P814L increased release probability and caused a dyskinetic movement disorder with developmental delay (Lipstein 2017, PMID:28192369).
- **Neurodevelopmental syndrome.** A 48-patient cohort defined three subtypes: reduced protein and synaptic strength, gain of function, and impaired second-messenger regulation. Variants were tested in mouse neurons and *C. elegans* (Asadollahi 2025, Nat Genet 57:2691–2704, PMID:41125872). The UniProt record lists the corresponding disorders as NEDHES, NEDSMS and IDDSF.
- **ALS/FTD risk.** Intronic variants are risk and survival modifiers (van Es 2009, PMID:19734901). When nuclear TDP-43 is lost, a cryptic exon is included in UNC13A mRNA, causing nonsense-mediated decay and protein loss. Risk alleles rs12973192 and rs12608932 weaken TDP-43 binding and increase inclusion (Ma 2022, PMID:35197626; Brown 2022, Nature 603:131–137). hnRNP L, A1 and A2B1 also repress the exon (PLOS Biol 2023).
- **Therapy.** An antisense oligonucleotide that skips the cryptic exon (TRCN-1023, Trace Neuroscience) was reported in July 2026 as authorised for a Phase 1/2 trial (FUNCTION ALS). Sources differ on start dates, so check current status.

## 6. Evolution

The unc-13 family is conserved across animals (*C. elegans* unc-13, *Drosophila* Unc13A/B; Brose 1995, PMID:7559667). The MUN domain is shared with CAPS and BAIAP3 and is structurally related to exocyst-type tethering factors. This supports the view that Munc13 is an ancient tether and SNARE-assembly chaperone specialised for regulated exocytosis.

## 7. Open questions

- The exact number and arrangement of Munc13-1 molecules at each release site in vivo.
- How regulatory signals couple structurally to MUN activity.
- Whether Munc13-1 functions autonomously after assembly, together with synaptotagmin and complexin.
- The synaptic consequences of partial UNC13A loss in human motor neurons.

## Sources

Verified by web search in this session (†):
- † [Wang et al. 2020, EMBO J: Munc13 activates the Munc18-1/syntaxin-1 complex (PMID:32643828)](https://pubmed.ncbi.nlm.nih.gov/32643828/)
- † [Xu et al. 2017, eLife: Munc13-1 C1C2BMUN structure](https://elifesciences.org/articles/24278.pdf)
- † [Frontiers Mol Neurosci 2021: syntaxin-1 linker and MUN NF pocket](https://www.frontiersin.org/articles/10.3389/fnmol.2021.785696/full)
- † [Ma et al. 2022, Nature: TDP-43 represses cryptic exon inclusion in UNC13A (PMID:35197626)](https://pubmed.ncbi.nlm.nih.gov/35197626/)
- † [Brown et al. 2022, Nature: TDP-43 loss and ALS-risk SNPs drive mis-splicing of UNC13A](https://link.springer.com/article/10.1038/s41586-022-04436-3)
- † [Alzforum summary of the 2022 cryptic exon papers](https://alzforum.org/node/1635881)
- † [PLOS Biol 2023: hnRNP repression of the UNC13A cryptic exon (PMC10057836)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10057836)
- † [Asadollahi et al. 2025, Nat Genet: open-access copy at UCL Discovery](https://discovery.ucl.ac.uk/id/eprint/10216199/)
- † [Grushin et al. 2022: PDB 7T7C, hexagonal Munc13-1 assembly](https://rcsb.org/structure/7T7C)
- † [Karlócai et al. 2021, eLife: variability in Munc13-1 content of release sites](https://elifesciences.org/articles/67468/peer-reviews)
- † [Lu et al. 2006, PLoS Biol: Munc13-1 homodimer to Munc13-1/RIM heterodimer switch](https://dx.doi.org/10.1371/journal.pbio.0040192)
- † [Deng et al. 2011, Neuron: RIM activates priming by reversing Munc13 homodimerization (PMC3063404)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3063404)
- † [Camacho et al. 2017, Nat Commun: Munc13 C2A–RIM heterodimerization (PMC5436228)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5436228)
- † [UCL News, July 2026: UNC13A antisense trial announcement](https://www.ucl.ac.uk/news/2026/jul/novel-treatment-motor-neurone-disease-be-trialled-humans)

From the local UniProt record (`genes/human/UNC13A/UNC13A-uniprot.txt`, Q9UPW8): function, subunit, location and disease comments, and PMIDs 12871971, 23999003, 27648472, 28192369, 41125872.

Cited from memory, not checked in this session: Brose 1995; Betz 1998, 2001; Augustin 1999; Richmond 2001; Rhee 2002; Rosenmund 2002; Varoqueaux 2002; Junge 2004; Basu 2005; Kalla 2006; Kwan 2006; Kang 2006; Siksou 2009; van Es 2009; Shin 2010; Tada 2010; Ma 2011, 2013; van de Bospoort 2012; Lipstein 2013, 2021; Imig 2014; Yang 2015; Liu 2016; Lai 2017; Michelassi 2017; Quade 2019. Sakamoto 2018 was only partly confirmed (DOI and thesis record).

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/32643828/
2. https://elifesciences.org/articles/24278.pdf
3. https://www.frontiersin.org/articles/10.3389/fnmol.2021.785696/full
4. https://pubmed.ncbi.nlm.nih.gov/35197626/
5. https://link.springer.com/article/10.1038/s41586-022-04436-3
6. https://alzforum.org/node/1635881
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC10057836
8. https://discovery.ucl.ac.uk/id/eprint/10216199/
9. https://rcsb.org/structure/7T7C
10. https://elifesciences.org/articles/67468/peer-reviews
11. https://dx.doi.org/10.1371/journal.pbio.0040192
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC3063404
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC5436228
14. https://www.ucl.ac.uk/news/2026/jul/novel-treatment-motor-neurone-disease-be-trialled-humans