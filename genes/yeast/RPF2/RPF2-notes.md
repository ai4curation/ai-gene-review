# RPF2 (P36160, YKR081C) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: RPF2 is the seed donor (SGD:S000001789) of PAINT node PTN000296192, from
which the IBA rows of NEUCR/NCU08595 propagate. Both sit in PANTHER PTHR12728:SF0
(RIBOSOME PRODUCTION FACTOR 2 HOMOLOG). No ProtNLM2 material was opened or used.

### Deep research

`just deep-research-falcon yeast RPF2 --fallback perplexity-lite` failed: falcon
"Failed to authenticate"; perplexity-lite returned HTTP 401 (insufficient quota). No
deep-research file exists. The review is built from cached primary literature
(publications/) plus PMC full text of Zhang 2007 (PMC2000323), checked by WebFetch.

Additional papers cached for this review: PMID:12048200, 12702244, 17938242, 24662372,
26117542, 26159998, 30291245, 32719344, 37291423. Two incorrectly guessed PMIDs
(25855813, 24717426) were also cached during lookup; they are unrelated papers and are
not cited.

### Experimentally established in S. cerevisiae

- Essential, mainly nucleolar; Rrs1 two-hybrid partner; depletion accumulates 27SB
  pre-rRNA and reduces 60S subunits [PMID:12048200 "the Rpf2p depletion leads to an
  accumulation of 27 SB pre-rRNA"].
- Rpf2-Rrs1 recruit 5S rRNA, rpL5 and rpL11 into 90S/pre-60S particles
  [PMID:17938242 "Rpf2 and Rrs1 are required for recruiting rpL5, rpL11, and 5S rRNA
  into preribosomes"].
- Rpf2 subcomplex needed to load Spb4 and then Nog2 [PMID:22735702].
- Direct 5S rRNA binding; yeast Rpf2 R236 most important single residue; triple
  basic-patch mutant abolishes binding [PMID:25855814]. Yeast Rpf2-Rrs1 structure with
  5S RNA shows an E-loop binding module, plus contacts to Rpl5, Rsa4 and 25S RNA
  [PMID:26159998].
- C-terminal tail (255-344) needed for H68-70 folding, 5S RNP rotation and 60S
  assembly [PMID:32719344]; suppressors of cgr1 map to Rpf2-Rrs1 [PMID:30291245].
- Part of the hexameric 5S RNP precursor with Syo1 [PMID:37291423].

### Evolutionary scope (for transfer)

PAINT placed only rRNA binding (GO:0019843), nucleolus (GO:0005730) and LSU-rRNA
maturation (GO:0000463) at PTN000296192. It did not propagate 5S rRNA binding
(GO:0008097), assembly of LSU precursor of preribosome (GO:1902626) or ribosomal large
subunit assembly (GO:0000027), although this gene carries them experimentally. Treat
that as a deliberate decision when transferring to orthologs such as NCU08595: the
experimentally deeper terms are yeast-established, not node-level.

### Annotation decisions

- 27 bare GO:0005515 rows (SPB1, NOC2, NUG1, NOG1, MAK21, RRS1; HTP/pre-ribosome
  proteomics): REMOVE per protein-binding policy. The Rrs1 heterodimer is functionally
  central and is described in description/core_functions.
- GO:0008312 "7S RNA binding" (IDA, PMID:11864606): the GO term is SRP 7S RNA. The paper
  is about nucleolar pre-rRNA processing factors; 7S here is presumably the 5.8S
  precursor. Abstract only, so MODIFY to rRNA binding with a PROBABLE source_defect
  (requested_change CHECK) for SGD.
- General IEA terms (rRNA processing, maturation of LSU-rRNA, ribosome biogenesis):
  MODIFY to the specific descendants the gene already has.
- 5.8S maturation (IMP): KEEP_AS_NON_CORE, a consequence of the 27SB block.
