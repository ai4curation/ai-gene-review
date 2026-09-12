---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T15:13:18.989152'
end_time: '2026-07-11T15:32:39.857492'
duration_seconds: 1160.87
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: opgH
  gene_symbol: opgH
  uniprot_accession: Q88D04
  protein_description: 'RecName: Full=Glucans biosynthesis glucosyltransferase H {ECO:0000255|HAMAP-Rule:MF_01072};
    EC=2.4.1.- {ECO:0000255|HAMAP-Rule:MF_01072};'
  gene_info: Name=opgH {ECO:0000255|HAMAP-Rule:MF_01072}; Synonyms=mdoH; OrderedLocusNames=PP_5025;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the glycosyltransferase 2 family. OpgH
  protein_domains: Glucans_biosynth_gluTrFase_H. (IPR023725); Glyco_trans_2-like.
    (IPR001173); Glycosyltr_2/OpgH_subfam. (IPR050321); Nucleotide-diphossugar_trans.
    (IPR029044); Glycos_transf_2 (PF00535)
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
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: opgH-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: opgH-deep-research-openscientist_artifacts/final_report.pdf
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
- **UniProt Accession:** Q88D04
- **Protein Description:** RecName: Full=Glucans biosynthesis glucosyltransferase H {ECO:0000255|HAMAP-Rule:MF_01072}; EC=2.4.1.- {ECO:0000255|HAMAP-Rule:MF_01072};
- **Gene Information:** Name=opgH {ECO:0000255|HAMAP-Rule:MF_01072}; Synonyms=mdoH; OrderedLocusNames=PP_5025;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the glycosyltransferase 2 family. OpgH
- **Key Domains:** Glucans_biosynth_gluTrFase_H. (IPR023725); Glyco_trans_2-like. (IPR001173); Glycosyltr_2/OpgH_subfam. (IPR050321); Nucleotide-diphossugar_trans. (IPR029044); Glycos_transf_2 (PF00535)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "opgH" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'opgH' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **opgH** (gene ID: opgH, UniProt: Q88D04) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: OpgH (Q88D04, PP_5025) in *Pseudomonas putida* KT2440

**Gene:** *opgH* (synonym *mdoH*; ordered locus PP_5025)
**Protein:** Glucans biosynthesis glucosyltransferase H
**UniProt:** Q88D04
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440)
**EC:** 2.4.1.– | **Family:** Glycosyltransferase family 2 (GT2), OpgH subfamily | **Pfam:** PF00535 (Glycos_transf_2) | **HAMAP:** MF_01072

---

## Summary

OpgH (Q88D04, encoded by PP_5025) in *Pseudomonas putida* KT2440 is a **polytopic inner (cytoplasmic) membrane glycosyltransferase of family GT2 (EC 2.4.1.–)** that catalyzes the committed, backbone-polymerizing step of **osmoregulated periplasmic glucan (OPG)** biosynthesis. Using cytoplasmic **UDP-glucose** as the sugar donor, OpgH assembles a β-linked polyglucose chain at the cytoplasmic face of the inner membrane and is topologically positioned to translocate the nascent glucan into the periplasm. There, its operon partner **OpgG** — recently defined as a β-1,2-glucanase of the new glycoside hydrolase family GH186 — processes and shapes the polymer. In *Pseudomonas*, the mature OPGs are neutral, highly branched glucans of 6–13 glucose units linked by **β-1,2 bonds (backbone) and β-1,6 bonds (branches)**, whose abundance rises at low osmolarity — the defining hallmark of OPGs.

