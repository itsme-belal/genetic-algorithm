# 🧬 Genetic Algorithm Implementations in Python

This repository contains multiple implementations of **Genetic Algorithms (GA)** in Python, starting from basic concepts to more advanced and optimized versions.

The goal of this project is to demonstrate how Genetic Algorithms evolve solutions over generations using selection, crossover, and mutation.

---

## 📌 What is a Genetic Algorithm?

A Genetic Algorithm is an optimization technique inspired by **natural selection**. It iteratively improves a population of candidate solutions based on their fitness.

---

## ⚙️ How It Works

1. Initialize a random population
2. Evaluate fitness of each individual
3. Select the best individuals (parents)
4. Perform crossover to create offspring
5. Apply mutation to introduce variation
6. Repeat the process for multiple generations

---

## 📂 Project Structure

```bash
.
├── basic_ga.py              # Simple GA (concept demonstration)
├── fixed_population_ga.py  # Maintains population size
├── improved_ga.py          # Better mutation & exploration
├── best_tracking_ga.py     # Tracks best solution across generations
├── final_ga.py             # Optimized GA with early stopping
```

---

## 🚀 Features

* Multiple GA versions (from beginner to advanced)
* Fitness-based selection
* Crossover and mutation operations
* Best solution tracking
* Early stopping mechanism
* Easy-to-understand code structure

---

## 🧠 Problem Solved

We use GA to maximize the function:

```
f(x) = x²
```

Where:

```
0 ≤ x ≤ 31
```

The optimal solution is:

```
x = 31 → f(x) = 961
```

---

## ▶️ How to Run

Make sure you have Python installed.

Run any version:

```bash
python basic_ga.py
```

or

```bash
python final_ga.py
```

---

## 📊 Example Output

```
Initial Population: [10, 21, 5, 30]

Generation 1...
Generation 2...

Final Best: 31
Fitness: 961
```

---

## ⚠️ Important Notes

* Genetic Algorithms are **stochastic** (random-based), so results may vary between runs.
* The final generation may not always contain the best solution.
* Best results are obtained by:

  * Increasing population size
  * Increasing number of generations
  * Tracking the best solution across all generations

---

## 📈 Applications of Genetic Algorithms

* Route Optimization (TSP)
* Machine Learning (feature selection, hyperparameter tuning)
* Game AI
* Robotics
* Finance (portfolio optimization)
* Engineering design problems

---

## 💡 Key Insight

> Genetic Algorithms do not require an exact formula — only a way to measure how good a solution is.

---

## 🛠️ Technologies Used

* Python
* Standard libraries (`random`)

---

## 📬 Contributing

Feel free to fork this repository, improve the implementations, or add new GA-based problems.

---

## ⭐ Support

If you found this helpful, consider giving the repo a ⭐

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/your-username
