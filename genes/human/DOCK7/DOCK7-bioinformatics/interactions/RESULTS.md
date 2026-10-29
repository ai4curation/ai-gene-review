# DOCK7 interaction extraction results

The source graph contains nine incident DOCK7 records. Two match the LRCH1/LRCH3 subset: LRCH3 bait to DOCK7 prey, edge 552514, and LRCH1 bait to DOCK7 prey, edge 554276. The original PMID:40205054 study uses tagged-bait AP-MS in human U2OS cells. These are complex associations; no purified binary affinity is inferred.

The OpenCell CSV contains eighteen incident DOCK7 records and two selected partner records. DOCK7 is the endogenous-tagged bait, with LRCH1 at physical line 7610 and LRCH3 at physical line 7612 (header included). Complete prey accession groups remain in the JSON. No unique natural splice product is assigned from a group.

All other incident records are retained as context rather than interpreted as negative evidence. The source-specific directions differ across studies and are not combined into a single synthetic experiment. The extraction was executed successfully against the exact saved primary inputs, and a second saved-input replay compared every output field with the checked JSON. Dependencies are Python 3.9+ only.
