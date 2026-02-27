let chart;

async function predictStock() {
    const ticker = document.getElementById("ticker").value;
    const days = document.getElementById("days").value;

    if (!ticker || !days) {
        alert("Please enter ticker and days.");
        return;
    }

    document.getElementById("loading").classList.remove("hidden");

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            ticker: ticker,
            days: days
        })
    });

    const data = await response.json();

    document.getElementById("loading").classList.add("hidden");

    document.getElementById("accuracy").innerText =
        "Model Accuracy: " + (data.accuracy * 100).toFixed(2) + "%";

    const ctx = document.getElementById("chart").getContext("2d");

    if (chart) {
        chart.destroy();
    }

    chart = new Chart(ctx, {
        type: "line",
        data: {
            labels: Array.from({ length: data.forecast.length }, (_, i) => "Day " + (i + 1)),
            datasets: [{
                label: "Predicted Price",
                data: data.forecast,
                borderColor: "#00ffcc",
                borderWidth: 2
            }]
        }
    });
}
