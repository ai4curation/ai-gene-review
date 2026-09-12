# AP5B1 (human, Q2VPB7) — review notes

Curation journal for the PAINT/affinage review wave. Provenance is inline as
`[PMID:NNNNN "verbatim quote"]`. Everything asserted here was checked against the cited
source; anything I could not check is flagged as such.

## 0. Inputs and identity check

- UniProt record fetched into `AP5B1-uniprot.txt` is `ID   AP5B1_HUMAN             Reviewed;         878 AA.`
  with primary accession Q2VPB7 — the expected accession, not a merged one. Secondary
  accessions A1L0S6, H6WUK2, Q0D2Q2, Q8N3J7, Q8WYH6.
- 878 aa, 93,949 Da. This matters historically: the sequence in the databases in 2011 was
  57 residues short at the N terminus, and Hirst et al. corrected it —
  [PMID:22022230 "The corrected full-length sequence of human DKFZp761E198 is 878 amino acids long, corresponding to a predicted protein size of 94 kD"].
  The current record matches the corrected length exactly.
- Aliases that matter for literature searching: **beta-5 / β5** (the name proposed in 2011),
  **DKFZp761E198** (the clone name used throughout Hirst et al. 2011), ORF name **PP1030**.
  Searching Europe PMC for `"beta5 adaptin"` returns **zero** hits; the productive queries
  are `AP5B1`, `"AP-5 adaptor"`, `"adaptor protein complex 5"`, and the clone name.
- GOA: 24 rows, 9 distinct GO terms. By evidence code: IPI 12, NAS 6, IBA 2, IEA 1, HDA 1,
  IMP 1, IDA 1 (15 rows carry an experimental code; 15 rows carry a WITH/FROM). By aspect:
  MF 12, CC 7, BP 5. By assigning group: IntAct 8, UniProt 7, ComplexPortal 6, GO_Central 2,
  InterPro 1. Every one of these numbers was produced by a script over the GOA tsv, not read
  off by eye; the same harness reconciles each GOA row against exactly one review row on the
  key (GO id, evidence code, reference, normalised WITH/FROM) and it passes at 24/24 with one
  additional NEW row. The harness lives outside the repo tree, per the campaign rule on
  scratch files.
- Affinage record: `self_evaluation_pairwise: win`, `faith_pct: 100.0`, 7 citations, and
  `.affinage.log` says "trust gates clear". The narrative describes the right protein — the
  beta subunit of AP-5 — with no symbol collision of the AGT/AGXT kind. All 7 cited ids are
  numeric PMIDs; none is a bioRxiv `PMID:bio_...` id. All 7 resolved and were cached.

## 1. What the protein is

AP5B1 is the **beta subunit of AP-5**, the fifth and most recently discovered heterotetrameric
adaptor protein complex. The complex was defined in one paper: μ5 (C14orf108/AP5M1) was found
in a yeast two-hybrid screen to bind an uncharacterised protein, DKFZp761E198, whose closest
relatives are the beta adaptins —
[PMID:22022230 "When the sequence of DKFZp761E198 was analysed using an iterative PSI-BLAST search, the top hits (apart from DKFZp761E198 homologues in other organisms) were all β-adaptins, and HHpred searches also pulled out β-adaptin as the top hit"]
— and the pair were renamed on that basis:
[PMID:22022230 "Therefore, we suggest that C14orf108 and DKFZp761E198 should be renamed μ5 and β5, respectively, and that the complex that they form should be called AP-5."].
The other two subunits, ζ (AP5Z1/KIAA0415) and σ5 (AP5S1/C20orf29), came from an independent
proteomics study published the year before [PMID:20613862].

**Architecture.** β5 has the beta-adaptin layout — N-terminal alpha-solenoid trunk, then a
C-terminal appendage — but with two differences the 2011 paper called out:
[PMID:22022230 "although DKFZp761E198 lacks a long unstructured linker separating the solenoid and appendage domains, its appendage domain contains both the β-sandwich subdomain and the α/β platform domain"].
So it is *more* complete than β4 in its appendage and *less* flexible than β1/β2 in its hinge.
The cryo-EM structure of the whole assembly (PDB 8YAB/8YAH, chain B = AP5B1 1-878) resolves
helices from residue 10 to 629, i.e. the solenoid; UniProt annotates only one disordered
region in the whole protein, `FT   REGION          234..260`.

