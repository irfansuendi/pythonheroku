"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect, request
from python import app

@app.route("/", methods = ['GET','POST'])
def login():
  error=None
  if request.method =='POST':
    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
      error='user/pass salahhhhh'
    else:
      return redirect('/LaporanSPP')
  return render_template("login.html",
                          title='Yayasan')

##======================= Data Bantu ============================================
@app.route("/DataMurid")
def DataMurid():
  return render_template("DataMurid.html",
                          title='Yayasan')

@app.route("/DataPegawai")
def DataPegawai():
  return render_template("DataPegawai.html",
                          title='Yayasan')

@app.route("/DataSekolah")
def DataSekolah():
  return render_template("DataSekolah.html",
                          title='Yayasan')

@app.route("/DataKelas")
def DataKelas():
  return render_template("DataKelas.html",
                          title='Yayasan')

@app.route("/DataWaliKelas")
def DataWaliKelas():
  return render_template("DataWaliKelas.html",
                          title='Yayasan')

@app.route("/DataTS")
def DataTS():
  return render_template("DataTS.html",
                          title='Yayasan')

@app.route("/DataSPP")
def DataSPP():
  return render_template("DataSPP.html",
                          title='Yayasan')

@app.route("/DataRekening")
def DataRekening():
  return render_template("DataRekening.html",
                          title='Yayasan')
##=======================================================================================

##======================= Input SPP ============================================
@app.route("/InputSPP")
def InputSPP():
  return render_template("InputSPP.html",
                          title='Yayasan')

@app.route("/LaporanSPP")
def LaporanSPP():
  return render_template("LaporanSPP.html",
                          title='Yayasan')
##=======================================================================================

##======================= Input Formulir ============================================
@app.route("/InputDataFormulir")
def InputDataFormulir():
  return render_template("InputDataFormulir.html",
                          title='Yayasan')

@app.route("/LapFormulir")
def LapFormulir():
  return render_template("LapFormulir.html",
                          title='Yayasan')
##=======================================================================================


##======================= Input Data ============================================
@app.route("/InputDataConfirm")
def InputDataConfirm():
  return render_template("InputDataConfirm.html",
                          title='Yayasan')

@app.route("/LapConfirm")
def Lapconfirm():
  return render_template("LapConfirm.html",
                          title='Yayasan')

@app.route("/InputDataPengajuan")
def InputDataPengajuan():
  return render_template("InputDataPengajuan.html",
                          title='Yayasan')

@app.route("/LapPengajuan")
def LapPengajuan():
  return render_template("LapPengajuan.html",
                          title='Yayasan')
##=======================================================================================


##======================= Gak Kepake ============================================
@app.route("/InputDataSekolah")
def InputDataSekolah():
  return render_template("InputDataSekolah.html",
                          title='Yayasan')

@app.route("/InputDataTS")
def InputDataTS():
  return render_template("InputDataTS.html",
                          title='Yayasan')

@app.route("/InputDataPegawai")
def InputDataPegawai():
  return render_template("InputDataPegawai.html",
                          title='Yayasan')

@app.route("/InputDataMurid")
def InputDataMurid():
  return render_template("InputDataMurid.html",
                          title='Yayasan')

@app.route("/InputDataKelas")
def InputDataKelas():
  return render_template("InputDataKelas.html",
                          title='Yayasan')

@app.route("/InputDataSPP")
def InputDataSPP():
  return render_template("InputDataSPP.html",
                          title='Yayasan')

@app.route("/InputDataRekening")
def InputDataRekening():
  return render_template("InputDataRekening.html",
                          title='Yayasan')
