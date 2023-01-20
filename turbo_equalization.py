#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Hard/Soft/Turbo Equalization
# Author: AA
# Description: gnuradio flow graph
# Generated: Fri Jan 20 22:21:34 2023
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
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import gnuradio.trellis.fsm_utils as fu
import math
import numpy
import sip
import sys
from gnuradio import qtgui


class turbo_equalization(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Hard/Soft/Turbo Equalization")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Hard/Soft/Turbo Equalization")
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

        self.settings = Qt.QSettings("GNU Radio", "turbo_equalization")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.prefix = prefix = "C:/Program Files/GNURadio-3.7/share/gnuradio/examples/trellis/fsm_files"
        self.modulation = modulation = fu.pam4
        self.fsm_o = fsm_o = trellis.fsm(prefix+"/awgn1o2_4.fsm")
        self.channel = channel = fu.c_channel
        self.tot_mod = tot_mod = fu.make_isi_lookup(modulation,channel,False)
        self.bpsym = bpsym = int(round(math.log(fsm_o.I())/math.log(2)))
        self.block_b = block_b = bpsym*1000
        self.EsN0_dB = EsN0_dB = 15
        self.Es = Es = numpy.mean((numpy.square(numpy.abs(tot_mod[1]))))
        self.noisevar = noisevar = 10**(-EsN0_dB/10.0)  * Es   /2.0
        self.interleaver = interleaver = trellis.interleaver(block_b/bpsym,666)
        self.fsm_i = fsm_i = trellis.fsm(len(modulation[1]),len(channel))
        self.R = R = 100e3

        ##################################################
        # Blocks
        ##################################################
        self.trellis_viterbi_x_0 = trellis.viterbi_b(trellis.fsm(fsm_o), interleaver.K(), 0, -1)
        self.trellis_viterbi_combined_xx_1 = trellis.viterbi_combined_fb(trellis.fsm(fsm_o), interleaver.K(), -1, -1, 1, (0,1,2,3), digital.TRELLIS_HARD_SYMBOL)
        self.trellis_viterbi_combined_xx_0 = trellis.viterbi_combined_fb(trellis.fsm(fsm_i), interleaver.K(), -1, -1, tot_mod[0], (tot_mod[1]), digital.TRELLIS_EUCLIDEAN)
        self.trellis_siso_combined_f_0 = trellis.siso_combined_f(trellis.fsm(fsm_i), interleaver.K(), -1, -1, True, False, trellis.TRELLIS_MIN_SUM, tot_mod[0], (tot_mod[1]), trellis.TRELLIS_EUCLIDEAN)
        self.trellis_sccc_decoder_combined_xx_0 = trellis.sccc_decoder_combined_fb(
            trellis.fsm(fsm_o), -1, -1,
            trellis.fsm(fsm_i), -1, -1,
            trellis.interleaver(interleaver),
            interleaver.K(),
            5,
                        trellis.TRELLIS_MIN_SUM,
            tot_mod[0], (tot_mod[1]), digital.TRELLIS_EUCLIDEAN,
            1.0)

        self.trellis_permutation_0_0_0 = trellis.permutation(interleaver.K(), (interleaver.DEINTER()), fsm_o.O(), gr.sizeof_float*1)
        self.trellis_permutation_0_0 = trellis.permutation(interleaver.K(), (interleaver.DEINTER()), 1, gr.sizeof_char*1)
        self.trellis_permutation_0 = trellis.permutation(interleaver.K(), (interleaver.INTER()), 1, gr.sizeof_char*1)
        self.trellis_encoder_xx_0 =  trellis.encoder_bb(trellis.fsm(fsm_o), 0, 0) if False else trellis.encoder_bb(trellis.fsm(fsm_o), 0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	R, #samp_rate
        	"", #name
        	2 #number of inputs
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

        labels = ['Before Channel', 'After Channel', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [0, 0, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_number_sink_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0.set_title("BER (Turbo)")

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
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_win)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("BER (Soft)")

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
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("BER (Hard)")

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
        self.fir_filter_xxx_0 = filter.fir_filter_fff(1, (fu.c_channel))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bf((modulation[1]), modulation[0])
        self.blocks_unpack_k_bits_bb_0_0_0 = blocks.unpack_k_bits_bb(bpsym)
        self.blocks_unpack_k_bits_bb_0_0 = blocks.unpack_k_bits_bb(bpsym)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(bpsym)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, R,True)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(bpsym)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blks2_error_rate_0_0_0_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=block_b*100,
        	bits_per_symbol=1,
        )
        self.blks2_error_rate_0_0_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=block_b*100,
        	bits_per_symbol=1,
        )
        self.blks2_error_rate_0_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=block_b*100,
        	bits_per_symbol=1,
        )
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, 1007)), True)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noisevar**0.5, -42)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self._EsN0_dB_range = Range(-10, 20, 1, 15, 200)
        self._EsN0_dB_win = RangeWidget(self._EsN0_dB_range, self.set_EsN0_dB, 'Es/N0 (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._EsN0_dB_win)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.trellis_siso_combined_f_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.blks2_error_rate_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blks2_error_rate_0_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blks2_error_rate_0_0_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blks2_error_rate_0_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blks2_error_rate_0_0_0, 0), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.blks2_error_rate_0_0_0_0, 0), (self.qtgui_number_sink_0_0_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_add_xx_1, 0), (self.trellis_sccc_decoder_combined_xx_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.trellis_siso_combined_f_0, 1))
        self.connect((self.blocks_add_xx_1, 0), (self.trellis_viterbi_combined_xx_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.trellis_viterbi_combined_xx_1, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.trellis_encoder_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blks2_error_rate_0_0, 1))
        self.connect((self.blocks_unpack_k_bits_bb_0_0, 0), (self.blks2_error_rate_0_0_0, 1))
        self.connect((self.blocks_unpack_k_bits_bb_0_0_0, 0), (self.blks2_error_rate_0_0_0_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.trellis_encoder_xx_0, 0), (self.trellis_permutation_0, 0))
        self.connect((self.trellis_permutation_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.trellis_permutation_0_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.trellis_permutation_0_0_0, 0), (self.trellis_viterbi_x_0, 0))
        self.connect((self.trellis_sccc_decoder_combined_xx_0, 0), (self.blocks_unpack_k_bits_bb_0_0_0, 0))
        self.connect((self.trellis_siso_combined_f_0, 0), (self.trellis_permutation_0_0_0, 0))
        self.connect((self.trellis_viterbi_combined_xx_0, 0), (self.trellis_permutation_0_0, 0))
        self.connect((self.trellis_viterbi_combined_xx_1, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.trellis_viterbi_x_0, 0), (self.blocks_unpack_k_bits_bb_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "turbo_equalization")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.set_fsm_o(trellis.fsm(self.prefix+"/awgn1o2_4.fsm"))

    def get_modulation(self):
        return self.modulation

    def set_modulation(self, modulation):
        self.modulation = modulation
        self.set_tot_mod(fu.make_isi_lookup(self.modulation,self.channel,False))
        self.set_fsm_i(trellis.fsm(len(self.modulation[1]),len(self.channel)))
        self.digital_chunks_to_symbols_xx_0_0.set_symbol_table((self.modulation[1]))

    def get_fsm_o(self):
        return self.fsm_o

    def set_fsm_o(self, fsm_o):
        self.fsm_o = fsm_o
        self.trellis_viterbi_x_0.set_FSM(trellis.fsm(self.fsm_o))
        self.trellis_viterbi_combined_xx_1.set_FSM(trellis.fsm(self.fsm_o))
        self.trellis_encoder_xx_0.set_FSM(trellis.fsm(self.fsm_o))

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel
        self.set_tot_mod(fu.make_isi_lookup(self.modulation,self.channel,False))
        self.set_fsm_i(trellis.fsm(len(self.modulation[1]),len(self.channel)))

    def get_tot_mod(self):
        return self.tot_mod

    def set_tot_mod(self, tot_mod):
        self.tot_mod = tot_mod
        self.trellis_viterbi_combined_xx_0.set_D(self.tot_mod[0])
        self.trellis_viterbi_combined_xx_0.set_TABLE((self.tot_mod[1]))
        self.trellis_siso_combined_f_0.set_D(self.tot_mod[0])
        self.trellis_siso_combined_f_0.set_TABLE((self.tot_mod[1]))
        self.set_Es(numpy.mean((numpy.square(numpy.abs(self.tot_mod[1])))))

    def get_bpsym(self):
        return self.bpsym

    def set_bpsym(self, bpsym):
        self.bpsym = bpsym
        self.set_interleaver(trellis.interleaver(self.block_b/self.bpsym,666))
        self.set_block_b(self.bpsym*1000)

    def get_block_b(self):
        return self.block_b

    def set_block_b(self, block_b):
        self.block_b = block_b
        self.set_interleaver(trellis.interleaver(self.block_b/self.bpsym,666))

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

    def get_noisevar(self):
        return self.noisevar

    def set_noisevar(self, noisevar):
        self.noisevar = noisevar
        self.analog_noise_source_x_0.set_amplitude(self.noisevar**0.5)

    def get_interleaver(self):
        return self.interleaver

    def set_interleaver(self, interleaver):
        self.interleaver = interleaver

    def get_fsm_i(self):
        return self.fsm_i

    def set_fsm_i(self, fsm_i):
        self.fsm_i = fsm_i
        self.trellis_viterbi_combined_xx_0.set_FSM(trellis.fsm(self.fsm_i))
        self.trellis_siso_combined_f_0.set_FSM(trellis.fsm(self.fsm_i))

    def get_R(self):
        return self.R

    def set_R(self, R):
        self.R = R
        self.qtgui_time_sink_x_0.set_samp_rate(self.R)
        self.blocks_throttle_0.set_sample_rate(self.R)


def main(top_block_cls=turbo_equalization, options=None):

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
