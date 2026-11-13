---
provider: claude_code
cached: false
start_time: '2026-11-13T00:08:45.682662'
end_time: '2026-11-13T00:10:23.585776'
duration_seconds: 97.9
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: STXBP1
  gene_symbol: STXBP1
  uniprot_accession: P61764
  protein_description: 'RecName: Full=Syntaxin-binding protein 1; AltName: Full=MUNC18-1;
    AltName: Full=N-Sec1; AltName: Full=Protein unc-18 homolog 1; Short=Unc18-1; AltName:
    Full=Protein unc-18 homolog A; Short=Unc-18A; AltName: Full=p67;'
  gene_info: Name=STXBP1; Synonyms=UNC18A;
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the STXBP/unc-18/SEC1 family. .
  protein_domains: Sec-1-like_dom1. (IPR043154); Sec-1-like_dom3a. (IPR043127); Sec1-like.
    (IPR001619); Sec1-like_dom2. (IPR027482); Sec1-like_sf. (IPR036045)
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
  web_search_requests: 14
  num_turns: 15
  total_cost_usd: 1.5834131
  session_id: 1c0ed628-9fde-4c31-bcf5-5045d5867565
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 28
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P61764
- **Protein Description:** RecName: Full=Syntaxin-binding protein 1; AltName: Full=MUNC18-1; AltName: Full=N-Sec1; AltName: Full=Protein unc-18 homolog 1; Short=Unc18-1; AltName: Full=Protein unc-18 homolog A; Short=Unc-18A; AltName: Full=p67;
- **Gene Information:** Name=STXBP1; Synonyms=UNC18A;
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the STXBP/unc-18/SEC1 family. .
- **Key Domains:** Sec-1-like_dom1. (IPR043154); Sec-1-like_dom3a. (IPR043127); Sec1-like. (IPR001619); Sec1-like_dom2. (IPR027482); Sec1-like_sf. (IPR036045)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "STXBP1" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'STXBP1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **STXBP1** (gene ID: STXBP1, UniProt: P61764) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# STXBP1 (Munc18-1; UniProt P61764), human: function, localization and pathways

## Identity check

The symbol STXBP1 matches the UniProt record: syntaxin-binding protein 1 (Munc18-1, N-Sec1, Unc-18A, p67), *Homo sapiens*, STXBP/unc-18/SEC1 family. The literature found is for this protein and its near-identical rodent orthologs, and no symbol ambiguity was encountered.

**Provenance.** Claims with a link were confirmed in this session's web searches, at abstract or summary level only (full texts were not read). Claims marked *(from memory)* are standard literature I did not re-verify here; confirm their PMIDs before use in curation.

## 1. Summary

STXBP1 encodes Munc18-1, the neuronal Sec1/Munc18 (SM) protein. It is not an enzyme or transporter. It is a soluble, peripheral-membrane SNARE chaperone and assembly template with three separable roles:

- It binds and stabilizes syntaxin-1 in a closed conformation.
- With Munc13, it templates assembly of the syntaxin-1/SNAP-25/VAMP2 SNARE complex.
- It thereby drives docking, priming and fusion of synaptic vesicles and dense-core vesicles at the presynaptic plasma membrane.

It is essential for all neurotransmitter release. Heterozygous loss of function causes developmental and epileptic encephalopathy 4 (DEE4).

## 2. Molecular function

