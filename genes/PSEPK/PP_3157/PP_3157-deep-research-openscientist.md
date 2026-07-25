---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T04:09:57.418163'
end_time: '2026-07-17T04:48:08.327747'
duration_seconds: 2290.91
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_3157
  gene_symbol: PP_3157
  uniprot_accession: Q88I44
  protein_description: 'RecName: Full=Histidinol-phosphatase {ECO:0000256|ARBA:ARBA00013085,
    ECO:0000256|NCBIfam:TIGR02067}; EC=3.1.3.15 {ECO:0000256|ARBA:ARBA00013085, ECO:0000256|NCBIfam:TIGR02067};'
  gene_info: OrderedLocusNames=PP_3157 {ECO:0000313|EMBL:AAN68765.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the inositol monophosphatase superfamily.
  protein_domains: His_9_proposed. (IPR011809); Inositol_monoP_metal-BS. (IPR020583);
    Inositol_monoP_superfamily. (IPR051090); Inositol_monophosphatase-like. (IPR000760);
    Inositol_P (PF00459)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_3157-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_3157-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I44
- **Protein Description:** RecName: Full=Histidinol-phosphatase {ECO:0000256|ARBA:ARBA00013085, ECO:0000256|NCBIfam:TIGR02067}; EC=3.1.3.15 {ECO:0000256|ARBA:ARBA00013085, ECO:0000256|NCBIfam:TIGR02067};
- **Gene Information:** OrderedLocusNames=PP_3157 {ECO:0000313|EMBL:AAN68765.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the inositol monophosphatase superfamily.
- **Key Domains:** His_9_proposed. (IPR011809); Inositol_monoP_metal-BS. (IPR020583); Inositol_monoP_superfamily. (IPR051090); Inositol_monophosphatase-like. (IPR000760); Inositol_P (PF00459)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_3157" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_3157' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_3157** (gene ID: PP_3157, UniProt: Q88I44) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_3157 / Q88I44 (Histidinol-phosphate phosphatase)

**Organism:** *Pseudomonas putida* KT2440 (strain ATCC 47054 / DSM 6125 / NCIMB 11950; taxid 160488)
**Gene / locus:** PP_3157 (OrderedLocusName; EMBL AAN68765.1)
**UniProt:** Q88I44 (Q88I44_PSEPK), 263 aa, monomer, protein existence level 3 (inferred from homology)
**EC:** 3.1.3.15 — histidinol-phosphatase

---

## 1. Identity Verification (mandatory check)

The requested target is PP_3157 / Q88I44 in *Pseudomonas putida* KT2440. All authoritative annotations are internally consistent and match the target:

- **Protein description** (UniProt): "Histidinol-phosphatase, EC 3.1.3.15."
- **Organism**: *Pseudomonas putida* KT2440 — confirmed (taxid 160488; KEGG `ppu:PP_3157`; STRING `160488.PP_3157`; BioCyc `PPUT160488:G1G01-3376-MONOMER`).
- **Family / domains**: Inositol monophosphatase superfamily — confirmed by InterPro IPR000760 (Inositol_monophosphatase-like), IPR011809 (His_9_proposed), IPR020583 (metal-binding site), IPR051090 (IMP superfamily), Pfam PF00459 (Inositol_P), and NCBIfam **TIGR02067**.

There is no gene-symbol ambiguity concern here: "PP_3157" is an unambiguous ordered-locus identifier unique to the *P. putida* KT2440 genome. The functional annotation below is supported by strong homology and by direct experimental/structural characterization of close orthologs; the specific PP_3157 protein has not itself been enzymatically assayed (annotation is inferred from homology, PE3).

---

## 2. Summary Answer

PP_3157 encodes a **histidinol-phosphate phosphatase (HolPase, EC 3.1.3.15)** of the **inositol-monophosphatase (IMPase)–like "HisN" family** — the third, evolutionarily independent HolPase family (distinct from the HAD-type HisB of *E. coli* and the PHP-type of *Bacillus*). Acting in the **cytoplasm** as a soluble, **Mg²⁺-dependent** phosphomonoesterase, it catalyzes the **penultimate step of L-histidine biosynthesis**: hydrolysis of L-histidinol-phosphate to L-histidinol + inorganic phosphate. The product L-histidinol is then oxidized by histidinol dehydrogenase (HisD) to L-histidine.

---

## 3. Primary Function: the reaction catalyzed

**Reaction (UniProt catalytic activity):**
> L-histidinol phosphate + H₂O → L-histidinol + phosphate (EC 3.1.3.15)

**Pathway position (UniProt):** *Amino-acid biosynthesis; L-histidine biosynthesis; L-histidine from 5-phospho-α-D-ribose-1-diphosphate: step 8 of 9.* This is the penultimate phosphomonoester-hydrolysis step; it removes the phosphate installed earlier (by the aminotransferase HisC on imidazole-acetol phosphate → histidinol-phosphate) to generate the free alcohol L-histidinol [PMID 26994138].

**Family context — three unrelated HolPase families.** The dephosphorylation of histidinol-phosphate is performed by three non-homologous enzyme families across life: HAD-type (Gammaproteobacteria such as *E. coli*/*Salmonella*, as the N-terminal domain of bifunctional HisB), PHP-type (yeast and Firmicutes such as *Bacillus subtilis*), and the **IMPase-like "HisN" family** present in Actinobacteria (e.g., *Corynebacterium glutamicum* HisN) and plants [PMID 28720084]. PP_3157's InterPro/Pfam/TIGRFAM signatures place it squarely in the IMPase-like family — notable because *P. putida* is a Gammaproteobacterium yet uses the IMPase-type rather than the enterobacterial HAD-type HolPase (the reason is explained by comparative genomics in §6b: *Pseudomonas* has a monofunctional IGP dehydratase and no HAD-type HolPase domain).

---

## 4. Substrate specificity

Although this family is structurally homologous to **myo-inositol monophosphatases (IMPases)**, its members are **specific for L-histidinol-phosphate and do not dephosphorylate D-myo-inositol-1-phosphate**, the canonical IMPase substrate. This was shown biochemically for the orthologous plant enzyme MtHPP (*Medicago truncatula*):
> "MtHPP was able to cleave inorganic phosphate from HOLP but not from d-myo-inositol-1-phosphate, the main substrate of IMPases." [PMID 26994138]

Structurally, specificity is conferred by the **C-terminal domain** (which shares little identity with true IMPases), while the catalytic machinery resides in the conserved N-terminal domain [PMID 26994138]. Importantly, several IMPase-superfamily paralogs that are sequence-similar to HisN — **CysQ, ImpA (SuhB)** — are *not* HolPases and do not participate in histidine biosynthesis [PMID 28720084]; correct annotation therefore depends on the specific HisN/TIGR02067 signature carried by PP_3157 rather than generic IMPase homology.

---

## 5. Cofactor requirement, active site, and catalytic mechanism

**Cofactor:** Mg²⁺ (UniProt COFACTOR: Mg(2+); ChEBI:18420). The reaction of IMPase-type HolPases "requires Mg(2+) cations, is catalyzed mainly by amino acid residues from the N-terminal domain" [PMID 26994138], consistent with the classic multi-Mg²⁺ IMPase phosphomonoesterase mechanism.

**Metal-binding residues (UniProt features, PIRSR):** five annotated Mg²⁺-coordinating positions — 74, 90, 92, 93, 214 (positions 74, 92, 214 flagged "catalytic"). Residues 90–95 form the diagnostic IMPase metal-binding motif **"DPIDGT"** found in the PP_3157 sequence (…VL**DPIDGT**RAF…), the hallmark of the inositol-monophosphatase fold.

**Direct sequence evidence on PP_3157 itself.** Independent motif analysis of the 263-aa Q88I44 sequence confirms an intact IMPase active site: the **PROSITE inositol-monophosphatase signature-1 (PS00629)** matches as `WVLDPIDGTRAF` at residues 87–98, and the UniProt-annotated metal ligands map to acidic residues **Glu74, Asp90, Asp93, and Asp214**. An aromatic-rich active-site segment (…MRY**GGDCYAYC**M…, res ~185–196) supplies the conserved aromatic residues that, together with a catalytic aspartate, are required for activity in this family. Mutational work on the *C. glutamicum* family identified a "highly conserved aspartate residue accompanied by several aromatic amino acid residues" as essential for activity [PMID 28720084], matching PP_3157's architecture. The protein has no signal peptide or transmembrane region, consistent with a soluble cytoplasmic enzyme.

**Oligomeric state:** IMPase-superfamily enzymes typically function as homodimers (the plant MtHPP is a dimer [PMID 26994138]); PP_3157 is annotated as a single 263-aa chain and is expected to assemble similarly.

---

## 6. Subcellular localization

The enzyme is a **soluble cytoplasmic protein** with no signal peptide or transmembrane segments; histidine biosynthesis occurs in the bacterial cytoplasm. The compartmentalization of this family tracks the site of His biosynthesis: in plants the orthologous IMPase-like HolPase is targeted to the **plastid stroma**, where the pathway operates:
> "an IMPL2:green fluorescent protein fusion protein was targeted to the plastid, where His biosynthesis occurs in plants." [PMID 20023146]

For a bacterium such as *P. putida*, the corresponding compartment is the cytoplasm.

---

## 6b. Genomic context and comparative genomics (this study)

KEGG genome mapping of *P. putida* KT2440 confirms and sharpens the assignment:

- **PP_3157 = KO K05602** (histidinol-phosphatase, EC 3.1.3.15), placed in pathway **ppu00340** (Histidine metabolism) and module **M00026** (Histidine biosynthesis, PRPP→histidine). It is the **only** K05602 gene in the genome (chromosomal position 3,576,615–3,577,406).
- **PP_3157 is genomically isolated from the *his* clusters** — its immediate neighbors are unrelated (PP_3155 iron/siderophore receptor, PP_3156 universal-stress protein, PP_3159–3161 benzoate/*ben* operon). The other histidine genes are dispersed elsewhere: *hisB*(IGPD)-*hisH*-*hisA*-*hisF* at PP_0289–0293; *hisG*-*hisD*-*hisC* at PP_0965–0967; *hisZ* PP_4890; *hisIE* PP_5015. This mirrors the situation in Actinobacteria, where the IMPase-type *hisN* lies apart from the his operons.
- **Comparative-genomics rationale.** *P. putida hisB* (PP_0289) is **K01693 = monofunctional imidazoleglycerol-phosphate dehydratase (EC 4.2.1.19)**, *not* the bifunctional enterobacterial HisB (K01089) whose N-terminal HAD domain provides HolPase activity in *E. coli*. Thus in *Pseudomonas* the two activities fused in enteric HisB are **split**: IGP dehydratase is standalone, and the histidinol-phosphatase step is supplied *in trans* by the dedicated IMPase-type enzyme PP_3157. This explains why a Gammaproteobacterium uses the IMPase/HisN-type rather than the HAD-type HolPase.
- **Distinct from IMPase paralogs.** The genome separately encodes the IMPase-superfamily paralogs *suhB* (PP_0838, K01092, myo-inositol-1-phosphatase) and *cysQ* (PP_0261, K01082), which are not HolPases [PMID 28720084]. Their existence as separate loci confirms PP_3157 is specifically the his-pathway HolPase, not a mis-annotated CysQ/SuhB.

## 7. Biological process and pathway integration

PP_3157 supplies **L-histidinol** to the terminal oxidation steps of the his pathway. Its product is the substrate of histidinol dehydrogenase (HisD), which performs the two NAD⁺-dependent oxidations converting L-histidinol → L-histidinaldehyde → L-histidine. Thus PP_3157 sits between the transaminase step (HisC) and the final dehydrogenase step (HisD) in the linear, feedback-regulated histidine biosynthetic pathway (whose genes are dispersed across the *P. putida* genome rather than in a single operon; §6b). The pathway is metabolically expensive and tightly regulated; loss of the HolPase step blocks de novo histidine production.

**Genetic validation of the family's role.** The physiological (in vivo) HolPase identity of this IMPase-like family is established by cross-species complementation: an Arabidopsis IMPase-like protein rescued a bacterial *hisN* mutant —
> "Heterologous expression of IMPL2, but not the related IMPL1 protein, was sufficient to rescue the His auxotrophy of a Streptomyces coelicolor hisN mutant." [PMID 20023146]

and deletion/knockout studies of *hisN* in Actinobacteria confirmed its requirement for histidine prototrophy, with the caveat that genome-encoded paralogs can provide partial redundancy [PMID 28720084, PMID 16901339].

---

## 7b. Strength of homology to characterized enzymes (this study)

Because PP_3157 has not itself been assayed, the reliability of the annotation depends on how closely it resembles enzymes that *have* been characterized. Global pairwise alignment (Needleman–Wunsch, BLOSUM62) gives:

| Reference enzyme | Characterization | % identity to PP_3157 |
|---|---|---|
| *C. glutamicum* HisN (Q8NS80) | First kinetic data for IMPase-type HolPase [PMID 28720084] | **36.8%** (93/253) |
| *M. truncatula* MtHPP (G7J7Q5) | Substrate/product/by-product-bound crystal structures [PMID 26994138] | **48.8%** (127/260) |
| *A. thaliana* IMPL2 / HISN7 (Q6NPM8) | Genetically validated; embryo-lethal null rescued by His [PMID 20023146] | **49.0%** (128/261) |

All values lie well above the ~25–30% "twilight zone," so PP_3157 is a *close* homolog — not a marginal domain match — of enzymes for which the reaction, Mg²⁺-dependence, substrate specificity, active-site residues, 3D fold, and in-vivo His-biosynthesis role have all been directly demonstrated. This substantially strengthens confidence in the EC 3.1.3.15 / HisN assignment beyond the default "inferred from homology" level.

## 8. Evidence summary and confidence

| Claim | Evidence type | Strength |
|---|---|---|
| EC 3.1.3.15; reaction = histidinol-P → histidinol + Pi | UniProt curated catalytic activity + TIGR02067/InterPro | High |
| Member of IMPase-like (HisN) HolPase family | InterPro IPR011809/IPR000760, Pfam PF00459, TIGRFAM TIGR02067 | High |
| Mg²⁺-dependent; active-site Asp + DPIDGT motif | UniProt metal-binding features + ortholog mutagenesis [28720084] | High |
| Specific for histidinol-P, not inositol-1-P | Biochemistry of ortholog MtHPP [26994138] | High (by homology) |
| Penultimate step of His biosynthesis (step 8/9) | UniProt pathway + reviews [26994138, 28720084] | High |
| Cytoplasmic localization | Inference from pathway + plant plastid targeting [20023146] | Moderate–High |
| In vivo HolPase role (hisN) | Genetic complementation/knockouts [20023146, 28720084, 16901339] | High (family-level) |
| Sole/dedicated HolPase; split from monofunctional IGPD | KEGG genome mapping (this study): unique K05602; hisB=K01693 (IGPD only) | High |
| Distinct from suhB/cysQ IMPase paralogs | KEGG: suhB PP_0838, cysQ PP_0261 are separate loci | High |

**Principal limitation:** PP_3157 itself has not been directly enzymatically or structurally characterized (UniProt PE3, inferred from homology). All mechanistic and specificity details derive from closely related, experimentally studied orthologs in the same IMPase-like HolPase family. The assignment is nonetheless robust because it rests on a specific TIGRFAM/InterPro family signature (not generic IMPase homology) and on convergent biochemical, structural, and genetic evidence from multiple orthologs.

---

## 9. Supported and refuted hypotheses

- **Supported:** PP_3157 is a functional histidinol-phosphate phosphatase of the IMPase/HisN family, Mg²⁺-dependent, cytoplasmic, acting at the penultimate step of L-histidine biosynthesis.
- **Refuted / excluded:** PP_3157 is *not* a general myo-inositol monophosphatase, and not a CysQ/SuhB-type IMPase paralog (those do not act in His biosynthesis); it is not a HAD-type or PHP-type HolPase.

## 10. Future directions

Direct enzymatic assay of recombinant PP_3157 (kinetics on histidinol-P vs. inositol-1-P, Mg²⁺ dependence), a *PP_3157* knockout to test histidine auxotrophy and possible paralog redundancy in *P. putida*, and an experimental or AlphaFold-validated structure to confirm the dimeric IMPase fold and active-site residues.

---

### References
- PMID 28720084 — Kulis-Horn RK, Rückert C, Kalinowski J, Persicke M. *Sequence-based identification of inositol monophosphatase-like histidinol-phosphate phosphatases (HisN) in Corynebacterium glutamicum, Actinobacteria, and beyond.* (2017)
- PMID 26994138 — Ruszkowski M, Dauter Z. *Structural Studies of Medicago truncatula Histidinol Phosphate Phosphatase from Inositol Monophosphatase Superfamily...* (2016)
- PMID 20023146 — Petersen LN et al. *The missing link in plant histidine biosynthesis: Arabidopsis myoinositol monophosphatase-like2 encodes a functional histidinol-phosphate phosphatase.* (2010)
- PMID 23617600 — Kulis-Horn RK, Persicke M, Kalinowski J. *Histidine biosynthesis, its regulation and biotechnological application in Corynebacterium glutamicum.* (2014)
- PMID 16901339 — Mormann S et al. *Random mutagenesis in Corynebacterium glutamicum... identified the last unknown gene in the histidine biosynthesis pathway.* (2006)
- UniProt Q88I44; InterPro IPR011809/IPR000760/IPR020583; Pfam PF00459; NCBIfam TIGR02067; KEGG ppu:PP_3157.


## Artifacts

- [OpenScientist final report](PP_3157-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_3157-deep-research-openscientist_artifacts/final_report.pdf)