---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-18T15:24:33.710326'
end_time: '2026-11-18T15:25:56.791400'
duration_seconds: 83.08
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: TAF14
  gene_symbol: TAF14
  uniprot_accession: P35189
  protein_description: 'RecName: Full=Transcription initiation factor TFIID subunit
    14; AltName: Full=Actin non-complementing mutant 1; AltName: Full=Chromosome stability
    protein 10; AltName: Full=SWI/SNF chromatin-remodeling complex subunit TAF14;
    AltName: Full=SWI/SNF complex 29 kDa subunit; AltName: Full=SWI/SNF complex subunit
    TAF14; AltName: Full=TBP-associated factor 14; AltName: Full=TBP-associated factor
    30 kDa; AltName: Full=Transcription factor G 30 kDa subunit; AltName: Full=Transcription
    initiation factor TFIIF 30 kDa subunit;'
  gene_info: Name=TAF14; Synonyms=ANC1, CST10, SWP29, TAF30, TFG3; OrderedLocusNames=YPL129W;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the TAF14 family. .
  protein_domains: NET_dom. (IPR027353); Sas5/TAF14. (IPR016665); YEAST_sf. (IPR038704);
    YEATS. (IPR005033); YEATS_dom. (IPR055129)
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
  - claude-fable-5-2
  - claude-haiku-5-5
  web_search_requests: 6
  num_turns: 9
  total_cost_usd: 1.2354094
  session_id: 47795542-32fa-48c8-b2c1-2b82ca8b4d4b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 15
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P35189
- **Protein Description:** RecName: Full=Transcription initiation factor TFIID subunit 14; AltName: Full=Actin non-complementing mutant 1; AltName: Full=Chromosome stability protein 10; AltName: Full=SWI/SNF chromatin-remodeling complex subunit TAF14; AltName: Full=SWI/SNF complex 29 kDa subunit; AltName: Full=SWI/SNF complex subunit TAF14; AltName: Full=TBP-associated factor 14; AltName: Full=TBP-associated factor 30 kDa; AltName: Full=Transcription factor G 30 kDa subunit; AltName: Full=Transcription initiation factor TFIIF 30 kDa subunit;
- **Gene Information:** Name=TAF14; Synonyms=ANC1, CST10, SWP29, TAF30, TFG3; OrderedLocusNames=YPL129W;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the TAF14 family. .
- **Key Domains:** NET_dom. (IPR027353); Sas5/TAF14. (IPR016665); YEAST_sf. (IPR038704); YEATS. (IPR005033); YEATS_dom. (IPR055129)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TAF14" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TAF14' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TAF14** (gene ID: TAF14, UniProt: P35189) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TAF14 (YPL129W; UniProt P35189) in *Saccharomyces cerevisiae*: research report

**Identity check.** The symbol TAF14 (synonyms ANC1, TFG3, TAF30, SWP29, CST10) matches UniProt P35189, a 244-residue nuclear YEATS-domain protein of budding yeast. The literature found is for this protein and agrees with the family and domain assignments (YEATS; NET/ET domain; Sas5/TAF14 family).

**Provenance.** Claims are drawn from the local UniProt record, six web searches (read as abstracts and snippets, not full text), and my recall of the older literature. Items resting on recall alone are marked "(from memory)" and should be checked before use in an annotation.

## 1. Summary

Taf14 is not an enzyme, transporter or sequence-specific DNA-binding factor. It is a small, non-catalytic chromatin reader and scaffold shared by at least six nuclear transcription and chromatin complexes: TFIID, TFIIF, SWI/SNF, RSC, INO80 and NuA3. It has two functional modules:

- **N-terminal YEATS domain:** binds histone H3 acylated on Lys9 (H3K9ac, H3K9cr), preferring crotonyl-lysine.
- **C-terminal ET (extra-terminal) domain:** docks onto a short motif present in a catalytic or core subunit of each host complex. This domain carries most of the biological function.

It acts in the nucleus, on chromatin. UniProt notes it is the only non-essential TAF.

## 2. Molecular function

### 2.1 Acyl-lysine reader (YEATS domain)

