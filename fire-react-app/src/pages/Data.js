import React from "react";
import { MapContainer, TileLayer } from 'react-leaflet';
import "./Data.css";

function Data() {
    return (
     <MapContainer center={[35, -100]} zoom={5}scrollWheelZoom={true}>
              <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
              />
            </MapContainer>
  );
}

export default Data;