El código mayormente se hace dentro de la función 'topology()'
1. Inicio
Comienza iniciando la net, y configurando la pérdida de señal,
tal como fue solicitado en el enunciado. Se hizo de la
siguiente manera:

	net = Mininet_wifi()
	# Configuracion de la perdida de senal 3.5+ 4/10 = 3.9
	net.setPropagationModel(model="logDistance", exp=3.9)

2. Creación de las AP's
Se crearon las 14 Ap's en la forma solicitada, se hizo de la siguiente
manera:

		ap1 = net.addAccessPoint(
		'ap1',
		ssid='ap1-ssid',
		channel='1',
		position='0,57,0',
		failMode='standalone', stp=True
    )

Notar que el canal se decidió de forma que intentara minimizar la
interferencia entre AP's cercanos, dada la figura resultante.
Además, la ubicación viene dada por la figura pedida, que se graficó en 
geogebra para obtener las coordenadas, como se ve en la figura adjunta.
Finalmente, se añadió la linea 'failMode='standalone', stp=True' para
evitar los problemas que enfrentabamos al momento de hacer ping entre dos
estaciones.

3. Conexión entre AP's
Se definió la conexión entre cada AP y sus dos vecinos. Se hizo de la
siguiente manera:
  net.addLink(ap1, ap2)

4. Creación de las estaciones
Se crearon las estaciones, cumpliendo con las posiciones iniciales
especificadas, para uqe luego pudieran cubrir los recorridos solicitados.
Se hizo de la siguiente manera:
		sta1 = net.addStation(
			'sta1',
			mac='00:00:00:00:00:01',
			position='0,150,0'
    )

5. Movimiento de las estaciones
Se inició el tiempo en cero, y se señaló qué recorrido deería recorrer
cada estación. Por ejemplo, para la estación 2 el recorrido se hizo
de la siguiente manera:
  		net.mobility(
  			sta2,
  			'start',
  			time=1,
  			position='-150,-100,0'
  			)
  		net.mobility(
  			sta2,
  			'stop',
  			time=31,
  			position='100,100,0'
  			)

Así, en un movimiento continupo de 30 segundos, fue desde el cuadrante 
inferior iquierdo hasta el superior derecho donde haya cobertura de algún otro AP

