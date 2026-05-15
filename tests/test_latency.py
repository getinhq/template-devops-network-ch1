import pytest

import latency


def test_measure_once_requires_implementation():
    with pytest.raises(NotImplementedError):
        latency.measure_once("127.0.0.1")


def test_measure_once_returns_positive_ms():
    # After implementation, patch or use a reliable local target.
    ms = latency.measure_once("127.0.0.1")
    assert isinstance(ms, float)
    assert ms >= 0.0
