---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-17T07:45:46.174838'
end_time: '2026-07-17T08:22:21.150822'
duration_seconds: 2194.98
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: ilvH
  gene_symbol: ilvH
  uniprot_accession: Q88DY9
  protein_description: 'RecName: Full=Acetolactate synthase small subunit {ECO:0000256|RuleBase:RU368092};
    Short=AHAS {ECO:0000256|RuleBase:RU368092}; Short=ALS {ECO:0000256|RuleBase:RU368092};
    EC=2.2.1.6 {ECO:0000256|RuleBase:RU368092}; AltName: Full=Acetohydroxy-acid synthase
    small subunit {ECO:0000256|RuleBase:RU368092};'
  gene_info: Name=ilvH {ECO:0000313|EMBL:AAN70252.1}; OrderedLocusNames=PP_4679 {ECO:0000313|EMBL:AAN70252.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the acetolactate synthase small subunit family.
  protein_domains: Acetalactate_synth_ssu. (IPR004789); Acetolactate_synth/TF_NikR_C.
    (IPR027271); Acetolactate_synth_ssu_C. (IPR019455); ACT-like_dom_sf. (IPR045865);
    ACT_dom. (IPR002912)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ilvH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ilvH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88DY9
- **Protein Description:** RecName: Full=Acetolactate synthase small subunit {ECO:0000256|RuleBase:RU368092}; Short=AHAS {ECO:0000256|RuleBase:RU368092}; Short=ALS {ECO:0000256|RuleBase:RU368092}; EC=2.2.1.6 {ECO:0000256|RuleBase:RU368092}; AltName: Full=Acetohydroxy-acid synthase small subunit {ECO:0000256|RuleBase:RU368092};
- **Gene Information:** Name=ilvH {ECO:0000313|EMBL:AAN70252.1}; OrderedLocusNames=PP_4679 {ECO:0000313|EMBL:AAN70252.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the acetolactate synthase small subunit family.
- **Key Domains:** Acetalactate_synth_ssu. (IPR004789); Acetolactate_synth/TF_NikR_C. (IPR027271); Acetolactate_synth_ssu_C. (IPR019455); ACT-like_dom_sf. (IPR045865); ACT_dom. (IPR002912)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ilvH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ilvH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ilvH** (gene ID: ilvH, UniProt: Q88DY9) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *ilvH* (PP_4679, Q88DY9) — Acetohydroxy-acid Synthase Small Regulatory Subunit in *Pseudomonas putida* KT2440

## Summary

The gene **ilvH** (ordered locus **PP_4679**; UniProt **Q88DY9**) of *Pseudomonas putida* strain KT2440 encodes the **small, non-catalytic regulatory subunit of acetohydroxy-acid synthase (AHAS)**, also called acetolactate synthase (ALS; EC 2.2.1.6). The protein is a compact 163-residue polypeptide built from two modules: an N-terminal **ACT domain** (residues ~4–78) and a C-terminal **ferredoxin-like domain**. This two-domain architecture, its length, and its genomic pairing with a single cognate large catalytic subunit are all identical to the well-characterized *Escherichia coli* AHAS III regulatory subunit IlvH, from which the functional model is soundly transferred (64.2% full-length amino-acid identity; identical 163-residue length).

The AHAS holoenzyme — a dimer of large catalytic subunits (in *P. putida*, **IlvI / PP_4680**) and small regulatory subunits (IlvH) — catalyzes the **first committed and common step of branched-chain amino acid (BCAA) biosynthesis**: the thiamine-diphosphate-dependent condensation of two molecules of pyruvate to (2S)-2-acetolactate (valine/leucine branch) or of pyruvate plus 2-oxobutanoate to 2-aceto-2-hydroxybutyrate (isoleucine branch). Critically, **IlvH itself does not catalyze this reaction**. Instead, it performs two allosteric functions: (1) its N-terminal ACT domain **activates** the otherwise nearly inactive catalytic subunit, boosting activity by several-fold; and (2) its ACT-domain interface **binds the end-product L-valine**, imposing feedback inhibition that throttles carbon flux into the pathway. IlvH is therefore best described as the **feedback-control valve** — the molecular sensor that couples intracellular valine concentration to the rate of BCAA synthesis.

The enzyme functions in the **cytoplasm** of this Gram-negative bacterium (unlike its mitochondrially targeted eukaryotic orthologs). Genome analysis shows that *P. putida* KT2440 encodes only **one** AHAS small subunit and one cognate large subunit, arranged in a BCAA-biosynthesis gene cluster (ilvI–ilvH–ilvC, PP_4680–PP_4679–PP_4678). This contrasts with enterobacteria such as *E. coli*, which carry three AHAS isozymes. Consequently, IlvH is **non-redundant**: it is the sole regulatory gatekeeper controlling the relative synthesis of isoleucine, valine and leucine in this organism. No direct biochemical study of the *P. putida* enzyme exists; the annotation rests on strong orthology-based inference, which is nonetheless robust given the exceptional conservation of the functionally critical effector-binding core.

---

## Key Findings

### F001 — IlvH is the small regulatory subunit of AHAS, not a catalytic enzyme

UniProt entry Q88DY9 describes a 163-amino-acid protein consisting of a single N-terminal ACT domain (residues 4–78) followed by a C-terminal ferredoxin-like domain, annotated as EC 2.2.1.6 and assigned to the "acetolactate synthase small subunit family." This length and two-domain architecture are **identical** to the *E. coli* AHAS III regulatory subunit IlvH (also 163 aa), whose crystal structure was solved by Kaplun and colleagues ([PMID: 16458324](https://pubmed.ncbi.nlm.nih.gov/16458324/)). That study defines IlvH explicitly as "the regulatory subunit of one of three AHAS isozymes expressed in *Escherichia coli*, AHAS III," describing the protein as "a dimer, with two βαββαβ ferredoxin domains in each monomer."

A crucial point of clarification concerns the automated UniProt FUNCTION line, which quotes the acetolactate-forming reaction (2 pyruvate + H⁺ = (2S)-2-acetolactate + CO₂; Rhea 25249). **This reaction is catalyzed by the holoenzyme through the large catalytic subunit, not by IlvH itself.** The small subunit is non-catalytic and regulatory. This is stated directly by Lonhienne and colleagues ([PMID: 22198286](https://pubmed.ncbi.nlm.nih.gov/22198286/)): "Acetohydroxyacid Synthases (AHASs) have separate small regulatory subunits which specifically activate the catalytic subunits with which they are associated." The distinction is essential to a correct functional annotation: IlvH modulates an enzyme; it is not the enzyme.

### F002 — IlvH activates the catalytic subunit and confers valine feedback inhibition via ACT-domain effector sites

The dual regulatory function of the AHAS small subunit is established most cleanly by in-vitro reconstitution of purified subunits. Working with the yeast AHAS system, Pang and Duggleby ([PMID: 10213630](https://pubmed.ncbi.nlm.nih.gov/10213630/)) showed that "the ilv6 protein stimulates the catalytic activity of the ilv2 protein by up to 7-fold" (specific activity rising from 6.8 to 49.0 U/mg) and, additionally, "confers upon it sensitivity to inhibition by valine" (Kᵢ = 0.16 mM). The two subunits associate tightly, with a dissociation constant of ~70 nM.

Structural and biochemical work localizes the inhibitory valine-binding sites to the **interface between paired N-terminal ACT domains** of the regulatory subunit. As Lonhienne and colleagues state, "the binding sites for the inhibitory amino acid(s) (valine or leucine) are in the interface between two ACT (small ligand binding) domains, and are apparently found in all AHAS regulatory subunits" ([PMID: 22198286](https://pubmed.ncbi.nlm.nih.gov/22198286/)). In *P. putida* IlvH the ACT domain spans residues 4–78, consistent with this effector-binding role. Among the branched-chain amino acids, feedback inhibition is typically strongest for valine; in the *Ralstonia eutropha* IlvBH system the reported IC₅₀ values were valine 1.2 mM < isoleucine 2.3 mM < leucine 5.4 mM ([PMID: 25081555](https://pubmed.ncbi.nlm.nih.gov/25081555/)).

| Property | Value | System | Source |
|---|---|---|---|
| Activation of catalytic subunit | up to ~7-fold (6.8 → 49.0 U/mg) | Yeast Ilv6/Ilv2 | [PMID: 10213630](https://pubmed.ncbi.nlm.nih.gov/10213630/) |
| Valine Kᵢ (feedback inhibition) | 0.16 mM | Yeast AHAS | [PMID: 10213630](https://pubmed.ncbi.nlm.nih.gov/10213630/) |
| Subunit dissociation constant (Kd) | ~70 nM | Yeast AHAS | [PMID: 10213630](https://pubmed.ncbi.nlm.nih.gov/10213630/) |
| Effector-site location | ACT-domain dimer interface | *E. coli* AHAS III | [PMID: 16458324](https://pubmed.ncbi.nlm.nih.gov/16458324/); [PMID: 22198286](https://pubmed.ncbi.nlm.nih.gov/22198286/) |
| BCAA inhibition potency | Val (1.2) < Ile (2.3) < Leu (5.4 mM) | *R. eutropha* IlvBH | [PMID: 25081555](https://pubmed.ncbi.nlm.nih.gov/25081555/) |

### F003 — Pathway, substrate specificity and localization: a cytoplasmic AHAS gates the first common step of BCAA biosynthesis

UniProt's RuleBase pathway annotation (RU368092) places the AHAS holoenzyme at "L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 1/4" and "L-valine biosynthesis; L-valine from pyruvate: step 1/4." The holoenzyme condenses two pyruvate molecules to (2S)-2-acetolactate on the valine/leucine branch, or pyruvate plus 2-oxobutanoate to 2-aceto-2-hydroxybutyrate on the isoleucine branch. These reactions require the cofactors **thiamine diphosphate (ThDP), flavin adenine dinucleotide (FAD) and a divalent metal cation (usually Mg²⁺)**, all bound by the large catalytic subunit. Reviews of bacterial AHAS state that "Bacterial AHAS (EC 2.2.1.6) catalyzes the biosynthesis of isoleucine, leucine and valine by utilizing cofactors like Thiamin Diphosphate (ThDP), Flavin Adenine Dinucleotide (FAD) and a divalent metal cation (Usually Mg(2+))" ([PMID: 25882218](https://pubmed.ncbi.nlm.nih.gov/25882218/)).

AHAS is the **branch-point gatekeeper** controlling the relative synthesis of the three BCAAs; as described for the *R. eutropha* enzyme, AHAS "serves as a gatekeeper for the biosynthesis of all three branched-chain amino acids" and shows strong selectivity toward 2-ketobutyrate as its second substrate (substrate specificity ratio R = 140 in that organism) ([PMID: 25081555](https://pubmed.ncbi.nlm.nih.gov/25081555/)). This substrate preference is what allows a single enzyme to partition flux appropriately between the isoleucine and valine/leucine branches.

Regarding **subcellular localization**: bacterial AHAS is a soluble cytoplasmic enzyme. In eukaryotes the orthologous small subunit is targeted to mitochondria — Pang and Duggleby note that "the protein localized in mitochondria where it undergoes removal of a transit peptide targeting sequence" ([PMID: 10213630](https://pubmed.ncbi.nlm.nih.gov/10213630/)). *P. putida* IlvH lacks any such transit peptide, consistent with the enzyme functioning in the bacterial cytoplasm. The holoenzyme stoichiometry is a "dimer of large and small chains" (UniProt SUBUNIT annotation).

### F004 — Conserved two-module design: the N-terminal ACT domain activates; the C-terminal domain enables valine feedback

*P. putida* IlvH is a full-length ortholog of *E. coli* AHAS III IlvH: 163 aa vs 163 aa, **64.2% identity** over 162 aligned positions (Needleman–Wunsch), with the N-terminal ACT domain being the most conserved segment. Elegant domain-dissection experiments on the *E. coli* protein reveal that the two functions map to different parts of the molecule. Mendel and colleagues showed that "the N-terminal portion (about 80 amino acid residues) of the SSU is thus necessary and sufficient for recognition and activation" of the catalytic subunit — a truncated Δ80 construct gave kcat/KM about twice that of wild-type — but crucially "none of these constructs binds valine or leads to a valine-sensitive enzyme on reconstitution" ([PMID: 12488095](https://pubmed.ncbi.nlm.nih.gov/12488095/)). In other words, **activation requires only the N-terminal ACT domain, whereas valine feedback requires the C-terminal portion as well.**

This separability is reinforced by work on a minimal activation peptide, which activates catalytic subunits even across species (yeast, *Arabidopsis*, tobacco), yet "this peptide totally lost its ability for feedback regulation by valine, thus suggesting different elements for enzymatic activation and feedback regulation" ([PMID: 23512804](https://pubmed.ncbi.nlm.nih.gov/23512804/)). The magnitude of the activation effect is striking: isolated *E. coli* large subunits retain only ~15% (AHAS I), <<1% (AHAS II) and ~3% (AHAS III) of holoenzyme activity, all of which is fully restored upon reconstitution with the small subunit — "the LSUs have only approximately 15, <<1 and approximately 3%, respectively, of the activity of their respective holoenzymes, but the holoenzymes can be reconstituted with complete recovery of activity" ([PMID: 19653643](https://pubmed.ncbi.nlm.nih.gov/19653643/)). The catalytic subunit is essentially non-functional without its regulatory partner.

### F005 — Genomic context: ilvH sits in a BCAA-biosynthesis cluster beside its catalytic partner ilvI and downstream ilvC

Genome annotation of *P. putida* KT2440 places three consecutive loci in the expected pathway order:

| Locus | Gene | Product | Length | Role |
|---|---|---|---|---|
| PP_4680 | *ilvI* | Acetolactate synthase, large subunit (EC 2.2.1.6) | 574 aa | Catalytic subunit of AHAS |
| PP_4679 | *ilvH* (Q88DY9) | Acetolactate synthase, small subunit | 163 aa | **Regulatory subunit (this study)** |
| PP_4678 | *ilvC* | Ketol-acid reductoisomerase (NADP⁺) | 338 aa | Second enzyme of the pathway |

The adjacency **ilvI–ilvH–ilvC** places the AHAS catalytic and regulatory subunits together with the downstream reductoisomerase, mirroring the enterobacterial ilvIH/ilvBN operon organization. This physical clustering supports co-expression and reinforces the functional pairing of IlvH with IlvI.

### F006 — *P. putida* KT2440 encodes a single dedicated AHAS holoenzyme; IlvH is the sole regulatory subunit

A genome-wide UniProt search of *P. putida* KT2440 (taxid 160488) returns **exactly one** AHAS small (regulatory) subunit — ilvH / PP_4679 / Q88DY9 (163 aa) — and **one** clear cognate large catalytic subunit — ilvI / PP_4680 / Q88DY8 (574 aa). This is a fundamental contrast with enterobacteria such as *E. coli*, which possess three AHAS isozymes (I, II and III) with distinct small subunits ilvN, ilvM and ilvH ([PMID: 22198286](https://pubmed.ncbi.nlm.nih.gov/22198286/); [PMID: 19653643](https://pubmed.ncbi.nlm.nih.gov/19653643/)). The two additional ~545–547 aa ThDP-enzyme homologs in the *P. putida* genome are not paired with an AHAS-type small subunit and therefore do not constitute additional AHAS isozymes.

The functional implication is important: because there is no isozyme redundancy, **IlvH is the single, non-redundant valine-feedback valve** for the entire organism. Any perturbation of its feedback function would directly affect BCAA homeostasis. It is also worth noting from the same body of work that "the small, regulatory subunits (SSUs) of AHAS I and AHAS III (ilvN and ilvH) are required for valine inhibition, but ilvN and ilvH can only confer valine sensitivity on their own LSUs" ([PMID: 19653643](https://pubmed.ncbi.nlm.nih.gov/19653643/)) — underscoring the specificity of subunit pairing.

### F007 — Structural conservation of the ACT effector/activation core supports retained function in *P. putida* IlvH

Partitioning the sequence identity by domain shows that the functionally critical N-terminal region is the most conserved:

| Domain | *E. coli* residues | Identity to *P. putida* IlvH |
|---|---|---|
| N-terminal ACT / activation domain | 1–80 | 67.5% (54/80) |
| C-terminal ferredoxin-like domain | 81–163 | 61.0% (50/82) |

The N-terminal effector-binding core is essentially invariant. The first 35 residues align as *E. coli* `MRRILSVLLENESGALSRVIGLFSQRGYNIESLTV` versus *P. putida* `MRHIISLLLENEPGALSRVVGLFSQRNYNIESLTV`, conserving the **`GALSRV…GLFSQR` β-strand motif** that lines the ACT effector interface. Notably, this includes the glycine at the position corresponding to *E. coli* Gly14, whose substitution is known to yield valine-feedback-resistant AHAS. The valine effector sites lie at the interface of paired N-terminal ACT domains, as Kaplun and colleagues determined: "the effector (valine) binding sites can be located tentatively in two symmetrically related positions in the interface between a pair of N-terminal domains" ([PMID: 16458324](https://pubmed.ncbi.nlm.nih.gov/16458324/)). The near-perfect conservation of exactly this region in *P. putida* IlvH is strong structural evidence that both the activation and valine-feedback functions are retained.

### F008 — No direct biochemical study of *P. putida* IlvH exists; annotation is soundly inferred from a well-characterized ortholog

Targeted PubMed searches for *Pseudomonas*-specific acetohydroxy-acid synthase / IlvH regulation returned **no primary studies of the *P. putida* KT2440 enzyme**. The functional model for Q88DY9 is therefore transferred from the enterobacterial ortholog (*E. coli* AHAS III IlvH). This transfer is justified by multiple converging lines of evidence: 64.2% full-length identity; identical 163-aa length; identical two-domain (ACT + ferredoxin) architecture; a conserved ACT effector core (67.5% identity in residues 1–80); and identical genomic pairing with a single cognate catalytic subunit (ilvI, PP_4680). Across multiple orthologs (*E. coli*, yeast, *R. eutropha*), the small subunit consistently activates the catalytic subunit and confers valine feedback ([PMID: 12488095](https://pubmed.ncbi.nlm.nih.gov/12488095/); [PMID: 10213630](https://pubmed.ncbi.nlm.nih.gov/10213630/); [PMID: 19653643](https://pubmed.ncbi.nlm.nih.gov/19653643/); [PMID: 22198286](https://pubmed.ncbi.nlm.nih.gov/22198286/)). The annotation is thus reliable, though it remains an inference rather than a direct measurement.

---

## Mechanistic Model / Interpretation

The picture that emerges is a compact, elegant allosteric control device. IlvH is a two-module protein in which each module carries out a distinct task, and the whole functions only in the context of the AHAS holoenzyme.

```
        BCAA BIOSYNTHESIS — FIRST COMMON STEP (cytoplasm, P. putida KT2440)

   Pyruvate + Pyruvate ──────────┐
                                 │        AHAS holoenzyme
   Pyruvate + 2-oxobutanoate ────┤     (dimer of large + small)
                                 │
                                 ▼
        ┌───────────────────────────────────────────────┐
        │   IlvI (PP_4680, 574 aa) — CATALYTIC subunit   │
        │   ThDP · FAD · Mg2+                             │
        │   near-inactive alone (~3% activity)           │
        └───────────────▲───────────────────────────────┘
                         │ activates (up to ~7x)
                         │
        ┌────────────────┴──────────────────────────────┐
        │   IlvH (PP_4679, 163 aa) — REGULATORY subunit  │
        │                                                │
        │   [N-term ACT domain, res 4-78]  → ACTIVATION  │
        │   [C-term ferredoxin-like domain] → needed for │
        │                                     Val feedback│
        │                                                │
        │   Val binds at ACT–ACT dimer interface  ──┐    │
        └───────────────────────────────────────────┼────┘
                                                     │
                         FEEDBACK INHIBITION ◄───────┘
                         (L-valine, end product)

                 ▼ products
   (2S)-2-acetolactate ──► ... ──► L-valine, L-leucine
   2-aceto-2-hydroxybutyrate ──► ... ──► L-isoleucine
                 │
                 ▼ (next enzyme in cluster)
   IlvC (PP_4678) ketol-acid reductoisomerase
```

**Two separable functions in one protein.** The N-terminal ACT domain docks onto the catalytic subunit and switches it on — without IlvH, IlvI retains only a few percent of its potential activity. This is the "accelerator." The C-terminal ferredoxin-like domain, together with the ACT domain, forms the valine sensor: when intracellular valine rises, it binds at the symmetric ACT-dimer interface and inhibits the holoenzyme. This is the "brake." The genetic dissection of the *E. coli* ortholog (F004) proves these are structurally distinct elements — one can delete the C-terminal region to keep activation but lose feedback.

**A single non-redundant valve.** Because *P. putida* KT2440 has only one AHAS (F006), IlvH is the organism's sole feedback controller for BCAA biosynthesis. Where *E. coli* distributes this control across three isozymes with different regulatory properties, *P. putida* concentrates it in one enzyme. This makes IlvH the definitive control point balancing isoleucine, valine and leucine production against demand, and coupling that production to the availability of the pyruvate/2-oxobutanoate precursor pool.

**Localization.** The enzyme operates in the cytoplasm; there is no signal or transit peptide, consistent with all bacterial AHAS enzymes and in contrast to the mitochondrial targeting of eukaryotic orthologs (F003).

**Confidence.** Every mechanistic claim about *P. putida* IlvH is an orthology-based inference (F008), but the inference is unusually well-supported because the *functionally decisive* residues — the ACT effector core lining the valine-binding interface — are the most conserved part of the whole protein (F007). When the parts that matter most for function are the parts best conserved, functional transfer is on its firmest footing.

---

## Evidence Base

| PMID | Title (abbreviated) | How it supports the annotation |
|---|---|---|
| [16458324](https://pubmed.ncbi.nlm.nih.gov/16458324/) | *Structure of the regulatory subunit of AHAS isozyme III from E. coli* | Defines IlvH as an AHAS regulatory subunit; establishes the ACT + ferredoxin architecture and localizes valine-binding to the N-terminal domain interface. |
| [22198286](https://pubmed.ncbi.nlm.nih.gov/22198286/) | *Allosteric regulation in AHASs* | States small subunits are regulatory, "specifically activate" catalytic subunits, and place inhibitory amino-acid sites at the ACT-domain interface. |
| [10213630](https://pubmed.ncbi.nlm.nih.gov/10213630/) | *Reconstitution of yeast AHAS subunits* | Direct reconstitution: small subunit activates catalytic subunit up to 7-fold, confers valine sensitivity (Kᵢ=0.16 mM); shows eukaryotic mitochondrial targeting. |
| [12488095](https://pubmed.ncbi.nlm.nih.gov/12488095/) | *N-terminal domain sufficient for activation of AHAS III* | Shows N-terminal ~80-residue ACT domain is necessary and sufficient for activation, but does not bind valine — separating activation from feedback. |
| [23512804](https://pubmed.ncbi.nlm.nih.gov/23512804/) | *Minimum activation peptide from ilvH* | Minimal peptide activates catalytic subunits across species but cannot mediate valine feedback — confirms separable functional elements. |
| [19653643](https://pubmed.ncbi.nlm.nih.gov/19653643/) | *Interactions between large and small AHAS subunits of E. coli* | Quantifies the strong activation effect (LSUs ~3–15% active alone, fully restored on reconstitution); documents the three-isozyme enterobacterial system. |
| [25882218](https://pubmed.ncbi.nlm.nih.gov/25882218/) | *Mechanisms of bacterial AHAS* | Establishes EC 2.2.1.6, the BCAA-biosynthesis pathway, and the ThDP/FAD/Mg²⁺ cofactor requirements of the holoenzyme. |
| [25081555](https://pubmed.ncbi.nlm.nih.gov/25081555/) | *2-ketoisovalerate pathway enzymes of R. eutropha H16* | Describes AHAS as the BCAA "gatekeeper," substrate selectivity toward 2-ketobutyrate, and BCAA inhibition potency (Val < Ile < Leu). |

Supplementary literature reviewed and consistent with this model includes structural work on fungal and plant AHAS ([PMID: 32640464](https://pubmed.ncbi.nlm.nih.gov/32640464/)), engineering of feedback-insensitive AHAS for valine overproduction in yeast ([PMID: 29477860](https://pubmed.ncbi.nlm.nih.gov/29477860/)) and *Corynebacterium glutamicum* ([PMID: 25697867](https://pubmed.ncbi.nlm.nih.gov/25697867/), [PMID: 40063103](https://pubmed.ncbi.nlm.nih.gov/40063103/)), NMR assignment of the *E. coli* AHAS I regulatory subunit IlvN in the valine-bound form ([PMID: 20383786](https://pubmed.ncbi.nlm.nih.gov/20383786/)), and crystal structures of two AHAS III small-subunit orthologs from *Thermotoga maritima* and *Nitrosomonas europaea* confirming the conserved ACT + ferredoxin fold ([PMID: 17586771](https://pubmed.ncbi.nlm.nih.gov/17586771/)). None of these challenge the annotation; collectively they reinforce the conserved regulatory role of the AHAS small subunit across bacteria, fungi and plants.

**No contradictory evidence** was found in the literature. The only nuance requiring care is the automated UniProt FUNCTION line, which attributes the catalytic reaction to the entry — this reflects the holoenzyme reaction, not an activity of IlvH itself (see F001).

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of the *P. putida* KT2440 protein.** The entire functional model (F008) is inferred by orthology. There is no published purification, kinetic characterization, or in-vivo mutant analysis of Q88DY9/PP_4679 specifically. The inference is strong but not a substitute for direct measurement.

2. **Quantitative regulatory parameters are borrowed.** Activation magnitude (~7-fold), valine Kᵢ (0.16 mM), and subunit Kd (~70 nM) come from yeast and *E. coli* systems (F002). The precise values for the *P. putida* enzyme — including the relative potency of valine vs. isoleucine vs. leucine as inhibitors — are unknown and could differ.

3. **Substrate-partitioning behavior not measured for this organism.** While AHAS enzymes generally favor 2-oxobutanoate as the second substrate (giving the isoleucine branch its selectivity), the specific R-value for the *P. putida* IlvIH holoenzyme has not been determined.

4. **Operon structure and transcriptional regulation not experimentally confirmed.** The ilvI–ilvH–ilvC gene order (F005) is inferred from genome annotation; whether these genes form a single transcriptional unit, and how the operon is regulated (e.g., attenuation, global regulators) in *P. putida*, has not been established here.

5. **Structural model is homology-based.** No experimental structure of *P. putida* IlvH exists; the effector-site conservation argument (F007) relies on sequence alignment to solved orthologous structures.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant reconstitution and kinetics.** Co-express and purify *P. putida* IlvI (PP_4680) and IlvH (PP_4679), then measure (a) fold-activation of IlvI by IlvH, (b) the valine Kᵢ and the relative potency of Ile/Leu, and (c) the subunit Kd. This would convert the orthology inference into direct measurement.

2. **Substrate-specificity assay.** Determine the R-value (preference for 2-oxobutanoate vs. pyruvate as second substrate) of the reconstituted holoenzyme to quantify how flux is partitioned between the isoleucine and valine/leucine branches.

3. **Site-directed feedback-resistance mutants.** Introduce substitutions in the conserved ACT effector core (e.g., at the position corresponding to *E. coli* Gly14, or the *S. cerevisiae* Asn86/Gly89/Asn104-equivalent residues shown to relieve inhibition; [PMID: 29477860](https://pubmed.ncbi.nlm.nih.gov/29477860/)) to test whether valine feedback can be abolished while retaining activation — confirming the two-module model in this organism.

4. **In-vivo phenotyping.** Construct an *ilvH* deletion in *P. putida* KT2440 and test for BCAA auxotrophy or valine-hypersensitivity; complement with wild-type and feedback-resistant IlvH to confirm the non-redundant regulatory role (F006).

5. **Operon-structure verification.** Use RT-PCR / RNA-seq to confirm whether ilvI–ilvH–ilvC are co-transcribed and characterize transcriptional regulation of the cluster.

6. **Experimental or refined structural model.** Solve or model the *P. putida* IlvH structure (and, ideally, the IlvIH holoenzyme) to visualize the valine-binding interface and validate the conservation-based prediction.

---

## Conclusion

*ilvH* (PP_4679, Q88DY9) encodes the small, non-catalytic **regulatory subunit of acetohydroxy-acid synthase (AHAS, EC 2.2.1.6)** in the cytoplasm of *Pseudomonas putida* KT2440. Through its N-terminal ACT domain it allosterically **activates** the large catalytic subunit IlvI (PP_4680) — which is nearly inactive alone — while its ACT-dimer interface **binds L-valine** to impose end-product feedback inhibition. The holoenzyme it regulates catalyzes the first common, committed step of branched-chain amino acid biosynthesis. As the only AHAS small subunit encoded in this genome, IlvH is the non-redundant feedback-control valve gating carbon flux into isoleucine, valine and leucine. This annotation is inferred by strong orthology to the well-characterized *E. coli* AHAS III subunit rather than from direct study of the *P. putida* protein, but the inference is robust because the functionally decisive effector-binding core is the most conserved region of the molecule.


## Artifacts

- [OpenScientist final report](ilvH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ilvH-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:16458324
2. PMID:22198286
3. PMID:10213630
4. PMID:25081555
5. PMID:25882218
6. PMID:12488095
7. PMID:23512804
8. PMID:19653643
9. PMID:32640464
10. PMID:29477860
11. PMID:25697867
12. PMID:40063103
13. PMID:20383786
14. PMID:17586771