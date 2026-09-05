---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T02:13:29.703575'
end_time: '2026-09-01T04:03:31.799012'
duration_seconds: 6602.1
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: lolD
  gene_symbol: lolD
  uniprot_accession: Q88KY4
  protein_description: 'RecName: Full=Lipoprotein-releasing system ATP-binding protein
    LolD {ECO:0000255|HAMAP-Rule:MF_01708}; EC=7.6.2.- {ECO:0000255|HAMAP-Rule:MF_01708};'
  gene_info: Name=lolD {ECO:0000255|HAMAP-Rule:MF_01708}; OrderedLocusNames=PP_2155;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the ABC transporter superfamily. Lipoprotein
  protein_domains: AAA+_ATPase. (IPR003593); ABC_transporter-like_ATP-bd. (IPR003439);
    ABC_transporter-like_CS. (IPR017871); ABC_transpr_LolD-like. (IPR015854); LolD_lipo_ATP-bd.
    (IPR011924)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: lolD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: lolD-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88KY4
- **Protein Description:** RecName: Full=Lipoprotein-releasing system ATP-binding protein LolD {ECO:0000255|HAMAP-Rule:MF_01708}; EC=7.6.2.- {ECO:0000255|HAMAP-Rule:MF_01708};
- **Gene Information:** Name=lolD {ECO:0000255|HAMAP-Rule:MF_01708}; OrderedLocusNames=PP_2155;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the ABC transporter superfamily. Lipoprotein
- **Key Domains:** AAA+_ATPase. (IPR003593); ABC_transporter-like_ATP-bd. (IPR003439); ABC_transporter-like_CS. (IPR017871); ABC_transpr_LolD-like. (IPR015854); LolD_lipo_ATP-bd. (IPR011924)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "lolD" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'lolD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **lolD** (gene ID: lolD, UniProt: Q88KY4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of LolD (Q88KY4 / PP_2155) in *Pseudomonas putida* KT2440

## 0. Identity verification (performed first)

- **UniProt:** Q88KY4 — "Lipoprotein-releasing system ATP-binding protein LolD"; EC 7.6.2.- (translocase / ABC-transporter ATPase).
- **Gene / locus:** *lolD* / PP_2155, *Pseudomonas putida* KT2440.
- **Family / domains:** ABC transporter superfamily (LolD subfamily); AAA+ ATPase (IPR003593), ABC transporter-like ATP-binding domain (IPR003439/IPR017871), LolD-like ATP-binding (IPR015854), and the diagnostic **LolD lipoprotein-release ATP-binding** signature (IPR011924).

**Verification result: CONFIRMED, unambiguous.** The gene symbol *lolD*, the "lipoprotein-releasing system ATP-binding protein" description, the EC 7.6.2.- translocase class, and the LolD-specific InterPro signature (IPR011924) all coincide with a single, well-defined function: the ATPase subunit of the Lol (Localization of lipoprotein) ABC transporter LolCDE. The symbol is **not** ambiguous — "LolD" is used consistently across Gram-negative bacteria for this exact subunit. There is no competing gene family sharing the symbol. No *P. putida*-specific primary study of PP_2155 exists, so the functional narrative below is built from (i) the extensively characterized *Escherichia coli* system and (ii) the experimentally validated *Pseudomonas aeruginosa* orthologous system, then transferred to *P. putida* by orthology.

---

## 1. Summary (answer to the research question)

LolD (Q88KY4, PP_2155) is the **cytoplasmic ATP-binding/ATP-hydrolyzing (nucleotide-binding-domain) subunit of the LolCDE ABC transporter**, the machine that initiates sorting of outer-membrane lipoproteins in Gram-negative bacteria. Two copies of LolD associate with one integral-membrane LolC and one LolE to form LolCDE in the **inner (cytoplasmic) membrane**; LolD hydrolyzes ATP on the **cytoplasmic face** of that membrane, and this chemical energy is mechanically coupled — via the conserved "LolD motif" that contacts LolC/LolE — to the **detachment (release) of triacylated outer-membrane lipoproteins from the periplasmic leaflet of the inner membrane**. Unusually for an ABC transporter, LolCDE does not translocate a solute across the bilayer; instead LolD's ATPase activity powers extraction of the lipoprotein's lipid anchor and its hand-off to the periplasmic chaperone LolA, the committed first step of the Lol trafficking pathway. The reaction is essential for outer-membrane biogenesis and viability, making LolCDE (and thus LolD) a validated antibacterial target.

