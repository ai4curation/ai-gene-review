# PRKAB2 notes

## AMPK beta-2 scaffold

PRKAB2 encodes the beta-2 scaffold subunit of AMPK. AMPK is an
alpha/beta/gamma heterotrimer whose catalytic alpha activation loop is switched
on by Thr172 phosphorylation, while the gamma subunit binds AMP, ADP and ATP
[PMID:21399626, "AMPK is a heterotrimeric complex comprising an α catalytic subunit and two regulatory subunits (β and γ)1."]. The beta subunit is the
glycogen-binding scaffold in that complex [PMID:25412657, "AMPK consists of an α-subunit with an N-terminal kinase domain (KD) and a regulatory C-terminus, a glycogen-binding β-subunit, and an AMP/ADP/ATP-binding γ-subunit"].

Beta-2 is represented directly in several structural AMPK complexes. PMID:25412657
solved human alpha1/beta2/gamma1 holo-AMPK, while PMID:29657085 solved
activated alpha2/beta2/gamma1 and alpha2/beta1/gamma1 complexes to analyse
beta-2-selective activation [PMID:29657085, "structures of the glucose importagog SC4 bound to activated α2β2γ1 and α2β1γ1"].

PAINT asserts the same five PTHR10343 root terms on PRKAB2 as on PRKAB1:
nucleus, cytoplasm, nucleotide-activated protein kinase complex, protein kinase
binding, and signal transduction. The AMPK complex and alpha-kinase binding
assertions are correct for PRKAB2, and the cytosolic rows are core. Nuclear and
broad signaling rows are kept as non-core.

## Adipose thermogenesis and ER rows

The cold-induced thermogenesis rows trace to an adipocyte-specific mouse double
knockout of both beta subunits. The experiment removed beta-1 and beta-2 from
brown and white adipocytes and impaired cold-induced BAT function
[PMID:27411013, "found that iβ1β2AKO mice\nwere cold intolerant and resistant to β-adrenergic activation of BAT and beiging"].
That supports a non-core thermogenesis role for beta-containing AMPK complexes.

The Reactome ER-lumen row comes from an AMPK to PD-L1 phosphorylation event
[Reactome:R-HSA-9931292, "AMP-activated protein kinase (AMPK), activated in response to metformin, directly binds with PD-L1 (CD274) and phosphorylates S195 of PD-L1."]. PD-L1 can be the ER/secretory substrate, but the PRKAB2-containing
AMPK heterotrimer should not be annotated as an ER-lumen protein.

PRKAB2 is also covered by a large IntAct GO:0005515 block. Those rows are
removed uniformly because bare protein binding records a physical contact
without a beta-subunit molecular function; removal does not dispute the
reported interactions.
