// script.js

// ==========================
// VARIABLES
// ==========================
let finalTranscript = "";
let seconds = 0;
let timerInterval;
let recognition;

// ==========================
// START RECORDING
// ==========================
function startRecording() {
    // Reset timer & transcript if starting fresh
    seconds = 0;
    finalTranscript = "";
    document.getElementById("timer").innerText = "Time: 0s";
    document.getElementById("textInput").value = "";

    // Start timer
    timerInterval = setInterval(() => {
        seconds++;
        document.getElementById("timer").innerText = "Time: " + seconds + "s";
    }, 1000);

    // Check browser support
    if (!('webkitSpeechRecognition' in window)) {
        alert("Speech recognition not supported in this browser.");
        return;
    }

    // Initialize recognition
    recognition = new webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.interimResults = true;
    recognition.continuous = true;

    recognition.onresult = (event) => {
        let interimTranscript = "";
        for (let i = event.resultIndex; i < event.results.length; i++) {
            if (event.results[i].isFinal) {
                finalTranscript += event.results[i][0].transcript + " ";
            } else {
                interimTranscript += event.results[i][0].transcript;
            }
        }
        document.getElementById("textInput").value = finalTranscript + interimTranscript;
    };

    recognition.onerror = (event) => {
        console.error("Speech recognition error:", event.error);
    };

    recognition.start();
}

// ==========================
// STOP RECORDING
// ==========================
function stopRecording() {
    if (recognition) {
        recognition.stop();
    }
    clearInterval(timerInterval); // stop timer
}

// ==========================
// SUBMIT FORM
// ==========================
function submitForm() {
    const text = document.getElementById("textInput").value.trim();
    if (!text) {
        alert("Please provide an answer before analyzing.");
        return;
    }
    document.getElementById("hiddenText").value = text;
    document.getElementById("hiddenForm").submit();
}

// ==========================
// THEME TOGGLE
// ==========================
function toggleTheme() {
    document.body.classList.toggle("dark");
    // Save preference to localStorage (optional)
    if (document.body.classList.contains("dark")) {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.setItem("theme", "light");
    }
}

// ==========================
// APPLY SAVED THEME ON LOAD
// ==========================
window.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        document.body.classList.add("dark");
    }
});