async function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    let responseText = document.getElementById("response");
    let loader = document.getElementById("loader");

    if (!userInput) {
        responseText.innerHTML = "Please enter a message.";
        return;
    }

    responseText.innerHTML = "";
    loader.style.display = "block";  // Show loader

    try {
        let response = await fetch("/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userInput })
        });

        let data = await response.json();
        responseText.innerHTML = data.response || "Error: No response received";
    } catch (error) {
        responseText.innerHTML = "Error connecting to server.";
    } finally {
        loader.style.display = "none";  // Hide loader
    }
}
