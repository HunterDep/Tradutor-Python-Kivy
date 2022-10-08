"""
Criado Por Hunter Dep

YouTube: https://youtube.com/channel/UCyo1KzxCt9iJybQPFXmMOPg

GitHub: https://github.com/HunterDep
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from googletrans import Translator

langs = {
	"Português": "pt",
	"Inglês": "en"
}

Código = """
Tradução:
	size_hint_y: .5
	
	BoxLayout:
		id: título1
		Label:
			text: 'TradutorKivy'
			
	BoxLayout:
		id: título2
		size_hint_y: .5
		padding : 50
		Label:
			text: 'Coloque o Texto'
	
	BoxLayout:
		id: box_texto
		size_hint_y: .5
		padding : 50
		TextInput:
			id: texto
			
	BoxLayout:
		id: box_lang
		size_hint_y: .5
		padding: 100
		Button:
			id: lang
			text: 'Português'
			on_press: root.MudarLang()
			
	BoxLayout:
		id: traduzir
		size_hint_y: .5
		padding: 100
		Button:
			text: 'Traduzir'
			on_press: root.Função()
			
	BoxLayout:
		id: box_resultado
		size_hint_y: .5
		padding: 50
		TextInput:
			id: resultado
			text: ''
			
	BoxLayout:
		id: trocar
		size_hint_y: .5
		padding: 115
		Button:
			text: 'Trocar'
			on_press: root.Trocar()
"""

class Tradução(FloatLayout):
	def MudarLang(self):
		if self.ids.lang.text in "Português":
			self.ids.lang.text = "Inglês"
		elif self.ids.lang.text in "Inglês":
			self.ids.lang.text = "Português"
			
	def Função(self):
		texto = self.ids.texto.text
		tradutor = Translator()
		tradução = tradutor.translate(texto, dest=langs[self.ids.lang.text])
		self.ids.resultado.text = f"{tradução.text}"
		
	def Trocar(self):
		tradutor = Translator()
		txt1 = self.ids.texto.text
		txt2 = self.ids.resultado.text
		
		self.ids.texto.text = txt2
		self.ids.resultado.text = txt1

class TradutorPython(App):
	def build(self):
		return Builder.load_string(Código)
	def on_start(self):
		self.root.ids.título1.y = 950
		self.root.ids.título2.y = 940
		self.root.ids.box_texto.y = 770
		self.root.ids.box_lang.y = 555
		self.root.ids.traduzir.y = 390
		self.root.ids.box_resultado.y = 170
		self.root.ids.trocar.y = -50
		
TradutorPython().run()
