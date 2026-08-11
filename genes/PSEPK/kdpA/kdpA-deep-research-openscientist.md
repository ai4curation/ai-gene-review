---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-11T03:46:39.302509'
end_time: '2026-08-11T04:01:57.578385'
duration_seconds: 918.28
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: kdpA
  gene_symbol: kdpA
  uniprot_accession: Q88FD7
  protein_description: 'RecName: Full=Potassium-transporting ATPase potassium-binding
    subunit {ECO:0000255|HAMAP-Rule:MF_00275}; AltName: Full=ATP phosphohydrolase
    [potassium-transporting] A chain {ECO:0000255|HAMAP-Rule:MF_00275}; AltName: Full=Potassium-binding
    and translocating subunit A {ECO:0000255|HAMAP-Rule:MF_00275}; AltName: Full=Potassium-translocating
    ATPase A chain {ECO:0000255|HAMAP-Rule:MF_00275};'
  gene_info: Name=kdpA {ECO:0000255|HAMAP-Rule:MF_00275}; OrderedLocusNames=PP_4161;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the KdpA family. {ECO:0000255|HAMAP-
  protein_domains: KdpA. (IPR004623); KdpA (PF03814)
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
citation_count: 21
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: kdpA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: kdpA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FD7
- **Protein Description:** RecName: Full=Potassium-transporting ATPase potassium-binding subunit {ECO:0000255|HAMAP-Rule:MF_00275}; AltName: Full=ATP phosphohydrolase [potassium-transporting] A chain {ECO:0000255|HAMAP-Rule:MF_00275}; AltName: Full=Potassium-binding and translocating subunit A {ECO:0000255|HAMAP-Rule:MF_00275}; AltName: Full=Potassium-translocating ATPase A chain {ECO:0000255|HAMAP-Rule:MF_00275};
- **Gene Information:** Name=kdpA {ECO:0000255|HAMAP-Rule:MF_00275}; OrderedLocusNames=PP_4161;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the KdpA family. {ECO:0000255|HAMAP-
- **Key Domains:** KdpA. (IPR004623); KdpA (PF03814)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "kdpA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'kdpA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **kdpA** (gene ID: kdpA, UniProt: Q88FD7) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *kdpA* (Q88FD7, PP_4161) in *Pseudomonas putida* KT2440

## Summary

**kdpA (Q88FD7, ordered locus PP_4161) encodes KdpA, the potassium-binding and translocating "A" subunit of the inner-membrane KdpFABC high-affinity K⁺ import pump of *Pseudomonas putida* KT2440.** KdpA is a polytopic integral membrane protein that is *not itself an enzyme* — it contains no ATP-hydrolyzing or phosphorylation machinery. Instead, it is a **channel-like ion-recognition subunit**: it selectively binds K⁺ from the periplasmic side of the plasma membrane at a KcsA-like selectivity filter and hands the ion off, through an intersubunit tunnel, to the catalytic P-type ATPase subunit KdpB, which supplies the energy for uptake through ATP hydrolysis. In effect, KdpA provides the *substrate specificity* (K⁺) while KdpB provides the *power stroke*, an unusual division of labor that makes KdpFABC a "split-site" type Ia P-type ATPase.

The **substrate is the potassium ion (K⁺)**, and the physiological function of the complex is **high-affinity potassium scavenging and turgor/osmotic homeostasis**. The *kdpFABC* operon (of which *kdpA* is a member) is not constitutively expressed; it is switched on specifically under **severe K⁺ limitation or osmotic/salt upshift** by the **KdpD/KdpE two-component signal-transduction system**, which senses the stress and transcriptionally activates the operon. KdpA carries out its function **in the plasma (inner) membrane**, recognizing K⁺ from the periplasmic face and delivering it to the cytoplasm.

The functional assignment for the *P. putida* protein specifically is strongly supported. Q88FD7 is a confident ortholog of the biochemically and structurally characterized *Escherichia coli* KdpA (**54% amino-acid identity**), it retains the four-MPM channel topology and the KcsA-derived **TNGGG selectivity-filter glycine motif**, the experimentally validated *E. coli* filter glycine G232 is positionally conserved (P. putida G236), and the gene sits in an intact *kdpABCD* operon in the KT2440 genome alongside its cognate KdpD/KdpE regulatory system. The report below lays out each line of evidence, the mechanistic model that unifies them, the supporting literature, and the residual gaps (chiefly the absence of *P. putida*-specific biochemical studies).

---

## Key Findings

### Finding 1 — KdpA is the K⁺-binding, channel-like subunit of the KdpFABC pump

The core identity of the protein is unambiguous. UniProt assigns Q88FD7 (PP_4161) to the **KdpA family** as the "Potassium-transporting ATPase potassium-binding subunit" under HAMAP-Rule MF_00275. This family assignment is grounded in decades of structural and biochemical work on the *E. coli* orthologue. The 2.9-Å crystal structure of the *E. coli* KdpFABC complex directly established the architecture: the complex has "one channel-like subunit (KdpA) belonging to the superfamily of potassium transporters and another pump-like subunit (KdpB) belonging to the superfamily of P-type ATPases" ([PMID: 28636601](https://pubmed.ncbi.nlm.nih.gov/28636601/)). More recent cryo-EM work adds the functional detail that "**KdpA is a channel-like subunit with a selectivity filter that binds potassium from the periplasm**" ([PMID: 41929109](https://pubmed.ncbi.nlm.nih.gov/41929109/)).

The critical mechanistic point is that KdpA and KdpB have distinct roles: KdpA recognizes and translocates the ion, KdpB hydrolyzes ATP. KdpA alone has no catalytic activity — it is the *specificity* determinant of the pump, analogous to the pore module of a potassium channel, but harnessed to an active transporter rather than working as a passive channel.

### Finding 2 — KdpA is evolutionarily derived from 2TM K⁺ channels, and K⁺ selectivity is set by conserved filter glycines

KdpA's channel-like character is not merely a structural analogy — it reflects genuine evolutionary descent. Bioinformatic analysis of KdpA sequences showed that "the transmembrane KdpA subunit of the high affinity K(+)-translocating P-type Kdp-ATPase is evolutionarily derived from the superfamily of **2TM-type K(+) channels** in bacteria" ([PMID: 10620285](https://pubmed.ncbi.nlm.nih.gov/10620285/)). Whereas a canonical KcsA-type channel is a tetramer of four identical two-transmembrane (2TM) subunits, KdpA fuses four such **membrane–pore–membrane (MPM)** units into a *single* polypeptide, reproducing the fourfold pseudosymmetric selectivity filter within one chain.

The selectivity filter itself is built from conserved glycine motifs homologous to the GYG signature of K⁺ channels. Mutagenesis pins these residues to ion selectivity directly:

| Mutation (E. coli KdpA) | Consequence | Reference |
|---|---|---|
| G232D | Reduced K⁺ affinity; broadened specificity to Na⁺, Li⁺, H⁺; loss of Rb⁺ discrimination | [PMID: 10920013](https://pubmed.ncbi.nlm.nih.gov/10920013/) |
| G345 / G470 substitutions | Altered ion selectivity of the whole KdpFABC complex | [PMID: 15292155](https://pubmed.ncbi.nlm.nih.gov/15292155/) |

The G232 residue "is the first in a highly conserved GGG motif that was aligned with the GYG sequence of the selectivity filter (P- or H5-loop) of K(+) channels" ([PMID: 10920013](https://pubmed.ncbi.nlm.nih.gov/10920013/)). Replacing the glycines at positions 345 and 470 — members of putative selectivity-filter regions III and IV — "alters the ion selectivity of the KdpFABC complex" ([PMID: 15292155](https://pubmed.ncbi.nlm.nih.gov/15292155/)). These experiments establish that KdpA's filter glycines are the physical determinants of what the pump transports.

### Finding 3 — Mechanism: K⁺ enters at the KdpA filter and is delivered to KdpB through an intersubunit tunnel, energized by ATP hydrolysis

The most striking mechanistic feature of KdpFABC is that ion binding and ATP hydrolysis occur on *different subunits*, which requires a physical conduit between them. The *E. coli* crystal structure revealed exactly that: "a **protein-embedded tunnel** runs between these potassium and water sites and a helix controlling the cytoplasmic gate of KdpA is linked to the phosphorylation domain of KdpB" ([PMID: 28636601](https://pubmed.ncbi.nlm.nih.gov/28636601/)). K⁺ captured at the KdpA selectivity filter is therefore routed through this buried tunnel to a canonical cation site in KdpB, while a KdpA gating helix communicates mechanically with KdpB's catalytic phosphorylation domain.

This design is described as a **hybrid mechanism**: the pump "features a unique hybrid mechanism combining a channel-like selectivity filter in KdpA with the ATP-driven transport functionality of KdpB" ([PMID: 41384914](https://pubmed.ncbi.nlm.nih.gov/41384914/)). Coupling residues at the KdpA–KdpB interface link ATP hydrolysis to ion movement, ensuring that the channel-like filter does not leak K⁺ but instead moves it only in step with the catalytic cycle of KdpB.

### Finding 4 — *kdpA* is expressed within the *kdpFABC* operon, induced by K⁺ limitation/osmotic stress via KdpD/KdpE

KdpA is not produced constitutively. It is encoded within the *kdpFABC* operon, "an inducible high-affinity K⁺ transporter that is synthesised under conditions of severe K⁺ limitation or osmotic upshift" ([PMID: 17536175](https://pubmed.ncbi.nlm.nih.gov/17536175/)). Expression is controlled by a dedicated two-component system: "The **KdpD/KdpE two-component system** of *Escherichia coli* activates the expression of the *kdpFABC* operon encoding the high-affinity K⁺ uptake system KdpFABC in response to K⁺ limitation or salt stress" ([PMID: 20146748](https://pubmed.ncbi.nlm.nih.gov/20146748/)). KdpD is the membrane sensor histidine kinase; upon stress it phosphorylates the response regulator KdpE, which binds the operon promoter and drives transcription.

This regulatory logic frames KdpA's physiological niche: it is an **emergency, high-affinity K⁺-scavenging system** deployed when the cell's constitutive, lower-affinity K⁺ uptake routes (e.g., Trk/Kup) can no longer maintain intracellular potassium, turgor, membrane potential, and cytoplasmic pH. Notably, the precise molecular stimulus sensed by KdpD remains debated: quantitative work argues that a reduction in turgor is *not* the direct trigger, and that KdpD responds most effectively to K⁺-limiting conditions in the medium ([PMID: 18245296](https://pubmed.ncbi.nlm.nih.gov/18245296/)).

### Finding 5 — The *P. putida* protein itself retains the channel-like topology and selectivity-filter signature

Crucially, the above features are not merely inferred from *E. coli* — they are directly present in Q88FD7. The 564-residue *P. putida* KdpA sequence has **10 predicted transmembrane helices**, consistent with the four-MPM topology of the K⁺-transporter superfamily. The conserved selectivity-filter signature **TNGGG** is present at residues 234–238 (the GGG corresponding to the *E. coli* KdpA G232 whose mutation broadens specificity), and additional pore-loop signatures mark the other three filter regions (GGVGAG ~378; TSGSANNGS ~465; SNGS/MHDS ~347–357). UniProt GO annotations for the protein are internally consistent with this: **plasma membrane** (GO:0005886), **potassium ion binding** (GO:0030955), and **P-type K⁺ transmembrane transporter activity** (GO:0008556). Cross-references anchor the identity across databases: RefSeq WP_010954929.1, KEGG ppu:PP_4161, Pfam PF03814, InterPro IPR004623.

### Finding 6 — PP_4161 lies in an intact *kdpABCD(E)* operon in the KT2440 genome

The genomic context confirms that the *P. putida* protein functions in the same molecular machine as its *E. coli* counterpart. In the KT2440 genome the genes form a contiguous cluster:

| Locus | Gene | KEGG KO | Product | EC |
|---|---|---|---|---|
| PP_4161 | *kdpA* | K01546 | K⁺-binding subunit | — |
| PP_4160 | *kdpB* | K01547 | P-type ATPase, ATP-binding subunit | 7.2.2.6 |
| PP_4159 | *kdpC* | K01548 | Assembly/coupling subunit | — |
| PP_4158 | *kdpD* | K07646 | Two-component sensor histidine kinase | 2.7.13.3 |

This *kdpA-kdpB-kdpC-kdpD* arrangement matches the canonical *kdpFABC* + *kdpDE* architecture, so PP_4161 has both its structural partners (KdpB/KdpC) and its regulatory system (KdpD/KdpE) encoded alongside it — exactly what is required for a functional, inducible high-affinity K⁺ pump.

### Finding 7 — Q88FD7 is a confident ortholog of *E. coli* KdpA (54% identity) with exact conservation of the functional filter glycine

Direct sequence alignment cements the transfer of functional knowledge from *E. coli* to *P. putida*. A Needleman–Wunsch global alignment (BLOSUM62) of P. putida KdpA (Q88FD7, 564 aa) against *E. coli* K-12 KdpA (P03959, 557 aa) yields **302 identical positions = 54.4% identity, 69.9% similarity** over a 566-column alignment. Most importantly, the functionally critical region aligns residue-for-residue: the P. putida TNGGG filter (residues 234–238) maps directly onto the *E. coli* TNGGG (230–234), and the **experimentally characterized *E. coli* KdpA G232 aligns exactly to P. putida G236**, both within the conserved GGG motif. Because that exact residue's mutation is known to broaden the pump's ion specificity, its conservation in *P. putida* is strong evidence that the KT2440 protein shares the same K⁺-selectivity mechanism.

### Finding 8 — KdpFABC is an electrogenic type Ia P-type ATPase running a Post-Albers cycle with ion transport and ATPase sites on separate subunits

Finally, biophysical work defines the kinetic and thermodynamic character of the pump that KdpA is part of. Electrophysiological and kinetic studies on purified *E. coli* KdpFABC show it is "a **unique type Ia P-type ATPase**, because it separates the sites of ATP hydrolysis and ion transport on two different subunits" and imports K⁺ **electrogenically** ([PMID: 23930894](https://pubmed.ncbi.nlm.nih.gov/23930894/)). Time-resolved caged-ATP experiments established that it follows a **Post-Albers (E1/E2) reaction cycle** ([PMID: 24766073](https://pubmed.ncbi.nlm.nih.gov/24766073/)), with an apparent ATP-binding affinity of ~70 µM and a rate-limiting E1P→P-E2 conformational transition of ~1.7 s⁻¹ at 20 °C that is K⁺-independent (K⁺ binds in the membrane domain after phosphorylation). The electrogenic transport has been modeled quantitatively as an ATP-dependent pump ([PMID: 38950825](https://pubmed.ncbi.nlm.nih.gov/38950825/)). These data place KdpA's ion-handling role firmly within a classical P-type ATPase pumping cycle — but one in which the ion-binding half is delegated to a channel-derived subunit.

---

## Mechanistic Model / Interpretation

Putting the findings together yields a coherent, structurally grounded model of how KdpA works and why it matters to *P. putida*.

**Architecture and division of labor.** KdpFABC is a heterotetramer of four subunits — KdpF (a small stabilizing peptide), KdpA (the K⁺-recognition subunit), KdpB (the catalytic P-type ATPase), and KdpC (assembly/coupling). KdpA is the evolutionary descendant of a KcsA-like K⁺ channel, folded into a single chain of four MPM repeats that reconstitute a fourfold selectivity filter. This is the "specificity module." KdpB is a classical P-type ATPase with the canonical actuator (A), nucleotide-binding (N), and phosphorylation (P) cytoplasmic domains — the "engine." The unusual feature of KdpFABC, relative to all other P-type ATPases, is that **the ion is bound and released by a different subunit (KdpA) than the one that hydrolyzes ATP (KdpB)**.

```
   PERIPLASM  (K+ source, low external [K+])
        |
        v   K+ enters and is selected by the
   [ KdpA ]  KcsA-like selectivity filter
   filter    (TNGGG glycines; E.coli G232 = P.putida G236)
        |
        |   intersubunit protein-embedded TUNNEL
        v   (K+ + water pathway; gating helix links to KdpB P-domain)
   [ KdpB ]  canonical P-type ATPase cation site
   A-N-P     ATP hydrolysis -> aspartyl-phosphate (E1P)
   domains   Post-Albers cycle drives release of K+
        |
        v
   CYTOPLASM  (K+ delivered; turgor / Vm / pH restored)

   Regulation:  low [K+] or osmotic upshift
                --> KdpD (sensor kinase) autophosphorylates
                --> KdpE~P (response regulator) activates
                --> transcription of kdpFABC operon
```

**Transport cycle.** In the Post-Albers scheme, K⁺ from the periplasm is captured at the KdpA filter and threaded through the buried tunnel toward KdpB. ATP binds KdpB (apparent Kd ~70 µM) and phosphorylates its conserved aspartate to form E1P; the rate-limiting E1P→P-E2 conformational change (~1.7 s⁻¹ at 20 °C) then drives the coupled release of K⁺ into the cytoplasm. The gating helix of KdpA, physically linked to the KdpB phosphorylation domain, is the mechanical relay that couples catalysis in KdpB to gating in KdpA, so that K⁺ moves only in register with the ATPase cycle rather than leaking through the channel-like filter. The net reaction is electrogenic K⁺ import against a steep concentration gradient — precisely the capability the cell needs when external K⁺ is scarce.

**Physiological role and localization.** KdpA does its job in the **plasma (inner) membrane**, recognizing K⁺ at the periplasmic face and delivering it to the cytoplasm. The whole system is an **inducible, high-affinity, emergency K⁺ scavenger**. Under normal conditions, constitutive transporters suffice, and *kdpFABC* is silent. When K⁺ becomes limiting or the cell suffers an osmotic/salt upshift, KdpD/KdpE turns the operon on, and KdpFABC restores intracellular K⁺ to maintain turgor pressure, membrane potential, and cytoplasmic pH homeostasis. For *P. putida* KT2440 — a metabolically versatile soil bacterium that experiences fluctuating water and ion availability in the rhizosphere — such a scavenging system is a plausible and important stress-adaptation module, even though the KT2440 protein has not itself been studied biochemically.

**Confidence in the transfer to *P. putida*.** The assignment for Q88FD7 rests on three independent, mutually reinforcing lines of evidence: (1) family/domain assignment (KdpA family, Pfam PF03814, InterPro IPR004623, HAMAP MF_00275); (2) 54% global identity to the structurally and mutationally characterized *E. coli* KdpA, including residue-for-residue conservation of the TNGGG filter and the functionally validated G232→G236 glycine; and (3) genomic context — an intact *kdpABCD* operon with the cognate KdpD/KdpE regulator. Together these justify high-confidence transfer of the *E. coli* mechanistic model to the *P. putida* protein.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [28636601](https://pubmed.ncbi.nlm.nih.gov/28636601/) | *Crystal structure of the potassium-importing KdpFABC membrane complex* | Defines KdpA as the channel-like K⁺ subunit and KdpB as the P-type ATPase; describes the intersubunit tunnel and gating-helix/P-domain link (Findings 1, 3) |
| [41929109](https://pubmed.ncbi.nlm.nih.gov/41929109/) | *Lipids are essential for potassium transport by KdpFABC* | States KdpA binds K⁺ from the periplasm via a selectivity filter (Finding 1) |
| [10620285](https://pubmed.ncbi.nlm.nih.gov/10620285/) | *Does KdpA have a structure similar to K⁺ channels?* | Establishes evolutionary derivation of KdpA from 2TM K⁺ channels (Finding 2) |
| [10920013](https://pubmed.ncbi.nlm.nih.gov/10920013/) | *Replacement of glycine 232 by aspartic acid in KdpA broadens ion specificity* | Mutagenesis identifying the GGG filter glycine (G232) as a K⁺-selectivity determinant (Findings 2, 7) |
| [15292155](https://pubmed.ncbi.nlm.nih.gov/15292155/) | *Substitutions in selectivity filter regions III and IV in KdpA alter ion selectivity* | Confirms KdpA filter residues (G345/G470) govern the pump's ion selectivity (Finding 2) |
| [41384914](https://pubmed.ncbi.nlm.nih.gov/41384914/) | *On the mechanism of K⁺ transport through the inter-subunit tunnel of KdpFABC* | Describes the hybrid channel/ATPase mechanism and interface coupling (Finding 3) |
| [17536175](https://pubmed.ncbi.nlm.nih.gov/17536175/) | *The Kdp-ATPase system and its regulation* | Establishes the operon as an inducible high-affinity K⁺ transporter under K⁺ limitation/osmotic upshift (Finding 4) |
| [20146748](https://pubmed.ncbi.nlm.nih.gov/20146748/) | *The complexity of the "simple" two-component system KdpD/KdpE* | KdpD/KdpE activates the operon in response to K⁺ limitation/salt stress (Finding 4) |
| [18245296](https://pubmed.ncbi.nlm.nih.gov/18245296/) | *Reduction of turgor is not the stimulus for the sensor kinase KdpD* | Refines the regulatory model: turgor reduction is not the direct KdpD stimulus (Finding 4) |
| [23930894](https://pubmed.ncbi.nlm.nih.gov/23930894/) | *Mechanistic analysis of the pump cycle of KdpFABC* | Type Ia P-type ATPase separating ATP hydrolysis and ion transport on two subunits; electrogenic K⁺ import (Finding 8) |
| [24766073](https://pubmed.ncbi.nlm.nih.gov/24766073/) | *Role of protons in the pump cycle of KdpFABC* | Establishes Post-Albers cycle and kinetic parameters (~70 µM ATP; 1.7 s⁻¹ rate-limiting step) (Finding 8) |
| [38950825](https://pubmed.ncbi.nlm.nih.gov/38950825/) | *Numerical model for electrogenic transport by KdpFABC* | Quantitative electrogenic-pump model (Finding 8) |

Additional structural and regulatory studies in the reviewed literature reinforce this picture without altering it: cryo-EM structures of KdpFABC and analyses of the K⁺ conduction pathway ([PMID: 34272288](https://pubmed.ncbi.nlm.nih.gov/34272288/), [PMID: 30478378](https://pubmed.ncbi.nlm.nih.gov/30478378/), [PMID: 40654642](https://pubmed.ncbi.nlm.nih.gov/40654642/), [PMID: 41259220](https://pubmed.ncbi.nlm.nih.gov/41259220/)); studies of serine-phosphorylation regulation and an inhibited E1 off-cycle state ([PMID: 32955430](https://pubmed.ncbi.nlm.nih.gov/32955430/), [PMID: 36255052](https://pubmed.ncbi.nlm.nih.gov/36255052/)); intersubunit coupling analysis ([PMID: 34429416](https://pubmed.ncbi.nlm.nih.gov/34429416/)); a KdpFABC review ([PMID: 31259644](https://pubmed.ncbi.nlm.nih.gov/31259644/)); and a protocol for reconstituting P-type ATPases including KdpFABC in liposomes ([PMID: 26695029](https://pubmed.ncbi.nlm.nih.gov/26695029/)).

**Independence of evidence.** It is worth emphasizing that the annotation does not rest on any single source. The structural biology (crystallography, cryo-EM), the classical mutagenesis, the electrophysiology, the regulatory genetics, and the sequence/genomic bioinformatics are independent methodologies that converge on the same conclusion. The one caveat — addressed next — is that nearly all of the *experimental* evidence comes from *E. coli*, and is transferred to *P. putida* by orthology.

---

## Limitations and Knowledge Gaps

1. **No *P. putida*-specific biochemistry.** All direct experimental characterization (crystal/cryo-EM structures, mutagenesis, transport kinetics, regulation) has been performed on the *E. coli* KdpFABC system. For *P. putida* KT2440 specifically, the assignment is inferential — based on 54% orthology, domain conservation, and genomic context. No purified *P. putida* KdpA transport assay, structure, or knockout phenotype was identified.

2. **Filter-residue numbering is homology-based.** The identification of the *P. putida* selectivity-filter residues (e.g., G236 as the counterpart of *E. coli* G232) comes from sequence alignment, not from a solved *P. putida* structure. While the alignment is unambiguous in the filter region, the exact side-chain geometry has not been experimentally confirmed for Q88FD7.

3. **KdpF is not separately annotated in the KT2440 locus survey.** The genomic analysis identified *kdpA-B-C-D* as contiguous, but the very small *kdpF* peptide (which stabilizes the complex in *E. coli*) was not explicitly confirmed in the KT2440 context; its presence should be verified.

4. **Regulatory stimulus is still debated even in *E. coli*.** Work on KdpD indicates that turgor reduction is not the direct stimulus ([PMID: 18245296](https://pubmed.ncbi.nlm.nih.gov/18245296/)), and the precise molecular signal remains contested. The regulatory model for *P. putida* is therefore transferred with the same open question.

5. **Post-translational regulation not assessed in *P. putida*.** Serine-phosphorylation control of KdpFABC ([PMID: 32955430](https://pubmed.ncbi.nlm.nih.gov/32955430/)) and off-cycle inhibited states ([PMID: 36255052](https://pubmed.ncbi.nlm.nih.gov/36255052/)) are established in *E. coli*; whether *P. putida* KdpB carries the analogous regulatory serine was not determined here.

6. **Stoichiometry and coupling ratio not independently verified for the ortholog.** The electrogenic, ATP-coupled uptake stoichiometry is from *E. coli* studies; the coupling ratio for the *P. putida* pump is assumed conserved.

---

## Proposed Follow-up Experiments / Actions

1. **Confirm *kdpF* and the full operon structure.** Re-examine the KT2440 genome annotation to verify the presence and position of *kdpF* and the *kdpE* response-regulator gene, completing the *kdpFABCDE* map.

2. **Structural prediction and filter validation.** Generate an AlphaFold model of Q88FD7 (and the KdpFABC complex by orthology-guided modeling) and confirm that G236 and the other predicted filter glycines (regions II–IV) form a fourfold selectivity filter superimposable on the *E. coli* KdpA structure (PMID 28636601).

3. **Heterologous complementation.** Test whether *P. putida* *kdpABC* restores high-affinity K⁺ uptake in an *E. coli* kdp-deletion strain, providing direct functional evidence for the ortholog.

4. **Expression/induction assay in *P. putida*.** Measure *kdpFABC* transcription in KT2440 under K⁺ limitation and osmotic/salt upshift (qRT-PCR or reporter fusion) to confirm KdpD/KdpE-dependent induction in this organism.

5. **Targeted mutagenesis of G236.** Recapitulate the *E. coli* G232D experiment in *P. putida* KdpA (G236D) and assay for the predicted loss of K⁺ affinity and broadened cation specificity, directly validating the filter mechanism in the ortholog.

6. **Transport kinetics of purified complex.** Reconstitute purified *P. putida* KdpFABC into proteoliposomes (as done for *E. coli*, PMID 26695029) and measure ATP-dependent, electrogenic K⁺ transport to confirm the conserved Post-Albers, split-site mechanism.

---

## Conclusion

*kdpA* (Q88FD7, PP_4161) encodes **KdpA, the potassium-binding "A" subunit of the inner-membrane KdpFABC high-affinity K⁺ import pump** of *Pseudomonas putida* KT2440. It is a **channel-like, non-catalytic subunit** — evolutionarily derived from 2TM K⁺ channels — that selectively binds **K⁺** at a KcsA-like selectivity filter on the periplasmic face and delivers it, via an intersubunit tunnel, to the catalytic P-type ATPase subunit **KdpB**, which powers electrogenic uptake by ATP hydrolysis through a Post-Albers cycle. The *kdpFABC* operon is an **inducible, high-affinity K⁺-scavenging system** switched on under K⁺ limitation or osmotic/salt stress by the **KdpD/KdpE two-component system** to maintain turgor, membrane potential, and pH homeostasis. The assignment for this specific ortholog is strongly supported by 54% identity to the experimentally characterized *E. coli* KdpA, conservation of the mutationally validated filter glycine (E. coli G232 = P. putida G236), retention of the four-MPM channel topology, and an intact *kdpABCD* operon in the KT2440 genome.


## Artifacts

- [OpenScientist final report](kdpA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](kdpA-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:28636601
2. PMID:41929109
3. PMID:10620285
4. PMID:10920013
5. PMID:15292155
6. PMID:41384914
7. PMID:17536175
8. PMID:20146748
9. PMID:18245296
10. PMID:23930894
11. PMID:24766073
12. PMID:38950825
13. PMID:34272288
14. PMID:30478378
15. PMID:40654642
16. PMID:41259220
17. PMID:32955430
18. PMID:36255052
19. PMID:34429416
20. PMID:31259644
21. PMID:26695029