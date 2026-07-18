---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T14:47:05.010444'
end_time: '2026-07-11T15:00:50.196632'
duration_seconds: 825.19
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: rubA
  gene_symbol: rubA
  uniprot_accession: Q88C68
  protein_description: 'RecName: Full=Rubredoxin {ECO:0000256|PIRNR:PIRNR000071};'
  gene_info: Name=rubA {ECO:0000313|EMBL:AAN70880.1}; OrderedLocusNames=PP_5315 {ECO:0000313|EMBL:AAN70880.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the rubredoxin family.
  protein_domains: Rubredoxin. (IPR024922); Rubredoxin-like_dom. (IPR024934); Rubredoxin_dom.
    (IPR024935); Rubredoxin_ET. (IPR050526); Rubredoxin_Fe_BS. (IPR018527)
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
  path: rubA-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: rubA-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88C68
- **Protein Description:** RecName: Full=Rubredoxin {ECO:0000256|PIRNR:PIRNR000071};
- **Gene Information:** Name=rubA {ECO:0000313|EMBL:AAN70880.1}; OrderedLocusNames=PP_5315 {ECO:0000313|EMBL:AAN70880.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the rubredoxin family.
- **Key Domains:** Rubredoxin. (IPR024922); Rubredoxin-like_dom. (IPR024934); Rubredoxin_dom. (IPR024935); Rubredoxin_ET. (IPR050526); Rubredoxin_Fe_BS. (IPR018527)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "rubA" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'rubA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **rubA** (gene ID: rubA, UniProt: Q88C68) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of **rubA** (Rubredoxin, PP_5315 / UniProt Q88C68)
### *Pseudomonas putida* strain KT2440 (PSEPK)

---

## 1. Summary (Answer to the Research Question)

**RubA is a rubredoxin: a small (~55-residue), soluble, non-heme iron protein that acts as a one-electron carrier, not as an enzyme.** It harbours a single mononuclear iron atom held in a tetrahedral cage of four cysteine thiolates (a Fe(S-Cys)₄ centre) contributed by two CXXCG motifs. It shuttles reducing equivalents by cycling its iron between the Fe³⁺ and Fe²⁺ states. Physiologically, RubA is the mobile electron-shuttle of a compact electron-transport chain in which **NAD(P)H → rubredoxin reductase (AlkT, an FAD flavoprotein encoded by the adjacent gene PP_5314) → rubredoxin (RubA) → a terminal oxidoreductase acceptor.** In the canonical, structurally characterized version of this system the terminal acceptor is the membrane-bound alkane monooxygenase AlkB. RubA carries out its function in the **cytoplasm**, docking transiently with its partner proteins. Its function is inferred from its sequence/domain architecture, from the crystal structure of the near-identical *Pseudomonas aeruginosa* rubredoxin–rubredoxin reductase complex, and from mutagenesis of homologous alkane-system rubredoxins.

**Identity verification:** The gene symbol *rubA*, the organism (*P. putida* KT2440), the rubredoxin protein family, and the InterPro/Pfam rubredoxin domains are all mutually consistent. This is a genuine, correctly identified rubredoxin. One important caveat is discussed in Section 5: the alkane-degradation phenotype historically tied to *Pseudomonas* rubredoxins comes from a **different strain** (*P. putida* GPo1, OCT plasmid), and should not be assumed to operate in KT2440.

---

## 2. Molecular Identity and Cofactor

| Property | Value | Source |
|---|---|---|
| UniProt accession | Q88C68 | UniProt |
| Gene / locus | *rubA* / PP_5315 | UniProt, KEGG `ppu:PP_5315` |
| Length | 55 aa | UniProt sequence |
| Domain | Single Rubredoxin-like domain (res. 1–52) | Pfam PF00301; InterPro IPR024922, IPR018527 |
| Cofactor | 1 × mononuclear non-heme Fe | UniProt "Iron / Metal-binding" |
| Iron ligands | Cys6, Cys9, Cys39, Cys42 | UniProt binding-site features |

The sequence is:

```
MKKWQCIVCGLIYDEAEGWPDDGIAPGTRWEDVPEDWLCPDCGVGKSDFEMISIG
```

The four iron ligands form the two hallmark rubredoxin motifs, both of the **CXXCG** type:
- **C6-I-V-C9-G10** (`CIVCG`)
- **C39-P-D-C42-G43** (`CPDCG`)

These two loops wrap the iron into the classic tetrahedral Fe(S-Cys)₄ knuckle. This is the diagnostic architecture of the rubredoxin family: "*Common to most Rds are the two iron-binding CXXCG motifs*" (van Beilen et al., 2002, PMID 11872724). Rubredoxin is the structurally simplest of the iron–sulfur-type redox proteins — it contains **no acid-labile sulfide** and no Fe–Fe cluster, only a single iron. The redox chemistry is a simple one-electron Fe³⁺/Fe²⁺ couple, and the surrounding backbone and polar side chains fine-tune the reduction potential (Swartz & Ichiye, 1997, PMID 9370467; Swartz, Beck & Ichiye, 1996, PMID 8968568).

**Evidence type:** Bioinformatic (sequence/domain assignment, motif identification) corroborated by decades of structural biology on the rubredoxin fold.

### Structural sub-type: archetypal short single-domain rubredoxin
A pairwise comparison performed in this work places RubA firmly in the **canonical short, single-domain** rubredoxin class:

| Protein | Length | CXXC motifs | Best ungapped identity to Q88C68 |
|---|---|---|---|
| **Q88C68 (RubA, KT2440)** | 55 aa | 2 (pos 6, 39) | — |
| Rubredoxin, *Clostridium pasteurianum* (P00268) | 54 aa | 2 (pos 6, 39) | 53.7 % |
| **AlkG / Rubredoxin-2, GPo1** (P00272) | **173 aa** | **4 (pos 6, 39, 124, 157)** | 52.7 % (to one domain) |
| AlkT reductase (Q88C69, PP_5314) | 382 aa | 0 | 18 % (background) |

RubA (55 aa, two CXXC knuckles) is essentially the size and architecture of the textbook *Clostridium* rubredoxin, sharing ~54 % identity with it. It is emphatically **not** the elongated, two-domain GPo1 AlkG "Rubredoxin-2" (173 aa, four CXXC motifs = a degenerate N-terminal domain + linker + functional C-terminal iron domain). RubA also **lacks the AlkG1-diagnostic arginine insertion** downstream of its second CXXCG motif (…C39-P-D-C42-G-**V**GKSDF…), consistent with an electron-transfer-competent (non-AlkG1) rubredoxin. This classifies RubA as a generic, mobile single-iron electron carrier rather than a member of the specialized elongated alkane-rubredoxin lineage.

---

## 3. Primary Function: One-Electron Carrier

RubA is **not a catalytic enzyme** — it catalyzes no substrate transformation of its own. Its "substrate" in the functional sense is an electron: it accepts a single electron at its iron centre from a reduced donor and passes it to an acceptor. It is therefore best described as a **redox-active electron-transfer protein / electron shuttle** (UniProt: `electron transfer activity`, GO:0009055; `iron ion binding`, GO:0005506; keyword *Electron transport*).

### The AlkT–RubA electron-transport module
In *P. putida* KT2440, *rubA* (PP_5315) is immediately adjacent to and co-oriented with **PP_5314 (*alkT*, UniProt Q88C69)**, a **rubredoxin–NAD(⁺) reductase** (KEGG KO K05297; EC 1.18.1.1) — an FAD-dependent flavoprotein that oxidizes NAD(P)H. (Note: an earlier draft mislabeled the partner as "PP_5316/rubB"; the correct, verified reductase locus is **PP_5314/alkT** — there is no PP_5316 in the annotation.) The two genes form a minimal electron-relay:

```
NAD(P)H  ──►  AlkT/PP_5314 (FAD, rubredoxin reductase)  ──►  RubA/PP_5315 (Fe³⁺/Fe²⁺)  ──►  terminal acceptor
```

**Genomic and interaction evidence (this work):** KEGG places PP_5314 (alkT) and PP_5315 (rubA) directly adjacent on the complement strand (positions 6,061,555–6,062,703 and 6,062,720–6,062,887). In the STRING network (taxid 160488), *alkT* (PP_5314) is by far the top-ranked functional partner of *rubA*, with a combined confidence score of **0.999** (genomic neighborhood 0.75, gene-fusion/co-occurrence 0.90, co-expression 0.67, text-mining 0.90). A paralogous rubredoxin reductase (PP_5371, K05297) is encoded elsewhere, next to an aldehyde dehydrogenase (PP_5372), and STRING also links *rubA* (at lower, mostly text-mining-based confidence 0.72–0.75) to several aldehyde dehydrogenases (aldA, aldB-I, aldB-II) and to the ferric-uptake regulator Fur — hinting at possible connections to aldehyde metabolism and iron homeostasis that remain to be tested experimentally.

The mechanism and geometry of the AlkT→RubA step are known at atomic resolution from the near-identical *P. aeruginosa* system. Hagelueken et al. (2007, PMID 17636129) solved the crystal structure of the rubredoxin reductase (RdxR) both alone and **in complex with rubredoxin**, refined at 2.40/2.45 Å. Key mechanistic findings, all directly transferable to RubA/RubB:
- RdxR has two cofactor-binding domains plus a **C-terminal domain that specifically recognizes the rubredoxin**.
- Recognition is governed by only a "*small number of direct interactions*", consistent with a **transient, fast-exchange electron-transfer complex** — exactly what a mobile shuttle requires.
- The **shortest distance between the two redox centres (FAD ↔ rubredoxin Fe) is 6.2 Å**, short enough for efficient direct electron tunnelling.

### The downstream acceptor (canonical role)
In alkanotrophic organisms this three-component chain (NAD(P)H:rubredoxin reductase + rubredoxin) feeds electrons to the **membrane-bound, non-heme diiron alkane monooxygenase AlkB**, which uses them to activate O₂ and hydroxylate an inert C–H bond of an alkane:

- "*Rubredoxins (Rds) are essential electron transfer components of bacterial membrane-bound alkane hydroxylase systems*" (van Beilen et al., 2002, PMID 11872724).
- "*Electrons are typically supplied by NADH via a rubredoxin reductase (AlkT) to a rubredoxin (AlkG) to AlkB*"; AlkB is "*a non-heme diiron enzyme that catalyzes the hydroxylation of alkanes*" via "*two-electron reduction of its diferric active site*" (Williams et al., 2022, PMID 34990970).
- The *P. aeruginosa* chromosomal genes *rubB, rubA1, rubA2* "*constitute an electron transport (ET) pathway that shuttles reducing equivalents from carbon metabolism to the membrane-bound alkane hydroxylases AlkB1 and AlkB2*" (Hagelueken et al., 2007, PMID 17636129).

**Substrate specificity note:** Because RubA is an electron carrier, "substrate specificity" applies to its *protein partners*, not to a small molecule. Mutagenesis of alkane-system rubredoxins showed that partner specificity is encoded in surface residues: AlkG2-type rubredoxins can donate electrons to AlkB, whereas AlkG1-type cannot — largely because of an inserted arginine downstream of the second CXXCG motif (van Beilen et al., 2002, PMID 11872724). Functional interchangeability among alkane-system rubredoxins is well documented: rubredoxin "*can be replaced by rubredoxins from other alkane hydroxylase systems*" (Smits et al., 2002, PMID 11872725). RubA (Q88C68), lacking the AlkG1 arginine insertion and carrying two intact CXXCG knuckles, has the hallmarks of a functional electron-donating (AlkG2-like) rubredoxin.

**Evidence type:** Structural (crystallography of the homologous complex), biochemical/genetic (complementation and site-directed mutagenesis of homologs), and bioinformatic (operonic pairing with *alkT*/PP_5314; STRING score 0.999).

---

## 4. Subcellular Localization

RubA is a **soluble, cytoplasmic** protein (UniProt GO:0005737, cytoplasm). It has no signal peptide or transmembrane segment. It performs electron transfer in the aqueous cytoplasm, forming transient encounter complexes:
- On its reducing side, with the FAD domain of the cytoplasmic reductase AlkT/PP_5314 (the 6.2-Å redox-centre approach documented crystallographically for the homolog; Hagelueken et al., 2007, PMID 17636129).
- On its oxidizing side, with a terminal acceptor. When that acceptor is an integral-membrane monooxygenase such as AlkB, RubA delivers electrons at the cytoplasmic face of the inner membrane.

Thus RubA operates at the **cytoplasm / inner-membrane interface**, bridging soluble NAD(P)H-derived reducing power to a (frequently membrane-embedded) oxygen-activating enzyme.

---

## 5. Pathway Context and an Important Annotation Caveat

**Canonical pathway:** electron transfer for O₂-activating oxidoreduction — most famously the **alkane β-oxidation entry / alkane hydroxylation** pathway, where RubA-type rubredoxins reductively prime AlkB. This is reflected in the UniProt GO term `alkane catabolic process` (GO:0043448) attached to Q88C68.

**Caveat — do not over-interpret the alkane annotation for KT2440:**
- The extensively studied alkane-degradation rubredoxin **AlkG comes from *P. putida* GPo1**, where the *alk* genes reside on the **OCT plasmid** (Smits et al., 2002, PMID 11872725; van Beilen et al., 2002, PMID 11872724).
- ***P. putida* KT2440 — the organism of Q88C68 — is a plasmid-cured, non-alkanotrophic strain.** **Direct genomic check (this work):** a KEGG query confirms KT2440 encodes **no alkane 1-monooxygenase (KO K00496)** — i.e., no membrane diiron AlkB. The *alkT/rubA* pair therefore cannot be feeding an AlkB alkane hydroxylase, because none exists in this genome.
- **A naming trap, ruled out:** STRING lists a *rubA* partner named "alkB" (PP_3400, score 0.847). On inspection PP_3400 is **not** an alkane hydroxylase but an **α-ketoglutarate/Fe(II)-dependent DNA oxidative demethylase (KO K03919, EC 1.14.11.33)** — the DNA-alkylation-repair AlkB, an unrelated protein family. The edge is driven entirely by text-mining (text-mining sub-score 0.847; all other channels 0), a pure artifact of the ambiguous "alkB" symbol. There is no functional link between RubA and this DNA-repair enzyme.
- KEGG maps the reductase *alkT* (PP_5314) into the **Fatty acid degradation pathway (ppu00071)**, but this pathway is **incomplete** in KT2440 in the absence of a terminal alkane/fatty-acid hydroxylase.
- KT2440's *alkT/rubA* most closely mirrors the **chromosomal** *P. aeruginosa* *rubB/rubA1/rubA2* module. Hagelueken et al. explicitly note that this RdxR–Rdx redox couple "*also is crucial as part of the oxidative stress response in archaea or anaerobic bacteria*" and "*has been analyzed in detail as a model system for ET processes*" (2007, PMID 17636129).

**Interpretation:** For KT2440 specifically, the GO `alkane catabolic process` label is best read as a **family-inherited (electronic) inference**, not a demonstrated phenotype — and the genome positively lacks the AlkB that the label presumes. The demonstrated, transferable facts are (i) RubA is a rubredoxin electron carrier and (ii) it is the shuttle of an NADH→AlkT(PP_5314)→RubA relay. The identity of the physiological terminal acceptor in KT2440 has not been established experimentally; plausible roles include general provision of low-potential reducing equivalents to O₂-activating oxidoreductases and participation in the oxidative-stress response, by analogy to the *P. aeruginosa* and anaerobe systems.

---

## 6. Supported and Refuted Hypotheses

**Supported**
- **H1 — RubA is a bona fide rubredoxin with a mononuclear Fe(S-Cys)₄ centre.** Supported by sequence (Cys6/9/42/39 ligands, two CXXCG motifs), Pfam PF00301, InterPro rubredoxin domains. *(High confidence.)*
- **H2 — RubA is a one-electron shuttle in an NADH→rubredoxin-reductase(AlkT/PP_5314)→rubredoxin relay.** Supported by verified operonic pairing with *alkT* (PP_5314, K05297, EC 1.18.1.1; STRING 0.999) and by the atomic-resolution *P. aeruginosa* RdxR–Rdx complex (6.2 Å redox-centre separation, transient interface). *(High confidence by homology.)*
- **H3 — RubA is soluble/cytoplasmic and acts at the cytoplasm–membrane interface with its partners.** Supported by GO:0005737 and absence of TM/signal segments. *(High confidence.)*
- **H6 — RubA is an archetypal short single-domain rubredoxin, not the elongated GPo1 AlkG.** Supported by length/motif comparison (55 aa, 2 CXXC; ~54 % identity to *C. pasteurianum* rubredoxin) vs. the 173-aa, four-CXXC AlkG; and by absence of the AlkG1 arginine insertion. *(High confidence.)*

**Refuted / down-weighted**
- **H4 — RubA is itself a catalytic enzyme with a small-molecule substrate.** Refuted: rubredoxins carry electrons; they do not transform a chemical substrate. Any "substrate specificity" is protein-partner specificity.
- **H5 — RubA drives alkane catabolism in KT2440.** Refuted at the genomic level: KT2440 encodes no alkane 1-monooxygenase (K00496); the alkane-catabolism GO/KEGG labels are homology/pathway-mapping inferences with no terminal AlkB acceptor present in the strain. The STRING "alkB" partner (PP_3400) is an unrelated DNA-repair dioxygenase (K03919), a naming artifact.

---

## 7. Limitations and Future Directions

- **No KT2440-specific experimental study of PP_5315/PP_5316 was found.** Functional assignment rests on homology to *P. aeruginosa* (structure) and *P. putida* GPo1 / other alkanotrophs (biochemistry/genetics).
- **The physiological terminal acceptor in KT2440 is unknown.** The genome lacks AlkB, so the acceptor is something else. STRING association (mostly text-mining, low confidence) hints at **aldehyde dehydrogenases** (aldA, aldB-I, aldB-II; note the paralogous reductase PP_5371 sits next to aldehyde dehydrogenase PP_5372) and links to the iron regulator **Fur**. Future work: identify RubA's redox partners by pull-down/crosslinking, test involvement in oxidative-stress survival (Δ*rubA*/Δ*alkT* mutants), test aldehyde/lipid-oxidation phenotypes, and measure its midpoint redox potential.
- **Direct biochemical characterization of RubA** (UV-vis 490-nm rubredoxin signature, EPR of the Fe³⁺ state, electron-transfer kinetics with RubB) would confirm the inferred properties.
- **Recommended annotation refinement:** retain "rubredoxin / electron transfer / iron-binding / cytoplasm" as high-confidence; flag "alkane catabolic process" as inferred-from-homology pending KT2440 evidence.

---

## 8. Key References
- Hagelueken G. et al. *Crystal structure of the electron transfer complex rubredoxin–rubredoxin reductase of Pseudomonas aeruginosa.* PNAS/PMID **17636129** (2007).
- van Beilen J.B. et al. *Rubredoxins involved in alkane oxidation.* J. Bacteriol., PMID **11872724** (2002).
- Smits T.H.M. et al. *Functional analysis of alkane hydroxylases from gram-negative and gram-positive bacteria.* PMID **11872725** (2002).
- Williams S.C. et al. *An alkane monooxygenase (AlkB) family in which all electron transfer partners are covalently bound to the oxygen-activating hydroxylase.* PMID **34990970** (2022).
- Williams S.C. & Austin R.N. *An Overview of the Electron-Transfer Proteins That Activate Alkane Monooxygenase (AlkB).* PMID **35295299** (2022).
- Swartz P.D. & Ichiye T. *Protein contributions to redox potentials of homologous rubredoxins.* PMID **9370467** (1997); Swartz, Beck & Ichiye PMID **8968568** (1996).
- UniProt Q88C68; Pfam PF00301; KEGG ppu:PP_5315.


## Artifacts

- [OpenScientist final report](rubA-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](rubA-deep-research-openscientist_artifacts/final_report.pdf)