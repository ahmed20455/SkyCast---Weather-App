function getCurrentLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                fetch("/current_location", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        lat: position.coords.latitude,
                        lon: position.coords.longitude
                    })
                })
                .then(response => {
                    if (response.redirected) {
                        window.location.href = response.url;  // Follow redirect
                    } else if (!response.ok) {
                        return response.json().then(data => { throw new Error(data.error); });
                    }
                })
                .catch(error => alert("Error: " + error.message));
            },
            (error) => alert("Geolocation failed: " + error.message)
        );
    } else {
        alert("Geolocation is not supported by your browser.");
    }
}
