---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T15:13:43.300352'
end_time: '2026-10-24T15:34:37.504023'
duration_seconds: 1254.2
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: mouse
  gene_id: Rtl8b
  gene_symbol: Rtl8b
  uniprot_accession: Q9D1F0
  protein_description: 'SubName: Full=CAAX box 1 homolog A (Human) {ECO:0000313|EMBL:AAH03436.1};
    SubName: Full=CAAX box 1 homolog B (Human) {ECO:0000313|EMBL:AAH29838.1};'
  gene_info: Name=Rtl8b {ECO:0000313|MGI:MGI:3576504}; Synonyms=Cxx1a {ECO:0000313|EMBL:AAH03436.1},
    Cxx1b {ECO:0000313|EMBL:AAH29838.1}, Rtl8a {ECO:0000313|MGI:MGI:1913408};
  organism_full: Mus musculus (Mouse).
  protein_family: Not specified in UniProt
  protein_domains: RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)
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
  path: Rtl8b-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Rtl8b-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q9D1F0
- **Protein Description:** SubName: Full=CAAX box 1 homolog A (Human) {ECO:0000313|EMBL:AAH03436.1}; SubName: Full=CAAX box 1 homolog B (Human) {ECO:0000313|EMBL:AAH29838.1};
- **Gene Information:** Name=Rtl8b {ECO:0000313|MGI:MGI:3576504}; Synonyms=Cxx1a {ECO:0000313|EMBL:AAH03436.1}, Cxx1b {ECO:0000313|EMBL:AAH29838.1}, Rtl8a {ECO:0000313|MGI:MGI:1913408};
- **Organism (full):** Mus musculus (Mouse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** RTL1/1-8/LDOC_capsid-like. (IPR032549); RTL1-8_LDOC (PF16297)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "Rtl8b" matches the protein description above**
2. **Verify the organism is correct:** Mus musculus (Mouse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'Rtl8b' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **Rtl8b** (gene ID: Rtl8b, UniProt: Q9D1F0) in mouse.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: Mouse *Rtl8b* (Q9D1F0)

**Gene:** *Rtl8b* (synonyms *Cxx1a*, *Cxx1b*, *Rtl8a*; "CAAX box 1 homolog"; Mart8b/SIRH5)
**UniProt:** Q9D1F0 | **Organism:** *Mus musculus* (Mouse)
**Protein length:** 113 aa (~13 kDa) | **Key domain:** RTL1/1-8/LDOC capsid-like (IPR032549; Pfam PF16297)

---

## Summary

Mouse **Rtl8b** is **not an enzyme, transporter, or classical signaling molecule**, and — despite its historical name "CAAX box 1 homolog" (Cxx1) — **it is not a prenylated CAAX protein at all**. Direct sequence analysis of Q9D1F0 shows the protein contains **zero cysteine residues** and terminates in an acidic sequence (…WEEDEDF) that cannot support C-a-a-X prenylation. The "CAAX box" name is a historical misnomer. Instead, Rtl8b is a small (~13 kDa) **protein-interaction adaptor derived from the Gag/capsid protein of a domesticated Ty3/gypsy LTR-retrotransposon**. It belongs to the mammalian Mart/SIRH (sushi-ichi-related retrotransposon-homolog) family — specifically the **RTL8** subgroup (SIRH5/Mart8) — and consists almost entirely of a single capsid-like domain carrying an arginine-rich, nucleolar/nucleic-acid-binding N-terminal motif.

The **primary function** of Rtl8b is to **bind partner proteins and change their subcellular localization and assembly behavior**, acting as a molecular adaptor at the interface of two pathways: (1) the **ubiquitin–proteasome/protein-quality-control (PQC) system**, where RTL8 drives the proteasomal shuttle factor **UBQLN2** into the nucleolus and into ubiquitin-rich subnuclear PQC compartments; and (2) the biology of its retroelement-derived paralog **PEG10**, whose N-terminal Gag/capsid RTL8 binds to **antagonize PEG10 virus-like-particle (VLP) formation**, while simultaneously serving as the **obligate bridge** that enables PEG10 to recruit UBQLN2 into cytoplasmic **stress granules**.

Functionally, therefore, Rtl8b operates in **two cellular locations** — the **nucleolus/subnuclear PQC bodies** and **cytoplasmic stress granules / PEG10 particles** — within **proteostasis and PEG10 retroelement-particle pathways**. It is expressed in **placental trophoblast and brain**, tissues that overlap strongly with PEG10. This report synthesizes eight confirmed findings and 13 reviewed papers into a mechanistic model of Rtl8b as a Gag-derived proteostasis/PEG10 adaptor, and flags the key limitation: nearly all mechanistic data derive from the human RTL8 orthologs (which are ~80–82% identical and encode an invariant functional C-terminal motif), with mouse-specific *Rtl8b* experiments still lacking.

---

## Gene/Protein Identity Verification

Following the mandatory verification protocol, I confirm the target is correctly identified, with one important caveat about the gene name:

| Check | Result |
|-------|--------|
| Gene symbol "Rtl8b" matches UniProt record | ✅ Yes — Q9D1F0, Name=Rtl8b, synonyms Cxx1a/Cxx1b/Rtl8a |
| Organism is *Mus musculus* | ✅ Yes |
| Protein family/domains align with literature | ✅ Yes — RTL1-8/LDOC capsid-like domain (PF16297) matches the Mart/SIRH/RTL8 retroelement-derived family |
| "CAAX box 1" (Cxx1) name consistent with biochemistry | ❌ **No — this name is a misnomer** (see Finding F005) |

**Critical clarification on naming.** The UniProt description "CAAX box 1 homolog A/B" and the synonyms *Cxx1a/Cxx1b* are **misleading legacy names**. A CAAX box is a C-terminal Cys-aliphatic-aliphatic-X motif that directs prenylation. Q9D1F0 has **no cysteine anywhere** in its 113 residues and ends in …DEDF. The gene was later correctly reclassified as a member of the **RTL8 / Mart8 / SIRH5** retrotransposon-derived family. Literature should be read under the names **RTL8**, **Mart8**, or **SIRH5**, not "CAAX box protein." This is not a case of researching the wrong gene — it is the *same* gene under a corrected modern identity.

---

## Key Findings

### F001 — Rtl8b is a domesticated Ty3/gypsy retrotransposon Gag-derived gene with a capsid-like domain

Rtl8b is a member of the **Mart/SIRH family** of mammalian genes that originated from the **Gag (capsid) protein of Ty3/gypsy LTR-retrotransposons** and were "domesticated" into functional host genes during evolution. The UniProt record for Q9D1F0 lists the **RTL1/1-8/LDOC capsid-like domain** (InterPro IPR032549; Pfam PF16297), the structural signature of this family. Henke et al. (2015) classify the mouse *Cxx1a,b,c* = *Mart8b,c,a* cluster explicitly within this family, describing Mart/SIRH genes as "a class of Ty3/gypsy LTR-retroelements showing moderate homology to the sushi-ichi LTR-retrotransposon in pufferfish" ([PMID: 25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/)). Campodonico et al. (2024) further characterize the family's domain architecture, noting that "RTL8 resembles a truncated form of PEG10 that shares homology with the N-terminal gag-like capsid domain" ([PMID: 39775359](https://pubmed.ncbi.nlm.nih.gov/39775359/)).

This places Rtl8b in the same structural lineage as other Gag-derived mammalian proteins — PEG10, Arc, and the LDOC1 group — all of which retain a retroviral capsid fold repurposed for host functions. The capsid origin is the single most important fact for understanding Rtl8b's biochemistry: capsid domains are **self- and hetero-oligomerizing protein-assembly modules**, which explains why Rtl8b behaves as an adaptor/assembly partner rather than an enzyme.

### F002 — RTL8 (Rtl8b) is a UBQLN2 adaptor that drives UBQLN2 nuclear/nucleolar translocation to protein-quality-control compartments

The first assigned molecular function for RTL8 came from Mohan et al. (2022), who identified the RTL8 family in a mass-spectrometry interactome of **UBQLN2** — a ubiquilin that shuttles ubiquitinated substrates to the proteasome and is genetically linked to ALS/FTD. They "identified a family of small (13 kDa), highly homologous uncharacterized proteins, RTL8, and confirmed the interaction between UBQLN2 and RTL8 both in vitro using recombinant proteins and in vivo using mouse brain tissue" ([PMID: 35247097](https://pubmed.ncbi.nlm.nih.gov/35247097/)). The validation **in mouse brain tissue** is directly relevant to the mouse Rtl8b annotation.

Functionally, RTL8 acts as a **localization adaptor for UBQLN2**:
- "Under endogenous and overexpressed conditions, RTL8 localizes to nucleoli."
- "When co-expressed with UBQLN2, RTL8 promotes nuclear translocation of UBQLN2."
- "UBQLN2 and RTL8 colocalize within ubiquitin-enriched subnuclear structures containing PQC components."

The effect is **specific to UBQLN2** and not its paralogs UBQLN1 or UBQLN4, indicating a selective protein–protein interaction rather than a generic ubiquilin effect. Mechanistically, RTL8's arginine-rich N-terminus (Finding F006) likely supplies the nucleolar-localization signal that carries UBQLN2 into the nucleolus and into ubiquitin-rich subnuclear PQC bodies. This establishes Rtl8b as a node in **protein homeostasis (proteostasis)**, controlling where quality-control machinery is concentrated inside the nucleus.

### F003 — RTL8 (Rtl8b) regulates PEG10: incorporated into and antagonizes PEG10 virus-like particles, and gates PEG10–UBQLN2 stress-granule recruitment

RTL8's second major function links it to its paralog **PEG10**, a Gag/Pol-derived retroelement gene that assembles **virus-like particles (VLPs)**. Campodonico et al. (2024) showed that **RTL8 cannot form VLPs on its own** but is **incorporated into PEG10 particles** through binding the PEG10 N-terminal capsid: "Alone, RTL8 is unable to form VLPs, but was incorporated into PEG10-derived particles." Critically, RTL8 acts as a **negative regulator** of PEG10 particle biogenesis: "RTL8 co-expression decreased the abundance of PEG10 VLPs and increased intracellular levels of PEG10, suggesting a model where RTL8 inhibits PEG10 VLP formation or release" ([PMID: 39775359](https://pubmed.ncbi.nlm.nih.gov/39775359/)). In effect, RTL8 is a truncated, assembly-incompetent capsid that "caps" or poisons PEG10 particle assembly — a classic dominant-negative behavior for a capsid-like subunit.

A second study (Mohan et al., 2025) revealed that RTL8 is the **obligate molecular bridge** connecting PEG10 and UBQLN2 at cytoplasmic stress granules: "RTL8 confers on UBQLN2 the ability to complex with and regulate PEG10," and "PEG10, a core component of stress granules, drives the recruitment of UBQLN2 to stress granules under various stress conditions but can only do so when RTL8 is present" ([PMID: 40680123](https://pubmed.ncbi.nlm.nih.gov/40680123/)). The relative levels of RTL8, PEG10, and UBQLN2 together remodel **stress-granule disassembly kinetics**. Thus, Rtl8b sits at the control point of a three-protein module (RTL8–PEG10–UBQLN2) governing stress-granule dynamics and proteostasis.

### F004 — Mouse Rtl8/Cxx1 genes are expressed in placenta (trophoblast) and brain

Expression data situate Rtl8b in tissues shared with PEG10. Henke et al. (2015) found that the mouse *Cxx1a,b,c*/*Mart8b,c,a* cluster is low at the blastocyst stage but is **developmentally up-regulated during placentogenesis**, reaching up to "1,489 molecules/ng cDNA at E9.5," with sense/antisense transcripts co-localizing in **junctional-zone trophoblast** subtypes ([PMID: 25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/)). In parallel, RTL8 protein is "broadly expressed in many of the same tissues as PEG10, including in human brain" ([PMID: 39775359](https://pubmed.ncbi.nlm.nih.gov/39775359/)), and endogenous RTL8 was detected directly in **mouse brain tissue** ([PMID: 35247097](https://pubmed.ncbi.nlm.nih.gov/35247097/)). The **placenta + brain** expression pattern is a recurring theme among domesticated retroelement genes and reinforces the functional partnership with PEG10.

### F005 — The "CAAX box" (Cxx1) name is a misnomer: Rtl8b has no cysteine and no CAAX prenylation motif

Direct computational sequence analysis of the 113-aa Q9D1F0 sequence demonstrates conclusively that the "CAAX box 1" designation is incorrect:
- The protein contains **zero cysteine residues (0.0%)** — a CAAX box absolutely requires a cysteine as the prenylation acceptor.
- The **C-terminus is …WEEDEDF** (final four residues DEDF), which does **not** match the C-a-a-X consensus (which places a cysteine four residues from the C-terminus).

Prenylation (farnesylation/geranylgeranylation) via a CAAX box is therefore **structurally impossible** for this protein. Any annotation implying membrane-anchoring by prenylation, or function as a "CAAX protein," is erroneous. This finding is central to the correct annotation: Rtl8b is a soluble, capsid-derived adaptor, not a lipid-modified membrane protein.

### F006 — Rtl8b is essentially a single Gag/capsid-like domain with an N-terminal arginine-rich (nucleolar/nucleic-acid-binding) motif

UniProt feature annotation shows a **single RTL1/3-8/LDOC capsid-like domain spanning residues 18–113** — effectively the entire protein (Pfam PF16297; InterPro IPR032549). Sequence analysis reveals a striking **hexa-arginine run (RRRRRR) at residues 19–24**, right at the start of the domain. The N-terminal ~40 residues are **30% basic (K/R)** versus 11% in the remainder (whole-protein K/R = 17.7%), while the **C-terminus is acidic (…EEDEDF)**.

This architecture is mechanistically informative:
- The **arginine-rich N-terminus** functions as a **nucleolar-localization signal (NoLS)** and likely a **nucleic-acid/RNA-binding** surface — consistent with RTL8's nucleolar localization (F002) and with the RNA-packaging heritage of Gag capsids.
- The **acidic C-terminus** provides an opposite-charge surface available for protein–protein contacts.
- The absence of any catalytic domain confirms the **adaptor/structural**, non-enzymatic nature of the protein.

### F007 — Mouse Rtl8a and Rtl8b encode an identical protein; the capsid core and an invariant acidic C-terminal motif (FGWEEDEDF) are conserved mouse-to-human

Sequence comparison shows that **mouse Rtl8a and Rtl8b encode a 100% identical 113-aa protein** (Q9D1F0 / F6VWQ4). The capsid-like core (anchored on the invariant **NPIPFP** motif) is **~80% identical** between mouse Rtl8b and mouse Rtl8c, and between mouse and all three human orthologs (RTL8A/B/C, ~80–82%). Most strikingly, the **C-terminal nonapeptide "FGWEEDEDF" is strictly invariant** across all five mouse and human paralogs examined.

The perfect conservation of this acidic C-terminal motif across >75 million years of mouse–human divergence is strong evolutionary evidence that it is **functionally essential** — most plausibly a conserved **protein-interaction motif** mediating binding to UBQLN2 and/or PEG10. The high paralog identity also means that the mechanistic findings obtained with human RTL8 (F002, F003) can be **reasonably extrapolated to mouse Rtl8b**, because the proteins are nearly identical and share the invariant functional motif.

### F008 — Pathway context: Rtl8b acts upstream of PEG10, a retroelement-derived gene essential for placentation and implicated in neurological disease

Rtl8b's principal regulatory target, **PEG10**, is a paternally expressed imprinted Mart/SIRH gene **essential for placental development**. Silencing PEG10 produced cells that "displayed a reduced proliferation rate and impaired invasiveness in vitro" in trophoblast (JEG-3 and primary chorionic villous) cells ([PMID: 26680220](https://pubmed.ncbi.nlm.nih.gov/26680220/)), and disruption of the PEG10 imprinted domain causes placental defects including decreased labyrinthine volume and embryonic viability ([PMID: 26241757](https://pubmed.ncbi.nlm.nih.gov/26241757/)). Because RTL8/Rtl8b binds the PEG10 N-terminal capsid and antagonizes PEG10 VLP formation ([PMID: 39775359](https://pubmed.ncbi.nlm.nih.gov/39775359/)) and is required for PEG10-driven UBQLN2 stress-granule recruitment ([PMID: 40680123](https://pubmed.ncbi.nlm.nih.gov/40680123/)), Rtl8b functions **upstream of / as a modulator of PEG10 activity**. This connects Rtl8b to the physiologically and clinically important PEG10 pathway in both placentation and neurological disease.

---

## Mechanistic Model / Interpretation

Rtl8b is best understood as a **"truncated capsid adaptor"**: an evolutionarily domesticated, assembly-incompetent fragment of a retroviral Gag/capsid that has been repurposed to **dock onto partner proteins and redirect their localization and assembly**. Its two documented functional arms converge on **proteostasis and stress-granule/PEG10 particle biology**.

```
                          RTL8b (Q9D1F0, ~13 kDa)
          [ Arg-rich NoLS ]---[ Gag/capsid-like domain ]---[ acidic FGWEEDEDF ]
              (res 19-24 RRRRRR)     (res 18-113)         (invariant C-term motif)
                     |                     |                        |
          nucleolar targeting /    capsid hetero-oligo-      conserved protein-
          RNA / nucleic-acid       merization w/ PEG10       interaction surface
          binding surface               capsid

   NUCLEUS / NUCLEOLUS arm                       CYTOPLASM arm (stress granules / PEG10)
   -----------------------                       ----------------------------------------
   RTL8b --- binds ---> UBQLN2                    RTL8b --- binds N-term capsid --> PEG10
      |                                               |                               |
      v                                               v                               v
   drives UBQLN2 nuclear/nucleolar            incorporated into PEG10 VLPs,     obligate bridge:
   translocation into ubiquitin-rich          but caps/inhibits VLP             PEG10 recruits
   subnuclear PQC compartments                formation & release               UBQLN2 to stress
   (UBQLN2-specific; not UBQLN1/4)             (dominant-negative capsid)        granules ONLY if
                                                                                 RTL8b is present
```

**Three-protein module.** The emerging picture is a regulatory triad — **RTL8 ⟷ PEG10 ⟷ UBQLN2** — whose stoichiometry tunes two outputs:
1. **PEG10 particle abundance:** RTL8 incorporation into PEG10 capsids reduces VLP output and raises intracellular PEG10 (a built-in brake on particle release).
2. **Stress-granule dynamics:** RTL8 is the switch that permits PEG10 to pull UBQLN2 into stress granules, thereby shaping stress-granule assembly/disassembly kinetics and, by extension, the cell's handling of ribonucleoprotein condensates and misfolded protein during stress.

| Functional axis | Location | Partner | RTL8b action | Evidence (PMID) |
|---|---|---|---|---|
| Proteostasis / PQC | Nucleolus & subnuclear PQC bodies | UBQLN2 | Drives UBQLN2 nuclear/nucleolar translocation (UBQLN2-specific) | [35247097](https://pubmed.ncbi.nlm.nih.gov/35247097/) |
| PEG10 particle biology | Cytoplasm / VLPs | PEG10 capsid (N-term) | Co-assembles but antagonizes VLP formation/release | [39775359](https://pubmed.ncbi.nlm.nih.gov/39775359/) |
| Stress-granule regulation | Cytoplasmic stress granules | PEG10 + UBQLN2 | Obligate bridge for PEG10→UBQLN2 recruitment; tunes SG kinetics | [40680123](https://pubmed.ncbi.nlm.nih.gov/40680123/) |

**Why an adaptor, not an enzyme?** The capsid fold is an oligomerization/assembly module, not a catalytic one; Rtl8b has no catalytic domain, no cysteine, and no CAAX motif. Its arginine-rich NoLS explains nucleolar targeting and its ability to carry UBQLN2 into the nucleolus, while its capsid surface explains hetero-oligomerization with PEG10 capsids. The invariant C-terminal **FGWEEDEDF** motif (conserved across all mouse and human paralogs) is the leading candidate for the actual partner-binding "business end" and is a prime target for mutagenesis.

**Physiological significance.** Through its control of PEG10 — essential for trophoblast proliferation/invasion and placental labyrinth formation — and its modulation of UBQLN2 (an ALS/FTD gene) proteostasis, Rtl8b is positioned at the intersection of **placental development** and **neuronal protein-quality-control**, matching its placenta + brain expression.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [35247097](https://pubmed.ncbi.nlm.nih.gov/35247097/) | *RTL8 promotes nuclear localization of UBQLN2…* | **Core.** Defines RTL8 as a UBQLN2 adaptor; nucleolar localization; mouse-brain validation (F002) |
| [40680123](https://pubmed.ncbi.nlm.nih.gov/40680123/) | *Endogenous retrovirus-like proteins recruit UBQLN2 to stress granules…* | **Core.** RTL8 as obligate PEG10–UBQLN2 bridge; stress-granule kinetics (F003) |
| [39775359](https://pubmed.ncbi.nlm.nih.gov/39775359/) | *The gag-like gene RTL8 antagonizes PEG10-mediated VLPs* | **Core.** Domain structure; VLP incorporation + antagonism; expression overlap with PEG10 (F001, F003, F004) |
| [25888968](https://pubmed.ncbi.nlm.nih.gov/25888968/) | *Selective expression of sense/antisense SIRH transcripts in placentogenesis* | **Core.** Classifies Cxx1a,b,c=Mart8 as Ty3/gypsy SIRH genes; placental expression (F001, F004) |
| [26680220](https://pubmed.ncbi.nlm.nih.gov/26680220/) | *Silencing of PEG10 inhibits trophoblast proliferation and invasion* | Pathway context: PEG10's placental role (F008) |
| [26241757](https://pubmed.ncbi.nlm.nih.gov/26241757/) | *Peg10/Kcnq1 imprinted domains in placental development* | Pathway context: PEG10 ICR essential for labyrinth/viability (F008) |
| [34413232](https://pubmed.ncbi.nlm.nih.gov/34413232/) | *PEG10 packages its own mRNA; pseudotyping for mRNA delivery* | Background on PEG10 Gag/capsid VLP biology (context for F003) |
| [38798208](https://pubmed.ncbi.nlm.nih.gov/38798208/) | *Human Virus-Like Proteins: Implications for Gene Therapy* | Review context: Gag-derived mammalian proteins (PEG10, Arc) |
| [27764577](https://pubmed.ncbi.nlm.nih.gov/27764577/) | *LDOC1 interacts with GNL3L to modulate NF-κB…* | Context on the related LDOC/capsid family (nucleolar GTPase interplay) |
| [10403563](https://pubmed.ncbi.nlm.nih.gov/10403563/) | *Identification of LDOC1…* | Context: LDOC1 is a nuclear capsid-family protein |

**Consistency of the evidence.** The three core RTL8 papers (PMIDs 35247097, 39775359, 40680123) are mutually reinforcing and build a coherent two-arm model (UBQLN2/PQC nucleolar arm + PEG10/stress-granule cytoplasmic arm). No reviewed paper contradicts the model. The expression data (PMID 25888968) and PEG10 placental genetics (PMIDs 26680220, 26241757) provide independent physiological grounding.

**A note on the LDOC1 literature.** Several reviewed papers concern **LDOC1**, a related member of the same capsid/LDOC superfamily, in cancer/NF-κB contexts (e.g., PMIDs 27764577, 28240050, 30634502, 22825526, 10403563). These are **not** Rtl8b studies and were retained only to characterize the broader family; claims from them are not attributed to Rtl8b.

---

## Limitations and Knowledge Gaps

1. **Most mechanistic data are from human RTL8, not mouse Rtl8b specifically.** The UBQLN2-adaptor, VLP-antagonism, and stress-granule-bridge functions (F002, F003) were established largely in human/overexpression systems. The extrapolation to mouse Rtl8b rests on high sequence identity (~80–82% paralog-wide; mouse Rtl8a=Rtl8b 100% identical; invariant C-terminal motif, F007) rather than direct mouse Rtl8b loss-of-function experiments.

2. **Paralog redundancy confounds gene-specific annotation.** Mouse Rtl8a and Rtl8b are identical proteins, and Rtl8c differs only modestly. No study has isolated a unique, non-redundant function for *Rtl8b* as distinct from *Rtl8a/c*. Phenotypes may require compound knockouts.

3. **No experimentally determined 3-D structure** of Rtl8b exists in the reviewed evidence; the capsid-like fold and NoLS are inferred from Pfam/InterPro domain assignment and sequence composition, not solved coordinates.

4. **The functional C-terminal motif (FGWEEDEDF) is conserved but untested.** Its role as the partner-binding surface is a strong inference from evolutionary conservation, not yet validated by mutagenesis.

5. **No in vivo mouse phenotype for Rtl8b** (knockout/knock-in) is documented in the reviewed literature; physiological roles in placenta and brain remain inferred from expression and from the PEG10 partnership.

6. **Direct nucleic-acid binding by the arginine-rich motif is predicted, not demonstrated** for Rtl8b; it is inferred from Gag heritage and composition.

---

## Proposed Follow-up Experiments / Actions

1. **Mouse-specific loss-of-function.** Generate single and compound *Rtl8a/b/c* knockouts (CRISPR) in mouse trophoblast and neuronal models; assay UBQLN2 nucleolar localization, PEG10 VLP output, and stress-granule disassembly kinetics to confirm the human-derived model in the native mouse context.

2. **Mutagenesis of the invariant C-terminal motif.** Mutate/delete **FGWEEDEDF** and the hexa-arginine NoLS (RRRRRR, res 19–24) in Rtl8b and test, respectively, UBQLN2/PEG10 binding and nucleolar targeting — to map the adaptor's two functional surfaces.

3. **Structural biology.** Solve the Rtl8b capsid-like domain structure (X-ray/cryo-EM), ideally in complex with the PEG10 N-terminal capsid, to define the hetero-oligomerization interface; validate any AlphaFold model against solved structure.

4. **Stoichiometry / dose–response.** Systematically titrate RTL8:PEG10:UBQLN2 ratios to quantify how the triad tunes VLP abundance and stress-granule dynamics, testing the "capping/dominant-negative capsid" model quantitatively.

5. **Nucleic-acid binding assays.** Test whether Rtl8b's arginine-rich motif binds RNA/DNA (EMSA, CLIP), probing the retained Gag RNA-packaging heritage.

6. **Physiological readouts.** In placenta, test whether Rtl8b modulates PEG10-dependent trophoblast proliferation/invasion; in neurons, test whether Rtl8b dosage affects UBQLN2 proteostasis relevant to ALS/FTD.

---

## Conclusion

Mouse **Rtl8b (Q9D1F0)** is a small (~13 kDa), **non-enzymatic, Gag/capsid-derived protein-interaction adaptor** of the Mart/SIRH/RTL8 retroelement family — **not** the prenylated "CAAX box" protein its legacy name implies (it has no cysteine and no CAAX motif). It is essentially a single capsid-like domain bearing an arginine-rich nucleolar/nucleic-acid-binding N-terminus and an invariant acidic C-terminal motif. Its primary function is to **bind and relocalize partner proteins**: it drives the proteasomal shuttle factor **UBQLN2** into the nucleolus and ubiquitin-rich subnuclear protein-quality-control compartments, and it binds the N-terminal capsid of its paralog **PEG10** to antagonize PEG10 virus-like-particle formation while serving as the **obligate bridge** enabling PEG10 to recruit UBQLN2 into cytoplasmic stress granules. It thus acts at the **nucleolus** and in **cytoplasmic stress granules/PEG10 particles**, within **proteostasis and PEG10 retroelement-particle pathways**, and is expressed in **placental trophoblast and brain**.


## Artifacts

- [OpenScientist final report](Rtl8b-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Rtl8b-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:25888968
2. PMID:39775359
3. PMID:35247097
4. PMID:40680123
5. PMID:26680220
6. PMID:26241757