**No clathrin apparatus.** This is the single most informative negative about β5, and I
re-tested it rather than repeating it — see `AP5B1-bioinformatics/RESULTS.md`. The 2011
statements were:
[PMID:22022230 "it also lacks two other clathrin-binding motifs, LLDLL and YQW"] and
[PMID:22022230 "DKFZp761E198 does contain a copy of the fourth clathrin-binding motif, WDW; however, this sequence is in the middle of the α-helical solenoid and is therefore unlikely to interact with clathrin."].
My re-test on the current UniProt sequences and current Pfam boundaries:

- `LLDLL` and `YQW` are absent — confirmed.
- The clathrin box consensus L(phi)x(phi)[DE] matches once, `LLRLE`@841, **inside the folded
  PF21590 domain**. In AP1B1 and AP2B1 the same consensus matches once each (`LLNLD`@632,
  `LLNLD`@631) and both sit in the long unstructured hinge — the position where the motif
  actually works. So
  [file:human/AP5B1/AP5B1-bioinformatics/RESULTS.md "AP5B1 has no clathrin box in an accessible linker"].
- The trunk-to-appendage linker is 62 aa in AP5B1 against 187 in AP1B1 and 178 in AP2B1;
  [file:human/AP5B1/AP5B1-bioinformatics/RESULTS.md "AP5B1's is the shortest, and by a factor of ~3 against the two clathrin-dependent beta subunits."]
  This confirms the "no long hinge" claim quantitatively.
- **One qualification that the re-test produced.** The `WDW` at 223-225 is *not* in the
  solenoid on the current records: no Pfam domain and no UniProt feature covers residue 223
  (the nearest 8YAB helix ends at 203; the disordered region starts at 234). The 2011
  structural dismissal of that motif does not hold. It does not change the conclusion,
  because
  [file:human/AP5B1/AP5B1-bioinformatics/RESULTS.md "the validated W-box consensus is `PWxxW`, and **`PWxxW` is absent from AP5B1**"],
  and because the cell biology is independent of the sequence argument:
  [PMID:22022230 "AP-5 does not associate with clathrin and is insensitive to brefeldin A."].

