---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-23T16:30:36.051386'
end_time: '2026-07-23T16:46:18.236144'
duration_seconds: 942.18
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mraY
  gene_symbol: mraY
  uniprot_accession: Q88N79
  protein_description: 'RecName: Full=Phospho-N-acetylmuramoyl-pentapeptide-transferase
    {ECO:0000255|HAMAP-Rule:MF_00038}; EC=2.7.8.13 {ECO:0000255|HAMAP-Rule:MF_00038};
    AltName: Full=UDP-MurNAc-pentapeptide phosphotransferase {ECO:0000255|HAMAP-Rule:MF_00038};'
  gene_info: Name=mraY {ECO:0000255|HAMAP-Rule:MF_00038}; OrderedLocusNames=PP_1334;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the glycosyltransferase 4 family. MraY
  protein_domains: Glycosyl_transferase_4. (IPR000715); PNAcMuramoyl-5peptid_Trfase.
    (IPR003524); PNAcMuramoyl-5peptid_Trfase_CS. (IPR018480); Glycos_transf_4 (PF00953);
    MraY_sig1 (PF10555)
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
citation_count: 11
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mraY-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mraY-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88N79
- **Protein Description:** RecName: Full=Phospho-N-acetylmuramoyl-pentapeptide-transferase {ECO:0000255|HAMAP-Rule:MF_00038}; EC=2.7.8.13 {ECO:0000255|HAMAP-Rule:MF_00038}; AltName: Full=UDP-MurNAc-pentapeptide phosphotransferase {ECO:0000255|HAMAP-Rule:MF_00038};
- **Gene Information:** Name=mraY {ECO:0000255|HAMAP-Rule:MF_00038}; OrderedLocusNames=PP_1334;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the glycosyltransferase 4 family. MraY
- **Key Domains:** Glycosyl_transferase_4. (IPR000715); PNAcMuramoyl-5peptid_Trfase. (IPR003524); PNAcMuramoyl-5peptid_Trfase_CS. (IPR018480); Glycos_transf_4 (PF00953); MraY_sig1 (PF10555)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mraY" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mraY' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mraY** (gene ID: mraY, UniProt: Q88N79) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: MraY (Phospho-N-acetylmuramoyl-pentapeptide-transferase) in *Pseudomonas putida* KT2440

**UniProt:** Q88N79 | **Gene:** *mraY* | **Locus:** PP_1334 | **EC:** 2.7.8.13
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / NCIMB 11950 / KT2440)
**Protein family:** Glycosyltransferase 4 (GT4) superfamily, MraY subfamily
**Domains:** Glycos_transf_4 (PF00953); MraY_sig1 (PF10555); IPR003524; IPR018480

---

## Gene/Protein Identity Verification

| Attribute | Value |
|---|---|
| UniProt accession | Q88N79 |
| Gene name | *mraY* (ordered locus PP_1334) |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) |
| Protein | Phospho-N-acetylmuramoyl-pentapeptide-transferase (translocase) |
| EC number | 2.7.8.13 |
| Alt. name | UDP-MurNAc-pentapeptide phosphotransferase |
| Family | GT4 / MraY; polyprenyl-phosphate N-acetylhexosamine-1-phosphate transferase (PNPT) superfamily |
| Domains | Glycos_transf_4 (PF00953); MraY_sig1 (PF10555); IPR003524 / IPR018480 |
| Annotation basis | HAMAP rule MF_00038 |

**Verification result: CONFIRMED, unambiguous.** The gene symbol *mraY*, the protein description (phospho-N-acetylmuramoyl-pentapeptide-transferase, EC 2.7.8.13), the GT4/MraY family assignment, and the diagnostic Pfam domains (PF00953 Glycos_transf_4, PF10555 MraY_sig1) are all mutually consistent and correspond to a single, deeply conserved bacterial enzyme. *mraY* is universally single-copy and essential across bacteria, so there is no gene-symbol ambiguity. No direct experimental study of the *P. putida* PP_1334 ortholog was found; its function is assigned by strong sequence/domain homology (HAMAP MF_00038) to biochemically and structurally characterized MraY enzymes of *E. coli*, *B. subtilis*, and *Aquifex aeolicus*. Because MraY is one of the most highly conserved enzymes of the essential peptidoglycan pathway, this inference is robust.

