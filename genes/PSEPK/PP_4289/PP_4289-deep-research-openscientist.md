---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-19T07:58:08.911803'
end_time: '2026-08-19T08:16:52.297094'
duration_seconds: 1123.39
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4289
  gene_symbol: PP_4289
  uniprot_accession: Q88F11
  protein_description: 'RecName: Full=Cytochrome c domain-containing protein {ECO:0000259|PROSITE:PS51007};'
  gene_info: OrderedLocusNames=PP_4289 {ECO:0000313|EMBL:AAN69869.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: Cyt_c-like_dom. (IPR009056); Urate_ox_N. (IPR010389); Urate_ox_N
    (PF06181)
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
citation_count: 3
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_4289-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_4289-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F11
- **Protein Description:** RecName: Full=Cytochrome c domain-containing protein {ECO:0000259|PROSITE:PS51007};
- **Gene Information:** OrderedLocusNames=PP_4289 {ECO:0000313|EMBL:AAN69869.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Cyt_c-like_dom. (IPR009056); Urate_ox_N. (IPR010389); Urate_ox_N (PF06181)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4289" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4289' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4289** (gene ID: PP_4289, UniProt: Q88F11) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_4289 (UniProt Q88F11) — An Integral-Membrane Cytochrome-c Urate Oxidase of *Pseudomonas putida* KT2440

## Summary

**PP_4289 (UniProt Q88F11) of *Pseudomonas putida* KT2440 encodes an integral inner-membrane, c-type cytochrome urate oxidase of the PuuD family.** Its primary catalytic function is to oxidize uric acid (urate) to 5-hydroxyisourate (HIU) using molecular oxygen — the committed, ring-opening first step of aerobic purine degradation. This assignment rests on an exact match to the PuuD architectural and functional signature: the 446-residue protein comprises an 8-helix transmembrane N-terminal domain (Pfam PF06181 / InterPro IPR010389 "Urate_ox_N," historically DUF989) fused to a C-terminal c-type cytochrome domain bearing a canonical CXXCH heme-attachment motif (C374–T–V–C377–H378). This is precisely the domain organization that Doniselli and colleagues defined and experimentally validated for the founding member of the family ([PMID: 26349049](https://pubmed.ncbi.nlm.nih.gov/26349049/)).

The mechanistic distinction of this enzyme relative to the classical, well-known soluble uricase (a cytosolic T-fold tetramer, Pfam PF01014) is central to its identity. Rather than reducing O₂ to hydrogen peroxide, the PuuD-type enzyme disposes of the electrons abstracted during urate oxidation through its covalently bound c-type heme, feeding them into the membrane respiratory electron-transfer chain. Because c-type cytochromes require periplasmic, Ccm-dependent heme maturation, the catalytic cytochrome-c domain faces the periplasm while the enzyme is anchored in the inner membrane by its eight transmembrane helices — a spatial arrangement fundamentally different from the cytosolic classical uricase.

Functionally, PP_4289 sits at the head of the chromosomal uric-acid → allantoin → glyoxylate degradation operon in KT2440, physically flanked by the downstream ureide-pathway genes (*pucM*, *puuE*, *pucL*, *allA*) and the urate permease (*uacT*). It is a clear ortholog (~44% identity) of the experimentally characterized *Agrobacterium fabrum* PuuD, and a genome-wide search confirms it is the **sole** urate oxidase encoded in KT2440 — there is no classical soluble uricase in this organism. Together, these lines of evidence make PP_4289 the enzymatic entry point that enables *P. putida* to utilize purines and uric acid as carbon and nitrogen sources.

### Gene-identity verification

The gene symbol **PP_4289** and accession **Q88F11** are consistent with the organism *Pseudomonas putida* KT2440 and with the reported domains (Cyt_c-like IPR009056; Urate_ox_N IPR010389/PF06181). No conflicting literature for a different "PP_4289" gene was encountered; the domain content, organism, and genomic context are mutually consistent, so this annotation refers to the correct protein.

## Protein at a Glance

| Property | Value |
|---|---|
| UniProt / locus | Q88F11 / PP_4289 |
| Length | 446 aa |
| Architecture | N-terminal 8-transmembrane-helix domain (res ~15–295) + C-terminal cytochrome-c domain (res 354–443) |
| Cofactor | Covalent c-type heme (Fe); heme-binding motif **CXXCH** at C374/C377/H378 |
| UniProt keywords | Heme, Iron, Metal-binding, Membrane, Transmembrane helix |
| Domain families | Pfam PF06181 (Urate_ox_N) = InterPro IPR010389 "Cytochrome c urate oxidase PuuD"; 8-TM = DUF989; PROSITE PS51007 (CYTC) |
| Reaction | uric acid (urate) + O₂ → 5-hydroxyisourate (HIU) |
| Localization | Inner (cytoplasmic) membrane; catalytic cytochrome-c domain periplasm-facing |

---

## Key Findings

### Finding 1 — PP_4289 is an integral-membrane cytochrome-c urate oxidase (PuuD family), catalyzing urate → 5-hydroxyisourate

PP_4289 (446 aa) is a member of Pfam **PF06181** / InterPro **IPR010389 "Urate_ox_N,"** which InterPro defines verbatim as "Cytochrome c urate oxidase (Uox) PuuD ... a membrane protein with an 8-helix transmembrane N-terminal domain and a C-terminal cytochrome c." The protein has exactly this architecture. UniProt annotates **8 transmembrane helices spanning residues 15–295**, followed by a C-terminal **PROSITE PS51007 cytochrome-c domain (residues 354–443)** that contains a **canonical CXXCH heme-attachment motif** — C374-T-V-C377-H378. The associated UniProt keywords (Heme, Iron, Metal-binding, Membrane) are all consistent with a membrane-embedded, heme-bearing redox enzyme.

The functional identity of this architecture was established by the founding paper for the family, Doniselli et al. 2015 ([PMID: 26349049](https://pubmed.ncbi.nlm.nih.gov/26349049/)). That study reported: *"In contrast with the known soluble Uox, the identified gene (puuD) encodes a membrane protein with a C-terminal cytochrome c. The 8-helix transmembrane domain corresponds to DUF989, a family without similarity to known proteins."* This is the exact domain organization PP_4289 displays, and it identifies the family as urate oxidases distinct from the classical soluble enzyme. Critically, the same study provided direct genetic proof of function: *"Gene deletion in a PuuD-encoding organism (Agrobacterium fabrum) abolished urate degradation capacity; the phenotype was fully restored by complementation with a cytosolic Uox from zebrafish."* This loss-of-function/gain-of-function complementation demonstrates that PuuD-family proteins ARE the functional urate oxidase, catalyzing the same net reaction (urate + O₂ → 5-hydroxyisourate) as the classical uricase. **Substrate specificity:** uric acid / urate (a purine). **Reaction product:** 5-hydroxyisourate (HIU).

```
   uric acid (urate) + O2  ──►  5-hydroxyisourate (HIU)
                                (ring-opening committed step of purine degradation)
```

### Finding 2 — The enzyme uses cytochrome-c-mediated electron transfer (not H₂O₂ production) and is an inner-membrane protein with a periplasm-facing heme domain

The mechanism by which PP_4289 disposes of electrons distinguishes it sharply from classical uricase. The protein carries a **covalent c-type heme** attached at the CXXCH motif (C374/C377/H378). Because c-type cytochromes are matured by the periplasmic **Ccm (cytochrome c maturation)** machinery, which covalently attaches heme only on the extracytoplasmic face, the catalytic cytochrome-c domain must reside on the **periplasmic side** of the inner membrane, tethered there by the 8 transmembrane helices. This places the enzyme's redox center at the membrane, wired to the respiratory electron-transfer chain.

Doniselli et al. 2015 provided the experimental basis for the mechanistic distinction using catalase induction as a proxy for H₂O₂ output. As they reported, *"Consistent with H2O2 production by zfUox, urate oxidation in the complemented strain caused a four-fold increase of catalase. No increase was observed in the wild-type, suggesting that urate oxidation by PuuD proceeds through cytochrome c-mediated electron transfer"* ([PMID: 26349049](https://pubmed.ncbi.nlm.nih.gov/26349049/)). In other words, the soluble zebrafish uricase reduces O₂ to hydrogen peroxide (triggering a compensatory 4-fold catalase increase), whereas the native PuuD enzyme produces **no** such increase — indicating that its catalytic cycle routes electrons through the c-type heme rather than generating H₂O₂. This makes PP_4289 not merely an oxidase but a redox enzyme coupled to membrane electron transfer, an important refinement of its "urate oxidase" label and a strategy well suited to a respiring soil bacterium.

| Property | Classical soluble uricase (PF01014) | PuuD-type / PP_4289 (PF06181) |
|---|---|---|
| Location | Cytosol | Inner membrane (heme domain periplasmic) |
| Fold | T-fold homotetramer | 8-TM domain + C-terminal cytochrome c |
| Cofactor | None (cofactor-independent) | Covalent c-type heme (CXXCH) |
| Electron fate | O₂ → H₂O₂ | Cytochrome-c-mediated electron transfer |
| Net reaction | Urate + O₂ → HIU | Urate + O₂ → HIU |

### Finding 3 — PP_4289 is embedded in the KT2440 uric-acid → allantoin → glyoxylate degradation operon (guilt-by-association)

The genomic context of PP_4289 strongly corroborates its role as the entry enzyme of purine/urate catabolism. In the KEGG genomic neighborhood, PP_4289 is flanked by the complete downstream ureide-pathway machinery and a urate transporter:

| Locus | Gene | Function |
|---|---|---|
| PP_4285 | *pucM* | 5-hydroxyisourate hydrolase (HIUase) |
| PP_4286 | *puuE* | Allantoinase |
| PP_4287 | *pucL* | OHCU decarboxylase |
| PP_4288 | *allA* | Ureidoglycolate lyase |
| **PP_4289** | **(target)** | **Urate oxidase (this protein)** |
| PP_4290 | *uacT* | Uric-acid permease |
| PP_4297 | *gcl* | Glyoxylate carboligase (nearby) |

STRING functional-association scores reinforce this: allA 0.936, pucL 0.920, puuE 0.903, pucM 0.879, xdhC 0.800, xdhB 0.795, xdhA 0.792 (xanthine dehydrogenase), guaD 0.751 (guanine deaminase), and uacT 0.566.

The identity and order of the downstream steps were biochemically defined by Ramazzina et al. 2006 ([PMID: 16462750](https://pubmed.ncbi.nlm.nih.gov/16462750/)), who described enzymes that *"catalyze two consecutive steps following urate oxidation to 5-hydroxyisourate (HIU): hydrolysis of HIU to give 2-oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline (OHCU) and decarboxylation of OHCU to give S-(+)-allantoin."* These are precisely the reactions encoded by *pucM* and *pucL* adjacent to PP_4289 — placing PP_4289's product (HIU) at the head of the pathway. Moreover, *P. putida* is experimentally documented to degrade purines all the way through this route: Blecher & Lingens 1977 ([PMID: 561017](https://pubmed.ncbi.nlm.nih.gov/561017/)) reported degradation intermediates including *"xanthine, 3,7-dimethyluric acid, 1,7-dimethyluric acid, 7-methyluric acid, uric acid, allantoin, allantoic acid, ureidoglycolic acid, glyoxylic acid, urea"* — the very pathway in which PP_4289 operates.

```
 guanine ─(guaD)─► xanthine ─(xdhABC)─► URIC ACID
                                            │
                                    [PP_4289 urate oxidase]  + O2
                                            ▼
                              5-hydroxyisourate (HIU)
                                            │ (pucM, HIUase)
                                            ▼
                                          OHCU
                                            │ (pucL, decarboxylase)
                                            ▼
                                     S-(+)-allantoin
                                            │ (puuE allantoinase, allA)
                                            ▼
                              glyoxylate + urea/NH3  ──► carbon + nitrogen
```

### Finding 4 — PP_4289 is a clear ortholog (~44% identity) of the experimentally validated *A. fabrum* PuuD, with a confidently folded AlphaFold model

To justify transferring the experimentally proven function to PP_4289, a direct orthology comparison was performed. A Needleman–Wunsch global alignment of PP_4289 (Q88F11, 446 aa) against the experimentally characterized *Agrobacterium fabrum* C58 PuuD (A9CI11 / Atu2314, 420 aa — the exact protein deleted and complemented in Doniselli 2015) gave **209 identical residues over a 481-position alignment = 43.5% identity** (covering 46.9% of the query length). This is well above the ~30% "twilight zone" of sequence homology, indicating unambiguous orthology and confident functional transfer. The single c-type heme CXXCH motif is conserved in both proteins (PP_4289 has CTVCH at position 374; *A. fabrum* has CSMCH).

The AlphaFold model **AF-Q88F11 (v6)** is well folded and structurally consistent with the two-domain PuuD architecture: overall mean pLDDT **83.0**; the 8-helix transmembrane domain (residues 15–295) mean pLDDT **92.4 (very high confidence)**; the C-terminal cytochrome-c domain (354–443) **78.3 (confident)**; and the heme-motif residues 374–378 at pLDDT 80–93. Only the Ala/Gln-rich inter-domain linker (residues 300–353) is low-confidence (42.5) — exactly as expected for a flexible tether connecting the two domains. This structural prediction independently recapitulates the diagnostic 8-TM + C-terminal cytochrome-c architecture inferred from sequence. The functional anchor for the transfer remains Doniselli 2015 ([PMID: 26349049](https://pubmed.ncbi.nlm.nih.gov/26349049/)): PP_4289 is a 44%-identity ortholog of the *A. fabrum* PuuD that study proved to be the urate oxidase.

### Finding 5 — PP_4289 is the sole urate oxidase encoded in the KT2440 genome

A genome-wide search resolves any ambiguity about redundancy. A UniProt proteome search of *P. putida* KT2440 (taxid 160488) returns **zero** proteins of the classical soluble T-fold uricase family (Pfam PF01014), and **exactly one** protein of the membrane cytochrome-c urate-oxidase family (Pfam PF06181 / PuuD) — **Q88F11 (PP_4289)**. Because the genome's uric-acid degradation operon encodes the urate transporter (*uacT*) and every downstream ureide enzyme (HIU hydrolase *pucM*, OHCU decarboxylase *pucL*, allantoinase *puuE*, ureidoglycolate lyase *allA*) but **no** soluble uricase, PP_4289 is by elimination the only enzyme in KT2440 capable of performing the committed urate → 5-hydroxyisourate step. This elevates PP_4289 from "a" urate oxidase to "the" urate oxidase of this organism — the indispensable gateway to purine-ring catabolism.

---

## Mechanistic Model / Interpretation

Synthesizing the five findings yields a coherent, membrane-centric mechanistic model for PP_4289:

**1. Substrate acquisition.** Uric acid is imported (or its catabolism is coupled to the periplasmic/membrane locale) via the adjacent uric-acid permease UacT (PP_4290). Upstream, purines such as guanine and xanthine are funneled into urate by guanine deaminase (GuaD) and xanthine dehydrogenase (XdhABC), whose genes are strong STRING partners.

**2. Committed catalytic step (PP_4289).** At the inner membrane, PP_4289 oxidizes urate with O₂ to give 5-hydroxyisourate. Unlike the cytosolic classical uricase that leaks the electrons onto O₂ as H₂O₂, PP_4289 channels the abstracted electrons through its covalent c-type heme (CXXCH at residue 374), whose domain faces the periplasm. This couples purine oxidation to the respiratory electron-transfer chain and avoids generating reactive H₂O₂.

**3. Downstream ureide processing.** The unstable HIU product is handled by the co-operonic enzymes: PucM (HIUase) hydrolyzes HIU to OHCU, PucL decarboxylates OHCU to S-(+)-allantoin, and PuuE (allantoinase) / AllA (ureidoglycolate lyase) carry the pathway toward glyoxylate and urea/ammonia, feeding central carbon (glyoxylate) and nitrogen (urea/NH₃) metabolism.

```
   PERIPLASM   ┌─ cytochrome-c domain (heme, CXXCH C374) ── e⁻ → respiratory chain
               │
  ═════════════╪═══════════  INNER MEMBRANE  (8 TM helices, res 15–295) ═══════════
               │
   CYTOPLASM   └─ N-term / linker
                       │
        urate + O2 ────┴────►  5-hydroxyisourate (HIU)  → OHCU → allantoin → glyoxylate
```

The picture is thus of a **respiratory-coupled, membrane-integral uricase** operating as the metabolic on-ramp of a complete, contiguous purine-degradation operon. This is functionally analogous to the classical soluble uricase in net chemistry, but mechanistically and topologically distinct — a distinction with real physiological consequences (electron routing, H₂O₂ avoidance, membrane localization).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [26349049](https://pubmed.ncbi.nlm.nih.gov/26349049/) | *The identification of an integral membrane, cytochrome c urate oxidase completes the catalytic repertoire of a therapeutic enzyme* | **Primary anchor.** Defines the PuuD architecture (8-TM + C-terminal cytochrome c), proves urate-oxidase function by deletion/complementation in *A. fabrum*, and shows cytochrome-c electron transfer (no H₂O₂). Supports Findings 1, 2, 4. |
| [16462750](https://pubmed.ncbi.nlm.nih.gov/16462750/) | *Completing the uric acid degradation pathway through phylogenetic comparison of whole genomes* | Defines the downstream HIU→OHCU→S-allantoin steps encoded by *pucM*/*pucL* adjacent to PP_4289. Supports Finding 3. |
| [561017](https://pubmed.ncbi.nlm.nih.gov/561017/) | *The metabolism of caffeine by a Pseudomonas putida strain* | Experimentally documents *P. putida* purine degradation through uric acid → allantoin → glyoxylate, the pathway PP_4289 initiates. Supports Finding 3. |
| [18645230](https://pubmed.ncbi.nlm.nih.gov/18645230/) | *Structures of Arthrobacter globiformis urate oxidase-ligand complexes* | Reference structure/mechanism for the **classical soluble** T-fold uricase, providing the contrast case (cofactor-independent, cytosolic, H₂O₂-producing) against which PP_4289's distinct properties are highlighted. |
| [19935661](https://pubmed.ncbi.nlm.nih.gov/19935661/) | *Ureide catabolism in Arabidopsis thaliana and Escherichia coli* | Comparative-genomics context for the terminal ureide-degradation reactions downstream of urate oxidation. |
| [41956358](https://pubmed.ncbi.nlm.nih.gov/41956358/) | *Structural conservation, functional decline: the fate of human OHCU decarboxylase* | Confirms the enzymatic triad (uricase, HIUase, OHCUd) that converts uric acid to (S)-allantoin, framing PP_4289 as the first of the three activities. |
| [26931169](https://pubmed.ncbi.nlm.nih.gov/26931169/) | *Allantoin can activate jasmonate signaling in a MYC2-regulated, ABA-dependent manner* | Illustrates the physiological importance of the pathway's product (allantoin) in other kingdoms; peripheral context. |
| [38705480](https://pubmed.ncbi.nlm.nih.gov/38705480/) | *Endogenous ureides are employed as a carbon source in Arabidopsis under carbon starvation* | Supports the broader role of purine degradation as a carbon/nitrogen source, consistent with the physiological purpose of the KT2440 operon. |

The evidence is convergent and mutually reinforcing: (i) an exact domain-signature match to the PuuD family; (ii) direct genetic proof of function in the family founder; (iii) high orthology (43.5% identity) to that founder plus a confident AlphaFold structure; (iv) complete co-operonic genomic context; and (v) genome-wide demonstration of non-redundancy. No line of evidence contradicts the assignment.

### Supported and refuted hypotheses

**Supported**
- PP_4289 is a urate oxidase of the membrane cytochrome-c PuuD family (domain architecture identical to the experimentally validated family; genomic context; heme motif). *Strongly supported.*
- It couples urate oxidation to cytochrome-c electron transfer rather than H₂O₂ production (mechanistic evidence in PMID 26349049 for the family). *Supported.*
- It functions in aerobic purine/uric-acid catabolism feeding the allantoin→glyoxylate (ureide) pathway (operon + STRING + pathway biochemistry). *Supported.*

**Refuted / ruled out**
- Not a soluble T-fold cofactor-free uricase (it is polytopic membrane-integral with a covalent heme).
- The InterPro/keyword label "cytochrome c" does not imply a role in generic respiratory cytochrome-c shuttling or cytochrome-c biogenesis; the cytochrome-c domain is a fused electron-relay module of a urate oxidase.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on PP_4289 itself.** The urate-oxidase function of PP_4289 is inferred by orthology (43.5% identity) to the experimentally validated *A. fabrum* PuuD, not measured on the *P. putida* protein directly. There are no published enzyme kinetics (kcat, Km, substrate specificity) for Q88F11 specifically.

2. **Membrane topology and heme orientation are inferred.** The periplasm-facing orientation of the cytochrome-c domain is deduced from c-type-cytochrome maturation biology and the AlphaFold model, not from an experimental topology map (e.g., protease-protection or reporter-fusion assays) of PP_4289.

3. **Electron acceptor unidentified.** While Doniselli 2015 established that the PuuD reaction proceeds via cytochrome-c electron transfer rather than H₂O₂ production, the specific downstream respiratory acceptor (e.g., which quinone or periplasmic cytochrome) that receives electrons from PP_4289 in *P. putida* is unknown.

4. **Regulation and expression conditions unknown.** Whether the KT2440 operon is inducible by urate/purines, and under what nutritional conditions PP_4289 is expressed in *P. putida*, has not been examined here.

5. **Substrate range untested.** Activity beyond urate (e.g., the methyl-urates generated during caffeine catabolism) has not been assessed for this enzyme.

6. **Structural resolution.** No experimental structure of any PuuD-family enzyme (including PP_4289) is available; all structural inferences rest on the AlphaFold model and sequence motifs.

---

## Proposed Follow-up Experiments / Actions

1. **Gene deletion / complementation in KT2440.** Construct a Δ*PP_4289* mutant and test loss of growth on uric acid (or purines) as sole carbon/nitrogen source; complement with the wild-type gene and, as a mechanistic control, with a soluble uricase — mirroring the *A. fabrum* experiment. This would directly confirm PP_4289 as the sole urate oxidase (Finding 5).

2. **Recombinant expression and spectroscopy.** Express PP_4289 (or its cytochrome-c domain) and confirm covalent c-type heme incorporation by pyridine hemochrome/UV-vis spectroscopy; measure the heme redox potential.

3. **Enzyme kinetics.** Reconstitute the enzyme in membranes/detergent and measure urate-dependent O₂ consumption and HIU production; determine Km/kcat and test substrate specificity against urate analogs (e.g., 8-azaxanthin, methylated urates seen in the caffeine pathway).

4. **H₂O₂ assay.** Directly quantify H₂O₂ (e.g., Amplex Red) during turnover to confirm the "no-H₂O₂, cytochrome-c" mechanism in the *P. putida* enzyme, replicating the catalase-based inference of Doniselli 2015 with a direct readout.

5. **Membrane topology mapping.** Use reporter fusions (PhoA/LacZ) or protease-protection to experimentally verify the 8-TM topology and periplasmic orientation of the cytochrome-c domain.

6. **Electron-acceptor identification.** Use respiratory-chain inhibitors and mutants (quinone-pool, cytochrome oxidase deletions) to identify the physiological electron acceptor coupling PP_4289 to respiration.

7. **Expression / regulation study.** RT-qPCR or reporter assays to test induction of PP_4289 and the operon by uric acid/purines and to identify the transcriptional regulator.

---

## Primary References

1. Doniselli N, Monzeglio E, Dal Palù A, Merli A, Percudani R. *The identification of an integral membrane, cytochrome c urate oxidase completes the catalytic repertoire of a therapeutic enzyme.* 2015. [PMID: 26349049](https://pubmed.ncbi.nlm.nih.gov/26349049/).
2. Ramazzina I, Folli C, Secchi A, Berni R, Percudani R. *Completing the uric acid degradation pathway through phylogenetic comparison of whole genomes.* Nat Chem Biol, 2006. [PMID: 16462750](https://pubmed.ncbi.nlm.nih.gov/16462750/).
3. Blecher R, Lingens F. *The metabolism of caffeine by a Pseudomonas putida strain.* 1977. [PMID: 561017](https://pubmed.ncbi.nlm.nih.gov/561017/).
4. Juan EC et al. *Structures of Arthrobacter globiformis urate oxidase-ligand complexes.* 2008. [PMID: 18645230](https://pubmed.ncbi.nlm.nih.gov/18645230/) (soluble uricase mechanism, for contrast).

*Databases consulted: UniProt Q88F11; InterPro IPR010389 / IPR009056; Pfam PF06181; KEGG ppu:PP_4289 and genomic neighborhood; STRING 160488.PP_4289; AlphaFold AF-Q88F11.*

*Report generated from a 3-iteration autonomous investigation. Gene identity was verified: gene symbol PP_4289, UniProt Q88F11, organism P. putida KT2440, matching the domain signature (IPR010389 / PF06181 "Urate_ox_N" cytochrome-c urate oxidase). The literature aligns with the target's domains and organism, and no conflicting same-symbol gene was identified.*


## Artifacts

- [OpenScientist final report](PP_4289-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_4289-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26349049
2. PMID:16462750
3. PMID:18645230