**Family placement.** UniProt puts AP5B1 in `DR   PANTHER; PTHR34033; AP-5 COMPLEX SUBUNIT BETA-1; 1.`
and `DR   PANTHER; PTHR34033:SF1; AP-5 COMPLEX SUBUNIT BETA-1; 1.` — *not* in the beta-adaptin
family. AP1B1, AP2B1, AP3B1 and AP4B1 are all PTHR11134 ("ADAPTOR COMPLEX SUBUNIT BETA FAMILY
MEMBER", 17,626 proteins). PTHR34033 has 1,227 proteins, one subfamily, and five reviewed
members: the human, mouse, rat, bovine and Xenopus AP5B1 orthologues
(`interpro/panther/PTHR34033/PTHR34033-entries.csv`). The practical consequence for this
review is that the PAINT route by which AP-1/2/3/4 beta-subunit terms could leak onto AP5B1
**does not exist** —
[file:human/AP5B1/AP5B1-bioinformatics/RESULTS.md "PAINT therefore cannot leak AP-1/2/3/4 beta-subunit terms onto AP5B1 through the family tree."]
The two IBAs on this gene are therefore not a family-transfer risk; they are something else
entirely, discussed in §4.

## 2. The complex(es): AP-5 core and the AP-5/SPG11/SPG15 hexamer

Two distinct assemblies, and GO represents only one of them.

**AP-5 core (tetramer)** = ζ (AP5Z1) + β5 (AP5B1) + μ5 (AP5M1) + σ5 (AP5S1). GO term
`GO:0044599 AP-5 adaptor complex`, definition "An AP-type membrane coat adaptor complex that
in humans consists of beta5, zeta, mu5 and sigma5 subunits and is found associated with
membranes in the endosomes; it is not clear whether AP-5 forms clathrin coats in vivo."
ComplexPortal CPX-5181, 1:1:1:1, which is what the UniProt record cites
(`DR   ComplexPortal; CPX-5181; AP-5 Adaptor complex.`).
[PMID:26085577 "AP-5, similar to the other APs, comprises a core of four proteins, namely, ζ, β5, µ5 and σ5 subunits, which share structural similarity to corresponding subunits in other AP complexes."]

**AP-5/SPG11/SPG15 (hexamer)** = AP-5 core + spatacsin (SPG11) + spastizin (ZFYVE26/SPG15),
stoichiometric:
[PMID:23825025 "we show that the four AP-5 subunits can be coimmunoprecipitated with SPG11 and SPG15, both from cytosol and from detergent-extracted membranes, with a stoichiometry of ∼1:1:1:1:1:1"].
This is the form the complex is thought to take natively —
[PMID:29381698 "However, AP-5 is predicted to be structurally very similar to APs 1-4, even though in its native form it exists as a heterohexamer rather than a heterotetramer."].
The division of labour proposed in 2013:
[PMID:23825025 "We propose that AP-5, SPG15, and SPG11 form a coat-like complex, with AP-5 involved in protein sorting, SPG15 facilitating the docking of the coat onto membranes by interacting with PI3P via its FYVE domain, and SPG11 (possibly together with SPG15) forming a scaffold."]
The 2025 cryo-EM structure supports it:
[PMID:40175557 "the N-terminal region of SPG11 is required for AP5 complex interaction and assembly"] and
[PMID:40175557 "The AP5 complex is in a super-open conformation."]

**GO has no term for the hexamer.** I checked: QuickGO ontology search for "spatacsin" and
for "SPG11" returns nothing; OLS search of GO for "spastizin spatacsin complex" returns
nothing; `GO:0044599` has no children. ComplexPortal, by contrast, *does* curate it —
**CPX-20045 "AP5-Spastizin-spatacsin complex"** (participants CPX-5181 + CPX-26503, cited to
PMID:40175557, PMID:25365221, PMID:23825025) and **CPX-26503 "Spastizin-spatacsin complex"** —
and neither carries a GO cross-reference. That asymmetry is a genuine ontology gap, recorded
as such in the review's `knowledge_gaps` and `proposed_new_terms`. It is also why the four
SPG11 IPI rows and the one SPG15 IPI row cannot be replaced by the CC annotation that would
actually capture them.

**Assembly evidence specific to AP5B1** (i.e. not just "AP-5 does X"):

- β5 binds μ5 directly, and the site is mapped:
  [PMID:22022230 "Two clones encoding residues 16–229 of DKFZp761E198, isolated from a human placental cDNA library screen using C14orf108 as bait, were tested for specificity."]
  [PMID:22022230 "The mapping of the binding site on DKFZp761E198 for C14orf108 to residues 16–229 is also consistent with a β-μ-like interaction"]
  This is the canonical beta-mu arrangement of AP-1/AP-2 reproduced in AP-5.
- β5 is required for μ5 stability, the classic beta-subunit behaviour:
  [PMID:22022230 "knocking down DKFZp761E198 also decreased the intensity of the C14orf108 band"].
- β5 was itself used as a bait in the study that found ζ and σ5:
  [PMID:20613862 "Glycine eluates from KIAA0415-LAP, KIAA0415-NFLAP, SPG11-LAP, and DKFZp761E198-LAP immunopurifications were used for in-solution digestion and analyzed by shotgun-LC-MS/MS"],
  [PMID:20613862 "Reciprocal immunoprecipitation experiments followed by mass spectrometry analyses of in-gel and in-solution digests confirmed the existence of a protein complex, which consists of at least five core proteins: KIAA0415, SPG11, SPG15, C20orf29, and DKFZp761E198"].
  So the AP5B1 IPI rows attributed to PMID:20613862 are bait-side as well as prey-side.
- AP5B1 is named as a component of the assembled complex a decade later:
  [PMID:33464297 "The SPG15-GFP construct assembles into a complex containing SPG11 and the four subunits of AP-5 (AP5Z1, AP5B1, AP5M1, and AP5S1"].
- A measured negative worth recording: β5 was used as bait in a yeast two-hybrid library
  screen looking for a second large subunit and found none —
  [PMID:22022230 "we carried out a yeast two-hybrid library screen using β5 as bait, but did not find any candidates for another adaptin"].
  ζ was found by proteomics, not by two-hybrid.

## 3. Function

**Endosome-to-Golgi retrieval.** The AP5B1-specific evidence is the knockdown phenotype. β5
siRNA phenocopies μ5 siRNA: the cation-independent mannose 6-phosphate receptor and the
retromer subunit Vps26 accumulate in enlarged perinuclear puncta —
[PMID:22022230 "Double labelling for the CIMPR and the retromer subunit Vps26 in control cells (a), cells depleted of C14orf108 (b), and cells depleted of DKFZp761E198 (c)."],
[PMID:22022230 "The finding that the DKFZp761E198 knockdown phenocopies the C14orf108 knockdown provides further evidence not only that the knockdown phenotypes are specific, but also that the interaction between C14orf108 and DKFZp761E198 is physiologically relevant."],
and at the complex level
[PMID:22022230 "Knocking down AP-5 subunits interferes with the trafficking of the cation-independent mannose 6-phosphate receptor and causes the cell to form swollen endosomal structures with emanating tubules."].
The direction of the defect was not resolved in 2011 and the 2011 GO annotation reflects that
(GO:0016197 endosomal transport, IMP). It was resolved in 2018 by CRISPR knockout of AP5Z1
plus spatial proteomics:
[PMID:29381698 "Immunolocalisation showed that loss of AP-5 led to impaired retrieval of the cation-independent mannose 6-phosphate receptor (CIMPR), GOLIM4, and GOLM1 from endosomes back to the Golgi region."],
[PMID:29381698 "Together, our findings suggest that AP-5 functions in a novel sorting step out of late endosomes, acting as a backup pathway for retromer."].
Six knockdowns (four AP-5 subunits plus SPG11 and SPG15) give the same CIMPR phenotype:
[PMID:23825025 "Knockdowns of SPG11 or SPG15 phenocopy knockdowns of AP-5 subunits: all six knockdowns cause the cation-independent mannose 6-phosphate receptor to become trapped in clusters of early endosomes."].
Together this is why `GO:0016197 endosomal transport` (IMP) should become
`GO:0042147 retrograde transport, endosome to Golgi` — a descendant of GO:0016197 (verified
via the QuickGO ancestors endpoint), so this is a refinement, not a change of claim.

**The cargo question is open, and the field says so.** AP-5's own cargo-binding activity has
never been demonstrated:
[PMID:29381698 "The AP-5 adaptor protein complex is presumed to function in membrane traffic, but so far nothing is known about its pathway or its cargo."],
and even after identifying the pathway the cargo link is a proposal routed through a partner
subunit, not through AP-5:
[PMID:29381698 "we propose that sortilin may act as a link between Golgi proteins and the AP-5/SPG11/SPG15 complex"].
This is why I did **not** add `GO:0140312 cargo adaptor activity` as a NEW row or as
`contributes_to_molecular_function`: its definition requires bridging membrane, cargo receptor
and deformation machinery, and the cargo-receptor half of that has not been shown for AP-5.
It is recorded as an MF knowledge gap instead.

**Recruitment.** Coincidence detection of PI3P and Rag GTPases, with PI3P read by the SPG15
FYVE domain, so the membrane-binding determinant is on a partner rather than on β5:
[PMID:33464297 "recruitment of AP-5/SPG11/SPG15 is enhanced in starved cells and occurs by coincidence detection, requiring both phosphatidylinositol 3-phosphate (PI3P) and Rag GTPases"],
[PMID:33464297 "GDP-locked RagC promotes recruitment of AP-5/SPG11/SPG15, while GTP-locked RagA prevents its recruitment."]

**Membrane remodelling and lysosome reformation.** The 2025 structural work adds an in vitro
activity for the assembled hexamer:
[PMID:40175557 "Our findings reveal that the AP5-SPG11-SPG15 complex can bind PI3P molecules, sense membrane curvature and drive membrane remodeling in vitro."],
[PMID:40175557 "These studies provide insights into the structure and function of the spastic paraplegia AP5-SPG11-SPG15 complex, which is essential for the initiation of autolysosome tubulation."].
Note: that paper's cache entry is abstract-only (`full_text_available: false`), so I have not
been able to see which subunit contributes the curvature-sensing surface. The review therefore
records this as a complex-level `contributes_to_molecular_function` and says so.
The loss-of-function counterpart is a storage phenotype:
[PMID:26085577 "Loss of AP-5 results in accumulation of aberrant endolysosomes: defining a new type of lysosomal storage disease."]

**Localisation.** Three independent lines, spanning 18 years:
- Placental lysosomal-membrane proteomics found it before anyone knew what it was —
  [PMID:17897319 "In membranes purified from placental lysosomes, we identified 58 proteins, known to reside at least partially in the lysosomal membrane."],
  [PMID:17897319 "Among these, 12 novel proteins of unknown functions were found."].
- The complex colocalises on a late endosomal/lysosomal compartment —
  [PMID:23825025 "In addition, AP-5, SPG11, and SPG15 colocalize on a late endosomal/lysosomal compartment."];
  in 2011 the compartment was identified through μ5, because tagged β5 could not be localised —
  [PMID:22022230 "substantial colocalisation can be seen between tagged C14orf108 and LAMP1, a protein associated with late endosomes and lysosomes"].
- **AP5B1 protein itself** was finally imaged in 2025, in human RPE, with an anti-AP5B1
  antibody — [PMID:40081374 "Immunofluorescence imaging of those sections confirmed the punctate staining patterns of AP5Z1, AP5M1, and AP5B1, revealing their strongest co-localization with Rab7, a marker of late endosomes, and partial overlap with TGN46-positive Golgi-derived vesicles"].
  This is the first direct, subunit-specific localisation of AP5B1 and it agrees with the
  complex-level NAS annotations from ComplexPortal.

**Human genetics.** AP5B1 is a macular dystrophy gene, established in 2025-2026 across three
independent cohorts. This is *new since the GOA snapshot* and none of it is annotated:
[PMID:40081374 "New WES, new WGS screening, or a reanalysis of previous sequencing data by using a customized analytical pipeline led to the identification of assortments of bi-allelic variants in AP5Z1 (14 families), AP5M1 (three families), and AP5B1 (two families)"],
[PMID:41830174 "Five unrelated patients from Europe and Iran were identified with a distinctive macular degeneration associated with bi-allelic variants in AP5Z1 (HGNC: 22197) and AP5B1 (HGNC: 25104), subunits of the vesicular fifth adaptor protein (AP-5) complex."],
[PMID:42568187 "Here, we describe 22 affected individuals from 20 families with AP5B1-associated IRD, all carrying the recurrent missense variant c.2354T>C"].
The AP5B1 alleles in the 2025 cohort are truncating —
[PMID:40081374 "they all remove more than two-thirds of the protein's full sequence and are therefore extremely likely to represent full LoF alleles"] —
and p.Leu785Pro is a founder allele —
[PMID:42568187 "These findings further support AP5B1 as a cause of macular dystrophy, identify p.Leu785Pro as a relatively frequent pathogenic allele in individuals of European and Ashkenazi Jewish ancestry"].
Note that Leu785 falls inside PF21590 (781-873), the C-terminal appendage domain, per the
bioinformatics run. Unlike AP5Z1 (spastic paraplegia SPG48), AP5B1 has not been reported as an
HSP gene; the phenotype reported for AP5B1 is retinal.

**A measured negative.** The paper that discovered AP5Z1 came out of a DNA-repair RNAi screen,
and three of the five complex members scored in it — but β5 did not:
[PMID:20613862 "Knockdown of SPG11 and DKFZp761E198, however, did no have an effect on the percentage of GFP positive cells"]
(the "did no have" typo is in the source and is reproduced verbatim). There is no DNA-repair
annotation on AP5B1 in GOA, so there is nothing to remove; recorded so that a future reviewer
reading the title of PMID:20613862 does not add one.

**Not annotated, and deliberately so.** HIV-2 Gag particle release depends on AP-5 while
HIV-1's does not — [PMID:27392064 "HIV-2 particle release was dependent on the adaptor protein complex AP-3 and the newly identified AP-5 complex, but much less so on AP-1."] —
but the siRNA used there targets AP5M1 ("AP-5μ ON-TARGETplus AP5M1 J-015523-09"), not AP5B1,
and viral hijacking of a trafficking route is not a function of the host gene. No row.

## 4. The two IBAs and the one IEA

Fetched slice: `just fetch-panther-paint PTHR34033` →
`interpro/panther/PTHR34033/PTHR34033-paint.tsv`, which contains exactly two IBD rows:

```
PTHR34033  PTN002145545  GO:0030119  C  IBD  false  UniProtKB:Q2VPB7  taxon:2759  20170228
PTHR34033  PTN002145545  GO:0016197  P  IBD  false  UniProtKB:Q2VPB7  taxon:2759  20170228
```

Reading this carefully matters. There is **one** node in the whole family, `PTN002145545`,
placed at `taxon:2759` (Eukaryota) — the root of the family — and **its only seed is
UniProtKB:Q2VPB7, i.e. AP5B1 itself**. The two terms it carries are precisely the two
experimental annotations AP5B1 had in 2017: the IDA for GO:0030119 and the IMP for GO:0016197,
both from PMID:22022230. The GOA WITH/FROM for both IBA rows is
`PANTHER:PTN002145545|UniProtKB:Q2VPB7`, which is exactly what that node structure predicts.

So these are the textbook self-referential IBA case that CLAUDE.md and the skill both call out:
the gene's own experimental annotation is one of the descendant evidences the PAINT curator
used to place the IBD, so the gene legitimately appears among the sources of the IBA it
receives. That is not circular and the short donor list is not weak. What the IBA adds over
the IDA/IMP is a phylogenetic statement: the curator judged this function to be ancestral to
the whole eukaryotic AP5B1 clade rather than lineage-specific — a judgement that the
comparative genomics in the same paper supports
([PMID:22022230 "AP-5 subunits can be found in all five eukaryotic supergroups, but they have been co-ordinately lost in many organisms."],
[PMID:22022230 "Thus, AP-5 is an evolutionarily ancient complex, which is involved in endosomal sorting, and which has links with hereditary spastic paraplegia."]).
`root_cause: NO_FAILURE_CORE` for both, `source_status: SUPPORTS_TRANSFER` for both entries.
Human AP5B1 is trivially inside the inheriting clade (it *is* the seed), there is no IRD/IKR
anywhere in the family, and the family index shows the four other reviewed members are all
full-length (876-883 aa) orthologues with no sign of pseudogenisation.

The IEA row (GO:0016197, GO_REF:0000002, WITH/FROM `InterPro:IPR038741`) traces to an
InterPro2GO mapping I verified at the source: the InterPro API returns for IPR038741 the name
"AP-5 complex subunit beta-1", type `family`, a single GO mapping `GO:0016197 endosomal
transport`, and the description "AP5B1 is part of the AP-5 adaptor protein complex, which may
be involved in endosomal transport". IPR038741 is the AP5B1-specific family signature (UniProt
carries it as `DR   InterPro; IPR038741; AP5B1.`), so the mapping is family-specific, not a
promiscuous pan-adaptin mapping, and it is correct. `root_cause: NO_FAILURE_CORE`.

