(function (window, document, $) {
	"use strict";
	
	$(window).on('load', function () {
		
	});
	
	/* On resize */
	$(window).on('resize', function () {
	});
	
	/* On scroll */
	$(window).on('scroll', function () {
		//Show or Hide back to top button
		if ($(window).scrollTop() >= 180) {
			$('#hook-to-top').addClass('hook_shown');
		} else {
			$('#hook-to-top').removeClass('hook_shown');
		}
		
		//Show or Hide Sticky Menu
		if ($(window).scrollTop() >= 180) {
			$('.header-sticky').addClass('fixed-top');
		} else {
			$('.header-sticky').removeClass('fixed-top');
		}
		
		//menu on scroll
		if ($(this).scrollTop() > 150) {
			$('.header-landing').addClass('scrolling-menu');
		} else {
			$('.header-landing').removeClass('scrolling-menu');
		}
	});
	
	$(document).ready(function($) {
		//scrolling
		var offset = $('.main-nav').attr('data-offset');
		var anchor_offset = $('#anchor').attr('data-offset');
		if ($('.main-nav').length > 0) $('.main-nav').singlePageNav({ 'offset': offset, 'filter': '.onepage' });
		if ($('#anchor, .anchor').length > 0) $('#anchor, .anchor').singlePageNav({ 'offset': anchor_offset, 'filter': '.onepage' });
		
		if (($("body, html").scrollTop() == 0) && ($(".main-nav .onepage").length > 0)) {
			$('.main-nav').find('li').children('a').removeClass('current');
			$('.main-nav').children('li').first().children('a').addClass('current');
		}
		
		//Toggle sidebar panel
		var sidebar_is_open = false;
		init_sidebar(sidebar_is_open);
		
		//search button
		$('.search-trigger').on('click',function(){
            $(this).toggleClass("show-search");
			$('.header-search').toggleClass("show-search");
        });
		
		//Toggle Accordion
		$(document).on('show.bs.collapse hide.bs.collapse', '.accordion', function(e) {
			var $target = $(e.target)
			if (e.type == 'show')
				$target.prev('.accordion-heading').find('.accordion-toggle').addClass('active');
			if (e.type == 'hide')
				$target.prev('.accordion-heading').find('.accordion-toggle').removeClass('active');
		});
		
		//Toggle Mobile Menu
		$('.mobile-panel li a').on('click',function(){
            $(this).siblings(".sub-menu").toggleClass('open');
			$(this).toggleClass('open');
			if($(this).siblings(".sub-menu").hasClass('open')) {
				$(this).siblings(".sub-menu").slideDown();
			} else {
				$(this).siblings(".sub-menu").slideUp();
			}
        });
		
		//Toggle Search
		$('.search-trigger-header').on('click', function() {
			$('body').toggleClass('show-search');
		});
		$('.search-close').on('click', function() {
			$('body').toggleClass('show-search');
		});
		
		//fitvids
		if ($('.media').length > 0) $('.media').fitVids();
		
		//Popup Magnific
		popupContent();
		
		//Owl Carousel
		OwlCarousel();
		
		//blog slick slider
		BlogSlickSlider();
		
		//Counter
		Counter();
		
		//Progress Bars
		ProgressBar();
		
		//Text Rotation
		initRotationText();
		
		//Google Map
		googleMap();
		
		//banner carousel background image rotation
		var headerHeight = $('.header-desktop').height();
		var bannerHeight = window.innerHeight - $('.header-desktop').innerHeight();
		
		$('.section-banner-carousel').css('height', bannerHeight);
		$('.banner-carousel .item').each(function() {
			$(this).css('height', bannerHeight);
			$(this).find('fullheight').css('height', bannerHeight);
		});
		
		$('.section-hover').hide();
		$('.section-hover').first().show();
		
		$(".banner-carousel .item").on("mouseenter", function() {
			var source = $(this).attr("data-source");
			$('#' + source).fadeIn();
			$('.section-hover').not('#' + source).fadeOut();
			if($('#' + source).find('video').length > 0) {
				$('#' + source).find('video').get(0).play();
			}
		});
		
		$('.banner-carousel .owl-pagination .owl-page').on('touchstart', function() {
			checkScreenSize($(this));
		});
		
		//scroll to top
		$('body').on('click', '#hook-to-top', function() {
			$("html, body").animate({
				scrollTop: 0
			}, 800);
			return false;
		});
	});

})(window, document, jQuery);

/*=================================================================
	check screen size
===================================================================*/
function checkScreenSize(obj){
	var newWindowWidth = $(window).width();
	if (newWindowWidth < 769) {
		
		var index = obj.index();
		index = parseInt(index, 10);
		$(".banner-carousel-nav").find("li").removeAttr("class");
		$(".banner-carousel-nav").find("li").eq(index).addClass("active");
		
		var source = $(".banner-carousel-nav").find("li").eq(index).attr("data-source");
		$('#' + source).fadeIn();
		$('.section-hover').not('#' + source).fadeOut();
	}
}


