from typing import Optional

from fastapi import FastAPI
from dotenv import load_dotenv

import google.generativeai as palm
load_dotenv()

palm.configure(api_key=palm)

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}
context = ""
examples = [
  [
    "What does &ai provides?",
    "And ai is a platform to integrate machine learning plugins, it can make any business ai ready in 10 mins"
  ],
  [
    "What are the products offered by &ai",
    "It can help us develop asweosme products and services of AI"
  ],
  [
    "What is the pricing model of &ai",
    "all AI services are free for first 3 months"
  ],
  [
    "Is &ai product based or service based company",
    "&ai is a product-based company. They offer a platform that allows businesses to integrate machine learning plugins into their existing products and services. This can help businesses to improve their products and services, and to create new products and services that are powered by artificial intelligence.\r\n\r\n&ai's platform is easy to use and can be integrated with any type of product or service. The platform includes a library of machine learning plugins that can be used to solve a variety of problems, such as image recognition, natural language processing, and machine translation.\r\n\r\n&ai's platform is a valuable tool for businesses that want to improve their products and services with artificial intelligence. The platform is easy to use and can be integrated with any type of product or service. The platform includes a library of machine learning plugins that can be used to solve a variety of problems."
  ]
]
messages = [
  "hi",
  "Hi there! How can I help you today?",
  "who are you?",
  "I am a large language model, also known as a conversational AI or chatbot trained to be informative and comprehensive. I am trained on a massive amount of text data, and I am able to communicate and generate human-like text in response to a wide range of prompts and questions. For example, I can provide summaries of factual topics or create stories.",
  "what is and ai",
  "&ai is a company that provides a platform for businesses to integrate machine learning into their products and services. The company's platform allows businesses to create and deploy machine learning models without any coding or machine learning expertise. &ai's platform is used by businesses in a variety of industries, including retail, healthcare, and finance.\r\n\r\n&ai was founded in 2016 by two former Google employees, Ilya Sutskever and Dario Amodei. The company is headquartered in San Francisco, California.\r\n\r\n&ai's platform is based on the company's proprietary machine learning technology, which is called &ai Core. &ai Core is a suite of machine learning algorithms that can be used to solve a variety of problems, including image recognition, natural language processing, and machine translation.\r\n\r\n&ai's platform is easy to use and can be integrated with any type of product or service. The platform includes a library of machine learning models that can be used to solve a variety of problems. Businesses can also use &ai's platform to create their own machine learning models.\r\n\r\n&ai's platform is a valuable tool for businesses that want to improve their products and services with artificial intelligence. The platform is easy to use and can be integrated with any type of product or service. The platform includes a library of machine learning models that can be used to solve a variety of problems."
]
messages.append("NEXT REQUEST")
response = palm.chat(
  **defaults,
  context=context,
  examples=examples,
  messages=messages
)
print(response.last) # Response of the AI to your most recent request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": response.last}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
