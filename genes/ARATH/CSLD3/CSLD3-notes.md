# CSLD3 (KOJAK, At3g03050; UniProt Q9M9M4) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: CSLD3 is reviewed here in its own right because it is the closest experimentally
characterised relative of the peanut CSLD protein ARAHY/A0A444Z7V7. No ProtNLM2 output was
opened or used. This section records what is experimentally established for Arabidopsis
CSLD3 itself, and what is only inferred.

### Deep research

`just deep-research-falcon ARATH CSLD3 --fallback perplexity-lite` failed: Falcon (Edison)
returned 403 "Failed to authenticate", and the perplexity-lite fallback returned 401
insufficient_quota. No deep-research file exists. The review was built from primary papers
cached in `publications/` (found by a PubMed search for CSLD3/KOJAK/AtCSLD3) and the UniProt
record.

### Evolutionary placement

- PANTHER PTHR13301 ("X-BOX TRANSCRIPTION FACTOR-RELATED", the PANTHER name for the
  CESA/CSL superfamily); subfamily PTHR13301:SF58 is named CELLULOSE SYNTHASE-LIKE PROTEIN D3.
- CSLD3 receives two IBAs from PAINT node PTN001410221: plasma membrane (GO:0005886) and
  plant-type primary cell wall biogenesis (GO:0009833). All seeds of that node are CESAs
  (AT5G17420 CESA7, AT5G64740 CESA6, AT4G32410 CESA1, AT5G05170 CESA3), so the node is
  ancestral to CESA and CSLD lineages. PAINT placed cellulose synthase activity
  (GO:0016759) and cellulose biosynthetic process (GO:0030244) on a different node
  (PTN000999295), which CSLD3 does not descend from (CSLD3 has no IBA to either term). So
  PAINT did not propagate catalytic activity to CSLDs. For CSLD3 that gap is filled by its
  own biochemistry (below), not by transfer.
- Peanut A0A444Z7V7 sits in the AtCSLD2 + AtCSLD3 clade (identity 0.858 to CSLD3, 0.852 to
  CSLD2; NJ tree, `genes/ARAHY/A0A444Z7V7/A0A444Z7V7-bioinformatics/RESULTS.md`). That tree
  cannot separate CSLD2 from CSLD3 orthology.

### Experimentally established for Arabidopsis CSLD3

1. **Molecular function: UDP-glucose-dependent beta-1,4-glucan synthase.** Purified His-tagged
   CSLD3 from yeast, reconstituted in proteoliposomes, used UDP-Glc, not GDP-Man, and made a
   product cleaved only by a beta-1,4-specific glucanase [PMID:32169960 "these results
   strongly support the conclusion that CSLD3 utilizes UDP-Glc as a substrate and synthesizes
   β-1,4-glucan and not β-1,4-mannan"]. The CSLD3 catalytic domain in a CESA6 chimera rescued
   the cesa6 prc1-1 mutant; the TED-motif-dead version did not. The reciprocal chimera (CSLD3
   with the CESA6 catalytic domain) rescued csld3 root hairs [PMID:21765420]. This matches
   GO:0016760 cellulose synthase (UDP-forming) activity.
2. **Complex:** detergent-solubilised CSLD3 runs as a large complex (~700 kD, like CESA6) and
   forms 10-12 nm particles with threefold symmetry [PMID:32169960].
3. **Location:** a functional eYFP-CSLD3 sits in a polarized apical plasma-membrane domain of
   growing root hairs, where CESAs are absent [PMID:21765420]. CSLD3 is in a plasma-membrane
   phosphoproteome (Ser-755) [PMID:14506206], and LOPIT puts it in Golgi/TGN
   [PMID:16618929, PMID:22923678]. Early work with 35S:GFP-KJK saw ER signal
   [PMID:11156607]; this probably shows biosynthetic transit or an overexpression artefact.
4. **Process:** csld3/kjk mutants start root hairs, but the hairs burst at the tip and do not
   elongate [PMID:11156607; PMID:11402188]. Cellulose and xyloglucan are disorganised in
   mutant root-hair walls [PMID:21279381]. Root hair elongation (GO:0048767) is missing from
   GOA for CSLD3, but the paralog CSLD2 carries it (IMP, PMID:18768911). CSLD3 does part of
   the work of this process: it synthesises wall glucan at the growing tip. So a NEW
   annotation passes the participation test. The comparator check also passes: CSLD2 carries
   the term.
5. **Redundancy/pleiotropy (not annotated as process participation):** csld3 csld5 and
   csld2 csld5 double mutants are dwarfed [PMID:21471331]. csld2 csld3 double mutants show
   synergid degeneration and reduced female transmission [PMID:22661983]. Overexpression
   promotes root/hypocotyl cell elongation, and the ethylene effects on root hairs depend on
   CSLD3 [PMID:29253184]. These are phenotypes downstream of wall synthesis and are left out.

### Contested: mannan synthase activity

Yin et al. 2011 [PMID:21471331] found GDP-Man mannosyltransferase activity in tobacco
microsomes only when CSLD2 and CSLD3 were co-expressed, "but not when they were expressed
separately". The IDA (PMID:21904114, a short follow-up of that work) therefore rests on
crude microsomes with endogenous mannan synthase, and CSLD3 alone was negative. The purified
reconstitution [PMID:32169960] found no GDP-Man use. The PTHR13301 family review reached the
same conclusion. Action: REMOVE both mannan rows (IDA and ARBA IEA, kept consistent).

### Inferred only

- Golgi membrane residence (UniProt SubCell ECO:0000305, LOPIT): a trafficking compartment
  shared with CESAs; not where activity was shown.
- Cold response: only increased expression at low temperature, plus partial phenotypic
  rescue at 5 °C [PMID:18768911; PMID:21279381]. This does not show that CSLD3 takes part
  in a cold response.
