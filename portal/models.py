# from django.db import models
# from django.contrib.auth.models import User

# provincias = (
# 	("Buenos_Aires", "Buenos Aires"),
# 	("Catamarca", "Catamarca"),
# 	("Chaco", "Chaco"),
# 	("Chubut", "Chubut"),
# 	("Cordoba", "Cordoba"),
# 	("Corrientes", "Corrientes"),
# 	("Entre_Rios", "Entre Rios"),
# 	("Formosa", "Formosa"),
# 	("Jujuy", "Jujuy"),
# 	("La_Pampa", "La Pampa"),
# 	("La_Rioja", "La Rioja"),
# 	("Mendoza", "Mendoza"),
# 	("Misiones", "Misiones"),
# 	("Neuquen", "Neuquen"),
# 	("Rio_Negro", "Rio Negro"),
# 	("Salta", "Salta"),
# 	("San_Juan", "San Juan"),
# 	("San_Luis", "San Luis"),
# 	("Santa_Cruz", "Santa Cruz"),
# 	("Santa_Fe", "Santa Fe"),
# 	("Santiago_del_Estero", "Santiago_del_Estero"),
# 	("Tierra_del_Fuego", "Tierra del Fuego"),
# 	("Tucuman", "Tucuman"),
# )

# class Provincias(models.Model):
# 	nombre = models.CharField(max_length=30, choices=provincias)

# 	def __unicode__(self):
# 		return self.nombre

# 	class Meta:
# 		verbose_name_plural = "Provincias"

# class Localidades(models.Model):
# 	nombre = models.CharField(max_length=30)
# 	idProvincia = models.ForeignKey(Provincias)

# 	def __unicode__(self):
# 		return self.nombre

# 	class Meta:
# 		verbose_name_plural = "Localidades"

# class EncuestasUtilidadPortal(models.Model):
# 	valoracion = models.IntegerField()
# 	fecha_hora = models.DateTimeField()
# 	comentarios = models.TextField()

# 	def __unicode__(self):
# 		return "%s".format(self.id)

# class Perfiles(models.Model):
# 	nombre = models.CharField(max_length=50)
# 	apellido = models.CharField(max_length=50)
# 	direccion = models.CharField(max_length=50)
# 	imagen = models.ImageField(upload_to="imagen/perfiles/")
# 	idUsuario = models.ForeignKey(User)
# 	idLocalidad = models.ForeignKey(Localidades)

# 	def __unicode__(self):
# 		return "%s - %s".format(self.nombre, self.apellido)

# 	class Meta:
# 		verbose_name_plural = "Perfiles"

# class TipoTelefono(models.Model):
# 	tipo = models.CharField(max_length=30)

# 	def __unicode__(self):
# 		return self.tipo

# 	class Meta:
# 		verbose_name_plural = "Tipo Telefono"

# class EmpresaTelefonica(models.Model):
# 	nombre = models.CharField(max_length=40)

# 	def __unicode__(self):
# 		return self.nombre

# 	class Meta:
# 		verbose_name_plural = "Empresa Telefonica"

# class Telefonos(models.Model):
# 	numero = models.CharField(max_length=20)
# 	idEmpresa = models.ForeignKey(EmpresaTelefonica)
# 	idTipo = models.ForeignKey(TipoTelefono)

# 	def __unicode__(self):
# 		return self.numero

# 	class Meta:
# 		verbose_name_plural = "Telefonos"

# class TelefonosPerfiles(models.Model):
# 	idPerfil = models.ForeignKey(Perfiles)
# 	idTelefono = models.ForeignKey(Telefonos)

# 	def __unicode__(self):
# 		return "%s - %s".format(self.idPerfil, self.idTelefono)

# 	class Meta:
# 		verbose_name_plural = "Telefonos Perfiles"

# class PlanesSociales(models.Model):
# 	nombre = models.CharField(max_length=50)

# 	def __unicode__(self):
# 		return self.nombre

# 	class Meta:
# 		verbose_name_plural = "Planes Sociales"

# class Vehiculos(models.Model):
# 	nombre = models.CharField(max_length=50)

# 	def __unicode__(self):
# 		return self.nombre

# 	class Meta:
# 		verbose_name_plural = "Vehiculos"

# class SituacionLaboral(models.Model):
# 	situacion = models.CharField(max_length=50)

# 	def __unicode__(self):
# 		return self.situacionDiscapacidades

# 	class Meta:
# 		verbose_name_plural = "Situacion Laboral"

# class TipoCarnet(models.Model):
# 	tipo = models.CharField(max_length=30)

# 	def __unicode__(self):
# 		return self.tipo

