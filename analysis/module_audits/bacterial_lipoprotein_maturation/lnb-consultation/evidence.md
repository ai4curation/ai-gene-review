# Lnb terminal lipoprotein N-acylation: independent consultation

Full PMID39495918 (Armbruster et al., 2024, “Identification and characterization of the lipoprotein N-acyltransferase in Bacteroides”) was read from the unchanged complete publication cache. The final journal article, not the earlier preprint PMID38853980, supplies the evidence. Retrieval/classification captures are dated 2026-11-07 UTC.

## Exact identities and classification

| Target | UniProt / taxon | Native sequence | Evidence role |
|---|---|---|---|
| B. fragilis NCTC 9343 BF9343_0945 | Q5LGL3 / NCBITaxon:272559; BACFN | 408 aa | Exact genomic clone restores N-acylation in E. coli lacking lnt. |
| B. thetaiotaomicron VPI-5482 BT_4364 | Q89ZL3 / NCBITaxon:226186; BACTN | 395 aa | Native VPI-5482-derived Δtdk deletion/complementation, endogenous reporters and Cys substitutions. |

The paper identifies the loci; official UniProt queries independently connect them to accessions and exact strain records. No existing gene review was found by locus or accession before normal `just fetch-gene` seeding. Both resulting seeds have zero annotation rows. Source-provided locus gene symbols are retained, with the literature alias `lnb` added.

Both raw records carry InterPro IPR025178, “Lnb, N-terminal periplasmic domain,” and IPR057436, “Lnb-like, transmembrane domain,” together with Pfam PF13387/PF25221 and NCBIfam NF051878 (`lpactltferLnb`). These are official current assignments. The InterPro entries are domains; IPR025178 also occurs with other domains, so it is not a universal whole-protein Lnb selector by itself. Neither protein has a PANTHER cross-reference or a seeded IBA row. PAINT-loss tools report that lineage losses could not be checked; no claim of absence of losses is made.

## Assays and their limits

BF9343_0945 rescues a conditional E. coli lnt strain, then supports replacement/deletion of the host lnt in a Δlpp background. The purified species in the decisive product assay is the Lpp(K58A)-Strep reporter, not purified Lnb. The primary states: “we purified Lpp(K58A)-Strep from the Δlnt strain carrying pBF9343_0945 and analyzed its N-terminal tryptic peptide”. The MS/MS product fragments establish N-acylation. This is strong cellular activity evidence but not a B. fragilis knockout, an isolated enzyme turnover assay, donor identification or kinetics.

BT_4364 is tested in its native VPI-5482-derived Δtdk background. Lpp and the endogenous BT_3736/BT_3183 reporters shift to smaller forms on deletion and regain triacylation with complementation. The source states: “In each case, complementation of the ΔBT_4364 strain with BT_4364 under the constitutive promoter us1311 was sufficient to restore triacylation.” The living deletion strain shows that Lnb is not universally essential under those conditions. It does not establish that every Bacteroidota strain tolerates its loss.

C148S fails the cellular rescue retained by C198S. The relevant source says: “Only Lnb(C198S) could restore N-acylation activity to Δlnb cells, suggesting that C148 is essential for activity of Lnb”. This shows functional importance of C148; an acyl-cysteine intermediate is not directly demonstrated, and a residue's chemical role is not separated experimentally from stability/folding effects. H49 and N66 are model/conservation candidates, not independently assayed catalytic residues. The current Q89ZL3 sequence contains H49/N66/C148/C198. Its length is 395 aa, whereas the paper narrative says 398; the cause remains unresolved. None of these residue numbers is copied to the 408-aa B. fragilis protein.

Five membrane helices and the periplasmic orientation of the N-terminal domain are predicted. The topology model in the primary is B. thetaiotaomicron Lnb; both targets independently carry the corresponding raw domain/membrane predictions. Whole-client-proteome fractionation is not a localization assay for Lnb or a resolution of client inner-versus-outer-membrane placement. The source explicitly states: “As analysis was performed on TM, these data do not indicate protein localization in the inner versus outer membrane.”

The full Results/Methods do not identify a physiological Lnb acyl donor or report purified-Lnb reconstitution. The Discussion concludes: “Further studies are required to characterize Lnb at the enzymatic level and within other Bacteroides strains.” Canonical Lnt's phospholipid-donor EC reaction and the related LnsA structural comparison are not transferred as demonstrated Lnb donor chemistry or protease activity.

## Terms and additions

Each gene receives two NEW assertions: GO:0016747 (acyltransferase activity, transferring groups other than amino-acyl groups; EXP) and GO:0042158 (lipoprotein biosynthetic process; IMP). The experimentally established acceptor modification fits the acyltransferase genus without fixing a donor. The generic EXP code records cellular experimental characterization and does not imply purified-enzyme IDA. The BP passes the participation test: Lnb supplies the N-acyl modification step itself, not merely a substrate consumed by it.

Fresh exact-term QuickGO queries find GO:0042158 on the same-role canonical Lnt comparators E. coli P23930 (5 annotations) and P. putida KT2440 Q88DN4 (1 annotation). These are comparator states used only in reasoning, not biological supporting quotations. A preliminary query using a non-Lnt identifier was excluded and remains transparently recorded as rejected in the acquisition receipt. Current GO confirms GO:0016410 is obsolete and GO:0140186 describes acyl-CoA-dependent lysine N6 acylation, not the observed N-terminal cysteine chemistry. The GO-CAM index was checked for both targets and the two exact-role comparators; the result is recorded in gocam-comparator-check.json and is not used as positive evidence. The two new terms have different aspects and no ancestor/descendant redundancy; no other BP is proposed.

No growth, cell morphology, polysaccharide-utilization, client-transport or OMV-production activity is inferred from downstream phenotypes. Core location remains broad membrane association supported by target topology prediction. No NEW localization row is added merely to silence the resulting nonblocking annotation-coverage suggestion.

## Acquisition and preservation

Both real Falcon attempts failed HTTP403 authentication/access rejection. Logs are retained; no generated-provider report was invented. The normal-fetch raw files and full primary cache are frozen in seed-baseline.json. The checker verifies exact identities, sequences/classification, tested BT residue identities, verbatim primary support, comparator counts and source hashes, and reports the original zero-row seeds separately from the four newly authored assertions. No module/family/project edits, commits, pushes or full-corpus validation are part of this consultation.
