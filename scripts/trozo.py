 # -*- coding: utf-8 -*-
import pprint
formato = [
        ["localizacion", [
            ["cups", 22],
            ["direccion", 150],
            ["poblacion", 45],
            ["codigo_postal", 10],
            ["provincia", 45]
            ]
         ],
        ["datos_titular", [
            ["tipo_titular", 2],
            ["nombre_apellidos_razon_social", 50],
            ["direccion", 80],
            ["poblacion", 45],
            ["codigo_postal", 10],
            ["provincia", 45],
            ]
         ],
        ["datos_contrato", [
            ["fecha_alta", 10],
            ["codigo_tarifa", 3],
            ["tension_suministro", 9],
            ["potencia_max_autoriz_bie", 12],
            ["potencia_max_autoriz_acta", 12],
            ["tipo_punto_medida", 2],
            ["ICP_instalado", 1],
            ["tipo_perfil_consumo", 2],
            ["derechos_acceso", 12],
            ["derechos_extension", 12],
            ["propiedad_equipo_medida", 1],
            ["propiedad_icp", 1],
            ["potencia_p1", 12],
            ["potencia_p2", 12],
            ["potencia_p3", 12],
            ["potencia_p4", 12],
            ["potencia_p5", 12],
            ["potencia_p6", 12],
            ["potencia_p7", 12],
            ["potencia_p8", 12],
            ["potencia_p9", 12],
            ["potencia_p10", 12],
            ["fecha_ultimo_cambio_comercializador", 10],
            ["fecha_ultimo_movimiento_contratacion", 10],
            ["fecha_limite_derechos_extension", 10],
            ["fecha_ultima_lectura", 10],
            ["potencia_disponible_caja", 12],
            ["impago", 11],
            ["desposito_garantia", 1],
            ["importe_deposito", 11],
            ["vivienda_habitual", 1],
            ["telegestionado_activo", 2]
        ]],
        ["sustitucion_contadores",[
            ["anio", 4],
            ["trimestre", 1]
            ]
        ],
        ["consumos", [
            ["anio", 4],
            ["tip_facturacion", 4],
            ["fecha_lectura_anterior", 10],
            ["fecha_lectura_actual", 10],
            ["tarifa", 4],
            ["discriminacion_horaria", 3],
            ["energia_activa_p1", 14],
            ["energia_activa_p2", 14],
            ["energia_activa_p3", 14],
            ["energia_activa_p4", 14],
            ["energia_activa_p5", 14],
            ["energia_activa_p6", 14],
            ["energia_activa_p7", 14],
            ["energia_reactiva_p1", 14],
            ["energia_reactiva_p2", 14],
            ["energia_reactiva_p3", 14],
            ["energia_reactiva_p4", 14],
            ["energia_reactiva_p5", 14],
            ["energia_reactiva_p6", 14],
            ["energia_reactiva_p7", 14],
            ["potencia_maxima_p1", 11],
            ["potencia_maxima_p2", 11],
            ["potencia_maxima_p3", 11],
            ["potencia_maxima_p4", 11],
            ["potencia_maxima_p5", 11],
            ["potencia_maxima_p6", 11],
            ["potencia_maxima_p7", 11],
            ]
        ]
    ]

res = []
file = open("trozo.txt", "r")
chunk = " ";
while chunk != '':
    documentGlobal = {}
    document = {}

    #print formato[0][0]
    for entry in formato[0][1]:
        chunk = file.read(entry[1])
        if chunk == '' or chunk == '\n':
            break
        document[entry[0]] = chunk
        #print entry[0]+": "+chunk
    if chunk == '' or chunk == '\n':
        break

    documentGlobal[formato[0][0]] = document
    document = {}

    #print "--------------"
    #print formato[1][0]
    for entry in formato[1][1]:
        chunk = file.read(entry[1])
        document[entry[0]] = chunk
        #print entry[0]+": "+chunk

    documentGlobal[formato[1][0]] = document
    document = {}

    #print "--------------"
    #print formato[2][0]
    for entry in formato[2][1]:
        chunk = file.read(entry[1])
        document[entry[0]] = chunk
        #print entry[0]+": "+chunk

    documentGlobal[formato[2][0]] = document
    document = {}

    #print "--------------"
    #print formato[3][0]
    for entry in formato[3][1]:
        chunk = file.read(entry[1])
        document[entry[0]] = chunk
        #print entry[0]+": "+chunk

    documentGlobal[formato[3][0]] = document
    document = {}
    auxList = []
    #print "--------------"
    #print formato[4][0]
    chunk = "a"
    for entry in formato[4][1]:
        chunk = file.read(entry[1])
        document[entry[0]] = chunk
        #print entry[0]+": "+ chunk
    auxList.append(document)
    document = {}
    chunk = file.read(1)
    while chunk != '\n' and chunk != '':
        first = True
        #print "--------------"
        #print formato[4][0]
        for entry in formato[4][1]:
            if first:
                chunk += file.read(entry[1]-1)
                document[entry[0]] = chunk
                first = False
            else:
                chunk = file.read(entry[1])
                document[entry[0]] = chunk
            #print entry[0]+": "+chunk
        auxList.append(document)
        document = {}
        chunk = file.read(1)
    documentGlobal[formato[4][0]] = auxList
    res.append(documentGlobal)

fileSavedata = open('trozo.json', "w+")
fileSavedata.write(pprint.pformat(res))

#pprint.pprint(res)

#print pprint.pformat(res)
