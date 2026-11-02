---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:33:03.937390'
end_time: '2026-10-30T21:35:01.433855'
duration_seconds: 117.5
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_3231
  gene_symbol: PP_3231
  uniprot_accession: Q88HX2
  protein_description: 'SubName: Full=Uncharacterized protein {ECO:0000313|EMBL:AAN68838.1};'
  gene_info: OrderedLocusNames=PP_3231 {ECO:0000313|EMBL:AAN68838.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Emycin_Estase. (IPR007815); UCP036794_erythomycin. (IPR014622);
    Erythro_esteras (PF05139)
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
  web_search_requests: 3
  num_turns: 8
  total_cost_usd: 0.6148450999999999
  session_id: a10c7d57-c5ea-40a6-ae3c-1a6f268203a2
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88HX2
- **Protein Description:** SubName: Full=Uncharacterized protein {ECO:0000313|EMBL:AAN68838.1};
- **Gene Information:** OrderedLocusNames=PP_3231 {ECO:0000313|EMBL:AAN68838.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Emycin_Estase. (IPR007815); UCP036794_erythomycin. (IPR014622); Erythro_esteras (PF05139)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_3231" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_3231' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_3231** (gene ID: PP_3231, UniProt: Q88HX2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Research report: PP_3231 (UniProt Q88HX2), *Pseudomonas putida* KT2440

## Summary

No published experiment has characterised PP_3231. Its function can only be inferred from its domains. The protein belongs to the erythromycin esterase (Ere) family, a group of enzymes that use a metal-independent, histidine-based catalytic mechanism and include esterases that inactivate macrolide antibiotics. Its putative catalytic residues are conserved, so it is probably an active hydrolase that acts on esters. Nothing shows that its natural substrate is erythromycin or any other macrolide. The only GO annotation, "response to antibiotic" (IEA, from InterPro), is a family-level guess and should be treated as weak.

## 1. Identity check

| Field | Value | Source |
|---|---|---|
| Accession | Q88HX2 (TrEMBL, unreviewed, 455 aa, 52.2 kDa) | UniProt record |
| Locus | PP_3231 (EMBL AAN68838.1; RefSeq WP_010954115.1) | UniProt record |
| Organism | *P. putida* KT2440 (taxon 160488) | UniProt record |
| Name | "Uncharacterized protein" (submitter-assigned, ECO:0000313) | UniProt record |
| Protein existence | PE 4: Predicted | UniProt record |
| Domains | Pfam PF05139 Erythro_esteras; InterPro IPR007815 Emycin_Estase and IPR014622 (PIRSF036794, UCP_erythr_ester); CDD cd14728 Ere-like; Gene3D 3.40.1660.10 and 3.30.1870.10 (EreA-like domains); SUPFAM SSF159501 EreA/ChaN-like | UniProt record |
| PANTHER | PTHR31299 / PTHR31299:SF0 "ESTERASE, PUTATIVE (AFU_ORTHOLOGUE AFUA_1G05850)-RELATED" | UniProt record |
| eggNOG | COG2312 (erythromycin esterase homolog) | UniProt record |

The locus tag, organism and domain content all agree. A web search for "PP_3231" turned up no literature on this gene. The only literature on KT2440 as a whole is the genome papers ([Nelson et al. 2002, PMID:12534463](https://umiacswww-vip.umiacs.umd.edu/node/19075); Belda et al. 2016, PMID:26913973), which annotate it only as a hypothetical or uncharacterised protein. **The literature on this protein is therefore limited to genome annotation. Everything below is inferred from the family it belongs to.**

## 2. The erythromycin esterase family (what PP_3231 is related to)

### 2.1 Biochemistry of the family
- **Founding members.** EreA and EreB are plasmid-encoded enzymes that make bacteria resistant to 14- and 15-membered macrolides. They hydrolyse the macrolactone ester bond, which opens the ring and inactivates the antibiotic. The fold is distinct from serine esterases.
- **Mechanism.** Morar *et al.* (2012, *Biochemistry* 51:1740–1751, PMID:22303981) combined kinetics, mutagenesis, solvent isotope effects, pH profiles and inhibitor studies. They ruled out a Ser or Thr nucleophile and found that one histidine (H46 in EreB) is essential. They proposed that this histidine acts as a general base that activates a water molecule to attack the ester. EreA, EreB and the *Bacillus cereus* homologue Bcr136 had distinct properties. Only EreA was inhibited by chelators, and the authors suggested it holds a non-catalytic metal. The paper's title, "Mechanism and Diversity of the Erythromycin Esterase Family of Enzymes", reflects its point that this family is widespread in bacteria beyond the known resistance genes. ([Wright lab summary](https://www.thewrightlab.com/publications-1/2012/2/10/mechanism-and-diversity-of-the-erythromycin-esterase-family-of-enzymes); [PubMed 22303981](https://www.ncbi.nlm.nih.gov/pubmed/22303981); [McMaster thesis](https://macsphere.mcmaster.ca/handle/11375/12688))
- **Structure.** Zieliński *et al.* (2021, *Nat. Commun.* 12:1732, doi:10.1038/s41467-021-22016-3) solved the first crystal structures in the family, of EreC (>90% identical to EreA). They captured closed and open forms that differ in a flexible loop at residues ~295–303 (PDB 6XCQ and 6XCS). The active-site residues are His50, Glu78, His289, Glu47, Arg261 and Asp262. Earlier mutagenesis had shown that E78A abolishes activity and H289A lowers k_cat about 1000-fold. A secondary summary describes His50 as the catalytic base, Glu47 as positioning His50, and Glu78 and His289 as substrate-specificity residues. That summary has not been checked against the primary text. ([PMC7979712](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7979712/); [RCSB 6XCQ](https://rcsb.org/structure/6XCQ); [RCSB 6XCS](https://rcsb.org/structure/6XCS); [arXiv 2505.23356](https://arxiv.org/pdf/2505.23356))

### 2.2 Conserved catalytic residues in PP_3231 (my own sequence analysis)
I compared the Q88HX2 sequence with the EreC active-site motifs by eye. I did not run a formal alignment. The PP_3231 residue numbers below were checked with a script against the UniProt sequence.

| EreC residue | Role (as summarised above) | PP_3231 candidate | Local context |
|---|---|---|---|
| Glu47 | positions the catalytic His | **E60** | LLG**E**ASH |
| His50 | general base | **H63** | EAS**H**GSS |
| Glu78 | essential (E78A inactive) | **E91** | VAV**E**ADW |
| Arg261 / Asp262 | active site | **R268 / D269** | WNL**RD**RH |
| His289 | substrate binding; H289A lowers k_cat ~1000× | **H294 or H297** | VWA**H**NS**H**IG |

The E-x-x-H motif keeps exactly the same spacing as in EreC (E47/H50 corresponds to E60/H63). E91 sits the same distance (+13) from EreC Glu78 as E60 does from Glu47. **Interpretation:** the catalytic machinery appears intact, so PP_3231 is probably a catalytically active Ere-type hydrolase rather than a pseudoenzyme. This remains an inference until a formal alignment or structure-based superposition (for example the AlphaFold model against 6XCQ) confirms the correspondence.

## 3. Likely function of PP_3231

- **Molecular function, best supported:** a hydrolase acting on carboxylic ester bonds (GO:0016788 level), using the Ere-family general-base mechanism.
- **Substrate:** unknown. Three points argue against assigning erythromycin esterase activity (EC 3.1.1.-, macrolide hydrolysis) directly:
  1. PP_3231 is classified in the PIRSF036794 "uncharacterised protein" subgroup and in PANTHER PTHR31299, whose name refers to fungal orthologues. It does not cluster with the mobile EreA/EreB/EreC/EreD resistance determinants.
  2. Morar *et al.* (2012) stress that the family is diverse, and that homologues such as Bcr136 differ biochemically from EreA and EreB.
  3. The gene is chromosomal and core to *P. putida*. It does not appear to be a mobile resistance element, and Pseudomonads are intrinsically macrolide-tolerant mainly through efflux and outer-membrane impermeability.

  The natural substrate may therefore be an endogenous or environmental ester, for example a plant- or soil-derived macrolactone or polyketide. This is speculation.
- **Localisation:** no signal peptide or transmembrane segment is annotated in the UniProt entry (no Phobius or SignalP features). Characterised Ere enzymes are cytoplasmic. The **cytoplasm** is the most likely location, but this is predicted only.
- **Pathway:** none assigned. KEGG ppu:PP_3231 and BioCyc have no pathway placement for it.

## 4. Assessment of the existing GO annotation

| Term | Evidence | Assessment |
|---|---|---|
| GO:0046677 response to antibiotic (BP) | IEA, InterPro2GO from IPR007815 | **Over-annotation.** The mapping assumes every Ere-family member confers macrolide resistance. No data show that PP_3231 hydrolyses antibiotics or responds to them. A conservative action would be MARK_AS_OVER_ANNOTATED, or UNDECIDED. |

A defensible new annotation would be an esterase/hydrolase MF term at the GO:0016788 level ("hydrolase activity, acting on ester bonds"). It would rest on family membership and the conserved E-x-x-H/E catalytic residues (an ISS/IC-type inference). Erythromycin esterase activity specifically should not be annotated without biochemical data.

## 5. Open questions and suggested experiments

1. Purify recombinant PP_3231 and test it against erythromycin, azithromycin and other macrolides, and against generic esters such as p-nitrophenyl esters. Measure kinetics.
2. Mutate H63A and E91A to test whether the Ere mechanism is conserved.
3. Measure the macrolide MIC of a ΔPP_3231 mutant and the wild type, for example using the KT2440 RB-TnSeq fitness data in the Fitness Browser (not consulted here).
4. Superpose the AlphaFold model on EreC (6XCQ) and compare substrate-pocket volume and the conformation of the flexible lid loop.

## Sources
- UniProt Q88HX2 flat file (local copy: `genes/PSEPK/PP_3231/PP_3231-uniprot.txt`)
- Morar M. *et al.* (2012) Mechanism and diversity of the erythromycin esterase family of enzymes. *Biochemistry* 51:1740–1751. PMID:22303981: [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/22303981), [Wright lab](https://www.thewrightlab.com/publications-1/2012/2/10/mechanism-and-diversity-of-the-erythromycin-esterase-family-of-enzymes), [CORE](https://core.ac.uk/works/49968234), [McMaster](https://macsphere.mcmaster.ca/handle/11375/12688)
- Zieliński M. *et al.* (2021) Structural and functional insights into esterase-mediated macrolide resistance. *Nat. Commun.* 12:1732: [PMC7979712](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7979712/), [DOAJ](https://doaj.org/article/7b2d872b0cc04ef1b3ff7eb82c9ff6ed)
- PDB [6XCQ](https://rcsb.org/structure/6XCQ) and [6XCS](https://rcsb.org/structure/6XCS)
- Secondary summary of EreC active-site roles (unverified against the primary paper): [arXiv 2505.23356](https://arxiv.org/pdf/2505.23356)
- Nelson K.E. *et al.* (2002) Complete genome sequence of *P. putida* KT2440. *Environ. Microbiol.* 4:799–808: [link](https://umiacswww-vip.umiacs.umd.edu/node/19075)
- Belda E. *et al.* (2016) The revisited genome of *P. putida* KT2440. *Environ. Microbiol.* 18:3403–3424 (PMID:26913973; cited from the UniProt record)

## Citations

1. https://umiacswww-vip.umiacs.umd.edu/node/19075
2. https://www.thewrightlab.com/publications-1/2012/2/10/mechanism-and-diversity-of-the-erythromycin-esterase-family-of-enzymes
3. https://www.ncbi.nlm.nih.gov/pubmed/22303981
4. https://macsphere.mcmaster.ca/handle/11375/12688
5. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7979712/
6. https://rcsb.org/structure/6XCQ
7. https://rcsb.org/structure/6XCS
8. https://arxiv.org/pdf/2505.23356
9. https://core.ac.uk/works/49968234
10. https://doaj.org/article/7b2d872b0cc04ef1b3ff7eb82c9ff6ed