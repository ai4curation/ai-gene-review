---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T15:17:21.131414'
end_time: '2026-07-23T15:36:05.775819'
duration_seconds: 1124.64
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4379
  gene_symbol: PP_4379
  uniprot_accession: Q88ES4
  protein_description: 'SubName: Full=Beta-ketoacyl-acyl-carrier-protein synthase
    I {ECO:0000313|EMBL:AAN69957.1}; EC=2.3.1.180 {ECO:0000313|EMBL:AAN69957.1};'
  gene_info: OrderedLocusNames=PP_4379 {ECO:0000313|EMBL:AAN69957.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: ACP_syn_III_C. (IPR013747); ACP_syn_III_N. (IPR013751); Thiolase-like.
    (IPR016039); ACP_syn_III (PF08545); ACP_syn_III_C (PF08541)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
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
  path: PP_4379-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_4379-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88ES4
- **Protein Description:** SubName: Full=Beta-ketoacyl-acyl-carrier-protein synthase I {ECO:0000313|EMBL:AAN69957.1}; EC=2.3.1.180 {ECO:0000313|EMBL:AAN69957.1};
- **Gene Information:** OrderedLocusNames=PP_4379 {ECO:0000313|EMBL:AAN69957.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ACP_syn_III_C. (IPR013747); ACP_syn_III_N. (IPR013751); Thiolase-like. (IPR016039); ACP_syn_III (PF08545); ACP_syn_III_C (PF08541)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4379" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4379' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4379** (gene ID: PP_4379, UniProt: Q88ES4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_4379 (UniProt Q88ES4)
### β-Ketoacyl-[acyl-carrier-protein] synthase III (FabH / KAS III) of *Pseudomonas putida* KT2440

---

## 1. Summary (Answer to the Research Question)

**PP_4379 (Q88ES4) encodes the housekeeping β-ketoacyl-[acyl-carrier-protein] synthase III (KAS III, "FabH"; EC 2.3.1.180) of *Pseudomonas putida* KT2440.** Its product is a soluble, cytoplasmic condensing enzyme of the bacterial dissociated (type II) fatty-acid synthase (FAS II). Its primary catalytic function is to **initiate** each cycle of de novo fatty-acid biosynthesis by carrying out a decarboxylative (Claisen) condensation of an acyl-CoA primer — physiologically **acetyl-CoA** — with **malonyl-ACP**, producing **acetoacetyl-ACP (β-ketoacyl-ACP), CO₂ and CoA**. The resulting β-ketoacyl-ACP seeds the reductive elongation cycle that builds straight-chain fatty acids for membrane glycerophospholipids. Catalysis uses the canonical KAS III **Cys–His–Asn** triad (here **Cys114–His237–Asn268**). A notable species-specific feature is that, unlike in *E. coli* where FabH is essential, in *P. putida* FabH is **not essential**: the elongation enzyme FabB provides the in-vivo initiation activity, so PP_4379 is a catalytically competent but functionally redundant initiator.

> **Annotation caveat (important):** The GenBank/UniProt free-text name *"Beta-ketoacyl-acyl-carrier-protein synthase I"* is a **legacy misannotation**. The attached EC number (2.3.1.180), the KEGG orthology (K00648), the eggNOG group (COG0332, FabH), and the Pfam domains (ACP_syn_III, PF08545/PF08541) all unambiguously specify **synthase III (FabH / KAS III)**, *not* synthase I (FabB). This report treats PP_4379 as FabH throughout.

---

## 2. Target Verification

| Attribute | Value | Source/Evidence |
|---|---|---|
| UniProt | Q88ES4 (unreviewed, TrEMBL) | UniProtKB |
| Locus | PP_4379; RefSeq WP_003254453.1; GenBank AAN69957 | UniProt/RefSeq |
| Organism | *Pseudomonas putida* KT2440 (TaxID 160488) | UniProt |
| Length / MW | 309 aa / 33.2 kDa | UniProt sequence |
| Domains | ACP_syn_III N (PF08545, res 108–185); ACP_syn_III C (PF08541, res 221–306); Thiolase-like fold (IPR016039); CDD KAS_III (cd00830) | UniProt/InterPro |
| EC / KO | EC 2.3.1.180 / K00648 (3-oxoacyl-[ACP] synthase III) | UniProt/KEGG |
| Orthology | eggNOG COG0332 (FabH) | UniProt |
| Pathways | KEGG ppu00061 (Fatty acid biosynthesis); module M00082 (FAS, initiation) | KEGG |
| Genome position | complement(4,970,636–4,971,565) | KEGG |

**Verification conclusion:** The gene symbol, EC number, orthology, and domain architecture are mutually consistent and match a FabH/KAS III enzyme in the specified organism. Literature on *Pseudomonas putida* FabH exists and applies directly (see §6). This is the correct target; the only discrepancy is the descriptive "synthase I" name, resolved above.

---

## 3. Molecular Identity and Structural Evidence

### 3.1 Domain architecture and fold
PP_4379 has the two-lobed **thiolase-like (condensing-enzyme) fold** characteristic of KAS III, built from the N-terminal (PF08545) and C-terminal (PF08541) ACP_syn_III domains and a five-layer αβαβα core (Gene3D 3.40.47.10; SUPFAM SSF53901). KAS III enzymes function as **homodimers**, with each active site formed at the dimer interface — the structural basis established by multiple FabH crystal structures (*E. coli*, *S. aureus*, *M. luteus*) [4,5,6].

### 3.2 Catalytic triad (conserved)
Sequence alignment to *E. coli* FabH places the canonical **Cys–His–Asn** triad at:

| Residue (PP_4379) | Sequence motif | *E. coli* FabH equivalent |
|---|---|---|
| **Cys114** | …SLG**C**SGY… | Cys112 (nucleophile) |
| **His237** | …FCI**H**QGS… | His244 |
| **Asn268** | …LETG**N**TV… | Asn274 |

The active-site cysteine is the acyl-accepting nucleophile; the His/Asn pair activates malonyl-ACP for decarboxylation and stabilizes the resulting carbanion/oxyanion. This His-Asn-Cys triad is the defining, conserved signature of all characterized FabH enzymes [2], confirming PP_4379 is a catalytically competent condensing enzyme rather than a degenerate homolog.

### 3.3 Discrimination from the second KT2440 KAS III paralog
KT2440 contains **two** ~305–309-aa KAS III–domain proteins:

- **PP_4379 (Q88ES4)** — the canonical FabH; **27.6 %** identical to *E. coli* FabH (global Needleman–Wunsch); the **sole** gene assigned KO K00648 and the sole member of the FAS-initiation module.
- **PP_3787 (Q88GD7)** — a **divergent** KAS III (only **14.8 %** identical to *E. coli* FabH and **16 %** to PP_4379), located next to an aminotransferase and a **non-ribosomal peptide synthetase** (PP_3788), consistent with a specialized/secondary-metabolite role rather than housekeeping FAS.

Because PP_4379 is markedly more *E. coli*-FabH-like and is the KEGG-designated FAS-initiation enzyme, it corresponds to the **canonical "FabH1"** of *P. putida* (see §6). (A third, larger KAS-III-domain protein, PP_4545/EC 2.3.1.207, is a distinct enzyme and not a FabH.)

---

## 4. Primary Function — Reaction and Substrate Specificity

**Reaction (initiation of FAS II):**

> acetyl-CoA + malonyl-[ACP] → acetoacetyl-[ACP] + CO₂ + CoA

**Mechanism (ping-pong):**
1. **Acyl transfer / priming:** the acyl group of the CoA primer (acetyl-CoA) is transferred onto the active-site **Cys114** thiol, releasing CoA and forming an acetyl-enzyme thioester.
2. **Decarboxylative condensation:** **His237/Asn268** promote decarboxylation of malonyl-ACP to a C2 carbanion, which attacks the acetyl-enzyme thioester, yielding **β-ketoacyl(acetoacetyl)-ACP** + CO₂ and regenerating the free cysteine.

**Substrate specificity (inferred from close FabH homologs):** Canonical FabH enzymes are specific for **short, straight-chain acyl-CoA primers**. For *E. coli* FabH: *K*ₘ(acetyl-CoA) ≈ 40 µM, *K*ₘ(malonyl-ACP) ≈ 5 µM; primer preference **acetyl-CoA ≈ propionyl-CoA ≫ butyryl-CoA**, with **no** activity on hexanoyl-/octanoyl-CoA [1]. For *S. pneumoniae* FabH: *K*ₘ(acetyl-CoA) = 40.3 µM, *K*ₘ(malonyl-ACP) = 18.6 µM, again preferring straight short-chain CoA primers [2]. Given PP_4379's canonical primer-binding architecture and highest similarity to *E. coli* FabH among KT2440 paralogs, its **physiological primer is acetyl-CoA**, committing acetate/acetyl units into straight-chain fatty acids. (Chain-length/branched-substrate selectivity in FabH is governed by the size of the primer pocket and residues such as the L9-loop/Phe near the triad — the structural determinant that distinguishes acetyl-selective from bulkier-primer FabH enzymes [5,6].)

**Downstream fate of the product:** acetoacetyl-ACP enters the elongation cycle — reduction (FabG), dehydration (FabA/FabZ), reduction (FabI) — and is elongated by the KAS I/II condensing enzymes FabB (PP_4175) and FabF (PP_1916/PP_3303) to yield C16–C18 acyl-ACPs used for membrane phospholipid synthesis.

---

## 5. Localization

PP_4379 is a **soluble cytoplasmic** enzyme. It is a component of the bacterial **dissociated (type II) fatty-acid synthase**, whose enzymes are individual cytosolic proteins acting on substrates tethered to the small acidic **acyl carrier protein (ACP, PP_1915)** [1]. The 309-aa sequence contains no signal peptide and no transmembrane segment. Its products (long acyl-ACPs) are handed to the membrane-associated acyltransferases (PlsX/PlsB/PlsC) at the cytoplasmic face of the inner membrane, but the FabH condensation reaction itself occurs in the cytoplasm.

---

## 6. Biological Process, Pathway Context, and Regulation

### 6.1 Pathway role
PP_4379 catalyzes the **committed initiation step** of **de novo fatty-acid biosynthesis** (FAS II; KEGG module M00082), the pathway that supplies acyl chains for **membrane glycerophospholipids** and, in *P. putida*, ultimately for storage polymers such as medium-chain-length polyhydroxyalkanoates (via β-oxidation/FAS intermediates).

### 6.2 Non-essentiality and functional redundancy in *Pseudomonas* (key nuance)
Unlike the *E. coli* paradigm — where FabH is the essential, sole initiator — the *Pseudomonas* FAS-initiation architecture is different:

- **Guo et al. (2024)** showed that *P. putida* F1 carries **two functional fabH genes** (PpfabH1 and PpfabH2) but **neither is essential**; **PpFabH1 is a canonical KAS III similar to *E. coli* FabH**, whereas PpFabH2 condenses malonyl-ACP with short/medium-chain acyl-CoAs. The genuine in-vivo initiator is **FabB** (the KAS I elongation enzyme), which decarboxylates malonyl-ACP and condenses the acetyl-ACP product with malonyl-ACP [3]. PP_4379's direct F1 ortholog is **Pput_1488** (79 % identity; conserved genomic synteny), and PP_4379 is the KT2440 counterpart of the **canonical PpFabH1**.
- In the related species *P. aeruginosa*, **deletion of all four KAS III genes yields wild-type growth**, and FAS is instead initiated by the divergent KAS I/II enzyme **FabY (PA5174)** [7].

**Interpretation:** PP_4379 is a fully competent acetyl-CoA-specific FabH that *can* prime FAS, but in *P. putida* the indispensable initiation flux is provided redundantly by FabB. PP_4379 therefore contributes to and can modulate the pool of short-chain β-ketoacyl-ACP primers rather than being an indispensable gatekeeper.

### 6.3 Regulation
FabH is a physiological control point of FAS: its activity is **feedback-inhibited by long-chain acyl-ACP end-products** (potency increasing with chain length from C12 to C20; competitive with malonyl-ACP), coupling initiation flux to cellular demand for membrane lipids [1]. This makes PP_4379 a regulatory node even where it is not strictly essential.

### 6.4 Genomic context (observation)
PP_4379 is not located within the housekeeping fabD–fabG–acpP–fabF operon (PP_1913–PP_1916); instead it sits within a **flagellar gene cluster** (flanked by flagellin PP_4378 and hook-associated proteins PP_4380/PP_4381), and its F1 ortholog Pput_1488 is likewise flanked by flagellin/FlaG genes and a nucleotide-sugar epimerase/dehydratase (Pput_1486). This synteny is conserved between strains. While its biochemical assignment as the housekeeping FabH is secure, the consistent co-localization with flagellar/glycosylation-island genes is an intriguing observation that could merit experimental follow-up (e.g., a possible ancillary role supplying acyl primers to a flagellin-glycosylation or lipid-modification pathway). This is **not established** and is flagged only as a hypothesis.

### 6.5 Pharmacological relevance
FabH/KAS III is a validated antibacterial drug target; structure-based inhibitors bind at/near the catalytic triad, and resistance mutations map to the triable region [4,5]. PP_4379 is the *P. putida* representative of this target class, though its non-essentiality in *Pseudomonas* tempers its value as a lethal target in this genus.

---

## 7. Supported and Refuted Hypotheses

**Supported**
- H1 — PP_4379 is a KAS III/FabH (EC 2.3.1.180), not a KAS I: **supported** (domains PF08545/PF08541, KO K00648, COG0332, conserved Cys114–His237–Asn268 triad).
- H2 — It initiates FAS II via acetyl-CoA + malonyl-ACP condensation, cytoplasmic: **supported** (biochemistry of canonical FabH; pathway/module assignment).
- H3 — It is the canonical "FabH1" of *P. putida*, more *E. coli*-FabH-like than the paralog PP_3787: **supported** (27.6 % vs 14.8 % identity; sole K00648; orthology to characterized PpFabH1/Pput_1488).
- H4 — FabH is dispensable in *P. putida* because FabB initiates FAS: **supported** by direct experimental evidence [3] and consistent with *P. aeruginosa* [7].

**Refuted / corrected**
- The database name "β-ketoacyl-ACP synthase **I**" (implying FabB/KAS I): **refuted** — all orthogonal evidence indicates KAS III (FabH).

---

## 8. Limitations and Future Directions

- **No direct biochemistry on PP_4379 itself.** Function is inferred from unambiguous orthology, conserved catalytic residues, and detailed characterization of close homologs (*E. coli*, *S. pneumoniae*, *P. putida* F1 PpFabH1). Direct enzymology (primer chain-length profile, *K*ₘ/*k*cat, structure) of the KT2440 protein has not been reported.
- **Substrate specificity is inferred, not measured.** Acetyl-CoA preference is predicted from sequence/architecture; medium-chain activity (as seen for the paralogous PpFabH2) has not been excluded for PP_4379.
- **Structure is predicted only** (AlphaFold model available; no experimental structure of PP_4379).
- **Genomic flagellar-cluster context is unexplained.** Whether PP_4379 has an ancillary role linked to flagellar glycosylation is an open, testable question (targeted deletion + lipidomic/glycomic phenotyping).
- Recommended experiments: recombinant expression + in-vitro condensation assays with an acyl-CoA panel; ΔPP_4379 (and ΔPP_4379 ΔfabB) phenotyping; crystallography/cryo-EM.

---

## 9. References
1. Heath RJ, Rock CO. *Inhibition of β-ketoacyl-ACP synthase III (FabH) by acyl-ACP in E. coli.* (PMID 8631920) — reaction, kinetics, primer specificity, acyl-ACP feedback inhibition.
2. Khandekar SS, et al. *Identification, substrate specificity, and inhibition of S. pneumoniae FabH.* (PMID 11375394) — conserved His-Asn-Cys triad; kinetics; short straight-chain primer preference.
3. Guo Z, et al. *Diversity in fatty acid elongation enzymes: FabB initiates FAS in P. putida F1.* (PMID 38335573) — two non-essential *P. putida* fabH genes; PpFabH1 canonical; FabB is the initiator.
4. McKinney DC, et al. *Antibacterial FabH inhibitors … resistance mutations near the catalytic triad.* (PMID 27626097) — FabH as validated antibacterial target.
5. Qiu X, et al. *Crystal structure and substrate specificity of S. aureus FabH.* (PMID 15987898) — fold, primer-pocket determinants of specificity.
6. Pereira JH, et al. *Structure of FabH … branched fatty acids in M. luteus.* (PMID 22993086) — initial condensation step; L9-loop/Phe specificity determinant.
7. Yuan Y, et al. *FAS in P. aeruginosa is initiated by FabY, not FabH.* (PMID 22753059) — KAS III dispensable in *Pseudomonas*.

*Additional database evidence: UniProt Q88ES4; KEGG ppu:PP_4379 (K00648; ppu00061; M00082); InterPro IPR013747/IPR013751/IPR016039; Pfam PF08545/PF08541; eggNOG COG0332.*


## Artifacts

- [OpenScientist final report](PP_4379-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_4379-deep-research-openscientist_artifacts/final_report.pdf)