# SIRV1 protein 114 (Q8QL27) — curation notes

## HEADLINE: this accession IS the assayed AcrIII-1 ring nuclease

`modules/anti_crispr_suppression.yaml` records an open curation gap:

> Which specific DUF1874-family protein was assayed as the AcrIII-1 ring nuclease cannot
> be established from local data, so the family is grounded by InterPro with a reviewed
> SIRV1 member as an orienting exemplar rather than by the assayed accession.

and the annoton description says the exemplar "orients the family without asserting that
this particular accession is the assayed protein."

**That gap is resolved, and the answer is that the orienting exemplar and the assayed
protein are the same molecule.** Four independent lines, each checkable:

**1. The paper's own identifier.** The phylogenetic methods name the query sequence by
RefSeq accession:
[PMID:31942067 "AcrIII-1 homologs were collected by using gp29 (NP_666617) of SIRV1 as a query"].
The UniProt record for Q8QL27 carries `DR RefSeq; NP_666617.1; NC_004087.1.` NCBI
`efetch` of NP_666617.1 returns `DUF1874 domain-containing protein [Sulfolobus islandicus
rod-shaped virus 1]` with the sequence

```
MNKVYLANAFSINMLTKFPTKVVIDKIDRLEFCENIDNEDIINSIGHDSTIQLINSLCGTTFQKNRVEIK
LEKEDKLYVVQISQRLEEGKILTLEEILKLYESGKVQFFEIIVD
```

which is **character-for-character identical** to the Q8QL27 sequence block.

**2. The deposited structure.** The data-availability statement gives one PDB code
[PMID:31942067 "The structural coordinates and data have been deposited in the Protein Data Bank with deposition code 6SCF."],
and that structure is the cA4 complex
[PMID:31942067 "we co-crystallised an inactive variant (H47A) of SIRV1 gp29 with cA4 and solved the structure to 1.55 Å resolution"].
`PDB; 6SCF; X-ray; 1.55 A; A/B/C/D/E/F/G/H=1-114` is cross-referenced from Q8QL27, and the
RCSB entry record gives 6SCF's primary citation as "An anti-CRISPR viral ring nuclease
subverts type III CRISPR immunity" with structure title "A viral anti-CRISPR subverts type
III CRISPR immunity by rapid degradation of cyclic oligoadenylate". Resolution, ligand and
chain range all match.

**3. The catalytic residues.** The paper's alignment legend names four conserved residues
[PMID:31942067 "Conserved residues H47, R66, R85 and E88 are indicated by asterisks."],
and H47A is the inactive variant used for co-crystallisation. Counting into the Q8QL27
sequence: position 47 = **H**, 66 = **R**, 85 = **R**, 88 = **E**. All four match at the
exact positions. A chance match of four specified residue identities at four specified
positions is not a coincidence worth entertaining.

**4. The apo structure.** The paper's introduction cites a pre-existing structure of the
family member it then assays
[PMID:31942067 "Structures are available for several family members, including gp29 of Sulfolobus islandicus rod-shaped virus 1 (SIRV1) 17 and B116 of Sulfolobus turreted icosahedral virus (STIV) 18."].
Q8QL27 carries `PDB; 2X4I; X-ray; 2.20 A`, whose RCSB structure title is "ORF 114a from
Sulfolobus islandicus rudivirus 1" — i.e. the apo structure of this protein. The
cA4-induced loop movement the paper reports was measured against it.

**Naming note, which is what obscured this.** The literature calls the protein "gp29"
(presumably gene 29 of the SIRV1 genome), UniProt calls it "Uncharacterized protein 114"
and `ORFNames=114`, PDB calls it "ORF 114a", and the directory here is `orf114`. Those are
four names for one molecule, numbered by different conventions. RefSeq NP_666617 is the
join that makes them one.

**Recommended module edits** (to `modules/anti_crispr_suppression.yaml`):
- Close the third knowledge gap, with `NP_666617` plus PDB 6SCF as the resolution.
- Remove the `description` caveat on the `representative_members` entry for
  `UniProtKB:Q8QL27` ("it orients the family without asserting that this particular
  accession is the assayed protein") — it is the assayed protein.
- The `acriii1_ring_nuclease` annoton can carry experimental-grade evidence rather than
  family-level inference.

## What the protein does

Discovery framing
[PMID:31942067 "Here, we investigated the DUF1874 protein, which is conserved and widespread in a variety of archaeal viruses and plasmids, bacteriophages and prophages (Extended Data Fig.1), for an Acr function."].

The mechanism is attack on the **signalling layer** of type III CRISPR immunity, not on any
Cas protein
[PMID:31942067 "Here we identify a new family of viral anti-CRISPR (Acr) enzymes that rapidly degrade cyclic tetra-adenylate (cA4). The viral ring nuclease AcrIII-1 is widely distributed in archaeal and bacterial viruses and in proviruses."],
[PMID:31942067 "The enzyme uses a previously unknown fold to bind cA4 specifically, and a conserved active site to rapidly cleave this signalling molecule, allowing viruses to neutralize the type III CRISPR defence system."],
and the consequence of attacking a messenger rather than a protein is host-range breadth
[PMID:31942067 "The AcrIII-1 family has a broad host range, as it targets cA4 signalling molecules rather than specific CRISPR effector proteins."].

Enzymology, on this protein specifically
[PMID:31942067 "we cloned and expressed two family members in E. coli: the SIRV1 gp29 protein and the YddF protein encoded by an integrative and conjugative element ICEBs1 from B. subtilis"],
[PMID:31942067 "Both proteins possess a potent ring nuclease activity, rapidly degrading cA4 to generate linear di-adenylate (ApA>P) with a cyclic 2’,3’ phosphate"],
[PMID:31942067 "With a catalytic rate exceeding 5 min-1, the Acr enzyme is at least 60-fold more active than the cellular ring nuclease Crn1 from S. solfataricus."],
[PMID:31942067 "Both SIRV1 gp29 and YddF enzymes show a strong preference for cA4 over cA6"].

Structure: a dimer with the substrate in the interface, on a fold unrelated to the only
previously known cOA-binding module
[PMID:31942067 "The complex reveals a molecule of cA4 bound at the dimer interface."],
[PMID:31942067 "The structure of AcrIII-1 is unrelated to the CARF domain, which is the only protein family thus far known to bind cOA"].

In vivo, gain of function in the host: expressing *this* gene from a plasmid in a
*Sulfolobus islandicus* strain whose only defence is type III-B rescues an unrelated,
*duf1874*-less lytic virus from CRISPR immunity
[PMID:31942067 "However, the same cells expressing the SIRV1 gp29 gene from a plasmid were readily infected, giving rise to plaque formation. These data are consistent with the hypothesis that SIRV1 gp29 is functioning as an Acr specific for type III CRISPR defence."].
This is the single most important experiment for annotation purposes, because it is in a
living host, it is on this exact gene, and it establishes sufficiency.

## Erratum check

PubMed lists an erratum/matters-arising-style entry for this paper
(`Nature. 2025 Apr;640(8059):E8-E14. doi: 10.1038/s41586-025-08649-0`). I could not
retrieve its content from the cache and have not read it, so I cannot say what it
revises. The annotations proposed here are flagged with that caveat in
`reference_review.review_notes`, and the paper is **not** marked `is_invalid`, since a
listed comment is not a retraction and I have no evidence it affects the gp29 results.
A curator with access should read it before finalising.

## Ontology

GO has no term for cleaving a cyclic oligoadenylate second messenger. QuickGO searches for
"ring nuclease" return only the generic nuclease terms and the nuclease
inhibitor/activator terms; searches for "cyclic oligoadenylate" return `GO:0001730
2'-5'-oligoadenylate synthetase activity` (the metazoan OAS enzyme, a different molecule
and the wrong direction) and the cyclic-nucleotide-binding and phosphodiesterase terms,
none of which fit. `GO:0004521 RNA endonuclease activity` is defensible and is asserted as
the nearest existing term — cA4 is a tetrameric ribonucleotide and ring opening is an
internal phosphodiester cleavage — but it loses the substrate, which is the whole point.
A new term `cyclic oligoadenylate ring nuclease activity` is proposed under GO:0004521.
It would also serve the host-encoded Crn1/Crn2 self-regulators (e.g. UniProtKB:Q97YD2),
which the module explicitly excludes from its own boundary but which share the chemistry,
so the term is not a one-gene request.

## Status of the UniProt record

Reviewed Swiss-Prot entry, but still `RecName: Full=Uncharacterized protein 114`, with no
FUNCTION line and zero GOA annotations, six years after a *Nature* paper characterised it
enzymatically, structurally and in vivo. This is the most striking curation gap in this
round, and unlike the TrEMBL cases it is a *reviewed* entry, so it should be
straightforward to fix.

## 2026-10-26: expression context and the 2025 AcrIII-1 exchange

The original protein identity and purified cA4 ring-nuclease activity remain supported by PMID:31942067. PubMed metadata for PMID:40240860 and PMID:40240850 were fetched normally; neither cache has an informative abstract. Normal URL fetching preserved the publisher previews and figure captions at https://www.nature.com/articles/s41586-025-08649-0 and https://www.nature.com/articles/s41586-025-08650-7?error=cookies_not_supported. These are subscription previews, not full experimental articles. Author-portal searching did not supply complete text.

The Comment's figure caption explicitly contrasts virus-encoded and plasmid-expressed gp29/gp37. The Reply preview reiterates cA4 nuclease activity and the plasmid-expression phenotype. This is sufficient to remove an unqualified claim of native counterdefence from the description and core process, but insufficient to declare the biochemical/plasmid phenotype false or to rule out every native infection context. The earlier NEW process row is retired and retained as UNDECIDED provenance pending full adjudication; it was not an imported GOA assertion. The three existing proposed molecular-function/location rows remain, with inferred host-cytoplasmic action stated as such. No additional GO rows were created.

A live QuickGO search on 2026-10-26 found no dedicated cyclic-oligoadenylate ring-nuclease term. The proposed term is retained; its definition now says endonucleolytic cleavage rather than assuming water-mediated hydrolysis, because the reported products carry a cyclic phosphate. GO-CAM/family scope must distinguish host regulatory Crn2 proteins and effective viral counterdefence rather than propagating the latter to all DUF1874 proteins.

Falcon with the configured Perplexity fallback was attempted and failed authentication/quota checks; the manual primary-source audit above is the research record. Publication caching completed independently. The review validates after the changes.

## 2026-10-26: independent scientific QA and public primary-text inspection

This entry supersedes the earlier Erratum check and the initial statement that the exchange could not be read. The [public reproduction](https://www.scribd.com/document/850988680/s41586-025-08650-7) displays both primary articles, with their printed Nature titles, authors, DOI and page headers. Its main texts were inspected through publicly indexed OCR. Normal ReferenceFetcher URL caching succeeded, but the resulting source file contains the landing page rather than the main-text OCR. The generated upload title and synopsis are not evidence. Publisher/PubMed caches remain incomplete and were not edited.

The infection study concerns SIRV2 native gp37 and SIRV1 gp29 transplanted into SIRV2, with an early-expression rescue. It does not directly establish native SIRV1 infection behavior. The Reply disputes physiological generalization and raises possible experimental confounders; those objections remain attributed to its authors. The retired UNDECIDED process proposal now rests on unresolved native scope, not inaccessible text or denial of the measured phenotype. The nuclease, substrate-binding and inferred host-cytoplasm proposals remain supported.

Chemistry/rate corrections follow PMID:31942067 directly. Its methods use enzyme excess for single-turnover measurements (4 micromolar dimer versus approximately 200 nanomolar cA4, 50 degrees Celsius). The reported rate is therefore not presented as steady-state kcat. The proposed term specifies cleavage of an internal 3'-5' linkage and a 2',3'-cyclic-phosphate product; it does not assume water-mediated hydrolysis or make universal effector inactivation part of the molecular-function definition. The older family-wide anti-CRISPR findings are now explicitly the original authors' interpretation. Suggested experiments distinguish the available SIRV2 system from a future SIRV1 experiment, and require direct participation evidence in addition to knockout necessity. All four annotation payloads were preserved.


## PR5555 follow-up: canonical sources and evidence scope (2026-10-25)

Removed the Scribd entry and both publisher URL variants from the current bibliography. The Comment and Reply now have one canonical PMID identity each (40240860/40240850). The old public-reproduction account above is historical provenance only and is not a canonical reference. Normal PMID refresh: 40240860 returned HTTP429; 40240850 remained abstract-only without informative text. No cache was hand-edited. The original publisher previews and newly normally fetched Figure 1/2 captions are inspected and extracted by `orf114-source-analysis/extract_publisher_previews.py`; the generated excerpt file and manifest retain exact strings, canonical PMIDs/DOIs, stable publisher URLs and input hashes. Figure 2 identifies SIRV2 Para-gp29 explicitly. Its caption supports the construct and induction design; detailed earlier main-text conclusions remain attributed to the earlier inspection and are not newly claimed to be in a complete normal cache. The Reply preview establishes the authors' continued chemistry/plasmid claim, not all objections discussed in its full text. The retired UNDECIDED process decision and all four original row payloads remain unchanged.

Moved the ONTOLOGY-only gap to its already-present proposed ring-nuclease term; creating the GO term and then replacing the proposed-name core remains ontology work. The resolved CURATION-only identity gap is recorded here: Q8QL27 matches assayed gp29 through NP_666617 and PDB 6SCF; historical nomenclature obscured that mapping. Updating the Swiss-Prot name/function is a curator question, now represented in suggested_questions, not an experimental knowledge gap. Native expression/infection scope remains the sole biological knowledge gap.
