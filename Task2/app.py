import gradio as gr

def companyChat(company_name, chat_history):
  from langchain.chains import ConversationalRetrievalChain
  from langchain_community.retrievers import KayAiRetriever
  from langchain_anthropic import ChatAnthropic
  model = ChatAnthropic(
        model_name="claude-3-sonnet-20240229"
    )
  retriever = KayAiRetriever.create(
        dataset_id="company", data_types=["10-K"], num_contexts=10
    ) 
  qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)
  company = company_name
  outputs = []
  chat_history = []
  questions = [
    f"Summarize the {company}'s financial performance over the past years, including revenue growth, profitability (net income), and margins. In English",
    f"Identify and analyze {company}'s earnings per share (EPS diluted and basic), Calculate Return on equity (ROE) and Debt-to-Equity ratio For past few years. In English",
    f"Add bullet points for main risks identified by {company} in its 10-K filing. In English" ]
  for question in questions:
      result = qa({"question": question, "chat_history": chat_history})
      chat_history.append((question, result["answer"]))
      outputs.append(result["answer"])  # Append both answers to a list
  return outputs  # Return the list of both answers

# Define the interface with inputs and outputs
interface = gr.Interface(
  fn=companyChat,
  inputs=gr.Textbox(label="Company Name or Ticker"),
  outputs=[gr.Textbox(label="Company's financial performance over the past years"), gr.Textbox(label="Company's earnings per share (EPS), return on equity (ROE), and debt-to-equity ratio For past few years"), gr.Textbox(label="Main risks identified in 10-K filing")],
  title="Insights on 10K Filings",
  description="Get Insights right from the 10K Filings submitted by the company",
  theme="soft",
  examples=["APPL", "NVDA", "MSFT"],
  cache_examples=True,
  clear_btn="Clear",
)

interface.launch()
