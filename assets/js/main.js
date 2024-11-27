
        const names = [];
        const resultsDiv = document.getElementById("results");

        document.getElementById("addNameButton").addEventListener("click", () => {
            const nameInput = document.getElementById("nameInput");
            const name = nameInput.value.trim();
            if (name && !names.includes(name)) {
                names.push(name);
                nameInput.value = '';
                nameInput.focus();
                resultsDiv.innerHTML = `<p>${name} added successfully! (${names.length} total)</p>`;
            } else {
                resultsDiv.innerHTML = `<p style="color: red;">Invalid or duplicate name!</p>`;
            }
        });

        document.getElementById("assignNumbersButton").addEventListener("click", () => {
            const iterations = document.getElementById("iterations").value;
            if (!iterations || iterations < 1) {
                alert("Please enter a valid number of iterations (at least 1).");
                return;
            }
            fetch("http://127.0.0.1:5000/assign-numbers", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ names, iterations: parseInt(iterations) }),
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.final_assignments) {
                        resultsDiv.innerHTML = "<h2>Final Assignments</h2>";
                        data.final_assignments.forEach((assignment) => {
                            const div = document.createElement("div");
                            div.className = "result-item";
                            div.textContent = `${assignment.name} -> ${assignment.number}`;
                            resultsDiv.appendChild(div);
                    });
                }
                    else{
                        resultsDiv.innerHTML = `<p style="color: red;">Error: ${data.error}</p>`;
                    }
                })
                .catch((error) => {
                    console.error("Error:", error);
                    resultsDiv.innerHTML = `<p style="color: red;">Error assigning numbers. Please try again.</p>`;
                });
        });
        document.getElementById("downloadButton").addEventListener("click", () => {
            window.location.href = "http://127.0.0.1:5000/download-results";
        });
