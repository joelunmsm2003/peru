$(document).ready(function() {

	// store wrap div in a variable
	$container = $( "body" );
	
	// p tag where we will display the document width
	$documentWidth = $( '#curr_size' );
	
	// display document width in the container
	$documentWidth.text( $container.width() + " px" );


	// fire event when window is resized
	$( window ).resize( function(){
	
	  /* check whether our paragraph is empty
	  if ($documentWidth.length===0){
	    // add a span tag to our paragraph
	    $documentWidth = $( '<span id="document-width" />' );
	
	    // add the span to the paragraph
	    $container.prepend( $documentWidth );
	  }
	  */
	
	  // display document width in the container
	  $documentWidth.text( $container.width() + " px" );
	
	});
	
	// Menu Toggle
	$('.toggle-me').on('click', function(e){
	  
	  e.preventDefault();
	  
	  $('body').toggleClass('nav-collapsed');
	  
	});
  
  /*
  // Fastclick
  $(function() {
    FastClick.attach(document.body);
  });
  */
 
  // Side navigation menu, Top (mobile) navigation menu 

  var SideNav = (function() {
    
    var sideNav = $('.offcanvas');
    var topNav = $('.top-nav');
    var navItems = $("li a", sideNav);
   
    init();
    function init() {
              
        // wait till page has loaded, and then some
        $(function() { setTimeout(collapse, 1200); });
        
        sideNav
          .mouseenter(expand)
          .mouseleave(collapse);
        
    }
    
    function collapse() {
      $('body').addClass('nav-collapsed');
    }
    
    function expand() {
      $('body').removeClass('nav-collapsed');
    }
    
  })();

});