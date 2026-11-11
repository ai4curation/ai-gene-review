# Enterobacterial FadE/FadBA evidence limits

Full articles were acquired separately into ignored cache; shared publication records were not refreshed. Extracted text uses BeautifulSoup article.get_text(" ", strip=True). The small quotations below retain that exact text, including the publisher spacing in E. c oli.

## PMID:12057976
Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC135136/?report=xml ; accessed 2026-11-06; HTML SHA256 f684f7810e122ce1f5c27fff34578576da07326d694b2ea3dd07772c21b597bc.

However, our array analysis and prior genetic analysis give no candidates for an ETF homologue in the FadR regulon.

## PMID:16385050
Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC1347308/?report=xml ; accessed 2026-11-06; HTML SHA256 f8a2887ae94b83709542aca79cd3a68473daa1e73b1e24fa1d3c61d269b92b04.

All bacterial strains are derivatives of E. c oli K-12 or S. enterica LT2.
The inserts of the resultant plasmids were sequenced to verify the fidelity of the cloned PCR products.
Our results indicate that no single step of the β-oxidation cycle is responsible for the greater efficiency of the S. enterica system.

## Construct and physiological interpretation

PMID12057976 identifies yafH as fadE using MG1655 derivatives, minimal coding-sequence complementation and allele analysis. JWC266 is the fadE disruption; the C8/C10/C12 substrate-growth test uses its fadR613::Tn10 derivative JWC267. The study does not purify an ETF-coupled FadE system. Extra terminal domains are proposed as possible electron-transfer machinery, not demonstrated ETF activity.

PMID16385050 amplifies fadE and fadBA from LT2 genomic DNA, verifies the insert sequences and integrates pSH72 (fadE) and pSH68 (fadBA) into corresponding E. coli deletion backgrounds. Current reviewed LT2 UniProt identities are Q8ZRJ7/STM0309, Q9L6L5/STM3983 and P0A2H7/STM3982; the paper provides strain/gene construct identity rather than a deposited sequence accession for each insert. FadBA is exchanged as a pair, so it does not independently localize the efficiency difference to either subunit or to one catalytic site.

Wild-type LT2 grows slowly on decanoate; wild-type UB1005 does not under the reported conditions. Octanoate/hexanoate utilization is distinguished in fadR strains. Oleate CoA profiles compare SI92 (UB1005 panD) and SI81 (LT2 panD); medium-chain profiles use their fadR backgrounds, acetate growth and added octanoate/hexanoate. The paper reports near-complete substrate conversion to acetyl-CoA in the tested Salmonella cultures and accumulation of intermediates in E. coli, not identical endpoints implied by homologous spiral enzymes. Butyrate as an external sole carbon source is not equivalent to intracellular butyryl-CoA processing. HPLC intermediate assignments use retention times; long-chain substituted intermediates are less precisely identified.

Replacing E. coli fadBA alone did not markedly improve long/medium-chain clearance. LT2 fadE improved clearance; replacing both fadE and fadBA further reduced the C4-retention-time intermediate. These are pathway-complementation/metabolite experiments, not purified FadE Michaelis constants or proof that isolated Salmonella FadA alone completes every fatty acid substrate. No PA14/Pa10348 enzyme kinetics are transferred to either enterobacterial target.

## Ontology boundary

GO:0070991 medium-chain fatty acyl-CoA dehydrogenase activity: Catalysis of the reaction: a medium-chain 2,3-saturated fatty acyl-CoA + H+ + oxidized [electron-transfer flavoprotein] = a medium-chain trans-(2E)-enoyl-CoA + reduced [electron-transfer flavoprotein]. A medium-chain fatty acid has an aliphatic tail containing 6 to 12 carbons.

GO:0004466 long-chain fatty acyl-CoA dehydrogenase activity: Catalysis of the reaction: a long-chain 2,3-saturated fatty acyl-CoA + H+ + oxidized [electron-transfer flavoprotein] = a long-chain (2E)-enoyl-CoA + reduced [electron-transfer flavoprotein]. A long-chain fatty acid has an aliphatic tail containing 13 to 22 carbons.

GO:0003995 acyl-CoA dehydrogenase activity: Catalysis of the reaction: a 2,3-saturated acyl-CoA + H+ oxidized [electron-transfer flavoprotein] = a (2E)-enoyl-CoA + reduced [electron-transfer flavoprotein].

QuickGO source: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003995,GO:0004466,GO:0070991 ; checked 2026-11-06. All three definitions explicitly name electron-transfer flavoprotein. The proposed acceptor-unspecified reaction retains demonstrated acyl-CoA oxidation without asserting that ETF has been excluded.
