# AI-Powered-Study-Assistant-CLI
An AI-based CLI Study Assistant built using Python and the Gemini API.

---

# Features

* Generates structured learning roadmaps
* Interactive follow-up question support
* Compact AI-generated study guidance
* Gemini API integration
* Environment variable support using `.env`

---

# Technologies Used

* Python
* Gemini API
* google-genai
* python-dotenv

---

# Project Structure

```bash
AI-Powered-Study-Assistant-CLI/
│
├── assistant.py
├── .env
├── requirements.txt
└── README.md
```

---
## Prompt Design Questions

### 1. What role did you assign in your system prompt, and why did you choose that framing?

The system prompt assigns the role **"Master Learning Strategist and Curriculum Designer."**
This framing was chosen to make the AI behave like an expert educator who creates structured and progressive learning roadmaps. It helps the model focus on skill progression, concise planning, and practical topic sequencing instead of giving random or overly detailed explanations.

---

### 2. What format did you specify for the study plan output, and how did you enforce it in the prompt?

#For Roadmap Generation and introduction.

When the user provides a topic, you must output a structured study plan adhering strictly to the following formatting rules:
1. Use Markdown headers for the main sections.
2. Provide a list of essential subtopics arranged in a logical, recommended learning order.
3. For each subtopic, provide description explaining what it is.

OUTPUT FORMAT:
(Topic Name):

~ Subtopic : 
    Discription
~(All the subtopic like this)

Roadmap :

~ All the topics piority wise.
~ How much min time we have to give for particular topics, difficulty and where to learn.

---

### 3. What happens if you remove the system prompt entirely — how does the output change?

Without the system prompt, the AI generates a much less structured response and often gives long explanations instead of a concise roadmap. The learning stages become inconsistent, formatting changes, and the output may include unnecessary details or motivational text.

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Bobbykumar5158/AI-Powered-Study-Assistant-CLI
```

## 2. Move Into Project Folder

```bash
cd AI-Powered-Study-Assistant-CLI
```

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```


# Setup API Key

Create a `.env` file in the project folder.

```env
GEMINI_API_KEY=your_api_key_here
```

---

# Run the Program

```bash
python assistant.py
```

---

# How It Works

1. User enters a study topic.
2. AI give intoduction about it and subtopics then it generates roadmap.
3. User can ask follow-up questions (if it is not related to previous topic it will generate new roadmap).
4. AI responds briefly with study guidance.
5. Session statistics are displayed at the end(Summary).

---

# Working

