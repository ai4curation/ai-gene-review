# SERINC5 manual deep-research synthesis

## Scope and provenance

This manual synthesis was prepared after the required automated deep-research attempt failed: Falcon returned HTTP 402 (payment required), and the Perplexity-lite fallback returned HTTP 401 (insufficient quota). No failed provider-named output was retained. Evidence was instead assembled from the reviewed human UniProtKB record Q86VE9, all 18 GOA rows, every locally cached GOA publication, the cached Reactome event R-HSA-8932980, and an additional primary study that directly tests the proposed connection between scrambling and antiviral restriction.

## Molecular function

Evidence conclusion: SERINC5 is a non-ATP-dependent phospholipid scramblase at the plasma membrane and in retroviral envelopes. Purified/reconstituted human SERINC proteins move phosphatidylserine (PS), phosphatidylethanolamine (PE), and phosphatidylcholine (PC) between membrane leaflets [PMID:37474505, "purified hSERINCs reconstituted into proteoliposomes induce flipping of phosphatidylserine (PS), phosphatidylethanolamine and phosphatidylcholine."]. The same study measured SERINC5-dependent PS exposure on HIV-1 particles [PMID:37474505, "The incorporation of hSERINC5 resulted in the exposure of PS on the surface of virus particles"]. A later independent study confirmed that virion-incorporated SERINC5 eliminates PS asymmetry [PMID:38785977, "This asymmetry is completely lost upon incorporation of SER5 or TMEM16F."].

The 2005 Serinc-family study described a carrier-like contribution to serine-derived lipid synthesis [PMID:16120614, "facilitates the synthesis of two serine-derived lipids, phosphatidylserine and sphingolipids."]. This abstract does not demonstrate free-serine transmembrane transport by human SERINC5, and the newer direct molecular evidence identifies phospholipid scrambling. Therefore GO:0140104 molecular carrier activity is biologically related but too broad and should be replaced by GO:0017128 phospholipid scramblase activity. The legacy Reactome event title asserting L-serine transport should not be treated as direct proof of that transport mechanism.

## Antiviral role and mechanism boundary

SERINC5 is a potent intrinsic retroviral restriction factor. It resides at the producer-cell plasma membrane, is incorporated into budding HIV-1 particles, and inhibits subsequent entry; HIV-1 Nef redirects SERINC5 to an endosomal compartment and excludes it from virions [PMID:26416734, "SERINC5 localizes to the plasma membrane, where it is efficiently incorporated into budding HIV-1 virions and impairs subsequent virion penetration of susceptible target cells."] [PMID:26416734, "Nef redirects SERINC5 to a Rab7-positive endosomal compartment and thereby excludes it from HIV-1 particles."]. Knockdown, knockout, and re-expression experiments independently establish the role of SERINC5 (together with SERINC3) in restricting HIV-1 replication [PMID:26416733, "SERINC3 and SERINC5 together restricted HIV-1 replication"].

Scrambling and antiviral restriction are both well established, but the causal link is not. The 2023 study correlated PS exposure with reduced infectivity [PMID:37474505, "SERINC3, SERINC5 and the scramblase TMEM16F expose PS on the surface of HIV-1 and reduce infectivity"]. However, direct lipid-manipulation experiments subsequently found that PS externalization itself is not the principal restriction mechanism [PMID:38785977, "PS externalization is likely not the key driver for infectivity reduction by SER5."]. The review therefore represents phospholipid scrambling and antiviral innate immunity as distinct core functions/roles while leaving their mechanistic relationship unresolved.

## Localization and peripheral evidence

Plasma-membrane localization is directly supported by two 2015 HIV-1 studies, the 2023 lipid-scrambling study, HPA immunofluorescence, and reviewed UniProt. Perinuclear localization is infection-conditioned: Nef/GlycoGag removes SERINC5 from the surface and redirects it to endosomal/perinuclear compartments, so it is valid but non-core.

The HPA cytosol row conflicts with SERINC5's established multipass-membrane topology and cannot be evaluated from a cached primary record, so it remains UNDECIDED rather than being overruled. The urinary-exosome HDA paper is abstract-only in the cache and does not mention SERINC5 in the accessible text; the extracellular-exosome row also remains UNDECIDED. The phosphatidylserine-metabolic-process ISS row is retained as non-core because older mammalian family evidence and reviewed UniProt support a possible effect on serine-derived lipid synthesis, but direct human evidence defines scrambling rather than lipid synthesis as the proximal activity.

## Isoforms and open questions

Reviewed UniProt lists four isoforms (Q86VE9-1 through Q86VE9-4). The cited functional studies do not establish isoform-specific scrambling, trafficking, Nef sensitivity, or antiviral potency. The most important unresolved questions are how SERINC5 scrambling is regulated in uninfected cells, which lipid/membrane effect actually causes restriction, and whether the four isoforms differ in these activities.
