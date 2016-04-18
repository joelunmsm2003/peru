
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

      $http.get("/carteras").success(function(response) {$scope.carteras = response;

       
    });


    $http.get("/user").success(function(response) {$scope.user = response;

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


 
        

        $scope.agregar=""

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

        console.log(contact)

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

