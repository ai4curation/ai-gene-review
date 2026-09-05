---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T08:23:27.025234'
end_time: '2026-08-31T09:06:47.096485'
duration_seconds: 2600.07
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: pvdH
  gene_symbol: pvdH
  uniprot_accession: Q88F75
  protein_description: 'SubName: Full=Diaminobutyrate-2-oxoglutarate transaminase
    {ECO:0000313|EMBL:AAN69804.1}; EC=2.6.1.76 {ECO:0000313|EMBL:AAN69804.1};'
  gene_info: Name=pvdH {ECO:0000313|EMBL:AAN69804.1}; OrderedLocusNames=PP_4223 {ECO:0000313|EMBL:AAN69804.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the class-III pyridoxal-phosphate-dependent
  protein_domains: Aminotrans_3. (IPR005814); Aminotrans_3_PPA_site. (IPR049704);
    Dat. (IPR004637); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421)
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
  path: pvdH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: pvdH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88F75
- **Protein Description:** SubName: Full=Diaminobutyrate-2-oxoglutarate transaminase {ECO:0000313|EMBL:AAN69804.1}; EC=2.6.1.76 {ECO:0000313|EMBL:AAN69804.1};
- **Gene Information:** Name=pvdH {ECO:0000313|EMBL:AAN69804.1}; OrderedLocusNames=PP_4223 {ECO:0000313|EMBL:AAN69804.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the class-III pyridoxal-phosphate-dependent
- **Key Domains:** Aminotrans_3. (IPR005814); Aminotrans_3_PPA_site. (IPR049704); Dat. (IPR004637); PyrdxlP-dep_Trfase. (IPR015424); PyrdxlP-dep_Trfase_major. (IPR015421)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "pvdH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'pvdH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **pvdH** (gene ID: pvdH, UniProt: Q88F75) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of *pvdH* (Q88F75 / PP_4223) in *Pseudomonas putida* KT2440

## 1. Summary / Answer to the Research Question

**pvdH** encodes **L-2,4-diaminobutyrate:2-oxoglutarate aminotransferase (PvdH; EC 2.6.1.76)**, a soluble, cytoplasmic, pyridoxal-5′-phosphate (PLP)-dependent enzyme of the class-III aminotransferase family. Its primary function is to transaminate **L-aspartate-β-semialdehyde (ASA)** with the amino group of **L-glutamate**, producing **L-2,4-diaminobutyrate (DAB)** and **2-oxoglutarate (α-ketoglutarate)**. DAB is one of the two building blocks—together with D-tyrosine—that are condensed to form the fluorescent dihydroxyquinoline **chromophore of pyoverdine**, the major siderophore of *P. putida* KT2440. PvdH therefore supplies an essential precursor for **pyoverdine-mediated iron acquisition**, acting upstream in the cytoplasm before the pyoverdine peptide is assembled, exported to the periplasm for maturation, and secreted.

## 2. Gene / Protein Identity (verified)

- **UniProt:** Q88F75 — "Diaminobutyrate-2-oxoglutarate transaminase," EC 2.6.1.76
- **Gene / locus:** *pvdH* / PP_4223
- **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125)
- **Family / domains:** Class-III PLP-dependent aminotransferase — Aminotrans_3 (IPR005814), Aminotrans_3_PPA_site (IPR049704), **Dat** (IPR004637, diaminobutyrate aminotransferase), PyrdxlP-dep_Trfase (IPR015424/IPR015421).

**Identity verification:** The gene symbol, EC number, and domain architecture are fully consistent. The direct functional characterization of PvdH was performed on the *P. aeruginosa* PAO1 ortholog, but that study explicitly showed that PvdH homologues reside in the pyoverdine-synthesis loci of other pyoverdine-producing *Pseudomonas*, and *P. putida* KT2440 is an established pyoverdine producer. Q88F75 is therefore correctly annotated as the *P. putida* PvdH ortholog. No conflicting "same-symbol, different-gene" literature was encountered.

## 3. Primary Molecular Function and Substrate Specificity

The definitive biochemistry comes from Vandenende, Vlasschaert & Seah (2004), who subcloned, hyperexpressed, and purified PvdH and characterized it enzymatically (PMID 15317763):

- **Reaction catalyzed:** aminotransferase interconverting **aspartate-β-semialdehyde ⇌ L-2,4-diaminobutyrate**, using α-ketoglutarate/L-glutamate as the keto-acid/amino donor pair.
- **Kinetic mechanism:** classic **ping-pong bi-bi**, as expected for PLP transaminases (the PLP cofactor cycles between pyridoxal and pyridoxamine forms).
- **Substrate specificity for the amino acceptor:** **highest specificity for α-ketoglutarate**; specificity toward pyruvate is **41-fold lower**; **negligible activity** toward other keto acids tested. This establishes glutamate/α-ketoglutarate as the physiological amino shuttle.