**Confidence:** Very high. The annotation rests on four independent, converging evidence layers: (1) direct *E. coli*/*P. aeruginosa* biochemistry establishing LolD's reaction, mechanism and essentiality; (2) *P. putida*-specific sequence analysis showing a complete, canonical ABC nucleotide-binding domain (NBD-only architecture); (3) 81.5% identity to the biochemically validated *P. aeruginosa* LolD ortholog; and (4) an intact chromosomal *lolC–lolD–lolE* cluster in *P. putida* KT2440, confirming the full machine is encoded in the target organism. No experimental study of PP_2155 itself exists, but function transfer is exceptionally well supported.

---

## 2. Biological context: the lipoprotein biogenesis and Lol sorting pathway

Bacterial lipoproteins are made as cytoplasmic precursors, exported by Sec to the periplasmic (outer) leaflet of the inner membrane, and matured by three enzymes — Lgt (diacylglyceryl transferase), LspA (signal peptidase II), and Lnt (apolipoprotein N-acyltransferase) — to yield the N-terminal triacyl-cysteine lipid anchor (Narita & Tokuda 2010, PMID 26443779). *E. coli* has >90 lipoproteins, most destined for the outer membrane (Narita & Tokuda 2010; Narita, Matsuyama & Tokuda 2004, PMID 15221203).

Sorting of the outer-membrane subset requires the **five-protein Lol system, LolABCDE** (Okuda & Tokuda 2011, PMID 21663440):

1. **LolCDE** (inner-membrane ABC transporter; contains **LolD**) recognizes an outer-membrane-destined lipoprotein and, using ATP, **releases it from the inner membrane**, generating a soluble LolA–lipoprotein complex.
2. **LolA** (periplasmic chaperone) shields the acyl chains in a hydrophobic cavity and ferries the lipoprotein across the aqueous periplasm.
3. **LolB** (outer-membrane receptor lipoprotein) accepts the cargo and **inserts it into the inner leaflet of the outer membrane** (Narita & Tokuda 2010, PMID 20419407).

**LolD is the energizing engine of step 1** — the committed, rate-initiating step of the whole pathway.

---

## 3. Primary molecular function of LolD

### 3.1 It is the ATPase subunit of LolCDE
The founding study reconstituted LolCDE in proteoliposomes and showed it "belong[s] to the ATP-binding cassette (ABC) transporter family" and "catalyses the release of lipoproteins in LolA- and sorting-signal-dependent manners" (Yakushi et al. 2000, PMID 10783239). Notably, the authors emphasized that "the LolCDE complex differs mechanistically from all other ABC transporters as it is not involved in the transmembrane transport of substrates" — i.e., LolD's ATP hydrolysis powers a *release/extraction* reaction, not vectorial solute transport.

### 3.2 Stoichiometry and site of catalysis
LolCDE contains "two copies of an ATPase subunit, LolD, and one copy each of integral membrane subunits LolC and LolE. **LolD hydrolyzes ATP on the cytoplasmic side of the inner membrane**, while LolC and/or LolE recognize and release lipoproteins anchored to the periplasmic leaflet of the inner membrane" (Ito et al. 2006, PMID 16585747). Thus the catalytic reaction — ATP + H₂O → ADP + Pᵢ — occurs in the **cytoplasm**, at the two LolD nucleotide-binding domains, while the substrate-handling occurs on the opposite (periplasmic) face.

### 3.3 Substrate specificity
LolCDE's substrate is the set of **mature triacylated lipoproteins bearing an outer-membrane sorting signal**. Specificity is governed by the residue(s) following the N-terminal acyl-Cys: in *E. coli* the "+2 rule" (Asp at position 2 = inner-membrane retention / LolCDE-avoidance signal), and in *Pseudomonas* the "+3,+4 rule" (Narita & Tokuda 2007, PMID 17350956). LolCDE releases only lipoproteins **lacking** the retention signal. LolD itself does not read the sorting signal (that is done by LolC/LolE); LolD supplies the energy that acts on whatever cargo the membrane subunits have engaged. Aminoacylation of the N-terminal cysteine (Lnt product) is required for Lol-dependent release (Fukuda et al. 2002, PMID 12198129).

### 3.4 Mechanistic coupling — the "LolD motif"
LolD carries "a characteristic sequence called the LolD motif, which is highly conserved among LolD homologs but not other ABC transporters of *E. coli*" (Ito et al. 2006, PMID 16585747). Systematic mutagenesis of all 32 residues of this motif produced 26 dominant-negative alleles (growth arrest on overexpression), and suppressor mutations mapped to the periplasmic loops of LolC and cytoplasmic loops of LolE — genetically defining the **LolD↔LolC/E interaction surface** through which ATP hydrolysis is transmitted to the membrane subunits to drive release. This is the mechanistic heart of energy coupling: LolD is the motor, LolC/E the substrate-handling stators.

### 3.5 Biochemical reconstitution
The functional machine was rebuilt from separately purified subunits: "the functional lipoprotein-releasing machinery was reconstituted into proteoliposomes with *E. coli* phospholipids and separately purified LolC, LolD and LolE" (Kanamaru et al. 2007, PMID 17509078). LolD's ATPase activity (and its dependence on phospholipids/assembly) was directly measured, and — strikingly — a minimal releasing activity could form from LolE + LolD without LolC, underscoring LolD as the indispensable catalytic partner.

---

## 4. Subcellular localization / where LolD acts

- **Compartment:** peripheral membrane protein of the **inner (cytoplasmic) membrane**, associated with the integral-membrane subunits LolC/LolE.
- **Catalytic site orientation:** the two LolD nucleotide-binding domains face the **cytoplasm**, where ATP hydrolysis occurs (Ito et al. 2006, PMID 16585747).
- **Site of the biological reaction it powers:** extraction of lipoproteins from the **periplasmic leaflet of the inner membrane**, with product delivery into the **periplasm** (as the LolA–lipoprotein complex). Downstream steps (LolA transit, LolB insertion) occur in the periplasm and outer membrane respectively (Okuda & Tokuda 2011, PMID 21663440).

---

## 5. Transfer to *Pseudomonas putida* (orthology evidence)

No PP_2155-specific experimental study exists. Confidence in the annotation rests on:

- **Close-relative validation:** In *P. aeruginosa*, cloned LolCDE (with its LolD ATPase), LolA and LolB homologs are functional — purified LolCDE "reconstituted into proteoliposomes … When incubated in the presence of ATP and a LolA homologue, the reconstituted LolCDE homologue released lipoproteins, leading to the formation of a LolA-lipoprotein complex," with subsequent LolB-dependent outer-membrane insertion (Tanaka et al. 2007, PMID 17350955). *P. putida* is a close congener of *P. aeruginosa*.
- **Pseudomonas sorting logic:** the "+3,+4 rule" defines the inner-membrane retention signal read by the *Pseudomonas* Lol system (Narita & Tokuda 2007, PMID 17350956) — the specificity framework applicable to *P. putida*.
- **Sequence/domain conservation:** Q88KY4 bears the LolD-diagnostic InterPro signature (IPR011924) plus the canonical Walker A/B and ABC signature motifs (IPR003439/IPR017871), i.e., a bona fide LolD-type nucleotide-binding domain.

### 5.1 Organism-specific sequence evidence (this work)
Direct motif analysis of the retrieved 227-residue Q88KY4 sequence confirms a **complete, canonical ABC nucleotide-binding domain** in correct order and spacing:

| Motif | Sequence (residues) | Role |
|-------|--------------------|------|
| Walker A / P-loop | **GSSGSGKST** (~42–50) | binds ATP β/γ phosphates |
| Q-loop | **Q84** (in QFHH) | coordinates Mg²⁺/catalytic water; couples to TMD partner |
| ABC signature / C-loop | **LSGGERQR** (~147–154) | forms composite ATP site at NBD dimer interface |
| Walker B | **LVMLDE** (~167–172; D171/E172) | Mg²⁺ coordination and catalytic base |
| H-loop / switch | **H** in VVTHD (~205–208) | stabilizes transition state |

The protein is **only ~227 aa with no transmembrane segment** — i.e., a **stand-alone nucleotide-binding domain**, exactly the architecture expected for the separate cytoplasmic LolD ATPase that dimerizes and docks onto the integral-membrane LolC/LolE subunits. This constitutes direct *P. putida*-specific molecular evidence that Q88KY4 is a catalytically competent ABC ATPase of the LolD type, complementing the *E. coli*/*P. aeruginosa* biochemistry.

