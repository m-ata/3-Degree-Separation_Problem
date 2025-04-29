# 🎬 3 Degrees of Separation with BFS

This project solves the **"3 Degrees of Separation"** problem using the **Breadth-First Search (BFS)** algorithm, inspired by the "Six Degrees of Kevin Bacon" concept. It finds the shortest connection path between two actors based on shared movie appearances.

## 🧠 Problem Description

Given a dataset of actors and movies:
- **Nodes**: Actors (people)
- **Edges**: Movies shared with other actors
- **Goal**: Find the shortest sequence of co-starring relationships using BFS

### Example Path:
- Emma Watson → Daniel Radcliffe (Harry Potter series)
- Daniel Radcliffe → Tom Hanks (The Circle)

- 
## 🗂️ Project Structure
- Degrees-of-separation/
- ├── README.md # Documentation
- ├── degrees.py # Main program
- ├── util.py # BFS implementation
- ├── large/ # Full dataset
- │ ├── people.csv
- │ ├── movies.csv
- │ └── stars.csv
- └── small/ # Test dataset
- ├── people.csv
- ├── movies.csv
- └── stars.csv

- 
## 📁 Dataset Format
- **people.csv**: `id`, `name`, `birth`
- **movies.csv**: `id`, `title`, `year`
- **stars.csv**: `person_id`, `movie_id` (many-to-many relationships)

## ⚙️ How It Works
1. Loads CSV data into memory
2. Builds a graph with actors as nodes and shared movies as edges
3. Uses BFS to find the shortest path
4. Outputs human-readable connection path

## 🚀 Getting Started

### Requirements
- Python 3.7+

### Installation
```bash
git clone https://github.com/m-ata/3-Degree-Separation_Problem.git
cd 3-Degree-Separation_Problem
```
#### Usage
- For small test dataset
```bash
python degrees.py small
```
- For large dataset
```bash
python degrees.py large
```
## Example session output:
- Name: Emma Watson
- Name: Jennifer Lawrence

# 3 degrees of separation.
- 1: Emma Watson and Michael Gambon starred in Harry Potter and the Deathly Hallows: Part 2
- 2: Michael Gambon and Charlotte Rampling starred in Paris by Night
- 3: Charlotte Rampling and Jennifer Lawrence starred in Red Sparrow

## 🛠️ Implementation Details

### degrees.py
- Main program logic
- Handles data loading and pathfinding
- Manages user input/output

### util.py
- Contains `Node` class for graph representation
- Implements `QueueFrontier` class for BFS operations

## 🔍 Limitations

- **Unweighted relationships**: All connections treated equally
- **Name ambiguity**: No disambiguation for identical names
- **Basic interface**: Console-only interaction
- **Scalability**: May struggle with extremely large datasets

## 🚀 Future Improvements

- [ ] **Name disambiguation**: Handle duplicate names
- [ ] **Weighted edges**: Incorporate:
  - Screen time metrics
  - Number of collaborations
  - Movie ratings/relevance
- [ ] **Web interface**:
  - Interactive visualization
  - AJAX-powered searches
- [ ] **Performance**:
  - Optimize for large datasets
  - Add caching mechanisms
- [ ] **Additional features**:
  - Degree centrality metrics
  - Most common connectors
  - Timeline visualization

## 🙌 Acknowledgements
- Inspired by Harvard's CS50 AI course
- Based on the "Six Degrees of Kevin Bacon" concept


## 📜 License
NO License 
