# Anti-CRISPR suppression audit

## 2026-10-26 — taxon and mechanism revision

Reviews PMID:32503371 and PMID:32186918 were searched and normally cached, then their mechanistic claims were checked against primary studies. They describe structurally diverse stoichiometric inhibitors and enzymatic suppressors; neither establishes one obligatory sequence of Acr activities. The module now has a ONE_OR_MORE set of alternative routes and a separate optional Aca2 expression-control part. Removed recognition→nuclease PRECEDES, recognition→Aca CAUSES, and unrestricted Aca regulation of every inhibitor family. The two Aca2 annotons describe DNA- and RNA-dependent repression of its characterized ZF40 locus, not a sensor that turns on after Cas immunity is disabled.

Stoichiometric inhibition means target occupancy matters; it does not imply every blocker must be in molar excess. Dimeric inhibitors and the 4:2 AcrID1–Cas10d assembly illustrate distinct stoichiometries. Catalytic multiple-turnover assays do not by themselves establish sufficient native expression. Cas9 guide loading, target-DNA/RNA recognition, catalytic activation, effector-subunit sequestration and covalent modification are independent points of attack.

The participant envelope now includes Viruses and Bacteria. Viral genes can be deposited under bacterial prophage records, and PMID:32218510 explicitly identifies Acr genes in plasmids, ICEs, prophages, transposons and integrons. Its E. faecalis conjugation experiments establish protection of targeted mobile plasmids. This does not make every mobile element viral. Bacteria and Archaea are host systems, distinct from the participant's deposited taxon; human-cell editing experiments do not imply natural eukaryotic host defense. Native-expression evidence must be distinguished from heterologous counterdefense capability.

### Representative panel

| Product | Source accession | Review path | Distinct coverage |
|---|---|---|---|
| AcrIF8 | H9C181 | BPZF4/AcrF8 | Cas7f and crRNA contacts |
| AcrIF2 | Q6TM72 | BPD31/orf30 | Type I-F/selected I-C DNA mimic |
| AcrIIA4 | A0A247D711 | LISMN/acrIIA4 | RNA-loaded Cas9 PAM/RuvC-site occlusion |
| AcrIIA2 | A0A059T5F6 | 9CAUD/acrIIA2 | Ortholog-supported convergent DNA mimic |
| AcrIF3 | L7P7R7 | 9CAUD/acrIF3 | Cas2/3 recruitment inhibition |
| AcrIIC1 | A0A2D0TCG3 | NEIME/acrIIC1 | HNH inhibition with DNA binding retained |
| AcrVA1 | A0A5H1ZR47 | 9GAMM/acrVA1 | Cas12a-dependent guide cleavage |
| gp29/AcrIII-1 | Q8QL27 | SIRV1/orf114 | cA4 chemistry, disputed native deployment |
| Aca2 | H9C180 | BPZF4/ACA2 | Local DNA/RNA expression repression |
| AcrID1 | A0A1B3SN05 | 9VIRU/acrID1 | Archaeal Cas10d sequestration |
| AcrIIC2 | A0A425B3G2 | NEIME/acrIIC2 | Cas9 guide-loading inhibition |
| AcrVIA1 Lse | A0A6P3CWF5 | LISSE/acrVIA1 | RNA-targeting type VI-A inhibition |
| AcrVA5 | archived A0A0U2B867 v17 | 9GAMM/acrVA5 | Cas12a lysine acetylation |

Nine original members are retained; four additions cover new mechanism/host combinations. Existing specific InterPro Acr families are retained. New IIC2/VIA1 products have no verified specific InterPro selector. AcrID1's IPR009804 SIFV-Orf14 and AcrVA5's IPR016181 acyltransferase-fold membership are too broad to assert family-wide inhibition. DUF1874/STIV B116-like membership likewise does not establish native anti-CRISPR deployment; gp29 now uses an exact gene-product selector. No PANTHER identifier or ancestral claim is guessed.

### Source-specific limits

- PMID:36805026 extends AcrIF2 activity to the tested D. vulgaris type I-C system; naming does not imply universal type I-F restriction or all type I-C susceptibility.
- LP-101 AcrIIA2 A0A059T5F6 differs by nine residues from the directly assayed prophage protein according to the existing gene notes. The module explicitly preserves ortholog inference.
- PMID:31243272/30850331 show AcrIIC2 blocks Nme1Cas9 guide loading through its bridge helix. It need not bind an already formed RNP. PMID:29507349/33239638 establish SIRV3 AcrID1 and a 4:2 AcrID1:Cas10d complex; a completed target-bound effector resists inhibition.
- PMID:32467331 establishes phage phiLS46 AcrVIA1 against L. seeligeri Cas13a, with one virion sufficient in the tested system. UniProt/PDB 6VRB map 229 residues, whereas the paper describes native gp2 as 232 residues. Preserve the construct-length discrepancy. Unrelated proteins have been called AcrVIA1, so no functional claim is transferred by name alone.
- PMID:30936531 demonstrates AcrVA1-triggered multiple-turnover crRNA cleavage and release of the 3-prime targeting fragment, not a wholly apo effector or universal irreversibility. The original paper leaves catalytic-center identity unresolved; later PMID:31155345 attributes an RNase site to AcrVA1 helix alpha2. The old categorical claim that no candidate catalytic residues exist is removed; precise later assay accessibility is recorded by the individual reviewer.
- PMID:31942067 establishes gp29 cA4 cleavage and suppression after experimental expression. The products carry a 2-prime,3-prime cyclic phosphate; water-mediated hydrolysis is not assumed. Comment PMID:40240860 tests native SIRV2 gp37 and SIRV1 gp29 transplanted into SIRV2, not native SIRV1 infection. Earlier expression rescues protection. Reply PMID:40240850 disputes physiological generalization and raises possible experimental confounders. Both main texts were inspected in the final SIRV review through public primary-text OCR; normal URL caches preserve landing pages rather than that OCR. Chemistry remains established; native counterdefense is disputed and no unconditional process assertion is attached to this member. Type III systems also directly cleave RNA and can have Cas10 nuclease activity or other cyclic-oligonucleotide specificities; cA4 removal does not disable every branch.
- PMID:31428783 supports Aca2 promoter repression; PMID:38987591 adds RNA stem-loop recognition that blocks ribosome access. These are local expression controls, not evidence of universal Aca-dependent phage viability.
- AcrVA5 official UniSave v17 sequence matches RefSeq WP_046699157.1 exactly and PDB 6IUF after its PLGS tag. Exact provenance/reproducible scripts are in its gene folder. PMID:30936526 establishes MbCas12a Lys635 acetylation; PMID:35581175 shows CobB-dependent reversal in tested heterologous systems. Broad GNAT family membership does not select anti-CRISPR activity.

