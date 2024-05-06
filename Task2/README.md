
# FSIL-Task 2: Construct and Deploy Simple App

`Get10KInsights` is a web-based interface to get insights about a company from its 10K filing reports, the retrival is done with Kay.ai API and Athropic Claude 3 API by using Langchain as a Framework.

## Tech Stack
1. Built using `Gradio`.
2. Deployed on [`HuggingFace Spaces`](https://huggingface.co/spaces/prathameshdalal/Get10KInsights)

## Context Retrivers
1. Kay AI
2. Anthropic Claude 3


# Useage

## Method 1: HuggingFace Spaces Interface

The App is hosted on [`HuggingFace Spaces`](https://huggingface.co/spaces/prathameshdalal/Get10KInsights). 

1. To get insights about a particular company. <br>
   *Enter Company Name or Ticker* in the Input Text-Box

2. Few Examples are stored in the example section of the [page](https://huggingface.co/spaces/prathameshdalal/Get10KInsights). <br>
   *Click on the Ticker to view the example insights*

<hr> 

## Method 2: API Endpoints

In Order to get the insights using API endpoints, there is some setup which needs to be done. <br>
<br>
Install the gradio client.

```bash
$ pip install gradio_client
```

### api_name: /predict

```python
from gradio_client import Client

client = Client("prathameshdalal/Get10KInsights")
result = client.predict(
		company_name="APPL",
		api_name="/predict"
)
print(result)
```
### Accepts 1 parameter:

#### ``company_name`` *str* **Required**

The input value that is provided in the "Company Name or Ticker" Textbox component.

### Returns 3 elements

[0] str **"Company's financial performance over the past years"** <br>

[1] str **"Company's earnings per share (EPS), return on equity (ROE), and debt-to-equity ratio For past few years"** <br>

[2] str **"Main risks identified in 10-K filing"** <br>

# Demo 

https://github.com/PrathameshDalal/FSIL-Assignment/assets/78019189/ed729a6f-f316-46b2-8514-5baa3918982c


### Response Time 
Average Response time to retrive the insights is around 40s.

### Useage & Rate-Limit
Currently the Anthropic Claude 3 is hosted on a Free Tier with $5 Credit with a rate-limit of 5 Requests/per minute.
