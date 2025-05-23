<template>
  <div class="flex gap-6 items-start">
    <div
      id="dice-container"
      class="w-[400px] h-[400px] border border-gray-300 flex-shrink-0"
    ></div>

    <div class="flex flex-col gap-4 w-44">
      <input
        id="dice-input"
        type="text"
        v-model="diceInput"
        class="border border-gray-300 rounded px-3 py-2 text-base"
      />
      <button
        @click="rollDice"
        id="roll-button"
        class="bg-green-600 text-white rounded px-4 py-2 text-base hover:bg-green-700 transition"
      >
        Roll Dice
      </button>
      <div v-if="resultText" class="mt-2 text-sm text-gray-700 font-medium">
        {{ resultText }}
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import DiceBox from '@3d-dice/dice-box-threejs';

export default {
  setup() {
    const diceInput = ref('3d20');
    const resultText = ref('');
    let diceBoxInstance = null;

    onMounted(async () => {
      diceBoxInstance = new DiceBox('#dice-container', {
        light_intensity: 1,
        gravity_multiplier: 300,
        baseScale: 80,
        strength: 4,
        theme_customColorset: {
          background: "#ffdc9f",
          foreground: "#000000",
          texture: "none",
          material: "plastic"
        },
        onRollComplete: (results) => {
          const allValues = results.sets.flatMap(set => set.rolls.map(r => r.value));
          const total = allValues.reduce((a, b) => a + b, 0);
          const formula = allValues.join('+');
          resultText.value = `${formula} = ${total}`;
        }
      });

      await diceBoxInstance.initialize();
    });

    onBeforeUnmount(() => {
      diceBoxInstance?.dispose();
      diceBoxInstance = null;
    });

    const rollDice = () => {
      resultText.value = '';
      diceBoxInstance.roll(diceInput.value.trim());
    };

    return { diceInput, rollDice, resultText };
  },
};
</script>

<style>
</style>