/*=================================================================
	check screen size
===================================================================*/
function popupContent(){
	/**
	* Popup
	*/
	$('[data-init="magnificPopup"]').each(function(index, el) {
		var $el = $(this);
	
	var magnificPopupDefault = {
			removalDelay: 500, //delay removal by X to allow out-animation
			callbacks: {
				beforeOpen: function() {
					this.st.mainClass = this.st.el.attr('data-effect');
				}
			},
			midClick: true // allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source.
		}
	
	// Merge settings.
		var settings = $.extend(true, magnificPopupDefault, $el.data('options'));
	
	$el.magnificPopup(settings);
	});
	
	//Gallery
	if ($(".gallery-item").length > 0) {
		$('.gallery-item').magnificPopup({
			gallery: {
				enabled: true
			}
		});
	}
	
	if($(".quick-view").length > 0) {
		$('.quick-view').magnificPopup({
			type: 'ajax'
		});
	}
	
	$('.popup-youtube').magnificPopup({
		type: 'iframe',
	});
}

/*=================================================================
	blog slick slider
===================================================================*/

function BlogSlickSlider(){
	if($(".blog-slick-slider").length > 0) {
		$('.blog-slick-slider').slick({
		  centerMode: true,
		  centerPadding: '60px',
		  slidesToShow: 3,
		  prevArrow: '<button type="button" class="slick-prev mdi-chevron-left"></button>',
          nextArrow: '<button type="button" class="slick-next mdi-chevron-right"></button>',
		  responsive: [
			{
			  breakpoint: 1080,
			  settings: {
				centerMode: true,
				centerPadding: '0px',
				dots: !1,
				slidesToShow: 3,
				slidesToScroll: 3,
				infinite: !0
			  }
			},
			{
			  breakpoint: 920,
			  settings: {
				centerMode: !1,
				dots: !1,
				slidesToShow: 2,
				slidesToScroll: 2,
				infinite: !0
			  }
			},
			{
			  breakpoint: 480,
			  settings: {
				centerMode: true,
				centerPadding: '0px',
				dots: !1,
				slidesToShow: 1,
				slidesToScroll: 1,
				infinite: !0
			  }
			}
		  ]
		});
	}
	
	if($(".media-slider").length > 0) {
		$('.media-slider').slick({
		  	infinite: true,
			speed: 500,
			fade: true,
			cssEase: 'linear',
			prevArrow: '<button type="button" class="slick-prev mdi-chevron-left"></button>',
          	nextArrow: '<button type="button" class="slick-next mdi-chevron-right"></button>',
		});
	}
}

/*=================================================================
	owl carousel
===================================================================*/
function OwlCarousel() {
	//Twitter Slider
	if ($(".twitter-slider").length > 0) {
		$('.twitter-slider').each(function() {
			var $this_slider = $(this);
			$this_slider.flexslider({
				animation: "fade",
				useCSS: false,
				slideshow: true,
				slideshowSpeed: 5000,
				animationDuration: 300,
				smoothHeight: true,
				directionNav: true,
				controlNav: false,
				keyboardNav: false,
				touchDrag: false,
				prevText: '<i class="fa fa-chevron-left prk_less_opacity"></i>',
				nextText: '<i class="fa fa-chevron-right prk_less_opacity"></i>',
				start: function(slider) {
					slider.css({ 'min-height': 0 });
					$(window).trigger("debouncedresize");
				}
			});
		});
	}
	if ($(".product-slider").length > 0) {
		$(".product-slider").each(function() {
			$(this).owlCarousel({
				navigation: false,
				slideSpeed: 600,
				pagination: true,
				paginationSpeed: 400,
				autoHeight: true,
				addClassActive: true,
				autoPlay: false,
				singleItem: true,
				afterInit: makePages,
				afterUpdate: makePages,
				transitionStyle : "backSlide",
			});
		});
	}
	if ($(".testimonials-slider").length > 0) {
		$(".testimonials-slider").each(function() {
			$(this).owlCarousel({
				navigation: false,
				slideSpeed: 600,
				pagination: true,
				paginationSpeed: 400,
				autoHeight: true,
				addClassActive: true,
				autoPlay: true,
				singleItem: true,
				transitionStyle : "backSlide",
			});
		});
	}
	if ($(".partner-slider").length > 0) {
		$(".partner-slider").each(function() {
			$(this).owlCarousel({
				items: 6,
				loop: true,
				mouseDrag: true,
				nav: false,
				dots: false,
				pagination: false,
				autoPlay: true,
				autoplayTimeout: 5000,
				autoplayHoverPause: true,
				smartSpeed: 1000,
				autoplayHoverPause: true,
				itemsDesktop: [1199, 4],
				itemsDesktopSmall: [979, 3],
				itemsTablet: [768, 2],
				itemsMobile: [479, 1]
			});
		});
	}
	if ($(".banner-carousel").length > 0) {
		$(".banner-carousel").each(function(){
			var autoplay = ($(this).attr("data-auto-play") === "true") ? true : false;
			$(this).owlCarousel({
				items: $(this).attr("data-desktop"),
				loop: true,
				mouseDrag: false,
				touchDrag: false,
				navigation: true,
				dots: false,
				pagination: true,
				autoPlay: autoplay,
				autoplayTimeout: 5000,
				autoplayHoverPause: true,
				smartSpeed: 1000,
				autoplayHoverPause: true,
				itemsDesktop: [1199, $(this).attr("data-desktop")],
				itemsDesktopSmall: [979, $(this).attr("data-laptop")],
				itemsTablet: [768, $(this).attr("data-tablet")],
				itemsMobile: [479, $(this).attr("data-mobile")]
			});
		});
	}
}

