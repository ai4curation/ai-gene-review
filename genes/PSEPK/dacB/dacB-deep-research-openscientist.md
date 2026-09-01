---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T00:43:44.372824'
end_time: '2026-09-01T00:58:53.808267'
duration_seconds: 909.44
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: dacB
  gene_symbol: dacB
  uniprot_accession: Q88L37
  protein_description: 'SubName: Full=D-alanyl-D-alanine carboxypeptidase {ECO:0000313|EMBL:AAN67712.1};'
  gene_info: Name=dacB {ECO:0000313|EMBL:AAN67712.1}; OrderedLocusNames=PP_2098 {ECO:0000313|EMBL:AAN67712.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the peptidase S13 family.
  protein_domains: Beta-lactam/transpept-like. (IPR012338); Peptidase_S13. (IPR000667);
    Peptidase_S13 (PF02113)
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
citation_count: 13
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: dacB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: dacB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88L37
- **Protein Description:** SubName: Full=D-alanyl-D-alanine carboxypeptidase {ECO:0000313|EMBL:AAN67712.1};
- **Gene Information:** Name=dacB {ECO:0000313|EMBL:AAN67712.1}; OrderedLocusNames=PP_2098 {ECO:0000313|EMBL:AAN67712.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the peptidase S13 family.
- **Key Domains:** Beta-lactam/transpept-like. (IPR012338); Peptidase_S13. (IPR000667); Peptidase_S13 (PF02113)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "dacB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'dacB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **dacB** (gene ID: dacB, UniProt: Q88L37) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *dacB* (PP_2098, UniProt Q88L37) in *Pseudomonas putida* KT2440

## Summary

The gene **dacB** (ordered locus **PP_2098**; UniProt **Q88L37**) of *Pseudomonas putida* strain KT2440 encodes **Penicillin-Binding Protein 4 (PBP4)**, a **low-molecular-mass (LMM), periplasmic serine hydrolase** of the **peptidase S13 family** (Pfam PF02113; InterPro IPR000667; the β-lactamase/transpeptidase-like superfamily). Its primary, direct function is that of a **bifunctional peptidoglycan DD-carboxypeptidase / DD-endopeptidase**: it hydrolytically trims the terminal D-alanine from pentapeptide muropeptide stems (DD-carboxypeptidase activity) and cleaves the D-Ala–*meso*-diaminopimelate (D-Ala–mDAP) cross-links between adjacent glycan strands (DD-endopeptidase activity). Critically, it does **not** perform transpeptidation (cross-link formation). These conclusions rest on direct biochemistry of the two best-characterized orthologs — *Pseudomonas aeruginosa* DacB (70% identical to the *P. putida* protein) and *Escherichia coli* PBP4/DacB — together with high-confidence structural and sequence evidence for the *P. putida* protein itself.

The enzyme operates in the **periplasm**, where its substrate — the peptidoglycan (murein) sacculus — resides. It is recovered as a soluble/loosely associated species rather than an integral membrane protein, and it carries an N-terminal Sec-type signal region for export across the inner membrane. Catalysis proceeds through a **covalent acyl-enzyme mechanism** at an active-site serine, using the two canonical penicillin-recognizing motifs — **SxxK** (catalytic Ser59) and **KTG** (Lys410). An AlphaFold model of Q88L37 (mean pLDDT 93.9) confirms a confidently folded S13 fold with these two motifs converging into a single catalytic cleft (Ser59 Oγ 2.89 Å from Lys62 Nζ), structurally validating the protein as a catalytically competent DD-peptidase.

Beyond its housekeeping role in **periplasmic peptidoglycan maturation and remodeling**, DacB/PBP4 is a recognized **regulatory node coupling cell-wall turnover to β-lactamase induction**. In the closely related *P. aeruginosa*, loss of dacB triggers overproduction of the chromosomal **AmpC β-lactamase** through activation of the **CreBC (BlrAB) two-component system**, conferring clinically important β-lactam resistance, and the protein acts as a slowly-deacylating "trap" for β-lactams. Because *P. putida* DacB is 70% identical to *P. aeruginosa* DacB and possesses an intact active site, this signaling role is expected to be conserved, though it has not been directly demonstrated in *P. putida* itself. This report presents a robust, multi-evidence functional annotation grounded in orthologous experimental data, structural bioinformatics, and authoritative reviews of bacterial cell-wall biology.

---

## Key Findings

### Finding 1 — PP_2098/dacB is a peptidase S13 LMM-PBP4, a close ortholog of the characterized *P. aeruginosa* DacB

Sequence analysis places Q88L37 firmly within the well-characterized DacB/PBP4 group. A global Needleman–Wunsch alignment of the 470-residue *P. putida* protein against *P. aeruginosa* PAO1 DacB/PBP4 (Q9HZG1, PA3047, 476 aa) yields **343/491 = 69.9% identity** — an exceptionally high level of conservation that supports direct functional transfer from the *P. aeruginosa* ortholog. Against the more distant *E. coli* K-12 PBP4/DacB (P24228, dacB/b3182), identity is ~32.3% (178/551), still clearly within the same family.

Database annotations are internally consistent and converge on the same assignment: UniProt/InterPro place the protein in **peptidase family S13** (IPR000667; Pfam **PF02113** Peptidase_S13; Gene3D 3.50.80.20 "D-Ala-D-Ala carboxypeptidase C, peptidase S13"; SUPFAM SSF56601 β-lactamase/transpeptidase-like; PANTHER PTHR30023:SF0 penicillin-sensitive carboxypeptidase A). Both hallmark serine penicillin-recognizing active-site motifs are present in the correct spatial order: the **SxxK** nucleophile motif (S-T-M-K, catalytic Ser59) and the **KTG** triad motif (Lys410). This active-site architecture matches that of *E. coli* PBP4, confirming that Q88L37 is not a degenerate pseudo-enzyme but a bona fide member of the penicillin-recognizing serine hydrolase clan.

**Why this matters:** the 70% identity to an experimentally characterized ortholog is the single strongest justification for transferring the DD-carboxypeptidase/DD-endopeptidase functional annotation to the *P. putida* protein.

### Finding 2 — DacB/PBP4 is a bifunctional DD-carboxypeptidase / DD-endopeptidase acting on peptidoglycan

The catalytic activity is established by direct biochemistry on the two closest characterized orthologs. In *P. aeruginosa*, in vivo digestion of *E. coli* and *P. aeruginosa* sacculi by LMM-PBP4/DacB reduced dimeric, trimeric, and anhydrous muropeptides plus monomeric pentapeptide (M5), and kinetics on the natural muropeptides M5 and D45 confirmed activity, *"validating the occurrence of D,D-carboxypeptidase and D,D-endopeptidase activities"* with *"better behaviour as a D,D-endopeptidase"* ([PMID: 27716106](https://pubmed.ncbi.nlm.nih.gov/27716106/)). This is the decisive experiment for the *Pseudomonas* ortholog, and notably it indicates the enzyme is a **more efficient endopeptidase (cross-link cleaver) than carboxypeptidase**.

In *E. coli*, analysis of murein from cells overexpressing purified PBP4 showed that it *"exclusively catalyses a DD-carboxypeptidase and DD-endopeptidase reaction"* and *"is not involved in transpeptidation"* ([PMID: 2046551](https://pubmed.ncbi.nlm.nih.gov/2046551/)). This establishes both the dual hydrolytic activity and the crucial negative result that PBP4 does **not** build cross-links.

Genetic dissection in *P. aeruginosa* PAO1 places PBP4 within the LMM-PBP set: *"PBP4 and PBP7 play a significant role as dd-carboxypeptidase only if PBP5 is absent, and their dd-endopeptidase activity is also inferred"* ([PMID: 25896695](https://pubmed.ncbi.nlm.nih.gov/25896695/)). This shows that the DD-carboxypeptidase activity of PBP4 is partly redundant with the dedicated major DD-carboxypeptidase PBP5/DacC, but becomes physiologically significant when PBP5 is absent.

Consistent GO annotations for Q88L37 are serine-type carboxypeptidase activity (GO:0004185) and peptidoglycan metabolic process (GO:0000270).

The two reactions catalyzed can be summarized as follows:

| Activity | Bond cleaved | Substrate | Product |
|---|---|---|---|
| **DD-carboxypeptidase** | D-Ala⁴–D-Ala⁵ peptide bond | Pentapeptide stem (…-L-Lys/mDAP-D-Ala-D-Ala) | Tetrapeptide + free D-Ala |
| **DD-endopeptidase** | D-Ala⁴–mDAP cross-link | Cross-linked (dimeric/oligomeric) muropeptides | Separated glycan strands |
| **Transpeptidation** | — | — | **Not catalyzed** (excluded, PMID 2046551) |

### Finding 3 — DacB/PBP4 localizes to the periplasm as a low-molecular-mass PBP

Multiple lines of evidence place the enzyme in the periplasm. Biochemically, *E. coli* PBP4/DacB is recovered as a soluble species: after sonication, *"the majority (80%) of the overproduced PBP4 was detected in the 100,000 X g supernatant"* ([PMID: 2046551](https://pubmed.ncbi.nlm.nih.gov/2046551/)) — a hallmark of a periplasmic/loosely membrane-associated LMM-PBP rather than an integral membrane protein.

Structurally, the *E. coli* PBP4 crystal structure contains *"a penicillin binding domain similar to known structures, but includes a large insertion which folds into domains with unique folds"*, and covalent acyl-enzyme complexes with five antibiotics locate the reaction at a serine active site ([PMID: 16411754](https://pubmed.ncbi.nlm.nih.gov/16411754/)). The nature of the substrate (the murein sacculus, which resides in the periplasm), the family classification (peptidase S13, penicillin-sensitive carboxypeptidase A), and covalent β-lactam binding all place catalysis in the periplasm. The Q88L37 sequence begins with a Sec-type N-terminal signal/anchor region (MPLALPSHAA…) consistent with export across the inner membrane to reach its periplasmic substrate.

### Finding 4 — In *Pseudomonas*, dacB/PBP4 loss triggers AmpC β-lactamase overexpression via CreBC, linking PG turnover to a signaling pathway

A distinguishing and clinically important feature of *Pseudomonas* DacB is its role as a regulatory node. In *P. aeruginosa*, high-level clinical β-lactam resistance *"is driven by the inactivation of the dacB-encoded nonessential PBP4, which behaves as a trap target for beta-lactams"*, triggering *"overproduction of the chromosomal beta-lactamase AmpC and the specific activation of the CreBC (BlrAB) two-component regulator"* ([PMID: 19325877](https://pubmed.ncbi.nlm.nih.gov/19325877/)). This establishes dacB/PBP4 as the causal node whose loss activates a defined two-component signaling pathway.

The magnitude of this effect has been quantified. dacB mutants show constitutively elevated AmpC expression and are classified as high-level AmpC resistant mutants (HARMs) ([PMID: 23612194](https://pubmed.ncbi.nlm.nih.gov/23612194/)). Quantitatively, *"the inactivation of PBP4 led to a significant increase in ampC expression (around 50-fold)"*, rising to ~1,000-fold when all three LMM-PBPs (PBP4/DacB, PBP5/DacC, PBP7/PbpG) are removed, correlating with peptidoglycan pentapeptide levels ([PMID: 25896695](https://pubmed.ncbi.nlm.nih.gov/25896695/)). The mechanistic link runs through the muropeptide-recycling pathway: this resistance is reverted by inactivating **nagZ** or **ampG** ([PMID: 21357303](https://pubmed.ncbi.nlm.nih.gov/21357303/)), confirming that the accumulation of specific muropeptide signals produced when PBP4 is absent is what drives the response.

It is worth noting that this regulatory circuit is **not universal**: in *Enterobacter cloacae* complex, DacB inactivation is *not* responsible for constitutive ampC overexpression, and AmpD amino-acid changes are the dominant in vivo determinant ([PMID: 26438498](https://pubmed.ncbi.nlm.nih.gov/26438498/)). This contrast strengthens the specificity of the *Pseudomonas* dacB→CreBC→AmpC circuit and underscores that the *P. putida* prediction is best transferred from *P. aeruginosa* (70% identity) rather than from more distant enterics.

### Finding 5 — DacB/PBP4 is a penicillin-sensitive serine hydrolase whose slow deacylation makes it an efficient β-lactam "trap"

The mechanistic basis for the trap behavior is structural. The *E. coli* PBP4 crystal structure was solved both native and *"covalently linked to various antibiotics"*; five acyl-enzyme complexes show β-lactams bound covalently at the active-site serine, and *"the altered geometry of conserved active site residues compared with those of other PBPs suggests a possible cause for the slow deacylation rate of PBP4"* ([PMID: 16411754](https://pubmed.ncbi.nlm.nih.gov/16411754/)). Slow deacylation means the enzyme, once acylated by a β-lactam, remains trapped in the covalent complex — the physical basis for its behavior as a β-lactam "trap target." Physiologically, PBP4/DacB is a nonessential protein that *"behaves as a trap target for beta-lactams"* ([PMID: 19325877](https://pubmed.ncbi.nlm.nih.gov/19325877/)).

Consistent with a serine-hydrolase mechanism, the Q88L37 sequence conserves the S-x-x-K nucleophile motif (STMK, Ser59) and the K-T-G motif (Lys410) that define the penicillin-recognizing active site.

### Finding 6 — AlphaFold model of Q88L37 confirms a confidently folded S13 DD-peptidase with an intact SxxK…KTG active site

Structural bioinformatics on the *P. putida* protein itself corroborates the annotation. The AlphaFold DB model AF-Q88L37-F1 (v6) is high-confidence: **mean pLDDT = 93.9**, with 96% of residues at pLDDT > 70 and 88% > 90 (a well-modeled fold). The two canonical serine-PBP catalytic motifs are present and spatially converged into a single active site: motif 1 **S-x-x-K = Ser59-Thr60-Met61-Lys62** (all pLDDT 98–99), and motif 3 **K-T-G = Lys410-Thr411-Gly412**.

In the model, **Ser59 Oγ lies 2.89 Å from Lys62 Nζ** (hydrogen-bonding distance — the nucleophile/general-base pair) and **4.67 Å from Lys410 Nζ** (the KTG lysine lining the substrate cleft). This SxxK…K(T/S)G spatial arrangement is diagnostic of the β-lactamase/transpeptidase (penicilloyl-serine) superfamily active site, and its intactness in the *P. putida* model indicates the protein is a catalytically competent enzyme rather than a degenerate relic.

### Finding 7 — DacB/PBP4 acts within periplasmic peptidoglycan maturation, a recognized regulatory layer of cell-wall growth

Authoritative reviews of bacterial cell-wall biology place DD-peptidases like PBP4 in the periplasmic PG-maturation/remodeling machinery. In Gram-negative bacteria, *"the peptidoglycan sacculus resides in the periplasm"*, where robust growth is achieved by dynamic multi-protein complexes assembled from *"freely diffusing sets of peptidoglycan synthases, hydrolases and their regulators"*, whose composition depends on cell-cycle state (elongation vs division) ([PMID: 28214390](https://pubmed.ncbi.nlm.nih.gov/28214390/)). PG synthesis is regulated *"by PG maturation through the action of PG hydrolytic enzymes"* ([PMID: 27862967](https://pubmed.ncbi.nlm.nih.gov/27862967/)) — the very activity class to which DacB belongs.

Genomic context in *P. putida* KT2440 reinforces an accessory rather than core-synthetic role: PP_2098/dacB is **not** embedded in a dedicated PG-biosynthesis operon. Its flanking genes encode a diguanylate cyclase (PP_2097), a DUF469 protein (PP_2099), and a two-component histidine kinase/response-regulator pair (PP_2100/PP_2101) — a genomic neighborhood consistent with an autonomously expressed "accessory" remodeling enzyme rather than an operon-linked core synthase.

---

## Mechanistic Model / Interpretation

Bringing the findings together yields a coherent model of DacB/PBP4 as a periplasmic peptidoglycan-editing enzyme with a secondary regulatory function.

**Enzymatic role (housekeeping):** DacB is exported to the periplasm, where it edits the maturing peptidoglycan sacculus. It removes terminal D-Ala residues from pentapeptide stems (DD-carboxypeptidase) and, more efficiently, cleaves existing D-Ala–mDAP cross-links (DD-endopeptidase). By controlling the density of pentapeptide donor stems and cross-links, DacB helps regulate the degree of cross-linking and creates space for new glycan-strand insertion during elongation and division. This activity is partially redundant with the major DD-carboxypeptidase PBP5/DacC, which explains why dacB is individually non-essential.

```
        INNER MEMBRANE                 PERIPLASM (site of action)
   ┌──────────────────────┐   Sec    ┌─────────────────────────────────────┐
   │  cytoplasm           │  export  │  Peptidoglycan (murein) sacculus     │
   │  (dacB translated)   │ ───────► │                                     │
   └──────────────────────┘          │   GlcNAc-MurNAc glycan strands       │
                                      │        │                            │
                                      │   stem: L-Ala–D-Glu–mDAP–D-Ala–D-Ala │
                                      │                        ▲    ▲        │
                                      │      DacB/PBP4 (Ser59)  │    │        │
                                      │   DD-CPase ────────────┘    │        │
                                      │   (removes D-Ala5)          │        │
                                      │   DD-EPase ─────────────────┘        │
                                      │   (cleaves D-Ala4–mDAP cross-link)   │
                                      └─────────────────────────────────────┘
```

**Catalytic mechanism:** Catalysis uses a classic penicilloyl-serine mechanism. Ser59 (SxxK motif) is the nucleophile, activated by the adjacent Lys62; Lys410 (KTG motif) lines the substrate cleft. The acyl-enzyme intermediate on the D-Ala carbonyl is normally hydrolyzed to regenerate free enzyme. β-Lactam antibiotics mimic the D-Ala–D-Ala terminus, acylate Ser59, and — because PBP4 deacylates slowly — trap the enzyme in a stable covalent complex.

**Regulatory role (signaling, demonstrated in *P. aeruginosa*):** When DacB is inactivated (genetically, or functionally by β-lactam trapping), the periplasmic muropeptide pool shifts — pentapeptide-containing fragments accumulate. Recycled via AmpG (permease) and NagZ (glucosaminidase), these fragments act as signaling molecules that, in *Pseudomonas*, activate the CreBC (BlrAB) two-component system and derepress AmpC β-lactamase, producing high-level β-lactam resistance.

```
   dacB/PBP4 inactivation ──► altered muropeptide pool (↑ pentapeptides)
                                      │
                          AmpG import + NagZ processing
                                      │
                                      ▼
                        CreBC (BlrAB) 2-component activation
                                      │
                                      ▼
                     AmpC β-lactamase overexpression (~50×)
                                      │
                                      ▼
                        high-level β-lactam resistance
```

**Confidence of transfer to *P. putida*:** The enzymatic annotation (DD-CPase/DD-EPase, periplasmic, serine mechanism) is transferred with **high confidence** — it rests on 70% sequence identity to a directly characterized ortholog, an intact modeled active site, and consistent family/domain assignments. The regulatory (AmpC/CreBC) annotation is transferred with **moderate confidence** as a strong prediction: the circuit is well established in *P. aeruginosa* and *P. putida* possesses the orthologous machinery, but it has not been directly demonstrated in *P. putida*, and the enterobacterial counter-example (PMID 26438498) shows the circuit's wiring is species-dependent.

---

## Evidence Base

| PMID | Title (abbrev.) | Organism | How it supports the annotation |
|---|---|---|---|
| [27716106](https://pubmed.ncbi.nlm.nih.gov/27716106/) | In vivo functional/molecular characterization of PBP4 (DacB) of *P. aeruginosa* | *P. aeruginosa* | **Decisive ortholog biochemistry**: validates DD-carboxypeptidase AND DD-endopeptidase activity; enzyme behaves better as endopeptidase |
| [2046551](https://pubmed.ncbi.nlm.nih.gov/2046551/) | Cloning/overexpression of *E. coli* dacB; murein composition | *E. coli* | PBP4 exclusively catalyzes DD-CPase and DD-EPase, **not** transpeptidation; 80% soluble → periplasmic |
| [16411754](https://pubmed.ncbi.nlm.nih.gov/16411754/) | Crystal structure of *E. coli* PBP4, native + antibiotic complexes | *E. coli* | Penicillin-binding serine domain; covalent acyl-enzymes; altered active-site geometry → slow deacylation (trap) |
| [25896695](https://pubmed.ncbi.nlm.nih.gov/25896695/) | Role of *P. aeruginosa* LMM-PBPs in AmpC, resistance, PG structure | *P. aeruginosa* | Places PBP4 in LMM-PBP set; quantifies ampC induction (~50× single, ~1000× triple mutant); redundancy with PBP5 |
| [19325877](https://pubmed.ncbi.nlm.nih.gov/19325877/) | β-lactam resistance response from inactivation of nonessential PBP | *P. aeruginosa* | dacB/PBP4 loss = causal node; AmpC overproduction + CreBC(BlrAB) activation; "trap target for β-lactams" |
| [23612194](https://pubmed.ncbi.nlm.nih.gov/23612194/) | PG-remodeling enzyme repertoire and β-lactam resistance | *P. aeruginosa* | dacB mutants = HARMs with constitutively elevated AmpC; two pathways to AmpC expression |
| [21357303](https://pubmed.ncbi.nlm.nih.gov/21357303/) | AmpG inactivation restores susceptibility | *P. aeruginosa* | dacB-driven resistance reverted by nagZ/ampG → confirms muropeptide-recycling link |
| [26438498](https://pubmed.ncbi.nlm.nih.gov/26438498/) | AmpC regulation in *Enterobacter cloacae* complex | *E. cloacae* | **Counter-example**: DacB loss does NOT cause constitutive ampC overexpression in ECC → circuit is species-specific |
| [28214390](https://pubmed.ncbi.nlm.nih.gov/28214390/) | Robust PG growth by dynamic multi-protein complexes | Review | Sacculus is periplasmic; hydrolases like PBP4 operate in dynamic PG-growth complexes |
| [27862967](https://pubmed.ncbi.nlm.nih.gov/27862967/) | Regulation of bacterial cell wall growth | Review | PG synthesis regulated by maturation via hydrolytic enzymes (DacB's activity class) |

Supporting context on LMM-PBP redundancy and DD-carboxypeptidase physiology is provided by studies of *E. coli* DacC/DacA under stress ([PMID: 37098975](https://pubmed.ncbi.nlm.nih.gov/37098975/)) and broader reviews of PBP activities and cell division ([PMID: 26370943](https://pubmed.ncbi.nlm.nih.gov/26370943/); [PMID: 23215820](https://pubmed.ncbi.nlm.nih.gov/23215820/)).

**Concordance of evidence:** Both direct biochemical studies of DacB/PBP4 orthologs (2/2: PMID 27716106 in *Pseudomonas*, PMID 2046551 in *E. coli*) agree that the enzyme is a bifunctional DD-carboxypeptidase/DD-endopeptidase that does not transpeptidate. All three *P. aeruginosa* genetic studies (3/3: PMID 19325877, 23612194, 25896695) agree that dacB loss elevates AmpC. The only discordant note (PMID 26438498) concerns a distant enterobacterial species and does not undermine the transfer from *P. aeruginosa* to *P. putida*.

---

## Limitations and Knowledge Gaps

1. **No direct experimental characterization of the *P. putida* KT2440 protein.** Every enzymatic and regulatory claim is transferred by orthology from *P. aeruginosa* (70% identity) and *E. coli* (~32% identity). No purified-enzyme kinetics, no muropeptide-profiling of a *P. putida* dacB mutant, and no localization assay have been performed on Q88L37 itself. The AlphaFold model, while high-confidence, is a prediction, not an experimental structure.

2. **The AmpC/CreBC signaling role is inferred, not demonstrated, in *P. putida*.** *P. putida* is a non-pathogenic soil/rhizosphere bacterium and its β-lactamase induction wiring may differ from clinical *P. aeruginosa*. The enterobacterial counter-example (PMID 26438498) shows the dacB→AmpC link is not universal. Whether *P. putida* KT2440 even mounts a comparable CreBC-dependent AmpC response upon dacB loss is unverified.

3. **Substrate-specificity fine detail is unresolved for the *P. putida* enzyme.** The relative DD-carboxypeptidase vs DD-endopeptidase preference (the *P. aeruginosa* ortholog favors endopeptidase activity) has not been measured for Q88L37, nor has its muropeptide substrate preference (e.g., monomeric M5 vs cross-linked D45) been quantified.

4. **Physiological/morphological consequences in *P. putida* are unknown.** Because LMM-PBPs are redundant (PBP4 activity is significant mainly when PBP5/DacC is absent), the phenotype of a *P. putida* dacB single mutant under standard and stress conditions (osmotic, pH) has not been documented.

5. **Genomic-context interpretation is provisional.** The inference that flanking genes (diguanylate cyclase PP_2097; TCS PP_2100/PP_2101) indicate an "accessory, autonomously expressed" enzyme is bioinformatic and does not establish co-regulation or functional interaction.

---

## Proposed Follow-up Experiments / Actions

1. **Purify recombinant *P. putida* DacB (Q88L37) and assay muropeptide kinetics.** Measure DD-carboxypeptidase (release of D-Ala from pentapeptide M5) and DD-endopeptidase (cleavage of dimeric D45) activities directly, to confirm the transferred annotation and determine the endo/carboxy preference for this specific ortholog. *(High priority; directly resolves gaps 1 & 3.)*

2. **Construct a *P. putida* KT2440 ΔdacB mutant and profile its sacculus by HPLC/MS muropeptide analysis.** Compare pentapeptide, cross-link, and anhydro-muropeptide levels vs wild type to verify in vivo remodeling function. Pair with a ΔdacB ΔdacC double mutant to test redundancy with PBP5.

3. **Test the AmpC/CreBC circuit in *P. putida*.** Quantify chromosomal β-lactamase expression and β-lactam MICs in the ΔdacB mutant, and probe whether a CreBC (BlrAB) ortholog is required, to determine whether the *P. aeruginosa* regulatory role is conserved. *(Directly resolves gap 2.)*

4. **Solve or confirm the structure and active-site geometry experimentally.** Crystallize or cryo-EM the *P. putida* enzyme, ideally as a β-lactam acyl-enzyme complex, to validate the AlphaFold-predicted SxxK…KTG cleft and characterize deacylation kinetics (trap behavior).

5. **Verify periplasmic localization and signal-peptide processing** via cell-fractionation and N-terminal sequencing of the mature protein, confirming Sec-dependent export.

6. **Phenotypic characterization under stress.** Given that homologous DD-carboxypeptidases (DacC/DacA) have distinct roles under alkaline vs salt stress ([PMID: 37098975](https://pubmed.ncbi.nlm.nih.gov/37098975/)), test *P. putida* ΔdacB for growth and cell-shape defects across pH and osmotic conditions.

---

## Conclusion

*P. putida* KT2440 **dacB** (PP_2098, Q88L37) encodes **PBP4**, a periplasmic, low-molecular-mass, peptidase S13-family serine hydrolase that functions as a **bifunctional peptidoglycan DD-carboxypeptidase / DD-endopeptidase** in the maturation and remodeling of the murein sacculus — trimming terminal D-Ala from pentapeptide stems and cleaving D-Ala–mDAP cross-links, without performing transpeptidation. This annotation is supported by 70% identity to the experimentally characterized *P. aeruginosa* ortholog, direct biochemistry of *E. coli* and *P. aeruginosa* PBP4, and a high-confidence AlphaFold model with an intact SxxK(Ser59)…KTG(Lys410) active site. As a secondary, inferred role, DacB is expected to serve as a control node coupling peptidoglycan turnover to β-lactamase (AmpC) induction via the CreBC two-component system, as directly demonstrated in *P. aeruginosa*, though this regulatory function awaits verification in *P. putida* itself.


## Artifacts

- [OpenScientist final report](dacB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](dacB-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27716106
2. PMID:2046551
3. PMID:25896695
4. PMID:16411754
5. PMID:19325877
6. PMID:23612194
7. PMID:21357303
8. PMID:26438498
9. PMID:28214390
10. PMID:27862967
11. PMID:37098975
12. PMID:26370943
13. PMID:23215820