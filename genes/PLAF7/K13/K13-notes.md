# K13 (Kelch13 / PfK13, PF3D7_1343700, UniProt Q8IDQ2) — curation notes

> **Provenance note.** Automated deep research was not available in this environment
> (no working provider credentials), so **no `*-deep-research-*.md` file was generated**.
> What follows is a **manual literature review** carried out by reading the UniProt flat
> file, the GOA rows, the publications cited by GOA, and additional primary papers
> located through PubMed E-utilities (titles and PMIDs verified against PubMed before
> fetching) and cached under `publications/`.

## Identity

- UniProt Q8IDQ2 (TrEMBL), 726 aa, `SubName: Full=Kelch protein K13`, ORF name
 `PF3D7_1343700`, *Plasmodium falciparum* 3D7 (NCBITaxon:36329). No HGNC-style gene
 symbol exists, hence `gene_symbol: Q8IDQ2` in the review and the folder alias `K13`.
- Domain architecture from the UniProt record: a disordered N-terminal region (1–58),
 a coiled coil (241–308), a BTB/POZ domain (`DOMAIN 350..452 /note="BTB"`), and a
 six-bladed Kelch-repeat β-propeller (`SMART; SM00612; Kelch; 6`;
 `Gene3D; 2.120.10.80; Kelch-type beta propeller`). PDB 4ZGC covers residues 338–726
 (BTB + propeller) as chains A/B.
- InterPro assignments include IPR003131 (T1-type BTB), IPR000210 (BTB/POZ),
 IPR015915 (Kelch-type β-propeller). The single InterPro2GO annotation in GOA
 (`GO:0051260 protein homooligomerization`) derives from IPR003131.

## Function: hemoglobin endocytosis at the K13 compartment

The most direct functional evidence is that K13 is required for endocytosis of host
erythrocyte cytosol:

- [PMID:31896710 Birnbaum et al. 2020 Science, "we identified proteins located
 at a Kelch13-defined compartment. Inactivation of eight of these proteins,
 including Kelch13, rendered parasites resistant to ART, revealing a pathway
 critical for resistance. Functional analysis showed that these proteins are
 required for endocytosis of hemoglobin from the host cell. Parasites with
 inactivated Kelch13 or a resistance-conferring Kelch13 mutation displayed
 reduced hemoglobin endocytosis."]. Only the abstract is cached for this paper
 (`full_text_available: false`).
- [PMID:38700363 Behrens et al. 2024 mBio, "K13 and its compartment neighbors (KICs),
 including UBP1, are involved in endocytosis of host cell cytosol."] and, in the
 same paper, "Titration of K13 and KIC7 indicated that the cellular levels of these
 proteins determined resistance through the rate of endocytosis." — i.e. resistance
 tracks quantitatively with how much endocytosis K13 supports, and
 "we found correlations between K13 protein amount, resistance, and fitness cost."
- [PMID:38039338 Schmidt et al. 2023 PLoS Pathogens, "vesicle trafficking and
 endocytosis domains were frequent in proteins involved in resistance or endocytosis
 (or both), comprising one group of K13 compartment proteins"]. The same paper states
 the route the cargo takes: "Hemoglobin trafficking to the parasite food vacuole is
 believed to be initiated at membrane invaginations called cytostomes [30,42,48,49]
 followed by vesicular transport from the parasite plasma membrane (PPM) to the food
 vacuole [42,50]".

So the cargo is host erythrocyte cytosol (chiefly hemoglobin), the destination is the
food/digestive vacuole, and K13 acts at the uptake step, not at proteolysis. This is a
parasite acquiring nutrients from its host cell, and it is also the step that supplies
the heme that activates artemisinins.

## Localization

- [PMID:32310999 Gnädig et al. 2020 PLoS Pathogens, "we localize K13 to the parasite
 endoplasmic reticulum, Rab-positive vesicles, and sites adjacent to cytostomes."]
 and "We also saw evidence of K13 associating with cytostomes that traffic
 host-endocytosed hemoglobin from the parasitophorous vacuolar space to the DV".
- The same study's co-IPs recovered "endoplasmic reticulum-resident molecules,
 mitochondrial proteins, and Rab GTPases, in both K13 mutant and wild-type isogenic
 lines" — consistent with a vesicle-trafficking context.
- Birnbaum's "Kelch13-defined compartment" is a discrete focal structure at the
 parasite periphery; GO has `GO:0031910 cytostome` ("Stable, specialized structure for
 the ingestion of food by the cell into phagosomes") but no term for the K13
 compartment itself, and the imaging places K13 *adjacent to* rather than *in* the
 cytostome. I therefore did not assert a cellular-component annotation and instead
 proposed a term.

## Artemisinin resistance

- [PMID:24352242 Ariey et al. 2014 Nature, "Strong correlations between the presence of a mutant
 allele, in vitro parasite survival rates and in vivo parasite clearance rates
 indicate that K13-propeller mutations are important determinants of artemisinin
 resistance."] This paper is the `original_reference_id` for the GOA
 `GO:0009410 response to xenobiotic stimulus` IDA. Its experimental content is the
 selection of the F32-ART5 line and allele association: "These data indicate that the
 PF3D7_1343700 M476I mutation increased the resistance of F32-Tanzania to DHA in the
 RSA0–3h."
- [PMID:25502314 Straimer et al. 2015 Science, "With isolates from Cambodia, where
 resistance first emerged, survival rates decreased from 13 to 49% to 0.3 to 2.4%
 after the removal of K13 mutations."] — gene editing establishes causality of the
 propeller mutations.
- Mechanistically, resistance is a *loss* of K13 activity: less hemoglobin is taken up,
 so less heme is released to activate the drug [PMID:31896710 "ARTs are activated by
 degradation products of hemoglobin. Hence, reduced activity of Kelch13 and its
 interactors diminishes hemoglobin endocytosis and thereby ART activation, resulting
 in parasite resistance."]. Nothing in this describes an induced parasite *response*
 to the drug; the wild-type protein is not a xenobiotic-response factor, which is why
 I marked the GOA `GO:0009410` row as over-annotated rather than accepting it.

## The PfPI3K interaction (GO:0005515 IPI)

- The IntAct partner is UniProtKB:Q8I3V5 = PF3D7_0515300, annotated by UniProt as
 "phosphatidylinositol 3-kinase" (EC 2.7.1.137), i.e. PfPI3K.
- [PMID:25874676 Mbengue et al. 2015 Nature, "Further analysis revealed that
 immunopurified (IP) PfPI3K was bound to PfKelch13WT and this was reduced by the C580Y
 mutation (Fig. 2e)."] The paper frames K13 as a CRL3-type substrate adaptor by analogy:
 "The mammalian orthologue of PfKelch13 functions is a substrate adapter for an E3
 ubiquitin ligase18." — explicitly an inference from the mammalian KEAP1 paralogy plus
 the observation that "K48-linked and atypical ubiquitination, both signals for
 proteosomal degradation were prominent in PfPI3K and concomitantly reduced by
 PfKelch13C580Y."
- Caveat recorded for the review: the ubiquitin-ligase-adaptor model has not been
 corroborated by the later endocytosis work, and the independent K13 interactome of
 [PMID:32310999] recovered ER proteins and Rab GTPases rather than a cullin-RING
 ligase. I accept the interaction as real but removed the bare `GO:0005515` row, since the
 term carries no functional information and there is no supportable molecular
 function to modify it to; in particular I did not elevate "ubiquitin-like ligase-substrate adaptor activity"
 (GO:1990756) to a core function, and raised the question in `suggested_questions`.

## Oligomerization (GO:0051260 IEA)

- The InterPro2GO call from the T1-type BTB domain is supported by direct structural
 data: PDB 4ZGC is a BTB+propeller dimer, and
 [PMID:35092154 Sharma et al. 2022 FEBS J, "(a) PfKelch13 forms a stable hexamer in P6
 symmetry, (b) interactions of the N-termini drive the hexameric assembly"]. The same
 study notes "To date, only two crystal structures of the BTB/POZ-KRP domains as
 tight dimers are available". Self-assembly is a real property but a structural
 prerequisite rather than the gene's core biological role, so it is kept as non-core.

## Protist-specific checks performed

- No animal- or plant-specific terms are present in the GOA file; the three rows are
 generic (`protein binding`, `response to xenobiotic stimulus`,
 `protein homooligomerization`).
- No apicoplast, rhoptry, microneme or parasitophorous-vacuole terms are asserted, and
 none is supported: K13's documented sites are the parasite periphery/cytostome
 vicinity, ER and vesicles.
- Host-vs-symbiont: the cargo K13 imports comes from the host erythrocyte cytosol, so
 `GO:0044002 acquisition of nutrients from host` ("The process that begins with the
 production and formation of structures and molecules in an organism that are required
 for the acquisition and utilization of nutrients from its host organism, and the ends
 with the acquirement of the nutrients") is the correct host-aware framing; the
 parasite is the symbiont and the erythrocyte the host.
- Paralog-family over-annotation: K13 is a BTB-Kelch protein in a large family
 (PANTHER PTHR45632 per UniProt). No KEAP1-derived mammalian function (e.g. NFE2L2
 regulation — the Reactome cross-references R-PFA-9755511 "KEAP1-NFE2L2 pathway" and
 R-PFA-4641258 "Degradation of DVL" are inferred-event projections, not parasite
 annotations) was transferred into this review; *P. falciparum* has no NFE2L2.

## Curation decisions

| Term | Evidence | Action |
|---|---|---|
| GO:0005515 protein binding | IPI, PMID:25874676 (PfPI3K) | REMOVE (term uninformative; interaction accepted and kept in IntAct, no supportable MF to modify to) |
| GO:0009410 response to xenobiotic stimulus | IDA, PMID:24352242 | MARK_AS_OVER_ANNOTATED |
| GO:0051260 protein homooligomerization | IEA, InterPro IPR003131 | KEEP_AS_NON_CORE |
| GO:0006897 endocytosis | NEW | core |
| GO:0044002 acquisition of nutrients from host | NEW | core |

Proposed new terms: a BP child of endocytosis for cytostome-mediated uptake of host
cell cytosol, and a CC term for the Kelch13 compartment.
