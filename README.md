# Deployment Guide Using Streamlit

### Step-by-step Streamlit Deployment Guide

> Ref: Streamlit guide [Streamlit Crash Course: From Zero to Data App](https://www.youtube.com/watch?v=d7fnzDQ5qM8)

[![Streamlit Crash Course: From Zero to Data App](https://img.youtube.com/vi/d7fnzDQ5qM8/0.jpg)](https://www.youtube.com/watch?v=d7fnzDQ5qM8)

**Step 1:** Create the _Virtual Environment_ by running the below command in the terminal

```
py -m vent .venv
```

**Step 2:** Avtivate the Environment run below command in the terminal

```
.venv/Scripts/activate
```

**Step 3:** _Install **Streamlit** library_ run below command in the terminal

```
pip install streamlit
```

**Step 4:** Import the Streamlit library into main app file (e.g. streamlit_app.py)

```
import streamlit as st
```

> Your main app file should contain other necessary code to run the ML model

**Step 5:** Run the _Streamlit Server_ from terminal locally

```
streamlit run streamlit_app.py
```

> This will start the server and open in browser with this default URL: [http://localhost:8501/](http://localhost:8501/)

**Step 6:** Deploy the app to _Community Cloud_
Open this link: [https://streamlit.io/cloud](https://streamlit.io/cloud) and create Free account then login

**Step 7:** Click on _Creare app_ button

> 1.a. Choose _Deploy a public app from template_

> 1.b. Select _Blank app_ from left side panel

> 1.c. Give a name of your GitHub repository (This will create a new repo in youe HitHub account)

> 1.d. Give desired _App URL_ (optional)

> 1.e. Click _Deploy_ button (This will create the repo and open the url in the browser)

> 1.f. Clone the repo locally -> change _streamlit_app.py_ based on your requirement

> 1.g. Commit and push your changes

For more practing checkout this [30 days Streamlit challange](http://30days.streamlit.app/)
