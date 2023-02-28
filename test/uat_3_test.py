import pytest
import fq_stats

def test_long():
    assert fq_stats.main(["--count", "test/data/wiki_example.fq.gz"]) == 2

def test_short():
    assert fq_stats.main(["--length", "test/data/wiki_example.fq.gz"]) == 72 * 2
