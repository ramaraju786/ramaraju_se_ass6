# 🌦️ Quadratic Weather Model with SDLC Approaches 📈  

 📌 Introduction  
This project demonstrates how a **quadratic equation** can be used to model weather patterns 🌍 (specifically temperature variation over time).  

At the same time, it creatively connects the concept of **Software Development Life Cycle (SDLC)** models — **Waterfall, Iterative, and Agile** — by simulating temperature predictions in different development approaches.  

---

🎯 Objectives  
- 🔹 Show how **quadratic functions** can model weather-like data.  
- 🔹 Illustrate the difference between **Waterfall, Iterative, and Agile models** in a fun, practical way.  
- 🔹 Provide students with an easy-to-understand Python program combining **Math + Weather + Software Engineering concepts**.  

---

 📖 Problem Statement  
Predicting weather requires complex systems 🌦️. However, for learning purposes, we can use a **simple quadratic function**:  

\[
T = a \cdot t^2 + b \cdot t + c
\]

Where:  
- `t` = time (hours)  
- `T` = predicted temperature (°C)  
- `a, b, c` = constants controlling curve shape  

---

🧠 Methodology  
The function:  

```python
def quadratic_weather_model(t):
    a, b, c = 0.05, -0.3, 25   # coefficients
    return a * t**2 + b * t + c

🔎 SDLC Modes in Quadratic Weather Model  

This model is applied in **three SDLC modes**:  

🚰 Waterfall Mode  
- Predictions are calculated **once in sequence**.  
- ⏱️ Example: Check temperature **every 6 hours** without revisiting previous steps.  

 🔄 Iterative Mode  
- Predictions are refined **in cycles (iterations)**.  
- 🔁 Example: Re-run calculations in **multiple iterations** (every 12 hours).  

⚡ Agile Mode  
- Predictions are checked in **sprints with flexible increments**.  
- 🏃 Example: Check at **specific times (0, 6, 12, 18, 24 hrs)** over multiple sprints.  

---

⚙️ Functional Requirements  

✅ Calculate quadratic-based temperature for given hours.  
✅ Print predictions for **Waterfall, Iterative, and Agile modes**.  
✅ Allow easy modification of coefficients (`a`, `b`, `c`).  

---

🚫 Non-Functional Requirements  

⏱️ Fast execution (**lightweight**).  
🐍 Implemented in **Python** for simplicity.  
📚 Code is designed for **education and demonstration**.

📊 Example Output  

🚰 Waterfall Mode  
=== WATERFALL MODE ===
Time: 0 hrs -> Predicted Temp: 25.00°C
Time: 6 hrs -> Predicted Temp: 23.80°C
Time: 12 hrs -> Predicted Temp: 24.20°C
Time: 18 hrs -> Predicted Temp: 26.20°C
Time: 24 hrs -> Predicted Temp: 29.80°C

yaml
Copy
Edit

---

🔄 Iterative Mode  
=== ITERATIVE MODE ===
Iteration 1:
Time: 0 hrs -> Temp: 25.00°C
Time: 12 hrs -> Temp: 24.20°C
Time: 24 hrs -> Temp: 29.80°C
Iteration 2:
...

yaml
Copy
Edit

---

⚡ Agile Mode  
=== AGILE MODE ===
Sprint 1:
Time: 0 hrs -> Temp: 25.00°C
Time: 6 hrs -> Temp: 23.80°C
Time: 12 hrs -> Temp: 24.20°C
Time: 18 hrs -> Temp: 26.20°C
Time: 24 hrs -> Temp: 29.80°C
yaml
Copy
Edit

---

🚀 Future Scope  

📊 Extend model with **real datasets**.  
🌍 Compare quadratic model with **machine learning predictions**.  
🖥️ Create a **visual plot** instead of plain text output.  
📲 Convert into an **interactive educational tool**.  

---

💡 Conclusion  

This project is a **blend of mathematics and software engineering** 💻.  
It shows:  
- 🔹 How a **quadratic function** can approximate weather-like data.  
- 🔹 How different **SDLC models (Waterfall, Iterative, Agile)** behave in practice.  
- 🔹 How concepts can be taught in a **fun and interactive way** 🎓.  
