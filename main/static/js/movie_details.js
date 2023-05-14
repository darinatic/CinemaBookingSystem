console.log("movie_details.js loaded");

const container = document.querySelector(".seat-container");
let seats = null;
const count = document.getElementById("count");
const total = document.getElementById("total");
const totalPrice = document.getElementById("totalPrice")
const movieSelect = document.getElementById("movie");
const resetBtm = document.querySelector(".sc-reset");
const addToCartBtn = document.querySelector(".sc-addToCart");

const table = document.querySelector(".table");
const newRow = table.insertRow();

// const movieJson = "{{ movie_json|escapejs }}";
// const movieObj = JSON.parse(movieJson);

let addTicketsOnReload = true;


let ticketPrice = + movieSelect.value;

const sessionJSON = "{{ session_json|escapejs }}";
const sessionObj = JSON.parse(sessionJSON);

const movieObj = sessionObj.movie;
console.log(sessionObj);

populateUI();

// Save selected movie index and price
function setMovieData(movieIndex, moviePrice) {
    localStorage.setItem("selectedMovieIndex", movieIndex);
    localStorage.setItem("selectedMoviePrice", moviePrice);
}

// Update total and count
function updateSelectedCount() {
    const selectedSeats = document.querySelectorAll(".row .seat.selected");

    const seatsIndex = [...selectedSeats].map((seat) => [...seats].indexOf(seat));

    localStorage.setItem("selectedSeats", JSON.stringify(seatsIndex));

    if (addTicketsOnReload) {
        seatsIndex.forEach((seat) => {
            addSeatToCart(seat);
        });
        addTicketsOnReload = false;
    }

    const selectedSeatsCount = selectedSeats.length;

    count.innerText = selectedSeatsCount;
    total.innerText = selectedSeatsCount * ticketPrice;
    totalPrice.innerText = selectedSeatsCount * ticketPrice;

    setMovieData(movieSelect.selectedIndex, movieSelect.value);
}

// Get data from localstorage and populate UI
function populateUI() {

    generateSeats();
    setSeatsArray();

    const selectedSeats = JSON.parse(localStorage.getItem("selectedSeats"));

    if (selectedSeats !== null && selectedSeats.length > 0) {
        seats.forEach((seat, index) => {
            if (selectedSeats.indexOf(index) > -1) {
                seat.classList.add("selected");
            }
        });
    }

    const selectedMovieIndex = localStorage.getItem("selectedMovieIndex");

    if (selectedMovieIndex !== null) {
        movieSelect.selectedIndex = selectedMovieIndex;
    }
}

function generateSeats() {
    const seatObjs = sessionObj.seats;
    let seatRowNo = 0;
    let seatRow = null;

    seatObjs.forEach((seat, index) => {
        if (index % 8 === 0) {
            seatRowNo++;
            seatRow = document.createElement("div");
            seatRow.classList.add("row", "justify-content-center");
        }

        const seatDiv = document.createElement("div");
        seatDiv.classList.add("seat");

        if (seat.is_available === false) {
            seatDiv.classList.add("sold");
        }

        seatRow.appendChild(seatDiv);

        if ((index + 1) % 8 === 0 || index === seatObjs.length - 1) {
            const seatContainer = document.querySelector(".seat-container");
            seatContainer.appendChild(seatRow);
        }
    });
}

function setSeatsArray() {
    seats = document.querySelectorAll(".row .seat:not(.sold)");
}

function addSeatToCart(index) {

    const newRow = table.insertRow();
    newRow.setAttribute("data-indexes", index.toString());

    const seat = newRow.insertCell(0);
    const typeSelect = newRow.insertCell(1);
    const price = newRow.insertCell(2);
    const button = newRow.insertCell(3);

    seat.innerHTML = '<div class="sc-ticket"><p>Seat No.' + (index + 1).toString() + '</p></div>';
    typeSelect.innerHTML = '<select name="ticket_type" id="sc_ticketType"><option value="child">child</option><option value="adult">adult</option></select>';
    price.innerHTML = '<div class="ticket-price">$ 5.00</div>';
    button.innerHTML = '<div class="ticket-deselect-btn"><button>-</button></div>';

    button.addEventListener("click", () => {
        table.deleteRow(newRow.rowIndex);
        updateSelectedCount();
    });
}

function removeSeatFromCart(index) {
    const rows = table.rows;
    for (let i = 1; i < rows.length; i++) {
        if (rows[i].getAttribute("data-indexes") === index.toString()) {
            table.deleteRow(i);
            updateSelectedCount();
            break;
        }
    }
}

function clearSelection() {
    const selectedSeats = document.querySelectorAll(".row .seat.selected");
    selectedSeats.forEach((seat) => {
        seat.classList.remove("selected");
    });

    const rows = table.rows;
    for (let i = rows.length - 1; i > 0; i--) {
        table.deleteRow(i);
    }

    updateSelectedCount();
}

// Seat click event
container.addEventListener("click", (e) => {
    if (e.target.classList.contains("seat") && !e.target.classList.contains("sold")) {
        e.target.classList.toggle("selected");

        updateSelectedCount();
        console.log([...seats].indexOf(e.target));

        if (e.target.classList.contains("selected")) {
            addSeatToCart([...seats].indexOf(e.target));
        } else {
            const index = [...seats].indexOf(e.target);
            removeSeatFromCart(index);
        }
    }
});

resetBtm.addEventListener("click", () => {
    clearSelection();
});

addToCartBtn.addEventListener("click", () => {


    const rows = table.rows;
    const seats = [];

    for (let i = 1; i < rows.length; i++) {
        const indexes = rows[i].getAttribute("data-indexes").split(",");
        const seat = indexes.map((index) => [index])[0][0];
        const price = rows[i].querySelector(".ticket-price").innerText;
        seats.push({ seat, price });
    }

    const data = {
        "session": sessionObj,
        "seats": seats
    };

    fetch("{% url 'addtoCart' %}", {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', // Necessary to work with request.is_ajax()
            'X-CSRFToken': "{{ csrf_token }}"
        },
        body: JSON.stringify(
            { "data": data }
        )
    }).then(response => {
        if (response.ok) {
            window.location.href = '{% url "ticketcart" %}';
        } else {
            throw new Error('Something went wrong');
        }
    })
}); // Initial count and total set
updateSelectedCount();