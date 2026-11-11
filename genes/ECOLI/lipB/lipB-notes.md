# lipB (P60720) notes

Reviewed for the endogenous protein lipoylation module (modules/endogenous_protein_lipoylation.yaml).

## Literature sources

No deep-research provider is configured in this session (no provider API key), so no
`-deep-research-*.md` file was generated. These notes rest on the cached publications
(all abstract-only for this gene) and the UniProt record.

## Function

- Octanoyl-ACP:protein N-octanoyltransferase, EC 2.3.1.181, step 1/2 of endogenous lipoylation.
  [file:ECOLI/lipB/lipB-uniprot.txt "Catalyzes the transfer of endogenously produced octanoic acid from octanoyl-acyl-carrier-protein onto the lipoyl domains of lipoate-dependent enzymes"]
- Purified LipB transfers octanoyl from octanoyl-ACP to apo-H protein; Km 10.2 uM (octanoyl-ACP), 13.2 uM (apo-H).
  [PMID:15642479 "We also show that the protein catalyzes the transfer of the octanoyl group from octanoyl-ACP to apo-H protein"]
- lipB encodes the enzyme (not a regulator); also transfers lipoyl from lipoyl-ACP in vitro; active protein starts at an upstream TTG.
  [PMID:12591875 "We now report genetic and biochemical evidence demonstrating that lipB encodes the lipoyltransferase."]
- Acyl-thioester intermediate on Cys169 (UniProt ACT_SITE 169).
- Co-purifies with intact PDH and OGDH complexes and binds ACP tightly; GcvH does not co-purify.
  [PMID:21209092 "We also report that LipB forms a very tight, albeit noncovalent, complex with acyl carrier protein."]

## dam regulation row

PMID:11072067 maps the cde-4 insertion (raising dam P2 promoter activity) to lipB. No mechanism;
treated as an indirect consequence of loss of lipoylation (MARK_AS_OVER_ANNOTATED).
