# Ruegeria BetC and BetT identity and assay scope

Reviewed 2026-11-06. This is a manual source analysis, not a provider report.

## Locus and strain identity

Both primary studies (PMID26058574, PMID40801533) study Ruegeria pomeroyi DSS-3. The normally fetched UniProt records are the same strain, taxon 246200. Q5LUH1 is betC-1/SPO1083, 502aa; Q5LUG7 is SPO1087, 400aa, named BetT in the papers. Q5LRB5/SPO2214 is the distinct betC-2 paralog and is not the 2015 betC mutant target.

The 2015 official supplement TableS1 explicitly names the Spo1083 primers as cloning or confirming the betC mutant and the Spo1087 primers as cloning or confirming the betT mutant. All 12 cloning/confirmation primers map uniquely to the corresponding CP000031.2 genomic region after removal of the documented CAAT-plus-restriction-site cloning tails. Published primer spaces are preserved in the exact table extraction and normalized only for sequence matching. The official AAV94383.1 and AAV94387.1 protein records translate those loci and exactly match the complete frozen UniProt sequences. No protein identity is inferred from length alone. The second BetC-like paralog is excluded by locus-specific primer mapping.

The original supplement DOCX, unchanged official GenPept records, exact table extraction, derived genomic window and provenance are adjacent. `verify_identity.py` checks complete protein identity and all 12 primer matches. It additionally verifies uniqueness across the complete official chromosome when the original cached FASTA is available; the chromosome sequence SHA256 is recorded in provenance.json. The committed window is explicitly a derived interval, not a fabricated official record.

The 2025 main text independently states that betC is SPO1083 and that betT–betA is SPO1087–1088. Thus its regulatory results refer to these loci. BetT is an alias of the locus-based SPO1087 record; betC-1 retains the UniProt standard symbol.

## What the experiments demonstrate

PMID26058574 identifies BetC using homology to characterized choline sulfatases, then shows that disrupting the mapped locus abolishes growth on COS while preserving growth on choline and glycine betaine. This supports the specific hydrolytic step in COS utilization in combination with the independent choline-sulfatase signatures (IPR017785, TIGR03417, PF12411) in Q5LUH1. It is not a purified Ruegeria BetC turnover assay. No target-specific rate constant, metal preference, formylglycine processing measurement, phosphorylcholine hydrolysis or promiscuous phosphatase chemistry is established by these studies.

For BetT, the measured choline phenotype is an 84% reduction in culture-medium choline depletion during growth of the disrupted mutant, together with reduced growth rate. This is native genetic/physiological evidence for choline transport, not an initial-rate tracer assay or reconstituted membrane flux assay. The protein has 11 predicted transmembrane helices in the frozen record. The paper names it a BCCT-type transporter, but the frozen Q5LUG7 record has no PANTHER/InterPro/Pfam cross-reference, so no such family ID is invented.

COS-grown betT-mutant cells retain growth but their growth rate falls 38% (0.027 versus 0.043 per hour). That is a real contribution under the tested conditions; retention of growth does not prove absence of COS transport. Conversely, a partial growth phenotype cannot establish transported cargo. The quantification method explicitly excludes COS from the measured amines. The 2025 Figure1 label calls BetT a choline/COS transporter, but the newer experiments address BetI regulation and do not supply a direct BetT-dependent COS flux assay. COS induction of betTA expression is regulation, not proof of substrate recognition. Neither COS transport nor a NOT-COS-transport annotation is warranted. Unchanged glycine-betaine growth similarly does not prove absolute exclusion of that cargo.

The two genes in betTA are co-transcribed. The 2015 insertion mutant and growth-coupled depletion assay do not independently resolve possible downstream effects or ion coupling; direct uptake with nonpolar deletion and complementation would strengthen the assignment. This limitation is recorded without rejecting the published choline-transporter interpretation.

## Annotation boundaries

Choline-sulfatase activity is already seeded for betC-1; the broader sulfuric-ester hydrolase term is refined to it. The available primary data do not resolve the precise compartment of Q5LUH1; its inherited cytoplasm inference is plausible but left UNDECIDED, with no contradictory localization claimed and no core location forced. The specific COS catabolic process is proposed as a new ontology term rather than substituting choline catabolism, which consumes a different molecule.

For SPO1087, propose GO:0015220 choline transmembrane transporter activity from native genetic evidence and GO:0005886 plasma membrane from membrane architecture and the uptake role. No ionic coupling, COS cargo, glycine-betaine exclusion, osmoprotection process or downstream catabolic BP is inferred. GO:0015220 already has a part_of path to choline transport; a redundant NEW GO:0015871 row is not added. The local GO-CAM index has no entry for either accession.

QuickGO checks found that same-role E.coli BetT P0ABC9 carries choline transporter activity and plasma membrane. The two characterized BetC comparators, S.meliloti O69787 and P.putida Q88RQ2, both carry choline-sulfatase activity; O69787 also carries choline biosynthesis, whereas Q88RQ2 does not. These are convention checks, never evidence for the target's chemistry. No exact GO process term for COS breakdown was found. Its natural parent is sulfur compound catabolic process (GO:0044273). BetC performs the hydrolytic chemistry itself, so the proposed process is not justified by necessity evidence alone.
