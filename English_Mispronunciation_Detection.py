# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import aiml
from espnet2.bin.asr_inference import Speech2Text
from espnet_model_zoo.downloader import ModelDownloader
import soundfile
import Levenshtein
import pyaudio
import wave

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("alice/startup.xml")
kernel.respond("load alice")
lista = []
flag = False

def botToActivePronunciation(frase):
    respuesta = kernel.respond(frase)
    print(kernel.respond(frase))
    return respuesta

def bot(frase):
    print(flag)
    error = []
    #frase = input("Escriba su mensaje >> ")
    if flag == False:
        respuesta = kernel.respond(frase)
        print(kernel.respond(frase))
    elif flag == True:
        respuesta = kernel.respond(frase)
        Grabar_voz()
        inferencia = Inferencia()
        distancia = Distancia(frase, inferencia)

        if len(distancia) > 0:
            error = ErrorPronunciacion(distancia, frase)
            print("Mispronunciation detected in words: " )
            for i in range(len(error)):
                print(error[i]," ")
        else:
            print(kernel.respond(frase))


    res = [respuesta, error]

    return res

def Grabar_voz():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "example.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def Inferencia():
	speech2text = Speech2Text("exp/asr_train_asr_transformer_raw_bpe/config.yaml", "exp/asr_train_asr_transformer_raw_bpe/100epoch.pth")
	audio, rate = soundfile.read("example.wav")
	nbests = speech2text(audio)
	text, *_ = nbests[0]
	#print(text)
	text = text.replace("'"," ")
	return text

def Distancia(s1, s2):
	print("Esta es la frase: ",s1, "\n", "Esta es la inferencia: ",s2)
	#print("\n\n")
	#print(Levenshtein.editops(s1, s2))

	distancia = Levenshtein.editops(s1, s2)

	return distancia

def ErrorPronunciacion(distancia, frase):
	tam_MovimientosLev = len(distancia)
	tam_frase = len(frase)

	x = frase.split(" ")
	tam_palabras = len(x)

	errores = []
	palabra_idx = []
	cont = 0

	for i in range(tam_palabras):
		letras = []

		for j in range(len(x[i])):
			letras.append(cont)
			letras.append(x[i][j])
			cont+=1

		palabra_idx.append(letras)
		cont+=1

	if tam_MovimientosLev != 0:
		for j in range(tam_MovimientosLev):
			idx = distancia[j][1]

			for k in range(len(palabra_idx)):
				if idx in palabra_idx[k]:
					errores.append(x[k])
	errores = list(dict.fromkeys(errores))

	return errores

def Historial(mensaje, respuesta):

    lista.append('\n')
    lista.append('Your Message: ' + mensaje)
    lista.append('\n')
    lista.append('Response: ' + respuesta)
    lista.append('\n')

    str = " "

    return (str.join(lista))

def Formato(error):
    errores = []

    for i in range(len(error)):
        errores.append(error[i])
        errores.append('\n')

    str = " "

    return (str.join(errores))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(616, 603)

        self.startPracticeButton = QtWidgets.QPushButton(Form)
        self.startPracticeButton.setGeometry(QtCore.QRect(20, 50, 211, 41))
        self.startPracticeButton.setObjectName("startPracticeButton")
        self.startPracticeButton.clicked.connect(self.startPractice)
        self.stopPracticeButton = QtWidgets.QPushButton(Form)
        self.stopPracticeButton.setGeometry(QtCore.QRect(20, 100, 211, 41))
        self.stopPracticeButton.setObjectName("stopPracticeButton")
        self.stopPracticeButton.clicked.connect(self.stopPractice)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(370, 10, 141, 31))
        self.label.setObjectName("label")

        self.labelStatus = QtWidgets.QLabel(Form)
        self.labelStatus.setGeometry(QtCore.QRect(20, 150, 211, 41))
        self.labelStatus.setObjectName("labelStatus")
        self.practiceStatus = QtWidgets.QLabel(Form)
        self.practiceStatus.setGeometry(QtCore.QRect(80, 150, 211, 41))
        self.practiceStatus.setObjectName("practiceStatus")

        self.labelMicroStatus = QtWidgets.QLabel(Form)
        self.labelMicroStatus.setGeometry(QtCore.QRect(20, 170, 211, 41))
        self.labelMicroStatus.setObjectName("labelMicroStatus")
        self.microStatus = QtWidgets.QLabel(Form)
        self.microStatus.setGeometry(QtCore.QRect(100, 170, 211, 41))
        self.microStatus.setObjectName("microStatus")


        self.mispronouncedWords = QtWidgets.QTextBrowser(Form)
        self.mispronouncedWords.setGeometry(QtCore.QRect(270, 50, 311, 171))
        self.mispronouncedWords.setObjectName("textEdit")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 240, 141, 31))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 240, 291, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")


        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 240, 89, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.getText)



        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(35, 291, 541, 291))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.startPracticeButton.setText(_translate("Form", "Sart Practice Pronunciation"))
        self.stopPracticeButton.setText(_translate("Form", "Stop Practice Pronunciation"))
        self.label.setText(_translate("Form", "Mispronunciations:"))
        self.labelStatus.setText(_translate("Form", "Status:"))
        self.practiceStatus.setText(_translate("Form", "Deactivated"))
        self.labelMicroStatus.setText(_translate("From", "Microphone:"))
        self.microStatus.setText(_translate("From", "-"))
        self.pushButton_3.setText(_translate("Form", "Send"))
        self.label_2.setText(_translate("Form", "Enter Your Message:"))

    def getText(self):
        text = self.plainTextEdit.toPlainText()
        respuesta = bot(text)
        historial = Historial(text, respuesta[0])
        forrmatoError = Formato(respuesta[1])

        self.textBrowser.setText( historial )
        self.mispronouncedWords.setText( forrmatoError )

    def startPractice(self):
        global flag
        code = "MARK123"
        response = botToActivePronunciation(code)
        if response == 'recordig':
            self.practiceStatus.setText( "Activated" )
            print("start practice")
            flag = True

    def stopPractice(self):
        global flag
        code = "MARK123"
        response = botToActivePronunciation(code)
        if response == 'recordig':
            self.practiceStatus.setText( "Dectivated" )
            print("stop practice")
            flag = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)


    Form.show()
    sys.exit(app.exec_())
