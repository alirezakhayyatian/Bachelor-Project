#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Superposition Coding
# Author: Alireza khayyatiyan
# Description: interference_cancellation
# Generated: Fri Jan 20 22:20:21 2023
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
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import trellis
from gnuradio import trellis, digital
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import numpy
import sip
import sys
from gnuradio import qtgui


class int_cancellation1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Superposition Coding")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Superposition Coding")
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

        self.settings = Qt.QSettings("GNU Radio", "int_cancellation1")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.snr_db = snr_db = 10
        self.prefix = prefix = "C:/Program Files/GNURadio-3.7/share/gnuradio/examples/trellis/fsm_files/"
        self.noisevar = noisevar = 10**(-snr_db/10)
        self.fsm2 = fsm2 = "awgn1o2_4.fsm"
        self.fsm1 = fsm1 = "awgn1o2_16.fsm"
        self.block = block = 1000
        self.alpha = alpha = .1
        self.R = R = 100e3

        ##################################################
        # Blocks
        ##################################################
        self._alpha_range = Range(0, 1, .01, .1, 200)
        self._alpha_win = RangeWidget(self._alpha_range, self.set_alpha, 'P1/P', "counter_slider", float)
        self.top_grid_layout.addWidget(self._alpha_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.trellis_viterbi_combined_xx_2 = trellis.viterbi_combined_cb(trellis.fsm(prefix+fsm2), block, -1, -1, 1, ((1-alpha)**0.5*1,(1-alpha)**0.5*1j,(1-alpha)**0.5*(-1j),(1-alpha)**0.5*(-1)), digital.TRELLIS_EUCLIDEAN)
        self.trellis_viterbi_combined_xx_1 = trellis.viterbi_combined_cb(trellis.fsm(prefix+fsm1), block, -1, -1, 1, (alpha**0.5*1,alpha**0.5*1j,alpha**0.5*(-1j),alpha**0.5*(-1)), digital.TRELLIS_EUCLIDEAN)
        self.trellis_viterbi_combined_xx_0_0 = trellis.viterbi_combined_cb(trellis.fsm(prefix+fsm1), block, -1, -1, 1, (alpha**0.5*1,alpha**0.5*1j,alpha**0.5*(-1j),alpha**0.5*(-1)), digital.TRELLIS_EUCLIDEAN)
        self.trellis_viterbi_combined_xx_0 = trellis.viterbi_combined_cb(trellis.fsm(prefix+fsm2), block, -1, -1, 1, ((1-alpha)**0.5*1,(1-alpha)**0.5*1j,(1-alpha)**0.5*(-1j),(1-alpha)**0.5*(-1)), digital.TRELLIS_EUCLIDEAN)
        self.trellis_encoder_xx_2_0 =  trellis.encoder_bb(trellis.fsm(prefix+fsm2), 0, 0) if False else trellis.encoder_bb(trellis.fsm(prefix+fsm2), 0)
        self.trellis_encoder_xx_2 =  trellis.encoder_bb(trellis.fsm(prefix+fsm1), 0, 0) if False else trellis.encoder_bb(trellis.fsm(prefix+fsm1), 0)
        self.trellis_encoder_xx_1 =  trellis.encoder_bb(trellis.fsm(prefix+fsm2), 0, 0) if False else trellis.encoder_bb(trellis.fsm(prefix+fsm2), 0)
        self.trellis_encoder_xx_0 =  trellis.encoder_bb(trellis.fsm(prefix+fsm1), 0, 0) if False else trellis.encoder_bb(trellis.fsm(prefix+fsm1), 0)
        self._snr_db_range = Range(0, 20, 1, 10, 200)
        self._snr_db_win = RangeWidget(self._snr_db_range, self.set_snr_db, 'P/sigma^2 (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._snr_db_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_0.set_title('BER 1 (after cancelling user 2)')

        labels = ['BER', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_0_win, 3, 2, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0.set_title("BER 2 (after cancelling user 1)")

        labels = ['BER', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_win, 3, 1, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("BER 2 (Raw)")

        labels = ['BER', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_win, 2, 1, 1, 1)
        for r in range(2, 3):
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
        self.qtgui_number_sink_0.set_title("BER1 (Raw)")

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
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 2, 2, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	1024, #size
        	'Befor Interference', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0_0.enable_grid(True)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()

        labels = ['Constellation 1', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win, 4, 1, 4, 1)
        for r in range(4, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	'After Interference', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 'Constellation')
        self.qtgui_const_sink_x_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0.enable_grid(True)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['Constellation 2', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 4, 2, 4, 1)
        for r in range(4, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_chunks_to_symbols_xx_0_0_1 = digital.chunks_to_symbols_bc((1,1j,-1j,-1), 1)
        self.digital_chunks_to_symbols_xx_0_0_0 = digital.chunks_to_symbols_bc((1,1j,-1j,-1), 1)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((1,1j,-1j,-1), 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((1,1j,-1j,-1), 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, R,True)
        self.blocks_sub_xx_2_0 = blocks.sub_cc(1)
        self.blocks_sub_xx_2 = blocks.sub_cc(1)
        self.blocks_multiply_const_vxx_2_0 = blocks.multiply_const_vcc(((1-alpha)**0.5, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vcc((alpha**0.5, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc(((1-alpha)**0.5, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((alpha**0.5, ))
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_error_rate_0_0_0_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=block*100,
        	bits_per_symbol=2,
        )
        self.blks2_error_rate_0_0_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=block*100,
        	bits_per_symbol=2,
        )
        self.blks2_error_rate_0_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=block*100,
        	bits_per_symbol=2,
        )
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=block*100,
        	bits_per_symbol=2,
        )
        self.analog_random_source_x_1 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, block)), True)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, block)), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noisevar, -42)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.blks2_error_rate_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blks2_error_rate_0_0_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.trellis_encoder_xx_0, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.blks2_error_rate_0_0, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.blks2_error_rate_0_0_0, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.trellis_encoder_xx_1, 0))
        self.connect((self.blks2_error_rate_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blks2_error_rate_0_0, 0), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.blks2_error_rate_0_0_0, 0), (self.qtgui_number_sink_0_0_0, 0))
        self.connect((self.blks2_error_rate_0_0_0_0, 0), (self.qtgui_number_sink_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_sub_xx_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_sub_xx_2_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.trellis_viterbi_combined_xx_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.trellis_viterbi_combined_xx_2, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_sub_xx_2, 1))
        self.connect((self.blocks_multiply_const_vxx_2_0, 0), (self.blocks_sub_xx_2_0, 1))
        self.connect((self.blocks_sub_xx_2, 0), (self.trellis_viterbi_combined_xx_0, 0))
        self.connect((self.blocks_sub_xx_2_0, 0), (self.trellis_viterbi_combined_xx_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_1, 0), (self.blocks_multiply_const_vxx_2_0, 0))
        self.connect((self.trellis_encoder_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.trellis_encoder_xx_1, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.trellis_encoder_xx_2, 0), (self.digital_chunks_to_symbols_xx_0_0_0, 0))
        self.connect((self.trellis_encoder_xx_2_0, 0), (self.digital_chunks_to_symbols_xx_0_0_1, 0))
        self.connect((self.trellis_viterbi_combined_xx_0, 0), (self.blks2_error_rate_0_0_0, 1))
        self.connect((self.trellis_viterbi_combined_xx_0_0, 0), (self.blks2_error_rate_0_0_0_0, 1))
        self.connect((self.trellis_viterbi_combined_xx_1, 0), (self.blks2_error_rate_0, 1))
        self.connect((self.trellis_viterbi_combined_xx_1, 0), (self.trellis_encoder_xx_2, 0))
        self.connect((self.trellis_viterbi_combined_xx_2, 0), (self.blks2_error_rate_0_0, 1))
        self.connect((self.trellis_viterbi_combined_xx_2, 0), (self.trellis_encoder_xx_2_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "int_cancellation1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_snr_db(self):
        return self.snr_db

    def set_snr_db(self, snr_db):
        self.snr_db = snr_db
        self.set_noisevar(10**(-self.snr_db/10))

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.trellis_viterbi_combined_xx_2.set_FSM(trellis.fsm(self.prefix+self.fsm2))
        self.trellis_viterbi_combined_xx_1.set_FSM(trellis.fsm(self.prefix+self.fsm1))
        self.trellis_viterbi_combined_xx_0_0.set_FSM(trellis.fsm(self.prefix+self.fsm1))
        self.trellis_viterbi_combined_xx_0.set_FSM(trellis.fsm(self.prefix+self.fsm2))
        self.trellis_encoder_xx_2_0.set_FSM(trellis.fsm(self.prefix+self.fsm2))
        self.trellis_encoder_xx_2.set_FSM(trellis.fsm(self.prefix+self.fsm1))
        self.trellis_encoder_xx_1.set_FSM(trellis.fsm(self.prefix+self.fsm2))
        self.trellis_encoder_xx_0.set_FSM(trellis.fsm(self.prefix+self.fsm1))

    def get_noisevar(self):
        return self.noisevar

    def set_noisevar(self, noisevar):
        self.noisevar = noisevar
        self.analog_noise_source_x_0.set_amplitude(self.noisevar)

    def get_fsm2(self):
        return self.fsm2

    def set_fsm2(self, fsm2):
        self.fsm2 = fsm2
        self.trellis_viterbi_combined_xx_2.set_FSM(trellis.fsm(self.prefix+self.fsm2))
        self.trellis_viterbi_combined_xx_0.set_FSM(trellis.fsm(self.prefix+self.fsm2))
        self.trellis_encoder_xx_2_0.set_FSM(trellis.fsm(self.prefix+self.fsm2))
        self.trellis_encoder_xx_1.set_FSM(trellis.fsm(self.prefix+self.fsm2))

    def get_fsm1(self):
        return self.fsm1

    def set_fsm1(self, fsm1):
        self.fsm1 = fsm1
        self.trellis_viterbi_combined_xx_1.set_FSM(trellis.fsm(self.prefix+self.fsm1))
        self.trellis_viterbi_combined_xx_0_0.set_FSM(trellis.fsm(self.prefix+self.fsm1))
        self.trellis_encoder_xx_2.set_FSM(trellis.fsm(self.prefix+self.fsm1))
        self.trellis_encoder_xx_0.set_FSM(trellis.fsm(self.prefix+self.fsm1))

    def get_block(self):
        return self.block

    def set_block(self, block):
        self.block = block
        self.trellis_viterbi_combined_xx_2.set_K(self.block)
        self.trellis_viterbi_combined_xx_1.set_K(self.block)
        self.trellis_viterbi_combined_xx_0_0.set_K(self.block)
        self.trellis_viterbi_combined_xx_0.set_K(self.block)

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.trellis_viterbi_combined_xx_2.set_TABLE(((1-self.alpha)**0.5*1,(1-self.alpha)**0.5*1j,(1-self.alpha)**0.5*(-1j),(1-self.alpha)**0.5*(-1)))
        self.trellis_viterbi_combined_xx_1.set_TABLE((self.alpha**0.5*1,self.alpha**0.5*1j,self.alpha**0.5*(-1j),self.alpha**0.5*(-1)))
        self.trellis_viterbi_combined_xx_0_0.set_TABLE((self.alpha**0.5*1,self.alpha**0.5*1j,self.alpha**0.5*(-1j),self.alpha**0.5*(-1)))
        self.trellis_viterbi_combined_xx_0.set_TABLE(((1-self.alpha)**0.5*1,(1-self.alpha)**0.5*1j,(1-self.alpha)**0.5*(-1j),(1-self.alpha)**0.5*(-1)))
        self.blocks_multiply_const_vxx_2_0.set_k(((1-self.alpha)**0.5, ))
        self.blocks_multiply_const_vxx_2.set_k((self.alpha**0.5, ))
        self.blocks_multiply_const_vxx_1.set_k(((1-self.alpha)**0.5, ))
        self.blocks_multiply_const_vxx_0.set_k((self.alpha**0.5, ))

    def get_R(self):
        return self.R

    def set_R(self, R):
        self.R = R
        self.blocks_throttle_0.set_sample_rate(self.R)


def main(top_block_cls=int_cancellation1, options=None):

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
