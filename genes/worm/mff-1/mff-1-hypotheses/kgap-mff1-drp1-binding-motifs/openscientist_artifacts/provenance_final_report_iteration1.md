# MFF-1 (Q19343, C. elegans): does it retain a predicted DRP-1 binding module?

Hypothesis slug: `kgap-mff1-drp1-binding-motifs`
Source: `genes/worm/mff-1/mff-1-ai-review.yaml` (free text)
Analysis date: 2026-11-23. All computations below were run in this job; code and output tables are in `provenance/`.

## Executive judgment

**Partially supported.** The architectural half of the hypothesis is confirmed by sequence analysis. The mechanistic half, that the repeats are *the* Drp1-binding motifs validated by human mutagenesis, is not supported by the literature, because that mutagenesis does not appear to exist.

What holds up:

- MFF-1 is a 158-residue protein with the same three-module layout as human MFF: N-terminal VPE-type Mff repeats, a predicted coiled coil, and a C-terminal tail anchor ending two residues after the transmembrane segment in a basic RR, the signature of an outer-mitochondrial-membrane tail-anchored protein.
- A position-specific scoring matrix for the Mff repeat, calibrated against 175,800 shuffled windows, calls one repeat in MFF-1 above a 1e-4 empirical threshold (residue 39, SVPEHITV, 12.55 bits, p = 2.3e-5), with two further sub-threshold VPE windows at residues 2 and 68. Smith-Waterman alignment of human MFF 40-100 against MFF-1 1-80 (SW = 42, 36.0 % identity, z = 4.59 versus shuffled, empirical p < 0.007) independently puts human R1 opposite MFF-1 residue 1 and human R2 opposite MFF-1 residue 38, in register. The repeats are real and orthologous.
- AlphaFold DB gives MFF-1 a single long confident helix at 105-157 (mean pLDDT 78.2, the best-ordered part of a protein whose global mean pLDDT is 60.3), matching the human 287-341 helix that spans UniProt's annotated coiled coil 291-322 and TM 323-340.

What does not hold up:

- The seed hypothesis asks to score "the key residues identified by mutagenesis in human MFF" within the repeats. Four targeted PubMed searches found no primary paper that mutates or deletes the MFF N-terminal repeats and measures DRP1 binding. The repeats are a conserved signature of unmeasured functional weight.
- The MFF modules that mammalian biochemistry actually implicates point in a different direction. Clinton et al. 2016 (PMID 26578514) found the MFF coiled coil is not essential for DRP1 interaction. Liu, Kage and Higgs 2021 (PMID 34347505) found MFF oligomerises through that coiled coil (Kd ~10 microM) and that this oligomerisation is required for DRP1 activation. Liu and Chan 2015 (PMID 26446846) placed the determining variable on the DRP1 side: MFF cannot bind assembly-deficient DRP1.
- There is no C. elegans measurement of an MFF-1/DRP-1 interaction. The single relevant worm primary paper (PMID 39998089) reports genetic co-dependence of a stress-induced mitochondrial phenotype on mff-1, mff-2, drp-1 and clk-1.

Most important caveat: MFF-1's repeat matches are weaker than the vertebrate consensus (best 12.55 bits versus 15.19 and 21.29 in human), and Pfam PF05644 does not reach its gathering threshold on MFF-1 at all, although it does on MFF-2 and human MFF. InterPro assigns MFF-1 only family-level IPR008518 (Mff/Tango-11) over residues 92-158, i.e. the coiled coil and tail anchor, not the repeats.

## Evidence matrix

| # | Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|---|
| 1 | This job, `mff_repeat_debiased_hits.csv` | Computational (motif PSSM, empirical null) | Supports | MFF-1 retains Mff repeat motifs | MFF-1 R2 at residue 39 (SVPEHITV) = 12.55 bits, p = 2.3e-5; R1 (res 2) 9.90, R3 (res 68) 9.06. Human R1 15.19, R2 21.29; Dm Tango11 R1 12.26, R2 19.18 | 12 MFF-family proteins, 175,800-window shuffled null, Met1 position excluded from the PSSM | Medium-high. The worm motif is real but weaker than vertebrate; only one of three clears the stringent threshold |
| 2 | This job, `mff_sw_alignments.csv` | Computational (Smith-Waterman + shuffled null) | Supports | The repeat region is orthologous, not a coincidental VPE match | Human MFF 40-100 vs MFF-1 1-80: SW 42, 36.0 % id over 50 aa, z = 4.59, p < 0.007; alignment places human R1/R2 opposite MFF-1 R1/R2 in register | BLOSUM62, gap 11/1, 150 shuffles | Medium-high. Short alignment; z-score from a composition-shuffled null, not a database E-value |
| 3 | This job, `mff_architecture_table.csv` | Computational (Kyte-Doolittle, AlphaFold DB) | Supports | MFF-1 has a coiled coil plus tail anchor | TM predicted 138-156 (KGLLLALIGAVITLAYSYL, KD peak 1.72), then exactly RR; AlphaFold helix 105-157, pLDDT 78.2. Human MFF: TM 322-340 then RR, helix 287-341, pLDDT 87.1 | AlphaFold DB models Q19343, P91344, Q9GZY8 | High for the tail anchor (unambiguous). Medium for the coiled coil: AlphaFold gives a confident helix but I could not run COILS/Marcoil, and a monomer helix is not proof of a coiled coil |
| 4 | PMID 21149567 (Otera 2010) | Direct assay + localisation | Supports (mammal) | MFF binds DRP1 directly | "Mff and Drp1 physically interacted in vitro and in vivo"; Mff knockdown releases Drp1 foci; Mff-CAAX redirects Drp1 to the plasma membrane | HeLa/MEF, mammalian | High for mammals. Does not localise the interaction to the repeats |
| 5 | PMID 18353969 (Gandre-Babbe & van der Bliek 2008) | Mutant phenotype + localisation | Supports (architecture) | MFF is a conserved tail-anchored fission factor | "Mff and Fis1 are both tail anchored in the mitochondrial outer membrane"; "a conserved membrane fission pathway"; identified via a Drosophila RNAi screen | Drosophila S2 cells, human cells | High. Establishes conservation of the module and the tail anchor, not worm function |
| 6 | PMID 26446846 (Liu & Chan 2015) | Direct assay + mutant | Qualifies | What determines MFF-DRP1 binding | "Mff cannot bind to assembly-deficient mutants of Drp1"; DRP1 insert B inhibits the interaction | Recombinant protein + cells, mammalian | High. Shifts the mapped determinant to the DRP1 side; no MFF repeat mutants |
| 7 | PMID 26578514 (Clinton 2016) | Direct assay (reconstitution) | Competing / qualifies | Is the MFF coiled coil the binding module? | "the coiled-coil motif in Mff is not essential for Drp1 interactions, but rather serves to augment cooperative self-assembly of Drp1 proximal to the membrane" | Purified DRP1 + lipid-anchored MFF | High. Means conservation of the coiled coil alone does not predict binding |
| 8 | PMID 34347505 (Liu, Kage & Higgs 2021) | Direct assay + mutant phenotype | Qualifies / supports | Role of the MFF coiled coil | MFF is a dynamic oligomer (probably trimer) via its C-terminal coiled coil, Kd ~10 microM; oligomerisation required for DRP1 activation and for MFF puncta | Purified proteins, TIRF; U2OS MFF-knockout rescue | High. Partly conflicts with #7 on whether the coiled coil matters for binding versus activation |
| 9 | PMID 26578513 (Macdonald 2016) | Direct assay | Qualifies | MFF function is isoform- and lipid-dependent | MFF stimulation of DRP1 cooperative GTPase differs between DRP1 splice isoforms and depends on cardiolipin | Purified proteins, liposomes | High. Shows the MFF-DRP1 functional readout is context-dependent, relevant when extrapolating across species |
| 10 | PMID 39998089 (Lan 2025) | Mutant phenotype (genetic) | Supports weakly (worm) | Do mff-1 and drp-1 act in the same pathway in C. elegans? | LIN-24-induced donut mitochondria "depends on genes involved in mitochondrial dynamics, including mff-1, mff-2, drp-1, and clk-1" | C. elegans, starvation/overexpression | Low-medium for the hypothesis. Genetic co-dependence in one stress paradigm, no binding or ordering data |
| 11 | PMID 39365854 (Seager 2024), PMID 39293584 (Hanada 2024) | Direct assay + mutant | Qualifies | Is the human regulatory layer transferable? | MFF SUMOylation at K151 and AMPK phosphorylation control fission; exon-6 splicing modulates it | Mouse MEF, human cells | High for mammals. All sites lie in the 205-aa linker that MFF-1 lacks (its linker is 29 aa) |
| 12 | InterPro / Pfam (database) | Database | Qualifies | Does a curated HMM call the MFF-1 repeats? | IPR008518 Mff/Tango-11 and PTHR16501 cover Q19343 92-158 only; PF05644 does not reach threshold on Q19343, but hits P91344 87-152 and Q9GZY8 27-342 | InterPro API, retrieved this job | High. Curated models recognise the C-terminal module in MFF-1, not the repeats |

