(function() {
    var map3 = L.map('networkmap').setView([51.462405, -0.066630], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map3);

    setTimeout(function() { map3.invalidateSize(); }, 300);

    const styleNetwork = {
        color: "#284ca8",  
        weight: 0.8
    };

    fetch('data/Network.geojson')
      .then(res => res.json())
      .then(data => {
          L.geoJson(data, {style: styleNetwork}).addTo(map3);
      });

    const Networktitle = L.control({ position: 'topright' });
    Networktitle.onAdd = function () {
        const div = L.DomUtil.create('div', 'maptitle');
        div.innerHTML = '<h4> South London Road Network</h4>';
        return div;
    };
    Networktitle.addTo(map3);

})();
