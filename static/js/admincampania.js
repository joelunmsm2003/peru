
var App=angular.module('App', ['ngCookies']);

App.config(function($interpolateProvider){
$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});

function Controller($scope,$http,$cookies,$filter) {


    campania = window.location.href.split("adminCampania/")[1].split("/")[0]

    $scope.camp =campania

    var sortingOrder ='-id';
    $scope.sortingOrder = sortingOrder;
    $scope.reverse = false;
    $scope.filteredItems = [];
    $scope.groupedItems = [];
    $scope.itemsPerPage = 20;
    $scope.pagedItems = [];
    $scope.currentPage = 0;

    $http.get("/infocampania/"+campania).success(function(response) {

        $scope.campana = response[0]['nombre']
        $scope.cartera = response[0]['cartera__nombre']

    });

    $http.get("/agentesdisponibles/"+campania).success(function(response) {

        $scope.usuarios = response;
        $scope.agentesd =response
       
    });

    $http.get("/agentescampania/"+campania).success(function(response) {

        $scope.usuarioscampania = response;
        $scope.agentesc =response
    });

    $http.get("/empresas").success(function(response) {$scope.empresas = response[0];
 
    });

    $http.get("/getempresa").success(function(response) {

        $scope.empresax=response[0]
       
    });

    $http.get("/user").success(function(response) {

        $scope.user = response;

        $scope.user = $scope.user[0]

    });

    $http.get("/nivel").success(function(response) {$scope.nivel = response;

        console.log('$scope.nivel',$scope.nivel)

    });

    $scope.todo = []

    $scope.add = function(index,contact) 

    {
        $scope.tipox = "true"        
    }

     $scope.next = function() 

    {

        window.location='/filtros/'+campania
         
    }

    $scope.agregaruser = function() 

    {
        $scope.usuariosp = $filter('filter')($scope.usuarios,$scope.tipox);

        console.log($scope.usuariosp)

        var todo={

            campania: campania,
            dato: $scope.usuariosp,
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

            console.log(data)


        swal({   title: "Agente agregado",   type: "success",  timer: 1000,   showConfirmButton: false });

            

               $http.get("/agentesdisponibles/"+campania).success(function(response) {

                $scope.usuarios = response;
                $scope.agentesd =response

                });


                $http.get("/agentescampania/"+campania).success(function(response) {

                $scope.usuarioscampania = response;
                $scope.agentesc =response

                });

 
    
    
        })


    }


       $scope.quitaruser = function() 

    {
        $scope.usuarioscampaniap = $filter('filter')($scope.usuarioscampania,$scope.tipox);

        console.log($scope.usuarioscampaniap)




        var todo={

            campania: campania,
            dato: $scope.usuarioscampaniap,
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


swal({   title: "Agente quitado",   type: "success",  timer: 900,   showConfirmButton: false });
 
            
               $http.get("/agentesdisponibles/"+campania).success(function(response) {

                $scope.usuarios = response;
                $scope.agentesd =response

                });


                $http.get("/agentescampania/"+campania).success(function(response) {

                $scope.usuarioscampania = response;
                $scope.agentesc =response

                });

        


        })
    



    }



    $scope.agregar = function(index,contact,seleccionar) 

    {

    console.log('contact',contact,seleccionar)

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

              

            swal({     title: data[0]['agente__user__first_name'] +' agregado ' ,   timer: 1500,   showConfirmButton: false });
    
    
    
        })

    
    };

    $scope.quitar = function(index,contact) 

    {

        console.log('quitar',contact)

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

            swal({    title: data +' quitado de esta campaña',   timer: 1000,   showConfirmButton: false });
    
    
        })
    
    };

    $scope.numberOfPages = function() 

    {

    return Math.ceil($scope.clientes.length / $scope.pageSize);
    
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

    $scope.search = function () {



        String.prototype.capitalizeFirstLetter = function() {

        return this.charAt(0).toUpperCase() + this.slice(1);

        }

        var output = {};

        obj = $filter('filter')($scope.agentesd,$scope.tipo)

        $scope.contador1 = ObjectLength(obj)
       

        $scope.usuarios = $filter('filter')($scope.agentesd,$scope.tipo);

        console.log($scope.usuarios)



    };

        $scope.search1 = function () {



        String.prototype.capitalizeFirstLetter = function() {

        return this.charAt(0).toUpperCase() + this.slice(1);

        }

        var output = {};

        obj = $filter('filter')($scope.agentesc,$scope.tipo1x)

        $scope.contador2 = ObjectLength(obj)
       

        $scope.usuarioscampania = $filter('filter')($scope.agentesc,$scope.tipo1x);

        console.log($scope.usuarios)



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

