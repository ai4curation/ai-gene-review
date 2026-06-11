# EMC1 (human, Q8N766) — review notes

## Identity / architecture
- 993 aa precursor; cleaved signal peptide (1..22); large lumenal domain (23..962), single TM helix (963..983), short cytoplasmic tail (984..993) — i.e. a single-pass type I membrane protein [file:human/EMC1/EMC1-uniprot.txt "Single-pass type I membrane protein"].
- Large lumenal region is a GOLD-like / WD40-YVTN β-propeller (Gene3D 2.130.10.10; Pfam Beta-prop_EMC1_N + EMC1_C; InterPro IPR026895). N-glycosylated at N370/N818/N913; disulfides 227-237, 338-368. It is the largest EMC subunit and acts as a lumenal scaffold; it is non-catalytic.
- Belongs to the EMC1 family.

## Function (EMC complex context)
- Component of the ER membrane protein complex (EMC) [file:human/EMC1/EMC1-uniprot.txt "Component of the ER membrane protein complex (EMC)."], a 9-10 subunit conserved ER insertase/chaperone [PMID:32439656 "The nine-subunit \nendoplasmic reticulum (ER) membrane protein complex (EMC) is a conserved co- and \nposttranslational insertase at the ER."].
- The EMC enables energy-independent insertion of newly synthesized membrane proteins, preferring TMDs that are weakly hydrophobic or have destabilizing (charged/aromatic) features [file:human/EMC1/EMC1-uniprot.txt "enables the energy-independent insertion into endoplasmic"].
- EMC is a transmembrane-domain insertase: purified EMC in liposomes catalyzes insertion of tail-anchored substrates (e.g. squalene synthase) [PMID:29242231 "Purified EMC in synthetic liposomes catalyzed the insertion of its substrates in a reconstituted system."].
- Cotranslational role in multipass biogenesis; engages clients after TMD clusters enriched for charged residues [PMID:29809151 "the ER membrane protein complex (EMC) binds to and promotes the biogenesis of a range of multipass transmembrane proteins"].
- Sets topology: EMC inserts the first TMD of GPCRs co-translationally in N-exo orientation, cooperating with Sec61 [PMID:30415835 "EMC inserts TMDs co-translationally and cooperates with the Sec61 translocon to ensure accurate topogenesis of many membrane proteins."].
- Catalytic insertase vestibule is formed by EMC3 + EMC6, NOT EMC1 [PMID:32439656 "occurs via an enclosed hydrophilic vestibule within the membrane formed by the subunits EMC3 and EMC6"]. EMC1 contributes as a structural lumenal scaffold subunit (contributes_to / part_of qualifiers in GOA reflect this complex-level contribution).

## Localization
- ER membrane (IDA) first established in the ERAD interaction-mapping study that identified EMC subunits [PMID:22119785; file:human/EMC1/EMC1-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"].

## Disease
- Biallelic/monoallelic variants cause CAVIPMR (cerebellar atrophy, visual impairment, psychomotor retardation; MIM 616875), AR neurodegenerative disorder [file:human/EMC1/EMC1-uniprot.txt "Cerebellar atrophy, visual impairment, and psychomotor"]. Variants: T82M, G471R, G868R (PMID:26942288); A144T in retinitis pigmentosa (uncertain; PMID:23105016).

## Protein-binding IPIs
- Three GO:0005515 IPI annotations all derive from SARS-CoV-2 interactome screens with viral partner P0DTC8 (ORF8) [file:human/EMC1/EMC1-uniprot.txt "Q8N766; P0DTC8: 8; Xeno"] — PMID:32353859, 33060197, 36217030. Bare protein binding, viral partner, not core EMC function → KEEP_AS_NON_CORE.

## Review decisions summary
- Core: EMC complex membership (GO:0072546, part_of); ER membrane localization (GO:0005789); contribution to complex insertase activity (GO:0032977, contributes_to) and insertion processes (GO:0071816 TA, GO:0045050 stop-transfer) — ACCEPT.
- Generic parents (GO:0016020 membrane, GO:0032991 protein-containing complex, GO:0005783 ER) — correct but uninformative → KEEP_AS_NON_CORE.
- No REMOVE/MODIFY/UNDECIDED calls; all experimental/complex annotations verifiable and consistent.

## Verification pass (2026-06-11) — verbatim supporting text confirmed
- EMC complex membership: uniprot "Component of the ER membrane protein complex (EMC)." [file:human/EMC1/EMC1-uniprot.txt].
- ER membrane localization: uniprot "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane" (IDA from PMID:22119785, which is the ERAD interaction-mapping paper that identified EMC subunits) [file:human/EMC1/EMC1-uniprot.txt].
- TA insertion / insertase activity reconstituted: [PMID:29242231 "Purified EMC in \nsynthetic liposomes catalyzed the insertion of its substrates in a reconstituted \nsystem."] and [PMID:29242231 "EMC is a transmembrane domain insertase"].
- Cotranslational multipass biogenesis & charged-residue clusters: [PMID:29809151 "the ER membrane protein complex (EMC) binds to and promotes the \nbiogenesis of a range of multipass transmembrane proteins"] and "immediately following \nclusters of TMDs enriched for charged residues".
- Topogenesis / N-exo first TMD of GPCRs, cooperates with Sec61: [PMID:30415835 "EMC inserts TMDs co-translationally and cooperates \nwith the Sec61 translocon to ensure accurate topogenesis of many membrane \nproteins."] and "the co-translational \ninsertion of the first transmembrane domain (TMD)".
- Catalytic vestibule is EMC3+EMC6 (EMC1 is non-catalytic lumenal scaffold): [PMID:32439656 "occurs via an enclosed hydrophilic \nvestibule within the membrane formed by the subunits EMC3 and EMC6"]; EMC is "a conserved co- and \nposttranslational insertase at the ER." Note PMID:32439656 full_text_available: false (abstract only) but abstract suffices for cited claims.
- GO:0032977 (membrane insertase activity) carries contributes_to qualifier — correct framing for a scaffold subunit; the WHOLE complex has insertase activity. ACCEPT.
- GO:0032991 (protein-containing complex) IDA from PMID:28246125 (MGI; ZMPSTE24/influenza paper) — cached text has no EMC mention (abstract about ZMPSTE24 antiviral role); this is a generic complex co-purification annotation, generic parent of EMC complex → KEEP_AS_NON_CORE (do not REMOVE an IDA per guidelines).
- Three GO:0005515 protein binding IPI all target viral P0DTC8 (SARS-CoV-2 ORF8): uniprot "Q8N766; P0DTC8: 8; Xeno" → real virus-interactome captures, bare uninformative term → KEEP_AS_NON_CORE.

