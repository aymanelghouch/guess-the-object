const fileInput = document.getElementById("file-input");
const preview = document.getElementById("preview");
const uploadText = document.getElementById("upload-text");
const predictBtn = document.getElementById("predict-btn");
const errorBox = document.getElementById("error");
const results = document.getElementById("results");
const topLabel = document.getElementById("top-label");
const topConf = document.getElementById("top-conf");
const others = document.getElementById("others");

// 1. El usuario elige una imagen
fileInput.addEventListener("change", () => {
  const file = fileInput.files[0];
  if (!file) return;

  preview.src = URL.createObjectURL(file);
  preview.hidden = false;
  uploadText.hidden = true;
  predictBtn.disabled = false;
  results.hidden = true;
  errorBox.hidden = true;
});

// 2. El usuario pulsa "Identificar objeto"
predictBtn.addEventListener("click", async () => {
  const file = fileInput.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append("file", file); // "file" = nombre del campo que espera FastAPI

  setLoading(true);
  errorBox.hidden = true;

  try {
    const response = await fetch("/predict", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const err = await response.json();
      throw new Error(err.detail || "Error del servidor");
    }

    const data = await response.json();
    showResults(data.predictions);
  } catch (e) {
    showError(e.message);
  } finally {
    setLoading(false);
  }
});

function setLoading(isLoading) {
  predictBtn.disabled = isLoading;
  predictBtn.textContent = isLoading ? "Analizando..." : "Identificar objeto";
}

function showError(message) {
  errorBox.textContent = message;
  errorBox.hidden = false;
  results.hidden = true;
}

// "tabby, tabby cat" -> "tabby"
function cleanLabel(label) {
  return label.split(",")[0];
}

function formatPercent(x) {
  return (x * 100).toFixed(1) + "%";
}

function showResults(predictions) {
  const [best, ...rest] = predictions;

  topLabel.textContent = cleanLabel(best.label);
  topConf.textContent = formatPercent(best.confidence);

  others.innerHTML = "";
  for (const p of rest) {
    const li = document.createElement("li");

    const name = document.createElement("span");
    name.textContent = cleanLabel(p.label);

    const bar = document.createElement("div");
    bar.className = "bar";
    const fill = document.createElement("div");
    fill.className = "fill";
    fill.style.width = `${p.confidence * 100}%`;
    bar.appendChild(fill);

    const pct = document.createElement("span");
    pct.textContent = formatPercent(p.confidence);

    li.append(name, bar, pct);
    others.appendChild(li);
  }

  results.hidden = false;
}