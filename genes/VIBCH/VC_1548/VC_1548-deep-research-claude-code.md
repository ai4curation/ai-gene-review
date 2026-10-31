---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T21:32:00.692869'
end_time: '2026-10-30T21:37:22.293142'
duration_seconds: 321.6
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: VIBCH
  gene_id: VC_1548
  gene_symbol: VC_1548
  uniprot_accession: H9L4R2
  protein_description: 'RecName: Full=TonB system biopolymer transport component {ECO:0008006|Google:ProtNLM};'
  gene_info: OrderedLocusNames=VC_1548 {ECO:0000313|EMBL:AAF94702.1};
  organism_full: Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
  protein_family: Not specified in UniProt
  protein_domains: UCP028069. (IPR016866); DUF3450 (PF11932)
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
  - claude-opus-5
  - claude-opus-5-5
  web_search_requests: 2
  num_turns: 15
  total_cost_usd: 1.0227387000000001
  session_id: 2edb84a6-3bc1-4698-a769-ffbe5e631f18
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 10
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** H9L4R2
- **Protein Description:** RecName: Full=TonB system biopolymer transport component {ECO:0008006|Google:ProtNLM};
- **Gene Information:** OrderedLocusNames=VC_1548 {ECO:0000313|EMBL:AAF94702.1};
- **Organism (full):** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** UCP028069. (IPR016866); DUF3450 (PF11932)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VC_1548" matches the protein description above**
2. **Verify the organism is correct:** Vibrio cholerae serotype O1 (strain ATCC 39315 / El Tor Inaba N16961).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VC_1548' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VC_1548** (gene ID: VC_1548, UniProt: H9L4R2) in VIBCH.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

Fetched the V. vulnificus TtpB2/TtpD2 paper; now extracting the parts on the DUF3450-type protein.

I've confirmed VC_1548 is TtpB2 (NP_231188) in the V. cholerae tonB2 operon. Last step: pulling the TtpB2-specific results from Barnes et al. 2020 before I write the report.

# VC_1548 (UniProt H9L4R2) in *Vibrio cholerae* O1 El Tor N16961: TtpB2, a component of the TonB2 system

## Summary

VC_1548 is the *V. cholerae* copy of **TtpB2** (TonB2 transport protein B). It is a small protein of 252 amino acids with an N-terminal signal peptide, a coiled coil (leucine zipper) and a DUF3450 domain. It is the first gene of the **TonB2 energy-transduction operon** on chromosome I.

The only direct experimental work on this protein is in *Vibrio vulnificus*. There, the TtpB2 orthologue is **absolutely required** for TonB2-dependent uptake of ferric siderophores. Within the genus it also shows **species-specific complementation**: TtpB2 from other *Vibrio* species, including *V. cholerae*, cannot replace the *V. vulnificus* protein (Barnes et al., 2020). No catalytic activity is expected. TtpB2 is best described as an accessory, non-enzymatic structural or adaptor subunit of the TonB2–ExbB2–ExbD2 complex. That complex carries proton-motive-force energy to TonB-dependent outer-membrane receptors, which then import iron–siderophore and heme complexes.

Two things remain unknown: which residues or partners make up its specific interaction, and whether it sits in the periplasm or on the membrane. No study has examined VC_1548 itself in *V. cholerae*.

---

## 1. Identity check

| Attribute | Value | Source |
|---|---|---|
| UniProt | H9L4R2 (TrEMBL, unreviewed; PE 4 "Predicted") | local UniProt record |
| Locus | VC_1548; RefSeq NP_231188.1 / WP_001881338.1; GenBank AAF94702.1 | UniProt; NCBI ESummary ("hypothetical protein VC1548 [Vibrio cholerae O1 biovar El Tor str. N16961]") |
| Organism | *V. cholerae* O1 El Tor N16961, chromosome I, complement(1660180..1660938) | KEGG vch:VC_1548 |
| Length | 252 aa, 28.5 kDa | UniProt |
| Domains | DUF3450 (PF11932); IPR016866 / PIRSF028069 (UCP028069) | UniProt |
| Features | Signal peptide 1–18 (SignalP); coiled coil 42–97 (Coils) | UniProt |
| UniProt name | "TonB system biopolymer transport component" (ProtNLM machine-generated name) | UniProt |

