# AMZ1 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- AMZ1 (archaemetzincin-1, Q400G9) belongs to the archaemetzincin family (peptidase M54) within the metzincin superfamily.
- **The only activity paper is withdrawn.** PMID:15972818 (Díaz-Perales et al. 2005), which reported that recombinant AMZ1/AMZ2 hydrolyze peptides, was withdrawn by JBC in 2019 (PMID:30808005: "Withdrawal: Identification and characterization of human archaemetzincin-1 and -2, two novel members of a family of metalloproteases widely distributed in Archaea."). UniProt's CAUTION line flags this.
  - Affinage's gates were clear, but its whole activity narrative rests on this withdrawn paper. My first draft of this review accepted the three peptidase IEAs on that basis. I found the problem while starting AMZ2, before merge, and reworked the review.
- **AMZ1 lacks the third zinc-binding His.** See `AMZ1-bioinformatics/RESULTS.md`:
  - AMZ1 has HELCHLLGLGN (Asn271), where AMZ2 and the archaeal AmzA structures have H.
  - Graef et al. 2012 (PMID:22937112, full text) note: "AMZ1 has the third histidine of the metzincins' consensus sequence replaced by asparagine, serine or threonine, depending on the organism". They add that this raises "some concern on the proteolytic activity of AMZ1".
  - The same paper says even the archaeal enzymes show no activity in standard assays.
- **Decisions:**
  - Peptidase, metallopeptidase and proteolysis IEAs are UNDECIDED. The activity is neither established nor refuted; REMOVE would over-read one residue substitution.
  - The CC ND row is accepted.
  - No core function; WHOLLY_DARK knowledge gap.
