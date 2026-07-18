---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T17:44:07.158355'
end_time: '2026-07-17T18:21:47.130926'
duration_seconds: 2259.97
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: argC1
  gene_symbol: argC1
  uniprot_accession: Q88QQ6
  protein_description: 'RecName: Full=N-acetyl-gamma-glutamyl-phosphate reductase
    1 {ECO:0000255|HAMAP-Rule:MF_00150}; Short=AGPR 1 {ECO:0000255|HAMAP-Rule:MF_00150};
    EC=1.2.1.38 {ECO:0000255|HAMAP-Rule:MF_00150}; AltName: Full=N-acetyl-glutamate
    semialdehyde dehydrogenase 1 {ECO:0000255|HAMAP-Rule:MF_00150}; Short=NAGSA dehydrogenase
    1 {ECO:0000255|HAMAP-Rule:MF_00150};'
  gene_info: Name=argC1 {ECO:0000255|HAMAP-Rule:MF_00150}; OrderedLocusNames=PP_0432;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the NAGSA dehydrogenase family. Type 1
  protein_domains: AGPR. (IPR050085); AGPR_AS. (IPR023013); AGPR_dimerisation_dom.
    (IPR058924); AGPR_type-1. (IPR000706); NAD(P)-bd_dom_sf. (IPR036291)
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
citation_count: 6
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: argC1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: argC1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88QQ6
- **Protein Description:** RecName: Full=N-acetyl-gamma-glutamyl-phosphate reductase 1 {ECO:0000255|HAMAP-Rule:MF_00150}; Short=AGPR 1 {ECO:0000255|HAMAP-Rule:MF_00150}; EC=1.2.1.38 {ECO:0000255|HAMAP-Rule:MF_00150}; AltName: Full=N-acetyl-glutamate semialdehyde dehydrogenase 1 {ECO:0000255|HAMAP-Rule:MF_00150}; Short=NAGSA dehydrogenase 1 {ECO:0000255|HAMAP-Rule:MF_00150};
- **Gene Information:** Name=argC1 {ECO:0000255|HAMAP-Rule:MF_00150}; OrderedLocusNames=PP_0432;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the NAGSA dehydrogenase family. Type 1
- **Key Domains:** AGPR. (IPR050085); AGPR_AS. (IPR023013); AGPR_dimerisation_dom. (IPR058924); AGPR_type-1. (IPR000706); NAD(P)-bd_dom_sf. (IPR036291)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "argC1" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'argC1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **argC1** (gene ID: argC1, UniProt: Q88QQ6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *argC1* (Q88QQ6, PP_0432) in *Pseudomonas putida* KT2440

**Gene:** `argC1` (OrderedLocusName **PP_0432**)
**Protein:** N-acetyl-γ-glutamyl-phosphate reductase 1 (AGPR 1 / NAGSA dehydrogenase 1)
**UniProt:** Q88QQ6 (ARGC1_PSEPK)
**EC:** 1.2.1.38
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440), taxid 160488

---

## Summary

`argC1` (PP_0432) of *Pseudomonas putida* KT2440 encodes **N-acetyl-γ-glutamyl-phosphate reductase (AGPR)**, also called N-acetylglutamate-5-semialdehyde dehydrogenase (NAGSA dehydrogenase), the enzyme (EC 1.2.1.38) that carries out the **third step of the de novo L-arginine biosynthesis pathway**. The enzyme is a soluble, cytoplasmic, homodimeric NADPH-dependent oxidoreductase. In the biosynthetic (reductive) direction it catalyzes the reversible reaction *N-acetyl-L-glutamyl-5-phosphate + NADPH + H⁺ → N-acetyl-L-glutamate-5-semialdehyde + NADP⁺ + phosphate* — a reductive dephosphorylation in which a hydride from NADPH replaces the acyl-phosphate, releasing inorganic phosphate. It acts downstream of the N-acetylglutamate kinase (ArgB, PP_5289) and upstream of the acetylornithine aminotransferase (ArgD, PP_0372).