**The identification is confirmed.** Barnes et al. (2020) list the *V. cholerae* O1 El Tor TtpB2 under RefSeq accession **NP_231188**, and NCBI resolves that accession to the VC1548 product (verified by ESummary). The same paper lists TtpD2 as NP_231183, which resolves to VC1543 (verified by efetch). The gene symbol is not ambiguous here: "VC_1548" is a locus tag, and the literature calls the protein **TtpB2** (or "TtpB" generically).

The ProtNLM name "TonB system biopolymer transport component" is a machine prediction (ECO:0008006). Even so, it is consistent with the published experimental assignment of the orthologue.

## 2. Genomic context: the *V. cholerae* tonB2 cluster

From KEGG gene records (chromosome I, all on the minus strand):

| Locus | Size | Annotation / Pfam | TonB2-system name |
|---|---|---|---|
| VC_1543 | 392 aa | TPR repeats | **TtpD2** |
| VC_1544 | — | TonB_C; K03832 | **TonB2** |
| VC_1545 | — | ExbD; K03559 | **ExbD2** |
| VC_1546 | — | MotA_ExbB; K03561 | **ExbB2** |
| VC_1547 | 457 aa | MotA_ExbB (+ DUF3450-like hit) | **TtpC2** |
| **VC_1548** | 252 aa | **DUF3450** | **TtpB2** |
| VC_1549–1551 | — | UgpB/A/E glycerol-3-phosphate ABC transporter (opposite strand) | unrelated |

The six genes are adjacent and lie on the same strand. Read in the direction of transcription, the order is ttpB2 (VC_1548) → ttpC2 → exbB2 → exbD2 → tonB2 → ttpD2 (VC_1543). This matches the *V. vulnificus* operon, where "the gene ttpB2 is located immediately upstream of ttpC2 and is the first gene in the tonB2 operon… ttpD2 is the last gene in the tonB2 operon and is found downstream of tonB2" (Barnes et al., 2020). In *V. vulnificus*, a predicted Fur-binding site and promoter sit just upstream of ttpB2, which implies the operon is induced when iron is low. The same arrangement is expected in *V. cholerae*, but this has not been tested.

## 3. Primary function: an essential accessory subunit of the TonB2 energy-transduction complex

### 3.1 The TonB2 system

In Gram-negative bacteria, active transport across the outer membrane needs proton-motive-force (PMF) energy from the inner membrane. The **TonB–ExbB–ExbD** complex delivers that energy to TonB-dependent outer-membrane receptors (Stork et al., 2007; Braun et al., 2023). Every *Vibrio* species studied has at least two TonB systems. The **TonB2 systems are unusual because they need extra "Ttp" proteins** (Kuehl & Crosa, 2010; Payne et al., 2016):

- **TtpC** (VC_1547 in *V. cholerae*) was the first one identified. A polar insertion in ttpC blocked ferric-anguibactin transport in *V. anguillarum*, and TtpC co-purified in a complex that may also contain TonB2, ExbB2 and ExbD2. The authors also showed that "TtpC from *V. cholerae* also plays a role in the TonB2-mediated transport of enterobactin" (Stork et al., 2007, PMID:17189363). TtpC from several vibrios can complement in other species (Kuehl & Crosa, 2009, PMID:19130262; Kustusch et al., 2012, PMID:22505675). TtpC is thought to span the periplasm and so connect the PMF to the outer-membrane receptors, which the short TonB2 protein cannot reach alone (Kuehl & Crosa, 2010, PMID:20860484).
- **TtpB and TtpD** were added later. Barnes et al. (2020) state that "All six protein components of the TonB2 system—TonB2, ExbB2, ExbD2, TtpB2, TtpC2, and TtpD2—are essential for the uptake of both endogenously produced iron-bound siderophores and exogenous siderophores produced from other organisms" (PMID:31595707).

