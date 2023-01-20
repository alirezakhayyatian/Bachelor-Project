#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: gmsk_transmitter
# Author: Alireza khayyatiyan
# Description: AUT:bachelor thesis
# Generated: Fri Jan 20 22:19:50 2023
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
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import math
import numpy as np
import pmt
import sip
import sys
from gnuradio import qtgui


class gmsk_transmitter(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "gmsk_transmitter")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("gmsk_transmitter")
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

        self.settings = Qt.QSettings("GNU Radio", "gmsk_transmitter")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 2
        self.snr_db = snr_db = 10
        self.gaussian_taps = gaussian_taps = filter.firdes.gaussian(1,sps,0.3,4*sps)
        self.taps = taps = np.convolve(np.array(gaussian_taps),np.array((1,)*sps))
        self.sensitivity = sensitivity = np.pi/(2*sps)
        self.samp_rate = samp_rate = 1e6
        self.noisevar = noisevar = 10**(-snr_db/10.0)
        self.gainUSRP = gainUSRP = 35
        self.frf = frf = 2.2e9

        ##################################################
        # Blocks
        ##################################################
        self._snr_db_range = Range(-10, 10, 1, 10, 200)
        self._snr_db_win = RangeWidget(self._snr_db_range, self.set_snr_db, 'SNR (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._snr_db_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
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
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, samp_rate/2/1.42, samp_rate/20/1.42*50/35, firdes.WIN_HAMMING, 6.76))
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(sps, (taps))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_ff(digital.TED_MOD_MUELLER_AND_MULLER, sps, 0.045, 1.0, 1.0, 1.5, 1, digital.constellation_bpsk().base(), digital.IR_MMSE_8TAP, 128, ([]))
        self.digital_chunks_to_symbols_xx_0_0_0 = digital.chunks_to_symbols_bf(([-1,1]), 1)
        self.digital_binary_slicer_fb_1 = digital.binary_slicer_fb()
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
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((.5, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'E:\\webcam\\grc\\bhqethcjrxxw.jpg', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_char*1, 'E:\\webcam\\grc\\image.jpg', False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=sps,
        		bits_per_symbol=1,
        		preamble='',
        		access_code='',
        		pad_for_usrp=True,
        	),
        	payload_length=0,
        )
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code='',
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(1.0/sensitivity)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noisevar, 0)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(sensitivity)
        self.analog_agc3_xx_0 = analog.agc3_cc(1e-3, 1e-4, 1.0, 1.0, 1)
        self.analog_agc3_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc3_xx_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.blks2_packet_encoder_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blks2_packet_encoder_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.channels_fading_model_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_chunks_to_symbols_xx_0_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.channels_cfo_model_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.channels_cfo_model_0_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.channels_fading_model_0, 0), (self.channels_cfo_model_0_0, 0))
        self.connect((self.digital_binary_slicer_fb_1, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.digital_binary_slicer_fb_1, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.analog_frequency_modulator_fc_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_agc3_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "gmsk_transmitter")
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

    def get_gaussian_taps(self):
        return self.gaussian_taps

    def set_gaussian_taps(self, gaussian_taps):
        self.gaussian_taps = gaussian_taps
        self.set_taps(np.convolve(np.array(self.gaussian_taps),np.array((1,)*self.sps)))

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.interp_fir_filter_xxx_0.set_taps((self.taps))

    def get_sensitivity(self):
        return self.sensitivity

    def set_sensitivity(self, sensitivity):
        self.sensitivity = sensitivity
        self.analog_quadrature_demod_cf_0.set_gain(1.0/self.sensitivity)
        self.analog_frequency_modulator_fc_0.set_sensitivity(self.sensitivity)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/2/1.42, self.samp_rate/20/1.42*50/35, firdes.WIN_HAMMING, 6.76))
        self.channels_fading_model_0.set_fDTs(100.0/self.samp_rate)
        self.channels_cfo_model_0_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_noisevar(self):
        return self.noisevar

    def set_noisevar(self, noisevar):
        self.noisevar = noisevar
        self.analog_noise_source_x_0.set_amplitude(self.noisevar)

    def get_gainUSRP(self):
        return self.gainUSRP

    def set_gainUSRP(self, gainUSRP):
        self.gainUSRP = gainUSRP

    def get_frf(self):
        return self.frf

    def set_frf(self, frf):
        self.frf = frf


def main(top_block_cls=gmsk_transmitter, options=None):

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
