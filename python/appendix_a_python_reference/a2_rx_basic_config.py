import adi

sdr = adi.Pluto()
sdr.rx_lo = 1_000_000_000
sdr.rx_sample_rate = 2_000_000
sdr.rx_rf_bandwidth = 2_000_000
sdr.gain_control_mode = "manual"
sdr.rx_hardwaregain = 20

samples = sdr.rx()
print(samples[:10])
