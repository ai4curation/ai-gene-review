# Nitrogen-regulatory PTS: preliminary literature triage

Checked 2026-11-07 against main `b4f249a30490049f1009fea5871a037219596e0f`. This is manual research, not provider-generated deep research or a completed curation. `baseline.json` records the exact module and existing review hashes. No curated files have changed.

## Review source and claims to investigate

[Banerjee, Cabeen and Chandler 2026, PMID:41870250](https://pmc.ncbi.nlm.nih.gov/articles/PMC13104625/) is a directly relevant comparative minireview (DOI 10.1128/jb.00541-25; full text accessible; page declares CC BY 4.0). It describes PtsP-to-PtsO-to-PtsN signaling, variable downstream outputs, and independent functions of the upstream proteins. It reports glutamine sensing in several lineages and warns that the input mechanism is not established universally. Its distribution section includes homologs outside Proteobacteria, whereas its historical introduction gives a narrower PtsN statement. Do not treat these as a resolved universal taxonomic boundary. Read the underlying comparative studies and distinguish individual homologs from an intact functional relay.

Useful primary-paper leads in this review: Goodwin and Gage 2014, DOI 10.1128/JB.01489-14 (Sinorhizobium); Ronneau et al. 2016, DOI 10.1038/ncomms11423 (Caulobacter); and the Rhizobium study below. These provide candidate evidence beyond the two gammaproteobacterial lineages already represented. The review also identifies PtsO/PtsP-independent effects and cross-talk as reasons not to equate a knockout phenotype with the terminal PtsN mechanism.

[Pflüger-Grau and Görke 2010, PMID:20202847](https://pubmed.ncbi.nlm.nih.gov/20202847/), DOI 10.1016/j.tim.2010.02.003, is a second relevant review candidate. Full text has not been retrieved here; no findings or quotations are asserted from it.

## Primary cross-lineage evidence

[Sánchez-Cañizares et al. 2020, PMID:32341157](https://pmc.ncbi.nlm.nih.gov/articles/PMC7229655/), DOI 10.1073/pnas.1917471117, studies Rhizobium leguminosarum bv. viciae 3841. Its abstract and introduction describe PEP transfer through PtsP and NPr to PtsN and ManX, with a GAF-dependent response to glutamine. The two terminal outputs separate nitrogen-related regulation from carbon-metabolic effects. This is a candidate alphaproteobacterial panel, not permission to assert that every downstream output is an obligatory part of the conserved relay. Exact locus/accession identities, experimental rows and source organisms still require verification. The page specifies the PNAS license; do not presume unrestricted full-text redistribution.

## Local curation issues established by inspection

- The current three-part module uses two named PANTHER subfamilies plus an unnamed NPr family descriptor. The NPr omission is explicitly justified by HPr/NPr mixing in the available subfamily; do not guess a replacement identifier.
- All six current exemplars come from E. coli and P. putida. Main contains three PSEPK review files, all DRAFT (18 annotation rows total, zero PENDING). The three named ECOLI review paths are absent. Accession aliases must be searched before seeding new reviews.
- The terminal annoton's sole MF is kinase regulation although the description defines a general phosphostate effector. Assess whether that choice improperly requires a particular downstream target for organisms with other outputs. Preserve supported KdpD regulation as evidence and optional context rather than silently broadening its proof.
- The existing PSEPK PtsN review has one core-function entry with neither an asserted nor proposed MF; inspect the current schema and complete the biological synthesis rather than changing status alone.
- The broad bacterial context is a range, not a universal-presence assertion. Resolve the supported architectural scope from primary studies, family placement and real organism panels before narrowing or broadening it.

## Required next work

Create an isolated module branch when storage permits, load current module guidance, retrieve references through normal cache tooling, and attempt configured Falcon research honestly. Consult the annotation reviewer on the existing panel. Resolve additional alpha/beta lineage exemplars from primary papers and UniProt before fetching missing genes. Review the three family descriptors against actual classifications and PAINT evidence. Curate all member annotations with source payload/order preserved, mine evidence for every step, test real positive and negative organism/architecture cases, validate and render, add generated history records, then run full validation before a dedicated PR. No completion or capacity claim has been made by this triage.


## Additional primary evidence and architecture boundary (2026-11-07)

[Karstens et al. 2014, PMID:24515609](https://pubmed.ncbi.nlm.nih.gov/24515609/) reports that Ralstonia eutropha H16 PtsN copurifies with SpoT1; two-hybrid and far-Western results support interaction by the unphosphorylated regulator. Its abstract reports no corresponding native KdpD interaction, although the Ralstonia protein complements E. coli KdpD regulation. This distinguishes a conserved regulatory protein from a conserved target pair. The paper's evolutionary interpretation remains a hypothesis, not evidence for a PAINT gain or loss. Full text and assay controls remain to be inspected.

[Kaddor and Steinbuechel 2011, PMID:21478317](https://pmc.ncbi.nlm.nih.gov/articles/PMC3127587/) provides a useful architecture comparator: table 1 assigns H16_A0326 to a 586-aa PtsI enzyme I, H16_A0325 to an 89-aa HPr, and H16_A0384 to PtsN. These upstream proteins must not silently become exemplars of the module's GAF-containing PtsP/NPr architecture. Establish domains and native phosphotransfer evidence before deciding whether this is an alternative relay or an intact-module positive. H16_A2203 is a distinct HPr-related candidate whose low similarity and missing canonical residues require particular care. These are comparative boundaries, not absence claims.

[Ronneau et al. 2016, PMID:27109061](https://www.nature.com/articles/ncomms11423.pdf) reports glutamine-responsive EI(Ntr) signaling and SpoT modulation by phosphorylated HPr and EIIA(Ntr) in Caulobacter. This is a candidate alphaproteobacterial positive for the upstream architecture and an additional non-KdpD output. The full HTML retrieval is currently blocked (publisher redirect; PMC CAPTCHA); the accessible publisher PDF abstract establishes the lead but does not replace detailed assay/strain/accession verification.

An accession search of committed main gene reviews and UniProt records found no P37177, P0A9N0, or P69829 entries under alternate paths (git grep over all genes, not only ECOLI). Thus alias duplication has been checked for the three missing E. coli exemplars; recheck current main when beginning the branch.


## Primary assay and family-selector findings (2026-11-07, 12:46 UTC)

[Goodwin and Gage 2014, PMID:24633875, author-hosted full PDF](https://gage.mcb.uconn.edu/downloads/2014_goodwin_jbact.pdf) identifies the assayed constructs as ptsP/smc02437 and hpr/smc02754. Purified EI(Ntr) transfers phosphate to HPr; glutamine binds the isolated GAF domain and inhibits the enzyme, whereas alpha-ketoglutarate did not show the corresponding effect. The recombinant expression strains are E. coli hosts, not the protein's native organism. This supplies direct entry/relay evidence; it does not by itself prove every terminal PtsN output. The manuscript methods inspected here do not explicitly name the donor strain, so the current 1021 locus/accession correspondence still needs sequence/construct verification.

[Ronneau et al. 2016 full publisher PDF in the authors' institutional repository](https://pure.unamur.be/ws/files/13636727/ncomms11423.pdf) is accessible despite the publisher/PMC HTML failures. Methods identify NA1000-derived Caulobacter strains. Figure 6 and accompanying text distinguish phosphorylated PtsN-SpoT interaction in bacterial two-hybrid assays from HPr's indirect action; HPr-SpoT interaction was not detected in that assay. Do not generalize that assay negative to universal absence or infer direct HPr binding from an effect on SpoT.

Live UniProt lookups resolve candidate identifiers (see candidate-identities-20261107.json). NA1000 PtsP is A0A0H3C823/CCNA_00892 (754 aa); candidate HPr and PtsN are A0A0H3C344/CCNA_00241 (92 aa) and A0A0H3CDT8/CCNA_03710 (180 aa). The last two are protein-name matches, not yet construct-verified gene aliases. SMc02437 and SMc02754 resolve to Q92MK4 and Q92TC0 in strain 1021. UniProt's unreviewed protein names/EC fields are lookup metadata, not functional or localization evidence.

**A concrete selector mismatch now needs resolution:** both alpha-lineage PtsP candidates carry PTHR46244:SF6, whereas the current module requires SF1. Official local PANTHER labels confirm both subfamilies belong to PTHR46244. Do not merely append the candidates under SF1 or mechanically broaden to the parent: examine the actual member/tree scope and require the GAF-containing nitrogen-relay role. Candidate HPr proteins fall in the already-ambiguous PTHR33705:SF2, reinforcing the need for role/partner evidence rather than the official NPR name alone. The PtsN candidate carries the module's PTHR47738:SF1.

The cached PTHR46244 entry table adds a concrete negative control: E. coli carbohydrate-PTS PtsI P08839 is also SF6. A union of SF1/SF6 still does not identify nitrogen-relay entry proteins. The exact cached rows and source hash are in ptsp-selector-counterexample.json.


## Existing-member consultation and ontology check

The read-only annotation-reviewer consultation is saved in psepk-readonly-consultation-20261107.json: 18 ordered rows comprise 11 machine IEA and **seven active historical NEW proposals** (PtsP 1, PtsH 2, PtsN 4). All must retain their original payload and lifecycle during curation. The cached PMID18296519 is flagged as full text but contains only Abstract/Discussion; complete methods/results/figures still need retrieval. Target KdpD evidence, broad-term action/reason consistency and localization support require review before declaring these genes COMPLETE.

[QuickGO live term definitions](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0016301,GO%3A0016772,GO%3A0019887) were checked on 2026-11-07. All three terms are active. Kinase activity makes ATP the usual donor, not an exclusive donor; therefore a non-ATP phosphorelay alone does not disprove the term. The distinction between catalytic phosphotransfer and an intermediate phosphocarrier still needs a defensible explanation and comparator evidence. Protein kinase regulator activity requires modulation of kinase activity, so KdpD binding or promoter output alone should not silently become proof of that MF.
