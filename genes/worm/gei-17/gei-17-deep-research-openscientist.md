---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-04T02:02:07.759481'
end_time: '2026-10-04T02:42:25.116617'
duration_seconds: 2417.36
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: worm
  gene_id: gei-17
  gene_symbol: gei-17
  uniprot_accession: Q94361
  protein_description: 'RecName: Full=E3 SUMO-protein ligase gei-17; EC=2.3.2.-; AltName:
    Full=E3 SUMO-protein transferase gei-17 {ECO:0000305}; AltName: Full=Gex-3-interacting
    protein 17;'
  gene_info: Name=gei-17 {ECO:0000312|WormBase:W10D5.3c}; ORFNames=W10D5.3 {ECO:0000312|WormBase:W10D5.3c};
  organism_full: Caenorhabditis elegans.
  protein_family: Belongs to the PIAS family. .
  protein_domains: PINIT. (IPR023321); PINIT_sf. (IPR038654); Znf_MIZ. (IPR004181);
    Znf_RING/FYVE/PHD. (IPR013083); PINIT (PF14324)
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
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: gei-17-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: gei-17-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q94361
- **Protein Description:** RecName: Full=E3 SUMO-protein ligase gei-17; EC=2.3.2.-; AltName: Full=E3 SUMO-protein transferase gei-17 {ECO:0000305}; AltName: Full=Gex-3-interacting protein 17;
- **Gene Information:** Name=gei-17 {ECO:0000312|WormBase:W10D5.3c}; ORFNames=W10D5.3 {ECO:0000312|WormBase:W10D5.3c};
- **Organism (full):** Caenorhabditis elegans.
- **Protein Family:** Belongs to the PIAS family. .
- **Key Domains:** PINIT. (IPR023321); PINIT_sf. (IPR038654); Znf_MIZ. (IPR004181); Znf_RING/FYVE/PHD. (IPR013083); PINIT (PF14324)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "gei-17" matches the protein description above**
2. **Verify the organism is correct:** Caenorhabditis elegans.
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'gei-17' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **gei-17** (gene ID: gei-17, UniProt: Q94361) in worm.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# gei-17 (Q94361): The PIAS-family SUMO E3 Ligase of *Caenorhabditis elegans*

## Gene/Protein Identity Verification

This report concerns **gei-17** (UniProt **Q94361**; WormBase/ORF **W10D5.3**), the *Caenorhabditis elegans* gene encoding an **E3 SUMO-protein ligase** of the **PIAS family** (EC 2.3.2.-). Identity was verified against the UniProt-provided target throughout:

- **Protein family match:** All primary literature describes GEI-17 as the *C. elegans* **PIAS** ortholog ("PIAS(GEI-17)"), matching the UniProt "Belongs to the PIAS family" designation.
- **Domain match:** UniProt lists the diagnostic PIAS domains **PINIT** (PF14324/IPR023321, residues ~203–367) and the **SP-RING / MIZ-type zinc finger** (Znf_MIZ IPR004181; RING/FYVE/PHD fold IPR013083, residues ~400–485). These are the catalytic hallmarks of the PIAS/Siz1 SUMO-ligase class.
- **Organism match:** Every cited study is in *C. elegans*.
- **Name origin:** "GEI" denotes a **G**ex-3 (GEX-3)-**i**nteracting protein; "gei-17" was named as a Gex-3-interacting protein, but its molecular identity is the nematode PIAS SUMO E3 ligase.

The gene symbol is **unambiguous** for this protein, and a well-developed body of primary *C. elegans* literature supports the functional annotation below. There is no cross-organism symbol confusion for "gei-17."

---

## Summary

**gei-17 encodes the single PIAS-family SUMO E3 ligase of *C. elegans***, a nuclear, zinc-dependent protein transferase (EC 2.3.2.-) that catalyzes the covalent attachment of the small ubiquitin-like modifier **SMO-1** (the worm SUMO/SMT3 ortholog) onto lysine residues of specific substrate proteins. GEI-17 works within the canonical SUMO cascade: the SUMO-activating E1, the single E2 conjugating enzyme **UBC-9**, and GEI-17 as the substrate-selecting E3. Mechanistically, its **SP-RING** domain recruits the charged E2~SUMO (UBC-9~SMO-1) thioester while its **PINIT** domain supports substrate/SUMO engagement — a mechanism established experimentally for the orthologous yeast PIAS ligase Ull1/Siz1 and inferred for GEI-17 by conserved domain architecture. In vitro, GEI-17 both SUMOylates substrates and undergoes extensive **auto-SUMOylation**.