> "PvdH was found to catalyze an aminotransferase reaction, interconverting aspartate beta-semialdehyde and l-2,4-diaminobutyrate. Steady-state kinetic analysis … established that the enzyme adopts a ping-pong kinetic mechanism and has the highest specificity for alpha-ketoglutarate." (PMID 15317763)

**Genetic requirement:** *pvdH* (and *asd*, aspartate-β-semialdehyde dehydrogenase, which makes the ASA substrate) knockouts **cannot synthesize pyoverdine under iron limitation unless L-2,4-diaminobutyrate is supplied exogenously**, proving that PvdH is the physiological source of DAB for the chromophore (PMID 15317763).

Mechanistically, PvdH belongs to the same class-III aminotransferase / **Dat (diaminobutyrate aminotransferase)** family as EctB (the DAB aminotransferase of ectoine biosynthesis) and DABA-AT of other pathways, all of which perform the ASA→DAB transamination. The InterPro "Dat" signature (IPR004637) on Q88F75 independently corroborates this assignment by sequence.

### 3.1 Sequence / structure-level evidence for the target protein itself

Because the enzymatic characterization above was performed on the *P. aeruginosa* PAO1 ortholog, I independently verified that the *P. putida* protein (Q88F75) carries the same functional identity:

- **Length & cofactor:** Q88F75 is a **452-residue** protein annotated with a **pyridoxal-5′-phosphate (PLP)** cofactor (ChEBI:597326), the hallmark of aminotransferases.
- **No export/membrane signals:** the entry has **no signal peptide and no transmembrane segment** (only an N-terminal disordered, polar-biased region, residues 8–27), consistent with a **soluble cytoplasmic** enzyme.
- **Orthology:** a full-length Needleman–Wunsch alignment against the biochemically characterized PAO1 PvdH (**Q9I168 / PA2413**, 469 aa) gives **83.6 % amino-acid identity (377/451 aligned positions)**. This near-full-length, high identity establishes clear orthology and justifies transferring the experimentally measured ASA⇌DAB aminotransferase activity to Q88F75.

## 4. Subcellular Localization

PvdH is predicted to be a **soluble cytoplasmic enzyme**. Evidence and inference:
- Class-III PLP aminotransferases (Aminotrans_3 fold) are canonically soluble cytoplasmic proteins; Q88F75 has no signal peptide or transmembrane segment consistent with this.
- Its product, the amino acid DAB, is a **cytoplasmic metabolite** incorporated by cytoplasmic non-ribosomal peptide synthetases (NRPS) into the pyoverdine precursor (ferribactin). Pyoverdine biosynthesis begins in the cytoplasm; the precursor is subsequently translocated to the **periplasm** for chromophore maturation and then secreted. PvdH acts in the **cytoplasmic (precursor-supply) phase**, upstream of periplasmic maturation.

The downstream compartmentalization is well documented in *P. putida* KT2440: deleting the **PvdRT-OpmQ** and **MdtABC-OpmB** efflux systems causes pyoverdine to accumulate **in the periplasm** ("more pyoverdine in the periplasm," PMID 30346656), and PvdT/PvdR were biochemically shown to directly interact with pyoverdine and hydrolyze ATP (PMID 36807028). These place secretion/maturation in the periplasm/membrane, distinct from PvdH's cytoplasmic role.

### 4.1 Genomic locus context (synteny) in KT2440

Genomic-neighborhood analysis of the KT2440 chromosome confirms, in the **exact target strain**, that *pvdH* (PP_4223) is **embedded within the pyoverdine biosynthesis gene cluster**, co-localized with the peptide-assembly, export, and uptake machinery:

| Locus | Gene | Product |
|-------|------|---------|
| PP_4215 | *pvdO* | Pyoverdine biosynthesis-related protein |
| PP_4216 | *pvdE* | Pyoverdine ABC export system (fused ATPase/permease) |
| PP_4217 | *fpvA* | TonB-dependent ferripyoverdine outer-membrane receptor |
| PP_4219 | *pvdD* | Non-ribosomal peptide synthetase (ferribactin synthase) |
| PP_4220 | *pvdJ* | NRPS subunit of ferribactin synthase |
| PP_4221 | *pvdI* | NRPS subunit of ferribactin synthase |
| PP_4222 | — | SyrP-like tailoring protein |
| **PP_4223** | **pvdH** | **Diaminobutyrate-2-oxoglutarate transaminase (this study)** |

This synteny is precisely the pyoverdine-locus co-localization predicted by Vandenende et al. (2004) for PvdH orthologs, and provides independent genomic evidence that PP_4223 acts specifically in pyoverdine biosynthesis (supplying DAB to the adjacent NRPS enzymes) rather than in generic transamination.