## GO curation implications

All of the following are leads requiring curator verification.

**Do not assert a DRP-1 binding MF term for MFF-1 on this evidence alone.** The appropriate evidence class would be ISS/ISO from human MFF, and the inference chain has two weak links: the repeats are not experimentally mapped as the binding site in any species, and nothing in C. elegans has been measured.

Recommended handling:

| GO aspect | Candidate term | Lead action | Rationale |
|---|---|---|---|
| CC | `GO:0005741` mitochondrial outer membrane | Retain or add, high confidence | Unambiguous C-terminal tail anchor (TM 138-156 followed by RR), matching the human MFF topology (PMID 18353969). This is the best-supported computational call in the whole analysis |
| CC | `GO:0031307` integral component of mitochondrial outer membrane, or `GO:0098573` intrinsic component of mitochondrial membrane | Lead, prefer the generic `GO:0005741` until worm localisation is shown | Tail anchoring is predicted, not observed in C. elegans |
| BP | `GO:0000266` mitochondrial fission | Retain as a lead with ISS/IMP qualification | Supported by family membership plus the worm genetic co-dependence in PMID 39998089, which is weak but on-target |
| MF | DRP-1 binding, e.g. `GO:0019901` protein kinase binding is wrong; the relevant class is `GO:0005515` protein binding or a GTPase-receptor term | **Do not recommend.** If anything, record as a prediction/lead only | "Protein binding" is uninformative and the specific claim is unmapped. A more informative MF would be `GO:0140693` molecular condensate scaffold activity (no) or a receptor-style term; none is supported |
| MF | `GO:0090140` regulation of mitochondrial fission is BP, not MF; the closest defensible MF is none | Leave MF unannotated for MFF-1 | The gene product's molecular activity is "membrane-anchored receptor that recruits a dynamin GTPase". GO has no clean MF for this; curators usually express it as BP `GO:0000266` plus CC `GO:0005741` |

If the review currently carries an MF term asserting direct DRP-1 binding derived from this hypothesis, the lead is to **downgrade it to a prediction with ISS evidence and an explicit note that the binding site is unmapped**, not to accept it as a core function statement. If the review currently has no such term, the lead is **do not add one**.

## Mechanistic scope

The immediate molecular function being tested is: *MFF-1 is an integral outer-mitochondrial-membrane protein whose cytosol-facing N-terminal region physically binds DRP-1 and recruits it from the cytosol to the mitochondrial surface.*

Direct gene-product activity (what the hypothesis is really about):
- membrane insertion via a C-terminal tail anchor (predicted here, not observed in worm),
- homo-oligomerisation via a coiled coil (predicted here; required for DRP1 activation in mammals, PMID 34347505),
- physical association with DRP-1 (not measured in worm; direct in mammals, PMID 21149567),
- stimulation of DRP-1 GTPase/assembly (not measured in worm; mammalian, PMIDs 26578514, 26578513).

