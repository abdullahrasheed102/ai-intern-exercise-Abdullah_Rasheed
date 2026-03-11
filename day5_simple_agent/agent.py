import os
from dotenv import load_dotenv
import google.generativeai as genai
from tools import calculator

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def decide_tool(query):
    prompt = f"""
You are an AI agent.

User question: {query}

Available tools:
- calculator → performs mathematical calculations

If the question requires math respond exactly with:
TOOL: calculator

Otherwise respond exactly with:
TOOL: none
"""

    response = model.generate_content(prompt)
    return response.text.strip()


def extract_expression(query):
    prompt = f"""
Extract ONLY the mathematical expression from the following question.

Question:
{query}

Return only the expression.
Example:
Input: What is 25 * 8?
Output: 25 * 8
"""
    response = model.generate_content(prompt)
    return response.text.strip()


def generate_final_answer(query, tool_result):
    prompt = f"""
User question:
{query}

Tool result:
{tool_result}

Write a helpful final answer for the user.
"""
    response = model.generate_content(prompt)
    return response.text.strip()


def run_agent(query):

    tool_decision = decide_tool(query)

    if "calculator" in tool_decision.lower():

        expression = extract_expression(query)

        result = calculator(expression)

        final_answer = generate_final_answer(query, result)

        return {
            "query": query,
            "tool": "calculator",
            "answer": final_answer
        }

    else:

        response = model.generate_content(query)

        return {
            "query": query,
            "tool": "none",
            "answer": response.text
        }


def main():

    with open("queries.txt", "r") as f:
        queries = f.readlines()

    output_lines = []

    for q in queries:
        q = q.strip()

        result = run_agent(q)

        output = f"""Query: {result['query']}
Tool used: {result['tool']}
Answer:
{result['answer']}
---
"""

        print(output)
        output_lines.append(output)

    with open("results.txt", "w") as f:
        f.writelines(output_lines)


if __name__ == "__main__":
    main()