### 3.2 Experimental evidence on TtpB2 (from the *V. vulnificus* orthologue)

All of the following comes from Barnes et al., *MicrobiologyOpen* 2020 (PMID:31595707, PMC6957404). The experiments were done in *V. vulnificus* strains that lacked TonB1 and TonB3, so that only TonB2 could work:

- **Iron-limited growth.** "Both TtpB2 and TtpD2 are absolutely required for the function of the TonB2 system in *V. vulnificus* for growth in iron-limited conditions."
- **Endogenous siderophore.** ΔttpB2 strains could not take up vulnibactin through TonB2.
- **Exogenous siderophores.** ΔttpB2 strains also could not take up siderophores made by other organisms. In TonB2-only backgrounds the assays included vibriobactin, vibrioferrin, ferrioxamine and enterobactin.
- **No cross-complementation by TtpB3.** The paralogue TtpB3 (about 30% similar) is present in the strains but "cannot be used in place of TtpB2". TtpB3 and TtpD3 are inactive in iron transport.
- **Species-specific complementation.** Only *V. vulnificus* TtpB2 (biotype 1 or 2) restored growth. "Provision of any other TtpB2 protein from different *Vibrio* species… was not able to restore growth". The plasmids tested included a *V. cholerae* CA401 ttpB2 clone. The authors conclude that "the TonB2 system has a specificity for its own TtpB2 protein but not TtpD2." TtpC2 and TtpD2, by contrast, complement freely across species. This suggests TtpB2 makes close, co-evolved contacts with other subunits of its own complex.

**What this means for VC_1548.** By orthology and conserved operon position, VC_1548 is expected to be needed for TonB2-dependent iron acquisition in *V. cholerae*. The inference is strong but untested in *V. cholerae*. The species-specificity result also shows that VC_1548 does not work with the *V. vulnificus* TonB2 machinery. That fits a role tuned to the *V. cholerae* TonB2/ExbB2/ExbD2/TtpC2 partners.

### 3.3 Substrates of the *V. cholerae* TonB2 pathway that VC_1548 likely supports

