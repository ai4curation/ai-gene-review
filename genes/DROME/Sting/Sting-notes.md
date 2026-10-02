# Drosophila melanogaster Sting (dSTING, CG1667, FBgn0033453; UniProt A0A0B4LFY9) — curation notes

## Provenance
Automated deep research (`just deep-research DROME Sting --provider perplexity`) failed in this
environment (`agentapi not found in PATH`, no provider configured), so no `-deep-research-<provider>.md`
file was generated. These notes are compiled manually from the cached publications in `publications/`
and the UniProt record. All assertions carry inline PMID provenance with verbatim supporting text.

## Summary of gene function
dSTING is the single Drosophila ortholog of the STING family (STING_LBD + STING_TM domains;
IPR029158). It is a multi-pass endoplasmic reticulum membrane protein (343 aa) that functions as an
innate-immune signaling adapter. Unlike vertebrate STING, the fly (and insects generally) have **no
type I interferon system and no TBK1->IRF3->IFN axis**; dSTING instead signals to the NF-kappaB
transcription factor **Relish** through the IMD pathway (via the kinase dIKKbeta), driving
antimicrobial peptide (AMP) and antiviral gene expression.

### Ligand recognition (molecular function)
- Binds bacterial **cyclic di-GMP** (c-di-GMP): [PMID:29924997 "DmSTING retains its ability to bind cyclic di-GMP, leading to the induction of innate immune response genes."]
- Binds the virus-induced CDNs **3'2'-cGAMP** (strongly preferred) and **2'3'-cGAMP**, produced by the cGAS-like receptors cGLR1/cGLR2 in response to (ds)RNA virus: [PMID:34261127 "We show that RNA recognition activates Drosophila cGLR1 to synthesize the novel product cG[3'-5']pA[2'-5']p (3'2'-cGAMP)."] and [PMID:34261128 "We show that cGLR1 and cGLR2 activate Sting- and NF-κB-dependent antiviral immunity in response to infection with RNA or DNA viruses."]
- A crystal structure of dSTING bound to 3'2'-cGAMP explains isomer selectivity: [PMID:34261127 "A crystal structure of Drosophila stimulator of interferon genes (dSTING) in complex with 3'2'-cGAMP explains selective isomer recognition"]
- Also responds to the virus-induced CDN **2'3'-c-di-GMP**, a more potent dSTING agonist than cGAMP: [PMID:37659413 "This CDN was a more potent STING agonist than cGAMP in D. melanogaster"]

### Antibacterial function
- Activates AMP production and defense against *Listeria monocytogenes* via Relish/IMD: [PMID:29924997 "Following infection with\nListeria monocytogenes, dmSTING activates an innate immune response via\nactivation of the NF-κB transcription factor Relish, part of the immune\ndeficiency (IMD) pathway."] and [PMID:29924997 "epistasis analysis in flies indicated that dmSTING functioned predominantly through the IMD pathway and Relish to achieve antimicrobial peptide induction."]
- Protects against the Gram-negative bacterium *Coxiella burnetii* by limiting reactive oxygen species: [PMID:38363133 "Sting-null flies exhibit higher mortality and reduced induction of antimicrobial\npeptides following C. burnetii infection compared to control flies."]

### Antiviral function (NF-kappaB / Relish, interferon-independent)
- Controls picorna-like viruses downstream of the cGLR sensors, acting upstream of dIKKbeta to induce the antiviral factor Nazo: [PMID:30119996 "We showed that dSTING participated in the control of\ninfection by picorna-like viruses, acting upstream of dIKKβ to regulate\nexpression of Nazo, an antiviral factor."]
- 2'3'-cGAMP triggers a Relish (NF-kB)-dependent, interferon-independent antiviral program: [PMID:33262294 "Our results reveal that dSTING\nregulates an NF-κB-dependent antiviral program that predates the emergence of\ninterferons in vertebrates."]
- Orally acquired bacterial CDNs drive dSTING/dTBK1-dependent, NF-kB-dependent antiviral immunity in gut enterocytes: [PMID:34965418 "we find CDN protection is dSTING- and\ndTBK1-dependent, leading to NF-kB-dependent gene expression."]
- A cryptic RHIM (cRHIM) motif drives dSTING oligomerization and antiviral signaling and its interaction with IMD: [PMID:38969190 "insect STING employed a homotypic\nmotif to form intermolecular interactions that are essential for its antiviral\nsignaling."]

### Autophagy (interferon-independent, context-specific)
- In the adult brain, Zika-virus-induced NF-kB signaling induces dSTING, which restricts infection by inducing autophagy: [PMID:29934091 "dSTING protects against ZIKV by\ninducing autophagy in the brain."]

### Localization
- Endoplasmic reticulum membrane, multi-pass membrane protein: [PMID:30119996 "FUNCTION, SUBCELLULAR LOCATION"] (UniProt SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane {ECO:0000269|PubMed:30119996}").

## Curation implications
- The IEA `GO:0032481 positive regulation of type I interferon production` (InterPro2GO from IPR029158)
  is taxonomically inappropriate for Drosophila, which has no type I interferons. dSTING signals to
  NF-kB/Relish, not IFN. This is a demonstrably wrong electronic mapping and is removed.
- Autophagy / autophagosome / reticulophagy terms reflect the ancestral STING autophagy function
  (mammalian Q86WV6) transferred by IBA; the fly has a real but context-specific (Zika brain) autophagy
  role — retained as non-core where they are inherited/component terms.
- Core functions are cyclic-dinucleotide binding (c-di-GMP, 3'2'-cGAMP, 2'3'-cGAMP) driving the
  cGAS/STING signaling pathway to NF-kB (Relish), producing antibacterial and antiviral innate immune
  responses, at the ER membrane.
