---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:37:33.726462'
end_time: '2026-09-01T03:52:31.413183'
duration_seconds: 4497.69
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mlaE
  gene_symbol: mlaE
  uniprot_accession: Q88P93
  protein_description: 'RecName: Full=Intermembrane phospholipid transport system
    permease protein MlaE {ECO:0000256|ARBA:ARBA00020857};'
  gene_info: Name=mlaE {ECO:0000313|EMBL:AAN66584.1}; OrderedLocusNames=PP_0959 {ECO:0000313|EMBL:AAN66584.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MlaE permease family.
  protein_domains: ABC_MlaE_roteobac. (IPR003453); MlaE_Permease. (IPR053408); Permease_MalE.
    (IPR030802); MlaE (PF02405)
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
citation_count: 8
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mlaE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mlaE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88P93
- **Protein Description:** RecName: Full=Intermembrane phospholipid transport system permease protein MlaE {ECO:0000256|ARBA:ARBA00020857};
- **Gene Information:** Name=mlaE {ECO:0000313|EMBL:AAN66584.1}; OrderedLocusNames=PP_0959 {ECO:0000313|EMBL:AAN66584.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MlaE permease family.
- **Key Domains:** ABC_MlaE_roteobac. (IPR003453); MlaE_Permease. (IPR053408); Permease_MalE. (IPR030802); MlaE (PF02405)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mlaE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mlaE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mlaE** (gene ID: mlaE, UniProt: Q88P93) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: MlaE (Q88P93 / PP_0959) in *Pseudomonas putida* KT2440

## Summary

**MlaE (UniProt Q88P93; ordered locus PP_0959) is the integral inner-membrane permease subunit of the MlaFEDB ABC transporter, the inner-membrane core of the Mla (Maintenance of Lipid Asymmetry) system of *Pseudomonas putida* KT2440.** It is a polytopic membrane protein that forms the transmembrane translocation channel and harbors the glycerophospholipid substrate-binding site of the complex. In functional terms, MlaE is a **lipid (glycerophospholipid) translocase/permease**: it moves phospholipid across the inner membrane, coupling the movement to ATP binding and hydrolysis carried out by the cytoplasmic ATPase subunit MlaF. Its "substrate" is not a small metabolite or ion but bulk **glycerophospholipid (GPL)**, and its "reaction" is vectorial transport across the lipid bilayer rather than a chemical transformation.

At the pathway level, MlaE operates as part of a multi-compartment transport system that spans the entire Gram-negative cell envelope. The Mla system removes phospholipids that become mislocalized to the outer leaflet of the outer membrane (OM) and returns them, via the periplasmic shuttle protein MlaC and the OM MlaA–OmpC/F complex, to the inner membrane (IM) where MlaFEDB resides. This **retrograde (OM → IM) trafficking** preserves the characteristic lipid asymmetry of the OM — lipopolysaccharide (LPS) in the outer leaflet, phospholipids in the inner leaflet — which is essential for the OM's function as a permeability barrier against antibiotics and other noxious compounds.

The functional assignment for *P. putida* MlaE is made with high confidence by strong structural, evolutionary, and bioinformatic conservation with experimentally characterized orthologs. High-resolution cryo-EM structures of MlaFEDB from *Escherichia coli* and from the close relative *Pseudomonas aeruginosa* directly demonstrate MlaE's role as the transmembrane component and reveal a continuous phospholipid-transport pathway passing through MlaE. The *P. putida* protein is a 266-residue, 5-transmembrane-helix inner-membrane protein assigned by UniProt to the MlaE permease family, with domain signatures (PF02405 MlaE; IPR003453; IPR053408; IPR030802) that are diagnostic of this transporter family. No *P. putida*-specific experimental study of MlaE was identified; the annotation is therefore an evidence-supported inference from orthologs, which is the standard and appropriate basis for functional annotation of this well-conserved protein.

---

## Gene / Protein Identity Verification

Before presenting the functional findings, the target identity was verified against the UniProt-provided context, as mandated:

| Attribute | Target (from UniProt) | Literature/analysis match |
|---|---|---|
| Gene symbol | *mlaE* | ✅ Consistent — "mlaE" is the standard symbol for the MlaFEDB permease subunit across Gram-negative bacteria |
| UniProt accession | Q88P93 | ✅ |
| Ordered locus | PP_0959 | ✅ *P. putida* KT2440 locus tag |
| Organism | *Pseudomonas putida* KT2440 | ✅ Structural work exists for the close relative *P. aeruginosa* (PMID 33845086) |
| Protein family | MlaE permease family | ✅ Matches all literature describing MlaE as the transmembrane permease of MlaFEDB |
| Key domains | PF02405 (MlaE); IPR003453; IPR053408; IPR030802 | ✅ Diagnostic of the MlaE permease family |

**Conclusion of verification:** The gene symbol, organism, family, and domain architecture are mutually consistent and unambiguously identify Q88P93 as the MlaE permease of the Mla system. There is no evidence of symbol ambiguity that would confound the annotation. The one caveat is that all mechanistic experiments were performed on orthologs (*E. coli*, *P. aeruginosa*), not on the *P. putida* protein itself — this is addressed throughout as an inference from conserved structure and sequence.

---

## Key Findings

### Finding 1 — MlaE is the integral-membrane permease subunit of the MlaFEDB ABC transporter that translocates phospholipids

MlaE is the transmembrane (permease) component of the inner-membrane ABC transporter complex MlaFEDB. This is the central, defining functional assignment of the protein. In the canonical architecture of ABC transporters, transport activity is distributed across dedicated subunits: nucleotide-binding domains (NBDs) hydrolyze ATP in the cytoplasm, while transmembrane domains (TMDs) form the substrate-conducting pathway across the membrane. In MlaFEDB, **MlaE is the transmembrane domain / permease**, MlaF is the ATP-hydrolyzing NBD, MlaB is a regulatory STAS-domain subunit, and MlaD is a periplasmic/membrane-anchored substrate-binding subunit.

The most direct evidence comes from the 3.05 Å cryo-EM structure of *E. coli* MlaFEDB with substrate bound (Coudray et al. 2020). This structure resolved two phospholipid molecules within the complex and traced **a continuous transport pathway that extends from the MlaE substrate-binding site, through the channel of MlaD, and into the periplasm** ([PMID: 33236984](https://pubmed.ncbi.nlm.nih.gov/33236984/)). The same study noted that **"the transmembrane subunit, MlaE, has minimal sequence similarity to other transporters"** — a feature that later led to MlaFEDB being recognized as the founding member of a structurally distinct ABC transporter superfamily. The overall complex assembles with a stoichiometry of MlaF₂E₂D₆B₂ (i.e., two copies each of MlaF, MlaE, MlaB, and six copies of MlaD) (Ekiert/Coudray/Bhabha 2022, [PMID: 35981415](https://pubmed.ncbi.nlm.nih.gov/35981415/)).

The functional significance for *P. putida* MlaE is that this protein provides the physical channel through which phospholipid crosses the inner membrane. It does not chemically modify its substrate; rather, it acts as a gated conduit whose conformation is driven by the ATPase cycle of the associated MlaF subunits.

### Finding 2 — The Mla system maintains outer-membrane lipid asymmetry via retrograde phospholipid transport

The biological process in which MlaE participates is the **maintenance of outer-membrane lipid asymmetry**. The Mla pathway was first defined genetically in *E. coli* by Malinverni & Silhavy (2009), who identified a **"highly conserved pathway ... composed of at least 6 proteins [that] contains at least 1 component in each cellular compartment"** and named it Mla for its role in preserving OM lipid asymmetry ([PMID: 19383799](https://pubmed.ncbi.nlm.nih.gov/19383799/)). The six-component system comprises the OM lipoprotein MlaA in complex with porins OmpC/F, the periplasmic shuttle protein MlaC, and the inner-membrane ABC transporter MlaFEDB (which contains MlaE).

The direction of transport is **retrograde** — from the OM back to the IM. As reviewed by Low & Chng (2021), **"the OmpC-Mla ... system ... mediates the retrograde transport of phospholipids from the outer leaflet of the OM to the inner membrane"** ([PMID: 34753108](https://pubmed.ncbi.nlm.nih.gov/34753108/)). Although the transport directionality was historically debated (some groups proposed anterograde IM→OM transport), recent biochemical studies strongly support the retrograde model (Abellón-Ruiz 2023, [PMID: 36459067](https://pubmed.ncbi.nlm.nih.gov/36459067/)). Under either interpretation, MlaE remains the inner-membrane permease that moves phospholipid across the IM; the debate concerns net physiological directionality, not MlaE's molecular role.

This process matters physiologically because the asymmetric OM — with LPS confined to the outer leaflet and phospholipids to the inner leaflet — is what makes the Gram-negative OM an effective barrier against detergents, bile salts, and many antibiotics. When phospholipids accumulate in the OM outer leaflet, permeability increases and cell survival is compromised. The Mla system corrects this by extracting the mislocalized phospholipids and returning them across the envelope.

### Finding 3 — MlaE localizes to the inner (cytoplasmic) membrane, and its function is structurally conserved in *Pseudomonas*

MlaE carries out its function embedded in the **inner (cytoplasmic) membrane**. MlaFEDB is repeatedly described as an inner-membrane ABC transporter complex; Ekiert et al. (2022) state that **"at the heart of the Mla pathway is a structurally unique ABC transporter complex in the inner membrane, called MlaFEDB"** ([PMID: 35981415](https://pubmed.ncbi.nlm.nih.gov/35981415/)). The cytoplasmic ATPase (MlaF) and regulatory (MlaB) subunits face the cytoplasm; the MlaE transmembrane helices span the IM; and MlaD projects into the periplasm to hand off/receive lipid from the periplasmic shuttle MlaC.

Critically for the *P. putida* annotation, the transporter has been structurally characterized in the close relative *Pseudomonas aeruginosa*. Zhou et al. (2021) reported **"cryo-EM structures of the ATP-binding cassette (ABC) transporter MlaFEBD from P. a[e]ruginosa, the core complex in the Mla pathway,"** in apo, ADP, and ATP-bound states at 3.4–3.9 Å ([PMID: 33845086](https://pubmed.ncbi.nlm.nih.gov/33845086/)). These structures confirm that the *Pseudomonas* complex adopts the same ~12-molecule architecture and phospholipid-transport function seen in *E. coli*. Complementary *E. coli* structures bound to phospholipid, ADP, and AMP-PNP define the ATP-dependent transport cycle and identify functional residues (Tang et al. 2020, [PMID: 33199922](https://pubmed.ncbi.nlm.nih.gov/33199922/)). Because *P. putida* and *P. aeruginosa* are congeners with highly conserved Mla operons, the *P. aeruginosa* structural data provide strong, genus-level support for the function and localization of *P. putida* MlaE.

### Finding 4 — *P. putida* MlaE (266 aa) is a polytopic inner-membrane protein with 5 predicted transmembrane helices

Direct sequence-level evidence for the *P. putida* protein comes from UniProt Q88P93, which annotates a **266-residue protein** with **five predicted helical transmembrane segments** (approximately residues 21–42, 54–77, 153–173, 204–223, and 244–263), a subcellular location of **"Cell inner membrane,"** and assignment to the **MlaE permease family**. The UniProt functional annotation states that the protein is **"Part of the ABC transporter complex MlaFEDB ... Probably responsible for the translocation of the substrate across the membrane,"** and the subunit annotation records the stoichiometry of two MlaF, two MlaE, two MlaB, and six MlaD.

This membrane topology — a compact polytopic protein with ~5 TM helices — is fully consistent with a permease/translocase role and matches the topology of MlaE orthologs whose structures have been solved. The domain complement (PF02405 MlaE; IPR003453 ABC_MlaE_proteobac; IPR053408 MlaE_Permease; IPR030802 Permease_MalE) is diagnostic of the MlaE permease family, reinforcing the functional assignment independently of the structural homology argument.

### Finding 5 — The transported substrate is glycerophospholipid mislocalized to the OM outer leaflet

The **substrate specificity** of the MlaE permease is **bulk glycerophospholipid (GPL)** — not LPS, not a small ion or metabolite. Kaur et al. (2024) state that OM asymmetry **"is maintained by the Mla system (MlaA-MlaBCDEF), which contributes to lipid homeostasis by removing mislocalized GPLs from the outer leaflet of the OM"** ([PMID: 39373473](https://pubmed.ncbi.nlm.nih.gov/39373473/)). This is corroborated structurally: the cryo-EM structures of MlaFEDB directly visualize bound phospholipid molecules seated within the MlaE/MlaD transport pathway (Coudray et al. 2020, [PMID: 33236984](https://pubmed.ncbi.nlm.nih.gov/33236984/)). Thus the cargo physically handled by the MlaE permease is a glycerophospholipid molecule, consistent with the "phospholipid transporter" designation of the complex. The system exhibits some substrate promiscuity across phospholipid species, consistent with its role in bulk lipid homeostasis rather than transport of a single defined lipid.

---

## Mechanistic Model / Interpretation

The findings converge on a coherent, well-supported mechanistic model in which MlaE is the membrane-embedded engine that moves phospholipid across the inner membrane within a trans-envelope relay.

### The Mla trans-envelope transport system

```
        OUTER MEMBRANE (asymmetric: LPS out / PL in)
   ┌───────────────────────────────────────────────────┐
   │   [ MlaA – OmpC/F ]   <-- extracts mislocalized PL  │
   └───────────────────────┬───────────────────────────┘
                           │  phospholipid
                           ▼
   PERIPLASM        ( MlaC )  <-- soluble lipid shuttle
                           │
                           ▼
   ┌───────────────────────────────────────────────────┐
   │        MlaD₆  (periplasmic ring / hand-off)         │
   │   ─────────────────────────────────────────────    │
   │        MlaE₂  ◄══ PERMEASE / translocation channel  │  INNER
   │                    + substrate-binding site         │  MEMBRANE
   │   ─────────────────────────────────────────────    │
   │        MlaF₂ (ATPase / NBD)   MlaB₂ (STAS reg.)     │
   └───────────────────────────────────────────────────┘
        CYTOPLASM  (ATP → ADP + Pi drives the cycle)

   Net direction: OM  ──retrograde──►  IM
   Stoichiometry: MlaF₂ E₂ D₆ B₂
```

### MlaE's specific role within the cycle

1. **Substrate reception.** A phospholipid mislocalized to the OM outer leaflet is extracted by the MlaA–OmpC/F complex and carried across the periplasm by the soluble shuttle MlaC. MlaC delivers the lipid to the MlaD₆ ring on the periplasmic face of MlaFEDB.
2. **Channel entry and binding.** The lipid enters a continuous pathway that runs from MlaD's central channel down into the **MlaE substrate-binding site** — the pathway directly resolved in the 3.05 Å structure (PMID 33236984). MlaE thus provides both the binding pocket and the transmembrane conduit.
3. **ATP-coupled translocation.** ATP binding and hydrolysis by the cytoplasmic MlaF NBDs drive conformational changes in the MlaE TMDs, translocating the phospholipid across the inner membrane. MlaB (a STAS-domain protein) modulates MlaF activity and complex stability.
4. **Delivery to the IM.** The phospholipid is deposited into the inner membrane, completing retrograde return and restoring OM asymmetry.

In this model MlaE is best described not as an enzyme in the classical (bond-breaking) sense but as a **primary active lipid transporter subunit** — the transmembrane "gate" of a lipid-handling ABC machine. Its catalytic partner is MlaF (the ATPase); its substrate-delivery partner is MlaD; its physiological cargo is glycerophospholipid.

### Why the annotation transfers confidently to *P. putida*

| Line of evidence | Source | Strength for *P. putida* |
|---|---|---|
| 266-aa, 5-TM, IM localization, MlaE family | UniProt Q88P93 | Direct (this protein) |
| Diagnostic domains PF02405 / IPR003453 / IPR053408 / IPR030802 | InterPro/Pfam | Direct (this protein) |
| MlaFEDB structure & function in *P. aeruginosa* (congener) | PMID 33845086 | Very strong (same genus) |
| Substrate = phospholipid, continuous MlaE pathway | PMID 33236984 | Strong (ortholog, mechanism) |
| Retrograde OM→IM process, 6-protein pathway | PMID 19383799; 34753108; 36459067 | Strong (pathway conservation) |
| Substrate = mislocalized GPL | PMID 39373473 | Strong (system-level) |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports / informs the annotation |
|---|---|---|
| [33236984](https://pubmed.ncbi.nlm.nih.gov/33236984/) | *Structure of bacterial phospholipid transporter MlaFEDB with substrate bound* | 3.05 Å cryo-EM; identifies MlaE as the transmembrane subunit with the substrate-binding site; traces the continuous lipid pathway MlaE→MlaD→periplasm; two phospholipids bound. Core mechanistic evidence. |
| [19383799](https://pubmed.ncbi.nlm.nih.gov/19383799/) | *An ABC transport system that maintains lipid asymmetry...* | Foundational genetics defining the 6-protein Mla pathway spanning all envelope compartments; establishes biological process. |
| [34753108](https://pubmed.ncbi.nlm.nih.gov/34753108/) | *Current mechanistic understanding of intermembrane lipid trafficking...* | Review stating the retrograde OM→IM direction of Mla-mediated phospholipid transport. |
| [36459067](https://pubmed.ncbi.nlm.nih.gov/36459067/) | *Forward or backward... phospholipid trafficking by the Mla system* | Reviews the directionality debate; concludes biochemistry supports retrograde transport; situates MlaFEDB in the IM. |
| [35981415](https://pubmed.ncbi.nlm.nih.gov/35981415/) | *Structure and mechanism of the bacterial lipid ABC transporter, MlaFEDB* | States MlaFEDB is a structurally unique IM ABC transporter; provides MlaF₂E₂D₆B₂ stoichiometry. |
| [33845086](https://pubmed.ncbi.nlm.nih.gov/33845086/) | *Structural Insight into Phospholipid Transport by the MlaFEBD Complex from P. aeruginosa* | Cryo-EM of the *Pseudomonas* complex (apo/ADP/ATP); genus-level structural confirmation directly relevant to *P. putida*. |
| [33199922](https://pubmed.ncbi.nlm.nih.gov/33199922/) | *Structural insights into OM asymmetry maintenance ... by MlaFEDB* | *E. coli* structures + transport assays defining ATP-dependent transport and functional residues; establishes transport direction via reconstituted system. |
| [39373473](https://pubmed.ncbi.nlm.nih.gov/39373473/) | *Insight into the outer membrane asymmetry of...* | Explicitly identifies glycerophospholipids (GPLs) as the mislocalized substrate removed by the Mla system. |
| [39080293](https://pubmed.ncbi.nlm.nih.gov/39080293/) | *Structure of the MlaC-MlaD complex...* | Defines periplasmic hand-off between MlaC shuttle and MlaD; contextualizes how lipid reaches the MlaE channel. |
| [37100290](https://pubmed.ncbi.nlm.nih.gov/37100290/) | *Protein-protein interactions in the Mla lipid transport system...* | Deep mutational scanning + AlphaFold mapping of Mla interfaces; supports shuttle mechanism feeding MlaFEDB. |
| [40169428](https://pubmed.ncbi.nlm.nih.gov/40169428/) | *Unveiling multiple copies of MlaC...* | Documents Mla operon variation across Proteobacteria and MlaC substrate promiscuity; informs conservation reasoning. |
| [41047745](https://pubmed.ncbi.nlm.nih.gov/41047745/) | *Distinctive Properties of Mla Proteins...* | Computational analysis of individual Mla components including MlaE (EQ loop, orientation); reinforces non-canonical ABC nature. |

**Consistency of the evidence:** All primary structural and genetic studies agree on the essential points — MlaE is the transmembrane permease of an inner-membrane ABC transporter that moves glycerophospholipid as part of the Mla asymmetry-maintenance pathway. The only genuine controversy in the literature (retrograde vs. anterograde net direction) does not affect the molecular role assigned to MlaE. No paper contradicts the core annotation.

---

## Limitations and Knowledge Gaps

1. **No *P. putida*-specific experimental data.** Every mechanistic and structural experiment cited was performed on orthologs — principally *E. coli*, with genus-level support from *P. aeruginosa*. The *P. putida* KT2440 MlaE (Q88P93) itself has not been the direct subject of a purified-protein, structural, or genetic study in the reviewed literature. The functional annotation is therefore an inference — a well-justified one, given strong sequence/structure conservation and the *P. aeruginosa* structures — but it remains an inference rather than a direct measurement.

2. **Transport directionality remains formally debated.** Although recent biochemistry favors retrograde (OM→IM) transport, an anterograde interpretation has been argued historically. This is a system-level question and does not change MlaE's identity as the IM permease, but it does leave the precise physiological net flux for *P. putida* unconfirmed.

3. **Substrate specificity granularity.** The substrate is established as bulk glycerophospholipid, and the system shows promiscuity across phospholipid species. Whether *P. putida* MlaE has any preference among phospholipid headgroups or acyl-chain compositions — potentially relevant given *P. putida*'s notable membrane remodeling during solvent stress — has not been determined.

4. **Physiological role in *P. putida* lifestyle.** *P. putida* is a soil bacterium renowned for solvent tolerance and membrane adaptation. Whether the Mla system contributes specifically to these traits (as opposed to general OM barrier maintenance) is unexplored for this organism.

5. **Predicted vs. experimentally verified topology.** The 5-TM topology and TM boundaries for Q88P93 are computational predictions from UniProt, not experimentally mapped for the *P. putida* protein.

---

## Proposed Follow-up Experiments / Actions

1. **Genetic confirmation in *P. putida* KT2440.** Construct a Δ*mlaE* (ΔPP_0959) deletion and assay for the hallmark Mla phenotypes: increased OM permeability (SDS/EDTA and bile-salt sensitivity), altered antibiotic susceptibility, and outer-membrane vesicle (blebbing) phenotypes. Complementation with plasmid-borne *mlaE* should restore wild-type behavior.

2. **Lipidomic asymmetry assay.** Use phospholipase-accessibility or lipidomic profiling of OM vs. IM fractions in wild-type vs. Δ*mlaE* to test whether phospholipids accumulate in the OM outer leaflet, directly confirming the retrograde asymmetry-maintenance function in *P. putida*.

3. **Reconstituted transport assay.** Purify *P. putida* MlaFEDB and reconstitute into proteoliposomes with MlaC and MlaA–OmpC/F (as done for *E. coli* in PMID 33199922) to measure ATP-dependent phospholipid transport and confirm directionality for the *Pseudomonas* system.

4. **Structure determination.** Solve a cryo-EM structure of *P. putida* MlaFEDB (or generate a validated AlphaFold3 model of the complex) to confirm the 5-TM MlaE topology, the substrate-binding pocket, and the continuous MlaE→MlaD lipid pathway in this organism.

5. **Substrate-specificity profiling.** Test a panel of glycerophospholipid species (varying headgroup and acyl chains, including *cis/trans* unsaturated species relevant to *P. putida* solvent adaptation) for binding/transport to determine whether *P. putida* MlaE has headgroup or acyl-chain preferences.

6. **Solvent-tolerance link.** Assay Δ*mlaE* for altered organic-solvent tolerance and membrane integrity under solvent stress, to test whether the Mla system contributes to *P. putida*'s hallmark solvent resistance beyond baseline OM barrier maintenance.

---

## Conclusion

MlaE (Q88P93 / PP_0959) is confidently annotated as the **integral inner-membrane permease subunit of the MlaFEDB ABC transporter**, the inner-membrane core of the *P. putida* Mla (Maintenance of Lipid Asymmetry) system. It forms the transmembrane translocation channel and glycerophospholipid substrate-binding site, coupling phospholipid movement across the inner membrane to ATP hydrolysis by MlaF. Functionally, it is a **glycerophospholipid translocase** acting within a trans-envelope, retrograde (OM→IM) transport relay (MlaA–OmpC/F → MlaC → MlaFEDB) that preserves outer-membrane lipid asymmetry and thereby the OM permeability barrier. It performs this role embedded in the **inner (cytoplasmic) membrane** as part of a conserved ~12-subunit MlaF₂E₂D₆B₂ complex. The assignment rests on direct sequence/domain evidence for the *P. putida* protein combined with strong structural evidence from *E. coli* and the congeneric *P. aeruginosa*; no *P. putida*-specific experimental characterization yet exists, making targeted genetic and biochemical validation the priority next step.


## Artifacts

- [OpenScientist final report](mlaE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mlaE-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:33236984
2. PMID:35981415
3. PMID:19383799
4. PMID:34753108
5. PMID:36459067
6. PMID:33845086
7. PMID:33199922
8. PMID:39373473