from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Sequence
import numpy as np
import adi


@dataclass
class RxConfig:
    lo_hz: int
    sample_rate_hz: int
    rf_bw_hz: int
    gain_db: int = 20
    gain_mode: str = "manual"
    channels: Sequence[int] = (0,)


@dataclass
class TxConfig:
    lo_hz: int
    sample_rate_hz: int
    rf_bw_hz: int
    gain_db: int = -10


def pluto_connect(uri: Optional[str] = None):
    """Connect to ADALM-Pluto (default USB/Ethernet)."""
    return adi.Pluto(uri) if uri else adi.Pluto()


def pluto_rx_config(sdr, cfg: RxConfig) -> None:
    sdr.rx_enabled_channels = list(cfg.channels)
    sdr.rx_lo = int(cfg.lo_hz)
    sdr.rx_sample_rate = int(cfg.sample_rate_hz)
    sdr.rx_rf_bandwidth = int(cfg.rf_bw_hz)
    sdr.gain_control_mode = cfg.gain_mode
    if cfg.gain_mode == "manual":
        sdr.rx_hardwaregain = int(cfg.gain_db)


def pluto_tx_config(sdr, cfg: TxConfig) -> None:
    sdr.tx_lo = int(cfg.lo_hz)
    sdr.tx_sample_rate = int(cfg.sample_rate_hz)
    sdr.tx_rf_bandwidth = int(cfg.rf_bw_hz)
    sdr.tx_hardwaregain_chan0 = int(cfg.gain_db)


def pluto_rx_block(sdr) -> np.ndarray:
    """Receive one block of complex IQ samples."""
    return np.asarray(sdr.rx())


def pluto_tx(sdr, wave: np.ndarray) -> None:
    """Transmit complex baseband waveform."""
    sdr.tx(np.asarray(wave))


def pluto_tx_stop(sdr) -> None:
    """Stop TX safely."""
    try:
        sdr.tx_destroy_buffer()
    except Exception:
        pass
