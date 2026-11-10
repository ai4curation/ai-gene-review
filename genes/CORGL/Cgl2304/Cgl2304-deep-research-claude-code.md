---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T23:28:32.982449'
end_time: '2026-10-30T23:33:45.760324'
duration_seconds: 312.78
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: CORGL
  gene_id: Q8NNA0
  gene_symbol: Cgl2304
  uniprot_accession: Q8NNA0
  protein_description: 'SubName: Full=Uncharacterized protein, probably involved in
    trehalose biosynthesis {ECO:0000313|EMBL:BAB99697.1};'
  gene_info: OrderedLocusNames=Cgl2304 {ECO:0000313|EMBL:BAB99697.1};
  organism_full: Corynebacterium glutamicum (strain ATCC 13032 / DSM 20300 / JCM 1318
    / BCRC 11384 / CCUG 27702 / LMG 3730 / NBRC 12168 / NCIMB 10025 / NRRL B-2784
    / 534).
  protein_family: Not specified in UniProt
  protein_domains: Kinase-like_dom_sf. (IPR011009)
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
  web_search_requests: 6
  num_turns: 22
  total_cost_usd: 1.2534052
  session_id: 6758d937-5b9c-48e4-9bfd-ae0949f797af
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 10
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q8NNA0
- **Protein Description:** SubName: Full=Uncharacterized protein, probably involved in trehalose biosynthesis {ECO:0000313|EMBL:BAB99697.1};
- **Gene Information:** OrderedLocusNames=Cgl2304 {ECO:0000313|EMBL:BAB99697.1};
- **Organism (full):** Corynebacterium glutamicum (strain ATCC 13032 / DSM 20300 / JCM 1318 / BCRC 11384 / CCUG 27702 / LMG 3730 / NBRC 12168 / NCIMB 10025 / NRRL B-2784 / 534).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Kinase-like_dom_sf. (IPR011009)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Cgl2304" matches the protein description above**
2. **Verify the organism is correct:** Corynebacterium glutamicum (strain ATCC 13032 / DSM 20300 / JCM 1318 / BCRC 11384 / CCUG 27702 / LMG 3730 / NBRC 12168 / NCIMB 10025 / NRRL B-2784 / 534).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Cgl2304' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Cgl2304** (gene ID: Q8NNA0, UniProt: Q8NNA0) in CORGL.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

I'm comparing Cgl2304 with the characterized mycobacterial maltokinase (Mak, O07177) to see whether the family assignment holds.

Cgl2304 sits right after treS (Cgl2303), sharing a 4-nt overlap with it, and is about 44% identical to Mtb Mak. Next I'm checking the literature on the Mak reaction and on GlgE in C. glutamicum.

The Henrich thesis says a "TreX" makes maltose-1-phosphate in C. glutamicum. I'm checking whether that "TreX" is actually this gene.

# Cgl2304 (Q8NNA0) of *Corynebacterium glutamicum* ATCC 13032 is a predicted maltokinase (Mak/Pep2, EC 2.7.1.175) in the TreS–Mak–GlgE α-glucan pathway

## 1. Identity check

| Item | Value | Source |
|---|---|---|
| UniProt | Q8NNA0 (secondary Q6M3E0), unreviewed TrEMBL entry, 363 aa, 39.9 kDa, PE 4 ("Predicted") | local `Cgl2304-uniprot.txt` |
| Locus tags | Cgl2304 (BA000036, Kalinowski/Ikeda genome) = **cg2530** (the BX927147 locus tag) | UniProt DR STRING/KEGG lines `196627.cg2530`, `cgl:Cgl2304` |
| Name in UniProt | "Uncharacterized protein, probably involved in trehalose biosynthesis" (submitter name, ECO:0000313) | UniProt |
| Orthology group | eggNOG **COG3281** | UniProt DR eggNOG |
| Domains | Protein kinase-like superfamily IPR011009 / SSF56112 (residues 97–362); CATH 3.90.1200.10 (157–363). No Pfam Mak_N_cap (PF18085) match | UniProt; InterPro API (queried 2026-10-30) |
| Existing GO annotations | **None.** The GOA file has no data rows | local `Cgl2304-goa.tsv` |

**The identity checks pass.** The literature found refers to this exact locus (cg2530) in *C. glutamicum* ATCC 13032. No literature on a different gene with the same symbol turned up. Note that the one primary *C. glutamicum* study calls this gene "**treX**". That is a local name only. It must not be confused with the unrelated glycogen debranching enzyme TreX (GH13) found in other bacteria.

