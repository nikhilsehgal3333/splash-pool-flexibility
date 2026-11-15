[out:json][timeout:240];
area["ISO3166-2"="DE-SH"]->.sh;
(
  node["power"="generator"]["generator:source"="wind"](area.sh);
  way["power"="generator"]["generator:source"="wind"](area.sh);
);
out center tags;