## 5. Partner resolution for the 12 IPI rows

All eight distinct accessions resolved via the UniProt REST API (`size` > 1, Swiss-Prot status
recorded):

| Accession | Gene | Protein | Verdict |
|---|---|---|---|
| O43299 | AP5Z1 | AP-5 complex subunit zeta-1 | AP-5 core subunit |
| Q9NUS5 | AP5S1 | AP-5 complex subunit sigma-1 | AP-5 core subunit |
| Q9H0R1-1 | AP5M1 | AP-5 complex subunit mu-1 (MuD/MUDENG) | AP-5 core subunit, direct β5 partner |
| Q8BJ63 | Ap5m1 | AP-5 complex subunit mu-1, **mouse** | same, cross-species (IntAct `Xeno`) |
| Q96JI7 | SPG11 | Spatacsin | hexamer scaffold |
| Q68DK2 | ZFYVE26 | Spastizin / FYVE-CENT | hexamer membrane-docking subunit |
| Q13554 | CAMK2B | CaMKII beta | high-throughput only |
| Q9GZT8 | NIF3L1 | NIF3-like protein 1 | high-throughput only |

Reference projection test (QuickGO by `reference=`, paginated fully, entities counted not
annotations):

| Reference | annotations | distinct entities |
|---|---|---|
| PMID:25416956 (Rolland Y2H) | 24,599 | 937 |
| PMID:33961781 (BioPlex AP-MS) | 9,514 | 2,196 |
| PMID:17897319 (lysosomal proteomics) | 246 | 242 |
| PMID:22022230 (Hirst 2011) | 45 | 10 |
| PMID:20613862 (Slabicki 2010) | 25 | 5 |
| PMID:40175557 (cryo-EM) | 42 | 10 |
| PMID:23825025 (Hirst 2013) | 8 | 4 |