## 2. Summary

Cgl2304/cg2530 is very probably the *C. glutamicum* **maltokinase** (Mak, also called Pep2). It would catalyze:

> D-maltose + ATP → α-maltose 1-phosphate + ADP + H⁺ (EC 2.7.1.175; RHEA:31915)

This is the second step of the four-enzyme **TreS–Mak–GlgE–GlgB pathway**, which turns trehalose (or maltose) into branched α-glucan (glycogen-like polymer):

1. TreS converts trehalose to maltose.
2. Mak phosphorylates maltose to maltose-1-phosphate (M1P).
3. GlgE adds the maltosyl unit from M1P onto α-1,4-glucan chains.
4. GlgB adds the branches.

The assignment rests on four independent lines of evidence:

1. **Homology.** Cgl2304 is ~42–44% identical over ~270 aligned residues to characterized mycobacterial maltokinases, and it keeps their kinase catalytic motifs.
2. **Gene neighbourhood.** The gene sits directly downstream of, and overlaps, *treS* (Cgl2303/cg2529). This mirrors the conserved *treS–mak* arrangement in mycobacteria.
3. **Pathway completeness.** The genome encodes a GlgE (Cgl1225/cg1382) next to GlgB (Cgl1224/cg1381).
4. **Genetics.** Insertional inactivation of cg2530 in a Δ*malQ* background abolished the residual trehalose/maltose utilization that remains when the MalQ route is gone (Henrich thesis, 2011).

**No direct biochemical assay of the *C. glutamicum* protein has been published.** The enzymatic activity is therefore an inference from homology, not an experimental result for this protein. Like its relatives, Cgl2304 is a soluble cytoplasmic enzyme, with no signal peptide or transmembrane segments annotated.

## 3. Molecular function (inferred)

### 3.1 The maltokinase reaction and what is known from orthologs

