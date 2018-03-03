
var App=angular.module('App', ['ngCookies','chart.js','ngAnimate']);

App.config(function($interpolateProvider){
$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});


campania = window.location.href.split("monitoreo/")[1].split("/")[0]



$(function () {
    // Create the chart
    $('#graph2').highcharts({
        chart: {
            type: 'column',
             events: {
                        load: function () {

                                serie1 = this.series

                                  var updateChart = function() {

                                $.getJSON("/botoneragraph/"+campania, function (result) {

                                    console.log('Gestion',result)
                                    serie1[0].points[0].update(result['Promesa'])
                                    serie1[0].points[1].update(result['Contacto Directo'])
                                    serie1[0].points[2].update(result['Contacto Indirecto'])
                                    serie1[0].points[4].update(result['No Contacto'])
                           
                                });

                            }

                        setInterval(function(){updateChart()},20000);

                            }
                        }
        },
        title: {
            text: 'Resultado de la Gestión'
        },
     
        xAxis: {


            categories: [
                'Promesa',
                'Contacto Directo',
                'Contacto Indirecto',
                'No Contacto'
              

            ],
            crosshair: true
        },
        yAxis: {
            title: {
                text: 'Porcentaje'
            }

        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                borderWidth: 0,
                dataLabels: {
                    enabled: true,
                    format: '{point.y:.0f}'
                }
            }
        },

        tooltip: {
            headerFormat: '<span style="font-size:11px">{series.name}</span><br>',

            pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.0f}</b><br/>'

        },

         


        series: [{
            name: 'Llamadas',
            colorByPoint: true,
            data: [{
                name: 'Promesa',
                y: 0,
                drilldown: 'Promesa'
            }, {
                name: 'Directo',
                y: 0,
                drilldown: 'Directo'
            }, {
                name: 'Indirecto',
                y: 0,
                drilldown: 'Indirecto'
            },

            , {
                name: 'No Contacto',
                y: 0,
                drilldown: 'No Contacto'
            }

        ]
        }],
        drilldown: {
            series: [{
                name: 'Promesa',
                id: 'Promesa',
                data: [3
            
                ]
            }, {
                name: 'Directo',
                id: 'Directo',
                data: [
                    [
                        'v40.0',
                        5
                    ],
                    [
                        'v41.0',
                        4.32
                    ],
                    [
                        'v42.0',
                        3.68
                    ],
                    [
                        'v39.0',
                        2.96
                    ],
                    [
                        'v36.0',
                        2.53
                    ],
                    [
                        'v43.0',
                        1.45
                    ],
                    [
                        'v31.0',
                        1.24
                    ],
                    [
                        'v35.0',
                        0.85
                    ],
                    [
                        'v38.0',
                        0.6
                    ],
                    [
                        'v32.0',
                        0.55
                    ],
                    [
                        'v37.0',
                        0.38
                    ],
                    [
                        'v33.0',
                        0.19
                    ],
                    [
                        'v34.0',
                        0.14
                    ],
                    [
                        'v30.0',
                        0.14
                    ]
                ]
            }, {
                name: 'Indirecto',
                id: 'Indirecto',
                data: [
                    [
                        'v35',
                        2.76
                    ],
                    [
                        'v36',
                        2.32
                    ],
                    [
                        'v37',
                        2.31
                    ],
                    [
                        'v34',
                        1.27
                    ],
                    [
                        'v38',
                        1.02
                    ],
                    [
                        'v31',
                        0.33
                    ],
                    [
                        'v33',
                        0.22
                    ],
                    [
                        'v32',
                        0.15
                    ]
                ]
            }, {
                name: 'No Contacto',
                id: 'No Contacto',
                data: [
                    [
                        'v8.0',
                        2.56
                    ],
                    [
                        'v7.1',
                        0.77
                    ],
                    [
                        'v5.1',
                        0.42
                    ],
                    [
                        'v5.0',
                        0.3
                    ],
                    [
                        'v6.1',
                        0.29
                    ],
                    [
                        'v7.0',
                        0.26
                    ],
                    [
                        'v6.2',
                        0.17
                    ]
                ]
            }]
        }
    });
});


