<template>
  <div class="flex flex-col items-center gap-4 p-4">
    <canvas
      ref="canvas"
      :width="canvasWidth"
      :height="canvasHeight"
      class="border border-black"
    ></canvas>
    <button
      @click="generateDungeon"
      class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition"
    >
      Сгенерировать подземелье
    </button>
  </div>
</template>

<script setup>
import {onMounted, ref} from 'vue';

const canvas = ref(null);
const ctx = ref(null);
const canvasWidth = 500;
const canvasHeight = 500;
const tileSize = 10;
const cols = canvasWidth / tileSize;
const rows = canvasHeight / tileSize;
let dungeon = [];

const generateRandomDungeon = () => {
  dungeon = Array.from({length: rows}, () =>
      Array(cols).fill(0).map(() => (Math.random() > 0.45 ? 1 : 0))
  );
};

const cellularAutomata = () => {
  const iterations = 5;

  for (let i = 0; i < iterations; i++) {
    dungeon = dungeon.map((row, y) =>
        row.map((cell, x) => {
          const neighbors = countNeighbors(x, y);
          if (cell === 1) {
            return neighbors >= 4 ? 1 : 0;
          } else {
            return neighbors >= 5 ? 1 : 0;
          }
        })
    );
  }

  fillDisconnectedRegions();
  connectRooms();
};

const countNeighbors = (x, y) => {
  let count = 0;
  for (let dy = -1; dy <= 1; dy++) {
    for (let dx = -1; dx <= 1; dx++) {
      if (dx === 0 && dy === 0) continue;
      const nx = x + dx;
      const ny = y + dy;
      if (nx >= 0 && nx < cols && ny >= 0 && ny < rows) {
        count += dungeon[ny][nx];
      }
    }
  }
  return count;
};

const fillDisconnectedRegions = () => {
  const visited = Array.from({length: rows}, () => Array(cols).fill(false));

  const dfs = (x, y) => {
    const stack = [[x, y]];
    while (stack.length > 0) {
      const [cx, cy] = stack.pop();
      if (visited[cy][cx]) continue;
      visited[cy][cx] = true;
      for (let dy = -1; dy <= 1; dy++) {
        for (let dx = -1; dx <= 1; dx++) {
          if (dx === 0 && dy === 0) continue;
          const nx = cx + dx;
          const ny = cy + dy;
          if (nx >= 0 && nx < cols && ny >= 0 && ny < rows && dungeon[ny][nx] === 1 && !visited[ny][nx]) {
            stack.push([nx, ny]);
          }
        }
      }
    }
  };

  for (let x = 0; x < cols; x++) {
    if (!visited[0][x] && dungeon[0][x] === 1) dfs(x, 0); // Верхний край
    if (!visited[rows - 1][x] && dungeon[rows - 1][x] === 1) dfs(x, rows - 1); // Нижний край
  }
  for (let y = 0; y < rows; y++) {
    if (!visited[y][0] && dungeon[y][0] === 1) dfs(0, y); // Левый край
    if (!visited[y][cols - 1] && dungeon[y][cols - 1] === 1) dfs(cols - 1, y); // Правый край
  }

  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      if (!visited[y][x]) dungeon[y][x] = 0;
    }
  }
};

const connectRooms = () => {
  const rooms = [];
  const visited = Array.from({length: rows}, () => Array(cols).fill(false));

  const dfsFindRoom = (x, y, room) => {
    const stack = [[x, y]];
    while (stack.length > 0) {
      const [cx, cy] = stack.pop();
      if (visited[cy][cx]) continue;
      visited[cy][cx] = true;
      room.push([cx, cy]);
      for (let dy = -1; dy <= 1; dy++) {
        for (let dx = -1; dx <= 1; dx++) {
          if (dx === 0 && dy === 0) continue;
          const nx = cx + dx;
          const ny = cy + dy;
          if (nx >= 0 && nx < cols && ny >= 0 && ny < rows && dungeon[ny][nx] === 1 && !visited[ny][nx]) {
            stack.push([nx, ny]);
          }
        }
      }
    }
  };

  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      if (dungeon[y][x] === 1 && !visited[y][x]) {
        const room = [];
        dfsFindRoom(x, y, room);
        rooms.push(room);
      }
    }
  }

  if (rooms.length < 2) return;

  for (let i = 0; i < rooms.length - 1; i++) {
    const roomA = rooms[i];
    const roomB = rooms[i + 1];

    const startA = roomA[Math.floor(Math.random() * roomA.length)];
    const startB = roomB[Math.floor(Math.random() * roomB.length)];

    let [x1, y1] = startA;
    let [x2, y2] = startB;

    while (x1 !== x2) {
      dungeon[y1][x1] = 1;
      x1 += x1 < x2 ? 1 : -1;
    }
    while (y1 !== y2) {
      dungeon[y1][x1] = 1;
      y1 += y1 < y2 ? 1 : -1;
    }
  }
};

const drawDungeon = () => {
  if (!ctx.value) return;
  ctx.value.clearRect(0, 0, canvasWidth, canvasHeight);
  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      ctx.value.fillStyle = dungeon[y][x] === 1 ? '#fff' : '#000';
      ctx.value.fillRect(x * tileSize, y * tileSize, tileSize, tileSize);
    }
  }
};

const generateDungeon = () => {
  generateRandomDungeon();
  cellularAutomata();
  drawDungeon();
};

onMounted(() => {
  ctx.value = canvas.value.getContext('2d');
  generateDungeon();
});
</script>

<style scoped>
</style>
