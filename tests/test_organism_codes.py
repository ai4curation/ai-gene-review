"""Test organism code support in gene fetching.

This module tests the ability to use UniProt organism codes (like PSEPK, ECOLI)
in addition to common names and taxonomy IDs.
"""

from unittest.mock import patch, MagicMock

import pytest

from ai_gene_review.etl.gene import (
    resolve_organism_code_to_taxon,
    resolve_gene_to_uniprot,
    uniprot_by_gene_taxon,
    get_organism_name_from_uniprot,
    expand_organism_name,
)


class TestOrganismCodeResolution:
    """Test organism code to taxon ID resolution."""

    @patch("ai_gene_review.etl.gene.requests.get")
    def test_resolve_organism_code_to_taxon(self, mock_get):
        """Test resolving UniProt organism codes to taxonomy IDs."""
        # Mock response for PSEPK
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [
                {
                    "taxonId": 160488,
                    "scientificName": "Pseudomonas putida KT2440",
                    "mnemonic": "PSEPK",
                }
            ]
        }
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        # Test PSEPK
        taxon_id = resolve_organism_code_to_taxon("PSEPK")
        assert taxon_id == "160488"

        # Verify API call
        mock_get.assert_called_with(
            "https://rest.uniprot.org/taxonomy/stream",
            params={"query": "mnemonic:PSEPK", "format": "json", "size": "1"},
            timeout=10,
        )

    @patch("ai_gene_review.etl.gene.requests.get")
    def test_resolve_organism_code_not_found(self, mock_get):
        """Test handling of unknown organism codes."""
        # Mock empty response
        mock_response = MagicMock()
        mock_response.json.return_value = {"results": []}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        # Test unknown code
        taxon_id = resolve_organism_code_to_taxon("XXXXX")
        assert taxon_id is None

    @patch("ai_gene_review.etl.gene.requests.get")
    def test_resolve_organism_code_api_error(self, mock_get):
        """Test handling of API errors."""
        # Mock API error
        mock_get.side_effect = Exception("API Error")

        # Should return None on error
        taxon_id = resolve_organism_code_to_taxon("PSEPK")
        assert taxon_id is None


class TestOrganismNameFetching:
    """Test fetching organism names from UniProt."""

    @patch("ai_gene_review.etl.gene.requests.get")
    def test_get_organism_name_from_uniprot(self, mock_get):
        """Test fetching organism name from UniProt ID."""
        # Mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "organism": {"scientificName": "Pseudomonas putida (strain KT2440)"}
        }
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        # Test fetching name
        name = get_organism_name_from_uniprot("Q88JH0")
        assert name == "Pseudomonas putida (strain KT2440)"

        # Verify API call
        mock_get.assert_called_with(
            "https://rest.uniprot.org/uniprotkb/Q88JH0?format=json&fields=organism_name",
            timeout=10,
        )

    @patch("ai_gene_review.etl.gene.requests.get")
    def test_get_organism_name_api_error(self, mock_get):
        """Test handling of API errors when fetching organism name."""
        mock_get.side_effect = Exception("API Error")

        # Should return None on error
        name = get_organism_name_from_uniprot("Q88JH0")
        assert name is None