### Further coverage considered

AcrIIA17 E. faecalis WP_002401839.1 and AcrIIA16 plasmid proteins provide valuable nonviral conjugation examples (PMID:32218510), but an exact usable current UniProt mapping was not established. They remain literature-supported scope evidence rather than guessed member identifiers. AcrIIA18 A0A2G3NPZ8_STRMC/WP_099390844.1/PDB7VLM is an exact available guide-cleavage representative, but is not needed to duplicate that mechanism here and should not be relabelled as a nonviral plasmid example without locus evidence. AcrIIA22 target-DNA nicking/supercoil relaxation (PMID:34644300) is another distinct strategy considered; exact member mapping remains outside this panel. The module is representative, not exhaustive of Acr diversity.

Knowledge gaps now concern biological deployment, target breadth and regulation rather than only missing ontology labels. Individual review/source cache ownership was coordinated; all newly used PMIDs were fetched through the normal repository pipeline. No cached source was manually edited.

### Final checks

All seven retained InterPro labels were checked against the official InterPro entry API on 2026-10-26: IPR057730, IPR057728, IPR056215, IPR049085, IPR064626, IPR064663 and IPR015060. Each official full name matches the module verbatim. This manual check is necessary because the focused module validator warns that InterPro is not configured in its OAK resolver; it is not a substitute for a verified family identity. The assayed members retain their existing family assignments, while broad-fold families were not used for the additions.

Module Pydantic schema validation and focused module term/member checks pass. The remaining function-ID advisories concern intentionally ungrounded specific DNA-mimic and ring-nuclease functions; no guessed GO identifiers were supplied. AcrVA5 passes targeted gene validation with two expected advisories because current GOA has zero rows while its evidence-backed core is present. Matching append-only histories were scaffolded and validated for the module and new gene. No commit was made by this worker.

## 2026-10-26: final integration QA

Aligned the module with the final SIRV1 review: corrected the Comment infection scope, attributed the Reply objections, and described cA4 phosphodiester cleavage without assuming hydrolysis. The original enzyme-excess measurements report single-turnover rates, not steady-state kcat. Clarified that host-relative cytoplasm applies to viral products and is not inherited by every bacterial source record. The panel contains 13 distinct proteins: 12 alternative inhibitor mechanisms and optional Aca2 DNA/RNA autoregulation, with no compulsory mechanistic sequence. Replaced an AcrF8 boilerplate research quotation with direct primary evidence, and checked Aca2 crystallographic Mg binding against the original crystallization conditions.


## PR5555 follow-up (2026-10-25)

Added cytoplasm (GO:0005737) alongside host cell cytoplasm in structured context to reflect the existing bacterial-source versus viral-source convention. No mechanism or taxon scope changed. The SIRV1 source bibliography now uses only canonical PMIDs40240860/40240850 for the 2025 exchange; its reproducible publisher-preview/caption extraction supplies accessible evidence without treating Scribd, cookies-error URLs or CDN paths as article identities. The earlier main-text-inspection account above is historical provenance, not a new assertion of full-text cache availability. Figure2 explicitly identifies SIRV2 Para-gp29; existing native-infection caveats remain. AcrVA1 retains its IC catalytic-entity caveat. The AcrIIC2 qualifier suggestion was not adopted: current annotation-reviewer instructions explicitly exclude gene-product relationship qualifiers from review reasoning and editing; the independently supported biological claim remains accepted.


## PR 5555 official AcrIF8 family verification (2026-10-26)

The [official InterPro entry](https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR057730/) confirms IPR057730, Anti-CRISPR protein AcrF8; its integrated signature is Pfam PF25699. The [protein/entry endpoint](https://www.ebi.ac.uk/interpro/api/protein/uniprot/H9C181/entry/interpro/IPR057730/) directly assigns H9C181 across residues 1–92. The [NCBI CDD cd22241 record](https://www.ncbi.nlm.nih.gov/Structure/cdd/cddsrv.cgi?uid=cd22241) and the unchanged representative UniProt record independently corroborate AcrIF8 identity, but CDD is not listed as this InterPro entry's integrated signature. Raw official responses, hashes and a reproducible retrieval script are in `modules/anti_crispr_suppression-source-analysis/`. Retain the verified ID and exact official label; no graph, family scope, function or taxon change.

AcrVA1's gene core now records contribution to the assembled RNase activity, consistent with its existing catalytic-component caveat. The module's existing conditional mechanism is unchanged. The orf114 historical source-access note now explicitly says the former Scribd landing-page cache was removed; no current source cache was deleted or edited.
