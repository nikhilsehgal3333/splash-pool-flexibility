[out:json][timeout:180];
area["ISO3166-2"="DE-SH"]->.sh;
(
  nwr["leisure"="sports_centre"]["sport"~"swimming"](area.sh);
  nwr["leisure"="swimming_pool"](area.sh);
  nwr["leisure"="water_park"](area.sh);
  nwr["amenity"="public_bath"](area.sh);
  nwr["leisure"="swimming_area"](area.sh);
  nwr["sport"="swimming"]["leisure"!="sports_centre"]["leisure"!="swimming_pool"](area.sh);
);
out center tags;