---

## Summary

**MraY (Q88N79 / PP_1334) is an essential, polytopic integral cytoplasmic-membrane enzyme that catalyzes the first membrane-committed step of bacterial peptidoglycan (cell wall) biosynthesis.** It is a phospho-N-acetylmuramoyl-pentapeptide transferase — also called a "translocase" or UDP-MurNAc-pentapeptide phosphotransferase (EC 2.7.8.13). Working at the inner (cytoplasmic) leaflet of the plasma membrane, it transfers the phospho-MurNAc-pentapeptide moiety from the soluble cytoplasmic precursor **UDP-MurNAc-pentapeptide** onto the membrane-embedded lipid carrier **undecaprenyl phosphate** (C₅₅-P, bactoprenyl phosphate), producing the first lipid-linked cell-wall intermediate — **Lipid I** (undecaprenyl-pyrophosphoryl-MurNAc-pentapeptide) — and releasing **uridine monophosphate (UMP)**. This reaction is the pivotal event that hands the growing peptidoglycan monomer from the cytoplasmic (soluble) phase of synthesis to the membrane-associated assembly line.

The functional assignment for the *P. putida* protein rests on HAMAP rule MF_00038, which propagates biochemical and structural characterization from experimentally studied MraY orthologs on the basis of strong sequence conservation and the presence of the diagnostic Glycos_transf_4 (PF00953) and MraY-specific (PF10555) domains. No direct enzymological study of the *P. putida* KT2440 protein itself has been published, but the conservation of catalytic residues and signature motifs makes the annotation highly reliable.