class TestUniprotLookupWithOrganismCodes:
    """Test UniProt lookups with different organism identifiers."""

    @patch("ai_gene_review.etl.gene.requests.get")
    @patch("ai_gene_review.etl.gene.resolve_organism_code_to_taxon")
    def test_uniprot_lookup_with_organism_code(self, mock_resolve, mock_get):
        """Test UniProt lookup using organism code."""
        # Mock organism code resolution
        mock_resolve.return_value = "160488"

        # Mock UniProt API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [
                {
                    "primaryAccession": "Q88JH0",
                    "uniProtkbId": "PEDH_PSEPK",
                    "genes": [{"geneName": {"value": "pedH"}}],
                    "organism": {"scientificName": "Pseudomonas putida KT2440"},
                }
            ]
        }
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        # Test lookup
        results = uniprot_by_gene_taxon("pedH", "PSEPK", limit=1)

        assert len(results) == 1
        assert results[0]["accession"] == "Q88JH0"
        assert results[0]["gene"] == "pedH"
        assert results[0]["organism"] == "Pseudomonas putida KT2440"

        # Verify organism code was resolved
        mock_resolve.assert_called_once_with("PSEPK")

        # Verify correct query was built
        expected_query = (
            "(gene_exact:pedH) AND (organism_id:160488) AND (reviewed:true)"
        )
        call_args = mock_get.call_args[1]["params"]
        assert call_args["query"] == expected_query

    @patch("ai_gene_review.etl.gene.requests.get")
    def test_uniprot_lookup_with_common_name(self, mock_get):
        """Test UniProt lookup using common organism name."""
        # Mock UniProt API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [
                {
                    "primaryAccession": "P04637",
                    "uniProtkbId": "P53_HUMAN",
                    "genes": [{"geneName": {"value": "TP53"}}],
                    "organism": {"scientificName": "Homo sapiens"},
                }
            ]
        }
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        # Test lookup with common name
        results = uniprot_by_gene_taxon("TP53", "human", limit=1)

        assert len(results) == 1
        assert results[0]["accession"] == "P04637"
        assert results[0]["gene"] == "TP53"
        assert results[0]["organism"] == "Homo sapiens"

        # Verify correct query was built (should use taxon ID for human)
        expected_query = "(gene_exact:TP53) AND (organism_id:9606) AND (reviewed:true)"
        call_args = mock_get.call_args[1]["params"]
        assert call_args["query"] == expected_query

    @patch("ai_gene_review.etl.gene.requests.get")
    def test_uniprot_lookup_with_taxon_id(self, mock_get):
        """Test UniProt lookup using NCBI taxon ID."""
        # Mock UniProt API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [
                {
                    "primaryAccession": "P00722",
                    "uniProtkbId": "BGAL_ECOLI",
                    "genes": [{"geneName": {"value": "lacZ"}}],
                    "organism": {"scientificName": "Escherichia coli K12"},
                }
            ]
        }
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        # Test lookup with taxon ID
        results = uniprot_by_gene_taxon("lacZ", "83333", limit=1)

        assert len(results) == 1
        assert results[0]["accession"] == "P00722"
        assert results[0]["gene"] == "lacZ"

        # Verify correct query was built
        expected_query = "(gene_exact:lacZ) AND (organism_id:83333) AND (reviewed:true)"
        call_args = mock_get.call_args[1]["params"]
        assert call_args["query"] == expected_query


class TestOrganismNameExpansion:
    """Test organism name expansion functionality."""

    def test_expand_common_names(self):
        """Test expansion of common organism names."""
        assert expand_organism_name("human") == "Homo sapiens"
        assert expand_organism_name("mouse") == "Mus musculus"
        assert expand_organism_name("yeast") == "Saccharomyces cerevisiae"
        assert expand_organism_name("fly") == "Drosophila melanogaster"
        assert expand_organism_name("worm") == "Caenorhabditis elegans"

    def test_preserve_scientific_names(self):
        """Test that scientific names are preserved."""
        assert expand_organism_name("Homo sapiens") == "Homo sapiens"
        assert expand_organism_name("Escherichia coli") == "Escherichia coli"

    @patch("ai_gene_review.etl.gene.requests.get")
    def test_expand_organism_code(self, mock_get):
        """Test expansion of UniProt organism codes."""
        # Mock response for PSEPK
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [
                {
                    "scientificName": "Pseudomonas putida (strain KT2440)",
                    "taxonId": 160488,
                    "mnemonic": "PSEPK",
                }
            ]
        }
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = expand_organism_name("PSEPK")
        assert result == "Pseudomonas putida (strain KT2440)"

        # Verify API call
        mock_get.assert_called_with(
            "https://rest.uniprot.org/taxonomy/stream",
            params={"query": "mnemonic:PSEPK", "format": "json", "size": "1"},
            timeout=10,
        )

    @patch("ai_gene_review.etl.gene.requests.get")
    def test_expand_taxon_id(self, mock_get):
        """Test expansion of taxon IDs."""
        # Mock response for taxon ID
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "results": [
                {
                    "scientificName": "Escherichia coli str. K-12 substr. MG1655",
                    "taxonId": 511145,
                }
            ]
        }
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = expand_organism_name("511145")
        assert result == "Escherichia coli str. K-12 substr. MG1655"

        # Verify API call
        mock_get.assert_called_with(
            "https://rest.uniprot.org/taxonomy/stream",
            params={"query": "id:511145", "format": "json", "size": "1"},
            timeout=10,
        )

    @patch("ai_gene_review.etl.gene.requests.get")
    def test_expand_unknown_code(self, mock_get):
        """Test handling of unknown organism codes."""
        # Mock empty response
        mock_response = MagicMock()
        mock_response.json.return_value = {"results": []}
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        # Should return original if not found
        result = expand_organism_name("XXXXX")
        assert result == "XXXXX"

    def test_case_insensitive_common_names(self):
        """Test that common names are case-insensitive."""
        assert expand_organism_name("Human") == "Homo sapiens"
        assert expand_organism_name("HUMAN") == "Homo sapiens"
        assert expand_organism_name("ecoli") == "Escherichia coli"
        assert expand_organism_name("E.coli") == "Escherichia coli"