GEI-17 is a **nuclear, chromatin-associated enzyme** that acts as a hub for regulated SUMOylation in three major arenas. **(1) Genome maintenance and DNA-damage tolerance:** GEI-17 was first discovered as the E3 that SUMOylates **MUS-101/TopBP1**, and it enables replication of damaged chromosomes by SUMOylating and stabilizing the translesion polymerase **POLH-1 (pol η)**, protecting it from CRL4-Cdt2-mediated proteolysis until translesion synthesis is complete. Together with *polh-1* and *rad-2*, GEI-17 **silences the ATL-1/CHK-1 (ATR–Chk1) DNA-damage checkpoint** in early embryos by suppressing replication-fork stalling. **(2) Chromosome segregation:** Through dynamic, spatially organized SUMOylation, GEI-17 drives both mitotic chromosome alignment and acentrosomal oocyte-meiotic segregation, building SUMO–SIM scaffolds and modifying the chromokinesin **KLP-19**, the kinase **BUB-1**, and the CLASP ortholog **CLS-2**. **(3) Transcription and nuclear organization:** GEI-17 SUMOylates specific transcription factors (the ETS factor **LIN-1** at K169; the T-box factor **TBX-2**), is required for **perinuclear telomere anchoring**, and regulates **piRNA transcription condensate** formation.

The unifying theme is that GEI-17 is a **nuclear SUMO-writing enzyme** that confers regulatory information — stability, localization, protein–protein scaffolding, and activity changes — onto chromatin-associated substrates during DNA replication/repair, chromosome segregation, and transcription. Its function is executed in the nucleus, on chromatin, at replication forks, and on the chromosome–spindle apparatus.

---

## Key Findings

### Finding 1 — GEI-17 is the sole PIAS-family SUMO E3 ligase in *C. elegans*, acting with E2 UBC-9 and SUMO SMO-1

GEI-17 is annotated in UniProt (Q94361) as "E3 SUMO-protein ligase gei-17; EC 2.3.2.-; Belongs to the PIAS family," a ~780-residue (~88 kDa) protein carrying the diagnostic **PINIT** domain (PF14324/IPR023321) and the **SP-RING / MIZ-type zinc finger** (IPR004181; a RING/FYVE/PHD-type zinc-binding fold, IPR013083). Multiple genetic and biochemical studies establish GEI-17 as the nematode PIAS ortholog that functions in the SUMO conjugation pathway alongside the single E2 conjugating enzyme **UBC-9** and the SUMO ortholog **SMO-1** (SMT3).

