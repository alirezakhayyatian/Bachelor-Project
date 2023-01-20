#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: receiver
# Author: alireza khayyatiyan
# Generated: Fri Jan 20 21:56:46 2023
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import trellis
from gnuradio import trellis, digital
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import math
import numpy as np
import pmt
import sip
import sys
from gnuradio import qtgui


class rx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "receiver")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("receiver")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
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

        self.settings = Qt.QSettings("GNU Radio", "rx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 2
        self.prefix = prefix = "C:/Program Files/GNURadio-3.7/share/gnuradio/examples/trellis/fsm_files"
        self.block = block = 1000
        self.sensitivity = sensitivity = np.pi/(2*sps)
        self.samp_rate = samp_rate = 1e6
        self.interleaver = interleaver = trellis.interleaver(block,666)
        self.fsm_o = fsm_o = trellis.fsm(prefix+"/awgn1o2_4.fsm")
        self.fsm_i = fsm_i = trellis.fsm(prefix+"/awgn2o3_4.fsm")

        ##################################################
        # Blocks
        ##################################################
        self.trellis_sccc_decoder_x_0 = trellis.sccc_decoder_b(
            trellis.fsm(fsm_o), 0, -1,
            trellis.fsm(fsm_i), 0, -1,
            trellis.interleaver(trellis.interleaver(block,666)),
            block,
            10,
                        trellis.TRELLIS_MIN_SUM)

        self.trellis_metrics_x_0 = trellis.metrics_f(8, 3, ([-1,-1,-1,   -1,-1,1,    -1,1,-1,   -1,1,1,  1,-1,-1,   1,-1,1,  1,1,-1,  1,1,1  ]), digital.TRELLIS_EUCLIDEAN)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'RF frequency', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_ff(digital.TED_MOD_MUELLER_AND_MULLER, sps, 0.045, 1.0, 1.0, 1.5, 1, digital.constellation_bpsk().base(), digital.IR_MMSE_8TAP, 128, ([]))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, 'E:\\webcam\\grc\\recorder.bin', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_char*1, 'E:\\webcam\\grc\\image.jpg', False)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code='',
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(1.0/sensitivity)
        self.analog_agc3_xx_0 = analog.agc3_cc(1e-3, 1e-4, 1.0, 1.0, 1)
        self.analog_agc3_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc3_xx_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.analog_agc3_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.trellis_metrics_x_0, 0))
        self.connect((self.trellis_metrics_x_0, 0), (self.trellis_sccc_decoder_x_0, 0))
        self.connect((self.trellis_sccc_decoder_x_0, 0), (self.blks2_packet_decoder_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_sensitivity(np.pi/(2*self.sps))

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.set_fsm_o(trellis.fsm(self.prefix+"/awgn1o2_4.fsm"))
        self.set_fsm_i(trellis.fsm(self.prefix+"/awgn2o3_4.fsm"))

    def get_block(self):
        return self.block

    def set_block(self, block):
        self.block = block
        self.set_interleaver(trellis.interleaver(self.block,666))

    def get_sensitivity(self):
        return self.sensitivity

    def set_sensitivity(self, sensitivity):
        self.sensitivity = sensitivity
        self.analog_quadrature_demod_cf_0.set_gain(1.0/self.sensitivity)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_interleaver(self):
        return self.interleaver

    def set_interleaver(self, interleaver):
        self.interleaver = interleaver

    def get_fsm_o(self):
        return self.fsm_o

    def set_fsm_o(self, fsm_o):
        self.fsm_o = fsm_o

    def get_fsm_i(self):
        return self.fsm_i

    def set_fsm_i(self, fsm_i):
        self.fsm_i = fsm_i


def main(top_block_cls=rx, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
