---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T12:16:07.556390'
end_time: '2026-08-31T12:28:42.823847'
duration_seconds: 755.27
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: galE
  gene_symbol: galE
  uniprot_accession: Q88I72
  protein_description: 'RecName: Full=UDP-glucose 4-epimerase {ECO:0000256|ARBA:ARBA00018569,
    ECO:0000256|RuleBase:RU366046}; EC=5.1.3.2 {ECO:0000256|ARBA:ARBA00013189, ECO:0000256|RuleBase:RU366046};'
  gene_info: Name=galE {ECO:0000313|EMBL:AAN68737.1}; OrderedLocusNames=PP_3129 {ECO:0000313|EMBL:AAN68737.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the NAD(P)-dependent epimerase/dehydratase
  protein_domains: Epimerase_deHydtase. (IPR001509); NAD(P)-bd_dom_sf. (IPR036291);
    UDP_G4E. (IPR005886); Epimerase (PF01370)
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: galE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: galE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88I72
- **Protein Description:** RecName: Full=UDP-glucose 4-epimerase {ECO:0000256|ARBA:ARBA00018569, ECO:0000256|RuleBase:RU366046}; EC=5.1.3.2 {ECO:0000256|ARBA:ARBA00013189, ECO:0000256|RuleBase:RU366046};
- **Gene Information:** Name=galE {ECO:0000313|EMBL:AAN68737.1}; OrderedLocusNames=PP_3129 {ECO:0000313|EMBL:AAN68737.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the NAD(P)-dependent epimerase/dehydratase
- **Key Domains:** Epimerase_deHydtase. (IPR001509); NAD(P)-bd_dom_sf. (IPR036291); UDP_G4E. (IPR005886); Epimerase (PF01370)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "galE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'galE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **galE** (gene ID: galE, UniProt: Q88I72) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: galE (UDP-glucose 4-epimerase) in *Pseudomonas putida* KT2440

**UniProt Accession:** Q88I72 | **Gene:** galE | **Ordered locus:** PP_3129 | **EC:** 5.1.3.2
**KEGG ortholog:** K01784 · COG1087 · Pfam PF01370 (Epimerase) · TIGR01179 (galE) · cd05247 (UDP_G4E_1_SDR_e)
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440), taxon PSEPK

---

## Summary

**galE (PP_3129, UniProt Q88I72) encodes UDP-glucose 4-epimerase (GalE, EC 5.1.3.2), a soluble cytoplasmic homodimeric enzyme of the NAD(P)-dependent epimerase/dehydratase (short-chain dehydrogenase/reductase, SDR) superfamily.** Its primary molecular function is the reversible, NAD⁺-dependent epimerization of the C4′ hydroxyl of the glucose moiety of UDP-α-D-glucose, producing UDP-α-D-galactose (Rhea RHEA:22168; ChEBI 58885 ↔ 66914). The reaction proceeds by a distinctive "transient keto-intermediate" mechanism: a tightly (essentially irreversibly) bound NAD⁺ abstracts a hydride from C4′ of the sugar to form a 4-ketopyranose intermediate, which is then reduced from the opposite face, inverting the stereochemistry at C4. A conserved SDR Ser–Tyr–Lys catalytic triad — mapped in this work to **Ser(~113–115)–Tyr135–Lys139** of Q88I72 — provides the catalytic acid/base machinery, with the catalytic tyrosine essential for activity.

**The distinctive, organism-specific conclusion of this investigation concerns GalE's physiological role in KT2440.** Although GalE catalyzes what is nominally the terminal step of the Leloir pathway of galactose *catabolism*, *P. putida* KT2440 lacks the two upstream Leloir catabolic enzymes — galactokinase (galK, K00849) and galactose-1-phosphate uridylyltransferase (galT, K00965). Their absence means KT2440 cannot funnel exogenous galactose through the canonical degradative route to GalE. Instead, PP_3129 lies within an **exopolysaccharide (EPS) biosynthesis/export gene cluster** (flanked by PP_3126, PP_3127–PP_3128, PP_3132), and the anabolic partner enzymes phosphoglucomutase (pgm, PP_3578) and UTP–glucose-1-phosphate uridylyltransferase (galU, PP_3821) are present. This indicates that GalE in KT2440 functions **anabolically**, generating UDP-galactose from central-metabolism-derived UDP-glucose to serve as the activated sugar donor for cell-surface glycan (LPS core/O-antigen and exopolysaccharide/capsule) biosynthesis.

**Where does it act?** GalE is a soluble cytoplasmic enzyme — nucleotide-sugar interconversion occurs in the cytoplasm, and UniProt lists no signal peptide or transmembrane region for Q88I72 (321 aa, ~34.97 kDa homodimer). It supplies the activated nucleotide-sugar pool from which membrane-associated glycosyltransferases build surface glycans that are ultimately exported to the cell envelope. The evidence base combines direct UniProt/KEGG annotation of Q88I72/PP_3129, comparative genomics of the KT2440 genome, extensive biochemical/structural literature on GalE-family enzymes, and functional-genetic studies in related Gram-negative bacteria demonstrating GalE's role in LPS and EPS biosynthesis.

---

## Gene / Protein Identity Verification

Identity is **confirmed and unambiguous.** UniProt Q88I72 (321 aa, 34,968 Da) is annotated as UDP-glucose 4-epimerase, gene *galE*, ordered locus PP_3129, in *P. putida* KT2440. KEGG independently assigns ppu:PP_3129 the symbol *galE*, ortholog K01784, EC 5.1.3.2. The protein carries the diagnostic GalE/SDR domain signatures (PF01370 Epimerase, cd05247 UDP_G4E_1_SDR_e, TIGR01179 galE, COG1087, SSF51735 NAD(P)-binding Rossmann fold). All literature reviewed on GalE describes the same enzyme and reaction; no ambiguity with unrelated genes was encountered.

*Note:* KT2440 encodes a second K01784 paralog, **PP_0501**, but it is located beside a dTDP-4-rhamnose-reductase gene (a rhamnose/dTDP-sugar context) and represents a distinct nucleotide-sugar enzyme — **PP_3129 is the canonical galE** and the subject of this report.

---

## Key Findings

### Finding 1 — GalE is a NAD-dependent UDP-glucose 4-epimerase catalyzing reversible UDP-glucose ↔ UDP-galactose interconversion

UniProt entry Q88I72 (PSEPK, strain KT2440) describes a 321-amino-acid protein of 34,968 Da annotated with the catalytic activity "UDP-α-D-glucose = UDP-α-D-galactose" (Rhea RHEA:22168; ChEBI 58885/66914), EC 5.1.3.2. The entry specifies an NAD⁺ cofactor (ChEBI:57540), a homodimeric quaternary structure, and assignment to the galactose metabolism pathway (UniPathway UPA00214) within the NAD(P)-dependent epimerase/dehydratase (SDR) superfamily. Multiple orthogonal domain signatures corroborate this assignment: TIGRFAMs TIGR01179 (galE), COG1087, the conserved-domain model cd05247 (UDP_G4E_1_SDR_e), and Pfam PF01370 (Epimerase). Gene Ontology terms GO:0003978 (UDP-glucose 4-epimerase activity) and GO:0033499 (galactose catabolic process via UDP-galactose, i.e., the Leloir pathway) are attached to the entry.

The enzymatic identity is directly supported by primary literature on GalE-family enzymes. A molecular-evolution review [PMID: 33171387](https://pubmed.ncbi.nlm.nih.gov/33171387/) states that **"UDP-glucose 4-epimerase (GalE) catalyzes the interconversion of UDP-glucose (UDP-Glc) and UDP-galactose (UDP-Gal),"** precisely matching the annotated reaction for Q88I72. A structural/mechanistic review [PMID: 26162744](https://pubmed.ncbi.nlm.nih.gov/26162744/) further establishes the family assignment: **"UDP-sugar 4-epimerase (GalE) belongs to the short-chain dehydrogenase/reductase (SDR) superfamily of proteins and is one of enzymes in the Leloir pathway."** These two facts — the reaction catalyzed and the SDR-family membership — anchor the functional annotation of the *P. putida* protein.

### Finding 2 — Catalysis proceeds via a transient keto-intermediate SDR mechanism with tightly bound NAD⁺ and a catalytic tyrosine; substrate specificity is set by a "gatekeeper" residue

The mechanism of UDP-hexose 4-epimerases is well established. The enzyme abstracts a hydride from the C4′ position of the sugar onto the nicotinamide of NAD⁺, forming a transient 4-ketopyranose intermediate; the intermediate is then reduced by returning the hydride to the *opposite* face of C4, inverting its stereochemistry and yielding the epimeric product. Crucially, the NAD cofactor is bound essentially irreversibly and is activated by the uridine nucleotide of the substrate. The review [PMID: 26162744](https://pubmed.ncbi.nlm.nih.gov/26162744/) documents this cofactor behavior: **"including irreversible binding of the cofactor NAD and uridine nucleotide-induced activation of this cofactor."** The evolutionary review [PMID: 33171387](https://pubmed.ncbi.nlm.nih.gov/33171387/) summarizes the mechanism and its variability, noting GalEs **"use a conserved 'transient keto intermediate' mechanism and have variable substrate specificity."**

Substrate scope across the GalE family falls into three groups: group 1 enzymes prefer non-acetylated UDP-Glc/UDP-Gal; group 3 enzymes prefer acetylated UDP-GlcNAc/UDP-GalNAc; group 2 enzymes accept both. This preference is toggled largely by a single "gatekeeper" residue in the active site. Mutational analysis of the *Marinithermus hydrothermalis* enzyme [PMID: 23250228](https://pubmed.ncbi.nlm.nih.gov/23250228/) identified **"the identity of the so-called 'gatekeeper' residue (Ser279), which has previously been suggested to influence substrate specificity."** The *P. putida* sequence carries the conserved catalytic Tyr-x-x-x-Lys motif ("YGLSK") and the SDR Ser of the Ser/Tyr/Lys triad, along with the galE-specific TIGR01179 signature — consistent with a canonical UDP-Glc/UDP-Gal (group 1-type) epimerase, though the exact substrate breadth (whether it also accepts UDP-GlcNAc/GalNAc) has not been experimentally determined for Q88I72.

### Finding 3 — GalE acts in the cytoplasm and supplies UDP-galactose both for Leloir catabolism and as a biosynthetic precursor for LPS/exopolysaccharide

In organisms possessing the full Leloir pathway, GalE catalyzes the final step (GalK → GalT → GalE) of galactose catabolism. But GalE is equally important anabolically: it provides UDP-galactose as the activated donor for extracellular LPS core/O-antigen and capsule/exopolysaccharide biosynthesis. A review on *Aeromonas hydrophila* GalE [PMID: 20461162](https://pubmed.ncbi.nlm.nih.gov/20461162/) states this dual role explicitly: **"UDP-galactose 4-epimerase (GalE) catalyses the last step in the Leloir pathway of galactose metabolism and provides precursor for the biosynthesis of extracellular LPS and capsule."**

This biosynthetic role is demonstrated experimentally by galE knockout phenotypes across Gram-negative bacteria. In *Neisseria gonorrhoeae*, galE mutants **"displayed deep rough phenotypes, and chemical analysis confirmed the loss of galactose from the mutant lipopolysaccharide"** [PMID: 8355614](https://pubmed.ncbi.nlm.nih.gov/8355614/), directly linking GalE to the galactose content of LPS. In *Campylobacter jejuni*, a galE mutant **"expressed a lipid A-core molecule of reduced molecular weight"** and was attenuated in adhesion/invasion [PMID: 10768949](https://pubmed.ncbi.nlm.nih.gov/10768949/). Because nucleotide-sugar interconversion is a cytoplasmic process, and because UniProt lists no signal peptide or transmembrane region for the soluble 321-aa homodimeric Q88I72, GalE performs its catalysis in the cytoplasm, feeding UDP-galactose to membrane-associated glycosyltransferases that assemble surface glycans.

### Finding 4 — In KT2440 the canonical Leloir catabolic route is absent; galE (PP_3129) sits in an EPS-biosynthesis cluster and acts anabolically

This is the central organism-specific finding. Systematic examination of the *P. putida* KT2440 genome (KEGG organism code **ppu**) shows that the two upstream Leloir catabolic enzymes are **missing**: there is **no galactokinase galK (K00849)** and **no galactose-1-phosphate uridylyltransferase galT (K00965)** ortholog. In contrast, the anabolic partners are present: galU (UTP–glucose-1-phosphate uridylyltransferase, PP_3821), pgm (phosphoglucomutase, PP_3578), and galE itself. The absence of galK/galT means galactose cannot be funneled to GalE via the classical degradative pathway; instead, the UDP-glucose substrate for GalE is generated anabolically from central metabolism: glucose-1-phosphate (via pgm) → UDP-glucose (via galU) → UDP-galactose (via galE).

The genomic neighborhood of PP_3129 reinforces this interpretation. galE (PP_3129, K01784) is transcribed on the complementary strand (coordinates 3,541,757–3,542,722) and is directly flanked by polysaccharide biosynthesis and export genes: PP_3126 (polysaccharide export protein), PP_3127–PP_3128 (exopolysaccharide transport/biosynthesis proteins), and PP_3132 (polysaccharide transporter). This clustering strongly suggests co-functional organization around surface-glycan production. Notably, the second K01784 paralog PP_0501 lies adjacent to a dTDP-4-rhamnose-reductase-related gene (PP_0500), indicating a distinct O-antigen/nucleotide-sugar role and cleanly distinguishing it from PP_3129. KEGG assigns PP_3129 to galactose metabolism (ppu00052), amino-sugar and nucleotide-sugar metabolism (ppu00520), and biosynthesis of nucleotide sugars (ppu01250).

The precedent that GalE can act biosynthetically independent of catabolism is established in *Erwinia amylovora*, where **"In the absence of galactose, the galE mutant was deficient in amylovoran synthesis"** [PMID: 7507102](https://pubmed.ncbi.nlm.nih.gov/7507102/) — showing GalE supplying UDP-galactose for exopolysaccharide (amylovoran) production even without a catabolic galactose input, exactly paralleling the KT2440 arrangement lacking galK/galT. The general biosynthetic-precursor role is further supported by [PMID: 20461162](https://pubmed.ncbi.nlm.nih.gov/20461162/).

### Finding 5 — Sequence analysis of Q88I72 confirms an intact SDR/GalE catalytic apparatus

Direct motif scanning of the 321-residue Q88I72 sequence confirms all hallmarks of a functional GalE:

- **(i) N-terminal Rossmann NAD(P)-binding fingerprint.** A glycine-rich GxxGxxG motif appears at residues 7–13 (GGAGYIG), embedded in the diagnostic GalE β1-αA "GGAGYIGSH" motif. The full N-terminal segment reads MKYLVVGGAGYIGSH — the canonical dinucleotide-binding fold start.
- **(ii) SDR catalytic triad.** The catalytic tyrosine appears in the Y-x-x-x-K motif at Tyr135/Lys139 ("YGLSK"), preceded by the catalytic serine within an upstream Ser-rich segment (…HLVFSSSAAVYG…, ~Ser113–115). This Ser–Tyr135–Lys139 arrangement mirrors the Ser124/Tyr149/Lys153 triad of *E. coli* GalE and the Tyr137 of the *Thermoplasma volcanium* GalE-like enzyme.

The KEGG/Pfam MOTIF list for PP_3129 includes Epimerase (PF01370) plus multiple NAD-binding SDR Pfam signatures (GDP_Man_Dehyd, adh_short, KR, NAD_binding_2/4/10, RmlD_sub_bind), all consistent with the extended SDR/epimerase-dehydratase superfamily. The essentiality of the catalytic tyrosine in a GalE-family enzyme was established by site-directed mutagenesis in *T. volcanium*: **"The catalytic residue was assessed using site-directed mutagenesis, and Tyr(137) was found to be essential for catalysis"** [PMID: 22374996](https://pubmed.ncbi.nlm.nih.gov/22374996/) — corresponding to the Tyr135 identified in the *P. putida* sequence. The SDR framework itself is confirmed by [PMID: 26162744](https://pubmed.ncbi.nlm.nih.gov/26162744/): GalE **"belongs to the short-chain dehydrogenase/reductase (SDR) superfamily of proteins."**

---

## Mechanistic Model / Interpretation

### The reaction

GalE inverts the configuration at C4 of the hexose ring of a UDP-sugar without net oxidation or reduction of the substrate, using a permanently bound NAD⁺ as a transient hydride shuttle:

```
        UDP-α-D-glucose                             UDP-α-D-galactose
             |                                              |
             |   (1) hydride abstraction from C4'           |
             |       by tightly bound NAD+                  |
             v                                              ^
        [ UDP-4-ketopyranose ]  <---- transient keto intermediate ----
             |                                              |
             |   (2) hydride returned to OPPOSITE face      |
             |       of C4 by NADH; Tyr135 = acid/base      |
             +----------------------------------------------+

   Catalytic triad:  Ser(~113–115)  —  Tyr135  —  Lys139   (SDR fold)
   Cofactor:         NAD+ (irreversibly bound, uridine-nucleotide activated)
   Quaternary:       homodimer, ~35 kDa/subunit, soluble/cytoplasmic
```

### Metabolic context in KT2440 — anabolic, not catabolic

The pivotal insight is that KT2440's gene complement reroutes GalE's biological purpose. The following table contrasts the canonical Leloir catabolic wiring with the situation in KT2440:

| Enzyme | KEGG KO | Role in Leloir catabolism | Present in KT2440? |
|---|---|---|---|
| GalK (galactokinase) | K00849 | Gal → Gal-1-P | **Absent** |
| GalT (Gal-1-P uridylyltransferase) | K00965 | Gal-1-P + UDP-Glc → Glc-1-P + UDP-Gal | **Absent** |
| **GalE (UDP-glucose 4-epimerase)** | **K01784** | UDP-Gal ↔ UDP-Glc (terminal step) | **Present (PP_3129; paralog PP_0501)** |
| Pgm (phosphoglucomutase) | — | Glc-6-P ↔ Glc-1-P | Present (PP_3578) |
| GalU (UTP–Glc-1-P uridylyltransferase) | — | Glc-1-P → UDP-Glc | Present (PP_3821) |

Because galK and galT are missing, KT2440 does not run the degradative Leloir loop. Instead, GalE operates in the **biosynthetic direction** on a UDP-glucose pool supplied by central carbon metabolism:

```
   Central metabolism (glucose / gluconeogenesis)
                 |
          Glucose-6-phosphate
                 |  pgm (PP_3578)
                 v
          Glucose-1-phosphate
                 |  galU (PP_3821)  + UTP
                 v
            UDP-glucose  ------------------> [ glucosylated glycans ]
                 |  galE (PP_3129)   <=== THIS ENZYME
                 v
           UDP-galactose
                 |
                 v
   Glycosyltransferases (membrane-associated)
                 |
                 v
   LPS core / O-antigen  +  Exopolysaccharide / capsule  --> cell surface
```

The physical clustering of galE (PP_3129) with polysaccharide export/biosynthesis genes (PP_3126 export protein; PP_3127–PP_3128 EPS transport/biosynthesis; PP_3132 polysaccharide transporter) provides a genomic argument that the UDP-galactose produced here is destined for surface-glycan assembly. The independent paralog PP_0501, sitting next to a dTDP-rhamnose-reductase gene, likely serves a separate O-antigen/nucleotide-sugar niche — a common bacterial strategy of dedicating distinct epimerase copies to distinct glycan pathways.

### Localization

All available evidence points to a **cytoplasmic** site of action. Nucleotide-sugar interconversion is intrinsically a soluble-phase cytoplasmic process; UniProt reports no signal peptide and no transmembrane helices for Q88I72; and the protein is a compact ~35 kDa soluble homodimer. GalE therefore feeds the cytoplasmic nucleotide-sugar pool that membrane-bound glycosyltransferases draw upon to build glycans subsequently exported to the periplasm, outer membrane, and cell surface.

*Caveat on biological framing:* KT2440 is a non-pathogenic environmental saprophyte. The "virulence factor" language from the pathogen studies cited above (gonococcus, *Campylobacter*, *Erwinia*) applies to KT2440 only by analogy to the underlying biochemistry of surface-glycan biosynthesis, not to pathogenicity per se — in KT2440 these glycans contribute to envelope integrity, surface properties, and biofilm/EPS formation.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [33171387](https://pubmed.ncbi.nlm.nih.gov/33171387/) | *Molecular evolution and functional divergence of UDP-hexose 4-epimerases* | States exact reaction (UDP-Glc ↔ UDP-Gal); establishes transient keto-intermediate mechanism and variable substrate specificity |
| [26162744](https://pubmed.ncbi.nlm.nih.gov/26162744/) | *UDP-hexose 4-epimerases: structure, mechanism and substrate specificity* | Confirms SDR-superfamily membership, Leloir role, and irreversible/uridine-activated NAD cofactor |
| [23250228](https://pubmed.ncbi.nlm.nih.gov/23250228/) | *UDP-Glc(NAc) 4-epimerase from Marinithermus hydrothermalis* | Identifies the single "gatekeeper" residue (Ser279) controlling acetylated vs non-acetylated preference |
| [22374996](https://pubmed.ncbi.nlm.nih.gov/22374996/) | *Archaeal GalE-like L-threonine dehydrogenase, Thermoplasma volcanium* | Site-directed mutagenesis proves catalytic Tyr137 essential — corresponds to Tyr135 in the P. putida sequence |
| [20461162](https://pubmed.ncbi.nlm.nih.gov/20461162/) | *galE of Aeromonas hydrophila (cloning, modeling)* | States dual role: last Leloir step AND precursor provision for extracellular LPS and capsule |
| [8355614](https://pubmed.ncbi.nlm.nih.gov/8355614/) | *Role of galE in gonococcal LPS* | Experimental: galE mutants show deep-rough LPS and loss of galactose from LPS |
| [10768949](https://pubmed.ncbi.nlm.nih.gov/10768949/) | *galE of Campylobacter jejuni in LPS synthesis and virulence* | Experimental galE knockout: reduced-MW lipid A-core, links GalE to LPS core biosynthesis |
| [7507102](https://pubmed.ncbi.nlm.nih.gov/7507102/) | *Galactose metabolism genetics of Erwinia amylovora* | Shows GalE acts biosynthetically (amylovoran/EPS) even absent galactose — direct parallel to KT2440's galK/galT-less arrangement |

**Supporting context from broader literature.** Structural studies of homologs (*Thermotoga maritima* TMGalE, [PMID: 26344854](https://pubmed.ncbi.nlm.nih.gov/26344854/); *Nostoc* all4713, [PMID: 42250718](https://pubmed.ncbi.nlm.nih.gov/42250718/)) confirm the homodimeric architecture and UDP-Glc/NAD co-complex geometry generalizable to the *P. putida* enzyme. Human GALE studies ([PMID: 23732289](https://pubmed.ncbi.nlm.nih.gov/23732289/), [PMID: 23644136](https://pubmed.ncbi.nlm.nih.gov/23644136/), [PMID: 22654673](https://pubmed.ncbi.nlm.nih.gov/22654673/)) reinforce the catalytic-tyrosine and dual UDP-Gal/UDP-GalNAc substrate themes but pertain to a eukaryotic ortholog with broader substrate range. The link between GalE, galactose metabolism, and EPS/biofilm is independently demonstrated in *Bacillus subtilis*, where UDP-galactose is channeled into EPS ([PMID: 22893383](https://pubmed.ncbi.nlm.nih.gov/22893383/)), and the galE–LPS axis is reinforced by a drug-repurposing study showing galE overexpression rescues ciclopirox toxicity via galactose-metabolism/LPS pathways in *E. coli* ([PMID: 23936064](https://pubmed.ncbi.nlm.nih.gov/23936064/)).

**Challenges / caveats in the evidence.** No paper in the reviewed set characterizes the *P. putida* KT2440 GalE (Q88I72/PP_3129) directly — there is no purified-enzyme kinetic study, no crystal structure, and no targeted knockout phenotype for this specific protein. All mechanistic and localization claims are therefore inferences from (a) direct database annotation of Q88I72, (b) comparative genomics of the KT2440 genome, and (c) well-established homolog biochemistry. This is a strong but inferential chain.

---

## Supported and Refuted Hypotheses

| Hypothesis | Status | Basis |
|---|---|---|
| PP_3129 = NAD⁺-dependent UDP-glucose 4-epimerase (EC 5.1.3.2), reversible UDP-Glc ⇌ UDP-Gal | **Supported** | UniProt/KEGG annotation; conserved SDR triad + Rossmann motif in sequence; family reviews |
| Enzyme uses SDR transient-keto-intermediate mechanism with catalytic Tyr | **Supported** | Mechanistic reviews; Tyr137 mutagenesis in GalE-fold enzyme; Tyr135 conserved in Q88I72 |
| Cytoplasmic localization | **Supported (inference)** | No signal peptide/TM; nucleotide-sugar metabolism is cytoplasmic |
| Primary role in KT2440 is Leloir *catabolism* of galactose | **Refuted / unlikely** | KT2440 lacks galK and galT |
| Primary role in KT2440 is *biosynthetic* (UDP-Gal for LPS/EPS surface glycans) | **Supported (inference)** | Gene-cluster context (PP_3126–3132 EPS genes); presence of pgm+galU; cross-species precedent |
| Strict group-1 (UDP-Glc/Gal-only) vs. promiscuous (also UDP-GlcNAc/GalNAc) specificity | **Undetermined** | No enzymatic assay of Q88I72 available |

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of Q88I72.** The functional annotation rests on sequence/domain evidence (UniProt ARBA/RuleBase, TIGR01179, cd05247, Pfam PF01370) and homology to characterized GalEs. No kinetic parameters (kcat, Km for UDP-Glc/UDP-Gal), no experimentally determined structure, and no targeted PP_3129 knockout phenotype exist for the KT2440 protein specifically.

2. **Substrate breadth is unresolved.** It is not experimentally known whether the KT2440 GalE is a strict group-1 (UDP-Glc/Gal only) enzyme or whether it also epimerizes UDP-GlcNAc/UDP-GalNAc (group 2). The "gatekeeper" residue identity in Q88I72 was not experimentally mapped, so acetylated-substrate activity remains an open question.

3. **Two paralogs complicate assignment.** KT2440 encodes at least two K01784 (GalE-family) proteins — PP_3129 and PP_0501. Functional redundancy, division of labor between LPS/O-antigen and EPS/capsule, or differential expression have not been experimentally dissected. The genomic-context argument (PP_3129 in an EPS cluster; PP_0501 by a rhamnose-reductase gene) is suggestive but not proof of non-overlapping function.

4. **Downstream fate of UDP-galactose is inferred.** The specific glycan structures (which LPS core/O-antigen positions, which EPS species) that incorporate GalE-derived galactose in KT2440 have not been mapped. The EPS-cluster co-localization is genomic evidence, not biochemical proof of pathway flux.

5. **Reliance on KEGG absence-calls.** The conclusion that galK/galT are absent rests on KEGG ortholog assignment. While robust, absence-of-annotation is weaker than experimental demonstration that KT2440 cannot catabolize galactose via the Leloir route; a cryptic or divergent galK/galT — or an alternative oxidative (De Ley–Doudoroff) galactose route — cannot be fully excluded from annotation alone.

---

## Proposed Follow-up Experiments / Actions

1. **Purify and kinetically characterize recombinant PP_3129.** Express Q88I72 in *E. coli*, purify, and measure steady-state kinetics against UDP-glucose, UDP-galactose, and (critically) UDP-GlcNAc/UDP-GalNAc to define substrate-specificity group and confirm NAD⁺ dependence. This directly closes Gaps 1 and 2.

2. **Solve or model the structure and map the gatekeeper.** Obtain a crystal structure (or high-confidence AlphaFold model with docked UDP-Glc/NAD⁺) and identify the gatekeeper residue equivalent to *M. hydrothermalis* Ser279 to predict acetylated-substrate activity; validate Tyr135 essentiality by a Y135F site-directed mutant.

3. **Construct single and double knockouts (ΔPP_3129, ΔPP_0501, double).** Assay LPS profile (SDS-PAGE/silver stain for a deep-rough phenotype, as in *N. gonorrhoeae*), EPS/capsule production, biofilm formation, and galactose content of surface glycans. This tests the anabolic model and the paralog division-of-labor hypothesis. RB-TnSeq fitness profiling under galactan/EPS-relevant conditions would complement this.

4. **Confirm galactose-catabolism deficiency phenotypically.** Test whether KT2440 can grow on D-galactose as a sole carbon source; a growth defect would experimentally corroborate the KEGG-based absence of a functional Leloir catabolic route.

5. **Transcriptional co-regulation analysis.** Use RNA-seq or reporter fusions to test whether PP_3129 is co-transcribed/co-regulated with the flanking EPS-export genes (PP_3126–PP_3132) under biofilm-inducing or surface-attachment conditions, strengthening the biosynthetic-cluster interpretation.

6. **Metabolic flux / metabolomics.** Quantify intracellular UDP-glucose and UDP-galactose pools in wild-type vs ΔgalE strains to directly demonstrate GalE's anabolic contribution to the UDP-galactose pool feeding surface glycans.

---

## Conclusion

galE / PP_3129 (UniProt Q88I72) in *Pseudomonas putida* KT2440 encodes a cytoplasmic, homodimeric, NAD⁺-dependent UDP-glucose 4-epimerase (GalE, EC 5.1.3.2) of the SDR superfamily that reversibly epimerizes UDP-α-D-glucose to UDP-α-D-galactose via a transient 4-keto-intermediate mechanism using a Ser–Tyr135–Lys139 catalytic triad and a tightly bound NAD⁺. Its identity is firmly established by database annotation, conserved catalytic-motif analysis, and extensive homolog biochemistry. Its *physiological* role in KT2440 is distinctively **anabolic**: because the organism lacks the upstream Leloir catabolic enzymes galK and galT, and because PP_3129 resides within an exopolysaccharide biosynthesis/export gene cluster, GalE functions to generate UDP-galactose (from central-metabolism-derived UDP-glucose via pgm and galU) as the activated sugar donor for cell-surface LPS and exopolysaccharide/capsule glycan biosynthesis, rather than for galactose degradation. This annotation is well-supported but remains inferential pending direct biochemical and genetic characterization of the KT2440 protein.


## Artifacts

- [OpenScientist final report](galE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](galE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:33171387
2. PMID:26162744
3. PMID:23250228
4. PMID:20461162
5. PMID:8355614
6. PMID:10768949
7. PMID:7507102
8. PMID:22374996
9. PMID:26344854
10. PMID:42250718
11. PMID:23732289
12. PMID:23644136
13. PMID:22654673
14. PMID:22893383
15. PMID:23936064