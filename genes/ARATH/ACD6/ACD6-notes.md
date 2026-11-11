# ACD6 (At4g14400, Q8LPS2) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: ACD6 was requested as the closest experimentally characterised relative of a
maize PGG-domain protein (A0A804UIX9). That relationship is only a shared Pfam PF13962 (PGG)
domain plus ankyrin repeats; A0A804UIX9 is in PANTHER PTHR24177 while ACD6 is in
PTHR24186:SF46 ("PROTEIN ACCELERATED CELL DEATH 6-LIKE"). No PAINT node or subfamily joins
them, so nothing below should be read as transferable to that protein. ProtNLM2 output was not
consulted.

### Deep research

`just deep-research-falcon ARATH ACD6 --fallback perplexity-lite` failed: falcon returned
"Edison API request failed: Failed to authenticate" (HTTP 403), and the perplexity-lite fallback
also failed. No deep-research file exists; this review is built from the cached primary papers
(all eight GOA references) and the curated UniProt record.

### Family / evolutionary placement

- PANTHER PTHR24186 (ankyrin repeat domain-containing), subfamily SF46 (ACD6-like). Reviewed
  members of PTHR24186 in the PANTHER cache: ACD6 (SF46), ITN1 (SF48), At5g02620 (SF26),
  At2g01680 (SF2), rice NPR4 (SF42), E. coli ArpA (SF38). None besides ACD6 has a
  defense-signaling function that could be transferred, and nothing has been transferred.
- The only IBA is `membrane` from PTN000652806, with ACD6 itself (AT4G14400) in WITH/FROM.
  PAINT propagated only a membrane location from this family, no process or function: a
  deliberate, conservative node choice.
- Lu et al. 2003 [PMID:14507999 "ACD6 encodes a novel protein with putative ankyrin and transmembrane regions. It is a member of one of the largest uncharacterized gene families in higher plants."]
  and noted 34 ACD6-like Arabidopsis proteins, none with assigned function at the time.
- Architecture (UniProt): N-terminal ~70 aa disordered/unique region, ~10 ANK repeats (66-428),
  then six predicted TM helices (457-659) that correspond to the PGG domain region. Topology
  (cytoplasmic ankyrin domain) is experimentally supported [PMID:16297071 "ACD6 localizes to the plasma membrane and is an integral membrane protein with a cytoplasmic ankyrin domain."].

### Experimentally established in Arabidopsis

1. Positive, dose-dependent regulator of SA-dependent defense.
   - gain-of-function acd6-1 (L591F in TM helix): dwarf, spontaneous cell death, high SA,
     resistance to P. syringae; all SA dependent [PMID:10488236 "The acd6-conferred phenotypes are suppressed by removing a key signaling molecule, salicylic acid (SA), by using the nahG transgene"].
   - loss of function (acd6-T, RNAi): reduced SA after infection, increased susceptibility
     [PMID:14507999 "Thus, ACD6 is a necessary and dose-dependent activator of the defense response against virulent bacteria and can activate SA-dependent cell death."].
   - Overexpression primes defenses; affects SA-dependent and SA-independent defenses
     [PMID:16297071 "ACD6 overexpression confers enhanced disease resistance by priming stronger and quicker defense responses"].
   - Natural hyperactive alleles (Est-1) confer broad resistance to fungi (G. orontii,
     G. cichoracearum), oomycete (H. arabidopsidis Noco2) and bacteria, at a growth cost
     [PMID:20520716 "A hyperactive ACD6 allele, compared to the reference allele, strongly enhances resistance to a broad range of pathogens from different phyla"].
2. Positive feedback with SA: ACD6 mRNA requires light, SA and intact SA signaling and is
   induced systemically and by BTH [PMID:14507999].
3. Localization: integral multipass membrane protein, PM and ER pools; soluble pool bound to
   cytosolic HSP70, ubiquitinated and proteasome-degraded (ERAD substrate). SA increases the PM
   pool. Forms complexes with FLS2 (and BAK1); FLS2/BAK1 need ACD6 for maximal SA-induced PM
   accumulation [PMID:24923602].
4. Ankyrin-domain suppressor mutations disrupt complex formation and PM delivery
   [PMID:24923602 "This suggests that the ankyrin domain may act as a platform for assembling protein complexes"].

### Not established

- No biochemical molecular function (no enzymatic, channel, transporter or defined binding
  activity). The PGG/TM region is reminiscent of channel-like topology but no transport activity
  has been shown. Molecular_function ND is appropriate.
- "protein ubiquitination" IDA: ACD6 is the ubiquitinated substrate (ERAD), not an agent of
  ubiquitination; fails the participation test.
- "response to freezing": phenotype of the gain-of-function mutant only, explained by SA
  overaccumulation (suppressed by nahG) [PMID:19959255]; indirect.
- "response to virus" IEP: ACD6 is up-regulated in an LSB1/GDU3 activation-tagged line that
  resists BSCTV; the abstract does not show ACD6 induction by the virus itself. Full text not
  available; left UNDECIDED.
- Requirement of ACD6 for FLS2/BAK1 PM accumulation is necessity evidence; no NEW process term
  (e.g. protein localization to plasma membrane) was added.

### Actions summary

- ACCEPT: PM (x3), ER membrane (x2), defense response to bacterium, positive regulation of
  defense response to bacterium (x2), positive regulation of defense response to oomycetes,
  regulation of defense response to fungus (no positive child exists in GO), ND MF.
- MODIFY: regulation of SA mediated signaling pathway (x3) -> GO:0080151 positive regulation;
  membrane (x3) -> plasma membrane / ER membrane.
- KEEP_AS_NON_CORE: responses to light, bacterium, SA (IEP, IMP), cellular response to SA.
- MARK_AS_OVER_ANNOTATED: cytoplasm (ISM), response to freezing.
- REMOVE: protein ubiquitination.
- UNDECIDED: response to virus.
