import csv

class Analizador:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.datos = []
        self._leer_datos()

    def _leer_datos(self):
        try:
            with open(self.archivo_csv, newline='', encoding='latin-1') as csvfile:
                lector = csv.DictReader(csvfile)
                for fila in lector:
                    fila['TOTAL_VENTAS'] = float(fila['TOTAL_VENTAS'])  # Asegura que es un número
                    self.datos.append(fila)
        except FileNotFoundError:
            print(f"El archivo '{self.archivo_csv}' no fue encontrado.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def ventas_totales_por_provincia(self):
        ventas_por_provincia = {}
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            if provincia == "ND":
                continue
            ventas = fila['TOTAL_VENTAS']
            if provincia in ventas_por_provincia:
                ventas_por_provincia[provincia] += ventas
            else:
                ventas_por_provincia[provincia] = ventas
        return ventas_por_provincia

    def ventas_por_provincia(self, nombre_provincia):
        """Retoma el total de ventas de una provincia específica"""
        nombre_provincia = nombre_provincia.strip().upper()
        resumen = self.ventas_totales_por_provincia()

        if nombre_provincia not in resumen:
            raise KeyError(f"La provincia {nombre_provincia} no se encuentra en los datos")
        return resumen[nombre_provincia]

    def exportaciones_totales_por_mes(self):
        exportaciones_por_mes = {}
        for fila in self.datos:
            mes = fila['MES']
            if mes == "ND":
                continue
            try:
                exportaciones = float(fila['EXPORTACIONES'])
            except (ValueError, TypeError):
                continue
            if mes in exportaciones_por_mes:
                exportaciones_por_mes[mes] += exportaciones
            else:
                exportaciones_por_mes[mes] = exportaciones
        return exportaciones_por_mes

    def diferencia_ventas_exportaciones_por_provincia(self):
        diferencia_por_provincia = {}
        for fila in self.datos:
            provincia = fila['PROVINCIA']
            if provincia == "ND":
                continue
            try:
                ventas = float(fila['TOTAL_VENTAS'])
                exportaciones = float(fila['EXPORTACIONES'])
            except (ValueError, TypeError):
                continue
            diferencia = ventas - exportaciones
            if provincia in diferencia_por_provincia:
                diferencia_por_provincia[provincia] += diferencia
            else:
                diferencia_por_provincia[provincia] = diferencia
        return diferencia_por_provincia