function makePages() {
	$.each(this.owl.userItems, function(i) {
		$('.owl-controls .owl-page').eq(i)
			.css({
				'background': 'url(' + $(this).find('img').attr('src') + ')',
				'background-size': 'cover'
			})
	});
}

/*=================================================================
	sidebar panel
===================================================================*/
function init_sidebar(sidebar_is_open) {
	$('.hidden-bar-toggle').on('click', function(e) {
		prk_toggle_sidebar(sidebar_is_open);
	});
}
function hasParentClass(e, classname) {
	if (e === document) {
		return false;
	}
	if (classie.has(e, classname)) {
		return true;
	}
	return e.parentNode && hasParentClass(e.parentNode, classname);
}
function prk_toggle_sidebar(sidebar_is_open) {
	if (sidebar_is_open === false) {
		$('.hidden-bar-toggle').removeClass('hover_trigger');
		sidebar_is_open = true;
		$('body').addClass('prk_shifted');
		$('.hidden-bar').css({ 'visibility': 'visible' });
		setTimeout(function() {
			document.addEventListener("click", function(evt) {
				console.log(evt);
				if (evt === 'close_flag' || hasParentClass(evt.target, 'hider_flag')) {
					if (sidebar_is_open === true) {
						prk_toggle_sidebar(sidebar_is_open);
					}
				}
				if (evt.target.className.includes("onepage")) {
					if (sidebar_is_open === true) {
						prk_toggle_sidebar(sidebar_is_open);
					}
				}
			});
			$('#body_hider').addClass('prk_shifted_hider');
			$('body').addClass('showing_hidden_sidebar');
		}, 300);
	} else {
		sidebar_is_open = false;
		$('body').removeClass('prk_shifted');
		$('body').removeClass('showing_hidden_sidebar');
		$('#body_hider').removeClass('prk_shifted_hider');
		setTimeout(function() {
			document.addEventListener("click", function(evt) {
				if (evt === 'close_flag' || hasParentClass(evt.target, 'hider_flag')) {
					if (sidebar_is_open === true) {
						prk_toggle_sidebar(sidebar_is_open);
					}
				}
				if (evt.target.className.includes("onepage")) {
					if (sidebar_is_open === true) {
						prk_toggle_sidebar(sidebar_is_open);
					}
				}
			});
			$('.hidden-bar').css({ 'visibility': 'hidden' });
		}, 300);
	}
}

/*=================================================================
	counter
===================================================================*/
function Counter() {
	if ($('.counter-wraper').length > 0) {
		$('.counter-wraper').each(function(index) {
			var $this = $(this);
			var waypoint = $this.waypoint({
				handler: function(direction) {
					$this.find('.counter-digit:not(.counted)').countTo().addClass('counted');
				},
				offset: "90%"
			});
		});
	}
}

/*=================================================================
	progressbar
===================================================================*/
function ProgressBar() {
	$('.group-progressbar').each(function() {
		var $this = $(this);
		var waypoint = $this.waypoint({
			handler: function(direction) {
				$this.find('.progressbar').progressbar({ display_text: 'center' });
			},
			offset: "80%"
		});
	});
}

/*=================================================================
	Text rotation
===================================================================*/
function initRotationText() {
	if ($('#js-rotating').length > 0) {
		$("#js-rotating").Morphext({
			animation: "flipInX",
			// An array of phrases to rotate are created based on this separator. Change it if you wish to separate the phrases differently (e.g. So Simple | Very Doge | Much Wow | Such Cool).
			separator: ",",
			// The delay between the changing of each phrase in milliseconds.
			speed: 2000,
			complete: function() {
				// Called after the entrance animation is executed.
			}
		});
	}
}

/*=================================================================
	google map
===================================================================*/
function googleMap() {
	if ($("#googleMap").length > 0) {
		$obj = $("#googleMap");
		var myCenter = new google.maps.LatLng($obj.data("lat"), $obj.data("lon"));
		var myMaker = new google.maps.LatLng($obj.data("lat"), $obj.data("lon"));
		function initialize() {
			var mapProp = {
				center: myCenter,
				zoom: 16,
				scrollwheel: false,
				mapTypeControlOptions: {
					mapTypeIds: [ google.maps.MapTypeId.ROADMAP, "map_style" ]
				}
			};
			var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
			var marker = new google.maps.Marker({
				position: myMaker,
				icon: $obj.data("icon")
			});
			marker.setMap(map);
		}
		google.maps.event.addDomListener(window, "load", initialize);
	}
}