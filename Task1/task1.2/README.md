# FSIL-Assignment Task 1.2: Generating Insights from 10K filings


## Setting up the API Keys

```python
import os
os.environ["KAY_API_KEY"] = <API KEY>
os.environ["ANTHROPIC_API_KEY"] = <API KEY>
```

## LLMs Used
1. Anthropic Claude 3
2. Kay AI

## Insights

1. Financial Performance of the Company, Revenue Growth, Profitability and Margin. 
- Analyzing financial performance of the company will help in Investment Decision Making.
<br>

2. Company's Earning per share (EPS), Return on Equity (RoE) and Debt-to-Equity Ratio
-  Users can gain a comprehensive understanding of the company's profitability, efficiency in utilizing equity capital, and its financial risk exposure by analyzing EPS, RoE, and debt-to-equity ratio.
<br>

3. Risk Analysis of the Company
- Users can identify potential vulnerabilities, anticipate challenges, and make informed decisions to mitigate risks and protect their investments.
<br>

## Rate Limit
5 Requests/per minute. Currently Anthropic 3 is running on a Free Tier ($5 credit). 