- The YEATS domain binds H3K9ac, and this association was linked to gene transcription and the DNA damage response (Shanle et al. 2015, *Genes Dev*, PMID:26341557).
- It binds H3K9cr more tightly than H3K9ac, making Taf14 a crotonyl-lysine reader (Andrews et al. 2016, *Nat Chem Biol*, PMID:27089029).
- Crotonyl-lysine is held by a non-canonical π-π-π stacking mechanism; the isolated YEATS domain does not bind DNA (Klein et al. 2018, *Nat Commun*, PMID:30385749).
- In the yeast metabolic cycle, H3K9 crotonylation peaks as H3K9 acetylation falls and energy becomes limiting. Mutating the Taf14 YEATS domain de-represses the periodically expressed fatty-acid β-oxidation genes, so reader function here is repressive (Gowans et al. 2019, *Mol Cell*, [PMC6931132](https://pmc.ncbi.nlm.nih.gov/articles/PMC6931132)).

### 2.2 Complex-docking adaptor (ET domain)

- The ET domain recognises a common motif in subunits of RSC, SWI/SNF, INO80, NuA3, TFIID and TFIIF. The ET-binding motif (hxhKh-type) occurs in Sth1, Taf2, Tfg1, Ino80 and Snf5 (Chen et al. 2020, *Nat Commun*, [PMID:32826896](https://pubmed.ncbi.nlm.nih.gov/32826896/), [PMC7442819](https://pmc.ncbi.nlm.nih.gov/articles/PMC7442819); Nguyen et al., [PMC11539623](https://pmc.ncbi.nlm.nih.gov/articles/PMC11539623)).
- The ET domain undergoes liquid–liquid phase separation in vitro, enhanced by partner binding. The authors propose that Taf14 clusters transcription machinery; this is an in vitro observation and a proposal, not a demonstrated in vivo role.
- The ET domain alone rescues the taf14Δ growth defect (Chen et al. 2020). An earlier study found the YEATS domain dispensable for complex association, which depends on the C-terminal domain, and reported that the YEATS domain has a negative effect on growth (Schulze et al. 2010, *Mol Genet Genomics*, [doi:10.1007/s00438-010-0523-x](https://link.springer.com/doi/10.1007/s00438-010-0523-x)).
- A crystal structure shows the ET domain bound to a Sth1 peptide ([PDB 6LQZ](https://proteopedia.org/w/6lqz)).

### 2.3 Regulated DNA and nucleosome binding (linker)

The linker between the two domains binds DNA, but in free Taf14 it is occluded by the flanking domains (autoinhibition). Binding of the Taf2 C-terminal tail to both domains releases the linker so it can engage DNA and the nucleosome (Klein et al. 2022, *Nat Commun*, [PMC9177701](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9177701/); [PDB 7UHE](https://www.rcsb.org/structure/7UHE)).

## 3. Host complexes

| Complex | Tether | Evidence |
|---|---|---|
| TFIID | Taf2 C-terminus | Taf2-ΔC loses Taf14 in vivo and in vitro but still incorporates stably into TFIID ([PMC5077207](https://pmc.ncbi.nlm.nih.gov/articles/PMC5077207)); TFIID subunit identification PMID:10788514, PMID:12138208 |
| TFIIF | Tfg1 | Third, yeast-specific subunit with Tfg1 and Tfg2 (Henry et al. 1994, PMID:7995524); UniProt notes no Taf14 homolog in TFIIF of higher eukaryotes |
| SWI/SNF | Snf5 | Reported as three copies of Taf14/SWP29 per complex (PMID:12524530) |
| RSC | Sth1 C-terminal region (residues 1183–1359) | Accessory subunit ([PMC7442819](https://pmc.ncbi.nlm.nih.gov/articles/PMC7442819)); the interaction is implicated in heat resistance and carbohydrate metabolism |
| INO80 | Ino80 | Purified subunit (Shen et al. 2003, PMID:12887900); placed in the Arp8 module with Arp4, actin and Ies4 ([PMC6071913](https://pmc.ncbi.nlm.nih.gov/articles/PMC6071913)) |
| NuA3 (NuA3a and NuA3b) | Yng1 motif plus Sas3 | John et al. 2000, PMID:10817755; two motifs are sandwiched between two ET domains, and disrupting both contacts impairs NuA3 function in transcription and DNA repair (Nguyen et al. 2024, [*Nat Commun*](https://link.springer.com/article/10.1038/s41467-024-49730-y), [PMC11196586](https://pmc.ncbi.nlm.nih.gov/articles/PMC11196586)) |

Kabani et al. 2005 (*BBRC*) reported that Anc1/Taf14 contacts the catalytic subunits of TFIID, TFIIF, RSC, INO80 and NuA3 (from memory).

**Mediator.** The UniProt record carries a GO "mediator complex" (IDA:SGD) line. None of the searches found support for Taf14 as a Mediator subunit, and it is not part of the accepted Mediator composition (from memory). I did not trace the source paper, so treat this as a probable co-purification artefact to be checked against the cited reference rather than dismissed outright.

## 4. Biological processes

- **RNA polymerase II transcription initiation.** Taf14 acts through TFIID and TFIIF. A 2020 study reported that the main role of the YEATS domain is to stabilise the pre-initiation complex, and that Taf14 interactions become crucial in rpb9Δ cells, where TFIIF recruitment is impaired (*Epigenetics & Chromatin* 2020, [DOAJ record](https://doaj.org/article/63eff72672de44c280419249a97c5bfd)).
- **Chromatin remodelling and histone acetylation.** Taf14 is a subunit of SWI/SNF, RSC and INO80 and of the H3K14 acetyltransferase NuA3. The remodelling and acetylation are catalysed by Snf2, Sth1, Ino80 and Sas3; Taf14 contributes reader and docking functions only.
- **DNA damage response.** Supported by the YEATS–H3K9ac work (PMID:26341557) and the NuA3 ET-domain study (2024).
- **Stress and metabolic gene regulation.** Heat-shock transcription ([BMC Genomics 2017](https://bmcgenomics.biomedcentral.com/track/pdf/10.1186/s12864-017-3544-6)) and metabolic-cycle repression of β-oxidation genes (Gowans 2019).
- **Actin cytoskeleton and morphogenesis.** The gene was first isolated as *anc1* (actin non-complementing); mutants show morphogenesis and actin defects, yet the protein is nuclear (Welch & Drubin 1994, PMID:7949419). The cytoskeletal phenotype is therefore best read as an indirect, pleiotropic consequence of altered transcription.

## 5. Localization

Taf14 is nuclear (Welch & Drubin 1994; UniProt), acting on chromatin at promoters (TFIID, TFIIF, SWI/SNF, NuA3a) and coding regions (NuA3b). Abundance is about 3,100 molecules per cell in log phase (PMID:14562106).

## 6. Evolution

Taf14 belongs to the YEATS family, with yeast paralogs Yaf9 and Sas5 and human relatives ENL (MLLT1), AF9 (MLLT3), YEATS4/GAS41 and YEATS2 (from memory, beyond the 1994 paper's title noting similarity to human leukemia proteins). The combination of an acyl-lysine-reading YEATS domain with an ET-like partner-docking domain parallels the reader-plus-recruitment architecture of ENL and AF9.

## 7. Open questions

- How Taf14 is partitioned among its six complexes, and whether the reported three copies per TFIID and SWI/SNF reflect ET-mediated dimerisation; [PMC11539623](https://pmc.ncbi.nlm.nih.gov/articles/PMC11539623) notes that the distribution mechanism is still under study.
- Whether phase separation occurs in vivo.
- Why the YEATS reader is largely dispensable for growth when the ET domain is not.
- The basis of the Mediator annotation.

## Sources

- [Chen et al. 2020, Taf14 recognizes a common motif (PubMed 32826896)](https://pubmed.ncbi.nlm.nih.gov/32826896/) · [PMC7442819](https://pmc.ncbi.nlm.nih.gov/articles/PMC7442819)
- [Klein et al. 2022, Taf2 mediates DNA binding of Taf14 (PMC9177701)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9177701/) · [PDB 7UHE](https://www.rcsb.org/structure/7UHE)
- [Nguyen et al. 2024, *Nat Commun* s41467-024-49730-y](https://link.springer.com/article/10.1038/s41467-024-49730-y) · [PMC11196586](https://pmc.ncbi.nlm.nih.gov/articles/PMC11196586)
- [Nguyen et al., Taf14 complex formation (PMC11539623)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11539623) (publication year not confirmed)
- [Gowans et al. 2019 (PMC6931132)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6931132)
- [Schulze et al. 2010, *Mol Genet Genomics*](https://link.springer.com/doi/10.1007/s00438-010-0523-x)
- [Taf2 C-terminus and Taf14 in TFIID, 2016 (PMC5077207)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5077207)
- [Taf14 and PIC stabilisation, *Epigenetics & Chromatin* 2020](https://doaj.org/article/63eff72672de44c280419249a97c5bfd)
- [INO80 cryo-EM (PMC6071913)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6071913)
- [BMC Genomics 2017, Taf14 and heat shock](https://bmcgenomics.biomedcentral.com/track/pdf/10.1186/s12864-017-3544-6)
- [PDB 6LQZ, Taf14 ET–Sth1](https://proteopedia.org/w/6lqz)
- [UniProt P35189](https://uniprot.org/uniprotkb/P35189/entry), including the PMIDs cited from its reference list (7949419, 7995524, 10788514, 10817755, 12138208, 12524530, 12887900, 14562106, 26341557, 27089029, 30385749)

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC6931132
2. https://pubmed.ncbi.nlm.nih.gov/32826896/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC7442819
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC11539623
5. https://link.springer.com/doi/10.1007/s00438-010-0523-x
6. https://proteopedia.org/w/6lqz
7. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9177701/
8. https://www.rcsb.org/structure/7UHE
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC5077207
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC6071913
11. https://link.springer.com/article/10.1038/s41467-024-49730-y
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC11196586
13. https://doaj.org/article/63eff72672de44c280419249a97c5bfd
14. https://bmcgenomics.biomedcentral.com/track/pdf/10.1186/s12864-017-3544-6
15. https://uniprot.org/uniprotkb/P35189/entry