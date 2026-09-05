---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:12:52.003247'
end_time: '2026-09-01T02:26:28.684710'
duration_seconds: 816.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lolC
  gene_symbol: lolC
  uniprot_accession: Q88KY5
  protein_description: 'SubName: Full=LolC {ECO:0000313|EMBL:AAN67767.1};'
  gene_info: Name=lolC {ECO:0000313|EMBL:AAN67767.1}; OrderedLocusNames=PP_2154 {ECO:0000313|EMBL:AAN67767.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ABC-4 integral membrane protein family.
  protein_domains: ABC3_permease_C. (IPR003838); Lipoprotein-release_system. (IPR051447);
    LolCE_TM. (IPR011925); MacB_PCD. (IPR025857); FtsX (PF02687)
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
  path: lolC-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lolC-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KY5
- **Protein Description:** SubName: Full=LolC {ECO:0000313|EMBL:AAN67767.1};
- **Gene Information:** Name=lolC {ECO:0000313|EMBL:AAN67767.1}; OrderedLocusNames=PP_2154 {ECO:0000313|EMBL:AAN67767.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ABC-4 integral membrane protein family.
- **Key Domains:** ABC3_permease_C. (IPR003838); Lipoprotein-release_system. (IPR051447); LolCE_TM. (IPR011925); MacB_PCD. (IPR025857); FtsX (PF02687)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lolC" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lolC' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lolC** (gene ID: lolC, UniProt: Q88KY5) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: LolC (Q88KY5 / PP_2154) in *Pseudomonas putida* KT2440

## Summary

**LolC (UniProt Q88KY5; ordered locus PP_2154) is a transmembrane subunit of the essential inner-membrane ABC transporter LolCDE, the molecular machine that initiates the outer-membrane lipoprotein-sorting (Lol) pathway in the Gram-negative bacterium *Pseudomonas putida* KT2440.** LolCDE selectively extracts mature, triacylated, outer-membrane-destined lipoproteins from the outer leaflet of the inner membrane and hands them to the periplasmic chaperone LolA, which ferries them across the periplasm to the outer-membrane receptor LolB for insertion into the inner leaflet of the outer membrane. LolC does not itself hydrolyze ATP (that is the role of the LolD nucleotide-binding subunit) and does not conduct substrate through a membrane pore; instead it belongs to the MacB/FtsX superfamily of "mechanotransmission" ABC transporters, which convert cytoplasmic nucleotide-binding-domain movements into conformational work at the periplasmic face of the membrane.

Within the heterodimeric LolCDE complex (one LolC, one LolE, two LolD), LolC and LolE play **distinct, non-redundant** roles. LolC is specifically the **LolA-docking subunit**: its large periplasmic domain recruits soluble LolA from the periplasm and "primes" it to receive the lipoprotein cargo. High-resolution structural work identifies two LolC structural elements — a solvent-exposed β-hairpin loop termed the **"Hook"** and a trio of surface residues termed the **"Pad"** — as the essential features for LolA recruitment, and shows that this docking step is independent of ATP binding and hydrolysis. Substrate selectivity of the complex follows the well-established **"+2 rule"**: lipoproteins bearing aspartate at position 2 (in combination with certain position-3 residues) carry a "Lol-avoidance signal" and are retained in the inner membrane, whereas lipoproteins with any other residue at position 2 are released to the outer membrane. Full N-acylation of the N-terminal cysteine (yielding the mature triacylated form) is a prerequisite for release, independent of the sorting signal.

The specific *P. putida* KT2440 assignment is well supported. Genomic-neighborhood analysis shows a canonical, contiguous **lolCDE operon** (PP_2154 = lolC, PP_2155 = lolD, PP_2156 = lolE), and a global sequence alignment demonstrates that Q88KY5 is unambiguously the **LolC ortholog** (55.4% identity to *E. coli* LolC vs. 49.3% to *E. coli* LolE), not LolE. Because lipoprotein trafficking by the Lol machinery is essential for cell-envelope biogenesis and viability — demonstrated directly in *Pseudomonas aeruginosa* as well as *E. coli* — LolCDE (including LolC) is a validated, actively pursued antibacterial drug target, with multiple small-molecule inhibitors whose resistance mutations map to LolC and LolE.

---

## Gene / Protein Identity Verification

Before reporting function, the identity of the target was verified against the UniProt record and the primary literature, as mandated by the research brief.

| Attribute | Value |
|---|---|
| UniProt accession | Q88KY5 |
| Gene name | *lolC* |
| Ordered locus | PP_2154 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) |
| Length | 416 aa |
| Protein family | ABC-4 integral membrane protein family |
| Diagnostic domains | LolCE_TM (IPR011925), FtsX (PF02687), MacB_PCD (IPR025857), ABC3_permease_C (IPR003838), Lipoprotein-release_system (IPR051447) |

**Verdict: identity confirmed.** The gene symbol *lolC*, the ABC-4 / MacB-family domain architecture, and the operon context all align consistently with the LolC subunit of the Lol lipoprotein-sorting machinery. A global Needleman–Wunsch alignment (see Finding F006) resolves the potential LolC-vs-LolE ambiguity decisively in favor of LolC. This is therefore *not* a case of an ambiguous or mis-annotated symbol; the functional literature — although developed largely in *E. coli* — transfers to Q88KY5 with high confidence, reinforced by direct experimental work in the closely related *Pseudomonas aeruginosa*.

---

## Key Findings

### F001 — LolC is a transmembrane subunit of the LolCDE ABC transporter that initiates outer-membrane lipoprotein sorting

LolC is one of the two integral membrane subunits of the **LolCDE complex**, an ATP-binding cassette (ABC) transporter that constitutes the inner-membrane component of the Lol (Localization of Lipoproteins) machinery. The complete Lol system comprises three functional modules: the inner-membrane LolCDE transporter, the periplasmic carrier protein LolA, and the outer-membrane receptor LolB. As stated in the authoritative review of the pathway, *"The Lol system comprises an inner-membrane ABC transporter LolCDE complex, a periplasmic carrier protein, LolA, and an outer membrane receptor protein, LolB"* ([PMID: 20419407](https://pubmed.ncbi.nlm.nih.gov/20419407/)). The complex is the initiating enzyme of the pathway: *"The ATP-binding cassette (ABC) transporter LolCDE initiates the Lol pathway by selectively extracting and transporting lipoproteins for trafficking"* ([PMID: 36228045](https://pubmed.ncbi.nlm.nih.gov/36228045/)). Its subunit stoichiometry is defined biochemically: *"LolCDE is composed of one copy each of membrane subunits LolC and LolE, and two copies of nucleotide-binding subunit LolD"* ([PMID: 19809197](https://pubmed.ncbi.nlm.nih.gov/19809197/)). The UniProt assignment of Q88KY5 to the ABC-4 integral membrane protein family, carrying the LolCE_TM (IPR011925), FtsX (PF02687) and MacB_PCD domains, is fully consistent with this role.

### F002 — LolC operates by mechanotransmission, not by transmembrane substrate passage

LolC belongs to the **MacB/FtsX superfamily** of ABC transporters, which are mechanistically distinct from classical channel-forming ABC transporters. Q88KY5 carries the MacB periplasmic-domain (MacB_PCD) and FtsX transmembrane signatures that define this superfamily. Critically, *"The MacB transmembrane domain lacks a central cavity through which substrates could be passed, but instead conveys conformational changes from one side of the membrane to the other, a process we term mechanotransmission"* ([PMID: 29109272](https://pubmed.ncbi.nlm.nih.gov/29109272/)). The LolCDE complex is explicitly identified as a member of this mechanotransmission superfamily: *"Homologs of MacB that do not form tripartite pumps, but share structural features underpinning mechanotransmission, include the LolCDE lipoprotein trafficking complex and FtsEX cell division signaling protein"* ([PMID: 29109272](https://pubmed.ncbi.nlm.nih.gov/29109272/)). The broader review of the family confirms that *"many MacB-like ABC transporters do not form tripartite pumps, but instead operate in diverse cellular processes including antibiotic sensing, cell division and lipoprotein trafficking"* ([PMID: 29892271](https://pubmed.ncbi.nlm.nih.gov/29892271/)). Mechanistically, this means reversible dimerization of the cytoplasmic LolD nucleotide-binding domains — driven by ATP binding/hydrolysis — is transmitted through the second transmembrane segment and coupling helix of LolC to open and close its periplasmic domain, powering the extraction of lipoprotein from the membrane rather than its passage through a pore.

### F003 — LolC and LolE have distinct, non-redundant roles; LolC is the LolA-docking subunit

Although LolC and LolE are sequence-similar and share an identical membrane topology — *"Both LolC and LolE were found to have four transmembrane segments with a large periplasmic loop exposed to the periplasm"* ([PMID: 19809197](https://pubmed.ncbi.nlm.nih.gov/19809197/)) — they are functionally differentiated. Sulfhydryl-reagent accessibility and lipoprotein-release-inhibition assays established that *"Inhibition of the release of lipoproteins by the sulfhydryl reagent supported a previous proposal that LolC and LolE have distinct functions"* ([PMID: 19809197](https://pubmed.ncbi.nlm.nih.gov/19809197/)). The distinguishing role of LolC is to serve as the **hand-off subunit to LolA**. The structure of LolA bound to lipoprotein shows that *"LolA, initially primed to receive lipoprotein by interaction with LolC, further opens to accommodate the three ligand acyl chains"* ([PMID: 36037338](https://pubmed.ncbi.nlm.nih.gov/36037338/)), demonstrating that LolC specifically primes and docks LolA to receive the cargo. Complementary photo-crosslinking work maps a central four-helix lipoprotein-binding cavity contributed jointly by the LolC/LolE periplasmic domains ([PMID: 38156779](https://pubmed.ncbi.nlm.nih.gov/38156779/)), positioning LolC at the interface where cargo is transferred out of the complex.

### F004 — The substrate is mature triacylated lipoprotein; selectivity is governed by the "+2 sorting rule"

The physiological substrate of LolCDE is a **mature, triacylated lipoprotein** anchored to the membrane by lipids attached to an N-terminal cysteine. Whether a given lipoprotein is extracted is determined by the residue at position 2, immediately following the lipidated cysteine. The classic study of retention signals states: *"The inner membrane retention signal, Asp at position 2 in combination with certain residues at position 3, functions as a Lol avoidance signal, i.e. the signal inhibits the recognition of lipoproteins by LolCDE that releases lipoproteins from the inner membrane"* ([PMID: 12896969](https://pubmed.ncbi.nlm.nih.gov/12896969/)). In other words, **Asp at +2 = inner-membrane retention (Lol avoidance); any other residue = release to the outer membrane.** Mechanistically the avoidance signal depends on a critical length of negative charge at residue 2. A separate prerequisite for release is complete N-acylation of the N-terminal cysteine (the Lnt-catalyzed step producing the triacylated form): *"We show here that the aminoacylation is essential for the Lol-dependent release of lipoproteins from membranes"* ([PMID: 12198129](https://pubmed.ncbi.nlm.nih.gov/12198129/)), and this requirement is independent of the sorting signal. LolC/LolE thus recognize a fully matured acyl anchor while reading the +2 position to decide whether to act.

### F005 — LolCDE (including LolC) is essential for viability and is a validated antibacterial target in *Pseudomonas*

Lipoprotein trafficking by the Lol machinery is indispensable for building the Gram-negative cell envelope. *"The LolCDE ABC transporter is the inner membrane component, which is essential for bacterial viability"* ([PMID: 29339384](https://pubmed.ncbi.nlm.nih.gov/29339384/)), and *"Lipoprotein transport from the inner to the outer membrane, carried out by the Lol machinery, is essential for the biogenesis of the Gram-negative cell envelope and, consequently, for bacterial viability"* — a statement established in *Pseudomonas aeruginosa* itself ([PMID: 32989085](https://pubmed.ncbi.nlm.nih.gov/32989085/)), lending direct genus-level support to the same role in *P. putida*. Consistent with essentiality, LolCDE is being actively exploited for antibiotic discovery, and LolC is directly implicated as part of the drug-binding machinery: *"Resistance to the pyrazole compound mapped to mutations in either LolC or LolE, components of the essential LolCDE transporter complex, which is required for trafficking of lipoproteins to the outer membrane"* ([PMID: 25733621](https://pubmed.ncbi.nlm.nih.gov/25733621/)). Additional chemotypes — the pyrrolopyrimidinedione G0507 ([PMID: 29339384](https://pubmed.ncbi.nlm.nih.gov/29339384/)), SMT-738 ([PMID: 38084954](https://pubmed.ncbi.nlm.nih.gov/38084954/)), and abaucin targeting the homodimeric LolDF variant ([PMID: 42091888](https://pubmed.ncbi.nlm.nih.gov/42091888/)) — reinforce the LolCDE/LolDF transporter as a tractable target.

### F006 — Sequence analysis confirms Q88KY5 is a genuine LolC ortholog (not LolE)

To resolve the LolC-vs-LolE ambiguity, full-length UniProt sequences were aligned by global Needleman–Wunsch alignment. *P. putida* KT2440 LolC (Q88KY5, 416 aa) shares **55.4% identity (205/370 aligned columns) with *E. coli* K-12 LolC (P0ADC3)** versus **49.3% (188/381) with *E. coli* LolE (P75958)**. For reference, the two *E. coli* paralogs LolC and LolE share only 43.1% identity with each other, so the clearly higher similarity of Q88KY5 to LolC identifies it as the LolC ortholog rather than a second LolE. Both the length (~416 aa, matching the ~400-aa LolC architecture) and the conserved domain set (LolCE_TM/IPR011925, FtsX/PF02687, MacB_PCD/IPR025857, ABC3_permease_C/IPR003838) match the *E. coli* LolC architecture, validating functional transfer from the *E. coli* model.

| Comparison | % identity | Aligned columns |
|---|---|---|
| Q88KY5 (P. putida LolC) vs *E. coli* LolC (P0ADC3) | **55.4%** | 205/370 |
| Q88KY5 (P. putida LolC) vs *E. coli* LolE (P75958) | 49.3% | 188/381 |
| *E. coli* LolC vs *E. coli* LolE (paralog baseline) | 43.1% | — |

### F007 — LolC acts at the inner-membrane/periplasm interface as the entry step of lipoprotein biogenesis-and-sorting

LolC's site of action places it at the culmination of a multi-stage lipoprotein maturation pathway. Pre-prolipoproteins are first exported across the inner membrane, predominantly by the Sec translocon: *"Lipoproteins are synthesized as precursors in the cytosol and then translocated across the inner membrane by the Sec translocon to the outer leaflet of the inner membrane, where lipoprotein precursors are processed to mature lipoproteins"* ([PMID: 20419407](https://pubmed.ncbi.nlm.nih.gov/20419407/)). At the outer leaflet of the inner membrane they are lipid-modified by Lgt (diacylglyceryl transferase), cleaved by signal peptidase II (LspA), and N-acylated by Lnt to give mature triacylated lipoproteins. Only then does the Lol pathway act: *"Fully modified lipoproteins that are destined to be anchored in the inner leaflet of the outer membrane (OM) are selected, transported and inserted by the Lol (lipoprotein outer membrane localization) pathway machinery, which consists of the inner-membrane (IM) ABC transporter-like LolCDE complex, the periplasmic LolA chaperone and the OM LolB lipoprotein receptor"* ([PMID: 24780125](https://pubmed.ncbi.nlm.nih.gov/24780125/)). LolC itself is an integral inner-membrane protein whose large periplasmic domain is *"exposed to the periplasm"* ([PMID: 19809197](https://pubmed.ncbi.nlm.nih.gov/19809197/)) — the compartment in which it recruits and primes LolA.

### F008 — LolC's periplasmic domain recruits and primes LolA via the "Hook" β-hairpin and "Pad" residues, nucleotide-independently

The precise structural basis for the LolC→LolA hand-off was revealed by a crystal structure of *E. coli* LolA bound to the LolC periplasmic domain. *"The structure reveals how a solvent-exposed β-hairpin loop (termed the 'Hook') and trio of surface residues (the 'Pad') of LolC are essential for recruiting LolA from the periplasm and priming it to receive lipoproteins"* ([PMID: 30012603](https://pubmed.ncbi.nlm.nih.gov/30012603/)). Importantly, this recruitment is decoupled from the ATPase cycle: *"Experiments with purified LolCDE complex demonstrate that association with LolA is independent of nucleotide binding and hydrolysis"* ([PMID: 30012603](https://pubmed.ncbi.nlm.nih.gov/30012603/)). Homology models based on MacB place the LolA-recruitment site at least ~50 Å above the inner membrane, at the distal tip of LolC's periplasmic domain — consistent with a two-step logic in which LolA docking (nucleotide-independent) precedes ATP-driven cargo extraction and transfer.

### F009 — *P. putida* KT2440 encodes a canonical contiguous *lolCDE* operon (PP_2154–PP_2155–PP_2156)

Genomic-neighborhood analysis confirms the physiological complex in the target organism. PP_2154 = *lolC* (Q88KY5, 416 aa, membrane permease) is immediately followed by **PP_2155 = *lolD*** (Q88KY4, 227 aa, Lipoprotein-releasing system ATP-binding protein LolD, EC 7.6.2.-) and **PP_2156 = *lolE*** (Q88KY3, 413 aa, Lipoprotein-releasing system permease). Both LolC and LolE carry the identical diagnostic domain set (LolCE_TM/IPR011925, ABC3_permease_C/IPR003838, MacB_PCD/IPR025857, Lipoprotein-release_system/IPR051447), consistent with a heterodimeric LolCDE transporter (one LolC, one LolE, two LolD) exactly as characterized in *E. coli*. The upstream gene PP_2153 is an unrelated PilZ-domain protein, indicating the operon boundary. This genomic organization independently confirms that *P. putida* assembles a canonical heterodimeric LolCDE machine.

| Locus | Gene | UniProt | Length | Product |
|---|---|---|---|---|
| PP_2153 | (pilZ) | — | — | PilZ-domain protein (unrelated; operon boundary) |
| **PP_2154** | **lolC** | **Q88KY5** | **416 aa** | **Membrane permease (LolA-docking subunit) — this protein** |
| PP_2155 | lolD | Q88KY4 | 227 aa | ABC ATP-binding protein LolD (EC 7.6.2.-) |
| PP_2156 | lolE | Q88KY3 | 413 aa | Membrane permease LolE |

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent picture of LolC as the **LolA-docking, cargo-priming transmembrane subunit** of the essential inner-membrane LolCDE machine. The Lol pathway can be summarized as a relay across the Gram-negative envelope:

```
   CYTOPLASM        INNER MEMBRANE          PERIPLASM              OUTER MEMBRANE
                    (outer leaflet)

  prolipoprotein --> [Sec] --> Lgt --> LspA --> Lnt --> mature triacylated lipoprotein
                                                             |
                                                    +2 residue check:
                                              Asp@2 = RETAINED (Lol avoidance)
                                              other = RELEASED
                                                             |
                                                             v
                          +---------------------------------------------+
                          |            LolCDE  (1 LolC : 1 LolE : 2 LolD)|
        ATP  ---->  [ LolD-LolD ]  nucleotide-binding domains (cytoplasm)|
        hydrolysis      |  mechanotransmission via TM2 + coupling helix  |
                        v                                                |
                   [ LolC ]  periplasmic domain  <-- "Hook" + "Pad"      |
                        |         recruits & primes LolA (ATP-independent)|
                        +------------------|--------------------------+
                                           v
                                    LolA (loaded) --- crosses periplasm --->  LolB --> OM inner leaflet
```

Two mechanistically separable steps define LolC's job. **Step 1 (nucleotide-independent):** LolC's distal periplasmic domain — through its Hook β-hairpin and Pad residues — captures free LolA from the periplasm and primes its hydrophobic cavity to accept an acyl chain (F008). This step does not require ATP. **Step 2 (ATP-driven):** ATP binding and hydrolysis by the paired LolD subunits in the cytoplasm drive their reversible dimerization; because LolC/LolE lack a central membrane pore, this movement is transmitted mechanically ("mechanotransmission", F002) up through the transmembrane helices to reconfigure the periplasmic domains, extracting the lipoprotein from the outer leaflet of the inner membrane and transferring it into the primed LolA. The overlapping lipoprotein- and LolC-binding sites within the LolA cavity (F003) provide the structural logic for this hand-off: as LolA accepts the acyl chains it displaces from LolC and departs.

Substrate selection is a two-filter process. First, only fully N-acylated (triacylated) lipoproteins are competent for release (F004) — an implicit quality-control checkpoint that couples maturation to sorting. Second, the +2 rule reads the residue adjacent to the lipidated cysteine: an aspartate (with the right +3 context) creates a negatively charged "avoidance signal" that prevents recognition, keeping the lipoprotein in the inner membrane, while any other residue permits extraction and delivery to the outer membrane (F004). LolC and LolE together form the four-helix cavity that binds the cargo, but LolC is uniquely responsible for the downstream LolA interface (F003).

Because this relay is the sole route for delivering lipoproteins (including critical outer-membrane-biogenesis factors) to the outer membrane, loss of LolCDE function collapses envelope integrity and kills the cell (F005). This essentiality, combined with the surface-exposed, druggable periplasmic domain, explains why LolC and LolE are focal points of multiple inhibitor programs and why resistance mutations map directly to them.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the findings |
|---|---|---|
| [20419407](https://pubmed.ncbi.nlm.nih.gov/20419407/) | *Sorting of bacterial lipoproteins to the outer membrane by the Lol system* | Defines the Lol machinery (LolCDE + LolA + LolB) and the upstream Sec-dependent export/IM processing (F001, F007) |
| [36228045](https://pubmed.ncbi.nlm.nih.gov/36228045/) | *Cryo-EM structures of LolCDE reveal the molecular mechanism of bacterial lipoprotein sorting* | Establishes LolCDE's initiating, selective-extraction role (F001) |
| [19809197](https://pubmed.ncbi.nlm.nih.gov/19809197/) | *Membrane topology and functional importance of the periplasmic region of LolCDE* | Subunit stoichiometry, LolC topology (4 TM + periplasmic loop), and distinct LolC/LolE functions (F001, F003, F007) |
| [29109272](https://pubmed.ncbi.nlm.nih.gov/29109272/) | *Structure and mechanotransmission mechanism of the MacB ABC transporter superfamily* | Places LolCDE in the mechanotransmission superfamily; no central substrate pore (F002) |
| [29892271](https://pubmed.ncbi.nlm.nih.gov/29892271/) | *Antibiotic Resistance Mediated by the MacB ABC Transporter Family* | Confirms lipoprotein trafficking as a MacB-superfamily function (F002) |
| [36037338](https://pubmed.ncbi.nlm.nih.gov/36037338/) | *Structural basis of lipoprotein recognition by the Lol chaperone LolA* | Shows LolA is primed by LolC before opening to accept acyl chains (F003) |
| [38156779](https://pubmed.ncbi.nlm.nih.gov/38156779/) | *Dissection of an ABC transporter LolCDE function analyzed by photo-crosslinking* | Maps the four-helix LolC/LolE cargo-binding cavity (F003) |
| [12896969](https://pubmed.ncbi.nlm.nih.gov/12896969/) | *Mechanism underlying inner membrane retention caused by Lol avoidance signals* | Establishes the +2 rule (Asp@2 = avoidance) (F004) |
| [12198129](https://pubmed.ncbi.nlm.nih.gov/12198129/) | *Aminoacylation of the N-terminal cysteine is essential for Lol-dependent release* | Shows mature N-acylation is a prerequisite for release (F004) |
| [29339384](https://pubmed.ncbi.nlm.nih.gov/29339384/) | *A Novel Inhibitor of the LolCDE ABC Transporter* | States LolCDE essentiality; G0507 inhibitor (F005) |
| [25733621](https://pubmed.ncbi.nlm.nih.gov/25733621/) | *Novel antibacterial targets revealed by a cell wall reporter assay* | Pyrazole resistance maps to LolC/LolE; validates LolC as target (F005) |
| [32989085](https://pubmed.ncbi.nlm.nih.gov/32989085/) | *Transcriptional Responses of P. aeruginosa to Lol inhibition* | Confirms Lol essentiality in *Pseudomonas* (genus-level transfer) (F005) |
| [24780125](https://pubmed.ncbi.nlm.nih.gov/24780125/) | *Secretion of bacterial lipoproteins: through the cytoplasmic membrane, the periplasm and beyond* | Describes the multi-stage biogenesis + Lol pathway (F007) |
| [30012603](https://pubmed.ncbi.nlm.nih.gov/30012603/) | *A structure of LolA bound to the LolC periplasmic domain* | Identifies the LolC "Hook" and "Pad"; nucleotide-independent LolA docking (F008) |
| [42091888](https://pubmed.ncbi.nlm.nih.gov/42091888/) | *Structure and druggable conformation of the homodimeric lipoprotein transporter of A. baumannii* | Structural/druggability context for LolCDE/LolDF; abaucin MOA (F005) |
| [38084954](https://pubmed.ncbi.nlm.nih.gov/38084954/) | *SMT-738: a small-molecule inhibitor of lipoprotein transport* | Additional validated LolCDE-targeting chemotype (F005) |

**Consistency of the evidence.** The evidence base is internally consistent and mutually reinforcing across biochemistry (topology, sulfhydryl accessibility, in vitro release assays), structural biology (cryo-EM of LolCDE, crystal structure of LolA–LolC), genetics (resistance and gain-of-function mutations mapping to LolC/LolE/LolD), and comparative genomics (operon structure, orthology). No cited study contradicts the model; the principal caveat is that nearly all mechanistic data derive from *E. coli*, with essentiality independently confirmed in *P. aeruginosa*.

---

## Limitations and Knowledge Gaps

1. **Model-organism inference.** No study in the knowledge base characterizes *P. putida* KT2440 LolC (Q88KY5) directly. The functional assignment rests on (a) strong orthology to *E. coli* LolC (55.4% identity; F006), (b) an intact *lolCDE* operon in KT2440 (F009), and (c) demonstrated Lol essentiality in the congeneric *P. aeruginosa* (F005). These provide high confidence but not direct experimental proof in *P. putida*.

2. **No experimental structure of the *Pseudomonas* complex.** The Hook/Pad LolA-recruitment elements and the four-helix cargo cavity are defined in *E. coli*. Whether *P. putida* LolC's periplasmic domain has identical Hook/Pad geometry has not been verified structurally (an AlphaFold model + comparison would close this gap).

3. **Substrate repertoire in *P. putida* unknown.** The +2 rule (F004) is an *E. coli* finding. The specific lipoprotein clientele of *P. putida* LolCDE, and whether the +2 avoidance rule operates identically in this species, have not been established.

4. **Quantitative kinetics/energetics unspecified.** The ATP-per-cargo stoichiometry and the precise coupling between LolD hydrolysis and LolC conformational change remain debated even in the *E. coli*/MacB literature (cf. the "molecular bellows" vs. hydrolysis-power-stroke discussion in [PMID: 33888866](https://pubmed.ncbi.nlm.nih.gov/33888866/)).

5. **Regulation in *P. putida*.** Whether the Rcs stress-response feedback that couples defective sorting to *lolA* induction in *E. coli* ([PMID: 22563052](https://pubmed.ncbi.nlm.nih.gov/22563052/)) operates in *P. putida* is unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Structural verification in silico.** Generate an AlphaFold2/3 model of *P. putida* LolC (Q88KY5) and superpose it on the *E. coli* LolC periplasmic domain (from [PMID: 30012603](https://pubmed.ncbi.nlm.nih.gov/30012603/)) to confirm conservation of the Hook β-hairpin and Pad residues, and model the LolCDE heterodimer (with Q88KY4/LolD and Q88KY3/LolE) to inspect the four-helix cargo cavity.

2. **Genetic essentiality test.** Attempt conditional depletion / CRISPRi knockdown of PP_2154 in *P. putida* KT2440 to confirm essentiality and observe envelope defects (outer-membrane permeabilization, lipoprotein mislocalization).

3. **Cargo mapping.** Use bioinformatic +2-rule scanning of the *P. putida* lipoproteome to predict LolCDE substrates vs. inner-membrane-retained lipoproteins, then validate a subset by membrane fractionation.

4. **In vitro reconstitution.** Purify the *P. putida* LolCDE complex and a cognate LolA, and reconstitute ATP-dependent lipoprotein release to test whether the *E. coli* mechanism (nucleotide-independent LolA docking; ATP-driven extraction) is conserved.

5. **Inhibitor cross-reactivity / drug discovery.** Test whether existing LolCDE inhibitors (G0507, pyrazoles, SMT-738) engage the *P. putida* complex, and use the model as a scaffold for structure-based design; map candidate resistance residues onto LolC/LolE.

6. **Regulatory circuit.** Test whether Lol dysfunction in *P. putida* triggers an Rcs-like envelope stress response modulating *lolA/lolCDE* expression.

---

## Conclusion

LolC (Q88KY5 / PP_2154) is the LolA-docking, cargo-priming transmembrane subunit of the essential inner-membrane ABC transporter **LolCDE** in *Pseudomonas putida* KT2440. It initiates the Lol pathway: reading matured, triacylated outer-membrane-destined lipoproteins (selected by the +2 "Asp = retain" rule), it uses MacB-family mechanotransmission — powered by ATP hydrolysis at the paired LolD subunits — to extract them from the outer leaflet of the inner membrane and hand them, via its Hook/Pad-bearing periplasmic domain, to the primed periplasmic chaperone LolA for delivery through LolB to the outer membrane. Its site of action is the inner-membrane/periplasm interface, its role is non-redundant with LolE, and its function is essential for cell-envelope biogenesis and viability, making it a validated antibacterial target.


## Artifacts

- [OpenScientist final report](lolC-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lolC-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:20419407
2. PMID:36228045
3. PMID:19809197
4. PMID:29109272
5. PMID:29892271
6. PMID:36037338
7. PMID:38156779
8. PMID:12896969
9. PMID:12198129
10. PMID:29339384
11. PMID:32989085
12. PMID:25733621
13. PMID:38084954
14. PMID:42091888
15. PMID:24780125
16. PMID:30012603
17. PMID:33888866
18. PMID:22563052