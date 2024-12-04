// navigation  menu js
function openNav() {
    $("#myNav").addClass("menu_width");
    $(".menu_btn-style").fadeIn();
}

function closeNav() {
    $("#myNav").removeClass("menu_width");
    $(".menu_btn-style").fadeOut();
}


// get current year

function displayYear() {
    var d = new Date();
    var currentYear = d.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}
displayYear();



//client section owl carousel
$(".owl-carousel").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    dots: false,
    navText: [
        '<i class="fa fa-long-arrow-left" aria-hidden="true"></i>',
        '<i class="fa fa-long-arrow-right" aria-hidden="true"></i>'
    ],
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});


// slider carousel control


$('.slider_btn_prev').on('click', function (e) {
    e.preventDefault()
    $('.slider_text_carousel').carousel('prev')
    $('.slider_image_carousel').carousel('prev')
})


$('.slider_btn_next').on('click', function (e) {
    e.preventDefault()
    $('.slider_text_carousel').carousel('next')
    $('.slider_image_carousel').carousel('next')
})


/** google_map js **/

function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

document.addEventListener("DOMContentLoaded", () => {
    const airlineItems = document.querySelectorAll(".airline-item");
    airlineItems.forEach(item => {
        item.addEventListener("click", () => {
            item.classList.toggle("expanded");
            const logo = item.querySelector(".airline-logo");
            if (logo) logo.classList.toggle("highlight")
        })
    })
})

document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".btn-custom");
    buttons.forEach(button => {
        button.addEventListener("mousedown", () => {
            button.classList.add("btn-clicked");
        });
        button.addEventListener("mouseup", () => {
            setTimeout(() => button=classList.remove("btn-cicked"), 150);
        })
        button.addEventListener("mouseleave", () => {
            button.classList.remove("btn-clicked");
        })
    })
})

document.querySelector('#toggle-search').addEventListener('click', () => {
    const form = document.querySelector('#search-form');
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
});

document.querySelector('#search-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const destination = document.querySelector('#destination').value;
    fetch(`/api/search?destination=${destination}`)
        .then(response => response.json())
        .then(data => {
            const results = document.querySelector('#results');
            results.innerHTML = data.map(item => `<p>${item.name}</p>`).join('');
        });
});

document.addEventListener("DOMContentLoaded", function () {
    const countryLinks = document.querySelectorAll(".country-name");

    countryLinks.forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault();
            const countryId = this.dataset.countryId; // Asegúrate de que cada enlace tenga un data-country-id
            
            fetch(`/api/country/${countryId}/airlines/`)
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    // Actualiza el DOM dinámicamente con los datos recibidos
                })
                .catch(error => console.error("Error:", error));
        });
    });
});
