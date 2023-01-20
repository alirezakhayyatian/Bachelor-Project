#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: transmiter
# Author: Alireza Khayyatiyan
# Description: AUT: bachelor thesis
# Generated: Fri Jan 20 21:56:35 2023
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
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import trellis
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import numpy as np
import pmt
import sip
import sys
from gnuradio import qtgui


class tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "transmiter")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("transmiter")
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

        self.settings = Qt.QSettings("GNU Radio", "tx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 2
        self.snr_db = snr_db = 6.8
        self.prefix = prefix = "C:/Program Files/GNURadio-3.7/share/gnuradio/examples/trellis/fsm_files"
        self.gaussian_taps = gaussian_taps = filter.firdes.gaussian(1,sps,0.3,4*sps)
        self.block = block = 1000
        self.taps = taps = np.convolve(np.array(gaussian_taps),np.array((1,)*sps))
        self.sensitivity = sensitivity = np.pi/(2*sps)
        self.samp_rate = samp_rate = 1e6
        self.noisevar = noisevar = 10**(-snr_db/10.0)
        self.interleaver = interleaver = trellis.interleaver(block,666)
        self.fsm_o = fsm_o = trellis.fsm(prefix+"/awgn1o2_4.fsm")
        self.fsm_i = fsm_i = trellis.fsm(prefix+"/awgn2o3_4.fsm")

        ##################################################
        # Blocks
        ##################################################
        self.fcc = Qt.QTabWidget()
        self.fcc_widget_0 = Qt.QWidget()
        self.fcc_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.fcc_widget_0)
        self.fcc_grid_layout_0 = Qt.QGridLayout()
        self.fcc_layout_0.addLayout(self.fcc_grid_layout_0)
        self.fcc.addTab(self.fcc_widget_0, 'Tab 0')
        self.fcc_widget_1 = Qt.QWidget()
        self.fcc_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.fcc_widget_1)
        self.fcc_grid_layout_1 = Qt.QGridLayout()
        self.fcc_layout_1.addLayout(self.fcc_grid_layout_1)
        self.fcc.addTab(self.fcc_widget_1, 'power4')
        self.top_grid_layout.addWidget(self.fcc)
        self.trellis_sccc_encoder_xx_0 = trellis.sccc_encoder_bb(trellis.fsm(fsm_o), 0, trellis.fsm(fsm_i), 0, trellis.interleaver(trellis.interleaver(block,666)), block)
        self._snr_db_range = Range(-10, 10, 1, 6.8, 200)
        self._snr_db_win = RangeWidget(self._snr_db_range, self.set_snr_db, 'SNR (dB)', "counter_slider", float)
        self.fcc_grid_layout_0.addWidget(self._snr_db_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.fcc_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.fcc_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(0.2)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.fcc_grid_layout_1.addWidget(self._qtgui_freq_sink_x_1_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.fcc_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.fcc_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_00 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_00.set_update_time(0.10)
        self.qtgui_freq_sink_x_00.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_00.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_00.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_00.enable_autoscale(False)
        self.qtgui_freq_sink_x_00.enable_grid(False)
        self.qtgui_freq_sink_x_00.set_fft_average(0.2)
        self.qtgui_freq_sink_x_00.enable_axis_labels(True)
        self.qtgui_freq_sink_x_00.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_00.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_00.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_00.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_00.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_00.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_00.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_00.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_00_win = sip.wrapinstance(self.qtgui_freq_sink_x_00.pyqwidget(), Qt.QWidget)
        self.fcc_grid_layout_0.addWidget(self._qtgui_freq_sink_x_00_win, 2, 1, 4, 1)
        for r in range(2, 6):
            self.fcc_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.fcc_grid_layout_0.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(sps, (taps))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_chunks_to_symbols_xx_0_0_0 = digital.chunks_to_symbols_bf(([-1,-1,-1,   -1,-1,1,    -1,1,-1,   -1,1,1,  1,-1,-1,   1,-1,1,  1,1,-1,  1,1,1  ]), 3)
        self.channels_fading_model_0 = channels.fading_model( 8, 100.0/samp_rate, True, 12, 0 )
        self.channels_cfo_model_0_0 = channels.cfo_model(
                samp_rate,
                0.01,
                1e3,
                0
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'E:\\webcam\\grc\\book.jpg', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, 'E:\\webcam\\grc\\recorder.bin', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=2,
        		bits_per_symbol=1,
        		preamble='',
        		access_code='',
        		pad_for_usrp=True,
        	),
        	payload_length=0,
        )
        self.analog_noise_source_x_1 = analog.noise_source_c(analog.GR_GAUSSIAN, noisevar, 0)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(sensitivity)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_noise_source_x_1, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blks2_packet_encoder_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.channels_cfo_model_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blks2_packet_encoder_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.trellis_sccc_encoder_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.channels_cfo_model_0_0, 0), (self.channels_fading_model_0, 0))
        self.connect((self.channels_fading_model_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.channels_fading_model_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.channels_fading_model_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.channels_fading_model_0, 0), (self.blocks_multiply_xx_0, 2))
        self.connect((self.channels_fading_model_0, 0), (self.blocks_multiply_xx_0, 3))
        self.connect((self.channels_fading_model_0, 0), (self.qtgui_freq_sink_x_00, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.analog_frequency_modulator_fc_0, 0))
        self.connect((self.trellis_sccc_encoder_xx_0, 0), (self.digital_chunks_to_symbols_xx_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_taps(np.convolve(np.array(self.gaussian_taps),np.array((1,)*self.sps)))
        self.set_sensitivity(np.pi/(2*self.sps))
        self.set_gaussian_taps(filter.firdes.gaussian(1,self.sps,0.3,4*self.sps))

    def get_snr_db(self):
        return self.snr_db

    def set_snr_db(self, snr_db):
        self.snr_db = snr_db
        self.set_noisevar(10**(-self.snr_db/10.0))

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.set_fsm_o(trellis.fsm(self.prefix+"/awgn1o2_4.fsm"))
        self.set_fsm_i(trellis.fsm(self.prefix+"/awgn2o3_4.fsm"))

    def get_gaussian_taps(self):
        return self.gaussian_taps

    def set_gaussian_taps(self, gaussian_taps):
        self.gaussian_taps = gaussian_taps
        self.set_taps(np.convolve(np.array(self.gaussian_taps),np.array((1,)*self.sps)))

    def get_block(self):
        return self.block

    def set_block(self, block):
        self.block = block
        self.set_interleaver(trellis.interleaver(self.block,666))

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.interp_fir_filter_xxx_0.set_taps((self.taps))

    def get_sensitivity(self):
        return self.sensitivity

    def set_sensitivity(self, sensitivity):
        self.sensitivity = sensitivity
        self.analog_frequency_modulator_fc_0.set_sensitivity(self.sensitivity)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_00.set_frequency_range(0, self.samp_rate)
        self.channels_fading_model_0.set_fDTs(100.0/self.samp_rate)
        self.channels_cfo_model_0_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_noisevar(self):
        return self.noisevar

    def set_noisevar(self, noisevar):
        self.noisevar = noisevar
        self.analog_noise_source_x_1.set_amplitude(self.noisevar)

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


def main(top_block_cls=tx, options=None):

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
