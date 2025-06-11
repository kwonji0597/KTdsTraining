# 실행 : python .\00.RAG.app.py (python .\Tab키 눌러서 파일 찾는다)
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

def main():
    os.system('cls' if os.name == 'nt' else 'clear') # 리눅스와 맥에서는 'clear' 지만 윈도우면 cls 라서 if문 해줌
    load_dotenv() #환경변수 읽어들이는 작업

    # Get environment variables
    openai_endpoint = os.getenv("OPENAI_ENDPOINT")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    chat_model = os.getenv("CHAT_MODEL")
    embedding_model = os.getenv("EMBEDDING_MODEL")
    search_endpoint=os.getenv("SEARCH_ENDPOINT")
    search_api_key=os.getenv("SEARCH_API_KEY")
    index_name = os.getenv("INDEX_NAME")
    
    # Initialize Azure OpenAI client
    chat_client = AzureOpenAI(
        api_version="2024-12-01-preview",
        azure_endpoint=openai_endpoint,
        api_key=openai_api_key
    )

    # Initialize prompt with system message
    prompt = [
        {
            "role": "system",
            "content": "You are a travel assistant that provides information on travel service available from Margie's Travel."
        },
    ]

    while True: #안에있는 부분은 계속 반복적으로 돔
        input_text = input("Enter your question (or type 'exit' to quit): ")

        # 사용자가 exit 입력하면 빠져나옴
        if input_text.lower() == "exit":    #lower() => 대문자도 소문자로. 비교 구문은 == 두개 들어감.
            print("Exiting the application.")
            break
        elif input_text.strip() == "":      # strip() : 단어 앞뒤 공백 제거
            print("Please enter a valid question.")
            continue
    
        # Add user input to the prompt
        prompt.append({"role": "user", "content": input_text})  # append =>위에 시스템 메세지에  user 메세지 추가

        # Additional parameters to apply RAG pattern using the AI Search index
        # RAG를 위한 파라메터 만들기
        rag_params = {
            "data_sources": [
                {
                    # he following params are used to search the index
                    "type": "azure_search",
                    "parameters": {
                        "endpoint": search_endpoint,
                        "index_name": index_name,
                        "authentication": {
                            "type": "api_key",
                            "key": search_api_key,
                        },
                        # The following params are used to vectorize the query
                        "query_type": "vector",
                        "embedding_dependency": {
                            "type": "deployment_name",
                            "deployment_name": embedding_model,
                        },
                    }
                }
            ],
        }
        
        # Submit the chat request with RAG parameters
        #결과 도출(response)
        response = chat_client.chat.completions.create(
            model=chat_model,   # 대화형 모델 : gpt-4-0-mini
            messages=prompt,    #프롬프트 -> 메시지에 넣음
            #rag_parameters=rag_params # 만든 RAG를 위한 파라메터 담아줌            
            extra_body=rag_params   # 만든 RAG를 위한 파라메터 담아줌  (rag_parameters 가 예전파라메터라 바꿈.)
        )

        #RAG에서 나온 결과 completion 담아주고 
        completion = response.choices[0].message.content
        print(completion)   # 프린트

        # Add the response to the chat history
        # 마지막 completion 결과까지 append
        prompt.append({"role": "assistant", "content": completion})


# main 함수명 main
if __name__ == "__main__":
    main()