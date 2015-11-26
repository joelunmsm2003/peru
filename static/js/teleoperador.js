
var App=angular.module('App', ['ngCookies']);

App.config(function($interpolateProvider){
$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});



function Controller($scope,$http,$cookies,$filter) {


    agente = window.location.href.split("teleoperador/")[1].split("/")[0]


    var sortingOrder ='-id';
    $scope.sortingOrder = sortingOrder;
    $scope.reverse = false;
    $scope.filteredItems = [];
    $scope.groupedItems = [];
    $scope.itemsPerPage = 20;
    $scope.pagedItems = [];
    $scope.currentPage = 0;


    
    $http.get("/resultado").success(function(response) {$scope.resultado = response;

       
       
    });

    $http.get("/cliente/"+agente).success(function(response) {$scope.cliente = response[0];

       console.log($scope.cliente)
       base_ant = $scope.cliente.id
       
    });






    $http.get("/empresas").success(function(response) {$scope.empresas = response[0];

        
       
    });



 


    setInterval(function(){ 

     $http.get("/cliente/"+agente).success(function(response) {

        $scope.cliente = response[0];

        base_act = $scope.cliente.id

        console.log(base_act,base_ant)
      

        if (base_act != base_ant){

         swal({   title: 'Campaña ' + $scope.cliente.campania__nombre,   text: "Tienes una nueva llamada ",   type: "success",   confirmButtonColor: "#b71c1c",  confirmButtonText: "Ok", }, function(){ window.location.href = "/teleoperador/"+agente });

        
         setTimeout(
          function() 
          {
            window.location.href = "/teleoperador/"+agente
          }, 3000);


        }

        base_ant = $scope.cliente.id

      
       
    });

    $http.get("/user").success(function(response) {$scope.user = response;

        $scope.user = $scope.user[0]

    });

    $http.get("/atendida/"+agente).success(function(response) {$scope.atendida = response;

       
    });

    $http.get("/desfase/"+agente).success(function(response) {$scope.desfase = response;


       
    });

    $http.get("/agente/"+agente).success(function(response) {$scope.agente = response;


            data = JSON.parse($scope.agente['data'])

            $scope.datoagente =data[0]

      

    });


    }, 1000);


    $scope.Admin = function(contact) 
    {

    console.log(contact.id)
    window.location="/adminCampania/"+contact.id
    
    };

    $scope.Reasignar = function(contact) 
    {

        $scope.model = angular.copy(contact);
        console.log($scope.model)
 
    };

    $scope.botonera = function(contact) 
    {

       
        console.log(agente)

        var todo={

            resultado: contact,
            cliente : $scope.cliente,
            agente: agente,
            done:false
        }

        $http({
        url: "/botonera/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

   

        })
 
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

        swal({   title: "Perucall",   text: "Supervisor actualizado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Aceptar",   }, function(){   window.location.href = "/campania" });

         
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

       swal({   title: "Perucall",   text: "Empresa "+data +" agregado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Agregado",   }, function(){   window.location.href = "/empresa" });

         
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

            swal({title: "Perucall", text: "Empresa "+data +" editado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Editado",   }, function(){  });


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

        swal({title: "Perucall", text: "Empresa "+data +" eliminado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Eliminado",   }, function(){   });

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
            $(this).removeClass().addClass('fa fa-chevron-up');
        });
        if ($scope.reverse)
            $('th.'+newSortingOrder+' i').removeClass().addClass('fa-chevron-up');
        else
            $('th.'+newSortingOrder+' i').removeClass().addClass('fa-chevron-down');
    
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
        $scope.currentPage = this.n;
    };

    
    Controller.$inject = ['$scope', '$filter'];

}

