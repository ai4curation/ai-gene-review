# FLAD1 (Q8NFF5) — Gene Review Notes

## Identity and summary

FLAD1 encodes human FAD synthase (FMN adenylyltransferase; FMNAT; FADS; EC 2.7.7.2),
the enzyme that catalyzes the **final, committed step of FAD-cofactor biosynthesis**:
adenylylation of flavin mononucleotide (FMN) with ATP to yield flavin adenine
dinucleotide (FAD) plus diphosphate. FAD is the cofactor of hundreds of flavoenzymes
(respiratory chain Complex I/II, acyl-CoA dehydrogenases, MTHFR, dimethylglycine
dehydrogenase, monoamine oxidase, etc.). The reaction requires a divalent metal,
optimally Mg2+.

[file:human/FLAD1/FLAD1-uniprot.txt "FAD synthase catalyzes the adenylation of flavin mononucleotide (FMN) to form flavin adenine dinucleotide (FAD) coenzyme"]
[file:human/FLAD1/FLAD1-uniprot.txt "Reaction=FMN + ATP + H(+) = FAD + diphosphate"]
[PMID:16643857 "FAD synthetase (FADS) (EC 2.7.7.2) is a key enzyme in the metabolic pathway that converts riboflavin into the redox cofactor FAD"]
[PMID:16643857 "Both isoforms possessed FADS activity and had a strict requirement for MgCl(2)"]

The human enzyme is **bifunctional and multidomain**, distinguishing it from the
single-domain yeast Fad1p:
- **C-terminal PAPS-reductase domain (FADSy; ~residues 355-587)** = the FAD-forming
  catalytic (FMN adenylyltransferase) domain.
- **N-terminal molybdopterin-binding-resembling (MPTb) domain (with a KH domain)** =
  a **FAD hydrolase / FAD diphosphatase (FADHy)** activity (EC 3.6.1.18), and, at lower
  efficiency, an NADH diphosphatase / NADH pyrophosphatase activity (EC 3.6.1.22).

[file:human/FLAD1/FLAD1-uniprot.txt "This enzyme has two activities: FAD diphosphatase activity"]
[file:human/FLAD1/FLAD1-uniprot.txt "In the N-terminal section; belongs to the MoaB/Mog family"]
[file:human/FLAD1/FLAD1-uniprot.txt "In the C-terminal section; belongs to the PAPS reductase"]
[PMID:26277395 "The recombinant hFADS2 was able to hydrolyse added FAD in a Co(2+) and mersalyl dependent reaction"]
[PMID:38688286 "the combination of the N-terminal molybdopterin-binding and KH domains is the minimal essential substructure required for the hydrolysis of FAD and other ADP-containing dinucleotides"]

## Reactions (from UniProt CATALYTIC ACTIVITY)

- FAD synthase (forward): `FMN + ATP + H+ = FAD + diphosphate` (EC 2.7.7.2, RHEA:17237) — the physiological/biosynthetic direction.
- FAD diphosphatase / FAD hydrolase: `FAD + H2O = FMN + AMP + 2 H+` (EC 3.6.1.18, RHEA:13889).
- NADH diphosphatase / NADH pyrophosphatase: `NADH + H2O = reduced NMN + AMP + 2 H+` (EC 3.6.1.22, RHEA:48868).
- FAD synthase also runs the reverse pyrophosphorolytic reaction at a much lower rate.

[file:human/FLAD1/FLAD1-uniprot.txt "Reaction=FAD + H2O = FMN + AMP + 2 H(+)"]
[file:human/FLAD1/FLAD1-uniprot.txt "PATHWAY: Cofactor biosynthesis; FAD biosynthesis; FAD from FMN: step"]

Note the direction convention: GO:0003919 FMN adenylyltransferase activity is defined
`ATP + FMN = diphosphate + FAD` (the synthase direction), while GO:0047884 FAD
diphosphatase activity is `FAD + H2O = AMP + FMN` (the hydrolase direction). Both are
distinct, well-supported activities of this bifunctional protein.

## Cofactor / metal requirement