The two proteome-scale screens are what they look like: 937- and 2,196-entity projections
([PMID:25416956 "While currently available information is highly biased and only covers a relatively small portion of the proteome, our systematic map appears strikingly more homogeneous"],
[PMID:33961781 "Through affinity-purification mass spectrometry, we have created two proteome-scale, cell-line-specific interaction networks."]).
CAMK2B and NIF3L1 come only from those two and have no functional follow-up anywhere in the
AP-5 literature, so both go to `MARK_AS_OVER_ANNOTATED`. Note the trap: CAMK2B appears in both
screens and the UniProt IntAct block reads
`Q2VPB7; Q13554: CAMK2B; NbExp=4; IntAct=EBI-5917279, EBI-1058722;` — but an NbExp count is
experiments, not independent studies, and two high-throughput methods agreeing is still two
high-throughput methods. By contrast
`Q2VPB7; Q96JI7: SPG11; NbExp=8; IntAct=EBI-5917279, EBI-2822128;` is supported by targeted
work across four papers.

The lysosomal proteomics reference (242 entities) is a broad projection too, but unlike the
interactome screens its claim is independently corroborated for this protein by three later,
targeted studies (Hirst 2013, Hirst 2021, Kaminska 2025), so it is accepted rather than
downgraded.

## 6. Decisions taken (summary; the reasoning per row is in the YAML)