The physiological role of the OpgH product is that of a **periplasmic envelope component involved in osmotic and periplasmic-volume adaptation, membrane and detergent/antibiotic resistance, and Rcs-mediated envelope-stress signaling**. Loss of OPG synthesis (via *opgH*/*mdoH* mutation) produces a pleiotropic envelope phenotype, sensitizes cells to SDS, perturbs the periplasmic Donnan potential, and de-represses colanic-acid capsule synthesis through the RcsC sensor. In enterobacteria and *Pseudomonas syringae*, the *opgGH* (*mdoGH* / *hrpM*) locus is additionally required for full virulence, linking periplasmic glucans to host interaction. Beyond its enzymatic role, OpgH **moonlights** in *E. coli* as a nutrient-dependent antagonist of the cell-division protein **FtsZ**, using UDP-glucose as a proxy for nutritional status to couple cell size to central metabolism.

An important disambiguation was resolved during this investigation: OpgH is **distinct** from a separately encoded *P. putida* KT2440 BcsA-like "orphan" protein that synthesizes **cyclic-β-1,3-glucan** via a fused GT2–GH17 architecture. OpgH is a single-GT2-domain OpgH-subfamily enzyme producing β-1,2/β-1,6 OPGs, whereas the orphan synthase is a two-domain enzyme producing a different polymer. The two therefore represent **two independent periplasmic glucan pathways** in the same organism. Finally, note that the specific functional assignment for PP_5025 rests on **strong orthology** to biochemically characterized *E. coli* and *Pseudomonas* OpgH/MdoH proteins rather than on direct experimental study of the *P. putida* protein itself — the annotation is confident but inferential, and gene symbol, organism, GT2/OpgH family, and Pfam PF00535 all match the OPG glucosyltransferase, confirming this is the correct target.

---

## Key Findings

### F001 — OpgH is a GT2-family inner-membrane glucosyltransferase that polymerizes the OPG glucose backbone from UDP-glucose

*P. putida* OpgH belongs to **glycosyltransferase family 2** (Pfam PF00535; HAMAP rule MF_01072), the family that defines its enzymatic class. The reaction it catalyzes is the transfer of glucose from the nucleotide-sugar donor **UDP-glucose** onto a growing glucan chain, building the polysaccharide backbone of osmoregulated periplasmic glucans. This activity is best defined through its biochemically characterized orthologs. In *Yersinia pseudotuberculosis*, the *opgGH* operon "encodes glucosyltransferases that synthesize osmoregulated periplasmic glucans (OPGs) from UDP-glucose, using acyl carrier protein (ACP) as a cofactor" [PMID: 26150539](https://pubmed.ncbi.nlm.nih.gov/26150539/) — this single statement pins down substrate (UDP-glucose), product (OPGs), cofactor (ACP), and enzymatic class. Direct biochemical evidence comes from *E. coli*, where "mutants lacking MdoH are deficient in a glucosyltransferase activity assayed in vitro" [PMID: 9352918](https://pubmed.ncbi.nlm.nih.gov/9352918/), and where MdoH "presence was shown to be necessary for normal glucosyl transferase activity" [PMID: 7934824](https://pubmed.ncbi.nlm.nih.gov/7934824/). Because Q88D04 is a clear ortholog carrying the same catalytic GT2 domain and HAMAP signature, the same reaction is assigned to the *P. putida* enzyme.

**Reaction (backbone synthesis):** UDP-glucose + [β-glucan]ₙ → UDP + [β-glucan]ₙ₊₁. **Substrate specificity:** sugar donor = UDP-glucose; acceptor = the elongating β-glucan chain; the product backbone is β-1,2-linked glucose (see F003, F004). **Enzyme classification:** GT2 family (nucleotide-diphospho-sugar transferase fold, IPR029044); EC 2.4.1.– hexosyltransferase.

### F002 — OpgH is a polytopic inner-membrane protein with a large cytoplasmic catalytic domain positioned to translocate nascent glucan to the periplasm

The membrane topology of the OpgH ortholog MdoH (847 aa in *E. coli*) was experimentally mapped using **51 different MdoH–β-lactamase fusions**, which showed that "the MdoH protein crosses the cytoplasmic membrane eight times, with the N and C termini in the cytoplasm" [PMID: 9352918](https://pubmed.ncbi.nlm.nih.gov/9352918/). Critically, a large **~310-amino-acid cytoplasmic domain** lies between the second and third transmembrane segments and carries the catalytic (glucosyltransferase) function — consistent with the enzyme drawing on cytoplasmic UDP-glucose. The topological model further "suggests that this protein could be directly involved in the **translocation of nascent polyglucose chains to the periplasmic space**" [PMID: 9352918](https://pubmed.ncbi.nlm.nih.gov/9352918/), implying a dual polymerization/translocation role. In *Pseudomonas*, the ortholog is likewise "a 97 kDa protein spanning the cytoplasmic membrane" [PMID: 7934824](https://pubmed.ncbi.nlm.nih.gov/7934824/). This places OpgH's catalysis on the cytoplasmic face of the inner membrane, with the polymer destined for the periplasm. The partner OpgG is a periplasmic ~56 kDa protein that matures the glucan there (F003).

### F003 — OpgH acts with the periplasmic partner OpgG; OpgG/OpgD are β-1,2-glucanases (new family GH186) that shape the glucan

*opgH* is the second gene of the **opgGH (mdoGH) operon**, and OpgG is a ~56 kDa **periplasmic** protein whose function was long undefined [PMID: 7934824](https://pubmed.ncbi.nlm.nih.gov/7934824/). Recent structural and functional work resolved it: analyses of *E. coli* OpgG and OpgD "revealed that these proteins are **β-1,2-glucanases** with remarkably different activity from each other, establishing a new glycoside hydrolase family, **GH186**" [PMID: 37735577](https://pubmed.ncbi.nlm.nih.gov/37735577/). Because OpgG hydrolyzes β-1,2 linkages, the backbone made by OpgH is inferred to be **β-1,2-linked glucose**, which OpgG then trims/shapes in the periplasm. The synthesis–hydrolysis logic is reinforced in *Caulobacter*, where OpgH (synthesis) and BglX (hydrolysis) together define an OPG pathway producing a **cyclic hexamer of glucose** [PMID: 36516849](https://pubmed.ncbi.nlm.nih.gov/36516849/). Thus OpgH does not act alone: it initiates and polymerizes, while periplasmic glucanases (OpgG/OpgD, or BglX) determine final chain length and architecture. Downstream substituent transferases (e.g., OpgC succinylation in enterobacteria; [PMID: 26790533](https://pubmed.ncbi.nlm.nih.gov/26790533/)) may decorate the backbone in some species.

### F004 — In *Pseudomonas*, OPGs are branched β-1,2/β-1,6 glucans, and the *opgGH*/*mdoGH* locus corresponds to the *hrpM* pathogenicity locus

Chemical characterization of the periplasmic glucans of *Pseudomonas syringae* pv. *syringae* showed they are "**neutral, unsubstituted, and composed solely of glucose**," 6–13 glucose units in size, and that "the glucans are **linked by beta-1,2 and beta-1,6 glycosidic bonds**" — a highly branched structure with a β-1,2 backbone and β-1,6 branches [PMID: 7961404](https://pubmed.ncbi.nlm.nih.gov/7961404/). These glucans are osmoregulated: "these periplasmic glucans were more abundant when the osmolarity of the growth medium was lower" [PMID: 7961404](https://pubmed.ncbi.nlm.nih.gov/7961404/). This defines the exact product class expected for *P. putida* OpgH — a neutral, branched pseudomonad-type glucan, contrasting with the anionic, substituted *E. coli* MDO. Furthermore, the *E. coli mdoGH* operon shares "**a considerable homology (69% identical nucleotides out of 2816)**" with the two genes at the *hrpM* locus of *Pseudomonas syringae* pv. *syringae*, a locus required for pathogenicity and the plant hypersensitive reaction [PMID: 7934824](https://pubmed.ncbi.nlm.nih.gov/7934824/). This directly links the glucosyltransferase operon to a pseudomonad host-interaction function.

### F005 — OPGs made by OpgH are periplasmic envelope components required for osmotic adaptation, membrane/detergent resistance, and Rcs-mediated signaling

OPGs are periplasmic oligosaccharides that are "modulated during osmotic fluxes" and constitute intrinsic envelope components (review [PMID: 28593831](https://pubmed.ncbi.nlm.nih.gov/28593831/)). Their loss is pleiotropic: "mutants defective in OPG synthesis have a highly pleiotropic phenotype, indicative of an overall alteration of their envelope properties" [PMID: 10779706](https://pubmed.ncbi.nlm.nih.gov/10779706/). A precise phenotype is detergent resistance: "wild-type *E. coli* MC4100 grew in the presence of **10% SDS** whereas isogenic *mdoA* and *mdoB* mutants could not grow above **0.5% SDS**" [PMID: 12798996](https://pubmed.ncbi.nlm.nih.gov/12798996/) — a 20-fold sensitization. OPGs also shape periplasmic physical chemistry: as highly anionic (in enterobacteria) polymers they generate a **Donnan potential** that concentrates cations and contributes to periplasmic volume regulation [PMID: 12379178](https://pubmed.ncbi.nlm.nih.gov/12379178/), and MDOs are proposed to "play a key role in periplasmic volume regulation at low-to-moderate osmolality" [PMID: 10733957](https://pubmed.ncbi.nlm.nih.gov/10733957/). Finally, periplasmic OPG levels feed into envelope-stress signaling: inactivation of *mdoH* increases colanic-acid capsule via the Rcs system because "the periplasmic levels of MDOs act to signal RcsC to activate *cps* expression" [PMID: 9352941](https://pubmed.ncbi.nlm.nih.gov/9352941/). Reviews connect periplasmic OPGs to signal transduction that indirectly regulates virulence, and secreted OPGs to antibiotic and host-cell interactions [PMID: 26265506](https://pubmed.ncbi.nlm.nih.gov/26265506/).

### F006 — OpgH moonlights as a nutrient-dependent FtsZ antagonist that couples cell size to central metabolism

Beyond making glucan, OpgH has a second, "moonlighting" function established in *E. coli*: it is "a **nutrient-dependent regulator of *E. coli* cell size**." Under nutrient-rich growth, "OpgH localizes to the nascent septal site, where it **antagonizes assembly of the tubulin-like cell division protein FtsZ**, delaying division and increasing cell size," a mechanism consistent with OpgH sequestering FtsZ from growing polymers [PMID: 23935518](https://pubmed.ncbi.nlm.nih.gov/23935518/). The molecular link to metabolism is UDP-glucose: the work highlights "the conservation of uridine diphosphate glucose as a proxy for nutrient status and the use of **moonlighting enzymes to couple growth rate-dependent phenomena to central metabolism**" [PMID: 23935518](https://pubmed.ncbi.nlm.nih.gov/23935518/). This is independently corroborated: "OpgH also **sequesters FtsZ** in order to regulate cell size according to nutrient availability," and Δ*opgGH* cells are smaller [PMID: 26150539](https://pubmed.ncbi.nlm.nih.gov/26150539/). Whether the *P. putida* ortholog retains this moonlighting role has not been directly tested, but the shared UDP-glucose-binding GT2 architecture makes it plausible.

### F007 — OpgH is distinct from the co-existing *P. putida* KT2440 cyclic-β-1,3-glucan synthase (a BcsA-like "orphan"); two separate periplasmic glucan pathways

This finding resolves a potential misidentification. *P. putida* KT2440 encodes a **BcsA-like "orphan" protein** that bioinformatic and structural modeling describes as "a two-domain transmembrane ovoid-like structure ... with a periplasmic **glycosyl hydrolase family GH17 domain** linked via a transmembrane region to a **cytoplasmic glycosyltransferase family GT2 domain**" [PMID: 37267309](https://pubmed.ncbi.nlm.nih.gov/37267309/). The proposed mechanism is that "the **GT2 domain synthesises β-(1,3)-glucan** that is transferred to the GH17 domain where it is cleaved and cyclised to produce **cyclic-β-(1,3)-glucan (CβG)**" [PMID: 37267309](https://pubmed.ncbi.nlm.nih.gov/37267309/). This enzyme shares <41% identity with cellulose synthase BcsA and is **architecturally and product-wise distinct from OpgH**: OpgH is a single-GT2-domain, OpgH-subfamily membrane glucosyltransferase (HAMAP MF_01072; PF00535) that produces β-1,2/β-1,6 osmoregulated periplasmic glucans in partnership with periplasmic OpgG. Thus, *P. putida* KT2440 possesses **two separate periplasmic glucan pathways**: the OpgGH OPG pathway (branched β-1,2/β-1,6 glucans) and the orphan CβG pathway (cyclic β-1,3-glucan). Q88D04/PP_5025 is the OPG pathway enzyme, and the two should not be conflated.

---

## Mechanistic Model / Interpretation

The evidence assembles into a coherent, spatially organized model of OpgH function at the *P. putida* inner membrane:

```
   CYTOPLASM                          INNER MEMBRANE                    PERIPLASM
 ------------------------------------------------------------------------------------

  UDP-glucose ---->  [ OpgH cytoplasmic GT2 domain ]
   (donor, and       (~310 aa catalytic loop between TM2 and TM3)
   nutrient proxy)          |
                            | polymerize beta-1,2 backbone
                            v
                    ====== OpgH (8 TM segments) ======  --translocate-->  nascent
                            N- and C-termini cytoplasmic                   beta-glucan
                                                                              |
                                                                              v
                                                            [ OpgG / OpgD : GH186 beta-1,2-glucanase ]
                                                             trims, shapes, branches (beta-1,6)
                                                                              |
                                                                              v
                                                            Mature OPG: neutral, branched
                                                            beta-1,2 / beta-1,6 glucan (6-13 Glc)
                                                            Osmoregulated (up at low osmolarity)

  MOONLIGHTING (nutrient-rich):
  UDP-glucose high --> OpgH at septum --> sequesters FtsZ --> delays division --> larger cells
```

**Primary function (enzymatic).** OpgH is the backbone-building enzyme of OPG biosynthesis. It binds cytoplasmic UDP-glucose at its large cytoplasmic GT2 domain (F001, F002) and transfers glucose to a growing chain, forming a β-1,2 backbone (F003, F004). Its eight-times-membrane-spanning topology positions it to hand the nascent chain across the inner membrane into the periplasm (F002).

**Maturation (partner enzymes).** OpgG (and its paralog OpgD), acting as a periplasmic GH186 β-1,2-glucanase, processes the nascent polymer to yield the final OPG species (F003). In *Pseudomonas*, the finished product is a neutral, branched β-1,2/β-1,6 glucan of 6–13 glucose units, more abundant at low osmolarity (F004).

**Localization.** Catalysis begins on the **cytoplasmic face of the inner membrane**; the finished polymer resides in the **periplasm** where it performs its physiological work (F002, F003, F005).

**Downstream physiology.** As a bulky, abundant periplasmic solute, OPGs regulate periplasmic osmotic/volume balance and Donnan potential, maintain envelope integrity (SDS/antibiotic resistance), and, through their concentration, act as an input to Rcs envelope-stress signaling that governs capsule, motility, biofilm, and — in pathogens — virulence (F005). In *Pseudomonas syringae*, the operon corresponds to the *hrpM* pathogenicity locus (F004).

**Metabolic coupling (moonlighting).** Because OpgH senses UDP-glucose, it doubles as a nutrient gauge; under rich conditions it sequesters FtsZ at the septum to enlarge cells, coupling division timing to central metabolism (F006).

The following table summarizes the two distinct glucan systems in *P. putida* KT2440 and situates OpgH:

| Feature | **OpgH / OpgGH (PP_5025, Q88D04)** | Orphan BcsA-like synthase |
|---|---|---|
| Architecture | Single GT2 domain, 8 TM segments | Fused GT2 (cytoplasmic) + GH17 (periplasmic) |
| Product | Branched β-1,2 / β-1,6 OPGs (6–13 Glc) | Cyclic β-1,3-glucan (CβG) |
| Donor | UDP-glucose | UDP-glucose |
| Partner | Periplasmic OpgG/OpgD (GH186 glucanase) | Intramolecular GH17 domain |
| Regulation | Osmoregulated (↑ low osmolarity) | Not characterized |
| Evidence | Orthology + biochemistry of MdoH/OpgH | Bioinformatics/structural modeling |

---

## Evidence Base

| PMID | Title (abbrev.) | How it supports the annotation |
|---|---|---|
| [9352918](https://pubmed.ncbi.nlm.nih.gov/9352918/) | Topological analysis of MdoH | Direct biochemistry: MdoH mutants lack glucosyltransferase activity; 8-TM topology; large cytoplasmic catalytic domain; implicated in glucan translocation |
| [26150539](https://pubmed.ncbi.nlm.nih.gov/26150539/) | *opgGH* in *Yersinia* | States substrate (UDP-glucose), product (OPGs), cofactor (ACP); confirms FtsZ-sequestration/cell-size role |
| [7934824](https://pubmed.ncbi.nlm.nih.gov/7934824/) | *mdoA*/*hrpM* homology | MdoH necessary for glucosyltransferase activity; 97 kDa membrane protein; OpgG periplasmic; links operon to *Pseudomonas hrpM* pathogenicity |
| [37735577](https://pubmed.ncbi.nlm.nih.gov/37735577/) | OpgG/OpgD enzymology | Defines OpgG/OpgD as β-1,2-glucanases (new family GH186), implying β-1,2 backbone |
| [7961404](https://pubmed.ncbi.nlm.nih.gov/7961404/) | *P. syringae* periplasmic glucans | Chemical structure: neutral, β-1,2/β-1,6-linked, 6–13 Glc, osmoregulated |
| [36516849](https://pubmed.ncbi.nlm.nih.gov/36516849/) | EstG/OpgH/BglX in *Caulobacter* | OpgH (synthesis) + glucanase (hydrolysis) pathway; cyclic hexamer OPG product |
| [12798996](https://pubmed.ncbi.nlm.nih.gov/12798996/) | MDOs and SDS resistance | *mdoH* mutants: 20-fold SDS sensitization — envelope-integrity role |
| [9352941](https://pubmed.ncbi.nlm.nih.gov/9352941/) | *mdoH* and colanic acid | Periplasmic MDO levels signal via RcsC to control capsule |
| [23935518](https://pubmed.ncbi.nlm.nih.gov/23935518/) | Moonlighting enzyme/cell size | OpgH sequesters FtsZ; UDP-glucose as nutrient proxy |
| [12379178](https://pubmed.ncbi.nlm.nih.gov/12379178/) | Periplasmic Ca²⁺/Donnan | MDOs generate Donnan potential concentrating periplasmic cations |
| [10733957](https://pubmed.ncbi.nlm.nih.gov/10733957/) | Turgor/periplasmic water | MDOs proposed key to periplasmic volume regulation |
| [10779706](https://pubmed.ncbi.nlm.nih.gov/10779706/) | OPGs in Proteobacteria | OPG-deficient mutants have pleiotropic envelope alteration |
| [28593831](https://pubmed.ncbi.nlm.nih.gov/28593831/) | OPG review | OPGs modulated during osmotic fluxes; core envelope osmoadaptation |
| [26265506](https://pubmed.ncbi.nlm.nih.gov/26265506/) | OPG biological roles review | Periplasmic OPGs in signal transduction/virulence; secreted OPGs in antibiotic/host interaction |
| [37267309](https://pubmed.ncbi.nlm.nih.gov/37267309/) | BcsA-like orphan synthases | Distinguishes *P. putida* cyclic-β-1,3-glucan synthase from OpgH |
| [26790533](https://pubmed.ncbi.nlm.nih.gov/26790533/) | *opgC* succinylation | Backbone (not substituents) required for virulence in *Dickeya*; contextualizes OPG modification |
| [7814331](https://pubmed.ncbi.nlm.nih.gov/7814331/) | UDP-glucose as signal | UDP-glucose as intracellular signal (σS control), context for OpgH's nutrient-sensing |

**Consistency of the evidence.** The enzymatic assignment (GT2 glucosyltransferase using UDP-glucose) is supported by both sequence/family criteria and direct in vitro biochemistry of orthologs (3 independent lines: [9352918](https://pubmed.ncbi.nlm.nih.gov/9352918/), [26150539](https://pubmed.ncbi.nlm.nih.gov/26150539/), [7934824](https://pubmed.ncbi.nlm.nih.gov/7934824/)). The product chemistry for *Pseudomonas* specifically is established ([7961404](https://pubmed.ncbi.nlm.nih.gov/7961404/)). Localization is supported by experimental topology mapping ([9352918](https://pubmed.ncbi.nlm.nih.gov/9352918/)). The downstream physiology is multiply corroborated across osmoadaptation, envelope integrity, Donnan/volume, and Rcs signaling. No retrieved paper contradicts the core annotation.

---

## Supported and Refuted Hypotheses

**Supported**
- OpgH is a GT2 inner-membrane glucosyltransferase using UDP-glucose to build the OPG β-glucan backbone ([26150539](https://pubmed.ncbi.nlm.nih.gov/26150539/), [9352918](https://pubmed.ncbi.nlm.nih.gov/9352918/), [7934824](https://pubmed.ncbi.nlm.nih.gov/7934824/)).
- OpgH is a polytopic inner-membrane protein (8 TM) with a cytoplasmic catalytic domain; its product is periplasmic ([9352918](https://pubmed.ncbi.nlm.nih.gov/9352918/)).
- OpgH acts in an operon/pathway with the periplasmic β-1,2-glucanase OpgG ([37735577](https://pubmed.ncbi.nlm.nih.gov/37735577/), [7934824](https://pubmed.ncbi.nlm.nih.gov/7934824/)).
- Pseudomonad OPGs are neutral branched β-1,2/β-1,6 glucans, osmoregulated ([7961404](https://pubmed.ncbi.nlm.nih.gov/7961404/)).
- OpgH product underlies envelope integrity, osmoadaptation, Rcs signaling, and pathogenicity ([12798996](https://pubmed.ncbi.nlm.nih.gov/12798996/), [9352941](https://pubmed.ncbi.nlm.nih.gov/9352941/), [10779706](https://pubmed.ncbi.nlm.nih.gov/10779706/), [7934824](https://pubmed.ncbi.nlm.nih.gov/7934824/)).
- OpgH moonlights as an FtsZ-sequestering cell-size regulator ([23935518](https://pubmed.ncbi.nlm.nih.gov/23935518/)).

**Refuted / Excluded**
- OpgH is **not** the *P. putida* cyclic-β-1,3-glucan "orphan" BcsA-like synthase (a separate GT2/GH17 enzyme; [37267309](https://pubmed.ncbi.nlm.nih.gov/37267309/)).
- OpgH is **not** the periplasmic glucanase — that role belongs to OpgG/OpgD (GH186; [37735577](https://pubmed.ncbi.nlm.nih.gov/37735577/)).

---

## Limitations and Knowledge Gaps

1. **No direct study of PP_5025.** Every mechanistic claim about Q88D04 is transferred by orthology from *E. coli* MdoH/OpgH, *Yersinia*, *Caulobacter*, and *P. syringae*. No paper reports purification, kinetics, gene knockout, or structural determination of the *P. putida* KT2440 OpgH itself. The assignment is confident but inferential.

2. **Cofactor and precise mechanism.** The ACP-cofactor requirement is cited from the *Yersinia opgGH* description ([26150539](https://pubmed.ncbi.nlm.nih.gov/26150539/)); the exact role of ACP, the initiation/priming mechanism, and processivity of the *P. putida* enzyme are not directly established.

3. **Product structure in *P. putida* specifically.** The β-1,2/β-1,6 branched structure is documented for *P. syringae* ([7961404](https://pubmed.ncbi.nlm.nih.gov/7961404/)); *P. putida* KT2440 OPGs have not been chemically characterized here. Whether substituents (e.g., succinyl, as in *Dickeya* via OpgC, [26790533](https://pubmed.ncbi.nlm.nih.gov/26790533/)) decorate *P. putida* OPGs is unknown — although pseudomonad OPGs are reported neutral/unsubstituted.

4. **Moonlighting role unverified in *P. putida*.** FtsZ antagonism/cell-size control is demonstrated in *E. coli* ([23935518](https://pubmed.ncbi.nlm.nih.gov/23935518/)) and *Yersinia* ([26150539](https://pubmed.ncbi.nlm.nih.gov/26150539/)); its conservation in *P. putida* is plausible but untested.

5. **Signaling wiring may differ.** Rcs-mediated capsule control ([9352941](https://pubmed.ncbi.nlm.nih.gov/9352941/)) and Donnan-potential effects ([12379178](https://pubmed.ncbi.nlm.nih.gov/12379178/)) derive from enterobacteria whose OPGs are anionic; *Pseudomonas* OPGs are neutral/unsubstituted ([7961404](https://pubmed.ncbi.nlm.nih.gov/7961404/)), so downstream physiology may be quantitatively different.

6. **Two-pathway coexistence.** The relationship, regulation, and possible functional redundancy between the OpgGH OPG pathway and the orphan cyclic-β-1,3-glucan pathway ([37267309](https://pubmed.ncbi.nlm.nih.gov/37267309/)) in *P. putida* is unexplored.

---

## Proposed Follow-up Experiments / Actions

1. **Targeted knockout of PP_5025 (*opgH*) in *P. putida* KT2440** with phenotyping for: low-osmolarity growth, SDS/antibiotic sensitivity, and cell-size distribution — directly testing F005/F006 in the native organism.

2. **Chemical characterization of *P. putida* KT2440 OPGs** (isolation + NMR/mass spectrometry of linkage composition and degree of polymerization) to confirm the β-1,2/β-1,6 branched structure and check for substituents.

3. **In vitro reconstitution:** express and purify the OpgH cytoplasmic GT2 domain (or full-length in nanodiscs) and assay UDP-glucose-dependent glucosyltransferase activity, including the ACP-cofactor dependence.

4. **Reconstitute the OpgH–OpgG pair** to demonstrate coupled synthesis–maturation and determine final chain-length control by the GH186 partner.

5. **Test FtsZ-sequestration/cell-size moonlighting in *P. putida*** via localization (fluorescent OpgH), FtsZ co-localization, and cell-size measurement across nutrient conditions.

6. **Genetically dissect pathway crosstalk** between OpgGH and the orphan cyclic-β-1,3-glucan synthase (single and double mutants) to define whether the two periplasmic glucan systems are redundant, complementary, or independently regulated.

7. **Structural determination** (cryo-EM) of *P. putida* OpgH to confirm the 8-TM topology and visualize the UDP-glucose-binding catalytic domain and putative translocation path.

---

*Report generated from a 3-iteration autonomous investigation comprising 7 confirmed findings and 20 reviewed papers. The functional annotation of OpgH (Q88D04 / PP_5025) rests on strong orthology to biochemically characterized MdoH/OpgH proteins; direct experimental study of the P. putida protein is the principal outstanding gap.*


## Artifacts

- [OpenScientist final report](opgH-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](opgH-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26150539
2. PMID:9352918
3. PMID:7934824
4. PMID:37735577
5. PMID:36516849
6. PMID:26790533
7. PMID:7961404
8. PMID:28593831
9. PMID:10779706
10. PMID:12798996
11. PMID:12379178
12. PMID:10733957
13. PMID:9352941
14. PMID:26265506
15. PMID:23935518
16. PMID:37267309