FAD synthase activity requires a divalent metal (Mg2+ optimal; Co2+ comparable; lower
with Mn/Ca/Zn). FAD diphosphatase activity instead requires Co2+ (Ni/Mn partial;
Mg/Ca/Cu cannot substitute) and is stimulated by K+.

[file:human/FLAD1/FLAD1-uniprot.txt "The FAD synthase activity requires a divalent metal"]
[file:human/FLAD1/FLAD1-uniprot.txt "Magnesium or cobalt supports the highest FAD synthase activity"]
[file:human/FLAD1/FLAD1-uniprot.txt "The FAD diphosphatase activity requires cobalt"]

## Kinetics (isoform 2; from UniProt)

KM(FMN) ~0.35-1.5 uM; KM(ATP) ~15 uM; kcat(FAD synthesis) ~0.69 s-1 (E. coli-purified).
kcat is low, consistent with FAD release being rate-limiting and with a "FAD chaperone"
delivery step.

[PMID:16643857 "exhibited a K(M) value for FMN of 1.5+/-0.3microM"]
[PMID:21951714 "FAD release may represent the rate-limiting step of the whole catalytic cycle"]

## FAD chaperone / delivery function

Beyond catalysis, hFADS2 physically interacts with client apo-flavoproteins and
directly transfers newly made FAD to them (a "FAD chaperone" role). Demonstrated for
the nuclear demethylase KDM1A/LSD1 and mitochondrial dimethylglycine dehydrogenase
(DMGDH).

[PMID:25954742 "hFADS is able to operate as a FAD \"chaperone.\""]
[PMID:25954742 "A direct transfer of the cofactor from hFADS2 to apo-dimethyl glycine dehydrogenase was also demonstrated"]
[file:human/FLAD1/FLAD1-uniprot.txt "Interacts with KDM1A; which promotes"]
[file:human/FLAD1/FLAD1-uniprot.txt "Interacts with DMGDH; which promotes DMGDH holoenzyme formation"]

## Subcellular localization (isoform-dependent)

- **Isoform 1** (587 aa, canonical; N-terminal cleavable mitochondrial transit peptide,
  residues 1-17) → **mitochondrial matrix**.
- **Isoform 2** (490 aa; lacks the first 97 aa) → **cytosol** (most abundant isoform).
- FADS is also found in the **nucleus**, consistent with a nuclear flavin-cofactor pool
  supplying LSD1/KDM1A.

[PMID:20060505 "hFADS1, but not hFADS2, localizes in mitochondria"]
[file:human/FLAD1/FLAD1-uniprot.txt "Isoform 1 and 2 are located in mitochondria and cytosol, respectively"]
[file:human/FLAD1/FLAD1-uniprot.txt "SUBCELLULAR LOCATION: Nucleus"]
[file:human/FLAD1/FLAD1-uniprot.txt "SUBCELLULAR LOCATION: [Isoform 1]: Mitochondrion matrix"]
[file:human/FLAD1/FLAD1-uniprot.txt "SUBCELLULAR LOCATION: [Isoform 2]: Cytoplasm, cytosol"]

## Structure

Crystal structure (PDB 8ROM/8RON) of full-length hFADS2 and its C-terminal PAPS domain
in complex with FAD. The enzyme forms a **stable C2-symmetric dimer**; packing of one
protomer's KH domain against the other's N-terminal domain creates the adenosine-specific
hydrolytic active site.

[PMID:38688286 "hFADS2 associates in a stable C2-symmetric dimer"]
[file:human/FLAD1/FLAD1-uniprot.txt "SUBUNIT: Dimer (PubMed:38688286)"]

## Disease

Biallelic FLAD1 variants cause **Lipid Storage Myopathy due to FAD Synthase Deficiency
(LSMFLAD; MIM:255100)**, presenting as combined respiratory-chain deficiency and multiple
acyl-CoA dehydrogenase deficiency (MADD-like). Some (frameshift, hypomorphic) cases are
riboflavin-responsive. (Primary reference PMID:27259049 not in local cache; disease
statement quoted from UniProt.)

[file:human/FLAD1/FLAD1-uniprot.txt "Lipid storage myopathy due to flavin adenine dinucleotide"]
[file:human/FLAD1/FLAD1-uniprot.txt "Some patients show significant improvement with riboflavin treatment"]

