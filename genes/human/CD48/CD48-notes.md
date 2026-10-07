# CD48 (human, P09326) review notes

## Deep research status

Automated deep research could not be generated in this session: falcon returned
HTTP 402 (Payment Required), the perplexity-lite fallback provider was not
installed, and the openai provider returned HTTP 401 (invalid API key). The
review was therefore built from the UniProt record and the cached primary
literature listed below, with two additional key papers cached for this review
(PMID:9841922, PMID:19494291).

## Key findings

- **Ligand of 2B4 (CD244).** [PMID:9841922 "Human CD48 bound human 2B4 with a similar affinity (Kd approximately 8 microM)."]
- **Trans and cis engagement tune NK activity.** [PMID:27249817 "Here we show that natural killer (NK) cell-expressed 2B4 not only binds in trans to CD48 on neighbouring cells but also interacts in cis with CD48 on the same cell."]
  2B4 engagement by CD48 drives ITSM phosphorylation, SAP/EAT-2 recruitment and NK cytotoxicity.
- **TCR signalosome adaptor role.** [PMID:19494291 "CD2 functions as the master switch recruiting CD48 and Lck. CD48 in turn shuttles the transmembrane adapter molecule LAT."]
- **CD2 ligand (weak, mainly rodent).** [PMID:12356317 "the low-affinity CD2-CD48 bond generates weak adhesion"]; the abstract states murine proteins were used.
- **GPI anchor, raft residence.** [PMID:1999351 "linkage to the cell membrane through a glycosyl phosphatidylinositol tail and this was verified experimentally"]; [PMID:12007789 "abolished Lck association with the GPI-anchored protein, CD48"]
- **Soluble form in plasma.** [PMID:9418191 "We describe the detection of a soluble form of CD48 in plasma and serum."]
- **IFN-inducible.** [PMID:9041467 "both Hu-IFN-alpha/beta and Hu-IFN-gamma increase the level of CD48 mRNA"]

## Curation decisions

- All five `protein binding` IPIs were changed (MODIFY): the four with CD244 to signaling receptor
  binding, and the one with CD2 to cell adhesion molecule binding.
- `defense response` (TAS, cloning paper) was marked as over-annotated; the paper does not support it.
- NEW annotation: positive regulation of T cell receptor signaling pathway, from PMID:19494291
  (single abstract-only study). A NEW molecular adaptor activity annotation was dropped after PR
  review: CD48 is GPI-anchored with no cytoplasmic domain, so its effect on LAT is most likely
  raft co-recruitment rather than a binding activity.
- Activation-direction claims are anchored to PMID:16002700 ("In human NK cells, 2B4/CD48
  interaction induces activation signals"), not to the Introduction of PMID:27249817. That paper's
  own CD48 result is that cis CD48 reduces trans engagement of 2B4.
