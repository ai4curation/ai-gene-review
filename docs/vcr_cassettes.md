# VCR Cassettes for Integration Tests

Integration tests make HTTP calls to UniProt, QuickGO, InterPro, CATH, NCBI Entrez, and other APIs. VCR cassettes record these responses once and replay them, making tests fast and deterministic.

## Quick Reference

| Command | What it does | Network? | Time |
|---------|-------------|----------|------|
| `just pytest` | Unit tests only | No | ~14s |
| `just pytest-integration` | Replay from cassettes | No | ~90s |
| `just record-cassettes` | Record missing cassettes | Yes | ~14 min |
| `just rerecord-cassettes` | Re-record all cassettes | Yes | ~14 min |
| `just test-full` | Unit + integration | No | ~2 min |

## Recording Cassettes

Cassettes must be recorded once before integration tests can replay. This requires network access.

```bash
# Record cassettes for any tests that don't have one yet
just record-cassettes

# Re-record ALL cassettes from scratch (e.g. after API changes)
just rerecord-cassettes
```

Recording runs with `-x` (stop on first failure) and `-v` (verbose) so you can see progress.

## How It Works

An autouse fixture in `tests/conftest.py` detects `@pytest.mark.integration` tests and wraps them in a VCR cassette context. No changes to test code are needed.

- Cassettes are stored at `tests/cassettes/<module>/<test_name>.yaml`
- Parametrized tests get unique cassettes automatically (pytest node name includes params)
- VCR matches requests on method, URI, and body
- Auth headers (`Authorization`, `X-API-Key`, `Cookie`) are filtered out of recordings

## Adding New Integration Tests

1. Mark your test with `@pytest.mark.integration`
2. Run `just record-cassettes` to record its cassette
3. Commit the cassette YAML file along with your test

```python
@pytest.mark.integration
def test_my_new_api_call():
    response = requests.get("https://rest.uniprot.org/uniprotkb/P12345")
    assert response.status_code == 200
```

## Skipping VCR for Specific Tests

Some tests download large binary data (e.g. oaklib downloads multi-GB sqlite databases) that VCR cannot serialize. Use `@pytest.mark.vcr_skip` to bypass VCR while keeping the `integration` marker:

```python
@pytest.mark.integration
@pytest.mark.vcr_skip  # oaklib downloads multi-GB sqlite databases
def test_validate_term_real_api():
    ...
```

These tests always make live calls (or use locally cached data) and have no cassette file.

## When to Re-record

Re-record cassettes when:

- An upstream API changes its response format
- You need to update test assertions to match current API data
- A cassette file gets corrupted or deleted

```bash
# Re-record everything
just rerecord-cassettes

# Re-record a single test's cassette by deleting it and recording
rm tests/cassettes/test_publication_etl/test_fetch_pubmed_data.yaml
just record-cassettes
```

## VCR Record Modes

The `--vcr-record` flag controls behavior:

| Mode | Behavior |
|------|----------|
| `none` (default) | Replay only; fails if cassette is missing |
| `new_episodes` | Replay existing, record any new requests |
| `all` | Re-record everything from scratch |

## Troubleshooting

**MemoryError when recording**: The test likely downloads a very large response (>500MB). Add `@pytest.mark.vcr_skip` to bypass VCR for that test.

**CannotSendRequest during replay**: The cassette doesn't contain a matching request. Either the test changed its HTTP calls or the cassette needs re-recording. Run `just record-cassettes` to add the missing request.

**Tests pass in recording but fail in replay**: Check if the test depends on response timing or uses `time.sleep()` — VCR replays responses instantly but sleep calls still execute.