## Notes on annotation review

- Core MF is **GO:0003919 FMN adenylyltransferase activity** (= FAD synthase), the
  biosynthetic step; supported by a large body of EXP/IDA annotations.
- **GO:0047884 FAD diphosphatase activity** is a genuine, experimentally demonstrated
  second catalytic activity (MPTb/KH domain), so it is a real (secondary) core function,
  not an over-annotation. IDA support in PMID:26277395, PMID:31351152, PMID:38688286.
- **GO:0035529 NADH pyrophosphatase activity** is a lower-efficiency side activity of the
  same hydrolase site (EC 3.6.1.22, RHEA:48868); real but non-core (KEEP_AS_NON_CORE).
- **GO:0003824 catalytic activity** (IEA, InterPro) is an uninformative root — MARK_AS_OVER_ANNOTATED (better specific terms exist).
- The many **protein binding / identical protein binding IPI** annotations come from
  high-throughput interactome screens (HuRI, BioPlex, etc.). Bare GO:0005515 is
  uninformative → MARK_AS_OVER_ANNOTATED (per policy, never REMOVE an IPI). The
  identical protein binding (GO:0042802) reflects the physiological homodimer, so keep
  as non-core. The functionally meaningful interactions (KDM1A, DMGDH) are the
  apo-flavoprotein clients (PMID:25954742), captured as the FAD-chaperone role, not as
  bare "protein binding".
- Localization: cytosol (IDA, isoform 2), mitochondrial matrix (IDA, isoform 1), nucleus
  (IDA) are all experimentally supported. Mitochondrion (HTP) and mitochondrial-matrix
  IEA are consistent. Nucleus IEA/ISS and cytoplasm ARBA IEA are redundant with the IDA
  evidence.


## 2026-10-28 source-aware audit and current scientific interpretation

This entry supersedes conflicting interpretations in the preserved earlier journal. It does not rewrite that journal or add publication quotations. The detailed source access, assay boundaries, partner joins, natural-product checks and PAINT evidence are in [FLAD1-evidence.yaml](FLAD1-evidence.yaml).

The current official snapshot contains 43 annotation contexts. Source-aware seeding retains the prior 41 records, adds two separately identified partners for PMID:25416956, and adds the current nucleus/cytosol GO_REF:0000120 assertions. The old GO_REF:0000044 nucleus and cytosol assertions are explicitly retired, keeping their original reference identifiers and complete historical reviews. Thus the document has 43 current plus two historical rows, rather than two newly discovered GO functions. Seventeen legacy source lists were populated by the supported seeder. All 38 inherited quotation/reference occurrences are conserved, including duplicated cofactor quotations moved into the synthase core. The title and quotation checks apply to inherited quotations, not newly manufactured evidence.

All 29 pre-existing shared normal source files were hydrated from the pinned main commit before the genuine gene fetch, and remain byte-identical. Five previously qualified absent publications were genuinely fetched: PMID:17049878, PMID:19369195, PMID:23946482, PMID:27259049 and PMID:9110174. Only the last two have full text in their fetched normal cache. The UniProt and GOA files were regenerated through the repository fetcher. No shared source was edited to improve an assay claim. Research used actual primary sources and independent consultations; known campaign provider authentication/quota failures were not retried, and no manual text is presented as provider-generated research.

The two core activities are FMN adenylyltransferase and FAD diphosphatase. ATP and divalent-metal requirements belong within the synthase core rather than being independent third/fourth core functions. The description no longer lists respiratory complex I as an FAD-dependent example. The broad InterPro catalytic-activity assertion is modified to the demonstrated FMN adenylyltransferase activity, not called biologically excessive merely for being general. Cytoplasm is a valid broad location and is refined by MODIFY to the experimentally supported cytosol and mitochondrial-matrix terms, retaining their distinct product scopes. Cytosol and mitochondrial matrix in the synthase description refer to the supported product-specific pools; they do not assign these locations to all five products. The matrix annotations are accepted as a compartment of the core synthase function with the longer-product assay scope. ACCEPT does not require a location to apply to every natural isoform; the broader mitochondrial-proteome annotation remains non-core.

