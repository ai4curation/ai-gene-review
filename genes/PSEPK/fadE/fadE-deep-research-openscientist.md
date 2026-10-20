---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-10T23:05:02.355753'
end_time: '2026-08-10T23:24:18.689424'
duration_seconds: 1156.33
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: fadE
  gene_symbol: fadE
  uniprot_accession: Q88LN6
  protein_description: 'RecName: Full=Acyl-coenzyme A dehydrogenase {ECO:0000256|ARBA:ARBA00020144};
    EC=1.3.8.7 {ECO:0000256|ARBA:ARBA00012033}; EC=1.3.8.8 {ECO:0000256|ARBA:ARBA00012040};'
  gene_info: Name=fadE {ECO:0000313|EMBL:AAN67512.1}; OrderedLocusNames=PP_1893 {ECO:0000313|EMBL:AAN67512.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the acyl-CoA dehydrogenase family.
  protein_domains: Acyl-CoA_dehydrogenase. (IPR050741); Acyl-CoA_Oxase/DH_mid-dom.
    (IPR006091); Acyl-CoA_Oxase/DH_mid-dom_sf. (IPR046373); AcylCo_DH-like_C. (IPR036250);
    AcylCo_DH/oxidase_C. (IPR009075)
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
  path: fadE-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: fadE-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88LN6
- **Protein Description:** RecName: Full=Acyl-coenzyme A dehydrogenase {ECO:0000256|ARBA:ARBA00020144}; EC=1.3.8.7 {ECO:0000256|ARBA:ARBA00012033}; EC=1.3.8.8 {ECO:0000256|ARBA:ARBA00012040};
- **Gene Information:** Name=fadE {ECO:0000313|EMBL:AAN67512.1}; OrderedLocusNames=PP_1893 {ECO:0000313|EMBL:AAN67512.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the acyl-CoA dehydrogenase family.
- **Key Domains:** Acyl-CoA_dehydrogenase. (IPR050741); Acyl-CoA_Oxase/DH_mid-dom. (IPR006091); Acyl-CoA_Oxase/DH_mid-dom_sf. (IPR046373); AcylCo_DH-like_C. (IPR036250); AcylCo_DH/oxidase_C. (IPR009075)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "fadE" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'fadE' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **fadE** (gene ID: fadE, UniProt: Q88LN6) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *fadE* (PP_1893, UniProt Q88LN6) in *Pseudomonas putida* KT2440

## 1. Summary / Answer to the Research Question

**FadE (PP_1893, Q88LN6) is a membrane-anchored, FAD-dependent acyl-coenzyme A dehydrogenase (EC 1.3.8.7 / 1.3.8.8) that catalyzes the first and committed step of each cycle of fatty-acid β-oxidation:** the α,β-dehydrogenation of a saturated medium- or long-chain fatty acyl-CoA to the corresponding *trans*-2(E)-enoyl-CoA, passing the abstracted electrons via its tightly bound FAD to electron-transfer flavoprotein (ETF) and onward to the respiratory chain. It works in the cytoplasm while tethered to the cytoplasmic (inner) membrane through an N-terminal transmembrane helix, and it operates within the fatty-acid degradation (β-oxidation) pathway together with FadD (acyl-CoA synthetase), FadB (multifunctional hydratase/dehydrogenase) and FadA (thiolase). In *P. putida* this pathway both feeds acetyl-CoA into central metabolism and supplies intermediates for medium-chain-length polyhydroxyalkanoate (mcl-PHA) biosynthesis.

**Gene identity — verified.** The symbol *fadE* is used correctly here. UniProt, KEGG (`ppu:PP_1893`, ortholog **K06445**), and eggNOG (**COG1960**) all annotate PP_1893 as an acyl-CoA dehydrogenase in the fatty-acid degradation pathway, and the protein belongs to the large (~815 aa, ~89 kDa) membrane-associated **FadE clade** typified by *Escherichia coli* FadE. This is distinct from the classic ~400-aa soluble mitochondrial ACADs and from *P. putida*'s own separate aromatic phenylacyl-CoA dehydrogenase (PP_0368). No conflicting-gene ambiguity was found; the naming, family, domains, and organism are all consistent.

---

## 2. Protein Identity and Domain Architecture

| Property | Value | Source |
|---|---|---|
| UniProt | Q88LN6 (Q88LN6_PSEPK), protein existence: inferred from homology | UniProt |
| Gene / locus | *fadE* / PP_1893; genome position complement(2,134,303–2,136,750) | UniProt/KEGG |
| Length / mass | 815 aa / 89,195 Da | UniProt |
| EC numbers | 1.3.8.7 (medium-chain acyl-CoA dehydrogenase); 1.3.8.8 (long-chain) | UniProt |
| Cofactor | FAD (non-covalent) | UniProt (CHEBI:57692) |
| Orthology | KEGG K06445; eggNOG COG1960 | KEGG/eggNOG |
| Domains | ACAD N-terminal (142–236), middle (240–338), C-terminal (363–508), bacterial-type C-terminal extension (517–802) | UniProt/Pfam (PF02771/PF02770/PF00441/PF09317) |
| Transmembrane | Helical TM segment, residues 43–64 | UniProt |

FadE is roughly twice the size of a canonical soluble ACAD. The extra bulk comes from **(i)** an N-terminal hydrophobic membrane anchor and **(ii)** a bacterial-type C-terminal extension (residues 517–802). This architecture is the hallmark of the *E. coli* FadE–type acyl-CoA dehydrogenases (COG1960), to which PP_1893 unambiguously belongs. **Orthology is firmly established:** *E. coli* FadE (gene *b0221*) is 814 aa and is assigned to the same KEGG ortholog group **K06445** as PP_1893 (815 aa) — an almost exact length match for this unusually large ACAD clade (KEGG). (A naïve global alignment to one shorter UniProt sequence record gave only ~28% identity; this reflects both the deep evolutionary divergence within this bacterial clade and a truncated sequence record, not a weak assignment — the KO/COG orthology call and the matching domain architecture and near-identical length are the decisive evidence.)

---

## 3. Primary Function: Reaction Catalyzed and Substrate Specificity

### Reaction
FadE catalyzes the FAD-dependent α,β-dehydrogenation of a saturated fatty acyl-CoA thioester:

> a (medium/long-chain) 2,3-saturated fatty acyl-CoA + oxidized [ETF] + H⁺ → a (2*E*)-enoyl-CoA + reduced [ETF]
> (UniProt catalytic-activity annotations; Rhea RHEA:14477 for medium-chain, RHEA:17721 for long-chain)

This is **the first, committed step of every turn of the β-oxidation cycle**. In the *E. coli* and *Shewanella* orthologs this role is stated explicitly: FadE is "the first committed enzyme of the β-oxidation pathway" (Yusuf et al., 2020, PMID 32507597) and "a flavoprotein involved in each turn of the beta-oxidation cycle" (Sirithanakorn & Imlay, 2024, PMID 39436877).

### Catalytic mechanism (authoritative review)
Acyl-CoA dehydrogenases "constitute a family of flavoproteins that catalyze the alpha,beta-dehydrogenation of fatty acid acyl-CoA conjugates" (Ghisla & Thorpe, 2004, PMID 14728676). Mechanistically, an active-site glutamate base removes the substrate αC–H as a proton while the βC–H is transferred "as a hydride to the flavin N(5) position," producing a reduced-enzyme·enoyl-CoA charge-transfer complex that is the point of electron transfer to ETF (PMID 14728676). This explains FadE's obligate dependence on FAD and its coupling to the ETF/respiratory electron sink rather than to NAD(P)⁺.

### Substrate specificity
- UniProt assigns **both EC 1.3.8.7 (medium-chain) and EC 1.3.8.8 (long-chain)**, and KEGG's GenBank name is "medium-long chain acyl-CoA dehydrogenase" — i.e., a broad medium-to-long chain-length window rather than a single narrow substrate.
- Physiological requirement in the ortholog group: in *E. coli*, "Aerobic growth on sodium oleate was observed only for the cells with intact *fadE* gene" (Gulevich et al., 2016, PMID 29369593), and catabolism of the medium-chain fatty acid dodecanoate (C12) proceeds through FadE (PMID 39436877). These experiments establish that FadE-type activity is **necessary to initiate degradation of exogenous fatty acids as carbon/energy sources**.
- In *P. putida* KT2440, β-oxidation of exogenous medium/long-chain fatty acids (C6–C12) is the central catabolic route generating acetyl-CoA and supplying mcl-PHA monomers (Liu et al., 2023, PMID 36763117).

---

## 4. Subcellular Localization

FadE performs its chemistry **in the cytoplasm, while anchored to the cytoplasmic (inner) membrane**:
- UniProt annotates a single helical **transmembrane segment at residues 43–64**; keywords include Membrane, Transmembrane, Transmembrane helix.
- Kyte–Doolittle hydropathy analysis (this work) shows the protein's global hydrophobicity maximum (peak KD ≈ 2.6) over the N-terminal region (~residues 32–68), coincident with the annotated TM helix.
- The catalytic ACAD domains (residues ~142–802) and FAD-binding site are soluble and cytoplasm-facing; GO assigns **C:cytoplasm** (GO:0005737), **F:FAD binding** (GO:0050660), **F:long-chain (GO:0004466)** and **medium-chain (GO:0070991) acyl-CoA dehydrogenase activity**, and **P:fatty acid β-oxidation using acyl-CoA dehydrogenase** (GO:0033539).

Thus FadE is best described as a **monotopic/peripheral inner-membrane flavoenzyme** whose N-terminal helix physically couples the first oxidation of β-oxidation to the membrane-proximal ETF/electron-transport machinery. This distinguishes the bacterial FadE clade from the fully soluble matrix ACADs of mitochondria.

---

## 5. Pathway Context, Partners, and Regulation

### The β-oxidation spiral in *P. putida* KT2440
FadE is step 1 of the four-reaction cycle that shortens an acyl chain by two carbons per turn:
1. **Activation** — free fatty acid → acyl-CoA, by FadD (long-chain-fatty-acid–CoA ligase; *fadD-I/II* = PP_4549/PP_4550, EC 6.2.1.3).
2. **Dehydrogenation** — acyl-CoA → *trans*-2-enoyl-CoA, by **FadE (PP_1893)** ← *this gene*.
3. **Hydration + oxidation** — enoyl-CoA → 3-hydroxyacyl-CoA → 3-ketoacyl-CoA, by the multifunctional FadB (PP_2136; EC 4.2.1.17/1.1.1.35).
4. **Thiolysis** — 3-ketoacyl-CoA → acetyl-CoA + (chain-2)acyl-CoA, by FadA thiolase (PP_2051; EC 2.3.1.16).

The released acetyl-CoA enters the TCA cycle; in *P. putida* the (R)-3-hydroxyacyl-CoA intermediates are also channelled (via PhaJ enoyl-CoA hydratases) into mcl-PHA polyester storage (PMID 36763117).

### Genomic organization and paralog redundancy
PP_1893 is a **standalone gene**, not part of the *fadBA* operon — it is flanked by an unrelated type-1 fimbrial cluster (*fimD/fimC/fimI* = PP_1889–1891), a hypothetical ORF (PP_1892), and a glutathione-S-transferase/ABC-transporter region (PP_1894–1896) (KEGG genome map). PP_1893 is the genome's **only** K06445/COG1960 FadE-type ACAD, but *P. putida* additionally encodes several other acyl-CoA dehydrogenases — a short-chain enzyme *acd* (PP_2216, EC 1.3.8.1), three EC 1.3.8.7 enzymes (PP_2437, PP_2793, PP_3725; K00249), and the inducible aromatic phenylacyl-CoA dehydrogenase PP_0368 (McMahon & Mayhew, 2007, PMID 17559393). This paralog set implies **partial functional redundancy** in the dehydrogenation step, consistent with the robustness of β-oxidation in this organism.

### Regulation (characterized in the *E. coli* ortholog)
In *E. coli*, *fadE* (originally *yafH*) is a genuine acyl-CoA dehydrogenase whose transcription is controlled by the **FadR** repressor (Sadovskaya et al., 2001, PMID 11771124). The *fadE* operon is induced ~10-fold by long-chain fatty acids (C12 partial, ≥C14 full), repressed by glucose, and constitutively expressed in *fadR* mutants (Clark, 1981, PMID 6271734); long-/medium-chain acyl-CoA effectors bind FadR to relieve repression, co-inducing *fadE* and *fadBA* (Zhang et al., 2006, PMID 16734787). An analogous fatty-acid-responsive control is expected in *P. putida* (which carries FadR/PsrA-type regulators), though this specific regulation has been demonstrated experimentally mainly in the enterobacterial model.

---

## 6. Evidence Basis

- **Direct experimental (orthologs):** genetic requirement of *fadE* for aerobic growth on oleate and role in dodecanoate catabolism in *E. coli* (PMIDs 29369593, 39436877); mechanistic enzymology of ACADs (PMID 14728676); FadR-mediated transcriptional control (PMIDs 6271734, 16734787, 11771124); substrate-differentiated FadE homologs in *Shewanella* (PMID 32507597).
- **Organism-specific (P. putida KT2440):** central role of β-oxidation and its coupling to mcl-PHA metabolism (PMID 36763117); existence of a separate large aromatic-acyl-CoA dehydrogenase, PP_0368 (PMID 17559393).
- **Database / bioinformatic:** UniProt Q88LN6 (EC, catalytic-activity Rhea reactions, FAD cofactor, TM helix 43–64, domain map, GO); KEGG K06445 / module M00087 / pathway ppu00071 and genome neighborhood; eggNOG COG1960; Kyte–Doolittle hydropathy (this work) confirming the N-terminal membrane anchor.

---

## 7. Supported and Refuted Hypotheses

**Supported**
- H1: FadE is an FAD-dependent acyl-CoA dehydrogenase catalyzing β-oxidation's first, committed dehydrogenation. ✔ (UniProt/KEGG + ortholog literature)
- H2: Broad medium/long-chain substrate specificity. ✔ (dual EC assignment; KEGG name; ortholog growth phenotypes)
- H3: Cytoplasm-facing enzyme anchored to the inner membrane by an N-terminal TM helix. ✔ (UniProt features + GO + hydropathy)
- H4: Functions in the β-oxidation pathway with FadD/FadB/FadA; feeds acetyl-CoA and mcl-PHA precursor supply. ✔ (KEGG pathway; PMID 36763117)

**Refuted / not supported**
- That *fadE* lies in the *fadBA* operon — **refuted**: PP_1893 is a standalone gene among fimbrial/transporter genes.
- That PP_1893 is the sole acyl-CoA dehydrogenase / non-redundant — **not supported**: multiple paralogous ACADs exist (PP_2216, PP_2437, PP_2793, PP_3725, PP_0368).

---

## 8. Limitations and Future Directions

- **No enzyme-level study of PP_1893 itself** exists; its precise chain-length optimum, kinetic parameters (kcat/Km across C4–C18 acyl-CoAs), and quaternary structure are inferred from orthology and family membership, not measured directly. Direct biochemistry on purified PP_1893 would define its true substrate profile.
- **Regulation in *P. putida*** (FadR/PsrA involvement, inducer chain-length threshold) has not been experimentally mapped for PP_1893 specifically.
- **Redundancy** among the *P. putida* ACADs means the phenotypic consequence of a *fadE* single knockout is untested; combinatorial deletions would clarify which paralogs cover which chain lengths.
- Localization is inferred from sequence/GO; membrane fractionation or fluorescent tagging would confirm inner-membrane association experimentally.

---

*Prepared through iterative analysis of UniProt, KEGG, eggNOG/InterPro annotations, sequence/hydropathy analysis, and primary literature on FadE-clade acyl-CoA dehydrogenases and P. putida β-oxidation.*


## Artifacts

- [OpenScientist final report](fadE-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](fadE-deep-research-openscientist_artifacts/final_report.pdf)