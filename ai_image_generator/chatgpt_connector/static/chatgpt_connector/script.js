const generateBtn = document.querySelector("#generateBtn");
const gridContainer = document.querySelector("#gridContainer");
const picNums = new Set();

function generateRandomPics() {
  const randNum = Math.floor(Math.random() * 1000) + 1;

  // Prevent duplicate image
  while (picNums.has(randNum)) {
    randNum = Math.floor(Math.random() * 1000) + 1;
  }

  const imgUrl = `https://picsum.photos/500?random=${randNum}`;
  const img = document.createElement("img");
  img.setAttribute("id", "imgGrid");
  img.src = imgUrl;

  gridContainer.appendChild(img);
}

generateBtn.addEventListener("click", generateRandomPics);