# 	class Meta:
# 		verbose_name_plural = "Tipo Carnet"

# class ObrasSociales(models.Model):
# 	numero_afiliado = models.IntegerField()
# 	nombre = models.CharField(max_length=30)


# class SubTipos(models.Model):
# 	nombre = models.CharField(max_length=30)

# class Pensiones(models.Model):
# 	nombre = models.CharField(max_length=30)

# class ComoAdquirio(models.Model):
# 	forma = models.CharField(max_length=30)

# class EntesEmisoresCertificados(models.Model):
# 	nombre = models.CharField(max_length=30)

# class TipoDiscapacidad(models.Model):
# 	nombre = models.CharField(max_length=30)
# 	idSubTipo = models.ForeignKey(SubTipos)
# 	idComoAdquirio = models.ForeignKey(ComoAdquirio)
# 	idPension = models.ForeignKey(Pensiones)
# 	idEntes = models.ForeignKey(EntesEmisoresCertificados)

# class Discapacidades(models.Model):
# 	nombre = models.CharField(max_length=30)
# 	dificultades_descripcion = models.CharField(max_length=30, null=True, blank=True)
# 	dificulad_para_trabajar = models.BooleanField()
# 	tiene_pase_libre = models.BooleanField()
# 	idTipoDiscapacidad = models.ForeignKey(TipoDiscapacidad)

# class Curriculums(models.Model):
# 	nombres = models.CharField(max_length=30)
# 	apellidos = models.CharField(max_length=30)
# 	fecha_nac = models.DateField()
# 	domicilio = models.CharField(max_length=50)
# 	email = models.EmailField()
# 	dni = models.IntegerField()
# 	hijos = models.IntegerField()
# 	disp_viajar = models.BooleanField()
# 	disp_reubicacion = models.BooleanField()
# 	carnet = models.BooleanField()
# 	inscripto_AFIP = models.BooleanField()
# 	cod_postal = models.IntegerField()
# 	cuit_cuil = models.CharField(max_length=13)
# 	concubinato = models.BooleanField()
# 	cuerpo = models.TextField()
# 	foto = models.ImageField(upload_to="imagen/cv/")
# 	idUsuario = models.ForeignKey(User)
# 	idLocalidad = models.ForeignKey(Localidades)
# 	idPlanSoc = models.ForeignKey(PlanesSociales)
# 	idVehiculo = models.ForeignKey(Vehiculos)
# 	idSituacion = models.ForeignKey(SituacionLaboral)
# 	poseeEstudios = models.BooleanField()
# 	discapacidad = models.BooleanField()
# 	idObraSocial = models.ForeignKey(ObraSocial)
# 	idDiscapacidad = models.ForeignKey(Discapacidades, null=True, blank=True)

# 	def __unicode__(self):
# 		return "%s - %s".format(self.nombres, self.apellidos)

# 	class Meta:
# 		verbose_name_plural = "Curriculums"

# class Niveles(models.Model):
# 	nombre = models.CharField(max_length=30)

# class AreasEstudios(models.Model):
# 	nombre = models.CharField(max_length=30)

# class Titulos(models.Model):
# 	nombre = models.CharField(max_length=30)

# class CategoriasProgramas(models.Model):
# 	nombre = models.CharField(max_length=30)

# class ConocimientosPc(models.Model):
# 	nombre = models.CharField(max_length=30)
# 	idCategoria = models.ForeignKey(CategoriasProgramas)

# class Situaciones(models.Model):
# 	nombre = models.CharField(max_length=30)

# class AreasEstudiosCursos(models.Model):
# 	nombre = models.CharField(max_length=30)

# class CursosRealizados(models.Model):
# 	nombre = models.CharField(max_length=30)
# 	institucion = models.CharField(max_length=50)
# 	fecha_fin = models.DateField()
# 	idAreaEstudio = models.ForeignKey(AreasEstudiosCursos)

# class Estudios(models.Model):
# 	institucion = models.CharField(max_length=30)
# 	idNivel = models.ForeignKey(Niveles)
# 	idAreaEstudio = models.ForeignKey(AreasEstudios)
# 	idCurriculum = models.ForeignKey(Curriculums)
# 	idSituacion = models.ForeignKey(Situaciones)
# 	idTitulo = models.ForeignKey(Titulos)
# 	idConocimiento = models.ForeignKey(ConocimientosPc)
# 	idCursoRealizado = models.ForeignKey(CursosRealizados)

# class NivelIdioma(models.Model):
# 	nombre = models.CharField(max_length=30)

# class TiposConocimientosIdiomas(models.Model):
# 	nombre = models.CharField(max_length=30)