### 5.2 Quantitative orthology to experimentally validated LolD (this work)
Global (Needleman–Wunsch) pairwise alignment of the retrieved UniProt sequences:

| Comparison | Identity | Notes |
|-----------|----------|-------|
| *P. putida* LolD (Q88KY4, 227 aa) vs *P. aeruginosa* LolD (Q9HZL7 / LOLD_PSEAE, 227 aa) | **81.5%** (185/227) | same length; P. aeruginosa ortholog is experimentally validated (PMID 17350955) |
| *P. putida* LolD vs *E. coli* LolD (P75957 / LOLD_ECOLI, 233 aa) | **57.3%** (134/234) | cross-genus; well above the ~30% "safe" ortholog-transfer threshold |

All three proteins carry the **identical Walker A P-loop (GSSGSGKS)** and **identical ABC signature (LSGGE)** and are all annotated "Lipoprotein-releasing system ATP-binding protein LolD." The 81.5% identity to a biochemically validated same-genus ortholog, with perfectly conserved catalytic motifs and identical NBD-only architecture, elevates the annotation of PP_2155 from *inferred* to *strongly supported by quantitative homology to an experimentally characterized ortholog*.

### 5.3 Genomic context: a complete lolCDE cluster in P. putida (this work)
The loci flanking *lolD* in the *P. putida* KT2440 chromosome encode its two obligate membrane partners, in the canonical arrangement:

| Locus | Gene | UniProt | Length | Product / localization |
|-------|------|---------|--------|------------------------|
| PP_2154 | **lolC** | Q88KY5 | 416 aa | LolC; cell membrane, multi-pass |
| **PP_2155** | **lolD** | **Q88KY4** | 227 aa | **LolD ATPase; cell inner membrane, peripheral membrane protein** |
| PP_2156 | **lolE** | Q88KY3 | 413 aa | LolE "lipoprotein releasing system, permease protein"; cell membrane, multi-pass |

Flanking genes (PP_2153, a PilZ-domain protein; PP_2157, a sensor histidine kinase) are unrelated. This chromosomal **lolC–lolD–lolE cluster** mirrors the *E. coli lolCDE* operon and demonstrates that *P. putida* encodes a **complete LolCDE transporter** with LolD's integral-membrane partners present and adjacently encoded — independent genomic-synteny evidence that PP_2155 is the ATPase subunit of an assembled LolCDE machine. The UniProt subcellular annotation for Q88KY4 — "Cell inner membrane; Peripheral membrane protein" (HAMAP-Rule MF_01708) — confirms the localization stated in §4.

---

## 6. Essentiality and pathway significance

The Lol pathway is required for viability; a phenotypic screen identified a pyrazole inhibitor whose resistance mutations map to "LolC or LolE, components of the **essential LolCDE transporter complex**, which is required for trafficking of lipoproteins to the outer membrane," and the compound blocked ATP-dependent lipoprotein release in spheroplasts (Nayar et al. 2015, PMID 25733621). Because LolD supplies the ATP hydrolysis that powers this essential release reaction, its activity is indispensable for outer-membrane biogenesis. This is the basis for interest in LolCDE/LolD as an antibacterial target.

