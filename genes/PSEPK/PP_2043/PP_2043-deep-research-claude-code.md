---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:12:13.968586'
end_time: '2026-10-30T21:15:46.945472'
duration_seconds: 212.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2043
  gene_symbol: PP_2043
  uniprot_accession: Q88L92
  protein_description: 'RecName: Full=DUF1329 domain-containing protein {ECO:0008006|Google:ProtNLM};'
  gene_info: OrderedLocusNames=PP_2043 {ECO:0000313|EMBL:AAN67657.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: DUF1329. (IPR010752); DUF1329 (PF07044)
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
  web_search_requests: 4
  num_turns: 18
  total_cost_usd: 1.002860085
  session_id: 0a7f1f2f-53ba-403a-9296-20f74a1d49ae
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 8
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88L92
- **Protein Description:** RecName: Full=DUF1329 domain-containing protein {ECO:0008006|Google:ProtNLM};
- **Gene Information:** OrderedLocusNames=PP_2043 {ECO:0000313|EMBL:AAN67657.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DUF1329. (IPR010752); DUF1329 (PF07044)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2043" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2043' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2043** (gene ID: PP_2043, UniProt: Q88L92) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Fitness browser is behind Cloudflare; running a few more literature searches on the DUF1329/TP0789 family and P. aeruginosa homologs.

Checking the Thompson 2020 full text to see whether it names PP_2042/PP_2043 (or only PP_0765/PP_0766).

# PP_2043 (UniProt Q88L92), a DUF1329 protein of unknown function in *Pseudomonas putida* KT2440

## Summary

Nobody has studied PP_2043 itself in the lab. I found no paper that characterises it directly. Its GOA file has only a header row, so the gene has no existing GO annotations.

What can be inferred:
- It is a **secreted, soluble protein** of 442 amino acids. It has a cleavable Sec signal peptide and **no lipobox**, so it probably lives in the **periplasm**.
- It belongs to the **DUF1329 family (Pfam PF07044, InterPro IPR010752)**. That family is predicted to have the **LolA/LolB/LppX fold** (CDD cd16329, "LolA_like"; Gene3D 2.50.20.10). This is the fold of proteins that carry hydrophobic cargo through the periplasm.
- PP_2043 sits directly downstream of **PP_2042**, a gene for a DUF1302 protein. DUF1302 is predicted to be an outer-membrane β-barrel. DUF1302 and DUF1329 genes almost always occur together.
- A paralogous DUF1302/DUF1329 pair in the same strain, **PP_0765/PP_0766**, is needed to grow on fatty-acid esters (Tween 20 and butyl stearate). Two competing ideas explain this:
  - the pair hydrolyses the esters ("esterase" hypothesis);
  - the pair exports a cell-envelope component together with a BNR protein and an RND exporter.

The most defensible statement is: *a periplasmic protein with a LolA-like fold, part of a DUF1302–DUF1329 outer-membrane system of unknown cargo, possibly linked to how cells handle hydrophobic substrates such as fatty-acid esters*. There is **no evidence for any catalytic activity, specific substrate or biological process** that would justify a specific GO molecular-function or process term.

---

## 1. Identity checks

| Item | Value | Source |
|---|---|---|
| Accession | Q88L92 (TrEMBL, unreviewed) | UniProt record `PP_2043-uniprot.txt` |
| Locus | PP_2043 (EMBL AAN67657.1) | UniProt |
| Organism | *P. putida* KT2440 (taxon 160488) | UniProt |
| Length | 442 aa, 49.0 kDa | UniProt SQ line |
| Name | "DUF1329 domain-containing protein". This is a ProtNLM machine-generated name (ECO:0008006), not a curated one. | UniProt DE |
| GenBank annotation | "conserved exported protein of unknown function" | KEGG ppu:PP_2043 |
| Domains | Pfam PF07044 DUF1329; InterPro IPR010752; CDD cd16329 LolA_like; Gene3D 2.50.20.10 "Lipoprotein localisation LolA/LolB/LppX". KEGG also lists a "TP_0789-like" motif. | UniProt DR lines; KEGG |
| GO annotations | None. GOA file is header only. | `PP_2043-goa.tsv` |

The symbol is a locus tag specific to KT2440, so it cannot be confused with another gene. Everything below about "DUF1329" is family-level information, applied to PP_2043 only by inference.

## 2. Sequence features and likely location

- **Signal peptide.** SignalP predicts residues 1–20, and the mature chain runs from 21 to 442 (UniProt FT SIGNAL/CHAIN, ECO:0000256|SAM:SignalP). The N-terminus is `MTMKMRMVMIGLFWASGTLAA|AGLPDN…`. That is a positively charged n-region, a hydrophobic h-region and an A-x-A cleavage motif, which is typical of a type I (signal peptidase I) Sec signal.
- **No lipoprotein lipobox.** There is no Cys at +1 of the mature protein and no [LVI][ASTVI][GAS]C motif. PP_2043 is therefore unlikely to be lipid-anchored. The paralog PP_0766 (`MNKTRSLLQAGVLGLSLLATSVMA|AVS…`) likewise has no lipobox (my own inspection of the local UniProt sequences).
- **No transmembrane segments** are annotated after the signal peptide.

**Likely location: periplasmic space (soluble).** This is a computational prediction. No fractionation or proteomic localisation data exist for PP_2043.

## 3. Family and structural inference: a LolA-like fold

- CDD and Gene3D both assign PP_2043 to the **LolA/LolB/LppX superfamily**. NCBI's LolA_fold-like family (cd16324) contains the periplasmic chaperone LolA, the outer-membrane lipoprotein receptor LolB and the N-terminal domain of RseB. LolA "accepts outer membrane (OM)-specific lipoproteins that are released from the inner membrane by the LolCDE complex and transfers them to the OM receptor LolB" ([NCBI CDD cd16324](https://www.ncbi.nlm.nih.gov/Structure/cdd/cd16324)).
- This fold is an **incomplete β-barrel with a hydrophobic cavity**. Its general job is to shield hydrophobic cargo (lipid moieties, acylated molecules) while it crosses the aqueous periplasm. LppX in mycobacteria uses the same fold to carry complex lipids. That suggests DUF1329 is a periplasmic **carrier or chaperone for a hydrophobic molecule**. It need not be a lipoprotein carrier: PP_2043 has no partner Lol machinery encoded nearby.
- The NCBI CDD record for the partner family DUF1302 (pfam06980) says that DUF1302 proteins are predicted outer-membrane β-barrels, "probably part of an exporter system" that includes an MMPL-family exporter and a DUF1329 protein that "likely acts as a LolA-like chaperone" ([NCBI CDD pfam06980](https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam06980)).
- In the Fitness Browser reannotations for *Kangiella aquimarina*, DUF1329 is described as distantly related to LolB and predicted to sort an adhesin to the outer membrane. That prediction rests on co-fitness with a putative adhesin, an MmpL exporter and a BNR-repeat outer-membrane protein ([Fitness Browser, *K. aquimarina* reannotations](https://fitprivate.genomics.lbl.gov/cgi-bin/orgReanno.cgi?orgId=Kang)). It is a prediction, not a measurement.

**Interpretation:** the fold supports a role as a **periplasmic carrier of a hydrophobic or amphipathic molecule**, working with the outer-membrane DUF1302 protein. The cargo is unknown. No study shows binding, and no study shows enzymatic activity.

## 4. Genomic context in KT2440

Coordinates and annotations below are from the KEGG REST entries for ppu:PP_2039–PP_2046.

| Locus | Strand / position | Annotation |
|---|---|---|
| PP_2039 | + 2,317,759–2,318,925 | putative acyl-CoA dehydrogenase |
| PP_2040 | + 2,318,988–2,320,283 | MFS transporter |
| PP_2041 | − 2,320,296–2,321,240 | LysR-family regulator |
| **PP_2042** | + 2,321,455–2,323,308 | DUF1302 exported protein (predicted OM β-barrel) |
| **PP_2043** | + 2,323,313–2,324,641 | **DUF1329 exported protein** |
| PP_2044 | + 2,324,641–2,325,027 | DUF202 inner-membrane protein (YidH-like) |
| PP_2045 | − 2,325,342–2,327,303 | linear primary-alkylsulfatase (metallo-β-lactamase fold, SCP2 domain) |
| PP_2046 | − 2,327,405–2,328,328 | LysR-family regulator |

- PP_2042, PP_2043 and PP_2044 are on the same strand. The gaps are 4 bp between PP_2042 and PP_2043, and the stop of PP_2043 overlaps the start of PP_2044. This strongly suggests **one operon, PP_2042-PP_2043(-PP_2044)**. A divergent LysR regulator (PP_2041) sits upstream.
- The neighbours are **lipid/acyl-related**: an acyl-CoA dehydrogenase, and an alkylsulfatase with an SCP2 lipid-binding domain. This resembles the setting of the paralogous PP_0765/PP_0766 pair, which is "near fatty acid catabolic genes" (Thompson et al. 2020, below). Unlike some DUF1302/1329 loci, this one has **no adjacent MMPL or RND exporter** gene.

## 5. Experimental evidence from the paralogous pair PP_0765/PP_0766

The only relevant experimental data are from **Thompson et al. 2020**, *Appl Environ Microbiol* 86:e01665-20 ([PMID:32826213](https://pubmed.ncbi.nlm.nih.gov/32826213/); [PMC7580535](https://pmc.ncbi.nlm.nih.gov/articles/PMC7580535/); DOI 10.1128/AEM.01665-20). The authors ran RB-TnSeq on KT2440 with 13 fatty acids and 10 alcohols as carbon sources.

- "PP_0765 and PP_0766 encode a DUF1302 family protein and a DUF1329 family protein, respectively." They are "likely coexpressed in an operon positively regulated by the LuxR-type regulator PP_0767."
- PP_0765, PP_0766 and PP_0767 had "significant and severe fitness defects specific to Tween 20" compared with laurate (C12). PP_0765 and PP_0766 (with PP_2018 and PP_4058) were also specific to **butyl stearate** compared with myristate. So the defect shows up only when the fatty acid is supplied as an **ester**.
- The authors propose: "PP_0765 and PP_0766 contribute to catalyzing the hydrolysis of fatty esters, accounting for the missing catabolic step of butyl stearate and Tween 20". The abstract puts it as "DUF1302/DUF1329 family proteins potentially function as esterases."
- They also note the alternative. Earlier work in other pseudomonads found co-fitness of DUF1302/DUF1329 genes "with BNR domain and RND family efflux genes when grown on Tween 20". Those authors "proposed that the genes may work together in order to export a component of the cell wall."
- They state plainly that "Further work will need to be done to biochemically characterize the potential enzymatic activity of these proteins."

**What this means for PP_2043:**
1. PP_2043 itself is not discussed. In the portion of the paper I could verify, it is not mentioned at all. PP_2042/PP_2043 is a **paralogous** copy of the PP_0765/PP_0766 system. It might handle a different cargo, or be expressed under different conditions.
2. The esterase idea is a hypothesis, and a weak one. Neither DUF family has a recognisable hydrolase motif (no α/β-hydrolase fold, no Ser-His-Asp triad). The ester-specific phenotype fits an envelope role just as well: on an ester carbon source the cells may depend on an **outer-membrane function** (presenting or secreting a lipase, or remodelling the envelope). A pooled fitness assay would detect that as well as it would detect an esterase. Thompson et al. themselves note that a secreted or outer-membrane esterase activity "would be shared among the library."
3. The fold evidence fits a **non-catalytic carrier** better than an esterase.

## 6. Proposed model for PP_2043 (inference only)

```
cytoplasm ──(Sec)──► PP_2043 mature protein in periplasm (LolA-like fold)
                       │ binds / shuttles an unknown hydrophobic or amphipathic cargo
                       ▼
                     PP_2042 (DUF1302, predicted OM β-barrel) ──► outer membrane / cell surface
                     PP_2044 (DUF202 inner-membrane protein) – co-transcribed, role unknown
```

- **Molecular function:** a lipid- or hydrophobic-molecule carrier (LolA-like) is plausible. Catalytic (esterase) activity is speculative.
- **Biological process:** probably part of outer-membrane-directed transport or export of an envelope component or surface protein. Under some conditions it may support use of fatty-acid esters. This rests only on the paralog's phenotype.
- **Location:** periplasmic space, predicted from the signal peptide, the absence of a lipobox or TM helices, and the soluble LolA fold.

## 7. Implications for GO annotation

- **Cellular component:** "periplasmic space" (GO:0042597) is the one claim that is reasonably supported. It rests on two lines: the SignalP signal peptide with no lipobox or TM segment, and the soluble LolA/LolB periplasmic-carrier fold. An IEA/ISM-level inference would be defensible. Nothing here supports "outer membrane".
- **Molecular function / biological process:** there is no basis yet for "esterase activity", "lipoprotein transporter activity" or "lipoprotein localization to outer membrane". The LolA analogy is a fold similarity, not functional orthology. Transferring Lol-pathway GO terms would be an over-annotation.
- If any process term is wanted, a broad one would be the most that could be argued, and only with a caveat that it is a prediction. I would leave MF and BP unannotated.

## 8. Open questions and experiments

1. **Cargo:** what does the PP_2043 hydrophobic cavity bind? Lipidomics of the purified periplasmic protein, or crystallography or an AlphaFold-based cavity analysis.
2. **Phenotype:** does deleting PP_2042-PP_2044 give an ester- or lipid-specific growth defect like ΔPP_0765-0766? Are the two systems redundant (double mutant)? The KT2440 Fitness Browser data for PP_2042/PP_2043 would answer part of this, but the site blocked automated access, so I could not check it.
3. **Esterase test:** assay purified PP_2042 and PP_2043, singly and together, against Tween 20 or p-nitrophenyl esters. That would directly confirm or rule out the esterase hypothesis.
4. **Location:** fractionate cells (periplasm, inner membrane, outer membrane) with tagged PP_2043.
5. **Regulation:** what does the divergent LysR regulator PP_2041 respond to? Lipid or acyl-CoA inducers would point to substrate handling.

## Sources

- UniProt Q88L92 flat file (local `genes/PSEPK/PP_2043/PP_2043-uniprot.txt`): signal peptide, PF07044/IPR010752, CDD cd16329, Gene3D 2.50.20.10, ProtNLM name.
- KEGG GENES ppu:PP_2039 – PP_2046 (https://rest.kegg.jp/get/ppu:PP_2043): gene neighbourhood and annotations.
- Thompson MG et al. (2020) *Appl Environ Microbiol* 86(21):e01665-20, PMID:32826213, https://pmc.ncbi.nlm.nih.gov/articles/PMC7580535/
- NCBI CDD pfam06980 (DUF1302): https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam06980
- NCBI CDD cd16324 (LolA_fold-like): https://www.ncbi.nlm.nih.gov/Structure/cdd/cd16324
- Fitness Browser reannotations, *Kangiella aquimarina*: https://fitprivate.genomics.lbl.gov/cgi-bin/orgReanno.cgi?orgId=Kang
- PaperBLAST family search PF07044: https://papers.genomics.lbl.gov/cgi-bin/hmmSearch.cgi?hmmId=PF07044
- STRING (DUF1329 homolog context): https://string-db.org/network/62928.azo0037

**Limits of this report:**
- No primary literature on PP_2043 was found.
- I could only verify about the first quarter of the Thompson et al. full text word for word. "Not mentioned" for PP_2042/PP_2043 applies to that portion.
- The KT2440 Fitness Browser pages were behind a Cloudflare challenge and were not consulted.

## Citations

1. https://www.ncbi.nlm.nih.gov/Structure/cdd/cd16324
2. https://www.ncbi.nlm.nih.gov/Structure/cdd/pfam06980
3. https://fitprivate.genomics.lbl.gov/cgi-bin/orgReanno.cgi?orgId=Kang
4. https://pubmed.ncbi.nlm.nih.gov/32826213/
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC7580535/
6. https://rest.kegg.jp/get/ppu:PP_2043
7. https://papers.genomics.lbl.gov/cgi-bin/hmmSearch.cgi?hmmId=PF07044
8. https://string-db.org/network/62928.azo0037