# class Idiomas(models.Model):
# 	nombre = models.CharField(max_length=30)
# 	posee_estudio_internacional = models.BooleanField()
# 	idEstudio = models.ForeignKey(Estudios)
# 	idTipoConocimiento = models.ForeignKey(TiposConocimientosIdiomas)
# 	idNivel = models.ForeignKey(NivelIdioma)

# class DatosCarnet(models.Model):
# 	municipio = models.CharField(max_length=30)
# 	idTipo = models.ForeignKey(TipoCarnet)
# 	idCurriculum = models.ForeignKey(Curriculums)

# 	def __unicode__(self):
# 		return "%s".format(self.id)

# class TelefonosCurriculums(models.Model):
# 	idCurriculum = models.ForeignKey(Curriculums)
# 	idTelefono = models.ForeignKey(Telefonos)

# 	def __unicode__(self):
# 		return "%s - %s".format(self.idCurriculum, self.idTelefono)

# 	class Meta:
# 		verbose_name_plural = "Telefonos Curriculums"

# class AreasOcupacionales(models.Model):
# 	nombre = models.CharField(max_length=50)

# 	def __unicode__(self):
# 		return self.nombre

# 	class Meta:
# 		verbose_name_plural = "Areas Ocupacionales"

# class GruposOcupacionales(models.Model):
# 	nombre = models.CharField(max_length=50)
# 	idArea = models.ForeignKey(AreasOcupacionales)

# 	def __unicode__(self):
# 		return self.nombre

# 	class Meta:
# 		verbose_name_plural = "Grupos Ocupacionales"

# class OficiosProfesiones(models.Model):
# 	idCurriculum = models.ForeignKey(Curriculums)
# 	idGrupoOcupacional = models.ForeignKey(GruposOcupacionales)

# 	def __unicode__(self):
# 		return "%s - %s".format(self.idCurriculum.id, self.idGrupoOcupacional.id)

# 	class Meta:
# 		verbose_name_plural = "Oficios Profesiones"

# class Tags(models.Model):
# 	label = models.CharField(max_length=20)

# 	def __unicode__(self):
# 		return self.label

# 	class Meta:
# 		verbose_name_plural = "Tags"

# class Productos(models.Model):
# 	nombre = models.CharField(max_length=30)
# 	costo = models.FloatField()
# 	stock = models.IntegerField()

# 	def __unicode__(self):
# 		return "%s - $%s - %s".format(self.nombre, self.costo, self.stock)

# class TagsProducto(models.Model):
# 	idTag = models.ForeignKey(Tags)
# 	idProducto = models.ForeignKey(Productos)

# 	def __unicode__(self):
# 		return "%s - %s".format(self.idTag, self.idProducto)

# 	class Meta:
# 		verbose_name_plural = "Tags Producto"

# class Empresas(models.Model):
# 	nombre = models.CharField(max_length=30)
# 	direccion = models.CharField(max_length=30)
# 	mision = models.TextField()
# 	vision = models.TextField()
# 	latitud = models.IntegerField()
# 	longitud = models.IntegerField()
# 	cuil_cuit = models.IntegerField()
# 	banner = models.ImageField(upload_to="imagen/banner/")
# 	idUsuario = models.ForeignKey(User)

# 	def __unicode__(self):
# 		return "%s - %s".format(self.nombre, self.cuil_cuit)

# class Catalogos(models.Model):
# 	idEmpresa = models.ForeignKey(Empresas)
# 	nombre = models.CharField(max_length=30)
# 	fecha_inicio = models.DateTimeField()
# 	fecha_fin = models.DateTimeField()

# 	def __unicode__(self):
# 		return "%s - %s".format(self.idEmpresa, self.nombre)

# 	class Meta:
# 		verbose_name_plural = "Catalagos"

# class ProductosCatalogos(models.Model):
# 	idProducto = models.ForeignKey(Productos)
# 	idCatalogo = models.ForeignKey(Catalogos)

# 	def __unicode__(self):
# 		return "%s - %s".format(self.idProducto, self.idCatalogo)

# 	class Meta:
# 		verbose_name_plural = "Productos Catalogos"

# class Categorias(models.Model):
# 	nombre = models.CharField(max_length=30)

# 	def __unicode__(self):
# 		return self.nombre

# 	class Meta:
# 		verbose_name_plural = "Categorias"

# class CategoriasEmpresas(models.Model):
# 	idEmpresa = models.ForeignKey(Empresas)
# 	idCategoria = models.ForeignKey(Categorias)

# 	def __unicode__(self):
# 		return "%s - %s".format(self.idEmpresa, self.idCategoria)

# 	class Meta:
# 		verbose_name_plural = "Categorias Empresas"