$(function () {
    $('#pie3D').highcharts({
        chart: {
            type: 'pie',
            options3d: {
                enabled: true,
                alpha: 45,
                beta: 0
            },
            events: {
                        load: function () {

                                var serie3 = this.series[0];

                                  var updateChartpie = function() {

                                $.getJSON("/botoneragraph/"+campania, function (response) {

                                    nocontesta = response['No Contesta']
                                    buzon = response['Buzon']
                                    congestiondered = response['Error']
                                    contesta = response['Contesta']
                                    abandonada = response['Abandonada']

                                    console.log(response)


                                    // Andy changes si no existe este estado pasa como igual a 0

                                    if(!congestiondered){
                                        congestiondered = 0.001
                                    }
                                    if(!nocontesta){
                                        nocontesta = 0.001
                                    }
                                    if(!buzon){
                                        buzon = 0.001
                                    }
                                    if(!contesta){
                                        contesta = 0.001
                                    }
                                    if(!abandonada){
                                        abandonada=0.001
                                    }


                                    serie3.data[0].update(nocontesta);
                                    serie3.data[1].update(buzon);
                                    serie3.data[2].update(congestiondered);
                                    serie3.data[3].update(contesta);
                                    serie3.data[4].update(abandonada);

                                    console.log('pie3d......',nocontesta,buzon,congestiondered,contesta,abandonada)
                                });

                            }


                        setInterval(function(){updateChartpie()},10000);


                            }
                        }
        },
        title: {
            text: 'Estado de Llamadas'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
          plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                depth: 35,
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                }
            }
        },
        series: [{
            type: 'pie',
            name: 'Cantidad',
            data: [

                ['No Contesta', 1],
                ['Buzon', 1],
                ['Error', 1],
                ['Contesta', 1],
                ['Abandonada',1]
            ]
        }]
    });
});







