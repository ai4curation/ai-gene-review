---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-16T10:41:50.084024'
end_time: '2026-07-16T10:58:07.120731'
duration_seconds: 977.04
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rffG
  gene_symbol: rffG
  uniprot_accession: Q88LZ1
  protein_description: 'RecName: Full=dTDP-glucose 4,6-dehydratase {ECO:0000256|ARBA:ARBA00011990,
    ECO:0000256|RuleBase:RU004473}; EC=4.2.1.46 {ECO:0000256|ARBA:ARBA00011990, ECO:0000256|RuleBase:RU004473};'
  gene_info: Name=rffG {ECO:0000313|EMBL:AAN67405.1}; OrderedLocusNames=PP_1785 {ECO:0000313|EMBL:AAN67405.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the NAD(P)-dependent epimerase/dehydratase
  protein_domains: dTDP_Gluc_deHydtase. (IPR005888); NAD(P)-bd_dom. (IPR016040); NAD(P)-bd_dom_sf.
    (IPR036291); GDP_Man_Dehyd (PF16363)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 18
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: rffG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: rffG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LZ1
- **Protein Description:** RecName: Full=dTDP-glucose 4,6-dehydratase {ECO:0000256|ARBA:ARBA00011990, ECO:0000256|RuleBase:RU004473}; EC=4.2.1.46 {ECO:0000256|ARBA:ARBA00011990, ECO:0000256|RuleBase:RU004473};
- **Gene Information:** Name=rffG {ECO:0000313|EMBL:AAN67405.1}; OrderedLocusNames=PP_1785 {ECO:0000313|EMBL:AAN67405.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the NAD(P)-dependent epimerase/dehydratase
- **Key Domains:** dTDP_Gluc_deHydtase. (IPR005888); NAD(P)-bd_dom. (IPR016040); NAD(P)-bd_dom_sf. (IPR036291); GDP_Man_Dehyd (PF16363)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rffG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rffG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rffG** (gene ID: rffG, UniProt: Q88LZ1) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *rffG* (Q88LZ1, PP_1785): dTDP-Glucose 4,6-Dehydratase of *Pseudomonas putida* KT2440

**Organism:** *Pseudomonas putida* strain KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) — proteome code PSEPK
**Gene:** *rffG* (Ordered locus PP_1785) · **UniProt:** Q88LZ1 · **KEGG:** ppu:PP_1785 · **KO:** K01710 · **COG:** COG1088
**Enzyme:** dTDP-glucose 4,6-dehydratase · **EC 4.2.1.46**

## Summary

**The gene *rffG* (locus PP_1785; UniProt Q88LZ1) of *Pseudomonas putida* strain KT2440 encodes dTDP-glucose 4,6-dehydratase (EC 4.2.1.46), the enzyme conventionally named RmlB.** It is a cytoplasmic, NAD⁺-dependent enzyme that catalyzes the **second, committed step of the dTDP-L-rhamnose biosynthetic pathway**: the conversion of dTDP-α-D-glucose to dTDP-4-keto-6-deoxy-D-glucose plus water. All UniProt annotations — the EC number, the InterPro domain assignments (IPR005888 dTDP_Gluc_deHydtase; IPR016040/IPR036291 NAD(P)-binding Rossmann domains), the protein family (NAD(P)-dependent epimerase/dehydratase), and the ortholog group (COG1088) — are internally consistent and are fully corroborated by primary biochemical and structural literature on orthologous enzymes. The gene symbol *rffG*, the organism, and the domain architecture all match; there is no ambiguity in the identification.

The enzyme's reaction is mechanistically well understood from studies of close orthologs. A tightly (essentially permanently) bound NAD⁺ cofactor first oxidizes the glucosyl C4 hydroxyl to a 4-keto group (generating enzyme-bound NADH); water is then eliminated between C5 and C6 to form a 4-keto-glucose-5,6-ene intermediate; finally a hydride is transferred back from NADH to C6, regenerating NAD⁺ and yielding the product dTDP-4-keto-6-deoxy-D-glucose. The enzyme is highly specific for the nucleotide sugar dTDP-D-glucose. The catalytic machinery — a Rossmann-fold dinucleotide-binding domain plus a conserved Thr/Tyr/Asp/Glu catalytic set and the SDR-family YxxxK motif — is directly identifiable in the Q88LZ1 sequence itself.

Biologically, RmlB feeds into dTDP-L-rhamnose, the activated sugar donor that pseudomonads use to build cell-surface glycans — the lipopolysaccharide (LPS) core and O-antigen, and, in the broader *Pseudomonas* genus, rhamnolipid surfactants and rhamnose-containing biofilm exopolysaccharides. In KT2440, *rffG* sits within a complete chromosomal *rmlABCD* operon (PP_1782–PP_1785) flanked by glycosyltransferases, exactly the genomic arrangement expected for a dedicated nucleotide-sugar biosynthetic module. Because L-rhamnose and its four-enzyme pathway (RmlA–D) are entirely absent from humans, this pathway is a recognized selective antibacterial target.

---

## Key Findings

### Finding 1 — *rffG* is a dTDP-glucose 4,6-dehydratase catalyzing the second step of dTDP-L-rhamnose biosynthesis

UniProt Q88LZ1 assigns EC 4.2.1.46 (dTDP-glucose 4,6-dehydratase), with the diagnostic InterPro domain IPR005888 (dTDP_Gluc_deHydtase) and NAD(P)-binding Rossmann domains (IPR016040/IPR036291). The reaction — **dTDP-α-D-glucose → dTDP-4-keto-6-deoxy-D-glucose + H₂O** — is the second of the four sequential steps in the canonical RmlA → RmlB → RmlC → RmlD pathway that converts glucose-1-phosphate and dTTP into dTDP-L-rhamnose.

The chemical mechanism has been directly resolved. Rapid-mix/quench mass spectrometry on the *Escherichia coli* enzyme captured the reaction intermediates in real time and established the three-step sequence: "*NAD(+) initially oxidizes glucosyl C4 of dTDP-glucose to NADH and dTDP-4-ketoglucose. Next, water is eliminated between C5 and C6 of dTDP-4-ketoglucose to form dTDP-4-ketoglucose-5,6-ene. Hydride transfer from NADH to C6 of dTDP-4-ketoglucose-5,6-ene regenerates NAD(+) and produces the product dTDP-4-keto-6-deoxyglucose*" ([PMID: 11076501](https://pubmed.ncbi.nlm.nih.gov/11076501/)). This defines exactly the reaction and catalytic mechanism assigned to *rffG*/Q88LZ1. Independent characterization of the Group A *Streptococcus* enzyme confirmed the pathway assignment, noting that "*GAS RmlB and RmlC are critical for dTDP-L-rhamnose biosynthesis through their action as dTDP-glucose-4,6-dehydratase and dTDP-4-keto-6-deoxyglucose-3,5-epimerase enzymes respectively*" ([PMID: 30600561](https://pubmed.ncbi.nlm.nih.gov/30600561/)).

The key insight is that although the enzyme is classified as a dehydratase (a lyase), the reaction proceeds through an internal **oxidation–dehydration–reduction** cycle mediated by a bound NAD⁺ that is regenerated by the end of each turnover, so no net consumption of cofactor occurs. This is why the enzyme carries a Rossmann NAD-binding fold despite catalyzing a net dehydration.

### Finding 2 — RffG operates in the cytoplasm and supplies dTDP-L-rhamnose for LPS core, O-antigen, rhamnolipid, and biofilm exopolysaccharide

The pathway product, dTDP-L-rhamnose, is a cytoplasmic nucleotide sugar consumed downstream by membrane-associated glycosyltransferases. In the close relative *P. aeruginosa*, the contiguous *rmlBDAC* operon synthesizes dTDP-L-rhamnose, and the downstream uses are well documented: "*L-Rhamnose (L-Rha) is a component of the lipopolysaccharide (LPS) core, several O antigen polysaccharides, and the cell surface surfactant rhamnolipid of Pseudomonas aeruginosa. In this study, four contiguous genes (rmlBDAC) responsible for the synthesis of dTDP-L-Rha in P. aeruginosa have been cloned and characterized*" ([PMID: 11065359](https://pubmed.ncbi.nlm.nih.gov/11065359/)). In that study, *rmlC* mutants produced a truncated LPS core unable to attach A-band or B-band O antigen, demonstrating that L-rhamnose is the LPS-core acceptor site for O-polysaccharide attachment.

The subcellular logic places RffG firmly in the cytoplasm: nucleotide-sugar precursors are made in the cytosol and then consumed at the cytoplasmic face of the inner membrane during O-unit assembly. As shown for *P. aeruginosa*, "*The O antigen of Pseudomonas aeruginosa B-band lipopolysaccharide is synthesized by assembling O-antigen-repeat units at the cytoplasmic face of the inner membrane*" ([PMID: 15838026](https://pubmed.ncbi.nlm.nih.gov/15838026/)). dTDP-L-rhamnose is also required for biofilm exopolysaccharide: the *P. aeruginosa* Psl polysaccharide analysis "*demonstrated the requirement for GDP-d-mannose, UDP-d-glucose and dTDP-l-rhamnose in Psl production*" ([PMID: 19659934](https://pubmed.ncbi.nlm.nih.gov/19659934/)). Notably, several *P. putida* strains produce rhamnose-containing O-polysaccharides directly (e.g., D-rhamnose homopolymers and mannose/rhamnose repeat units have been structurally characterized in *P. putida* O-antigens), consistent with an active rhamnose pathway in this species.

### Finding 3 — RffG belongs to the SDR / NAD(P)-dependent epimerase-dehydratase superfamily with a conserved Thr–Tyr–Asp–Glu catalytic set

High-resolution X-ray structures of the family member DesIV (a dTDP-glucose 4,6-dehydratase from *Streptomyces venezuelae*) reveal a classic Rossmann-fold NAD-binding domain and a precisely arranged catalytic quartet. In that structure, Tyr151 and Thr127 hydrogen-bond the substrate 4′-hydroxyl, Asp128 acts as a general acid, and Glu129 as a general base: "*the side chain of Asp(128) is in the correct position to function as a general acid for proton donation to the 6'-hydroxyl group while the side chain of Glu(129) is ideally situated to serve as the general base for proton abstraction at C-5*" ([PMID: 14570895](https://pubmed.ncbi.nlm.nih.gov/14570895/)).

Independent site-directed mutagenesis of the *E. coli* enzyme identified a homologous catalytic set near the substrate-pyranose binding pocket: "*The first group consists of Asp135(DEH), Glu136(DEH), Glu198(DEH), Lys199(DEH), and Tyr301(DEH). These residues are near the substrate-pyranose binding pocket*" ([PMID: 11380254](https://pubmed.ncbi.nlm.nih.gov/11380254/)). Mutation of these residues reduced catalytic efficiency by roughly 100-fold, confirming their functional importance. Together these studies establish that the enzyme family combines a permanently bound (recycled) NAD⁺ with an acid/base catalytic set to accomplish the oxidation–dehydration–reduction cycle — an architecture matching the IPR016040/IPR036291 Rossmann domains annotated for Q88LZ1.

### Finding 4 — In KT2440, *rffG* (PP_1785) lies in a complete chromosomal *rmlABCD* operon flanked by glycosyltransferases

Genomic context strongly reinforces the functional assignment. The KEGG/GenBank annotation of the PP_1782–PP_1786 locus shows the four dTDP-L-rhamnose pathway genes clustered together:

| Locus | Gene | Enzyme | KO / EC |
|-------|------|--------|---------|
| PP_1782 | *rfbC* (*rmlC*) | dTDP-4-dehydrorhamnose 3,5-epimerase | K01790 / EC 5.1.3.13 |
| PP_1783 | *rfbA* (*rmlA*) | glucose-1-phosphate thymidylyltransferase | K00973 / EC 2.7.7.24 |
| PP_1784 | *rfbD* (*rmlD*) | dTDP-4-dehydrorhamnose reductase | K00067 / EC 1.1.1.133 |
| **PP_1785** | ***rffG* (*rmlB*)** | **dTDP-glucose 4,6-dehydratase** | **K01710 / EC 4.2.1.46** |

The cluster is flanked by a putative mannosyltransferase (PP_1780), an O-acyltransferase (PP_1781), and a glycosyltransferase (PP_1786) — the accessory enzymes that would consume the nucleotide-sugar product to build surface glycans. UniProt Q88LZ1 (366 aa) confirms the reaction dTDP-α-D-glucose = dTDP-4-dehydro-6-deoxy-α-D-glucose + H₂O (Rhea:17221), NAD⁺ cofactor, ortholog group COG1088, and KEGG module M00793 (dTDP-L-Rha biosynthesis, Glc-1P ⇒ dTDP-L-Rha). KEGG names the gene "dTDP-glucose 4,6-dehydratase 2," indicating a second paralogous isozyme elsewhere in the genome — a common situation in pseudomonads that maintain separate rhamnose pathways for distinct glycan destinations. This clustered *rmlABCD* organization is the canonical arrangement seen across bacteria (documented in *E. coli* O-antigen clusters, *Azospirillum*, *Streptococcus mutans*, mycobacteria, and *P. aeruginosa*), further supporting the identity.

### Finding 5 — Strict specificity for dTDP-D-glucose; acid/base catalysis of the dehydration step; the pathway is human-absent

The dehydration step proceeds through acid/base catalysis proven by an elegant fluorinated-substrate experiment. In the *E. coli* enzyme, "*The enzyme contains the tightly bound coenzyme NAD(+), which mediates the dehydrogenation and rereduction steps of the reaction mechanism. In this study, we have determined that Asp135 and Glu136 are the acid and base catalysts, respectively, of the dehydration step*" ([PMID: 11601973](https://pubmed.ncbi.nlm.nih.gov/11601973/)). Using dTDP-6-fluoro-6-deoxyglucose — a substrate that eliminates fluoride without needing acid protonation of a leaving hydroxyl — Asp135 variants performed like wild type, whereas on the natural substrate they were ~100× slower, cleanly isolating Asp135's role as the acid catalyst.

The enzyme acts specifically on the **thymidine-diphospho (dTDP) sugar**, distinguishing it from the UDP- and GDP-hexose-modifying enzymes of the same superfamily. Substrate recognition is anchored on the nucleotide moiety and the D-gluco configuration of the pyranose. Finally, the pathway's therapeutic relevance is well established: "*The biosynthesis of L-rhamnose utilizes four successive enzymes RmlA, RmlB, RmlC and RmlD. Neither rhamnose nor the genes responsible for its synthesis are observed in humans*" ([PMID: 26323856](https://pubmed.ncbi.nlm.nih.gov/26323856/)). This human-absence, combined with the essentiality of the pathway in many pathogens (e.g., *rmlB* and *rmlC* are essential for mycobacterial growth, [PMID: 16472764](https://pubmed.ncbi.nlm.nih.gov/16472764/)), makes RmlB a validated antibacterial target.

### Finding 6 — The Q88LZ1 sequence itself carries the diagnostic NAD-binding fingerprint and SDR catalytic motif

Direct sequence analysis of the 366-residue Q88LZ1 protein maps the experimentally defined catalytic architecture onto the actual *P. putida* enzyme. Two features stand out:

1. An **N-terminal glycine-rich dinucleotide-binding motif GGAGFIG at residues 6–12** — the canonical GxxGxxG Rossmann fingerprint that binds NAD⁺ within the βαβ fold of this family.
2. The **extended-SDR catalytic YxxxK motif at Y158-S-A-S-K162**, whose tyrosine is the conserved catalytic acid/base residue characteristic of the NAD(P)-dependent epimerase/dehydratase superfamily.

These directly correspond to the residues shown to be catalytic in orthologs — e.g., the DesIV catalytic tyrosine that engages the substrate: "*phenolate group of Tyr(151) and O(gamma) of Thr(127) lie at 2.7 and 2.6 A, respectively from the 4'-hydroxyl group of the dTDP-glucose substrate*" ([PMID: 14570895](https://pubmed.ncbi.nlm.nih.gov/14570895/)). The presence of an intact NAD-binding fingerprint and an intact catalytic YxxxK motif in the KT2440 sequence indicates the enzyme is an active, correctly folded RmlB rather than a degenerate pseudo-enzyme.

---

## Mechanistic Model / Interpretation

RffG performs the second reaction of a linear, four-enzyme nucleotide-sugar assembly line that converts glucose-1-phosphate and dTTP into the activated donor dTDP-L-rhamnose:

```
   Glc-1-P + dTTP
        │  RmlA (RfbA / PP_1783)   glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24)
        ▼
   dTDP-α-D-glucose
        │  ►► RmlB (RffG / PP_1785)  dTDP-GLUCOSE 4,6-DEHYDRATASE  (EC 4.2.1.46)  ◄◄
        │      [bound NAD⁺ recycled]  oxidation → dehydration → reduction
        ▼
   dTDP-4-keto-6-deoxy-D-glucose
        │  RmlC (RfbC / PP_1782)   3,5-epimerase (EC 5.1.3.13)
        ▼
   dTDP-4-keto-6-deoxy-L-mannose (dTDP-4-keto-L-rhamnose)
        │  RmlD (RfbD / PP_1784)   4-reductase (EC 1.1.1.133)  [NAD(P)H]
        ▼
   dTDP-β-L-RHAMNOSE  ──►  glycosyltransferases (PP_1780, PP_1781, PP_1786 ...)
                              │
                              ▼
             LPS core / O-antigen • rhamnolipid • biofilm EPS (Psl-type)
```

Within the RmlB active site, a single catalytic cycle looks like this:

```
Step 1 (dehydrogenation):  NAD⁺ abstracts hydride from glucosyl C4-OH
                            → dTDP-4-KETO-glucose + enzyme-bound NADH
                            (Tyr/Thr position and polarize the 4'-OH)

Step 2 (dehydration):       Glu136-type BASE removes C5 proton;
                            Asp135-type ACID protonates the C6-OH leaving group
                            → dTDP-4-keto-glucose-5,6-ENE + H₂O

Step 3 (re-reduction):      NADH returns hydride to C6
                            → dTDP-4-KETO-6-DEOXY-glucose + regenerated NAD⁺
```

The cofactor is conserved across turnovers, which is why a "dehydratase" nonetheless requires — and permanently retains — an oxidized nicotinamide cofactor and a Rossmann fold. This oxidation/reduction bookkeeping is the unifying feature of the NAD(P)-dependent epimerase/dehydratase (extended SDR) superfamily to which RffG belongs.

**Localization.** All of this chemistry occurs in the **cytoplasm**. The product dTDP-L-rhamnose is a soluble nucleotide sugar handed off to glycosyltransferases that act at the cytoplasmic face of the inner membrane, where O-antigen repeat units are assembled before being flipped and polymerized. RffG itself has no membrane-spanning segments and no secretion signal; it is a soluble cytosolic enzyme.

**Physiological role.** The pathway's output is a building block, not a signaling molecule. Its importance is structural: L-rhamnose is incorporated into the LPS core/O-antigen and, in pseudomonads more broadly, into rhamnolipid surfactants and rhamnose-containing exopolysaccharides that support surface attachment, biofilm formation, and (in plant-associated pseudomonads and rhizobia) host colonization. Because RffG operates upstream of all these outputs, loss of function would be expected to truncate the LPS and diminish rhamnose-dependent surface glycans — a phenotype demonstrated for *rml* mutants in *P. aeruginosa* and *Azospirillum brasilense*.

---

## Evidence Base

| PMID | Study focus | How it supports the annotation |
|------|-------------|-------------------------------|
| [11076501](https://pubmed.ncbi.nlm.nih.gov/11076501/) | Rapid mix-quench MS of dTDP-glucose 4,6-dehydratase | Directly resolves the three-step oxidation–dehydration–reduction mechanism and the exact reaction catalyzed by RffG. |
| [30600561](https://pubmed.ncbi.nlm.nih.gov/30600561/) | Streptococcal dTDP-L-rhamnose enzymes | Confirms RmlB is the dTDP-glucose-4,6-dehydratase performing the second pathway step. |
| [14570895](https://pubmed.ncbi.nlm.nih.gov/14570895/) | X-ray structure of DesIV dehydratase | Defines the Rossmann NAD-binding fold and Thr/Tyr/Asp/Glu catalytic set; establishes the catalytic tyrosine matching the Q88LZ1 YxxxK motif. |
| [11380254](https://pubmed.ncbi.nlm.nih.gov/11380254/) | Probing E. coli dehydratase catalysis | Experimentally identifies active-site residues (Asp135, Glu136, Glu198, Lys199, Tyr301) whose mutation cripples catalysis ~100-fold. |
| [11601973](https://pubmed.ncbi.nlm.nih.gov/11601973/) | Dehydration by Glu136/Asp135 | Proves Asp135 (acid) and Glu136 (base) catalyze the dehydration step; confirms tightly bound recycled NAD⁺. |
| [11065359](https://pubmed.ncbi.nlm.nih.gov/11065359/) | *rml* locus in *P. aeruginosa* LPS | Establishes the *rmlBDAC* pathway in a close *Pseudomonas* relative and the downstream uses (LPS core, O-antigen, rhamnolipid). |
| [15838026](https://pubmed.ncbi.nlm.nih.gov/15838026/) | WaaL ligase in *P. aeruginosa* | Places O-antigen assembly at the cytoplasmic face of the inner membrane, supporting cytoplasmic localization. |
| [19659934](https://pubmed.ncbi.nlm.nih.gov/19659934/) | *P. aeruginosa* Psl exopolysaccharide | Shows dTDP-L-rhamnose is required for biofilm exopolysaccharide production. |
| [26323856](https://pubmed.ncbi.nlm.nih.gov/26323856/) | RmlA–D as anti-TB targets | Confirms the four-enzyme L-rhamnose pathway and its absence in humans (selective-target rationale). |
| [16472764](https://pubmed.ncbi.nlm.nih.gov/16472764/) | *rmlB/rmlC* essentiality in mycobacteria | Demonstrates RmlB/RmlC essentiality for growth, underscoring pathway importance. |

Supporting genomic-context evidence comes from numerous O-antigen cluster sequencing studies (*E. coli* O138/O141/O157, [PMID: 16110955](https://pubmed.ncbi.nlm.nih.gov/16110955/), [PMID: 15633653](https://pubmed.ncbi.nlm.nih.gov/15633653/), [PMID: 11029441](https://pubmed.ncbi.nlm.nih.gov/11029441/); *Azospirillum*, [PMID: 14987774](https://pubmed.ncbi.nlm.nih.gov/14987774/); *Streptococcus mutans*, [PMID: 9209063](https://pubmed.ncbi.nlm.nih.gov/9209063/)), all reporting the conserved *rmlBDAC*/*rmlABCD* clustering that we observe in KT2440 at PP_1782–PP_1785. Structural characterizations of *P. putida* O-polysaccharides ([PMID: 12350329](https://pubmed.ncbi.nlm.nih.gov/12350329/), [PMID: 29304442](https://pubmed.ncbi.nlm.nih.gov/29304442/), [PMID: 28554122](https://pubmed.ncbi.nlm.nih.gov/28554122/)) document rhamnose-containing surface glycans in this species, consistent with an active rhamnose pathway.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of Q88LZ1 itself.** Every mechanistic and structural detail cited here derives from *orthologous* RmlB enzymes (*E. coli*, *S. venezuelae* DesIV, Group A *Streptococcus*), not from the purified *P. putida* KT2440 protein. The identification is very strong on the basis of sequence identity, domain architecture, intact catalytic motifs, and genomic context — but kinetic constants (kcat, Km for dTDP-glucose), an experimentally determined structure, and confirmation of NAD⁺ occupancy for the KT2440 enzyme are all inferred rather than measured.

2. **Paralog ambiguity.** KEGG labels PP_1785 "dTDP-glucose 4,6-dehydratase **2**," implying at least one additional dehydratase-like gene in KT2440. The precise division of labor between the paralogs (e.g., LPS-directed vs. exopolysaccharide- or rhamnolipid-directed rhamnose pools) has not been resolved and could affect which surface glycans depend specifically on *rffG*/PP_1785.

3. **Species-specific downstream fate.** The downstream uses of dTDP-L-rhamnose (rhamnolipid, Psl) are best documented in *P. aeruginosa*. While *P. putida* clearly makes rhamnose-containing O-antigens, the exact set of glycoconjugates fed by PP_1785 in KT2440 has not been experimentally traced.

4. **Regulation and operon expression.** The transcriptional organization of the PP_1782–PP_1786 region (single operon vs. multiple transcripts, regulatory inputs) was inferred from gene clustering, not measured.

5. **The gene name "rffG" is a historical carryover.** In enterobacteria, *rffG* denotes the dTDP-glucose 4,6-dehydratase of the ECA (enterobacterial common antigen) pathway; in KT2440 the same symbol is applied to the *rml*-type dehydratase feeding the general rhamnose pathway. The enzymatic activity is identical (EC 4.2.1.46), so the naming does not change the functional conclusion, but readers should not assume an ECA-specific role in *P. putida*.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Express and purify His-tagged PP_1785 from KT2440; confirm co-purifying NAD⁺ (by A₃₄₀/MS), and determine steady-state kinetics (kcat, Km) on dTDP-D-glucose. Test substrate specificity against UDP-glucose and GDP-mannose to confirm strict dTDP/D-gluco selectivity.

2. **Genetic knockout and complementation.** Construct an in-frame PP_1785 deletion (and a double knockout with the paralog) and analyze LPS by SDS-PAGE/silver stain and glycosyl-composition analysis to test loss of rhamnose from surface glycans; complement to confirm specificity.

3. **Paralog dissection.** Identify the second "dTDP-glucose 4,6-dehydratase" locus, compare expression across growth conditions (planktonic vs. biofilm, rhizosphere vs. lab medium), and use single vs. double mutants to assign each paralog to specific glycan outputs.

4. **Structure determination.** Solve the X-ray or cryo-EM structure of the KT2440 enzyme with bound NAD⁺ and a substrate analog to verify the predicted Rossmann fold and the Y158/K162 catalytic motif positions inferred from sequence.

5. **Active-site mutagenesis.** Mutate the predicted catalytic residues (the Y158 of the YxxxK motif and the Asp/Glu acid–base pair) and measure activity loss to confirm the transferability of the *E. coli*/DesIV catalytic model to the *P. putida* enzyme.

6. **Phenotypic assays.** Assess the *rffG* mutant for biofilm formation, surface motility, and (given KT2440's rhizosphere lifestyle) plant-root colonization, to connect the enzyme's biochemical role to ecologically relevant surface-glycan phenotypes.

---

## Conclusion

The identity of *rffG* (PP_1785, Q88LZ1) is unambiguous and fully consistent with the UniProt annotation: it is the **RmlB dTDP-glucose 4,6-dehydratase (EC 4.2.1.46)** of *Pseudomonas putida* KT2440. It is a cytoplasmic, NAD⁺-dependent enzyme of the extended-SDR (NAD(P)-dependent epimerase/dehydratase) superfamily that catalyzes the second, committed step of dTDP-L-rhamnose biosynthesis, converting dTDP-α-D-glucose to dTDP-4-keto-6-deoxy-D-glucose via an internal oxidation–dehydration–reduction cycle. It sits in a complete chromosomal *rmlABCD* operon and supplies the activated sugar donor used to build cell-surface glycans (LPS core/O-antigen, and in pseudomonads rhamnolipid and rhamnose-containing exopolysaccharide). Its identity, family, domains, and mechanism are all corroborated by concordant biochemical, structural, and genomic evidence.


## Artifacts

- [OpenScientist final report](rffG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](rffG-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11076501
2. PMID:30600561
3. PMID:11065359
4. PMID:15838026
5. PMID:19659934
6. PMID:14570895
7. PMID:11380254
8. PMID:11601973
9. PMID:26323856
10. PMID:16472764
11. PMID:16110955
12. PMID:15633653
13. PMID:11029441
14. PMID:14987774
15. PMID:9209063
16. PMID:12350329
17. PMID:29304442
18. PMID:28554122