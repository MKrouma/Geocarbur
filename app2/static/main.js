var map = L.map('map').setView([5.440828, -4.06088], 10);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Fetch stations data and create markers
function addStations() {
    
}
fetch('/api/stations')
    .then(response => response.json())
    .then(stations => {
        console.log("Station data: ", stations);
        
        // Create markers for each station
        stations.forEach(station => {
            L.marker([station.latitude, station.longitude])
                .addTo(map)
                .bindPopup(`
                    <div class="station-popup">
                        <b>${station.nom}</b><br>
                        Opérateur: ${station.operateur}<br>
                        ${station.shop ? 'Shop: ' + station.shop : ''}
                    </div>
                `);
        });
    })
    .catch(error => console.error('Error fetching stations:', error));