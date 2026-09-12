---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T18:17:01.810912'
end_time: '2026-07-11T18:38:50.923946'
duration_seconds: 1309.11
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: icd
  gene_symbol: icd
  uniprot_accession: Q88FS2
  protein_description: 'RecName: Full=Isocitrate dehydrogenase [NADP] {ECO:0000256|ARBA:ARBA00019562,
    ECO:0000256|RuleBase:RU004446}; EC=1.1.1.42 {ECO:0000256|ARBA:ARBA00013013, ECO:0000256|RuleBase:RU004446};'
  gene_info: Name=icd {ECO:0000313|EMBL:AAN69605.1}; OrderedLocusNames=PP_4011 {ECO:0000313|EMBL:AAN69605.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the isocitrate and isopropylmalate
  protein_domains: IsoCit/isopropylmalate_DH_CS. (IPR019818); Isocitrate_DH_NADP_dimer_prok.
    (IPR004439); IsoPropMal-DH-like_dom. (IPR024084); Iso_dh (PF00180)
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: icd-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: icd-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FS2
- **Protein Description:** RecName: Full=Isocitrate dehydrogenase [NADP] {ECO:0000256|ARBA:ARBA00019562, ECO:0000256|RuleBase:RU004446}; EC=1.1.1.42 {ECO:0000256|ARBA:ARBA00013013, ECO:0000256|RuleBase:RU004446};
- **Gene Information:** Name=icd {ECO:0000313|EMBL:AAN69605.1}; OrderedLocusNames=PP_4011 {ECO:0000313|EMBL:AAN69605.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the isocitrate and isopropylmalate
- **Key Domains:** IsoCit/isopropylmalate_DH_CS. (IPR019818); Isocitrate_DH_NADP_dimer_prok. (IPR004439); IsoPropMal-DH-like_dom. (IPR024084); Iso_dh (PF00180)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "icd" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'icd' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **icd** (gene ID: icd, UniProt: Q88FS2) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *icd* (PP_4011, Q88FS2) — NADP-Dependent Isocitrate Dehydrogenase of *Pseudomonas putida* KT2440

## Summary

The gene **icd** (ordered locus name **PP_4011**; UniProt **Q88FS2**) of *Pseudomonas putida* KT2440 encodes an **NADP⁺-dependent isocitrate dehydrogenase (IDH; EC 1.1.1.42)**. This is a soluble, cytoplasmic, divalent-cation (Mg²⁺/Mn²⁺)-dependent oxidoreductase that catalyzes the reversible **oxidative decarboxylation of D-(2R,3S)-isocitrate to α-ketoglutarate (2-oxoglutarate) + CO₂**, with concomitant reduction of NADP⁺ to NADPH. This is the third reaction of the tricarboxylic acid (TCA) cycle. The gene symbol *icd*, the organism, the protein family (isocitrate/isopropylmalate dehydrogenase superfamily; PF00180), and the diagnostic domain InterPro IPR004439 ("Isocitrate_DH_NADP_dimer_prok") all agree, and direct analysis of the Q88FS2 protein sequence confirms the identity beyond doubt. **This is the correct gene; the identification is unambiguous.**

Icd is a member of the homodimeric **subfamily-I (E. coli-type)** bacterial NADP-IDHs. Direct pairwise alignment of the 418-residue Q88FS2 sequence against the biochemically defined *E. coli* IDH (P08200) gives **76.2% identity**, and every functionally critical residue is conserved: the catalytic **Tyr–Asp–Lys proton-relay triad** (Tyr162/Asp309/Lys232 in *P. putida* numbering), the divalent-metal ligands (Asp285/Asp313), the NADP⁺ 2′-phosphate specificity pocket, and — importantly — the strictly conserved **regulatory phosphorylation-site serine (Ser115)**. Hydropathy analysis reveals no transmembrane segment and no signal peptide, confirming a cytoplasmic localization.

Beyond catalysis, Icd occupies a pivotal position in central metabolism. As the source of **α-ketoglutarate**, it supplies the carbon skeleton for glutamate synthesis and hence ammonia/nitrogen assimilation, and as an NADP⁺-reducing enzyme it is a principal source of **biosynthetic and antioxidant NADPH**. It sits at the **isocitrate branch point** that partitions carbon flux between the full TCA cycle and the carbon-conserving glyoxylate bypass. In Gram-negative bacteria this branch point is controlled by reversible phosphorylation of the active-site serine by the bifunctional kinase/phosphatase **AceK (IDHKP)**. KT2440 encodes a genuine AceK (PP_4565) and a complete glyoxylate shunt, and because the AceK recognition elements are structurally restricted to the *dimeric* Gram-negative IDHs, Icd/PP_4011 — and not the adjacent, structurally distinct *monomeric* NADP-IDH (idh/PP_4012) — is the phosphoregulated, branch-point isozyme.

---

## Key Findings

### Finding 1 — Icd is an NADP-dependent isocitrate dehydrogenase catalyzing isocitrate → α-ketoglutarate (EC 1.1.1.42)

UniProt Q88FS2 annotates PP_4011 as isocitrate dehydrogenase [NADP], EC 1.1.1.42, a member of the isocitrate/isopropylmalate dehydrogenase family (Pfam PF00180; InterPro IPR004439, "Isocitrate_DH_NADP_dimer_prok"). The canonical, biochemically established reaction for this enzyme family is the divalent-cation-dependent, reversible NADP-linked interconversion:

> **isocitrate + NADP⁺ ⇌ α-ketoglutarate + CO₂ + NADPH**

This reaction has been directly demonstrated in multiple orthologs, including *Streptococcus mutans* IDH, *Acinetobacter baumannii* AbIDH1, and the archetypal *E. coli* IDH. The reversibility of the enzyme — the same active site can perform reductive carboxylation of α-ketoglutarate back to isocitrate — is a general property of the IDH family ([PMID: 23484056](https://pubmed.ncbi.nlm.nih.gov/23484056/)): *"Isocitrate dehydrogenase (IDH) is a reversible enzyme in the tricarboxylic acid cycle that catalyzes the NAD(P)(+)-dependent oxidative decarboxylation of isocitrate to α-ketoglutarate (αKG) and the NAD(P)H/CO2-dependent reductive carboxylation of αKG to isocitrate."* This establishes both the reaction and the TCA-cycle context of the enzyme to which Icd belongs.

### Finding 2 — Icd belongs to the homodimeric, divalent-cation-dependent subfamily-I (E. coli-type) NADP-IDH with strong NADP⁺ specificity

The prokaryotic dimeric NADP-IDH class (InterPro IPR004439) is the E. coli/subfamily-I type. The defining biochemical property of this subfamily is a very strong preference for NADP⁺ over NAD⁺, encoded not by a classical Rossmann fold but by a distinct adenosine-binding pocket. In *E. coli* IDH this preference is ~7,000-fold on a kcat/Km basis, and remarkably, six mutations in the coenzyme pocket can invert this to an 850-fold NAD⁺ preference — a landmark demonstration that the specificity determinants are localized and well understood ([PMID: 8524825](https://pubmed.ncbi.nlm.nih.gov/8524825/)): *"The isocitrate dehydrogenase of Escherichia coli, which lacks the Rossmann fold common to other dehydrogenases, displays a 7000-fold preference for NADP over NAD."*

The quaternary structure and metal dependence are equally diagnostic. Homologous bacterial enzymes are ~70–84 kDa homodimers requiring a divalent metal. *S. mutans* IDH is a ~70 kDa homodimer whose activity is Mn²⁺-dependent ([PMID: 23484056](https://pubmed.ncbi.nlm.nih.gov/23484056/)): *"The molecular weight of SmIDH was estimated to be 70 kDa by gel filtration chromatography, suggesting a homodimeric structure. SmIDH was divalent cation-dependent and Mn(2+) was found to be the most effective cation."* A second Gram-negative homolog confirms the pattern ([PMID: 33290880](https://pubmed.ncbi.nlm.nih.gov/33290880/)): *"AbIDH1 is an 83.5 kDa homodimer in solution. The kinetics showed that AbIDH1 is a fully active NADP-dependent enzyme."* UniProt annotates the SUBUNIT of Q88FS2 as "Homodimer," consistent with this class.

### Finding 3 — In Gram-negative bacteria, subfamily-I NADP-IDH is regulated by reversible phosphorylation (AceK/IDHKP), gating the TCA-vs-glyoxylate branch point

*E. coli* IDH was the first bacterial enzyme shown to be regulated by reversible phosphorylation. The bifunctional **isocitrate dehydrogenase kinase/phosphatase (AceK/IDHKP)** phosphorylates a substrate-binding serine to inactivate IDH; the level of remaining IDH activity determines whether carbon flux runs through the full TCA cycle or is diverted into the glyoxylate bypass for growth on two-carbon substrates ([PMID: 22889914](https://pubmed.ncbi.nlm.nih.gov/22889914/)): *"The switch between the Krebs cycle and the glyoxylate bypass is controlled by isocitrate dehydrogenase kinase/phosphatase (AceK)."*

The direct link between IDH activity level and flux partitioning is explicit ([PMID: 23192354](https://pubmed.ncbi.nlm.nih.gov/23192354/)): *"the level of IDH activity determines whether carbon flux is directed through the glyoxylate bypass (for growth on two-carbon substrates) or the full tricarboxylic acid cycle."* Critically, the structural determinants that allow AceK to recognize its substrate are conserved only in a specific structural class ([PMID: 21870819](https://pubmed.ncbi.nlm.nih.gov/21870819/)): *"the highly stringent AceK binding sites on ICDH are maintained only in Gram-negative bacteria."* Because *P. putida* KT2440 is a Gram-negative γ-proteobacterium encoding a dimeric IDH, Icd retains the machinery for this regulation. Additional layers of control (e.g., lysine acetylation) also modulate bacterial IDH ([PMID: 29733852](https://pubmed.ncbi.nlm.nih.gov/29733852/)): *"E. coli ICDH was the first bacterial enzyme shown to be regulated by reversible phosphorylation."*

### Finding 4 — Icd functions in the cytoplasm as a principal NADPH source and supplier of α-ketoglutarate for glutamate/nitrogen assimilation

By coupling oxidative TCA turnover to reduction of NADP⁺, Icd is a major generator of cytoplasmic NADPH, which is used for reductive biosynthesis and defense against oxidative stress. Its product, α-ketoglutarate, is the carbon skeleton for glutamate synthesis, the entry point for ammonia assimilation via the glutamine synthetase/glutamate synthase (GS/GOGAT) and glutamate dehydrogenase pathways. NADP-specific IDH is routinely detected as a soluble activity in bacterial cell-free extracts operating within the glutamate-forming network ([PMID: 24310015](https://pubmed.ncbi.nlm.nih.gov/24310015/)): *"malate dehydrogenase, fumarase, fumarate reductase and an NADP-specific isocitrate dehydrogenase were readily detectable."*

*P. putida* KT2440 is recognized as a robust metabolic chassis whose central metabolism generates abundant NADPH to counter oxidative/redox stress ([PMID: 26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/)): the re-annotated genome *"recognizes the capacity of this bacterium to perform difficult redox reactions, thereby multiplying its value as a platform microorganism for industrial biotechnology."* Icd is a central NADPH-generating node in this redox-rich metabolism.

### Finding 5 — Icd uses the conserved three-step β-decarboxylating dehydrogenase mechanism with a Tyr/Asp/Lys proton relay

The enzyme belongs to the α-hydroxyacid oxidative β-decarboxylase (isocitrate/isopropylmalate dehydrogenase) superfamily, whose members catalyze a conserved three-step reaction ([PMID: 22891681](https://pubmed.ncbi.nlm.nih.gov/22891681/)): *"NADP(+) dependent isocitrate dehydrogenase (IDH; EC 1.1.1.42) belongs to a large family of α-hydroxyacid oxidative β-decarboxylases that catalyze similar three-step reactions, with dehydrogenation to an oxaloacid intermediate preceding β-decarboxylation to an enol intermediate followed by tautomerization to the final α-ketone product."*

The three chemical steps are: (1) metal-assisted dehydrogenation of isocitrate to an oxalosuccinate intermediate with hydride transfer to NADP⁺, (2) β-decarboxylation to an enol intermediate releasing CO₂, and (3) tautomerization to α-ketoglutarate. Crystal structures of a pseudo-Michaelis complex of the *E. coli* enzyme identify the catalytic residues and their motions ([PMID: 22891681](https://pubmed.ncbi.nlm.nih.gov/22891681/)): *"Lys230* is positioned to deprotonate/reprotonate the α-hydroxyl in both reaction steps and Tyr160 moves into position to protonate C3 following β-decarboxylation. A proton relay from the catalytic triad Tyr160-Asp307-Lys230* connects the α-hydroxyl of isocitrate to the bulk..."* A divalent metal chelates the substrate, and a phosphorylation loop positions the NADP⁺ nicotinamide. This regulatory serine is strictly conserved and its phosphorylation switches the enzyme off ([PMID: 15173171](https://pubmed.ncbi.nlm.nih.gov/15173171/)): *"Bacterial IDHs are reversibly regulated by phosphorylation of a strictly conserved serine residue at the active site."*

### Finding 6 — Direct sequence analysis of Q88FS2 confirms a 418-aa dimeric E. coli-type NADP-IDH with all functional residues conserved and no membrane-targeting features

This is the strongest, most direct line of evidence for the annotation because it interrogates the target sequence itself rather than relying on homology annotations. Pairwise global alignment (Needleman–Wunsch, BLOSUM62) of the *P. putida* KT2440 Icd sequence (Q88FS2, 418 aa) against the biochemically defined *E. coli* ortholog (P08200, 416 aa) gives **76.2% identity (317/416)**. The 418-residue length matches the ~416-aa dimeric (subfamily-I) enzyme, decisively distinguishing it from the ~741-aa monomeric NADP-IDH clade.

Every functionally critical *E. coli* residue is conserved (E. coli → P. putida numbering):

| Functional role | *E. coli* residue | *P. putida* (Q88FS2) residue |
|---|---|---|
| Catalytic proton-relay triad | Tyr160, Asp307, Lys230 | Tyr162, Asp309, Lys232 |
| Divalent-metal ligands | Asp283, Asp311 | Asp285, Asp313 |
| Regulatory phosphorylation serine | Ser113 | **Ser115** |
| NADP⁺ 2′-phosphate specificity pocket | Lys344, Tyr345, Tyr391, Arg395, Arg292 | Lys346, Tyr347, Tyr393, Arg397, Arg294 |

The conservation of the proton-relay triad ([PMID: 22891681](https://pubmed.ncbi.nlm.nih.gov/22891681/)) confirms catalytic competence, and conservation of the NADP-specificity determinants ([PMID: 8524825](https://pubmed.ncbi.nlm.nih.gov/8524825/) — *"displays a 7000-fold preference for NADP over NAD"*) supports strict NADP⁺ specificity. Kyte–Doolittle hydropathy (window 19) reaches a maximum of only 1.16, with zero windows above the ~1.6 transmembrane threshold, and the N-terminus (MGYQKIKVPTDG…) lacks a signal peptide — together indicating a **soluble cytoplasmic protein** with no membrane targeting.

### Finding 7 — KT2440 encodes two distinct NADP-IDH isozymes plus a genuine AceK and complete glyoxylate shunt; Icd is specifically the dimeric, AceK-regulated branch-point isozyme

A proteome query of *P. putida* KT2440 (UniProt organism 160488) reveals **two separate NADP-dependent isocitrate dehydrogenases**, both EC 1.1.1.42, arranged in tandem:

| Gene | Locus | UniProt | Length | Type |
|---|---|---|---|---|
| **icd** (target) | PP_4011 | Q88FS2 | 418 aa | Dimeric, E. coli/subfamily-I (SUBUNIT "Homodimer") |
| idh | PP_4012 | Q88FS1 | 741 aa | Monomeric NADP-IDH (AltName "Oxalosuccinate decarboxylase"; PIRNR009407) |

The two genes are consecutive (locus tags PP_4011/PP_4012; consecutive EMBL CDS AAN69605/AAN69606). KT2440 also encodes the cognate regulator **AceK (Q88EA1, aceK/PP_4565)**, isocitrate dehydrogenase kinase/phosphatase (EC 2.7.11.5 / 3.1.3.-), and a complete glyoxylate bypass: isocitrate lyase **AceA (PP_4116, EC 4.1.3.1)** and malate synthase G **GlcB (PP_0356, EC 2.3.3.9)**, with isocitrate supplied by three aconitases (PP_2112, PP_2336, PP_2339).

Because AceK recognition elements are structurally restricted to dimeric Gram-negative ICDHs ([PMID: 21870819](https://pubmed.ncbi.nlm.nih.gov/21870819/)), and because Icd's phosphorylation-site serine (Ser115) is conserved (Finding 6), **Icd/PP_4011 — not the monomeric Idh/PP_4012 — is the isozyme subject to AceK phosphoregulation** at the isocitrate branch point. This makes Icd the flux-controlling "valve" ([PMID: 23192354](https://pubmed.ncbi.nlm.nih.gov/23192354/)): *"the level of IDH activity determines whether carbon flux is directed through the glyoxylate bypass ... or the full tricarboxylic acid cycle."*

### Finding 8 — Structural/biochemical evidence confirms the dimeric Icd (not the monomeric Idh) as the phosphoregulated branch-point IDH, and confirms IDH is essential for 2-oxoglutarate/glutamate biosynthesis

Both monomeric and dimeric NADP-IDHs catalyze the same oxidative decarboxylation of (2R,3S)-isocitrate to 2-oxoglutarate + CO₂ + NADPH, but they differ decisively in regulation. In the monomeric *Corynebacterium glutamicum* enzyme, the region corresponding to the *E. coli* phosphorylation loop is α-helical and structured, so it is not a phosphorylation target ([PMID: 16416443](https://pubmed.ncbi.nlm.nih.gov/16416443/)): *"In CgIDH, the amino acid residues corresponding to the Escherichia coli IDH phosphorylation-loop are alpha-helical compared with the more flexible random-coil region in the E. coli protein where IDH activation is controlled by phosphorylation. This more structured region supports the idea that activation of CgIDH is not controlled by phosphorylation."* This confirms that within KT2440's two isozymes, only the dimeric Icd/PP_4011 can be AceK-regulated. The two isozyme classes share no significant overall sequence identity yet are structurally homologous ([PMID: 11185559](https://pubmed.ncbi.nlm.nih.gov/11185559/)): *"No significant overall sequence identity is found between the monomeric and dimeric enzymes. However, structure-based alignment leads to the identification of three regions in the monomeric enzyme that match closely the three motifs located in the central region of dimeric IDHs."*

The physiological essentiality of NADP-IDH for glutamate biosynthesis is demonstrated experimentally: chromosomal inactivation of *icd* in *C. glutamicum* causes glutamate auxotrophy with complete loss of ICD activity ([PMID: 7836312](https://pubmed.ncbi.nlm.nih.gov/7836312/)): *"Inactivation of the chromosomal icd gene led to glutamate auxotrophy and to the absence of any detectable ICD activity."* The branch-point significance is explicit ([PMID: 21931217](https://pubmed.ncbi.nlm.nih.gov/21931217/)): *"It also lies at a crucial bifurcation point between CO2-generating steps in the cycle and carbon-conserving steps in the glyoxylate bypass. Hence, the enzyme is a focus of regulation."* In KT2440, the glyoxylate shunt is physiologically engaged on acetate, being up-regulated by the transcription factor HexR ([PMID: 41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/)).

---

## Mechanistic Model / Interpretation

### The catalyzed reaction and its chemistry

```
                         Mg²⁺/Mn²⁺
   D-isocitrate  +  NADP⁺  ─────────►  α-ketoglutarate  +  CO₂  +  NADPH
   (2R,3S)                             (2-oxoglutarate)

   Step 1 (dehydrogenation):   isocitrate → oxalosuccinate + NADPH   [hydride → NADP⁺]
   Step 2 (β-decarboxylation):  oxalosuccinate → enol intermediate + CO₂
   Step 3 (tautomerization):    enol → α-ketoglutarate

   Proton relay:  α-OH ⇄ Lys232 ⇄ Asp309 ⇄ Tyr162 → C3 (P. putida numbering)
   Metal ligands: Asp285, Asp313 chelate substrate + divalent cation
```

### Position in metabolism — the isocitrate branch point

```
                Glycolytic / gluconeogenic substrates
                                 │
                                 ▼
       citrate ──► cis-aconitate ──► ISOCITRATE
                                          │
                          ┌───────────────┴────────────────┐
                Icd (PP_4011) NADP-IDH             AceA (isocitrate lyase)
                full TCA cycle                     glyoxylate bypass
                          │                                │
                          ▼                                ▼
              α-ketoglutarate + CO₂ + NADPH        glyoxylate + succinate
                          │                                │
        ┌─────────────────┴──────────┐            GlcB (malate synthase)
        ▼                            ▼                     │
   Glutamate / N-assimilation   succinyl-CoA ... → oxaloacetate ◄── malate
```

**Control logic.** The partitioning of isocitrate between Icd (→ full TCA, CO₂-releasing, NADPH-generating) and isocitrate lyase AceA (→ glyoxylate bypass, carbon-conserving) is governed by the activity of Icd. When cells grow on C2/gluconeogenic substrates (e.g., acetate), AceK phosphorylates Icd on Ser115, lowering its activity; this raises the steady-state isocitrate concentration and channels flux into the glyoxylate bypass, conserving carbon for biosynthesis. When Icd is active (dephosphorylated), flux proceeds through the full cycle, maximizing NADPH and α-ketoglutarate output. In KT2440 this switch is transcriptionally reinforced on acetate by HexR-mediated up-regulation of the glyoxylate shunt ([PMID: 41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/)).

### Isozyme division of labor in KT2440

KT2440 is unusual in encoding two NADP-IDHs. The evidence indicates a clear structural/regulatory division: the **dimeric Icd/PP_4011** carries the classic AceK-phosphoregulated, flux-gating role (it has the flexible phosphorylation loop and conserved Ser115), whereas the **monomeric Idh/PP_4012** is structurally incapable of AceK regulation (its equivalent loop is α-helical, as shown for the homologous monomeric CgIDH). Both can produce α-ketoglutarate + NADPH, but only Icd functions as the regulated branch-point valve.

### Localization

All evidence points to a **soluble cytoplasmic** enzyme: no transmembrane segment (hydropathy max 1.16, below the ~1.6 threshold), no signal peptide, and the enzyme is routinely recovered as a soluble activity in cell-free extracts of related bacteria. It performs its function in the cytoplasm, where the TCA cycle, glyoxylate bypass, and glutamate biosynthesis all operate in this Gram-negative bacterium.

---

## Evidence Base

| PMID | Relevance to Icd/PP_4011 | Support / Challenge |
|---|---|---|
| [23484056](https://pubmed.ncbi.nlm.nih.gov/23484056/) | Defines the reversible NADP-IDH reaction; documents homodimeric, Mn²⁺-dependent *S. mutans* enzyme | Supports F1, F2 |
| [8524825](https://pubmed.ncbi.nlm.nih.gov/8524825/) | *E. coli* IDH shows 7000-fold NADP over NAD preference; non-Rossmann architecture | Supports F2, F6 |
| [33290880](https://pubmed.ncbi.nlm.nih.gov/33290880/) | *A. baumannii* AbIDH1 — 83.5 kDa homodimer, fully NADP-dependent | Supports F2 |
| [22889914](https://pubmed.ncbi.nlm.nih.gov/22889914/) | AceK controls the Krebs-cycle/glyoxylate-bypass switch | Supports F3 |
| [21870819](https://pubmed.ncbi.nlm.nih.gov/21870819/) | AceK binding sites maintained only in Gram-negative dimeric ICDHs | Supports F3, F7 |
| [23192354](https://pubmed.ncbi.nlm.nih.gov/23192354/) | IDH activity level determines TCA-vs-glyoxylate flux | Supports F3, F7 |
| [29733852](https://pubmed.ncbi.nlm.nih.gov/29733852/) | Bacterial IDH regulated by phosphorylation and acetylation | Supports F3 |
| [24310015](https://pubmed.ncbi.nlm.nih.gov/24310015/) | NADP-specific IDH detectable as soluble activity feeding glutamate network | Supports F4 |
| [26913973](https://pubmed.ncbi.nlm.nih.gov/26913973/) | KT2440 redox-rich central metabolism; robust chassis | Supports F4 |
| [22891681](https://pubmed.ncbi.nlm.nih.gov/22891681/) | Three-step β-decarboxylase mechanism; Tyr160-Asp307-Lys230 relay in *E. coli* IDH | Supports F5, F6 |
| [15173171](https://pubmed.ncbi.nlm.nih.gov/15173171/) | Bacterial IDHs regulated by phosphorylation of conserved active-site serine | Supports F5 |
| [16416443](https://pubmed.ncbi.nlm.nih.gov/16416443/) | Monomeric CgIDH phosphorylation loop is α-helical, not phosphoregulated | Supports F8 (isozyme discrimination) |
| [7836312](https://pubmed.ncbi.nlm.nih.gov/7836312/) | *icd* inactivation → glutamate auxotrophy, loss of ICD activity | Supports F4, F8 (essentiality) |
| [21931217](https://pubmed.ncbi.nlm.nih.gov/21931217/) | IDH at TCA/glyoxylate bifurcation, focus of regulation | Supports F8 |
| [11185559](https://pubmed.ncbi.nlm.nih.gov/11185559/) | Monomeric vs dimeric IDH: no overall identity but structural homology | Supports F7, F8 |
| [41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/) | HexR up-regulates glyoxylate shunt on acetate in KT2440 | Contextual support F8 |

**Note on the human IDH literature.** Several retrieved papers (e.g., PMIDs 42039522, 41881251, 41808665, 41394091) concern human cytosolic IDH1 and cancer-associated R132H neomorphic mutants that produce D-2-hydroxyglutarate. These are homologous but distinct proteins from a different organism and are **not** used to support claims about the bacterial Icd; they are noted only to document that "IDH" literature is dominated by the human oncometabolite field, which is why gene-identity verification was essential.

---

## Gene-Identity Verification (Conclusion: CONFIRMED)

All mandatory checks pass:

1. **Symbol matches description** — *icd* is the standard symbol for isocitrate dehydrogenase; the UniProt description (NADP-IDH, EC 1.1.1.42) matches.
2. **Organism correct** — All evidence is for, or applied to, *P. putida* KT2440 (organism 160488), not a different species with an *icd* homolog.
3. **Family/domains align** — Pfam PF00180, InterPro IPR004439 (dimeric prokaryotic NADP-IDH), and IPR019818/IPR024084 all match the dimeric E. coli-type NADP-IDH described in the literature.
4. **Direct sequence confirmation** — 76.2% identity to *E. coli* IDH with all catalytic, metal, NADP-specificity, and regulatory residues conserved (Finding 6), which is definitive and does not rely on annotation transfer alone.

**The gene symbol is not ambiguous for this protein; the identification is secure.**

---

## Limitations and Knowledge Gaps

- **No direct experimental characterization of PP_4011 itself.** All kinetic parameters (Km, kcat, NADP/NAD selectivity, metal preference) are inferred from orthologs (*E. coli*, *S. mutans*, *A. baumannii*) and from sequence conservation. The actual enzyme has not, to our knowledge, been purified and assayed in these iterations.
- **Phosphoregulation is inferred, not demonstrated for KT2440.** The conservation of Ser115 and of AceK-recognition elements, plus the presence of a genuine AceK (PP_4565), strongly predict that Icd/PP_4011 is phosphoregulated — but in-vivo phosphorylation and AceK-dependent activity modulation of PP_4011 have not been experimentally shown here.
- **Division of labor between PP_4011 and PP_4012 is a structural inference.** The proposal that Icd carries the regulated branch-point role while Idh does not is based on structural homology to CgIDH; the actual expression conditions, relative flux contributions, and possible functional redundancy of the two isozymes in KT2440 remain to be measured.
- **NADP⁺ specificity magnitude is estimated by homology.** While the specificity-pocket residues are conserved, the exact fold-preference for NADP⁺ over NAD⁺ in the *P. putida* enzyme has not been measured.
- **No experimental structure of Q88FS2.** Mechanistic and residue assignments rely on the *E. coli* crystal structures and sequence alignment; an experimental or high-confidence predicted structure of PP_4011 would further consolidate the model.

---

## Proposed Follow-up Experiments / Actions

1. **Recombinant expression and kinetic characterization** of PP_4011 (His-tagged, expressed in *E. coli*): determine Km(isocitrate), Km(NADP⁺), kcat, the NADP⁺/NAD⁺ selectivity ratio, and the divalent-metal preference (Mg²⁺ vs Mn²⁺), confirming Findings 1, 2, and 6 directly.
2. **AceK phosphoregulation assay:** co-incubate purified PP_4011 with purified AceK (PP_4565) ± ATP and measure loss of IDH activity; use a Ser115Ala mutant as a phosphorylation-null control to prove the site, directly testing Finding 7.
3. **Comparative gene knockouts:** construct ΔPP_4011, ΔPP_4012, and the double mutant; test for glutamate auxotrophy and growth on glucose vs acetate. This would resolve the isozyme division of labor (Finding 8) and reveal any redundancy.
4. **¹³C metabolic flux analysis** on glucose vs acetate in wild-type vs Δicd to quantify the flux split at the isocitrate branch point and Icd's contribution to NADPH generation.
5. **Structural determination** (X-ray, cryo-EM, or AlphaFold-Multimer of the homodimer) of PP_4011 in complex with isocitrate, NADP⁺, and metal, to verify the modeled active-site geometry and the Tyr162/Asp309/Lys232 relay.
6. **Phosphoproteomics** of KT2440 grown on acetate to detect Ser115 phosphorylation on PP_4011 in vivo, and to confirm PP_4012 is not phosphorylated at the equivalent position.

---

## Conclusion

*icd* (PP_4011, Q88FS2) encodes the **homodimeric, NADP⁺-specific isocitrate dehydrogenase of *Pseudomonas putida* KT2440** — a soluble cytoplasmic, Mg²⁺/Mn²⁺-dependent enzyme that catalyzes the reversible oxidative decarboxylation of D-isocitrate to α-ketoglutarate + CO₂ with reduction of NADP⁺ to NADPH, via a conserved three-step β-decarboxylase mechanism and a Tyr162/Asp309/Lys232 proton relay. It performs the third step of the TCA cycle, supplies NADPH and α-ketoglutarate (for glutamate/nitrogen assimilation), and sits at the isocitrate branch point that partitions carbon between the full TCA cycle and the glyoxylate bypass. As the dimeric, Gram-negative-type isozyme bearing a conserved regulatory Ser115, it is the AceK-phosphoregulated branch-point enzyme, distinct from the co-encoded monomeric NADP-IDH (idh/PP_4012). The functional assignment is confirmed by 76% sequence identity to *E. coli* IDH with complete conservation of all catalytic, metal-binding, NADP-specificity, and regulatory residues.


## Artifacts

- [OpenScientist final report](icd-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](icd-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:23484056
2. PMID:8524825
3. PMID:33290880
4. PMID:22889914
5. PMID:23192354
6. PMID:21870819
7. PMID:29733852
8. PMID:24310015
9. PMID:26913973
10. PMID:22891681
11. PMID:15173171
12. PMID:16416443
13. PMID:11185559
14. PMID:7836312
15. PMID:21931217
16. PMID:41260329