Actual PMID:23443125 Methods/Results assign FAD synthesis to the human 329–587 C-terminal construct. Its reverse reaction uses pyrophosphate; it is not the water-dependent FAD diphosphatase reaction. PMID:26277395 and PMID:31351152 establish recombinant FAD hydrolysis under particular cobalt-dependent conditions. A separate consultation of the original PMID:38688286 author-repository PDF refines the active substructure to MPTb plus KH with an interprotomer site; MPTb alone binds nucleotides but is not sufficient for measured hydrolysis. Its 110–587 crystal construct is twelve residues shorter than natural isoform 2. Physiological hydrolysis remains uncertain, as the authors themselves discuss scarce free cobalt. The separately retrieved primary text is documented distinctly from the abstract-only normal cache.

NADH pyrophosphatase remains a reported non-core substrate activity. The current inspection does not establish a quantitative lower rate or a constitutive role in cellular NADH turnover. NADH inhibition of FAD hydrolysis, NADH binding/docking, and NADH substrate turnover are different claims. The inherited UniProt excerpt on the NADH row describes FAD hydrolysis and cannot by itself support NADH turnover. It is preserved for provenance, with this limitation made explicit.

PMID:25954742 directly demonstrates transfer from recombinant human hFADS2 to recombinant rat apo-DMGDH. Its LSD1 association assays use rat nuclear material, not a purified-human-LSD1 transfer experiment. Human HepG2 staining supports nuclear/cytoplasmic FADS localization without resolving every splice product. Rat donor D4A4P4 has its own nuclear experimental evidence in PMID:23946482 and PMID:25954742. Nuclear FAD-degrading activity in the former study is not automatically assigned to FLAD1. The human isoform-1 import and processing observations in PMID:20060505 are distinguished from its predicted exact transit-peptide cleavage boundary.

The five seeded natural products remain in their original order with all identifiers and names preserved. Their reconstructed sequences match official FASTA records at 587, 490, 446, 294 and 338 residues. Only the two legacy dangling-comma VSP notes were repaired through the repository helper, appending VSP_027952 and VSP_027953. PMID:27259049 paper isoforms 5/6 cannot be equated by number to current UniProt products. Its Met268/Met355 constructs were expressed in control fibroblasts; the Met268 activity observation is not a patient-cell rescue experiment. The endogenous small-band product identity remains partly speculative. Neither the natural products 3–5 nor a newly invented Q8NFF5-6 receives those effects. FAD-dependent stability recovery of a recombinant variant is distinguished from catalytic recovery and variable clinical riboflavin response.

The actual PTHR23293 tree contains 233 nodes. Human Q8NFF5 is leaf PTN002510965 with an exact 587-residue ungapped MSA match. Both incoming IBA terms join positive original IBDs at PTN000591373 on that target path. The current API release and original PAINT source are separately pinned; no whole-release identity is assumed. Human evidence among the descendants is expected and is not circular.

Eight of nine incoming interaction contexts have exact official IntAct pair/publication joins. The remaining PMID:40205054/Q5T6F2 context is retained on independent same-pair PMID:33961781 coimmunoprecipitation evidence, with the missing newer-source assay expressly disclosed. Generic associations do not establish adaptor, kinase-binding or other specific molecular activities. PMID:25416956 is the 2014 interactome study, not the later HuRI resource. Self-association is consistent with structural dimerization but is not a separate catalytic core. The exact PMID:34800366 FLAD1 target table row was not recovered; its inherited title quotation is not treated as a target-specific hit. Independent PMID:20060505 localization supports the non-core mitochondrial context.

The user campaign instructions retain supported generic binding as KEEP_AS_NON_CORE and prohibit new publication quotations. They take precedence over conflicting local skill/CLAUDE defaults; this is an explicit current instruction, not a legacy exemption. No validator behavior was changed. Canonical checks determine the computed status and advisories. No NEW annotation is proposed.

Independent scientific review also narrowed the PMID:25135855 finding to measured biochemical thiol dependence and a proposed physiological redox switch, while preserving its exact inherited quotation. Final ontology-enabled validation passed with only the six disclosed generic-binding policy advisories. The unchanged canonical helper confirms DRAFT with zero status mismatches. History schema validation and private HTML rendering also passed.
