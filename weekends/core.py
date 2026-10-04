import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()

class Movie(BaseModel):
  title: str
  release_year: Optional[int]
  genre: List[str]
  director: Optional[str]
  cast: List[str]
  rating: Optional[float]
  summary: str

model = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
)

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """\
You are an expert assistant that extracts useful information from movie paragraphs.
{format_instructions}
""",
        ),
        ("human", "{paragraph}"),
    ]
)

para = input("Give your paragraph: ")

final_prompt = prompt.invoke(
  {"paragraph": para, "format_instructions": parser.get_format_instructions()}
)
response = model.invoke(final_prompt)
movie_data = parser.parse(response.text)
print(movie_data)
