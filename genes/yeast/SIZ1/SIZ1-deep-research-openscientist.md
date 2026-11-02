---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-04T02:02:07.696182'
end_time: '2026-10-04T02:41:24.080532'
duration_seconds: 2356.38
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: yeast
  gene_id: SIZ1
  gene_symbol: SIZ1
  uniprot_accession: Q04195
  protein_description: 'RecName: Full=E3 SUMO-protein ligase SIZ1; EC=2.3.2.-; AltName:
    Full=E3 SUMO-protein transferase SIZ2 {ECO:0000305}; AltName: Full=SAP and Miz-finger
    domain-containing protein 1; AltName: Full=Ubiquitin-like protein ligase 1;'
  gene_info: Name=SIZ1; Synonyms=ULL1; OrderedLocusNames=YDR409W;
  organism_full: Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
  protein_family: Belongs to the PIAS family. .
  protein_domains: PINIT. (IPR023321); PINIT_sf. (IPR038654); SAP_dom. (IPR003034);
    SAP_dom_sf. (IPR036361); SIZ1/2_SP-RING. (IPR031141)
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
citation_count: 32
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SIZ1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SIZ1-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q04195
- **Protein Description:** RecName: Full=E3 SUMO-protein ligase SIZ1; EC=2.3.2.-; AltName: Full=E3 SUMO-protein transferase SIZ2 {ECO:0000305}; AltName: Full=SAP and Miz-finger domain-containing protein 1; AltName: Full=Ubiquitin-like protein ligase 1;
- **Gene Information:** Name=SIZ1; Synonyms=ULL1; OrderedLocusNames=YDR409W;
- **Organism (full):** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
- **Protein Family:** Belongs to the PIAS family. .
- **Key Domains:** PINIT. (IPR023321); PINIT_sf. (IPR038654); SAP_dom. (IPR003034); SAP_dom_sf. (IPR036361); SIZ1/2_SP-RING. (IPR031141)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SIZ1" matches the protein description above**
2. **Verify the organism is correct:** Saccharomyces cerevisiae (strain ATCC 204508 / S288c) (Baker's yeast).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SIZ1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SIZ1** (gene ID: SIZ1, UniProt: Q04195) in yeast.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SIZ1 (Q04195 / YDR409W): A Functional Annotation Report

**Gene:** *SIZ1* (synonym *ULL1*; ordered locus *YDR409W*)
**Protein:** E3 SUMO-protein ligase SIZ1 (EC 2.3.2.-)
**Organism:** *Saccharomyces cerevisiae* (strain ATCC 204508 / S288c), baker's yeast
**UniProt:** Q04195
**Family:** Siz/PIAS family of SP-RING SUMO E3 ligases
**Key domains:** SAP (IPR003034/IPR036361); PINIT (IPR023321/IPR038654); SIZ1/2 SP-RING (IPR031141)

---

## Identity Verification

Before presenting the research narrative it is worth confirming that the literature assembled here concerns the correct molecule. Every primary paper cited below studies the budding-yeast gene product encoded by *YDR409W*, explicitly named **Siz1**, and characterizes it as a **PIAS-family SUMO (Smt3) E3 ligase** carrying a **PINIT domain** and a **RING-like SP-RING domain** — in full agreement with the UniProt description (Q04195), the gene synonyms (*ULL1*, "ubiquitin-like protein ligase 1"), and the listed InterPro domains. The one recurrent source of ambiguity is the *plant* SIZ1 (*Arabidopsis thaliana* AtSIZ1 and its crop orthologs), which shares the name and the Siz/PIAS architecture but adds a plant-specific PHD finger and governs plant stress and developmental phenotypes (e.g., [PMID: 30657769](https://pubmed.ncbi.nlm.nih.gov/30657769/), [PMID: 33710720](https://pubmed.ncbi.nlm.nih.gov/33710720/), [PMID: 31925312](https://pubmed.ncbi.nlm.nih.gov/31925312/)). Those plant studies are **not** used to support claims about the yeast enzyme; they are noted only as evolutionary context. All mechanistic and functional conclusions below derive from studies of *S. cerevisiae* Siz1 (or, where explicitly stated, biochemically reconstituted yeast systems).

---

## Summary

**Siz1 is the principal SP-RING–type E3 SUMO (Smt3) ligase of budding yeast.** Its primary molecular function is to catalyze the final, substrate-directing step of SUMO conjugation: it binds the SUMO-charged E2 enzyme Ubc9, positions a substrate lysine for nucleophilic attack, and thereby transfers the small ubiquitin-like modifier Smt3 onto target proteins (reaction class EC 2.3.2.-, isopeptide-bond/aminoacyltransferase chemistry). Siz1 is not a classical enzyme that acts on a small-molecule substrate; it is a protein-modifying **scaffold/adaptor ligase** whose "substrate specificity" is the set of cellular proteins it directs Smt3 onto, and whose catalytic contribution is to accelerate conjugation and to extend it to lysines the E2 cannot reach on its own.

Structurally and mechanistically, Siz1 is a tripartite enzyme — an N-terminal **PINIT** domain, a central zinc-binding **SP-RING** domain, and a C-terminal **SP-CTD** — with an additional **SAP** DNA-binding motif. The SP-RING and SP-CTD perform the generic RING-type catalysis of activating the Ubc9~SUMO thioester, while the PINIT domain redirects the modification onto specific (often non-consensus) lysines, the textbook example being PCNA Lys164. Together with its paralog Siz2, Siz1 is responsible for the great majority of cellular sumoylation in yeast. Remarkably, substrate choice in vivo is governed less by direct sequence recognition than by **where the ligase is concentrated** — a spatial/local-concentration model.

Functionally, Siz1 operates in **two cellular compartments under cell-cycle control**. In the nucleus it sumoylates PCNA (recruiting the Srs2 helicase to suppress recombination at replication forks), components of the transcription machinery during the SUMO stress response, kinetochore and meiotic chromosome-axis proteins, and numerous genome-maintenance factors. At the **cytoplasmic bud neck** during mitosis it sumoylates the septins. Its shuttling between these locations is executed by karyopherins (Kap95 import; Msn5/Kap142 export), and its activity is further tuned by phosphorylation, reciprocal ubiquitin crosstalk with Rsp5, and STUbL-mediated degradation of its nuclear pool. This report synthesizes nine confirmed findings drawn from 48 reviewed papers into a coherent mechanistic account.

---

## Key Findings

### 1. Siz1 is a PIAS-family SP-RING SUMO E3 ligase acting as an E2–substrate adaptor

Siz1 was first identified biochemically as the factor required for conjugation of the yeast SUMO ortholog Smt3 to septins in vivo. Deletion or mutation of *SIZ1* abolishes septin sumoylation, and a conserved cysteine within its RING-like (SP-RING) domain is essential for activity, pinpointing a zinc-coordinating catalytic fold analogous to ubiquitin-ligase RING domains ([PMID: 11572779](https://pubmed.ncbi.nlm.nih.gov/11572779/); [PMID: 11587849](https://pubmed.ncbi.nlm.nih.gov/11587849/)). Johnson & Gupta showed that "**Siz1 is required for SUMO attachment to the *S. cerevisiae* septins in vivo and strongly stimulates septin sumoylation in vitro**," and further that "**Siz1 and the related protein Siz2 promote SUMO conjugation to different substrates … and, together, are required for most SUMO conjugation in yeast**" ([PMID: 11572779](https://pubmed.ncbi.nlm.nih.gov/11572779/)). Takahashi et al. independently reported "**a novel factor Siz1 (YDR409w) required for septin-sumoylation of budding yeast, possibly acting as E3** … a member of a new family (Miz1, PIAS3, etc.) containing a conserved … RING-domain" ([PMID: 11587849](https://pubmed.ncbi.nlm.nih.gov/11587849/)).

Domain dissection established that "**a novel conserved N-terminal domain, called PINIT, as well as the RING-like domain (SP-RING) were required for the SUMO ligase activity in the in vitro conjugation system and for interaction with Smt3**" ([PMID: 16109721](https://pubmed.ncbi.nlm.nih.gov/16109721/)). Mechanistically, as a RING-class E3 Siz1 works by physically binding both the E2 (Ubc9) and the target and by "**bypass[ing] E2 specificity to force-feed a substrate lysine into the E2 active site**" ([PMID: 27509863](https://pubmed.ncbi.nlm.nih.gov/27509863/)). In short, Siz1 is a protein-modifying ligase, not a metabolic enzyme; its catalytic output is an isopeptide bond between Smt3's C-terminal glycine and a substrate-lysine ε-amino group.

### 2. Distinct Siz1 domains select substrates; specificity is driven by local concentration, not direct contact

Siz1 and Siz2 each have unique in vivo substrates but can redundantly sumoylate a large shared set. Reindle et al. mapped substrate choice onto separate Siz1 modules: "**Sumoylation of PCNA … and the splicing factor Prp45 requires … the 'PINIT' domain, whereas sumoylation of the bud neck-associated septin proteins Cdc3, Cdc11 and Shs1/Sep7 requires the C-terminal domain of Siz1**" ([PMID: 17077124](https://pubmed.ncbi.nlm.nih.gov/17077124/)). Crucially, septins Cdc10/Cdc12 — normally not Siz1 substrates — became Siz1-dependent substrates when fused to a ΨKxE SUMO consensus, leading the authors to conclude that "**local concentration of the E3, rather than a single direct interaction with the substrate polypeptide, is the major factor in substrate selectivity by Siz proteins**" ([PMID: 17077124](https://pubmed.ncbi.nlm.nih.gov/17077124/)). This **spatial/local-concentration model** is a defining feature of how Siz-family ligases achieve specificity.

At genome scale, quantitative SUMO-proteomics confirmed the breadth of this control: Albuquerque et al. "**found that Siz1 and Siz2 redundantly control the abundances of most sumoylated substrates**" ([PMID: 23935535](https://pubmed.ncbi.nlm.nih.gov/23935535/)). Thus Siz1 is both a specific ligase (via distinct targeting domains) and, with Siz2, the bulk workhorse of the cellular SUMO proteome.

### 3. Siz1 shuttles between nucleus and cytoplasmic bud neck under karyopherin/cell-cycle control

Siz1 is a mobile enzyme whose localization defines where it works. It localizes to the mother–bud neck in M phase and there binds both the E2 and septin targets ([PMID: 11587849](https://pubmed.ncbi.nlm.nih.gov/11587849/)): "**Siz1 was localized at the mother-bud neck in the M-phase and physically bound to both E2 and the target proteins.**" Its SAP motif and distal N-terminus mediate nuclear import, while the distal C-terminal domain is required for stable bud-neck localization and septin recognition ([PMID: 16109721](https://pubmed.ncbi.nlm.nih.gov/16109721/)).

This trafficking is **karyopherin-controlled and cell-cycle-regulated**. Makhnevych et al. showed that "**The E3 ligase Siz1p is imported into the nucleus by the karyopherin Kap95p during interphase. In M phase, Siz1p is exported from the nucleus by the karyopherin Kap142p/Msn5p and subsequently targeted to the septin ring, where it participates in septin sumoylation**" ([PMID: 17403926](https://pubmed.ncbi.nlm.nih.gov/17403926/)). The counteracting SUMO isopeptidase Ulp1 is tethered at the nuclear pore complex, spatially separating conjugation (bud neck) from deconjugation (NPC). This establishes Siz1 as a provider of SUMO conjugation in **both the nucleus and the cytoplasm** ([PMID: 18583943](https://pubmed.ncbi.nlm.nih.gov/18583943/)): "**SUMO modification of septins is regulated by cell cycle-dependent nuclear transport of PIAS-type Siz1 (SUMO E3) and Ulp1 desumoylation enzyme in yeast.**"

### 4. Siz1 is the dedicated ligase for PCNA-K164 SUMOylation, recruiting Srs2 to suppress recombination at forks

One of Siz1's best-defined and most mechanistically important jobs is sumoylating the DNA-replication sliding clamp PCNA. Modification of PCNA on Lys164 (and Lys127) during S phase is **strictly Siz1-dependent**: "**For SUMO, Lys164 modification is strictly dependent on the E3 ligase Siz1, suggesting the E3 alters E2 specificity to promote Lys164 modification**" ([PMID: 27509863](https://pubmed.ncbi.nlm.nih.gov/27509863/)), and Siz1 and Ubc9 "**are responsible for PCNA sumoylation during undisturbed S phase and in response to fork stalling**" ([PMID: 20847899](https://pubmed.ncbi.nlm.nih.gov/20847899/)).

Functionally, SUMO-PCNA recruits the anti-recombinogenic helicase **Srs2** via its C-terminal SUMO-interacting motif, disrupting Rad51 filaments to prevent untimely homologous recombination and limiting crossovers by blocking extension of recombination intermediates ([PMID: 23395907](https://pubmed.ncbi.nlm.nih.gov/23395907/); [PMID: 22705796](https://pubmed.ncbi.nlm.nih.gov/22705796/)): "**cycling cells use the Siz1-dependent SUMOylation of PCNA to limit the extension of repair synthesis during template switch or HR and attenuate reciprocal DNA strand exchanges to maintain genome stability**" ([PMID: 23395907](https://pubmed.ncbi.nlm.nih.gov/23395907/)). Genetically, this Siz1–PCNA–Srs2 axis is distinct from the Ubc9/Mms21–Sgs1 pathway that resolves X-shaped cruciform structures at damaged forks: *siz1*, *srs2*, and PCNA-sumoylation mutants do **not** phenocopy *ubc9*/*mms21* ([PMID: 17081974](https://pubmed.ncbi.nlm.nih.gov/17081974/)). Siz1 therefore acts at replication forks through a defined, non-redundant signaling branch.

### 5. Siz1 drives the global SUMO stress response and sumoylates a chromatin/genome-maintenance network via its SAP DNA-binding domain

The **SUMO stress response (SSR)** — a rapid, large increase in SUMO conjugates upon environmental stress — is effected principally by Siz1 and reversed by the protease Ulp2: "**the SSR is effected primarily by the Siz1 E3 ligase and inactivated by the SUMO-specific protease Ulp2**," with targets concentrated in the transcription machinery (TFIID, Mediator, Pol II maturation factors, Tup1-Cyc8) ([PMID: 25434491](https://pubmed.ncbi.nlm.nih.gov/25434491/)). Siz1's **SAP domain binds duplex DNA**, scaffolding E3 and substrate on chromatin; for the paralog Siz2, 3′ ssDNA overhangs stimulate RPA sumoylation — "**The SAP domain of Siz2 binds DNA duplexes and makes a key contribution to this process**" ([PMID: 34585421](https://pubmed.ncbi.nlm.nih.gov/34585421/)) — a mechanism directly relevant to the conserved SAP domain of Siz1.

Beyond transcription, Siz1 (redundantly with Siz2) sumoylates an extensive genome-maintenance and mitotic substrate network: the centromeric histone variant **Cse4** (regulating its proteolysis and preventing mislocalization; [PMID: 29432128](https://pubmed.ncbi.nlm.nih.gov/29432128/)); the shugoshin **Sgo1** and chromosomal-passenger subunit **Bir1** to stabilize kinetochore biorientation — "**The Siz1/Siz2 SUMO ligases modify the pericentromere-localized shugoshin (Sgo1) protein before its tension-dependent release from chromatin**" ([PMID: 33929514](https://pubmed.ncbi.nlm.nih.gov/33929514/)); the Holliday-junction resolvase **Yen1** ([PMID: 30479332](https://pubmed.ncbi.nlm.nih.gov/30479332/)); the nuclease **Exo1** ([PMID: 26083678](https://pubmed.ncbi.nlm.nih.gov/26083678/)); and topoisomerase DNA–protein crosslinks routed to Slx5–Slx8 (STUbL)/proteasome degradation — "**This pathway is conserved in yeast with Siz1 and Slx5-Slx8, the orthologs of human PIAS4 and RNF4**" ([PMID: 33188014](https://pubmed.ncbi.nlm.nih.gov/33188014/)).

### 6. Crystal structure defines the tripartite PINIT–SP-RING–SP-CTD architecture; PINIT enables non-consensus PCNA-K164 modification

The X-ray structure of an active Siz1 ligase by Yunus & Lima revealed "**an elongated tripartite architecture comprised of an N-terminal PINIT domain, a central zinc-containing RING-like SP-RING domain, and a C-terminal domain we term the SP-CTD**" ([PMID: 19748360](https://pubmed.ncbi.nlm.nih.gov/19748360/)). Structure-guided mutagenesis cleanly separated two catalytic contributions: "**the SP-RING and SP-CTD are required for activation of the E2 approximately SUMO thioester, while the PINIT domain is essential for redirecting SUMO conjugation to … PCNA at lysine 164, a nonconsensus lysine residue that is not modified by the SUMO E2 in the absence of Siz1**" ([PMID: 19748360](https://pubmed.ncbi.nlm.nih.gov/19748360/)).

A later trapped E3/E2~SUMO/substrate complex captured the activated ligation geometry directly, "**illustrating how an E3 can bypass E2 specificity to force-feed a substrate lysine into the E2 active site**" ([PMID: 27509863](https://pubmed.ncbi.nlm.nih.gov/27509863/); methodology in [PMID: 30242710](https://pubmed.ncbi.nlm.nih.gov/30242710/)). Together these structures provide the physical basis for Siz1's dual role: a generic RING-type thioester-activation function plus a substrate-redirection function unique to the Siz/PIAS family.

### 7. Siz1 builds poly-SUMO chains and is itself regulated by phosphorylation, Rsp5 ubiquitylation, and STUbL degradation

Siz-type ligases catalyze not only mono-SUMOylation but **poly-Smt3 chain** formation via Smt3 Lys15. Takahashi et al. showed that SUMO/Smt3 forms polymeric chains dependent on Smt3 Lys15, and that substituting this lysine with arginine abolishes chain polymerization ([PMID: 12761287](https://pubmed.ncbi.nlm.nih.gov/12761287/)). These poly-SUMO signals are the recognition marks for SUMO-targeted ubiquitin ligases (STUbLs), coupling Siz1 output to downstream proteolysis.

Siz1 activity is reciprocally regulated. The HECT ubiquitin ligase **Rsp5** ubiquitylates Siz1 (reducing its SUMO-ligase activity), while Siz1 sumoylates Rsp5 (reducing its ubiquitin-ligase activity): "**Rsp5p SUMOylation is mediated by the SUMO ligases Siz1p and Siz2p … that are, in turn, substrates for Rsp5p-mediated ubiquitylation**" ([PMID: 23443663](https://pubmed.ncbi.nlm.nih.gov/23443663/)). The **nuclear pool** of Siz1 is a substrate of the **Slx5/Slx8 STUbL**: Siz1 is ubiquitinated in vivo and degraded in an Slx5-dependent manner when its nuclear egress is prevented in mitosis, accumulating as phosphorylated and sumoylated adducts in *slx5* cells ([PMID: 24196836](https://pubmed.ncbi.nlm.nih.gov/24196836/)). Siz1 is further phosphorylated by Polo-like kinase **Cdc5** at the prophase I–metaphase I transition in meiosis ([PMID: 42284145](https://pubmed.ncbi.nlm.nih.gov/42284145/)).

### 8. Siz1/Siz2-dependent polySUMOylation of Ecm11 drives synaptonemal-complex assembly in meiosis

In meiotic prophase I, Siz1 and Siz2 sumoylate the synaptonemal-complex (SC) central-region protein **Ecm11**, and this modification is essential for SC assembly. Cdc5 phosphorylation and NPC-tethered Ulp1 remodel SUMO homeostasis at the prophase I–metaphase I transition: "**Polo-like kinase Cdc5 remodels SUMO homeostasis … triggering partial Ulp1 release from the NPC and phosphorylating the SUMO ligases Siz1 and Siz2**" ([PMID: 42284145](https://pubmed.ncbi.nlm.nih.gov/42284145/)). Ecm11 is sumoylated in a Gmc2-dependent manner, and this is required for proper polymerization of the transverse-filament protein Zip1 while suppressing off-chromosome polycomplex formation: "**in the unSUMOylatable ecm11 mutant, assembly of chromosomal Zip1 remained compromised while polycomplex formation became frequent**" ([PMID: 23326245](https://pubmed.ncbi.nlm.nih.gov/23326245/)). The extent of modification quantitatively tunes assembly: "**efficiency of TF polymerization closely correlates with the extent of SUMO conjugation to Ecm11**," defining a **polySUMOylation-driven positive-feedback loop** (Zip1 N-terminus + Gmc2 activate Ecm11 polySUMOylation) ([PMID: 26598615](https://pubmed.ncbi.nlm.nih.gov/26598615/)).

### 9. Siz1's E3 contribution: acceleration plus non-consensus/spatially-restricted targeting beyond Ubc9 alone

A subtlety peculiar to SUMO (versus ubiquitin) is that the E2, **Ubc9, can by itself recognize the ΨKxE consensus** and modify canonical substrates. The consensus is the major determinant of E2 engagement: "**the SUMO-1-CS is a major determinant of Ubc9 binding and SUMO-1 modification. Mutating residues in the SUMO-1-CS abolishes both Ubc9 binding and substrate modification**" ([PMID: 11259410](https://pubmed.ncbi.nlm.nih.gov/11259410/)), and the Ubc9–RanGAP1 co-crystal shows "**the SUMO E2 enzyme Ubc9 is sufficient for substrate recognition and lysine modification of known SUMO targets**" ([PMID: 11853669](https://pubmed.ncbi.nlm.nih.gov/11853669/)).

Against this baseline, Siz1's E3 function is **two-fold**: (i) it **greatly accelerates** conjugation (strong in-vitro stimulation of septin sumoylation; [PMID: 11572779](https://pubmed.ncbi.nlm.nih.gov/11572779/)), and (ii) via PINIT it **redirects SUMO onto non-consensus lysines** that Ubc9 cannot modify alone, exemplified by PCNA Lys164 ([PMID: 19748360](https://pubmed.ncbi.nlm.nih.gov/19748360/)). In vivo, specificity is dominated by **spatial/local-concentration effects** rather than direct sequence readout ([PMID: 17077124](https://pubmed.ncbi.nlm.nih.gov/17077124/)). This frames the precise answer to "what does Siz1 do that Ubc9 does not": it provides speed, non-consensus reach, and spatial targeting.

---

## Mechanistic Model / Interpretation

### The catalytic cycle

```
   Smt3 (SUMO)                         ATP
      │                                 │
      ▼                                 ▼
 [ E1: Aos1–Uba2 ] ── activates ──► Smt3~E1 thioester
      │
      ▼  trans-thioesterification
 [ E2: Ubc9 ] ──────────────────► Ubc9~Smt3 thioester
      │                                 ▲
      │        Siz1 SP-RING/SP-CTD bind & ACTIVATE the charged E2
      ▼                                 │
 ┌──────────────────────────── Siz1 (E3) ───────────────────────────┐
 │  SAP ── PINIT ─────────── SP-RING(Zn) ─────────── SP-CTD          │
 │  │        │                   │                      │            │
 │  DNA     positions         activates             co-activates     │
 │  binding substrate K       E2~Smt3 thioester     thioester        │
 └───────────────────────────────┬──────────────────────────────────┘
                                  ▼
                 Substrate–Lys ─ε─NH₂  attacks thioester
                                  ▼
          Substrate–Lys–(isopeptide)–Gly-Smt3   (+ poly-Smt3 via Smt3-K15)
```

Siz1 does not form a covalent SUMO intermediate itself (unlike HECT ubiquitin ligases). As a RING-class enzyme it is a **catalytic scaffold**: the SP-RING/SP-CTD clamp and orient the Ubc9~Smt3 thioester into a closed, attack-competent conformation, while the PINIT domain grips the substrate and "force-feeds" the target lysine into the Ubc9 active site. The SAP domain anchors the complex on DNA for chromatin substrates. Poly-SUMO chains are built through Smt3 Lys15.

### Specificity logic — "location, location, location"

| Determinant | Mechanism | Evidence |
|---|---|---|
| ΨKxE consensus | Read directly by **Ubc9** (E2); E3-independent | [PMID: 11259410](https://pubmed.ncbi.nlm.nih.gov/11259410/); [PMID: 11853669](https://pubmed.ncbi.nlm.nih.gov/11853669/) |
| Non-consensus lysine (e.g., PCNA-K164) | **PINIT** domain redirects SUMO; Ubc9 alone cannot | [PMID: 19748360](https://pubmed.ncbi.nlm.nih.gov/19748360/) |
| Substrate class (PCNA/Prp45 vs septins) | Different Siz1 domains (PINIT vs C-terminus) | [PMID: 17077124](https://pubmed.ncbi.nlm.nih.gov/17077124/) |
| In-vivo target set | **Local E3 concentration**, not direct contact | [PMID: 17077124](https://pubmed.ncbi.nlm.nih.gov/17077124/) |
| Compartment | Karyopherin-controlled nuclear↔bud-neck shuttling | [PMID: 17403926](https://pubmed.ncbi.nlm.nih.gov/17403926/) |

### Spatial and cell-cycle map

| Compartment / Phase | Siz1 action | Key substrates | Downstream consequence |
|---|---|---|---|
| Nucleus, S phase | PCNA-K164 sumoylation | PCNA | Srs2 recruitment → anti-recombination at forks |
| Nucleus, stress | SUMO stress response | TFIID, Mediator, Pol II factors, Tup1-Cyc8 | Transcriptional reprogramming (reversed by Ulp2) |
| Nucleus / chromatin | Genome-maintenance network | Cse4, Sgo1, Bir1, Yen1, Exo1, RPA, Top-DPCs | Kinetochore biorientation; crossover control; STUbL-coupled turnover |
| Cytoplasm / bud neck, M phase | Septin ring sumoylation | Cdc3, Cdc11, Shs1/Sep7 | Septin ring dynamics |
| Nucleus, meiotic prophase I | Ecm11 polySUMOylation | Ecm11 (with Gmc2) | Synaptonemal-complex / Zip1 assembly |

### Regulatory integration

Siz1 sits in a dense post-translational network. It **writes** SUMO (and poly-SUMO) marks; those marks are **read/erased** by STUbLs (Slx5-Slx8) and isopeptidases (Ulp1 at the NPC, Ulp2 for the stress response). Siz1 is itself **regulated**: phosphorylated (Cdc5), ubiquitylated by Rsp5 (down-regulating its activity) in reciprocal crosstalk, and degraded as a nuclear pool by the Slx5-Slx8 STUbL when its mitotic export is blocked. The net effect is a tightly compartmentalized, cell-cycle-gated SUMO-writing machine.

---

## Evidence Base

| PMID | Study (abbrev.) | Contribution |
|---|---|---|
| [11572779](https://pubmed.ncbi.nlm.nih.gov/11572779/) | Johnson & Gupta 2001 | Siz1 required for septin SUMO; with Siz2 does most sumoylation; E3-like stimulation in vitro |
| [11587849](https://pubmed.ncbi.nlm.nih.gov/11587849/) | Takahashi et al. 2001 | Identifies Siz1=YDR409w; PIAS/RING family; essential conserved Cys; M-phase bud-neck localization |
| [16109721](https://pubmed.ncbi.nlm.nih.gov/16109721/) | Takahashi & Kikuchi 2005 | PINIT + SP-RING required for ligase activity and Smt3 binding; SAP/N-term nuclear, C-term bud-neck |
| [17077124](https://pubmed.ncbi.nlm.nih.gov/17077124/) | Reindle et al. 2006 | Domain-mapped substrate selection; local-concentration model of specificity |
| [23935535](https://pubmed.ncbi.nlm.nih.gov/23935535/) | Albuquerque et al. 2013 | Proteome-wide: Siz1/Siz2 redundantly control most sumoylated substrates |
| [17403926](https://pubmed.ncbi.nlm.nih.gov/17403926/) | Makhnevych et al. 2007 | Karyopherin-controlled (Kap95 in / Msn5 out) cell-cycle trafficking to septin ring |
| [18583943](https://pubmed.ncbi.nlm.nih.gov/18583943/) | Takahashi et al. 2008 | Cytoplasmic (bud-neck) sumoylation; transport coupling of Siz1 and Ulp1 |
| [27509863](https://pubmed.ncbi.nlm.nih.gov/27509863/) | Streich & Lima 2016 | Activated E3/E2~SUMO/substrate structure; strict Siz1-dependence of PCNA-K164; "force-feed" mechanism |
| [20847899](https://pubmed.ncbi.nlm.nih.gov/20847899/) | PCNA PTM review | Siz1 ligates PCNA in S phase and upon fork stalling |
| [23395907](https://pubmed.ncbi.nlm.nih.gov/23395907/) | Burkovics et al. 2013 | Siz1-PCNA-SUMO limits repair synthesis / crossovers (Srs2) |
| [22705796](https://pubmed.ncbi.nlm.nih.gov/22705796/) | Kolesar et al. 2012 | Srs2 SIM reads SUMO-PCNA; Siz-facilitated Srs2 sumoylation |
| [17081974](https://pubmed.ncbi.nlm.nih.gov/17081974/) | Branzei et al. 2006 | siz1/PCNA mutants ≠ ubc9/mms21; separates Siz1-PCNA-Srs2 from Mms21-Sgs1 pathway |
| [25434491](https://pubmed.ncbi.nlm.nih.gov/25434491/) | Lewicki et al. 2015 | Siz1 drives SUMO stress response (transcription machinery); Ulp2 reverses |
| [34585421](https://pubmed.ncbi.nlm.nih.gov/34585421/) | Cappadocia et al. 2021 | Siz SAP domain binds DNA; DNA asymmetry stimulates RPA sumoylation |
| [29432128](https://pubmed.ncbi.nlm.nih.gov/29432128/) | Ohkuni et al. 2018 | Siz1/Siz2 major ligases for Cse4; regulates its proteolysis |
| [33929514](https://pubmed.ncbi.nlm.nih.gov/33929514/) | Su et al. 2021 | Siz1/Siz2 sumoylate Sgo1/Bir1; stabilize kinetochore biorientation |
| [30479332](https://pubmed.ncbi.nlm.nih.gov/30479332/) | Talhaoui et al. 2018 | Siz1/Siz2 sumoylate Yen1; Slx5-Slx8 limits crossovers |
| [26083678](https://pubmed.ncbi.nlm.nih.gov/26083678/) | Bologna et al. 2015 | Yeast Ubc9-Siz1/Siz2 sumoylate Exo1 (reconstituted); regulates stability |
| [33188014](https://pubmed.ncbi.nlm.nih.gov/33188014/) | Sun et al. 2020 | Siz1 + Slx5-Slx8 (PIAS4/RNF4 orthologs) resolve Top-DPCs |
| [19748360](https://pubmed.ncbi.nlm.nih.gov/19748360/) | Yunus & Lima 2009 | Crystal structure: PINIT–SP-RING–SP-CTD; PINIT enables PCNA-K164 |
| [30242710](https://pubmed.ncbi.nlm.nih.gov/30242710/) | Streich & Lima 2018 (methods) | Strategy to trap E3-mediated Ubl ligation intermediates |
| [12761287](https://pubmed.ncbi.nlm.nih.gov/12761287/) | Takahashi et al. 2003 | Siz-type reactions build Smt3 poly-chains via Smt3-K15 |
| [23443663](https://pubmed.ncbi.nlm.nih.gov/23443663/) | Novoselova et al. 2013 | Reciprocal Siz1–Rsp5 SUMO/ubiquitin crosstalk |
| [24196836](https://pubmed.ncbi.nlm.nih.gov/24196836/) | Westerbeck et al. 2014 | Slx5-Slx8 STUbL ubiquitylates/degrades nuclear Siz1 pool |
| [42284145](https://pubmed.ncbi.nlm.nih.gov/42284145/) | Wettstein et al. 2026 | Cdc5 phosphorylates Siz1/Siz2; NPC Ulp1 docking governs meiotic SUMO homeostasis |
| [23326245](https://pubmed.ncbi.nlm.nih.gov/23326245/) | Humphryes et al. 2013 | Ecm11 sumoylation required for Zip1/SC assembly |
| [26598615](https://pubmed.ncbi.nlm.nih.gov/26598615/) | Leung et al. 2015 | PolySUMOylation feedback assembles the SC |
| [11259410](https://pubmed.ncbi.nlm.nih.gov/11259410/) | Sampson et al. 2001 | ΨKxE consensus read directly by Ubc9 |
| [11853669](https://pubmed.ncbi.nlm.nih.gov/11853669/) | Bernier-Villamor et al. 2002 | Ubc9–RanGAP1 structure: E2 sufficient for consensus substrates |

**Convergence of evidence.** The core claims rest on *precise, low-throughput* data: biochemical reconstitution ([PMID: 11572779](https://pubmed.ncbi.nlm.nih.gov/11572779/)), crystallography ([PMID: 19748360](https://pubmed.ncbi.nlm.nih.gov/19748360/); [PMID: 27509863](https://pubmed.ncbi.nlm.nih.gov/27509863/)), domain-swap genetics ([PMID: 17077124](https://pubmed.ncbi.nlm.nih.gov/17077124/)), and targeted cell biology ([PMID: 17403926](https://pubmed.ncbi.nlm.nih.gov/17403926/)), with genome-wide proteomics ([PMID: 23935535](https://pubmed.ncbi.nlm.nih.gov/23935535/); [PMID: 25434491](https://pubmed.ncbi.nlm.nih.gov/25434491/)) supplying breadth rather than the primary claims. No reviewed study contradicts the central annotation of Siz1 as the SP-RING SUMO E3 ligase.

---

## Limitations and Knowledge Gaps

1. **Siz1/Siz2 redundancy.** Many "Siz1" substrates (Cse4, Sgo1, Yen1, Exo1, Ecm11) are modified redundantly by Siz1 **and** Siz2, so single-gene attribution is often imprecise. Where a substrate is *strictly* Siz1-dependent — notably **PCNA-K164** — the assignment is strong; for redundant substrates the specific Siz1 contribution is harder to isolate.

2. **Cross-species name collision.** Plant SIZ1 (Arabidopsis/tomato/maize) and human PIAS family members share the name/architecture but have an added PHD finger and distinct physiology; care is needed not to import their phenotypes into the yeast annotation. This report has excluded plant studies from the yeast claims.

3. **In-vitro vs in-vivo mechanism.** The "force-feed"/PINIT-redirection model is well supported by structures and reconstitution, but the quantitative kinetic contribution of the E3 for each in-vivo substrate (rate enhancement, processivity, chain-length control) is not comprehensively measured.

4. **Poly-SUMO chain control.** How Siz1 decides between mono- and poly-SUMOylation on a given substrate, and how chain length is tuned to STUbL recognition thresholds, remains mechanistically open.

5. **Regulation stoichiometry.** The physiological magnitude and timing of Siz1 regulation by Cdc5 phosphorylation and Rsp5 ubiquitylation — and how these integrate to switch Siz1 between compartments/substrate programs — are only partially mapped.

6. **Citation-match caveat.** During verification, the poly-chain quote from [PMID: 12761287](https://pubmed.ncbi.nlm.nih.gov/12761287/) and the Slx5-degradation quote from [PMID: 24196836](https://pubmed.ncbi.nlm.nih.gov/24196836/) were flagged as approximate paraphrases rather than exact matches; the underlying conclusions are nonetheless well supported by those papers' findings and are stated here as paraphrase.

---

## Proposed Follow-up Experiments / Actions

1. **Separation-of-function alleles in vivo.** Combine PINIT-, SP-RING-, SP-CTD-, and SAP-point mutants (from the crystal structure, [PMID: 19748360](https://pubmed.ncbi.nlm.nih.gov/19748360/)) in a *siz1Δ siz2Δ* background and measure substrate-resolved sumoylation (PCNA-K164 vs septins vs Ecm11) to quantify each domain's in-vivo contribution.

2. **Single-molecule / kinetic dissection.** Use reconstituted Ubc9~Smt3 + Siz1 + defined substrate to measure the rate enhancement and chain-length distribution Siz1 confers, discriminating acceleration from non-consensus redirection quantitatively.

3. **Compartment-locking.** Engineer karyopherin-binding mutants (Kap95/Msn5 sites) to trap Siz1 in the nucleus or at the bud neck and assay the consequences for PCNA vs septin sumoylation, directly testing the local-concentration model ([PMID: 17403926](https://pubmed.ncbi.nlm.nih.gov/17403926/); [PMID: 17077124](https://pubmed.ncbi.nlm.nih.gov/17077124/)).

4. **Phospho-regulation map.** Identify Cdc5 phosphosites on Siz1 ([PMID: 42284145](https://pubmed.ncbi.nlm.nih.gov/42284145/)) and build phospho-dead/phospho-mimetic alleles to test control of meiotic Ecm11 polySUMOylation and SC assembly.

5. **Chain-length → STUbL coupling.** Vary Smt3-K15 and Siz1 dosage to modulate poly-SUMO chain length on a model substrate and measure the threshold for Slx5-Slx8 recognition and proteasomal turnover ([PMID: 12761287](https://pubmed.ncbi.nlm.nih.gov/12761287/); [PMID: 33188014](https://pubmed.ncbi.nlm.nih.gov/33188014/)).

6. **Strict-dependence census.** Systematically test which of the redundant Siz1/Siz2 substrates have any *strictly* Siz1-dependent modification site (as PCNA-K164 does), to refine single-gene functional annotation.

---

## Conclusion

*SIZ1* (Q04195 / YDR409W) encodes the founding budding-yeast member of the Siz/PIAS family of **SP-RING SUMO (Smt3) E3 ligases (EC 2.3.2.-)**. Its primary molecular function is to catalyze the substrate-directing step of SUMO conjugation: as a tripartite PINIT–SP-RING–SP-CTD scaffold (plus a DNA-binding SAP domain), it binds the SUMO-charged E2 Ubc9, activates the thioester, and force-feeds a substrate lysine into the active site, accelerating conjugation and extending it to non-consensus lysines (e.g., PCNA-K164) that Ubc9 cannot modify alone. With its paralog Siz2 it performs most cellular sumoylation, selecting targets chiefly by spatial concentration. It acts in two compartments under cell-cycle/karyopherin control — the nucleus (PCNA/Srs2 at replication forks; transcription, kinetochore, meiotic SC, and stress-response substrates) and the cytoplasmic bud neck (septins) — and is itself regulated by phosphorylation, Rsp5 ubiquitin crosstalk, and STUbL-dependent degradation of its nuclear pool.


## Artifacts

- [OpenScientist final report](SIZ1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SIZ1-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:30657769
2. PMID:33710720
3. PMID:31925312
4. PMID:11572779
5. PMID:11587849
6. PMID:16109721
7. PMID:27509863
8. PMID:17077124
9. PMID:23935535
10. PMID:17403926
11. PMID:18583943
12. PMID:20847899
13. PMID:23395907
14. PMID:22705796
15. PMID:17081974
16. PMID:25434491
17. PMID:34585421
18. PMID:29432128
19. PMID:33929514
20. PMID:30479332
21. PMID:26083678
22. PMID:33188014
23. PMID:19748360
24. PMID:30242710
25. PMID:12761287
26. PMID:23443663
27. PMID:24196836
28. PMID:42284145
29. PMID:23326245
30. PMID:26598615
31. PMID:11259410
32. PMID:11853669