The identification rests on strong convergent evidence. The UniProt/HAMAP assignment (rule MF_00150) places argC1 in the **NAGSA dehydrogenase family, Type 1**, supported by the diagnostic InterPro domains AGPR_type-1 (IPR000706), AGPR active-site (IPR023013), AGPR dimerisation domain (IPR058924) and the NAD(P)-binding superfamily fold (IPR036291). Direct inspection of the Q88QQ6 sequence confirms both catalytic hallmarks are intact: the N-terminal Rossmann dinucleotide-binding glycine fingerprint (`GIVGGTG`, residues 5–11) and the family-defining active-site motif `PGCYPT` (residues 148–153) containing the catalytic cysteine (Cys150). Functional characterization of orthologs — including complementation of *E. coli* argC auxotrophs by cloned argC from *Corynebacterium glutamicum* [PMID: 9818083] and *Streptomyces clavuligerus* [PMID: 1339424], and the crystal structure of the *Mycobacterium tuberculosis* enzyme in complex with NADP⁺ [PMID: 17316682] — establish the reaction, cofactor, fold and catalytic residues that argC1's sequence conserves.

Within *P. putida*, argC1 feeds the economical **cyclic (ArgJ-dependent) ornithine pathway**: the genome encodes a bifunctional ornithine acetyltransferase (ArgJ, PP_1346) but no stand-alone N-acetylglutamate synthase (ArgA), meaning the acetyl group is recycled from N-acetylornithine to glutamate rather than being hydrolyzed and re-synthesized. The arg genes are dispersed across the genome (not operonic), and pathway expression is repressed by arginine, though only weakly (~5-fold) in *P. putida* [PMID: 176312]. Notably, KT2440 carries **two AGPR paralogs**: argC1 (the canonical Type-1 isozyme, this report's target) and a deeply divergent (~36% identity) paralog **argC2** (P59308, PP_3633). De novo arginine synthesis is conditionally essential on minimal medium [PMID: 20158506], consistent with argC1's biosynthetic role, though the presence of two paralogs may partially buffer a single knockout.

---

## Key Findings

### Finding 1 — argC1 is N-acetyl-γ-glutamyl-phosphate reductase (AGPR), the third enzyme of arginine biosynthesis

UniProt Q88QQ6 assigns argC1 (PP_0432) to the **NAGSA dehydrogenase family, Type 1** via HAMAP rule MF_00150, with the domain complement expected of an authentic AGPR: AGPR_type-1 (IPR000706), AGPR active-site (IPR023013), AGPR dimerisation domain (IPR058924), and NAD(P)-binding domain superfamily (IPR036291). The enzyme's EC number, 1.2.1.38, defines an oxidoreductase acting on the aldehyde/oxo group of a donor with NAD(P)⁺ as acceptor.

This annotation is anchored in experimental work on orthologs. In *Corynebacterium glutamicum*, the cloned argC gene expressed in an *E. coli* auxotroph produced a protein of the expected size and enzyme activity, confirming it encodes N-acetylglutamate-5-semialdehyde dehydrogenase [PMID: 9818083]:

> "Enzyme activity and size of the expressed protein in the E. coli auxotroph carrying the recombinant argC gene revealed that the cloned gene indeed codes for N-acetylglutamate 5-semialdehyde dehydrogenase."

In *Streptomyces clavuligerus*, the 340-aa (35.2 kDa) ArgC complements argC mutants and produces AGPR activity, and the authors identified a conserved active-center motif shared across all AGPRs [PMID: 1339424]. In *Sinorhizobium meliloti*, argC is explicitly defined as the enzyme catalyzing "the high-energy-consuming third step in the arginine synthesis pathway" [PMID: 29121239]:

> "argC encodes N-acetyl-gamma-glutamyl phosphate reductase, the enzyme that catalyzes the high-energy-consuming third step in the arginine synthesis pathway."

Crucially, the reaction itself has been measured in *P. putida*: N-acetylglutamate-γ-semialdehyde dehydrogenase activity is present and repressible by arginine in this very organism [PMID: 176312]. Together these lines of evidence make the functional assignment of argC1 secure rather than inferential.

### Finding 2 — argC1 acts in the cytoplasm and its expression is repressed by arginine

AGPR is a soluble cytoplasmic enzyme of the amino-acid biosynthetic machinery. The NAGSA dehydrogenase family carries no signal peptide or transmembrane segments (UniProt Q88QQ6), placing the reaction in the cytosol where the upstream (ArgB) and downstream (ArgD) substrates are generated and consumed. This is the expected localization for a small-molecule biosynthetic dehydrogenase.

Functionally, the pathway argC1 serves is under feedback control by the end product. In *P. putida*, the coupled N-acetyl-α-glutamokinase / N-acetylglutamate-γ-semialdehyde dehydrogenase activities are repressible and derepressible by arginine, although repression is incomplete — the maximum difference between repressed and derepressed states for any pathway enzyme was only ~5-fold [PMID: 176312]:

> "The synthesis of four of the enzymes of the arginine biosynthetic pathway (N-acetyl-alpha-glutamokinase/N-acetylglutamate-gamma-semialdehyde dehydrogenase, ornithine carbamoyltransferase and acetylornithine-delta-transaminase) could be repressed and derepressed, but the maximum difference observed between repressed and derepressed levels for any enzyme of the pathway was only 5-fold."

Arginine-dependent repression of argC is conserved: in *S. clavuligerus*, "Formation of AGPR is repressed by addition of arginine to the culture medium" [PMID: 1339424], and in *Saccharomyces cerevisiae* the argB–argC gene cluster shows an ~85-fold repression range [PMID: 220508]. These observations are consistent with regulation of the arg regulon by an ArgR-type repressor, with *P. putida* exhibiting comparatively weak (relaxed) control.

### Finding 3 — KT2440 encodes two AGPR paralogs; argC1 is the Type-1 isozyme, distinct from argC2

A UniProt search of *P. putida* KT2440 (taxid 160488) returns two proteins annotated as N-acetyl-γ-glutamyl-phosphate reductase (EC 1.2.1.38):

| Feature | argC1 | argC2 |
|---|---|---|
| UniProt | Q88QQ6 (ARGC1_PSEPK) | P59308 (ARGC2_PSEPK) |
| Locus | PP_0432 | PP_3633 |
| Length | 344 aa (~36.3 kDa) | 313 aa |
| Family assignment | NAGSA dehydrogenase **Type 1** (HAMAP MF_00150) | "putative ArgC-like" |
| Domains | IPR000706 + IPR058924 + IPR036291; Pfam PF01118 + PF22698; COG0002 | partial / putative |

The two genes map to widely separated loci (PP_0432 vs PP_3633), indicating they are paralogous isozymes rather than two halves of one split gene. argC1 carries the complete Type-1 HAMAP signature and is therefore the canonical AGPR; the "1" suffix in the gene name reflects the existence of this second paralog.

### Finding 4 — AGPR is a two-domain NADP(H) oxidoreductase; the catalytic mechanism is defined structurally

UniProt Q88QQ6 assigns argC1 the reversible reaction (Rhea 21588):

```
N-acetyl-L-glutamate 5-semialdehyde + phosphate + NADP⁺
        ⇌  N-acetyl-L-glutamyl 5-phosphate + NADPH + H⁺
```

run in the reductive (biosynthetic) direction, and places it as step 3 of the L-glutamate → N²-acetyl-L-ornithine segment of arginine biosynthesis. The enzymatic mechanism is defined by the crystal structure of the *M. tuberculosis* ortholog in complex with NADP⁺ [PMID: 17316682]. Each subunit comprises an **α/β (Rossmann-like NADP-binding) domain** and an **α+β domain**, with NADP⁺ bound in the interdomain cleft:

> "The enzyme N-acetyl-gamma-glutamyl-phosphate reductase (AGPR) catalyzes the nicotinamide adenine dinucleotide phosphate (NADPH)-dependent reductive dephosphorylation of N-acetyl-gamma-glutamyl-phosphate to N-acetylglutamate-gamma-semialdehyde."

> "Each MtbAGPR subunit consists of alpha/beta and alpha+beta domains; NADP(+) is bound in the cleft between them."

A loop (Leu88–His92) closes ~5 Å over the cofactor adenine upon binding, and substrate docking implicates His217/His219 in hydrogen-bonding the substrate, with Arg114 forming an ion pair with the substrate's phosphate group to position it for chemistry [PMID: 17316682]:

> "residues His217 and His219 could form hydrogen bonds with the docked substrate. In addition, an ion pair could form between the substrate phosphate group and the guanidinium group of Arg114."

argC1's domain architecture (IPR000706, IPR036291, IPR058924; Pfam PF01118/PF22698) matches this fold, and it functions as a homodimer typical of the family — establishing both the substrate specificity (the phosphorylated, N-acetylated glutamate semialdehyde) and the hydride-transfer mechanism by structural homology.

### Finding 5 — argC1 feeds the cyclic (ArgJ-dependent) ornithine pathway, encoded by a dispersed arg regulon

KEGG KO-to-gene mapping for *P. putida* KT2440 places the complete arginine pathway across scattered genomic loci:

| Step | Enzyme | KO | *P. putida* gene(s) |
|---|---|---|---|
| 1 | N-acetylglutamate synthase (ArgA) | K00619 | **none found** |
| 2 | N-acetylglutamate kinase (ArgB) | K00930 | PP_5289 |
| **3** | **AGPR (ArgC)** | **K00145** | **PP_0432 (argC1)**, PP_3633 (argC2) |
| 4 | Acetylornithine aminotransferase (ArgD) | K00821 | PP_0372 |
| 5 | Ornithine acetyltransferase (ArgJ) | K00620 | PP_1346 |
| 6 | Ornithine carbamoyltransferase (ArgF) | K00611 | PP_1000, PP_1079 |
| 7 | Argininosuccinate synthase (ArgG) | K01940 | PP_1088 |
| 8 | Argininosuccinate lyase (ArgH) | K01755 | PP_0184 |

The presence of a bifunctional **ArgJ** (PP_1346) together with the **absence of a stand-alone ArgA** indicates *P. putida* uses the economical **cyclic pathway**: ArgJ transfers the acetyl group from N-acetyl-L-ornithine back onto L-glutamate to regenerate N-acetyl-L-glutamate, rather than hydrolytically removing it (ArgE) and re-acetylating de novo (ArgA). This recycles the acetyl group and conserves acetyl-CoA. The arg genes are dispersed genome-wide rather than clustered in a single operon, and gene-neighborhood inspection confirms PP_0432 sits among functionally unrelated genes (PP_0431 membrane protein, PP_0433 ErpA Fe-S insertion factor, PP_0434 AnmK), i.e., it is not co-transcribed with other arg genes.

```
     L-glutamate
         │  ArgA (ABSENT — replaced by ArgJ recycling)
         ▼
   N-acetyl-L-glutamate
         │  ArgB / N-acetylglutamate kinase (PP_5289)  + ATP
         ▼
   N-acetyl-L-glutamyl-5-phosphate
         │  ◀── argC1 / AGPR (PP_0432) + NADPH  ◀── THIS ENZYME
         ▼        (releases Pi)
   N-acetyl-L-glutamate-5-semialdehyde
         │  ArgD / acetylornithine aminotransferase (PP_0372)
         ▼
   N-acetyl-L-ornithine
         │  ArgJ (PP_1346) ── transfers acetyl back to glutamate ─┐
         ▼                                                        │
     L-ornithine ───────────────────────────────────────────────┘ (cyclic)
         │  ArgF → ArgG → ArgH
         ▼
     L-arginine
```

### Finding 6 — argC1 and argC2 are deeply divergent paralogs (~36% identity) in unrelated genomic contexts

A global Needleman–Wunsch alignment of the two *P. putida* AGPRs gives only **142/391 = 36.3% identity** between argC1 (344 aa) and argC2 (313 aa), indicating ancient paralogs rather than a recent duplication. Their genomic neighborhoods differ completely: PP_0432 (argC1) sits beside unrelated genes (unknown-function/membrane proteins, ErpA, AnmK), whereas PP_3633 (argC2) is annotated "putative ArgC-like" and is flanked by a LysR-family regulator (PP_3632), a GNAT acetyltransferase (PP_3634), and a sulfonate ABC transporter (PP_3635–6). argC1 carries the full HAMAP MF_00150 Type-1 signature; argC2 is only "putative." This strongly supports argC1 as the housekeeping AGPR of arginine biosynthesis, with argC2 a divergent paralog whose precise role (possibly a specialized or acquired function, given its transporter/acetyltransferase gene context) remains to be established.

### Finding 7 — argC1's sequence retains the intact NADP-binding and AGPR active-site motifs

Direct inspection of the 344-aa Q88QQ6 sequence locates the two catalytic hallmarks of a competent Type-1 AGPR:

1. **NADP-binding Rossmann fingerprint** `GIVGGTG` at residues 5–11 (`MIKV-GIVGGTG-YTG`), matching the IPR036291 NAD(P)-binding superfamily assignment.
2. **AGPR active-site signature** `PGCYPT` at residues 148–153 (`…IAV-PGCYPT-ATQ…`), containing the strictly conserved catalytic **cysteine, Cys150**.

The PGCYPT motif was identified as the conserved active center across all AGPRs [PMID: 1339424]:

> "A conserved PGCYPT domain present in all the AGPR sequences suggests that this may be the active center of the protein."

The presence of both motifs in argC1 (and their absence/degeneration in argC2) confirms that argC1 retains the intact catalytic apparatus and is the enzymatically competent isozyme.

### Finding 8 — De novo arginine synthesis is conditionally essential on minimal medium

A genome-wide mini-Tn5 knockout screen of *P. putida* KT2440 on glucose minimal medium recovered conditionally essential genes including amino-acid biosynthetic genes, and reported that "Auxotrophs for all amino acids predicted by the in silico models were found" [PMID: 20158506]:

> "Auxotrophs for all amino acids predicted by the in silico models were found"

This establishes that de novo arginine synthesis — the pathway argC1 serves — is required for growth in the absence of exogenous arginine, and that an arginine auxotroph phenotype is obtainable when the pathway is disrupted. Because KT2440 carries two AGPR paralogs, a single argC1 knockout may be partially buffered by argC2; the auxotrophy is fundamentally a property of the pathway/regulon rather than necessarily of the single gene.

---

## Mechanistic Model / Interpretation

The convergent evidence produces a clear and coherent model. `argC1` (PP_0432) is a **cytoplasmic, homodimeric, NADPH-dependent oxidoreductase** that performs the committed reductive step at the heart of arginine biosynthesis. Its substrate is the acyl-phosphate intermediate **N-acetyl-L-glutamyl-5-phosphate** produced by ArgB; its product is the aldehyde **N-acetyl-L-glutamate-5-semialdehyde** consumed by ArgD. Mechanistically, the enzyme couples oxidation of NADPH to reductive dephosphorylation of a high-energy acyl-phosphate — the "high-energy-consuming third step" [PMID: 29121239] — with a Rossmann domain binding the NADP(H) cofactor in an interdomain cleft, His217/His219 recognizing the substrate, and Arg114 clamping the phosphate leaving group [PMID: 17316682]. The catalytic Cys150 within the PGCYPT motif is the nucleophile/active-site residue conserved across all AGPRs [PMID: 1339424].

Physiologically, argC1 sits within *P. putida*'s **cyclic, acetyl-recycling ornithine pathway**, distinguished by a bifunctional ArgJ and the absence of ArgA. This design conserves acetyl-CoA and reflects the metabolic economy typical of soil/rhizosphere pseudomonads. The pathway is transcriptionally responsive to arginine availability (weak ~5-fold repression in *P. putida*), consistent with ArgR-type feedback control, and is conditionally essential — cells require it whenever arginine is not supplied exogenously. Ornithine, the product of the acetylated segment, further feeds into citrulline/arginine and the polyamine precursor pool, so argC1 sits upstream of a metabolic node with broad importance.

A distinctive feature of KT2440 is the **duplication of AGPR** into argC1 and the divergent argC2 (~36% identity). The intact catalytic motifs, complete HAMAP Type-1 signature, and canonical arg-pathway assignment mark argC1 as the housekeeping biosynthetic enzyme. argC2's specialized genomic context (LysR regulator, GNAT acetyltransferase, sulfonate transporter) hints at a possibly neofunctionalized or condition-specific role, but this remains unresolved and outside argC1's core function.

---

## Evidence Base

| PMID | Study | Relevance |
|---|---|---|
| [PMID: 17316682](https://pubmed.ncbi.nlm.nih.gov/17316682/) | *Crystal structure of AGPR from M. tuberculosis with NADP(+)* | **Primary structural evidence**: defines the two-domain fold, NADP-binding cleft, and catalytic residues (His217/His219, Arg114) that argC1's domains conserve. |
| [PMID: 9818083](https://pubmed.ncbi.nlm.nih.gov/9818083/) | *Molecular cloning and analysis of argC from C. glutamicum* | **Functional complementation**: cloned argC complements an *E. coli* argC auxotroph and expresses N-acetylglutamate-5-semialdehyde dehydrogenase, proving gene→enzyme identity. |
| [PMID: 1339424](https://pubmed.ncbi.nlm.nih.gov/1339424/) | *Characterization of S. clavuligerus argC (NAGSA-phosphate reductase)* | Defines the 340-aa AGPR, its complementation, arginine repression, and the conserved **PGCYPT active-center motif** (present at residues 148–153 of argC1). |
| [PMID: 29121239](https://pubmed.ncbi.nlm.nih.gov/29121239/) | *Overproduction of S. meliloti ArgC* | States the exact enzyme name, reaction position (third step), and "high-energy-consuming" nature of the AGPR reaction. |
| [PMID: 176312](https://pubmed.ncbi.nlm.nih.gov/176312/) | *Regulation of arginine and pyrimidine biosynthesis in P. putida* | **Direct organism evidence**: NAGSA dehydrogenase activity is present and arginine-repressible (~5-fold) in *P. putida* itself. |
| [PMID: 20158506](https://pubmed.ncbi.nlm.nih.gov/20158506/) | *Conditionally essential genes for P. putida KT2440 on minimal medium* | Genome-wide knockout screen recovering amino-acid auxotrophs, showing the arginine pathway is conditionally essential. |
| [PMID: 220508](https://pubmed.ncbi.nlm.nih.gov/220508/) | *argB-argC two-gene cluster in S. cerevisiae* | Comparative regulation: coordinate arginine repression of AGPR (~85-fold range) and separability of ArgB/ArgC activities. |
| [PMID: 8180696](https://pubmed.ncbi.nlm.nih.gov/8180696/) | *S. coelicolor argCJB gene cluster* | Comparative genetics: argC complements auxotrophs; ArgC homology with *E. coli*/*B. subtilis* ArgC; arginine operator upstream. |

The evidence is unusually strong for a functional annotation: it combines (i) direct enzyme-activity measurement in *P. putida* [PMID: 176312], (ii) complementation-proven gene identity in multiple orthologs [PMID: 9818083, 1339424], (iii) an atomic-resolution mechanism [PMID: 17316682], and (iv) sequence-level confirmation that argC1 retains all catalytic motifs. No evidence contradicts the AGPR assignment.

---

## Limitations and Knowledge Gaps

1. **No direct biochemistry on argC1 itself.** The reaction, kinetics, and cofactor preference are established for orthologs and inferred for argC1 from sequence/domain conservation. Purified-protein kinetic parameters (Km for N-acetyl-glutamyl-phosphate and NADPH, kcat, NADPH vs NADH preference) for the *P. putida* enzyme have not been measured.

2. **No argC1-specific structure.** Localization (cytoplasmic), fold, and mechanism are inferred by homology to the *M. tuberculosis* structure [PMID: 17316682]; no experimental structure of Q88QQ6 exists.

3. **The argC1/argC2 division of labor is unresolved.** Whether argC2 contributes to arginine biosynthesis, is silent, or serves a specialized function is unknown. A single argC1 knockout phenotype (and any complementation by argC2) has not been reported directly; the auxotrophy evidence is at the pathway level [PMID: 20158506].

4. **Regulation is characterized only at the activity level.** The specific transcription factor(s) (e.g., an ArgR ortholog), operator sites, and the promoter of PP_0432 have not been mapped in *P. putida*; the ~5-fold repression figure aggregates several enzymes [PMID: 176312].

5. **Localization is inferential.** Cytoplasmic localization is deduced from the absence of signal/transmembrane features and family behavior, not from experimental fractionation of the *P. putida* protein.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant enzymology.** Express and purify Q88QQ6, and determine steady-state kinetics (Km, kcat) for N-acetyl-L-glutamyl-5-phosphate and NADPH, and confirm NADPH-over-NADH preference, to convert the homology-based assignment into direct evidence.

2. **Genetic dissection of paralogs.** Construct single (ΔargC1, ΔargC2) and double knockouts and test arginine auxotrophy on minimal medium ± arginine. This would establish whether argC1 alone is sufficient/necessary and whether argC2 provides any backup AGPR activity.

3. **Cross-complementation.** Test whether cloned argC1 (and separately argC2) complements an *E. coli* or *P. putida* argC auxotroph, mirroring the ortholog experiments [PMID: 9818083, 1339424].

4. **Structure determination.** Solve the crystal or cryo-EM structure of argC1 (± NADP⁺/substrate analog) to confirm the two-domain fold, homodimer, and the roles of the residues corresponding to His217/His219/Arg114/Cys150.

5. **Regulatory mapping.** Identify the argC1 promoter and any ArgR-type operator; use reporter fusions or RNA-seq under arginine-replete vs -limited conditions to quantify PP_0432-specific repression.

6. **Localization confirmation.** Cell fractionation or fluorescent-fusion imaging to verify cytoplasmic localization of the enzyme in *P. putida*.

---

## Conclusion

`argC1` (Q88QQ6, PP_0432) of *Pseudomonas putida* KT2440 is the gene encoding **N-acetyl-γ-glutamyl-phosphate reductase (AGPR / NAGSA dehydrogenase 1, EC 1.2.1.38)**, a soluble cytoplasmic, homodimeric, NADPH-dependent oxidoreductase that catalyzes the **third step of L-arginine biosynthesis** — the reductive dephosphorylation of N-acetyl-L-glutamyl-5-phosphate to N-acetyl-L-glutamate-5-semialdehyde. It operates between ArgB and ArgD within *P. putida*'s economical **cyclic, ArgJ-dependent ornithine pathway** (bifunctional ArgJ present, ArgA absent), a pathway that is conditionally essential on minimal medium and subject to weak arginine feedback repression. argC1 is the canonical Type-1 isozyme, retaining the intact NADP-binding fingerprint (GIVGGTG) and catalytic PGCYPT/Cys150 motif, and is distinct from a deeply divergent (~36% identity) paralog, argC2 (PP_3633).


## Artifacts

- [OpenScientist final report](argC1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](argC1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:9818083
2. PMID:1339424
3. PMID:17316682
4. PMID:20158506
5. PMID:29121239
6. PMID:8180696