- `GO:0030119` **IDA** (PMID:22022230) → **MODIFY** to `GO:0044599 AP-5 adaptor complex`. The
  cited paper is the one that *defined* AP-5 and named β5 as its subunit; the specific term
  now exists and is already on the gene by NAS. The strongest evidence should carry the
  specific term.
- `GO:0030119` **IBA** → **ACCEPT**. The IBD mirrors the 2017 state of the seed; a family-level
  claim at the parent is appropriately conservative, not a granularity failure.
- `GO:0016197` **IMP** (PMID:22022230) → **MODIFY** to `GO:0042147 retrograde transport,
  endosome to Golgi` (a verified descendant), with PMID:29381698 as additional reference for
  the direction.
- `GO:0016197` **IBA** and **IEA** → **ACCEPT** (both correct, both appropriately general).
- `GO:0016192` **NAS** → **MODIFY** to `GO:0042147`. It is the grandparent of a term already on
  the gene, so it conveys nothing as it stands.
- Nine `GO:0005515` IPI rows whose partner is an AP-5 core subunit or a hexamer partner →
  **MODIFY** to `GO:0005198 structural molecule activity`. Justification is not "it binds
  something": β5 binds μ5 through a mapped N-terminal site in the canonical beta-mu
  arrangement, and knocking β5 down destabilises μ5 — that is a structural-integrity
  contribution, which is what GO:0005198 means. The annotation that would really capture the
  SPG11/SPG15 rows is CC membership of the hexamer, and that term does not exist.
