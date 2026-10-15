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
                .then(response => response.json().then(data => {
                    if (!response.ok) throw new Error (data.error || "Unable to fetch weather");
                    window.location.href =  data.redirect;
                }))
                .catch(error => alert("Error: " + error.message));
            },
            (error) => alert("Geolocation failed: " + error.message)
        );
    } else {
        alert("Geolocation is not supported by your browser.");
    }
}
