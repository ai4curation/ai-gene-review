---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T18:08:19.661620'
end_time: '2026-07-11T18:40:50.583498'
duration_seconds: 1950.92
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: mqo3
  gene_symbol: mqo3
  uniprot_accession: Q88IS4
  protein_description: 'RecName: Full=Probable malate:quinone oxidoreductase 3 {ECO:0000255|HAMAP-Rule:MF_00212};
    EC=1.1.5.4 {ECO:0000255|HAMAP-Rule:MF_00212}; AltName: Full=MQO 3 {ECO:0000255|HAMAP-Rule:MF_00212};
    AltName: Full=Malate dehydrogenase [quinone] 3 {ECO:0000255|HAMAP-Rule:MF_00212};'
  gene_info: Name=mqo3 {ECO:0000255|HAMAP-Rule:MF_00212}; Synonyms=mqo-3; OrderedLocusNames=PP_2925;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the MQO family. {ECO:0000255|HAMAP-
  protein_domains: FAD/NAD-bd_sf. (IPR036188); MQO. (IPR006231); Mqo (PF06039)
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: mqo3-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: mqo3-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88IS4
- **Protein Description:** RecName: Full=Probable malate:quinone oxidoreductase 3 {ECO:0000255|HAMAP-Rule:MF_00212}; EC=1.1.5.4 {ECO:0000255|HAMAP-Rule:MF_00212}; AltName: Full=MQO 3 {ECO:0000255|HAMAP-Rule:MF_00212}; AltName: Full=Malate dehydrogenase [quinone] 3 {ECO:0000255|HAMAP-Rule:MF_00212};
- **Gene Information:** Name=mqo3 {ECO:0000255|HAMAP-Rule:MF_00212}; Synonyms=mqo-3; OrderedLocusNames=PP_2925;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the MQO family. {ECO:0000255|HAMAP-
- **Key Domains:** FAD/NAD-bd_sf. (IPR036188); MQO. (IPR006231); Mqo (PF06039)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "mqo3" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'mqo3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **mqo3** (gene ID: mqo3, UniProt: Q88IS4) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *mqo3* (PP_2925, UniProt Q88IS4) — Probable Malate:Quinone Oxidoreductase 3 of *Pseudomonas putida* KT2440

## 1. Summary (Answer to the Research Question)

**mqo3** (locus tag **PP_2925**; KEGG symbol *mqo-III*; UniProt **Q88IS4**) of *Pseudomonas putida* KT2440 encodes one of three paralogous **malate:quinone oxidoreductases (MQO; EC 1.1.5.4)**. Its primary, and essentially sole, catalytic function is the **FAD-dependent oxidation of (S)-malate (L-malate) to oxaloacetate, transferring the two electrons directly to a membrane quinone** rather than to NAD⁺:

> **(S)-malate + a quinone → oxaloacetate + a quinol**  (Rhea:46012; EC 1.1.5.4)

This is the malate → oxaloacetate step of the **tricarboxylic acid (TCA/citric acid) cycle**, performed via the "quinone route" (UniProt/HAMAP pathway: *TCA cycle; oxaloacetate from (S)-malate (quinone route): step 1/1*). Because the electron acceptor is a lipophilic quinone of the respiratory chain, MQO3 acts as a **membrane-associated peripheral flavoprotein that couples the TCA cycle directly to aerobic respiration**, in the same conceptual manner that succinate dehydrogenase (complex II) does. The enzyme carries out its function on the **cytoplasmic face of the inner (cytoplasmic) membrane**, where it can reduce the membrane ubiquinone pool. Its substrate specificity is for L-malate (the flavin/FAD active site is that of the MQO/DAO glutathione-reductase-2-like FAD superfamily), and its "substrate" on the acceptor side is a respiratory quinone (ubiquinone in aerobically grown *Pseudomonas*).

The identity of the target is confirmed: gene symbol, EC number, MQO family (Pfam PF06039; InterPro IPR006231 "MQO", IPR036188 "FAD/NAD(P)-binding domain superfamily"), organism (*P. putida* KT2440, taxid 160488), and locus tag (PP_2925) are all mutually consistent across UniProt, KEGG, and the primary MQO literature. There is no ambiguity of identity; the caveat is only that no experimental study has characterized **this specific paralog** — its function is inferred from the well-characterized bacterial MQO family plus bioinformatic, structural, and network evidence.

---

## 2. Gene/Protein Identity and Verification

| Attribute | Value | Source |
|---|---|---|
| Gene name / synonym | *mqo3* / *mqo-3* / *mqo-III* | UniProt Q88IS4; KEGG ppu:PP_2925 |
| Locus tag | PP_2925 | UniProt; KEGG |
| Protein | Probable malate:quinone oxidoreductase 3 (MQO 3) | UniProt (HAMAP-Rule MF_00212) |
| EC | 1.1.5.4 (malate dehydrogenase, quinone) | UniProt; KEGG |
| Length | 539 aa | UniProt |
| Cofactor | FAD (non-covalent) | UniProt; Molenaar 1998 (PMID 9660197) |
| Family/domains | MQO family; Pfam PF06039 (Mqo), also DAO; IPR006231, IPR036188 | UniProt/InterPro; KEGG MOTIF |
| Organism | *Pseudomonas putida* KT2440 (taxid 160488) | UniProt |
| Reference proteome | UP000000556 | UniProt |

All identifiers are internally consistent, and the retrieved primary literature (below) is genuinely about **malate:quinone oxidoreductase**, not a same-symbol homonym. Verification passed.

---

## 3. Primary Function: The Catalyzed Reaction and Substrate Specificity

MQO is a **flavin adenine dinucleotide (FAD)-dependent oxidoreductase** that oxidizes L-malate to oxaloacetate and reduces a quinone. Unlike the classical NAD-dependent malate dehydrogenase (MDH, EC 1.1.1.37), MQO **does not use NAD⁺**; the natural electron acceptor is a membrane quinone. This was established biochemically for the founding family member from *Corynebacterium glutamicum*:

> "It oxidizes L-malate to oxaloacetate and donates electrons to ubiquinone-1 and other artificial acceptors or, via the electron transfer chain, to oxygen. NAD is not an acceptor and the natural direct acceptor for the enzyme is most likely a quinone." (Molenaar et al., 1998, PMID 9660197)

The same study established that **FAD is the (non-covalently but tightly bound) prosthetic group** and that the enzyme is lipid-activated (Molenaar et al., 1998, PMID 9660197). MQO3's sequence contains the canonical N-proximal FAD/dinucleotide-binding fingerprint (`VDVLLVGGGIMS`), a Rossmann-like βαβ motif of the FAD/NAD(P)-binding superfamily (IPR036188), shared by all three *P. putida* paralogs.

**Thermodynamic/directional consequence.** Because MQO deposits electrons into the quinone pool (high redox potential relative to NAD⁺) rather than reducing NAD⁺, the malate→oxaloacetate reaction becomes **effectively irreversible in the oxidative direction**, in contrast to the readily reversible NAD-MDH. This "pulls" the TCA cycle forward and directly links carbon oxidation to respiratory electron flow. The purified thermophilic *Bacillus* PS3 MQO directly demonstrated menaquinol production that could feed a quinol oxidase, confirming quinone reduction as the physiological output (Kabashima et al., 2013, PMID 23143325).

**Substrate specificity.** The carbon substrate is L-(S)-malate; the acceptor is a respiratory quinone (ubiquinone in aerobic *Pseudomonas*; menaquinone in organisms that use it). This is an inference from the conserved MQO family fold and the UniProt/Rhea catalytic annotation; no paralog-specific kinetic study exists for PP_2925.

---

## 4. Biological Process / Pathway Context

MQO3 operates in **central carbon metabolism**, specifically the **TCA cycle** (KEGG ppu00020; module M00009), and is mapped by KEGG additionally to **pyruvate metabolism** (ppu00620), the **methylcitrate cycle** (M00982), and general **carbon metabolism** (ppu01200). Its reaction sits at the **malate ↔ oxaloacetate node**, a major hub connecting:

- the **oxidative TCA cycle** (fumarate → malate → oxaloacetate → citrate),
- the **glyoxylate shunt** (isocitrate lyase/malate synthase; important during growth on acetyl-CoA-generating substrates), and
- **anaplerosis/gluconeogenesis** (oxaloacetate ↔ PEP/pyruvate via PEP carboxylase, pyruvate carboxylase, malic enzyme, PEP carboxykinase).

This placement is independently confirmed by the **STRING functional-association network** for PP_2925, whose highest-scoring partners are precisely the neighbours of this node: fumarate hydratase (fumC-I/fumC-II, PP_0897; produces MQO's substrate malate), **citrate synthase gltA** (consumes MQO's product oxaloacetate), **malate synthase glcB** (glyoxylate-shunt malate producer), the parallel **NAD-MDH (mdh)**, and the anaplerotic enzymes **PEP carboxylase (ppc), pyruvate carboxylase (pycB), and malic enzyme (maeB)** — together with the two sister paralogs mqo-I and mqo-II (all association scores 0.90–0.94).

Functional relevance in *P. putida* physiology: *P. putida* is an obligately aerobic, metabolically versatile soil bacterium with a strongly **oxidative, respiration-driven metabolism** and a highly active TCA cycle that is central to its catabolism of organic acids and of **aromatic/lignin-derived compounds** (which funnel through acetyl-CoA and the glyoxylate/TCA cycle) (e.g., Zhou et al., 2025, PMID 40883435; Moreno et al., 2024, PMID 38923400). A respiration-coupled malate oxidase such as MQO fits this lifestyle by maximizing the yield of reducing equivalents delivered to the electron-transport chain.

In the related organism *P. aeruginosa*, **mqo is required for growth on ethanol** (which enters metabolism as acetyl-CoA and depends on a functional glyoxylate/TCA cycle to regenerate oxaloacetate) (Görisch, 2003, PMID 12686116) — a concrete example of the physiological importance of MQO-type malate oxidation in pseudomonads.

---

## 5. Subcellular Localization

MQO family enzymes are **peripheral membrane proteins** associated with the cytoplasmic (inner) membrane, from which they can be released by chelators:

> "Mqo is a peripheral membrane protein and can be released from the membrane by addition of chelators." (Molenaar et al., 1998, PMID 9660197)

They are membrane-associated (not integral polytopic membrane proteins) and function at the **cytoplasmic face of the inner membrane**, where the catalytic FAD domain oxidizes cytosolic malate and reduces the membrane quinone pool. In *H. pylori* MQO activity was demonstrated directly in isolated membranes, and the enzyme was described as being — "similar to succinate dehydrogenase" — a shared component of **both the electron transfer chain and the citric acid cycle** (Kather et al., 2000, PMID 10809701). By homology, MQO3 of *P. putida* is expected to localize to the inner membrane and reduce ubiquinone.

**Paralog-specific feature.** Uniquely among the three *P. putida* MQOs, MQO3 carries an **N-terminal ~24-residue extension** (`MKITIKPKLAMAGLALAIGMLNAQAA…`) that has the classic tripartite architecture of a **Sec-type signal peptide** (positively charged n-region KITIKPK; hydrophobic h-region LAMAGLALAIGML; an A-x-A signal-peptidase-I cleavage motif …AQAA↓ET), after which the sequence aligns residue-for-residue with the N-terminus of MQO2. The AlphaFold model (AF-Q88IS4; mean pLDDT 88.8) shows these first ~24 residues are **disordered/very-low-confidence (per-residue pLDDT ~37–49)** and structurally separate from the well-folded FAD-catalytic core (confidence rises sharply at residues ~25–30). This is consistent with a **flexible, membrane-targeting or cleavable N-terminal add-on** distinct from the catalytic domain. *Caveat:* canonical MQOs are cytoplasm-facing peripheral membrane enzymes (they must access the cytoplasmic quinone pool), so genuine periplasmic export is unlikely; the extension is more plausibly a membrane-anchoring/targeting or regulatory segment. UniProt/HAMAP annotate no signal-peptide feature. This should be treated as a bioinformatic hypothesis pending experimental localization.

---

## 6. Evolutionary / Paralog Context

*P. putida* KT2440 encodes **three MQO paralogs** — mqo1/PP_0751 (502 aa), mqo2/PP_1251 (527 aa), mqo3/PP_2925 (539 aa), all assigned KEGG orthology K00116 / EC 1.1.5.4 — **plus a single canonical NAD-dependent MDH** (mdh/PP_0654; K00024; EC 1.1.1.37). Global pairwise alignment shows **mqo3 and mqo2 are recent, close paralogs (78.0% identity)**, whereas mqo1 is more anciently diverged (mqo3–mqo1 50.7%; mqo2–mqo1 48.2%). Thus mqo3 most likely arose by a relatively recent duplication of an mqo2-like ancestor, with the acquisition/retention of its distinctive N-terminal extension as the main sequence divergence. Expansion of MQO gene families is characteristic of metabolically versatile *Pseudomonas*.

The presence of both MQO and NAD-MDH routes implies **functional redundancy** at the malate-oxidation step. In *E. coli*, MQO and MDH are active simultaneously, but Δ*mqo* has no measurable growth or fitness defect while Δ*mdh* is severely impaired — i.e., MQO is dispensable when MDH is present (van der Rest et al., 2000, PMID 11092847). By analogy, MQO3 is expected to be **conditionally used and non-essential** in *P. putida*, rather than the principal malate-oxidizing enzyme, especially given the additional redundancy from mqo1 and mqo2.

---

## 7. Regulation (family-level inference)

MQO expression is tied to respiratory/redox status. In *E. coli*, *mqo* transcription is controlled by the **ArcA-ArcB redox two-component system**, and MQO activity peaks during exponential (respiratory) growth and falls at stationary phase (van der Rest et al., 2000, PMID 11092847). MQO activity is also regulated by carbon/energy source. In *C. glutamicum*, loss of MQO down-regulates TCA-cycle gene expression and **redirects oxaloacetate flux** (e.g., toward L-lysine biosynthesis), illustrating that MQO activity influences the partitioning of the oxaloacetate node (Mitsuhashi et al., 2006, PMID 17090916). Paralog-specific regulation of PP_2925 in *P. putida* has not been experimentally defined.

---

## 8. Supported and Refuted Hypotheses

**Supported:**
- **H1 (primary function):** MQO3 catalyzes FAD-dependent oxidation of L-malate to oxaloacetate with a quinone acceptor (EC 1.1.5.4). *Supported* by UniProt/Rhea catalytic annotation, conserved FAD-binding fingerprint, MQO-family membership, and biochemically characterized homologs (PMID 9660197, 23143325).
- **H2 (localization):** MQO3 is a peripheral, inner-membrane-associated flavoprotein acting at the cytoplasmic face. *Supported* by family biochemistry (PMID 9660197, 10809701).
- **H3 (pathway):** MQO3 sits at the malate↔oxaloacetate node of the TCA/glyoxylate/anaplerotic network, coupling the cycle to respiration. *Supported* by KEGG pathway mapping and STRING network (partners: fumarase, citrate synthase, malate synthase, MDH, Ppc/PycB/MaeB).
- **H4 (evolution/redundancy):** mqo3 is a recent duplicate of mqo2 and functionally redundant with NAD-MDH and the other MQOs. *Supported* by pairwise identity analysis and the *E. coli* Δ*mqo* precedent (PMID 11092847).

**Refuted / down-weighted:**
- **H5 (periplasmic export via the N-terminal signal):** Although MQO3's N-terminal extension has Sec-signal-peptide architecture and is disordered in the AlphaFold model, genuine periplasmic localization is **inconsistent** with the requirement for MQO to reduce the cytoplasmic quinone pool. This hypothesis is down-weighted in favour of a membrane-targeting/regulatory role; it remains untested experimentally.

---

## 9. Evidence Quality and Limitations

- **Strengths:** The core annotation (reaction, cofactor, localization, pathway) rests on decades of biochemical and genetic characterization of the MQO family in *C. glutamicum*, *E. coli*, *H. pylori*, and *Bacillus*, plus fully consistent, curated database records (UniProt HAMAP MF_00212, KEGG, Rhea, InterPro) and independent structural (AlphaFold) and network (STRING) corroboration.
- **Evidence level:** UniProt classifies all three *P. putida* MQO paralogs (Q88IS4/mqo3, Q88NF9/mqo2, Q88PU7/mqo1) at protein-existence level **"3: Inferred from homology"**, with no proteomics cross-references — consistent with the "Probable" designation and the absence of paralog-specific experimental work.
- **Limitations:** No experimental study has directly characterized **PP_2925/MQO3 itself** — kinetics, quinone specificity, exact subcellular topology, the role of the N-terminal extension, and the physiological division of labour among mqo1/mqo2/mqo3 in *P. putida* are all inferred, not measured. The annotation status "Probable" reflects this. High-throughput RB-TnSeq fitness datasets exist for *P. putida* (e.g., PMID 32826213, 33964456) and could, in principle, quantify MQO3's conditional fitness contribution, but paralog-specific values were not extracted here.

## 10. Future Directions

1. Targeted deletion of PP_2925 (and combinatorial Δmqo1/2/3 and Δmdh mutants) to define the division of labour and essentiality at the malate-oxidation step.
2. Enzymatic characterization of purified MQO3 (kinetics, ubiquinone vs. menaquinone specificity, FAD stoichiometry).
3. Experimental determination of subcellular topology and the fate/function of the N-terminal extension (cleavage, membrane anchoring, or regulation).
4. Condition-resolved proteomics to determine which paralog is expressed on which carbon source (organic acids vs. sugars vs. aromatics).

---

### Key References
- Molenaar D, van der Rest ME, Petrović S. Biochemical and genetic characterization of the membrane-associated malate dehydrogenase (acceptor) from *Corynebacterium glutamicum*. **1998** (PMID 9660197).
- van der Rest ME, Frank C, Molenaar D. Functions of the membrane-associated and cytoplasmic malate dehydrogenases in the citric acid cycle of *Escherichia coli*. **2000** (PMID 11092847).
- Kather B, Stingl K, van der Rest ME, Altendorf K, Molenaar D. Another unusual type of citric acid cycle enzyme in *Helicobacter pylori*: the malate:quinone oxidoreductase. **2000** (PMID 10809701).
- Mitsuhashi S, Hayashi M, Ohnishi J, Ikeda M. Disruption of malate:quinone oxidoreductase increases L-lysine production by *Corynebacterium glutamicum*. **2006** (PMID 17090916).
- Kabashima Y, Sone N, Kusumoto T, Sakamoto J. Purification and characterization of malate:quinone oxidoreductase from thermophilic *Bacillus* sp. PS3. **2013** (PMID 23143325).
- Görisch H. The ethanol oxidation system and its regulation in *Pseudomonas aeruginosa*. **2003** (PMID 12686116).
- UniProt Q88IS4; KEGG ppu:PP_2925; Rhea RHEA:46012; AlphaFold AF-Q88IS4; STRING 160488.PP_2925.


## Artifacts

- [OpenScientist final report](mqo3-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](mqo3-deep-research-openscientist_artifacts/final_report.pdf)