```bash
================================================================================
************************ AI-Powered-Study-Assistant-CLI ************************
================================================================================
User (type 'exit' or 'quit' to and chat) : Large Language Model
Large Language Model:

~ Foundational Concepts:
    Understanding Natural Language Processing basics (tokenization, embeddings) and core deep learning concepts (neural networks, backpropagation).
~ Transformer Architecture:
    Delving into self-attention mechanisms, multi-head attention, encoder-decoder structure, and positional encoding – the backbone of LLMs.
~ Pre-training & Fine-tuning:
    Learning about unsupervised pre-training objectives (e.g., masked language modeling) and adapting models for specific tasks via supervised fine-tuning.
~ Scaling Laws & Model Size:
    Exploring how model performance scales with data, parameters, and compute, and the implications of massive model sizes.
~ Applications & Ethics:
    Investigating practical uses of LLMs (e.g., text generation, summarization) and critical ethical considerations (bias, safety, misuse).

Roadmap:

~ Foundational Concepts: 60 min, Easy, Online courses/NLP textbooks.
~ Transformer Architecture: 120 min, Medium, Hugging Face documentation, research papers.
~ Pre-training & Fine-tuning: 90 min, Medium, Online tutorials, PyTorch/TensorFlow docs.
~ Scaling Laws & Model Size: 45 min, Medium, Research papers, blog posts.
~ Applications & Ethics: 30 min, Easy, AI ethics discussions, tech blogs.

================================================================================

User (type 'exit' or 'quit' to end chat) : total hrs required

-   Total estimated study time: 5 hours 45 minutes.
-   This is a general guideline; actual time may vary based on prior knowledge and learning pace.

================================================================================

User (type 'exit' or 'quit' to end chat) : explain transformer architecture

-   **Self-Attention Mechanism:** Allows the model to weigh the importance of different words in the input sequence when processing each word, capturing long-range dependencies.
-   **Multi-Head Attention:** Multiple self-attention layers run in parallel, enabling the model to focus on different parts of the input sequence and gather diverse information.
-   **Encoder-Decoder Structure:**
    -   **Encoder:** Processes the input sequence, creating a rich representation. Comprises multiple identical layers.
    -   **Decoder:** Generates the output sequence, attending to the encoder's output and previously generated tokens.
-   **Positional Encoding:** Adds information about the absolute or relative position of tokens in the sequence, as self-attention alone is permutation-invariant.
-   **Feed-Forward Networks:** A simple neural network applied independently to each position in the sequence after attention, adding non-linearity.
-   **Residual Connections & Layer Normalization:** Used throughout the architecture to facilitate training deeper networks by ensuring stable gradient flow.

 ================================================================================

 User (type 'exit' or 'quit' to end chat) : where i can learn this

-   **Hugging Face Documentation:** Excellent, practical guides and tutorials, especially their "Transformers" library.
-   **"Attention Is All You Need" Paper:** The original research paper (Vaswani et al., 2017) is the definitive source, though technically dense.
-   **Illustrated Transformer Blog Post:** Jay Alammar's blog provides highly visual and intuitive explanations.
-   **Online Courses:** DeepLearning.AI's "Natural Language Processing with Attention Models" or similar specialized NLP courses.
-   **YouTube Tutorials:** Many educators provide visual breakdowns of the architecture (e.g., StatQuest, AI Explained).

 ================================================================================

 User (type 'exit' or 'quit' to end chat) : yt channels

-   **StatQuest with Josh Starmer:** Provides highly visual and intuitive explanations of complex machine learning concepts, including attention.
-   **AI Explained:** Offers clear, conceptual breakdowns of cutting-edge AI topics and architectures like Transformers.
-   **Arxiv Insights:** Explains research papers, including those on Transformer variants, in an accessible manner.
-   **3Blue1Brown:** While not specifically focused on Transformers, his neural network series provides foundational understanding that helps grasp advanced architectures.
-   **CodeEmporium:** Often has practical, code-focused explanations of deep learning models.

===============================================================================

User (type 'exit' or 'quit' to end chat) : welcome

My role is to help students break down complex topics into clear, actionable study roadmaps. Please provide your next topic or a question about the current roadmap.

================================================================================

User (type 'exit' or 'quit' to end chat) : python language

Python Language:

~ Basics & Syntax:
    Understanding variables, data types (int, float, string, bool), basic operators, and control flow (if/else, loops).
~ Data Structures:
    Learning about fundamental built-in structures: lists, tuples, dictionaries, and sets, and their common operations.
~ Functions & Modules:
    Defining and calling functions, understanding scope, and importing/using modules and packages.
~ Object-Oriented Programming (OOP):
    Grasping concepts of classes, objects, inheritance, and polymorphism for structured code.
~ File I/O & Error Handling:
    Reading from and writing to files, and implementing `try-except` blocks for robust error management.

Roadmap:

~ Basics & Syntax: 90 min, Easy, Codecademy, Python Docs.
~ Data Structures: 120 min, Easy, W3Schools, Python Docs.
~ Functions & Modules: 90 min, Medium, Real Python, YouTube tutorials.
~ Object-Oriented Programming (OOP): 150 min, Medium, GeeksforGeeks, specialized OOP tutorials.
~ File I/O & Error Handling: 60 min, Easy, Automate the Boring Stuff, Python Docs.

================================================================================

User (type 'exit' or 'quit' to end chat) : explain oops

-   **Object-Oriented Programming (OOP):** A programming approach that organizes software design around data, or objects, rather than functions and logic.
-   **Core Idea:** Objects combine related data (attributes) and behavior (methods) into a single unit.
-   **Classes as Blueprints:** Classes act as templates from which individual objects are created.
-   **Four Pillars:**
    -   **Encapsulation:** Bundling data and methods that operate on the data within a single unit (class), restricting direct access to some of an object's components.
    -   **Inheritance:** Allows classes to acquire properties and behaviors from other classes, forming a hierarchical structure.
    -   **Polymorphism:** Enables objects of different classes to be treated as objects of a common superclass, allowing methods to behave differently based on the object's type.
    -   **Abstraction:** Showing only essential information and hiding complex implementation details.

================================================================================

User (type 'exit' or 'quit' to end chat) : Thermodynamics

Thermodynamics:

~ Fundamental Concepts:
    Defining system, surroundings, boundary, state variables (P, V, T), intensive/extensive properties, and equilibrium.
~ Zeroth Law & Temperature:
    Understanding thermal equilibrium and the concept of temperature as a measure of thermal energy.
~ First Law of Thermodynamics:
    Conservation of energy, internal energy, heat, work, and enthalpy.
~ Second Law of Thermodynamics:
    Entropy, spontaneity, heat engines, refrigerators, and the direction of natural processes.
~ Third Law of Thermodynamics:
    Absolute zero temperature and its implications for entropy.

Roadmap:

~ Fundamental Concepts: 60 min, Easy, Physics textbooks, Khan Academy.
~ Zeroth Law & Temperature: 30 min, Easy, HyperPhysics, university lectures.
~ First Law of Thermodynamics: 120 min, Medium, MIT OpenCourseWare, chemistry textbooks.
~ Second Law of Thermodynamics: 150 min, Medium, Crash Course Physics, specialized thermodynamics texts.
~ Third Law of Thermodynamics: 45 min, Easy, Online encyclopedias, general chemistry resources.

================================================================================

User (type 'exit' or 'quit' to end chat) : applied maths 1 in btech 1sr year

Applied Maths 1 (B.Tech 1st Year):

~ Differential Calculus:
    Limits, continuity, differentiability, derivatives of various functions, Rolle's and Mean Value Theorems, applications (maxima/minima).
~ Integral Calculus:
    Indefinite and definite integrals, methods of integration, applications (area, volume).
~ Matrices & Determinants:
    Types of matrices, operations, determinants, inverse of a matrix, rank, eigenvalues, and eigenvectors.
~ Ordinary Differential Equations (ODEs):
    First-order ODEs (variable separable, exact, linear, Bernoulli), higher-order linear ODEs with constant coefficients.
~ Multivariable Calculus:
    Partial differentiation, Euler's theorem, total derivative, Jacobian, maxima/minima of functions of several variables.

Roadmap:

~ Differential Calculus: 180 min, Medium, NPTEL, Engineering Math textbooks.
~ Integral Calculus: 180 min, Medium, Khan Academy, Schaum's Outlines.
~ Matrices & Determinants: 150 min, Medium, Gilbert Strang lectures, university notes.
~ Ordinary Differential Equations (ODEs): 210 min, Hard, Paul's Online Notes, Differential Equations textbooks.
~ Multivariable Calculus: 150 min, Hard, MIT OpenCourseWare (Multivariable Calculus), tutorial videos.

================================================================================

 User (type 'exit' or 'quit' to end chat) : yt channels for this

-   **NPTEL (National Programme on Technology Enhanced Learning):** Offers comprehensive course series specifically designed for engineering mathematics, often aligning with B.Tech syllabi.
-   **Khan Academy:** Provides structured lessons and practice problems for Differential Calculus, Integral Calculus, Matrices, and ODEs.
-   **Professor Leonard:** Excellent for in-depth, traditional lecture-style learning for single-variable and multivariable calculus, as well as differential equations.
-   **3Blue1Brown:** Offers highly visual and intuitive explanations for Linear Algebra (Matrices & Determinants) and some Calculus concepts, building strong foundational understanding.
-   **The Organic Chemistry Tutor:** Despite the name, has extensive playlists covering various math topics including calculus, differential equations, and linear algebra with clear examples.
-   **MIT OpenCourseWare (e.g., 18.01SC Single Variable Calculus, 18.02SC Multivariable Calculus, 18.03SC Differential Equations):** Provides full university lecture series.

================================================================================

User (type 'exit' or 'quit' to end chat) : explain differential calculus

-   **Focus:** Studies the rates at which quantities change and the slopes of curves.
-   **Limits:** The foundational concept, describing the value a function approaches as the input approaches a certain value.
-   **Continuity:** A function is continuous if its graph can be drawn without lifting the pen; formally, a limit exists and equals the function's value at that point.
-   **Differentiability:** A function is differentiable at a point if it has a well-defined tangent line at that point; implies continuity.
-   **Derivatives:** The central tool; represents the instantaneous rate of change of a function with respect to its independent variable, or the slope of the tangent line to the curve at a given point.
-   **Applications:** Used to find maxima and minima (optimization), rates of change in physics (velocity, acceleration), and approximation of functions.
-   **Key Theorems:** Rolle's Theorem and Mean Value Theorem provide insights into the behavior of differentiable functions over intervals.

================================================================================

User (type 'exit' or 'quit' to end chat) : exit

================================================================================

# Summary

-   **Large Language Model:**
    -   Focuses on NLP basics, Transformer architecture, pre-training/fine-tuning strategies, scaling principles, and ethical considerations for large AI language models.
-   **Python Language:**
    -   Covers foundational Python concepts including syntax, core data structures (lists, dicts), functions, Object-Oriented Programming (OOP) principles, and file handling.
-   **Thermodynamics:**
    -   Explores the relationship between heat and energy, delving into the four laws of thermodynamics governing energy conservation, entropy, and the direction of spontaneous processes.
-   **Applied Maths 1 (B.Tech 1st Year):**
    -   Encompasses essential engineering math topics: Differential Calculus (rates of change), Integral Calculus (accumulation), Matrices & Determinants (linear algebra), Ordinary Differential Equations, and Multivariable Calculus.

TOTAL QUES ASKED : 12
================================================================================
******************** Thank You for Using our AI assistant. *********************
================================================================================
```
---


# Author

Developed using Python and Gemini AI.