Downstream, and not evidence for the molecular claim:
- mitochondrial network morphology in mff-1 RNAi or mutants,
- the donut-mitochondria phenotype in PMID 39998089, which is two steps removed (a stress phenotype that requires several dynamics genes),
- peroxisomal fission, apoptosis timing and cytochrome c release, all of which are mammalian downstream readouts in PMID 18353969.

## Conflicts and alternatives

1. **The coiled coil conflict.** Clinton 2016 says the MFF coiled coil is dispensable for DRP1 binding; Liu/Higgs 2021 says the coiled coil drives oligomerisation and that oligomerisation is required for DRP1 activation. These are reconcilable (binding versus activation) but they mean the seed hypothesis's "coiled coil, therefore binding module" step is not safe. Worth flagging explicitly in the review.

2. **Paralog ambiguity between MFF-1 and MFF-2.** MFF-2 (P91344, 161 aa) is the *better* match to human MFF by every curated and computed measure I ran: Pfam PF05644 hits MFF-2 but not MFF-1; the C-terminal module aligns to human MFF at 40.0 % identity over 45 aa (z = 8.47) for MFF-2 versus 19.5 % over 77 aa (z = 4.53) for MFF-1; the single best repeat is 16.46 bits in MFF-2 versus 12.55 in MFF-1. If the two paralogs have diverged in function, carrying mammalian MFF inferences onto MFF-1 specifically is the riskier of the two transfers. UniProt also lists several shorter C. elegans MFF entries (G1K0W6 135 aa, G1K0W7 137 aa, A7LPG4 132 aa) that may be isoforms; isoform choice was not resolved here.

3. **MFF-1's annotated N-terminus.** The MFF-1 R1 motif begins at the initiator methionine itself (M1-QVPDHLSV), whereas vertebrate R1 begins around residue 21 after an N-terminal extension. Either the worm protein genuinely lacks that extension, or the gene model's start codon is mis-assigned. This matters because the motif score at position 1 is the most artefact-prone call in the analysis; I removed the Met position from the PSSM for exactly this reason, after which R1 drops below threshold (9.90 bits).

4. **Non-mitochondrial MFF function.** PMID 41832149 reports MFF acting on melanosome fission via ARP2/3, independent of DRP1. An MFF-family protein is not automatically a DRP1 receptor, and sequence conservation of the module does not discriminate these uses.

5. **Different receptor landscape in C. elegans.** UniProt searches find no MIEF1/MIEF2 (MiD51/MiD49) orthologue in C. elegans, consistent with those being vertebrate-specific. In worm the DRP-1 receptor candidates are MFF-1, MFF-2, FIS-1 (Q20291) and FIS-2 (Q6AHP8). This *raises* the prior that MFF-1/MFF-2 carry the receptor role, but it also means the worm pathway may be wired differently from the mammalian MFF/MiD/Fis1 arrangement.

6. **The regulatory layer does not transfer.** Human MFF's eleven annotated phosphosites, the AMPK sites S146/S172, the SUMO site K151 and the alternatively spliced exons all lie in a 205-residue central linker. MFF-1's corresponding linker is 29 residues with no recognisable counterpart sequence. Any statement about MFF-1 should stop at constitutive receptor architecture.

## Knowledge gaps

| Gap | What I checked | Why it matters for curation | What would resolve it |
|---|---|---|---|
| The MFF repeats have never been mutated and tested for DRP1 binding | Four PubMed query formulations; the retrieved mapping papers (26446846, 26578514, 34347505) map determinants elsewhere | The seed hypothesis's central premise is unsourced; a review that cites "key residues identified by mutagenesis in human MFF" would be citing a paper that I could not locate | An alanine scan or deletion of human MFF R1/R2 with a DRP1 co-IP or GTPase-stimulation readout |
| No C. elegans MFF-1/DRP-1 interaction data of any kind | PubMed for worm mff-1/mff-2; UniProt Q19343 is unreviewed TrEMBL with no interaction annotation | Determines whether the annotation can ever be better than ISS | Worm co-IP, split-GFP or Y2H between MFF-1 and DRP-1 |
| MFF-1 subcellular localisation in worm | No localisation paper found; the tail anchor is predicted only | `GO:0005741` would otherwise be ISS, not IDA | MFF-1::GFP knock-in, colocalisation with a mitochondrial marker, carbonate extraction |
| Whether MFF-1 and MFF-2 are redundant | Sequence comparison only; MFF-2 is the stronger human match | Determines whether single-gene statements are safe | mff-1, mff-2 single and double mutant mitochondrial morphology and DRP-1::GFP recruitment |
| Whether the MFF-1 helix 105-137 is a genuine coiled coil | AlphaFold monomer helix plus a crude heptad a/d enrichment score (0.57 for MFF-1, 0.65 for human). I could not run COILS, Marcoil, DeepCoil or AlphaFold-Multimer in this environment, and I am not inferring a coiled coil from the monomer helix alone | Oligomerisation is the module with demonstrated functional requirement in mammals | A proper coiled-coil predictor, or AlphaFold-Multimer homotrimer modelling, or SEC-MALS on the MFF-1 cytosolic domain |
| MFF-1 gene model / start codon | Noted that the R1 motif starts at Met1, unlike all other orthologs | Affects whether MFF-1 has two or three repeats and whether R1 exists at all | 5' RACE or ribosome-profiling start-site data from WormBase |

## Discriminating tests

Ranked by information per unit effort.

1. **MFF-1::GFP / DRP-1::mCherry colocalisation and recruitment in C. elegans.** If DRP-1 puncta are lost or redistributed in an *mff-1 mff-2* double mutant, the receptor role is established in worm and the ISS inference becomes an IMP-supported BP plus a defensible CC. This is the single highest-value experiment.
2. **Direct binding, worm proteins.** Purified MFF-1 cytosolic domain (residues 1-104) against purified DRP-1 (Q8WQC9), by pull-down or ITC, with MFF-2 run in parallel. Reads out the paralog question at the same time.
3. **Repeat-deletion rescue.** Rescue *mff-1* loss with MFF-1 lacking R1, R2, R3 individually and in combination. This is the experiment the seed hypothesis implicitly assumes already exists in human, done in the organism being curated.
4. **Coiled-coil swap.** Replace the MFF-1 105-137 segment with a GCN4 trimer or a monomerising mutant, as Liu/Higgs 2021 did for human MFF, and score DRP-1 recruitment. Discriminates "binding module" from "oligomerisation module".
5. **Comparative, cheap, and I could not run it here:** AlphaFold-Multimer on MFF-1 (1-104) plus the DRP-1 stalk, with human MFF plus human DRP1 as a positive control. If the worm repeats dock onto the orthologous DRP-1 surface with a reasonable ipTM, that is real supporting evidence for the specific claim; if they do not, the hypothesis weakens considerably.
6. **Carbonate extraction / protease protection** on worm mitochondria to confirm tail-anchor topology rather than predict it.

## Curation leads

All leads require curator verification.

**Candidate references, with snippets to verify against the abstracts:**

- PMID 21149567 (Otera 2010). Snippet: "Mff and Drp1 physically interacted in vitro and in vivo". Use for: direct MFF-DRP1 interaction in mammals, as the ISS source. Note it does not localise the interaction.
- PMID 18353969 (Gandre-Babbe & van der Bliek 2008). Snippet: "Mff and Fis1 are both tail anchored in the mitochondrial outer membrane, but other parts of these proteins are very different and they exist in separate 200-kDa complexes". Use for: tail-anchor architecture and pathway conservation.
- PMID 26578514 (Clinton 2016). Snippet: "the coiled-coil motif in Mff is not essential for Drp1 interactions, but rather serves to augment cooperative self-assembly of Drp1 proximal to the membrane". Use for: the caveat that coiled-coil conservation does not imply binding.
- PMID 34347505 (Liu, Kage & Higgs 2021). Snippet: "Mff is an oligomer (most likely a trimer) that dynamically associates and disassociates through its C-terminal coiled coil, with a Kd in the range of 10 µM. Dynamic Mff oligomerization is required for Drp1 activation." Use for: the functional role of the module that *is* well conserved in MFF-1.
- PMID 26446846 (Liu & Chan 2015). Snippet: "Mff cannot bind to assembly-deficient mutants of Drp1, suggesting that Mff selectively interacts with higher-order complexes of Drp1." Use for: the mapped determinant lies on DRP1.
- PMID 39998089 (Lan 2025). Snippet: "This mitochondrial remodeling depends on genes involved in mitochondrial dynamics, including mff-1, mff-2, drp-1, and clk-1." Use for: the only worm-specific mff-1/drp-1 link, explicitly labelled as genetic co-dependence.

