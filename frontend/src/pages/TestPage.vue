<template>
  <div id="dice-container">
    <button @click="rollDice" id="roll-button">Roll Dice</button>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue';
import DiceBox from '@3d-dice/dice-box';

export default {
  setup() {
    const diceBoxRef = ref(null);
    let diceBoxInstance = null;

    onMounted(() => {
      diceBoxInstance = new DiceBox(diceBoxRef.value, {
        assetPath: '/assets/',
        scale: 10,
      });

      diceBoxInstance.init().then(() => {
        console.log('DiceBox initialized');
      }).catch((error) => {
        console.error('Error initializing DiceBox:', error);
      });
    });

    const rollDice = () => {
      if (diceBoxInstance) {
        diceBoxInstance.roll("5d20").then((results) => {
          const values = results.map(result => result.value);
          const rollString = values.join(' + ');
          const sum = values.reduce((acc, val) => acc + val, 0);
          console.log(`Roll results: ${rollString} = ${sum}`);
        }).catch((error) => {
          console.error('Error during roll:', error);
        });
      } else {
        console.error('DiceBox is not initialized yet.');
      }
    };

    return {
      diceBoxRef,
      rollDice
    };
  }
};
</script>

<style>
#roll-button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
}
.dice-box-canvas {
  width: 50%;
  height: 50%;
  background-size: cover;
  border: 1px solid #ccc;
}
</style>
