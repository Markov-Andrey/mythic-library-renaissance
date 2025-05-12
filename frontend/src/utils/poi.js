// poi.js
import IconCity from "@/icons/IconCity.vue";
import IconTown from "@/icons/IconTown.vue";
import IconVillage from "@/icons/IconVillage.vue";
import IconRuin from "@/icons/IconRuin.vue";

export const POI_TYPES = [
  {
    name: 'city',
    icon: IconCity,
    density: 1,
    allowedTerrains: ['meadow'],
    spreadRadius: 8,
  },
  {
    name: 'town',
    icon: IconTown,
    density: 4,
    allowedTerrains: ['meadow'],
    spreadRadius: 4,
  },
  {
    name: 'village',
    icon: IconVillage,
    density: 10,
    allowedTerrains: ['meadow', 'forest', 'swamp'],
    spreadRadius: 3,
  },
  {
    name: 'ruin',
    icon: IconRuin,
    density: 3,
    allowedTerrains: ['meadow', 'forest', 'swamp', 'mountain', 'desert', 'savanna'],
    spreadRadius: 1,
  },
];