**Possible action changes:**

- Replace any statement of the form "MFF-1 binds DRP-1 directly" with "MFF-1 retains the MFF repeat/coiled-coil/tail-anchor architecture and is predicted to act as a DRP-1 receptor; direct binding has not been tested in C. elegans and the repeat motifs have not been mapped as the binding site in any species."
- Keep `GO:0000266` mitochondrial fission as a BP lead with ISS or IMP (PMID 39998089) evidence.
- Add or retain `GO:0005741` mitochondrial outer membrane as the best-supported CC lead, flagged as predicted from the tail anchor.
- Do not add an MF term asserting DRP-1 binding. Do not fall back on `GO:0005515` protein binding as the recommendation.

**Suggested questions for the curator:**

- Does the review distinguish MFF-1 from MFF-2? MFF-2 is the stronger human match on every measure here, so claims built from human MFF transfer to MFF-2 more safely than to MFF-1.
- Does the review cite a specific human MFF repeat mutagenesis paper? If so, that reference should be checked, because I could not find one.
- Which MFF-1 isoform does the review annotate? UniProt lists Q19343 at 158 aa plus several shorter C. elegans MFF entries.

**Suggested experiments:** items 1-4 in Discriminating Tests, with item 1 (DRP-1::GFP recruitment in an *mff-1 mff-2* double mutant) as the priority.

## Limitations of this analysis

- All sequence analysis is my own; I could not run HMMER, COILS, Marcoil, TMHMM/DeepTMHMM, Phobius or AlphaFold-Multimer in this environment, and I did not substitute guesses for them. The coiled-coil call rests on an AlphaFold monomer helix plus a crude heptad enrichment statistic, which is weaker than a dedicated predictor.
- PSSM and Smith-Waterman significance come from composition-shuffled nulls, not from database-wide E-values. The z-scores are informative about whether the match beats chance for these specific sequence pairs, not about genome-wide false-discovery rate.
- The PubMed tool used here appears to rank by recency and returns nothing for narrowly phrased queries, so absence of a repeat-mutagenesis paper is a failure to find, not a proof of absence. A curator should re-check with full Boolean PubMed and Google Scholar before relying on that negative.
- Local `*-bioinformatics` files in the AI Gene Review repository were deliberately withheld from this run, so this report does not reconcile with them.

## Provenance files

- `provenance/plot_1.png`: three-panel architecture comparison (repeat positions with PSSM scores, repeat score profile with empirical threshold, AlphaFold pLDDT traces) for human MFF, Drosophila Tango11, C. elegans MFF-1 and MFF-2.
- `provenance/plot_2.png`: linker-length comparison showing the 205-aa human regulatory linker versus 29 aa in MFF-1.
- `mff_repeat_pssm_hits.csv`, `mff_repeat_debiased_hits.csv`: motif scan output before and after removing the Met1 position.
- `mff_sw_alignments.csv`: Smith-Waterman scores, identities, shuffled means, z-scores and empirical p-values.
- `mff_architecture_table.csv`: per-protein repeat calls, predicted TM span and sequence, and post-TM C-terminal residues.
- `mff_orthologs.json`, `afdb_plddt.json`: the exact sequences and AlphaFold confidence values used.
