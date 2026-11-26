# Existing-member consultation

Both BACSU reviews remain COMPLETE after substantive review of all 18 original rows. No annotation was added, removed, reordered or changed outside its review object. The two historical PcrB NEW assertions remain NEW with their original payloads.

## Scientific corrections

- **EgsA:** The glycerophospholipid-process claim is UNDECIDED. A recombinant enzyme making G1P and a downstream enzyme consuming G1P establish chemical compatibility, not a demonstrated native connection. Different forward/reverse KM values do not establish net cellular direction. No un-fed egsA deletion/complementation lipidomics proving the EgsA–PcrB connection was identified.
- **Cofactors:** GO0050492 is refined to both existing is_a children GO0106357/GO0106358. Preferred NAD activity remains core; secondary NADP activity remains KEEP_AS_NON_CORE. The author dissertation Table 10 gives efficiencies 13,800 ± 830 versus 108 ± 27.77 M−1s−1 (pH 8.2, 45°C). Lower efficiency or unmeasured native use does not make measured molecular activity false. The core uses the NAD-specific function; the module's broad NAD(P) requirement remains a valid biochemical ancestor.
- **PcrB:** Magnesium binding becomes ACCEPT because the metal is required for catalysis, rather than peripheral merely because a reaction-specific term exists. Both inherited NEW claims are retained. Ether synthesis directly supports the lipid process; it does not imply a bulk structural membrane lipid or every downstream protein-modification process.
- **Distribution and topology:** Bacillus carrier biology is not transferred to all PcrB homologs; PcrB is more widespread than LhaT. Ac-HepG membrane translocation and recycling remain unresolved. No autonomous transport function is asserted.
- **PAINT:** Normal lineage-loss checks found no IRD/IKR for either target. PcrB's broad inherited prenyltransferase assertion agrees with direct target assays. The short donor list is not used to reconstruct a specific ancestral C35 substrate scope.

## Source scope

PMID18558723 remains an abstract-only protected cache. The authoritative Guldan 2010 author dissertation was independently acquired, with exact source hash and scoped evidence under `genes/BACSU/egsA/egsA-source-analysis/`. Its pMUTIN4 araM disruption in 168 was tested for LTA abundance. Subsequent lipid labeling fed external 14C-G1P, bypassing endogenous synthesis; it supports PcrB-dependent conversion, not EgsA flux. The full PDF and extract remain ignored. The kinetic table was visually inspected.

PMID42286214 cites prior engineered E. coli lipid synthesis without AraM; it neither identifies the alternative mechanism nor directly demonstrates it in B. subtilis. The paper's own data concern PlsY/PlsC specificity. PMID40626731 provides native Bacillus carrier biology. Cached full primary23322418 and21214173 support PcrB chemistry. Protected publication caches were not refreshed or manually edited; no newly fetched publication cache is part of this handoff. The online full PMID24684232 was accessible, but quotations retained in the reviews are from its frozen abstract. Other abstract-only references remain identified as such.

Both requested default Falcon calls failed HTTP403; no provider file was manufactured. Manual source review and notes document the evidence actually used. Current QuickGO term definitions and the two NAD(P)-child relationships are captured in `quickgo-terms.json`, retrieved 2026-11-07 from the URLs embedded there.

## Verification

`check_preservation.py` compares ordered non-review payloads against the immutable root baseline, prior NEW actions and append-only notes against the pinned base commit, and every one of the 17 protected source hashes. Focused validation logs, render results, helper-created history paths and the exact final path/hash manifest are recorded in the ignored existing-review handoff. No module, family, project or shared-source edits were made by this consultation.
