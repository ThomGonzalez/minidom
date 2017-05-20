from xml.dom import minidom


class Field(object):
	def __init__(self, attribute_name):
		self.attribute_name = attribute_name


class XmlReader(object):
	"""
	Clase base de XML.
	"""

	def __init__(self, path=None):
		self.document = minidom.parse(path)

	def get_file(self):
		return self.document

	def get_elements(self, node_xml):
		return self.document.getElementsByTagName(node_xml)

	def get_attributes(self, nodes, fields):
		data = []
		dic = {}
		# Extraer datos del nodo.
		for node in nodes:
			# Recorrer lista de atributos.
			for name in fields:
				atribute = node.getAttribute(name)
				# Actualizar diccionario.
				dic.update({name: atribute})
			# Agregar a la lista los diccionarios.
			data.append(dic)
		return data


class Base(object):

	def get_fields(self):
		fields = []

		for field in self.map_fields:
			name = getattr(field, 'attribute_name')
			fields.append(name)

		return fields


class Comprobante(Base):
	"""
	Nodo de comprobante
	"""
	node_xml = 'cfdi:Comprobante'

	map_fields = (
		Field(attribute_name='version'),
		Field(attribute_name='tipoDeComprobante'),
		Field(attribute_name='fecha'),
		Field(attribute_name='serie'),
		Field(attribute_name='folio'),
		Field(attribute_name='sello'),
		Field(attribute_name='noCertificado'),
		Field(attribute_name='certificado'),
		Field(attribute_name='metodoDePago'),
		Field(attribute_name='fomaDePago'),
		Field(attribute_name='subTotal'),
		Field(attribute_name='descuento'),
		Field(attribute_name='total'),
		Field(attribute_name='TipoCambio'),
		Field(attribute_name='Moneda'),
		Field(attribute_name='LugarExpedicion')
	)

	def __init__(self, document):
		self.document = document
		self.node = self.document.get_elements(self.node_xml)
		self.fields = self.get_fields()

	def data(self):
		_data = self.document.get_attributes(self.node, self.fields)
		return _data



class Percepcion(Base):
	"""docstring for ClassName"""
	node = 'nomina12:Percepcion'

	map_fields = (
		Field(attribute_name='Clave'),
		Field(attribute_name='TipoPercepcion'),
		Field(attribute_name='Concepto'),
		Field(attribute_name='ImporteGravado'),
		Field(attribute_name='ImporteExento'),
	)


class Deduccion(Base):
	"""docstring for ClassName"""
	node = 'nomina12:Deduccion'

	map_fields = (
		Field(attribute_name='Clave'),
		Field(attribute_name='TipoDeduccion'),
		Field(attribute_name='Concepto'),
		Field(attribute_name='Importe'),
	)


class ParseXml(object):

	path = 'CFDI_v12.xml'

	document = XmlReader(path=path)

	comprobante = Comprobante(document=document).data()
	print(comprobante)
