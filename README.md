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

### Syncing your repository with the upstream
1. In your remote repository on Github, click sync fork and then click update to update your repository to the latest commit in the upstream repository.
2. To update the cloned repository in your system, type <code>git pull</code> by opening the terminal inside your project folder.

### Uploading Files
Mentees are required to upload their solutions to assignments within the respective deadlines. To upload files, they may either use Github or the following command lines:
1. Stage the files for commit using the <code>git add </code>command. <code>git add filename1 filename2</code> for specific files and <code>git add . </code> for all files.
2. Verify the files to be modified using : <code>git status</code> command.
3. Use <code>git reset filename</code> to prevent a file from getting staged. Or include the filename in the .gitignore file.
4. Commit the files using the <code>git commit</code> command. <code>git commit -m "Commit message" </code>.
5. Push the files into your main branch/ other branches. <code>git push origin main</code>
6. When you add files for the first time, create a pull request using Github.

### Setup Python Virtual Environment
1. Install virtualenv using the following command: <code> pip install virtualenv</code>
2. Navigate to your project directory. <code> cd Intro-to-ML-and-DL</code> . This may differ according to the location in your system.
3. Create a new virtual environment. <code> virtualenv venv </code> . You can replace venv with any name.
4. Activate the virtual environment. On Windows , <code>venv\Scripts\activate.bat</code>. On Linux/macOS , <code>source venv/bin/activate</code>.
5. Run the following command : <code> pip install -r requirements.txt</code>

### Happy Coding!!!
