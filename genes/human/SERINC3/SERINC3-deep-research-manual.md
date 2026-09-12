# Manual deep-research synthesis for human SERINC3

Date: 2026-07-18

## Scope and retrieval

This synthesis covers human SERINC3 (UniProtKB Q13530) using the reviewed
UniProt record, all 15 grouped GOA annotations, five GOA-cited primary papers,
the 2023 human SERINC3 cryo-EM/scramblase study, and a 2025 computational
preprint on its lipid-translocation mechanism. Falcon failed with HTTP 402 and
the Perplexity-lite fallback failed with HTTP 401 because quota was unavailable.
No provider-labelled report was retained.

## Molecular function

SERINC3 is a 473-residue multipass membrane protein with two helical bundles
joined by a tilted crossmember helix. Purified human SERINC3 reconstituted into
proteoliposomes flips phosphatidylserine, phosphatidylethanolamine, and
phosphatidylcholine without ATP [PMID:37474505, "purified hSERINCs reconstituted
into proteoliposomes induce flipping of phosphatidylserine (PS),
phosphatidylethanolamine and phosphatidylcholine."]. It therefore has direct
phospholipid-scramblase activity rather than merely the older, broad
"molecular carrier" description.

Evidence conclusion: SERINC3 is a non-ATP-dependent phospholipid scramblase at
the plasma membrane.

The 2005 family study reported increased incorporation of serine into membrane
lipid synthesis and called SERINCs carrier proteins [PMID:16120614, "facilitates
the synthesis of two serine-derived lipids, phosphatidylserine and
sphingolipids."]. That work motivated the family name, but the direct human
SERINC3 structure and purified-protein assay now support the more specific
scramblase term. The evidence reviewed here does not establish that SERINC3
itself transports free serine across a membrane.

## Antiviral mechanism

SERINC3 is a cell-intrinsic retroviral restriction factor. When present in the
producer-cell plasma membrane it is incorporated into budding HIV-1 particles,
where it reduces subsequent infectivity. Combined SERINC3/SERINC5 knockout and
re-expression experiments establish the phenotype [PMID:26416733, "SERINC3 and
SERINC5 together restricted HIV-1 replication"]. An independent screen found
SERINC3 to be a weaker but still detectable inhibitor than SERINC5
[PMID:26416734, "SERINC5, and to a lesser extent SERINC3, as a potent inhibitor
of HIV-1 particle infectivity"].

The 2023 study connects the molecular and antiviral functions: SERINC3-driven
lipid scrambling exposes phosphatidylserine on virions, disrupts membrane
asymmetry, alters Env conformation, and reduces infectivity
[PMID:37474505, "SERINC3, SERINC5 and the scramblase TMEM16F expose PS on the
surface of HIV-1 and reduce infectivity"]. Nef counteracts restriction by
excluding SERINC3 from virions and redirecting it away from the cell surface.

A 2025 preprint uses molecular-dynamics enhanced sampling to propose a
credit-card-like phosphatidylserine pathway rather than classical alternating
access [PMID:41292925, "hSERINC3 adopts a \"credit card\" mechanism of lipid
scrambling"]. This supports mechanism-level hypotheses but does not change the
GO-level scramblase assignment.

## Localization and boundaries

Plasma-membrane localization is central to both lipid scrambling and virion
incorporation. Golgi-membrane annotations are consistent with biosynthetic
trafficking and conserved mammalian localization. Perinuclear localization is
infection-conditioned: HIV-1 Nef redirects SERINC proteins to an endosomal/
perinuclear compartment, so it is retained as non-core rather than presented as
the primary steady-state location.

The neurodegeneration interactome record is a candidate binary interaction and
does not define a SERINC3 biochemical function. Generic protein binding is
therefore marked over-annotated.

