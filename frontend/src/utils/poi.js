// poi.js
import IconCity from "@/icons/IconCity.vue";
import IconTown from "@/icons/IconTown.vue";
import IconVillage from "@/icons/IconVillage.vue";

export const POI_TYPES = [
  {
    name: 'city',
    icon: IconCity,
    count: 3,
    allowedTerrains: ['meadow'],
    spreadRadius: 8,
  },
  {
    name: 'town',
    icon: IconTown,
    count: 6,
    allowedTerrains: ['meadow'],
    spreadRadius: 4,
  },
  {
    name: 'village',
    icon: IconVillage,
    count: 16,
    allowedTerrains: ['meadow', 'forest', 'swamp'],
    spreadRadius: 3,
  },
];
