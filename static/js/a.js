var centesimas = 0;
var segundos = 0;
var minutos = 0;
var horas = 0;
function inicio () {
  control = setInterval(cronometro,10);
  document.getElementById("inicio").disabled = true;
  document.getElementById("parar").disabled = false;
  document.getElementById("continuar").disabled = true;
  document.getElementById("reinicio").disabled = false;
}
function parar () {
  clearInterval(control);
  document.getElementById("parar").disabled = true;
  document.getElementById("continuar").disabled = false;
}
function reinicio () {
  clearInterval(control);
  centesimas = 0;
  segundos = 0;
  minutos = 0;
  horas = 0;
  Centesimas.innerHTML = ":00";
  Segundos.innerHTML = ":00";
  Minutos.innerHTML = ":00";
  Horas.innerHTML = "00";
  document.getElementById("inicio").disabled = false;
  document.getElementById("parar").disabled = true;
  document.getElementById("continuar").disabled = true;
  document.getElementById("reinicio").disabled = true;
}
function cronometro () {
  if (centesimas < 99) {
    centesimas++;
    if (centesimas < 10) { centesimas = "0"+centesimas }
    Centesimas.innerHTML = ":"+centesimas;
  }
  if (centesimas == 99) {
    centesimas = -1;
  }
  if (centesimas == 0) {
    segundos ++;
    if (segundos < 10) { segundos = "0"+segundos }
    Segundos.innerHTML = ":"+segundos;
  }
  if (segundos == 59) {
    segundos = -1;
  }
  if ( (centesimas == 0)&&(segundos == 0) ) {
    minutos++;
    if (minutos < 10) { minutos = "0"+minutos }
    Minutos.innerHTML = ":"+minutos;
  }
  if (minutos == 59) {
    minutos = -1;
  }
  if ( (centesimas == 0)&&(segundos == 0)&&(minutos == 0) ) {
    horas ++;
    if (horas < 10) { horas = "0"+horas }
    Horas.innerHTML = horas;
  }
}
jQuery.fn.anim_progressbar = function(aOptions) {
                var iCms = 1000;
                var iMms = 60 * iCms;
                var iHms = 3600 * iCms;
                var iDms = 24 * 3600 * iCms;

                var aDefOpts = {
                    start : new Date(),
                    finish : new Date().setTime(new Date().getTime() + 10 * iMms), // TODO get time from database
                    interval : 100
                };
                var aOpts = jQuery.extend(aDefOpts, aOptions);
                var vPb = this;

                return this.each(function() {
                    var iElapsedMs=0,
                        iLeftMs = aOpts.finish - new Date();
                    var iDuration = aOpts.finish - aOpts.start;
                    var ticker = function() {


                            iElapsedMs += aOpts.interval;
           
                            iLeftMs -= aOpts.interval;
    
                            var iDays = parseInt(iLeftMs / iDms), iHours = parseInt((iLeftMs - (iDays * iDms)) / iHms), iMin = parseInt((iLeftMs - (iDays * iDms) - (iHours * iHms)) / iMms), iSec = parseInt((iLeftMs - (iDays * iDms) - (iMin * iMms) - (iHours * iHms)) / iCms), iPerc = (iElapsedMs > 0) ? iElapsedMs / iDuration * 100 : 0;
                            $(vPb).children('.progressbar_con').children('#progressBar').html(iMin + 'm:' + iSec + 's</b>');
                            $(vPb).children('.progressbar_con').children('#progressBar').css('width', iPerc + '%');
                            if (iPerc >= 100) {
                              $(vPb).children('.progressbar_con').children('#progressBar').html('<b>Time Over</b>');
 clearInterval(vInterval); 
                                
clearInterval(vInterval);                                 


                        }

                    };
                    
                    
                    var vInterval = setInterval(ticker, aOpts.interval);
                    $(vPb).find(".pause").on("click",function(){

                         clearInterval(vInterval); 
                    });
                    $(vPb).find(".resume").on("click",function(){

                         vInterval = setInterval(ticker, aOpts.interval);
                    });
                     

                });
            };
            $('#progressBarMain').anim_progressbar();