Mechanistically, MraY belongs to the polyprenyl-phosphate N-acetylhexosamine-1-phosphate transferase (PNPT) superfamily. It requires a divalent metal cofactor (Mg²⁺), uses conserved acidic aspartate residues and an essential histidine for catalysis, and operates through an ordered ternary-complex mechanism in which both substrates bind before either product is released. The gene sits within the highly conserved *mra*/*dcw* (division and cell-wall) gene cluster, physically and transcriptionally linked to cell-division and other Mur-pathway genes. Because MraY is essential, universally distributed in bacteria, and absent from humans, it is a validated and heavily pursued target for antibacterial drug discovery — inhibited by several structurally distinct classes of natural-product nucleoside antibiotics and by the bacteriophage φX174 lysis protein E.

---

## Key Findings

### Finding 1 — MraY catalyzes the first membrane step of peptidoglycan synthesis, producing Lipid I

MraY carries out the reaction:

> **UDP-MurNAc-pentapeptide + undecaprenyl phosphate (C₅₅-P) → Lipid I (C₅₅-PP-MurNAc-pentapeptide) + UMP**

This is a phosphotransfer reaction in which the phospho-N-acetylmuramoyl-pentapeptide unit is transferred from a uridine-diphosphate donor to a polyprenyl-phosphate lipid acceptor. It is the committed membrane step that converts the last *soluble* cytoplasmic peptidoglycan precursor into the first *membrane-bound* lipid intermediate. Mechanistically the enzyme cleaves the pyrophosphate bond of the UDP-sugar and forms a new pyrophosphate linkage to the lipid carrier, releasing UMP.

The enzymatically characterized orthologs of MraY (from *B. subtilis* and *E. coli*) were shown to transfer the phospho-MurNAc-pentapeptide moiety onto undecaprenyl phosphate, yielding Lipid I and releasing UMP; the enzyme was purified to homogeneity and kinetically characterized (Bouhss et al., 2004). The reaction is notably **reversible** — in the presence of UMP the enzyme will run backward, regenerating UDP-MurNAc-pentapeptide from Lipid I. A review of MraY biochemistry states the reaction explicitly: *"The integral membrane protein MraY translocase is essential for peptidoglycan biosynthesis catalysing the transfer of the peptidoglycan precursor phospho-MurNAc-pentapeptide to the lipid carrier undecaprenyl phosphate, thereby generating the cell wall intermediate lipid I"* ([PMID: 31138496](https://pubmed.ncbi.nlm.nih.gov/31138496/)). The primary characterization paper defines the reaction, substrate, product, and reversibility: *"The MraY translocase catalyzes the first membrane step of bacterial cell wall peptidoglycan synthesis (i.e. the transfer of the phospho-N-acetylmuramoyl-pentapeptide motif onto the undecaprenyl phosphate carrier lipid), a reversible reaction yielding undecaprenylpyrophosphoryl-N-acetylmuramoyl-pentapeptide (lipid intermediate I)"* ([PMID: 15131133](https://pubmed.ncbi.nlm.nih.gov/15131133/)).

**Substrate specificity.** The donor is UDP-MurNAc-pentapeptide, the product of the cytoplasmic MurA–MurF pathway; MraY is specific for this MurNAc-pentapeptide donor and can be distinguished from its paralog WecA, which instead uses UDP-GlcNAc while sharing the same lipid acceptor ([PMID: 27312048](https://pubmed.ncbi.nlm.nih.gov/27312048/)). The lipid acceptor is undecaprenyl phosphate (C₅₅-P); shorter polyprenyl-phosphate homologs (e.g., C₃₅-P) serve as functional analogs in vitro kinetic assays. For the *P. putida* KT2440 protein this activity is assigned by HAMAP rule MF_00038 based on strong sequence and domain homology (Glycos_transf_4 PF00953, MraY_sig1 PF10555; EC 2.7.8.13), so the substrate specificity is inferred to be identical.

### Finding 2 — MraY is a polytopic integral cytoplasmic-membrane protein acting at the inner leaflet

MraY is an essential integral membrane protein embedded in the bacterial cytoplasmic (inner) membrane. It is a polytopic (multiple transmembrane helices) protein, historically refractory to overexpression and purification, and requiring membrane or detergent environments for activity (Bouhss et al., 2004). Its catalytic site faces the cytoplasmic side of the membrane, where it accesses both its soluble substrate (cytoplasmic UDP-MurNAc-pentapeptide) and its lipid substrate (undecaprenyl phosphate embedded in the inner leaflet). MraY orthologs adopt a ten-transmembrane-helix architecture with the catalytic acidic residues on cytoplasmically exposed loops.

MraY's product, Lipid I, is subsequently converted to Lipid II by the glycosyltransferase MurG (which adds GlcNAc), and Lipid II is then flipped across the membrane and polymerized on the outer leaflet. Thus MraY functions at a strategic membrane interface, physically coupling the cytoplasmic Mur-enzyme pathway to the membrane-bound assembly of the cell wall. The primary literature directly states MraY is *"This essential integral membrane protein, which is considered as a very promising target for the search of new antibacterial compounds"* ([PMID: 15131133](https://pubmed.ncbi.nlm.nih.gov/15131133/)), and the pathway review places MraY firmly within *"the membrane steps leading to the formation of the lipid II intermediate"* ([PMID: 18081839](https://pubmed.ncbi.nlm.nih.gov/18081839/)).

**Subcellular localization: cytoplasmic (inner) membrane, with the active site at the cytoplasmic leaflet.**

### Finding 3 — Catalytic mechanism: PNPT superfamily, Mg²⁺-dependent, ordered ternary complex, conserved acidic and histidine residues

MraY belongs to the **polyprenyl-phosphate N-acetylhexosamine-1-phosphate transferase (PNPT) superfamily** — the same superfamily as its paralog WecA (involved in enterobacterial common antigen / O-antigen synthesis) and the eukaryotic enzyme GPT/DPAGT1 (which primes N-linked glycosylation). Members of this superfamily catalyze the transfer of a hexosamine-1-phosphate from a nucleotide-sugar donor onto a polyprenyl-phosphate acceptor.

Several converging lines of biochemical and structural evidence define the mechanism:

- **Superfamily assignment and ternary-complex requirement.** MraY and WecA both require the second substrate for forward and reverse exchange reactions and lack independent pyrophosphatase activity — consistent with a single-displacement, ternary-complex mechanism rather than a ping-pong (covalent enzyme intermediate) mechanism (Al-Dabbagh et al., 2016). The review states: *"These two enzymes are members of the polyprenyl-phosphate N-acetylhexosamine 1-phosphate transferase superfamily, which are essential for bacterial envelope biogenesis"* ([PMID: 27312048](https://pubmed.ncbi.nlm.nih.gov/27312048/)).

- **Kinetics of ordered binding and an essential histidine.** Kinetic and docking studies of *B. subtilis* MraY show that both substrates must bind before any product is released — *"the concomitant binding of both UDP-MurNAc-pentapeptide-DNS and C35-P to the enzyme is required before the release of the two products"* ([PMID: 27226570](https://pubmed.ncbi.nlm.nih.gov/27226570/)) — and identify a fully conserved essential histidine (His-289 in *B. subtilis* numbering) in the active site.

- **Divalent-cation dependence and catalytic acidic residues.** The crystal structure of *Aquifex aeolicus* MraY with the inhibitor muraymycin D2 revealed three catalytically essential acidic (aspartate) residues and a required Mg²⁺ cofactor, and demonstrated large active-site conformational changes upon ligand binding. The inhibitor structure study notes that muraymycin D2 *"does not interact with three acidic residues or the Mg(2+) cofactor required for catalysis"* ([PMID: 27088606](https://pubmed.ncbi.nlm.nih.gov/27088606/)), thereby pinpointing these residues and the metal ion as the catalytic core.

These catalytic residues (the conserved aspartates coordinating Mg²⁺ and the essential active-site histidine) are conserved in the *P. putida* sequence by virtue of the HAMAP signature, supporting the inference that the enzyme uses the same Mg²⁺-dependent ordered ternary-complex chemistry.

### Finding 4 — MraY is essential, encoded in the *mra*/*dcw* gene cluster, and a validated antibacterial target