- Three `GO:0005515` IPI rows with CAMK2B/NIF3L1 → **MARK_AS_OVER_ANNOTATED**.
- The five CC/BP NAS rows and the HDA row → **ACCEPT**.
- One **NEW** row: `GO:0001895 retina homeostasis`, IMP, PMID:40081374. Three independent
  2025-2026 cohorts, bi-allelic LoF and founder missense alleles, plus subunit-specific RPE
  localisation. Flagged in its own reason as a tissue-level, non-core consequence rather than
  a molecular core function.

Final tally: 12 MODIFY, 9 ACCEPT, 3 MARK_AS_OVER_ANNOTATED, 1 NEW. No REMOVE and no
UNDECIDED: nothing in GOA for this gene is contradicted by the literature, and every cited
reference was readable at least in abstract.

**Three validation warnings remain, all deliberate.** Two are "inconsistent review actions"
on GO:0016197 and GO:0030119, where the IBA/IEA rows are ACCEPTed at the general term while
the human experimental row is refined. That divergence is the point rather than an oversight:
the direction of transport and the four-subunit composition are human results, and pushing
either down a level on a eukaryote-root PAINT node or on an InterPro family signature would
propagate a human-specific finding to 1,227 proteins across 2,973 taxa. Each of those four
`review.reason` fields states the divergence explicitly. The third warning is that no
`supporting_text` cites the affinage file; that is the campaign rule (affinage is a lead, not
evidence) and is recorded in the affinage `reference_review`.

