# -Rescursive character text splitting
# -It will follow the philospohy that any text follow a inherent structure i.e we organize a text into paragraph, sentences, words . based on Hirarchy of structuring it will try to split the text



from langchain.text_splitter import RecursiveCharacterTextSplitter

text = '''
Generative AI relies on sophisticated machine learning models called deep learning models algorithms that simulate the learning and decision-making processes of the human brain. These models work by identifying and encoding the patterns and relationships in huge amounts of data, and then using that information to understand users' natural language requests or questions and respond with relevant new content.

AI has been a hot technology topic for the past decade, but generative AI, and specifically the arrival of ChatGPT in 2022, has thrust AI into worldwide headlines and launched an unprecedented surge of AI innovation and adoption. Generative AI offers enormous productivity benefits for individuals and organizations, and while it also presents very real challenges and risks, businesses are forging ahead, exploring how the technology can improve their internal workflows and enrich their products and services. According to research by the management consulting firm McKinsey, one third of organizations are already using generative AI regularly in at least one business function.¹ Industry analyst Gartner projects more than 80 of organizations will have deployed generative AI applications or used generative AI application programming interfaces (APIs) by 2026.2

'''


splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 0

)

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks)