# PARK7/DJ-1 Gene Review Notes

## Gene Identity
- **UniProt ID:** Q99497 (PARK7_HUMAN)
- **Gene Symbol:** PARK7
- **Protein Name:** Parkinson disease protein 7 / DJ-1
- **Alternative names:** Maillard deglycase, Oncogene DJ1, Parkinsonism-associated deglycase
- **EC numbers:** 3.1.2.-, 3.5.1.-, 3.5.1.124
- **Family:** Peptidase C56 family (PfpI/Hsp31/DJ-1 superfamily)
- **Size:** 189 amino acids, homodimer
- **Critical residue:** Cys-106 (active site, easily oxidized to sulfinic acid; essential for most activities)

## Key Functional Summary

PARK7/DJ-1 is a multifunctional protein whose precise molecular function remains controversial. It plays an important role in cell protection against oxidative stress and is causatively linked to autosomal recessive early-onset Parkinson disease (PARK7, OMIM:606324).

### Core biochemical activities (established):

1. **Glyoxalase activity (weak but confirmed):** Converts methylglyoxal/glyoxal to lactate/glycolate in a GSH-independent manner. This activity is consistently observed but is much weaker than canonical glyoxalases [PMID:22523093 "Human DJ-1 and its homologs are novel glyoxalases"; PMID:31653696 "kcat is 0.02 sec(-1) for glyoxalase activity"]

2. **Protein deglycase activity (CONTROVERSIAL):**
   - **FOR:** Richarme et al. demonstrated DJ-1 repairs methylglyoxal- and glyoxal-glycated cysteine, arginine and lysine residues in proteins [PMID:25416785 "DJ-1 is a protein deglycase that repairs methylglyoxal- and glyoxal-glycated amino acids and proteins by acting on early glycation intermediates"]. Also demonstrated nucleotide deglycase activity for guanine glycation repair [PMID:28596309 "DJ-1 and its prokaryotic homologs constitute a major nucleotide repair system that we name guanine glycation repair"]
   - **AGAINST:** Pfaff et al. found no evidence for deglycase activity in Drosophila and attributed in vitro cysteine deglycase activity to a TRIS buffer artifact [PMID:27903648]. Andreeva et al. showed the apparent deglycase activity results from glyoxalase-mediated removal of free methylglyoxal shifting equilibrium, causing spontaneous hemithioacetal decomposition [PMID:31653696 "DJ-1 does not possess protein deglycase activity"]. DJ-1 knockout HEK293 cells showed no difference in MGO adduct levels.
   - **RESOLUTION:** UniProt notes both sides. The weight of evidence suggests DJ-1 has glyoxalase activity that may appear as deglycase activity due to equilibrium shifts. True deglycase activity remains unresolved.

3. **Oxidative stress sensor/chaperone:** Cys-106 oxidation to sulfinic acid acts as a redox sensor [PMID:12939276; PMID:15181200]. Functions as a redox-dependent molecular chaperone inhibiting alpha-synuclein aggregation [PMID:15502874 "DJ-1 is a redox-dependent molecular chaperone that inhibits alpha-synuclein aggregate formation"]

4. **Copper chaperone for SOD1:** DJ-1 acts as a copper chaperone for SOD1 activation, facilitates copper delivery [PMID:24567322 "DJ-1 is a copper chaperone acting on SOD1 activation"]. Binds both Cu(I) and Cu(II) [PMID:23792957; PMID:24144264].

5. **Protease activity:** Undergoes C-terminal cleavage and activation of protease activity in response to oxidative stress [PMID:20304780 "Parkinson disease protein DJ-1 converts from a zymogen to a protease by carboxyl-terminal cleavage"]. However, the 1.1A crystal structure study found lack of proteolytic activity [PMID:12855764].

6. **Transcription coactivator:** Acts as transcriptional co-activator, upregulates tyrosine hydroxylase by inhibiting sumoylation of PSF [PMID:16731528]. Protects against neuronal apoptosis as transcriptional co-activator [PMID:15790595].

### Key protective mechanisms:

1. **NFE2L2/Nrf2 stabilization:** Stabilizes the antioxidant transcriptional master regulator Nrf2 by preventing its Keap1-mediated ubiquitination and proteasomal degradation [PMID:17015834 "DJ-1, a cancer- and Parkinson's disease-associated protein, stabilizes the antioxidant transcriptional master regulator Nrf2"]

2. **NF-kappaB pathway modulation:** Enhances cell survival by binding OTUD7B/Cezanne, a negative regulator of NF-kappaB [PMID:21097510]

3. **TRAIL-induced apoptosis inhibition:** Blocks pro-caspase-8 recruitment to FADD [PMID:21785459]

4. **Mitochondrial protection:** Part of PINK1-PRKN-DJ-1 complex promoting unfolded protein degradation [PMID:19229105]. Mitochondrial localization enhanced by Cys-106 oxidation, leads to enhanced neuroprotection [PMID:18711745]. Binds mitochondrial complex I and maintains its activity [PMID:19822128].

5. **Histone glycation protection:** Protects histones from adduction by methylglyoxal, controls levels of methylglyoxal-derived arginine modifications on chromatin [PMID:30150385; PMID:30894531]

### Subcellular localization:
- Predominantly cytoplasm, also nucleus and mitochondrion
- Translocates to mitochondrion then nucleus in response to oxidative stress [PMID:18711745]
- Also found in lipid rafts (via palmitoylation), endoplasmic reticulum, PML bodies
- Detected in extracellular exosomes

### Androgen receptor signaling:
- Positive regulator of androgen receptor signaling pathway [PMID:11477070; PMID:12612053; PMID:17510388]
- Binds androgen receptor directly [PMID:17510388]
- This may relate to male fertility functions rather than core neuroprotective function

### Dopamine biosynthesis:
- Activates tyrosine hydroxylase (TH) and L-DOPA decarboxylase [PMID:19703902]
- Transcriptionally upregulates TH by inhibiting PSF sumoylation [PMID:16731528]
- Relevant to Parkinson's disease pathology

### RNA binding:
- Binds mRNAs with GG/CC motifs and partially inhibits translation; dissociates under oxidative stress [PMID:18626009]

### Metal binding:
- Binds copper (Cu(I) and Cu(II)) and toxic mercury ions [PMID:23792957; PMID:24144264]

## Disease association
- Autosomal recessive early-onset Parkinson disease (PARK7)
- Disease-causing variants: L166P (most studied), E64D, A104T, D149A, E163K, etc.
- L166P is rapidly degraded by proteasome, impairs homodimerization [PMID:12851414; PMID:14713311]
- Also associated with oncogenic transformation (originally identified as oncogene DJ1 [PMID:9070310])

## Assessment of annotation landscape

The gene has ~150 GO annotations, many of which are highly specific downstream effects rather than core molecular functions. Key issues to watch for:
1. Many annotations describe downstream effects of oxidative stress protection rather than direct molecular function
2. The deglycase/glyoxalase controversy means some annotations may need careful evaluation
3. Multiple "protein binding" IPI annotations should be evaluated for more specific binding terms
4. Several redundant location annotations from different evidence types
5. Androgen receptor signaling annotations may be non-core for most biological contexts
