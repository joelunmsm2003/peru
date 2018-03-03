
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
    $scope.itemsPerPage = 20;
    $scope.pagedItems = [];
    $scope.currentPage = 0;

     $scope.calificacion = function(data) 

    {

          $('#eval').modal('hide')
        $('.modal-backdrop').remove();

    


    }




      $scope.fecha = function(data) 

    {

        console.log(data)

        var hoy = new Date().toJSON().slice(0,10);

        console.log('jjjjj',hoy)


        
        
        $http.get("/traercampania/"+data.campania).success(function(response) {


        fecha = response[0]['fecha']

        console.log(fecha)

        fecha = fecha.slice(0,10)

        $scope.model.fecha = fecha;

        $scope.model.fechafin = hoy;





        });




        



    }


    
    $scope.btnpregunta = 'True'


    $http.get("/preguntas/1").success(function(response) {$scope.preguntas = response;

    });

    $http.get("/examen").success(function(response) {$scope.examen = response;

        $scope.primer = response[0]

        console.log('criterio 1',response[0])

    });

    $http.get("/nota/").success(function(response) {$scope.nota = response;

    });

      $scope.Pass = function (model) {
  
        console.log('$scope.model',$scope.model)
        
        var todo={

       
            dato: $scope.model,
            done:false
        }

        $http({
        url: "/changepass/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        $http.get("/usuarios").success(function(response) {$scope.clientes = response;

        $scope.search();

        });


       swal({   title: data +' cambiado de password',   type: "success",  timer: 1000,   showConfirmButton: false });


        $('#Pass').modal('hide')
        $('.modal-backdrop').remove();

        })

        


    };



    
    $http.get("/usuarios").success(function(response) {$scope.clientes = response;

        $scope.search();

    });

     $http.get("/getempresa").success(function(response) {

        $scope.empresax=response[0]
       
    });

     $http.get("/supervisores").success(function(response) {$scope.supervisores = response;

   

    });


    $scope.nivelagente = false


          $http.get("/troncales").success(function(response) {$scope.troncales = response[0];

        console.log('trncales',$scope.troncales)
       
    });



     $http.get("/empresas").success(function(response) {$scope.empresas = response[0];


       $scope.empresasf = response

       console.log('empresasf',$scope.empresasf)
    });

    $http.get("/carteras").success(function(response) { $scope.carteras = response; });


    $http.get("/user").success(function(response) {

        $scope.user = response;

        $scope.user = $scope.user[0]

    });


    $http.get("/nivel").success(function(response) {$scope.nivel = response;

$('.container').fadeToggle("slow")

    });

    $scope.numberOfPages = function() 

    {

    return Math.ceil($scope.clientes.length / $scope.pageSize);
    
    };

    $scope.usermodal = true


     $scope.import = function(data) 

    {

        $scope.usermodal = false


    }


     $scope.ocultauser = function(data) 

    {

        $scope.usermodal = true
        $scope.contact = ""


    }


    $scope.calificarsi = function(data) 

    {

        console.log('data',data)




        
        $scope.pregunta = data
        $scope.pregunta.estadosi= true
        $scope.pregunta.estadono= false

        $scope.model.campania = $scope.agente.cam_codigo
        $scope.model.user = $scope.userxp
        $scope.model.pregunta = data
        $scope.model.respuesta = 'Si'
        $scope.model.agente =   $scope.agente

        console.log('Si.....',$scope.model)

     
        $http({

        url: "/calificaraudio/",
        data: $scope.model,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        })



    }

    $http.get("/preguntas/1").success(function(response) {$scope.preguntas = response;

    });

    $http.get("/examen").success(function(response) {$scope.examen = response;

        $scope.primer = response[0]

        console.log('criterio 1',response[0])

    });

    $http.get("/nota/").success(function(response) {$scope.nota = response;

    });

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


     $scope.calificarno = function(data) 

    {
         
       $scope.pregunta = data
        $scope.pregunta.estadono= true
        $scope.pregunta.estadosi= false

        $scope.model.campania = $scope.agente.cam_codigo
        $scope.model.user = $scope.userxp
        $scope.model.pregunta = data
        $scope.model.respuesta = 'No'
        $scope.model.agente =   $scope.agente

        console.log($scope.model)


        $http({

        url: "/calificaraudio/",
        data: $scope.model,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        })
    }


     $scope.quitarsupervisor = function(data) 

    {

       console.log('99999999999',data,$scope.model)

        var todo={

            agente:$scope.model,
            supervisor: data,
            done:false
        }

       $http({
        url: "/quitarsupervisor/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {


                $http.get("/agentesupervisor/"+$scope.model.id).success(function(response) {

                $scope.agentesupervisor = response;

                console.log('as',response)

                });

                $http.get("/agentenosupervisor/"+$scope.model.id).success(function(response) {

                $scope.agentenosupervisor = response;

                console.log('ans',response)


                });


        

        })



    }

    $http.get("/campanias/").success(function(response) {

        $scope.campanias = response;

      
        });


    $scope.traecampanias = function(data) 

    {

        console.log('Get campania',data)

        $http.get("/getcampanias/"+data.cartera).success(function(response) {

        $scope.campaniasx = response;

        console.log('C....',response[0])

        if(response[0]==undefined){

            swal({   title: 'No hay campañas para esta cartera :(',   type: "success",  timer: 1000,   showConfirmButton: false });
        }

        });
    }



     $scope.agregarsupervisor = function(data) 

    {

       console.log(data,$scope.model)

        var todo={

            agente:$scope.model,
            supervisor: data,
            done:false
        }

       $http({
        url: "/agregarsupervisor/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {


                $http.get("/agentesupervisor/"+$scope.model.id).success(function(response) {

                $scope.agentesupervisor = response;

                console.log('as',response)

                });

                $http.get("/agentenosupervisor/"+$scope.model.id).success(function(response) {

                $scope.agentenosupervisor = response;

                console.log('ans',response)


                });


        

        })



    }



     $scope.agregarcartera = function(index,contact) 

    {

    
    console.log($scope.carterasupervisor)

    $scope.carteranosupervisor.splice(index,1);

    $scope.carterasupervisor.push(contact);

    var todo={

            add: "New",
            user:$scope.model,
            dato: contact,
            done:false
        }

       $http({
        url: "/agregarcartera/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        $('#myModal').modal('hide')
        $('.modal-backdrop').remove();

     
        $scope.agregar=""

        })



    
    };

 


    $scope.MyCtrl = function() 

    {

    $scope.agregar.cartera = [$scope.colors[0], $scope.colors[1]];
    }



    $scope.nivelcartera= 0

    $scope.nivelp = function(agregar) 

    {

    nivel = agregar['nivel']

    if (nivel==3){

        $scope.nivelcartera = false
      $scope.nivelagente = true
    }

    if (nivel==1){

        $scope.nivelcartera = false
      $scope.nivelagente = false
    }
    if (nivel==5){

        $scope.nivelcartera = false
      $scope.nivelagente = false
    }





    
    if (nivel ==2){


        $scope.nivelcartera = 1
        $scope.nivelagente = false

    }

        $http.get("/getanexo/"+nivel).success(function(response) {

        $scope.anexos = response;

        console.log(response)

        });
   


    
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

        $('#myModal').modal('hide')
        $('.modal-backdrop').remove();

        swal({   title: data,   type: "success",  timer: 1000,   showConfirmButton: false });


    $http.get("/usuarios").success(function(response) {$scope.clientes = response;

        $scope.search();

    });




        $scope.nivelcartera = false
        $scope.nivelagente = false
 
        

        $scope.agregar=""
        $scope.anexos = ""

        })


    };

    $scope.saveContact = function (idx,currentPage) {


        $scope.pagedItems[currentPage][idx] = angular.copy($scope.model);
        $('#edit').modal('hide')
        $('.modal-backdrop').remove();

        console.log('modelo',$scope.model)


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

   
              swal({   title: "Usuario "+data +" editado",   type: "success",  timer: 700,   showConfirmButton: false });

         //window.location.href = "/usuario"  

             $http.get("/usuarios").success(function(response) {$scope.clientes = response;

        $scope.search();

    });



     });





        $('#Edit').modal('hide')
        $('.modal-backdrop').remove();
    };



    $scope.eliminarContact = function (idx,currentPage) {

        $('#eliminar').modal('hide')
        $('.modal-backdrop').remove();


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
        

        swal({   title: "Usuario "+data +" eliminado",   type: "success",  timer: 700,   showConfirmButton: false });
 
         $http.get("/usuarios").success(function(response) {$scope.clientes = response;

        $scope.search();

        });

        })

    };


    $scope.editContact = function (contact,index,currentPage) {

        $scope.index = index;
        $scope.numberPage =currentPage;

        nivel = contact.nivel

        $http.get("/getanexo/"+nivel).success(function(response) {

        $scope.anexos = response;

        $scope.anexos.push(contact.anexo)

        console.log(response)

        });

        $http.get("/carterasupervisor/"+contact.id).success(function(response) {

        $scope.carterasupervisor = response;

        console.log('hshhshshs',$scope.carterasupervisor)

        });

        $http.get("/carteranosupervisor/"+contact.id).success(function(response) {

        $scope.carteranosupervisor = response;

        console.log('hshhshshs',$scope.carterasupervisor)

        });

        $http.get("/agentesupervisor/"+contact.id).success(function(response) {

        $scope.agentesupervisor = response;

        console.log('as',response)

        });

        $http.get("/agentenosupervisor/"+contact.id).success(function(response) {

        $scope.agentenosupervisor = response;

        console.log('ans',response)


        });






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




    $scope.descargaudio = function (data) {

        console.log(data)

        console.log(data['fecha'].slice(11,13))

        anio = data['fecha'].slice(0,4)
        mes = data['fecha'].slice(5,7)
        dia = data['fecha'].slice(8,10)
        campania = data['cam_codigo']
        origen = data['cam_codigo']
        destino = data['llam_numero']
        fecha = data['fecha'].slice(0,10)
        hora = data['fecha'].slice(11,13)
        min = data['fecha'].slice(14,16)
        seg= data['fecha'].slice(17,19)

    window.location.href = "http://192.168.50.206:81/monitor/pcall/"+anio+"/"+mes+"/"+dia+"/"+campania+"/"+origen+"-"+destino+"-"+fecha+"_"+hora+"-"+min+"-"+seg+".gsm"
        

    }

    $scope.evaluar = function(nota,index) 

    {

        console.log('Evaluando...')


                $scope.btnpregunta = 'True'
                $scope.btncalifica = 'False'


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



    $scope.getaudios = function (data) {

        $http({
        url: "/getaudios/",
        data: data,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        console.log('getaudios',data)

        $scope.audiospe = data


        })


    }


    $scope.postaudios = function (data) {

        $http({
        url: "/postaudios/",
        data: data,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

        console.log('postaudios',data)

        $scope.audiospe = data


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

