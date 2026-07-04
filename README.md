# Production-Grade Core Python Engineering Suite

A collection of 9 modular, backend utility applications showcasing clean architecture, input safety, security constraints, and interactive UIs.

## Architecture Highlights

* **Project 1: To-Do System Engine** — Backed by JSON persistence and explicit file-I/O safety nets.
* **Project 2: AST Math Calculator** — Evaluates string inputs securely via Abstract Syntax Trees (`ast.parse`) instead of raw `eval()`.
* **Project 3: Live Weather Pipeline** — Connects to remote REST APIs using the `requests` layer with adaptive connection timeout handling.
* **Project 4: CSPRNG Password Generator** — Cryptographically secure generation utilizing the OS-linked `secrets` module.
* **Project 5: OOP Academic Quiz Engine** — Constructed around strict Object-Oriented principles to decouple data nodes from processing loops.
* **Project 6: Relational Expense Ledger** — Utilizing an embedded SQLite3 relational database, fortified against SQL injections using parametrized queries.
* **Project 7: Data Mining Web Scraper** — Processes explicit DOM elements using `BeautifulSoup4` with client header emulation.
* **Project 8: Graphical Snake Game** — Implemented using Python's native `turtle` graphics library with clean frame buffers and safety wrappers for window closing routines.
* **Project 9: Media Streaming Core Simulation** — Handles programmatic audio player queue logic using dynamic indexing state pointers.
