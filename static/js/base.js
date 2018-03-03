
campania = window.location.href.split("reporteg/")[1].split("/")[0]



var App=angular.module('App', ['ngCookies','ngAnimate']);

App.config(function($interpolateProvider){
$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});


function Controller($scope,$http,$cookies,$filter) {


    var sortingOrder ='-id';
    $scope.sortingOrder = sortingOrder;
    $scope.reverse = false;
    $scope.filteredItems = [];
    $scope.groupedItems = [];
    $scope.itemsPerPage = 30;
    $scope.pagedItems = [];
    $scope.currentPage = 0;



    
    $http.get("/base").success(function(response) {$scope.clientes = response;

        $scope.search();
       
    });

    $http.get("/empresas").success(function(response) {$scope.empresas = response[0];

        
       
    });


    $http.get("/supervisores").success(function(response) {$scope.supervisores = response;

      
       
    });


    $scope.mpromesa = []
    $scope.mdirecto = []
    $scope.mindirecto = []
    $scope.mnocontacto = []


    $http.get("/botoneraagente/"+campania).success(function(response) {

        $scope.agenteboton = response;
        console.log('Inicio',response)



        for( var key in response ) {

            $scope.mpromesa.push(8)
            $scope.mdirecto.push(3)
            $scope.mindirecto.push(55)
            $scope.mnocontacto.push(1)

        }

       
    });


    $http.get("/carteras").success(function(response) {

        $scope.carteras = response;
       
    });

    $http.get("/botoneragraph/"+campania).success(function(response) {

        $scope.nocontacto = response['No Contacto']
        $scope.directo = response['Contacto Indirecto']
        $scope.indirecto = response['Contacto Indirecto']
        $scope.promesa = response['Promesa']
        $scope.buzon = response['Buzon']
        $scope.congestiondered = response['Congestion de Red']
        $scope.asterisk = response['Asterisk']
        $scope.nocontesta = response['No Contesta']
        $scope.pendiente = response['Pendiente']
        $scope.pPromesa = response['pPromesa']

        $scope.pDirecto=response['pDirecto']
        $scope.pIndirecto=response['pIndirecto']
        $scope.pNocontacto=response['pNocontacto']
        $scope.pNocontesta=response['pNocontesta']
        $scope.pBuzon=response['pBuzon']
        $scope.pCongestion=response['pCongestion']
        $scope.pAsterisk=response['pAsterisk']
        $scope.pPendiente=response['pPendiente']


    });


    $http.get("/user").success(function(response) {$scope.user = response;

        $scope.user = $scope.user[0]

    });

    $http.get("/getcamp/"+campania).success(function(response) {

        $scope.infocamp = response[0];
        $('.repor').fadeToggle("slow")
        $('.navbar-default').fadeToggle("slow")
        $('.panel-default').fadeToggle("slow")
        $('.table').fadeToggle("slow")
        

  




    });

     $scope.graficarcampania = function(data) 


    {       
            

        console.log(data.campania.id)
        window.location="/reporteg/"+data.campania.id

    };

    

     $scope.getcampania = function(cartera) 


    {       console.log('cartera...........',cartera)

            console.log($scope.user.nivel)

            if ($scope.user.nivel == 2 || $scope.user.nivel == 1 ){

                $http.get("/getcampanias/"+cartera.cartera_id).success(function(response) {$scope.campanias = response;

                console.log('campanias',$scope.campanias)
               
            });

            }
            else{

                $http.get("/getcampanias/"+cartera.id).success(function(response) {$scope.campanias = response;

                console.log('campanias',$scope.campanias)
               
            });
            }
            

            


    };

    $scope.descarga = function() 

    {       
        

        window.location="/reportecsv/"+12+'/'+campania;
    };




    $scope.regxpag = function() 
    {

     $http.get("/base").success(function(response) {$scope.clientes = response;

        $scope.search();
       
    });
    
    };

    $scope.Reasignar = function(contact) 
    {

        $scope.model = angular.copy(contact);
        console.log($scope.model)
 
    };

     $scope.reasig = function(contact) 
    {

        console.log('jjjj',contact)

        var todo={

            add: "New",
            dato: contact,
            done:false
        }

        $http({
        url: "/reasignarsupervisor/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        swal({   title: "Supervisor actualizado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Cerrar",   }, function(){   window.location.href = "/campania" });

         
         $scope.agregar=""


        })


 
    };






    $scope.numberOfPages = function() 
    {

    return Math.ceil($scope.clientes.length / $scope.pageSize);
    
    };







    $scope.addNew=function(agregar){

      



        var todo={

            add: "New",
            dato: agregar,
            done:false
        }

        $http({
        url: "/empresas/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

       swal({   title: "Empresa "+data +" agregado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Cerrar",   }, function(){   window.location.href = "/empresa" });

         
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
        url: "/empresas/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

            swal({title: "Empresa "+data +" editado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Cerrar",   }, function(){  });


        })


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
        url: "/empresas/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        swal({ title: "Empresa "+data +" eliminado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Cerrar",   }, function(){   });

        $scope.contador =$scope.contador-1


        })
    };


    $scope.editContact = function (contact,index,currentPage) {

        $scope.index = index;
        $scope.numberPage =currentPage;
        $scope.model = angular.copy(contact);
        console.log('edit',$scope.model);

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

    promesa = []

    $scope.agenteg = function (data) {


        var todo={

            agentes: $scope.agenteboton,
            campania:campania ,
            
        }


        $http({
        url: "/agentegrafico/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        console.log('Graficando...',data)

           
        for( var key in data ) {

            $scope.mpromesa.push(2)
            $scope.mdirecto.push(1)
            $scope.mindirecto.push(111)
            $scope.mnocontacto.push(1)

        }


        })

    



    }

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


            console.log($scope.pagedItems.length)

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

  

     $scope.activa = function (data) {
            
        console.log('activa',data)
        data.seleccionar = 'si'
        data.btnon = false
        data.btnoff = true
    };

     $scope.desactiva = function (data) {
            
        console.log('desac',data)
        data.seleccionar='no'
        data.btnon = true
        data.btnoff = false
    };
    
    
    $scope.setPage = function () {
        $scope.currentPage = this.n-1;
        console.log($scope.currentPage)
    };

      $http.get("/getempresa").success(function(response) {

        $scope.empresax=response[0]
       
    });

      $scope.graficoc = false

      //grafica ultima


$(function () {

    



    $http.get("/botoneraagente/"+campania).success(function(response) {

        console.log('kkkkk',response)



   

    $('#columnas').highcharts({
        chart: {
            type: 'column',
             events: {
                        load: function () {

                                serie1 = this.series

                                $scope.link = function(){


                                    $scope.graficoc = true

                                    obj = $filter('filter')($scope.agenteboton,'si')

                                    console.log('Filtrando.....',obj)

                                    var chart = $('#columnas').highcharts();

                                    while(chart.series.length > 0){

                                         chart.series[0].remove(true);

                                    }    

                                    pregunta = []
                                    p = []
                                    d=[]
                                    i=[]
                                    nc=[]

                                    for( var key in obj ) {

                                      p.push(parseInt(obj[key]['promesa']))
                                      d.push(parseInt(obj[key]['directo']))
                                      i.push(parseInt(obj[key]['indirecto']))
                                      nc.push(parseInt(obj[key]['nocontacto']))

                                      pregunta[key]=obj[key]['agente__user__first_name'] 

                                    }

                                    

                                    console.log('pregunta',pregunta)
                                    var chart = $('#columnas').highcharts();
                                    chart.xAxis[0].setCategories(pregunta) 

                                    serie1 = this.series

                                    chart.addSeries({
                                    data: p,
                                    name:'Promesa',
                                    index: 0,
                                    zIndex:1
                                    });

                                    chart.addSeries({
                                    data: d,
                                    name:'Directo',
                                    index: 1,
                                    zIndex:1
                                    });

                                    chart.addSeries({
                                    data: i,
                                    name:'Indirecto',
                                    index: 2,
                                    zIndex:1
                                    });

                                    chart.addSeries({
                                    data: nc,
                                    name:'No Contacto',
                                    index: 3,
                                    zIndex:1
                                    });


                                     
       
                                }




                                

                            }
                        }
        
           },
        title: {

            text: "Cartera : " + $scope.infocamp.cartera__nombre+ " " + "Campaña : " +$scope.infocamp.nombre
        },

        subtitle: {
            text: 'Agente - Botonera'
        },
        

        xAxis: {
            categories: [
                'Jan',
                'Feb'
               
            ],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Cantidad '
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y} </b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
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
        series: [{
            name: 'Promesa',
            data: $scope.mpromesa

        }, {
            name: 'Directo',
            data: $scope.mdirecto

        }, {
            name: 'Indirecto',
            data: $scope.mindirecto

        }, {
            name: 'No Contacto',
            data: $scope.mnocontacto

        }]
    });

    
    $.getJSON("/botoneraagente/"+campania, function (result) {

        pregunta = []

        for( var key in result ) {

          pregunta[key]=result[key]['agente__user__first_name']

        }

        console.log('pregunta',pregunta)

        var chart = $('#columnas').highcharts();
        chart.xAxis[0].setCategories(pregunta)


    })


     });


    });



//fin grafica

    
    Controller.$inject = ['$scope', '$filter'];



   $(function () {
    // Create the chart
    $('#graph1').highcharts({
        chart: {
            type: 'column',
             events: {
                        load: function () {

                                serie1x = this.series

                                  var updateChart = function() {

                                $.getJSON("/botoneragraph/"+campania, function (result) {

                                    console.log('botoro llam',result['Contacto Indirecto'])

       

                                  
                                    serie1x[0].points[0].update(result['Promesa'])
                                    serie1x[0].points[1].update(result['Contacto Directo'])
                                    serie1x[0].points[2].update(result['Contacto Indirecto'])
                                    serie1x[0].points[3].update(result['No Contacto'])
                                    serie1x[0].points[4].update(result['Pendiente'])
                                    serie1x[0].points[5].update(result['Pendiente'])
                                   

     
                           
                                });

                            }

                        setTimeout(function(){updateChart()},1000);

                            }
                        }
        },
       

        title: {

            text: 'Cobertura - Campaña'

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
                text: 'Cantidad'
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
            pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.0f}</b> <br/>'
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
            }, {
                name: 'No Contacto',
                y: 80,
                drilldown: 'No Contacto'
            }
            , 
             {
                name: 'Pendiente',
                y: 80,
                drilldown: 'Pendiente'
            }




        ]
        }]
        
    });
});

