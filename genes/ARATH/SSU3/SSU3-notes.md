# SSU3 (Q9LYT7, At3g58990) review notes

## Identity / nomenclature
- IPMI SSU3 (Knill 2009) = AtLeuD2 (He 2010) = IPMI1 (Gigolashvili 2009). [PMID:19597944 "At2g43090 (IPMI SSU1), At2g43100 (IPMI SSU2), and At3g58990 (IPMI SSU3)"]; [PMID:19542295 "IPMI1 ( At3g58990 ), IPMI2 ( At2g43100 )"]
- Small (LeuD, domain-4) subunit; determines substrate specificity of the heterodimer. [PMID:32612621 "Our study shows that the substrate recognition region that differs between IPMI SSU1 and the other two IMPI SSUs determines the substrate preference of IPMI."]

## Function: glucosinolate-specialized paralog
- [PMID:20663849 "Reverse genetics and metabolite profiling showed that AtLeuD1 and AtLeuD2 function redundantly in aliphatic glucosinolate biosynthesis, but AtLeuD3 is not likely to be involved in this pathway."]
- ssu3-1 single mutant (Ws) weak: [PMID:19597944 "The very weak phenotype of the ipmi ssu3-1 might be due to this mutant being in the Ws-0 background, which per se contains predominantly short-chain glucosinolates"]
- Double knockout: [PMID:24608865 "our metabolite profiling of an ipmi ssu2-1/ipmi ssu3-1 double knockout mutant showed the absolute requirement of these two genes for the biosynthesis of C7 and C8 glucosinolates"]
- Not a Leu-pathway subunit in vivo: [PMID:24608865 "Furthermore, IPMI SSU2 and SSU3 play no substantial role in Leu biosynthesis, since IPM does not accumulate to higher levels when both genes are inactivated."] but capable of IPM turnover [PMID:24608865 "On the contrary, IPMI containing SSU2 or SSU3 subunits has a broad substrate range including Met derivatives with different side-chain lengths and IPM."] and residual Leu synthesis when SSU1 depleted [PMID:24608865 "As indicated by the normal green color a residual Leu biosynthesis occurs in or along the vasculature by the participation of IPMI SSU2 and/or IPMI SSU3."]

## Localization
- Plastid (N-terminal GFP) [PMID:19542295]; full-length SSU3:GFP in chloroplast-sized plastids of vascular-associated cells [PMID:32612621 "IPMI SSU1 is found in small plastids, whereas IMPI SSU2 and SSU3 are found in chloroplasts."]; stroma [PMID:20663849].

## Curation decisions
- L-leucine biosynthetic process (IBA, IEA) -> MARK_AS_OVER_ANNOTATED (paralog functional divergence; propagation_review added against PTN002879868).
- GO:0003861 (IBA/IDA/IEA) accepted: SSU3-containing IPMI can act on IPM, but it is a secondary capability; core MF is contributes_to GO:0120528.
- NEW: GO:0009316 complex membership (IPI, PMID:20663849).
- Falcon deep research not available at time of review.
