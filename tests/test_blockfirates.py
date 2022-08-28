from blockfirates.client import BlockFiRates


def test_rates_returned():
    assert len(BlockFiRates().get_all_rates()) > 0


def test_get_info_type():
    assert isinstance(BlockFiRates().get_info("BTC"), dict)


def test_get_info_apy_type():
    assert isinstance(BlockFiRates().get_info(symbol="BTC")["info"]["apy"], float)