//pie

$(function () {

    $(document).ready(function () {

        // Build the chart
        $('#pie').highcharts({
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie',
                events: {
                        load: function () {

                                var serie3 = this.series[0];

                                  var updateChartpie = function() {

                                $.getJSON("/botoneragraph/"+campania, function (response) {

                                    console.log('botoro Pie chart',response)

                                    nocontacto = response['No Contacto']
                                    directo = response['Contacto Directo']
                                    indirecto = response['Contacto Indirecto']
                                    promesa = response['Promesa']

                                    serie3.data[0].update(promesa);
                                    serie3.data[1].update(directo);
                                    serie3.data[2].update(indirecto);
                                    serie3.data[3].update(nocontacto);
                                                       
                           
                                });

                            }


                        setTimeout(function(){updateChartpie()},1000);

                       

                            }
                        }
            },
            title: {
                text: 'Efectividad Campaña Botonera Agente'
            },
           
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
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
                name: 'Brands',
                colorByPoint: true,
                data: [{
                    name: 'Promesa',
                    y: 55
                }, {
                    name: 'Directo ',
                    y: 55,
                    sliced: true,
                    selected: true
                }, {
                    name: 'Indirecto',
                    y: 55
                }, {
                    name: 'No Contacto',
                    y: 55
                }]
            }]
        });
    });
});


}
