FORMAT: 1A

# PeruCall

PeruCall es una colleccion de APIS para la gestion de un marcador progresivo y predictivo

# Grupo Empresa

Recursos relacionados a Empresa

## Empresa [/empresas]

### Listado de empresas [GET]

+ Response 200 (application/json)

        [
            {
                mascaras__tipo: "Externa",
                url: "http://itconser.tk",
                mail: "it@xiencias.org",
                licencias: "10",
                nombre: "XIENCIAS",
                contacto: "55558",
                telefono: 3890866,
                id: 77
            },
            {
                mascaras__tipo: "Interna",
                url: "",
                mail: "rleon@colecta.com",
                licencias: "2",
                nombre: "COLECTA",
                contacto: "Rosa Leon",
                telefono: 45454545,
                id: 73
            }
        ]

### Crear edita elimina una empresa [POST]

Crea, edita, elimina una empresa usando esta accion para esto se envia un objeto JSON 
indicando el tipo de accion y los datos de la empresa 

+ add (string) - Tipo de accion
+ dato (json object) - Una colleccion de empresa
+ Crea nueva empresa
 
        {
            "add": "New",
            "dato": 
            {
                mascaras__tipo: "Interna",
                url: "",
                mail: "rleon@colecta.com",
                licencias: "2",
                nombre: "COLECTA",
                contacto: "Rosa Leon",
                telefono: 45454545,
                id: 73
            }
        }
+ Edita una empresa


        {
            "add": "Edit",
            "dato": 
            {
                mascaras__tipo: "Interna",
                url: "",
                mail: "rleon@colecta.com",
                licencias: "2",
                nombre: "COLECTA",
                contacto: "Rosa Leon",
                telefono: 45454545,
                id: 73
            }
        }

+ Elimina una empresa

        {
            "add": "Eliminar",
            "dato": 
            {
                id: 73
            }
        }

# Grupo Usuarios 

## Usuarios [/usuarios]

### Lista usuarios [GET]

Lista usuarios segun el nivel a que pertenece

* **Agente** Se ve asimismo
* **Administrador** Ve los usuarios de la empresa
* **Monitor** Ve los usuarios de la empresa
* **Supervisor** Ve los usuarios de la empresa
* **Manager** Ve todos los usuarios de todas las empresas

+ Response 200 (application/json)

        [
            {
                username: "agente@colecta2",
                nivel: 3,
                first_name: "agente colecta2",
                empresa__nombre: "Brujitas S.A",
                email: "",
                anexo: 289,
                nivel__nombre: "Agente",
                telefono: null,
                id: 368
            },
            {
                username: "agente@colecta1",
                nivel: 4,
                first_name: "",
                empresa__nombre: null,
                email: "",
                anexo: null,
                nivel__nombre: "Manager",
                telefono: null,
                id: 367
            }
        ]

### Crea edita elimina usuarios [POST]

Crea, edita, elimina usuarios

+ add (string) - Tipo de accion
+ dato (json object) - Una colleccion de usuario
+ Response 200 (application/json)

        {
            "add": "New",
            "dato": 
            {
                username: "agente@colecta1",
                nivel: 4,
                first_name: "",
                empresa__nombre: null,
                email: "",
                anexo: null,
                nivel__nombre: "Manager",
                telefono: null,
                id: 367
            }
        }

        {
            "add": "Edit",
            "dato": 
            {
                username: "agente@colecta1",
                nivel: 4,
                first_name: "",
                empresa__nombre: null,
                email: "",
                anexo: null,
                nivel__nombre: "Manager",
                telefono: null,
                id: 367
            }
        }
        {
            "add": "Eliminar",
            "dato": 
            {
                id: 73
            }
        }

# Grupo Campañas
## Campañas [/campanias]

### Lista Campañas [GET]

Lista las campañas segun el nivel a que pertenece

* **Agente** No puede ver las campañas
* **Supervisor** Ve todas las campañas que ha creado
* **Administrador** Ve las campañas de toda la empresa
* **Manager** Ve todos los campañas de todas las empresas
+ Response 200 (application/json)

        [
            {
                barr: 0,
                supervisor: 59,
                htinicio: "08:00:00 ",
                color: "#5C93B5",
                b: false,
                filtro: "1",
                font: "#fff",
                fecha_cargada: "2016-07-11 15:41:08 UTC",
                id: 381,
                totalagentes: 1,
                mxllamada: 2,
                troncal: null,
                canales: 2,
                conectados: 1,
                ina: 0,
                discado: 1,
                factor: 1,
                nombre: "CTG_PROM",
                errados: 0,
                llamadaxhora: 4,
                cartera__nombre: "CONTUGAS",
                supervisor__user__first_name: "JOSELYN VALLE",
                cargados: 85,
                password: "12345",
                estado: "",
                a: true,
                hombreobjetivo: 80,
                barridos: 7,
                inactividad: 0,
                hfin: "19:00:00 ",
                act: 1,
                timbrados: 4,
                usuario__first_name: "ADMINISTRADOR"
            },
            {
                barr: 0,
                supervisor: 55,
                htinicio: "08:00:00 ",
                b: false,
                filtro: "1",
                fecha_cargada: "2016-07-08 22:49:21 UTC",
                id: 380,
                totalagentes: 1,
                mxllamada: 2,
                troncal: null,
                canales: 2,
                conectados: 0,
                ina: 0,
                discado: 1,
                factor: 1,
                nombre: "PRUEBA_0807_3",
                errados: 0,
                llamadaxhora: 4,
                cartera__nombre: "MAF",
                supervisor__user__first_name: "SUPERVISOR1",
                cargados: 6,
                password: "12345",
                estado: "",
                a: true,
                hombreobjetivo: 80,
                barridos: 0,
                inactividad: null,
                hfin: "19:00:00 ",
                act: 1,
                timbrados: 4,
                usuario__first_name: "ADMINISTRADOR"
            }

        ]

### Elimina Campaña [POST]

+ Request (application/json)

        dato: 
                {
                    id: 367
                }


## Campaña [/uploadCampania]

### Upload Campaña [POST]

+ Request (application/json)

        {
            'tgestion': '60',
            'llamadaxhora': '25',
            'hombreobjetivo': '80', 
            'supervisor': '55', 
            'mxllamada': '2', 
            'canales': '7', 
            'factor': '1', 
            'cartera': '53', 
            'discado': '1', 
            'dato': 'valor', 
            'inicio': '08:00', 
            'nombre': '777', 
            'timbrados': '4', 
            'password': '28050', 
            'fin': '19:00', 
            'csrfmiddlewaretoken': 'xBjtmrstQwYlvmQcDg4fCJDu18mG29jR'
        }