The direct biochemical evidence that GEI-17 is a catalytically active E3 comes from in vitro reconstitution. Pelisch and colleagues showed that "*In vitro analysis revealed that KLP-19 is efficiently sumoylated in a GEI-17-dependent manner, while GEI-17 undergoes extensive auto-sumoylation*" ([PMID: 27939944](https://pubmed.ncbi.nlm.nih.gov/27939944/)). This demonstrates both substrate SUMOylation activity and the characteristic PIAS auto-SUMOylation. Genetically, GEI-17 is paired with the E2 in vivo: "*Accumulation of SUMO conjugates on the metaphase plate and proper chromosome alignment depend on the SUMO E2 conjugating enzyme UBC-9 and SUMO E3 ligase PIAS(GEI-17)*" ([PMID: 25475837](https://pubmed.ncbi.nlm.nih.gov/25475837/)). Together these establish GEI-17's core molecular identity: a PIAS-type SUMO E3 ligase catalyzing the transfer of SMO-1 from UBC-9 to substrate lysines.

### Finding 2 — GEI-17 enables replication of damaged chromosomes by SUMOylating and stabilizing translesion polymerase POLH-1 (pol η)

A defining functional role of GEI-17 is in **DNA-damage tolerance**. Kim & Michael (2008) demonstrated that "*Both the POLH-1 (pol eta) translesion synthesis (TLS) DNA polymerase and the GEI-17 SUMO E3 ligase are essential for the efficient replication of damaged chromosomes in Caenorhabditis elegans embryos*" ([PMID: 19111656](https://pubmed.ncbi.nlm.nih.gov/19111656/)). Upon DNA damage, POLH-1 is normally targeted for destruction by the **CRL4-Cdt2** (Cul4–Ddb1–Cdt2) ubiquitin ligase. GEI-17 counteracts this: "*GEI-17 protects POLH-1 from CRL4-Cdt2-mediated destruction until after it has performed its function in TLS, and this is likely via SUMOylation of POLH-1*" ([PMID: 19111656](https://pubmed.ncbi.nlm.nih.gov/19111656/)).

This finding is mechanistically precise and illustrates the "regulatory information" model of SUMOylation: GEI-17 does not act as a protease or a kinase, but writes a SUMO mark on POLH-1 that **antagonizes its ubiquitin-dependent proteolysis**, thereby timing the availability of the TLS polymerase to the window when it is needed to bypass lesions. The consequence of this activity — preventing replication-fork stalling on damaged templates — links directly to checkpoint silencing (Finding 5). This role is captured in the curated GO terms "positive regulation of error-prone translesion synthesis" (GO:1904333, IMP) and "negative regulation of protein catabolic process" (GO:0042177, IMP).

### Finding 3 — GEI-17 drives mitotic and meiotic chromosome segregation through dynamic, spatially organized SUMOylation

GEI-17 is central to chromosome segregation in both mitotic and meiotic divisions. In **mitosis**, chromatin-associated SUMO conjugates rise at metaphase and fall at anaphase; metaphase-plate SUMO accumulation and proper chromosome alignment require UBC-9 and GEI-17 ([PMID: 25475837](https://pubmed.ncbi.nlm.nih.gov/25475837/)). The system is dynamic in both directions — deconjugation by the SUMO protease ULP-4 is needed for Aurora-B (AIR-2) relocation and cell-cycle progression — underscoring that it is the *cycle* of SUMOylation/deSUMOylation, written by GEI-17 and erased by proteases, that organizes mitotic chromosome behavior.

In **oocyte meiosis**, which in *C. elegans* occurs on an **acentrosomal spindle**, GEI-17 assembles the machinery for chromosome congression. Pelisch et al. (2017) showed that "*SUMO E3 ligase GEI-17/PIAS is required for KLP-19 recruitment to the RC [ring complex], and proteomic analysis identified KLP-19 as a SUMO substrate in vivo*" ([PMID: 27939944](https://pubmed.ncbi.nlm.nih.gov/27939944/)). The mechanism is a **SUMO–SIM (SUMO-interaction motif) protein network**: "*GEI-17 and another RC component, the kinase BUB-1, contain functional SUMO interaction motifs (SIMs), allowing them to recruit SUMO modified proteins, including KLP-19, into the RC*" ([PMID: 27939944](https://pubmed.ncbi.nlm.nih.gov/27939944/)). GEI-17 therefore builds a self-organizing scaffold: it SUMOylates substrates and, via its own SIM and those of partner proteins, cross-links SUMOylated components into the inter-homolog ring complex that drives chromosome congression and segregation.

### Finding 4 — GEI-17 SUMOylates specific transcription factors and regulates telomere anchoring and piRNA transcription

Beyond replication and segregation, GEI-17 modifies the activity and localization of **nuclear transcription and chromatin factors**. During **vulval development**, tissue-specific auxin-induced degradation (AID) of GEI-17/SMO-1 disrupts anchor-cell positioning, basement-membrane breaching, vulval precursor cell fate, and morphogenesis; crucially, "*sumoylation of the ETS transcription factor LIN-1 at K169 is necessary for the proper contraction of the ventral vulA toroids*" ([PMID: 35666766](https://pubmed.ncbi.nlm.nih.gov/35666766/)). This identifies a specific substrate (LIN-1), a specific modified residue (K169), and a defined morphogenetic consequence.

GEI-17 is also linked to the T-box transcription factor **TBX-2**: "*TBX-2 contains 2 consensus sumoylation sites, and it interacts in a yeast two-hybrid assay with the UBC-9 and GEI-17 components of the C. elegans SUMO-conjugating pathway*" ([PMID: 16701625](https://pubmed.ncbi.nlm.nih.gov/16701625/)), a function required for ABa-derived pharyngeal muscle development.

In **nuclear architecture**, perinuclear telomere anchoring in embryos requires GEI-17: "*Telomere position in early embryos required the NE protein SUN-1, the single-strand binding protein POT-1, and the small ubiquitin-like modifier (SUMO) ligase GEI-17*" ([PMID: 24297748](https://pubmed.ncbi.nlm.nih.gov/24297748/)). Finally, GEI-17 regulates **piRNA transcription**: "*we searched for factors that regulate piRNA transcription and isolated the SUMO E3 ligase GEI-17 as inhibiting and the SUMO protease TOFU-3 as promoting piRNA transcription foci formation, thereby regulating piRNA production*" ([PMID: 40316696](https://pubmed.ncbi.nlm.nih.gov/40316696/)). Here GEI-17 opposes the formation of transcriptional condensates, with the SUMO protease TOFU-3 acting in the opposite direction — again illustrating the writer/eraser balance that tunes GEI-17's outputs.

### Finding 5 — GEI-17 (with POLH-1 and rad-2) silences the ATL-1/CHK-1 DNA-damage checkpoint in embryos

A striking developmental role of GEI-17 is in **checkpoint silencing**. In early *C. elegans* embryos, the DNA-damage checkpoint is actively suppressed so that the rapid, scheduled divisions of the P (germline) lineage can proceed. Holway et al. (2006) found that "*the checkpoint response to DNA damage is actively silenced in embryos but not in the germ line*," and that "*Silencing requires rad-2, gei-17, and the polh-1 translesion DNA polymerase, which suppress replication fork stalling and thereby eliminate the checkpoint-activating signal*" ([PMID: 16549501](https://pubmed.ncbi.nlm.nih.gov/16549501/)).

This places GEI-17 upstream in a mechanistically coherent pathway: by stabilizing POLH-1 (Finding 2), GEI-17 ensures efficient translesion synthesis, which prevents replication forks from stalling on damaged templates. Because stalled forks generate the single-stranded DNA/RPA signal that activates ATL-1 (ATR) and downstream CHK-1 (Chk1), suppressing fork stalling **eliminates the checkpoint-activating signal** at its source. A parallel silencing mechanism operates through the SMK-1/PPH-4.1 phosphatase, which recruits protein phosphatase 4 to replicating chromatin to silence the CHK-1 response ([PMID: 17908915](https://pubmed.ncbi.nlm.nih.gov/17908915/)); the GEI-17/POLH-1 pathway and the SMK-1/PPH-4.1 pathway together keep the embryonic ATL-1–CHK-1 axis quiet. This is reflected in the GO annotation "negative regulation of mitotic DNA damage checkpoint" (GO:1904290, IMP).

### Finding 6 — Domain-based mechanistic inference: PINIT and SP-RING domains execute SUMO transfer

GEI-17's catalytic mechanism can be inferred with high confidence from its conserved domain architecture and from direct experiments on orthologous PIAS/Siz-type ligases. Takahashi & Kikuchi (2005), studying the yeast PIAS-type ligase Ull1/Siz1, showed that "*A novel conserved N-terminal domain, called PINIT, as well as the RING-like domain (SP-RING) were required for the SUMO ligase activity in the in vitro conjugation system and for interaction with Smt3 in an in vitro binding assay*" ([PMID: 16109721](https://pubmed.ncbi.nlm.nih.gov/16109721/)). They further defined the catalytic logic of this enzyme class: "*E3 (SUMO ligase) functions as an adaptor between E2 and each substrate*" ([PMID: 16109721](https://pubmed.ncbi.nlm.nih.gov/16109721/)).

Because GEI-17 carries both diagnostic domains — **PINIT** (residues ~203–367) and the **SP-RING zinc finger** (residues ~400–485) — the inference is direct: the SP-RING domain recruits and positions the charged E2~SUMO (UBC-9~SMO-1) thioester for catalysis, while the PINIT domain supports substrate and SUMO engagement. In the orthologous enzyme, the N-terminal SAP motif governs DNA binding and nuclear localization rather than catalysis, consistent with GEI-17 being a chromatin-associated enzyme whose catalytic core resides in the PINIT + SP-RING module.

### Finding 7 — Original characterization: GEI-17 SUMOylates MUS-101/TopBP1; authoritative GO places it on chromatin in the nucleus

GEI-17 was originally characterized by Holway, Hung & Michael (2005) in a systematic RNAi screen for modifiers of *mus-101* (the *C. elegans* Mus101/**TopBP1** ortholog, a replication and DNA-damage factor). Among chromosome I modifiers, "*we have found five chromosome I genes that modify the mus-101 RNAi phenotype, and we go on to show that one of them encodes an E3 SUMO ligase that promotes SUMO modification of MUS-101 in vitro*" ([PMID: 15654100](https://pubmed.ncbi.nlm.nih.gov/15654100/)). This is the founding identification of gei-17 as a SUMO E3 ligase and the demonstration of its in vitro activity toward a specific substrate (MUS-101/TopBP1). UniProt Q94361 cites this work as the defining FUNCTION statement ("Functions as an E3-type smo-1 ligase") and assigns the PATHWAY "protein sumoylation."

Curated **Gene Ontology** annotations in WormBase corroborate the nuclear, chromatin-based identity:

| GO aspect | Term | Evidence |
|---|---|---|
| Cellular component | chromatin (GO:0000785) | IDA |
| Cellular component | metaphase plate (GO:0070090) | IDA |
| Cellular component | nucleoplasm | IBA |
| Molecular function | SUMO ligase activity (GO:0061665) | IDA |
| Molecular function | RNA Pol II transcription factor binding; transcription coregulator/inhibitor; zinc ion binding | — |
| Biological process | DNA damage response | IMP |
| Biological process | positive regulation of error-prone translesion synthesis (GO:1904333) | IMP |
| Biological process | negative regulation of mitotic DNA damage checkpoint (GO:1904290) | IMP |
| Biological process | negative regulation of protein catabolic process (GO:0042177) | IMP |
| Biological process | meiotic metaphase I homologous chromosome alignment | IMP |
| Biological process | protein sumoylation | IDA |

These annotations independently recapitulate every major experimental finding above: SUMO ligase activity, chromatin/metaphase-plate localization, translesion synthesis, checkpoint suppression, protection from proteolysis, and meiotic chromosome alignment.

### Finding 8 — In oocyte meiosis GEI-17 SUMOylates BUB-1 and regulates CLS-2/CLASP during anaphase I

The meiotic role extends beyond KLP-19 to the kinase BUB-1 and the CLASP ortholog CLS-2. Pelisch et al. (2019) reported that "*SUMO modification of BUB-1 is regulated by the SUMO E3 ligase GEI-17 and the SUMO protease ULP-1. SUMO and GEI-17 are required for BUB-1 localisation between segregating chromosomes during early anaphase I*" ([PMID: 31243051](https://pubmed.ncbi.nlm.nih.gov/31243051/)). Furthermore, "*CLS-2 is subject to SUMO-mediated regulation; CLS-2 precociously localises in the midbivalent when either SUMO or GEI-17 are depleted*" ([PMID: 31243051](https://pubmed.ncbi.nlm.nih.gov/31243051/)). CLS-2/CLASP is a microtubule-stabilizing protein that generates poleward force; GEI-17-dependent SUMOylation controls the **timing** of its localization. Thus GEI-17 governs the ordered, timed dynamics of multiple proteins (KLP-19, BUB-1, CLS-2) on the acentrosomal spindle to achieve faithful chromosome segregation during anaphase I.

---

## Mechanistic Model / Interpretation

GEI-17 is best understood as a **nuclear SUMO "writer"** whose single biochemical activity — transferring SMO-1 from UBC-9 onto substrate lysines — is deployed across several chromatin-based processes. In each case, the SUMO mark confers one of a small set of regulatory outcomes: **protection from proteolysis**, **protein localization/scaffolding via SUMO–SIM interactions**, or **modulation of transcription-factor/condensate activity**. The outputs are shaped not only by GEI-17 but by opposing **SUMO proteases** (ULP-1, ULP-4, TOFU-3), making SUMOylation a dynamic, reversible regulatory layer.

### The core enzymatic cascade

```
   SMO-1 (SUMO)
      │  E1 activation (ATP)
      ▼
   E1 ~ SMO-1
      │  transthiolation
      ▼
   UBC-9 (E2) ~ SMO-1  ──────┐
                             │  SP-RING domain positions E2~SUMO
      GEI-17 (PIAS E3) ◄─────┘
      │  PINIT domain engages substrate/SUMO
      ▼
   Substrate–Lys–SMO-1   ◄──►  SUMO proteases (ULP-1, ULP-4, TOFU-3)
   (+ GEI-17 auto-SUMOylation)        [reversal / erasure]
```

### Substrate map and functional outputs

| Substrate | Process | SUMOylation outcome | Localization | Evidence (PMID) |
|---|---|---|---|---|
| **MUS-101/TopBP1** | DNA replication/damage | SUMO modification (in vitro) | chromatin | [15654100](https://pubmed.ncbi.nlm.nih.gov/15654100/) |
| **POLH-1 (pol η)** | Translesion synthesis | Protection from CRL4-Cdt2 proteolysis; times TLS | replication fork | [19111656](https://pubmed.ncbi.nlm.nih.gov/19111656/) |
| **KLP-19** (chromokinesin) | Meiotic congression | Recruitment to ring complex via SUMO–SIM | midbivalent/RC | [27939944](https://pubmed.ncbi.nlm.nih.gov/27939944/) |
| **BUB-1** (kinase) | Meiotic anaphase I | Localization between segregating chromosomes | spindle midzone | [31243051](https://pubmed.ncbi.nlm.nih.gov/31243051/) |
| **CLS-2/CLASP** | Meiotic force generation | Timing of midbivalent localization | spindle | [31243051](https://pubmed.ncbi.nlm.nih.gov/31243051/) |
| **LIN-1** (ETS TF) | Vulval morphogenesis | SUMO at K169; vulA toroid contraction | nucleus | [35666766](https://pubmed.ncbi.nlm.nih.gov/35666766/) |
| **TBX-2** (T-box TF) | Pharyngeal muscle | Consensus SUMO sites; interaction | nucleus | [16701625](https://pubmed.ncbi.nlm.nih.gov/16701625/) |
| (telomere complex) | Telomere anchoring | Perinuclear tethering via SUN-1/POT-1 | nuclear periphery | [24297748](https://pubmed.ncbi.nlm.nih.gov/24297748/) |

### Integrated logic of the DNA-damage / checkpoint module

```
  DNA damage  ──►  CRL4-Cdt2 targets POLH-1 for degradation
                          │
                GEI-17 SUMOylates POLH-1  ──►  POLH-1 stabilized
                          │
                Efficient translesion synthesis
                          │
                Replication forks do NOT stall
                          │
                No ssDNA/RPA signal ──► ATL-1 (ATR)/CHK-1 (Chk1) NOT activated
                          │
                Embryonic P-lineage divisions stay on schedule
```

This single module explains three GO annotations at once: *positive regulation of error-prone translesion synthesis*, *negative regulation of protein catabolic process* (stabilizing POLH-1), and *negative regulation of the mitotic DNA-damage checkpoint*. It is the clearest example of GEI-17's "write a SUMO mark → change a protein's fate → change a cellular decision" logic.

### Where GEI-17 works

GEI-17 is a **nuclear** enzyme. Its catalytic actions occur on **chromatin** (SUMO ligase activity, GO:0000785 IDA), at **replication forks** (POLH-1/MUS-101), on the **metaphase plate** and **acentrosomal meiotic spindle/ring complex** (KLP-19, BUB-1, CLS-2), at the **nuclear periphery** (telomere anchoring), and at sites of **piRNA transcription**. It does not have a described extracellular or cytoplasmic catalytic role; its SAP-motif/DNA-binding and nuclear-localization determinants (by orthology to Ull1/Siz1) keep it chromatin-proximal.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution to the annotation |
|---|---|---|
| [15654100](https://pubmed.ncbi.nlm.nih.gov/15654100/) | *mus-101 modifier RNAi screen* | **Founding identification** of gei-17 as an E3 SUMO ligase; SUMOylates MUS-101/TopBP1 in vitro. |
| [19111656](https://pubmed.ncbi.nlm.nih.gov/19111656/) | *Regulated proteolysis of pol η* | GEI-17 stabilizes POLH-1 via SUMOylation, protecting it from CRL4-Cdt2; enables damaged-chromosome replication. |
| [16549501](https://pubmed.ncbi.nlm.nih.gov/16549501/) | *Checkpoint silencing in embryos* | gei-17 (+ polh-1, rad-2) silences the embryonic ATL-1/CHK-1 checkpoint by suppressing fork stalling. |
| [17908915](https://pubmed.ncbi.nlm.nih.gov/17908915/) | *SMK-1/PPH-4.1 silencing* | Parallel checkpoint-silencing pathway; contextualizes GEI-17's role in the embryonic DNA-damage response. |
| [25475837](https://pubmed.ncbi.nlm.nih.gov/25475837/) | *Dynamic SUMO in mitosis* | GEI-17 + UBC-9 required for metaphase-plate SUMO and chromosome alignment; ULP-4 reverses. |
| [27939944](https://pubmed.ncbi.nlm.nih.gov/27939944/) | *SUMO network in oocyte meiosis* | GEI-17 SUMOylates KLP-19; SUMO–SIM scaffold (GEI-17, BUB-1 SIMs) builds the ring complex; auto-SUMOylation shown. |
| [31243051](https://pubmed.ncbi.nlm.nih.gov/31243051/) | *Sumoylation in meiotic segregation* | GEI-17 SUMOylates BUB-1; regulates CLS-2/CLASP timing in anaphase I. |
| [35666766](https://pubmed.ncbi.nlm.nih.gov/35666766/) | *SUMO in vulval development* | GEI-17/SMO-1 sumoylate LIN-1 at K169; diverse developmental SUMO functions. |
| [16701625](https://pubmed.ncbi.nlm.nih.gov/16701625/) | *TBX-2 and UBC-9* | TBX-2 interacts with UBC-9/GEI-17; links GEI-17 to a T-box transcription factor. |
| [24297748](https://pubmed.ncbi.nlm.nih.gov/24297748/) | *POT-1 telomere anchoring* | GEI-17 required for perinuclear telomere anchoring via SUN-1/POT-1. |
| [40316696](https://pubmed.ncbi.nlm.nih.gov/40316696/) | *piRNA condensate formation* | GEI-17 inhibits piRNA transcription foci (TOFU-3 promotes); regulates piRNA production. |
| [16109721](https://pubmed.ncbi.nlm.nih.gov/16109721/) | *Yeast Ull1/Siz1 domains* | Experimental basis for GEI-17 mechanism: PINIT + SP-RING required for SUMO-ligase activity; E3 = E2–substrate adaptor. |
| [27631810](https://pubmed.ncbi.nlm.nih.gov/27631810/) | *Tools to study SUMO in C. elegans* | Methods review establishing the reagents (E3 ligases, SUMO proteases) used to dissect GEI-17 function. |
| [31614335](https://pubmed.ncbi.nlm.nih.gov/31614335/) | *PIASy regulation of MafA* | Mammalian PIAS comparator: PIAS can repress transcription SUMOylation-independently via SIM — relevant to interpreting GEI-17's non-catalytic scaffolding. |

**Convergence of evidence.** The annotation rests on multiple orthogonal lines: (i) **direct in vitro biochemistry** (SUMOylation of MUS-101 and KLP-19; auto-SUMOylation); (ii) **genetics/RNAi/AID** (phenotypes for replication, checkpoint, segregation, development); (iii) **in vivo proteomics** (KLP-19 as a SUMO substrate); (iv) **curated GO (IDA/IMP)**; and (v) **domain-based inference** anchored to experimentally validated orthologs. The DNA-damage/checkpoint and meiotic-segregation stories are each supported by two or more primary papers.

**A note on PIAS versatility.** The mammalian PIASy–MafA study ([PMID: 31614335](https://pubmed.ncbi.nlm.nih.gov/31614335/)) shows that PIAS proteins can also repress transcription through a **SIM-dependent, SUMOylation-independent** mechanism, with the PINIT and SP-RING domains dispensable for that particular repression. This cautions that some of GEI-17's transcriptional/condensate effects (e.g., LIN-1, TBX-2, piRNA foci) may combine catalytic SUMOylation with non-catalytic SIM-mediated scaffolding — a nuance worth testing in the worm.

---

## Limitations and Knowledge Gaps

1. **Direct substrate lysine mapping is sparse.** For several substrates (MUS-101, POLH-1, KLP-19, BUB-1), the modified lysine(s) and the in vivo stoichiometry/dynamics are not fully defined. The best-mapped site is LIN-1 K169. Precise site-level SUMO acceptor maps are largely missing.

2. **Catalytic vs. scaffolding contributions are not separated.** GEI-17 has both SUMO-ligase activity and a SUMO-interaction capacity (SIM). Which outputs require catalysis versus SIM-mediated scaffolding (as seen for mammalian PIASy–MafA) has not been dissected with catalytic-dead (SP-RING mutant) versus SIM-mutant GEI-17 for most processes.

3. **No experimental structure of GEI-17.** The domain-level mechanism is inferred from yeast Ull1/Siz1 and the PIAS family; there is no worm-specific structural data (crystal/cryo-EM/validated AlphaFold analysis) presented here to confirm the E2~SUMO docking geometry.

4. **Redundancy and specificity within the SUMO system.** GEI-17 is described as the sole PIAS-family E3, but the extent to which substrate selection depends on GEI-17 versus the shared E2 UBC-9, versus additional non-PIAS E3-like factors, is incompletely resolved for some substrates.

5. **Opposing proteases.** The erasers (ULP-1, ULP-4, TOFU-3) shape GEI-17's net output, but the full writer/eraser network and its spatial/temporal regulation remain only partially mapped.

6. **Quantitative/structural bioinformatics not performed here.** This report is literature- and annotation-based; no new sequence/structure analysis (e.g., conservation of the SP-RING zinc-coordinating residues, SIM prediction) was independently computed.

---

## Proposed Follow-up Experiments / Actions

1. **Separation-of-function alleles.** Engineer (CRISPR) an SP-RING catalytic-dead GEI-17 and a SIM-mutant GEI-17, and test each across the four arenas (TLS/checkpoint, mitotic alignment, meiotic ring complex, transcription/piRNA) to partition catalytic vs. scaffolding requirements — directly testing the PIASy–MafA-inspired hypothesis.

2. **In vivo SUMO-site proteomics.** Perform SUMO-remnant immunoaffinity MS in wild-type vs. *gei-17* depletion to map acceptor lysines on POLH-1, MUS-101, KLP-19, BUB-1, and CLS-2, and to define the GEI-17-dependent SUMO proteome.

3. **Non-degradable/non-SUMOylatable POLH-1.** Test POLH-1 lysine-to-arginine (SUMO-site) and degron mutants to confirm that SUMOylation is the signal protecting POLH-1 from CRL4-Cdt2 and timing TLS.

4. **Structure determination / validated modeling.** Solve or model (AlphaFold-Multimer, with PAE/pLDDT validation) the GEI-17 SP-RING–UBC-9~SMO-1 complex to confirm the catalytic geometry inferred from Ull1/Siz1.

5. **Live imaging of SUMO dynamics.** Use the established worm SUMO-reporter toolkit ([PMID: 27631810](https://pubmed.ncbi.nlm.nih.gov/27631810/)) to quantify GEI-17-dependent SUMO conjugation/deconjugation in space and time at forks, the metaphase plate, and the meiotic ring complex, with and without the opposing proteases.

6. **Condensate mechanism for piRNA.** Determine whether GEI-17 inhibits piRNA transcription foci by SUMOylating a specific condensate component (vs. SIM-mediated sequestration), and identify the TOFU-3 target that it counteracts.

---

## Conclusion

**gei-17 (Q94361) encodes the single PIAS-family SUMO E3 ligase of *C. elegans***: a nuclear, zinc-dependent protein transferase (EC 2.3.2.-) whose PINIT and SP-RING/MIZ domains transfer the SUMO ortholog SMO-1 from the E2 UBC-9 onto substrate lysines (with extensive auto-SUMOylation). This single activity underlies three major, well-evidenced functions — (1) DNA-damage tolerance and silencing of the ATL-1/CHK-1 checkpoint via SUMOylation of MUS-101/TopBP1 and stabilization of POLH-1/pol η; (2) mitotic and acentrosomal-meiotic chromosome segregation via SUMO–SIM scaffolds and modification of KLP-19, BUB-1, and CLS-2/CLASP; and (3) transcriptional/nuclear-organization control (LIN-1 K169, TBX-2, telomere anchoring, piRNA condensates). GEI-17 executes its function **in the nucleus — on chromatin, at replication forks, and on the chromosome–spindle apparatus**.


## Artifacts

- [OpenScientist final report](gei-17-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](gei-17-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:27939944
2. PMID:25475837
3. PMID:19111656
4. PMID:35666766
5. PMID:16701625
6. PMID:24297748
7. PMID:40316696
8. PMID:16549501
9. PMID:17908915
10. PMID:16109721
11. PMID:15654100
12. PMID:31243051
13. PMID:31614335
14. PMID:27631810