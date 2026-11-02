# ureG (Q09066, H. pylori 26695) - curation notes

Deep research: attempted once on this gene - `just deep-research HELPY ureG --provider
perplexity` (2026-10-23) - and it failed: "Provider 'perplexity' not available. Available:
falcon, openscientist". Per CLAUDE.md no hand-written `-deep-research-*.md` file was created.
The literature below was assembled from the publications cache (PMIDs 24115911, 24627523,
11196647 already present; 25752610, 29203664, 18767150, 14521881 fetched with
`just fetch-pmid` for this review) plus the UniProt record.

## Mechanistic picture

UreG is a SIMIBI-class (G3E family) P-loop GTPase that converts a nucleotide cycle into
nickel delivery:

1. UreF-UreH recruits UreG into the (UreG-UreF-UreH)2 preactivation complex, juxtaposing the
   two invariant Cys66-Pro67-His68 motifs to build one metal site at the dimer interface
   [PMID:24115911].
2. GTP binding rotates Cys66 and His68 toward each other into square-planar nickel
   coordination; the same conformational change is required for dimerization, GTPase activity
   and activation [PMID:29203664 "Mutagenesis studies on HpUreG support the conformational
   changes induced by GTP binding as essential to dimerization of UreG, GTPase activity, in
   vitro urease activation"].
3. Nickel reaches UreG from UreE through the 2E-2G complex, which also enhances GTP binding
   [PMID:25752610]; Kd(Ni) is ~0.36 uM with GTP/Mg present [PMID:25752610].
4. Nickel + GTP release the charged UreG dimer from UreF-UreH (1.2 Ni per dimer; lost in C66A
   and H68A) [PMID:24115911]; bicarbonate-stimulated hydrolysis of ~2 GTP per dimer then
   returns UreG to a monomer and releases nickel to urease [PMID:24115911].
5. In vivo, the chromosomal P-loop mutant K14A has no urease activity, not rescued by nickel
   [PMID:14521881].

Apparent discrepancies worth keeping in mind: the 2003 paper reports negligible GTP hydrolysis
even for purified parental UreG [PMID:14521881], and apo-HpUreG dimerizes with zinc rather
than nickel [PMID:18767150]. Both were measured without the GTP/dimer/HCO3- context later
shown to be required, so they are not evidence against the GTPase or against nickel
specificity.

## Decisions

- `GO:0003924` (IEA, InterPro:IPR004400): ACCEPT, core - direct phosphate-release measurement
  plus the in vivo P-loop mutant.
- `GO:0016151`: ACCEPT, core (1.2 Ni/dimer; Kd ~0.36 uM).
- `GO:0018237` (IBA, node PTN000785693, Arabidopsis UreG donor): ACCEPT, core.
- UreE-partner `GO:0005515` rows: MODIFY to `GO:0170061 nickel chaperone activity`;
  UreF-partner row: MODIFY to `GO:0018237`.
- Both `GO:0042802 identical protein binding` rows: MODIFY to `GO:0042803 protein
  homodimerization activity` - the self-association is a specific, functionally decisive
  homodimerization that assembles the metal site.
- `GO:0019627`: MODIFY to `GO:0043419` (propagation_review: node transfer sound, granularity
  only). `GO:0043419` IEA row: ACCEPT.
- `GO:0150006 urease activator complex` added as NEW (IDA, PMID:24115911).
