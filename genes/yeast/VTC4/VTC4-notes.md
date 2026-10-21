# VTC4 (P47075, YJL012C) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised reference ortholog for N. crassa vtc-4
(Q7SCX0). ProtNLM2 output was not consulted.

### Deep research

`just deep-research-falcon yeast VTC4 --fallback perplexity-lite` failed: falcon returned
"Exception: Failed to authenticate" and the perplexity-lite fallback returned HTTP 401
(insufficient quota). No deep-research file exists. The review is built from the 13 cached
publications (4 with full text: PMID:11102525, PMID:11823419, PMID:19841731, PMID:26928762,
PMID:36759618), the abstracts of the rest, the curated UniProt record, and the PMC full text of
PMID:17079729 read via web fetch (not cached locally).

### Evolutionary placement

- PANTHER PTHR46140:SF1 (VACUOLAR TRANSPORTER CHAPERONE COMPLEX SUBUNIT 4-RELATED). Note that SF1 also
  contains yeast VTC1 (P40046, 129 aa, TM-only), so SF1 membership alone is not sufficient for transfer
  of polyP kinase activity; the full SPX + TTM (VTC) + 3-TM architecture with the conserved
  catalytic residues is the relevant criterion
  (`interpro/panther/PTHR46140/PTHR46140-entries.csv`). VTC2 and VTC3 are SF2.
- P47075 is itself an experimental donor at PTN001646574 (polyP kinase activity, polyP biosynthesis,
  VTC complex, ER), together with T. brucei Vtc4 (Q382V9). Its own appearance in WITH/FROM is expected.
- N. crassa phylogeny (genes/NEUCR/vtc-4/vtc-4-bioinformatics/RESULTS-rereview.md) places VTC-4 in a
  Vtc4 clade with yeast Vtc4 and S. pombe vtc4, separate from the Vtc2/Vtc3 clade.

### What is experimentally established in S. cerevisiae

1. Polyphosphate polymerase (polyP kinase, EC 2.7.4.1) catalytic subunit. Crystal structures of the
   central TTM/VTC domain (aa 189-480) with ATP show polyP winding through a tunnel; metal-assisted
   gamma-phosphate transfer to an acceptor phosphate [PMID:19390046 "Nucleotide- and phosphate-bound
   structures suggest that the enzyme functions by metal-assisted cleavage of the ATP gamma-phosphate,
   which is then in-line transferred to an acceptor phosphate to form polyP chains."]. Mutagenesis
   R264A/R266A abolishes activity; active-site K458; Mn2+ dependence (UniProt, ECO:0000269).
   VTC2/VTC3 carry I/L at the active-site lysine position, so VTC4 is the only catalytic subunit.
2. Required for polyP accumulation in vivo: phm3 (= vtc4) deletion lacks detectable polyP
   [PMID:11102525 "Both the phm3 Δ and phm4 Δ mutants lacked detectable polyP."]; confirmed by in-cell
   31P-NMR [PMID:36759618 "We found that vtc1 and vtc4 are essential for the generation of the vacuolar polyP"].
3. Coupled synthesis and translocation into the vacuole lumen. Reconstituted VTC imports polyP it
   synthesises; cytosolic polyP is not imported; TM mutations block both synthesis and import
   [PMID:25315834]. Cryo-EM (Vtc1:Vtc3:Vtc4 = 3:1:1) shows a 15-TM channel to which each subunit
   contributes TM1; Vtc4 K622A/R629A in TM1 reduces synthesis and channel-residue mutations eliminate
   the vacuolar polyP store [PMID:36759618, PMID:37066886]. Vtc4 thus contributes structurally to
   polyP transmembrane transport. No GO term for polyP transmembrane transport exists;
   GO:0034486 vacuolar transmembrane transport (not a descendant of GO:0007034 vacuolar transport,
   checked via OLS hierarchicalAncestors) is the best available.
4. Regulation by inositol (pyro)phosphates via its SPX domain. SPX-Vtc4 crystal structures with InsP6
   (PDB 5IIG/5IIT), binding-surface mutations impair InsP binding and polyP synthesis [PMID:27080106];
   in the full complex it is the SPX of Vtc4, not Vtc3, that senses InsP6 [PMID:36759618].
5. Subunit of the VTC complex (GO:0033254): co-IP of Vtc1-Vtc4 [PMID:11823419], cryo-EM structures
   [PMID:36759618, PMID:37066886].
6. Localization: vacuolar membrane (major), ER/nuclear envelope and cell periphery
   (Vtc1-Vtc2-Vtc4 subcomplex), relocating to vacuole under starvation [PMID:17079729; PMID:19390046].
   PMC1751332 full text: "All GFP-Vtc fusions localized to the ER, marking the nuclear rim."

### Secondary / non-core roles

- Vacuole fusion: vtc4Δ vacuoles do not fuse in vitro and anti-Vtc4 antibodies inhibit fusion; Vtc1/Vtc4
  required for Sec18/NSF priming and LMA1 binding [PMID:11823419]. Later work suggests at least part of
  this is mediated by lumenal polyP signalling to SNAREs [PMID:27252384]. Not in GOA for VTC4; I did not
  add a NEW fusion term (mechanism of participation unclear; may be indirect via polyP). Raised as a
  question.
- Microautophagy: VTC complex enriched on autophagic tubes, required for scission of microautophagic
  vesicles [PMID:17079729]. PMC full text: "Both Vtc3p and Vtc4p were enriched about twofold on the
  membranes forming the invaginations versus the vacuolar boundary membrane." and "Vacuoles derived from
  all four knockout strains showed a significant reduction of microautophagic activity." These autophagic
  tubes are vacuolar membrane invaginations, not autophagosomes, so GO:0000421 autophagosome membrane and
  GO:0061736 engulfment of target by autophagosome (macroautophagy-specific by definition) are wrong terms.
- Calmodulin binding: PMC full text reports the central cytosolic Vtc4 domain (aa 183-487)
  "bound to Cmd1p-Sepharose in the presence and in absence of free Ca2+" and "Both Vtc2p, Vtc3p, and
  Vtc4p coimmunoprecipitated with Cmd1p." Genuine but peripheral.
- V-ATPase: vtc4Δ vacuoles carry fewer V1 subunits; slight reduction in H+ uptake [PMID:12584253].

### Transfer guidance (for N. crassa vtc-4 and other Vtc4 orthologs)

Transferable with phylogenetic grounding (Vtc4 clade, SF1, catalytic residues retained): polyP kinase
activity, polyP biosynthesis, VTC complex membership, vacuolar membrane localization, SPX-InsP binding
(if basic surface conserved). Not to be transferred on homology alone: ER/cell-periphery localization
(subcomplex- and condition-specific in yeast), vacuole fusion, microautophagy, calmodulin binding.
