document.addEventListener("DOMContentLoaded", function () {
    let favButton = document.getElementById("fav-btn");

    if (favButton) {
        favButton.addEventListener("click", function () {
            let eventId = this.getAttribute("data-event-id");
            let requestUrl = this.getAttribute("data-url");
            let isFavourite = favButton.getAttribute("data-is-favourite") === "true"; // Проверяваме правилно

            console.log("Before click - isFavourite:", isFavourite); // ✅ Логваме текущото състояние

            fetch(requestUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(),
                },
                body: JSON.stringify({ event_id: eventId })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    alert(data.message);

                    // ✅ Тук правилно сменяме състоянието
                    if (isFavourite) {
                        favButton.classList.remove("btn-danger");
                        favButton.classList.add("btn-success");
                        favButton.innerHTML = 'Add to Favourites <i class="fas fa-heart" style="margin-left: 5px;"></i>';
                        favButton.setAttribute("data-is-favourite", "false");
                    } else {
                        favButton.classList.remove("btn-success");
                        favButton.classList.add("btn-danger");
                        favButton.innerHTML = 'Remove from Favourites <i class="fas fa-heart-broken" style="margin-left: 5px;"></i>';
                        favButton.setAttribute("data-is-favourite", "true");
                    }

                    console.log("After click - isFavourite:", favButton.getAttribute("data-is-favourite")); // ✅ Логваме след клик
                } else if (data.error) {
                    alert("Грешка: " + data.error);
                }
            })
            .catch(error => console.error("Error:", error));
        });
    }
});

// Функция за вземане на CSRF токен
function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith("csrftoken=")) {
                cookieValue = cookie.substring("csrftoken=".length, cookie.length);
                break;
            }
        }
    }
    return cookieValue;
}
