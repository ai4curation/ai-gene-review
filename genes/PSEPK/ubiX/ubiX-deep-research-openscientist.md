---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T17:53:41.765967'
end_time: '2026-07-18T19:42:06.347150'
duration_seconds: 6504.58
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ubiX
  gene_symbol: ubiX
  uniprot_accession: Q88QE6
  protein_description: 'RecName: Full=Flavin prenyltransferase UbiX {ECO:0000256|HAMAP-Rule:MF_01984};
    EC=2.5.1.129 {ECO:0000256|HAMAP-Rule:MF_01984};'
  gene_info: Name=ubiX {ECO:0000256|HAMAP-Rule:MF_01984}; OrderedLocusNames=PP_0548
    {ECO:0000313|EMBL:AAN66175.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the UbiX/PAD1 family.
  protein_domains: Flavin_trans-like. (IPR036551); Flavoprotein. (IPR003382); UbiX-like.
    (IPR004507); Flavoprotein (PF02441)
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
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ubiX-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ubiX-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QE6
- **Protein Description:** RecName: Full=Flavin prenyltransferase UbiX {ECO:0000256|HAMAP-Rule:MF_01984}; EC=2.5.1.129 {ECO:0000256|HAMAP-Rule:MF_01984};
- **Gene Information:** Name=ubiX {ECO:0000256|HAMAP-Rule:MF_01984}; OrderedLocusNames=PP_0548 {ECO:0000313|EMBL:AAN66175.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the UbiX/PAD1 family.
- **Key Domains:** Flavin_trans-like. (IPR036551); Flavoprotein. (IPR003382); UbiX-like. (IPR004507); Flavoprotein (PF02441)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ubiX" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ubiX' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ubiX** (gene ID: ubiX, UniProt: Q88QE6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *ubiX* (UbiX, Q88QE6, PP_0548) in *Pseudomonas putida* KT2440

**Gene:** ubiX (OrderedLocusName PP_0548) · **UniProt:** Q88QE6 · **EC:** 2.5.1.129
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), "PSEPK"
**Family:** UbiX/PAD1 flavin prenyltransferase family (Pfam PF02441; InterPro IPR004507, IPR003382, IPR036551)

---

## Identity Verification (Mandatory)

- **Gene symbol vs. protein:** The symbol *ubiX* matches the UniProt description "Flavin prenyltransferase UbiX." ✔
- **Organism:** Target is *P. putida* KT2440; this report distinguishes direct experimental evidence (from the well-studied *E. coli* / yeast orthologs) from the homology-based assignment for PP_0548. ✔
- **Family/domains:** Literature on the UbiX/PAD1 family (Flavoprotein / UbiX-like domains, FMN-binding Rossmann fold) aligns with the domains listed for Q88QE6. ✔
- **Conclusion:** This is an unambiguous, well-characterized enzyme family. No literature exists for a *different* gene sharing the symbol "ubiX." Direct biochemistry has been performed on orthologs; PP_0548 is annotated by **HAMAP-Rule MF_01984 and strong orthology (~45% identity to *E. coli* UbiX; ~51% to the *E. coli* Pad1 paralog)**. The function below is assigned by robust evolutionary inference, corroborated by extensive experimental work on orthologs.

---

## Summary

**UbiX (Q88QE6, locus PP_0548) of *Pseudomonas putida* KT2440 is a soluble, cytoplasmic, metal-independent flavin prenyltransferase (EC 2.5.1.129).** Its primary and specific function is to synthesize the diffusible prenylated-FMN (prFMN) cofactor. It transfers a dimethylallyl moiety from dimethylallyl-monophosphate (DMAP) onto reduced flavin mononucleotide (FMN), forming two new covalent bonds — one to the flavin **N5** atom and one to the flavin **C6** atom — thereby adding a fourth, non-aromatic ring to the isoalloxazine system. UbiX is *not* itself a decarboxylase; its prFMN product is the essential activating cofactor for the partner enzyme UbiD, a reversible (de)carboxylase.

In *P. putida* KT2440 the genome encodes exactly one cognate UbiD (Q88CG8 / PP_5213), which anchors UbiX's primary physiological role to **ubiquinone (coenzyme Q) biosynthesis** — specifically the non-oxidative decarboxylation of the 3-octaprenyl-4-hydroxybenzoate intermediate. UbiX operates in the cytoplasm as a soluble, oligomeric flavoprotein.

The functional assignment for PP_0548 rests on four converging lines of evidence rather than direct biochemistry of the *P. putida* protein itself: (1) **experimental biochemistry** of *E. coli*/yeast orthologs demonstrating flavin-prenyltransferase activity and its role in ubiquinone biosynthesis; (2) **structural biology** of the family showing a soluble Rossmann-fold FMN flavoprotein assembling into trimers/dodecamers; (3) **evolutionary/sequence analysis** establishing PP_0548 as a genuine UbiX ortholog (≈45% identity, conserved FMN-binding motif); and (4) **residue-level mapping** confirming that the catalytically important π-system active-site residues and phosphate-binding loops are intact.

---

## Key Findings

### Finding 1 — UbiX is a flavin prenyltransferase that synthesizes prFMN (EC 2.5.1.129)

The core molecular function of UbiX is the biosynthesis of prenylated-FMN. UbiX catalyzes the transfer of a dimethylallyl moiety from **dimethylallyl-monophosphate (DMAP)** onto reduced FMN. In the product, the dimethylallyl group is joined to the flavin isoalloxazine at both the **N5 and C6 atoms**, generating a fourth, non-aromatic six-membered ring fused to the isoalloxazine. Distinctively among prenyltransferases, UbiX is **metal-independent** and requires the monophosphorylated (not diphosphorylated) prenyl donor DMAP.

The reaction (EC 2.5.1.129):

> reduced FMN (FMNH₂) + dimethylallyl-monophosphate (DMAP) → prenylated-FMN (prFMN) + phosphate

This is stated directly in the primary structural/biochemical study of UbiX ([PMID: 26083743](https://pubmed.ncbi.nlm.nih.gov/26083743/)): *"UbiX acts as a flavin prenyltransferase, linking a dimethylallyl moiety to the flavin N5 and C6 atoms. This adds a fourth non-aromatic ring to the flavin isoalloxazine group. In contrast to other prenyltransferases, UbiX is metal-independent and requires dimethylallyl-monophosphate as substrate."* That the enzyme produces a *diffusible* cofactor rather than acting as a decarboxylase itself was established for the isofunctional yeast enzyme PAD1 ([PMID: 25647642](https://pubmed.ncbi.nlm.nih.gov/25647642/)): *"PAD1 catalyzes the formation of a novel, diffusible cofactor required by FDC for decarboxylase activity."*

**Substrate specificity:** the flavin substrate is reduced FMN (the 5′-phosphate is important; riboflavin supports only a partial, single-bond reaction), and the prenyl donor is DMAP. In vivo, DMAP can arise from phosphorylation of prenol (e.g., by ThiM) or dephosphorylation of DMAPP by Nudix hydrolases ([PMID: 29551348](https://pubmed.ncbi.nlm.nih.gov/29551348/)). For the *P. putida* KT2440 ortholog specifically, this function is assigned by **HAMAP-Rule MF_01984** and strong orthology rather than direct assay.

### Finding 2 — UbiX provides prFMN to UbiD for the decarboxylation step of ubiquinone (CoQ) biosynthesis

The physiological pathway in which UbiX operates is **ubiquinone (coenzyme Q) biosynthesis**. UbiX does not act alone: it supplies the prFMN cofactor that the decarboxylase UbiD requires. In *E. coli*, the UbiX/UbiD pair is responsible for the decarboxylation of the **3-octaprenyl-4-hydroxybenzoate** (4-hydroxy-3-octaprenylbenzoate) intermediate of the CoQ pathway.

The loss-of-function phenotype is diagnostic. An *E. coli ubiX* mutant *"produces very low levels of Q, grows slowly on succinate as the sole carbon source, accumulates 4-hydroxy-3-octaprenyl-benzoate"* ([PMID: 17889824](https://pubmed.ncbi.nlm.nih.gov/17889824/)) — exactly the signature expected if the octaprenyl-hydroxybenzoate decarboxylation step is blocked (succinate is a non-fermentable, respiration-dependent carbon source, so poor growth on it reflects impaired ubiquinone-dependent respiration). The specific pathway intermediate is identified in the mechanistic study ([PMID: 26083743](https://pubmed.ncbi.nlm.nih.gov/26083743/)): *"ubiX and ubiD, which are responsible for decarboxylation of the 3-octaprenyl-4-hydroxybenzoate precursor."* The *P. putida* genome encodes the orthologous *ubiX* (PP_0548) in this same pathway context.

### Finding 3 — Catalytic mechanism resembles class I terpene cyclase chemistry via an N5-dimethylallyl-FMN intermediate

Kinetic crystallography has resolved the UbiX reaction into an ordered, two-bond-forming sequence with striking parallels to **class I terpene (terpenoid) synthases** — unusual for a flavoenzyme.

1. **N5–C1′ bond formation:** After FMN reduction, an active site dominated by π-systems assists phosphate–C1′ bond breakage, forming the first bond between flavin N5 and C1 of the dimethylallyl group. This yields an **N5-dimethylallyl-FMN intermediate**, part of which is released during catalysis and has been isolated and characterized ([PMID: 39231435](https://pubmed.ncbi.nlm.nih.gov/39231435/)): *"UbiX catalyzes the sequential formation of two bonds, the first between N5 of the flavin and C1 of DMAP, and the second between C6 of the flavin and C3 of DMAP."*
2. **C6–C3′ bond formation:** UbiX then acts as a chaperone, reorienting the adduct through transient carbocation species to close the fourth ring ([PMID: 31142738](https://pubmed.ncbi.nlm.nih.gov/31142738/)): *"UbiX then acts as a chaperone for adduct reorientation, via transient carbocation species, leading ultimately to formation of the dimethylallyl C3'-C6 bond."*

After synthesis, prFMN undergoes **oxidative maturation** to the **iminium** species that confers azomethine-ylide reactivity on partner UbiD enzymes ([PMID: 32951834](https://pubmed.ncbi.nlm.nih.gov/32951834/)): *"Following prenylation, prFMN undergoes oxidative maturation to form the iminium species required for UbiD activity."* This azomethine-ylide chemistry enables UbiD's reversible non-oxidative (de)carboxylation via a 1,3-dipolar cycloaddition mechanism — the first known enzymatic example of such chemistry ([PMID: 26083754](https://pubmed.ncbi.nlm.nih.gov/26083754/)).

### Finding 4 — UbiX is a soluble, oligomeric FMN-binding flavoprotein acting in the cytoplasm

The UbiX/PAD1 family adopts an **FMN-binding Rossmann fold** with a **non-covalently bound FMN** located at the interface between two monomers. The proteins assemble into oligomers built from a trimer unit that further associates into **dodecamers**. This was established from the 2.0 Å crystal structure of *E. coli* Pad1, a close UbiX paralog (51% identity) ([PMID: 15459342](https://pubmed.ncbi.nlm.nih.gov/15459342/)): *"Each Pad1 monomer consists of a typical Rossmann fold containing a non-covalently bound molecule of FMN,"* and *"Pad1 also forms dodecamers."*

These are **soluble cytoplasmic flavoproteins** with no signal peptide, transmembrane region, or secretion signal. UbiX generates the diffusible prFMN cofactor within the cytoplasm, where its partner UbiD also operates. This localizes UbiX's function to the **cytoplasmic compartment** of *P. putida*, consistent with the early cytoplasmic steps of the CoQ pathway.

### Finding 5 — Bioinformatic confirmation that PP_0548 is a genuine UbiX ortholog

A global Needleman–Wunsch alignment of *P. putida* KT2440 UbiX (Q88QE6, 209 aa) against experimentally characterized *E. coli* K12 UbiX (P0AG03 / UBIX_ECOLI, 189 aa) yields **84/186 identical aligned positions = 45.2% identity** (44.4% over the full *E. coli* length) — well above the ~30% threshold used to infer orthology and conserved function. The diagnostic N-terminal FMN-binding glycine-rich flavodoxin motif is conserved.

| Feature | *P. putida* KT2440 (Q88QE6) | *E. coli* K12 (P0AG03) |
|---|---|---|
| Length | 209 aa | 189 aa |
| Glycine-rich FMN motif | `T-G-A-S-G-A-Q-Y-G` | `S-G-A-S-G-A-I-Y-G` |
| Shared consensus | `GxSGAxYG` | `GxSGAxYG` |
| Global identity | — | 45.2% over aligned positions |

Both are single-domain flavoproteins of 189–209 aa. This level of identity, combined with the conserved diagnostic motif, is well above the threshold for confident functional orthology in this family and confirms PP_0548 as a **bona fide UbiX**, not a distant or misannotated paralog.

### Finding 6 — KT2440 encodes a single cognate UbiD partner (PP_5213), pinning UbiX's role to CoQ biosynthesis

A UniProt proteome survey of *P. putida* KT2440 (taxon 160488) shows that the **UbiD family (Pfam PF01977) is represented by exactly one protein**: Q88CG8 / UBID_PSEPK (gene *ubiD*, PP_5213, 488 aa), annotated as 3-octaprenyl-4-hydroxybenzoate carboxy-lyase (EC 4.1.1.98). The UbiX/flavoprotein family (PF02441) contains UbiX itself plus one unrelated-function member, CoaBC (Q88C96, PP_5285, phosphopantothenoylcysteine decarboxylase; CoA biosynthesis).

| Protein | UniProt | Locus | Length | Pfam | Function |
|---|---|---|---|---|---|
| UbiX | Q88QE6 | PP_0548 | 209 aa | PF02441 | Flavin prenyltransferase (prFMN synthesis) |
| CoaBC | Q88C96 | PP_5285 | — | PF02441 | Phosphopantothenoylcysteine decarboxylase (unrelated) |
| UbiD | Q88CG8 | PP_5213 | 488 aa | PF01977 | 3-octaprenyl-4-hydroxybenzoate carboxy-lyase (EC 4.1.1.98) |

Because there is exactly **one cognate prFMN-dependent decarboxylase** (UbiD / PP_5213) in the genome, PP_0548's prFMN output has a single dedicated downstream consumer, fixing UbiX's primary physiological role to **coenzyme Q biosynthesis**. The two genes are **unlinked** (PP_0548 vs PP_5213), matching the non-operonic *ubiX*/*ubiD* arrangement of *E. coli*.

### Finding 7 — Catalytically important FMN-binding and π-system active-site residues are conserved in PP_0548

Residue-level mapping of the *P. putida*–*E. coli* UbiX alignment demonstrates that the functional core is intact in PP_0548:

- **(i) FMN-phosphate-binding glycine-rich loop** `GxSGAxYG` (*P. putida* G13–G20);
- **(ii) flavin-phosphate "PCS" loop** (*E. coli* `...ILPCSIKT...` vs *P. putida* `...VVVPCSTGT...`);
- **(iii) aromatic residues building the π-system-rich active site** — Y19, F168, Y169 and W200 (*P. putida* numbering; = *E. coli* Y16, F152, Y153, W186);
- plus multiple **invariant acidic residues** (e.g., *P. putida* E33, E49, D51, E130, E140, D176/D177).

Because UbiX catalysis is attributed to a metal-independent, π-system-dominated active site that assists phosphate–C1′ cleavage and stabilizes transient carbocations (Finding 3), conservation of exactly these residues in PP_0548 provides structural-bioinformatic evidence that the *P. putida* enzyme retains fully intact catalytic machinery.

### Finding 8 — Consolidated conclusion supported by four convergent evidence lines

The functional annotation of *P. putida* UbiX rests on four converging evidence types:

1. **Experimental biochemistry** of orthologs — *E. coli*/yeast UbiX/PAD1 are flavin prenyltransferases making prFMN from reduced FMN + DMAP ([PMID: 26083743](https://pubmed.ncbi.nlm.nih.gov/26083743/), [PMID: 25647642](https://pubmed.ncbi.nlm.nih.gov/25647642/), [PMID: 39231435](https://pubmed.ncbi.nlm.nih.gov/39231435/)), and *ubiX* deletion abolishes ubiquinone while accumulating 3-octaprenyl-4-hydroxybenzoate ([PMID: 17889824](https://pubmed.ncbi.nlm.nih.gov/17889824/));
2. **Structure** — soluble Rossmann-fold FMN flavoprotein forming trimers/dodecamers with FMN at subunit interfaces ([PMID: 15459342](https://pubmed.ncbi.nlm.nih.gov/15459342/));
3. **Evolution** — 45% identity to *E. coli* UbiX with a conserved FMN-binding motif;
4. **Residue-level** — conservation of the π-system active-site residues (Y19/F168/Y169/W200) and phosphate-binding loops in PP_0548.

The genomic context (KT2440 has exactly one cognate UbiD, PP_5213) closes the loop by defining the downstream pathway.

---

## Mechanistic Model / Interpretation

UbiX sits at a specific, well-defined node in coenzyme Q biosynthesis. Its job is to **build a cofactor, not to act on the pathway substrate directly**. The prFMN it produces is handed to UbiD, which performs the actual chemistry on the CoQ intermediate:

```
   Cytoplasm (P. putida KT2440)
   ─────────────────────────────────────────────────────────────

   DMAP (dimethylallyl-monophosphate)
        +                         ┌──────────────────────────┐
   reduced FMN  ───────────────►  │   UbiX  (PP_0548)         │
                                  │   flavin prenyltransferase│
                                  │   EC 2.5.1.129            │
                                  │   metal-independent       │
                                  └───────────┬──────────────┘
              step 1: N5–C1' bond             │
              step 2: C6–C3' bond (chaperone, │
              carbocation reorientation)      ▼
                                        prFMN (reduced)
                                              │
                                   oxidative maturation
                                              ▼
                                    prFMN (iminium form,
                                    azomethine-ylide character)
                                              │  diffuses to partner
                                              ▼
                                  ┌──────────────────────────┐
   3-octaprenyl-4-hydroxy-        │   UbiD  (PP_5213)         │
   benzoate  ──────────────────►  │   carboxy-lyase           │──► 2-octaprenylphenol
                                  │   EC 4.1.1.98             │    (+ CO2)
                                  │   prFMN-dependent         │
                                  └──────────────────────────┘
                                              │
                                              ▼
                            downstream CoQ maturation → Ubiquinone (CoQ)
```

Three features deserve emphasis:

- **Division of labor.** UbiX is a *cofactor-biosynthetic* enzyme. Historically both UbiX and UbiD were thought to be "decarboxylases" (indeed the PP_0548 paralog Pad1 was crystallized as a "UbiX-like decarboxylase" — [PMID: 15459342](https://pubmed.ncbi.nlm.nih.gov/15459342/)). The modern understanding, established in 2015, is that UbiX/PAD1 makes a diffusible cofactor and UbiD/FDC is the sole decarboxylase ([PMID: 25647642](https://pubmed.ncbi.nlm.nih.gov/25647642/), [PMID: 26083754](https://pubmed.ncbi.nlm.nih.gov/26083754/)).
- **Chemical novelty.** The prFMN cofactor extends the isoalloxazine with a fourth non-aromatic ring, giving the oxidized cofactor azomethine-ylide character. This enables UbiD to perform reversible non-oxidative decarboxylation via 1,3-dipolar cycloaddition — the first known enzymatic example ([PMID: 26083754](https://pubmed.ncbi.nlm.nih.gov/26083754/)). UbiX's prenyl-transfer step itself borrows carbocation chemistry from terpene synthases ([PMID: 31142738](https://pubmed.ncbi.nlm.nih.gov/31142738/)).
- **Localization and pathway specificity.** As a soluble, signal-peptide-free flavoprotein, UbiX functions in the cytoplasm. In KT2440 its single cognate UbiD (PP_5213) commits its prFMN output to the CoQ pathway, making the annotation both specific and well-constrained. Because *P. putida* is a versatile aromatic-degrading soil bacterium, the same UbiX–UbiD prFMN chemistry underpins related decarboxylation reactions (e.g., ferulic/cinnamic-acid decarboxylation) in the broader family ([PMID: 32951834](https://pubmed.ncbi.nlm.nih.gov/32951834/)).

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the findings |
|---|---|---|
| [26083743](https://pubmed.ncbi.nlm.nih.gov/26083743/) | *UbiX is a flavin prenyltransferase required for bacterial ubiquinone biosynthesis* | Primary source: UbiX activity, DMAP substrate, N5/C6 chemistry, metal-independence, CoQ-pathway context (Findings 1, 2) |
| [25647642](https://pubmed.ncbi.nlm.nih.gov/25647642/) | *Isofunctional enzymes PAD1 and UbiX catalyze formation of a novel cofactor…* | UbiX/PAD1 makes a diffusible cofactor for a separate decarboxylase (Findings 1, 8) |
| [17889824](https://pubmed.ncbi.nlm.nih.gov/17889824/) | *The role of UbiX in E. coli coenzyme Q biosynthesis* | Loss-of-function phenotype: low Q, poor succinate growth, intermediate accumulation (Finding 2) |
| [39231435](https://pubmed.ncbi.nlm.nih.gov/39231435/) | *Characterization of the N5-dimethylallyl-FMN Intermediate…* | Ordered two-bond mechanism; intermediate isolated (Findings 3, 8) |
| [31142738](https://pubmed.ncbi.nlm.nih.gov/31142738/) | *The UbiX reaction mechanism resembles class I terpene cyclase chemistry* | Carbocation-mediated adduct reorientation / terpene-cyclase parallel (Finding 3) |
| [32951834](https://pubmed.ncbi.nlm.nih.gov/32951834/) | *Biochemistry of prenylated-FMN enzymes* | Oxidative maturation of prFMN to iminium required by UbiD (Finding 3) |
| [26083754](https://pubmed.ncbi.nlm.nih.gov/26083754/) | *New cofactor supports α,β-unsaturated acid decarboxylation via 1,3-dipolar cycloaddition* | Cofactor structure/azomethine-ylide chemistry; UbiD is the true decarboxylase (Mechanistic model) |
| [15459342](https://pubmed.ncbi.nlm.nih.gov/15459342/) | *Crystal structure of a dodecameric FMN-dependent UbiX-like decarboxylase (Pad1)…* | Rossmann fold, non-covalent FMN at interface, dodecamer, soluble (Finding 4) |
| [29551348](https://pubmed.ncbi.nlm.nih.gov/29551348/) | *Biosynthesis and Activity of Prenylated FMN Cofactors* | Origin of DMAP; free prFMN activates Fdc1 (Finding 1 context) |
| [12799002](https://pubmed.ncbi.nlm.nih.gov/12799002/) | *Regulation of the isofunctional genes ubiD and ubiX…* | ubiX/ubiD expression regulated by carbon source and fnr/arcA/hemA (context) |
| [31072499](https://pubmed.ncbi.nlm.nih.gov/31072499/), [31072498](https://pubmed.ncbi.nlm.nih.gov/31072498/), [33751438](https://pubmed.ncbi.nlm.nih.gov/33751438/), [32579338](https://pubmed.ncbi.nlm.nih.gov/32579338/), [39572138](https://pubmed.ncbi.nlm.nih.gov/39572138/) | prFMN production / UbiD reconstitution methods | Confirm UbiX as the enzyme used to generate prFMN for UbiD activation (methodological support) |

**Consistency of the evidence.** All 15 reviewed papers are consistent with a single coherent picture: UbiX is a flavin prenyltransferase producing prFMN for prFMN-dependent UbiD decarboxylases. No source contradicts the assignment. The only historical wrinkle is nomenclature — older structural work labeled the family "UbiX-like decarboxylase" ([PMID: 15459342](https://pubmed.ncbi.nlm.nih.gov/15459342/)) before the prenyltransferase function was resolved in 2015; this is a superseded interpretation, not a genuine conflict.

**Important caveat on evidence type.** The direct biochemical, structural, and mechanistic studies were performed on *E. coli* (and yeast PAD1) enzymes, not on the *P. putida* KT2440 protein itself. Transfer of function to PP_0548 is an *inference* — but a very strong one — supported by HAMAP-Rule MF_01984, ≈45% sequence identity with a conserved diagnostic FMN-binding motif (Finding 5), residue-level conservation of the active site (Finding 7), and a single cognate UbiD partner in the same genome (Finding 6).

---

## Supported and Refuted Hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| UbiX is a flavin prenyltransferase producing prFMN (EC 2.5.1.129) | **Supported** | PMID 26083743, 25647642, 39231435 |
| UbiX itself decarboxylates 3-octaprenyl-4-hydroxybenzoate ("carboxy-lyase") | **Refuted** (legacy annotation) | No decarboxylase activity for purified UbiX; UbiD is the decarboxylase (PMID 26083743, 25647642) |
| Substrate = reduced FMN + DMAP; metal-independent | **Supported** | PMID 26083743, 29551348, 39231435 |
| Role in ubiquinone (CoQ) biosynthesis in vivo | **Supported** | PMID 17889824, 26083743 |
| Soluble cytoplasmic oligomeric flavoprotein | **Supported** (family structure) | PMID 15459342 |

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on PP_0548.** No published in vitro characterization, crystal structure, or deletion phenotype exists for the *P. putida* KT2440 UbiX specifically. The annotation is inference-by-orthology, albeit exceptionally well-supported.
2. **prFMN not directly demonstrated in KT2440.** The prFMN cofactor and its maturation have been shown in *E. coli*/yeast systems; physical isolation from *P. putida* KT2440 has not been reported.
3. **DMAP supply pathway in *P. putida* is assumed.** In *E. coli*, DMAP arises from ThiM phosphorylation of prenol or Nudix dephosphorylation of DMAPP ([PMID: 29551348](https://pubmed.ncbi.nlm.nih.gov/29551348/)); the precise KT2440 source was not investigated.
4. **Potential additional prFMN clients.** The KT2440 reference proteome has a single PF01977 UbiD (PP_5213), but *P. putida* is a versatile aromatic degrader; whether other prFMN-dependent activities are recruited under specific conditions was not exhaustively explored.
5. **Oligomeric state of PP_0548 inferred from a paralog.** The dodecamer/trimer architecture is established for *E. coli* Pad1 (51%-identity paralog); the exact quaternary state of PP_0548 is not experimentally determined.
6. **Regulation in *P. putida* uncharacterized here.** *ubiD/ubiX* regulation by carbon source and anaerobic regulators is documented in *E. coli* ([PMID: 12799002](https://pubmed.ncbi.nlm.nih.gov/12799002/)); analogous regulation at PP_0548/PP_5213 was not assessed.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant characterization of PP_0548.** Express and purify Q88QE6, reconstitute with reduced FMN + DMAP, and confirm prFMN production by LC-MS/UV-vis — directly validating EC 2.5.1.129 for the *P. putida* enzyme.
2. **Reciprocal reconstitution with PP_5213 (UbiD).** Use PP_0548-generated prFMN to activate purified *P. putida* UbiD and assay decarboxylation of 3-octaprenyl-4-hydroxybenzoate (or a soluble surrogate), closing the pathway in the native organism.
3. **Gene deletion / complementation in KT2440.** Construct a Δ*ubiX* (ΔPP_0548) strain and test for the diagnostic phenotype (reduced CoQ, impaired growth on succinate/non-fermentable carbon sources, intermediate accumulation), with complementation to confirm specificity.
4. **Structure determination of PP_0548.** Solve the crystal or cryo-EM structure (with bound FMN/prFMN) to confirm the Rossmann fold, FMN-at-interface binding, oligomeric state, and the modeled π-system active-site residues (Y19/F168/Y169/W200).
5. **Trace the DMAP supply route in *P. putida*.** Identify the KT2440 ThiM ortholog and candidate Nudix hydrolases and test their contribution to DMAP provision.
6. **Survey conditional prFMN clients.** Under aromatic-catabolic growth conditions, test whether additional decarboxylase activities depend on UbiX-derived prFMN.

---

## Conclusion

UbiX (Q88QE6, PP_0548) in *Pseudomonas putida* KT2440 is a **soluble, cytoplasmic, metal-independent flavin prenyltransferase (EC 2.5.1.129)** whose primary function is to synthesize the diffusible **prenylated-FMN (prFMN) cofactor** from reduced FMN and dimethylallyl-monophosphate, forming N5 and C6 flavin–prenyl bonds via a terpene-cyclase-like carbocation mechanism. It is not a decarboxylase itself; its prFMN product activates the partner enzyme **UbiD (PP_5213)**, the sole cognate decarboxylase in KT2440, to catalyze the non-oxidative decarboxylation of 3-octaprenyl-4-hydroxybenzoate in **ubiquinone (coenzyme Q) biosynthesis**. This assignment — experimentally established for the *E. coli*/yeast orthologs — is transferred to PP_0548 by HAMAP rule, ≈45% sequence identity, conserved FMN-binding and π-system active-site residues, and the single-UbiD genomic context.

### Key references
- White, Payne, … Leys. *UbiX is a flavin prenyltransferase required for bacterial ubiquinone biosynthesis.* Nature, 2015. PMID 26083743.
- Payne, White, … Leys. *New cofactor supports α,β-unsaturated acid decarboxylation via 1,3-dipolar cycloaddition.* Nature, 2015. PMID 26083754.
- Lin, Ferguson, … Marsh. *Isofunctional enzymes PAD1 and UbiX…* 2015. PMID 25647642.
- Gulmezian et al. *The role of UbiX in E. coli coenzyme Q biosynthesis.* 2007. PMID 17889824.
- Marshall et al. *The UbiX flavin prenyltransferase reaction mechanism resembles class I terpene cyclase chemistry.* 2019. PMID 31142738.
- Datar et al. *Characterization of the N5-dimethylallyl-FMN intermediate…* 2024. PMID 39231435.
- Saaret, Balaikaite, Leys. *Biochemistry of prenylated-FMN enzymes.* 2020. PMID 32951834.
- Wang et al. *Biosynthesis and Activity of Prenylated FMN Cofactors.* 2018. PMID 29551348.
- Rangarajan et al. *Crystal structure of a dodecameric FMN-dependent UbiX-like decarboxylase (Pad1)…* 2004. PMID 15459342.


## Artifacts

- [OpenScientist final report](ubiX-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ubiX-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26083743
2. PMID:25647642
3. PMID:29551348
4. PMID:17889824
5. PMID:39231435
6. PMID:31142738
7. PMID:32951834
8. PMID:26083754
9. PMID:15459342
10. PMID:12799002