function Controller($scope,$http,$cookies,$filter) {







    console.log(window.location.href.split("monitoreo/"))

    campania = window.location.href.split("monitoreo/")[1].split("/")[0]
    $scope.camp = campania
    var sortingOrder ='-id';
    $scope.sortingOrder = sortingOrder;
    $scope.reverse = false;
    $scope.filteredItems = [];
    $scope.groupedItems = [];
    $scope.itemsPerPage = 20;
    $scope.pagedItems = [];
    $scope.currentPage = 0;



    function ObjectLength( object ) {
    var length = 0;
    for( var key in object ) {
        if( object.hasOwnProperty(key) ) {
            ++length;
        }
    }
    return length;
    };

    $http.get("/estllamada/"+campania).success(function(response) {$scope.nllam = response['barridos'];

        console.log('llammm',$scope.nllam)

    });

    $http.get("/infocampania/"+campania).success(function(response) {

        $scope.campana = response[0]['nombre']
        $scope.cartera = response[0]['cartera__nombre']
        $scope.discado = response[0]['discado']
        $scope.mascara = response[0]['supervisor__user__empresa__mascaras']



       
    });

    $http.get("/preguntas/1").success(function(response) {$scope.preguntas = response;

    });

    $http.get("/examen").success(function(response) {$scope.examen = response;

        $scope.primer = response[0]

        console.log('criterio 1',response[0])

    });

    $http.get("/nota/").success(function(response) {$scope.nota = response;

    });

    setInterval(function(){ 

    $http.get("/agentes/"+campania).success(function(response) {$scope.agentes = response;

    $scope.ocupado = ObjectLength($filter('filter')($scope.agentes,'En Llamada'))
    $scope.engestion = ObjectLength($filter('filter')($scope.agentes,'En Gestion'))
    $scope.enpausa = ObjectLength($filter('filter')($scope.agentes,'En Pausa'))
    $scope.enespera = ObjectLength($filter('filter')($scope.agentes,'En Espera'))
    $scope.total1 = $scope.ocupado+$scope.engestion+$scope.enpausa+$scope.enespera

    });


    $http.get("/botoneragraph/"+campania).success(function(response) {

        $scope.pendiente = response['Pendiente']
        $scope.acd = response['ACD']
        $scope.total2 = response['total']
        $scope.procesado = parseInt($scope.total2) - parseInt($scope.pendiente)
	console.log('ACD 1',$scope.acd)
	console.log('Pendiente 1',$scope.pendiente)
	
    });


    $http.get("/colas/"+campania).success(function(response) {$scope.colas = response;

        console.log('colas',$scope.colas)

    });
    

    }, 5000);

       $http.get("/botoneragraph/"+campania).success(function(response) {

        $scope.pendiente = response['Pendiente']
        $scope.acd = response['ACD']        
        $scope.total2 = response['total']
        $scope.procesado = parseInt($scope.total2) - parseInt($scope.pendiente)
	console.log('ACD 2',$scope.acd)
	console.log('Pendiente 2',$scope.pendiente)
	
    });


    


     $http.get("/agentescampania/"+campania).success(function(response) {$scope.usuarioscampania = response;

        

    });

 

    $http.get("/empresas").success(function(response) {$scope.empresas = response[0];


       
    });
     $http.get("/getempresa").success(function(response) {

        $scope.empresax=response[0]
       
    });



     $http.get("/agentescampania/"+campania).success(function(response) {

        //$scope.campana = response[0]['campania__nombre']
        //$scope.cartera = response[0]['campania__cartera__nombre']


    });



     $scope.minterna = true
    $scope.mexterna = true


    $http.get("/user").success(function(response) {$scope.user = response;

        $scope.user = $scope.user[0]

        console.log('Mascara',$scope.user.empresa__mascaras__tipo)

        if($scope.user.empresa__mascaras__tipo == 'Interna'){

            $scope.minterna = true
            $scope.mexterna = false
        }

        else{

             $scope.minterna = false
             $scope.mexterna = true
        }

        console.log($scope.minterna,$scope.mexterna)

    });


    $http.get("/nivel").success(function(response) {$scope.nivel = response;

    $('.navbar-default').fadeToggle("slow","linear")
    $('.panel-default').fadeToggle("slow","linear")
    $('.table').fadeToggle("slow","linear")



    });

    $scope.btnpregunta = 'True'

     $scope.monitorbtn = true
     $scope.monitorbtnapagado = false

     $scope.susurrobtn = true
     $scope.susurrobtnapagado = false

    $scope.monitor = function(data) 

    {
        console.log(data)

                data.monitorbtn = false
         data.monitorbtnapagado = true

        $('a.monitor').attr('disabled', true);

        $http.get("/accionmonitor/"+data.campania__usuario__anexo+"/"+data.agente__anexo).success(function(response) {

         swal({   title: 'Escucha Activado :) ',   type: "success",  timer: 1500,   showConfirmButton: false });

 

        });

        setTimeout(function(){ 
           data.monitorbtn = true
            data.monitorbtnapagado = false
        }, 30000);

    }

    $scope.susurro = function(data) 

    {    

        data.susurrobtn = false
        data.susurrobtnapagado = true

        console.log(data)

        $http.get("/accionsusurro/"+data.campania__usuario__anexo+"/"+data.agente__anexo).success(function(response) {

         swal({   title: 'Susurro Activado :) ',   type: "success",  timer: 1500,   showConfirmButton: false });

        });

        setTimeout(function(){ 

            data.susurrobtn = true
            data.susurrobtnapagado = false

        }, 30000);
    }


    $scope.criterio = function(cri) 

    {       
            $scope.btnpregunta = 'True'
            $scope.btncalifica = 'False'


            if (parseInt(cri.id)<4){


                    console.log(cri.id)

                    nucri = parseInt(cri.id)+1

                    $http.get("/examen").success(function(response) {$scope.examen = response;

                    $scope.primer = response[cri.id]

                    });


                    $http.get("/preguntas/"+nucri).success(function(response) {

                    $scope.preguntas = response;


                    });

            }
            if (parseInt(cri.id)==3){

                console.log('>5...')

                $scope.btnpregunta = 'False'
                $scope.btncalifica = 'True'

            }

     
        




    }

   $scope.model  = {}
   $scope.dato  = {}


   $scope.calificacion = function(data) 

    {

          $('#eliminar').modal('hide')
        $('.modal-backdrop').remove();

    


    }



    $scope.calificarsi = function(data) 

    {

        $scope.pregunta = data
        $scope.pregunta.estadosi= true
        $scope.pregunta.estadono= false

        $scope.model.campania = campania
        $scope.model.user = $scope.userxp
        $scope.model.pregunta = data
        $scope.model.respuesta = 'Si'
        $scope.model.agente =   $scope.agente

        console.log('Calificar SI',$scope.model)

        $http({

        url: "/calificar/",
        data: $scope.model,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        })

    }

    

     $scope.calificarno = function(data) 

    {
         
        $scope.pregunta = data
        $scope.pregunta.estadono= true
        $scope.pregunta.estadosi= false

        $scope.model.campania = campania
        $scope.model.user = $scope.userxp
        $scope.model.pregunta = data
        $scope.model.respuesta = 'No'

        console.log($scope.model)


        $http({

        url: "/calificar/",
        data: $scope.model,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        })
    }



    $scope.agregar = function(index,contact) 

    {


    $scope.usuarioscampania.push(contact);
    $scope.usuarios.splice(index,1);

        var todo={

            campania: campania,
            dato: contact,
            done:false
        }

        $http({

        url: "/agregaragente/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

            swal({   title: "Asignacion de agentes",   text: data +' agregado',   timer: 2000,   showConfirmButton: false });
    
    
    
        })

    
    };

    $scope.quitar = function(index,contact) 

    {

    $scope.usuarios.push(contact);
    $scope.usuarioscampania.splice(index,1);

            var todo={

            campania: campania,
            dato: contact,
            done:false
        }

        $http({

        url: "/quitaragente/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

            swal({   title: "Asignacion de agentes",   text: data +' quitado',   timer: 2000,   showConfirmButton: false });
    
    
        })
    
    };

    
    $('.monixxx').show()
    $scope.bb = 'True'
    $scope.bbi = 'False'
    $scope.mon = function() 

    {

    console.log('jjdjdjddjj')

    $('.monixxx').show()
    $scope.bb = 'False'
    $scope.bbi = 'True'

    };

    $scope.ocultarmon = function() 

    {

    $('.monixxx').hide()
    $scope.bb = 'True'
    $scope.bbi = 'False'

    };

    $('.flex-item1').show()
    $scope.colai = 'True'
    $scope.cola = 'False'

    $scope.consumo = function() 

    {


    $('.flex-item1').show()
    $('.flex-item' ).css( "width", "87%" );
    $scope.cola = 'False'
    $scope.colai = 'True'

    };


    $scope.ocultarconsumo = function() 

    {


    $('.flex-item1').hide()
    $('.flex-item' ).css( "width", "100%" );
    $scope.cola = 'True'
    $scope.colai= 'False'


    };

    $scope.numberOfPages = function() 

    {

    return Math.ceil($scope.clientes.length / $scope.pageSize);
    
    };

    $scope.evaluar = function(nota,index) 

    {

    $http.get("/preguntas/1").success(function(response) {$scope.preguntas = response;

    });

    $http.get("/examen").success(function(response) {$scope.examen = response;

        $scope.primer = response[0]

        console.log('criterio 1',response[0])


    });


    console.log('pregunta',$scope.preguntas)

    $scope.agente = nota

    console.log('nota',nota)

    $scope.userxp = nota
    
    };




    $scope.addNew=function(agregar){


        console.log('agregar',agregar)

        var todo={

            add: "New",
            dato: agregar,
            done:false
        }

        $http({
        url: "/usuarios/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        swal({   title: "Perucall",   text: "Usuario "+data +" agregado",   type: "success",   confirmButtonColor: "#337ab7",   confirmButtonText: "OK",   }, function(){   window.location.href = "/usuario" });
 
        $scope.agregar=""

        })


    };

    $scope.saveContact = function (idx,currentPage) {


        $scope.pagedItems[currentPage][idx] = angular.copy($scope.model);
        $('#edit').modal('hide')
        $('.modal-backdrop').remove();


        var todo={

            add: "Edit",
            dato: $scope.model,
            done:false
        }


        $http({
        url: "/usuarios/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        swal({   title: "Perucall",   text: "Usuario "+data +" editado",   type: "success",   confirmButtonColor: "#337ab7",   confirmButtonText: "OK",   }, function(){   });
 
        })


        $('#Edit').modal('hide')
        $('.modal-backdrop').remove();
    };



    $scope.eliminarContact = function (idx,currentPage) {

        $('#eliminar').modal('hide')
        $('.modal-backdrop').remove();

        $scope.pagedItems[currentPage].splice(idx,1);

        var todo={

            dato: $scope.model,
            add: "Eliminar",
            done:false
        }


        $http({
        url: "/usuarios/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        $scope.contador =$scope.contador-1

        })

    };


    $scope.editContact = function (contact,index,currentPage) {

        $scope.index = index;
        $scope.numberPage =currentPage;
        $scope.model = angular.copy(contact);
        console.log('edit',$scope.model);

    };

    $scope.calificar = function (contact,user) {


        $('#notificacion').modal('hide')
        $('.modal-backdrop').remove();

        $http.get("/examen").success(function(response) {$scope.examen = response;

        $scope.primer = response[0]

        });


        $http.get("/preguntas/1").success(function(response) {

        $scope.preguntas = response;


        });

        /*

        msj = contact.respuesta +" " +contact.nota.tipo

        username = user.agente__user__username


        var todo={

            msj: msj,
            username: username,
            done:false
        }

        $http({

        url: "/enviar/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

            swal({   title: "Perucall",   text: "Agente "+user.agente__user__first_name +" calificado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "OK",   }, function(){   });
            $scope.pregunta=""
        
        })

*/
    };

    $scope.notificar = function (contact,user) {

        $('#notificacion').modal('hide')
        $('.modal-backdrop').remove();

        msj = contact

        console.log('Notifica......',user)

        username = user.agente__user__username

        var todo={

            msj: msj,
            username: username,
            done:false
        }

        $http({

        url: "/notificar/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

            swal({ title: "Agente "+user.agente__user__first_name +" notificado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Cerrar",   }, function(){   });
            $scope.notificacion=""
    
        })
    };



    $scope.sort_by = function(newSortingOrder,currentPage) {


        function sortByKey(array, key) {
            return array.sort(function(a, b) {
            var x = a[key]; var y = b[key];
            return ((x < y) ? -1 : ((x > y) ? 1 : 0));
            });
        }

    

        function sortByKey(array, key) {
            return array.sort(function(a, b) {
            var x = a[key]; var y = b[key];
            return ((x < y) ? -1 : ((x > y) ? 1 : 0));
            });
        }

    
        if ($scope.sortingOrder == newSortingOrder)
            $scope.reverse = !$scope.reverse;

        $scope.sortingOrder = newSortingOrder;


        people = sortByKey($scope.agentes, newSortingOrder);

        if ($scope.reverse){

            console.log($scope.reverse);
            people = sortByKey(people, newSortingOrder).reverse();
            
        }
  

        $scope.agentes = people

        $scope.search()


        // icon setup
        $('th i').each(function(){
            // icon reset
            $(this).removeClass().addClass('icon-sort');
        });
        if ($scope.reverse)
            $('th.'+newSortingOrder+' i').removeClass().addClass('icon-chevron-up');
        else
            $('th.'+newSortingOrder+' i').removeClass().addClass('icon-chevron-down');
    
    };

    $scope.search = function () {

        
        console.log('search')

        String.prototype.capitalizeFirstLetter = function() {

        return this.charAt(0).toUpperCase() + this.slice(1);

        }

        var output = {};

        obj = $filter('filter')($scope.clientes,$scope.tipo)

        $scope.contador = ObjectLength(obj)
       
        console.log('$scope.tipo',$scope.tipo)

        $scope.filteredItems = $filter('filter')($scope.clientes,$scope.tipo);

        $scope.currentPage = 0;

        console.log('$scope.filteredItems',$scope.filteredItems)

        $scope.groupToPages();

    };


    function ObjectLength( object ) {
    var length = 0;
    for( var key in object ) {
        if( object.hasOwnProperty(key) ) {
            ++length;
        }
    }
    return length;
    };


    $scope.groupToPages = function () {

        console.log('Grupo')
        $scope.pagedItems = [];
        
        for (var i = 0; i < $scope.filteredItems.length; i++) {


            if (i % $scope.itemsPerPage === 0) {
                $scope.pagedItems[Math.floor(i / $scope.itemsPerPage)] = [ $scope.filteredItems[i] ];
            } else {
                $scope.pagedItems[Math.floor(i / $scope.itemsPerPage)].push($scope.filteredItems[i]);
            }
        }

        console.log('$scope.pagedItems',$scope.pagedItems[0])

             var input =[]

            for (var i = 1; i <= $scope.pagedItems.length; i++) input.push(i);

            $scope.toto = input

    };


    $scope.prevPage = function () {
        if ($scope.currentPage > 0) {
            $scope.currentPage--;
        }
    };
    
    $scope.nextPage = function () {
        if ($scope.currentPage < $scope.pagedItems.length - 1) {
            $scope.currentPage++;
        }
    };
    
    $scope.setPage = function () {
        $scope.currentPage = this.n-1;
    };

    $scope.grafi = function () {
        console.log('dddd')

      

    };


    
    Controller.$inject = ['$scope', '$filter'];

}

