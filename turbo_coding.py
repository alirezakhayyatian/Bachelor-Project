#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: turbo_coding
# Author: Alireza Khayyatiyan
# Description: AUT:bachelor thesis
# Generated: Fri Jan 20 22:20:48 2023
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
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import trellis
from gnuradio import trellis, digital
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import gnuradio.trellis.fsm_utils as fu
import math
import numpy
import sip
import sys
from gnuradio import qtgui


class turbo_coding(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "turbo_coding")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("turbo_coding")
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

        self.settings = Qt.QSettings("GNU Radio", "turbo_coding")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.mod = mod = fu.psk2x3
        self.dim = dim = mod[0]
        self.constellation = constellation = mod[1]
        self.prefix = prefix = "C:/Program Files/GNURadio-3.7/share/gnuradio/examples/trellis/fsm_files"
        self.modulation = modulation = fu.pam4
        self.channel = channel = fu.c_channel
        self.block = block = 1000
        self.EsN0_dB = EsN0_dB = 2
        self.Es = Es = sum(numpy.square(constellation))/(len(constellation)/(1.0*dim))
        self.tot_mod = tot_mod = fu.make_isi_lookup(modulation,channel,False)
        self.samp_rate = samp_rate = 32000
        self.noisevar = noisevar = 10**(-EsN0_dB/10.0)  * Es   /2.0
        self.interleaver = interleaver = trellis.interleaver(block,666)
        self.fsm_o2 = fsm_o2 = trellis.fsm(prefix+"/awgn2o3_4.fsm")
        self.fsm_o = fsm_o = trellis.fsm(prefix+"/awgn1o2_4.fsm")
        self.fsm_i = fsm_i = trellis.fsm(prefix+"/awgn2o3_4.fsm")
        self.R = R = 100e3

        ##################################################
        # Blocks
        ##################################################
        self.trellis_viterbi_x_0_0 = trellis.viterbi_b(trellis.fsm(fsm_o), block, -1, -1)
        self.trellis_viterbi_x_0 = trellis.viterbi_b(trellis.fsm(fsm_i), block, -1, -1)
        self.trellis_metrics_x_0_1 = trellis.metrics_f(4, 2, ([0,1,2,3]), digital.TRELLIS_EUCLIDEAN)
        self.trellis_metrics_x_0_0 = trellis.metrics_f(2**dim, dim, (constellation), digital.TRELLIS_EUCLIDEAN)
        self.trellis_encoder_xx_0_0_0 =  trellis.encoder_bb(trellis.fsm(fsm_o2), 0, 0) if False else trellis.encoder_bb(trellis.fsm(fsm_o2), 0)
        self.trellis_encoder_xx_0_0 =  trellis.encoder_bb(trellis.fsm(fsm_o), 0, 0) if False else trellis.encoder_bb(trellis.fsm(fsm_o), 0)
        self.trellis_encoder_xx_0 =  trellis.encoder_bb(trellis.fsm(fsm_i), 0, 0) if False else trellis.encoder_bb(trellis.fsm(fsm_i), 0)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	'B', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [0, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	'X', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [0, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("BER")

        labels = ['BER', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bf((constellation), dim)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_char*1, R,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, R,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='SER',
        	win_size=block*100,
        	bits_per_symbol=1,
        )
        self.analog_random_source_x_0_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, 1007)), True)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, 1007)), True)
        self._EsN0_dB_range = Range(-10, 20, 1, 2, 200)
        self._EsN0_dB_win = RangeWidget(self._EsN0_dB_range, self.set_EsN0_dB, 'Es/N0 (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._EsN0_dB_win)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blks2_error_rate_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_random_source_x_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blks2_error_rate_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.trellis_metrics_x_0_1, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.trellis_encoder_xx_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.trellis_encoder_xx_0_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.trellis_metrics_x_0_0, 0))
        self.connect((self.trellis_encoder_xx_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.trellis_encoder_xx_0_0, 0), (self.trellis_encoder_xx_0, 0))
        self.connect((self.trellis_encoder_xx_0_0_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.trellis_encoder_xx_0_0_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.trellis_metrics_x_0_0, 0), (self.trellis_viterbi_x_0, 0))
        self.connect((self.trellis_metrics_x_0_1, 0), (self.trellis_viterbi_x_0_0, 0))
        self.connect((self.trellis_viterbi_x_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.trellis_viterbi_x_0_0, 0), (self.blks2_error_rate_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "turbo_coding")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_mod(self):
        return self.mod

    def set_mod(self, mod):
        self.mod = mod
        self.set_dim(self.mod[0])
        self.set_constellation(self.mod[1])

    def get_dim(self):
        return self.dim

    def set_dim(self, dim):
        self.dim = dim
        self.trellis_metrics_x_0_0.set_O(2**self.dim)
        self.trellis_metrics_x_0_0.set_D(self.dim)
        self.set_Es(sum(numpy.square(self.constellation))/(len(self.constellation)/(1.0*self.dim)))

    def get_constellation(self):
        return self.constellation

    def set_constellation(self, constellation):
        self.constellation = constellation
        self.trellis_metrics_x_0_0.set_TABLE((self.constellation))
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.constellation))
        self.set_Es(sum(numpy.square(self.constellation))/(len(self.constellation)/(1.0*self.dim)))

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.set_fsm_o2(trellis.fsm(self.prefix+"/awgn2o3_4.fsm"))
        self.set_fsm_o(trellis.fsm(self.prefix+"/awgn1o2_4.fsm"))
        self.set_fsm_i(trellis.fsm(self.prefix+"/awgn2o3_4.fsm"))

    def get_modulation(self):
        return self.modulation

    def set_modulation(self, modulation):
        self.modulation = modulation
        self.set_tot_mod(fu.make_isi_lookup(self.modulation,self.channel,False))

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel
        self.set_tot_mod(fu.make_isi_lookup(self.modulation,self.channel,False))

    def get_block(self):
        return self.block

    def set_block(self, block):
        self.block = block
        self.trellis_viterbi_x_0_0.set_K(self.block)
        self.trellis_viterbi_x_0.set_K(self.block)
        self.set_interleaver(trellis.interleaver(self.block,666))

    def get_EsN0_dB(self):
        return self.EsN0_dB

    def set_EsN0_dB(self, EsN0_dB):
        self.EsN0_dB = EsN0_dB
        self.set_noisevar(10**(-self.EsN0_dB/10.0)  * self.Es   /2.0)

    def get_Es(self):
        return self.Es

    def set_Es(self, Es):
        self.Es = Es
        self.set_noisevar(10**(-self.EsN0_dB/10.0)  * self.Es   /2.0)

    def get_tot_mod(self):
        return self.tot_mod

    def set_tot_mod(self, tot_mod):
        self.tot_mod = tot_mod

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_noisevar(self):
        return self.noisevar

    def set_noisevar(self, noisevar):
        self.noisevar = noisevar

    def get_interleaver(self):
        return self.interleaver

    def set_interleaver(self, interleaver):
        self.interleaver = interleaver

    def get_fsm_o2(self):
        return self.fsm_o2

    def set_fsm_o2(self, fsm_o2):
        self.fsm_o2 = fsm_o2
        self.trellis_encoder_xx_0_0_0.set_FSM(trellis.fsm(self.fsm_o2))

    def get_fsm_o(self):
        return self.fsm_o

    def set_fsm_o(self, fsm_o):
        self.fsm_o = fsm_o
        self.trellis_viterbi_x_0_0.set_FSM(trellis.fsm(self.fsm_o))
        self.trellis_encoder_xx_0_0.set_FSM(trellis.fsm(self.fsm_o))

    def get_fsm_i(self):
        return self.fsm_i

    def set_fsm_i(self, fsm_i):
        self.fsm_i = fsm_i
        self.trellis_viterbi_x_0.set_FSM(trellis.fsm(self.fsm_i))
        self.trellis_encoder_xx_0.set_FSM(trellis.fsm(self.fsm_i))

    def get_R(self):
        return self.R

    def set_R(self, R):
        self.R = R
        self.blocks_throttle_0_0.set_sample_rate(self.R)
        self.blocks_throttle_0.set_sample_rate(self.R)


def main(top_block_cls=turbo_coding, options=None):

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
