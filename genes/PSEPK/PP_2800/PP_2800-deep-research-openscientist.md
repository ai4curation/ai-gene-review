---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T08:23:27.025293'
end_time: '2026-08-31T08:45:11.370098'
duration_seconds: 1304.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2800
  gene_symbol: PP_2800
  uniprot_accession: Q88J49
  protein_description: 'SubName: Full=Diaminobutyrate-2-oxoglutarate transaminase
    {ECO:0000313|EMBL:AAN68408.1};'
  gene_info: OrderedLocusNames=PP_2800 {ECO:0000313|EMBL:AAN68408.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-III pyridoxal-phosphate-dependent
  protein_domains: Aminotrans_3. (IPR005814); Aminotrans_3_PPA_site. (IPR049704);
    Dat. (IPR004637); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
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
  path: PP_2800-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_2800-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88J49
- **Protein Description:** SubName: Full=Diaminobutyrate-2-oxoglutarate transaminase {ECO:0000313|EMBL:AAN68408.1};
- **Gene Information:** OrderedLocusNames=PP_2800 {ECO:0000313|EMBL:AAN68408.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-III pyridoxal-phosphate-dependent
- **Key Domains:** Aminotrans_3. (IPR005814); Aminotrans_3_PPA_site. (IPR049704); Dat. (IPR004637); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2800" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2800' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2800** (gene ID: PP_2800, UniProt: Q88J49) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_2800 (UniProt Q88J49)

**Organism:** *Pseudomonas putida* KT2440 (strain ATCC 47054 / DSM 6125 / NCIMB 11950)
**Locus:** PP_2800 · **Gene product:** Diaminobutyrate–2-oxoglutarate transaminase (putative)
**Protein:** 417 aa, ~45.25 kDa · **UniProt:** Q88J49 (unreviewed, TrEMBL) · **RefSeq:** WP_010953709.1
**EC / KO:** EC 2.6.1.76 / KEGG K00836

---

## 1. Summary (answer to the research question)

PP_2800 encodes a **soluble, cytoplasmic, pyridoxal-5′-phosphate (PLP)-dependent class-III (ω-)aminotransferase of the DAT/EctB family** (diaminobutyrate–2-oxoglutarate transaminase, EC 2.6.1.76). Enzymes of this family catalyze the **reversible transfer of an amino group between the distal (ω) position of a C4 amino-acid semialdehyde and 2-oxoglutarate/glutamate**, interconverting **L-aspartate-β-semialdehyde + L-glutamate ⇌ L-2,4-diaminobutyrate (DABA) + 2-oxoglutarate**. This assignment is based on **sequence homology and conserved-domain signatures only** — there is no direct experimental characterization of the PP_2800 protein. Importantly, although the DAT/EctB reaction is the canonical first, rate-limiting step of **ectoine** biosynthesis, *P. putida* KT2440 **lacks the downstream ectoine genes (ectA, ectC, ectD)** and therefore cannot make ectoine. The genome encodes **two K00836 paralogs (PP_2800 and PP_4223, ~51 % identical) that are functionally partitioned**: **PP_4223** lies inside the pyoverdine (ferribactin-synthase) NRPS cluster and is the parsimonious supplier of L-2,4-diaminobutyrate (L-Dab) for the pyoverdine siderophore, whereas **PP_2800** sits in a separate GABA/diamine metabolism cluster. Thus the physiological role of PP_2800 is best interpreted as **cytoplasmic metabolism/interconversion of C4 amino compounds (aspartate-β-semialdehyde/DABA-, and possibly GABA-type ω-amino substrates)**, rather than siderophore or compatible-solute synthesis.

## 2. Molecular identity and evidence

**Domain/family evidence (bioinformatic).** UniProt and InterPro assign PP_2800 to:
- Pfam **PF00202 Aminotran_3** (class-III aminotransferase); PROSITE **PS00600** (class-III PLP AA-transferase active-site motif).
- TIGRFAM **TIGR00709 "dat"** and NCBIfam **NF006733 / PRK09264**, both specific to 2,4-diaminobutyrate:2-oxoglutarate 4-aminotransferases.
- PANTHER **PTHR43552:SF2 "diaminobutyrate–2-oxoglutarate transaminase."**
- InterPro: IPR004637 (Dat), IPR005814/IPR049704 (Aminotrans_3), IPR015421/15424 (PLP-dependent transferase, major/fold).
- eggNOG **COG0160** (4-aminobutyrate aminotransferase and related aminotransferases).
- Cofactor: **pyridoxal-5′-phosphate** (GO:0030170, PLP binding).

Confidence level in UniProt is **PE 3 "Inferred from homology"** — i.e., predicted, not experimentally verified for this protein.

**The catalyzed reaction (from characterized family members).** The founding biochemical study of the *Acinetobacter baumannii* Dat enzyme purified the protein and demonstrated the reversible reaction *"L-2,4-diaminobutyric acid + 2-ketoglutaric acid ⇌ L-glutamic acid + L-aspartic beta-semialdehyde"* (Ikai & Yamamoto, 1997, PMID 9260954). Recent structural/biochemical work on EctB confirms the physiological direction *"converts aspartate-β-semialdehyde (ASA) to DABA"* and that this is *"the rate-limiting step of ectoine biosynthesis"* (Skogvold et al., 2026, PMID 41652856).

**Substrate specificity.** DABA aminotransferases are **ω-transaminases that aminate the distal ω-position** of their substrate. Structural work on *Chromohalobacter salexigens* EctB provided *"the first description of two binding pockets in the active site that may account for the catalytic character of DABA aminotransferases"* (Hillier et al., 2020, PMID 32112674), explaining the characteristic **dual-substrate specificity** (one pocket for the amino donor/glutamate, one for the C4 amino-acceptor). Consistent with broad specificity, the *Marinobacter* EctB showed *"activity was highest using DABA and GABA as substrates"* (PMID 41652856). Such promiscuity means the exact in-vivo substrate of PP_2800 cannot be fixed from homology alone.

## 3. Cellular localization

PP_2800 is predicted to be a **cytoplasmic (cytosolic) soluble enzyme**. This is inferred from: (i) it is a PLP-dependent central-metabolism aminotransferase, a class that is universally cytosolic; (ii) the sequence begins `MNKIETFERL…` with **no Sec/Tat signal peptide and no transmembrane segment**; and (iii) characterized homologs (EctB, Dat) are soluble oligomeric proteins purified from the cytosol. Family members assemble as **homotetramers built from two functional dimers**, with a "gating loop" from the neighboring monomer helping to shape each active site (PMID 32112674).

## 4. Pathway context and the KT2440-specific interpretation

**Canonical pathway (in ectoine producers).** DABA aminotransferase (EctB) performs the first committed step of ectoine biosynthesis: ASA → DABA; DABA is then N-acetylated by **EctA** and cyclized by **EctC (ectoine synthase)** to ectoine, optionally hydroxylated by **EctD** to 5-hydroxyectoine (PMID 32112674; PMID 38960226). The same Dat reaction also feeds, together with a DABA **decarboxylase (Ddc)**, the **1,3-diaminopropane** pathway in *Acinetobacter* and *Haemophilus* (PMID 9260954; PMID 9514614), and can participate in promiscuous routes such as a *"β-alanine biosynthetic pathway consisting of promiscuous metabolic enzymes … including 2,4-diaminobutyrate aminotransferase (Dat) and 2,4-diaminobutyrate decarboxylase (Ddc)"* (Perchat et al., 2022, PMID 35623386).

**Why the canonical roles do not apply directly to KT2440.** A KEGG genome-wide orthology check shows *P. putida* KT2440 encodes the DABA-aminotransferase ortholog K00836 **as two paralogs (PP_2800 and PP_4223)** but has **no ectA (K06718), no ectC (K06720), and no ectD (K10674)**. The ectoine pathway is therefore **genetically incomplete**, and PP_2800 cannot support ectoine synthesis. No DABA decarboxylase (ddc) is present adjacent to PP_2800 either, arguing against a dedicated 1,3-diaminopropane operon at this locus.

**Genomic-neighborhood evidence.** PP_2800 sits (complement strand, ~3.190–3.192 Mb) within a tight cluster of **C4-amino/ω-amino-compound metabolism** genes:

| Locus | Product | KO / EC |
|-------|---------|---------|
| PP_2799 | 4-aminobutyrate(GABA)–pyruvate transaminase (class III) | K16871 / 2.6.1.96 |
| **PP_2800** | **DABA–2-oxoglutarate transaminase** | **K00836 / 2.6.1.76** |
| PP_2801 | 4-aminobutyraldehyde dehydrogenase | K00137 / 1.2.1.19 |
| PP_2802 | amino-acid permease | – |
| PP_2806 | TetR-family transcriptional regulator | – |

The co-occurrence of a **GABA aminotransferase**, an **aminobutyraldehyde dehydrogenase** (an enzyme of putrescine/polyamine→GABA catabolism), an **amino-acid permease** and a local **TetR regulator** indicates a locus dedicated to **uptake and catabolic interconversion of 4-carbon amino compounds** (GABA/polyamine-derived intermediates). Given the broad ω-transaminase specificity of the family, the most defensible interpretation is that PP_2800 supplies **transamination of aspartate-β-semialdehyde/DABA (and possibly related ω-amino substrates such as GABA)** feeding cytoplasmic amino-acid/polyamine metabolism, rather than a compatible-solute pathway.

### 4a. The two paralogs are functionally partitioned: PP_4223 (not PP_2800) is the pyoverdine-siderophore enzyme

*P. putida* KT2440 carries **two K00836 DABA-aminotransferase paralogs, PP_2800 and PP_4223**, which share **50.9 % amino-acid identity** (global alignment, 201/395 aligned positions) and both retain the conserved class-III catalytic-lysine motif (PP_2800 `…ICDEIQAGCGRTGD…TCAK…`; PP_4223 `…IVDEIQSGFARTGR…TLSK…`). Crucially, their **genomic contexts differ completely**:

- **PP_4223** is embedded **within the pyoverdine (ferribactin) biosynthetic locus** — flanked by PP_4219–PP_4221, the **non-ribosomal peptide synthetase (NRPS) subunits of ferribactin synthase** (ferribactin is the pyoverdine precursor), and PP_4222 (SyrP-like). **L-2,4-diaminobutyrate (L-Dab) is a documented pyoverdine building block**: the fluorophore is generated *"by periplasmic oxidation and cyclization reactions of d-tyrosine and l-diaminobutyric acid"* (Ringel et al., 2018, PMID 29208656), and the *P. putida* pyoverdine peptide contains an L-Dab residue arising *"from the condensation of 2,4-diaminobutyric acid and glutamine"* (Gwose & Taraz, 1992, PMID 1388514). PP_4223 is therefore the parsimonious source of L-Dab for pyoverdine and the physiological basis of the KEGG "biosynthesis of various siderophores" (ppu00975) mapping of the K00836 orthology.
- **PP_2800**, by contrast, lies **outside any NRPS/siderophore locus**, within the GABA/diamine metabolism cluster described above.

This partition means the siderophore role attributed to the orthology should be assigned primarily to **PP_4223**, whereas **PP_2800 most likely serves general cytoplasmic amino-acid/diamine (C4 ω-amino) metabolism**. The two enzymes may retain overlapping DABA-transaminase activity (potential partial redundancy), but their distinct genomic niches argue for distinct primary roles.

**Orthology test (decisive).** *P. aeruginosa* PAO1 carries a **single** K00836 gene, **PA2413 = PvdH** ("diaminobutyrate--2-oxoglutarate aminotransferase"), located within its pyoverdine locus and experimentally required to supply L-Dab for pyoverdine. Global pairwise identity shows **PP_4223 is 85.7 % identical to PvdH** (382/446), i.e. its clear ortholog, while **PP_2800 is only 54.4 % identical to PvdH** (211/388). This confirms with high confidence that **the pyoverdine DABA-transaminase function in *P. putida* is carried by PP_4223 (the PvdH ortholog), and PP_2800 is a lineage-specific duplication** whose primary role lies outside siderophore biosynthesis, consistent with its GABA/diamine-cluster context.

## 5. Supported and refuted hypotheses

- **Supported:** PP_2800 is a PLP-dependent class-III DABA-type ω-aminotransferase (EC 2.6.1.76) — strong, converging domain/orthology evidence.
- **Supported:** The protein is cytoplasmic and soluble (no signal peptide/TM; family biochemistry).
- **Refuted (for KT2440):** PP_2800 acts as the EctB step of an ectoine biosynthetic pathway — refuted because ectA/ectC/ectD are absent from the genome.
- **Not supported by local context:** A dedicated 1,3-diaminopropane (dat–ddc) operon at this locus — no adjacent ddc.
- **Reassigned:** The siderophore/pyoverdine role of the K00836 orthology belongs primarily to the paralog **PP_4223** (embedded in the ferribactin-synthase NRPS cluster), not PP_2800.
- **Best current inference:** PP_2800 performs cytoplasmic transamination of C4 amino-semialdehydes (ASA/DABA, and possibly GABA) within an amino-acid/polyamine catabolic/interconversion cluster.

## 6. Limitations and future directions

- **No direct experimental data exist for PP_2800**; all functional statements are homology/context inferences (UniProt PE3; GO terms IEA only).
- Class-III ω-transaminases are **catalytically promiscuous**, so the exact preferred substrate and metabolic direction in vivo remain undetermined.
- The KT2440 genome carries a **paralog, PP_4223 (also K00836, 50.9 % identical)** that is the **PvdH ortholog (85.7 % identical to *P. aeruginosa* PvdH/PA2413)** and supplies pyoverdine L-Dab; whether the two paralogs are functionally redundant under any condition remains to be tested directly.
- **Recommended experiments:** (i) recombinant expression and steady-state kinetics against ASA, DABA, GABA and putrescine-derived aldehydes; (ii) transcriptional/operon mapping and regulation by the local TetR regulator (PP_2806); (iii) metabolomics of a ΔPP_2800 mutant to detect DABA/GABA/1,3-diaminopropane changes; (iv) an AlphaFold model (available: AlphaFoldDB Q88J49) to confirm the two-pocket active-site architecture and predicted PLP-Lys Schiff-base residue.

---

### Key references
- Ikai & Yamamoto, 1997, *J Bacteriol* — PMID **9260954** (Dat reaction, EC 2.6.1.76).
- Ikai & Yamamoto, 1998, *J Bacteriol* — PMID **9514614** (dat/ddc, 1,3-diaminopropane).
- Hillier, Altermark & Leiros, 2020, — PMID **32112674** (EctB crystal structure, tetramer, dual active-site pockets).
- Skogvold et al., 2026 — PMID **41652856** (EctB biochemistry; DABA/GABA substrate range).
- Su et al., 2024 — PMID **38960226** (EctB as rate-limiting step; ectABC).
- Perchat et al., 2022 — PMID **35623386** (Dat promiscuity in alternative pathways).
- Ringel, Dräger & Brüser, 2018 — PMID **29208656** (pyoverdine fluorophore formed from D-Tyr + L-Dab; PvdH-type DABA-AT supplies L-Dab).
- Gwose & Taraz, 1992 — PMID **1388514** (*P. putida* pyoverdine structure contains L-Dab).
- Nelson et al., 2002, *Environ Microbiol* — PMID **12534463** (KT2440 genome).


## Artifacts

- [OpenScientist final report](PP_2800-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_2800-deep-research-openscientist_artifacts/final_report.pdf)