# 📚 Data Structures – Class Repository

This repository contains all the work completed for the Data Structures course. It includes theoretical analysis, practical exercises, midterm assignments, and in-class activities. The focus was on understanding and implementing core data structures, analyzing algorithmic complexity, and building hands-on projects that apply these structures in real use cases.

---

## ✅ Topics Covered

### 🧱 Data Structures Implemented
- **Arrays**
- **Stacks**
- **Queues**
- **Linked Lists**
  - Includes a reversal method
- **Binary Trees**
- **Binary Search Trees (BST)**
  - Includes a custom delete-node method and real use case in a Jupyter Notebook
- **AVL Trees**

### 📊 Time Complexity Experiments
- **Midterm I**: Compared complexity of search vs delete (`pop`) operations across structures.
- **Midterm II**: Analyzed AVL Trees vs Binary Search Trees in terms of time complexity.
- **Complejidad**: Tested time complexity with simple for-loop implementations:
  - Linear search (`O(n)`)
  - Product pair search (`O(n²)`)

### 💻 Projects & Practical Work
- **Geet (`MyGeet/`)**: A simplified Git clone with basic commands:
  - `init`, `add`, `commit`, etc
- **BST Use Case (`bst&tarea/`)**: Notebook demonstrating the delete operation in different scenarios.
- **CLI Homework (`Tarea_CLI/`)**: Used the `click` Python package to create a basic command-line interface with test commands.
- **Directory Tree Generator (`Directory Tree/`)**: Simulated directory scanning where file paths are nodes in a custom tree structure.
- **Linked List Reversal Tests (`reverse-ll/`)**: Created the method for reversing a linked list and it's tests.

---


## 📂 Repository Structure

```bash
Datos/
├── Complejidad/           → Time complexity tests (e.g., O(n), O(n²))
├── Directory Tree/         → Homework: generate tree based on file paths

Estructuras/
├── Arrays/                → Static array exercises
├── AVL/                   → AVL tree implementation
├── binary_tree/           → Basic binary tree structure
├── bst&tarea/             → Binary search tree + notebook with delete showcase
├── Lists/                 → Linked list implementations
├── Queues/                → Queue data structure
├── Stacks/                → Stack data structure

Midterm I/                 → Search vs delete (pop) complexity analysis
Midterm II/                → AVL vs BST complexity comparison  

MyGeet/                    → Mini Git system ("geet" project)  
reverse-ll/                → Linked list reversal implementation  

Tarea_CLI/                 → CLI exercise using click

.gitignore                 → Git ignored files  
README.md                  → You're here :)