## 5. Pathway Context and Biological Process

PvdH functions in the **pyoverdine siderophore biosynthesis pathway**, the principal high-affinity iron-acquisition system of fluorescent pseudomonads:

1. **Precursor supply (cytoplasm):** Asd generates aspartate-β-semialdehyde; **PvdH transaminates it to L-2,4-diaminobutyrate (DAB)**. In parallel, D-tyrosine is provided.
2. **Chromophore/peptide assembly:** DAB + D-tyrosine are condensed by NRPS machinery, building the pyoverdine peptide backbone and the precursor of the fluorescent dihydroxyquinoline chromophore.
3. **Maturation & export (periplasm/membrane):** the precursor is transported to the periplasm, matured, and secreted via ABC/RND efflux systems (**PvdRT-OpmQ**, with **MdtABC-OpmB** contributing; PMID 30346656, 36807028).
4. **Iron capture & uptake:** secreted apo-pyoverdine chelates Fe(III); the ferri-pyoverdine complex is imported through the outer-membrane receptor **FpvA**.

**Physiological importance in *P. putida* KT2440:**
- KT2440 produces a structurally characterized pyoverdine as its **major (essentially sole) siderophore** (PMID 19459056), so PvdH-derived DAB is essential for its principal iron-scavenging system under iron limitation.
- Pyoverdine iron acquisition also controls **surface motility**: pyoverdine (ppsD) or FpvA-receptor mutants fail to spread on surfaces, and iron availability acts as an environmental cue for swarming-like movement at 18–28 °C (PMID 17564617).

We deliberately restrict the annotation to this precise precursor-supply role; broader pleiotropic iron-linked phenotypes are mentioned only insofar as they establish the pathway's function.

## 6. Supported and Refuted Hypotheses

**Supported**
- PvdH is a PLP-dependent class-III aminotransferase (EC 2.6.1.76) catalyzing ASA ⇌ DAB — supported by direct enzymology (PMID 15317763) and domain evidence (IPR004637 "Dat").
- α-Ketoglutarate/glutamate is the physiological amino-shuttle pair — supported by 41-fold specificity over pyruvate (PMID 15317763).
- PvdH provides the DAB precursor required for pyoverdine — supported by knockout complementation with exogenous DAB (PMID 15317763).
- The pathway serves iron acquisition and pyoverdine-dependent surface motility in KT2440 (PMID 19459056, 17564617).

**Refuted / excluded**
- PvdH is **not** a broad-specificity transaminase: it has negligible activity toward keto acids other than α-ketoglutarate (and, weakly, pyruvate) (PMID 15317763).
- PvdH is **not** a membrane/secretion component: export and periplasmic maturation are handled by distinct proteins (PvdRT-OpmQ, MdtABC-OpmB; PMID 30346656, 36807028).

## 7. Limitations and Future Directions

- The direct enzymatic characterization was performed on the *P. aeruginosa* PAO1 ortholog; the *P. putida* KT2440 protein (Q88F75) itself has not, to our knowledge, been individually purified and kinetically characterized. Given high sequence conservation and shared pyoverdine-locus context, function is confidently inferred but not experimentally demonstrated for KT2440 specifically.
- Subcellular localization of PvdH is inferred from family/fold and pathway logic rather than measured directly (e.g., fractionation or fluorescent tagging).
- A crystal structure of PvdH would confirm the PLP-binding lysine and active-site residues; comparative modeling against EctB/DABA-AT structures could refine substrate-binding determinants.

---

### Key References
- Vandenende CS, Vlasschaert M, Seah SYK. *Functional characterization of an aminotransferase required for pyoverdine siderophore biosynthesis in Pseudomonas aeruginosa PAO1.* J Bacteriol, 2004. **PMID 15317763.**
- Matthijs S, et al. *Siderophore-mediated iron acquisition in Pseudomonas entomophila L48 and its close relative Pseudomonas putida KT2440.* 2009. **PMID 19459056.**
- Matilla MA, et al. *Temperature and pyoverdine-mediated iron acquisition control surface motility of Pseudomonas putida.* 2007. **PMID 17564617.**
- Henríquez T, Stein NV, Jung H. *PvdRT-OpmQ and MdtABC-OpmB efflux systems are involved in pyoverdine secretion in Pseudomonas putida KT2440.* 2019. **PMID 30346656.**
- Stein NV, et al. *The ABC transporter family efflux pump PvdRT-OpmQ of Pseudomonas putida KT2440: purification and initial characterization.* 2023. **PMID 36807028.**


## Artifacts

- [OpenScientist final report](pvdH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](pvdH-deep-research-openscientist_artifacts/final_report.pdf)