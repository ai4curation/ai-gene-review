# Kdp cross-species audit consultation

Read-only investigation, 2026-11-07. Authoritative source is freshly fetched origin/main **e9d50a8a42ab5e6b5560d09ff8c44e64f4c77360**; checked-out root HEAD was older, so repository records were inspected using git-show snapshots. No curated repository files, publication caches, gene inputs or released Isc inputs were edited. This is scope consultation, not completion of the new biological audit or validation.

## Existing coverage and provenance

Merged PR5850 (merge 8af33c29cf02c24e00d0a1428d586443cf036398, merged 2026-11-04) made the module COMPLETE and reported thirteen completed member reviews and five completed family reviews. Its final review approved the scoped changes while explicitly leaving some pre-existing DESVH annotation problems. Those are historical claims, not evidence that this broader audit has been performed. PR metadata/reviews are saved in pr5850.json.

Current module members: ECOLI kdpA/B/C/D/E/F (160 rows), PSEPK kdpA/B/C/D/E/F (48), DESVH/Q725T7 (13): **13 reviews / 221 rows**. Existing STAA8/kdpD Q2FWH7 adds ten rows but is not a module representative: audit **14 existing reviews / 231 rows** if included. All currently say COMPLETE.

Existing family reviews: PTHR30607 (KdpA SF2), PTHR43743 (KdpB SF1), PTHR30042 (KdpC SF2), PTHR45569 (KdpD SF1), PTHR48111 (broad OmpR/PhoB, KdpE SF50). KdpF is grounded by TIGR02115/IPR011726, not PANTHER. Recheck actual member placements and PAINT scopes; do not infer function merely from these names.

## Material scope changes needed

1. **Separate pump capacity from regulatory implementation while retaining the complete homeostasis scope.** The present required KdpD-His-to-KdpE relay, KdpE transcription branch and FABC pump describe the canonical E. coli route. Retain that as an explicit implementation, plus a transport endpoint and independently evidence-qualified regulatory profiles. Do not silently reduce the whole module to transport alone. Same-organism compatible complex witnesses and same-polypeptide KdpE receiver/DNA output are required; unrelated family hits cannot complete the system.
2. **KdpF is not a universal capacity requirement.** Current active_units include F without an optional qualification. Existing E. coli evidence PMID10608856 distinguishes in-vivo dispensability from stabilization of detergent-solubilized complex and lipid rescue. Preserve F as a supported native component/context; permit a specifically supported functional KdpABC route. Do not extend this dispensability to KdpC without evidence.
3. **KdpD is not solely a positive histidine-kinase input.** PMID38622146 establishes a second, inhibitory serine-kinase activity targeting KdpB; the current ECOLI/kdpD review already includes it. The module omits this arm. The short Deinococcus KdpD comparison also prevents an unqualified 'truncated KdpD lacks kinase' statement: loss of the histidine transmitter is not loss of the N-terminal serine kinase. No universal transfer to PSEPK or every family member is justified.
4. **Caulobacter is a direct counterexample to universal obligatory cognate activation.** PMID39133005 tests NA1000 kdpABCDE, CCNA_01663–01667. KdpE-dependent promoter activity persists without KdpD; mutant/reporting experiments support a major phosphatase role and another unidentified phosphorylation source. KdpD kinase participation remains plausible and growth-phase dependent. Do not invent the alternative HK or pretend purified phosphotransfer was measured. The KdpABC system supports low-K growth but is not the organism's sole route.
5. **Transport mechanism and contribution need current evidence.** KdpA selectivity and KdpB catalytic ATPase form an assembled transporter; neither an isolated B homolog nor independent ATP hydrolysis establishes coupled transport. KdpC's old ATP-affinity/chaperone model needs reconciliation with its periplasmic topology and newer structures. Do not reject an experimentally observed binding activity solely because a proposed physiological model is outdated. KdpF has no demonstrated independent catalytic MF. Avoid generic potassium:proton antiporter-complex mappings; reaction proton bookkeeping is not a claim of transmembrane proton exchange.

## Recommended panel

| Priority | Panel | Verified identity/source | Reason and limit |
|---|---|---|---|
| Required | Existing 14 records above | Current main snapshots; PR5850 | Re-audit all rows, not only mechanism-linked ones. PSEPK is mainly inferred; DESVH single B remains a partial-panel comparator. |
| Required new | **Caulobacter vibrioides NA1000** KdpA/B/C/D/E | B8GVF8 / A0A0H3C7Y6 / B8GVG0 / A0A0H3C8H5 / A0A0H3C8M3; CCNA_01663–01667; taxon565050; PMID39133005 | Matched native five-member panel with regulatory diversity. UniProt API capture candidate-uniprot.json verifies accession/locus/taxon. No missing KdpF should be manufactured. |
| Required new comparator | **Deinococcus geothermalis DSM11300** short KdpD | Q1J2K3, Dgeo_2852,365aa,taxon319795; PMID38622146 | Official Q1J2K3.json verified. Paper PDF text/search reports malformed accession QJ1J2K3: reconcile construct/SI to actual Q1J2K3 before asserting exact assayed identity. Start with a regulatory comparator, not a complete native transport witness. |
| Strong next panel | **Mycolicibacterium smegmatis mc²155** KdpABCDE and carefully resolved KdpF | PMID28484428, DOI10.3389/fmicb.2017.00570; full primary XML saved | Native deletions/reporters and KdpE DNA binding. KdpF ORF is experimentally remapped within old MSMEG_5391; do not seed an obsolete full-length hypothetical protein as KdpF. Exact current accessions and construct sequences still need official lookup. No purified whole-pump kinetics established by this paper. |
| Strong regulatory comparison | **S. aureus** existing STAA8 KdpD, then matched KdpE/pump if identity resolved | PMID26195599,33989637,23671116; existing Q2FWH7 | Specific c-di-AMP binding/regulation. PMID26195599 cellular assays use LAC* and a second KdpD from MRSA252; do not relabel them as NCTC8325. Prefer an assay-matched panel or explicit orthology transfer. PMID21422185 broadens virulence/regulatory context, not a universal denial of Kdp transport. |

