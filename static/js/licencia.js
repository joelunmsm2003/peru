
var App=angular.module('App', ['ngCookies']);

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


    
    $http.get("/empresas").success(function(response) {$scope.clientes = response;

        $scope.search();

        $scope.empresas=response[0]
       
    });

    $http.get("/user").success(function(response) {$scope.user = response;

        $scope.user = $scope.user[0]

    });

     $http.get("/licencias").success(function(response) {$scope.licencias = parseInt(response);

        console.log('lic',$scope.licencias)
        $scope.licact = response



    });



     $http.get("/lictmp").success(function(response) {$scope.lictmp = response;

       



    });

       $http.get("/getempresa").success(function(response) {

        $scope.empresax=response[0]
        
        $('.container').fadeToggle("slow")
       
    });








    $scope.totall = function(data) 
    {

    $scope.total = parseInt(data.lictemporal) + parseInt($scope.licact)
    };



    $scope.addlicencia = function(data) 
    {

    console.log(data)


        var todo={

            dato: data,
            done:false
        }

        $http({
        url: "/licencias/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

       swal({      title: "Licencias Temporal agregado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Cerrar",   }, function(){   window.location.href = "/licencia" });



        })

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

       swal({     title: "Empresa "+data +" agregado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Cerrar",   }, function(){   window.location.href = "/empresa" });

 
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

            swal({ title: "Empresa "+data +" editado",   type: "success",   confirmButtonColor: "#b71c1c",   confirmButtonText: "Cerrar",   }, function(){ window.location.href = "/empresa" });


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
        $scope.currentPage = this.n-1;
    };

    
    Controller.$inject = ['$scope', '$filter'];

}