TtpB2 is not a transporter and is not expected to bind the substrates itself. Its "substrates" are those of the TonB2-dependent outer-membrane receptors it helps to energise. In *V. cholerae*, TonB1 and TonB2 overlap: both support uptake of **hemin, vibriobactin and ferrichrome** (Seliger et al., 2001, *Mol Microbiol

I'll finish the report, picking up where it stopped — without reproducing the withheld portion.

## 3.3 Pathway context (continued)

TtpB2 is not itself a transporter and is not expected to bind iron substrates. Its functional "substrates" are those of the TonB-dependent outer-membrane receptors that the TonB2 complex energizes. In *V. cholerae*, the two TonB systems have overlapping and distinct roles: both can support hemin, vibriobactin and ferrichrome utilization, and mutations in either system reduce competitive colonization in the infant mouse model (Seliger, Mey, Valle & Payne, *Mol Microbiol* 39:801–812, 2001). TonB2 is specifically required for enterobactin uptake via VctA or IrgA, and TtpC was shown to contribute to that TonB2-mediated enterobactin transport in *V. cholerae* (Stork et al. 2007, PMID:17189363). Since TtpB2 is an essential component of the same six-protein complex in *V. vulnificus*, VC_1548 is predicted to be required for this same set of TonB2-dependent uptake events — a prediction that has not been tested directly in *V. cholerae*.

## 4. Localization

No experimental localization data exist for VC_1548 or any TtpB orthologue. The available evidence is computational:

- **SignalP** predicts a cleaved signal peptide (residues 1–18) with the mature chain 19–252 (UniProt H9L4R2, ECO:0000256|SAM:SignalP), indicating Sec-dependent export out of the cytoplasm.
- **Coils** predicts a coiled coil at residues 42–97 (ECO:0000256|SAM:Coils); Barnes et al. describe an N-terminal leucine zipper motif (Leu-X6-Leu-X6-Leu-X6-Leu) in TtpB2.
- No transmembrane helix is predicted in the UniProt record.

Together these point to a **periplasmic** protein (or one peripherally associated with the inner membrane face), consistent with a role bridging or scaffolding within the TonB2 complex, which itself spans from the inner membrane across the periplasm to outer-membrane receptors. The coiled coil is the kind of element used for protein–protein interaction, and fits the observed species-specific partner requirement. This should be treated as inference from sequence features, not as established localization.

## 5. Family and evolutionary notes

- **DUF3450 (PF11932) / IPR016866 (PIRSF028069)** is the defining domain. Barnes et al. note that DUF3450 "appears in both eukaryotes and bacteria and always contains about 260 amino acids" — matching the 252-aa length of VC_1548. The eukaryotic occurrences are unlikely to be functionally related to TonB energization.
- **eggNOG COG3883**, assigned in the UniProt record, is a poorly characterized/"predicted membrane protein" category — i.e. no independent functional assignment.
- The KEGG motif listing for VC_1548 (DUF3450 plus a long tail of coiled-coil-rich families such as DUF4200, Fib_alpha, Nuf2_DHR10-like) is dominated by low-specificity coiled-coil matches and should not be read as evidence of relationship to those families. The one informative hit is DUF3450.
- **Paralogy caution:** VC_1547 (TtpC2) also returns a DUF3450-region hit in KEGG's motif list alongside its MotA_ExbB domain. TtpB and TtpC are distinct proteins with distinct genetics, so DUF3450 presence alone does not distinguish them; operon position and length (252 vs 457 aa) do.
- *V. vulnificus* carries a third system (TonB3) with ttpB3/ttpD3 paralogues that are **inactive in iron transport** (Barnes et al. 2020; Kustusch et al. 2012). This is a caution against assuming every DUF3450 protein in a TonB-like cluster is functional in iron uptake. *V. cholerae* N16961 is not reported to carry a TonB3 system.

## 6. Proposed annotation

| Aspect | Term | Evidence basis |
|---|---|---|
| Molecular function | No catalytic activity; protein-complex scaffolding/adaptor within the TonB2 complex | inference from domain architecture + essentiality of the orthologue |
| Biological process | Siderophore-dependent iron import / energy transduction for TonB-dependent outer-membrane transport | orthologue knockout phenotype (ISS-grade for VC_1548) |
| Cellular component | Periplasm, and/or plasma-membrane-associated TonB2 complex | SignalP signal peptide + no TM helix; complex membership of partners |

Because *all* direct evidence comes from the *V. vulnificus* orthologue and from TtpC (not TtpB) in *V. cholerae*, annotations on VC_1548 itself should carry sequence-similarity evidence rather than experimental codes. An "iron ion transmembrane transporter activity" assignment would be an over-annotation: TtpB2 energizes transport but is not the permease.

## 7. Open questions and suggested experiments

1. **Is VC_1548 required for TonB2-dependent transport in *V. cholerae*?** A clean ΔVC_1548 in a ΔtonB1 background, assayed for enterobactin, vibriobactin, ferrichrome and hemin utilization, would convert the current orthology inference into direct evidence.
2. **Where does it sit?** Fractionation of periplasm vs inner/outer membrane, plus protease accessibility in spheroplasts.
3. **What does it contact?** Co-purification or crosslinking against TonB2, ExbB2/ExbD2 and TtpC2 would explain the species-specific complementation failure; chimeric TtpB2 constructs between *V. cholerae* and *V. vulnificus* would map the specificity determinant, as was done for TtpC.
4. **Is it Fur-regulated?** Test the predicted upstream Fur box and confirm ttpB2 as the operon's first gene by RT-PCR across the gene junctions.
5. **Does it matter in vivo?** Infant-mouse competition, paralleling the Seliger et al. tonB1/tonB2 results.

## Caveats on evidence quality

- **No primary publication addresses VC_1548 directly.** The strongest claims rest on an orthologue in a different species.
- The Barnes et al. complementation data explicitly show that *V. cholerae* TtpB2 does **not** function in *V. vulnificus*. This confirms the genes are orthologous and co-regulated, but it also means the functional transfer is at the level of "plays the same role in its own system", not "interchangeable protein".
- The UniProt protein name is ProtNLM-generated (ECO:0008006) and is not independent evidence; UniProt protein existence is PE 4 (Predicted).
- I was not able to retrieve full text for the Kuehl & Crosa and Payne et al. reviews via Europe PMC; claims attributed to them above come from their abstracts, which I did retrieve.

## Sources

- [Barnes AD et al. (2020) Two novel proteins, TtpB2 and TtpD2, are essential for iron transport in the TonB2 system of *Vibrio vulnificus*. MicrobiologyOpen. PMID:31595707](https://pmc.ncbi.nlm.nih.gov/articles/PMC6957404)
- [Stork M et al. (2007) A novel protein, TtpC, is a required component of the TonB2 complex for specific iron transport in the pathogens *Vibrio anguillarum* and *Vibrio cholerae*. J Bacteriol. PMID:17189363](https://pmc.ncbi.nlm.nih.gov/articles/PMC1855762)
- [Kuehl CJ, Crosa JH (2009) Molecular and genetic characterization of the TonB2-cluster TtpC protein in pathogenic vibrios. Biometals. PMID:19130262](https://pmc.ncbi.nlm.nih.gov/articles/PMC3032568)
- [Kustusch RJ et al. (2012) The ttpC gene is contained in two of three TonB systems in *Vibrio vulnificus*. J Bacteriol. PMID:22505675](https://pmc.ncbi.nlm.nih.gov/articles/PMC3370854)
- [Kuehl CJ, Crosa JH (2010) The TonB energy transduction systems in *Vibrio* species. Future Microbiol. PMID:20860484](https://pmc.ncbi.nlm.nih.gov/articles/PMC3032567)
- [Payne SM, Mey AR, Wyckoff EE (2016) Vibrio iron transport: evolutionary adaptation to life in multiple environments. PMID:26658001](https://pmc.ncbi.nlm.nih.gov/articles/PMC4711184)
- [Seliger SS, Mey AR, Valle A-M, Payne SM (2001) The two TonB systems of *Vibrio cholerae*. Mol Microbiol 39:801–812](https://web.biosci.utexas.edu/paynelab/Abstracts/abstract37.html)
- [Braun V, Ratliff AC, Celia H, Buchanan SK (2023) Energization of outer membrane transport by the ExbB ExbD molecular motor. PMID:37219427](https://pmc.ncbi.nlm.nih.gov/articles/PMC10294619)
- [Heidelberg JF et al. (2000) DNA sequence of both chromosomes of the cholera pathogen *Vibrio cholerae*. Nature 406:477-483. PMID:10952301](https://pubmed.ncbi.nlm.nih.gov/10952301/)
- KEGG gene records vch:VC_1543–VC_1551 (https://rest.kegg.jp/get/vch:VC_1548); NCBI protein NP_231188, NP_231183, NP_231187; UniProt H9L4R2 (local record)

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC6957404
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC1855762
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC3032568
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC3370854
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC3032567
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC4711184
7. https://web.biosci.utexas.edu/paynelab/Abstracts/abstract37.html
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC10294619
9. https://pubmed.ncbi.nlm.nih.gov/10952301/
10. https://rest.kegg.jp/get/vch:VC_1548