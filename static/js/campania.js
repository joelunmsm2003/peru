var App = angular.module('App', ['ngCookies', 'ngAnimate']);

App.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});


function Controller($scope, $http, $cookies, $filter, $interval) {

    $('.contc').hide()


    $http.get("/campanias").success(function(response) {

        $scope.clientes = response;

        $scope.clientes1 = response;

         $(".loader").fadeOut( "slow" );


        $scope.search()

        for (var key in response) {



            $scope.ina = response[key].ina
            $scope.act = response[key].act
            $scope.barr = response[key].barr
        }


        console.log($scope.ina, $scope.act, $scope.barr)




    });




    $(function() {


        $("#upcampania").on("submit", function(e) {

            $('#upcampania').hide()

            $('.loading').show()
            $('.contc').show()
            $('.modal-footer').hide()


            e.preventDefault();
            var f = $(this);
            var formData = new FormData(document.getElementById("upcampania"));
            console.log('formdata', formData)
            formData.append("dato", "valor");


            $.ajax({
                    url: "/conteofilas/",
                    type: "post",
                    dataType: "html",
                    data: formData,
                    cache: false,
                    contentType: false,
                    processData: false
                })
                .done(function(res) {

                    console.log('conteo de filas', res)

                    $scope.contadorc = res

                    tick()

                    $interval(tick, 1000);

                });


        });

        $("#upcampania").on("submit", function(e) {

            $('#upcampania').hide()

            $('.loading').show()

            e.preventDefault();
            var f = $(this);
            var formData = new FormData(document.getElementById("upcampania"));
            console.log('formdata', formData)
            formData.append("dato", "valor");

            $.ajax({
                    url: "/uploadCampania/",
                    type: "post",
                    dataType: "html",
                    data: formData,
                    cache: false,
                    contentType: false,
                    processData: false
                })
                .done(function(res) {

                    console.log('nooooooooooooooooo')

                    $('.loading').hide()

                    $('#myModal').modal('hide')
                    $('.modal-backdrop').remove();


                    window.location = "/filtros/" + res



                });
        });




    });


    $scope.a = false
    $scope.b = false

    $scope.avanza = 0
    $scope.avanzac = '#234'

    $('.loading').hide()



    var tick = function() {

        $http.get("/nregistrosbase").success(function(response) {
            $scope.avanza = response;



        });

        //$scope.porcentaje = parseInt($scope.avanza*100/$scope.contadorc)

    }




    var sortingOrder = '-id';
    $scope.sortingOrder = sortingOrder;
    $scope.reverse = false;
    $scope.filteredItems = [];
    $scope.groupedItems = [];
    $scope.itemsPerPage = 20;
    $scope.pagedItems = [];
    $scope.currentPage = 0;

    $scope.discado = false

    $scope.parar = function(data) {
        console.log('Parar', data)

        $('#pararcampania').modal('hide')
        $('.modal-backdrop').remove();

        $http.get("/pausarcampania/" + data.id).success(function(response) {

            $http.get("/campanias").success(function(response) {
                $scope.clientes = response;

                $scope.search();

            });

            swal({
                title: 'Campaña ' + data.nombre + ' detenida',
                type: "success",
                timer: 1000,
                showConfirmButton: false
            });

        });

    }




    $scope.activar = function(data) {

        $('#activarcampania').modal('hide')
        $('.modal-backdrop').remove();
        console.log('Parar', data)

        $http.get("/activarcampania/" + data.id).success(function(response) {

            $http.get("/campanias").success(function(response) {
                $scope.clientes = response;

                $scope.search();

            });

            swal({
                title: 'Campaña ' + data.nombre + ' activada',
                type: "success",
                timer: 1000,
                showConfirmButton: false
            });


        });

    }


    $scope.eliminar = function(data, index)

    {

        $scope.model = data
        $scope.model.index = index

        console.log('index', index)

    };


    $scope.discadoget = function(data) {

        console.log('data', data)
        if (data == 1) {
            $scope.discado = false

        } else {

            $scope.discado = true
        }

    }

    $scope.color = '#333'




    $http.get("/campanias").success(function(response) {
        $scope.clientes = response;

        console.log('Clientes 1', $scope.clientes)

        $scope.dato = response[0]

        console.log('Clientes', $scope.clientes)

        $scope.search();

    });


    $scope.eliminarfiltro = function(data)

    {
        $('#eliminarfiltro').modal('hide')
        $('.modal-backdrop').remove();

        $('#eliminar').modal('hide')
        $('.modal-backdrop').remove();

        console.log('data', data)




        var todo = {

            dato: data,
            done: false
        }



        $http({

            url: "/eliminarfiltro/",
            data: todo,
            method: 'POST',
            headers: {
                'X-CSRFToken': $cookies['csrftoken']
            }
        }).
        success(function(r) {

            swal({
                title: 'Filtro eliminado :(',
                timer: 1500,
                showConfirmButton: false
            });

            $http.get("/campanias").success(function(response) {

                $scope.clientes = response;
                $scope.search();

            })

        })

    };


    $scope.cantcanal = function(data) {

        console.log(data)
        if (data < 1) {

            $scope.canal = 1
        }

    }



    $scope.filtros = function(data) {

        $http.get("/filtroscampania/" + data.id).success(function(response) {


            if (parseInt(ObjectLength(response)) == 0) {

                swal({
                    title: 'La campaña ' + data.nombre + ' no tiene filtros',
                    timer: 1000,
                    showConfirmButton: false
                });

            } else {

                data.a = false
                data.b = true

            }

            console.log('response', response)

            for (var key in response) {

                console.log('Key...', key)

                id = response[key].id
                campania_id = response[key].campania
                name = response[key].campania__nombre
                status = response[key].status
                resultado = response[key].resultado
                estadoname = response[key].estadoname
                ciudad = response[key].status_f
                segmento = response[key].status_g
                grupo = response[key].status_h
                total = response[key].total
                fonosporbarrer = response[key].fonosporbarrer

                $http.get("/header/" + campania_id).success(function(response) {

                    console.log('HEader...', response)
                    $scope.status_f_h = response[0]['statusf']
                    $scope.status_h_h = response[0]['statusg']
                    $scope.status_g_h = response[0]['statush']


                })

                if (key == 0) {

                    $scope.clientes.push({
                        fonosporbarrer: 'Barrido',
                        total: 'Total',
                        status_f: $scope.status_f_h,
                        status_h: $scope.status_h_h,
                        status_g: $scope.status_g_h,
                        campania: campania_id,
                        id: campania_id,
                        filtro: '0',
                        nombre: 'Estado',
                        estado: status,
                        estadoname: 'Estado',
                        color: 'gray',
                        font: '#fff',
                        id_filtro: 100000000
                    })

                }


                if (status == 1) {

                    $scope.clientes.push({
                        fonosporbarrer: fonosporbarrer,
                        total: total,
                        status_f: ciudad,
                        status_h: segmento,
                        status_g: grupo,
                        campania: campania_id,
                        id: campania_id,
                        filtro: '0',
                        nombre: estadoname,
                        estado: status,
                        estadoname: estadoname,
                        color: '#E8E8E8',
                        font: '#000',
                        id_filtro: id
                    })

                } else {

                    $scope.clientes.push({
                        fonosporbarrer: fonosporbarrer,
                        total: total,
                        status_f: ciudad,
                        status_h: segmento,
                        status_g: grupo,
                        campania: campania_id,
                        id: campania_id,
                        filtro: '0',
                        nombre: estadoname,
                        estado: status,
                        estadoname: estadoname,
                        color: '#A9E09D',
                        font: '#000',
                        id_filtro: id
                    })

                }

            }

            $scope.search();

        });




    }

    $scope.ocultafiltros = function(data) {

        data.a = true
        data.b = false


        $http.get("/campanias").success(function(response) {
            $scope.clientes = response;

            $scope.search();

        });




    }

    $scope.activafiltro = function(contact, index)

    {

        console.log('Contact------', contact)
        contact.estado = 0
        contact.estadoname = "Activado"
        contact.color = "#A9E09D"
        contact.font = "#4F4444"



        $http.get("/activafiltro/" + contact.id + '/' + contact.campania).success(function(response) {


            $http.get("/campanias").success(function(response) {
                $scope.clientes = response;

                $scope.search();

            });


        });

    }


    $http.get("/carteras").success(function(response) {
        $scope.carteras = response;

    });



    $scope.desactivafiltro = function(contact, index)

    {
        contact.estado = 1
        contact.estadoname = "Apagado"
        contact.color = "#E8E8E8"
        contact.font = "#564D4D"



        $http.get("/desactivafiltro/" + contact.id_filtro + '/' + contact.campania).success(function(response) {

            $http.get("/campanias").success(function(response) {
                $scope.clientes = response;

                $scope.search();

            });

        });


    }




    $http.get("/empresas").success(function(response) {
        $scope.empresas = response[0];



    });


    $http.get("/supervisores").success(function(response) {
        $scope.supervisores = response;



    });



    $scope.mpass = true


    $http.get("/user").success(function(response) {
        $scope.user = response;

        $scope.user = $scope.user[0]

        if ($scope.user['nivel'] == 2) {

            $scope.mpass = false

        }


        $('.container').fadeToggle("slow")

    });


    $scope.Admin = function(contact) {

        console.log(contact.id)

        nivel = $scope.user['nivel']

        if (nivel == 5) {

            window.location = "/monitoreo/" + contact.id
        } else {

            window.location = "/filtros/" + contact.id

        }




    };

    $scope.Reasignar = function(contact) {

        $scope.model = angular.copy(contact);
        console.log($scope.model)
        if ($scope.model.discado == 1) {

            $scope.discado = true
        } else {

            $scope.discado = false

        }

    };

    $scope.reasig = function(contact) {

        console.log('jjjj', contact)

        $('#reasignar').modal('hide')
        $('.modal-backdrop').remove();

        var todo = {

            add: "New",
            dato: contact,
            done: false
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


            swal({
                title: 'Campaña ' + contact.nombre + ' editada :)',
                type: "success",
                timer: 1000,
                showConfirmButton: false
            });

            $scope.agregar = ""

            $http.get("/campanias").success(function(response) {
                $scope.clientes = response;

                $scope.search();

            });



        })



    };




    $scope.numberOfPages = function() {

        return Math.ceil($scope.clientes.length / $scope.pageSize);

    };




    $scope.addNew = function(agregar) {

        var todo = {

            add: "New",
            dato: agregar,
            done: false
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

            swal({
                title: "Empresa " + data + " agregado",
                type: "success",
                confirmButtonColor: "#b71c1c",
                confirmButtonText: "Cerrar",
            }, function() {
                window.location.href = "/empresa"
            });

            $scope.agregar = ""

        })

    };

    $scope.saveContact = function(idx, currentPage) {


        consoel.log()
        $('#edit').modal('hide')
        $('.modal-backdrop').remove();


        var todo = {

            add: "Edit",
            dato: $scope.model,
            done: false
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

            swal({
                title: "Empresa " + data + " editado",
                type: "success",
                confirmButtonColor: "#b71c1c",
                confirmButtonText: "Cerrar",
            }, function() {});


        })


    };



    $scope.eliminarContact = function(idx, currentPage) {


        $('#eliminar').modal('hide')
        $('.modal-backdrop').remove();


        $http.get("/user").success(function(response) {
            $scope.user = response;

            $scope.user = $scope.user[0]


        });


        if ($scope.user.nivel == 1) {

            var todo = {

                dato: $scope.model,
                add: "Eliminar",
                done: false
            }


            $http({
                url: "/campanias/",
                data: todo,
                method: 'POST',
                headers: {
                    'X-CSRFToken': $cookies['csrftoken']
                }
            }).
            success(function(data) {

                $scope.contador = $scope.contador - 1

                $http.get("/campanias").success(function(response) {
                    $scope.clientes = response;

                    $scope.search();

                });


            })
        }


        if ($scope.user.nivel == 2) {


            swal({

                    title: "Ingrese clave secreta",
                    type: "input",
                    confirmButtonColor: "#b71c1c",
                    showCancelButton: true,
                    closeOnConfirm: false,
                    animation: "slide-from-top",
                    inputPlaceholder: "Ingrese clave secreta"
                },

                function(inputValue) {
                    if (inputValue === false) return false;
                    if (inputValue === "") {

                        swal.showInputError("Ingrese la clave");

                        return false
                    } else {

                        $http.get("/passcampania/" + $scope.model.id).success(function(response) {
                            $scope.pass = response;

                            $scope.passcampania = $scope.pass[0]

                            console.log('pass', inputValue, $scope.passcampania)

                            if (parseInt(inputValue) == parseInt($scope.passcampania.password)) {

                                var todo = {

                                    dato: $scope.model,
                                    add: "Eliminar",
                                    done: false
                                }


                                $http({
                                    url: "/campanias/",
                                    data: todo,
                                    method: 'POST',
                                    headers: {
                                        'X-CSRFToken': $cookies['csrftoken']
                                    }
                                }).
                                success(function(data) {

                                    $scope.contador = $scope.contador - 1

                                })



                                swal({
                                    title: "Campaña Eliminada ",
                                    type: "success",
                                    confirmButtonColor: "#b71c1c",
                                    confirmButtonText: "Aceptar",
                                }, function() {});

                                $http.get("/campanias").success(function(response) {
                                    $scope.clientes = response;

                                    $scope.search();

                                });

                            } else {

                                swal({
                                    title: "Contraseña incorrecta, lo siento ",
                                    timer: 800,
                                    showConfirmButton: false
                                });
                            }


                        });




                    }




                });

        }

    };

    $http.get("/getempresa").success(function(response) {

        $scope.empresax = response[0]

    });



    $scope.editContact = function(contact, index, currentPage) {

        $scope.index = index;
        $scope.numberPage = currentPage;
        $scope.model = angular.copy(contact);
        console.log('edit', $scope.model);

    };


    $scope.sort_by = function(newSortingOrder, currentPage) {


        function sortByKey(array, key) {
            return array.sort(function(a, b) {
                var x = a[key];
                var y = b[key];
                return ((x < y) ? -1 : ((x > y) ? 1 : 0));
            });
        }


        if ($scope.sortingOrder == newSortingOrder)
            $scope.reverse = !$scope.reverse;

        $scope.sortingOrder = newSortingOrder;

        people = sortByKey($scope.clientes, newSortingOrder);

        if ($scope.reverse) {

            console.log($scope.reverse);
            people = sortByKey(people, newSortingOrder).reverse();

        }


        $scope.clientes = people

        $scope.search()


        // icon setup
        $('th i').each(function() {
            // icon reset
            $(this).removeClass().addClass('icon-sort');
        });
        if ($scope.reverse)
            $('th.' + newSortingOrder + ' i').removeClass().addClass('icon-chevron-up');
        else
            $('th.' + newSortingOrder + ' i').removeClass().addClass('icon-chevron-down');

    };

    $scope.search = function() {




        var output = {};

        $scope.clientes = $filter('filter')($scope.clientes1, $scope.tipo)

        $scope.contador = ObjectLength($scope.clientes)


        $scope.filteredItems =$scope.clientes

        $scope.currentPage = 0;

        console.log('$scope.filteredItems', $scope.filteredItems)

        $scope.groupToPages();

    };


    function ObjectLength(object) {
        var length = 0;
        for (var key in object) {
            if (object.hasOwnProperty(key)) {
                ++length;
            }
        }
        return length;
    };


    $scope.groupToPages = function() {

        console.log('Grupo')
        $scope.pagedItems = [];

        for (var i = 0; i < $scope.filteredItems.length; i++) {


            if (i % $scope.itemsPerPage === 0) {
                $scope.pagedItems[Math.floor(i / $scope.itemsPerPage)] = [$scope.filteredItems[i]];
            } else {
                $scope.pagedItems[Math.floor(i / $scope.itemsPerPage)].push($scope.filteredItems[i]);
            }
        }

        console.log('$scope.pagedItems', $scope.pagedItems[0])
        var input = []

        for (var i = 1; i <= $scope.pagedItems.length; i++) input.push(i);

        $scope.toto = input

    };


    $scope.prevPage = function() {
        if ($scope.currentPage > 0) {
            $scope.currentPage--;
        }
    };

    $scope.nextPage = function() {
        if ($scope.currentPage < $scope.pagedItems.length - 1) {
            $scope.currentPage++;
        }
    };

    $scope.setPage = function() {
        $scope.currentPage = this.n - 1;
    };


    Controller.$inject = ['$scope', '$filter'];

}