## 7. What affinage missed, and what it got right

Got right: the mechanistic narrative is accurate and correctly scoped to AP-5 and to this
subunit; the retromer-backup framing, the Rag/PI3P coincidence detection, the LSD phenotype
and the 2025 macular dystrophy paper are all real and correctly cited. The `mechanism_profile`
GO grounding was not imported (per the brief) and would have been partly wrong if it had been:
it proposes `GO:0060090 molecular adaptor activity` as the molecular activity, which overstates
what has been shown, given that AP-5's cargo interaction is explicitly unknown.

Missed — found by independent Europe PMC searching:

1. **PMID:42568187** (2026), the largest AP5B1 disease cohort to date, 22 individuals from 20
   families, and the paper that establishes p.Leu785Pro as a founder allele. Affinage's newest
   citation is PMID:40081374 (April 2025).
2. **PMID:41830174** (2026), the independent replication cohort (AP5Z1 and AP5B1 retinal
   degeneration).
3. **PMID:20613862** is in GOA and supplies four of the twelve IPI rows, and it is the study
   that found ζ and σ5 with β5 as one of the baits — affinage does not cite it at all. Its
   title is about a DNA repair screen, which is exactly the "titled for something else" failure
   mode the brief warns about.
4. **PMID:22022230**, the paper that defines the complex and contains every AP5B1-specific
   experiment, is also not in affinage's citation list (it cites the 2013 follow-up instead).
   Both 3 and 4 were already seeded into the review by GOA, so nothing was lost, but it is
   a reminder that affinage's gates measure precision, not recall.
5. **PMID:17897319**, the source of the HDA lysosomal-membrane row.

Cross-check on affinage's claims that I could verify independently: PMID:29381698,
PMID:26085577, PMID:33464297, PMID:27392064 and PMID:40081374 all resolve to the papers
affinage describes and say what affinage says they say. Reference reviews recorded accordingly.

## 8. Open questions carried into `knowledge_gaps`

- No demonstrated molecular activity for AP-5 or for β5: no cargo sorting motif recognised, no
  cargo binding shown. `Pharos; Q2VPB7; Tdark.`
- No GO CC term for the AP-5/SPG11/SPG15 hexamer even though ComplexPortal curates it
  (CPX-20045), so five IPI rows have nowhere accurate to land.
- Which subunit of the hexamer provides the curvature-sensing surface in PMID:40175557 is not
  determinable from the abstract, and that paper's cache entry has no full text.
- Whether β5's appendage — which uniquely among the AP-5-family-adjacent beta subunits retains
  both platform and sandwich subdomains — binds accessory proteins the way the AP-1/AP-2 ears
  do. No ligand has been reported for it.
