---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T15:28:47.198639'
end_time: '2026-07-18T16:07:23.017349'
duration_seconds: 2315.82
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_4797
  gene_symbol: PP_4797
  uniprot_accession: Q88DM8
  protein_description: 'RecName: Full=Lipoyl synthase {ECO:0008006|Google:ProtNLM};'
  gene_info: OrderedLocusNames=PP_4797 {ECO:0000313|EMBL:AAN70366.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Not specified in UniProt
  protein_domains: ArfA. (IPR005589); ArfA (PF03889)
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_4797-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_4797-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DM8
- **Protein Description:** RecName: Full=Lipoyl synthase {ECO:0008006|Google:ProtNLM};
- **Gene Information:** OrderedLocusNames=PP_4797 {ECO:0000313|EMBL:AAN70366.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ArfA. (IPR005589); ArfA (PF03889)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_4797" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_4797' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_4797** (gene ID: PP_4797, UniProt: Q88DM8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: PP_4797 (UniProt Q88DM8) in *Pseudomonas putida* KT2440

## Summary

**PP_4797 (UniProt Q88DM8) encodes ArfA (alternative ribosome-rescue factor A), a small, basic, intrinsically disordered protein that rescues bacterial ribosomes stalled on truncated "non-stop" mRNAs. It is *not* a lipoyl synthase.** The "Lipoyl synthase" name attached to this UniProt entry is a spurious machine-generated annotation (evidence code `ECO:0008006|Google:ProtNLM`) with no experimental support. It directly contradicts the protein's own domain content: Q88DM8 carries the ArfA domain signature (InterPro **IPR005589** / Pfam **PF03889**, "ArfA"), a family with a completely different fold and function from the radical-SAM enzyme lipoyl synthase. The genuine lipoyl synthase of *P. putida* KT2440 is a separate, neighboring gene, **lipA / PP_4800** (Q88DM5, 338 aa, EC 2.8.1.8) — the physical proximity of PP_4797 and PP_4800 in the genome is the most likely reason the ProtNLM machine-learning pipeline mistakenly transferred the "Lipoyl synthase" label onto PP_4797.

The primary function of ArfA is **co-translational quality control**. When a ribosome translates to the 3′ end of an mRNA that lacks an in-frame stop codon (a "non-stop" mRNA, produced by transcriptional errors, mRNA damage, or premature cleavage), it stalls with an empty A-site and cannot terminate normally, because the canonical release factors require a stop codon. ArfA recognizes this stalled state: its positively charged C-terminal region inserts into the vacant mRNA entry channel of the 30S subunit, effectively "sensing" the absence of downstream mRNA. Its N-terminal region then specifically recruits **release factor RF2** (not RF1) and, through an induced-fit conformational switch, positions RF2's catalytic GGQ motif in the peptidyl-transferase center to hydrolyze the peptidyl-tRNA bond. This releases the incomplete nascent polypeptide and frees the ribosome for recycling.

ArfA operates in the **cytoplasm**, on the **70S ribosome**, as one of three parallel and partially redundant bacterial ribosome-rescue systems. The *P. putida* KT2440 genome encodes the complete network: ArfA's partner RF2 (prfB/PP_1495), the RNase III (rnc/PP_1433) that regulates *arfA* expression, and the two redundant rescue pathways — tmRNA–SmpB *trans*-translation (smpB/PP_4733) and ArfB (PP_2946). ArfA's own synthesis is elegantly autoregulated: it is produced only from a non-stop mRNA generated by RNase III cleavage, and the resulting protein is tagged and degraded by the tmRNA system, so ArfA accumulates to functional levels only when *trans*-translation is overwhelmed or absent — a fail-safe backup design.

---

## Key Findings

### Finding 1 — PP_4797 (Q88DM8) is ArfA, not a lipoyl synthase

The UniProt entry Q88DM8 is annotated with the RecName "Lipoyl synthase," but this name carries the evidence code `ECO:0008006|Google:ProtNLM`, which designates a name produced automatically by Google's ProtNLM protein-language-model pipeline with no experimental or curated support. In contrast, the entry's domain architecture is definitive: it carries the ArfA domain signature **InterPro IPR005589 / Pfam PF03889 ("ArfA")**. These two annotations are mutually exclusive on biochemical grounds. Genuine lipoyl synthase (LipA) is a radical-SAM enzyme of roughly 300+ residues that harbors two [4Fe-4S] clusters coordinated by a characteristic CxxxCxxC cysteine motif and adopts an ordered (β/α) TIM-barrel-like radical-SAM fold. None of these features are present in Q88DM8. The ArfA family, by contrast, is a well-defined and taxonomically broad group across proteobacteria — the foundational survey by Schaub and colleagues analyzed 431 *arfA* coding sequences across the proteobacteria.

This finding is supported by the foundational description of ArfA as a distinct ribosome-rescue factor: *"Escherichia coli possesses an additional ribosome rescue pathway mediated by the ArfA peptide"* ([PMID: 22791716](https://pubmed.ncbi.nlm.nih.gov/22791716/)), which establishes ArfA as its own protein family consistent with the PF03889/IPR005589 signature on Q88DM8.

### Finding 2 — ArfA rescues stalled ribosomes by recruiting and activating release factor RF2

The mechanism of ArfA is among the best-characterized in bacterial translational quality control, resolved by multiple independent cryo-EM structures of the *E. coli* 70S ribosome bound to ArfA and RF2, all in the 3.0–3.4 Å range ([PMID: 27934701](https://pubmed.ncbi.nlm.nih.gov/27934701/), [PMID: 28077875](https://pubmed.ncbi.nlm.nih.gov/28077875/), [PMID: 28300532](https://pubmed.ncbi.nlm.nih.gov/28300532/), [PMID: 27906160](https://pubmed.ncbi.nlm.nih.gov/27906160/)). These structures show ArfA's positively charged C-terminus occupying the vacant mRNA entry channel/tunnel of the 30S subunit, downstream of the A site — the physical basis for "sensing" the absence of mRNA. ArfA's N-terminus specifically recruits RF2 (and not RF1) and, through an induced-fit conformational switch, positions RF2's catalytic **GGQ motif** in the peptidyl-transferase center to hydrolyze the peptidyl-tRNA and release the truncated nascent chain.

The structural work states the mechanism directly: ArfA *"binds within the ribosomal mRNA channel and substitutes for the absent stop codon in the A site by specifically recruiting release factor 2 (RF2), initially in a compact preaccommodated state"* ([PMID: 27934701](https://pubmed.ncbi.nlm.nih.gov/27934701/)). The substrate and functional outcome are likewise confirmed: ArfA *"rescues ribosomes stalled on truncated mRNAs by recruiting release factor RF2, which normally binds stop codons to catalyze peptide release"* ([PMID: 28300532](https://pubmed.ncbi.nlm.nih.gov/28300532/)). The structure by Huter et al. further shows that *"the positively charged C-terminal domain of ArfA anchors in the mRNA entry channel of the ribosome"* and that *"specific interactions between residues in the N-terminal domain of ArfA and RF2 help RF2 to adopt a catalytically competent conformation for peptide release"* ([PMID: 28077875](https://pubmed.ncbi.nlm.nih.gov/28077875/)). Kinetic work independently established that peptide release by ArfA/RF2 proceeds by an **induced-fit mechanism** and that methylation of the RF2 GGQ glutamine enhances the rate of release ([PMID: 26554029](https://pubmed.ncbi.nlm.nih.gov/26554029/)).

### Finding 3 — Sequence features of Q88DM8 match ArfA and exclude lipoyl synthase

The Q88DM8 protein is only **54 amino acids** long, with the sequence:

```
MSKKPKKHGPNKAKSIVAQPLFRCRQEQPNKGKGSYRREAFQSRDWEASYFLAA
```

The sequence is strongly basic. UniProt annotates a "Basic residues" compositional bias at positions 1–11 (`MSKKPKKHGPN`) and a "Basic and acidic residues" bias at positions 24–39, and residues 1–39 are predicted to be intrinsically disordered. Its cross-references confirm Pfam PF03889 (ArfA) and InterPro IPR005589 (ArfA). This combination — a very short, positively charged, disordered peptide — is diagnostic of ArfA, which folds only upon binding the negatively charged mRNA channel and rRNA of the ribosome. Lipoyl synthase, by comparison, is roughly 300+ residues with an ordered radical-SAM fold and Fe-S cluster cysteine motifs, none of which appear in Q88DM8. Moreover, the 54-residue length is fully consistent with ArfA's characteristic truncated (non-stop) product (see Finding 4).

### Finding 4 — ArfA is autoregulated through non-stop mRNA, RNase III, and tmRNA

ArfA synthesis is controlled by a remarkable negative-feedback design that couples its production to the very stress it responds to. In *E. coli*, **RNase III cleaves a hairpin within the *arfA* coding sequence** to produce a transcript that lacks a stop codon; the ribosome translating this non-stop message stalls and would ordinarily be rescued by *trans*-translation, which appends an ssrA (tmRNA) tag that marks ArfA for proteolytic degradation. As a result, functional ArfA accumulates only when the tmRNA system is overwhelmed or absent — precisely when the backup rescue capacity is needed. This is documented directly: *"RNase III cleaves a hairpin structure within the arfA-coding sequence to produce transcripts that lack stop codons. In the absence of tmRNA tagging, truncated ArfA chains are released from the ribosome"* ([PMID: 21435036](https://pubmed.ncbi.nlm.nih.gov/21435036/)).

The regulatory logic is general across proteobacteria: a survey of 431 *arfA* genes found that *"82.8% of the transcripts contain predicted hairpins in their 3′-coding regions"*, with RNase III cleavage confirmed in multiple gammaproteobacteria including *Haemophilus*, *Proteus*, *Vibrio*, and *Pasteurella* ([PMID: 22791716](https://pubmed.ncbi.nlm.nih.gov/22791716/)). Consistent with this, ArfA is essential for the viability of *E. coli* ΔssrA (tmRNA-null) cells, demonstrating functional redundancy with *trans*-translation, and a C-terminally truncated ArfAΔ18 (~55 aa) retains full activity. The 54-aa length of the *P. putida* ORF fits precisely this truncated, functional form.

### Finding 5 — PP_4797 is a bona fide ArfA ortholog sharing the conserved core motifs

Direct comparison of PP_4797 (Q88DM8, 54 aa) with the experimentally characterized *E. coli* ArfA (P36675/ARFA_ECOLI, 72 aa) confirms conservation of the diagnostic ArfA core motifs:

| ArfA core motif | *E. coli* ArfA (P36675) | *P. putida* PP_4797 (Q88DM8) |
|---|---|---|
| **PLFR** | HD**PLFR**QR | AQ**PLFR**CR |
| **KGKGSY** | N**KGKGSY**MRK | PN**KGKGSY**RRE |
| **WEAS** | RGN**WEAS**GKK | RD**WEAS**YFLAA |

Both proteins are short, strongly basic (the *P. putida* protein carries a net charge of approximately +9), and disordered. The *P. putida* annotated ORF (GenBank AAN70366) terminates roughly 9 residues after the conserved WEAS motif — very near the position where the functional truncated *E. coli* ArfAΔ18 (~55 aa) ends. This is consistent with the annotated product corresponding to the RNase III / non-stop truncated ArfA form. Together these features establish PP_4797 as a genuine ArfA ortholog, not a distant or ambiguous homolog.

### Finding 6 — The complete ArfA-dependent rescue network is present in the *P. putida* KT2440 genome

The functional relevance of ArfA in *P. putida* depends on the presence of its molecular partners. UniProt queries of *P. putida* KT2440 (taxid 160488) confirm that the organism encodes every component of the ArfA pathway and its redundant systems:

| Component | Role | Gene / locus | Accession |
|---|---|---|---|
| **ArfA** | Non-stop ribosome rescue factor (this protein) | PP_4797 | Q88DM8 |
| **RF2 (prfB)** | Release factor recruited by ArfA; catalyzes peptide release | PP_1495 | A0A140FW22 |
| **RNase III (rnc)** | Cleaves *arfA* hairpin to make non-stop mRNA (autoregulation) | PP_1433 | Q88MY5 |
| **SmpB** | Partner of tmRNA in *trans*-translation (parallel pathway) | PP_4733 | Q88DT6 |
| **ArfB** | Independent peptidyl-tRNA hydrolase rescue factor (EC 3.1.1.29) | PP_2946 | Q88IQ3 |

This establishes that PP_4797 (ArfA) operates within an intact **three-system ribosome-rescue network** in *P. putida* — trans-translation (tmRNA–SmpB), ArfA–RF2, and ArfB — mirroring the arrangement in *E. coli* and other proteobacteria.

### Finding 7 — The real lipoyl synthase in *P. putida* is a separate gene (lipA / PP_4800)

The misannotation is definitively resolved by identifying the true lipoyl synthase. *P. putida* KT2440 encodes a bona fide lipoyl synthase as a distinct protein: **Q88DM5 (lipA / PP_4800)**, 338 aa, **EC 2.8.1.8**, carrying the canonical radical-SAM Pfam **PF04055** domain and the lipoyl-synthase N-terminal domain **PF16881**. This is the enzyme that catalyzes sulfur insertion into the octanoyl moiety to form lipoyl groups on lipoyl-carrier proteins. By contrast, Q88DM8 (PP_4797) is 54 aa with only the ArfA domain (PF03889) and no EC number. Critically, the two genes are near-neighbors in the genome (PP_4797 vs PP_4800), which plausibly explains how the ProtNLM machine-learning pipeline mistakenly transferred the "Lipoyl synthase" name onto the adjacent ArfA gene. The two proteins are unrelated in sequence, size, fold, cofactor content, and function.

---

## Mechanistic Model / Interpretation

### The non-stop stalling problem

Bacterial mRNAs are short-lived and frequently damaged; it is estimated that 2–4% of all translation reactions terminate with a ribosome stalled on a non-stop mRNA. When a ribosome reaches the 3′ end of an mRNA lacking an in-frame stop codon, the A-site is empty of both codon and release factor. Normal termination cannot occur because RF1/RF2 recognition of the peptidyl-tRNA hydrolysis reaction is triggered by a stop codon in the A-site. The ribosome, the truncated mRNA, and the incomplete nascent chain are all trapped. Cells must rescue these complexes to recover ribosomes and to dispose of potentially toxic incomplete proteins.

### How ArfA solves it — a "stop-codon surrogate"

```
   Non-stop mRNA (no stop codon)
        5'———————————[empty A-site]   3'
                          |
   P-site  peptidyl-tRNA  |
                          v
        +-----------------------------+
        |      30S mRNA entry channel |  <-- ArfA C-terminus (basic, disordered)
        |   [ ArfA C-term inserts here]|      "senses" absence of mRNA
        +-----------------------------+
                          |
        ArfA N-terminus --+--> recruits RF2 (compact "preaccommodated" state)
                          |
        Induced-fit switch --> RF2 opens, GGQ motif reaches PTC
                          |
                          v
        Peptidyl-tRNA hydrolysis -> truncated peptide released
        70S ribosome recycled
```

ArfA acts as a **stop-codon surrogate**. Its positively charged, intrinsically disordered C-terminal tail threads into the empty mRNA entry channel of the 30S subunit — a location that is only accessible when no downstream mRNA is present, giving ArfA its specificity for non-stop complexes. Its N-terminal region binds RF2 and remodels it: RF2 arrives in a compact, catalytically inactive ("preaccommodated") conformation and is switched, via induced fit, into an open, active state in which its conserved GGQ motif is positioned next to the CCA-end of the P-site tRNA in the peptidyl-transferase center. RF2 then hydrolyzes the peptidyl-tRNA ester bond, releasing the incomplete polypeptide and permitting ribosome recycling. Notably, ArfA is strictly selective for RF2 over RF1 — a specificity dictated by the N-terminal ArfA/RF2 interface visualized in the cryo-EM structures.

### Autoregulation — a demand-driven backup

```
   arfA mRNA
      |
      v  RNase III cleaves internal hairpin
   non-stop arfA mRNA  -->  translated  -->  ribosome stalls
      |                                         |
      |                       +-----------------+----------------+
      |                 tmRNA present                     tmRNA absent /
      |                 (normal conditions)               overwhelmed (stress)
      |                       |                                  |
      v                       v                                  v
   ArfA is ssrA-tagged    ArfA degraded                   ArfA released intact
   by tmRNA               -> LOW ArfA                      -> FUNCTIONAL ArfA
                                                           accumulates -> rescue
```

ArfA's expression is coupled to the capacity of the *trans*-translation system through a negative feedback loop. Its transcript is deliberately rendered "non-stop" by RNase III cleavage of an internal coding-region hairpin. Under normal conditions, tmRNA–SmpB rescues the ribosome translating this non-stop *arfA* message and tags the ArfA protein for degradation, keeping ArfA levels low. When tmRNA is saturated or absent — exactly the condition under which the backup pathway is needed — ArfA escapes tagging, is released intact, and accumulates to functional levels. This makes ArfA a **demand-driven, fail-safe backup** to trans-translation.

### Localization and pathway placement

ArfA functions in the **cytoplasm**, directly on the translating **70S ribosome**. It is a component of the bacterial **translational quality-control / ribosome-rescue pathway**, operating in parallel with, and redundantly to, the tmRNA–SmpB *trans*-translation system and the ArfB peptidyl-tRNA hydrolase. All three systems are encoded in the *P. putida* KT2440 genome (Finding 6). ArfA has no metabolic-enzyme role; it does not catalyze a small-molecule reaction and, in particular, has nothing to do with lipoic acid biosynthesis, which is carried out by the separate PP_4800/LipA (Finding 7).

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [22791716](https://pubmed.ncbi.nlm.nih.gov/22791716/) | *Proteobacterial ArfA peptides are synthesized from non-stop messenger RNAs* | Establishes ArfA as a distinct proteobacterial rescue-factor family (supports Finding 1); documents the non-stop mRNA/hairpin regulatory mechanism as general across proteobacteria — 82.8% of 431 *arfA* transcripts have 3′ hairpins (supports Findings 4–5). |
| [27934701](https://pubmed.ncbi.nlm.nih.gov/27934701/) | *Translational termination without a stop codon* | Cryo-EM structure showing ArfA binds the mRNA channel, substitutes for the absent stop codon, and recruits RF2 in a compact preaccommodated state (core support for Finding 2). |
| [28300532](https://pubmed.ncbi.nlm.nih.gov/28300532/) | *Mechanism of ribosome rescue by ArfA and RF2* | Confirms substrate (truncated/non-stop mRNA-stalled ribosomes) and RF2-dependent peptide-release function (Finding 2). |
| [28077875](https://pubmed.ncbi.nlm.nih.gov/28077875/) | *Structural basis of co-translational quality control by ArfA and RF2 bound to ribosome* | Shows the positively charged ArfA C-terminus anchors in the mRNA entry channel and that N-terminal ArfA–RF2 interactions position RF2 for catalysis; defines RF2-over-RF1 specificity (Finding 2). |
| [27906160](https://pubmed.ncbi.nlm.nih.gov/27906160/) | *Mechanistic insights into the alternative translation termination by ArfA and RF2* | Cryo-EM of 70S•ArfA•RF2•non-stop mRNA•P-tRNA; C-terminal loop occupies the mRNA entry channel, RF2 GGQ positioned at the P-tRNA CCA end — the "stop-codon surrogate" model (Finding 2). |
| [26554029](https://pubmed.ncbi.nlm.nih.gov/26554029/) | *Peptide release... by an induced-fit mechanism* | Kinetic evidence that ArfA/RF2 peptide release proceeds by induced fit and is enhanced by RF2 GGQ methylation (Finding 2). |
| [21435036](https://pubmed.ncbi.nlm.nih.gov/21435036/) | *tmRNA regulates synthesis of the ArfA ribosome rescue factor* | Documents RNase III cleavage of the *arfA* hairpin and tmRNA-dependent degradation — the autoregulatory circuit (Finding 4). |
| [28629612](https://pubmed.ncbi.nlm.nih.gov/28629612/) | *Structural Basis for Ribosome Rescue in Bacteria* | Review placing ArfA–RF2 among the three bacterial rescue systems (tmRNA–SmpB, ArfA–RF2, ArfB); contextualizes Findings 2 and 6. |
| [33815344](https://pubmed.ncbi.nlm.nih.gov/33815344/) | *Ribosome Rescue Pathways in Bacteria* | Broad review of the rescue systems and their targeting of stalled ribosome, mRNA, and nascent chain (context for Findings 2, 6). |
| [31776341](https://pubmed.ncbi.nlm.nih.gov/31776341/) | *Release factor-dependent ribosome rescue by BrfA in Bacillus subtilis* | Shows a convergent RF2-recruiting rescue factor (BrfA) in a Gram-positive; ArfA and BrfA are distinct but use convergent strategies — highlights functional generality (context for Finding 2). |
| [30563899](https://pubmed.ncbi.nlm.nih.gov/30563899/) | *A New Mechanism for Ribosome Rescue Can Recruit RF1 or RF2* | Contextualizes ArfA's strict RF2 selectivity against other rescue mechanisms. |
| [34565314](https://pubmed.ncbi.nlm.nih.gov/34565314/) | *Diversity and Similarity of Termination and Ribosome Rescue...* | Positions ArfA•RF2 and ArfB among quality-control factors with peptidyl-tRNA hydrolase activity, distinct from canonical release factors (Findings 2, 6). |
| [41231940](https://pubmed.ncbi.nlm.nih.gov/41231940/) | *A cascade of structural rearrangements positions RF2 for polypeptide hydrolysis* | Single-molecule FRET on RF2 conformational landscape; supports the induced-fit activation model relevant to ArfA-mediated RF2 activation (Finding 2). |
| [39535229](https://pubmed.ncbi.nlm.nih.gov/39535229/) | *The ribosome-associated quality control pathway supports survival in the absence of non-stop rescue factors* | Demonstrates functional overlap/redundancy among rescue pathways including ArfA (context for Finding 6). |
| [39026760](https://pubmed.ncbi.nlm.nih.gov/39026760/) | *RqcH supports survival in the absence of non-stop ribosome rescue factors* | Further evidence of redundancy among the non-stop rescue systems (context for Finding 6). |

The evidence base is unusually strong for a functional-annotation question: the mechanism rests on **at least four independent high-resolution (3.0–3.4 Å) cryo-EM structures**, complementary **kinetic/biochemical** studies, and a **comparative-genomics survey** of 431 *arfA* genes. No paper in the literature set supports the "lipoyl synthase" annotation for this protein; all evidence converges on the ArfA identity.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of *P. putida* ArfA.** The functional assignment for PP_4797 is by strong orthology to *E. coli* ArfA (conserved PLFR/KGKGSY/WEAS motifs, identical domain signature, matching size, charge, and disorder), not by direct biochemistry in *P. putida* itself. All mechanistic structures and kinetics were obtained in *E. coli*. While the ArfA mechanism is deeply conserved across proteobacteria, species-specific details (e.g., exact RF2 interface residues, the precise RNase III cleavage site in *P. putida*) have not been experimentally verified in strain KT2440.

2. **Autoregulation confirmed only by inference in *P. putida*.** *P. putida* encodes RNase III (rnc/PP_1433) and the tmRNA–SmpB system (Finding 6), and the 54-aa ORF length is consistent with a truncated non-stop product. However, RNase III cleavage of the *P. putida arfA* hairpin and tmRNA tagging of *P. putida* ArfA have not been demonstrated directly.

3. **The exact full-length vs. truncated boundary.** The annotated ORF (54 aa, AAN70366) likely corresponds to the truncated non-stop product; the precise position of any hairpin and the length of a hypothetical full-length translation product were not experimentally mapped here.

4. **Phenotypic essentiality in *P. putida* not tested.** In *E. coli*, ArfA is essential in a ΔssrA background. Whether *arfA* (PP_4797) is similarly synthetically essential with tmRNA loss in *P. putida* KT2440 has not been assayed; this investigation was literature- and sequence/genomics-based, not wet-lab.

5. **Database annotation risk persists.** The ProtNLM "Lipoyl synthase" name remains attached to the public UniProt record; downstream tools that ingest this name uncritically will continue to propagate the error until corrected.

---

## Proposed Follow-up Experiments / Actions

1. **Submit a UniProt annotation correction.** File a report to UniProt flagging Q88DM8's "Lipoyl synthase" (ProtNLM) name as inconsistent with its PF03889/IPR005589 ArfA domain, and cite the neighboring lipA/PP_4800 (Q88DM5) as the true EC 2.8.1.8 lipoyl synthase. This is the single highest-value corrective action.

2. **Direct in vitro rescue assay.** Reconstitute *P. putida* ArfA (PP_4797) with purified *P. putida* 70S ribosomes, RF2 (PP_1495), a defined non-stop mRNA, and a P-site peptidyl-tRNA; measure ArfA/RF2-dependent peptide release and test RF2 vs RF1 selectivity, mirroring the *E. coli* kinetic assays ([PMID: 26554029](https://pubmed.ncbi.nlm.nih.gov/26554029/)).

3. **Genetic synthetic-lethality test.** Construct *P. putida* KT2440 Δ*ssrA* (ΔtmRNA), Δ*arfA* (ΔPP_4797), and the double mutant to test whether *arfA* becomes essential when *trans*-translation is removed, as in *E. coli*.

4. **Map the RNase III cleavage/autoregulation.** Use 5′/3′ RACE and RNase III (Δ*rnc*/PP_1433) mutants to determine whether the *P. putida arfA* transcript is processed into a non-stop mRNA and whether ArfA is tmRNA-tagged, confirming the conserved autoregulatory circuit.

5. **Structural confirmation (optional, high effort).** A cryo-EM structure of the *P. putida* 70S•ArfA•RF2 complex would provide species-specific confirmation and address whether the C-terminal channel-anchoring and N-terminal RF2 interface are conserved in detail.

6. **Bioinformatic sweep for similar ProtNLM errors.** Because gene-neighborhood proximity appears to have driven the misannotation, systematically screen other small ArfA-domain proteins (PF03889) in UniProt for spurious enzyme names transferred from neighboring metabolic genes.

---

## Conclusion

PP_4797 (UniProt Q88DM8) of *Pseudomonas putida* KT2440 is **ArfA (alternative ribosome-rescue factor A)**, a ~54-residue basic, intrinsically disordered peptide that rescues ribosomes stalled on non-stop mRNAs. Its C-terminus inserts into the vacant 30S mRNA entry channel to sense the missing stop codon, and its N-terminus specifically recruits and activates release factor RF2, which hydrolyzes the peptidyl-tRNA to release the truncated nascent chain. It functions in the cytoplasm on the 70S ribosome within the bacterial translational quality-control network, in parallel with and redundant to tmRNA–SmpB trans-translation and ArfB, and is autoregulated via RNase III-generated non-stop mRNA and tmRNA-dependent degradation. The "Lipoyl synthase" name in UniProt is a spurious machine-generated (ProtNLM) misannotation; the genuine lipoyl synthase is the separate neighboring gene lipA/PP_4800 (Q88DM5, EC 2.8.1.8).


## Artifacts

- [OpenScientist final report](PP_4797-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_4797-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:22791716
2. PMID:27934701
3. PMID:28077875
4. PMID:28300532
5. PMID:27906160
6. PMID:26554029
7. PMID:21435036