**Closed syntaxin-1 binding.** The Munc18-1–syntaxin-1 crystal structure (Misura et al., 2000) was the first SM–SNARE structure. It showed Munc18-1 holding syntaxin-1 in an autoinhibited closed conformation, which suggested a clamp ([eLife review](https://elifesciences.org/articles/60724.pdf)). A second binding mode uses the syntaxin N-peptide and an extended domain 3a conformation compatible with open syntaxin and SNARE complexes ([Hu et al., PNAS 2011; PDB 3PUJ](https://www.rcsb.org/structure/3puj)). In vitro, Munc18-1 can inhibit or stimulate fusion depending on the assay ([PMC3382502](https://pmc.ncbi.nlm.nih.gov/articles/PMC3382502)).

**Syntaxin-1 chaperone.** Syntaxin-1 levels fall about 70% in Munc18-1 knockout mice, yet the residual syntaxin-1 is still targeted to synapses. This supports a stabilizing role and argues against Munc18-1 being a strict targeting factor ([Toonen et al., 2005](https://pubmed.ncbi.nlm.nih.gov/15935055/)).

**SNARE assembly template (the core activity).**
- Optical-tweezers experiments showed Munc18-1 catalyzes stepwise SNARE zippering through a "template complex". In it, Munc18-1 holds the N-terminal SNARE-motif regions of syntaxin and VAMP2 together and keeps the C-terminal regions apart. Mutant effects on template stability tracked effects on fusion ([Jiao et al., eLife 2018](https://elifesciences.org/articles/41771)).
- Cryo-EM structures of a synaptobrevin–Munc18-1–syntaxin-1 complex at 3.5 and 3.7 Å (PDB 7UDB, 7UDC) showed how syntaxin-1 opens and how SNARE assembly is nucleated ([Stepien et al., Sci Adv 2022](https://pubmed.ncbi.nlm.nih.gov/35731863/)).
- Munc13 opens syntaxin-1 through its MUN domain, enabling Munc18-1 domain 3a to prime assembly ([Wang et al., 2020](https://pubmed.ncbi.nlm.nih.gov/32643828/)). Mutating hinge-loop residues T323/M324/R325 disrupted Munc13-1-mediated assembly and fusion in vitro ([BMC Biology 2023](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01655-6)).
- The same templating logic was shown for the SM protein Vps33 (Baker et al., Science 2015), supporting a conserved SM mechanism *(from memory)*.
- Munc18-1 and Munc13 also route assembly through an NSF/α-SNAP-resistant pathway (Ma et al., Science 2013) *(from memory)*.

**Specificity.** UniProt records binding to syntaxins 1, 2 and 3 but not syntaxin 4, plus STX1A binding by experiment (PMID:12730201).

## 3. Biological process

**Neurotransmitter release.** Deleting Munc18-1 in mice eliminated secretion from synaptic vesicles. The brain still assembled, so synapse formation does not require secretion, although maintenance does ([Verhage et al., Science 2000](https://pure.amsterdamumc.nl/en/publications/synaptic-assembly-of-the-brain-in-the-absence-of-neurotransmitter-2/)).

**Dense-core vesicle docking.** In Munc18-1-null chromaffin cells, calcium-dependent exocytosis and morphologically docked vesicles were each reduced about 10-fold, with normal kinetics of the remaining release. This places Munc18-1 upstream of SNARE complex formation ([Voets et al., Neuron 2001](https://pubmed.ncbi.nlm.nih.gov/11545717/)).

**Priming.** Disrupting Munc18-1 binding to the SNARE complex selectively impaired synaptic vesicle priming and left Ca2+-triggered fusion of primed vesicles intact ([Deák et al., JCB 2009](https://rupress.org/jcb/article-split/184/5/751/35286/Munc18-1-binding-to-the-neuronal-SNARE-complex)).

**Regulation by phosphorylation.**
- Conventional PKC phosphorylates Ser306 and Ser313, which inhibits syntaxin binding. Ser313 phosphorylation rises with synaptic activity at the neuromuscular junction ([Frontiers Mol Neurosci 2018](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2018.00207/full)).
- Src-family kinases phosphorylate Tyr473. The phosphomimetic Y473D blocks VAMP2 binding and SNARE-assembly stimulation, and abolishes priming but not docking ([Meijer et al., EMBO J 2018](https://link.springer.com/10.15252/embj.201796484)).

**Other reported roles.**
- Munc18-1 was proposed as a chaperone for α-synuclein, limiting its aggregation ([Chai et al., JCB 2016](https://rupress.org/jcb/article/214/6/705/38709/Munc18-1-is-a-molecular-chaperone-for-synuclein)). This is a secondary activity.
- Null neurons degenerate cell-autonomously even with trophic support ([Heeroma et al., 2004](https://repub.eur.nl/pub/73202/Heeroma_et_al-2004-European_Journal_of_Neuroscience.pdf)).
- GOA carries platelet, acrosome and mast-cell terms; I did not examine their supporting papers. In platelets and most non-neuronal secretory cells the dominant SM paralogs are Munc18-2 (STXBP2) and Munc18-3 (STXBP3) *(from memory)*, so these are best treated as peripheral.

## 4. Localization

- UniProt lists cytosol (PMID:20887364) and peripheral membrane, with expression in brain and spinal cord, highly enriched in axons.
- The functional site is the cytoplasmic face of the presynaptic plasma membrane at the active zone, where Munc18-1 is recruited through syntaxin-1, and docking sites for dense-core vesicles in neuroendocrine cells.
- Two splice isoforms exist (P61764-1 and P61764-2), differing at the C-terminus.
- Mitochondrion, extracellular exosome and RNA-binding annotations come from sequence similarity or high-throughput evidence and lack mechanistic support in the literature found here.

## 5. Pathway context

Munc18-1 acts in the regulated exocytosis pathway in this order:

1. Munc18-1 binds closed syntaxin-1 and stabilizes it.
2. Munc13 opens syntaxin-1.
3. Munc18-1 templates syntaxin-1 and VAMP2, and SNAP-25 joins.
4. The partially zippered complex is clamped (synaptotagmin and complexin) until Ca2+ triggers fusion.
5. NSF and α-SNAP disassemble the complex for reuse.

## 6. Disease and recent developments

**Epidemiology and phenotype.** A study harmonizing 534 individuals estimated a frequency of at least 1:30,000. Neurodevelopmental abnormalities occurred in 95% and seizures in 89%. No clear genotype–phenotype correlation emerged, and haploinsufficiency was the main mechanism ([Xian et al., Brain 2022](https://pmc.ncbi.nlm.nih.gov/articles/pmid/35190816)). A separate paper cites up to 1:26,000 ([Balagura et al., 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9166568)).

**Mechanism.**
- Reviews agree on haploinsufficiency, with dominant-negative effects proposed for some variants ([Abramov et al., J Neurochem 2020](https://vivo.weill.cornell.edu/display/pubid32643187); [BioTech 2025](https://mdpi.com/2673-6284/14/1/11)).
- At least five missense variants destabilize the protein and pull wild-type Munc18-1 into aggregates. The chemical chaperones 4-phenylbutyrate, sorbitol and trehalose reversed this in yeast, worm and mouse-neuron models ([Guiberson et al., Nat Commun 2018](https://www.nature.com/articles/s41467-018-06507-4)).
- In mice, haploinsufficiency reduced cortical inhibition from parvalbumin and somatostatin interneurons by different mechanisms (synaptic strength versus connectivity) ([Chen et al., eLife 2020](https://pubmed.ncbi.nlm.nih.gov/32073399/)).
- Patient iPSC-derived GABAergic neurons showed about 20% protein reduction despite 50% mRNA reduction, with reduced spiking ([2021 study](https://pure.fujita-hu.ac.jp/en/publications/impaired-neuronal-activity-and-differential-gene-expression-in-st/)).
- A 2024 engineered human-neuron study reported gain-of-function-like release changes ([PMID 38484778](https://www.pubmed.gov/38484778/)); I could not confirm the variant details.

**Therapeutics.**
- **Gene therapy.** The FDA cleared the IND for CAP-002, an intravenous engineered AAV gene therapy, in May 2025 ([Capsida release](https://www.businesswire.com/news/home/20250512366164/en)). Its Phase 1/2a trial is NCT06983158. Registry aggregators list the trial as suspended after the death of the first dosed patient in September 2025 ([registry record](https://scge.mcw.edu/platform/data/report/clinicalTrials/NCT06983158)). I found no company statement or publication, so treat this as unconfirmed.
- **4-phenylbutyrate.** A glycerol phenylbutyrate trial covering STXBP1 and SLC6A1 is registered as NCT04937062 ([Weill Cornell summary](https://teach.weill.cornell.edu/node/438)); I found no published results. A zebrafish study dated 2026 reported that 4-PBA and analogs failed to rescue the *stxbp1a* mutant locomotion deficit and urged caution ([ZFIN record](https://crick.zfin.org/ZDB-PUB-260611-1)).

## 7. Implications for annotation

- **Core molecular function:** syntaxin-1 binding and SNARE binding, expressed mechanistically as SNARE-complex assembly chaperone/template activity. The record's "vesicle docking activity" term is by sequence similarity.
- **Core processes:** SNARE complex assembly and its regulation, synaptic vesicle priming, vesicle docking, and synaptic vesicle fusion to the presynaptic active zone membrane.
- **Core locations:** presynapse and active zone, cytosol, cytoplasmic side of the plasma membrane.
- **Peripheral or doubtful:** platelet, acrosome and mast-cell terms; mitochondrion; exosome; RNA binding; response to estradiol.
- **Evidence caveat:** most mechanistic evidence comes from rat and mouse Munc18-1, which the mature human protein matches almost exactly *(from memory)*. Human-specific evidence is mainly genetic and iPSC-based.

## Open questions

- How far aggregation-driven dominant-negative effects, as opposed to simple haploinsufficiency, contribute across missense variants.
- Whether Munc18-1 stays bound to the SNARE complex through fusion. eLife reviewers called the evidence for its release on full zippering indirect ([peer review](https://elifesciences.org/articles/41771/peer-reviews)).
- How relevant the α-synuclein chaperone activity is in vivo.

## Sources

- [Stepien et al. 2022, Sci Adv (PubMed)](https://pubmed.ncbi.nlm.nih.gov/35731863/)
- [BMC Biology 2023, domain 3a hinge loop](https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01655-6)
- [Jiao et al. 2018, eLife](https://elifesciences.org/articles/41771) and [peer reviews](https://elifesciences.org/articles/41771/peer-reviews)
- [Wang et al. 2020, Munc13 activates Munc18-1/syntaxin-1](https://pubmed.ncbi.nlm.nih.gov/32643828/)
- [Hu et al. 2011, PDB 3PUJ](https://www.rcsb.org/structure/3puj)
- [eLife SM protein review](https://elifesciences.org/articles/60724.pdf)
- [PMC3382502, N-peptide and fusion](https://pmc.ncbi.nlm.nih.gov/articles/PMC3382502)
- [Verhage et al. 2000, Science](https://pure.amsterdamumc.nl/en/publications/synaptic-assembly-of-the-brain-in-the-absence-of-neurotransmitter-2/)
- [Voets et al. 2001, Neuron](https://pubmed.ncbi.nlm.nih.gov/11545717/)
- [Toonen et al. 2005](https://pubmed.ncbi.nlm.nih.gov/15935055/)
- [Heeroma et al. 2004](https://repub.eur.nl/pub/73202/Heeroma_et_al-2004-European_Journal_of_Neuroscience.pdf)
- [Deák et al. 2009, JCB](https://rupress.org/jcb/article-split/184/5/751/35286/Munc18-1-binding-to-the-neuronal-SNARE-complex)
- [Meijer et al. 2018, EMBO J](https://link.springer.com/10.15252/embj.201796484)
- [Frontiers Mol Neurosci 2018, PKC and Ser313](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2018.00207/full)
- [Chai et al. 2016, JCB](https://rupress.org/jcb/article/214/6/705/38709/Munc18-1-is-a-molecular-chaperone-for-synuclein)
- [Xian et al. 2022, Brain](https://pmc.ncbi.nlm.nih.gov/articles/pmid/35190816)
- [Balagura et al. 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9166568)
- [Abramov et al. 2020, J Neurochem](https://vivo.weill.cornell.edu/display/pubid32643187)
- [BioTech 2025 review](https://mdpi.com/2673-6284/14/1/11)
- [Guiberson et al. 2018, Nat Commun](https://www.nature.com/articles/s41467-018-06507-4)
- [Chen et al. 2020, eLife](https://pubmed.ncbi.nlm.nih.gov/32073399/)
- [iPSC GABAergic neuron study, 2021](https://pure.fujita-hu.ac.jp/en/publications/impaired-neuronal-activity-and-differential-gene-expression-in-st/)
- [PMID 38484778](https://www.pubmed.gov/38484778/)
- [Capsida CAP-002 IND release](https://www.businesswire.com/news/home/20250512366164/en)
- [NCT06983158 registry record](https://scge.mcw.edu/platform/data/report/clinicalTrials/NCT06983158)
- [Weill Cornell chemical chaperone summary](https://teach.weill.cornell.edu/node/438)
- [ZFIN record, 4-PBA zebrafish study](https://crick.zfin.org/ZDB-PUB-260611-1)
- UniProt P61764 flat file (local copy, `genes/human/STXBP1/STXBP1-uniprot.txt`)

## Citations

1. https://elifesciences.org/articles/60724.pdf
2. https://www.rcsb.org/structure/3puj
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC3382502
4. https://pubmed.ncbi.nlm.nih.gov/15935055/
5. https://elifesciences.org/articles/41771
6. https://pubmed.ncbi.nlm.nih.gov/35731863/
7. https://pubmed.ncbi.nlm.nih.gov/32643828/
8. https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-023-01655-6
9. https://pure.amsterdamumc.nl/en/publications/synaptic-assembly-of-the-brain-in-the-absence-of-neurotransmitter-2/
10. https://pubmed.ncbi.nlm.nih.gov/11545717/
11. https://rupress.org/jcb/article-split/184/5/751/35286/Munc18-1-binding-to-the-neuronal-SNARE-complex
12. https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2018.00207/full
13. https://link.springer.com/10.15252/embj.201796484
14. https://rupress.org/jcb/article/214/6/705/38709/Munc18-1-is-a-molecular-chaperone-for-synuclein
15. https://repub.eur.nl/pub/73202/Heeroma_et_al-2004-European_Journal_of_Neuroscience.pdf
16. https://pmc.ncbi.nlm.nih.gov/articles/pmid/35190816
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC9166568
18. https://vivo.weill.cornell.edu/display/pubid32643187
19. https://mdpi.com/2673-6284/14/1/11
20. https://www.nature.com/articles/s41467-018-06507-4
21. https://pubmed.ncbi.nlm.nih.gov/32073399/
22. https://pure.fujita-hu.ac.jp/en/publications/impaired-neuronal-activity-and-differential-gene-expression-in-st/
23. https://www.pubmed.gov/38484778/
24. https://www.businesswire.com/news/home/20250512366164/en
25. https://scge.mcw.edu/platform/data/report/clinicalTrials/NCT06983158
26. https://teach.weill.cornell.edu/node/438
27. https://crick.zfin.org/ZDB-PUB-260611-1
28. https://elifesciences.org/articles/41771/peer-reviews