---

## 7. Supported and refuted hypotheses

**Supported**
- H1: Q88KY4 is the ATPase (NBD) subunit of the LolCDE ABC transporter — supported (PMID 10783239, 16585747, 17509078).
- H2: LolD hydrolyzes ATP in the cytoplasm and this energizes lipoprotein release from the inner-membrane periplasmic leaflet — supported (PMID 16585747).
- H3: Energy coupling proceeds via the conserved LolD motif contacting LolC/LolE — supported by mutagenesis/suppressor genetics (PMID 16585747).
- H4: Function is conserved in *Pseudomonas*, licensing orthologous annotation of PP_2155 — supported (PMID 17350955, 17350956).
- H5: The complex is essential and drug-targetable — supported (PMID 25733621).

**Refuted / excluded**
- LolCDE is **not** a classical solute-translocating ABC transporter; it does not move substrate across the bilayer (explicitly stated in PMID 10783239). LolD therefore is not annotated as energizing transmembrane import/export of small molecules.
- The symbol *lolD* is **not** ambiguous with any unrelated gene family; no alternative identity was found.

---

## 8. Limitations and future directions

- **Organism gap:** All mechanistic data derive from *E. coli* and *P. aeruginosa*; direct *P. putida* KT2440 biochemistry/genetics on PP_2155 is lacking. A conditional depletion or purified-complex assay in *P. putida* would confirm the transfer.
- **Structure:** Cryo-EM structures of *E. coli* LolCDE exist (referenced in Tao et al. 2024, PMID 38156779) and show a central lipoprotein-binding cavity; an experimental or AlphaFold model of *P. putida* LolD could confirm Walker A/B, signature, Q-loop and the LolD-motif interface, and quantify conservation.
- **Sorting signal:** Whether *P. putida* strictly follows the +3,+4 rule for its own lipoprotein repertoire has not been individually tested.

---

## References (PMIDs)
- 10783239 — Yakushi et al. 2000, *Nat Cell Biol.* Discovery of LolCDE as lipoprotein-releasing ABC transporter.
- 16585747 — Ito et al. 2006, *J Bacteriol.* LolD stoichiometry, cytoplasmic ATP hydrolysis, LolD motif genetics.
- 17509078 — Kanamaru et al. 2007, *J Biol Chem.* Complete reconstitution from separate subunits; LolD ATPase.
- 20888319 — Sakamoto et al. 2010. LolCDE (incl. LolD) mutations altering sorting.
- 17350955 — Tanaka et al. 2007. *P. aeruginosa* Lol system reconstitution.
- 17350956 — Narita & Tokuda 2007. Pseudomonas "+3,+4 rule".
- 12198129 — Fukuda et al. 2002. N-Cys aminoacylation required for Lol release.
- 21663440 — Okuda & Tokuda 2011. Review: lipoprotein sorting in bacteria.
- 26443779 — Narita & Tokuda 2010. Review: biogenesis/membrane targeting of lipoproteins.
- 20419407 — Narita & Tokuda 2010. Review: sorting by the Lol system.
- 15221203 — Narita, Matsuyama & Tokuda 2004. Review: lipoprotein trafficking in *E. coli*.
- 25733621 — Nayar et al. 2015. LolCDE essential; small-molecule inhibitor of release.
- 38156779 — Tao et al. 2024. Photo-crosslinking dissection of LolCDE function.


## Artifacts

- [OpenScientist final report](lolD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](lolD-deep-research-openscientist_artifacts/final_report.pdf)