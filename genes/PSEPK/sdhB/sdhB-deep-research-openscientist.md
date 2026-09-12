---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T18:52:09.300824'
end_time: '2026-07-11T19:04:50.767780'
duration_seconds: 761.47
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: sdhB
  gene_symbol: sdhB
  uniprot_accession: Q88FA8
  protein_description: 'RecName: Full=Succinate dehydrogenase iron-sulfur subunit
    {ECO:0000256|ARBA:ARBA00022131}; EC=1.3.5.1 {ECO:0000256|ARBA:ARBA00012792};'
  gene_info: Name=sdhB {ECO:0000313|EMBL:AAN69771.1}; OrderedLocusNames=PP_4190 {ECO:0000313|EMBL:AAN69771.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the succinate dehydrogenase/fumarate reductase
  protein_domains: 2Fe-2S_ferredoxin-like_sf. (IPR036010); 4Fe4S_Fe-S-bd. (IPR017896);
    4Fe4S_Fe_S_CS. (IPR017900); Beta-grasp_dom_sf. (IPR012675); Helical_ferredxn.
    (IPR009051)
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
  path: sdhB-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: sdhB-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88FA8
- **Protein Description:** RecName: Full=Succinate dehydrogenase iron-sulfur subunit {ECO:0000256|ARBA:ARBA00022131}; EC=1.3.5.1 {ECO:0000256|ARBA:ARBA00012792};
- **Gene Information:** Name=sdhB {ECO:0000313|EMBL:AAN69771.1}; OrderedLocusNames=PP_4190 {ECO:0000313|EMBL:AAN69771.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the succinate dehydrogenase/fumarate reductase
- **Key Domains:** 2Fe-2S_ferredoxin-like_sf. (IPR036010); 4Fe4S_Fe-S-bd. (IPR017896); 4Fe4S_Fe_S_CS. (IPR017900); Beta-grasp_dom_sf. (IPR012675); Helical_ferredxn. (IPR009051)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "sdhB" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'sdhB' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **sdhB** (gene ID: sdhB, UniProt: Q88FA8) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: **sdhB** (PP_4190, UniProt Q88FA8) in *Pseudomonas putida* KT2440

## Gene/Protein Identity Verification

| Field | Value |
|-------|-------|
| UniProt accession | Q88FA8 |
| Gene name | *sdhB* (ordered locus PP_4190) |
| Protein | Succinate dehydrogenase iron-sulfur subunit |
| EC number | 1.3.5.1 (succinate:quinone oxidoreductase) |
| Organism | *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) |
| Family | Succinate dehydrogenase / fumarate reductase, iron-sulfur (B) subunit |
| Key domains | 2Fe-2S ferredoxin-like (IPR036010); 4Fe-4S Fe-S binding (IPR017896); 4Fe-4S ferredoxin CS (IPR017900); β-grasp (IPR012675); helical ferredoxin (IPR009051) |

**Identity confirmed.** The gene symbol *sdhB*, the "succinate dehydrogenase iron-sulfur subunit" description, the EC 1.3.5.1 assignment, and the diagnostic 2Fe-2S + 4Fe-4S iron-sulfur domain architecture are all mutually consistent and match the highly conserved SdhB/FrdB (subunit B) family. This is an unambiguous, well-characterized protein family. Because no *P. putida*-specific biochemical study of SdhB exists in the searched literature, function is established here from (i) UniProt/InterPro annotation and (ii) primary crystallographic and biochemical studies of the closely homologous bacterial complexes (*E. coli* SQR and QFR, *Wolinella succinogenes* QFR), whose subunit B is structurally and mechanistically equivalent.

---

## 1. Summary (Answer to the Research Question)

SdhB is the **iron-sulfur subunit of succinate:quinone oxidoreductase (respiratory Complex II / succinate dehydrogenase, EC 1.3.5.1)**. Together with the flavoprotein subunit SdhA it forms the soluble catalytic head of the complex, which is peripherally attached to the **cytoplasmic (inner/matrix) face of the bacterial inner membrane** via the integral membrane cytochrome subunit(s) SdhC(/SdhD). SdhB's specific molecular role is **electron conduction**: it carries a linear chain of three iron-sulfur clusters ([2Fe-2S], [4Fe-4S], [3Fe-4S]) that wires electrons, one at a time, from the FAD/succinate-oxidation site in SdhA to the membrane quinone-reduction site, thereby coupling **succinate → fumarate oxidation (a TCA-cycle step) to quinone → quinol reduction (feeding the aerobic respiratory chain)**.

---

## 2. Primary Function: the Catalyzed Reaction and Substrate Specificity

The holoenzyme catalyzes the reversible reaction (EC 1.3.5.1):

> **succinate + quinone ⇌ fumarate + quinol**

Membrane-bound succinate:quinone reductases (SQR, Complex II) and the related quinol:fumarate reductases (QFR) "couple the oxidation of succinate to fumarate to the reduction of quinone to quinol and also catalyse the reverse reaction" [Lancaster & Kröger 2000, PMID 11004459]. The two enzyme classes "are collectively referred to as succinate:quinone oxidoreductases (EC 1.3.5.1), have very similar compositions and are predicted to share similar structures" [PMID 11004459].

**Substrate specificity / division of labor within the complex:**
- The **dicarboxylate substrate (succinate/fumarate)** is bound and oxidized/reduced at the covalently bound **FAD in subunit A (SdhA)**, not in SdhB. "Subunit A contains the site of fumarate reduction and a covalently bound flavin adenine dinucleotide prosthetic group. Subunit B contains three iron-sulphur centres" [Lancaster et al. 1999, *Nature*, PMID 10586875].
- **SdhB's "substrate" is the electron itself.** It provides the physical conduit of three Fe-S clusters that transfer electrons from FAD to the quinone. In the intact complex "the cofactors are arranged in a nearly linear manner from the membrane-bound quinone to the active site flavin" [Iverson et al. 1999, *Science*, PMID 10373108].
- The distal end of SdhB, together with the membrane anchor, forms part of the **quinone-binding site**. In *E. coli* SQR the residue SdhB(G227) lies at the entrance of the water channel/quinone pocket [Cheng et al. 2008, PMID 18690748], and quinone binding is mediated by hydrogen bonding to a conserved tyrosine at the interface [Horsefield et al. 2006, PMID 16407191].

Thus SdhB does not itself possess dicarboxylate substrate specificity; its molecular specificity is for **single-electron transfer** along a defined redox gradient toward ubiquinone (the physiological acceptor in aerobic *P. putida*).

---

## 3. Cofactor Content and Electron-Transfer Mechanism

SdhB harbors **three iron-sulfur centres**, the defining feature of the B subunit [PMID 11004459; PMID 10586875]:
1. A **[2Fe-2S]** cluster (2Fe-2S ferredoxin-like domain, IPR036010) — proximal, adjacent to the FAD of SdhA.
2. A **[4Fe-4S]** cluster (4Fe-4S Fe-S binding domain, IPR017896/IPR017900) — central.
3. A **[3Fe-4S]** cluster — distal, near the quinone-binding site at the membrane interface.

These clusters form a nearly linear relay spanning ~40 Å, enabling sequential electron hops from FAD to quinone [PMID 10373108]. Crucially, the redox potentials of this arrangement are tuned to **minimize electron leakage**: Yankovskaya et al. determined the *E. coli* SQR structure and found "the SQR redox centers are arranged in a manner that aids the prevention of reactive oxygen species (ROS) formation at the flavin adenine dinucleotide. This is likely to be the main reason SQR is expressed during aerobic respiration rather than the related enzyme fumarate reductase, which produces high levels of ROS" [Yankovskaya et al. 2003, *Science*, PMID 12560550]. The eukaryotic SDHB subunit likewise "is required for succinate oxidation" and is the subunit critical in driving/controlling mitochondrial ROS generation [Sun et al. 2020, PMID 32371258], underscoring the conserved role of this Fe-S wire.

**Biogenesis note:** correct incorporation of Fe-S clusters into the B subunit is essential for a functional, stable protein. In the human ortholog, dedicated assembly factors deliver Fe-S clusters to SDHB, and failure "impairs biogenesis of holo-SDHB and results in ... degradation of SDHB" [Maio et al. 2016, PMID 26749241]. While *P. putida* uses bacterial ISC/SUF Fe-S machinery rather than the mitochondrial factors, the principle that SdhB requires post-translational Fe-S cluster loading to be active is general.

---

## 3a. Direct Sequence-Level Evidence for the KT2440 Protein

To move beyond database annotation, the KT2440 SdhB sequence (Q88FA8, 234 aa) was retrieved and aligned to the crystallographically-characterized *E. coli* SdhB (P07014, 238 aa):

- **73.1% amino-acid identity** (Needleman–Wunsch global alignment; 69% over the 248-residue alignment) — far above the ~30% threshold for confident functional orthology.
- **All 11 iron-sulfur cluster cysteine ligands are strictly conserved and in identical order:** P. putida Cys 53, 58, 73, 145, 148, 150, 151, 155, 202, 208, 212 correspond one-to-one to E. coli Cys 55, 60, 75, 149, 152, 154, 155, 159, 206, 212, 216.
- The **N-terminal [2Fe-2S] ferredoxin motif** (`CREGVCGSDG…NMNGKNGLACIT`) is **identical** between the two species.
- The **C-terminal bacterial di-ferredoxin motif** that ligates the [4Fe-4S] and [3Fe-4S] clusters and lies adjacent to the quinone site (`YECILCACCSTSCPSF`) is **identical**, and the second motif (`RC..IMNC..VCPKG`) is nearly identical.

This constitutes direct, protein-specific evidence (not merely transferred annotation) that KT2440 SdhB has the same three-cluster ligation scheme and therefore the same electron-relay mechanism as the structurally-defined *E. coli* Complex II subunit. Consistent with the SDHB subfamily, the sequence contains **no signal peptide or transmembrane segment**, confirming it is a soluble/peripheral subunit.

## 4. Subcellular Localization

SdhB is a **peripheral (extrinsic) membrane protein on the cytoplasmic face of the *P. putida* inner (cytoplasmic) membrane**. It is not itself membrane-integral (it has no signal peptide or transmembrane helix; the SDHB subfamily is "without a signal peptide" [PMID 32371258]) but is held at the membrane through:
- its tight association with SdhA (forming the soluble catalytic dimer), and
- the docking of that dimer onto the integral membrane subunit(s) SdhC(/SdhD), which contain the transmembrane helices and heme b and constitute the quinone-binding, membrane-embedded module [PMID 11004459; PMID 12560550].

The overall complex therefore places the succinate-oxidation and Fe-S electron-relay chemistry in the cytoplasm, immediately adjacent to the membrane quinone pool—consistent with its electroneutral operation in which "the quinone reduction reaction must consume cytoplasmic protons which are released stoichiometrically during succinate oxidation" [Cheng et al. 2008, PMID 18690748].

---

## 4a. Genomic Context: the sdhCDAB Operon (KT2440-specific evidence)

KEGG genome annotation of *P. putida* KT2440 shows that PP_4190 (*sdhB*) sits in a contiguous, same-strand (complement) gene block encoding the **complete Complex II** plus the adjacent 2-oxoglutarate dehydrogenase genes:

| Locus | Product | Complex II role |
|-------|---------|-----------------|
| PP_4193 | SDH cytochrome b-556 subunit | **SdhC** (membrane anchor, heme *b*, quinone site) |
| PP_4192 | SDH hydrophobic membrane anchor | **SdhD** (membrane anchor, quinone site) |
| PP_4191 | SDH flavoprotein subunit | **SdhA** (FAD, succinate oxidation) |
| **PP_4190** | **SDH iron-sulfur subunit** | **SdhB (this protein), 4735881–4736585 (705 bp = 234 aa)** |
| PP_4189 | 2-oxoglutarate decarboxylase E1 | SucA (2-OG dehydrogenase) |
| PP_4188 | dihydrolipoyltranssuccinylase E2 | SucB |
| PP_4187 | dihydrolipoyl dehydrogenase E3 | Lpd |

Key implications:
- **All four Complex II subunits are encoded** (membrane cytochrome-*b*/quinone module SdhC+SdhD and the soluble catalytic SdhA+SdhB dimer) → KT2440 possesses an intact, membrane-bound succinate:ubiquinone oxidoreductase.
- Gene order **sdhC–sdhD–sdhA–sdhB** is the canonical *sdhCDAB* arrangement conserved with *E. coli*; **SdhA immediately precedes SdhB**, consistent with their assembly into the FAD-flavoprotein/iron-sulfur catalytic dimer.
- The tight genomic linkage of *sdhCDAB* to the **2-oxoglutarate dehydrogenase complex (sucAB) and shared E3 (lpd)** mirrors the classic bacterial TCA-cycle operon and implies co-regulation of two sequential citric-acid-cycle steps, firmly placing SdhB's succinate-oxidation activity within the citric acid cycle in vivo.

## 5. Biochemical Pathways and Physiological Role

SdhB sits at the **junction of two pathways**:

1. **Tricarboxylic acid (TCA / citric acid) cycle** — the SdhA·SdhB catalytic head performs the succinate → fumarate oxidation step of the cycle. In *P. putida* KT2440 the citric acid cycle is a core, tightly regulated component of central carbon metabolism [Sudarsan et al. 2014, PMID 24951791]. *P. putida* is a metabolically versatile obligate aerobe that channels carbon (from sugars via the Entner–Doudoroff route, and from many aromatic/organic-acid substrates) into the TCA cycle, making succinate dehydrogenase an important node of central metabolic flux.

2. **Aerobic respiratory electron-transport chain** — the electrons removed from succinate are passed by SdhB's Fe-S chain into the **membrane ubiquinone pool**, which then feeds downstream respiratory complexes (cytochrome bc1 / terminal oxidases) to reduce O₂ and generate proton-motive force. Complex II is thus the physical, non-proton-pumping link that couples the TCA cycle directly to aerobic respiration [PMID 12560550; PMID 11004459].

By carrying out succinate oxidation while its redox centers are poised to avoid ROS production, SdhB (as part of SQR) is specifically adapted to *P. putida*'s **aerobic lifestyle**, in contrast to the ROS-prone fumarate reductase used in anaerobic respiration [PMID 12560550].

**KEGG pathway-level confirmation (KT2440-specific).** KEGG assigns PP_4190 to orthology **K00240** ("succinate dehydrogenase iron-sulfur subunit [EC:1.3.5.1]"; EC 1.3.5.1 = oxidoreductase acting on the CH–CH group of donors with a quinone as acceptor). Critically, sdhB is listed **simultaneously in the Citrate cycle map (ppu00020) and the Oxidative phosphorylation map (ppu00190)** — the formal database statement of its dual role as the single reaction shared by the TCA cycle and the respiratory chain. It belongs to module **M00149 "Succinate dehydrogenase, prokaryotes" (SdhABCD)** and to TCA modules M00009 and M00011 (2-oxoglutarate ⇒ oxaloacetate). Additional membership in the butanoate (ppu00650) and methylcitrate-cycle (M00982) maps reflects that succinate–fumarate interconversion also connects to propionate/short-chain-carbon metabolism in the metabolically versatile *P. putida*.

---

## 6. Supported vs. Refuted Hypotheses

**Supported**
- H1: SdhB is the iron-sulfur (B) subunit of Complex II (SQR), part of EC 1.3.5.1. **Strongly supported** (UniProt/InterPro + homologous structures).
- H2: SdhB's molecular role is electron conduction via three Fe-S clusters, not dicarboxylate catalysis (which occurs at SdhA/FAD). **Strongly supported** [PMID 10586875, 10373108].
- H3: The complex is localized to the cytoplasmic face of the inner membrane, coupling TCA cycle to aerobic respiratory chain. **Supported** [PMID 12560550, 18690748, 24951791].
- H4: Fe-S center arrangement is tuned to suppress ROS, favoring aerobic expression. **Supported** [PMID 12560550].

**Refuted / not supported**
- That SdhB itself binds/oxidizes the dicarboxylate substrate — **refuted**; the FAD/dicarboxylate site is in SdhA [PMID 10586875].
- That SdhB is an integral membrane protein — **refuted**; the SDHB subfamily lacks a signal peptide/TM domain and is peripheral [PMID 32371258].

---

## 7. Limitations and Future Directions

- **No *P. putida* KT2440-specific biochemical/structural study** of SdhB was found; direct mechanistic and structural evidence is from homologs (*E. coli*, *W. succinogenes*, eukaryotic SDHB). This gap is mitigated by three independent organism-specific lines of evidence assembled here — 73% sequence identity with all 11 Fe-S cysteine ligands conserved, an intact canonical *sdhCDAB* operon, and KEGG K00240/EC 1.3.5.1 pathway mapping — so transfer of function is well justified; nonetheless, direct EPR/kinetic/structural characterization of the KT2440 enzyme would confirm cluster identities and midpoint potentials.
- The exact **quinone species** used in *Pseudomonas* (ubiquinone-9) and the **transcriptional regulation** of the KT2440 *sdhCDAB–sucAB* locus were not experimentally examined here (the operon gene organization was confirmed from the KEGG genome annotation).
- Future work: verify the three Fe-S cluster types by EPR in the KT2440 enzyme, define the SdhB–SdhA and SdhB–SdhC/D interfaces, and quantify Complex II flux under aerobic vs. carbon-limited growth.

---

### Key References
- Lancaster & Kröger 2000, *Biochim Biophys Acta* — PMID 11004459
- Lancaster et al. 1999, *Nature* (W. succinogenes QFR structure) — PMID 10586875
- Iverson et al. 1999, *Science* (E. coli QFR structure) — PMID 10373108
- Yankovskaya et al. 2003, *Science* (E. coli SQR / Complex II structure, ROS) — PMID 12560550
- Horsefield et al. 2006 (quinone-binding site) — PMID 16407191
- Cheng et al. 2008 (proton/quinone channel, SdhB G227) — PMID 18690748
- Sun et al. 2020 (SDHB subunit, Fe-S domains, ROS) — PMID 32371258
- Maio et al. 2016 (Fe-S delivery to SDHB) — PMID 26749241
- Sudarsan et al. 2014 (P. putida KT2440 central carbon metabolism) — PMID 24951791


## Artifacts

- [OpenScientist final report](sdhB-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](sdhB-deep-research-openscientist_artifacts/final_report.pdf)