MraY is essential for viability and is not present in eukaryotes, making it an attractive and selective antibacterial target. In *E. coli*, *mraY* lies within the Pmra-driven *mra* gene cluster together with cell-division and cell-envelope biosynthesis genes: *"the Pmra promoter is required for expression of the first nine genes of the mra cluster: mraZ (orfC), mraW (orfB), ftsL (mraR), ftsI, murE, murF, mraY, murD, and ftsW"* ([PMID: 9721276](https://pubmed.ncbi.nlm.nih.gov/9721276/)). Repressing this promoter depletes UDP-MurNAc-pentapeptide and decreases peptidoglycan synthesis, directly confirming *mraY*'s role in the pathway and its co-regulation with the division machinery. In *P. putida* KT2440, the corresponding gene is PP_1334, embedded in an orthologous *mra*/*dcw* cluster — reflecting the deep conservation of the division-and-cell-wall gene neighborhood across bacteria.

Its essentiality is further underscored by two independent lines of chemical/biological evidence. First, MraY is inhibited by structurally diverse **uridine-containing nucleoside natural-product antibiotics**: *"several classes of uridine-containing nucleoside antibiotics (tunicamycins, mureidomycins/pacidamycins/sansanmycins, liposidomycins/caprazamycins, muraymycins, capuramycins) that target translocase MraY"* ([PMID: 31471595](https://pubmed.ncbi.nlm.nih.gov/31471595/)). Second, MraY is the specific molecular target of the bacteriophage φX174 lysis protein E: *"Protein E, the lysis protein of bacteriophage phiX174, is a specific inhibitor of MraY, the phospho-MurNAc-pentapeptide translocase that catalyzes the synthesis of lipid I"* ([PMID: 18791230](https://pubmed.ncbi.nlm.nih.gov/18791230/)) — inhibition of MraY by protein E blocks Lipid I synthesis and causes cell lysis, an elegant natural demonstration that MraY activity is indispensable for viability. Note that tunicamycin also inhibits the human MraY paralog GPT/DPAGT1, which limits its selectivity; structural work aims to design MraY-selective agents ([PMID: 29459785](https://pubmed.ncbi.nlm.nih.gov/29459785/); [PMID: 29778697](https://pubmed.ncbi.nlm.nih.gov/29778697/)).

---

## Mechanistic Model / Interpretation

MraY occupies the linchpin position in the peptidoglycan biosynthetic pathway — the transition from the cytoplasmic (Mur) phase to the membrane (lipid-intermediate) phase.

### The peptidoglycan biosynthetic pathway and MraY's position

```
  CYTOPLASM  (soluble Mur enzymes)
  ─────────────────────────────────────────────
  UDP-GlcNAc
     │  MurA, MurB
     ▼
  UDP-MurNAc
     │  MurC → MurD → MurE → MurF  (add L-Ala, D-Glu, meso-DAP, D-Ala-D-Ala)
     ▼
  UDP-MurNAc-pentapeptide  ◄── last SOLUBLE precursor
     │
  ═══╪══════════════════════════════════════════ INNER MEMBRANE (cytoplasmic leaflet)
     │
     │   ┌──────────────────────────────────────┐
     │   │   MraY (PP_1334, Q88N79)  EC 2.7.8.13 │
     │   │   + undecaprenyl-P (C55-P)            │
     │   │   – UMP                               │
     │   └──────────────────────────────────────┘
     ▼
  LIPID I  (C55-PP-MurNAc-pentapeptide)  ◄── first MEMBRANE intermediate
     │  MurG  (+ UDP-GlcNAc, – UDP)
     ▼
  LIPID II  (C55-PP-MurNAc(-pentapeptide)-GlcNAc)
     │  flippase (MurJ / FtsW)
     ▼  ... flip to periplasmic leaflet ...
  Transglycosylation + transpeptidation (PBPs) → mature peptidoglycan sacculus
```

MraY is the gatekeeper of this transition. Its two substrates come from two different physical compartments — the water-soluble UDP-MurNAc-pentapeptide from the cytoplasm and the lipophilic undecaprenyl phosphate from the membrane — and MraY brings them together at the membrane surface. The reaction it performs is an N-acetylhexosamine-1-phosphate transfer: the MurNAc-pentapeptide is joined to the lipid carrier through a pyrophosphate linkage, with UMP leaving as the by-product.

### Enzymatic mechanism at a glance

| Feature | Property | Evidence |
|---|---|---|
| Reaction type | Phospho-MurNAc-pentapeptide (hexosamine-1-P) transfer | PMID 15131133, 31138496 |
| Donor substrate | UDP-MurNAc-pentapeptide (cytoplasmic) | PMID 15131133 |
| Acceptor substrate | Undecaprenyl phosphate (C₅₅-P, membrane lipid) | PMID 15131133 |
| Products | Lipid I + UMP | PMID 15131133 |
| Reversibility | Reversible (runs backward with UMP) | PMID 15131133 |
| Cofactor | Mg²⁺ (divalent cation) | PMID 27088606 |
| Catalytic residues | 3 conserved aspartates + essential His | PMID 27088606, 27226570 |
| Kinetic mechanism | Ordered ternary complex (both substrates bind before product release) | PMID 27226570, 27312048 |
| Superfamily | Polyprenyl-P N-acetylhexosamine-1-P transferase (PNPT / GT4) | PMID 27312048 |
| Localization | Polytopic inner-membrane protein; acts at cytoplasmic leaflet | PMID 15131133, 18081839 |

The ternary-complex mechanism (as opposed to a covalent ping-pong intermediate) is significant: the phospho-MurNAc-pentapeptide is transferred in a single step directly from UDP-MurNAc-pentapeptide to the lipid, with the Mg²⁺ ion and the conserved aspartates positioning the phosphates and stabilizing the transition state, and the essential histidine participating in catalysis. The large conformational changes seen crystallographically on ligand binding indicate that MraY closes over its substrates to form a competent active site.

### Evolutionary and structural context

MraY, WecA (bacterial), and GPT/DPAGT1 (eukaryotic) are paralogs in the PNPT superfamily, all transferring a sugar-1-phosphate onto a polyprenyl-phosphate carrier. This shared chemistry explains why the natural product **tunicamycin** inhibits both MraY (antibacterial) and human GPT (off-target toxicity), and why muraymycin A1 is a potent inhibitor of DPAGT1. Efforts to design MraY-selective inhibitors exploit the structural differences between the bacterial and human enzymes ([PMID: 29459785](https://pubmed.ncbi.nlm.nih.gov/29459785/); [PMID: 29778697](https://pubmed.ncbi.nlm.nih.gov/29778697/)). For the *P. putida* protein specifically, this evolutionary framework provides confidence that the catalytic machinery, substrate specificity, and membrane topology are conserved.

---

## Evidence Base

The functional annotation of Q88N79 relies on transfer of experimental characterization from well-studied orthologs (HAMAP MF_00038). The key supporting literature is summarized below.

| PMID | Title (abbreviated) | How it supports the annotation |
|---|---|---|
| [15131133](https://pubmed.ncbi.nlm.nih.gov/15131133/) | *Purification and characterization of the bacterial MraY translocase...* | Primary biochemistry: defines the reaction, substrates, product (Lipid I), reversibility; establishes MraY as an essential integral membrane protein |
| [31138496](https://pubmed.ncbi.nlm.nih.gov/31138496/) | *Caprazamycins: Biosynthesis and structure activity relationship studies* | States the exact reaction and substrates; MraY as translocase target |
| [18081839](https://pubmed.ncbi.nlm.nih.gov/18081839/) | *The biosynthesis of peptidoglycan lipid-linked intermediates* | Places MraY within the membrane steps forming Lipid I / Lipid II |
| [27312048](https://pubmed.ncbi.nlm.nih.gov/27312048/) | *Catalytic mechanism of MraY and WecA...* | Assigns MraY to the PNPT superfamily; ternary-complex mechanism; WecA uses UDP-GlcNAc |
| [27226570](https://pubmed.ncbi.nlm.nih.gov/27226570/) | *New Insight into the Catalytic Mechanism of Bacterial MraY...* | Kinetics: ordered concomitant substrate binding; essential His-289 |
| [27088606](https://pubmed.ncbi.nlm.nih.gov/27088606/) | *Structural insights into inhibition of lipid I production...* | Crystal structure (*A. aeolicus*): 3 acidic residues + Mg²⁺ required; conformational changes |
| [9721276](https://pubmed.ncbi.nlm.nih.gov/9721276/) | *Contribution of the Pmra promoter... mra cluster* | Genomic context: *mraY* in the *mra*/*dcw* cluster; co-regulation with division genes; depletion decreases PG synthesis |
| [31471595](https://pubmed.ncbi.nlm.nih.gov/31471595/) | *Mechanism of action of nucleoside antibacterial natural product antibiotics* | Documents MraY as target of multiple nucleoside antibiotic classes |
| [18791230](https://pubmed.ncbi.nlm.nih.gov/18791230/) | *Genetic analysis of MraY inhibition by the phiX174 protein E* | Protein-based inhibitor; confirms MraY makes Lipid I and is essential |
| [29778697](https://pubmed.ncbi.nlm.nih.gov/29778697/) | *Structural basis for selective inhibition of antibacterial target MraY* | Structural comparison of bacterial MraY vs human GPT; inhibitor binding modes |
| [29459785](https://pubmed.ncbi.nlm.nih.gov/29459785/) | *GlcNAc-1-P-transferase-tunicamycin complex structure...* | Distinguishes MraY from human GPT; basis for selective inhibition |
| [16305528](https://pubmed.ncbi.nlm.nih.gov/16305528/) | *MraY Inhibitors as Novel Antibacterial Agents* | Validates MraY as a drug target; catalogs inhibitor classes |
| [41447945](https://pubmed.ncbi.nlm.nih.gov/41447945/) | *New Insights of Muraymycin A1 and Its Analogs as DPAGT1 Inhibitors* | Illustrates paralog relationship (MraY inhibitors also hit eukaryotic DPAGT1) |
| [31769280](https://pubmed.ncbi.nlm.nih.gov/31769280/) | *Substrate Tolerance of Bacterial Glycosyltransferase MurG...* | Context for downstream MurG step (Lipid I → Lipid II) |

**Strength of evidence.** The reaction, substrates, products, membrane localization, mechanism, and essentiality are all supported by direct experimental characterization of MraY orthologs (purified-enzyme kinetics, crystallography, genetics). The *P. putida* KT2440 assignment itself is **homology-based (inference by HAMAP MF_00038)** rather than direct experimental study, but the conservation of the diagnostic PF00953/PF10555 domains and the catalytic residues makes this a high-confidence annotation.

### Supported vs. refuted hypotheses

**Supported:**
- MraY is a phospho-MurNAc-pentapeptide transferase producing Lipid I from UDP-MurNAc-pentapeptide + undecaprenyl phosphate. ✔ (strong biochemical + structural evidence in orthologs; homology in *P. putida*)
- MraY is an integral cytoplasmic-membrane enzyme acting at the inner leaflet. ✔
- MraY requires Mg²⁺ and conserved acidic/His active-site residues, using a ternary-complex mechanism. ✔
- MraY is essential and functions within the *mra*/*dcw* cell-division/cell-wall gene cluster. ✔

**Refuted / excluded:**
- The enzyme does **not** use a covalent (ping-pong) mechanism and has **no intrinsic pyrophosphatase activity** ([PMID: 27312048](https://pubmed.ncbi.nlm.nih.gov/27312048/)).
- The gene symbol is **not** ambiguous: all identifiers converge on a single well-characterized enzyme; no competing gene with the same symbol was found.

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of the *P. putida* KT2440 protein.** All enzymological and structural characterization derives from orthologs (*E. coli*, *B. subtilis*, *A. aeolicus*). The function of Q88N79 is assigned by homology (HAMAP MF_00038). No published Km/kcat values, purified-enzyme assays, deletion/depletion phenotypes, or structures exist for the *P. putida* protein specifically.

2. **Species-specific substrate details.** The pentapeptide stem composition can vary between species; the third residue is typically *meso*-diaminopimelate in Gram-negatives such as *P. putida*. While MraY largely recognizes the UDP-MurNAc-phosphate portion of the donor, the precise substrate kinetics for the *P. putida* pentapeptide have not been measured.

3. **Membrane topology not experimentally mapped in *P. putida*.** The polytopic (≈10-TM) topology and transmembrane-helix arrangement are inferred from ortholog structures, not directly determined for PP_1334.

4. **Regulation and protein–protein interactions.** Whether *P. putida* MraY participates in a divisome-associated complex (e.g., with MurG, FtsW, or other Mur enzymes) or is regulated at the *mra* promoter as in *E. coli* has not been experimentally verified for this strain.

5. **Literature is not strain-specific.** None of the reviewed abstracts concerns *P. putida* KT2440 specifically; all conclusions extrapolate from the conserved bacterial paradigm. This is expected for a housekeeping enzyme, but the caveat should be stated explicitly.

Despite these gaps, the annotation is robust: MraY is one of the most conserved and best-characterized enzymes in bacterial cell-wall synthesis, and the diagnostic domain architecture leaves little ambiguity about the identity and function of Q88N79.

---

## Proposed Follow-up Experiments / Actions

1. **Direct enzymatic confirmation.** Express and purify PP_1334 (in a detergent/membrane system) and assay phospho-MurNAc-pentapeptide transferase activity using *P. putida* UDP-MurNAc-pentapeptide and undecaprenyl phosphate, measuring Lipid I formation and UMP release; determine Km/kcat and Mg²⁺ dependence.

2. **Essentiality test in *P. putida* KT2440.** Use a conditional knockdown (e.g., CRISPRi or an inducible-promoter depletion) of PP_1334 and confirm growth arrest / lysis, depletion of Lipid I, and accumulation of UDP-MurNAc-pentapeptide, mirroring the *E. coli* Pmra depletion phenotype.

3. **Catalytic-residue validation.** Perform site-directed mutagenesis of the conserved aspartates and the essential histidine (aligned to His-289 of *B. subtilis*) to confirm they are required for activity in the *P. putida* enzyme.

4. **Inhibitor sensitivity profiling.** Test whether *P. putida* MraY is inhibited by tunicamycin, muraymycin D2, and capuramycin analogs, and whether these compounds arrest *P. putida* growth — relevant given *Pseudomonas*' notable intrinsic resistance mechanisms.

5. **Structural characterization.** Obtain a cryo-EM or crystal structure of PP_1334, ideally with a nucleoside inhibitor bound, to confirm the active-site architecture and enable structure-guided, species-selective inhibitor design.

6. **Localization and interaction mapping.** Use fluorescent fusions or membrane fractionation to confirm inner-membrane localization, and pull-down / bacterial two-hybrid assays to test for association with MurG and the divisome in *P. putida*.

---

## Conclusion

MraY (Q88N79 / PP_1334) in *Pseudomonas putida* KT2440 is an essential, polytopic integral cytoplasmic-membrane enzyme — phospho-N-acetylmuramoyl-pentapeptide transferase / translocase (EC 2.7.8.13) — that catalyzes the first membrane-committed step of peptidoglycan biosynthesis. At the inner leaflet of the plasma membrane it transfers the phospho-MurNAc-pentapeptide moiety from cytoplasmic UDP-MurNAc-pentapeptide onto the lipid carrier undecaprenyl phosphate, generating Lipid I and releasing UMP in a reversible, Mg²⁺-dependent, ordered ternary-complex reaction. It thereby couples the cytoplasmic Mur pathway to membrane-bound cell-wall assembly, hands Lipid I to MurG (→ Lipid II), is encoded within the conserved *mra*/*dcw* division-and-cell-wall gene cluster, and is a clinically important, human-absent antibacterial target. All conclusions for the *P. putida* protein are inferred by strong homology (HAMAP MF_00038) from biochemically and structurally characterized MraY orthologs.

---

*Search date: 2026-07-23. Primary sources are peer-reviewed biochemical, structural, genetic, and review articles indexed in PubMed; database annotation (UniProt/HAMAP) is used only to transfer the well-established function to the specific ortholog.*


## Artifacts

- [OpenScientist final report](mraY-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mraY-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:31138496
2. PMID:15131133
3. PMID:27312048
4. PMID:18081839
5. PMID:27226570
6. PMID:27088606
7. PMID:9721276
8. PMID:31471595
9. PMID:18791230
10. PMID:29459785
11. PMID:29778697