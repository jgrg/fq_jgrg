import pytest
import fq_stats

def test_long():
    assert fq_stats.main(["--count", "test/data/wiki_example.fq"]) == 2

def test_short():
    assert fq_stats.main(["-c", "test/data/wiki_example.fq"]) == 2
