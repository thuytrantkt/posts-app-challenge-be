# Getting Started

1. **Set up pyenv environment**

   If you haven't installed pyenv yet, you can do so by following the instructions [here](https://github.com/pyenv/pyenv#installation).

   ```
   pyenv install 3.11.4
   pyenv virtualenv 3.11.4 slack-clone
   pyenv activate slack-clone
   ```

2. **Install Python dependencies**

   ```
   pip install -r requirements.txt
   ```

3. **Start Flask Application**

   ```
   python app.py
   ```

Note: `colab-challenge-be` should be associated with the front end that can be cloned from this repository [`colab-challenge-fe`](https://github.com/thuytrantkt/colab-challenge-fe). Please follow README in that repository to setup front end and run the server.