class TestResolveGeneToUniprotPrimarySymbolPreference:
    """Regression tests for the resolver bug behind issue #910.

    UniProt's ``gene_exact:`` query matches both primary gene symbols and
    deprecated synonyms. Before the fix, a Swiss-Prot entry for gene Y that
    listed gene X as a deprecated synonym would shadow a TrEMBL entry whose
    primary symbol is X (the actual gene the user asked for). These tests
    encode the desired behavior: prefer primary-symbol matches; fall through
    to TrEMBL for non-human organisms when only synonym matches exist in
    Swiss-Prot.
    """

    @patch("ai_gene_review.etl.gene.uniprot_by_gene_taxon")
    def test_csr1_synonym_in_swissprot_falls_through_to_trembl(
        self, mock_lookup
    ):
        """worm csr-1 scenario: Swiss-Prot returns nhr-47 (csr-1 as synonym),
        TrEMBL returns the actual CSR-1 Argonaute entries."""
        swissprot_synonym_hit = [
            {
                "accession": "Q17370",
                "entry_name": "NHR47_CAEEL",
                "gene": "nhr-47",  # NOTE: primary is nhr-47, not csr-1
                "organism": "Caenorhabditis elegans",
            }
        ]
        trembl_primary_hits = [
            {
                "accession": "H2KZD5",
                "entry_name": "H2KZD5_CAEEL",
                "gene": "csr-1",
                "organism": "Caenorhabditis elegans",
            },
            {
                "accession": "Q27GU1",
                "entry_name": "Q27GU1_CAEEL",
                "gene": "csr-1",
                "organism": "Caenorhabditis elegans",
            },
        ]
        mock_lookup.side_effect = [swissprot_synonym_hit, trembl_primary_hits]

        result = resolve_gene_to_uniprot("csr-1", "worm")

        # Must NOT pick Q17370 (csr-1 is only a synonym there)
        assert result != "Q17370"
        # Must pick the first TrEMBL primary-symbol hit
        assert result == "H2KZD5"

        # Verify the resolver actually consulted both Swiss-Prot and TrEMBL
        assert mock_lookup.call_count == 2
        first_call_kwargs = mock_lookup.call_args_list[0].kwargs
        second_call_kwargs = mock_lookup.call_args_list[1].kwargs
        assert first_call_kwargs.get("reviewed_only") is True
        assert second_call_kwargs.get("reviewed_only") is False

    @patch("ai_gene_review.etl.gene.uniprot_by_gene_taxon")
    def test_primary_symbol_match_returned_directly(self, mock_lookup):
        """Normal case: Swiss-Prot has a primary-symbol match — return it."""
        swissprot_hits = [
            {
                "accession": "P04637",
                "entry_name": "P53_HUMAN",
                "gene": "TP53",
                "organism": "Homo sapiens",
            }
        ]
        mock_lookup.return_value = swissprot_hits

        result = resolve_gene_to_uniprot("TP53", "human")

        assert result == "P04637"
        # Only one lookup needed — no TrEMBL fallthrough
        assert mock_lookup.call_count == 1

    @patch("ai_gene_review.etl.gene.uniprot_by_gene_taxon")
    def test_primary_symbol_filter_is_case_insensitive(self, mock_lookup):
        """Primary-symbol comparison must be case-insensitive."""
        swissprot_hits = [
            {
                "accession": "P12830",
                "entry_name": "CADH1_HUMAN",
                "gene": "CDH1",
                "organism": "Homo sapiens",
            }
        ]
        mock_lookup.return_value = swissprot_hits

        # Lower-case query against upper-case primary symbol — should still match
        assert resolve_gene_to_uniprot("cdh1", "human") == "P12830"

    @patch("ai_gene_review.etl.gene.uniprot_by_gene_taxon")
    def test_human_synonym_only_raises_informative_error(self, mock_lookup):
        """For human, synonym-only matches must raise — never silently return
        the wrong gene's entry. Error message must mention the synonym hits."""
        swissprot_synonym_hit = [
            {
                "accession": "Q99999",
                "entry_name": "OTHER_HUMAN",
                "gene": "OTHER",
                "organism": "Homo sapiens",
            }
        ]
        mock_lookup.return_value = swissprot_synonym_hit

        with pytest.raises(ValueError) as excinfo:
            resolve_gene_to_uniprot("FAKEGENE", "human")

        msg = str(excinfo.value)
        assert "FAKEGENE" in msg
        # Error must hint at the synonym match so the user can act
        assert "Q99999" in msg or "synonym" in msg.lower()
        # Must not have consulted TrEMBL for human
        assert mock_lookup.call_count == 1

    @patch("ai_gene_review.etl.gene.uniprot_by_gene_taxon")
    def test_worm_no_hits_anywhere_raises(self, mock_lookup):
        """Non-human gene with no Swiss-Prot or TrEMBL hits at all must raise."""
        mock_lookup.return_value = []

        with pytest.raises(ValueError):
            resolve_gene_to_uniprot("nonexistent-gene", "worm")

        # Should have tried both Swiss-Prot and TrEMBL
        assert mock_lookup.call_count == 2
