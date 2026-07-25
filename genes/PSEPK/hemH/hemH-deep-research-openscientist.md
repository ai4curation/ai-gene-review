---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-20T20:09:55.755018'
end_time: '2026-07-20T20:23:37.914125'
duration_seconds: 822.16
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: hemH
  gene_symbol: hemH
  uniprot_accession: Q88PV4
  protein_description: 'RecName: Full=Ferrochelatase {ECO:0000255|HAMAP-Rule:MF_00323};
    EC=4.98.1.1 {ECO:0000255|HAMAP-Rule:MF_00323}; AltName: Full=Heme synthase {ECO:0000255|HAMAP-Rule:MF_00323};
    AltName: Full=Protoheme ferro-lyase {ECO:0000255|HAMAP-Rule:MF_00323};'
  gene_info: Name=hemH {ECO:0000255|HAMAP-Rule:MF_00323}; OrderedLocusNames=PP_0744;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ferrochelatase family. {ECO:0000255|HAMAP-
  protein_domains: Ferrochelatase. (IPR001015); Ferrochelatase_C. (IPR033644); Ferrochelatase_N.
    (IPR033659); Ferrochelatase (PF00762)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: hemH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: hemH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88PV4
- **Protein Description:** RecName: Full=Ferrochelatase {ECO:0000255|HAMAP-Rule:MF_00323}; EC=4.98.1.1 {ECO:0000255|HAMAP-Rule:MF_00323}; AltName: Full=Heme synthase {ECO:0000255|HAMAP-Rule:MF_00323}; AltName: Full=Protoheme ferro-lyase {ECO:0000255|HAMAP-Rule:MF_00323};
- **Gene Information:** Name=hemH {ECO:0000255|HAMAP-Rule:MF_00323}; OrderedLocusNames=PP_0744;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ferrochelatase family. {ECO:0000255|HAMAP-
- **Key Domains:** Ferrochelatase. (IPR001015); Ferrochelatase_C. (IPR033644); Ferrochelatase_N. (IPR033659); Ferrochelatase (PF00762)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "hemH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'hemH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **hemH** (gene ID: hemH, UniProt: Q88PV4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *hemH* (Ferrochelatase, Q88PV4) in *Pseudomonas putida* KT2440

## 1. Summary / Answer to the Research Question

**hemH** (locus **PP_0744**; UniProt **Q88PV4**) of *Pseudomonas putida* KT2440 encodes **protoporphyrin ferrochelatase** (heme synthase / protoheme ferro-lyase; **EC 4.98.1.1**), the terminal enzyme of the tetrapyrrole/heme‑biosynthetic pathway. Its primary function is to catalyze the insertion of one **ferrous iron (Fe²⁺) ion into protoporphyrin IX**, releasing two protons and producing **protoheme IX (heme *b*)** — the essential cofactor of cytochromes, catalases, and peroxidases. Because *P. putida* is a Gram‑negative (diderm) bacterium, its ferrochelatase belongs to the classical **protoporphyrin‑dependent** branch of heme biosynthesis and acts on **protoporphyrin IX** (not coproporphyrin III). The enzyme works in the **cytoplasm / at the cytoplasmic face of the inner membrane**, where it obtains Fe²⁺ and the porphyrin precursor and hands off heme to apo‑hemoproteins.

---

## 2. Gene / Protein Identity Verification

| Attribute | Value |
|---|---|
| Gene symbol | *hemH* |
| Ordered locus | PP_0744 |
| UniProt | Q88PV4 |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125), a Gram‑negative γ‑proteobacterium |
| Protein | Ferrochelatase / heme synthase / protoheme ferro‑lyase |
| EC | 4.98.1.1 (reclassified from the historical 4.99.1.1) |
| Length / mass | 338 aa / 37.8 kDa |
| Family / domains | Ferrochelatase family; PF00762, Ferrochelatase_N (IPR033659), Ferrochelatase_C (IPR033644) |

**Verification outcome — identity confirmed and unambiguous.** The gene symbol *hemH* is the canonical bacterial designation for ferrochelatase and is fully consistent with the protein description, family, and Pfam/InterPro domains. Orthology is quantitatively confirmed: Q88PV4 shares **43.9 % sequence identity with *E. coli* HemH (P23871)** with full conservation of the catalytic core (see §4). The catalytic activity, pathway assignment (protoheme from protoporphyrin‑IX, step 1/1), and the presence of the diagnostic ferrochelatase sequence motifs (see §4) all agree. There is no ambiguity of the kind that affects poorly characterized symbols; *hemH* → ferrochelatase is a one‑to‑one, well‑established assignment across bacteria. Direct genetic proof exists for orthologues: the cloned *hemH* gene is *necessary and sufficient* to rescue ferrochelatase‑deficient mutants, and its purified ~39‑kDa product carries ferrochelatase activity (Frustaci & O'Brian, 1993; PMID 8368826).

---

## 3. Primary Function: The Reaction Catalyzed

Ferrochelatase catalyzes the **final committed step** of heme biosynthesis:

> **Protoporphyrin IX + Fe²⁺ → protoheme IX (heme *b*) + 2 H⁺**
> (UniProt/Rhea RHEA:22584, written in the reverse sense as heme *b* + 2 H⁺ = protoporphyrin IX + Fe²⁺; EC 4.98.1.1)

"Ferrochelatase catalyzes the insertion of ferrous iron into a porphyrin macrocycle to produce the essential cofactor, heme" (Medlock et al., 2021; PMID 34402499). UniProt assigns the pathway as *"protoheme biosynthesis; protoheme from protoporphyrin‑IX: step 1/1"* — i.e., this enzyme performs the single, terminal metallation step. The product, heme *b*, is the prosthetic group of respiratory cytochromes (b/o/d oxidases, cytochrome *bc₁*), catalases and peroxidases, and other hemoproteins that are indispensable for the aerobic, respiratory lifestyle of *P. putida*.

**Substrate specificity.** *P. putida* is a diderm, so it uses the **protoporphyrin‑dependent** pathway and its ferrochelatase is a **protoporphyrin ferrochelatase (PpfC‑type)** whose porphyrin substrate is **protoporphyrin IX** (2 propionate + 2 vinyl substituents). This contrasts with the **coproporphyrin‑dependent** pathway "used almost exclusively by monoderm bacteria" (Gabler et al., 2024; PMID 38390750), discovered in 2015 (Gabler et al., 2022; PMID 34719106), in which coproporphyrin ferrochelatases (CpfC) act on the four‑propionate substrate coproporphyrin III. Correctly placing HemH in the protoporphyrin‑dependent branch is essential for defining its true substrate.

**Metal‑ion selectivity.** In vitro, ferrochelatases can insert several divalent metals (Fe²⁺, Co²⁺, Ni²⁺, Zn²⁺, Cu²⁺), but **Fe²⁺ is the physiological and kinetically preferred substrate** and, uniquely, is not subject to severe substrate inhibition (Hunter et al., 2008; PMID 18593702). Metals such as Mn²⁺, Pb²⁺, Cd²⁺, Hg²⁺ act as inhibitors; high‑resolution crystallography shows that this "inhibition" is **not** a failure to insert the metal but is set at the **product‑release** step via a conserved π‑helix conformational switch (Medlock et al., 2009; PMID 19703464). Thus physiological Fe²⁺ specificity is achieved largely through iron delivery and controlled product release rather than by simple exclusion of competing metals.

---

## 4. Mechanism and Structure–Function Mapping

Sequence analysis of Q88PV4 localizes the invariant ferrochelatase catalytic apparatus onto the *P. putida* protein:

- **N‑terminal `LGSP` motif (residues 11–14)** — part of the conserved porphyrin/metal‑binding pocket signature of the family.
- **His189**, embedded in the diagnostic **`SFHGLP`** motif — the conserved active‑site histidine (positionally homologous to *B. subtilis* His183 and human His263); annotated by UniProt as a binding site.
- **Glu294** — the conserved catalytic glutamate (homologous to *B. subtilis* Glu264 / human Glu343); annotated by UniProt as a binding site.

The catalytic cycle, established from structural, kinetic, HDX‑MS and QM/MM studies of homologues, comprises:

1. **Porphyrin binding and distortion.** Binding induces distortion of the tetrapyrrole macrocycle that exposes the pyrrole nitrogens; "distortion of the tetrapyrrole has been proposed to be an important component of the mechanism of metallation" (Karlberg et al., 2008; PMID 18423489, *B. subtilis* ferrochelatase).
2. **Proton abstraction / metal insertion.** The conserved His participates in metal handling and the conserved Glu drives deprotonation and product release: "structural data support a role for E343 in proton abstraction and product release" (Medlock et al., 2021; PMID 34402499). Fe²⁺ is delivered from the face opposite pyrrole‑proton abstraction.
3. **Product release** of heme *b*, gated by the conserved π‑helix conformational change that also underlies metal selectivity (Medlock et al., 2009; PMID 19703464).

**Possible [2Fe‑2S] cluster (bioinformatic + structural inference, not annotated).** Q88PV4 has 8 cysteines; four of them (**C213, C214, C225, C230**) fall within an internal ~18‑residue segment (`AADCC…VSSVCYRGQC`). This pattern matches the "new class" of bacterial protoporphyrin ferrochelatases that ligate a **[2Fe‑2S] cluster via four cysteines in an internal ~20‑residue segment** (Shepherd et al., 2006; PMID 16548850), distinct from the C‑terminal cluster of animal enzymes; such clusters were also confirmed in *Caulobacter* and *Mycobacterium* ferrochelatases (Dailey & Dailey, 2002; PMID 11948160).

*Structural support (Iteration 2).* The AlphaFold model **AF‑Q88PV4‑F1** (overall mean pLDDT 96.5) shows these internal cysteines converging into a compact pocket — SG–SG distances **C214–C225 = 3.4 Å, C213–C225 = 4.1 Å, C213–C214 = 3.9 Å** (with C230 ~8.6 Å away), all at high local confidence (pLDDT 85–98). Because AlphaFold does not place metals, the convergence of three thiols within ~3.5–4 Å is the geometric signature of a **metal/cofactor‑coordination site** rather than random surface cysteines.

*Comparative‑genomics support (Iteration 3).* Global alignment of Q88PV4 against *E. coli* HemH (P23871) — an enzyme **experimentally known to lack a [2Fe‑2S] cluster** — gives 43.9 % identity (clear orthology) with a fully conserved catalytic core (P. putida His189 ↔ *E. coli* His194; Glu294 ↔ Glu275; N‑terminal Leu11 ↔ Leu13). Crucially, *E. coli* HemH has only 4 cysteines total, and **three of P. putida's four internal cysteines are absent in *E. coli*** at the aligned positions: C213 ↔ *E. coli* Arg210, C225 ↔ Thr214, C230 ↔ Glu217 (only C214 ↔ *E. coli* Cys211). Thus *P. putida* carries exactly the extra cysteines expected of the cluster‑containing subclass, precisely where the cluster‑less enzyme does not.

Importantly, HAMAP rule MF_00323 does **not** annotate a cluster for Q88PV4, so this remains a **testable hypothesis** (best resolved by EPR/UV‑vis of the purified protein and Cys→Ser mutagenesis), not an established fact; if present, the cluster is proposed to modulate iron affinity/activity rather than be strictly required for catalysis.

---

## 5. Subcellular Localization

UniProt annotates the subcellular location of Q88PV4 as **cytoplasm**. Consistent with this, bacterial ferrochelatases are commonly **peripheral inner‑membrane proteins acting at the cytoplasmic face**; for example, the *Caulobacter crescentus* enzyme "is a homodimeric, membrane‑associated protein" (Dailey & Dailey, 2002; PMID 11948160). This localization places HemH where it can draw Fe²⁺ and protoporphyrin IX from the cytoplasm and deliver newly made heme *b* to membrane‑embedded apo‑hemoproteins (e.g., respiratory oxidases of the inner membrane).

---

## 6. Pathway Context

HemH acts at the very end of the conserved tetrapyrrole pathway:
glutamate → 5‑aminolevulinate (Hem A/L pathway) → porphobilinogen (HemB) → hydroxymethylbilane (HemC) → uroporphyrinogen III (HemD) → coproporphyrinogen III (HemE) → protoporphyrinogen IX (HemF/HemN) → **protoporphyrin IX (HemG/HemY)** → **heme *b* (HemH / ferrochelatase)**. In diderms such as *P. putida*, HemH is the sole terminal metallation step supplying heme for the respiratory chain and for oxidative‑stress defense enzymes (catalase/peroxidases). Its product heme *b* is also the precursor for heme *o*/heme *d* and *c*-type cytochrome maturation. Because heme is essential and Fe²⁺ is potentially toxic, this step sits at the intersection of iron homeostasis and respiratory metabolism, which is why the pathway (and ferrochelatase specifically) is an attractive antimicrobial target in pathogens (e.g., N‑methyl mesoporphyrin inhibition; Wu et al., 2009; PMID 19597542).

---

## 7. Supported and Refuted Hypotheses

**Supported**
- H1 — HemH/Q88PV4 is a protoporphyrin ferrochelatase catalyzing Fe²⁺ insertion into protoporphyrin IX to form heme *b* (EC 4.98.1.1). *Strongly supported* (UniProt/Rhea, HAMAP MF_00323, conserved motifs, homologue genetics PMID 8368826).
- H2 — Substrate is protoporphyrin IX because *P. putida* is a diderm using the protoporphyrin‑dependent pathway. *Supported* (PMID 34719106, 38390750).
- H3 — Catalysis proceeds via porphyrin distortion + His/Glu‑mediated proton abstraction/metal insertion; His189 and Glu294 are the catalytic residues. *Supported* (PMID 18423489, 34402499).
- H4 — Physiological Fe²⁺ specificity is governed by iron delivery / product release. *Supported* (PMID 19703464, 18593702).
- H5 — Enzyme functions in the cytoplasm / cytoplasmic face of the inner membrane. *Supported* (UniProt; PMID 11948160).

**Open / Not yet resolved**
- H6 — P. putida HemH binds an internal‑ligand [2Fe‑2S] cluster (four internal Cys). *Plausible but unproven, now with three converging lines of inference*: (i) internal 4‑Cys motif matching the Shepherd/Dailey cluster subclass (PMID 16548850, 11948160); (ii) AlphaFold geometry placing three thiols within 3.4–4.1 Å; (iii) comparative alignment showing three of these cysteines are absent in the cluster‑less *E. coli* enzyme. Still requires experimental spectroscopy/mutagenesis; not annotated by UniProt/HAMAP.

**Refuted / Excluded**
- The enzyme is **not** a coproporphyrin ferrochelatase (CpfC) and does **not** use coproporphyrin III as its physiological substrate, because that pathway is restricted to monoderm bacteria (PMID 38390750).

---

## 8. Limitations and Future Directions

- **Evidence is largely by homology.** No dedicated biochemical or genetic study of the *P. putida* KT2440 HemH protein was found in targeted PubMed searches (Iterations 1–2); functional assignment rests on the highly conserved ferrochelatase family, UniProt/HAMAP rule‑based annotation, sequence‑motif mapping, AlphaFold structure, and experiments on orthologues (*B. subtilis*, human, *B. japonicum*, *E. coli*, *L. lactis*). This absence is expected for a housekeeping enzyme in a non‑pathogen and does **not** indicate ambiguity: the *hemH* → ferrochelatase assignment is unambiguous. Precise kinetics (kcat, Km for protoporphyrin IX and Fe²⁺) for the *P. putida* enzyme remain to be measured.
- **[2Fe‑2S] status unresolved.** The internal four‑cysteine motif is suggestive but must be tested directly (EPR/UV‑vis, Cys→Ser variants), since related γ‑proteobacteria (e.g., *E. coli*) lack the cluster.
- **Localization inferred.** UniProt lists "cytoplasm"; the degree of inner‑membrane association specific to *P. putida* has not been experimentally mapped.
- **Future work:** heterologous expression and purification of PP_0744; steady‑state kinetics and metal/porphyrin specificity; cofactor spectroscopy; crystal/cryo‑EM structure; conditional knockdown to confirm essentiality and heme auxotrophy in *P. putida*.

---

### Key References
- Medlock et al. 2021, *Insight into the function of active site residues in the catalytic mechanism of human ferrochelatase* — PMID 34402499
- Karlberg et al. 2008, *Porphyrin binding and distortion… B. subtilis ferrochelatase* — PMID 18423489
- Medlock et al. 2009, *Product release rather than chelation determines metal specificity* — PMID 19703464
- Hunter et al. 2008, *Metal ion substrate inhibition of ferrochelatase* — PMID 18593702
- Gabler et al. 2024/2022, *Coproporphyrin ferrochelatase / coproporphyrin‑dependent pathway* — PMID 38390750, 34719106
- Shepherd et al. 2006 & Dailey & Dailey 2002, *[2Fe‑2S]‑cluster‑containing bacterial ferrochelatases* — PMID 16548850, 11948160
- Frustaci & O'Brian 1993, *hemH encodes ferrochelatase (B. japonicum)* — PMID 8368826
- Wu et al. 2009, *Heme pathway/ferrochelatase as drug target* — PMID 19597542


## Artifacts

- [OpenScientist final report](hemH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](hemH-deep-research-openscientist_artifacts/final_report.pdf)