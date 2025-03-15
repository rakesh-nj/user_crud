## steps to run
### 1.Clone this repo 
check top right side , code -> clone -> copy the url and paste with git clone <copied_url>
### 2.create virtual environment
```bash
python3 -m venv .venv # on linux / mac
```
### 3. activate virtual environment
```bash
source .venv/bin/activate
```
### 4. install dependencies
```bash
pip install -r requirements.tx
```
### 5. run 
```bash
uvicorn main:app --reload
```
