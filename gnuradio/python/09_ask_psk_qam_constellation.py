#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ASK / PSK / QAM Constellations (Baseband)
# Author: DJ2RF
# Description: Generate 4-ASK, BPSK, QPSK, 16QAM and show constellation
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class ask_psk_qam_constellation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ASK / PSK / QAM Constellations (Baseband)", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ASK / PSK / QAM Constellations (Baseband)")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ask_psk_qam_constellation")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.sym_rate = sym_rate = 10000
        self.samp_rate = samp_rate = 200000
        self.sps = sps = int(samp_rate/sym_rate)
        self.mode = mode = 2

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            2048, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Spectrum (Selected)', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            2048, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0.enable_grid(True)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['Selected Constellation', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.digital_chunks_to_symbols_xx_qpsk = digital.chunks_to_symbols_ic([0.707+0.707j, 0.707-0.707j, -0.707+0.707j, -0.707-0.707j], 1)
        self.digital_chunks_to_symbols_xx_bpsk = digital.chunks_to_symbols_ic([-1+0j, 1+0j], 1)
        self.digital_chunks_to_symbols_xx_ask = digital.chunks_to_symbols_if([0.25, 0.5, 0.75, 1.0], 1)
        self.digital_chunks_to_symbols_xx_16qam = digital.chunks_to_symbols_ic([ (-3-3j)/3.1623, (-3-1j)/3.1623, (-3+1j)/3.1623, (-3+3j)/3.1623, (-1-3j)/3.1623, (-1-1j)/3.1623, (-1+1j)/3.1623, (-1+3j)/3.1623, ( 1-3j)/3.1623, ( 1-1j)/3.1623, ( 1+1j)/3.1623, ( 1+3j)/3.1623, ( 3-3j)/3.1623, ( 3-1j)/3.1623, ( 3+1j)/3.1623, ( 3+3j)/3.1623 ], 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_gr_complex*1,mode,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_repeat_qpsk = blocks.repeat(gr.sizeof_gr_complex*1, sps)
        self.blocks_repeat_bpsk = blocks.repeat(gr.sizeof_gr_complex*1, sps)
        self.blocks_repeat_ask = blocks.repeat(gr.sizeof_float*1, sps)
        self.blocks_repeat_16qam = blocks.repeat(gr.sizeof_gr_complex*1, sps)
        self.blocks_float_to_complex_ask = blocks.float_to_complex(1)
        self.analog_random_source_x_qpsk = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 4, 1000))), True)
        self.analog_random_source_x_bpsk = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 2, 1000))), True)
        self.analog_random_source_x_ask = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 4, 1000))), True)
        self.analog_random_source_x_16qam = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 16, 1000))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_16qam, 0), (self.digital_chunks_to_symbols_xx_16qam, 0))
        self.connect((self.analog_random_source_x_ask, 0), (self.digital_chunks_to_symbols_xx_ask, 0))
        self.connect((self.analog_random_source_x_bpsk, 0), (self.digital_chunks_to_symbols_xx_bpsk, 0))
        self.connect((self.analog_random_source_x_qpsk, 0), (self.digital_chunks_to_symbols_xx_qpsk, 0))
        self.connect((self.blocks_float_to_complex_ask, 0), (self.blocks_selector_0, 0))
        self.connect((self.blocks_repeat_16qam, 0), (self.blocks_selector_0, 3))
        self.connect((self.blocks_repeat_ask, 0), (self.blocks_float_to_complex_ask, 0))
        self.connect((self.blocks_repeat_bpsk, 0), (self.blocks_selector_0, 1))
        self.connect((self.blocks_repeat_qpsk, 0), (self.blocks_selector_0, 2))
        self.connect((self.blocks_selector_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_16qam, 0), (self.blocks_repeat_16qam, 0))
        self.connect((self.digital_chunks_to_symbols_xx_ask, 0), (self.blocks_repeat_ask, 0))
        self.connect((self.digital_chunks_to_symbols_xx_bpsk, 0), (self.blocks_repeat_bpsk, 0))
        self.connect((self.digital_chunks_to_symbols_xx_qpsk, 0), (self.blocks_repeat_qpsk, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ask_psk_qam_constellation")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sym_rate(self):
        return self.sym_rate

    def set_sym_rate(self, sym_rate):
        self.sym_rate = sym_rate
        self.set_sps(int(self.samp_rate/self.sym_rate))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sps(int(self.samp_rate/self.sym_rate))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.blocks_repeat_16qam.set_interpolation(self.sps)
        self.blocks_repeat_ask.set_interpolation(self.sps)
        self.blocks_repeat_bpsk.set_interpolation(self.sps)
        self.blocks_repeat_qpsk.set_interpolation(self.sps)

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode
        self.blocks_selector_0.set_input_index(self.mode)




def main(top_block_cls=ask_psk_qam_constellation, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
