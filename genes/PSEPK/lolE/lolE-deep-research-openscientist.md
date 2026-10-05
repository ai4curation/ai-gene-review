---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:13:29.722030'
end_time: '2026-09-01T04:06:32.931290'
duration_seconds: 6783.21
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lolE
  gene_symbol: lolE
  uniprot_accession: Q88KY3
  protein_description: 'SubName: Full=Lipoprotein releasing system, permease protein
    {ECO:0000313|EMBL:AAN67769.1};'
  gene_info: Name=lolE {ECO:0000313|EMBL:AAN67769.1}; OrderedLocusNames=PP_2156 {ECO:0000313|EMBL:AAN67769.1};
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
citation_count: 15
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: lolE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lolE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KY3
- **Protein Description:** SubName: Full=Lipoprotein releasing system, permease protein {ECO:0000313|EMBL:AAN67769.1};
- **Gene Information:** Name=lolE {ECO:0000313|EMBL:AAN67769.1}; OrderedLocusNames=PP_2156 {ECO:0000313|EMBL:AAN67769.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ABC-4 integral membrane protein family.
- **Key Domains:** ABC3_permease_C. (IPR003838); Lipoprotein-release_system. (IPR051447); LolCE_TM. (IPR011925); MacB_PCD. (IPR025857); FtsX (PF02687)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lolE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lolE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lolE** (gene ID: lolE, UniProt: Q88KY3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: LolE (Q88KY3 / PP_2156) in *Pseudomonas putida* KT2440

## Summary

**LolE (UniProt Q88KY3; locus PP_2156) is one of the two integral inner‑membrane permease subunits of the LolCDE ABC transporter — the "lipoprotein‑releasing system" that performs the first committed, ATP‑dependent step of the Lol pathway that sorts lipoproteins to the outer membrane of Gram‑negative bacteria.** It is not itself a lipoprotein; the UniProt "Lipoprotein" descriptor refers to its *substrate*. LolE is a polytopic membrane protein of 413 residues with four transmembrane segments and a large periplasmic loop that carries the conserved cargo‑binding cleft engaging the lipoprotein's acyl anchor. Together with its paralog LolC (PP_2154) and two copies of the nucleotide‑binding ATPase LolD (PP_2155), LolE extrudes mature, triacylated, outer‑membrane‑destined lipoproteins from the outer leaflet of the inner membrane and hands them to the periplasmic chaperone LolA for delivery to LolB at the outer membrane.

Mechanistically, LolCDE belongs to the **MacB/FtsX ABC transporter superfamily**, which operates by "mechanotransmission": the transmembrane domain contains no solute channel and instead relays ATP‑driven conformational changes from the cytoplasmic LolD ATPase across the membrane to the periplasmic domain, physically levering the lipoprotein out of the bilayer. Substrate specificity is governed by an avoidance signal — lipoproteins bearing aspartate at position +2 relative to the lipidated N‑terminal cysteine are *not* released and are retained in the inner membrane, whereas outer‑membrane‑destined lipoproteins are extruded. The transporter is essential for outer‑membrane biogenesis and bacterial viability, and it is a validated antibacterial target, with multiple chemical scaffolds mapping resistance mutations directly to the LolC/LolE subunits.

The functional assignment of *P. putida* Q88KY3 is anchored by strong orthology to the experimentally characterized *Escherichia coli* system (~39% identity to *E. coli* LolE), a complete syntenic *lolC–lolD–lolE* operon at PP_2154–PP_2156, conserved diagnostic domains (FtsX PF02687, MacB_PCD, ABC3_permease_C, LolCE_TM), and a bioinformatically confirmed topology matching the experimentally determined LolC/LolE architecture. Direct biochemical and structural characterization derives from *E. coli* and, for lipoprotein sorting fidelity, *Pseudomonas aeruginosa*; there is no *P. putida*‑specific functional study of Q88KY3. The annotation is nevertheless of high confidence given the convergent orthology, synteny, and domain evidence.

---

## Key Findings

### F001 — LolE is a permease subunit of the LolCDE lipoprotein‑release ABC transporter

Q88KY3 is annotated by UniProt as "Lipoprotein releasing system, permease protein," gene *lolE*, and assigned to the ABC‑4 integral membrane protein family. Its domain architecture — ABC3_permease_C (IPR003838), LolCE_TM (IPR011925), the MacB periplasmic core domain (IPR025857/MacB_PCD), and FtsX (PF02687) — is diagnostic of the LolC/LolE class of transporter permeases. In the experimentally characterized *E. coli* system, the LolCDE complex is composed of one copy each of the membrane subunits LolC and LolE and two copies of the nucleotide‑binding ATPase LolD ([PMID: 19809197](https://pubmed.ncbi.nlm.nih.gov/19809197/)). The complex releases outer‑membrane‑specific lipoproteins from the inner membrane in an ATP‑dependent manner, forming a soluble complex between the lipoprotein and the periplasmic chaperone LolA ([PMID: 18218629](https://pubmed.ncbi.nlm.nih.gov/18218629/)). As stated directly in the primary literature: *"An ATP binding cassette transporter LolCDE complex releases lipoproteins from the inner membrane of Escherichia coli in an ATP-dependent manner, leading to the formation of a complex between a lipoprotein and a periplasmic chaperone, LolA"* and *"the LolCDE complex catalyzes the extrusion of lipoproteins anchored to the outer leaflet of the inner membrane"* ([PMID: 18218629](https://pubmed.ncbi.nlm.nih.gov/18218629/)). LolE is therefore a transporter subunit — specifically one of the two integral‑membrane permease components — of this machine.

### F002 — The periplasmic domain of LolE carries the conserved substrate‑binding cleft

PhoA‑fusion topology mapping showed that both LolC and LolE possess four transmembrane segments and a large periplasmic loop, and that sulfhydryl‑accessibility differences and release‑inhibition data indicate LolC and LolE have *distinct* functions despite their similar topology ([PMID: 19809197](https://pubmed.ncbi.nlm.nih.gov/19809197/)). Recent cryo‑EM structures of LolCDE captured with three different lipoprotein substrates (Lpp, Pal, and LolB) revealed that *"the lipoproteins make a sequence-independent but structurally conserved interaction with a cleft on the surface of the periplasmic domain of LolE that promotes efficient transport"* ([PMID: 41557797](https://pubmed.ncbi.nlm.nih.gov/41557797/)). This directly assigns the conserved cargo‑binding cleft to LolE (rather than LolC), providing a structural basis for the functional division of labor between the two paralogous subunits. Full transport‑cycle cryo‑EM structures of *E. coli* LolCDE (apo, lipoprotein‑, LolA‑, ADP‑, and AMP‑PNP‑bound) further resolve how the transporter sorts and moves its cargo ([PMID: 33782615](https://pubmed.ncbi.nlm.nih.gov/33782615/)).

### F003 — Substrate specificity: OM‑destined lipoproteins are released; the Asp+2 "Lol avoidance signal" is excluded

The LolCDE complex mediates release of outer‑membrane‑specific lipoproteins from the inner membrane, whereas inner‑membrane‑specific lipoproteins that carry aspartate at position +2 are *not* released: *"the inner membrane-specific lipoproteins possessing Asp at position 2 are not released by LolCDE because it functions as a LolCDE avoidance signal, causing the retention of these lipoproteins in the inner membrane"* ([PMID: 20419407](https://pubmed.ncbi.nlm.nih.gov/20419407/)). This "+2 rule" is the central determinant of lipoprotein sorting fidelity in the Lol system. Independent support comes from Gram‑positive systems, where Asp at position +2 tightens anchoring of lipoproteins to the cytoplasmic membrane ([PMID: 28901671](https://pubmed.ncbi.nlm.nih.gov/28901671/)), and *"Lpp possessing aspartate (Asp) at position +2 are not translocated because it functions as a LolCDE avoidance signal"* ([PMID: 28901671](https://pubmed.ncbi.nlm.nih.gov/28901671/)). The species that *is* released forms a water‑soluble lipoprotein–LolA complex that crosses the periplasm to LolB at the outer membrane.

### F004 — Mechanism: MacB‑superfamily "mechanotransmission," not a solute channel

LolCDE belongs to the MacB/FtsX ABC transporter superfamily. Structural studies of the archetype MacB established that *"The MacB transmembrane domain lacks a central cavity through which substrates could be passed, but instead conveys conformational changes from one side of the membrane to the other, a process we term mechanotransmission"* ([PMID: 29109272](https://pubmed.ncbi.nlm.nih.gov/29109272/)). Crucially, that work explicitly names LolCDE as a homolog sharing these features: *"Homologs of MacB that do not form tripartite pumps, but share structural features underpinning mechanotransmission, include the LolCDE lipoprotein trafficking complex and FtsEX cell division signaling protein"* ([PMID: 29109272](https://pubmed.ncbi.nlm.nih.gov/29109272/)). The energizing cycle works because *"reversible dimerization of the nucleotide binding domains drives opening and closing of the MacB periplasmic domains via concerted movements of the second transmembrane segment and major coupling helix"* ([PMID: 29109272](https://pubmed.ncbi.nlm.nih.gov/29109272/)). Applied to LolE, ATP binding and hydrolysis at the LolD ATPase dimer are transmitted through LolE's transmembrane helices to lever its periplasmic domain — and the bound lipoprotein — up and out of the membrane. Full transport‑cycle cryo‑EM of *E. coli* LolCDE corroborates this ATP‑coupled conformational cycling ([PMID: 33782615](https://pubmed.ncbi.nlm.nih.gov/33782615/)). Consistent with this, Q88KY3 carries the diagnostic FtsX (PF02687) and MacB_PCD periplasmic‑core domains, and the operon's LolD (PP_2155; EC 7.6.2.–; 227 aa) supplies the ATPase.

### F005 — Genomic context: Q88KY3 is the LolE of a complete syntenic *lolCDE* operon in *P. putida* KT2440

UniProt/KEGG records for *P. putida* KT2440 show three consecutive loci that constitute the transporter: **lolC = PP_2154** (Q88KY5, 416 aa), **lolD = PP_2155** (Q88KY4, 227 aa; "Lipoprotein‑releasing system ATP‑binding protein LolD," EC 7.6.2.–), and **lolE = PP_2156** (Q88KY3, 413 aa, permease). Q88KY3 is 413 aa, assigned to the ABC‑4 integral membrane protein family (LolC/E subfamily), and localized to the inner membrane as a multi‑pass membrane protein (UniProt keywords: Cell membrane, Membrane, Transmembrane helix, Transport). Global pairwise alignment gives ~38.9% identity to *E. coli* LolE (P75958) and ~37.6% to *E. coli* LolC (P0ADC3), consistent with LolC and LolE being ancient paralogs arising from gene duplication. The syntenic operon order (*lolC–lolD–lolE*) mirrors *E. coli* and cleanly resolves the ortholog assignment of Q88KY3 as LolE rather than LolC.

| Locus | UniProt | Length | Role | *E. coli* ortholog |
|-------|---------|--------|------|--------------------|
| PP_2154 (*lolC*) | Q88KY5 | 416 aa | Membrane permease subunit; primes LolA | LolC |
| PP_2155 (*lolD*) | Q88KY4 | 227 aa | Nucleotide‑binding ATPase (2 copies); EC 7.6.2.– | LolD |
| **PP_2156 (*lolE*)** | **Q88KY3** | **413 aa** | **Membrane permease subunit; binds cargo** | **LolE** |

### F006 — LolCDE is essential and a validated antibacterial target

The outer membrane is an essential structural component of Gram‑negative bacteria, and *"The LolCDE ABC transporter is the inner membrane component, which is essential for bacterial viability"* ([PMID: 29339384](https://pubmed.ncbi.nlm.nih.gov/29339384/)). Chemical‑genetic validation directly implicates LolE: pyridineimidazole inhibitors of lipoprotein trafficking select resistance mutations that *"map to either the LolC or LolE protein of the LolCDE transporter complex"* and block LolA‑dependent release of the lipoprotein Lpp ([PMID: 25583975](https://pubmed.ncbi.nlm.nih.gov/25583975/)). An independent pyrrolopyrimidinedione inhibitor (G0507) also targets LolCDE ([PMID: 29339384](https://pubmed.ncbi.nlm.nih.gov/29339384/)). Importantly for *P. putida*, the pathway's essentiality and druggability extend to pseudomonads: in *Pseudomonas aeruginosa*, *"Lipoprotein transport from the inner to the outer membrane, carried out by the Lol machinery, is essential for the biogenesis of the Gram-negative cell envelope and, consequently, for bacterial viability"* ([PMID: 32989085](https://pubmed.ncbi.nlm.nih.gov/32989085/)), and a small‑molecule Lol inhibitor triggers a defined transcriptional stress response.

### F007 — Upstream: LolE acts on fully mature, triacylated lipoproteins from the Sec/Lgt/LspA/Lnt maturation pathway

LolE engages a specific, fully processed substrate. Bacterial lipoproteins are synthesized as preprolipoproteins and exported across the inner membrane via the Sec (or Tat) translocon; on exit they are recognized by phosphatidylglycerol::prolipoprotein diacylglyceryl transferase (Lgt), which adds a diacylglyceryl group to the invariant lipobox cysteine: *"Following synthesis, preprolipoproteins are transported through the cytoplasmic membrane via the Sec or Tat translocon. As they exit the transport machinery, they are recognized by a phosphatidylglycerol::prolipoprotein diacylglyceryl transferase (Lgt), which converts them to prolipoproteins by adding a diacylglyceryl group to the sulfhydryl side chain of the invariant Cys"* ([PMID: 32490790](https://pubmed.ncbi.nlm.nih.gov/32490790/)). Lipoprotein‑specific signal peptidase II (LspA) then cleaves the signal peptide, and in Gram‑negatives apolipoprotein N‑acyltransferase (Lnt) adds the third, N‑linked acyl chain to yield the triacylated lipoprotein ([PMID: 15186407](https://pubmed.ncbi.nlm.nih.gov/15186407/)). This mature, triacylated species — anchored by its N‑terminal acyl moiety in the outer leaflet of the inner membrane — is exactly what LolCDE engages: LolA accepts *"triacylated lipoproteins from the inner membrane transporter LolCDE"* ([PMID: 36037338](https://pubmed.ncbi.nlm.nih.gov/36037338/)).

### F008 — Downstream and division of labor: LolE binds cargo, LolC primes LolA, LolA ferries to LolB

Within LolCDE the two membrane subunits are functionally distinct ([PMID: 19809197](https://pubmed.ncbi.nlm.nih.gov/19809197/)). Cryo‑EM assigns the conserved cargo‑binding cleft to LolE's periplasmic domain ([PMID: 41557797](https://pubmed.ncbi.nlm.nih.gov/41557797/)), whereas LolA is recruited and primed by LolC: *"The structure highlights how LolA, initially primed to receive lipoprotein by interaction with LolC, further opens to accommodate the three ligand acyl chains in a precise conformation within its cavity"* ([PMID: 36037338](https://pubmed.ncbi.nlm.nih.gov/36037338/)). After release, a water‑soluble lipoprotein–LolA complex traverses the periplasm: *"This complex traverses the hydrophilic periplasm to reach the outer membrane, where LolB accepts a lipoprotein from LolA and then catalyzes its incorporation into the inner leaflet of the outer membrane"* ([PMID: 20419407](https://pubmed.ncbi.nlm.nih.gov/20419407/)). LolA's ability to carry structurally diverse cargo arises because *"LolA forms extensive interactions with the acyl chains but not with any residue of the cargo"* ([PMID: 36037338](https://pubmed.ncbi.nlm.nih.gov/36037338/)) — mirroring LolE's sequence‑independent recognition of the acyl anchor. LolB homologs are present in γ‑proteobacteria, the clade that includes *P. putida* ([PMID: 39149330](https://pubmed.ncbi.nlm.nih.gov/39149330/)).

### F009 — Bioinformatic topology confirms a polytopic inner‑membrane protein with a large periplasmic loop

Kyte–Doolittle hydropathy analysis (window 19, threshold 1.6) of the 413‑aa Q88KY3 sequence predicts approximately four hydrophobic transmembrane‑like segments (≈ residues 21–53, 267–299, 318–347, 378–401) separated by a very large hydrophilic stretch of ~214 residues (≈ residues 53–267). This matches the experimentally determined LolC/LolE topology of *"four transmembrane segments with a large periplasmic loop exposed to the periplasm"* ([PMID: 19809197](https://pubmed.ncbi.nlm.nih.gov/19809197/)). UniProt independently annotates Q88KY3 as a multi‑pass inner‑membrane protein, and the large loop corresponds to the MacB_PCD/periplasmic domain (IPR025857) that hosts the conserved lipoprotein‑binding cleft ([PMID: 41557797](https://pubmed.ncbi.nlm.nih.gov/41557797/)).

### F010 — LolE is the transporter, not a lipoprotein: no lipobox is present

Sequence inspection of Q88KY3 shows the N‑terminus (MFRPLPIFIGARYTRAKRRNHF…) contains no lipobox motif ([LVIMFATG][ASTVILGF][GAS]C) within the first ~35 residues; the first cysteine occurs at position 384, deep within a C‑terminal transmembrane helix rather than at a processed N‑terminal signal‑peptide/lipobox junction. LolE is therefore *not* a lipidated lipoprotein cargo but a polytopic inner‑membrane transporter subunit (four TM segments + large periplasmic loop; [PMID: 19809197](https://pubmed.ncbi.nlm.nih.gov/19809197/)) whose substrates are triacylated lipoproteins ([PMID: 20419407](https://pubmed.ncbi.nlm.nih.gov/20419407/), [PMID: 36037338](https://pubmed.ncbi.nlm.nih.gov/36037338/)). The UniProt "Lipoprotein" keyword denotes its substrate/function, not modification of the protein itself — an important clarification that prevents misannotation.

---

## Mechanistic Model / Interpretation

The findings converge on a single, coherent picture: **LolE is the cargo‑binding permease subunit of the LolCDE inner‑membrane ABC transporter that launches lipoproteins into the Lol sorting pathway.** The full relay can be depicted as follows:

```
   CYTOPLASM        INNER MEMBRANE (IM)          PERIPLASM              OUTER MEMBRANE (OM)
 ┌───────────┐   ┌────────────────────────┐   ┌──────────────┐      ┌────────────────────┐
 │ Ribosome  │   │  Sec/Tat translocon    │   │              │      │                    │
 │ pre-pro-  │──▶│  Lgt → LspA → Lnt      │   │              │      │                    │
 │ lipoprot. │   │  = triacyl lipoprotein  │   │              │      │                    │
 └───────────┘   │  (outer IM leaflet)     │   │              │      │                    │
                 │          │              │   │              │      │                    │
                 │          ▼              │   │              │      │                    │
                 │   ┌───────────────┐     │   │              │      │                    │
   ATP  ────────▶│   │ LolC │ LolE   │◀───── acyl anchor bound │      │                    │
   │             │   │  ▲       ▲cleft│    │  by LolE cleft    │      │                    │
   ▼             │   │ LolD  LolD (x2)│    │              │      │                    │
 ADP+Pi ◀────────│   └───────────────┘     │   │              │      │                    │
 (mechano-       │      LolCDE             │   │  LolA ━━━━━▶ LolA━━▶ LolB ──▶ OM inner    │
  transmission)  │  (MacB superfamily,     │   │ (primed by   │      │      leaflet        │
                 │   no solute channel)    │   │  LolC)       │      │                    │
                 └────────────────────────┘   └──────────────┘      └────────────────────┘

 Avoidance rule:  Asp at position +2  ⇒  NOT released  ⇒  lipoprotein RETAINED in IM
```

**Localization.** LolE performs its function at the **inner (cytoplasmic) membrane and its periplasmic face**. Its four transmembrane helices anchor it in the bilayer; its large periplasmic loop projects into the periplasm where the cargo‑binding cleft and the interfaces with LolA/LolC reside; and its ATPase partner LolD sits on the cytoplasmic face.

**Catalytic / transport logic.** LolE does not form a solute channel. Instead, ATP binding and hydrolysis at the LolD dimer drive reversible nucleotide‑binding‑domain dimerization, which is transmitted through LolE's transmembrane helix 2 and coupling helix to swing the periplasmic domain — the essence of MacB‑superfamily mechanotransmission. During this cycle the periplasmic cleft of LolE grips the triacyl anchor of the lipoprotein and physically extracts it from the outer leaflet of the inner membrane. The extracted lipoprotein is then transferred to LolA, which has been pre‑positioned by LolC.

**Specificity logic.** Recognition is *sequence‑independent* — LolE and LolA both engage the conserved acyl chains rather than the polypeptide, which is why a single transporter can sort structurally diverse lipoproteins. Fidelity is imposed negatively, by the **Asp+2 avoidance signal**: lipoproteins destined to remain in the inner membrane carry Asp at position +2, which prevents LolCDE from releasing them.

**Division of labor within the complex.** Although LolC and LolE are paralogs with near‑identical four‑TM/large‑periplasmic‑loop topology, they are functionally specialized: **LolE binds the cargo** (conserved periplasmic cleft), while **LolC primes and recruits the LolA chaperone**. This asymmetry, first inferred from sulfhydryl‑accessibility and inhibition data, is now confirmed by cryo‑EM.

For *P. putida* KT2440 specifically, all direct mechanistic evidence is inherited from *E. coli* (and, for sorting fidelity in pseudomonads, *P. aeruginosa*), but the inference is exceptionally strong: Q88KY3 sits in a complete syntenic *lolC–lolD–lolE* operon, shows ~39% identity to *E. coli* LolE, carries every diagnostic domain (FtsX, MacB_PCD, ABC3_permease_C, LolCE_TM), and has a bioinformatically confirmed topology matching the experimental LolC/LolE architecture.

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|------|-----------------|--------------------------------|
| [19809197](https://pubmed.ncbi.nlm.nih.gov/19809197/) | Membrane topology & periplasmic region of LolCDE | Defines LolE as one of two membrane permease subunits (with LolC + 2× LolD); establishes 4‑TM/large‑periplasmic‑loop topology; shows LolC/LolE are functionally distinct |
| [18218629](https://pubmed.ncbi.nlm.nih.gov/18218629/) | Single cycle of LolCDE→LolA ligand transfer | Establishes ATP‑dependent extrusion of lipoproteins from the IM outer leaflet and lipoprotein–LolA complex formation |
| [41557797](https://pubmed.ncbi.nlm.nih.gov/41557797/) | Liganded LolCDE structures | Cryo‑EM assigns the conserved, sequence‑independent cargo‑binding cleft to LolE's periplasmic domain |
| [33782615](https://pubmed.ncbi.nlm.nih.gov/33782615/) | LolCDE full transport‑cycle cryo‑EM | Apo/lipoprotein/LolA/ADP/AMP‑PNP structures resolve the ATP‑coupled sorting and transport mechanism |
| [20419407](https://pubmed.ncbi.nlm.nih.gov/20419407/) | Sorting of lipoproteins by the Lol system | States substrate (OM‑specific lipoproteins), the Asp+2 avoidance signal, and the downstream LolA→LolB→OM route |
| [28901671](https://pubmed.ncbi.nlm.nih.gov/28901671/) | Asp tightens staphylococcal lipoprotein anchoring | Independent confirmation of the Asp+2 avoidance/retention signal |
| [29109272](https://pubmed.ncbi.nlm.nih.gov/29109272/) | MacB superfamily mechanotransmission | Defines the channel‑free mechanotransmission mechanism and explicitly names LolCDE as a member |
| [29339384](https://pubmed.ncbi.nlm.nih.gov/29339384/) | Novel LolCDE inhibitor (G0507) | LolCDE is essential for viability and druggable |
| [25583975](https://pubmed.ncbi.nlm.nih.gov/25583975/) | Pyridineimidazole Lol inhibitors | Resistance mutations map directly to LolC/LolE — chemical‑genetic proof LolE is on the release pathway |
| [32989085](https://pubmed.ncbi.nlm.nih.gov/32989085/) | *P. aeruginosa* Lol inhibition transcriptomics | Confirms Lol essentiality/druggability in a pseudomonad |
| [32490790](https://pubmed.ncbi.nlm.nih.gov/32490790/) | Lgt in lipoprotein maturation | Describes Sec/Tat export + Lgt lipidation generating LolE's substrate |
| [15186407](https://pubmed.ncbi.nlm.nih.gov/15186407/) | LspA & lipoprotein processing | Establishes LspA cleavage step in maturation preceding Lol handling |
| [36037338](https://pubmed.ncbi.nlm.nih.gov/36037338/) | Structural basis of LolA recognition | Confirms triacylated substrate; LolC primes LolA; acyl‑chain (not sequence) recognition |
| [30992347](https://pubmed.ncbi.nlm.nih.gov/30992347/) | *E. coli* LolCDE sorts lipoproteins in *P. aeruginosa* | Shows the LolCDE sorting logic operates faithfully in a *Pseudomonas* host |

The evidence base is internally consistent. The strongest, most direct evidence (cryo‑EM structures, topology mapping, chemical genetics) all derives from *E. coli*; the *Pseudomonas*‑specific papers ([PMID: 32989085](https://pubmed.ncbi.nlm.nih.gov/32989085/), [PMID: 30992347](https://pubmed.ncbi.nlm.nih.gov/30992347/)) establish that the same machinery and sorting rules operate in pseudomonads, bridging the inference to *P. putida*.

---

## Limitations and Knowledge Gaps

1. **No *P. putida*‑specific functional study.** All mechanistic, structural, and biochemical data derive from *E. coli*; sorting‑fidelity data extend to *P. aeruginosa*. The assignment for Q88KY3 rests on orthology, synteny, and domain conservation — strong but inferential. No published gene‑knockout, essentiality assay, or structure exists specifically for PP_2156.

2. **Substrate repertoire in *P. putida* is uncharacterized.** The specific set of outer‑membrane lipoproteins that LolCDE sorts in *P. putida* KT2440, and whether the Asp+2 rule holds with identical stringency in this organism, have not been experimentally defined.

3. **LolC vs. LolE functional asymmetry is inferred, not measured, in *P. putida*.** The cargo‑binding cleft on LolE and the LolA‑priming role of LolC are established in *E. coli*; conservation of the exact residues forming the cleft in Q88KY3 was not exhaustively verified at the residue level.

4. **LolB status in *P. putida*.** LolB homologs are present broadly in γ‑proteobacteria, but a direct confirmation of a functional LolB ortholog and its locus in KT2440 was not established here.

5. **Quantitative kinetics unknown.** ATP‑hydrolysis rates, transport turnover, and inhibitor sensitivity for the *P. putida* LolCDE have not been measured.

---

## Proposed Follow‑up Experiments / Actions

1. **Confirm essentiality in *P. putida* KT2440.** Attempt a clean *lolE* (PP_2156) deletion and a conditional/depletion allele (e.g., arabinose‑ or rhamnose‑regulated). Predicted outcome: non‑viability or severe envelope defect upon depletion, confirming the essential role inferred from *E. coli*/*P. aeruginosa*.

2. **Verify the syntenic operon and co‑transcription.** RT‑PCR / RNA‑seq across PP_2154–PP_2156 to confirm *lolC–lolD–lolE* form a single transcriptional unit, and map the operon's promoter.

3. **Residue‑level analysis of the cargo cleft.** Structurally align an AlphaFold model of Q88KY3 to the *E. coli* LolE cryo‑EM structures ([PMID: 41557797](https://pubmed.ncbi.nlm.nih.gov/41557797/), [PMID: 33782615](https://pubmed.ncbi.nlm.nih.gov/33782615/)) to confirm conservation of the periplasmic binding‑cleft residues; test predicted cleft residues by mutagenesis + release assays.

4. **Define the *P. putida* lipoproteome and test the Asp+2 rule.** Combine bioinformatic lipobox prediction with membrane fractionation / MS to catalog IM vs. OM lipoproteins, and mutate the +2 position of a reporter lipoprotein to test retention/release.

5. **Chemical‑genetic validation.** Test whether known LolCDE inhibitors (pyridineimidazoles, G0507) inhibit *P. putida* growth, and whether resistance mutations map to PP_2156, directly confirming LolE as the target in this organism.

6. **Reconstitution.** Purify the PP_2154–PP_2156 complex and reconstitute ATP‑dependent lipoprotein release in vitro with a *P. putida* LolA, measuring ATPase and transport kinetics.

---

*Prepared from an autonomous multi‑iteration investigation (10 confirmed findings; 20 papers reviewed). All functional claims are attributed to the primary/review literature cited above; the *P. putida*‑specific assignment of Q88KY3 as LolE is an orthology‑, synteny‑, and domain‑based inference of high confidence.*


## Artifacts

- [OpenScientist final report](lolE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lolE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:19809197
2. PMID:18218629
3. PMID:41557797
4. PMID:33782615
5. PMID:20419407
6. PMID:28901671
7. PMID:29109272
8. PMID:29339384
9. PMID:25583975
10. PMID:32989085
11. PMID:32490790
12. PMID:15186407
13. PMID:36037338
14. PMID:39149330
15. PMID:30992347