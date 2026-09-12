---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T14:00:01.903354'
end_time: '2026-07-18T14:37:39.392975'
duration_seconds: 2257.49
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mazG
  gene_symbol: mazG
  uniprot_accession: Q88MB7
  protein_description: 'RecName: Full=Nucleoside triphosphate pyrophosphohydrolase
    {ECO:0000256|ARBA:ARBA00074799}; EC=3.6.1.8 {ECO:0000256|ARBA:ARBA00066372};'
  gene_info: Name=mazG {ECO:0000313|EMBL:AAN67278.1}; OrderedLocusNames=PP_1657 {ECO:0000313|EMBL:AAN67278.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the nucleoside triphosphate pyrophosphohydrolase
  protein_domains: MazG-like_dom. (IPR004518); NTP-PPase_MazG-like_C. (IPR048011);
    NTP-PPase_MazG-like_N. (IPR048015); NTP_PyrPHydrolase_MazG. (IPR011551); MazG
    (PF03819)
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
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mazG-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mazG-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88MB7
- **Protein Description:** RecName: Full=Nucleoside triphosphate pyrophosphohydrolase {ECO:0000256|ARBA:ARBA00074799}; EC=3.6.1.8 {ECO:0000256|ARBA:ARBA00066372};
- **Gene Information:** Name=mazG {ECO:0000313|EMBL:AAN67278.1}; OrderedLocusNames=PP_1657 {ECO:0000313|EMBL:AAN67278.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the nucleoside triphosphate pyrophosphohydrolase
- **Key Domains:** MazG-like_dom. (IPR004518); NTP-PPase_MazG-like_C. (IPR048011); NTP-PPase_MazG-like_N. (IPR048015); NTP_PyrPHydrolase_MazG. (IPR011551); MazG (PF03819)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mazG" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mazG' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mazG** (gene ID: mazG, UniProt: Q88MB7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MazG (Q88MB7 / PP_1657) in *Pseudomonas putida* KT2440: A House-Cleaning Nucleoside Triphosphate Pyrophosphohydrolase

## Summary

**MazG (UniProt Q88MB7, locus PP_1657) of *Pseudomonas putida* KT2440 is a cytoplasmic, divalent-metal-dependent nucleoside triphosphate pyrophosphohydrolase (NTP-PPase; EC 3.6.1.8) that catalyzes the hydrolysis of nucleoside triphosphates to their corresponding nucleoside monophosphates plus inorganic pyrophosphate (NTP + H₂O → NMP + PPᵢ).** It belongs to the MazG-like all-α NTP-PPase superfamily (Pfam PF03819; InterPro IPR011551), a group of "house-cleaning" enzymes whose principal physiological role is to sanitize the cellular nucleotide pool by removing non-canonical and oxidatively damaged (deoxy)nucleoside triphosphates before they can be misincorporated into DNA or RNA. Characterized MazG orthologs hydrolyze all eight canonical ribo- and deoxyribonucleoside triphosphates, with a preference for deoxynucleotides, and additionally destroy mutagenic species such as 8-oxo-dGTP, dUTP, and 2-hydroxy-(iso-)ATP.

No primary experimental study has been published on the *P. putida* KT2440 protein itself. However, the functional assignment for Q88MB7 rests on an unusually strong chain of homology-based evidence. Global sequence alignment shows Q88MB7 is **56.7 % identical (74.7 % similar) to the biochemically and structurally characterized *Escherichia coli* MazG** (P0AEY3), whose crystal structure and NTPase mechanism were solved by Lee et al. (2008). Q88MB7 is a 277-residue, **two-domain (tandem) enzyme** with duplicated MazG cores (residues 28–101 and 180–236), and it retains the conserved catalytic **E-x-GDLLF** metal-coordinating motifs in both lobes. An AlphaFold model confirms this tandem architecture at high confidence (overall mean pLDDT 88.5), with both α-helical catalytic cores modeled at very high confidence and a lower-confidence flexible inter-domain linker.

At the genomic level, PP_1657 lies immediately downstream of *relA* (PP_1656, the (p)ppGpp synthetase), preserving a *relA*–*mazG* synteny seen across many bacteria and pointing to a role in tuning the **stringent-response alarmone ppGpp** and nucleotide homeostasis. Notably, and unlike *E. coli*, the *P. putida* locus **lacks an adjacent *mazEF* toxin–antitoxin module**, so the *E. coli*-specific link between MazG and *mazEF*-mediated programmed cell death should not be assumed for this organism. In short, MazG in *P. putida* is best described as a soluble cytoplasmic nucleotide-pool-sanitizing enzyme coupled, through genomic and biochemical context, to the stringent stress response.

---

## Gene / Protein Identity Verification

Before presenting findings, the identity of the target was verified against the UniProt record, satisfying the mandatory checks in the research brief:

| Attribute | Expected (UniProt Q88MB7) | Verified in this investigation |
|---|---|---|
| Gene symbol | *mazG* | ✅ Consistent with MazG-family assignment |
| Organism | *Pseudomonas putida* KT2440 | ✅ Locus PP_1657 confirmed in KT2440 genome |
| EC number | 3.6.1.8 | ✅ Reaction NTP → NMP + PPᵢ confirmed for family |
| Protein family | MazG-like NTP pyrophosphohydrolase | ✅ PF03819 / IPR011551, duplicated cores |
| Key domains | MazG-like N + C (IPR048015, IPR048011) | ✅ Two tandem MazG domains (res 28–101, 180–236) |

**Conclusion of verification:** The gene symbol *mazG* is *not* ambiguous in this case. The literature for MazG-family NTP pyrophosphohydrolases aligns precisely with the UniProt description, domain architecture, and EC number for Q88MB7. The one caveat is that *mazG* is genomically associated with the *mazEF* toxin–antitoxin system in *E. coli*, and some literature conflates MazG with programmed cell death; this investigation explicitly checked and found that the *mazEF* module is **absent** adjacent to PP_1657, so that association does not transfer to *P. putida*. Research therefore proceeded on the correct gene.

---

## Key Findings

### 1. MazG is a nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8) that hydrolyzes NTP → NMP + PPᵢ

The primary, defining function of MazG is the hydrolysis of a nucleoside triphosphate into a nucleoside monophosphate plus inorganic pyrophosphate. This reaction (EC 3.6.1.8) is established by direct biochemical characterization of multiple MazG orthologs. *E. coli* MazG was shown to hydrolyze **all eight of the canonical ribo- and deoxyribonucleoside triphosphates** to their respective monophosphates and PPᵢ, with a notable **preference for deoxynucleotides** ([PMID: 12218018](https://pubmed.ncbi.nlm.nih.gov/12218018/)). The *Thermotoga maritima* ortholog (Tm-MazG) similarly "catalyzes the hydrolysis of all eight canonical ribo- and deoxyribonucleoside triphosphates to their corresponding nucleoside monophosphates and PPᵢ," and in a second step **hydrolyzes the resultant PPᵢ to Pᵢ**, giving it an additional pyrophosphatase activity ([PMID: 12657645](https://pubmed.ncbi.nlm.nih.gov/12657645/)).

Q88MB7 is assigned to this family and reaction by UniProt (EC 3.6.1.8; MazG-like NTP-PPase superfamily; PF03819 / IPR011551). Because the reaction chemistry and broad substrate range are conserved features of the enzyme family and are supported by the very high sequence identity to characterized enzymes (see Finding 7), the *P. putida* protein is confidently assigned the same catalytic activity.

**Reaction:**
```
   NTP  +  H2O   ──MazG (Mg2+/Mn2+)──►   NMP  +  PPi
  (dNTP)                                (dNMP)
```

### 2. MazG is a "house-cleaning" enzyme that removes non-canonical / oxidatively damaged (d)NTPs

Beyond turning over canonical nucleotides, the biologically important role of MazG is to act as a **"house-cleaning" enzyme** — one that eliminates aberrant nucleotides from the pool so they cannot be incorporated into nucleic acids, where they would be mutagenic or cytotoxic. A structure-guided classification placed dimeric dUTPases, HisE, and MazG in a new superfamily of all-α NTP pyrophosphohydrolases and predicted that "uncharacterized members of this superfamily perform 'house-cleaning' functions by hydrolyzing abnormal NTPs and are functionally analogous to the structurally unrelated hydrolases of the Nudix superfamily" ([PMID: 15740738](https://pubmed.ncbi.nlm.nih.gov/15740738/)). The same analysis pointed to **2-hydroxy-adenosine (isoguanosine) triphosphate — a product of oxidative damage of ATP — as the most likely substrate** for the *Sulfolobus* MazG active site.

This prediction was confirmed experimentally in mycobacteria: mycobacterial MazG "is a potent NTP-PPase capable of hydrolyzing all canonical (d)NTPs, as well as the mutagenic **dUTP** and **8-oxo-7,8-dihydro-2'-dGTP**" ([PMID: 20529853](https://pubmed.ncbi.nlm.nih.gov/20529853/)). Because 8-oxo-dGTP and 2-hydroxy-ATP arise from reactive oxygen species and are strongly mutagenic if incorporated into DNA, MazG's ability to hydrolyze them ties the enzyme directly to genome-protection and oxidative-stress defense. This house-cleaning role is the most likely primary physiological function of *P. putida* MazG.

### 3. MazG adopts a metal-dependent, all-α-helical fold with a conserved acidic active site

Crystal structures of MazG orthologs show a conserved all-α architecture built from a characteristic four-helix module. The *Bacillus*-conserved MazG "assembles into a tetrameric architecture. Each monomer adopts a four-α-helix bundle that accommodates a metal ion using four acidic residues, and presents one putative substrate-binding site" ([PMID: 26920050](https://pubmed.ncbi.nlm.nih.gov/26920050/)). This confirms two hallmarks of the family: (i) an all-α fold and (ii) a **metal-coordinating cluster of acidic residues** (glutamates/aspartates) at the active site that positions the catalytic divalent cation (Mg²⁺ or Mn²⁺).

Crucially for Q88MB7, the *E. coli* enzyme — the closest characterized homolog — is a **two-domain monomer**: "composed of two similarly folded globular domains in tandem. Among the two putative catalytic domains, only the C-terminal domain has well ordered active sites and exhibits an NTPase activity" ([PMID: 18353782](https://pubmed.ncbi.nlm.nih.gov/18353782/)). This tandem two-domain organization matches the domain annotation for Q88MB7 exactly (see Finding 5) and indicates that in the *P. putida* enzyme, catalysis is likely concentrated in the ordered C-terminal MazG core, with the N-terminal core playing a structural/regulatory or accessory role.

### 4. MazG regulates nucleotide/alarmone (ppGpp) homeostasis and supports survival under nutritional and oxidative stress

MazG's enzymatic activity has a documented downstream consequence for the **stringent response**. In *E. coli*, "enzymatic activity of MazG in vivo affects the cellular level of guanosine 3',5'-bispyrophosphate (ppGpp), synthesized by RelA under amino acid starvation. The reduction of ppGpp, caused by MazG, may extend the period of cell survival under nutritional stress" ([PMID: 18353782](https://pubmed.ncbi.nlm.nih.gov/18353782/)). MazG thereby acts as a counterweight to RelA — trimming the ppGpp alarmone and modulating how long cells persist during starvation.

MazG also physically engages the translation/ribosome-associated GTPase machinery: "we discovered that Era interacts with MazG" — a direct protein–protein interaction with the essential GTPase Era ([PMID: 12218018](https://pubmed.ncbi.nlm.nih.gov/12218018/)). In *E. coli*, *mazG* is "being transcribed in the same polycistronic mRNA with *mazEF*" ([PMID: 16390452](https://pubmed.ncbi.nlm.nih.gov/16390452/)), placing it in the operon context of the *mazEF* toxin–antitoxin/programmed-cell-death module in that organism. Finally, the stress relevance of MazG is functionally demonstrated in mycobacteria, where "deletion of *mazG* in *M. smegmatis* rendered the mycobacteria defective in response to oxidative stress" ([PMID: 20529853](https://pubmed.ncbi.nlm.nih.gov/20529853/)). As a soluble metabolic enzyme acting on cytosolic nucleotide pools, MazG carries out its function in the **cytoplasm**.

### 5. Q88MB7 is a 277-aa two-domain enzyme with duplicated PF03819 cores and conserved E-x-GDLLF metal-binding motifs in both lobes

Domain analysis of UniProt Q88MB7 shows a **277-residue protein containing two MazG-like NTP-pyrophosphohydrolase domains** (residues 28–101 and 180–236). Pfam PF03819, Gene3D 1.10.287.1080, and SUPFAM SSF101386 are each annotated in **duplicate** ("2"), and the protein maps to eggNOG **COG3956** (MazG family). Sequence analysis identifies the conserved MazG metal-coordinating acidic signature **E-x-GD-x-x-F in both domains** — E59-LGDLLF in the N-terminal lobe and E203-VGDLLF in the C-terminal lobe — each flanked by additional acidic residues (…ERGDF…, …DGDADALED…) that form the metal-binding cluster.

This tandem two-domain organization mirrors *E. coli* MazG (a two-domain monomer in which catalytic activity resides in the C-terminal domain; [PMID: 18353782](https://pubmed.ncbi.nlm.nih.gov/18353782/)) rather than the single-domain minimal MazG proteins such as *T. maritima* TM0360 ([PMID: 25758186](https://pubmed.ncbi.nlm.nih.gov/25758186/)) or *D. radiodurans* DR2231 ([PMID: 21733847](https://pubmed.ncbi.nlm.nih.gov/21733847/)). This is an important classification: it means Q88MB7's closest functional model is the well-studied *E. coli* enzyme, whose broad canonical-NTP substrate range and ppGpp-modulating physiology are the most directly transferable.

### 6. In KT2440, *mazG* (PP_1657) lies immediately downstream of *relA* (PP_1656) but lacks an adjacent *mazEF* module

Genomic-neighborhood analysis (KEGG) shows PP_1657 (*mazG*) is directly adjacent to **PP_1656**, annotated as ATP:GTP 3'-pyrophosphotransferase, KEGG orthology **K00951 = GTP pyrophosphokinase / (p)ppGpp synthetase RelA** (EC 2.7.6.5; UniProt Q88MB8), within the purine-metabolism pathway. The other immediate neighbors — PP_1654 (cysteine synthase), PP_1655 (RlmD rRNA methyltransferase), and PP_1658–1660 (conserved proteins of unknown function) — **do not include *mazE* or *mazF* toxin–antitoxin genes**.

This is a significant organism-specific distinction. In *E. coli* the chromosomal arrangement is *relA*–*mazEF*–*mazG*, embedding *mazG* in the programmed-cell-death operon. In *P. putida* the **_relA_–_mazG_ adjacency is retained but the intervening _mazEF_ module is absent.** The conserved *relA*–*mazG* linkage strengthens the interpretation that MazG participates in tuning the ppGpp stringent response (consistent with Finding 4), while the missing *mazEF* module means the *E. coli*-specific programmed-cell-death connection should **not** be extrapolated to *P. putida*.

```
  E. coli:      relA ── mazE ── mazF ── mazG      (mazG in mazEF operon)
  P. putida:    relA ── mazG                       (relA-mazG synteny; no mazEF)
             (PP_1656)  (PP_1657)
```

### 7. Q88MB7 is a clear ortholog of the biochemically and structurally characterized *E. coli* MazG (56.7 % identity, 74.7 % similarity)

A global Needleman–Wunsch alignment (BLOSUM62) of Q88MB7 (277 aa) against *E. coli* MazG P0AEY3 (263 aa) yields **148/261 identical positions (56.7 % identity) and 74.7 % similarity across essentially the full length**. P0AEY3 is the enzyme whose crystal structure and NTPase mechanism were solved by Lee et al. (2008) — the "MazG-ATP complex structure and subsequent mutagenesis studies explain the peculiar active site environment accommodating all eight canonical NTPs as substrates" ([PMID: 18353782](https://pubmed.ncbi.nlm.nih.gov/18353782/)).

Both tandem MazG domains are conserved between the two proteins. The N-terminal metal-binding motif **GDLLFQVV is identical**, and the C-terminal catalytic-domain signature aligns residue-for-residue:

| Region | *E. coli* MazG (P0AEY3) | *P. putida* MazG (Q88MB7) |
|---|---|---|
| N-terminal metal motif | GDLLFQVV | GDLLFQVV (identical) |
| C-terminal catalytic signature | LEEE-MGDLLFATVNLARHL | LEDE-VGDLLFAAVNLARHL |
| Downstream MazG signature | ANxKFERRFR | ANxKFERRFR (conserved) |

At **56.7 % identity**, well above the ~30–40 % threshold generally accepted for confident transfer of enzyme function and identical reaction chemistry, and with all catalytically essential acidic residues conserved, Q88MB7 can be assigned the same substrate range and mechanism as *E. coli* MazG with high confidence.

### 8. AlphaFold confidently predicts the tandem two-domain MazG fold

The AlphaFold DB model for Q88MB7 (AF-Q88MB7-F1, v6, 277 residues) has a **high overall mean pLDDT of 88.5 (median 91.9)**; 93.1 % of residues are modeled at confident level (pLDDT > 70) and 61.7 % at very high confidence (> 90). The two MazG-like domains are each predicted with very high confidence — **N-terminal domain (res 28–101) mean pLDDT 93.8** and **C-terminal domain (res 180–236) mean pLDDT 93.9**. In contrast, the **inter-domain segment (res 102–179) is lower** (mean 79.6, min 50), consistent with a flexible linker, and the extreme C-terminal tail (237–277) is partly disordered (min pLDDT 33).

This structural prediction independently corroborates the two-domain, all-α architecture inferred from sequence, and mirrors the experimentally observed *E. coli* two-domain fold. The lower-confidence linker is expected for a flexible connector between two rigid catalytic lobes.

---

## Mechanistic Model / Interpretation

Integrating the eight findings yields a coherent model for the role of MazG in *P. putida* KT2440:

**Molecular function.** MazG is a Mg²⁺/Mn²⁺-dependent NTP pyrophosphohydrolase that cleaves the α–β phosphoanhydride bond of nucleoside triphosphates, releasing PPᵢ and the nucleoside monophosphate. It is broad-specificity toward all eight canonical (d)NTPs (deoxynucleotide-preferring) but, physiologically, its most important substrates are aberrant nucleotides.

**Cellular role — nucleotide-pool sanitation.** The enzyme's central job is "house-cleaning": destroying non-canonical / oxidatively damaged nucleotides (8-oxo-dGTP, dUTP, 2-hydroxy-ATP/isoguanosine triphosphate) before DNA/RNA polymerases can incorporate them. By converting these to monophosphates, MazG removes their triphosphate "currency," preventing mutagenic misincorporation and preserving genome integrity — functionally parallel to the Nudix hydrolases (e.g., MutT) but structurally unrelated.

**Regulatory coupling — the stringent response.** MazG's genomic position immediately downstream of *relA* and the demonstrated ability of MazG activity to lower ppGpp levels connect nucleotide catabolism to the stringent response. RelA synthesizes the alarmone ppGpp during nutritional/oxidative stress; MazG activity trims ppGpp, modulating the depth and duration of stringent shutdown and, in *E. coli*, extending survival under starvation. The retention of *relA*–*mazG* synteny in *P. putida* suggests this regulatory partnership is conserved.

```
   Oxidative / nutritional stress
            │
            ▼
   ROS ──► damaged (d)NTPs (8-oxo-dGTP, 2-OH-ATP, dUTP)
            │                                   ┌────────────────┐
            ▼                                   │  RelA (PP_1656) │──► ppGpp ↑
        ┌─────────┐                             └────────────────┘        │
        │  MazG   │ hydrolyzes damaged (d)NTPs        (genomically         │
        │(PP_1657)│──► NMP + PPi                        adjacent)          ▼
        └─────────┘        │                        MazG NTPase ──► ppGpp ↓
            │              ▼                        (tunes stringent response,
            ▼       clean nucleotide pool            extends survival)
     genome protection     │
   (prevents mutagenic      ▼
    misincorporation)   faithful DNA/RNA synthesis
```

**Localization.** As a soluble enzyme acting on cytosolic nucleotide pools, MazG operates in the **cytoplasm**. There is no signal peptide or transmembrane region implied by its all-α globular fold.

**What differs in *P. putida* vs. *E. coli*.** The *E. coli* literature ties MazG to *mazEF*-mediated programmed cell death because of operon co-transcription. In *P. putida*, the *mazEF* module is absent adjacent to PP_1657. Therefore, the *P. putida* enzyme is best interpreted as a nucleotide-sanitizing / stringent-response-modulating enzyme, and claims about programmed cell death should be treated as *E. coli*-specific and not automatically transferred.

---

## Evidence Base

| PMID | Study (organism / system) | How it supports the findings |
|---|---|---|
| [12218018](https://pubmed.ncbi.nlm.nih.gov/12218018/) | *E. coli* MazG; Era interaction | Defines EC 3.6.1.8 reaction; all 8 canonical (d)NTPs, deoxynucleotide preference; MazG–Era interaction (F1, F4) |
| [12657645](https://pubmed.ncbi.nlm.nih.gov/12657645/) | *T. maritima* Tm-MazG | Confirms NTP→NMP+PPᵢ for all 8 NTPs; extra pyrophosphatase activity (F1) |
| [15740738](https://pubmed.ncbi.nlm.nih.gov/15740738/) | Superfamily classification | Predicts house-cleaning role; 2-OH-ATP as substrate; all-α superfamily (F2) |
| [20529853](https://pubmed.ncbi.nlm.nih.gov/20529853/) | Mycobacterial MazG | Experimental hydrolysis of dUTP & 8-oxo-dGTP; oxidative-stress defect on deletion (F2, F4) |
| [26920050](https://pubmed.ncbi.nlm.nih.gov/26920050/) | *Bacillus* MazG crystal structure | Tetrameric all-α fold; metal-coordinating acidic active site (F3) |
| [18353782](https://pubmed.ncbi.nlm.nih.gov/18353782/) | *E. coli* MazG crystal structure | Two-domain tandem architecture; catalytic C-terminal domain; ppGpp modulation; reference for homology transfer (F3, F4, F7) |
| [16390452](https://pubmed.ncbi.nlm.nih.gov/16390452/) | *E. coli* mazEF/mazG regulation | *mazG* co-transcribed with *mazEF* in *E. coli* (F4; contrast with F6) |
| [25758186](https://pubmed.ncbi.nlm.nih.gov/25758186/) | *T. maritima* TM0360 structure | Single-domain minimal MazG; contrast to two-domain Q88MB7 (F5) |
| [21733847](https://pubmed.ncbi.nlm.nih.gov/21733847/) | *D. radiodurans* DR2231 | dUTP-specific MazG-like house-cleaning enzyme; oxidative-stress framework (F2, F5) |
| [36937295](https://pubmed.ncbi.nlm.nih.gov/36937295/) | Housecleaning MazG structural analysis | Reinforces house-cleaning nomenclature/role for the family (F2) |
| [26075750](https://pubmed.ncbi.nlm.nih.gov/26075750/) | Human DCTPP1 (MazG-like) | Illustrates substrate-specialization within superfamily; tetrameric form (context) |
| [21972224](https://pubmed.ncbi.nlm.nih.gov/21972224/) | *E. coli* cisplatin stress proteomics | MazG among stress-responsive proteins (context) |
| [33265965](https://pubmed.ncbi.nlm.nih.gov/33265965/) | Oxidative-stress transcriptomics | Broader oxidative-stress-response context (context) |

**Concordance and tension.** The core reaction and house-cleaning role are supported by concordant biochemistry across at least three organisms (*E. coli*, *T. maritima*, mycobacteria) plus structure-based prediction. The main point of tension is the *mazEF*/programmed-cell-death association, which is documented in *E. coli* ([PMID: 16390452](https://pubmed.ncbi.nlm.nih.gov/16390452/)) but does **not** apply to *P. putida* because the *mazEF* module is genomically absent there — an important negative finding that prevents over-interpretation.

---

## Supported and Refuted Hypotheses

**Supported (homology + strong cross-species evidence):**
- **H1** — Q88MB7 is an NTP pyrophosphohydrolase (EC 3.6.1.8) catalyzing NTP → NMP + PPᵢ. *Supported.*
- **H2** — It acts broadly on canonical (d)NTPs with deoxynucleotide preference. *Supported.*
- **H3** — It performs house-cleaning removal of damaged nucleotides (8-oxo-dGTP, dUTP, 2-OH-ATP). *Supported.*
- **H4** — It is a metal-dependent, all-α-helical enzyme with a two-lobed MazG core. *Supported.*
- **H5** — It is cytoplasmic. *Supported (inference from soluble metabolic-enzyme role).*

**Refined / revised for *P. putida* specifically:**
- **H6a** — PP_1657 is embedded in a *mazEF* toxin–antitoxin operon (as in *E. coli*). *Refuted by genomic context* — no *mazE/mazF* genes neighbor PP_1657.
- **H6b** — PP_1657 is functionally linked to ppGpp/stringent-response metabolism. *Strengthened* — PP_1657 is directly downstream of *relA* (PP_1656, (p)ppGpp synthetase), conserving *E. coli relA–mazG* synteny.
- **H6c** — PP_1657 participates in *mazEF*-mediated programmed cell death. *Unsupported for this strain* — the linked toxin–antitoxin module is absent.

---

## Limitations and Knowledge Gaps

1. **No primary study of the *P. putida* protein.** Every functional statement about Q88MB7 is an inference from homology, domain architecture, genomic context, and structural prediction. No enzymatic assay, knockout phenotype, or structure exists for the KT2440 enzyme specifically.
2. **Substrate specificity is inferred, not measured.** While 56.7 % identity to *E. coli* MazG strongly implies the same broad canonical-(d)NTP range with deoxynucleotide preference, the exact kinetic parameters (kcat, Km) and the relative efficiency toward damaged nucleotides in *P. putida* are unknown. MazG-like enzymes can specialize (e.g., DR2231 is dUTP-specific; human DCTPP1 prefers dCTP), so specialization in Q88MB7 cannot be fully excluded.
3. **Oligomeric state uncertain.** Characterized MazGs range from dimers (TM0360) to tetramers (*Bacillus*, mycobacterial) to two-domain monomers (*E. coli*). Q88MB7's two-domain architecture predicts an *E. coli*-like monomeric two-domain arrangement, but its actual quaternary structure has not been determined.
4. **ppGpp/stringent-response coupling is by analogy.** The *relA*–*mazG* synteny is suggestive, but a direct effect of *P. putida* MazG on ppGpp levels has not been measured.
5. **Metal preference and active-site details** (Mg²⁺ vs. Mn²⁺; which acidic residues are catalytically essential) are inferred from motif conservation rather than mutagenesis in this ortholog.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Express and purify His-tagged Q88MB7; measure pyrophosphohydrolase activity against all eight canonical (d)NTPs plus the mutagenic substrates 8-oxo-dGTP, dUTP, and 2-hydroxy-ATP. Determine kcat/Km to confirm the predicted broad specificity and deoxynucleotide preference, and to test for specialization.
2. **Metal-dependence and active-site mutagenesis.** Test Mg²⁺ vs. Mn²⁺ dependence and mutate the predicted metal-binding glutamates (E59, E203 in the GDLLF motifs) to confirm catalytic essentiality, distinguishing the roles of the N- and C-terminal cores.
3. **Genetic knockout phenotyping.** Construct a PP_1657 deletion in KT2440 and assay sensitivity to oxidative stress (H₂O₂, paraquat), mutation frequency (rifampicin-resistance assays), and survival during amino-acid starvation, to test the house-cleaning and stringent-response roles in vivo.
4. **ppGpp measurement.** Quantify intracellular ppGpp in wild-type vs. Δ*mazG* under starvation to test whether MazG modulates the alarmone as in *E. coli*.
5. **Structure determination.** Solve the crystal or cryo-EM structure (or experimentally validate the AlphaFold model) to confirm the tandem two-domain fold, oligomeric state, and active-site geometry.
6. **Interaction mapping.** Test whether *P. putida* MazG interacts with the Era GTPase homolog and/or RelA, probing conservation of the regulatory network beyond the missing *mazEF* module.

---

## Evidence Confidence Summary

| Claim | Evidence type | Confidence |
|-------|---------------|-----------|
| NTP pyrophosphohydrolase, EC 3.6.1.8 (NTP→NMP+PPᵢ) | Family/EC + ortholog biochemistry + 56.7% id to *E. coli* MazG | **High** |
| Broad canonical (d)NTP substrates, dNTP preference | Ortholog biochemistry (*E. coli*, *T. maritima*) | High (moderate for exact ranking) |
| House-cleaning of damaged NTPs (8-oxo-dGTP, dUTP, 2-OH-ATP) | Ortholog biochemistry + superfamily prediction | Moderate–High |
| Two-domain, metal-dependent all-α fold | Q88MB7 domains + motifs + AlphaFold (pLDDT 88.5) | **High** |
| Cytoplasmic localization | Inference (soluble metabolic enzyme) | High |
| Functional link to ppGpp/stringent response | *E. coli* data + conserved *relA–mazG* synteny | Moderate |
| NOT in a *mazEF* operon / not in *mazEF*-PCD | *P. putida* genomic context | High (for this strain) |

---

## Conclusion

MazG (Q88MB7 / PP_1657) of *Pseudomonas putida* KT2440 is, by strong homology and structural inference, a **cytoplasmic, divalent-metal-dependent nucleoside triphosphate pyrophosphohydrolase (EC 3.6.1.8)** that hydrolyzes NTPs to NMP + PPᵢ, acting on all eight canonical (deoxy)ribonucleoside triphosphates with a deoxynucleotide preference. Its principal biological role is **"house-cleaning" sanitation of the nucleotide pool** — destroying non-canonical and oxidatively damaged nucleotides such as 8-oxo-dGTP, dUTP, and 2-hydroxy-ATP to prevent their mutagenic incorporation into DNA and RNA — and its conserved genomic linkage downstream of *relA* implicates it in tuning the ppGpp stringent-response alarmone. Unlike *E. coli*, it is not embedded in a *mazEF* toxin–antitoxin operon, so it should not be assumed to drive *mazEF*-mediated programmed cell death. All conclusions derive from robust protein, genomic, and structural bioinformatics (notably 56.7 % identity to the mechanistically characterized *E. coli* MazG and a high-confidence AlphaFold two-domain model), as no primary study of the *P. putida* ortholog itself yet exists.


## Artifacts

- [OpenScientist final report](mazG-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mazG-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:12218018
2. PMID:12657645
3. PMID:15740738
4. PMID:20529853
5. PMID:26920050
6. PMID:18353782
7. PMID:16390452
8. PMID:25758186
9. PMID:21733847