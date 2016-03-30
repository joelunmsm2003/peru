
var App=angular.module('App', ['ngCookies','chart.js','ngAnimate']);

App.config(function($interpolateProvider){
$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});


console.log('hdhdhd',window.location.href.split("campaniaresult/")[1].split("/"))

campania = window.location.href.split("campaniaresult/")[1].split("/")[0]

examen = window.location.href.split("campaniaresult/")[1].split('/')[1]





$(function () {


    $('#calidadagente').highcharts({

        title: {
        text: 'Resultados Cantidad de Si y No'
        },
        chart: {
            type: 'column',
              events: {
                        load: function () {

                                serie = this.series

                                $.getJSON("/resultadocampania/"+campania+"/"+examen, function (result) {


                                    console.log(result)

                                    serie[0].points[0].update(result[0]['respno'])
                                    serie[1].points[0].update(result[0]['respsi'])

                                    serie[0].points[1].update(result[1]['respno'])
                                    serie[1].points[1].update(result[1]['respsi'])

                                    serie[0].points[2].update(result[2]['respno'])
                                    serie[1].points[2].update(result[2]['respsi'])

                                    serie[0].points[3].update(result[3]['respno'])
                                    serie[1].points[3].update(result[3]['respsi'])

                                    serie[0].points[4].update(result[4]['respno'])
                                    serie[1].points[4].update(result[4]['respsi'])

                                    serie[0].points[5].update(result[5]['respno'])
                                    serie[1].points[5].update(result[5]['respsi'])

                                    serie[0].points[6].update(result[6]['respno'])
                                    serie[1].points[6].update(result[6]['respsi'])

                                    serie[0].points[7].update(result[7]['respno'])
                                    serie[1].points[7].update(result[7]['respsi'])

                                    serie[0].points[8].update(result[8]['respno'])
                                    serie[1].points[8].update(result[8]['respsi'])
                          
                                });

                        

                            }
                        }
        },




       

       
        xAxis: {
            categories: ['Preparación para Llamada', 'Comprensión Acertiva y Rápida', 'Producto y herramientas de gestión','Argumentos precisos, coherentes y correctos', 'Cierre de Negociación, Consecuencias','Teléfono Contacto, Horarios de Atención,...']
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Total Llamadas'
            },
            stackLabels: {
                enabled: true,
                style: {
                    fontWeight: 'bold',
                    color: (Highcharts.theme && Highcharts.theme.textColor) || 'gray'
                }
            }
        },
        legend: {
            align: 'right',
            x: -30,
            verticalAlign: 'top',
            y: 25,
            floating: true,
            backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
            borderColor: '#CCC',
            borderWidth: 1,
            shadow: false
        },
        tooltip: {
            headerFormat: '<b>{point.x}</b><br/>',
            pointFormat: '{series.name}: {point.y}<br/>Muestra: {point.stackTotal}'
        },
        plotOptions: {
            column: {
                stacking: 'normal',
                dataLabels: {
                    enabled: true,
                    color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white',
                    style: {
                        textShadow: '0 0 4px black'
                    }
                }
            }
        },
        series: [{
            name: 'Sí',
            data: [0, 0, 0, 0,0,0,0]
        }, {
            name: 'No',
            data: [0, 0, 0, 0, 0,0,0]
        }]
    });


    

    $.getJSON("/resultadocampania/"+campania+"/"+examen, function (result) {

        console.log('examenesssss',result)

        pregunta = []


        for( var key in result ) {

          pregunta[key]=result[key]['pregunta']

        }

        var chart = $('#calidadagente').highcharts();
        chart.xAxis[0].setCategories(pregunta)

        console.log(pregunta)




    })


    


});





function Controller($scope,$http,$cookies,$filter) {


    console.log(window.location.href.split("campaniaresult/"))

    campania = window.location.href.split("campaniaresult/")[1].split("/")[0]
    var sortingOrder ='-id';
    $scope.sortingOrder = sortingOrder;
    $scope.reverse = false;
    $scope.filteredItems = [];
    $scope.groupedItems = [];
    $scope.itemsPerPage = 20;
    $scope.pagedItems = [];
    $scope.currentPage = 0;


    


    $http.get("/preguntas/1").success(function(response) {$scope.preguntas = response;

    });

    $http.get("/examen").success(function(response) {$scope.examen = response;

    $scope.primer = response[0]

    });

    $http.get("/examenes").success(function(response) {$scope.examenes = response;

    });

    $http.get("/campanias").success(function(response) {$scope.campanias = response;

    });

    $http.get("/traercampania/"+campania).success(function(response) {$scope.rcampania = response[0];

        console.log('jsjsjs',response[0])

    });

   
    $http.get("/getexamen/"+examen).success(function(response) {$scope.n_examen = response[0];

    });



    $http.get("/empresas").success(function(response) {$scope.empresas = response[0];

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

    $scope.change = function(data) 

    {

        console.log('ififif',data)

        location.href = "/campaniaresult/"+data.campania.id+'/'+data.examen.id



    }


    $scope.calificarsi = function(data) 

    {

 
        $scope.model.campania = campania
        $scope.model.user = $scope.user
        $scope.model.pregunta = data
        $scope.model.respuesta = 'Si'

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

    $scope.model  = {}

     $scope.calificarno = function(data) 

    {

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

    console.log('nota',nota.agente__user__username)

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