Official candidate query: https://rest.uniprot.org/uniprotkb/search?query=(gene:kdp*)%20AND%20(organism_id:565050%20OR%20organism_id:319795%20OR%20organism_id:196186)&format=json&size=100 . The third taxon yielded no candidate and is not an established Mycobacterium panel; no absence inference is warranted. Dgeo ABC accessions Q1J2K5/Q1J2K6/Q1J2K4 are verified sequence candidates only, not assayed native pump claims.

## Gene and family audit priorities

- DESVH/Q725T7: four MARK_AS_OVER_ANNOTATED rationales explicitly mean true but general (nucleotide binding, ion transport, membrane, hydrolase); refine according to current policy. ATP/Mg support quotes use keyword lines despite available curated feature evidence. Description gives ~2µM affinity and mechanistic detail without distinguishing target measurement from E. coli inference. These were already noted, in part, by PR5850's approving reviewer.
- KdpA/B/C/F: revisit whole-complex versus subunit MF treatment consistently; lack of autonomous activity is not by itself grounds to erase a genuine complex contribution. Keep original row payloads and inherited NEW assertions frozen before adjudication.
- KdpD: explicitly assess histidine kinase, phosphatase and serine kinase separately; domain architecture and direct assays matter. c-di-AMP sensitivity is not universal. PTHR45569 broad kinase-language needs this boundary.
- KdpE: broad PTHR48111 is not a Kdp-specific selector. Even SF50 membership does not prove the same regulon, physiological input, or positive edge in every species. Assess non-Kdp virulence claims individually, not as core universal homeostasis requirements.
- KdpF: small-gene annotation can miss or mis-start the ORF; absence of a family hit cannot substitute for locus/sequence investigation. Conversely, adding an F peptide cannot be used to force complete pump capacity.

## Verified literature acquisition list

Reviews:
- PMID33798529; DOI10.1016/j.jmb.2021.166968; PMC9041122, *Molecular Mechanisms for Bacterial Potassium Homeostasis*. Broad comparative framework; predates the 2024 tandem kinase result.
- PMID31259644; DOI10.1080/09687688.2019.1638977; PMC6681667, *The KdpFABC complex—K+ transport against all odds*. Explicit older competing transport models; reconcile with later structures rather than treating one historical model as settled.

Primary priorities:
- PMID10608856, KdpF stabilization/in-vivo dispensability.
- PMID38622146; DOI10.1038/s41467-024-47526-8, tandem serine/histidine kinase and Deinococcus comparison.
- PMID39133005; DOI10.1128/jb.00107-24; PMC11411941, native NA1000 regulation. Indexed full text read; EuropePMC XML attempt returned500 and is not claimed as a local capture.
- PMID28484428; DOI10.3389/fmicb.2017.00570; PMC5401905, mc²155 regulation and KdpF remapping. Successful full primary XML acquired only under /tmp.
- PMID26195599; DOI10.1128/JB.00480-15; PMC4686210, Staphylococcus c-di-AMP specificity and cellular expression; PMID33989637 provides structural follow-up.
- PMID41259220; DOI10.7554/eLife.107397; PMC12629597, final published Kdp conduction-pathway paper (use instead of its older preprint PMID40654642).
- PMID41384914; DOI10.1085/jgp.202513794; PMC12833782, tunnel/transport versus ATPase coupling; assay/model limits must be read before quantitative claims.
- PMID41929109; DOI10.64898/2026.03.20.713019; PMC13042032, lipid dependence. **PubMed explicitly labels this a preprint**; supplementary/updating evidence, not established peer-reviewed consensus.

Source URLs: https://pubmed.ncbi.nlm.nih.gov/<PMID>/ and https://pmc.ncbi.nlm.nih.gov/articles/<PMCID>/ for each listed identifier; current Nature primary https://www.nature.com/articles/s41467-024-47526-8 ; Caulobacter https://journals.asm.org/doi/10.1128/jb.00107-24 . No new publication cache was written.

## Capacity controls for the eventual audit

Positive controls should distinguish canonical E. coli regulated pump, E. coli F-independent transport in the demonstrated setting, qualified PSEPK inferred complete panel, and Caulobacter native regulatory profile. Negative controls: lone DESVH KdpB, missing KdpA/B/C, arbitrary cross-taxon subunit mixtures, generic P-type ATPase replacing KdpB, generic OmpR replacing KdpE, short Dgeo serine kinase satisfying histidine-kinase requirement, and serine-phosphorylated inhibited pump being called constitutively active. Dgeo kinase-only evidence must not complete a native pump. Do not claim every cross-species assembly is impossible: the negative result concerns absent compatibility evidence. No capacity/schema tests were run in this consultation.