- **First described in actinomycetes.** Maltokinase was first named for an enzyme from *Actinoplanes missouriensis* that makes maltose-1-phosphate from maltose and ATP. Homologs in *Streptomyces coelicolor* and *M. tuberculosis* (Pep2/Rv0127) were recognised later (reviewed in Fraga et al. 2015, *Sci Rep* 5:8026, PMID:25619172, https://pubmed.ncbi.nlm.nih.gov/25619172/).
- ***M. bovis* BCG / *M. tuberculosis* Mak (O07177, Rv0127; Mendes et al. 2010, *BMC Biochem* 11:21, PMID:20507595, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2885305/):**
  - activity depends on maltose and ATP;
  - GTP and UTP can also serve as phosphate donor, but ATP is preferred;
  - Mg²⁺ is needed for maximal activity;
  - the product was confirmed as maltose-1-phosphate by TLC and NMR;
  - Km(maltose) ≈ 2.52 ± 0.40 mM and Km(ATP) ≈ 0.74 ± 0.12 mM.
- **UniProt's curated O07177 entry:** "Catalyzes the ATP-dependent phosphorylation of maltose to maltose 1-phosphate… involved in a branched alpha-glucan biosynthetic pathway from trehalose, together with TreS, GlgE and GlgB." It places Mak in the aminoglycoside phosphotransferase family.
- **Structure (Fraga et al. 2015, PMID:25619172):** *M. vanbaalenii* Mak (1.15–1.71 Å, including an ATP-analogue complex) has an eukaryotic-like kinase (ELK) fold. That fold resembles aminoglycoside phosphotransferases and methylthioribose kinases. A distinctive N-terminal "cap" domain resembles the cystatin fold. Structural constraints mean only α-maltose is phosphorylated.
- **TreS–Pep2 complex (Roy et al. 2013, *ACS Chem Biol*, PMID:23901909):** in mycobacteria, TreS and Pep2 form a hetero-octameric complex. Complex formation strongly increases Pep2's maltokinase activity, possibly by channelling substrate.

### 3.2 Sequence evidence specific to Cgl2304 (my own analysis)

I ran local Smith–Waterman alignments (BLOSUM62, gap −11/−1; Biopython; UniProt sequences retrieved 2026-10-30):

| Comparison | Aligned region (Cgl2304) | Identity |
|---|---|---|
| Cgl2304 vs *M. tuberculosis* Mak O07177 (455 aa) | 89–361 ↔ Mtb 141–452 | 118/268 = **44.0%** |
| Cgl2304 vs *M. vanbaalenii* Mak A1TH50 (441 aa, structure organism) | 89–362 ↔ 133–440 | 114/271 = **42.1%** |

The Henrich thesis independently reports 37% identity to *pep2* (rv0127) with an e-value of 3e-50.

**Conserved catalytic motifs.** Cgl2304 contains the Brenner-type catalytic loop **HGDLHLGQ** at residues 246–253. It is identical to Mtb Mak 320–327; the Asp is the predicted catalytic base. It also has the Mg²⁺-binding **IDFEG** ("DFG-like") motif at 264–268, which matches Mtb 338–342. Both motifs sit at the same relative positions in the two proteins, offset by 74 residues. This supports a catalytically competent kinase rather than a pseudokinase.

**Shorter, divergent N-terminus.** Cgl2304 is ~90 residues shorter than the mycobacterial enzymes. Its first ~88 residues do not align with the Mtb Mak N-terminal cap (~residues 1–140), and InterPro finds no Mak_N_cap (PF18085) signature. The genome does encode a separate 213-aa "Maltokinase N-terminal cap domain-containing protein" (Cgl0153, Q8NTZ8, also COG3281), but it showed no significant local alignment to Mtb Mak.

**The gene model is probably not truncated.** The Cgl2304 CDS (BA000036.3:2439907..2440998) overlaps the end of the *treS* CDS (2438114..2439910) by 4 nt, a typical ATGA translational-coupling overlap. An upstream extension would run into *treS*. The short N-terminus therefore looks like genuine divergence of the cap region. Sequence identity between Maks from different taxa can be as low as ~10% (Fraga et al. 2015). Whether this divergence affects activity or the interaction with TreS is unknown.

## 4. Biological process and pathway context in *C. glutamicum*

### 4.1 Genes for the pathway are present

From UniProt organism queries (taxon 196627):

| Step | Enzyme | *C. glutamicum* gene |
|---|---|---|
| Trehalose ⇄ maltose | TreS, maltose α-D-glucosyltransferase, EC 5.4.99.16 | Cgl2303 / cg2529 (Q8NNA1), immediately upstream of Cgl2304 |
| Maltose + ATP → M1P | Mak/Pep2, EC 2.7.1.175 | **Cgl2304 / cg2530 (this gene)** |
| M1P + α-glucanₙ → α-glucanₙ₊₂ | GlgE, EC 2.4.99.16 | Cgl1225 / cg1382 (Q8NR39) |
| Branching | GlgB, EC 2.4.1.18 | Cgl1224 / cg1381 (Q8NR40) |
| (Classical route) ADP-glucose synthesis | GlgC | Cgl1118 / cg1269 (Q8NRD4) |

In *M. tuberculosis*, Kalscheuer et al. (2010, *Nat Chem Biol* 6:376, PMID:20305657) defined this pathway: TreS → Pep2 → GlgE → GlgB. They showed that blocking GlgE makes maltose-1-phosphate build up to toxic levels ("self-poisoning"). This made Pep2/Mak and GlgE candidate drug targets. Deleting *treS* or *pep2* in *M. smegmatis* stopped M1P from accumulating in a Δ*glgE* background.

### 4.2 Direct genetic evidence in *C. glutamicum* (Henrich 2011 thesis, Univ. Köln)

Source: A. W. Henrich, Dissertation, Universität zu Köln, February 2011, https://kups.ub.uni-koeln.de/4163/ (section 3.3.3, "TreX: A new player in trehalose/maltose metabolism", and Discussion 4.7).

1. **Gene identification.** The authors found "the gene *treX* (cg2530) downstream adjacent to the *treS* gene (cg2529)". They noted its homology to *pep2* (rv0127), which also lies downstream of *treS* (rv0126) in *M. tuberculosis*.
2. **A second pathway exists.** A Δ*malQ* strain (MalQ is the amylomaltase of the main maltose route) could still use maltose in mixed-substrate cultures.
3. **Polar effect of the *treS* deletion.** Δ*malQ* Δ*treS* could not use maltose, and plasmid-borne *treS* did not restore this, although the same plasmid complements Δ*treS* alone. The authors concluded that deleting *treS* also inactivated the downstream cg2530, consistent with co-transcription and translational coupling.
4. **Inactivating cg2530 removes the second pathway.**
   - Insertional inactivation of cg2530 in wild type had no effect on growth on glucose plus trehalose. Wild type, Δ*malQ* and the cg2530 mutant all reached OD₆₀₀ ≈ 33 at μ ≈ 0.40 h⁻¹.
   - In contrast, "C. glutamicum ΔmalQ IM treX did not seem to be able to utilize trehalose for growth". The double mutant also failed to use maltose.
   - The authors concluded that "a second pathway for the utilization of trehalose/maltose is present in C. glutamicum", channelling "maltose into metabolism via maltose-1-phosphate and α-glucan".

**Caveats on this evidence:**
- It is a doctoral thesis, not a peer-reviewed article.
- The defect only shows when the MalQ route is also missing, so the evidence is genetic (necessity), not biochemical.
- No M1P or α-glucan was measured in the mutants.
- The thesis also describes an unexpected trehalose-related phenotype when *treS* was overexpressed in the Δ*malQ* cg2530 mutant, suggesting further unresolved roles in the TreS/cg2530 system.

The thesis therefore supports Cgl2304's role in a MalQ-independent route for trehalose and maltose utilization. That route is compatible with the TreS–Mak–GlgE pathway, but it is not a direct demonstration of maltokinase activity.

### 4.3 Where this fits in *C. glutamicum* trehalose and glycogen physiology

- *C. glutamicum* has three trehalose routes: OtsA/OtsB, TreY/TreZ and TreS. TreY/TreZ dominates synthesis and OtsAB plays a minor role. Because cytoplasmic trehalose far exceeds maltose, TreS is expected to work mainly in the **degradative** direction (trehalose → maltose) in vivo. Δ*treS* strains accumulate more trehalose (Wolf et al. 2003; Tzvetkov et al. 2003; Padilla et al. 2004; summarised in Tournu et al. 2013 review, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3744402/).
- **Cgl2304 is the step that commits TreS-derived maltose to α-glucan via M1P.** In *C. glutamicum*, the pathway is therefore best seen as a trehalose-recycling and carbon-storage route into glycogen/α-glucan. It runs alongside the classical GlgC/GlgA (ADP-glucose) pathway.
- **A caution on older data.** The *treS* deletion strains used in earlier trehalose-accumulation studies probably also had polar effects on cg2530 (Henrich 2011). Phenotypes attributed to *treS* loss may partly reflect loss of Mak.
- **Biotechnology.** *C. glutamicum* TreS (cg2529) has been cloned and characterized for trehalose production from maltose (Korea University reports, https://scholar.korea.ac.kr/handle/2021.sw.korea/116669). Cgl2304 was not studied there.

## 5. Cellular location

No experimental localization data exist for Cgl2304. Inference:
- Neither UniProt nor InterPro annotates a signal peptide or TM segment.
- Its substrates (maltose, ATP) and partner enzymes (TreS, GlgE, GlgB) are cytoplasmic.
- Mycobacterial Mak is soluble and forms a soluble complex with TreS (PMID:23901909).

**Predicted location: cytoplasm (cytosol).** In mycobacteria the same pathway also supplies capsular α-glucan, which ends up outside the cell. That product's final location is not a location of the kinase itself.

## 6. Suggested GO annotations (computational / IC level)

| Aspect | Term | Basis | Confidence |
|---|---|---|---|
| MF | maltokinase activity (EC 2.7.1.175; check the current GO id with OLS/QuickGO) | ~44% identity to experimentally characterized Mak with conserved HGDxHxxQ and DFE motifs; *treS*-adjacent synteny | Moderate–high (ISS/IBA-type) |
| BP | glycogen (α-glucan) biosynthetic process via the TreS–Mak–GlgE route; trehalose catabolism/utilization | complete pathway gene set present; genetic data in Δ*malQ* background (thesis) | Moderate |
| CC | cytoplasm / cytosol | no export or TM signals; soluble orthologs | Moderate (IC) |

Not recommended: generic "protein kinase activity" or protein-serine/threonine kinase terms. The ELK fold is shared with small-molecule kinases (APH and MTR kinases), and the substrate here is a sugar, not a protein.

## 7. Open questions and suggested experiments

1. **Biochemistry.** Express recombinant Cgl2304 and test ATP/Mg²⁺-dependent phosphorylation of maltose, confirming the product as α-M1P by NMR or HPAEC. Measure Km/kcat and test nucleotide and sugar specificity.
2. **The N-terminal cap question.** Does the shorter, divergent N-terminus change activity, oligomeric state, or binding to TreS (Cgl2303)? Test for a TreS–Mak complex by co-purification or SEC-MALS, and check whether TreS speeds up Cgl2304 activity as it does for mycobacterial Pep2.
3. **Clean genetics.** Make an in-frame Δcg2530 and a non-polar Δ*treS*. Measure M1P and glycogen levels, alone and combined with Δ*glgE* (which should accumulate M1P) and Δ*glgC* (to separate the two glycogen routes).
4. **Physiology.** Does the pathway matter for trehalose recycling, cell-envelope glycan, or stress tolerance in *C. glutamicum*?
5. **Cgl0153.** What does this separate COG3281 "Mak N-cap" protein do? Is it a fragment of a second Mak-like gene?

## 8. References

1. Ikeda M, Nakagawa S. The *Corynebacterium glutamicum* genome: features and impacts on biotechnological processes. *Appl Microbiol Biotechnol* 62:99–109 (2003). PMID:12743753. https://doi.org/10.1007/s00253-003-1328-1 (genome source of the Cgl2304 entry).
2. Kalscheuer R, et al. Self-poisoning of *Mycobacterium tuberculosis* by targeting GlgE in an α-glucan pathway. *Nat Chem Biol* 6:376–384 (May 2010). PMID:20305657.
3. Mendes V, Maranha A, Lamosa P, da Costa MS, Empadinhas N. Biochemical characterization of the maltokinase from *Mycobacterium bovis* BCG. *BMC Biochem* 11:21 (27 May 2010). PMID:20507595. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2885305/
4. Roy R, et al. Synthesis of α-glucan in mycobacteria involves a hetero-octameric complex of trehalose synthase TreS and maltokinase Pep2. *ACS Chem Biol* 8:2245–2255 (18 Oct 2013). PMID:23901909. https://pubmed.ncbi.nlm.nih.gov/23901909
5. Fraga J, et al. Structure of mycobacterial maltokinase, the missing link in the essential GlgE-pathway. *Sci Rep* 5:8026 (26 Jan 2015). PMID:25619172. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4306142/
6. Henrich AW. Dissertation, Universität zu Köln (Feb 2011): sections 3.3.3 and 4.7 on cg2530 ("treX"). https://kups.ub.uni-koeln.de/4163/ ; PDF: https://kups.ub.uni-koeln.de/4163/1/Dissertation_Alexander_Henrich.pdf
7. Tournu H, Fiori A, Van Dijck P. Relevance of trehalose in pathogenicity: some general rules, yet many exceptions. *PLoS Pathog* (2013). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3744402/ (context on *C. glutamicum* trehalose routes).
8. Trehalose synthase from *C. glutamicum* ATCC 13032 (cg2529), Korea University reports. https://scholar.korea.ac.kr/handle/2021.sw.korea/116669
9. UniProtKB Q8NNA0 (Cgl2304), O07177 (Mtb Mak), A1TH50 (*M. vanbaalenii* Mak), Q8NNA1 (TreS, Cgl2303), Q8NR39 (GlgE, Cgl1225), Q8NR40 (GlgB), Q8NTZ8 (Cgl0153); InterPro API record for Q8NNA0; ENA CDS records BAB99697/BAB99696. All accessed 2026-10-30.
10. Rhea RHEA:31915 (D-maltose + ATP = α-maltose 1-phosphate + ADP + H⁺). https://www.rhea-db.org/rhea/31915

**Provenance of my own analyses.** The alignments, motif positions and CDS overlap above were computed in this session in a temporary directory, `/tmp/cgl2304`; they are not saved in the repository. To cite them in a review, re-run them reproducibly in `genes/CORGL/Cgl2304/Cgl2304-bioinformatics/`.

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/25619172/
2. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2885305/
3. https://kups.ub.uni-koeln.de/4163/
4. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3744402/
5. https://scholar.korea.ac.kr/handle/2021.sw.korea/116669
6. https://doi.org/10.1007/s00253-003-1328-1
7. https://pubmed.ncbi.nlm.nih.gov/23901909
8. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4306142/
9. https://kups.ub.uni-koeln.de/4163/1/Dissertation_Alexander_Henrich.pdf
10. https://www.rhea-db.org/rhea/31915