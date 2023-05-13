# Intro-to-ML-and-DL
**Intro-to-ML-and-DL** is a repository for the 2023 Summer Project offered by the Stamatics Society of IIT Kanpur.
This repository shall contain the week-wise lessons, resources and assignments for the project. 

## Installation
### Requirements
1. Python 3.6 or higher
2. pip
### Setup Git
1. First check if Git is already installed. In the terminal / command prompt type: 
  <pre><code>git --version</code></pre>
2. If Git is not installed, <a href="https://git-scm.com/downloads">download Git</a>.
3. Set up your local Git profile in the terminal:
<pre><code>git config --global user.name "your-name"
git config --global user.email "your-email"</code></pre>
4. To check if Git is correctly configured you can type: <code>git config --list</code>

### Setup Project
1. Fork the repository.
2. Clone the repository. In your terminal, type:
  <pre><code>git clone https://github.com/your-username/Intro-to-ML-and-DL.git</code></pre>
3. Navigate to the repository directory : <code>cd Intro-to-ML-and-DL</code>
4. Set up a remote connection to the original repository
   <code>git remote add upstream https://github.com/Intro-to-ML-and-DL/Intro-to-ML-and-DL.git</code>
5. Verify that the remote connection : <code>git remote -v</code>. You would see two remote connections: origin (pointing to your forked repository) and upstream (pointing to the original repository).
6. Create a pull request in github.

### Setup Python Virtual Environment
1. Install virtualenv using the following command: <code> pip install virtualenv</code>
2. Navigate to your project directory. <code> cd Intro-to-ML-and-DL</code> . This may differ according to the location in your system.
3. Create a new virtual environment. <code> virtualenv venv </code> . You can replace venv with any name.
4. Activate the virtual environment. On Windows , <code>venv\Scripts\activate.bat</code>. On Linux/macOS , <code>source venv/bin/activate</code>.
5. Run the following command : <code> pip install -r requirements.txt</code>

### Happy Coding!!!
