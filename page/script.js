const n = document.getElementById("n");
const realResult = document.getElementById("real-result");
console.log("ok");
const limit = 2000;

n.addEventListener("input", (e) => {
    const primeN = e.target.value
    const index = Math.ceil(primeN / 5000);

    console.log("ok");

    if(index > limit) {
        realResult.textContent = "No data";
    }

    fetch(`../prime_number_json/prime_numbers${index}.json`)
        .then(res => res.json())
        .then(data => {
            realResult.textContent = `${data[primeN]}`;
        });
});