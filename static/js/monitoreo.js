
var App=angular.module('App', ['ngCookies','chart.js','ngAnimate']);

App.config(function($interpolateProvider){
$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});






campania = window.location.href.split("monitoreo/")[1].split("/")[0]

$(function () {
    $('#pie').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie',
            events: {
                    load: function () {

                        // set up the updating of the chart each second
                        var series = this.series[0];


        var updateChart = function() {
            
        $.getJSON("/estllamada/"+campania, function (result) {


            console.log('grafica',result)

            
            
            series.data[0].update(result['porbarrer']);
            series.data[1].update(result['barridos']);
          

            

        });   


        }      
              
        setInterval(function(){updateChart()},100000);



                    }
                }



        },
        title: {
            text: 'Tráfico'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                showInLegend: true,
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },

         
        series: [{

            name: "Total",
            colorByPoint: true,
            data: [
            {
                name: "Por Barrer",
                y: 0,

            }, {
                name: "Barridos",
                y: 0,
            }
            ]
        }]

    });
});


$(function () {
    $('#pie1').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie',
            events: {
                    load: function () {

                        // set up the updating of the chart each second
                        var series = this.series[0];


        var updateChart = function() {
            
        $.getJSON("/estllamada/"+campania, function (result) {


            console.log('grafica',result)

            
            
            series.data[0].update(result['errados']);
            series.data[1].update(result['correctos']);
          

            

        });   


        }      
              
        setInterval(function(){updateChart()},100000);



                    }
                }



        },
        title: {
            text: 'Estado '
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                showInLegend: true,
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },

         
        series: [{

            name: "Estado ",
            colorByPoint: true,
            data: [
            {
                name: "Errados",
                y: 0,

            }, {
                name: "Correctos",
                y: 0,
            }
            ]
        }]

    });
});



$(function () {
    $('#xy').highcharts({
        chart: {
            type: 'areaspline',

        },
        title: {
            text: 'Cantidad'
        },
        legend: {
            layout: 'vertical',
            align: 'left',
            verticalAlign: 'top',
            x: 150,
            y: 100,
            floating: true,
            borderWidth: 1,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
        },
        xAxis: {
            categories: [
                'Lu',
                'Ma',
                'Mi',
                'Ju',
                'Vi',
                'Sa',
                'Do'
            ],
            plotBands: [{ // visualize the weekend
                from: 4.5,
                to: 6.5,
                color: 'rgba(68, 170, 213, .2)'
            }]
        },
        yAxis: {
            title: {
                text: 'Nro Llamadas'
            }
        },
        tooltip: {
            shared: true,
            valueSuffix: ' units'
        },
        credits: {
            enabled: false
        },
        plotOptions: {
            areaspline: {
                fillOpacity: 0.5
            }
        },
        series: [{
            name: 'Atendidas',
            data: [3, 4, 3, 5, 4, 10, 12]
        }, {
            name: 'Fallidas',
            data: [1, 3, 4, 3, 3, 5, 4]
        }]
    });
});


$(function () {

    $('#ga').highcharts({

        chart: {
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false,
            events: {
                        load: function () {

                                // set up the updating of the chart each second
                                var series = this.series[0].points[0];
                                var updateChart = function() {

                                $.getJSON("/estllamada/"+campania, function (result) {

                                console.log('grafica',result)
                                
                                  series.update(0);

                                });   

                                }      
                                setInterval(function(){updateChart()},100000);

                            }
                        }
        },

        title: {
            text: 'Llamadas'
        },

        pane: {
            startAngle: -150,
            endAngle: 150,
            background: [{
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#FFF'],
                        [1, '#333']
                    ]
                },
                borderWidth: 0,
                outerRadius: '109%'
            }, {
                backgroundColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                    stops: [
                        [0, '#333'],
                        [1, '#FFF']
                    ]
                },
                borderWidth: 1,
                outerRadius: '107%'
            }, {
                // default background
            }, {
                backgroundColor: '#DDD',
                borderWidth: 0,
                outerRadius: '105%',
                innerRadius: '103%'
            }]
        },

        // the value axis
        yAxis: {
            min: 0,
            max: 30,

            minorTickInterval: 'auto',
            minorTickWidth: 1,
            minorTickLength: 10,
            minorTickPosition: 'inside',
            minorTickColor: '#666',

            tickPixelInterval: 30,
            tickWidth: 2,
            tickPosition: 'inside',
            tickLength: 10,
            tickColor: '#666',
            labels: {
                step: 2,
                rotation: 'auto'
            },
            title: {
                text: ''
            },
            plotBands: [{
                from: 0,
                to: 10,
                color: '#55BF3B' // green
            }, {
                from: 10,
                to: 20,
                color: '#DDDF0D' // yellow
            }, {
                from: 20,
                to: 30,
                color: '#DF5353' // red
            }]
        },

        series: [{
            name: 'Speed',
            data: [80],
            tooltip: {
                valueSuffix: ' km/h'
            }
        }]

    },
    // Add some life
    function (chart) {
        if (!chart.renderer.forExport) {
           
                var point = chart.series[0].points[0],
                    newVal,
                    inc = Math.round((Math.random() - 0.5) * 20);

                newVal = point.y + inc;
                if (newVal < 0 || newVal > 200) {
                    newVal = point.y - inc;
                }

                point.update(4);

           
        }
    });
});


function Controller($scope,$http,$cookies,$filter) {







    console.log(window.location.href.split("monitoreo/"))

    campania = window.location.href.split("monitoreo/")[1].split("/")[0]
    var sortingOrder ='-id';
    $scope.sortingOrder = sortingOrder;
    $scope.reverse = false;
    $scope.filteredItems = [];
    $scope.groupedItems = [];
    $scope.itemsPerPage = 20;
    $scope.pagedItems = [];
    $scope.currentPage = 0;

    $http.get("/agentes/"+campania).success(function(response) {$scope.agentes = response;

    });

    $http.get("/infocampania/"+campania).success(function(response) {

        $scope.campana = response[0]['nombre']
        $scope.cartera = response[0]['cartera__nombre']

       
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


    console.log('agentes',$scope.agentes)


    });

    }, 100000);

    


     $http.get("/agentescampania/"+campania).success(function(response) {$scope.usuarioscampania = response;

        

    });

 

    $http.get("/empresas").success(function(response) {$scope.empresas = response[0];


       
    });

     $http.get("/agentescampania/"+campania).success(function(response) {

        $scope.campana = response[0]['campania__nombre']
        $scope.cartera = response[0]['campania__cartera__nombre']


    });






    $http.get("/user").success(function(response) {$scope.user = response;

        $scope.user = $scope.user[0]

    });


    $http.get("/nivel").success(function(response) {$scope.nivel = response;

        console.log('$scope.nivel',$scope.nivel)

    });

    $scope.btnpregunta = 'True'


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
        $scope.model.user = $scope.user
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
        $scope.model.user = $scope.user
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
    $scope.bb = 'False'
    $scope.bbi = 'True'
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

    $scope.user = nota
    
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

            swal({   title: "Perucall",   text: "Agente "+user.agente__user__first_name +" notificado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "OK",   }, function(){   });
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


        people = sortByKey($scope.clientes, newSortingOrder);

        if ($scope.reverse){

            console.log($scope.reverse);
            people = sortByKey(people, newSortingOrder).reverse();
            
        }
  

        $scope.clientes = people

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

    
    Controller.$inject = ['$scope', '$filter'];

}

