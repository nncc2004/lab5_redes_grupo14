import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology():
	net = Mininet_wifi()

	# Configuracion de la perdida de senal 3.5+ 4/10 = 3.9
	net.setPropagationModel(model="logDistance", exp=3.9)

	# Creacion de las AP's
	if True:	
		'''
		Las posiciones como se muetran en el diagrama
		Los canales los puse asi porque intenta manener al menos 
		4 canales de distancia con el AP mas cercano para evitar
		interferencias
		REvisar README para el detalle
		'''
		info("*** Creando los AP's\n")
		
		ap1 = net.addAccessPoint(
		'ap1',
		ssid='ap1-ssid',
		channel='1',
		position='0,57,0'
		)

		ap2 = net.addAccessPoint(
		'ap2',
		ssid='ap2-ssid',
		channel='6',
		position='44.55,35.53,0'
		)

		ap3 = net.addAccessPoint(
		'ap3',
		ssid='ap3-ssid',
		channel='11',
		position='55.57,-12.68,0'
		)

		ap4 = net.addAccessPoint(
		'ap4',
		ssid='ap4-ssid',
		channel='1',
		position='24.73,-51.36,0'
		)

		ap5 = net.addAccessPoint(
		'ap5',
		ssid='ap5-ssid',
		channel='11',
		position='-24.73,-51.36,0'
		)

		ap6 = net.addAccessPoint(
		'ap6',
		ssid='ap6-ssid',
		channel='1',
		position='-55.57,-12.68,0'
		)

		ap7 = net.addAccessPoint(
		'ap7',
		ssid='ap7-ssid',
		channel='6',
		position='-44.55,35.53,0'
		)

		ap8 = net.addAccessPoint(
		'ap8',
		ssid='ap8-ssid',
		channel='6',
		position='0,114,0'
		)

		ap9 = net.addAccessPoint(
		'ap9',
		ssid='ap9-ssid',
		channel='10',
		position='89.10,71.06,0'
		)

		ap10 = net.addAccessPoint(
		'ap10',
		ssid='ap10-ssid',
		channel='4',
		position='111.14,-25.36,0'
		)

		ap11 = net.addAccessPoint(
		'ap11',
		ssid='ap11-ssid',
		channel='6',
		position='49.46,-102.72,0'
		)

		ap12 = net.addAccessPoint(
		'ap12',
		ssid='ap12-ssid',
		channel='3',
		position='-49.46,-102.72,0'
		)

		ap13 = net.addAccessPoint(
		'ap13',
		ssid='ap13-ssid',
		channel='9',
		position='-111.14,-25.36,0'
		)

		ap14 = net.addAccessPoint(
		'ap14',
		ssid='ap14-ssid',
		channel='11',
		position='-89.10,71.06,0'
		)
		
		aps = [
			ap1, ap2, ap3, ap4, ap5, ap6, ap7,
			ap8, ap9, ap10, ap11, ap12, ap13, ap14
		]
		c1 = net.addController('c1')
		net.configureNodes()

	
	#Conexion entre AP's
	if True:
		info("*** Crando enlaces en anillo interno\n")
		net.addLink(ap1, ap2)
		net.addLink(ap2, ap3)
		net.addLink(ap3, ap4)
		net.addLink(ap4, ap5)
		net.addLink(ap5, ap6)
		net.addLink(ap6, ap7)
		net.addLink(ap7	, ap1)
		info("*** Creando enlaces con AP's externos\n")
		net.addLink(ap1, ap8)
		net.addLink(ap2, ap9)
		net.addLink(ap3, ap10)
		net.addLink(ap4, ap11)
		net.addLink(ap5, ap12)
		net.addLink(ap6, ap13)
		net.addLink(ap7, ap14)
		
		
	#Creacion de las estaciones en sus posiciones iniciales
	if True:
		info("*** Creando y posicionando las 5 estaciones\n")
		
		#estacion1: solo cobertura por AP8
		sta1 = net.addStation(
			'sta1',
			mac='00:00:00:00:00:01',
			position='0,150,0'
		)
		
		#estacion2: cuadrante inferior izquierdo, fuera de cobertura
		sta2 = net.addStation(
			'sta2',
			mac='00:00:00:00:00:02',
			position='-150,-100,0'
		)
		#estacion3: cobertura por uno de los AP del anillo itnerior, por el lado derecho de la topologia
		sta3 = net.addStation(
			'sta3',
			mac='00:00:00:00:00:03',
			position='60,30,0'
		)
		#estacion4: En el origen del plano
		sta4 = net.addStation(
			'sta4',
			mac='00:00:00:00:00:04',
			position='0,0,0'
		)
		#estacion5: zona con maximo solapamiento
		sta5 = net.addStation(
			'sta5',
			mac='00:00:00:00:00:05',
			position='0,-10,0'
		)
		
	if True:

		info("*** Graficando topologia\n")
		net.plotGraph(
		min_x=-200,
		min_y=-200,
		max_x=200,
		max_y=200
		)
		
		net.build()
		c1.start()

		for ap in aps:
			ap.start([c1])

		CLI(net)
		net.stop()



if __name__ == '__main__':
	setLogLevel('info')
	topology()
